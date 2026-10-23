# LEDGER-v1 — closed interface ledger, explicit closed module graph and Sun(5)/Sun(6) site bindings for the written Sun(7) composition [bookkeeping only; CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read at 2026-10-20T00:42:49-0700, immediately before this exclusive create. Owner SunM13MixedFibres, math-1.
- **Frozen scope:** `LEDGER-SCOPE-v1.md` (this directory) 6f1a4fefcea0b5beec763f051191b97a2348cea907742eb2e5613a611c64803c, written 00:23:33 before any input was read.
- **Authority:** TR = `RUN/control/written-sun7-closed-interface-ledger-transition-v1.json` 50ba9d9c2aec544983a246bd435221b6d7a74a608fc81d320fa2af7d9a948cd1 (target LF68).
- **Repairs:** final review MAJOR M1 (FR LF7-27; FD LF24-26). Section 3 REPLACES the numbered-order assertion at C LF62
  ("01-17,24,RW,18-23,25-79"); that assertion and its CUT-v3 node numbers are not used anywhere below.
- **Rule.** Bookkeeping only. Every row cites the census line that lists the interface as live, the literal statement/
  scope lines, the governing correction and the discharge. No theorem is re-derived; no mathematical claim or premise is
  added. Every row and every graph edge is CANDIDATE_UNVERIFIED. Full Sun(7) UNACCEPTED; nothing here is an acceptance.
- **Metadata check (hash/byte only):** every pinned input of TR re-hashed to its pin; all 117 (path, sha256) source entries of
  the five census groups in IDX re-hash to the current files (0 mismatches), so each census read exactly today's bytes.

## 0. Keys
Roots: RUN = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h; R = RUN/review; R16 = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review;
O16 = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7; S = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7;
D = S/continuations/k7-k62-residue; K = S/continuations/k63-residue/k62-followon; A = S/continuations/k7-a2-closure. Full paths and full sha256 of
every key are in the part manifests.
| key | file (sha256 prefix) |
|---|---|
| C, CE | R/sun7-complete-written-composition-candidate-v1.md (9f7a60c2); -erratum-v1.md (00b9749d) |
| FR, FD | R/sun7-FINAL-COMPOSITION-codex-v1.prompt.stdout.txt (e12c4c80); -first-family-parent-disposition-v1.json (b1466297) |
| CR, CW, CH, CA, CK | census outputs R/sun7-CENSUS-{ROOTS, ROWS-K63, RICH-A1, R2-A2, K62}-codex-v1.prompt.stdout.txt (18e12f90, fc258a63, 702aacb1, c33c441d, 27485e5f) |
| DR, DW, DH, DA, DK | the matching R/sun7-CENSUS-*-parent-disposition-v1.json (7b9a3c55, 8d8e74e4, 94427a59, 480b8575, 4eb3887a) |
| IDX, RW | R/sun7-source-body-census-index-v1.json (3700b22a); R/sun7-positive-written-rule-envelope-candidate-v1.md (a6272c5b) |
| RM, RK7, ADD, RKE, WV | O16/README.md (2a6d6d6e); O16/rules-k7-v1.md (77b9afec); O16/rules-k7-addendum-v1.md (fb2c306b); O16/rules-k7-erratum-v1.md (75a61776); R16/sun-coset7-written-parent-verdict-v1.md (73a25ba6) |
| S56, S56V | S/continuations/sun56-written-composition/S56W-v1.md (9dfa360e); R/sun56-S56W-parent-verdict-v1.md (63baa72b) |
| C5, C56, K52, KII | S/continuations/core5-written-bridge/C5W-v1.md (2e4b42b2); .../core6-written-bridge/C56W-v1.md (63cbcdb1); .../k52-written/K52-W-v1.md (c9c5ecbf); .../kii-written/KII-W-v1.md (b25d4274) |
| K52V, KIIV | R/sun7-K52W-parent-verdict-v1.md (66df666e); R/sun7-KIIW-parent-verdict-v1.md (6e907403) |
| X1C, X1L, X1V | R/x1-written-parent-candidate-v1.md (09948b0c); its clarification-v1 (49f956b2); R/x1-written-parent-verdict-v1.md (84d7d8ab) |
| L, LE, LFCV | S/K7-LFC-INV-v1.md (45be9162); S/K7-LFC-INV-erratum-v1.md (7af9acf0); R/sun7-lfc-inv-parent-verdict-v1.md (8621e744) |
| M/ME, Z/ZE, H/H1/H2 | S/K7-M1-v1.md / -erratum-v1; S/K7-Z2-v1.md / -erratum-v1; S/K7-35-v1.md / -erratum-v1 / -erratum-v2 |
| U/UE, P/PE, N, NFV | D/K7-U1-v1.md / -erratum-v1; D/K7-Z23-P5-v1.md / -erratum-v1; S/continuations/k7-complement-f/K7-NF-v1.md (734613fd); R/sun7-K7-NF-parent-verdict-v1.md (dc92a745) |
| KD/KD2, KE/KE3, KR/KR2, RPE | S/K63-D-v1.md / -erratum-v2; S/K63-E-v1.md / -erratum-v3; S/continuations/k63-residue/K63-RES-v1.md (1542a551) / -erratum-v2 (c31d7623); R/sun7-K63RES-parent-erratum-v1.md (3594dd19) |
| DEV, RESV | R/sun7-K63DE-K735-parent-verdict-v1.md (1a1c6390); R/sun7-K63RES-parent-verdict-v1.md (5ac59529) |
| NO4, RICH, R1E, CE1, D23P | D/K7-D23-NO4-v1.md; D/K7-D23-RICH-v1.md (ba32d282); D/K7-D23-RICH-erratum-v1.md; D/K7-D23RICH-D23P-erratum-v1.md (55cb66ca); D/K7-D23P-v1.md (89739dc2) |
| A1S, TC, A22, OV1, OV2 | D/K7-A1-STRUCT-v1.md; D/K7-TC-v1.md; D/K7-TC-A22-v1.md; D/K7-A1-A2-delta-erratum-v1.md (0e477743); -v2.md (9580ef79) |
| RDV, D23V, A12V, A12C | R/sun7-K7-D23RICH-D23P-parent-verdict-v1.md (1167bc4f); R/sun7-D23-parent-verdict-v1.md (d3453de1); R/sun7-K7-A1-A2-repairs-parent-verdict-v1.md (2a7c5b6c); its parent erratum-v1 (2fab0aec) |
| K23, CELL, EC, R2E, R2V | D/K7-CASEA-K23-v1.md; D/K7-CELL-v1.md; D/K7-R2-R3-consolidated-erratum-v1.md; D/K7-R2-repair-erratum-v1.md (3bd5474d); R/sun7-K7-R2-parent-verdict-v1.md (9b0f7df5) |
| F5, U1A, U2A, U3A, A2XV | D/K7-A2-FIVE-v1.md (93fd95d7); A/K7-A2-UNIT-1/2/3-v1.md; R/sun7-A2X-parent-verdict-v1.md (9ad41f21) |
| E3, E3E2, DG, SD, M13, CAP, CD1 | K/K62-E3-v1.md; K/K62-E3-erratum-v2.md; K/K62-DG-v1.md; K/K62-SH-DG-erratum-v1.md (755edc21); K/K62-M13-A-v1.md; K/K62-CAP-v1.md; K/K62-CAP-DT-erratum-v1.md (996f924c) |
| FULL, FP2, FULLV | S/continuations/k62-full-closure/K62-FULL-v1.md (fabf04dd); R/sun7-K62-FULL-parent-erratum-v2.md; R/sun7-K62-FULL-parent-verdict-v1.md (f3b22e53) |
| E3V, SDV, M13V, CAPV | R/sun7-K62E3-parent-verdict-v1.md (576969dd); R/sun7-K62-SH-DG-parent-verdict-v1.md (cae455c3); R/sun7-K62-M13-parent-verdict-v1.md (2fac7a30); R/sun7-K62-CAP-DT-parent-verdict-v1.md (84061c6f) |
Discharge codes: **[B:g]** proof body lies in census group g (CR/CW/CH/CA/CK; the cited census line gives that census's
verdict on the body); **[Z]** permitted classical Zhu Sun(3)/Sun(4); **[S5W@s]/[S6W@s]** statement substitution at site s of
section 4; **[FR]** checked only by the first-family final review. "LFk-m" are one-based physical lines of the named file.

## 1. Nodes: retained modules, exported statement, proof body with governing corrections, census coverage
| node | exported statement (literal LF) | proof body; governing corrections in reading order | census coverage |
|---|---|---|---|
| N01 ZHU | Sun(3), Sun(4) in every group (Zhu, arXiv:0807.2207 Thm 1.1: RM LF15; WV LF60) | external classical import; not re-proved in this run (S56V LF10) | permitted import (TR LF68 (1)(b)); no census |
| N02 ELEM | L0.1-L0.6 (L0.6 = Sun(2)), L1-L3, K2 (pairwise disjoint), deletion (RM LF21-25; S56 LF34-65) | S56 LF34-65 (S56 parent erratum v1 item 1; v2 m8); LE E1 LF12-19, E2 LF21-25 | CR LF15, LF64; CW LF32, LF143 |
| N03 R0 | finite-core quotient preserving indices, intersection indices, disjointness, conjugated intersections (RM LF27-29; LFCV LF23) | RM LF29; S56 LF143-147 | CR LF11, LF44; CW LF142 |
| N04 C5W | Core(5) for every finite group (C5 LF110-120) | C5 LF1-150 with sun5-C5W-parent-erratum-v1 | CR LF16, LF45 |
| N05 C56W | Core5(6) for every finite group (C56 LF109-119) | C56 LF1-141 with sun6-C56W parent errata v1, v2 | CR LF17, LF46 |
| N06 P45 | Prop 4.5 (S56 LF68-69) | S56 LF70-103 (erratum v2 m5: qualifies only through this re-proof) | CR LF15, LF63 |
| N07 S5W | S56 LF17-20; S56V LF7, LF10 | S56 LF105-120 (Lemma R1, Theorem S5W) with S56 errata v1, v2 | CR LF15, LF47; DR LF19 |
| N08 S6W | S56 LF21-25; S56V LF8, LF10 | S56 LF122-141 (Lemma R1(6), Theorem S6W; optional S5W route LF140-141) | CR LF15, LF47 |
| N09 T | L1 (T1)-(T3), tau_min/tau_max (RK7 LF19-24) | inline RK7 LF20-24; WV LF23, LF38 | CR LF12, LF51 |
| N10 F7 | forced containment (ADD LF56-60) | ADD LF62-67 (actual tau; no LF80 clause) | CR LF13, LF70 |
| N11 VFC | (V1)-(V4) and VFC-count (RK7 LF40-49) | RK7 LF46, LF49; WV LF34 with overlay item 3 (WV LF48) for (V2)-(V4) | CR LF12, LF67 |
| N12 LFC | LFC (a)-(d) (L LF18-34) | L LF36-45; LE E1-E3 LF12-32 | CW LF31-32, LF73 |
| N13 INV | INV (a)-(b) (L LF52-71); q = alpha* (LE E7 LF56-59) | L LF52-75; LE E6-E7 LF47-63 | CW LF74 |
| N14 ROWU | ROW-U (i)-(iii) and standard weights (L LF79-101); E8 value bound (LE LF69-80); ROW-U-deg transfer (ME F3 LF24-32) | L LF85-109; LE E8; ME F3 | CW LF75 |
| N15 DEF | CE, P0, P1, gcd matrices, six class definitions (RM LF33-52, LF67, LF85-96; WV LF18-21, overlay A-1 LF46) | RM LF42, LF52 | CR LF11 |
| N16 RW | positive envelope: T, K/K1/K2, P, VFC, RPLP incl. F7, CAP gcd-capping (RW LF10-23) | RK7 LF19-80; ADD LF17-159; RKE W1-W2; WV LF23, LF38-42, items 4-5 LF49-50 | CR LF30, LF51 (section 5 placement superseded by section 3 here) |
| N17 R1(7) | RM LF56-58 | RM LF60-65 | CR LF44 |
| N18 R1a, N19 R1b | RM LF71; RM LF73 | inline | CR LF11 |
| N20 R1c | RM LF75-79 | inline, with Prop 4.5 | CR LF44, LF63 |
| N21 D2, N22 D2' | RM LF82-83; RK7 LF55-56, LF58-61 | RK7 LF55-61; WV LF36 (overlay item 2 LF47: rules section 3) | CR LF68 |
| N23 COVER | six classes K7, K6.2*, K6.3, K5.2*, K5.3, KII (RM LF85-103; WV LF20-21; C LF14) | RM LF54-103; C LF36-43 | CR LF11, LF44; FR LF34-35 |
| N24 X1 | X1V LF5 | X1C LF20-34 with X1V overlays LF19-20 and X1L LF1-7 | CR LF27-29, LF50, LF80 |
| N25 K53B | K5.3 contains the X1 tuple (WV LF24) | ADD LF159; C LF29 | CR LF50; FR LF38 |
| N26 K52W | exact RM LF94 matrix (K52V LF9) | K52 LF1-206 with sun7-K52W-parent-erratum-v1 | CR LF18, LF48 |
| N27 KIIW | all gcds <= 6, exactly two 5-divisible indices (KIIV LF5) | KII LF1-192 with sun7-KIIW-parent-erratum-v1 | CR LF19, LF49 |
| N28 M0 | L LF113-114 | L LF116-121 | CW LF76 |
| N29 U0 | K63-U0 (L LF131-133, R0 lift LE E5) and its Step 1 subset form (KD2 H5 LF28-33; KE3 J5 LF24-26) | L LF135-144 | CW LF77, LF112 |
| N30 ROW1 | ROW-1 (a)-(c) (M LF22-52) | M LF24-52 with ME F2-F5 LF17-43 | CW LF78 |
| N31 M1 | K7-M1 (M LF56-57) | M LF56-74; ME F1, F6 | CW LF79 |
| N32 Z2 | K7-Z2 (Z LF20-24); ROW-1-deg transfer (ZE G2 LF18-25) | Z LF18-102 with ZE G1-G10 | CW LF80-81 |
| N33 K735 | K7-35 and ROW-2 (H LF13-18, LF20-54) | H LF20-82; H1 K1; H2 K2-K4 | CW LF82-83 |
| N34 U1 | K7-U1 (U LF158) | U LF28-181 with UE E-1..E-6 | CW LF84-85 |
| N35 ZP5 | Z23-P5 (P LF10-20) | P LF44-217 with PE P-1..P-6 | CW LF86-87 |
| N36 NF | K7-NF (N LF83-86; NFV LF11) | N LF22-111 with the NF parent errata v1-v3 (R/sun7-K7-NF-parent-erratum-v1/v2/v3.md) | CW LF88-90 |
| N37 K63D, N38 K63E | DEV LF9, LF10 | KD LF24-96 (+D errata v1, v2); KE LF23-73 (+E errata v1-v3) | CW LF92-95 |
| N39 K63RES | RESV LF5 | KR LF21-194 with R errata v1, v2 (X1-X8); RPE LF5 | CW LF96-101; RPE: FR LF43 only |
| N40 NO4 | D23-CENTER, D23-MIX (D23V LF5-8) | NO4 LF54-154 with NO4 erratum X-1..X-13 | CH LF19-20, LF39-40 |
| N41 RICH | RDV LF9-10 | RICH LF50-246; R1E R-1 LF15-26; CE1 RF1-RF9; A12C LF5 (section 6 locator) | CH LF21-23, LF41-46 |
| N42 D23P | RDV LF12-13 | D23P LF48-112; CE1 PF1-PF3 LF425-577 | CH LF24, LF47 |
| N43 A1S | A12V LF26 | A1S LF21-133; OV1 A1.1-A1.13 as amended by OV2 | CH LF25, LF48-50 |
| N44 TC | A12V LF27-30 | TC LF22-88; OV1 TC.1-TC.14; OV2 V2.2-V2.4, V2.8 | CH LF26, LF51-53 |
| N45 A22 | A12V LF31 | A22 LF10-55; OV1 A22.1-A22.5 | CH LF27, LF54 |
| N46 K23 | R2V LF12-14 | K23 LF16-154; then K23E; EC R2.1 (amended by R2E E1), R2.2; R2E E3-E13 (R2V LF31) | CA LF21-22, LF71-72 |
| N47 CELL | R2V LF15-16 | CELL LF15-131; CELLE (C.1 by EC R2.4, C.2 by R2E E2); EC R2.3; R2E E14-E24 (R2V LF31) | CA LF23-26, LF73-74 |
| N48 A1CL | (a1) closure (R2V LF5, LF9, LF17) | R2V LF17; CELL LF135-138 | CA LF28; FR LF41 |
| N49 A2F | A12V LF33-37 (Lemma F, FG-a2, Cor 5/6-a2, D23-a2, ZT5 S1-S5, BRIDGE A2.10, TRANSFER) | F5 LF38-203; OV1 A2.1-A2.17; OV2 V2.5-V2.7; A12C LF5 | CA LF13, LF67-70; CH LF55 |
| N50 UN1, N51 UN2 | A2XV LF13, LF14 | U1A LF8-201 with U1E; U2A LF7-152 with U2E1 (items 1, 3-7) and U2E2 | CA LF14-15, LF17-19, LF75-78 |
| N52 A2X | A2XV LF9 | U3A LF47-148 with U3E; A2XV LF15-17 | CA LF16, LF20, LF79-82 |
| N53 E3 | E3V LF5 | E3 LF22-105; E3 erratum v1 (F2 only); E3E2 Z1-Z12 (supersedes F1, F3) | CK LF11-13, LF37-41 |
| N54 SH1 | SH-1 argument only (SDV LF16) | SD S2 LF62-80 | CK LF16, LF42; IDX LF1160 |
| N55 DG | SDV LF17-23 (conditional Theorem DG) | DG LF20-61; DG erratum v1 (in force); SD G1-G8 (L1/VFC citations withdrawn) | CK LF14-16, LF44-48 |
| N56 M13A | M13V LF13-14 (items 1-2) | M13 LF32-107; M13 parent erratum (status only for A) | CK LF20-21, LF53-55 |
| N57 CAP62 | CAPV LF23-25 | CAP LF35-90; CD1 CD1-CD3; CAP-DT erratum v2 V1-V14; CD1 CD4-CD7 NOT in snapshot (RES-1) | CK LF17-19, LF49-52; IDX LF1159 |
| N58 FULL | K62X: whole K6.2* (FULLV LF9, LF11) | FULL LF69-252 with K62-FULL-erratum-v1, parent provenance erratum, parent errata v1, v2 | CK LF22-26, LF56-63 |
| N59 FINAL | Sun(7) for every group (C LF6) | C LF24-34, LF36-44 with CE LF5 | FR LF3, LF31-41 [FR] |

## 2. Closed interface ledger (every live incoming interface listed by C and by the five census reviews)
Columns: row | listed live at | interface: exact statement / scope (literal LF) | governing correction | consumer nodes | discharge.

### 2.1 Final candidate (C LF11-22 inputs; C LF29, LF32 steps; C LF49-57 cutover)
| row | listed at | interface and scope | correction | consumers | discharge |
|---|---|---|---|---|---|
| F01 | C LF11 | R0 and elementary product/index/coset/Sun(2) facts | S56 erratum v2 m8 | N03-N59 | [B:CR] N02, N03 (CR LF44, LF64) |
| F02 | C LF12 | Zhu Sun(3)/Sun(4), three/four disjoint left cosets, every group | - | N04, N05, N07, N08, N11, N12, N18, N19, N21, N22, N26, N27, N47, N50-N53, N58 | [Z] N01 |
| F03 | C LF13 | S5W/S6W: every group, 5/6 disjoint LEFT cosets, equal subgroups allowed | S56 errata v1-v2 (m3, m4, m6) | sites S1-S12 (section 4) | [B:CR] N07, N08 from N04, N05 (CR LF47; S56V LF5-10) |
| F04 | C LF14, LF36-44 | COVER: finite CE with all gcds <= 6 lies in K7, K6.2*, K6.3, K5.2*, K5.3, KII; every such configuration (no least order) | WV items 1-3 (LF46-48) | N59 | [B:CR] N23 (CR LF11, LF44, LF68); FR LF34-35 |
| F05 | C LF15 | X1: (3r1,3r2,6r3,6r4,6r5), r1, r2 odd, all pairwise coprime | X1V LF19-20 | N59 via N25 | [B:CR] N24 (CR LF50, LF80) |
| F06 | C LF16 | K52W: exact RM LF94 matrix only, not the D2' universe | K52 parent erratum items 1-5 | N59 | [B:CR] N26 (CR LF48; K52V LF9); FR LF37 |
| F07 | C LF17 | KIIW: all gcds <= 6 and exactly two 5-divisible indices | KII parent erratum items 1-5 | N59 | [B:CR] N27 (CR LF49; KIIV LF5); FR LF36 |
| F08 | C LF18 | K63 D (f_d = 1), E (f_d >= 2, no C 2-marker), RES (f_d >= 2 with one); unbounded scope | D, E, RES errata; RPE LF5 (i* keeps 2^E) | N59 | [B:CW] N37-N39 (CW LF92-101); RPE: FR LF43 (RES-3) |
| F09 | C LF19 | K7-NF: every K7 configuration lies in F (distinct 2- and 3-marker vertices) | NF parent errata v1-v3 | N59 | [B:CW] N36 (CW LF88-89, LF123: no (a1) import) |
| F10 | C LF20 | K7(a1) excluded, R2V LF9 setting | reading order R2V LF31 | N59 | [B:CA] N48 (CA LF71-74; R2V LF17); FR LF41 |
| F11 | C LF21 | K7(a2) excluded (A2XV LF9), p retained | U1E; U2E1/U2E2; U3E | N59 | [B:CA] N52 (CA LF79-82); FR LF41 |
| F12 | C LF22 | K62X: whole K6.2* class, both orientations, FB discharges DG antecedents | FULL parent errata v1 (alpha_(d i*) = 1 for BUD-DEEP), v2 item 3 | N59 | [B:CK] N58 (CK LF56-63); FR LF40 |
| F13 | C LF29 | K5.3 to X1 deletion/cofactor bridge | - | N59 | [B:CR] N25 (CR LF50); FR LF38 |
| F14 | C LF32 | K7 split: NF, then 5-marker absent/on z/on t = (a1), on a third vertex = (a2) | - | N59 | [FR] FR LF41; uses F09-F11 |
| F15 | C LF49 | RM LF61 Sun(6) (six original cosets, all gcds 5) | - | N17 | [S6W@S1] |
| F16 | C LF50 | RM LF63 Sun(5) (every five original cosets) | - | N17 | [S5W@S2] |
| F17 | C LF51 | LFC allowed subfamilies of sizes 5/6 (incl. ROW and class calls) | LE E3 LF29-32 | N12 and LFC consumers | [S5W@S4]/[S6W@S4] |
| F18 | C LF52 | VFC/RPLP allowed subfamilies of sizes 5/6 | WV item 3 LF48 | N11 (RPLP only inside N16) | [S5W@S5]/[S6W@S5] |
| F19 | C LF53 | old elementary/L3/K2/Prop 4.5/internal fibre citations replaced by written proofs | S56 erratum v2 m5 | N02, N06, N11-N13 | [B:CR] N02, N06, N11 (WV LF34, LF38); [B:CW] N12, N13 |
| F20 | C LF54 | old K/P/RPLP/CAP non-use claims replaced by RW positive contracts | RW LF20, LF27-30 | N16 (no operative consumer, section 3) | [B:CR] N16 (CR LF30, LF51) |
| F21 | C LF55 | StageA X1, StageB K52/KII replaced by X1, K52W, KIIW | - | N59 | rows F05-F07; no operative StageA/B consumer: CR LF81, CW LF113, CH LF89, CA LF47, CK LF93 |
| F22 | C LF57 | excluded premises: seven-piece Sun in a subgroup, least-order frame, L5/FH seven-piece, old C18, blanket L8 M1, computed dual/coverage | - | all nodes | no operative use in any group: CR LF3, LF58-61, LF70, LF79; CW LF3, LF134; CH LF77-80, LF84, LF89; CA LF38-41, LF47; CK LF76-77, LF83-84, LF93. Every node of section 1 except N01 lies in one of these groups, so the union covers the operative graph (section 3 C2) |

### 2.2 ROOTS (CR claim table LF42-52, live items in LF56-83, Sun sites LF85-94, open items LF100-106)
| row | listed at | interface and scope | correction | consumers | discharge |
|---|---|---|---|---|---|
| R01 | CR LF44 | R0 (finite-core quotient; not a least-order choice) | - | N17, N23, N24, N26, N27, N59 | [B:CR] N03 |
| R02 | CR LF44, LF89 | RM LF61: six original left cosets, all gcds 5 | - | N17 | [S6W@S1] |
| R03 | CR LF44, LF90 | RM LF63: every five-subfamily | - | N17 | [S5W@S2] |
| R04 | CR LF44, LF63 | Prop 4.5 at R1c: (2r1,4r2,4r3,4r4), r's pairwise coprime, r1 odd (RM LF19, LF75-79) | S56 erratum v2 m5 | N20 | [B:CR] N06 (S56 LF67-103) |
| R05 | CR LF64 | elementary L0.1-L0.6 replacing old [GEN]/rules-v1 L0 provenance | S56 erratum v2 m8 | N03, N09-N15, N17-N27 | [B:CR] N02 (S56 LF38-48) |
| R06 | CR LF45-46 | C5W/C56W use only Sun(2) and Zhu Sun(3)/(4) | C5W, C56W errata | N04, N05 | [B:CR] N02; [Z] N01 |
| R07 | CR LF47 | H5 => S5W and H5 and H6 => S6W; unrestricted cores meet H5/H6 | S56 erratum v2 m2, m3, m7 | N07, N08 | [B:CR] N02-N06; [Z] N01 |
| R08 | CR LF48 | K52-W: FC24 (pairs, four-subsets), actual INV | K52 erratum | N26 | [B:CR] N26 (own re-proof); [Z] Sun(4) |
| R09 | CR LF49 | KII-W: FC23 (pairs, triples), actual INV | KII erratum | N27 | [B:CR] N27; [Z] Sun(3) |
| R10 | CR LF50, LF80 | X1: pairwise fibre bound (replaces LFC), T, actual INV | X1V LF19-20 | N24 | [B:CR] N24 (X1L), N09; [B:CW] N13 |
| R11 | CR LF50 | K5.3 bridge (ADD LF159) | - | N25 | [B:CR] N25 |
| R12 | CR LF65 | K: written packing proof (WV LF38, LF48) or S56 L3/K2 (LF54-61) | S56 erratum v1 item 1 | N16 only | [B:CR] N16, N02 |
| R13 | CR LF66 | P grid and rounding (WV LF38; ADD F6) | - | N16 only | [B:CR] N16 |
| R14 | CR LF67, LF91 | VFC (V2)-(V4) via WV LF34/LF48; (V3) at five/six pieces | WV item 3 | N21, N22, N32, N34, N35, N39-N47, N49-N52, N57, N58 | [B:CR] N11; Sun: [S5W/S6W@S5] |
| R15 | CR LF68 | D2, D2' (partial D3 is not retained) | WV item 2 LF47 | N23 | [B:CR] N21, N22 |
| R16 | CR LF69 | CAP gcd-capping arithmetic (RK7 LF70-76; ADD LF126-159; WV LF42) | RW LF18 | N16, N57 | [B:CR] N16 |
| R17 | CR LF70 | RK7 LF80 L8 M1 clause not retained; actual-tau T bounds and F7 suffice | RW LF28 | N10 | [B:CR] N09, N10 (ADD LF62-67) |
| R18 | CR LF71-72 | RPLP proof (ADD LF21-104); Farkas only for the closed relaxation | RKE W2; WV item 5 LF50 | N16 only | [B:CR] N16 |
| R19 | CR LF102 | FCS global negative census (K/P/RPLP DROP) | RW LF35 | - | not needed: K, P and the RPLP LP have no operative consumer outside N16 (section 3 C3); no negative census is asserted |
| R20 | CR LF103 | seven-piece/frame exclusion across other consumers | - | all | row F22 |
| R21 | CR LF104 | IN1: ROW-U inheritance | LE E8; KD2 H5; KE3 J5 | N28-N35, N37, N38, N40-N42 | rows W04, H05; site S6, S7 |
| R22 | CR LF104 | IN10: only direct Sun(2)-(4) in K62, A2 units, (a1) chain, A2-FIVE | - | N46-N58 | rows A02-A08, K03-K05; CH LF61-71; CA LF51-57; CK LF77-81 |
| R23 | CR LF104 | KS5: other StageB citations | - | - | row F21 |
| R24 | CR LF104 | PROV: import-accounting sentences | - | - | historical; the live edges are rows of this section (CW LF126, CH LF83, CA LF42-43, CK LF78-81) |
| R25 | CR LF104 | D2' consumer in COVER (K52W does not cover the D2' universe) | - | N23 | row R15; C LF42; FR LF35, LF37 |
| R26 | CR LF105 | RW's named global order | - | - | replaced by section 3 |

### 2.3 ROWS-K63 (CW live list LF140-149)
| row | listed at | interface and scope | correction | consumers | discharge |
|---|---|---|---|---|---|
| W01 | CW LF142 | R0: finite-core quotient, no minimal-counterexample argument | - | N28-N39 | [B:CR] N03 |
| W02 | CW LF143 | L0.1, Lagrange, L0.2, re-derived measure/range identities LE LF14-19 | LE E1 | N12-N14, N28-N39 | [B:CR] N02; [B:CW] LE E1 |
| W03 | CW LF144 | Sun(2)-Sun(4); theorem-level Sun(5)/Sun(6) only at the identified subgroup/piece-count scopes | - | N12, N14, N29, N37-N39 | [B:CR] N02 (Sun(2)); [Z]; [S5W/S6W@S4, S6-S9] |
| W04 | CW LF145 | LFC, INV, verified ROW transfers and subset bounds: ROW-U/E8, ROW-U-deg, ROW-1, ROW-1-deg (ZE G2), ROW-2, H5/J5 subset form | LE E1-E8; ME F2-F5; ZE G2; H1, H2; KD2 H5; KE3 J5 | N28-N35, N37-N40, N42 | [B:CW] N12-N14, N29, N30, N32, N33 |
| W05 | CW LF146 | T: triple bounds on actual configurations and their inverses | ZE G5 | N32, N34, N35 | [B:CR] N09 |
| W06 | CW LF147 | VFC V1-V4 and weighted count | KR2 X2 | N32, N34, N35, N39 | [B:CR] N11 |
| W07 | CW LF148 | F7 at the explicitly checked inequalities | - | N32, N34, N35 | [B:CR] N10 |
| W08 | CW LF149 | (a1) closure, only for K7-REM | - | none retained: K7-REM (N LF120-133) is not a node; C LF32 joins N36, N48, N52 directly | not an edge; N48 is discharged by F10 |

### 2.4 RICH-A1 (CH live list LF96-110; Sun accounting LF59-71)
| row | listed at | interface and scope | correction | consumers | discharge |
|---|---|---|---|---|---|
| H01 | CH LF96 | K7 and marker placement: n_i = 6r_i, pairwise coprime r_i; (a1) five unmarked W; D23P (a2) four unmarked and a separate 5-vertex; unbounded exponents | - | N40-N45 | [B:CR] N15 (RM LF91); RDV LF9-13 |
| H02 | CH LF98 | R0, L0.1/L0.3, Lagrange, INV (markers preserved, involution), 1 <= x <= 5, alpha + alpha* <= 6 | LE E1, E6, E7 | N40-N45 | [B:CR] N02, N03; [B:CW] N13 |
| H03 | CH LF100 | LFC/VFC: fibre multiplicities, allowed sets, feasible-weight inequality, VFC masses and local indices, strict union avoidance | LE E3; WV item 3 | N40-N45 | [B:CW] N12; [B:CR] N11 |
| H04 | CH LF102 | T and F7, either orientation; no computed RPLP result | - | N40-N45 (F7: N40, N42) | [B:CR] N09, N10 |
| H05 | CH LF104 | ROW-1 (odd {3,5}-smooth neighbour, degree transfer); ROW-2 local gcd-matrix transfer (CE1 P1) | ME F2-F5; ZE G2; CE1 PF1 | N40 (ROW-1), N42 (ROW-2) | [B:CW] N30, N32, N33; CE1 PF1 inside N42 [B:CH] |
| H06 | CH LF106 | corrected RICH: FG7 (a1) auxiliary scope, Cor 5/6 with equality, NO5/R3/TR/CC/TZ/LZ at stated hypotheses; CC needs separation, PFG-t needs connectivity | R1E R-1; CE1 RF1-RF9 | N43-N47, N49 | [B:CH] N41 |
| H07 | CH LF108 | TC prerequisites: R1 at E = 1 (OV1 TC.4), FG-V (OV1 TC.7); R3-R5 keep E >= 2 | OV1 TC.4, TC.7; OV2 V2.3 | N44-N47 | [B:CH] N44 |
| H08 | CH LF110 | A2 transfer restrictions: (a2-no5), actual parameters <= 4, restricted auxiliary chain, actual VFC q, D23-a2 for D23-MIX, beta_zu <= 3 for FG-a2(b) | OV1 A2.10-A2.17; OV2 V2.5-V2.7; A12C LF5 | N49, N52 | [B:CH] OV1/OV2 (CH LF55); [B:CA] N49 (CA LF67-70) |

### 2.5 R2-A2 (CA live list LF94-103)
| row | listed at | interface and scope | correction | consumers | discharge |
|---|---|---|---|---|---|
| A01 | CA LF96 | R0, L0.1-L0.3, Lagrange, preserved under finite reduction | - | N46-N52 | [B:CR] N02, N03 |
| A02 | CA LF97 | LFC/INV with overlays; actual inversion keeps labelled indices and markers | LE E1-E8 | N46-N52 | [B:CW] N12, N13 |
| A03 | CA LF98 | VFC and L1 at literal scopes | WV item 3 | N46-N52 | [B:CR] N11, N09 |
| A04 | CA LF99 | D23P/RICH data, granularity/equality conclusions | CE1 | N46, N47, N49, N52 | [B:CH] N41, N42 |
| A05 | CA LF100 | F, FG-a2, D23-a2, S1-S5; restricted BRIDGE/TRANSFER | OV1 A2 items; OV2 V2.5-V2.7 | N51, N52 | [B:CA] N49; [B:CH] OV1/OV2 (CH LF55) |
| A06 | CA LF101 | (a1) inputs A1-STRUCT/TC/TC-A22, not extended to a third marked vertex | OV1, OV2 | N46-N48 | [B:CH] N43-N45 |
| A07 | CA LF102 | U1 conditional statements; U2 normalised-S statements; consumer hypotheses checked | U1E; U2E1 (1, 3-7); U2E2 | N52 | [B:CA] N50, N51 |
| A08 | CA LF103, LF105 | historical Sun(5)/Sun(6) theorem imports | - | through N11, N12, N14, N43, N49 | [S5W/S6W@S4, S5, S6]; Corollary L [S5W@S10-S12] (CA LF59 defers CorL to RICH-A1: CH LF67-69) |

### 2.6 K62 (CK live list LF105-112)
| row | listed at | interface and scope | correction | consumers | discharge |
|---|---|---|---|---|---|
| K01 | CK LF107 | K6.2* index/marker/cofactor conditions; R0; L0.1/Lagrange; E1 | - | N53-N58 | [B:CR] N15, N03, N02; [B:CW] LE E1 |
| K02 | CK LF108 | actual inversion: class preserved, families exchanged, alpha + alpha* <= g | LE E6, E7 | N53-N58 | [B:CW] N13 |
| K03 | CK LF109 | LFC and VFC at local scopes (at most six other pieces), with theorem-level Sun(5)/(6) provenance | - | N53-N58 | [B:CW] N12; [B:CR] N11; [S5W/S6W@S4, S5] (generic; no direct five/six-piece use: CK LF77-81) |
| K04 | CK LF110 | corrected E3; conditional DG; SH-1 written disjointness | E3 erratum v1 F2; E3E2 Z1-Z12 (supersede F1/F3); DG erratum v1; SD G1-G8 (L1/VFC withdrawn); SD S2 | N55, N56, N58 | [B:CK] N53, N54, N55 |
| K05 | CK LF111 | M13-A DG*/C2* in (1,3); DG* keeps its own four-subset hypothesis | M13 parent erratum (status only) | N58 | [B:CK] N56 |
| K06 | CK LF112 | CAP/RC: finite representation, C1/C2, RC-O/RC-i*, conditional transfer | CD1 CD1-CD3; CAP-DT erratum v2 V1-V14 | none operative (FULL LF67 with FP2 LF7; CK LF91-92) | [B:CK] N57 (documentary envelope); RES-1 |

## 3. Explicit closed module graph (replaces C LF62's numbered order)
Nodes are those of section 1. "Nx <- inputs" lists every incoming edge, each justified by the module's own import
declaration (cited) and by the ledger rows named. The listing order N01 < N02 < ... < N59 is an acyclic order: every
input of every node has a smaller number (checked row by row below). Edges marked (cons.) are conservative extras.
| node | inputs (edges) | declared at | rows |
|---|---|---|---|
| N01 ZHU | - (external) | RM LF15 | F02 |
| N02 ELEM | - | S56 LF35-37 | F01, R05 |
| N03 R0 | N02 | RM LF29; S56 LF144-147 | F01, R01 |
| N04 C5W | N01, N02 | C5 LF22-30 | R06 |
| N05 C56W | N01, N02 | C56 LF23-31 | R06 |
| N06 P45 | N02, N03 | S56 LF154 | R04 |
| N07 S5W | N01, N02, N03, N04, N06 | S56 LF157, LF159 | F03, R07 |
| N08 S6W | N01, N02, N03, N04, N05, N06; N07 (cons., optional route S3) | S56 LF158, LF160 | F03, R07 |
| N09 T | N02 | RK7 LF19-24 | R17 |
| N10 F7 | N09 | ADD LF62-67 | R17, W07 |
| N11 VFC | N01, N02, N07, N08 | RK7 LF40-46; WV LF34 | R14, F18 |
| N12 LFC | N01, N02, N07, N08 | L LF12-14 | F17, W04 |
| N13 INV | N02, N03, N11 | L LF52-71; LE E7 LF56-59; LFCV LF19, LF23 | W04, K02 |
| N14 ROWU | N12 | L LF85-92; LE E8 | W04, R21 |
| N15 DEF | N02 | RM LF33-52 | H01, K01 |
| N16 RW | N01, N02, N07, N08, N09, N10, N11, N15 | RW LF6-23 | F20, R12-R13, R16, R18 |
| N17 R1(7) | N02, N07, N08, N15 | RM LF60-65 | R02, R03 |
| N18 R1a | N01, N15 | RM LF71 | F02 |
| N19 R1b | N01, N15 | RM LF73 | F02 |
| N20 R1c | N02, N06, N15, N19 | RM LF75-79 | R04 |
| N21 D2 | N01, N11, N15 | RK7 LF55-56; WV LF36 | R15 |
| N22 D2' | N01, N02, N11, N15, N19 | RK7 LF58-61; WV LF36 | R15, R25 |
| N23 COVER | N03, N15, N17, N18, N19, N20, N21, N22 | RM LF85-103; C LF38-43 | F04 |
| N24 X1 | N02, N03, N09, N13 | X1C LF12-18 with X1V LF19-20 | R10 |
| N25 K53B | N02, N15 | ADD LF159; C LF29 | R11, F13 |
| N26 K52W | N01, N02, N03, N15 | K52 LF45-56 | R08 |
| N27 KIIW | N01, N02, N03, N15 | KII LF24-35 | R09 |
| N28 M0 | N03, N13, N14 | L LF116-121 | W04 |
| N29 U0 | N02, N03, N12, N14, N15 | L LF135-144; LE E5 | W04, R21 |
| N30 ROW1 | N02, N12, N14 | M LF7-11; ME F1 LF10-15 | W04, H05 |
| N31 M1 | N02, N03, N12, N13, N14, N30 | M LF7-11; ME F1 | W01-W04 |
| N32 Z2 | N02, N03, N09, N10, N11, N12, N13, N14, N30 | Z LF7-16; ZE G1 LF10-16, G5 LF43-47 | W01-W07 |
| N33 K735 | N02, N03, N12, N13, N14, N30, N32 | H LF5-9; H2 K4 LF21-23 | W04, H05 |
| N34 U1 | N02, N03, N09, N10, N11, N12, N13, N14, N15 | U LF10-26 | W01-W07 |
| N35 ZP5 | N02, N03, N09, N10, N11, N12, N13, N14, N15, N30, N32 | P LF22-42 | W01-W07 |
| N36 NF | N03, N15, N28, N31, N32, N33, N34, N35 | N LF43-57; NF parent erratum v3 LF5 | F09 |
| N37 K63D | N02, N03, N12, N13, N14, N15, N29 | KD LF6-11; KD2 H5 LF28-33 | W01-W04 |
| N38 K63E | N02, N03, N12, N13, N14, N15, N29 | KE LF6-8; KE3 J5 LF24-26 | W01-W04 |
| N39 K63RES | N02, N03, N11, N12, N13, N15 | KR LF7-19 with KR2 X1 LF11-20, X2 LF22-29 | W01-W06 |
| N40 NO4 | N03, N09, N10, N11, N12, N13, N14, N15, N30, N32 | NO4 LF30-52 | H01-H05 |
| N41 RICH | N02, N03, N09, N11, N12, N13, N14, N15, N40; N32 (cons., method pointer ZE G5 at RICH LF33-34) | RICH LF21-42 | H01-H03, H06 |
| N42 D23P | N02, N03, N09, N10, N11, N12, N13, N15, N33, N40 | D23P LF24-46; CE1 P3a-P3b | H01-H05 |
| N43 A1S | N03, N07 (site S10/S11), N09, N11, N12, N13, N14, N15, N40, N41 | A1S LF10-19; OV1 A1.3-A1.4 LF65-96 | H06, A06 |
| N44 TC | N03, N09, N11, N12, N13, N15, N41, N43 | TC LF11-20 | H06, H07 |
| N45 A22 | N03, N11, N12, N13, N41, N43, N44 | A22 LF5-16 | A06 |
| N46 K23 | N02, N03, N09, N11, N12, N13, N40, N41, N43, N44, N45 | K23 LF5-14; R2E E3-E4 | A01-A04, A06 |
| N47 CELL | N01, N02, N03, N11, N12, N13, N41, N43, N44, N46 | CELL LF5-13 with R2E E15 LF360-363 | A01-A04, A06 |
| N48 A1CL | N03, N13, N41, N43, N44, N45, N46, N47 | R2V LF17; CELL LF135-138 | F10 |
| N49 A2F | N02, N03, N07 (site S12), N09, N11, N12, N13, N14, N15, N41, N42, N43, N44, N45 | F5 LF22-36; TRANSFER: OV1 A2.17 / OV2 V2.7 | H08, A05 |
| N50 UN1 | N01, N02, N03, N09, N11, N12, N13 | U1A LF24-32 | A01-A03, A07 |
| N51 UN2 | N01, N02, N03, N09, N11, N12, N13, N49 | U2A LF13-24 | A01-A03, A05, A07 |
| N52 A2X | N02, N03, N09, N11, N12, N13, N15, N42, N49, N50, N51 | U3A LF16-26 (R2V read for scope only, LF23) | F11, A01-A07 |
| N53 E3 | N01, N02, N03, N12, N13, N15 | E3 LF6-13 | K01-K03 |
| N54 SH1 | N02, N12, N53 | SD LF73-80 | K04 |
| N55 DG | N02, N03, N12, N13, N53 | SD G1 LF157-169 | K04 |
| N56 M13A | N02, N03, N12, N13, N15, N53, N54, N55 | M13 LF7-16 | K04 |
| N57 CAP62 | N02, N03, N09, N11, N12, N13, N15, N16, N53 | CAP LF9-18 | K06, R16 |
| N58 FULL | N01, N02, N03, N11, N12, N13, N15, N53, N55, N56 | FULL LF49-67 | F12, K01-K05 |
| N59 FINAL | N02, N03, N15, N23, N24, N25, N26, N27, N36, N37, N38, N39, N48, N52, N58 | C LF11-22, LF24-34 | F01-F14 |

**Closure statements (bookkeeping, CANDIDATE_UNVERIFIED).**
- **C1 (order).** In every row each input number is smaller than the node number, so N01, ..., N59 is a topological order
  and the graph is acyclic. Independently proved LFC/VFC (N11, N12) precede RW (N16), as CE LF5 requires; NF (N36) has no
  (a1) input; Units 1/2 (N50, N51) precede A2X (N52); FB is internal to FULL (N58), after DG (N55) and M13A (N56).
- **C2 (bodies).** Every node except N01 (permitted external Zhu import) and N59 (the composition itself, checked by FR
  only) has its proof body and governing corrections inside a census snapshot (section 1, last column). Governing text
  outside the snapshots: RES-1 to RES-3.
- **C3 (reachability).** Following inputs backwards from N59 reaches every node except N16 RW and N57 CAP62. These two
  are documentary-envelope nodes: N16's only consumer is N57, and N57 has no consumer (FULL LF67 read with FP2 LF7; CK
  LF91-92; no operative proof invokes RW: CW LF151, CH LF92, CA LF105, CK LF98). They cannot create a cycle.
- **C4 (leaves).** Every path from N59 ends at N01 (Zhu), N02 (ELEM: S56 section 2, LE E1-E2) or N03 (R0); every Sun(5)/
  Sun(6) use ends at N07/N08 through a site of section 4. This is the assertion requested at FR LF19-21, stated at the
  displayed node boundary.

## 4. Sun(5)/Sun(6) sites bound to S5W/S6W (every live site found by the censuses and FR)
| site | location (literal LF) | ambient subgroup | coset side / inversion | piece count | binds | consumers | evidence |
|---|---|---|---|---|---|---|---|
| S1 | RM LF61 (R1(7) step 1) | the finite quotient G of R0 | original disjoint LEFT cosets; no inversion | any 6 of the 7 (deletion RM LF25), all gcds 5 | S6W | N17 | CR LF89; FR LF34, LF49 |
| S2 | RM LF63 (step 3) | same G | original LEFT cosets | every 5-subfamily | S5W | N17 | CR LF90; FR LF49 |
| S3 | S56 LF140-141 (optional) | finite G in the proof of S6W | original LEFT cosets | 5 of 6 | S5W (upstream of S6W) | N08 (optional route only) | CR LF47, LF92 |
| S4 | LFC (c): L LF39-43; LE E3 LF29-32 | U_v; in the inverted configuration U*_v = g_vU_vg_v^-1 | x^-1(g_jU_j cap C) = (x^-1 p_j)(U_j cap U_v): LEFT cosets in U_v, index lambda_j; no inversion | |T| in {5, 6} out of |S_C| <= 6 | S5W / S6W | N12 and every LFC consumer | CW LF73, LF109; CH LF61; CA LF55; CK LF77; FR LF50 |
| S5 | VFC (V3): RK7 LF43, LF46; WV LF34, item 3 LF48 | U_v after g_v = 1 (inverse: its own vertex subgroup) | pieces (U_v cap w_jU_jw_j^-1)w_j in a RIGHT fibre U_v y; right-translate by y^-1, then invert: LEFT cosets in U_v, index d_j = q_j n_j / g_vj | |T| in {5, 6} out of |S_R| <= 6 | S5W / S6W | N11 and every VFC consumer; RPLP only in N16 | CR LF91; CW LF136; CH LF62; CA LF56; CK LF77; FR LF51; RW LF23 |
| S6 | ROW-U classes: L LF89-91, weights LF97, LF101 | U_v at an apex with six unmarked neighbours (or U*_v) | via S4 | R5: 6 pieces, all gcds 5; R24: 5 pieces, gcds <= 4 | S6W (R5), S5W (R24) | N14; inherited by N28-N38, N40-N42 (ROW-1 (c), ROW-2, E8 subset form) | CW LF111, LF115 |
| S7 | K63-U0: Step 1 L LF135-141 (ROW-U weights on five C-neighbours); Step 2 L LF142-143 | Step 1: U_v, v in C; Step 2: U_d | via S4 | Step 1: five C-pieces (quarter weights); Step 2: five of six C-pieces, all gcds 4 | S5W | N29; through the H5/J5 subset form N37, N38 | CW LF77, LF112 |
| S8 | K63-E D-ROW: KE LF25-32 | U_d | via S4 | five-piece subfamilies of at most six pieces | S5W | N38 | CW LF128 |
| S9 | K63-RES case (1c): KR LF140-143; KR2 X8 LF61-73 | U_v (x = alpha) or U*_v (x = alpha*, inverted configuration) | via S4 (LFC (c)) | 6 pieces, all gcds 5 | S6W | N39 | CW LF130; FR LF53; RESV LF18 |
| S10 | Corollary L, 44444 feasibility: A1S LF89-90; OV1 A1.10 New LF172 | U_t at apex t of C^x (U*_t for x = alpha*) | via S5: RIGHT-coset pieces inverted to LEFT | 5 pieces (W-fours, indices 4w_u) | S5W | N43 | CH LF67; FR LF52 |
| S11 | Corollary L, kills of 44441 and 44444: A1S LF84-95 (LF89-90 "[Sun(5)]") | U_t | via S5 | 5 pieces: z and four W-fours, pairwise gcds <= 4 | S5W | N43 | CH LF68; FR LF52 |
| S12 | TRANSFER of full Corollary L: OV1 A2.2 LF505-511; OV2 V2.7 (ii) LF193-194 | U_t in (a2-no5) | via S5 | same 5 pieces; p may be a four (index 4 5^B w_p, all gcds <= 4) | S5W | N49 | CH LF69; FR LF52 |
Notes. (i) Consumers of Corollary L's "at least two entries 4" (N44-N46, N52) use only its b <= 1 kills, Sun(2)/Sun(3)
(OV1 A1.4 LF87-92; CH LF70; CA LF44; U3A LF64-67), but S10-S12 are bound because full Corollary L is an accepted exported
statement. (ii) Not live, not bound: RICH's withdrawn six-label branch (RICH LF96-103; R1E R-1; CH LF63); L5/FH with
seven pieces (RK7 LF32; CR LF59, LF93; RW LF30). (iii) No other node applies Sun(5)/Sun(6) directly: CR LF45-50 (C5W,
C56W, K52W, KIIW, X1), CH LF64-66, LF70-71, CA LF38, LF57, U1E item 3, CK LF77-81. Every binding needs no distinct-subgroup
hypothesis and no seven-piece theorem (S56 LF19, LF22-25; FR LF55).

## 5. Exact residuals (never silently discharged)
| id | object | what is missing | effect on the operative graph |
|---|---|---|---|
| RES-1 | CD1 items CD4-CD7 (CD1 LF161-249; targets K62-CAP-v1 (D) rule discipline, (B3), (pi1), (B5)) | outside the K62 census snapshot LF1-154 (IDX LF1159; CK LF18, LF52) | none: they govern only N57, which has no operative consumer (C3). Needed only if the FULL "conservative envelope" (FP2 LF7) is to be certified rather than kept documentary |
| RES-2 | WV LF51-60: overlay items 6-9 (LF51-54, checker/format/coverage), process F-1 (LF56), imports and limits (LF58-60) | outside the ROOTS snapshot LF16-50 | none mathematical: items 6-9 concern certificate checkers; LF60's Sun(5)/Sun(6) import is bound at S1-S12; its other imports are N01, N02, N06 |
| RES-3 | RPE (K63-RES parent erratum v1, 3594dd19) | written after the ROWS-K63 census; checked only by FR LF43 and the parent's direct check DW LF20 | wording only (no weight or gcd change); N39's census coverage is otherwise complete |
| RES-4 | N59 FINAL (C sections 3-4 with CE) | no census; first-family review only (FR LF31-41; FD LF15-27); second-family and parent gates pending | the final join itself |
| RES-5 | N01 ZHU | not re-proved in this run (S56V LF10) | permitted classical import (TR LF68) |
| RES-6 | N16 RW | second-family RW gate pending (IDX LF1165); CR LF30, LF51 support only its restricted interface | none: no operative consumer (C3) |
Not residuals (examined, not consumed by any node): K62-SH-v1 statements (only the S2 argument: IDX LF1160; CK LF42-43);
M13 items 3-6, M13-B/C/D, K62-M13-erratum-v1, DT-A/B/C with K62-DT-C-erratum-v1, GS (cross-check), pending MK/M3R/R2MIX/
M13X (CK LF90-91; FULL LF65-67); K7-REM (W08); RM LF109-111 frame, RK7 LF13 subgroup clause, L5/FH, RK7 LF80 clause (C LF57;
CR LF58-61, LF70); K62-ARCH, K62-STATUS-v2, rules-k6-v1 and this directory's candidate documents (IDX LF1060-1156);
historical Sun(5)/Sun(6) and StageA/StageB records (replaced at section 4 and rows F05-F07, F21).

## 6. Status and non-claims
This ledger answers FR M1 at the displayed interface boundary: every live incoming interface listed by C and by the five
census reviews is a row of section 2 with a discharge; section 3 is the explicit graph with an acyclic order; section 4
binds every live Sun(5)/Sun(6) site; section 5 lists the residuals. It certifies nothing: all rows are CANDIDATE_UNVERIFIED
bookkeeping, pending review and the parent's disposition. Full Sun(7) UNACCEPTED. Historical Sun(5)/Sun(6)/StageB records
stay computer-assisted; StageB F-1 stays permanent. No novelty, Lean, human-review or runtime claim. Old files unchanged.
