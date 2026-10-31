# f21 — independent review of the three-party support obstruction

Reviewer **MathSemigroup-2**, math-4; author **PhysicsAME46-2**, physics-6. Native prewrite observation: **Wed Oct 28 17:20:33 PDT 2026**. Assignment SHA `68c2fb5ff702956a2151b96a440cc19b1b9c70dfe841d53a86d53c71a9bff304`.

## 1. Verdict and exact scope

**NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE — 0 FATAL / 0 MAJOR / 0 MINOR.**

For the **one explicit published real 60-term tensor** of Pandya's Table 1, every choice of one fixed spectator and every triple of arbitrary invertible complex local maps on the other three parties yields at least60 nonzero coefficients. The identity triple attains60, so the restricted GL-orbit minimum is exactly60. The same holds when the spectator map is monomial (in particular monomial unitary), by permutation/rescaling of its six slices. Therefore any product unitary making THIS tensor's support below60 must have four nonmonomial factors.

This is a **specific-orbit** statement, not a lower bound for every AME(4,6) tensor, not a four-party-orbit no-go, not a global minimum/novelty result and not a sub-60 witness. Nothing about physical local unitaries is assumed in the stronger GL lower-bound proof. Same-harness written review and exact finite checks are not formal/kernel, independent-model/human or complete source-priority acceptance.

## 2. Inputs, provenance and independently exercised checks

Complete candidate `frontier-20261028-three-party-orbit-obstruction-v1.md` is75LF, SHA `81d66a899197064107351d703fda6fbedb7ec7842766c39d1168af27dd8fc07d`, matched by native `shasum`. I also read the complete earlier candidate `frontier-20261028-two-party-orbit-obstruction-v1.md`, SHA `94f85389567b2a3ea8e8f1a418af58977f4fdc3670f4a696fa6512703b7a9f75`, and the registered33LF AME definition packet, SHA `07d0ecd8964839862d06c09fda5e444ad5713501438d3c0e04d4e42522c03b01`. The earlier orbit-bound claims and advertised author's results are not proof premises for the present result.

I read the public primary [Pandya, arXiv:2610.16673v1, Table 1 and Proposition 1](https://arxiv.org/html/2610.16673v1#S2.T1). Its36 officer cells and signs/sqrt(2) values were independently transcribed into the new checker and compared visually to the displayed primary table. The separate local author table `frontier-20261028-pandya-table-v1.txt`, SHA `cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38`, is read bytewise by that checker; all36 of its cells match my transcription exactly. This is a primary-table comparison, not a claim of independent discovery of the published tensor.

The new standalone program `frontier-review-f21-independent-support-check-v1.py`, SHA `4e446149a509cc34c0bd9686c6205e2fe075ffda905c2e77027e5024ce3b5931`, imports **no author parser, engine, certificate, checker or output**. It uses only standard-library integer tuples to represent a+b√2, exact support sets and graph traversal. Actual command, timeout30s and exit0 at **Wed Oct 28 17:20:11 PDT 2026**:

```text
/opt/homebrew/bin/python3 mathematics/evidence/three-area-20261027-96h/parallel-18/semigroup-embedding/frontier-review-f21-independent-support-check-v1.py physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261028-pandya-table-v1.txt

table_sha256=cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38
source_table_cells=36 support=60 sqrt2_coefficients=12
PASS primary-transcription equality; all six exact two-party Gram marginals = 2I before normalization
pencils=72 pencil12=24 pencil9=48 rectangular_masks=144
PASS all 24 spectator slices, all 63 nonempty masks per pencil, ownership and graph structures
CONTROL deleting one source-table coefficient rejected at primary-transcription comparison
```

The control detects a changed table at the primary-comparison predicate; it is not a complete mask-checker mutation suite. The manual transcription and its comparison are one reviewer's source reading, not an independent-family attestation or exhaustive proof of every conceivable transcription error. No floating-point zero threshold is involved.

Prior same-harness contacts include the w20/w58 AME reviews and QOA source-only work; these are disclosed familiarity, not blindness or an unaffected-cognition claim. No author contact or historical held result was used as a proof premise. The owner-direction now permits the named public source and bounded exact scientific verification prospectively; this does not retroactively validate any previous quarantined result.

## 3. Exact tensor/source validation

The program parses the36 ordered A,B cells, rejects repeated/out-of-range coordinates and malformed coefficients, and builds a four-index support with exactly60 distinct entries. It independently requires12 coefficients √2 and48 coefficients ±1 before the common 1/√72 normalization. The complete text of its36-cell `SOURCE` constant was typed from the public Table 1, rather than imported from an author checker; equality to the local data includes each sign and each CD coordinate.

For each of the six choices of a two-party subsystem, and for every ordered pair of its36 basis indices, the program groups tensor entries by the SAME complementary two-party index and computes the real Gram sum exactly in Z[√2]. It obtains2 on every diagonal and0 off diagonal in the unnormalized table. Division by72 therefore gives I/36 in all six actual reduced states; the trace is one. This independently confirms the witness's normalization and all six AME conditions on the **same** tensor. It is not a derivation of any all-AME support lower bound.

The original registered problem quantifies over all complex AME states and all physical product bases. Our verified tensor is one legitimate element; the following restricted-orbit conclusion must not be substituted for that original universal minimization.

## 4. General pencil lemma — full quantifiers

Let `T=Σ_(j=1)^d e_j⊗M_j ∈ A⊗B⊗C`, with the d matrices M_j linearly independent. Let `L={x∈C^d: rank(M(x))≤1}`, M(x)=Σ_j x_j M_j, and suppose L lies in a subspace W of dimension w. Necessarily 0<=w<=d.

Apply any invertible linear map A0 on A and invertible maps U,V on B,C. The d coefficient rows of A0 give a basis x_1,...,x_d of C^d. Because the M_j are independent, each basis vector x_i is nonzero and M(x_i) is nonzero. The transformed i-th slice is `U M(x_i) V^T`, with exactly the same rank. At most w members of a basis can lie in W, since those members would otherwise be a linearly independent set of size>w inside W. Thus at least d-w slices have rank>=2 and the remaining slices have rank>=1.

Any matrix has at least as many nonzero entries as its rank: rank is at most the number of nonzero rows and every nonzero row requires an entry. The A-index slices have disjoint coefficient positions, so summing their supports gives at least

`w·1+(d-w)·2=2d-w`.

This remains correct if fewer than w basis vectors are in W, if L contains only zero (take W=0), if w=d, or if all matrices outside W have rank larger than2. No assumption that all vectors in W actually give rank1 is needed. Coefficients and local maps are arbitrary complex numbers; no scalar realness or unitarity is required.

## 5. Independently verified ownership and all 63 masks

For each spectator party s∈{1,2,3,4}, each level t∈{0,...,5}, and each of the other three choices of A pencil axis, use the remaining two axes as matrix rows and columns. This is exactly 4·6·3=72 pencils. The independent program constructs each pencil directly from the same60 source coefficients and confirms:

1. All six generators in every pencil are nonzero. No matrix cell belongs to two different variables. Thus they are linearly independent: inspecting a cell owned by any chosen j forces x_j=0 in a vanishing combination.
2. For each of the 24 12-entry pencils, every one of the63 nonempty variable masks gives a nonrectangular union of cell supports. Their full edge graph is a connected bipartite12-cycle, and each variable owns two edges with distinct rows and distinct columns.
3. For each of the 48 9-entry pencils, precisely three of the63 masks give rectangular unions; they are singleton masks for the three one-entry generators. The full graph is one6-cycle plus three disjoint isolated edges, and the three two-entry generators each own two edges with distinct rows and columns.

The counts apply to **all** spectators/levels/axis choices, not only one selected orientation. The independent program separately checks the stronger graph component/degrees and ownership claims, in addition to enumerating every mask; 48·3=144 rectangular masks in total. All24 spectator-level slice counts are `(9,12,12,9,9,9)` in the order0,...,5.

Why this finite combinatorics is sufficient: in a pencil matrix, every cell is either0 or a fixed nonzero coefficient times **one** variable. Therefore a complex variable is nonzero iff all its owned cells appear in support, and two variables cannot cancel in one cell. For a nonzero rank-one matrix `u v^T`, the nonzero cells are exactly supp(u)×supp(v), a nonempty rectangle. Thus a nonrectangular variable-mask union cannot carry a rank-one matrix regardless of coefficient signs or complex parameter values.

The graph interpretation proves the same exclusions without evaluating matrix minors: a rectangle with at least two rows and columns contains a4-cycle; neither a12-cycle nor a6-cycle plus isolated edges contains one. Every two-edge owner occupies two different rows AND columns. Hence any mask containing such an owner cannot be a one-row or one-column rectangle either. In a9-entry graph, a union of two or three isolated-edge singleton owners spans distinct components and cannot be a rectangle; exactly each single isolated edge is one. The mask test also explicitly verifies this conclusion and all boundaries.

For every 12-entry pencil, the rank-at-most-one set L contains only0, so W=0. For every 9-entry pencil, all nonzero rank-one vectors have their variable supports among the three singleton masks, and hence L is contained in the coordinate span of those three variables, W of dimension3. A linear combination of these three variables need not itself have rank1; containment, not equality, is all the pencil lemma needs.

## 6. Same local maps and the exact sixty bound

Fix an arbitrary spectator and its level t. That level defines one 6×6×6 tensor for the three active parties. **The same** three arbitrary invertible maps used on the full tensor act on this slice. Every local pencil bound from §§4–5 is universal in those maps, so it can be applied separately to every spectator level without choosing six different maps.

At every 12-entry original level, w=0 and d=6 give support>=12. At every 9-entry original level, w=3 and d=6 give support>=9. The six levels are distinct spectator-index slices and their output supports are disjoint; hence the transformed full support is at least

`9+12+12+9+9+9=60`.

This argument holds for each of the four spectators; the stronger simultaneous 72-pencil verification is not needed to assume extra freedom. The identity matrices leave the original exactly60 nonzero coefficients, so the bound is attained. Multiplying the fixed spectator by a monomial map permutes/rescales its six slices without changing their support cardinalities. The conclusion for any product unitary with at least one monomial factor follows; contraposition gives the candidate's necessary four-nonmonomial condition for a sub-60 product-unitary image of THIS tensor only.

No result for an arbitrary four-nonmonomial transformation is inferred, and an invertible but nonunitary basis change is used solely as a stronger mathematical quantifier for this fixed tensor, not as a physical product-basis assumption.

## 7. Review findings and remaining gates

No substantive defect found in the rank lemma, all-variable cell/mask reasoning, graph characterization, unchanged-map quantifier, six-slice sum or stated restricted-orbit conclusion. Independent exact checks additionally verified all six AME marginals for the same tensor and matched the source table, without relying on the author's correlated checker engine.

The reported primary source's 38 lower bound involves separate literature/partial-Latin-square inputs and was **not** reconstructed here; it is irrelevant to this 60 restricted-orbit conclusion. The primary paper's broader classification, any worldwide most-recent state, universal AME lower bound and novelty/priority are not authenticated by this review. The finite certificate, a manually transcribed primary table and same-harness programs are not a formal proof or independent-model/human review.

Original all-state/all-basis AME minimum, a sub-60 witness, and the effect of four nonmonomial local factors remain open at this review scope. Main must read the complete candidate, this return, operative table and exact-check evidence before any adoption. No author contact, publication, external model, nested task, deletion or infrastructure change occurred.
