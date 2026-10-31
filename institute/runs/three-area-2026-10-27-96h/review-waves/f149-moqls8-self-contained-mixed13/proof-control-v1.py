#!/usr/bin/env python3
# proof-control-v1.py -- f149 reviewer-authored bounded exact controls for the U13
# self-contained packet (frontier-20261028-four-family-mixed13-self-contained-v1.md).
#
# Python stdlib only; exact integer / Fraction / Gaussian-rational arithmetic.
# No author or sibling code is imported or executed.  Every control is an
# independently designed finite check of ONE combinatorial or algebraic step that the
# written proofs rely on; each positive control is paired with a targeted negative
# control (a deliberate mutation of the hypothesis or of the expectation) that must be
# detected.  These are supporting diagnostics, NOT a universal proof of U13.

import itertools, os, subprocess, hashlib, sys, platform, time
from fractions import Fraction as Fr
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = ("/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/"
       "parallel-18/moqls8/frontier-20261028-four-family-mixed13-self-contained-v1.md")
RECEIPT = os.path.join(HERE, "proof-control-receipt-v1.txt")

LINES = []
FAILS = 0


def log(s=""):
    print(s, flush=True)
    LINES.append(s)


def native_date():
    return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z %Z"],
                          capture_output=True, text=True).stdout.strip()


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def check(name, ok, detail=""):
    global FAILS
    if not ok:
        FAILS += 1
    log(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))
    return ok


def P(*xs):
    return tuple(sorted(xs, reverse=True))


# =============================================================================
# C1  Incidence enumeration (min line degree 2) for m = 4..12, r <= c <= 6.
#     Independent check of every (r,c)/degree-profile case list in the packet.
# =============================================================================
def enum_incidence(r, c, m, min_deg):
    """Counter keyed (row profile desc, col profile desc) -> number of labelled r x c
    0/1 boards with exactly m ones, every column degree >= min_deg, every row degree
    >= min_deg (so all r rows and c columns are incident)."""
    subs = {s: [tuple(x) for x in itertools.combinations(range(r), s)]
            for s in range(min_deg, r + 1)}
    sizes = sorted(subs)
    counts = Counter()
    rowdeg = [0] * r
    coldegs = []

    def rec(j, remaining):
        if j == c:
            if remaining == 0 and min(rowdeg) >= min_deg:
                counts[(tuple(sorted(rowdeg, reverse=True)),
                        tuple(sorted(coldegs, reverse=True)))] += 1
            return
        left = c - j - 1
        for s in sizes:
            rem = remaining - s
            if rem < left * min_deg or rem > left * r:
                continue
            coldegs.append(s)
            for sub in subs[s]:
                for i in sub:
                    rowdeg[i] += 1
                rec(j + 1, rem)
                for i in sub:
                    rowdeg[i] -= 1
            coldegs.pop()

    rec(0, m)
    return counts


A4, B4, C4 = P(4, 4, 2, 2), P(4, 3, 3, 2), P(3, 3, 3, 3)
two = lambda n: P(*([2] * n))

# Expected realized incidence-profile sets, transcribed from the packet's case
# statements (r <= c; transposes implied).  Profiles that the packet eliminates by a
# SUPPORT fact (e.g. odd degrees on all-support-2 lines) are still incidence-realizable
# and are therefore listed here.  Equality is tested, so both omissions and phantom
# cases would be flagged.
EXPECTED = {
    4: {(2, 2): {(P(2, 2), P(2, 2))}},
    5: {},
    6: {(2, 3): {(P(3, 3), two(3))}, (3, 3): {(two(3), two(3))}},
    7: {(3, 3): {(P(3, 2, 2), P(3, 2, 2))}},
    8: {(2, 4): {(P(4, 4), two(4))}, (3, 3): {(P(3, 3, 2), P(3, 3, 2))},
        (3, 4): {(P(4, 2, 2), two(4)), (P(3, 3, 2), two(4))}, (4, 4): {(two(4), two(4))}},
    9: {(3, 3): {(P(3, 3, 3), P(3, 3, 3))},
        (3, 4): {(P(3, 3, 3), P(3, 2, 2, 2)), (P(4, 3, 2), P(3, 2, 2, 2))},
        (4, 4): {(P(3, 2, 2, 2), P(3, 2, 2, 2))}},
    10: {(2, 5): {(P(5, 5), two(5))},
         (3, 4): {(P(4, 4, 2), P(3, 3, 2, 2)), (P(4, 3, 3), P(3, 3, 2, 2))},
         (3, 5): {(x, two(5)) for x in [P(5, 3, 2), P(4, 4, 2), P(4, 3, 3)]},
         (4, 4): {(a, b) for a in [P(4, 2, 2, 2), P(3, 3, 2, 2)]
                  for b in [P(4, 2, 2, 2), P(3, 3, 2, 2)]},
         (4, 5): {(x, two(5)) for x in [P(4, 2, 2, 2), P(3, 3, 2, 2)]},
         (5, 5): {(two(5), two(5))}},
    11: {(3, 4): {(P(4, 4, 3), P(3, 3, 3, 2))},
         (3, 5): {(x, P(3, 2, 2, 2, 2)) for x in [P(5, 4, 2), P(5, 3, 3), P(4, 4, 3)]},
         (4, 4): {(a, b) for a in [P(4, 3, 2, 2), P(3, 3, 3, 2)]
                  for b in [P(4, 3, 2, 2), P(3, 3, 3, 2)]},
         (4, 5): {(x, P(3, 2, 2, 2, 2)) for x in [P(5, 2, 2, 2), P(4, 3, 2, 2), P(3, 3, 3, 2)]},
         (5, 5): {(P(3, 2, 2, 2, 2), P(3, 2, 2, 2, 2))}},
    12: {(2, 6): {(P(6, 6), two(6))},
         (3, 4): {(P(4, 4, 4), P(3, 3, 3, 3))},
         (3, 5): {(x, P(3, 3, 2, 2, 2)) for x in [P(5, 5, 2), P(5, 4, 3), P(4, 4, 4)]},
         (3, 6): {(x, two(6)) for x in [P(6, 4, 2), P(6, 3, 3), P(5, 5, 2), P(5, 4, 3), P(4, 4, 4)]},
         (4, 4): {(a, b) for a in [A4, B4, C4] for b in [A4, B4, C4]},
         (4, 5): {(x, y) for x in [P(5, 3, 2, 2), A4, B4, C4]
                  for y in [P(4, 2, 2, 2, 2), P(3, 3, 2, 2, 2)]},
         (4, 6): {(x, two(6)) for x in [P(6, 2, 2, 2), P(5, 3, 2, 2), A4, B4, C4]},
         (5, 5): {(a, b) for a in [P(4, 2, 2, 2, 2), P(3, 3, 2, 2, 2)]
                  for b in [P(4, 2, 2, 2, 2), P(3, 3, 2, 2, 2)]},
         (5, 6): {(x, two(6)) for x in [P(4, 2, 2, 2, 2), P(3, 3, 2, 2, 2)]},
         (6, 6): {(two(6), two(6))}},
}


def realized_table(min_deg, ms, maxdim):
    table = {}
    for m in ms:
        table[m] = {}
        for r in range(2, maxdim + 1):
            for c in range(r, maxdim + 1):
                if r * c < m or (min_deg >= 2 and 2 * max(r, c) > m):
                    continue
                cnt = enum_incidence(r, c, m, min_deg)
                if cnt:
                    table[m][(r, c)] = cnt
    return table


def compare(table, expected, ms):
    ok = True
    for m in ms:
        got = {rc: set(cnt.keys()) for rc, cnt in table[m].items()}
        exp = expected.get(m, {})
        if got != exp:
            ok = False
            log(f"   m={m}: MISMATCH")
            for rc in sorted(set(got) | set(exp)):
                g_, e_ = got.get(rc, set()), exp.get(rc, set())
                if g_ != e_:
                    log(f"      (r,c)={rc}: realized-only={sorted(g_ - e_)} expected-only={sorted(e_ - g_)}")
    return ok


def control_C1():
    log("== C1  incidence enumeration, min line degree 2, r<=c<=6, m=4..12 ==")
    ms = list(range(4, 13))
    t = time.time()
    table = realized_table(2, ms, 6)
    log(f"   enumeration wall time {time.time() - t:.1f}s")
    for m in ms:
        for rc in sorted(table[m]):
            tot = sum(table[m][rc].values())
            prof = sorted(table[m][rc].keys())
            log(f"   m={m} (r,c)={rc} labelled boards={tot} profiles={prof}")
    check("C1.a realized (r,c)/profile sets equal the packet's case lists for every m=4..12",
          compare(table, EXPECTED, ms))
    want = {(2, 5): 1, (3, 4): 54, (3, 5): 210, (4, 4): 2040, (4, 5): 2580, (5, 5): 2040}
    got = {rc: sum(cnt.values()) for rc, cnt in table[10].items()}
    check("C1.b m=10 labelled board counts equal P05's auxiliary 1/54/210/2040/2580/2040",
          got == want, f"got={got}")
    even = set()
    for rc, cnt in table[12].items():
        if rc[1] == 6:
            for (rp, cp) in cnt:
                if all(d % 2 == 0 for d in rp):
                    even.add(rp)
    p09 = {P(6, 6), P(6, 4, 2), P(4, 4, 4), P(6, 2, 2, 2), P(4, 4, 2, 2), P(4, 2, 2, 2, 2), two(6)}
    check("C1.c m=12, six incident columns: all-even row profiles == P09 list", even == p09, f"{sorted(even)}")
    p11 = {rp for (rp, cp) in table[11][(4, 4)]} | {cp for (rp, cp) in table[11][(4, 4)]}
    p12 = {rp for (rp, cp) in table[12][(4, 4)]} | {cp for (rp, cp) in table[12][(4, 4)]}
    check("C1.d m=11 4x4 side profiles == {(4,3,2,2),(3,3,3,2)}", p11 == {P(4, 3, 2, 2), P(3, 3, 3, 2)})
    check("C1.e m=12 4x4 side profiles == {A,B,C}", p12 == {A4, B4, C4})
    s35 = {rp for (rp, cp) in table[10][(3, 5)] if all(d % 2 == 0 for d in rp)}
    s45 = {rp for (rp, cp) in table[10][(4, 5)] if all(d % 2 == 0 for d in rp)}
    check("C1.f m=10 all-even survivors: (3,5)->{(4,4,2)}, (4,5)->{(4,2,2,2)}",
          s35 == {P(4, 4, 2)} and s45 == {P(4, 2, 2, 2)})
    no3 = {rp for (rp, cp) in table[12][(4, 5)] if cp == P(4, 2, 2, 2, 2) and 3 not in rp}
    check("C1.g m=12 4x5, cols (4,2,2,2,2): degree-3-free row profiles == {(4,4,2,2)}", no3 == {A4})
    mut = {m: dict(v) for m, v in EXPECTED.items()}
    mut[7] = {}
    log("   N1: comparing against an expectation with the m=7 (3,3) case deleted ...")
    check("C1.N1 negative control: deleted m=7 case is detected as a mismatch", not compare(table, mut, ms))
    t1 = realized_table(1, [4, 5], 3)
    check("C1.N2 negative control: with min degree 1, m=5 is realizable and m=4 has non-2x2 shapes",
          bool(t1[5]) and set(t1[4]) != {(2, 2)}, f"m=4 shapes={sorted(t1[4])}, m=5 shapes={sorted(t1[5])}")


# =============================================================================
# C2  P10 section 1: projector multiplicity identity on a 3x4 board.
# =============================================================================
def control_C2():
    log("== C2  P10 projector-multiplicity identity (3 row 4-sets, 4 column 3-sets) ==")
    axes = range(8)
    K1 = frozenset({0, 1, 2, 3})
    four = [frozenset(s) for s in itertools.combinations(axes, 4)]
    three = [frozenset(s) for s in itertools.combinations(axes, 3)]
    sols = []
    for K2 in four:
        for K3 in four:
            Ks = [K1, K2, K3]
            mult = Counter(x for K in Ks for x in K)
            cands = [T for T in three if sum(1 for K in Ks if T <= K) >= 2]
            for Ts in itertools.combinations_with_replacement(cands, 4):
                if Counter(x for T in Ts for x in T) == mult:
                    sols.append((Ks, Ts))
    allK = all(K[0] == K[1] == K[2] for K, _ in sols)
    omit = all(len({tuple(K[0] - T) for T in Ts}) == 4 and all(len(K[0] - T) == 1 for T in Ts)
               for K, Ts in sols)
    check("C2.a every solution has K1=K2=K3", bool(sols) and allK, f"{len(sols)} solutions (K1 fixed by symmetry)")
    check("C2.b every solution has T_j = K minus a_j with four distinct a_j", bool(sols) and omit)
    K2, K3 = frozenset({0, 1, 2, 4}), frozenset({0, 1, 2, 5})
    mult = Counter(x for K in [K1, K2, K3] for x in K)
    bad = [Ts for Ts in itertools.combinations_with_replacement(three, 4)
           if Counter(x for T in Ts for x in T) == mult]
    check("C2.N negative control: without the containment hypothesis a distinct-K solution exists",
          len(bad) > 0, f"example T-multiset={[sorted(T) for T in bad[0]] if bad else None}")


# =============================================================================
# C3  P17 and P22 projector balances.
# =============================================================================
def control_C3():
    log("== C3  P17 / P22 coordinate projector balances ==")
    K = frozenset({0, 1, 2, 3})
    pairs = [frozenset(s) for s in itertools.combinations(K, 2)]
    triples = [frozenset(s) for s in itertools.combinations(K, 3)]

    def mult(*sets):
        return Counter(x for S in sets for x in S)

    sols, viol = 0, 0
    for V1 in pairs:
        V2 = K - V1
        for T1 in triples:
            for T2 in triples:
                for U in pairs:
                    if mult(K, K, V1, V2) == mult(K, T1, T2, U):
                        sols += 1
                        a1, a2 = next(iter(K - T1)), next(iter(K - T2))
                        if not (a1 != a2 and U == frozenset({a1, a2}) and len(U & T1) == 1 and len(U & T2) == 1):
                            viol += 1
    check("C3.a P17: every balance solution has U={a1,a2}, a1!=a2, |U∩T_j|=1", sols > 0 and viol == 0,
          f"solutions={sols} violations={viol}")
    viol2 = 0
    for V1 in pairs:
        for V2 in pairs:
            if V1 | V2 == K:
                continue
            for T1 in triples:
                for T2 in triples:
                    for U in pairs:
                        if mult(K, K, V1, V2) == mult(K, T1, T2, U):
                            a1, a2 = next(iter(K - T1)), next(iter(K - T2))
                            if not (a1 != a2 and U == frozenset({a1, a2})):
                                viol2 += 1
    check("C3.N1 negative control: without V1⊔V2=K the conclusion U={a1,a2} fails somewhere", viol2 > 0,
          f"violating solutions={viol2}")
    U = frozenset({0, 1})
    TA, TB = U | {2}, U | {3}
    all3 = [frozenset(s) for s in itertools.combinations(range(8), 3)]
    found = {frozenset([C1, C2]) for C1 in all3 for C2 in all3 if mult(C1, C2) == mult(K, U)}
    check("C3.b P22: P_C1+P_C2=P_K+P_U forces {C1,C2}={T_A,T_B}", found == {frozenset([TA, TB])},
          f"{[sorted(map(sorted, f)) for f in found]}")
    found2 = {frozenset([C1, C2]) for C1 in all3 for C2 in all3 if mult(C1, C2) == mult(K, frozenset({2, 3}))}
    check("C3.N2 negative control: a mutated right-hand side P_K+P_{c,d} gives a different pair",
          found2 != {frozenset([TA, TB])}, f"{[sorted(map(sorted, f)) for f in found2]}")


# =============================================================================
# Exact Gaussian-rational linear algebra helpers (for C4, C5)
# =============================================================================
class GQ:
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re, self.im = Fr(re), Fr(im)

    def __add__(s, o): return GQ(s.re + o.re, s.im + o.im)
    def __sub__(s, o): return GQ(s.re - o.re, s.im - o.im)
    def __neg__(s): return GQ(-s.re, -s.im)
    def __mul__(s, o): return GQ(s.re * o.re - s.im * o.im, s.re * o.im + s.im * o.re)
    def conj(s): return GQ(s.re, -s.im)
    def iszero(s): return s.re == 0 and s.im == 0
    def abs2(s): return s.re * s.re + s.im * s.im
    def __eq__(s, o): return s.re == o.re and s.im == o.im
    def __repr__(s): return f"({s.re}{'+' if s.im >= 0 else '-'}{abs(s.im)}i)"


def g(re, im=0): return GQ(re, im)
I = GQ(0, 1)
ZERO, ONE = GQ(0), GQ(1)


def inner(a, b):
    s = GQ(0)
    for x, y in zip(a, b):
        s = s + x.conj() * y
    return s


def vadd(a, b): return tuple(x + y for x, y in zip(a, b))
def vscale(c, a): return tuple(c * x for x in a)
def iszerovec(a): return all(x.iszero() for x in a)


def complement3(a, b):
    """w in C^3 with <a,w> = <b,w> = 0: componentwise conj(a) x conj(b)."""
    a, b = [x.conj() for x in a], [x.conj() for x in b]
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def collinear(a, b):
    """rank([a b]) <= 1 via all 2x2 minors."""
    n = len(a)
    for i in range(n):
        for j in range(i + 1, n):
            if not (a[i] * b[j] - a[j] * b[i]).iszero():
                return False
    return True


def support(a): return frozenset(i for i, x in enumerate(a) if not x.iszero())


# =============================================================================
# C4  P19/P20 cross-Gram step: planes sharing e_c give operator norm exactly 1;
#     zero-diagonal 2x2 of norm 1 has a unit off-diagonal; forced collinearity with e_c.
# =============================================================================
def control_C4():
    log("== C4  cross-Gram operator-norm step for two 2-planes (exact Gaussian rationals) ==")
    pyth = [(Fr(3, 5), Fr(4, 5)), (Fr(4, 5), Fr(3, 5)), (Fr(5, 13), Fr(12, 13)), (Fr(12, 13), Fr(5, 13)),
            (Fr(8, 17), Fr(15, 17)), (Fr(15, 17), Fr(8, 17)), (Fr(1), Fr(0)), (Fr(0), Fr(1))]
    e = [tuple(ONE if i == k else ZERO for i in range(4)) for k in range(4)]

    def unit2(a, b):
        return (g(a), g(b), ZERO, ZERO)

    def onb_of_plane(w, f, a, b, phase=ONE):
        # w ⊥ f unit; x1 = a w + phase*b f ; x2 = -conj(phase*b) w + a f  (a,b real, a^2+b^2=1)
        x1 = vadd(vscale(g(a), w), vscale(phase * g(b), f))
        x2 = vadd(vscale(-(phase * g(b)).conj(), w), vscale(g(a), f))
        return x1, x2

    def gram(X, Y):
        return [[inner(X[i], Y[j]) for j in range(2)] for i in range(2)]

    def det_I_minus_GstarG(G):
        H = [[sum((G[k][i].conj() * G[k][j] for k in range(2)), GQ(0)) for j in range(2)] for i in range(2)]
        M = [[(ONE if i == j else ZERO) - H[i][j] for j in range(2)] for i in range(2)]
        d = M[0][0] * M[1][1] - M[0][1] * M[1][0]
        assert d.im == 0
        return d.re

    phases = [ONE, I, g(Fr(3, 5), Fr(4, 5)), g(Fr(-5, 13), Fr(12, 13))]
    pos_ok, pos_n, dz = True, 0, 0
    for (a, b), (a2, b2) in itertools.product(pyth[:6], repeat=2):
        w = unit2(-b, a)       # perpendicular within U={0,1} of the low ray u=(a,b)
        w2 = unit2(-b2, a2)
        if collinear(w, w2):
            continue
        for (p_, q_), (p2, q2), ph, ph2 in itertools.product(pyth, pyth, phases, phases):
            X = onb_of_plane(w, e[2], p_, q_, ph)
            Y = onb_of_plane(w2, e[2], p2, q2, ph2)
            G = gram(X, Y)
            pos_n += 1
            if det_I_minus_GstarG(G) != 0:
                pos_ok = False
            if G[0][0].iszero() and G[1][1].iszero():
                dz += 1
                b01, b10 = G[0][1].abs2(), G[1][0].abs2()
                good = (b01 == 1 and collinear(X[0], Y[1]) and collinear(X[0], e[2])) or \
                       (b10 == 1 and collinear(X[1], Y[0]) and collinear(X[1], e[2]))
                if not good:
                    pos_ok = False
    check("C4.a planes sharing e_c: det(I-G*G)=0 (norm exactly 1) for every exact ONB pair; every zero-diagonal "
          "instance has a unit off-diagonal whose rays are collinear with e_c", pos_ok,
          f"{pos_n} ONB pairs, {dz} zero-diagonal instances")
    check("C4.b at least one exact zero-diagonal instance was actually exercised", dz > 0)
    neg_ok, neg_n = True, 0
    f2 = (g(Fr(3, 5)), ZERO, g(Fr(4, 5)), ZERO)
    for (a, b) in pyth[:6]:
        w = unit2(-b, a)
        w2 = e[3]
        assert inner(w2, f2).iszero()
        for (p_, q_), (p2, q2), ph in itertools.product(pyth, pyth, phases):
            X = onb_of_plane(w, e[2], p_, q_, ph)
            Y = onb_of_plane(w2, f2, p2, q2)
            G = gram(X, Y)
            neg_n += 1
            if det_I_minus_GstarG(G) == 0:
                neg_ok = False
    check("C4.N negative control: non-intersecting planes in C^4 give det(I-G*G)!=0 (norm < 1) for every ONB pair",
          neg_ok and neg_n > 0, f"{neg_n} instances")


# =============================================================================
# C5  P23 cube structure and exact ray propagation on instances.
# =============================================================================
def control_C5():
    log("== C5  P23: K_{4,4} minus a perfect matching, faces, prism matching, exact ray propagation ==")
    R = [("R", i) for i in range(4)]
    C = [("C", j) for j in range(4)]
    edges = {frozenset({R[i], C[j]}) for i in range(4) for j in range(4) if i != j}
    deg = Counter(v for e_ in edges for v in e_)
    check("C5.a cube: 12 edges, every vertex degree 3", len(edges) == 12 and set(deg.values()) == {3})

    def adj(v): return [w for e_ in edges if v in e_ for w in e_ if w != v]
    faces = []
    for i1, i2 in itertools.combinations(range(4), 2):
        for j1, j2 in itertools.combinations(range(4), 2):
            cyc = [R[i1], C[j1], R[i2], C[j2]]
            if all(frozenset({cyc[k], cyc[(k + 1) % 4]}) in edges for k in range(4)):
                faces.append(cyc)
    check("C5.b exactly six 4-faces", len(faces) == 6)
    prism_ok = True
    for F in faces:
        leave = {}
        for v in F:
            others = [w for w in adj(v) if w not in F]
            if len(others) != 1:
                prism_ok = False
                break
            leave[v] = others[0]
        else:
            W = [leave[v] for v in F]
            if len(set(W)) != 4 or set(W) & set(F):
                prism_ok = False
            if not all(frozenset({W[k], W[(k + 1) % 4]}) in edges for k in range(4)):
                prism_ok = False
    check("C5.c every face: leaving edges form a perfect matching onto the opposite face preserving cyclic adjacency", prism_ok)

    E = lambda x, y: frozenset({x, y})

    def propagate(p, q, r, free=None):
        """Face v1=R0,v2=C2,v3=R1,v4=C3 with rays p (R0C2), q (C2R1), p (R1C3), r (C3R0).
        Propagate unique complements; if a complement is not unique (collinear inputs),
        use the supplied free ray.  Return dict edge->ray and vertex-consistency flag."""
        ray = {E(R[0], C[2]): p, E(C[2], R[1]): q, E(R[1], C[3]): p, E(C[3], R[0]): r}
        ray[E(R[0], C[1])] = complement3(p, r)   # leaving R0
        ray[E(C[2], R[3])] = complement3(p, q)   # leaving C2
        ray[E(R[1], C[0])] = complement3(q, p)   # leaving R1
        ray[E(C[3], R[2])] = complement3(p, r)   # leaving C3

        def comp(a, b):
            w = complement3(a, b)
            if iszerovec(w):
                assert free is not None and inner(a, free).iszero() and inner(b, free).iszero()
                return free
            return w
        # opposite face in cyclic order C1 - R3 - C0 - R2
        ray[E(R[3], C[1])] = comp(ray[E(R[0], C[1])], ray[E(C[2], R[3])])
        ray[E(R[3], C[0])] = comp(ray[E(C[2], R[3])], ray[E(R[3], C[1])])
        ray[E(R[2], C[0])] = comp(ray[E(R[1], C[0])], ray[E(R[3], C[0])])
        ray[E(R[2], C[1])] = comp(ray[E(C[3], R[2])], ray[E(R[2], C[0])])
        assert set(ray) == edges
        return ray, consistent(ray)

    def consistent(ray):
        for v in R + C:
            inc = [ray[e_] for e_ in edges if v in e_]
            if any(iszerovec(x) for x in inc):
                return False
            for x, y in itertools.combinations(inc, 2):
                if not inner(x, y).iszero():
                    return False
        return True

    def classify(ray, p_ref):
        pcls = [e_ for e_, v in ray.items() if collinear(v, p_ref)]
        matching = len(pcls) == 4 and len({v for e_ in pcls for v in e_}) == 8
        rest = [e_ for e_ in ray if e_ not in pcls]
        comps, seen = [], set()
        for e0 in rest:
            if e0 in seen:
                continue
            comp, stack = set(), [e0]
            while stack:
                x = stack.pop()
                if x in comp:
                    continue
                comp.add(x)
                for y in rest:
                    if y not in comp and x & y:
                        stack.append(y)
            seen |= comp
            comps.append(comp)
        two_squares = len(comps) == 2 and all(len(c_) == 4 for c_ in comps)
        classes_ok, bases = True, []
        for comp in comps:
            cl = []
            for e_ in comp:
                v = ray[e_]
                for k in cl:
                    if collinear(v, k[0]):
                        k.append(v)
                        break
                else:
                    cl.append([v])
            if len(cl) != 2 or any(len(k) != 2 for k in cl) or not inner(cl[0][0], cl[1][0]).iszero():
                classes_ok = False
            bases.append(cl)
        return matching, two_squares, classes_ok, bases

    p = (g(1), g(1), g(1))
    q = (g(1), g(-1), g(0))
    r = (g(1), I, g(-1) - I)
    assert inner(p, q).iszero() and inner(p, r).iszero() and not collinear(q, r)
    ray, cons = propagate(p, q, r)
    m_, sq_, cl_, bases = classify(ray, p)
    check("C5.d case q∦r: propagated cube is vertex-consistent (three pairwise orthogonal nonzero rays at every vertex)", cons)
    check("C5.e case q∦r: p-edges form a perfect matching; the other 8 edges are two vertex-disjoint squares, "
          "each alternating an orthogonal ray pair", m_ and sq_ and cl_)
    bq = any(any(collinear(k[0], q) for k in cl) for cl in bases)
    br = any(any(collinear(k[0], r) for k in cl) for cl in bases)
    check("C5.f case q∦r: the two square bases are {q,q⊥} and {r,r⊥}", bq and br)
    common = frozenset(range(3))
    for v in ray.values():
        common &= support(v)
    check("C5.g instance diagnostic: a coordinate used by all twelve rays exists", len(common) >= 1,
          f"common axes={sorted(common)}")
    p0 = complement3(p, q)
    s = vadd(p, vscale(g(0, 2), q))          # generic ray ⊥ p0, not collinear with p or q
    assert inner(p0, s).iszero() and not collinear(s, p) and not collinear(s, q)
    ray2, cons2 = propagate(p, q, q, free=s)
    m2, sq2, cl2, bases2 = classify(ray2, p0)
    check("C5.h case q=r: consistent; the four leaving edges (p0) form a perfect matching; two squares with orthogonal "
          "alternating pairs", cons2 and m2 and sq2 and cl2)
    rbad = (g(1), I, g(-1))
    assert not inner(p, rbad).iszero()
    _, cons_bad = propagate(p, q, rbad)
    check("C5.N1 negative control: a face with p not orthogonal to r is detected as vertex-inconsistent", not cons_bad)
    mut = dict(ray)
    mut[E(R[3], C[1])] = q      # claim the opposite-face edge is q instead of the forced p
    check("C5.N2 negative control: replacing the forced opposite-face p-edge by q is detected as inconsistent",
          not consistent(mut))


# =============================================================================
# C6  Exclusive-cycle bound arithmetic (P02/P08) at n=8.
# =============================================================================
def control_C6():
    log("== C6  P02/P08 pigeonhole arithmetic at n=8 ==")
    n = 8
    tab = {k: min(k - 1, n - k) for k in range(2, 8)}
    check("C6.a min(k-1, 8-k) <= 3 for all k=2..7 (no exclusive-axis cycle in a four-family)",
          max(tab.values()) <= 3, f"{tab}")
    check("C6.b P08 particular cases: C4 -> t<=1, C6 -> t<=2, C8 -> t<=3", (2 - 1, 3 - 1, 4 - 1) == (1, 2, 3))
    check("C6.N negative control: at n=10 the same bound would allow k=5 with min(4,5)=4", min(4, 5) == 4)


def main():
    t0 = native_date()
    log("f149 proof-control-v1.py -- reviewer-authored bounded exact controls (stdlib only)")
    log(f"start native clock: {t0}")
    log(f"python: {sys.version.split()[0]}  platform: {platform.platform()}")
    exists = os.path.exists(SRC)
    src_sha = sha256(SRC) if exists else "MISSING"
    src_bytes = os.path.getsize(SRC) if exists else -1
    src_lf = open(SRC, "rb").read().count(b"\n") if exists else -1
    log(f"source: {SRC}")
    log(f"source sha256={src_sha} bytes={src_bytes} LF={src_lf}")
    log(f"script sha256={sha256(os.path.abspath(__file__))}")
    check("source bytes/hash/LF match the manifest (2eeda45e…9775, 142557 B, 852 LF)",
          src_sha == "2eeda45e6c4396530b856c1aef85816fd84076ecd82e782738ac95aa8d529775"
          and src_bytes == 142557 and src_lf == 852)
    log()
    for ctl in (control_C1, control_C2, control_C3, control_C4, control_C5, control_C6):
        t = time.time()
        ctl()
        log(f"   ({ctl.__name__} {time.time() - t:.1f}s)")
        log()
    t1 = native_date()
    log(f"end native clock: {t1}")
    log(f"FAIL count: {FAILS}")
    log("Scope: finite/algebraic diagnostics of specific proof steps; not a proof of U13, not an "
        "independent-family, human, formal or novelty verification.")
    with open(RECEIPT, "w", encoding="utf-8") as f:
        f.write("\n".join(LINES) + "\n")
    print(f"receipt written: {RECEIPT}")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
