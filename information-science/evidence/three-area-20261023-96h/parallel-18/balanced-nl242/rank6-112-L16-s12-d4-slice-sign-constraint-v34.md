# Balanced NL242 (3,112), L=16, s=12, d=4: a single-carrier slice-sign constraint

Owner: InfoBalancedNL242-2, info-6; continuation handle InfoBalancedNL242-2-2. Native `/bin/date` observed before this write: 2026-10-27T10:57:17-0700 PDT.

**WRITTEN AUTHOR CANDIDATE, NOT REVIEWED OR ADOPTED.** This adds an independent-of-the-moment-table necessary sublemma to the already author-excluded v9/v10 distinct-inactivity d=4 case. It is not independent review and does not replace the v10 exclusion. No scientific program, selected-state probe, accepted floor, formal/kernel or novelty claim.

## Claim

In the v9 distinct-inactivity setting, the two single-carrier slices cannot both have positive products of the twelve Σ-signs. Their three nonzero slice-sign products therefore have either two negative single-carrier products and a positive both-carrier product, or one positive and one negative single-carrier product and a negative both-carrier product.

## Proof

All twelve Σ-cosets have one small value, and all three nonzero slices have m=12 on the 16 Π-dual classes by v9. Suppose a single-carrier slice η has Γ_η=+1. Its sums are multiples of 4, with 12 non-3-divisible classes. Parseval gives

    192=16·12+48n₈+144n₁₂,

so Ψ is 0 or ±4 and φ(Ψ)=Ψ/4. Pairing the two choices of the outside carrier character, while summing the other dual extension, gives for x∈Σ

    υ_η(x)=(1/2) ĥφ(Ψ)(x)=8g_η(x).                                (1)

This is the same affine-class pairing used in v14, with 16 quotient classes and four extensions.

Fix a Σ-coset x. Let its one small T entry be −4−8e, with e=+1 for −12 and e=−1 for +4. Write its three large entries as −4+24ε_j, ε_j∈{±1}. Among the three other β-positions exactly one has the same η-character as the small entry; (1) forces its ε to be e and both opposite-character entries to have ε=−e. Thus there is exactly one large entry with ε=e, and its position must be the same-character partner of the small entry.

For two distinct nonzero η,η′ the same-character partner of any fixed β-position is different. Consequently one T-row cannot satisfy (1) in both slices. Hence the two single-carrier Γ-products cannot both be +1.

Finally, because the three nonzero radical characters multiply to 1 at every β and every Σ-coset is single, their three sign products multiply to Γ₀=+1. The two listed possibilities follow. ∎

## Limits and dependencies

This is a uniform necessary slice constraint only; it does not independently exclude the d=4 case. It uses `rank6-112-L16-s12-d4-partial-v9.md` SHA-256 `b489d713eb9473bf224931096afadb3394db74290145f97ca94f99948ca84bcf`, 69 LF; the local v32 zero-slice derivation SHA-256 `0478ceadc45b2c799c2e9b24acca48c99458e117cc4d4019c8064f6b2ea1d9c0`, 33 LF; and the explicitly stated v205 admitted cuts. The full author L≥18 chain, original witness-or-unrestricted-exclusion gap and (24,24,2) remain unreviewed/open at their previous scopes. All process findings including the v10 precision finding, v263 early-stop deviation, HOLD, N4 UNKNOWN, aux214 STOP and HELD/ZERO/NONINPUT remain binding; novelty UNCLEARED.
