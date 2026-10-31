# Higher powers of 5: arbitrary-tail parity, Fourier saturation, and the first residual quotient

Owner **MathShor-2**, math-5. Native `/bin/date` immediately before writing: **Thu Oct 29 13:38:34 PDT 2026**.

**WRITTEN UNREVIEWED CANDIDATE for arbitrary anchored cyclic tilings.** This is not a variant of the constructed f217 tail. It derives constraints from **every** possible Q under the stated head cardinality. No T2, solver result, or previously submitted scientific theorem is a premise. A cyclotomic field-degree fact is named explicitly in §4. The unrestricted Shor completion problem remains OPEN.

## 0. Source boundary and exact scope

Main directed one packet on the real higher-5-power residual: an argument or obstruction for arbitrary tails Q **with the actual head anchors present**. The proof below starts from that full hypothesis. It does not assume the f217/f219 tail construction, its six special 2-adic exceptions, or any chosen Q. Parent reports of f189/f201/f212 dispositions and of f217 review are status only. No Q55, fibre/cofactor, prior candidate verdict, solver output, or HELD/ZERO body is imported.

This is same-author work after reading and considering earlier unreviewed fibre/cofactor material and after writing the f217/f219 constructions. There is no blind-review, unaffected-cognition, independent-author or novelty claim. Earlier arithmetic and cadence disclosures, the parent-recorded service gap, and all historical quarantine records remain in force.

Put A={0,3,8,11}, Y={0,1,7,13,14}. An anchored tiling is P,Q⊆Z_n with A⊆P, Y⊆Q and P⊕Q=Z_n.

> **Theorem (candidate).** Suppose n>14 and P⊕Q is an anchored tiling with |P|=5^e2^a, e≥2, a≥0. Then:
>
> 1. A tail is odd **exactly when** it is 1 mod 3. For each j mod 11, all tails congruent to j mod 11 have one common residue f(j) mod 25. Moreover f(j)∈Y for all j and
>
>        f(0)=0, f(1)=1, f(2)=13, f(3)=14, f(7)=7.           (F25)
>
> 2. For each parity ε and residue j mod 11, the numbers of P-elements in the 25 classes mod 25 are equal. For each i mod 3 and j mod 11, the difference between the even and odd head counts is also independent of the residue mod 25.
>
> 3. In particular |P|≥100. Thus |P|=25 and |P|=50 are impossible at **every** order n.
>
> 4. If |P|=100, then the actual head projection mod 66 is exactly
>
>        P mod 66 = 25·{0,3,8,11}                                (S66)
>
> as a multiset: each of those four residues appears 25 times, and no other residue appears. Each of the four classes contains exactly one P-element in every residue class mod 25.

The displayed multiset equation is called the *saturation identity* below.

The theorem is conditional on a tiling; it does not prove an anchored tiling exists. It rules out two global cardinalities, but makes **no** order-floor, all-order noncompletion, or higher-5-power solution claim. The |P|=100 case is a necessary structure, not an exclusion.

For the literal Shor code

    S=b{1,a,a^7,a^13,a^14} ∪ {a^3,a^8}b{1,a^2,a^4,a^6} ∪ a^11b{1,a,a^2},

the actual-word border theorem of Restivo–Salemi–Sportelli, as stated in Cordero [arXiv:2301.13566v1, p. 3, Thm 1.1](https://arxiv.org/pdf/2301.13566v1), imports the same-code anchored tiling caller for a finite UD factor-complete extension with pure-a atom a^n. It is not used to prove the cyclic statement, and a quotient or cyclic tiling is not claimed sufficient to construct a code.

## 1. Elementary tiling tools and the universal tail rule

We reconstruct the two required tiling facts. If P⊕Q=Z_n and gcd(t,|P|)=1, then tP⊕Q=Z_n. For a prime ℓ∤|P|, let p,q be the group-ring sums and G the sum of all residues. In F_ℓ[Z_n], freshman's dream and Fermat give

    p^ℓ q = p^(ℓ−1)G = |P|^(ℓ−1)G = G.

The corresponding nonnegative integer coefficients are all congruent to 1 mod ℓ and sum to |P||Q|=n, so all are 1. This proves injectivity and the ℓ-dilation tiling; iterate over prime factors of t.

Also, nonzero P- and Q-differences in a tiling cannot have the same gcd with n. Indeed if gcd(d_P,n)=gcd(d_Q,n)=g<n, write d_P=gu,d_Q=gv with u,v units mod n/g. CRT lifts v/u to a unit w mod n. Since |P| divides n, w is coprime to |P|; wP⊕Q is a tiling, but wd_P≡d_Q gives a collision. These facts are re-proved here, not imported from a previous packet.

Elementary anchor consequences give 330|n: if n is odd, the head difference 8 and tail difference 1 both have gcd 1 with n; if 3,5 or11 is absent from n, the corresponding head difference and tail difference 1 collide. Furthermore 3,5,11 divide |Q|: otherwise dilating Q by such a prime makes the scaled tail difference 1 and actual head difference of that prime collide. Thus write

    n=2^K·5^v·R,   |P|=5^e2^a,   |Q|=5^(v−e)2^bR,
    K≥1, v≥e+1, a+b=K, R odd, gcd(R,5)=1, 33|R.            (1)

Since R is coprime to |P|, RP⊕Q tiles. Restricting to cosets mod R gives the same positive number of tails in every class mod R. Consequently every class mod 33 has exactly

    w=5^(v−e)·2^b·R/33 > 0                                      (2)

tail elements. No squarefreeness or fixed order is assumed.

**Universal odd-difference rule.** For q,q′∈Q of opposite parity, x=q−q′ satisfies

    25∤x  ⇒  gcd(x,165)=1.                                      (3)

Proof. Put g=gcd(x,n), which is odd. If 5|x but 25∤x, then 5 exactly divides g; t=g/5 is coprime to |P|, and the scaled actual A-difference 5 in tP⊕Q has the same gcd g as x. If 5∤x and 3|x or 11|x, use t=g/3 or t=g/11 respectively and the corresponding actual A-difference. In both cases the dilation and equal-gcd exclusion give a contradiction. ∎

In particular, opposite-parity tails that agree mod 3, mod 5 or mod 11 must agree mod 25.

## 2. The arbitrary Q is forced into a five-value mod-25 graph

**No even q∈Q is 1 mod 3.** Such a q compared with the three odd anchors 1,7,13 would, by (3), be simultaneously congruent to 1,7,13 mod 25. Thus all tails 1 mod 3 are odd.

Every class mod 33 is nonempty by (2).

- All tails in class 3 mod 33 are even. An odd element there would compare to even anchor 0 via mod 3 and to even anchor 14 via mod 11, forcing residues 0 and 14 mod 25.
- All tails in class 25 mod 33 are odd, since 25≡1 mod 3. Comparing any of them to even anchor 14 via mod 11 gives residue 14 mod 25. Every class-3 tail is even and agrees mod 11 with such an odd class-25 tail; it is therefore also 14 mod 25.
- All tails in class 11 mod 33 are even. An odd element there would compare to even anchor 14 via mod 3 and even anchor 0 via mod 11, forcing 14 and 0 mod 25.
- All tails in class 22 mod 33 are odd. They agree mod 11 with even anchor 0 and are 0 mod 25. Every even class-11 tail agrees mod 11 with an odd class-22 tail, so is also 0 mod 25.

Now an odd tail 0 mod 3 would have to agree mod 25 with both even anchor 0 and an even class-3 tail, giving 0 and 14. An odd tail 2 mod 3 would have to agree with both even anchor 14 and an even class-11 tail, again giving 14 and 0. Hence

    q odd  ⇔  q≡1 (mod 3).                                      (4)

For every j mod 11, choose an odd Q-element with residue j mod 11 and 1 mod 3, and an even Q-element with residue j mod 11 and 0 mod 3. They exist by (2). All opposite-parity pairs with that j agree mod 11, so (3) makes **every** Q-element of that j have the same residue f(j) mod 25. The five anchors force

    f(0)=0, f(1)=1, f(2)=13, f(3)=14, f(7)=7.                 (5)

For any j,k, choose an odd tail with mod-11 label j and an even tail with label k. If f(j)≡f(k) mod 5, their difference is divisible by 5 and (3) gives f(j)=f(k) mod 25. The five values of Y occupy all five residues mod 5, exactly once. Thus every f(j) equals one of those five anchored values mod 25. Taking representatives in [0,25), f(j)∈Y. This proves Theorem 1, with six labels genuinely unspecified.

## 3. A nonvanishing statement for every such arbitrary tail

For roots ω∈{1,−1}, τ∈μ_3, η∈μ_11 and ξ∈μ_25, let Q̂ be the Fourier transform of Q at the character x↦ω^xτ^xη^xξ^x. By (2), (4) and the function f,

    Q̂(ω,τ,η,ξ)=w·(1+τω+τ²)·Σ_(j=0)^10 η^j ξ^(f(j)).       (6)

We claim the sum over j in (6) is nonzero whenever ξ≠1, for **every allowed function f**.

- If η≠1, its minimal polynomial over Q(ξ) is Φ_11 of degree 10: the named classical fact is [Q(ζ_11,ζ_5^s):Q(ζ_5^s)]=φ(11)=10 for coprime conductors, a consequence of cyclotomic irreducibility and the totient degree formula. A degree-at-most-10 polynomial vanishing at η would have all 11 coefficients equal. The coefficients at j=0 and j=1 are 1 and ξ, different since ξ≠1.
- If η=1 and ξ has order 25, the sum is F(ξ), where F(X)=Σ_j X^(f(j)) is a nonzero integer polynomial of degree at most 14. The minimal polynomial Φ_25 has degree 20, so F(ξ)≠0.
- If η=1 and ξ has order 5, reduce F mod X^5−1. Its five residue coefficients are positive integers summing to 11, because f takes values in Y and the anchors cover every residue mod 5. They cannot all be equal since 5∤11. A degree-at-most-4 polynomial vanishing at a primitive fifth root would be a scalar multiple of Φ_5 and have all five coefficients equal.

When τ=1 and ω=±1, the prefactor 2+ω is nonzero. When ω=−1 and τ≠1, it is 1−τ+τ²=−2τ, also nonzero. Therefore

    Q̂(ω,1,η,ξ) ≠ 0       for ω=±1, η∈μ_11, ξ∈μ_25\{1};
    Q̂(−1,τ,η,ξ) ≠ 0      for τ∈μ_3, η∈μ_11, ξ∈μ_25\{1}. (7)

No statement is made here for arbitrary high 2-adic roots or roots of order at least 125. In particular the six free f-values are not silently fixed.

## 4. Fourier inversion and the |P|≥100 bound

For each parity ε, j mod 11 and s mod 25, let H_(ε,j)(s) count P-elements with those three residues. The tiling identity gives P̂Q̂=0 at every nontrivial character. Equation (7), followed by Fourier inversion in parity and mod 11, says that for every ε,j all nontrivial Fourier coefficients of H_(ε,j) on Z_25 vanish. Thus

    H_(ε,j)(s)=c_(ε,j)    for every s∈Z_25,                    (8)

where c_(ε,j) is a nonnegative integer.

The anchors 0,11,3,8 lie in the four **distinct** parity/mod-11 buckets

    (even,0), (odd,0), (odd,3), (even,8).

Each corresponding c_(ε,j) is at least 1, since (8) is constant and its bucket contains the named actual anchor. Therefore |P|=25Σ_(ε,j)c_(ε,j)≥100. If |P|=25·2^a, this excludes a=0,1 and proves Theorem 3.

Now let H_(ε,i,j)(s) count P-elements also having residue i mod 3. The second line of (7), followed by Fourier inversion in mod 3 and mod 11, gives

    H_(0,i,j)(s)−H_(1,i,j)(s) = d_(i,j), independent of s.    (9)

This is the exact signed joint constraint claimed in Theorem 2. It is not an assumption that all individual mod-3 head fibres are uniform.

## 5. The exact |P|=100 saturation

Suppose |P|=100. Equation (8) and the four actual anchors leave exactly the four buckets listed above, with c=1 in each and c=0 elsewhere. In each of these buckets, there is exactly one P-element for every s mod 25.

For a head residue s mod 25, write E(s),O(s)∈Z_3 for the mod-3 labels of the even and odd elements in the j=0 buckets. Equation (9) says the vector

    e_(E(s))−e_(O(s)) ∈ Z^3

is independent of s. If it is nonzero, its ordered positive and negative coordinates determine E(s),O(s) uniquely, so both are constant. If it is zero, E(s)=O(s) for every s.

The j=3 bucket is odd only. Equation (9) therefore makes its mod-3 label independent of s; anchor 3 sets it to 0. Likewise the j=8 bucket is even only and anchor 8 sets its mod-3 label to 2.

The alternative E(s)=O(s) for all s is impossible by a **full folded tiling count**. Fix any target with parity 0, residue 0 mod 3, arbitrary mod-11 label J and arbitrary mod-25 label z. Every residue of the folded group Z_2×Z_3×Z_11×Z_25 receives n/(2·3·11·25)=2w representations.

- The even and odd j=0 P-rows must pair with Q of label J and the same P-residue s=z−f(J). If E(s)=O(s), exactly one of those two P-elements yields target mod 3: for even P, allowed Q residues mod 3 are {0,2}; for odd P, Q must be odd and has residue 1.
- The j=8 even P-row has residue 2 mod 3, so it would need an even Q-element of residue 1 mod 3, which does not exist.
- The j=3 odd P-row has residue 0 mod 3, so it would need an odd Q-element of residue 0 mod 3, which does not exist.

Each permissible Q mod-33 class contains exactly w elements, and its residue mod 25 is f(J). Therefore the total would be w, not the required 2w. Contradiction.

Thus E,O are constant and distinct. Anchor 0 gives E(0)=0; anchor 11 gives O(11)=2. So the four actual parity/mod-3/mod-11 rows are

    (even,0,0), (odd,2,0), (odd,0,3), (even,2,8).

CRT identifies these with residues 0,11,3,8 mod 66. Each bucket has exactly 25 elements, one per mod-25 class, proving the saturation identity. ∎

## 6. A fully anchored quotient obstruction to further inference

The saturation identity is not itself a contradiction. Here is an explicit **twofold quotient cover** satisfying both literal anchor sets and every constraint of §§2–5 at the level of Z_1650≅Z_2×Z_3×Z_11×Z_25.

Choose f(0)=0,f(1)=1,f(2)=13,f(3)=14,f(7)=7, and set f(j)=0 at the six other j. Define

    P₀ = {CRT(a mod 2, a mod 3, a mod 11, s) : a∈A, s∈Z_25},
    Q₀ = {CRT(1_(r≡1 mod3), r mod3, r mod11, f(r mod11)) : 0≤r<33}.

All CRT expressions are residues mod 1650. Then |P₀|=100, |Q₀|=33, A⊆P₀, Y⊆Q₀, and P₀ mod66 consists of 25 copies of each actual head anchor.

For a target parity ε and residue t mod3, the pairs (a, q mod3) that can represent it are exactly:

| target parity ε | t=0 | t=1 | t=2 |
|---|---|---|---|
| 0 | (0,0),(11,1) | (3,1),(8,2) | (0,2),(8,0) |
| 1 | (3,0),(8,1) | (0,1),(11,2) | (3,2),(11,0) |

For each of these two pairs, the target mod-11 label determines the Q-label j uniquely, and the target mod-25 residue then determines the P-residue s uniquely. Thus **every** element of Z_1650 has exactly two representations in P₀+Q₀. This proves a twofold cover, not P₀⊕Q₀. Its role is to show that the derived saturation and the simultaneous anchors are mutually consistent in the entire displayed quotient. It is neither an original-code completion nor evidence that an anchored cyclic tiling exists at any order.

## 7. Finite controls, exact remaining gap, and review obligations

The owner checked the explicit quotient by exact integer CRT and `collections.Counter` in the retained eval kernel. The actual output: |P₀|=100, |Q₀|=33; A⊆P₀ and Y⊆Q₀; all 1650 residues have representation count 2; the P mod-66 histogram is {0:25,3:25,8:25,11:25}. The six entries of the table above were also checked directly. Only Python integers were used. These are bounded, same-owner controls of the explicit quotient, not independent or formal verification of the all-n theorem.

**First remaining gap for |P|=100:** lift the saturated mod-1650 representation to an actual direct tiling at the full 2^K·5^v·R modulus while retaining the actual head/tail anchors, or prove that every such lift fails. The quotient alone cannot establish failure: the displayed twofold cover realizes every quotient condition proved here. For larger 5-powers, (8) gives 25-element blocks but does not control residues above mod 25; in particular no nonvanishing claim is made at roots of order 125 or above. Multiple distinct odd head primes and all other odd-head possibilities are outside this packet.

A complete review must independently check the exact odd-difference rule, uniformity mod 33, all arbitrary-f nonvanishing cases and the cyclotomic field-degree import, both Fourier inversions, the signed-count dichotomy and the 2w-versus-w folded count, then the quotient multiplicity table. Historical process and source qualifications are not a certificate of independent provenance. No earlier theorem's review verdict is transferred.

**END OF ARBITRARY-TAIL FIVE-POWER SATURATION CANDIDATE.**
