"""Ball-arithmetic primitives for the DUAL sufficient test (python-flint acb/arb).

Setting (real pole 1, pair -(1+delta) +- i w, xi = delta - i w, r = delta/w), threshold T, kappa = 1/(1+T).
Test functional centre mu = s/(1-s), s in [0,1]. With z = 1 + xi:
  Nt(s, z) = kappa s^2 z^2 - 2 s (1-s) z + 2 (1-s)^2           [ = (1-s)^2 N(mu z), N(y) = kappa y^2 - 2y + 2 ]
  W(s, xi) = Nt(s, 1+xi) / (Nt(s, 1) (1+xi)^3)                   [ = Q(mu(1+xi))/Q(mu), Q(y) = N(y)/y^3 ]
Sufficient test (Lemma D): if W = |W| e^{i alpha} with alpha in [0, 2 pi) and
  Phi := w log|W| + delta alpha <= 0, equivalently |W| <= exp(-delta alpha / w),
for every mu > 0, then every nonnegative density with poles {1, 1+xi, 1+conj(xi)} has SCV >= T.
g(xi) := log W (branch continuous from g(0) = 0):
  g' = Nt_z/Nt - 3/(1+xi),  g'' = (Nt_zz Nt - Nt_z^2)/Nt^2 + 3/(1+xi)^2,
  g''' = (2 Nt_z^3 - 3 Nt Nt_z Nt_zz)/Nt^3 - 6/(1+xi)^3,   Nt_z = 2 kappa s^2 z - 2 s(1-s), Nt_zz = 2 kappa s^2.
  l1 = g'(0) (real).  Im g(delta - i w) = -int_0^w Re g'(delta - i sig) d sig.
  R2(xi) = (g(xi) - l1 xi)/xi^2 = int_0^1 (1-u) g''(u xi) du;  R2'(xi) = int_0^1 (1-u) u g'''(u xi) du.
  Phi/(w |xi|^2) = -delta <Re R2'(delta - i sig)>_{sig in [0,w]} - Re R2(delta - i w).
"""
import flint
from flint import arb, acb


def Nt(s, z, kap):
    return kap * s * s * z * z - 2 * s * (1 - s) * z + 2 * (1 - s) * (1 - s)


def Nt_z(s, z, kap):
    return 2 * kap * s * s * z - 2 * s * (1 - s)


def W_of(s, xi, kap):
    z = 1 + xi
    return Nt(s, z, kap) / (Nt(s, acb(1), kap) * z * z * z)


def g1(s, xi, kap):
    z = 1 + xi
    return Nt_z(s, z, kap) / Nt(s, z, kap) - 3 / z


def g2(s, xi, kap):
    z = 1 + xi
    N = Nt(s, z, kap)
    Nz = Nt_z(s, z, kap)
    Nzz = 2 * kap * s * s
    return (Nzz * N - Nz * Nz) / (N * N) + 3 / (z * z)


def g3(s, xi, kap):
    z = 1 + xi
    N = Nt(s, z, kap)
    Nz = Nt_z(s, z, kap)
    Nzz = 2 * kap * s * s
    return (2 * Nz * Nz * Nz - 3 * N * Nz * Nzz) / (N * N * N) - 6 / (z * z * z)


def rect(dl, dh, wl, wh):
    """acb box {x - i y : x in [dl,dh], y in [wl,wh]} (arb unions)."""
    return acb(arb(dl).union(arb(dh)), -(arb(wl).union(arb(wh))))


def test_general(s, dl, dh, wl, wh, kap):
    """Direct test on a box with w >= wl > 0. Returns (ok, info). Uses W on the box and Arg_+."""
    xi = rect(dl, dh, wl, wh)
    W = W_of(s, xi, kap)
    absW = abs(W)
    if not (absW > 0):
        return False, "absW"
    d = arb(dl).union(arb(dh))
    w = arb(wl).union(arb(wh))
    re, im = W.real, W.imag
    if im >= 0 and not (re < 0 and im.contains(0)):
        alpha = W.arg()  # principal arg in [0, pi]
        if not (alpha >= 0):
            return False, "branch"
    elif im < 0:
        alpha = W.arg() + 2 * arb.pi()
    else:
        return False, "branch"
    phi = w * absW.log() + d * alpha
    re, im = W.real, W.imag
    if im >= 0 and not (re < 0 and im.contains(0)):
        alpha = W.arg()  # principal arg in [0, pi]
        if not (alpha >= 0):
            alpha = arb(0).union(2 * arb.pi())
    elif im < 0:
        alpha = W.arg() + 2 * arb.pi()
    else:
        alpha = arb(0).union(2 * arb.pi())  # conservative: Arg_+ always lies in [0, 2 pi)
    phi = w * absW.log() + d * alpha
    return bool(phi < 0), "general"
        return False, "argrange"
    G2 = g2(s, R, kap)
    G3 = g3(s, R, kap)
    d = arb(0).union(arb(dh))
    val = -d * (G3.real / 6) - G2.real / 2
    return bool(val < 0), "corner"


def test_bedge(s, dl, dh, wh, kap):
    """B-edge test for delta in [dl, dh] (dl > 0), w in (0, wh]: Phi/w = log|W| + delta*(Im g / w),
    Im g / w in -hull(Re g'(delta - i[0, wh]))."""
    R = rect(dl, dh, 0, wh)
    G1 = g1(s, R, kap)
    if not (G1.real < 0):
        return False, "g1sign"
    if not (arb(wh) * abs(G1.real) < arb.pi()):
        return False, "argrange"
    W = W_of(s, R, kap)
    absW = abs(W)
    if not (absW > 0):
        return False, "absW"
    d = arb(dl).union(arb(dh))
    val = absW.log() + d * (-G1.real)
    return bool(val < 0), "bedge"


def test_largedelta(s, d0l, d0h, bl, bh, kap):
    """Large-delta chart: d = 1/(1+delta) in [d0l, d0h], beta = arctan(w/(1+delta)) in [bl, bh] subset [0, pi/2].
    1 + xi = e^{-i beta}/(d cos beta). W = (d cos b) V, V = [k s^2 e^{ib} - 2 s(1-s)(d cos b) e^{2ib}
    + 2 (1-s)^2 (d cos b)^2 e^{3ib}] / Nt(s,1). Test |W| <= exp(-(1-d) * alpha / tan(beta)), alpha = Arg_+ V.
    For bl = 0 the ratio alpha/tan(beta) uses alpha/beta in hull(d/db arg V on [0,bh]) and beta/tan(beta) <= 1."""
    d = arb(d0l).union(arb(d0h))
    b = arb(bl).union(arb(bh))
    dc = d * b.cos()
    e1 = acb(b.cos(), b.sin())
    e2 = e1 * e1
    e3 = e2 * e1
    N1 = Nt(s, acb(1), kap)
    V = (kap * s * s * e1 - 2 * s * (1 - s) * dc * e2 + 2 * (1 - s) * (1 - s) * dc * dc * e3) / N1
    absW = dc * abs(V)
    if bl > 0:
        if V.imag >= 0 and not (V.real < 0 and V.imag.contains(0)):
            alpha = V.arg()
        elif V.imag < 0:
            alpha = V.arg() + 2 * arb.pi()
        else:
            return False, "branch"
        if not (alpha >= 0):
            return False, "branch"
        ratio = alpha / b.tan()
    else:
        # derivative of arg V w.r.t. beta = Im(V_b / V), V_b = i[k s^2 e1 - 4 s(1-s) dc e2 + 6(1-s)^2 dc^2 e3]/N1
        #   + terms from d(dc)/db = -d sin b: [- 2 s(1-s)(-d sin b) e2 + 4 (1-s)^2 dc (-d sin b) e3]/N1
        ds = -d * b.sin()
        Vb = (acb(0, 1) * (kap * s * s * e1 - 4 * s * (1 - s) * dc * e2 + 6 * (1 - s) * (1 - s) * dc * dc * e3)
              + (-2 * s * (1 - s) * ds * e2 + 4 * (1 - s) * (1 - s) * dc * ds * e3)) / N1
        if not (V.real > 0):
            return False, "Vreal"
        dargs = (Vb / V).imag
        if not (dargs >= 0):
            return False, "dargsign"
        if not (b.upper() * dargs.upper() < arb.pi()):
            return False, "argrange"
        ratio = dargs  # alpha/beta in hull(dargs) and beta/tan(beta) in (0,1]: alpha/tan(beta) <= dargs_upper
        ratio = arb(0).union(arb(dargs.upper()))
    rhs = (-(1 - d) * ratio).exp()
    return bool(absW < rhs), "largedelta"


def test_largew(s, dl, dh, nl, nh, kap):
    """Large-w chart: nu = 1/w in [nl, nh], delta in [dl, dh]. zz = 1/(1+xi) = nu/(nu(1+delta) - i).
    W = [k s^2 zz - 2 s(1-s) zz^2 + 2(1-s)^2 zz^3]/Nt(s,1). Test |W| <= exp(-delta * nu * alpha)."""
    d = arb(dl).union(arb(dh))
    nu = arb(nl).union(arb(nh))
    zz = acb(nu) / acb(nu * (1 + d), -1)
    N1 = Nt(s, acb(1), kap)
    W = (kap * s * s * zz - 2 * s * (1 - s) * zz * zz + 2 * (1 - s) * (1 - s) * zz * zz * zz) / N1
    absW = abs(W)
    if W.imag >= 0 and not (W.real < 0 and W.imag.contains(0)):
        alpha = W.arg()
    elif W.imag < 0:
        alpha = W.arg() + 2 * arb.pi()
    else:
        # W may straddle the positive real axis only if W ~ 0; fall back to alpha <= 2 pi
        alpha = arb(0).union(2 * arb.pi())
    if not (alpha >= 0):
        alpha = arb(0).union(2 * arb.pi())
    rhs = (-d * nu * alpha).exp()
    return bool(absW < rhs), "largew"
