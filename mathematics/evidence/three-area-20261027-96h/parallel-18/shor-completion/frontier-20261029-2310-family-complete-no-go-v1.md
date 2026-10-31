# Shor completion: no anchored border tiling at any order 2310·2^k

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Thu Oct 29 08:49:23 PDT 2026**.

**Status: HIGH-CONSEQUENCE UNREVIEWED CANDIDATE.** The argument is WRITTEN for every k≥0. It has three named imports:

- the actual-word border theorem (classical, reconstructed in §2);
- Sands' divisor-set theorem;
- Tijdeman's dilation theorem.

It does **not** use the Coven–Meyerowitz condition T2 or Łaba–Londner Corollary 6.2, any solver outcome, or any fibre, Q55 or cofactor packet. The finite arithmetic facts it quotes were checked with exact integers in the owner's eval kernel (§7).

This is not an adoption, formal proof, human review, independent-model-family review or novelty clearance. **The original unrestricted finite-completion problem remains OPEN.**

## 0. Provenance and non-imports

After logging `564956bf…` as an UNREVIEWED necessary condition, Main directed on 2026-10-29: "Continue the literal open d∈{7,21,35,77} bridge or produce a genuinely global witness/no-go; retain same-author exposure and all non-premise statements." This packet closes that bridge for the whole family.

This is same-author work. The owner's provenance statement sent to Main on 2026-10-29 shortly after 00:02:01 PDT applies here as well. Verbatim:

> "Provenance correction to my pending freeze question: by 'independent' I meant no dependency on the pending Q55 theorem or a fibre packet as a mathematical premise. It is SAME-AUTHOR work, not a disjoint exposure: I had read and considered my prior unreviewed fibre-related sources before developing this route."

History. The owner found this route on 2026-10-29, between about 07:55 and 08:29 PDT, and recorded it in `owner-20261029-checkpoint-2310-bridge-tijdeman-v1.json`. That file also discloses a 37-minute checkpoint-cadence overrun. During that work, the owner ran exploratory eval-kernel computations: state censuses of the earlier e=165 arc-consistency fixpoint, and a Q-side arc-consistency computation for e ∈ {165, 55, 33, 15}, strengthened by Tijdeman's theorem. They closed no case, and none is used here. Every finite fact below is recomputed by the pinned checker of §7.

**Not premises.** Each item below is a separate unreviewed, or only conditionally dispositioned, same-author candidate. This packet uses none of them:

- `frontier-20261029-2310-family-all-q-seven-divides-head-v1.md` (`564956bf…`);
- `frontier-20261029-165-family-all-q-anchored-border-no-go-v1.md` (`20169ac9…`) and its erratum 1 (`54329f3e…`);
- `frontier-20261028-universal-55-tail-obstruction-v1.md` (`d6c9929c…`, f128), the odd-55 cofactor classification, and every `*fibre*` packet;
- the 2310-family packets `frontier-20261028-2310-family-q55-obstruction-v1.md` (`01b0904c…`), `…-odd-tail-joint-prime-obstruction-v1.md` (`b6189059…`), `…-odd-tail-three-residuals-v1.md` (`fce25631…`) and `…-q165-coupled-gcd-obstruction-v1.md` (`33c64115…`), together with the f169 review of that chain;
- the order-2310 candidate `frontier-20261028-2310-border-no-go-candidate-v1.md` (`88bd20a0…`);
- every order-660, 1320, 1980 or 2640 packet, and the f157 and f174 parent dispositions;
- all HELD, ZERO or NONINPUT material.

Where those packets prove overlapping statements, this packet re-derives what it needs from the three named imports alone.

## 1. Statement

> **Theorem (candidate).** Let k≥0 and n=2310·2^k. No subsets P,Q ⊆ Z_n satisfy all three conditions: every residue of Z_n is uniquely p+q with p∈P and q∈Q; A={0,3,8,11}⊆P; and Y={0,1,7,13,14}⊆Q.

No restriction is placed on |P|, on |Q|, or on the parity of either.

> **Corollary (candidate).** No finite uniquely decipherable, factor-complete extension of the literal Shor code has actual pure-a atom a^n with n=2310·2^k, k≥0.

This excludes the orders 2310, 4620, 9240, 18480, … for every tail cardinality. In particular it covers the cases d∈{7,21,35,77} that `564956bf…` left open, where d is the odd part of |P|.

Conditional scope: §2 (actual border) and §3 (Sands, Tijdeman). §4 also records two lemmas that hold for every order divisible by 330. Orders not of the form 2310·2^k are not addressed beyond those lemmas. The unrestricted original question is not addressed.

## 2. Actual border factorization (classical import, reconstructed)

Let `1` be the empty word. The literal code is

    S = b{1,a,a^7,a^13,a^14} ∪ {a^3,a^8} b {1,a^2,a^4,a^6} ∪ a^11 b {1,a,a^2}.

Suppose, for contradiction, that D is a finite code with these properties:

- D contains S;
- D is UD (concatenation of atom sequences is injective);
- D is factor-complete (every word over {a,b} is a factor of a word in D*);
- D has actual pure-a atom a^n.

Let L be the maximum atom length. Completeness embeds a^(2L+1) in a D-factorization, so some pure-a atom exists. Two distinct pure-a atoms a^u, a^v would give the different lists (a^u,a^v) and (a^v,a^u) for the same word. Since b∈S, UD forbids b^k for k≥2: the list (b^k) and the list of k copies of (b) would spell the same word. Define

    P = {i mod n : a^i b^k ∈ D, k≥1},     Q = {j mod n : b^l a^j ∈ D, l≥1}.

Then A⊆P and Y⊆Q. The classical statement is the Restivo–Salemi–Sportelli theorem, as given in Cordero, [arXiv:2301.13566v1, p. 3, Theorem 1.1](https://arxiv.org/pdf/2301.13566v1). The following reconstruction uses only UD and factor-completeness.

**Directness.** Take actual atoms u_t = a^(i_t) b^(k_t) and v_t = b^(l_t) a^(j_t) for t=1,2, with i_1+j_1 ≡ i_2+j_2 (mod n). Choose G in that common class, larger than both i_t+j_t, and choose H and K large. Each of the two lists

    (b)^(H−l_t), v_t, (a^n)^((G−i_t−j_t)/n), u_t, (b)^(K−k_t)

spells b^H a^G b^K. A border atom without an a is b. Otherwise the left border atom starts with b and ends with a, and the right border atom starts with a and ends with b. So the positive central a-run identifies both border atoms. Distinct residue pairs would therefore give distinct lists for the same word, contrary to UD.

**Coverage.** Embed b^L a^g b^L, with g>L in a prescribed class mod n. The atom containing the last left b starts inside the left guard and cannot reach the right guard, so it is some b^l a^j. Symmetrically, the atom containing the first right b is some a^i b^k. Every atom between them is a^n. Hence g ≡ i+j (mod n).

So P⊕Q=Z_n and |P||Q|=n. Since n ≥ 2310, the anchors are distinct residues.

## 3. Imports and two elementary tools

For X ⊆ Z_M write Div_M(X) = {gcd(x−x′, M) : x, x′ ∈ X}. For an integer t, tX denotes {tx : x∈X}.

**(I1) Sands.** For P,Q ⊆ Z_M, P⊕Q=Z_M holds iff |P||Q|=M and Div_M(P) ∩ Div_M(Q) = {M}. See Łaba–Londner, [arXiv:2106.14042v3, p. 10, Theorem 2.5](https://arxiv.org/pdf/2106.14042v3). Only the direction "tiling ⇒ disjoint divisor sets" is used.

**(I2) Tijdeman.** If P⊕Q=Z_M and r is coprime to |P|, then rP⊕Q=Z_M. In particular rP has |P| distinct residues.

- Łaba–Londner state the integer form, [arXiv:2106.14042v3, p. 3](https://arxiv.org/pdf/2106.14042v3): "Tijdeman [47] proved that if a finite set A tiles the integers, and if r ∈ N is relatively prime to |A|, then rA := {ra : a ∈ A} also tiles Z with the same tiling complement".
- They apply it in Z_M in the proof of their Corollary 6.2 (p. 26), citing "[47, Theorem 1]; see also [2, Lemma 2.2]". Here [47] is R. Tijdeman, *Decomposition of the integers as a direct sum of two subsets* (1995), and [2] is Coven–Meyerowitz.
- The cyclic form follows from the integer form, because P⊕Q=Z_M is equivalent to P⊕(Q+MZ)=Z.

**(D) Dilation.** If P⊕Q=Z_M and gcd(t,|P|) = gcd(s,|Q|) = 1, then tP⊕sQ=Z_M. Hence, by (I1), Div_M(tP) ∩ Div_M(sQ) = {M}. *Proof.* Apply (I2) to P to get tP⊕Q. Then apply it to Q inside that tiling, using |tP|=|P|. ∎

**(C) Coset restriction.** Let X⊕Z=G be a direct sum in a finite abelian group with X⊆H, a subgroup. Then X⊕(Z∩(g+H)) = g+H for every coset g+H, and so |Z∩(g+H)| = |H|/|X|. *Proof.* Each y ∈ g+H is uniquely x+z, and z = y−x ∈ g+H. ∎

All divisor sets below are taken with M=n unless stated otherwise. The relevant differences of the anchors are:

- the odd A-differences are ±3, ±5, ±11, with witnesses 3=3−0, 5=8−3, 11=11−0;
- 1 = 1−0 is a Y-difference, so 1 ∈ Div(Y) ⊆ Div(Q).

## 4. Two lemmas for every order n with 330 | n

**Lemma 1.** Each p∈{3,5,11} divides |Q|.

*Proof.* Suppose p∤|Q|. By (D) with s=p, P⊕pQ=Z_n. Since p·1−p·0 = p and p|n, we have p = gcd(p,n) ∈ Div(pQ). The A-difference equal to p gives p ∈ Div(P). Since p≠n, this contradicts (I1). ∎

**Lemma 2 (forbidden odd tail differences).** Let q,q′∈Q with x=q−q′ odd, and let g=gcd(x,n). If some p∈{3,5,11} divides x and g/p is coprime to |P|, we have a contradiction.

*Proof.* Put t=g/p, an integer because p divides both x and n. By (I2), tP⊕Q=Z_n. The A-difference p gives the tA-difference tp=g, and gcd(g,n)=g. So g ∈ Div(tP) ∩ Div(Q). Since x is odd and n is even, g≠n. This contradicts (I1). ∎

**Lemma 3.** |P| is not a power of 2.

*Proof.* Suppose |P|=2^a, and let T be the odd part of n. T is coprime to |P|, so TP⊕Q=Z_n by (I2). TP lies in the subgroup TZ_n, whose cosets are the residue classes mod T. By (C), Q meets every class mod T. Since 165|T, Q contains some q ≡ 6 (mod 165).

Let x be any odd Q-difference and p∈{3,5,11} a prime dividing it. Then g/p is odd, hence coprime to 2^a, so Lemma 2 forbids x. Thus every odd Q-difference is coprime to 165. If q is odd, x=q−0 is odd, and 3|x because q≡0 (mod 3). If q is even, x=q−1 is odd, and 5|x because q≡1 (mod 5). Either way we have a contradiction. ∎

*Remark (disclosed, not proposed for review).* For n=165·2^t with t≥1, Lemma 1 gives 165 | |Q|, so |P| is a power of 2, and Lemma 3 excludes it. This reproduces the theorem of `20169ac9…` from the border theorem, (I1) and (I2), without T2. Main has said that no incremental review variant of that candidate will be added while the f176 written-proof review is pending. This remark is recorded for the parent's information only. It changes neither that candidate nor its review scopes.

## 5. The family n = 2310·2^k

Write n = 1155·2^K with K=k+1≥1. By Lemma 1, 165 | |Q|. Since |P||Q|=n, |P| is either 2^a or 7·2^a. Lemma 3 excludes 2^a. It remains to treat

    |P| = 7·2^a,   |Q| = 165·2^b,   a+b = K.

Under this assumption, 165 is coprime to |P| and 7 is coprime to |Q|. For r∈Z_165 put Q_r = {q∈Q : q≡r (mod 165)}. For γ∈Z_7 put P_γ = {p∈P : p≡γ (mod 7)}.

**(S1) Tail rule mod 7.** If q,q′∈Q, q−q′ is odd, and gcd(q−q′,165)>1, then q≡q′ (mod 7).

*Proof.* Otherwise g=gcd(q−q′,n) is an odd divisor of 165. For a prime p∈{3,5,11} dividing q−q′, g/p is a product of primes from {3,5,11}, so it is coprime to 7·2^a. Lemma 2 then gives a contradiction. ∎

**(S2) Fibres.** By (I2), 165P⊕Q=Z_n. The set 165P lies in 165Z_n, whose cosets are the classes mod 165. By (C), every Q_r has exactly (n/165)/|P| = 2^b ≥ 1 elements.

**(S3) Parity dichotomy.** Exactly one of the following holds:

- every Q_r contains elements of both parities; or
- every P_γ contains elements of both parities, and each Q_r has all its elements of a single parity.

*Proof.* Fix r and γ, and let N = n/165 = 7·2^K.

1. By (C) applied to 165P⊕Q, Q_r⊕165P = r+165Z_n, so (Q_r−r)⊕165P = 165Z_n.
2. The map ι: 165Z_n → Z_N, 165y ↦ y mod N, is a group isomorphism. Put V = ι(Q_r−r) and P̄ = ι(165P) = {p mod N : p∈P}. Then V⊕P̄ = Z_N and |V| = 2^b.
3. Since 7 is coprime to |V|, (I2) gives 7V⊕P̄ = Z_N.
4. 7V lies in 7Z_N, whose cosets are the classes mod 7. By (C), P̄_γ⊕7V equals the class γ mod 7 in Z_N, where P̄_γ = {p mod N : p∈P_γ}.
5. By CRT, reduction mod 2^K maps that class bijectively and additively onto Z_{2^K}. Hence (P̄_γ mod 2^K)⊕(7V mod 2^K) = Z_{2^K}.

Parities transfer as follows. For p∈P, p mod 2^K has the parity of p. For q∈Q_r, write q−r=165y with y∈V. Then y≡q−r (mod 2), and 7y mod 2^K has the parity of y. So the first factor contains an odd difference iff P_γ has both parities, and the second iff Q_r has both parities.

In a tiling of Z_{2^K} with K≥1, at most one factor contains an odd difference. If both did, 1 would lie in both divisor sets, against (I1). At least one factor contains an odd difference, since otherwise every sum would have one parity. So for every pair (γ,r), exactly one of P_γ and Q_r has both parities. If some Q_{r0} has both parities, no P_γ does, and then every Q_r does. Otherwise every Q_r is single-parity, and then every P_γ has both parities. ∎

**(S4) Not every Q_r has both parities.** Suppose every Q_r does.

- Within Q_r, an even element and an odd element differ by an odd multiple of 165. By (S1) they are congruent mod 7, so all of Q_r has one residue mod 7.
- An even element of Q_r and an odd element of Q_{r+3} have an odd difference ≡ −3 (mod 165), whose gcd with 165 is 3. By (S1), Q_r and Q_{r+3} share their residue mod 7. The same holds for Q_r and Q_{r+5}.
- Since 3 and 5 generate Z_165, all of Q has one residue mod 7.

But 0,1 ∈ Y ⊆ Q. ∎

**(S5)** By (S3) and (S4), every P_γ contains both parities, and every Q_r is single-parity, say of parity ε_r. Let E = {r : ε_r=0} and O = {r : ε_r=1}. The anchors give 0,14 ∈ E and 1,7,13 ∈ O; their classes mod 165 are distinct.

**(S6) Separation.** Let p,p′∈P_γ with p−p′ odd, and let h₀=gcd(p−p′,165). Then no r∈E and r′∈O satisfy r≡r′ (mod h₀).

*Proof.* Suppose r∈E, r′∈O and h₀ | r−r′. Take q∈Q_r and q′∈Q_{r′}. Then x=q−q′ is odd and h₀|x. Let h=gcd(x,165), so h₀|h. Since h is coprime to |P| and 7 is coprime to |Q|, (D) gives hP⊕7Q=Z_n. We compute two gcds:

- gcd(7x,n) = 7h. Indeed 7x is odd, 49∤n, and for ℓ∈{3,5,11}, ℓ | 7x iff ℓ|h.
- gcd(h(p−p′),n) = 7h. Indeed h(p−p′) is odd and 7|p−p′. For ℓ∈{3,5,11}, ℓ | h(p−p′) iff ℓ|h or ℓ|h₀, which holds iff ℓ|h.

So 7h ∈ Div(hP) ∩ Div(7Q), and 7h≠n because 7h is odd. This contradicts (I1). ∎

Because E and O are both nonempty, h₀>1. By (S6), membership of r in E depends only on r mod h₀.

**Lemma H.** Let ℓ∈{3,5,11} and m=165/ℓ=q₁q₂, and use CRT to write Z_165 = Z_ℓ × Z_m. Suppose E⊔O = Z_165 with E and O nonempty, and E = Z_ℓ × E′ for some E′ ⊆ Z_m. Then the bipartite graph H is connected. Its vertex set is Z_165; its edges join r∈E and r′∈O whenever gcd(r−r′,165)>1, that is, whenever r and r′ agree mod 3, mod 5 or mod 11.

*Proof.* We have O = Z_ℓ × O′ with E′⊔O′ = Z_m, both nonempty.

1. For each x∈Z_ℓ, every (x,e′) with e′∈E′ is adjacent to every (x,o′) with o′∈O′, since they agree mod ℓ. So each layer {x}×Z_m is connected.
2. Some e′∈E′ and o′∈O′ agree mod q₁ or mod q₂. If not, take e′=(e₁,e₂) and o′=(o₁,o₂), so that e₁≠o₁ and e₂≠o₂. The element z=(e₁,o₂) agrees with e′ mod q₁, so z∉O′; it agrees with o′ mod q₂, so z∉E′. This is impossible.
3. With such a pair, (x,e′) is adjacent to (x′,o′) for all x and x′. This joins all the layers. ∎

**(S7) h₀ = 165.** This holds for every pair in (S6).

*Proof.* Otherwise some prime ℓ∈{3,5,11} does not divide h₀. Then h₀ | 165/ℓ, so membership in E does not depend on the ℓ-coordinate, and Lemma H makes H connected. For any edge (r,r′) and any q∈Q_r, q′∈Q_{r′}, q−q′ is odd and gcd(q−q′,165) = gcd(r−r′,165) > 1. By (S1), all of Q_r ∪ Q_{r′} then has one residue mod 7. Since H is connected and every fibre is nonempty, all of Q has one residue mod 7, again contradicting 0,1∈Q. ∎

**(S8)** For each γ, all elements of P_γ are congruent mod 165. By (S5), P_γ contains both parities. Each even–odd pair is congruent mod 165 by (S7). Two elements of the same parity are both congruent to an element of the other parity.

**(S9) Contradiction.** 0∈P_0, and P_0 contains an odd element p₀. By (S8), p₀≡0 (mod 165); also p₀≡0 (mod 7), so p₀≡0 (mod 1155). The anchor 8 lies in P. The difference x=8−p₀ is odd and x≡8 (mod 1155). Since gcd(8,1155)=1, gcd(x,n)=1. But 1 ∈ Div(Y) ⊆ Div(Q), which contradicts (I1). ∎

This excludes |P| = 7·2^a. Together with Lemma 3, it proves the Theorem. The Corollary follows by §2.

## 6. Remarks and limits

1. **Relation to `564956bf…`.** Lemmas 1 and 3 already imply that candidate's conclusion: the odd part d of |P| is 1 or 7, and d=1 is impossible. This packet does not use it. That packet and its hash are unchanged.
2. **Other orders.** Lemmas 1–3 hold for every n with 330|n. This packet makes no claim for orders at which |P| can have an odd prime factor: for example when 9|n, 25|n or 121|n, or when n has prime factors outside {2,3,5,7,11}. Section 5 uses that 7 exactly divides n, that the primes 3, 5 and 11 exactly divide n, and that n has no other odd prime.
3. **Imports.** The deep inputs are (I1) and (I2). Both are classical, cited from Łaba–Londner, and not re-proved here. The border theorem is reconstructed in §2. T2 is not used.
4. **No solver.** No SAT or UNSAT outcome is used. The arc-consistency exploration mentioned in §0 is not a premise.

## 7. Exact finite checks

Checker: `frontier-20261029-2310-family-complete-no-go-check.py`, SHA256 `63e36a43da435a4d699c4cee9ee7fe55d938bb446ac4e73ed0d242f6511c67a9`, 202 LF / 6,842 bytes. It was executed by `exec` of exactly those bytes in the owner eval kernel on 2026-10-29, finishing before 08:44 PDT, in 108.88 s. Every assertion passed and the output was `"result": "PASS"`. It uses only Python integers, `math.gcd` and finite loops. It verifies none of the imports and none of the all-k written arguments. It checks:

1. The anchor differences: the odd A-differences are {3,5,11}, the odd Y-differences are {1,7,13}, and the witnesses are those quoted in §3.
2. The gcd facts of Lemma 1 and §3 for n=1155·2^K, K=1,…,40. It also checks that 7 ∉ Div(A), so Lemma 1 cannot force 7 into |Q|.
3. The forbidden odd gcds of Lemma 2, by enumerating the divisors of 1155. For |P| a power of 2 they are the 14 divisors sharing a prime with 165. For |P|=7·2^a they are exactly {3,5,11,15,33,55,165}, which is (S1).
4. Lemma 3's class-6 arithmetic, on representatives of both parities.
5. That steps ±3, ±5 reach all of Z_165, as used in (S4).
6. The two gcd identities of (S6), over all residues mod 1155: gcd(7x,1155) = 7·gcd(x,165); and gcd(hy,1155)=7h whenever 7|y and gcd(y,165)|h|165.
7. Lemma H as a control, exhaustively over every E/O partition of Z_165 that is g-periodic for g∈{3,5,11,15}: 6, 30, 2,046 and 32,766 partitions respectively, all connected. It also checks that the period-165 partition E={0} is disconnected, so the restriction of Lemma H to proper periods is necessary. (Lemma H is proved in writing for every proper period.)
8. The anchor fibres and residues used in (S4), (S5) and (S9).
9. The arithmetic of (S9): gcd(8−p₀, n) = 1 for odd p₀≡0 (mod 1155), on a bounded set of K and p₀.
10. A non-vacuity control. Without anchors, every cardinality split |P| ∈ {2^a, 7·2^a} tiles Z_{1155·2^K} for K≤4 (28 explicit interval tilings).
11. A positive control of (I1) and (I2): on all tilings of Z_12 and Z_18 with 0 in both factors (192 and 1,188 ordered pairs), Sands' criterion agrees with direct tiling, and every dilation by an r coprime to |P| tiles.

## 8. What a reviewer must reconstruct

1. §2, or else acceptance of the classical border import.
2. The statements and applicability of (I1) and (I2), together with (D) and (C).
3. Lemmas 1–3.
4. Steps (S1)–(S9) and Lemma H. In particular: the parity transfer in (S3), the two gcd identities in (S6), and the separation-to-connectivity step in (S7).
5. Confirmation that none of the §0 non-premises is used.

**END OF 2310·2^k COMPLETE NO-GO CANDIDATE.**
