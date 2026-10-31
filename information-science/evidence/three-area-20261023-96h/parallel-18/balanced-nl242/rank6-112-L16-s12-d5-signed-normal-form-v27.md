# Balanced NL242 (3,112), L=16, s=12, d=5: signed zero-slice normal form

Owner: InfoBalancedNL242-2, info-6; continuation handle InfoBalancedNL242-2-2. Native `/bin/date` observed before this write: 2026-10-27T10:31:22-0700 PDT.

**WRITTEN AUTHOR CANDIDATE, NOT REVIEWED OR ADOPTED.** This refines the zero-slice structure in v13–v16 and classifies the signed pair (Σ,g₀), not a full target, witness or global equivalence class. It remains conditional on those unreviewed sources and their exact admitted cuts. No scientific program, selected-state probe, independent review, formal/kernel or novelty claim.

## Claim

Up to an affine change of Π and multiplication of g₀ by an affine ±1 character on Π, the unique signed zero-slice configuration is

    Σ = B × F₂,    B={0,e₁,e₂,e₃,e₄,e₁+e₂+e₃+e₄}⊂F₂⁴,
    g₀(u,t) = −1 if u=0, and +1 otherwise.                           (1)

This does not imply that the full lifted-bent data, the other slice signs, or the original NL242 problem are equivalent under these operations.

## Proof

v15/v16 give the six canonical r-pairs, the affine-circuit support B×F₂, and a constant pair product σ∈{±1}. Thus for u∈B,

    g₀(u,t)=a(u)σ^t,    a(u)∈{±1}.

After multiplying by a character of the fibre coordinate, take σ=+1. Let κ=∏_{u∈B}a(u). For a character (λ,b) of F₂⁴×F₂,

    Ψ(λ,b) = (1+(−1)^b) Σ_{u∈B} a(u)χ_λ(u).

Since Σ_{u∈B}u=0, the six summands in the inner sum have product κ for every λ. The six labels affinely span F₂⁴ with exactly the six-point relation. Therefore, modulo simultaneous reversal, all 16 sign patterns with product κ occur exactly once.

If κ=+1, one of the 16 inner sums has magnitude 6 and the other fifteen have magnitude 2. The 32 quotient-class values Ψ then have fifteen non-3-divisible entries, contradicting v13's six. If κ=−1, six have inner magnitude 4 and ten are zero, giving precisely the six |Ψ|=8 values in v13. Thus κ=−1.

The restrictions of affine characters of F₂⁴ to the six labels are exactly the sign patterns of product +1: every such restriction has product +1, and the 32 affine characters are distinct because the labels affinely span. Their action is transitive on the 32 sign patterns of product −1. Hence multiply by a suitable affine character to put exactly one negative sign at u=0, yielding (1). ∎

## Exact limits

The source-separated premises are `rank6-112-L16-s8-s10-exclusion-v7.md` §3; the six-character and zero count in `rank6-112-L16-s12-d5-six-character-structure-v13.md` SHA-256 `59fdd87fc77e24c2b426a017d98b6ebf33063d4ad06520ccd1d2964cfcb8ab9c`; the six-pair proof in `rank6-112-L16-s12-d5-antipodal-pairs-sublemma-v15.md` SHA-256 `10b9867ec2c76ed19c83a0023733996cd46cde9b950c5d9239866babbb15b0eb`; and the circuit proof in `rank6-112-L16-s12-d5-pair-circuit-and-a2-sublemma-v16.md` SHA-256 `664f9ef3d9237c0862ca493f16b0b54550e188d29d6fcc29072047dfd4ffbfab`. Only those precise zero-slice sections are imported; no m=24 slice, HELD candidate or held guidance is needed here.

The conditional author-only L≥18 candidate at (3,112) still requires review of its whole chain. Other types, the original witness-or-unrestricted-exclusion question and (24,24,2) remain open. All earlier findings, pre-pin corrections, v263 early-stop deviation, HOLD, N4 UNKNOWN, aux214 STOP and HELD/ZERO/NONINPUT remain binding. Novelty UNCLEARED.
