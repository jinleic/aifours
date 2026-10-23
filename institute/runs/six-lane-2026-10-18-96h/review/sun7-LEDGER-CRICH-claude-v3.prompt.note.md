# CRICH second-family interface-closure audit (N40–N45, H01–H08, S10–S11)

**Counts: FATAL 0, MAJOR 0, MINOR 6.** All six are completeness or bookkeeping findings. None is a correctness defect.

Local closure is valid relative to the named boundaries once the repairs below are made, subject to the conditional items at the end. This does not approve full Sun7, runtime, novelty, Lean or human review. Errata v2–v10 and the governing addenda were applied throughout.

## Claim-wise verdicts

**C1. Order and acyclicity: VALID.**
- Every input in LEDGER LF257–262, plus the X2 additions of N01/N02, precedes its consumer in the v6 explicit order N01–N08, N15, N09–N14, N16–N59.
- The internal chains are N40→N41→N43→N44→N45 and N40→N42. There are no backward edges.

**C2. N40 NO4: VALID, with m5.**
- The declarations in NO4 LF32–48 map to providers as follows:
  - R0 and the K7 definition → N03, N15.
  - LFC, INV, E1/E6/E7 and ROW-U/E8 → N12, N13, N02, N14.
  - ROW-1 with the G2 transfer → N30, N32.
  - T, VFC, F7 → N09, N11, N10.
  - Sun(2)/(3) → N02, N01 (X2).
- The exclusions at LF50–51 hold.
- The MIX scope is (a1): 5 absent, on z, or on t. This is exactly where the apex-z ROW-1 premise holds (re-derived in m5).

**C3. N41 RICH: VALID (nit N1).**
- RICH LF22–40 is read with CE1 items 9a/9b (LF381–383, LF396–406). Providers:
  - R0, L0.1, Lagrange, K7 → N02, N03, N15.
  - LFC, INV, E1/E2/E6/E7 → N12, N13, N02.
  - E8 at three W-neighbours → N14.
  - T and VFC → N09, N11.
  - D23-MIX, used only in (a1) (LF35–38) → N40.
  - N32 (cons.) for the G5 pointer; N01 (cons.).
- F7, ROW-1 and ROW-2 are correctly absent as direct inputs.
- The withdrawn six-label branch (LF96–103) is replaced by R-1 LF15–22 and is unbound (note (ii), LF309).
- The remaining six-label arguments exclude sets using only Sun(2) pairs or Sun(4) gcd-3 four-subsets (CH LF63–64, LF71).
- The §6 navigation at LF212–213 is excluded by A12C LF5 (CH LF21, LF33).

**C4. N42 D23P: VALID, conditional on m5; edge nit in m1.**
- ROW-2 is applied at the marked apex z through CE1 PF1, which N42 owns (H05 LF185; governing addendum).
- Labels at z are n_j·x_zj/6, which do not depend on z's factor 2^E. So the H35 hypothesis is not imported (CH LF104).
- D23-CENTER is used at "5-marker anywhere" (LF35) for the (a2) case; see m5.

**C5. N43 A1S: VALID with m1, m2, m3, m6.**
- A1S LF10–19 is read with OV1 A1.3–A1.4. Direct Sun(5) occurs only at S10/S11 (via N07).
- I re-derived the suppression claim at A1.4 LF94–95, i.e. that 5^Bz and 5^Bt never enter a label gcd:
  - At a W-apex, c = x_uz ∈ {1,2,3} by MIX.
  - e = x_ut ≠ 5, and every W-entry ≠ 5, by NO5.
  - Bz·Bt = 0.
  - Together these mean no label gcd contains a factor 5.

**C6. N44 TC: VALID with m1, m2, m4.**
- Read through OV1 TC.1–TC.2:
  - FG7(b) enters only through FG-V (actual family).
  - Corollary 5/6 is used with the RF2 equality clause.
  - Corollary L enters only through its Sun(5)-free consequence "at least two entries 4".
- The measures at TC LF16 are correct:
  - μ(U_aU_u) = α_au/6 by L0.3.
  - μ(D_j) = α*_aj/6 by INV(b) with (V1).
  - Both orientations follow because inversion is an involution.

**C7. N45 A22: VALID with m1, m2, m4.**
- Entries lie in {1,2,4}: start from the E1 range 1–5, remove 3 by W3/E3 and 5 by NO5.
- F ∩ F* = ∅ by E7, since 4 + 4 > 6.
- Row R1 holds for every E ≥ 1 via TC.4 (H07).

**C8. S10/S11 are genuine five-piece S5W sites: VALID.**
- Setting:
  - At apex t of C^x, the VFC pieces R ∩ g_jU_j are right cosets of subgroups of U_t, by (V2).
  - When x = α*, the ambient group is U*_t of the actual inverted configuration (INV(a), E6).
  - The pieces have index d_j = x*_tj·n_j/6.
  - Right-translating by w⁻¹ and inverting gives five pairwise-disjoint left cosets in U_t, which is finite after R0.
- S10: d_u = 4w_u, so every pairwise gcd is 4, because the w's are pairwise coprime and prime to 30.
- S11 adds the z-piece, d_z = q_tz·2^E·5^Bz·w_z:
  - gcd(d_z, 4w_u) = gcd(q_tz·2^E·5^Bz, 4) ≤ 4.
  - Sun(5) then makes the five-element set not allowed under (V3).
- Scope checks:
  - There are 5 ≤ 6 pieces, and no seven-piece theorem is used.
  - Equal subgroups are allowed.
  - t's own marker never enters.
  - The route is S5; equivalently S4 on the inverted configuration (cf. v10 m4).
- The computer-assisted Sun(5) record cited at OV1 A1.4 LF89–91 is superseded by [S5W@S10/S11].
- Consumers N44/N45 use only the b ≤ 1 kills, which need only Sun(2)/(3) (note (i), LF307–308). This is correct given OV1 TC.2 and A22.1.

**C9. Rows.**
- H01 is VALID: K7 ⇔ n_i = 6r_i with the r_i pairwise coprime, since gcd(6r_i, 6r_j) = 6·gcd(r_i, r_j).
- H02–H04 are valid as interfaces; their consumer cells need repair (m1, m2).
- H05: see m5. H06: see m3. H07: see m2.
- H08's consumers (N49, N52) are outside this packet.

**C10. Exclusions: VALID.**
- No RPLP, Ppair, TG, K, minimal frame, Sun(7) or census premise is used (NO4 LF51; CE1 LF396–397; LF567).
- The computer-assisted Sun(5)/(6) records are cited only as transitive provenance (CE1 LF402–406, LF571–575; OV1 LF89–94, 243–244, 426–427). They are replaced by S5W/S6W via N11/N12 (X1) and via N07.
- TC §5–6, A22 LF57–62 and the Pc5′/Q_B discussions are navigation only (CH LF26–27, LF114).

## MINOR findings

**m1. Missing direct edges: N02, N15, N32 (completeness).**
- **Step:** H02 (LF182) lists consumers N40–N45 with discharge N02. By v5 m5(iv) and v7 m2, N02's consumers are exactly the nodes that list N02. N43, N44 and N45 (LF260–262) do not list it, yet each uses it directly:
  - A1S LF17 imports E1/E2, and OV1 LF87 declares a direct Sun(2).
  - TC LF16 uses L0.3, and OV1 LF242 declares a direct Sun(2).
  - A22 LF12 uses the E1 range, and OV1 LF426 declares a direct Sun(2).
- X2 added N02 to N40 for the identical declaration at NO4 LF50–51, but not to these three.
- Further gaps:
  - N45 states its theorem on the (a1) predicates (A22 LF12–16) but lacks N15 (compare v9 m2).
  - N42 lacks a conservative N32 edge for the G5 pointer at D23P LF43, although N41 has one for the same pointer at RICH LF33–34.
  - TC LF17's blanket import "everything imported by RICH and A1-STRUCT" covers N14 and N40, which are absent from N44's cell.
- **Consequence:** none mathematically, since all of these are reachable in the ancestry. However, the completeness statement in F01/R05 is false as written.
- **Repair (all forward edges):**
  - Add N02 to N43, N44 and N45.
  - Add N15 (cons.) to N45.
  - Add N32 (cons.) to N42.
  - Add N14 and N40 (cons.) to N44, or state that LF17 is discharged via N41/N43.

**m2. Row/consumer misalignment (bookkeeping).**
- **Step:**
  - H01–H03 (consumers N40–N45) are missing from the rows cells of N43, N44 and N45.
  - H04 is missing from N41, N43 and N44, although all three list N09 and apply T (RICH LF30; A1S LF17). N45 has no N09; it uses T only through A1S's section-0 triangle rule (OV1 LF423).
  - H06 and H07 are missing from N45, although OV1 A22.1 LF421–425 imports NO5, FG7 and Corollary 5/6 with RF2, and R1 for E ≥ 1 via TC.4.
  - H07 lists N44 as a consumer of its own discharge.
- **Consequence:** as written, N45's cells do not bind the E = 1 prerequisite supplied by TC.4.
- **Repair:**
  - N41: add H04.
  - N43: rows H01–H04, H06, A06.
  - N44: rows H01–H04, H06, H07.
  - N45: rows H01–H03, H06, H07, A06.
  - H04 consumers: "N40–N44; N45 via N43".
  - H07 consumers: N45–N47.

**m3. H06 attributes PFG-t to N41 (provider attribution).**
- **Step:** H06 (LF186) puts "PFG-t needs connectivity" under the discharge [B:CH] N41. PFG-t is actually an A1S lemma (CH LF25; OV1 LF413, LF423). Since N43 is also listed as an H06 consumer, the row has N43 consuming its own lemma.
- **Consequence:** no edge is missing (N43→N45 exists). But the connectivity hypothesis must be checked against N43's statement, not N41's.
- **Repair:** move the PFG-t clause to a row discharged by N43. Keep the FG7, Corollary 5/6, NO5, R3, TR, CC, TZ and LZ items under N41.

**m4. N44 and N45 declaration cells cite superseded text (completeness).**
- **Step:**
  - N44's cell cites "TC LF11–20". Its LF17–18 still reads "Sun(2)–Sun(5) … FG7 …". The governing text is OV1 TC.1–TC.2 (LF224–231, LF242–245).
  - N45's cell cites "A22 LF5–16". LF5–8 there has been replaced by OV1 A22.1 (LF421–427).
  - By contrast, N43's cell correctly cites its overlay.
- **Consequence:** read literally, the cells give wrong scopes:
  - N44 would admit Sun(4)/(5) and direct FG7, contradicting note (i) at LF307–308 and H06's auxiliary-scope restriction.
  - N45 would import R1 without the TC.4 extension to E = 1.
  - The overlays are already in the body cells, so this is a declaration-cell defect, not a correctness one.
- **Repair:**
  - N44: "TC LF11–20 as replaced by OV1 TC.1–TC.2".
  - N45: "A22 LF10–16; LF5–8 replaced by OV1 A22.1".

**m5. N40's ROW-1 instance is unowned, and the CENTER/MIX split is unrecorded (scope precision; conditional correctness risk for N42).**
- **Step:** The governing addendum (LF3) requires N40 and N42 to verify their own label-gcd premises. H05 records CE1 PF1 for N42 but records nothing for N40. Re-deriving N40's premise at apex z:
  - λ_u = w_u·x_zu for u in W, and λ_t = 3^A·5^Bt·w_t·x_zt.
  - Because g = 6, z's own factor 2^E·5^Bz never appears.
  - W–W label gcds equal the x-gcds.
  - t is the single odd {3,5}-smooth neighbour.
- This holds in all of (a1), which is exactly MIX's scope, in both orientations by INV(a)/E6.
- In (a2), the premise as stated at NO4 LF41–42 ("five unmarked labels") fails at every apex. Some vertex would need the separate 5^B never to enter a gcd, and that would have to be checked.
- N40's export cell (LF87) lumps CENTER and MIX together. Meanwhile:
  - D23P imports CENTER at "5-marker anywhere" (LF35).
  - CE1 P3b (LF569–571) says CENTER "rests on … ROW-1 … G2".
- **Consequence:** if CENTER's proof (NO4 LF54–99) invokes ROW-1/G2 in (a2) without that gcd check, N42's use in (a2) is unsupported, which would be MAJOR for N42. CH LF61 places the ROW interfaces only at NO4 LF30–42 and LF101–114, which suggests P3b is file-level provenance. I cannot verify this from the packet.
- **Repair:**
  - H05: add "ROW-1/G2 at apex z, both orientations, owned by N40 (NO4 LF38–42 plus the NO4-E ROW-1 transfer), MIX branch".
  - N40: split the export into CENTER (5-marker anywhere, NO4 LF54–99, no ROW-1/G2) and MIX ((a1), LF101–154).
  - Parent to confirm the split against NO4 LF54–99 and D23V LF5–8.

**m6. E8 instance ownership and S6 wording (bookkeeping).**
- **Step:**
  - v6 MIN-2 and v9 item 5 make each consumer check its own abstract gcd premise, and v10 m2 records this for N37/N38. No such record exists for:
    - N41's R3 instance: three W-neighbours (CE1 LF197–209, LF381–383).
    - N43's E3 instance: four W-neighbours plus one coprime label (OV2 LF26–27).
  - Both premises hold, as in m5. Because N ≤ 4, the R24 b ≥ 4 and R5 branches are vacuous and only Sun(2)–(4) are used.
  - X7 (LF16) lists N41 but not N43 as an S6 consumer, although both use N14 in the same way.
  - v9 item 5's list omits ROW-2 at D23P's apex z (CE1 PF1), where the R24/R5 branches can be live (P3b LF568–569).
- **Consequence:** bookkeeping only; no Sun(5)/(6) instance is left unbound.
- **Repair:**
  - Annotate N41 and N43 in the v10 m2 style: "E8 from N14 under the abstract premise; instance owned and checked in the cited body; N ≤ 4; no S5W/S6W binding".
  - Align X7.
  - Add "ROW-2 at D23P's z (U_z, or U*_z via INV)" to the S6 list.

## Nits (uncounted)
- **N1:** N41's body cell should read "RICH LF50–246 except LF212–213 (A12C LF5); LF96–103 replaced by R-1 LF15–22".
- **N2:** S11 should cite "with OV1 A1.10 LF172", as S10 does.
- **N3:** X2's citation "RICH LF39–40" is superseded by CE1 9a LF381–383. The direct Sun(2)–(4) content is unchanged.

## Conditional or not checkable from this packet
- The export texts D23V LF5–8, RDV LF9–13, A12V LF26–31 and A12C LF5, and the census lines CH LF39–58, were not supplied. So the intra-packet provider→consumer matches were checked only against consumer declarations, H01–H08 and CH LF94–110, and they stay conditional on those texts. The matches are: MIX at RICH LF35–38, CENTER at D23P LF35, the RICH base for N43–N45, A1S→TC/A22, and TC→A22.
- The N30/N32/N33 exports (BROW) and the N07/S4/S5 statements belong to separate gates.
- OV2 items V2.1 and V2.9–V2.11 are not assigned beyond N43's "as amended by OV2". If any of them amends TC or A22, add it to the N44 or N45 body.
- For CA2: D23-a2 (H08) needs a named provider, presumably N42, in the N49/N52 inputs.
