# Hostile review: PA19 ms09 empty-pair / forced-pair proof `43dd4c42…`, with parent errata v1 `b93c2b54…` and v2 `9acdd422…`

**Result:** Theorems A and B are correct. b59, b67, b69 and b70 are **ACCEPT** at the original-frontier-v1, fixed-profile/fixed-skeleton scope. There are **0 FATAL, 0 MAJOR and 6 new MINOR** findings. All parent erratum repairs are confirmed. B0 is **ACCEPT** against the header bytes, the entry bytes and the encoder code at lines 83–87 and 99.

**Method:**
- I checked everything by hand from the pasted text only. I made no tool calls, read no files and computed no hashes.
- I did not consult the Codex verdict cited in erratum v2.
- `proof:N` means line N of `notes/ms09-empty-pair-and-pair-demand-proof-v1.md`. I reconstructed these line numbers from the packaged text, and the reconstruction reproduces the erratum's anchors at lines 119, 140 and 151.

## Per-case verdicts

| Case | Bytes (width) | Listed types | deg(0..4) | Private rows | Σt+priv / rows | e | Route | Verdict |
|---|---|---|---|---|---|---|---|---|
| b59 | [3934,4011) 77 | {0,1,2}, {0,3,4}; {1,3}, {1,4}, {2,3}, {2,4} | 2,3,3,3,3 | 2,1,1,1,1 = 6 | 14+6 = 20 / 6+6+7 = 19 | 7 | Thm B | **ACCEPT** |
| b67 | [4594,4684) 90 | {0,1,2}; {0,3}, {0,4}, {1,3}, {1,4}, {2,3}, {2,4}, {3,4} | 3,3,3,4,4 | 1,1,1,0,0 = 3 | 17+3 = 20 / 8+3+8 = 19 | 8 | Thm A | **ACCEPT** |
| b69 | [4775,4870) 95 | all 2-sets except {0,1} | 3,3,4,4,4 | 1,1,0,0,0 = 2 | 18+2 = 20 / 9+2+8 = 19 | 8 | Thm A | **ACCEPT** |
| b70 | [4872,4975) 103 | all ten 2-sets | 4,4,4,4,4 | 0 | 20+0 = 20 / 10+0+9 = 19 | 9 | Thm A | **ACCEPT**, no count gain |

In all four cases, distinct listed sets meet in at most one column, and every deg is at most 4.

**b59 trace:**
- The row {0,1,2} has complement {3,4}, which is unlisted, so its pair partner can only be p3 or p4.
- The row {0,3,4} has complement {1,2}, which is unlisted, so its pair partner can only be p1 or p2.
- Lemma 6 forces n2 = 2 for both rows.
- The two rows share Q_0, so they cannot share a pair block.
- That requires four pair blocks, but only three exist.

**What is new:** Per erratum v1 (I have not seen frontier v9), only b59, b67 and b69 are potentially new. b70 is written corroboration of an existing closure.

## Per-claim verdicts

| Claim | Verdict | Independent check |
|---|---|---|
| F1, proof:28 | ACCEPT | P0 gives 6+15 = 21 and P1 gives 12+9+1 = 22, so the total is 171 = C(19,2). Each pair agrees at most once and the total is 171, so each pair agrees exactly once. |
| F2, proof:30 | ACCEPT (N2a) | Two distinct blocks that both contain r and s lie in different columns, which gives two agreements. |
| F3, proof:32–36 | ACCEPT | n2 = n4+t−2 and n3 = 5−t−2n4, with max(0, 2−t) ≤ n4 ≤ ⌊(5−t)/2⌋. For t = 0..3 the listed patterns are exactly all solutions. |
| F4 / F5, proof:38, 40 | ACCEPT | For t = 0 the pattern (0,1,2) is unique. Each P1 column has one pair block, so Σn2 = 6. Pair partners are T-disjoint and nonempty. |
| L1, proof:46–48 | ACCEPT | Each pair of empty rows shares exactly one block, and it is never a quad or a pair block. The group sums e, 2e and e follow from F4. |
| L2, proof:50–52 | ACCEPT | Moving one unit from x_i to x_j lowers the sum by x_i−1−x_j ≥ 1. The balanced value is kC(q,2)+rq. |
| Thm A, proof:54–58 | ACCEPT | e = 8: 5·3 + 14 + 0 = 29 > 28. e = 9: 5·4 + 18 + 0 = 38 > 36. Dropping the P1 per-column coupling and the block-size caps only weakens the bound. The theorem uses only e. |
| L3, proof:64–72 | ACCEPT-WITH-FIXES (N1, editorial) | The budget is 5·2 + 10 + 0 = 20 against 21. All patterns are re-derived exhaustively below. |
| L3 consequence, proof:74 | ACCEPT | A 4-block with eps 0 would cost 3, so it is impossible. A triple with eps 0, a 4-block with eps 1, and a 3-block with eps 2 are mutually exclusive single-unit events. |
| L4, proof:76–80 | ACCEPT | A nonempty row shares exactly one block with each of the 7 empty rows, so its eps-sum is exactly 7. |
| L5 (R1), proof:83, 87 | ACCEPT | Pattern (1,0,2): the quad and pair block give 0, four triples give ≥1 each, two 4-blocks give ≥2 each. The sum is ≥8 unless the row is in the special block. |
| L5 (R2), proof:84, 88 | ACCEPT | Pattern (1,2,0): three quads and the pair block give 0, two triples give ≤2 each, two 3-blocks give ≤1 each. The sum is ≤6 unless the row is in the special 3-block. |
| L6, proof:90–92 | ACCEPT | The partner is nonempty with T ⊆ {x,y}. Since {x,y} is unlisted, the partner is private with n2 = 1. If n2(r) = 1, then X_T = 1, so no special triple or 4-block exists and R1 fails for the partner. |
| Thm B, proof:94–96 | ACCEPT | 3+3 > 5, so the two T-sets meet and no pair block is shared. The two rows need 2+2 = 4 distinct pair blocks, but there are only 3. |
| §4, proof:100–109 | ACCEPT | See the per-case table. |
| §5, proof:113–115 | ACCEPT (comparison only) | For t = 3, n2 ∈ {1,2}, which matches F3. The sample pairing is T-disjoint. Nothing from GPS or from b3/b30/b44 is used as a premise. |
| §6 slack table, proof:119 | ACCEPT (N2b) | Recomputed values are 0, 0, 1, 3, 4, 6, 4, 1, −1, −2. |
| §6 e-table, proof:121–133 | DIAGNOSTIC | The four named rows are verified from bytes. The other rows are consistent with the B0.7 corroboration. |
| §6 b65 and b63, proof:136–137 | DIAGNOSTIC, steps correct | b65: the forced structure is the 4-block {p3, p4, w, ∅} with w ∈ {p0,p1,p2}. b63: the residual alternatives are stated correctly. |
| §6 b66/b68 and next-lemma text, proof:138, 142 | DIAGNOSTIC (N3) | See N3. |
| §6 e ≤ 6 claim, proof:140 | ACCEPT-WITH-FIXES (erratum v1 §2) | See "Parent errata confirmed". |
| §7, proof:148–151 | ACCEPT-WITH-FIXES (erratum v1 §1, N4) | See N4 and "Parent errata confirmed". |
| Result statement, proof:7–16 | ACCEPT-WITH-FIXES (erratum v1 §1) | Holds for the original layer only. |

**Lemma 3 re-derivation, including the 4-block exceptions:**

```
P0 triples, Σx = 7:      j = x−1, C(x,2) = C(j,2)+j, Σj = 2  ⇒ X_c = #{j ∈ {−1,2}}
  X_c=0: {2,2,1,1,1}   X_c=1: j=2 → {3,1,1,1,1};  j=−1 → {2,2,2,1,0}
P1 4-blocks, Σy = 14:    j = y−2, C(y,2) = C(j,2)+2j+1, Σj = 2  ⇒ ΣC = 10 + ΣC(j,2)
  C(j,2) = 3,1,0,0,1 for j = −2..2.  X_Q=0: {3,3,2,2,2,2}
  X_Q=1: j=2 → {4,2,2,2,2,2};  j=−1 → {3,3,3,2,2,1};  y=0 costs 3 → impossible
P1 3-blocks:             z=3 costs 3; X_T ≤ 1 ⇒ all z ≤ 1 except at most one z=2
```

## Findings

**FATAL:** none. **MAJOR:** none.

**MINOR (new):**

- **N1, proof:71.** The line "All other choices violate one of the three equations" asserts the case elimination without showing it. The statement is true. Repair: insert the j = y−2 substitution shown above.
- **N2, wording.**
  - (a) proof:30: "a triple of c contains no row of Q_c" holds because blocks of one column partition the rows, not "hence" from T-disjointness.
  - (b) proof:119: "Lemma 1 by itself" should read "Lemma 1 with the Lemma 2 bound." The stronger reading is also true. For example, at e = 7 the system has a solution: triples {2,2,1,1,1} in every P0 column, 4-blocks {3,3,2,2,2,2}, one P1 3-block with eps 2, and per-P1-column sums 6+1, 4+3, 4+3.
- **N3, proof:138 and proof:142.** These diagnostic assertions are unproved.
  - "Compatible with Lemmas 3–5" for b66/b68 is asserted, and the b66/b68 bytes are not in the packet.
  - The two side claims at proof:142 are true:
    - P1 rainbow: quad-mates already agree in column c.
    - Under b65's forced X_c = 0:
      - g sits alone in a triple with eps 2.
      - The four rows of Q_4 occupy four distinct triples of column 3.
      - So p0, p1 and p2 fill the three triples with eps 1, each next to a distinct row of Q_4.
  - Repair: mark these "not proved". Erratum v2 already removes any obstruction or minimality reading.
- **N4, proof:3 and proof:148.** "execution: none" and "without any computation" conflict with the manifest, which says grep -ob, sed and shasum were run. Repair: reword as "no computation beyond read/locate/hash".
- **N5, proof:22 (B0).** The proof quotes `build` but not the call site that binds `c0`, `types`, `empty` and `special` to the header and entry. Only the docstring describes that binding. This is not needed for the written exclusion (see B0.3).
- **N6, ledger key.** Frontier-v1 pairs the cases with s_tags as follows: b59 with s00042, b67 with s00054, b69 with s00069 and b70 with s00070. The proof correctly keys on b_index. Any disposition must key on b_index plus skeleton content plus the skel-b sha, never on the s-number. The A2 mapping is not verified here.

**Parent errata confirmed:**
- **v1 §1:** The original-layer reading is correct, and proof:151 is stale. The frontier-v1 b70 entry (0 pending intervals, one reserved interval) is consistent with this.
- **v1 §2:** proof:140 is false at e = 1, where slack is 0 per proof:119. One addition: for e ≤ 1 there are no empty pairs, so Lemma 1 is vacuous and slack 0 there carries no information.
- **v1 §3:** The compressed views are not the raw bytes. This also applies to the scope note's phrase "identical per-case copies", which are JSON-equal but not byte-equal.
- **v2 §1:** b70 spans lines 5707–5767 (61 lines), so the scope note's endpoint 5708 truncates it. The start line 3223 was not checked.
- **v2 §2:** Relabelling the headings at proof:117 and proof:142 is right. No obstruction or minimality result is certified.

## B0 bridge audit

**Verdict: ACCEPT** for these four entries.

- **B0.1, profile bytes [0,433).** The header has five `[4, 3, 3, 3, 3, 3]`, then three `[4, 4, 3, 3, 3, 2]`, with `"c0": 5` and `"L": 0`. This is exactly the setting in §0, and L = 0 agrees with 171 = C(19,2). The quoted header is exactly 433 bytes and ends with `"skeletons": [`.
- **B0.2, entry bytes.** The four strings have lengths 77, 90, 95 and 103, which equal their range widths. b69 and b70 are separated by exactly `, `.
- **B0.3, member construction from code, not comments.**
  - `encode_skel_b.py:83-86` builds the row list as: the listed types in order, then 4−deg(x) rows {x} for each x, then `empty` rows ∅.
  - `:87` asserts there are 19 rows.
  - `:99` puts P0 symbol 0 on row r exactly when c ∈ member[r]. So the symbol-0 class of column c is {r : c ∈ member[r]}, which has deg(c) + (4 − deg(c)) = 4 rows.
  - `:88` places the 4 on symbol 0.
  - Therefore Q_c is that class and T(r) = member[r] for every row, which is exactly B0. The docstring agrees but is not relied on.
- **B0.4, what each theorem uses from B0.**
  - Theorem A uses only that exactly e rows lie in no quad.
  - Theorem B also uses that the rows with |T| = 2 are exactly the listed 2-sets, and that the private counts are as stated.
- **B0.5, robustness.**
  - Both theorems' hypotheses are invariant under permutations of rows, columns and symbols, so the exclusions cover every relabelling of each skeleton.
  - No list, `ext.json`, orbit or interval data is used, and every interval of a case is a restriction of the excluded class.
- **B0.6, frontier-v1 binding.**
  - The entries with b_index 59, 67, 69 and 70 have skeleton_types and skeleton_empty JSON-equal to the bytes.
  - Their line spans of 45, 52, 55 and 61 lines match the pretty-print shape: 17 header lines, plus t+2 lines per type, plus 2 closing lines, plus 2 for b70's single reserved interval.
- **B0.7, index-to-offset corroboration (hand derivation, not a premise).**
  - The per_h counts (4, 6, 10, 15, 14, 11, 6, 3, 1, 1; total 71) equal the numbers of S5-classes of skeletons with h = 1..10 listed types.
  - Each one-line entry has length 3e + 5h + 26, because Σt = e + h + 1.
  - Ordering by h and summing gives b59's start as 433 + 3501 = 3934. The same model reproduces 4594, 4775, 4872 and 4975.
  - The model also reproduces the frontier line gaps: 335 lines for b60–b66 and 51 lines for b68.
  - The h-ordering is my inference, and the header field `hmax: 6` is unexplained by it. So this is corroboration only.

**Residuals (trust items, not proof gaps):**
- The encoder call site is not quoted (N5).
- The clauses after line 99 are not quoted. They are irrelevant to the written exclusion.
- The encoder does not itself check deg ≤ 4 or that listed sets pairwise meet in at most one column. Both were checked by hand for these four cases.
- Skeleton-list coverage is out of scope.

## Trust boundary

- **Inputs:** only the pasted package, the raw excerpts and the two errata. Every SHA-256 is unverified by me. The binding of what I reviewed to those digests rests on the parent's check, per erratum v1 §3.
- **Frontier v9:** I have not seen it. "b70/b5/b9 already closed" and the count of 132 are parent statements.
- **No prior verdict used:** b3, b30 and b44 served only as a comparison of semantics.
- **Process:** The scope note says it was frozen before derivation, but it also discloses that the Theorem A inequality was sketched before the freeze. This does not affect correctness.
- **Level of this verdict:** a written hand check of a fixed-profile, fixed-skeleton theorem. It is not solver-checked or Lean-checked, it is not a human certificate, and it does not address coverage, ms06, GPS or the lists.

## Claim boundary

- No interval, list, queue or frontier count changes before the parent decides on both families.
- PA(19,8,6) stays UNDECIDED.
- No claim about optimum 18 or 19, and no novelty, Lean or human-verification claim.
- Nothing in this review blocks parent acceptance at the stated scope. N1–N6 are editorial or trust items.
