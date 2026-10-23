# K7(a2) Unit 3, narrowed second-family review of LF9–80 (conditional interface only)

**Result: FATAL 0 · MAJOR 0 · MINOR 6.** The (a2-no5) closure at Unit 3:55–80 passes conditionally. Lines 15–46 were not reviewed because they are absent from the snapshot.

**Basis.** This is a written review only. I used no tools, file reads beyond the embedded snapshot, computation or delegation. Prior model outcomes, including the review counts quoted in the parent errata, were not used as premises. Every new claim remains CANDIDATE_UNVERIFIED. This is not an A2X verdict.

**Abbreviations used below:**
- U1, U2, U3 = `K7-A2-UNIT-{1,2,3}-v1.md`
- A2F = `K7-A2-FIVE-v1.md`
- OV1, OV2 = `K7-A1-A2-delta-erratum-v{1,2}.md`
- A1S = `K7-A1-STRUCT-v1.md`
- TC = `K7-TC-v1.md`
- LI, LIE = `K7-LFC-INV-v1.md` and its erratum

## 0. Coverage

- **Reviewed:**
  - U3:9–14 and U3:47–80.
  - Checked against the literal text of U1:8–22 and U1:34–192, and U2:7–24 and U2:26–144.
  - Checked against every manifest excerpt, the Unit 1 parent erratum v1, and the Unit 2 parent errata v1 and v2.
- **Not reviewed: U3:15–46.** These lines are inside the owned range but absent from the manifest, which covers only 9–14 and 47–148 (see m1).
  - I therefore checked each *use* of a Unit 1 or Unit 2 contract in LF47–80 directly against the literal Unit 1 and Unit 2 text.
- **Context only, not audited:** U3:82–148.
- **Unit 1 and Unit 2 proofs were not re-proved.** Their exports were treated as conditional inputs at their literal hypotheses.

## 1. Verdict per claim

| Claim | U3 lines | Verdict |
|---|---|---|
| Exact (a2) setting and R0 | 9–14 | PASS |
| Partition and actual inversion | 47–53 | PASS |
| No5 preamble: TZ(iii), D23-a2, FG-a2 own/opposite including p, G_z/G_t | 56–62 | PASS |
| Case A ⇒ H_A | 64–69 | PASS, conditional on the U1 H_A chain |
| Case B: CASEB-T re-derivation, then M_B | 71–77 | PASS, conditional on U1 R1/R1−, TC/K3 and M_B |
| Mirror and E=1 | 78–80 | PASS (wording only) |
| Contract table | 15–46 | NOT REVIEWED |

## 2. Checks

### 2.1 Setting (U3:9–14)

- **Matches the scope.** It equals `K7-A2-SCOPE-v1.md:14–17`.
  - n_j = 6r_j with pairwise gcd 6 is exactly the condition that the r_j are pairwise coprime.
  - "Every w is prime to 30" is forced by coprimality with the three markers.
- **Consistent with the other units.**
  - It is contained in U1's setting (U1:9–12, read as "contains" per Unit 1 erratum m1).
  - It equals U2:8–10.
- **No bounded exponents.** E, A and B are never bounded in LF9–80.
- **R0 is adequate.**
  - README:29 preserves indices, pairwise intersections and disjointness.
  - The LFC verdict at :23 adds conjugated intersections, by normality.
  - The intersection indices T_x(Q) of arbitrary subfamilies are also preserved, because the normal core lies in every subgroup and every conjugate.

### 2.2 Partition and inversion (U3:47–53)

- **The 5-entry is confined to z–t.**
  - Lemma F's literal consequence (A2F:48–49) allows only a z–t entry of 5, in at most one orientation.
  - Positivity (LIE:16–18) and INV(b) with E7 (LI:64, LIE:61–63) give α_zt + α\*_zt ≤ 6.
  - So the two entries cannot both be 5, and α_zt = 5 forces α\*_zt = 1.
- **Inversion is the actual one.**
  - INV(a) (LI:56–58) and E6 (LIE:49–54) preserve indices, markers and disjointness.
  - α(Γ\*) = α\*(Γ) holds by definition, and α\*(Γ\*) = α(Γ) holds because (Γ\*)\* = Γ.
- **No5 is inversion-stable.** Inversion only swaps the two matrices.
- **Conclusion.** The split into no5 and zt5 is exhaustive and disjoint, and there is no "other-five" branch.

### 2.3 FG-a2 own/opposite at W′ and at p; source of G_z/G_t (U3:56–62)

The check runs over both actual families β ∈ {α, α\*}. Their indices are n_j by INV(a), and β ≤ 4 in no5.

- **At u ∈ W′.** A2F:103–104 needs 5 ∤ β_zt. This holds because β_zt ∈ {1,2} by D23-a2 (A2F:129), applied to both families since x_zt ≠ 5.
- **At p.** A2F:105 needs β_zt ≠ 5 and β_zu ≤ 3 on W′.
  - For β = α: α_zu = 3, because T = W after U3:57.
  - For β = α\*: α\*_zu ∈ {1,2,3} by D23-a2. In Case B, α\*_zv ∈ {1,2}.
- **Direction is respected.**
  - In Γ^x, LFC granularity uses the conjugate (opposite) family: U2:27–32, and Cor 5/6-a2 at A2F:120–122 with β = x\*.
  - VFC uses the own family: U2:33–34, and FG-V at OV2:60–62 through transfer item (iv) at OV2:195–197.
  - All four combinations (own/opposite × W′/p) hold.
- **G_z and G_t (U1:35–38) follow a fortiori.**
  - Cor 5/6-a2 gives val ≤ 5 for every feasible y, with weight 1 on every fibre where S_C ≠ ∅. This contains (L_z) and (L_t).
  - FG-V's union bound of 5/6 contains (V_z) and (V_t) by monotonicity.
  - The no5 supply therefore does **not** rest on the unproved remark at U1:39–40 (Unit 1 erratum m2).
  - It also does not rest on Unit 2, whose chain is stated under the zt5 S-data (U2:15–18).

### 2.4 Case A against the literal H_A (U1:84–86)

| H_A item | Supplied by |
|---|---|
| c = 3 in both families at every W-vertex | T = W (U3:57) and T\* = W |
| W–W entries in {1,2,4} | Corollary W3 (A1S:34), via TRANSFER (OV2:186), plus no5 |
| W–t entries in {1,2,4} | Lemma E3 (A1S:44), via TRANSFER |
| G_z and G_t, both families, all of W including p | §2.3 |
| CL | PFG-t (A1S:52–58, as amended by OV1:147–148) with Corollary L (A1S:97, OV1:160) |

Notes on the CL row:
- PFG-t's graph Γ^x = {uv ⊂ W : x_uv ≤ 2} is literally U1's Γ_x.
- Its M is the x\*-row at t over W (A1S:53–56), which matches U1's phrase "t-entries of x′". The direction is correct.
- Only the two-fours consequence is used, which needs only Sun(2)/(3) (OV1:91–92).

Further checks on Case A:
- **Inversion symmetry.** H_A is symmetric under inversion. U1's normalisations by actual inversion (U1:98–101, and the M_A orientation at U1:134) therefore stay inside Case A.
- **M_A.** Its extra hypothesis, V_z at W in Γ^α (U1:167), is part of H_A.
- **Scope of the conclusion.** The cited result covers all22 and all six other degree vectors with their inverses.

### 2.5 Case B: CASEB-T re-derivation and the M_B join (U3:71–77)

**R1/R1− hypotheses at apex a ∈ T\* in Γ^{α\*} (U1:51).**
- c\* = α\*_az = 3.
- The W-row is (2,2,4,4), and e\* = α\*_ta ≤ 2 in this branch. E3 gives α\*_ta ∈ {1,2,4}, so the split is exhaustive.
- G_z(a, α\*) comes from §2.3. When a = p, this uses FG-a2(b) with β = α, which is satisfied.
- R1 holds for every E (U1:63), and R1− is z-free.
- Conclusion: L′_v1 = L′_v2.

**K3 (U1:46–48).**
- Roles: K3's u is a, K3's apex is v1, and j = v2.
- The family is the same one, α\*, as TC requires (Unit 1 erratum m6). The three vertices are distinct and none is z.
- K3 requires α_v1v2 + α_v1a ≤ 5, but 4 + 2 = 6. This uses V4 only.

**Consequence for every a ∈ T\*.**
- α\*_ta = 4, so α_ta ≤ 2 by INV.
- CASEB gives α_ta ∈ {2,4} (A1S:122), including a = p in the transfer. Hence α_ta = 2.
- This re-derivation is necessary: CASEB only gives "for at least two a" (A1S:122), while M_B needs all three.

**M_B hypotheses (U1:180–182) against their sources:**

| Datum | Source | Datum | Source |
|---|---|---|---|
| α_aa′ = 4 | A1S:121 | α\*_aa′ = 2 | TC-B (TC:55–56) |
| α_av = 2 | A1S:121 | α\*_av = 4 | A1S:122 |
| α_v1v2 = 4 | A1S:120 | α\*_v1v2 = 2 | TC-B |
| α_tv = 4 | A1S:121 | α\*_ta = 4 (all a) | re-derived above |
| α_ta = 2 (all a) | re-derived above | α\*_tv ∈ {1,2} | A1S:123 |
| α_za = 3 | T = W (U3:57), not displayed at :72 (m2) | α\*_za = 3 | definition of T\* |
| V_z at W in Γ^{α\*} (a1 and v_i, per Unit 1 erratum m4) | §2.3 | | |

Every hypothesis is met. M_B allows any α_zv and z–t entries; here α_zv = 3 and α\*_zt ∈ {1,2}.

### 2.6 E = 1

- **Case A.**
  - H_A has no E-hypothesis.
  - Inside U1, Lemma B (U1:58–61) derives E ≥ 2 for every single-four row. So for E = 1, every vertex has d = d′ = 2, which is all22. That case is closed in U1 §5 without any E condition.
  - No transferred E ≥ 2-only row is used (OV2:188 restricts R3/R4/R5 to E ≥ 2).
- **Case B.**
  - E ≥ 2 is a *conclusion* of the accepted CASEB (A1S:120). So E = 1 Case B is excluded by a premise, not silently dropped.
  - R1/R1−, K3 and M_B do not depend on E. In M_B, N_z = 2^(E+1)w_z holds for every E ≥ 1.

### 2.7 The p marker

- **Never unmarked.** p keeps its 5-marker throughout (U3:13, :68).
- **Case A.** U1's rows are local, with p allowed to be any vertex (U1:50, :53).
- **Case B.**
  - p may be any of a1, a2, a3, v1, v2, and may also be the R1 apex or the K3 apex.
  - Labels of the form 2^i·5^B·w_p keep the two/four pair gcds unchanged.
  - Every z-entry is at most 3 at W-apices, and α\*_tz ≤ 2. So there is no z–p 5-collision in no5.
  - M_B's z-exclusion uses 5 ∤ n_z (U1:177, :191).

### 2.8 Accepted scopes; no accidental (a1) closure

- **Used, and within the verdict lists:**
  - Lemma F, FG-a2, Cor 5/6-a2 and D23-a2.
  - BRIDGE TZ(iii), in the enumerated A2.10 form (OV1:621–625). The auxiliary FG7 is explicitly not transferred (OV1:625–627).
  - From the TRANSFER named list (OV2:186–188): W3, E3, PFG-t with Corollary L, CASEB, TC-B and FG-V.
- **Not used:**
  - R2's (a1) closure, and K23/CELL from (a1). U3:69 explicitly disclaims these.
  - TC-A22, TC-P, the transferred Lemma B and the transferred R3/R4/R5.
  - TX, ZA, ZB and R3.
  - Any Unit 2 export.

## 3. MINOR findings

**m1 — coverage, `K7-A2-UNIT-3-v1.md:15–46`.**
- Problem: these lines are absent from the snapshot.
- Why it matters: Unit 2 parent erratum v2 (:5, :9) cites U3:22, :33–34 and :42 as the governing G_z/G_t definition and its sourcing. This review cannot confirm that check.
- Effect in this scope: none, because U3:58–62 derives G_z/G_t independently.
- Repair: embed :15–46, or attest that:
  - :33–34 equals U1:35–38 verbatim;
  - :22 and :42 attribute Unit 2's G_z/G_t to zt5 only, and FG-a2 / Cor 5/6-a2 / FG-V to no5.

**m2 — `K7-A2-UNIT-3-v1.md:72`.**
- Problem: the Case-B α-data omit za = 3, which M_B requires (U1:181). It follows from :57.
- Repair: append "za = zv = 3 (T = W)".

**m3 — `K7-A2-UNIT-3-v1.md:64` and `:78`.**
- Problem: "Case A: T\*=W" tacitly relies on :57, and :78 repeats the :57 normalisation.
- Repair: write "Case A: T = T\* = W", and replace :78 with a back-reference to :57.

**m4 — `K7-A2-UNIT-3-v1.md:58–62`.**
- Problem 1: the step from gcd 6 to G_z/G_t is correct but only implied.
  - Repair: state that L_z/L_t come from Cor 5/6-a2 with β = x\*, that V_z/V_t come from FG-V in the own family, and that U1:39–40 is unused.
- Problem 2: ":62 Φ_u intersection(Φ_j)" is ambiguous.
  - Repair: write Φ_u·(∩_{j≠u} Φ_j).
- Problem 3: ":58 β_zt ≠ 5" matches FG-a2(a)'s "5 ∤ β_zt" only because β ≤ 5.
  - Repair: say so.

**m5 — `K7-A2-UNIT-3-v1.md:79–80`.**
- Problem: the E = 1 justification cites only R1 and CASEB. Case A's E = 1 closure actually lives inside H_A.
- Repair: add "Case A: H_A carries no E-hypothesis; for E = 1, U1 B forces all22, which U1 §5 closes; no transferred E≥2 row is used."

**m6 — Sun disclosure, `K7-A2-UNIT-3-v1.md:66–67`.**
- Problem 1: the embedded LF9–80 contain no Sun(5)/(6) statement.
  - OV1:505–511 records that the accepted TRANSFER uses Sun(5) *directly* inside Corollary L. It also reaches the computer-assisted Sun(5)/(6) results transitively.
  - Unit 3's own use of Corollary L is the two-fours consequence, which needs only Sun(2)/(3) (OV1:91–92). That part is correct.
- Problem 2: the label "OV1 A1.4" cannot be confirmed from the snapshot. The supporting text is OV1:87–92.
- Repair: add "Sun(5)/(6), computer-assisted, enter only through the accepted inputs (OV1:505–511); no Sun(7)."

**Observation, not a finding.** The e\* = 2 instance of R1 also has an accepted transferred source ("row R1, every E ≥ 1", OV2:187). Case B's dependence on Unit 1 is therefore effectively R1−, TC/K3 and M_B.

## 4. Conditional-interface verdict

- **(a2-no5) is empty (U3:55–80): CONDITIONAL PASS.** This holds provided both of the following hold:
  1. The U1 inputs are correct at their literal hypotheses:
     - for Case A, the H_A chain: §3 (B, row list, twins), §4 (K2, type list, (a)–(c)), §5 and §6, with M_A and EQ/SUB/IN/CELL;
     - for Case B, R1−, TC/K3 and M_B.
  2. The cited accepted statements hold at the A1/A2, LFC/INV and written-verdict scopes.

  Every use in LF55–80 meets the stated hypotheses, and the no5 branch consumes no Unit 2 export.
- **Partition and inversion (U3:47–53): PASS.**
- **Setting (U3:9–14): PASS.**
- **U3:15–46: NOT REVIEWED.**

Nothing here concludes A2X, (a2-zt5), K7 or Sun(7). All new claims remain CANDIDATE_UNVERIFIED pending the parent disposition.
