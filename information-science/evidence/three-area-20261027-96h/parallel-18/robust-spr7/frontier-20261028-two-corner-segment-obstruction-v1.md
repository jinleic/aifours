# Two-corner atom supports are excluded, conditional on a named segment theorem

**Status: WRITTEN deduction using an explicit external theorem; not independently reviewed or parent-adopted.** This is a structural obstruction to one class of negative certificates, not a general septic verdict.

## Named import

Yu and Wang, [*Robust Strictly Positive Real Synthesis for Polynomial Families of Arbitrary Order*](https://arxiv.org/html/math/0211012v1), Theorem 1, state: for two real monic Hurwitz polynomials of the same degree, their entire convex segment is Hurwitz if and only if there is a common equal-degree strictly positive-real numerator for the two endpoints. Their Definition 1 explicitly requires the numerator and denominator to have equal degree. The cited theorem is imported as stated; its proof has not been independently reconstructed in this packet.

## Consequence for atom certificates

Assume that theorem. In any all-member-stable monic interval box of any degree, no finite nonzero nonnegative combination of pairing atoms supported on at most two distinct actual denominator members, even allowing the compactified infinity atom, can have all coefficient sums nonpositive. In particular, a negative septic certificate supported on actual parity corners must use at least three distinct corner polynomials.

Indeed, the segment between any two members stays inside the independent coefficient box and is Hurwitz. The imported theorem supplies a single exact-degree numerator \(c\) whose pairings with both are strictly positive at every finite frequency. Its leading coefficient is positive, so its infinity pairing is positive. Moreover \(c\) is itself Hurwitz: along \((1-\theta)a+\theta c\), the ratio to \(a\) has positive real part on the imaginary axis, and the leading coefficient stays positive, so no root crosses. All coefficients of \(c\) are therefore positive. Dotting the purported nonpositive coefficient-sum vector with \(c\) would be nonpositive, while the same dot product is a nonzero nonnegative weighted sum of strictly positive atom pairings. Contradiction.

The independently written fixed-parity theorem in `frontier-20261028-fixed-parity-arbitrary-odd-degree-theorem-v1.md` supplies an import-free exclusion for any number of atoms sharing one even or one odd component in odd degree; it already rules out adjacent-corner pairs in the septic box. The external segment theorem is needed here to cover a pair of opposite corners or two arbitrary members with both parity components changing.

This deduction does not show that three corners are sufficient for a counterexample, nor that a certificate with three or four corners exists or does not exist. It is a named-import mathematical implication, not a finite computation, formal proof, cross-vendor review, novelty claim, or resolution of the original interval problem.
