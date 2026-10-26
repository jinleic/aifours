# Candidate v1 — doubled-fiber isolation and thin-label coherence exclude the whole v3555/e0 stratum

Observed immediately before creation: **2026-10-24T04:05:11-0700**. PhysicsAME46, physics-6. Same primary problem. **Complete WRITTEN CANDIDATE, not independently reconstructed or parent-accepted.** No scientific executable/import, arithmetic program, enumeration, solver, CAS, compilation, tests, CLI, native launch or nested agent. `continuation-v3555-scope-v1.json` records the full quantified scope and honestly states that exploration had already begun before that scope record; no preregistration or observation-order reset is claimed.

## 1. Literal whole-stratum theorem and infrastructure boundary

For a normalized arbitrary-complex AME(4,6), in an arbitrary product orthonormal basis, put

    A=6psi, T={x:|A_x|=1}, N=supp(A)\T,
    t=|T|, h=36−t, e=|supp(A)|−(72−t),
    d_(i,a)=6−#{x∈T:x_i=a}, V_i={a:d_(i,a)>0}, v_i=|V_i|.

**Candidate theorem.** No such tensor has h=12,t=24,e=0,support48 and active sizes(3,5,5,5), up to party permutation. Every actual officer placement, nonzero amplitude and complex phase is retained. This is NOT a result only for one graph or one thin-value labeling.

The baseline officer identities force the only profile

    {4,4,4} {3,3,2,2,2}³.

That narrowing is re-derived in §3 and is not the new progress. The new coherence chain is: D3 plus doubled-fiber closure rules out EVERY Hamming-distance-one N pair; actual thin slices become parity tetrahedra; active-to-thin officer bijections forbid cross-label pairs and force one officer pair per label; the remaining thin-pair graphs have at most one edge each, contradicting the actual36 thin incidences on24 N points.

**Reviewed infrastructure consumed:** LemmaD3 and the exact e=0 pair-line/block facts in `v4445-coherence-exclusion-v1.md`, SHA256 `3be4074ca32dbceb5b27776ad22470cd58efa4c97415604df27c4066dcf7302c`. Their actual parent boundary is `institute/runs/three-area-2026-10-23-96h/ame-v4445-stratum-parent-v1.md`, SHA256 `7d5af2adf2c092008fb4e4023b02537206ce774bf1a98f9c815bd9eb653ed094`, read completely including untruncated9. No old v4445/all-e3333 verdict is transferred to the NEW deductions here.

This excludes ONE whole remaining support48 stratum. Other strata remain; the global documented48..60 bound is unchanged and no lower49 follows by itself.

## 2. Exact pair facts and the precise D3 input

All six actual two-party marginals equal I36/36. For any cut P|Pc the flattening M_P of A is unitary, with

    rho_P=M_P M_P†/36,
    rho_Pc=(M_P†M_P)^T/36.

Consequently every pair-value line has squared A-norm1. Officers exhaust their lines and cannot agree in two coordinates. Every line is occupied. An officer-free line has at least two nonzero coefficients, and N uses only active values. There are exactly h officer-free lines in EVERY pair projection.

At e=0 each officer-free line has exactly two entries, both in N, in all six pair directions. The local N-slice at deficit d has2d points and takes d values in every other coordinate, each twice. Orthogonality plus degree2 makes every non-officer flattening component a closed2×2 unitary block.

The universal deficit1 obstruction is independent of e: five officers at a local value leave at most one possible additional tensor position after all partner exclusions, but its missing pair-line needs at least two nonzeros. Thus every positive deficit is at least2.

**D3, used only at its reviewed scope:** if two N points in an e=0 AME tensor differ in just coordinate i and share value c at j!=i, then d_(j,c) cannot be3. The physical reason is rectification of the associated closed2×2 unitary block by a LOCAL U_i=B†. At the shared j=c slice its old officers lie outside the two mixed i-levels and remain; two new unit-modulus entries would turn3 officers into5, forbidden universally.

For clarity this input preserves ALL six reductions, not just the chosen flattening: when i∈P, rho'_P=(U_i tensor I)rho_P(U_i tensor I)†=I36/36; when i∉P, partial-trace invariance gives rho'_P=rho_P=I36/36. No e restriction on the transformed state is needed to apply the deficit1 contradiction. The new proof does not assume an unconditional no-Hamming1 theorem beyond this literal common-deficit3 predicate.

## 3. The whole target has exactly the stated thick/thin profile

Place the three-value coordinate at party1 by a party permutation. This preserves all six marginal conditions,h,e and support. For an officer x let c(x) count its active coordinates. General officer incidence counting gives

    kappa1=sum_T c=6sum_i v_i−4h,
    kappa2=sum_T binom(c,2)=sum_(i<j)v_i v_j−6h.

Here v=(3,5,5,5),h=12,t=24, so kappa1=60 and kappa2=48. The sum of the nonnegative integer polynomial(c−2)(c−3)/2 is48−2·60+3·24=0. Therefore every officer has c∈{2,3}.

At an active value of deficit d in coordinate i, with S_i=sum_(j!=i)v_j,

    #officers=6−d,
    sum_(T:x_i=a)(c−1)=S_i−3d.

Since c−1≥1, d≤(S_i−6)/2. At party1, S_1=15 gives d≤4, so three positive deficits summing12 are4,4,4. At every other party S_i=13 gives d≤3. Positive deficits are at least2, so five parts summing12 are3,3,2,2,2.

Write X=V_1 for the three active values of party1. For j∈{2,3,4}, write T_j for its THREE thin values of deficit2 and H_j for its TWO thick values of deficit3. Its one inactive value is neither. These symbols name actual local basis values; no coordinate alphabet, phase or shape is identified between parties by assumption.

## 4. EVERY Hamming-distance-one N pair is impossible

This is the first new coherence step. Suppose two N points differ only at party i, with levels a,b. For triples z in the other three coordinates define

    D_ab={z:A_(a;z)!=0 and A_(b;z)!=0}.

It contains the proposed fiber. Form a graph on these triples, joining by a color-j edge when they share the j-value, j!=i. I now derive its entire local structure rather than import an unchecked catalogue.

In flattening(i,j)|rest, the column through a doubled fiber has precisely its two entries in rows(a,z_j),(b,z_j). Closed2×2 closure provides a unique partner doubled triple z' with z'_j=z_j. Both other coordinates of z' change: if another coordinate also agreed, all four block entries would share two fixed coordinates, contradicting exact-two pair-line degree. A third triple with the same j-value is impossible because row(a,z_j) is already full. Thus every vertex has exactly one neighbor of each of the three colors, these neighbors are distinct, and the graph is simple cubic, each color a matching. Distinct doubled triples cannot agree in two coordinates.

For a doubled triple put v_z=(A_(a;z),A_(b;z))^T. It is a UNIT vector: the line fixing any two other-coordinate values is already filled by its two entries. At adjacent triples the two vectors are orthogonal columns of the same closed2×2 unitary block. In C² the orthogonal ray is unique, so rays alternate on graph walks and an odd cycle would make a nonzero ray orthogonal to itself. Every component is bipartite. Simplicity and cubic degree force at least3 vertices in each part, hence at least6 vertices in every component.

Choose TWO distinct five-value parties j,k in{2,3,4} different from i; such a pair always exists. For EVERY doubled triple, D3 rules out a thick value at j or k, since it would be the common deficit3 coordinate of the original doubled pair. Thus all triples in the component use only the three thin values at each of j,k. Each used value occurs exactly twice, by the color-matching argument above, so the component has at most6 vertices. It therefore has EXACTLY6 vertices and uses ALL three thin values at j and at k.

For any used thin value at j, its two doubled triples contribute four N points and exhaust its entire deficit2 slice. Therefore no N point outside this component can use ANY thin value at j. The same holds at k. All outside N points use only H_j×H_k, a2×2 pair grid.

The six doubled triples give SIX distinct(j,k) pairs; two sharing both coordinates would give four entries on an exact-two line. Each pair has its two a/b coefficients and is one hole line. Outside the component there are at most FOUR further(j,k) hole lines, because outside N points use only the two thick values in each coordinate. There is no cross thin/thick escape: every thin slice at both parties was already exhausted by the component.

The complete(j,k) projection would therefore have at most6+4=10 hole lines. It must have h=12. Contradiction.

This rules out ANY initial doubled fiber, in ANY varying coordinate and any pair of its active levels. Hence N has minimum Hamming distance at least2. The argument keeps arbitrary complex rays, uses their actual C² orthogonality, and contains no graph enumeration or common-ray ansatz imposed on the input.

## 5. Derived active-to-thin officer bijections

For each j∈{2,3,4}, an active x∈X has deficit4. Of its five active partner values at j, exactly four give holes, so exactly ONE gives an officer. A thick value at j has deficit3 and hence no active officer neighbor at party1 of active size3. A thin value has deficit2 and hence exactly one such neighbor. Consequently the active officer pairs define a bijection

    F_j:X -> T_j.

Label F_j(x) at party j by the abstract label x∈X. This is shorthand for actual derived bijections, not an imposed equality of physical basis symbols, an identification of inactive values or a restriction of officer placements.

Every N point whose party-j value is the thin label x must have its first coordinate different from x, because the pair(1=x,j=F_j(x)) already carries its officer. Conversely the thin slice at F_j(x) uses exactly the other TWO first-coordinate active values, since its two first-coordinate hole lines must be occupied.

## 6. Thin slices are parity tetrahedra; different thin labels cannot meet

Every thin slice at a five-value party has4 N points, taking two values twice in each of the other three coordinates. The four points are distinct binary triples. Four balanced binary triples are either a fixed-XOR two-coordinate plane with the third bit free, or the parity plane of all three bits. One proof uses the three possible2+2 partitions of four points: coinciding partitions give the first case; three distinct partitions give XOR/complement. The first case would contain a Hamming1 pair, excluded by §4. Thus EVERY thin slice is a parity tetrahedron. Its projection onto EACH pair of other coordinates is the FULL2×2 rectangle of its actual two-value neighbor sets.

Suppose N contained a point with thin labels x and y at two five-value parties j,k, where x!=y. Every N point on that fixed(j,k) line has first coordinate avoiding BOTH x,y, by §5. Only one first-coordinate value remains in X of size3. That pair-line, if it meets N, has exactly two nonzero entries. They would agree in party1,j,k and differ only in the fourth coordinate: a Hamming1 pair. Contradiction.

Thus whenever a non-officer point has at least two thin last coordinates, their labels are the SAME. This is an actual pair-line exclusion, not a restriction chosen for convenience.

## 7. An actual weight3 officer per first label excludes all-three-thin N points

Fix x∈X. Its deficit4 gives exactly TWO officers. Their total active incidences in parties2,3,4 is

    sum_(j=2)^4(v_j−4)=3.

Each officer has active weight2 or3 by §3 and already has the active first coordinate. It therefore contributes1 or2 to that count. Two contributions summing3 force one officer of each type. Let O_x be the actual weight3 officer.

It has TWO active last coordinates. By the F_j definitions, both are thin values of label x. Their pair-line is occupied by O_x and cannot contain any N coefficient. Hence no N point can have all three last coordinates thin with label x. By §6 any proposed three-thin point would have equal labels, so this excludes ALL N points with three thin last coordinates.

This uses an actual forced officer O_x for each label, not an assumed position or a scalar profile asserted realizable.

## 8. The remaining same-label thin-pair graphs have at most one edge

For each label x∈X, define a graph G_x on the three five-value parties{2,3,4}. An edge j-k means the actual pair-line(j=F_j(x),k=F_k(x)) meets N. Every such line has exactly two entries, and by §7 both have exactly TWO thin coordinates, not three.

If one vertex j had edges to BOTH other vertices k,l, then in the thin slice j=F_j(x), its k-neighbor set contains F_k(x) and its l-neighbor set contains F_l(x). The parity tetrahedron's FULL(k,l) rectangle projection from §6 would give an actual N point with those two values and j fixed: a three-thin point of label x. This is forbidden.

Thus every G_x has maximum degree at most1. A graph on three vertices then has at most ONE edge. There are three labels, and each edge accounts for exactly two N points with two thin coordinates. Every two-thin N point has one label by §6 and belongs to its unique pair-edge; with no three-thin points there is no double counting. Therefore

    n_2=#{N points with exactly two thin last coordinates} <=2·3=6. (T2)

This is a complete structural constraint for all thin-pair incidences, not a check of one selected graph or a finite table.

## 9. Whole-stratum contradiction

The nine thin local values (three at each of three parties) each occur in exactly4 N points. Their total incidence count is

    I_thin=3·3·4=36.

There are exactly|N|=2h=24 points. By §7 each has0,1 or2 thin last coordinates. Writing n_r for their counts,

    n_0+n_1+n_2=24,
    I_thin=n_1+2n_2 <=24+n_2 <=30,

where the last bound is(T2). This contradicts I_thin=36.

The contradiction follows only after actual unitary-ray closure, D3, parity projections and the forced officer pair have eliminated the other coherent possibilities. The original global moments alone do not give(T2). The entire h12/e0/v3555 stratum is impossible. Party permutation restores every possible placement of its three-value coordinate, preserving all six marginals and all definitions. ∎

## 10. Exact checks required and remaining unrestricted target

The load-bearing new checks are:

1. In §4 the doubled graph really is simple cubic and bipartite over arbitrary complex phases; its two selected nonvarying five-value coordinates must be thin by D3; six vertices exhaust all three thin slices, and every pair projection must still have12 holes.
2. The F_j maps are DERIVED active-to-thin bijections; different-label thin pairs leave only one first-coordinate possibility and hence violate the already-proved no-Hamming1 result.
3. Every thin slice has a full rectangle projection; one actual weight3 officer O_x per first label excludes three-thin points; no same-label pair graph can have two incident edges. The two-thin point bound must count actual occurrences without overlap.
4. All uses of exact-two cardinality and block closure retain the ORIGINAL e=0 hypothesis. The reviewed D3 transformation preserves all six pair marginals and uses the universal deficit1 obstruction on its transformed state without assuming e'=0.

All these steps are written above. No QLS6 classification, no-AME(4,2), old lower48 certificate, operator catalogue, tested table, support-minimal basis, real form or equal nonzero modulus is a premise. Standard complex2-space ray orthogonality is the only geometric-ray fact used. The baseline moment narrowing in §3 is not separately counted as a discovery.

This new snapshot needs actual separate reconstruction and parent disposition; neither the older v4445 review nor the all-e3333 review certifies it automatically. No formal/kernel/human/novelty or worldwide SOTA acceptance is claimed.

Other support48 active/deficit profiles and required e>0 cases remain. In particular the proof does not exclude every v4455/v4555 or other h/e stratum, does not construct an exact state and does not establish lower49. The documented unrestricted48..60 interval, source/open-status qualifications, original deadline and scientific-launch HOLD are unchanged.
