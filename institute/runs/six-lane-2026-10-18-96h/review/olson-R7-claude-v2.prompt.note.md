# Hostile review: R7 (p=7, k=8, κ̂=3)

**Texts reviewed:** `proof-R7-v1.md`, read with author erratum 1 (applied at LF206–207) and the parent erratum (applied at LF133–134).

**Method:** I re-derived every step by hand in this response. I used no tools, computation or delegation. I did not check any hash, byte or line metadata.

## Bottom line

**FATAL 0 · MAJOR 0 · MINOR 8.**
- One MINOR is already disposed by the parent erratum, and I verified that erratum is correct.
- Seven MINORs are open: 2 import-scope, 4 mathematical/expository, 1 labels.
- None of the open items touches a load-bearing inference.

| Claim | Verdict at the full NF antecedent | Load-bearing inputs |
|---|---|---|
| THEOREM R7 (b∈{1,2,3}) | Correct | NF, GRX (if direction), RS(b) with K=6, CD inside RS(b); UH-A used for A≥9 only |
| PROP. R7-PURE (b=0) | Correct, re-proved independently of KP4 §7.3 | NF, GRX, RS(b), CD. **Not UH-A**: all letters equal gives A=12 directly after U7 and normalization |
| COROLLARY (cell p=7, k=8, κ̂=3 is empty) | Correct, since b=0 and b≥1 are exhaustive | The union of the two; UH-A enters only through Theorem R7 |

Nothing follows for κ̂=4 at p=7, other cells, p≥11, or multiset-only statements, and nothing of that kind is claimed.

## 1. UH-A antecedent, checked before A≥9 is used (LF66–70)

The antecedent holds literally:
- Prime p=7≥7 (boundary case).
- (p−1)/2 = 3 ≤ κ = 3 ≤ p−3 = 4 (left boundary).
- Length 4p−2 = 26; terminal k = p+1 = 8; κ̂ = 3.
- e = 4, H = e−1 = 3, any distribution allowed.
- Empty-run rule holds (ROT-few-E-v4 LF38).
- A common nonzero dominant class is proved in-file before the import (U7, LF55–58), independently of UH-A.
- The orientation A≥A' is chosen at LF60–61.

How UH-A is used:
- Only A ≥ 2κ+3 = 9 is imported.
- A'≤3 is re-proved at LF65, and b≤3 follows from A≥9.
- UH-SH is not used, and could not be: 3e = 12 > p+2 = 9.
- Errata v1–v3 do not change the UH-A row.
- The identification of UH-A's class and orientation with R7's is automatic, but the text does not argue it (finding I1).

## 2. Sub-claim verification

| Item | LF | Result |
|---|---|---|
| SR7 / V_m | 32–37 | All l_i are odd, so δ_GRX = #{f_i=0} = 8−Φ and C_max = Φ+6. Hence n ∈ [max(0,8−2m), min(14−2m,12)], even. Exact. T(z_P) = Σ_{i∈P} τ_i follows from Σθ=0. |
| Cycle facts | 41–43 | C_8 has no triangle. Five vertices split into ≤3 paths with Σ⌈s_i/2⌉ ≥ 3. A shared neighbour set {x±1} = {x'±1} would force 4 ≡ 0 mod 8. All correct. |
| Lemma M | 47–50 | Capped total ≥ 2q in both branches. An equal pair x_i = x_{i+q} would need q+1 consecutive equal entries. Correct. |
| Lemma P7 | 51–54 | μ≤6 gives q=6≤12−μ. RS(b) on 6 nonzero d_i with K=6 gives min(7, 1+6) = 7 residues. n=6 is admissible for m=1..4. Within RS(b)'s accepted scope. |
| Lemma U7 | 55–58 | ≥7 of 12 forces a unique value and a unique class. For class {0}: pigeonhole gives y_j = y_{j'}; runs R_{j+1..j'} form a proper arc with T = 0; six zeros sum to 0. Correct. |
| Normalization | 59–61 | φ((v,e)(v',e')) = ((v+ev')/a, ee') = φ(v,e)φ(v',e'). Bijective. Blocks, parities and the empty-run rule are preserved; T and signed sums both scale by 1/a. Correct. |
| W7 and A'≤3 | 62–65 | Signed +1 count is A−d(P); signed −1 count is A'+d(P); deviants are never signed ±1. Band [A−6, 6−A'] is nonempty iff A+A'≤12. All-plus with n=8 gives A'≤3. Correct for every proper nonempty P. |
| Lemma S | 77–81 | Sum = (2ν−\|J\|) + Σ_J(1+2ω) = 2(ν+Σ_Jω). Both occurrence bounds kept. With A≥9: ν≤4 is free, ν=5 needs \|J\|≥b−2, ν=6 needs J=B, and \|J\|≤2ν never binds when ν≥2. Consistent with the accepted UH-E restriction. |
| Lemma B + classification | 82–91 | ω→β map: 1→3, 4→2, 5→4, 6→−1 (and 2→5, 3→0). **b=2:** excluded pairs are (1,1)=2, (4,4)=1, (4,5)=2, (4,6)=3, (5,5)=3. **b=3:** the partners of 4 lie in {1,4}; {4,4,1}=2 and {5,6,6}=3 are excluded; {4,4,4}=5, {1,5,6}=5, {1,6,6}=6, {6,6,6}=4 survive. C1–C12 is exhaustive. |
| Lemma E | 92–115 | All 13 rows re-computed; see Table A. |
| §4 | 117–128 | q ∈ [max(0, 2ν−12+ε), min(2ν, ε)], sum = 2(ν−q). All intervals verified; see Table B. |
| 5.1 | 137–144 | See Table C. In (a), every prefix is a proper arc, and d_t ≥ Λ−λ > λ. (b) gives the contradiction A ≥ 2Λ. In (c), empty runs ≥ 7−b−λ = 2 while E = 0. |
| 5.2–5.4 | 146–233 | See Table D. Every census, list, witness and kill is correct. |

### Table A: Lemma E (G, G≥1, M re-computed)

| Cfg | ω | G | G≥1 | M | ω_B | single-empty t | two empties | E |
|---|---|---|---|---|---|---|---|---|
| C1 | 6 | {0,6} | – | {1..5} | 6 | ±1 | Adjacent: s∉{2..5}; non-adjacent: s∉{1..5}; so s=0 and the t are opposite; a triple is impossible | ≤2 |
| C2 | 4 | {0,4} | – | {1,2,3,5,6} | 4 | −1 | s=5: s−5=0∈G | ≤1 |
| C3 | 5 | {0,5} | – | {1,2,3,4,6} | 5 | −1 | Same as C2 | ≤1 |
| C4 | 1,4 | {0,1,4,5} | – | {2,3,6} | 5 | None (no 3 consecutive residues in M) | – | 0 |
| C5 | 1,5 | {0,1,5,6} | – | {2,3,4} | 6 | Only t=0, excluded | – | 0 |
| C6 | 1,6 | {0,1,6} | – | {2..5} | 0 | 1 | s=2: adjacent s−3=6∈G; non-adjacent s−2=0∈G | ≤1 |
| C7 | 5,6 | {0,4,5,6} | – | {1,2,3} | 4 | −1 | s=5: 0∈G | ≤1 |
| C8 | 6,6 | {0,5,6} | – | {1..4} | 5 | −1 | s=5: 0∈G | ≤1 |
| C9 | 4,4,4 | {0,1,4,5} | {1,4,5} | {2,3,6} | 5 | t=6 fails: 1∈G≥1 | – | 0 |
| C10 | 1,5,6 | {0,1,4,5,6} | same | {2,3} | 5 | t=6 fails | – | 0 |
| C11 | 1,6,6 | {0,1,5,6} | same | {2,3,4} | 6 | t=6 fails (t=0 excluded) | – | 0 |
| C12 | 6,6,6 | {0,4,5,6} | {4,5,6} | {1,2,3} | 4 | −2, −1 | Only s=5 (both −1) survives; a triple gives −3−4 ≡ 0 ∈ G | ≤2 |
| pure | – | {0} | – | {1..6} | 0 | 1, 2 | Non-adjacent s∈{2,3,4} is killed by (E2); any triple contains a non-adjacent pair | ≤2 |

### Table B: §4 intervals

| (m, ε) | ν | Intervals | Union | Allowed set |
|---|---|---|---|---|
| (2 or 3, 4) | 2, 4 | [−2,2], [0,4] | [−2,4] | ∅ (FORB) |
| (2 or 3, 8) | 2, 4 | [−2,2], [−4,0] | [−4,2] | ∅ (FORB) |
| (1, 3) | 3–6 | [0,3], [1,4], [2,4], [3,3] | [0,4] | {−2,−1} |
| (1, 5) | 3–6 | [−2,3], [−1,3], [0,2], [1,1] | [−2,3] | {−3} |
| (2, 5) | 2–5 | [−2,2], [−2,3], [−1,3], [0,2] | [−2,3] | {−3} |
| (2, 7) | 2–5 | [−2,2], [−3,2], [−3,1], [−2,0] | [−3,2] | {3} |

### Table C: heavy-run data (5.1)

| Cfg | (A, A') | λ | Λ | Λ−λ > λ | A < 2Λ | 7−b−λ |
|---|---|---|---|---|---|---|
| C4, C5 | (10, 0) | 3 | 7 | 4 > 3 | 10 < 14 | 2 |
| C9 | (9, 0) | 2 | 7 | 5 > 2 | 9 < 14 | 2 |
| C10 | (9, 1) | 2 | 6 | 4 > 2 | 9 < 12 | 2 |
| C11 | (9, 2) | 2 | 5 | 3 > 2 | 9 < 10 | 2 |

### Table D: census, survivors and kills (5.2–5.4)

ΣP+ = A − A' − s₋.

| Case | Band | Negative runs | Zero runs ≤ | \|P+\| ≥ | ΣP+ | Forbidden sums | Survivors → kill |
|---|---|---|---|---|---|---|---|
| C2/C3 | [5,6] | – | 1 empty + u-only | 6 | 11 | 5, 6 | none |
| C6/C7 (i) | [4,5] | g1 = −1 | 2 | 5 | 10 | 4, 5, 6 | none |
| C6/C7 (ii) | [4,5] | – | g1 + 1 + 1 | 5 | 9 | 4, 5 | none |
| C6/C7 (iii) | [4,5] | – | 2 | 6 | 9 | 4, 5 | none |
| C8, s₋=0 | {4} | – | 1 + 2 balanced | 5 | 8 | 4 | none |
| C8, one −1 | {4} | 1 | 1 + 1 | 5 | 9 | 4, 5 | none |
| C8, one −2 | {4} | 1 | 1 | 6 | 10 | 4, 6 | none |
| C8, two −1 | {4} | 2 | 1 | 5 | 10 | 4, 5, 6 | none |
| C1 (i) | {5} | g | 2 | 5 | 11 | 5, 6 | (7,1^4): {h7,e} has ε=8, so both empties are the neighbours of h7. The other 5 places form a path, so some 1-run x is not adjacent to g. {h7,g,x} has m=3, ε=8. |
| C1 (ii) | {5} | – | g + 2 | 5 | 10 | 5 | (6,1^4): {h6,x} has ε=8. (2^5): Allow₁(3) and Allow₂(5) force non-adjacent pairs to have distinct t in {−2,−1}; an independent triple is impossible. |
| C1 (iii) | {5} | – | 2 | 6 | 10 | 5 | none |
| C12 (a) | {3} | – | 2 + 3 | 3 | 6 | 3 | (4,1,1): ε=4. (2^3): each t=−3; a non-adjacent pair sums to 1 ∉ {3}. |
| C12 (b) | {3} | −1 | 2 + 2 | 3 | 7 | 3, 4 | (5,1,1): ε=4 |
| C12 (c1) | {3} | −2 | 2 + 1 | 4 | 8 | 3, 5 | (2^4): same kill as (2^3) |
| C12 (c2) | {3} | −1, −1 | 2 + 1 | 3 | 8 | 3, 4, 5 | (6,1,1): x would need all 3 zero runs as neighbours |
| C12 (d1) | {3} | −3 | 2 | 5 | 9 | 3, 6 | none (total ≥ 14) |
| C12 (d2) | {3} | −2, −1 | 2 | 4 | 9 | 3–6 | none |
| C12 (d3) | {3} | three −1 | 2 | 3 | 9 | 3–6 | (7,1,1): two runs with the same two neighbours, impossible (no 4-cycle) |
| pure | {6} | – | 2 | 6 | 12 | 6 | (7,1^5): {h7,x} has m=2, ε=8 |

**Partition lists.** I re-enumerated each list using the bijection "k parts of N with parts ≤ c ↔ partitions of N−k into at most k parts with parts ≤ c−1".
- Every list is exactly complete.
- Every bracketed witness is a genuine forbidden subset sum.
- Every profile marked "allowed" is genuinely allowed.

Counts by number of parts:

| Case | Counts |
|---|---|
| C2 | 5 / 4 / 3 (6, 7, 8 parts) |
| C6 (i) | 3 / 3 / 2 |
| C6 (ii) | 3 / 2 / 2 / 1 |
| C8, s₋=0 | 2 / 2 / 1 / 1 |
| C8, one −2 | (5,1^5) plus 3 / 2 |
| C1 (i) | 6 five-part profiles plus (7,1^4) |
| C1 (ii) | 5 / 4 / 3 / 2 plus (6,1^4) |
| C12 (a) | 3 / 2 / 1 / 1 |
| C12 (b) | 4 / 3 / 2 / 1 / 1 |
| C12 (c1, after E1) | 5 / 3 / 2 / 1 / 1 |
| C12 (c2) | 5 / 5 / 3 / 2 / 1 / 1 |
| pure | 9 / 6 / 5 plus (7,1^5) |

Author erratum E1 is correct and complete.

## 3. Findings and minimal repairs

### Import-scope

**I1 — MINOR — LF68–69.** The text asserts that UH-A's "dominant class and orientation are those of 2.3" without argument.
- Repair: append after LF69: "Any class {c,−c} with #c≥9 equals {1,−1}, since that class holds ≥7 letters (2.3) and 9+7>12. Also c=−1 is impossible, since it would give A≥A'≥9 and A+A'≥18>12."

**I2 — MINOR — LF30–31 versus LF66–68.** UH-A's accepted scope is the NF-level antecedent (w has some adm

issible NF with k=8, κ̂=3). LF30–31, however, says the proof excludes "every such avoider u (word form)", and the text never connects the two.
- Repair: add at LF68: "UH-A is applied to w. A is a count in the rotation multiset, which w and u share (NF preserves it) and which φ maps to the normalized count."
- Alternative repair: "u is its own admissible NF: its maximal constant sub-blocks are S_0..S_7, all odd, and no PM* or fusion step applies."

### Mathematical / expository

**M1 — MINOR, DISPOSED — LF133–134.**
- The original sentence is false. Example: in C2 with all eight runs positive, the all-parts subset of P+ is the full run set, and the empty subset is not nonempty.
- The parent erratum is correct. Since A≥9, d(∅) = 0 < A−6 and d(all) = A−A' > 6−A'.
- The erratum also covers mixed sets (positive runs together with g1 or other negative runs). So every band contradiction in 5.2–5.4 is a legitimate W7 instance.
- Every FORB and Allow set has m≥1, so it is proper and nonempty by construction.

**M2 — MINOR — LF160–161 (C6/C7 case (iii)).** The reduction to parts ≤3 is not restated.
- Repair: "A part ≥6 would leave ≥5 parts summing to ≤3, and 4 and 5 are forbidden, so all parts are ≤3. The 6- to 8-part lists of (ii) all fail."

**M3 — MINOR — vacuous profiles.** Several lists include profiles with more parts than there are available positive runs:
- LF156: the 8-part profiles.
- LF159: the 8- and 9-part profiles.
- LF166 and LF171: the C6 lists, reused.
- LF169, LF178, LF186: the 8-part profiles.
- LF207 after E1, and LF212: (1^8).

This is a harmless superset.
- Repair, one sentence at LF135: "Lists may contain profiles with more parts than available positive runs; such entries are vacuous."

**M4 — MINOR — notation.**
- (a) LF75, 82, 97, 108: define G_(≥r) := G for r≤0. The cases b=1 and b=2 use G_(≥−1) and G_(≥0).
- (b) LF112: "t=6: t−5=1" should add "∉ G_(≥1)".
- (c) LF57: name the arc: "runs R_(j+1),…,R_(j') form a proper arc (m=1) with T = y_(j') − y_j = 0".
- (d) LF94: "(E1) hold for s" should read "the four selection conditions of (E1) hold for s; s=0 is not excluded". This is the reading C1 actually uses at LF100–101.

**M5 — MINOR — LF242.** "Without it the cases A in {7,8} would remain" assumes A≥7 without UH-A. The file does not prove this. It is true and not load-bearing.
- Repair: delete the sentence, or add: "W7 alone gives A≥7. If A≤6, every run has d_i≤−1 or d_i≥4. Empty runs fail this. At most A'≤3 runs have d_i≤−1, and at most one run has d_i≥4. But there are 8 runs."

### Labels

**L1 — MINOR.** Three parts are labelled inconsistently with the file's own convention:

| Item | Lines | Current label | Should be |
|---|---|---|---|
| Lemma S | LF77 | none | [RE-DERIVED]: the p=7 instance of the UH-E / KP4-B1 selection, proved in-file |
| The three Lemma B conditions and the b=1 list | LF83, LF240 | [NEW] | [RE-DERIVED]: pending KP4 Lemma B1 (obstruction LF50–53), disclosed at scope LF38–39 |
| The b=2 and b=3 classification | LF83, LF240 | [NEW] | [NEW] (correct as is) |
| Lemma E, rows C1, C8, C12 and pure | LF92, LF240 | [NEW] | [RE-DERIVED, different route]: they reproduce pending KP4 Lemma PR (obstruction LF39–42) and scope LF37–38 |
| Lemma E, deviant rows (C2–C7, C9–C11) | LF92, LF240 | [NEW] | [NEW] (correct as is) |

- Package LF39 ("Sec. 3 [NEW]") needs the same correction.
- This has no effect on premises: every one of these steps is re-proved in-file.

## 4. Not checked, and recommendation

**Not checked:**
- SHA256 values, byte counts, LF ranges and the manifest. No tools were permitted.
- UH-A's own proof. It is an accepted input, and I used only verdict LF9 and LF15 and errata v1–v3 as pasted.
- The KP4 packet. It is context only, and no step of R7 needs it.

**Recommendation:**
- ACCEPT-WITH-MINOR-FIXES at the exact scope, for Theorem R7, Proposition R7-PURE and the Corollary.
- I1, I2, M2, M4 and M5 fit in one numbered erratum with no logical change. M3 and L1 are optional.
- The status stays CANDIDATE_UNVERIFIED until the parent's both-family verdict.
