#!/usr/bin/env python3
"""reviewer-f119-controls-v1.py

Independent diagnostic controls for review f119 (privacy-uniform-joint-budget), written by the
f119 reviewer from the reviewer's OWN reconstruction. No author code is imported or executed.

All load-bearing checks are exact (fractions.Fraction). Section 10 uses mpmath at 60 digits and is a
high-precision NUMERIC control of the mixed-cost dual only (not a proof).

Setting (reconstructed, R^2): D = closed l1 unit diamond, |D| = 2. A law mu is b-private iff
mu(A+v) >= b mu(A) for every Borel A and every v in D. J = E|X|_2^2, L = E|X|_1.
Shell law S(a,b): density proportional to b^{k(x)}, k(x) = ceil((|x|_1 - a)_+).
"""
import sys, os, hashlib, datetime, platform
from fractions import Fraction as Fr

OUT = []
FAILS = []
def out(s=""):
    OUT.append(str(s)); print(s)
def check(name, cond, detail=""):
    st = "PASS" if cond else "FAIL"
    if not cond: FAILS.append(name)
    out(f"[{st}] {name}" + (f" :: {detail}" if detail else ""))
def fl(x, n=12):
    return f"{float(x):.{n}g}"

T0 = datetime.datetime.now(datetime.timezone.utc).isoformat()
SRC = os.path.abspath(__file__)
with open(SRC, "rb") as fh:
    SRC_SHA = hashlib.sha256(fh.read()).hexdigest()
out(f"# reviewer-f119-controls-v1.py run")
out(f"start_utc={T0}")
out(f"source={SRC}")
out(f"source_sha256={SRC_SHA}")
out(f"python={platform.python_version()} platform={platform.platform()}")

# ===================================================================================
# 1. F(r) exact rational samples and continuity at 1/6
# ===================================================================================
out("\n## 1. F(r) exact samples")
def F(r):
    r = Fr(r); assert r > 0
    return Fr(27, 4) * r * (1 - 2 * r) ** 2 if r < Fr(1, 6) else Fr(1, 2)
samples = {Fr(1, 24): Fr(121, 512), Fr(1, 12): Fr(25, 64), Fr(1, 9): Fr(49, 108), Fr(1, 6): Fr(1, 2)}
for r, want in samples.items():
    check(f"F({r}) == {want}", F(r) == want, f"F={F(r)}")
left_limit = Fr(27, 4) * Fr(1, 6) * (1 - Fr(1, 3)) ** 2
check("F continuous at 1/6: (27/4)(1/6)(2/3)^2 == 1/2", left_limit == Fr(1, 2), f"value={left_limit}")

# ===================================================================================
# 2. kappa substitution identities (rational-function identities, checked at > degree points)
# ===================================================================================
out("\n## 2. kappa = 2r/(1-6r) substitution identities")
# After clearing denominators both identities are polynomial identities in r of degree <= 6;
# agreement at 40 distinct rationals therefore proves them. ell-homogeneity checked at 3 values of ell.
pts = [Fr(i, 241) for i in range(1, 41)]  # 1/241 .. 40/241 < 1/6
ok1 = ok2 = okopt = True
for r in pts:
    kap = 2 * r / (1 - 6 * r)
    for ell in (Fr(1), Fr(1, 7), Fr(3, 1000)):
        j = r * ell
        H = j + kap * ell
        ok1 &= (H / (1 + 2 * kap) == 3 * j)
        ok2 &= (H ** 3 / (kap ** 2 * (1 + 2 * kap)) == ell ** 3 * F(r))
    # kappa* is a critical point / minimiser of g(k) = (r+k)^3/(k^2(1+2k)) (not load-bearing)
    g = lambda k: (r + k) ** 3 / (k ** 2 * (1 + 2 * k))
    okopt &= (g(kap) == F(r)) and all(g(kap * (1 + d)) >= F(r) for d in (Fr(-1, 2), Fr(-1, 10), Fr(1, 10), Fr(1, 2), Fr(5)))
check("H/(1+2kappa) == 3j at 40x3 rational points", ok1)
check("H^3/(kappa^2(1+2kappa)) == ell^3 F(r) at 40x3 rational points", ok2)
check("g(kappa*) == F(r) and g >= F(r) at perturbed kappa (consistency, not load-bearing)", okopt)
# condition H < (1+2kappa)/3  <=>  j < 1/9
r = Fr(1, 10); kap = 2 * r / (1 - 6 * r)
for j in (Fr(1, 9) - Fr(1, 10 ** 9), Fr(1, 9), Fr(1, 9) + Fr(1, 10 ** 9)):
    ell = j / r; H = j + kap * ell
    check(f"j={j}: (H < (1+2k)/3) == (j < 1/9)", (H < (1 + 2 * kap) / 3) == (j < Fr(1, 9)))

# ===================================================================================
# 3. Exact geometric moment sums  S_n(a,b) = sum_k b^k (a+k)^n  via Eulerian polynomials
# ===================================================================================
out("\n## 3. Geometric moment sums: Eulerian polynomial recurrence + partial-sum interval cross-check")
def padd(p, q):
    n = max(len(p), len(q)); return [(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0) for i in range(n)]
def pmul(p, q):
    r_ = [Fr(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for k, y in enumerate(q):
            r_[i + k] += x * y
    return r_
def pscale(p, c): return [c * x for x in p]
def pder(p): return [i * p[i] for i in range(1, len(p))] or [Fr(0)]
def pstrip(p):
    while len(p) > 1 and p[-1] == 0: p = p[:-1]
    return p
# Li_{-i}(b) = N_i(b)/(1-b)^{i+1};  Li_{-(i+1)} = b d/db Li_{-i}  =>  N_{i+1} = b[(1-b) N_i' + (i+1) N_i]
N = [[Fr(1)]]
for i in range(4):
    Ni = N[i]
    Nn = pmul([Fr(0), Fr(1)], padd(pmul([Fr(1), Fr(-1)], pder(Ni)), pscale(Ni, i + 1)))
    N.append(pstrip(Nn))
claimed = {1: [0, 1], 2: [0, 1, 1], 3: [0, 1, 4, 1], 4: [0, 1, 11, 11, 1]}
for i in range(1, 5):
    check(f"Eulerian numerator N_{i} == {claimed[i]}", N[i] == [Fr(c) for c in claimed[i]], f"derived={[int(c) for c in N[i]]}")
def Li(i, b):  # sum_{k>=0} k^i b^k, exact, 0<b<1
    num = sum(c * b ** e for e, c in enumerate(N[i]))
    return num / (1 - b) ** (i + 1)
def binom(n, k):
    from math import comb; return comb(n, k)
def S(n, a, b):  # sum_{k>=0} b^k (a+k)^n exact
    return sum(binom(n, i) * a ** (n - i) * Li(i, b) for i in range(n + 1))
# Independent tail bound (b <= 1/2, n <= 4, a+K+1 >= 1):  tail_K <= 3000 b^{K+1} (a+K+1)^4,
# using (1+m)^4 <= 1000 (4/3)^m for all m>=0 (checked m<=100; ratio decreasing for m>=13).
okc = all((1 + m) ** 4 <= 1000 * Fr(4, 3) ** m for m in range(0, 101))
mono = all(((2 + m) ** 4 * Fr(3, 4) ** (m + 1)) <= ((1 + m) ** 4 * Fr(3, 4) ** m) for m in range(13, 101))
check("(1+m)^4 <= 1000 (4/3)^m for m=0..100 and ratio decreasing for m>=13", okc and mono)
def partial_interval(n, a, b, K=120):
    P = sum(b ** k * (a + k) ** n for k in range(K + 1))
    tail = 3000 * b ** (K + 1) * (a + K + 1) ** 4
    return P, P + tail
okS = True
for (a, b) in [(Fr(1, 1000), Fr(1, 10 ** 9)), (Fr(1, 100), Fr(1, 2 * 10 ** 6)), (Fr(1, 10), Fr(1, 2000)), (Fr(1, 2), Fr(1, 16)), (Fr(1), Fr(1, 2)), (Fr(3, 2), Fr(1, 3))]:
    for n in (2, 3, 4):
        lo, hi = partial_interval(n, a, b)
        v = S(n, a, b)
        okS &= (lo <= v <= hi)
check("closed-form S_n within exact partial-sum interval [P_K, P_K+tail] at 6 (a,b) x n=2,3,4", okS)
# Direct shell-area definition of Z vs Abel-summed closed form 2(1-b) S_2
okZ = True
for (a, b) in [(Fr(1, 100), Fr(1, 2 * 10 ** 6)), (Fr(1, 2), Fr(1, 16)), (Fr(1), Fr(1, 2))]:
    K = 120
    direct = 2 * a ** 2 + sum(b ** k * 2 * ((a + k) ** 2 - (a + k - 1) ** 2) for k in range(1, K + 1))
    closed = 2 * (1 - b) * S(2, a, b)
    # direct partial sum <= closed <= direct + tail of the direct series (<= 2*tail bound on sum b^k(a+k)^2 * 2)
    tail = 2 * 3000 * b ** (K + 1) * (a + K + 1) ** 4
    okZ &= (direct <= closed <= direct + tail)
check("Z: direct shell-area partial sums bracket 2(1-b)S_2 (Abel summation)", okZ)

# ===================================================================================
# 4. Shell law exact moments; pointwise privacy of the shell index (finite rational sample)
# ===================================================================================
out("\n## 4. Shell law S(a,b): exact (J,L); shell-index Lipschitz check")
def shell_JL(a, b):
    a, b = Fr(a), Fr(b)
    S2, S3, S4 = S(2, a, b), S(3, a, b), S(4, a, b)
    return Fr(1, 3) * S4 / S2, Fr(2, 3) * S3 / S2   # (J, L)
from math import ceil as _ceil
def kidx(x, a, width=Fr(1)):
    n1 = abs(x[0]) + abs(x[1])
    t = (n1 - a) / width
    return 0 if t <= 0 else _ceil(t)
grid = [Fr(i, 7) for i in range(-21, 22)]
shifts = [(Fr(i, 5), Fr(k, 5)) for i in range(-5, 6) for k in range(-5, 6) if abs(Fr(i, 5)) + abs(Fr(k, 5)) <= 1]
def lipschitz_ok(a, width):
    for x0 in grid:
        for x1 in grid:
            kx = kidx((x0, x1), a, width)
            for v in shifts:
                kv = kidx((x0 + v[0], x1 + v[1]), a, width)
                if abs(kx - kv) > 1: return False
    return True
check("width-1 shell index: |k(x+v)-k(x)| <= 1 on 43^2 points x 61 shifts (a=3/10)", lipschitz_ok(Fr(3, 10), Fr(1)))
check("NEGATIVE CONTROL: width-1/2 shell index violates |k(x+v)-k(x)|<=1 (expected violation found)", not lipschitz_ok(Fr(3, 10), Fr(1, 2)))

# ===================================================================================
# 5. Finite necessary inequalities (2),(3) on ACTUAL private shell laws and mixtures
# ===================================================================================
out("\n## 5. Finite inequalities (2),(3) tested on genuine b-private laws at their own exact (J,L)")
def bound2(j, ell):  # (2): valid iff r<1/6 and j<1/9
    r = j / ell
    if r < Fr(1, 6) and j < Fr(1, 9): return ell ** 3 * F(r) / (1 - 9 * j)
    return None
def bound3(ell):     # (3): valid iff ell<2/3 (for any r)
    return ell ** 3 / (2 - 3 * ell) if ell < Fr(2, 3) else None
A_GRID = [Fr(1, 1000), Fr(1, 100), Fr(1, 20), Fr(1, 10), Fr(1, 4), Fr(1, 2), Fr(1), Fr(2)]
B_GRID = [Fr(1, 10 ** 9), Fr(1, 10 ** 6), Fr(1, 10 ** 4), Fr(1, 1000), Fr(1, 100), Fr(1, 20), Fr(1, 10), Fr(1, 4), Fr(1, 2), Fr(9, 10)]
n2 = n3 = 0; viol = []
laws = []
for a in A_GRID:
    for b in B_GRID:
        J, L = shell_JL(a, b); laws.append((a, b, J, L))
        u2 = bound2(J, L)
        if u2 is not None:
            n2 += 1
            if not (b <= u2): viol.append(("(2)", a, b, J, L, u2))
        u3 = bound3(L)
        if u3 is not None:
            n3 += 1
            if not (b <= u3): viol.append(("(3)", a, b, J, L, u3))
check(f"(2) holds on all applicable shell laws (applicable={n2} of {len(laws)})", not any(v[0] == "(2)" for v in viol))
check(f"(3) holds on all applicable shell laws (applicable={n3} of {len(laws)})", not any(v[0] == "(3)" for v in viol))
for v in viol: out("   VIOLATION " + str(v))
# mixtures (same b, different a): b-private; (J,L) linear in weights
nm2 = nm3 = 0; violm = []
for b in B_GRID:
    sub = [(a, J, L) for (a, bb, J, L) in laws if bb == b]
    for i in range(len(sub)):
        for k in range(i + 1, len(sub)):
            for w in (Fr(1, 4), Fr(1, 2), Fr(3, 4)):
                Jm = w * sub[i][1] + (1 - w) * sub[k][1]; Lm = w * sub[i][2] + (1 - w) * sub[k][2]
                u2 = bound2(Jm, Lm); u3 = bound3(Lm)
                if u2 is not None:
                    nm2 += 1
                    if not (b <= u2): violm.append(("(2)", b, sub[i][0], sub[k][0], w))
                if u3 is not None:
                    nm3 += 1
                    if not (b <= u3): violm.append(("(3)", b, sub[i][0], sub[k][0], w))
check(f"(2) holds on applicable two-shell mixtures (applicable={nm2})", not any(v[0] == "(2)" for v in violm))
check(f"(3) holds on applicable two-shell mixtures (applicable={nm3})", not any(v[0] == "(3)" for v in violm))
for v in violm: out("   VIOLATION " + str(v))
# how tight is (2) on the k=0.. shell family far from the asymptotic regime? report min slack ratio
ratios = []
for (a, b, J, L) in laws:
    u2 = bound2(J, L)
    if u2 is not None: ratios.append((float(b / u2), str(a), str(b)))
ratios.sort(reverse=True)
out("   top b/bound2 ratios on the grid (must be <=1): " + "; ".join(f"{r_:.6g}@(a={a_},b={b_})" for r_, a_, b_ in ratios[:4]))

# ===================================================================================
# 6. Explicit uniform construction with K = 7 on exact adversarial sequences
# ===================================================================================
out("\n## 6. Construction (9)/(r>=1/6) with explicit K=7: exact feasibility and two-sided ratio")
K_CONST = Fr(7)
def construct(j, ell):
    j, ell = Fr(j), Fr(ell); r = j / ell
    eta = ell + ell ** 2 / j
    gam = 1 - K_CONST * eta
    assert gam > 0, "gamma<=0: outside explicit regime"
    if r < Fr(1, 6):
        a = gam * Fr(3, 2) * (1 - 2 * r) * ell; b = gam ** 3 * ell ** 3 * F(r)
    else:
        a = gam * ell; b = a ** 3 / 2
    return a, b, gam, eta, r
def upper(j, ell):
    r = j / ell
    return bound2(j, ell) if r < Fr(1, 6) else bound3(ell)
def lemmaE_ok(a, b, J, L):
    # explicit Lemma E (reviewer): a<=1/100, b<=a^3/2
    if not (a <= Fr(1, 100) and 0 < b <= a ** 3 / 2): return False
    Lc = Fr(2, 3) * (a + b / a ** 2); Jc = b / (3 * a ** 2)
    okL = (Lc * (1 - Fr(52, 100) * a) <= L <= Lc * (1 + Fr(304, 100) * a))
    okJ = (Jc * (1 + a ** 4 / b) / (1 + Fr(52, 100) * a) <= J <= Jc * (1 + a ** 4 / b + Fr(412, 100) * a))
    return okL and okJ
def run_case(tag, j, ell):
    a, b, gam, eta, r = construct(j, ell)
    J, L = shell_JL(a, b)
    feas = (J <= j) and (L <= ell)
    up = upper(j, ell)
    ratio = b / up                      # lower/upper, must be <= 1 and -> 1
    lowgap = 1 - b / (ell ** 3 * F(r))  # = 1 - gamma^3 <= 21 eta
    upgap = up / (ell ** 3 * F(r)) - 1  # <= 2 ell
    e_ok = lemmaE_ok(a, b, J, L)
    allok = feas and e_ok and (ratio <= 1) and (lowgap <= 21 * eta) and (upgap <= 2 * ell) and (b <= a ** 3 / 2)
    check(f"{tag} r={fl(r,6)} ell={fl(ell,4)} eta={fl(eta,4)}", allok,
          f"J/j={fl(J/j,10)} L/ell={fl(L/ell,10)} b/upper={fl(ratio,10)} lowgap={fl(lowgap,6)} (<=21eta={fl(21*eta,4)}) upgap={fl(upgap,6)} (<=2ell={fl(2*ell,4)}) LemmaE={e_ok}")
    return ratio, eta
# Sequence A: r -> 0 slowly (ell=10^-2m, j=10^-3m, so ell^2/j = 10^-m)
out(" Sequence A (r->0, ell^2/j = 10^-m):")
for m in range(2, 7):
    run_case("A", Fr(1, 10 ** (3 * m)), Fr(1, 10 ** (2 * m)))
# very small r with ell^2/j = 1/10 (near regime edge)
run_case("A-edge", Fr(1, 10 ** 19), Fr(1, 10 ** 10))
# Sequence B/C: r -> 1/6 from below / above with ell = 10^-m
out(" Sequence B/C (r -> 1/6 from below/above):")
for m in range(3, 8):
    ell = Fr(1, 10 ** m)
    run_case("B", (Fr(1, 6) - Fr(1, 10 ** m)) * ell, ell)
    run_case("C", (Fr(1, 6) + Fr(1, 10 ** m)) * ell, ell)
run_case("B=1/6 exactly", Fr(1, 6) * Fr(1, 10 ** 4), Fr(1, 10 ** 4))
# Sequence D: oscillating r with ell -> 0
out(" Sequence D (oscillating r, including r>>1):")
rat_prev = None
for m in range(3, 6):
    ell = Fr(1, 10 ** (2 * m))
    for r in (Fr(1, 10 ** m), Fr(1, 6) - Fr(1, 10 ** m), Fr(1, 6), Fr(1, 6) + Fr(1, 10 ** m), Fr(1000), Fr(1, 10 ** m)):
        run_case("D", r * ell, ell)
# rate check: along A, (1 - ratio)/eta bounded
out(" Rate check along A: (1-b/upper)/eta")
for m in range(2, 7):
    pass
    a, b, gam, eta, r = construct(Fr(1, 10 ** (3 * m)), Fr(1, 10 ** (2 * m)))
    up = upper(Fr(1, 10 ** (3 * m)), Fr(1, 10 ** (2 * m)))
    out(f"   m={m}: eta={fl(eta,4)}  (1-b/upper)/eta={fl((1-b/up)/eta,6)}")

# ===================================================================================
# 7. Relative error of J as b/a^3 -> 0 at fixed a (the a^4/b term is real and exactly as stated)
# ===================================================================================
out("\n## 7. J relative error vs b/a^3 -> 0 at fixed a = 1/100")
a = Fr(1, 100)
okE = True
for b in (a ** 3 / 2, a ** 3 / 10, a ** 4, a ** 5, a ** 6, a ** 8):
    J, L = shell_JL(a, b)
    rel = 3 * a ** 2 * J / b - 1
    rel_after = (3 * a ** 2 * J / b) / (1 + a ** 4 / b) - 1   # should be O(a) uniformly
    okE &= (Fr(-52, 100) * a <= rel_after <= Fr(412, 100) * a)
    out(f"   b/a^3={fl(b/a**3,4)}: 3a^2J/b-1={fl(rel,6)}  a^4/b={fl(a**4/b,6)}  residual after removing a^4/b={fl(rel_after,6)} (|.|<=4.12a={fl(Fr(412,100)*a,4)})")
check("J = ((b+a^4)/(3a^2))(1+O(a)) with |O(a)| in [-0.52a, 4.12a] for all sampled b/a^3 in (0,1/2]", okE)

# ===================================================================================
# 8. Hypothesis boundary: j = ell^2 (eta >= 1): gamma=1 construction is infeasible (not a defect)
# ===================================================================================
out("\n## 8. Scope boundary: ell^2/j not small (j = ell^2) -> raw construction infeasible")
for m in (3, 4, 5):
    ell = Fr(1, 10 ** m); j = ell ** 2; r = j / ell
    a = Fr(3, 2) * (1 - 2 * r) * ell; b = ell ** 3 * F(r)
    J, L = shell_JL(a, b)
    out(f"   ell={fl(ell,3)} j=ell^2: gamma=1 shell has J/j={fl(J/j,8)} (>1 => infeasible), L/ell={fl(L/ell,8)}; (2) at its own (J,L): b<=bound? {b <= bound2(J, L)}")
    check(f"j=ell^2 (ell={fl(ell,3)}): raw construction J>j (theorem makes no claim here)", J > j)
    check(f"j=ell^2 (ell={fl(ell,3)}): finite (2) still holds for that genuine law at its own (J,L)", b <= bound2(J, L))

# ===================================================================================
# 9. Negative controls on the bound checker (the inequalities have teeth)
# ===================================================================================
out("\n## 9. Negative controls")
# (i) a 2% tighter 'bound' is refuted by an actual feasible private law at small eta
j, ell = Fr(1, 10 ** 15), Fr(1, 10 ** 10)
a, b, gam, eta, r = construct(j, ell); J, L = shell_JL(a, b)
fake = Fr(98, 100) * ell ** 3 * F(r) / (1 - 9 * j)
check("NEGATIVE: 0.98 x bound (2) is violated by a genuine feasible law (eta~1e-5)", (J <= j and L <= ell) and not (b <= fake), f"b/fake={fl(b/fake,8)}")
# (ii) non-private uniform law on aD with pretended b=a^3 is rejected by (2)
a = Fr(1, 100); Ju, Lu = a ** 2 / 3, Fr(2, 3) * a
check("NEGATIVE: uniform-on-aD (not private) with pretended b=a^3 violates (2)", not (a ** 3 <= bound2(Ju, Lu)), f"bound2={fl(bound2(Ju,Lu),6)} pretended={fl(a**3,6)}")
# (iii) a wrong Eulerian numerator breaks the partial-sum interval cross-check
def Li_wrong(i, b):
    wrong = {0: [1], 1: [0, 1], 2: [0, 1, 1], 3: [0, 1, 4, 1], 4: [0, 1, 10, 11, 1]}  # 10 instead of 11
    return sum(Fr(c) * b ** e for e, c in enumerate(wrong[i])) / (1 - b) ** (i + 1)
a, b = Fr(1, 2), Fr(1, 16)
S4w = sum(binom(4, i) * a ** (4 - i) * Li_wrong(i, b) for i in range(5))
lo, hi = partial_interval(4, a, b)
check("NEGATIVE: mutated Eulerian polynomial (10 for 11) fails partial-sum interval", not (lo <= S4w <= hi))

# ===================================================================================
# 10. High-precision numeric control of the mixed-cost dual (6): b(d-2H) <= G_kappa(H), H=J+kappa L
# ===================================================================================
out("\n## 10. mpmath (60 dps) control of dual (6) with EXACT G_kappa (first-quadrant disc region)")
try:
    import mpmath as mp
    mp.mp.dps = 60
    def G_mixed(T, kap):
        T = mp.mpf(T); kap = mp.mpf(kap)
        c = kap / 2; R2 = T + kap ** 2 / 2
        umax = mp.sqrt(R2 - c * c)
        if umax <= c: return mp.mpf(0)
        def inner(u):
            vmax = mp.sqrt(R2 - u * u)
            return (R2 - u * u) * (vmax - c) - (vmax ** 3 - c ** 3) / 3
        return 4 * mp.quad(inner, [c, umax])
    # sanity: kappa->0 gives pi T^2/2 ; T/kappa^2 -> 0 gives 2T^3/(3 kappa^2) ; containment always
    T = mp.mpf(1) / 3
    g0 = G_mixed(T, mp.mpf(10) ** -25); ref0 = mp.pi * T ** 2 / 2
    check("G_kappa -> pi T^2/2 as kappa->0 (rel err < 1e-20)", abs(g0 / ref0 - 1) < mp.mpf(10) ** -20, f"rel={mp.nstr(g0/ref0-1,5)}")
    gl = G_mixed(mp.mpf(10) ** -8, mp.mpf(1)); refl = 2 * mp.mpf(10) ** -24 / 3
    check("G_kappa -> 2T^3/(3kappa^2) as T/kappa^2->0 (rel err < 1e-6)", abs(gl / refl - 1) < mp.mpf(10) ** -6, f"rel={mp.nstr(gl/refl-1,5)}")
    okc = all(G_mixed(Tt, kk) <= 2 * mp.mpf(Tt) ** 3 / (3 * mp.mpf(kk) ** 2) for Tt in (mp.mpf(1) / 1000, mp.mpf(1) / 10, 1) for kk in (mp.mpf(1) / 100, 1, 10))
    check("containment G_kappa(T) <= 2T^3/(3kappa^2) at 9 (T,kappa)", okc)
    def mpf(x): return mp.mpf(x.numerator) / mp.mpf(x.denominator)
    # dual consequence on genuine laws: b(d-2H) <= G(H) and H >= B (B root of G(B)+2bB=bd)
    okd = True; rows = []
    testset = [(Fr(1, 100), Fr(1, 2 * 10 ** 6)), (Fr(1, 10), Fr(1, 2000)), (Fr(1, 4), Fr(1, 100)), (Fr(1, 2), Fr(1, 16)), (Fr(1), Fr(1, 2))]
    for (a, b) in testset:
        J, L = shell_JL(a, b); r = J / L
        kaps = [Fr(1, 10), Fr(1), Fr(10)] + ([2 * r / (1 - 6 * r)] if r < Fr(1, 6) else [])
        for kap in kaps:
            H = J + kap * L; d = (2 + 4 * kap) / 3
            lhs = mpf(b) * (mpf(d) - 2 * mpf(H)); G = G_mixed(mpf(H), mpf(kap))
            # root B
            f = lambda B: G_mixed(B, mpf(kap)) + 2 * mpf(b) * B - mpf(b) * mpf(d)
            lo_, hi_ = mp.mpf(10) ** -30, mpf(d) / 2
            for _ in range(200):
                mid = (lo_ + hi_) / 2
                if f(mid) < 0: lo_ = mid
                else: hi_ = mid
            B = hi_
            ok = (lhs <= G * (1 + mp.mpf(10) ** -40) + mp.mpf(10) ** -50) and (mpf(H) >= B * (1 - mp.mpf(10) ** -40))
            okd &= ok
            rows.append(f"   a={a} b={b} kappa={fl(kap,5)}: b(d-2H)={mp.nstr(lhs,8)} G(H)={mp.nstr(G,8)} ratio={mp.nstr(G/lhs if lhs>0 else mp.inf,8)} H={mp.nstr(mpf(H),8)} B={mp.nstr(B,8)} ok={ok}")
    for rw in rows: out(rw)
    check("dual (6) consequences b(d-2H)<=G_kappa(H) and J+kappa L>=B on 5 shell laws x kappas (60 dps)", okd)
    # sharpness along the construction: G(H)/(b(d-2H)) -> 1 as eta -> 0  (kappa = kappa*(r))
    out("   sharpness along construction (r=1/50, K=7): G(H)/(b(d-2H)) should -> 1 like 1+O(eta)")
    for m in (3, 4, 5, 6):
        ell = Fr(1, 10 ** m); j = Fr(1, 50) * ell
        a, b, gam, eta, r = construct(j, ell); J, L = shell_JL(a, b)
        kap = 2 * r / (1 - 6 * r); H = J + kap * L; d = (2 + 4 * kap) / 3
        lhs = mpf(b) * (mpf(d) - 2 * mpf(H)); G = G_mixed(mpf(H), mpf(kap))
        out(f"   ell={fl(ell,3)} eta={fl(eta,4)}: G/(b(d-2H)) - 1 = {mp.nstr(G/lhs-1,6)}  ((G/lhs-1)/eta={mp.nstr((G/lhs-1)/mpf(eta),5)})")
except Exception as e:  # mpmath control is optional; failure here is reported, not hidden
    check("mpmath dual control executed", False, repr(e))

# ===================================================================================
out("\n## Summary")
T1 = datetime.datetime.now(datetime.timezone.utc).isoformat()
out(f"end_utc={T1}")
out(f"fail_count={len(FAILS)}")
for f_ in FAILS: out(f"  FAILED: {f_}")
out("VERDICT_OF_CONTROLS=" + ("ALL_PASS" if not FAILS else "FAILURES_PRESENT"))
OUTPATH = os.path.join(os.path.dirname(SRC), "reviewer-f119-controls-output-v1.txt")
with open(OUTPATH, "w") as fh:
    fh.write("\n".join(OUT) + "\n")
print(f"output_written={OUTPATH}")
