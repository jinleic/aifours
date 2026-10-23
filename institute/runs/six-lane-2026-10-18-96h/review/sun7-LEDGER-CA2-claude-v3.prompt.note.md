# CA2 (N46–N52): 0 FATAL / 0 MAJOR / 6 MINOR, plus 3 uncounted nits

I applied ledger errata v2–v10. None of v9 or v10 weakens a provider used here. All six findings are completeness or bookkeeping issues. There are no correctness, process, priority or computation findings.

## Claim-wise verdicts

- **Order and acyclicity: valid.**
  - Every input of N46–N52 precedes its consumer in v6's explicit order. This covers the inputs in LEDGER LF263–269 plus worker erratum X2/X3.
  - N49→N51→N52 and N50→N52, so the units precede A2X.
  - No edge runs from N46–N48 into N49–N52, and there is no back edge.

- **N46 K23: valid (m1, m4).** K23 LF5–14 with R2E E3–E4 is fully covered:
  - A1S, TC and A22 come from N43–N45 at A06's OV1→OV2 scope.
  - RICH's Cor 5/6, FG7, NO5 and D23-MIX come from N40/N41. K23 has no D23P use, so no N42 edge is needed.
  - LFC, INV, VFC, L1 and R0 come from N12, N13, N11, N09 and N03.
  - Sun(2) comes from N02 and Sun(3) from N01 (X2).
  - Inversion is actual inversion only (E6; R2V LF13).
  - **E4's 44411 kill, re-derived.** At apex t the labels are w_uα_tu.
    - Put y=1/3 on the three labels 4w_u (pairwise gcd 4).
    - Put y=1 on the two labels w_u (gcd 1 with every other label, so singleton-only by Sun(2)).
    - The value is 6, so Σyα/6=1, which contradicts LFC(d).
    - Only Sun(2) is used.

- **N47 CELL: valid (m5).**
  - CELL LF11–13 with E15 is covered by N41, N12, N13 (E6 covers "nor in its inverse" and the CELL-B mirror), N11, N02 (including L0.2) and N03.
  - The three left cosets in K∩L are a direct Sun(3), which goes to N01 under X1.
  - CELL's "Used from them" list (LF9–10) needs only N43, N44 and N46. So the absence of an N45 edge is correct.

- **N48 A1CL: valid (m1).** The R2V LF17 split is exhaustive. TZ(iii) gives T=W or T*=W, which yields three cases:
  - Both hold: Case A.
  - Only T=W: Case B.
  - Only T*=W: the mirror, which is the actual inversion of Case B with the same labelled indices and markers (E6).
  - The providers are N45, N46/N47, N43/N44, N41 (TZ), N13 and N03. There is no direct Sun use (X4).

- **N49 A2F: valid relative to m2, m3, m6 and B1.**
  - F5 LF22–36 is covered:
    - D23P from N42 and RICH from N41.
    - E1/E2/L0.1/L0.3 from N02, E6/E7 from N13 and E8 from N14.
    - L1 from N09, VFC from N11 and R0 from N03.
    - N01 via X2.
  - The TRANSFER premise (OV2 LF183–186) comes from N43–N45.
  - The TRANSFER restrictions hold as stated:
    - In (a2-no5), 5∤β_zt, so FG-a2(a) applies.
    - β_zt≠5, and β_zu≤3 on W′ by D23P "for each x" (F5 LF26), so FG-a2(b) applies.
    - The parameters are the actual α of C, all ≤4.
    - The VFC q is the actual α* (INV(b)).

- **S12: valid relative to B2.**
  - The ambient is U_t with five pieces (inverted via (V3) if the route is S5).
  - In (a2), t carries no 5-marker. For λ_p=2^i5^Bw_p against 2^{i′}w_u, the gcd is 2^{min(i,i′)}.
  - So all gcds are ≤4 whatever role p plays in the row (one, two or four).
  - S5W applies at k=5 with no distinct-subgroup hypothesis (LF312). The N07 edge is present.

- **N50 UN1: valid.**
  - U1A LF24–32 imports foundational providers only: N02, N03, N09 and N11–N13.
  - The cell-subgroup Sun(3) goes to N01.
  - There is no N49 edge, and LF30–32 is attribution only, not an (a1) theorem.

- **N51 UN2: valid (B3).**
  - FG-a2 is used only for β=α*. Its hypotheses hold:
    - α*_zt=1, from α+α*≤g (E7) with α_zt=5.
    - α*_zu∈{1,2,3}.
  - BRIDGE and TRANSFER are correctly unused, because α_zt=5 lies outside (a2-no5).
  - These readings match LFC(a),(d) and VFC (V1),(V2),(V4) at g=6:
    - labels r_jx;
    - measures x′/6;
    - local indices r_jx′.

- **N52 A2X: valid (m1).**
  - U3A LF16–26 is covered (N01 via X3).
  - R2V is used for scope only, and there is no N46–N48 edge.
  - TRANSFER is used only on the no5 list.
  - **LF134–139 Sun(3), re-checked.**
    - The index triples (2·3^Aw_t, 2ρ_v, 2ρ_a) and (2·3^Aw_t, 2ρ_a, 2^{E+1}w_z) have pairwise gcd 2.
    - This holds because each ρ is odd, prime to 3 and pairwise coprime (ρ_p=5^Bw_p included).
    - m_z^H=3 follows from v3(n_z)=1.

- **Exclusions: valid.**
  - There is no Sun(7), no least-order frame, no seven-piece L5/FH, no C18 call and no computed coverage.
  - StageB F-1 and TX/ZA/ZB/R3 appear only as provenance (CA LF38–48; U1A LF30–32; U3A LF24–26).
  - Historical computer-assisted Sun5/6 clauses stay live only as A08 rebinds them to S5W/S6W at S4–S6 and S10–S12.

## Findings (all MINOR)

**m1. Rows and consumer cells are not aligned (bookkeeping).**

- *Problem.*
  - A01, A02, A03 and A06 name N48, but N48's rows cell is F10 only. N48 uses only R0 (N03), INV/E6 (N13) and A1/TC/A22 statements. It has no N02, N09, N11 or N12 edge. Its N41 edge (TZ(iii), R2V LF17) appears in no A-row.
  - N49's rows cell (H08, A05) omits A01–A04, although A04 names N49. It also omits A06 (N49 is the TRANSFER consumer of N43–N45) and A08 (N49 carries S12).
  - N52 lists A06, but A06's consumers are N46–N48. N52 has no N43–N45 edge and reaches them only through A05/TRANSFER (U3A LF19, LF23, LF26).
  - The A04 and A06 discharges are not per-consumer. N46/N47 have no N42 edge, N52 has no N41 edge, and N47 has no N45 edge.
- *Consequence.* None mathematically. The literal rows misstate edges.
- *Repair.*
  - N48 rows: A01 (R0 only), A02 (INV/E6 only), A06, the row carrying TZ(iii), F10. Drop N48 from A03.
  - N49 rows: A01–A06, A08, H08.
  - A06 consumers: N46–N49, with the restriction reading "except by A05/TRANSFER in (a2-no5)". Drop A06 from N52.
  - A04 per consumer: N46 and N47 take N41; N49 takes N41 and N42; N52 takes N42.
  - A06 for N47: N43 and N44 only.

**m2. A02's provider column is stale under v5 m2 and v6 MIN-2 (bookkeeping).**

- *Problem.* A02 lists "LE E1–E8" discharged by N12 and N13. But:
  - E1 (LE LF14–18) and E2 (LF23–24) are N02 exports.
  - LF19's K7 instance (α≤5) is owned by the consumer.
  - E8 (LF71–78) is an abstract N14 export.
  - Only E3 (N12) and E6/E7 (N13) belong to A02.
- *Consequence.* None. Every node using E1/E2 has an N02 edge, and the only E8 consumer, N49, has an N14 edge.
- *Repair.* Re-cell A02 as E3/E6/E7. Route E1/E2 via A01/N02. Route E8 via N14 for N49 only (see m3).

**m3. N49 has no consumer-side E8 premise cell (completeness).**

- *Problem.* F5 LF32 imports E8. Under v6 and the CA2-v2 header LF10, N49 must check for each chosen set X that the label gcds equal the α-gcds. This is not automatic in the zt5 data:
  - At u∈W′, gcd(λ_z, λ_t) = gcd(3·2^Ew_z, 3^Aw_tα_ut) ∈ {6, 12}, while gcd(3, α_ut) = 1.
  - At u∈W′, λ_z against w_jα_uj with α_uj∈{2,4} gives gcd 2 or 4, against an α-gcd of 1.
  - At apex z, gcd(5·3^Aw_t, 3·5^Bw_p) = 15, while gcd(5, 3) = 1.
  - The premise does hold for X⊆W∖{apex}, with p handled by (B2). This is exactly what OV2 V2.7(ii)/(vi) does for TRANSFER's E3.
- *Consequence.* F5's E8 steps are not certified by this packet. The pre-v6 CA census was not this check.
- *Repair.* Add a cell in v10 m2 style: "E8 instances are owned by N49; the premise is checked per use at F5 LF… with X⊆W∖{apex}, p by (B2), and z/t only with a separate check."

**m4. The Corollary-L notes are incomplete (accounting).**

- *Problem.*
  - Note (i) (LF307–308) omits N46's second Corollary-L use: the 44411 (b=3, k1=2) kill in R2E E4 LF139–141. That kill uses only Sun(2) and LFC(d) (verified above), so no new site is needed.
  - S12's consumer cell names N49 only. N52 imports TRANSFER as exactly OV2 V2.7 and so inherits the S12 binding.
- *Repair.* Amend Note (i) to include the 44411 use. Set the S12 consumers to "N49; inherited by N52 (Sun(2)/(3) consequence only, U3A LF64–67)".

**m5. N47's declaration text is not aligned with A06 (literal scope).**

- *Problem.* Under "CELL LF5–13 + R2E E15", lines LF5–10 still describe A1-STRUCT, TC and TC-A22 as "unreviewed" and "read through OV1" only, with TC-A22 as a condition. N46's equivalent text was replaced by R2E E3.
- *Consequence.* N47's literal premise binds to the OV1-only reading. That is wrong if OV2 amends Lemma TC, FG-V, CASEB or TC-B.
- *Repair.* If one of E14–E24 (already in N47's body cell) repairs CELL's status line, cite it. Otherwise add: "N47 consumes Lemma TC, FG-V, CASEB and TC-B at A06's OV1→OV2 scope; TC-A22 is unused (no N45 edge)."

**m6. N41→N49 is an argument import but is not named as one (completeness).**

- *Problem.* F5 LF29–31 imports RICH's G0, the proofs of FG7 (chain form) and Cor 5/6 (re-run in F5 §2), and all §4 statements and proofs (the ZT5 re-run). Under the v4 m5 and v9 m1 convention, such re-instantiated arguments need an explicit provider export. N49's cell lists only "N41".
- *Consequence.* Cor 5/6-a2, FG7(b) and S1–S5, which feed N51 and N52, cannot be matched to N41 from this packet.
- *Repair.* Rewrite N49's input as "N41 (statements plus ARGUMENT export: G0, FG7 chain proof, Cor 5/6 proof, §4 read with R1E R-1 and CE1; re-instantiated via (B1)–(B4))". The matching export belongs in N41's cell or in H08, which is CRICH's gate.

## Nits (uncounted)

- **n1.** OV2 V2.7(vi)'s "(F7)" is A2-FIVE's own F7 (CA LF13), not addendum F7 (N10). No N10 edge is needed, but the label should say so.
- **n2.** X3's "K cap L" is K∩H with HK=G in U3A LF134–139's notation.
- **n3.** N48's cells should name N41 as the provider of TZ(iii).

## Boundaries (these keep claims conditional; they are not findings)

- **B1.** OV2 LF190 voids TRANSFER on any further erratum to A1-STRUCT, TC or TC-A22. N49 and N52 therefore hold only while N43–N45 carry no source erratum after OV2. A12C LF5 must be confirmed to be scope-only, and any CRICH source erratum reopens N49.
- **B2.** S12's "same 5 pieces" and its "via S5" route depend on CRICH's S10/S11 instance list. If those instances are on the LFC side, the route reads "via S4", which is equivalent by INV (see v10 m4 S9).
- **B3.** The literal FG-a2, Lemma F, D23-a2, S1–S5 and BRIDGE statements at A12V LF33–37 are not pasted. Applying them to Γ* is valid provided FG-a2 is stated for every actual (a2) configuration, since Γ* qualifies by E6 with matrix α*.
- **B4.** N01–N15, S5W/S6W (N07/N08), the N40–N45 exports and N59 are separate gates.

## Conclusion

Once m1–m6 are applied, local CA2 closure of N46–N52, rows A01–A08 and S12 is valid relative to the named boundaries. N49's E8 steps and RICH re-runs stay conditional until the m3 and m6 cells exist. This gives no global Sun7, runtime, novelty, human or Lean approval; full Sun7 remains UNACCEPTED.
