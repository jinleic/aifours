# RPdelta v2: independent hostile review (second family)

**Basis.** I used only the embedded text: the 8 candidate files, consolidated erratum `2450446d`, the packet, and the import excerpts. V5 `13ee1ba8`, with its bindings S1/m1–m7, served as the interface authority. RP-LIFT and RP-2NE were not used. The only computation was hand algebra on the printed formulas. The Codex verdict played no part.

## Verdicts

| Group | Verdict | FATAL / MAJOR / MINOR |
|---|---|---|
| SEG-k (K + K-e) | **ACCEPT-WITH-FIXES** (documentary) | 0 / 0 / 2 |
| INV, TRANSFER, T1–T3 | **ACCEPT-WITH-FIXES** | 0 / 0 / 1 |
| B.1–B.3, Theorem B, B.4 (+B-e1, B-e2) | **ACCEPT-WITH-FIXES** | 0 / 0 / 2 |
| B′ (+BP-e) | **ACCEPT-WITH-FIXES** | 0 / 0 / 2 (shared with B) |

- No fix changes a statement, range or proof step.
- I verified E1–E5 independently. All five are correct and binding.
  - E1: the ledger is exact.
  - E2: the qualifier is correct.
  - E3: there is no circularity, because certified gain ≤ total < Π_need < p−1 forces gain = 2t on an unsaturated segment.
  - E4 (a)–(c): each holds. For (c), R=19, d=2 gives b−a=0 < ⌊d/2⌋.
  - E5: correct; its exact non-vacuous scope is given in §3.

---

## 1. SEG-k

**Checks**

- **(i)** q ≥ k−2κ. This follows from (P0) with e_F=0, since odd runs are nonempty.
- **(ii)** q ≤ R and d ≤ R−q+1.
- **(H1)**, with a=⌈(R−d)/4⌉, b=⌊(R+d)/4⌋, c=⌈R/2⌉:
  - **a ≤ κ.** The width is H−(b−a). Since b−a is an integer ≤ d/2, the width is ≥ H−⌊d/2⌋. It suffices that c−⌊d/2⌋ ≥ κ+2. That holds because c−⌊d/2⌋ ≥ (R−d)/2 ≥ (q−1)/2 ≥ (k−2κ−1)/2 ≥ κ+2, and the last step is equivalent to k ≥ 4κ+5.
  - **a ≥ κ+1.** Here (H1) is equivalent to c−b ≥ 2. Since c−b is an integer ≥ (R−d)/4, it is ≥ a ≥ κ+1.
    - For κ=0: R−d ≥ q−1 ≥ k−1 ≥ p ≥ 5, so a ≥ 2.
    - K-e correctly withdraws K18's wrong-direction claim, and nothing relies on it.
- **(H2)**
  - n_CA ≥ (3q−k)/2 ≥ k−3κ.
  - 2m_lo+2 = max(4, 2κ+4−2a), with 2a ≥ (k−2κ−1)/2.
  - The two needed inequalities are 3k ≥ 12κ+9 and k ≥ 3κ+4. Both follow from k ≥ 4κ+5 when κ ≥ −1.
  - κ<0 is excluded by (Pairs), and R=0 by AR.
- **(H3)** g_E ≥ k−R ≥ Π_need+1, which is equivalent to the second hypothesis.
- **Π_need branch.** The hypotheses give R = 2p−k+2κ ≤ 2p−2κ−5 ≤ 2p−5. So Π_need ≥ 2 and only SEG's I.12 loop is used.
- **D1/D2.**
  - The substitution is correct.
  - The endpoints are correct for both parities, and the condition p ≥ 5δ+11 is right.
  - In the example (29, 2, 9, 45), (H3) holds with equality.
  - At δ=0, D1 = [⌈(p+1)/4⌉, ⌊(p−5)/2⌋] lies inside the I.14 R=p row, and it is empty for p=5, 7.
  - In the Range paragraph, the even-k threshold (4p+2κ+1)/3 is equivalent to (4p+2κ+2)/3 by parity, so there is no overclaim.

**Findings**

- **MINOR K-1 (K-e e3).** The justification of Π_need ≥ 1 cites erratum-4, which is not in the packet.
  - Repair: use the one-line bound above, R ≤ 2p−2κ−5.
  - V5 accepts SEG for every R in any case, so this is not load-bearing.
- **MINOR K-2 (K36).** The phrase "same lower condition κ ≥ (p+3δ+2)/4" is false for even δ with p+3δ ≡ 3 (mod 4).
  - In that case SEG-k's lower endpoint is (p+3δ+1)/4, which is exactly E/D2. The containment claim itself survives.
  - E can also occur where the SEG-num band is empty. Example: p=31, δ=4 gives E={11} and SEG-num = [12, 11]. That point still lies outside A.
  - Repair: record that K34–41 are superseded by D1/D2 and E1.

## 2. INV / TRANSFER / T1–T3

**Checks**

- **Moves on the actual maximal decomposition (ΔA, ΔB, ΔH):**
  - P1: (0, 0, [double fusion with both outer blocks odd]).
  - P2: (0, 0, 0). The even block l_j is appended, and the merged run is nonempty, so nothing fuses.
  - P3: (0, 0, 0). The filled run lay between distinct values.
  - P4: (−1, −1, 1 + [the fusing neighbours are both odd]). The pair is inserted into a block of the same value (MON L99–101), so nothing splits. This is the V-RED39 correction.
  - Hence D is constant, ΔB ∈ {0, −1} and Δg ∈ {0, −1}.
  - Cross-check: g_T ≤ g_0 is equivalent to k_T ≤ o_F(w0), which is accepted MON.
- **Terminal.**
  - B_T < κ_T gives g_T ≥ 1.
  - All-odd (0.1) gives k_T = 2p−D_0+2g_T.
  - Fact 2.2 gives R_T ≥ p.
- **Dependency.** RED's accepted proof (I1–I4, K0*, B=K, K1*, TII, SING, QQ) never uses INV or TRANSFER. TRANSFER runs RED's process on the given w0, so it inherits RED's conditional import base. There is no cycle.
- **Clause hypotheses.**
  - (a) applies because the terminal lies in RES_<.
  - (d) is the p ≥ 11 row of I.14; κ ≤ p−1 is automatic.
  - (f): B_T=0 means all rotations are ρ_1 and κ_T ≥ 2. EDGE Cor.2 applies under R ≥ 4κ−4. The R ≥ 2p cut is never needed, because R_T = D_0 ≤ A_0 ≤ 2p−1 by (Z0).
- **E2.** A nonempty box contains (g_0, B_0), so some cell has R ≥ p iff D_0+2B_0 ≥ p.
  - An empty box (g_0 ≤ 0, or g_0=1 with B_0=0) gives the conclusion vacuously.
  - Under D_0 ≤ 1, a nontrivial box forces B_0 ≥ (p−1)/2, κ_0 ≥ (p+1)/2 and o_F = 2p−D_0+2g_0 ≥ 2p+1.
- **T1–T3.** The algebra is correct, and (0.1) is valid for w0 even when it has even blocks.

**Finding**

- **MINOR T-1 (T59–60).** "box minimum of 2g−b at (1, B_0) … iff": when B_0=0, the cell (1, 0) is not in the box, so the condition is only sufficient.
  - Repair: "on the box 2g−b ≥ 2−B_0, so it suffices that A_0+⌊D_0/2⌋ ≤ p+1".
  - T2 is unaffected.

**Scope note (not a finding).** TRANSFER excludes exactly the cells covered by (a)–(f). As written it does not certify cells that only the following would cover:
- the SEG-num top cell κ=(p−δ−4)/2 for odd δ, which (c) misses;
- B/B′;
- the p=5 and p=7 rows of I.14;
- raw structural SEG.

## 3. B.1–B.3 / Theorem B / B.4

**Checks**

- **Headers.** The headers B6–10 and BP4–5 are stale. Read them through V5. The proofs are compatible with e5 I.1–I.7 and with S1/m1.
- **B.1.** Items (i)–(iv) hold, including a+c ≥ (p+4δ−3x+1+2ε)/2.
- **B.2.**
  - (v): m_lo is defined without a max, and m_lo ≥ 1 is proved.
  - (vi): this is the exact identity H−(b−a) ≥ H−⌊d/2⌋.
  - (vii): needs d+3−4ε ≥ 0.
  - (viii): is only a sufficient condition (E4a).
  - (ix): follows by subtraction.
  - In addition, N_O ≤ (p+7−4ε+δ)/2 ≤ p, so V5 m2 holds here too.
- **Construction.**
  - The base is toggled per S1/m1, with at most one base arc per run. Σc = N_O ≥ 4 is even.
  - |O| ∈ {N_O−2, N_O} and m_b ≥ m_lo ≥ 1.
  - |L∩O| ≤ λ+1, and G_b ≥ min(a, N_O)+λ−2.
  - The identity G_b+W2+W1 = g_E−|L∩O| checks term by term: AB∖O contributes 1, L∖O contributes e_j, and L∩O contributes e_j−2.
  - The segment formed by blocks 3.. of an L-run lies in the gap after its pair-arc. Several segments in one gap are covered by I.1.
  - The L base is a two-block arc that is toggled directly; neither SEG's singleton base nor the e5 recipe is involved.
- **Allocation.**
  - Σt ≤ max(⌈G_need/2⌉, G_need−W2/2), using that W2 is even and W1 ≥ G_need−W2.
  - The E3 invariant holds.
  - Rate-1 units are used only after all rate-2 units.
- **B.3.** |T| ≤ d and m ∈ [m_b, m_b+Σt] ⊂ [m_lo, m_hi] give both windows, using the I.5 endpoint check.
- **Theorem B.**
  - The B-e1 sign is correct.
  - Case a > N_O: G_b+r ≥ N_O ≥ Π_need, Σt ≤ 2, and the width is ≥ 3 provided δ ≤ (p−7)/2+ε.
  - Potential: λ=0 needs 3δ ≤ p−4−4ε, and λ>0 needs δ ≤ p/2−5+ε.
  - Budget: the second bound expands to p+δ+20+4ε−2x ≤ 3p−9+6ε−6δ, which is equivalent to 7δ+29−2ε−2x ≤ 2p.
  - The Range statement, the k-form and the examples (31: 4, 5; 101: 24, 25) are correct.
- **B.4.** Only the last inequality uses the hypothesis. The inequality is correctly strict, since the equality case kills. The g_E form is equivalent.

**Findings**

- **MINOR B-1 (B27, B30; BP17).** The proof uses d ≥ 1 without justification. It is needed in (vii) when ε=1, and it underlies the (R+2)/4 bound in (v).
  - Repair: (P0) gives at least k−2κ = p−δ ≥ 1 odd runs. An odd run has odd a_j−b_j, so d ≥ 1 even when runs are mixed.
- **MINOR B-2 (B67, B71–73; BP24–25).** "G_need ≤ Π_need−a−λ+2" is false when the right-hand side is negative (then G_need=0). In that case the chain leading to Π_need−(2/3)a−g_E/3+3 is unjustified.
  - Harmless: G_need=0 gives Σt=0, and B.3 then needs only m_hi ≥ m_lo+1.
  - Repair: write max(0, ·), and use the nontrivial chain only when G_need > 0. This is the packet's §4.5 reading; move it into an erratum.

**Observation (not a finding, not accepted).** Given B′, B.4 is non-vacuous only at (p, ε, δ) = (17, 0, 1), where it forces x=0 and a ≤ N_O.
- Why only there:
  - B.4's range requires p ≥ 17.
  - For p ≥ 20+2ε, B′ covers that range.
  - Among p ∈ {17, 19}, only (17, 0) has an empty B′.
- At that cell, x=0 also meets every B′ condition in its x-form: F1 (0 ≤ 6), F2 (δ+x+32−2ε = 33 ≤ 34), validity and potential. B's own chain kills x ≥ 1.
- So the written arguments would exclude this cell too. The package does not claim it, and do

es not need it. Using it would require a separate written addendum and its own review.

## 4. B′

**Checks**

- **Validity is rechecked without B.2's range.**
  - m_lo ≥ 1 is ensured by δ ≤ p−4−4ε.
  - N_O ≤ q is ensured by 3δ ≤ p−7+4ε.
  - (vi), (vii) and (ix) are range-free once d ≥ 1 is supplied (B-1).
  - At ε=1 the range reaches 3δ = p−8. There, the λ=0 potential (3δ ≤ p−4−4ε) and F1 hold with equality and remain valid. B.2 is never invoked beyond its own range.
- **(\*)** holds, since ⌊d/2⌋ ≤ ⌊(x+1)/2⌋ follows from d ≤ x+1.
- **Case a > N_O** needs (p−12+4ε)/3 ≤ (p−7+2ε)/2, which is equivalent to p ≥ 2ε−3.
- **λ > 0** needs (p−12+4ε)/3 ≤ p/2−5+ε, which is equivalent to p ≥ 6+2ε.
- **F1** is an exact "iff": 4⌊(x+1)/2⌋ ≤ p−12+4ε+δ, and since ⌊(x+1)/2⌋ ≤ δ, the condition 3δ ≤ p−12+4ε suffices.
- **F2.** After multiplying by 6, the left side is p+δ+20+4ε−2x and the right side is 3p−12+6ε−3x. This is equivalent to δ+x+32−2ε ≤ 2p, and x ≤ 2δ makes 3δ ≤ 2p−32+2ε sufficient.
- **Range.**
  - The first term of the min binds iff p ≥ 20+2ε.
  - Examples check: p=19 gives 2, 2; p=31 gives 6, 7; p=101 gives 29, 31.
  - The range is nonempty iff p ≥ 19 (ε=0) or p ≥ 17 (ε=1); at p=17, ε=1 it is δ=1 only.
  - BP-e is correct: at p=19, B gives δ ≤ 1 for both ε.
- **B ⊆ B′ whenever B is nonempty.**
  - The first comparison is equivalent to p ≥ −3−22ε.
  - The second is equivalent to 8p ≥ 137−8ε, which holds exactly where B is nonempty.
- **E4(b) and E5** are worded correctly, and the E5 example (17, 0, 1) is right.

**Findings:** B-1 and B-2 apply verbatim (BP17, BP24–25). There are no others.

## 5. Coverage claims against accepted I.14 (E1 ledger)

All coverage claims check out:

- **Increments.** For δ ≥ 1, the universal accepted numerical exclusions are exactly A (V5 l.40). SEG-k adds exactly E, and B/B′ add exactly N.
- **Disjointness.** A, E and N are pairwise disjoint:
  - E = L_A − 1, so E is not in A.
  - E ≤ (p−δ−5)/2 < κ_ε.
  - κ_ε lies strictly between the two A-intervals: it is above U_A iff δ > 2ε−3, and below L_K always.
- **J endpoints.** J has the correct endpoints: κ ≥ 2; k ≥ p+1 iff κ ≥ ⌈(δ+1)/2⌉; and H ≥ 0. Both N ⊂ J (κ_ε ≥ 7, δ ≤ p−2−2ε) and E ⊂ J hold.
- **Codex cell.** The Codex cell lies in the complement:
  - it is not in A, because L_A = (p+5)/4;
  - it is not in E, because δ is odd;
  - it is not in N, because that would need p ∈ {3, 7}.
- **δ = 0.** There is no increment at δ=0.
- **Terminal vs initial words.**
  - TRANSFER adds no terminal cells.
  - T1 and T2 are statements about initial words. They are parametrised by o_F(w0), κ_0 (with even blocks counted in H), A_0 and B_0.
  - They must never be entered in the terminal ledger. Their only nontrivial content is at o_F(w0) > p.

## 6. Recommended exact accepted scope

1. **SEG-k.** Let p ≥ 5 be prime, and take any word in setting (S): all maximal blocks odd, one rotation pair, genuine empty runs, any B, any purity. If k ≥ 4κ+5 and k ≥ p+⌊R/2⌋+1, the word is solvable.
2. **INV and TRANSFER group.**
   - INV holds along RED's P1–P4 starting from any REFL-violating avoider.
   - TRANSFER is accepted with clauses (a)–(f) only.
   - T1 and T3 are accepted. T2 is accepted, but it depends on item 1.
   - All of these hold at RED's accepted conditional scope.
3. **Region B.**
   - B.1 is accepted.
   - B.2 is accepted for 1 ≤ δ ≤ (p−12)/3, with (viii) read as a sufficient condition.
   - B.3 is accepted.
   - Theorem B is accepted for 1 ≤ δ ≤ (2p−29+2ε)/7.
   - B.4 is accepted as a necessary-structure statement on 1 ≤ δ ≤ (p−12)/3, never as a band.
4. **B′.** Accepted for 1 ≤ δ ≤ min((p−12+4ε)/3, (2p−32+2ε)/3), any B.

**Numerical increment over I.14:** exactly E(p,δ) ∪ N(p,δ) for δ ≥ 1, and nothing at δ = 0.

## 7. What stays open

**R > p.** For each δ ≥ 1, Remaining(p,δ) = J ∖ (A ∪ E ∪ N). It falls into three parts, which merge where the SEG-num or K2P+ band is empty:

- **Low:** [max(2, ⌈(δ+1)/2⌉), L_A−1] ∖ E. This is the arc-method region, and it contains the Codex cell.
- **Middle:** [U_A+1, L_K−1], which always has δ+2 values.
  - N removes (p−1)/2 iff δ ≤ M_BP(p,0), and removes (p−3)/2 iff δ ≤ M_BP(p,1).
  - The cells (p+1)/2, …, L_K−1 always remain. For δ = 1 this is the single cell κ = (p+1)/2, with k = 2p.
- **High:** [max(L_K, p−δ−2), p−1]. These cells have k ≥ 2p+1 and k ≤ 3κ+2.

Inside this remainder, only word-level tools apply:
- raw structural SEG;
- B=0 CJ/EDGE;
- B.4, which is non-vacuous only at (17, 0, 1).

None of these is a universal band.

**R = p (V5).** Open cells:
- (5,2), (5,3) and (7,3);
- 2 ≤ κ < ⌈(p+1)/4⌉ for p ≥ 11.

FP-1 covers some of these only under its diversity hypothesis, which does not count as coverage.

**TRANSFER.** Box cells that satisfy none of (a)–(f) remain unexcluded, including cells in N or in the SEG-num top cell for odd δ.

**Unrestricted targets.** REFL(p), REFL-HI(p), RES-HI(p), INV*(p) and ordered Olson for D_(2p) remain open. Novelty and priority were not assessed.
