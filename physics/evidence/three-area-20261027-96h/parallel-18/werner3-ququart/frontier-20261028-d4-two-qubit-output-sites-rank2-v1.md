# Original q3≥0 for rank≤2 with two 2D local output supports

**PhysicsResearch96h-2 / physics-1. WRITTEN all-variable proof; UNREVIEWED.** This is a source-independent positive result for a strictly larger original-target subclass than the 2×2×2 output-support exact square. It is not a proof for every original rank≤2 C, a global equality classification, a source-certificate/novelty claim, or parent/f62/f153/human/family/formal/Lean/physical-operational acceptance.

## 1. Original-domain statement

Let `H=(C⁴)^tensor3`. Choose any two distinct sites, labeled 1 and2, and arbitrary two-dimensional subspaces `E_1,E_2⊂C⁴` with orthogonal projections P_1,P_2. If C:H→H is any complex operator of rank≤2 satisfying

`(P_1⊗P_2⊗I_3) C=C`,                                                 (1)

then the original unnormalized-trace functional satisfies

`q3(C) >= 0`.                                                         (2)

No support restriction is made on site3, the input legs, Hermiticity, positivity or product structure. Local output support of dimension0 or1 is included by extending it to a 2D E_i. Since q3(C)=q3(C†), the same conclusion holds when the corresponding **input** supports at any two distinct sites have dimension≤2.

The 2×2×2 supported result `frontier-20261028-d4-qubit-output-support-exact-sos-v1.md`, SHA256 `83fd1683c2b81957406f55a8ac1f1f932dfdd555ad99c23b7ded752a4738654a`, needs no rank bound and provides an exact projection-square/equality space; the present theorem drops its support restriction at site3 but uses rank≤2. Neither result implies (2) for a generic original rank2 C, whose local output and input supports can exceed2 at all sites.

## 2. Original q3 as a tensor quadratic form

Use the canonical vectorization `vec C=Σ_(x,y) C_xy |x>⊗|bar y>` and regroup the output/input copies by site. On `V_i⊗bar V_i`, `V_i=C⁴`, define

`|Ω_i>=Σ_(j=0)^3 |e_j>⊗|bar e_j>`,
`K_i=I−(1/2)|Ω_i><Ω_i|`.

Direct expansion of the eight subsets gives the exact original identity

`q3(C)=<vec C,(K_1⊗K_2⊗K_3) vec C>`.                              (3)

For one local matrix X this is `<vec X,K_i vec X>=||X||HS²−|Tr X|²/2`. No restriction of the original trace convention is made. The vector |Ω_i> is an identity-operator tensor, not a selected physical target state.

By (1), vec C is supported on E_1,E_2 in the first two output factors. Consequently (3) is unchanged when K_i for i=1,2 is compressed to `E_i⊗bar V_i`:

`L_E=(P_E⊗I) K (P_E⊗I)=P_E⊗I−(1/2)|Ω_E><Ω_E|`,
`|Ω_E>=Σ_(a=1)^2 |e_a>⊗|bar e_a|`,                                  (4)

where e_1,e_2 is any orthonormal basis of E.

## 3. The compressed qubit factor is separable, explicitly

For every 2D E⊂V, normalized Haar measure on the unit sphere of E gives

`L_E = 3∫_(u∈S(E)) |u><u|⊗|bar u_perp><bar u_perp| dμ(u)`
`      + P_E⊗(I−bar P_E)`.                                          (5)

Here u_perp is any unit vector in E orthogonal to u; its phase does not affect its projector. The second term is a finite sum of rank-one positive product operators in arbitrary orthonormal bases of E and E-perp, so (5) is a positive product decomposition on output⊗conjugate-input.

To derive (5), unitary invariance and the dimension3 symmetric subspace of E⊗E give

`∫ |u><u|^tensor2 dμ=(I+F_E)/6`.

Partial transposition of the second factor in a fixed orthonormal E basis yields

`∫ |u><u|⊗|bar u><bar u| dμ=(P_E⊗bar P_E+|Ω_E><Ω_E|)/6`.

Also `∫ |u><u|=P_E/2` and `|bar u_perp><bar u_perp|=bar P_E−|bar u><bar u|`. Thus

`3∫ |u><u|⊗|bar u_perp><bar u_perp|`
` = P_E⊗bar P_E−(1/2)|Ω_E><Ω_E|`,

and adding the E-perp term gives (5). This is an exact ordinary Haar/swap identity, not a numerical or selected-target calculation.

## 4. Every remaining one-site contraction has rank≤2

Expand the product of (5) on sites1 and2 into its positive continuous and finite product terms. Each term has the form

`|u_1><u_1|⊗|bar v_1><bar v_1|` on site1 and
`|u_2><u_2|⊗|bar v_2><bar v_2|` on site2,

with positive weight; v_i is either u_i-perpendicular inside E_i or an E_i-perpendicular basis vector from the finite term. Its contribution to (3) is

`<vec X,K_3 vec X> = ||X||HS²−|Tr X|²/2`,                           (6)

where the actual one-site matrix is

`X=(<u_1 u_2|⊗I_3) C (|v_1 v_2>⊗I_3)`.

Since left/right multiplication cannot increase rank, `rank X≤rank C≤2`. The trace/singular-value inequality then gives `|Tr X|≤sqrt(2)||X||HS`, so (6) is nonnegative for every term. Integrating/summing positive weights proves (2). This uses the **same C** for all contractions, not independently chosen local witnesses.

The reasoning yields a precise but implicit equality criterion in this class: q3(C)=0 iff every such X, for every continuous frame and every finite E-perp term at both sites, is either zero or a scalar multiple of an orthogonal rank2 projection. Necessity follows from nonnegative summands, continuity and full Haar support; sufficiency follows by (6). The rank≤2 equality characterization is the usual equality case of the trace/singular-value inequalities. This is not a parametrization of those C or a global equality classification.

## 5. Trust and process boundaries

The proof uses original q3/vectorization, a named elementary Haar identity, rank monotonicity and singular-value inequalities only. It has no dependency on the public-source certificate, corrected multipliers, a selected physical target value or the elected HELD/ZERO/NONINPUT episode/guidance. The local product decomposition is a support-conditional analytic representation, not an unrestricted polynomial-SOS in arbitrary rank2 factors and not a contradiction to the parent-adopted unrestricted-factor no-go. The prior public full-target Werner claim retires new-discovery status; no literature-exhaustiveness or novelty claim is made. Frozen f153/f62, historic process/held findings, and independent-review/formal/human/operational boundaries remain unchanged.
