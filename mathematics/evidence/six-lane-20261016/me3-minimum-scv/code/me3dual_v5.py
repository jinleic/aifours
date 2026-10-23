"""DUAL far-region tests, version 5 (for certified use; supersedes the never-executed me3dual_v4.py and the
calibration-only me3dual_v3.py, both kept unchanged).

Changes found in exploratory calibration k02 and debug runs x05/x07:
  * GENERAL: W = zz (w1 + zz (w2 + zz w3)), zz = 1/(1+xi), w1 = kappa s^2/N1, w2 = -2 s(1-s)/N1, w3 = 2(1-s)^2/N1,
    enclosed by the intersection of the naive ball and the complex mean-value form (as in v4).
  * B-EDGE: all real-axis quantities are evaluated in REAL arb arithmetic (v3 used acb, whose complex division
    returned an indeterminate ball for wide real denominators, giving nan for g''').
  * LD1/LD2: an argument alpha >= 0 of W is chosen among: beta + principal arg P (if its branch is determined and
    alpha >= 0), beta + Arg_+(P); fallback alpha in [0, 2 pi) via Arg_+(W). For small beta (box starting at 0) the
    mean-value bound on arg P is used as before.
  * CORNER: unchanged from v3 (the number of explicit series terms N is a spec parameter; v3 calibration used N = 60,
    whose naive ball recursion inflated; the certified spec uses a smaller N with the rigorous tail bound).
Definitions, certificates and identities: see the docstring of me3dual_v3.py (LEMMA D, series, B-edge expansion).
"""
from flint import arb, acb
from me3jet_v1 import J, LOG, RE, IM, mvf, jet_inputs
import me3dual_v3 as V3
import me3dual_v4 as V4

I = acb(0, 1)
ball, sym, N1f = V3.ball, V3.sym, V3.N1f
W_generic, W_enclosure = V4.W_generic, V4.W_enclosure
test_general = V4.test_general
test_largew = V3.test_largew
test_corner = V3.test_corner


def twopi():
    return 2 * arb.pi()


def _args_nonneg(P):
    """Candidate enclosures of arguments of P that are >= 0 or principal (may be negative small); returns list."""
    cands = []
    if P.real > 0:
        cands.append(P.arg())                      # principal, continuous on Re P > 0
    if P.imag > 0:
        cands.append(P.arg())                      # in (0, pi)
    elif P.imag < 0:
        cands.append(P.arg() + twopi())            # in (pi, 2 pi)
    elif P.real < 0:
        cands.append((-P).arg() + arb.pi())        # in (pi/2, 3 pi/2)
    return cands


def _ld_common(aW, omd, bb, bl, bh, P, Pb, beta_top):
    """Decide the radial test |W| < exp(-(1-d) alpha / tan beta) for some argument alpha >= 0 of W = (+) e^{i beta} P."""
    rhs_ok = lambda ratio: bool(aW < (-omd * ratio).exp())  # noqa: E731
    if bh >= beta_top or (bl > 0 and bh >= beta_top):
        if bl > 0 and rhs_ok(arb(0).union(twopi() / arb(bl).tan())):
            return True
        return False
    if bl > 0:
        tb = bb.tan()
        for a in _args_nonneg(P):
            alpha = bb + a
            if alpha >= 0 and rhs_ok(alpha / tb):
                return True
        return rhs_ok(arb(0).union(twopi() / arb(bl).tan()))
    # bl == 0: alpha = beta + arg P with arg P continuous from 0 at beta = 0 (needs Re P > 0 on the box)
    ratio = V3._ld_ratio_small_beta(P, Pb, bh)
    if ratio is None:
        return False
    return rhs_ok(ratio)


def test_ld1(sl, sh, d0l, d0h, bl, bh, kap, beta_top):
    sb, db, bb = ball(sl, sh), ball(d0l, d0h), ball(bl, bh)
    N1 = N1f(sb, kap)
    w1, w2, w3 = kap * sb * sb / N1, -2 * sb * (1 - sb) / N1, 2 * (1 - sb) * (1 - sb) / N1
    cb, sn = bb.cos(), bb.sin()
    zeta = db * cb * acb(cb, sn)
    P = w1 + w2 * zeta + w3 * zeta * zeta
    aW = abs(db * cb) * abs(P)
    e2 = acb((2 * bb).cos(), (2 * bb).sin())
    Pb = (w2 + 2 * w3 * zeta) * I * db * e2
    ok = _ld_common(aW, 1 - db, bb, bl, bh, P, Pb, beta_top)
    return ok, "ld1"


def test_ld2(xl, xh, ql, qh, bl, bh, kap, beta_top, s_max, d_max):
    xb, qb, bb = ball(xl, xh), ball(ql, qh), ball(bl, bh)
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
    Pb = (-2 * xb * (1 - xb) * (1 - sb) * I * eb + 4 * (1 - sb) * (1 - sb) * (1 - xb) * (1 - xb) * I * e2b) / N1
    ok = _ld_common(aW, 1 - arb(d_max), bb, bl, bh, Ph, Pb, beta_top)
    return ok, "ld2"


# ---------------------------------------------------------------- B-edge in real arithmetic
def gk_real(S, Dl, kap):
    """g, g', g'', g''' at real xi = delta; S, Dl real (arb or real jets)."""
    z = 1 + Dl
    N1 = kap * S * S - 2 * S * (1 - S) + 2 * (1 - S) * (1 - S)
    Nt = kap * S * S * z * z - 2 * S * (1 - S) * z + 2 * (1 - S) * (1 - S)
    Nz = 2 * kap * S * S * z - 2 * S * (1 - S)
    Nzz = 2 * kap * S * S
    g0 = LOG(Nt / N1) - 3 * LOG(z)
    Pb = (-2 * xb * (1 - xb) * (1 - sb) * I * eb + 4 * (1 - sb) * (1 - sb) * (1 - xb) * (1 - xb) * I * e2b) / N1
    # conservative: 0 < 1 - d <= 1 for every feasible point, and exp(-(1-d) ratio) >= exp(-ratio) for ratio >= 0
    ok = _ld_common(aW, arb(1), bb, bl, bh, Ph, Pb, beta_top)
    g3 = (2 * Nz * Nz * Nz - 3 * Nt * Nz * Nzz) / (Nt * Nt * Nt) - 6 / (z * z * z)
    return g0, g1, g2, g3


def _rjets(balls):
    z, o = arb(0), arb(1)
    units = [(o, z, z), (z, o, z), (z, z, o)]
    return [J(b, units[i]) for i, b in enumerate(balls)]


def test_bedge(sl, sh, dl, dh, wh, kap):
    sb, db = ball(sl, sh), ball(dl, dh)
    whb = arb(wh)
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
    g0, g1, g2, g3 = gk_real(sb, db, kap)
    imlow = -g1 - whb * whb * abs(g3) / 6 - w4 * M5 / 120
    if not (imlow > 0):
        # mean-value form for g1 and g3 in (s, delta)
        mids = [arb((sl + sh) / 2), arb((dl + dh) / 2)]
        jm = gk_real(mids[0], mids[1], kap)
        jj = gk_real(*_rjets([sb, db, arb(0)])[:2], kap)
        hs, hd = sym(sl, sh), sym(dl, dh)
        g1m = jm[1] + jj[1].d[0] * hs + jj[1].d[1] * hd
        g3m = jm[3] + jj[3].d[0] * hs + jj[3].d[1] * hd
        g1 = g1.intersection(g1m) if g1.is_finite() else g1m
        g3 = g3.intersection(g3m) if g3.is_finite() else g3m
        imlow = -g1 - whb * whb * abs(g3) / 6 - w4 * M5 / 120
        if not (imlow > 0):
            return False, "bedge-img"
    Bv = g0 - db * g1
    Cv = -g2 / 2 + db * g3 / 6
    Cu = Cv.upper() if Cv.is_finite() else None
    if Bv.is_finite() and Cu is not None:
        Cp = arb(Cu) if Cu > 0 else arb(0)
        if Bv + whb * whb * Cp + E < 0:
            return True, "bedge"
    mids = [arb((sl + sh) / 2), arb((dl + dh) / 2)]
    jm = gk_real(mids[0], mids[1], kap)
    jj = gk_real(*_rjets([sb, db, arb(0)])[:2], kap)
    hs, hd = sym(sl, sh), sym(dl, dh)
    Bm = (jm[0] - mids[1] * jm[1]) + (jj[0].d[0] - db * jj[1].d[0]) * hs + (jj[0].d[1] - jj[1].v - db * jj[1].d[1]) * hd
    Cmid = -jm[2] / 2 + mids[1] * jm[3] / 6
    Cm = Cmid + (-jj[2].d[0] / 2 + db * jj[3].d[0] / 6) * hs + (-jj[2].d[1] / 2 + jj[3].v / 6 + db * jj[3].d[1] / 6) * hd
    if not (Bm.is_finite() and Cm.is_finite()):
        return False, "bedge"
    Cp = arb(Cm.upper()) if Cm.upper() > 0 else arb(0)
    if Bm + whb * whb * Cp + E < 0:
        return True, "bedge-mvf"
    return False, "bedge"
