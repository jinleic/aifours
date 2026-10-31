# Balanced NL242 (3,112), L=16, s=12, d=5: m=24 is exactly a 3+3 pair split

Owner: InfoBalancedNL242-2, info-6; continuation handle InfoBalancedNL242-2-2. Native `/bin/date` observed before this write: 2026-10-27T10:41:18-0700 PDT.

**WRITTEN AUTHOR CANDIDATE, NOT REVIEWED OR ADOPTED.** This refines v14/v15 by deriving the m=24 sign and 3+3 split directly from the zero-slice pair-circuit geometry, without their Π-half moment or pure-coset argument. Same author; it is not independent review. No scientific program, selected-state probe, whole-type exclusion, witness, formal/kernel or novelty claim.

## Claim

Let Σ be the six r-pairs of the zero-slice circuit in v15/v16, and let g:Σ→{±1} be arbitrary. Its 32 quotient-class Walsh values Ψ satisfy the following equivalent conditions:

1. m=#{classes with 3∤Ψ}=24;
2. max|Ψ|≤6;
3. exactly three r-pairs have sign product +1 and three have sign product −1.

Under these conditions Γ=∏_Σg=−1, and Ψ has 24 magnitudes 2 and eight magnitudes 6.

## Proof

Let k be the number of positive-product r-pairs. In the half of dual classes with χ(r)=+1 only those k pairs contribute to Ψ; in the other half only the 6−k negative-product pairs contribute. Each active pair contributes twice a signed character of its quotient label. The six quotient labels form an affine circuit, so every subset of at most five is affinely independent.

If the larger of k,6−k is between 3 and 5, there is a character making every signed term in that group equal, giving max|Ψ|≥2·max(k,6−k). If the larger group has size 6, its sign patterns have a fixed product; depending on that product, a character realizes either all signs equal or five signs equal and one opposite, so max|Ψ|≥8. Consequently max|Ψ|≤6 forces k=3.

Conversely, if k=3, each half is twice a sum of three signed characters. Their labels are affinely independent. Exactly one quarter of the 16 classes in each half have all three signs equal and magnitude 6; the other three quarters have magnitude 2. Hence there are eight |Ψ|=6 and 24 |Ψ|=2 values, m=24 and Γ=−1.

Finally suppose m=24. If Γ=−1, all Ψ are congruent to 2 mod 4 and Parseval is saturated by 24·2²+8·6²=384, giving max|Ψ|=6. If Γ=+1, all Ψ are divisible by 4; Parseval gives

    384=16·24+48n₈+144n₁₂,

so every Ψ is 0 or ±4, contradicting the first paragraph. Thus m=24 implies max|Ψ|≤6 and therefore k=3. ∎

## Dependencies and limits

Uses only the six-pair part of `rank6-112-L16-s12-d5-antipodal-pairs-sublemma-v15.md` SHA-256 `10b9867ec2c76ed19c83a0023733996cd46cde9b950c5d9239866babbb15b0eb`, 49 LF, and the affine-circuit part of `rank6-112-L16-s12-d5-pair-circuit-and-a2-sublemma-v16.md` SHA-256 `664f9ef3d9237c0862ca493f16b0b54550e188d29d6fcc29072047dfd4ffbfab`, 47 LF; these parts depend on v7/v13 and their exact admitted cuts, not on the later m=24 conclusions. It gives no independent review or adoption of them.

The author-only L≥18 candidate, original witness-or-unrestricted-exclusion gap, (24,24,2), all earlier findings and pre-pin corrections, v263 early-stop deviation, HOLD, N4 UNKNOWN, aux214 STOP and HELD/ZERO/NONINPUT remain as previously stated.
