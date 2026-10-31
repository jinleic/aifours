# An explicit 11-parameter open family of five-node certificate exclusions

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 16:31:56 PDT 2026**. **WRITTEN theorem candidate**, importing the predecessor's WRITTEN-checked-in-kernel exact 64-value table; the numerical perturbation guard below was also checked with exact integers and `fractions.Fraction` in one Eval host. No independent review, formal proof, parent adoption or novelty clearance is claimed.

## 1. Explicit open family

Let \(\epsilon=10^{-30}\). Independently perturb the six displayed odd-band endpoints and five squared frequencies by at most \(\epsilon\):
\[
(a,b,c,d,e,f)\approx(1,4,7,13,20,24),\qquad
(t_1,t_2,t_3,t_4,t_5)\approx(2,3,5,6,16). \tag{1}
\]
Define the odd extrema by
\[
O_-(t)=-(t-a)(t-d)(t-e),\qquad O_+(t)=-(t-b)(t-c)(t-f). \tag{2}
\]
They define an actual independent three-coordinate odd coefficient box because the coefficients of \(O_+-O_-\) in \((1,t,t^2)\) remain strictly positive. Let \(K\) be **any** all-Hurwitz monic septic independent coefficient box with exactly this odd box and arbitrary positive even intervals. The five node atoms may use arbitrary actual members, and infinity and zero-odd atoms are allowed.

**Theorem.** No positive odd-canceling measure supported on these five perturbed positive nodes and infinity can satisfy the eight original-box Vieta-vertex no-go inequalities. This holds simultaneously for every point in the explicit 11-parameter neighborhood (1), every eligible even box and every allowed actual atom/weight choice.

The family is genuinely nonvacuous with all seven positive widths: for every perturbed odd box, the fixed even box centered at
\((363/8,407/4,45/2,1)\) with coordinate radius \(1/1000\) is all-Hurwitz together with it. Because the two cubic root-to-coefficient maps have nonzero Vandermonde Jacobians at these simple roots, the six root parameters also give a nonempty open set in the actual odd-endpoint coefficient coordinates; the five node parameters are independent.

## 2. Uniform rational guard

The predecessor `frontier-20261029-fixed-odd-box-uniform-five-node-exclusion-v1.md`, SHA-256 `be552e11fcfb832f77cc15d4a523ee6eee7d0b5863313a17fd32c84eec84883e`, proves the base-point result and gives eight exact minima of the 64 endpoint-circuit/Vieta-vertex values. Their overall minimum is \(1507/6048>1/5\).

The perturbed order is unchanged: \(a<t_1<t_2<b<t_3<t_4<c<d<t_5<e<f\). The first two odd signs in any nonzero odd circuit must be \(-,+\); the next two nodes have odd sign \(-\), and the fifth has sign \(+\). As in the predecessor, odd cancellation gives exactly two four-finite-node-plus-infinity circuits, and one common test cubic
\[
F(t)=(-t)(c-t)(d-t) \tag{3}
\]
is strictly negative at all five nodes. The even upper envelope \(U\) is an actual component with its three roots in the closed gap product \([0,a]\times[b,c]\times[d,e]\). As before, it suffices to bound the same eight odd-endpoint circuit choices against the eight even-root vertices.

Each of these 64 values is a sum of four rational terms \(N_i/D_i\), where \(N_i=F(t_i)F_\nu(t_i)\) is a product of six signed linear factors and
\[
D_i=t_iO_{\pm}(t_i)\prod_{j\ne i}(t_i-t_j)
\]
is a product of seven. Every involved root or node stays in \([0,25]\), so each signed factor has absolute value at most 50. At the base point every denominator factor has absolute value at least 1; throughout (1) each has absolute value at least \(4/5\), so \(|D_i|>1/5\). Every factor changes by at most \(2\epsilon\). Product telescoping gives
\[
|\Delta N_i|\le12\epsilon 50^5,\quad |\Delta D_i|\le14\epsilon 50^6,
\quad
\left|\Delta\frac{N_i}{D_i}\right|\le60\epsilon50^5+350\epsilon50^{12}. \tag{4}
\]
For four terms, exact arithmetic gives
\[
4(60\epsilon50^5+350\epsilon50^{12})
=\frac{13671875000003}{40000000000000000000}<\frac1{10}. \tag{5}
\]
Thus every perturbed endpoint-circuit/vertex value remains larger than \(1/5-1/10=1/10\). Endpoint monotonicity of reciprocals gives the same lower bound for arbitrary actual odd components; even upper-envelope domination and multi-affine interpolation give it for arbitrary even boxes and actual members. A positive mixture of the two circuits therefore has strictly positive pairing at (3), contradicting the proposed no-go's nonpositive vertex condition.

## 3. Admission and width guards

At the base point \(O_+-O_-=412+t+t^2\). Perturbing each root by at most \(\epsilon\), product telescoping with roots bounded by 25 changes each difference coefficient by at most \(3750\epsilon<1\). Thus all three independent odd widths remain positive and all odd coefficients remain positive. The root order in (1) makes the odd bands precisely \([a,b],[c,d],[e,f]\).

At the six base endpoints, the fixed even box has worst signed margins listed in (3) of the predecessor, with minimum \(34871/1000\). Over \(t\in[0,25]\) the derivatives of its two even endpoint cubics have absolute value below \(10000\). Shifting an odd-band endpoint by at most \(\epsilon\) therefore changes the corresponding margin by less than \(10000\epsilon<1/1000\). All six signs persist, proving that this concrete seven-width box remains Hurwitz for every perturbed odd box by the disjoint-band Hermite–Biehler argument.

## 4. Scope

The inequalities in (5), \(3750\epsilon<1\), and \(10000\epsilon<1/1000\) were checked exactly in one Python Eval host; the product bounds, circuit decomposition, root-gap arguments and smooth-coordinate claim are written mathematics. The predecessor's 64 finite checks are named imports, not an independent replay. The neighborhood excludes one support pattern only. Other locations, odd boxes, seven/eight-location supports and the original arbitrary-box verdict remain open. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
