# info-6: exact 15-coefficient reduction of all dual divisibility identities

Owner **InfoBalancedNL242-2-2**, same original slot. Native `/bin/date` observed before writing: **2026-10-27T17:20:16-0700 PDT**. **ADDITIVE UNREVIEWED AUTHOR CANDIDATE**, explicitly permitted by Main under the already ACKed dual-enumerator release. This does not alter the frozen prior candidate and does not prove a witness, no-go, numerical feasibility or novelty.

## Statement: all 257 indices, both directions

For arbitrary integers A_t, −7≤t≤7, define the ordinary integer polynomial

    B(z)=Σ_{t=−7}^7 A_t(1−z)^{7+t}(1+z)^{7−t}.

Let K_j be the released length-256 binomial sum. Then the following are **equivalent**, with no moment or positivity premise:

1. For every j=0,1,…,256, the integer

       binom(256,j)+Σ_t A_t K_j(128+t)

   is divisible by 512.
2. Coefficientwise in Z/512Z[z],

       B(z)+(1−z²)^7+256z(1−z²)^6 ≡ 0.                         (1)

The polynomial in (1) has degree at most 14, so condition 2 means exactly its **15 coefficients at z^0 through z^14** vanish modulo 512. There are no additional coefficient ranges hidden beyond degree 14. This equivalence concerns **divisibility only**: the resulting dual quotients still must all be nonnegative, and a feasible collection of counts/quotients is not an actual code, generator or Boolean witness.

Equivalently, if K_j^{(14)}(r) denotes the same binomial sum for length 14, all the 257 divisibility conditions are precisely the following 15 simultaneous congruences:

    Σ_t A_t K_{2r}^{(14)}(7+t) ≡ −(−1)^r binom(7,r)  (mod 512),
        0≤r≤7;
    Σ_t A_t K_{2r+1}^{(14)}(7+t) ≡ −256(−1)^r binom(6,r)  (mod 512),
        0≤r≤6.                                                   (2)

All 15 counts, every original rank/weight alternative and `(24,24,2)` remain in scope. No count distribution, code, coefficient instance or small test case is selected.

## Proof

In the formal polynomial ring over the integers, the defining binomial expansion gives

    Σ_{j=0}^{256} K_j(128+t)z^j=(1−z)^{128+t}(1+z)^{128−t}.

Hence the generating polynomial for all 257 numerators in statement 1 is

    P(z)=(1+z)^{256}+(1−z²)^{121}B(z).                         (3)

Work coefficientwise in R=(Z/512Z)[[z]]. The factor (1−z²)^{121} has constant term one and is a unit in R, so P≡0 is equivalent in **both** directions to

    B(z)+(1+z)^{256}(1−z²)^{−121} ≡0.                          (4)

There is no loss from using formal series: P is the degree-256 polynomial whose coefficients are exactly all stated numerators, so P≡0 means divisibility at each j=0,…,256.

Set q=z/(1−z). Elementary algebra gives

    (1+z)^{256}(1−z²)^{−121}
      =(1−z²)^7 ((1+z)/(1−z))^{128}
      =(1−z²)^7(1+2q)^{128}.                                   (5)

For 1≤k≤128, binom(127,k−1) is odd: modulo 2, (1+x)^{127}=Π_{i=0}^6(1+x^{2^i}), whose coefficients are all one by unique binary expansion. Thus binom(128,k)=(128/k)binom(127,k−1) has 2-adic valuation 7−v₂(k). For k≥3 the product 2^k binom(128,k) is divisible by 512, since k−v₂(k)≥2. The k=1 coefficient is 256 and the k=2 coefficient is 256·127, also congruent to 256 modulo 512. Therefore

    (1+2q)^{128} ≡ 1+256(q+q²)  (mod 512).                     (6)

Exactly q+q²=z/(1−z)², and modulo 2, (1−z)²≡1−z². Multiplication by 256 makes this reduction valid modulo 512, so (5)–(6) give the formal-series identity

    (1+z)^{256}(1−z²)^{−121}
       ≡ (1−z²)^7+256z(1−z²)^6  (mod 512).                    (7)

The right side is a polynomial of degree 14. Substitution of (7) into (4) proves the equivalence in (1), including the converse and the fact that coefficients above degree 14 vanish automatically modulo 512. Expanding the length-14 binomial generating products and the two explicit terms of (1) gives (2) for the stated complete ranges. ∎

## Status and pinned provenance

The frozen predecessor `dual-enumerator-symbolic-v1.md` is unchanged: SHA-256 `7a05f4b954bacaf5ba865fa3559dd0ab5ff4f130f32383d60d9245ded0c92897`, 99 LF. The actual pre-body ACK is `dual-enumerator-prebody-ack-v1.json`, SHA-256 `9d4776d632f485b2ee3234385ac213d64f8617bfa89fdc64acdd29358fe6584b`, 17 LF. The released code source is `walsh-projective-code-equivalence-v1.md`, SHA-256 `b68e9f6bc546872e96066625ebfb7872f92f7a78d0187e9fa1925045148dbfeb`, 50 LF; w81's source/claim reconstruction is not a method-noninfluence certificate. All pins were verified before this write.

This is a reduction of the stated **integrality** conditions, not a claim about nonnegative D_j, existence of a common solution, original-object reconstruction, novelty or priority. It uses only the released all-variable code-enumerator statements and elementary integer binomial/formal-series algebra. No sector/half-split transform, stopped truth-degree/ANF, Gate-I, post052 route, post054 selected diagnostic, L1, held source or consumer was used; no clean-cognition assurance is inferred. Both owner PROCESS MAJORs, L1 quarantine, all STOP/HOLD/ZERO/NONINPUT, N4 UNKNOWN and aux214 STOP persist. No independent-model, human, formal/kernel or executable verification is claimed.
