# Open five-contact shape family with six-dimensional span rigidity

**Status: WRITTEN candidate with exact WRITTEN-checked-in-kernel determinant evidence; author result, not parent adoption.** A nonempty open set of the feasible nine-parameter five-contact boundary shapes has the following property: every sufficiently near-boundary strictly stable radial box has **no** common SPR numerator in the real span of its four parity endpoints and the first two derivatives of its midpoint. This theorem does not claim an unrestricted common numerator for every shape; the separate explicit example has one.

## Opposite-sign determinant criterion

Use the boundary family, its five actual corner/contact pairs, and the six generators
\[
g=(E_-(-s^2),E_+(-s^2),sO_-(-s^2),sO_+(-s^2),Dm,D^2m)
\]
from `frontier-20261028-generic-five-contact-span-rigidity-v1.md` and `frontier-20261029-six-dimensional-endpoint-derivatives-open-obstruction-v1.md`, where \(m\) is the boundary coefficient midpoint. Let \(T\) be the \(5\times6\) matrix of the five boundary contact derivatives \(\partial_tP_{a_i,g_j}(t_i)\), and let \(r(t)\) be the row of pairings with the actual boundary corner \(a_{--}\). Suppose, for some fixed \(t_\star>0\),
\[
\det\begin{pmatrix}T\\r(0)\end{pmatrix}
\det\begin{pmatrix}T\\r(t_\star)\end{pmatrix}<0.
\]
Then \(T\) has rank five and its one-dimensional kernel is spanned by its signed cofactor vector \(q\). Up to one common sign, \(r(0)q\) and \(r(t_\star)q\) are the two displayed determinants; they have opposite signs. Thus no nonzero polynomial in the boundary six-generator span satisfying all five contact tangent conditions can have both pairings nonnegative.

By the compactness argument in the cited generic span theorem, if near-boundary radial boxes admitted such common numerators arbitrarily close to \(\rho=1\), a normalized subsequence would converge to a nonzero boundary-span polynomial. Rank five implies the six generators are independent: a generator relation would lie in \(\ker T\) and be annihilated by \(r(0)\), contradicting the nonzero extended determinant. Generator coordinates therefore remain bounded near the boundary. The limit's five contact pairings are nonnegative and vanish at their interior contact points, so all five derivatives vanish. Its pairings at \(t=0\) and \(t=t_\star\) are also nonnegative. The opposite-sign criterion rules out this nonzero limit, a contradiction. Hence some shape-dependent \(\rho_0<1\) excludes the real six-generator span for every \(\rho\in(\rho_0,1)\). The alternating marker signs ensure these radial boxes are strictly Hurwitz.

## A nonempty open set

At the explicitly feasible shape
\[
(t_1,\ldots,t_5)=(1,2,3,6,8),\quad
u=1/2,\quad v=11,\quad\alpha=1,\quad\beta=989/855,\quad t_\star=5,
\]
the two exact determinants are
\[
\frac{92976603844243299782254016}{37141485}>0,\qquad
-\frac{11890176991971970453391840}{22284891}<0.
\]
They remain of opposite sign on a nonempty open neighborhood in the nine-dimensional feasible shape space, because the entries are polynomial in those parameters. This is an **open-set** result, not a claim of density or of all shapes. For the anchor shape, the companion six-dimensional packet additionally gives a concrete \(\rho=9999/10000\) box, seven actual positive atoms, an explicit unrestricted common numerator, and an explicit endpoint neighborhood.

Frozen determinants: `frontier-20261029-generic-six-dimensional-boundary-frozen-v1.json`, SHA-256 `380cf257268e41b9744ea7157e3ac22b4df0a1195df9e9c03c81b1ef7942f891`. Independent factor and monomial checker `frontier-20261029-generic-six-dimensional-boundary-independent-kernel-v1.py`, SHA-256 `8a0b719d9eee5d978bb6a65f831546de9d1219f589f4bd273f7dd29cc416fe4b`; receipt `frontier-20261029-generic-six-dimensional-boundary-independent-result-v1.json`, SHA-256 `4b4d36a1b7072e2254550e2b3995d6ddb22552f848a786b440b3ea2d851b1928`. The explicit-box companion is `frontier-20261029-six-dimensional-endpoint-derivatives-open-obstruction-v1.md`, SHA-256 `552e4c5ce6e169743e8e90c855d750d047f7c6ea1941378372c19d8d8c583acf`.

The determinant values were computed exactly with integers and `fractions.Fraction` on one Python Eval host. The openness, rank, compactness and stability arguments are written mathematics; no formal proof, cross-vendor review, novelty clearance, universal arbitrary-box theorem, or unrestricted negative certificate is claimed.
