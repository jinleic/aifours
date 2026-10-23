# Hostile review: Theorem PP1-EXCL v1

**Object:** `proof-PP1-EXCL-v1.md` (`6fea2fd2…0944d0`), lines 1–248, reviewed against frozen scope `PP1-EXCL-scope-v1.md` (`d386f944…2fba`).

**Method:** written review only by claude-opus-5-5. I used no tools, ran no computation, made no edits and delegated nothing. Hashes, byte counts and line numbers come from the supplied package and were not recomputed.

## 0. Verdict

**FATAL 0 · MAJOR 0 · MINOR 5, plus 1 optional hardening.** Every mathematical step checks. All five MINORs are in consequence sentences, remarks, the import table or notation. None touches a proof step.

| Claim (lines) | Verdict |
|---|---|
| Theorem PP1-EXCL, p ≥ 7 (17–19) | **ACCEPT**, relative to NF, GRX, CT and RS(b) at their accepted scopes |
| Theorem PP1-EXCL′ (23–25) | **ACCEPT** |
| Theorem EXCL-PM, conditional (27–28, 81–110) | **ACCEPT**; its only input is GRX, as stated |
| §2.1 reduction (60–62) | ACCEPT |
| §2.2: SEL, P0/P1/P2, direct check (64–79) | ACCEPT (o6 is optional) |
| Lemma W (86–90) | ACCEPT |
| Lemma CL (119–142) | ACCEPT |
| Lemma OM / OM′ (144–156) | ACCEPT |
| Lemma SR (158–165) | ACCEPT |
| Lemma ER (167–185) | ACCEPT |
| §4.5: H2a, H2c, H1 (a = 0), H1 (a ≠ 0) (187–205) | ACCEPT |
| Conditional reading and "logical consequence" (29–34) | ACCEPT-WITH-FIXES (m1) |
| §5 remarks (209–217) | ACCEPT-WITH-FIXES (m2, m5) |
| §6 import table (231–237) | ACCEPT-WITH-FIXES (m3) |
| Notation across the file | ACCEPT-WITH-FIXES (m4) |
| [NEW]/[RE-DERIVED] labels | Accurate; see the accounting note in m5 |

File-level verdict: **ACCEPT-WITH-FIXES.** The outcome is (O1) of the scope. The §0 statements match the frozen target, with no silent substitution.

## 1. Step audit

**§2.1 Reduction.**
- κ^ = p−1 ⇔ H^ = Σ(l_i−1)/2 = 0 ⇔ every odd l_i equals 1. So F = k = p+1 and R = 3p−3 = 2p+2κ^−k. ✓
- NF line 37 makes w^ an avoider. PM* transfers avoidance in the original→reduced direction only (lowodd item 2), and that is the only direction used: the contradiction is produced inside w^.
- k = p+1 is even, which is admissible: NF fixes only k ≡ o (mod 2).
- Cyclic reading is exact:
  - changing the cyclic cut conjugates the product;
  - singleton blocks cannot be split by the cut;
  - a run split by the linear cut is harmless because rotations commute.
- Only output properties of the terminal form are used, so the result covers every admissible normal form (the universal reading of ZX overlay 2). ✓

**§2.2 Selection rule and patterns.**
- With l_i = 1, [l_i ≢ f_i] = [f_i = 0]. So δ = p+1−Φ, C_max = Φ, and the only choice is C = Φ.
- 0 ≤ 2p−Φ ≤ 2p ≤ 3p−3 holds.
- P1: |J| ≤ p leaves a nonempty complement, so f = 1 exactly at the distinct blocks S_(i−1) and S_j.
- P2: i−1, i, l−1, l are pairwise distinct ⇔ l ∉ {i−1, i, i+1}.
- I re-derived every pattern family from the group law alone, with A = sum of the selected letters in positive runs and B = sum in negative runs:
  - Arc J = {i..j}, read from R_(j+1): product (A + y_(i−1) − B − y_j, +1), so the condition is A − B = y_j − y_(i−1).
  - P2, read from R_(i+1): product (A − B + y_(l−1) − y_l + y_(i−1) − y_i, +1), so the condition is A − B = τ_i + τ_l.
- Both agree with GRX's T(z) under the M2 convention, so the file has no sign-convention exposure anywhere.

**Lemma W.**
- With n = 2p−2, the feasible q form the interval [max(0, n−E_+), min(n, E_−)].
- If E_± ≥ p−1, then E_+ + E_− = 3p−3 gives the interval [E_−−p+1, E_−], which has exactly p integers.
- The sums (n−2q)c then cover Z_p, because 2c is a unit.
- The boundary cases E_+ = p−1 and E_− = p−1 also check. ✓

**EXCL-PM.**
- **Step 1:** the sum −2qc vanishes ⇔ p | q. The feasibility conditions for q ∈ {0, p, 2p} are as stated. A, B ≤ 2p−1 and p−2 ≤ min(A, B) ≤ p−1 leave exactly two cases.
- **WLOG A ≥ B:** the swap c ↔ −c exchanges A↔B, E_+↔E_− and a_i↔b_i. It leaves the hypothesis, Lemma W and Step 1 invariant, and Step 3 needs only that −2c is a unit.
- **Step 2:** E_− = B − b_i + a_i is correct.
  - Case (2p−2, p−1): a_i ≥ p holds in at most one run (2p > 2p−2). The other ≥ p runs need b_i ≥ a_i+1 ≥ 1. Empty runs fail the same inequality.
  - Case (2p−1, p−2): a_i ≥ p+1 holds in at most one run (2p+2 > 2p−1).
- **Step 3:** an empty run gives E_+ = 2p−1 and E_− = p−2, so q ∈ [0, p−2]. The sums −2(q+1)c cover exactly Z_p∖{0}. τ_i ≠ 0 by the empty-run rule, so u has no empty run. The final count then works.
- The scope's E1 in its w-form equals EXCL-PM + §2.1 + rotation-multiset invariance (lines 29–30). It uses NF and GRX only, as frozen. ✓

**Lemma CL.**
- (Z) is P0. Y(x) = (1, x) is odd, and every 2p-subsequence has C₂-coordinate 0. So (Z) is exactly (ZP_(p−1)), since [2κ+2, 2p] = {2p}.
- CT instance:
  - κ = p−1 lies in [0, p−1];
  - n = p−3 lies in [1, 3p−3] (needs p ≥ 4);
  - |Y|−n = 2p is even and in {2p};
  - so Σ min(p−3, v_x) ≤ 2p−5.
- Heavy values contribute p−3; the rest contribute v_x (consistent at v = p−3).
  - No heavy value: 3p−3 > 2p−5.
  - Three heavy values: 3p−9 > 2p−5 (needs p > 4).
  - One heavy value: v_a = 2p−1.
- Two heavy values:
  - ε ≤ 1, and the feasibility window for j is correct.
  - v_b ∈ {p−2, p−1}. A tie v_a = v_b is impossible, since 2v ≤ 2p−2 < 3p−4.
  - With ε = 1, j* = 0 ⇔ c = a and j* = p−1 ⇔ c = b, so j* ∈ [1, p−2]. Since j*+p > v_b, j* is the only candidate j.
  - (2p−2, p−2): always feasible, so impossible.
  - (2p−3, p−1): feasible ⇔ j* ≥ 2, so j* = 1 and c = 2a−b. a, b, c are distinct since p is odd.
- The three types are mutually exclusive by their top multiplicity. ✓

**Lemma OM / OM′.**
- The omitted set is C plus K−|C| a-letters of Π_+. These are disjoint because the fillers are not free.
- The remaining set has 3p−3−K = 2p−2m letters, with signed sum D − aK − Σ_C ω = T. ✓
- OM′: K ≥ p−1, and both branches give Σ_x min(K, v_x(N′)) ≥ p−1. RS(b) then gives Σ_(≤K)(N′) = Z_p.
- OM′ is used only with m = 1. ✓

**Lemma SR.**
- The free letters are:
  - non-a letters outside R_i, with weight u−a ≠ 0;
  - every letter of R_i, with weight −u−a, which is zero ⇔ u = −a.
- So there are exactly β_i zero weights.
- a ≠ 0: the a-letters of R_i have weight −2a ≠ 0.
- a = 0: the zero weights in R_i are its α_i zero-letters, and β_i = α_i. The count N + α_i − β_i = N still holds. ✓

**Lemma ER.**
- B~ has nonzero terms, because in H1 no letter of B equals a.
- RS(b) with K = p−2 gives |Σ(B~)| ≥ p−1.
- Complements give an involution on Σ(B~), and σ(B~) = σ(B) + 2a.
- If all negative runs are empty, then N_z = B~ and D = (2p−1)a + σ(B). This makes explicit the point the parent erratum on ROT-SING+ flagged.
- (i): D−aK−T = pa + σ(B) − τ_i. This gives Σ(B~) = Z_p∖{r0} with r0 ≠ 0, and τ_i = r0−2a for every empty run.
- (ii): forces τ_(i+1) = 0, which contradicts y_i ≠ y_(i+1).
- (iii): K = p+1 ≤ 2p−1, and D−aK−T ≡ σ(B)−2a−T. This gives T+4a = 2r0 = r0, so r0 = 0, a contradiction. ✓

**§4.5 Eliminations.**
- **H2a:** at least p runs need β_i ≥ α_i+1, but N = p−1. This also kills the ROT-SING+ survivor b = −a.
- **H2c:** at least p runs need β_i ≥ α_i+2, but N = p. The argument is uniform in −a ∈ {b}, {c} or neither.
- Empty runs are included in both H2a and H2c, since α = β = 0 violates the forced inequality.
- **H1, a = 0:** the arc j+1..j′ has 1 ≤ |J| ≤ p. Its T = 0 is met by any 2p−2 zero letters, whatever their signs.
- **H1, a ≠ 0:**
  - every run with α_i ≤ p needs β_i ≥ α_i;
  - so there is a unique run R_h with α_h ≥ p+1;
  - the p other runs share N = p−2 non-a letters, so at least two of them are empty;
  - this contradicts ER. ✓

**Cross-check of the two routes.** Under the pair hypothesis with a = c:
- In H2a (b = −a), SR's condition β_i ≥ α_i+1 is literally EXCL-PM's b_i ≥ a_i+1.
- In H1 with B = (−c)^(p−2), Σ(B~) = Z_p∖{2c}. So ER (i) forces τ_i = 0, which is exactly EXCL-PM Step 3.

**p = 7 instance.** K = 6, n = 12, |Y|−n = 14, and v_a ∈ {13, 12, 11}. Every comparison holds.

**Attempted breaks, all of which failed:**
- fillers colliding with C;
- P2 change blocks coinciding;
- an arc with |J| = p+1 in H1 (a = 0);
- Σ(B~) = Z_p in ER (i) (that case is already an identity);
- a = 0 inside OM, SR and H2a/H2c;
- SR evaluated at empty runs;
- a second run with α_i ≥ p+1, α_i ≥ p or α_i ≥ p−1.

## 2. Findings

**m1 — MINOR (scope wording), lines 33–34; also line 29.**
- **Line:** "…ROT-SING+ holds vacuously and its rotation multiset describes no avoider."
- **Failure:** Read literally, this says no length-(4p−2) avoider has rotation multiset ρ_c^(2p−2) ρ_(−c)^(p−1). That is not proved here:
  - the multiset forces F = p+1, hence even k and κ^ = (p−3+k)/2;
  - cells such as (k, κ^) = (p−1, p−2), which DAV's κ^ ≤ k−1 does not exclude, are untouched by this file;
  - the literal reading also contradicts the file's own non-claim at lines 225–226.
- **Failure (line 29):** "asserts exactly this pair hypothesis" understates ROT-SING+, which asserts the exact multiset.
- **Fix:** replace the sentence with: "so for p ≥ 7 no avoider has an admissible normal form in this cell; ROT-SING+ is then vacuously true at its own scope (a consequence of PP1-EXCL, not a validation of the ROT-SING+ proof); nothing is asserted about that multiset in other (k, κ^) cells." At line 29, use "asserts in particular this pair property".

**m2 — MINOR, lines 216–217.**
- **Failure:** the list of "where k = p+1 is used" omits R = 3p−3, which is load-bearing in:
  - Lemma W's window length p = (3p−3)−(2p−2)+1;
  - Step 1's two (A, B) cases;
  - Step 3's range q ∈ [0, p−2];
  - CT's n = p−3 and |Y|−n = 2p, and hence the types of Lemma CL;
  - K = p−3+2m;
  - the cancellation (2p−1)a − (p−1)a = pa in ER (i).
- **Fix:** add these items to the list.

**m3 — MINOR, lines 236–237.**
- **Failure (RS(b) row):** RS(b) is invoked only at K = p−1 (OM′ via SR) and K = p−2 (the ER bound). The values "K = p−1 (ER (i)–(ii))" and "K = p+1 (ER (iii))" are omission budgets of Lemma OM, which does not use RS.
- **Failure (Cauchy–Davenport row):** "only inside RS(b)" omits that CT's proof uses RS(a), which is also iterated Cauchy–Davenport.
- **Fix:** correct both cells. There is no validity impact.

**m4 — MINOR (notation), lines 67, 77, 92, 121, 123, 126, 150.**
- **Failure:** several symbols are overloaded:
  - u is both the word and a letter, in one sentence at line 67;
  - B is a count (line 92), a run sum (line 77) and a sequence (line 121);
  - C is the reflection count and also the free-letter set (line 150);
  - c is the pair generator in §3 and the third letter in H2c (line 123);
  - line 126's v_x(Y) means v_(Y(x))(Y).
- Every use is local, so no step is affected.
- **Fix:** rename the clashing symbols.

**m5 — MINOR (accounting), lines 209–213.**
- The labels are accurate under the file's own definitions (§4 below). The issue is progress accounting relative to the pending ROT-SING+.
- **Failure:** the text does not say that the only conclusion not already claimed in ROT-SING+ is the exclusion of H2a with b = −a.
  - H2c is a new argument for a conclusion ROT-SING+ §6 already claims.
  - EXCL-PM's case (2p−1, p−2) re-proves a sub-case of H1.
- **Fix:** add one sentence saying this.

**o6 — optional hardening, lines 76–79.**
- **Suggestion:** add the arc and P2 products from §1. Every pattern used would then be checked from the group law, and GRX would serve only as a cross-check.

## 3. Where k = p+1 and p enter

**k = p+1 is load-bearing through three channels:**
- **Singleton blocks with F = k:** C_max = Φ, so there is no reflection slack.
- **R = 3p−3:** see m2.
- **p+1 runs:**
  - "at least p runs" in §3 Step 2 and in H2a/H2c;
  - "at least two empty runs" in H1 (a ≠ 0) — with only p runs there would be one empty run, which ER permits;
  - p+1 > |Z_p| in H1 (a = 0).

**p-dependence:**
- CT needs p ≥ 5.
- n ≥ 1 needs p ≥ 4, and excluding three heavy values needs p > 4.
- P2 needs k ≥ 4.
- Everything else needs only an odd prime p.
- Nothing uses p ≥ 7. The parenthetical "k ≥ 8" at line 69 is true but unused.
- Line 34 is accurate as a statement of dependencies. **This review gives no approval for p = 5.**

## 4. Labels

| Item | Label | Assessment |
|---|---|---|
| Lemma CL | RE-DERIVED | Accurate. Same argument as ROT-SING+; the j* range is now stated correctly (ROT-SING+ line 59 wrote p−1 and repaired it in lines 60–61) |
| OM / OM′, ER, H1 (a = 0) | RE-DERIVED | Accurate |
| H1 (a ≠ 0) | RE-DERIVED via SR | Accurate; same inequality, now also covering α_i = 0 |
| SR | NEW in this form | Accurate; a routine single-run specialisation of OM′ |
| Lemma W, EXCL-PM | NEW | Accurate; not in ROT-SING+ |
| H2a | NEW | Accurate; new argument and new conclusion |
| H2c | NEW | Accurate as "written here"; the conclusion was already claimed by ROT-SING+ (m5) |

## 5. Import-domain audit

| Input | Instance used | In scope? |
|---|---|---|
| NF (ROT-few-E-v4 lines 28–43; fewodd addendum line 12; ZX overlays 1–3; lowodd item 2, M1, M4) | Terminal-form outputs only: w^ is an avoider of the same length; cyclic representation with odd blocks; empty-run rule; formulas for H^, κ^ and R | **Yes.** See note below. |
| GRX (notes-GRX lines 7–20; lowodd item 1, M2) | "If" direction only; Φ ∈ {0, 2, 4}; C = Φ | **Yes**, and every instance was also verified directly (§1) |
| CT (LSplus-e2 lines 13–19; STAB-delta item 6) | κ = p−1, n = p−3, \|Y\| = 3p−3 | **Yes.** See note below. |
| RS(b) (ROW lines 16–27 with R5; CFXT item 4) | Integer K = p−1 and K = p−2, nonzero terms in both | **Yes** |
| Cauchy–Davenport | Inside RS(a) via CT, and inside RS(b) | Classical import |
| Excluded premises: ROT-SING+, ROT-SING, ONE-SHORT-LS, ASSEMBLY-P, ROT-PP1, (S1), Lev, S(p), index-one, REFL | None | None is used in §§2–4. ROT-SING+ appears only in lines 29–34 |

**NF note:**
- The addendum's restriction (o_F ≤ k, calls with k ≤ (2p+4)/5) attaches to SHgen-E, which this file does not use. The output properties it does use are k-independent.
- PM* is used in its accepted direction only.
- κ^ is an integer, and the existential normal form is read universally.

**CT note:** item 6 states its range 0 ≤ κ ≤ p−1 explicitly. STAB-delta line 9's default range governs only LS/LS+/STAB claims.

No input is used outside its accepted scope, and I found no gap.

## 6. Trust boundary

**Reviewed:** the full proof, the scope, the slot transition, and the quoted input and verdict excerpts, all as reproduced in the package.

**Not done:**
- Hashes and line ranges were not checked against disk.
- Pre-freeze timing was not verified. The written route (s1)–(s3) does match Lemma W, EXCL-PM, and SR in H2a/H2c.
- I did not review the input proofs. I checked only that each input is applied within its stated hypotheses; the quoted CT and RS proofs are consistent with those uses.

**Accepted as given:** the acceptance status of each input, taken from the quoted verdicts and your prompt.

**Unresolved status:** ROT-SING (k = p) is called "accepted" at scope line 45 but "pending" at ROT-SING+ line 140. It appears only in the non-load-bearing remark at lines 112–115, which this review neither accepts nor rejects.

**Not approved:**
- reflection rigidity;
- INV*;
- any other (k, κ^) cell, including (p−1, p−2);
- any o_F statement or assembly;
- ordered Olson for D_(2p) or for all groups;
- p = 5;
- Lean or human review;
- novelty or priority;
- ROT-SING+ through its own proof.
