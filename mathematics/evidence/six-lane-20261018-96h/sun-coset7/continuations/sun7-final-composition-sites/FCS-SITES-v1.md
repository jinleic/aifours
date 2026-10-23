# FCS-SITES-v1 — site-by-site STATEMENT-ONLY substitution checklist for the final Sun(7) composition [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read at 2026-10-19T21:39:23-0700, immediately before this exclusive create. Owner SunM13MixedFibres, math-1.
- **Frozen scopes:** `FCS-SCOPE-v1.md` 32ee3245a9a92471fc8134b291d22d5566e6cfe284f86d72deb15870a80c4b07; `CUT3-SCOPE-v1.md` 56162bfd…92df;
  `FINAL-SCOPE-addendum-v1.md` 8ee0d35d…4bd0 (this directory). Companion: `CUT-v3.md` 79ae0763…cfa (node ids "n.."
  below refer to its section 7). Roots and abbreviations as in CUT-v3 (S, D, K62, A, O16, R, R16, OV1, OV2, CE1, R2E, WV).
- **Nature.** An audit of citation sites, not a proof. No accepted theorem is re-derived; each site is judged only by
  matching its literal use against the literal replacement statement and the S56W substitution rules. Full Sun(7) is
  UNACCEPTED; nothing here certifies completeness.

## 0. Replacement authorities and the rules every site must satisfy
- **S5W / S6W** (S/continuations/sun56-written-composition/S56W-v1.md LF16-25, read with parent errata v1 b2299b6f… and v2
  ef62c628…; accepted by R/sun56-S56W-parent-verdict-v1.md 63baa72b… LF5-14): for EVERY group and five (resp. six) pairwise
  disjoint LEFT cosets of finite-index subgroups, some pair of indices has gcd >= 5 (resp. >= 6); subgroups may coincide; no
  cover, finite-original-group, abelian, solvability, normality or prime-power restriction. Statements are mathematically
  identical to the historical Sun(5)/Sun(6) statements with notation normalised (erratum v1 item 2; v2 m1).
- **Written lemmas accepted with S56W** ("the displayed written lemmas", verdict LF14): L0.1-L0.6 (S56W LF38-48; G finite,
  erratum v2 m8), L1-L2 (LF49-53), L3 and K2 for PAIRWISE DISJOINT cosets only (LF54-61 with erratum v1 item 1), Prop 4.5
  (LF67-103), R1 (LF106-115), R1(6) (LF126-137), R0 (LF143-147). Prop 4.5/R1/R1(6) qualify only through these re-proofs
  (erratum v2 m5).
- **K52W / KIIW** (R/sun7-K52W-parent-verdict-v1.md LF5-9; R/sun7-KIIW-parent-verdict-v1.md LF5-11).
- **VFC fibre geometry**: WV LF34 with mandatory overlay item 3 (WV LF48), an accepted written derivation independent of the
  old records (also confirmed in R/sun7-CUT2-M3-codex-v1.prompt.stdout.txt LF73-78).
- **Substitution rules** (S56W LF182-186; erratum v2 m4, m6; verdict LF14): statement-only, at individually checked sites; the
  family must consist of pairwise disjoint LEFT cosets of finite-index subgroups (right cosets inverted first, with the same
  subgroups); exactly 5 or 6 cosets, obtained by deletion; indices taken in the ambient group where applied (e.g. U_v); no
  Sun(5)/Sun(6) minimal-order frame or frame-only result (e.g. old C18); no old internal bridge/certificate/exclusion lemma
  under the new label.

## 1. Replacement map (summary)
| old authority | load-bearing sites | new authority | binding conditions |
|---|---|---|---|
| Sun(5), R16/sun-coset5-parent-verdict-v1.md 2cf02436… | TS2; TS4/TS5 at \|T\| = 5; instances IN1, IN3, IN7 | S5W (n14) | left cosets (VFC: inverted), exactly 5 by deletion, any group incl. U_v, equal subgroups allowed |
| Sun(6), R16/sun-coset6-parent-gate-verdict-v1.md efe1d849… | TS1; TS4/TS5 at \|T\| = 6; instances IN1, IN6 | S6W (n15) | same, exactly 6 |
| Prop 4.5 inside the old Sun(5) record (proof-v4 section 2) | IL2 | S56W section 3 (n09) | tuple (2r1,4r2,4r3,4r4), r's pairwise coprime, r1 odd |
| L0 proofs in old sun-coset5 rules-v1 L0; [GEN] L0.3 | IL1, IL3 | S56W section 2; LFC-INV erratum E1/E2 (n01, n04) | finite G (after R0) |
| VFC (V2)-(V4) proofs in old proof-v4 section 5 / proof-k6-lemmas section 1(b) | IL8 (with TS4) | WV LF34 + overlay item 3 (n17) | none further |
| StageB, R16/sun-coset7-stageB-classes-parent-verdict-v1.md fd14952c…: K5.2* | KS1-KS3 | K52W (n35) | exact README LF94 class; the D2' case is removed by written D2' (n30) in COVER |
| StageB: KII | KS1-KS3 | KIIW (n36) | README KII (a = 2) inside KIIW's scope |
| rules-k7 K (L2/L3), P (L4), F (L5), Lemma CAP, RPLP, FH, minimal frame | IL5-IL7, IL9, IL10, IL12, TS3 (frame clause) | none | DROP: not in the final proof-use closure; must not be imported |

## 2. Theorem-statement sites (TS)
| id | site (file LF) | old citation and statement used | ambient group | coset side / inversion | deletion | cofactor / marker conditions | replacement and needed internal lemma | status |
|---|---|---|---|---|---|---|---|---|
| TS1 | O16/README.md LF61 (R1(7) step 1); parent derivation WV LF20, LF32; COMP LF36 | Sun(6) (k6 verdict efe1d849…): with a >= 3, every vertex is 5-divisible and every pair has gcd exactly 5, so any six of the seven cosets contradict Sun(6) | the CE group (finite after R0, README LF29); S6W holds in every group | the seven given left cosets; no inversion | any 6 of 7 (README LF25) | none (gcd 5 < 6 for every pair) | S6W (n15); P1(i)-(ii) are README's own (LF46-52) | SUB |
| TS2 | README LF63 (R1(7) step 3); WV LF32; COMP LF38 | Sun(5) (k5 verdict 2cf02436…): every 5-subset contains a pair with gcd >= 5, i.e. (a <= 1, P1) gcd 6, a pair inside C; hence \|C\| >= 4 | CE group | left cosets; no inversion | every 5-subfamily of 7 | none | S5W (n14) | SUB |
| TS3 | README LF13-17 (imports), LF25 (deletion clause); rules-k7-v1 LF13 | declarations "Sun(5)/Sun(6) for every group"; "Imports available inside any subgroup: Sun(t) for t <= 6" | every group, incl. subgroups | — | k-subfamilies by deletion | none | S5W/S6W at the same scope (citation only). The LF13 clause "Sun(7) inside a subgroup only for a proper subgroup of a minimal counterexample (README section 6)" is DROP (frame unused, IL12) | SUB (+DROP clause) |
| TS4 | rules-k7-v1 LF43 ((V3): \|T\| <= 6, "only imports are used") and LF46 ((V3) proof: Sun(\|T\|) in U_v); WV LF34 ("every subset of at least two simultaneous pieces obeys Sun(t), t <= 6") | Sun(5)/Sun(6) applied to 5 or 6 pieces in one right fibre R = U_v y | U_v (finite; any group suffices) | pieces are right cosets (U_v cap w_jU_jw_j^-1)w_j; right-translate by y^-1, then invert: pairwise disjoint LEFT cosets in U_v of the same subgroups, indices d_j = q_j n_j/g_vj (WV LF34; S56W erratum v2 m6) | T subset S_R with \|T\| in {5,6}; \|S_R\| <= 6 since D_j avoids U_v (V4) | none (subgroups U_v cap w_jU_jw_j^-1 may coincide; allowed) | S5W/S6W; internal lemma: VFC (V2)-(V4) geometry from WV LF34 + overlay item 3 (IL8), NOT the old proof-v4/proof-k6-lemma citations of rules-k7-v1 LF46 | SUB+L |
| TS5 | S/K7-LFC-INV-v1.md LF12-14 (imports: Sun(5) 2cf02436…, Sun(6) efe1d849…, "always applied inside the subgroup U_v to at most six pieces"), LF42-43 (LFC (c): "Apply Sun(\|T\|) (imports, \|T\| <= 6) inside U_v"), erratum E3 (LF29-32); LFC verdict LF18 | Sun(5)/Sun(6) applied to 5 or 6 pieces in one left fibre C = xU_v | U_v | LEFT cosets directly: x^-1(g_jU_j cap C) = (x^-1 p_j)(U_j cap U_v) (LF39-41); no inversion | T subset S_C, \|T\| in {5,6}; \|S_C\| <= 6 (E3) | none (U_j cap U_v may coincide for different j) | S5W/S6W; no internal lemma beyond LFC's own proof (L0.1/L0.2 via S56W section 2 / E1) | SUB |
Applications to the INVERTED configuration (INV (a), E6) are again left cosets g_j^-1 U*_j of finite-index subgroups; TS4/TS5 apply
verbatim with U*_v (conjugate of U_v) as ambient group.

## 3. Instance sites (\|T\| = 5 or 6 applications that route through TS4/TS5) — no separate substitution needed
| id | site | content | route | status |
|---|---|---|---|---|
| IN1 | K7-LFC-INV-v1.md LF89-91, LF96-101; erratum E8 LF69-80 | ROW-U classes: R5 allowed sets <= 5 (Sun(6)); R24 five pieces with gcds <= 4 (Sun(5)); weights 1/min(5,k5), 1/4 for b >= 4 | TS5 at apex v (labels of unmarked neighbours have alpha-gcds) | INST; inherited by M0, ROW-1 (M1), Z2, ROW-2 (K7-35), U1, Z23-P5, D23, D23P (via ROW-2), K63-D/E (subset form, K63-D erratum v2 H5 LF28-33; K63-E erratum v3 J5 LF24-26). RICH, A1-STRUCT and the A2 files apply E8 only to <= 3 or 4 neighbours, where the Sun(5)/Sun(6) branches are vacuous (CE1 RF4 LF197-209, RF9 LF381-383; OV2 V2.1 LF26-27) |
| IN2 | K7-LFC-INV-v1.md LF142-144 (K63-U0 Step 2: five pieces with gcd 4 at d, Sun(5)) | Sun(5) at apex d | TS5 | DROP for the final chain: K63-U0 is redundant in the final K6.3 partition (R/sun7-K63RES-parent-verdict-v1.md LF18); K63-D/E cite only Step 1's subset-form weights (IN1) |
| IN3 | S/K63-E-v1.md LF25-31 (D-ROW: "no 5-set (gcds <= 4)"; p_alpha = 6: y = 1/4) | Sun(5) at apex d over the six C-pieces | TS5 (left cosets in U_d; 5-subfamily) | INST |
| IN4 | S/K63-E-erratum-v3.md LF12-15 (J3: "sets of fives size <= 5") | at a C-apex the fives lie among at most five C-neighbours, so the bound needs no Sun instance; read as a Sun(6) clause it routes through TS5 | TS5 | INST (no new requirement) |
| IN5 | S/K63-D-v1.md LF55 ("no 5-set ... gcds 3 < 4") | Sun(4)-hereditary bound | — | not a Sun(5)/(6) site (recorded) |
| IN6 | S/continuations/k63-residue/K63-RES-v1.md LF114-116 and LF140-143 (case (1c), x_* = 5: six types with pairwise gcd exactly 5, so allowed sets have at most 5 elements; y = 1/5 on all six gives 27/5 > 5); erratum v2 RESX8 LF61-73; K63RES verdict LF18 | the single load-bearing Sun(6) instance of the K6.3 branch | TS5 (row count at v: LFC of the configuration for x = alpha, of the inverted configuration for x = alpha*; left cosets; \|T\| = 6 = all six neighbours) | INST -> S6W |
| IN7 | D/K7-A1-STRUCT-v1.md LF26-30, LF84-90; OV1 A1.4 (LF87-95), A1.10 (LF169-173) | two/four class "no 5-set" [Sun(5)]; Corollary L kills 44441/44444 and y = 1/4 feasibility | TS4 (PFG-t is VFC at apex t: right cosets inverted; \|T\| = 5) | INST; the final chain consumes only Corollary L's ">= 2 fours" (Sun(2)/Sun(3)): OV1 A1.4 LF91-92, R2E LF139-142, A/K7-A2-UNIT-3-v1.md LF155-157, R/sun7-A2-unit3-parent-erratum-v1.md LF12 |
| IN8 | D/K7-D23-RICH-v1.md LF96-97 (NO5 (a) last branch, y = 1/5 on six labels: direct Sun(6)) | WITHDRAWN by mandatory erratum-1 R-1 (D/K7-D23-RICH-erratum-v1.md LF5-7, LF24-26; RICH/D23P verdict LF8) | — | DROP (no instance remains) |
| IN9 | S/continuations/k62-full-closure/K62-FULL-v1.md LF46 (LFC (c) restated, "Sun(\|T\|) inside Phi^x_v") | general allowed-set clause; FULL's direct instances are Sun(2)/Sun(3) (LF275-276) | TS5 | INST |
| IN10 | K62 E3 (K62-E3-erratum-v2.md LF60-64), DG (SH-DG erratum LF164-167), M13-A (LF15), CAP/RC (CAP-DT erratum v2 LF160-162); A2X Units (Unit 1 LF28, Unit 2 LF13, Unit 3 LF155-157); (a1) chain (R2 verdict LF46); A2-FIVE (LF35-36) | direct instances Sun(2)-Sun(4) only; Sun(5)/Sun(6) only through the packages | — | PROV (no \|T\| >= 5 instance) |

## 4. Internal-lemma sites (IL)
| id | site | old provenance | needed separately accepted written lemma | status |
|---|---|---|---|---|
| IL1 | README LF21 ("proofs in sun-coset5 rules-v1 L0"), L0.1 LF22, L0.2 LF23, L0.6 LF24 (proof inline), deletion LF25; COMP LF104 (N0) | old k5 lane rules-v1 L0 | S56W section 2 L0.1-L0.6 (LF38-48; G finite, erratum v2 m8); LFC-INV erratum E1 (LF12-19), E2 (LF21-25); used in finite G after R0 | SUB+L |
| IL2 | README LF19, LF79 (R1c); WV LF21, LF32, LF60; COMP LF46, LF108 (N4) | Prop 4.5 inside the old Sun(5) record (proof-v4 section 2) | S56W section 3 Prop 4.5 (LF67-103), via its written re-proof only (erratum v2 m5); conditions: (2r1,4r2,4r3,4r4), r's pairwise coprime, r1 odd (README LF19, LF79; COMP-U0 parent erratum item 1); ambient: the CE group (R0); four of the seven left cosets (deletion) | SUB+L |
| IL3 | rules-k7-v1 LF4 ([GEN] provenance), LF17 (L0.3 [GEN]) | old k5/k6 rule files | LFC-INV erratum E1 (LF12-19); S56W L0.3 (LF40-42) | SUB+L |
| IL4 | rules-k7-v1 LF19-24 (L1 (T) [GEN]) | label only | none: T1-T3 proved inline; accepted WV LF23, LF38 | no substitution |
| IL5 | rules-k7-v1 LF26 (L2/L3 (K) [GEN], "Proof: sun-coset5 rules-v1 L3") | old k5 rules-v1 L3 | none needed: no final-chain module imports rules-k7 K (declarations LFC-INV LF15, M1 LF10, Z2 LF15, K7-35 LF8, K63-D LF10, K63-E LF8, K63-RES LF18, RICH LF42, NO4 LF51, U1 LF25, Z23-P5 LF41, X1 candidate LF18); inside Prop 4.5 S56W's own L3/K2 (pairwise disjoint) is used | DROP |
| IL6 | rules-k7-v1 LF30 (L4 (P) [GEN], rounding as in old CERT-FORMAT-k6-v3) | old k6 format | none (RPLP/StageA/StageB only; Ppair not imported) | DROP |
| IL7 | rules-k7-v1 LF32 (L5 (F)); rules-k7-erratum-v1 LF13-18 | old k6 lemma; \|T\| = 7 frame | none (FH only; FH UNUSED, addendum LF161-169) | DROP |
| IL8 | rules-k7-v1 LF46 ((V2), (V4): "sun-coset5 proof-v4 section 5 (R2, R3)"; (V3): "sun-coset6 proof-k6-lemmas-v1 section 1(b)") | old Sun(5)/Sun(6) internal lemmas | WV LF34 fibre/inversion derivation with overlay item 3 (WV LF48): "the explicit fibre/inversion and packing proofs above supply the previously citation-only steps" | SUB+L (with TS4) |
| IL9 | rules-k7-v1 LF66-80 (Lemma CAP; "upward closed in tau as in sun-coset6 rules-k6-v1 L8 M1", LF80) | old k6 rule | none: rules-k7 CAP serves only StageA/StageB certificates; K62's CAP-C1/C2/RC (n75-n76) are proved by inline chains and the CD3 light-fibre proof | DROP |
| IL10 | rules-k7-addendum-v1 LF17 (RPLP-k7, general form of old k6 L12), LF41 (F4), LF120 (imports); LF71 (attribution remark) | old k6 L12 | none except F7 (LF56-67, proof inline; WV LF40) | DROP (F7 retained, no old lemma) |
| IL11 | K7-LFC-INV-v1.md LF47-48 ("LFC is rules-k7-v1 L5 with H = U_v") | navigation | none: LFC proved LF36-45 | PROV |
| IL12 | README LF109-111 (minimal-counterexample frame; "every group satisfies Sun(k) for k <= 6") | frame | none: unused (S56W erratum v2 m6; COMP CE-LIFT uses R0 only) | DROP |

## 5. K5.2* / KII sites (KS) and composition sites
| id | site | old citation | replacement | conditions checked | status |
|---|---|---|---|---|---|
| KS1 | S/continuations/sun7-composition/SUN7-COMP-v1.md LF53 (class row "KII, K5.2*": StageB fd14952c… LF5 "with the D2' case") | StageB, computer-assisted | **K5.2*:** K52W. README LF94 (a <= 1, \|C\| = 5, D = {d1,d2} subset (A2 \ A3) cap E, C cap E = {i*}; gcds C-C 6, d1-d2 4, d-i* 4, d-(C \ i*) 2) is K52W's literal scope: verdict LF9 ("README LF94's K5.2* gcd matrix ... all admissible valuations/cofactors and absent/present marker placements remain"); K52-W Lemma SHAPE LF25-39 (both directions; LF39 "Hence a <= 1 and all the README line-94 conditions hold"). **KII:** KIIW. README LF96 (a = 2, R1(7)(II)) lies inside the verdict's scope LF5 ("all pairwise index gcds <= 6 and exactly two indices divisible by 5"; KII-W LF19-22, SHAPE LF37-53) | ambient: arbitrary group (both verdicts), applied to the CE; seven left cosets; no deletion; all exponents/cofactors/markers. The D2' case is NOT covered by K52W (verdict LF9) and is removed BEFORE the K5.2* leaf by written D2' (rules-k7-v1 LF58-61; n30) in COVER (COMP LF44) | SUB |
| KS2 | COMP LF91 ("KII and K5.2*: impossible by StageB") | StageB | "KII: KIIW; K5.2*: K52W (the D2' case was removed in COVER)" | as KS1 | SUB |
| KS3 | COMP LF112 (node C1 StageB; one checker; F-1) | StageB | nodes K52W (ELEM, Zhu Sun(4), R0, README definitions; own FC24/INV) and KIIW (ELEM, Zhu Sun(3), R0, README definitions; own FC23/INV); computation: none | historical StageB verdict and F-1 unchanged (gate record LF45) | SUB |
| KS4 | COMP LF9-10, LF88, LF120, LF125-131, LF142, LF150-152 and erratum v2 Q1-Q4 (status/boundary sentences naming StageB, Sun(5), Sun(6) as computer-assisted load-bearing nodes) | historical statuses | restated only in a dated status section of a new version (SUN7-COMP-erratum-v3.md section S); gate decisions are the parent's (R/sun7-gates-after-written56-and-A2X-parent-v1.json LF12-46) | old text not edited | SUB (status text, new version) |
| KS5 | other StageB citations in load-bearing texts | — | none found (only the COMP files and old review packages/indices cite fd14952c) | — | none |
| CS1 | COMP LF36 / LF38 (case-tree rows citing Sun(6) / Sun(5)) | as TS1 / TS2 | S6W / S5W | as TS1 / TS2 | SUB |
| CS2 | COMP LF46 (R1c "Sun(3) + Prop 4.5"), LF108 (N4) | Prop 4.5 in proof-v4 | S56W section 3 | IL2 | SUB+L |
| CS3 | COMP LF104 (N0 "imports nothing"; README L0) | old L0 proofs | elementary root n01 (S56W section 2) | IL1 | SUB+L |
| CS4 | COMP LF106-107 (N2 Sun(5), N3 Sun(6); computer-assisted; minimal frame internal to N2) | old records | S5W (n14), S6W (n15) | TS1-TS5 | SUB |
| CS5 | COMP LF109 (N5 "written rules: VFC, T/K/P, RPLP, CAP, D2, D2'; X1 bridge") | mixed | narrowed to VFC (n05, n17), T (n07), F7 (n08), D2 (n29), D2' (n30), BRIDGE-X1 (n32); K, P, RPLP, CAP DROP (IL5, IL6, IL9, IL10) | — | SUB (narrowing) |
| CS6 | COMP LF110-111 (N6 load-bearing N2/N3; N7 LFC with Sun(t), t <= 6) | old records | TS1, TS2, TS5 | — | SUB |
| CS7 | COMP LF115 (C4: N3 load-bearing in K63-RES; read LF18 per COMP-U0 erratum item 3) | Sun(6) | S6W through TS5 (IN6) | IN6 | SUB |
| CS8 | COMP LF126-129 (computation-boundary list for N2/N3) | old records | see KS4 | — | SUB (status text) |

## 6. Provenance-only sentences (PROV; examined, nothing replaced)
LFC verdict LF33; K62-E3-v1 LF11 and erratum v2 Z1 LF60-64; SH-DG erratum S1 LF54-58 and G1 LF164-168; CAP-DT erratum v1
LF591-598, erratum v2 LF160-162, LF279; M13-A LF15-16; K62-FULL LF54, LF275-277, FULL erratum LF26-27, FULL parent erratum v2
LF7; K63-RES LF17; A1-STRUCT LF17-19 with OV1 A1.4 (LF87-95); TC LF18 with OV1 TC.2 (LF242-244); A2-FIVE LF35-36 with OV1
LF498-511, LF780-782; RICH LF39-40 with CE1 RF9 (LF374-383, LF412-422); D23P CE1 P3b (LF565-576); K7-D23-NO4 LF50-51; Z2 LF15-16
with G6 (LF49-53); M1 LF10; K7-35 LF8; K63-D LF10; U1 LF22; Z23-P5 LF40; NF LF139-141; A2 Units (LF28-29; LF13-14; LF155-157)
and unit 3 parent erratum LF12; R2E LF12-14, LF52-53; K7-A2-SCOPE LF37-38; README LF99-101. Each records the import closure
at its date; the final composition restates the closure with S5W/S6W through TS1-TS5 and leaves these texts unchanged.

## 7. Gap list and non-claims
**Genuine gaps found at the statement-substitution level: none** (CANDIDATE finding for review, not a certification). Every
load-bearing old Sun(5)/Sun(6)/K5.2*/KII citation is either replaced by an accepted written statement at a checked site
(TS1-TS5, KS1-KS3, CS1-CS8), routed through such a site (IN1, IN3, IN4, IN6, IN7, IN9), replaced by a separately accepted
written lemma (IL1-IL3, IL8), or outside the final proof-use closure (IN2, IN8, IL5-IL7, IL9, IL10, IL12). Open dependencies
outside this file: review of CUT-v3 (parts A/B), the second-family disposition of CUT-v2 M12, the COMP-U0 metadata overlay,
and the final composition review. Not claimed: full Sun(7); acceptance of anything; computation-freeness of historical
records; novelty, Lean, human review or runtime authority.
