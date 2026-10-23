"""DUAL far-region tests, version 8: me3dual_v7.py with a cancellation-free root p for the CORNER series.

Change (found in calibration k04-cal-SWC, debug x08): v7 formed sqrt(4B - A^2) from balls of A and B; near s = 1 the
difference 4B - A^2 (about 0.085 at s = 0.9) is a cancellation of two terms near 5.2 and its ball contained 0. v8 uses
the exact identity  p = (s(1-s)(1 + i c0) - kappa s^2)/N1,  c0 = sqrt(2 kappa - 1),  which satisfies
p + conj(p) = 2 Re p = -2 (kappa s^2 - s(1-s))/N1 = -A  and  |p|^2 = s^2[(1-s-kappa s)^2 + (1-s)^2 (2 kappa - 1)]/N1^2
= kappa s^2 N1 / N1^2 = B, so (1 - p xi)(1 - conj(p) xi) = 1 + A xi + B xi^2 = Nt(s, 1+xi)/N1 (no square root of a
ball is needed). Everything else is as in me3dual_v7.py / me3dual_v6.py.
"""
from flint import arb, acb
from me3jet_v1 import RE, mvf
import me3dual_v3 as V3
import me3dual_v7 as V7

I = acb(0, 1)
ball, sym, N1f = V3.ball, V3.sym, V3.N1f
test_general, test_largew, test_ld1, test_ld2, test_bedge = (V7.test_general, V7.test_largew, V7.test_ld1,
                                                             V7.test_ld2, V7.test_bedge)


def corner_series_v8(S, Dl, Om, kap, N):
    N1 = N1f(S, kap)
    c0 = (2 * kap - 1).sqrt()
    p = (S * (1 - S) * acb(1, c0) - kap * S * S) / N1
    c = [None]
    pk = p
    for j in range(1, N + 1):
        c.append(-2 * RE(pk) / j + 3 * (-1) ** j / j)
        pk = pk * p
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
    psi, ig = corner_series_v8(acb(sb), acb(db), acb(wb), kap, N)
    psi, ig = psi.real, ig.real
    mids = [arb((sl + sh) / 2), arb((dl + dh) / 2), arb((wl + wh) / 2)]
    hb = [sym(sl, sh), sym(dl, dh), sym(wl, wh)]
    if not (ig - tail_ig >= 0):
        def Fi(S, Dl, Om):
            return (corner_series_v8(S, Dl, Om, kap, N)[1],)
        (igm,) = mvf(Fi, mids, [sb, db, wb], hb)
        ig = ig.intersection(igm) if ig.is_finite() else igm
        if not (ig - tail_ig >= 0):
            return False, "corner-img"
    if psi + tail_psi < 0:
        return True, "corner"

    def Fp(S, Dl, Om):
        return (corner_series_v8(S, Dl, Om, kap, N)[0],)
    (pm,) = mvf(Fp, mids, [sb, db, wb], hb)
    if pm + tail_psi < 0:
        return True, "corner-mvf"
    return False, "corner"
