# PA(19,8,6) formula and placement-list bindings v1 (PA19FinalFormulaBindings)

Recorded 2026-10-18 PDT (host clock). Machine aggregate: `RESULT.json` sha256 `eb6e591f7422d7b0b06d045458cf01f572d0da8a2e3e8d59cfb16090c046ef6c` (M1 split, lists, E0, controls, M2 direct/E0-B). The M2-split extension and the ms09_b00002 list replay are reported from their own receipts in §6, because they ran after the frozen aggregator. Append-only log: `LOG.md`.

## What this is and is not

**Is:**
- formula binding: CNF bytes are rebuilt in RAM with the declared, hash-pinned lane encoders, hashed, compared with each record's `cnf_sha256`/`cnf_bytes`, and discarded;
- placement-list binding: the unchanged lane producer is re-executed with the production argv.

**Is not:**
- a solver run, a proof-checker run, or a native proof replay;
- an UNSAT acceptance or an M1/M2 coverage verdict;
- a PA(19,8,6) claim. PA(19,8,6) stays undecided.

**Re-execution, not independent authorship.** List replays re-execute `extend_p1q.py`/`extend_b.py`, and rebuilds re-execute the declared encoders. Neither is an independently authored encoder or enumerator.

**Handling rules:**
- No CNF, proof or list was copied. Lane files were read in place, against SHA pins.
- The only lane-path writes were none. The list producers wrote into desk FIFOs (0 B on disk).
- The desk totals about 10.9 MB.

## 1. Census and denominators (pinned before any rebuild)

`pins-v1.json` (`e7cfd639…1b68`) and `jobs-v1.jsonl.gz` (`2ec7348b…eef5`) were written by `fb_v1.py pin` at 03:23 under token t1. The chosen records come from PA19FinalReceiptAudit's `split-index-map.jsonl.gz` (`8812e2af…6b53`).

**Census result:**
- 93 split cases, 34,917 chosen records.
- census_not_ok 0: every record's bytes equal the index-map hash and all identity checks pass.
- Every case's index coverage is complete. All 93 specs are bound (S = L = R0).

| Route / family | Chosen | Reused by unchanged hash | Rebuilt here |
|---|---|---|---|
| d ms01 (encode_full; 1 `_exact` = encode_full2; 1 `_r3`) | 17,438 | 139 (R8) | 17,299 |
| e ms09 (encode_partq singles, encode_partbatch batches, 1 `_r3`) | 8,184 | 146 (R8) | 8,038 |
| e ms06 (encode_partbatch; rev 9/12/14/15; 2 `_r3`) | 9,295 | 253 (R8 inc-001 + ms06-binding-v2) | 9,042 |
| **total** | **34,917** | **538** | **34,379** |

**How reused records were counted:**
- A reused record counted only if its current bytes hashed equal to the index-map hash **and** to the record hash in the reused R8/inc-001 receipt.
- The `_exact` (f00012) and the ms01/ms09 `_r3` records are among the R8-reused ones.
- Rebuilt `_r3` records additionally required the recorded CNF to equal the original record's CNF.

**Serializers:** every `cnf_bytes_of` (rev 4, 5, 9, 12, 14, 15) is AST-identical to stream_check4's. Each revision's own pinned module was executed.

## 2. Split formula binding (M1 routes d/e)

`fb_v1.py split` ran 03:24:54–03:50:44 under token t1, nice 10:
- 1,514 CPU s, maxrss 317 MB;
- `split-run-v1-p1.json` `35588241…e073`;
- rows `split-v1-p1.jsonl.gz` `3c761c03…4339` (one line per chosen record: path, record sha, indices, encoder, revision, rebuilt `[cnf_sha256, bytes, vars, clauses]`).

| Final status | d ms01 | e ms09 | e ms06 | Total |
|---|---|---|---|---|
| PASS: rebuilt == record, list parent-bound (R6 / ms06-v2) | 17,299 | 8,038 | 247 | 25,584 |
| PASS_LIST_REPLAYED: formula equal, list bound by §3 | — | — | 8,795 | 8,795 |
| PRIOR_R8_PASS / PRIOR_INC001_V2_PASS (hash reuse) | 139 | 146 | 253 | 538 |
| MISMATCH / FAIL / UNRESOLVED | 0 | 0 | 0 | **0** |

- **All 93 split cases have every chosen record bound.**
- `exposure-leaf-hashes-v1.json` (`72749bed…6912`) lists 502 parent leaf hashes for the bridge F-A NONE-class split leaves:
  - the 500 ms06_s00150 rev-9 batches;
  - ms01_s03171 `f01788_r3`;
  - ms09_s00010 `batch_04300_04399_r3`.
- The route b and c5 exposure cases keep their R5-bound base CNFs.

## 3. The 18 worker-only ms06 placement lists (extend_p1q, m = 1)

**Producer, re-executed in place:**
- `src/extend_p1q.py` `bd2292c3…1b35`, `encode_skel.py` `dd871522…cc22`, `encode_e1.py` `2a76e8bd…b830`;
- venv python realpath sha `cbf84109…ca43`;
- networkx 3.7 tree digest equal to the R6 pin.

**Argv:** `-B -I -X pycache_prefix=<desk>/nopyc <LANE>/src/extend_p1q.py <LANE>/cases19skel/specs/<tag>.json <desk FIFO> 1`. The only transformation is that OUT_JSON is a FIFO.

**Supervision and admission:**
- The lane's unchanged `enumeration_helper_guard_v3.run_helper` with S = `stream_check15`:
  - 1800 s per list;
  - 60 s TERM_WAIT, then quarantine; no SIGKILL;
  - child cap 5 GiB minus driver RSS minus 16 MiB;
  - in-flight floor 12e9.
- Exclusive windows: COUNT 0 was set by InfoPacking19. All of t0..t7 and bigmem were held as O_RDONLY flocks, and the helper lock was taken via run_helper.
- A list was admitted only if at least 1,950 s remained. Main's rule was to stop at the first non-equal list.

**Comparator:** byte equality first. Otherwise the parsed values of all four fields must be equal, with identical key sets. No field is ignored, and `source` must be `<tag>.json`.

**Result: all 18 lists are BYTE_EQUAL to the stored list.** In every case FIFO bytes = stored bytes, and the stdout summary matched.

| Chunk / driver | Window (locks held) | Lists |
|---|---|---|
| 1 / fb_v2 `ee951b2a…44dd` | 03:50:44–04:09:50, `chunk-1-v1.json` `be65bdd4…6854` | s00228, s00204, s00406, s00212, s00216 equal; s00310 **UNKNOWN** (floor trip, see below); 12 not attempted |
| 2 / fb_v3 `d2d1fcd3…3d32` | 04:16:26–05:16:39, `chunk-2-v1.json` `1df30e1f…0e11` | s00310 (fresh attempt), s00287, s00297, s00430, s00389, s00285, s00410, s00368, s00266, s00414, s00214, s00311, s00370: all equal |

**Chunk-1 UNKNOWN (kept on record):**
- The s00310 receipt is `67d299fc…ed01`: helper guard "in-flight free-space floor"; minimum sampled free 11,999,723,520 B at 344.6 s; own child SIGTERM, stop=term, no quarantine.
- The cause of the disk dip is UNESTABLISHED (Main's correction). This desk wrote 0 B during the replay.

**Defects found and fixed, each as a new frozen version reviewed by Main:**
- v2 adds stop-on-first-non-equal.
- v3 stops parsing the jobs file in `lists`. Chunk 1 had a 160 MB driver RSS, which left a child cap of 5,066,128 KB, below the s00370/s00214 worker peaks.

**Timings and peaks.** Times ranged from 90 s (s00311) to 758 s (s00430). The maximum child RSS was 5,030,080 KB for s00370, against a cap of 5,154,496. Per-list receipts are `lists/<tag>-replay-v1-c{1,2}.json`; their SHAs are in RESULT.json `lists.replays`.

## 4. E0 CNFs (encode_q0)

`fb_v1.py e0` ran 03:24 under t1: 25 s, maxrss 220 MB. Receipt `e0-result-v1.json` `660c74c6…cfce`; rows `e0-v1.jsonl` `5cd5cb6c…647b`.

**Inputs:**
- graph6 from the R2-bound snapshot index `436139a7…` (equal to the lane copy);
- the spec is exactly run_cases.py's `{"kind":"q0","N":19,"k":8,"q":6,"graph6":…, "index":i}`, and it equals the lane spec file;
- `encode_q0.build` + pinned `encode_e1.CNF.write` (module-global `open` shadowed by a RAM sink), cross-checked against `stream_check4.cnf_bytes_of`.

**Result: 486/486 PASS.** In each case:
- rebuilt sha = `results/gNNN.json` `cnf_sha256` = check `cnf_sha256_now` = `cnf_sha256_at_solve` = the stored CNF file hashed in place (488,587,891 B total);
- bytes, vars and clauses are equal;
- record bytes equal the audit pins.

Delivered to PA19StoredProofReplay at 03:25.

## 5. Controls (in-memory overlays; no lane file modified; no proof assertion)

**M1 mapper.** `controls-v1.json` `487c9a88…bc74` (fb_v4 `40e833d0…2a74`): 75/75 as expected.

- **Fixtures** (8): d single, d `_exact`, d `_r3`, e9 single, e9 batch, e6 rev12 batch, e6 rev9 batch, e6 `_r3`.
- **Baselines:** each fixture evaluates PASS or PENDING unmodified.
- **Per-fixture mutations, each failing for its intended reason:**
  - wrong record → `record_sha_equals_pinned`;
  - wrong but self-consistent record → `filename_range_equals_index_map`;
  - wrong list → `list_sha_equals_pinned` (FAIL_INPUT_BINDING);
  - wrong list with its hash pinned → rebuilt CNF differs, or the encoder refuses;
  - wrong placement indices → `cnf_sha256_equal`;
  - well-formed wrong SHA → `cnf_sha256_equal`.
- **encode_full vs encode_full2:**
  - encode_full on `f00012_exact` → MISMATCH, and the CNF equals the original UNKNOWN record's CNF;
  - encode_full2 on a plain record → MISMATCH;
  - `_exact` declaring encode_full → FAIL_STRUCTURAL.
- **Omitted chosen leaf** (3 cases): exact hole count, and the census total changes.
- **E0:** graph swap, the stored CNF of another graph, and a well-formed wrong SHA all fail.
- **List comparator:** identity and re-serialization → BYTE_EQUAL; whitespace → SEMANTIC; an altered block, a swapped order, a dropped placement, a changed source, a changed raw and an extra field → MISMATCH.

fb_v1's own controls run raised before writing anything, because every same-family a3 list has identical entries at the d_single index. v4 changed only that fixture search (diff in LOG.md).

**M2 controls:**
- M2 direct/E0-B: `m2-controls-v1.json` `8a5a8148…daf6`, 10/10 as expected.
- M2 split: `m2part-controls-p1.json` `cb23ea81…12b5`, 7/7 as expected.

## 6. M2 bindings (Main IRC, after the M1 jobs; separate pinned stages)

None of these results is M2 coverage, and STATUS was not read. The strict-predicate classification is PA19FinalReceiptAudit's `stream_predicate` (m1_receipts_v1 `b4e7baa2`), reported as metadata only.

**M2 direct (encode_skel_b.build_v2) + E0-B (encode_q0b):**
- Driver fb_m2_v1 `49506607…6f58`.
- Census `m2-pins-v1.json` `eaecc88f…e75c`, frozen at 05:21: 5,399 `m2skel_drat` + 486 `m2q0c` records. 5,880 pass the strict predicate; 5 are UNKNOWN-status records (bound anyway).
- B lists: 9/9 bound (S = L = R0, R3 `B_byte_equal`).
- Run `m2-run-v1.json` `9e529dca…2d08` (05:21–05:51, 1,753 CPU s, maxrss 277 MB): **5,399/5,399 direct PASS and 486/486 E0-B PASS.** For E0-B, the run_m2q0c stdout transform reproduced the writer bytes, and `encoder_info` was equal.
- A delta census for records completed after 05:21 is not done (Main: "fine later").

**M2 split (m2part_drat, build_partbatch):**
- Driver fb_m2part_v1 `7d6ae49e…82f4`; census `m2part-pins-p1.json` `3accf207…0f9a`: 194 records in 34 dirs.
- Run `m2part-run-p1.json` `f94f746a…4006`: 69 PRIOR_R8_PASS, 123 PASS, and 2 FORMULA_EQUAL_LIST_PENDING (ms09_b00002).
- 33 lists equal R6's predictions.
- The ms09_b00002 list was then replayed by fb_m2list_v1 `c6845c92…653f` (one child, `src/extend_b.py` `31924ed6`, under one token plus the helper lock):
  - **BYTE_EQUAL**;
  - FIFO 6,550 B; sha `3e170c36…dd8d` = stored;
  - 1.0 s, child RSS 5,472 KB;
  - receipt `m2list/ms09_b00002-replay-v1.json` `3954a54a…69f5`.
- This promotes those 2 records to formula-plus-list bound.

## 7. Process, resources, deviations

- **Tokens.** Regular work took one existing token as an O_RDONLY flock, never written, with a bounded wait. Waits were 0 s throughout. Lists ran in COUNT-0 windows set by InfoPacking19. COUNT and the guards were never edited.
- **Argv and isolation.** Every parent and child argv contains the absolute lane path (watchdog4-visible). Every child got an owned TMPDIR.
- **Peaks.**
  - Driver RSS ≤ 317 MB.
  - List children were within the 5 GiB-minus-driver cap.
  - At most 1 busy process for regular work.
- **Defer and stop events:**
  - chunk-1 floor trip (UNKNOWN; not retried until Main's GO);
  - fb_v1 controls exception (no output written).
- **No SIGKILL; no quarantine occurred.** The 18:00 deadline was met.
- **Versions** (all frozen 0444 and SHA-logged before running):

  | File | sha256 |
  |---|---|
  | fb_v1 | `23219f5d…75ee` |
  | fb_v2 | `ee951b2a…44dd` |
  | fb_v3 | `d2d1fcd3…3d32` |
  | fb_v4 | `40e833d0…2a74` |
  | fb_m2_v1 | `49506607…6f58` |
  | fb_m2part_v1 | `7d6ae49e…82f4` |
  | fb_m2list_v1 | `c6845c92…653f` |
  | fb_finalize_v1 | `22a5ffdb…d2be` |

- **Interpreter:** `/opt/homebrew/opt/python@3.14/bin/python3.14` (realpath sha `cbf84109…`), run with `-B -I`.

**Remaining limits:**
- Producer and encoder soundness and enumerator completeness are bridge and math items, not receipts.
- Bindings re-execute lane code, so they cannot detect a shared encoder or enumerator error.
- M2 coverage remains open.
- No native proof replay was done here.
