# Parent disposition - the published 60-term AME(4,6) tensor: exact verification and local-orbit support obstructions (f7, f21)

Observed native clock before writing: **2026-10-28T17:31:53-0700 PDT**. Same-harness written support with exact finite checks; not formal/kernel, human, configured-family or novelty acceptance. Frontier-first direction: [contract addendum 2](../contract-addendum-2-frontier-first-owner-direction-v1.json).

## Complete reads by Main

| Input | SHA-256 | LF | Read |
|---|---|---|---|
| Candidate `frontier-20261028-three-party-orbit-obstruction-v1.md` (PhysicsAME46-2) | `81d66a899197064107351d703fda6fbedb7ec7842766c39d1168af27dd8fc07d` | 75 | raw 1-75 through ending |
| Candidate `frontier-20261028-two-party-orbit-obstruction-v1.md` (statement read via the f7 and f21 returns; file pinned) | `94f85389567b2a3ea8e8f1a418af58977f4fdc3670f4a696fa6512703b7a9f75` | 54 | pinned; its lemma is the two-active-party special case reconstructed in f7 and subsumed by the three-party theorem |
| Source table `frontier-20261028-pandya-table-v1.txt` | `cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38` | 38 | pinned (public Pandya arXiv:2610.16673v1 Table 1 transcription, independently compared by both reviewers) |
| Review f21 `frontier-review-f21-ame-three-party-support-v1.md` (MathSemigroup-2) | `33597eeaf6c291955cf8a07a1c28871cf666227fa7651f7d0693664140a6cfd7` | 90 | raw 1-90 through ending |
| Review f7 `frontier-review-f7-ame-two-party-support-v1.md` (PhysicsDepol4-2) | `1e8da82133ede5ddce2d3e54a9038ea365e662c3c08efef993f7bee72474b194` | 68 | raw 1-68 through ending |
| Assignments f21 / f7 | `68c2fb5ff702956a2151b96a440cc19b1b9c70dfe841d53a86d53c71a9bff304` / `232a9ce41e57d4c69130ae130238b72d847d1a6f743b5bc5bdd32bb0fab8be86` | 23 / 22 | frozen before dispatch |

## Adopted statements (exact scope)

Let T be the explicit real 60-term tensor transcribed from the public source (36 cells, coefficients ±1 and √2 over √72).

1. **Exact witness verification (same-harness, three independent implementations: author dense/sparse checkers, f7 reviewer checker, f21 reviewer checker).** T has 60 nonzero coefficients, squared-norm numerator 72, and all six two-party reductions equal I_36/36 exactly (all 7776 entries, in Z[√2]); so T is an AME(4,6) state in the computational product basis. The published table is PRIOR; this is verification, not construction.
2. **General pencil lemma.** For T = Σ_{j=1}^d e_j ⊗ M_j with linearly independent M_j, if the rank-at-most-one pencil vectors lie in a subspace of dimension w, then after arbitrary invertible maps on the three factors the support is at least 2d - w.
3. **Three-party local-orbit obstruction (specific to T).** For every choice of spectator party and every triple of invertible complex 6x6 maps on the other three parties (spectator fixed or monomial), the support is at least 60; the identity attains 60. Proof: in each of the 24 spectator-level slices the six pencil generators own disjoint cells; the 24 twelve-entry slices have 12-cycle support graphs (no rank-one pencil vector, w = 0, bound 12) and the 48 nine-entry pencils have a 6-cycle plus three isolated edges (rank-one vectors confined to three singleton coordinates, w = 3, bound 9); summing 9+12+12+9+9+9 = 60. Hence any product unitary lowering THIS tensor below 60 must be nonmonomial on all four parties. The two-active-party statement (weighted partial-permutation slices, rank = nnz) and the one-party classification (support 60 iff the unitary is monomial; least nonmonomial value 78) are the special cases reconstructed in f7.

## Parent verification

Main reconstructed the pencil lemma (basis vectors x_t after the A change; rank preserved by U(·)V^T; nnz >= rank; at most w basis vectors in W; disjoint slices), the rectangular-support necessity for rank one, the cycle-graph arguments excluding rectangles (C_12 and C_6 contain no C_4; two-edge owners meet two rows and two columns; rectangles are connected), the summation over spectator levels with the SAME local maps, and the monomial-spectator reduction. The finite support facts (72 pencils, 63 masks each, 144 rectangular singleton masks) were established by the author's two parsers and by the f21 reviewer's standalone checker (exit 0, PASS) and are read by Main as verified claims, not re-executed.

Reviewer verdicts: f21 NO_SUBSTANTIVE_DEFECT 0F/0M/0m; f7 NO_SUBSTANTIVE_DEFECT at the two-party/one-party scope.

## Not established

The original target (minimum support over all AME(4,6) states and all physical product bases) is unchanged; no sub-60 witness exists here and no bound below 60 is excluded for four-nonmonomial moves or for other AME states (an exact 78-support AME tensor in the same orbit shows the no-Hamming-one property is basis specific). The source's 38 lower bound is not reconstructed; novelty NR. Historical holds for this slot remain historical records.
