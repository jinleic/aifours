"""DUAL far-region tests, version 3 (python-flint arb/acb + first-order jets for mean-value forms).

Notation (real pole 1, pair -(1+delta) +- i w, xi = delta - i w, z = 1 + xi), T = 11/50, kappa = 1/(1+T):
  Nt(s, z) = kappa s^2 z^2 - 2 s (1-s) z + 2 (1-s)^2,  N1 = Nt(s, 1) > 0,  s = mu/(1+mu) in [0,1],
  W(s, xi) = Nt(s, z) / (N1 z^3) = Q_T(mu z)/Q_T(mu),   Q_T(y) = (kappa y^2 - 2 y + 2)/y^3.
  W = w1/z + w2/z^2 + w3/z^3 with w1 = kappa s^2/N1, w2 = -2 s(1-s)/N1, w3 = 2(1-s)^2/N1 (w1 + w2 + w3 = 1).
LEMMA D (written proof): if for every s in (0,1) the point W lies in conv({0} U {e^{-xi t}: t >= 0}), every
nonnegative density with poles {1, z, conj(z)} has SCV >= T. Certificates used here (each a finite convex combination):
  RADIAL : W = |W| e^{i alpha} for some alpha >= 0 with |W| <= e^{-delta alpha / w}   [t = alpha/w, weight |W| e^{delta alpha/w}]
           (any argument alpha >= 0 of W is allowed; W = 0 is trivially fine);
  SMALL  : |W| <= e^{-2 pi delta / w}  (RADIAL with alpha = Arg_+ W in [0, 2 pi));
  TRIANGLE: W = a + b e^{-xi t'} with a, b >= 0, a + b <= 1, t' = theta'/w for an explicit rational theta'.
g = log W (analytic continuation from g(0) = 0 along segments from xi = 0): Phi := Im[conj(xi) g] = w Re g + delta Im g;
if Im g >= 0 then alpha = Im g is an argument of W and RADIAL <=> Phi <= 0.
Series (corner): 1 + A xi + B xi^2 = Nt(s, 1+xi)/N1, A = (2 kappa s^2 - 2 s(1-s))/N1, B = kappa s^2/N1;
  g = sum_{j>=1} c_j xi^j, c_j = -P_j/j + 3(-1)^j/j, P_0 = 2, P_1 = -A, P_j = -A P_{j-1} - B P_{j-2}
  (P_j = p^j + q^j, |p| = |q| = sqrt(B) since A^2 - 4B = 4 s^2 (1-s)^2 (1 - 2 kappa)/N1^2 < 0).
  xi^m = X_m - i w U_m: X_0 = 1, U_0 = 0, X_{m+1} = delta X_m - w^2 U_m, U_{m+1} = X_m + delta U_m; |U_m| <= m |xi|^{m-1}.
  Phi/(w|xi|^2) = -sum_{j>=2} c_j U_{j-1};  Im g / w = -sum_{j>=1} c_j U_j.
B-edge (fixed real delta, 0 < w <= wh): Phi/w = B + w^2 C + E,  B = g(delta) - delta g'(delta),
  C = -g''(delta)/2 + delta g'''(delta)/6,  |E| <= wh^4 M4/24 + delta wh^4 M5/120,
  Im g / w >= -g'(delta) - wh^2 |g'''(delta)|/6 - wh^4 M5/120,
  M_k = sup |g^(k)| on R = [dl,dh] - i[0,wh]:  |g^(k)| <= (k-1)! (|v1|^k + |v2|^k + 3/|z|^k),
  v_{1,2} = 1/(z - z_{1,2}) = kappa s/(kappa s z - (1-s)(1 +- i c0)), c0 = sqrt(2 kappa - 1).
"""
from flint import arb, acb
from me3jet_v1 import J, LOG, RE, IM, mvf

I = acb(0, 1)


def twopi():
    return 2 * arb.pi()


def N1f(s, kap):
    return kap * s * s - 2 * s * (1 - s) + 2 * (1 - s) * (1 - s)


def Ntf(s, z, kap):
    return kap * s * s * z * z - 2 * s * (1 - s) * z + 2 * (1 - s) * (1 - s)


def W_generic(S, Dl, Om, kap):
    z = 1 + Dl - I * Om
    return Ntf(S, z, kap) / (N1f(S, kap) * z * z * z)


def ball(lo, hi):
    return arb(lo).union(arb(hi))


def sym(lo, hi):
    h = (hi - lo) / 2
    return arb(-h).union(arb(h))


# ---------------------------------------------------------------- GENERAL chart (s, delta, w), w >= wl > 0
def _branch_const(W):
    """Return (c, mode) such that alpha = Im(log_principal(sgn*W)) + c is an argument of W, analytic on the box:
    mode 'up' (Im W > 0): alpha = arg W in (0, pi); 'down' (Im W < 0): arg W + 2pi in (pi, 2pi);
    'left' (Re W < 0): arg(-W) + pi in (pi/2, 3pi/2). None if undetermined."""
    if W.imag > 0:
        return arb(0), "up"
    if W.imag < 0:
        return twopi(), "down"
    if W.real < 0:
        return arb.pi(), "left"
    return None, None


def test_general(sl, sh, dl, dh, wl, wh, kap, theta_tri):
    sb, db, wb = ball(sl, sh), ball(dl, dh), ball(wl, wh)
    W = W_generic(acb(sb), acb(db), acb(wb), kap)
    aW = abs(W)
    # SMALL
    if aW < (-2 * arb.pi() * db / wb).exp():
        return True, "small"
    c, mode = _branch_const(W)
    if mode is not None and aW > 0:
        alpha = (-W).arg() + c if mode == "left" else W.arg() + c
        phi = wb * aW.log() + db * alpha
        if phi < 0:
            return True, "radial"
        # mean-value form of Phi on the box (branch fixed by mode)
        sgn = -1 if mode == "left" else 1

        def F(S, Dl, Om):
            Wj = W_generic(S, Dl, Om, kap)
            Lg = LOG(sgn * Wj)
            return (Om * RE(Lg) + Dl * (IM(Lg) + c),)
        mids = [arb((sl + sh) / 2), arb((dl + dh) / 2), arb((wl + wh) / 2)]
        Wm = W_generic(acb(mids[0]), acb(mids[1]), acb(mids[2]), kap)
        cm, modem = _branch_const(Wm)
        if modem == mode:
            (pm,) = mvf(F, mids, [sb, db, wb], [sym(sl, sh), sym(dl, dh), sym(wl, wh)])
            if pm < 0:
                return True, "radial-mvf"
    # TRIANGLE with theta' (rational, in (pi, 2pi)): Z' = e^{-r theta'} e^{i theta'}, r = delta/w
    if theta_tri is not None:
        th = arb(theta_tri)
        rb = db / wb
        Zp = (-rb * th).exp() * acb(th.cos(), th.sin())
        if Zp.imag < 0:
            b = W.imag / Zp.imag
            a = W.real - b * Zp.real
            if b >= 0 and a >= 0 and a + b <= 1:
                return True, "triangle"
    return False, "general"


# ---------------------------------------------------------------- LARGE-w chart (s, delta, nu = 1/w)
def test_largew(sl, sh, dl, dh, nl, nh, kap):
    sb, db, nb = ball(sl, sh), ball(dl, dh), ball(nl, nh)
    zz = acb(nb) / acb(nb * (1 + db), -1)
    N1 = N1f(sb, kap)
    W = (kap * sb * sb * zz - 2 * sb * (1 - sb) * zz * zz + 2 * (1 - sb) * (1 - sb) * zz * zz * zz) / N1
    if abs(W) < (-2 * arb.pi() * db * nb).exp():
        return True, "small"
    return False, "largew"


# ---------------------------------------------------------------- LARGE-delta charts
def _ld_ratio_small_beta(Pv, Pb, bh):
    """alpha = beta + arg P with arg P continuous from 0 at beta = 0 (requires Re P > 0 on the box).
    alpha/tan(beta) <= (1 + sup Im(P_b/P)) * (beta/tan beta), beta/tan beta in (0,1]; alpha >= 0 iff 1 + inf >= 0."""
    if not (Pv.real > 0):
        return None
    q = (Pb / Pv).imag
    lo = 1 + q
    if not (lo >= 0):
        return None
    if not (arb(bh) * lo.upper() < arb.pi() / 2):
        return None
    return arb(0).union(arb(lo.upper()))


def test_ld1(sl, sh, d0l, d0h, bl, bh, kap, beta_top):
    """Chart LD-1: s in [sl, sh] (sl > 0), d = 1/(1+delta) in [d0l, d0h], beta = arctan(w/(1+delta)) in [bl, bh].
    zeta = 1/z = d cos(b) e^{ib}; W = zeta P, P = w1 + w2 zeta + w3 zeta^2; d zeta/d beta = i d e^{2ib}."""
    sb, db, bb = ball(sl, sh), ball(d0l, d0h), ball(bl, bh)
    N1 = N1f(sb, kap)
    w1, w2, w3 = kap * sb * sb / N1, -2 * sb * (1 - sb) / N1, 2 * (1 - sb) * (1 - sb) / N1
    cb, sn = bb.cos(), bb.sin()
    zeta = db * cb * acb(cb, sn)
    P = w1 + w2 * zeta + w3 * zeta * zeta
    aW = abs(db * cb) * abs(P)
    omd = 1 - db
    if bh >= beta_top:
        if not (bl > 0 and P.real > 0):
            return False, "ld1-top"
        ratio = arb(0).union((arb.pi() / arb(bl).tan()))      # alpha = beta + arg P in [0, pi) as Re P > 0
    elif bl > 0:
        if not (P.real > 0):
            return False, "ld1-ReP"
        alpha = bb + P.arg()
        if not (alpha >= 0):
            return False, "ld1-alpha"
        ratio = alpha / bb.tan()
    else:
        e2 = acb((2 * bb).cos(), (2 * bb).sin())
        Pb = (w2 + 2 * w3 * zeta) * I * db * e2
        ratio = _ld_ratio_small_beta(P, Pb, bh)
        if ratio is None:
            return False, "ld1-ratio"
    if aW < (-omd * ratio).exp():
        return True, "ld1"
    return False, "ld1"


def test_ld2(xl, xh, ql, qh, bl, bh, kap, beta_top, s_max, d_max):
    """Chart LD-2 (blow-up at s, zeta -> 0): s = chi*rt, |zeta| = d cos b = (1-chi)*rt, chi in [xl,xh], rt in [ql,qh].
    P-hat = P/rt^2 = [kappa chi^2 - 2 chi (1-chi)(1-s) e^{ib} + 2 (1-s)^2 (1-chi)^2 e^{2ib}]/N1(s).
    W = (1-chi) rt^3 e^{ib} P-hat. Feasibility: s <= s_max and d = (1-chi) rt/cos b <= d_max.
    Returns 'skip' when the whole box is infeasible."""
    xb, qb, bb = ball(xl, xh), ball(ql, qh), ball(bl, bh)
    # infeasible-box skips (exact corner tests)
    if arb(xl) * arb(ql) > arb(s_max):
        return True, "skip-s"
    if (1 - arb(xh)) * arb(ql) > arb(d_max) * arb(bl).cos():
        return True, "skip-d"
    sb = xb * qb
    N1 = N1f(sb, kap)
    eb = acb(bb.cos(), bb.sin())
    e2b = eb * eb
    Ph = (kap * xb * xb - 2 * xb * (1 - xb) * (1 - sb) * eb + 2 * (1 - sb) * (1 - sb) * (1 - xb) * (1 - xb) * e2b) / N1
    aW = abs(1 - xb) * qb * qb * qb * abs(Ph)
    omd = 1 - arb(d_max)          # 1 - d >= 1 - d_max for every feasible point
    if bh >= beta_top:
        if not (bl > 0 and Ph.real > 0):
            return False, "ld2-top"
        ratio = arb(0).union((arb.pi() / arb(bl).tan()))
    elif bl > 0:
        if not (Ph.real > 0):
            return False, "ld2-ReP"
        alpha = bb + Ph.arg()
        if not (alpha >= 0):
            return False, "ld2-alpha"
        ratio = alpha / bb.tan()
    else:
        Pb = (-2 * xb * (1 - xb) * (1 - sb) * I * eb + 4 * (1 - sb) * (1 - sb) * (1 - xb) * (1 - xb) * I * e2b) / N1
        ratio = _ld_ratio_small_beta(Ph, Pb, bh)
        if ratio is None:
            return False, "ld2-ratio"
    if aW < (-omd * ratio).exp():
        return True, "ld2"
    return False, "ld2"


# ---------------------------------------------------------------- SMALL-w corner chart (series)
def corner_series_generic(S, Dl, Om, kap, N):
    """Truncated Psi_N = -sum_{j=2}^N c_j U_{j-1} and IgN = -sum_{j=1}^N c_j U_j (generic over acb/jets)."""
    N1 = N1f(S, kap)
    A = (2 * kap * S * S - 2 * S * (1 - S)) / N1
    B = kap * S * S / N1
    Pm2, Pm1 = 2, -A
    c = [None, -Pm1 / 1 + 3 * (-1) / 1]
    for j in range(2, N + 1):
        Pj = -A * Pm1 - B * Pm2
        c.append(-Pj / j + 3 * (-1) ** j / j)
        Pm2, Pm1 = Pm1, Pj
    X, U = [1], [0]
    w2 = Om * Om
    for m in range(N):
        X.append(Dl * X[m] - w2 * U[m])
        U.append(X[m] + Dl * U[m])
    psi = 0
    for j in range(2, N + 1):
        psi = psi - c[j] * U[j - 1]
    ig = 0
    for j in range(1, N + 1):
        ig = ig - c[j] * U[j]
    return psi, ig


def test_corner(sl, sh, dl, dh, wl, wh, kap, N):
    sb, db, wb = ball(sl, sh), ball(dl, dh), ball(wl, wh)
    N1 = N1f(sb, kap)
    Bup = arb((kap * sb * sb / N1).upper())
    rp = Bup.sqrt()
    xm = (arb(dh) * arb(dh) + arb(wh) * arb(wh)).sqrt()
    q1 = rp * xm
    if not (q1 < 1 and xm < 1):
        return False, "corner-radius"
    tail_psi = 2 * rp * rp * q1 ** (N - 1) / (1 - q1) + 3 * xm ** (N - 1) / (1 - xm)
    tail_ig = 2 * rp * q1 ** N / (1 - q1) + 3 * xm ** N / (1 - xm)
    psi, ig = corner_series_generic(acb(sb), acb(db), acb(wb), kap, N)
    psi, ig = psi.real, ig.real
    if not (ig - tail_ig >= 0):
        # mean-value form for ig
        def Fi(S, Dl, Om):
            p_, i_ = corner_series_generic(S, Dl, Om, kap, N)
            return (i_,)
        mids = [arb((sl + sh) / 2), arb((dl + dh) / 2), arb((wl + wh) / 2)]
        (ig,) = mvf(Fi, mids, [sb, db, wb], [sym(sl, sh), sym(dl, dh), sym(wl, wh)])
        if not (ig - tail_ig >= 0):
            return False, "corner-img"
    if psi + tail_psi < 0:
        return True, "corner"

    def Fp(S, Dl, Om):
        p_, i_ = corner_series_generic(S, Dl, Om, kap, N)
        return (p_,)
    mids = [arb((sl + sh) / 2), arb((dl + dh) / 2), arb((wl + wh) / 2)]
    (pm,) = mvf(Fp, mids, [sb, db, wb], [sym(sl, sh), sym(dl, dh), sym(wl, wh)])
    if pm + tail_psi < 0:
        return True, "corner-mvf"
    return False, "corner"


# ---------------------------------------------------------------- SMALL-w B-edge chart (expansion in w)
def gk_real_generic(S, Dl, kap):
    """g, g', g'', g''' at real xi = delta (generic over acb/jets; inputs real-valued)."""
    z = 1 + Dl
    N1 = N1f(S, kap)
    Nt = Ntf(S, z, kap)
    Nz = 2 * kap * S * S * z - 2 * S * (1 - S)
    Nzz = 2 * kap * S * S
    g0 = LOG(Nt / N1) - 3 * LOG(z)
    g1 = Nz / Nt - 3 / z
    g2 = (Nzz * Nt - Nz * Nz) / (Nt * Nt) + 3 / (z * z)
    g3 = (2 * Nz * Nz * Nz - 3 * Nt * Nz * Nzz) / (Nt * Nt * Nt) - 6 / (z * z * z)
    return g0, g1, g2, g3


def test_bedge(sl, sh, dl, dh, wh, kap):
    sb, db = ball(sl, sh), ball(dl, dh)
    whb = arb(wh)
    # bounds M4, M5 on R = [dl,dh] - i[0,wh]
    c0 = (2 * kap - 1).sqrt()
    zR = acb(1 + db, -(arb(0).union(whb)))
    v1 = kap * sb / (kap * sb * zR - (1 - sb) * acb(1, c0))
    v2 = kap * sb / (kap * sb * zR - (1 - sb) * acb(1, -c0))
    a1, a2, az = abs(v1), abs(v2), 1 / abs(zR)
    M4 = 6 * (a1 ** 4 + a2 ** 4 + 3 * az ** 4)
    M5 = 24 * (a1 ** 5 + a2 ** 5 + 3 * az ** 5)
    if not (M4.is_finite() and M5.is_finite()):
        return False, "bedge-M"
    w4 = whb ** 4
    E = w4 * M4 / 24 + arb(dh) * w4 * M5 / 120
    g0, g1, g2, g3 = gk_real_generic(acb(sb), acb(db), kap)
    g0, g1, g2, g3 = g0.real, g1.real, g2.real, g3.real
    # Im g >= 0 condition
    imlow = -g1 - whb * whb * abs(g3) / 6 - w4 * M5 / 120
    if not (imlow > 0):
        return False, "bedge-img"
    Bv = g0 - db * g1
    Cv = -g2 / 2 + db * g3 / 6
    Cp = arb(0).union(Cv) if not (Cv < 0) else arb(0)
    Cp = arb(Cp.upper()) if Cp.upper() > 0 else arb(0)
    if Bv + whb * whb * Cp + E < 0:
        return True, "bedge"

    def Fb(S, Dl, Om):
        a, b, c, d = gk_real_generic(S, Dl, kap)
        return (a - Dl * b, -c / 2 + Dl * d / 6)
    mids = [arb((sl + sh) / 2), arb((dl + dh) / 2), arb(0)]
    Bm, Cm = mvf(Fb, mids, [sb, db, arb(0)], [sym(sl, sh), sym(dl, dh), arb(0)])
    Cp2 = arb(Cm.upper()) if Cm.upper() > 0 else arb(0)
    if Bm + whb * whb * Cp2 + E < 0:
        return True, "bedge-mvf"
    return False, "bedge"
