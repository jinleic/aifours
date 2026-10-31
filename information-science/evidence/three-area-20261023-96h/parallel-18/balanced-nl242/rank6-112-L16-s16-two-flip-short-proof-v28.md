# Balanced NL242 (3,112), L=16, s=16: short two-flip exclusion

Owner: InfoBalancedNL242-2, info-6; continuation handle InfoBalancedNL242-2-2. Native `/bin/date` observed before this write: 2026-10-27T10:36:18-0700 PDT.

**WRITTEN AUTHOR CANDIDATE, NOT REVIEWED OR ADOPTED.** This is a second same-author shortening of the s=16 argument, not an independent review. It uses only the L16 budget/hyperplane lemma, v23's parity exclusions, and ordinary Walsh moments; it is conditional on the exact admitted cuts of those sources. It does not settle the unrestricted original problem or establish novelty.

## Proof

By the unreviewed v23, N₀≥52 forces τ=0 and Γ=+1. Let m=64−N₀≤12. With W the unsigned Walsh transform, Lemma H implies W(0)=16 and W∈{0,±4,±8} elsewhere. If t counts the |W|=8 nonzero frequencies, Parseval and the fourth moment give

    #|W|=4=48−4t,  #W=0=15+3t,  p=20+2t,  0≤t≤12,               (1)

where p counts Σ-planes. A signed value |Ψ|=16 would make g a signed character on Σ, and hence m=49−3t≥13, impossible. Every Ψ is divisible by 4. If a,b,c count its magnitudes 4,8,12, then

    a+4b+9c=64,   a+b≤12,
    b+3c≥18,      4b+9c≤64;                                     (2)

these force c≥3. Choose any |Ψ(ζ*)|=12. Its signed character agrees with g at 14 points and disagrees at two distinct points y,z. Put d=y+z≠0. For the 32 η with χ_η(d)=+1,

    Ψ(ζ*+η)=ε[W(η)−4χ_η(y)].                                   (3)

Thus each W-zero in this half is a |Ψ|=4 value. At most 32 W-zeros lie in the other half. The first use of (3), with a≤m≤12, gives 15+3t≤44, so t≤9 and p≤38.

The signed fourth moment gives A₄=−20+2b+12c, where A₄ is the signed plane sum and A₄≤p≤38. Therefore b+6c≤29. Combined with (2), this forces c=3, b=9, a=1 and A₄=34. Then p≥34, so t≥7. But the second use of (3), with the now-forced a=1, gives 15+3t≤32+1, so t≤6. Contradiction. ∎

## Status

This excludes the remaining τ=0/Γ=+1 s=16 branch only conditionally and at author-candidate level. Together with v23 it is a short author-only s=16 exclusion; it is not independent verification of any prior file. Together with the rest of the unreviewed v205 L16 case chain it gives the same conditional L≥18 candidate in v24, never an accepted floor, whole-type exclusion, witness, unrestricted exclusion, (24,24,2) closure or novelty result.

Dependencies: `rank6-112-L16-reduction-v6.md` SHA-256 `450cd2ac6328e5c1c1b2a4eaad4a9d7144ac21be4582b67894ac7a35431b283d`; `rank6-112-L16-s16-tau-nonzero-and-negative-exclusion-v23.md` SHA-256 `95d0ac2a74367702e0aad3d0baad63639e93bf6daf82d5705d7e7a9b3f918a96`, 40 LF. Earlier findings, pre-pin corrections, v263 early-stop deviation, HOLD v2, N4 UNKNOWN, aux214 STOP and every HELD/ZERO/NONINPUT cut remain binding.
