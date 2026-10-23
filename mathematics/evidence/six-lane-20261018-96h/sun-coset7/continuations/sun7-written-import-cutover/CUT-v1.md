# CUT-v1 — Sun(7) written import-substitution audit and conditional composite [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read at 2026-10-19T18:04:45-0700, immediately before this exclusive create. Owner SunM13MixedFibres.
- **Frozen scope:** `CUT-SCOPE-v1.md` (this directory), sha256 dfb213b42f86b40fe7ff3361b01fb2b2a2c6a567f915be588ce4f9f533372f98.
- **Authority:** `RUN/control/sun7-written-import-substitution-scope-v1.json`, sha256
  1b3bc0ba6aaed69f934bf9e754e3d2b348040c455676a46650458f5fffbd188f.
- **Nature.** A written/logical AUDIT plus a CONDITIONAL composite statement. No new class proof, no acceptance, no full
  Sun(7) claim, no alteration of any historical record, no cure of StageB's F-1. Every judgment below is grounded in a
  quoted verdict line; where a verdict did not settle a dependency it would be listed as UNRESOLVED (none was found).
- Roots: O16 = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016; S = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7;
  RUN = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h (verdicts in RUN/review); R16 = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review.

## 0. The new import map (applied to S/continuations/sun7-composition/SUN7-COMP-v1.md, 98796f95…d7, with its errata)
- **M1 (StageB -> written).** The StageB class statement (R16/sun-coset7-stageB-classes-parent-verdict-v1.md, fd14952c…c13f,
  line 5; one checker, line 46; permanent F-1, line 40) is no longer cited. K5.2* is cited from the ACCEPTED written
  K52W verdict (RUN/review/sun7-K52W-parent-verdict-v1.md, 66df666edf4eed6e740d3f7cb66a084db4ae019e8bb3156aeb7c43863093fb5d, lines
  5, 9) and KII from the ACCEPTED written KIIW verdict (RUN/review/sun7-KIIW-parent-verdict-v1.md,
  6e907403e3c88e0577318dd197f6e648c0a7880b07092f562871c6c494006d7c, lines 5, 11). The D2' case stays removed by the written
  Lemma D2' of the reduction (README line 83), as before.
- **M2 (Sun(5)/Sun(6) -> S5W/S6W, conditional).** Every load-bearing use of the Sun(5) or Sun(6) THEOREM (as a statement,
  applied to a coset family in any group, including inside a subgroup U_v) is cited from S5W/S6W
  (S/continuations/sun56-written-composition/S56W-v1.md, 9dfa360e6b54d6075e79f240bf2375e9049a66ae02fc14f375946e0bed61b894, section
  1), whose statements are verbatim the accepted ones (R16/sun-coset5-parent-verdict-v1.md line 8; R16/sun-coset6-parent-gate-
  verdict-v1.md line 9). S5W needs **H5** (Core(5), C5W 2e4b42b2…5c69); S6W needs **H5 and H6** (Core5(6), C56W 63cbcdb1…f8b1);
  H5, H6 and S56W are UNREVIEWED. Nothing else from the old Sun(5)/Sun(6) proofs is re-imported.
- **M3 (K7 branch).** The old composition's unreviewed Lemma K7-SPLIT and its hypothesis (H-NF) are replaced by the ACCEPTED
  K7-NF/K7-REM assembly (RUN/review/sun7-K7-NF-parent-verdict-v1.md, dc92a745773706c40b9abf2c8c6c3ac949b0b680f36264bacc9aa3d8d6d8e998,
  lines 5, 9-12): every K7 configuration lies in (a2). (a2) stays the UNVERIFIED hypothesis **HA** (Theorem A2X, units 1-3,
  pending second-family review of the split unit 3).
- **Unchanged.** Reduction, LFC/INV, VFC, Prop 4.5, X1 + bridge, K62X, K63-D/E/RES and the (a1) closure remain cited at their
  accepted literal scopes with their mandatory overlays.

## 1. Conditional composite statement
**Theorem SUN7-COND [CANDIDATE_UNVERIFIED; CONDITIONAL].** Assume HA (A2X), H5 (Core(5)), H6 (Core5(6)) and the correctness of
the composition S56W. Then **Sun(7)** holds: for any group G, subgroups U_1..U_7 of finite index (possibly equal) and pairwise
disjoint left cosets g_1U_1..g_7U_7, some i < j has gcd([G:U_i],[G:U_j]) >= 7 (O16/sun-coset7/README.md line 11). Moreover, under
these hypotheses every load-bearing node of the proof is a WRITTEN argument: the only non-elementary external imports are
Zhu's Theorem 1.1 (Sun(3), Sun(4)); no computer-assisted node (StageB, the Sun(5) bridge, the Sun(6) checker) is used.
*Proof (assembly).* If Sun(7) fails in G, R0 gives a CE in a finite quotient (README lines 27-35; written verdict line 18).
The accepted written reduction (README lines 54-103, rules-k7-v1 lines 53-58; written verdict lines 20-21), with its
Sun(5)/Sun(6) steps cited from S5W/S6W (M2), puts the CE into one of K7, K6.2*, K6.3, K5.2*, K5.3, KII. KII: KIIW. K5.2*: K52W.
K5.3: X1 + bridge. K6.2*: K62X. K6.3: K63-D, K63-E, K63-RES. K7: K7-REM puts it in (a2), excluded by HA. Each class authority
is stated for arbitrary groups (or finite groups plus R0), so it applies to the CE. QED

## 2. Load-bearing ledger (every node; old dependency -> new import)
| id | node and literal scope | text / verdict (sha256) and lines | computational dependency recorded there | new import | status |
|---|---|---|---|---|---|
| N0 | Sun(7) target; R0; CE; P0, P1 | O16/sun-coset7/README.md (2a6d6d6e…3fd1) 11, 27-52; R16/sun-coset7-written-parent-verdict-v1.md (73a25ba6…9f35) 16-18 | none (Sun(2) elementary) | unchanged | ACC |
| N1 | six-class reduction: R1(7) step 1 (a >= 3: Sun(6)), step 3 (\|C\| >= 4: Sun(5)), R1a (Zhu k=4), R1b (Zhu k=3), R1c (Prop 4.5), D2/D2' (VFC) | README 54-103; O16/sun-coset7/rules-k7-v1.md (77b9afec…3cee) 53-58; written verdict 20-21, 60 | Sun(5), Sun(6) statement imports | Sun(5) -> S5W; Sun(6) -> S6W (H5/H6) | ACC + conditional imports |
| N2 | VFC (V1)-(V4) and count | rules-k7-v1 40-49; written verdict 23, 34 | (V3) applies Sun(t), t <= 6, inside U_v (rules-k7-v1 line 43) | Sun(5)/(6) instances -> S5W/S6W | ACC |
| N3 | LFC, INV, ROW-U, K7-M0 | S/K7-LFC-INV-v1.md (45be9162…726c) with erratum (7af9acf0…bd5); RUN/review/sun7-lfc-inv-parent-verdict-v1.md (8621e744…cca18) 18-23 | LFC uses Sun(t), 2 <= t <= 6 (line 18); imports Sun(5)/(6) (line 33); the parent control is explicitly NOT load-bearing (lines 25-27) | Sun(5)/(6) -> S5W/S6W | ACC |
| N4 | Prop 4.5 | O16/sun-coset5/proof-v4.md (3d17efcc…4516) 63-101 with rules erratum v3 (1b3e126e…5e8ed); written verdict line 21 | none: written (also reproduced in S56W section 3) | unchanged | ACC |
| C1a | KII | old: StageB (fd14952c…c13f) line 5 | computer-assisted, one checker (line 46) | **KIIW** (6e907403…7c) lines 5, 11: Sun(2) re-proved + Zhu Sun(3) only; no Sun(4)-(7), no LFC package, no StageB | ACC written |
| C1b | K5.2* (README line 94) | old: StageB line 5 | as above | **K52W** (66df666e…fb5d) lines 5, 9: elementary + Zhu Sun(4), Sun(2) re-proved; no Sun(3), (5), (6) | ACC written |
| C2 | K5.3 via X1 + bridge | RUN/review/x1-written-parent-verdict-v1.md (84d7d8ab…0c4c) 5, 19-20; O16/sun-coset7/rules-k7-addendum-v1.md (fb2c306b…1066) 159 | none: "written, computation-free" (line 5); no Sun(3)-(6) | unchanged | ACC |
| C3 | K6.2* (Theorem K62X) | RUN/review/sun7-K62-FULL-parent-verdict-v1.md (f3b22e53…1f0c) 5, 9, 23; parent erratum v2 (299e73f4…5c52) line 7 | Sun(5)/(6) transitive (line 23; erratum v2 item 3 inherits M13-A's closure incl. CAP/RC) | Sun(5)/(6) -> S5W/S6W | ACC |
| C3.1 | E3 (e_d >= 4, e* = 2) | RUN/review/sun7-K62E3-parent-verdict-v1.md (576969dd…) 5, 29, 31 | direct Sun(2), Sun(4); LFC package's Sun(5)/(6) (line 31); "numerical compatibility check is not an existence claim" (line 29) | Sun(5)/(6) -> S5W/S6W | ACC |
| C3.2 | DG (SH/DG) | RUN/review/sun7-K62-SH-DG-parent-verdict-v1.md (cae455c3…) 5, 32, 36 | "No native computation" (line 5); direct Sun(2)-(4); Sun(5)/(6) via LFC (line 36) | Sun(5)/(6) -> S5W/S6W | ACC |
| C3.3 | M13-A..D at stated scope | RUN/review/sun7-K62-M13-parent-verdict-v1.md (2fac7a30…) 5, 50 + erratum (99276f6d…) | Sun(5)/(6) via LFC/VFC (line 5); "certificate values" (line 50) are hand weights in the written proof, re-derived by both reviews | Sun(5)/(6) -> S5W/S6W | ACC |
| C3.4 | CAP-62, C1/C2 granularity, RC-O, RC-i* | RUN/review/sun7-K62-CAP-DT-parent-verdict-v1.md (84061c6f…) 5, 23-25 | written finite representation; "no complete subfamily exclusion or finite coverage" (line 5); Sun(5)/(6) transitive | Sun(5)/(6) -> S5W/S6W | ACC |
| C4 | K6.3: K63-D, K63-E, K63-RES | RUN/review/sun7-K63DE-K735-parent-verdict-v1.md (1a1c6390…3919) 5, 9-10, 46; RUN/review/sun7-K63RES-parent-verdict-v1.md (5ac59529…7bac) 5, 12, 18; correction json (b41e47fc…) 9 | "no exploratory search, LP optimum or leaf census is a premise" (K63DE line 5); Sun(6) load-bearing in the all-gcd-5 case (K63RES line 18); exact-weight controls "not a premise" (K63RES line 12) | Sun(6) -> S6W; Sun(5) -> S5W | ACC |
| K1 | K7 \ F (K7-NF) and K7-REM | NF verdict (dc92a745…e998) 5, 9-12, 22 | assembly; Sun(5)/(6) transitive (line 22) | Sun(5)/(6) -> S5W/S6W | ACC |
| K1.1 | M0 / M1 / Z2 / K7-35 / U1 / Z23-P5 | LFC verdict 21; RUN/review/sun7-M1-parent-verdict-v1.md (7121ceed…) 5, 13, 25; …Z2… (0f6b9aa3…) 5, 32; K63DE verdict 11; …U1… (44dfbe85…) 5-8, 32; …Z23P5… (7179e564…) 5, 15 | each: written; "No computational output is a premise" (M1 13); "no computed leaf census, LP optimum or exploratory search" (Z2 32); probes not premises (U1 32); "No new enumeration is a premise" (Z23P5 15); Sun(t <= 6) inherited | Sun(5)/(6) -> S5W/S6W | ACC |
| K2 | (a1) closure | RUN/review/sun7-K7-R2-parent-verdict-v1.md (9b0f7df5…b926d) 5, 9, 17, 44, 46 | Sun(5)/(6) transitive (line 5); line 44's replay is a text-binding check, "not a substitute for proof review" | Sun(5)/(6) -> S5W/S6W | ACC |
| K2.1 | A1/A2 repairs; RICH/D23P; D23 | RUN/review/sun7-K7-A1-A2-repairs-parent-verdict-v1.md (2a7c5b6c…) 5; …D23RICH-D23P… (1167bc4f…) 21-23; RUN/review/sun7-D23-parent-verdict-v1.md (d3453de1…) 15 | Sun(5)/(6) transitive; "No finite probe is a premise" (D23 15); A2.10 "enumerated" = a written list of claims (OV1 lines 29-30) | Sun(5)/(6) -> S5W/S6W | ACC |
| HA | (a2): Theorem A2X, units 1-3 | S/continuations/k7-a2-closure/K7-A2-UNIT-{1,2,3}-v1.md (79d948bf…, 1bef6d8c…, a2b40a9e…) | written; imports accepted A1/A2 (incl. BRIDGE A2.10, TRANSFER), RICH/D23P, LFC/INV | Sun(5)/(6) -> S5W/S6W | **UNVERIFIED (pending)** |
| HS | S5W, S6W | S56W (9dfa360e…b894) sections 1-7 | written; Zhu, Prop 4.5, R0, R1, R1(6) | replaces the accepted computer-assisted Sun(5) (2cf02436…) and Sun(6) (efe1d849…) statement imports | **UNREVIEWED** |
| H5 | Core(5) | S/continuations/core5-written-bridge/C5W-v1.md (2e4b42b2…5c69) 110-120 | written; Sun(2), Zhu Sun(3) | — | **UNREVIEWED** |
| H6 | Core5(6) | S/continuations/core6-written-bridge/C56W-v1.md (63cbcdb1…f8b1) 109-119 | written; Sun(2), Zhu Sun(3), Sun(4) | — | **UNREVIEWED** |
| Z | Zhu Thm 1.1 (k = 3, 4) | arXiv:0807.2207 (README line 15) | classical | unchanged | external |
**Dropped from the load-bearing set:** StageB (all of it), StageA (already non-load-bearing: ruling line 15), the old Sun(5)
bridge and S-D section, the Sun(6) checker/certificates, the written-verdict rules CAP (finite-coverage bridge) and RPLP
(used only by StageA/B), every minimal-order frame, every control/probe/exploratory computation (each explicitly a
non-premise in its verdict), and SUN7-COMP's K7-SPLIT (superseded by accepted K7-REM).

## 3. Hidden-computation audit result
Reading every verdict in the ledger, the ONLY computational dependencies recorded anywhere in the accepted chains are:
(i) the Sun(5) and Sun(6) THEOREM imports (direct in N1, N2, N3, C4; transitive in every other class chain through LFC/VFC
and the reduction) and (ii) StageB for K5.2*/KII. Under M1/M2 both are replaced; (i) only conditionally. Every other
"check", "control", "certificate value", "probe", "replay" or "numerical check" named in these verdicts is stated there to be a
non-premise (LFC 25-27; K63RES 12; M1 13; Z2 32; U1 32; Z23P5 15; D23 15; K62E3 29; SH-DG 5; R2 44) or is a written
hand-checkable weight inside a proof (M13 50). **No UNRESOLVED dependency was found.**

## 4. Quantifiers, equal subgroups, acyclicity
- **Quantifiers.** Each class authority is stated for arbitrary groups with finite-index subgroups (K52W line 9; KIIW line 5;
  X1 line 5; K62-FULL line 9; K63DE line 13; K63RES line 5; NF line 9; R2 line 5) or for finite groups with the R0 lift; the
  composite passes from arbitrary G to a finite CE first, so every authority applies. S5W/S6W are stated for every group and
  are applied inside finite subgroups U_v exactly as the accepted Sun(5)/Sun(6) statements were.
- **Equal subgroups.** No ledger node assumes distinct subgroups (S56W section 1 states "possibly equal"; classes are
  index-defined; INV and fibre counts treat cosets, not subgroups).
- **Acyclicity.** S5W/S6W depend only on Zhu, Prop 4.5, R0, R1, R1(6), H5, H6; H5 and H6 re-prove their own fibre counts with
  Sun(2)-Sun(4) and import neither the LFC package nor Sun(5)/Sun(6). Class nodes depend on S5W/S6W, LFC/INV, VFC and accepted
  lemmas; the reduction depends on S5W/S6W; HA depends on accepted K7 lemmas; nothing depends on SUN7-COND. Hence the DAG
  {Zhu, elementary} -> {H5, H6, Prop 4.5} -> {S5W, S6W} -> {LFC/INV, VFC, reduction, class nodes, HA} -> SUN7-COND is acyclic.

## 5. Gate status under the new map (factual, no promotion)
| gate | status |
|---|---|
| NF (G1) | MET: accepted assembly (NF verdict) |
| A2X (G2) | OPEN (HA) |
| composition review (G3) | OPEN: SUN7-COMP and this CUT file unreviewed |
| two-checker/written-replacement ruling (RUN/control/sun7-full-result-computation-gate-ruling-v1.json, 4818f1ca…5eada, lines 9-15): StageB K5.2*/KII | MET for a composition citing K52W/KIIW (KIIW verdict line 19) |
| same ruling: Sun(5), Sun(6) | UNMET until H5, H6 and S56W are accepted (then the written replacement the ruling allows) |
| process (G5) | StageB F-1 permanent and NOT cured; StageB is simply no longer load-bearing under M1 |
| formal/human (G6) | none |

## 6. Residual obligations (explicit)
1. **HA:** A2X units 1-3 (unit 3 being split into no5 vs zt5 + conditional join for second-family review).
2. **H5:** review/verdict of C5W.  3. **H6:** review/verdict of C56W.  4. **HS:** review/verdict of S56W.
5. Review of this CUT file and of SUN7-COMP with its errata (the K7-SPLIT node is superseded; its other content stands).
No further computational residual and no unresolved dependency were found.

## 7. Citation substitution list (old -> new; history unchanged)
| where cited | old citation | new citation |
|---|---|---|
| README R1(7) step 1; LFC/VFC Sun(6) instances; K63-RES all-gcd-5 case | Sun(6), R16 efe1d849… (computer-assisted) | S6W, S56W section 5 (CONDITIONAL on H5, H6) |
| README R1(7) step 3; LFC/VFC Sun(5) instances | Sun(5), R16 2cf02436… (computer-assisted) | S5W, S56W section 4 (CONDITIONAL on H5) |
| SUN7-COMP class row KII | StageB fd14952c… | KIIW 6e907403… (ACCEPTED written) |
| SUN7-COMP class row K5.2* | StageB fd14952c… | K52W 66df666e… (ACCEPTED written) |
| SUN7-COMP K7 row (K0, K1) | K7-SPLIT + (H-NF) | K7-REM, NF verdict dc92a745… (ACCEPTED) |
The old verdicts and records stay byte-identical and keep their computer-assisted / F-1 labels; a substituted citation
names the new written authority, never re-labels the old one.

## 8. Non-claims and review checks
Not claimed: Sun(7); acceptance of HA, H5, H6, S56W or this file; that any old record became computation-free; a cure of
F-1; novelty, Lean or human review. **Requested checks:** (1) every ledger row against its quoted verdict lines; (2) the
statement identity behind M1, M2, M3; (3) that no verdict in the chains hides another load-bearing computation; (4) the
quantifier and acyclicity arguments; (5) the gate table's factual accuracy.
