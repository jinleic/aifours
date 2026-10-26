# Supplied-proof reconstruction — unrestricted finite-b lower bound and sharp leading MSE

Observed before exclusive creation: **2026-10-23T15:16:09-0700 PDT**. Reviewer MathOlson-2, primary math-2. Assignment: `peer-review-wave-eighteen-v3.json`, read in full including common contract and the MathOlson-2 entry. This is ordinary same-harness written reconstruction, not blind, cross-vendor, human, formal or novelty review. No scientific execution, numerical spot check, solver, compiler or external-model CLI was used. Only this named review output is written; author/shared sources remain unchanged.

## Snapshot, exposure and exact scope

Complete344-line author source read, with overlapping ranged reads1–180 and181–355:

    information-science/evidence/three-area-20261023-96h/parallel-18/
      privacy-diamond-mse/proof-unrestricted-low-privacy-constant-v1.md

**Independently observed SHA256:**

    2a7c0e4ad18fcbed81ab119e5634b112e39b9252403752c2ea20c2c18865eeff

It matches the assigned pin. Read the complete `residual-unrestricted-optimum-v1.md` and the frozen selection/model boundary. I had previously reconstructed the octagonal comparison, so prior exposure is explicitly disclosed. I do NOT inherit its verdict here: the all-law lower-bound engine, disk upper envelope, constants and limiting statements were independently reconstructed in this review. For the dependent gamma-family assertion, I freshly reread its exact load-bearing predecessor sections2–3, lines49–162, and reconstruct them below. The mandatory SCDF provenance addendum was already read completely during the preceding review; it remains operative and is not a theorem-optimality premise.

**Verdict: no substantive defect found at the exact supplied scopes. Findings: 0 FATAL / 0 MAJOR / 0 MINOR.**

The checked claims are:

* For EVERY feasible BOREL probability law and every0<b<1,

      J(mu)>=2sqrt(b/(3pi)+b²/pi²)-2b/pi.

* For the unrestricted optimum over exactly those laws,

      lim_(b↓0) V_b/sqrt(b)=2/sqrt(3pi).

* Dependently, min_gamma C_gamma/sqrt(b) tends to2/3, and its ratio to the unrestricted optimum tends to sqrt(pi/3).

No exact finite-b optimizer, equality in the finite-b lower bound, global finite-b optimality of the disk-core mechanism, full-book resolution, novelty or publication acceptance follows. Parent disposition is separate.

## 1. Measure-level privacy really implies absolute continuity

The model quantifies over EVERY Borel E and EVERY real h in the FULL sensitivity diamond D. If N is any Borel Lebesgue-null set, the imposed inequality may therefore be integrated over h∈D:

    2mu(N)<=b^(-1) integral_D mu(N+h)dh.

The integral is zero. Indeed (x,h)↦1_N(x-h) is jointly Borel measurable, so Tonelli against mu(dx) and Lebesgue dh is legitimate. For each FIXED x the section of h is contained in x-N, a null set. This proves mu(N)=0 for every such N and hence mu is absolutely continuous on the Borel sigma-field. No density/smoothness/symmetry assumption was smuggled into the feasible class.

A nonnegative Borel Radon–Nikodym density p can be chosen with integral1 and finite value a.e. For each FIXED h, changing variables in mu(E+h) gives integral_E p(x+h)dx. Domination for ALL Borel E then implies p(x+h)>=bp(x) for Lebesgue-a.e. x. This is a per-h almost-everywhere statement, not a common exceptional set or a pointwise version for all shifts.

## 2. Correct order of quantifiers in the near-peak floor

The bad-pair set

    {(x,h):h∈D, p(x+h)<bp(x)}

is jointly measurable because p is Borel. Its x-section has measure0 for EACH h. Tonelli on the sigma-finite product Lebesgue space gives a full-measure set H of x for which the inequality holds for almost every h∈D. This does NOT assert that it holds at every h for a selected x.

For any finite-density good x, m=p(x), translation of the a.e.-h statement gives p(y)>=bm for a.e. y∈x+D. Its integral is at least2bm and at most1. Therefore p(x)<=1/(2b) on a full-measure set, so the ESSENTIAL peak satisfies

    0<M=esssup p<=1/(2b)<infinity.

The positive lower bound M>0 follows from integral p=1. No attained maximum is needed. For every shrinking tolerance, the essential near-peak superlevel set has positive measure; intersect it with H and the full-measure sets where p is finite and p<=M. This supplies actual x_n with m_n=p(x_n)→M, without requiring their locations bounded, convergent or near zero.

For each such x_n the floor bm_n 1_(x_n+D) holds a.e. Thus

    q_n=p-bm_n 1_(x_n+D)

has EXACT mass alpha_n=1-2bm_n>=0 and cap0<=q_n<=M a.e. The cap is M, not m_n, and no unproved pointwise-peak replacement occurs. The countable family of a.e. statements suffices for the scalar inequalities and limit; no uniform-in-all-x shift version is required.

## 3. Sharp density-cap constant and translated diamond moment

For mass alpha and cap M, the comparison density q0=M 1_(B_R), R²=alpha/(pi M), has that exact mass. The pointwise product

    (|x|²-R²)(q-q0)>=0

holds inside and outside the disk because q<=M inside and q>=0 outside. Equal masses eliminate the R² term. If the moment of q is infinite the lower bound is automatic; otherwise all the subtractions used are integrable. The radial disk integral is

    M integral_(B_R)|x|²dx=M(pi/2)R⁴=alpha²/(2pi M).

This verifies the SHARP factor1/(2pi M), not a one-dimensional or square-cap constant.

For the diamond, area2, centroid0 and moment2/3 give

    integral_(x_n+D)|y|²dy=2/3+2|x_n|²>=2/3.

I rederive moment2/3 by integrating u² over a quadrant triangle, obtaining1/12, then adding the second coordinate and four quadrants. Crucially the translation term is nonnegative for EVERY x_n. Discarding it is valid even if the near-peak sequence escapes; no symmetry, mean-zero or location assumption on mu is used.

## 4. All-law finite-b lower bound and nonattainment limits

If J(mu)=infinity the bound is immediate. Otherwise split the actual nonnegative density into the translated floor and q_n. The previous two steps give

    J(mu)>=(2/3)b m_n+(1-2b m_n)²/(2pi M).

This is an actual inequality for EACH n. Passing to the finite scalar limit m_n→M requires no spatial convergence, compactness, dominated-convergence assertion for q_n, or attainment of the peak. It yields

    J(mu)>=(2/3)bM+(1-2bM)²/(2pi M)
          =1/(2pi M)+(2b/3+2b²/pi)M-2b/pi.

The arithmetic–geometric mean inequality for the first two positive terms is

    J(mu)>=2sqrt[(1/(2pi))(2b/3+2b²/pi)]-2b/pi
          =2sqrt[b/(3pi)+b²/pi²]-2b/pi.

This holds for every0<b<1 and every feasible law. Relaxing the allowed cap range M<=1/(2b) in this minimization only weakens a lower bound, so no unlicensed minimizer-domain assumption is hidden. The paper correctly does NOT claim finite-b attainability of all inequalities simultaneously.

Taking the infimum over ALL feasible Borel laws is therefore legitimate. Dividing this exact bound by sqrt(b) gives

    2sqrt[1/(3pi)+b/pi²]-2sqrt(b)/pi →2/sqrt(3pi),

which is the asserted unrestricted liminf. The lower bound is positive for b>0 because its square-root term exceeds b/pi.

## 5. Disk-core feasibility and exact normalization for every r

For any r>0, A_k=B_r+kD are compact, nested and exhaustive. The closed-set level index is Borel and finite. For EVERY h∈D, A_k+h⊂A_(k+1); applying the same implication with -h gives |n_r(x+h)-n_r(x)|<=1 pointwise. Thus the density b^n/Z has the FULL continuous-shift privacy condition, including boundary/corner points, once Z is finite and positive. This proof works even when B_r is not inside D; the prior SCDF source is used only to identify known mechanism ancestry in the asymptotic regime, not as a feasibility premise.

The layer identity

    b^n=(1-b)sum_(k>=0)b^k 1_(A_k)

is exact by geometric summation at every point with the chosen boundary convention. Tonelli then gives Z=E|A_G| and N=E M(A_G) BEFORE assuming finite moments. Nonnegative terms justify this step without a tail cutoff.

For k>0, the Euclidean parallel body of kD decomposes into its diamond, four outward edge strips and four circular vertex sectors, with disjoint interiors under the nearest-face/vertex decomposition. The diamond has area2k²; its four edges total length4sqrt2 k, so the strips have area4sqrt2 kr; the exterior angles total2pi, so sectors have area pi r². This is valid for all r>0, not just a thin offset. For k=0 the same formula is the direct disk area. Consequently

    |A_k|=2k²+4sqrt2 rk+pi r²,
    Z=pi r²+4sqrt2 rT1+2T2>=pi r²>0.

Every geometric T_j formula in(23) is finite for0<b<1, and T_j/b→1. No polygon-area clipping transition is unhandled here.

## 6. Full finite-b moment envelope, including the k=0 contribution

The leading disk-core moment is handled EXACTLY at k0:

    M(A0)=pi r⁴/2, multiplied by P(G=0)=1-b.

It would be invalid to substitute only the coarse diamond envelope at this core when claiming a sharp leading constant; the author does not do that. For k>=1, the valid containment B_r⊂sqrt2 rD yields

    A_k⊂(k+sqrt2 r)D,
    M(A_k)<=(2/3)(k+sqrt2 r)⁴.

I expand the fourth power independently:

    k⁴+4sqrt2 rk³+12r²k²+8sqrt2 r³k+4r⁴.

The first four terms sum with T4,T3,T2,T1 because positive powers vanish at k0. The last constant term sums only over k>=1 and therefore has factor P(G>=1)=b, NOT1. Thus

    N<=(1-b)pi r⁴/2
       +(2/3)[T4+4sqrt2 rT3+12r²T2+8sqrt2 r³T1+4r⁴ b].

All tails are included exactly in the T_j and tail probability b. This proves finiteness, so the proposed law is an actual normalized probability density with finite MSE. Division by Z>=pi r² and replacement1-b<=1 give exactly the finite envelope(26), for all b∈(0,1), r>0. The envelope is an upper bound, not an exact moment formula for every shell or an optimizer claim.

## 7. Matching powers and the sharp unrestricted constant

Put r=c b^(1/4), c=(4/(3pi))^(1/4). The core contribution to U/sqrt(b) is c²/2. The T4 contribution tends to2/(3pi c²). The remaining four terms after division are constants times

    (T3/b)b^(1/4), (T2/b)b^(1/2),
    (T1/b)b^(3/4), b,

respectively. I independently obtain these powers from the explicit r-factors in(26); each vanishes because T_j/b→1. No interchange of an unbounded shell series and an asymptotic limit is needed after the explicit finite envelope has been established.

Since c²=2/sqrt(3pi), the two limiting positive terms are EACH1/sqrt(3pi). The feasible family therefore gives limsup V_b/sqrt(b)<=2/sqrt(3pi). Combining with section4's all-law liminf proves the exact limit. The changing family mu_b is legitimate for bounding an infimum; an attained minimizer V_b is not required at any b.

Because b=e^(-epsilon), this is equivalently e^(epsilon/2)V(epsilon)→2/sqrt(3pi). The entire lower bound allowed nonsymmetric laws and nonzero means. The symmetric disk family is only a feasible upper construction, not a covert restriction on the lower feasible set.

## 8. Dependent all-gamma asymptotic reconstructed anew

For this section I freshly read the predecessor's exact formula and uniform lower-bound proof, not merely its review verdict. Layering the specific homothetic diamond family gives

    C_gamma=(1/3)E(G+gamma)⁴/E(G+gamma)²,

with T1..T4 as displayed in the new manuscript. Let a=b/(1-b), v=b/(1-b)², m=gamma+a. The central moments tau3=b(1+b)/(1-b)³>0 and tau4=b(1+7b+b²)/(1-b)⁴>=b yield E(G+gamma)⁴>=m⁴+b and E(G+gamma)²=m²+v. The exact square identity

    z²+b-2(sqrt(b)-v)(z+v)=(z+v-sqrt(b))²+v²

therefore gives C_gamma>=(2/3)(sqrt(b)-v) for EVERY gamma, including0 and1. Hence the optimized-family liminf is at least2/3 with no sampled optimizer.

For the upper limit choose the ACTUAL allowed gamma=b^(1/4)∈[0,1]. The numerator in(30)'s displayed formula has leading gamma⁴+T4=2b+o(b): the other terms are orders b^(7/4), b^(3/2), b^(5/4). Its denominator is sqrt(b)+o(sqrt(b)), since gamma T1 has order b^(5/4) and T2 order b. Thus C_gamma/sqrt(b)→2/3, bounding the minimum above and proving its exact limit.

Both limiting constants are positive. Their ratio is

    (2/3)/(2/sqrt(3pi))=sqrt(pi/3)>1.

This is a valid dependent observation, not a second independent discovery or a replacement for a finite-parameter counterexample.

## 9. Mechanism ancestry and acceptance limits

The arbitrary-core Minkowski-shell construction is PRIOR SCDF2013 mechanism class, with the author's mandatory provenance addendum retained. For sufficiently small b, sqrt2 r<1, the disk core lies in D and is coordinate-downward, so it fits that authenticated construction. Its inclusion does not supply an old global mixed-MSE optimality theorem; none is imported into this proof. The new candidate's potential delta is the measure-level finite-b bound and matching unrestricted leading constant, not invention of a shell mechanism or the bathtub principle.

This review does not certify that those precise constants/comparisons are novel, nor that the source screen is exhaustive. It establishes no exact finite-epsilon V, global finite-b minimizer, formal/kernel result or human acceptance. No verdict is inherited from the previous octagon review. No mathematical repair is requested at the checked pinned scope; parent review and source-priority disposition remain separate.

The bounded assignment is complete. I return to the ONE ordered-Olson primary, maintaining any currently operative parent review gate rather than treating this temporary review as another research slot.
