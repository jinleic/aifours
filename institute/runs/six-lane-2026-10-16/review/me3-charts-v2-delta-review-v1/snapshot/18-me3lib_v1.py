"""Ball-arithmetic (python-flint arb/acb) primitives for the ME(3) minimum-SCV lane.

PRIMAL (D2 extreme rays, real pole 1, pair -(1+delta) +- i omega, r = delta/omega, phi = omega*tau):
  c = (1 - i r) e^{(r - i) phi},  zeta = 1/(1 + r w - i w),  P_k = c zeta^{k+1},  a_k = 1 - Re P_k  (= m_k / k!)
  1 + S = 2 a0 a2 / a1^2.
  d/dr at fixed (w, phi):  dP_k/dr = P_k [phi + (r - i)/(1 + r^2) - (k+1) w zeta],  a_k' = -Re(dP_k/dr).
  S >= T  <=>  G := 2 a0 a2 - (1+T) a1^2 >= 0 (given a1 > 0).
  dS/dr > 0  <=>  D := a0' a1 a2 + a0 a1 a2' - 2 a0 a1' a2 > 0 (given a0, a1, a2 > 0).
Feasibility: phi <= theta1(r), theta1(r) the root in (pi, 2pi) of g_r(u) = e^{r u}(cos u - r sin u) = 1;
  g_r is increasing on (pi, 2pi), so g_r(u) > 1 with u in (pi, 2pi) certifies u > theta1(r).

All functions take arb balls (possibly wide) and return arb balls enclosing every value on the box.
"""
import flint
from flint import arb, acb


def primal_terms(r, w, phi):
    """Return (a0, a1, a2, da0, da1, da2) enclosures for arb balls r, w, phi."""
    one = acb(1)
    c = acb(1, -r) * acb(r * phi, -phi).exp()
    zeta = one / acb(1 + r * w, -w)
    shift = acb(phi) + acb(r, -1) / (1 + r * r)
    a = []
    da = []
    zp = zeta
    for k in range(3):
        P = c * zp
        a.append(1 - P.real)
        dP = P * (shift - (k + 1) * w * zeta)
        da.append(-dP.real)
        zp = zp * zeta
    return a[0], a[1], a[2], da[0], da[1], da[2]


def primal_G_D(r, w, phi, T):
    a0, a1, a2, d0, d1, d2 = primal_terms(r, w, phi)
    G = 2 * a0 * a2 - (1 + T) * a1 * a1
    D = d0 * a1 * a2 + a0 * a1 * d2 - 2 * a0 * d1 * a2
    return a0, a1, a2, G, D


def g_feas(r, u):
    """g_r(u) = e^{r u}(cos u - r sin u)."""
    return (r * u).exp() * (u.cos() - r * u.sin())


def S_point(r, w, phi):
    a0, a1, a2, _, _, _ = primal_terms(arb(r), arb(w), arb(phi))
    return 2 * a0 * a2 / (a1 * a1) - 1
