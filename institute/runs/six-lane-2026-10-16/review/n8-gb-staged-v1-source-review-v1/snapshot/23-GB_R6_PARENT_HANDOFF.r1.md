# Handoff: frozen GB staged pipeline r6 — API, data paths and parent-replay changes (static, r1)

**Stand-down.** On parent instruction, the four remaining WORKER GB items (P0-B2, P0-B3, P2-C2, P2-C1) are stood down. This lane makes no further worker native solver or checker run, even on RELEASE.
- Marker `L/evidence/gb_direct_v6/hold/STANDDOWN-1.json`, SHA256 `284d3b834fef9bca171d2d78e57874cc9d1aef95b4b98f6229165ca2a489e1e0`, x-created; HOLD markers stay 2 HOLD / 1 RELEASE.
- The eight PASS receipts are worker/timing evidence only (§6). They are never counted.

This handoff implements nothing and runs nothing.

Frozen source being described:
- `L/code/gb_direct_r6.py`, SHA256 `89fa8959fa83467a13f32e4222dcd9ede36c2fec51e4a9ac7f3cef72b78b7032`;
- freeze `L/review/GB_DIRECT_FREEZE.r6.json`, SHA256 `f1b022c164da0810146ba95c26e9d71d6e611839524304fd5d2bd82c072ea9c9`;
- byte producer `L/code/gb_one_p4_r2.py`, SHA256 `5ca7c0da82c5ddd308acbbc2424da1ac6b4a0db08d0571f656eda5e841ffe262`, called "adapter" below.

`L` = `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16`. "r6:N" and "adapter:N" are 1-based line numbers in those pinned files.

## 1. Pins and constants (r6:59–89)
- `GEN`/`GEN_SHA` (adapter), `OWN`/`OWN_SHA` (lane own-hash receipt), `WMAN`/`WMAN_SHA` (template table): r6:60–65.
- `KISSAT` `/opt/homebrew/Cellar/kissat/4.0.4/bin/kissat`, SHA256 `05d6f3e9c402a1fe8853b0746e384e1b3d1c4a550e255f11daa2461d279aa848`: r6:66–67.
- `DRAT` = parent drat-trim, SHA256 `a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37`: r6:68–69.
- `BODY_SHA` GB base body `f5da05206f44ff72e5aeade076820e2de52c9d2352f58b048ded1df76bdbf1b9` (350550717 B, 17025578 clauses, 3803745 vars): r6:70.
- Output: `OUTBASE`/`HOLD_DIR`/`OUTDIR` r6:71–73. `OUTDIR` must contain `fifo/`, `logs/`, `tmp/` and `receipts/`; every log and receipt is x-created.
- Time: `DEADLINE` 17:55 in-flight stop and `LAUNCH_CUTOFF` 17:29: r6:75–76.
- Memory and disk caps:
  - `LANE_CAP_RSS` 11 GiB, `GA_RESERVED` 4.6 GiB, `GA_MARKER`: r6:77–79;
  - `AGG_CAP` 6 GiB, counting self + kissat + drat-trim resident: r6:80;
  - `FLOOR` 12e9 in-flight free, `FRESH` 12.2e9 + `MARGIN` 5e7, `LANE_CAP` lane bytes: r6:81–84.
- `GB_ITEMS` holds the twelve direct ids with kissat `--time=3600` and drat-trim `-t 7200`: r6:85–86. `DUP_BASELINE` 375334: r6:87. `TINY_UNSAT`/`TINY_SAT`: r6:88–89.
- Interpreter used: `/opt/homebrew/opt/python@3.14/bin/python3.14 -I -B` (3.14.3).

## 2. Callable API (import the file as a module; set OUTDIR first)
- `pipeline_staged(label, parts, expected_bytes, expected_sha, ksec, dsec, stopflag)` (r6:502–576). It returns a receipt dict.
  - `parts` is a list of bytes-like segments, e.g. `[header, body, tail]`. Segments are written in order to both feeds and are never concatenated or copied.
  - `expected_bytes` and `expected_sha` are the bound identity.
  - `stopflag` is a dict; set `stopflag['sigterm']=True` to stop cooperatively.
  - It uses the module globals `OUTDIR`, `KISSAT`, `DRAT` and the caps.
- **Stage 1** (r6:512–536): kissat alone.
  - argv `[KISSAT, '--time=K', '/dev/fd/<cnf>', <named FIFO>]` (r6:517).
  - The CNF goes through an anonymous pipe via `writer` (r6:212–228), which hashes and counts exactly the bytes written.
  - The DRAT stream goes through the owned FIFO to `collector` (r6:407–421), which keeps chunks in RAM with sha256 and bytes.
  - A keepalive write end is held until kissat is reaped (r6:515, 525–529).
- **Stage 2** (r6:538–554): only if stage 1 had no stop, no survivor, rc20 and the collector reported ok.
  - drat-trim alone, argv `[DRAT, '/dev/fd/<cnf>', '-i', '-t', 'D']` (r6:540). The proof goes to stdin through `proof_feeder` (r6:423–437), which hashes and counts what it writes and frees chunks as it goes.
  - Stdout goes through `log_filter` (r6:253–281). It sha256s and counts the FULL raw stream, counts duplicate-literal normalisation lines and stores every other line.
- **`supervise(live, rec, t0, stopflag, peak, on_exit)`** (r6:439–499) polls every 0.5 s.
  - It reaps with `os.wait4`, which gives rc, wall, ru_maxrss, user and sys.
  - It samples libproc `proc_pid_rusage` max(resident, phys_footprint) for self and children (r6:127–132).
  - It stops, in this order, on: an unknown reading (fail closed); aggregate > AGG_CAP; GA counted + aggregate > 11 GiB; the deadline; driver SIGTERM; free < FLOOR (checked every 2 s).
  - Stops are SIGTERM only, followed by a bounded 120 s wait that records survivors. It never sends SIGKILL.
- **`status_lines(path)`** (r6:283–286): status lines are exact `s ` lines after removing CR only.
- **Lane-specific parts:** `gate(label)` (r6:579–588) holds the GA-driver exclusion, the HOLD markers and the fresh disk/lane checks, and `ga_usage()` (r6:167–197) is the GA-desk scan. Neither should be reused by a parent desk.

## 3. Supplying independently bound bytes
- **How r6 builds bytes (worker path, r6:636–669).**
  1. Load the adapter by path and check its SHA; `gb = gen.load_gb()`.
  2. Rebind `gb.F = gen.make_sink(original, None)` (adapter:109–161), call `gb.encode(8,[1,2,3,4,5],0,[1],True,fixg=None,g5=True,allrows=False,allcols=False)`, then restore `gb.F`.
  3. Take `body = f.body` and check `BODY_SHA` (r6:646–648).
  4. Direct items: `units = gen.template_units(f, WMAN case)` (adapter:300–305), header `'p cnf %d %d\n' % (f.n, f.count+42)`, tail `''.join('%d 0\n' % v for v in units)` (r6:664–665).
  5. The full SHA and byte count must equal `OWN` before any feed, otherwise the run aborts (r6:666–669).
- **For a counted parent replay,** supply `parts` from the PARENT's own independent byte construction, e.g. its binder `bind_gb_v2.py`. Take `expected_bytes`/`expected_sha` from `R/moqls8-gb-parent-binding-v1/GBBINDING.json` `formulas[].bytes`/`.sha256` (SHA256 `d917203deb29a13e212c290e227a001a695765d080a897141d6dc154d79fc673`). The worker adapter's bytes are equal (ALL 22 MATCH), but the parent decides whose producer it trusts.
- **Six strengthened ids** (P1-B1.M2, P1-B2.M2, P1-B2.M4, P1-B3.M2, P1-B5.M2, P1-B5.M3): r6 has NO code path for them, since `GB_ITEMS` covers direct items only. A parent version must build:
  - header `'p cnf 3803745 17025746\n'` (count + 168);
  - tail = the 42 source-template unit lines followed by the 126 binaries `gen.m_clauses(f, s)` (adapter:308–312), each a sorted negative pair serialised as `'%d %d 0\n'`, in i=2..7 and (c,d) combinations order (adapter:309–310).

  The bound identities are in GBBINDING. The adapter's own construction is at adapter:368–379.

## 4. Receipt fields and predicate (r6:507–510, 535–536, 551–575)
**Receipt fields:**
- run: `label`, `started_at`, `finished_at`, `wall_s`, `mode`, `events[]`;
- argv: `kissat_argv`, `drat_argv`;
- feeds: `expected_feed_bytes`, `expected_feed_sha256`, `solver_feed{ok,written,sha256,error}`, `checker_feed{…}`;
- kissat: `kissat{rc,wall_s,ru_maxrss_bytes,user_s,sys_s}`, `kissat_stage_wall_s`, `kissat_status_lines`, `kissat_log{path,sha256,bytes}`;
- drat-trim: `drat{…}`, `drat_stage_wall_s`, `drat_status_lines`, `drat_warnings`, `drat_log{path,sha256,bytes}`;
- raw stream: `drat_stdout_filter{ok,error,raw_stdout_sha256,raw_stdout_bytes,duplicate_literal_warning_lines,kept_lines}`, `duplicate_literal_count_equals_formula_baseline_375334`;
- proof: `proof{proof_bytes_read,proof_sha256,proof_bytes_relayed,proof_relayed_sha256,collector_error,feeder_error,error}`;
- resources and outcome: `sampled_peak_resident{kissat,drat,aggregate,lane_counted_ga_max}`, `stop_reason`, `survivors`, `criteria{…}`, `verdict`.

The kissat log file is the raw solver stream: stdout and stderr go straight to an x-created file.

**Criteria (r6:570–574):**
- `kissat_rc20` and `kissat_status_exact == ['s UNSATISFIABLE']`;
- `drat_rc0` and `drat_status_exact == ['s VERIFIED']`;
- `no_fatal_drat_warning`: any WARNING, early EOF or "less than expected" line not in the duplicate-literal class fails;
- `drat_log_filter_ok`;
- `feeds_measured_complete`: both feeds ok, written == expected and sha == expected;
- `proof_relay_complete`: no collector or feeder error, read == fed bytes, collected sha == fed sha;
- `no_stop`: no stop reason and no survivors.

`verdict` is PASS only if all criteria hold; any stop gives STOPPED_UNKNOWN; anything else is FAIL (r6:575).

## 5. What must change for a parent-owned COUNTED replay (assembly r3 §7)
1. **Ownership.** `OUTBASE`/`OUTDIR` live in a parent desk. The parent re-pins every constant in r6:59–89 to reviewed versions and freezes its own script and controls before use.
2. **Admission.** Replace `gate()` and `ga_usage()` (r6:167–197, 579–588) with the parent's own admission:
   - exact per-item reservations;
   - one pipeline per lane rule;
   - the parent monitor or a fresh statvfs reading.

   Drop the HOLD markers and the GA-driver exclusion.
3. **Items and bytes.** Use an explicit 18-id list: 12 direct plus the 6 strengthened, with the §3 construction and GBBINDING identities. Give the native limits per item and keep them inside the 3 h chunk rule.
4. **Own controls, all through the SAME staged relay.** r6 runs only a staged tiny positive (r6:620–625) and a concurrent-path satisfiable-checker control (`control_mismatch`, r6:683–713). The parent version needs:
   - a staged satisfiable-checker rejection;
   - invalid-proof rejections (truncated, empty, wrong-CNF proof fed by `proof_feeder`);
   - a feed-hash-mismatch rejection;
   - the NEW digest-agreement control: retain a tiny control proof and compare its independent sha/bytes with the `collector` and `proof_feeder` records.
5. **Parse-count defence (recommended).** Assert from the checker log:
   - `c parsing input formula with V variables and C clauses` equals the bound header;
   - `c finished parsing, read N bytes from proof file` equals the fed proof bytes.

   r6 relies on the measured-feed equality alone. drat-trim is known to print `s VERIFIED` on a truncated CNF.
6. **Fail-closed and provenance.** Keep the r3 §7 list:
   - unstarted, interrupted, digest-mismatch or binding-mismatch runs are not PASS;
   - weaker formula, weaker checker, skipped cases, lost guards or relaxed caps are forbidden.
7. **Memory.** Staging bounds the peak by the larger stage plus the proof buffer: P0-B1 peaked at 4.91 GB with a 0.77 GB proof. Concurrent transport reached 6.08 GB.

## 6. Worker evidence (not counted)
Kissat 4.0.4 output was reproducible: P1-B4 gave the same proof SHA256 in three runs (probe r1, probe r2, r3).

| Leaf | Transport | Wall s | Kissat s | Proof B | Proof SHA256 | Peak B | Receipt / SHA256 |
|---|---|---|---|---|---|---|---|
| P1-B4 | concurrent r3 | 184.036 | 23.914 | 307290350 | `cebf2feb843bf9c9c1794eb37655a00d22c222152f9de20e46884692a40006b5` | 3687089568 | `L/evidence/gb_direct_v3/run-a1/receipts/GB-P1-B4.json` / `934ac38391903abb15ce890dd7e015f189f70b42bcbc7830deb69ec95c94424e` |
| P0-B4 | concurrent r3 | 185.111 | 23.912 | 306861986 | `1fa34b88ba13ba984f5a21b6356d5a4312cacf24fabe9c7553c2fd529e10cd2d` | 3688498592 | `L/evidence/gb_direct_v3/run-a1/receipts/GB-P0-B4.json` / `e1188c2c918e40e08acb2d63758c4a6b82cecdfed4bc36c10988414904028d06` |
| P0-B5 | concurrent r4 | 183.081 | 23.42 | 307162262 | `946db7dd2547a1206da9849ba2eee9a3e00885b6a654beb1a7d47157ba5967f9` | 3684009352 | `L/evidence/gb_direct_v4/run-b1/receipts/GB-P0-B5.json` / `975af5b2867e38e9435f0bbf436780374e8d6dea941e5e7ed7a617d11ef12647` |
| P0-B6 | concurrent r4 | 441.825 | 163.281 | 760784930 | `662ecb049142a8007f77ca38857fc0cc8236dd3b37f323f199a049484d0506ba` | 5939414600 | `L/evidence/gb_direct_v4/run-b1/receipts/GB-P0-B6.json` / `ec8d10a675731720a91294519414c9f420c7f4ea423bd5e4037878aa991e1631` |
| P1-B6 | concurrent r4 | 412.514 | 156.616 | 764589325 | `e94e586dc2b37f081b3ce299889e06ad9acec0e2ce51373c03ec90beabeea779` | 5388715424 | `L/evidence/gb_direct_v4/run-b1/receipts/GB-P1-B6.json` / `89b2bbce3df45fd017b5e1c71c10683f4d28b1154a678a58397fade60db1fca7` |
| P2-C4 | concurrent r4 | 277.465 | 88.076 | 317663671 | `8a009d1ce9fad9916ec6ee80a45a075bab1a7432f3e9357651ae01c767062645` | 5498963432 | `L/evidence/gb_direct_v4/run-b2/receipts/GB-P2-C4.json` / `e36d1c0d171bd32dcd00f3d7e0ede1c7725a473bef44dfdbcd04e57481650847` |
| P2-C3 | concurrent r4 | 268.175 | 79.901 | 316240754 | `7e0a4a8e0fd2dab68475df8a68012bbd01d7b92f03993566186f8e625f1a3c63` | 6076974496 | `L/evidence/gb_direct_v4/run-b2/receipts/GB-P2-C3.json` / `9255aaeb018c580778284bff4ae22f9ab0cac767ad4fd2231e15b009bdaaa793` |
| P0-B1 | staged r6 | 698.729 | 342.068 | 770042119 | `80aecc158be172b4097fe2865f2d22453f4d5432c221fe595bfb787130bf4caf` | 4914282496 | `L/evidence/gb_direct_v6/run-c1/receipts/GB-P0-B1.json` / `bb0a8ffd7903a16618158d1fff989bbe599d6084cb9e3bc9fd96b55c96888f79` |
