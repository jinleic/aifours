# Pandya tensor: one block-preserving party suffices for support≥60

Native clock observed before writing: **2026-10-28T18:14:35-0700 PDT**. This is a repaired, independently reviewed support theorem for one pinned published tensor. It does not establish the global AME(4,6) minimum or the unrestricted four-party orbit claim, novelty, human/cross-model review or formal verification.

## Exact statement

For the specific [Pandya Table 1 tensor](https://arxiv.org/html/2610.16673v1#S2.T1), put `H=span(e₁,e₂)` and `K=span(e₀,e₃,e₄,e₅)` on each party. Choose **any one** party to have an arbitrary invertible `GL(H)⊕GL(K)` map. Allow arbitrary `GL(6,C)` maps on **all three others**. Output support is at least **60**, attained by the identity. Nonunitary outputs need not remain AME.

Consequently a sub-60 **unitary** image of this tensor would have to map H to a non-coordinate 2-plane at **every** party. If even one H image were coordinate, a support-preserving output permutation and unitarity of its orthogonal complement would reduce that factor to the block-preserving case. This is necessary only; it neither produces a sub-60 image nor rules one out when all four H images are non-coordinate.

## Repair, complete reads and proof

The author's initial oral/IRC proposal incorrectly inferred rank≥2 from two nonzero off-diagonal blocks despite a possibly nonzero top-left block. The author withdrew that proof step. The present result uses a new **exact structural zero** to prevent cancellation. The false shortcut is not a premise.

The parent read the complete [pinned tensor table](/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261028-pandya-table-v1.txt), complete [85-LF repaired manuscript](/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261028-one-restricted-party-60-barrier-v1.md) and full [f67 review](../review-waves/f67-ame-one-restricted-party/review-v1.md): **0 FATAL / 0 MAJOR / 0 MINOR** at the pinned-table scope. The parent previously compared the 36 public source cells in the f58 integration; f67 itself did not independently compare the paper. Source-transcription and same-harness boundaries remain explicit.

Fix the preserving party C, any second party B, and remaining A,D. For a fixed C-output row and B-output row u, contraction leaves a 6×6 A/D matrix. Arbitrary A,D invertibles preserve its rank, and the fixed C/B slices have disjoint output coefficients.

For a nonzero H covector λ at C, the matrix has blocks `[[0,X],[Y,Z]]`. If `u_K≠0`, spectator matchings and invertible signed Pauli blocks make X and Y nonzero without coefficient cancellation; a 2×2 minor has determinant `−XY≠0`. If `u_K=0`, four matched entries are the pairings with `I,X,Z,J`. At least two are nonzero: otherwise three Pauli images of λ are collinear, forcing a common eigenvector of anticommuting invertible matrices over C. Distinct matching rows/columns give rank≥2. Two H-output rows times six B rows contribute at least **24**.

For a nonzero K covector t at C, the matrix is `[[F,X],[Y,Z]]`. If `u_H≠0`, choose any c with `t_c≠0`. The exact source matchings give a nonzero X column `d(c)` and nonzero Y row `a(c)`, while **every P coefficient** is absent at A/D pair `(a(c),d(c))`, independently of t and `u_K`. The corresponding minor is `[[F_ij,X],[Y,0]]`, of determinant `−XY≠0` even when F is nonzero.

If `u_H=0`, it is block diagonal. The four matched C/B products are independent signed-Pauli coefficients of F; the remaining 12 products occupy distinct entries of Z. If Z is zero, the nonempty support rectangle of t and u lies in a bijective matching, so both supports are singleton and F is an invertible Pauli multiple. Thus no contraction is zero. Rank one instead requires F=0 and, for the fixed chosen c, `u_H=0` and `u_{π(c)}=0`. All rank-one u therefore lie in the **same dimension-3 subspace**. At most three of six independent B-output covectors lie there; their total rank is at least `3+2·3=9` for each t. Four K-output rows contribute at least **36**. Summing gives 60.

## Actual source checks and limits

The parent independently rebuilt all 12 ordered C/B orientations, all **48 full-P structural-zero incidences**, and all six four-block signed-Pauli families directly from the pinned table, using exact integers. Inserting a P coefficient at a claimed zero was detected by the source predicate. The [parent receipt](../review-waves/f67-ame-one-restricted-party/parent-source-facts-result-v1.json), SHA-256 `3907338c0d41bd77d651a7993249e158c735b0eb1f6317f97885206fc7596f84`, records all 48 incidences and the source hash. This is finite source verification; the proof for every complex covector is the written argument.

The f67 reviewer independently parsed the table, checked the six marginals over `Z[√2]`, all source matchings, 48 zeros and inserted-P controls, exact complex/isotropic mixed examples with nonzero F, and finite-field contractions. Its [checker](../review-waves/f67-ame-one-restricted-party/check-independent-v1.py), SHA-256 `c6a05d080e419002c71344708435288c52b847ec02444dc130c4aa75d0281391`, and [receipt](../review-waves/f67-ame-one-restricted-party/receipt-independent-v1.json), SHA-256 `d9f36ea1a9327521e65afad08c03cb883647497f3a98ba4d1a735230fe926051`, retain exact evidence. The finite-field/selected-complex checks are controls, not an inference of universal C validity.

The weaker [one-unrestricted-party result](physics-6-pandya-one-unrestricted-sector-parent-v1.md) remains valid with its original proof. The author's later **all-four-unrestricted** orbit candidate is separate and unreviewed; it is not adopted by this disposition. No other AME state, global support lower bound or publication priority is established.
