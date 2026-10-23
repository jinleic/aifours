# Sun shard review: report v12 §3 and §3.1, 57 Sun authorities and the R2/R3 index

**Verdict: FIX.** Counts: **0 FATAL / 0 MAJOR / 4 MINOR.** All four findings are documentary and none changes a mathematical statement. No load-bearing body inside this scope is missing, so no re-review is required.

**Reading basis.** I read report v12 together with report errata 1–7 and map errata v7-e1 and v8-e1. I read ledger erratum 15 first and then erratum 16, as erratum 2 item 2 requires.

**Method.** This is hand documentary comparison of the pasted bodies only. I used no tools, code, computation, network or delegation. Hash and line-number matches are visual comparisons of the supplied strings. They are metadata, not forensic authentication. Component theorems are taken as accepted-statement imports; I did not re-audit their proofs.

## 1. Core checks

**Sun statement (gcd ≥ 7, distinct indices, arbitrary groups): PASS on the operative reading.**
- Original report v12 LF42 is a paraphrase set in quote format. It omits i≠j.
- Erratum 3 m4 makes LF42 read verbatim. Its text matches composition verdict LF7 exactly (bold markup aside): "some pair **i≠j** has gcd([G:U_i],[G:U_j])≥7", with subgroups possibly equal.
- Report LF44 lists the excluded hypotheses: no cover, finite group, normality, solvability, bounded valuation or bounded cofactor. This matches verdict LF7.
- "R0 finite-core quotient without assuming G finite" matches verdict LF11 and parent-check LF7, which says "No least-order selection".
- The v11 order-25..29 statement appears nowhere in v12. It is non-operative under report LF303, the withdrawal record LF3 and addendum v13. The failure history is retained at LF303/LF381 and in addendum v13.

**§3 composition boundary: PASS.**
- **Input list (LF44):** matches verdict LF11, including K62 FULL with E3, SH-DG, M13-A, CAP-DT and CI62. The report does not list M13X, R2MIX or GS as FULL inputs, which matches FULL LF23 ("not premises").
- **Ledger order (LF46):** N01–N08, N15, N09–N14, N16–N59, with N16→N57→N58→N59 ancestry. This matches verdict LF22, CI62 LF11 and DEFORDER LF6.
- **Ledger coverage (LF46):** together the local gates cover N01–N58:
  - AROOT and DEFORDER/AFIBRE (N09–N16), ARED (N17–N27), BROW (N28–N36), BK63 (N37–N39)
  - CRICH (N40–N45), CA2 (N46–N52), CK62 (N53–N58)
  - CUT2-M12 discharges CK62's N56/N58 conditions (CUT2 LF35).
- **Non-premise list (LF46):** consistent with verdict LF22 and LF27, CI62 LF9 and CENSUS-K62 LF19.
- **Review counts (LF48):** match verdict LF18–20, JOIN-CLOSURE LF15 and erratum 15 LF3. "Do NOT erase earlier MAJORs/NO_VERDICT" is consistent with:
  - FINAL-COMPOSITION 0F/1M
  - CLOSED-P2 0F/2M
  - FINAL-ABC parts B and C, 0F/2M each
  - the original AFIBRE review, 0F/1M
  - A2X Unit3 NO_VERDICT

**Ledger erratum 15 then 16 (LF50): PASS** with erratum 2.
- N42 consumes the local ROW-2 argument from N33, re-instantiated under PF1.
- N14 supplies the weights only once PF1 has verified the subset premise.
- N41 makes a three-neighbour E8 call; N43 makes the four-neighbour call.
- These all match erratum 16 LF5–7. Erratum 15's N41 "four-run" wording and its ROW-2≡N14 wording are superseded.
- The DG-stmt/DG-arg naming comes from erratum 15 item 2, as erratum 2 item 2 corrects.
- "No backdating" matches erratum 16 LF9.

**Legacy computation versus written replacements (LF52, LF11, LF74, LF320, LF330): PASS.**
- K52W LF19 and KIIW LF19 replace the two StageB branches.
- Written X1 replaces StageA operationally (parent-check LF16).
- S56W replaces Sun5/6 at site-specific bindings (S56W LF14; parent-check LF23).
- The F-1 record and historical computation are retained.
- The Sun5/6 second checkers stay unqualified and unused (S56W LF14; throttle-deferred obligation 11).

**§3.1 named results, LF61–74: PASS** row by row against the named-results file and each verdict, except MINOR-1 and MINOR-2 below.

**R2/R3 index (LF76): PASS.** The index body supports the line:
- R2 is accepted for (a1) with 29 repairs.
- R3a and R3b ended NO_VERDICT and were not accepted.
- A2X is a distinct rewrite.

R2 verdict LF37/LF50 and A2X LF37 corroborate it. The index hash matches the other-disposition map LF7.

**§11 Sun composite rows (LF354–358): PASS.** CENSUS, CLOSED-P1/P2 with A1-A2, EXPOSURE, FINAL and M1 roles are each faithful to their bodies.

## 2. Findings and minimal fixes (original report line numbers)

1. **MINOR-1, LF57 (attribution).** LF57 says the literal authorities for all the following rows are in the named-results file. That file covers only 13 rows; it has no K7-M1 row. The K7-M1 row at LF69 is governed by the M1 verdict.
   - **Fix:** after "…`73ff2047…b7aa`" append: "; the K7-M1 row (LF69) is governed instead by sun7-M1-parent-verdict-v1.md — SHA256 `7121ceeedc1f1b0de8d9642c8f5c2aed052d9f2e83140afee33ffcd2f71ced84` (§11 LF358)."

2. **MINOR-2, LF66 (scope precision).** "tripleintersection density" drops the inequality. K62A-TG LF10 and named-results LF12 state a lower bound.
   - **Fix:** read "triple-intersection density LOWER BOUND μ(X_a∩X_b∩X_c)≥1/gcd(n_v,T) (finite G or common finite-core quotient)".

3. **MINOR-3, LF44 (navigation and literal input names).** The three assigned files sun5-C5W, sun56-S56W and sun6-C56W are never named in the report. The verdict LF11 input list names them "(S56W/C5W/C56W)".
   - **Fix:** read "written all-group Sun5/6 (S56W; its H5/H6 discharged by the cores C5W/C56W)", following S56W LF5.

4. **MINOR-4, LF303 (cross-cutting statement fidelity).** The cited governing withdrawal record LF5 paraphrases the accepted statement without i≠j. Addendum v13 LF5 is similarly loose.
   - **Fix:** after "Sun's actual gcd-of-indices theorem" insert "(composition verdict LF7 verbatim, pairs i≠j, as read at LF42 via erratum 3 m4; the withdrawal LF5 and addendum-v13 LF5 paraphrases are not statement sources)". The old files are not edited.

**Already disposed and verified, not re-counted:** LF42 (erratum 3 m4), the LF50 DG attribution (erratum 2 item 2), and erratum 1 LF18's DG attribution (erratum 2 item 2).

**Optional, not counted:**
- LF46 could add verdict LF22's "seven-piece, least-order, computed-coverage" to its non-premise list.
- LF355 could say that the A1-A2 repairs record is a scoped mathematical acceptance (TC-A22, TC-B, BRIDGE, TRANSFER).

## 3. Per-filename fidelity (57 assigned files plus the index)

The SHA256 values for all 57 files agree across inventory v6 (LF781–1063), map v7 (rows 161–217) and the shard headers, by visual comparison. The compact map assigns 40 files to D093, 3 to D095 and 14 to D094/D096–D108, for 57 in total.

Cross-pins also agree:
- The composition verdict's pins for ledger errata v2–v15, CUT2, I1, I2, CI62, DEFORDER and JOIN-CLOSURE (LF42–63) match the shard hashes.
- Erratum 16's D23P and CE1 pins match D23RICH LF8/LF12.
- The R2/R3 index pins (R2, A2X, the composition verdict and erratum 16) match the shard hashes.

| # | File | Report location checked | Outcome | Body basis |
|---|---|---|---|---|
| 1 | sun5-C5W | §3 LF44, LF11, LF52 | **FIX (M-3)** | LF5 Core(5) finite 4r_i; LF13 Zhu Sun3; LF17 not full Sun5, Gong rules out novelty, no novelty claimed |
| 2 | sun56-S56W | LF44, LF52, LF330 | **FIX (M-3)** | LF5–10 all-group Sun5/6; LF14 site-specific, checkers unused |
| 3 | sun6-C56W | LF44 | **FIX (M-3)** | LF5 Core5(6) 5r_i; LF11 Zhu3/4 |
| 4 | sun7-A2X | LF44, LF76, LF48 | PASS | LF5–9 (a2); LF25 NO_VERDICT not approval; LF37 imports |
| 5 | CENSUS-K62 | §11 LF354, LF46 | PASS | LF17–20 non-premises; LF27–30 no cover or history removal |
| 6 | CENSUS-R2-A2 | LF354 | PASS | LF17–28 local only; substitution deferred to composition |
| 7 | CENSUS-RICH-A1 | LF354 | PASS | LF21–31 Sun5/6 sites need explicit binding (parent-check LF23) |
| 8 | CENSUS-ROOTS | LF354, LF44 (RW) | PASS | LF17–25 |
| 9 | CENSUS-ROWS-K63 | LF354, LF44 (NF) | PASS | LF15–30 wording minor; K63-U0 Sun5 eligible for S5W |
| 10 | CI62-first-family | LF44, LF46 | PASS | LF14–24 first-family only, notation fix |
| 11 | CI62 verdict | LF44, LF46 | PASS | LF5–15 no CAP cover, conservative edges |
| 12 | CUT2-M12 | LF46 | PASS | LF26–36 N56/N58 discharged; N59 dated |
| 13 | D23 | §3.1 LF61 | PASS | LF5–8, LF18 |
| 14 | DEFORDER-first-family | LF46 | PASS | LF14–16 |
| 15 | DEFORDER verdict | LF46 order, LF48 | PASS | LF5–11 order; earlier AFIBRE MAJOR kept |
| 16 | EXPOSURE-X1X2 | §11 LF356 | PASS | LF3 not accepted; LF28–38 |
| 17 | EXPOSURE2-Y1Y2 | LF356 | PASS | LF3, LF33–41 |
| 18 | EXPOSURE3 | LF356 | PASS | LF3 first-family only; LF51 CAP-ENV scoped |
| 19 | FINAL-ABC | LF357, LF48 | PASS | LF51–56 B/C 0F/2M historical |
| 20 | FINAL-COMPOSITION | LF357, LF48 | PASS | LF15–27 M1 then closed ledger |
| 21 | FINAL-JOIN-CLOSURE | LF48, LF357 | PASS | LF15 0/0/0 |
| 22 | FINAL-JOIN-I1 | LF48 | PASS | LF15–20 Prop4.5 binding |
| 23 | FINAL-JOIN-I2 | LF48 | PASS | LF15–20 FULL class, erratum 3 |
| 24 | K52W | LF44, LF11, LF52 | PASS | LF9 exact scope; LF19 StageB part only, F-1 uncured |
| 25 | K62-CAP-DT | LF44, LF46 | PASS | LF5, LF26 no cover or feasibility; LF43 |
| 26 | K62-FULL | LF44 | PASS | LF9 full class; LF23 premise limits |
| 27 | K62-GS | LF62 | PASS | LF9–13 |
| 28 | K62-M13 | LF63, LF46 | PASS | LF5 not an exclusion |
| 29 | K62-M13X | LF64 | PASS | LF9–11 |
| 30 | K62-R2MIX | LF65 | PASS | LF11–16 conditional M3E |
| 31 | K62-SH-DG | LF44, LF50 | PASS | LF19–23 DG parts (a)/(b) |
| 32 | K62A-TG | LF66 | **FIX (M-2)** | LF9–11 |
| 33 | K62E3 | LF44 | PASS | LF5, LF31 |
| 34 | K63DE-K735 | LF67, LF44 | PASS | LF9–13, LF36 |
| 35 | K63RES | LF44, LF52 | PASS | LF5; LF18 Sun6 import, later substituted |
| 36 | K7-A1-A2-repairs | §11 LF355 | PASS (optional note) | LF25–56 |
| 37 | K7-D23RICH-D23P | LF68 | PASS | LF9–13 |
| 38 | K7-NF | LF44 | PASS | LF11 NF, REM not used (CLOSED-P1 LF20) |
| 39 | K7-R2 | LF44, LF76 | PASS | LF5, LF17, LF50 |
| 40 | KIIW | LF44, LF11 | PASS | LF5, LF11, LF19 |
| 41 | LEDGER-ARED | LF46 | PASS | LF14–21 N17–N27 |
| 42 | LEDGER-AROOT | LF46 | PASS | LF14–20 |
| 43 | LEDGER-BK63 | LF46 | PASS | LF22 N37–N39, all of P1 |
| 44 | LEDGER-BROW | LF46 | PASS | LF19–21 N28–N36 |
| 45 | LEDGER-CA2 | LF46 | PASS | LF4 N46–N52 |
| 46 | LEDGER-CK62 | LF46 | PASS | LF3–4, LF21–30 (CUT2 obligation) |
| 47 | LEDGER-CLOSED-P1 | §11 LF355 | PASS | LF15–23 |
| 48 | LEDGER-CLOSED-P2 | LF355, LF48 | PASS | LF15–32 0F/2M then CI62/v2 |
| 49 | LEDGER-CRICH | LF46 | PASS | LF19–20 N40–N45 |
| 50 | sun7-M1 | LF69, LF358 | **FIX (M-1)** | LF5 content faithful; LF25; attribution at LF57 |
| 51 | sun7-RW | LF44, LF46 | PASS | LF5, LF9 |
| 52 | sun7-U1 | LF70 | PASS | LF5–8 |
| 53 | sun7-Z2 | LF71 | PASS | LF5 |
| 54 | sun7-Z23P5 | LF72 | PASS | LF5 |
| 55 | complete-written-composition | LF40–52, LF7, LF11 | PASS (LF42 via erratum 3 m4) | LF7, LF11, LF15–22, LF26–28 |
| 56 | sun7-lfc-inv | LF73 | PASS | LF18–24, LF27 |
| 57 | sun7-stageA-K53 | LF74 | PASS | LF5, LF9, LF24 |
| — | R2-R3 final-disposition index (out of pattern) | LF76 | PASS | LF12, LF21, LF30, LF45 |

**Tally:** 52 PASS, 5 FIX (all MINOR), 0 unsupported.

## 4. Scope and limits

**Bodies not supplied and not needed for any line checked:**
- composition errata v1–v3
- LEDGER-v1 and its erratum, and ledger errata v2–v14
- the consolidation record and the Prop4.5 binding
- review outputs and candidate proofs
- priority notes and the deviation registers
- checkpoint 042, the R3a/R3b authority inside the index

Each checked report line is supported by a supplied verdict or disposition. Not certified here: the R3b "3600s after 2700s" timing, and whether the deviation registers cover every item in composition verdict LF28.

**x1-written-parent-verdict-v1.md** is mapped to §3 (map row 218, D093) but is outside this 57-file assignment and its body is not supplied, so I did not assess it. The X1 claims at LF44, LF74 and LF261 are supported here by composition verdict LF11 and parent-check LF16. Final integration must confirm that another shard covers this file.

**OUT_OF_SCOPE and not approved:** §2, §4 (including DELTA1, which stays CANDIDATE, and the high-core target, NOT_PROVED), §5–§8, §10, the non-Sun parts of §9 and §11, the §7 Sun priority citations (Zhu, Menon, and Gong from C5W LF17), and errata 4–7 except where they concern Sun.

The 218-record count is dated. No post-212 pattern record is a Sun file, and no future file is claimed covered.

No human-review, Lean, priority, runtime or settlement claim is made.
