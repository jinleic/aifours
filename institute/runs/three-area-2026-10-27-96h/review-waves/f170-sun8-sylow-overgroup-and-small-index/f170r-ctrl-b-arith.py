#!/usr/bin/env python3
"""f170r control B -- independently authored by reviewer ReviewF170Sun8Sylow.

Exhaustive exact arithmetic behind claims (b) and (c):
  * (c) Sec.2: any FIVE indices with pairwise gcds in {2..7} contain a triple
    with min_ordering B_{ij|k} = (d_ij - 1) * lcm(d_ik, d_jk) <= 42.
    Complete model: an index matters only through its exponents of 2,3,5,7
    capped at 3,2,2,2 (a shared exponent reaching the cap forces gcd >= 8, 9,
    25 or 49; a shared prime >= 11 forces gcd >= 11).  All 108 capped types,
    all type-triples and all type-5-multisets are enumerated.
  * (c) Sec.1: the valuation identity and the bound
      gcd(lcm(m_i,m_j) * c, m_k) <= (d_ij - 1) * lcm(d_ik, d_jk) for 1 <= c < d_ij.
  * (b) Sec.2: selection count (>= 4, or >= 5 if p divides no index) and the
    gcd step gcd(7*A*c, 7*a) = 7.
Negative controls must fail for the intended reason.
Usage: python3 -B this.py OUTFILE
"""
import itertools
import math
import sys

OUTPATH = sys.argv[1]
LINES = []
RESULTS = []


def log(*a):
    s = " ".join(str(x) for x in a)
    LINES.append(s)
    print(s, flush=True)


def check(name, ok, detail=""):
    RESULTS.append((name, bool(ok)))
    log(("PASS " if ok else "FAIL ") + name + ((" :: " + detail) if detail else ""))


def neg(name, rejected, detail=""):
    RESULTS.append(("NEG " + name, bool(rejected)))
    log(("NEG-REJECTED-AS-INTENDED " if rejected else "NEG-NOT-REJECTED(BAD) ") + name
        + ((" :: " + detail) if detail else ""))


def lcm(a, b):
    return a * b // math.gcd(a, b)


CAPS = (3, 2, 2, 2)
PR = (2, 3, 5, 7)
TYPES = [t for t in itertools.product(range(4), range(3), range(3), range(3))]


def tval(t):
    return 2 ** t[0] * 3 ** t[1] * 5 ** t[2] * 7 ** t[3]


def tgcd(s, t):
    m = tuple(min(a, b) for a, b in zip(s, t))
    if any(m[i] >= CAPS[i] for i in range(4)):
        return None  # true gcd >= 8, 9, 25 or 49
    return tval(m)


def valid(g):
    return g is not None and 2 <= g <= 7


def Bval(dij, dik, djk):
    return (dij - 1) * lcm(dik, djk)


def minB_from_gcds(dxy, dxz, dyz):
    return min(Bval(dxy, dxz, dyz), Bval(dxz, dxy, dyz), Bval(dyz, dxy, dxz))


def main():
    log("f170r control B: exhaustive arithmetic for claims (b),(c)")
    n = len(TYPES)
    check("108 capped types", n == 108)
    G = [[tgcd(TYPES[i], TYPES[j]) for j in range(n)] for i in range(n)]
    V = [[valid(G[i][j]) for j in range(n)] for i in range(n)]
    # sanity: capped gcd equals the true gcd of the representative integers when valid
    ok = all((not V[i][j]) or G[i][j] == math.gcd(tval(TYPES[i]), tval(TYPES[j]))
             for i in range(n) for j in range(n))
    check("capped-type gcd equals true gcd of representatives on every valid pair", ok)
    # sanity: representatives with exponents beyond the cap behave identically
    ok2 = True
    for i in range(n):
        for j in range(n):
            s, t = TYPES[i], TYPES[j]
            bump = tuple(e + (1 if e == CAPS[k] else 0) for k, e in enumerate(s))
            a, b = tval(bump), tval(t)
            truth = math.gcd(a, b)
            ok2 &= (V[i][j] == (2 <= truth <= 7)) and ((not V[i][j]) or truth == G[i][j])
    check("raising a capped exponent never changes validity or gcd", ok2)
    # ---- triples ----
    seven_max = 0
    seven_all42 = True
    non7_max = 0
    non7_arg = None
    patterns = set()
    minB = {}
    ntrip = 0
    for i, j, k in itertools.combinations_with_replacement(range(n), 3):
        if not (V[i][j] and V[i][k] and V[j][k]):
            continue
        ntrip += 1
        dxy, dxz, dyz = G[i][j], G[i][k], G[j][k]
        mb = minB_from_gcds(dxy, dxz, dyz)
        minB[(i, j, k)] = mb
        e7 = [TYPES[x][3] >= 1 for x in (i, j, k)]
        if all(e7):
            seven_all42 &= (dxy, dxz, dyz) == (7, 7, 7) and mb == 42 and \
                Bval(dxy, dxz, dyz) == Bval(dxz, dxy, dyz) == Bval(dyz, dxy, dxz) == 42
            seven_max = max(seven_max, mb)
        elif not any(e7):
            patterns.add(tuple(sorted((dxy, dxz, dyz))))
            if mb > non7_max:
                non7_max = mb
                non7_arg = (tval(TYPES[i]), tval(TYPES[j]), tval(TYPES[k]), (dxy, dxz, dyz))
    log("valid type-triples:", ntrip)
    check("three 7-divisible indices: all pairwise gcds 7 and B = 42 in every ordering", seven_all42 and seven_max == 42)
    check("three non-7 indices: min over orderings of B <= 40 (max attained 40)", non7_max == 40,
          f"max min-B {non7_max} at representatives {non7_arg}")
    log("realizable sorted non-7 gcd patterns:", sorted(patterns))
    check("the gcd pattern (4,5,6) is not realizable by integers", (4, 5, 6) not in patterns)
    neg("abstract pattern (4,5,6) without the realizability argument satisfies min-B <= 42",
        minB_from_gcds(4, 5, 6) > 42, f"min-B(4,5,6) = {minB_from_gcds(4, 5, 6)}")
    # hand cases of the candidate, as explicit pattern values
    hand = {
        "a=2: B=lcm(b,c)<=30": max(minB_from_gcds(2, b, c) for b in range(2, 7) for c in range(b, 7)) <= 30,
        "a=3,c<=5: <=40": max(minB_from_gcds(3, b, c) for b in range(3, 6) for c in range(b, 6)) <= 40,
        "a=3,c=6 b=3,4,6 via 3-edge <=24": all(Bval(3, b, 6) <= 24 for b in (3, 4, 6)),
        "a=3,b=5,c=6 via 5-edge = 24": Bval(5, 3, 6) == 24,
        "a=4 cases except (4,5,6) <=20": all(minB_from_gcds(4, b, c) <= 20 for b in range(4, 7)
                                             for c in range(b, 7) if (b, c) != (5, 6)),
        "a=5: 20,25,24": [minB_from_gcds(5, 5, 5), minB_from_gcds(5, 5, 6), minB_from_gcds(5, 6, 6)] == [20, 25, 24],
        "a=6: 30": minB_from_gcds(6, 6, 6) == 30,
    }
    for k_, v_ in hand.items():
        check("hand case " + k_, v_)
    # ---- five-multisets (direct, no pigeonhole) ----
    adj = [[j for j in range(n) if V[i][j] and j >= i] for i in range(n)]
    count5 = 0
    bad5 = []

    def tri(a, b, c):
        return minB[tuple(sorted((a, b, c)))]

    def rec(chosen, cands):
        nonlocal count5
        if len(chosen) == 5:
            count5 += 1
            if min(tri(a, b, c) for a, b, c in itertools.combinations(chosen, 3)) > 42:
                bad5.append(tuple(tval(TYPES[x]) for x in chosen))
            return
        for x in cands:
            nc = [y for y in cands if y >= x and V[x][y]]
            rec(chosen + [x], nc)

    rec([], [i for i in range(n) if any(V[i])])
    check("every valid 5-multiset of indices contains a triple with min-B <= 42 (direct enumeration)",
          count5 > 0 and not bad5, f"valid 5-multisets={count5} counterexamples={bad5[:3]}")
    # informational: are FOUR indices already enough for this method?  (not a negative control)
    bad4 = None
    n4 = 0
    for combo in itertools.combinations_with_replacement(range(n), 4):
        if all(V[a][b] for a, b in itertools.combinations(combo, 2)):
            n4 += 1
            if min(tri(a, b, c) for a, b, c in itertools.combinations(combo, 3)) > 42:
                bad4 = tuple(tval(TYPES[x]) for x in combo)
                break
    log("INFO four-index search: valid 4-multisets scanned =", n4,
        "; first 4-set with every triple min-B > 42 (None = none exists) =", bad4)
    # ---- valuation identity and bound (3) on integers ----
    R = range(1, 61)
    ok = all(math.gcd(lcm(a, b), c) == lcm(math.gcd(a, c), math.gcd(b, c)) for a in R for b in R for c in R)
    check("gcd(lcm(a,b),c) = lcm(gcd(a,c),gcd(b,c)) for all 1<=a,b,c<=60", ok)
    fake = next(((a, b, c) for a in R for b in R for c in R
                 if math.gcd(lcm(a, b), c) != math.gcd(a, c) * math.gcd(b, c)), None)
    neg("planted product variant gcd(lcm(a,b),c) = gcd(a,c)*gcd(b,c)", fake is not None, f"first failure {fake}")
    ok = all(math.gcd(x * y, z) <= math.gcd(x, z) * y for x in R for y in range(1, 13) for z in R)
    check("gcd(x*y,z) <= gcd(x,z)*y for 1<=x,z<=60, 1<=y<=12", ok)
    worst = 0
    okb = True
    cnt = 0
    for mi in range(2, 85):
        for mj in range(2, 85):
            dij = math.gcd(mi, mj)
            if not 2 <= dij <= 7:
                continue
            L = lcm(mi, mj)
            for mk in range(2, 85):
                dik, djk = math.gcd(mi, mk), math.gcd(mj, mk)
                if not (2 <= dik <= 7 and 2 <= djk <= 7):
                    continue
                bnd = Bval(dij, dik, djk)
                for c in range(1, dij):
                    g = math.gcd(L * c, mk)
                    cnt += 1
                    okb &= g <= bnd
                    worst = max(worst, g)
    check("bound (3): gcd(lcm(m_i,m_j)c, m_k) <= (d_ij-1)lcm(d_ik,d_jk) for all m<=84, 1<=c<d_ij",
          okb, f"{cnt} cases")
    # ---- (b) selection count ----
    mins = []
    min_unused = []
    for assign in itertools.product(range(9), repeat=4):  # prime -> index 0..7, or 8 = divides no a_i
        excluded = {a for a in assign if a < 8}
        sel = 8 - len(excluded)
        mins.append(sel)
        if assign[3] == 8:
            min_unused.append(sel)
    check("(b) selection: >= 4 selected indices, = 4 attainable; >= 5 if p divides no index",
          min(mins) == 4 and min(min_unused) == 5)
    neg("planted selection count without pairwise coprimality (all a_i = 30p allowed)",
        sum(1 for a in [30 * 11] * 8 if a % 11 and math.gcd(a, 30) == 1) < 4,
        "eight equal cofactors 330 leave 0 selected; coprimality (from gcd exactly 7) is load-bearing")
    # gcd step: gcd(7*A*c, 7*a) = 7 when gcd(a,30)=1, gcd(a,A)=1, c 5-smooth
    smooth = sorted({2 ** i * 3 ** j * 5 ** k for i in range(6) for j in range(4) for k in range(3)})
    ok = True
    for a in range(1, 400):
        if math.gcd(a, 30) != 1:
            continue
        for A in range(1, 200):
            if math.gcd(a, A) != 1:
                continue
            for c in smooth[:40]:
                ok &= math.gcd(7 * A * c, 7 * a) == 7 and lcm(7 * A * c, 7 * a) == 7 * A * a * c
    check("(b) gcd(7Ac,7a)=7 and lcm=7Aac whenever gcd(a,30)=gcd(a,A)=1 and c is 5-smooth", ok)
    neg("planted gcd step with an even cofactor a=2 and even c=6",
        math.gcd(7 * 1 * 6, 7 * 2) != 7, f"gcd(42,14)={math.gcd(42, 14)}")
    npass = sum(1 for _, ok_ in RESULTS if ok_)
    log(f"SUMMARY: {npass}/{len(RESULTS)} checks as expected; failures: {[nm for nm, ok_ in RESULTS if not ok_]}")
    with open(OUTPATH, "w") as fh:
        fh.write("\n".join(LINES) + "\n")


if __name__ == "__main__":
    main()
