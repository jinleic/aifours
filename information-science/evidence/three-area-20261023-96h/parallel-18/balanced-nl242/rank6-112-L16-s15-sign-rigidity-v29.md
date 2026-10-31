# Balanced NL242 (3,112), L=16, s=15: sign rigidity on the two 3-spaces

Owner: InfoBalancedNL242-2, info-6; continuation handle InfoBalancedNL242-2-2. Native `/bin/date` observed before this write: 2026-10-27T10:38:24-0700 PDT.

**WRITTEN AUTHOR CANDIDATE, NOT REVIEWED OR ADOPTED.** This strengthens the sign analysis behind v21, conditional on the unreviewed support classification v20 and Lemma H. It is a same-author alternative, not independent review. It concerns only this L16 case and makes no whole-type, witness, unrestricted-exclusion, formal/kernel or novelty claim.

## Claim

Write Σ=F∪G as in v20 and normalize g(0)=+1. On each of F,G the sign function is either

    g(x)=χ_λ(x), or   g(x)=−χ_λ(x)+2·1_{x=0},                    (1)

for some character χ_λ. Thus the only possible N₀ values from the two restrictions are 1, 7 or 49, in particular N₀<52.

## Proof

For any nonzero linear character on F extended trivially over G, the negative side of its hyperplane cuts Σ in exactly four points of F, an affine 2-plane not containing 0. By Lemma H every such side has sign product +1. Let M⊂F\{0} be the negative points of g. For every λ∈F* these positive-plane conditions say

    λ·Σ_{x∈M}x=0;

hence ΣM=0. The seven nonzero points of F also sum to zero. Neither one nor two distinct nonzero points can sum to zero, so M or its complement cannot have size 1 or 2. A three-point zero-sum set has the form {a,b,a+b}; its complement is a four-point affine plane not containing 0. It follows that M is empty, all seven points, such a triple, or its complement.

The empty and four-point cases give the first form in (1). The all-seven and three-point cases give the second: in the three-point case choose the nonzero λ annihilating span{a,b}. The identical reasoning holds on G. This is an implication from all hyperplane conditions, not a claim about other slices.

For the first form, the eight 3-space Walsh values are one +8 and seven 0, so the mod-3 multiplicities are (7,0,1). For the second, they are one −6 and seven +2, giving (1,0,7). Since the restrictions agree at 0 and Ψ=A+B−1, their residue convolution yields N₀=1 for two first forms, 7 for one of each, and 49 for two second forms. All contradict the L16 requirement N₀≥52. ∎

## Dependencies and exact scope

Uses `rank6-112-L16-s15-support-classification-v20.md` SHA-256 `0d3b51c59eec62cbb260478f088a7d7976b0fc6a90ff8d32df80a253377e2ba5`, 43 LF, and Lemma H/budget in `rank6-112-L16-reduction-v6.md` SHA-256 `450cd2ac6328e5c1c1b2a4eaad4a9d7144ac21be4582b67894ac7a35431b283d`. It independently narrows the **author-only** sign cases but does not constitute independent review of v20 or v21. The conditional L≥18 candidate, original witness-or-unrestricted-exclusion gap, (24,24,2), all earlier findings and pre-pin corrections, v263 early-stop disclosure, HOLD, N4 UNKNOWN, aux214 STOP and all HELD/ZERO/NONINPUT remain as previously stated.
