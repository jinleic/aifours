# Balanced NL242 (3,112), L=16, s=12, d=4: derivation of the N₀=52 premise and zero-slice rigidity

Owner: InfoBalancedNL242-2, info-6; continuation handle InfoBalancedNL242-2-2. Native `/bin/date` observed before this write: 2026-10-27T10:51:14-0700 PDT.

**WRITTEN AUTHOR CANDIDATE, NOT REVIEWED OR ADOPTED.** This supplies a local proof-completeness detail for the same d=4 L16 case: v10's setting asserts N₀=52 for two stated slice-zero shapes without deriving it there. The calculation below derives the equality, and further shows one of the two Parseval-level magnitude patterns is not realizable. It does not alter the pinned v9/v10, certify their other arguments, or constitute independent review. No scientific program, selected-state probe, whole-type exclusion, witness, formal/kernel or novelty claim.

## Claim and proof

Use the v9/v10 hypotheses: Σ lies in an affine 4-flat Π, |Σ|=12, τ=ΣΣ=0, Γ=∏g=+1, and N₀≥52. On the 16 dual classes of Π, let Ψ be the signed sum. Each class represents four original frequencies, so there are at most three classes not divisible by 3. All Ψ are multiples of 4, and Parseval gives Σ_classes Ψ²=16·12=192.

Let a,b,c count magnitudes 4,8,12. The number m=a+b is at most 3 and

    16m+48b+144c=192,     equivalently m+3b+9c=12.                (1)

As b≤m≤3, (1) has exactly two nonnegative possibilities: (a,b,c)=(0,3,0) or (3,0,1). In both, m=3, so N₀=4(16−3)=52. This establishes the premise used in v10 without assuming either pattern is realizable.

The first pattern is impossible. Fourier inversion on Π would give

    g(x)1_Σ(x) = (1/2) Σ_{i=1}^3 εᵢχ_{ζᵢ}(x),

which is a half-integer at every point and therefore cannot be 0 or ±1. Thus the only possible pattern is one |Ψ|=12, three |Ψ|=4, and twelve zeros. The |Ψ|=12 value saturates the sum of twelve ±1 terms, so g is a signed affine character on Σ.

For the v9 geometric shape Σ=Π\C with C an affine 2-flat, the four nonzero Ψ-frequencies are a translate of the 2-space annihilating dir(C); the unique |Ψ|=12 value is at its centre. On the Π-class, with g(x)=εχ_{ζ*}(x), Fourier inversion of h₀=φ(Ψ) gives

    ĥ₀(x)=4 εχ_{ζ*}(x) [4·1_Σ(x)−3].                              (2)

Thus ĥ₀=4g on Σ and ĥ₀=−12εχ_{ζ*} on C; it vanishes off the Π-class by affine support. Equation (2) is supplementary structure, not a new whole-case exclusion. ∎

## Status

The N₀ equality in v10 is supported by this new author derivation, while the original pinned text and its "two admissible shapes" wording remain unchanged; the first algebraic shape is now explicitly shown unrealizable. This is a disclosed local proof-completeness/precision finding and supporting lemma, not an independent review or a finding that v10's conclusion is false. The earlier attribution/zero-count MINORs, pre-pin corrections, v263 early-stop deviation, HOLD, N4 UNKNOWN, aux214 STOP and HELD/ZERO/NONINPUT remain binding.

Dependencies: `rank6-112-L16-s12-d4-partial-v9.md` SHA-256 `b489d713eb9473bf224931096afadb3394db74290145f97ca94f99948ca84bcf`, 69 LF; `rank6-112-L16-s12-d4-exclusion-v10.md` SHA-256 `c52b0f6512cf05bf35e745c2d2628fde22c1c6e7cf34bc8d024cbffeace67e62`, 47 LF; and their exact stated source cuts. The author's conditional L≥18 candidate remains unreviewed, the original witness-or-unrestricted-exclusion and (24,24,2) gaps remain OPEN, and novelty is UNCLEARED.
