# Erratum: two-frequency obstruction is to the four-corner hull only

**WITHDRAWN claim:** The labels and printed scope in `frontier-20261028-sturm-band-box-numerator-obstruction-frozen-v1.json` and `frontier-20261028-sturm-band-box-numerator-obstruction-independent-kernel-v1.py` incorrectly say that the two-frequency certificate excludes *all* monic numerators in the full coefficient box. Those files are retained unchanged but must not be cited for that claim.

The exact arithmetic in them is correct: the weighted pairing functional is strictly negative on each of the four actual Kharitonov parity corners, while it is positive on the already certified unrestricted common numerator. Hence the valid conclusion is only that **no monic common numerator can lie in the convex hull of those four parity corners**. This includes, for example, every individual Kharitonov vertex and their midpoint. It is not an all-numerator negative certificate, and it does not decide whether a different numerator in the full independent coefficient box exists.

**Reason for correction.** A combination of two frequency pairings is an arbitrary affine functional of the numerator coefficients; its maximum over the full seven-dimensional coefficient box need not be attained at one of the four parity corners. For the displayed positive weights and frequencies, direct exact maximization using the coordinate signs gives
\[
\max_{b\in K}\left(10^{10}P_{a_1,b}(428/3)+7P_{a_2,b}(32768/3)\right)
=\frac{12018495361183542517657199466699640090379939457302821}
{6011579824865280000000000}>0.
\]
Thus the four-corner calculation does not exclude the full box. The coefficient-sign maximizer uses a mixed vertex, not a parity corner. A separate exact breakpoint check also found that no positive weight ratio at those two fixed frequencies makes the full-box maximum negative; this is limited to those two frequencies, not all possible certificates.

The independent monomial-convolution replay did check the four negative corner values and 28 strict Hurwitz minors, but its original scope string overstated their consequence. This erratum supersedes that scope; the valid unrestricted positive numerator remains independently checked in `frontier-20261028-sturm-band-anisotropic-box-synthesis-v1.md`. No formal, cross-vendor or novelty claim is made.
