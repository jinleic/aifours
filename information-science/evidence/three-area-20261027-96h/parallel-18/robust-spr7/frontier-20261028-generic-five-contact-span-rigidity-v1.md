# Generic five-contact boundaries defeat the real endpoint span

**Status: WRITTEN candidate with one WRITTEN-checked-in-kernel determinant; author result, not parent adoption.** For an open dense set of feasible five-contact boundary shapes, sufficiently near-boundary strictly stable radial boxes have **no** common SPR numerator in the real span of their four parity endpoint polynomials. This is a generic obstruction to an endpoint-span construction, not an unrestricted negative certificate and not an assertion that every such box has or lacks some other numerator.

## The nine-parameter boundary family

Take
\[
0<u<t_1<t_2<t_3<t_4<t_5<v,\qquad \alpha,\beta>0,
\]
and set
\[
\begin{aligned}
E_-&=-\beta(t-u)(t-t_3)(t-t_4),& E_+&=-\alpha(t-t_1)(t-t_2)(t-t_5),\\
O_-&=-(t-t_1)(t-t_4)(t-t_5),& O_+&=-(t-t_2)(t-t_3)(t-v).
\end{aligned}
\]
Restrict the nine parameters to the **open feasible set** where the resulting seven independent coefficient intervals have strictly positive lower endpoints and widths. Let \(K_\rho\) be the midpoint-centered radial subbox of the boundary box, \(0<\rho<1\), with monic leading coefficient.

At every positive marker \(t_1,\ldots,t_5\), the center signs are respectively \((-,+),(-,-),(+,-),(+,+),(-,+)\). The corresponding boundary extrema are zero, and the other parity extrema are strict because the roots are distinct. At \(t=0\) both parities are positive and at infinity both leading signs are negative. Therefore every \(K_\rho\), \(\rho<1\), has the alternating root-band signs and is strictly Hurwitz by Hermite–Biehler and connected-box homotopy.

## Tangent rank and compactness theorem

At the boundary, write the four polynomial generators as
\[
g_0=E_-(-s^2),\quad g_1=E_+(-s^2),\quad
 g_2=sO_-(-s^2),\quad g_3=sO_+(-s^2).
\]
The five actual corner/contact pairs are
\[
(a_{+-},t_1),\ (a_{++},t_2),\ (a_{-+},t_3),\
(a_{--},t_4),\ (a_{+-},t_5).
\]
Let \(T\) be the \(5\times4\) matrix whose row \(i\) consists of \(\partial_tP_{a_i,g_j}(t_i)\), \(j=0,\ldots,3\).

**Theorem.** If \(\operatorname{rank}T=4\), there is a shape-dependent \(\rho_0<1\) such that for every \(\rho\in(\rho_0,1)\), no nonzero polynomial in the real span of the four **actual \(K_\rho\) parity endpoint generators** is a common strictly positive-real numerator for \(K_\rho\).

**Proof.** Suppose otherwise. Choose \(\rho_n\uparrow1\) and such common numerators \(b_n\), each normalized by a positive scalar so its coefficient Euclidean norm is one. A subsequence converges to a nonzero polynomial \(b\). Rank four implies the four boundary generators are linearly independent: a linear relation between them would be annihilated by every tangent row. Some four coefficient rows therefore have a nonsingular generator minor, which remains nonsingular nearby. The generator coefficients of \(b_n\) are consequently bounded and, along a further subsequence, converge; hence \(b\) lies in the boundary generator span.

For each boundary contact corner, continuity of \(P\) gives \(P_{a_i,b}(t)\ge0\) for every \(t\ge0\). Since \(E_{a_i}(t_i)=O_{a_i}(t_i)=0\), the same polynomial vanishes at the interior point \(t_i>0\), so its derivative there is zero. The four span coefficients of \(b\) therefore lie in \(\ker T\), which is trivial. This gives \(b=0\), contradicting its unit norm. No independence or compactness of an invented coefficient hull is used. ∎

## Why rank four is generic

Each entry and each \(4\times4\) minor of \(T\) is a polynomial in \((u,v,\alpha,\beta,t_1,\ldots,t_5)\). At the feasible shape
\[
(t_1,\ldots,t_5)=(1,2,3,6,8),\quad
u=\tfrac12,\quad v=11,\quad\alpha=1,\quad\beta=\tfrac{989}{855},
\]
the minor on the first four contact rows is exactly
\[
\frac{3812324409600}{361}\ne0.
\]
All seven coefficient widths there are strictly positive. Thus this minor is not the zero polynomial. Its nonzero set is open and dense in the nine-dimensional feasible open parameter set, and on it \(\operatorname{rank}T=4\). The conclusion is therefore generic in this precise parameterized sense; no claim is made at rank-deficient shapes. The prior explicit \(\rho=49/50\) five-atom example independently proves the obstruction for one actual box and separately supplies an unrestricted common numerator.

Frozen boundary parameters and determinant: `frontier-20261028-generic-five-contact-span-rigidity-frozen-v1.json`, SHA-256 `ec10b639d8fcc0cc9299b21be2cf8549cd015e3a91a13218d15dfb63aec1a0bf`. Independent factor-expansion and monomial-derivative checker `frontier-20261028-generic-five-contact-span-rigidity-independent-kernel-v1.py`, SHA-256 `39ca6cf562d69bc9ff015365ad1ade17b2497f287108ad56a2eca3eb9411ede2`; receipt `frontier-20261028-generic-five-contact-span-rigidity-independent-result-v1.json`, SHA-256 `dd55c9d8f35af754e0fe2db92ddbf038cc0cd4e462d99050cce9529d6728df80`.

Only the specific determinant and factor identities were machine-checked with exact integers and `fractions.Fraction` on one Python Eval host. The genericity, root-band, compactness and tangent arguments are written mathematics. No formal proof, cross-vendor review, novelty clearance, original arbitrary-box verdict, or negative certificate against all numerators is claimed.
