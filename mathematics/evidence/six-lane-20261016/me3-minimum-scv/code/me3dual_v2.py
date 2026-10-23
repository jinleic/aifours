"""Ball-arithmetic primitives for the DUAL sufficient test (python-flint acb/arb). Version 2.

(v1 = me3dual_v1.py is a never-executed draft damaged by an editing slip; it is kept unchanged and unused.)

Setting (real pole 1, pair -(1+delta) +- i w, xi = delta - i w, r = delta/w), threshold T, kappa = 1/(1+T).
Test functional centre mu = s/(1-s), s in [0,1]. With z = 1 + xi:
  Nt(s, z) = kappa s^2 z^2 - 2 s (1-s) z + 2 (1-s)^2           [ = (1-s)^2 N(mu z), N(y) = kappa y^2 - 2y + 2 ]
  W(s, xi) = Nt(s, 1+xi) / (Nt(s, 1) (1+xi)^3)                   [ = Q(mu(1+xi))/Q(mu), Q(y) = N(y)/y^3 ]
Sufficient test (Lemma D): if W = |W| e^{i alpha} with alpha in [0, 2 pi) and
  Phi := w log|W| + delta alpha <= 0, equivalently |W| <= exp(-delta alpha / w),
for every mu > 0, then every nonnegative density with poles {1, 1+xi, 1+conj(xi)} has SCV >= T.
g(xi) := log W (branch continuous from g(0) = 0 along segments from 0):
  g' = Nt_z/Nt - 3/(1+xi),  g'' = (Nt_zz Nt - Nt_z^2)/Nt^2 + 3/(1+xi)^2,
  g''' = (2 Nt_z^3 - 3 Nt Nt_z Nt_zz)/Nt^3 - 6/(1+xi)^3,   Nt_z = 2 kappa s^2 z - 2 s(1-s), Nt_zz = 2 kappa s^2.
  Im g(delta - i w) = -int_0^w Re g'(delta - i sig) d sig.
  R2(xi) = (g(xi) - g'(0) xi)/xi^2 = int_0^1 (1-u) g''(u xi) du;  R2'(xi) = int_0^1 (1-u) u g'''(u xi) du.
  Phi/(w |xi|^2) = -delta <Re R2'(delta - i sig)>_{sig in [0,w]} - Re R2(delta - i w).
"""
from flint import arb, acb

TWO_PI = None


def _twopi():
    return 2 * arb.pi()


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
    """acb box {x - i y : x in [dl,dh], y in [wl,wh]} (arb unions of exact rational endpoints)."""
    return acb(arb(dl).union(arb(dh)), -(arb(wl).union(arb(wh))))


def arg_plus(W):
    """Enclosure of Arg_+(W) in [0, 2 pi): exact branch when W's box avoids the positive real axis issue,
    otherwise the conservative enclosure [0, 2 pi]."""
    re, im = W.real, W.imag
    if im >= 0 and not (re < 0 and im.contains(0)):
        a = W.arg()
        if a >= 0:
            return a
    elif im < 0:
        return W.arg() + _twopi()
    return arb(0).union(_twopi())


def test_general(s, dl, dh, wl, wh, kap):
    """Direct test on a box with w >= wl > 0: w log|W| + delta Arg_+(W) < 0."""
    xi = rect(dl, dh, wl, wh)
    W = W_of(s, xi, kap)
    absW = abs(W)
    if not (absW > 0):
        return False, "absW"
    d = arb(dl).union(arb(dh))
    w = arb(wl).union(arb(wh))
    phi = w * absW.log() + d * arg_plus(W)
    return bool(phi < 0), "general"


def test_corner(s, dh, wh, kap):
    """Corner test for every xi = delta - i w with delta in [0, dh], w in (0, wh]: rectangle R = [0,dh] - i[0,wh]
    contains every u*xi (u in [0,1]) and every delta - i sig (sig in [0, w]). Certifies Re g' < 0 on R (so Im g in
    (0, w max|Re g'|] subset (0, pi)) and Phi/(w|xi|^2) <= -delta Re(g'''(R))/6 - Re(g''(R))/2 < 0."""
    R = rect(0, dh, 0, wh)
    G1 = g1(s, R, kap)
    if not (G1.real < 0):
        return False, "g1sign"
    if not (arb(wh) * abs(G1.real) < arb.pi()):
        return False, "argrange"
    G2 = g2(s, R, kap)
    G3 = g3(s, R, kap)
    d = arb(0).union(arb(dh))
    val = -d * (G3.real / 6) - G2.real / 2
    return bool(val < 0), "corner"


def test_bedge(s, dl, dh, wh, kap):
    """B-edge test for delta in [dl, dh] (dl > 0), w in (0, wh]: Phi/w = log|W| + delta*(Im g / w),
    Im g / w in hull(-Re g'([dl,dh] - i[0, wh])); requires Re g' < 0 there (Im g in (0, pi))."""
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


def test_largedelta(s, d0l, d0h, bl, bh, kap, beta_top):
    """Large-delta chart: d = 1/(1+delta) in [d0l, d0h], beta = arctan(w/(1+delta)) in [bl, bh].
    1/(1+xi) = (d cos b) e^{ib}; W = (d cos b) V, V = [k s^2 e^{ib} - 2 s(1-s)(d cos b) e^{2ib}
    + 2 (1-s)^2 (d cos b)^2 e^{3ib}] / Nt(s,1). Test |W| < exp(-(1-d) * alpha / tan b), alpha = Arg_+ V.
    bl = 0: alpha/tan(b) <= sup d/db arg V on the box (alpha(0) = 0, V(b=0) > 0, b/tan b <= 1).
    bh >= beta_top (box reaching pi/2): alpha/tan b <= 2 pi / tan(bl) (needs bl > 0)."""
    d = arb(d0l).union(arb(d0h))
    b = arb(bl).union(arb(bh))
    cb = b.cos()
    dc = d * cb
    e1 = acb(cb, b.sin())
    e2 = e1 * e1
    e3 = e2 * e1
    N1 = Nt(s, acb(1), kap)
    V = (kap * s * s * e1 - 2 * s * (1 - s) * dc * e2 + 2 * (1 - s) * (1 - s) * dc * dc * e3) / N1
    absW = abs(dc) * abs(V)
    if bh >= beta_top:
        if not (bl > 0):
            return False, "top-needs-bl"
        ratio = arb(0).union(_twopi() / arb(bl).tan())
    elif bl > 0:
        alpha = arg_plus(V)
        ratio = alpha / b.tan()
    else:
        ds = -d * b.sin()
        Vb = (acb(0, 1) * (kap * s * s * e1 - 4 * s * (1 - s) * dc * e2 + 6 * (1 - s) * (1 - s) * dc * dc * e3)
              + (-2 * s * (1 - s) * ds * e2 + 4 * (1 - s) * (1 - s) * dc * ds * e3)) / N1
        if not (V.real > 0):
            return False, "Vreal"
        dargs = (Vb / V).imag
        if not (dargs >= 0):
            return False, "dargsign"
        if not (arb(bh) * dargs.upper() < arb.pi()):
            return False, "argrange"
        ratio = arb(0).union(arb(dargs.upper()))
    rhs = (-(1 - d) * ratio).exp()
    return bool(absW < rhs), "largedelta"


def test_largew(s, dl, dh, nl, nh, kap):
    """Large-w chart: nu = 1/w in [nl, nh], delta in [dl, dh]. zz = 1/(1+xi) = nu/(nu(1+delta) - i).
    W = [k s^2 zz - 2 s(1-s) zz^2 + 2(1-s)^2 zz^3]/Nt(s,1). Test |W| < exp(-delta * nu * Arg_+ W)."""
    d = arb(dl).union(arb(dh))
    nu = arb(nl).union(arb(nh))
    zz = acb(nu) / acb(nu * (1 + d), -1)
    N1 = Nt(s, acb(1), kap)
    W = (kap * s * s * zz - 2 * s * (1 - s) * zz * zz + 2 * (1 - s) * (1 - s) * zz * zz * zz) / N1
    absW = abs(W)
    rhs = (-d * nu * arg_plus(W)).exp()
    return bool(absW < rhs), "largew"
