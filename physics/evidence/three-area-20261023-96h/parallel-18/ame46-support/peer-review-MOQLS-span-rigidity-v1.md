# Peer reconstruction — MOQLS low projector-span rigidity v1

Reviewer: PhysicsAME46, physics-6. Clock actually observed before writing: `2026-10-23T14:34:56-0700`. One bounded parent-assigned cross-review, not a change of primary problem. No author/shared files changed. No scientific executable, solver, enumeration, compilation, numerical assay, CLI or nested agent was used.

## Exact pinned inputs and read scope

Paths below are in sibling `../moqls8/` and were read-only.

| Input | SHA256 observed with shasum | Read scope |
|---|---|---|
| `proof-low-span-rigidity-v1.md` | `d64f57609450e2c6afbff5ddf3a6d768b1bb9c23d3159a8bf7a19604475380a6` | Complete manuscript, LF1–185 |
| `proof-isolated-sector-exclusion-v1.md` | `34e5eca0a0d7ebac81b67c39cde758591513c79bf848d3bf9263c27126d1855d` | Complete dependency, LF1–202 |
| `selection-v1.md` | `aae6f0bfeff42e6277d277199c0875c0c7368b8c8153560e2ff1cea4bc10f782` | Complete definition/target boundary, LF1–47 |
| `proof-global-gram-defect-v1.md` | `3b54a3e46ceb9ffa9edccab28664e13e322f5b47707fdffb77a51beba9a608d8` | Only the a_s definition and budget interface, LF69–124, as a conditional premise; not a new full review |
| `proof-global-gram-defect-v1-erratum-1.md` | `ef32720fe1b7c64a8539d6ae8cf5d94a0605e10a002aeb8483a5a2ac8eeb5d59` | Complete operative wording qualification, LF1–13 |

The two parent-specified proof hashes match. An initial metadata command used an incorrect guessed dependency basename and reported a missing file; the directory and source reference supplied the actual `proof-isolated-sector-exclusion-v1.md`, whose hash then matched. No differently hashed source was substituted.

## Verdict at the exact reviewed scope

**0 FATAL / 0 MAJOR / 0 MINOR findings. No substantive defect found in the written low-span theorem or the sector/rank14 dependency.** This is an actual supplied-proof, ordinary in-harness reconstruction, not blind, cross-vendor, human or formal/kernel verification. The global covariance budget remains an explicit separately proved input to the K5/B3 compositions; this review checks its mathematical interface, not its complete derivation or historical review acceptance.

The reviewed core claim is: for actual t≥2 MOQLS(n), if n<2(t+1), every nonclassical square has real projector-span dimension at least n+3. The conditional K5 exclusion at n8/t5 follows if the separately stated surplus budget≤14 is accepted. Neither this verdict nor the manuscripts prove the unrestricted five-square order8 family classical.

## Independent mathematical reconstruction

### A. Two-matchings and isolated two-space

Low-span LF27–41 and sector LF23–65 are sound. For fixed x in one matching, its row and column meet the other matching at two different cells. Both inner products vanish in every other square. Completeness of the second matching's ONB in the SAME m-space makes every transition support nonempty. Physical product orthogonality makes those t−1 supports disjoint, giving t−1≤m−2 and m≥t+1.

For an isolated complex two-space, a shared ray determines its entire orthogonal ray-pair; different pairs have all four cross overlaps nonzero. Each pair class is a two-regular board on equally many rows/columns with two ray matchings. Its repeated rays force m_a-dimensional spans in each other square; cross-class orthogonality and Σm_a=n saturate all dimensions. This verifies the same-space hypothesis required by the two-matchings lemma rather than assuming it for projections. Two distinct ray-pair classes consequently require n≥2(t+1).

### B. One-channel lemma, including overlapping coordinate edges

Low-span LF49–79 correctly handles arbitrary complex amplitudes and unrestricted mixing inside B-perp. Each mixed ONB line must contain at least two mixed projectors to cancel its nonzero B/B-perp block. At most two orthogonal vectors can lie in the channel F, so there are exactly two and their remaining B-pure vector is b-perp.

For an alpha pair different from beta, neither of its rays can occur in a mixed row/column. Its occurrences are matchings on the same row/column sets. The beta repeated b-perp ray forces dimension m_beta+k, while alpha requires m_alpha. These lower bounds sum to n and their spaces are mutually orthogonal, giving exact saturation. Every mixed entry in another square is orthogonal to all alpha spaces and to the m_beta pure-b vectors, hence lies in the stated k-space W_s. Applying the matching argument after a second saturation on F-ray classes gives k≥t+1. Together with some m_alpha≥t+1 this proves the claimed contradiction. No projected-part orthogonality or missing complement-purity premise is used.

### C. Line-frame cost and weight2 cases

Low-span LF81–135 uses the real Hermitian span correctly. Because the complete reference diagonal algebra D lies in S, off-diagonal projection has kernel D and dimension a_1−n. For any actual ONB transition, its two diagonal algebras intersect in one real scalar per bipartite support component. The quotient cost is therefore Σ(r_component−1). A weight3 cell under surplus≤2 forces one square size3 component and exhausts the global two-dimensional off-diagonal span.

Surplus1 confines every noncoordinate rank-one projector to the same coordinate edge and yields the forbidden isolated two-space. At surplus2, a weight2 cell plus a weight3 cell confines the off-block direction across B/e_d to one channel: rank-one outer-product proportionality makes every mixed B-component parallel to the same u, even for complex phases. Reference rays or the original weight2 vector supply a pure-B ray outside beta. With no weight3 cell, distinct coordinate edges have disjoint matrix supports and consume independent real dimensions; at most two occur. One edge, two disjoint edges, and two overlapping edges are all treated, with the last genuinely requiring the one-channel lemma. Two independent complex phase directions on one edge are not accidentally omitted.

### D. Three-space / distinct-class actual row sets

Low-span LF137–149 is complete. In the no-weight2-in-ANY-line-frame branch, a three-space is globally isolated. Its transition between any two actual line ONBs has no column of weight2. A non-full column must be singleton; deleting its isolated row/column leaves a2×2 unitary, which is monomial unless it has forbidden weight2 columns. Thus every3×3 transition is monomial or fully nonzero.

At an actual row/column intersection in this three-space the common cell ray rules out the full transition, so their unordered three-ray bases coincide. This proves that each basis class has the SAME m_a actual rows and columns, not merely abstract matchings. It has m_a occurrences of each ray. Distinct classes have all cross overlaps nonzero, forcing orthogonal spans in each other square; Σm_a=n again saturates them. Two of the three ray matchings give m_a≥t+1. A single class would make the square classical, so two classes supply the final contradiction.

### E. Sector/rank14 dependency

Sector LF88–127 gives axis-span dimension12 from the four transition components1,3,2,2. Dimension12 forces every rank-one projector block-pure, contradicting the two different B/C ray-pairs and the isolated-sector theorem. At dimension13, the off-block image has dimension1. If its active support touched three blocks, the identities c_X conjugate(c_Y)=lambda force all normalized mixed projectors to have the same positive off-block contribution; an ONB row could not cancel it. The active set must therefore consist of two fixed blocks, and the required B and C mixing identifies them as B,C.

Sector LF129–174 is the same valid one-channel saturation as part B above, with the actual B3 axes ensuring at least one alpha class. It gives k≥6 and m_alpha≥6, impossible in8 rows. Hence a_1≥14 at the literal B3-support hypothesis; no source-normalization completeness beyond B3 was assumed.

### F. Covariance budget interface and conditional arithmetic

The global proof's LF77 defines exactly the same a_s as the real span of ALL cell projectors. Its LF122 supplies Σ(a_s−8)≤14 for actual five-square order8 families. The low-span theorem gives a_s−8≥3 for every nonclassical square since8<2(5+1). Five nonclassical squares would require5·3=15>14. This checks the conditional global K5 exclusion with no change of dimension convention.

Under B3 rank14 and at least four nonclassical squares, the minimum surplus is(14−8)+3(11−8)+0=15>14. Thus the conditional B3 K4/K5 conclusion is also correct. Consuming old K1/K2/K3 results could then close physical B3 only at their original trust boundaries; those old classifications/certificates were not reviewed or replayed here. The manuscripts correctly keep Boolean GB_B3.M2 UNKNOWN and the full unrestricted K4/Problem16 frontier open.

## Handoff

The parent should treat this as a written correctness check at the stated conditional boundaries, not novelty, kernel or full-target acceptance. No author correction is requested by this reviewer. I now return to the AME(4,6) support primary; this cross-review is not an additional problem slot.
