# Shor completion: at orders 2310·2^k, 7 must divide the head border

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Thu Oct 29 07:48:08 PDT 2026**.

**Status: UNREVIEWED CANDIDATE.** The written argument covers every k. It rests on the named imports listed below, the deep one being Łaba–Londner Corollary 6.2 (T2). The finite residue tables and one arc-consistency fixpoint were checked with exact integers in the owner's eval kernel (§7). This is a **necessary condition, not an order exclusion**. It is not an adoption, formal proof, independent-family review or novelty clearance. The original unrestricted finite UD factor-completion problem remains OPEN.

## 0. Provenance and non-imports

This packet is same-author work. It applies the method of the separately frozen, unreviewed candidate `frontier-20261029-165-family-all-q-anchored-border-no-go-v1.md` (SHA256 `20169ac9…`) to n=2310·2^k. **That candidate is not a premise**: every mathematical step specific to this order family is restated here, and the only text reused from it is the order-independent border reconstruction named in §2. The owner's same-author fibre-exposure statement quoted in its §0 applies here as well.

**Not premises:**

- the 2310-family odd-tail candidates `b618…` (joint-prime/matching), `fce2…` (Q105/231/385) and `33c6…` (Q165);
- `frontier-20261028-2310-family-q55-obstruction-v1.md` and the pending Q55 theorem f128;
- all fibre packets;
- every order-specific branch packet.

The e=385 and e=231 tables below coincide in substance with `fce2…` §§3–4. They are re-derived here, and they need only that each residue class be nonempty, so they hold for either parity of |Q|. The e=105 case uses a different (Fourier) argument from `fce2…`'s 2-adic step.

## 1. Statement

> **Theorem (candidate).** Let k≥0 and n=2310·2^k. Suppose P⊕Q=Z_n is a direct tiling with A={0,3,8,11}⊆P and Y={0,1,7,13,14}⊆Q. Then 7 divides |P|. More precisely, the odd part d of |P| is one of 7, 21, 35 or 77; equivalently, the odd part e of |Q| is one of 165, 55, 33 or 15.

> **Corollary (candidate).** The same conclusion holds for the actual multi-b border factors P, Q of any finite UD factor-complete extension of the literal Shor code whose pure-a order is 2310·2^k.

## 2. Imports and parity rules

1. **Actual-word border theorem.** This is Restivo–Salemi–Sportelli, as stated in Cordero, [arXiv:2301.13566v1, p. 3, Thm 1.1](https://arxiv.org/pdf/2301.13566v1); the classical theorem is the import. An order-independent UD/factor-completeness reconstruction of directness and coverage is written out in §2 of the 165-family candidate and applies verbatim with n=2310·2^k; it is cited only as an aid.
2. **Sands' divisor exclusion**, [Łaba–Londner, arXiv:2106.14042v3, p. 10, Thm 2.5](https://arxiv.org/pdf/2106.14042v3).
3. **T2**, through [LL p. 26, Corollary 6.2](https://arxiv.org/pdf/2106.14042v3), with T2 as defined in [LL p. 3, Thm 1.1](https://arxiv.org/pdf/2106.14042v3). Here n = 2^(k+1)·3·5·7·11. Each odd prime appears to the first power, so only 2 can divide both |P| and |Q|, and the corollary applies to both factors.

**Lemma 1′.** If u is odd, then gcd(u,n) = gcd(u,1155), the product of those primes among 3, 5, 7, 11 that divide u.

- Old head differences 3−0, 8−3 and 11−0 give the odd P-gcds 3, 5 and 11.
- Old tail differences 1−0 and 7−0 give the odd Q-gcds 1 and 7.

With Sands this yields:

- **(SQ′)** For opposite-parity q≠q′ in Q, the set of primes from {3,5,7,11} dividing q−q′ is not {3}, {5} or {11}.
- **(SP′)** For opposite-parity p≠p′ in P, that prime set is neither ∅ nor {7}. In particular, at least one of 3, 5, 11 divides p−p′.

**Lemma 2′ (uniformity).** Write |P| = d·2^a and |Q| = e·2^b with d and e odd. Then de = 1155. By the tiling identity, Φ_p divides the mask of the factor whose cardinality the prime p divides. T2 then gives (X^d−1)/(X−1) | P(X) and (X^e−1)/(X−1) | Q(X). So every class mod d holds exactly 2^a elements of P, and every class mod e holds exactly 2^b ≥ 1 elements of Q. The proof is word-for-word that of Lemma 2 in the 165-family candidate, with 165 replaced by 1155.

## 3. At most one of 3, 5, 11 divides d

**Lemma 3′.** P has no element in the classes 4 (mod 15), 1 (mod 33) or 2 (mod 55).

*Proof.* Compare x with its two opposite-parity old heads: 0 and 8 if x is odd, 3 and 11 if x is even. Neither difference is divisible by either of the two primes that the class determines. These differences are:

- for 4 (mod 15): x−0 ≡ 4, x−8 ≡ 11, x−3 ≡ 1, x−11 ≡ 8 (mod 15);
- for 1 (mod 33): x−0 ≡ 1, x−8 ≡ 26, x−3 ≡ 31, x−11 ≡ 23 (mod 33);
- for 2 (mod 55): x−0 ≡ 2, x−8 ≡ 49, x−3 ≡ 54, x−11 ≡ 46 (mod 55).

The prime 7 alone cannot satisfy (SP′). So the remaining prime of {3,5,11} must divide both differences. That is impossible, because the two compared heads differ modulo it: 0≢8 and 3≢11 modulo 11, modulo 5 and modulo 3. ∎

So, by Lemma 2′, d ∈ {1,3,5,11} ∪ {7,21,35,77}. The four cases d∈{1,3,5,11} are now excluded.

## 4. The cases d=1, 3, 5

For a fixed e, the class r = x mod e of an element x∈Q fixes x modulo the *fixed* primes, which are the primes dividing e. For d=3 or 5 there is one *free* prime f. Let x, x′∈Q have opposite parity and lie in distinct classes, and let K be the set of fixed primes dividing x−x′. Then (SQ′) gives:

    K=∅ ⇒ x ≢ x′ (mod f);   K={3},{5} or {11} ⇒ x ≡ x′ (mod f);   otherwise (K={7} or |K|≥2) no constraint.

Brackets [·] below give class differences. The even old tails are 0 and 14; the odd ones are 1, 7 and 13.

**d=1, e=1155.** Q has an element x in class 827 (mod 1155), where 827 ≡ 2 (mod 165) and 827 ≡ 1 (mod 7).

- If x is even: x−13 ≡ 814 (mod 1155) is divisible by 11 alone.
- If x is odd: x−14 ≡ 813 is divisible by 3 alone.

Either violates (SQ′).

**d=3, e=385, f=3.** The fixed primes are 5, 7 and 11.

- **Class 3**, i.e. (r_5,r_7,r_11) = (3,3,3).
  - Even is impossible: against 1 [2], K=∅, so x≢1 (mod 3); against 13 [−10], K={5}, so x≡1.
  - Odd: against 0 [3], K=∅, so x≢0; against 14 [−11], K={11}, so x≡2.
- **Class 24**, i.e. (4,3,2).
  - Even is impossible: against 1 [23], K=∅, so x≢1; against 13 [11], K={11}, so x≡1.
  - Odd: against 0 [24], K=∅, so x≢0; against 14 [10], K={5}, so x≡2.
- **Class 25**, i.e. (0,4,3).
  - Odd is impossible: against 0 [25], K={5}, so x≡0; against 14 [11], K={11}, so x≡2.
  - Even: against 1, 7, 13 [24, 18, 12], K=∅ each time, so x≢1.

Then x_25 against x_3 [22, K={11}] forces x_25 ≡ 2 (mod 3), while x_25 against x_24 [1, K=∅] forces x_25 ≢ 2. Contradiction.

**d=5, e=231, f=5.** The fixed primes are 3, 7 and 11.

- **Class 22**, i.e. (r_3,r_7,r_11) = (1,1,0).
  - Even is impossible: against 7 [15, K={3}], x≡2 (mod 5); against 13 [9, K={3}], x≡3. Against 1 [21, K={3,7}] there is no constraint.
  - Odd: against 0 [22, K={11}], x≡0; against 14 [8, K=∅], x≢4.
- **Class 25**, i.e. (1,4,3).
  - Even is impossible: against 1 [24, K={3}], x≡1; against 7 [18, K={3}], x≡2.
  - Odd: against 0 [25, K=∅], x≢0; against 14 [11, K={11}], x≡4.
- **Class 26**, i.e. (2,5,4).
  - Even: against 1, 7, 13 [25, 19, 13], K=∅ each time, so x ∉ {1,2,3}.
  - Odd: against 0 [26, K=∅], x≢0; against 14 [12, K={3}], x≡4.
- **Class 36**, i.e. (0,1,3).
  - Odd is impossible: against 0 [36, K={3}], x≡0; against 14 [22, K={11}], x≡4.
  - Even: against 7 [29] and 13 [23], K=∅, so x ∉ {2,3}. Against 1 [35, K={7}] there is no constraint.

The chain:

1. Suppose x_26 is even.
   - If x_26 ≡ 0, then against x_22 [4, K=∅] it must differ from x_22 ≡ 0, which is false.
   - If x_26 ≡ 4, then against x_25 [1, K=∅] it must differ from x_25 ≡ 4, which is false.

   So x_26 is odd with x_26 ≡ 4.
2. x_36 is even. Against x_25 [11, K={11}], x_36 ≡ 4. Against x_26 [10, K=∅], x_36 ≢ 4.

Contradiction.

## 5. The case d=11 (e=105)

**Lemma 4′ (finite fixpoint).** Every x∈Q satisfies two conditions: x is odd iff x ≡ 1 (mod 3), and x ≡ g(x mod 5) (mod 11), where g = (0,1,7,2,3).

*Proof (WRITTEN-checked-in-kernel).* By Lemma 2′ every class r mod 105 is nonempty. Assign to each element its type, namely its residue mod 2310, which records parity and residues mod 3, 5, 7, 11. For each class, the initial domain is the set of types in that class that satisfy (SQ′) against all five old tails.

Arc consistency is sound: remove a type from class r if it is (SQ′)-incompatible with every remaining type of some other class s. Class s is nonempty, and every element of Q must be compatible with every element of s.

The exact fixpoint computation, starting from the initial domain-size histogram reported in §7, ends with every one of the 105 domains a singleton. Each singleton satisfies the stated formula. That formula depends only on r mod 15. The 165-family candidate's hand proof of the 15-class analogue is not reused, because here sharing r mod 7 can cancel constraints. ∎

**Lemma 5′.** For u∈Z_5, the 21 classes mod 105 over u comprise 7 classes with each value of r mod 3. Hence the number of elements of Q congruent to z (mod 110) is:

- 7·2^(b+1) if z is even and z mod 55 ∈ {0,1,7,13,14};
- 7·2^b if z is odd and z mod 55 ∈ {0,1,7,13,14};
- 0 otherwise.

So for ξ^110 = 1,

    Q(ξ) = 7·2^b · (2+ξ^55) · Y(ξ^56),    Y(X) = 1+X+X^7+X^13+X^14.

If 11 divides ord ξ, this is nonzero. The reason: Y ≠ 0 has degree 14 < 40 = deg Φ_55, and 1+X+X^2+X^3+X^7 has degree 7 < 10 = deg Φ_11. ∎

**Lemma 6′ and contradiction.**

1. The orders 11, 22, 55 and 110 all divide n. At a primitive root of any of these orders, Q ≠ 0 while P·Q = 0, so P vanishes there.
2. Hence Φ_11 Φ_22 Φ_55 Φ_110 = 1+X^10+…+X^100 divides P(X). So the count of P-elements in a class mod 110 depends only on the class mod 10.
3. Since 11∈P and 11 ≡ 1 (mod 10), some x∈P satisfies x ≡ 1 (mod 110).
4. For this x, the differences x−0 ≡ 1 and x−8 ≡ −7 (mod 110) are divisible by neither 5 nor 11.
5. By (SP′), 3 divides both, because 7 alone is forbidden. Then x ≡ 0 and x ≡ 2 (mod 3), a contradiction. ∎

This proves the Theorem.

## 6. Exact remaining gap

The cases d ∈ {7,21,35,77} remain, equivalently e ∈ {165,55,33,15}. In each, 7 is a free prime on the Q side.

The owner also ran exploratory kernel computations. They are not in the pinned checker and are not evidence of feasibility. Unpinned type-level arc consistency found no contradiction:

- on the Q side for e ∈ {165,55,33,15}: for e=165, 105 of the 165 classes end with a determined parity and 70 with singleton domains;
- on the P side for d ∈ {77,35,21,7}.

The Fourier transfer of §5 needs a structure lemma that those fixpoints do not supply. **First unproved step:** exclude these four (d,e) pairs for every parity of |Q|. A natural route couples P and Q 2-adically, generalizing the odd-|Q| argument of `33c6…` to arbitrary 2-power allocations. That route is not attempted here.

## 7. Finite checks

Checker: `frontier-20261029-2310-family-all-q-seven-check.py`, SHA256 `2d92691bf1e6f53a431c41edc1a4de4e5a1b6dfe1fb6a2f5a7ebafff225c5b79`, 166 LF / 5,665 bytes. Those exact bytes were executed in the owner's eval kernel before 07:48:08 PDT on 2026-10-29, in 0.14 s, with output `PASS`. It uses only integer, gcd and polynomial arithmetic.

It checks:

- Lemma 3′ over all residues mod 2310.
- That class 827 (mod 1155) has an empty tail domain.
- The e=385 and e=231 state tables, and that they admit no compatible triple or 4-tuple.
- The 105-class arc-consistency fixpoint. The initial domain-size histogram is {1:12, 2:32, 8:8, 9:18, 10:8, 11:3, 12:6, 18:8, 19:4, 20:6}. The final domains are all singletons matching the formula, they contain Y, and they are pairwise compatible.
- That the fold mod 110 equals 7 times the stated weights, with nonzero remainders mod Φ_11, Φ_22, Φ_55 and Φ_110.
- The identity Φ_11 Φ_22 Φ_55 Φ_110 = 1+X^10+…+X^100.
- That all 21 types ≡ 1 (mod 110) fail (SP′) against 0 or against 8.
- Bounded actual-gcd diagnostics for n = 2310, 4620, 9240, 18480. These give P-screen sizes 248, 528, 1224, 2448 and Q-screen sizes 409, 1108, 2636, 5944, and confirm that the actual screens respect every type domain used.

It does not verify the imports or the all-k written steps.

## 8. Limits and review gates

**Limits.** The candidate is conditional on LL Corollary 6.2 (used for uniformity), on Sands' theorem and on the border theorem. It excludes no order. The four cases of §6 and the unrestricted original problem remain OPEN.

**Reviewers should check:**

1. the T2 hypothesis for n = 2^(k+1)·1155;
2. (SQ′) and (SP′);
3. every table row and chain step in §4;
4. the soundness of arc consistency and the reported fixpoint;
5. Lemmas 5′ and 6′;
6. that none of the §0 non-premises is used.

**END OF 2310·2^k SEVEN-DIVIDES-HEAD CANDIDATE.**
