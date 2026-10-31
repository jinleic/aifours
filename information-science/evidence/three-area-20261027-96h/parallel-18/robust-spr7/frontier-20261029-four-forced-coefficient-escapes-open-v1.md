# Four coefficients of every common numerator must exceed the box

**Status: WRITTEN candidate with WRITTEN-checked-in-kernel independent exact finite replay; not parent adoption.** For an explicit original-eligible septic box which **does** have a common numerator, every common monic numerator must exceed the denominator's upper interval endpoints in **each** of four specified coefficients. This is a universal necessary condition on the unrestricted numerator, not an optimization or an endpoint-span restriction. It persists throughout an explicit full-width 14-dimensional neighborhood.

## The explicit box and inequalities

Let \(K\) be the actual box in `frontier-20261029-universal-odd-coefficient-open-obstruction-v1.md` (SHA-256 `03faf09f07f8ac0c8ffceb4cb3b42cc86fc881b4822cd1527b98849453c5f30d`): the box whose boundary parity polynomials have the five contact nodes \((1,3/2,100,101,2000)\), at radial factor \(1-10^{-8}\). Its exact fourteen endpoints, stable-corner checks, and a separately replayed unrestricted common numerator are pinned there.

**Theorem.** Every degree-seven common numerator \(b\), normalized to \(b_7=1\), satisfies
\[
\boxed{b_3>211000,\qquad b_4>1000000,\qquad b_5>2150,\qquad b_6>909.}
\]
These are independent necessary inequalities, all holding simultaneously. The corresponding denominator upper endpoints are
\[
\left(\overline a_3,\overline a_4,\overline a_5,\overline a_6\right)=
\left(\frac{81640399998301}{400000000},\frac{8009999963975021}{4000000000000},
\frac{840999999999}{400000000},\frac{200199999999}{200000000000}\right),
\]
each strictly below the respective displayed lower bound. In particular \(b_6\) must be more than 900 times the corresponding denominator upper endpoint. No other numerator coefficient is fixed, bounded, or required to lie in the box.

### Why the numerator coefficients are positive

For any actual Hurwitz \(a\in K\), strict positivity of \(\operatorname{Re}(b/a)\) and exact degree force \(b_7>0\). Positively normalize \(b_7=1\). Along the monic segment \((1-\theta)a+\theta b\), the ratio to \(a\) has positive real part on the imaginary axis, so no imaginary-axis root can occur. Homotopy from \(a\) proves \(b\) Hurwitz; its real coefficients are all strictly positive by factorization into left-half-plane real linear and conjugate quadratic factors. This fact is used below, not assumed for an arbitrary polynomial.

## Four independent atom sums

All atoms are actual corners and positive finite squared frequencies from the eight-pair list in the linked packet. For each target \(j\), a different finite collection has strictly positive rational weights and aggregate monomial vector \(C^{(j)}\), with the following exact properties:

| Target \(j\) | Positive atoms | Strictly negative coordinates among \(0,\ldots,6\) other than \(j\) | Zero coordinates there | \(C_j>0\), \(C_7+T_j C_j\le0\) |
|---|---:|---|---|---:|
| 3 | 7 | 2 | 0,1,4,5,6 | \(T_3=211000\) |
| 4 | 5 | 2,3,6 | 0,1,5 | \(T_4=1000000\) |
| 5 | 6 | 2,6 | 0,1,3,4 | \(T_5=2150\) |
| 6 | 6 | 2 | 0,1,3,4,5 | \(T_6=909\) |

Every pairing of a common numerator with each actual atom is positive, hence \(C^{(j)}\cdot b>0\). Since all \(b_k>0\),
\[
0<C^{(j)}\cdot b\le C^{(j)}_j b_j+C^{(j)}_7b_7
\le C^{(j)}_j(b_j-T_jb_7),
\]
proving the four inequalities. The frozen JSON gives every atom, integer weight and exact coordinate sum. A separate monomial checker reconstructs the sums, signs and thresholds directly, verifies all weights positive, and rejects flipped-weight and increased-threshold controls. None of the four vectors is all-negative: each has one positive coordinate. They are therefore not a negative verdict on the original question.

## Explicit 14-endpoint open persistence

Independently change each lower and upper endpoint by less than \(\epsilon=10^{-10000}\), retaining monicity and recomputing the actual corners. For each of the four atom sums, keep the listed atom frequencies and keep one or two nonpivot positive weights fixed. Solve for the other weights so that the table's zero coordinates remain **exactly** zero. The independently checked zero-coordinate matrices have full row ranks \(5,3,4,5\), respectively, with explicit nonzero pivot minors. At the anchor all selected weights are strictly positive, all other designated coefficients strictly negative, and the following weakened thresholds have strict slack:
\[
b_3>210000b_7,\qquad b_4>900000b_7,\qquad
b_5>2140b_7,\qquad b_6>900b_7.
\]
Each weakened threshold still exceeds the corresponding perturbed denominator upper endpoint.

The open replay makes the Cramer/continuity argument quantitative. A common denominator \(D<10^{37}\) covers all anchor atom-row entries. Because frozen weights are positive integers smaller than \(10^{200}\), every nonzero pivot, replacement or augmented determinant of dimension at most six has anchor magnitude at least \(D^{-6}\). All matrix entries are below \(10^{251}\), and their perturbations below \(10^{241}\epsilon\): original coefficient bounds are below \(10^{10}+1\), atom frequencies are below 2000, at most two frozen free weights enter a row, and all weakened thresholds are at most \(10^6\). The exact checker verifies
\[
6!\,6\,10^{251\cdot5+241}\epsilon<\tfrac12D^{-6}.
\]
Leibniz expansion and telescoping therefore preserve the sign of every relevant determinant, hence all pivot weights, negative coordinates, target scales and weakened threshold slacks. The one fixed unrestricted good numerator and stability persist because this neighborhood is contained in the previously independently replayed \(10^{-370}\) neighborhood. Thus the four individual coefficient escapes hold for **every** box in a nonempty explicitly specified open set.

## Evidence and limits

Exact atoms, sums, zero sets and pivots: `frontier-20261029-four-forced-coefficient-escapes-frozen-v1.json`, SHA-256 `0880f38b67095511ce397296b19bc978a8fdb7a4a14255488fb95232a4268e28`. Independent anchor replay `frontier-20261029-four-forced-coefficient-escapes-independent-kernel-v1.py`, SHA-256 `b3b12d4578a382e20e22bdedf482f9863b06dbeed8257ce38bc70f46436de97c`. Open data `frontier-20261029-four-forced-coefficient-escapes-open-frozen-v1.json`, SHA-256 `8376d4a53a457af8fea6da2722b07efd57968f0d0a6f19256e7e328e77d682e9`; Cramer/augmented-determinant replay `frontier-20261029-four-forced-coefficient-escapes-open-independent-kernel-v1.py`, SHA-256 `3fb6f043838d9592db676143b9e64ec0e5405066d0c06932a565de4bfcdb5791`; combined receipt `frontier-20261029-four-forced-coefficient-escapes-independent-result-v1.json`, SHA-256 `bf2ee5ed5f5c7feb029b39375e48d79c2cb6f7bf756d4ac7e96263e302f18752`.

All finite arithmetic uses exact integers and `fractions.Fraction` on one Python Eval host; Routh/Hurwitz, coefficient positivity, compactness, homotopy and determinant perturbation are written mathematics. The example and neighborhood have common numerators, so these inequalities are not an all-numerator obstruction. No original negative or universal positive verdict, formal proof, cross-vendor review, or novelty clearance is claimed.
