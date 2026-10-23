# Referee report: proof-SLZ3-v1 (sha256 `0cfe637f…` as supplied)

**Basis.** I read the five texts as supplied. I did not recompute hashes and used no tools, files or computation. S1-sharp is read through erratum 1; its items A-m1, A-m2, A-m6 and A-m8 are needed by the steps SLZ3 marks "Unchanged". Zeng–Yuan is credit only and plays no role here. `proof-SLZ-EXT-v2.md` and `notes-LS-propagation-v1.md` are not in the packet.

## Verdicts

### (1) Shortest-long bound: ACCEPT-WITH-FIXES, 0 FATAL / 0 MAJOR (MINOR M1–M5, M9, M10)

The theorem is correct for every prime p ≥ 5 and every κ with ⌊2p/3⌋+1 ≤ κ ≤ p−1. This holds relative to S1-sharp (with erratum 1) and the index-one import. I re-derived every reused step in the new range. None of them secretly needs κ ≤ ⌊2p/3⌋ or p ≥ 3δ−1.

**Standing facts.** Write κ0 = ⌊2p/3⌋.
- **R1:** 3κ ≥ 2p+1.
- **R2:** δ = 2κ−p is odd and (p+2)/3 ≤ δ ≤ p−2, so δ ≥ 3.
- **R3:** u = 2κ ≤ 2p−2.
- **H (hypothesis for contradiction):** N ≥ 3κ+2. With R1 this gives N ≥ 2p+3, and parity then gives N ≥ 2p+4.

**Step 1.** Proper nonempty zero-sums of T have length in [l,u]. This uses only the minimality of N (erratum A-m2).
- N ≥ 2p+2 gives D ≤ 2δ−2 and l ≥ p−δ+2.
- H gives l ≥ κ+2 and D ≤ κ−2.

**Step 2.** A nested split gives 2l ≤ |T′| ≤ u, i.e. N ≤ 3κ. This contradicts H.

**Step 3 and the induction.**
- The case split is exhaustive. Either κ−1 = κ0, or κ0+1 ≤ κ−1 ≤ p−2, which is inside the Theorem's range.
- Suppose every proper nonempty zero-sum of T has length ≤ u−2 (this includes the case where there are none). Then T itself satisfies (ZP_{κ−1}): its proper zero-sums are < 2κ, and N > 2p.
- **Base case.** S1-sharp is accepted with no length bound. Applied to T, it bounds every zero-sum of T by 2κ0 < N.
- **Inductive case.** Apply Theorem(κ−1) to T. It gives a shortest (κ−1)-long zero-sum T0 with |T0| ≤ 3κ−2.
  - Since |T0| ≥ 2κ and T satisfies (ZP_{κ−1}), we get |T0| ≥ 2p+1. By parity, |T0| ≥ 2p+2 ≥ 2κ+2.
  - So T0 is a κ-long zero-sum of Y, and N ≤ |T0| ≤ 3κ−2, contradicting H.
- **Hereditary check: clean.**
  - (ZP_{κ−1}) is derived for T only and is never asserted for Y.
  - Minimality of N is used only as "N ≤ |T0|".
  - T0 is never claimed to be shortest in Y.
- Hence Q exists with |Q| = u, and Q′ = T−Q has |Q′| = l ≥ κ+2. Both are minimal. Applying Step 1 to Q′ gives D ≥ 0.

**Step 4.**
- |Q| = p+δ ≥ p+3 ≥ ⌊2p/2⌋+2, which is inside the record's general C_n scope with n = 2p composite.
- ord(a) ≠ 1 (a zero term would be even), ≠ p (all multiples even), ≠ 2 (that forces |Q| = 2). So a is an odd generator g, the coefficients are odd and lie in [1,2p−1], and A_Q = 2p.
- mass(S_Q) = p−δ ≥ 2, so |S_Q| ≤ (p−δ)/2 and m ≥ (p+3δ)/2.
- S_Q ≠ ∅ because u ≠ 2p (R3). This is the essential use of κ ≤ p−1.
- b_min ≤ p−δ+1, and every b ∈ S_Q satisfies b ≤ p−δ−2|S_Q|+3.

**Step 5 (MC).** Independent of κ. The two excluded pairs are exactly the cases where (Q−Q1)W is empty or equals T.

**Step 6.**
- m ≥ D+2 holds because (p+3δ)/2 ≥ 2δ ≥ D+2. This needs only δ ≤ p and D ≤ 2δ−2.
- b0 ≤ m needs only |S_Q| ≥ 3−2δ.
- Both the |Z0| = 1 and |Z0| ≥ 2 contradictions use only D ≤ 2δ−2, m ≥ (p+3δ)/2, the Step 4 bounds, and m−D+1 > 0.
- p ≥ 3δ−1 is never used.

**Step 7.**
- r ∈ [0,D] by Step 6.
- The prefix W is proper because A_W ≤ 2p+D < 4p (D ≤ 2δ−2 ≤ 2p−6).
- r ≠ 0 because Q′ is minimal.
- g^r ⊆ Q because D < m.
- Both MC pairs are legal: W ≠ ∅ and W ≠ Q′; Q−g^s ≠ Q, W⁻ ⊊ Q′, and s ∈ [1, D+1] ⊆ [1, m].
- The output is l ≤ D, i.e. 2l ≤ u, i.e. N ≤ 3κ, contradicting H.

**Step 8.** Independent of κ.
- Q1 = {b_min} is a legal MC pair.
- (8a) uses b_min ≥ 3 and is trivial at t′ = 0.
- (8b) is vacuous at t′ = 0.
- (8c) needs b_min−t′ ≥ 1, which follows from (8a).
- Y_low = ∅ whenever t′ ≤ 2.

**Step 9.**
- l and p are integers with l even, so base = (3l−2p)/2 is an integer.
- 3l−2p ≥ 3κ+6−2p ≥ 7, so base ≥ 4.
- X ≥ 0 gives t′ ≥ base ≥ 4. So every case t′ ≤ 3, including the erratum A-m6 branch, dies at once.
- Two terms of Y above t′ would give X ≥ t′−2 > t′−base.
- From |Y| = l−t′ ≤ (b_min−t′−1)/3 + 1: 3l ≤ b_min+2t′+2 ≤ 3b_min.
- Hence l ≤ b_min ≤ p−δ+1 < l, a contradiction.

### (2) Equivalent proper-long statement: ACCEPT-WITH-FIXES, 0/0 (MINOR M7)

Both directions hold. They use only the fact that (ZP_κ) passes to subsequences.
- **Theorem ⇒ equivalent form.** Apply the Theorem to Y := T. T is a κ-long zero-sum of itself, and the shortest one has length ≤ 3κ+1 < |T|, so it is proper.
- **Equivalent form ⇒ Theorem.** A shortest κ-long zero-sum T of Y is itself a (ZP_κ) zero-sum. If |T| ≥ 3κ+2, a proper long zero-sum of T would be a shorter long zero-sum of Y.

### (3) Sharpness and scope: ACCEPT-WITH-FIXES, 0/0 (MINOR M5, M6, M8, M11)

**p ≡ 1 (mod 3), κ = (2p+1)/3.** Here κ ≤ p−1 because p ≥ 7. The F1 claim is correct:
- Take g an odd generator. Nonempty zero-sums g^i(3g)^j satisfy 0 < i+3j ≤ 4p, so i+3j ∈ {2p, 4p}.
- i+3j = 4p occurs only for F1 itself.
- i+3j = 2p with i ≤ p+3 forces j ≥ (p−1)/3. The length is then 2p−2j ≤ (4p+2)/3 = 2κ.
- So F1 satisfies (ZP_κ), has no proper κ-long zero-sum, and has N = 2p+2 = 3κ+1. The bound is attained, and "3κ+2" in form (2) cannot be lowered.
- Consistency check: F1 has l = (2p+4)/3 and base = 2. So the "+2" in H is exactly what Step 9 needs at this κ.

**p ≡ 2 (mod 3), κ = (2p+2)/3.** The parity rounding is correct:
- N is even, so N ≤ 3κ+1 = 2p+3 gives N ≤ 2p+2. Together with N ≥ 2p+2, this gives N = 2p+2 = 3κ.
- F1 attains this, although the text does not say so. Erratum F1 gives a largest proper length of 2κ0+2 = 2κ.

**Scope of sharpness.** Only κ = κ0+1 is addressed, and the text does not overclaim. The following is my own derivation and is not required for acceptance:
- For κ ≥ κ0+2, the same nine steps close under N ≥ 3κ+1.
  - Steps 2 and 7 need N > 3κ; Step 3 needs N > 3κ−2.
  - Step 9 needs 3l−2p ≥ 6. With l ≥ κ+1 and 3κ ≥ 2p+4 this holds.
- So the argument actually supports N ≤ 3κ everywhere in the range except κ = (2p+1)/3.
- At κ = (2p+4)/3 with p ≡ 1 (mod 3), p ≥ 7, take T = g^{p+6}(3g)^{p−2}.
  - Proper zero-sums need j ≥ (p−4)/3, so their length is at most (4p+8)/3 = 2κ.
  - T satisfies (ZP_κ) and has length 3κ = 2p+4, so N = 3κ is attained there.
- The uniform bound 3κ+1 is therefore attained only at κ = (2p+1)/3. Any restatement would be a new claim needing its own review.

**LS distinction.**
- SLZ3 bounds |T| for a shortest long T ⊆ Y. It gives no bound on |Y|.
- It yields the LS+ inequality only when Y = T, which is exactly form (2). In that sense the §4 phrase "exactly SLZ3 for Y with no proper long zero-sum" is right.
- It gives no LS(p,κ), LS+, INV*, ordered-Olson or dihedral coverage.

**Consequence vs Lemma SLZ.** The arithmetic 3κ+1 < p+2κ+1 ⇔ κ < p is correct. SLZ itself is outside the packet and unchecked here.

## Findings

**FATAL:** none.
**MAJOR:** none.
**MINOR:**

- **M1** (§2 setup: "κ ≥ (2p+1)/3 ≥ (p+3)/2 for p ≥ 5")
  - Problem: the middle inequality fails at p = 5 (11/3 < 4). The conclusion still holds there because κ = 4 is an integer.
  - Repair: write "δ ≥ (p+2)/3 > 2 and δ is odd, so δ ≥ 3; κ ≤ p−1 gives δ ≤ p−2".

- **M2** (§2 Step 3)
  - (i) "T0 has length ≥ 2p+2" has no reason given. Add: by (ZP_{κ−1}) for T, since |T0| ≥ 2κ, and by parity.
  - (ii) The word "long" is not indexed. Write "(κ−1)-long zero-sum of T" and "κ-long zero-sum of Y".
  - (iii) State that the replacement keeps erratum A-m2's closing line: l ≤ u, i.e. D ≥ 0.
  - Optional shortcut: T0 ≠ T would be a proper zero-sum of length ≥ u, so T0 = T.

- **M3** (§2 Steps 6–7, marked "Unchanged")
  - Problem: the range-sensitive inequalities are asserted but not re-derived. These are m ≥ D+2, A_W < 4p, and g^r, g^s ⊆ Q.
  - Repair: add one line: "(p+3δ)/2 ≥ 2δ ≥ D+2 since δ ≤ p−2; D ≤ 2δ−2 ≤ 2p−6."

- **M4** (§3 hypothesis map)
  - (a) It omits Step 3's uses of N > 3κ−2 and N > 2p.
  - (b) "N ≥ 2p+2 (from (ZP_κ))" is misattributed. H alone gives N ≥ 2p+4, Step 1 uses only minimality, and Step 3 derives (ZP_{κ−1}) for T. So (ZP_κ) on Y is never invoked.
  - (c) "Step 4 (via l)" is wrong: Step 4 uses no l.
  - (d) Steps 6–7 also use κ ≤ p−1, through δ ≤ p.
  - Repair: rewrite the map. Do not drop (ZP_κ) from the statement on the strength of (b) without a separate review.

- **M5** (title)
  - Problem: the title omits κ ≤ p−1, which is necessary. At κ = p, (ZP_p) is vacuous and g^{4p} has shortest long zero-sum of length 4p > 3p+1.
  - Repair: add the upper bound to the title.

- **M6** (§0 Sharpness)
  - State that g is an odd generator; g = p violates (ZP).
  - Write "nonempty zero-sums".
  - Show ⌈(p−3)/3⌉ = (p−1)/3.
  - For p ≡ 2 (mod 3), give "N even" as the reason and note that F1 attains N = 3κ.
  - Add "no sharpness claimed for κ ≥ (2p+4)/3".

- **M7** (§0 "Equivalently")
  - Problem: the equivalence is asserted without derivation.
  - Repair: add the two-line derivation from verdict (2).

- **M8** (§0 Consequence)
  - Problem: Lemma SLZ's acceptance and hypotheses are not in the packet.
  - Repair: replace "whenever κ ≤ p−1" with "for every κ in the SLZ3 range".

- **M9** (§1 Imports, "Nothing else")
  - S1-sharp's acceptance is relative to S1+ and the index-one theorem; list S1+ as a transitive import.
  - Erratum 1 is a mandatory overlay for the "Unchanged" steps; say so.
  - Give the full index-one hash `e461514461d2…4d35c6` instead of `e4615144...35c6`.

- **M10** (notation, Steps 5–9)
  - Problem: "Y" is both the ambient sequence and the non-g part of Q′. "Non-unit part" is a misnomer, since 3g, 5g, … are units.
  - Repair: rename, e.g. Q′ = g^{t′}R.

- **M11** (§4)
  - Problem: LS(p,κ), "thr" and the propagation notes are outside the packet, so "3κ+1 ≤ thr−(p−κ)" cannot be checked here.
  - Repair: define thr or cite its accepted statement. Add: "SLZ3 bounds |T|, not |Y|; no LS, LS+, INV*, ordered-Olson or dihedral consequence follows."

This is a model referee check of a written proof. It is not formal or human verification, and it makes no novelty or priority assessment.
