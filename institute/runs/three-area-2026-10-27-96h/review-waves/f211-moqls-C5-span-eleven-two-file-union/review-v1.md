# f211: independent same-harness review of the complete C5 two-file union

**Disposition: 0 F / 0 M / 0 m; 1 INCONCLUSIVE item.** The predecessor's scoped conclusions and the completion's LOCAL5 ≥ 11 conclusion are independently supported by the written reconstruction below, using GAP3 and no unverified module statement. The one INCONCLUSIVE item is whether the predecessor's four listed caller conditions are exactly the hypotheses of the historical Gate 6 theorem: the permitted parent disposition names that theorem but does not print its formal hypotheses. This is a dependency-identification uncertainty, not a counterexample or an unresolved step in the alternate reconstruction below. This review is not parent adoption.

Native `/bin/date` observation before writing this review: **2026-10-29T13:17:36-0700 PDT**. This is an observation before the write, not a claimed file-creation time.

## Freeze, inputs, actual read sequence

The manifest was the first research artifact opened. Its observed SHA-256 was `c3e273118cfbd951907789943f519f4d6ecae499f0cad69794e2aeec164a1ab3`, matching the assigned prefix `c3e273118cfb`. Before opening any input body, I measured SHA-256, bytes and LF for **all three** inputs; all agreed with the manifest. In the manifest's order, I then displayed every line using these actual short raw windows, including the final lines, before mathematical reconstruction or controls:

| Input and manifest role | Observed SHA-256 | Bytes / LF | Actual `:raw` windows, inclusive |
|---|---|---:|---|
| `institute/runs/three-area-2026-10-23-96h/MOQLS-unrestricted-four-family-ray-gap-intrinsic-and-local-span-budget-entire-parent-v1.md`, prior disposition | `2e254b56d108994844cf337c31b98fa851effca15a68a847c6cb2db84552bee4` | 9675 / 63 | 1–15, 16–30, 31–45, 46–60, 61–63 |
| `physics/evidence/three-area-20261027-96h/parallel-18/moqls8/frontier-20261029-C5-span-ten-no-Lagrangian-ray-v1.md`, predecessor P | `d4a47f3456399fa9da42a36253e30e1b73b035b64c7c1e36808cf9547969444b` | 15439 / 115 | 1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–105, 106–115 |
| `physics/evidence/three-area-20261027-96h/parallel-18/moqls8/frontier-20261029-C5-span-eleven-completion-v1.md`, completion C | `0b1fe8d135faa4d55cc136f80832c9a910d208ec18fcfc28e37f42eab413510c` | 11334 / 96 | 1–15, 16–30, 31–45, 46–60, 61–75, 76–90, 91–96 |

The disposition's Gate 1 is the only mathematical theorem imported in the independent argument: a nonfixed ray has multiplicity at most three. A multiplicity-eight fixed ray is orthogonal to every other Q-ray, because it occurs once in every row; it is therefore a singleton intrinsic component and cannot belong to the five-dimensional component. Thus every ray used below has multiplicity at most three. The disposition names Gate 6's tested-qutrit span-five virtual-anchor obstruction, but does not enumerate its hypotheses or conclusion. Its linked body was not opened, and its exact caller match is not silently assumed here. No other old result, author script, author PASS/receipt, solver result, sibling review, web/literature/model output, or held material is used as evidence.

## Claim-by-claim dispositions

`0F/0M/0m` means no defect was found in the stated reconstruction, not a formal certification. The theorem-match uncertainty is separately marked rather than passed by inference.

| Source / claim | Verdict | Independent basis |
|---|---|---|
| P §§1–2; C §1: component setup, exact per-mate off-line resolution, disjoint weights, C5-STAR and no isolated star ray | 0F/0M/0m | §1 below derives the identities from the actual product ONBs and GAP3. |
| P §3: real cross image has dimension ≥2; a two-real-dimensional image is isotropic/Lagrangian | 0F/0M/0m | §2, including the otherwise vacuous zero-image case. |
| P §4: at least three projective directions in the two-dimensional case | 0F/0M/0m | §3 gives the closed partner orbit and the finite-minimum contradiction. |
| P §5: K-MASS, at least three independent pure-K projectors, and `h0≥5`, with `P_A∈H0` at equality | 0F/0M/0m | §4 derives the operator count and handles both active-line cases. |
| P §§6–7: exclude cross-image dimensions 0 and 1; obtain SAT; classify every two-dimensional rank-one pencil and exclude it | 0F/0M/0m | §5 includes a direct proof of the common-A case, independent of the qutrit-module import. |
| P §7, specifically the assertion that the four printed conditions match the *exact* adopted qutrit theorem | **INCONCLUSIVE** | The caller geometry is independently checked in §5, but the pinned disposition supplies only the theorem's name, not a literal signature against which to compare it. No linked body is permitted. The direct proof makes the scoped exclusion independent of this uncertainty. |
| P §8; C §1: star span ≥6, `(EQ)`, kernel equality and `(EXACT)` under `b≤10` | 0F/0M/0m | §§1 and 6 provide the off-diagonal classification and dimension count. |
| C §§2–3: existence of a nonmonomial pivot; connected-block count; 3+1 impossible; 2+2 yields SPLIT | 0F/0M/0m | §7 proves each possible transition partition. |
| C §4: all of 2+1+1, including the common-direction positivity and three distinct off-line cells | 0F/0M/0m | §8 uses the **exact** three weighted identities and disjointness, not merely an unweighted bound. |
| C §§5–6: block-positive rank argument, forbidden tested two-plane, and LOCAL5 ≥ 11 | 0F/0M/0m | §9 derives the contradiction for arbitrary complex families. |
| C §6's conditional LOCAL4/q4 bridge, its separately cited C4 candidate, A10/A11, and global existence/nonexistence | OUT OF SCOPE, not evaluated | The manifest explicitly excludes LOCAL4/q4 claims; no other candidate or linked body was opened. No conclusion on those claims is implied. |

## 1. Exact identity, star inequality, and isolated stars

Let a component have complex span W of dimension five, and let `P_v` denote a rank-one projector. Its rays and those of other intrinsic components are mutually orthogonal. Compressing any full row or column resolution to W gives a five-ONB of actual component rays; there are 40 component cells and `sum_C P_z=8P_W` by summing rows.

Fix a cell y with Q-ray u and one mate X. Taking the X_y partial matrix element of the complete Q–X product-ONB resolution gives `sum_z |<X_y,X_z>|² P_z=I_8`. The y term is `P_u`; X-orthogonality removes every other cell in y's row and column. At an off-line cell, product orthogonality removes it unless its Q-ray is perpendicular to u. Compression to W is therefore the exact identity

`sum_{z in C, off y's row/column, Q_z⊥u} |<X_y,X_z>|² P_z = P_W-P_u`.  (EXACT)

At each cell z, weights from two different mates cannot both be nonzero, since their same-cell product vectors must be orthogonal; each weight is at most one. Summing the three identities and adding the two disjoint four-ray row and column stars yields

`A_u := sum_{z in C, Q_z⊥u} P_z ≥ 5(P_W-P_u)`.  (STAR)

If a star ray w were perpendicular to every other distinct star ray, evaluating STAR at w would give its total cell multiplicity at least five, contrary to GAP3. This no-isolated-star rule is used only for actual rays.

## 2. Minimum cross dimension and the isotropic two-dimensional case

Write the real cross image relative to actual u as `{u χ*: χ∈L_u}`. After phasing an active ray v as `v=αu+λ`, `α>0`, its perpendicular part λ is in `L_u` up to a nonzero real scaling. An intrinsic component of dimension five contains a distinct ray nonorthogonal to u; otherwise u would itself form a singleton component.

If `L_u` were contained in one complex line, all active rays would lie in a fixed two-plane B containing u. For a mixed actual x in B, every u-inactive star-x ray lies in `B⊥`, of dimension three. A five-ONB through x must therefore contain the unique B-partner x'. It is orthogonal to every other distinct star-x ray, contradicting STAR. This also covers a one-real-dimensional image; the zero-image case contradicts irreducibility directly. Hence `dim_R L_u≥2`.

Suppose `dim_R L_u=2` and `Im<.,.>` is nonzero on it. This alternating form is then nondegenerate. Orthogonality of two active phase-fixed rays forces their perpendicular parts to have zero alternating pairing and therefore to be real-proportional. The same B-partner/isolated-star argument is forced for each mixed x, a contradiction. Thus the form vanishes. Since the real image is not in a complex line, `Xi=R u+L_u` is a real Euclidean three-space with complexification A of dimension three. Put `Pi=A∩u⊥` and `K=W∩A⊥`, each complex two-dimensional. All active rays are real in Xi, all outside-A rays are u-inactive, and their A-projections lie in Pi. `H0`, the real span of P_u and the actual active projectors, lies in `Sym(Xi)`.

## 3. At least three projective directions

If only one direction in Pi occurred, L_u would be contained in one complex line. Suppose exactly two, λ1 and λ2. Any component line not containing u has at least two active entries: the expansion of u cannot consist of a single distinct active ray. It has at most two, since three would include two in the same `span(u,λi)`, whose orthogonal pair spans that plane and forces the third entry to be u-inactive. With exactly two, the expansion of u places u in their span, so they share one λi direction and form the actual in-plane partner pair.

For an actual mixed x in plane 1, if no mixed plane-2 ray were perpendicular to x, its in-plane partner would be isolated in star x. Hence a cross-plane partner exists, and likewise after exchanging the planes. For unit directions let `κ=<λ1,λ2>`. The planes are distinct and a cross-plane orthogonal pair exists, so `0<|κ|<1`. Writing x proportional to `u+rλ1`, successive cross-plane, in-plane, cross-plane, in-plane partners have ratios

`-1/(κ conjugate(r))`, `conjugate(κ)r`, `-1/(|κ|² conjugate(r))`, `|κ|²r`.

All are actual. Repeating strictly decreases the modulus in the finite nonempty set of actual plane-1 ratios, a contradiction. At least three directions occur.

## 4. K mass and the five-dimensional active span

For each of three distinct λ directions choose a mixed active x. A u-inactive star-x ray lies in `V_λ=K+(Pi∩λ⊥)`; active rays have no K part. Compressing STAR to K gives at least `5I_K` from cells in V_λ. The three V_λ intersect pairwise exactly in K; an outside-K ray is counted at most once. For `M_K=sum_{z∈C,Q_z∈K}P_z`, the three inequalities and `sum_C P_z=8P_W` give

`15I_K≤8I_K+2M_K`, hence `M_K≥(7/2)I_K`.  (K-MASS)

Its trace gives at least seven pure-K cells. GAP3 gives at least three distinct K rays, and three distinct complex-qubit rank-one projectors are real-linearly independent: their trace-one Bloch points lie on a sphere, which a line meets in at most two points. Thus `dim H_K≥3`.

A line without u has two or three active entries, the latter because A has dimension three. With two, their expansion of u makes them an orthogonal pair in one real plane `Ru+Rλ`; their projectors and P_u span its three-dimensional real symmetric algebra. With three, the active entries form a real ONB E of Xi and their projector sum is P_A.

If a three-active line exists but `dim H0≤4`, its three E-diagonal projectors and P_u already span H0, since all three E-coordinates of u are nonzero. For a non-E rank-one real projector in that space, its three off-diagonal entries are a common scalar multiple of those of P_u. Rank-one identities recover each diagonal from a triple of off-entries; normalization makes the projector P_u itself. Therefore the only active rays would be u and the three E rays. No two-active line could expand u in two E rays; every row not containing u would have to contain all three E rays. There are at least `8-m(u)≥5` such rows, contradicting GAP3.

If no three-active line exists, each of three distinct λ directions supplies a closed active pair. The three real-qubit projectors P_λ span `Sym(Pi_R)`, while P_u and two independent cross directions supply the remaining dimensions. Thus `dim H0=6`. In all cases `h0:=dim H0≥5`; if `h0=5`, a three-active line exists and `P_A∈H0`.

## 5. Saturation, all rank-one pencils, and an independent common-A exclusion

Let X be the image of `Z↦P_A Z P_K` on S. Its kernel contains the direct sum `H0+H_K`, so `dim_R X≤10-h0-dim H_K`. If X is zero, every actual ray lies in A or K, contradicting intrinsic irreducibility. If X has real dimension one, every mixed ray has the same A and K factor directions. Choose an actual pure-K ray w not perpendicular to that K direction; among the at least three K rays such a w exists. Any outside-K star-w ray lies in A. A five-ONB through w must include its unique K-partner, which is isolated in star w. Thus `dim X≥2`, and all inequalities saturate:

`b=10`, `h0=5`, `dim H_K=3`, `dim_R X=2`, and `ker(cross)=H0⊕H_K`.  (SAT)

Consequently every pure-A actual projector belongs to H0 and has a real representative in Xi, and `P_A∈H0`.

Choose two real-independent actual rank-one cross generators. If their A factors are parallel, every mixed A factor has that common direction; if their K factors are parallel, every mixed K factor has that common direction. If both factor pairs are complex-independent, a combination with both real coefficients nonzero has rank two, so a rank-one actual cross uses only one generator. These cases exhaust the pencil, including complex-scalar multiples. In the common-K and independent-two-direction cases there are at most two mixed K directions. One of the at least three actual K rays is perpendicular to neither; its line completion again forces an isolated K partner. Only the common-A case remains.

Let all mixed A projections be along unit a0. A line containing a mixed ray has exactly two pure-A entries, an ONB of `A∩a0⊥`: mixed vectors are orthogonal to any pure-A entries, and compressing the five-ONB resolution to `A∩a0⊥` forces those entries to span it. Lines without mixed rays have a complete A-ONB. For one mixed line its pure-A projectors are in H0; subtracting them from `P_A∈H0` shows `P_a0∈H0`, so a0 can be phase-real in Xi. All other intrinsic components project zero to A. GAP3 bounds every actual A-ray multiplicity. Moreover, if the locally completed real A bases were disconnected in the real frame `(a0,e1,e2)`, the active generators of H0 would be block diagonal in a nontrivial partition, giving dimension at most `3+1=4`, not five. These are the four caller facts the predecessor lists. The disposition does not itself print the corresponding theorem signature, so the exact historical caller identification remains INCONCLUSIVE.

The common-A case can nevertheless be excluded directly, without assuming that signature:

1. `H0` is a five-dimensional subspace of the six-dimensional real symmetric matrices on Xi. Choose nonzero real symmetric M perpendicular to H0 for the trace pairing, and write `q(v)=v^T M v`. Every pure-A actual ray has a real representative v with `q(v)=0`; also `q(a0)=0` because `P_a0∈H0`.
2. There is an actual pure-A ray w with `<w,a0>≠0`: otherwise all generators of H0 lie in the real two-plane `a0⊥`, whose symmetric projector span has dimension at most three. If an outside-A ray is perpendicular to this w, its A projection is zero, because that projection is a multiple of a0. Thus compression of STAR for w to A gives at least `5(P_A-P_w)` entirely from pure-A star rays. Its trace is at least ten.
3. If the real quadratic form q restricted to the two-plane `w⊥∩Xi` were nonzero, its zero set there would contain at most two projective real directions. GAP3 would bound their total cell multiplicity, and hence the trace just counted, by six. Contradiction. Thus this restricted form is identically zero. Since `q(w)=0` as well, in real orthonormal coordinates `M=w v^T+v w^T` for a nonzero v perpendicular to w.
4. The same argument applies to every actual pure-A ray nonorthogonal to a0. Any ray w' with `q(w')=0` and `q|_{w'⊥}=0` must lie in `im M=span(w,v)` and, there, is one of exactly the two orthogonal projective directions w and v. Because `q(a0)=0`, a0 is perpendicular to at least one of these two directions. Hence **at most one** actual pure-A direction is nonorthogonal to a0; call it w.
5. In an actual component five-ONB containing w, every outside-A ray has zero A projection. Compressing that ONB to A therefore gives three pure-A ONB rays, including w. The other two are perpendicular to both w and a0. Unless w is parallel to a0, that common perpendicular in A has complex dimension one, impossible. If w is parallel to a0, every pure-A ray lies either on a0 or in `a0⊥`, so the real span of their projectors has dimension at most `1+3=4`, again contradicting `dim H0=5`.

This independently excludes the common-A pencil and therefore the entire `dim_R L_u=2` case. It uses only the already-derived STAR, saturation, elementary real quadratic geometry, and GAP3.

## 6. Star span and the exact all-ray equality

For any actual u, take a four-ONB E of `H=W∩u⊥` from a row through u. Its diagonal algebra has dimension four. Suppose the off-diagonal image of the actual star-projector span has real dimension at most one. If it is zero, all star rays are E axes and an axis is isolated. Otherwise choose a non-axis star ray. Its nonzero off-diagonal support is the complete graph on its coordinate support, and every other non-axis star ray has that same off-diagonal support. If this support has two vertices, every non-axis star ray lies in that coordinate two-plane; an E axis outside it is isolated. If it has at least three vertices, the triple-product rank-one identities and normalization determine the non-axis projector uniquely. A unit vector perpendicular to that single ray sees at most three total weight from the E axes, because each axis multiplicity is at most three, contrary to STAR's weight at least five. Thus `σ_u≥6`.

The kernel of the u-cross map contains `R P_u` and the actual star span, directly. Therefore `b≥1+σ_u+dim_R L_u`. The previous sections give `dim_R L_u≥3` under `b≤10`, so necessarily

`b=10`, `σ_u=6`, `dim_R L_u=3`, and `S∩BD_u=R P_u⊕span_R{P_v:v⊥u, v actual}`.

This holds for **every** actual u, not just the chosen pivot. EXACT was independently derived in §1. These are the predecessor's EQ and kernel identity, and the completion's precise inputs.

## 7. Pivot and the 3+1 / 2+2 cases

If every component cell had the same unordered row and column component ONB, fix a row basis E. Its five cells lie in five distinct columns; each such column would have component basis E. Every E ray would then occur at least five times, contrary to GAP3. Hence an actual nonmonomial pivot y exists. Its row and column share u; removing u gives distinct four-ONBs E,F of H. The entire star span has dimension six and contains the four-dimensional E-diagonal algebra, so its off-diagonal image V has real dimension two.

For a unitary transition, a Hermitian operator diagonal in both bases is constant on each connected component of the bipartite support graph: every F vector is an eigenvector, and its nonzero E coordinates must share an eigenvalue. Conversely one scalar per block works. Thus `dim(D_E∩D_F)` is the number of connected blocks, and F contributes `4−number_of_blocks` independent off-diagonal directions. A connected 4-block would contribute three and is impossible. The nonmonomial possibilities are 3+1, 2+2, and 2+1+1.

For 3+1, the two F directions exhaust V on the three-coordinate block. Every actual star projector has zero cross to the fourth E axis; rank-one purity places its ray either in the three-space or on that axis, making the axis isolated. For 2+2, the two block directions exhaust V, so every star ray is in one of the two orthogonal coordinate planes B,D. Each plane contains two different actual two-ONBs and has a three-dimensional projector span. This is SPLIT.

## 8. The full 2+1+1 pivot and exact weighted counting

Let B be the rotated plane and D the two unchanged actual axes g,h. The rotation contributes a nonzero pure-B off-diagonal direction `Z_B∈V`; therefore the B–D cross image of V has dimension at most one. If it is zero, every star ray is in B or D. Neither plane can consist solely of its two E axes, since then those axes are isolated. At least three distinct qubit rays in each plane span at least three real projector dimensions; the total star span six forces exactly three in each, yielding SPLIT.

If the cross image has dimension one, an actual mixed star projector supplies its rank-one generator `b0 d0*`, and every mixed star ray has B and D factors parallel to b0 and d0. The kernel of the cross map on V is `R Z_B`; a pure-D star projector has no B off-entry and hence no off-entry at all. Its ray is therefore g or h. If d0 is an axis, the other is isolated. Otherwise its D off-diagonal entry is nonzero. In **any positive** actual-star resolution of `I_H`, the D off-diagonal is `c Off(P_d0)` with `c≥0`, since pure-D contributions are diagonal and every mixed contribution has the same D direction. It must vanish, so c is zero and every mixed term has zero weight; the g and h terms each have total weight one.

Apply this to each of the three EXACT off-line resolutions for y. Each mate contributes total g weight one. At each individual off-line g-cell the three mate weights sum to at most one, so there must be at least three distinct off-line g-cells. The unchanged g also occurs once in y's row and once in y's column, in different cells. Thus `m(g)≥5`, contradicting GAP3. The analogous count holds for h. This eliminates the one-dimensional-cross case; every nonmonomial pivot yields SPLIT. An unweighted STAR inequality alone would not justify discarding mixed terms.

## 9. Positive rank and LOCAL5 ≥ 11

For SPLIT, let U be all component cells with nonzero u-overlap and set

`F=sum_{z∈U} P_H P_z P_H`.

The other cells are star rays in B or D. Since the sum over all component cells compresses to `8I_H`, F is block diagonal, `F_B⊕F_D`. Positivity shows its range is the complex span of the projected active vectors. After a nonzero real rescaling these lie in the real three-dimensional image L_u, hence `rank F_B+rank F_D≤3`. Both blocks are nonzero: a zero B block would put all active rays in `B⊥`, while all inactive rays lie in B or D, splitting the intrinsic component orthogonally. The same holds for D. Thus one block has rank one; let its range in B be `C b0`.

Every active ray has B projection parallel to b0, and every inactive ray outside B has zero B projection. SPLIT supplies at least three distinct actual B rays, so one w is neither b0 nor its orthogonal ray. Any actual outside-B ray perpendicular to w has zero B projection and lies in `B⊥`, which has dimension three in W. A five-ONB through w must contain its unique B-partner w'. Every other distinct star-w ray is perpendicular to w', making w' isolated, contrary to STAR and GAP3. Therefore `b≤10` is impossible. The resulting written conclusion is exactly: **every intrinsic C5 of every member of an ordinary four-MOQLS(8) has real projector span at least eleven.** No LOCAL4 or q4 consequence is asserted here.

## Independent exact controls and limitations

I wrote and ran only the reviewer-owned `reviewer-exact-controls.py` in this wave directory; it does not import or execute author code. Native clock before the run: `2026-10-29T13:16:47-0700 PDT`; after: `2026-10-29T13:16:47-0700 PDT`. Script SHA-256: `ac93ff85286d2f30967f47037530c8478826e527fd8b0773d69b6b179a84e24e`; exit code **0**, with a 120-second run deadline.

* Exact integer sampling of 124 nonzero zero-diagonal real symmetric matrices and 49 primitive projective rational directions checked 1,044 nonzero and 120 zero restricted quadratic forms, plus 1,164 anchor cases. The tests found at most two null directions when the restriction was nonzero and checked the exceptional-direction and anchor consequences. This is a **finite control**, not exclusion of unsampled continuous configurations; the proof is §5.
* Exhausting half-integer cell-weight triples with total at most one found 0, 0, and 21 assignments for respectively one, two, and three cells to supply unit weight to all three mates. This checks the counting mechanism, not all real weights; the general argument is the sum bound in §8.
* Intended-reason negatives were observed: opposite mixed D directions cancel to `I_D` if the common-direction hypothesis is removed; two orthogonal rays of multiplicity five meet the trace-10 bound if GAP3 is removed; and one cell can supply all three mates if disjointness is removed. These are sensitivity controls, not physical four-MOQLS constructions.

## Imports, remaining gap, and deviations

The only mathematically used imported theorem is GAP3 at its stated nonfixed-ray scope. The Gate 6 qutrit module is named but its formal caller match remains the one INCONCLUSIVE item; the alternate common-A proof above avoids needing it. No residual gap was found in the stated LOCAL5 reconstruction, subject to ordinary written-proof review and the explicit assumptions above. This does not resolve the separately excluded LOCAL4/q4 bridge, global family existence, or novelty.

No contract deviation is identified. Input bodies were read fully, in the prescribed order, before the mathematical work; the measured manifest and all input bindings matched. No author code, other source body, solver result, external search, other model, sibling review, author contact, Git operation, publication, deletion, or infrastructure mutation was used. The reviewer-owned finite control is not a build, lint, formatter, or author test.

**Same-harness review is not human review, independent-model-family review, formal or kernel verification, or novelty verification.**
