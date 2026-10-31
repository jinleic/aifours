# Balanced NL242 (3,112), L=16, s=16: sharper τ≠0 zero bound and equality structure

Owner: InfoBalancedNL242-2, info-6; continuation handle InfoBalancedNL242-2-2. Native `/bin/date` observed before this write: 2026-10-27T10:54:47-0700 PDT.

**WRITTEN AUTHOR CANDIDATE, NOT REVIEWED OR ADOPTED.** This strengthens the same s=16 τ≠0 sublemma of v23; it is not a new target, a selected-state probe, an independent review or a novelty claim. It uses exact hand algebra only.

## Claim

For any 16-point signed Σ⊂F₂⁶ with τ=ΣΣ≠0, the number N₀ of Walsh values divisible by 3 is at most 48. If equality holds and aff(Σ)=F₂⁶, then projection modulo ⟨τ⟩ has either four or eight singleton fibres, which form an affine 2-flat or 3-flat respectively. On the parity half A where Ψ≡0 mod 4, the restricted spectrum is respectively eight values ±4 on an affine 3-flat, or four values ±8 on an affine 2-flat; their signs are an affine character on that frequency flat. This is a necessary equality description, not an existence or exclusion claim at a chosen configuration.

## Proof of the bound

Use v23's notation: m_A,m_B count non-3-divisible values in the 0-mod-4 and 2-mod-4 halves, m=m_A+m_B=64−N₀, and

    R=3n₈+9n₁₂+15n₁₆+6n₁₀+12n₁₄=2m_B−m_A−8.

Exactly as in v23,

    Σ_A|Ψ| = 4m_A+4n₈+12n₁₂+12n₁₆
           ≤ 4m_A+(4/3)R ≤ (4/3)(2m−8).                        (1)

The restricted inverse is 32[f(x)+t f(x+τ)] for t∈{±1} and f=g·1_Σ. It cannot vanish identically: that would make Σ a union of eight τ-pairs with XOR 0, contradicting τ≠0. Thus its L¹ norm is at least 32. Equation (1) gives m≥16 and N₀≤48. ∎

## Equality structure

If m=16 then both inequalities in (1) are equalities and Σ_A|Ψ|=32. No full τ-pair can contribute to the restricted inverse: a contributing full pair would have magnitude 2 and force L¹ norm at least 64. Hence the inverse is supported precisely on the singleton fibres of Σ, with value ±1 there. Let h be their number.

At a singleton, equality in the triangle inequality makes every nonzero restricted spectral term have the same sign. Conversely, that alignment gives inverse magnitude 1. The alignment equations are affine character equations in the 5-dimensional quotient, so the singleton fibres form an affine flat of size h=2^{5−r}, where r is the affine dimension of the restricted spectral support. The singleton labels have XOR zero, so h cannot be 2; h=0 is impossible and h≤16. If h=16, there are no full pairs and the projected support is an affine 4-flat, giving aff(Σ) dimension at most 5. Thus under aff(Σ)=F₂⁶ only h=4 or h=8 can occur.

Equality in (1) also forces n₁₆=n₁₀=n₁₄=0. Let a,b,c count |Ψ|=4,8,12 in A. Then m_A=a+b and

    a+2b+3c=8,      2h=a+4b+9c,
    hence h=12−m_A.                                              (2)

If h=4, m_A=8 and (2) forces a=8, b=c=0. The support has affine dimension r=3 and eight points, so it is a 3-flat with signs an affine character. If h=8, m_A=4 and b+3c=4. The alternative (a,b,c)=(3,1,1) would have five spectral points, impossible in the required affine 2-flat. Therefore (a,b,c)=(0,4,0), and the four spectral points fill a 2-flat with character signs. ∎

## Limits

The L16 premise N₀≥52 is already incompatible with N₀≤48. Equality at 48 is only an analytic boundary description and is not claimed to occur for the NL242 target. The conditional author-only L≥18 floor still requires whole-chain independent review. The original witness-or-unrestricted-exclusion and (24,24,2) gaps remain open. All process findings, v263 early-stop disclosure, HOLD, N4 UNKNOWN, aux214 STOP and HELD/ZERO/NONINPUT remain binding; novelty UNCLEARED.

Dependency: `rank6-112-L16-s16-tau-nonzero-and-negative-exclusion-v23.md`, SHA-256 `95d0ac2a74367702e0aad3d0baad63639e93bf6daf82d5705d7e7a9b3f918a96`, 40 LF, specifically its universally quantified parity-half identity and inverse formula; ordinary Fourier orthogonality supplies the equality analysis.
