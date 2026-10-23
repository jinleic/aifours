#!/usr/bin/env python3
"""core7_engine_v3 -- profile engine for rules-k7-v1 + rules-k7-addendum-v1 (lane sun-coset7). EXPLORATORY.

v3 = v2 + cooperative stop guard + memory-light output writer (search logic unchanged):
  - every stop (self-budget, free disk < 12.0e9, peak RSS >= 0.9 GiB, SIGTERM) raises StopRun from
    Guard.tick(), so the run ends UNKNOWN through write_outputs with its exact frontier (profiles_done,
    profile_in_progress); SIGTERM only sets a flag that tick() reads; disk and peak RSS are read every 20 s;
  - write_outputs streams the certificate files through a bounded in-memory gzip compressor (no joined
    copy of the leaf text; no recomputation of the dual-key set).
Standard library only; deterministic; one process; self-budgeted (no external timeouts).
Usage:
  python3 core7_engine_v3.py UNIVERSE OUTDIR BUDGET_SECONDS
  UNIVERSE in: X1, MSP45, CORE5, K52, KII, K62, K63    (program-level list; each run still needs a parent GO)
               K53, K7                               (defined but NOT authorised to run)
  python3 core7_engine_v3.py CONTROLS OUTDIR BUDGET_SECONDS   (realisable-family soundness controls)

Rules (rules-k7-v1): T (L1, general gamma/ell), K (L2/L3 with K1, also on partial assignments by
deletion), VFC-LP (Corollary VFC-count, on partial and complete stars by deletion; exact duals for
every admissible q), P (L4, leaves), RPLP (sun-coset6 rules-k6-v3 L12 transcribed to general
g/gamma; leaves; exact dual or Farkas vectors). No FH rule in v1 (omission is sound).
Patterns are (profiles, alpha) with capped profiles (min(e,4), min(f,2), min(g,2)) (Lemma CAP).

Outputs (exclusive create in OUTDIR): run.json (status COMPLETE or UNKNOWN), vfc_killed.json.gz
(killed star signatures), lp_duals.json.gz (exact duals keyed by LP key), leaves.jsonl.gz (one line
per leaf orbit under the profile stabiliser: rule + witness, or SURVIVE), survivors.json.
"""
import hashlib
import itertools
import json
import os
import platform
import resource
import signal
import sys
import time
import zlib
from fractions import Fraction as F
from math import gcd

DISK_FLOOR = 12_000_000_000
DISK_EVERY = 20.0
RSS_CAP = int(0.9 * 1024 ** 3)  # bytes; peak resident set size that triggers a cooperative stop
PRIMES = (2, 3, 5)


def lcm(a, b):
    return a * b // gcd(a, b)


def vp(n, p):
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c


def gprof(p, q):
    return 2 ** min(p[0], q[0]) * 3 ** min(p[1], q[1]) * 5 ** min(p[2], q[2])


# ---------------------------------------------------------------- universes
DOM = {
    'C': [(e, f, g) for e in (1, 2, 3, 4) for f in (1, 2) for g in (0, 1, 2)],
    'D2': [(e, 0, g) for e in (1, 2, 3, 4) for g in (0, 1, 2)],
    'D2E': [(e, 0, g) for e in (2, 3, 4) for g in (0, 1, 2)],
    'D3': [(0, f, g) for f in (1, 2) for g in (0, 1, 2)],
    'X': [(e, 0, g) for e in (1, 2, 3, 4) for g in (1, 2)],
    'Y': [(0, f, g) for f in (1, 2) for g in (1, 2)],
    'P1': [(1, f, g) for f in (0, 1, 2) for g in (0, 1, 2)],
    'P4': [(e, f, g) for e in (2, 3, 4) for f in (0, 1, 2) for g in (0, 1, 2)],
    'Q4': [(e, f, g) for e in (2, 3, 4) for f in (0, 1, 2) for g in (0, 1, 2)],
}


def rp(a, b):
    return tuple(sorted((a, b)))


UNIVERSES = {
    'X1': (['D3', 'D3', 'C', 'C', 'C'], {rp('D3', 'D3'): {3}, rp('C', 'D3'): {3}, rp('C', 'C'): {6}}),
    'MSP45': (['P1', 'P4', 'P4', 'P4'], {rp('P1', 'P4'): {2}, rp('P4', 'P4'): {4}}),
    'CORE5': (['Q4'] * 5, {rp('Q4', 'Q4'): {4}}),
    'K52': (['D2E', 'D2E'] + ['C'] * 5, {rp('D2E', 'D2E'): {4}, rp('C', 'D2E'): {2, 4}, rp('C', 'C'): {6}}),
    'KII': (['X', 'Y'] + ['C'] * 5, {rp('X', 'Y'): {5}, rp('C', 'X'): {2, 4}, rp('C', 'Y'): {3}, rp('C', 'C'): {6}}),
    'K53': (['D3', 'D3'] + ['C'] * 5, {rp('D3', 'D3'): {3}, rp('C', 'D3'): {3}, rp('C', 'C'): {6}}),
    'K62': (['D2'] + ['C'] * 6, {rp('C', 'D2'): {2, 4}, rp('C', 'C'): {6}}),
    'K63': (['D3'] + ['C'] * 6, {rp('C', 'D3'): {3}, rp('C', 'C'): {6}}),
    'K7': (['C'] * 7, {rp('C', 'C'): {6}}),
}
AUTHORISED = {'X1', 'MSP45', 'CORE5', 'K52', 'KII', 'CONTROLS', 'K62', 'K63'}


def enumerate_profiles(roles, allowed):
    """All profile tuples, one per orbit under role-preserving permutations (non-decreasing within
    each maximal run of equal roles), with every pairwise gcd in the allowed set."""
    k = len(roles)
    out = []
    cur = []

    def rec(i):
        if i == k:
            out.append(tuple(cur))
            return
        dom = DOM[roles[i]]
        start = 0
        if i > 0 and roles[i - 1] == roles[i]:
            start = dom.index(cur[i - 1])
        for t in range(start, len(dom)):
            p = dom[t]
            if all(gprof(p, cur[j]) in allowed[rp(roles[i], roles[j])] for j in range(i)):
                cur.append(p)
                rec(i + 1)
                cur.pop()
    rec(0)
    return out


# ---------------------------------------------------------------- guard
class StopRun(Exception):
    pass


def peak_rss_bytes():
    """Peak resident set size of this process (ru_maxrss is bytes on macOS, KiB on Linux)."""
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r if sys.platform == 'darwin' else r * 1024


class Guard:
    """v3: no check raises outside tick(); tick() is the only place a stop is raised, and every stop ends
    the run UNKNOWN through write_outputs (exact frontier). SIGTERM only sets self.term."""

    def __init__(self, budget, outdir):
        self.t0 = time.time()
        self.budget = budget
        self.outdir = outdir
        self.last_disk = 0.0  # so the first tick() reads disk and RSS at once
        self.min_free = None
        self.max_rss = None
        self.term = False
        self.reason = None
        signal.signal(signal.SIGTERM, self._on_term)

    def _on_term(self, signum, frame):
        self.term = True

    def check_disk(self, force=False):
        now = time.time()
        if force or now - self.last_disk >= DISK_EVERY:
            st = os.statvfs(self.outdir)
            free = st.f_bavail * st.f_frsize
            self.last_disk = now
            self.min_free = free if self.min_free is None else min(self.min_free, free)
            rss = peak_rss_bytes()
            self.max_rss = rss
            if free < DISK_FLOOR:
                self.reason = 'free disk %d < 12.0e9' % free
                raise StopRun()
            if rss >= RSS_CAP:
                self.reason = 'peak RSS %d >= 0.9 GiB (%d bytes)' % (rss, RSS_CAP)
                raise StopRun()

    def tick(self):
        if self.term:
            self.reason = 'SIGTERM received (cooperative stop)'
            raise StopRun()
        if time.time() - self.t0 > self.budget:
            self.reason = 'self-budget %ds exceeded' % self.budget
            raise StopRun()
        self.check_disk()


GUARD = None


# ---------------------------------------------------------------- exact / float simplex (packing form)
def packing_exact(M, c):
    """max c.z s.t. M z <= 1, z >= 0 (exact, Bland). ('opt', val, z) or ('unb', c.d, d) with ray d."""
    m, n = len(M), len(c)
    T = [[F(x) for x in row] + [F(1 if r == i else 0) for r in range(m)] + [F(1)] for i, row in enumerate(M)]
    obj = [-F(x) for x in c] + [F(0)] * m + [F(0)]
    basis = [n + i for i in range(m)]
    while True:
        enter = next((j for j in range(n + m) if obj[j] < 0), None)
        if enter is None:
            z = [F(0)] * n
            for i, b in enumerate(basis):
                if b < n:
                    z[b] = T[i][-1]
            return 'opt', obj[-1], z
        leave, best = None, None
        for i in range(m):
            if T[i][enter] > 0:
                ratio = T[i][-1] / T[i][enter]
                if best is None or ratio < best or (ratio == best and basis[i] < basis[leave]):
                    best, leave = ratio, i
        if leave is None:
            d = [F(0)] * n
            if enter < n:
                d[enter] = F(1)
            for i, b in enumerate(basis):
                if b < n:
                    d[b] = -T[i][enter]
            return 'unb', sum(F(x) * y for x, y in zip(c, d)), d
        pv = T[leave][enter]
        T[leave] = [x / pv for x in T[leave]]
        for i in range(m):
            if i != leave and T[i][enter] != 0:
                f = T[i][enter]
                T[i] = [a - f * b for a, b in zip(T[i], T[leave])]
        f = obj[enter]
        obj = [a - f * b for a, b in zip(obj, T[leave])]
        basis[leave] = enter


def packing_float(M, c, tol=1e-9):
    m, n = len(M), len(c)
    T = [list(map(float, row)) + [1.0 if r == i else 0.0 for r in range(m)] + [1.0] for i, row in enumerate(M)]
    obj = [-float(x) for x in c] + [0.0] * m + [0.0]
    basis = [n + i for i in range(m)]
    for _ in range(50000):
        enter = next((j for j in range(n + m) if obj[j] < -tol), None)
        if enter is None:
            z = [0.0] * n
            for i, b in enumerate(basis):
                if b < n:
                    z[b] = T[i][-1]
            return 'opt', obj[-1], z
        leave, best = None, None
        for i in range(m):
            if T[i][enter] > tol:
                ratio = T[i][-1] / T[i][enter]
                if best is None or ratio < best - 1e-12 or (abs(ratio - best) <= 1e-12 and basis[i] < basis[leave]):
                    best, leave = ratio, i
        if leave is None:
            d = [0.0] * n
            if enter < n:
                d[enter] = 1.0
            for i, b in enumerate(basis):
                if b < n:
                    d[b] = -T[i][enter]
            return 'unb', sum(float(x) * y for x, y in zip(c, d)), d
        pv = T[leave][enter]
        T[leave] = [x / pv for x in T[leave]]
        for i in range(m):
            if i != leave and T[i][enter] != 0.0:
                f = T[i][enter]
                T[i] = [a - f * b for a, b in zip(T[i], T[leave])]
        f = obj[enter]
        obj = [a - f * b for a, b in zip(obj, T[leave])]
        basis[leave] = enter
    return 'iter', None, None


def verify_packing(M, c, z):
    if any(x < 0 for x in z):
        return False
    for row in M:
        if sum(a * b for a, b in zip(row, z) if a) > 1:
            return False
    return sum(a * b for a, b in zip(c, z)) >= 1


# ---------------------------------------------------------------- VFC LP (keyed, exact duals)
LPMEMO = {}   # key -> (value, y)


def allowed_masks(dvals):
    """Hereditary-allowed subsets (bitmasks) of entries with local-index valuations dvals[x] = (v2,v3,v5)."""
    n = len(dvals)
    g = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if x != y:
                g[x][y] = 2 ** min(dvals[x][0], dvals[y][0]) * 3 ** min(dvals[x][1], dvals[y][1]) * 5 ** min(dvals[x][2], dvals[y][2])
    ok = {}
    for mask in sorted(range(1, 1 << n), key=lambda m: bin(m).count('1')):
        mem = [x for x in range(n) if mask >> x & 1]
        s = len(mem)
        if s == 1:
            ok[mask] = True
            continue
        good = max(g[x][y] for x, y in itertools.combinations(mem, 2)) >= s
        ok[mask] = good and all(ok[mask ^ (1 << x)] for x in mem)
    return [m for m in ok if ok[m]]


def lp_solve(key):
    if key in LPMEMO:
        return LPMEMO[key]
    n = len(key)
    c = [F(e[0], e[1]) for e in key]
    dvals = [(e[2], e[3], e[4]) for e in key]
    allm = allowed_masks(dvals)
    maxm = [m for m in allm if not any((m | o) == o and m != o for o in allm)]
    M = [[1 if m >> x & 1 else 0 for x in range(n)] for m in maxm]
    st, val, y = packing_exact(M, c)
    res = (val, tuple(y))
    LPMEMO[key] = res
    return res


def lp_key_for(entries, q):
    """entries[x] = (g, alpha, b2, b3, b5); q[x] in [1, g-alpha]. Returns sorted key."""
    ks = []
    for (g, al, b2, b3, b5), qq in zip(entries, q):
        fr = F(qq, g)
        ks.append((fr.numerator, fr.denominator, vp(qq, 2) + b2, vp(qq, 3) + b3, vp(qq, 5) + b5))
    return tuple(sorted(ks))


SIGMEMO = {}  # signature -> killed (bool)


def vfc_signature_killed(sig):
    """sig = sorted tuple of (g, alpha, b2, b3, b5). Killed iff every admissible q has LP value >= 1."""
    if sig in SIGMEMO:
        return SIGMEMO[sig]
    killed = True
    n_q = 0
    for q in itertools.product(*[range(1, g - al + 1) for (g, al, _, _, _) in sig]):
        n_q += 1
        if (n_q & 255) == 0:
            GUARD.tick()
        val, _ = lp_solve(lp_key_for(sig, q))
        if val < 1:
            killed = False
            break
    SIGMEMO[sig] = killed
    return killed


# ---------------------------------------------------------------- pattern machinery
class Engine:
    def __init__(self, prof):
        self.prof = prof
        k = self.k = len(prof)
        self.G = [[gprof(prof[i], prof[j]) if i != j else 0 for j in range(k)] for i in range(k)]
        self.A = [[0] * k for _ in range(k)]
        self.E = [(i, j) for i in range(k) for j in range(i + 1, k)]
        self.tri_at = {}
        for t, (i, j) in enumerate(self.E):
            self.tri_at[t] = [(h, i, j) for h in range(i)]
        # stabiliser of the profile tuple (vertices with equal role and profile are interchangeable)
        self.stab = None
        self.tmcache = {}

    def set_stab(self, roles):
        k = self.k
        groups = {}
        for v in range(k):
            groups.setdefault((roles[v], self.prof[v]), []).append(v)
        glist = list(groups.values())
        perms = []
        for parts in itertools.product(*[itertools.permutations(gr) for gr in glist]):
            p = [0] * k
            for gr, img in zip(glist, parts):
                for a, b in zip(gr, img):
                    p[a] = b
            perms.append(tuple(p))
        self.stab = perms

    # ----- T
    def taumin(self, a, b, c):
        A, G, P = self.A, self.G, self.prof
        key = (a, b, c, A[a][b], A[a][c], A[b][c])
        r = self.tmcache.get(key)
        if r is not None:
            return r
        t = 1
        for x, y, z in ((a, b, c), (a, c, b), (b, c, a)):
            al = A[x][y]
            gz = lcm(G[x][z], G[y][z])
            gg = 1
            for idx, p in enumerate(PRIMES):
                le = P[z][idx] - vp(gz, p)
                gg *= p ** min(vp(al, p), le)
            t = lcm(t, al // gg)
        self.tmcache[key] = t
        return t

    def taumax(self, a, b, c):
        A, G = self.A, self.G
        best = None
        for y, x, z in ((a, b, c), (b, a, c), (c, a, b)):
            gy = lcm(G[x][y], G[y][z])
            bound = F(gy * A[x][z]) * min(F(A[x][y], G[x][y]), F(A[y][z], G[y][z]))
            bv = bound.numerator // bound.denominator
            best = bv if best is None else min(best, bv)
        return best

    def t_ok(self, a, b, c):
        return self.taumin(a, b, c) <= self.taumax(a, b, c)

    # ----- K
    def linked(self, v, i, j):
        A, G = self.A, self.G
        tm = self.taumin(*sorted((i, v, j)))
        if tm * G[i][v] >= lcm(G[i][v], G[i][j]) * A[v][j] * A[i][v]:
            return True
        if tm * G[j][v] >= lcm(G[j][v], G[j][i]) * A[v][i] * A[j][v]:
            return True
        return False

    def k_partial(self, h, i, j):
        """After triangle {h,i,j} is completed: K at each apex for sets S containing the other two."""
        A, G = self.A, self.G
        for v, a, b in ((h, i, j), (i, h, j), (j, h, i)):
            if not self.linked(v, a, b):
                continue
            nb = [u for u in range(self.k) if u != v and A[v][u] and u not in (a, b)]
            for r in range(0, len(nb) + 1):
                for extra in itertools.combinations(nb, r):
                    S = (a, b) + extra
                    if sum(F(A[u][v], G[u][v]) for u in S) < 1:
                        continue
                    if all(A[x][y] for x, y in itertools.combinations(S, 2)) and all(
                            self.linked(v, x, y) for x, y in itertools.combinations(S, 2)):
                        return ('K', v, sorted(S))
        return None

    def k_full(self):
        A, G, k = self.A, self.G, self.k
        for v in range(k):
            oth = [w for w in range(k) if w != v]
            for r in range(2, len(oth) + 1):
                for S in itertools.combinations(oth, r):
                    if sum(F(A[u][v], G[u][v]) for u in S) >= 1 and all(
                            self.linked(v, x, y) for x, y in itertools.combinations(S, 2)):
                        return ('K', v, list(S))
        return None

    # ----- VFC
    def vfc_sig(self, v):
        A, G, P = self.A, self.G, self.prof
        ent = []
        for j in range(self.k):
            if j != v and A[v][j]:
                g = G[v][j]
                ent.append((g, A[v][j]) + tuple(P[j][idx] - vp(g, p) for idx, p in enumerate(PRIMES)))
        return tuple(sorted(ent))

    # ----- P
    def p_bounds(self, v, j, kk):
        A, G, P = self.A, self.G, self.prof
        a = A[j][kk]
        gg = 1
        for idx, p in enumerate(PRIMES):
            gg *= p ** min(P[v][idx], max(P[j][idx], P[kk][idx]) + vp(a, p))
        u = F(1, gg)
        Xj, Xk = F(A[v][j], G[v][j]), F(A[v][kk], G[v][kk])
        gam = lcm(G[v][j], G[v][kk])
        lb = max(F(self.taumin(*sorted((v, j, kk))), gam * a), Xj + Xk - 1, F(0))
        q = lb / u
        lo = (-((-q.numerator) // q.denominator)) * u
        mm = min(Xj, Xk)
        q = mm / u
        hi = (q.numerator // q.denominator) * u
        if hi == mm:
            def k2ok(v_, j_, k_):  # U_v U_j subset U_v U_k allowed?
                return F(A[v_][j_], G[v_][j_]) + F(A[k_][j_], G[k_][j_]) < 1
            if Xj < Xk:
                ok = k2ok(v, j, kk)
            elif Xk < Xj:
                ok = k2ok(v, kk, j)
            else:
                ok = k2ok(v, j, kk) and k2ok(v, kk, j)
            if not ok:
                hi -= u
        return lo, hi

    def rule_p(self):
        A, G, k = self.A, self.G, self.k
        for v in range(k):
            oth = [w for w in range(k) if w != v]
            X = {j: F(A[v][j], G[v][j]) for j in oth}
            his = {}
            for j, kk in itertools.combinations(oth, 2):
                lo, hi = self.p_bounds(v, j, kk)
                if lo > hi:
                    return ('Ppair', v, [j, kk])
                his[(j, kk)] = hi
            for r in range(2, len(oth) + 1):
                for S in itertools.combinations(oth, r):
                    tot = sum(1 - X[j] for j in S) - sum(1 - X[j] - X[kk] + his[(j, kk)] for j, kk in itertools.combinations(S, 2))
                    if tot >= 1:
                        return ('PB', v, list(S))
        return None

    # ----- RPLP
    def forced(self, v, w, j):
        """X_w subset X_j forced (T3 at apex v of {v,w,j})."""
        A, G = self.A, self.G
        tm = self.taumin(*sorted((v, w, j)))
        return tm * G[v][w] >= lcm(G[v][w], G[v][j]) * A[w][j] * A[v][w]

    def rplp_vertex(self, v):
        A, G, P, k = self.A, self.G, self.prof, self.k
        oth = [w for w in range(k) if w != v]
        n = len(oth)
        pairs = list(itertools.combinations(range(n), 2))
        lohi = [self.p_bounds(v, oth[a], oth[b]) for a, b in pairs]
        forced = [(a, b) for a in range(n) for b in range(n) if a != b and self.forced(v, oth[a], oth[b])]
        ent = [(G[v][j], A[v][j]) + tuple(P[j][idx] - vp(G[v][j], p) for idx, p in enumerate(PRIMES)) for j in oth]
        certs = []
        for q in itertools.product(*[range(1, G[v][j] - A[v][j] + 1) for j in oth]):
            GUARD.tick()
            key = lp_key_for(ent, q)
            val, _ = lp_solve(key)
            if val >= 1:
                certs.append(['R', key_str(key)])
                continue
            dv = [(vp(qq, 2) + e[2], vp(qq, 3) + e[3], vp(qq, 5) + e[4]) for e, qq in zip(ent, q)]
            allm = set(allowed_masks(dv))
            cols = []
            for amask in range(1, 1 << n):
                if any((amask >> b & 1) and not (amask >> a & 1) for a, b in forced):
                    continue
                sub = amask
                smasks = [0]
                s = amask
                while s:
                    smasks.append(s)
                    s = (s - 1) & amask
                for sm in smasks:
                    if sm == 0 or sm in allm:
                        cols.append((amask, sm))
            M = []
            for am, sm in cols:
                sa = [1 if sm >> x & 1 else 0 for x in range(n)]
                aa = [1 if am >> x & 1 else 0 for x in range(n)]
                pp = [1 if (am >> a & 1 and am >> b & 1) else 0 for a, b in pairs]
                M.append(sa + [-x for x in sa] + aa + [-x for x in aa] + [-x for x in pp] + pp)
            c = [F(qq, G[v][j]) for qq, j in zip(q, oth)] + [-F(qq, G[v][j]) for qq, j in zip(q, oth)]
            c += [1 - F(A[v][j], G[v][j]) for j in oth] + [-(1 - F(A[v][j], G[v][j])) for j in oth]
            yhi, ylo = [], []
            for (a, b), (lo, hi) in zip(pairs, lohi):
                j, kk = oth[a], oth[b]
                base = 1 - F(A[v][j], G[v][j]) - F(A[v][kk], G[v][kk])
                yhi.append(base + hi)
                ylo.append(base + lo)
            c += [-x for x in yhi] + ylo
            z = rplp_dual(M, c)
            if z is None:
                return None
            npair = len(pairs)
            vec = [z[i] - z[n + i] for i in range(n)] + [z[2 * n + i] - z[3 * n + i] for i in range(n)]
            vec += list(z[4 * n:4 * n + npair]) + list(z[4 * n + npair:4 * n + 2 * npair])
            certs.append(['P', [str(x) for x in vec]])
        return ('RPLP', v, certs)

    def rule_rplp(self):
        for v in range(self.k):
            r = self.rplp_vertex(v)
            if r is not None:
                return r
        return None

    def canon(self):
        A = self.A
        best = None
        for p in self.stab:
            code = tuple(A[p[i]][p[j]] for i, j in self.E)
            if best is None or code < best:
                best = code
        return best


def rplp_dual(M, c):
    st, val, z = packing_float(M, c)
    if st == 'opt' and val < 1 - 1e-9:
        return None
    if st == 'opt':
        zf = [F(x).limit_denominator(100000) if x > 1e-12 else F(0) for x in z]
        if verify_packing(M, c, zf):
            return zf
    if st == 'unb' and val is not None and val > 1e-12:
        zf = [F(x / val).limit_denominator(100000) if x > 1e-12 else F(0) for x in z]
        if verify_packing(M, c, zf):
            return zf
    st, val, z = packing_exact(M, c)
    if st == 'opt':
        return z if val >= 1 else None
    if st == 'unb' and val > 0:
        zf = [x / val for x in z]
        if verify_packing(M, c, zf):
            return zf
    return None


def key_str(key):
    return ';'.join('%d/%d,%d,%d,%d' % e for e in key)


# ---------------------------------------------------------------- tree walk
def run_tree(eng, roles, stats, leafmemo, survivors, leaflines):
    k = eng.k
    E = eng.E
    A = eng.A
    G = eng.G
    deg = [0] * k
    eng.set_stab(roles)

    def rec(t):
        GUARD.tick()
        stats['nodes'] += 1
        if t == len(E):
            stats['leaves'] += 1
            c = eng.canon()
            if c in leafmemo:
                return
            w = eng.k_full() or eng.rule_p() or eng.rule_rplp()
            code = ''.join(map(str, c))
            leafmemo[c] = w[0] if w else 'SURVIVE'
            rec_line = {'prof': [list(p) for p in eng.prof], 'canon': code,
                        'rep': ''.join(str(A[i][j]) for i, j in E), 'rule': w[0] if w else 'SURVIVE'}
            if w:
                rec_line['witness'] = list(w[1:])
                stats['leaf_rule'][w[0]] = stats['leaf_rule'].get(w[0], 0) + 1
            else:
                stats['leaf_rule']['SURVIVE'] = stats['leaf_rule'].get('SURVIVE', 0) + 1
                survivors.append(rec_line)
            leaflines.append(json.dumps(rec_line, separators=(',', ':')))
            return
        i, j = E[t]
        for al in range(1, G[i][j]):
            A[i][j] = A[j][i] = al
            closed = None
            for (h, a, b) in eng.tri_at[t]:
                if not eng.t_ok(h, a, b):
                    closed = 'T'
                    break
            if closed is None:
                deg[i] += 1
                deg[j] += 1
                for v in (i, j):
                    if deg[v] >= 3 and vfc_signature_killed(eng.vfc_sig(v)):
                        closed = 'VFC'
                        stats['vfc_sigs_used'].add(eng.vfc_sig(v))
                        break
                if closed is None:
                    for (h, a, b) in eng.tri_at[t]:
                        if eng.k_partial(h, a, b):
                            closed = 'Kp'
                            break
                if closed is None:
                    rec(t + 1)
                deg[i] -= 1
                deg[j] -= 1
            if closed:
                stats['closed'][closed] = stats['closed'].get(closed, 0) + 1
        A[i][j] = A[j][i] = 0
    rec(0)


def run_universe(name, outdir, budget):
    global GUARD
    roles, allowed = UNIVERSES[name]
    GUARD = Guard(budget, outdir)
    profs = enumerate_profiles(roles, allowed)
    stats = {'universe': name, 'profiles': len(profs), 'profiles_done': 0, 'nodes': 0, 'leaves': 0,
             'closed': {}, 'leaf_rule': {}, 'vfc_sigs_used': set(), 'profile_in_progress': None}
    leafmemo_all = 0
    survivors, leaflines = [], []
    status = 'COMPLETE'
    try:
        for prof in profs:
            stats['profile_in_progress'] = [list(p) for p in prof]
            eng = Engine(prof)
            leafmemo = {}
            run_tree(eng, roles, stats, leafmemo, survivors, leaflines)
            leafmemo_all += len(leafmemo)
            stats['profiles_done'] += 1
        stats['profile_in_progress'] = None
    except StopRun:
        status = 'UNKNOWN'
    stats['leaf_orbits'] = leafmemo_all
    return status, profs, stats, survivors, leaflines


def _gz_bounded(chunks, limit):
    """v3: gzip-compress an iterable of byte chunks in memory without joining them; None if the
    compressed size exceeds limit (nothing is kept then)."""
    co = zlib.compressobj(9, zlib.DEFLATED, 31)
    out, size = [], 0
    for ch in chunks:
        b = co.compress(ch)
        if b:
            out.append(b)
            size += len(b)
            if size > limit:
                return None
    b = co.flush()
    out.append(b)
    size += len(b)
    return None if size > limit else b''.join(out)


def write_outputs(outdir, name, status, profs, stats, survivors, leaflines, extra=None):
    sha = hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest()
    used = sorted(stats.pop('vfc_sigs_used', set()))
    killed_sigs = [list(map(list, s)) for s in used]
    limit = 15 * 1024 * 1024
    # v3: duals for every memoised LP key of value >= 1, streamed in key-tuple order. This is exactly the
    # v1/v2 key set: vfc_signature_killed evaluates and memoises every q of each signature it kills (all of
    # value >= 1), and every RPLP "R" certificate cites a memoised key of value >= 1.
    keys = sorted(k for k, (val, y) in LPMEMO.items() if val >= 1)

    def dual_chunks():
        yield b'{'
        for i, key in enumerate(keys):
            val, y = LPMEMO[key]
            frag = json.dumps(key_str(key)) + ':' + json.dumps({'value': str(val), 'y': [str(x) for x in y]})
            yield ((',' if i else '') + frag).encode()
        yield b'}'

    surv = json.dumps(survivors, indent=1).encode()
    files = {
        'leaves.jsonl.gz': _gz_bounded(((line + '\n').encode() for line in leaflines), limit),
        'vfc_killed.json.gz': _gz_bounded([json.dumps(killed_sigs).encode()], limit),
        'lp_duals.json.gz': _gz_bounded(dual_chunks(), limit),
        'survivors.json': surv,
    }
    if any(b is None for b in files.values()) or sum(len(b) for b in files.values()) > limit:
        files = {'survivors.json': surv}
        status_note = 'outputs truncated: certificate files exceed 15 MiB and were not written'
    else:
        status_note = None
    hashes = {}
    for fn, b in files.items():
        with open(os.path.join(outdir, fn), 'xb') as f:
            f.write(b)
        hashes[fn] = hashlib.sha256(b).hexdigest()
    run = {'engine': 'core7_engine_v3', 'engine_sha256': sha, 'universe': name, 'status': status,
           'stop_reason': GUARD.reason, 'python': sys.version, 'platform': platform.platform(),
           'seconds': round(time.time() - GUARD.t0, 1), 'min_free_disk_bytes': GUARD.min_free,
           'profiles_total': len(profs), 'stats': stats, 'survivor_count': len(survivors),
           'lp_memo_entries': len(LPMEMO), 'sig_memo_entries': len(SIGMEMO),
           'output_sha256': hashes, 'note': status_note, 'exploratory': True,
           'sigterm_received': GUARD.term, 'rss_cap_bytes': RSS_CAP,
           'peak_rss_bytes_last_check': GUARD.max_rss, 'peak_rss_bytes_at_write': peak_rss_bytes()}
    if extra:
        run['extra'] = extra
    with open(os.path.join(outdir, 'run.json'), 'x') as f:
        json.dump(run, f, indent=1, default=str)
    return run


# ---------------------------------------------------------------- realisable controls
def perm_from_cycles(N, cycles):
    p = list(range(N + 1))
    for c in cycles:
        for i in range(len(c)):
            p[c[i]] = c[(i + 1) % len(c)]
    return tuple(p)


def pmul(p, q):
    return tuple(p[q[x]] for x in range(len(p)))


def closure(gens, N):
    e = tuple(range(N + 1))
    S, fr = {e}, [e]
    while fr:
        nf = []
        for x in fr:
            for g in gens:
                y = pmul(x, g)
                if y not in S:
                    S.add(y)
                    nf.append(y)
        fr = nf
    return frozenset(S)


def realised(G, subs, reps):
    k = len(subs)
    order = len(G)
    cos = [frozenset(pmul(g, u) for u in U) for U, g in zip(subs, reps)]
    disjoint = all(not (cos[i] & cos[j]) for i, j in itertools.combinations(range(k), 2))
    n = [order // len(U) for U in subs]
    prof = []
    for x in n:
        prof.append((min(vp(x, 2), 4), min(vp(x, 3), 2), min(vp(x, 5), 2)))
    eng = Engine(tuple(prof))
    for i, j in itertools.combinations(range(k), 2):
        I = order // len(subs[i] & subs[j])
        assert I % lcm(n[i], n[j]) == 0
        al = I // lcm(n[i], n[j])
        eng.A[i][j] = eng.A[j][i] = al
        assert gprof(prof[i], prof[j]) == gcd(n[i], n[j]), (n[i], n[j])
    # actual tau checks against T bounds
    tviol = []
    for a, b, c in itertools.combinations(range(k), 3):
        T = order // len(subs[a] & subs[b] & subs[c])
        L = lcm(lcm(n[a], n[b]), n[c])
        tau = T // L
        if T % L or tau % eng.taumin(a, b, c) or tau > eng.taumax(a, b, c):
            tviol.append([a, b, c, tau, eng.taumin(a, b, c), eng.taumax(a, b, c)])
    eng.stab = [tuple(range(k))]
    kills = {}
    kills['K'] = eng.k_full()
    kills['P'] = eng.rule_p()
    vf = []
    for v in range(k):
        if vfc_signature_killed(eng.vfc_sig(v)):
            vf.append(v)
    kills['VFC_vertices_killed'] = vf
    kills['RPLP'] = eng.rule_rplp()
    return {'n': n, 'disjoint': disjoint, 'alpha': {'%d%d' % (i, j): eng.A[i][j] for i, j in itertools.combinations(range(k), 2)},
            'T_violations': tviol, 'kills': {kk: (str(vv) if vv else vv) for kk, vv in kills.items()}}


def controls():
    out = {}
    N = 5
    c = lambda *cy: perm_from_cycles(N, cy)
    A5 = closure([c((1, 2, 3)), c((1, 2, 3, 4, 5))], N)
    D = closure([c((1, 2, 5, 3, 4)), c((1, 2), (4, 5))], N)
    T = closure([c((2, 3, 5)), c((1, 4), (2, 3))], N)
    V = closure([c((1, 2), (3, 4)), c((1, 3), (2, 4))], N)
    out['A5_6_6_6_10_15'] = realised(A5, [D, D, D, T, V], [c((1, 5, 3)), c((1, 4, 2, 3, 5)), c((1, 5, 2, 3, 4)), c((1, 2, 4)), c((3, 4, 5))])
    N = 6
    c = lambda *cy: perm_from_cycles(N, cy)
    G = closure([c((1, 2)), c((3, 4)), c((3, 4, 5, 6))], N)
    Aa = closure([c((3, 4, 5)), c((4, 5, 6))], N)
    P = closure([c((3, 6)), c((4, 5)), c((3, 4), (5, 6))], N)
    Q = closure([c((1, 2), (3, 4, 5, 6)), c((1, 2), (3, 5))], N)
    R = closure([c((1, 2)), c((3, 4), (5, 6)), c((3, 5), (4, 6))], N)
    out['C2xS4_4_6_6_6_6'] = realised(G, [Aa, P, P, Q, R], [c((1, 2)), c(), c((4, 5, 6)), c((1, 2), (4, 5)), c((1, 2), (3, 5, 4, 6))])
    K1 = closure([c((1, 2), (3, 6, 4, 5)), c((1, 2), (3, 5), (4, 6))], N)
    K2 = closure([c((3, 6)), c((3, 5, 6, 4))], N)
    K3 = closure([c((1, 2), (3, 6, 4, 5)), c((1, 2), (3, 4))], N)
    K4 = closure([c((1, 2)), c((1, 2), (3, 5), (4, 6)), c((1, 2), (3, 6), (4, 5))], N)
    Cc = closure([c((4, 6, 5))], N)
    out['C2xS4_6_6_6_6_16'] = realised(G, [K1, K2, K3, K4, Cc], [c(), c((3, 4, 5, 6)), c((1, 2), (3, 5)), c((1, 2), (3, 6)), c((1, 2))])
    N = 6
    c = lambda *cy: perm_from_cycles(N, cy)
    C6 = closure([c((1, 2, 3, 4, 5, 6))], N)
    triv = frozenset([tuple(range(N + 1))])
    el = sorted(C6)
    out['C6_six_cosets_of_trivial'] = realised(C6, [triv] * 6, el[:6])
    return out


def main():
    name, outdir, budget = sys.argv[1], sys.argv[2], float(sys.argv[3])
    if name not in AUTHORISED:
        raise SystemExit('universe %s is not authorised by the current parent GO' % name)
    os.makedirs(outdir, exist_ok=False)
    global GUARD
    if name == 'CONTROLS':
        GUARD = Guard(budget, outdir)
        status = 'COMPLETE'
        try:
            res = controls()
        except StopRun:
            status, res = 'UNKNOWN', {}
        rec = {'engine_sha256': hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(),
               'status': status, 'stop_reason': GUARD.reason, 'seconds': round(time.time() - GUARD.t0, 1),
               'min_free_disk_bytes': GUARD.min_free, 'controls': res, 'exploratory': True}
        with open(os.path.join(outdir, 'controls.json'), 'x') as f:
            json.dump(rec, f, indent=1, default=str)
        print(json.dumps({'status': status, 'families': list(res.keys())}))
        return
    status, profs, stats, survivors, leaflines = run_universe(name, outdir, budget)
    run = write_outputs(outdir, name, status, profs, stats, survivors, leaflines)
    print(json.dumps({'universe': name, 'status': status, 'profiles': len(profs),
                      'profiles_done': run['stats']['profiles_done'], 'nodes': run['stats']['nodes'],
                      'leaves': run['stats']['leaves'], 'leaf_orbits': run['stats']['leaf_orbits'],
                      'closed': run['stats']['closed'], 'leaf_rule': run['stats']['leaf_rule'],
                      'survivors': len(survivors), 'seconds': run['seconds']}))


if __name__ == '__main__':
    main()
