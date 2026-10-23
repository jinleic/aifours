"""PILOT checks for the d = 8 route (parent's x^(7/8) dual + complete-graph hypercontractivity); review/D8_PILOT.md.

Exact (sympy) identities:
  S1 entropy cancellation: with lambda_v = ln(C m_v^(7/8)) the coefficient of sum m ln m in U_lambda is
     (d-1)/4 - (d/4)(7/8) = 0 at d = 8;
  S2 closed form after optimising C: U(M) = (1-d) ln 4 + (d/2) ln(2 E(f)) = -10 ln 2 + 4 ln E(f) at d = 8;
     U(J) = Psi_8(J) = 8 ln 3 - 12 ln 2 with E(J) = 72 * 4^(-7/4) = 9/sqrt 2;
  S3 inclusion-exclusion: 2E = (sum f)^2 - sum_p R_p^2 - sum_q C_q^2 + sum f^2 (generic symbols);
  S4 row identity: S^2 + Q/2 = 18 ||T_(1/3) g||_2^2 on the uniform 4-point space (generic g);
  S5 ||g||_(8/7)^2 = 4^(-7/4) when g_j = r_j^(7/8) and sum r_j = 1;
  S6 finite-n weak duality kernel: max_{b>=0} (-b ln b + b theta) = e^(theta - 1).
Rigorous numerics (exact rationals / arb):
  R1 ln 7 < 2 (7 < e^2), hence rho = 1/3 <= 7^(-ln3/2) = (p'-1)^(-1/(4 alpha)) with alpha = 1/(2 ln 3), p' = 8;
  R2 a^2 - 1/9 > 0 for a = 7^(-ln3/2); kappa = (441/128)(a^2-1/9); C_8 = (4 sqrt2/9) kappa (enclosures);
  R3 control: d = 9 needs ln 8 <= 2, which is false (the route must fail at d = 9);
  R4 direct second proof of the row inequality F(r) = S^2 + Q/2 <= 9/(4 sqrt2) - c |r-U|^2 (c = 1/40):
     two-valued reduction (hand argument in the note) + arb subdivision of the families (x,y,y,y), (x,x,y,y)
     outside a neighbourhood of U, and a rigorous Taylor (second-derivative) bound near U.
Sanity (floats, non-evidence): E(f)(M) <= E(J) on random doubly stochastic and row-stochastic matrices.
Writes ../evidence/verify_d8_pilot.json.
"""
import json
import math
import os
from fractions import Fraction as Fr

import numpy as np
import sympy as sp
from flint import arb, ctx

ctx.prec = 200


def A(x):
    return arb(x.numerator) / arb(x.denominator) if isinstance(x, Fr) else arb(x)


def main():
    out = {"note": "PILOT checks; not a frozen proof; floats only in the sanity section"}
    # ---------------------------------------------------------------- S: exact identities
    S = {}
    d = sp.Integer(8)
    S["S1 (d-1)/4 - (d/4)(7/8) == 0 at d=8"] = sp.simplify((d - 1) / 4 - d / 4 * sp.Rational(7, 8)) == 0
    E_, Cc = sp.symbols("E C", positive=True)
    k = 4
    # U(C) = C_d - d ln C + (C^2/4) E with C_d = (1-d/2) ln4 + (d/2) ln d - d/2; optimise C
    Cd = (1 - d / 2) * sp.log(4) + d / 2 * sp.log(d) - d / 2
    Uc = Cd - d * sp.log(Cc) + Cc ** 2 / 4 * E_
    Copt = sp.solve(sp.diff(Uc, Cc), Cc)[0]
    Uopt = sp.simplify(Uc.subs(Cc, Copt))
    S["S2 optimal C^2 = 2d/E"] = sp.simplify(Copt ** 2 - 2 * d / E_) == 0
    S["S2 U_opt == (1-d) ln4 + (d/2) ln(2E)"] = sp.simplify(sp.expand_log(Uopt - ((1 - d) * sp.log(4) + d / 2 * sp.log(2 * E_)), force=True)) == 0
    EJ = 72 * sp.Rational(1, 4) ** sp.Rational(7, 4)
    S["S2 E(J) == 9/sqrt2"] = sp.simplify(EJ - 9 / sp.sqrt(2)) == 0
    UJ = (1 - d) * sp.log(4) + d / 2 * sp.log(2 * EJ)
    psiJ = (2 - d) * sp.log(4) + d * sp.log(3)
    S["S2 U(J) == Psi_8(J) == 8 ln3 - 12 ln2"] = (sp.simplify(sp.expand_log(UJ - psiJ, force=True)) == 0 and
                                                 sp.simplify(sp.expand_log(psiJ - (8 * sp.log(3) - 12 * sp.log(2)), force=True)) == 0)
    # S3 inclusion-exclusion on a generic 4x4 array
    F = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"f{i}{j}"))
    lhs = sum(F[p, q] * F[r, s] for p in range(4) for q in range(4) for r in range(4) for s in range(4) if p != r and q != s)
    tot = sum(F)
    R = [sum(F[p, :]) for p in range(4)]
    Cs = [sum(F[:, q]) for q in range(4)]
    rhs = tot ** 2 - sum(x ** 2 for x in R) - sum(x ** 2 for x in Cs) + sum(x ** 2 for x in F)
    S["S3 sum_{p!=r,q!=s} f f' == (sum f)^2 - sum R^2 - sum C^2 + sum f^2"] = sp.expand(lhs - rhs) == 0
    # S4 row identity
    g = sp.symbols("g0:4")
    Eg = sum(g) / 4
    rho = sp.Rational(1, 3)
    Tg = [Eg + rho * (gi - Eg) for gi in g]
    norm2 = sum(t ** 2 for t in Tg) / 4
    Srow = sum(g)
    Qrow = sum(gi ** 2 for gi in g)
    S["S4 S^2 + Q/2 == 18 ||T_(1/3) g||_2^2"] = sp.expand(Srow ** 2 + Qrow / 2 - 18 * norm2) == 0
    # S5 ||g||_{8/7}^2 for g = r^(7/8), sum r = 1:  ((1/4) sum r)^(2*7/8) = 4^(-7/4)
    r = sp.symbols("r0:4", positive=True)
    p = sp.Rational(8, 7)
    normp = (sum((ri ** sp.Rational(7, 8)) ** p for ri in r) / 4) ** (1 / p)
    S["S5 ||r^(7/8)||_(8/7) == ((sum r)/4)^(7/8)"] = sp.simplify(normp - (sum(r) / 4) ** sp.Rational(7, 8)) == 0
    # S6 max_b (-b ln b + b theta) = e^(theta-1)
    b, th = sp.symbols("b theta", positive=True)
    expr = -b * sp.log(b) + b * th
    bstar = sp.solve(sp.diff(expr, b), b)[0]
    S["S6 argmax b* = e^(theta-1) and max = e^(theta-1); concave (2nd derivative -1/b)"] = (
        sp.simplify(bstar - sp.exp(th - 1)) == 0 and sp.simplify(expr.subs(b, bstar) - sp.exp(th - 1)) == 0
        and sp.simplify(sp.diff(expr, b, 2) + 1 / b) == 0)
    out["S exact identities"] = S
    # ---------------------------------------------------------------- R: rigorous numerics
    Rr = {}
    e2 = arb(2).exp()
    Rr["R1 7 < e^2 (certain)"] = bool(arb(7) < e2)
    Rr["R1 also via rational bound e > 2.7 => e^2 > 7.29 > 7"] = (Fr(27, 10) ** 2 > 7)
    ln3, ln7 = arb(3).log(), arb(7).log()
    a2 = (-(ln3 * ln7)).exp()                  # a^2 = 7^(-ln 3)
    Rr["R2 a = 7^(-ln3/2)"] = str(a2.sqrt())
    Rr["R2 rho=1/3 <= a (certain)"] = bool(arb(1) / 3 < a2.sqrt())
    gap = a2 - arb(1) / 9
    Rr["R2 a^2 - 1/9 (enclosure)"] = str(gap)
    Rr["R2 a^2 - 1/9 > 0 (certain)"] = bool(gap > 0)
    kappa = arb(441) / 128 * gap
    C8 = 4 * arb(2).sqrt() / 9 * kappa
    Rr["R2 kappa = (441/128)(a^2-1/9)"] = str(kappa)
    Rr["R2 C_8 = (4 sqrt2/9) kappa"] = str(C8)
    Rr["R2 C_8 > 0.0147 (certain)"] = bool(C8 > arb("0.0147"))
    Rr["R3 control d=9: ln 8 > 2 (certain), so the condition (d-1) <= e^2 fails"] = bool(arb(8).log() > 2)
    Rr["R3 general condition: 1/3 <= (d-1)^(-ln3/2) <=> ln(d-1) <= 2; d=7: ln6 < 2, d=8: ln7 < 2"] = bool(arb(6).log() < 2) and bool(arb(7).log() < 2)
    # R4 direct verification of the row inequality on the two families, c = 1/40
    c = arb(1) / 40
    Fu = 9 / (4 * arb(2).sqrt())

    def pw(x, e):
        return arb(0) if x == 0 else A(x) ** e

    e78, e74 = arb(7) / 8, arb(7) / 4

    def F_family1(x):      # (x, y, y, y), y = (1-x)/3
        y = (1 - x) / 3
        Sv = pw(x, e78) + 3 * pw(y, e78)
        Qv = pw(x, e74) + 3 * pw(y, e74)
        return Sv * Sv + Qv / 2, (A(x) - A(Fr(1, 4))) ** 2 + 3 * (A(y) - A(Fr(1, 4))) ** 2

    def F_family2(x):      # (x, x, y, y), y = 1/2 - x
        y = Fr(1, 2) - x
        Sv = 2 * pw(x, e78) + 2 * pw(y, e78)
        Qv = 2 * pw(x, e74) + 2 * pw(y, e74)
        return Sv * Sv + Qv / 2, 2 * (A(x) - A(Fr(1, 4))) ** 2 + 2 * (A(y) - A(Fr(1, 4))) ** 2

    # monotone enclosure over an interval [lo, hi]: x^(7/8), x^(7/4) increasing; y decreasing in x
    def enclose1(lo, hi):
        ylo, yhi = (1 - hi) / 3, (1 - lo) / 3
        Smax = pw(hi, e78) + 3 * pw(yhi, e78)
        Qmax = pw(hi, e74) + 3 * pw(yhi, e74)
        Fmax = Smax * Smax + Qmax / 2
        # distance^2 is convex in x along the family, so its MAXIMUM over [lo, hi] is at an endpoint
        d1 = (A(lo) - A(Fr(1, 4))) ** 2 + 3 * (A((1 - lo) / 3) - A(Fr(1, 4))) ** 2
        d2 = (A(hi) - A(Fr(1, 4))) ** 2 + 3 * (A((1 - hi) / 3) - A(Fr(1, 4))) ** 2
        d2max = ((d1 + d2 + abs(d1 - d2)) / 2).upper()
        return Fmax, d2max

    def enclose2(lo, hi):
        yhi = Fr(1, 2) - lo
        Smax = 2 * pw(hi, e78) + 2 * pw(yhi, e78)
        Qmax = 2 * pw(hi, e74) + 2 * pw(yhi, e74)
        Fmax = Smax * Smax + Qmax / 2
        d1 = 4 * (A(lo) - A(Fr(1, 4))) ** 2
        d2 = 4 * (A(hi) - A(Fr(1, 4))) ** 2
        d2max = ((d1 + d2 + abs(d1 - d2)) / 2).upper()
        return Fmax, d2max

    def G_and_Gp(name, X):
        """G = S^2 + Q/2 + c*dist2 and its x-derivative along the family, in arb on the ball X."""
        a78, a74 = arb(7) / 8, arb(7) / 4
        q = arb(1) / 4
        if name.startswith("family (x,y,y,y)"):
            Y = (1 - X) / 3
            S = X ** a78 + 3 * Y ** a78
            Sp = a78 * (X ** (a78 - 1) - Y ** (a78 - 1))
            Q = X ** a74 + 3 * Y ** a74
            Qp = a74 * (X ** (a74 - 1) - Y ** (a74 - 1))
            D = (X - q) ** 2 + 3 * (Y - q) ** 2
            Dp = 2 * (X - q) - 2 * (Y - q)
        else:
            Y = arb(1) / 2 - X
            S = 2 * X ** a78 + 2 * Y ** a78
            Sp = 2 * a78 * (X ** (a78 - 1) - Y ** (a78 - 1))
            Q = 2 * X ** a74 + 2 * Y ** a74
            Qp = 2 * a74 * (X ** (a74 - 1) - Y ** (a74 - 1))
            D = 2 * (X - q) ** 2 + 2 * (Y - q) ** 2
            Dp = 4 * (X - q) - 4 * (Y - q)
        return S * S + Q / 2 + c * D, 2 * S * Sp + Qp / 2 + c * Dp

    eta = Fr(1, 25)
    res4 = {}
    for name, enc, lo0, hi0 in (("family (x,y,y,y), x in [0,1]", enclose1, Fr(0), Fr(1)),
                                ("family (x,x,y,y), x in [0,1/2]", enclose2, Fr(0), Fr(1, 2))):
        segs = [(lo0, Fr(1, 4) - eta), (Fr(1, 4) + eta, hi0)]
        ok, worst, count, centred = True, None, 0, 0
        for a0, b0 in segs:
            m = 4000
            for i in range(m):
                lo = a0 + (b0 - a0) * Fr(i, m)
                hi = a0 + (b0 - a0) * Fr(i + 1, m)
                Fmax, d2max = enc(lo, hi)
                slack = Fu - c * d2max - Fmax       # > 0 implies F(x) + c*dist2(x) < Fu on the whole piece
                count += 1
                if not bool(slack > 0):
                    # centred (mean-value) form: G(x) <= G(mid) + G'([lo,hi]) * [-rad, rad]
                    mid = (lo + hi) / 2
                    rad = float(hi - lo) / 2 * 1.000001 + 1e-30
                    Xb = A(mid) + arb(0, rad)
                    Gm, _ = G_and_Gp(name, A(mid))
                    _, Gp = G_and_Gp(name, Xb)
                    slack = Fu - (Gm + Gp * arb(0, rad))
                    centred += 1
                    if not bool(slack > 0):
                        ok = False
                v = float(slack.mid()) - float(slack.rad())
                if worst is None or v < worst[0]:
                    worst = (v, str(lo), str(hi))
        res4[name] = {"pieces": count, "pieces needing the centred form": centred,
                      "F <= F(U) - c|r-U|^2 certainly on every piece outside |x-1/4| < 1/25": ok,
                      "smallest certified slack (float display)": worst}
    # Taylor near U: second derivative of F along each family must be <= -2c * (d|r-U|^2/dx^2)/2 ...
    # use h(x) = F(x) - F(U) + c*dist2(x); h(1/4) = 0, h'(1/4) = 0 (by symmetry); bound h'' < 0 on |x-1/4| <= eta
    xs = sp.symbols("x", positive=True)
    Fs1 = (xs ** sp.Rational(7, 8) + 3 * ((1 - xs) / 3) ** sp.Rational(7, 8)) ** 2 + (xs ** sp.Rational(7, 4) + 3 * ((1 - xs) / 3) ** sp.Rational(7, 4)) / 2
    D1 = (xs - sp.Rational(1, 4)) ** 2 + 3 * ((1 - xs) / 3 - sp.Rational(1, 4)) ** 2
    Fs2 = (2 * xs ** sp.Rational(7, 8) + 2 * (sp.Rational(1, 2) - xs) ** sp.Rational(7, 8)) ** 2 + (2 * xs ** sp.Rational(7, 4) + 2 * (sp.Rational(1, 2) - xs) ** sp.Rational(7, 4)) / 2
    D2 = 2 * (xs - sp.Rational(1, 4)) ** 2 + 2 * (sp.Rational(1, 2) - xs - sp.Rational(1, 4)) ** 2
    taylor = {}
    for name, Fs, Ds in (("family1", Fs1, D1), ("family2", Fs2, D2)):
        h = Fs + sp.Rational(1, 40) * Ds
        hp = sp.diff(h, xs)
        hpp = sp.diff(h, xs, 2)
        hval = sp.N(h.subs(xs, sp.Rational(1, 4)) - 9 / (4 * sp.sqrt(2)), 50)
        hpval = sp.N(hp.subs(xs, sp.Rational(1, 4)), 50)
        # rigorous bound of h'' on [1/4 - eta, 1/4 + eta] by monotone pieces: split into 400 subintervals,
        # evaluate h'' with arb at interval balls (h'' is a sum of powers of x and (1-x) etc., analytic away from 0)
        # (h'' evaluated below with arb balls through eval_hpp)
        ok = True
        worst = None
        m = 400
        for i in range(m):
            lo = Fr(1, 4) - eta + 2 * eta * Fr(i, m)
            hi = Fr(1, 4) - eta + 2 * eta * Fr(i + 1, m)
            mid = (lo + hi) / 2
            rad = float(hi - lo) / 2 * 1.000001 + 1e-30
            ball = A(mid) + arb(0, rad)
            # interval evaluation through arb: rebuild h'' with arb powers
            v = eval_hpp(name, ball)
            if not bool(v < 0):
                ok = False
            fv = float(v.mid()) + float(v.rad())
            if worst is None or fv > worst:
                worst = fv
        taylor[name] = {"h(1/4) (should be 0)": str(hval), "h'(1/4) (should be 0)": str(hpval),
                        "h'' < 0 certainly on |x-1/4| <= 1/25 (400 balls)": ok, "largest h'' upper bound": worst}
    res4["Taylor neighbourhoods"] = taylor
    Rr["R4 direct row inequality, c = 1/40"] = res4
    out["R rigorous"] = Rr
    # ---------------------------------------------------------------- sanity floats
    rng = np.random.default_rng(78)
    import explore_exact_exponent as E
    f = lambda x: np.clip(x, 0, None) ** 0.875
    EJ = 9 / math.sqrt(2)
    worst_ds, worst_rs = -1e9, -1e9
    for _ in range(20000):
        M = E.sinkhorn(np.exp(rng.normal(scale=rng.choice([0.5, 1, 2, 4]), size=(4, 4))))
        y = f(M.reshape(-1))
        worst_ds = max(worst_ds, (0.5 * y @ (E.ADJ @ y) - EJ) / np.sum((M - E.J) ** 2))
        Rm = np.array([rng.dirichlet(np.ones(4) * rng.choice([0.1, 1, 4])) for _ in range(4)])
        y = f(Rm.reshape(-1))
        worst_rs = max(worst_rs, (0.5 * y @ (E.ADJ @ y) - EJ) / np.sum((Rm - E.J) ** 2))
    out["sanity: max (E(f)-E(J))/|M-J|^2 on 2e4 random DS / row-stochastic (floats; proof needs <= -kappa)"] = [worst_ds, worst_rs]
    # weak duality sanity: U(M) = -10 ln2 + 4 ln E_{7/8}(M) >= Psi_8(M) (exact inner optimum, Newton dual solver)
    gap_min, gap_J = 1e9, None
    for i in range(300):
        M = E.sinkhorn(np.exp(rng.normal(scale=rng.choice([0.3, 1, 2]), size=(4, 4))))
        y = f(M.reshape(-1))
        Uv = -10 * math.log(2) + 4 * math.log(0.5 * y @ (E.ADJ @ y))
        gap_min = min(gap_min, Uv - E.psi_exact(M, 8)[0])
    yJ = f(E.J.reshape(-1))
    gap_J = -10 * math.log(2) + 4 * math.log(0.5 * yJ @ (E.ADJ @ yJ)) - E.psi_exact(E.J, 8)[0]
    out["sanity: weak duality U - Psi_8 (min over 300 random DS; value at J) (floats; must be >= 0 and = 0)"] = [gap_min, gap_J]

    # beta-window control: B_beta(M) - B_beta(J) with lambda_v = alpha + beta ln m_v (D8_SCREEN §3 family)
    def B_beta(M, beta):
        mv = M.reshape(-1)
        ent = float(np.sum(np.where(mv > 0, mv * np.log(np.where(mv > 0, mv, 1.0)), 0.0)))
        y = np.clip(mv, 0, None) ** beta
        T = 0.5 * y @ (E.ADJ @ y)
        return (1 - 4) * math.log(4) - 4 * math.log(2) + (7 - 8 * beta) / 4 * ent + 4 * math.log(T)
    tests = []
    for _ in range(3000):
        tests.append(E.sinkhorn(np.exp(rng.normal(scale=rng.choice([0.3, 1, 2, 4]), size=(4, 4)))))
    perms = [np.eye(4), np.eye(4)[[1, 0, 3, 2]], np.eye(4)[[1, 2, 3, 0]]]
    for P in perms:
        for t in np.linspace(0.01, 1.0, 100):
            tests.append(E.family(P, t))
    window = {}
    for beta in (0.80, 0.84, 0.86, 0.87, 0.875, 0.88, 0.8808, 0.885, 0.89, 0.90, 0.95):
        bJ = B_beta(E.J, beta)
        worst = max((B_beta(M, beta) - bJ) / np.sum((M - E.J) ** 2) for M in tests)
        window[str(beta)] = worst
    out["control (floats): max over 3300 DS test matrices of (B_beta(M)-B_beta(J))/|M-J|^2; route needs < 0; "
        "beta = 7/8 is the entropy-cancelling choice, hypercontractive window beta <= e^2/(1+e^2) = 0.8808"] = window
    out["all_ok"] = bool(all(S.values()) and Rr["R1 7 < e^2 (certain)"] and Rr["R2 a^2 - 1/9 > 0 (certain)"]
                         and Rr["R2 rho=1/3 <= a (certain)"] and Rr["R3 control d=9: ln 8 > 2 (certain), so the condition (d-1) <= e^2 fails"]
                         and all(v["F <= F(U) - c|r-U|^2 certainly on every piece outside |x-1/4| < 1/25"]
                                 for kk, v in res4.items() if kk.startswith("family"))
                         and all(v["h'' < 0 certainly on |x-1/4| <= 1/25 (400 balls)"] for v in taylor.values()))
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "verify_d8_pilot.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print(json.dumps(out, indent=1, default=str))


def eval_hpp(name, X):
    """Second derivative of h = F + (1/40) dist^2 along the family, evaluated in arb on the ball X."""
    a78, a74 = arb(7) / 8, arb(7) / 4
    if name == "family1":
        Y = (1 - X) / 3
        # S = x^a + 3 y^a, Q = x^b + 3 y^b with y' = -1/3, y'' = 0
        S = X ** a78 + 3 * Y ** a78
        Sp = a78 * X ** (a78 - 1) - a78 * Y ** (a78 - 1)                 # d/dx of 3 y^a = 3 a y^(a-1) (-1/3)
        Spp = a78 * (a78 - 1) * X ** (a78 - 2) + a78 * (a78 - 1) * Y ** (a78 - 2) / 3
        Qpp = a74 * (a74 - 1) * X ** (a74 - 2) + a74 * (a74 - 1) * Y ** (a74 - 2) / 3
        Dpp = 2 + 3 * 2 * (arb(1) / 9)                                   # dist2 = (x-1/4)^2 + 3 (y-1/4)^2
    else:
        Y = arb(1) / 2 - X
        S = 2 * X ** a78 + 2 * Y ** a78
        Sp = 2 * a78 * X ** (a78 - 1) - 2 * a78 * Y ** (a78 - 1)
        Spp = 2 * a78 * (a78 - 1) * X ** (a78 - 2) + 2 * a78 * (a78 - 1) * Y ** (a78 - 2)
        Qpp = 2 * a74 * (a74 - 1) * X ** (a74 - 2) + 2 * a74 * (a74 - 1) * Y ** (a74 - 2)
        Dpp = 2 * 2 + 2 * 2
    # F = S^2 + Q/2 => F'' = 2 S'^2 + 2 S S'' + Q''/2 ; h'' = F'' + Dpp/40
    return 2 * Sp * Sp + 2 * S * Spp + Qpp / 2 + Dpp / 40


if __name__ == "__main__":
    main()
