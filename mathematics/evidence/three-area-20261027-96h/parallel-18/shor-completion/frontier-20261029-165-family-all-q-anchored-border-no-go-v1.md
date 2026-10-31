# Shor completion: no anchored border tiling at any order 165·2^t

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Thu Oct 29 07:15:12 PDT 2026**.

**Status: HIGH-CONSEQUENCE UNREVIEWED CANDIDATE.** The argument for every t is WRITTEN. It has one explicitly named deep import, Łaba–Londner Corollary 6.2 (the Coven–Meyerowitz T2 condition), plus two classical imports: the actual-word border theorem and Sands' divisor exclusion. The finite residue tables were checked with exact integers in the owner's eval kernel (§8). This is not an adoption, formal proof, human review, independent-model-family review or novelty clearance. **The original unrestricted finite UD factor-completion problem remains OPEN.**

## 0. Provenance and non-imports

Main's decision of 2026-10-29 authorized writing and freezing this route as a NEW candidate, on two conditions. The same-author exposure must be disclosed, and neither the pending Q55 theorem nor any fibre packet may be a premise. That decision message also records a parent allocation-latency MAJOR (`20d75344…`). A later Main message, received before this packet was written, reported the conditional parent disposition of f157 (order-2640 even tail) and repeated the instruction not to import the unadopted Q55 claim.

The owner's own provenance statement was sent to Main on 2026-10-29, shortly after 00:02:01 PDT. Verbatim:

> "Provenance correction to my pending freeze question: by 'independent' I meant no dependency on the pending Q55 theorem or a fibre packet as a mathematical premise. It is SAME-AUTHOR work, not a disjoint exposure: I had read and considered my prior unreviewed fibre-related sources before developing this route."

History. The owner first worked this route out in the eval kernel late on 2026-10-28 PDT and kept it there, unwritten and noninput, while Main's decision was pending (`owner-20261029-unfrozen-math-frontier-v1.json`). That kernel has since died, and nothing from it is used. The written argument below was re-derived. Every finite fact was recomputed in a fresh kernel by the pinned checker of §8.

**Not premises.** Each item below is a separate unreviewed (or only conditionally dispositioned) same-author candidate:

- `frontier-20261028-universal-55-tail-obstruction-v1.md`, the pending Q55 theorem (f128);
- `frontier-20261028-odd-55-cofactor-classification-v1.md`;
- `frontier-20261028-even-tail-unified-fibres-v1.md` and every other `*fibre*` packet;
- `frontier-20261028-p22-cyclotomic-structure-v1.md` and `frontier-20261028-three-times-power-two-parity-v1.md`;
- every order-660, 1320 or 2640 branch packet, including `frontier-20261028-2640-even-tail-self-contained-review-v1.md` (f157) and its parent disposition;
- the 2310-family and 165-family odd-tail packets (`b618…`, `fce2…`, `33c6…`, `fe70…`).

Wherever those packets prove overlapping statements, this packet re-derives what it needs from the three named imports alone. In particular, case d=3 in §6 treats the |Q|=55 situation independently. That treatment is conditional on T2. It neither uses nor validates f128's argument.

## 1. Statement

> **Theorem (candidate).** Let t≥1 and n=165·2^t. There are no subsets P,Q ⊆ Z_n such that every residue of Z_n is uniquely p+q with p∈P, q∈Q, and such that A={0,3,8,11}⊆P and Y={0,1,7,13,14}⊆Q.

No restriction is placed on |P|, |Q| or the parity of either cardinality.

> **Corollary (candidate).** No finite uniquely decipherable, factor-complete extension of the literal Shor code has actual pure-a atom a^n with n=165·2^t, t≥1.

So the orders 330, 660, 1320, 2640, 5280, … are all excluded, for either parity of the tail border. At order 2640 this covers the odd-tail case, which the dispositioned f157 leaves open. It does so by an argument that does not use f157.

Conditional scope: §2 (actual border), §3 (Sands) and §4 (LL Corollary 6.2). The remaining steps are written and elementary. Orders not of the form 165·2^t, the case t=0, and the unrestricted original question are not addressed.

## 2. Actual border factorization (classical import, reconstructed)

Let `1` be the empty word. The literal code is

    S = b{1,a,a^7,a^13,a^14} ∪ {a^3,a^8} b {1,a^2,a^4,a^6} ∪ a^11 b {1,a,a^2}.

Assume, for contradiction, that D is a finite code with the following properties:

- D contains S;
- D is UD: concatenation of atom sequences is injective;
- D is factor-complete: every word over {a,b} is a factor of a word in D*;
- the unique actual pure-a atom of D is a^n.

**Pure-a and pure-b atoms.** Let L be the maximum atom length. Completeness embeds a^(2L+1) in a D-factorization, so some pure-a atom exists. Two distinct ones a^u, a^v would give the different lists (a^u,a^v) and (a^v,a^u) for the same word. Since b∈S, UD forbids every b^k with k≥2: (b^k) and k copies of (b) would be different factorizations.

**Borders.** Define residues mod n from actual atoms with any positive number of b's:

    P = {i mod n : a^i b^k ∈ D, k≥1},     Q = {j mod n : b^l a^j ∈ D, l≥1}.

Then A⊆P and Y⊆Q. The classical statement is the Restivo–Salemi–Sportelli theorem, as given in Cordero, [arXiv:2301.13566v1, p. 3, Theorem 1.1](https://arxiv.org/pdf/2301.13566v1). The reconstruction below uses only UD and factor-completeness.

**Directness.** Take actual atoms u_t = a^(i_t) b^(k_t) and v_t = b^(l_t) a^(j_t), for t=1,2, with i_1+j_1 ≡ i_2+j_2 (mod n). Choose G in that common class, larger than both i_t+j_t, and choose H,K large. Each list

    (b)^(H−l_t), v_t, (a^n)^((G−i_t−j_t)/n), u_t, (b)^(K−k_t)

spells b^H a^G b^K. Any border atom without an a is b. Otherwise the left border atom starts with b and ends with a, and the right one starts with a and ends with b. The positive central a-run therefore identifies both border atoms. So distinct residue pairs give distinct lists, contrary to UD.

**Coverage.** Embed b^L a^g b^L, with g>L in a prescribed class mod n. The atom containing the last left b starts inside the left guard and cannot reach the right guard, so it is some b^l a^j. Symmetrically, the atom containing the first right b is some a^i b^k. Every atom between them is a^n. Hence g ≡ i+j (mod n).

So P⊕Q = Z_n and |P||Q| = n. Since n≥330, the anchors are distinct residues.

## 3. Sands' rule in parity form

**Sands' divisor exclusion.** No nonzero P-difference and nonzero Q-difference have the same gcd with n. See Łaba–Londner, [arXiv:2106.14042v3, p. 10, Theorem 2.5](https://arxiv.org/pdf/2106.14042v3). Brief reason: if gcd(p−p′,n) = gcd(q−q′,n), a unit w mod n has w(p−p′) ≡ q−q′. The set wP still tiles with Q, because ζ ↦ ζ^w permutes the primitive m-th roots for every m|n. Then wp+q′ ≡ wp′+q gives a collision.

**Lemma 1.** If u is odd and n=165·2^t, then gcd(u,n) = gcd(u,165), the product of those primes among 3, 5, 11 that divide u.

The old heads give the P-differences gcd(3−0,n)=3, gcd(8−3,n)=5 and gcd(11−0,n)=11. The old tails give the Q-difference gcd(1−0,n)=1. With Lemma 1 this yields:

- **(SQ)** If q≠q′ in Q have opposite parity, the number of primes from {3,5,11} dividing q−q′ is not exactly one.
- **(SP)** If p≠p′ in P have opposite parity, at least one of 3, 5, 11 divides p−p′.

These are the only consequences of Sands' theorem used. They depend only on residues mod 330 and are the same for every t≥1.

## 4. The T2 import and uniformity

Masks are P(X) = Σ_{p∈P} X^p with representatives in [0,n). The tiling identity is

    P(X)Q(X) ≡ 1+X+…+X^(n−1)   (mod X^n−1).

**Import (T2).** Let S_F be the set of prime powers s with Φ_s | F(X). The condition (T2) states that whenever s_1,…,s_k ∈ S_F are powers of different primes, Φ_{s_1…s_k} divides F(X) ([LL, p. 3, Theorem 1.1](https://arxiv.org/pdf/2106.14042v3)).

[LL, p. 26, Corollary 6.2](https://arxiv.org/pdf/2106.14042v3): let F⊕B = Z_M with M = p_1^{n_1}…p_K^{n_K}. If, for each i≥3, p_i divides at most one of |F| and |B|, then both F and B satisfy (T2). The paper notes that this holds for instance when n_i=1 for all i∉{1,2}.

Here M = n = 2^t·3·5·11. Take p_1=2, p_2=3, p_3=5, p_4=11. Then n_3 = n_4 = 1. More strongly, since |P||Q| = n, each of 3, 5, 11 divides exactly one of |P| and |Q|. **So P and Q both satisfy (T2).** This is the only deep import.

**Lemma 2.** Write |P| = d·2^a and |Q| = e·2^b with d and e odd. Then de = 165 and gcd(d,e) = 1.

- (a) For each p∈{3,5,11}, Φ_p divides the mask of the factor whose cardinality p divides.
- (b) (X^d−1)/(X−1) divides P(X), and (X^e−1)/(X−1) divides Q(X). So every residue class mod d contains exactly 2^a elements of P, and every class mod e contains exactly 2^b ≥ 1 elements of Q.

*Proof.* (a) Since p|n, Φ_p divides X^n−1 and 1+…+X^(n−1), so it divides P(X)Q(X). By irreducibility, Φ_p divides P(X) or Q(X). If Φ_p divides Q(X), then Q = Φ_p·R in Z[X], because Φ_p is monic. Hence p = Φ_p(1) divides Q(1) = |Q|. The same holds for P.

(b) By (a), every prime h|e lies in S_Q. By T2, Φ_h | Q(X) for every h>1 dividing the squarefree number e. The product of these Φ_h is (X^e−1)/(X−1). Reduce Q modulo X^e−1. The result has degree <e and is divisible by 1+…+X^(e−1), so it is a constant multiple of it. The constant is |Q|/e. The same argument applies to P. ∎

## 5. The odd part of |P| is 1, 3, 5 or 11

**Lemma 3.** P has no element in the classes 4 (mod 15), 1 (mod 33) or 2 (mod 55). Hence d ∈ {1,3,5,11}.

*Proof.* Let x lie in one of these classes. Compare x with the two old heads of opposite parity: 0 and 8 when x is odd, 3 and 11 when x is even. Each is a different residue from x modulo the relevant modulus. In every case below, neither difference is divisible by either of the two primes that the class determines, so by (SP) the third prime must divide both differences. That is impossible.

| class | x odd: x−0, x−8 | x even: x−3, x−11 | third prime would need |
|---|---|---|---|
| 4 mod 15 | 4, 11 (mod 15) | 1, 8 (mod 15) | 11 to divide both; but 0≢8 and 3≢11 (mod 11) |
| 1 mod 33 | 1, 26 (mod 33) | 31, 23 (mod 33) | 5 to divide both; but 0≢8 and 3≢11 (mod 5) |
| 2 mod 55 | 2, 49 (mod 55) | 54, 46 (mod 55) | 3 to divide both; but 0≢8 and 3≢11 (mod 3) |

Suppose two of 3, 5, 11 divided d. Then Lemma 2(b) would put elements of P in every class modulo their product, including the excluded class. ∎

So (d,e) ∈ {(1,165), (3,55), (5,33), (11,15)}. All four cases are impossible.

## 6. The cases d=1, 3, 5

Fix e. The class r = x mod e of an element x∈Q determines x modulo the primes dividing e, called the *fixed* primes. For d=3, 5 or 11 there is exactly one other prime f of {3,5,11}, the *free* prime.

Let x, x′∈Q have opposite parity and lie in distinct classes, and let k be the number of fixed primes dividing x−x′. Distinct classes force k<2. Then (SQ) is equivalent to the rule:

    (R)   k=0 ⇒ x ≢ x′ (mod f);      k=1 ⇒ x ≡ x′ (mod f).

The old tails are even (0 and 14) or odd (1, 7, 13). Each element named below lies in a class different from the anchor it is compared with. The bracketed numbers are class differences r−y.

**d=1 (e=165).** By Lemma 2(b), Q has an element x ≡ 2 (mod 165).

- If x is even, then x−13 ≡ −11 (mod 165) is odd and divisible by 11 alone.
- If x is odd, then x−14 ≡ −12 (mod 165) is odd and divisible by 3 alone.

Either case violates (SQ).

**d=3 (e=55, f=3).** Q has elements x_3, x_24, x_25 in classes 3, 24 and 25 (mod 55).

- **Class 3** (≡3 mod 5, ≡3 mod 11).
  - Even is impossible. Against 1 [2, k=0], x ≢ 1 (mod 3). Against 13 [−10, k=1], x ≡ 13 ≡ 1.
  - Odd: against 0 [3, k=0], x ≢ 0. Against 14 [−11, k=1], x ≡ 2 (mod 3).
- **Class 24** (≡4 mod 5, ≡2 mod 11).
  - Even is impossible. Against 1 [23, k=0], x ≢ 1. Against 13 [11, k=1], x ≡ 1.
  - Odd: against 0 [24, k=0], x ≢ 0. Against 14 [10, k=1], x ≡ 2 (mod 3).
- **Class 25** (≡0 mod 5, ≡3 mod 11).
  - Odd is impossible. Against 0 [25, k=1], x ≡ 0. Against 14 [11, k=1], x ≡ 2.
  - Even: against 1, 7, 13 [24, 18, 12, k=0 each], x ≢ 1 (mod 3).

So x_3 and x_24 are odd and ≡ 2 (mod 3), and x_25 is even.

- x_25 against x_3 [22, k=1]: x_25 ≡ 2 (mod 3).
- x_25 against x_24 [1, k=0]: x_25 ≢ 2 (mod 3).

Contradiction.

**d=5 (e=33, f=5).** Q has elements in classes 22, 3, 4 and 15 (mod 33).

- **Class 22** (≡1 mod 3, ≡0 mod 11).
  - Even is impossible. Against 1 [21, k=1], x ≡ 1 (mod 5). Against 7 [15, k=1], x ≡ 2.
  - Odd: against 0 [22, k=1], x ≡ 0 (mod 5).
- **Class 3** (≡0 mod 3, ≡3 mod 11).
  - Odd is impossible. Against 0 [3, k=1], x ≡ 0. Against 14 [−11, k=1], x ≡ 4.
  - Even: against 1, 7, 13 [2, −4, −10, k=0 each], x ∉ {1,2,3} (mod 5).
- **Class 4** (≡1 mod 3, ≡4 mod 11).
  - Even is impossible. Against 1 [3, k=1], x ≡ 1. Against 7 [−3, k=1], x ≡ 2.
  - Odd: against 0 [4, k=0], x ≢ 0. Against 14 [−10, k=0], x ≢ 4 (mod 5).
- **Class 15** (≡0 mod 3, ≡4 mod 11).
  - Odd: against 0 [15, k=1], x ≡ 0.
  - Even: against 1, 7, 13 [14, 8, 2, k=0 each], x ≡ 0 or 4 (mod 5).

The chain:

1. x_22 is odd with x_22 ≡ 0.
2. x_3 is even. Against x_22 [−19, k=0], x_3 ≢ 0, so x_3 ≡ 4 (mod 5).
3. Suppose x_15 were odd, so x_15 ≡ 0. Against x_3 [12, k=1], x_15 ≡ 4, which is false. So x_15 is even. Against x_22 [−7, k=0], x_15 ≢ 0, so x_15 ≡ 4.
4. x_4 is odd. Against x_15 [11, k=1], x_4 ≡ 4 (mod 5). But x_4 ≢ 4.

Contradiction.

## 7. The case d=11 (e=15, f=11)

Identify each class r mod 15 with (r_3, r_5) = (r mod 3, r mod 5). Take opposite-parity elements of Q in distinct classes. They share at most one coordinate. Rule (R) becomes:

- if they share exactly one coordinate, they are congruent mod 11;
- if they share none, they are incongruent mod 11.

The anchors are:

| anchor | class | parity | residue mod 11 |
|---|---|---|---|
| 0 | (0,0) | even | 0 |
| 1 | (1,1) | odd | 1 |
| 7 | (1,2) | odd | 7 |
| 13 | (1,3) | odd | 2 |
| 14 | (2,4) | even | 3 |

Put g(0), …, g(4) = 0, 1, 7, 2, 3. Every class is nonempty by Lemma 2(b).

**Lemma 4 (structure of Q).** Every x∈Q is odd if and only if x ≡ 1 (mod 3), and x ≡ g(x mod 5) (mod 11). Equivalently, x mod 55 ∈ {0,1,7,13,14} and the parity of x is fixed by x mod 3.

*Proof.*

- **Step 1.** Classes with r_3=1 contain only odd elements. An even x there shares r_3 with each of the odd anchors 1, 7, 13 outside its own class, and at least two such anchors exist. It would therefore be congruent to two of 1, 7, 2 (mod 11).
- **Step 2.** In class (1,0), every element shares r_5 with anchor 0, so it is ≡ 0 (mod 11). In class (1,4), every element shares r_5 with anchor 14, so it is ≡ 3.
- **Step 3.** Let x be even in a class (r_3,u) with r_3∈{0,2}. Use five odd references: an element of class (1,0) (≡0), an element of class (1,4) (≡3), and the anchors 1, 7, 13 (≡1, 7, 2). Their r_5 values are 0, 4, 1, 2, 3 and their r_3 is 1, so x shares a coordinate with exactly one of them, the one with r_5=u. Hence x ≡ g(u) (mod 11).
- **Step 4.** Let x be odd in a class (r_3,u) with r_3∈{0,2}.
  - If r_3=0 and u≠0, x shares r_3 with anchor 0, so x ≡ 0. If moreover u=4, x also shares r_5 with anchor 14, so x ≡ 3, which is impossible. Hence class (0,4) is entirely even, and by Step 3 its elements are ≡ g(4) = 3.
  - If r_3=2 and u≠4, x shares r_3 with anchor 14, so x ≡ 3. If moreover u=0, x shares r_5 with anchor 0, so x ≡ 0, which is impossible. Hence class (2,0) is entirely even, with elements ≡ g(0) = 0.
- **Step 5.** The remaining odd candidates with r_3∈{0,2} all fail:
  - (0,u), u∈{1,2,3}: x ≡ 0 by Step 4. But x shares nothing with the even elements of (2,0), which are ≡ 0, so x ≢ 0.
  - (2,u), u∈{1,2,3}: x ≡ 3. But x shares nothing with the even elements of (0,4), which are ≡ 3.
  - (0,0): x shares r_3 with (0,4), so x ≡ 3. But x shares nothing with anchor 14, which is ≡ 3.
  - (2,4): x shares r_3 with (2,0), so x ≡ 0. But x shares nothing with anchor 0.

  So every class with r_3∈{0,2} is entirely even, with residues g(r_5) by Step 3.
- **Step 6.** An odd x in class (1,u) shares r_5 with the even elements of (0,u), which are ≡ g(u). Hence x ≡ g(u). ∎

**Lemma 5.** If ξ^110 = 1 and 11 divides the order of ξ, then Q(ξ) ≠ 0.

*Proof.* Fix u∈Z_5. The three classes over u have r_3 = 0, 1, 2, because 5 ≡ 2 (mod 3). By Lemma 4, the r_3=1 class is odd and the other two are even. All elements of these classes are ≡ g(u) (mod 11), and each class has 2^b elements. Hence the number Q_110(z) of elements of Q congruent to z (mod 110) is:

- 2^(b+1) if z is even and z mod 55 ∈ {0,1,7,13,14};
- 2^b if z is odd and z mod 55 ∈ {0,1,7,13,14};
- 0 otherwise.

Since z ≡ 55·(z mod 2) + 56·(z mod 55) (mod 110), this gives

    Q(ξ) = 2^b · (2+ξ^55) · Y(ξ^56),    where Y(X) = 1+X+X^7+X^13+X^14.

Here 2+ξ^55 ∈ {1,3}. Also β = ξ^56 has order equal to the odd part of ord ξ, which is 11 or 55.

- If ord β = 55, then Y(β) ≠ 0, because the nonzero polynomial Y has degree 14 < 40 = deg Φ_55.
- If ord β = 11, then Y(β) = 1+β+β^2+β^3+β^7 ≠ 0, because that polynomial has degree 7 < 10 = deg Φ_11. ∎

**Lemma 6.** The polynomial Φ_11 Φ_22 Φ_55 Φ_110 = 1+X^10+X^20+…+X^100 divides P(X). Consequently the number P_110(z) of elements of P congruent to z (mod 110) depends only on z mod 10.

*Proof.* Each m∈{11,22,55,110} divides n. For a primitive m-th root ξ, P(ξ)Q(ξ) = Σ_{j<n} ξ^j = 0. By Lemma 5, Q(ξ) ≠ 0, so P(ξ) = 0 and Φ_m | P. These four distinct irreducible factors of X^110−1 multiply to (X^110−1)/(X^10−1). Divisibility survives reduction modulo X^110−1. A polynomial of degree <110 that is divisible by 1+X^10+…+X^100 equals R(X)(1+X^10+…+X^100) with deg R<10, so its coefficients are 10-periodic. ∎

**Conclusion for d=11.**

1. Since 11∈P and 11 ≡ 1 (mod 10), Lemma 6 gives P_110(1) = P_110(11) ≥ 1. So some x∈P satisfies x ≡ 1 (mod 110).
2. Such an x is odd and differs from the old heads 0 and 8. The differences are x−0 ≡ 1 and x−8 ≡ −7 (mod 110), so neither is divisible by 5 or 11.
3. By (SP), 3 divides both differences. Then x ≡ 0 and x ≡ 8 ≡ 2 (mod 3).

Contradiction. With the other three cases this proves the Theorem. The Corollary then follows from §2. ∎

## 8. Exact finite checks

Checker: `frontier-20261029-165-family-all-q-check.py`, SHA256 `4c550a5750a822235f20a9862d582082f3427c307f6196575099149638a4538e`, 234 LF / 9,099 bytes. It was executed by `exec` of exactly those bytes in a freshly reset owner eval kernel on 2026-10-29, before 07:15:12 PDT. Every assertion passed and the output was `"result": "PASS"`. It uses only Python integers, `math.gcd` and finite loops. It does not verify any import, nor the all-t written reductions.

The check works on residue types mod 330. This is exact for every t by Lemma 1, since every comparison is between elements of opposite parity. It confirms:

1. Lemma 3's three classes contain no residue mod 330 that passes (SP) against A. The old heads are pairwise (SP)-consistent.
2. Section 6's domain tables.
   - Class 2 (mod 165) has an empty domain.
   - For e=55, the (parity, mod 3) states are exactly {(1,2)}, {(1,2)} and {(0,0),(0,2)}, and no triple from them is pairwise compatible.
   - For e=33, the (parity, mod 5) states are exactly {(1,0)}, {(0,0),(0,4)}, {(1,1),(1,2),(1,3)} and {(0,0),(0,4),(1,0)}, and no 4-tuple from them is pairwise compatible.
3. For e=15:
   - The initial domain sizes are [18,9,2,2,1,8,2,9,2,8,1,2,2,9,18].
   - Unpinned arc consistency over all 15 classes reaches exactly the singleton types predicted by Lemma 4: 0, 1, 7, 13, 14, 55, 56, 62, 68, 110, 234, 276, 282, 288, 289 (mod 330).
   - These types contain Y, are pairwise (SQ)-consistent, and reduce mod 55 to {0,1,7,13,14}.
   - Separate assertions mirror Steps 1–6 one by one.
4. Lemma 5 and Lemma 6, by exact polynomial division.
   - The fold of the Lemma 4 types mod 110 equals the stated weights.
   - Its remainder mod Φ_m is nonzero for m∈{1,2,11,22,55,110} and zero for m∈{5,10}.
   - Y(X) has nonzero remainders mod Φ_55 and Φ_11.
   - Φ_11 Φ_22 Φ_55 Φ_110 = 1+X^10+…+X^100.
5. The final certificate. Among the three types ≡ 1 (mod 110), (SP) against 0 allows only x ≡ 0 (mod 3), and (SP) against 8 allows only x ≡ 2 (mod 3).
6. Bounded diagnostics for t=1,…,6 (n=330, …, 10560), using actual gcd(·,n).
   - G_Y(n) ∋ 1 and G_A(n) ⊇ {3,5,11}.
   - The actual head screen avoids the three Lemma 3 classes.
   - The actual tail screen avoids 2 (mod 165), and its types lie inside every domain used above.
   - Screen sizes: P 6, 42, 112, 224, 448, 896 and Q 47, 118, 286, 658, 1316, 2632.

## 9. Controls, relation to other candidates, limits

**Q-side positive control.** At n=2640 the 15-element set

    {0,1,7,13,14,288,289,385,1376,1712,1760,2048,2256,2544,2592}

was built by CRT with one element per class mod 15 and the parity and mod-11 residue of Lemma 4. Its 16-adic residues are the literal anchors, or 0/1 elsewhere. The checker verifies that it contains Y and that all its pairwise gcds avoid G_A(2640) = {3,5,8,11}. So the Q-side consequences used in case d=11 are jointly consistent. The contradiction needs the P-side transfer of Lemma 6. This set is not a factorization or a code.

**P-side type control.** Each of the two final (SP) constraints on x ≡ 1 (mod 110) is satisfiable on its own. Only both together fail.

**Relation to other candidates; none is used.** If this packet survives review, then at the orders 165·2^t it subsumes:

- the order-660, 1320 and 2640 branch candidates;
- the dispositioned f157 even-tail result at 2640;
- the |Q|=55 branch of f128, for k≥2, as a T2-conditional statement proved by a different method;
- the 165-family odd-tail candidate `fe70…`.

No combined order floor, and no consequence for other orders, is asserted here.

**Limits.**

- Everything depends on LL Corollary 6.2. It gives uniformity of P mod d in Lemma 3 and uniformity of Q mod e in all four cases. Without T2 the case analysis fails at its first step.
- Only odd-difference Sands consequences are used. This is a deliberate relaxation, so the weaker hypotheses still give a valid necessary argument.
- The odd order n=165 (t=0), all other orders, and the original unrestricted problem remain OPEN.

**Review gates.**

1. The quantifiers of the actual-word border theorem, and the hypotheses and statement of LL Corollary 6.2 and Theorem 2.5.
2. (SQ), (SP) and Lemma 1.
3. Lemma 2: cyclotomic allocation and uniformity.
4. Every row of the Lemma 3 and §6 tables, and each chain step.
5. Steps 1–6 of Lemma 4.
6. The counting, CRT factorization and degree arguments of Lemma 5.
7. Lemma 6 and the final three-line contradiction.
8. Confirmation that none of the §0 non-premises is used.

**END OF ALL-Q 165·2^t ANCHORED-BORDER CANDIDATE.**
