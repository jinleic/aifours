# Review v1: wave `f176-shor-165-all-tail-written-proof`

Reviewer: **ReviewF176ShorProof**, a same-harness task agent assigned to the written-proof slice.
Native `/bin/date` observed immediately before composing this file: **Thu Oct 29 08:27:56 PDT 2026**. The post-write clock and this file's SHA-256 are in `reviewer-f176-review-v1-receipt.json`. This file cannot contain its own hash.

Kind: INDEPENDENT_SAME_HARNESS_SCIENTIFIC_REVIEW. It is **not** a human review, an independent-model-family review, a formal or kernel check, or a novelty/SOTA assessment. It grants no adoption, no global completion or no-go, and no novelty.

## 0. Bindings and summary

| item | SHA-256 | bytes | LF | status |
|---|---|---|---|---|
| `manifest-v1.json` | `f2ff789256702497a9992de7ca93e3e1fa3ab6e9da123297a41e03ce7dc82490` | 3160 | – | verified first, read completely |
| candidate `frontier-20261029-165-family-all-q-anchored-border-no-go-v1.md` | `20169ac9e398d9d1ef37d263f9b51d0f9168c095c3e3eb21ade47572822d39c6` | 23071 | 312 | verified, read completely (lines 1–312) |
| author checker `frontier-20261029-165-family-all-q-check.py` | `4c550a5750a822235f20a9862d582082f3427c307f6196575099149638a4538e` | 9099 | 234 | verified, read completely (lines 1–234); **never executed or imported** |

Scoped verdict:

- **FATAL: none. MAJOR: none.**
- I reconstructed every load-bearing step of §§2–7 by hand and found each one correct, **conditional on one imported theorem**: Łaba–Londner (LL) Corollary 6.2. I transcribed its exact hypotheses from the arXiv v3 LaTeX source. They hold for every n = 165·2^t with t ≥ 1 (§3 below).
- **MINOR (4):** m1, a sign typo in the d=5 chain; m2, the immediate Sands exclusion at t=1 is not noted and the t=1 diagnostic is degenerate; m3, the import bundles CM Theorem 1.1(iii) and Tijdeman's theorem and this should be disclosed; m4, the directness step is worded tersely.
- **INCONCLUSIVE (4):** i1, correctness of the deep import itself; i2, the author's execution receipt; i3, the §9 subsumption claims about other packets; i4, the §0 provenance and process statements.
- Independent controls: 50 of 50 pre-stated expectations were observed, with exit status 0 (§6).
- Status of the Theorem and Corollary: **conditionally correct at same-harness level**. If LL Corollary 6.2 holds, there is no anchored tiling P⊕Q = Z_{165·2^t} for any t ≥ 1, and the Corollary follows through §2. This verdict covers only this selected infinite family. It is not an all-order no-go, and the original unrestricted problem is untouched.

## 1. Actual read order and process record

1. 07:28:34 PDT: located the wave directory and computed the manifest SHA-256, which matched `f2ff…2490`. Read the manifest completely.
2. Hash job completed 07:30:42 PDT: candidate and checker SHA-256, bytes and LF all matched the manifest.
3. Read the candidate completely in raw form: lines 1–110, 111–220, 221–312.
4. Read the checker completely in raw form: lines 1–120, 121–234. Read/hash only.
5. Process note, not a mathematical input: the harness required me to read the skill text `independent-snapshot-review`. It describes external-model delegation, which this wave forbids, and was not used.
6. Received two STATUS-ONLY messages from Main, the f162 Olson hold and the f161 hold. I opened none of the affected materials and consumed nothing from them.
7. After all inputs were read, I read the named primary sources:
   - LL arXiv:2106.14042v3 through the arXiv abstract page and the converted PDF text.
   - The LL v3 e-print LaTeX source, fetched into memory only (07:48:58 PDT) and never written to disk. Tarball SHA-256 `e525bb0ade3be9d6fff3dc59b8a0ae077a2783c420c1cbf09bdefbaa26b71378` (354,605 B); member `T2-general-revised-2022-03.tex` SHA-256 `5628d55968060c664d1ea12951af6a65ebf5b6fb9e1171b367c46d970e76c3bb` (158,997 B).
   - Cordero arXiv:2301.13566v1, abstract and converted PDF text, p. 3, Theorem 1.1.
8. Reconstructed §§2–7 by hand.
9. Ran reviewer-only in-memory prototypes to design the controls (see deviation d3).
10. Wrote `reviewer-f176-controls-v1.py` and made one clarity-only edit to the R5h expression before the single official run (08:23:12–08:25:54 PDT, exit 0).
11. Wrote this file.

**Not opened:** Q55/f128, f157 and its disposition, any `*fibre*` packet, the 2310-family and 165-family odd-tail packets (`b618…`, `fce2…`, `33c6…`, `fe70…`), any order-660, 1320 or 2640 branch packet, `owner-20261029-unfrozen-math-frontier-v1.json`, and any HELD/ZERO item. I used no Git, web search, external model or paid API, made no author contact, and deleted nothing.

## 2. Source transcriptions

LL quotations are verbatim from the v3 LaTeX source, with macros kept. Page numbers come from the page markers of the converted v3 PDF and match the candidate's citations.

**LL Theorem 1.1 (p. 3, `\label{CM-thm}`).** "Let $S_A$ be the set of prime powers $p^\alpha$ such that $\Phi_{p^\alpha}(X)$ divides $A(X)$. Consider the following conditions. (T1) $A(1)=\prod_{s\in S_A}\Phi_s(1)$, (T2) if $s_1,\dots,s_k\in S_A$ are powers of different primes, then $\Phi_{s_1\dots s_k}(X)$ divides $A(X)$. Then: • if $A$ satisfies (T1), (T2), then $A$ tiles $\ZZ$; • if $A$ tiles $\ZZ$ then (T1) holds; • if $A$ tiles $\ZZ$ and $|A|$ has at most two distinct prime factors, then (T2) holds."

**LL Definition 2.4 and Theorem 2.5 (p. 10, `\label{thm-sands}`).** "$\Div(A)=\Div_M(A):=\{(a-a',M):\ a,a'\in A\}$." / "**(Divisor exclusion; Sands)** If $A,B\subset \ZZ_M$ are sets, then $A\oplus B=\ZZ_M$ if and only if $|A|\,|B|=M$ and $\Div(A) \cap \Div(B)=\{M\}$."

**LL Theorem 6.1 (p. 25, `\label{subgroup-reduction}`).** "(Subgroup reduction) ([CM, Lemma 2.5]; see also [dutkay-kraus, Theorem 4.4]) Assume that $ A\oplus B=\ZZ_M $, where $M=\prod_{i=1}^K p_i^{n_i}$, and that: (i) there exists an $i\in\{1,\dots,K\}$ such that $A\subset p_i\ZZ_M$, (ii) (T2) holds for both $A'$ and $B'$ in any tiling $A'\oplus B'=\ZZ_{N_i} $, where $N_i=M/p_i$, $|A'|=|A|$, and $|B'|=|B|/p_i$. Then $ A $ and $ B $ satisfy (T2)."

**LL Corollary 6.2 (p. 26, `\label{almostsquarefree}`).** "Let $ A\oplus B=\ZZ_M $, where $M=p_1^{n_1}p_2^{n_2}p_3^{n_3} \dots p_K^{n_K}$. Assume that for each $i\geq 3$, the prime factor $p_i$ divides at most one of $|A|$ and $|B|$. (This happens e.g., if $n_i=1$ for $i\not\in\{1,2\}$). Then both $A$ and $B$ satisfy (T2)."

The source proof, verbatim apart from macro expansion:

> "This is not stated explicitly in [CM], but it follows by a very similar argument. (See also [Tao-blog], [dutkay-kraus], [shi].) We proceed by induction in the number of prime factors. If K=2 and M=p_1^{n_1}p_2^{n_2}, this is Theorem 1.1. Suppose that K≥3 and that (T2) holds for both A' and B' in any tiling A'⊕B'=Z_{M/p_K}. By the assumption of the lemma, at least one of |A| and |B| is not divisible by p_K. Assume without loss of generality that p_K∤|A|. By Tijdeman's theorem ([Tij, Theorem 1]; see also [CM, Lemma 2.2]), Ã⊕B=Z_M is again a tiling, where Ã(X)=A(X^{p_K}). We have Ã⊂p_K Z_M, so that we may apply Theorem 6.1 to conclude that Ã and B satisfy (T2). By (6.1), this also means that A satisfies (T2), since the (T2) condition for A involves only cyclotomic polynomials Φ_s with (s,p_K)=1."

**LL §2.1 notation.** "We also reserve $K$ for the number of the distinct prime divisors of $M$, and use $p_1,\dots,p_K$ to denote those divisors, so that $M=\prod_{i=1}^K p_i^{n_i}$, where $p_1,\dots,p_K$ are distinct primes and $n_1,\dots,n_K\in\NN$." No ordering of the primes is imposed. The introduction (p. 4) states the same result for the case where "at most two of $p_1,\dots,p_K$ divide both $|A|$ and $|B|$".

**Cordero arXiv:2301.13566v1, p. 3, Theorem 1.1.** The set-builder braces were partly lost in the PDF text extraction. The statement reads: "If M is a finite maximal code such that b, a^n ∈ M then the ordered pair ({k, a^k b^+ ∈ M}, {k, b^+ a^k ∈ M}) is a factorization of size n." The paper attributes it to Restivo–Salemi–Sportelli [RSS89]. "Factorization of size n" means: for all k ∈ [n] there is a unique (p,q) ∈ P×Q with k = p+q in Z_n.

The candidate's paraphrases of LL Theorem 1.1, Theorem 2.5 and Corollary 6.2 are faithful. Its P/Q definitions are the mod-n reductions of Cordero's sets. The candidate does not rely on that citation: it reconstructs the border from UD and factor-completeness alone, and I verified that reconstruction (§4).

## 3. Import audit at n = 165·2^t (t ≥ 1)

**Which primes divide both cardinalities.** n = 2^t·3·5·11 and |P||Q| = n.

- Each of 3, 5 and 11 occurs to the first power, so each divides exactly one of |P| and |Q|.
- 2 divides both exactly when a ≥ 1 and b ≥ 1, which needs t ≥ 2.

So the set of primes dividing both cardinalities is either ∅ or {2}.

**Hypothesis check.** The candidate labels (p₁,p₂,p₃,p₄) = (2,3,5,11). Then for i ≥ 3 we have p_i ∈ {5,11} with n_i = 1. This is LL's own parenthetical case, so the hypothesis holds for every t. Because LL's notation imposes no ordering, any labeling with 2 ∈ {p₁,p₂} also works, and the introduction's weaker form ("at most two primes divide both") holds with room to spare. **PASS.**

**Why the T2 conclusion applies.** LL's proof specializes to this chain:

1. **Remove 11.** The factor F ∈ {P,Q} with 11 ∤ |F| is dilated: 11F ⊕ (the other factor) = Z_n by Tijdeman's theorem. Here r = 11 is coprime to |F| but **not** a unit mod n, so this is Tijdeman's genuine theorem and not the elementary unit-multiplier lemma. Since 11F ⊂ 11Z_n, Theorem 6.1 reduces the question to tilings of Z_{2^t·15} with cardinalities (|F|, |other|/11).
2. **Remove 5.** The same step reduces to Z_{2^t·3}.
3. **Base case.** Every factor size divides 2^t·3, which has two primes, so CM Theorem 1.1(iii) gives T2.

The cardinality pattern is preserved at each level, because Theorem 6.1(ii) fixes |A′| = |A| and |B′| = |B|/p_i, and 5 has exponent 1 in 2^t·15. The known looseness of "induction in the number of prime factors" when n_K ≥ 2 does not arise, because each removed prime (11, then 5) has exponent 1.

T2 transfers from 11F back to F by LL (6.1): for (s,11) = 1, Φ_s | F(X^{11}) ⇔ Φ_s | F(X). In addition, S_F contains no power of 11, since Φ₁₁ | F would force 11 | F(1) = |F|.

**What the candidate uses.** Only two things:

- (i) Each prime h ∈ {3,5,11} dividing |Q| (resp. |P|) lies in S_Q (resp. S_P). The candidate proves this elementarily in Lemma 2(a).
- (ii) T2 then gives Φ_m | Q for every m | e with m > 1 (resp. for P and m | d).

All indices involved divide n, so the choice of representatives in [0,n) does not matter.

**Classification.**

- **Deep, imported, not re-proved here:** CM Theorem 1.1(iii); Tijdeman [Tij, Theorem 1]; and LL Theorem 6.1 / CM Lemma 2.5. I read the Theorem 6.1 proof but did not re-verify it line by line.
- LL's own proof of Corollary 6.2 is about one paragraph long.
- The peer-review or publication status of v3 was not checked, since web search was not allowed.

**Verdict.** Hypotheses PASS and the import is correctly applied. Correctness of the import itself is **INCONCLUSIVE** (i1, outside this slice).

## 4. Claim-by-claim verdicts

| Claim | What I independently reconstructed | Verdict |
|---|---|---|
| §2 pure-a atom exists and is unique; b^k ∉ D for k ≥ 2 | a^{2L+1} is embedded, and its middle-a atom is pure-a. (a^u,a^v) and (a^v,a^u) are distinct lists for u ≠ v. (b^k) differs from (b,…,b). | VERIFIED |
| §2 anchors | 0 ∈ P via b ∈ D (i=0, k=1); 3, 8, 11 ∈ P via a³b, a⁸b, a¹¹b; Y ⊆ Q via b, ba, ba⁷, ba¹³, ba¹⁴. The anchors are distinct mod n because n ≥ 330. | VERIFIED |
| §2 directness | Identify atoms by position: the atom covering the last b of b^H is v_t (l_t ≥ 1), and the atom covering the first right b is u_t (k_t ≥ 1). Equal lists therefore give equal (i,j), so distinct residue pairs with equal sum give two factorizations of b^H a^G b^K. The edge cases j_t = 0 or i_t = 0 (border atom = b) are covered, and G > i_t+j_t makes the a^n count nonnegative. | VERIFIED; wording note m4 |
| §2 coverage | Atom length is ≤ L and g > L. The atom covering the last left b starts in the guard and ends before the right guard, so it is b^l a^j; symmetrically the other is a^i b^k. Interior atoms are pure-a, hence a^n, so g ≡ i+j. | VERIFIED |
| §2 conclusion P⊕Q = Z_n, \|P\|\|Q\| = n | Uses only finiteness, UD, factor-completeness, b ∈ D, and a^n as the pure-a atom. | VERIFIED |
| §3 Sands statement | Matches LL Thm 2.5: Div∩Div = {M} is equivalent to "no two nonzero differences have equal gcd". | VERIFIED (source) |
| §3 Sands proof sketch | Solve w(p−p′) ≡ q−q′ mod n/g and lift to a unit mod n, using the surjection (Z/n)^× → (Z/(n/g))^×. wP ⊕ Q holds by the cyclotomic criterion, since ζ ↦ ζ^w preserves the order. The collision wp+q′ ≡ wp′+q with wp ≠ wp′ follows. | VERIFIED (elementary) |
| Lemma 1 | Trivial. Also checked exhaustively for t ≤ 6 (R1d). | VERIFIED |
| P-differences have gcd 3, 5, 11; Q has gcd 1 | Holds for every t ≥ 1 (R1c, checked to t=8). | VERIFIED |
| (SQ), (SP) | Necessary consequences of Sands that use only odd differences, so they depend only on residues mod 330. The type rules agree with actual gcds (R1e, t ≤ 4). | VERIFIED |
| Lemma 2: de = 165, gcd = 1 | Squarefree 165. | VERIFIED |
| Lemma 2(a) | Φ_p divides 1+…+X^{n−1} and hence P·Q; Φ_p is prime in Z[X]; monic division gives p \| \|factor\|; and p divides exactly one cardinality. | VERIFIED |
| Lemma 2(b) | Given T2, Φ_m \| Q for all m \| e with m > 1. Their product is (X^e−1)/(X−1). Reduction mod X^e−1 then gives c·(1+…+X^{e−1}) with c = \|Q\|/e = 2^b ≥ 1. | VERIFIED given T2 |
| Lemma 3 table and exclusion | All 12 printed differences recomputed. Each is coprime to its class primes, and the third prime would have to divide 8. Checked at type level mod 330 (R2a, R2b) and at every residue with actual gcd for t = 1..6 (R2e). | VERIFIED |
| d ∈ {1,3,5,11} exhaustive | The odd divisors of 165 with at most one prime factor (R2c); a two-prime d covers a forbidden class by Lemma 2(b). | VERIFIED |
| Rule (R) | Two fixed primes and distinct classes give k ≤ 1; the count is k + [f \| x−x′]. | VERIFIED |
| §6 d=1 | 2−13 = −11 (11 only); 167−14 = 153 = 3²·17 (3 only). Class 2 domain is empty (R3a). | VERIFIED |
| §6 d=3 | All 15 bracketed rows, k values, mod-3 conclusions and the two-line chain (R3b, R3c, R3f). | VERIFIED |
| §6 d=5 | All rows and the four-step chain (R3d, R3e, R3f). Step 4 prints "[11, k=1]" but r−y = 4−15 = −11. k and the conclusion are unaffected. | VERIFIED; **m1** |
| §7 anchor table and g | (r₃,r₅), parity and mod-11 values for 0, 1, 7, 13, 14 (R4e). | VERIFIED |
| Lemma 4 Steps 1–6 | Hand-checked each step, including "at least two anchors outside the class" in Step 1 and the four sub-cases of Step 5. Finite content mirrored in R4f. The global backtracking has a unique one-per-class consistent selection, and each type that extends is exactly the Lemma 4 type (R3g, R4b, R4c). | VERIFIED |
| Lemma 5 | Counts: 2^{b+1} even, 2^b odd, 0 otherwise. CRT 55·(z mod 2)+56·(z mod 55). W ≡ (2+X⁵⁵)Y(X⁵⁶) mod X¹¹⁰−1. 2+ξ⁵⁵ ∈ {1,3}. ord ξ⁵⁶ is the odd part of ord ξ, which is 11 or 55. Degrees: 14 < 40 = φ(55), and the reduction 1+X+X²+X³+X⁷ has degree 7 < 10 (R5a–R5f, R5h). | VERIFIED |
| Lemma 6 | m \| n for every t ≥ 1; P(ξ)Q(ξ) = 0; four distinct irreducible factors; Φ₁₁Φ₂₂Φ₅₅Φ₁₁₀ = Σ_{k≤10} X^{10k} (R5g); 10-periodicity of the fold. Also observed on 1024 genuine complements at n = 660 and on the found complements at t = 3, 4 (R9b4, R9d). | VERIFIED |
| Conclusion for d = 11 | 11 ∈ P and 11 ≡ 1 (mod 10) give P₁₁₀(1) ≥ 1. Such an x is odd. x−0 ≡ 1 and x−8 ≡ −7 (mod 110) are coprime to 5·11. (SP) then forces 3 \| x and 3 \| x−8. The types ≡ 1 mod 110 are {1, 111, 221}: only 111 passes against 0, only 221 against 8, and none passes both (R6a, R6b). | VERIFIED |
| §1 Theorem | All four d-cases are impossible. | **CONDITIONALLY VERIFIED** (given LL Cor. 6.2) |
| §1 Corollary | §2 plus the Theorem. | **CONDITIONALLY VERIFIED** |
| §8 finite checks | Recomputed independently; see §7. The arc-consistency algorithmic claim was not recomputed. The t=1 diagnostic is degenerate. | VERIFIED except as listed; **m2** |
| §8 author execution receipt | Not executed, per contract. | **INCONCLUSIVE (i2)** |
| §9 Q-side control at 2640 | All stated properties hold (R8a). The set is also, beyond the candidate's claim, an actual tile of Z₂₆₄₀: a complement of size 176 was found and verified (R8c). No complement contains A (R8b). | VERIFIED |
| §9 P-side type control | Each single head constraint is satisfiable; the conjunction is not (R6). | VERIFIED |
| §9 "subsumes" other candidates | Would require opening non-premises, which is forbidden. | **INCONCLUSIVE (i3)**, not assessed |
| §0 non-premise use (review gate 8) | §§1–7 cite and use no non-premise packet. Only the three named imports and elementary arguments appear. | VERIFIED (textual) |
| §0 provenance and process history | Not verifiable by a reviewer. | **INCONCLUSIVE (i4)** |
| "This is the only deep import" | True as a citation unit, but Cor. 6.2 bundles CM Thm 1.1(iii), Tijdeman's theorem (with the non-unit multipliers 11 and 5) and the subgroup reduction. The candidate cites arXiv v3 only. | **m3** (disclosure) |

## 5. Boundary audit (t = 1, zeros, equality cases)

- **t = 1 (n = 330).** Every step holds: n is even so parity is defined; 110 | 330; a+b = 1; and the anchors are distinct. Independently, Div₃₃₀(A) ∩ Div₃₃₀(Y) = {2}, because gcd(8,330) = gcd(14,330) = 2. Sands therefore excludes t = 1 immediately, without T2 (R1a). For t = 2..8 this intersection is empty (R1b), so the full argument is needed exactly for t ≥ 2. The candidate does not mention the shortcut. Its t=1 "actual screens" of §8 item 6 are degenerate: the P-screen of size 6 contains none of 0, 3, 8, 11, and the Q-screen also omits some tails (R7c). This is **m2**. It is presentational only, since the written proof covers t = 1.
- **t = 0** (n odd, parity undefined) is correctly excluded by the candidate.
- **a = 0 or b = 0** (an odd cardinality, including the "odd-tail" case |Q| = 15): Lemma 2(b) gives 2⁰ = 1 element per class, Lemma 5 gives weights 2/1, and Lemmas 6 and 3 are unchanged.
- **k = 2** is excluded by "distinct classes", and **x = x′** is excluded by opposite parity. Same-class pairs never constrain at type level, because both fixed primes divide the difference.
- **Zeros.** 2+ξ⁵⁵ ∈ {1,3}. Y(β) ≠ 0 at orders 11 and 55 by strict degree gaps (7 < 10 and 14 < 40). Q(ξ) does vanish at orders 5 and 10, which is exactly why Lemma 5 requires 11 | ord ξ (R5d).
- **Representatives.** Every cyclotomic index used divides n, so masks taken mod X^n−1 are well defined.
- **Final step.** 11 mod 110 = 11 ≠ 1, so the forced element x is a new element, not the anchor 11.

## 6. Independent controls (bounded, exact, reviewer-authored)

**Script.** `reviewer-f176-controls-v1.py`: SHA-256 `01742b312af081bd27dafb2f5b7211604b51d8171c6d8563cfbe5a1276ee27e2`, 27,281 bytes, 617 LF. It uses only the standard library and does not import or execute author code. It reads the checker's bytes for hashing only (R0).

**Output.** `reviewer-f176-controls-v1-output.json`: SHA-256 `1e28e6c7d3fbb2869dd0c0b961acd571fca6aecff5e66fa704980250e6e623e5`, 15,698 bytes, 1035 LF.

**Receipt.** `/bin/date` before: Thu Oct 29 08:23:12 PDT 2026. Interpreter `/opt/homebrew/bin/python3` (3.14.3), cwd = wave directory, stdin = /dev/null. **Exit status 0.** Stdout: `{"elapsed_s": 161.902, "failed": [], "n_checks": 50, "result": "ALL_EXPECTATIONS_OBSERVED"}`. `/bin/date` after: Thu Oct 29 08:25:54 PDT 2026.

| Block | Method, independent of the author's | Intended positive / negative outcome | Observed |
|---|---|---|---|
| R0 | SHA-256 of both inputs at run time | binding | match |
| R1 | Div_n(A), Div_n(Y) for t=1..8; Lemma 1 exhaustive for t ≤ 6; type rules vs actual gcd for t ≤ 4 | collision {2} only at t=1 / none for t ≥ 2 | t=1: DivA={2,3,5,11}, DivY={1,2,6}; t=2: {3,4,5,11} / {1,2,6,12}; t≥3: {3,5,8,11} / {1,2,6,12} |
| R2 | Lemma 3 at type level and with actual gcd for every residue, t=1..6 | full A excludes all three classes / dropping any single head re-admits one type in each class | as intended |
| R3 | domains, states and printed brackets; **global backtracking** over all one-per-class selections | e=165, 55, 33 give 0 selections and e=15 gives exactly 1 / dropping tail 0 or 14 re-admits ≥1000 (capped) selections for e=55 and 33; dropping any tail gives >1 selection for e=15 | as intended; the only bracket mismatch is m1. Dropping 1, 7 or 13 alone leaves e=55/33 contradictory (overdetermined) and gives 7 selections for e=15 |
| R4 | e=15 domain sizes; per-type extendability; Lemma 4 prediction; step mirrors | unique S = {0,1,7,13,14,55,56,62,68,110,234,276,282,288,289} | sizes [18,9,2,2,1,8,2,9,2,8,1,2,2,9,18]; S unique |
| R5 | my own exact cyclotomic division (Φ_k by exact quotient of X^k−1) | W nonzero mod Φ₁₁, Φ₂₂, Φ₅₅, Φ₁₁₀ / zero exactly at m = 5, 10 | as intended; identity and product verified |
| R6 | final certificate | none of {1,111,221} passes both 0 and 8 / dropping 8 re-admits 111, dropping 0 re-admits 221, dropping 3 changes nothing | as intended |
| R7 | recomputed the §8 screens | sizes P 6, 42, 112, 224, 448, 896; Q 47, 118, 286, 658, 1316, 2632 | match; anchors fail the screens only at t=1 |
| R8 | the 2640 control set; exact cover (Algorithm X, MRV) | no complement ⊇ A / a genuine complement containing 0 exists | none (25 nodes) / found, \|P\| = 176, verified |
| R9a | n=330, Q forced to S | anchored none / unanchored found | as intended |
| R9b | **n=660 exhaustive: all 2¹⁰ = 1024 Lemma-4 tail sets with b=0**, under 10 forced-head variants | A: 1024 none / {0}, {0,3}, {0,5}: 1024 found | A, {0,8}, {0,11}, {0,3,8}, {0,3,11}, {0,8,11}, {3,8,11}: 1024 none each; {0}, {0,3}, {0,5}: 1024 found each; no caps; max 321 nodes |
| R9b4 | the 1024 found tilings at n=660 | consistency with the imports | all 1024 satisfy: tiling; Lemma-6 10-periodicity of P mod 110; Sands exclusion; T2 for P and for Q; uniformity mod odd part; Tijdeman dilations (r = 3,5,7,9,13 on P; r = 2,4,8,11,22 on Q) |
| R9c | n=660, b=1: the unique tail set S∪(S+330) | anchored none / unanchored found | as intended |
| R9d | seeded random samples: t=3 (b=0:32, b=1:8, b=2:4) and t=4 (b=0:8, b=1:4, b=2:2) | no complement ⊇ A in any sample | 0 found in all 58 samples; found complements verified and 10-periodic |

**What the controls establish:**

- All load-bearing finite tables (§7 below).
- An exhaustive exact check, independent of the cyclotomic argument, that **at t = 2 no Lemma-4 tail set has an anchored complement**. b=0 is exhaustive, and b=1 is a single set. b=2 is impossible at n=660, since each type mod 330 has only two lifts.
- The same holds at t = 1 (Q = S, exhaustive).
- At t = 3 and 4 the same holds for bounded samples only.

**What the controls do not establish:**

- They do not test T2 or the rest of the deep import. R9b4 shows only consistency on 1024 genuine tilings.
- R9 is conditional on Lemma 4, which itself relies on T2.
- Because the obstruction at n=660 is overdetermined ({0,8} ⊆ P or {0,11} ⊆ P alone already admits no complement), exact cover cannot isolate the candidate's specific route. That route is checked by R5 and R6.
- No T2-free search was done. In particular there was no unconditional exhaustive search over all (|P|,|Q|) at n=660.
- t=4 with b=3 was not run because of cost.
- Prototype-only observation, **not part of the receipted run**: 1020 of the 1024 tail sets at n=660 have 4 = gcd(8,660) in Div(Q), which explains the {0,8} result by Sands.

## 7. Finite arithmetic: audited and not audited

**Audited by hand and by independent code:**

- the gcd values of §3;
- the Lemma 3 table (12 differences);
- d=1 (2 rows);
- d=3 (15 bracketed comparisons, including the 2 chain rows);
- d=5 (20 bracketed comparisons, including the 4 chain rows);
- the §7 anchor table and g;
- the finite content of Lemma 4 Steps 1–6;
- the Lemma 5 counts, CRT identity, factorization, orders and degrees;
- the Lemma 6 product identity;
- the final certificate;
- §8 items 1, 2, 4, 5, 6 (including all screen sizes) and the item-3 domain sizes and types;
- the §9 2640 set.

A pairwise (SP)-consistent and Y pairwise (SQ)-consistent: checked by hand (A's opposite-parity differences are 3, 11, 5, 3; Y's are all prime to 165), and for Y also by code through R4d.

**Not audited:**

- (a) §8 item 3's algorithmic claim that *arc consistency alone* reaches exactly the singleton types. Global consistency, which is stronger, was verified instead. Non-load-bearing.
- (b) The author's statement that the checker ran and printed PASS (i2).
- (c) Any arithmetic in non-premise packets (not opened).
- (d) Any finite content internal to LL or CM. None is relied on beyond the imported statements.

## 8. Exact assumptions of this review

- **EA1.** LL Corollary 6.2 (arXiv:2106.14042v3) is correct, together with CM Theorem 1.1(iii), Tijdeman [Tij, Thm 1], and LL Theorem 6.1 / CM Lemma 2.5. None of these were re-proved.
- **EA2.** Standard facts:
  - the cyclotomic tiling criterion (LL (1.1)⇔(1.3));
  - irreducibility of Φ_k over Q;
  - X^k−1 = ∏_{d|k} Φ_d;
  - divisibility by a monic polynomial stays in Z[X].
- **EA3.** The candidate's definitions: UD means unique factorization of atom lists; factor-complete means every word is a factor of some word of D*; D is finite.
- **EA4.** The literal S is taken as printed. Only b ∈ S, the head words a^i b (i ∈ A) and the tail words b a^j (j ∈ Y) are used. I did not compare S against Shor (1985).
- **EA5.** t is an integer ≥ 1.

## 9. Findings

**FATAL:** none.

**MAJOR:** none.

**MINOR:**

- **m1** (§6, d=5, chain step 4): "Against x_15 [11, k=1]" should be [−11, k=1], since r−y = 4−15. k and the conclusion are unchanged. All other 34 brackets are correct (R3f).
- **m2** (§5 boundary, §8 item 6): Sands alone excludes t = 1, because 2 ∈ Div₃₃₀(A) ∩ Div₃₃₀(Y). The candidate does not state this, and its t=1 "actual screen" diagnostics are degenerate without comment: the anchors themselves fail them. No effect on the proof.
- **m3** (§4, §9 "Limits"): the "only deep import" should disclose what Cor. 6.2 bundles: CM Thm 1.1(iii), Tijdeman's theorem with the non-unit multipliers 11 and 5, and the subgroup reduction. It should also note that LL present it as a short corollary of the CM argument and that only arXiv v3 is cited. This changes how much external confidence the import carries, not the logic.
- **m4** (§2, directness): "the positive central a-run therefore identifies both border atoms" is terse. The clean argument is positional (the atoms covering the last left b and the first right b). There is no gap.

**INCONCLUSIVE:**

- **i1:** correctness of the deep import. Its hypotheses are verified (PASS); the theorem itself is not re-proved.
- **i2:** the author's checker execution receipt (not executed).
- **i3:** §9 statements about subsuming f157, the f128 branch, `fe70…` and the branch packets.
- **i4:** §0 provenance and process statements.

**Process observation, not a mathematical finding.** The checker's section comments ("Section 4 (e=165)", "Section 5 (e=55)", "Section 6 (e=33)") do not match the candidate's numbering, where all three are in §6. This is harmless.

## 10. Deviations and process notes

- **d1.** I read the harness skill text `independent-snapshot-review` (external-model procedure) because of the harness rule. It is not an input, and nothing from it was used.
- **d2.** Two Main STATUS-ONLY messages arrived, concerning f162 and f161. No affected material was accessed.
- **d3.** Before the official run I ran reviewer-only in-memory prototypes, with no files written. These included:
  - one exact-cover prototype stopped by the 30 s eval cap;
  - one random-sample prototype interrupted at the 600 s cap while running t=4, b=3, which was then dropped from the official script for cost.

  The official script's R9 expectations had first been observed in these prototypes and were re-run from scratch. Only the official run is evidence. The 1020/1024 Div figure in §6 is prototype-only and is labeled so.
- **d4.** I read the author checker completely, as the manifest requires, before writing my script. R7 reimplements the checker's screen definitions, because the candidate text does not define the screens precisely. R4f mirrors the same six steps. Both are therefore not methodologically independent of the author's checker. R3g/R4b (global backtracking), R5 (my own cyclotomic arithmetic) and R8/R9 (exact cover) use different methods.
- **d5.** I fetched the LL e-print LaTeX tarball into memory, never to disk, to transcribe exact statements. It is the named public primary source arXiv:2106.14042v3. This was a direct read, not a web search.
- **d6.** I made one edit to the control script before its single official run: a clarity rewrite of the R5h exponent with no semantic change. The receipted SHA is that of the final bytes.

## 11. Reviewer artifacts in this wave directory

| artifact | SHA-256 |
|---|---|
| `reviewer-f176-controls-v1.py` | `01742b312af081bd27dafb2f5b7211604b51d8171c6d8563cfbe5a1276ee27e2` |
| `reviewer-f176-controls-v1-output.json` | `1e28e6c7d3fbb2869dd0c0b961acd571fca6aecff5e66fa704980250e6e623e5` |
| `review-v1.md` (this file) | in `reviewer-f176-review-v1-receipt.json` and in the reviewer's final return |

No global completion or no-go, no novelty, and no adoption is granted. Same-harness only.
