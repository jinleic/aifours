#!/usr/bin/python3
"""
reviewer-f121-controls-v1.py
Reviewer-authored finite controls for review-wave f121 (privacy high-privacy universal Laplace).
Independently structured: every closed form used here was derived by the reviewer; no author
code exists in the candidate and none is imported or executed. Positive controls must PASS,
negative controls must show the expected VIOLATION, mutations probe boundaries.

Run exactly:  /usr/bin/python3 reviewer-f121-controls-v1.py
Writes (same directory): reviewer-f121-controls-v1-receipt.json / .txt
"""
import os, sys, json, hashlib, subprocess, math, random, platform
from fractions import Fraction as Fr
from decimal import Decimal, getcontext
import numpy as np
import scipy
from scipy import integrate, optimize, special

getcontext().prec = 60
HERE = os.path.dirname(os.path.abspath(__file__))
SELF = os.path.abspath(__file__)
CAND = ("/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/"
        "parallel-18/privacy-diamond-mse/frontier-20261028-sharp-high-privacy-universal-limit-v1.md")
MANIFEST = os.path.join(HERE, "manifest-v1.json")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        h.update(fh.read())
    return h.hexdigest()


def clock():
    return subprocess.run(["/bin/date", "-u", "+%Y-%m-%dT%H:%M:%SZ"],
                          capture_output=True, text=True).stdout.strip()


def pins(path):
    with open(path, "rb") as fh:
        data = fh.read()
    return {"path": path, "sha256": hashlib.sha256(data).hexdigest(),
            "bytes": len(data), "LF": data.count(b"\n")}


RESULTS = []


def rec(name, kind, ok, detail):
    RESULTS.append({"name": name, "kind": kind, "status": "PASS" if ok else "FAIL",
                    "detail": detail})
    print(f"[{'PASS' if ok else 'FAIL'}] ({kind}) {name}: {detail}")


# --------------------------------------------------------------------------------------
# A. Exact series identities and finite-eps universal relative error
# --------------------------------------------------------------------------------------
def control_A():
    # A1 exact Fraction identities (algebraic in b): sum b^n and sum (2n-1) b^n with exact tails
    allok = True
    det = []
    for b in [Fr(1, 2), Fr(9, 10), Fr(99, 100)]:
        N = 300
        S1 = sum(b ** n for n in range(1, N + 1))
        tail1 = b ** (N + 1) / (1 - b)
        S2 = sum((2 * n - 1) * b ** n for n in range(1, N + 1))
        tail2 = b ** (N + 1) * (2 * b / (1 - b) ** 2 + Fr(2 * N + 1) / (1 - b))
        ok1 = (S1 + tail1 == b / (1 - b))
        ok2 = (S2 + tail2 == b * (1 + b) / (1 - b) ** 2)
        allok &= ok1 and ok2
        det.append(f"b={b}: sum b^n id {ok1}, sum(2n-1)b^n id {ok2}")
    rec("A1 exact series identities (Fraction, partial sum + exact tail)", "positive", allok, "; ".join(det))

    # A2 Decimal(60): lower bounds vs Laplace values, universal relative error in [e^-eps, 1]
    allok = True
    det = []
    for eps_s in ["0.000001", "0.0001", "0.001", "0.01", "0.1", "0.5", "1", "2", "5"]:
        eps = Decimal(eps_s)
        b = (-eps).exp()
        LJ = 2 * b * (1 + b) / (1 - b) ** 2
        LL = 2 * b / (1 - b)
        UJ = 4 / eps ** 2
        UL = 2 / eps
        rJ = LJ / UJ
        rL = LL / UL
        ok = (LJ <= UJ) and (LL <= UL) and (b <= rJ <= 1) and (b <= rL <= 1)
        # kappa battery incl. oscillating / unbounded weights
        kappas = [Decimal(0), Decimal(1), 1 / eps, 1 / eps ** 2, 1 / eps ** 3,
                  Decimal(str(1 + math.sin(1 / float(eps)))) / eps ** Decimal("1.5"), Decimal(10) ** 6]
        for k in kappas:
            r = (LJ + k * LL) / (UJ + k * UL)
            ok &= (min(rJ, rL) - Decimal(10) ** -50 <= r <= max(rJ, rL) + Decimal(10) ** -50) and (b <= r <= 1)
        allok &= ok
        det.append(f"eps={eps_s}: 1-rJ={float(1 - rJ):.3e}, 1-rL={float(1 - rL):.3e}, "
                   f"(1-rJ)/eps={float((1 - rJ) / eps):.4f}, (1-rL)/eps={float((1 - rL) / eps):.4f}, "
                   f"1-e^-eps={float(1 - b):.3e}, ok={ok}")
    rec("A2 universal-in-kappa relative error: e^-eps <= inf/(4/eps^2+2kappa/eps) <= 1", "positive",
        allok, " | ".join(det))


# --------------------------------------------------------------------------------------
# B. Half-line tail inequalities on explicit private laws; negative controls without privacy
# --------------------------------------------------------------------------------------
def control_B():
    # B1 continuous Laplace rate eps (Decimal): P(|X|>=n)=b^n equality; moments vs bounds
    eps = Decimal("0.1")
    b = (-eps).exp()
    EabsX = 1 / eps
    EX2 = 2 / eps ** 2
    ok = (EabsX >= b / (1 - b)) and (EX2 >= b * (1 + b) / (1 - b) ** 2)
    rec("B1 Laplace(eps) satisfies E|X|>=b/(1-b), EX^2>=b(1+b)/(1-b)^2", "positive", ok,
        f"E|X|={float(EabsX):.6f} vs {float(b / (1 - b)):.6f}; EX^2={float(EX2):.6f} vs {float(b * (1 + b) / (1 - b) ** 2):.6f}; tail P(|X|>=n)=b^n exactly")

    # B2 discrete two-sided geometric p_k=(1-b)/(1+b) b^{|k|} (exact Fraction, b=9/10)
    b = Fr(9, 10)
    c = (1 - b) / (1 + b)
    pk = lambda k: c * b ** abs(k)
    priv = all(b <= pk(k) / pk(k + 1) <= 1 / b for k in range(-40, 40))
    tails_ok = all(2 * b ** n / (1 + b) >= b ** n for n in range(1, 60))
    E1 = 2 * b / (1 - b ** 2)
    E2 = 2 * b / (1 - b) ** 2
    # verify the closed forms by truncated sums (float tolerance, b^400 ~ 5e-19)
    N = 400
    E1s = 2 * sum(k * pk(k) for k in range(1, N + 1))
    E2s = 2 * sum(k * k * pk(k) for k in range(1, N + 1))
    cf_ok = abs(float(E1s - E1)) < 1e-12 and abs(float(E2s - E2)) < 1e-12
    ok = priv and tails_ok and cf_ok and (E1 >= b / (1 - b)) and (E2 >= b * (1 + b) / (1 - b) ** 2)
    rec("B2 discrete two-sided geometric: private ratio, P(|X|>=n)>=b^n, both moment bounds (exact)", "positive", ok,
        f"E|X|={float(E1):.6f}>= {float(b / (1 - b)):.6f}; EX^2={float(E2):.6f}>= {float(b * (1 + b) / (1 - b) ** 2):.6f}; closed forms ok={cf_ok}")

    # B3 staircase density f=c b^{|k|} on cell k (exact): tail equality, moments with slack
    b = Fr(9, 10)
    E1 = b / (1 - b) + Fr(1, 2)
    E2 = b * (1 + b) / (1 - b) ** 2 + b / (1 - b) + Fr(1, 3)
    # exact verification of these closed forms via cell sums with exact tails
    c = (1 - b) / 2
    N = 300
    S1 = 2 * sum(c * b ** k * Fr(2 * k + 1, 2) for k in range(0, N + 1))
    T1 = 2 * c * (b ** (N + 1)) * (Fr(2 * (N + 1) + 1, 2) / (1 - b) + b / (1 - b) ** 2)  # sum_{k>N} b^k (k+1/2)
    S2 = 2 * sum(c * b ** k * Fr(3 * k * k + 3 * k + 1, 3) for k in range(0, N + 1))
    # tail of sum_{k>N} b^k (k^2+k+1/3): shift m=k-N-1
    M = N + 1
    tail_k2 = b ** M * ((b * (1 + b) / (1 - b) ** 3) + 2 * M * b / (1 - b) ** 2 + Fr(M * M) / (1 - b))
    tail_k = b ** M * (b / (1 - b) ** 2 + Fr(M) / (1 - b))
    tail_1 = b ** M / (1 - b)
    T2 = 2 * c * (tail_k2 + tail_k + Fr(1, 3) * tail_1)
    cf_ok = (S1 + T1 == E1) and (S2 + T2 == E2)
    ok = cf_ok and (E1 >= b / (1 - b)) and (E2 >= b * (1 + b) / (1 - b) ** 2)
    # float spot-check of all-shift privacy ratio for d in [-1,1] (ratio in {b,1,1/b})
    bf = float(b)
    fcell = lambda x: bf ** abs(math.floor(x)) if x >= 0 else bf ** (abs(math.floor(x) + 1))
    rng = random.Random(1)
    priv = True
    for _ in range(20000):
        x = rng.uniform(-8, 8)
        d = rng.uniform(-1, 1)
        r = fcell(x) / fcell(x + d)
        priv &= (r <= 1 / bf + 1e-12)
    rec("B3 staircase private density: exact moment closed forms, bounds, all-shift ratio<=1/b", "positive",
        ok and priv, f"closed forms exact={cf_ok}; E|X|={float(E1):.5f}; EX^2={float(E2):.5f}; ratio spot-check ok={priv}")

    # B4 NEGATIVE: Laplace rate 2eps is NOT eps-private; bound (1) must fail
    eps = Decimal("0.1")
    b = (-eps).exp()
    E1 = 1 / (2 * eps)
    E2 = 2 / (2 * eps) ** 2
    viol = (E1 < b / (1 - b)) and (E2 < b * (1 + b) / (1 - b) ** 2)
    rec("B4 NEGATIVE: non-private Laplace(2eps) violates both bounds in (1)", "negative", viol,
        f"E|X|={float(E1):.4f} < {float(b / (1 - b)):.4f}; EX^2={float(E2):.4f} < {float(b * (1 + b) / (1 - b) ** 2):.4f}")

    # B5 NEGATIVE: X2 point mass (privacy fails for +-e2): J=2/eps^2 < 2b(1+b)/(1-b)^2
    J = 2 / eps ** 2
    viol = J < 2 * b * (1 + b) / (1 - b) ** 2
    rec("B5 NEGATIVE: X=(Laplace, 0) violates two-coordinate bound (needs both coordinate privacies)", "negative", viol,
        f"J={float(J):.4f} < {float(2 * b * (1 + b) / (1 - b) ** 2):.4f}")


# --------------------------------------------------------------------------------------
# C. Integration-by-parts inequalities (10) under |p'|<=p ; identity vs inequality separation
# --------------------------------------------------------------------------------------
def moments_1d(phi, dphi, breakpoints):
    """p ∝ exp(-phi) symmetric on R; returns (m1, m2, ibp1, ibp2) computed on [0,inf)."""
    w = lambda z: math.exp(-phi(z))
    def Q(g):
        tot = 0.0
        pts = [0.0] + breakpoints
        for a, c in zip(pts[:-1], pts[1:]):
            tot += integrate.quad(g, a, c, epsabs=1e-13, epsrel=1e-13)[0]
        tot += integrate.quad(g, pts[-1], np.inf, epsabs=1e-13, epsrel=1e-13)[0]
        return 2 * tot
    Z = Q(w)
    m1 = Q(lambda z: z * w(z)) / Z
    m2 = Q(lambda z: z * z * w(z)) / Z
    ibp1 = Q(lambda z: z * dphi(z) * w(z)) / Z        # = -∫ z p' dz  (should be 1)
    ibp2 = Q(lambda z: z * z * dphi(z) * w(z)) / Z    # = -∫ z|z| p' dz (should be 2 m1)
    return m1, m2, ibp1, ibp2


def control_C():
    # C1 Laplace: equality case
    m1, m2, i1, i2 = moments_1d(lambda z: abs(z), lambda z: 1.0, [1.0])
    ok = abs(m1 - 1) < 1e-10 and abs(m2 - 2) < 1e-10 and abs(i1 - 1) < 1e-10 and abs(i2 - 2 * m1) < 1e-10
    rec("C1 Laplace: E|Z1|=1, EZ1^2=2, IBP identities exact (equality case of (10))", "positive", ok,
        f"m1={m1:.12f} m2={m2:.12f} ibp1={i1:.12f} ibp2={i2:.12f}")

    # C2 p ∝ exp(-sqrt(1+z^2)): |dlogp/dz|=|z|/sqrt(1+z^2)<1 satisfies (9); strict inequalities
    m1, m2, i1, i2 = moments_1d(lambda z: math.sqrt(1 + z * z), lambda z: z / math.sqrt(1 + z * z), [1.0, 5.0])
    cf = 2 / (math.e * special.k1(1.0))  # reviewer closed form for E|Z1|
    ok = (m1 > 1 + 1e-6) and (m2 > 2 * m1 + 1e-6) and abs(i1 - 1) < 1e-9 and abs(i2 - 2 * m1) < 1e-9 and abs(m1 - cf) < 1e-9
    rec("C2 smooth (9)-density: E|Z1|>1 strictly, EZ1^2>2E|Z1| strictly, IBP identities, closed form 2/(e K1(1))", "positive", ok,
        f"m1={m1:.9f} (cf {cf:.9f}) m2={m2:.9f} 2m1={2 * m1:.9f} ibp1={i1:.9f} ibp2={i2:.9f}")

    # C3 exponential family: a=0.8 satisfies (9); a=1.5 violates (9) and the conclusion of (10) fails
    det = []
    ok = True
    for a, expect_sat in [(0.8, True), (1.5, False)]:
        m1, m2, i1, i2 = moments_1d(lambda z, a=a: a * abs(z), lambda z, a=a: a, [1.0])
        sat = (m1 >= 1 - 1e-10) and (m2 >= 2 * m1 - 1e-10)
        ident = abs(i1 - 1) < 1e-9 and abs(i2 - 2 * m1) < 1e-9
        ok &= (sat == expect_sat) and ident
        det.append(f"a={a}: m1={m1:.6f} m2={m2:.6f} (10)-conclusion holds={sat} (expected {expect_sat}); IBP identity holds={ident}")
    rec("C3 rate-a Laplace: (9) load-bearing (a=1.5 breaks (10) while IBP identity still holds)", "mutation", ok, " | ".join(det))

    # C4 perturbation cone inside (9): phi_theta=|z|-theta*min(|z|,1); outside: |z|+theta*min(|z|,1)
    det = []
    ok = True
    for theta in [0.0, 0.25, 0.5, 0.75, 1.0]:
        phi = lambda z, t=theta: abs(z) - t * min(abs(z), 1.0)
        dphi = lambda z, t=theta: (1 - t) if abs(z) < 1 else 1.0
        m1, m2, i1, i2 = moments_1d(phi, dphi, [1.0])
        cond = (abs(m1 - 1) < 1e-10 and abs(m2 - 2) < 1e-10) if theta == 0 else (m1 > 1 + 1e-6 and m2 > 2 * m1 + 1e-6)
        ident = abs(i1 - 1) < 1e-9 and abs(i2 - 2 * m1) < 1e-9
        ok &= cond and ident
        det.append(f"theta={theta}: m1={m1:.6f} m2={m2:.6f} ident={ident}")
    for theta in [0.25, 1.0]:
        phi = lambda z, t=theta: abs(z) + t * min(abs(z), 1.0)
        dphi = lambda z, t=theta: (1 + t) if abs(z) < 1 else 1.0
        m1, m2, i1, i2 = moments_1d(phi, dphi, [1.0])
        viol = m1 < 1 - 1e-6
        ok &= viol
        det.append(f"NEG theta={theta} (|phi'|=1+theta on |z|<1): m1={m1:.6f} <1 -> (10) fails as expected={viol}")
    rec("C4 (9)-cone perturbations keep E|Z1|>=1 with equality only at Laplace; steeper (non-(9)) perturbations break it", "mutation", ok, " | ".join(det))


# --------------------------------------------------------------------------------------
# D. Translation modulus (11): sharp constant 2tanh(s/2) vs candidate e^s-1 ; LP mutation
# --------------------------------------------------------------------------------------
def control_D():
    # D1 staircase with exact ratio C (Fraction): ||f - f_h||_1 = 2(C-1)/(C+1) exactly
    det = []
    ok = True
    for C in [Fr(11, 10), Fr(3, 2), Fr(3), Fr(7)]:
        c = (C - 1) / (C + 1)
        N = 200
        f = lambda k, c=c, C=C: c * C ** (-abs(k))
        S = sum(abs(f(k) - f(k - 1)) for k in range(-N, N + 1))
        # exact tails: k>=N+1 terms c C^{-k}(C-1); k<=-N-1 terms c C^{k}(1-1/C)
        tail_right = c * (C - 1) * C ** (-(N + 1)) / (1 - 1 / C)
        tail_left = c * (1 - 1 / C) * C ** (-(N + 1)) / (1 - 1 / C)
        L1 = S + tail_right + tail_left
        exact = (L1 == 2 * (C - 1) / (C + 1))
        cand = L1 <= C - 1
        naive = L1 <= 2 * (C - 1)
        ok &= exact and cand and naive
        det.append(f"C={C}: L1={float(L1):.6f} ==2(C-1)/(C+1):{exact}; <=C-1 ({float(C - 1):.4f}):{cand}")
    rec("D1 staircase: ||f-f_h||_1 = 2(C-1)/(C+1) exactly; candidate bound e^s-1 holds with slack", "positive", ok, " | ".join(det))

    # D1b Laplace translate: L1 = 2(1-C^{-1/2}) numeric via quad vs C-1
    det = []
    ok = True
    for lam, h in [(1.0, 0.3), (1.0, 1.0), (2.0, 0.7)]:
        C = math.exp(lam * h)
        g = lambda x: abs(0.5 * lam * math.exp(-lam * abs(x)) - 0.5 * lam * math.exp(-lam * abs(x - h)))
        L1 = (integrate.quad(g, -np.inf, 0, limit=400)[0] + integrate.quad(g, 0, h, limit=400)[0]
              + integrate.quad(g, h, np.inf, limit=400)[0])
        cf = 2 * (1 - C ** -0.5)
        ok &= abs(L1 - cf) < 1e-8 and L1 <= C - 1 and L1 <= 2 * (C - 1) / (C + 1) + 1e-12
        det.append(f"lam={lam},h={h}: L1={L1:.8f} cf={cf:.8f} sharp={2 * (C - 1) / (C + 1):.8f} cand={C - 1:.8f}")
    rec("D1b Laplace translate L1 = 2(1-C^-1/2) <= 2tanh(s/2) <= e^s-1", "positive", ok, " | ".join(det))

    # D2 LP on a cycle: max_f mu(A)-mu(A-h) under two-sided ratio constraints, for many A
    det = []
    ok = True
    m, q = 3, 30
    N = m * q
    rng = random.Random(7)
    for s in [0.2, 1.0, 3.0]:
        C = math.exp(s)
        bound = (C - 1) / (C + 1)
        cand_bound = (C - 1) / 2
        rows = []
        for k in range(N):
            r1 = np.zeros(N); r1[k] = 1; r1[(k + m) % N] -= C; rows.append(r1)
            r2 = np.zeros(N); r2[(k + m) % N] = 1; r2[k] -= C; rows.append(r2)
        A_ub = np.array(rows); b_ub = np.zeros(2 * N)
        A_eq = np.ones((1, N)); b_eq = np.array([1.0])
        def solve(Aset):
            ind = np.zeros(N)
            for k in Aset: ind[k] = 1
            cvec = -(ind - np.roll(ind, -m))  # maximize sum_k f_k [1_A(k) - 1_A(k+m)]
            res = optimize.linprog(cvec, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=(0, None), method="highs")
            assert res.status == 0, res.message
            return -res.fun, res.x
        sets = [set(range(N // 2)), set(range(m)), set(range(N // 4)), set(k for k in range(N) if (k // m) % 2 == 0)]
        for _ in range(12):
            sets.append(set(k for k in range(N) if rng.random() < 0.5))
        maxv = 0.0
        for Aset in sets:
            v, x = solve(Aset)
            maxv = max(maxv, v)
            # adaptive refinement: A* = {k: f_k > f_{k-m}} from LP optimum, re-solve
            for _ in range(4):
                Astar = set(k for k in range(N) if x[k] > x[(k - m) % N] + 1e-15)
                if not Astar: break
                v2, x = solve(Astar)
                maxv = max(maxv, v2)
        tol = 1e-7 * (1 + bound)
        ok &= (maxv <= bound + tol) and (maxv <= cand_bound + tol) and (maxv >= 0.99 * bound)
        det.append(f"s={s}: LPmax D={maxv:.9f}, sharp (C-1)/(C+1)={bound:.9f} (ratio {maxv / bound:.6f}), candidate (C-1)/2={cand_bound:.6f}")
    rec("D2 LP mutation on cycle (N=90): sup mu(A)-mu(A-h) <= (C-1)/(C+1) for all tested A incl. adaptive; attained", "mutation", ok, " | ".join(det))


# --------------------------------------------------------------------------------------
# E. §6 translated-mixture counterexample: exact moments, (5), TV/W1/W2 behaviour, privacy
# --------------------------------------------------------------------------------------
def control_E():
    # E1 reviewer closed form E|Z+R| = R + e^{-R}, Z ~ Laplace(1)
    det = []
    ok = True
    for R in [0.5, 2.0, 5.0]:
        val = integrate.quad(lambda z: abs(z + R) * 0.5 * math.exp(-abs(z)), -np.inf, -R, limit=300)[0] + \
              integrate.quad(lambda z: abs(z + R) * 0.5 * math.exp(-abs(z)), -R, 0, limit=300)[0] + \
              integrate.quad(lambda z: abs(z + R) * 0.5 * math.exp(-abs(z)), 0, np.inf, limit=300)[0]
        ok &= abs(val - (R + math.exp(-R))) < 1e-9
        det.append(f"R={R}: quad={val:.10f} cf={R + math.exp(-R):.10f}")
    rec("E1 closed form E|Z1+R| = R + e^-R (unit Laplace)", "positive", ok, " | ".join(det))

    # E2 mixture (1-t)Λ + t τ_{R e1}Λ, R=α^{1/2}, t=α^{-3/4}
    det = []
    ok = True
    prevW2 = -1
    for alpha in [16.0, 1e2, 1e3, 1e4, 1e6, 1e8]:
        R = math.sqrt(alpha); t = alpha ** -0.75
        U = 4 + t * R * R
        V = 2 + t * (R + math.exp(-R) - 1)
        obj = U + alpha * V
        rel = obj / (4 + 2 * alpha) - 1
        relbound = (alpha ** 0.25 + alpha ** 0.75) / (4 + 2 * alpha)
        W2lb = math.sqrt(U) - 2
        TV = t * (1 - math.exp(-R / 2))
        W1ub = t * R
        ok &= abs(U - (4 + alpha ** 0.25)) < 1e-9 * U and abs(V - 2) <= t * R + 1e-15 and abs(rel) <= relbound + 1e-15 \
              and W2lb > prevW2 and TV <= t and abs(W1ub - alpha ** -0.25) < 1e-12 * W1ub
        prevW2 = W2lb
        det.append(f"a={alpha:.0e}: U={U:.4f} V-2={V - 2:.3e} rel={rel:.3e} (<= {relbound:.3e}) W2>={W2lb:.4f} TV={TV:.3e} W1<={W1ub:.3e}")
    rec("E2 §6 mixture: U=4+α^1/4, |V-2|<=tR, (5)-relative error ->0, W2 lower bound ->∞, TV,W1 ->0", "positive", ok, " | ".join(det))

    # E3 mutation t=1/α: bounded second moment, W2 still bounded away from 0, (5) still holds
    det = []
    ok = True
    for alpha in [1e2, 1e4, 1e8]:
        R = math.sqrt(alpha); t = 1 / alpha
        U = 4 + t * R * R
        V = 2 + t * (R + math.exp(-R) - 1)
        rel = (U + alpha * V) / (4 + 2 * alpha) - 1
        W2lb = math.sqrt(U) - 2
        ok &= abs(U - 5) < 1e-12 and abs(rel) < 2 / math.sqrt(alpha) and W2lb > 0.23
        det.append(f"a={alpha:.0e}: U={U:.6f} rel={rel:.3e} W2>={W2lb:.4f}")
    rec("E3 mutation t=1/α: (5) holds, second moment bounded (U=5) yet W2 does not converge (>=√5-2)", "mutation", ok, " | ".join(det))

    # E4 TV of 1D Laplace translate = 1 - e^{-R/2} (quad)
    det = []
    ok = True
    for R in [0.5, 3.0]:
        g = lambda x: abs(0.5 * math.exp(-abs(x)) - 0.5 * math.exp(-abs(x - R)))
        L1 = integrate.quad(g, -np.inf, 0)[0] + integrate.quad(g, 0, R)[0] + integrate.quad(g, R, np.inf)[0]
        ok &= abs(L1 / 2 - (1 - math.exp(-R / 2))) < 1e-9
        det.append(f"R={R}: TV={L1 / 2:.9f} cf={1 - math.exp(-R / 2):.9f}")
    rec("E4 TV(τ_R Λ, Λ) = 1 - e^{-R/2} so TV(mixture, Λ) = t(1-e^{-R/2}) <= t", "positive", ok, " | ".join(det))

    # E5 privacy of mixture in X coordinates (eps=0.5, alpha=16): log f(x)-log f(x+d) <= eps on diamond boundary
    eps = 0.5; alpha = 16.0; R = math.sqrt(alpha); t = alpha ** -0.75; shift = R / eps
    def logf(x):
        a1 = math.log(1 - t) - eps * (abs(x[0]) + abs(x[1]))
        a2 = math.log(t) - eps * (abs(x[0] - shift) + abs(x[1]))
        mx = max(a1, a2)
        return mx + math.log(math.exp(a1 - mx) + math.exp(a2 - mx))
    rng = random.Random(3)
    worst = -1.0
    for _ in range(40000):
        x = (rng.uniform(-20, 30), rng.uniform(-20, 20))
        u = rng.uniform(-1, 1); v = (1 - abs(u)) * rng.choice([-1, 1])  # boundary of l1 diamond
        d = (u, v)
        worst = max(worst, logf(x) - logf((x[0] + d[0], x[1] + d[1])))
    rec("E5 mixture in X-coordinates is eps-private on the full diamond boundary (log-ratio <= eps)", "positive",
        worst <= eps + 1e-12, f"max log-ratio={worst:.12f} vs eps={eps}")


# --------------------------------------------------------------------------------------
# F/G. Laplace privacy positive + Gaussian negative; (7) step-count sanity
# --------------------------------------------------------------------------------------
def control_FG():
    eps = 0.3
    rng = random.Random(11)
    worst = -1.0
    for _ in range(40000):
        x = (rng.uniform(-15, 15), rng.uniform(-15, 15))
        u = rng.uniform(-1, 1); v = (1 - abs(u)) * rng.choice([-1, 1])
        lr = eps * ((abs(x[0] + u) + abs(x[1] + v)) - (abs(x[0]) + abs(x[1])))
        worst = max(worst, lr)
    rec("F1 product-Laplace density ratio <= e^eps on diamond boundary (reverse triangle inequality)", "positive",
        worst <= eps + 1e-12, f"max log-ratio={worst:.12f} eps={eps}")
    # negative: Gaussian ratio unbounded: log ratio = (|x+d|^2-|x|^2)/(2σ^2) grows linearly in |x|
    sig = 1.0
    x = (50.0, 0.0); d = (-1.0, 0.0)
    lr = ((x[0] + d[0]) ** 2 - x[0] ** 2) / (2 * sig ** 2)
    rec("F2 NEGATIVE: Gaussian noise violates eps-privacy (log-ratio at x=(50,0), d=(-1,0))", "negative",
        abs(lr) > eps, f"|log-ratio|={abs(lr):.3f} > eps={eps}")
    rng = random.Random(5)
    ok = True
    for _ in range(10000):
        eps_ = 10 ** rng.uniform(-4, 0)
        h = (rng.uniform(-5, 5), rng.uniform(-5, 5))
        h1 = abs(h[0]) + abs(h[1])
        n = math.ceil(h1 / eps_)
        if n == 0:
            continue
        step = (h[0] / (eps_ * n), h[1] / (eps_ * n))
        ok &= (abs(step[0]) + abs(step[1]) <= 1 + 1e-12) and (eps_ * n <= h1 + eps_ + 1e-12)
    rec("G1 (7) step decomposition: n=ceil(||h||_1/eps) equal steps lie in closed diamond, eps*n <= ||h||_1+eps", "positive", ok, "10000 random (h,eps)")


def main():
    t0 = clock()
    print("reviewer-f121-controls-v1 start", t0)
    print("interpreter", sys.executable, platform.python_version(), "numpy", np.__version__, "scipy", scipy.__version__)
    cand = pins(CAND)
    man = pins(MANIFEST)
    print("candidate pins", cand)
    print("manifest pins", man)
    control_A(); control_B(); control_C(); control_D(); control_E(); control_FG()
    t1 = clock()
    npass = sum(r["status"] == "PASS" for r in RESULTS)
    summary = {"script": SELF, "script_sha256": sha256(SELF), "clock_start_utc": t0, "clock_end_utc": t1,
               "interpreter": sys.executable, "python": platform.python_version(),
               "numpy": np.__version__, "scipy": scipy.__version__,
               "candidate_pins": cand, "manifest_pins": man,
               "n_controls": len(RESULTS), "n_pass": npass, "all_pass": npass == len(RESULTS), "results": RESULTS}
    with open(os.path.join(HERE, "reviewer-f121-controls-v1-receipt.json"), "w") as fh:
        json.dump(summary, fh, indent=2)
    with open(os.path.join(HERE, "reviewer-f121-controls-v1-receipt.txt"), "w") as fh:
        fh.write(f"reviewer-f121-controls-v1 receipt\nstart {t0}\nend {t1}\nscript sha256 {summary['script_sha256']}\n")
        fh.write(f"interpreter {sys.executable} python {platform.python_version()} numpy {np.__version__} scipy {scipy.__version__}\n")
        fh.write(f"candidate {cand}\nmanifest {man}\n")
        for r in RESULTS:
            fh.write(f"[{r['status']}] ({r['kind']}) {r['name']}: {r['detail']}\n")
        fh.write(f"controls {len(RESULTS)} pass {npass} all_pass {npass == len(RESULTS)}\n")
    print("end", t1, "controls", len(RESULTS), "pass", npass, "all_pass", npass == len(RESULTS))


if __name__ == "__main__":
    main()
