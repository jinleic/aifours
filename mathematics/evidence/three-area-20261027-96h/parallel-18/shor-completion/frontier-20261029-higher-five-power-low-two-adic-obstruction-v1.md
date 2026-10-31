# Higher powers of 5: no head cardinality 5^e or 2·5^e

Owner **MathShor-2**, math-5. Native `/bin/date` immediately before writing: **Thu Oct 29 14:01:26 PDT 2026**.

**WRITTEN UNREVIEWED CANDIDATE, conditional on the named Łaba–Londner T2 import.** This is a distinct remaining head family, with e≥3; it does not expand the frozen |P|=100 reviews f232/f233 or import their result. The original unrestricted Shor completion problem remains OPEN.

## 0. Provenance and inputs

Main reported the |P|=100 packet `9ed4749c…` frozen for two hostile reviews and directed further primary work to a distinct remaining head family, not more |P|=100 versions. The candidate here concerns arbitrary n and |P|=5^e or 2·5^e for e≥3, and a necessary 2-adic spectrum for |P|=4·5^e. It is not a claim that the |P|=100 candidate is accepted.

This is same-author work after the earlier fibre/cofactor exposure, f217/f220 packets and the |P|=100 derivation. The owner has seen those related sources; there is no disjoint-exposure, blind-review, or clean-cognition claim. The arbitrary-tail parity graph, dilation, and fibre extraction are reconstructed below, rather than importing any author/reviewer result. No previous verdict, f217 special tail, Q55 theorem, selected solver result, or HELD/ZERO/NONINPUT body is a premise. Previous arithmetic/cadence disclosures and all process records remain in force.

The classical import needed for the cyclic theorem is Łaba–Londner [arXiv:2106.14042v3, p. 26, Corollary 6.2](https://arxiv.org/pdf/2106.14042v3): if at most two distinct primes divide both cardinalities of a cyclic tiling, both factors satisfy Coven–Meyerowitz (T2). T2 combines owned prime-power cyclotomic divisors of distinct primes; the statement appears on p. 3 of the same source. The corollary's ancestry includes the Coven–Meyerowitz two-prime result, Tijdeman and subgroup reduction. These are named imports, not independently re-proved here. Ordinary cyclotomic irreducibility and Φ_(p^j)(1)=p are also named standard algebraic inputs. The code-to-border caller is separately imported in §1.

## 1. Exact theorem and literal original-code caller

Let A={0,3,8,11}, Y={0,1,7,13,14}. An anchored tiling means P,Q⊆Z_n with A⊆P, Y⊆Q and P⊕Q=Z_n.

> **Theorem (candidate).** For every n>14 and e≥3, no anchored tiling has |P|=5^e or |P|=2·5^e.

> **Additional necessary structure.** If e≥3 and an anchored tiling has |P|=4·5^e, write K=v_2(n). Then K≥4, and the only prime-power cyclotomic polynomials of 2-power order dividing P are Φ_2 and Φ_16. In particular the theorem does not exclude |P|=4·5^e, or claim any such tiling exists.

This is an all-n head-cardinality statement, not an order floor, original-problem solution, or statement about e=2,|P|=100. It makes no assertion for head parts involving another odd prime.

For the literal code

    S=b{1,a,a^7,a^13,a^14} ∪ {a^3,a^8}b{1,a^2,a^4,a^6} ∪ a^11b{1,a,a^2},

the actual-word border theorem of Restivo–Salemi–Sportelli, stated in Cordero [arXiv:2301.13566v1, p. 3, Thm 1.1](https://arxiv.org/pdf/2301.13566v1), supplies the same-code anchored P,Q for any finite UD factor-complete extension with actual pure-a atom a^n. This is a named caller import and no converse is claimed.

## 2. Elementary dilation, gcd exclusion and parameters

If X⊕Z=Z_n and gcd(t,|X|)=1, then tX⊕Z=Z_n. For a prime ℓ∤|X|, work in F_ℓ[Z_n] and write x,z for the characteristic sums and G for the sum of all group elements. Freshman's dream, the tiling xz=G and xG=|X|G give x^ℓz=|X|^(ℓ−1)G=G mod ℓ. The corresponding integer coefficients are nonnegative, all 1 mod ℓ, and sum to n; hence all are exactly 1. This proves both the ℓ-dilation and injectivity. Iterate over prime factors of t.

Two nonzero differences d_X∈X−X,d_Z∈Z−Z in a direct tiling cannot have the same gcd with n. If they did, CRT would lift d_Z/g divided by d_X/g modulo n/g to a unit u mod n, where g is the common gcd. Then uX⊕Z tiles by the dilation lemma, but ud_X≡d_Z gives two representations. These facts are reconstructed here, not transferred from f219.

For an anchored tiling, 330|n: otherwise the tail difference 1 has common gcd 1 with head difference 8 or one of 3,5,11. Also each of 3,5,11 divides |Q|; if a prime ℓ were absent from |Q|, dilating Q by ℓ would make ℓ(1−0) collide with the corresponding actual head difference ℓ.

For |P|=5^e2^a, write

    n=2^K·5^v·R,     |Q|=2^(K−a)·5^(v−e)·R,
    K≥1, v≥e+1,       R odd, gcd(R,5)=1, 33|R.                (2.1)

RP⊕Q tiles. Its coset decomposition shows that Q has equal positive cardinality in every class mod R, and consequently equal positive cardinality w=|Q|/33 in every class mod33.

**Odd tail rule.** If q−q′ is odd and is divisible by any of 3,5,11, then 25|(q−q′). If its 5-valuation is exactly1, let g=gcd(q−q′,n) and use the admissible multiplier t=g/5 on head difference5. If 5∤(q−q′) but 3 or11 divides it, use t=g/3 or g/11 on the corresponding head difference. In each case t is odd and 5-free, so coprime to |P|, and gives an equal-gcd collision. Thus a difference divisible by any of these primes must instead be divisible by25.

## 3. Every arbitrary tail's parity and mod-25 graph

An even Q-element cannot be 1 mod3: comparing it to odd anchors 1,7,13 would force three different mod25 values. All classes mod33 are nonempty.

- Every element in class3 mod33 is even. If odd, it would equal both anchor0 (same mod3) and anchor14 (same mod11) mod25. Every element in class25 is odd and equals14 mod25 by comparison with anchor14. Comparing class3 with class25 forces the even class3 elements to equal14 mod25.
- Every element in class11 is even. If odd, comparison with anchors14 (same mod3) and0 (same mod11) would force two different residues. Class22 is odd and equals0 mod25 by comparison with anchor0; it forces the even class11 elements to equal0 mod25.
- An odd tail of residue0 mod3 would compare with even anchor0 and an even class3 element, forcing 0 and14 mod25; an odd tail of residue2 would compare with even anchor14 and an even class11 element, forcing14 and0. Both are impossible.

Thus

    q odd  ⇔  q≡1 mod3.                                        (3.1)

For each j mod11, there are both an odd and an even tail with that j, by the nonempty mod33 classes. The odd tail rule implies every tail of that j shares a fixed mod25 residue f(j). The anchors yield

    f(0)=0, f(1)=1, f(2)=13, f(3)=14, f(7)=7.                 (3.2)

If two f-values agree mod5 they agree mod25: compare an odd tail in the first mod11 class with an even tail in the second. Since Y occupies every mod5 residue once, each f(j) is one of Y. The six unspecified f-values remain arbitrary.

The equal mod33 counts and (3.1) give Q(−1)=11w≠0. Since n is even, the tiling mask identity yields P(−1)=0 and therefore Φ2 divides P. This alone rules out a=0.

## 4. Ownership of 2-powers and Q-fibre extraction

P and Q satisfy T2 by the named LL Corollary: only 2 and5 divide |P|, so no other prime can be shared. For 1≤i≤K, Φ_(2^i) divides at least one mask. Evaluating distinct prime-power factors at 1 shows P owns at most a and Q at most K−a of these K factors. Hence every factor is owned exactly once and P owns exactly a. In particular:

- if a=1, P owns only Φ2 and Q owns Φ_(2^i) for every 2≤i≤K;
- if a=2, P owns Φ2 and one further Φ_(2^s), 2≤s≤K, while Q owns all other 2-power factors.

For any prime power ℓ^j|R, Q owns Φ_(ℓ^j): otherwise ℓ would divide P(1)=5^e2^a. If Q owns Φ_(2^i), T2 therefore gives Φ_(2^i d)|Q for every divisor d|R. Since R is odd,

    Φ_(2^i)(X^R)=∏_(d|R)Φ_(2^i d)(X).                           (4.1)

Decompose Q(X)=Σ_(r modR)X^rF_r(X^R). Divisibility by the left side of (4.1), followed by uniqueness of residue-basis decomposition, yields Φ_(2^i)|F_r for every r. R is odd, so the mask of the actual Q_r also vanishes at primitive 2^i-th roots.

Thus Q-owned Φ4, Φ8 or Φ16 gives the following exact coefficient property in **every** actual Q_r: after folding mod4,8 or16, the counts in the two halves of each lower-bit class are equal. This follows from Φ_(2^i)=1+X^(2^(i−1)). Every Q_r has fixed parity by (3.1).

## 5. A universal high-bit collision rule

Let q,q′∈Q and g=gcd(q−q′,n). If 5∤(q−q′) and the 2-part of g is exactly8, then no anchored tiling exists: t=g/8 is odd and 5-free, hence coprime to |P|; tP⊕Q tiles, and the actual head difference 8 scaled by t has gcd g, colliding with q−q′.

For K=3, the required 2-part condition is q≡q′ mod8. For K≥4, it is q−q′≡8 mod16. The actual Q_r containing 13 has mod25 value f(2)=13, and the one containing 7 has mod25 value f(7)=7; these differ mod5 from anchors 1 and13 as needed below.

## 6. The cases K≤2, K=3 and K≥4

**K≤2:** gcd(3·8,n)=gcd(13−1,n)=3·2^K, because 3 divides n and both differences contain exactly one factor of 3. Multiplication of P by3 is allowed, and the head difference 3·8 collides with the actual tail difference 13−1. Thus K=1 and K=2 are impossible, regardless of a.

**K=3:**

- If Q owns Φ8, the Q_r containing 13≡5 mod8 also contains an element congruent1 mod8. It remains 13 mod25. Its difference from anchor1 is divisible by8 and not by5, contradicting §5.
- If a=1, Q necessarily owns Φ8, so a=1 is impossible.
- If a=2, the previous bullet forces P to own Φ8 in addition to Φ2. Then Q owns Φ4. The Q_r containing 7≡3 mod4 contains an element congruent1 mod4, hence congruent1 or5 mod8. It remains 7 mod25. Comparing with anchor1 or13 respectively gives a difference divisible by8 and not5, contradicting §5. Thus a=2 is also impossible at K=3.

**K≥4:**

- Q cannot own both Φ8 and Φ16. In the Q_r containing 13≡5 mod8, Φ8 gives an element congruent1 mod8, and Φ16 gives one congruent9 mod16. Its mod25 value is13. The difference from anchor1 is 8 mod16 and not divisible by5, contradicting §5.
- If a=1, P owns only Φ2, so Q owns both Φ8 and Φ16: impossible. Combined with a=0 and K≤2,3, this proves the Theorem.
- If a=2, P owns Φ2 and one further Φ_(2^s). The previous bullet forces s∈{3,4}. If s=3, Q owns Φ4 and Φ16. The Q_r of anchor7 has a tail congruent1 mod4. If it is 1 mod8, Φ16 supplies one congruent9 mod16, contradicting §5 against anchor1. If it is 5 mod8, Φ16 supplies one congruent5 mod16, contradicting §5 against anchor13≡13 mod16. In both cases its mod25 value is7, distinct mod5 from the compared anchor. Hence s≠3, leaving s=4.

We have proved the additional necessary structure: for a=2, K≥4 and P owns exactly Φ2,Φ16 among the 2-power factors. ∎

## 7. Exact residual and checks

For e≥3, the remaining |P|=4·5^e branch is **not** excluded by this packet. Its low 2-power allocation is constrained as above, but each parity/mod11/mod25 head bucket may have multiplicity larger than one. The four-row saturation used in a different |P|=100 candidate is not available merely from the present hypothesis. Higher 5-adic ownership and the simultaneous full head anchors still need a genuine high-modulus argument.

For context only, the owner constructed unanchored cyclic tiling relaxations at (e,K)=(3,4), with |P|=2000,|Q|=165 and Y⊆Q, in which Q owns Φ_(5^3) or Φ_(5^4), respectively, while P⊆33Z_n and misses head anchors3,8,11. The two exact finite sumsets both covered all 330000 residues in the owner's kernel. They are **not** premises or anchored-completion witnesses; they show why an unproved rule forcing a single high 5-adic owner would be unsafe.

The owner also checked the coefficient transport with exact integers: for all c1,c5 in {0,1,2,3,4} with c1=c5>0, c1>0 (4 cases); and for all c1,c5,c9,c13 in {0,1,2,3} satisfying c1=c9, c5=c13, c1+c9=c5+c13 and c13>0, c9>0 (3 cases). Bounded gcd controls for K=1,…,6, v=4,5,7 and R∈{33,99,363} matched the stated 2-adic cases, including the 18 K≤2 equal-gcd checks. These finite controls are not a proof of the all-n theorem and are not independent-model, human, formal/kernel or novelty verification.

A fresh hostile review must check the arbitrary-Q parity graph, coprime-dilation/gcd reconstruction, prime-power ownership counting, LL Cor6.2/T2 with arbitrary R, residue-basis extraction into each fibre, all K/s cases, and the exact anchor comparisons. It must retain all source and same-author qualifications. No review result is inherited from f232/f233, f220 or f219.

**END OF HIGHER-FIVE-POWER LOW-TWO-ADIC OBSTRUCTION.**
