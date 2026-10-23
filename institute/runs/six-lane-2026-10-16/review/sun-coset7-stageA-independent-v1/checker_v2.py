#!/usr/bin/env python3
"""sun-coset7 Stage A independent checker, version 2 (Python standard library only).

Written only from the frozen definition texts
  README.md               2a6d6d6e1dadbad522c8c8f9322c17eae719fb01fe373e6b1caf8c40cadc3fd1
  rules-k7-v1.md          77b9afec448ab44605b9ee513778bffd3e40aa9157807e8402f5488330e73cee
  rules-k7-addendum-v1.md fb2c306b17a258181bb770c7c6c38585da77c0e312c68463cee7dc0f15fd1066
  CERT-FORMAT-k7-v1.md    2c0e483011a0ea3aace670da4b9a200ae333e676682e0e10fb47d2e584401545
and the parent coverage clarification (CERT-FORMAT s5, last line, read as "sufficient").
No producer code is imported, copied or executed.  Producer profile tuples, canonical codes,
signatures, LP keys and counts are serialisations compared with values recomputed here; they
never decide coverage.

Coverage design
  * Own enumeration of every admissible capped profile tuple, own role-preserving orbit action,
    and a check that the capped image of the index family of addendum A3 (arbitrary valuations)
    lies inside that enumeration.
  * Every capped coordinate stands for the interval [cap, infinity); every quantity a rule uses
    must be determined on that interval (CAP checked per instance, fail closed).
  * Full re-walk of the alpha tree of every orbit representative, mirroring CERT-FORMAT s2:
    T on completed triangles; VFC on the full assigned star at i and at j (degree >= 3), decided
    by re-verifying every q with recomputed LP keys against the stored exact duals (vfc_killed
    is only cross-checked); then K-partial.
  * Every reached leaf class must have exactly one leaf line whose witness verifies (PB, or RPLP
    with every q, every column and every allowed subset recomputed).  A reached class without a
    verified line is reported, and an independent search (K, Ppair, PB, VFC on every N' with
    |N'| >= 3, each re-verified) is recorded for it; classes still uncovered must be SURVIVE lines.

Commands
  all     --lane L --out F                          pin audit + X1, MSP45, CORE5 + controls
  verify  --universe U --input-dir D --out F        one universe directory (no pins)
Exit codes: 0 COMPLETE_VALID, 1 INVALID, 2 INCOMPLETE, 3 UNKNOWN (stopped), 4 NOT_STARTED,
5 internal error.
v2 differs from v1 (2676c7d5...afcb2) only in the terminal decision/publication/exit handling
(_finish): a stop or SIGTERM seen before the decision gives UNKNOWN/3; one seen during or after
serialisation, or a publication error, creates <out>.CANCELLED.json and a nonzero exit; a SIGTERM
after the last check ends the process by the signal.  A result counts only on a normal exit with
its recorded exit_code and no marker.
"""

import argparse
import gzip
import hashlib
import io
import itertools
import json
import math
import os
import platform
import re
import resource
import signal
import sys
import time
from fractions import Fraction as Fr

VERSION = 'sun-coset7-stageA-independent-checker-v2'
PRIMES = (2, 3, 5)
CAPS = (4, 2, 2)              # profile = (min(v2,4), min(v3,2), min(v5,2)), rules-k7-v1 s4
INF = 1 << 40                 # +infinity in valuation intervals
ADMISSION_FREE = 12_200_000_000 + 16 * 1024 * 1024
INFLIGHT_FLOOR = 12_000_000_000
RSS_LIMIT = 1 << 30
SELF_BUDGET = 1800.0
MAX_DECOMPRESSED = 64 * 1024 * 1024
MAX_EXAMPLES = 25
RUN_FILES = ('run.json', 'survivors.json', 'vfc_killed.json.gz', 'lp_duals.json.gz', 'leaves.jsonl.gz')
HASHED_OUTPUTS = ('leaves.jsonl.gz', 'vfc_killed.json.gz', 'lp_duals.json.gz', 'survivors.json')

FROZEN_TEXTS = {
    'README.md': '2a6d6d6e1dadbad522c8c8f9322c17eae719fb01fe373e6b1caf8c40cadc3fd1',
    'rules-k7-v1.md': '77b9afec448ab44605b9ee513778bffd3e40aa9157807e8402f5488330e73cee',
    'rules-k7-addendum-v1.md': 'fb2c306b17a258181bb770c7c6c38585da77c0e312c68463cee7dc0f15fd1066',
    'CERT-FORMAT-k7-v1.md': '2c0e483011a0ea3aace670da4b9a200ae333e676682e0e10fb47d2e584401545',
}
RECEIPT_REL = 'evidence/stageA-RECEIPT.md'
RECEIPT_SHA = '90906aa60ac3026317af164069d2c0e22f825fc776cf789d4507d1445db4657c'
ENGINE_REL = 'code/core7_engine_v1.py'
ENGINE_SHA = 'e7b4f039ba02c9e8ab5c39579c0d21d3ce4e1d3aba13ec2813129eda67a4288d'
CONTROLS_PIN = 'stageA-CONTROLS/controls.json'
FREEZE_RECORDS = ('evidence/freeze-v1.sha256', 'evidence/addendum-v1.sha256',
                  'evidence/certformat-v1.sha256', 'evidence/rules-addendum-v1.sha256')

STOP = {'flag': False, 'why': None}


def _on_sigterm(signum, frame):
    STOP['flag'] = True
    STOP['why'] = 'SIGTERM'


class CapError(Exception):
    pass


class Reject(Exception):
    def __init__(self, code, detail=''):
        super().__init__(code, detail)
        self.code = code
        self.detail = str(detail)[:400]


class Stopped(Exception):
    pass


# ----------------------------------------------------------------------------- resources

class Guard:
    def __init__(self, path, budget=SELF_BUDGET):
        self.path = path
        self.t0 = time.monotonic()
        self.budget = budget
        self.last = -1e18
        self.min_free = None
        self.max_rss = 0
        self.samples = 0
        self.ticks = 0

    def free(self):
        st = os.statvfs(self.path)
        return st.f_bavail * st.f_frsize

    def rss(self):
        r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        return r if sys.platform == 'darwin' else r * 1024

    def sample(self):
        self.samples += 1
        self.last = time.monotonic()
        f = self.free()
        self.min_free = f if self.min_free is None else min(self.min_free, f)
        r = self.rss()
        self.max_rss = max(self.max_rss, r)
        if not STOP['flag']:
            if f < INFLIGHT_FLOOR:
                STOP.update(flag=True, why='statvfs free %d below in-flight floor %d' % (f, INFLIGHT_FLOOR))
            elif r > RSS_LIMIT:
                STOP.update(flag=True, why='peak RSS %d above %d' % (r, RSS_LIMIT))
            elif self.last - self.t0 > self.budget:
                STOP.update(flag=True, why='self budget %d s exceeded' % self.budget)

    def tick(self):
        self.ticks += 1
        if (self.ticks & 1023) == 0 and time.monotonic() - self.last >= 2.0:
            self.sample()
        if STOP['flag']:
            raise Stopped(STOP['why'])

    def report(self):
        return {'statvfs_samples': self.samples, 'min_free_bytes': self.min_free,
                'peak_rss_bytes': self.max_rss, 'elapsed_seconds': round(time.monotonic() - self.t0, 3),
                'stop': STOP['why']}


# ----------------------------------------------------------------------------- parsing

def _pairs_hook(pairs):
    d = {}
    for k, v in pairs:
        if k in d:
            raise Reject('JSON_DUPLICATE_KEY', k)
        d[k] = v
    return d


def _float_hook(s):
    raise Reject('JSON_FLOAT_FORBIDDEN', s)


def _const_hook(s):
    raise Reject('JSON_CONSTANT_FORBIDDEN', s)


class FloatToken(str):
    """A JSON float kept as its literal text; tolerated only at whitelisted metadata paths."""


def _check_floats(o, path, allowed):
    if isinstance(o, FloatToken):
        if path not in allowed:
            raise Reject('JSON_FLOAT_FORBIDDEN', path)
    elif isinstance(o, dict):
        for k, v in o.items():
            _check_floats(v, path + (k,), allowed)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            _check_floats(v, path + (i,), allowed)


def strict_loads(text, float_paths=()):
    """Duplicate keys, NaN/Infinity and floats rejected; floats only at the given metadata paths."""
    hook = FloatToken if float_paths else _float_hook
    try:
        obj = json.loads(text, object_pairs_hook=_pairs_hook, parse_float=hook, parse_constant=_const_hook)
    except Reject:
        raise
    except (ValueError, RecursionError) as e:
        raise Reject('JSON_SYNTAX', e)
    if float_paths:
        _check_floats(obj, (), set(float_paths))
    return obj


RAT_RE = re.compile(r'-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?\Z')


def parse_rat(s):
    if not isinstance(s, str) or not RAT_RE.match(s):
        raise Reject('BAD_RATIONAL', s)
    return Fr(s)


def is_int(x):
    return isinstance(x, int) and not isinstance(x, bool)


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def read_bytes(path):
    with open(path, 'rb') as f:
        return f.read()


def gunzip(b):
    try:
        with gzip.GzipFile(fileobj=io.BytesIO(b)) as f:
            out = f.read(MAX_DECOMPRESSED + 1)
    except (OSError, EOFError) as e:
        raise Reject('GZIP_BAD', e)
    if len(out) > MAX_DECOMPRESSED:
        raise Reject('GZIP_TOO_LARGE')
    return out


def utf8(b):
    try:
        return b.decode('utf-8')
    except UnicodeDecodeError as e:
        raise Reject('UTF8_BAD', e)


# ----------------------------------------------------------------------------- arithmetic

def vp(n, p):
    if not is_int(n) or n <= 0:
        raise ValueError(n)
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c


def lcm(a, b):
    return a // math.gcd(a, b) * b


def ival(c, t):
    return (c, INF) if c >= CAPS[t] else (c, c)


def iadd(a, c):
    return (a[0] + c, INF if a[1] >= INF else a[1] + c)


def imin(a, b):
    return (min(a[0], b[0]), min(a[1], b[1]))


def imax(a, b):
    return (max(a[0], b[0]), max(a[1], b[1]))


def ispoint(a):
    return a[0] == a[1]


def bits(m):
    out = []
    x = 0
    while m:
        if m & 1:
            out.append(x)
        m >>= 1
        x += 1
    return out


def popcount(m):
    return bin(m).count('1')


def cap_profile(n):
    return tuple(min(vp(n, p), CAPS[t]) for t, p in enumerate(PRIMES))


def gcd_interval(pi, pj):
    lo, hi = 1, 1
    for t, p in enumerate(PRIMES):
        m = imin(ival(pi[t], t), ival(pj[t], t))
        lo *= p ** m[0]
        hi = None if (hi is None or m[1] >= INF) else hi * p ** m[1]
    return lo, hi


def sig_str(sig):
    return ';'.join(','.join(str(x) for x in e) for e in sig)


def code_str(code):
    return ''.join(str(x) for x in code)


# ----------------------------------------------------------------------------- issues

class Issues:
    def __init__(self):
        self.items = {}

    def add(self, code, severity, detail=None):
        rec = self.items.get(code)
        if rec is None:
            rec = self.items[code] = {'severity': severity, 'count': 0, 'examples': []}
        if severity == 'INVALID' or (severity == 'INCOMPLETE' and rec['severity'] == 'NOTE'):
            rec['severity'] = severity
        rec['count'] += 1
        if detail is not None and len(rec['examples']) < MAX_EXAMPLES:
            rec['examples'].append(detail)

    def severities(self):
        return {r['severity'] for r in self.items.values()}

    def verdict(self):
        s = self.severities()
        if 'INVALID' in s:
            return 'INVALID'
        if 'INCOMPLETE' in s:
            return 'INCOMPLETE'
        return 'COMPLETE_VALID'


# ----------------------------------------------------------------------------- one pattern

class Pat:
    """A capped profile tuple with interval semantics; alpha is passed as a k x k matrix."""

    def __init__(self, prof):
        self.k = k = len(prof)
        self.prof = tuple(tuple(p) for p in prof)
        self.val = [[ival(self.prof[i][t], t) for t in range(3)] for i in range(k)]
        self.g = [[0] * k for _ in range(k)]
        for i in range(k):
            for j in range(i + 1, k):
                g = 1
                for t, p in enumerate(PRIMES):
                    m = imin(self.val[i][t], self.val[j][t])
                    if not ispoint(m):
                        raise CapError('gcd undetermined at pair %d,%d' % (i, j))
                    g *= p ** m[0]
                self.g[i][j] = self.g[j][i] = g
        self.E = [(i, j) for i in range(k) for j in range(i + 1, k)]
        self.eidx = {e: n for n, e in enumerate(self.E)}
        self.nbrs_at = []
        for t in range(len(self.E)):
            nb = [[] for _ in range(k)]
            for (x, y) in self.E[:t + 1]:
                nb[x].append(y)
                nb[y].append(x)
            self.nbrs_at.append([sorted(l) for l in nb])
        self._fac = {}
        self._tpass = {}
        self._link = {}

    def factor(self, x, y, z, a):
        """alpha_xy / gcd(alpha_xy, ell_z) with gamma_z = lcm(g_xz, g_yz) (rules L1, CERT s3)."""
        key = (min(x, y), max(x, y), z, a)
        r = self._fac.get(key)
        if r is None:
            gam = lcm(self.g[x][z], self.g[y][z])
            d = 1
            for t, p in enumerate(PRIMES):
                va = vp(a, p)
                l = iadd(self.val[z][t], -vp(gam, p))
                if l[0] < 0:
                    raise CapError('negative ell valuation')
                if va <= l[0]:
                    m = va
                elif ispoint(l):
                    m = l[0]
                else:
                    raise CapError('tau_min factor undetermined (%d,%d;%d) alpha=%d' % (x, y, z, a))
                d *= p ** m
            r = a // d
            self._fac[key] = r
        return r

    def tau_min(self, A, a, b, c):
        return lcm(lcm(self.factor(a, b, c, A[a][b]), self.factor(a, c, b, A[a][c])),
                   self.factor(b, c, a, A[b][c]))

    def tau_max(self, A, a, b, c):
        best = None
        for y, x, z in ((a, b, c), (b, a, c), (c, a, b)):
            gxy, gyz = self.g[x][y], self.g[y][z]
            axy, ayz, axz = A[x][y], A[y][z], A[x][z]
            gam = lcm(gxy, gyz)
            if axy * gyz <= ayz * gxy:
                num, den = axy, gxy
            else:
                num, den = ayz, gyz
            val = (gam * axz * num) // den
            if best is None or val < best:
                best = val
        return best

    def T_pass(self, A, a, b, c):
        key = (a, b, c, A[a][b], A[a][c], A[b][c])
        r = self._tpass.get(key)
        if r is None:
            r = self.tau_min(A, a, b, c) <= self.tau_max(A, a, b, c)
            self._tpass[key] = r
        return r

    def tmin3(self, A, x, y, z):
        a, b, c = sorted((x, y, z))
        return self.tau_min(A, a, b, c)

    def linked(self, A, v, i, j):
        """K1: U_vU_i in U_jU_i (apex i) or U_vU_j in U_iU_j (apex j)."""
        if i > j:
            i, j = j, i
        key = (v, i, j, A[v][i], A[v][j], A[i][j])
        r = self._link.get(key)
        if r is None:
            tm = self.tmin3(A, v, i, j)
            gi, gj, gij = self.g[i][v], self.g[j][v], self.g[i][j]
            r = (tm * gi >= lcm(gi, gij) * A[v][j] * A[i][v]) or (tm * gj >= lcm(gj, gij) * A[v][i] * A[j][v])
            self._link[key] = r
        return r

    def forced(self, A, v, a, b):
        """(F7): tau_min(v,a,b) g_va >= lcm(g_va, g_vb) alpha_ab alpha_va  =>  X_a subset X_b."""
        tm = self.tmin3(A, v, a, b)
        gva, gvb = self.g[v][a], self.g[v][b]
        return tm * gva >= lcm(gva, gvb) * A[a][b] * A[v][a]

    def pair_bounds(self, A, v, j, k):
        """(F6)/L4: lo <= mu(X_j cap X_k) <= hi on the grid u = 1/gcd(n_v, I_jk)."""
        Xj = Fr(A[v][j], self.g[v][j])
        Xk = Fr(A[v][k], self.g[v][k])
        den = 1
        for t, p in enumerate(PRIMES):
            m = imin(self.val[v][t], iadd(imax(self.val[j][t], self.val[k][t]), vp(A[j][k], p)))
            if not ispoint(m):
                raise CapError('u-grid undetermined at v=%d pair %d,%d' % (v, j, k))
            den *= p ** m[0]
        u = Fr(1, den)
        tm = self.tmin3(A, v, j, k)
        Lb = max(Fr(tm, lcm(self.g[v][j], self.g[v][k]) * A[j][k]), Xj + Xk - 1, Fr(0))
        lo = u * math.ceil(Lb / u)
        mn = min(Xj, Xk)
        hi = u * math.floor(mn / u)
        if hi == mn:
            ajk = Fr(A[j][k], self.g[j][k])
            j_in_k = Xj + ajk < 1          # K2: X_j subset X_k needs alpha_vj/g_vj + alpha_kj/g_kj < 1
            k_in_j = Xk + ajk < 1
            if Xj < Xk:
                barred = not j_in_k
            elif Xk < Xj:
                barred = not k_in_j
            else:
                barred = not (j_in_k and k_in_j)
            if barred:
                hi -= u
        return lo, hi, u

    def star_records(self, A, v, nb):
        recs = []
        for j in nb:
            g = self.g[v][j]
            vg = (vp(g, 2), vp(g, 3), vp(g, 5))
            bcap = tuple(self.prof[j][t] - vg[t] for t in range(3))
            bint = tuple(iadd(self.val[j][t], -vg[t]) for t in range(3))
            recs.append((g, A[v][j], bcap, bint))
        return recs

    def Kp(self, A, t):
        i, j = self.E[t]
        nbt = self.nbrs_at[t]
        for h in range(i):
            tri = (h, i, j)
            for v in tri:
                a, b = [x for x in tri if x != v]
                if not self.linked(A, v, a, b):
                    continue
                rest = [u for u in nbt[v] if u != a and u != b]
                for r in range(len(rest) + 1):
                    for extra in itertools.combinations(rest, r):
                        S = (a, b) + extra
                        good = True
                        for x, y in itertools.combinations(S, 2):
                            e = (x, y) if x < y else (y, x)
                            if self.eidx[e] > t or not self.linked(A, v, x, y):
                                good = False
                                break
                        if good and sum(Fr(A[u][v], self.g[u][v]) for u in S) >= 1:
                            return True
        return False


def alpha_matrix(pat, code):
    A = [[0] * pat.k for _ in range(pat.k)]
    for n, (i, j) in enumerate(pat.E):
        A[i][j] = A[j][i] = code[n]
    return A


# ----------------------------------------------------------------------------- VFC / duals

_ALLOWED = {}


def allowed_masks(dints):
    """All allowed position sets (hereditary definition, every subset checked; intervals)."""
    r = _ALLOWED.get(dints)
    if r is not None:
        return r
    m = len(dints)
    pg = {}
    for x in range(m):
        for y in range(x + 1, m):
            lo, hi = 1, 1
            for t, p in enumerate(PRIMES):
                iv = imin(dints[x][t], dints[y][t])
                lo *= p ** iv[0]
                hi = None if (hi is None or iv[1] >= INF) else hi * p ** iv[1]
            pg[(x, y)] = (lo, hi)
    good = {}
    for mask in range(1, 1 << m):
        mem = bits(mask)
        s = len(mem)
        if s < 2:
            continue
        val = False
        for x, y in itertools.combinations(mem, 2):
            lo, hi = pg[(x, y)]
            if lo >= s:
                val = True
                break
            if hi is None or hi >= s:
                val = None
        good[mask] = val
    out = []
    for mask in range(1 << m):
        if popcount(mask) <= 1:
            out.append(mask)
            continue
        verdict = True
        sub = mask
        while sub:
            if popcount(sub) >= 2:
                gv = good[sub]
                if gv is False:
                    verdict = False
                    break
                if gv is None:
                    verdict = None
            sub = (sub - 1) & mask
        if verdict is None:
            raise CapError('allowed-set test undetermined %r mask %d' % (dints, mask))
        if verdict:
            out.append(mask)
    r = tuple(out)
    _ALLOWED[dints] = r
    return r


def check_dual(y, coeffs, dints):
    """(R)/VFC-count: y >= 0, sum over every allowed T <= 1, sum coeff*y >= 1."""
    if len(y) != len(coeffs):
        return False, 'DUAL_LENGTH'
    for x in y:
        if x < 0:
            return False, 'DUAL_NEGATIVE'
    try:
        allowed = allowed_masks(dints)
    except CapError:
        return False, 'CAP_UNDETERMINED'
    for mask in allowed:
        if mask and sum(y[x] for x in bits(mask)) > 1:
            return False, 'DUAL_ALLOWED_SUM_GT_1'
    if sum(c * x for c, x in zip(coeffs, y)) < 1:
        return False, 'DUAL_OBJECTIVE_LT_1'
    return True, None


def lp_instance(recs, q):
    """Recomputed LP key (serialisation), objective coefficients and local valuation intervals."""
    ents = []
    for (g, a, bcap, bint), qx in zip(recs, q):
        fr = Fr(qx, g)
        vq = (vp(qx, 2), vp(qx, 3), vp(qx, 5))
        ser = (fr.numerator, fr.denominator, bcap[0] + vq[0], bcap[1] + vq[1], bcap[2] + vq[2])
        di = (iadd(bint[0], vq[0]), iadd(bint[1], vq[1]), iadd(bint[2], vq[2]))
        ents.append((ser, di, fr))
    ents.sort(key=lambda e: (e[0], e[1]))
    keystr = ';'.join('%d/%d,%d,%d,%d' % e[0] for e in ents)
    return keystr, tuple(e[2] for e in ents), tuple(e[1] for e in ents)


def local_dints(recs, q):
    out = []
    for (g, a, bcap, bint), qx in zip(recs, q):
        vq = (vp(qx, 2), vp(qx, 3), vp(qx, 5))
        out.append((iadd(bint[0], vq[0]), iadd(bint[1], vq[1]), iadd(bint[2], vq[2])))
    return tuple(out)


KEY_ENTRY_RE = re.compile(r'([1-9][0-9]*)/([1-9][0-9]*),([0-9]+),([0-9]+),([0-9]+)\Z')


def parse_key(s):
    if not isinstance(s, str) or not s:
        raise Reject('LP_KEY_MALFORMED', s)
    ents = []
    for part in s.split(';'):
        m = KEY_ENTRY_RE.match(part)
        if not m:
            raise Reject('LP_KEY_MALFORMED', s)
        ents.append(tuple(int(x) for x in m.groups()))
    return ents


class DualBook:
    def __init__(self, obj, iss):
        if not isinstance(obj, dict):
            raise Reject('LP_DUALS_NOT_OBJECT')
        self.y = {}
        self.value = {}
        self.ents = {}
        self.referenced = set()
        self._memo = {}
        for key, rec in obj.items():
            ents = parse_key(key)
            if ents != sorted(ents):
                iss.add('LP_KEY_NOT_SORTED', 'INVALID', key)
            for e in ents:
                if math.gcd(e[0], e[1]) != 1 or e[0] >= e[1]:
                    iss.add('LP_KEY_FRACTION_NONCANONICAL', 'INVALID', key)
                    break
            if not isinstance(rec, dict) or set(rec.keys()) != {'value', 'y'} or not isinstance(rec['y'], list):
                raise Reject('LP_DUAL_SCHEMA', key)
            self.y[key] = [parse_rat(s) for s in rec['y']]
            self.value[key] = parse_rat(rec['value'])
            self.ents[key] = ents

    def check(self, key, coeffs, dints):
        mk = (key, dints)
        r = self._memo.get(mk)
        if r is None:
            y = self.y.get(key)
            r = (False, 'DUAL_MISSING') if y is None else check_dual(y, coeffs, dints)
            self._memo[mk] = r
        return r

    def verify_stored(self, iss):
        bad = 0
        value_mismatch = 0
        for key, ents in self.ents.items():
            coeffs = tuple(Fr(e[0], e[1]) for e in ents)
            dints = tuple(((e[2], e[2]), (e[3], e[3]), (e[4], e[4])) for e in ents)
            ok, code = check_dual(self.y[key], coeffs, dints)
            if not ok:
                bad += 1
                iss.add('LP_DUAL_INVALID_STORED:' + code, 'INVALID', key)
            elif sum(c * x for c, x in zip(coeffs, self.y[key])) != self.value[key]:
                value_mismatch += 1
        if value_mismatch:
            iss.add('LP_DUAL_VALUE_FIELD_MISMATCH', 'NOTE', value_mismatch)
        return {'stored_keys': len(self.ents), 'stored_invalid': bad, 'value_field_mismatch': value_mismatch}


def verify_recs(recs, book):
    """Every q in prod [1, g-alpha] refuted by a stored exact dual at its recomputed key."""
    keys = []
    for q in itertools.product(*[range(1, r[0] - r[1] + 1) for r in recs]):
        keystr, coeffs, dints = lp_instance(recs, q)
        ok, code = book.check(keystr, coeffs, dints)
        if not ok:
            return False, [code, keystr, list(q)], keys
        keys.append(keystr)
    return True, None, keys


# ----------------------------------------------------------------------------- universes

ROLE_DOMAINS = {
    'C': ((1, 2, 3, 4), (1, 2), (0, 1, 2)),
    'D3': ((0,), (1, 2), (0, 1, 2)),
    'P1': ((1,), (0, 1, 2), (0, 1, 2)),
    'P4': ((2, 3, 4), (0, 1, 2), (0, 1, 2)),
    'Q4': ((2, 3, 4), (0, 1, 2), (0, 1, 2)),
}
UNIVERSES = {
    'X1': (('D3', 'D3', 'C', 'C', 'C'), {('D3', 'D3'): (3,), ('C', 'D3'): (3,), ('C', 'C'): (6,)}),
    'MSP45': (('P1', 'P4', 'P4', 'P4'), {('P1', 'P4'): (2,), ('P4', 'P4'): (4,)}),
    'CORE5': (('Q4',) * 5, {('Q4', 'Q4'): (4,)}),
}
# addendum A3: n_i = c_i r_i, r's pairwise coprime, the listed r's odd.
FAMILIES = {
    'X1': ((3, 3, 6, 6, 6), (0, 1)),
    'MSP45': ((2, 4, 4, 4), (0,)),
    'CORE5': ((4, 4, 4, 4, 4), ()),
}
EXPECTED = {
    'X1': {'labelled_profiles': 660, 'profile_orbits': 115, 'leaf_orbits': 157,
           'leaf_rule': {'PB': 130, 'RPLP': 27}},
    'MSP45': {'labelled_profiles': 567, 'profile_orbits': 135, 'leaf_orbits': 0, 'leaf_rule': {}},
    'CORE5': {'labelled_profiles': 1331, 'profile_orbits': 71, 'leaf_orbits': 0, 'leaf_rule': {}},
}


def rolekey(r1, r2):
    return tuple(sorted((r1, r2)))


def admissible_pair(pi, pj, allowed):
    lo, hi = gcd_interval(pi, pj)
    if hi is not None and lo == hi:
        return lo in allowed
    if lo > max(allowed):
        return False
    raise CapError('gcd interval undetermined %r %r' % (pi, pj))


def enumerate_admissible(roles, allowed_map):
    k = len(roles)
    doms = [list(itertools.product(*ROLE_DOMAINS[r])) for r in roles]
    out = []
    cur = []

    def rec(i):
        if i == k:
            out.append(tuple(cur))
            return
        for p in doms[i]:
            ok = True
            for j in range(i):
                key = rolekey(roles[j], roles[i])
                if key not in allowed_map:
                    raise Reject('ROLE_PAIR_UNDEFINED', key)
                if not admissible_pair(cur[j], p, allowed_map[key]):
                    ok = False
                    break
            if ok:
                cur.append(p)
                rec(i + 1)
                cur.pop()

    rec(0)
    return out


def family_image(name, B):
    coeffs, odd = FAMILIES[name]
    k = len(coeffs)
    base = [tuple(vp(c, p) for p in PRIMES) for c in coeffs]
    per_prime = []
    for t in range(3):
        vecs = set()
        cand = [tuple([0] * k)]
        for i in range(k):
            if t == 0 and i in odd:
                continue
            for v in range(1, B + 1):
                vec = [0] * k
                vec[i] = v
                cand.append(tuple(vec))
        for vec in cand:
            vecs.add(tuple(min(base[i][t] + vec[i], CAPS[t]) for i in range(k)))
        per_prime.append(vecs)
    img = set()
    for v2 in per_prime[0]:
        for v3 in per_prime[1]:
            for v5 in per_prime[2]:
                img.add(tuple((v2[i], v3[i], v5[i]) for i in range(k)))
    return img


def role_group(roles):
    k = len(roles)
    return [p for p in itertools.permutations(range(k)) if all(roles[p[i]] == roles[i] for i in range(k))]


def role_runs(roles):
    runs = []
    s = 0
    for i in range(1, len(roles) + 1):
        if i == len(roles) or roles[i] != roles[s]:
            runs.append((s, i))
            s = i
    return runs


def sorted_within_runs(t, runs):
    return all(t[x] <= t[x + 1] for (s, e) in runs for x in range(s, e - 1))


def profile_universe(name, iss):
    roles, allowed = UNIVERSES[name]
    k = len(roles)
    labelled = enumerate_admissible(roles, allowed)
    S = set(labelled)
    if len(S) != len(labelled):
        iss.add('ENUMERATION_DUPLICATES', 'INCOMPLETE', len(labelled) - len(S))
    img = family_image(name, 6)
    img_next = family_image(name, 7)
    if img != img_next:
        iss.add('FAMILY_IMAGE_NOT_STABLE', 'INCOMPLETE')
    not_covered = sorted(img - S)
    if not_covered:
        iss.add('FAMILY_PROFILE_NOT_IN_ENUMERATION', 'INCOMPLETE', [list(map(list, t)) for t in not_covered[:5]])
    beyond = sorted(S - img)
    if beyond:
        iss.add('ENUMERATION_BEYOND_FAMILY_IMAGE', 'NOTE', len(beyond))
    G = role_group(roles)
    runs = role_runs(roles)
    contiguous = len({roles[s] for (s, e) in runs}) == len(runs)
    reps, seen, sizes = [], set(), []
    for t in sorted(S):
        if t in seen:
            continue
        orb = {tuple(t[p[i]] for i in range(k)) for p in G}
        if not orb <= S:
            iss.add('ADMISSIBLE_SET_NOT_ROLE_INVARIANT', 'INCOMPLETE', list(map(list, t)))
        seen |= orb
        srt = [m for m in orb if sorted_within_runs(m, runs)]
        if len(srt) != 1:
            iss.add('REPRESENTATIVE_CONVENTION_FAILS', 'INCOMPLETE', list(map(list, t)))
            continue
        reps.append(srt[0])
        sizes.append(len(orb))
    fixed = sum(1 for p in G for t in S if tuple(t[p[i]] for i in range(k)) == t)
    burnside = fixed // len(G) if fixed % len(G) == 0 else None
    if burnside != len(reps) or sum(sizes) != len(S):
        iss.add('ORBIT_COUNT_INCONSISTENT', 'INCOMPLETE', [burnside, len(reps), sum(sizes), len(S)])
    exp = EXPECTED[name]
    if len(S) != exp['labelled_profiles'] or len(reps) != exp['profile_orbits']:
        iss.add('EXPECTED_PROFILE_COUNT_MISMATCH', 'NOTE', [len(S), len(reps)])
    max_allowed = max(max(v) for v in allowed.values())
    info = {'roles': list(roles), 'allowed_gcds': {'-'.join(k2): list(v) for k2, v in allowed.items()},
            'role_group_order': len(G), 'role_runs_contiguous': contiguous,
            'labelled_admissible': len(S), 'family_image_size': len(img), 'family_image_stable_B6_B7': img == img_next,
            'family_image_subset_of_enumeration': not not_covered, 'enumeration_minus_family': len(beyond),
            'profile_orbits': len(reps), 'burnside_orbits': burnside,
            'H3_max_gcd_le_6': max_allowed <= 6}
    return sorted(reps), G, info


def stab_maps(pat, G):
    maps = []
    for p in G:
        if all(pat.prof[p[i]] == pat.prof[i] for i in range(pat.k)):
            maps.append(tuple(pat.eidx[(min(p[i], p[j]), max(p[i], p[j]))] for (i, j) in pat.E))
    return maps


def canon_code(maps, alpha):
    best = None
    for m in maps:
        c = tuple(alpha[m[x]] for x in range(len(m)))
        if best is None or c < best:
            best = c
    return best


# ----------------------------------------------------------------------------- tree walk

def walk_rep(pat, book, killed_set, star_memo, enc, iss, guard, stats):
    k, E = pat.k, pat.E
    nE = len(E)
    A = [[0] * k for _ in range(k)]
    leaves = []

    def node(t):
        i, j = E[t]
        for a in range(1, pat.g[i][j]):
            guard.tick()
            stats['children'] += 1
            A[i][j] = A[j][i] = a
            closed = None
            for h in range(i):
                if not pat.T_pass(A, h, i, j):
                    closed = 'T'
                    break
            if closed is None:
                for v in (i, j):
                    nb = pat.nbrs_at[t][v]
                    if len(nb) < 3:
                        continue
                    stats['vfc_checks'] += 1
                    recs = pat.star_records(A, v, nb)
                    sig = tuple(sorted((r[0], r[1]) + r[2] for r in recs))
                    listed = sig in killed_set
                    if listed:
                        enc.add(sig)
                    mk = tuple(sorted(recs))
                    r = star_memo.get(mk)
                    if r is None:
                        ok_, why_, keys_ = verify_recs(list(mk), book)
                        if ok_:
                            book.referenced.update(keys_)
                        r = star_memo[mk] = (ok_, why_)
                    if r[0]:
                        if closed is None:
                            closed = 'VFC'
                        if not listed:
                            iss.add('VFC_REVERIFIED_STAR_NOT_LISTED', 'NOTE', sig_str(sig))
                    elif listed:
                        iss.add('VFC_LISTED_SIG_NOT_REVERIFIED:' + r[1][0], 'INVALID',
                                {'sig': sig_str(sig), 'key': r[1][1], 'q': r[1][2]})
            if closed is None and pat.Kp(A, t):
                closed = 'Kp'
            if closed is not None:
                stats['closed_' + closed] += 1
                continue
            if t == nE - 1:
                stats['leaves'] += 1
                leaves.append(tuple(A[x][y] for (x, y) in E))
            else:
                stats['open_internal'] += 1
                node(t + 1)
        A[i][j] = A[j][i] = 0

    node(0)
    return leaves


# ----------------------------------------------------------------------------- leaf witnesses

def verify_pb(pat, A, wit):
    if not (isinstance(wit, list) and len(wit) == 2):
        return 'PB_WITNESS_MALFORMED'
    v, S = wit
    if not is_int(v) or not 0 <= v < pat.k or not isinstance(S, list) or not S:
        return 'PB_WITNESS_MALFORMED'
    if not all(is_int(x) and 0 <= x < pat.k and x != v for x in S) or any(S[x] >= S[x + 1] for x in range(len(S) - 1)):
        return 'PB_WITNESS_MALFORMED'
    X = {j: Fr(A[v][j], pat.g[v][j]) for j in S}
    tot = sum(1 - X[j] for j in S)
    for j, kk in itertools.combinations(S, 2):
        lo, hi, u = pat.pair_bounds(A, v, j, kk)
        tot -= 1 - X[j] - X[kk] + hi
    return None if tot >= 1 else 'PB_SUM_LT_1'


def verify_rplp(pat, A, wit, book):
    if not (isinstance(wit, list) and len(wit) == 2):
        return 'RPLP_WITNESS_MALFORMED', None
    v, certs = wit
    if not is_int(v) or not 0 <= v < pat.k or not isinstance(certs, list):
        return 'RPLP_WITNESS_MALFORMED', None
    N = [u for u in range(pat.k) if u != v]
    n = len(N)
    recs = pat.star_records(A, v, N)
    Q = list(itertools.product(*[range(1, r[0] - r[1] + 1) for r in recs]))
    if len(certs) != len(Q):
        return 'RPLP_CERT_COUNT_MISMATCH', None
    pairs = list(itertools.combinations(range(n), 2))
    X = [Fr(A[v][u], pat.g[v][u]) for u in N]
    yhi, ylo = [], []
    for (a, b) in pairs:
        lo, hi, u = pat.pair_bounds(A, v, N[a], N[b])
        yhi.append(1 - X[a] - X[b] + hi)
        ylo.append(1 - X[a] - X[b] + lo)
    forced = [(a, b) for a in range(n) for b in range(n) if a != b and pat.forced(A, v, N[a], N[b])]
    Acols = [Am for Am in range(1, 1 << n) if all(((Am >> a) & 1) or not ((Am >> b) & 1) for (a, b) in forced)]
    pin = {Am: [pi for pi, (a, b) in enumerate(pairs) if (Am >> a) & 1 and (Am >> b) & 1] for Am in Acols}
    keys = []
    nP = nR = ncols = 0
    for q, cert in zip(Q, certs):
        if not (isinstance(cert, list) and len(cert) == 2 and isinstance(cert[0], str)):
            return 'RPLP_CERT_MALFORMED', None
        tag, payload = cert
        if tag == 'R':
            if not isinstance(payload, str):
                return 'RPLP_CERT_MALFORMED', None
            keystr, coeffs, dints = lp_instance(recs, q)
            if keystr != payload:
                return 'RPLP_R_KEY_MISMATCH', None
            ok, code = book.check(keystr, coeffs, dints)
            if not ok:
                return 'RPLP_R_' + code, None
            keys.append(keystr)
            nR += 1
        elif tag == 'P':
            if not isinstance(payload, list) or len(payload) != 2 * n + 2 * len(pairs):
                return 'RPLP_P_LENGTH', None
            vec = [parse_rat(s) for s in payload]
            ca, cb = vec[:n], vec[n:2 * n]
            cu, cl = vec[2 * n:2 * n + len(pairs)], vec[2 * n + len(pairs):]
            if any(x < 0 for x in cu) or any(x < 0 for x in cl):
                return 'RPLP_P_NEGATIVE_UL', None
            allowed = set(allowed_masks(local_dints(recs, q)))
            for Am in Acols:
                base = sum(cb[x] for x in bits(Am)) + sum(cl[pi] - cu[pi] for pi in pin[Am])
                Sm = Am
                while True:
                    if Sm == 0 or Sm in allowed:
                        ncols += 1
                        if base + sum(ca[x] for x in bits(Sm)) > 1:
                            return 'RPLP_P_COLUMN_VIOLATION', None
                    if Sm == 0:
                        break
                    Sm = (Sm - 1) & Am
            obj = (sum(ca[x] * Fr(q[x], recs[x][0]) for x in range(n))
                   + sum(cb[x] * (1 - X[x]) for x in range(n))
                   - sum(cu[pi] * yhi[pi] for pi in range(len(pairs)))
                   + sum(cl[pi] * ylo[pi] for pi in range(len(pairs))))
            if obj < 1:
                return 'RPLP_P_OBJECTIVE_LT_1', None
            nP += 1
        else:
            return 'RPLP_CERT_BAD_TAG', None
    book.referenced.update(keys)
    return None, {'v': v, 'q_count': len(Q), 'P': nP, 'R': nR, 'forced_pairs': len(forced),
                  'A_sets': len(Acols), 'columns_checked': ncols}


def fallback_kill(pat, A, book):
    """Independent search on a leaf: K, Ppair, PB, VFC on every N' with |N'| >= 3 (re-verified)."""
    k = pat.k
    for v in range(k):
        N = [u for u in range(k) if u != v]
        for r in range(2, len(N) + 1):
            for S in itertools.combinations(N, r):
                if all(pat.linked(A, v, x, y) for x, y in itertools.combinations(S, 2)) and \
                        sum(Fr(A[u][v], pat.g[u][v]) for u in S) >= 1:
                    return ['K', v, list(S)]
        hi = {}
        for j, kk in itertools.combinations(N, 2):
            lo_, hi_, u_ = pat.pair_bounds(A, v, j, kk)
            if lo_ > hi_:
                return ['Ppair', v, [j, kk]]
            hi[(j, kk)] = hi_
        for r in range(1, len(N) + 1):
            for S in itertools.combinations(N, r):
                X = {j: Fr(A[v][j], pat.g[v][j]) for j in S}
                tot = sum(1 - X[j] for j in S) - sum(1 - X[j] - X[kk] + hi[(j, kk)]
                                                     for j, kk in itertools.combinations(S, 2))
                if tot >= 1:
                    return ['PB', v, list(S)]
        for r in range(3, len(N) + 1):
            for Np in itertools.combinations(N, r):
                ok, why, keys = verify_recs(sorted(pat.star_records(A, v, list(Np))), book)
                if ok:
                    book.referenced.update(keys)
                    return ['VFC', v, list(Np)]
    return None


def parse_leaves(text, k, nE, iss):
    if text == '':
        return []
    if text == '\n':
        iss.add('LEAVES_EMPTY_FILE_IS_ONE_NEWLINE', 'NOTE', None)
        return []
    if not text.endswith('\n'):
        raise Reject('LEAVES_NO_TRAILING_NEWLINE')
    out = []
    code_re = re.compile('[1-9]{%d}' % nE)
    for n, line in enumerate(text[:-1].split('\n')):
        if line == '':
            raise Reject('LEAVES_BLANK_LINE', n)
        obj = strict_loads(line)
        if not isinstance(obj, dict) or set(obj.keys()) != {'prof', 'canon', 'rep', 'rule', 'witness'}:
            raise Reject('LEAF_LINE_SCHEMA', n)
        prof = obj['prof']
        if not (isinstance(prof, list) and len(prof) == k and
                all(isinstance(p, list) and len(p) == 3 and all(is_int(x) for x in p) for p in prof)):
            raise Reject('LEAF_LINE_PROF_SCHEMA', n)
        for f in ('canon', 'rep'):
            if not (isinstance(obj[f], str) and code_re.fullmatch(obj[f])):
                raise Reject('LEAF_LINE_CODE_SCHEMA', n)
        if obj['rule'] not in ('K', 'Ppair', 'PB', 'RPLP', 'SURVIVE'):
            raise Reject('LEAF_LINE_RULE', n)
        out.append(obj)
    return out


def process_leaves(pats, maps, reps_index, reached, lines, book, iss, guard):
    classes = {}
    for ri, lst in reached.items():
        for alpha in lst:
            classes.setdefault((ri, canon_code(maps[ri], alpha)), set()).add(alpha)
    line_of, verified, survive = {}, {}, set()
    rule_counts, verified_counts = {}, {}
    rplp_stats = {'q_total': 0, 'P': 0, 'R': 0, 'columns_checked': 0}
    for n, obj in enumerate(lines):
        guard.tick()
        prof = tuple(tuple(p) for p in obj['prof'])
        rule = obj['rule']
        ctx = {'line': n, 'prof': obj['prof'], 'canon': obj['canon'], 'rule': rule}
        ri = reps_index.get(prof)
        if ri is None:
            iss.add('LEAF_LINE_PROF_NOT_A_REPRESENTATIVE', 'INVALID', ctx)
            continue
        pat = pats[ri]
        rep = tuple(int(c) for c in obj['rep'])
        canon = tuple(int(c) for c in obj['canon'])
        if any(not 1 <= rep[x] <= pat.g[i][j] - 1 for x, (i, j) in enumerate(pat.E)):
            iss.add('LEAF_LINE_REP_ALPHA_OUT_OF_RANGE', 'INVALID', ctx)
            continue
        cc = canon_code(maps[ri], rep)
        if cc != canon:
            iss.add('LEAF_LINE_CANON_MISMATCH', 'INVALID', dict(ctx, recomputed=code_str(cc)))
            continue
        cls = (ri, canon)
        if cls in line_of:
            iss.add('LEAF_LINE_DUPLICATE_CLASS', 'INVALID', ctx)
            continue
        line_of[cls] = n
        rule_counts[rule] = rule_counts.get(rule, 0) + 1
        if cls not in classes:
            iss.add('LEAF_LINE_UNREACHED_CLASS', 'INVALID', ctx)
        elif rep not in classes[cls]:
            iss.add('LEAF_REP_NOT_A_REACHED_LABELLED_LEAF', 'NOTE', ctx)
        A = alpha_matrix(pat, rep)
        why = None
        try:
            if rule == 'PB':
                why = verify_pb(pat, A, obj['witness'])
            elif rule == 'RPLP':
                why, st = verify_rplp(pat, A, obj['witness'], book)
                if st:
                    rplp_stats['q_total'] += st['q_count']
                    rplp_stats['P'] += st['P']
                    rplp_stats['R'] += st['R']
                    rplp_stats['columns_checked'] += st['columns_checked']
            elif rule == 'SURVIVE':
                survive.add(cls)
                continue
            else:
                iss.add('UNSUPPORTED_LEAF_RULE_WITNESS_FORMAT:' + rule, 'INCOMPLETE', ctx)
                continue
        except CapError as e:
            iss.add('CAP_UNDETERMINED_AT_LEAF', 'INCOMPLETE', dict(ctx, err=str(e)))
            continue
        except Reject as e:
            why = 'WITNESS_MALFORMED:' + e.code
        if why is None:
            verified[cls] = rule
            verified_counts[rule] = verified_counts.get(rule, 0) + 1
        else:
            iss.add('LEAF_WITNESS_FAILED:' + why, 'INVALID', ctx)
    uncovered, fallback = [], []
    for cls in sorted(classes):
        if cls in verified:
            continue
        guard.tick()
        ri, code = cls
        ctx = {'prof': [list(p) for p in pats[ri].prof], 'canon': code_str(code)}
        try:
            how = fallback_kill(pats[ri], alpha_matrix(pats[ri], code), book)
        except CapError as e:
            how = None
            iss.add('CAP_UNDETERMINED_IN_FALLBACK', 'INCOMPLETE', dict(ctx, err=str(e)))
        if cls not in line_of:
            iss.add('LEAF_CLASS_MISSING_LINE', 'INCOMPLETE', dict(ctx, independent_kill=how))
        if how is not None:
            fallback.append(dict(ctx, independent_kill=how))
        elif cls not in survive:
            uncovered.append(ctx)
            iss.add('LEAF_CLASS_UNCOVERED', 'INCOMPLETE', ctx)
    listing = []
    for cls in sorted(classes):
        ri, code = cls
        listing.append({'rep': ri, 'prof': [list(p) for p in pats[ri].prof], 'canon': code_str(code),
                        'labelled_leaves': len(classes[cls]), 'line': line_of.get(cls),
                        'verified_rule': verified.get(cls)})
    return {'reached_classes': len(classes), 'reached_labelled_leaves': sum(len(s) for s in classes.values()),
            'lines': len(lines), 'line_rule_counts': rule_counts, 'verified_rule_counts': verified_counts,
            'classes_verified_by_line': sum(1 for c in classes if c in verified),
            'classes_killed_only_by_independent_search': len(fallback),
            'independent_search_examples': fallback[:MAX_EXAMPLES],
            'uncovered_classes': len(uncovered), 'survive_classes': len(survive),
            'uncovered_subset_of_SURVIVE': len(uncovered) == 0, 'rplp': rplp_stats, 'classes': listing}, survive


# ----------------------------------------------------------------------------- one universe

def verify_universe(name, indir, pins, guard):
    t0 = time.monotonic()
    iss = Issues()
    res = {'universe': name, 'input_dir': os.path.abspath(indir), 'inputs': {}}
    frontier = {'profile_reps_total': None, 'profile_reps_completed': 0, 'current_rep': None}
    res['frontier'] = frontier
    try:
        raw = {}
        for fn in RUN_FILES:
            b = read_bytes(os.path.join(indir, fn))
            raw[fn] = b
            h = sha256_bytes(b)
            res['inputs'][fn] = {'sha256': h, 'bytes': len(b)}
            if pins is not None:
                res['inputs'][fn]['pinned'] = pins.get(fn)
                if pins.get(fn) != h:
                    iss.add('INPUT_PIN_MISMATCH', 'INVALID', fn)
        if pins is None:
            iss.add('PINS_NOT_CHECKED', 'NOTE', 'verify mode: fixture directory')
        rj = strict_loads(utf8(raw['run.json']), float_paths=[('seconds',)])
        if isinstance(rj, dict) and isinstance(rj.get('seconds'), FloatToken):
            iss.add('RUN_JSON_TIMING_FLOAT_TOLERATED', 'NOTE', 'seconds=' + rj['seconds'])
        surv = strict_loads(utf8(raw['survivors.json']))
        killed_raw = strict_loads(utf8(gunzip(raw['vfc_killed.json.gz'])))
        duals_raw = strict_loads(utf8(gunzip(raw['lp_duals.json.gz'])))
        leaves_text = utf8(gunzip(raw['leaves.jsonl.gz']))

        reps, G, pinfo = profile_universe(name, iss)
        res['profiles'] = pinfo
        pats = [Pat(p) for p in reps]
        maps = [stab_maps(p, G) for p in pats]
        reps_index = {p.prof: n for n, p in enumerate(pats)}
        frontier['profile_reps_total'] = len(pats)
        nE = len(pats[0].E)
        k = pats[0].k

        if not isinstance(killed_raw, list):
            raise Reject('VFC_KILLED_NOT_LIST')
        killed_list, killed_set = [], set()
        for n, s in enumerate(killed_raw):
            if not isinstance(s, list) or not s:
                raise Reject('VFC_SIG_SCHEMA', n)
            ents = []
            for e in s:
                if not (isinstance(e, list) and len(e) == 5 and all(is_int(x) for x in e)):
                    raise Reject('VFC_SIG_SCHEMA', n)
                g, a, b2, b3, b5 = e
                if not (g >= 2 and 1 <= a <= g - 1 and min(b2, b3, b5) >= 0):
                    raise Reject('VFC_SIG_ENTRY_RANGE', n)
                ents.append(tuple(e))
            if ents != sorted(ents):
                iss.add('VFC_SIG_NOT_SORTED', 'INVALID', n)
            t = tuple(sorted(ents))
            if t in killed_set:
                iss.add('VFC_SIG_DUPLICATE', 'INVALID', n)
            killed_set.add(t)
            killed_list.append(t)

        book = DualBook(duals_raw, iss)
        res['lp_duals'] = book.verify_stored(iss)

        sig_ok = 0
        for sig in killed_list:
            guard.tick()
            recs = sorted((g, a, (b2, b3, b5), ((b2, b2), (b3, b3), (b5, b5))) for (g, a, b2, b3, b5) in sig)
            ok, why, keys = verify_recs(recs, book)
            if ok:
                sig_ok += 1
                book.referenced.update(keys)
            else:
                iss.add('VFC_SIG_NOT_VERIFIED:' + why[0], 'INVALID', {'sig': sig_str(sig), 'key': why[1], 'q': why[2]})
        res['vfc_killed'] = {'listed': len(killed_list), 'verified_exact_semantics': sig_ok}

        stats = {'children': 0, 'closed_T': 0, 'closed_VFC': 0, 'closed_Kp': 0, 'open_internal': 0,
                 'leaves': 0, 'vfc_checks': 0}
        star_memo, enc, reached = {}, set(), {}
        tw = time.monotonic()
        for ri, pat in enumerate(pats):
            frontier['current_rep'] = [list(p) for p in pat.prof]
            try:
                reached[ri] = walk_rep(pat, book, killed_set, star_memo, enc, iss, guard, stats)
            except CapError as e:
                iss.add('CAP_UNDETERMINED_IN_WALK', 'INCOMPLETE', {'rep': ri, 'err': str(e)})
                reached[ri] = []
            frontier['profile_reps_completed'] = ri + 1
        frontier['current_rep'] = None
        stats['walk_seconds'] = round(time.monotonic() - tw, 3)
        stats['star_patterns_reverified'] = sum(1 for r in star_memo.values() if r[0])
        stats['star_patterns_not_killed'] = sum(1 for r in star_memo.values() if not r[0])
        res['walk'] = stats

        dead = killed_set - enc
        if dead:
            iss.add('VFC_SIG_DEAD_NEVER_ENCOUNTERED', 'INVALID', [sig_str(s) for s in sorted(dead)[:MAX_EXAMPLES]])
        res['vfc_killed'].update({'encountered_in_walk': len(enc), 'dead': len(dead)})

        lines = parse_leaves(leaves_text, k, nE, iss)
        lres, survive = process_leaves(pats, maps, reps_index, reached, lines, book, iss, guard)
        res['leaves'] = lres

        if not isinstance(surv, list):
            raise Reject('SURVIVORS_NOT_LIST')
        surv_lines = [obj for obj in lines if obj['rule'] == 'SURVIVE']
        if surv != surv_lines:
            iss.add('SURVIVORS_FILE_MISMATCH', 'INVALID', [len(surv), len(surv_lines)])
        if surv_lines:
            iss.add('SURVIVE_LINES_PRESENT_NO_EXCLUSION', 'INCOMPLETE', len(surv_lines))

        unref = set(book.y) - book.referenced
        res['lp_duals'].update({'referenced_keys': len(book.referenced & set(book.y)),
                                'referenced_missing': len(book.referenced - set(book.y)),
                                'unreferenced_stored_keys': len(unref)})
        if unref:
            iss.add('LP_DUAL_UNREFERENCED_STORED_KEYS', 'NOTE', len(unref))

        # run.json: claims compared with recomputed values
        if not isinstance(rj, dict):
            raise Reject('RUN_JSON_SCHEMA')
        if rj.get('status') != 'COMPLETE':
            iss.add('RUN_STATUS_NOT_COMPLETE', 'INCOMPLETE', rj.get('status'))
        if rj.get('universe') != name:
            iss.add('RUN_JSON_UNIVERSE_MISMATCH', 'INVALID', rj.get('universe'))
        if rj.get('engine_sha256') != ENGINE_SHA:
            iss.add('RUN_JSON_ENGINE_SHA_MISMATCH', 'INVALID', rj.get('engine_sha256'))
        out = rj.get('output_sha256')
        if not isinstance(out, dict) or set(out) != set(HASHED_OUTPUTS):
            iss.add('RUN_JSON_OUTPUT_HASH_SET', 'INVALID', None)
        else:
            for fn in HASHED_OUTPUTS:
                if out[fn] != res['inputs'][fn]['sha256']:
                    iss.add('RUN_JSON_OUTPUT_HASH_MISMATCH', 'INVALID', fn)
        if rj.get('profiles_total') != len(pats):
            iss.add('RUN_JSON_PROFILES_TOTAL_MISMATCH', 'INVALID', [rj.get('profiles_total'), len(pats)])
        if rj.get('survivor_count') != len(surv_lines):
            iss.add('RUN_JSON_SURVIVOR_COUNT_MISMATCH', 'INVALID', [rj.get('survivor_count'), len(surv_lines)])
        st = rj.get('stats') if isinstance(rj.get('stats'), dict) else {}
        if st.get('leaf_orbits') != len(lines):
            iss.add('RUN_JSON_LEAF_ORBITS_MISMATCH', 'INVALID', [st.get('leaf_orbits'), len(lines)])
        if st.get('leaf_rule') != lres['line_rule_counts']:
            iss.add('RUN_JSON_LEAF_RULE_MISMATCH', 'INVALID', [st.get('leaf_rule'), lres['line_rule_counts']])
        closed = st.get('closed') if isinstance(st.get('closed'), dict) else {}
        mirror = {
            'closed_T': [closed.get('T'), stats['closed_T']],
            'closed_VFC': [closed.get('VFC'), stats['closed_VFC']],
            'closed_Kp': [closed.get('Kp'), stats['closed_Kp']],
            'labelled_leaves': [st.get('leaves'), stats['leaves']],
            'leaf_orbits': [st.get('leaf_orbits'), lres['reached_classes']],
        }
        nodes_candidates = {'open_internal+leaves': stats['open_internal'] + stats['leaves'],
                            'open_internal+reps': stats['open_internal'] + len(pats),
                            'open_internal+leaves+reps': stats['open_internal'] + stats['leaves'] + len(pats),
                            'children': stats['children']}
        res['mirror_expected_checks'] = {
            'pairs_[engine_claim,recomputed]': mirror,
            'all_equal': all(a == b for a, b in mirror.values()),
            'engine_nodes': st.get('nodes'),
            'nodes_candidates': nodes_candidates,
            'nodes_matching_candidates': [n for n, v in nodes_candidates.items() if v == st.get('nodes')],
            'expected_receipt_counts': EXPECTED[name],
        }
        if not res['mirror_expected_checks']['all_equal']:
            iss.add('MIRROR_EXPECTED_CHECK_MISMATCH', 'NOTE', mirror)
        if rj.get('exploratory') is not True:
            iss.add('RUN_JSON_NOT_MARKED_EXPLORATORY', 'NOTE', rj.get('exploratory'))
        res['status'] = None
    except Stopped as e:
        res['status'] = 'UNKNOWN'
        res['stop_reason'] = str(e)
    except Reject as e:
        iss.add('MALFORMED_INPUT:' + e.code, 'INVALID', e.detail)
    except CapError as e:
        iss.add('CAP_UNDETERMINED', 'INCOMPLETE', str(e))
    except OSError as e:
        iss.add('INPUT_UNREADABLE', 'INVALID', str(e))
    res['issues'] = iss.items
    if res.get('status') != 'UNKNOWN':
        res['status'] = iss.verdict()
    res['seconds'] = round(time.monotonic() - t0, 3)
    return res


# ----------------------------------------------------------------------------- receipt audit

PIN_RE = re.compile(r'([0-9a-f]{64})  (stageA-[A-Za-z0-9]+/[A-Za-z0-9_.]+)\Z')


def frozen_texts(lane, iss):
    out = {}
    for rel, want in FROZEN_TEXTS.items():
        try:
            h = sha256_bytes(read_bytes(os.path.join(lane, rel)))
        except OSError:
            h = None
        out[rel] = {'expected': want, 'actual': h, 'match': h == want}
        if h != want:
            iss.add('FROZEN_TEXT_HASH_MISMATCH', 'INVALID', rel)
    return out


def receipt_audit(lane, iss):
    out = {'path': os.path.join(lane, RECEIPT_REL)}
    b = read_bytes(out['path'])
    out['sha256'] = sha256_bytes(b)
    out['sha256_expected'] = RECEIPT_SHA
    if out['sha256'] != RECEIPT_SHA:
        iss.add('RECEIPT_SHA_MISMATCH', 'INVALID', out['sha256'])
    text = utf8(b)
    pins, in_block = {}, False
    for line in text.split('\n'):
        if line.startswith('```'):
            in_block = not in_block
            continue
        if in_block:
            m = PIN_RE.match(line)
            if not m:
                iss.add('RECEIPT_BLOCK_LINE_UNPARSED', 'INVALID', line)
                continue
            if m.group(2) in pins:
                iss.add('RECEIPT_PIN_DUPLICATE', 'INVALID', m.group(2))
            pins[m.group(2)] = m.group(1)
    out['pin_count'] = len(pins)
    if len(pins) != 16:
        iss.add('RECEIPT_PIN_COUNT_NOT_16', 'INVALID', len(pins))
    files = {}
    for rel, want in sorted(pins.items()):
        p = os.path.join(lane, 'evidence', rel)
        try:
            fb = read_bytes(p)
            got, size = sha256_bytes(fb), len(fb)
        except OSError:
            got, size = None, None
        files[rel] = {'pinned': want, 'actual': got, 'bytes': size, 'match': got == want}
        if got != want:
            iss.add('RECEIPT_PIN_MISMATCH', 'INVALID', rel)
    out['pins'] = files
    unpinned = []
    for d in ('stageA-X1', 'stageA-MSP45', 'stageA-CORE5', 'stageA-CONTROLS'):
        for fn in sorted(os.listdir(os.path.join(lane, 'evidence', d))):
            if d + '/' + fn not in pins:
                unpinned.append(d + '/' + fn)
    out['unpinned_files_in_stageA_dirs'] = unpinned
    if unpinned:
        iss.add('RECEIPT_UNPINNED_FILE', 'NOTE', unpinned)
    try:
        eng = sha256_bytes(read_bytes(os.path.join(lane, ENGINE_REL)))
    except OSError:
        eng = None
    out['engine_file_sha256_hash_only'] = eng
    out['engine_sha_in_receipt_text'] = ENGINE_SHA in text
    if eng != ENGINE_SHA or ENGINE_SHA not in text:
        iss.add('ENGINE_IDENTITY_MISMATCH', 'INVALID', eng)
    recs = {}
    for rel in FREEZE_RECORDS:
        try:
            lines = utf8(read_bytes(os.path.join(lane, rel))).split('\n')
            recs[rel] = {'host_clock_line': lines[0], 'entries': [l for l in lines[1:] if l]}
        except (OSError, Reject):
            recs[rel] = None
    out['freeze_records'] = recs
    wall = [l for l in text.split('\n') if l.startswith('- **Wall clock:**')]
    out['receipt_wall_clock_line'] = wall[0] if wall else None
    out['late_certificate_format_freeze'] = (
        'CERT-FORMAT-k7-v1 freeze record host clock %r versus Stage A wall clock %r: the certificate '
        'format and the RPLP addendum postdate the Stage A run (disclosed deviation; this replay does '
        'not make it preregistered).' % (
            (recs.get('evidence/certformat-v1.sha256') or {}).get('host_clock_line'), out['receipt_wall_clock_line']))
    return out, pins


# ----------------------------------------------------------------------------- realisable controls

def perm_parity(p):
    inv = 0
    for x in range(len(p)):
        for y in range(x + 1, len(p)):
            if p[x] > p[y]:
                inv += 1
    return inv & 1


class FinGroup:
    def __init__(self, els):
        self.el = sorted(set(els))
        self.n = len(self.el)
        self.idx = {e: i for i, e in enumerate(self.el)}
        self.mul = [[self.idx[tuple(a[y] for y in b)] for b in self.el] for a in self.el]
        self.e = self.idx[tuple(range(len(self.el[0])))]
        self.inv = [row.index(self.e) for row in self.mul]
        self.full = (1 << self.n) - 1

    def closure(self, gens):
        S = {self.e}
        frontier = [self.e]
        while frontier:
            nxt = []
            for s in frontier:
                for g in gens:
                    t = self.mul[s][g]
                    if t not in S:
                        S.add(t)
                        nxt.append(t)
            frontier = nxt
        m = 0
        for s in S:
            m |= 1 << s
        return m

    def subgroups(self):
        cyc = {}
        for x in range(self.n):
            cyc.setdefault(self.closure([x]), x)
        subs = {m: [x] for m, x in cyc.items()}
        frontier = list(subs.items())
        while frontier:
            new = []
            for m, gens in frontier:
                for cm, cx in cyc.items():
                    if cm & ~m == 0:
                        continue
                    jm = self.closure(gens + [cx])
                    if jm not in subs:
                        subs[jm] = gens + [cx]
                        new.append((jm, gens + [cx]))
            frontier = new
        return subs

    def prod(self, X, Y):
        m = 0
        yb = bits(Y)
        for x in bits(X):
            row = self.mul[x]
            for y in yb:
                m |= 1 << row[y]
        return m

    def lmul(self, g, X):
        row = self.mul[g]
        m = 0
        for x in bits(X):
            m |= 1 << row[x]
        return m

    def rmul(self, X, g):
        m = 0
        for x in bits(X):
            m |= 1 << self.mul[x][g]
        return m

    def left_cosets(self, H):
        seen, out = 0, []
        for g in range(self.n):
            if (seen >> g) & 1:
                continue
            c = self.lmul(g, H)
            out.append((g, c))
            seen |= c
        return out

    def right_cosets(self, H):
        seen, out = 0, []
        for g in range(self.n):
            if (seen >> g) & 1:
                continue
            c = self.rmul(H, g)
            out.append((g, c))
            seen |= c
        return out


def make_group(name):
    if name == 'A5':
        els, expect = [p for p in itertools.permutations(range(5)) if perm_parity(p) == 0], 60
    elif name == 'C2xS4':
        els = []
        for s in itertools.permutations(range(4)):
            els.append(tuple(s) + (4, 5))
            els.append(tuple(s) + (5, 4))
        expect = 48
    elif name == 'C6':
        c = (1, 2, 3, 4, 5, 0)
        x = tuple(range(6))
        els = []
        for _ in range(6):
            els.append(x)
            x = tuple(c[y] for y in x)
        expect = 6
    else:
        raise Reject('CONTROL_GROUP_UNKNOWN', name)
    G = FinGroup(els)
    if G.n != expect:
        raise Reject('CONTROL_GROUP_ORDER', name)
    return G


def control_family(fam, rec, guard):
    iss = Issues()
    out = {'family': fam}
    if not isinstance(rec, dict) or not isinstance(rec.get('n'), list) or not isinstance(rec.get('alpha'), dict):
        raise Reject('CONTROL_SCHEMA', fam)
    n_list = rec['n']
    if not all(is_int(x) and x >= 1 for x in n_list):
        raise Reject('CONTROL_SCHEMA', fam)
    k = len(n_list)
    A = [[0] * k for _ in range(k)]
    want_keys = {'%d%d' % (i, j) for i in range(k) for j in range(i + 1, k)}
    if set(rec['alpha']) != want_keys:
        raise Reject('CONTROL_ALPHA_KEYS', fam)
    for key, val in rec['alpha'].items():
        if not is_int(val):
            raise Reject('CONTROL_ALPHA_VALUE', fam)
        i, j = int(key[0]), int(key[1])
        A[i][j] = A[j][i] = val
    gname = fam.split('_')[0]
    G = make_group(gname)
    subs = G.subgroups()
    out['group'] = {'name': gname, 'order': G.n, 'subgroup_count': len(subs)}
    by_order = {}
    for m in subs:
        by_order.setdefault(popcount(m), []).append(m)
    cands = []
    for n in n_list:
        if G.n % n:
            raise Reject('CONTROL_INDEX_NOT_DIVISOR', [fam, n])
        lst = []
        for H in sorted(by_order.get(G.n // n, [])):
            for g, c in G.left_cosets(H):
                lst.append((H, g, c))
        cands.append(lst)
    chosen = []
    nodes = [0]

    def bt(i):
        if i == k:
            return True
        for cand in cands[i]:
            guard.tick()
            nodes[0] += 1
            H, g, c = cand
            good = True
            for j in range(i):
                Hj, gj, cj = chosen[j]
                if c & cj:
                    good = False
                    break
                inter = popcount(H & Hj)
                I = G.n // inter
                l = lcm(n_list[i], n_list[j])
                if I % l != 0 or I // l != A[j][i]:
                    good = False
                    break
            if good:
                chosen.append(cand)
                if bt(i + 1):
                    return True
                chosen.pop()
        return False

    found = bt(0)
    out['search_nodes'] = nodes[0]
    out['realised'] = found
    if not found:
        iss.add('CONTROL_NOT_REALISED_WITH_STATED_N_ALPHA', 'INVALID', fam)
        out['issues'] = iss.items
        out['status'] = iss.verdict()
        return out
    U = [c[0] for c in chosen]
    gs = [c[1] for c in chosen]
    cos = [c[2] for c in chosen]
    out['realisation'] = [{'index': n_list[i], 'subgroup_order': popcount(U[i]),
                           'subgroup_generators': [list(G.el[x]) for x in subs[U[i]]],
                           'subgroup_elements': [list(G.el[x]) for x in bits(U[i])],
                           'coset_representative': list(G.el[gs[i]])} for i in range(k)]
    for i in range(k):
        if popcount(U[i]) * n_list[i] != G.n:
            iss.add('CONTROL_INDEX_WRONG', 'INVALID', i)
        for j in range(i + 1, k):
            if cos[i] & cos[j]:
                iss.add('CONTROL_COSETS_NOT_DISJOINT', 'INVALID', [i, j])
    prof = [cap_profile(n) for n in n_list]
    pat = Pat(prof)
    out['profiles'] = [list(p) for p in prof]
    w = [n // (2 ** vp(n, 2) * 3 ** vp(n, 3) * 5 ** vp(n, 5)) for n in n_list]
    for i in range(k):
        for j in range(i + 1, k):
            if pat.g[i][j] != math.gcd(n_list[i], n_list[j]):
                iss.add('CONTROL_PROFILE_GCD_MISMATCH', 'INVALID', [i, j])
            if math.gcd(w[i], w[j]) != 1:
                iss.add('CONTROL_H2_FAILS', 'INVALID', [i, j])
            if not 1 <= A[i][j] <= pat.g[i][j] - 1:
                iss.add('CONTROL_ALPHA_RANGE', 'INVALID', [i, j])
    P = [[G.prod(U[x], U[y]) for y in range(k)] for x in range(k)]
    mu = lambda m: Fr(popcount(m), G.n)
    for i in range(k):
        for j in range(k):
            if i != j and mu(P[i][j]) != Fr(A[i][j], pat.g[i][j]):
                iss.add('CONTROL_L03_MEASURE_MISMATCH', 'INVALID', [i, j])
    # T on every triangle, with the true tau
    tri = []
    for a, b, c in itertools.combinations(range(k), 3):
        tm, tM = pat.tau_min(A, a, b, c), pat.tau_max(A, a, b, c)
        T = G.n // popcount(U[a] & U[b] & U[c])
        L = lcm(lcm(n_list[a], n_list[b]), n_list[c])
        if T % L:
            iss.add('CONTROL_TAU_NOT_INTEGER', 'INVALID', [a, b, c])
            continue
        tau = T // L
        if tau % tm or tau > tM:
            iss.add('CONTROL_TRUE_TAU_VIOLATES_TMIN_TMAX', 'INVALID', [a, b, c, tau, tm, tM])
        if tm > tM:
            iss.add('CONTROL_KILLED_BY_T', 'INVALID', [a, b, c])
        tri.append([a, b, c, tau, tm, tM])
    out['triangles_[a,b,c,tau,tau_min,tau_max]'] = tri
    # K: link claims against true containments; K kill search; L3 on true pair conditions; K2
    links = 0
    for v in range(k):
        others = [u for u in range(k) if u != v]
        for i, j in itertools.combinations(others, 2):
            true_pair = (P[v][i] & ~P[j][i] == 0) or (P[v][j] & ~P[i][j] == 0)
            if pat.linked(A, v, i, j):
                links += 1
                if not true_pair:
                    iss.add('CONTROL_LINK_CLAIM_FALSE', 'INVALID', [v, i, j])
        for r in range(2, len(others) + 1):
            for S in itertools.combinations(others, r):
                s = sum(Fr(A[u][v], pat.g[u][v]) for u in S)
                if all(pat.linked(A, v, x, y) for x, y in itertools.combinations(S, 2)) and s >= 1:
                    iss.add('CONTROL_KILLED_BY_K', 'INVALID', [v, list(S)])
                if all((P[v][x] & ~P[y][x] == 0) or (P[v][y] & ~P[x][y] == 0)
                       for x, y in itertools.combinations(S, 2)) and s > 1 - Fr(1, n_list[v]):
                    iss.add('CONTROL_L3_FALSE_ON_TRUE_DATA', 'INVALID', [v, list(S)])
        for j in others:
            for kk in others:
                if j != kk and P[v][j] & ~P[v][kk] == 0 and not (Fr(A[v][j], pat.g[v][j]) + Fr(A[kk][j], pat.g[kk][j]) < 1):
                    iss.add('CONTROL_K2_FALSE_ON_TRUE_DATA', 'INVALID', [v, j, kk])
    out['link_claims_checked'] = links
    # P and realised RPLP/VFC primal at every vertex
    realised = {}
    for v in range(k):
        N = [u for u in range(k) if u != v]
        n = len(N)
        X = [P[v][u] for u in N]
        Y = [G.full & ~x for x in X]
        hi = {}
        for a, b in itertools.combinations(range(n), 2):
            lo_, hi_, u_ = pat.pair_bounds(A, v, N[a], N[b])
            act = mu(X[a] & X[b])
            if not lo_ <= act <= hi_ or (act / u_).denominator != 1:
                iss.add('CONTROL_PAIR_BOUNDS_FALSE_ON_TRUE_DATA', 'INVALID', [v, N[a], N[b], str(lo_), str(act), str(hi_)])
            if lo_ > hi_:
                iss.add('CONTROL_KILLED_BY_PPAIR', 'INVALID', [v, N[a], N[b]])
            hi[(a, b)] = hi_
        for r in range(1, n + 1):
            for S in itertools.combinations(range(n), r):
                Xs = {x: Fr(A[v][N[x]], pat.g[v][N[x]]) for x in S}
                tot = sum(1 - Xs[x] for x in S) - sum(1 - Xs[x] - Xs[y] + hi[(x, y)] for x, y in itertools.combinations(S, 2))
                if tot >= 1:
                    iss.add('CONTROL_KILLED_BY_PB', 'INVALID', [v, [N[x] for x in S]])
        hv = G.inv[gs[v]]
        D, qs, ds = [], [], []
        for x, u in enumerate(N):
            cu = G.lmul(G.mul[hv][gs[u]], U[u])
            if cu & U[v]:
                iss.add('CONTROL_TRANSLATED_OVERLAP', 'INVALID', [v, u])
            Dx = G.prod(U[v], cu)
            D.append(Dx)
            g = pat.g[v][u]
            sz = popcount(Dx)
            qx = sz * g // G.n if (sz * g) % G.n == 0 else None
            if qx is None or not 1 <= qx <= g - A[v][u]:
                iss.add('CONTROL_Q_OUT_OF_DOMAIN', 'INVALID', [v, u, qx])
            if Dx & X[x]:
                iss.add('CONTROL_D_MEETS_X', 'INVALID', [v, u])
            usz = G.n // n_list[u]
            dx = sz // usz if sz % usz == 0 else None
            if dx is None or qx is None or dx * g != qx * n_list[u]:
                iss.add('CONTROL_LOCAL_INDEX_MISMATCH', 'INVALID', [v, u])
            qs.append(qx)
            ds.append(dx)
        if None in qs or None in ds:
            continue
        recs = pat.star_records(A, v, N)
        allowed = set(allowed_masks(local_dints(recs, tuple(qs))))
        forced = [(a, b) for a in range(n) for b in range(n) if a != b and pat.forced(A, v, N[a], N[b])]
        for a, b in forced:
            if X[a] & ~X[b]:
                iss.add('CONTROL_FORCED_CONTAINMENT_FALSE', 'INVALID', [v, N[a], N[b]])
        cols = {}
        for y0, R in G.right_cosets(U[v]):
            Sm = Am = 0
            for x in range(n):
                if R & ~D[x] == 0:
                    Sm |= 1 << x
                elif R & D[x]:
                    iss.add('CONTROL_RIGHT_COSET_STRADDLES_D', 'INVALID', [v, N[x]])
                if R & ~Y[x] == 0:
                    Am |= 1 << x
                elif R & Y[x]:
                    iss.add('CONTROL_RIGHT_COSET_STRADDLES_Y', 'INVALID', [v, N[x]])
            if Sm & ~Am:
                iss.add('CONTROL_S_NOT_SUBSET_A', 'INVALID', v)
            sub = Sm
            while sub:
                if popcount(sub) >= 2:
                    s = popcount(sub)
                    if not any(math.gcd(ds[x], ds[y]) >= s for x, y in itertools.combinations(bits(sub), 2)):
                        iss.add('CONTROL_V3_FALSE_ON_TRUE_DATA', 'INVALID', [v, sub])
                sub = (sub - 1) & Sm
            if Sm and Sm not in allowed:
                iss.add('CONTROL_ALLOWED_TEST_REJECTS_TRUE_S_R', 'INVALID', [v, Sm])
            if Am == 0:
                if Sm:
                    iss.add('CONTROL_S_WITHOUT_A', 'INVALID', v)
                continue
            for a, b in forced:
                if (Am >> b) & 1 and not (Am >> a) & 1:
                    iss.add('CONTROL_FORCED_CLOSURE_FALSE', 'INVALID', [v, N[a], N[b]])
            cols[(Am, Sm)] = cols.get((Am, Sm), 0) + popcount(R)
        for x in range(n):
            if sum(c for (Am, Sm), c in cols.items() if (Sm >> x) & 1) != popcount(D[x]):
                iss.add('CONTROL_E1_FALSE', 'INVALID', [v, N[x]])
            if sum(c for (Am, Sm), c in cols.items() if (Am >> x) & 1) != popcount(Y[x]):
                iss.add('CONTROL_E2_FALSE', 'INVALID', [v, N[x]])
        for a, b in itertools.combinations(range(n), 2):
            cnt = sum(c for (Am, Sm), c in cols.items() if (Am >> a) & 1 and (Am >> b) & 1)
            if cnt != popcount(Y[a] & Y[b]):
                iss.add('CONTROL_B_COUNT_FALSE', 'INVALID', [v, N[a], N[b]])
            lo_, hi_, u_ = pat.pair_bounds(A, v, N[a], N[b])
            Xa, Xb = Fr(A[v][N[a]], pat.g[v][N[a]]), Fr(A[v][N[b]], pat.g[v][N[b]])
            if not 1 - Xa - Xb + lo_ <= Fr(cnt, G.n) <= 1 - Xa - Xb + hi_:
                iss.add('CONTROL_B_BOUNDS_FALSE_ON_TRUE_DATA', 'INVALID', [v, N[a], N[b]])
        tot = sum(cols.values())
        union = 0
        for yy in Y:
            union |= yy
        if tot != popcount(union) or tot >= G.n:
            iss.add('CONTROL_TOT_FALSE', 'INVALID', v)
        realised[v] = {'q_true': qs, 'local_indices_true': ds, 'forced_pairs': [[N[a], N[b]] for a, b in forced],
                       'column_types_used': len(cols), 'mu_union_Y': str(Fr(tot, G.n))}
    out['realised_primal_per_vertex'] = realised
    claims = {'disjoint': rec.get('disjoint'), 'T_violations': rec.get('T_violations'), 'kills': rec.get('kills')}
    out['source_claims'] = claims
    kills = rec.get('kills') or {}
    if rec.get('disjoint') is not True or rec.get('T_violations') != [] or \
            any(kills.get(x) not in (None, []) for x in ('K', 'P', 'VFC_vertices_killed', 'RPLP')):
        iss.add('CONTROL_SOURCE_CLAIM_DIFFERS', 'NOTE', claims)
    out['issues'] = iss.items
    out['status'] = iss.verdict()
    out['meaning'] = ('Explicit realisation found by this checker; true tau, links, K2, L3, pair bounds, '
                      'V3, forced containments, columns and E1/E2/B/TOT checked on the actual cosets. '
                      'A feasible true primal at q* means no (R) or (P) certificate can refute q* at any '
                      'vertex (and, by restriction, at any partial star), so VFC and RPLP cannot kill it; '
                      'T, K, Ppair and PB were evaluated exhaustively.')
    return out


def verify_controls(lane, pin, guard):
    iss = Issues()
    path = os.path.join(lane, 'evidence', CONTROLS_PIN)
    out = {'path': path}
    try:
        b = read_bytes(path)
        out['sha256'] = sha256_bytes(b)
        out['pinned'] = pin
        if pin != out['sha256']:
            iss.add('CONTROLS_PIN_MISMATCH', 'INVALID', out['sha256'])
        data = strict_loads(utf8(b), float_paths=[('seconds',)])
        if not isinstance(data, dict) or not isinstance(data.get('controls'), dict):
            raise Reject('CONTROLS_SCHEMA')
        if data.get('engine_sha256') != ENGINE_SHA:
            iss.add('CONTROLS_ENGINE_SHA_MISMATCH', 'INVALID', data.get('engine_sha256'))
        fams = {}
        for fam in sorted(data['controls']):
            r = control_family(fam, data['controls'][fam], guard)
            fams[fam] = r
            if r['status'] != 'COMPLETE_VALID':
                iss.add('CONTROL_FAMILY_NOT_SURVIVING:' + fam, 'INVALID', r['status'])
        out['families'] = fams
        status = None
    except Stopped as e:
        status = 'UNKNOWN'
        out['stop_reason'] = str(e)
    except Reject as e:
        iss.add('MALFORMED_CONTROLS:' + e.code, 'INVALID', e.detail)
        status = None
    except CapError as e:
        iss.add('CONTROL_CAP_UNDETERMINED', 'INCOMPLETE', str(e))
        status = None
    out['issues'] = iss.items
    out['status'] = status or ('PASS' if iss.verdict() == 'COMPLETE_VALID' else iss.verdict())
    return out


# ----------------------------------------------------------------------------- main

def header(args):
    me = os.path.abspath(__file__)
    return {'checker': VERSION, 'checker_path': me, 'checker_sha256': sha256_bytes(read_bytes(me)),
            'python': sys.version, 'executable': sys.executable, 'platform': platform.platform(),
            'argv': sys.argv, 'pid': os.getpid(), 'tmpdir_env': os.environ.get('TMPDIR'),
            'started_host_clock': time.strftime('%Y-%m-%dT%H:%M:%S%z'),
            'independence': 'stdlib only; written from frozen texts; no producer code imported, copied or executed'}


# ----------------------------------------------------------------------------- v2 terminal handling

CANCEL_SUFFIX = '.CANCELLED.json'
PUBLICATION_CONTRACT = ('This result counts only if the process exited normally with status equal to '
                        'exit_code and no file <result path>' + CANCEL_SUFFIX + ' exists; a process '
                        'ended by a signal publishes no result.')


def _sigterm_pending():
    """SIGTERM pending for this single-threaded process while SIGTERM is blocked."""
    return signal.SIGTERM in signal.sigpending()


def _finish(args, res, outf, guard, code):
    """Terminal decision, publication and exit status (the only part of v2 that differs from v1).

    1. SIGTERM is blocked before the decision.  CPython's pthread_sigmask runs any Python handler
       already tripped, so STOP records every earlier SIGTERM; a later one stays pending.
    2. The terminal resource sample is taken before the decision.  A latched stop (SIGTERM, free-space
       floor, RSS, self budget) or a pending SIGTERM makes the overall result UNKNOWN with exit 3.
    3. The result is serialised, flushed, fsynced and closed and the summary printed with SIGTERM
       still blocked; then resources are sampled once more.
    4. SIGTERM is reset to SIG_DFL while still blocked and pending SIGTERM is read a last time.  A
       SIGTERM pending then, a stop latched after the decision or a publication error creates the
       exclusive external marker <out>.CANCELLED.json and forces exit 3 (5 for a publication error);
       the serialised file must then not be used.
    5. Only then is SIGTERM unblocked: a SIGTERM arriving after the last check terminates the process
       by the default action, so a late delivery can never end in a normal exit.
    """
    signal.pthread_sigmask(signal.SIG_BLOCK, {signal.SIGTERM})
    term = {'sigterm_blocked_for_decision': True,
            'overall_before_terminal_decision': res.get('overall'),
            'exit_code_before_terminal_decision': code}
    try:
        guard.sample()
    except Exception as e:
        if not STOP['flag']:
            STOP.update(flag=True, why='terminal resource sample failed: %s: %s' % (type(e).__name__, e))
    pending = _sigterm_pending()
    if pending:
        signal.sigwait({signal.SIGTERM})
        if not STOP['flag']:
            STOP.update(flag=True, why='SIGTERM pending at terminal decision')
    term['sigterm_pending_at_decision'] = pending
    term['stop_latched_at_decision'] = STOP['flag']
    term['stop_reason_at_decision'] = STOP['why']
    if STOP['flag']:
        res['overall'], code = 'UNKNOWN', 3
    term['decided_overall'] = res['overall']
    term['decided_exit_code'] = code
    res['terminal'] = term
    res['resources'] = guard.report()
    res['finished_host_clock'] = time.strftime('%Y-%m-%dT%H:%M:%S%z')
    res['exit_code'] = code
    res['publication_contract'] = PUBLICATION_CONTRACT
    stop_at_decision = STOP['flag']
    problem, final = None, code
    try:
        json.dump(res, outf, indent=1, sort_keys=False, default=str)
        outf.write('\n')
        outf.flush()
        os.fsync(outf.fileno())
        outf.close()
        summ = {'overall': res['overall'], 'exit_code': code}
        for U, r in (res.get('universes') or {}).items():
            summ[U] = r.get('status')
        if 'controls' in res:
            summ['controls'] = res['controls'].get('status')
        print(json.dumps(summ), flush=True)
    except Exception as e:
        problem, final = 'publication error: %s: %s' % (type(e).__name__, e), 5
    if problem is None:
        try:
            guard.sample()
        except Exception as e:
            problem, final = 'post-publication resource sample failed: %s: %s' % (type(e).__name__, e), 3
    signal.signal(signal.SIGTERM, signal.SIG_DFL)
    late = _sigterm_pending()
    if late:
        signal.sigwait({signal.SIGTERM})
        if problem is None:
            problem, final = 'SIGTERM received during or after serialisation', 3
    if problem is None and STOP['flag'] and not stop_at_decision:
        problem, final = 'stop latched after the decision: %s' % STOP['why'], 3
    if problem is not None:
        marker = {'cancelled': True, 'result_path': os.path.abspath(args.out), 'reason': problem,
                  'sigterm_pending_after_serialisation': late, 'decided_overall': res['overall'],
                  'decided_exit_code': code, 'process_exit_code': final, 'checker': VERSION,
                  'pid': os.getpid(), 'host_clock': time.strftime('%Y-%m-%dT%H:%M:%S%z')}
        try:
            with open(args.out + CANCEL_SUFFIX, 'x') as mf:
                json.dump(marker, mf, indent=1, default=str)
                mf.write('\n')
                mf.flush()
                os.fsync(mf.fileno())
        except Exception:
            pass
        try:
            print(json.dumps({'cancelled': True, 'reason': problem, 'exit_code': final}), flush=True)
        except Exception:
            pass
    signal.pthread_sigmask(signal.SIG_UNBLOCK, {signal.SIGTERM})
    return final


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='cmd', required=True)
    a = sub.add_parser('all')
    a.add_argument('--lane', required=True)
    a.add_argument('--out', required=True)
    v = sub.add_parser('verify')
    v.add_argument('--universe', required=True, choices=sorted(UNIVERSES))
    v.add_argument('--input-dir', required=True)
    v.add_argument('--out', required=True)
    args = ap.parse_args()
    signal.signal(signal.SIGTERM, _on_sigterm)
    outf = open(args.out, 'x')
    res = header(args)
    guard = Guard(os.path.dirname(os.path.abspath(args.out)))
    free0 = guard.free()
    res['admission'] = {'statvfs_free_bytes': free0, 'required_bytes': ADMISSION_FREE,
                        'projected_growth_bytes_max': 16 * 1024 * 1024, 'ok': free0 >= ADMISSION_FREE}
    code = 0
    try:
        if free0 < ADMISSION_FREE:
            res['overall'] = 'NOT_STARTED'
            code = 4
        else:
            guard.sample()
            if args.cmd == 'all':
                top = Issues()
                res['frozen_texts'] = frozen_texts(args.lane, top)
                res['receipt_audit'], pins = receipt_audit(args.lane, top)
                res['top_issues'] = top.items
                res['universes'] = {}
                verdicts = [top.verdict()]
                for U in ('X1', 'MSP45', 'CORE5'):
                    if STOP['flag']:
                        res['universes'][U] = {'status': 'UNKNOWN', 'stop_reason': STOP['why'], 'not_started': True}
                        verdicts.append('UNKNOWN')
                        continue
                    upins = {fn: pins.get('stageA-%s/%s' % (U, fn)) for fn in RUN_FILES}
                    r = verify_universe(U, os.path.join(args.lane, 'evidence', 'stageA-' + U), upins, guard)
                    res['universes'][U] = r
                    verdicts.append(r['status'])
                if STOP['flag']:
                    res['controls'] = {'status': 'UNKNOWN', 'stop_reason': STOP['why']}
                    verdicts.append('UNKNOWN')
                else:
                    res['controls'] = verify_controls(args.lane, pins.get(CONTROLS_PIN), guard)
                    verdicts.append('COMPLETE_VALID' if res['controls']['status'] == 'PASS' else res['controls']['status'])
            else:
                r = verify_universe(args.universe, args.input_dir, None, guard)
                res['universes'] = {args.universe: r}
                verdicts = [r['status']]
            if 'UNKNOWN' in verdicts:
                res['overall'], code = 'UNKNOWN', 3
            elif 'INVALID' in verdicts:
                res['overall'], code = 'INVALID', 1
            elif 'INCOMPLETE' in verdicts:
                res['overall'], code = 'INCOMPLETE', 2
            else:
                res['overall'], code = 'COMPLETE_VALID', 0
    except Exception as e:  # internal error: fail closed
        import traceback
        res['overall'] = 'INTERNAL_ERROR'
        res['internal_error'] = '%s: %s' % (type(e).__name__, e)
        res['internal_traceback'] = traceback.format_exc()
        code = 5
    return _finish(args, res, outf, guard, code)


if __name__ == '__main__':
    sys.exit(main())
