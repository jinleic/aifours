#!/usr/bin/env python3
# reviewer-f118-controls-v2.py
# v2 = reviewer-f118-controls-v1.py (SHA-256 4555b0c43718f0c33868d5d7588c2fb11cefc3c3a56de4e0fb1222090407f1a0) with ONE change:
#   the S2.b check used mp.polyroots, which raised NoConvergence (maxsteps=50) at b=0.999999 in the v1 run
#   (partial record: reviewer-f118-controls-output-v1.txt); it is replaced by the explicit quadratic formula.
#   Output/receipt file names bumped to v2. Everything else is byte-identical to v1.
# Independent same-harness reviewer controls for review wave
#   f118-privacy-occupied-cap-finite-dual
# Reviewed input (read in full before writing this file):
#   frontier-20261028-overlap-corrected-finite-dual-v1.md  (SHA-256 d57a58ca...124f3, 5928 B, 100 LF)
# This file contains ONLY reviewer-written code.  No author code is imported, copied or executed.
# Exact arithmetic  = fractions.Fraction (proof-grade for rational/polynomial identities).
# mpmath (50 digits) = labelled high-precision DIAGNOSTIC evaluation of closed forms, never proof.
# mp.quad appears only in labelled cross-checks of reviewer-derived closed forms, never as proof of an inequality.

import sys, os, hashlib, time, datetime, random, json, platform
from fractions import Fraction as Fr
from math import factorial, ceil
import mpmath as mp
mp.mp.dps = 50

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_TXT = os.path.join(HERE, "reviewer-f118-controls-output-v2.txt")
OUT_JSON = os.path.join(HERE, "reviewer-f118-receipt-v2.json")
INPUT = ("/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/"
         "parallel-18/privacy-diamond-mse/frontier-20261028-overlap-corrected-finite-dual-v1.md")
MANIFEST = ("/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/"
            "f118-privacy-occupied-cap-finite-dual/manifest-v1.json")


class Tee:
    def __init__(self, path):
        self.f = open(path, "w")

    def write(self, s):
        sys.__stdout__.write(s)
        self.f.write(s)

    def flush(self):
        sys.__stdout__.flush()
        self.f.flush()


sys.stdout = Tee(OUT_TXT)
RESULTS = []


def check(name, ok, detail=""):
    ok = bool(ok)
    RESULTS.append({"name": name, "pass": ok, "detail": detail})
    print(("PASS " if ok else "FAIL ") + name + (("  | " + detail) if detail else ""))
    return ok


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def lf_count(path):
    with open(path, "rb") as f:
        return f.read().count(b"\n")


t_start = time.time()
print("=== reviewer-f118-controls-v1.py (reviewer-written, exact + labelled diagnostics) ===")
print("clock_start_utc   ", datetime.datetime.now(datetime.timezone.utc).isoformat())
print("clock_start_local ", datetime.datetime.now().astimezone().isoformat())
print("python", sys.version.replace("\n", " "), "| mpmath", mp.__version__, "| platform", platform.platform())
SELF_SHA = sha256(os.path.abspath(__file__))
IN_SHA, IN_B, IN_LF = sha256(INPUT), os.path.getsize(INPUT), lf_count(INPUT)
MF_SHA, MF_B = sha256(MANIFEST), os.path.getsize(MANIFEST)
print("self_sha256    ", SELF_SHA)
print("input_sha256   ", IN_SHA, "bytes", IN_B, "LF", IN_LF)
print("manifest_sha256", MF_SHA, "bytes", MF_B)
check("S0.a input binding: SHA d57a58ca...124f3 / 5928 B / 100 LF",
      IN_SHA == "d57a58caedd6efd0751c5a4c6059c5c86db31446811e08bab317531da7d124f3" and IN_B == 5928 and IN_LF == 100)
check("S0.b manifest binding: SHA f650d734...6481 / 1814 B",
      MF_SHA == "f650d734052325037c8a33f673a2adf6b35505976e168becf2d1ee679d6ac481" and MF_B == 1814)

# =====================================================================================
# S1. Exact integrals over the closed l1 diamond D = {|x1|+|x2|<=1}; phi = |x|^2 + kappa*||x||_1
# =====================================================================================
print("\n--- S1: exact diamond integrals, G and d(T) closed forms, inequality (7), containment identity ---")


def tri_monomial(a, b):
    # ∫_{x,y>=0, x+y<=1} x^a y^b dx dy = a! b! / (a+b+2)!   (exact)
    return Fr(factorial(a) * factorial(b), factorial(a + b + 2))


int_D_sq = 4 * (tri_monomial(2, 0) + tri_monomial(0, 2))
int_D_l1 = 4 * (tri_monomial(1, 0) + tri_monomial(0, 1))
area_D = 4 * tri_monomial(0, 0)
check("S1.a ∫_D |x|^2 = 2/3 (exact)", int_D_sq == Fr(2, 3), str(int_D_sq))
check("S1.b ∫_D ||x||_1 = 4/3 (exact)", int_D_l1 == Fr(4, 3), str(int_D_l1))
check("S1.c |D| = 2 (exact)", area_D == 2, str(area_D))


def d_of_kappa(k):
    return int_D_sq + k * int_D_l1


check("S1.d d(κ) = 2/3 + 4κ/3 and d/2 < κ + 1/2 for κ ∈ {0,1/10,1/3,5}",
      all(d_of_kappa(k) == Fr(2, 3) + Fr(4, 3) * k and d_of_kappa(k) / 2 < k + Fr(1, 2)
          for k in [Fr(0), Fr(1, 10), Fr(1, 3), Fr(5)]))


# L-only cost phi=||x||_1 : G_L(T) = ∫(T-||x||_1)_+ = 4 * T^3 * ∫_tri (1-x-y) (scaling x -> T x)
def G_L(T):
    return Fr(2, 3) * T ** 3


def G_L_from_triangle(T):
    return 4 * T ** 3 * (tri_monomial(0, 0) - tri_monomial(1, 0) - tri_monomial(0, 1))


check("S1.e G_L(T) = 2T^3/3 equals exact scaled-triangle integral (T=1/7,1/2,2/3,1,5/2)",
      all(G_L(T) == G_L_from_triangle(T) for T in [Fr(1, 7), Fr(1, 2), Fr(2, 3), Fr(1), Fr(5, 2)]))

# scaled upper-bound integral used in (9): ∫(T - κ||x||_1)_+ dx = G_L(T)/κ^2 = 2T^3/(3κ^2)  (substitution y = κx)
check("S1.f ∫(T-κ||x||_1)_+ = 2T^3/(3κ^2) (exact scaling, κ=1/3,2,7; T=1/2,3)",
      all(G_L(T) / (k * k) == 2 * T ** 3 / (3 * k * k) for k in [Fr(1, 3), Fr(2), Fr(7)] for T in [Fr(1, 2), Fr(3)]))


# d_L(T) = ∫_D (||x||_1 - T)_+ : layer-cake in u=||x||_1 (|{||x||_1<=u}| = 2u^2, so "perimeter density" 4u)
def d_L(T):
    T = Fr(T)
    if T >= 1:
        return Fr(0)
    # ∫_T^1 (u-T) 4u du = 4/3 - 2T + 2T^3/3
    return Fr(4, 3) - 2 * T + Fr(2, 3) * T ** 3


# (7): G(T) - d(T) >= 2T - d.  For L-only: G_L - d_L - (2T - 4/3) = 0 for T<=1 and = (2/3)(T-1)^2(T+2) for T>=1
ok = True
for i in range(0, 41):
    T = Fr(i, 20)
    gap = G_L(T) - d_L(T) - (2 * T - Fr(4, 3))
    ok &= gap >= 0 and (gap == 0 if T <= 1 else gap == Fr(2, 3) * (T - 1) ** 2 * (T + 2))
check("S1.g inequality (7) for L-only at T=i/20, i=0..40: equality iff {phi<T} ⊂ D (T<=1), slack (2/3)(T-1)^2(T+2) beyond", ok)
check("S1.h at T=d/2=2/3: G_L(2/3) = d_L(2/3) = 16/81, so G(d/2) - b d(d/2) = (1-b)16/81 > 0  ⇒ root < d/2 strictly",
      G_L(Fr(2, 3)) == d_L(Fr(2, 3)) == Fr(16, 81))
check("S1.i containment identity d_L(T) = d - 2T + G_L(T) holds for T<=1 (sublevel inside D) and FAILS at T=3/2 (value 0 vs 7/12)",
      all(d_L(T) == Fr(4, 3) - 2 * T + G_L(T) for T in [Fr(1, 4), Fr(1, 2), Fr(2, 3), Fr(1)])
      and d_L(Fr(3, 2)) == 0 and Fr(4, 3) - 3 + G_L(Fr(3, 2)) == Fr(7, 12))
# outside-D cost: ||x||_1 > 1 ⇒ |x|^2 >= ||x||_1^2/2 > 1/2, so phi > 1/2 + κ > d/2 ; Cauchy–Schwarz check on rationals
ok = True
random.seed(118)
for _ in range(200):
    x1 = Fr(random.randint(-10 ** 6, 10 ** 6), random.randint(1, 10 ** 6))
    x2 = Fr(random.randint(-10 ** 6, 10 ** 6), random.randint(1, 10 ** 6))
    ok &= (x1 * x1 + x2 * x2) * 2 >= (abs(x1) + abs(x2)) ** 2
check("S1.j |x|^2 >= ||x||_1^2 / 2 (200 random rational points, exact)", ok)

# =====================================================================================
# S2. kappa = 0 closed form (3), old root, limits, candidate's printed floats (mp 50 digits; DIAGNOSTIC)
# =====================================================================================
print("\n--- S2: κ=0 closed form (3), looser root, limits, §5 floats (mp 50-digit DIAGNOSTIC) ---")


def B0_new(b):
    b = mp.mpf(b)
    return (2 * b / 3) / (b + mp.sqrt(b * b + (mp.pi / 3) * b * (1 - b)))


def B0_old(b):
    b = mp.mpf(b)
    return 2 * (mp.sqrt(b * b + mp.pi * b / 3) - b) / mp.pi


def Phi0(T, b):   # (1-b)G(T) + 2bT at κ=0 with G=πT^2/2
    return (1 - b) * mp.pi * T * T / 2 + 2 * b * T


ok = True
det = []
for b in ["0.01", "0.1", "0.5", "0.9", "0.999", "1e-8"]:
    bb = mp.mpf(b)
    B = B0_new(bb)
    res = Phi0(B, bb) - 2 * bb / 3
    Bo = B0_old(bb)
    reso = mp.pi * Bo ** 2 / 2 + 2 * bb * Bo - 2 * bb / 3
    ok &= abs(res) < mp.mpf(10) ** -45 and abs(reso) < mp.mpf(10) ** -45 and B > Bo and B < mp.mpf(1) / 3
    det.append(f"b={b}: res_new={mp.nstr(res, 3)} res_old={mp.nstr(reso, 3)} B={mp.nstr(B, 12)} B_old={mp.nstr(Bo, 12)}")
check("S2.a (3) satisfies (1) at κ=0 (|res|<1e-45); old root satisfies G+2bT=bd; B > B_old and B < 1/3 at six b", ok, "; ".join(det))

ok = True
for b in ["0.3", "0.77", "0.999999"]:
    bb = mp.mpf(b)
    c = (mp.pi / 3) * bb * (1 - bb)
    Bq = 2 * (mp.sqrt(bb * bb + c) - bb) / ((1 - bb) * mp.pi)        # explicit positive root of (1-b)πT^2/2 + 2bT - 2b/3 = 0 (unrationalized)
    Bneg = 2 * (-mp.sqrt(bb * bb + c) - bb) / ((1 - bb) * mp.pi)     # the other root, negative
    ok &= abs(Bq - B0_new(bb)) < mp.mpf(10) ** -44 and Bneg < 0 and abs(Phi0(Bq, bb) - 2 * bb / 3) < mp.mpf(10) ** -44
check("S2.b explicit quadratic-formula root of (1)|κ=0 equals rationalized (3) to 1e-44; other root negative (unique positive root)", ok)

b1 = 1 - mp.mpf(10) ** -25
b0 = mp.mpf(10) ** -30
check("S2.c B_0(b) -> 1/3 as b -> 1 (b = 1-1e-25)", abs(B0_new(b1) - mp.mpf(1) / 3) < mp.mpf(10) ** -20, mp.nstr(B0_new(b1), 30))
check("S2.d B_0(b)/sqrt(b) -> 2/sqrt(3π) as b -> 0 (b = 1e-30)",
      abs(B0_new(b0) / mp.sqrt(b0) - 2 / mp.sqrt(3 * mp.pi)) < mp.mpf(10) ** -14,
      mp.nstr(B0_new(b0) / mp.sqrt(b0), 20) + " vs " + mp.nstr(2 / mp.sqrt(3 * mp.pi), 20))

cand = {"0.01": ("0.05909111882108342", "0.05935971840483336"),
        "0.1": ("0.15196308045258433", "0.15765128068926104"),
        "0.5": ("0.24162562298805274", "0.2742577804065216"),
        "0.9": ("0.26980699911590084", "0.324163217120009")}
ok = True
det = []
for b, (o, n) in cand.items():
    bb = mp.mpf(b)
    on, nn = B0_old(bb), B0_new(bb)
    eo, en = abs(on - mp.mpf(o)), abs(nn - mp.mpf(n))
    ok &= eo < mp.mpf("1e-15") and en < mp.mpf("1e-15")
    det.append(f"b={b}: |old-cand|={mp.nstr(eo, 2)} |new-cand|={mp.nstr(en, 2)} new={mp.nstr(nn, 17)} old={mp.nstr(on, 17)}")
check("S2.e candidate §5 floats reproduced from reviewer closed forms to < 1e-15", ok, "; ".join(det))


def d_kappa_quad(k, B):
    # DIAGNOSTIC: ∫_D (phi - B)_+ with phi = |x|^2 + k||x||_1, by 4 x first-quadrant nested mp.quad split at the kink
    # (sublevel {phi<=B} must lie inside D; arc y_k(x) = -k/2 + sqrt(k^2/4 + B - x^2 - kx), x in [0, x_k])
    g = lambda x, y: max(x * x + y * y + k * (x + y) - B, 0)
    xk = (-k + mp.sqrt(k * k + 4 * B)) / 2

    def inner(x):
        if x < xk:
            yk = -k / 2 + mp.sqrt(k * k / 4 + B - x * x - k * x)
            return mp.quad(lambda y: g(x, y), [0, yk, 1 - x])
        return mp.quad(lambda y: g(x, y), [0, 1 - x])

    return 4 * mp.quad(inner, [0, xk, 1])


d0_third = d_kappa_quad(mp.mpf(0), mp.mpf(1) / 3)
check("S2.f DIAGNOSTIC (kink-split mp.quad, not proof): d_0(1/3) = π/18 = G_0(1/3) to 1e-25, i.e. (7) is an equality at T=d/2, κ=0",
      abs(d0_third - mp.pi / 18) < mp.mpf("1e-25"), f"d_0(1/3)≈{mp.nstr(d0_third, 20)} π/18={mp.nstr(mp.pi / 18, 20)}")

# =====================================================================================
# S3. Budget algebra (8)-(11): exact rational identities
# =====================================================================================
print("\n--- S3: budget constraints (8)-(11), exact rational algebra ---")


def F(r):
    return Fr(27, 4) * r * (1 - 2 * r) ** 2


check("S3.a F(1/24)=121/512, F(1/12)=25/64, F(1/9)=49/108 (the three §5 coefficients; r values not stated by author)",
      F(Fr(1, 24)) == Fr(121, 512) and F(Fr(1, 12)) == Fr(25, 64) and F(Fr(1, 9)) == Fr(49, 108))

# (8) algebra: Φ(H) >= b d  <=>  b <= G/(d-2H+G)  when d-2H>0  (exact sign check at random rationals)
ok = True
for _ in range(300):
    b = Fr(random.randint(1, 999), 1000)
    G = Fr(random.randint(0, 10 ** 4), 10 ** 4)
    d = Fr(random.randint(1, 10 ** 4), 10 ** 3)
    H = d / 2 * Fr(random.randint(0, 999), 1000)   # H < d/2
    lhs = (1 - b) * G + 2 * b * H >= b * d
    rhs = b <= G / (d - 2 * H + G)
    ok &= (lhs == rhs) and (d - 2 * H + G > 0)
check("S3.b (8): [(1-b)G(H)+2bH >= bd] <=> [b <= G(H)/(d-2H+G(H))] with positive denominator when H<d/2 (300 random exact)", ok)

rs = [Fr(1, 24), Fr(1, 12), Fr(1, 9), Fr(1, 7), Fr(1, 100), Fr(3, 20), Fr(33, 200)]
for _ in range(20):
    n = random.randint(1, 10 ** 6)
    rs.append(Fr(n, 6 * n + random.randint(1, 10 ** 6)))      # r < 1/6
ls = [Fr(1, 10), Fr(1, 3), Fr(1, 2), Fr(2, 3), Fr(7, 5), Fr(5, 2), Fr(10), Fr(random.randint(1, 10 ** 6), random.randint(1, 10 ** 6))]
ok = okd = okold = okstrict = okprem = okk = True
npts = 0
for r in rs:
    for l in ls:
        k = 2 * r / (1 - 6 * r)
        okk &= k > 0
        j = r * l
        H = j + k * l
        d = Fr(2, 3) + Fr(4, 3) * k
        U = 2 * H ** 3 / (3 * k * k)
        okd &= (d - 2 * H == Fr(2, 3) * (1 - 2 * r) * (1 - 9 * j) / (1 - 6 * r))
        okprem &= ((d - 2 * H > 0) == (j < Fr(1, 9)))
        if j < Fr(1, 9):
            lhs = U / (d - 2 * H + U)
            rhs = l ** 3 * F(r) / (1 - 9 * j + l ** 3 * F(r))
            ok &= (lhs == rhs)
            okold &= (U / (d - 2 * H) == l ** 3 * F(r) / (1 - 9 * j))
            okstrict &= rhs < l ** 3 * F(r) / (1 - 9 * j)
            npts += 1
check(f"S3.c (9) exact identity U/(d-2H+U) == l^3F(r)/(1-9j+l^3F(r)), κ=2r/(1-6r)>0, U=2H^3/(3κ^2), at {npts} rational (r,l) points "
      f"(27 r-values x 8 l-values exceed the cross-multiplied polynomial degrees ⇒ identity)", ok and okk)
check("S3.d d-2H == (2/3)(1-2r)(1-9j)/(1-6r) exactly; premise H<d/2 <=> j<1/9 when r<1/6", okd and okprem)
check("S3.e looser-root form U/(d-2H) == l^3F(r)/(1-9j); new (9) strictly smaller whenever j>0", okold and okstrict)

ok = oks = True
for l in [Fr(1, 10), Fr(1, 3), Fr(1, 2), Fr(3, 5), Fr(13, 20), Fr(2, 3) - Fr(1, 10 ** 6)]:
    lhs = G_L(l) / (Fr(4, 3) - 2 * l + G_L(l))
    rhs = l ** 3 / (2 - 3 * l + l ** 3)
    ok &= lhs == rhs and (2 - 3 * l + l ** 3) == (l - 1) ** 2 * (l + 2) and (2 - 3 * l + l ** 3) > 0
    oks &= rhs < l ** 3 / (2 - 3 * l)
check("S3.f (10) == G_L(l)/(d_L-2l+G_L(l)); denominator = (l-1)^2(l+2) > 0; strictly below looser l^3/(2-3l) for 0<l<2/3", ok and oks)
check("S3.g (10) at l = 2/3 equals exactly 1 (vacuous at the boundary, consistent with root <= 2/3)",
      Fr(2, 3) ** 3 / (2 - 3 * Fr(2, 3) + Fr(2, 3) ** 3) == 1)

# (11): (π j^2/2)/(2/3 - 2j + π j^2/2) == 3π j^2/(4 - 12 j + 3π j^2): exact coefficient scaling by 6
num_c, den_r, den_j, den_c = Fr(1, 2) * 6, Fr(2, 3) * 6, Fr(-2) * 6, Fr(1, 2) * 6
check("S3.h (11): scaling numerator/denominator of (8)|κ=0 by 6 gives coefficients (3π j^2)/(4 - 12 j + 3π j^2) exactly",
      num_c == 3 and den_r == 4 and den_j == -12 and den_c == 3)
ok = True
for j in ["0.01", "0.1", "0.2", "0.3", "0.3333"]:
    jj = mp.mpf(j)
    lhs = (mp.pi * jj ** 2 / 2) / (mp.mpf(2) / 3 - 2 * jj + mp.pi * jj ** 2 / 2)
    rhs = 3 * mp.pi * jj ** 2 / (4 - 12 * jj + 3 * mp.pi * jj ** 2)
    ok &= abs(lhs - rhs) < mp.mpf(10) ** -48 and rhs < 3 * mp.pi * jj ** 2 / (4 - 12 * jj) and (4 - 12 * jj + 3 * mp.pi * jj ** 2) > 0
check("S3.i (11) numeric agreement (<1e-48), positive denominator, strictly below looser 3πj^2/(4-12j) for 0<j<1/3", ok)
check("S3.j (11) denominator 4-12j+3πj^2 has negative discriminant 144-48π<0 (positive for ALL j)", 144 - 48 * mp.pi < 0)

# =====================================================================================
# S4. L-only exact-rational root controls: containment, strict improvement, relaxed-primal tightness, NEGATIVE wrong-cap controls
# =====================================================================================
print("\n--- S4: L-only exact roots, relaxed primal (explicit admissible densities), NEGATIVE wrong-cap/wrong-mass controls ---")


def bisect_root(f, lo, hi, iters=90):
    assert f(lo) < 0 < f(hi)
    for _ in range(iters):
        mid = (lo + hi) / 2
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return lo, hi


dL = Fr(4, 3)


def PhiL(T, b):
    return (1 - b) * G_L(T) + 2 * b * T


def hL(T, b):
    return G_L(T) - b * d_L(T)


def V_L(t, b):
    # explicit admissible density: p = bM on D (floor), + (1-b)M on {||x||_1<=t} ⊂ D (t<=1): 0<=p<=M, p>=bM on D, ∫p=1
    M = 1 / (2 * b + 2 * (1 - b) * t * t)
    return M * (b * dL + (1 - b) * Fr(4, 3) * t ** 3), M


bs = [Fr(1, 100), Fr(1, 10), Fr(1, 4), Fr(1, 2), Fr(9, 10), Fr(99, 100)]
summary = []
allok = True
BR = {}
for b in bs:
    lo, hi = bisect_root(lambda T: PhiL(T, b) - b * dL, Fr(0), Fr(2, 3))
    olo, ohi = bisect_root(lambda T: G_L(T) + 2 * b * T - b * dL, Fr(0), Fr(2, 3))
    BR[b] = (lo, hi, olo, ohi)
    ok1 = PhiL(Fr(2, 3), b) - b * dL == (1 - b) * Fr(16, 81)
    ok2 = (hL(lo, b) < 0 < hL(hi, b))
    ok3 = ohi < lo
    ts = [Fr(i, 400) for i in range(1, 401)] + [lo, hi, (lo + hi) / 2]
    okV = all(PhiL(V_L(t, b)[0], b) >= b * dL for t in ts)
    okM = all(0 < V_L(t, b)[1] <= 1 / (2 * b) for t in ts)
    Vmid = V_L((lo + hi) / 2, b)[0]
    Vmin = min(V_L(t, b)[0] for t in ts)
    okT = (Vmin >= lo) and (Vmid - hi < Fr(1, 10 ** 20))
    allok &= ok1 and ok2 and ok3 and okV and okM and okT
    summary.append(f"b={b}: B∈[{float(lo):.12f},{float(hi):.12f}] B_old∈[{float(olo):.12f},{float(ohi):.12f}] "
                   f"minV-B_hi={float(Vmin - hi):.1e} V(t=B_mid)-B_hi={float(Vmid - hi):.1e}")
check("S4.a L-only (exact, 90 bisections): Φ(2/3)-bd=(1-b)16/81>0 ⇒ B<2/3; root of (1) = root of G=b·d_L; B_old<B strictly; "
      "V(t)>=B for 403 explicit admissible densities per b; min V reached at t=B (tight relaxation)", allok, " ; ".join(summary))

ok = True
det = []
for b in [Fr(1, 10), Fr(1, 4)]:
    lo, hi, olo, ohi = BR[b]
    # NEGATIVE 1: over-tight cap M-2l on E  ->  (1-2b)G + 2bT = bd
    wlo, whi = bisect_root(lambda T: (1 - 2 * b) * G_L(T) + 2 * b * T - b * dL, Fr(0), Fr(2, 3))
    # NEGATIVE 2: forgetting the floor mass (∫g taken as 1 instead of 1-2l) -> (1-b)G = bd
    flo, fhi = bisect_root(lambda T: (1 - b) * G_L(T) - b * dL, Fr(0), Fr(2))
    t = (lo + hi) / 2
    V, M = V_L(t, b)
    ref1 = ((1 - 2 * b) * G_L(V) + 2 * b * V) < b * dL      # V < B_wrongcap exactly
    ref2 = ((1 - b) * G_L(V)) < b * dL                      # V < B_wrongmass exactly
    ok &= ref1 and ref2 and (wlo > hi) and (flo > hi)
    det.append(f"b={b}: B∈[{float(lo):.9f},{float(hi):.9f}]; B_wrongcap∈[{float(wlo):.9f},{float(whi):.9f}]; "
               f"B_wrongmass∈[{float(flo):.9f},{float(fhi):.9f}]; explicit density (M={float(M):.6f}, floor {float(b * M):.6f} on D, "
               f"fill level t={float(t):.6f}) costs {float(V):.9f} < both wrong 'bounds'")
check("S4.b NEGATIVE controls: over-tight cap (M-2ℓ on E) and forgotten floor mass each yield a 'bound' refuted by an explicit "
      "admissible density (0<=p<=M, p>=bM on D, ∫p=1); the candidate's cap/mass accounting is load-bearing", ok, " ; ".join(det))

# =====================================================================================
# S5. Translation-minimizer control: exact polygon clipping (L-only cost), I(x0,T)=∫_{x0+D}(||x||_1-T)_+ >= I(0,T)=d_L(T)
# =====================================================================================
print("\n--- S5: even-convex translation minimizer (exact polygon clipping, L-only cost) ---")


def clip_halfplane(poly, a, b, c):
    out = []
    n = len(poly)
    for i in range(n):
        P, Q = poly[i], poly[(i + 1) % n]
        fp, fq = a * P[0] + b * P[1] + c, a * Q[0] + b * Q[1] + c
        if fp >= 0:
            out.append(P)
        if (fp >= 0) != (fq >= 0):
            t = fp / (fp - fq)
            out.append((P[0] + t * (Q[0] - P[0]), P[1] + t * (Q[1] - P[1])))
    return out


def integrate_linear(poly, a, b, c):
    n = len(poly)
    if n < 3:
        return Fr(0)
    A2 = Cx = Cy = Fr(0)
    for i in range(n):
        x0, y0 = poly[i]
        x1, y1 = poly[(i + 1) % n]
        cr = x0 * y1 - x1 * y0
        A2 += cr
        Cx += (x0 + x1) * cr
        Cy += (y0 + y1) * cr
    if A2 == 0:
        return Fr(0)
    A = A2 / 2
    cx, cy = Cx / (6 * A), Cy / (6 * A)
    return abs(A) * (a * cx + b * cy + c)


def I_poly(poly, T):
    tot = Fr(0)
    for sx in (1, -1):
        for sy in (1, -1):
            P = clip_halfplane(poly, sx, 0, 0)
            P = clip_halfplane(P, 0, sy, 0)
            P = clip_halfplane(P, sx, sy, -T)
            tot += integrate_linear(P, sx, sy, -T)
    return tot


def I_shift(x0, T):
    X, Y = x0
    return I_poly([(X + 1, Y), (X, Y + 1), (X - 1, Y), (X, Y - 1)], T)


check("S5.a independent clipping integrator reproduces d_L(T) at x0=0 for T∈{0,1/4,1/2,2/3,1,3/2} (cross-checks S1 layer-cake formula)",
      all(I_shift((Fr(0), Fr(0)), T) == d_L(T) for T in [Fr(0), Fr(1, 4), Fr(1, 2), Fr(2, 3), Fr(1), Fr(3, 2)]))
shifts = [(Fr(1, 3), Fr(0)), (Fr(1, 2), Fr(1, 4)), (Fr(-1, 5), Fr(2, 5)), (Fr(1), Fr(1)), (Fr(3, 2), Fr(-1, 7)), (Fr(1, 1000), Fr(0)),
          (Fr(0), Fr(1, 1000)), (Fr(-3, 4), Fr(-3, 4))]
ok = okstrict = okeven = okconv = True
det = []
for T in [Fr(1, 4), Fr(1, 2), Fr(2, 3)]:
    base = I_shift((Fr(0), Fr(0)), T)
    for s in shifts:
        v = I_shift(s, T)
        ok &= v >= base
        okstrict &= v > base
        okeven &= v == I_shift((-s[0], -s[1]), T)
        okconv &= I_shift((2 * s[0], 2 * s[1]), T) + base >= 2 * v
        if T == Fr(2, 3):
            det.append(f"x0=({s[0]},{s[1]}): I={float(v):.6f} >= I(0)={float(base):.6f}")
check("S5.b I(x0,T) >= I(0,T) for 8 shifts x 3 levels (exact)", ok, " ; ".join(det))
check("S5.c strict increase I(x0,T) > I(0,T) for every nonzero shift tested (exact)", okstrict)
check("S5.d evenness I(x0)=I(-x0) and midpoint convexity I(2x0)+I(0)>=2I(x0) (exact)", okeven and okconv)

# =====================================================================================
# S6. kappa>0: reviewer-derived closed-form G_κ, roots, strict comparison, relaxed tightness (mp 50-digit DIAGNOSTIC)
# =====================================================================================
print("\n--- S6: κ>0 closed-form G_κ (reviewer derivation), roots B vs B_old, containment, relaxed tightness (mp DIAGNOSTIC) ---")


def Aq(s, k):
    # first-quadrant area of {phi<=s}: disk centre (-a,-a), radius R, a=κ/2, R^2=s+2a^2, cut to x,y>=0
    a = k / 2
    R2 = s + 2 * a * a
    R = mp.sqrt(R2)
    return (R2 / 2) * (mp.pi / 2 - 2 * mp.asin(a / R)) - a * mp.sqrt(R2 - a * a) + a * a


def area_sub(s, k):
    return 4 * Aq(s, k) if k > 0 else mp.pi * s


def G_k(T, k):
    if k == 0:
        return mp.pi * T * T / 2
    a = k / 2
    U2 = T + 2 * a * a
    U = mp.sqrt(U2)
    W = mp.sqrt(U2 - a * a)
    return (mp.pi * U2 ** 2 / 2 - 2 * U2 ** 2 * mp.asin(a / U) - (10 * a / 3) * W ** 3 - 2 * a ** 3 * W
            + 4 * a * a * U2 - mp.mpf(8) / 3 * a ** 4)


def Aq_direct(s, k):   # independent 1-D form: ∫_0^{xmax} (-a + sqrt(R^2-(x+a)^2)) dx  (mp.quad, smooth integrand)
    a = k / 2
    R2 = s + 2 * a * a
    xmax = -a + mp.sqrt(R2 - a * a)
    return mp.quad(lambda x: -a + mp.sqrt(R2 - (x + a) ** 2), [0, xmax])


ok = True
det = []
for k in [mp.mpf("0.1"), mp.mpf("0.5"), mp.mpf(1), mp.mpf(3)]:
    for T in [mp.mpf("0.2"), mp.mpf("0.7"), mp.mpf(2)]:
        e1 = abs(Aq(T, k) - Aq_direct(T, k))
        e2 = abs(G_k(T, k) - mp.quad(lambda s: area_sub(s, k), [0, T]))
        e3 = abs(mp.diff(lambda x: G_k(x, k), T) - area_sub(T, k))
        ub = G_k(T, k) <= 2 * T ** 3 / (3 * k * k)
        tt = (-k + mp.sqrt(k * k + 4 * T)) / 2
        lb = G_k(T, k) >= tt ** 4 + (2 * k / 3) * tt ** 3
        ok &= e1 < mp.mpf("1e-30") and e2 < mp.mpf("1e-30") and e3 < mp.mpf("1e-25") and ub and lb
    det.append(f"κ={mp.nstr(k, 3)} ok")
e0 = abs(G_k(mp.mpf("0.5"), mp.mpf("1e-12")) - mp.pi * mp.mpf("0.25") / 2)
check("S6.a DIAGNOSTIC: closed-form A_q and G_κ agree with independent 1-D quadratures (<1e-30), G' = sublevel area, "
      "2T^3/(3κ^2) upper bound and t^4+(2κ/3)t^3 lower bound hold, κ->0 limit πT^2/2", ok and e0 < mp.mpf("1e-10"), " ; ".join(det))


def mp_bisect(f, lo, hi, iters=170):
    assert f(lo) < 0 < f(hi)
    for _ in range(iters):
        mid = (lo + hi) / 2
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


ok = True
det = []
for b in [mp.mpf("0.01"), mp.mpf("0.1"), mp.mpf("0.5"), mp.mpf("0.9")]:
    for k in [mp.mpf(0), mp.mpf("0.1"), mp.mpf("0.5"), mp.mpf(1), mp.mpf(3)]:
        d = mp.mpf(2) / 3 + 4 * k / 3
        Phi = lambda T, b=b, k=k, d=d: (1 - b) * G_k(T, k) + 2 * b * T - b * d
        B = mp_bisect(Phi, mp.mpf(0), d / 2)
        Bo = mp_bisect(lambda T, b=b, k=k, d=d: G_k(T, k) + 2 * b * T - b * d, mp.mpf(0), d / 2)
        A = area_sub(B, k)
        M = 1 / (2 * b + (1 - b) * A)
        V = M * (b * d + (1 - b) * (B * A - G_k(B, k)))         # cost of the explicit relaxed density filled to level B
        okr = (B > Bo) and (B < d / 2) and (d / 2 < k + mp.mpf(1) / 2) and abs(V - B) < mp.mpf("1e-40") and abs(Phi(B)) < mp.mpf("1e-45")
        # relaxed densities filled to other levels T<=κ+1/2 (fill inside D) must cost >= B
        okV = True
        for i in range(1, 61):
            T = (k + mp.mpf(1) / 2) * i / 60
            A2 = area_sub(T, k)
            M2 = 1 / (2 * b + (1 - b) * A2)
            V2 = M2 * (b * d + (1 - b) * (T * A2 - G_k(T, k)))
            okV &= V2 >= B - mp.mpf("1e-40")
        ok &= okr and okV
        if k in (mp.mpf("0.5"), mp.mpf(3)) or b == mp.mpf("0.5"):
            det.append(f"b={mp.nstr(b, 3)} κ={mp.nstr(k, 3)}: B={mp.nstr(B, 12)} B_old={mp.nstr(Bo, 12)} d/2={mp.nstr(d / 2, 6)}")
check("S6.b DIAGNOSTIC (170-step mp bisection): for b∈{.01,.1,.5,.9} x κ∈{0,.1,.5,1,3}: B>B_old, B<d/2<κ+1/2, V(B)=B to 1e-40 "
      "(relaxation tight), 60 other fill levels cost >= B", ok, " ; ".join(det))

ok = True
det = []
for (b, k) in [(mp.mpf("0.5"), mp.mpf(1)), (mp.mpf("0.1"), mp.mpf("0.5")), (mp.mpf("0.9"), mp.mpf(3))]:
    d = mp.mpf(2) / 3 + 4 * k / 3
    B = mp_bisect(lambda T, b=b, k=k, d=d: (1 - b) * G_k(T, k) + 2 * b * T - b * d, mp.mpf(0), d / 2)
    dq = d_kappa_quad(k, B)
    res = G_k(B, k) - b * dq
    ident = dq - (d - 2 * B + G_k(B, k))
    ok &= abs(res) < mp.mpf("1e-25") and abs(ident) < mp.mpf("1e-25")
    det.append(f"b={mp.nstr(b, 2)} κ={mp.nstr(k, 2)}: G(B)-b·d_κ(B)≈{mp.nstr(res, 3)}, d_κ(B)-(d-2B+G(B))≈{mp.nstr(ident, 3)}")
check("S6.c DIAGNOSTIC (kink-split mp.quad, not proof): root of (1) also solves G(T)=b·∫_D(phi-T)_+ and d_κ(B)=d-2B+G(B) (<1e-25) for κ=1,1/2,3", ok, " ; ".join(det))

# =====================================================================================
# S7. NEGATIVE sublevel/containment control: rectangle privacy set D'=[-2,2]x[-1/4,1/4] (|D'|=2), L-only cost (exact)
#     The dual argument gives root B*' of G(T)=b d'(T); the (1)-form reduction needs {phi<T} ⊂ D', which FAILS here.
# =====================================================================================
print("\n--- S7: NEGATIVE sublevel control — rectangle privacy set where containment fails (exact rational) ---")
a_, c_ = Fr(2), Fr(1, 4)
dP = a_ + c_          # ∫_{D'} ||x||_1 = 2ac(a+c) = a+c since 2ac = 1


def pos(x):
    return x if x > 0 else Fr(0)


def dP_T(T):
    return Fr(2, 3) * (pos(a_ + c_ - T) ** 3 - pos(c_ - T) ** 3 - pos(a_ - T) ** 3)


rect = [(a_, -c_), (a_, c_), (-a_, c_), (-a_, -c_)]
check("S7.a d'(T) closed form equals independent clipping integral over D' at T∈{0,1/8,1/4,1/2,1,2,9/4}; d'(0)=9/4",
      all(dP_T(T) == I_poly(rect, T) for T in [Fr(0), Fr(1, 8), Fr(1, 4), Fr(1, 2), Fr(1), Fr(2), Fr(9, 4)]) and dP_T(Fr(0)) == dP == Fr(9, 4))
check("S7.b identity d'(T) = d' - 2T + G_L(T) holds at T=c/2 (sublevel inside D') but FAILS at T=1/2 and T=1",
      dP_T(c_ / 2) == dP - 2 * (c_ / 2) + G_L(c_ / 2) and all(dP_T(T) != dP - 2 * T + G_L(T) for T in [Fr(1, 2), Fr(1)]))
ok = True
det = []
for b in [Fr(1, 2), Fr(9, 10)]:
    hP = lambda T, b=b: G_L(T) - b * dP_T(T)                 # true dual root function (increasing)
    P1 = lambda T, b=b: (1 - b) * G_L(T) + 2 * b * T - b * dP  # (1)-form with d' (what the reduction WOULD give)
    slo, shi = bisect_root(hP, Fr(0), Fr(3))
    olo, ohi = bisect_root(P1, Fr(0), Fr(3))

    def cost_t(t, b=b):
        # explicit admissible density for D': floor bM on D', fill at residual cap ((1-b)M inside D', M outside) on {||x||_1<=t}, c<t<=a
        Ain = 2 * t * t - 2 * (t - c_) ** 2
        Iin = Fr(4, 3) * t ** 3 - 2 * (Fr(2, 3) * t ** 3 - c_ * t * t + c_ ** 3 / 3)
        Aout = 2 * t * t - Ain
        Iout = Fr(4, 3) * t ** 3 - Iin
        M = 1 / ((1 - b) * Ain + Aout + 2 * b)
        l = b * M
        return l * dP + (M - l) * Iin + M * Iout, M, t

    cands = [cost_t(Fr(i, 400)) for i in range(101, 801)]
    best = min(cands, key=lambda z: z[0])
    sep = olo > shi                       # (1)-form root strictly above true dual root
    ref = P1(best[0]) < 0                 # explicit density cost < (1)-form root  (exact)
    cons = all(hP(z[0]) >= 0 for z in cands)   # every explicit density costs >= true dual root (exact)
    contain_fails = shi > c_              # the true root's sublevel {||x||_1<=B*'} is NOT inside D'
    ok &= sep and ref and cons and contain_fails
    det.append(f"b={b}: B*'∈[{float(slo):.9f},{float(shi):.9f}] (>c=0.25: containment fails); (1)-form root∈[{float(olo):.9f},{float(ohi):.9f}]; "
               f"explicit density (M={float(best[1]):.6f}, fill level t={float(best[2]):.4f}) costs {float(best[0]):.9f} < (1)-form root")
check("S7.c NEGATIVE: with containment failing, the (1)-form root exceeds the true dual root and is refuted by an explicit admissible density; "
      "all explicit densities still cost >= the true dual root (containment lemma is load-bearing, and the dual itself stays valid)", ok, " ; ".join(det))

# =====================================================================================
# S8. POSITIVE control: explicit l1-diamond ε-private staircase laws (exact rational moments) must satisfy J>=B_0, L>=B_L, J+κL>=B_κ
# =====================================================================================
print("\n--- S8: POSITIVE control — explicit ε-private staircase laws (exact rational moments) ---")


def geo_sums(b):
    return (b / (1 - b), b / (1 - b) ** 2, b * (1 + b) / (1 - b) ** 3, b * (1 + 4 * b + b * b) / (1 - b) ** 4)


ok = True
for b in [Fr(1, 2), Fr(1, 10), Fr(9, 10)]:
    S = geo_sums(b)
    bb = mp.mpf(b.numerator) / b.denominator
    N = 4000
    ps = [mp.fsum(bb ** kk * kk ** m for kk in range(1, N)) for m in range(4)]
    ok &= all(abs(mp.mpf(S[m].numerator) / S[m].denominator - ps[m]) < mp.mpf("1e-30") for m in range(4))
check("S8.a geometric moment sums Σk^m b^k (m=0..3) closed forms match 4000-term partial sums (<1e-30)", ok)


def stair_moments(b, delta):
    # density p = M b^{k(x)}, k(x) = max(0, ceil(||x||_1 - delta)); shells {delta+k-1 < ||x||_1 <= delta+k}
    S0, S1, S2, S3 = geo_sums(b)
    M = 1 / (2 * delta ** 2 + 2 * ((2 * delta - 1) * S0 + 2 * S1))
    L = M * (Fr(4, 3) * delta ** 3 + Fr(4, 3) * (3 * S2 + (6 * delta - 3) * S1 + (3 * delta ** 2 - 3 * delta + 1) * S0))
    J = M * (Fr(2, 3) * delta ** 4 + Fr(2, 3) * (4 * S3 + (12 * delta - 6) * S2 + (12 * delta ** 2 - 12 * delta + 4) * S1
                                                 + (4 * delta ** 3 - 6 * delta ** 2 + 4 * delta - 1) * S0))
    return M, J, L


def kidx(x, delta):
    n = abs(x[0]) + abs(x[1]) - delta
    return max(0, ceil(n)) if n > 0 else 0


ok = True
npairs = 0
for _ in range(2000):
    delta = Fr(random.randint(1, 100), 100)
    x = (Fr(random.randint(-500, 500), 100), Fr(random.randint(-500, 500), 100))
    h1 = Fr(random.randint(-100, 100), 100)
    rem = int((1 - abs(h1)) * 100)
    h2 = Fr(random.choice([-1, 1]) * random.randint(0, rem), 100)
    assert abs(h1) + abs(h2) <= 1
    y = (x[0] + h1, x[1] + h2)
    ok &= kidx(y, delta) <= kidx(x, delta) + 1 and kidx(x, delta) <= kidx(y, delta) + 1
    npairs += 1
check(f"S8.b staircase privacy: shell index changes by at most 1 under any l1 shift ||h||_1<=1 ({npairs} random exact pairs) ⇒ p(x+h)>=b p(x)", ok)

PI_LO = Fr(314159265358979, 10 ** 14)
ok = True
det = []
for b in [Fr(1, 100), Fr(1, 10), Fr(1, 2), Fr(9, 10)]:
    lo, hi = bisect_root(lambda T: PhiL(T, b) - b * dL, Fr(0), Fr(2, 3))
    bb = mp.mpf(b.numerator) / b.denominator
    B0 = B0_new(bb)
    for delta in [Fr(1, 100), Fr(1, 10), Fr(1, 3), Fr(1), Fr(3)]:
        M, J, L = stair_moments(b, delta)
        okL = PhiL(L, b) >= b * dL                                        # L >= B_L exact
        okJ = (1 - b) * PI_LO * J * J / 2 + 2 * b * J >= 2 * b / 3           # J >= B_0 exact via rational lower bound on π
        okM = M <= 1 / (2 * b)                                             # density cap consistent with all-event privacy
        okK = True
        for k in [mp.mpf("0.5"), mp.mpf(1)]:
            d = mp.mpf(2) / 3 + 4 * k / 3
            Bk = mp_bisect(lambda T, k=k, d=d: (1 - bb) * G_k(T, k) + 2 * bb * T - bb * d, mp.mpf(0), d / 2)
            okK &= (mp.mpf(J.numerator) / J.denominator + k * mp.mpf(L.numerator) / L.denominator) >= Bk
        ok &= okL and okJ and okM and okK
        if delta in (Fr(1, 10), Fr(1)):
            det.append(f"b={b} δ={delta}: J={float(J):.5f} (B_0={mp.nstr(B0, 6)}, J/B_0={float(J) / float(B0):.2f}) "
                       f"L={float(L):.5f} (B_L≈{float(hi):.6f}, L/B_L={float(L) / float(hi):.2f})")
check("S8.c every staircase law (4 b x 5 δ) satisfies L>=B_L (exact), J>=B_0 (exact with π>3.14159265358979), "
      "M<=1/(2b), and J+κL>=B_κ for κ=1/2,1 (mp DIAGNOSTIC); no counterexample in this private family", ok, " ; ".join(det))

ok = True
det = []
for b in ["0.01", "0.1", "0.5", "0.9"]:
    bb = mp.mpf(b)
    eps = -mp.log(bb)
    J, L = 4 / eps ** 2, 2 / eps
    lo, hi, _olo, _ohi = BR[Fr(b)]
    okb = J >= B0_new(bb) and L >= mp.mpf(hi.numerator) / hi.denominator
    ok &= okb
    det.append(f"b={b}: Laplace J={mp.nstr(J, 6)} L={mp.nstr(L, 6)} vs B_0={mp.nstr(B0_new(bb), 6)}")
check("S8.d DIAGNOSTIC: product-Laplace law (density ∝ e^{-ε||x||_1}, ε=-ln b) satisfies J>=B_0 and L>=B_L", ok, " ; ".join(det))

# =====================================================================================
# S9. Summary and receipt
# =====================================================================================
npass = sum(1 for r in RESULTS if r["pass"])
nfail = len(RESULTS) - npass
t_end = time.time()
print("\n=== SUMMARY: %d checks, %d PASS, %d FAIL; elapsed %.2fs ===" % (len(RESULTS), npass, nfail, t_end - t_start))
print("clock_end_utc     ", datetime.datetime.now(datetime.timezone.utc).isoformat())
print("clock_end_local   ", datetime.datetime.now().astimezone().isoformat())
for r in RESULTS:
    if not r["pass"]:
        print("FAILED:", r["name"])
receipt = {
    "schema_version": 1,
    "kind": "REVIEWER_CONTROL_RECEIPT",
    "review_wave": "f118-privacy-occupied-cap-finite-dual",
    "script": os.path.basename(os.path.abspath(__file__)),
    "script_sha256": SELF_SHA,
    "input_path": INPUT, "input_sha256": IN_SHA, "input_bytes": IN_B, "input_LF": IN_LF,
    "manifest_path": MANIFEST, "manifest_sha256": MF_SHA, "manifest_bytes": MF_B,
    "python": sys.version.replace("\n", " "), "mpmath": mp.__version__, "platform": platform.platform(),
    "clock_start_utc": datetime.datetime.fromtimestamp(t_start, datetime.timezone.utc).isoformat(),
    "clock_end_utc": datetime.datetime.fromtimestamp(t_end, datetime.timezone.utc).isoformat(),
    "elapsed_seconds": round(t_end - t_start, 3),
    "n_checks": len(RESULTS), "n_pass": npass, "n_fail": nfail,
    "proof_grade_sections": ["S0", "S1", "S3 (exact parts)", "S4", "S5", "S7", "S8.a-S8.c (exact L, J parts)"],
    "diagnostic_only_sections": ["S2 (50-digit evaluation of closed forms)", "S2.f/S6.c (kink-split mp.quad)", "S3.i/S3.j (π numerics)",
                                 "S6.a/S6.b", "S8.c κ>0 part", "S8.d"],
    "author_code_executed": False,
    "checks": RESULTS,
}
with open(OUT_JSON, "w") as f:
    json.dump(receipt, f, indent=2)
    f.write("\n")
print("receipt_written", OUT_JSON)
sys.stdout.flush()
sys.stdout.f.close()
sys.exit(0 if nfail == 0 else 1)
