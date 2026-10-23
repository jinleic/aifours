"""DUAL far-region tests, version 4 (supersedes me3dual_v3.py for certified use; v3 kept unchanged).

Changes from v3 (found in exploratory calibration k02, run x05-debugG):
  * W is evaluated as W = w1 zz + w2 zz^2 + w3 zz^3 with zz = 1/(1+xi) and w1 = kappa s^2/N1, w2 = -2 s(1-s)/N1,
    w3 = 2(1-s)^2/N1 (identical to Nt(s,1+xi)/(N1 (1+xi)^3), but without the cancellation of the three O(1) terms
    of Nt that made the naive ball of W contain 0 for small s and large |xi|);
  * test_general first encloses W by the complex mean-value form W(m) + sum_j dW_j(B)[-h_j, h_j] (valid: W(x) - W(m)
    is an integral of grad W over the segment, whose values lie in the convex balls dW_j(B)), and uses the
    intersection with the naive ball for the branch decision, the SMALL test and the RADIAL test;
  * LD top boxes (beta reaching pi/2) use Arg_+ in [0, 2 pi): ratio <= 2 pi / tan(beta_lo) (v3 wrongly assumed
    beta + arg P >= 0 there).
All other definitions, certificates and identities are as documented in me3dual_v3.py (LEMMA D, series, B-edge).
"""
from flint import arb, acb
from me3jet_v1 import J, LOG, RE, IM, mvf
import me3dual_v3 as V3

I = acb(0, 1)
ball, sym, N1f = V3.ball, V3.sym, V3.N1f


def twopi():
    return 2 * arb.pi()


def W_generic(S, Dl, Om, kap):
    N1 = N1f(S, kap)
    zz = 1 / (1 + Dl - I * Om)
    w1 = kap * S * S / N1
    w2 = -2 * S * (1 - S) / N1
    w3 = 2 * (1 - S) * (1 - S) / N1
    return zz * (w1 + zz * (w2 + zz * w3))


def W_enclosure(sl, sh, dl, dh, wl, wh, kap):
    sb, db, wb = ball(sl, sh), ball(dl, dh), ball(wl, wh)
    Wn = W_generic(acb(sb), acb(db), acb(wb), kap)
    mids = [arb((sl + sh) / 2), arb((dl + dh) / 2), arb((wl + wh) / 2)]
    hb = [sym(sl, sh), sym(dl, dh), sym(wl, wh)]
    from me3jet_v1 import jet_inputs
    Wm = W_generic(*[acb(m) for m in mids], kap)
    Wj = W_generic(*jet_inputs([sb, db, wb]), kap)
    re = Wm.real
    im = Wm.imag
    for j in range(3):
        re = re + Wj.d[j].real * hb[j]
        im = im + Wj.d[j].imag * hb[j]
    # intersect with the naive enclosure when both are finite
    rr = re.intersection(Wn.real) if Wn.real.is_finite() else re
    ii = im.intersection(Wn.imag) if Wn.imag.is_finite() else im
    return acb(rr, ii), sb, db, wb, mids, hb


def _branch(W):
    if W.imag > 0:
        return arb(0), "up", 1
    if W.imag < 0:
        return twopi(), "down", 1
    if W.real < 0:
        return arb.pi(), "left", -1
    return None, None, None


def test_general(sl, sh, dl, dh, wl, wh, kap, theta_tri):
    W, sb, db, wb, mids, hb = W_enclosure(sl, sh, dl, dh, wl, wh, kap)
    aW = abs(W)
    if aW < (-2 * arb.pi() * db / wb).exp():
        return True, "small"
    c, mode, sgn = _branch(W)
    if mode is not None and aW > 0:
        alpha = (-W).arg() + c if mode == "left" else W.arg() + c
        phi = wb * aW.log() + db * alpha
        if phi < 0:
            return True, "radial"
        Wm = W_generic(*[acb(m) for m in mids], kap)
        cm, modem, _ = _branch(Wm)
        if modem == mode:
            def F(S, Dl, Om):
                Lg = LOG(sgn * W_generic(S, Dl, Om, kap))
                return (Om * RE(Lg) + Dl * (IM(Lg) + c),)
            (pm,) = mvf(F, mids, [sb, db, wb], hb)
            if pm < 0:
                return True, "radial-mvf"
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


def test_largew(sl, sh, dl, dh, nl, nh, kap):
    return V3.test_largew(sl, sh, dl, dh, nl, nh, kap)


def _ratio_small_beta(Pv, Pb, bh):
    return V3._ld_ratio_small_beta(Pv, Pb, bh)


def test_ld1(sl, sh, d0l, d0h, bl, bh, kap, beta_top):
    sb, db, bb = ball(sl, sh), ball(d0l, d0h), ball(bl, bh)
    N1 = N1f(sb, kap)
    w1, w2, w3 = kap * sb * sb / N1, -2 * sb * (1 - sb) / N1, 2 * (1 - sb) * (1 - sb) / N1
    cb, sn = bb.cos(), bb.sin()
    zeta = db * cb * acb(cb, sn)
    P = w1 + w2 * zeta + w3 * zeta * zeta
    aW = abs(db * cb) * abs(P)
    omd = 1 - db
    if bh >= beta_top:
        if not (bl > 0):
            return False, "ld1-top"
        ratio = arb(0).union(twopi() / arb(bl).tan())   # any W != 0 has an argument in [0, 2 pi)
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
        ratio = _ratio_small_beta(P, Pb, bh)
        if ratio is None:
            return False, "ld1-ratio"
    if aW < (-omd * ratio).exp():
        return True, "ld1"
    return False, "ld1"


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
    omd = 1 - arb(d_max)
    if bh >= beta_top:
        if not (bl > 0):
            return False, "ld2-top"
        ratio = arb(0).union(twopi() / arb(bl).tan())
    elif bl > 0:
        if not (Ph.real > 0):
            return False, "ld2-ReP"
        alpha = bb + Ph.arg()
        if not (alpha >= 0):
            return False, "ld2-alpha"
        ratio = alpha / bb.tan()
    else:
        Pb = (-2 * xb * (1 - xb) * (1 - sb) * I * eb + 4 * (1 - sb) * (1 - sb) * (1 - xb) * (1 - xb) * I * e2b) / N1
        ratio = _ratio_small_beta(Ph, Pb, bh)
        if ratio is None:
            return False, "ld2-ratio"
    if aW < (-omd * ratio).exp():
        return True, "ld2"
    return False, "ld2"


def test_corner(sl, sh, dl, dh, wl, wh, kap, N):
    return V3.test_corner(sl, sh, dl, dh, wl, wh, kap, N)


def test_bedge(sl, sh, dl, dh, wh, kap):
    return V3.test_bedge(sl, sh, dl, dh, wh, kap)
