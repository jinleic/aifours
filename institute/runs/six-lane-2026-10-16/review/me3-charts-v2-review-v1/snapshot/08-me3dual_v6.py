"""DUAL far-region tests, version 6 (for certified use). Never-executed drafts me3dual_v4.py (superseded) and
me3dual_v5.py (damaged by an editing slip) are kept unchanged; me3dual_v3.py was used only in exploratory calibration.

Changes relative to v3, found in exploratory calibration k02 and debug runs x05/x07:
  * GENERAL: W = zz (w1 + zz (w2 + zz w3)), zz = 1/(1+xi), w1 = kappa s^2/N1, w2 = -2 s(1-s)/N1, w3 = 2(1-s)^2/N1,
    enclosed by the intersection of the naive ball and the complex mean-value form (me3dual_v4.W_enclosure);
    the test itself is me3dual_v4.test_general (SMALL, RADIAL, RADIAL-MVF, TRIANGLE).
  * B-EDGE: all real-axis quantities in REAL arb arithmetic (v3 used acb; complex division of a wide real
    denominator returned an indeterminate ball, giving nan for g''').
  * LD1/LD2: an argument alpha >= 0 of W is chosen among beta + (principal arg P if alpha >= 0), beta + Arg_+(P),
    and the fallback Arg_+(W) in [0, 2 pi) (ratio <= 2 pi / tan beta_lo). For boxes starting at beta = 0 the
    mean-value bound on arg P is used (needs Re P > 0). The factor (1 - d) in the exponent is bounded
    conservatively: LD1 uses the box ball 1 - d; LD2 uses 1 (since 0 < 1 - d <= 1 and the exponent is >= 0).
  * CORNER: me3dual_v3.test_corner with N explicit series terms from the spec (rigorous tail bound for j > N).
Definitions, certificates and identities: see the docstring of me3dual_v3.py (LEMMA D, series, B-edge expansion).
"""
from flint import arb, acb
from me3jet_v1 import J, LOG
import me3dual_v3 as V3
import me3dual_v4 as V4

I = acb(0, 1)
ball, sym, N1f = V3.ball, V3.sym, V3.N1f
test_general = V4.test_general
test_largew = V3.test_largew
test_corner = V3.test_corner


def twopi():
    return 2 * arb.pi()


def _arg_candidates(P):
    cands = []
    if P.real > 0:
        cands.append(P.arg())
    if P.imag > 0:
        cands.append(P.arg())
    elif P.imag < 0:
        cands.append(P.arg() + twopi())
    elif P.real < 0:
        cands.append((-P).arg() + arb.pi())
    return cands


def _ld_common(aW, omd, bb, bl, bh, P, Pb, beta_top):
    def ok(ratio):
        return bool(aW < (-omd * ratio).exp())
    if bh >= beta_top:
        return bool(bl > 0) and ok(arb(0).union(twopi() / arb(bl).tan()))
    if bl > 0:
        tb = bb.tan()
        for a in _arg_candidates(P):
            alpha = bb + a
            if alpha >= 0 and ok(alpha / tb):
                return True
        return ok(arb(0).union(twopi() / arb(bl).tan()))
    ratio = V3._ld_ratio_small_beta(P, Pb, bh)
    return ratio is not None and ok(ratio)


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
    return _ld_common(aW, 1 - db, bb, bl, bh, P, Pb, beta_top), "ld1"


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
    return _ld_common(aW, arb(1), bb, bl, bh, Ph, Pb, beta_top), "ld2"


def gk_real(S, Dl, kap):
    """g, g', g'', g''' at real xi = delta (S, Dl real arb balls or real jets)."""
    z = 1 + Dl
    N1 = kap * S * S - 2 * S * (1 - S) + 2 * (1 - S) * (1 - S)
    Nt = kap * S * S * z * z - 2 * S * (1 - S) * z + 2 * (1 - S) * (1 - S)
    Nz = 2 * kap * S * S * z - 2 * S * (1 - S)
    Nzz = 2 * kap * S * S
    g0 = LOG(Nt / N1) - 3 * LOG(z)
    g1 = Nz / Nt - 3 / z
    g2 = (Nzz * Nt - Nz * Nz) / (Nt * Nt) + 3 / (z * z)
    g3 = (2 * Nz * Nz * Nz - 3 * Nt * Nz * Nzz) / (Nt * Nt * Nt) - 6 / (z * z * z)
    return g0, g1, g2, g3


def _rjets2(sb, db):
    z, o = arb(0), arb(1)
    return J(sb, (o, z, z)), J(db, (z, o, z))


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
    mS, mD = arb((sl + sh) / 2), arb((dl + dh) / 2)
    hs, hd = sym(sl, sh), sym(dl, dh)
    jm = None
    jj = None
    imlow = -g1 - whb * whb * abs(g3) / 6 - w4 * M5 / 120
    if not (imlow > 0):
        jm = gk_real(mS, mD, kap)
        jj = gk_real(*_rjets2(sb, db), kap)
        g1m = jm[1] + jj[1].d[0] * hs + jj[1].d[1] * hd
        g3m = jm[3] + jj[3].d[0] * hs + jj[3].d[1] * hd
        g1 = g1.intersection(g1m) if g1.is_finite() else g1m
        g3 = g3.intersection(g3m) if g3.is_finite() else g3m
        imlow = -g1 - whb * whb * abs(g3) / 6 - w4 * M5 / 120
        if not (imlow > 0):
            return False, "bedge-img"
    Bv = g0 - db * g1
    Cv = -g2 / 2 + db * g3 / 6
    if Bv.is_finite() and Cv.is_finite():
        Cp = arb(Cv.upper()) if Cv.upper() > 0 else arb(0)
        if Bv + whb * whb * Cp + E < 0:
            return True, "bedge"
    if jm is None:
        jm = gk_real(mS, mD, kap)
        jj = gk_real(*_rjets2(sb, db), kap)
    Bm = (jm[0] - mD * jm[1]) + (jj[0].d[0] - db * jj[1].d[0]) * hs + (jj[0].d[1] - jj[1].v - db * jj[1].d[1]) * hd
    Cm = (-jm[2] / 2 + mD * jm[3] / 6) + (-jj[2].d[0] / 2 + db * jj[3].d[0] / 6) * hs \
        + (-jj[2].d[1] / 2 + jj[3].v / 6 + db * jj[3].d[1] / 6) * hd
    if not (Bm.is_finite() and Cm.is_finite()):
        return False, "bedge"
    Cp = arb(Cm.upper()) if Cm.upper() > 0 else arb(0)
    if Bm + whb * whb * Cp + E < 0:
        return True, "bedge-mvf"
    return False, "bedge"
