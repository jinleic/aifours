# No intrinsic C4 component can consist of product rays in one common 2-by-2 factorization

**SELF-CONTAINED WRITTEN AUTHOR CANDIDATE — UNREVIEWED.** PhysicsMOQLS8-2. Actual clock before writing: Thu Oct 29 09:37:37 PDT 2026. This excludes a continuous tensor-product stratum of the C4 span-nine residual, and in fact does not require any projector-span bound. Both local factors and all phases may be complex. This is NOT an assertion that every C4 span-nine cone has this factorization; that classification is unproved. The unrestricted b=9 and C5 b=10 targets, q4 and the original four-family alternative remain OPEN.

## 1. Original setting, exact hypothesis and one imported theorem

Q,X1,X2,X3 are ANY four ordinary MOQLS of order 8: all actual row/column ONBs in C^8 and all six actual 64-dimensional same-cell pair-product ONBs. For distinct cells y,z and distinct members M,N, `<M_y,M_z><N_y,N_z>=0`. Let C be an intrinsic irreducible component of Q with complex span W of dimension FOUR. Each of the eight actual rows and eight actual columns meets C in four cells forming an ONB of W; there are exactly 32 component cells. S is the real span of their rank-one projectors, but its dimension is not restricted.

The stratum hypothesis is the existence of ONE fixed unitary identification W=C^2 tensor C^2 under which EVERY actual component ray is a simple product p_z tensor q_z of unit local vectors. The identification may be virtual and is chosen only once for this component; it is not a per-cell refactorization. No product structure on any mate or on W-perp is assumed.

**Sole import: GAP3**, every ray in a nontrivial intrinsic component of every four-MOQLS(8) has global multiplicity at most 3. Source: Gate 1 of `institute/runs/three-area-2026-10-23-96h/MOQLS-unrestricted-four-family-ray-gap-intrinsic-and-local-span-budget-entire-parent-v1.md`, SHA256 `2e254b56d108994844cf337c31b98fa851effca15a68a847c6cb2db84552bee4`. Sections 2–6 reprove all other used facts. In particular no general tensor-classification theorem, old solver outcome, catalogue, all-light theorem or unreviewed local-span bound is an input.

## 2. Five-fold star cover from the three actual mates

Put P_z=|Q_z><Q_z|. For each cell y and mate X, evaluate the X-factor of the complete Q-X tensor resolution along X_y. After removing z=y, row/column ONBs and product orthogonality leave exactly

    sum_{z outside y's row/column, Q_z perpendicular to Q_y}
        |<X_y,X_z>|^2 P_z = I_8-P_y.

At each distinct z, at most one of the three mate weights is nonzero, by the three mate-pair product ONBs, and each weight is at most one. Summing and compressing to W gives an unweighted projector sum at least 3(P_W-P_y) on the off-line component star. The star cells in y's row and y's column give two disjoint actual ONBs of W intersect Q_y-perp, each summing to P_W-P_y. Adding them back proves

    A_y := sum_{z in C, Q_z perpendicular to Q_y} P_z >= 5(P_W-P_y).       (P-STAR)

An actual ray g in this star which is perpendicular to every other distinct star ray would satisfy `<g,A_y g>=m(g)>=5`, contradicting GAP3. Thus no such isolated star ray can occur. This is the only family-level inequality used below.

## 3. Every two-by-two product ONB has a split factor

Every product ONB of C^2 tensor C^2 has at least one of these forms, as unordered rays:

    A-split: {a tensor b, a tensor b-perp,
              a-perp tensor c, a-perp tensor c-perp};
    B-split: {a tensor b, a-perp tensor b,
              c tensor b-perp, c-perp tensor b-perp}.

Here a-perp denotes its unique orthogonal local ray; all choices are arbitrary complex ones. The direct rectangular basis has BOTH forms and is not discarded or assigned an exclusive type.

Proof: start with u=a tensor b in the ONB. Each of the other three rays is perpendicular to u, so its first factor is a-perp OR its second factor is b-perp. At least two satisfy the same alternative. If two have first factor a-perp, their second factors are orthogonal and span C^2, so these two rays form an ONB of a-perp tensor C^2. Their two-dimensional orthogonal complement is a tensor C^2 and contains u and the remaining ray a tensor b-perp. This is A-split. Two with second factor b-perp give B-split in the same way. Rays satisfying both alternatives may be counted in either, and the pigeonhole still holds. This proves the classification without a real-form assumption.

Call {a,a-perp} an *A splitting basis* when some ACTUAL component row/column has the displayed A-split form. Define B splitting bases analogously.

## 4. A splitting basis consumes at least twenty actual component cells

For a local first-factor ray a let N_A(a) count all component cells whose first factor is exactly a projectively. Suppose an actual A-split basis as in Section 3 occurs. Apply (P-STAR) to the actual ray u=a tensor b and test it along the unit v=a-perp tensor b, which is perpendicular to u.

A product ray p tensor q perpendicular to u has p=a-perp OR q=b-perp. In the second alternative its overlap with v is zero unless it also belongs to the first, in which case the same formula still gives zero. Therefore the entire tested star sum is

    sum_{z with p_z=a-perp} |<b,q_z>|^2 >= 5.

Apply the same argument to the actual ray a tensor b-perp, tested along a-perp tensor b-perp. Adding the two inequalities and using the local ONB {b,b-perp} gives N_A(a-perp)>=10. The other two actual rays a-perp tensor c and a-perp tensor c-perp similarly give N_A(a)>=10. Thus

    N_A(a)+N_A(a-perp) >= 20.                           (P-A)

Two DIFFERENT unordered ONBs of C^2 share no ray. Consequently two different A splitting bases would require at least 40 disjoint component cells, whereas there are only 32. Hence **there is at most ONE A splitting basis among ALL sixteen actual lines**. By the identical second-factor argument, there is at most ONE B splitting basis. This argument counts original cells, not distinct rays or virtual tensor points.

## 5. The two allowed split bases make every component ray light

If no A splitting basis occurs, all actual lines must be B-split by Section 3. There is at most one such local basis {b,b-perp}. Every actual ray then lies in C^2 tensor b or C^2 tensor b-perp, two mutually orthogonal nonzero spaces; each contains actual rays because a line spans W. This contradicts C being one intrinsic component. The same argument applies if there is no B splitting basis. Thus there are fixed local bases {a,a-perp} and {b,b-perp}, the unique possible A and B splitting bases respectively.

Choose the ONE component ONB

    E={a tensor b, a tensor b-perp,
       a-perp tensor b, a-perp tensor b-perp}.

Every actual component ray belongs to an actual row. If that row is A-split, its first factor is a or a-perp, so it has support at most two in E. If the row is B-split, its second factor is b or b-perp, again giving support at most two. Rows having both forms satisfy both conclusions. Thus ALL actual component rays have E-support one or two. Other components of Q are irrelevant to this statement.

## 6. An all-light nontrivial component contradicts P-STAR

For completeness, suppose all rays of an intrinsic component are supported on at most two axes in one fixed ONB E of its span. Since the component is nontrivial, there is an actual two-supported ray x on coordinates i,j. An actual light ray perpendicular to x either is its unique orthogonal partner x' in the i,j plane OR has support disjoint from {i,j}: support intersecting in exactly one active coordinate gives one nonzero inner-product term and cannot be orthogonal.

In any actual component line through x the other r-1 orthogonal rays cannot all lie in the r-2 dimensional coordinate complement of {i,j}. Hence x' is actual. Every OTHER star-x ray has support disjoint from {i,j} and is perpendicular to x'. Thus x' is an isolated star ray. P-STAR forces m(x')>=5, contradicting GAP3.

Applying this with r=4 to Section 5 proves the theorem: **no intrinsic C4 component of any member of any ordinary four-MOQLS(8) admits one common C^2 tensor C^2 factorization making all of its actual rays product**.

## 7. Exact progress, first unproved step and assurance

This excludes every such product-component stratum, including arbitrary complex local factors, all virtual choices of the factorization, direct rectangular bases, mixtures of the two split types, and rays on split-basis boundaries. It is stronger than excluding only real-product span-nine cones, but weaker than excluding arbitrary C4 span nine. In particular the REAL product-projector space has dimension 3 times 3 = 9 and supplies a natural abstract low-span geometry; the theorem shows that geometry cannot be the actual intrinsic component of the four-family. This dimension observation is not used in the exclusion proof.

The FIRST UNPROVED bridge is whether every remaining b=9 C4 configuration can be put into that product geometry, or whether an unexcluded nonproduct rank-nine geometry can be removed directly. No such classification or exhaustion is claimed. C5 b10 is still unresolved. The earlier operator packet `frontier-20261029-operator-star-cover-and-local4-rigidity-v1.md` independently restricts b9 to sigma_u=5, real cross dimension three, full complex neighbour span, and exact block-diagonal kernel at every actual ray; its review is pending and it is not an additional import here.

Original A10 is GB15/18 with P1-B2.M2, P1-B2.M4, P1-B3.M2 UNKNOWN; A11 remains OPEN. No heavy/multi-GB run, scientific interpreter, selected numerical probe, external CLI or nested agent was used. This is exact WRITTEN mathematics only. All frozen sources and earlier process/cadence disclosures are preserved; independent full review and parent adoption are not performed by this author packet, and no formal, human, configured-family, executable, source-priority or novelty acceptance is claimed.
