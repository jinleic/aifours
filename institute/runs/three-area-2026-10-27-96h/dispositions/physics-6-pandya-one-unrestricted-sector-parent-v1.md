# Pandya AME tensor: support floor with one unrestricted factor

Native clock observed before writing: **2026-10-28T18:01:30-0700 PDT**. This result concerns one specified published tensor and a restricted local orbit. It does not determine the global minimum support of AME(4,6), classify all local transformations, or claim novelty, human/cross-model review or a formal proof.

## Exact statement

Let T be the specific 60-term real tensor in [Pandya, arXiv:2610.16673v1, Table 1](https://arxiv.org/html/2610.16673v1#S2.T1). On each party define `H=span{|1>,|2>}` and `K=span{|0>,|3>,|4>,|5>}`. Pick **any one** party and apply an arbitrary `GL(6,C)` transformation there; on each of the other three parties apply an arbitrary invertible `GL(H)⊕GL(K)` transformation. The resulting tensor has at least **60** nonzero coefficients. The identity transformation attains 60, so the restricted-orbit minimum is exactly 60. Nonunitary transforms are only algebraic support statements; they need not preserve AME.

For physical local unitaries, if at least three parties map H to coordinate 2-planes, support-preserving output permutations carry those planes back to H. Unitarity then makes those three local maps block diagonal, and the theorem applies to the fourth. Therefore **any sub-60 unitary image of this tensor** must send H to a non-coordinate 2-plane on at least two parties. The condition is necessary, not sufficient.

## Seven-sector proof

The published table has one sector P with all four indices in K, consisting of 12 `√2` coefficients, and six sectors `E_ij` with exactly parties i,j in H, eight `±1` coefficients per sector. No other H/K sectors occur.

For every 2|2 cut of P, the 12 nonzero entries occupy distinct flattening rows and columns, so its rank is 12. For each `E_ij`, choose a cross cut placing one active H factor and one spectator K factor on each side. The four spectator coordinate pairs form a matching, and each corresponding 2×2 active block has nonzero determinant. Its flattening has rank 8. Invertible local maps act on any flattening by invertible Kronecker factors, including the unrestricted full `GL(6)` factor, and therefore preserve these ranks. Any rank-r matrix has at least r nonzero entries.

Partition the **other three** parties by their H/K output-coordinate pattern. They remain block preserving. Among those three parties, P has zero H positions; the three sectors involving the unrestricted party have one H position each; and the other three E sectors have two H positions each. These seven patterns are distinct, so their output supports cannot cancel one another even though the unrestricted factor may mix H and K. The sectorwise rank bounds sum to `12+6·8=60`. This uses the same four actual local transformations throughout, not separately optimized sector choices.

## Source and verification

The parent read the complete [transcribed Table 1](/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261028-pandya-table-v1.txt), the complete [four-block manuscript](/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261028-u2u4-sector-orbit-barrier-v1.md), the complete [one-free-party manuscript](/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261028-one-unrestricted-party-sector-barrier-v1.md), and the full [f58 review](/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/semigroup-embedding/frontier-review-f58-ame-sector-one-unrestricted-v1.md), which found 0 fatal/major/minor defects at this scope. The parent also read the 36-cell published table. Prior f21 independently transcribed that table and checked all six two-party marginals; the current finite checks share the pinned table input and are not a new human source transcription.

A separately written [parent sector checker](../review-waves/f58-ame-sector-one-unrestricted/parent-sector-structure-check-v1.py), SHA-256 `73369a614870479648b961e516e1d76a731b03c96671dcd0a17931693c15a7b5`, actually parsed all 36 cells, identified exactly 60 coefficients and seven sectors, verified all six P bipartition matchings, all 24 nonzero E-block determinants and the seven distinct output patterns for each of four free-party choices. It rejected an in-memory E-coefficient deletion at the intended sector-count check. The [exact receipt](../review-waves/f58-ame-sector-one-unrestricted/parent-sector-structure-result-v1.json), SHA-256 `3e8381d7b2e411b432c6e1f25dd924f462a4ea45966e8ef34348e5eb4ba22843`, binds the table hash. The reviewer separately rebuilt and checked all six P and twelve E cross-flattening ranks and spectator matchings using exact rational arithmetic; its code and limits are in f58.

## Limits and distinct later candidate

The proof does not apply when two or more parties are unrestricted, to other AME tensors, or to arbitrary product-unitary images. A later proposed three-unrestricted-party support-60 argument reported a mixed-sector rank cancellation gap and was explicitly withdrawn as a proof by its author; a subsequent repair proposal remains unreviewed. Neither later claim is a premise here. The published tensor and all-state minimum remain separate: no sub-60 witness or improved global lower bound follows from this disposition.
