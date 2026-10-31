# Higher powers of 5: a high-modulus obstruction to head cardinality 100

Owner **MathShor-2**, math-5. Native `/bin/date` immediately before writing: **Thu Oct 29 13:51:17 PDT 2026**.

**HIGH-CONSEQUENCE WRITTEN UNREVIEWED CANDIDATE, conditional on named tiling and cyclotomic inputs.** This is one consolidated arbitrary-tail proof, including the earlier mod-25 saturation derivation and the new high-modulus lifting argument. It does not merely analyze the special f217 tail. The original unrestricted finite-completion question remains **OPEN**.

## 0. Provenance, review boundary, and imports

Main directed focus on the actual high-modulus lift with all literal head and tail anchors, not another constructed-tail variant. The owner previously derived the arbitrary-tail saturation packet `136274e5…` (f220 is frozen and its review pending), the tail-anchored countermodel `7073ae6a…` (f217 pending), and a special-tail joint obstruction `7f1978ff…`. This proof was developed after those contacts. **None of their mathematical conclusions or review verdicts is a premise:** §§2–5 reconstruct the arbitrary-tail facts; §§6–8 then use actual high-modulus tiling counts. No frozen source is edited, and f220/f217/f219 scopes are not retroactively combined.

Same-author earlier fibre/cofactor exposure, the owner arithmetic/cadence disclosures, the parent-recorded service gap, and every historical HELD/ZERO/NONINPUT record remain. There is no blind-review, unaffected-cognition, novelty, or independent-author claim. No held body, Q55 theorem, solver result, or selected control is used as a proof input.

**Explicit deep import:** Łaba–Londner, [arXiv:2106.14042v3, p. 26, Corollary 6.2](https://arxiv.org/pdf/2106.14042v3): in a cyclic tiling, if at most two distinct primes divide both factor cardinalities, both factors satisfy Coven–Meyerowitz (T2). T2 says that the cyclotomic polynomial at the product of any owned prime powers of distinct primes divides the same mask; see [the same paper, p. 3, Theorem 1.1](https://arxiv.org/pdf/2106.14042v3). The Corollary's ancestry includes the Coven–Meyerowitz two-prime theorem, Tijdeman and subgroup reduction; these are named imports, not independently re-proved here.

Ordinary cyclotomic irreducibility and the degree formula [Q(ζ_m):Q]=φ(m), including irreducibility of Φ_11 over Q(ζ_5) or Q(ζ_25) by coprime conductor degrees, are also named classical inputs. Coprime dilation and equal-gcd exclusion are reconstructed in §2. The actual-word border theorem is a separate named caller in §1.

## 1. Exact statement and original-code caller

Let A={0,3,8,11} and Y={0,1,7,13,14}. An anchored tiling means P,Q⊆Z_n, A⊆P, Y⊆Q, and every residue of Z_n has a unique expression p+q, p∈P,q∈Q.

> **Theorem (candidate).** For every n>14, there is no anchored tiling P⊕Q=Z_n with |P|=100.

> **Corollary (candidate).** At any order n>14, an anchored tiling with |P|=25·2^a requires a≥3. In particular |P|∈{25,50,100} is impossible.

All powers of 2,5 and other primes in n are arbitrary. No order floor or exclusion of |P|≥200 is claimed.

For the literal Shor code

    S=b{1,a,a^7,a^13,a^14} ∪ {a^3,a^8}b{1,a^2,a^4,a^6} ∪ a^11b{1,a,a^2},

the actual-word border theorem of Restivo–Salemi–Sportelli, stated in Cordero [arXiv:2301.13566v1, p. 3, Thm 1.1](https://arxiv.org/pdf/2301.13566v1), gives the same-code anchored P,Q for any finite UD factor-complete extension with pure-a atom a^n. This is an explicit caller import, not a claim that an arbitrary cyclic tiling produces a code. The theorem itself concerns anchored cyclic tilings only.

## 2. Elementary dilation, equal-gcd exclusion, and parameterization

If X⊕Z=Z_n and gcd(t,|X|)=1, then tX⊕Z=Z_n, with multiplication injective on X. For a prime ℓ∤|X|, in F_ℓ[Z_n] let x,z be the characteristic sums and G the sum of all residues. Freshman's dream and Fermat give x^ℓz=x^(ℓ−1)G=|X|^(ℓ−1)G=G. The corresponding nonnegative integer coefficients are all 1 mod ℓ and sum to n, so every coefficient is exactly 1; this also proves injectivity. Iterate over ℓ|t.

In any tiling, nonzero X- and Z-differences cannot have the same gcd with n. If gcd(d_X,n)=gcd(d_Z,n)=g<n, write d_X=gu,d_Z=gv with u,v units mod n/g. CRT lifts v/u to a unit t mod n. As |X| divides n, t is coprime to |X|; tX⊕Z tiles, but td_X≡d_Z gives two representations. This reconstructs the equal-gcd exclusion.

Assume for contradiction |P|=100=2²5². The anchors force 330|n: otherwise the head difference 8,3,5 or11 and tail difference 1 have common gcd 1. Also 3,5,11 divide |Q|: otherwise dilating Q by the missing prime makes its difference 1 collide with the corresponding head difference. Write

    n=2^K·5^v·R,     |Q|=2^(K−2)·5^(v−2)·R,
    K≥2, v≥3,         R odd, gcd(R,5)=1, 33|R.                 (2.1)

Since gcd(R,100)=1, RP⊕Q tiles. Restriction to cosets of RZ_n gives the same positive number of tails in every class mod R. Hence every class mod 33 contains exactly

    w = 2^(K−2)·5^(v−2)·R/33 > 0                             (2.2)

tails. This fact does not assume R squarefree.

For an odd Q-difference x, put g=gcd(x,n). If 25∤x then gcd(x,165)=1. Indeed, if 5|x but 25∤x, t=g/5 is odd and 5-free, so tP⊕Q tiles and the scaled actual head difference 5 has gcd g, a contradiction. If 5∤x but 3|x or11|x, use t=g/3 or g/11 and the corresponding actual head difference. Thus opposite-parity Q-elements agreeing mod 3,5 or11 must agree mod 25. We call this the *odd tail rule*.

## 3. The arbitrary tail graph is forced by the anchors

No even q∈Q is 1 mod 3: comparing it with the three odd anchors 1,7,13 and using the odd tail rule would force q to be congruent to each of these three distinct values mod25. Hence all tails 1 mod3 are odd.

Class 3 mod33 contains only even tails, since an odd one would have to equal both anchor 0 mod25 (agreement mod3) and anchor 14 mod25 (agreement mod11). Class 25 mod33 is odd and compares with 14 mod11, so it is 14 mod25. Comparing a class-3 element to a class-25 element makes every class-3 tail 14 mod25.

Likewise class 11 mod33 is even: an odd element would have to equal 14 (same mod3 as anchor14) and 0 (same mod11 as anchor0). Class 22 mod33 is odd and equals 0 mod25 by comparison with anchor0. Hence every class-11 tail also equals 0 mod25.

An odd tail 0 mod3 would have to equal both anchor0 and an even class-3 tail mod25, namely 0 and14. An odd tail 2 mod3 would have to equal both anchor14 and an even class-11 tail, namely14 and0. Therefore

    q odd  ⇔  q≡1 (mod3).                                       (3.1)

Every pair of residues (r mod3,j mod11) is occupied by (2.2). For any j mod11 choose one odd Q-element with r=1 and one even element with r=0. The odd tail rule makes all tails with label j have one common residue f(j) mod25. The five literal anchors give

    f(0)=0, f(1)=1, f(2)=13, f(3)=14, f(7)=7.                (3.2)

For any j,k, if f(j)≡f(k) mod5, choose opposite-parity tails with these labels; the odd tail rule forces f(j)=f(k) mod25. The five values in Y cover all five mod5 residues once, so every f(j) is one of Y. The other six values are genuinely arbitrary; no special f217 choice is assumed.

## 4. All 25-residue Fourier rows of P are uniform

For ω∈{1,−1}, τ∈μ_3, η∈μ_11 and ξ∈μ_25, put χ(x)=ω^xτ^xη^xξ^x. From (2.2), (3.1) and f,

    Q̂(χ)=w(1+τω+τ²) Σ_(j=0)^10 η^j ξ^(f(j)).                (4.1)

The j-sum is nonzero whenever ξ≠1, for every allowed f:

- If η≠1, η has minimal polynomial Φ_11 of degree10 over Q(ξ), by the named coprime-conductor degree input. A degree-at-most10 polynomial vanishing at η must have all 11 coefficients equal. Those at j=0 and j=1 are 1 and ξ, different.
- If η=1 and ξ has order25, the sum is a nonzero polynomial in ξ of degree≤14, whereas Φ_25 has degree20.
- If η=1 and ξ has order5, reduce the exponents mod5. The five coefficients are positive integers summing to11 and hence cannot all be equal. A degree-at-most4 polynomial vanishing at a primitive fifth root is a scalar multiple of Φ_5 and has equal coefficients.

For τ=1 and ω=±1, the prefactor 2+ω is nonzero. For ω=−1 and τ primitive3, the prefactor is −2τ, also nonzero. The tiling identity P̂Q̂=0 and Fourier inversion therefore imply:

1. for every parity ε and j mod11, the number of P-elements in each class mod25 is one constant c_(ε,j);
2. for every i mod3 and j mod11, the **difference** between even and odd P-counts is independent of the mod25 class.

The literal anchors 0,11,3,8 occupy four distinct parity/mod11 buckets: (even,0),(odd,0),(odd,3),(even,8). Each has c≥1. Since |P|=100=4·25, these are **all** the buckets, each with c=1. In each bucket there is exactly one P-element per residue z mod25.

Write E(z),O(z)∈Z_3 for the labels of the unique even and odd elements in the j=0 buckets. The signed mod3 property says the vector e_(E(z))−e_(O(z)) is independent of z. It is either always zero (E(z)=O(z) for all z), or a fixed ordered pair of distinct labels. The odd j=3 row is constant mod3 and contains 3, hence has label0. The even j=8 row is constant mod3 and contains 8, hence has label2.

The equal alternative E(z)=O(z) is impossible: fold the actual tiling to Z_2×Z_3×Z_11×Z_25 and fix a target of parity0 and residue0 mod3, with any mod11 value J and any mod25 value. It must have 2w representations since n/(2·3·11·25)=2w. The even/odd j=0 head rows use the same required mod25 residue z−f(J) and contribute exactly one possible Q class mod3 between them. The even j=8 row would need an even tail 1 mod3, and the odd j=3 row an odd tail 0 mod3; neither exists. Thus the count would be w, contradiction.

Therefore E,O are constant and distinct. Anchor0 gives E=0; anchor11 gives O=2. CRT yields the **exact saturation**

    P mod66 = 25·{0,3,8,11},                                  (4.2)

with one P-element per mod25 class in each of those four rows. In particular |P|=25 or50 is already impossible, independently of T2.

## 5. Cyclotomic allocation and individual Q-fibres

Both P and Q satisfy T2 by the named Łaba–Londner Corollary: only 2 and5 can divide |P|, so at most those two primes can be shared. All hypotheses, including arbitrary other prime powers in R, are covered.

P owns Φ_5 and Φ_25, because §4 proved Q nonzero at all primitive fifth and 25th roots and the tiling mask product vanishes there. Q(−1)=11w≠0 by (3.1), so P owns Φ_2.

Among Φ_(2^i), 1≤i≤K, P owns **exactly two** and Q owns the others. Each factor divides at least one mask by the tiling identity; if m_P and m_Q count ownership with multiplicity, then m_P+m_Q≥K. Evaluating prime-power divisors at 1 gives m_P≤v_2(|P|)=2 and m_Q≤v_2(|Q|)=K−2, so equality holds throughout and no factor is shared. Thus P owns Φ_2 and exactly one further Φ_(2^s), 2≤s≤K.

For every prime power ℓ^j|R, Q owns Φ_(ℓ^j): otherwise evaluation at1 would force ℓ to divide |P|=100. If Q owns Φ_(2^i), Q's T2 gives Φ_(2^i d) for every d|R. Since R is odd,

    Φ_(2^i)(X^R)=∏_(d|R) Φ_(2^i d)(X).                         (5.1)

Writing Q(X)=Σ_(r modR) X^r F_r(X^R), uniqueness of the residue-basis decomposition gives Φ_(2^i)|F_r for **every** mod-R fibre. Because R is odd, the original-exponent mask of each Q_r also vanishes at primitive 2^i-th roots.

Consequently, if Q owns Φ4, Φ8 or Φ16, then within each actual Q_r the folded mod-4, mod-8 or mod-16 counts agree across the two halves of each lower-bit class. For example Φ16 implies counts at x and x+8 mod16 are equal. This is an exact coefficient statement from Φ_(2^i)=1+X^(2^(i−1)), not an assumption of a particular fibre shape.

**Even-difference rule.** If q,q′∈Q, 5∤(q−q′), and gcd(q−q′,n) has exact 2-part 8, then no tiling exists: t=gcd(q−q′,n)/8 is odd and 5-free, hence coprime to |P|; the actual head difference 8 in tP⊕Q has the same gcd. When K≥4, the exact 2-part condition is q−q′≡8 (mod16). When K=3 it is simply q≡q′ (mod8).

## 6. Eliminating all 2-adic allocations except s=4

**K=2 is impossible:** gcd(3·8,n)=gcd(13−1,n)=12. Dilation by 3 is allowed because gcd(3,100)=1, so the head difference 3·8 and the tail difference 13−1 contradict equal-gcd exclusion.

**K=3.** Then s=2 or3.

- If s=2, Q owns Φ8. The Q_r containing anchor13 has a tail congruent to 1 mod8, paired with 13≡5 mod8. Its mod25 value is f(2)=13, whereas anchor1 has value 1. Their difference is divisible by8 and not5, contrary to the even-difference rule.
- If s=3, Q owns Φ4. The Q_r containing anchor7 has a tail congruent to1 mod4, paired with 7≡3. Its mod8 residue is 1 or5. Compare it with anchor1 or13 respectively: the difference is divisible by8 and their mod5 values are distinct. Again the even-difference rule is violated.

**K≥4.**

- If s∉{3,4}, Q owns Φ8 and Φ16. Starting from anchor13≡5 mod8, Φ8 gives an element in the same Q_r congruent1 mod8; Φ16 gives one congruent9 mod16. Its mod25 value is13, whereas anchor1 is1. Their difference is 8 mod16 and not divisible by5: contradiction.
- If s=3, Q owns Φ4 and Φ16. Starting from anchor7≡3 mod4, Φ4 gives an element of its Q_r congruent1 mod4. If its mod8 value is1, Φ16 supplies residue9 mod16 and it collides with anchor1. If its mod8 value is5, Φ16 supplies residue5 mod16 and it collides with anchor13≡13 mod16. Its mod25 value is7, different mod5 from both anchors. Again the even-difference rule is violated.

Thus the only remaining possibility is

    K≥4,    P owns Φ2 and Φ16,    Q owns Φ4 and Φ8.            (6.1)

## 7. The final high-modulus lift when s=4

### 7.1 A global mod-16 support for Q

By §5, **each actual mod-R fibre** owns Φ4 and Φ8 and has a fixed parity from (3.1). Hence, within each fibre, each of the four mod8 residues of that parity occurs with the same positive count. For every j mod11 and each permitted parity, such fibres exist by (2.2).

Fix a parity and one residue u mod8 of that parity. All five distinct f-values occur among Q-elements in that parity and residue u: choose an anchored label j for each value, then choose any required mod-R class and use its uniform mod8 support. If two such elements from different f-values occupied u and u+8 mod16, their difference would be 8 mod16 and not divisible by5, contradicting the even-difference rule. If a single f-value occupied both bits, an element of another f-value exists at one bit and conflicts with the opposite one. Thus **all** Q-elements with that parity and mod8 residue have the same mod16 residue, independently of their mod3 and mod11 labels.

Let E be the resulting four even mod16 residues and O the four odd residues. Each contains exactly one lift of each mod8 residue of its parity. In particular

    E⊔(E+8)=the eight even residues mod16,                   (7.1)

and similarly for O in the odd residues. Moreover, each actual Q class mod33 has exactly w/4 elements at each of the four residues in its parity set: this follows by summing the equal mod8 counts of its constituent mod-R fibres. Thus w is divisible by4.

The stabilizer of E under even translations is trivial. Any nonzero even translation generates a subgroup of Z_16 containing 8. If E were invariant under it, E would also be invariant under 8, contrary to (7.1).

### 7.2 The actual P rows become constant mod16

P owns Φ16, Φ5 and Φ25. By P's T2 it owns Φ80 and Φ400, and

    Φ16(X) Φ80(X) Φ400(X) = Φ16(X^25)=1+X^200.              (7.2)

For example Φ16=1+X^8, Φ80=1−X^8+X^16−X^24+X^32, and Φ400=1−X^40+X^80−X^120+X^160. Decompose P(X)=Σ_(z mod25)X^z P_z(X^25). Equation (7.2) implies Φ16|P_z for each z, so the mod16 counts of P in each fixed mod25 class match across residue r and r+8.

By (4.2), for each z mod25 there is exactly one actual P-element in each of the four rows 0,3,8,11 mod66. Let p_α(z) be its residue mod16. The rows 0 and8 are even, 3 and11 odd. The pairing just proved forces

    p_8(z)=p_0(z)+8,       p_11(z)=p_3(z)+8       (mod16).    (7.3)

Fold the actual tiling onto Z_16×Z_3×Z_11×Z_25. Every target receives n/(16·3·11·25)=w/4 representations. Fix a target mod25 value z and mod11 value J.

For target parity0 and mod3=2, the only possible head/tail-mod3 pairs are (head row 0, tail residue2) and (head row8, tail residue0). The two Q classes have mod16 support E with weight w/4 per residue. Hence the two translates

    E+p_0(z−f(J)),       E+p_8(z−f(J−8))

are disjoint and cover the eight even residues. Because the complement of E is E+8 and E has trivial even stabilizer, their offsets differ by exactly 8 mod16. Together with (7.3),

    p_0(z−f(J)) = p_0(z−f(J−8))      (mod16).                (7.4)

Take J=0. Then J−8=3 mod11 and f(0)−f(3)=−14, a unit mod25. As z varies, (7.4) makes p_0 constant on Z_25. Anchor0 gives p_0(z)=0 and p_8(z)=8 for all z.

Similarly, for target parity1 and mod3=2, the only head/tail pairs are (row3, tail residue2) and (row11, tail residue0). Their E-translates force

    p_3(z−f(J−3)) = p_3(z−f(J))      (mod16).

Taking J=3 uses f(3)−f(0)=14, again a unit mod25. Anchor3 gives p_3(z)=3 and p_11(z)=11 for every z. Thus **every actual P-element is congruent mod16 to its head-row anchor**.

### 7.3 Two target classes give an impossible period

For target parity0 and mod3=0, the only head/tail-mod3 pairs are (row0, tail0) and (row11, tail1). Their shifted Q supports E and 11+O must partition the eight even residues. By (7.1),

    11+O = E+8,       so O=E−3.                               (7.5)

For target parity1 and mod3=0, the only pairs are (row3, tail0) and (row8, tail1). Their shifted supports 3+E and 8+O must partition the eight odd residues, so

    8+O = 3+E+8,      so O=E+3.                               (7.6)

Equations (7.5)–(7.6) imply E+6=E. But 6 is a nonzero even translation, so its generated subgroup contains 8, contradicting the trivial-stabilizer property in §7.1. This rules out s=4 and completes the theorem. ∎

## 8. Finite controls and precise verification boundary

In the retained owner eval kernel, using Python integers, `itertools` and `math.gcd` only, the owner checked:

- For five nonempty bit-support sets at one fixed parity/mod8 coordinate, all 3^5=243 possibilities were considered. Under the necessary condition that distinct f-labels never occupy opposite bits, exactly two patterns remain: all five use bit0, or all use bit1.
- All 16 four-element even transversals E mod16 were checked: E+8 is the complementary even set, and no nonzero even translation stabilizes E. All 16×16 candidate pairs of even/odd transversals were checked; none satisfies both 11+O=E+8 and 8+O=11+E.
- The four actual head/tail-mod3 pairings used in §§7.2–7.3 were checked directly. The shift 14 generates all of Z_25.
- Integer coefficient multiplication checked (7.2) exactly. The low-bit anchor comparisons in §6 and a bounded set of the K=2 gcd identities were checked with integer arithmetic; they do not replace the written all-n cases.

These are finite same-owner controls of the bit/set arithmetic, not a formal proof or an independent verifier. The universal all-n argument is the written derivation. The LL Cor6.2/T2, cyclotomic degree and actual-code caller imports remain conditional pending independent source/application review. No human, independent-model-family or novelty gate has been performed by the owner.

The previous twofold quotient remains a valid **relaxation** of the mod1650 saturation, not a tiling; this packet uses additional mod16 and T2 fibre information precisely beyond that quotient. The f217 special tail and its pending review are not inputs. This theorem, if reviewed and adopted, excludes only |P|=100; larger powers of 5, head cardinality 15·2^a, and the original unrestricted problem remain OPEN.

## 9. Review obligations

A complete review must reconstruct the whole all-n proof, in particular:

1. the actual arbitrary-Q parity/f(j) graph and the field-degree nonvanishing with six free labels;
2. the four-row saturation and its 2w-versus-w folded count;
3. prime-power ownership counting, exact applicability of LL Cor6.2/T2 to **both** masks, and extraction of every Q_r factor using (5.1);
4. every K=2, K=3 and K≥4 case, including the two anchor comparisons and the exact 2-adic gcd needed for each multiplier;
5. for s=4, the common-bit and equal-weight conclusions in §7.1; the residue-basis extraction in (7.2); the projected multiplicity w/4; and the two shift-invariance arguments using f(0)−f(3)=−14;
6. the translated-set complement equations and the final period-6 contradiction;
7. all provenance, non-premise, import and original-code caller qualifications.

**END OF ARBITRARY-TAIL HEAD-100 HIGH-MODULUS OBSTRUCTION.**
