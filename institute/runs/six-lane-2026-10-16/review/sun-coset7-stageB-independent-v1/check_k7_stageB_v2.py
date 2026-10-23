#!/usr/bin/env python3
"""check_k7_stageB_v2.py -- independent, stdlib-only replay checker for the sun-coset7 Stage B
certificate outputs (universes K52 and KII).
v2 = v1 (00b4e2a6...) with one change: run.json is producer metadata used for comparison only, so its
float 'seconds' field is accepted there; certificate files keep the strict no-float/no-duplicate parser.

Written only from the frozen texts
  README.md                 2a6d6d6e1dadbad522c8c8f9322c17eae719fb01fe373e6b1caf8c40cadc3fd1
  rules-k7-v1.md            77b9afec448ab44605b9ee513778bffd3e40aa9157807e8402f5488330e73cee
  rules-k7-addendum-v1.md   fb2c306b17a258181bb770c7c6c38585da77c0e312c68463cee7dc0f15fd1066
  CERT-FORMAT-k7-v1.md      2c0e483011a0ea3aace670da4b9a200ae333e676682e0e10fb47d2e584401545
No producer code was read, imported, copied or executed.  Producer strings (profiles, canonical
codes, LP keys) are only compared with values recomputed here.  All arithmetic is exact.

What is established when the status is COMPLETE_VALID (and only then):
  * the admissible capped-profile universe is enumerated here from the README class definitions and
    cross-checked against the CERT-FORMAT role domains / gcd sets; one representative per
    role-preserving orbit is walked;
  * for every representative, the full alpha tree (edge order of CERT-FORMAT section 2) is re-walked;
    every node is either expanded into all children or closed by a rule verified here exactly
    (T: tau_min > tau_max; VFC: signature listed in vfc_killed AND every q-vector re-verified with an
    exact dual; Kp: linked pairs and sum >= 1 recomputed);
  * every reached leaf's canonical class (stabiliser recomputed here) has exactly one leaf line whose
    rep has that canonical code and whose RPLP witness verifies for every q (R: exact VFC dual;
    P: exact (*) inequality on every column and objective >= 1);
  * every listed vfc_killed signature, every lp_duals entry and every leaf line verifies.
Statuses: COMPLETE_VALID (exit 0), INVALID (exit 2), INCOMPLETE (exit 3), NOT_STARTED (exit 4).
"""
import argparse
import gzip
import hashlib
import itertools
import json
import math
import os
import re
import resource
import signal
import sys
import time
import traceback
from fractions import Fraction
from math import gcd

PRIMES = (2, 3, 5)
DISK_ADMIT = 12_216_777_216      # 12.2e9 + 16 MiB, fresh admission before the run
DISK_FLOOR = 12_000_000_000      # in-flight floor
RSS_STOP = 900 * 1024 * 1024     # cooperative stop well below the 1 GiB cap
DISK_POLL_S = 15.0
EXIT = {'COMPLETE_VALID': 0, 'INVALID': 2, 'INCOMPLETE': 3, 'NOT_STARTED': 4}
STOP = {'flag': None}


def _on_sigterm(signum, frame):
    STOP['flag'] = 'SIGTERM'


class CertError(Exception):
    def __init__(self, reason, detail=''):
        super().__init__(reason, detail)
        self.reason = reason
        self.detail = detail


class Stop(Exception):
    def __init__(self, reason):
        super().__init__(reason)
        self.reason = reason


class FailFast(Exception):
    pass


def lcm(a, b):
    return a * b // gcd(a, b)


def vp(n, p):
    if type(n) is not int or n <= 0:
        raise CertError('INTERNAL_VALUATION_ARG', repr(n))
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c


def gp(a, b):
    """gcd of two capped profiles (CERT-FORMAT section 1); equals the true gcd under (H1),(H2)."""
    return 2 ** min(a[0], b[0]) * 3 ** min(a[1], b[1]) * 5 ** min(a[2], b[2])


def is_int(x):
    return type(x) is int


# ---------------------------------------------------------------- strict parsing
def _pairs_nodup(pairs):
    d = {}
    for k, v in pairs:
        if k in d:
            raise CertError('JSON_DUPLICATE_KEY', str(k)[:100])
        d[k] = v
    return d


def _no_float(s):
    raise CertError('JSON_FLOAT_LITERAL', s[:40])


def _no_const(s):
    raise CertError('JSON_NONFINITE_CONSTANT', s[:40])


def strict_json(text):
    try:
        return json.loads(text, object_pairs_hook=_pairs_nodup, parse_float=_no_float,
                          parse_constant=_no_const)
    except json.JSONDecodeError as e:
        raise CertError('JSON_SYNTAX', str(e)[:200])


RAT_RE = re.compile(r'-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?')


def rat(s, what):
    if type(s) is not str or RAT_RE.fullmatch(s) is None:
        raise CertError('BAD_RATIONAL', ('%s: %r' % (what, s))[:120])
    return Fraction(s)


KEY_ITEM_RE = re.compile(r'([1-9][0-9]*)/([1-9][0-9]*),(0|[1-9][0-9]*),(0|[1-9][0-9]*),(0|[1-9][0-9]*)')


def key_string(key):
    return ';'.join('%d/%d,%d,%d,%d' % it for it in key)


def parse_key_string(s):
    """Parses a stored lp_duals key so that every stored entry is verified, used or not."""
    if type(s) is not str or not s:
        raise CertError('KEY_FORMAT', repr(s)[:100])
    items = []
    for part in s.split(';'):
        m = KEY_ITEM_RE.fullmatch(part)
        if m is None:
            raise CertError('KEY_FORMAT', s[:100])
        items.append(tuple(int(x) for x in m.groups()))
    key = tuple(items)
    if list(key) != sorted(key):
        raise CertError('KEY_UNSORTED', s[:100])
    for it in key:
        if gcd(it[0], it[1]) != 1 or not 0 < it[0] < it[1]:
            raise CertError('KEY_FRACTION', s[:100])
    if key_string(key) != s:
        raise CertError('KEY_NONCANONICAL', s[:100])
    return key


def key_from(entries, q):
    """LP key of CERT-FORMAT section 3 recomputed from entries (g, alpha, b2, b3, b5) and q."""
    items = []
    for (gg, _al, b2, b3, b5), qq in zip(entries, q):
        fr = Fraction(qq, gg)
        items.append((fr.numerator, fr.denominator, vp(qq, 2) + b2, vp(qq, 3) + b3, vp(qq, 5) + b5))
    items.sort()
    key = tuple(items)
    return key, key_string(key)


_ALLOWED_CACHE = {}


def allowed_masks(dvs):
    """allowed[m] for position subsets m: |T|<=1, or every T' subset of T with |T'|>=2 has x!=y
    with 2^min(d2)*3^min(d3)*5^min(d5) >= |T'| (hereditary definition, all subsets checked)."""
    r = _ALLOWED_CACHE.get(dvs)
    if r is not None:
        return r
    n = len(dvs)
    G = [[2 ** min(dvs[x][0], dvs[y][0]) * 3 ** min(dvs[x][1], dvs[y][1]) * 5 ** min(dvs[x][2], dvs[y][2])
          for y in range(n)] for x in range(n)]
    allowed = [False] * (1 << n)
    for m in range(1 << n):
        bits = [x for x in range(n) if (m >> x) & 1]
        if len(bits) <= 1:
            allowed[m] = True
            continue
        ok = max(G[x][y] for x in bits for y in bits if x < y) >= len(bits)
        allowed[m] = ok and all(allowed[m ^ (1 << x)] for x in bits)
    r = tuple(allowed)
    _ALLOWED_CACHE[dvs] = r
    return r


# ---------------------------------------------------------------- triangle formulas (rules L1, K1)
def tri_tau_min(px, py, pz, axy, axz, ayz):
    """lcm over the three edges of alpha / prod_p p^min(v_p(alpha), v_p(ell_third)),
    v_p(ell_z) = pi_z[p] - v_p(gamma_z), gamma_z = lcm of the two gcds at z."""
    gxy, gxz, gyz = gp(px, py), gp(px, pz), gp(py, pz)
    t = 1
    for a, gam, pt in ((axy, lcm(gxz, gyz), pz), (axz, lcm(gxy, gyz), py), (ayz, lcm(gxy, gxz), px)):
        d = 1
        for idx, p in enumerate(PRIMES):
            ell = pt[idx] - vp(gam, p)
            if ell < 0:
                raise CertError('NEGATIVE_ELL_VALUATION', repr((px, py, pz)))
            d *= p ** min(vp(a, p), ell)
        t = lcm(t, a // d)
    return t


def tri_tau_max(px, py, pz, axy, axz, ayz):
    """min over apex y of floor(gamma_y * alpha_xz * min(alpha_xy/g_xy, alpha_yz/g_yz))."""
    gxy, gxz, gyz = gp(px, py), gp(px, pz), gp(py, pz)
    best = None
    for gam, aopp, a1, g1, a2, g2 in (
            (lcm(gxy, gyz), axz, axy, gxy, ayz, gyz),    # apex y, others x,z
            (lcm(gxy, gxz), ayz, axy, gxy, axz, gxz),    # apex x, others y,z
            (lcm(gxz, gyz), axy, axz, gxz, ayz, gyz)):   # apex z, others x,y
        m = min(gam * aopp * a1 // g1, gam * aopp * a2 // g2)
        best = m if best is None else min(best, m)
    return best


def tri_T_ok(px, py, pz, axy, axz, ayz):
    return tri_tau_min(px, py, pz, axy, axz, ayz) <= tri_tau_max(px, py, pz, axy, axz, ayz)


def linked_formula(pv, pa, pb, ava, avb, aab):
    """linked(v; a, b): tau_min(a,v,b)*g_av >= lcm(g_av,g_ab)*alpha_vb*alpha_av  or
    tau_min(a,v,b)*g_bv >= lcm(g_bv,g_ab)*alpha_va*alpha_bv  (K1 at apex a, resp. apex b)."""
    tau = tri_tau_min(pa, pv, pb, ava, aab, avb)   # x=a, y=v, z=b
    gav, gab, gbv = gp(pa, pv), gp(pa, pb), gp(pb, pv)
    return (tau * gav >= lcm(gav, gab) * avb * ava) or (tau * gbv >= lcm(gbv, gab) * ava * avb)


# ---------------------------------------------------------------- universes
K = 7
EDGES = [(i, j) for i in range(K) for j in range(i + 1, K)]
EI = [[-1] * K for _ in range(K)]
for _t, (_i, _j) in enumerate(EDGES):
    EI[_i][_j] = EI[_j][_i] = _t
CAPPED = [(e, f, g) for e in range(5) for f in range(3) for g in range(3)]   # lexicographic, e outermost
PID = {p: n for n, p in enumerate(CAPPED)}
NP = len(CAPPED)

# (b) CERT-FORMAT-k7-v1 section 1, transcribed as data.
CF_DOMAINS = {
    'C': [(e, f, g) for e in (1, 2, 3, 4) for f in (1, 2) for g in (0, 1, 2)],
    'D2E': [(e, 0, g) for e in (2, 3, 4) for g in (0, 1, 2)],
    'X': [(e, 0, g) for e in (1, 2, 3, 4) for g in (1, 2)],
    'Y': [(0, f, g) for f in (1, 2) for g in (1, 2)],
}
CF_UNIVERSES = {
    'K52': (('D2E', 'D2E', 'C', 'C', 'C', 'C', 'C'),
            {('D2E', 'D2E'): (4,), ('C', 'D2E'): (2, 4), ('C', 'C'): (6,)}),
    'KII': (('X', 'Y', 'C', 'C', 'C', 'C', 'C'),
            {('X', 'Y'): (5,), ('C', 'X'): (2, 4), ('C', 'Y'): (3,), ('C', 'C'): (6,)}),
}


# (a) README-derived class predicates over the full capped cube (e<=4, f<=2, g<=2).
def readme_vertex_ok(U, v, p):
    e, f, g = p
    if U == 'K52':          # (I) type 2, |C| = 5, D = {d1, d2}: K5.2* together with the D2' case
        if v < 2:           # d in A_2 \ A_3 (type 2) and d in E (R1b, |D| >= 2)
            return e >= 2 and f == 0
        return e >= 1 and f >= 1                       # C = A_2 cap A_3
    if U == 'KII':          # Theorem R1(7)(II): A_5 = {x, y}
        if v == 0:
            return e >= 1 and f == 0 and g >= 1        # x in A_2 \ A_3, x in A_5
        if v == 1:
            return e == 0 and f >= 1 and g >= 1        # y in A_3 \ A_2, y in A_5
        return e >= 1 and f >= 1 and g == 0            # C = V \ {x, y}, not in A_5
    raise CertError('UNKNOWN_UNIVERSE', U)


def readme_pair_ok(U, u, v, pu, pv):
    gg = gp(pu, pv)
    if U == 'K52':
        du, dv = u < 2, v < 2
        if du and dv:
            return gg == 4                              # d1-d2: P = {2}, both in E
        if du or dv:
            return gg in (2, 4)                         # D-C: P = {2}; 4 iff both in E
        return gg == 6                                  # C-C
    s = {u, v}
    if s == {0, 1}:
        return gg == 5                                  # x-y
    if 0 in s:
        return gg in (2, 4)                             # x-C
    if 1 in s:
        return gg == 3                                  # y-C
    return gg == 6                                      # C-C


def readme_global_ok(U, prefix):
    if U == 'K52':                                      # a <= 1
        return sum(1 for p in prefix if p[2] >= 1) <= 1
    return True


def enum_labelled(n, vertex_ok, pair_ok, global_ok):
    out = []
    pre = []

    def rec():
        k = len(pre)
        if k == n:
            out.append(tuple(pre))
            return
        for p in CAPPED:
            if not vertex_ok(k, p):
                continue
            if all(pair_ok(i, k, pre[i], p) for i in range(k)):
                pre.append(p)
                if global_ok(pre):
                    rec()
                pre.pop()
    rec()
    return out


def runs_of(roles):
    runs, s = [], 0
    for i in range(1, len(roles) + 1):
        if i == len(roles) or roles[i] != roles[s]:
            runs.append((s, i))
            s = i
    return runs


def orbit_rep(t, runs):
    out = []
    for s, e in runs:
        out.extend(sorted(t[s:e]))
    return tuple(out)


def stabilizer_perms(pi, roles):
    groups = {}
    for v in range(len(pi)):
        groups.setdefault((roles[v], pi[v]), []).append(v)
    perms = [list(range(len(pi)))]
    for vs in groups.values():
        if len(vs) < 2:
            continue
        new = []
        for base in perms:
            for img in itertools.permutations(vs):
                p = list(base)
                for src, dst in zip(vs, img):
                    p[src] = dst
                new.append(p)
        perms = new
    return [tuple(p) for p in perms]


def canonical_code(A, stab):
    return min(tuple(A[p[i]][p[j]] for (i, j) in EDGES) for p in stab)


# ---------------------------------------------------------------- checker
class Checker:
    def __init__(self, args, out_dir):
        self.args = args
        self.out_dir = out_dir
        self.t0 = time.monotonic()
        self.budget = args.budget
        self.fail_fast = args.fail_fast
        self.last_disk = 0.0
        self.min_free = None
        self.disk_samples = 0
        self.rejections = []
        self.rej_counts = {}
        self.incomplete = []
        self.notes = []
        self.dual_cache = {}
        self.dual_obj_value_mismatch = 0
        self.T_memo = {}
        self.L_memo = {}
        self.cnt = [0, 0, 0, 0, 0, 0]   # visits, closed T, closed VFC, closed Kp, passed internal, leaves
        self.reached = {}
        self.rep_seen = set()
        self.used_sigs = set()
        self.line_status = {}
        self.line_rep = {}
        self.frontier = None
        self.per_profile = []

    # -- bookkeeping
    def reject(self, reason, detail=''):
        self.rej_counts[reason] = self.rej_counts.get(reason, 0) + 1
        if len(self.rejections) < 200:
            self.rejections.append({'reason': reason, 'detail': str(detail)[:300]})
        if self.fail_fast:
            raise FailFast(reason)

    def poll(self):
        if STOP['flag']:
            raise Stop(STOP['flag'])
        now = time.monotonic()
        if now - self.t0 > self.budget:
            raise Stop('SELF_BUDGET')
        if peak_rss_bytes() > RSS_STOP:
            raise Stop('RSS_SELF_LIMIT')
        if now - self.last_disk >= DISK_POLL_S:
            self.sample_disk()
            if self.min_free < DISK_FLOOR:
                raise Stop('DISK_FLOOR')

    def sample_disk(self):
        st = os.statvfs(self.out_dir)
        free = st.f_bavail * st.f_frsize
        self.min_free = free if self.min_free is None else min(self.min_free, free)
        self.disk_samples += 1
        self.last_disk = time.monotonic()
        return free

    # -- inputs
    def load_inputs(self, manifest_path, U):
        raw = open(manifest_path, 'rb').read()
        self.manifest_sha = hashlib.sha256(raw).hexdigest()
        man = strict_json(raw.decode('utf-8'))
        if type(man) is not dict or type(man.get('universes')) is not dict or U not in man['universes']:
            raise CertError('MANIFEST_FORMAT', 'universe %s missing' % U)
        ent = man['universes'][U]
        base = os.path.join(os.path.dirname(os.path.abspath(manifest_path)), ent['dir'])
        want = ent['files']
        names = ['leaves.jsonl.gz', 'lp_duals.json.gz', 'vfc_killed.json.gz', 'survivors.json', 'run.json']
        if type(want) is not dict or set(want) != set(names):
            raise CertError('MANIFEST_FORMAT', 'file set')
        self.input_records = []
        data = {}
        for nm in names:
            path = os.path.join(base, nm)
            b = open(path, 'rb').read()
            h = hashlib.sha256(b).hexdigest()
            self.input_records.append({'name': nm, 'path': path, 'bytes': len(b), 'sha256': h,
                                       'expected_sha256': want[nm], 'match': h == want[nm]})
            if h != want[nm]:
                raise CertError('INPUT_HASH_MISMATCH', nm)
            data[nm] = b
        self.manifest = man
        self.manifest_universe = ent
        return data

    # -- universe
    def build_universe(self, U):
        roles, allowed = CF_UNIVERSES[U]
        self.roles = roles
        cf = enum_labelled(
            K,
            lambda v, p: p in CF_DOMAINS[roles[v]],
            lambda u, v, pu, pv: gp(pu, pv) in allowed[tuple(sorted((roles[u], roles[v])))],
            lambda pre: True)
        rd = enum_labelled(
            K,
            lambda v, p: readme_vertex_ok(U, v, p),
            lambda u, v, pu, pv: readme_pair_ok(U, u, v, pu, pv),
            lambda pre: readme_global_ok(U, pre))
        cfs, rds = set(cf), set(rd)
        # (H1) consequences used by CAP: pairwise mins e<=2, f<=1, g<=1 on every labelled tuple
        h1_ok = all(min(t[i][0], t[j][0]) <= 2 and min(t[i][1], t[j][1]) <= 1 and min(t[i][2], t[j][2]) <= 1
                    for t in cf for i in range(K) for j in range(i + 1, K))
        runs = runs_of(roles)
        orbits = {}
        for t in cf:
            orbits.setdefault(orbit_rep(t, runs), []).append(t)
        group_order = 1
        for s, e in runs:
            group_order *= math.factorial(e - s)
        size_ok = True
        for r, mem in orbits.items():
            stab = len(stabilizer_perms(r, roles))
            if len(mem) * stab != group_order or len(set(mem)) != len(mem):
                size_ok = False
            if r not in cfs:
                size_ok = False
        reps = sorted(orbits)
        self.reps = reps
        self.rep_set = set(reps)
        info = {
            'roles': list(roles),
            'labelled_admissible_certformat': len(cf),
            'labelled_admissible_readme': len(rd),
            'readme_equals_certformat': cfs == rds,
            'readme_minus_certformat': len(rds - cfs),
            'certformat_minus_readme': len(cfs - rds),
            'H1_pairwise_mins_hold': h1_ok,
            'role_group_order': group_order,
            'orbits': len(reps),
            'orbit_size_sum': sum(len(v) for v in orbits.values()),
            'orbit_stabilizer_consistent': size_ok,
            'representatives_sha256': hashlib.sha256(json.dumps(reps).encode()).hexdigest(),
            'representatives': [list(map(list, r)) for r in reps],
        }
        if cfs != rds:
            self.reject('UNIVERSE_README_CERTFORMAT_MISMATCH', '%d/%d' % (len(rds - cfs), len(cfs - rds)))
        if not h1_ok:
            self.reject('UNIVERSE_H1_FAILS')
        if not size_ok or info['orbit_size_sum'] != len(cf):
            self.reject('UNIVERSE_ORBIT_ACCOUNTING')
        return info

    # -- duals
    def verify_dual(self, key, s):
        r = self.dual_cache.get(s)
        if r is not None:
            return r
        ent = self.duals.get(s)
        if ent is None:
            r = 'DUAL_MISSING'
        else:
            r = self.check_dual_entry(key, ent)
        self.dual_cache[s] = r
        return r

    def check_dual_entry(self, key, ent):
        if type(ent) is not dict or set(ent) != {'value', 'y'}:
            return 'DUAL_FORMAT'
        y = ent['y']
        if type(y) is not list or len(y) != len(key):
            return 'DUAL_LENGTH'
        try:
            ys = [rat(t, 'y') for t in y]
            val = rat(ent['value'], 'value')
        except CertError:
            return 'DUAL_BAD_RATIONAL'
        if any(t < 0 for t in ys):
            return 'DUAL_NEGATIVE'
        n = len(key)
        allowed = allowed_masks(tuple((it[2], it[3], it[4]) for it in key))
        sums = [Fraction(0)] * (1 << n)
        for m in range(1, 1 << n):
            low = (m & -m).bit_length() - 1
            sums[m] = sums[m & (m - 1)] + ys[low]
            if allowed[m] and sums[m] > 1:
                return 'DUAL_PACKING'
        obj = sum((Fraction(it[0], it[1]) * ys[x] for x, it in enumerate(key)), Fraction(0))
        if obj < 1:
            return 'DUAL_OBJECTIVE'
        if obj != val:
            self.dual_obj_value_mismatch += 1
        return 'OK'

    def verify_all_duals(self, raw):
        txt = gzip.decompress(raw).decode('utf-8')
        d = strict_json(txt)
        if type(d) is not dict:
            raise CertError('LP_DUALS_NOT_OBJECT')
        self.duals = d
        bad = {}
        for n_, s in enumerate(d):
            if not (n_ & 255):
                self.poll()
            try:
                key = parse_key_string(s)
            except CertError as e:
                bad[e.reason] = bad.get(e.reason, 0) + 1
                self.reject('LP_DUAL_KEY_' + e.reason, s)
                continue
            r = self.verify_dual(key, s)
            if r != 'OK':
                bad[r] = bad.get(r, 0) + 1
                self.reject('LP_DUAL_ENTRY_' + r, s)
        return {'entries': len(d), 'failed_by_reason': bad,
                'value_field_mismatches_informational': self.dual_obj_value_mismatch}

    # -- VFC signatures
    def verify_signatures(self, raw):
        txt = gzip.decompress(raw).decode('utf-8')
        vk = strict_json(txt)
        if type(vk) is not list:
            raise CertError('VFC_KILLED_NOT_LIST')
        killed = set()
        failed = {}
        nq = 0
        sizes = {}
        for n_, s in enumerate(vk):
            if not (n_ & 63):
                self.poll()
            try:
                if type(s) is not list or not s:
                    raise CertError('SIG_FORMAT')
                ent = []
                for e in s:
                    if type(e) is not list or len(e) != 5 or not all(is_int(x) for x in e):
                        raise CertError('SIG_FORMAT')
                    g_, a_, b2, b3, b5 = e
                    if not (2 <= g_ <= 6 and 1 <= a_ <= g_ - 1 and min(b2, b3, b5) >= 0):
                        raise CertError('SIG_ENTRY_RANGE', repr(e))
                    ent.append(tuple(e))
                t = tuple(ent)
                if list(t) != sorted(t):
                    raise CertError('SIG_UNSORTED')
                if t in killed:
                    raise CertError('SIG_DUPLICATE')
                for q in itertools.product(*[range(1, e[0] - e[1] + 1) for e in t]):
                    nq += 1
                    key, ks = key_from(t, q)
                    r = self.verify_dual(key, ks)
                    if r != 'OK':
                        raise CertError('SIG_Q_' + r, 'q=%r key=%s' % (q, ks))
                killed.add(t)
                sizes[len(t)] = sizes.get(len(t), 0) + 1
            except CertError as e:
                failed[e.reason] = failed.get(e.reason, 0) + 1
                self.reject('VFC_SIGNATURE_' + e.reason, '#%d %s %s' % (n_, json.dumps(s)[:120], e.detail))
        self.killed = killed
        return {'listed': len(vk), 'verified': len(killed), 'failed_by_reason': failed,
                'q_vectors_checked': nq, 'verified_by_size': {str(k): v for k, v in sorted(sizes.items())}}

    # -- RPLP witness
    def verify_rplp(self, pi, A, wit):
        if type(wit) is not list or len(wit) != 2:
            raise CertError('WITNESS_FORMAT')
        v, certs = wit
        if not is_int(v) or not 0 <= v < K or type(certs) is not list:
            raise CertError('WITNESS_FORMAT')
        N = [u for u in range(K) if u != v]
        n = len(N)

        def g(x, y):
            return gp(pi[x], pi[y])
        ent = []
        for u in N:
            gvu = g(v, u)
            b = tuple(pi[u][k] - vp(gvu, PRIMES[k]) for k in range(3))
            if min(b) < 0:
                raise CertError('NEGATIVE_B_VALUATION')
            ent.append((gvu, A[v][u]) + b)
        qlist = list(itertools.product(*[range(1, e[0] - e[1] + 1) for e in ent]))
        if len(certs) != len(qlist):
            raise CertError('RPLP_CERT_COUNT', '%d certs for %d q-vectors' % (len(certs), len(qlist)))
        forced = []
        for ia in range(n):
            for ib in range(n):
                if ia == ib:
                    continue
                ja, jb = N[ia], N[ib]
                tm = tri_tau_min(pi[v], pi[ja], pi[jb], A[v][ja], A[v][jb], A[ja][jb])
                if tm * g(v, ja) >= lcm(g(v, ja), g(v, jb)) * A[ja][jb] * A[v][ja]:
                    forced.append((ia, ib))          # X_a subset X_b: b in A forces a in A
        Asets = [m for m in range(1, 1 << n)
                 if all(not (m >> ib) & 1 or (m >> ia) & 1 for (ia, ib) in forced)]
        pairs = [(ia, ib) for ia in range(n) for ib in range(ia + 1, n)]
        pidx = {pr: k for k, pr in enumerate(pairs)}
        X = [Fraction(e[1], e[0]) for e in ent]
        yhi, ylo = [], []
        for (ia, ib) in pairs:
            j, k = N[ia], N[ib]
            ajk = A[j][k]
            ex = 1
            for idx, p in enumerate(PRIMES):
                ex *= p ** min(pi[v][idx], max(pi[j][idx], pi[k][idx]) + vp(ajk, p))
            ug = Fraction(1, ex)
            tm = tri_tau_min(pi[v], pi[j], pi[k], A[v][j], A[v][k], ajk)
            Lb = max(Fraction(tm, lcm(g(v, j), g(v, k)) * ajk), X[ia] + X[ib] - 1, Fraction(0))
            lo = ug * math.ceil(Lb / ug)
            mn = min(X[ia], X[ib])
            hi = ug * math.floor(mn / ug)
            if hi == mn:
                allow_jk = Fraction(A[v][j], g(v, j)) + Fraction(ajk, g(k, j)) < 1   # K2 for X_j in X_k
                allow_kj = Fraction(A[v][k], g(v, k)) + Fraction(ajk, g(j, k)) < 1   # K2 for X_k in X_j
                if X[ia] < X[ib]:
                    barred = not allow_jk
                elif X[ib] < X[ia]:
                    barred = not allow_kj
                else:
                    barred = not (allow_jk and allow_kj)
                if barred:
                    hi -= ug
            yhi.append(1 - X[ia] - X[ib] + hi)
            ylo.append(1 - X[ia] - X[ib] + lo)
        M = 1 << n
        nR = nP = 0
        for qi, (q, cert) in enumerate(zip(qlist, certs)):
            if type(cert) is not list or len(cert) != 2 or cert[0] not in ('R', 'P'):
                raise CertError('RPLP_CERT_FORMAT', 'q#%d' % qi)
            if cert[0] == 'R':
                key, ks = key_from(ent, q)
                if type(cert[1]) is not str or cert[1] != ks:
                    raise CertError('RPLP_R_KEY_MISMATCH', 'q#%d' % qi)
                r = self.verify_dual(key, ks)
                if r != 'OK':
                    raise CertError('RPLP_R_' + r, 'q#%d' % qi)
                nR += 1
                continue
            vec = cert[1]
            if type(vec) is not list or len(vec) != 2 * n + 2 * len(pairs):
                raise CertError('RPLP_P_LENGTH', 'q#%d' % qi)
            vals = [rat(s, 'P') for s in vec]
            av, bv = vals[0:n], vals[n:2 * n]
            uv, lv = vals[2 * n:2 * n + len(pairs)], vals[2 * n + len(pairs):]
            if any(x < 0 for x in uv) or any(x < 0 for x in lv):
                raise CertError('RPLP_P_NEGATIVE_UL', 'q#%d' % qi)
            dvs = tuple((vp(q[x], 2) + ent[x][2], vp(q[x], 3) + ent[x][3], vp(q[x], 5) + ent[x][4])
                        for x in range(n))
            allowed = allowed_masks(dvs)
            D = 1
            for x in vals:
                D = lcm(D, x.denominator)

            def sc(x):
                return x.numerator * (D // x.denominator)
            ai, bi = [sc(x) for x in av], [sc(x) for x in bv]
            wi = [sc(lv[k]) - sc(uv[k]) for k in range(len(pairs))]
            sa, sb, sp = [0] * M, [0] * M, [0] * M
            for m in range(1, M):
                low = (m & -m).bit_length() - 1
                rest = m & (m - 1)
                sa[m] = sa[rest] + ai[low]
                sb[m] = sb[rest] + bi[low]
                add = 0
                for y in range(n):
                    if (rest >> y) & 1:
                        add += wi[pidx[(min(low, y), max(low, y))]]
                sp[m] = sp[rest] + add
            for m in Asets:
                best = 0                        # S = empty
                sub = m
                while sub:
                    if allowed[sub] and sa[sub] > best:
                        best = sa[sub]
                    sub = (sub - 1) & m
                if sb[m] + sp[m] + best > D:
                    raise CertError('RPLP_P_STAR', 'q#%d A=%d' % (qi, m))
            obj = (sum((av[x] * Fraction(q[x], ent[x][0]) for x in range(n)), Fraction(0))
                   + sum((bv[x] * (1 - X[x]) for x in range(n)), Fraction(0))
                   - sum((uv[k] * yhi[k] for k in range(len(pairs))), Fraction(0))
                   + sum((lv[k] * ylo[k] for k in range(len(pairs))), Fraction(0)))
            if obj < 1:
                raise CertError('RPLP_P_OBJECTIVE', 'q#%d obj=%s' % (qi, obj))
            nP += 1
        return nR, nP

    # -- leaf lines
    def verify_leaf_lines(self, raw):
        txt = gzip.decompress(raw).decode('utf-8')
        if txt == '\n':
            self.notes.append('leaves.jsonl.gz decompresses to a single newline: zero leaf lines')
            parts = []
        else:
            if txt and not txt.endswith('\n'):
                raise CertError('LEAVES_NO_TRAILING_NEWLINE')
            parts = txt[:-1].split('\n') if txt else []
        good = 0
        nR = nP = 0
        rules = {}
        digits = re.compile(r'[1-5]{%d}' % len(EDGES))
        for ln, s in enumerate(parts):
            if not (ln & 15):
                self.poll()
            key = None
            try:
                if not s:
                    raise CertError('LEAF_EMPTY_LINE')
                obj = strict_json(s)
                if type(obj) is not dict or set(obj) != {'prof', 'canon', 'rep', 'rule', 'witness'}:
                    raise CertError('LEAF_LINE_KEYS')
                prof = obj['prof']
                if (type(prof) is not list or len(prof) != K or
                        any(type(p) is not list or len(p) != 3 or not all(is_int(x) for x in p) for p in prof)):
                    raise CertError('LEAF_PROF_FORMAT')
                pi = tuple(tuple(p) for p in prof)
                if pi not in self.rep_set:
                    raise CertError('LEAF_PROF_NOT_A_REPRESENTATIVE', repr(pi))
                canon, rep, rule = obj['canon'], obj['rep'], obj['rule']
                if type(canon) is not str or digits.fullmatch(canon) is None:
                    raise CertError('LEAF_CANON_FORMAT')
                if type(rep) is not str or digits.fullmatch(rep) is None:
                    raise CertError('LEAF_REP_FORMAT')
                rkey = rule if type(rule) is str else repr(rule)
                rules[rkey] = rules.get(rkey, 0) + 1
                A = [[0] * K for _ in range(K)]
                for (i, j), ch in zip(EDGES, rep):
                    a = int(ch)
                    if not 1 <= a <= gp(pi[i], pi[j]) - 1:
                        raise CertError('LEAF_REP_ALPHA_RANGE', rep)
                    A[i][j] = A[j][i] = a
                stab = stabilizer_perms(pi, self.roles)
                mine = ''.join(map(str, canonical_code(A, stab)))
                if mine != canon:
                    raise CertError('LEAF_REP_CANON_MISMATCH', 'canon=%s recomputed=%s' % (canon, mine))
                key = (pi, canon)
                if key in self.line_status:
                    self.line_status[key] = 'LEAF_LINE_DUPLICATE'
                    key = None
                    raise CertError('LEAF_LINE_DUPLICATE', canon)
                self.line_status[key] = 'PENDING'
                self.line_rep[key] = rep
                if rule != 'RPLP':
                    raise CertError('LEAF_RULE_UNSUPPORTED', repr(rule))
                r1, r2 = self.verify_rplp(pi, A, obj['witness'])
                nR += r1
                nP += r2
                self.line_status[key] = 'OK'
                good += 1
            except CertError as e:
                if key is not None:
                    self.line_status[key] = e.reason
                self.reject('LEAF_' + e.reason if not e.reason.startswith('LEAF_') else e.reason,
                            'line %d: %s' % (ln + 1, e.detail))
        return {'lines': len(parts), 'verified': good, 'rule_counts': rules,
                'R_certs_verified': nR, 'P_certs_verified': nP}

    # -- tree walk
    def walk_all(self):
        for ridx, pi in enumerate(self.reps):
            c0 = list(self.cnt)
            try:
                self.walk_rep(ridx, pi)
            except Stop as e:
                pref = []
                for (i, j) in EDGES:
                    a = self.cur_A[i][j]
                    if a == 0:
                        break
                    pref.append(a)
                self.frontier = {'stop_reason': e.reason, 'profile_index': ridx,
                                 'profile': [list(p) for p in pi], 'alpha_prefix_edge_order': pref,
                                 'profiles_completed': ridx, 'profiles_total': len(self.reps)}
                raise
            self.per_profile.append([ridx] + [self.cnt[k] - c0[k] for k in range(6)])

    def walk_rep(self, ridx, pi):
        P = [PID[p] for p in pi]
        g = [[gp(pi[i], pi[j]) if i != j else 0 for j in range(K)] for i in range(K)]
        W60 = [[(60 // g[i][j]) if i != j else 0 for j in range(K)] for i in range(K)]
        ENT = [[None] * K for _ in range(K)]
        for v in range(K):
            for u in range(K):
                if u != v:
                    gvu = g[v][u]
                    if gvu < 2:
                        raise CertError('INTERNAL_GCD_ONE')
                    b = tuple(pi[u][k] - vp(gvu, PRIMES[k]) for k in range(3))
                    if min(b) < 0:
                        raise CertError('NEGATIVE_B_VALUATION')
                    ENT[v][u] = [None] + [(gvu, a) + b for a in range(1, gvu)]
        A = [[0] * K for _ in range(K)]
        self.cur_A = A
        stab = stabilizer_perms(pi, self.roles)
        TM, LM, killed, cnt, used = self.T_memo, self.L_memo, self.killed, self.cnt, self.used_sigs

        def T_ok(h, i, j):
            key = ((((P[h] * NP + P[i]) * NP + P[j]) * 8 + A[h][i]) * 8 + A[h][j]) * 8 + A[i][j]
            r = TM.get(key)
            if r is None:
                r = tri_T_ok(pi[h], pi[i], pi[j], A[h][i], A[h][j], A[i][j])
                TM[key] = r
            return r

        def linked(v, a, b):
            key = ((((P[v] * NP + P[a]) * NP + P[b]) * 8 + A[v][a]) * 8 + A[v][b]) * 8 + A[a][b]
            r = LM.get(key)
            if r is None:
                r = linked_formula(pi[v], pi[a], pi[b], A[v][a], A[v][b], A[a][b])
                LM[key] = r
            return r

        def kp(t, i, j):
            for h in range(i):
                for (v, a, b) in ((h, i, j), (i, h, j), (j, h, i)):
                    if not linked(v, a, b):
                        continue
                    s0 = A[a][v] * W60[a][v] + A[b][v] * W60[b][v]
                    if s0 >= 60:
                        return True
                    cands = [u for u in range(K) if u != v and u != a and u != b
                             and EI[v][u] <= t and EI[a][u] <= t and EI[b][u] <= t
                             and linked(v, a, u) and linked(v, b, u)]
                    nc = len(cands)
                    if not nc:
                        continue
                    w = [A[u][v] * W60[u][v] for u in cands]
                    for m in range(1, 1 << nc):
                        idx = [x for x in range(nc) if (m >> x) & 1]
                        if s0 + sum(w[x] for x in idx) < 60:
                            continue
                        ok = True
                        for x in range(len(idx)):
                            for y in range(x + 1, len(idx)):
                                uu, ww = cands[idx[x]], cands[idx[y]]
                                if EI[uu][ww] > t or not linked(v, uu, ww):
                                    ok = False
                                    break
                            if not ok:
                                break
                        if ok:
                            return True
            return False

        einfo = []
        for t, (i, j) in enumerate(EDGES):
            nbi = tuple(u for u in range(K) if u != i and EI[i][u] <= t) if j >= 3 else None
            nbj = tuple(u for u in range(K) if u != j and EI[j][u] <= t) if i >= 2 else None
            if nbi is not None and len(nbi) != j:
                raise CertError('INTERNAL_DEGREE')
            if nbj is not None and len(nbj) != i + 1:
                raise CertError('INTERNAL_DEGREE')
            einfo.append((i, j, g[i][j], nbi, nbj))
        last = len(EDGES) - 1

        def rec(t):
            i, j, gij, nbi, nbj = einfo[t]
            Ai, Aj, Ei, Ej = A[i], A[j], ENT[i], ENT[j]
            for a in range(1, gij):
                Ai[j] = a
                Aj[i] = a
                cnt[0] += 1
                if not (cnt[0] & 4095):
                    self.poll()
                closed = 0
                for h in range(i):
                    if not T_ok(h, i, j):
                        closed = 1
                        break
                if not closed:
                    if nbi is not None:
                        sg = tuple(sorted([Ei[u][Ai[u]] for u in nbi]))
                        if sg in killed:
                            closed = 2
                            used.add(sg)
                    if not closed and nbj is not None:
                        sg = tuple(sorted([Ej[u][Aj[u]] for u in nbj]))
                        if sg in killed:
                            closed = 2
                            used.add(sg)
                if not closed and i >= 1 and kp(t, i, j):
                    closed = 3
                if closed:
                    cnt[closed] += 1
                    continue
                if t == last:
                    cnt[5] += 1
                    self.leaf(ridx, pi, A, stab)
                else:
                    cnt[4] += 1
                    rec(t + 1)
            Ai[j] = 0
            Aj[i] = 0

        rec(0)

    def leaf(self, ridx, pi, A, stab):
        cs = ''.join(map(str, canonical_code(A, stab)))
        key = (pi, cs)
        first = key not in self.reached
        self.reached[key] = self.reached.get(key, 0) + 1
        lab = ''.join(str(A[i][j]) for (i, j) in EDGES)
        if self.line_rep.get(key) == lab:
            self.rep_seen.add(key)
        if first:
            st = self.line_status.get(key)
            if st is None:
                self.reject('LEAF_LINE_MISSING', 'profile#%d %r canon=%s labelled=%s' % (ridx, pi, cs, lab))
            elif st != 'OK':
                self.reject('LEAF_WITNESS_NOT_VERIFIED', 'profile#%d canon=%s status=%s' % (ridx, cs, st))


def peak_rss_bytes():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r if sys.platform == 'darwin' else r * 1024


def now_iso():
    return time.strftime('%Y-%m-%dT%H:%M:%S%z')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--manifest', required=True)
    ap.add_argument('--universe', required=True, choices=sorted(CF_UNIVERSES))
    ap.add_argument('--out', required=True)
    ap.add_argument('--budget', type=float, default=1800.0)
    ap.add_argument('--fail-fast', action='store_true')
    args = ap.parse_args()
    if args.budget <= 0 or args.budget > 1800:
        print('budget must be in (0, 1800] s', file=sys.stderr)
        return 3
    out_fh = open(args.out, 'x')            # refuse to overwrite
    out_dir = os.path.dirname(os.path.abspath(args.out))
    signal.signal(signal.SIGTERM, _on_sigterm)
    src = open(os.path.abspath(__file__), 'rb').read()
    res = {
        'checker': os.path.abspath(__file__),
        'checker_sha256': hashlib.sha256(src).hexdigest(),
        'python': sys.version,
        'executable': sys.executable,
        'argv': sys.argv,
        'universe': args.universe,
        'fail_fast': args.fail_fast,
        'started_at': now_iso(),
        'budget_s': args.budget,
    }
    ck = Checker(args, out_dir)
    free0 = ck.sample_disk()
    res['admission_free_bytes'] = free0
    res['admission_required_bytes'] = DISK_ADMIT
    status = None
    if free0 < DISK_ADMIT:
        status = 'NOT_STARTED'
        res['not_started_reason'] = 'free %d < %d' % (free0, DISK_ADMIT)
    else:
        U = args.universe
        try:
            data = ck.load_inputs(args.manifest, U)
            res['manifest'] = os.path.abspath(args.manifest)
            res['manifest_sha256'] = ck.manifest_sha
            res['inputs'] = ck.input_records
            t = time.monotonic()
            res['universe_check'] = ck.build_universe(U)
            res['universe_check']['seconds'] = round(time.monotonic() - t, 3)
            t = time.monotonic()
            res['lp_duals_check'] = ck.verify_all_duals(data['lp_duals.json.gz'])
            res['lp_duals_check']['seconds'] = round(time.monotonic() - t, 3)
            t = time.monotonic()
            res['vfc_check'] = ck.verify_signatures(data['vfc_killed.json.gz'])
            res['vfc_check']['seconds'] = round(time.monotonic() - t, 3)
            t = time.monotonic()
            res['leaf_lines_check'] = ck.verify_leaf_lines(data['leaves.jsonl.gz'])
            res['leaf_lines_check']['seconds'] = round(time.monotonic() - t, 3)
            surv = strict_json(data['survivors.json'].decode('utf-8'))
            try:     # producer metadata, comparison only: floats allowed, duplicate keys still rejected
                run = json.loads(data['run.json'].decode('utf-8'), object_pairs_hook=_pairs_nodup)
            except (CertError, ValueError) as e:
                run = None
                ck.notes.append('run.json (comparison only) not parsed: %r' % (e,))
            t = time.monotonic()
            ck.walk_all()
            wsec = time.monotonic() - t
            c = ck.cnt
            reached_orbits = len(ck.reached)
            missing = sum(1 for k in ck.reached if ck.line_status.get(k) is None)
            unverified = sum(1 for k in ck.reached if ck.line_status.get(k) not in (None, 'OK'))
            extra = [k for k in ck.line_status if k not in ck.reached]
            res['walk'] = {
                'seconds': round(wsec, 3),
                'profiles_walked': len(ck.per_profile),
                'visits': c[0], 'closed_T': c[1], 'closed_VFC': c[2], 'closed_Kp': c[3],
                'passed_internal': c[4], 'leaves_labelled': c[5],
                'identity_visits_eq_sum': c[0] == c[1] + c[2] + c[3] + c[4] + c[5],
                'leaf_orbits_reached': reached_orbits,
                'reached_orbits_missing_line': missing,
                'reached_orbits_unverified_line': unverified,
                'lines_not_reached_by_walk': len(extra),
                'reps_equal_to_a_reached_labelled_leaf': len(ck.rep_seen),
                'vfc_listed_signatures_used_for_closures': len(ck.used_sigs),
                'T_memo_entries': len(ck.T_memo), 'linked_memo_entries': len(ck.L_memo),
                'per_profile_[idx,visits,T,VFC,Kp,passed,leaves]': ck.per_profile,
            }
            if not res['walk']['identity_visits_eq_sum']:
                ck.reject('INTERNAL_COUNT_IDENTITY')
            # survivors: SURVIVE lines must be exactly the survivors (expected: none)
            survive_lines = res['leaf_lines_check']['rule_counts'].get('SURVIVE', 0)
            my_survivors = missing + unverified
            res['survivors'] = {'survivors_json': surv, 'survive_lines': survive_lines,
                                'checker_unexcluded_orbits': my_survivors}
            if type(surv) is not list or surv != [] or survive_lines != 0 or my_survivors != 0:
                ck.reject('SURVIVORS_PRESENT_OR_MISMATCH', 'json=%r lines=%d checker=%d'
                          % (surv, survive_lines, my_survivors))
            # producer claims: comparison only, never premises
            st = run.get('stats', {}) if type(run) is dict else {}
            closed = st.get('closed', {}) if type(st) is dict else {}
            actual = {r['name']: r['sha256'] for r in ck.input_records}
            res['producer_comparison_informational'] = {
                'run_status': run.get('status') if type(run) is dict else None,
                'profiles_total': [run.get('profiles_total'), len(ck.reps)],
                'producer_nodes_vs_checker_[visits,passed_internal,passed_internal+leaves]':
                    [st.get('nodes'), [c[0], c[4], c[4] + c[5]]],
                'leaves': [st.get('leaves'), c[5]],
                'leaf_orbits': [st.get('leaf_orbits'), reached_orbits],
                'closed_T': [closed.get('T', 0), c[1]],
                'closed_VFC': [closed.get('VFC', 0), c[2]],
                'closed_Kp': [closed.get('Kp', 0), c[3]],
                'leaf_rule': [st.get('leaf_rule'), res['leaf_lines_check']['rule_counts']],
                'survivor_count': [run.get('survivor_count') if type(run) is dict else None, my_survivors],
                'output_sha256_match': {k: (run.get('output_sha256', {}).get(k) == actual.get(k))
                                        for k in ('leaves.jsonl.gz', 'vfc_killed.json.gz',
                                                  'lp_duals.json.gz', 'survivors.json')}
                if type(run) is dict and type(run.get('output_sha256')) is dict else None,
            }
            status = 'INVALID' if ck.rej_counts else 'COMPLETE_VALID'
        except Stop as e:
            status = 'INCOMPLETE'
            ck.incomplete.append(e.reason)
            res['frontier'] = ck.frontier
        except FailFast as e:
            status = 'INVALID'
            res['fail_fast_stop'] = str(e)
            res['frontier'] = ck.frontier
        except CertError as e:
            status = 'INVALID'
            ck.rejections.append({'reason': e.reason, 'detail': e.detail, 'fatal': True})
            ck.rej_counts[e.reason] = ck.rej_counts.get(e.reason, 0) + 1
        except Exception:
            status = 'INCOMPLETE'
            ck.incomplete.append('INTERNAL_EXCEPTION')
            res['traceback'] = traceback.format_exc()[-4000:]
        res.setdefault('inputs', getattr(ck, 'input_records', None))
        if 'walk' not in res:
            res['walk_partial_at_stop'] = {
                'visits': ck.cnt[0], 'closed_T': ck.cnt[1], 'closed_VFC': ck.cnt[2], 'closed_Kp': ck.cnt[3],
                'passed_internal': ck.cnt[4], 'leaves_labelled': ck.cnt[5],
                'profiles_completed': len(ck.per_profile), 'leaf_orbits_reached': len(ck.reached)}
        # fail closed: any definitive rejection -> INVALID; otherwise any stop/skip -> INCOMPLETE
        if ck.rej_counts:
            status = 'INVALID'
        elif ck.incomplete or status != 'COMPLETE_VALID':
            status = 'INCOMPLETE'
    try:
        ck.sample_disk()
    except OSError:
        pass
    ru = resource.getrusage(resource.RUSAGE_SELF)
    res.update({
        'status': status,
        'exit_code': EXIT[status],
        'rejection_counts': ck.rej_counts,
        'rejections_first_200': ck.rejections,
        'incomplete_reasons': ck.incomplete,
        'notes': ck.notes,
        'finished_at': now_iso(),
        'wall_seconds': round(time.monotonic() - ck.t0, 3),
        'cpu_user_s': round(ru.ru_utime, 3),
        'cpu_sys_s': round(ru.ru_stime, 3),
        'peak_rss_bytes': peak_rss_bytes(),
        'disk_min_free_bytes': ck.min_free,
        'disk_samples': ck.disk_samples,
        'sigterm_seen': STOP['flag'],
    })
    out_fh.write(json.dumps(res, sort_keys=True, indent=1) + '\n')
    out_fh.close()
    print('%s %s status=%s exit=%d wall=%.1fs rss=%d rejections=%s incomplete=%s'
          % (now_iso(), args.universe, status, EXIT[status], res['wall_seconds'], res['peak_rss_bytes'],
             json.dumps(ck.rej_counts, sort_keys=True), ck.incomplete))
    return EXIT[status]


if __name__ == '__main__':
    sys.exit(main())
