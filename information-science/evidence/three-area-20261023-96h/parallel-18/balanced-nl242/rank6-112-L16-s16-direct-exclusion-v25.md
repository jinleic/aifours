# Balanced NL242 (3,112), L=16, s=16: a direct written exclusion from the L16 budget

Owner: InfoBalancedNL242-2, info-6; continuation handle InfoBalancedNL242-2-2. Native `/bin/date` observed before this write: 2026-10-27T10:27:03-0700 PDT.

**WRITTEN AUTHOR CANDIDATE, NOT REVIEWED OR ADOPTED.** This is an alternative, shorter proof of the s=16 exclusion, not independent verification of v22–v24. It depends on the same source-separated v205 Lemma H/budget and the written parity exclusions in v23; all are unreviewed except their explicitly admitted cuts. No scientific program, selected-state probe, formal/kernel or novelty claim.

## Direct proof of the remaining branch

By v23 it suffices to take τ=0 and Γ=∏_Σg=+1. Put m=64−N₀≤12. Let W be the unsigned Walsh transform. Lemma H and τ=0 give W(0)=16 and W∈{0,±4,±8} elsewhere. If t counts |W|=8 away from zero, Parseval and the fourth moment give

    0≤t≤12,    #|W|=4 is 48−4t,    #W=0 is 15+3t,
    p=20+2t,                                                   (1)

where p is the number of Σ-planes. All Ψ are multiples of 4. A value |Ψ|=16 would make g a signed character on Σ, giving m=1+t+(48−4t)=49−3t≥13, impossible.

Let a,b,c count |Ψ|=4,8,12. From Parseval, a+4b+9c=64 and m=a+b≤12. Hence b+3c≥18 and 4b+9c≤64, so c≥3. Fix a frequency ζ* with |Ψ|=12. Its signed character disagrees with g at exactly two points y,z; for d=y+z≠0,

    Ψ(ζ*+η)=ε[W(η)−2χ_η(y)−2χ_η(z)].

Every zero of W in the χ_η(d)=+1 half gives a non-3-divisible Ψ-value ±4. There are at least (15+3t)−32 such zeros, so m≤12 forces t≤9 and p≤38.

The signed fourth moment, with A₄ the sum of g over the Σ-planes, gives A₄=−20+2b+12c. Since A₄≤p≤38, b+6c≤29. Together with b+3c≥18 this forces c≤3; hence c=3. The same inequalities force b=9 and a=1.

Put h=Ψ/4. Exactly four coefficients of h are odd and nine are ±2. Its Walsh transform is 16g·1_Σ. Modulo 4, the nine even terms contribute 2, so the four odd coefficients, reduced to ±1, have odd negative parity at every dual point. Their frequency XOR is zero; they form an affine plane P=ζ₀+H.

For v∉H, autocorrelation gives

    Σ_ζ h(ζ)h(ζ+v)=4W(v),

which is divisible by 16 because τ=0 makes W(v) divisible by 4. In the unordered-pair sum, each even coefficient in P+v forms exactly one odd-even pair and contributes 2 mod 4; every even-even pair contributes 0 mod 4. Thus the number of even coefficients in P+v must be even. The plane P is full of odd coefficients, so every one of the nine even coefficients lies in a nonzero H-coset. Summing the even coset counts makes nine even, a contradiction. ∎

## Exact scope

This independently written route, together with v23, excludes s=16 **only at author-candidate level**. The chain v6–v21 and this result imply the same conditional author-only L≥18 candidate as v24. It is not a review, an accepted floor, a whole-type exclusion, a witness, unrestricted exclusion, (24,24,2) closure or a novelty claim. All earlier findings, pre-pin corrections, v263 early-stop disclosure, HOLD v2, N4 UNKNOWN, aux214 STOP and HELD/ZERO/NONINPUT remain binding.

Dependencies: `rank6-112-L16-reduction-v6.md` SHA-256 `450cd2ac6328e5c1c1b2a4eaad4a9d7144ac21be4582b67894ac7a35431b283d`; `rank6-112-L16-s16-tau-nonzero-and-negative-exclusion-v23.md` SHA-256 `95d0ac2a74367702e0aad3d0baad63639e93bf6daf82d5705d7e7a9b3f918a96`, 40 LF; ordinary signed/unsigned Walsh moments.
