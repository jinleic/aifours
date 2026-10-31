# info-6 frontier: zero-XOR Walsh support and at least four Walsh zeros

Owner **InfoBalancedNL242-2-2**, original info-6 target. Native `/bin/date` observed before writing: **2026-10-28T17:31:10-0700 PDT**. **NEW WRITTEN CANDIDATE, NOT YET DISJOINTLY REVIEWED OR ADOPTED.** This is a universal necessary obstruction on one actual balanced Boolean function, not a selected spectral histogram, witness, unrestricted no-go, formal/kernel result or novelty claim.

## 1. The stronger universal conditions

For every balanced f:F₂⁹→{0,1} with max_a|W_f(a)|≤28, set k=W_f/4, S={a:k(a)≠0}, Z=V\S, and S₄={a:|k(a)|=4}={a:|W_f(a)|=16}. Then

1. For **every** u∈V, the numbers of positive and negative values among `k(a)(−1)^{a·u}` are both even.
2. The vector XOR of all frequencies in S is 0. Hence the XOR of all frequencies in Z is also 0, |Z| is even, and **|Z|≥4** because 0∈Z. In fact 4≤|Z|≤148.
3. The layer S₄ has even cardinality and vector XOR 0. Thus it is either empty or has at least four frequencies.

Every u, frequency and original rank/weight alternative, including `(24,24,2)`, is retained. These constraints strengthen the previously supported nonzero-frequency Walsh-zero statement; they do not rule out an actual function or realize one.

## 2. Reconstructed integer enumerator congruences

First take any such actual f with f(0)=0. Its one-support has 256 distinct nonzero points. Use these as columns of G. For a≠0, the original Walsh definition and the vanishing full-space nontrivial character sum give

    W_f(a)=4(w(aᵀG)−128).

The peak bound puts all these 511 codeword weights in [121,135], so G has rank 9. Write A_t for the number with weight 128+t (−7≤t≤7), and D_j for the number of binary vectors of weight j in the dual. Summing the character indicator of Gv=0 over all j-subsets gives, simultaneously for all j,

    512D_j=binom(256,j)+Σ_t A_t K_j(128+t),
    K_j(w)=Σ_i (−1)^i binom(w,i)binom(256−w,j−i).              (1)

Consequently the polynomial P whose coefficients are those numerators is divisible by 512 coefficientwise. Put

    B(z)=Σ_{t=−7}^7 A_t(1−z)^{7+t}(1+z)^{7−t},
    H(z)=(1−z²)^7+256z(1−z²)^6.

The defining binomial products give P(z)=(1+z)^{256}+(1−z²)^{121}B(z). In the formal ring (Z/512Z)[[z]], `(1−z²)^{121}` is a unit. Moreover

    (1+z)^{256}(1−z²)^{−121} ≡ H(z) (mod 512),
    B(z)+H(z) ≡0 (mod 512).                                     (2)

For completeness, write q=z/(1−z). The left side is `(1−z²)^7(1+2q)^128`. For 1≤j≤128, binom(127,j−1) is odd by `(1+x)^127=Π_{i=0}^6(1+x^{2^i})` modulo 2; hence v₂ binom(128,j)=7−v₂(j). In the binomial expansion, terms j≥3 vanish modulo 512, and the first two nonconstant terms both have coefficient 256. Since q+q²=z/(1−z)²≡z/(1−z²) mod 2, (2) follows. No numerical distribution is presumed.

Make the two formal substitutions z=1−u and z=u−1 in the **polynomial** congruence (2), and compare coefficients. At degree u^6, the H contribution is divisible by 512; the nonzero B coefficients each have factor 256 and an odd remaining binomial. This gives

    Σ_{t=−7}^{−1}A_t ≡0 (mod 2),      Σ_{t=1}^{7}A_t ≡0 (mod 2). (3)

Since Σ_tA_t=511, A₀ is odd. At degree u^7, after division by 128 and reduction modulo 4, the two substitutions give the stronger congruences

    A₀+2A_{−4}+1≡0 (mod 4),       A₀+2A_4+1≡0 (mod 4).          (4)

One way to see the coefficient reduction is `(1+x)^8≡1+2x^4+x^8 (mod 4)` and, for 0≤s≤6, `binom(8+s,7)≡2 binom(s,3) (mod 4)`; the last binomial is odd only when s=3. The positive-side calculation is the symmetric substitution. Equations (3)–(4) are statements about **all** A_t, not an exhibited distribution.

## 3. Universal translations force XOR zero

Now take an arbitrary original balanced f, without assuming f(0)=0. For every u∈V define `f_u(x)=f(x+u)⊕f(u)`. It is balanced, has f_u(0)=0, and has the same Walsh magnitudes, with

    k_{f_u}(a)=(−1)^{f(u)+a·u}k_f(a).                            (5)

Apply (3) to each f_u. Since both signs occur an even number of times, the possible common sign from f(u) does not affect that parity. Thus for every u the number of a∈S with k_f(a)(−1)^{a·u}<0 is even. Let N be the negative support at u=0. Its parity at u differs from |N| by

    Σ_{a∈S}(a·u) = u·(⊕_{a∈S}a)  (mod 2).

The left parity is 0 for every u, so nondegeneracy of the dot pairing forces ⊕S=0. Every coordinate occurs in 256 of the 512 vectors, so ⊕V=0; consequently ⊕Z=0. The support size is even, so |Z| is even. Since balance puts 0 in Z, a two-element Z would have a nonzero XOR; therefore |Z|≥4.

The odd value A₀ counts nonzero Walsh zeros, independently of the normalization in (5). The 256 odd codeword deviations have square sum at most 256·49, while the full sum is 16384, so the 255 even deviations contribute at least 3840. Of these, A₀ are zero and each other square is at most 36; hence `36(255−A₀)≥3840`, giving odd A₀≤147 and |Z|=A₀+1≤148.

Finally (4) makes A_4 and A_{−4} have the same parity, so |S₄| is even; it also fixes A_4 mod 2 solely from the invariant zero count A₀. Apply this to every f_u. The common sign in (5) may swap the two signs, but cannot change their parity because |S₄| is even. Therefore the parity of `{a∈S₄:k_f(a)(−1)^{a·u}=4}` is constant in u, and the same nondegeneracy argument gives ⊕S₄=0. A two-point set of distinct vectors has nonzero XOR, so a nonempty S₄ has at least four points. ∎

## 4. Independent symbolic checks and provenance

`frontier-20261028-zero-structure-check.py`, SHA-256 `730bed32e53378fc9b4b38135860028f72b363aed39151ca11424779ca6e45b0`, 105 LF, was executed locally with `/opt/homebrew/bin/python3 -B`. Its receipt `frontier-20261028-zero-structure-check-result.json`, SHA-256 `6b9959af55b0f5049e6f4ddbd9f31544ba091c6b3654161180e28f374ce59480`, 107 LF, records: all **257** coefficients of the integer polynomial identity checked modulo 512; all 15 formal A_t coefficients for both substitutions at degrees 6 and 7 matched (3)–(4); and a mutated constant was rejected at the intended degree. The computation checks the finite polynomial identities, not the existence of a target f or the whole written implication.

The exact code/dual interface previously received same-harness source reconstruction at `walsh-projective-code-equivalence-v1.md` SHA-256 `b68e9f6bc546872e96066625ebfb7872f92f7a78d0187e9fa1925045148dbfeb`, 50 LF; the parent-supported 15-congruence source is `dual-enumerator-congruence-reduction-v1.md` SHA-256 `6817ccf924a52f42fe5d860b936f79b021e6dd095efbd1b10c5a8a2facb74dad`, 70 LF. The proof above reconstructs the needed interface and congruence instead of treating an old stopped outcome as a premise.

An earlier same-owner frequency-label episode was historically held; the 2026-10-28 owner direction permits new independently checked scientific work but does not retroactively validate it. This is a fresh written reconstruction with an exact symbolic checker, **not** a claim of blind cognition or prior process success. A disjoint written review is still required before adoption. No external-model review, human, Lean/kernel, numerical uniqueness, literature novelty or original witness/no-go is asserted.
