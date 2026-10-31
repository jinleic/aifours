# f58 — independent review of the seven-sector and one-unrestricted-party barriers

Reviewer **MathSemigroup-2**, math-4; author **PhysicsAME46-2**, physics-6. Assignment SHA `40a629a21f0189ece24e5c2d8d6a104af59eb2fd98b358e3ced23c280fd30d39`. Native prewrite observation: **Wed Oct 28 17:51:10 PDT 2026**.

## 1. Verdict and exact scope

| Candidate | FATAL | MAJOR | MINOR | Exact disposition |
|---|---:|---:|---:|---|
| `frontier-20261028-u2u4-sector-orbit-barrier-v1.md`,68LF, SHA `8bf0f06dea859552924fa3be3340f70966d6b56b4c162335193bc7cf168b44f0` | 0 | 0 | 0 | **NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE**: for the specific published tensor, arbitrary GL(2)⊕GL(4) on all four parties leaves at least60 coefficients. |
| `frontier-20261028-one-unrestricted-party-sector-barrier-v1.md`,54LF, SHA `32d8636585bd0a114a8f5578afc217cc6988bb714fefc4fcb22fe924c973596b` | 0 | 0 | 0 | **NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE**: the same lower bound holds with ANY one factor in GL(6) and the other three in GL(2)⊕GL(4). |

In both cases the identity attains exactly60. For physical local unitaries, a sub-60 image of THIS tensor must have at least two parties whose image of H is not a coordinate 2-plane. These claims are about one published tensor and specified restricted local transformations, not arbitrary U(6)^4, all AME states, a global minimum, or a new witness. GL statements are stronger support-algebra assertions; nonunitary outputs are not labeled AME.

The candidate-reported nontrivial 256-support physical control was not rerun in this review and is not a premise of either universal rank proof. The prior three-party/nonmonomial and all-pairs results are separate earlier reviewed results, not necessary assumptions for the present proof. No formal/kernel/human/independent-model or novelty acceptance follows.

## 2. Inputs, exact independent verification and familiarity

Read in the assignment's order: entire38LF source table SHA `cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38`, entire68LF all-sector candidate, entire54LF one-unrestricted candidate. Native hashes matched. The source is [Pandya arXiv:2610.16673v1, Table 1](https://arxiv.org/html/2610.16673v1#S2.T1). My previous f21 review `frontier-review-f21-ame-three-party-support-v1.md`, SHA `33597eeaf6c291955cf8a07a1c28871cf666227fa7651f7d0693664140a6cfd7`, compared an independently typed36-cell primary-table transcription to this pinned file and exactly recomputed all six original marginals. The full registered AME-definition packet was also read in that review. Those direct checks concern the SAME tensor, not arbitrary AME states.

For this assignment I independently wrote `frontier-review-f58-independent-sector-ranks-v1.py`, SHA `ff085ef2b64d4a25fc7497a08f9d0fda577399c0a6273bdbcd9bddc2f792fc84`. It imports my own pinned strict source parser from f35, SHA `aa7105b8e868ba9a53507ba77f4fa93853423f1454634960db9ce8061fda6066`, but no author parser, code, result or rank receipt. It constructs all sectors and computes exact rational matrix ranks by independently written `Fraction` elimination; it factors out the common nonzero √2 **only from P**, while E uses its actual ±1 signs. No numeric zero tolerance is used.

Actual command, **Wed Oct 28 17:50:56 PDT 2026**, timeout30s, exit0:

```text
/opt/homebrew/bin/python3 -B mathematics/evidence/three-area-20261027-96h/parallel-18/semigroup-embedding/frontier-review-f58-independent-sector-ranks-v1.py physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261028-pandya-table-v1.txt

table_sha256=cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38
P_terms=12 E_sectors=6 E_terms_each=8 active_blocks=24
PASS all six P 2|2 flattenings rank12 and distinct row/column matchings
PASS all twelve E cross-flattenings rank8 and each 4-spectator matching/block determinant
CONTROL deletion of one E coefficient rejected: E block determinant
```

The deletion is a targeted control of the stated block-determinant failure, not an exhaustive mutation suite. This is one same-harness implementation on a shared public table, not independent-family or formal verification.

Prior same-harness familiarity includes my w20/w58/f21/f35/f52 AME reviews and QOA source-only work. It is disclosed, not blind or cognitively isolated. The current owner direction prospectively permits this source read/exact check; no historical held outcome is accepted as a premise. No author contact, external model, publication, deletion, Git push or infrastructure mutation occurred.

## 3. Independently reconstructed seven sectors

In the source basis put `H=span{|1>,|2>}` and `K=span{|0>,|3>,|4>,|5>}`. Every original coefficient has either zero or exactly two coordinates in H. Thus there are exactly seven nonempty source sectors:

- P in K⊗K⊗K⊗K, with12 coefficients, all unnormalized √2;
- E_ij for each unordered party pair {i,j}, with H exactly at i,j and K at the other two parties, eight coefficients each.

There are no source terms with one, three or four H indices. The seven supports are disjoint. Every actual GL(2)⊕GL(4) factor preserves H and K as subspaces, not just their dimensions, so their tensor products preserve each full sector. Different transformed sectors remain supported on disjoint product-coordinate index sets even when the K maps are dense. Their **same actual** local maps are used in each sector; independent sectorwise choices are not substituted.

## 4. Source flattening ranks, all signs and spectator matchings

For P and any2|2 cut, the program verifies that its12 nonzero entries lie in12 distinct flattened rows and12 distinct flattened columns. After row/column permutations they form a diagonal12×12 block with nonzero entries; rank is exactly12. There are six ordered side choices, each explicitly recomputed. Removing the global nonzero √2 factor does not change that rank.

For each E_ij, let {k,l} be the two K parties. The four source spectator index pairs form a perfect matching: all four allowed K values appear once in the k-coordinate and once in the l-coordinate. Each corresponding H_i×H_j matrix has exactly two nonzero ±1 entries and nonzero determinant. Thus across the cross cut `(i,k)|(j,l)`, permutations of the four spectator labels turn the flattening into the direct sum of four nonsingular2×2 blocks, so its rank is8. The independent program checks **both** cross choices for each of the six active pairs, all24 small determinants and the full 36×36 rational flattening ranks. It does not infer these ranks from the AME marginals alone.

Deleting one actual E coefficient destroys its 2×2 determinant and is caught at the intended predicate. The finite source facts are completely separate from the universal transformation argument below.

## 5. All four factors preserve H/K

For any of the seven source tensors and any selected2|2 cut, a product of four local GL(2)⊕GL(4) maps acts on its flattening by invertible Kronecker factors on the two sides, with a transpose on the right under the coefficient convention. Restriction to the relevant input/output H or K subspace is invertible by hypothesis. Therefore the P rank remains12 and each E_ij cross rank remains8.

Flattening only reindexes sector coefficients, and any matrix of rank r has at least r nonzero entries. Consequently the transformed P sector has at least12 coefficients and each transformed E sector has at least8. Since §3's sector supports stay disjoint, the full output has at least12+6·8=60 nonzero coefficients. Identity attains60, so this sector-orbit minimum is exact. No assumption that a dense K block preserves the original sparse 2×2 subblocks is used: only the full cross-flattening rank is preserved.

## 6. One party arbitrary GL(6): the correct disjoint grouping

Let a be any one unrestricted party. Partition **only the other three** parties by H/K occupancy; their block-diagonal maps preserve each pattern. The actual source has exactly the following seven nonempty patterns among those three parties:

1. Zero H positions: P, and no E sector.
2. Exactly one H position, say i: the unique E_ai sector.
3. Exactly two H positions i,j: the unique E_ij sector.
4. Three H positions: no source terms.

There are 1+3+3=7 distinct nonempty patterns. `V_a∈GL(6)` may mix H and K on the unrestricted party, but cannot mix the H/K coordinate patterns on the other three. Thus these seven output supports remain disjoint; this is not a claim that the unrestricted party itself preserves its old sectors.

Regard each sector in the **full** four-party space, with zeros outside its original H/K subspaces. On any2|2 flattening, applying the SAME V_a and the other three invertible factors multiplies the source matrix by invertible full-dimensional Kronecker factors. Embedding the original subspace in C^6 does not alter its original matrix rank. Thus P still has rank12 and every E_ij its own verified rank8, even when V_a mixes its H and K coordinates.

Each of the seven disjoint output patterns therefore has support at least its source rank. Summing gives60. This applies to every choice of unrestricted a and every complex GL(6) map; identity again attains the bound. No conclusion about two unrestricted parties follows: with only two other H/K patterns preserved, distinct original sectors can merge.

## 7. Physical coordinate-plane consequence and limits

Suppose a **unitary** U maps the fixed H onto a coordinate 2-plane. An output permutation of basis coordinates maps that image plane back to H and preserves support. Since U is unitary, it maps the orthogonal complement K onto the orthogonal complement of U(H), so after the same permutation the map is GL(2)⊕GL(4), in fact U(2)⊕U(4). This orthogonal-complement step depends on unitarity; it is not inferred from the plane condition for a general GL(6) map.

If at least three of four physical parties have coordinate-plane images, use an output permutation independently at those parties; the remaining party is arbitrary. Section6 then forbids support<60. Consequently any sub-60 product-unitary image of THIS tensor must have **at least two** non-coordinate images of H. This is a necessary condition, not a construction or a claim that two suffice. The weaker all-four-block-diagonal result gives the corresponding at-least-one condition.

No FATAL/MAJOR/MINOR defect was found in the source sector facts, rank counts, same-map/disjoint-support arguments, unrestricted-party grouping or physical coordinate-plane implication. The published 38 lower-bound import and its current worldwide status were not reconstructed here. Other AME tensors, arbitrary four-party GL/U(6) transformations and the original all-state/global-basis support minimum remain outside the conclusion.

This is same-harness written/computational review, not Main adoption, independent-model/human/formal/kernel or novelty clearance. Main must read both complete candidates and this actual return before disposition.
