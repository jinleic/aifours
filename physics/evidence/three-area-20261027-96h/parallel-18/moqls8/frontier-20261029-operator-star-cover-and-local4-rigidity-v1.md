# Operator star cover, full neighbour span in C4, and the exact span-nine residual

**SELF-CONTAINED WRITTEN AUTHOR CANDIDATE — UNREVIEWED.** PhysicsMOQLS8-2. Actual clock observed before writing: Thu Oct 29 09:24:33 PDT 2026. This supplies a stronger operator form of the three-mate frame inequality, a new full-neighbour-span restriction, and a shorter proof of LOCAL4>=9. It does NOT prove LOCAL4>=10, LOCAL5>=11, q4 exclusion, four-family classicality, existence, a numerical M(8), or A10/A11. No scientific program or arithmetic interpreter was used for these derivations. Same-harness written mathematics is not formal, human, configured-family, executable or novelty acceptance.

## 1. Actual objects and the sole imported theorem

Q,X1,X2,X3 are four ordinary MOQLS of order 8: four arrays of unit vectors in C^8, every actual row and column an ONB, and for every pair of distinct members M,N the 64 same-cell tensor products form an ONB. Thus for distinct cells y,z, `<M_y,M_z><N_y,N_z>=0`. Write P_y=|Q_y><Q_y|. Rays are unit vectors modulo phase; m(v) counts ALL occurrences of ray v in Q.

Let C be an intrinsic component of Q, namely a connected component of the non-orthogonality graph on its cells. Its complex span W has dimension r. Distinct components are orthogonal; every actual row and column meets C in an ONB of W. Indeed, each row resolves I, all its rays lie in mutually orthogonal component spaces, and compression to W gives an ONB of W. Put S=span_R{P_y:y in C}, b=dim_R S.

**Only imported theorem: GAP3.** Every ray in an intrinsic component of dimension at least two has m(v)<=3. This is Gate 1 of the adopted prior-round disposition `institute/runs/three-area-2026-10-23-96h/MOQLS-unrestricted-four-family-ray-gap-intrinsic-and-local-span-budget-entire-parent-v1.md`, SHA256 `2e254b56d108994844cf337c31b98fa851effca15a68a847c6cb2db84552bee4`. No C2/C3, LOCAL4/5/6 or global budget theorem is used to prove Sections 2–5.

For an actual ray u in C, its *star* is the set of all component rays perpendicular to u, with all their original cell occurrences retained. Its projector span has real dimension sigma_u. An isolated star ray g means that g is perpendicular to every other distinct ray of this star; it does NOT mean that g is an intrinsic component of Q.

## 2. The exact per-mate operator identity and five-fold star cover

For a cell y and a mate X define O(y) to be the cells z distinct from y, outside y's row and column, with Q_z perpendicular to Q_y. Define w_X(y,z)=|<X_y,X_z>|^2. Taking the partial matrix element along X_y in the ACTUAL tensor-ONB resolution gives

    sum_z w_X(y,z) P_z = I_8.

The term z=y is P_y. Other cells in y's row or column have zero X overlap. At any remaining z with nonzero Q overlap, Q–X product orthogonality forces the X overlap to vanish. Consequently

    sum_{z in O(y)} w_X(y,z) P_z = I_8-P_y.                 (OSC-1)

For distinct mates X,X', their product orthogonality implies w_X(y,z) w_X'(y,z)=0 whenever z!=y. Each weight lies in [0,1]. Hence omega(y,z)=sum_X w_X(y,z)<=1. Summing (OSC-1) over the three mates yields both the exact weighted resolution and the positive-semidefinite inequality

    sum_{z in O(y)} omega(y,z) P_z = 3(I_8-P_y),
    sum_{z in O(y)} P_z >= 3(I_8-P_y).                    (OSC-2)

These hold at EVERY cell; unlike a derivation which divides by |<a,Q_y>|^2, there is no active-cell assumption. Evaluating the second identity at any unit a gives the three-mate frame inequality also at zero-weight cells.

Now take y in C with ray u and compress to W. Projectors of other components vanish. The star cells in y's actual row form an ONB of W intersect u-perp and sum to P_W-P_u; the star cells in y's column give another such sum. These two cell sets are disjoint. Adding them back to (OSC-2) gives

    A_u := sum_{z in C, Q_z perpendicular to u} P_z
           >= 5(P_W-P_u).                               (OSC-3)

Equivalently, if T_u sums projectors over all cells of C having NONZERO overlap with u, then, because sum_{z in C}P_z=8P_W,

    T_u <= 3P_W+5P_u,       # {u-active cells in C} <= 3r+5.       (OSC-4)

The count is the trace of this operator inequality, not a new ray-multiplicity claim. In particular, an isolated star ray g would satisfy m(g)=<g,A_u g>>=5, contradicting GAP3. Thus **no star of a nontrivial component has an isolated ray**.

## 3. A low-dimensional star-span bound, with its needed justification

For r>=4, set d=r-1>=3. An actual row through u supplies an ONB E=(e_1,...,e_d) of W intersect u-perp, so its diagonal projector space D_E is contained in the star span. We prove

    sigma_u >= d+2 = r+1.                               (OSC-5)

Suppose instead that the off-diagonal image of the star span relative to E has dimension at most one. If it is zero, every star ray is an E-axis and A_u<=3 I_d by GAP3, contradicting (OSC-3). Otherwise choose an actual non-axis star ray v generating the one real off-diagonal direction X=Off_E(P_v). Every non-axis star ray w satisfies Off_E(P_w)=tX for a nonzero REAL scalar t.

If v has support two, the same off-support forces every non-axis w into that same coordinate two-plane. Each of the other d-2 actual E-axes is then an isolated star ray, already impossible. If v has support k>=3, w has the identical support. For any supported coordinate i choose two other supported coordinates j,k. Rank-one purity gives

    |w_i|^2 = (w_i conjugate(w_j)) (w_k conjugate(w_i)) / (w_k conjugate(w_j))
             = t |v_i|^2.

Thus t>0 and unit normalization gives t=1, so P_w=P_v. The entire star consists of E-axis rays and this one further ray v. For a unit xi perpendicular to v, the axis contributions to <xi,A_u xi> are at most 3 and the v contribution is zero, contradicting (OSC-3). This proves (OSC-5).

**Important scope clarification.** A star is not automatically a union of complete ONBs, so a bare appeal to the intrinsic-component 2d-1 theorem would NOT justify a star-span bound. The 09:21 checkpoint's C4/C5 bounds are justified by the explicit one-off-direction argument here together with (OSC-3), not by such an appeal. In particular sigma_u>=5 in C4 and sigma_u>=6 in C5.

## 4. Full neighbour span in an intrinsic C4

**Theorem.** If C has dimension four, then for EVERY actual ray u its u-active component rays complex-span ALL of W.

They contain u and some mixed ray, since otherwise u would be an isolated intrinsic component. Suppose their complex span A is proper. If dim A=2, write A=span(u,lambda). For any actual mixed ray x in A, the u-active ray perpendicular to x can only be its in-plane partner x'. Every u-inactive ray perpendicular to x lies in A-perp. In any actual line through x the other three ONB vectors cannot all lie in the two-space A-perp, so x' is actual and is in every line through x. It is perpendicular to all other star-x rays, an isolated star ray. This contradicts Section 2. The case dim A=1 was already excluded.

It remains to exclude dim A=3. Let Pi=A intersect u-perp (dimension two) and let pi be a unit vector of W perpendicular to A. Every mixed u-active ray has representative u+r lambda with lambda a unit direction in Pi and r!=0; a pi-active ray is necessarily u-inactive. For such x, any pi-active ray perpendicular to x lies in

    K_lambda = span(u,lambda)-perp within W
             = C pi + (Pi intersect lambda-perp).

Evaluating (OSC-3) for x along pi shows that the TOTAL pi-weight of actual Q cells with ray in K_lambda is at least 5. Three different projective lambda directions give three K-planes which pairwise intersect in C pi. Their pi-active cells are disjoint except for actual pi occurrences. Since the total pi-weight of all component cells is 8, while m(pi)<=3 if pi is actual and is zero otherwise, three such directions would imply

    15 <= 8+2m(pi) <= 14.

Therefore at most TWO projective lambda directions occur. Exactly two, lambda_1 and lambda_2, are needed to span A. Write B_i=span(u,lambda_i), so every u-active ray lies in B_1 or B_2.

Every actual line not containing u has at least two u-active rays. It cannot have three: two would lie in one B_i, and being orthogonal would span B_i, leaving all remaining line rays u-inactive. With exactly two, the expansion of u in that actual ONB puts u in their span, so their Pi projections are parallel and they lie in the SAME B_i. Thus they are an in-plane ONB pair. In particular the in-plane orthogonal partner of EVERY actual mixed B_i-ray is actual.

Let kappa=<lambda_1,lambda_2>, with |kappa|<1. For any actual mixed x in B_1 its B_1 partner x' is actual. All u-inactive rays perpendicular to x lie in K_lambda1 and are perpendicular to x'. If there were no mixed B_2 ray perpendicular to x, then x' would be an isolated star-x ray, impossible. Hence kappa!=0, and the unique B_2 ray perpendicular to x is actual. The same assertion holds after exchanging B_1 and B_2.

We now use only these two closure rules on the FINITE actual ray set: in-plane partners and cross-plane orthogonal partners. Represent x by u+r lambda_1, r!=0. Its cross-plane partner has B_2 ratio s=-1/(kappa conjugate(r)). That ray's in-plane partner has ratio s'=-1/conjugate(s)=conjugate(kappa) r. Its cross-plane B_1 partner has ratio t=-1/(conjugate(kappa) conjugate(s'))=-1/(|kappa|^2 conjugate(r)). Finally the in-plane partner has B_1 ratio

    r_new=-1/conjugate(t)=|kappa|^2 r.

All four rays in this chain are actual and mixed. Since 0<|kappa|^2<1, applying the chain to a B_1 mixed ray of minimum positive |r| gives a strictly smaller positive |r|, contradicting finiteness. This excludes dim A=3 and proves the theorem. No numerical state, chosen parameter value or executed orbit is used.

## 5. LOCAL4>=9 and the exact all-ray conditions at equality

For any actual u, consider the real-linear map Z -> P_u Z P_(u-perp) on S and write its image as {u chi*:chi in L_u}. Its kernel contains RP_u and the entire star span, in direct sum, so

    b >= 1+sigma_u+dim_R L_u.                            (OSC-6)

The image is generated by the crosses of actual u-active projectors. The full-neighbour-span theorem implies that their u-perp projections complex-span the three-space W intersect u-perp, hence dim_R L_u>=3. Section 3 gives sigma_u>=5. Consequently **b>=9** without the complex-pencil case analysis of the earlier 9d20ed1a packet.

If b=9, EVERY actual ray u simultaneously satisfies

    sigma_u=5,   dim_R L_u=3,   span_C L_u=W intersect u-perp,
    S intersect BD_u = RP_u direct-sum span_R{P_v:v perpendicular to u}.

Thus the span-nine residual has no deficient-neighbour-span ray, no star with one off-diagonal direction, no isolated star ray, and no unused block-diagonal dimension. In C5 with b=10, the present tools give sigma_u>=6 and dim_R L_u>=2 (the usual closed-plane/star-isolation argument); the only possible pairs are (sigma,dim_R L)=(6,2),(6,3),(7,2). No one of these pairs is excluded here.

## 6. Exact remaining original-target gap

The registered q4 bridge uses the ADOPTED all-four-nonclassical sum-of-spans bound 53 and the adopted component exclusions/bounds. Inserting LOCAL4>=9 leaves at least three members of span 13, of type C4 with b=9 plus four fixed rays OR C5 with b=10 plus three fixed rays; a fourth member has span at most 14. This arithmetic consequence is conditional on fresh review of the new LOCAL4 result. It does not close q4.

The missing implication is now precise: exclude an intrinsic C4 with b=9 and ALL the equality conditions of Section 5, and exclude an intrinsic C5 with b=10, or supply a coupled actual-family obstruction for the resulting low-span members. The operator cover is a necessary identity on the ACTUAL same-cell tensor ONBs, not an assertion that arbitrary star-cover data glue into mates. A10 stays GB15/18 with literal P1-B2.M2, P1-B2.M4, P1-B3.M2 UNKNOWN; A11 stays OPEN. No multi-GB or heavy attempt was made. Earlier immutable packets and all process/cadence disclosures remain unchanged. Review must reconstruct the complete operator identity, one-direction cone, finite closure and equality caller before any adoption.
