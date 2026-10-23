# Referee report: BAL-full v2 read with pre-review erratum 1

I reviewed only the inlined texts (candidate `dffbfea8…a3e1`, erratum `e0f826a2…fcbd`). I did not check hashes, ran nothing, and did not read the frozen-scope file or probe v5. Imports are taken at the scopes recorded in the supplied verdicts, and I did not re-audit their internals. Source-access limits of the classical imports (Savchev–Chen/index-one, EGZ) are not counted as gaps.

## Verdicts

| | Item | Verdict |
|---|---|---|
| 1 | Lemma BAL-forall | **ACCEPT.** Proof complete; 0 FATAL / 0 MAJOR. |
| 2 | Lemma ROOM | **ACCEPT.** 0 FATAL / 0 MAJOR. |
| 3 | Theorem ROT-ZB+ | **ACCEPT relative to imports**, read with erratum items 2–3. 0 FATAL / 0 MAJOR. |
| 4 | Corollary INV*/OLSON-ZB+ (a), (b) | **ACCEPT relative to imports**, read with erratum item 1. 0 FATAL / 0 MAJOR. |

Every implication I checked closes, so there is no counterexample to supply. The findings below are MINOR wording or scope points and do not touch any stated theorem.

## Verification record

### REALIZE and ZSTRUCT at (S′), checked against their embedded proofs
- **REALIZE never uses κ.**
  - Its jump claim needs only L ≥ p+1, odd positive coefficients and W ≤ 2p−1.
  - X_i ≥ L−n ≥ p+1−n gives W ≥ 2p+1 when n = 1.
  - For 2 ≤ n ≤ p−1 it gives W ≥ (n+1)(p+1−n)+n ≥ 2p+n.
  - For n ≥ p it gives W ≥ 3p.
  - So REALIZE holds for every index-<1 generator, not only an SC0-chosen one.
- **Setting facts.**
  - Y′ is zero-sum-free because Z is longest.
  - L ≥ 2p−k ≥ p+1 needs t ≤ κ (from the assumed S1) and k ≤ p−1.
  - m−slack ≥ 2L−2p+1+h ≥ 3 needs only L ≥ p+1.
- **ZSTRUCT.**
  - If r ∈ [3,W], the REALIZE swap lengthens Z.
  - If r ≥ W+1, then s ≤ slack < m, and g^s·z gives s ≤ 2t−1.
  - n− ≥ 1 for t ≥ 1 needs only κ < p.
- In ZR, κ ≤ (p−1)/2 entered only through S1(a) and EBOUND's 2t−1 ≤ p−2. BAL-full assumes S1. ROOM correctly cites s_i ≤ slack ≤ k−1 ≤ p−2 instead of 2t−1, which fails once κ > (p−1)/2.
- **Conclusion: the extension to (S′) is valid.**

### BAL-forall
- **P and mass.** Every coefficient on P is ≥ 1, so mass is additive and ≥ 0. Also mass(P) = e′ and A(P) = W+n+.
- **(F).** It realizes:
  - 0 (empty selection);
  - 1 (since m ≥ 3);
  - every value in [2,W] (REALIZE);
  - every value in [W+1, W+n+] (all of Y′ plus some g's of Z).
  - Together that is all of [0, W+n+].
- **j ≥ 1.** We have S(N) ≥ 0, S(N) ≡ n+, and 0 ≤ n+ ≤ 2κ ≤ 2p−2. So S(N) = n+ + 2pj with j ≥ 0, and unbalanced means j ≥ 1. This needs κ < p, which (S′) assumes.
- **(Lo).** There are exactly m+n+ copies of g in Y: an N-term −s·g equals g only if s = 2p−1 > slack. These copies are disjoint from N0, so f(N0) ≤ 2t.
- **(Hi).**
  - v lies in [0, W+n+] exactly when 2p−W ≤ S(N0) ≤ 2p+n+.
  - The exponent is −(S(N)−S(N0)) + v = 2p(1−j).
  - N−N0 and X are disjoint occurrence sets.
  - |X| ≥ v−e′.
  - The bound "length ≤ 2t" holds even for an empty selection.
  - Hence f(N0) ≥ 2p−e′.
- **Walk.**
  - Since S(N) ≥ 2p+n+ > m+n+, we get 0 ≤ i* < n−.
  - The first crossing lands in the (Hi) window. Lower end: m+n+ +1 ≥ 2p−W, because W+m ≥ 2L+h ≥ 2p+2. Upper end: at most 2p−1+n+−(W−m).
  - That upper end is < S(N), so N0 ≠ N and the full-N0 case never occurs.
- **Combine.** 2p−e′ ≤ f(N^(i*)) + s + 1 ≤ 2t + 2p − W, so L = W−e′ ≤ 2t.
- **Edge cases.**
  - t = 0: N is empty, so Z is balanced.
  - n+ = 0: the argument runs unchanged. Under L ≥ 2t+1 it shows that t ≥ 1 forces n+ ≥ 1.
  - i* = 0: actually impossible (s₁ ≤ slack < m), and harmless anyway.
- **Quantifiers.** The argument holds for every longest Z (all share length 2t) and every index-<1 generator g of Y−Z. Under 2κ+k ≤ 2p−1, L−2t ≥ 2p−k−2κ ≥ 1.

### ROOM
- **Bound W ≤ 2p−1−n+.**
  - Take Q ⊆ Y′ of weight 2p−n+ ∈ [2,W].
  - Then g^{n+}·Q is a zero-sum of length ≥ 2p−e′.
  - So 2p ≤ 2t+e′ ≤ 2t+2p−1−L, i.e. L ≤ 2t−1, a contradiction.
  - This uses neither balance nor ROT-ZB v2's BAL1/(B). Secs. 0–5 cite nothing from that unreviewed file.
- **Coefficient bounds.**
  - a_i ≤ 1+e′ ≤ k ≤ p−1, and a_i is odd, so a_i ≤ p−2.
  - s_i ≤ slack ≤ k−1 ≤ p−2.
  - Every signed coefficient is odd and lies in [−(p−2), p−2], so there is no Y(0) = p·g.
- **E identity.** Balance gives E = e′+n+−n−. With e′ ≤ k−1−2κ+n−, this gives E ≤ k−1−2κ+n+ ≤ k−1.

### ROT-ZB+
- **Length.** F = 2p−2−2κ̂+k gives R = 2p+2κ̂−k.
- **Range of κ̂.**
  - κ̂ ≤ min(k−1, (2p−1−k)/2), using DAV for k ≥ 2.
  - That minimum is ≤ (2p−2)/3, and κ̂ is an integer, so κ̂ ≤ ⌊2p/3⌋.
  - S1-sharp therefore gives (S1), and (S′) holds.
- **SHgen hypotheses.**
  - (H): 2H = 2p−2−2κ̂ ≥ k−1 ≥ E, exactly because 2κ̂+k ≤ 2p−1.
  - (K): η+a_max ≤ E+2 ≤ k+1 ≤ 2p−k−1, using k ≤ p−1.
  - SHgen-E caller (erratum 3): o_F(u°) ≤ k ≤ p−1. V3 discharge is as in the ZR verdict.
- **No hidden κ̂ restriction.** No import has κ̂ ≤ (p−1)/2 in its recorded scope. SHgen's accepted hypotheses are exactly (H) and (K). The S1-sharp verdict already runs the SHgen-based ZX criterion up to κ̂ ≤ (2p−2)/3.
- **Conclusion.** E = 0 forces every coefficient to be ±1, so all rotations lie in {ρ_c, ρ_−c} with c ≠ 0.
- **Erratum item 5 is correct.** ZR cells satisfy 2κ̂+k ≤ 2p−2, so ROT-ZB+ contains ROT-ZR.

### Corollary
- **Restated condition.** F ≥ 2o−1 is equivalent to 2κ(w)+o ≤ 2p−1, since F ≡ o (mod 2).
- **Cases.** These cover every admissible normal form, so the existential reading of "some normal form" causes no problem:
  - k = 1: K1.
  - k ≥ 2, κ̂ = 0: K01.
  - k ≥ 2, κ̂ ≥ 1: 2κ̂+k ≤ 2κ(w)+o ≤ 2p−1, so ROT-ZB+ applies.
- **Vacuous cases.**
  - F = 0: apply EGZ(n = p) twice to the 4p−2 ≥ 3p−1 commuting rotations (the RUNS m1 form). This gives an identity 2p-subword, so no such avoider exists.
  - o_F = 0 with F ≥ 1: the only possible terminal form is the single even block, which the imported normal form excludes.
  - The source of k ≥ 1 is therefore exactly as stated in erratum item 1.
- **REFL.** Restricted REFL is applied to the original word, with o ≤ p−1 ≤ p.
- **Deletion ledger for (b).**
  - Case 1: needs o ≤ 2p−3, which holds.
  - Case 2 gives (o−1, F−1): F−1 ≥ 2(o−1), so the condition is preserved.
  - Case 3 gives (o or o−2, F): preserved.
  - o stays ≤ p−1 throughout, and RGR-LONG closes the argument.

## Findings

**FATAL:** none. **MAJOR:** none.

**MINOR**

1. **Erratum 1 item 4, and Sec. 6 bullet 2: residual omits terminal k ≥ p+1.**
   - The terminal "rotation residual" leaves out cells with terminal k ≥ p+1. Every cited criterion needs k ≤ p, and these cells occur whenever o_F ≥ p+1.
   - The sentence also mixes the o_F ≤ p−1 scope with the k = p cells.
   - **Repair:** write "within terminal k ≤ p the rotation residual becomes …; terminal k ≥ p+1 (which forces o_F ≥ p+1) also remains open for ROT."
   - Also add: a word is residual only if *every* admissible normal form lies in a residual cell (ZX overlay 2).

2. **Sec. 2 Remark (ii): the example is outside (S′).**
   - At p = 7, Y = g⁹(−5g)³ has longest zero-sum g⁵(−5g), of length 6.
   - (S1) then needs κ ≥ 3, so R = 12 forces k = 8 > p−1.
   - Removing that longest zero-sum leaves L = 6 < p+1.
   - **Repair:** add "(outside (S′); it only shows that 'longest' is needed)".

3. **Sec. 7, consistency bullet: "as Lemma BAL-forall predicts" overstates.**
   - The lemma predicts balance only when L ≥ 2t+1.
   - **Repair:** say "consistent with", or record that every probed item had L ≥ 2t+1. This bullet is not a premise.

4. **Sec. 6 bullet 1: parity.** Since F ≡ o_F, the p = 31, o_F = 30 bound is effectively F ≥ 60, not 59. Cosmetic; not a premise.

## Parent integration notes (not defects)

- **Record the extension explicitly.** REALIZE and ZSTRUCT are used through their proofs at (S′) and for an arbitrary index-<1 generator. That goes beyond the Setting (S) statements accepted in the ZR verdict. This report verifies the extension.
- **Optional restatement of ROOM.** The W-bound in ROOM does not use balance; only the E identity does. The statement could say so.
- **ZB+ contains the uniform ZR2 and ZR3 corollaries.**
  - ZR2: F−o ≥ 2p−6 implies F ≥ 2o−1 whenever o ≤ 2p−5.
  - ZR3: F−o ≥ 2p−8 implies F ≥ 2o−1 whenever o ≤ 2p−7.
  - Both side conditions hold for o ≤ p−1, since p ≥ 7.
