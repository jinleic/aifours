"""DUAL far-region tests, version 7 (for certified use): me3dual_v6.py with a numerically stable CORNER series.

Change (found in exploratory calibration k03-cal-SWC): v3/v6 computed the power sums P_j = p^j + q^j by the linear
recurrence P_j = -A P_{j-1} - B P_{j-2}, whose ball enclosure inflates like ((|A| + B)/sqrt(B))^j. v7 computes
P_j = 2 Re(p^j) with p = (-A + i sqrt(4B - A^2))/2 by repeated complex multiplication (stable), both in the naive
ball evaluation and in the mean-value form (jets with SQRT, me3jet_v2). Identity: x^2 + A x + B = (x - p)(x - q),
q = conj(p), since 4B - A^2 = 4 s^2 (1-s)^2 (2 kappa - 1)/N1^2 >= 0 (> 0 for 0 < s < 1; at s in {0, 1} p = q real
and P_j = 2 p^j still holds). Then 1 + A xi + B xi^2 = (1 - p xi)(1 - q xi)... NOTE the series of
log(1 + A xi + B xi^2) is -sum_j (p'^j + q'^j) xi^j / j with p', q' the reciprocals' negatives: we need the roots of
y^2 + A y + B in the form (1 - p' xi)(1 - q' xi) = 1 - (p'+q') xi + p'q' xi^2, i.e. p' + q' = -A, p' q' = B, which are
exactly the roots of x^2 + A x + B = 0. So P_j = p'^j + q'^j with p' = (-A + i sqrt(4B - A^2))/2 (and conj), |p'| =
sqrt(B). All other tests are those of me3dual_v6.py.
"""
from flint import arb, acb
from me3jet_v1 import J, RE, mvf
from me3jet_v2 import SQRT
import me3dual_v3 as V3
import me3dual_v6 as V6

I = acb(0, 1)
ball, sym, N1f = V3.ball, V3.sym, V3.N1f
test_general, test_largew, test_ld1, test_ld2, test_bedge = (V6.test_general, V6.test_largew, V6.test_ld1,
                                                             V6.test_ld2, V6.test_bedge)


def corner_series_stable(S, Dl, Om, kap, N):
    """Psi_N = -sum_{j=2}^N c_j U_{j-1} and IgN = -sum_{j=1}^N c_j U_j with c_j = -2 Re(p^j)/j + 3(-1)^j/j."""
    N1 = N1f(S, kap)
    A = (2 * kap * S * S - 2 * S * (1 - S)) / N1
    B = kap * S * S / N1
    p = (-A + I * SQRT(4 * B - A * A)) / 2
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
    psi, ig = corner_series_stable(acb(sb), acb(db), acb(wb), kap, N)
    psi, ig = psi.real, ig.real
    mids = [arb((sl + sh) / 2), arb((dl + dh) / 2), arb((wl + wh) / 2)]
    hb = [sym(sl, sh), sym(dl, dh), sym(wl, wh)]
    if not (ig - tail_ig >= 0):
        def Fi(S, Dl, Om):
            return (corner_series_stable(S, Dl, Om, kap, N)[1],)
        (igm,) = mvf(Fi, mids, [sb, db, wb], hb)
        ig = ig.intersection(igm) if ig.is_finite() else igm
        if not (ig - tail_ig >= 0):
            return False, "corner-img"
    if psi + tail_psi < 0:
        return True, "corner"

    def Fp(S, Dl, Om):
        return (corner_series_stable(S, Dl, Om, kap, N)[0],)
    (pm,) = mvf(Fp, mids, [sb, db, wb], hb)
    if pm + tail_psi < 0:
        return True, "corner-mvf"
    return False, "corner"
