# moqls8 unified one-P4 bridge repair — static delta audit v1 (RESULT)

**Delegated disposition: DELTA-ACCEPT-WITH-FIXES.** This is not a theorem verdict; the parent decides.

- Target: OVL = `LANE/review/N8_UNIFIED_REVIEW_REPAIRS.r1.md`, SHA-256 `e0f3c860aaa81dd7b8214aabb84f5094fcaf425a6a17a01159d3aa779a9d1704`.
- Path keys: LANE = `physics/evidence/six-lane-20261016/moqls8-problem16`; R = `institute/runs/six-lane-2026-10-16/review`.
- Machine-readable record: `RESULT.json`, SHA-256 `d3eedf783e2104c296bc69cb36d7f92c2bd4f4dee38802ff3290b039250cec8b`.

**Basis.** Codex, Claude and the desk report 0 FATAL and 0 MAJOR. The five consolidated MINORs (F1–F5) are labelling, pinning and binding-documentation fixes. None of them changes a clause, unit, leaf SHA, case or mathematical step, so none blocks spending the 16 refutations pinned in WMAN. F1, F2 and F4 should go into an r2 overlay or a parent note before any result is counted.

## Per-question status

| Q | Consolidated | Codex | Claude | Desk |
|---|---|---|---|---|
| Q1: the 10 Claude MINORs | **Closed in substance; 2 residues** (BR2 m6 → F4, DEL m2 → F1); nothing reopened | CLOSED | PARTIAL (8 closed, 2 partial) | agrees: residues are pin/labelling only |
| Q2: property-form T16 | **PASS-WITH-FIXES**; the mathematics passes; fixes F2a, F3, F5a | PASS | PASS-WITH-FIXES | PASS (pinned enumeration, E2) |
| Q3: canonical extension and deletion safety | **PASS**; wording fix F5b only | PASS | PASS | PASS |
| Q4: byte filter | **PASS-WITH-FIXES** (F1, F2); claim scope correct | PASS (same boundary noted) | PASS-WITH-FIXES | PASS-WITH-FIXES |
| Q5: six gates | **PASS-WITH-FIXES**: sufficient in substance; gates should name F2 and F4 | PASS | PASS-WITH-FIXES | PASS-WITH-FIXES |

**Q2 in brief.** All of the following were checked by reading, from the stated hypotheses only:
- The two degree bounds. In each frame, Prop 1/G2 on cell pairs gives five disjoint nonempty supports among seven available cells.
- The component theorem (TPL:31–55).
- P0/P1/P2 and the 6/6/4 blocks.
- Every canonical choice against the GA:248–270 key: coordinate 0 most significant, False < True, ascending non-strict.

Nothing relies on reduced-K5 membership, on P4 for squares 2–5, on non-classicality, or on the 13-case/c112 interface. The moves σ ∈ Sym(A)×Sym(B), the relabelling s ↦ σ(s+2)−2 and the sort of rows 2–7 preserve alignment, SB2, and rows 0 and 1. No list is missing.

**Q3 in brief.** The stated canonical values satisfy every retained clause:
- G2–G5, the constants, the b3/c4 ANDs, u5 and lexeq (lexeq is the inclusive prefix);
- SB2 and the 42 units;
- the one-way w3 clauses.

w3 occurs positively only in the five ALOs (GA:247). Deleting exactly the four ALOs of squares 2–5 is therefore sound for arbitrary squares 2–5, classical or not, and nothing else is needed.

**Q5 in brief.**
- Classical sets need nothing.
- The A8 premise (all five squares, all entries, weight ≤ 2) plus W8 gives the weight-3 witness; only that square becomes Q1, and squares 2–5 stay unrestricted.
- The consequent is SRC:642 with n−3 = 5.
- No mathematical hypothesis is missing. Only explicit pins are missing (F2, F4).

## Consolidated findings (all MINOR)

**F1 — Producer-path identities are presented as second-path** (Q4; residue of DEL m2).
- Sources: Claude D-m1 and the desk. Codex Q4 notes the same boundary but does not classify it as a finding.
- Lines: OVL:81–86, LINK:19, RCPT:16,18, VER:1,37–42,90,99–100, PROD:31–40,80–81, RECIPE:13–19,46–47.
- Defect:
  - Only the producer's `Formula` class computes these values (PROD:33,38):
    - the F_one SHA `374d6fb4…`;
    - the header bytes `p cnf 509915 5740226\n` and `…5740268\n`;
    - all 16 leaf SHAs.
  - VER re-observes them in the same process: VER:40 compares against a constant, and VER:90 calls `f.leaf_sha`.
  - RCPT:16 and RCPT:18 are string literals (VER:99–100).
  - VER re-reads DEL without re-hashing it (VER:42). It never compares the rebuilt recipe `r` with BASE_RECIPE. RECIPE:46–47 are hard-coded `True`, and VER:1 calls itself "Independent".
  - The checks that are genuinely second-path sit at VER:43–89: the body traversal; the source header, CR and comment checks; the four deleted hashes and the Q1 hash; the name-table domains; and the unit reconstruction.
  - CL1:89 asked for an independently streamed F_one SHA to be pinned beforehand. That was not done.
- Correction:
  - Reword OVL:86 and LINK:19 to say: second-path body traversal and unit reconstruction; header bytes, F_one SHA and leaf SHAs recomputed only by the producer's `Formula`.
  - The gate-5 parent regeneration must recompute sha256(header ‖ retained body ‖ `%d 0\n` units) with an independent implementation and compare it against every WMAN `cnf_sha256`. Alternatively, a VER v2 can do this with its own `hashlib` and also assert sha256(DEL) and RECIPE == r.

**F2 — Two load-bearing identities are checked by no code and named in no gate** (Q2/Q4/Q5).
- Sources: Claude D-m2 and the desk. Codex lists the same items as "not checked by VER/PROD" and checked them itself.
- Lines: OVL:23–24,29–30,105–108, PROD:97–101, VER:65–66,80–89.
- Defect (a): WMAN `supports_row2to7` equal the T16 lists at TPL:88–95/101–104. PROD copies them from SMAN, and VER never reads TPL.
- Defect (b): F = GA(argv), and the map `7b4dd597…` and name table `b8423861…` are bound to F. They are pinned by SHA only, and gates OVL:105–111 do not cite the map meta or the parent binding receipt.
- Current status: there is no mismatch.
  - Codex compared all 16 lists and matched all 7,840 g ids against GA's allocation order.
  - Claude checked the 16 lists, and all 672 unit literals against g₁((0,c),(i,0)) = 49c+7i−6.
  - Desk checks E2, E4, E5 and E3 agree.
- Correction:
  - Add to gate 3 (OVL:108): "WMAN supports_row2to7 = TPL:88–95/101–104 verbatim; unit ids per GMAP 7b4dd597…, whose meta binds cnf 6ecb77a7… and encoder bf1aada1…".
  - Add to gate 1 (OVL:106): "F = GA(argv) and name table b8423861… per parent `binding-result.v2.json` dce638a9… (SEM:96–97)".

**F3 — The TPL excision is incomplete** (Q2).
- Sources: Claude D-m3; the desk concurs.
- Lines: OVL:26–28, TPL:1,4–5,20,59,62–63.
- Defect: OVL excludes only TPL:111–113 and 117–120. These lines still route through reduced-K5/old F:
  - TPL:20: "accepted K5 SB2 normalisation";
  - TPL:59: the reduced-K5 bridge, via IMP:11–14,72–74;
  - TPL:62–63: "All reduced-K5/P4 properties are preserved".
- None of these is needed mathematically.
- Correction: state exactly what T16 uses:
  - TPL:9–19 (line 20's justification replaced by the hypothesis supp Q1(1,0) = A);
  - TPL:22–55;
  - TPL:60–64 as made explicit by OVL:34–38, minus the reduced-K5/P4 sentence;
  - TPL:66–109.
  - TPL:1, 4–5, 59 and 111–131 are not used.

**F4 — Gate 4 does not pin a predicate or checker** (Q5; residue of BR2 m6).
- Sources: Claude D-m4 and the desk. Codex takes the concrete meaning from RM:216–228 and did not audit the runner or checker binaries.
- Lines: OVL:109, RM:216–224, RM:413.
- Correction: require 16/16 receipts that meet RM:222–224 (README as snapshotted, `45b80b2f…`) exactly:
  - both processes self-exited, with no guard trip and no relay error;
  - CaDiCaL exit 20 with `s UNSATISFIABLE`;
  - drat-trim `d834b649…` exit 0, with a line equal to `s VERIFIED` after stripping CR, and no `s NOT VERIFIED`;
  - solver-feed and checker-feed SHA both equal the case's WMAN `cnf_sha256`;
  - proof-stream SHA and byte count recorded;
  - runner `run_n8_one_p4_templates.py` `268e743b…`.
- LRAT-only checker results do not count.

**F5 — Editorial** (Q1–Q4).
- (a) OVL:17–19 says the supports are "aligned" in both frames. In the column-0 frame, disjointness is frame-free (Prop 1/G2 on the cell pair ((0,k),(i,0))). "Prop1" is unpinned; cite SRC:300–302 and ENC:95,134.
- (b) OVL:48 should say "inclusive prefix", v_i[0..k] = v_{i+1}[0..k] (GA:262–269). The value is unique, so Q3 is unaffected.
- (c) OVL:11,93,102 give truncated SEM and PV pins; use the full hashes.
- (d) Missing-space typography fuses hashes with words (e.g. OVL:4 `SHA2566200c8d7…`, OVL:77, OVL:84). The values are correct on inspection but cannot be machine-parsed.
- (e) RECIPE:13–44 lists the Q1 KEEP record under `"removed"`.

**Notes (not findings).**
- N1: T16 (OVL:21–24) could state that the moved set is again a genuine aligned five-set.
- N2: Under SB2, the kept Q1 ALO and every P4 clause are always satisfiable via w3₁(0,(1,0)). F_one plus its units therefore carries no effective P4 strength (CL1:135).

## Q1: the 10 Claude MINORs (CL1:31–75, 83–99)

| MINOR | Status | Where in OVL |
|---|---|---|
| BR2 m1: canonical w3 values | closed | OVL:52–57 |
| BR2 m2: provenance overstated | closed; labelling residue F1 | OVL:61–65, 81–88 |
| BR2 m3: template scope | closed; excision residue F3 | OVL:13–30 |
| BR2 m4: residual action and ρ | closed | OVL:34–38 |
| BR2 m5: no novelty claim | closed | OVL:92 |
| BR2 m6: premises and gates | Codex closed / Claude partial: strict predicate unpinned (F4) | OVL:94–114 |
| BR2 m7: wording and pins | closed | OVL:24, 38, 42–43, 48–50, 99–101 |
| DEL m1: unreceipted claim | closed | OVL:61–63, 81–88 |
| DEL m2: generator obligations | Codex closed / Claude partial: SHAs producer-path only (F1) | OVL:62–71, 81–88 |
| DEL m3: conventions and method | closed | OVL:67–73 |

Nothing was reopened. OVL:35 follows SEM:56–61 rather than IMP:67. OVL:41 follows SEM:78–79. OVL:108 follows SEM:51–52, and the overlay is consistent with CX1.

## Reviewer receipts (both runs returned notes; neither timed out)

| Field | Codex | Claude |
|---|---|---|
| Name (prompt in R/) | `moqls8-unified-delta-codex-v1` | `moqls8-unified-delta-claude-v1` |
| Model / effort | gpt-6.1-sol / max, read-only (reported identity) | claude-opus-5-5 / max, no tools (reported) |
| Status / duration | NOTE_RETURNED_UNVERIFIED / 405.96 s | NOTE_RETURNED_UNVERIFIED / 1103.78 s |
| Prompt SHA-256 | `a7ce7fb97aa20a916653578f71f9147b0b4f97514f3fdfd1a7b3c302f96ed805` | `dd5a269f627bffbd1ee0378a4e674c235219ccd60eeb8f9b32d34bdd8eda33e5` |
| Note SHA-256 | `527c613aeaabf96bee954b9578289b06ec8059c0cdf9650919488ed393261c06` (equals receipt) | `48441d5a4119d4c77dee3da446f6b0f2f832c5976b30968a2056daf243373269` |
| Receipt SHA-256 | `5ea18ab28721bd2652c51452c30b39b2e55a19f7d4809b78b26683df198f441e` | `286e77c0892c27e86c79b9246420d3d06c0885025330f40f6ead3c6adc9915ed` |
| stdout / stderr SHA-256 | `c0faa079…ff1e8` / `01c1ca08…ae37f` | `79b033a5…8335e` / empty `e3b0c442…b855` |
| Disposition | DELTA=ACCEPT; Q1=CLOSED; Q2–Q5=PASS | DELTA=ACCEPT-WITH-FIXES; Q1=PARTIAL; Q2=PWF; Q3=PASS; Q4=PWF; Q5=PWF |
| Tally | FATAL=0 MAJOR=0 MINOR=0 | FATAL=0 MAJOR=0 MINOR=5 |
| Disk gate (free ≥ 12.25e9) | 15,881,224,192 at 01:05:00 PASS | 15,881,240,576 at 01:05:00 PASS |

Runners: `run_codex_note_coop.py` `196fc7f1…ea69` and `run_claude_note_coop.py` `39c5860b…8a9b`. Both prompts were built from the pinned snapshot by `desk/build_prompts.py` `9ed5ac07…c414`, recorded in `desk/PROMPTS_PIN.json`. The Claude packet inlined every text, LF-numbered, with its SHA. The Codex prompt listed snapshot paths and pins, and Codex verified all 21 SHAs. Model notes are unverified model output; this RESULT consolidates them.

## Desk evidence (aids, not proof)

- **E1.** Every task pin matched before the snapshot. The weakened manifest `355b3380…fc74` was located at `LANE/evidence/n8_one_p4_templates_v1/MANIFEST.json`, and the primary text `265851e4…08df9` at `LANE/sources/2607.12933v2.raw.txt`. Snapshot: `SNAPSHOT_MANIFEST.json` `d491bb70…dd6b`, 21 files, 492,989 B, pinned before any review.
- **E2. T16 enumeration** (`desk/t16_enum.py` `8aadd9f5…53bc1`, pinned 01:00:22 before running; result `61d62afb…48b7`). It uses only the T16 hypotheses as necessary conditions: support of column 1 = A, degrees 1–3, no singleton row/column intersections, balanced components.
  - 140 sorted multisets, which is 43,290 labelled patterns. This equals the WMAN/SMAN control and README:362.
  - 16 orbits under Sym(A)×Sym(B) (group order 144), in bijection with the 16 TPL lists; each list is needed (negative control).
  - Only the five component types occur.
  - The TPL lists are ROWLEX-sorted and equal the WMAN supports.
  - Run cost: 0.13 s and 21 MB.
  - Limit: it reuses the same necessary conditions as TPL §2. I checked those by reading, not mechanically.
- **E3. ALO reconstruction** (`desk/alo_reconstruct.py` `1d5d9836…ce71`, pinned before running; result `9a4985cd…60ae`). Working from GA's allocation order alone, with no CNF read: the w3 base is 509600, all five line hashes equal the DEL pins, the indices equal DEL, and the deleted bytes total 1576 = RECIPE:45.
- **E4. GMAP meta.** It binds the argv (as ENC:44–45), 509915/5740230, cnf `6ecb77a7…`, encoder `bf1aada1…`; the row-2 ids 57…351 match IMP:55. Extract: `desk/gmap_extract.json` `5170c95e…496e`, given to Claude as [F].
- **E5. SMAN vs WMAN.**
  - ids, supports and units are identical for all 16 cases;
  - each `old_strong_leaf_cnf_sha256` equals the SMAN `cnf_sha256`;
  - every case has `run_required`=true and `excluded_by_imported_c112`=false.
- **E6. Byte arithmetic.** 137,664,569 − 21 − 1,576 (4×394) = 137,662,972 = RECIPE:12.
- **E7. Timeline.** Mtimes: DEL 23:32:44, BR2 23:33:57, PROD 23:41:38, RECIPE/WMAN 23:42:13, VER 00:03:53, RCPT 00:04:37, OVL 00:06:59, LINK 00:07:47 PDT. This is consistent with OVL §4.

Other desk file SHAs: `desk/snapshot_pin.py` `8531087b…66f7`, `desk/disk_gate.py` `07f2196a…8548`, `desk/write_result_json.py` (listed in RESULT.json).

## Deviations

1. `desk/t16_enum.time.txt` was created by shell redirection (a fresh file), not by an exclusive-open call.
2. `snapshot_pin.py`, `build_prompts.py` and `disk_gate.py` were not hash-pinned before they ran; only the two optional checks were. Their SHAs are recorded here and in RESULT.json.
3. The owned TMPDIR received CLI caches: `tmp/node-compile-cache` (561 files, about 2.7 MB) and an empty `tmp/.tmpSfXxuS`. They were left in place.
4. Codex also read workspace context files (a skill, the READMEs, AGENTS.md probes). All 22 of its commands were read-only, and it never opened the CNF or name table. Its sandbox refused one xcrun cache write to /tmp, so no write occurred.
5. The README was snapshotted as found (`45b80b2f…`) rather than task-pinned.
6. Claude used 126,187 of its 128,000 output tokens. Its note is complete, but a larger packet could truncate.
7. No retry was needed.

## Not claimed

- No Problem 16 / n = 8 verdict.
- No refutation or SAT result.
- No novelty assessment.
- No parent disposition.
- No PROD/VER replay.
- No read of the 137 MB CNF or of the name table.
