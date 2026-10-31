# Independent same-harness review: q1 C6 span thirteen with three classical mates

**Disposition: scientific F=0, M=0, m=0; INCONCLUSIVE items=0 at the stated written scope. Process F=0, M=1, m=0: the reviewer-owned control script was written before a native pre-write clock was observed.** The scientific candidate is **WRITTEN_SUPPORTED in this review**, not thereby parent-adopted. The pre-review-write native observation was `/bin/date`: **2026-10-29T13:36:39-0700 PDT**. This is an observation before writing this report, not an asserted file-creation time.

## Scope and individual verdicts

The exact scope is **q1-local, an ordinary four-MOQLS(8) with three actual classical mates**: for an intrinsic six-dimensional component of the remaining member, its real projector span has dimension at least 13. This does not assert that such a component cannot exist, settle all q1 cases or q4, establish existence or numerical M(8), or establish novelty.

| Claim | Verdict | Independent reason / location below |
|---|---|---|
| Physical five-net and six component entries on every actual line | 0F/0M/0m | Derived directly from the four actual product ONBs and classicality, §1. |
| STAR and the two-cover COMMON on the common perpendicular | 0F/0M/0m | Three disjoint weighted resolutions plus the actual row/column stars, then a positive-operator subtraction, §2. |
| Two-space capacity 3, uniqueness of a third ray, no two distinct two-ONBs | 0F/0M/0m | Projection mass 16 and disjoint targets, §3. |
| Tightened three-space capacity 6, and connected three-block corollaries | 0F/0M/0m | Mass 24, degree/triangle parity, and two disjoint three-ONBs cannot have two zero overlaps, §4. |
| Cross-image lower bound and non-complex-line property | 0F/0M/0m | Kernel/rank and an actual ONB through a mixed ray, §5. |
| Sparse-unitary lemma U5 | 0F/0M/0m | Support-degree proof, §6; independent finite support control, §10. |
| Connected five-block pivot | 0F/0M/0m | Saturation, eigenvector classification, and a star-vector contradiction, §7. |
| 4+1 pivot | 0F/0M/0m | Cross rank at most one, COMMON, and the shared-axis multiplicity, §8. |
| Forced 3+1+1 pivot, cross ranks 0/1/2 and common-factor cases | 0F/0M/0m | Off-space bookkeeping, two-cover, and STAR, §9.1–9.3. |
| Independent two-plane pencil and pure/mixed net-line count | 0F/0M/0m | All ONB multiplicity types are handled; at most 2 pure plus 2 mixed versus 5 actual lines, §9.4. |
| Import/scope boundary | 0F/0M/0m | GAP3 alone is used as an adopted theorem; the five-net interface is derived here, §11. |
| Process: native clock before writing the reviewer script | **M** | No native clock was observed before that script write; no script creation time is claimed, §11. |

## Frozen inputs, integrity, and actual sequence

The first research artifact opened was `manifest-v1.json`. Its measured SHA-256 is `eec45e4034f4598b4306c74b9cacd26cd11bd66c78cd37507d65b0b4ff1f0a03`, matching the requested `eec45e4034f4` prefix; its measured size/LF count was 3708 bytes/37 LF. Before any declared input body was read, `shasum -a 256` and `wc -cl` measured every declared input; each hash, byte count, and LF count matched the manifest:

| Input in manifest order | Measured SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `institute/runs/three-area-2026-10-23-96h/MOQLS-unrestricted-four-family-ray-gap-intrinsic-and-local-span-budget-entire-parent-v1.md` | `2e254b56d108994844cf337c31b98fa851effca15a68a847c6cb2db84552bee4` | 9675 | 63 |
| `institute/runs/three-area-2026-10-23-96h/moqls-five-net-entire598-ray-span-qutrit-parent-v1.md` | `dabeca7b8cbdb7a7bc5149b75c30d4a1523012a5c9609e8a7eadcec635aa12f9` | 12138 | 66 |
| `physics/evidence/three-area-20261027-96h/parallel-18/moqls8/frontier-20261029-q1-C6-span-thirteen-complete-v1.md` | `26efd7dbd91ec64bcf1ae6b0ec16e38bdd874639eb353ebbfb4f950330d1c468` | 22337 | 170 |

I then displayed every declared body completely in the prescribed order using these exact raw windows, including the endings:

1. First disposition: `1-15`, `16-30`, `31-45`, `46-60`, `61-63`.
2. Five-net disposition: `1-15`, `16-30`, `31-45`, `46-60`, `61-66`.
3. Candidate: `1-15`, `16-30`, `31-45`, `46-60`, `61-75`, `76-90`, `91-105`, `106-120`, `121-135`, `136-150`, `151-165`, `166-170`.

The first manifest display truncated its long lines 9 and 36; after the body reads I displayed those two lines separately as raw `9-9` and `36-36`. The mathematics and controls below were undertaken only after all three complete input reads. Administrative memory and generic snapshot-review guidance were also read after the integrity measurements; neither is mathematical evidence or an imported theorem. No linked source body or other review was opened as evidence.

## 1. Physical interface and component compression

Let the members be Q and three classical mates L₁,L₂,L₃. Classical means each mate uses one of eight orthogonal global rays, with arbitrary phases and its own output basis. Each row and column of a mate is an ONB and hence contains each label exactly once. For different classical mates, equality of their respective labels in two different cells would make both factors in the corresponding product inner product nonzero, contradicting the actual product ONB. There are 64 cells and 64 ordered label pairs, so every pair occurs exactly once. Rows, columns and the three symbol classes therefore give five classes of eight lines, with any two lines of different classes intersecting in exactly one cell.

A Q row and column is an ONB by definition. On a classical-symbol line, the mate's factors have the same ray, so product orthogonality forces Q's eight entries to be orthogonal; they form an ONB. Different intrinsic ray components of Q have orthogonal complex spans. An actual line ONB decomposes over these spans; therefore its entries in the selected six-dimensional component W are exactly a six-ONB. In particular the five lines through any selected cell y share no other cell, and their other 25 W-cells are distinct. Summing the eight actual row resolutions gives Σ_{z in C} P_z = 8 I_W. No affine-net, common mate basis, additional classical member, or prior five-net theorem is used.

## 2. STAR and the common-star two-cover

Fix actual u=Q_y in C and H=W∩u⊥. Resolve the actual Q⊗Lᵢ product ONB against the vector (Lᵢ)_y, then compress to H. The y term vanishes after this compression. A different cell with nonzero mate overlap must have Q_z⊥u. On y's row and column, all other mate labels differ from y's, so those weights vanish. For a fixed other cell, at most one of the three mate weights is nonzero: otherwise the two corresponding classical factors would both overlap their y factors, contradicting their product ONB. Each weight is at most one. Thus the three weighted resolutions give at least 3 I_H from disjointly weighted cells outside y's row and column. The actual Q row and column provide two further, disjoint H-ONBs. Hence, counting original cells with multiplicity,

A_u := Σ_{z in C, Q_z⊥u} P_z ≥ 5(I_W−P_u).  (STAR)

Its trace on H implies at least 25 orthogonal-star cells. If a star ray g is orthogonal to every other distinct star ray, evaluating STAR at g gives its global multiplicity m(g)≥5, contradicting adopted GAP3. This observation is used only for actual rays.

For actual perpendicular u,v put K=W∩u⊥∩v⊥. On H, the total Q projector sum is 8 I_H, so the contribution from cells not perpendicular to u is F_u=8 I_H−A_u|_H≤3 I_H. Compress STAR(v) to K and subtract only the cells not perpendicular to u. Their positive contribution is bounded above by F_u|_K. Thus

Σ_{z in C, Q_z⊥u, Q_z⊥v} P_K P_z P_K ≥ 2 I_K.  (COMMON)

Consequently the actual common-star rays span K after projection, and their projections span every subspace of K. The constant 2 is a lower operator bound, not a manufactured virtual frame.

## 3. Two-space capacity

For any complex two-plane B⊂W the total Q projection mass is tr(8I_W P_B)=16. For each distinct actual ray v⊂B, evaluate STAR(v) at its unique perpendicular direction v′ in B. The star cells contributing nonzero B-projection all project along v′ and have total B-mass at least 5. Different v give different target directions, so their cell sets are disjoint. There are at most three distinct actual rays in B.

If exactly three rays contained no orthogonal pair, their own occurrence cells would be outside all three target sets and contribute at least 3 additional units, giving 18>16. Thus an orthopair exists. The third ray is nonorthogonal to each member of that pair, so its m occurrence cells lie outside all target sets; 15+m≤16. As it is actual, m=1. Distinct ONBs of B would share no ray (a shared ray fixes its unique perpendicular partner) and would therefore have four distinct rays, impossible.

## 4. Three-space capacity and three-block consequences

Let D be any complex three-plane, and v₁,…,v_N all its distinct actual Q rays. Tracing STAR(vᵢ) on D gives at least 10. For a cell with nonzero D projection, all tested rays perpendicular to that cell lie in one two-plane in D, and §3 bounds their number by 3. The total projected mass is 24, so 10N≤3·24=72 and N≤7.

Suppose N=7. For each ray select one actual occurrence and let dᵢ be its number of perpendicular partners among the seven. Its perpendicular plane contains at most three actual rays, so dᵢ≤3. The deficit in the foregoing mass inequality is at most 2; the seven selected occurrence cells alone contribute Σ(3−dᵢ), hence this sum is ≤2. It is odd because Σdᵢ is even and 3·7 is odd. Therefore it is 1: six vertices of the orthogonality graph have degree 3 and one has degree 2.

The three neighbors of each degree-3 vertex lie in a two-plane. By §3 those three contain exactly one orthopair, so that vertex lies in exactly one triangle. The degree-2 vertex lies in at most one triangle. Triangles are consequently vertex-disjoint. All six degree-3 vertices must be covered, and the number covered is a multiple of three between 6 and 7; exactly two triangles cover those six and leave the degree-2 vertex outside. Each triangle is a three-ONB of D. The six triangle vertices each have one edge outside their own triangle; at most two such endpoints meet the outside vertex, leaving at least two edges between the two triangles.

For two disjoint three-ONBs, two zero entries in the same transition row or column would leave a singleton and hence a shared basis ray. Two zeros in different rows and columns leave those two rows with exactly one possible common nonzero position; orthogonality forces an additional zero, again a singleton. Thus at most one zero is possible, contradicting the two cross edges. Therefore **N≤6**.

Two disjoint actual three-ONBs cannot have a full transition either: any three of their six rays would fail to lie in one two-plane (a pair from one basis plus a ray from the other would force a zero). Repeating the STAR trace count with multiplicity bound 2 would give 6·10≤2·24, impossible. A connected three-block has no common ray and at most one zero; it therefore has exactly one. Its six rays exhaust D. The unique zero joins an E-ray r to an F-ray s; s is the third ray in the plane of the other two E-rays and r is the third ray in the plane of the other two F-rays. Section 3 gives m(r)=m(s)=1. Their graph is two triangles joined by r–s, so these are the only two actual three-ONBs among the six rays.

## 5. Cross-image inequality and non-degeneracy

Let S be the real span of the component projectors. For an actual u, let T_u be the real span of projectors of u-orthogonal component rays, σ=dim T_u, and identify the image of Z↦P_u Z P_H on S with uχ* for χ in a real vector space L⊂H. Both P_u and T_u lie in the kernel and their sum is direct. Rank-nullity gives

b≥1+σ+dim_R L.  (∗)

L cannot lie in one complex line. Otherwise every u-active ray, i.e. ray nonorthogonal to u, lies in B=span(u,a) for some a∈H. Intrinsic connectedness supplies an actual mixed ray x in B. In an actual six-ONB containing x, u-inactive vectors orthogonal to x lie in B⊥, which has dimension four; among the other five vectors at least one is u-active and hence the unique in-plane orthogonal partner x′ is actual. Every other distinct star-x ray lies in B⊥, so STAR(x) evaluated at x′ forces m(x′)≥5, against GAP3. Thus dim_R L≥2. Under b≤12, (∗) gives σ≤9; if dim_R L=2, its complex span Π has dimension at most two.

## 6. Sparse five-unitary lemma

Suppose a connected-support 5×5 unitary had at least two zeros in every row and column, hence degree at most 3 everywhere. Degree 1 would isolate a 1×1 unitary block, so every degree is at least 2. If a row has support {1,2}, any other row meeting one of these columns must meet both, because two orthogonal rows cannot overlap in exactly one nonzero position. The two columns thus have the same row support, of size two or three. Size two gives an isolated 2×2 unitary block. At size three, the restrictions of the other two rows to {1,2} are nonzero multiples of the same vector perpendicular to the first restriction; their inner product there is nonzero. Orthogonality requires a common third coordinate, and the degree bound makes all three rows supported on the same three columns. They form an isolated 3×3 block. Both cases contradict connectedness. Transposition similarly rules out degree-2 columns.

All rows and columns then have degree 3. The five row zero-sets are two-subsets of the columns, and each column lies in two such sets. Any two zero-sets must intersect, for disjoint zero-sets would leave the corresponding row supports meeting in exactly one coordinate. Duplicate zero-sets would exhaust both column zero counts, forcing the other zero-sets to be disjoint from them. Hence the zero-sets are distinct edges of a simple 2-regular graph on five vertices, necessarily a five-cycle, which has disjoint edges: contradiction. Thus a connected 5×5 unitary has a row or column with at most one zero.

## 7. Connected five-block pivot

At a selected cell y, let E be its actual row five-ONB in H; each other line through y gives another actual five-ONB F. The intersection of their diagonal algebras consists of scalars on the connected support blocks of the transition: a diagonal operator common to both bases has equal eigenvalues along every nonzero support edge. Therefore a connected k-block adds k−1 independent off-diagonal dimensions to D_E. A connected 2-block would give two distinct actual two-ONBs in one plane, forbidden by §3. The remaining partitions are 5, 4+1, 3+1+1, and five singletons.

For a connected five-block, D_E+D_F has dimension 9, hence σ≥9. Under b≤12, (∗) and dim_R L≥2 force σ=9 and dim_R L=2, so T_u=D_E+D_F and dim_C Π≤2. By §6, interchange E and F if necessary and select an E-axis eᵢ with at most one F-zero. For any actual u-star ray v perpendicular to eᵢ, write P_v=D+Y with D E-diagonal and Y F-diagonal. The equation P_v eᵢ=0 makes eᵢ an eigenvector of Y. All Y eigenvalues on F-vectors having nonzero overlap with eᵢ agree. With no zero, Y is scalar and v is an E-axis. With one zero Fⱼ, absorb the common scalar into D and obtain P_v=D′+tP_{Fⱼ}, with real t.

Connectedness gives Fⱼ support on at least two E-axes. If t=0, v is an E-axis. Otherwise its rank-one off-diagonal support is exactly that of Fⱼ. On at least three supported coordinates, products of a triple of off-diagonal entries force t>0 and recover the corresponding rank-one diagonals; no outside coordinate can be nonzero, and trace one gives P_v=P_{Fⱼ}. With exactly two supported coordinates, §3 allows only the two E-axes and the already actual Fⱼ in their plane.

Choose nonzero ξ∈H perpendicular to Π, eᵢ and, if present, Fⱼ; these impose at most four complex dimensions in H≅C⁵. Every u-active ray has zero ξ overlap, and the u-inactive rays perpendicular to eᵢ are E-axes or Fⱼ. Fⱼ has zero ξ overlap and E-axes contribute at most 3‖ξ‖² by GAP3. STAR(eᵢ) demands at least 5‖ξ‖², contradiction.

## 8. The 4+1 pivot

Write H=A⊕Ce for the connected four-block and its shared E/F axis. The four-block supplies three independent A-off-directions. The E-off-diagonal image of T_u has dimension σ−5≤4; hence its A–e cross image has real dimension at most one. If zero, every u-star ray is pure A or e, and STAR(u) along e would give m(e)≥5.

If the cross image is one-dimensional, an actual mixed star ray generates it as a e*, and every mixed star ray lies in span(a,e). For a mixed x in this plane, the pure-A common-star rays of u and x lie in A∩a⊥, dimension three; pure e is not perpendicular to x. COMMON(u,x) requires the common-star rays to span the four-dimensional H∩x⊥, so the unique in-plane partner x′ is actual. The plane contains orthopair x,x′ and the distinct third ray e, so §3 gives m(e)=1. But E and F contain e at distinct cells on distinct net lines through y, giving m(e)≥2. Contradiction.

## 9. The 3+1+1 pivot and five-line obstruction

### 9.1 Forcing the pivot and setting up its cross image

If all five line bases through y equalled E, each E-ray would occur at five distinct cells, violating GAP3. A different line therefore has a 3+1+1 transition, since all other nontrivial partitions have been excluded. Let H=A⊕B with dim A=3 and B=span(e,f), the shared E/F singleton axes. Both e and f occur on the two distinct pivot lines, so their multiplicities are at least two. The connected A-block has two disjoint actual A-ONBs, exactly one cross zero, six total A-rays, unique rays r and s with r⊥s, and no other A-ONB, by §4.

The E-off-diagonal image O of T_u has dimension σ−5≤4 because D_E⊂T_u and its kernel under removal of E-diagonal parts is exactly D_E. The pivot A-block contributes a two-dimensional subspace V_A⊂O with no A–B cross. Thus the real A–B cross image X has dimension at most two.

### 9.2 Cross dimension zero or one

If X=0, all u-star rays are pure A or B. STAR(u) compressed to B has trace at least 10. Section 3 gives at most three B-rays, and if three occur the third has multiplicity one, so their total occurrence count is at most 3+3+1=7. Contradiction.

If dim_R X=1, an actual mixed ray gives its rank-one generator a b₀*, and every mixed u-star ray lies in span(a,b₀). The pure B-rays are e,f and at most one third ray w, necessarily nonorthogonal to both and of multiplicity one. If w is not perpendicular to b₀, no mixed ray is perpendicular to w. All common-star rays of u,w outside B are then in the three-dimensional A, while COMMON requires them to span H∩w⊥ of dimension four. The unique B-partner w′ must therefore be actual; it differs from e,f,w, contradicting the two-plane cap. Hence a possible third pure-B ray is only b₀⊥. Test STAR(u) along that direction: the weighted e,f contribution is at most 3 because their squared overlaps sum to one, the possible third contributes at most 1, and the pure-A and mixed rays contribute zero. This is at most 4, not 5.

### 9.3 Cross dimension two and factor alternatives

If dim_R X=2, then dim O=4 and ker(O→X)=V_A. A pure-B projector has zero cross image, so its E-off part lies in V_A, which has only A-off entries. It must therefore have no B-off entry and be e or f. X is spanned by rank-one crosses of actual mixed rays; choose two real-independent ones a₁b₁*, a₂b₂*.

If b₁,b₂ are complex-parallel, every mixed B-part has the same direction. STAR(u) in its B-perpendicular direction receives at most 3 from e,f and nothing else. If a₁,a₂ are complex-parallel, every mixed A-part is parallel to a₀. The six pure-A rays are the two pivot ONBs; their projector sum weighted by actual multiplicities is at most

3I_A+3I_A−2(P_r+P_s)=6I_A−2(P_r+P_s),

because all multiplicities are at most 3 and m(r)=m(s)=1. Choose nonzero η∈span(r,s)∩a₀⊥. Since r⊥s, the pure-A contribution along η is at most 4‖η‖², and every other star ray contributes zero, contradicting STAR(u).

Otherwise both pairs a₁,a₂ and b₁,b₂ are complex-independent. A real linear combination of the two rank-one crosses with both coefficients nonzero has rank two: independent column and row factors give a rank-two factorization. An actual mixed cross has rank one, so it must be a scalar multiple of one generator. Hence all mixed rays lie in C₁=span(a₁,b₁) or C₂=span(a₂,b₂), with both A-factors and both B-factors independent. This is the remaining algebraic pencil, not itself an asserted contradiction.

### 9.4 Actual five-net lines

A pure-only five-ONB of H must use e,f and a three-ONB in A, so it is one of the two pivot bases. Each contains its own globally unique r or s, already used on its pivot line. Thus at most two net lines through y are pure-only.

For a mixed five-ONB, let nᵢ be the number of its mixed rays in Cᵢ; nᵢ≤2. Independence makes the following list exhaustive.

* (1,0) or (0,1): the remaining pure A- and B-rays fit respectively in dimensions two and one, giving at most four vectors total.
* (1,1): pure A-rays fit in A∩a₁⊥∩a₂⊥, dimension one, and no pure B-ray is perpendicular to both independent B-factors. At most three vectors result.
* (2,0) or (0,2): the two mixed rays are an ONB of Cᵢ. Completing to five requires a pure-B ray bᵢ⊥, which must be e or f; hence bᵢ is the other actual B-axis. The two mixed rays and bᵢ are three rays in Cᵢ, forcing m(bᵢ)=1 by §3, contradicting m(e),m(f)≥2.
* If one nᵢ is 2 and the other is positive, orthogonality to the first mixed in-plane ONB forces both a₁⊥a₂ and b₁⊥b₂. With only one mixed ray in the other plane, at most one pure-A and no pure-B ray remain, so five vectors cannot be reached. Thus (2,2) is necessary, and its fifth ray is the unique pure-A direction t=A∩a₁⊥∩a₂⊥.

Every possible mixed line therefore contains the same actual t. It is one of the six A-rays and already occurs on one of the pivot net lines. Its multiplicity is at most 3, and the five net lines through y share no other cell, so at most two further lines can be mixed. At most two are pure-only; four cannot account for the five actual net lines. This contradicts b≤12 and proves b≥13 at the stated scope.

## 10. Independent finite exact controls

A reviewer-authored script, `reviewer-exact-controls-v1.py`, reads no author code or frozen body. Its SHA-256, measured before execution, was `dde4f78a8b8770718266b6941e082fd8cf8d1be234f0e62091ca54d735fd2793`. The bounded run used `python3 -B`, with `/bin/date` observations **2026-10-29T13:36:04-0700 PDT** before the run and **2026-10-29T13:36:05-0700 PDT** after it; exit code **0**. It was subject to a 120-second maximum, did not time out, and used exact integer/Fraction arithmetic. These are finite controls of necessary support conditions, not a replacement for the written proofs or an exhaustive search of complex unitary phases.

* For 3×3 support patterns, imposing no row/column singleton and forbidding one-position row/column overlaps leaves **10** of 512 zero patterns: full support and the nine one-zero patterns. Intended-reason negative: two diagonal zeros preserve the minimum degrees but cause a row overlap of exactly one, and are rejected. The full-support pattern is deliberately retained: unitarity alone does not exclude it; the STAR mass argument is needed.
* For 5×5 supports with all row/column degrees 2 or 3, the script examined **42,504** row-support multisets, i.e. up to row permutation. **50** satisfy the necessary row/column overlap conditions and **0** of those are connected. Intended-reason negative: an actual exact rational orthogonal 2+3 block passes these support conditions but is disconnected; connectedness cannot be dropped from U5. A connected cyclic 3-regular support is rejected because two rows overlap in exactly one position; graph connectivity/regularity alone does not make a unitary.
* For seven-vertex graphs with degree sequence (3,3,3,3,3,3,2), fixing the last vertex as degree 2, **810** graphs occur. Requiring the degree-3 vertices each to have exactly one edge among their neighbors leaves **180**; all have two disjoint triangles with exactly two cross edges, and **0** cross supports meet the necessary conditions for disjoint three-ONBs. Intended-reason negative: the degree-only graph with edges `{01,02,03,12,13,24,35,45,46,56}` is rejected because vertex 0 has two, not one, edges among its neighbors. Thus degree sequence alone is not silently substituted for the two-plane local property.

## 11. Imports, remaining gaps, and process deviations

**Only adopted mathematical import:** GAP3 from the first pinned disposition, at its actual scope: in any ordinary four-MOQLS(8), each nonfixed ray has global multiplicity at most 3. Every ray used here lies in the nontrivial intrinsic C6 component and is nonfixed. The earlier unrestricted LOCAL6≥12 is context only, not an input to the proof. The second pinned disposition supplies interface definitions for orientation only: §1 independently derives the actual five-net and component restrictions. No C4/C5/LOCAL6/qutrit theorem, author PASS, linked body, solver status, literature claim, f197/f211 verdict, or other review is imported. No author code was run, imported, or compiled.

**Remaining gap:** this argument leaves all actual C6 cases with b≥13 and all other q1 components and gluing constraints open; it does not prove no-C6, settle q1/q4, or establish existence, maximum-three, or novelty. Ordinary written reconstruction is not a formal proof certificate.

**Process deviation, M=1:** I wrote the reviewer-owned control script before observing `/bin/date`; the first native observation was the control-start clock above. The script's pre-write native clock is therefore unavailable, and no creation time is asserted. The control's start/end clocks, measured script hash and exit code, and the report's pre-write clock are recorded. No other contract deviation is known.

This same-harness review is **not human, independent-model-family, formal/kernel, or novelty verification**. It does not constitute an independent-family or parent acceptance decision.
