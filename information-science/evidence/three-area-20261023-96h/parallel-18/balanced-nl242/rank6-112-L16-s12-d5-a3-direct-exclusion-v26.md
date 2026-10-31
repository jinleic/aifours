# Balanced NL242 (3,112), L=16, s=12, d=5: a direct m=20 exclusion of (a3)

Owner: InfoBalancedNL242-2, info-6; continuation handle InfoBalancedNL242-2-2. Native `/bin/date` observed before this write: 2026-10-27T10:29:37-0700 PDT.

**WRITTEN AUTHOR CANDIDATE, NOT REVIEWED OR ADOPTED.** This is a same-author alternative to v18, not independent verification. It eliminates (a3) using its m=20 slice alone, without the m=24 sign-product or support-disjointness step. It remains conditional on the author-only zero-slice pair/circuit chain. No scientific program, selected-state probe, formal/kernel or novelty claim.

## Setting

The v11 (a3) reduction has exactly one balanced p outside Π and, in one p-active slice, all 12 Σ-points plus the inside balanced p′ active, with m=20. The outside single-carrier and pure-coset lemmas require

    F(v)=Σ_{ζ:3∤Ψ(ζ)}χ_ζ(v)∈{0,±4} for every v∈W\{0}.           (1)

By the zero-slice part of v15 and v16, Σ is six r-pairs whose quotient labels form an affine six-point circuit. Translate p′ to 0 and choose representatives xᵢ in a complement to ⟨r⟩. The missing quotient point p′ is the common sum of two complementary triples C,D of labels. As in v18, normalizing their signed characters by the p′ character gives variables tᵢ with fixed products

    ∏_{i∈C}tᵢ=α,   ∏_{i∈D}tᵢ=β,

and all 16 sign patterns with these two products occur once in each fixed χ(r)-half. Put K={i: the two active Σ-signs in pair i have product +1}. In the plus half Ψ/s₀=1+2Σ_{i∈K}tᵢ, in the minus half the sum is over the complementary labels. Let N={ζ:3|Ψ}; it has 12 points. For v≠0, the N-transform is −F(v). In each half 3|Ψ iff the corresponding sum of tᵢ is 1 mod 3.

## Contradictions for all |K|

**0 or 6.** One half has no pair terms and hence no N-classes; all 12 lie in the other half. Therefore |F(r)|=12, contrary to (1).

**3.** If K is C or D, a full fixed-product triple contributes either 0 or 12 N-classes in its half; since the total is 12, the half counts are 0 and 12, again contradicting (1) at r. Otherwise K contains two labels i,j in C and one k in D. In each half the three active variables are independent, and N is the six classes with two plus signs and one minus sign among them. In the K half, Σ_N tᵢtₖ=−2. In the other half, tᵢ is free after the active variables are fixed, while tₖ is determined by the two active D-signs, so Σ_N tᵢtₖ=0. For v=xᵢ+xₖ, the N-transform is therefore ±2, contrary to (1).

**1 or 5.** Interchange halves and take K={i}, C={i,j,k}. Its N-count is 8. The other half has N-count 4; with the full D-triple this forces β=+1, and its four N-patterns are (tⱼ,tₖ)=(-1,-1) with D=+++, or (tⱼ,tₖ)=(+1,+1) with D one-plus/two-minus. For v=xⱼ+xₖ, the K-half contribution to the N-transform has magnitude 8 and sign α, because tⱼtₖ=αtᵢ=α on its N-classes. The other half's contribution has magnitude 4, because tⱼtₖ=+1 throughout. Taking v and v+r adds and subtracts these half-contributions; one magnitude is 12. This contradicts (1).

**2 or 4.** Interchange halves and take |K|=2. The K-half N-count is 4, so the other half has count 8. If the two K-labels lie in different C,D triples, the four active signs in the other half are independent and its N-count is 5, impossible. Thus K={i,j}⊂C={i,j,k}; the other N-count is 8 only when β=+1. In the K-half, N has tᵢ=tⱼ=−1, so its contribution at v=xᵢ+xⱼ has magnitude 4. In the other half, N has (tₖ,D)=(+1,+++) or (−1, one-plus/two-minus), with two choices for tᵢ,tⱼ for each D-pattern. Since tᵢtⱼ=αtₖ, its contribution is −4α. Again the transforms at v and v+r are their sum and difference; one has magnitude 8, contradicting (1). ∎

## Exact status and dependencies

This excludes (a3) only conditional on `rank6-112-L16-s12-d5-partial-v11.md`, the six-character zero-slice theorem v13, the pairing proof in `rank6-112-L16-s12-d5-antipodal-pairs-sublemma-v15.md` SHA-256 `10b9867ec2c76ed19c83a0023733996cd46cde9b950c5d9239866babbb15b0eb`, and the circuit proof in `rank6-112-L16-s12-d5-pair-circuit-and-a2-sublemma-v16.md` SHA-256 `664f9ef3d9237c0862ca493f16b0b54550e188d29d6fcc29072047dfd4ffbfab`; the latter two are used only at those exact sections, not their m=24 consequences. The exact admitted cuts and all errata remain as in the chain. No whole-type exclusion, original witness, unrestricted exclusion, (24,24,2) closure, independent acceptance or novelty follows. Earlier process findings, v263 early-stop deviation, HOLD, N4 UNKNOWN, aux214 STOP and all HELD/ZERO/NONINPUT remain binding.
