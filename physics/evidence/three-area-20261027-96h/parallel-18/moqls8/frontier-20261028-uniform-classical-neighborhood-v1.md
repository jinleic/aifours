# Quantitative classical-neighborhood rigidity for four MOQLS(8)

**PhysicsMOQLS8-2, physics-4. WRITTEN AUTHOR CANDIDATE with an exact finite control; NOT yet peer/parent reviewed, formalized, novelty-cleared, or an unrestricted four-family solution.**

## 1. Original target and actual advance

An ordinary QLS(n) is an n×n array of unit vectors in C^n whose rows and columns are ONBs. Two such arrays are orthogonal iff their n² same-cell tensor products form an ONB of C^n⊗C^n; a family is classical iff every member's entries, up to per-cell phase, are drawn from one member-specific global ONB. Four-family order8 asks whether any actual family with at least one nonclassical member exists. All four squares may be quantum; no common output frame is imposed.

The accepted five-family result concerns FIVE members and is not used as a four-family theorem. Previously supported four-family low-support/exposure statements do not supply an unrestricted higher-support gluing theorem. Their validity is not inferred from names or substituted into the argument below.

**New candidate:** every classical m-MOQLS(n) family is surrounded by an explicit, UNIFORM projective neighborhood containing no nonclassical actual m-family whenever `2(m+1)>n`. In particular, for any classical four-family at n=8, every actual four-family at projective cell distance at most **1/576** from it is classical. This covers ALL mixtures within the neighborhood, not merely the case with one nonclassical square. The argument uses actual complex row/column and all pair-product orthogonality, without assuming sparse support, a path, or a particular classical Latin net. The mathematical proof is §§2–7; the independently executable exact finite control is §8.

This establishes a quantitative boundary obstruction to continuous small-amplitude gluing from any classical four-family. It does **not** rule out nonclassical families at larger distance, imply that all families are connected to a classical one, or determine M(8). A finite example is evidence for the checker only, not evidence that the universal claim is true.

## 2. Theorem and metric — all classical configurations

For unit vectors v,w define projective chordal distance

    d([v],[w]) = sqrt(1 − |<v,w>|²).

For two labelled m-families use the maximum of this distance over all members and all n² cells. A classical labelled reference C has, for each member a, an ONB `{e^a_p : p=1,...,n}` and a Latin symbol map `L_a(i,j)` such that the reference ray at cell `(i,j)` is `[e^a_{L_a(i,j)}]`. Its members may have different bases and independent cell phases. Its actual row/column and pair-product ONBs imply that the maps L_a are mutually orthogonal Latin squares.

**Theorem (uniform local classicality).** Let `n≥2`, let `m≥1` be such that `2(m+1)>n`, and let C be ANY actual classical m-MOQLS(n) family. Let Q be ANY actual ordinary complex m-MOQLS(n) family on the SAME labelled grid. If

    max_(a,i,j) d([Q_a(i,j)],[C_a(i,j)]) ≤ 1 / [8 n(n+1)],       (1)

then every Q_a is classical; in fact there are a separate unitary U_a and cell phases λ_(a,i,j) with

    U_a Q_a(i,j) = λ_(a,i,j) e^a_(L_a(i,j))  for ALL a,i,j.    (2)

Consequently any nonclassical actual Q has distance **strictly greater** than the bound in (1) from EVERY labelled classical reference. Simultaneous row/column permutations merely relabel the grid and can be incorporated into the reference. No actual admissible nonclassical Q is asserted to exist.

For n=8,m=4, `m+1=5>4`, and the radius is `1/[8·8·9]=1/576`. This is a rigorous lower separation bound if the proof below survives review; it is not a fitted tolerance or a claimed sharp radius.

## 3. Actual classical incidence gives a dense five-line graph

Fix ANY member a and ANY two distinct symbols p,q in its own classical reference basis. There are exactly n cells carrying p and exactly n carrying q, each symbol appearing once in every row and column. Build a bipartite graph Γ_(a,p,q) on these two occurrence sets. Join a p-cell x to a q-cell y when ANY of the following actual reference classes agrees:

1. same row;
2. same column;
3. same symbol in any one of the other m−1 reference members.

Each of these m+1 classes is a perfect matching between the two occurrence sets. Row/column matchings exist by the Latin property of L_a. A companion matching exists because the ordered pairs `(L_a,L_b)` run through every symbol pair exactly once: this follows from the ACTUAL pair-product ONB of the reference classical squares.

No two matching classes give the same edge: a different pair of cells cannot share row and column; within any reference row or column each companion symbol occurs once; and two distinct companion members cannot repeat the same ordered symbol pair because their own reference pair-products are an ONB. Thus Γ is a **simple (m+1)-regular bipartite graph** on n+n vertices. The construction covers every p,q,a and every classical reference; no affine/net classification is assumed.

Since `2(m+1)>n`, ANY two vertices on the same side have intersecting neighborhoods: two subsets of an n-point opposite side, each of size m+1, cannot be disjoint. In particular every vertex on the p-side is at graph distance at most2 from the unique p-cell in the reference first row; the same holds independently on the q-side from the first-row q-cell. The graph is connected. This precise >n/2 argument is what fails at equality; no statement is made for `2(m+1)≤n`.

## 4. Align the ACTUAL first rows and bound all leakage

Suppose (1), with η=1/[8n(n+1)]. Work independently in each member's reference basis; this is not a common unitary across members. Choose each vector's phase so its inner product with its reference basis ray is nonnegative real. Its Euclidean distance from that reference unit vector is at most `sqrt(2)η≤2η`, since `||v−e||²=2(1−sqrt(1−d²))≤2d²`.

For member a, let F be the actual first-row unitary matrix with its columns in grid-column order, after these phases, and E the corresponding reference first-row unitary. Each column differs by at most2η, hence

    ||F−E||_op ≤ ||F−E||_F ≤ 2 sqrt(n)η ≤ 2nη.

Apply the separate output unitary `U_a=E F*`. It sends the actual first row to the reference first row EXACTLY and satisfies `||U_a−I||_op≤2nη` in this member's reference frame. Thus for every cell its projective leakage from its intended reference ray is bounded by

    δ := max ||projection onto the complement of the reference ray||
       ≤ 2(n+1)η = 1/(4n).                                     (3)

Rephase each aligned cell so its intended reference coefficient is positive real. This rephasing preserves all row/column and product-ONB constraints. The aligned first row remains exactly the reference basis with coefficient +1. For each cell x of reference symbol p,

    ψ_x = a_x e_p + Σ_(r≠p) c_(x,r)e_r,
    a_x = sqrt(1 − Σ_(r≠p)|c_(x,r)|²)>0,
    Σ_(r≠p)|c_(x,r)|² ≤ δ²,
    0≤1−a_x≤δ².                                                   (4)

All quantities in (3)–(4) refer to the actual transformed four-family, including arbitrary complex phases. No approximated array replaces it.

## 5. Every dense-graph edge enforces an ACTUAL zero

For any edge xy of Γ_(a,p,q), if x,y share a row or column, the selected member a is exactly orthogonal there by its own QLS condition.

Otherwise they share one reference symbol in a companion member b. Both ACTUAL companion vectors have positive reference coefficient and leakage≤δ in that same companion basis ray. Their actual overlap therefore obeys

    |<Q_b(x),Q_b(y)>| ≥ (1−δ²)−δ² = 1−2δ² > 0.                  (5)

The first lower term bounds the product of their two positive reference coefficients; Cauchy–Schwarz bounds the rest by δ². The final inequality follows from (3),n≥2.

The ACTUAL pair-product ONB condition for members a,b and distinct cells x,y then forces `<Q_a(x),Q_a(y)>=0`. Hence EVERY graph edge yields a literal selected-member zero, not just a first-order or support-pattern approximation. We use all companion symbols that occur, but only need one nonzero mate overlap per edge. All other pairs are left unrestricted.

## 6. Exact propagation inequality; no infinitesimal-to-global leap

For an arbitrary graph edge with x labelled p,y labelled q, insert (4) into the ACTUAL zero. It gives

    0 = a_x c_(y,p) + a_y conjugate(c_(x,q))
        + Σ_(r≠p,q) conjugate(c_(x,r)) c_(y,r).

The last sum has modulus≤δ², and the two coefficient corrections cost at most2δ³. Thus

    |c_(y,p) + conjugate(c_(x,q))| ≤ δ²(1+2δ).                   (6)

On the p-side put potential `conjugate(c_(x,q))`; on the q-side put potential `−c_(y,p)`. Equation (6) bounds the difference across EVERY edge by δ²(1+2δ). The first-row p-cell and q-cell have potential0 because their actual vectors are exactly e_p and e_q.

By §3, any p-occurrence is within two edges of the p first-row anchor, and any q-occurrence is within two edges of the q first-row anchor. Hence for EVERY distinct symbol pair and every occurrence,

    |c_(x,q)| ≤ 2 δ²(1+2δ).                                       (7)

This holds simultaneously for each member and all its off-reference coefficients. Taking the Euclidean norm of the n−1 off-reference coordinates, then the maximum over all cells and all members, yields

    δ ≤ 2 sqrt(n−1) δ²(1+2δ).                                     (8)

If δ>0, divide by δ. From δ≤1/(4n),n≥2, and sqrt(n−1)≤n,

    2 sqrt(n−1) δ(1+2δ) ≤ 1/2 + 1/(4n) < 1,

contradicting (8). Therefore δ=0. Every aligned actual vector is exactly its labelled reference ray. Undoing the unitary/phase choices proves (2) and completes the theorem.

The proof uses no differentiability assumption, no inferred integrability of a tangent, no finite cutoff on supports, and no classicality assumption on Q. The small-neighborhood hypothesis is essential: it guarantees the companion overlaps in (5) are nonzero. At large distance they may vanish and the graph edges may no longer impose selected-member zeros.

## 7. Consequences and exact remaining obstruction

1. **Uniform all-mixture local bridge:** for EVERY actual four-family of order8, if its labelled rays are within1/576 of ANY actual classical four-family, then all four members are classical. Every nonclassical member is excluded in that ball, regardless of how many other members are classical/nonclassical.
2. **Unconditional local gap:** if an actual nonclassical four-family exists, its maximum per-cell projective distance from EVERY classical four-family is >1/576. This is a necessary separation, not a witness.
3. **No infinitesimal escape at a classical point:** the anchored linearized edge constraints have zero kernel; §6 proves more, an explicit nonlinear neighborhood. The specific checker in §8 confirms this rank for one actual classical reference but does not replace the arbitrary-net proof.
4. **Unresolved:** this does not prove the feasible space is connected, exhibit a path, or exclude a disconnected/nonperturbative nonclassical family. It does not prove a numerical maximum or solve the unrestricted four-family problem. It does not imply the original five-family result or a QOA/entangled-array equivalence. Novelty/priority and independent review remain open.

The method uses only ordinary Latin incidence, complex inner products, graph cardinality and norm inequalities. The prior parent-adopted gluing/exposure statements provide context but are not correctness premises; historical source/STOP/quarantine outcomes are not relabelled as validated by this new argument.

## 8. Bounded exact finite experiment and two controls

Source: `frontier-20261028-classical-boundary-check-v1.py`, SHA256 **6873746364cabf946b7b9c5df1649501633702e007310faa3fb2de52782192d6**.
Receipt: `frontier-20261028-classical-boundary-receipt-v1.json`, SHA256 **5c60f8daa90b66ea7dbd69ad40a62b85bcb1ba2a57fcdcd0a7b75ad1c02442bd**.

Executed once, bounded, using:

    python3 -B frontier-20261028-classical-boundary-check-v1.py \
      --output frontier-20261028-classical-boundary-receipt-v1.json

The script constructs ONE classical affine four-family over the explicit 3-bit multiplication encoding, outputs all four actual symbol tables in the receipt, checks that nonzero multipliers permute the alphabet, and directly checks ALL 4,096 row/column Gram entries and ALL 24,576 six-pair product Gram entries as exact 0/1 integers. It then independently constructs every 5-regular Γ for that one family: **112 graphs**, each40 edges,all16 vertices connected,and **anchored complex incidence rank14/14** via exact rational Gaussian elimination. Total anchored real rank is **3136/3136**. The reported source SHA is computed from the executed script's own bytes.

Negative control1 duplicates one cell: row errors2,column errors2,pair-product errors6. Negative control2 duplicates one entire square: every row/column Gram still passes, but pair-product Gram errors448. Both were rejected for their intended reason. Runtime in the receipt was about0.073 seconds; these checks use integers and `fractions.Fraction`, not floating fitting.

The executed control is a single classical input and no nonclassical witness. It does not enumerate all classical nets, validate the universal proof, establish an exact quantum witness, or replace independent mathematical review. The two controls are diagnostic only; they do not constitute triple-independent verification or novelty clearance.

## 9. Assurance and next scientific question

The mathematical statement is **WRITTEN AUTHOR CANDIDATE**; finite control is **EXACT CHECKED on one named input**. This is not formal/kernel proof, independent/human/configured-family review, external SOTA/novelty audit, or original M(8) determination. The old selected-diagnostic/cross-slot/B4 and other historical outcomes are not accepted as premises or retrospectively called successful. No external model, source expansion, Git, deletion or infrastructure mutation was used.

The exact next obstacle is global: derive a lower-overlap graph mechanism for EVERY putative nonclassical family, or construct and directly verify an actual family outside these classical neighborhoods. The proof does not permit assuming a candidate can be moved continuously into the classical neighborhood. Further work should attack genuinely nonperturbative components, not repeat the local rigidity estimate.
