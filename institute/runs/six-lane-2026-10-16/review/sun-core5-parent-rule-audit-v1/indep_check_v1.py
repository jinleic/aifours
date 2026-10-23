#!/usr/bin/env python3
"""Parent audit sun-core5 v1: independent re-implementation (no worker code imported).

Written by the parent desk from its own re-derivation of rules-v1.md (L0-L8), proof-v1.md (Lemma R).
The worker's certificates.tsv.gz and survivors.json are READ as data only (to compare).

Usage: python3 indep_check_v1.py OUTDIR LANE_DIR
Writes OUTDIR/summary.json (exclusive create).  Standard library only, deterministic, one process.

Parts
  A  pattern universe: Burnside count, orbit enumeration, bijection with the worker's 21,150 codes.
  B  symbolic Core(5) closed forms (only the 2-/3-divisibility flags E2/E3 are used; no representative r):
     own classification T,K,P,N2,FH1,FH2 and verification of every worker witness; M1 checks;
     FH sensitivity (without the s=5 minimality clause; hereditary F2; smallest exponents).
  C  numeric general-index form at five explicit r-instances (L8/M2 validation, rule-by-rule).
  D  C1 shapes (2,2,2), (3,3,3,3), (2,4,4,4): own enumeration, general T/K/P at several instances.
  E  realisable controls in explicit permutation groups: rules must not fire; lemma predicates
     (L0.3, T1-T3, L2, L3, K2, P2-P5, PB bound, H1/F1-F3, Lemma R R1-R5, Core form of R) on actual data.
  F  S-D arithmetic replay of proof-v1 Steps 1-5 (symbolic).
"""
import gzip
import hashlib
import itertools
import json
import os
import sys
import time
from collections import Counter
from fractions import Fraction as Fr
from itertools import combinations, permutations, product
from math import gcd

INF = 10 ** 6


def lcm(a, b):
    return a * b // gcd(a, b)


def vp(x, p):
    c = 0
    while x % p == 0:
        x //= p
        c += 1
    return c


def ceil_to(x, u):
    q = x / u
    return (-((-q.numerator) // q.denominator)) * u


def floor_to(x, u):
    q = x / u
    return (q.numerator // q.denominator) * u


# =========================================================== A. universe
EDGES = list(combinations(range(5), 2))  # interface order used by the worker's codes
EIDX = {e: t for t, e in enumerate(EDGES)}
PERMS = list(permutations(range(5)))


def perm_src(pi):
    """new_alpha[s] = alpha[src[s]] when vertex i is relabelled pi[i]."""
    src = [None] * 10
    for t, (i, j) in enumerate(EDGES):
        a, b = pi[i], pi[j]
        src[EIDX[(min(a, b), max(a, b))]] = t
    return tuple(src)


PSRC = [(pi, perm_src(pi)) for pi in PERMS]


def burnside():
    ta = tp = 0
    for pi, src in PSRC:
        img = [None] * 10
        for s in range(10):
            img[src[s]] = s
        seen = [False] * 10
        c = 0
        for t in range(10):
            if not seen[t]:
                c += 1
                u = t
                while not seen[u]:
                    seen[u] = True
                    u = img[u]
        fix = sum(1 for i in range(5) if pi[i] == i)
        ta += 3 ** c
        tp += 3 ** c * (fix + 1) ** 2
    assert ta % 120 == 0 and tp % 120 == 0
    return ta // 120, tp // 120


def enumerate_universe():
    seen = set()
    reps = []
    for al in product((1, 2, 3), repeat=10):
        if al in seen:
            continue
        seen |= {tuple(al[src[s]] for s in range(10)) for _, src in PSRC}
        reps.append(al)
    pats = []
    for al in reps:
        stab = [pi for pi, src in PSRC if tuple(al[src[s]] for s in range(10)) == al]
        done = set()
        for e2 in (None, 0, 1, 2, 3, 4):
            for e3 in (None, 0, 1, 2, 3, 4):
                if (e2, e3) in done:
                    continue
                done |= {(None if e2 is None else pi[e2], None if e3 is None else pi[e3]) for pi in stab}
                pats.append((al, e2, e3))
    return reps, pats


def canon(al, e2, e3):
    best = None
    for pi, src in PSRC:
        k = tuple(al[src[s]] for s in range(10)) + (9 if e2 is None else pi[e2], 9 if e3 is None else pi[e3])
        if best is None or k < best:
            best = k
    return best


def parse_code(c):
    a, b = c.split("/")
    f = lambda ch: None if ch == "-" else int(ch)
    return tuple(int(ch) for ch in a), f(b[0]), f(b[1])


# =========================================================== B. symbolic Core(5) form
class Core:
    """Core(5) closed forms re-derived by the parent: n_i = 4 r_i, r pairwise coprime;
    gcd(r_z, a) for a in {1,2,3} is 2 iff (a=2, z=E2), 3 iff (a=3, z=E3), else 1."""

    def __init__(s, V, alpha, e2, e3):
        s.V = list(V)
        s.al = {}
        for (i, j), a in alpha.items():
            s.al[(i, j)] = a
            s.al[(j, i)] = a
        s.e2, s.e3 = e2, e3
        s._tm = {}

    def a(s, i, j):
        return s.al[(i, j)]

    def gr(s, z, a):
        if a == 2 and z == s.e2:
            return 2
        if a == 3 and z == s.e3:
            return 3
        return 1

    def tmin(s, x, y, z):  # (T1): alpha_pq | r_o * tau for each edge pq with opposite vertex o
        key = frozenset((x, y, z))
        if key not in s._tm:
            t = 1
            for p, q, o in ((x, y, z), (x, z, y), (y, z, x)):
                a = s.a(p, q)
                t = lcm(t, a // s.gr(o, a))
            s._tm[key] = t
        return s._tm[key]

    def tmax(s, x, y, z):  # (T2): tau <= product of any two alphas
        A, B, C = s.a(x, y), s.a(x, z), s.a(y, z)
        return min(A * B, A * C, B * C)

    def T_kill(s, tri):
        return s.tmin(*tri) > s.tmax(*tri)

    def link(s, v, i, j):  # K1 at v for {i,j}: tau = alpha_vi * alpha_vj (forced if it holds at tau_min)
        return s.tmin(v, i, j) == s.a(v, i) * s.a(v, j)

    def K_kill(s, v, S):  # L3: sum alpha_iv <= 3 when every pair of S is linked at v
        return len(S) >= 2 and all(s.link(v, i, j) for i, j in combinations(S, 2)) and sum(
            s.a(i, v) for i in S) >= 4

    def K2_allowed(s, v, j, k):  # U_vU_j subset U_vU_k  =>  alpha_vj + alpha_kj <= 3
        return s.a(v, j) + s.a(k, j) <= 3

    def pbounds(s, v, j, k):  # memoised wrapper (pure function of the pattern)
        key = (v, j, k)
        if key not in s.__dict__.setdefault("_pb", {}):
            s._pb[key] = s._pbounds(v, j, k)
        return s._pb[key]

    def _pbounds(s, v, j, k):  # in units of |G|
        Xj, Xk = Fr(s.a(v, j), 4), Fr(s.a(v, k), 4)
        u = Fr(1, 4 * s.gr(v, s.a(j, k)))  # (P2) double-coset increment
        lo = ceil_to(max(Fr(s.tmin(v, j, k), 4 * s.a(j, k)), Xj + Xk - 1, Fr(0)), u)  # (P3)
        m = min(Xj, Xk)
        hi = floor_to(m, u)
        if hi == m:  # (P4)
            if Xj < Xk:
                ok = s.K2_allowed(v, j, k)
            elif Xk < Xj:
                ok = s.K2_allowed(v, k, j)
            else:
                ok = s.K2_allowed(v, j, k) and s.K2_allowed(v, k, j)
            if not ok:
                hi -= u
        return lo, hi, u

    def Ppair_kill(s, v, j, k):
        lo, hi, _ = s.pbounds(v, j, k)
        return lo > hi

    def PB_val(s, v, S):  # (P5) Bonferroni with upper bounds hi
        X = {j: Fr(s.a(v, j), 4) for j in S}
        val = sum(1 - X[j] for j in S)
        for j, k in combinations(S, 2):
            val -= 1 - X[j] - X[k] + s.pbounds(v, j, k)[1]
        return val

    def PB_kill(s, v, S):
        return len(S) >= 2 and s.PB_val(v, S) >= 1

    def N2(s):
        return len(s.V) == 5 and all(s.a(i, j) == 2 for i, j in combinations(s.V, 2))

    # ---- L6 fibre lemma, gcd of lambda via valuations
    def lam_val(s, l, t, m, mode):
        er, fr = (INF, INF) if mode[0] == "sat" else (mode[1], mode[2])
        a2 = 2 + (er if l == s.e2 else 0) + vp(t, 2) - vp(m, 2)
        a3 = (fr if l == s.e3 else 0) + vp(t, 3)
        assert a2 >= 0
        return a2, a3

    def gcd_lam(s, x, tx, y, ty, m, mode):
        ax, ay = s.lam_val(x, tx, m, mode), s.lam_val(y, ty, m, mode)
        e, f = min(ax[0], ay[0]), min(ax[1], ay[1])
        assert e < INF and f < INF
        return 2 ** e * 3 ** f

    def fibre_admissible(s, m, inside, fixed, mode=("sat",), use_s5=True, hered=False):
        opts = {}
        for l in s.V:
            ts = [1] if l in inside else ([fixed[l]] if l in fixed else list(range(1, m + 1)))
            opts[l] = [(t, frozenset(M)) for t in ts for M in combinations(range(m), t)]
        for combo in product(*[opts[l] for l in s.V]):
            asg = dict(zip(s.V, combo))
            bad = False
            for l in s.V:  # (F3) for every vertex with t = 1, i.e. U_l inside H
                if asg[l][0] == 1:
                    for l2 in s.V:
                        if l2 != l and s.a(l, l2) * m > 4 * asg[l2][0]:
                            bad = True
                            break
                if bad:
                    break
            if bad:
                continue
            for c in range(m):  # (F2) traces in one coset of H
                S = [l for l in s.V if c in asg[l][1]]
                rs = range(2, len(S) + 1) if hered else ([len(S)] if len(S) >= 2 else [])
                for r in rs:
                    if r == 5 and not use_s5:
                        continue
                    for T in (combinations(S, r) if hered else [tuple(S)]):
                        if not any(s.gcd_lam(x, asg[x][0], y, asg[y][0], m, mode) >= r for x, y in combinations(T, 2)):
                            bad = True
                            break
                    if bad:
                        break
                if bad:
                    break
            if not bad:
                return True
        return False

    def H1_triangles(s):
        return [tri for tri in combinations(s.V, 3) if all(s.a(i, j) == 1 for i, j in combinations(tri, 2))]

    def FH1_kill(s, tri, **kw):
        return not s.fibre_admissible(4, list(tri), {}, **kw)

    def V2_of(s, x, y):
        return [v for v in s.V if v not in (x, y) and s.a(v, x) == 2 and s.a(v, y) == 2]

    def FH2_kill(s, x, y, **kw):
        if s.a(x, y) != 1:
            return False
        V2 = s.V2_of(x, y)
        if not V2:
            return False
        return (not s.fibre_admissible(4, [x, y], {v: 2 for v in V2}, **kw)) and (
            not s.fibre_admissible(2, [x, y] + V2, {}, **kw))

    def classify(s):
        for tri in combinations(s.V, 3):
            if s.T_kill(tri):
                return ("T", tri)
        for v in s.V:
            oth = [w for w in s.V if w != v]
            for r in range(2, len(oth) + 1):
                for S in combinations(oth, r):
                    if s.K_kill(v, S):
                        return ("K", v, S)
        for v in s.V:
            oth = [w for w in s.V if w != v]
            for j, k in combinations(oth, 2):
                if s.Ppair_kill(v, j, k):
                    return ("Ppair", v, (j, k))
            for r in range(2, len(oth) + 1):
                for S in combinations(oth, r):
                    if s.PB_kill(v, S):
                        return ("PB", v, S)
        if s.N2():
            return ("N2",)
        for tri in s.H1_triangles():
            if s.FH1_kill(tri):
                return ("FH1", tri)
        for x, y in combinations(s.V, 2):
            if s.FH2_kill(x, y):
                return ("FH2", (x, y))
        return None

    def hits(s, fh=True):
        h = {}
        others = lambda v: [w for w in s.V if w != v]
        h["T"] = any(s.T_kill(t) for t in combinations(s.V, 3))
        h["K"] = any(s.K_kill(v, S) for v in s.V for r in range(2, len(s.V)) for S in combinations(others(v), r))
        h["Ppair"] = any(s.Ppair_kill(v, j, k) for v in s.V for j, k in combinations(others(v), 2))
        h["PB"] = any(s.PB_kill(v, S) for v in s.V for r in range(2, len(s.V)) for S in combinations(others(v), r))
        h["N2"] = s.N2()
        if fh:
            h["FH1"] = any(s.FH1_kill(t) for t in s.H1_triangles())
            h["FH2"] = any(s.FH2_kill(x, y) for x, y in combinations(s.V, 2))
        return h


def core_from(al, e2, e3):
    return Core(range(5), {e: al[t] for t, e in enumerate(EDGES)}, e2, e3)


# =========================================================== C. numeric general-index form
class Gen:
    def __init__(s, n, alpha):
        s.n = list(n)
        s.k = len(n)
        s.V = list(range(s.k))
        s.al = {}
        for (i, j), a in alpha.items():
            s.al[(i, j)] = a
            s.al[(j, i)] = a
        s._tm = {}

    def a(s, i, j):
        return s.al[(i, j)]

    def g(s, i, j):
        return gcd(s.n[i], s.n[j])

    def I(s, i, j):
        return lcm(s.n[i], s.n[j]) * s.a(i, j)

    def P(s, i, j):
        return Fr(s.a(i, j), s.g(i, j))

    def L(s, x, y, z):
        return lcm(lcm(s.n[x], s.n[y]), s.n[z])

    def tmin(s, x, y, z):
        key = frozenset((x, y, z))
        if key not in s._tm:
            L = s.L(x, y, z)
            t = 1
            for p, q in ((x, y), (x, z), (y, z)):
                I = s.I(p, q)
                t = lcm(t, I // gcd(I, L))
            s._tm[key] = t
        return s._tm[key]

    def T3(s, y, x, z, tau):
        return Fr(s.L(x, y, z) * tau, s.n[y] * s.I(x, z))

    def tmax(s, x, y, z):
        best = None
        for yy in (x, y, z):
            xx, zz = [w for w in (x, y, z) if w != yy]
            b = min(s.P(yy, xx), s.P(yy, zz)) / s.T3(yy, xx, zz, 1)
            b = b.numerator // b.denominator
            best = b if best is None else min(best, b)
        return best

    def T_kill(s, tri):
        return s.tmin(*tri) > s.tmax(*tri)

    def link(s, v, i, j):
        t = s.tmin(v, i, j)
        return s.T3(i, v, j, t) == s.P(i, v) or s.T3(j, v, i, t) == s.P(j, v)

    def K_kill(s, v, S):
        return len(S) >= 2 and all(s.link(v, i, j) for i, j in combinations(S, 2)) and sum(s.P(i, v) for i in S) >= 1

    def K2_allowed(s, v, j, k):
        return s.P(v, j) + s.P(k, j) < 1

    def pbounds(s, v, j, k):  # memoised wrapper (pure function of the data)
        key = (v, j, k)
        if key not in s.__dict__.setdefault("_pb", {}):
            s._pb[key] = s._pbounds(v, j, k)
        return s._pb[key]

    def _pbounds(s, v, j, k):
        Xj, Xk = s.P(v, j), s.P(v, k)
        u = Fr(1, gcd(s.n[v], s.I(j, k)))
        lo = ceil_to(max(s.T3(v, j, k, s.tmin(v, j, k)), Xj + Xk - 1, Fr(0)), u)
        m = min(Xj, Xk)
        hi = floor_to(m, u)
        if hi == m:
            if Xj < Xk:
                ok = s.K2_allowed(v, j, k)
            elif Xk < Xj:
                ok = s.K2_allowed(v, k, j)
            else:
                ok = s.K2_allowed(v, j, k) and s.K2_allowed(v, k, j)
            if not ok:
                hi -= u
        return lo, hi, u

    def Ppair_kill(s, v, j, k):
        lo, hi, _ = s.pbounds(v, j, k)
        return lo > hi

    def PB_val(s, v, S):
        val = sum(1 - s.P(v, j) for j in S)
        for j, k in combinations(S, 2):
            val -= 1 - s.P(v, j) - s.P(v, k) + s.pbounds(v, j, k)[1]
        return val

    def PB_kill(s, v, S):
        return len(S) >= 2 and s.PB_val(v, S) >= 1

    def fibre_admissible(s, m, inside, fixed, use_s5=True):
        opts = {}
        for l in s.V:
            ts = [1] if l in inside else ([fixed[l]] if l in fixed else list(range(1, m + 1)))
            opts[l] = [(t, frozenset(M)) for t in ts if (s.n[l] * t) % m == 0 for M in combinations(range(m), t)]
        for combo in product(*[opts[l] for l in s.V]):
            asg = dict(zip(s.V, combo))
            bad = False
            for l in s.V:
                if asg[l][0] == 1:
                    for l2 in s.V:
                        if l2 != l and s.P(l, l2) > Fr(asg[l2][0], m):
                            bad = True
                            break
                if bad:
                    break
            if bad:
                continue
            lam = {l: s.n[l] * asg[l][0] // m for l in s.V}
            for c in range(m):
                S = [l for l in s.V if c in asg[l][1]]
                if len(S) < 2 or (len(S) == 5 and not use_s5):
                    continue
                if not any(gcd(lam[x], lam[y]) >= len(S) for x, y in combinations(S, 2)):
                    bad = True
                    break
            if not bad:
                return True
        return False

    def H1_triangles(s):
        out = []
        for tri in combinations(s.V, 3):
            if any(s.a(i, j) != 1 for i, j in combinations(tri, 2)):
                continue
            gs = {s.g(i, j) for i, j in combinations(tri, 2)}
            if len(gs) != 1:
                continue
            a = gs.pop()
            if any(s.n[x] % a for x in tri):
                continue
            q = [s.n[x] // a for x in tri]
            if all(gcd(q[i], q[j]) == 1 for i, j in combinations(range(3), 2)):
                out.append((tri, a))
        return out

    def hits(s, core=False, fh=True):
        others = lambda v: [w for w in s.V if w != v]
        h = {}
        h["T"] = any(s.T_kill(t) for t in combinations(s.V, 3))
        h["K"] = any(s.K_kill(v, S) for v in s.V for r in range(2, s.k) for S in combinations(others(v), r))
        h["Ppair"] = any(s.Ppair_kill(v, j, k) for v in s.V for j, k in combinations(others(v), 2))
        h["PB"] = any(s.PB_kill(v, S) for v in s.V for r in range(2, s.k) for S in combinations(others(v), r))
        h["N2"] = bool(core and s.k == 5 and all(s.a(i, j) == 2 for i, j in combinations(s.V, 2)))
        if fh:
            h["FH1"] = any(not s.fibre_admissible(a, list(tri), {}) for tri, a in s.H1_triangles())
            f2 = False
            if core:
                for x, y in combinations(s.V, 2):
                    if s.a(x, y) != 1:
                        continue
                    V2 = [v for v in s.V if v not in (x, y) and s.a(v, x) == 2 and s.a(v, y) == 2]
                    if V2 and not s.fibre_admissible(4, [x, y], {v: 2 for v in V2}) and not s.fibre_admissible(
                            2, [x, y] + V2, {}):
                        f2 = True
                        break
            h["FH2"] = f2
        return h


INSTANCES = {
    "I1_p5-17_x2_x3": ((5, 7, 11, 13, 17), 2, 3),
    "I2_p19-37_x4_x9": ((19, 23, 29, 31, 37), 4, 9),
    "I3_p5-17_x16_x81": ((5, 7, 11, 13, 17), 16, 81),
    "I4_p41-59_x128_x243": ((41, 43, 47, 53, 59), 128, 243),
    "I5_all1_x2_x3": ((1, 1, 1, 1, 1), 2, 3),
}


def inst_r(base, f2, f3, e2, e3, k=5):
    return [base[i] * (f2 if i == e2 else 1) * (f3 if i == e3 else 1) for i in range(k)]


# =========================================================== D. C1 shapes
def shape_patterns(d, amax, allowed2, allowed3, sym):
    k = len(d)
    E = list(combinations(range(k), 2))
    eidx = {e: t for t, e in enumerate(E)}

    def img(al, e2, e3, pi):
        new = [None] * len(E)
        for t, (i, j) in enumerate(E):
            a, b = pi[i], pi[j]
            new[eidx[(min(a, b), max(a, b))]] = al[t]
        return tuple(new) + (99 if e2 is None else pi[e2], 99 if e3 is None else pi[e3])

    seen = set()
    out = []
    for al in product(*[range(1, amax[e] + 1) for e in E]):
        for e2 in allowed2:
            for e3 in allowed3:
                key = al + (99 if e2 is None else e2, 99 if e3 is None else e3)
                if key in seen:
                    continue
                orb = {img(al, e2, e3, pi) for pi in sym}
                seen |= orb
                out.append((al, e2, e3))
    return E, out


def c1_shapes():
    res = {}
    specs = {
        "P42_(2,2,2)": ((2, 2, 2), [None, 0, 1, 2], [None, 0, 1, 2], list(permutations(range(3)))),
        "P43_(3,3,3,3)": ((3, 3, 3, 3), [None, 0, 1, 2, 3], [None, 0, 1, 2, 3], list(permutations(range(4)))),
        "P45_(2,4,4,4)_r1odd": ((2, 4, 4, 4), [None, 1, 2, 3], [None, 0, 1, 2, 3],
                                [(0,) + q for q in permutations((1, 2, 3))]),
    }
    for name, (d, a2, a3, sym) in specs.items():
        k = len(d)
        amax = {(i, j): gcd(d[i], d[j]) - 1 for i, j in combinations(range(k), 2)}
        E, pats = shape_patterns(d, amax, a2, a3, sym)
        per_inst = {}
        for iname, (base, f2, f3) in INSTANCES.items():
            killed = 0
            surv = []
            for al, e2, e3 in pats:
                r = inst_r(base, f2, f3, e2, e3, k)
                n = [d[i] * r[i] for i in range(k)]
                assert all(gcd(r[i], r[j]) == 1 for i, j in combinations(range(k), 2))
                Gn = Gen(n, {e: al[t] for t, e in enumerate(E)})
                h = Gn.hits(core=False, fh=False)
                if h["T"] or h["K"] or h["Ppair"] or h["PB"]:
                    killed += 1
                else:
                    surv.append([list(al), e2, e3])
            per_inst[iname] = {"killed_TKP": killed, "survivors": surv}
        res[name] = {"patterns": len(pats), "per_instance": per_inst}
    return res


# =========================================================== E. permutation-group controls
def pc(N, *cycles):
    p = list(range(N + 1))
    for c in cycles:
        for i in range(len(c)):
            p[c[i]] = c[(i + 1) % len(c)]
    return tuple(p)


def mul(p, q):  # functional composition: (p o q)(x) = p(q(x)); left coset gU = {g o u}
    return tuple(p[q[x]] for x in range(len(p)))


def inv(p):
    r = [0] * len(p)
    for x, y in enumerate(p):
        r[y] = x
    return tuple(r)


def gen_group(N, gens):
    e = tuple(range(N + 1))
    S = {e}
    fr = [e]
    while fr:
        nf = []
        for x in fr:
            for g in gens:
                y = mul(g, x)
                if y not in S:
                    S.add(y)
                    nf.append(y)
        fr = nf
    return frozenset(S)


def sprod(A, B):
    return frozenset(mul(a, b) for a in A for b in B)


def is_subgroup(H):
    return all(mul(a, inv(b)) in H for a in H for b in H)


def sun_pred(idx):
    """Sun's conclusion for a family of indices: some pair with gcd >= family size."""
    s = len(idx)
    return s < 2 or any(gcd(x, y) >= s for x, y in combinations(idx, 2))


def actual_checks(G, subs, reps):
    order = len(G)
    k = len(subs)
    Gs = set(G)
    cos = [frozenset(mul(g, u) for u in U) for U, g in zip(subs, reps)]
    disjoint = all(not (cos[i] & cos[j]) for i, j in combinations(range(k), 2))
    n = [order // len(U) for U in subs]
    alpha = {}
    for i, j in combinations(range(k), 2):
        I = order // len(subs[i] & subs[j])
        assert I % lcm(n[i], n[j]) == 0
        alpha[(i, j)] = I // lcm(n[i], n[j])
    gen = Gen(n, alpha)
    pr = {(i, j): sprod(subs[i], subs[j]) for i in range(k) for j in range(k) if i != j}
    viol = []
    for i, j in combinations(range(k), 2):
        if Fr(len(pr[(i, j)]), order) != gen.P(i, j):
            viol.append(["L0.3", i, j])
        if not 1 <= alpha[(i, j)] <= gen.g(i, j) - 1:
            viol.append(["alpha-range", i, j])
    for tri in combinations(range(k), 3):
        x, y, z = tri
        T = order // len(subs[x] & subs[y] & subs[z])
        L = gen.L(x, y, z)
        if T % L:
            viol.append(["L|T", tri])
            continue
        tau = T // L
        if tau % gen.tmin(*tri) or tau > gen.tmax(*tri):
            viol.append(["T1T2", tri, tau])
        for yy in tri:
            xx, zz = [w for w in tri if w != yy]
            Z = sprod(subs[yy], subs[xx] & subs[zz])
            if Fr(len(Z), order) != gen.T3(yy, xx, zz, tau):
                viol.append(["T3", tri, yy])
            if len(Z) == len(pr[(yy, xx)]) and not (pr[(yy, xx)] <= pr[(yy, zz)] and pr[(xx, yy)] <= pr[(zz, yy)]):
                viol.append(["L2", tri, yy])
    for v in range(k):
        oth = [w for w in range(k) if w != v]

        def cond(i, j):
            return pr[(v, i)] <= pr[(j, i)] or pr[(v, j)] <= pr[(i, j)]

        for r in range(2, len(oth) + 1):
            for S in combinations(oth, r):
                if all(cond(i, j) for i, j in combinations(S, 2)) and sum(len(pr[(i, v)]) for i in S) > order - len(subs[v]):
                    viol.append(["L3", v, S])
        X = {j: pr[(v, j)] for j in oth}
        for j, kk in combinations(oth, 2):
            lo, hi, u = gen.pbounds(v, j, kk)
            fr = Fr(len(X[j] & X[kk]), order)
            if (fr / u).denominator != 1 or fr < lo or fr > hi:
                viol.append(["P2P3P4", v, j, kk])
        for j, kk in permutations(oth, 2):
            if X[j] <= X[kk] and not gen.K2_allowed(v, j, kk):
                viol.append(["K2", v, j, kk])
        for r in range(2, len(oth) + 1):
            for S in combinations(oth, r):
                Y = {j: Gs - X[j] for j in S}
                lhs = sum(len(Y[j]) for j in S) - sum(len(Y[j] & Y[kk]) for j, kk in combinations(S, 2))
                if lhs > order - len(subs[v]):
                    viol.append(["P5", v, S])
                if gen.PB_val(v, S) > Fr(lhs, order):
                    viol.append(["PB-upper", v, S])
    # H1 + fibre lemma on actual data
    fchecks = []
    for tri, a in gen.H1_triangles():
        H = pr[(tri[0], tri[1])]
        ok = is_subgroup(H) and order // len(H) == a and all(subs[x] <= H for x in tri)
        ok = ok and all(pr[(p, q)] == H for p in tri for q in tri if p != q)
        if not ok:
            viol.append(["H1", tri])
            continue
        cosetsH = []
        seenH = set()
        for g in sorted(G):
            if g in seenH:
                continue
            C = frozenset(mul(g, h) for h in H)
            seenH |= C
            cosetsH.append(C)
        t = [len(subs[l]) // len(subs[l] & H) for l in range(k)]
        lam = [len(H) // len(subs[l] & H) for l in range(k)]
        for l in range(k):
            if n[l] * t[l] != a * lam[l] or sum(1 for C in cosetsH if C & cos[l]) != t[l]:
                viol.append(["F1", tri, l])
            if t[l] == 1:
                for l2 in range(k):
                    if l2 != l and Fr(len(pr[(l, l2)]), order) > Fr(t[l2], a):
                        viol.append(["F3", tri, l, l2])
        per_coset = []
        for C in cosetsH:
            S = [l for l in range(k) if C & cos[l]]
            hered = all(sun_pred([lam[l] for l in T]) for r in range(2, len(S) + 1) for T in combinations(S, r))
            per_coset.append({"S": S, "sun_pred_hereditary": hered})
            if not hered:
                viol.append(["F2", tri, S])
        fchecks.append({"triangle": list(tri), "a": a, "t": t, "lambda": lam, "cosets": per_coset})
    # Lemma R on actual data
    rinfo = []
    core_shape = all(x % 4 == 0 for x in n) and all(gcd(n[i] // 4, n[j] // 4) == 1 for i, j in combinations(range(k), 2))
    for v in range(k):
        h = inv(reps[v])
        tg = [mul(h, reps[i]) for i in range(k)]
        tcos = [frozenset(mul(tg[i], u) for u in subs[i]) for i in range(k)]
        Uv = subs[v]
        assert tcos[v] == Uv
        D, d = {}, {}
        for j in range(k):
            if j == v:
                continue
            Dj = frozenset(mul(mul(x, tg[j]), y) for x in Uv for y in subs[j])
            if Dj & pr[(v, j)]:
                viol.append(["R1", v, j])
            if len(Dj) == 0 or len(Dj) % (order // gcd(n[v], n[j])):
                viol.append(["R2", v, j])
            if len(Dj) % len(subs[j]):
                viol.append(["R-d-int", v, j])
            dj = len(Dj) // len(subs[j])
            seenC = set()
            for y in sorted(Dj):
                if y in seenC:
                    continue
                C = frozenset(mul(x, y) for x in Uv)
                seenC |= C
                piece = tcos[j] & C
                if not piece:
                    viol.append(["R3-meet", v, j])
                    continue
                w = min(piece)
                A = Uv & frozenset(mul(mul(w, b), inv(w)) for b in subs[j])
                if piece != frozenset(mul(x, w) for x in A) or len(Uv) // len(A) != dj:
                    viol.append(["R3-piece", v, j])
            if core_shape:
                sj = Fr(len(Dj) * 4, order)
                if sj.denominator != 1 or sj > 4 - alpha[(min(v, j), max(v, j))] or dj != sj * (n[j] // 4):
                    viol.append(["R-core-form", v, j])
            D[j], d[j] = Dj, dj
        seenR = set()
        ncos = 0
        for y in sorted(G):
            if y in seenR:
                continue
            C = frozenset(mul(x, y) for x in Uv)
            seenR |= C
            ncos += 1
            S = []
            for j in D:
                if C & D[j]:
                    if not C <= D[j]:
                        viol.append(["R-leftinv", v, j])
                    S.append(j)
            pieces = [tcos[j] & C for j in S]
            if any(p & q for p, q in combinations(pieces, 2)):
                viol.append(["R4-disjoint", v, S])
            if not all(sun_pred([d[j] for j in T]) for r in range(2, len(S) + 1) for T in combinations(S, r)):
                viol.append(["R4", v, S])
        for j, kk in combinations(sorted(D), 2):
            if D[j] & D[kk] and gcd(d[j], d[kk]) < 2:
                viol.append(["R5", v, j, kk])
        rinfo.append({"v": v, "d": {str(j): d[j] for j in sorted(d)},
                      "Dsize_over_G": {str(j): str(Fr(len(D[j]), order)) for j in sorted(D)}})
    data = {"order": order, "disjoint": disjoint, "n": n,
            "alpha": {f"{i}{j}": a for (i, j), a in sorted(alpha.items())}, "core_shape": core_shape}
    data["general_rule_hits"] = gen.hits(core=False)
    if core_shape:
        r = [x // 4 for x in n]
        e2 = [i for i in range(k) if r[i] % 2 == 0]
        e3 = [i for i in range(k) if r[i] % 3 == 0]
        assert len(e2) <= 1 and len(e3) <= 1
        q = Core(range(k), alpha, e2[0] if e2 else None, e3[0] if e3 else None)
        data["core_symbolic_hits"] = q.hits(fh=True)
        data["core_E2_E3"] = [e2[0] if e2 else None, e3[0] if e3 else None]
        if k == 5:
            g5 = Gen(n, alpha)
            data["core_numeric_hits"] = g5.hits(core=True)
    data["fibre_H1"] = fchecks
    data["lemmaR"] = rinfo
    data["violations"] = viol
    return data


def controls():
    out = {}
    # Menon Thm 3.1 (A5, (6,6,6,10,15)), generators and representatives as printed in arXiv:2608.15873v1
    N = 5
    A5 = frozenset(p for p in gen_group(N, [pc(N, (1, 2, 3)), pc(N, (1, 2, 3, 4, 5))]))
    D = gen_group(N, [pc(N, (1, 2, 5, 3, 4)), pc(N, (1, 2), (4, 5))])
    T = gen_group(N, [pc(N, (2, 3, 5)), pc(N, (1, 4), (2, 3))])
    Vv = gen_group(N, [pc(N, (1, 2), (3, 4)), pc(N, (1, 3), (2, 4))])
    reps = [pc(N, (1, 5, 3)), pc(N, (1, 4, 2, 3, 5)), pc(N, (1, 5, 2, 3, 4)), pc(N, (1, 2, 4)), pc(N, (3, 4, 5))]
    assert len(A5) == 60 and all(x <= A5 for x in (D, T, Vv)) and all(g in A5 for g in reps)
    out["A5_(6,6,6,10,15)"] = actual_checks(A5, [D, D, D, T, Vv], reps)
    full = [D, D, D, T, Vv]
    for drop in range(5):
        keep = [i for i in range(5) if i != drop]
        out[f"A5_drop{drop}"] = actual_checks(A5, [full[i] for i in keep], [reps[i] for i in keep])
    # Menon Sec 5 (C2 x S4 in S6): (4,6,6,6,6) and (6,6,6,6,16)
    N = 6
    G = gen_group(N, [pc(N, (1, 2)), pc(N, (3, 4)), pc(N, (3, 4, 5, 6))])
    A = gen_group(N, [pc(N, (3, 4, 5)), pc(N, (4, 5, 6))])
    P = gen_group(N, [pc(N, (3, 6)), pc(N, (4, 5)), pc(N, (3, 4), (5, 6))])
    Q = gen_group(N, [pc(N, (1, 2), (3, 4, 5, 6)), pc(N, (1, 2), (3, 5))])
    R = gen_group(N, [pc(N, (1, 2)), pc(N, (3, 4), (5, 6)), pc(N, (3, 5), (4, 6))])
    reps = [pc(N, (1, 2)), pc(N), pc(N, (4, 5, 6)), pc(N, (1, 2), (4, 5)), pc(N, (1, 2), (3, 5, 4, 6))]
    assert len(G) == 48
    full = [A, P, P, Q, R]
    out["C2xS4_(4,6,6,6,6)"] = actual_checks(G, full, reps)
    for drop in range(5):
        keep = [i for i in range(5) if i != drop]
        out[f"C2xS4_46666_drop{drop}"] = actual_checks(G, [full[i] for i in keep], [reps[i] for i in keep])
    K1 = gen_group(N, [pc(N, (1, 2), (3, 6, 4, 5)), pc(N, (1, 2), (3, 5), (4, 6))])
    K2 = gen_group(N, [pc(N, (3, 6)), pc(N, (3, 5, 6, 4))])
    K3 = gen_group(N, [pc(N, (1, 2), (3, 6, 4, 5)), pc(N, (1, 2), (3, 4))])
    K4 = gen_group(N, [pc(N, (1, 2)), pc(N, (1, 2), (3, 5), (4, 6)), pc(N, (1, 2), (3, 6), (4, 5))])
    C = gen_group(N, [pc(N, (4, 6, 5))])
    reps2 = [pc(N), pc(N, (3, 4, 5, 6)), pc(N, (1, 2), (3, 5)), pc(N, (1, 2), (3, 6)), pc(N, (1, 2))]
    out["C2xS4_(6,6,6,6,16)"] = actual_checks(G, [K1, K2, K3, K4, C], reps2)
    # k cosets of one subgroup
    for name, Nn, kk in (("Z5_five_cosets_of_1", 5, 5), ("Z4_four_cosets_of_1_core", 4, 4)):
        Z = gen_group(Nn, [pc(Nn, tuple(range(1, Nn + 1)))])
        one = frozenset([tuple(range(Nn + 1))])
        out[name] = actual_checks(Z, [one] * kk, sorted(Z)[:kk])
    # Core-shaped realisable 4-configurations (parent-chosen)
    N = 8
    a = pc(N, (1, 2), (3, 4), (5, 6), (7, 8))
    b = pc(N, (1, 3), (2, 4), (5, 7), (6, 8))
    c = pc(N, (1, 5), (2, 6), (3, 7), (4, 8))
    Z23 = gen_group(N, [a, b, c])
    e = tuple(range(N + 1))
    ab, abc = mul(a, b), mul(mul(a, b), c)
    line = lambda x: frozenset([e, x])
    out["Z2^3_four_lines_all_alpha2_core"] = actual_checks(Z23, [line(a), line(b), line(abc), line(c)], [e, c, b, ab])
    out["Z2^3_three_lines_plus_point_E2_core"] = actual_checks(Z23, [line(a), line(b), line(abc), frozenset([e])],
                                                                [e, c, b, ab])
    N = 4
    S4 = gen_group(N, [pc(N, (1, 2)), pc(N, (1, 2, 3, 4))])
    stab = lambda i: frozenset(g for g in S4 if g[i] == i)
    out["S4_four_point_stabilisers_all_alpha3_core"] = actual_checks(
        S4, [stab(1), stab(2), stab(3), stab(4)], [pc(N), pc(N, (1, 2)), pc(N, (1, 3)), pc(N, (1, 4))])
    out["S4_three_stabilisers_plus_C2_E3_core"] = actual_checks(
        S4, [stab(1), stab(2), stab(3), gen_group(N, [pc(N, (1, 2))])], [pc(N), pc(N, (1, 2)), pc(N, (1, 3)), pc(N, (1, 4))])
    return out


# =========================================================== F. S-D replay
def sd_replay():
    al = (1, 1, 2, 2, 3, 3, 3, 3, 3, 3)
    q = core_from(al, 1, 0)
    rep = {}
    rep["classify"] = q.classify()
    rep["tau_012"] = [q.tmin(0, 1, 2), q.tmax(0, 1, 2)]
    rep["tau_023"] = [q.tmin(0, 2, 3), q.tmax(0, 2, 3)]
    rep["tau_024"] = [q.tmin(0, 2, 4), q.tmax(0, 2, 4)]
    rep["T3_apex2"] = [str(Fr(q.tmin(0, 1, 2), 4 * q.a(0, 1))), str(Fr(q.tmin(0, 2, 3), 4 * q.a(0, 3))),
                       str(Fr(q.tmin(0, 2, 4), 4 * q.a(0, 4)))]
    rep["X_sizes_at_v2"] = {str(j): str(Fr(q.a(2, j), 4)) for j in (0, 1, 3, 4)}
    rep["s_max_at_v2"] = {str(j): 4 - q.a(2, j) for j in (0, 1, 3, 4)}
    # gcd(s0*r0, r_j) >= 2 possible?  r0: odd, 3|r0; r1: even, 3 does not divide; r3,r4 coprime to 6.
    # common prime must divide s0 (gcd(r0, rj) = 1) and s0 <= 3, so only p in {2,3} matter.
    div = {1: {2}, 3: set(), 4: set()}
    poss = {}
    for s0 in (1, 2, 3):
        for j in (1, 3, 4):
            ps = {p for p in (2, 3) if s0 % p == 0}
            poss[f"s0={s0},j={j}"] = bool(ps & div[j])
    rep["gcd_possible"] = poss
    rep["only_option"] = [k for k, v in poss.items() if v]
    rep["contradiction_for_only_option"] = "|D0| = 2|G|/4 > |Y1| = |G|/4"
    return rep


# =========================================================== main
def main():
    outdir, lane = sys.argv[1], sys.argv[2]
    os.makedirs(outdir, exist_ok=False)
    t0 = time.time()
    with open(os.path.abspath(__file__), "rb") as f:
        me = hashlib.sha256(f.read()).hexdigest()
    S = {"script_sha256": me, "python": sys.version, "started_epoch": t0}
    # ---- A
    na, npat = burnside()
    reps, pats = enumerate_universe()
    keys = [canon(*p) for p in pats]
    S["A_universe"] = {"burnside_alpha_classes": na, "burnside_patterns": npat,
                       "enumerated_alpha_orbits": len(reps), "enumerated_patterns": len(pats),
                       "enumerated_keys_distinct": len(set(keys))}
    cpath = os.path.join(lane, "evidence/engine-v1-run1/certificates.tsv.gz")
    with open(cpath, "rb") as f:
        gzb = f.read()
    raw = gzip.decompress(gzb)
    lines = raw.decode().rstrip("\n").split("\n")
    wkeys = {}
    for ln in lines:
        code, rule, wjs = ln.split("\t")
        wkeys[canon(*parse_code(code))] = (code, rule, wjs)
    S["A_universe"].update({
        "worker_certificates_gz_sha256": hashlib.sha256(gzb).hexdigest(),
        "worker_certificates_uncompressed_sha256": hashlib.sha256(raw).hexdigest(),
        "worker_lines": len(lines), "worker_distinct_orbits": len(wkeys),
        "worker_orbits_equal_parent_universe": set(wkeys) == set(keys)})
    # ---- B
    mycls = {}
    for p, kk in zip(pats, keys):
        mycls[kk] = core_from(*p).classify()
    S["B_parent_first_rule_counts"] = dict(Counter((c[0] if c else "SURVIVE") for c in mycls.values()))
    S["B_parent_survivors"] = [list(k) for k, c in mycls.items() if c is None]
    stats = Counter()
    fails, catmis, m1 = [], [], []
    fh2 = []
    for kk, (code, rule, wjs) in sorted(wkeys.items()):
        al, e2, e3 = parse_code(code)
        p = core_from(al, e2, e3)
        mc = mycls[kk][0] if mycls[kk] else "SURVIVE"
        if mc != rule:
            catmis.append([code, rule, mc])
        if rule == "SURVIVE":
            stats[("SURVIVE", True)] += 1
            continue
        w = json.loads(wjs)
        if rule == "T":
            tri, tm, tM = w
            ok = p.tmin(*tri) == tm and p.tmax(*tri) == tM and tm > tM
        elif rule == "K":
            v, Sx, sstr = w
            ok = p.K_kill(v, Sx) and Fr(sstr) == Fr(sum(p.a(i, v) for i in Sx), 4)
            for i, j in combinations(Sx, 2):
                if p.tmin(v, i, j) != p.tmax(v, i, j):
                    m1.append([code, v, i, j])
        elif rule == "Ppair":
            v, (j, k_), lo, hi = w
            ok = p.Ppair_kill(v, j, k_)
        elif rule == "PB":
            v, Sx, vstr = w
            ok = p.PB_kill(v, Sx) and p.PB_val(v, Sx) == Fr(vstr)
        elif rule == "N2":
            ok = p.N2() and w == []
        elif rule == "FH2":
            (x, y), V2, _, _ = w
            ok = p.a(x, y) == 1 and p.V2_of(x, y) == V2 and p.FH2_kill(x, y)
            fh2.append({"code": code, "xy": [x, y], "V2": V2,
                        "kill_without_s5_minimality": p.FH2_kill(x, y, use_s5=False),
                        "kill_hereditary_without_s5": p.FH2_kill(x, y, use_s5=False, hered=True),
                        "kill_hereditary_without_s5_at_e=f=1": p.FH2_kill(x, y, use_s5=False, hered=True,
                                                                         mode=("inst", 1, 1)),
                        "kill_at_e=f=1": p.FH2_kill(x, y, mode=("inst", 1, 1))})
        elif rule == "FH1":
            tri = w[0]
            ok = all(p.a(i, j) == 1 for i, j in combinations(tri, 2)) and p.FH1_kill(tri)
        else:
            ok = False
        stats[(rule, ok)] += 1
        if not ok:
            fails.append(code)
    S["B_witness_verification"] = {f"{r}:{'ok' if o else 'FAIL'}": c for (r, o), c in sorted(stats.items())}
    S["B_witness_failures"] = fails
    S["B_first_rule_category_mismatches"] = catmis
    S["B_M1_K_links_not_singleton_tau"] = m1
    S["B_FH2_sensitivity"] = {
        "n": len(fh2),
        "kill_without_s5_minimality": sum(d["kill_without_s5_minimality"] for d in fh2),
        "kill_hereditary_without_s5": sum(d["kill_hereditary_without_s5"] for d in fh2),
        "kill_hereditary_without_s5_at_e=f=1": sum(d["kill_hereditary_without_s5_at_e=f=1"] for d in fh2),
        "kill_at_e=f=1": sum(d["kill_at_e=f=1"] for d in fh2),
        "alpha_classes": sorted({d["code"].split("/")[0] for d in fh2}),
    }
    # ---- C (L8): rule-by-rule agreement of symbolic form with numeric general form at five instances
    mism = Counter()
    checked = 0
    fh_stage = []
    for p, kk in zip(pats, keys):
        al, e2, e3 = p
        q = core_from(al, e2, e3)
        hs = q.hits(fh=False)
        reach_fh = not any(hs.values())
        if reach_fh:
            hs.update({"FH1": any(q.FH1_kill(t) for t in q.H1_triangles()),
                       "FH2": any(q.FH2_kill(x, y) for x, y in combinations(range(5), 2))})
            fh_stage.append(p)
        for name, (base, f2, f3) in INSTANCES.items():
            r = inst_r(base, f2, f3, e2, e3)
            Gn = Gen([4 * x for x in r], {e: al[t] for t, e in enumerate(EDGES)})
            hn = Gn.hits(core=True, fh=reach_fh)
            for rule in hs:
                checked += 1
                if rule in ("FH1", "FH2") and name in ("I1_p5-17_x2_x3", "I5_all1_x2_x3"):
                    # small exponents: numeric gcds can only be smaller, so kills may only be added
                    if hs[rule] and not hn[rule]:
                        mism[(name, rule, "sym-kill-not-numeric")] += 1
                    elif hn[rule] and not hs[rule]:
                        mism[(name, rule, "numeric-extra-kill(allowed)")] += 1
                elif hs[rule] != hn[rule]:
                    mism[(name, rule)] += 1
    S["C_L8_instance_agreement"] = {"instances": {k: [list(v[0]), v[1], v[2]] for k, v in INSTANCES.items()},
                                    "rule_evaluations": checked,
                                    "mismatches": {"|".join(k): c for k, c in sorted(mism.items())},
                                    "fh_stage_patterns": len(fh_stage)}
    # ---- D
    S["D_C1_shapes"] = c1_shapes()
    # ---- E
    S["E_controls"] = controls()
    # ---- F
    S["F_SD_replay"] = sd_replay()
    S["seconds"] = round(time.time() - t0, 2)
    with open(os.path.join(outdir, "summary.json"), "x") as f:
        json.dump(S, f, indent=1, default=str)
    print(json.dumps({"A": S["A_universe"], "B_counts": S["B_parent_first_rule_counts"],
                      "B_witness": S["B_witness_verification"], "B_fail": len(fails), "B_catmis": len(catmis),
                      "B_m1": len(m1), "B_FH2": S["B_FH2_sensitivity"], "C": S["C_L8_instance_agreement"]["mismatches"],
                      "seconds": S["seconds"]}, default=str))


if __name__ == "__main__":
    main()
