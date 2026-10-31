# Exactly five coefficient-interval escapes are necessary and sufficient

**Status: WRITTEN candidate with WRITTEN-checked-in-kernel independent exact replays; not parent adoption.** There is an explicit 14-dimensional open family of genuine, strictly stable, all-seven-width septic boxes for which the minimum number of original denominator coefficient intervals violated by a common **monic** numerator is **exactly five**. The violating coordinates are necessarily \(b_2,b_3,b_4,b_5,b_6\), and a single explicit common numerator keeps \(b_0,b_1\) strictly inside their own intervals throughout the neighborhood. Thus this is a sharp unrestricted numerator-structure obstruction, not a negative answer to the original existence question.

## The box and the necessary five

Take the actual box \(K\) and the independent endpoint neighborhood \(|\Delta \ell_j|,|\Delta u_j|<10^{-10000}\) from `frontier-20261029-five-forced-coefficient-escapes-open-v1.md` (SHA-256 `8841a0affb66c16f2bab0f4b856b2fc290e7c58182890af0e10b8ffc6ede02c6`). Every box in that neighborhood has seven positive widths and is Hurwitz. The predecessor's five separately positive-weight, actual corner/frequency atom sums show that **every** common monic numerator satisfies the following strict lower bounds throughout this neighborhood:
\[
b_2>10500,\quad b_3>210000,\quad b_4>900000,\quad b_5>2140,\quad b_6>900.
\]
Each bound is strictly larger than the relevant box's own upper endpoint. At the anchor the stronger bounds \((11000,211000,1000000,2150,909)\) apply. These lower bounds use positivity of all coefficients of a common numerator, proved via the stable-segment homotopy in the predecessor. They require five distinct original-interval violations for **every** common monic numerator, with all its coefficients otherwise free.

## A numerator attaining exactly five

For every box in that same explicit neighborhood, the following **same** monic numerator is common SPR:
\[
(b_0,\ldots,b_7)=\left(
\frac{149999}{50},\ \frac{15007499}{50},\
\frac{1467398223}{100},\ \frac{6031551}{25},\
\frac{4801697}{2},\ \frac{247137}{100},\
\frac{153011}{100},\ 1\right).
\]
The independent checker verifies that \(b_0,b_1\) each have more than \(1/100\) distance to **both** of their anchor interval endpoints, so they remain inside all perturbed intervals. It checks all four actual corner pairings directly by signed monomial convolution and compactifies \(t\ge0\) with \(x=t/(1+t)\). On the independently reconstructed dyadic partitions, **all 752 Bernstein coefficients** are strictly positive, with minimum exceeding \(10^{-10}\); the four partitions have 20, 20, 26 and 28 leaves. Affine minimization gives a uniform positive pairing on the entire anchor box and half-line.

For endpoint perturbations of size \(\epsilon=10^{-10000}\), projecting any new member to the anchor box changes every nonleading coefficient by at most \(\epsilon\). If \(S=\sum_{j=0}^7|b_j|\), the compactified pairing changes by at most \(14\epsilon S\), which the checker verifies is less than the displayed strict margin. Thus the same \(b\) is a common numerator throughout the neighborhood and retains \(b_0,b_1\) inside. The predecessor's five necessary bounds force its other five coefficients above the corresponding new upper endpoints. Consequently the minimum number of violations is exactly five at every box in this open family.

## Evidence and limitations

Simple witness and exact frequency partition: `frontier-20261029-five-escapes-simple-sharp-witness-frozen-v1.json`, SHA-256 `594947a89b7c0234e6baa3676e7934b1691f8680a21a790e18b7c17a796f1add`. Independent direct-monomial/affine-substitution/Bernstein replay `frontier-20261029-five-escapes-simple-sharp-independent-kernel-v1.py`, SHA-256 `40162deed1ea37c1e8cb7e035b2404e6b7ab4720dd75fb46d17ef5bacb70eff9`; receipt `frontier-20261029-five-escapes-simple-sharp-independent-result-v1.json`, SHA-256 `047d2cfb0b26d0204439f3cf41212dcb786dfa00ccd0b09b9f60a6469ec7094c`. The checker rejects a zero-numerator-constant mutation. The predecessor supplies the exact five atom certificates and open determinant bounds; the cited anchor/open records supply the box's stability.

The computations are exact integer/`fractions.Fraction` arithmetic on one Python Eval host. The extremal, homotopy, and coefficient-positivity arguments are written mathematics. This example actually **has** a common numerator and therefore cannot be an unrestricted negative certificate. No arbitrary-box existence verdict, formal proof, cross-vendor review, or novelty clearance is claimed.
