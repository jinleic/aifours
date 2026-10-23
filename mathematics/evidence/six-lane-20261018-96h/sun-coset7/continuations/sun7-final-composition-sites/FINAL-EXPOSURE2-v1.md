# FINAL-EXPOSURE2-v1 — exposure-2: the literal interfaces still missing after FINAL-EXPOSURE-v1 (X1 MAJOR/MINOR, X2 MINORs) [exposure only; CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read at 2026-10-19T22:44:43-0700, immediately before this exclusive create. Owner SunM13MixedFibres, math-1.
- **Frozen scope:** `FINAL-EXPOSURE2-SCOPE-v1.md` 24700e6231e9201a9b1b6f7896b40e17c654c6d5ebf309ed05c93b7035ebcd7b (22:37:06). Disposition
  `RUN/review/sun7-EXPOSURE-X1X2-first-family-parent-disposition-v1.json` e62c5381…c250; reviews X1 23d988db… (0F/1M/1m), X2 a1ebf766… (0F/0M/2m).
- **Parent rulings adopted (disposition LF28-31):** a record-internal citation is sound when the verdict accepts that proof
  content with every inherited hypothesis, mandatory overlay and exclusion retained; acceptance of a theorem alone does not
  establish every assertion in its file. CAP LF80: qualified as in section 9.
- **Reading.** Rows are locators; every cited range is bound in packet Y1 (sections 1-6) or Y2 (sections 7-9). Roots and
  verdict abbreviations as in FINAL-EXPOSURE-v1 LF5-10. CE1 = D/K7-D23RICH-D23P-erratum-v1.md; OV1, OV2 = D/K7-A1-A2-delta-
  erratum-v1/v2.md; ecff = D/K7-R2-R3-consolidated-erratum-v1.md; R2E = D/K7-R2-repair-erratum-v1.md; K23E, CELLE = the
  CASEA-K23 and CELL errata; U1, U2, U3 = A/K7-A2-UNIT-1/2/3-v1.md. Nothing is re-derived; no new mathematics.

## 1. RICH Lemma R3 and survivors S1-S4 (n50)
- Accepted reading: RDV LF10 ("R3 (survivors S1-S4 are local-test survivors only)"); CE1 LF581-584 lists R3, S1-S4 and
  Corollary R3 among the unchanged statements.
- Literal text: RICH LF117-176: set-up and label-gcd table LF119-123; **Statement** LF125-128; proof LF130-160; survivors and
  weights LF161-172; Corollary R3 LF174-175.
- Mandatory overlays: CE1 RF4 LF185-210 (standard weights used only in the two k3 = 1 cases, subset form of E8 and H5);
  CE1 RF5 LF212-240 (5a: replaced (1,1) text; 5b: S1-S4 are local-test survivors only, not claimed realisable, weights not
  claimed LP-optimal).
- In (a2-no5) these claims enter only through the enumerated BRIDGE (OV1 A2.10 New LF620-628: "R3 with S1-S4 as local-test
  survivors only (RF5) and Corollary R3").

## 2. D23P in full (n51); no pointer to part A
- Accepted export: RDV LF12-13.
- Literal text, whole file: D23P LF1-124 (setting LF8-19; Theorem K7-D23P LF20-22; accepted imports LF24-46; row trichotomy at
  z LF48-69; proof LF71-112; scope LF114-124).
- Mandatory overlays: CE1 LF1-22 ("No statement change"); PF1 = P1 LF425-460 (ROW-2 transfer to the marked apex z); PF2 =
  P2a-P2d LF462-538 (M1 exact triangle tables, why x = 5 dies, normalisation before the F7 step; M2); PF3 = P3a-P3b LF540-577
  (imports: L0.3 listed; transitive Sun(5)/Sun(6) closure); unchanged list LF579-589.
- The part A exposure (manifest 849fadd9…) is replaced here by direct inclusion; its review result is not a premise.

## 3. PFG-t (i)/(ii) and Corollary L (n52)
- Accepted export: A12V LF26 ("Lemma PFG-t (i)/(ii) under connectivity, with Corollary L as a necessary condition only");
  bound by its hypothesis: A12V LF46.
- Literal text: A1-STRUCT LF50-58 (hypothesis: Gamma^x connected; (i) LF55-56; **(ii) LF57-58**); proof LF60-69; Corollary L
  LF71-95; LF97 ("every surviving M has at least two entries 4").
- Mandatory overlays (OV1, then OV2): A1.4 LF77-96 (Sun accounting: the Sun(5) use of Corollary L; "at least two entries 4"
  uses only the b <= 1 kills, Sun(2)/Sun(3)); A1.7 LF124-136 ((i) proof: FG7 (a)); **A1.8 LF138-149 ((ii) New: "so S_R contains
  z and is allowed (VFC (V3)); S_R lies in W cup {z} (apex t) and S_R cap W is an allowed W-set of y-weight 1.")**; A1.9
  LF151-161 (Corollary L: necessary condition, no realisability claim); A1.10 LF163-173 (44444 feasibility [Sun(5)]). OV2 has
  no item on PFG-t in (a1); its V2.7 (v) adapts the proof of (i) for the (a2-no5) transfer (OV2 LF183-206; exposed whole in X1).

## 4. K7-REM with NF parent errata v1-v3 and the verdict scope (n58)
- Verdict scope: NFV LF1-24 (LF5 status; LF9-12 the exact accepted statements; LF18 the parent check, including the (a1)/(a2)
  split; LF22 boundary).
- Parent errata, in order: v1 21f31a50… (LF5: proof line 143 wording); v2 758bd8bb… (m1-m4); v3 0eb500d6… (supersedes only the
  last sentence of v2 item 3; accepted wording for NF LF55-57: "Not cited directly: ...").
- Literal text: NF LF83-133: Theorem K7-NF LF83-86, proof LF88-111, remarks LF113-118; (a1)/(a2) definitions LF121-125; Lemma
  "F = (a1) disjoint-union (a2)" LF126-128; Corollary K7-REM LF129-131; Boundary LF132-133.
- As stated there: K7-REM uses Theorem K7-NF and the accepted (a1) closure (R2V LF5); it is a reduction (NFV LF12).

## 5. Unit 1 and Unit 2 literal contracts and their join applications (n66-n68)
- Accepted scope: A2XV LF13 (Unit 1 "at their stated hypotheses only"; "The omitted-marker bounds are hypotheses here, not
  general K7 assertions"), LF14 (Unit 2: normalised zt5 S-setting), LF15-17 (Unit 3 and the order of joins).
- **Unit 1 (packet Y1):** setting U1 LF8-23; foundational interfaces LF24-32; G_z/G_t := (L_z) and (V_z), and G_t likewise,
  LF34-40, as HYPOTHESES (LF38); TC LF42-45; K3 LF46-48; row tools LF50-56; B LF58-61; rigid rows R1, R1minus, R3/R3prime, R4/R5,
  R6 and two impossible rows LF62-77; Twins LF79-81; H_A LF83-91; five-index EQ LF144-149; SUB LF150-152; IN LF153-156;
  vertex-wise CELL LF157-165; M_A LF166-179; M_B LF180-191; export contract LF193-201. Not exposed: LF92-143 (proof of the
  H_A Case-A theorem: K2, type list, all22, refined matrix); its statement is the export at LF194-196.
- **Unit 2 (packet Y1):** setting U2 LF7-14; normalised S-data and the FG-a2 interface LF15-24; light lemma and VFC form
  LF26-34; omitted-marker chain FG-zf LF36-43; the bounds (L_z)/(L_t) and (V_z)/(V_t) LF44-47, with the FULL-gcd6 remark
  LF48-51; "Alpha has no W-three" LF53-56 (statement and set-up; proof LF57-86 not exposed); connected-graph bound LF87-96; ZT
  LF97-107; ZTR LF108-113; B-test LF115-120; ZS LF121-126; ZW LF128-143; exports LF145-152.
- **Unit parent errata (packet Y2, whole):** Unit 1 e9b104b2… (m1-m13, o5; item 2: G_z/G_t only as hypotheses); Unit 2 v1
  b6a2a8cc… (m1-m7) and v2 4ec9c8f5… (supersedes v1 item 2: G_z/G_t = (L_z)^(V_z) and (L_t)^(V_t) as stated at U2 LF45-47,
  proved from the FG-zf equalities LF36-43); Unit 3 d6b79ae6….
- **Join applications (packet Y2):** U3 LF47-54 (partition no5/zt5), LF55-80 (no5: H_A through Unit 1 at LF67-69; Unit 1
  R1/R1minus and K3 at LF74-75; M_B at LF77), LF82-89 (zt5, T* = W: Unit 2 ZS, ZW, G_z/G_t, ZT/ZTR for (CL), then H_A),
  LF91-140 (zt5, |T*| = 3: ZS, ZT, B-test, Unit 1 rows/K3, CELL, Unit 2 FULL bound at LF122-123).

## 6. MINOR m1: the "RICH section 6" locator (proposed reading for the parent; no mathematical change)
- The texts: A12V LF36 accepts "Theorem K7-A2-BRIDGE in its enumerated A2.10 form"; OV1 A2.10 New LF620-628 enumerates
  "Theorem K7-D23-RICH" and then says "RICH section 6 (navigation) and section 9 (residue description) are not transferred";
  A12V LF47 lists "RICH §§6 and 9" as not transferred. RICH section 6 (LF201-213) contains Theorem K7-D23-RICH (LF203-205), its
  proof (LF207-210) and a navigation paragraph (LF212-213), replaced by CE1 RF6 item 6a (New LF253-257: "Navigation only: ...
  No other local pattern is excluded."); RDV LF11 accepts that paragraph only as a navigation remark. Section 9's residue
  bullet is replaced by CE1 RF6 item 6b (LF260-273).
- Proposed reading: the excluded "section 6 (navigation)" is the navigation paragraph RICH LF212-213 as replaced by RF6 6a, and
  "section 9" is the residue description of RF6 6b. Theorem K7-D23-RICH transfers to (a2-no5) only as enumerated at OV1
  LF623. The parent owns A12V and may confirm or correct this reading.

## 7. R2 chain: K23E, CELLE, ecff R2.1-R2.4 and R2E in the governing order (n55-n57)
- Order (R2V LF31; R2E LF16-27): (1) apply R2E E1 to ecff R2.1's New field and R2E E2 to CELLE C.2's New field; (2) CASEA-K23:
  K23E (whole), ecff R2.1 (as amended) and R2.2, then R2E E3-E13; (3) CELL: CELLE C.1-C.4 (C.1 amended by ecff R2.4, C.2 by
  E2), ecff R2.3, then R2E E14-E24; (4) R2E E25-E29 target the review package only ("Package status/citation replacements are
  informational only", R2V LF31). All 29 R2E items are mandatory (R2V LF40).
- Packet Y2 binds K23E LF1-35, CELLE LF1-60, ecff LF38-114 (R2.1 LF44-65, R2.2 LF66-82, R2.3 LF83-98, R2.4 LF99-114), R2E
  LF1-28 (header, reading order) and LF55-666 (E1-E29 and boundary); R2E LF29-54 (finding-to-item table) is not bound.
- Amended interfaces named by the review: EQ = R2E E16 (LF366-384); IN = ecff R2.3 (LF83-98) then R2E E17 (LF385-400);
  vertex-wise CELL = R2E E18 (LF401-459); CELL-A/CELL-B steps E19-E23 (LF460-547); K3 distinct vertices = ecff R2.2; the S-f
  triangle = ecff R2.1 amended by E1 (LF57-74).

## 8. X2 MINOR 1: full governing overlay order for n71-n73
- **n71 (K62-E3).** Base K62-E3-v1 (70a60d55…) -> erratum v1 (095c31dc…, F1-F3) -> consolidated erratum v2 (f9f52e1b…, Z1-Z12).
  Erratum v2 LF5-6: "Erratum v1 F1 and F3 are superseded by items Z11 and Z6 below, which contain them; erratum v1 F2 stands"
  (also E3V LF10). No statement changes (v2 LF14-15, LF323-326). Replacement arguments imported in proof form by the exposed
  consumer declarations (SH-DG erratum G1 LF157-161; K62-M13-A LF10-12; K62-CAP LF15-17): Lemma 1 and its gcd computation (Z2),
  Lemma 3 in proof form for every non-empty Q (Z6, Z10), the step 3 argument (Z8), C2 and its sub-claim (a) (Z11, with the
  section 5 preamble Z9), premises (Z1). Packet Y2 binds v2 LF1-16, Z1 LF38-66, Z2 LF67-90, Z6 LF137-172, Z8 LF196-220, Z9
  LF221-243, Z10 LF244-262, Z11 LF263-298 and LF323-333, and erratum v1 whole. Not bound: Z3-Z5 (Lemma 2 proof wording), Z7
  (step 0), Z12 (navigation labels) and the disposition table LF17-37; they change no statement (LF323-326). Any use of
  them in proof form is CONDITIONAL here.
- **n72-n73 (K62-DG).** Base K62-DG-v1 (a4bfc41e…) -> K62-DG-erratum-v1 (e435430c…, section 5 step 3; "stays in force", SH-DG
  erratum LF5-6) -> combined K62-SH-DG-erratum-v1 (755edc21…) items G1-G8. SHDGV LF11: "Read the base texts only through these
  corrections"; SHDGV LF32: "Unembedded L1/VFC citations are withdrawn from DG." So the base citations of L1 and VFC (for
  example DG LF41-43) are not operative: G1 (LF139-171) withdraws them, G3 (LF197-222) derives DG-3 from L0.1 and Lagrange, and
  G8 (LF283-317, corollary only) uses LFC (c) of the original configuration. Packet Y2 binds SH-DG erratum LF1-17 and G1-G6
  (LF139-269), DG erratum v1 whole, and SHDGV LF7-12, LF31-32. Not bound: G7-G8 (P_ob corollary only; consumers n77-n78 use
  DG-1..DG-4 and Theorem DG with G5/G6: M13-A LF13-14, FULLV LF23) and S1-S5 (SH; S2 exposed in X2 for n74).

## 9. X2 MINOR 2: negative assertions qualified to the exposed interfaces
Read FINAL-EXPOSURE-v1 with these replacements (old text unchanged on disk):
- LF49-50: "In the exposed lines (K62-CAP-v1 LF70-80; CAP-DT erratum v1 LF131-154) there is no citation of Lemma CAP."
- LF51-55, first clause: "These displayed uses do not require LF80. A text search of the final-chain directories for 'upward
  closed' and 'L8 M1' (a process record, not a derivation) returned only rules-k7-v1 LF80 and rules-k7-addendum-v1 LF124. No
  universal-absence claim is made." The rest of LF53-55 stands.
- LF61-63: "No separate written export of rules-k6-v1 L8 (M1) is exposed here; its status elsewhere is not determined here. The
  displayed uses do not require it." Packet Y2 binds rules-k6-v1 LF175-180 and the Sun(6) gate verdict LF13-17 for reference.
- LF64-66: "CAP-ENV, at the exposed interfaces: the displayed uses reach rules-k7 Lemma CAP only through its accepted written
  gcd-capping argument (WV LF23, LF42) and do not require the LF80 clause."
- LF68-72: "No separately accepted written statement is exposed here for ... (list unchanged). Under the parent ruling
  (disposition LF29) these record-internal items may be cited where the governing verdict accepts that proof content, with all
  inherited hypotheses, overlays and exclusions retained; the X1 review confirmed n18-n23 on that basis. The Unit 1/2 contracts
  are now exposed in section 5. Whether that suffices remains the parent's decision."

## 10. Status and non-claims
Exposure only: every judgment is CANDIDATE_UNVERIFIED. Full Sun(7) UNACCEPTED; completeness certification WITHHELD pending
the parent's disposition of these exposures and the final composition review. Historical Sun(5)/Sun(6)/StageB records stay
computer-assisted; StageB F-1 permanent. No novelty, Lean, human-review or runtime claim. Old files unchanged; metadata and
reading only.
