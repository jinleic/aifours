DISPOSITION: ACCEPT-WITH-FIXES

- **Target (1), `c6/proof-SEEDB-r2.md`: ACCEPT-WITH-FIXES.** I found no mathematical error in Lemmas TS, IS, SL, SCW-B, C0, Theorem SEED-B, Claim E or Proposition AB. The fixes concern open-class accounting, a finite claim that rests on a mis-cited [F] receipt, and remarks.
- **Target (2), `c6/c5-fixes/proof-Cplus-r2.md`: ACCEPT.** The C4 integrality step is correct.
- **Target (3), `c6/c5-fixes/proof-SEED-r3.md`: NOT REVIEWED.**
  - Neither that file nor `c5/proof-SEED-r2.md` is in the packet, so I cannot confirm it is wording-only.
  - Also absent: `c5/proof-Cplus-r1.md`, `c6/proof-SEEDB-r1.md` and `c3/proof-NOLP-r2.md`. The version-delta claims (SEEDB-r2:3-9, Cplus-r2:7-14) are therefore unverified.
  - I audited both r2 texts standalone, so their correctness does not depend on those deltas.

All checks below are hand re-derivations from the packet text. Nothing was executed.

## Findings

**F1 — MINOR: the list of what remains open is incomplete.** SEEDB-r2:23-24 says item (iii) "also contains words with excess and all-single-letter words with 2B + kB >= p - 1." Read as the complement of what SEED-B covers, it omits two groups:
- **(a) B = 1 all-single-letter words** (W(p,kB), 1 ≤ kB ≤ p − 4). The region R requires B ≥ 2, and nothing in this file treats B = 1.
- **(b) The six classes of R failing (E):** (11;4,2), (11;5,2), (13;5,3), (13;6,2), (13;7,2), (17;7,4). Line 22 names only the p = 17 one.

Corrected sentence:
> Among all-single-letter item-(iii) classes (kB ≥ 1, B ≥ 1, kB + B ≤ p − 3), SEED-B leaves exactly:
> - B = 1;
> - B ≥ 2 with 2B + kB ≥ p − 1;
> - for p ∈ {11, 13, 17} only, the six classes above. Their exclusion is at present computer-assisted only (IND* class hypotheses certified by [F]; at p = 11 also word by word).
>
> All words with excess remain outside.

**F2 — MINOR: a finite claim is carried only by a mis-cited [F] receipt.**
- SEEDB-r2:22 and :181-182 assert the exception lists and cite "seedB.txt Part C". Part C (:200-201) is Claim E for 19 ≤ p ≤ 600. The six-class list is in Part A (:197-198).
- The lists are correct. A written replacement, using the proof of Claim E (failure of (E) forces 9B ≤ 2p + 2 and 3B ≥ 2p − 23) plus kB ≤ p − 2 − 2B:
  - **p = 17:** B = 4. Then 5kB > 34 forces kB = 7, and (7,4) fails both inequalities (52 > 51, 70 > 68).
  - **p = 13, B ∈ {2, 3}.**
    - B = 2: 5kB > 24 and 2kB > 10, with kB ≤ 7, give kB ∈ {6, 7}.
    - B = 3: 5kB > 23 with kB ≤ 5 gives kB = 5, and 59 > 52.
  - **p = 11:** B = 2. Then 5kB > 18 and kB ≤ 5 give kB ∈ {4, 5}; the pairs inequality fails as well (2kB > 2).
- If :182-184 is meant to assert that the six classes are excluded, label it [W+F] computer-assisted, as Corollary HYP is labelled.

**F3 — INFO: inexact remark (not load-bearing).** SEEDB-r2:240-241 says the anti seed top "(δ−B−3)/2" is lower than ⌊δ/2⌋−1 by ⌊B/2⌋+1.
- (δ−B−3)/2 is only a bound, and it can be a half-integer: 2.5 at (17;5,4).
- The exact gap depends on the parity of y:
  - y even: s_hi = ⌊δ/2⌋−⌊B/2⌋−2, so the gap is ⌊B/2⌋+1.
  - y odd: s_hi = ⌈δ/2⌉−⌊(B+1)/2⌋−2, so the gap is ⌊(B+1)/2⌋+1−[δ odd].
- Counterexamples:
  - (17;5,3): m = 5, δ = 12, s_hi = 2. The gap is 3, not 2.
  - (17;4,4): m = 5, δ = 13, s_hi = 3. The gap is 2, not 3.
- The remark is right for the two classes that contain Proposition-AB words, (17;5,4) and (17;5,5), where y = 6.

**F4 — INFO.** At :76, "As m <= (2kB+B+4)/3: 3m >= 2kB+B+2 gives …": the inference uses only 3m ≥ 2kB+B+2, which is the definition of m. The upper bound is used later, at :78. Reword accordingly.

**F5 — INFO.** :23 says "These are item-(iii) words", and the Corollary at :180 drops the qualifiers "all-odd inherited RGR word of length 4p−2".
- The definition of item (iii), including any ZSI-B exclusion, is not in the packet.
- The proof needs only NMH membership and R = k ≤ 2p−4, which hold:
  - all reflection runs are odd;
  - k ≥ p+3;
  - all runs are pure;
  - 1 ≤ B ≤ κ−1;
  - B ≤ A = p+kB ≤ 2p−1;
  - κ = k−p (PAR-K0:12 with o_F = k), consistent with kB = κ−B.
- Suggested wording: "NMH words with R = k ≤ 2p−4 (in particular their item-(iii) members)". Restore the qualifiers at :180.

**F6 — INFO.** The letter "R" is both the region (:21) and the rotation-letter count (:162, :173). Rename the region.

**F7 — INFO: Proposition AB.**
- It is correct provided the last plain step has condition (B) in the form at :223. That form follows from Lemma L with ranges [λ, U], but Lemma L is not in the packet.
- I checked the parity analysis at :225-227. For N even, e = 1 + [f even]; for N odd, e = [f odd]; the condition is f ≤ 4 − e.
- Cosmetic:
  - "f ≥ 1" should be ≥ 4 (resp. ≥ 5).
  - "D > 0" needs B < p+kB, which holds for NMH words but not for "any B".
- The [F] data are internally consistent by hand:
  - the word counts 52, 286, 328 and 1,534 equal the bracelet counts;
  - there are 1 and 13 AB words;
  - the interval counts 1, 5, 2, 1, 1, 1 match the six anti sets listed.

**F8 — INFO.** Cplus-r2:27-28 keep r1's provenance ("Written in c5/…", "target T4 of c5/README.md") inside the r2 file. Mark it as "(r1 provenance)" so it does not conflict with :3.

## Target (1): the points you flagged

1. **Section 0 (setting).**
   - lam, lamc and U follow from Lemma H with β = 0 and κ−B = kB.
   - D = p+kB−B equals c3's 2p−k+2kB.
   - (F1) follows from 2m ≤ k.
   - Singletons:
     - aligned: λ = 2−kB, U = ⌊δ/2⌋ ≥ B+1;
     - anti: λ = −kB, U = ⌊δ/2⌋−1.
   - The canonical-lift intervals have ⌊δ/2⌋+kB−1 and ⌊δ/2⌋+kB ≤ (p+kB)/2 < p integers, so the lift exists and is unique.

2. **Existence of the isolated configuration in Lemma IS, for every t and every placement.**
   - After deleting t and its two neighbours, the path contains at least n−3 aligned runs in r ≤ B+1 maximal aligned intervals. No position information is used.
   - Anti runs adjacent to Q or to t are harmless. They lie outside Q and Q+t, so m(Q) = m and m(Q+t) = m+1 for every placement.
   - Both reductions are correct: kB+2B+17 ≤ 3p, and kB+3⌊B/2⌋+2B+14 ≤ 2p (implied by (E) because 3⌊B/2⌋+2B ≤ 7B/2).
   - Where the pairs branch occurs at small primes:
     - p = 11: never.
     - p = 13: only (5,2), where m = 4 and the guarantee (n−B−4)/3 = 4 is attained (intervals (1,1,13)).
     - p = 17: exactly for (kB,B) ∈ {(8–11,2), (8,3), (9,3)}.

3. **(1.1), (1.2) and part (d) of Lemma IS.**
   - Singles: the λ-values follow from 2kB+B+2 ≤ 3m ≤ 2p−B−3.
   - The U-values need m ≤ δ−3, which is exactly the first inequality of (E). It is tight at (17;7,3), where m = 7 = δ−3.
   - Pairs: the values follow from kB+⌊B/2⌋+1 ≤ 2m ≤ p−⌊(B+1)/2⌋−1 and B+1 ≤ ⌈δ/2⌉. The latter is tight at δ = 2B+2, e.g. (17;11,2) and (17;9,3).
   - I re-derived the four explicit seed forms and the bounds (1.2).
   - Part (d): there is no wrap-around, and this uses only δ < p.

4. **SCW-B, s ≥ 3: all 36 term sums.**
   - I recomputed every sum on the domains 1−B ≤ y ≤ n (aligned t) and −B ≤ y ≤ n−1 (anti t), with m−1 ≤ m′ ≤ m.
   - The minimum lower bound is exactly (δ−B+2)/2, attained e.g. by:
     - aligned U2+T3 at y = 1−B, m′ = 1;
     - anti V2+S3 at y = −B;
     - anti V3+S2 at y = n−1.
   - The targets are ≤ (δ−B+1)/2, so every case has slack of at least 1/2.
   - B ≥ 2 enters only through δ−B ≥ 4 (≥ 2 would suffice).

5. **SCW-B, s = 2.**
   - (B^s): the sums are at most δ−B−1, δ−B−2, δ−B−3 against at least δ+2, δ, δ−2.
   - (A^s): the slack is kB+1, kB+2, kB+3.
   - The F-branch is complete. The route via (1.2) needs p ≤ 3kB+2B+3, which is implied in the "otherwise" case (p ≤ 3kB−3).

6. **Pin.**
   - The lower end is min(δ, δ−B+2, ⌊(δ+1)/2⌋+1) ≥ 1.
   - The upper end needs b_a ≤ (δ−B−3)/2 ≤ δ−1.
   - Hence X_[k] = p.

7. **Lemma C0.** I traced C-r1 Sections 1–2 under case (i).
   - Section 1 uses only Σx = p.
   - The Kill lemma is pure arithmetic given Lemma H.
   - (A-i) uses x_t ≤ ⌊d_t/2⌋ on Z, n_ev,al ≤ 4 and (0.1).
   - Case B: (B1) gives |X_o| ≥ 2Δ+kB+1 ≥ 2Δ+2. (B2) uses E/2 = p−k+κ and (0.1).
   - (H) enters only through (0.2), plus the singleton bound in (A-ii), which case (i) does not use.
   - Hypotheses match: (0.1) is equivalent to p ≥ kB+B+3, and here p ≥ kB+B+4; n_ev,al = 0.

8. **Claim E.** The proof is correct; strictly, 4p ≤ 71. The exception lists are exact (see F2).

9. **Imports and circularity.**
   - SEED-B uses only Lemma H, the Claim (whose hypothesis λ(Q)+λ(Q^c) ≤ p holds for avoiders by PAR-K0:67-68) and C-r1 case (i).
   - None of these depends on SEED-B, (H), Lemma L or BC, IND*, or [F].
   - There is no circularity. `proof-WALL.md` is not used by targets (1) or (2).

## Target (2): C4

- **The condition.** (ii+) is equivalent to 2s0 = 2(k−kB−2B)+n_pr−n_ev,al ≥ 1, i.e. s0 ≥ 1/2. (ii) implies (ii+) via k−kB−2B ≥ kB+3.
- **The count.** Lines :62-75 match C-r1:84-92 term by term. They keep the n_pr/2 term, which c3 drops harmlessly.
- **The integrality step (:76-77) is correct.** Δ = kB−Φ(Z) and |X_o| are integers, so |X_o|−2Δ is an integer ≥ s0 ≥ 1/2, hence ≥ 1. Under (i), s0 ≥ 2.
- **(B2+).** Σ⌈L_i/2⌉ ≥ Δ+1/2 implies at least Δ+1 runs.
  - This replaces the only use of 2Δ+2 in c3, at C-r1:95.
  - (M), (Fl) and (P) (C-r1:98-109) need only |S| = Δ+1 and the X_o-properties.
  - (A-ii) (C-r1:69-76) does not use n_ev,al, so the C3 bracket is accurate.
- **Corollary HYP data.** I re-derived k, A, B, κ, kB, E, n_ev,al, n_pr, s0 and the length 4p−2 from the arrays for H1–H7, and checked the blocks in Remark (1). All values are consistent.
- **Effect of C4.** Every one of H1–H7 has s0 ≥ 1, so the weakening adds no coverage for them.
- **Remark (2)** correctly calls the shrunk-window solutions relaxed-system solutions, not counterexamples.

## Target (3)

Not reviewable. To close it, supply r3 and c5-r2, or their diff, and confirm that statements, displayed formulas and inequalities are identical apart from the S1–S4, S9 and S10 prose.

## Is the scope claim exact?

- **Theorem statement: exact.** The hypothesis set (p ≥ 11, R ∧ (E), arbitrary anti-run positions) is stated exactly. R ∧ (E) = R for p ≥ 19, and the six-class exception list is exactly right.
- **The "what else item (iii) contains" sentence at :23-24: not exact.** It omits B = 1 and the six classes. With the F1 replacement it becomes exact.
