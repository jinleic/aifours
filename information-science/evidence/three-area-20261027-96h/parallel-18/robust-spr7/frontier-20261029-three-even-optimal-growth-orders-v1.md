# Sharp growth orders for three unrestricted numerator coordinates

**Status: WRITTEN corollary of pinned symbolic candidates; not parent adoption.** For the explicit stable, full-seven-width and constructively solvable boxes \(K_R\) in `frontier-20261029-unbounded-three-even-coefficients-v1.md` (SHA-256 `dad52df910b0b6fa7826bb2eba21976d0c12dff72e931c01b89e0939f5cc886f`), let
\[
m_j(R)=\inf\{b_j:\ b\text{ is a common monic SPR numerator for }K_R\}.
\]
These infima are finite and nonempty because the cited explicit \(b_R\) is common. For every \(R\ge5000\),
\[
\frac{R^4}{65}\le m_2(R)<\frac{R^4}{6},\quad
\frac{R^4}{100}\le m_4(R)<\frac{R^4}{40},\quad
\frac7{80}R^2\le m_6(R)<\frac{R^2}{5}.
\]
Consequently
\[
m_2(R)=\Theta(R^4),\qquad m_4(R)=\Theta(R^4),\qquad m_6(R)=\Theta(R^2).
\]
The lower sides apply to **every** unrestricted common numerator, via three positive actual-atom functionals; the same single explicit numerator realizes all three upper orders simultaneously. Individual strict lower inequalities yield non-strict lower bounds on the infima; attainment is not claimed.

The exact constructive asymptotic constants are
\[
\lim\frac{(b_R)_2}{R^4}=\frac{1251}{8425},\qquad
\lim\frac{(b_R)_4}{R^4}=\frac8{337},\qquad
\lim\frac{(b_R)_6}{R^2}=\frac{1317}{8425}.
\]
The corresponding denominator maxima grow only as \(\Theta(R^2),\Theta(R^2),\Theta(1)\). Therefore all three optimal numerator-to-denominator coefficient ratios diverge at order \(\Theta(R^2)\), not merely along an unnecessarily large chosen numerator. The b6 improvement is the separately pinned `frontier-20261029-unbounded-b6-strong-lower-v1.md` (SHA-256 `b0cba7cf3305cfb375b1f3eee9739ae8f335a23d2fc9b4f47fb7b0a2ba6206f3`); the open-set transfer is `frontier-20261029-unbounded-three-even-open-addendum-v1.md` (SHA-256 `e6a27e2bcc89d38c728cc1da76802784b2ecc8b6fbc9f14a4a845b2c72cbf22b`).

The preceding independent symbolic replays check all finite polynomial identities and parameter-wide signs with exact `fractions.Fraction` arithmetic on one Python Eval host. The infimum and asymptotic comparisons are written deductions. Exact infimum constants, formal proof, cross-vendor review, novelty clearance and the unrestricted arbitrary-box decision remain open.
