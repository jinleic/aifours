# Universal four-block upper sign — homogeneous coefficient-certificate reduction

Before-creation clock observed: **2026-10-23T16:32:15-07:00**. PhysicsResearch96h. Written reduction for the SAME all-reference sufficient-route target. This is not a positive certificate yet and is not unrestricted W4. A possible symbolic computation described below is NOT executed or authorized by this file.

The seven fixed-reference assay results are not premises. The proposed reduction concerns all nonnegative Schmidt probabilities, not another list of sampled references. The other generic8/12-dimensional residuals remain in scope even if this four-block lemma is completed.

## 1. Exact homogeneous physical matrix

Use four formal nonnegative variables p0,p1,p2,p3, not all zero, and S=sum p_i. Normalized probabilities are x_i=p_i/S. Define elementary symmetric polynomials e2,e3 in p and

`W3=S^3+2S e2-e3`,

`Dab=2S-p0-p1`, `Dcd=2S-p2-p3`,

`L=4W3 Dab Dcd`.

All three denominator factors are strictly positive on S>0. Indeed Dab,Dcd>=S>0. Also W3/S^3 is checkpoint002's regular common W, equal to `1+2T(1-T)+(1+T)m+(2-T)n>=1` for normalized pair coordinates.

For the fixed four-distinct-label coordinate block with positive labels0,1 and negative labels2,3, let M=C4-S4. It is enough to prove positivity of the symmetric polynomial matrix P=L M. Its diagonal entries all equal L; its six upper off-diagonal entries are

`P12=S[2S^2+(p0+p2)(p1+p3)] Dab Dcd`,

`P34=S[2S^2+(p0+p3)(p1+p2)] Dab Dcd`,

`P13=-2W3 Dcd(2S-p1)`,

`P24=-2W3 Dcd(2S-p0)`,

`P14=-2W3 Dab(2S-p3)`,

`P23=-2W3 Dab(2S-p2)`.

Each entry is homogeneous of degree5. These formulas follow from the physical matrix already derived in checkpoint001 and the exact cancellation

`1/4+E_ij=[2+(x_i+x_j)(1-x_i-x_j)]/(4W)`.

They do not assume positive eigenvalues or use point interpolation.

The same formula covers every four-dimensional phase block by relabeling the four probabilities. A proof for all p>=0 is consequently a proof for all such blocks, not merely one spectrum ordering.

## 2. Four leading minors suffice, with boundary handling explicit

Let f_k be the determinant of the leading kxk principal submatrix of P, k=1,2,3,4. Each f_k is homogeneous of degree5k. If all four are strictly positive when every p_i>0, Sylvester's criterion proves P>0 there. Since the rational physical matrix M has the positive denominator L at every S>0, it is continuous up to all zero/repeated probabilities. Taking limits then gives M>=0 throughout the required nonnegative domain, including product-reference vertices.

Thus no inverse of a singular q_i expression or omitted zero-eigenvalue branch is needed for this four-block certificate. This positivity criterion would not by itself prove any of the other all-reference matrix blocks.

## 3. A sufficient universal ordered-gap certificate

For each of the24 permutations pi, use the gap substitution

`p_(pi0)=g0+g1+g2+g3`,

`p_(pi1)=g1+g2+g3`,

`p_(pi2)=g2+g3`,

`p_(pi3)=g3`,

where every g_i>=0. These24 closed ordered cones cover the whole nonnegative orthant. Their interiors do not have to be disjoint, and ties are not discarded.

A sufficient certificate is:

- for every k and every permutation, every coefficient of the transformed f_k is nonnegative;
- its coefficient of the pure monomial `g3^(5k)` is strictly positive.

Then all four minors are strictly positive whenever p_i>0, because in the relevant ordered cone the smallest probability is g3>0. This explicitly includes ties among positive probabilities; the other gaps may vanish.

The pure-last coefficient is exactly f_k(1,1,1,1), by homogeneity, so it is independent of the ordering. A hand calibration from the uniform physical four-block is

`det M_[1]=1`,

`det M_[2]=8/9`,

`det M_[3]=47/108`,

`det M_[4]=5/27`.

At p_i=1 the common denominator is L=15552. Therefore the expected integer values of f_k are L^k times those four rationals. These equalities are controls only; evaluating them cannot prove the general polynomial identity or coefficient signs.

For exact efficient expansion the gap transformation can be implemented by three binomial shears after permuting exponents: replace variable0 by variable0+variable1, then1 by1+2, then2 by2+3. Their composition gives precisely the displayed cumulative sums. No floating-point root finder, random reference, numerical PSD test or fitted coefficient is needed.

## 4. Scientific and verification boundary of a proposed computation

A separately admitted integer-polynomial calculation could form P from its defining polynomials, compute the four determinants by the Leibniz formula, perform these exact substitutions and emit all coefficients. If every sign condition passes, the result is a **candidate universal coefficient certificate** for this four-block upper sign. Its defining matrix identity and certificate must still be independently reconstructed before promotion. Checkpoint002 then supplies its asymmetric lower sign.

A negative coefficient is only failure of this sufficient coefficient ansatz: a polynomial may be positive despite some negative coefficients. It is **not** a negative co-Choi value, route failure, proof of exhaustion, or W4 counterexample. A timeout/error is likewise not a mathematical verdict. No automatic replacement ansatz or additional calculation is authorized.

This reduction narrows an algebraic proof obligation without narrowing the scientific quantifiers. The universal all-reference target still requires the generic8-dimensional residuals and zero12-dimensional residuals already recorded, and unrestricted W4 remains NOT PROVED.
