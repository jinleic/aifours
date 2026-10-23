"""DUAL far-region tests, version 9: me3dual_v8.py with EXACT corner-series coefficients.

Defect fixed (hostile review institute/runs/six-lane-2026-10-16/review/me3-charts-codex-v1.note.md, finding 1,
FATAL): v8 (like v3 and v7) formed c_j = -2 Re(p^j)/j + 3(-1)^j/j as `-2 * RE(pk) / j + 3 * (-1) ** j / j`. The
second summand is a Python int/int true division, i.e. a binary float rounded BEFORE Arb receives it (first inexact
at j = 5), so the implemented polynomial did not enclose the stated exact coefficients and the j > N tail bound did
not cover the difference. v9 forms

    c_j = (-2 Re(p^j) + 3(-1)^j) / j

with the Python integer 3(-1)^j added exactly to the ball -2 Re(p^j) and a single outward-rounded ball division by
the Python integer j (python-flint converts Python integers exactly). Nothing else changes: the root
p = (s(1-s)(1 + i c0) - kappa s^2)/N1 with c0 = sqrt(2 kappa - 1), the recurrence for (X_m, U_m), the tail bounds and
the acceptance tests are those of me3dual_v8.py. They are copied here verbatim (not imported), so the certified
corner path executes no v3/v7/v8 corner code. The other chart tests are re-exported unchanged from me3dual_v7.py;
their Python-level arithmetic is covered by the static float audit proof/float-audit-v1.md.
"""
from flint import arb, acb
from me3jet_v1 import RE, mvf
import me3dual_v3 as V3
import me3dual_v7 as V7

ball, sym, N1f = V3.ball, V3.sym, V3.N1f
test_general, test_largew, test_ld1, test_ld2, test_bedge = (V7.test_general, V7.test_largew, V7.test_ld1,
                                                             V7.test_ld2, V7.test_bedge)


def corner_series_v9(S, Dl, Om, kap, N):
    """Psi_N = -sum_{j=2}^N c_j U_{j-1} and Ig_N = -sum_{j=1}^N c_j U_j, c_j = (-2 Re(p^j) + 3(-1)^j)/j exactly.
    Generic over acb balls and first-order jets (me3jet_v1.J)."""
    N1 = N1f(S, kap)
    c0 = (2 * kap - 1).sqrt()
    p = (S * (1 - S) * acb(1, c0) - kap * S * S) / N1
    c = [None]
    pk = p
    for j in range(1, N + 1):
        c.append((-2 * RE(pk) + 3 * (-1) ** j) / j)
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
    psi, ig = corner_series_v9(acb(sb), acb(db), acb(wb), kap, N)
    psi, ig = psi.real, ig.real
    mids = [arb((sl + sh) / 2), arb((dl + dh) / 2), arb((wl + wh) / 2)]
    hb = [sym(sl, sh), sym(dl, dh), sym(wl, wh)]
    if not (ig - tail_ig >= 0):
        def Fi(S, Dl, Om):
            return (corner_series_v9(S, Dl, Om, kap, N)[1],)
        (igm,) = mvf(Fi, mids, [sb, db, wb], hb)
        ig = ig.intersection(igm) if ig.is_finite() else igm
        if not (ig - tail_ig >= 0):
            return False, "corner-img"
    if psi + tail_psi < 0:
        return True, "corner"

    def Fp(S, Dl, Om):
        return (corner_series_v9(S, Dl, Om, kap, N)[0],)
    (pm,) = mvf(Fp, mids, [sb, db, wb], hb)
    if pm + tail_psi < 0:
        return True, "corner-mvf"
    return False, "corner"
