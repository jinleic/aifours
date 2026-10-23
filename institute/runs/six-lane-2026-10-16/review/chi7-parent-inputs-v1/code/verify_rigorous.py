"""Rigorous verification of every numeric inequality used in review/PROOF_CHI7.md (random 7-regular graph).

Two independent rigorous layers:
  (R) exact rational arithmetic (fractions.Fraction, Python big integers): logarithm enclosures from atanh series
      with explicit geometric tail bounds, and exact integer comparisons;
  (A) python-flint arb ball arithmetic (outward rounded) at 256 bits; an arb comparison is True only if certain.
Floating point appears only in the clearly labelled sanity section (S), which is NOT evidence.

Sections
  A. constants: 1 < ln3 < 4/3; C_d = (3/8)ln3 - d/18 (C_7 > 0 > C_8); c* = (27/8)ln3 in (7/2, 4);
     eta values (k=4); KPW threshold arithmetic; SSC numbers at (k,d) = (4,7).
  B. d = 8 control: phi_8(M) > phi_8(J/4) for M = (J/4 + I)/2, exactly via 13^32 > 2^56 * 3^32 * 5^5.
  C. first moment (proper 3-colourings of the pairing model): rigorous upper bound of the separable exponent
     Phi_d(x) = sum_k w_d(x_k), w_d(a) = (d-1) a ln a - d (1/2-a) ln(1/2-a), on the two KKT curves
     C1 = {(a,a,1-2a): a in [1/4,1/2]} and C2 = {(1/2,s,1/2-s): s in [0,1/2]}, for d = 5..8.
  S. sanity (floats, non-evidence): random checks of the per-row inequality and of the doubly stochastic decay bound.
  M. mutation controls: deliberately wrong constants must fail.
Writes ../evidence/verify_rigorous.json.  Run:  python -B verify_rigorous.py
"""
import json
import math
import os
import random
from fractions import Fraction as Fr

from flint import arb, ctx

ctx.prec = 256


# ----------------------------------------------------------------------------------------------- (R) rational logs
def atanh_bounds(x, terms=60):
    """Exact rational lower/upper bounds for atanh(x), 0 < x < 1 rational: partial sum and partial sum + tail,
    where tail = sum_{n>=N} x^(2n+1)/(2n+1) <= x^(2N+1) / ((2N+1) (1 - x^2))."""
    s = Fr(0)
    for n in range(terms):
        s += x ** (2 * n + 1) / (2 * n + 1)
    tail = x ** (2 * terms + 1) / ((2 * terms + 1) * (1 - x * x))
    return s, s + tail


def log_bounds(p, q=1):
    """Bounds for ln(p/q) with p/q > 1: ln(r) = 2 atanh((r-1)/(r+1))."""
    r = Fr(p, q)
    lo, hi = atanh_bounds((r - 1) / (r + 1))
    return 2 * lo, 2 * hi


LN2 = log_bounds(2)
LN3 = log_bounds(3)
LN5 = log_bounds(5)
LN13 = log_bounds(13)


def a_(x):
    if isinstance(x, Fr):
        return arb(x.numerator) / arb(x.denominator)
    return arb(x)


def certain_lt(x, y):
    return bool(x < y)


def main():
    out = {"precision_bits": ctx.prec}
    # ------------------------------------------------------------------------------------------- A. constants
    A = {}
    ln3_lo, ln3_hi = LN3
    A["ln3 rational enclosure (decimal, 30 digits)"] = [f"{float(ln3_lo):.15f}", f"{float(ln3_hi):.15f}"]
    A["ln3 width < 1e-30 (rational)"] = (ln3_hi - ln3_lo) < Fr(1, 10 ** 30)
    ln3 = arb(3).log()
    A["arb ln3 inside rational enclosure"] = bool(ln3 > a_(ln3_lo) - a_(Fr(1, 10 ** 40))) and bool(ln3 < a_(ln3_hi) + a_(Fr(1, 10 ** 40)))
    # A1  1 < ln 3 < 4/3   (sign structure of L' in the family-1 analysis; family-2 bound 3ln3/8 < 1/2)
    A["A1 1 < ln3 (rational)"] = ln3_lo > 1
    A["A1 ln3 < 4/3 (rational)"] = ln3_hi < Fr(4, 3)
    A["A1 arb"] = certain_lt(arb(1), ln3) and certain_lt(ln3, arb(4) / 3)
    # A2  C_d = (3/8) ln3 - d/18
    Cd = {}
    for d in (6, 7, 8):
        lo = Fr(3, 8) * ln3_lo - Fr(d, 18)
        hi = Fr(3, 8) * ln3_hi - Fr(d, 18)
        Cd[str(d)] = {"rational enclosure": [f"{float(lo):.12f}", f"{float(hi):.12f}"], "positive": lo > 0, "negative": hi < 0}
    A["A2 C_d = (3/8)ln3 - d/18"] = Cd
    A["A2 C_7 > 23/1000 (rational)"] = Fr(3, 8) * ln3_lo - Fr(7, 18) > Fr(23, 1000)
    A["A2 C_7 < 24/1000 (rational)"] = Fr(3, 8) * ln3_hi - Fr(7, 18) < Fr(24, 1000)
    # A3  c* = (27/8) ln 3 = (k-1)^3 log(k-1)/(k(k-2)) at k=4; threshold d* = 2c* = (27/4) ln 3 in (7, 8)
    A["A3 c* > 7/2 (rational)"] = Fr(27, 8) * ln3_lo > Fr(7, 2)
    A["A3 2c* < 8 (rational)"] = Fr(27, 4) * ln3_hi < 8
    A["A3 2c* enclosure"] = [f"{float(Fr(27, 4) * ln3_lo):.12f}", f"{float(Fr(27, 4) * ln3_hi):.12f}"]
    # A4  eta values at k = 4: eta(0)=2, eta(1/3)=(3/2)ln3, eta(3/4)=(4/3)ln4 ; min is (3/2) ln3
    A["A4 (3/2)ln3 < 2  <=>  ln3 < 4/3"] = Fr(3, 2) * ln3_hi < 2
    A["A4 (3/2)ln3 < (4/3)ln4  <=>  3^9 < 2^16 (exact integers)"] = 3 ** 9 < 2 ** 16
    A["A4 eta values (float display)"] = {"eta(0)": 2.0, "eta(1/3)": 1.5 * math.log(3), "eta(3/4)": (4 / 3) * math.log(4)}
    # A5  KPW threshold arithmetic
    ln2_lo, ln2_hi = LN2
    ln4_lo, ln4_hi = 2 * ln2_lo, 2 * ln2_hi
    A["A5 k=4 needs d < 6 ln3: 6 < 6ln3 < 7"] = (6 * ln3_lo > 6) and (6 * ln3_hi < 7)
    A["A5 d=7: k=5 since 7 < 8 ln4"] = 8 * ln4_lo > 7
    A["A5 d=7 exact clause d > 7 ln4 fails (7 ln4 > 7)"] = 7 * ln4_lo > 7
    A["A5 d=6: k=4 (2*2*ln2 < 6 < 6 ln3) and exact clause 6 > 5 ln3"] = (4 * ln2_hi < 6) and (6 * ln3_lo > 6) and (5 * ln3_hi < 6)
    # A6  SSC / second-moment numbers at (k,d) = (4,7)
    k, d = 4, 7
    A["A6 k^2-2k-d+2"] = k * k - 2 * k - d + 2
    A["A6 (d-1)/(k-1)^2"] = str(Fr(d - 1, (k - 1) ** 2))
    A["A6 sum lambda_m delta_m^2 = (k-1)^2 ln((k-1)/sqrt(k^2-2k-d+2)) = (9/2) ln 3 (float)"] = 4.5 * math.log(3)
    A["A6 E(Y^2)/(EY)^2 -> 3^(9/2) (float)"] = 3 ** 4.5
    A["A6 EY grows: k(1-1/k)^(d/2) > 1 <=> 16 (3/4)^7 > 1 (exact)"] = Fr(16) * Fr(3, 4) ** 7 > 1
    # A7  first moment at the balanced point (Molloy-Reed criterion q(1-1/q)^(d/2) < 1, q = 3), squared to be rational
    A["A7 d=7: 9 (2/3)^7 < 1 (exact)"] = 9 * Fr(2, 3) ** 7 < 1
    A["A7 d=6: 3 (2/3)^3 = 8/9 < 1 (exact)"] = 3 * Fr(2, 3) ** 3 < 1
    A["A7 d=5: 9 (2/3)^5 > 1 (exact; first moment inconclusive)"] = 9 * Fr(2, 3) ** 5 > 1
    out["A"] = A
    # ----------------------------------------------------------------------------------- B. d = 8 control
    B = {}
    # M = (J/4 + I)/2: rows (5/8, 1/8, 1/8, 1/8); rho = sum m^2 = 7/4.
    # phi_d(M) - phi_d(J/4) = ln2 - (5/8) ln5 + (d/2) ln(13/12)   [derivation in PROOF_CHI7.md, Control C2]
    # d = 8:  8 * diff = 32 ln13 - 56 ln2 - 32 ln3 - 5 ln5 > 0  <=>  13^32 > 2^56 3^32 5^5
    B["B1 13^32 > 2^56 * 3^32 * 5^5 (exact integers)"] = 13 ** 32 > 2 ** 56 * 3 ** 32 * 5 ** 5
    B["B1 log-ratio ln(13^32 / (2^56 3^32 5^5)) (float display)"] = 32 * math.log(13) - 56 * math.log(2) - 32 * math.log(3) - 5 * math.log(5)

    def phi_diff_arb(dd):
        return arb(2).log() - arb(5) / 8 * arb(5).log() + arb(dd) / 2 * (arb(13) / 12).log()

    def phi_direct_arb(dd, rows):
        Hm = arb(0)
        rho = arb(0)
        for row in rows:
            for m in row:
                ma = a_(m)
                if m != 0:
                    Hm -= ma * ma.log() / 4
                rho += ma * ma
        return Hm + arb(dd) / 2 * (arb(1) / 2 + rho / 16).log()

    Mrows = [[Fr(5, 8) if i == j else Fr(1, 8) for j in range(4)] for i in range(4)]
    Jrows = [[Fr(1, 4)] * 4 for _ in range(4)]
    for dd in (7, 8):
        dif = phi_diff_arb(dd)
        direct = phi_direct_arb(dd, Mrows) - phi_direct_arb(dd, Jrows)
        B[f"B2 d={dd}: phi(M)-phi(J/4) closed form (arb)"] = str(dif)
        B[f"B2 d={dd}: closed form == direct evaluation (balls overlap)"] = bool(abs(dif - direct) < arb("1e-60"))
        B[f"B2 d={dd}: sign"] = "+" if bool(dif > 0) else ("-" if bool(dif < 0) else "undecided")
    B["B3 M doubly stochastic (exact)"] = all(sum(r) == 1 for r in Mrows) and all(sum(Mrows[i][j] for i in range(4)) == 1 for j in range(4))
    out["B"] = B
    # ----------------------------------------------------------------------------------- C. first moment
    C = {}
    inv_e = 1 / arb(1).exp()

    def v_at(t):
        """t log t at an exact rational t in [0, 1] (arb ball)."""
        if t == 0:
            return arb(0)
        ta = a_(t)
        return ta * ta.log()

    def v_range(lo, hi):
        """Rigorous enclosure [L, U] (arb endpoints) of t log t over [lo, hi] subset [0, 1], lo <= hi rationals.
        t log t is decreasing on [0, 1/e] and increasing on [1/e, 1]."""
        vl, vh = v_at(lo), v_at(hi)
        if a_(hi) < inv_e:          # certainly hi < 1/e
            return vh.lower(), vl.upper()
        if a_(lo) > inv_e:          # certainly lo > 1/e
            return vl.lower(), vh.upper()
        a1, a2 = vl.upper(), vh.upper()
        U = ((a1 + a2 + abs(a1 - a2)) / 2).upper()   # ball containing max(a1, a2); its upper endpoint
        return (-inv_e).lower(), U

    def w_upper(dd, lo, hi):
        """Upper bound of w_d(a) = (d-1) a ln a - d (1/2 - a) ln(1/2 - a) over a in [lo, hi] subset [0, 1/2]."""
        _, Ua = v_range(lo, hi)
        Lc, _ = v_range(Fr(1, 2) - hi, Fr(1, 2) - lo)
        return (dd - 1) * Ua - dd * Lc

    def w_exact(dd, a):
        return (dd - 1) * v_at(a) - dd * v_at(Fr(1, 2) - a)

    N = 3000
    for dd in (5, 6, 7, 8):
        res = {}
        # C1: (a, a, 1-2a), a in [1/4, 1/2]
        all_neg1 = True
        worst1 = None
        for i in range(N):
            lo = Fr(1, 4) + Fr(i, 4 * N)
            hi = Fr(1, 4) + Fr(i + 1, 4 * N)
            ub = 2 * w_upper(dd, lo, hi) + w_upper(dd, 1 - 2 * hi, 1 - 2 * lo)
            if not bool(ub < 0):
                all_neg1 = False
            ubf = float(ub.mid()) + float(ub.rad())
            if worst1 is None or ubf > worst1[0]:
                worst1 = (ubf, str(lo), str(hi))
        # C2: (1/2, s, 1/2 - s), s in [0, 1/2]
        all_neg2 = True
        worst2 = None
        w_half = w_exact(dd, Fr(1, 2))
        for i in range(N):
            lo = Fr(i, 2 * N)
            hi = Fr(i + 1, 2 * N)
            ub = w_half + w_upper(dd, lo, hi) + w_upper(dd, Fr(1, 2) - hi, Fr(1, 2) - lo)
            if not bool(ub < 0):
                all_neg2 = False
            ubf = float(ub.mid()) + float(ub.rad())
            if worst2 is None or ubf > worst2[0]:
                worst2 = (ubf, str(lo), str(hi))
        bal = 3 * w_exact(dd, Fr(1, 3))
        res["Phi at balanced point x=(1/3,1/3,1/3) = ln3 + (d/2)ln(2/3) (arb)"] = str(bal)
        res["balanced value == ln3 + (d/2) ln(2/3)"] = bool(abs(bal - (arb(3).log() + arb(dd) / 2 * (arb(2) / 3).log())) < arb("1e-60"))
        res["C1 every piece certainly < 0"] = all_neg1
        res["C1 largest piece upper bound (float display) and piece"] = worst1
        res["C2 every piece certainly < 0"] = all_neg2
        res["C2 largest piece upper bound (float display) and piece"] = worst2
        res["conclusion: sup Phi_d < 0 on P (first moment -> 0)"] = all_neg1 and all_neg2
        C[f"d={dd}"] = res
    C["pieces per curve"] = N
    out["C"] = C
    # ----------------------------------------------------------------------------------- S. sanity (floats)
    S = {}
    rng = random.Random(20261017)
    c0 = 1.5 * math.log(3)

    def Dkl(p):
        return sum(x * math.log(4 * x) for x in p if x > 0)

    worst = float("inf")
    for _ in range(200000):
        e = [rng.expovariate(1.0) ** rng.choice([1, 2, 4]) for _ in range(4)]
        s = sum(e)
        p = [x / s for x in e]
        q = sum(x * x for x in p) - 0.25
        if q > 1e-12:
            worst = min(worst, Dkl(p) / q)
    S["S1 min over 2e5 random p of D(p||U)/(sum p^2 - 1/4) (float; expect >= 1.6479)"] = worst
    S["S1 (3/2) ln 3"] = c0
    p_star = [0.75, 1 / 12, 1 / 12, 1 / 12]
    S["S1 ratio at (3/4,1/12,1/12,1/12)"] = Dkl(p_star) / (sum(x * x for x in p_star) - 0.25)

    def phi(dd, M):
        Hm = -sum(m * math.log(m) for row in M for m in row if m > 0) / 4
        rho = sum(m * m for row in M for m in row)
        return Hm + dd / 2 * math.log(0.5 + rho / 16)

    def sinkhorn(M, it=200):
        for _ in range(it):
            M = [[x / sum(r) for x in r] for r in M]
            cs = [sum(M[i][j] for i in range(4)) for j in range(4)]
            M = [[M[i][j] / cs[j] for j in range(4)] for i in range(4)]
        return M

    C7 = 0.375 * math.log(3) - 7 / 18
    phiJ = math.log(4) + 7 * math.log(0.75)
    worst_ratio = float("inf")
    for _ in range(4000):
        M = sinkhorn([[rng.expovariate(1.0) ** rng.choice([1, 3, 6]) for _ in range(4)] for _ in range(4)])
        dev = sum((m - 0.25) ** 2 for row in M for m in row)
        if dev > 1e-9:
            worst_ratio = min(worst_ratio, (phiJ - phi(7, M)) / dev)
    S["S2 min over 4000 random doubly stochastic M of (phi_7(J/4)-phi_7(M))/||M-J/4||^2 (float; proof gives >= C_7)"] = worst_ratio
    S["S2 C_7 (float)"] = C7
    out["S (sanity, floats, NOT evidence)"] = S
    # ----------------------------------------------------------------------------------- M. mutation controls
    Mu = {}
    # per-row inequality with constant (3/2)ln3 + 1/100 must fail at p* (exact-ish check with arb)
    p_ex = [Fr(3, 4), Fr(1, 12), Fr(1, 12), Fr(1, 12)]
    D_ex = sum(a_(x) * (4 * a_(x)).log() for x in p_ex)
    S_ex = a_(sum(x * x for x in p_ex) - Fr(1, 4))
    Mu["M1 D(p*||U) - ((3/2)ln3 + 1/100) S(p*) < 0 (must be True: mutated constant fails)"] = bool(D_ex - (arb(3) / 2 * arb(3).log() + arb(1) / 100) * S_ex < 0)
    Mu["M1' D(p*||U) == (3/2) ln3 S(p*) (equality case, balls overlap)"] = bool(abs(D_ex - arb(3) / 2 * arb(3).log() * S_ex) < arb("1e-60"))
    Mu["M2 C_d < 0 at d = 15/2 (must be True)"] = Fr(3, 8) * ln3_hi - Fr(15, 2) / 18 < 0
    Mu["M3 first moment at d=5 not all negative (must be True)"] = not C["d=5"]["conclusion: sup Phi_d < 0 on P (first moment -> 0)"]
    Mu["M4 d=7 control at M=(J/4+I)/2 is negative (must be True)"] = B["B2 d=7: sign"] == "-"
    out["M (mutation controls)"] = Mu
    # ----------------------------------------------------------------------------------- verdict
    req = [
        A["A1 1 < ln3 (rational)"], A["A1 ln3 < 4/3 (rational)"], A["A1 arb"],
        A["A2 C_d = (3/8)ln3 - d/18"]["7"]["positive"], A["A2 C_d = (3/8)ln3 - d/18"]["8"]["negative"],
        A["A2 C_7 > 23/1000 (rational)"], A["A3 c* > 7/2 (rational)"], A["A3 2c* < 8 (rational)"],
        A["A4 (3/2)ln3 < 2  <=>  ln3 < 4/3"], A["A4 (3/2)ln3 < (4/3)ln4  <=>  3^9 < 2^16 (exact integers)"],
        A["A5 k=4 needs d < 6 ln3: 6 < 6ln3 < 7"], A["A5 d=7: k=5 since 7 < 8 ln4"],
        A["A5 d=7 exact clause d > 7 ln4 fails (7 ln4 > 7)"], A["A5 d=6: k=4 (2*2*ln2 < 6 < 6 ln3) and exact clause 6 > 5 ln3"],
        A["A6 k^2-2k-d+2"] == 3, A["A6 EY grows: k(1-1/k)^(d/2) > 1 <=> 16 (3/4)^7 > 1 (exact)"],
        A["A7 d=7: 9 (2/3)^7 < 1 (exact)"], A["A7 d=6: 3 (2/3)^3 = 8/9 < 1 (exact)"], A["A7 d=5: 9 (2/3)^5 > 1 (exact; first moment inconclusive)"],
        B["B1 13^32 > 2^56 * 3^32 * 5^5 (exact integers)"], B["B2 d=8: sign"] == "+", B["B2 d=8: closed form == direct evaluation (balls overlap)"],
        B["B2 d=7: closed form == direct evaluation (balls overlap)"], B["B3 M doubly stochastic (exact)"],
        C["d=7"]["conclusion: sup Phi_d < 0 on P (first moment -> 0)"], C["d=6"]["conclusion: sup Phi_d < 0 on P (first moment -> 0)"],
        C["d=8"]["conclusion: sup Phi_d < 0 on P (first moment -> 0)"],
        all(Mu.values()),
    ]
    out["all_required_true"] = all(bool(x) for x in req)
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "verify_rigorous.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1, default=str)
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
