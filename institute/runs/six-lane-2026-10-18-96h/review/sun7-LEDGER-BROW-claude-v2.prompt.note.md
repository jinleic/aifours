**BROW (N28–N36): second-family interface-closure verdict**

**Counts: FATAL 0 · MAJOR 0 · MINOR 4.** All four are completeness or bookkeeping. There is no correctness, priority or computation defect in the operative route. Governing errata v5–v8 are applied throughout.

**Order:** every listed input of N28–N36 precedes its consumer in the v6 explicit order. N02, N03, N15 and N09–N14 all come before N28. N30 and N32 come before N33 and N35. N28 and N31–N35 come before N36. The local graph is acyclic, and the numeric and explicit readings agree here.

## Claim-wise verdicts

**N28 M0: VALID** (edge repairs in m2)
- The ROW-U statement (L LF79–83) applies literally. The tuple n_i = 6w_i is K7 with every vertex unmarked (v6 LF11).
- INV(a) with E6 (LE LF49–54) gives the actual inverted configuration (g_iU_i)^−1 with the same index tuple. So ROW-U(iii) also holds for α*.
- E7 (LE LF61–63) gives α+α* ≤ g from the disjoint double cosets U_v·h·U_j and U_vU_j, without using VFC.
- Since 4+4 > 6, A4(v) and A4*(v) are disjoint. Both have size at least 3 inside six neighbours, so |A4(v)| = 3. That makes a 3-regular graph on 7 vertices, whose degree sum is odd (L LF116–121). Correct.
- The R0 lift is N03 (README LF29).
- Sun(5)/(6) enter only through ROW-U, at U_v and U*_v (site S6, as corrected by X7).

**N29 U0: VALID** (m1, m3)
- *Step 1 setup:* g_vd = gcd(6w_v, 3w_d) = 3, so α_vd ≤ 2 (LE LF18).
- *Step 1, d is isolated:* if α_vd = 1 then λ_d = w_d, which is coprime to every λ_j = w_jα_vj. By the hereditary condition (L LF29–30) and Sun(2) (LE E2), d can only appear in the set {d}.
- *Step 1, the five C-neighbours:* their labels satisfy gcd(λ_j, λ_j′) = gcd(α_vj, α_vj′), by the statement's coprimality and α ≤ 5. So N14's standard weights are feasible on them and contribute at least 4/6 (L LF138–140; LE LF79–80).
- *Step 1, contradiction:* adding d's 1/3 gives a total of at least 1, which exceeds 1−1/n_v.
- *Step 1 really uses Sun(5) quarter weights, as written.* The b ≥ 4 branch puts 1/4 on every R24 element (L LF101; LE LF80 "otherwise min(5,4)=4"). That weighting is feasible only because five R24 pieces, all with gcds ≤ 4, cannot share a U_v-fibre. This is S5W at site S7, reached via S4: five left cosets of U_j∩U_v inside U_v, with d excluded.
- *Step 2:* in U_d, λ_i = 4w_i. S5W applies to five of the six pieces, and 6·¼·⅔ = 1 gives the contradiction (L LF142–144).
- No INV is used, so no N13 edge is needed. The R0 lift is LE E5.
- *Non-operative observation:* Step 1's conclusion alone would survive with weight ⅓ on three fours, which needs no Sun input. Step 2 genuinely needs Sun(5). Keeping S7 is conservative and correct for the displayed text.

**N30 ROW1: VALID** at its scope: an unmarked apex with exactly one marked neighbour z, where m_z = 3^A5^B with actual exponents (ME LF19–22).
- Part (c) uses N14's abstract ROW-U-deg (ME LF27–30, per v6 LF22) together with N30's own check at ME LF31–32.
- I recomputed that check. g_vz = g_vu = 6, λ_z = m_zw_zα_vz and λ_u = w_uα_vu. If α_vu ∈ {1,2,4} and m_zw_z is odd, then gcd(λ_z, λ_u) = gcd(α_vz, α_vu).
- This is a lemma inside a finite configuration, so there is no R0 use (see m3).

**N31 M1: VALID**
- ROW-U statement is applied at the marked apex z. All six neighbours of z are unmarked, and L LF79 allows a marked apex.
- ROW-1 is used only at W-apexes, whose single marked neighbour z is odd-marked.
- INV and E6 (ME F1) handle the inverted configuration; R0 lifts the statement.
- The exclusions at M LF10–11 hold.

**N32 Z2: VALID**
- I re-derived the G2 hypotheses (ZE LF20–25).
  - If a 5-marked p ≠ z exists, P1(ii) forces h_z = 0, because all K7 vertices lie in A_2.
  - Then g_zp = 6 and λ_p = 5^{h_p}w_pα_zp, an odd {3,5}-smooth marker.
  - The five W labels have the form w_uα_zu.
  - The apex's even marker enters only through g_zj = 6.
- If there is no p, the ROW-U statement applies at z directly.
- ROW-1 is never used at W-apexes, where the neighbour z is even-marked.
- T and F7 are applied to the actual inverted configuration (ZE G5) through N09, N10 and N13.
- LIGHT's extra Sun(2)/(3) uses run through V3 right fibres, inside N11 (X1).

**N33 K735: VALID at the interface**
- P1(ii) and P1(iv) give m_t = 3^A and m_p = 5^B.
- ROW-1-deg is used only at the marked apexes t (neighbour marker 5^B) and p (neighbour marker 3^A). Both neighbour markers are odd. This comes via N30 and N32 (H LF6–7).
- W-apexes have two marked neighbours and are handled by N33's own ROW-2, which is body, not re-proved here.
- There is no T, F7 or VFC use (H LF8), so no N09–N11 edges. E1 comes via K4 (H2 LF22–23).

**N34 U1: VALID at the interface**
- The input cell equals the declaration U LF10–22.
- There is no ROW-1 (N30) or Z2 (N32) import (U LF23–26), so no even-marker transfer is inherited.
- For an even m_z the gcd identity can fail. Example: α_vz = 1, α_vu = 2, 2 | m_z gives gcd 2 against 1. So under v6, N34 must check its own gcd hypotheses. That is the role of ROW-1*/CROSS*/LIGHT* in U LF48–154 (body, not re-proved here).

**N35 ZP5: VALID at the interface**
- ROW-1 is used only at the centre z, with neighbour p. Here g_zp = gcd(6·2^E3^Aw_z, 6·5^Bw_p) = 6 and the marker 5^B is odd (P LF28–33; G2 via N32).
- ROW-1 is not used at W-apexes, nor at p, whose neighbour z is even-marked.
- There is no ROW-2, ROW-1* or Z2 CROSS/LIGHT import (P LF41), which matches the absence of N33/N34 edges.

**N36 NF: VALID** (m4)
- Inputs are exactly the six theorems plus N03 and N15. There is no N48 or (a1) edge (W08, LF176).
- I re-derived coverage from the scope column (N LF48–53). In K7 we have C = V, so P1(ii)–(iv) give |Z|, |T|, |P| ≤ 1. Outside F = {Z={z}, T={t}, z≠t}:

| Markers | Sub-case | Theorem |
|---|---|---|
| Z = ∅, T = ∅ | P = ∅ | M0 |
| Z = ∅, T = ∅ | P = {p} | M1 or U1 |
| Z = ∅, T = {t} | P ⊆ {t} | M1 |
| Z = ∅, T = {t} | P = {p≠t} | K7-35 |
| Z = {z}, T = ∅ | any P | Z2 |
| Z = T = {z} | P ⊆ {z} | U1 |
| Z = T = {z} | P = {p≠z} | Z23-P5 |

- Each scope's index form follows from the decomposition and P0(b).

## Findings

**m1 (completeness/ownership, v6 LF22 and v5 LF6): N29/N30 row texts.**
- *Problem:* v6 moves LE LF79–80 (the K63-U0 Step 1 instance) out of N14's body and into its consumer. N29's cells (LF77, LF246) list only L LF135–144 and E5, so the governing E8 instance belongs to no node.
- *Problem:* L LF138's phrase "unmarked with g = 6" is no longer an instance that N14 exports.
- *Problem:* the declaration's "Step 1 subset form (KD2 H5 LF28–33; KE3 J5 LF24–26)" cites instance text in consumer files that BROW cannot see.
- *Problem:* N30's body range ME LF17–43 includes LF27–30, which v6 makes N14's export.
- *Consequence:* none for correctness, since L LF138–140 is a complete five-neighbour argument. However, N29's export is broader than its body, and governing text is left unowned.
- *Repair:*
  - Set N29's body to L LF135–144 plus LE LF19 (the K63-U0 clause), LF42–45 and LF79–80.
  - Record N29's own one-line gcd identity, which follows from L LF136, the statement's coprimality and E1.
  - Have N29 export only the abstract Step-1 argument. Its hypotheses are: five neighbours satisfying ROW-U-deg, plus a d with α_vd/g_vd ≥ 1/3 whose label is coprime to the other five.
  - Treat H5 and J5 as instances owned by N37 and N38, gated in BK63.
  - Have N30 own ME LF17–26 and LF31–43, and cite LF27–30 through its N14 edge.

**m2 (completeness, direct edges).**
- *Problem:* N28, N30, N31, N32 and N33 use DEF predicates but do not list N15. The predicates used are K7, marked/unmarked, and n = 2^e3^f5^h·w with P0(b). See L LF116–118, M1 (N LF49), Z2 (N LF50), K735 (N LF51) and ZE LF20. This is the same situation as v6 LF8's addition of N15 to N13 and N14.
- *Problem:* N28 uses the definition and symmetry of α at L LF120. That definition sits in N02's body (LE LF16), and W02 already lists N28, but N28's input cell does not list N02.
- *Consequence:* none for ancestry, since both already reach these nodes through N13 and N14. All additions are forward edges.
- *Repair:*
  - N28: N02 (cons.), N03, N13, N14, N15.
  - N30: N02, N12, N14, N15.
  - N31, N32, N33: add N15.

**m3 (bookkeeping: rows and consumer lists).**
- **W01** (LF169) lists N30. But ROW-1 is a lemma in a finite configuration and N30 has no N03 input. Drop N30, as v7 LF5 dropped N17.
- **W02** (LF170) lists N36. But NF's SHAPE/MK/PART derive from P0/P1, which is N15, not N02. Drop N36, per the exact-consumer rule (v5 LF9; v7 LF6).
- **W03** (LF171) mismatches in both directions:
  - W03 lists N29, but N29's rows cell (LF246) omits W03. Add W03 there, since S7 is the genuine Step 1/2 S5W input, unless R21 already records it.
  - The rows cells of N31, N32, N34 and N35 include W03, but W03 excludes them, because under X1 their Sun uses enter through N11, N12 and N14. Change those cells to W01, W02, W04 (plus W05–W07 where applicable).
- **Rows cells** that omit W rows they consume:

| Node | Missing rows |
|---|---|
| N28 | W01, W02 |
| N29 | W01, W02 |
| N30 | W02 |
| N33 | W01, W02 |
| N36 | W01 |

**m4 (completeness and literal scope, N36).**
- **(a) Body range.** The body is N LF22–111 (LF84), but CW LF89 places K7-NF at N84–118. Either extend the body to N LF22–118, or certify that LF112–118 are navigation only. CW LF89 shows no (a1) use there, and K7-REM (LF120–133) stays excluded either way.
- **(b) Evidence cell.** The cell (LF253) cites N LF43–57 and v3 LF5.
  - That range includes N LF54, the (a1) row, which CW LF124 classifies as K7-REM only.
  - v3 LF5 also says "TC/CELL enter transitively through (a1)" and "Sun(5)/Sun(6) remain computer-assisted".
  - Neither applies to N36. Read literally, the cell would bring in a backward N48 dependency (a false (a1) cycle) and a computational premise. In this route, Sun(5)/(6) enter N36 only as S5W/S6W at the S4–S7 sites inherited from N28 and N31–N35.
  - *Repair:* use N LF43–53 plus LF55–57 as replaced by v3. Mark N LF54 and those two v3 clauses as K7-REM or historical provenance: no N48 edge and no computational premise.

## Uncounted notes
- **S6 wording.** S6's ambient "apex with six unmarked neighbours" (LF300) is narrower than its inherited uses: the ROW-1(c) apex, the G2 apexes z, t and p, and the H5/J5 subsets. There is no gap, because S4 supplies the S5W/S6W scope check at any apex: left cosets inside U_v, at most six pieces, and coinciding subgroups allowed (S56V LF10).
- **K7 row not pasted.** README LF91 is not in the packet. The NF coverage check used v6's K7 reading, in which unmarked means n_i = 6w_i, so C = V.
- **No N01 edges needed.** Every Sun(3)/(4) use in N28–N36 lies inside LFC/VFC fibres (X1, X4).
- **Node-owned bodies.** The ROW-2, ROW-1*, CROSS, LIGHT and W-apex certificates and NF's B1–B8 blocks are node-owned bodies and were not re-proved. Their interfaces fit.

## Scope
Local BROW closure is valid relative to the named provider boundaries: N02, N03 and N09–N15 as pasted, and S5W/S6W at S4, S6 and S7. Repairs m1–m4 change no proof step.

The H5/J5 instance transfer belongs to BK63. The global graph, the final join, full Sun7 and runtime are not approved here.
