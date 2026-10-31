# Both natural sextic truncations can fail for one stable septic

**Status: WRITTEN-checked-in-kernel; additive successor to `frontier-20261028-small-constant-lift-unstable-tail-limitation-v1.md`, not parent adoption.** The same strictly stable septic center in that packet has **both** its constant-truncated tail and its leading-term-truncated head non-Hurwitz. Thus reversing the polynomial does not automatically repair the lower-order lifting hypothesis.

For
\[
p_*(s)=(s+1)\prod_{v\in\{4,5,6\}}((s+1)^2+v^2)
\]
with ascending coefficients \((16354,20420,6419,2681,420,98,7,1)\), the two degree-six truncations have ascending coefficients
\[
\begin{aligned}
(p_*-p_*(0))/s &: (20420,6419,2681,420,98,7,1),\\
p_*-s^7 &: (16354,20420,6419,2681,420,98,7).
\end{aligned}
\]
The first has \(\Delta_5=-1933582924\); the second has \(\Delta_4=-7108113901\). Both violate a necessary Hurwitz-minor condition. Normalizing and reversing the head gives the sextic tail of the monic reciprocal septic:
\[
\left(7/16354,49/8177,210/8177,2681/16354,6419/16354,10210/8177,1\right),
\]
whose own \(\Delta_5=-103753464527335/584911245809539914512<0\). Reciprocal roots preserve the sign of the real part, and the direct negative minor independently verifies the same failure.

The preceding packet already proves that the full seven-width box of radius \(10^{-9}\) around \(p_*\) is all-member Hurwitz and has the common numerator \(p_*\). Its center is included, so neither the original tail set nor the reciprocal-tail set is robustly Hurwitz. No claim is made that every member's truncation is unstable, and this is not an SPR counterexample.

The standalone `frontier-20261028-both-truncations-independent-kernel-v1.py` (SHA-256 `b374e31971be97c758421e07cf3c23fc214a4000a7ac16a9fe3c7e970991f6d9`) reads the prior frozen center and recomputes all three negative minors exactly by rational Gaussian elimination. Receipt `frontier-20261028-both-truncations-independent-result-v1.json` has SHA-256 `221a3eaa2048114bb86a51a7cae86338dd06420550604adf2814146bbc019a29`. Earlier integer Bareiss independently matched the head and original-tail determinants. The surrounding-box certificate is bound in the preceding packet; no formal, cross-vendor, novelty or unrestricted-verdict claim is made.
