# Balanced NL242 (3,112), L=16, s=16: a forced spectrum when τ=0 and the sign product is positive

Owner: InfoBalancedNL242-2, info-6; continuation handle InfoBalancedNL242-2-2. Native `/bin/date` observed before this write: 2026-10-27T10:20:27-0700 PDT.

**WRITTEN AUTHOR CANDIDATE, NOT REVIEWED OR ADOPTED.** Under the source-separated v205 L16 premises, this is a proper necessary-condition sublemma for τ=0 and Γ=∏_Σg=+1. It does not exclude this subcase or s=16. All-variable hand reasoning only; no scientific program, selected numeric-state probe, independent review, formal/kernel or novelty claim.

## Claim

If s=16, τ=0, Γ=+1 and N₀≥52, then the signed transform Ψ has exactly four values of magnitude 4, six of magnitude 8, four of magnitude 12 and fifty zero values. Thus N₀=54. The eight frequencies where Ψ/4 is odd have XOR zero; their coefficients reduced modulo 4 have product +1. Moreover the signed plane sum is A₄=40, while the total number of affine planes in Σ is between 40 and 44, so at most two planes are negative.

## 1. Unsigned moments and removal of a character

Let W be the unsigned Walsh transform of 1_Σ. Lemma H of v6 forbids side sizes 1,2,3,5; with τ=0 every side size is even. Thus W(0)=16 and for nonzero ω, W∈{0,±4,±8}. Let t and u count |W|=8 and |W|=4. Parseval yields

    4t+u=48,       0≤t≤12.                                      (1)

If p is the number of affine 2-planes in Σ, the fourth moment gives

    16⁴ + 8⁴t + 4⁴u = 64(3·16²−2·16+24p),
    p=20+2t≤44.                                                  (2)

If some |Ψ|=16, then g is a signed character on Σ and Ψ is a signed translate of W. Its number m of non-3-divisible values is 1+t+u=49−3t≥13. This contradicts m=64−N₀≤12. So |Ψ|=16 is impossible.

## 2. The three possible magnitude patterns

Since τ=0 and Γ=+1, every Ψ is divisible by 4. Let a,b,c count magnitudes 4,8,12. Parseval and m=a+b≤12 give

    a+4b+9c=64,     b+3c≥18.                                    (3)

The signed fourth moment is 64(3·16²−2·16+24A₄), with |A₄|≤p≤44. Substituting (3) gives A₄=−20+2b+12c and hence b+6c≤32. Combining with a≥0 forces c∈{3,4}, and then exactly

    (a,b,c)∈{(1,9,3), (4,6,4), (0,7,4)}.                        (4)

This is a deduction for all transforms, not a selected input.

## 3. Four odd coefficients with odd b are impossible

Put h(ζ)=Ψ(ζ)/4, so h takes integer values and its Walsh transform on x is 16g(x)1_Σ(x). In the first and third patterns in (4), there are exactly four odd coefficients and b odd even coefficients, each even coefficient being ±2.

At every x the h-transform is 0 mod 4. The even coefficients contribute 2 mod 4, so the four odd coefficients, reduced to signs ±1 modulo 4, sum to 2 mod 4. Their number of negative terms is odd at every x. Their product is therefore −1 for every x, which forces the XOR of their four distinct frequencies to be zero. They form an affine 2-plane P=ζ₀+H.

For v outside H, autocorrelation and Parseval give

    Σ_ζ h(ζ)h(ζ+v) = 4W(v),                                     (5)

which is divisible by 16 because τ=0 makes W(v) divisible by 4. The left side is twice the sum over unordered {ζ,ζ+v} pairs. Let n_v be the number of even coefficients in the coset P+v. Exactly n_v pairs connect P to P+v; their products are 2 mod 4, while every even-even product is 0 mod 4. Equation (5) therefore forces n_v even. As v runs through nonzero H-cosets, every even coefficient lies in one such coset, because P is filled by the four odd coefficients. Hence b is even, contradicting b=9 or 7.

Only (a,b,c)=(4,6,4) remains. Its eight odd h-frequencies have XOR zero: now the six ±2 terms contribute 0 mod 4, so the eight reduced odd signs have even negative parity at every x. Their product is +1, forcing the XOR to vanish. Formula A₄=−20+2b+12c gives A₄=40; (2) gives p≤44, and A₄≤p forces p≥40. ∎

## Residual and dependencies

The positive-Γ, τ=0 branch remains open at the forced pattern above. The Γ=−1 and τ≠0 cases of s=16 are not excluded. No whole-L16 or whole-type exclusion, witness, unrestricted exclusion, (24,24,2) closure, independent acceptance or novelty follows.

Uses the L16 budget N₀≥52 and Lemma H in `rank6-112-L16-reduction-v6.md` SHA-256 `450cd2ac6328e5c1c1b2a4eaad4a9d7144ac21be4582b67894ac7a35431b283d`, plus ordinary Walsh orthogonality and the exact admitted cuts cited by v6. Prior author-chain results remain unreviewed. All earlier findings, pre-pin corrections, v263 early-stop disclosure, HOLD, N4 UNKNOWN, aux214 STOP and HELD/ZERO/NONINPUT remain binding.
