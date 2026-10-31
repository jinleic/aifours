# Both numerator parities must escape their denominator intervals

**Status: WRITTEN candidate with WRITTEN-checked-in-kernel exact independent replay; not parent adoption.** For the same actual eligible full-width box and the same explicit endpoint neighborhood as `frontier-20261029-universal-odd-coefficient-open-obstruction-v1.md` (SHA-256 `03faf09f07f8ac0c8ffceb4cb3b42cc86fc881b4822cd1527b98849453c5f30d`), there is a second independent positive-atom inequality. Taken together, they force **every** common monic numerator to leave the original intervals in at least one even coefficient **and** at least one odd coefficient. The even inequality leaves every odd coefficient and \(b_6\) completely unrestricted, and the odd inequality leaves every even coefficient completely unrestricted. A separately verified common numerator exists throughout the neighborhood.

## A second universal halfspace

For the anchor box with endpoints in the cited odd-halfspace packet, any common degree-seven numerator with \(b_7>0\) obeys
\[
\boxed{\quad b_0-2b_2+20b_4>
\frac{66093999512432059}{2000000000000}\,b_7.\quad}
\]
The rational constant is exactly
\(\overline a_0-2\underline a_2+20\overline a_4\). Hence, for monic \(b\), at least one of
\[
b_0>\overline a_0,\qquad b_2<\underline a_2,\qquad b_4>\overline a_4
\]
is mandatory. Independently, the prior odd inequality requires
\[
b_3>\overline a_3\quad\text{or}\quad b_5<\underline a_5.
\]
These are genuine necessary conditions for **all** common numerators, not claims about a chosen span, optimizer, or numerator ansatz. They give a direct obstruction to synthesizing a numerator by retaining **either** actual parity part; the other parity may be an arbitrary polynomial.

## Exact finite proof

Use the same eight actual corner/squared-frequency pairs listed in the prior packet, but the different eight positive integer weights frozen in `frontier-20261029-universal-simple-even-halfspace-frozen-v1.json`. Independent signed-monomial accumulation gives
\[
C=c\left(1,0,-2,0,20,0,0,-\frac{66093999512432059}{2000000000000}\right),\qquad c>0.
\]
Each common numerator makes all eight pairings strictly positive, so \(C\cdot b>0\). The right side is the maximum of \(a_0-2a_2+20a_4\) on the independent intervals, proving the anchor claim. The prior packet establishes the odd condition by a separate set of weights and replays both all-member stability and an unrestricted common numerator.

## The same explicit open family

Perturb each of the 14 endpoints by less than \(10^{-2000}\), and recompute the actual corners. For their eight monomial pairing rows \(r_i\), form the \(7\times8\) matrix with rows
\[
(r_{i1})_i,(r_{i3})_i,(r_{i5})_i,(r_{i6})_i,
(r_{i2}+2r_{i0})_i,(r_{i4}-20r_{i0})_i,
(r_{i7}+d' r_{i0})_i,
\]
where \(d'=\overline a'_0-2\underline a'_2+20\overline a'_4\). The exact checker verifies that its anchor signed cofactors are all positive after a common orientation, proportional to the frozen positive weights, and give a positive \(b_0\) scale. The anchor matrix and its \(8\times8\) augmentation have common denominator
\(D=6998400000000000000000000000000000000<10^{37}\). Nonzero cofactors and augmented determinant are therefore bounded below by \(D^{-7}\) and \(D^{-8}\), respectively.

Across the indicated endpoint perturbations every matrix entry has magnitude below \(10^{43}\) and changes by less than \(10^{39}\epsilon\), where \(\epsilon=10^{-2000}\): each original pairing row is bounded exactly as in the odd packet, \(|d|<10^5\), and \(|d'-d|\le23\epsilon\). The exact checker verifies
\[
7!\,7\,10^{43\cdot6+39}\epsilon<\tfrac12D^{-7},\quad
8!\,8\,10^{43\cdot7+39}\epsilon<\tfrac12D^{-8}.
\]
Thus the positive cofactor weights and positive \(b_0\) scale persist, giving the even halfspace with **each perturbed box's own** endpoints. The prior odd proof supplies the other halfspace on the same neighborhood and the strict stable common numerator throughout.

## Evidence and limit

Anchor positive-atom data: `frontier-20261029-universal-simple-even-halfspace-frozen-v1.json`, SHA-256 `91074e96c0e7c201380c348247551658485fd81a1c93aacfc9c37800e7408487`. Open data: `frontier-20261029-universal-even-halfspace-open-frozen-v1.json`, SHA-256 `d6cc440cf07351675680929a662f144e6be49353fcb0b3cbd64f8b56dd7ee223`. Standalone exact reconstruction and perturbation replay: `frontier-20261029-universal-even-halfspace-open-independent-kernel-v1.py`, SHA-256 `af354c752fe469f1535cf68118f634d5c7890e9f2e09f27a014c296d19d8ccfc`; receipt `frontier-20261029-universal-even-halfspace-open-independent-result-v1.json`, SHA-256 `874a759bd37a43e0d625626771b50bc2b14733fed4c3f1bb6e41dc92ccfcfe38`. The checker verifies all exact zero coordinates, all eight positive weights and cofactors, the nonzero augmented determinant, both quantitative perturbation inequalities and preservation of the fixed good-numerator margin.

The finite checks use exact integers/`fractions.Fraction` on one Python Eval host; determinant perturbation and the imported compactified stability/positivity arguments are written mathematics. Neither halfspace is an all-negative-coordinate certificate, and their joint feasible region is nonempty. No original negative or universal positive verdict, formal proof, cross-vendor review, or novelty clearance is claimed.
