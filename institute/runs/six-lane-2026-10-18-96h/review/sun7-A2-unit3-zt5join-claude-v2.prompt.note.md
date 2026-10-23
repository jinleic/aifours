# K7(a2) Unit 3: narrowed second-family review (written only, no tools)

**Source.** `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-a2-closure/K7-A2-UNIT-3-v1.md`, sha256 a2b40a9e…59be. Below, U1, U2 and U3 mean `K7-A2-UNIT-{1,2,3}-v1.md`.

## Coverage

**Reviewed in full:**
- U3:9–14
- U3:47–53
- U3:82–148

**Not in the embedded snapshot, so not reviewed:**
- U3:15–46. This is the rest of §0. According to Unit 2 parent erratum v2, it holds the G_z/G_t definition (:33–34) and where those bounds come from (:22, :42).
- U3:149–157.
- Nothing in this verdict covers these lines.

**Treated as inputs, not reviewed:**
- **H_NO5**, which is U3:55–80.
- The Unit 1 and Unit 2 exports, taken at their literal hypotheses. I read them through Unit 1 erratum v1 and Unit 2 errata v1 and v2.
- The accepted statements, taken at their verdict scopes. I read them through OV1 and then OV2. No statement used here is changed by an overlay; only the proofs of F1/F4/F6/F7/S5 are annotated.

**Not used as premises:** prior review outcomes that the errata cite.

## Counts and conditional-interface verdict

**FATAL 0 · MAJOR 0 · MINOR 7**

**Verdict: CONDITIONAL-INTERFACE PASS.** The reviewed lines derive Theorem A2X with no omitted branch, given four things:
1. H_NO5.
2. The Unit 1 exports in the table below, each at its literal hypotheses.
3. The Unit 2 exports in the table below, each at its literal hypotheses.
4. The accepted inputs: LFC, INV/E6, R0, L0.1–L0.3, L1, VFC V1–V4, Sun(2)–Sun(4), Lemma F, FG-a2, D23-a2 and S1–S5. Sun(5) and Sun(6) enter only transitively and are computer-assisted.

This review does **not** accept A2X, Unit 1, Unit 2, H_NO5, K7 or Sun(7). Every new claim remains CANDIDATE_UNVERIFIED.

## Verdict per claim

| Claim | Lines | Verdict |
|---|---|---|
| Setting (visible part) | U3:9–14 | PASS. The index arithmetic matches scope :14–17. The R0 normal core also preserves the conjugated intersections, so α* survives the reduction. |
| Partition; normalisation α_zt=5, α*_zt=1 | U3:47–53 | PASS. Lemma F plus α+α*≤6 gives a disjoint split with no "other-five" case. INV(a) double inversion gives α(Γ*)=α*(Γ) and α*(Γ*)=α(Γ); indices and markers are unchanged (INV(a), E6). α*_zt=1 follows from positivity. |
| §3, T*=W ⇒ H_A ⇒ empty | :82–89 | PASS as a conditional consumer (details in the export table). |
| §4(1) | :96–99 | PASS |
| §4(2) | :101–112 | PASS |
| §4(3) | :114–123 | PASS |
| §4(4) | :125–126 | PASS |
| §4(5) | :128–140 | PASS |
| A2X assembly | :142–148 | CONDITIONAL PASS. The dependency graph is acyclic: U2 imports nothing from U1, and neither imports U3. See m7. |

## Audit-focus items

**(a) Starred t-three row.**
- In the both-4 case, take the vector (v1 ½, v2 ½, t 1). The t-label is 3^{A+1}w_t, which is coprime to 4ρ_v, so val = 2+2+3 = 7 ≥ 6. That is a direct LFC kill.
- In the both-3 case, the local test only gives e* ≤ 3. That case is then removed entirely: a1 and a2 have e* = 4, and a3 is killed at apex v by (a1 ½, a2 ½, a3 1), val = 7.
- ZT (U2:97) independently gives α*_ta ∈ {1,2,4}.
- No branch is lost.

**(b) The p-entry-1 exception.**
- α_tp ∈ {1,2} is retained when p ∈ T* (:110–112).
- Every use of α_ta = 2 is at a chosen a ∈ T*∩W′ (:118, :128). That set is nonempty, since |T*∩W′| ≥ 2.
- The masses at v_i, the IN step and the cell indices never use α_ta.
- If p ∈ O*, then α_tp = 4, which matches S3.
- M_B is correctly not invoked.
- In the T*=W branch, p-entry 1 is absorbed by M_A's own choices (U1:168, :170–171).

**(c) FULL VFC orientation.**
- :123 uses the union bound in Γ^{α*}, whose own family is α*. That is FG-a2(a) at a ∈ W′ with β = α* and β_zt = 1, exactly as stated at U2:48–49.
- No FULL LFC is used in Γ^{α*}. Every val ≤ 5 there puts weight 0 on z or t and uses L_z or L_t (:107, :116).
- Full VFC in Γ^α is never used.

**(d) 11/12 > 5/6.**
- Step (3) uses the sets Z = D_z (μ = ½), K = D_v1∩D_v2, and N = occupied fibres outside Z∪K.
- K carries no a′, a″ or t: each such triple has pairwise index gcd 2, which Sun3 forbids. K carries no z either, by TC.
- D_a′ is disjoint from K, so μ(N) ≥ 4/6 − 1/2 = 1/6.
- D_v1\K and D_v2\K are disjoint subsets of N, so 4/6 ≤ 2μ(K) + μ(N).
- Z, K and N are pairwise disjoint, so the union has measure ≥ ½ + μ(K) + μ(N) ≥ 5/6 + μ(N)/2 ≥ 11/12 > 10/12. The arithmetic is correct.

**(e) Vertex-wise cells before locating t's column.**
- HK = G comes from Φ_a ⊆ H and m_a^K = 3.
- m_a^K = 3 holds because a meets at least two K-cosets (Φ_v ⊆ K and α*_av/6 > 1/3). Two of the three K-cosets are distinct v-columns, and IN with α*_va = 4 then forces m_a^K = 3.
- This uses no fact about where t sits.
- After that, CELL gives:
  - v-pieces in every cell of v's column (m_v^H = 3);
  - t-pieces in every cell of t's column (m_t^H = 3);
  - a-pieces in every cell of a's row, and the three rows are exactly the a-rows.
- So the (v, t, a) Sun3 kill is valid before t's column is known. The (t, a, z) kill uses N_z = 2^{E+1}w_z, which follows from v3(n_z) = 1 and forces m_z^H = 3.

## Step checks for §4 not covered above

**Step (1).**
- K_{3,2}(T*, O*) ⊆ Γ_α spans W and is connected, so ZT applies.
- ZT gives two starred t-fours. They lie in T*, because α*_tv ≤ 2.
- Apply B-test at a1 and a2, which is valid even if one of them is p:
  - c = 3 by S1;
  - W–W entries are in {1,2,4} by U2 §2 and Lemma F;
  - α_ta ∈ {1,2,4} by S3;
  - L_z and L_t hold.
- Any third entry ≤ 2 would force α_ta = 4, which is a contradiction.
- The pairs {a1a2, a1a3, a2a3} are all covered, so α_aa′ = 4 everywhere.

**Step (2), both-4 row list.** The W-row is (≤2, ≤2, 4, 4) with e* ∈ {1,2,4}. Every row except 2244|4 dies:

| Row | How it dies |
|---|---|
| 1144 | val 6, direct |
| 1244 \| 1 | val 6, U1:75 |
| 1244 \| 2, 1244 \| 4 | R5 |
| 2244 \| 1 | R1− |
| 2244 \| 2 | R1 |

Each R-row gives L′_v1 = L′_v2. Then K3 at apex v1 of Γ^{α*} (with u = a, j = v2) gives masses 4/6 + 2/6 = 1, which contradicts V4.

**Step (2), both-3.**
- Remainder 12: the vector (½, ½, 1, 1) gives val 6.
- Remainders 11 and 22: the vector gives val 4 + e*/3 ≤ 5 by L_z. Its feasibility holds because:
  - {v1, v2, t} has pairwise gcd 3 and weight sum 1;
  - when e* is even, {t, s, s′} is forbidden and {t, s} has weight 5/6.

**Step (3), remaining parts.**
- e* = 1 is killed directly, with val 6.
- For e* = 2, the vector (o 1, a 1) has val 5 with z = t = 0. L_t equality then holds. Since {o, z} is not allowed, L′_z ⊆ L′_a at both v. TC then gives D′_z ∩ D′_v = ∅.

**Step (4).** Direct, with val = 4 + 1 + 1 = 6.

**Step (5), EQ and SUB.**
- EQ at a has masses (4, 4, 2, 2, 2)/6 and indices 4ρ_a′, 4ρ_a″, 2ρ_v, 2ρ_v, 2·3^A w_t.
- EQ at v_i has indices 4ρ_v′, 4·3^A w_t, 2ρ_a.
- In both cases the five odd parts are pairwise coprime, and z is excluded.
- SUB at a uses α*_aa′ = α*_a′a″ = α*_aa″ = 2, which gives three distinct H-cosets.
- SUB at v_i uses α*_v1v2 = 2 and α*_v′t = 2, which gives h_v1K ≠ h_v2K and h_v′K ≠ h_tK.
- The z-piece index n_z·ab/9 has no prime outside {2, 3} ∪ primes(w_z). That includes having no 5, which covers p in any position.

## Export uses: hypotheses checked

| Use | Export | Literal hypothesis | Status |
|---|---|---|---|
| :83, :92 | ZS (U2:121) | normalised S-data | met by §1 |
| :84 | ZW (U2:143) | T* = W | branch |
| :84, :105, :107, :116 | G_z / G_t (U2:44–47) | u ∈ W, either orientation | every apex used is in W, including p |
| :85, :96 | ZT (U2:97) | Γ_α connected | the CL(α) antecedent; K_{3,2} at :96 |
| :85 | ZTR (U2:108) | Γ_{α*} connected | the CL(α*) antecedent |
| :93, :97 | no α W-three (U2:84) | S-data | met |
| :97 | B-test (U2:116) | Γ^α, c = 3, entries {1,2,4}, L_z/L_t | met at a1 and a2 |
| :123 | FULL Γ^{α*} VFC (U2:48–49) | u ∈ W, FG-a2 with β = α* | a ∈ W′, clause (a) |
| :86–88 | H_A theorem (U1 §4–6) | H_A (U1:84–86) | met. Γ* also satisfies H_A, because each item is two-sided (ZT and ZTR swap roles). U1 never uses the z–t entry; t-apex vectors put z at weight 0. |
| :104–105 | R1, R1−, R5, the 1244\|1 kill, K3, TC | U1 §3 row hypotheses; distinct vertices; j, a ≠ z | met at a ∈ T* in Γ^{α*} |
| :129–138 | EQ, SUB, IN, CELL (U1:144–164) | as stated there | met; the union source is uncited (m3) |

## MINOR findings and minimal repairs

**m1. U3:15–46 and U3:149–157 are absent from the packet.**
- The owned contract and tail cannot be verified.
- Repair: embed these lines, or certify that they contain metadata only.

**m2. U3:92 attributes facts to "Unit2 ZS" that are not in ZS's exported statement (U2:121).**
- α*_av ∈ {3,4} is proved inside ZS's proof at U2:122–123, by L1 T1/T3 and Lemma F.
- α*_v1v2 ≤ 2 and α*_tv ≤ 2 follow from INV(b).
- The facts are correct; only the attribution is off.
- Repair: cite each source as listed above.

**m3. U3:129 and :131 do not cite the source of EQ's hypothesis that the union is ≤ 5/6.**
- Repair: add "(U2:47 V_z at a and at v_i in Γ^{α*})". This mirrors U1 erratum m4 for M_B.

**m4. Notation clashes.**
- K is a fibre set at :120–122 but a subgroup at :131.
- H is the a-subgroup at :130–138 but the cell subgroup in CELL (U1:157).
- The formula N_z = [K∩H : Φ_z∩H] is correct, since Φ_z ⊆ K.
- Repair: rename the fibre set to K_v. Rename H to L, with cells as (K∩L)-cosets, as in U1 erratum m13.

**m5. Labels and local indices are swapped.**
- At :101, "local indices 4ρ_v, 3ρ_v′" should be "LFC labels".
- At :119, "label gcds" should be "VFC local indices d_j = r_jα_aj".

**m6. U3:88 understates what the H_A proof uses.**
- The text says the proof uses "only the omitted-marker bounds and ordinary LFC/V4". It also uses L1 twins, TC, K3, EQ, SUB, IN, CELL, CL and Sun(2)–(4).
- The intended point is correct: no FULL granularity is used.
- Repair: reword to "no FULL granularity in either orientation".

**m7. The join sentence at U3:145–146 is incomplete.**
- It omits the accepted zt5 inputs that U3 uses directly: Lemma F (:48, :93), S1 (:84) and S3 (:110).
- The visible U3 text also never says that Sun(5)/(6) are computer-assisted transitive imports. The package (:14) and U2:14 do say this.
- Repair: add one sentence covering both points.

## Observations (not findings)

1. **Step (3) does not need FULL.** It also closes from V_t (U2:47). D_z, D_v and D_a′ all avoid t, so the same 11/12 bound applies inside the union taken without t. This means U3's own steps never need FULL. U2 §2 (U2:58) still uses FULL.
2. **Lemma F's z–W′ clause.** The excerpt of F1–F7 (A2-FIVE:40–47) has no z–W′ clause. The consequence sentence at :48–49 and the accepted verdict (:34) do state it. In zt5 it also follows from F3/S1, and in no5 from D23-a2, so this slice has no gap.
3. **ZT makes U3:102–103 redundant, but it is correct.**

## Gate

This is a conditional interface only.
- No three-unit theorem is accepted until H_NO5, Unit 1 and Unit 2 are each accepted separately, along with the parent verdict.
- Nothing here gives a K7 or Sun(7) closure.
- No novelty, Lean or human-review claim is made.
