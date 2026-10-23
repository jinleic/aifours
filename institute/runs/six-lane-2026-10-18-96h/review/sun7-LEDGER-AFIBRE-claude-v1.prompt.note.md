**Counts:** FATAL 0 · MAJOR 1 · MINOR 4. All five findings concern completeness, scope or process. I found no correctness defect in the mathematics of N09–N16.

## Claim-wise verdicts

- **N09 T: correct, locally closed.**
  - (T1) holds because U_a∩U_b∩U_c ≤ U_x∩U_y and L = lcm(n_x,n_y)·ℓ_z.
  - (T3) follows from L0.1; (T2) is inclusion.
  - τ_min, τ_max and T-kill all hold at the actual τ (RK7 LF19–24; RWE m8 LF12).
  - Input N02 is complete and the edge is forward.

- **N10 F7: correct.**
  - Uses T3/T2 at apex v, τ a positive multiple of τ_min, and finite-set equality (ADD LF62–67).
  - Actual τ only; no LF80 clause and no monotonicity (R17 LF155; CR LF70).
  - Closed through N09, but one direct N02 use is unlisted (MIN-1).

- **N11 VFC: correct, closed.**
  - (V1) follows from L0.2 and the double-coset count.
  - (V2): D_j is a union of left U_j-cosets, so d_j is an integer. R∩g_jU_j = (U_v∩w_jU_jw_j⁻¹)w_j has U_v-index |U_vw_jU_j|/|U_j| = d_j.
  - (V3): right-translate by y⁻¹, then invert. This gives disjoint left cosets in U_v, with |S_R| ≤ 6.
  - (V4) and the weighted count also check.
  - This matches S5 (LF299) and F18. RK7 LF46's historical citations are replaced by WV LF34/LF48 (R14 LF152, F19 LF131).
  - Inputs N01/N02/N07/N08 are complete.

- **N12 LFC: correct, closed.**
  - (a)–(d) re-derived.
  - Site S4 (LF298) checks: pieces (x⁻¹y_j)(U_j∩U_v) are left cosets in U_v of index λ_j, with no inversion. |S_C| ≤ 6 by LE E3.
  - L LF13's historical Sun5/6 verdict imports are replaced by [S5W/S6W@S4] (F17 LF129). The statements match literally (S56V LF7–10).

- **N13 INV: (a), (b) and the E7 inequality are correct.**
  - (g_iU_i)⁻¹ = g_i⁻¹(g_iU_ig_i⁻¹).
  - μ(U_vhU_j) = α*_vj/g_vj.
  - q = α* uses only (V1)'s definition, which comes from N11.
  - The index-tuple core is closed. The class/marking/profile clause is **conditional on MAJ-1**.

- **N14 ROWU: mathematically correct.**
  - (i)–(iii), the standard weights, the E8 bound and the ROW-U-deg transfer were all re-derived. The LFCV item-3 label at ME LF30 is not needed.
  - Every Sun use lies inside LFC(c) fibres (S6 LF300 via S4; erratum X1).
  - The abstract transfer has no dependency on M1.
  - **Conditional on MAJ-1, MIN-1 and MIN-2.**

- **N15 DEF: definitional content correct and closed over N02.**
  - P0/P1 follow from L0.2/L0.6 and the CE definition.
  - The class predicates are functions of the labelled index tuple, which supports LE E6.
  - The gcd matrices follow from P0/P1 for each predicate.
  - The cited ranges over-include later theorems (MIN-3).

- **N16 RW: correct, read only with RWE and RWV.**
  - T, K, K1, K2, P, VFC-count, RPLP and CAP check as follows:
    - K: the packing sets g_iU_iU_v are disjoint under either disjunct and avoid U_v.
    - K1 uses T2/T3 and τ ≥ τ_min.
    - K2 is K at apex j with S = {v,k}.
    - P: the grid is 1/gcd(n_v,I_jk), with correct rounding, K2 strictness and Bonferroni sign.
    - RPLP: E1/E2/B/TOT and weak duality check; Farkas applies only to the closed relaxation.
    - F7 enters through N10.
    - CAP: LF72–75 with ADD LF128–139, LF143–148 and LF155.
  - These hold universally over finite seven-coset CE input, with P0/P1 supplying H1–H2.
  - LF75 (local VFC gcd, q ≤ 5) is distinct from the excluded LF76 (L5, t ≤ m ≤ 6).
  - Not used: LF80's second sentence, τ-monotonicity, any vector, coverage or engine result. No INV export (RWE m2 LF6).
  - Inputs are complete and forward. The export contains N57's use as stated in ledger erratum v4 LF6.
  - Literal row alignment is still needed (MIN-4).

## Findings

**MAJ-1: missing provider that cannot be added without breaking forward order** (completeness/order). Locations: LEDGER LF230 (N13), LF231 (N14), LF65 (N15).

- **The step that needs N15.**
  - ROW-U's statement and gcd reduction (L LF79, LF85–86) need DEF content:
    - the CE decomposition with gcd(w,30) = 1 (RM LF33–35);
    - the K7 gcd matrix and the "unmarked" definition (RM LF91; LE LF50–51), which give n_j = 6w_j and g_vj = 6;
    - P0(b) (RM LF42), which gives gcd(w_j,w_j′) = 1.
  - This is load-bearing. If gcd(w_j,w_j′) were 7, two R1 vertices would form an allowed pair, and y = 1 on both would be infeasible.
  - INV(a) exports "same class/marking" (LE E6 LF49–52, i.e. README §5 = N15) and "same profiles" (L LF57; profiles are defined at RK7 LF68, which is N16 vocabulary).
- **Why it fails.** N15 > N13 and N15 > N14, so these edges would point backward. The listed inputs do not close either node.
- **Mitigation.** There is no cycle, because DEF's only input is N02.
- **Consequence.** Consumers citing "INV(a) with E6" (ME LF13–15; CI62V LF7) or the K7 form of ROW-U inherit a provider the ledger does not list.
- **Repair (recommended):**
  1. Place DEF before N12, e.g. immediately after N08.
  2. Add DEF→N13 and DEF→N14.
  3. Read "same profiles" as "same labelled index tuple, hence every index-determined invariant". The profile definition then comes from the consumer's own N16 import.

**MIN-1: incomplete edge cells** (bookkeeping). Locations: LF227 (N10), LF231 (N14) versus R05 LF143.

- F7 step 2 (ADD LF64) uses L0.3 directly: μ(X_a) = α_va/g_va.
- ROW-U uses E1/L0.3 directly (α ∈ {1,…,5}; LE LF19).
- R05 omits N16, even though N16 lists N02 and its K/P proofs use L0.1–L0.5.
- Erratum X5 (LF14) files INV's (V1)-only use under R14, which covers (V2)–(V4). This over-attribution is harmless.
- No reachability or order consequence.
- **Repair:**
  - Add N02 to the N10 and N14 input cells.
  - Add N16 to R05's consumers.
  - Label N13's VFC use as (V1).

**MIN-2: N14 ranges include consumer text, risking a false ROW1/M1 cycle** (scope). Locations: LF64 "ME F3 LF24–32" and "LE LF69–80"; CW LF75.

- ME LF26 and LF31–32 are M1's ROW-1(c) context and verification. They use W, z and m_z from ME F2.
- LE LF79–80 is K63-U0 Step 1 (see CW LF112).
- Read as N14 exports, these would make N14 depend on later nodes.
- **Repair:**
  - N14 exports only ME LF27–30 (the hypothesis through "(i)–(iii) hold") and LE LF71–78.
  - Each consumer verifies ROW-U-deg for itself.

**MIN-3: DEF range over-inclusion** (scope). Location: LF65 "RM LF85–96; WV LF18–21".

- RM LF87 ("Every CE belongs to…") is an exhaustiveness theorem, not a definition.
- WV LF20–21 contain R1(7), the Sun(4)/Sun(3)/Prop4.5 and D2/D2′ eliminations, and "six classes".
- RM LF96 and LF67(II) cite "Theorem R1(7)(II)".
- WV LF18 includes an R0 clause.
- None of these is discharged by RM LF42/LF52, and as N15 exports they would be backward edges.
- No N09–N16 consumer uses them, so there is no local consequence.
- **Repair:**
  - Restrict N15 to the definitions, the class predicates, P0/P1, and the per-predicate gcd matrices.
  - Add the KII derivation inline:
    1. Let a = 2. By P0(a), P1(ii) and A_5 = {x,y}, we get x ∈ A_2∖A_3 and y ∈ A_3∖A_2 (up to naming).
    2. The other five vertices then lie in C.
    3. This yields the KII column with no Sun use.
  - Exhaustiveness stays with the reduction/COVER nodes.

**MIN-4: RW row not aligned with RWE/RWV** (process). Locations: LF66, LF233, R12 LF150, R18 LF156, F20 LF132.

- **Discharge ranges cite no erratum.** "RK7 LF19–80" and "ADD LF17–159" do not cite RWE or RWV, and literally span excluded text:
  - RK7: LF32 (seven-piece/frame), LF34–36 (XE), LF55–64 (N21/N22 text), LF76, LF80's second sentence.
  - ADD: LF17–19, LF71, LF152–154, LF157, LF159.
- **R12** still offers S56 L3/K2 with N02 as an alternative K route; RWE m4 removed it.
- **R18** cites ADD LF21–104; RWE m1 cites LF21–110 plus the first two sentences of LF124.
- **F20's "no operative consumer"** contradicts the N16→N57 capping edge (erratum v2 LF6, v3 LF5; CI62V LF11).
- **RW LF6's R0 clause** is consumer-side, since RWV LF5 scopes RW to finite input.
- Discharge cells only locate proof bodies (LEDGER LF44), and I confirmed that none of the excluded text is used.
- **Repair:**
  1. Rewrite the N16 row as "RW LF10–23 read only with RWE 3eb93c47 and RWV 1bc8080a".
  2. Set the discharge to:
     - RK7 LF19–24, LF26–28, LF30, LF40–49; LF70 for non-L5 quantities only, LF71–75; LF80 first sentence;
     - ADD LF21–110 (W2 governing LF106), LF124 first two sentences, LF128–139, LF143–148, LF155.
  3. Drop R12's alternative route.
  4. Align R18's range with RWE m1.
  5. Restrict F20's parenthetical to K/P/RPLP.

## Boundary imports and limits

**Boundary imports:**
- N01: Zhu Sun3/4.
- N02: L0.1–L0.6, Sun2, LE E1–E2.
- N03: R0, a conservative input at N13.
- N07/N08: S5W/S6W statements only, at S4, S5 and S6.
- WV LF34, LF38, LF40, LF42 and LF48–50.
- RWE/RWV, which fix N16's scope.
- CI62V, used only as an N57 boundary.

**Texts I could not check:**
- Rows W04, W07, K01, K02 and H01.
- RKE W1–W2.
- ADD LF111–124.
- CR LF11–13 and LF30; CW LF31–32.

My re-derivations needed none of these; any further obligations they state are unchecked.

N13 and N14 remain conditional until MAJ-1 is repaired. The global graph and final join, Sun7, runtime, novelty, Lean and human review are not approved here.
