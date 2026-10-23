# RUH2 hostile review: corrected snapshot P + PE + R + RE, with erratum-2 applied last

**Files and order.** All files are in `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/upperhalf-RUH-round2/`:
- **P**: `proof-RUH2-v1.md`
- **PE**: `erratum-1-proof-RUH2-v1.md`
- **R**: `residual-RUH2-v1.md`
- **RE**: `erratum-1-residual-RUH2-v1.md`
- **X2**: `erratum-2-RUH2-v1.md`

I applied them as PE (E1, E2), then RE, then X2 (M1, the PE parenthetical, N1–N5). Each X2 Old span appears verbatim exactly once in the embedded texts, and none overlaps E1 or E2.

**Limits of this review.** I used no tools, so SHA256, byte and manifest metadata are unchecked. I did not see or use the Codex text. Everything below is re-derived. All statuses remain CANDIDATE_UNVERIFIED, and the parent owns the verdict.

## Bottom line

**FATAL 0 · MAJOR 0 · MINOR 2.** Both MINOR findings are wording in residual §4; no proved claim is affected.

- Lemma L, Theorem A, Theorem B and Corollary B hold as written at their stated scopes.
- The SH and MW steps are genuinely proved in-file, not imported.
- Codex MAJOR 1 and MINOR 1–5 are fully repaired.
- No repair strengthens any statement.

## 1. Re-derived base (P:28–76): proved in-file, imports clean

- **Word form and SR.**
  - F = p+2e−1 and R = 3p−1−2e.
  - With all l_i odd, δ_GRX = N−Φ, so C ∈ [2m, 2m+2e−2] and j ∈ [m, m+e−1].
  - In the SH range, p ≥ 7 gives 2e ≤ p−1, so 0 ≤ 2p−2j ≤ R whenever 0 ≤ m ≤ e (P:39). ✓
- **Lemma P (P:45–47).**
  - The length j* = min((p+1)/2, m+e−1) satisfies j* ≥ m, because 2m ≤ N = p+1.
  - n* = max(p−1, 2κ+2−2m) ≤ 2κ for m ≥ 1, so the fillers satisfy n*−(p−1) ≤ R−2(p−1) = 2κ−p+1.
  - The Lemma M capping argument is valid.
  - RS(b) with K = p−1 on the p−1 nonzero swap differences reaches every residue. ✓
- **Lemma U (P:48–49).**
  - The class is unique because 2(2κ+1) > R = p+2κ−1.
  - For a = 0: pigeonhole gives y_i = y_k, hence a proper arc with m = 1 and T = 0. Then j = e is admissible and 2κ zeros give the identity. ✓
- **All-plus pattern (P:51).** j = e−1 gives A' ≤ κ. j = 0 gives A ≤ 2p−1, which uses 2p ≤ R. ✓
- **Window (W) (P:53).**
  - Under z_P, a has multiplicity A−d and −a has multiplicity A'+d.
  - Λ−λ = 2κ+2−A'−c. Substituting A' = p−1−c−δ gives p−2e+3+δ. ✓
- **Lemma MW (P:57–62).**
  - The omitted sum is K_j·s + Σ_J ω.
  - The values K_j·s are distinct because 0 < |2(j−j')| ≤ 2e−2 < p.
  - RS(b) gives |G_s| ≥ min(p, w0+1), and Cauchy–Davenport gives at least min(p, w0+q) sums. ✓
- **(MWe) (P:63–66).**
  - K_j = p−1+2(j−e) ≥ p−1 > w0, and q = min(e, r+1).
  - If r ≤ e−2, MW forces r ≥ p−2e+2−ε, hence 3e ≥ p+4−ε ≥ p+3, which contradicts 3e ≤ p+2. So φ ≥ p+κ.
  - This gives the split d ≤ c−e or d ≥ p+κ−A', with gap p+1+δ.
  - Complements swap type, because d(Pᶜ) = A−A'−d(P) and m(Pᶜ) = m(P).
  - Endpoint check, p=13 and e=5 (so 3e = p+2): K = 12,…,20. The case r ≤ 3 would need r ≥ 5−ε, which is impossible. So φ ≥ 21 = p+κ. ✓
- **Path (P:68–70).**
  - I checked each step: m = e is preserved whenever N ≥ 2e+2 (at p=13, N = 14 ≥ 12).
  - A removal step crossing the gap would need β_i ≥ p+1+δ > κ ≥ A', which is impossible. So the crossing step adds a run h with d_h ≥ p+1+δ. ✓
- **Light sets and counts (P:73–76).**
  - A high set avoiding h would give A ≥ α_h + Λ, i.e. 0 ≥ 3+2δ, which is impossible.
  - Then E+|Q| ≥ p−b = c+1 and |Q| ≤ d(Q) ≤ c−1, so E ≥ 2. ✓
- **Imports.**
  - Only NF, GRX (if direction), RS(b) (integer K, nonzero terms) and Cauchy–Davenport carry load.
  - UH-SH, UH-MW, UH-L, UH-E, KP3, KP4 and R7 are never invoked.
  - "As in UH-A" (P:17–18) is notation only: Lemma U defines the same unique majority class.

## 2. Lemma L (P:19–20, 80–87): HOLDS

**Setup.**
- w0 = p−1−g and φ = A−d = 2κ+g.
- K_j ≥ w0 ⇔ j ≥ e−g/2.
- K_j ≤ φ ⇔ j ≤ (p+1+g)/2, which is ≥ (3e−1+g)/2 because p ≥ 3e−2 (equality at p = 3e−2).

**Count.** Assume g ≤ e−1 and g ≤ 2m−2.
- **Case A** (m ≥ e−⌊g/2⌋): the count is at least min(e, ⌊(e+1+g)/2⌋), which is ≥ g+1. This case needs only g ≤ e−1 and m ≤ e.
- **Case B**, first branch: m+⌊g/2⌋ ≥ g+1 ⇔ ⌈g/2⌉ ≤ m−1, which follows from g ≤ 2m−2.
- **Case B**, second branch: ⌊(e−1+g)/2⌋+⌊g/2⌋+1 ≥ g+1, which follows from g ≤ e−1.

MW then requires q ≤ g, a contradiction. So g ≥ min(e, 2m−1).

**Scope.**
- It applies to every nonempty P avoiding h, including sets containing empty runs. Empty runs only fix positions and contribute 0 to d.
- Every j used is admissible for 1 ≤ m ≤ e. At m = 1 the lemma reduces to g ≥ 1.
- Nothing is claimed for m > e.

**Spot checks at p=13, e=5.**
- (m, g) = (2, 2): j ∈ {4, 5, 6}, so q = 3 and w0+q = 13, contradiction.
- (3, 4) and (5, 4): q = 5 and w0+q = 13, contradiction.

## 3. Lemma S (P:91–98): HOLDS

- J plus n−|J| copies of a sums to 2a(−j + Σ_J ω).
- "Free" (n ≤ A and n ≥ b) makes the allowed range of |J| equal to [0, b].
- At (N1), n = A+1 forces |J| ≥ 1, so t+j ∉ G_{≥1}, i.e. t+j ∈ M ∪ {0}.
- RS(b) with K = b gives |M| ≤ c.

## 4. Theorem A (P:21, 102–113): HOLDS

**(1) Independence bound.**
- Let M0 = ⌊(c+1)/2⌋+1. Then M0 ≤ ⌊e/2⌋+1 ≤ e, and 2M0−1 ≥ c+1 ≤ e.
- So Lemma L gives d ≤ −1 < 0 ≤ d(P), a contradiction.
- Selecting sub-intervals is legitimate, so the independence number of S is at most ⌊(c+1)/2⌋.

**(2) Parity and structure.**
- S misses h, so it is a disjoint union of paths, and Σ⌈L_i/2⌉ ≥ |S|/2 ≥ (c+1)/2.
- Hence c is odd, |S| = c+1, and every L_i is even.
- Both alternating classes of each path are maximum independent sets, so every run of S lies in one. For such a set, m = (c+1)/2 and 2m−1 = c < e, so d ≤ 0 and it contains no Q-run.
- Therefore Q = ∅ and there are exactly c+1 empty runs.

**(3) Missing-set contradiction.**
- m(Y) ≤ c+1 ≤ e, so j = e is admissible.
- n = 2κ ≤ A, and 2κ ≥ b ⇔ 2e ≤ p+1+c.
- RS(b) with K = c+1 on the c+1 nonzero t_i gives at least c+2 subset sums, hence at least c+1 nonempty sums, all in M−e.
- So |M| ≥ c+1 > c, a contradiction.

**Boundary c = e−1.** I checked it: 2M0−1 ≥ e, then 2m−1 = e−1 < e, then E = e gives m(Y) ≤ e. ✓

## 5. Theorem B (P:117–152, with E1, E2, M1, N1–N3): HOLDS

**Conventions.**
- A length is free iff 2j ≥ 10−c and j ≤ (p+1+c)/2.
- The largest j used is 7 for c ≤ 8 and 9 for c = 9; both satisfy the second condition for p ≥ 13.
- (N1) is at 2j = 9−c.
- I re-derived every singleton by lifting: a forced block avoids 0, so it has a unique lift in [1, p−1], and |M| ≤ c forces overlap with the base.
- I also re-derived every pair and triple. All pairs are covered; triples containing an excluded pair are excluded implicitly.

| c | base in M | singleton t | surviving pairs / sets | E | \|Q\| | position contradiction |
|---|---|---|---|---|---|---|
| 5 | [2,4] | −2, −1, 1 | t=1 gives M=[2,6], and a second run forces 7 or 8; **E1**: s=−3 fails at j=3, s=−4 at j=4, so only (−1,−1); a triple gives s+3=0 | 2 | 4 | m=3: 3>0; two components: 4>2; {q1}∪{q3,q4}: 3>2 |
| 6 | [2,4] | −1, 1, 2 | (1,1) adjacent, (−1,1); no triple | 2 | 5 | 3>1; 5>3; {q1,q2}∪{q4,q5}: 4>3 |
| 7 | [1,4] | −1, 1, 2 | (1,1) adjacent, (−1,1), (−1,2); only triple {−1,1,1}; no 4-set | ≤3 | ≥5 | 3>2; 5>4; {q1}∪{q3}∪{q5}: 3>2 |
| 8 | [1,4] | 1, 2, 3 | (1,1); (1,2) adjacent; no pair with 3; only triple {1,1,1}, consecutive | ≤3 | ≥6 | m=4: 4>3; 6>3; 6>5; {q1,q2}∪{q4}∪{q6}: 4>3 |
| 9 | [1,4] | 1..4 (t≥5: M is two-piece, and a pair forces t≡0 or −1) | M1 | ≤4; E=4 means four consecutive runs with t=1 | ≥6 | m=5: 5>4; 6>4; remove an interior run: 5>4; block ≥7: 5>4; block =6: {q1,q2}∪{q4,q5,q6}∪{e2}: 5>4 |

- Every forced block for c = 5..8 lies in [−4, 12]. Each block with a negative entry contains 0; the rest lie in [1, 12] ⊆ [1, p−1]. So N2's lift convention applies with no wrap at p = 13.
- Theorem A covers c = 3 and 4.

**M1 induction (the flagged step) is sound.**
- t_i ∈ [1, 4] is established first, so B0' = [1, t_max+5] ⊆ [1, 9] and |B0'| ≥ 6.
- For |Y| ≤ 5, m ≤ 5. Every j ∈ [m, m+4] ⊆ [1, 9] is then admissible (P:39) and free.
- **Inductive step:**
  - l(Y') ≤ l(Y)+5 ≤ 10 < p, since m grows by at most 1 and t_i ≤ 4. Also l(Y') ≥ 2.
  - So [l, l+4] ⊆ [2, 14]. Either it contains p, which is possible only at p=13 with l ∈ {9, 10}, and then 0 ∈ M, a contradiction.
  - Or it lies in [2, p−1]. Then 6+5 > 9 forces an integer overlap with B0', so M ⊇ [1, max(t_max+5, l+4)], giving l ≤ 5.
  - The cap l ≤ 10 is what rules out a lift lying wholly above p.
- **Conclusion:** |Y| = 5 would give l ≥ 6, a contradiction. So E ≤ 4, and E = 4 forces s = 4, m = 1. ✓
- **The original defect was real.** Old P:146–147 compared blocks as integers, but s+m can reach 25 for five runs. At p=13, [14,18] ≡ [1,5] was not excluded by the old PE remark, which handled only blocks crossing p.

## 6. Corollary B (P:23–24): HOLDS

- UH-A's literal antecedent holds at κ = p−5: p ≥ 7; (p−1)/2 ≤ p−5 ⇔ p ≥ 9; p−5 ≤ p−3.
- Its NF, H and empty-run clauses are identical to Theorem B's antecedent, including the existential "SOME admissible NF".
- Both texts orient the same class: the unique class with more than R/2 letters.
- So UH-A gives c ≥ 3, and A ≤ 2p−1 gives c ≤ 9.
- Theorem B excludes c ∈ [3, 9].

## 7. Residual note (R + RE + N4 + N5): exact, nothing beyond the proven range inferred

- **R1 (R:15–17).** The e-range and all listed examples are correct. In this range c ≤ 2e−1 comes from UH-A and the frozen R-UH definition, not from P:51 (which needs 2e ≤ p−1), and R does not claim otherwise.
- **R2 (R:18–23).** Every listed item is proved on the whole SH range; Sections 3–5 never use c ≤ e−1 or e = 5.
  - The base is [e−μ, e−1], because free ⇔ j ≥ ⌈e−c/2⌉.
  - The extra residue e−μ−1 is the all-plus (N1) length; it is nonzero iff c ≤ 2e−3.
- **Completeness (R:24).** The frozen range splits into:
  - R1, the non-SH range;
  - SH with e = 5, covered by Theorem B;
  - SH with e ≥ 6 and c ≤ e−1, covered by Theorem A;
  - SH with e ≥ 6 and c ≥ e, which is R2.
- **Failed-route notes.**
  - The F1–F5 arithmetic checks.
  - **F1 (with N4):** the bound φ ≥ 3p−4e+3−ε is right. At N = 2e only the two alternating sets have m = e, so no toggle path exists there.
  - **F2 (with N5):** two disjoint high sets ⇔ A' ≥ κ+1−c/2. Since A' = b−δ, this is equivalent to c+2δ ≤ 2e−4, and the equivalence is safe for odd c.

## 8. Erratum-2 repair audit

| Item | Repaired? | Scope |
|---|---|---|
| M1 (P:146–147, PE:35–36) | Yes; induction verified in §5 | unchanged |
| N1 (P:117) | Yes; every use has m ≤ 5 (c=8 uses 2, 3, 4; c=9 uses 3, 4, 5) | restriction |
| N2 (P:119) | Yes; the claim is false (−4≡9, −3≡10 mod 13) and the convention covers every comparison | weaker |
| N3 (P:139) | Yes; an adjacent (1,1) pair gives [3,7], so only [1,7] is forced | none |
| N4 (R:27–29) | Yes | route prose |
| N5 (RE:17) | Yes | route prose |

X2's statement that no statement changes (X2:119–122) is accurate.

## 9. Findings and minimal repairs

**MINOR-1.** `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/upperhalf-RUH-round2/residual-RUH2-v1.md:41`
- The heading "Smallest missing claims of these routes" asserts a minimality that nothing proves.
- It conflicts with R:5–7 and with package line 53.
- It is the same overstatement that parent erratum v2 item 2 removed from the R-UH obstruction.
- **Repair:** "## 4. Missing claims of these routes (route targets only; no minimality or necessity asserted)".

**MINOR-2.** `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/upperhalf-RUH-round2/residual-RUH2-v1.md:44`–46, the MC2 parenthetical.
- E ≤ ⌈c/2⌉−1 matches §7 (2, 2, 3, 3, 4).
- "Maximal case a block of consecutive empty runs of equal value" holds only at c = 8 and c = 9. It fails as a description at:
  - c = 5: (−1,−1) survives both adjacent and non-adjacent. Adjacent gives s+{3,4,5} = {1,2,3} with s+2 = 0 under (N1); non-adjacent gives [1,4].
  - c = 6: (−1,1) survives.
  - c = 7: the only surviving triple is {−1,1,1}.
- The "e=4 lists" are KP4's (candidate and outside this packet). Nothing depends on this parenthetical.
- **Repair:** "(at e=5, proof Sec. 7 gives E<=ceil(c/2)-1 for c=5,...,9; at c=2e-1=9 the only E=4 configuration is four consecutive empty runs with t=1; KP4 is not used)".

## 10. Editorial notes (not counted, optional)

- **P:143.** "All j>=1 are free" should be read as "all j ∈ [1, 9]". E2's preamble already covers every length used.
- **P:141.** The four-run line checks only m = 1. Every 4-set already contains a non-consecutive triple, which the triple list excludes.
- **P:130.** Triples containing t = 2 are omitted; each contains an excluded pair.
- **N2.** "Contains 0 ⇒ excluded" applies to free-length blocks. The (N1) element may be 0 (t = −2 at c = 5, t = −1 at c = 7); the text handles those cases explicitly.
- **Package line 48.** "Residues <=10 distinct" is stale: c = 8 uses residues up to 12, and c = 9 uses lifts up to 14. The package also does not list X2. This is metadata only.
