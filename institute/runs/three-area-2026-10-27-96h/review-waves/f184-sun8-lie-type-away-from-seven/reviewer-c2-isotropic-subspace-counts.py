#!/usr/bin/env python3
"""Reviewer control C2 for wave f184-sun8-lie-type-away-from-seven.

Independently authored by the reviewer; no author code is opened or run.
Brute-force geometric route: count totally isotropic / totally singular
k-subspaces in small classical polar spaces by direct enumeration over finite
fields, and compare with (a) the candidate's displayed formulas
Pi_G(q)/Pi_L(q) (transcribed by the reviewer) and (b) the reviewer's q=3 table
values. This is an independent anchor for the twisted Levi p'-orders and for
the Theorem B q=3 table. Negative controls must fail for the intended reason.
"""
import json, sys, time, itertools
from fractions import Fraction

T0 = time.time()
OUT = {"control": "reviewer-c2-isotropic-subspace-counts", "checks": {}, "negative": {}}
FAIL = []
def check(name, ok, detail=None):
    OUT["checks"][name] = {"ok": bool(ok), "detail": detail}
    if not ok:
        FAIL.append(name)

# ---------------- finite fields GF(p^k) with tables ----------------
class GF:
    def __init__(self, p, k, mod):
        # mod: monic irreducible of degree k, little-endian coefficient list (length k+1)
        self.p, self.k, self.q = p, k, p ** k
        q = self.q
        def to_vec(a):
            return [(a // p ** i) % p for i in range(k)]
        def to_int(v):
            return sum(c * p ** i for i, c in enumerate(v))
        self.add = [[to_int([(x + y) % p for x, y in zip(to_vec(a), to_vec(b))]) for b in range(q)] for a in range(q)]
        def mulv(u, v):
            r = [0] * (2 * k - 1)
            for i, x in enumerate(u):
                for j, y in enumerate(v):
                    r[i + j] = (r[i + j] + x * y) % p
            for d in range(2 * k - 2, k - 1, -1):
                c = r[d]
                if c:
                    for i in range(k + 1):
                        r[d - k + i] = (r[d - k + i] - c * mod[i]) % p
            return r[:k]
        self.mul = [[to_int(mulv(to_vec(a), to_vec(b))) for b in range(q)] for a in range(q)]
        self.neg = [next(b for b in range(q) if self.add[a][b] == 0) for a in range(q)]
        self.inv = [None] + [next(b for b in range(1, q) if self.mul[a][b] == 1) for a in range(1, q)]
        # field sanity: every nonzero element invertible, distributive spot check
        assert all(self.inv[a] is not None for a in range(1, q))
    def pw(self, a, e):
        r = 1
        for _ in range(e):
            r = self.mul[r][a]
        return r

def normalize(F, v):
    for c in v:
        if c:
            ic = F.inv[c]
            return tuple(F.mul[ic][x] for x in v)
    return None

def all_points(F, n):
    pts = []
    for v in itertools.product(range(F.q), repeat=n):
        if any(v):
            nv = normalize(F, v)
            if nv == v:
                pts.append(v)
    return pts

def ordered_basis_count(Q, k):
    r = 1
    for i in range(k):
        r *= (Q ** k - Q ** i) // (Q - 1)
    return r

def count_flats(F, pts, orth, kmax):
    """pts: list of isotropic points; orth(u,v)->bool symmetric; returns {k: number of t.i. k-spaces}."""
    idx = {p: i for i, p in enumerate(pts)}
    n = len(pts)
    masks = [0] * n
    for i in range(n):
        m = 0
        for j in range(n):
            if orth(pts[i], pts[j]):
                m |= 1 << j
        masks[i] = m
    res = {1: n}
    Q = F.q
    if kmax >= 2:
        c2 = sum(bin(masks[i] & ~(1 << i)).count("1") for i in range(n))
        res[2] = c2 // ordered_basis_count(Q, 2)
        assert c2 % ordered_basis_count(Q, 2) == 0
    if kmax >= 3:
        c3 = 0
        for i in range(n):
            mi = masks[i] & ~(1 << i)
            j = mi
            while j:
                low = j & -j
                jj = low.bit_length() - 1
                j ^= low
                # line through pts[i], pts[jj]
                line = 0
                P, R = pts[i], pts[jj]
                for a in range(F.q):
                    v = tuple(F.add[F.mul[a][x]][y] for x, y in zip(P, R))
                    line |= 1 << idx[normalize(F, v)]
                line |= 1 << i
                c3 += bin(masks[i] & masks[jj] & ~line).count("1")
        assert c3 % ordered_basis_count(Q, 3) == 0
        res[3] = c3 // ordered_basis_count(Q, 3)
    return res

# ---------------- integer polynomial helpers (values only) ----------------
def PSU_formula(m, q):
    PiG = 1
    for c in range(2, m + 1):
        PiG *= q ** c - (-1) ** c
    out = {}
    for k in range(1, m // 2 + 1):
        if 2 * k < m:
            PiL = 1
            for c in range(1, k + 1): PiL *= q ** (2 * c) - 1
            for c in range(2, m - 2 * k + 1): PiL *= q ** c - (-1) ** c
        else:
            PiL = q - 1
            for c in range(2, k + 1): PiL *= q ** (2 * c) - 1
        assert PiG % PiL == 0
        out[k] = PiG // PiL
    return out

def Ominus_formula(n, q):
    PiG = q ** n + 1
    for c in range(1, n): PiG *= q ** (2 * c) - 1
    out = {}
    for k in range(1, n):
        if k <= n - 2:
            PiL = (q - 1) * (q ** (n - k) + 1)
            for c in range(2, k + 1): PiL *= q ** c - 1
            for c in range(1, n - k): PiL *= q ** (2 * c) - 1
        else:
            PiL = q * q - 1
            for c in range(2, n): PiL *= q ** c - 1
        assert PiG % PiL == 0
        out[k] = PiG // PiL
    return out

# ---------------- unitary spaces ----------------
GF4 = GF(2, 2, [1, 1, 1])          # x^2+x+1
GF9 = GF(3, 2, [1, 0, 1])          # x^2+1
GF2 = GF(2, 1, [0, 1])
GF3 = GF(3, 1, [0, 1])

def unitary_case(F, q, m, kmax):
    conj = [F.pw(a, q) for a in range(F.q)]
    def h(u, v):
        s = 0
        for i in range(m):
            s = F.add[s][F.mul[u[i]][conj[v[m - 1 - i]]]]
        return s
    pts = [p for p in all_points(F, m) if h(p, p) == 0]
    counts = count_flats(F, pts, lambda u, v: h(u, v) == 0, kmax)
    return counts

uni = {}
for (q, m, kmax, F) in [(2, 3, 1, GF4), (2, 4, 2, GF4), (2, 5, 2, GF4), (2, 6, 3, GF4), (3, 3, 1, GF9), (3, 4, 2, GF9)]:
    counts = unitary_case(F, q, m, kmax)
    form = PSU_formula(m, q)
    ok = set(counts) == set(form) and all(counts[k] == form[k] for k in counts)
    uni[f"U{m}({q})"] = {"brute_force": counts, "candidate_formula": {k: form[k] for k in form}, "match": ok}
    check(f"unitary U{m}({q})", ok, uni[f"U{m}({q})"])
OUT["unitary"] = uni

# ---------------- orthogonal / symplectic spaces ----------------
def quad_case(F, dim, Qform, kmax):
    def B(u, v):
        s = [F.add[a][b] for a, b in zip(u, v)]
        return F.add[F.add[Qform(s)][F.neg[Qform(u)]]][F.neg[Qform(v)]]
    pts = [p for p in all_points(F, dim) if Qform(p) == 0]
    return count_flats(F, pts, lambda u, v: B(u, v) == 0, kmax)


def make_Q(F, n, kind):
    """Quadratic form on F^(2n) (kind 'minus' or 'plus') or F^(2n+1) (kind 'odd')."""
    M, A = F.mul, F.add
    def hyper(x, pairs):
        s = 0
        for i, j in pairs:
            s = A[s][M[x[i]][x[j]]]
        return s
    if kind == 'plus':
        pairs = [(i, 2 * n - 1 - i) for i in range(n)]
        return lambda x: hyper(x, pairs)
    if kind == 'minus':
        pairs = [(i, 2 * n - 1 - i) for i in range(n - 1)]
        a, b = n - 1, n
        if F.p == 2:
            return lambda x: A[hyper(x, pairs)][A[A[M[x[a]][x[a]]][M[x[a]][x[b]]]][M[x[b]][x[b]]]]
        else:  # q=3: x^2+y^2 anisotropic
            return lambda x: A[hyper(x, pairs)][A[M[x[a]][x[a]]][M[x[b]][x[b]]]]
    if kind == 'odd':
        pairs = [(i, 2 * n - i) for i in range(n)]
        return lambda x: A[hyper(x, pairs)][M[x[n]][x[n]]]
    raise ValueError

orth = {}
for (q, n, kmax, F) in [(2, 4, 3, GF2), (2, 5, 2, GF2), (3, 4, 3, GF3)]:
    counts = quad_case(F, 2 * n, make_Q(F, n, 'minus'), kmax)
    form = Ominus_formula(n, q)
    ok = all(counts[k] == form[k] for k in counts)
    orth[f"O-{2*n}({q})"] = {"brute_force": counts, "candidate_formula": form, "k_covered": sorted(counts), "match": ok}
    check(f"orthogonal minus O-{2*n}({q})", ok, orth[f"O-{2*n}({q})"])
OUT["orthogonal"] = orth

# q=3 table anchors (Theorem B): O7(3) [B3], Sp6(3) [C3], O8+(3) [D4: points, lines], U3(3), U4(3)
b3 = quad_case(GF3, 7, make_Q(GF3, 3, 'odd'), 3)
check("q=3 table: Omega7(3) singular points/lines/planes = 364,3640,1120", b3 == {1: 364, 2: 3640, 3: 1120}, b3)
def symp(u, v):
    F = GF3
    s = 0
    for i in range(3):
        s = F.add[s][F.mul[u[i]][v[5 - i]]]
        s = F.add[s][F.neg[F.mul[u[5 - i]][v[i]]]]
    return s == 0
pts6 = all_points(GF3, 6)
c3 = count_flats(GF3, pts6, symp, 3)
check("q=3 table: PSp6(3) t.i. points/lines/planes = 364,3640,1120", c3 == {1: 364, 2: 3640, 3: 1120}, c3)
d4 = quad_case(GF3, 8, make_Q(GF3, 4, 'plus'), 2)
check("q=3 table: POmega8+(3) singular points/lines = 1120,36400", d4 == {1: 1120, 2: 36400}, d4)
check("q=3 table: PSU3(3) isotropic points = 28", uni["U3(3)"]["brute_force"] == {1: 28})
check("q=3 table: PSU4(3) t.i. points/lines = 280,112", uni["U4(3)"]["brute_force"] == {1: 280, 2: 112})
OUT["q3_anchor"] = {"O7(3)": b3, "Sp6(3)": c3, "O8+(3)": d4}

# ---------------- negative controls ----------------
# NEG-A: hyperbolic (plus-type) 8-space over F2 must NOT match the candidate's minus-type formula
plus8 = quad_case(GF2, 8, make_Q(GF2, 4, 'plus'), 2)
negA = plus8[1] != Ominus_formula(4, 2)[1]
OUT["negative"]["NEG-A plus-type vs minus formula"] = {"plus_counts": plus8, "minus_formula": Ominus_formula(4, 2), "mismatch": negA}
check("NEG-A plus-type mismatch (expected)", negA)
# NEG-B: sign-mutated PSU Levi (x^c-1 in place of x^c-(-1)^c in the SU_{m-2k} factor, 2k<m branch only;
# the 2k=m branch kept correct). The twisted sign matters only when m-2k>=3, so U5(2) and U6(2) must mismatch.
def PSU_mut(m, q):
    PiG = 1
    for c in range(2, m + 1): PiG *= q ** c - (-1) ** c
    out = {}
    for k in range(1, m // 2 + 1):
        if 2 * k < m:
            PiL = 1
            for c in range(1, k + 1): PiL *= q ** (2 * c) - 1
            for c in range(2, m - 2 * k + 1): PiL *= q ** c - 1
        else:
            PiL = q - 1
            for c in range(2, k + 1): PiL *= q ** (2 * c) - 1
        out[k] = Fraction(PiG, PiL)
    return out
negB = {}
for key, (m, q) in {"U5(2)": (5, 2), "U6(2)": (6, 2)}.items():
    mut = PSU_mut(m, q)
    bf = uni[key]["brute_force"]
    negB[key] = {"mutated": mut, "brute_force": bf, "mismatch": any(mut[k] != bf[k] for k in bf if k in mut)}
OUT["negative"]["NEG-B sign-mutated PSU Levi"] = negB
check("NEG-B sign-mutated PSU Levi rejected (expected)", all(v["mismatch"] for v in negB.values()))

OUT["fail"] = FAIL
OUT["all_ok"] = not FAIL
OUT["elapsed_s"] = round(time.time() - T0, 3)
json.dump(OUT, sys.stdout, indent=1, sort_keys=True, default=str)
sys.stdout.write("\n")
sys.exit(0 if not FAIL else 1)
