# Every chiral pair is already inside f274's optimized certificate region

**WRITTEN, UNREVIEWED additive qualification** of `frontier-20261029-d4-t2-traceless-dual-strict-chiral-consolidated-v2.md` (SHA-256 b96fcf9f42e0762132d7b843149f424fcde28bd978439b144f3196e09e34efb5). This strengthens and supersedes the limited irreducible-example overlap diagnostic; neither previous file is changed. It uses the consolidated packet's UNREVIEWED chiral operator-norm theorem and the parent-adopted f274 relation `η≤2γ`.

## Claim

For **every** original traceless 4×4 pair with local Hermitian unitary involutions satisfying `Z_A A Z_A=−A`, `Z_B B Z_B=−B`, the f274 entrywise-factor and compound certificates satisfy

`γ(A,B)≤L`, and therefore **`η(A,B)≤2L`**.  (1)

Thus the complete chiral class, including all both-squares-nonnormal and unitarily irreducible members, is contained in f274's optimized sufficient region, conditional on review of the chiral norm proof. The independent chiral argument supplies an alternate physical proof and strictness result; it does **not** enlarge the certified set beyond f274. No claim about nonchiral pairs follows.

## Proof

Choose local bases in which the involutions are diagonal with `+1` and `−1` entries. The anticommutation equations make both local matrices off-diagonal with respect to those eigenspace decompositions. In particular `A_ii=B_jj=0` for every diagonal position. Define the entrywise nonnegative matrices `Ã=|A|`, `B̃=|B|`. They anticommute with the **same** respective diagonal involutions, are traceless, and have unchanged Frobenius norms.

For any tensor-product matrix entry,

`X_(i,j),(k,l)=A_ik δ_jl+δ_ik B_jl`.

The two summands can overlap only when `i=k` and `j=l`, where both are zero. Therefore there is no entrywise cancellation, and exactly

`|X| = Ã⊗I4+I4⊗B̃`.  (2)

The right-hand side is itself a chiral tensor sum. Apply the consolidated chiral norm theorem to `Ã,B̃`:

`|| |X| ||_op² ≤ ||Ã||_F²+||B̃||_F² = L`.

The displayed local bases are among those minimized over in f274, so `γ≤ρ(|X|ᵀ|X|)=|||X|||_op²≤L`. The adopted f274 domination `η≤2γ` proves (1). The argument handles zero blocks, unequal involution multiplicities and all complex phases of the original pair.

## Limits

The independent physical proof, its exact strictness for original nonnormal squares, and the symbolic irreducible examples remain mathematically distinct written statements. Their prior conservative f274-membership language is superseded by this later full-class inclusion. This note does not establish strict `η<2L` for all chiral pairs, any f274-complement example, unrestricted T2/T3/Z2/q3, a physical counterexample, numerical/physical-q sample, execution, source correctness, stronger-family/human review or novelty. Review scopes already frozen remain unchanged; this qualification requires prospective admission if included in a later review.
