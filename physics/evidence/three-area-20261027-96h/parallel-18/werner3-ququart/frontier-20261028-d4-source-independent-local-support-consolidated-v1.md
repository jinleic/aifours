# Source-independent q3 on local two-dimensional supports: consolidated packet

**PhysicsResearch96h-2 / physics-1. WRITTEN all-variable mathematics; UNREVIEWED.** This packet consolidates the source-independent local-support and nonproduct-equality line for a prospective single review. It proves a full original-q3 inequality on a precisely restricted but nontrivial rank≤2 subclass, an exact square on an independent higher-rank supported class, and explicit nonproduct equality families. It is **not** a proof for all original rank≤2 C, a global equality classification, a novelty claim, a parent/f62/f153/human/family/formal/Lean acceptance, or a physical-operational result. It does not change any frozen review scope or the pause on new source-conditional variants.

## 1. The original functional and the strongest supported rank≤2 theorem

On `H=(C⁴)^tensor3`, with unnormalized partial traces, let

`q3(C)=||C||HS²−(1/2)Σ_i||Tr_i C||HS²+(1/4)Σ_(i<j)||Tr_ij C||HS²−(1/8)|Tr C|²`.

Choose **two distinct physical sites**. At each of those two sites, independently choose either its local **output** leg or its local **input** leg. Suppose C:H→H is an arbitrary complex operator of rank≤2 such that the chosen local leg at each of those sites has support dimension at most2. Equivalently, after extending each support to a 2D subspace E_i with projection P_i, impose at the selected sites either `(P_i on output) C=C` or `C (P_i on input)=C`. No support constraint is made on the third site or on either unselected leg. Then

`q3(C) >= 0`.                                                         (1)

The theorem includes two output supports, two input supports, and a **mixed output/input** choice at different sites. All local factors and C may be complex and non-Hermitian. General rank2 C can have all six local input/output supports larger than2, so this is not the full original target.

The proof gives an exact implicit equality condition: the partial contractions X defined in §4 must all be zero or scalar multiples of orthogonal rank2 projections. This is an iff on the stated supported class, not a global classification.

## 2. Original q3 vectorization and two explicit separable compressions

Write `vec C=Σ_(x,y) C_xy |x>⊗|bar y>`, regrouped by physical site. With `|Ω_i>=Σ_(j=0)^3 |e_j>⊗|bar e_j>` and `K_i=I−|Ω_i><Ω_i|/2`, direct expansion of the original eight partial-trace terms gives

`q3(C)=<vec C,(K_1⊗K_2⊗K_3) vec C>`.                              (2)

In particular `<vec X,K_i vec X>=||X||HS²−|Tr X|²/2`. The |Ω_i> are fixed identity tensors, not selected target states.

For any two-dimensional E⊂C⁴ with projection P and `|Ω_E>=Σ_(a=1)^2 |e_a>⊗|bar e_a>`, the output-leg compression is

`L_E^out=P⊗I−|Ω_E><Ω_E|/2`
` = 3∫_(u∈S(E)) |u><u|⊗|bar u_perp><bar u_perp| dμ(u)`
`   + P⊗(I−bar P)`.                                                 (3)

The input-leg compression is independently

`L_E^in=I⊗bar P−|Ω_E><Ω_E|/2`
` = 3∫_(u∈S(E)) |u_perp><u_perp|⊗|bar u><bar u| dμ(u)`
`   + (I−P)⊗bar P`.                                                 (4)

Haar measure on the E unit sphere is normalized; u_perp is any unit orthogonal companion, whose phase is immaterial. The finite remainders are sums of rank-one positive product operators using any orthonormal bases of E and E-perp. Thus both (3) and (4) are exact positive product decompositions on the relevant output⊗conjugate-input local space.

Proof: unitary invariance gives `∫|u><u|^tensor2=(I+F_E)/6`, since the two-qubit symmetric subspace has dimension3. Partial transpose of the second factor yields

`∫|u><u|⊗|bar u><bar u|=(P⊗bar P+|Ω_E><Ω_E|)/6`.

Also `∫|u><u|=P/2` and `|u_perp><u_perp|=P−|u><u|`. Substitution separately proves (3) and (4), including the finite complementary-input or complementary-output term. These are ordinary Haar/swap facts, not numerical target-state probes.

## 3. Proof of (1), preserving the original rank bound

Apply the appropriate compression (3) or (4) at each selected site. Expand their positive product decompositions, keeping the **same original C** in every term. For any positive rank-one local factors `|a_i><a_i|⊗|bar b_i><bar b_i|` at the first selected site and analogously at the second, the remaining site's contribution is

`<vec X,K_3 vec X>=||X||HS²−|Tr X|²/2`,                            (5)
`X=(<a_1 a_2|⊗I_3) C (|b_1 b_2>⊗I_3)`.

The form of a_i,b_i depends on which of (3),(4) was used; in every case (5) is the same actual left/right contraction. Rank cannot increase under multiplication, so `rank X≤rank C≤2`, and

`|Tr X| <= sum of its singular values <= sqrt(2)||X||HS`.

Thus every term (5) is nonnegative, and the positive finite sums/integrals prove (1). No independently selected local moments or rank witness is substituted for C.

Moreover, equality in (1) holds exactly when every such X vanishes or is a nonzero scalar multiple of an orthogonal rank2 projection. This follows from the equality case of the singular-value inequalities, nonnegative summands, continuity and full Haar support; the finite terms must vanish individually. This is an exact **implicit** iff for the stated supported class, not an explicit parameterization or a global equality claim.

## 4. Exact square for 2×2×2 support without a rank assumption

Choose arbitrary two-dimensional local output spaces E_i at all three sites and let P_i be their orthogonal projections. On `L_E={X:(P_1⊗P_2⊗P_3)X=X}`, define

`D_i^E(X)=P_i⊗Tr_i X`, `R_i=Id−D_i^E/2`.

The input legs of X are unrestricted. Each D_i^E is Hilbert–Schmidt self-adjoint on L_E because `<X,D_i^E Y>=<Tr_i X,Tr_i Y>`; `(D_i^E)²=2D_i^E`, and the three commute. Therefore the R_i are commuting orthogonal projections. For every C∈L_E,

`q3(C)=<C,R_1R_2R_3 C>HS=||R_1R_2R_3 C||HS² >=0`.                 (6)

The first identity follows by expanding all eight subsets and using `<C,(Π_(i∈S)D_i^E)C>=||Tr_S C||²`. Its exact equality space is

`ker(R_1R_2R_3)=ker R_1+ker R_2+ker R_3`,
`ker R_i={P_i⊗X_i: remaining output supports lie in their E_j}`.       (7)

The sum need not be direct. This is the complete equality subspace **within L_E**, before imposing any rank bound; intersecting it with rank≤2 gives the exact supported original-rank equality set. The analogous all-input-support result follows by applying (6)–(7) to C†, since q3(C†)=q3(C). Dimension≤1 at any local leg is handled by an arbitrary 2D extension. The fixed support-dependent square is not an unrestricted polynomial-SOS on arbitrary rank2 factors and does not contradict the parent-adopted unrestricted-factor no-go.

## 5. Explicit original nonproduct equality families

Let `u=⊗u_i`, `v=⊗v_i` be arbitrary normalized product vectors, with `t_i=|<u_i,v_i>|²`, and `P_u=|u><u|`, `P_v=|v><v|`. For every complex α,β, direct product trace expansion gives

`q3(αP_u+βP_v)=(|α|²+|β|²)/8+2 Re(α conjugate(β)) Π_i(t_i−1/2)`
`                  >= (|α|−|β|)²/8`.                                 (8)

For nonzero αβ, equality holds iff every t_i is0 or1, and α=β when the number k of t_i=0 is odd, α=−β when k is even. If k=0 this gives C=0. If k=1 it is a product-operator equality. If k=2, `C=α(P_u−P_v)` is nonproduct; if k=3, `C=α(P_u+P_v)` is nonproduct. For each nonzero case α arbitrary, the two vectors are globally orthogonal and C has rank2. For k≥2 a cut through one orthogonal site leaves linearly independent local projectors on both sides, proving operator Schmidt rank2. Thus product operators do **not** exhaust the full original q3 equality set. No selected numerical target state, full equality classification or novelty claim is made.

Equation (8) follows since `q3(P_u)=q3(P_v)=1/8` and the original cross coefficient is `Π_i(t_i−1/2)`. The inequality uses `|t_i−1/2|≤1/2` and `|Re(α conjugate β)|≤|α||β|`; equality forces all factors to attain their extrema and the stated relative phase. This completely classifies equality only within the two-product-projector class.

## 6. What remains, and provenance

The unrestricted rank≤2 target remains unproved by this packet: no available argument here covers generic C with no two 2D local support legs. The above exact support-dependent positive representations are unrelated to an unrestricted-factor polynomial certificate. The known public full-target Werner claim retires new-discovery status but is not correctness-accepted by this packet. All results use only the original trace functional, elementary local vectorization/Haar identities, rank monotonicity and singular-value inequalities; no source-certificate premise, chosen numerical target q3 value, elected HELD/ZERO/NONINPUT episode or guidance is used. Historical process/held findings and the frozen f153/f62 review boundaries remain unchanged.
