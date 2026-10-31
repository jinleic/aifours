# Every four-party one-two-level-per-party local move preserves the 60 support floor

Owner **PhysicsAME46-2**. Native observation immediately before writing: **`Wed Oct 28 17:42:32 PDT 2026`**; not an exact file-write/completion/runtime clock. **WRITTEN proof with two independently structured exact finite checks; author candidate, not peer-reviewed, formal/kernel verified or novelty-cleared.**

## 1. Claim and original-target scope

Let `T` be the SPECIFIC published 60-term real AME(4,6) tensor of [Pandya, arXiv:2610.16673v1, Table 1](https://arxiv.org/html/2610.16673#S2.T1), transcribed as `frontier-20261028-pandya-table-v1.txt` SHA256 `cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38`. Its normalization and all SIX actual two-party marginals have been checked exactly by two reviewer-written implementations, as pinned in `frontier-20261028-two-party-orbit-obstruction-v1.md`, SHA256 `94f85389567b2a3ea8e8f1a418af58977f4fdc3670f4a696fa6512703b7a9f75`.

For EACH party i choose ANY pair of its six basis levels and let `V_i` act by ANY invertible complex 2×2 matrix on that pair and by ANY invertible monomial matrix on the other four levels. Then

`support((V_1⊗V_2⊗V_3⊗V_4) T) ≥ 60`.                                         (1)

There are `15^4=50625` pair choices, ALL covered. Identity attains60. In particular, every arbitrary two-level U(2) move on each of four parties, with monomial complement, is an actual physical product-basis change and cannot lower this witness's support. Arbitrary local monomial transformations before/after the two-level move also cannot help: output monomials preserve support, and input monomials can be commuted through by relabelling the selected pair and conjugating its arbitrary 2×2 block.

This is an exact continuous-parameter obstruction, **not** an angle/phase grid search. It is specific to ONE known AME state and its indicated subset of local maps. It does NOT settle general U(6)^4 orbit minimization, other AME states, the global minimum, or a strictly improved universal lower bound. A support-reducing arbitrary four-party transformation would have to leave this one-two-level-per-party class.

## 2. Invariant-block rank principle

For a fixed choice of pairs P_i, split each local space as the selected 2D coordinate subspace plus four one-dimensional unselected coordinate subspaces. Their tensor products form a direct coordinate-block decomposition. After removing harmless output monomial permutations/phases, every V_i preserves each summand and acts invertibly within its selected 2D summand. Distinct blocks remain disjoint in the final coefficient array.

For any block B let `r(B)` be its complex tensor/CP rank. Invertible local maps preserve r(B), and ANY expression in a product basis with s nonzero coefficients is a sum of s elementary product tensors, so `s≥r(B)`. The source block itself has t(B) nonzero terms, hence `r(B)≤t(B)`. Therefore, if we certify `r(B)≥t(B)` for EVERY nonempty block of a pair choice, its final support is at least

`sum_B r(B) = sum_B t(B) = 60`.

No independent choice of local transformations for different blocks is required: each lower bound applies to the SAME actual four-party transformation. In fact, the proof would remain valid even if different blocks used different invertible product maps, so the shared-map condition cannot weaken the inequality.

The exact checker found that **every block for every pair choice is rank-saturated**. The finite facts, including their precise certificate types, are in §5.

## 3. The load-bearing three-term binary tensor lemma

Let a nonzero 2×2×2 complex tensor have exactly THREE nonzero product-basis coefficients and no two occupied tuples at Hamming distance one. Then its complex tensor rank is EXACTLY3.

**Proof.** Three nonadjacent vertices of the binary 3-cube must all have the same parity: if two had opposite parity they would have distance3 (distance1 is forbidden), but every third cube vertex is distance1 from one of two antipodal vertices. Translate bits and permute axes to put the support at `000,011,101`, with nonzero coefficients a,b,c. It has rank at most3 from its source terms.

Slice on the first axis:

`M_0=[[a,0],[0,b]]`, `M_1=[[0,c],[0,0]]`,

so `det(x M_0+y M_1)=ab x²`. All three one-axis flattenings have rank2: both coordinate values occur and, by the no-Hamming-one property, their supports are disjoint.

If the tensor were a sum of TWO product tensors, rank2 of all three one-axis flattenings would force the two factors in EACH mode to be linearly independent. The pencil would then be `V diag(ℓ_1(x,y),ℓ_2(x,y)) W^T`, with V,W invertible and ℓ_1,ℓ_2 independent linear forms. Its determinant would be a nonzero scalar times a product of TWO DISTINCT linear factors. That contradicts the single repeated factor `ab x²` over C. Hence rank≥3, proving the lemma. ∎

A fourth 2D active leg which is CONSTANT on all three support terms is an extra product factor. Removing it leaves the same 2×2×2 W tensor; tensor rank is unchanged because a nonzero linear functional on that factor recovers the original three-way tensor. Thus the lemma applies in both the three-active case and the four-active/one-constant-leg case.

For two source terms, the independently checked no-Hamming-one property makes their Hamming distance at least2. A flattening separating two differing coordinates has the two terms in distinct rows and columns, so its rank is2. One term has rank1. These elementary cases need no special phase choice.

## 4. Modular flattening certificates are valid over C

The table's unnormalized coefficients lie in `Z[sqrt(2)]`. The homomorphism to `F_17` defined by `sqrt(2)↦6` is valid because `6²≡2 (mod17)`. A matrix minor nonzero after this reduction cannot have been zero in `Z[sqrt(2)]`, hence is nonzero in C. Thus modular flattening rank is a valid LOWER bound on complex flattening rank and hence on complex tensor rank.

For each four-active block not covered by the three-term W lemma, the exact algorithms form the three 2|2 flattenings and use the maximum modular rank. They do not infer equality from modular rank alone: equality follows when the modular lower bound equals the separately counted source support t(B), which is also an explicit t(B)-term decomposition upper bound. No floating-point zero tolerance or local-angle sampling appears in this argument.

## 5. Complete census and independent replay

The initial pair-fibre verifier found no Hamming-one pair in T's support. Then the first census split each of all50625 coordinate-pair choices into its nonempty invariant blocks and applied the rank rules above:

- `frontier-20261028-four-party-block-rank-bound-v2.py` SHA256 `aef05833e123958e7a9e23a9b4a3c28cb8f5c4e9a4fe2691d07225ff6a84e5ca` handled ordinary flattenings and three-active W blocks. Its receipt SHA256 `5245fe402dfb8d5b4b11e8554354ff5313b493b2572372ff5899ec0205148d28` had **50465** pair choices at lower bound60 and **160** at59; the latter were NOT silently promoted.
- `frontier-20261028-four-party-block-rank-bound-v3.py` SHA256 `8d6fc0cf70488c8847ce8d569c2b305f2033eff768d0ef31ce9fe3a96ced2dfe` checked that each remaining case contains a four-active three-term block with one constant leg, paid by §3's W lemma. Receipt `frontier-20261028-four-party-block-rank-bound-v3.json`, SHA256 `31228451bdb8c161d83b37526f258ecd7331395f8954ebd471a060fd05ddc4aa`, reports **160** such refinements, histogram `{60:50625}`, and no exception below60.
- A separately written parser and block classifier, `frontier-20261028-four-party-block-independent-v1.py`, SHA256 `315f9acc423dd7be553f9bee977789e06785f4ab1d44de9d24e43a627df069e2`, independently recomputed ALL blocks rather than trusting the first receipt. Its `frontier-20261028-four-party-block-independent-v1.json` receipt SHA256 `dcac1171b8ff08003978af1c0470e61e5787d2ddf3c7915baee9daba0d57a230` reports **50625 choices**, **2,993,046 nonempty blocks**, and every block's lower certificate equal to its actual term count. An added Hamming-one support mutation was rejected for the intended collision reason.

The independent complete block-type counts are:

| Active 2D legs | Source terms per block | Lower certificate | Block occurrences across all pair choices |
| ---: | ---: | --- | ---: |
| 0 | 1 | singleton | 600000 |
| 1 | 1 | singleton | 1200000 |
| 2 | 1 / 2 | singleton / separated two-term | 871200 / 14400 |
| 3 | 1 / 2 / 3 | singleton / separated / W lemma | 255840 / 21600 / 320 |
| 4 | 1 / 2 | singleton / separated | 22488 / 6642 |
| 4 | 3 | W with constant leg / nonzero modular minor | 160 / 336 |
| 4 | 4 | nonzero modular flattening determinant | 60 |

The independent checker used a distinct source parser and generic block-case logic; the two searches still operate in the SAME model/harness, and their common W lemma is a written input, not two independent proofs. An independent human/formal or disjoint scientific review and source-priority audit remain outstanding.

## 6. Scientific significance and remaining gap

This replaces the earlier `810000`-gate equal-angle/fourth-root-phase negative search by a proof covering **all continuous complex 2×2 invertible choices** on every selected pair of all four parties simultaneously. It also extends the prior special common-sector result to **all 50625 pair selections**. The three-party theorem remains valid independently.

The result is still an orbit obstruction, not a new AME minimum. Product unitaries involving multiple noncommuting two-level rotations on one or more parties, more general 3×3/4×4/6×6 mixing, and different AME states are not covered. The public source's support60 is prior; its reported38 lower bound/imports were not independently proved here. No actual sub-60 state was found and no global lower-bound/novelty claim is made.
