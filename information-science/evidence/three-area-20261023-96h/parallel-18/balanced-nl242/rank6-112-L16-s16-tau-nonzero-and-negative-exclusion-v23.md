# Balanced NL242 (3,112), L=16, s=16: τ≠0 and τ=0/negative sign product excluded

Owner: InfoBalancedNL242-2, info-6; continuation handle InfoBalancedNL242-2-2. Native `/bin/date` observed before this write: 2026-10-27T10:23:01-0700 PDT.

**WRITTEN AUTHOR CANDIDATE, NOT REVIEWED OR ADOPTED.** These are all-variable necessary exclusions conditional on the source-separated L16 budget N₀≥52. They do not exclude the positive-product, τ=0 branch or the whole L16 case. No scientific program, selected-state probe, independent review, formal/kernel or novelty claim.

## Claim A: τ≠0 is impossible

Let f=g·1_Σ, where |Σ|=16, τ=Σ_{x∈Σ}x≠0 and g(x)=±1. Its Walsh values Ψ have squared sum 64·16=1024. The product of the sixteen signed terms in Ψ(ζ) is Γχ_ζ(τ), so the classes with Ψ≡0 mod 4 and those with Ψ≡2 mod 4 are the two 32-element half-spaces χ_ζ(τ)=±1, in some order. Call the first half A and the second B.

Let m_A,m_B count the values not divisible by 3 in these respective halves. The L16 budget gives m_A+m_B≤12. In A let n₈,n₁₂,n₁₆ count the indicated magnitudes; in B let n₁₀,n₁₄ count those magnitudes. The only 3-divisible magnitude in B is 6. Parseval expands to

    1024 = 16m_A+48n₈+144n₁₂+240n₁₆
           +1152−32m_B+96n₁₀+192n₁₄,

or

    R := 3n₈+9n₁₂+15n₁₆+6n₁₀+12n₁₄
       = 2m_B−m_A−8 ≤ 16−3m_A.                                  (1)

Consequently the absolute sum on A obeys

    Σ_A |Ψ| = 4m_A+4n₈+12n₁₂+12n₁₆
            ≤ 4m_A+(4/3)R ≤ 64/3 < 32.                           (2)

If A is the half χ_ζ(τ)=t, t∈{±1}, character orthogonality gives, for every x,

    Σ_{ζ∈A} Ψ(ζ)χ_ζ(x) = 32[f(x)+t f(x+τ)].                       (3)

The bracket is an integer. By (2), (3) can hold only if it is zero for every x. Hence f(x+τ)=−t f(x), so Σ is a union of eight τ-pairs. Their total XOR is 8τ=0, contradicting τ=ΣΣ≠0. ∎

## Claim B: τ=0 and Γ=−1 is impossible

Here every Ψ is congruent to 2 mod 4. A value divisible by 3 therefore has magnitude 6 (the next possible magnitude is 18, exceeding 16). Thus 36N₀≤1024, so N₀≤28, contradicting N₀≥52. ∎

## Residual and dependencies

The only s=16 branch left by these claims is τ=0, Γ=+1, with the unreviewed v22 forced magnitude pattern (4,6,4,50) at absolute values (4,8,12,0). It remains OPEN. No whole-L16 or whole-type exclusion, witness, unrestricted exclusion, (24,24,2) closure, independent acceptance or novelty follows.

The only inherited mathematical premise used here is the L16 N₀≥52 budget in `rank6-112-L16-reduction-v6.md` SHA-256 `450cd2ac6328e5c1c1b2a4eaad4a9d7144ac21be4582b67894ac7a35431b283d`; ordinary Walsh Parseval, parity and orthogonality supply the rest. Existing findings, pre-pin corrections, v263 early-stop disclosure, HOLD, N4 UNKNOWN, aux214 STOP and all HELD/ZERO/NONINPUT remain binding.
