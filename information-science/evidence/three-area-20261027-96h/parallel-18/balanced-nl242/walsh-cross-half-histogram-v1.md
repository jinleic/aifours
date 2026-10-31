# info-6: a simultaneous odd/even half histogram coupling

Owner **InfoBalancedNL242-2-2**, same info-6 slot. Actual `/bin/date` observed before this write: **2026-10-27T15:10:04-0700 PDT**. **NEW WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** It derives universal necessary relations for the remaining truth-support-XOR branch, not an unrestricted exclusion, witness, rank/type selection, numerical nonlinearity improvement, formal/kernel or novelty claim. No scientific program, chosen numeric state, boundary diagnostic, or external-model review was used.

## Claim

Suppose f is an actual balanced peak≤28 Boolean object, let k=W_f/4 and T=Σ_{f(x)=1}x. The unreviewed support-XOR obstruction gives T≠0. On K=T^⊥ define Q(a)=k(a)/2 mod 2 and let u be the number of its ones. On the other half let n_j count |k|=j for j∈{1,3,5,7}. Then

    0≤u≤192,  u≡0 (mod 8),                                      (1)
    u ≡ n₇+7n₁+2n₃ (mod 16),                                  (2)
    3n₇−2n₃−3n₁ ≡0 (mod 16),                                  (3)
    n₇+n₁ ≡0 (mod 2),                                          (4)

and, simultaneously,

    n₇ ≥ ceil{[2¹⁴−128 floor((4080+20u)/128)−6400
                +24n₁+16n₃]/24}.                                 (5)

No possible u or histogram is chosen or tested; these are necessary constraints on the one actual common spectrum.

## Proof

The definition-first mod-4 coupling makes Q a Boolean polynomial of degree at most 2 on the 8-dimensional K, and Q(0)=0. The elementary nonzero-polynomial bound in `walsh-support-xor-obstruction-v1.md` gives u≤192.

To prove the divisibility in (1) without any polar-rank classification, write the multilinear polynomial Q as a sum over F₂ of monomials of degree at most 2. Then (-1)^Q is the product of the factors (1−2m) over its nonconstant monomials, possibly with an overall sign. After expanding, a term using s monomials has coefficient (-2)^s and depends on at most 2s coordinates. Its sum over K is divisible by 2^{s+8−min(8,2s)}, which is at least 2⁴. Thus Σ_K(-1)^Q is divisible by 16, and u=(256−Σ_K(-1)^Q)/2 is divisible by 8.

The full fourth-moment result gives, for global magnitude counts,

    (n₂+n₆)+5n₃+7n₅+6n₇ ≡0 (mod 16).

All even coefficients lie in K and u=n₂+n₆; all odd coefficients lie in the opposite half and n₁+n₃+n₅+n₇=256. Substitution yields (2). The all-hyperplane energy result gives E_odd≡0 (mod 128), and

    E_odd=6400−24n₁−16n₃+24n₇,

which is (3). Reducing (2) and (3) mod 8, using u≡0 mod 8, and adding gives (4).

On K, each of the u points with Q=1 has k²≤36; the remaining nonzero points have k²≤16 and k(0)=0. Hence E_K≤36u+16(255−u)=4080+20u. Since E_K is divisible by 128 and E_odd=2¹⁴−E_K, substitution in the displayed formula for E_odd gives the all-parameter tradeoff (5). ∎

## Exact scope and dependencies

This relation is a necessary same-object coupling, not an existence certificate or sufficient histogram criterion. It does not close any full rank, weight, `(24,24,2)` or original witness/no-go alternative. Inputs are the S1 supplied definitions, `prerequisite-derivation-v1.md` SHA-256 `075f61ffe1b5cfb000bb3bbda9ddd7fefea04e27806f19bedd9c5a2318fa3df9`, 87 LF; the unreviewed `walsh-support-xor-obstruction-v1.md` SHA-256 `380655caaa06ea27e4236070ff66e070be63963960efebfabef2e730d2091fc4`, 49 LF; `walsh-hyperplane-energy-v1.md` SHA-256 `6a1000f1c95ef4264e82fba6d229e59393241efaed367ee4d3e5687cec0f88a0`, 49 LF; and `walsh-fourth-moment-coupling-v1.md` SHA-256 `643d903d399827d56a91adcb3af4248a20da2c7b94ee81ee4c7f066f30c87210`, 43 LF. The degree-two divisibility is proved above, without invoking any held quadratic-rank lead.

Main's notification of written support for the v1 caller does not adopt any later source; this claim remains unreviewed. Source/book equivalence, independent full-scope review, human, formal/kernel, executable and novelty gates remain unperformed for it. Prior exposure, the administrative metadata-poll MINOR and all S1 STOP/HOLD/ZERO, N4 UNKNOWN and aux214 STOP remain binding.
