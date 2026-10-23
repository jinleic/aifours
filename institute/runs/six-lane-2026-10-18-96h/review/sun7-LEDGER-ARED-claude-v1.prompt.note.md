# ARED (N17–N27) interface-closure audit

**Counts: FATAL 0 · MAJOR 0 · MINOR 4**

- **Correctness:** no defect found in N17–N27.
- **Completeness:** m1–m4.
- **Process:** m4.
- **Priority and computation:** nothing found. No StageA/StageB, k5/k6 verdict, certificate or least-order/frame premise survives at any owned site.

## Claim-wise verdicts

- **N17 R1(7): closed.**
  - I re-derived RM LF60-65 from P0/P1 (RM LF37-52).
  - Site S1 (LEDGER LF295): a≥3 forces a=7, with every P={5}. Any six of the seven original LEFT cosets in the CE's G have gcd 5<6, which contradicts S6W (S56V LF8).
  - Site S2 (LF296): when a≤1, S5W (S56V LF7) on each 5-subfamily gives a gcd-6 pair, hence a pair in C, hence |V∖C|≤3.
  - Count, side and ambient group all fit. The k5/k6 verdict citations are superseded by statement only (C LF49-50; F15/F16 LF127-128; R02/R03 LF140-141).
  - The (II) case and the type split use only P1(i),(ii).
- **N18 R1a: closed.**
  - Zhu Sun(4) (C LF12) applies to four original LEFT cosets.
  - The "(§3)" gcd-3 citation (RM LF67) is just P1(i) under D⊆A₃∖A₂, so its provider is N15.
- **N19 R1b: closed.**
  - It is a lemma conditional on (I) type 2 (RM LF69). It needs only |C|≥2, which the (I) hypothesis supplies. So no N17→N19 edge is needed; N23 discharges (I).
  - Zhu Sun(3) applies to three original LEFT cosets.
- **N20 R1c: closed.**
  - Arithmetic re-checked: r₁=n_i/2 is odd since i∈C∖E; r_{t+1}=n_{d_t}/4. Coprimality comes from P={2}, with min e=1 for i–d pairs and min e=2 for d–d pairs.
  - The result fits S56 LF68-69 exactly: any group, four LEFT cosets, (2r₁,4r₂,4r₃,4r₄), pairwise coprime, r₁ odd.
  - It uses the re-proof N06, not a Sun(5) substitution (R04 LF142; CR LF63).
- **N21 D2: closed.**
  - VFC at v=d follows WV LF34: right fibres are right-translated and inverted to LEFT cosets in U_d, with index q·n/g.
  - g=2 forces α=q=1, so all local gcds are 3. Sun(4) inside U_d gives |S_R|≤3. Then Σ=3 contradicts the strict bound Σ<3.
  - Only 2- and 4-subsets are used. No S5W/S6W, Sun7 or frame is needed (WV LF36). The section citation is fixed by WV item B-1 (WV LF47).
- **N22 D2′: closed.**
  - D⊆E comes from N19.
  - If q∈{1,2}: gcd(d′,d_i)=1, so Sun(2) in U_{d₁} isolates D_{d₂}. Then μ≥1/4+5/6>1, contradicting the strict union bound.
  - If q=3: six local indices with pairwise gcd 3, so Sun(4) gives Σ=13/4>3.
- **N23 COVER: closed** for every CE, with no least-order choice.
  - I re-derived the case tree; every leaf is literally an RM LF91-96 definition.
  - The K6.2* and K5.2* leaves get C∩E={i*} from P1(iii).
  - The C∩E=∅ universe is removed by N22 before the K5.2* leaf, so K52W is not broadened (C LF16, LF28, LF42; R25 LF163).
  - This discharges the OPEN COVER-routing item in CR LF83 locally, without relying on the FR labels (F04 LF116).
- **N24 X1: closed locally.** After the X1V LF19-20 overlays, the live imports are:
  - **Own pairwise bound (checked):** g_jU_j meets t_j=n_vα_vj/g_vj left U_v-cosets. The translated pieces are LEFT cosets of index λ_j. Sun(2) forbids two coprime pieces in one fibre, and the apex fibre is empty, so Σ_F t_j ≤ n_v−1.
  - **INV (N13):** used only as INV(a), for an arbitrary finite family read by index tuple (LE E6), plus the VFC-free inequality α+α*≤g (LE E7).
  - **T (N09):** I checked the X1C LF16 form directly. Take W=U_v∩U_j∩U_k and τ=[G:W]/lcm(n_v,n_j,n_k).
    - Lagrange gives τ_min | τ.
    - Also [U_j∩U_k:W] = τℓ_v/α_jk ≤ n_v·min(α_vj/g_vj, α_vk/g_vk), so τ≤τ_max.
    - N09's literal statement is not in the packet, but this leaves no gap because the consumed form is elementary.
  - **R0 (N03) and the α-range (N02).**
  - There is no N12/LFC, no Sun(3)–(6), and no StageA.
- **N25 K53B: closed.**
  - ADD LF159 and C LF29 re-checked; the output is exactly the C LF15/F05 tuple.
  - It uses only N02 and N15 and does not consume X1. Note for the join: F05's "N59 via N25" (LF117) must appear as a direct N24→N59 edge.
- **N26 K52W: closed at declared scope, conditional on m3 and m4.**
  - K52 LF48-52 imports definitions only (no COVER, so no circularity). R0, elementary facts and Sun(2) are re-proved. Zhu Sun(4) is used inside U_v.
  - Its scope is the RM LF94 matrix. Every K5.2* configuration has that matrix by P1(i),(iii).
  - LF53-56 exclude StageB, VFC as a black box, Sun(5)/(6) and frames.
- **N27 KIIW: closed at declared scope, conditional on m4.**
  - KII LF26-31: SHAPE is re-derived, and the a=2 step needs no S6W. Zhu Sun(3) is used in U_c. FC23 and INV are explicitly re-proved.
  - Its scope is exactly leaf (II).
  - The old Sun(6)/Prop4.5 wording in WV LF20-21 is cited for definitions only.

**Order and errata.** Every input in LF234-244 precedes its consumer. Worker erratum X4's direct-N01 list matches (N18, N19, N21, N22, N26, N27). Parent errata v2–v4 do not touch N17–N27.

## Findings

**m1 (MINOR, ledger reconciliation)**
- **Mismatch:** LEDGER LF139 (row R01) lists N17 as an R0 consumer, but LF234 gives N17 no N03 input.
- **Why it is only bookkeeping:** R0 is unused inside N17. N17 is stated "in a CE", which is finite by definition (RM LF33), and S5W/S6W hold in every group. R0 is actually consumed at N23 and N59.
- **Consequence:** nothing mathematical; it is a row/edge disagreement at the join.
- **Repair:** drop N17 from R01, and read the S1/S2 ambient group (LF295-296) as "the CE's G, supplied by R0 at N23". Alternatively, add a conservative N03→N17 edge.

**m2 (MINOR, ledger reconciliation)**
- **Mismatch:** LF143 (row R05, discharged by N02) lists consumers N17–N27. But N18, N19, N21 and N23 (LF235, 236, 238, 240) have no N02 input.
- **Actual direct uses:**
  - N18 and N19 use deletion (RM LF25), which the ledger attributes to N02 at S1 (LF295).
  - N21 needs α to be an integer ≥1 (Lagrange) to get α_di=1, unless N11's literal statement includes that.
  - N23 has no direct use.
- **Consequence:** none mathematically.
- **Repair:** add N02 to N18, N19 and N21. Drop N23 from R05, or add N02→N23.

**m3 (MINOR, import-discharge completeness, N26)**
- **Mismatch:** K52 LF52 declares INV(a),(b) and cites the N13 record (L LF54-71, LE E6-E7). But it says only "geometric proof reproduced in sections 2-3". Unlike KII LF31, it never says INV is re-proved.
- **Ledger side:** row R08 (LF146) still discharges INV as N26's own re-proof, and LF243 has no N13 input. If sections 2-3 invoke INV rather than re-prove it, the edge N13→N26 is missing.
- **Consequence:** none for correctness, since N13 is earlier and supplies INV(a) plus the LE E7 inequality. But the literal declaration is not matched to a provider.
- **Repair:** cite the K52 lines that re-prove INV(a) and α+α*≤g. This is preferred, because an N13 edge would pull N11/VFC into N26's closure via worker erratum X5. Otherwise, add a conservative N13→N26 edge.

**m4 (MINOR, packet completeness/process)**
- **Missing text:** the governing parent errata for N26 and N27 are not in the packet: sun7-K52W-parent-erratum-v1 and sun7-KIIW-parent-erratum-v1, items 1-5 each (LF74-75, LF118-119, LF146-147). P1A LF11 requires them.
- **What I matched instead:** the pre-erratum tables (K52 LF45-56, KII LF24-35), with scopes fixed by C LF16-17 and rows F06/F07.
- **Consequence:** N26 and N27 stay conditional until it is confirmed that those items add no import and change no scope.
- **Repair:** supply the items, or a literal parent statement that they leave those tables and scopes unchanged.

## Boundary imports
- N01: Zhu Sun(3)/(4).
- N02: elementary facts, Sun(2), deletion.
- N03: R0.
- N06: Prop 4.5.
- N07 / N08: S5W / S6W.
- N09: T (consumed form re-derived above).
- N11: VFC (WV LF34).
- N13: INV (L LF52-71 with LE E6-E7).
- N15: CE, P0/P1 and the README §5 class definitions.

N04, N05, N10, N12, N14 and N16 are not imported by N17–N27.

**Status:** local closure holds for N17–N25. N26 and N27 hold conditionally (m4; N26 also m3). This is not approval of the final join, CI62, P1B/P2, full Sun7 or runtime. No novelty, priority, human or Lean claim is made.
