# PhysicsInfo shard: renewed complete documentary review (row1-erratum-3 generation)

**Method.** I compared the pasted bodies by hand. I used no tools, code, computation or network. Hashes and LF numbers are treated as supplied metadata.

**Coverage.** All 49 assigned bodies are present. For every one of the 49, the SHA in inventory-v6 and map-v7 matches the pasted header. All 37 correction bodies cited by those 49 records are present (Governing 1–37 and Shard 24–40), as are the 18 support records.

## Verdict: FIX (minor-only)

- **Counts:** 0 FATAL, 0 MAJOR, 9 MINOR, plus 2 uncounted nits.
- **Re-review:** none required. No load-bearing body is missing.
- **Row1-chain MAJOR from v2:** discharged.
  - The prompt (2a524cb0) has exactly 10 `###` bodies: candidate LF1–217, freeze, transition, primary LF195–225, GBBINDING snapshot e493b946, sparsity verdict, sparsity errata v1–v3, and row1 parent erratum v1.
  - Its LF1 says "Apply the appended parent erratum".
  - REVIEW-REQUEST c4fa71a4 contains only the in-file `process_deviation` string. It names no worker erratum.
  - Receipt 042e7698, note 660ec579 and verdict 893215c6 are mutually consistent.
  - I hand spot-checked the π/φ/support/c_s tables, the Lemma 3 table, H3 (π_s(1)=s+2) and the nonemptiness Gram entries. All are correct.
- **Erratum v3:** it introduces one wording MINOR of its own (fix 9).

## Explicit re-checks

| Item | Result |
|---|---|
| **FCLOSE/Fcouples (PhysicsInfo M3)** | PASS. FCLOSE LF5/LF9 gives C1–C12 with C13 conditional. Fcouples LF10 gives the composed consequence under exact (H) only (Prop2 + accepted FCLOSE + Theorem B). It discharges C13 for (H) arrays only. |
| **DRAT replay (PhysicsInfo minor)** | PASS. "Same algorithm, second build" matches run003 LF19, run004 LF13, run005 LF12, run006 LF9, run007 LF12, run008 LF10, run010 LF12 and run012 LF9. |
| **GB audit clock (M2)** | PASS. The audit `at` is 11:46:07. Solver and driver were reaped at 11:44:10, driver exit 3, no checker. This covers LF192. LF273's "ended by 11:46:07" is a true upper bound. |
| **R7/R9/WH10** | R9 (1536 runs, 10 endpoints, 0 maximal; receipt gives 24 classes × 64 starts) and WH10 (6384 starts, residual 0.13757415725848268, conditional prior, no certificate, not preregistered) match. One R7 MINOR (fix 7). |
| **J18** | Packaging-v2 LF15 places J18 in the RQLS State joins. M2 fixes LF253, but LF329 still has J18 in the CFR/MOLS bullet (fix 8). |
| **UNKNOWN / ansatz / credit discipline** | No ansatz miss is promoted to a no-go (assay v3, W8, R7/R9; WH10 rests on the cited prior). GA 16→17→18. GB 15/18 with three UNKNOWNs. PA trace 151→149→146→143→142→141→138→135→132→129→128 matches each verdict and frontier-v11 `current_counts_parent`: 16 ms06 and 7 ms09 closures. |

## Findings and minimal fixes (original LF numbers)

1. **MINOR, report LF205.** "AZ U/U' gives 12/16 … and 10/12 A-pairs" drops the lower-bound quantifiers of AZ verdict LF5. Replace with:
   > "U gives, in EACH of rows 1 and 7, at least 12 of 16 common-U pure pairs (A-refinement: at least 10 of 12 A-pairs). U′ gives, in EACH of columns 2 and 3, at least 12 of 16 own-index pure pairs. All are whole pure vectors of squares 2–5."
2. **MINOR, report LF207.** The H4(part) gloss omits q1, q7 ∈ V_A. Sources: Sigma verdict LF5, scope-precision LF5, Sigma erratum v1 item 4. Read:
   > "q1, q7 orthonormal in V_A = span{e1,e2,e3}, all three coordinates nonzero."
3. **MINOR, report LF213.** "Read through parent errata v1/v2" omits worker erratum 1 (bafdfd96). That erratum is where both MAJOR overclaims were withdrawn (JC verdict LF3; disposition `mandatory_errata`). Read:
   > "through worker erratum 1 and parent errata v1/v2."

   Apply the same reading at LF367.
4. **MINOR, report LF190.** The limits stated for B2.M2 are not carried to B3.M2. Append:
   > "The B3.M2 verdict has the same limits: 137665032 B formula; 671174069 B stream, read = delivered = consumed and hash-bound; payload not retained; one GA encoder and one DRAT checker. The P1-B3 template closure additionally uses the accepted NFr2+erratum1 import."
5. **MINOR, report LF236.** The replay audits do not cover b5's inherited intervals (run003 LF23/LF29). Insert:
   > "(b5's [0,99] and [100,199] rest on inherited VALIDATED measured-stream receipts with no retained or replayed proof bytes)."
6. **MINOR, report LF236.** "Retains historical raw arrays and frontier_counts 151; they are NOT current" is inaccurate:
   - `ms06_undecided` has 70 entries. That equals the current set: none of the 16 closed ms06 b-indices appear.
   - `ms09_undecided` has 59 entries. That is the v10 set, which still lists b65 even though b65 is closed in `new_case_closures_v11`.

   Replace with:
   > "frontier_counts 151 is the v1 baseline. The carried-forward arrays hold 70 ms06 (current) and 59 ms09 (v10, still incl. b65). Only `current_counts_parent` 70+58=128 is authoritative."
7. **MINOR, report LF220.** "2048 completed starts over 256 random configurations": the R7 audit binds 2048 runs over 256 distinct configurations × 8 starts. "Random" and "completed" are unsupported by the supplied body. Replace accordingly.
8. **MINOR, report LF329 (and LF230).** J18 remains in the CFR6,21/sixMOLS39 bullet, because M2 corrected only LF253.
   - Delete "/J18" at LF329.
   - Append at LF230: "This includes the RQLS STATE J18 origin-authentication join (packaging-v2 LF15), OPEN external, not MOLS-specific."
9. **MINOR, row1 erratum v3 LF7.** "With parent erratum v1 and its imported sparsity-verdict corrections" presents non-premise context as governing. This conflicts with candidate LF188 ("not a premise") and prompt LF3 ("context, not premises"), and the SPV errata predate the candidate. Read:
   > "Governs the immutable candidate with parent erratum v1. The sparsity verdict and errata v1–v3 are non-premise context only."

**Nits (uncounted)**
- **N1.** The PhysicsInfo erratum LF14 label "PA13" should read "PA19 run013".
- **N2.** Frontier v11 v4-closure `kind` says "all are … formula-parse" for the run-005 items. The phase correction measured only run-008/010/012 items, so the run-005 phase split is UNDETERMINED here. The report makes no such claim, so no report fix is needed.

## Per-file fidelity (49)

| # | File | Destination | Outcome |
|---|---|---|---|
| 1 | cfr21-theoremA-parent-verdict-v1.md | §6.2 LF249 | PASS: k≥4, 3∣n, 9∤n, support ≥6, dim K ≤1, rank 5/6 on {0,τ}. I hand-checked that k≥4 is necessary ({0,x,2x}). |
| 2 | mols39-LemmaU-R1-parent-verdict-v1.md | §6.2 LF251–253 | PASS: 2 classes / 486 lifts; 243/190/185/5; conditional R1; "human proof" reading; certificate unrun. |
| 3 | moqls8-B3-AZpurity-parent-verdict-v1.md | §5.1 LF205 | FIX (fix 1) |
| 4 | moqls8-B3-AZpurity-parent-verdict-v2-confirmation.md | LF205 | PASS |
| 5 | moqls8-B3-AZpurity-second-family-parent-disposition-v1.json | LF205 | PASS |
| 6 | moqls8-B3-Dext-parent-disposition-v1.json | LF211 | PASS |
| 7 | moqls8-B3-Dext-parent-disposition-v2-header.json | LF211/LF288 | PASS: upper-bound clock reading. |
| 8 | moqls8-B3-Dext-parent-verdict-v1.md | LF211 | PASS |
| 9 | moqls8-B3-Sigma-parent-disposition-v1.json | LF207 | PASS |
| 10 | moqls8-B3-Sigma-parent-verdict-v1.md | LF207 | FIX (fix 2) |
| 11 | moqls8-B3-interior-parent-disposition-v1.json | LF210 | PASS: its stale "hierarchy" field is governed by interior erratum v2, which the report applies. |
| 12 | moqls8-B3-interior-parent-verdict-v1.md | LF210 | PASS: same as #11. |
| 13 | moqls8-B3-interior-parent-verdict-v2-confirmation.md | LF210 | PASS |
| 14 | moqls8-B3-jointcompletion-parent-disposition-v1.json | LF213 | PASS |
| 15 | moqls8-B3-jointcompletion-parent-verdict-v1.md | LF213 | FIX (fix 3) |
| 16 | moqls8-B3-pair-genuine-parent-verdict-v1.md | LF201 | PASS |
| 17 | moqls8-B3-propagation-parent-disposition-v1.json | LF212 | PASS |
| 18 | moqls8-B3-propagation-parent-verdict-v1.md | LF212 | PASS |
| 19 | moqls8-B3-row1-parent-verdict-v1.md | LF204 | PASS: chain is errata v1–v3; fix 9 targets erratum v3, not the report. |
| 20 | moqls8-B3-row1-second-family-parent-disposition-v1.json | LF204 | PASS |
| 21 | moqls8-B3-sparsity-parent-verdict-v1.md | LF202 | PASS |
| 22 | moqls8-P1-B2-M2-parent-verdict-v1.json | LF190, LF198 | PASS: 137665034 B; rc 20/0; 455119925 B ×3; payload not retained; v5d termination unexplained. |
| 23 | moqls8-P1-B3-M2-parent-verdict-v1.json | LF190 | FIX (fix 4) |
| 24 | moqls8-PURE23-parent-verdict-v1.md | LF203 | PASS |
| 25 | pa19-D2-parent-disposition-v1.json | LF245 | PASS: 600→300 s; 1258291200→629145600 B; design-only. |
| 26 | pa19-b63-F45-parent-verdict-v1.md | LF236 | PASS |
| 27 | pa19-b65-parent-verdict-v1.md | LF236 | PASS: 129→128. |
| 28 | pa19-class-b63-final-repairs-parent-disposition-v1.json | LF240 | PASS |
| 29 | pa19-class-b63-parent-disposition-v1.json | LF238–240 | PASS: clocks superseded by addendum v5 LF8/LF17. |
| 30 | pa19-class-b63-parent-verdict-v1.md | LF238–240 | PASS: "71 ranges" corrected by addendum v5 LF14 and report LF288. |
| 31 | pa19-class-b63-parent-verdict-v2-confirmation.md | LF238–240 | PASS |
| 32 | pa19-ms09-e7-excess-parent-disposition-v1.json | LF242 | PASS |
| 33 | pa19-ms09-e7-excess-parent-verdict-v1.md | LF242 | PASS |
| 34 | pa19-ms09-structural-parent-verdict-v1.md | LF236 | PASS: 132→129; b70 is corroboration only. |
| 35 | pa19-run003-parent-verdict-v1.md | LF236 | FIX (fix 5); count 151→149 is correct. |
| 36 | pa19-run004-parent-verdict-v1.md | LF236 | PASS: 149→146. |
| 37 | pa19-run005-parent-verdict-v1.md | LF236 | PASS: 146→143. |
| 38 | pa19-run006-parent-verdict-v1.md | LF236 | PASS: 143→142. |
| 39 | pa19-run007-parent-verdict-v1.md | LF236 | PASS: 142→141; b9 [0,814] of 815. |
| 40 | pa19-run008-parent-verdict-v1.md | LF236 | PASS: 141→138. Its LF14 phase wording is withdrawn by a130a686 and not repeated in the report. |
| 41 | pa19-run010-parent-verdict-v1.md | LF236 | PASS: 138→135. |
| 42 | pa19-run012-parent-verdict-v1.md | LF236 | PASS: 135→132. |
| 43 | rqls10-E1-nonMUB-parent-verdict-v1.md | LF226 | PASS |
| 44 | rqls10-FCLOSE-parent-verdict-v1.md | LF227 via M3 | PASS |
| 45 | rqls10-FCO-2p-parent-verdict-v1.md | LF225 | PASS: 362880 = 9!; one producer; independent verifier unrun. |
| 46 | rqls10-Fcouples-parent-verdict-v1.md | LF227 via M3 | PASS |
| 47 | rqls10-WH5C2-parent-verdict-v1.md | LF228 | PASS |
| 48 | rqls10-WH5C2-second-family-parent-disposition-v1.json | LF228 | PASS |
| 49 | rqls10-assay-v3-full-parent-disposition-v1.json | LF220 | PASS. Fix 7 concerns the R7 support record in the same LF, not this file. |

**Support records.** These are PASS except as noted: GB B3.M2 audit and its SETTLED record, B2.M4 audit, GB appendix, v5d binding, native precision erratum v2, R9 audit and receipt, W8, kcal, v4 smoke, WH10 audit and prior, W1/R1–R10, PA19 HOLD, MOLS N1/successor4/prose erratum, beta-supervisor19, CP1/CP2, throttle/deferred-12, contract.
- R7 audit: fix 7.
- Packaging v2: fix 8.
- Frontier v11: fix 6 and nit N2.

## Scope and limits

**Bodies not supplied.** None of these is load-bearing for the report text checked; those claims are verdict-level imports.
- Candidate and proof texts.
- Review stdout and notes, including the Sigma Claude note LF185–196 that the AZ confirmation attributes. The row1 Codex 0F/0M count is likewise attribution only.
- Parent written checks and raw/replay audits.
- [G] (f529224e).
- Frontiers v2–v10 and the M2H inventories.
- Full GBBINDING [J].
- Beta/PRT sources.
- The RQLS fixed-B / trade / exact finite-phase records. LF220 uses these only as labels in a limitation statement.

**Out of scope, not approved here:**
- §1–4 (Sun and Olson, including the v11 withdrawal and DELTA1).
- §7 (including errata v4–v6 on CPro1).
- §8, except the GB clock.
- §9–11, except J18 placement and obligation retention.
- The 212-record census and map completeness.
- All other shards.

**No claims made:** no transitive mathematics re-proof (beyond the row1 spot-check), and no runtime, settlement, human, Lean or priority claim.
