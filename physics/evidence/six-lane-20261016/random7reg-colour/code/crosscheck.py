"""Independent cross-checks for review/PROOF_CHI7.r1.md (second route; not needed by the written proof).

X1 (rigorous, arb): Lemma 2.1(c) family 1, G(v) = (1+3v)ln(1+3v) + 3(1-v)ln(1-v) - (9/2) ln3 v^2 >= 0 on
    [-1/3, 1], by a route different from the hand proof:
    - on [-eta, eta] and [2/3-eta, 2/3+eta]: G'' > 0 rigorously, with G = G' = 0 exactly at 0 and 2/3;
    - elsewhere: G > 0 by subdivision with monotone enclosures of t ln t.
X2 (exact): Lemma 2.1(d) family 2 by convexity: H(u) = D(u) - (3/8)ln3 u^2 has H(0) = H'(0) = 0 and
    H'' = 1/(1-u^2) - (3/4)ln3 >= 1 - (3/4)ln3 > 0.
X3 (exact brute force): Lemma 5.1's count M(s) = prod s_i!/prod b_ij! of perfect matchings with no
    monochromatic pair, against exhaustive enumeration on small point sets.
X4 (exact big integers, sanity of the exponent): (1/n) ln E Z_3 for d = 7 and n = 20..320, computed exactly from
    Lemma 5.1, against the balanced exponent ln3 + (7/2)ln(2/3) = -0.3205.
Writes ../evidence/crosscheck.json.  Run: python -B crosscheck.py
"""
import itertools
import json
import math
import os
from fractions import Fraction as Fr
from math import comb, factorial

from flint import arb, ctx

ctx.prec = 200


def a_(x):
    return arb(x.numerator) / arb(x.denominator) if isinstance(x, Fr) else arb(x)


INV_E = 1 / arb(1).exp()


def tlnt(t):
    return arb(0) if t == 0 else a_(t) * a_(t).log()


def tlnt_range(lo, hi):
    vl, vh = tlnt(lo), tlnt(hi)
    if bool(a_(hi) < INV_E):
        return vh.lower(), vl.upper()
    if bool(a_(lo) > INV_E):
        return vl.lower(), vh.upper()
    a1, a2 = vl.upper(), vh.upper()
    return (-INV_E).lower(), ((a1 + a2 + abs(a1 - a2)) / 2).upper()


def X1(eta=Fr(1, 20), pieces=40000):
    ln3 = arb(3).log()
    res = {}
    # Taylor neighbourhoods: G''(v) = 9/(1+3v) + 3/(1-v) - 9 ln3 ; lower bound by monotonicity
    def gpp_lower(lo, hi):
        # 9/(1+3v) decreasing in v, 3/(1-v) increasing in v
        return 9 / (1 + 3 * a_(hi)) + 3 / (1 - a_(lo)) - 9 * ln3
    n1 = gpp_lower(-eta, eta)
    n2 = gpp_lower(Fr(2, 3) - eta, Fr(2, 3) + eta)
    res["G'' lower bound on [-eta, eta]"] = str(n1)
    res["G'' lower bound on [2/3-eta, 2/3+eta]"] = str(n2)
    res["G'' > 0 on both neighbourhoods (certain)"] = bool(n1 > 0) and bool(n2 > 0)
    # exact zeros: G(0) = 0, G'(0) = 0, G(2/3) = 3ln3 + ln(1/3) - 2ln3 = 0, G'(2/3) = 3 ln 9 - 6 ln 3 = 0
    G23 = 3 * ln3 + (arb(1) / 3).log() - 2 * ln3
    Gp23 = 3 * (arb(9)).log() - 6 * ln3
    res["G(2/3) == 0 and G'(2/3) == 0 (balls contain 0)"] = bool(abs(G23) < arb("1e-50")) and bool(abs(Gp23) < arb("1e-50"))
    # subdivision elsewhere: lower bound of G on [lo, hi]
    def G_lower(lo, hi):
        L1, _ = tlnt_range(1 + 3 * lo, 1 + 3 * hi)
        L2, _ = tlnt_range(1 - hi, 1 - lo)
        vmax2 = max(lo * lo, hi * hi)  # v^2 max on [lo, hi]
        return L1 + 3 * L2 - arb(9) / 2 * ln3 * a_(vmax2)
    segs = [(Fr(-1, 3), -eta), (eta, Fr(2, 3) - eta), (Fr(2, 3) + eta, Fr(1))]
    total = sum(s[1] - s[0] for s in segs)
    ok = True
    worst = None
    count = 0
    for lo0, hi0 in segs:
        m = max(1, int(pieces * (hi0 - lo0) / total))
        for i in range(m):
            lo = lo0 + (hi0 - lo0) * Fr(i, m)
            hi = lo0 + (hi0 - lo0) * Fr(i + 1, m)
            lb = G_lower(lo, hi)
            count += 1
            if not bool(lb > 0):
                ok = False
            f = float(lb.mid()) - float(lb.rad())
            if worst is None or f < worst[0]:
                worst = (f, str(lo), str(hi))
    res["subdivision pieces"] = count
    res["G > 0 certainly on every piece outside the two neighbourhoods"] = ok
    res["smallest piece lower bound (float display)"] = worst
    res["conclusion G >= 0 on [-1/3, 1]"] = ok and res["G'' > 0 on both neighbourhoods (certain)"] and res["G(2/3) == 0 and G'(2/3) == 0 (balls contain 0)"]
    return res


def X2():
    ln3 = arb(3).log()
    lb = 1 - arb(3) / 4 * ln3
    return {"min of H'' = 1/(1-u^2) - (3/4)ln3 >= 1 - (3/4)ln3": str(lb), "positive (certain)": bool(lb > 0)}


def matchings(points):
    if not points:
        yield []
        return
    a = points[0]
    for i in range(1, len(points)):
        b = points[i]
        rest = points[1:i] + points[i + 1:]
        for m in matchings(rest):
            yield [(a, b)] + m


def lemma51_formula(s):
    s1, s2, s3 = s
    b12, b13, b23 = (s1 + s2 - s3), (s1 + s3 - s2), (s2 + s3 - s1)
    if min(b12, b13, b23) < 0 or b12 % 2 or b13 % 2 or b23 % 2:
        return 0
    b12, b13, b23 = b12 // 2, b13 // 2, b23 // 2
    return factorial(s1) * factorial(s2) * factorial(s3) // (factorial(b12) * factorial(b13) * factorial(b23))


def X3():
    out = {}
    cases = [(4, 3, (2, 1, 1)), (4, 3, (1, 2, 1)), (4, 3, (2, 2, 0)), (6, 2, (2, 2, 2)), (6, 2, (3, 2, 1)),
             (4, 3, (3, 1, 0)), (5, 2, (2, 2, 1))]
    allok = True
    for n, d, sizes in cases:
        colour = []
        for c, m in enumerate(sizes):
            colour += [c] * m
        pts = list(range(n * d))
        cell = lambda p: p // d
        brute = sum(1 for mt in matchings(pts) if all(colour[cell(x)] != colour[cell(y)] for x, y in mt))
        formula = lemma51_formula(tuple(d * m for m in sizes))
        out[f"n={n},d={d},sizes={sizes}"] = {"brute": brute, "formula": formula}
        allok &= brute == formula
    out["all match"] = allok
    return out


def X4(d=7, ns=(20, 40, 80, 160, 320)):
    out = {}
    for n in ns:
        N = d * n
        pairings = factorial(N) // (factorial(N // 2) * 2 ** (N // 2))
        total = Fr(0)
        for n1 in range(n + 1):
            for n2 in range(n + 1 - n1):
                n3 = n - n1 - n2
                Ms = lemma51_formula((d * n1, d * n2, d * n3))
                if Ms:
                    total += Fr(comb(n, n1) * comb(n - n1, n2) * Ms, pairings)
        val = math.log(total.numerator) - math.log(total.denominator) if total > 0 else float("-inf")
        out[str(n)] = {"(1/n) ln E Z_3": val / n}
    out["balanced exponent ln3 + (7/2)ln(2/3)"] = math.log(3) + 3.5 * math.log(2 / 3)
    return out


def main():
    out = {"X1 family-1 G >= 0 (rigorous, second route)": X1(), "X2 family-2 convexity (rigorous)": X2(),
           "X3 Lemma 5.1 brute force (exact)": X3(), "X4 exact E Z_3 exponent for d=7 (sanity)": X4()}
    out["all_ok"] = bool(out["X1 family-1 G >= 0 (rigorous, second route)"]["conclusion G >= 0 on [-1/3, 1]"]
                         and out["X2 family-2 convexity (rigorous)"]["positive (certain)"]
                         and out["X3 Lemma 5.1 brute force (exact)"]["all match"])
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "crosscheck.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1, default=str)
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
