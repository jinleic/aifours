# LOCAL5 completion: every intrinsic C5 in a four-MOQLS(8) has real projector span at least eleven

**COMPLETE WRITTEN AUTHOR CANDIDATE CHAIN — NOT REVIEWED OR ADOPTED.** PhysicsMOQLS8-2. Actual clock observed before this addendum: Thu Oct 29 09:52:27 PDT 2026. This completes the LOCAL5>=11 target of the registered q4-span bridge, by excluding its final span-ten all-ray equality case. It does NOT complete LOCAL4>=10 or q4 exclusion. The required review unit is the WHOLE two-file union below; no earlier review covers this new conclusion.

## 1. Complete dependency boundary

The actual objects are an ordinary four-MOQLS(8) Q,X1,X2,X3, all original row/column ONBs and all six same-cell tensor-product ONBs. C is an intrinsic component of Q with complex span W of dimension FIVE. Each actual row and column meets C in a five-ONB, and there are 40 component cells. S is the real span of the component ray projectors and b=dim_R S. All phases and complex output frames remain arbitrary; no classical or tensor-product member is assumed.

This addendum consumes the ENTIRE new unreviewed predecessor `frontier-20261029-C5-span-ten-no-Lagrangian-ray-v1.md`, **115 LF / 15439 bytes**, SHA256 **d4a47f3456399fa9da42a36253e30e1b73b035b64c7c1e36808cf9547969444b**. That source supplies full proofs of the exact star identity, absence of isolated star rays, and the two-real-dimensional cross-image exclusion; its only adopted imports are GAP3 and the exact tested-qutrit span-five virtual-anchor module. A full review must reconstruct those proofs and every module caller, not assume the predecessor's headline as an accepted result.

Concretely the predecessor establishes, under b<=10, for EVERY actual component ray u:

    b=10, sigma_u=6, dim_R L_u=3,                          (EQ)

where sigma_u is the span of projectors of all actual component rays perpendicular to u, and L_u is the image of Z -> P_u Z P_(u-perp) written as {u chi*:chi in L_u}. It also establishes

    A_u := sum_{z in C, Q_z perpendicular to u} P_z >=5(P_W-P_u),

and the exact per-mate OFF-LINE identity, for every cell y with ray u,

    sum_{z in C off y's row/column, Q_z perpendicular to u}
          |<X_y,X_z>|^2 P_z = P_W-P_u.                    (EXACT)

For each distinct cell z the three mate weights are disjoint and their sum is at most one. Every actual component ray has m<=3 by adopted GAP3. In particular an actual star ray perpendicular to every other distinct ray of that star is impossible. The proof below uses EXACT, EQ and GAP3 at precisely these meanings.

## 2. A nonmonomial row/column pivot must exist

Suppose the unordered component ONBs of the row and column agree at EVERY component cell. Fix any component row basis E of five rays. Its five cells belong to five distinct original columns; at each of those cells the column's component basis would be E. Thus every E-ray occurs once in each of those five columns, giving multiplicity at least five, contrary to GAP3.

Hence choose an ACTUAL cell y with ray u where the row and column component ONBs differ. Removing their common ray u leaves two different actual four-ONBs E,F of the star space H=W intersect u-perp. By EQ the entire actual star-projector span T has dimension six and contains D_E, dimension four. Its off-diagonal space V relative to E has real dimension two.

For any two ONBs the intersection of their real diagonal Hermitian algebras has dimension equal to the number of connected blocks of the unitary transition. Indeed a Hermitian matrix diagonal in both bases has each F-vector as an eigenvector; nonzero E-coordinates of an F-vector must have the same diagonal eigenvalue. Propagating through the transition support gives one independent scalar per connected block. Thus a connected block of size k supplies k-1 independent off-diagonal directions.

A connected 4-block in F would supply three off-directions and is impossible. The remaining nonmonomial partitions are 3+1, 2+2, and 2+1+1.

## 3. A 3+1 pivot is impossible; 2+2 gives the desired split star

For a connected 3+1 transition, its two off-directions exhaust V on the three-coordinate block. Every actual star projector therefore has zero cross to the fourth axis. Rank-one purity puts every star ray in that three-space OR on the fourth axis, making the latter an isolated star ray. Contradiction.

For a 2+2 transition on orthogonal coordinate planes B,D, the two block off-directions exhaust V. Therefore EVERY actual star ray lies in B or D. Each plane carries its actual E and F two-ONBs, which are different unordered bases, and their projector span is three-dimensional. Thus

    H=B orthogonal-direct-sum D,  dim_C B=dim_C D=2,
    all actual u-inactive component rays lie in B or D,
    dim_R span{actual B-ray projectors}=dim_R span{actual D-ray projectors}=3.       (SPLIT)

## 4. The full 2+1+1 pivot case, using the EXACT weighted resolutions

Let B be the rotated coordinate two-plane in the transition and D the plane of the two unchanged actual axes g,h. The transition supplies a nonzero pure B-edge direction Z_B in V. Let X be the image of V under the B-D block-cross map. Since Z_B lies in its kernel and dim V=2, dim_R X<=1.

If X=0, every actual star ray lies in B or D. Neither plane can consist of only its two orthogonal axis rays: either such axis would then be an isolated star ray. Thus each plane contains at least three distinct rays, whose projectors have real span at least three. Since total star span is six, this again gives SPLIT.

Suppose X is one-dimensional. It has an actual rank-one generator b_0 d_0* because the star span is generated by actual projectors. Every actual star ray mixing B and D has B-part parallel to b_0 and D-part parallel to d_0. Every pure-D star projector has zero cross, so its off-part lies in ker(cross on V)=R Z_B and consequently has zero D off-part. Therefore the only possible pure-D star rays are the two axes g,h.

If d_0 is an axis, the other axis is perpendicular to all other actual star rays, an isolated star ray. If d_0 is NOT an axis, consider ANY positive weighted resolution of I_H using actual star projectors. Its D-compression consists of diagonal g,h contributions plus

    c P_d0,   c=sum_over_mixing_rays(weight times squared D-norm)>=0.

The D off-diagonal of P_d0 is nonzero. Since I_D is diagonal, c=0, so EVERY mixed ray has zero weight in such a positive resolution. The remaining pure-D terms then require total weight exactly one on g and exactly one on h.

Apply this fact to EACH of the THREE exact off-line resolutions in EXACT. At g-cells outside y's row and column the sum of each mate's weights is one. Their disjointness at every distinct cell and their upper bound one therefore require at least THREE such g-cells. But g already occurs once in y's actual row and once in y's actual column: both lines preserve g in this 2+1+1 transition, and these occurrences are different cells. Thus m(g)>=5, contrary to GAP3. The same holds for h.

This excludes the one-dimensional-cross case completely. Every possible nonmonomial pivot therefore yields SPLIT. Importantly, an unweighted star-cover inequality alone would NOT justify dropping the mixing rays here; the exact positive per-mate resolutions and their disjointness were essential.

## 5. The split star forces a forbidden tested two-plane

Fix the pivot u and planes B,D supplied by SPLIT. Let U be the collection of actual component cells with NONZERO u-overlap, and form the positive operator on H

    F = sum_{z in U} P_H P_z P_H.

All other component rays are perpendicular to u and lie in B or D. Since the full component resolution is 8P_W, their sum is B-D block diagonal, and hence F is B-D block diagonal too:

    F=F_B direct-sum F_D.

The range of F is the COMPLEX span of the vectors P_H Q_z, z in U. Each such vector lies in L_u after multiplication by a nonzero scalar from its u-overlap. As dim_R L_u=3, this complex span has dimension at most three. Therefore

    rank F_B + rank F_D <=3.

Neither block has rank zero. If F_B=0, every u-active ray has zero B-part and every other ray is in B or D, so B is orthogonal to every component ray outside it; this contradicts intrinsic irreducibility. The same applies to D. Since both are positive and nonzero on two-spaces, one has rank ONE. Without loss let rank F_B=1 with range C b_0. Positivity implies that EVERY actual u-active ray has B-projection parallel to b_0 (possibly zero). Every u-inactive ray outside B lies in D and has zero B-projection. Thus ALL actual component rays outside B have B-projection parallel to the same b_0.

By SPLIT, the actual pure-B projectors span three real dimensions, so there are at least three distinct pure-B rays. Choose one, w, which is neither b_0 nor its orthogonal ray. For any actual ray outside B that is perpendicular to w, its B-projection must be ZERO: a nonzero multiple of b_0 has nonzero inner product with w. Hence every such outside ray lies in B-perp, dimension three within W.

In an actual component five-ONB containing w the four other vectors cannot all lie in B-perp. Its unique in-plane B-partner w' is therefore ACTUAL. All other star-w rays lie in B-perp and are perpendicular to w'. Thus w' is an isolated star ray, which is impossible by the exact family star bound and GAP3.

This contradiction eliminates SPLIT, and hence eliminates b<=10 altogether.

## 6. LOCAL5 result and the unchanged q4 residual

The TWO-FILE WRITTEN candidate chain proves:

**Every intrinsic five-dimensional component of every member of every ordinary four-MOQLS(8) has real projector span at least ELEVEN.**

This is a local necessary bound in arbitrary complex physical families. It is not a construction, formal/kernel proof, independent-family result, novelty clearance or parent adoption. The predecessor's virtual-anchor-module import remains explicit; its load-bearing dependencies have not disappeared merely because the final contradiction is elementary.

In the q4 bridge, combine this candidate with the separate LOCAL4>=9 candidate and the adopted 53 span-sum budget ONLY AFTER the entire relevant proofs are reviewed. C5-type nonclassical members then have span at least 14, while only C4-type members with b=9 plus four fixed rays can have span 13. Therefore any putative q4 family would need at least THREE C4-type members of span 13, and the fourth member would have span at most 14. The b9 C4 PRODUCT stratum is separately excluded by `frontier-20261029-C4-product-component-exclusion-v1.md` (bfb192d7...), but an arbitrary b9 C4 has not been shown product or excluded. **q4 remains OPEN; LOCAL4>=10 remains OPEN.** Families containing a classical member and the full original four-family alternative are not settled by this local improvement.

A10 stays GB15/18, with literal P1-B2.M2, P1-B2.M4, P1-B3.M2 UNKNOWN; A11 stays OPEN. No heavy/multi-GB attempt, scientific interpreter, selected numerical probe, model CLI or nested agent was used. All earlier frozen files and process/cadence disclosures remain immutable. Required full review: the predecessor's entire L2-exclusion/module caller, every pivot partition, the weighted-resolution argument at 2+1+1, positivity/rank additivity in Section 5, and the exact global-budget caller. No claim of review or adoption follows from this author record.
