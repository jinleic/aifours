"""Ball-arithmetic (python-flint arb/acb) generator and definition-first checker for the three-pole PH family.

Generator = the construction of proof/ph3-theorem-v1.md Part B (cycle + three IVT angles + Taylor-jet exits).
Checker  = check_ph(): knows only the PH definition and F; it never looks at the generator's internals.
Ball arithmetic encloses every exact value; "certified" means the comparison holds for the whole enclosure.
Positivity/sign results are certified per instance; equalities that are exact theorems are reported as
enclosure-contains-zero consistency checks only. Finite instances never prove the all-n statement.
"""
import flint
from flint import arb, acb, arb_mat, acb_mat, fmpq

# ----------------------------------------------------------------------------------------------------------
# small exact-input helpers


def A_(v):
    """arb from int / fmpq / str / arb."""
    if isinstance(v, arb):
        return v
    return arb(v)


def certified_pos(xb):
    return bool(xb > 0)


def certified_nonneg(xb):
    return bool(xb >= 0)


def maxrad(balls):
    m = arb(0)
    for b in balls:
        r = b.rad()
        if r > m:
            m = r
    return m


def fstr(xb, digits=25):
    return xb.str(digits, radius=True) if hasattr(xb, "str") else str(xb)


# ----------------------------------------------------------------------------------------------------------
# polynomial helpers on lists of arb/acb, coefficients low -> high


def poly_mul(p, q):
    out = [p[0] * 0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] = out[i + j] + a * b
    return out


def poly_from_roots(roots):
    p = [arb(1)]
    for r in roots:
        p = poly_mul(p, [-r, arb(1)])
    return p


def poly_eval(p, x):
    acc = p[-1] * 1
    for c in reversed(p[:-1]):
        acc = acc * x + c
    return acc


def poly_divmod_monic(p, d):
    """Divide p by monic d (lists low->high). Returns (quotient, remainder)."""
    p = list(p)
    dq = len(p) - len(d)
    if dq < 0:
        return [arb(0)], p
    quo = [arb(0)] * (dq + 1)
    for k in range(dq, -1, -1):
        coef = p[k + len(d) - 1]
        quo[k] = coef
        for i in range(len(d)):
            p[k + i] = p[k + i] - coef * d[i]
    rem = p[:len(d) - 1]
    return quo, rem


def newton_coeffs(p, nodes):
    """Coefficients c_0..c_d of p in the basis 1, (x-nodes[0]), (x-nodes[0])(x-nodes[1]), ...
    (len(nodes) == deg p). Uses repeated synthetic division."""
    cur = list(p)
    out = []
    for nd in nodes:
        quo, rem = poly_divmod_monic(cur, [-nd, arb(1)])
        out.append(rem[0])
        cur = quo
    out.append(cur[0])
    assert len(cur) == 1
    return out


# ----------------------------------------------------------------------------------------------------------
# band geometry and the construction (normalized time: a - c = 1, x = sigma + A)


def band_psi(n, f):
    """psi for band n at fraction f in (0,1]: psi = hi - f (hi - lo), lo = 2pi/n, hi = 2pi/(n-1) (n>=4) or pi (n=3).
    f = 1 is the upper band endpoint beta = cot(pi/n); f -> 0 approaches the excluded lower endpoint."""
    pi = arb.pi()
    lo = 2 * pi / n
    hi = pi if n == 3 else 2 * pi / (n - 1)
    return hi - A_(f) * (hi - lo)


def G_fun(t, S, phi):
    return (t + phi).sin() * ((S - t) / 2 + phi).sin() ** 2 - phi.sin() ** 3


def find_t(n, psi, phi, S, exact_upper, max_iter=1200):
    """Certified bracket of a root of G on (t0, S/3]. Returns (t_ball, info)."""
    pi = arb.pi()
    if exact_upper:
        return S / 3, {"mode": "upper endpoint t*=S/3 (exact root since n*psi=2pi)"}
    t0b = S - 2 * (pi - phi)
    if t0b < 0:
        lo = arb(0)
    else:
        lo = t0b.upper() if t0b > 0 else arb(0)
    hi = (S / 3).lower()
    g_lo, g_hi = G_fun(lo, S, phi), G_fun(hi, S, phi)
    info = {"lo0": fstr(lo, 15), "hi0": fstr(hi, 15), "G_lo_neg": bool(g_lo < 0), "G_hi_pos": bool(g_hi > 0),
            "t0_case": "t0>0" if t0b > 0 else ("t0=0" if t0b < 0 else "ambiguous")}
    if not (g_lo < 0 and g_hi > 0):
        return None, info
    it = 0
    while it < max_iter:
        mid = ((lo + hi) / 2).mid()
        g = G_fun(mid, S, phi)
        if g < 0:
            lo = mid
        elif g > 0:
            hi = mid
        else:
            break
        it += 1
        if (hi - lo) < arb(2) ** (-(flint.ctx.prec - 20)):
            break
    info["bisect_iter"] = it
    info["width"] = fstr(hi - lo, 5)
    return lo.union(hi), info


def construct(n, f, theta_order=None, rep_angle_scale=None, orient=-1):
    """Normalized construction. Returns dict with balls; flags allow designed mutations:
    theta_order: permutation of angle list (default identity: special angles first);
    rep_angle_scale: multiply the repeated angle psi by this exact factor (mutation);
    orient: m_i = orient * beta * cot(theta_i) (proof uses -1)."""
    pi = arb.pi()
    exact_upper = (fmpq(f) == 1) if not isinstance(f, arb) else False
    psi = band_psi(n, f)
    phi = (pi - psi) / 2
    beta = phi.tan()
    S = 2 * pi - (n - 3) * psi
    tball, tinfo = find_t(n, psi, phi, S, exact_upper)
    out = {"n": n, "f": str(f), "psi": psi, "phi": phi, "beta": beta, "S": S, "t_info": tinfo}
    if tball is None:
        out["ok_angles"] = False
        return out
    rep = psi if rep_angle_scale is None else psi * A_(rep_angle_scale)
    thetas = [tball, (S - tball) / 2, (S - tball) / 2] + [rep] * (n - 3)
    if theta_order is not None:
        thetas = [thetas[k] for k in theta_order]
    out["thetas"] = thetas
    out["ok_angles"] = all(th > 0 and th < pi - phi for th in thetas)
    out["G_at_t_contains_0"] = bool(G_fun(tball, S, phi).contains(0))
    m = [orient * beta * th.cot() for th in thetas]
    out["m"] = m
    one_minus = [1 - mi for mi in m]
    out["ok_one_minus_m_pos"] = all(om > 0 for om in one_minus)
    W = arb(1)
    for om in one_minus:
        W = W * om
    out["W"] = W
    rho = (1 + beta ** 2) / 2
    mstar = (1 - beta ** 2) / 2
    out["rho"], out["mstar"] = rho, mstar
    # closed-form jet coefficients c_k, h_k (proof B7)
    ck = [((psi / 2).cos() - ((2 * k + 3) * psi / 2).cos()) / (2 * (psi / 2).sin() * psi.sin()) for k in range(max(n - 3, 1))]
    hk = [rho ** (-3 - k) * ck[k] for k in range(len(ck))]
    out["c_k"], out["h_k"] = ck, hk
    out["ok_ck_pos_k_le_n_minus_4"] = all(ck[k] > 0 for k in range(n - 3))
    # closed-form normalized exits (K = 1): t = (0,0,1, W h_{n-4}, ..., W h_0)
    t_closed = [arb(0), arb(0), arb(1)] + [W * hk[n - j] for j in range(4, n + 1)]
    out["t_closed"] = t_closed
    # polynomial route: q = prod(x - m_i) - W; P = q / D; exits = Newton coefficients of P for nodes m_n, ..., m_4
    q = poly_from_roots(m)
    q[0] = q[0] - W
    D = poly_mul([-arb(1), arb(1)], [beta ** 2, arb(0), arb(1)])
    P, rem = poly_divmod_monic(q, D)
    out["q_at_1"] = poly_eval(q, arb(1))
    qib = poly_eval([acb(c) for c in q], acb(0, beta))
    out["q_at_ibeta"] = qib
    out["rem"] = rem
    out["P"] = P
    nodes = [m[k] for k in range(n - 1, 2, -1)]  # m_n, m_{n-1}, ..., m_4  (0-based indices n-1..3)
    nc = newton_coeffs(P, nodes)  # coefficient of b_n = 1, b_{n-1} = (x - m_n), ..., b_3
    t_poly = [arb(0), arb(0)] + [nc[n - j] for j in range(3, n + 1)]
    out["t_poly"] = t_poly
    # Perron vector of M: u_1 = 1, u_{i+1} = (1 - m_i) u_i
    uu = [arb(1)]
    for i in range(n - 1):
        uu.append(uu[-1] * one_minus[i])
    out["perron_u"] = uu
    return out


def cycle_matrix(m, W):
    n = len(m)
    M = arb_mat(n, n)
    for i in range(n):
        M[i, i] = m[i]
    for i in range(n - 1):
        M[i, i + 1] = arb(1)
    M[n - 1, 0] = W
    return M


def ph_from_normalized(m, W, t_hat, beta, c, delta):
    """Original-scale PH candidate from normalized pieces. c, delta exact (fmpq/int). Returns dict with alpha,T, a,b,c
    and the normalization data v. alpha is the exact e_1 claimed by the proof (v_1 = 1 is checked separately)."""
    n = len(m)
    c, delta = A_(c), A_(delta)
    a = c + delta
    b = beta * delta
    Anorm = a / delta
    Cnorm = c / delta
    K = Cnorm * (Anorm ** 2 + beta ** 2)
    M = cycle_matrix(m, W)
    T0 = arb_mat(n, n)
    for i in range(n):
        for j in range(n):
            T0[i, j] = M[i, j] - (Anorm if i == j else 0)
    tv = arb_mat(n, 1)
    for i in range(n):
        tv[i, 0] = K * t_hat[i]
    negT0 = arb_mat(n, n)
    for i in range(n):
        for j in range(n):
            negT0[i, j] = -T0[i, j]
    v = negT0.solve(tv)
    vv = [v[i, 0] for i in range(n)]
    T = arb_mat(n, n)
    for i in range(n):
        for j in range(n):
            T[i, j] = delta * T0[i, j] * vv[j] / vv[i] if T0[i, j] != 0 else arb(0)
    alpha = [arb(1)] + [arb(0)] * (n - 1)
    return {"alpha": alpha, "T": T, "a": a, "b": b, "c": c, "v": vv, "K": K, "M": M}


# ----------------------------------------------------------------------------------------------------------
# definition-first checker


def F_value(s, a, b, c):
    ca, cb, cc = acb(a), acb(b), acb(c)
    return cc * (ca * ca + cb * cb) / ((s + cc) * ((s + ca) * (s + ca) + cb * cb))


def check_ph(alpha, T, a, b, c, tol_exp=-120, eig=True):
    """Check PH definition and F identity at test points. Returns dict of booleans + diagnostics.
    alpha: list of arb; T: arb_mat; a,b,c: arb. tol = 2^tol_exp for equality-type enclosure checks."""
    n = T.nrows()
    tol = arb(2) ** tol_exp
    res = {}
    res["alpha_nonneg"] = all(ai >= 0 for ai in alpha)
    sa = arb(0)
    for ai in alpha:
        sa = sa + ai
    res["alpha_sum_is_1"] = bool(sa.contains(1) and (sa - 1).abs_upper() < tol)
    res["metzler"] = all((T[i, j] >= 0) for i in range(n) for j in range(n) if i != j)
    rows = []
    for i in range(n):
        s_ = arb(0)
        for j in range(n):
            s_ = s_ + T[i, j]
        rows.append(s_)
    # row sum <= 0: certified negative, or an enclosure of 0 of radius < tol (exact-zero exit rows)
    res["rowsum_le_0"] = all((rs < 0) or (rs.contains(0) and rs.rad() < tol) for rs in rows)
    res["rows_exactzero_count"] = sum(1 for rs in rows if not (rs < 0))
    # Hurwitz certificate: y_mid > 0 with T y_mid < 0 certified (Metzler => Hurwitz)
    negT = arb_mat(n, n)
    ones = arb_mat(n, 1)
    for i in range(n):
        ones[i, 0] = arb(1)
        for j in range(n):
            negT[i, j] = -T[i, j]
    try:
        y = negT.solve(ones)
        ym = arb_mat(n, 1)
        for i in range(n):
            ym[i, 0] = y[i, 0].mid()
        Ty = T * ym
        res["hurwitz_certificate"] = bool(res["metzler"] and all(ym[i, 0] > 0 for i in range(n))
                                          and all(Ty[i, 0] < 0 for i in range(n)))
    except Exception as e:  # noqa: BLE001
        res["hurwitz_certificate"] = False
        res["hurwitz_error"] = repr(e)
    # transform identity at test points
    exits = [-rs for rs in rows]
    pts = [acb(0), acb(c), acb(-c / 2), acb(0, b), acb(a, 2 * b), acb(3 * a, a)]
    worst = arb(0)
    match = True
    for s in pts:
        Ms = acb_mat(n, n)
        for i in range(n):
            for j in range(n):
                Ms[i, j] = (s if i == j else acb(0)) - acb(T[i, j])
        ev = acb_mat(n, 1)
        for i in range(n):
            ev[i, 0] = acb(exits[i])
        X = Ms.solve(ev)
        val = acb(0)
        for i in range(n):
            val = val + acb(alpha[i]) * X[i, 0]
        diff = val - F_value(s, a, b, c)
        dabs = abs(diff)
        if dabs.upper() > worst:
            worst = dabs.upper()
        if not (diff.real.contains(0) and diff.imag.contains(0) and dabs.upper() < tol):
            match = False
    res["transform_match"] = match
    res["transform_worst_abs_upper"] = fstr(worst, 5)
    if eig:
        try:
            Tc = acb_mat(n, n)
            for i in range(n):
                for j in range(n):
                    Tc[i, j] = acb(T[i, j])
            evs = Tc.eig()
            res["eig_all_re_neg"] = all(e.real < 0 for e in evs)
            targets = [acb(-c), acb(-a, b), acb(-a, -b)]
            res["eig_contains_poles"] = all(any(e.overlaps(tg) for e in evs) for tg in targets)
            sabs = max((e.real.mid() for e in evs), key=lambda r: float(r))
            res["eig_spectral_abscissa_mid"] = fstr(sabs, 15)
        except Exception as e:  # noqa: BLE001
            res["eig_error"] = repr(e)[:200]
    res["PH_OK"] = bool(res["alpha_nonneg"] and res["alpha_sum_is_1"] and res["metzler"] and res["rowsum_le_0"]
                        and res["hurwitz_certificate"] and res["transform_match"])
    return res
