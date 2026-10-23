# AMENDMENT-4.r1, cut generator, B-map oracle, K3-Q4 sidecar and errata: static hostile review desk result (M7CutsHostileDesk), 2026-10-18 PT

Scope: two static CLI reviews plus a desk static reading of the pinned snapshot `snapshot/` (manifest `4b563226…63fb`, 71 files, 305,166 bytes, text only, no CNF or proof). All 8 assignment pins and the 3 parent-document pins match. Neither the desk nor the reviewers ran a solver, encoder, checker, generator or oracle. **No K3 or M(7) verdict, and nothing here is ACCEPTED: a delegated disposition is advice, not the parent's gate.** The draft stays NOT FROZEN and INACTIVE. The C321/C411 parent replays and B certificates are running and not accepted. No C311+cuts run exists.

| Review | Reported identity | Time | Disposition | FATAL | MAJOR | MINOR | Note SHA-256 | Receipt SHA-256 |
|---|---|---|---|---|---|---|---|---|
| `moqls7-amendment4-codex-v1` | gpt-6.1-sol, effort max, read-only sandbox (stderr header) | 675 s | ACCEPT-WITH-FIXES | 0 | 2 | 3 | `970430f7…2601` | `b7b51172…9025` |
| `moqls7-amendment4-claude-v1` | claude-opus-5-5 (init and modelUsage), no tools, 0 tool_use blocks | 2257 s | ACCEPT-WITH-FIXES | 0 | 3 | 15 | `dc66f3c1…364a` | `b096fb1a…0043` |

Codex provenance (`codex-command-provenance.json`): 61 commands (52 nl, 5 cat, 1 shasum, 1 wc, 1 ls, 1 rg). All ran with cwd = snapshot. No interpreter, write, redirect or outside path appears. Claude: result `success`, `is_error` false, list cost $6.70.

## Per-question status
| Q | Codex | Claude | Desk | Consolidated |
|---|---|---|---|---|
| Q1 | FIX-REQUIRED | FIX-REQUIRED | FIX-REQUIRED (text) | **FIX-REQUIRED (provenance/text only)**: Old binding gap closed in substance as post-hoc provenance; driver r2 binding correct; K2 prerequisite met; oracle observes B's own map; corrections m1-m8 needed in a new sidecar/errata version; B_C311 must be bound before any B/C311 use. |
| Q2 | CONDITIONAL | FIX-REQUIRED | CONDITIONAL mathematics; standard open | **FIX-REQUIRED (draft section 1 standard and B hashes, H3 wording); transport mathematics CONDITIONAL-sound**: Transport sound for all 14 frames, 42 points, every role assignment; G1/G2 unmet; standard and B instances must be fixed in the frozen version. |
| Q3 | FIX-REQUIRED | FIX-REQUIRED | FIX-REQUIRED | **FIX-REQUIRED**: Block generator faithful (238140 distinct clauses, 588 x (45+360), negative g literals, no auxiliaries, A and B maps correct); source-CNF binding promised by the draft is absent and no appender/strengthened-CNF code exists. |
| Q4 | ACCEPT | CONDITIONAL | CONDITIONAL | **CONDITIONAL**: Controls establish what they state; Psi(f) correctly labelled non-vacuity outside K3; no genuine K3 positive exists; README:91 applicability needs a parent ruling; label fixes m10-m11. |
| Q5 | CONDITIONAL | CONDITIONAL | CONDITIONAL | **CONDITIONAL**: Cut family invariant under all row/column/square permutations and transposition, hence under H of every cube; a common lex-minimal orbit member satisfies base, cube, lex and cuts; invariance not even needed; composition sound under H1-H5 and G1-G2. |
| Q6 | FIX-REQUIRED | CONDITIONAL | FIX-REQUIRED | **FIX-REQUIRED / NOT MET**: No freeze/use/acceptance condition is met; missing appender and certification driver, instance/standard/B_C311 bindings, segment and header controls. |

Overall: both reviewers return ACCEPT-WITH-FIXES with 0 FATAL. The mathematics (transport lemma, counts, cut family, lex compatibility, composition) is sound under H1–H5 and G1–G2. The package cannot be frozen or used as it stands: the external gates are unmet, the strengthened-input code and bindings are missing, and the acceptance standard is open.

## Agreed verified content (both reviews and the desk)
- **Q1, binding 1.** All nine sidecar targets match by SHA:
  - lex metadata `7bef0b78…190d` and cube metadata `3b2ab04f…d9ed`;
  - lex controls `3bd546ad…4053` and k3_lex `2b721e85…9b10`;
  - AMENDMENT-3 `374978c6…f3cc` and its bindings `0d842cf8…0316`;
  - the three screen receipts `0ad180cd…2eb6`, `fba1b566…ce94` and `1927cb60…9781`.
  - The source CNF `7fca33f1…2001` equals the value inside the lex metadata, the cube metadata and the original screen receipt. The lex CNF `059be616…8c4f` equals the lex metadata value.
  - Statuses: UNKNOWN at 1800.145 s, rc 0; UNKNOWN safety stops at 769.881 s and 1229.385 s, rc −15.
  - This meets `AMENDMENT-3.r1.md:46` in substance, as post-hoc provenance.
- **Q1, binding 2.** Delta r2 `8556bd50…0900` and driver r2 `49677766…8211` match; both cert_r2 receipts pin the driver, with `-t 3600` for solver and checker.
  - Chronology: delta frozen_at 21:39:20 (mtime 21:39:40) and driver mtime 21:38:35 both precede the first A/C321 start at 21:39:49.
- **Q1, K2 prerequisite.** The parent K2 verdict excludes exactly-two-non-classical triples (accepted text r2, caveats attached) and meets the prerequisite. Gram r2:52-65 and LEMMAS:69-78 are the right targets.
- **Q1, oracle.** It observes B's own map; it does not echo A.
  - `gram_encB.py:113-118` allocates `gv` first and `g()` reads it. The fix branch at `:203-215` iterates the same `gv` after all base clauses.
  - The designs carry pairs, never indices. An identity decode, A being a bijection and the all-nonzero sign control together give B-pair(v) = A-pair(v) for every v.
  - The base prefix is identical in all 14 designs, so `--fix-json` only appends.
  - Design counts equal the bit populations of 1..2646 (desk-recomputed: 1323, 1323, 1323, 1320, 1319, 1312, 1303, 1280, 1280, 1111, 1024, 599).
  - The B base hash `42a5f304…0aac` equals the B_C321/B_C411 metadata. The comparator self-tests are correctly labelled.
- **Q1, dating.**
  - The oracle was pinned at 00:48:54 (pin file mtime 00:49:12) and ran 00:49:18–00:49:40.
  - The generator was pinned at 01:00:31 (mtime 01:00:53) and ran 01:00:59–01:02:16.
  - The sidecar (00:51:30), errata (00:52) and draft (00:53) postdate the K2 verdict (00:42:18) and the parent notice (00:46).
  - No document presents a post-hoc binding as preregistered. cert_B_r4 (pre-oracle, UNKNOWN) is not relied on.
- **Q1, E2–E5 and E7.** These corrections are right for the cited frozen lines. In E2, var 109 = g₁((0,3),(1,0)) and var 145 = g₁((0,4),(1,0)).
- **Q2, hypotheses.** H1–H2 make every K3 configuration minimal, which gives all-line G4. H3–H5 restrict correctly. Own-row/column heaviness suffices.
- **Q2, counts.** w ≥ 1 by unit norm (Boolean G3), with G1 at the shared cell. G5 applies to the same cell pair (p,r), so the three neighbour sets are disjoint and Σw ≤ 6. The thresholds force exactly (4,1,1) or (3,2,1).
- **Q2, transport.** It holds for all 14 frames, 42 points and every role assignment.
  - Steps: transpose all three squares for column frames; apply ρ, then κ (the excluded frame cell goes to (0,0)); relabel the squares.
  - All six positions are occupied, so all 18 signed literals are fixed. The `--sym` units hold, as do G1–G5 and G4, including the replaced (1, row 0) constraint. G6 is implied.
  - Transposition preserves the QLS axioms, the tensor ONBs (the same 49 products), the ray sets and all-line heaviness.
  - "Heavy local type" means some weight ≥ 3 (G4's threshold).
  - There is no arbitrary-ONB, classical-line, K1/K2 or non-minimal overreach, no C311/UNKNOWN premise, and no circularity.
- **Q3, family.** `emit()` produces exactly 26460 + 211680 = 238140 distinct clauses in 588 groups of 45+360. Every literal is a negative non-collinear g variable in 1..2646, and there are no auxiliaries.
  - A's map equals the wrapper map (asserted at `k3_cuts_r1.py:308-309`). The B decode inversion is correct (`:259-274`).
  - Byte order is deterministic. The block length is 440·9477 + 2·1164240 + 2·238140 = 6974640, equal to `block_bytes_A`.
  - The import pins match the GENERATOR json, and the gate passed (15,951,609,856 B). Output is exclusive and no CNF was written.
- **Q4.** C1 covers 2100 = 4⁶ − 3·3⁶ + 3·2⁶ − 1 assignments, of which 450 = 3·30 + 6·60 are forbidden; spec = template = emitted.
  - psi_gram: m0 = 2 and f = [0,6,5,1,3,4,2]. Every own frame/point has weight 5, so (2940,0) = 588·C(5,4).
  - The Ψ fixture is not even a mutually orthogonal triple: Ψ and slope 2 are both supported at displacement (1,5). Its NON-VACUITY label is right.
  - No genuine K3 positive exists.
- **Q5, invariance.** The cut family is invariant under every row, column and square permutation and under transposition, so under H of every cube regardless of E2.
  - A common lex-minimal orbit member satisfies base ∧ cube ∧ lex ∧ cuts, with reconstructible auxiliaries.
  - Invariance is not even needed, because every cut clause is valid for every K3 configuration.

## Consolidated findings (the parent decides; frozen files must not be rewritten; fixes go into new versions)
**MAJOR-A (MAJOR)**. Sources: Codex M1, Codex M2, Claude M1, desk D4. Refs: `lane/review/drafts/AMENDMENT-4.r1.md:69-71`; `lane/code/k3_cuts_r1.py:292-299,318-319`; `lane/evidence/k3cubes/cuts_r1_receipt.json:26-32`; `lane/code/k3_cube_certify_r2.py:31-33,49-50`; `lane/code/k3_cube_certify_r3.py:27-73,95-97`; `lane/review/K3-CERTIFICATION-DRIVER-DELTA.r3.json:9`.
- Problem: Draft section 3 says the generator binds the source cube CNF SHA and the strengthened CNF size; the generator opens no C311 input, selects no instance, and the header increment is a descriptive string. No appender or driver exists that can build or certify a strengthened C311 input (r2/r3 regenerate original cubes and require an UNSAT screen of that same input).
- Correction: Split section 3: (i) block generator as implemented (receipt = block evidence only); (ii) new pinned appender + driver delta that regenerates the named input in memory (r3 method), asserts its SHA, re-emits and asserts block 05f31da4...e6dd, writes the header, binds the strengthened SHA, streams or counts it in the gate. Assert headers A original (96978, 865696), A lex (107513, 897308), B original (461370, 1867942).

**MAJOR-B (MAJOR)**. Sources: Claude M2, Codex Q6 items 2-3 and Q1 text, desk D1, D9. Refs: `lane/review/drafts/AMENDMENT-4.r1.md:24-26,84-85,87-88`; `lane/README.md:80-81`; `lane/explore/k3cubes/B_C311.meta.json:4-5`; `lane/code/bmap_oracle_r1.py:115`; `lane/code/k3_direct_B_r5.py:62`; `parent/moqls7-k3-cover-parent-disposition-v1.md:18`.
- Problem: Acceptance standard left open (A-only allowed) against Phase C two encodings; G1/G2 and section 5 name only A CNFs; B_C311 (b3ec0108...c077, meta bfa298ee...a056) exists but the oracle never reads its metadata and the r5 driver indexes a missing C311 key; no B lex C311 exists.
- Correction: Fix one standard for C321, C411 and C311+cuts (A+B per README:80-81, or a parent-recorded deviation). Under A+B name B_C321 8b7b8124...12c6, B_C411 01acf464...8bf8 and B_C311 in G1, G2 and section 5; bind B_C311 to the oracle in a new version; if A uses lex C311, state that B uses the original C311 or generate/bind a B lex input under AMENDMENT-3.

**MAJOR-C (MAJOR (process; reviewers split))**. Sources: Claude M3, Codex: no defect (note LF100, Q4 ACCEPT). Refs: `lane/README.md:91`; `lane/evidence/k3cubes/cuts_r1_receipt.json:90-91`; `parent/moqls7-k2-parent-verdict.md:52`.
- Problem: README 0.5 requires every necessary-condition encoding to admit all matched genuine controls before production. No genuine K3 positive exists; the published Psi(f) is necessarily rejected; the classical positives satisfy the cut clauses only (they violate base G4). The draft is silent on README:91.
- Correction: Frozen version states that the cuts are derived conditional clauses valid only under H1-H5 and G1-G2 and how README:91 applies; obtain an explicit parent ruling, as for the earlier README:91 deviation.

**MINOR and observations**
- **m1** (Codex m1, Claude m1a). `lane/review/K3-Q4-SIDECAR.r1.json:40`; `lane/review/AMENDMENT-2.r1.md:5-6`. Sidecar says AMENDMENT-2 did not state the K2 half; AMENDMENT-2.r1.md:5-6 names the K1/K2 exclusions. *Correction:* Restrict the omission to AMENDMENT-3, the receipt scope fields and the old draft.
- **m2** (Claude m1b, desk D12). `lane/review/K3-Q4-SIDECAR.r1.json:40`. "G4 ... holds for a K3 triple only when the triple minimises" reverses the logical direction. *Correction:* Read "G4 is justified (by the minimality lemma) for minimal triples; with K1 and K2 excluded every K3 triple is minimal".
- **m3** (Codex m2, Claude m2). `lane/review/K3-Q4-SIDECAR.r1.json:47`; `lane/review/K3-ERRATA.r1.md:59-60`; `lane/review/GRAM-ENCODING.r1.md:45-55`; `lane/code/gram_enc.py:15-16`; `lane/review/GRAM-ENCODING.r2.md:26-27`. Gram r1 already contains the minimality G4 argument; the K1 section 8 pointer is the gram_enc.py comment. ERRATA:59 abbreviates the r2 digest as ...d7c6; it ends ...d6c7. *Correction:* Correct the explanation and digest; keep the r2:52-65 / LEMMAS:69-78 destination (Claude adds r2:63-65 and LEMMAS:54-78).
- **m4** (Codex m3, prior desk MINOR chronology, prior Claude m8). `lane/review/AMENDMENT-3.r1.md:3`; `lane/review/AMENDMENT-3.bindings.r1.json:2`; `manifest.json (lex meta mtime 21:20:58)`; `lane/review/AMENDMENT-2.bindings.r1.json:2`. Freeze-order exceptions (bindings after input generation, before search; g6_controls 20:15:24 after the first screen start 20:13:35) remain unrecorded. *Correction:* Record them as provenance exceptions in the next sidecar version; no retroactive preregistration.
- **m5** (Claude m3, Codex Q1 text, desk D1). `lane/review/K3-ERRATA.r1.md:22-23`; `lane/review/K3-BMAP-ORACLE.r1.json:10`; `lane/code/bmap_oracle_r1.py:115`. "both B cube metadata files": three exist; B_C311 base-hash equality is static only. *Correction:* Reword; bind B_C311 (meta bfa298ee...a056) before any B/C311 use.
- **m6** (Claude m4). `lane/review/K3-Q4-SIDECAR.r1.json:2,6-22,25,31`. Binding 1 (00:51:30, after the lex screens ended 23:47:55) is not labelled post hoc; :31 cites desk mtimes (the desk manifest confirms driver r2 21:38:35 and delta r2 21:39:40 < 21:39:49); :25 is an unverifiable absence claim. *Correction:* Label "post-hoc provenance, not the pre-search binding of AMENDMENT-3.r1.md:46"; cite the mtime source; soften :25.
- **m7** (Claude m5). `lane/review/K3-Q4-SIDECAR.r1.json:43`; `lane/review/K3-ERRATA.r1.md:68,73`; `parent/moqls7-k2-parent-verdict.md:3,7,54`. K2 prerequisite "met" without the verdict qualifiers; "Parent replay is in progress" cites no parent record. *Correction:* Carry the qualifiers (computer-assisted, conditional on the trust base and the 35-class provenance caveat, not a new gate); cite the parent record or drop the sentence.
- **m8** (Claude m6, Codex note LF65 (label only)). `lane/review/AMENDMENT-4.GENERATOR.r1.json:2-3`; `lane/evidence/k3cubes/cuts_r1_receipt.json:2`; `lane/evidence/LOG.md:167`. Authority cites a parent label 01:12 PDT, later than the 01:00:31 pin and the 01:00:59 run; "host clock at receipt was before 01:00:31" is a worker statement. *Correction:* Treat 01:12 as a label only; record the message identifier or hash.
- **m9** (Claude m7, Codex note LF87, desk D3). `lane/code/k3_cuts_r1.py:9,238-256,259-274,298`. Generator B decode lacks header, base-prefix and sign checks and does not assert the oracle receipt status or pins; docstring "(as in the B-map oracle)" overstates. *Correction:* Assert oracle receipt PASS and pins (as k3_direct_B_r5 does) or replicate the oracle checks.
- **m10** (Claude m8, Codex note LF104, desk D7). `lane/evidence/k3cubes/cuts_r1_receipt.json:165-170`; `lane/review/AMENDMENT-4.GENERATOR.r1.json:15`. Once B_map_equals_A_map holds, block_sha_equal and sets_equal are tautological; the swapped-map test only shows SHA sensitivity yet is labelled non-vacuity. *Correction:* Label them as consequences; the only non-tautological datum is the runtime decode.
- **m11** (Claude m9, Codex note LF102). `lane/code/k3_cuts_r1.py:171-172,357-359,410-411`; `lane/evidence/k3cubes/cuts_r1_receipt.json:110-119`. distinct_ok includes the total count, so distinct_ok=false for at_most_four and one_clause_dropped is count-driven; per-mutation reasons are not stored. *Correction:* Store the full shape_report per mutation; separate distinctness from count.
- **m12** (Claude m10, Codex note LF92). `lane/code/k3_cuts_r1.py:292-299`; `lane/code/bmap_oracle_r1.py:87-91`; `lane/review/AMENDMENT-4.GENERATOR.r1.json:6`. Receipts do not record sys.executable, sys.version or imported module paths (no -I). *Correction:* Record them in the next run.
- **m13** (Claude m11). `lane/review/drafts/AMENDMENT-4.r1.md:16-18,90-93`; `parent/moqls7-k2-parent-verdict.md:17,21`. H3 names no parent file accepting the exact K3 encoder instantiation (3 squares, no L, heavy, --sym); section 6 omits auxiliary reconstruction and per-encoder soundness. *Correction:* State H3 as encoder soundness for the exact K3 base; add auxiliary reconstruction (A: h, guards; B: products, counters; lex prefixes) to section 6.
- **m14** (Claude m12). `lane/review/drafts/AMENDMENT-4.r1.md:40,45-47,51,53`. Transpose acting on all three squares is implicit; contradictions are not phrased against exact CNF hashes. *Correction:* Make both explicit.
- **m15** (Claude m13, desk D13). `lane/review/drafts/AMENDMENT-4.r1.md:8`; `lane/README.md:207-209`; `lane/evidence/LOG.md:160-161`; `lane/evidence/k3cubes/cuts_r1_receipt.json:15-18`. Interim text called AMENDMENT-4.r2.md (no SHA in README); archived copy e72233ca...2870; receipt binds draft ef87fa49. *Correction:* Do not reuse r2; bind the archive path/SHA; re-run the generator or add an explicit carry-over binding for a revised draft.
- **m16** (Claude m14, desk D14). `lane/review/drafts/AMENDMENT-4.r1.md:83-98`; `lane/review/drafts/AMENDMENT-4.md:61`. No driver, caps, screen policy or RSS limit for a C311+cuts run. *Correction:* Put them in the MAJOR-A driver delta.
- **m17** (Claude m15). `lane/evidence/k3cubes/cert_r2/A_C321.json:32`; `lane/evidence/k3cubes/cert_r2/A_C411.json:32`. Same solver_log_sha256 bde6e1ee... in both receipts. *Correction:* RESOLVED by desk: both logs are exactly b"s UNSATISFIABLE\n" (16 bytes). Not a defect.

Reviewer disagreements:
- README:91 (MAJOR-C): Claude MAJOR; Codex finds no defect (Q4 ACCEPT).
- Q2 label: Codex CONDITIONAL (puts the standard under Q6); Claude FIX-REQUIRED.
- Prior dependency text / Claude m9: Codex PARTIALLY-CLOSED; Claude CLOSED with new m1/m2. Consolidated PARTIALLY-CLOSED.
- Prior polish / Claude m14: Codex CLOSED; Claude PARTIALLY-CLOSED (instance unnamed). Consolidated PARTIALLY-CLOSED.
- Q6 label: Codex FIX-REQUIRED; Claude CONDITIONAL. Consolidated FIX-REQUIRED / NOT MET.

## Disposition of every prior finding (old K3 cover review)
| Prior finding | Location | Codex | Claude | Consolidated | Evidence |
|---|---|---|---|---|---|
| Desk MAJOR 1 (lex meta binding) | `prior/prior-desk-RESULT.findings-excerpt.md:LF61-64` | CLOSED | CLOSED (post hoc) | **CLOSED as post-hoc provenance** | `lane/review/K3-Q4-SIDECAR.r1.json:6-22` |
| Desk MAJOR 2 (G4/K1/K2 hypothesis) | `prior/prior-desk-RESULT.findings-excerpt.md:LF65-67` | CLOSED | CLOSED | **CLOSED** | `lane/review/drafts/AMENDMENT-4.r1.md:11-21` |
| Desk MAJOR 3 (gate on parent-accepted exact CNFs) | `prior/prior-desk-RESULT.findings-excerpt.md:LF68-70` | CLOSED | CLOSED (standard open) | **CLOSED; residual standard -> MAJOR-B** | `lane/review/drafts/AMENDMENT-4.r1.md:23-28` |
| Desk MINOR B map | `prior/prior-desk-RESULT.findings-excerpt.md:LF73-76` | CLOSED | CLOSED (m3 residual) | **CLOSED for C321/C411; B_C311 residual -> m5** | `lane/review/K3-ERRATA.r1.md:8-24; lane/evidence/k3cubes/bmap_oracle_r1.json` |
| Desk MINOR Q3 invariance | `prior/prior-desk-RESULT.findings-excerpt.md:LF77-79` | CLOSED | CLOSED | **CLOSED** | `lane/review/K3-ERRATA.r1.md:26-36` |
| Desk MINOR T(X) | `prior/prior-desk-RESULT.findings-excerpt.md:LF80` | CLOSED | CLOSED | **CLOSED** | `lane/review/K3-ERRATA.r1.md:38-44` |
| Desk MINOR wording (AM2 zero; G6 zero; collinear G6) | `prior/prior-desk-RESULT.findings-excerpt.md:LF81-84` | CLOSED | CLOSED | **CLOSED** | `lane/review/K3-ERRATA.r1.md:46-56` |
| Desk MINOR stale driver binding | `prior/prior-desk-RESULT.findings-excerpt.md:LF85-87` | CLOSED | CLOSED | **CLOSED (desk mtimes in manifest support sidecar:31)** | `lane/review/K3-Q4-SIDECAR.r1.json:24-31` |
| Desk MINOR chronology | `prior/prior-desk-RESULT.findings-excerpt.md:LF88-92` | OPEN | OPEN | **OPEN (not in the parent Q4 required list) -> m4** | `no erratum or sidecar entry` |
| Desk MINOR dependency text | `prior/prior-desk-RESULT.findings-excerpt.md:LF93-95` | PARTIALLY-CLOSED | CLOSED (with new m1, m2) | **PARTIALLY-CLOSED -> m1, m2, m3** | `lane/review/K3-Q4-SIDECAR.r1.json:38-49; lane/review/K3-ERRATA.r1.md:58-60,70-74` |
| Desk MINOR exclusion status wording | `prior/prior-desk-RESULT.findings-excerpt.md:LF96` | CLOSED | CLOSED | **CLOSED (unsourced replay sentence -> m7)** | `lane/review/K3-ERRATA.r1.md:62-68` |
| Desk MINOR AMENDMENT-4 polish | `prior/prior-desk-RESULT.findings-excerpt.md:LF97-103` | CLOSED (all items) | PARTIALLY-CLOSED (instance unnamed) | **CLOSED except instance selection: PARTIALLY-CLOSED** | `lane/review/drafts/AMENDMENT-4.r1.md:1,30-58,60-85` |
| Desk non-issue identical lex/cube solver logs | `prior/prior-desk-RESULT.findings-excerpt.md:LF104` | CLOSED | NOT-APPLICABLE | **NOT-APPLICABLE (resolved earlier; 10-byte c UNKNOWN)** | `lane/explore/k3cubes/screenA_r1/A_C311.solver.log; lane/explore/k3lex/screenA_r1/A_C311.solver.log` |
| Codex M1 | `prior/prior-codex-note.findings-excerpt.md:LF13-16` | CLOSED | CLOSED | **CLOSED (post hoc)** | `lane/review/K3-Q4-SIDECAR.r1.json:6-22` |
| Codex M2 | `prior/prior-codex-note.findings-excerpt.md:LF18-23` | CLOSED | CLOSED | **CLOSED; residual standard -> MAJOR-B** | `lane/review/drafts/AMENDMENT-4.r1.md:11-28` |
| Codex m1 | `prior/prior-codex-note.findings-excerpt.md:LF27-30` | CLOSED | CLOSED | **CLOSED** | `lane/review/K3-ERRATA.r1.md:26-36` |
| Codex m2 | `prior/prior-codex-note.findings-excerpt.md:LF32-35` | CLOSED | CLOSED | **CLOSED (runtime oracle exists)** | `lane/review/K3-ERRATA.r1.md:8-24` |
| Claude D1 | `prior/prior-claude-note.findings-excerpt.md:LF125-129` | CLOSED | CLOSED | **CLOSED** | `lane/review/drafts/AMENDMENT-4.r1.md:11-21` |
| Claude D2 | `prior/prior-claude-note.findings-excerpt.md:LF131-135` | CLOSED | CLOSED (M2) | **CLOSED; residual standard -> MAJOR-B** | `lane/review/drafts/AMENDMENT-4.r1.md:23-28` |
| Claude m1 | `prior/prior-claude-note.findings-excerpt.md:LF148` | CLOSED | CLOSED | **CLOSED** | `lane/review/K3-ERRATA.r1.md:46-49` |
| Claude m2 | `prior/prior-claude-note.findings-excerpt.md:LF150-154` | CLOSED | CLOSED | **CLOSED; B_C311 residual -> m5** | `lane/review/K3-ERRATA.r1.md:8-24; lane/code/bmap_oracle_r1.py` |
| Claude m3 | `prior/prior-claude-note.findings-excerpt.md:LF156-159` | CLOSED | CLOSED | **CLOSED** | `lane/review/K3-ERRATA.r1.md:51-56` |
| Claude m4 | `prior/prior-claude-note.findings-excerpt.md:LF161-164` | CLOSED | CLOSED | **CLOSED** | `lane/review/K3-ERRATA.r1.md:26-36` |
| Claude m5 | `prior/prior-claude-note.findings-excerpt.md:LF166` | CLOSED | CLOSED | **CLOSED** | `lane/review/K3-ERRATA.r1.md:38-44` |
| Claude m6 | `prior/prior-claude-note.findings-excerpt.md:LF168-171` | CLOSED | CLOSED | **CLOSED (post hoc)** | `lane/review/K3-Q4-SIDECAR.r1.json:6-22` |
| Claude m7 | `prior/prior-claude-note.findings-excerpt.md:LF173-177` | CLOSED | CLOSED | **CLOSED** | `lane/review/K3-Q4-SIDECAR.r1.json:24-31` |
| Claude m8 | `prior/prior-claude-note.findings-excerpt.md:LF179-182` | OPEN | OPEN | **OPEN -> m4** | `no erratum` |
| Claude m9 | `prior/prior-claude-note.findings-excerpt.md:LF184-187` | PARTIALLY-CLOSED | CLOSED (m1, m2) | **PARTIALLY-CLOSED -> m1, m2, m3** | `lane/review/K3-Q4-SIDECAR.r1.json:38-49; lane/review/K3-ERRATA.r1.md:58-60,70-74` |
| Claude m10 | `prior/prior-claude-note.findings-excerpt.md:LF189` | CLOSED | CLOSED | **CLOSED** | `lane/review/K3-ERRATA.r1.md:62-68` |
| Claude m11 | `prior/prior-claude-note.findings-excerpt.md:LF191` | CLOSED | CLOSED | **CLOSED** | `lane/review/drafts/AMENDMENT-4.r1.md:1,30,57-58` |
| Claude m12 | `prior/prior-claude-note.findings-excerpt.md:LF193-195` | CLOSED | CLOSED | **CLOSED** | `lane/review/drafts/AMENDMENT-4.r1.md:39-51` |
| Claude m13 | `prior/prior-claude-note.findings-excerpt.md:LF197` | CLOSED | CLOSED | **CLOSED** | `lane/review/drafts/AMENDMENT-4.r1.md:34-37` |
| Claude m14 | `prior/prior-claude-note.findings-excerpt.md:LF199-202` | CLOSED | PARTIALLY-CLOSED | **PARTIALLY-CLOSED (instance unselected; C2-C4 present)** | `lane/review/drafts/AMENDMENT-4.r1.md:73-85` |
| Claude m15 | `prior/prior-claude-note.findings-excerpt.md:LF204` | CLOSED | NOT-APPLICABLE | **NOT-APPLICABLE (resolved earlier)** | `prior desk LF104` |

Parent disposition requirements (`parent/moqls7-k3-cover-parent-disposition-v1.md`) and the nine prerequisites (prior desk LF106-115):
| Requirement | Status |
|---|---|
| Parent Q2: runtime B-map oracle before relying on any B certificate | MET for C321/C411 scope (oracle pinned 00:48:54, PASS 00:49:18-00:49:40, 0/2646 mismatches); B_C311 metadata not covered (m5) |
| Parent Q3: invariance wording and T(X) definition | MET (E2, E3) |
| Parent Q4: bind A_C311 lex metadata to cube metadata 3b2ab04f... and control receipt | MET as post-hoc provenance (sidecar binding 1) |
| Parent Q4: replace stale driver binding by K3-CERTIFICATION-DRIVER-DELTA.r2.json | MET (sidecar binding 2) |
| Parent Q4: restate K2 prerequisite | MET with wording errors (m1, m2, m7) |
| Parent Q4: repoint Gram r1 citation to Gram r2 | MET with an explanation error and digest typo (m3) |
| Parent Q5 / desk LF106-115 item 1: K1 accepted and K2 parent-accepted | Stated as H1-H2; met |
| item 2: accepted encoder bridge(s) + B erratum/oracle | Stated as H3; oracle exists; no parent file accepting the exact K3 instantiation (m13) |
| item 3: accepted cover and --sym WLOG | Stated as H5; parent Q1 accepted |
| item 4: parent-accepted C321/C411 exclusions of the exact CNFs | Stated as G1-G2; NOT MET; standard open (MAJOR-B) |
| item 5: reviewed, corrected transport lemma | Section 2; both reviews find it sound; minor wording (m14) |
| item 6: frozen reviewed generator, 238140 distinct clauses, per-encoder map, output SHA, control | Generator pinned and controls PASS, not frozen; source/strengthened binding absent (MAJOR-A) |
| item 7: H-invariance statement if lex is used | C4 + control d; holds |
| item 8: fresh DRAT-checked UNSAT of the exact strengthened C311 input on the protocol routes | Stated in section 5; NOT DONE; no appender/driver (MAJOR-A) |
| item 9: parent review of the full composition | Stated in section 6; NOT DONE; add auxiliary reconstruction (m13) |

## Q6: exact conditions to freeze, use and accept (none is met at pin time)
1. Parent verdicts accepting the exclusion of the exact C321 d598507d84a8d7595b30a100d528dca08bc0ce1aa71978583f09aac188298388 and C411 2b92f5b15cd641e4a07ecec241b7957deac972aa3c7333056ff3e739e46addf2 CNFs, each naming the hashes and its standard; under A+B also B_C321 8b7b8124...12c6 and B_C411 01acf464...8bf8 with post-oracle B certificates and parent replay. Status at pin: none (A parent replays running; B/C321 running; B/C411 not started).
2. One explicit standard for C321, C411 and C311+cuts: A+B per README.md:80-81 (Phase C, two encodings), or an A-only deviation recorded by the parent. The cover disposition (LF18) allows an A replay route for C321/C411 acceptance, but that is not by itself compliance with Phase C.
3. A parent statement accepting the exact K3 encoder instantiation (3 squares, no L, heavy, --sym) as sound for G1-G5/G4; may be part of the composition review.
4. Named C311 instance: A original 7fca33f1e6324cbe17bc44bbea7f8d9188bcac187252d766fb0fa5e39e1c2001 or A lex 059be6164176ee93c94d93bd47fa1d365477b6c94f3aa867df991f677e1a8c4f; for B only original B_C311 b3ec010855ad4abd75ffd6eb57aaa3ff158bc8447625ee2097f5a6057594c077 exists (no B lex). Bind B_C311 to the oracle in a new version (bmap_oracle_r1.py:115 checks C321/C411 only; k3_direct_B_r5.py:62 has no C311 key).
5. A new frozen version of the draft (not named r2; bind archive e72233ca...2870) carrying the fixes, with bindings to: its own SHA; generator 0ec92c86...1b0a and receipt 9cfc0e81...babbf (or a re-run on the new draft SHA); block 05f31da497315877347f7d780e0e6f4c9c4799c8becee3bdb192a8420ff6e6dd; oracle receipt 6e2bd95e...952c; K1, K2, C321, C411 verdicts; the chosen instance(s); appender and driver SHAs.
6. Missing code: a pinned appender/regenerator and certification driver delta for the strengthened input (no existing driver fits: k3_cube_certify_r2.py:31-33,49-50 and k3_cube_certify_r3.py:95-97 require an UNSAT screen of an original cube; k3_direct_B_r5 serves original C321/C411). Generate in memory per K3-CERTIFICATION-DRIVER-DELTA.r3, or count the file in the gate.
7. Missing pre-solve controls: appended segment = exactly 238140 clauses whose bytes hash to 05f31da4...e6dd (per encoder; B uses the oracle-identical map); header equality with A original (96978, 865696), A lex (107513, 897308), B original (461370, 1867942); prefix equality with the named input; C1-C4 re-bound to the frozen draft; for B either oracle-level checks or assertion of oracle PASS and pins.
8. README:91 ruling by the parent (MAJOR-C).
9. Resources: fresh gate per native stage >= 12.2e9 + projected retained growth (including any strengthened CNF), continuous 12e9 floor, stated solver/checker caps and screen policy, single solver+checker pipeline.
10. Certification: newly regenerated, DRAT-checked UNSAT of each exact strengthened input on each route of the chosen standard (solver rc 20, checker rc 0, exact s VERIFIED, no safety stop). No transfer of the old C321/C411 proofs. UNKNOWN stays UNKNOWN; SAT is a Boolean pattern only.
11. Parent replay of those certificates.
12. Parent review of the full composition K1 & K2 => G4 => --sym => three cubes => {C321, C411 accepted; transport => cuts; C311+cuts certified}, including auxiliary reconstruction and, if lex is used, the lex-representative step.

## Control limits
Mapping to the draft: C1 is control (b) local coverage; C2 is control (a) counts and distinctness; C3 is control (e) plus the oracle; C4 is control (d).
- **oracle**: Establishes that B's fix-branch pair-to-index map equals A's for all 2646 g variables under --squares 3 --heavy --sym; --fix-json is append-only (base prefix identical in all 14 designs); B base hash 42a5f304... equals B_C321/B_C411 metadata; design populations equal the bit populations of 1..2646. Does not: prove the base clauses use gv (static reading), mutate encoder B (no encoder-level negative control), check B_C311 metadata, cross-check the vars line; assumes deterministic B and the same interpreter.
- **a_shape**: Exact structural characterisation of the emitted A family relative to A's inverse map (588 groups x 45+360, no bad shape, no duplicates, total 238140): completeness follows because 45 and 360 are the maximal admissible key counts. Does not independently establish the semantic meaning of A's map (rests on gram_enc.build = k3_cubes.variable_map) and does not cover any CNF.
- **b_coverage_positives**: C1: on the 2100 disjoint local assignments with every square nonempty, exactly the 450 of type (4,1,1)/(3,2,1) are rejected; spec = template. Five classical triples give (0,0) on the cut clauses only (they violate base G4). Psi(f) gives exactly (2940,0): non-vacuity outside every triple encoding (weight 5 > (W) bound 4; the fixture is not mutually orthogonal). No genuine K3 positive exists; the controls do not test validity of the cuts, which rests on the transport lemma and G1/G2.
- **c_mutations**: Six concrete defect classes are caught for structural reasons (shape_ok false in the five emitted mutants; the mistransported column exclusion raises KeyError on a collinear pair). Not exhaustive; distinct_ok is count-coupled; reasons are not stored.
- **d_invariance**: Set invariance under the exact k3_lex.image sigma for all 22 generators and under transposition; removing one clause breaks invariance for some generator. Logically implied by the uniform definition plus (a); does not replace the mathematical argument.
- **e_ab**: The in-process B decode equals A's map (the only non-tautological datum; weaker than the oracle). Block-SHA and set equality are tautological given equal maps; the swapped-map SHA difference only shows SHA sensitivity. Not an independent cut implementation.

## Snapshot and hash manifest
- `snapshot/manifest.json` sha256 `4b563226b6e06655ae250cdba8b99cbbb13950832b001fe55baa6778d48c63fb`. Pinned from 2026-10-18T01:17:18-07:00; 71 files; 305,166 bytes excluding the manifest. `lane/` and `parent/` copies are byte-identical; `prior/` holds line-numbered findings-only excerpts.
- Assignment pins (all match):
  - `lane/review/drafts/AMENDMENT-4.r1.md` `ef87fa492abcc9a86e02be9d8f14f7810908a83458b32e38788f99f3acc5abb1` (source mtime 2026-10-18T00:53:17-07:00)
  - `lane/code/k3_cuts_r1.py` `0ec92c861024a728aa38d238fda2d7f5f056fae12cb0f474a15db0335b6e1b0a` (source mtime 2026-10-18T01:00:20-07:00)
  - `lane/review/AMENDMENT-4.GENERATOR.r1.json` `4c23ec44b7189e9df9fd36b39ee2d0a1e62e71bc02bdfd73ff49ab194ac65dd3` (source mtime 2026-10-18T01:00:53-07:00)
  - `lane/evidence/k3cubes/cuts_r1_receipt.json` `9cfc0e81bed2cbcbdcd2c205d697dc107b184609f722f0f799225e39092babbf` (source mtime 2026-10-18T01:02:16-07:00)
  - `lane/review/K3-Q4-SIDECAR.r1.json` `34bb5251ce27e8c112c690fe2d6acec162f33d0e404251af5e54aff9cf3d16e5` (source mtime 2026-10-18T00:51:42-07:00)
  - `lane/review/K3-ERRATA.r1.md` `85fa93fadaa636949c1c8c26672744833f8a42bc4ddd73d6328343eeeb47c662` (source mtime 2026-10-18T00:52:14-07:00)
  - `lane/evidence/k3cubes/bmap_oracle_r1.json` `6e2bd95ee38c615ab2a1a6282531da730b2bf0cc45e104e95b850102e0b1952c` (source mtime 2026-10-18T00:49:40-07:00)
  - `lane/code/bmap_oracle_r1.py` `13f4a5e6c34b61478fcdbb5fddc1a934901c1b82480553cfee8b0f958f73cd8e` (source mtime 2026-10-18T00:48:11-07:00)
- Parent pins (all match):
  - `parent/moqls7-k1-parent-verdict.md` `1cd0603c5dc3e5d724725388de6f9130721c3b686bda3b6ebde765a53dd7dfb8`
  - `parent/moqls7-k2-parent-verdict.md` `25ecb6bab8caad2a7e9c79faa8fbf8d2f34befab8c000338d8d14d63df811242`
  - `parent/moqls7-k3-cover-parent-disposition-v1.md` `fbfc0e1079cd94bcca65a9d1c68ef9f4ac545181d7f9f8bed02feb244aaff369`
- Prior excerpt sources: desk RESULT `0f80460c…ef84`, Codex note `42392eaa…8809`, Claude note `7ab7de84…79b3`.
- Further desk-observed mtimes, not attestations, relevant to Q1(f) and missing from the Claude packet:
  - `K3-BMAP-ORACLE.r1.json` 00:49:12; `k3_direct_B_r5.py` 00:48:48.
  - `k3_cube_certify_r2.py` 21:38:35; `K3-CERTIFICATION-DRIVER-DELTA.r2.json` 21:39:40.
  - lex metadata 21:20:58; lex controls 21:20:47; AMENDMENT-3 bindings 21:21:50.
- Inputs:
  - Codex prompt `36986a354e0fa826f42cb78b4889d9355713d95e143b557f536783967b440e88` (14,504 B).
  - Claude prompt `60540bea5261f0bd678932f3a8209c6f944826d7f13d5c73e1dacbcaa85c3550` (240,394 B; 46 inlined blocks).

| Artifact (R/) | SHA-256 | Bytes |
|---|---|---|
| `moqls7-amendment4-codex-v1.note.md` | `970430f7b51cbd6b987fc2e101844baa9a39fb2bf653f8a03c120674f0c02601` | 21,684 |
| `moqls7-amendment4-codex-v1.prompt.txt` | `36986a354e0fa826f42cb78b4889d9355713d95e143b557f536783967b440e88` | 14,504 |
| `moqls7-amendment4-codex-v1.receipt.json` | `b7b511721e673ebb100657f29432e10f9a7736c1108410d96a1669be7dab9025` | 790 |
| `moqls7-amendment4-codex-v1.stderr.txt` | `e9bef67beeb5738dbc11f64dfc52ce34735eeec1deb19fdb49838627ae5f0cfd` | 432,678 |
| `moqls7-amendment4-codex-v1.stdout.txt` | `9de2bfd7ce30898fbc9b148e42d978e208c4f9ffa4f7a0a432f37cb28ab855bf` | 21,685 |
| `moqls7-amendment4-claude-v1.note.md` | `dc66f3c118ad61f2bb966a31f127570bc83f68d44ce778a9be77d982e3de364a` | 24,005 |
| `moqls7-amendment4-claude-v1.prompt.txt` | `60540bea5261f0bd678932f3a8209c6f944826d7f13d5c73e1dacbcaa85c3550` | 240,394 |
| `moqls7-amendment4-claude-v1.receipt.json` | `b096fb1a4bf9a7fc01db6f63f96c0a24334945f7aa8e8c53bab76f6cb5e50043` | 1,151 |
| `moqls7-amendment4-claude-v1.stderr.txt` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | 0 |
| `moqls7-amendment4-claude-v1.stdout.json` | `62a68920a22ab41f72d0b9810a64f51fc39d1bca58c5aa62b665082c051721e5` | 1,141,466 |
| `moqls7-amendment4-review-v1/checkpoint-01.json` | `4de992f985cfa9cbc74712b23d2ef101188e3efdcf5e07c5dd9c185993370f90` | 1,269 |
| `moqls7-amendment4-review-v1/checkpoint-02.json` | `47198dde4a6112e4f2d76ef3213bb5f2a75272968952b3451ca92b5c55d96647` | 1,219 |
| `moqls7-amendment4-review-v1/checkpoint-03.json` | `69a754d8e488735f1cdc0b5e469ee10ab76a411ff6bd1c37dc76b49bbba40da0` | 876 |
| `moqls7-amendment4-review-v1/claude-run-provenance.json` | `32bf9e5a20a0593192a76328fdaaae71309743d83fe1ce47d37f5c03ccd94412` | 215,687 |
| `moqls7-amendment4-review-v1/codex-command-provenance.json` | `a3a2a3a81b29448ea4797ced3fffa18a1ac3f9515b1b752e718d9fe47b2f0fbf` | 16,238 |
| `moqls7-amendment4-review-v1/desk-analysis.md` | `e1a737446bb2e8337f35ae3f0828fca002ab46c88379c2fb94e46f72192dc8d7` | 5,743 |
| `moqls7-amendment4-review-v1/desk-log.jsonl` | `f1f6f7c73a1f7f06ec7357e6486d8403886accb154e5ac1e7f39f84a8d995b83` | 179,298 |
| `moqls7-amendment4-review-v1/RESULT.json` | `50f4c4fafa0aad9fd6da45092683e0ccc995f4c3d95c9c65076b49d9b589bc23` | 41,588 |

## Resources and timeline (host clock, PDT)
- 01:16:53 desk created. 01:17:55 snapshot pinned.
- 01:18:58 Codex gate PASS (15,703,236,608 B ≥ 12.2e9 + 10 MiB). Codex ran 01:18:58–01:30:14.
- 01:20:49 Claude gate PASS (15,679,115,264 B). Claude ran 01:20:49–01:58:26.
- Checkpoints at 01:21:00, 01:31:33 and 02:01:26. 02:03:12: 15,320,014,848 B free.
- New data before the RESULT files: 4,102,701 B (limit 20 MB), including ~2.7 MB of Codex CLI Node cache in `tmp-codex/`.
- No solver, encoder, checker, generator or oracle launch. No retry was needed.

## Deviations
- Claude prompt Q1(f) mentions manifest source_mtime_pt values that were not inlined in its packet; Claude reported it could not check them (note LF164, LF290). The prompt is exclusive-create and was not rewritten; the desk supplies the mtimes in RESULT.md.
- The Claude packet omitted K3-DIRECT-B-DELTA.r4.json, cert_B_r4/B_C321.json, the A_C321/A_C411 cube metadata, k3_cube_certify_r3.py, k3_direct_B_r5.py and excerpted others; Claude declared them unchecked. Codex read the full snapshot.
- Claude used 2256.9 s of the runner's 2400 s cap (completed; no timeout, no retry).
- tmp-codex holds 561 Node compile-cache files (~2.7 MB) written by the Codex CLI runtime because TMPDIR pointed there, plus an empty .tmpacVj2z directory; tmp-claude is empty. Nothing was written outside the desk.
- claude-run-provenance.json and one desk-log.jsonl line carry all 1780 Claude system events (thinking-token notices) because the init-event extraction was unfiltered; append-only, not rewritten.
- The snapshot includes the parent K2 verdict (needed for Q1(c)), which summarises the K2 proof route; no parent AMENDMENT-4 derivation or numerical smoke was supplied. prior/ held findings-only excerpts for the delta audit.
- Codex shasum used a zsh glob qualifier (lane/**/*(.)); static.

## Desk files
- `snapshot/`: inputs.
- `desk-analysis.md`: desk readings D1–D14, written while the reviewers ran and not shown to them.
- `codex-command-provenance.json` and `claude-run-provenance.json`.
- `checkpoint-01/02/03.json`.
- `desk-log.jsonl`: append-only.
- `RESULT.json` and this file.
- `tmp-codex/` (Codex CLI runtime cache) and `tmp-claude/` (empty) were the reviewers' TMPDIRs.
