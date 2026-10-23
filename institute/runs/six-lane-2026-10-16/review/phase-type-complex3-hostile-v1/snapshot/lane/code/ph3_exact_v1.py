"""Exact symbolic identities behind proof/ph3-theorem-v1.md (sympy; finite set of exact checks, no numerics).

argv[1] = run directory (created by run_v1.sh). Writes exact.json (exclusive create).
Each check is an exact polynomial / rational-function identity; a FAIL is reported, never patched.
"""
import sys
import json
import time
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402
import sympy as sp  # noqa: E402

RUN = sys.argv[1]
res = {}
x, u, z, sig = sp.symbols("x u z sigma")
beta, A, C, W, ms, r, tau = sp.symbols("beta A C W m_s r tau", positive=True)
I = sp.I


def record(name, ok, **info):
    res[name] = dict(ok=bool(ok), **info)
    print(name, "PASS" if ok else "FAIL", info if info else "")


def is_zero(e):
    return sp.simplify(sp.cancel(sp.together(sp.expand(e)))) == 0


t0 = time.time()

# E1: cycle determinant and first resolvent row, general weights, n = 3..7
for n in range(3, 8):
    m = sp.symbols(f"m1:{n + 1}")
    w = sp.symbols(f"w1:{n + 1}")
    M = sp.zeros(n, n)
    for i in range(n):
        M[i, i] = m[i]
    for i in range(n - 1):
        M[i, i + 1] = w[i]
    M[n - 1, 0] = w[n - 1]
    Ax = x * sp.eye(n) - M
    q_claim = sp.prod([x - mi for mi in m]) - sp.prod(w)
    det_ok = sp.expand(Ax.det(method="berkowitz") - q_claim) == 0
    y = sp.Matrix([[sp.prod(w[:j]) * sp.prod([x - m[k] for k in range(j + 1, n)]) for j in range(n)]])
    row = y * Ax
    row_ok = all(sp.expand(row[0, j] - (q_claim if j == 0 else 0)) == 0 for j in range(n))
    record(f"E1_cycle_det_and_resolvent_row_n{n}", det_ok and row_ok, det=det_ok, row=row_ok)

# E2: identities (I1), (I2) with sin/cos of theta, phi as independent symbols (no Pythagorean relation needed)
S1, C1, sph, cph = sp.symbols("S1 C1 sphi cphi", nonzero=True)
bt = sph / cph
mt = -bt * C1 / S1
I1 = (1 - mt) - (S1 * cph + C1 * sph) / (cph * S1)
I2 = (I * bt - mt) - bt * (C1 + I * S1) / S1
record("E2_I1_one_minus_m", is_zero(I1))
record("E2_I2_ibeta_minus_m", is_zero(I2))

# E3: q(i beta) formula for n = 3, 4, 5 (independent angle symbols; e^{i sum} = prod(C_k + i S_k))
for n in (3, 4, 5):
    Ss = sp.symbols(f"S1:{n + 1}", nonzero=True)
    Cs = sp.symbols(f"C1:{n + 1}")
    mm = [-bt * Cs[k] / Ss[k] for k in range(n)]
    lhs = sp.prod([I * bt - mk for mk in mm]) - sp.prod([1 - mk for mk in mm])
    rhs = (sph ** n * sp.prod([Cs[k] + I * Ss[k] for k in range(n)])
           - sp.prod([Ss[k] * cph + Cs[k] * sph for k in range(n)])) / (cph ** n * sp.prod(Ss))
    record(f"E3_q_at_ibeta_formula_n{n}", is_zero(lhs - rhs))

# E4: m_*, rho identities
mstar = (1 - beta ** 2) / 2
rho = (1 + beta ** 2) / 2
record("E4_one_minus_mstar_eq_rho", is_zero(1 - mstar - rho))
record("E4_mstar2_plus_beta2_eq_rho2", is_zero(mstar ** 2 + beta ** 2 - rho ** 2))
p_ = sp.symbols("p_", positive=True)
record("E4_mstar_eq_minus_beta_cot_psi",
       sp.simplify(-sp.tan(p_) * sp.cot(sp.pi - 2 * p_) - (1 - sp.tan(p_) ** 2) / 2) == 0)
record("E4_cos_2atan", sp.simplify(sp.cos(2 * sp.atan(beta)) - (1 - beta ** 2) / (1 + beta ** 2)) == 0)
record("E4_D_at_mstar", is_zero((mstar - 1) * (mstar ** 2 + beta ** 2) + rho ** 3))

# E5: generating function identity h(m_* + rho u) = rho^-3 / ((1-u)(1 - 2 cos(psi) u + u^2)), cos psi = -m_*/rho
cospsi = -(1 - beta ** 2) / (1 + beta ** 2)
hx = 1 / ((1 - x) * (x ** 2 + beta ** 2))
gen = hx.subs(x, mstar + rho * u) * rho ** 3 * (1 - u) * (1 - 2 * cospsi * u + u ** 2) - 1
record("E5_generating_function", is_zero(gen))
record("E5_cospsi_eq_cos_pi_minus_2atan", sp.simplify(sp.cos(sp.pi - 2 * sp.atan(beta)) - cospsi) == 0)

# E6: Chebyshev partial sums. (a) series coefficients vs sum of U_j(Cv); (b) U_j(cos psi) sin psi = sin((j+1)psi);
# (c) telescoped closed form 2 sin(psi/2) sum_{j<=k} sin((j+1)psi) = cos(psi/2) - cos((k+3/2)psi)
Cv, psi = sp.symbols("Cv psi")
K_MAX = 16
ser = sp.series(1 / ((1 - u) * (1 - 2 * Cv * u + u ** 2)), u, 0, K_MAX + 1).removeO()
ok_a = all(sp.expand(ser.coeff(u, k) - sum(sp.chebyshevu(j, Cv) for j in range(k + 1))) == 0 for k in range(K_MAX + 1))
record("E6a_series_coeff_eq_partial_sum_U", ok_a, k_max=K_MAX)
ok_b = all(sp.simplify(sp.expand((sp.chebyshevu(j, sp.cos(psi)) * sp.sin(psi) - sp.sin((j + 1) * psi)).rewrite(sp.exp))) == 0
           for j in range(K_MAX + 1))
record("E6b_U_j_cos_psi", ok_b, j_max=K_MAX)
ok_c = all(sp.simplify(sp.expand((2 * sp.sin(psi / 2) * sum(sp.sin((j + 1) * psi) for j in range(k + 1))
                                   - (sp.cos(psi / 2) - sp.cos((2 * k + 3) * psi / 2))).rewrite(sp.exp))) == 0
           for k in range(K_MAX + 1))
record("E6c_telescoped_closed_form", ok_c, k_max=K_MAX)

# E7: jet identity, generic m_* (free symbol ms) and W: if z^{n-3} | D(ms+z) P(z) + W with P monic deg n-3,
# then p_k = W * [z^k](-1/D(ms+z)) for k <= n-4.
Dz = sp.expand((ms + z - 1) * ((ms + z) ** 2 + beta ** 2))
for n in range(4, 11):
    d = n - 3
    pk = sp.symbols(f"p0:{d}")
    P = z ** d + sum(pk[k] * z ** k for k in range(d))
    expr = sp.expand(Dz * P + W)
    eqs = [expr.coeff(z, k) for k in range(d)]
    sol = sp.solve(eqs, pk, dict=True)
    hser = sp.series(-1 / Dz, z, 0, d).removeO()
    ok = len(sol) == 1 and all(is_zero(sol[0][pk[k]] - W * hser.coeff(z, k)) for k in range(d))
    record(f"E7_jet_identity_n{n}", ok)

# E8: n = 4, construction family: diag (m1, m2, m2, m_*), W = prod(1 - m_i), P = z + W/rho^3.
# E := q - D P has degree <= 3 and vanishes identically at x = 1 and x = m_*; so q = D P iff q(+-i beta) = 0.
m1, m2 = sp.symbols("m1 m2")
W4 = (1 - m1) * (1 - m2) ** 2 * (1 - mstar)
q4 = (x - m1) * (x - m2) ** 2 * (x - mstar) - W4
D = (x - 1) * (x ** 2 + beta ** 2)
P4 = (x - mstar) + W4 / rho ** 3
E = sp.expand(q4 - D * P4)
ok8 = (sp.degree(E, x) <= 3 and is_zero(E.subs(x, 1)) and is_zero(E.subs(x, mstar))
       and is_zero(E.subs(x, I * beta) - q4.subs(x, I * beta)))
record("E8_n4_construction_only_spectral_conditions", ok8, deg_E=int(sp.degree(E, x)))


def ph_normalize_symbolic(Mmat, tvec, n, Aval):
    """v = (-T0)^{-1} t with T0 = M - A I; returns v, transform e1 (sigma I - T0)^{-1} t."""
    T0 = Mmat - Aval * sp.eye(n)
    v = (-T0).LUsolve(tvec)
    tr = (sig * sp.eye(n) - T0).LUsolve(tvec)[0]
    return [sp.factor(sp.cancel(vi)) for vi in v], sp.factor(sp.cancel(tr))


def coeffs_positive_in_C(expr):
    """expr rational in C; True if numerator and denominator polynomials in C have only positive coefficients
    (then expr > 0 for every C > 0)."""
    num, den = sp.fraction(sp.cancel(sp.together(expr)))
    pn, pd = sp.Poly(sp.expand(num), C), sp.Poly(sp.expand(den), C)
    cn, cd = pn.coeffs(), pd.coeffs()
    s = 1 if cn[0] > 0 else -1
    return all(s * c > 0 for c in cn) and all(s * c > 0 for c in cd) if all(c.is_number for c in cn + cd) else None


# E9: uniform cycle at the upper endpoint beta = cot(pi/n), tau = tan(pi/n): i beta - m_* = rho e^{2 pi i/n}
b9 = 1 / tau
ms9, rho9 = (1 - b9 ** 2) / 2, (1 + b9 ** 2) / 2
cos2, sin2 = (1 - tau ** 2) / (1 + tau ** 2), 2 * tau / (1 + tau ** 2)
record("E9_uniform_cycle_real_part", is_zero(ms9 + rho9 * cos2))
record("E9_uniform_cycle_imag_part", is_zero(b9 - rho9 * sin2))

# E10: exact n = 3 control at beta = 1/sqrt(3) (Theorem 14 boundary) and n = 4 at beta = 1, uniform cycles,
# full PH normalization symbolic in A = 1 + C, positivity of v for all C > 0 via coefficient signs.
for n, bval in ((3, 1 / sp.sqrt(3)), (4, sp.Integer(1))):
    msv = (1 - bval ** 2) / 2
    Wv = (1 - msv) ** n
    Mm = sp.zeros(n, n)
    for i in range(n):
        Mm[i, i] = msv
    for i in range(n - 1):
        Mm[i, i + 1] = 1
    Mm[n - 1, 0] = Wv
    Dn = (x - 1) * (x ** 2 + bval ** 2)
    qn = sp.expand((x - msv) ** n - Wv)
    quo, rem = sp.div(qn, sp.expand(Dn), x)
    Kc = C * ((1 + C) ** 2 + bval ** 2)
    rhov = (1 + bval ** 2) / 2
    if n == 3:
        tv = sp.Matrix([0, 0, Kc])
    else:
        tv = sp.Matrix([0, 0, Kc, Kc * Wv / rhov ** 3])
    v, tr = ph_normalize_symbolic(Mm, tv, n, 1 + C)
    target = Kc / ((sig + C) * ((sig + 1 + C) ** 2 + bval ** 2))
    pos = [coeffs_positive_in_C(vi) for vi in v]
    ok = (rem == 0 and is_zero(v[0] - 1) and is_zero(tr - target) and all(p is True for p in pos))
    record(f"E10_uniform_cycle_exact_n{n}", ok, quotient=str(quo), v=[str(vi) for vi in v], v_positive=pos)

# E11: independent n = 4 closed form (screen): diag (0, 0, r, -r), W = beta^2 = 1 - r^2, exits (0,0,K,K(1-r)),
# symbolic in r in (0,1), A = 1 + C: divisibility, v1 = 1, transform identity, exit positivity.
b2 = 1 - r ** 2
M11 = sp.Matrix([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, r, 1], [b2, 0, 0, -r]])
q11 = sp.expand(x ** 2 * (x - r) * (x + r) - b2)
D11 = sp.expand((x - 1) * (x ** 2 + b2))
quo11, rem11 = sp.div(q11, D11, x)
K11 = C * ((1 + C) ** 2 + b2)
t11 = sp.Matrix([0, 0, K11, K11 * (1 - r)])
v11, tr11 = ph_normalize_symbolic(M11, t11, 4, 1 + C)
target11 = K11 / ((sig + C) * ((sig + 1 + C) ** 2 + b2))
record("E11_screen_n4_closed_form", rem11 == 0 and is_zero(v11[0] - 1) and is_zero(tr11 - target11)
       and sp.expand(quo11 - (x + 1)) == 0, quotient=str(quo11))

res["_elapsed_seconds"] = round(time.time() - t0, 2)
res["_all_ok"] = all(v["ok"] for k, v in res.items() if isinstance(v, dict))
with lane_guard.xopen(RUN + "/exact.json") as fh:
    json.dump(res, fh, indent=1)
print("ALL_OK", res["_all_ok"], "elapsed", res["_elapsed_seconds"])
