# PA(19,8,6) M1 receipt audit v1 (PA19FinalReceiptAudit)

Recorded 2026-10-18 PDT (host clock). Machine verdict: `RESULT.json`, sha256 `797e4cd6c253146ed363d39f739b07dc3bf9cdff3d654309688708f3ef4894b7`.

## What this audit is and is not

- **Is:** an independent, metadata-only reconstruction of M1 coverage (the first method). It reads the underlying per-record receipts directly. It does not import or trust aggregate15, summarize15, STATUS15 or the parent aggregator v2 predicate.
- **Is not:**
  - a native proof replay;
  - an encoder, generator or cover-soundness verdict;
  - parent acceptance;
  - a PA(19,8,6) nonexistence claim.
- **M2 is out of scope and NOT complete.** The producer's 5411/5577 figure at 01:25 is historical. The ms09 b3 empty-list structural route and the ms06 two-split route are M2 and are counted separately by the worker.
- **No restrictions on the frozen target.** It covers all 19×8 arrays over 6 symbols in which every pair of rows agrees at most once. No balanced-only restriction applies; E0 (the balanced multiset ms00) is reported separately.
- **Nothing outside this directory was touched.** No solver, checker, generator, encoder or model CLI ran. No lane file was written: every control is an in-memory overlay.

## Disposition

**ALL-M1-RECEIPTS-QUALIFY**, metadata only, under the schema limits and binding obligations below.

| Set | Cases | COVERED | UNKNOWN | SAT-CLAIM | EMPTY-COVER (not accepted) |
|---|---|---|---|---|---|
| A2, ms01–ms09 | 5577 | **5577** | 0 | 0 | 0 |
| E0, ms00, 486 graphs | 486 | **486** | 0 | 0 | — |

- **No holes:** none in A2, none in E0, and no placement index anywhere is uncovered.
- **No SAT claims:** none in any consumed M1 record, none in the 439 lane archive JSONs, and none in the 6 orphan files.
- **Point-in-time inventory:**
  - 47,265 files in the M1 route trees at 02:07:01; the same set at 02:07:15. Nothing was added, removed or changed.
  - Every consumed record inside those trees was in the start inventory with an unchanged mtime. Inputs outside the trees (indexes, contract, base CNF, sources) were hash-pinned instead.
  - New M2 files are ignored by construction, because M2 trees are not read.
- **Parent snapshot drift:**
  - 37,840 consumed files are byte-identical to the parent's earlier record-hash snapshots: R7 strict-aggregate-v2 at 2026-10-17 14:39 and R8 population at 14:56.
  - 0 records, lists or other files changed.
  - Records created after 14:56 have no parent snapshot hash.

### Per multiset: chosen route

Route codes:
- `a` = cycle-1 stored-proof proofcheck
- `b` = streamed proofstream
- `c5` = cycle2/hard5 direct
- `d` = A3 full split
- `e` = A3′/A3″ one-column split
- `cell` = s00468 six-unit cover

| ms | cases | a | b | c5 | d | e | cell |
|---|---|---|---|---|---|---|---|
| 01 | 3215 | 1436 | 1748 | | 31 | | |
| 02 | 59 | 59 | | | | | |
| 03 | 674 | 674 | | | | | |
| 04 | 39 | 39 | | | | | |
| 05 | 73 | 73 | | | | | |
| 06 | 482 | | 376 | 86 | | 19 | 1 |
| 07 | 482 | 209 | 273 | | | | |
| 08 | 482 | | 482 | | | | |
| 09 | 71 | | 28 | | | 43 | |

- Every case has exactly one qualifying route. The qualifying-route-set histogram is a 2490, b 2907, c5 86, cell 1, d 31, e 62.
- The independent producer-order classification equals the pinned `m1-complete-candidate-20261018T012523.json` (sha `cf3e87c5…d791`, matches) per multiset, with no differences. This is a comparison only; nothing was inherited.
- `STATUS15.json` was rewritten after the task pin. It is now `56062773…84e4`; the pin was `b0dac6b0…45f3`. Its per-multiset M1 counts still equal mine, but it is mutable and was not used.

## Evidence tier of each case's chosen route

| Tier | Meaning | Cases |
|---|---|---|
| T1 | staged rev12–15: exact CR-stripped `s_lines == ['s VERIFIED']`, replay feed complete (bytes and sha equal to proof), reader_ok, zbuf>0, no abort | 68 (c5 49, split 18, cell 1) |
| T2 | streamed rev9: exact s_lines, no replay/feed fields | 1 (ms06_s00150 split, 500 batches) |
| T3 | streamed rev5: substring verdict, says_timeout False | 235 (b 198, c5 37) |
| T4 | streamed rev4: substring verdict | 2783 (b 2709, split 74) |
| T5 | cycle-1 proofcheck: stored DRAT; drat-trim rc and self-exit not recorded | 2490 (a) |
| T5E | E0 cycle-1 `.check.json`: drat_trim_rc 0 and an exact `s VERIFIED` tail line | 486 (E0) |

A split case's tier is the weakest tier among its chosen records.

## Proof-path schemas and limits (fail-closed predicate)

### All stream records (rev4, 5, 9, 12–15)

**Required, with exact types:**
- `status` UNSAT, `solver_rc` 20 and `solver_stop` self;
- `checked`, `drat_trim_verified` and `checker_interrupted` False;
- `events == []`;
- no `proof_cap_hit` and no `admission_denied`;
- 64-hex `cnf_sha256`, `cnf_bytes` > 0, 64-hex `drat_sha256` and `drat_bytes` > 0 (proof-free records are rejected);
- `drat_trim.stop` self, `drat_trim.rc` 0 and `says_verified`;
- the solver string names drat-trim and contains no `lrat-check`/`--lrat=true`, and there is no lratstrict field.

**Per revision:**
- **rev5:** `says_timeout` must be present and False.
- **rev ≥ 9:** `s_lines` must equal `['s VERIFIED']` exactly. The producer strips only `\r`; a padded, negative or contradictory set fails.
- **rev ≥ 11:** also requires
  - staged, reader_ok, replay_ok and replay_sha256_matches;
  - `replay.ok`, no `replay.error`, `replay.bytes == drat_bytes` and `replay.sha256 == drat_sha256`;
  - `aborted_by_sigterm` False, `zbuf_bytes` > 0;
  - `drat_trim_binary == tools/drat-trim/drat-trim`.

**Never counted:** rev10 (retired; 371 rev10 records sit in the archive and none are counted), rev8, rev6 lratstrict, `cycle2/hard` (CaDiCaL LRAT plus lrat-check; 66 records), and `_r2` reruns (LRAT-only).

**Substring-verdict limit (rev4/5 and route a).** The verdict was `'s VERIFIED' in stdout`.
- The lane `drat-trim.c` (commit 2e3b2dc0) prints `s VERIFIED` only at lines 1480–1481; `s NOT VERIFIED` (line 1483) and `s TIMEOUT` do not contain that substring [OBS: source grep].
- The binary sha `111b0405…d5e4` equals the parent tool-hash receipt `pa19-lratcheck-smoke-v1/tool-hashes.txt`.
- No reproducible build record exists, so this is binary identity, not provenance.

### Route a (2490; `cases19skel/proofcheck/<tag>.json`, run_proofpass.py `f2f29167…`)

**Required:**
- the exact 15-key cycle-1 schema;
- tag, plus the pass-1 record UNSAT/rc20 and `pass1_status` UNSAT;
- `cnf` equal to the tag's stored CNF path and `cnf_sha256` equal to the parent R5 rebuild;
- `cnf_matches_pass1`, `kissat_rc` 20, `drat_trim_verified` and `ok`;
- a proof sha/bytes;
- a 2-line tail ending with `c verification time:` and containing no NOT VERIFIED or TIMEOUT.

**Limits:**
- drat-trim's rc and self-exit are not recorded.
- [INFERENCE from source order] The final `c verification time` line is printed only after the verdict at the end of `main`, so its presence shows drat-trim ran to completion.
- The stored DRAT for all 2490 exists and its size equals `drat_bytes`. The proofs were stat-checked only, not hashed.

### Route b (2907; `cycle2/proofstream`)

- Stream predicate, plus: `cnf_sha256` and `cnf_bytes` equal the R5 rebuild, `cnf_matches_pass1_sha`, `cnf_file` is the tag's CNF, and `ok`.
- rev4 = 2709, rev5 = 198.
- The proof was streamed and is not stored.

### Route c5 (86; `cycle2/hard5`)

- As route b, with `encoder == encode_skel.py` and mode `directk` or `directk-staged`.
- rev5 = 37, rev12 = 48, rev13 = 1.
- Rejected c5 records, whose cases are covered by other routes: 9 rev12 UNKNOWN, 1 rev5 SIGTERM (s00150), 1 rev13 stopped (s00468).

### Routes d/e (split)

**List checks:**
- `ext.json`: `num_full == len(full)`; `source == <tag>.json`.
- The list sha must equal the parent reference where one exists. Otherwise the list is labelled worker-only.

**Record checks:**
- Canonical filenames only: `fNNNNN`, `fNNNNN_exact`, `fNNNNN_r3`, `batch_lo_hi` and `batch_lo_hi_r3`; `_r2` is rejected.
- Index fields must equal the filename: `full_index` (a3), `sub_index` (part single) or `index` (`_r3`).
- Batches need an explicit `indices == range(lo, hi+1)`.
- The tag must equal the directory and the encoder must match the kind: encode_full, encode_full2 (`_exact`), encode_partq or encode_partbatch.
- An `_r3` must have the same `cnf_sha256`/`cnf_bytes` as its original record.

**Coverage:**
- Covered means the exact set union of qualifying records' indices equals `range(num_full)`.
- Any out-of-range record, any hole, any SAT record or `num_full == 0` (EMPTY-COVER, never a generic 0/0 pass) leaves the whole case UNKNOWN.
- Overlaps are counted, not double counted: 15 overlapping indices, all ms01_s02573 `_exact` reruns.
- The per-index chosen record is frozen in `run-v1/split-index-map.jsonl.gz` as path, sha, lo, hi, tier, revision, solver, kind and snapshot flag. A per-case `index_map_digest` is recorded.

| Split family | Cases | Placements | Chosen records | Parent R8 formula-bound | Byte-equal to parent snapshot |
|---|---|---|---|---|---|
| d ms01 A3 | 31 | 17,438 | 17,438 (17,436 single + 1 `_exact` + 1 `_r3` CaDiCaL rev5) | 139 | 17,438 |
| e ms09 A3′/A3″ | 43 | 359,560 | 8,184 (4,615 single + 3,568 batch rev4 + 1 batch_r3 CaDiCaL rev5) | 146 | 8,184 |
| e ms06 A3″ | 19 | 928,614 | 9,295 (500 rev9 + 8,795 rev12/14/15, including 2 CaDiCaL batch_r3) | 253 (s00150, inc-001) | 0 (created after 14:56) |

### Cell route: ms06_s00468, row 8, column 6

- The six-unit contract `cycle2/s00468-six-unit-contract.json` (sha `a9490508…60c3`) equals the frozen fields. Its runner `964e2c61…` and aggregator `7933b3b1…` hashes are unchanged.
- Base CNF: `137407b6…a994`, 1,504,628 B, equal to the contract and to the parent R5 rebuild. It contains the at-least-one clause `421 422 423 424 425 426 0` [OBS], so the six unit subcases exhaust the cell.
- **Unit-CNF hashes recomputed by me from the base bytes.** Each is `p cnf nv nc+1` + body + `<421+s> 0`:

  | s | Unit-CNF sha256 |
  |---|---|
  | 0 | `2250d435…` |
  | 1 | `1af0e82b…` |
  | 2 | `c8367432…` |
  | 3 | `ceac9950…` |
  | 4 | `ad345a72…` |
  | 5 | `2a312060…` |

- Each of `s00..s05.json` matches every identity and binding field (tag, row, column, symbol, literal, unit bytes, base header/body/sha/bytes, subcase sha and bytes, encoder label). Each meets the full T1 predicate. s00–s04 are rev13; s05 is rev14.
- No `s06+` record exists, no sibling cell directory exists, and the `deferred-s05` record is an UNKNOWN stop record.

### E0 (486; `cases19q0/results/gNNN{,.check}.json`, check_proofs.py `69c5b76d…`)

- **Required:**
  - both exact schemas;
  - `graph6` equal to the parent-pinned index `436139a7…`;
  - the CNF sha equal at solve and at check;
  - `proof_sha256` and `proof_bytes`, matching between the two records;
  - `drat_trim_rc` 0, `drat_trim_verified` and `ok`;
  - the 3-line tail holds exactly one exact `s VERIFIED` line and ends with a verification-time line.
- **Observed:** all 486 stored DRATs exist with size equal to `proof_bytes` (stat only).
- **Limits:** no self-exit flag. The `encode_q0` CNF↔graph6 binding is worker-only.

## Bindings: parent-replayed, sampled, worker-only

| Binding | Scope | Status | Receipt (sha) |
|---|---|---|---|
| R0 pins: index, 5577 specs, sources | full | parent pinned | `pa19-parent-cover-replay-v1/pin-result.json` (`429c5627…`) |
| R1 profiles; R2 E0 graph list (geng 486, index order); R4 index↔specs↔skeletons | full | parent replay PASS | `cover-binding-result.json` (`f0b1e282…`) |
| R3 skeleton generators A/B and the a_to_b maps | 9 multisets | parent replay, semantic PASS (the strict byte replay `4ea6b092…` fails only on added metadata) | `generator-semantic-check-v1.json` (`939d1ea7…`) |
| R5 base CNF `encode_skel(spec)` vs pass-1 and direct records | all 5577 | parent replay PASS_WITH_PENDING (all 5577 bound). This audit requires every route-a/b/c5 record's `cnf_sha256` to equal it | `pa19-cnf-binding-v1/cnf-binding-result.json` (`2a14a1dc…`) |
| R6 placement lists: ms01 A3 ×31, ms09 A3′ ×43 | 74 lists | parent regeneration: 73 byte-equal, s00067 predicted then equal | `placement-binding-result.json` (`6cd7f188…`) |
| ms06_s00150 placement list | 1 | parent replay, semantic-equal except the source path | `pa19-ms06-placement-binding-v2/result.json` (`cc748b23…`) |
| **18 other ms06 lists** | 18 | **worker-only.** 15 match the worker's own extend receipt (rc 0, no cap, raw/num_full/source). s00204, s00212 and s00214 were generated inline by `run_hard12` and have no receipt | `postcheck-v1.json` (`da674278…`) |
| R8 split-record formulas | 374 sampled + 253 inc-001 | parent sample PASS; 538 of my chosen records are among them | `subcase-binding-result.json` (`594e1998…`), `inc-001/inc-result.json` (`6f510d81…`) |
| **Remaining chosen split-record formulas** | **34,379 / 34,917** | **worker-recorded `cnf_sha256` only** | — |
| s00468 unit CNFs | 6 | recomputed in this audit from R5-bound base bytes | this audit |
| **E0 CNF ↔ graph6 (`encode_q0`)** | 486 | **worker-only** | — |
| Record bytes immutability | 37,840 files | equal to the parent R7 (14:39) and R8 (14:56) record-hash snapshots | `strict-aggregate-v2/aggregate.json` (`371fb2fd…`), `population.jsonl` (`e1b4835a…`) |
| Native proof replay | any M1 route | **none found** under `review/pa19*` | — |

I reused all successful parent checks by hash and reran none of them.

## Controls: 94/94 pass

`controls-v1.json` (`b8ecb7a8…`) ran from 02:08:07 to 02:17:53 against reader `b4e7baa2…`. These are evidence-parser checks on in-memory overlays of real records, **not proof mutations**. The C* controls ran with the parent snapshot hash check off, so the intended field predicate itself had to reject the change. Each control was checked for its expected state, its intended reason substring and its exact hole count. Fixtures were chosen deterministically from the run-v1 output:

| Fixture | Case |
|---|---|
| T1 batch case, worker-only list | ms06_s00228 |
| parent-R6 singles | ms09_s00004 |
| a3 | ms01_s01021 |
| batch_r3 | ms09_s00010 |
| b rev4 | ms01_s01440 |
| c5 T1 | ms06_s00197 |
| c5 rev5 | ms06_s00028 |
| a | ms01_s00000 |
| cell | ms06_s00468 |
| E0 | g000 |

| Group | Controls |
|---|---|
| Baselines | 12, plus Z00 with the snapshot check on: all COVERED |
| Placement/cube drops | drop one essential batch (100 holes), one ms09 single (1 hole), the covering `_r3` (100 holes); drop cube symbol s03 |
| Denominators | drop one placement from a worker-only list (out-of-range record → UNKNOWN); append one (1 hole); `num_full` ≠ list length; empty list → EMPTY-COVER; one placement dropped from an R6-bound list (sha mismatch) |
| Identity and hashes | wrong case tag (batch, b); wrong CNF hash (a, b; s01 unit); wrong base sha (s05); cnf_bytes off by one; `_r3` CNF ≠ original; `_r3` original missing; index-field mismatch (part single, a3), missing `full_index`, batch-style indices on an a3 single, non-canonical filename, indices list shortened; non-hex split `cnf_sha256`; wrong unit literal, duplicate symbol, extra s06, contract altered; E0 graph6 swapped, CNF changed between solve and check |
| Checker verdict | s_line with `\r` kept, padded, contradictory (+TIMEOUT), or NOT VERIFIED; rc 1; stop=term; rev4 says_verified False; rev5 says_timeout True or missing; route-a negative tail or blank tail; E0 rc flipped, negative tail, padded tail |
| Solver and process | solver_stop term; solver_rc 0; checker_interrupted True; checked False; events non-empty; admission_denied; proof_cap_hit; aborted_by_sigterm |
| Feed and reader | replay.bytes − 1; replay.sha256 altered; replay_ok False; reader_ok False; zbuf 0; c5 T1 replay.ok False; drat_bytes 0 (proof-free) |
| Retired and LRAT | retired rev10 injected; LRAT-only `_r2` injected; LRAT solver string on route b; only the `cycle2/hard` LRAT record left |
| SAT | SAT in a batch, in a `_r3`, in E0: all SAT-CLAIM |
| Missing field not read as PASS | `kissat_rc` removed; `drat_trim.rc` removed |
| Snapshot | Z01/Z03: a field-identical byte reformat of a snapshotted b record or split record is rejected. Z02: a reformatted pass-1 record fails the row while route b stays intact |

**Limitation the controls confirm by omission:** consider a split record outside the parent R8 formula sample that carries a well-formed but wrong `cnf_sha256`. Metadata cannot detect it, because no parent-recomputed expectation exists for that record. Only syntax is checked (control P05). Discharging this needs obligation 2.

## Outstanding parent replay and bridge obligations

1. **Native proof replay (none exists for M1).**
   - Stored-proof routes: route a's 2490 DRATs (`cases19skel/proof`) and E0's 486 DRATs (`cases19q0/proof`) can be checked with a parent-built drat-trim against the stored CNFs, after hashing each proof against `drat_sha256` or `proof_sha256`.
   - Streamed routes need a re-solve plus a streamed check (kissat `--seed=1`; compare `drat_sha256`): b 2907, c5 86, d 17,438 records, e 17,479 records, cell 6. Otherwise the parent must explicitly set a sampling policy.
2. **Split-record formula binding.** 34,379 chosen split records are worker-only `cnf_sha256`:
   - d: 17,299 unbound;
   - e-ms09: 8,038 unbound;
   - e-ms06: 9,042 unbound, including all 8,795 records on the 18 worker-only lists.

   Needed: an R8-style in-memory rebuild with the declared encoder from (pinned spec, list, indices).
3. **The 18 ms06 extend_p1q (m=1) lists need an R6-style replay**, with equal raw/num_full and orbit semantics: s00204, 212, 214, 216, 228, 266, 285, 287, 297, 310, 311, 368, 370, 389, 406, 410, 414, 430. List shas are in `M1-manifest-compact.tsv`. Worker receipts show helper peak RSS up to 5,070,832 KB (s00370); the lane checkpoint records 5,109,408 KB for s00214. Plan memory admission accordingly.
4. **E0 CNF binding:** rebuild 486 `encode_q0(graph6)` CNFs and compare with `cnf_sha256`.
5. **Bridge and math items, not receipts.** These need math review (bridge desk), not receipts:
   - The A3-exact amendment (`encode_full2`) is load-bearing for ms01_s02573 index 12 (`f00012_exact`; the original was UNKNOWN).
   - Soundness of the ms06 A3′ one-column split, of batch UNSAT ⇒ placement UNSAT, and of the cover, generator and skeleton lemmas.
   - Four counted CaDiCaL-binary-DRAT reruns, all drat-trim-checked:
     - `a3/ms01_s03171/f01788_r3`
     - `part/ms09_s00010/batch_04300_04399_r3`
     - `part/ms06_s00368/batch_42500_42599_r3`
     - `part/ms06_s00430/batch_05000_05099_r3`
6. **Checker provenance:** the drat-trim binary has hash identity only (`111b0405…`). A parent-built checker would discharge this (see 1).
7. **Retention:** the stored route-a and E0 proofs must stay on disk (they are not snapshotted) until obligation 1 is decided.

## Other observations

- **Orphans, never counted and none SAT:** `cycle2/hard/STOP-0632-revision1.json` and five `cycle2/part/check*-ext*.json` worker check copies.
- **No checker rejection:** no stream record (direct or split) in the M1 trees has an UNSAT solve with drat-trim self-exit and a rejection (NOT VERIFIED, rc ≠ 0 or no verdict). Every route-a and E0 record qualified.
- **Rejected records whose indices are covered elsewhere:**
  - ms01_s02573/f00012 (UNKNOWN);
  - ms01_s03171/f01788 (SIGTERM) and its `_r2` (LRAT-only);
  - ms09_s00010/batch_04300_04399 (SIGTERM) and its `_r2` (LRAT-only);
  - ms06_s00368/batch_42500_42599 and ms06_s00430/batch_05000_05099 (UNKNOWN, covered by `_r3`).

## Process and resources

- **Reader process:** one, stdlib only, `nice 10`, each run under ONE existing token taken by a read-only fd flock (`token_ro.py`). Token files were never written.

  | Run | Token wait | Notes |
  |---|---|---|
  | census | 0 s | held 01:31:50–01:31:53 |
  | run-v1 | 292 s | — |
  | controls | 584 s | — |
  | postcheck | 972 s | — |

  Each wait was one blocking flock with no polling. All token use paused during InfoPacking19's exclusive helper window, which ended 01:51.
- **Memory and disk:**
  - run-v1 maxrss was 249,479,168 B. Controls and postcheck RSS was not measured.
  - **Watchdog visibility gap:** the reader argv used relative paths, so lane watchdog4 did not include these processes in its "other" RSS sum. Run windows: run-v1 02:02:09–02:07:15, controls 02:08:07–02:17:53, postcheck 02:18:41–02:34:53. InfoPacking19 was told the windows and RSS figures; any future reader must use absolute paths.
  - Free disk was measured before census (15.60e9 B), smoke (15.41e9), run-v1 (15.31e9) and controls (15.23e9). The postcheck (02:18:41; projected retention < 0.1 MB) launched without a fresh disk reading; that is a gate-procedure lapse. Free disk was 14.71e9 B at 02:38:20.
  - Retained new data is about 14 MB: run-v1 12.2 MB, manifests, controls and this report. No CNF or proof was copied.
- **Pre-execution hash pins** are in `LOG.md`:

  | File | sha256 |
  |---|---|
  | `m1_receipts_v1.py` | `b4e7baa2605ab91776b1fc9cdff7f11a051d07f12fedddf8697f2251b9743a32` |
  | `controls_v1.py` | `5cca2b9ea599fc794030bea252d4bbbfcba74bcfb151c6c9465239f58c36e34d` |
  | `token_ro.py` | `8e069589…4b79` |
  | `census_v1.py` | `5a992f13…6f61` |
  | `finalize_v1.py` | `f2ff9b4d…9f7f` |
  | `postcheck_v1.py` | `21f3c9ab…56d3` |

## Files

| File | sha256 |
|---|---|
| `RESULT.json` | `797e4cd6c253146ed363d39f739b07dc3bf9cdff3d654309688708f3ef4894b7` |
| `M1-manifest-compact.tsv` (one line per case: chosen path/sha or list sha, num_full, records, digest, binding) | `83cc8df69a876991149ed8cba52bd0f4f8c540c1ed33f7c9dae44007c22bbcd1` |
| `run-v1/RESULT-core.json` | `3c3ae350…1397` |
| `run-v1/cases-A2.jsonl` | `d2471123…0a28` |
| `run-v1/cases-E0.jsonl` | `4a21c6ec…3460` |
| `run-v1/split-index-map.jsonl.gz` | `8812e2af…6b53` |
| `run-v1/consumed-manifest.tsv.gz` (47,272 consumed files with sha/size/mtime) | `0e0db23a9bda025455ce0b3dd561b3bb54c602b123b21a606549e0a9e1ee4ba5` |
| `controls-v1.json` | `b8ecb7a82cd4aa018ce11dd44d75d278a90035fc6ef1517298354edfe8164eba` |
| `postcheck-v1.json` | `da674278917010a02cc7e905b8d8f5ebadc1b3a995929d002d5aa9ce64eea573` |
| `census-v1.json` (exploratory schema census) | `a94ab9ce…5478` |

Parent verdict is separate.
