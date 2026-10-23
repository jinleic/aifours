#!/usr/bin/env python3
"""core5_engine_v1 -- frozen rule engine for rules-v1.md (lane sun-coset5).

Standard library only, deterministic, single process.
Usage:  python3 core5_engine_v1.py OUTDIR
Writes (exclusive create) into OUTDIR:
  certificates.tsv.gz  one line per Core(5) pattern: code, rule, witness
  survivors.json       surviving patterns with full data
  controls.json        controls C1-C4
  run.json             versions, counts, timings, sha256 of this file
Rules (rules-v1.md): T (L1), K (L3 with K1 links), Ppair/PB (L4), N2 (L5),
FH1 (L6 with H1 = M-S Lemma 3.7), FH2 (L6 with H2).  Evaluation at tau_min and at
representative r values is justified in rules-v1.md L8 (M1, M2).
"""
import gzip
import hashlib
import itertools
import json
import os
import platform
import sys
import time
from fractions import Fraction as Fr
from math import gcd

PRIMES = (5, 7, 11, 13, 17)


def lcm(a, b):
    return a * b // gcd(a, b)


def floor_frac(x):
    return x.numerator // x.denominator


# ---------------------------------------------------------------- engine core
class Pattern:
    """Concrete data: indices n[i] and alpha[(i,j)] (i<j)."""

    def __init__(self, n, alpha, core=False):
        self.n = list(n)
        self.k = len(n)
        self.alpha = dict(alpha)
        self.core = core  # True only for Core(5) shape (n_i = 4 r_i, r pairwise coprime)
        self._tau = {}

    def a(self, i, j):
        return self.alpha[(i, j) if i < j else (j, i)]

    def g(self, i, j):
        return gcd(self.n[i], self.n[j])

    def I(self, i, j):  # [G : U_i cap U_j]
        return lcm(self.n[i], self.n[j]) * self.a(i, j)

    def P(self, i, j):  # |U_i U_j| / |G|
        return Fr(self.a(i, j), self.g(i, j))

    def L(self, tri):
        x, y, z = tri
        return lcm(lcm(self.n[x], self.n[y]), self.n[z])

    def tau_min(self, tri):
        key = tuple(sorted(tri))
        if key not in self._tau:
            L = self.L(key)
            t = 1
            for x, y in itertools.combinations(key, 2):
                Ixy = self.I(x, y)
                t = lcm(t, Ixy // gcd(Ixy, L))
            self._tau[key] = t
        return self._tau[key]

    def T3(self, y, x, z, tau):  # |U_y (U_x cap U_z)| / |G|
        return Fr(self.L((x, y, z)) * tau, self.n[y] * self.I(x, z))

    def tau_max(self, tri):
        best = None
        for y in tri:
            x, z = [w for w in tri if w != y]
            bound = min(self.P(y, x), self.P(y, z)) * self.n[y] * self.I(x, z) / self.L(tri)
            b = floor_frac(bound)
            best = b if best is None else min(best, b)
        return best

    def link(self, v, i, j):
        """K1: pair {i,j} satisfies the L3 condition at vertex v (evaluated at tau_min)."""
        tau = self.tau_min((i, v, j))
        return self.T3(i, v, j, tau) == self.P(i, v) or self.T3(j, v, i, tau) == self.P(j, v)

    def K2_ok(self, v, j, k):
        """Containment U_v U_j subset U_v U_k is allowed only if P(v,j)+P(k,j) < 1."""
        return self.P(v, j) + self.P(k, j) < 1


def rule_T(p):
    for tri in itertools.combinations(range(p.k), 3):
        tm, tM = p.tau_min(tri), p.tau_max(tri)
        if tm > tM:
            return ("T", list(tri), tm, tM)
    return None


def rule_K(p):
    for v in range(p.k):
        oth = [w for w in range(p.k) if w != v]
        for r in range(2, len(oth) + 1):
            for S in itertools.combinations(oth, r):
                if all(p.link(v, i, j) for i, j in itertools.combinations(S, 2)):
                    s = sum(p.P(i, v) for i in S)
                    if s >= 1:
                        return ("K", v, list(S), str(s))
    return None


def p_bounds(p, v, j, k):
    """Return (lo, hi, unit) for |X_j cap X_k|/|G| at vertex v (L4)."""
    Xj, Xk = p.P(v, j), p.P(v, k)
    u = Fr(1, gcd(p.n[v], p.I(j, k)))
    lo = max(p.T3(v, j, k, p.tau_min((v, j, k))), Xj + Xk - 1, Fr(0))
    lo = -((-lo) // u) * u  # round up to a multiple of u
    m = min(Xj, Xk)
    hi = (m // u) * u
    if hi == m:
        if Xj < Xk:
            allowed = p.K2_ok(v, j, k)
        elif Xk < Xj:
            allowed = p.K2_ok(v, k, j)
        else:
            allowed = p.K2_ok(v, j, k) and p.K2_ok(v, k, j)
        if not allowed:
            hi -= u
    return lo, hi, u


def rule_P(p):
    for v in range(p.k):
        oth = [w for w in range(p.k) if w != v]
        his = {}
        for j, k in itertools.combinations(oth, 2):
            lo, hi, u = p_bounds(p, v, j, k)
            if lo > hi:
                return ("Ppair", v, [j, k], str(lo), str(hi))
            his[(j, k)] = hi
        for r in range(2, len(oth) + 1):
            for S in itertools.combinations(oth, r):
                val = sum(1 - p.P(v, j) for j in S) - sum(
                    1 - p.P(v, j) - p.P(v, k) + his[(j, k)] for j, k in itertools.combinations(S, 2))
                if val >= 1:
                    return ("PB", v, list(S), str(val))
    return None


def rule_N2(p):
    if p.core and all(x == 2 for x in p.alpha.values()):
        return ("N2",)
    return None


def fibre_search(p, m, inside, fixed_t):
    """L6: return number of admissible assignments found (0 means refuted) and count examined.
    inside: vertices with U subset H (t=1); fixed_t: dict vertex -> forced t."""
    verts = list(range(p.k))
    opts = {}
    for l in verts:
        if l in inside:
            ts = [1]
        elif l in fixed_t:
            ts = [fixed_t[l]]
        else:
            ts = list(range(1, m + 1))
        lst = []
        for t in ts:
            if (p.n[l] * t) % m:
                continue  # lambda_l must be an integer (F1)
            for M in itertools.combinations(range(m), t):
                lst.append((t, M))
        opts[l] = lst
    # symmetry of coset labels: first inside vertex placed in coset 0
    first = inside[0]
    opts[first] = [(1, (0,))]
    examined = 0
    order = verts
    for combo in itertools.product(*[opts[l] for l in order]):
        examined += 1
        asg = dict(zip(order, combo))
        ones = [l for l in verts if asg[l][0] == 1]
        ok = True
        for i in ones:  # F3
            for l in verts:
                if l != i and p.P(i, l) > Fr(asg[l][0], m):
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            continue
        lam = {l: p.n[l] * asg[l][0] // m for l in verts}
        for c in range(m):
            S = [l for l in verts if c in asg[l][1]]
            s = len(S)
            if s >= 2 and not any(gcd(lam[x], lam[y]) >= s for x, y in itertools.combinations(S, 2)):
                ok = False
                break
        if ok:
            return 1, examined
    return 0, examined


def h1_triangles(p):
    out = []
    for tri in itertools.combinations(range(p.k), 3):
        if any(p.a(i, j) != 1 for i, j in itertools.combinations(tri, 2)):
            continue
        gs = {p.g(i, j) for i, j in itertools.combinations(tri, 2)}
        if len(gs) != 1:
            continue
        a = gs.pop()
        if any(p.n[x] % a for x in tri):
            continue
        q = [p.n[x] // a for x in tri]
        if all(gcd(q[i], q[j]) == 1 for i, j in itertools.combinations(range(3), 2)):
            out.append((list(tri), a))
    return out


def rule_FH1(p):
    for tri, a in h1_triangles(p):
        found, ex = fibre_search(p, a, tri, {})
        if not found:
            return ("FH1", tri, a, ex)
    return None


def rule_FH2(p):
    if not p.core:
        return None
    for x, y in itertools.combinations(range(p.k), 2):
        if p.a(x, y) != 1:
            continue
        V2 = [v for v in range(p.k) if v not in (x, y) and p.a(v, x) == 2 and p.a(v, y) == 2]
        if not V2:
            continue
        f4, e4 = fibre_search(p, 4, [x, y], {v: 2 for v in V2})
        f2, e2 = fibre_search(p, 2, [x, y] + V2, {})
        if not f4 and not f2:
            return ("FH2", [x, y], V2, e4, e2)
    return None


RULES_FULL = (("T", rule_T), ("K", rule_K), ("P", rule_P), ("N2", rule_N2), ("FH1", rule_FH1), ("FH2", rule_FH2))
RULES_TKP = (("T", rule_T), ("K", rule_K), ("P", rule_P))


def classify(p, rules=RULES_FULL):
    for _, f in rules:
        w = f(p)
        if w is not None:
            return w
    return None


# ------------------------------------------------------- pattern enumeration
def edges(k):
    return list(itertools.combinations(range(k), 2))


def rep_r(k, e2, e3, odd=()):
    r = []
    for i in range(k):
        x = PRIMES[i]
        if i == e2:
            x *= 16
        if i == e3:
            x *= 81
        r.append(x)
    return r


def enumerate_shape(d, alpha_max, allowed_e2, allowed_e3, sym_group):
    """Yield canonical (alpha_tuple, e2, e3) up to sym_group (list of perms of vertices)."""
    k = len(d)
    E = edges(k)
    eidx = {e: i for i, e in enumerate(E)}
    pm = []
    for perm in sym_group:
        m = [0] * len(E)
        for t, (i, j) in enumerate(E):
            pi, pj = perm[i], perm[j]
            m[t] = eidx[(pi, pj) if pi < pj else (pj, pi)]
        pm.append((perm, m))
    ranges = [range(1, alpha_max[e] + 1) for e in E]
    out = []
    NONE = k  # code for "no such vertex"
    for al in itertools.product(*ranges):
        canon = True
        stab = []
        for perm, m in pm:
            nal = [0] * len(E)
            for t in range(len(E)):
                nal[m[t]] = al[t]
            nal = tuple(nal)
            if nal < al:
                canon = False
                break
            if nal == al:
                stab.append(perm)
        if not canon:
            continue
        seen = set()
        for e2 in allowed_e2:
            for e3 in allowed_e3:
                best = min((NONE if e2 is None else perm[e2], NONE if e3 is None else perm[e3]) for perm in stab)
                if best not in seen:
                    seen.add(best)
                    out.append((tuple(al), best[0], best[1]))
    out.sort()
    return out


def make_pattern(d, key, core):
    al, e2c, e3c = key
    k = len(d)
    e2 = None if e2c == k else e2c
    e3 = None if e3c == k else e3c
    r = rep_r(k, e2, e3)
    n = [d[i] * r[i] for i in range(k)]
    alpha = {e: al[t] for t, e in enumerate(edges(k))}
    return Pattern(n, alpha, core=core), e2, e3


def code_of(key, k):
    al, e2c, e3c = key
    f = lambda c: "-" if c == k else str(c)
    return "".join(map(str, al)) + "/" + f(e2c) + f(e3c)


def shape_core5():
    d = (4, 4, 4, 4, 4)
    amax = {e: 3 for e in edges(5)}
    allowed = [None, 0, 1, 2, 3, 4]
    return d, enumerate_shape(d, amax, allowed, allowed, list(itertools.permutations(range(5))))


def shape_ctrl(name):
    if name == "P42":
        d = (2, 2, 2)
        allowed2 = allowed3 = [None, 0, 1, 2]
        sym = list(itertools.permutations(range(3)))
    elif name == "P43":
        d = (3, 3, 3, 3)
        allowed2 = allowed3 = [None, 0, 1, 2, 3]
        sym = list(itertools.permutations(range(4)))
    elif name == "P45":
        d = (2, 4, 4, 4)
        allowed2 = [None, 1, 2, 3]  # r_1 odd
        allowed3 = [None, 0, 1, 2, 3]
        sym = [(0,) + q for q in itertools.permutations((1, 2, 3))]
    k = len(d)
    amax = {(i, j): gcd(d[i], d[j]) - 1 for i, j in edges(k)}
    return d, enumerate_shape(d, amax, allowed2, allowed3, sym)


# ----------------------------------------------------------- permutation groups
def perm_from_cycles(N, cycles):
    p = list(range(N + 1))
    for c in cycles:
        for i in range(len(c)):
            p[c[i]] = c[(i + 1) % len(c)]
    return tuple(p)


def pmul(p, q):  # functional composition: (p*q)(x) = p(q(x))
    return tuple(p[q[x]] for x in range(len(p)))


def closure(gens, N):
    e = tuple(range(N + 1))
    S = {e}
    frontier = [e]
    while frontier:
        nf = []
        for x in frontier:
            for g in gens:
                y = pmul(x, g)
                if y not in S:
                    S.add(y)
                    nf.append(y)
        frontier = nf
    return frozenset(S)


def setprod(A, B):
    return frozenset(pmul(a, b) for a in A for b in B)


def realised_pattern(G, subs, reps):
    """Exact data of a realisable configuration; checks disjointness; returns (Pattern, facts)."""
    k = len(subs)
    order = len(G)
    cos = [frozenset(pmul(g, u) for u in U) for U, g in zip(subs, reps)]  # left cosets gU (GAP Coset(H,g))
    disjoint = all(not (cos[i] & cos[j]) for i, j in edges(k))
    n = [order // len(U) for U in subs]
    alpha = {}
    for i, j in edges(k):
        Iij = order // len(subs[i] & subs[j])
        alpha[(i, j)] = Iij // lcm(n[i], n[j])
        assert Iij % lcm(n[i], n[j]) == 0
    p = Pattern(n, alpha)
    facts = {"disjoint": disjoint, "n": n, "alpha": {f"{i}{j}": v for (i, j), v in alpha.items()}}
    # lemma validation on actual data
    viol = []
    prods = {(i, j): setprod(subs[i], subs[j]) for i in range(k) for j in range(k) if i != j}
    for i, j in edges(k):
        if Fr(len(prods[(i, j)]), order) != p.P(i, j):
            viol.append(("L0.3", i, j))
    for tri in itertools.combinations(range(k), 3):
        x, y, z = tri
        T = order // len(subs[x] & subs[y] & subs[z])
        L = p.L(tri)
        if T % L:
            viol.append(("T0", tri))
            continue
        tau = T // L
        if tau % p.tau_min(tri) or tau > p.tau_max(tri):
            viol.append(("T1T2", tri, tau, p.tau_min(tri), p.tau_max(tri)))
        for yy in tri:
            xx, zz = [w for w in tri if w != yy]
            act = Fr(len(setprod(subs[yy], subs[xx] & subs[zz])), order)
            if act != p.T3(yy, xx, zz, tau):
                viol.append(("T3", tri, yy))
    for v in range(k):
        oth = [w for w in range(k) if w != v]
        # L3 with actual containments
        def cond(i, j):
            return prods[(v, i)] <= prods[(j, i)] or prods[(v, j)] <= prods[(i, j)]
        for r in range(2, len(oth) + 1):
            for S in itertools.combinations(oth, r):
                if all(cond(i, j) for i, j in itertools.combinations(S, 2)) and sum(p.P(i, v) for i in S) >= 1:
                    viol.append(("L3", v, S))
        X = {j: prods[(v, j)] for j in oth}
        for j, kk in itertools.combinations(oth, 2):
            inter = Fr(len(X[j] & X[kk]), order)
            lo, hi, u = p_bounds(p, v, j, kk)
            if (inter / u).denominator != 1 or inter < lo:
                viol.append(("P2P3", v, j, kk, str(inter), str(lo), str(u)))
            if X[j] <= X[kk] and not p.K2_ok(v, j, kk):
                viol.append(("K2", v, j, kk))
        Gs = set(G)
        for r in range(2, len(oth) + 1):
            for S in itertools.combinations(oth, r):
                Y = [Gs - X[j] for j in S]
                if len(set().union(*Y)) >= order:
                    viol.append(("P5union", v, S))
    facts["lemma_violations_on_actual_data"] = viol
    return p, facts


def control_realisable():
    out = {}
    # Menon Thm 3.1: A5, (6,6,6,10,15)
    N = 5
    A5 = frozenset(q for q in itertools.permutations(range(1, 6))
                   if sum(1 for i in range(5) for j in range(i + 1, 5) if q[i] > q[j]) % 2 == 0)
    A5 = frozenset((0,) + q for q in A5)
    c = lambda *cy: perm_from_cycles(N, cy)
    D = closure([c((1, 2, 5, 3, 4)), c((1, 2), (4, 5))], N)
    T = closure([c((2, 3, 5)), c((1, 4), (2, 3))], N)
    V = closure([c((1, 2), (3, 4)), c((1, 3), (2, 4))], N)
    subs = [D, D, D, T, V]
    reps = [c((1, 5, 3)), c((1, 4, 2, 3, 5)), c((1, 5, 2, 3, 4)), c((1, 2, 4)), c((3, 4, 5))]
    out["A5_66661015"] = run_realised(A5, subs, reps)
    # Menon Sec 5: C2 x S4 in S6, (4,6,6,6,6)
    N = 6
    c = lambda *cy: perm_from_cycles(N, cy)
    G = closure([c((1, 2)), c((3, 4)), c((3, 4, 5, 6))], N)
    A = closure([c((3, 4, 5)), c((4, 5, 6))], N)
    P = closure([c((3, 6)), c((4, 5)), c((3, 4), (5, 6))], N)
    Q = closure([c((1, 2), (3, 4, 5, 6)), c((1, 2), (3, 5))], N)
    R = closure([c((1, 2)), c((3, 4), (5, 6)), c((3, 5), (4, 6))], N)
    subs = [A, P, P, Q, R]
    reps = [c((1, 2)), c(), c((4, 5, 6)), c((1, 2), (4, 5)), c((1, 2), (3, 5, 4, 6))]
    out["C2xS4_46666"] = run_realised(G, subs, reps)
    # k cosets of one subgroup: Z5 (index 5, k=5) and Z4 (index 4, k=4), as permutation groups
    for name, N, k in (("Z5_five_cosets", 5, 5), ("Z4_four_cosets", 4, 4)):
        gen = perm_from_cycles(N, [tuple(range(1, N + 1))])
        G = closure([gen], N)
        e = tuple(range(N + 1))
        U = frozenset([e])
        elems = sorted(G)
        out[name] = run_realised(G, [U] * k, elems[:k])
    return out


def run_realised(G, subs, reps):
    p, facts = realised_pattern(G, subs, reps)
    k = len(subs)
    res = {"order": len(G), "facts": facts, "engine_full": classify(p, RULES_FULL)}
    subres = {}
    if k == 5:
        for drop in range(5):
            keep = [i for i in range(5) if i != drop]
            p4, f4 = realised_pattern(G, [subs[i] for i in keep], [reps[i] for i in keep])
            subres[f"drop{drop}"] = {"n": f4["n"], "disjoint": f4["disjoint"],
                                    "violations": f4["lemma_violations_on_actual_data"],
                                    "engine_full": classify(p4, RULES_FULL)}
    res["four_subconfigurations"] = subres
    return res


def control_abelian():
    """C3: alpha in cyclic Z60 (subgroups of index 4,12,20) and abelian Z2^3 x Z15."""
    res = {}
    # cyclic Z_60: subgroup of index d is dZ_60
    order = 60
    def sub_cyc(d):
        return frozenset(range(0, order, d))
    idx = [4, 12, 20]
    al = {}
    for d1, d2 in itertools.combinations(idx, 2):
        A, B = sub_cyc(d1), sub_cyc(d2)
        Iab = order // len(A & B)
        al[f"{d1},{d2}"] = Iab // lcm(d1, d2)
    res["Z60"] = al
    # abelian Z2^3 x Z15, elements (a,b,c,x); subgroups <u> x (subgroup of Z15 of order 15/s)
    els = [(a, b, c, x) for a in (0, 1) for b in (0, 1) for c in (0, 1) for x in range(15)]
    us = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1) if (a, b, c) != (0, 0, 0)]
    def sub_ab(u, s):  # index 4*s: <u> x sZ15
        return frozenset(((t * u[0]) % 2, (t * u[1]) % 2, (t * u[2]) % 2, x) for t in (0, 1) for x in range(0, 15, s))
    subsl = [(u, s) for u in us for s in (1, 3, 5)]
    vals = set()
    for (u1, s1), (u2, s2) in itertools.combinations(subsl, 2):
        if gcd(s1, s2) != 1:
            continue
        A, B = sub_ab(u1, s1), sub_ab(u2, s2)
        Iab = len(els) // len(A & B)
        vals.add(Iab // lcm(4 * s1, 4 * s2))
    res["Z2^3xZ15_alpha_values"] = sorted(vals)
    return res


# ------------------------------------------------------------- mutation checks
def recheck(p, w):
    """Re-verify one witness on pattern p; returns True if it still fires."""
    kind = w[0]
    if kind == "T":
        tri = w[1]
        return p.tau_min(tri) > p.tau_max(tri)
    if kind == "K":
        v, S = w[1], w[2]
        return all(p.link(v, i, j) for i, j in itertools.combinations(S, 2)) and sum(p.P(i, v) for i in S) >= 1
    if kind == "Ppair":
        v, (j, k) = w[1], w[2]
        lo, hi, u = p_bounds(p, v, j, k)
        return lo > hi
    if kind == "PB":
        v, S = w[1], w[2]
        his = {}
        for j, k in itertools.combinations(S, 2):
            lo, hi, u = p_bounds(p, v, j, k)
            if lo > hi:
                return True
            his[(j, k)] = hi
        val = sum(1 - p.P(v, j) for j in S) - sum(1 - p.P(v, j) - p.P(v, k) + his[(j, k)] for j, k in itertools.combinations(S, 2))
        return val >= 1
    if kind == "N2":
        return rule_N2(p) is not None
    if kind == "FH1":
        tri, a = w[1], w[2]
        if (tri, a) not in [(t, aa) for t, aa in h1_triangles(p)]:
            return False
        return fibre_search(p, a, tri, {})[0] == 0
    if kind == "FH2":
        x, y = w[1]
        if p.a(x, y) != 1:
            return False
        V2 = [v for v in range(p.k) if v not in (x, y) and p.a(v, x) == 2 and p.a(v, y) == 2]
        if not V2:
            return False
        return fibre_search(p, 4, [x, y], {v: 2 for v in V2})[0] == 0 and fibre_search(p, 2, [x, y] + V2, {})[0] == 0
    raise ValueError(kind)


def mutants(d, key):
    al, e2c, e3c = key
    k = len(d)
    E = edges(k)
    for t, (i, j) in enumerate(E):
        gmax = gcd(d[i], d[j]) - 1
        for v in range(1, gmax + 1):
            if v != al[t]:
                nal = list(al)
                nal[t] = v
                yield ("alpha", t, v), (tuple(nal), e2c, e3c)
    for e2 in list(range(k)) + [k]:
        if e2 != e2c:
            yield ("E2", e2), (al, e2, e3c)
    for e3 in list(range(k)) + [k]:
        if e3 != e3c:
            yield ("E3", e3), (al, e2c, e3)


# ---------------------------------------------------------------------- main
def main():
    outdir = sys.argv[1]
    os.makedirs(outdir, exist_ok=False)
    t0 = time.time()
    me = os.path.abspath(__file__)
    with open(me, "rb") as f:
        src_sha = hashlib.sha256(f.read()).hexdigest()
    run = {"engine": "core5_engine_v1", "engine_sha256": src_sha, "python": sys.version,
           "platform": platform.platform(), "started_epoch": t0}
    # Core(5) enumeration
    d, keys = shape_core5()
    run["core5_alpha_classes"] = len({k_[0] for k_ in keys})
    run["core5_patterns"] = len(keys)
    lines = []
    counts = {}
    survivors = []
    flagged_new = {"N2": 0, "FH2": 0}
    for key in keys:
        p, e2, e3 = make_pattern(d, key, core=True)
        w = classify(p)
        code = code_of(key, 5)
        if w is None:
            survivors.append({"code": code, "alpha": {f"{i}{j}": p.a(i, j) for i, j in edges(5)},
                              "E2": e2, "E3": e3, "n_representative": p.n})
            counts["SURVIVE"] = counts.get("SURVIVE", 0) + 1
            lines.append(f"{code}\tSURVIVE\t-")
        else:
            counts[w[0]] = counts.get(w[0], 0) + 1
            if w[0] in flagged_new:
                flagged_new[w[0]] += 1
            lines.append(f"{code}\t{w[0]}\t{json.dumps(w[1:], separators=(',', ':'))}")
    run["core5_rule_counts"] = counts
    run["core5_flagged_new_unreviewed"] = flagged_new
    run["core5_survivors"] = len(survivors)
    blob = ("\n".join(lines) + "\n").encode()
    gz = gzip.compress(blob, mtime=0)
    with open(os.path.join(outdir, "certificates.tsv.gz"), "xb") as f:
        f.write(gz)
    run["certificates_tsv_sha256_uncompressed"] = hashlib.sha256(blob).hexdigest()
    with open(os.path.join(outdir, "survivors.json"), "x") as f:
        json.dump(survivors, f, indent=1)
    t1 = time.time()
    # Controls
    controls = {}
    c1 = {}
    for name in ("P42", "P43", "P45"):
        dd, kk = shape_ctrl(name)
        surv = []
        cnt = {}
        for key in kk:
            p, e2, e3 = make_pattern(dd, key, core=False)
            w = classify(p, RULES_TKP)
            if w is None:
                surv.append(code_of(key, len(dd)))
            else:
                cnt[w[0]] = cnt.get(w[0], 0) + 1
        c1[name] = {"patterns": len(kk), "rule_counts": cnt, "survivors_TKP": surv}
    controls["C1_reproduce_MS_props_with_TKP_only"] = c1
    controls["C2_realisable"] = control_realisable()
    controls["C3_cyclic_abelian"] = control_abelian()
    # C4 mutation: for every killed Core(5) pattern, re-verify its witness and test all single-label mutants
    c4 = {"rechecked": 0, "recheck_failures": 0, "mutants": 0, "mutants_where_certificate_breaks": 0,
          "by_rule": {}, "note": "mutants tested for every T/K/P/N2 certificate; for FH1/FH2 only the first 25 such patterns in sorted order (cost cap)"}
    fh_tested = {"FH1": 0, "FH2": 0}
    d5, keys5 = d, keys
    for key, line in zip(keys5, lines):
        code, rule, wjs = line.split("\t")
        if rule == "SURVIVE":
            continue
        w = [rule] + json.loads(wjs)
        p, _, _ = make_pattern(d5, key, core=True)
        c4["rechecked"] += 1
        if not recheck(p, w):
            c4["recheck_failures"] += 1
        br = c4["by_rule"].setdefault(rule, [0, 0])
        if rule in fh_tested:
            if fh_tested[rule] >= 25:
                continue
            fh_tested[rule] += 1
        for desc, mkey in mutants(d5, key):
            pm, _, _ = make_pattern(d5, mkey, core=True)
            c4["mutants"] += 1
            br[0] += 1
            if not recheck(pm, w):
                c4["mutants_where_certificate_breaks"] += 1
                br[1] += 1
    # targeted demonstrations (intended reasons)
    demos = []
    def demo(label, al, e2, e3, mut_e2=None, mut_e3=None, mut_alpha=None):
        k = 5
        key = (tuple(al), k if e2 is None else e2, k if e3 is None else e3)
        p, _, _ = make_pattern(d5, key, core=True)
        w = classify(p)
        al2 = list(al)
        if mut_alpha:
            al2[mut_alpha[0]] = mut_alpha[1]
        key2 = (tuple(al2), (k if mut_e2 is None else mut_e2) if mut_e2 != "keep" else key[1],
                (k if mut_e3 is None else mut_e3) if mut_e3 != "keep" else key[2])
        p2, _, _ = make_pattern(d5, key2, core=True)
        demos.append({"label": label, "pattern": code_of(key, 5), "certificate": w,
                      "mutant": code_of(key2, 5), "certificate_still_fires_on_mutant": recheck(p2, w) if w else None,
                      "mutant_classification": classify(p2)})
    E5 = edges(5)
    ei = {e: t for t, e in enumerate(E5)}
    # (a) triangle {0,1,2} with alpha01=alpha12=1, alpha02=2 forces r_1 even (T); mutate E2 onto vertex 1
    al = [3] * 10
    al[ei[(0, 1)]] = 1; al[ei[(1, 2)]] = 1; al[ei[(0, 2)]] = 2
    demo("T_(1,1,2)_needs_opposite_even", al, None, None, mut_e2=1, mut_e3="keep")
    # (b) star of four 1s at vertex 0 (M-S Cor 3.9) -> K; mutate alpha04 to 2
    al = [2] * 10
    for j in (1, 2, 3, 4):
        al[ei[(0, j)]] = 1
    demo("K_star_1111_CorMS3.9", al, None, None, mut_e2="keep", mut_e3="keep", mut_alpha=(ei[(0, 4)], 2))
    # (c) star of four 3s at a vertex with gcd(r,6)=1 (screen N1) -> P; mutate E3 onto that vertex
    al = [1] * 10
    for j in (1, 2, 3, 4):
        al[ei[(0, j)]] = 3
    demo("P_star_3333_N1", al, None, None, mut_e2="keep", mut_e3=0)
    controls["C4_mutation"] = {"summary": c4, "demos": demos}
    with open(os.path.join(outdir, "controls.json"), "x") as f:
        json.dump(controls, f, indent=1, default=str)
    run["seconds_core5"] = round(t1 - t0, 2)
    run["seconds_total"] = round(time.time() - t0, 2)
    with open(os.path.join(outdir, "run.json"), "x") as f:
        json.dump(run, f, indent=1)
    print(json.dumps({"core5_patterns": run["core5_patterns"], "survivors": run["core5_survivors"],
                      "counts": counts, "seconds": run["seconds_total"]}))


if __name__ == "__main__":
    main()
