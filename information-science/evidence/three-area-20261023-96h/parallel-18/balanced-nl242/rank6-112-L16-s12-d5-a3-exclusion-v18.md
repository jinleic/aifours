# Balanced NL242 (3,112), L=16, s=12, d=5: variant (a3) excluded

Owner: InfoBalancedNL242-2, info-6; continuation handle InfoBalancedNL242-2-2. Native `/bin/date` observed before this write: 2026-10-27T10:09:15-0700 PDT.

**WRITTEN AUTHOR CANDIDATE, NOT REVIEWED OR ADOPTED.** This excludes the entire previously defined (a3) variant, conditional on the source-separated v205 author chain through v16. It is not a whole-L16, whole-type, witness, unrestricted-exclusion, formal/kernel or novelty claim. The proof is exact all-variable hand reasoning; no scientific program, selected-state probe, solver or independent review was used.

## 1. Geometry and two Fourier support conditions

In (a3), p is the only outside coset, while a balanced p′ lies inside Π\Σ. The slice with p′ active has inside set Σ∪{p′} and m=20; the other p-active slice has inside set Σ and m=24. Use v15/v16: Σ is six r-pairs and their six labels form an affine six-point circuit in W/⟨r⟩. Let M₊,M₋ be the forced 3+3 pair split of the m=24 slice.

Let F₂₀(v) be the Fourier transform of the 20 non-3-divisible m=20 classes. Pure-coset slice values give F₂₀(v)∈{0,±4} for every v≠0. The m=24 signed autocorrelation in v15 has magnitude 4 at v and v+r whenever v is the difference of labels in the same M-group: exactly those two r-pairs overlap, and their pair products agree. Therefore F₂₄(v),F₂₄(v+r) are nonzero there. Since a pure p-half coset has only one nonzero slice, F₂₀(v)=F₂₀(v+r)=0 for each such pair.

Translate Π so p′=0 and choose a complement W′ to ⟨r⟩. Take all six pair representatives xᵢ in W′. The quotient labels sum to zero. Their 20 triple sums occur in complementary pairs and give exactly the ten quotient points not among the six labels: distinct noncomplementary triples cannot have equal sums without a forbidden four-label relation, and no triple sum is a label. Thus p′=0 determines a unique partition into triples C,D with Σ_{i∈C}xᵢ=Σ_{i∈D}xᵢ=0.

For the m=20 slice, write s₀ for p′'s signed character and sᵢ for the signed character at xᵢ; put tᵢ=sᵢ/s₀. In each fixed χ(r)-half the 16 quotient classes realize exactly the 16 sign patterns with

    ∏_{i∈C}tᵢ=α,    ∏_{i∈D}tᵢ=β,                  α,β∈{±1}.      (2)

The two products are constant because the triple sums are zero; each triple has four allowed patterns, independently. Let Pᵢ be the m=20 sign product of pair i and let K={i:Pᵢ=+1}. In the χ(r)=+1 half, Ψ/s₀=1+2Σ_{i∈K}tᵢ; in the −1 half, the sum is over the complementary labels. Let N be the 12 classes with 3|Ψ.

For i,j in the same M-group, the two vanishing equations for F₂₀ at xᵢ+xⱼ and xᵢ+xⱼ+r imply separately in each r-half

    Σ_{ζ∈N, χ(r)=±1} tᵢtⱼ = 0.                                  (3)

Indeed the sum and difference of the two Fourier equations isolate the two halves, and tᵢtⱼ differs from χ(xᵢ+xⱼ) by a fixed sign. For either M-group, its three pair products form the three nontrivial characters of the relative-sign 2-space. Equation (3) forces the four relative-sign patterns to occur equally often in N in each half. Thus both N-half counts are divisible by 4. Their sum is 12, and |F₂₀(r)|=|Σ_Nχ(r)|≤4, so the counts are exactly 4 and 8, in some order.                                                     (4)

## 2. Exclusion by |K|

For any half with active pair-label set A, 3|Ψ is equivalent to Σ_{i∈A}tᵢ≡1 (mod 3). The two fixed triple products in (2) determine the following counts and correlations without assuming any particular sign realization.

**|K|=0 or 6.** One half has no pair terms, so Ψ/s₀=1 there and its N-count is 0, contrary to (4).

**|K|=3.** If K is C or D, a full triple of fixed product has sum either 3/−1 (product +1) or −3/+1 (product −1), giving N-count 0 or 12, not 4 or 8. Otherwise K has a 2+1 split across C,D. Its three signs are independent under (2), so the condition is exactly two plus signs and one minus sign: 6 of 16 classes. Again this contradicts (4).

**|K|=1 or 5.** Interchange halves if necessary and take K={i}, with C={i,j,k}. The one-term half has N-count 8; the other must have count 4. In that other half the active labels are j,k and all of D. For the triple D, product +1 gives sum 3 once and −1 three times; product −1 gives sum −3 once and +1 three times. The divisibility condition yields 4 classes in the first situation and 7 in the second. Thus β=+1, and the four N-patterns in the five-term half are

    (tⱼ,tₖ)=(-1,-1), D=(+,+,+),
    (tⱼ,tₖ)=(+1,+1), D having one + and two −.

For any l∈D, their unweighted correlations are

    Σ_N tⱼtₖ=4,     Σ_N tⱼtᵢ=2α,     Σ_N tⱼt_l=−2.

Thus j has a nonzero correlation with every other label. Every M-group has size three, so j must share its group with another label, violating (3).

**|K|=2 or 4.** Interchange halves if necessary and take |K|=2. The two signs are independent under (2); the two-term half has N-count 4, hence the four-term half must have count 8. If the omitted labels are in different intrinsic triples C,D, the four active signs consist of 2+2 independent signs, giving N-count 5. Thus the two omitted labels i,j lie in one triple C={i,j,k}. The four active labels are k and the three of D; their N-count is 8 if β=+1 and 2 if β=−1. Consequently β=+1. In the N-classes of this four-term half, (tₖ,D) is either (+1,+++) or (−1, one + and two −); each such D pattern is accompanied by two choices for tᵢ,tⱼ. For every l∈D,

    Σ_N tₖt_l=4,     Σ_N tᵢtⱼ=−4α.

Equation (3) prevents k sharing an M-group with any of D, so its two group-mates must be i,j. But the second nonzero correlation then violates (3). ∎

## Exact status and dependencies

Conditional on the entire prior author chain, **(a3) is excluded**. Together with the separate, unreviewed v17 candidate excluding (a2), the remaining L16 cases are distinct-inactivity (a4), s=15 and s=16. The (3,112) L≥16 and (3,144) L≥12 floors remain author-only; no independent review, whole-type exclusion, witness, unrestricted exclusion, (24,24,2) closure or novelty is claimed.

This uses `rank6-112-L16-s12-d5-antipodal-pairs-sublemma-v15.md` SHA-256 `10b9867ec2c76ed19c83a0023733996cd46cde9b950c5d9239866babbb15b0eb`, 49 LF; `rank6-112-L16-s12-d5-pair-circuit-and-a2-sublemma-v16.md` SHA-256 `664f9ef3d9237c0862ca493f16b0b54550e188d29d6fcc29072047dfd4ffbfab`, 47 LF; and the v11–v14 chain with its exact admitted cuts. Existing errata, pre-pin corrections, v263 early-stop disclosure, HOLD, N4 UNKNOWN, aux214 STOP and all HELD/ZERO/NONINPUT restrictions remain binding. Novelty UNCLEARED.
