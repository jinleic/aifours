DISPOSITION: ACCEPT-WITH-FIXES

This note is advice only. It is a static reading of the inlined packet, with no execution. It gives no K3 verdict, no M(7) value, and no novelty or priority statement. prior/ is used only in the delta table.

## FATAL
None. As read, the transport, the cut family, the generator emission and the oracle decode are sound. The defects below concern bindings, acceptance standards and wording.

## MAJOR

**M1. The strengthened-CNF half of the §3 spec is unimplemented, and no appender or certification driver exists.**
- **Spec.** `lane/review/drafts/AMENDMENT-4.r1.md:69-71` says the generator binds "its output SHA, the source cube CNF SHA, its own code SHA and the clause counts", and must stream or gate the strengthened CNF.
- **Implementation.** `lane/code/k3_cuts_r1.py:292-319` never opens any C311 CNF. The receipt binds only an in-memory block SHA (`lane/evidence/k3cubes/cuts_r1_receipt.json:26-32`). "nv unchanged; nc += 238140" (`:31`) is a string that no code implements.
- **No existing driver fits.**
  - `lane/code/k3_cube_certify_r2.py:31-33,49-50` requires an UNSAT screen and SHA equality with an existing cube CNF.
  - `lane/review/K3-CERTIFICATION-DRIVER-DELTA.r3.json:9` certifies only an "already-present search input".
- **Correction.** Split §3 into two parts:
  - (i) the block generator, as implemented;
  - (ii) a new pinned appender plus driver delta. It must regenerate the named C311 input in memory (the r3 method) and assert its SHA. It must re-emit the block and assert `05f31da4…e6dd`. It must write the header, bind the strengthened SHA, and either stream to the solver or count the file in the gate.
- **Header expectations.** These are derived from bound values. They are to be asserted, not taken as evidence.
  - A original: `p cnf 96978 865696` (`lane/evidence/k3cubes/bmap_oracle_r1.json:135-136`; `lane/explore/k3cubes/A_C311.meta.json:46`).
  - A lex: `p cnf 107513 897308` (`lane/explore/k3lex/A_C311.meta.json:77-78`).
  - B original: `p cnf 461370 1867942` (`bmap_oracle_r1.json:140-141`; `lane/explore/k3cubes/B_C311.meta.json:46`).

**M2. The acceptance standard is left open, in tension with Phase C, and the B inputs are unnamed.**
- **Draft.** `lane/review/drafts/AMENDMENT-4.r1.md:26` allows "A-route only", and `:87` says "route(s)". `:24-25` and `:84-85` name only A CNFs.
- **Protocol.** `lane/README.md:80-81` requires "two encodings" for the complete negative direction.
- **B inputs that exist.**
  - B_C321 `8b7b8124…12c6` (`lane/explore/k3cubes/B_C321.meta.json:5`).
  - B_C411 `01acf464…8bf8` (`B_C411.meta.json:5`).
  - B_C311 `b3ec0108…c077` (`B_C311.meta.json:5`).
- **Gaps.** No B lex C311 exists, and the oracle never reads B_C311 (`lane/code/bmap_oracle_r1.py:115`).
- **Correction.**
  - Fix one standard for C321, C411 and C311+cuts alike: either A+B per README:80-81, or a deviation that the parent records.
  - Under A+B, name the B hashes in G1, G2 and §5, and bind B_C311 to the oracle.
  - If A uses lex C311, state that B uses the original C311, or generate and bind a B lex input under AMENDMENT-3.

**M3. README §0.5 compliance is not addressed.**
- **Rule.** `lane/README.md:91` says every necessary-condition encoding must admit all matched genuine controls before production.
- **Why it cannot be met literally.**
  - The cuts are not a necessary condition for MOQLS in general.
  - They necessarily reject the published non-classical Ψ(f), which has weight 5 at all 588 frame/point pairs (receipt `:76-89`).
  - The only admitted genuine controls are classical triples (`:54-75`), and those violate base G4.
  - No genuine K3 positive exists.
- **Current state.** The receipt labels this honestly (`:91`), but the draft is silent.
- **Correction.** The frozen version should state that the cuts are derived conditional clauses, valid only under H1–H5 and G1–G2, and that README:91 is met only in this restricted sense. It should also obtain an explicit parent ruling, as was done for an earlier README:91 deviation (`parent/moqls7-k2-parent-verdict.md:52`).

## MINOR

**m1.** `lane/review/K3-Q4-SIDECAR.r1.json:40` has two errors.
- It says AMENDMENT-2 "did not state the K2 half". That is false: `lane/review/AMENDMENT-2.r1.md:5-6` names "the K1/K2 exclusions".
- "G4 … holds … only when the triple minimises" overstates. Read "G4 is justified only for minimal triples".

**m2.** `lane/review/K3-ERRATA.r1.md:60` and `K3-Q4-SIDECAR.r1.json:47` say "r1 pointed G4 at K1 §8".
- r1's own G4 paragraph does not support this. `lane/review/GRAM-ENCODING.r1.md:45-55` is verbatim the minimality argument of r2:52-62.
- The K1 §8 pointer is the code comment `lane/code/gram_enc.py:15-16`, which is so named at `GRAM-ENCODING.r2.md:26-27`.
- Correction: the repoint adds r2:63-65 (existence of the minimum; K1 §8 unused) and `LEMMAS.md:54-78` (simultaneous preservation of every partner).

**m3.** `K3-ERRATA.r1.md:22-23` and `lane/review/K3-BMAP-ORACLE.r1.json:10` say "both B cube metadata files", but three exist.
- The base hash 42a5f304… recorded at `B_C311.meta.json:4` equals `bmap_oracle_r1.json:142` only statically. The oracle never reads B_C311.
- Reword, and bind B_C311 (`bfa298ee…`) before any B/C311 use.

**m4.** Labelling and support for sidecar bindings 1 and 2:
- Binding 1 (`K3-Q4-SIDECAR.r1.json:2,6-22`) was recorded at 00:51:30, after the lex screens ended at 23:47:55 (`lane/explore/k3lex/screenA_r2/A_C311.json:6`). It is post hoc but is not labelled so. Add: "post-hoc provenance, not the pre-search binding of AMENDMENT-3.r1.md:46".
- The `:31` chronology rests on desk mtimes that are absent from the snapshot. The only in-snapshot support is the self-reported frozen_at (`K3-CERTIFICATION-DRIVER-DELTA.r2.json:2`) against the start time (`lane/evidence/k3cubes/cert_r2/A_C321.json:2`).
- No receipt names the delta; the only link is the driver SHA (`:47`).
- `:25` ("never used for a production run") is an absence claim that cannot be verified.

**m5.** Qualifiers missing from the K2-prerequisite statements:
- `K3-Q4-SIDECAR.r1.json:43` and `K3-ERRATA.r1.md:73` say the prerequisite is "met". That should carry the verdict's qualifiers: computer-assisted, "conditional on the trust base and the provenance caveat", and "not a new gate" (`parent/moqls7-k2-parent-verdict.md:3,7,54,59-62`).
- `K3-ERRATA.r1.md:67-68` asserts that a parent replay is in progress without citing any parent record.

**m6.** `lane/review/AMENDMENT-4.GENERATOR.r1.json:3`: the authority rests on a parent label of 01:12, which is later than the pin (`:2`, 01:00:31) and the run (receipt `:2`, 01:00:59).
- "Host clock at receipt was before 01:00:31" is a worker attestation with no host record. It is disclosed at `lane/evidence/LOG.md:167`.
- Record the message identifier or hash, and treat 01:12 as a label only.

**m7.** The generator's B decode (`lane/code/k3_cuts_r1.py:238-256,298`) is weaker than the oracle's.
- It omits the header check (`bmap_oracle_r1.py:137-138`), the base-prefix check (`:139-144`) and the sign controls (`:168-171`).
- It hashes the oracle receipt but checks neither its status nor its pins.
- The docstring at `:9`, "(as in the B-map oracle)", overstates.
- Fix: assert receipt PASS and pins (as r5 reportedly does, `K3-BMAP-ORACLE.r1.json:15`), or replicate the oracle's checks.

**m8.** Once `B_map_equals_A_map` holds, two of the receipt's checks are tautological (`cuts_r1_receipt.json:166-169`).
- `block_sha_equal` and `sets_equal` follow from the same `emit` with the same map.
- The swap test shows only that the SHA is sensitive to the map.
- Label them as such; E1 makes exactly this point for cube blocks (`K3-ERRATA.r1.md:15-16`).

**m9.** `distinct_ok` includes the count (`k3_cuts_r1.py:171-172`).
- So `distinct_ok: false` for `at_most_four…` and `one_clause_dropped` (receipt `:110-119`) is count-driven, not a distinctness failure.
- The reason each mutation was caught is not recorded (`:357-359`). Store the full `shape_report` for each mutation.

**m10.** The interpreter path and version are unrecorded (`k3_cuts_r1.py:292-299`; `bmap_oracle_r1.py:87-91`).
- The import hashes assume `sys.path[0]` is `code/`, since `-I` was not used.
- Record `sys.executable`, `sys.version` and each imported module's `__file__`.

**m11.** H3 and §6 need firmer statements (`AMENDMENT-4.r1.md:16-18,91-92`).
- H3 names no parent file that accepts the K3 instantiation: three quantum squares, no L, G4 on all lines, `--sym`. The K2 verdict accepts Gram r2 as G1–G5 for K2 (`parent/moqls7-k2-parent-verdict.md:17,21`).
- State H3 as encoder soundness for the exact K3 base.
- In §6, add auxiliary reconstruction (A: h and guards; B: counters; lex: prefixes) and per-encoder soundness for base∧cube∧(lex)∧cuts.
- H5 is needed only in §6.

**m12.** Make the transport steps explicit (`AMENDMENT-4.r1.md:40,45-47,51,53`).
- Say that the transpose acts on all three squares simultaneously.
- Write each contradiction as "with reconstructed auxiliaries, satisfies the exact CNF 2b92f5b1… (B_C411 01acf464… under A+B)", and likewise for C321.

**m13.** Version naming and the draft binding:
- `AMENDMENT-4.r1.md:8` calls the retired interim draft "AMENDMENT-4.r2.md". The frozen successor must not reuse r2, and should bind the archive path and SHA (`LOG.md:160-161`, e72233ca…2870).
- The receipt binds draft ef87fa49 (`cuts_r1_receipt.json:15-18`). A revised draft needs either a re-run or an explicit carry-over binding.

**m14.** `AMENDMENT-4.r1.md:83-98` sets no solver or checker caps, driver, screen policy or RSS limit. The old draft had a screen of at most 1800 s (`lane/review/drafts/AMENDMENT-4.md:61`). Put these in the M1 driver delta.

**m15.** Observation, not load-bearing: both cert_r2 receipts carry the same `solver_log_sha256`, bde6e1ee… (`A_C321.json:32`, `A_C411.json:32`). This is plausibly identical one-line quiet output. The parent replay should confirm it.

## Checks passed (no finding)

**Q1(a).** Every SHA and status in `K3-Q4-SIDECAR.r1.json:8-19` matches both the file headers and the in-file values:
- `lane/explore/k3lex/A_C311.meta.json:4-7`;
- `lane/explore/k3cubes/A_C311.meta.json:5-6`;
- `lane/explore/k3cubes/screenA_r1/A_C311.json:4,7,16-17`;
- both lex screens at `:4,7,16-17,22`;
- `AMENDMENT-3.bindings.r1.json:4,6,8,14`;
- `lex_controls_r1.json:264`.

The lex counts are consistent: 31612 = 6·4156 + 6676, and 10535 = 6·1385 + 2225 (3n−2 clauses and n−1 prefixes per generator, `k3_lex.py:54-69`). In substance the sidecar binds every item that AMENDMENT-3.r1.md:46 lists, but post hoc (m4).

**Q1(b).** The delta, driver, transport and receipt SHAs, the 3600/3600 caps (`k3_cube_certify_r2.py:51-53`; receipts `:8-9,17-18`) and the start times all match the sidecar (`:26-29`). The r3 and oracle SHAs also match. The r4 delta is not inlined.

**Q1(c).** The K1 and K2 SHAs, dispositions and times match. The line ranges r2:52-65 and LEMMAS:69-78 are exact. Minimality follows (`LEMMAS.md:70-71,75`). The K2 verdict (`:5-6,64`) meets the prerequisite in scope.

**Q1(d).** Encoder B's pair-to-index map is observed directly, not echoed from A.

What the code does:
- B allocates gv first (`gram_encB.py:113-118`), in the same order as `k3_cubes.py:62-65`.
- Every base literal goes through `g()`/`gv` (`:120-123,127,145,166,177,185-187,193,200`).
- The fix branch runs after all base clauses and signs one unit per gv key (`:203-215`).
- The dump closes `/dev/stdout` before the `vars` print (`:34-38,216-217`).
- The oracle parses the header, nc clauses and the `vars` line. Its prefix check (`:139-144`) proves that `--fix-json` changes no base byte.

Why this proves the map:
- After 12 designs, codes[v] is the A-index of B's own pair at v.
- codes[v] = v (`:172`) together with A being a bijection (`:100`) gives B-pair(v) = A-pair(v).
- The all_nonzero control puts every gv key in A's domain.
- The design counts equal the bit populations of 1..2646 (for example, bit11 gives 599 and bit9 gives 1111).

Assumptions:
- (A1) Base clause builders use only gv (static reading).
- (A2) B is deterministic across processes.
- (A3) The stdout layout is as read; the `vars` counts are not cross-checked.
- (A4) Production base bytes equal the oracle's. This is checked for C321 and C411 only (`bmap_oracle_r1.json:144-154`); for C311 it holds only statically.
- (A5) The same interpreter is used.

The comparator self-tests are correctly labelled (`:185`; receipt `:161`). There is no encoder-level negative control.

**Q1(e).**
- E2: 109 = g₁((0,3),(1,0)) and 145 = g₁((0,4),(1,0)) are correct.
- E3 matches `k3_lex.py:49,59,120`.
- E4 is the G3 condition for column 0 against row 0.
- E5 matches `GRAM-ENCODING.r2.md:42`.
- E7 is correct, but it lacks the B hashes (M2) and its replay claim is unsourced (m5).

**Q1(f).** By the recorded labels, the oracle was pinned at 00:48:54, before it ran (00:49:18–00:49:40). The generator was pinned at 01:00:31, before it ran (01:00:59–01:02:16).
- The sidecar, errata and draft (00:51–00:53) all postdate the K2 verdict (00:42:18) and the parent notice (00:46).
- Nothing relies on cert_B_r4 (sidecar `:34`; errata `:23-24`).
- No document presents a post-hoc binding as preregistered.
- Pin times are worker labels; receipt times come from the host clock. No manifest mtimes were provided.

**Q2.** The transport checks out for all 14 frames, all 42 off-line points and every assignment of roles.
- **Excluded cell.** The frame cell that shares p's other line goes to (0,0). For a row frame, (k, p₁) maps to (0,0). For a column frame, (p₀, k) maps under the transpose to (k, p₀) and then to (0,0). G1 excludes it.
- **Columns and literals.** The columns account for 1+4+1+1 = 1+3+2+1 = 7. All 18 literals are determined, because the three neighbour sets partition the six positions.
- **Roles.** In (4,1,1) the order of b and c is free. In (3,2,1) it is forced.
- **Constraints.** The `--sym` units hold. All G1–G5 and G4 constraints, including (1, row 0), hold by H2 and by invariance under three operations:
  - row and column permutations;
  - simultaneous transposition of all three squares (one cell bijection reindexes the tensor ONB; rays are unchanged);
  - relabelling of squares.

  G6 holds by `G6-G2-DERIVATION.r1.md`.
- **Counting.** w ≥ 1 by unit norm (Boolean G3), with G1 applied at the excluded cell. G5 applies to every pair (p, r) with r on ℓ, so the three neighbour sets are disjoint and the counts sum to at most 6. That forces type (4,1,1) or (3,2,1).
- **Heavy.** "Heavy" means at least 3 neighbours, which is G4's threshold (`gram_enc.py:131-136`).
- There is no overreach and no circularity, and no UNKNOWN is used as a premise.

**Q3.** The generator emits exactly the specified family.
- `positions()` drops exactly the collinear frame cell (`:67-71`).
- There are 42 points per frame and 405 template clauses per point; 588·405 = 238140.
- Clauses are distinct across groups, because four or more distinct frame cells fix both p and the frame line.
- Keys are normalised to A's p<q keys (`gram_enc.py:149`).
- The decode inversion is correct (`:274`).
- Clauses are emitted in canonical order, and the byte count is consistent.
- The pins and self-hash match (`AMENDMENT-4.GENERATOR.r1.json:6-8`; receipt `:10-19`).
- The gate check and exclusive output writes are correct, and no CNF is written.

**Q4.** The controls check out.
- 4⁶ − 3·3⁶ + 3·2⁶ − 1 = 2100 local assignments. The forbidden ones number 3·30 + 6·60 = 450.
- The spec equals the template, and `shape_report` shows the emitted family equals the spec at every (frame, p). So the chain from spec to emitted family is complete.
- `psi_gram` is the Gram support of ψ(i,j) = 7^{-1/2} Σ_x ω^{i f(x)+jx} e_x. f₀ + s·x is a permutation exactly for s ∈ {1,5}. So m₀ = 2, every own-line weight is 5, and the expected count is (2940,0).
- Whether this is exactly the source's Ex. 15 cannot be checked from the packet.
- Each mutation is caught for a structural reason, not only by count.

**Q5.** The uniform family is invariant under the full row × column × square group, so it is invariant under H regardless of E2. Invariance is not even needed:
- every member of an H-orbit is the Gram pattern of an actual K3 configuration, and the cuts are valid for every K3 configuration;
- so the lex-minimal member satisfies base∧cube (by E2), the lex clauses and the cuts.

## Freeze, use and acceptance conditions (Q6). None is met at pin time.

1. **Exclusions.** Parent verdicts accepting the exclusion of the exact C321 (`d598507d…8388`) and C411 (`2b92f5b1…ddf2`) CNFs, each stating its standard. Under A+B they must also name B_C321 and B_C411.
   - A-only needs a parent-recorded deviation from README:80-81.
   - Status: parent replays are running, B/C411 has not started, and nothing is accepted (`parent/moqls7-k3-cover-parent-disposition-v1.md:18`).
2. **K3 bridge.** A parent statement accepting the K3 instantiation of the encoder bridge (m11). This may form part of item 10.
3. **C311 instance.** Name the instance: A original `7fca33f1…` or A lex `059be616…`. For B, only the original `b3ec0108…` exists. Bind B_C311 to the oracle.
4. **New frozen version.** A new frozen version of the draft (not named r2), containing M1–M3 and m11–m14. Its bindings must cover:
   - the draft SHA;
   - generator `0ec92c86…` and receipt `9cfc0e81…` (or a re-run);
   - block `05f31da4…` and oracle receipt `6e2bd95e…`;
   - the K1, K2, G1 and G2 verdicts;
   - the chosen instance or instances;
   - the appender and driver SHAs.
5. **Missing code.**
   - An appender and driver delta (M1), with per-encoder literal maps and oracle-level checks for B (m7).
   - The strengthened CNF must be generated in memory per r3, or written once and counted in the gate.
6. **Missing pre-solve controls.**
   - A segment check on the appended bytes: 238140 clauses whose bytes hash to `05f31da4…`.
   - Header equality with the expectations in M1.
   - C1–C4 re-bound to the frozen draft.
7. **Resources.** A fresh gate per stage, the 12e9 floor, specified caps (m14), and a single solver+checker pipeline.
8. **Certification.** A newly regenerated, DRAT-checked UNSAT of each exact strengthened input on the route(s) of the chosen standard, with solver rc 20, checker rc 0, an exact `s VERIFIED` line and no safety stop. Old proofs are not transferred (`AMENDMENT-4.r1.md:86`).
9. **Replay.** A parent replay of those certificates.
10. **Composition review.** A parent review of the full §6 composition, including auxiliary reconstruction, the residual-symmetry step of the cover, and the lex-representative step if lex is used.

## Status by question

| Q | Status | Reason |
|---|---|---|
| Q1 | FIX-REQUIRED | Oracle sound and every SHA/status matches; sidecar and errata need factual fixes (m1–m5), and B_C311 needs binding |
| Q2 | FIX-REQUIRED | Transport sound for every frame, point and role; standard and B hashes (M2) and H3 statement (m11–m12) |
| Q3 | FIX-REQUIRED | Emits exactly 238140 distinct clauses; source-CNF binding, header and appender unimplemented (M1); B decode weak (m7) |
| Q4 | CONDITIONAL | Controls establish what they claim; README:91 status needs a parent ruling (M3); labels (m8–m9) |
| Q5 | CONDITIONAL | H-invariance holds and is not needed; composition sound given G1/G2, a certified strengthened input and the m11 steps |
| Q6 | CONDITIONAL | No listed condition is met |

## Prior findings

| Prior id | Status | Evidence |
|---|---|---|
| Desk MAJOR 1 | CLOSED (post hoc, m4) | lane/review/K3-Q4-SIDECAR.r1.json:6-22 |
| Desk MAJOR 2 | CLOSED | lane/review/drafts/AMENDMENT-4.r1.md:11-21 |
| Desk MAJOR 3 | CLOSED (standard open, M2) | lane/review/drafts/AMENDMENT-4.r1.md:23-28,47,51 |
| Desk MINOR B map (LF73) | CLOSED (m3 residual) | lane/review/K3-ERRATA.r1.md:8-24; lane/evidence/k3cubes/bmap_oracle_r1.json:156,163 |
| Desk MINOR invariance (LF77) | CLOSED | lane/review/K3-ERRATA.r1.md:26-36 |
| Desk MINOR T(X) (LF80) | CLOSED | lane/review/K3-ERRATA.r1.md:38-44 |
| Desk MINOR wording (LF81-84) | CLOSED | lane/review/K3-ERRATA.r1.md:46-56 |
| Desk MINOR stale binding (LF85) | CLOSED | lane/review/K3-Q4-SIDECAR.r1.json:24-31 |
| Desk MINOR chronology (LF88) | OPEN | not recorded in lane/review/K3-ERRATA.r1.md:1-75 or lane/review/K3-Q4-SIDECAR.r1.json:1-55 |
| Desk MINOR dependency (LF93) | CLOSED (m1, m2) | lane/review/K3-ERRATA.r1.md:58-60,70-74 |
| Desk MINOR status wording (LF96) | CLOSED | lane/review/K3-ERRATA.r1.md:62-68 |
| Desk MINOR AMENDMENT-4 polish (LF97) | PARTIALLY-CLOSED (instance unnamed) | lane/review/drafts/AMENDMENT-4.r1.md:1,30,34,39-51,77-85 |
| Desk non-issue (LF104) | NOT-APPLICABLE | prior/prior-desk-RESULT.findings-excerpt.md:LF104 |
| Codex M1 | CLOSED | lane/review/K3-Q4-SIDECAR.r1.json:6-22 |
| Codex M2 | CLOSED | lane/review/drafts/AMENDMENT-4.r1.md:11-28 |
| Codex m1 | CLOSED | lane/review/K3-ERRATA.r1.md:26-36 |
| Codex m2 | CLOSED | lane/review/K3-ERRATA.r1.md:8-24 |
| Claude D1 | CLOSED | lane/review/drafts/AMENDMENT-4.r1.md:11-21 |
| Claude D2 | CLOSED (M2) | lane/review/drafts/AMENDMENT-4.r1.md:23-28,47,51 |
| Claude m1 | CLOSED | lane/review/K3-ERRATA.r1.md:46-49 |
| Claude m2 | CLOSED | lane/review/K3-ERRATA.r1.md:8-24; lane/code/bmap_oracle_r1.py:162-176 |
| Claude m3 | CLOSED | lane/review/K3-ERRATA.r1.md:51-56 |
| Claude m4 | CLOSED | lane/review/K3-ERRATA.r1.md:30-36 |
| Claude m5 | CLOSED | lane/review/K3-ERRATA.r1.md:38-44 |
| Claude m6 | CLOSED | lane/review/K3-Q4-SIDECAR.r1.json:8-11 |
| Claude m7 | CLOSED | lane/review/K3-Q4-SIDECAR.r1.json:25-31 |
| Claude m8 | OPEN | lane/review/AMENDMENT-3.r1.md:3 vs lane/review/AMENDMENT-3.bindings.r1.json:2,14; no erratum |
| Claude m9 | CLOSED (m1, m2) | lane/review/K3-ERRATA.r1.md:58-60,70-74 |
| Claude m10 | CLOSED | lane/review/K3-ERRATA.r1.md:62-68 |
| Claude m11 | CLOSED | lane/review/drafts/AMENDMENT-4.r1.md:1,30,54-58 |
| Claude m12 | CLOSED | lane/review/drafts/AMENDMENT-4.r1.md:39-51 |
| Claude m13 | CLOSED | lane/review/drafts/AMENDMENT-4.r1.md:34 |
| Claude m14 | PARTIALLY-CLOSED | lane/review/drafts/AMENDMENT-4.r1.md:77-85 |
| Claude m15 | NOT-APPLICABLE | prior/prior-desk-RESULT.findings-excerpt.md:LF104 |

## Control limits
- **(a)** Establishes that the A-indexed emitted family equals the uniform 588×(45+360) spec, with distinct clauses and only negative literals. It does not check literal meaning independently of A's inverse map, and it does not cover the B block or any CNF.
- **(b)** Establishes that spec equals template, that the local rejection set is exact (450 of 2100), that classical triples are admitted and that Ψ(f) is rejected as predicted. It provides no genuine K3 positive and does not test the validity of the cuts.
- **(c)** Establishes that six defect classes are caught for structural reasons. It is not exhaustive, and it does not record the reasons.
- **(d)** Establishes closure under the exact σ of `k3_lex.image` for 22 generators and under transposition. This is logically implied by (a). Its non-vacuity check removes only one clause.
- **(e)** Establishes that the in-process B decode equals A's map. The block and set equalities are tautological given that, and the decode is weaker than the oracle.
- **Oracle** Establishes that B's fix-branch map equals A's map for all 2646 variables, and that `--fix-json` is append-only. That the base clauses use gv rests on static reading. There is no encoder mutation control, and B_C311 is unchecked.

## Scope
Read: every inlined file, verbatim or as excerpted, and prior/ for the delta table only.

Could not check:
- any CNF or proof bytes;
- manifest mtimes and `source_mtime_pt`;
- K3-DIRECT-B-DELTA.r4.json, k3_direct_B_r5.py, k3_cube_certify_r3.py and proof_stream.py;
- the full lex_controls_r1.json;
- the Ball–Simoens Ex. 15 text;
- any parent replay status.

Nothing was executed.
