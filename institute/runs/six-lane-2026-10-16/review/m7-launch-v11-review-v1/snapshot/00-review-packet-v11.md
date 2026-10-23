# M7 B-side parent replay desk: review packet v11 (Codex HOLD on v10, items 1-5)

Generated 2026-10-18T08:19:48-07:00 by M7BCubeParentReplay. Desk: `review/moqls7-k3-B-cube-parent-replay-v1/`. This packet supersedes `review-packet-v10.md` (b2588083082d748dc106b2a6db8381bf3944b315bfa8e2a7b5a3be678a848f9b) for launch purposes. The staged files are in `staging-Bcuts/`. `scripts/` is unchanged while B_C321-a3 (launch_B_v8) runs. B_C411-p1 and B_C311cuts-p1 launch only under `launch_B_v11.py`, after Codex's re-review and Main's explicit GO.

## Inputs

- `review/m7-launch-v10-codex-v1.note.md` 6556 B sha256 `f8f86f0d26ddff922bf3ba9a91d994144073b39730a80bb9366c7f78595153f8` (HOLD, items 1-5).
- Main's relay of that review:
  - item 4 is satisfied by POLICY, through a single-admitter invariant;
  - item 5 requires the hash-pinned producer receipt and the composition/append sources in this packet.
- Earlier inputs are listed in `review-packet-v10.md`.

## Staged files (`staging-Bcuts/`)

| file | bytes | sha256 |
|---|---|---|
| `bklib_v3.py` | 44858 | `51d34190e25001862699642558de0b157734096e9472ac25e2040bda11c406bc` |
| `compose_Bcuts_v1.py` | 8586 | `a5d303fda264026ae9ed644618da0d9142dfeaf6e98ec065bfbcc630a96907dc` |
| `replay_B_v4.py` | 24442 | `1a67794572b2b8b9c73737f3581f85c474c94a544b0f090ed6e0af77fd19f03f` |
| `launch_B_v9.py` | 35581 | `dee90b9bb30819a73c591dfb03d6bd60fb046a08ca7a555ecc3668320305960f` |
| `assemble_B_v9.py` | 40739 | `9c3c4241b53360df2c3ac7c4b1d8269ce0d266d72f2843c3b643b073afd7226c` |
| `launch_B_v10.py` | 63837 | `d55f12186deac37c2d74d359dcf2df26c286f03d1df3aa6af9c197635a38afad` |
| `assemble_B_v10.py` | 45469 | `3339537292a83aa3dc9a7918a7fdf2f084960ebd56773573dfb3cd9848882dee` |
| `launch_B_v11.py` | 73253 | `80557d31a45ca565059e7703927e98cc58acadd6a7692ca156e21c66dc734bd4` |
| `assemble_B_v11.py` | 47919 | `eda1df172383291bd32b8166b4cb6f76c527c5dce7bfab3e2091cec84b6db0ee` |

v11 changes only `launch_B_v11.py` and `assemble_B_v11.py`. bklib_v3, compose_Bcuts_v1 and replay_B_v4 are the reviewed v9 files, byte-identical.

## Diffs (desk root)

| diff | bytes | sha256 |
|---|---|---|
| `scripts-v8-to-v9-Bcuts.r2.diff` | 34600 | `54385cd424128e71ca2eca46ede11df930c8b74788a13c3c732de97110641e20` |
| `scripts-v8-to-v9-Bcuts.diff` | 31613 | `4fef55ab4f66bd57fe391f40bf3476494e8984dd5055e8cd9cf4da3787545ae3` |
| `scripts-v9-to-v10.diff` | 71254 | `f262ea22ecb061b9ec030039a6ab6d5a1701bd4ce3814dea8ac122a1724e673d` |
| `assembler-v5-to-v6-generalization.diff` | 27152 | `ca3e4e65fe5bb9b83331415cdc616c9c0e25e247a993c2c7c62a37bc3f8b9971` |
| `scripts-v10-to-v11.diff` | 47039 | `f824df65619d3019fd24d4945426ae26bf70b1212556b4e3f948274cbe8fc566` |

## Self-test evidence

- Binding: `receipts/test-v11-selftest-r2.selftest.json` 28187 B sha256 `ccb66053613e353dc3c9d95581cff5b876f1e656725a3bb0e59dfbf12b515d02`, all_ok True. It was produced by `launch_B_v11.py` sha256 `80557d31a45ca565059e7703927e98cc58acadd6a7692ca156e21c66dc734bd4`, the file in the table above.
- Earlier run: `receipts/test-v11-selftest.selftest.json` sha256 `650670065949cf0cc96edf1250a55b87c95f18f35b19cb57cc950ad9f3510ac2`, all_ok true. It used an earlier v11 draft with CENSUS_TRIES = 8. That draft needed 6 tries in that census, so the bound was raised to 15; the draft was never used.

| case | pid | pgid | sid | rc | SIGTERM after s | unreaped after bounded wait | blocking wait | readers (eof, exception) | seconds | ok |
|---|---|---|---|---|---|---|---|---|---|---|
| ps_ok | 94554 | 94554 | 94554 | 0 | None | False | False | {'stdout': (True, None), 'stderr': (True, None)} | 0.034 | True |
| term_honoring | 94555 | 94555 | 94555 | -15 | 2.008 | False | False | {'stdout': (True, None), 'stderr': (True, None)} | 2.029 | False |
| term_ignoring | 94571 | 94571 | 94571 | 0 | 2.014 | True | True | {'stdout': (True, None), 'stderr': (True, None)} | 8.063 | False |
| nonzero_rc | 94637 | 94637 | 94637 | 1 | None | False | False | {'stdout': (True, None), 'stderr': (True, None)} | 0.028 | False |
| stderr_output | 94638 | 94638 | 94638 | 0 | None | False | False | {'stdout': (True, None), 'stderr': (True, None)} | 0.054 | False |

Signals sent (os.kill instrumented): [{"pid": 94555, "signal": "SIGTERM", "t": 2.041}, {"pid": 94571, "signal": "SIGTERM", "t": 4.077}]. The test process: pid 94550, pgid 94550, sid 94550.

Checks, including the v11 parser and reader cases: ps_ok_is_ok_rc0_own_pid=True, term_honoring_one_sigterm_at_limit_reaped_in_bounded_wait=True, term_ignoring_one_sigterm_then_blocking_wait_until_self_exit=True, exactly_two_signals_both_sigterm_to_owned_helpers=True, timed_helpers_in_own_sessions=True, nonzero_rc_not_ok=True, stderr_output_not_ok=True, every_helper_reaped_no_lost_child=True, readers_explicit_eof_no_exception_all_cases=True, pump_records_eof=True, pump_records_exception_without_eof=True, lsof_complete_record_resolved=True, lsof_n_without_fcwd_malformed=True, lsof_missing_fcwd_unresolved=True, lsof_non_absolute_path_unresolved=True, lsof_other_fd_malformed=True, lsof_duplicate_pid_malformed=True, ps_negative_rss_malformed=True, ps_negative_pid_malformed=True, ps_uid_minus2_normalized=True, ps_empty_args_parsed_and_unresolved=True, zombie_and_parenthesized_args_unresolved=True, census_complete=True.

Census at 2026-10-18T08:16:17-07:00: tries ['unresolved', 'unresolved', 'unresolved', 'unresolved', 'complete']; counts {"first": 1188, "args": 1187, "lsof": 803, "second": 1187}.

- Retry details (unresolved identities): [[{"pid": 94650, "uid": 501, "state": "S", "comm": "sleep", "consistent": false, "args_resolved": false, "cwd_resolved": false}, {"pid": 94652, "uid": 501, "state": "Rs+", "comm": "omo-11ccacdc/lib/node_modules/@evolocity-lab/operad/node_modules/bun/bin/bun.exe", "consistent": false, "args_resolved": false, "cwd_resolved": false}, {"pid": 94640, "uid": 89, "state": "S", "comm": "work/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/mdworker_shared", "consistent": false, "args_resolved": true, "cwd_resolved": false}, {"pid": 94651, "uid": 89, "state": "S", "comm": "work/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/mdworker_shared", "consistent": false, "args_resolved": false, "cwd_resolved": false}], [{"pid": 94686, "uid": 501, "state": "S", "comm": "sleep", "consistent": false, "args_resolved": false, "cwd_resolved": false}, {"pid": 94693, "uid": 501, "state": "Rs+", "comm": "omo-11ccacdc/lib/node_modules/@evolocity-lab/operad/node_modules/bun/bin/bun.exe", "consistent": false, "args_resolved": false, "cwd_resolved": false}, {"pid": 94691, "uid": 89, "state": "Ss", "comm": "cs.framework/Versions/A/XPCServices/CGPDFService.xpc/Contents/MacOS/CGPDFService", "consistent": false, "args_resolved": false, "cwd_resolved": false}, {"pid": 94692, "uid": 269, "state": "Ss", "comm": "/usr/libexec/ReportMemoryException", "consistent": false, "args_resolved": false, "cwd_resolved": false}], [{"pid": 94712, "uid": 501, "state": "S", "comm": "sleep", "consistent": .
- Busy 2: [[74330, 'drat-trim'], [75121, 'drat-trim']].
- Foreign lane natives (pid, route_A5): [[74330, True]].
- Desk attempt processes, from the running a3: [[73730, 'Python'], [75097, 'Python'], [75099, 'Python'], [75121, 'drat-trim']].
- B/C411 matches: 0.

Informational admission, no launch: not ok, because of ['cap_at_least_min', 'ancestry_headroom_for_fixed_cap', 'desk_idle_no_other_attempt_process'].

Monitor stability: ok True; age 4.0 s; 31 window samples spanning 300.0 s; free_last 182056779776; max_drop 1280446464; limit 14046398314.666666.

## Mapping of the Codex v10 items to v11 (`launch_B_v11.py` line ranges)

1. **Monitor freshness at launch (BLOCKER).** `mode_run` (789-932):
   - `monitor_stability()` (682-748) is evaluated before the final census (`stab`) and AGAIN after it (`stab2`); both must be ok;
   - the pre-spawn guard also recomputes `time.time() - stab2.t_last_epoch` and requires 0..30 s, together with free >= GATE, `deadline_ok()`, no signals and no `*.QUARANTINE.json`;
   - the gate receipt records both evaluations (`stability`, `stability_after_final_census`) and `prespawn_recheck.monitor_last_sample_age_seconds`.
2. **Identity agreement and veto (MAJOR).** `census_once` (484-618):
   - consistent means present in A and C with equal ppid/pgid/uid/lstart/comm, plus args with the same lstart in B; absence from A is unresolved;
   - an own-uid live process with unresolved identity or cwd goes to `unresolved`;
   - every other non-skipped process (any uid, zombies included) without consistent resolved argv goes to `veto_unresolved`. `unresolved_args` (478-481) treats empty, `<defunct>` and parenthesized comm as unresolved;
   - both lists trigger a retry; `census` (621-641) retries up to 15 times, 2 s apart, then refuses;
   - the B/C411 veto then matches only resolved full argv, with no comm fallback;
   - zombies stay out of busy/RSS, and slot identity is checked independently.
3. **Helper output (MAJOR).**
   - `_pump` (312-322) records explicit EOF or the exception that ended it;
   - `run_helper` (339-416) requires both readers finished with EOF and no exception;
   - `parse_lsof` (456-475) is a state machine requiring `p` -> `fcwd` -> `n`. A missing `fcwd` or a non-absolute path leaves the cwd unresolved; any other tag, order or fd raises (e.g. `p42\nnunknown\n` raises);
   - `parse_ps_id` (419-437) requires non-negative decimal pid/ppid/pgid/rss and pid >= 1. uid is printed signed by ps (nobody = -2), must lie in [-2^31, 2^32) and is normalized mod 2^32. Rejecting -2 outright would refuse every census on this host, because uid -2 processes exist.
4. **Admission serialization (MAJOR): Main's single-admitter POLICY.**
   - `ADMITTER_INVARIANT` (190-194) is recorded in every gate receipt (`prepare`, 761-786).
   - `admission_v11` (655-664) adds `foreign_lane_natives_only_route_A5_slot1`: every lane native whose ancestry has no process with cwd in this desk must have `ROUTE_A5` (line 189: `C311cuts_A_r9` or `k3_cuts_certify_r9.py A`) on itself or an ancestor.
   - This desk's own attempts are serialized by `desk_idle_no_other_attempt_process`.
5. **Producer provenance (MAJOR).** See the next section.

## Item 5: hash-pinned producer receipt and composition/append sources

Copies made with lstat S_ISREG checks and exclusive create; each SHA-256 was re-checked against its pin. Directory: `review-packet-v11-sources/` (the lane path, with `/` replaced by `__`).

| lane file (M7-relative) | copy | bytes | sha256 (pin) | role |
|---|---|---|---|---|
| `evidence/k3cubes/C311cuts_B_r6/C311cuts_B.json` | `evidence__k3cubes__C311cuts_B_r6__C311cuts_B.json` | 8302 | `1f00363467d3ed30787cd1b3e4c2e695b8b4d7249623fc6e3994130f4be6c535` | producer route-B r6 receipt |
| `code/k3_cuts_certify_r6.py` | `code__k3_cuts_certify_r6.py` | 33885 | `12b141fd8e1e2997dec8966d66b2e5b1532069b3bd579f676201514cf271db91` | producer driver (receipt driver_sha256): regenerate_b/prepare composition and append |
| `code/gram_encB.py` | `code__gram_encB.py` | 8206 | `c7583efe838816d39fe33456af09897cc2a1f5633d1e57e1ee63b3e5238e2b45` | encoder B |
| `code/gram_enc.py` | `code__gram_enc.py` | 7296 | `b2c206d8bf4896868fb4e45cd87c633a6cfbb0d62c8fdb62b146ac84a7d38833` | encoder A (imported by k3_cubes, k3_cuts_r1) |
| `code/k3_cubes.py` | `code__k3_cubes.py` | 6101 | `70c79c624dd4c4ad0929a41790b7674eaa7343f3fcb5802c5e0c1abdbfb30550` | cube wrapper: variable_map, cube_clauses, make |
| `code/k3_lex.py` | `code__k3_lex.py` | 5945 | `2b721e85812cd7b3438771868f63da1e10f3fbeed6551f7888f74a399e159b10` | imported by k3_cuts_r1 |
| `code/k3_cuts_r1.py` | `code__k3_cuts_r1.py` | 20815 | `0ec92c861024a728aa38d238fda2d7f5f056fae12cb0f474a15db0335b6e1b0a` | AMENDMENT-4 cut block: emit |
| `explore/k3cubes/B_C311.meta.json` | `explore__k3cubes__B_C311.meta.json` | 814 | `bfa298eea4a6b102a16e15663d42c2cdf86ab7ab093f86bdecb7d8bf8d28a056` | B_C311 input metadata |
| `evidence/k3cubes/bmap_oracle_r1.json` | `evidence__k3cubes__bmap_oracle_r1.json` | 4688 | `6e2bd95ee38c615ab2a1a6282531da730b2bf0cc45e104e95b850102e0b1952c` | B-map oracle receipt |

Binding chain:
- producer receipt `driver_sha256` = `12b141fd...db91` = `code__k3_cuts_certify_r6.py`;
- receipt `environment.modules` = the gram_enc/k3_cubes/k3_lex/k3_cuts_r1 pins above;
- `prepared.input_sha256` b3ec0108...c077, `prepared.block_sha256` 05f31da4...e6dd (238,140 clauses), `prepared.strengthened_sha256` ae3b8309...783a;
- `bindings.oracle_receipt_sha256` = the bmap oracle receipt pin;
- `prepared.regeneration.B_C311_metadata_sha256` = the B_C311 meta pin.
`bklib_v3.producer_evidence_cuts` checks each of these; the v9 static check found every one true.

### Producer composition and append: `code__k3_cuts_certify_r6.py`

```python
  83  BLOCK_SHA = "05f31da497315877347f7d780e0e6f4c9c4799c8becee3bdb192a8420ff6e6dd"
```
```python
  84  BLOCK_CLAUSES = 238140
```
```python
 118  def dimacs_line(clause):
 119      return (" ".join(map(str, clause)) + " 0\n").encode()
```
```python
 122  def dimacs_header(nv, nc):
 123      return ("p cnf %d %d\n" % (nv, nc)).encode()
```
```python
 126  def digest(parts):
 127      h = hashlib.sha256()
 128      for part in parts:
 129          h.update(part)
 130      return h.hexdigest()
```
```python
 294  def b_base_output():
 295      command = ["/usr/bin/python3", "-B", os.path.join(HERE, "gram_encB.py"),
 296                 "--squares", "3", "--heavy", "--sym", "--out", "/dev/stdout"]
 297      out = subprocess.run(command, check=True, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
 298                           stderr=subprocess.PIPE).stdout
 299      first_end = out.index(b"\n") + 1
 300      fields = out[:first_end].decode().split()
 301      stats_start = out.rindex(b"\n", 0, len(out) - 1) + 1
 302      if len(fields) != 4 or fields[:2] != ["p", "cnf"] or not out[stats_start:].startswith(b"vars ") \
 303              or out.count(b"\n", first_end, stats_start) != int(fields[3]):
 304          raise AssertionError("encoder B output is not header + exactly nc clause lines + stats line")
 305      return int(fields[2]), int(fields[3]), out[first_end:stats_start]
```
```python
 308  def regenerate_b(route, oracle):
 309      meta_path = lane_path(route["input_meta"])
 310      with open(meta_path) as f:
 311          meta = json.load(f)
 312      check_b_c311_binding(meta, sha(meta_path), oracle)
 313      nv, nbase, base_body = b_base_output()
 314      base_sha = digest([dimacs_header(nv, nbase), base_body])
 315      if base_sha != route["base_sha256"] or base_sha != oracle["B_base"]["sha256"] \
 316              or [nv, nbase] != [oracle["B_base"]["variables"], oracle["B_base"]["clauses"]]:
 317          raise AssertionError("regenerated B base differs from the oracle base")
 318      cube, _, _ = k3_cubes.cube_clauses(k3_cubes.variable_map(), "C311")
 319      body = base_body + b"".join(dimacs_line(cl) for cl in cube)
 320      del base_body
 321      return (nv, nbase + len(cube)), body, {"base_sha256": base_sha, "base_header": [nv, nbase],
 322                                             "cube_clauses": len(cube), "B_C311_metadata_sha256": sha(meta_path),
 323                                             "B_C311_bound_to_oracle_base_wrapper_encoder": True,
 324                                             "method": "gram_encB.py stdout (k3_cube_certify_r3 method) + k3_cubes C311"}
```
```python
 327  def prepare(route_name, oracle):
 328      """Regenerate the named input in memory, append the re-emitted block, and assert every pre-solve binding."""
 329      route = ROUTES[route_name]
 330      if route_name == "A":
 331          (nv, nc), body, regen = regenerate_a(route)
 332      else:
 333          (nv, nc), body, regen = regenerate_b(route, oracle)
 334      input_parts = [dimacs_header(nv, nc), body]
 335      check_header(input_parts, route["input_header"])
 336      check_body(body, nc)
 337      check_input(input_parts, route["input_sha256"])
 338      check_prefix_against_file(lane_path(route["input"]), input_parts)
 339      clauses = k3_cuts_r1.emit(k3_cubes.variable_map())
 340      block = b"".join(dimacs_line(c) for c in clauses)
 341      check_block(block, clauses)
 342      del clauses
 343      parts = [dimacs_header(nv, nc + BLOCK_CLAUSES), body, block]
 344      check_header(parts, route["strengthened_header"])
 345      check_body(block, BLOCK_CLAUSES)
 346      strengthened_sha = digest(parts)
 347      return {"parts": parts, "sha256": strengthened_sha, "bytes": sum(len(p) for p in parts),
 348              "summary": {"instance": route["instance"], "input": route["input"], "input_sha256": route["input_sha256"],
 349                          "input_header": list(route["input_header"]), "strengthened_header": [nv, nc + BLOCK_CLAUSES],
 350                          "block_sha256": BLOCK_SHA, "block_clauses": BLOCK_CLAUSES, "block_bytes": len(block),
 351                          "input_prefix_equal_to_named_file": True, "strengthened_sha256": strengthened_sha,
 352                          "strengthened_bytes": sum(len(p) for p in parts), "regeneration": regen,
 353                          "block_map": "k3_cubes.variable_map(); equal to encoder B's map by the PASS oracle"}}
```

ROUTES['B'] (lines 91-111 of the same file) pins the input `explore/k3cubes/B_C311.cnf` b3ec0108...c077, the meta, the base 42a5f304...0aac and the input/strengthened headers (461370, 1629802)/(461370, 1867942).

### Cube composition (`code__k3_cubes.py`: `CUBES`, `variable_map`, `cube_clauses`, `make`)

```python
  19  CUBES = {"C311": ({1, 2, 3}, {4}, {5}),
  20           "C321": ({1, 2, 3}, {4, 5}, {6}),
  21           "C411": ({1, 2, 3, 4}, {5}, {6})}
```
```python
  58  def variable_map():
  59      # Written independently of encoder A's map. Encoder B allocates exactly
  60      # this prefix: square, earlier point, later point, skipping common lines.
  61      result = {}
  62      for a in (1, 2, 3):
  63          for p, q in itertools.combinations(PTS, 2):
  64              if p[0] != q[0] and p[1] != q[1]:
  65                  result[(a, p, q)] = len(result) + 1
  66      assert len(result) == 2646
  67      return result
```
```python
  70  def cube_clauses(vmap, name):
  71      supports = CUBES[name]
  72      def g(a, p, q):
  73          return vmap.get((a, min(p, q), max(p, q)))
  74      clauses = []
  75      for a, S in enumerate(supports, 1):
  76          for k in range(1, 7):
  77              v = g(a, POINT, (0, k))
  78              assert v is not None
  79              clauses.append([v if k in S else -v])
  80      n_units = len(clauses)
  81      singletons = []
  82      for a, S in enumerate(supports, 1):
  83          if len(S) != 1:
  84              continue
  85          q = (0, next(iter(S)))
  86          singletons.append({"square": a, "p": POINT, "q": q})
  87          for t in PTS:
  88              if t in (POINT, q):
  89                  continue
  90              left, right = g(a, POINT, t), g(a, q, t)
  91              if left is None and right is None:
  92                  continue
  93              if left is None:
  94                  clauses.append([-right])
  95              elif right is None:
  96                  clauses.append([-left])
  97              else:
  98                  clauses.extend(([-left, right], [left, -right]))
  99      return clauses, n_units, singletons
```
```python
 102  def make(encoder, cube, outcnf, outmeta):
 103      for path in (outcnf, outmeta):
 104          if os.path.exists(path):
 105              raise FileExistsError(path)
 106      coverage()
 107      vmap = variable_map()
 108      # Base output is a disposable scratch product, never frozen evidence.
 109      scratch = os.path.join(HERE, "..", "explore", "scratch")
 110      os.makedirs(scratch, exist_ok=True)
 111      if encoder == "A":
 112          F, actual = gram_enc.build(3, None, True, True, None)
 113          expected = {"%d|%d,%d|%d,%d" % (a, p[0], p[1], q[0], q[1]): v
 114                      for (a, p, q), v in vmap.items()}
 115          assert actual == expected
 116          base = F.text()
 117      else:
 118          basepath = os.path.join(scratch, "k3_cube_B_base.cnf")
 119          subprocess.run(["/usr/bin/python3", "-B", os.path.join(HERE, "gram_encB.py"),
 120                          "--squares", "3", "--heavy", "--sym", "--out", basepath],
 121                         check=True, capture_output=True)
 122          with open(basepath) as f:
 123              base = f.read()
 124      header, body = base.split("\n", 1)
 125      tag, form, nv, nc = header.split()
 126      assert (tag, form) == ("p", "cnf") and int(nv) >= len(vmap)
 127      clauses, units, twins = cube_clauses(vmap, cube)
 128      with open(outcnf, "x") as f:
 129          f.write("p cnf %s %d\n" % (nv, int(nc) + len(clauses)))
 130          f.write(body)
 131          for cl in clauses:
 132              f.write(" ".join(map(str, cl)) + " 0\n")
 133      meta = {"encoder": encoder, "cube": cube, "base_cnf_sha256": hashlib.sha256(base.encode()).hexdigest(),
 134              "cnf_sha256": digest(outcnf), "wrapper_sha256": digest(__file__),
 135              "base_encoder_sha256": digest(os.path.join(HERE, "gram_enc.py" if encoder == "A" else "gram_encB.py")),
 136              "support_sets": [sorted(S) for S in CUBES[cube]], "cube_unit_clauses": units,
 137              "same_ray_identities": twins, "extra_clauses": len(clauses)}
 138      with open(outmeta, "x") as f:
 139          json.dump(meta, f, indent=2)
 140          f.write("\n")
 141      print(json.dumps(meta))
```

### Cut block (`code__k3_cuts_r1.py`: constants, `positions`, `off_points`, `template`, `emit`)

```python
  40  N = 7
```
```python
  42  PTS = [(r, c) for r in range(N) for c in range(N)]
```
```python
  43  FRAMES = [("row", k) for k in range(N)] + [("col", k) for k in range(N)]
```
```python
  44  SQUARES = (1, 2, 3)
```
```python
  67  def positions(frame, p):
  68      kind, k = frame
  69      if kind == "row":
  70          return [(k, c) for c in range(N) if c != p[1]]
  71      return [(r, k) for r in range(N) if r != p[0]]
```
```python
  74  def off_points(frame):
  75      on = set(frame_cells(frame))
  76      return [q for q in PTS if q not in on]
```
```python
  79  def template():
  80      out = []
  81      for x in SQUARES:
  82          for R in itertools.combinations(range(6), 4):
  83              out.append(((x, R),))
  84      for x, y in itertools.permutations(SQUARES, 2):
  85          for R in itertools.combinations(range(6), 3):
  86              rest = [i for i in range(6) if i not in R]
  87              for T in itertools.combinations(rest, 2):
  88                  out.append(((x, R), (y, T)))
  89      return out
```
```python
  92  def emit(lit_map, positions_fn=positions):
  93      tpl = template()
  94      clauses = []
  95      for frame in FRAMES:
  96          for p in off_points(frame):
  97              pos = positions_fn(frame, p)
  98              for clause in tpl:
  99                  lits = []
 100                  for x, idxs in clause:
 101                      for i in idxs:
 102                          r = pos[i]
 103                          lits.append(-lit_map[(x, min(p, r), max(p, r))])
 104                  clauses.append(tuple(lits))
 105      return clauses
```

`gram_encB.py main()` is lines 92-217 of `code__gram_encB.py`. compose_Bcuts_v1 runs it unchanged with `--squares 3 --heavy --sym --out /dev/fd/W`, the producer's argv apart from the output path.

### The desk's restatement: `staging-Bcuts/compose_Bcuts_v1.py` `main` (lines 104-167)

```python
 104  def main():
 105      t0 = time.monotonic()
 106      if len(sys.argv) != 2 or sys.argv[1] != "C311":
 107          raise SystemExit(__doc__)
 108      mods = {}
 109      for name in ("gram_enc", "k3_cubes", "k3_lex", "k3_cuts_r1", "gram_encB"):
 110          mods[name] = load(name)
 111      k3, lex, cuts = mods["k3_cubes"][0], mods["k3_lex"][0], mods["k3_cuts_r1"][0]
 112      if not (k3.gram_enc is mods["gram_enc"][0] and lex.k3_cubes is k3 and cuts.k3_cubes is k3
 113              and cuts.k3_lex is lex and cuts.gram_enc is mods["gram_enc"][0]):
 114          raise SystemExit("a lane module bound an unverified dependency")
 115      cov = k3.coverage()
 116      vmap = k3.variable_map()
 117      t_enc = time.monotonic()
 118      base, stats = run_encoder_b(mods["gram_encB"][0])
 119      enc_seconds = round(time.monotonic() - t_enc, 3)
 120      header, body = base.split(b"\n", 1)
 121      tag, form, nv, nc = header.split()
 122      if not ((tag, form) == (b"p", b"cnf") and int(nv) >= len(vmap)):
 123          raise SystemExit("unexpected base header %r" % header)
 124      if stats != "vars %d clauses %d\n" % (int(nv), int(nc)):
 125          raise SystemExit("encoder B stats line %r does not match its header %r" % (stats, header))
 126      if not body.endswith(b"\n") or body.count(b"\n") != int(nc):
 127          raise SystemExit("encoder B body is not exactly nc newline-terminated clause lines")
 128      empty_clause_lines = sum(1 for ln in body.split(b"\n")[:-1] if ln.split() == [b"0"])
 129      cube, units, twins = k3.cube_clauses(vmap, "C311")
 130      extra = lines(cube)
 131      nc_in = int(nc) + len(cube)
 132      input_bytes = b"p cnf %s %d\n" % (nv, nc_in) + body + extra
 133      input_sha = hashlib.sha256(input_bytes).hexdigest()
 134      if input_sha != INPUT_SHA256 or (int(nv), nc_in) != INPUT_HEADER:
 135          raise SystemExit("regenerated B_C311 input %s %r differs from the pin" % (input_sha, (int(nv), nc_in)))
 136      del input_bytes
 137      block_clauses = cuts.emit(k3.variable_map())
 138      block = lines(block_clauses)
 139      block_sha = hashlib.sha256(block).hexdigest()
 140      if block_sha != BLOCK_SHA256 or len(block_clauses) != BLOCK_CLAUSES:
 141          raise SystemExit("cut block %s (%d clauses) differs from the pin" % (block_sha, len(block_clauses)))
 142      out = b"p cnf %d %d\n" % (int(nv), nc_in + len(block_clauses)) + body + extra + block
 143      out_sha = hashlib.sha256(out).hexdigest()
 144      if out_sha != OUTPUT_SHA256 or (int(nv), nc_in + len(block_clauses)) != OUTPUT_HEADER:
 145          raise SystemExit("strengthened output %s differs from the pin" % out_sha)
 146      info = {"cube": "C311", "encoder": "B", "kind": "C311 + AMENDMENT-4 cuts",
 147              "modules": {n: {"path": LANE_CODE + "/" + PINS[n][0], "sha256": m[1], "bytes": m[2]}
 148                          for n, m in mods.items()},
 149              "gram_encB": {"argv": ENC_B_ARGS + ["--out", "/dev/fd/<in-process pipe>"], "seconds": enc_seconds,
 150                            "stats_line": stats.strip()},
 151              "coverage": {"status": cov["status"], "n_valid": cov["n_valid"],
 152                           "complete_disjoint_cover": cov["complete_disjoint_cover"]},
 153              "vmap_entries": len(vmap),
 154              "base_cnf_sha256": hashlib.sha256(base).hexdigest(), "base_bytes": len(base),
 155              "base_header": [int(nv), int(nc)], "base_empty_clause_lines": empty_clause_lines,
 156              "support_sets": [sorted(S) for S in k3.CUBES["C311"]], "cube_unit_clauses": units,
 157              "same_ray_identities": json.loads(json.dumps(twins)), "extra_clauses": len(cube),
 158              "input_sha256": input_sha, "input_header": [int(nv), nc_in],
 159              "block_sha256": block_sha, "block_clauses": len(block_clauses), "block_bytes": len(block),
 160              "out_header": [int(nv), nc_in + len(block_clauses)], "out_bytes": len(out), "out_sha256": out_sha,
 161              "python": sys.version.split()[0], "python_executable": sys.executable,
 162              "ru_maxrss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 163              "seconds": round(time.monotonic() - t0, 3)}
 164      sys.stdout.buffer.write(out)
 165      sys.stdout.buffer.flush()
 166      sys.stderr.write(json.dumps(info, sort_keys=True) + "\n")
 167      sys.stderr.flush()
```

Correspondence:
- input = `p cnf nv (nc + len(cube))` + base body + `lines(cube)`; this equals `regenerate_b` + `prepare`'s `input_parts`, and k3_cubes.make's B branch;
- block = `lines(k3_cuts_r1.emit(k3_cubes.variable_map()))`; this equals `prepare`'s `dimacs_line` join;
- output = `p cnf nv (nc_in + 238140)` + body + cube lines + block; this equals `prepare`'s `parts`;
- the input (b3ec0108...), block (05f31da4..., 238,140) and output (ae3b8309...) pins are asserted in-process. The one test run gave stdout sha ae3b8309...783a.

### The producer receipt, embedded (`evidence__k3cubes__C311cuts_B_r6__C311cuts_B.json`, sha256 `1f003634...c535`)

```json
{
  "route": "B",
  "status": "VERIFIED_UNSAT_CASE",
  "verified_unsat": true,
  "started_at": "2026-10-18T04:59:28-07:00",
  "supervisor": {
    "supervisor_pid": 60539,
    "supervisor_script": "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/code/supervise_r3.py",
    "supervisor_sha256": "0ee8f39496fa3d6051639e99f10d907b8adadcb5d3446f2bb6242c924a83ec4d",
    "supervisor_record": "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/evidence/k3cubes/C311cuts_B_r6.supervisor.json"
  },
  "bindings": {
    "amendment_sha256": "75ac7aece0f050160bf147be91eec906ab99e68294bf9f70feb453b9bcbd9a91",
    "delta_sha256": "899a04375ca79ca39de9d315a6a3be2bc8157746fa278d6741f7432c72830681",
    "generator_receipt_sha256": "9624d6127890f90a279ab398888524ed0c5e89376b428e68130ad3bab6db4a24",
    "controls_receipt_sha256": "bb9445a2e62d7ed970bf031784934bfa85dc7c43f552554bf178720128beb3e3",
    "supervisor_controls_receipt_sha256": "3c77be50cbbd9bc07cf44036ac40ab14d21f5805ea03a895bf68f3b11de799de",
    "oracle_receipt_sha256": "6e2bd95ee38c615ab2a1a6282531da730b2bf0cc45e104e95b850102e0b1952c",
    "expected_strengthened_sha256": "ae3b8309601d115e2258782ae3cb793f4dc4b5950064b9536b1eca61521f783a"
  },
  "outer_gates": [
    {
      "at": "2026-10-18T04:59:28-07:00",
      "phase": "before in-memory regeneration and appending",
      "available_bytes": 25957052416,
      "launch_threshold_bytes": 12200000000,
      "projected_retained_growth_bytes": 10485760,
      "status": "PASS"
    },
    {
      "at": "2026-10-18T04:59:30-07:00",
      "phase": "before the native proof pipeline",
      "available_bytes": 25957101568,
      "launch_threshold_bytes": 12200000000,
      "projected_retained_growth_bytes": 10485760,
      "status": "PASS"
    }
  ],
  "prepared": {
    "instance": "original B_C311 + AMENDMENT-4 cuts, encoder B",
    "input": "explore/k3cubes/B_C311.cnf",
    "input_sha256": "b3ec010855ad4abd75ffd6eb57aaa3ff158bc8447625ee2097f5a6057594c077",
    "input_header": [
      461370,
      1629802
    ],
    "strengthened_header": [
      461370,
      1867942
    ],
    "block_sha256": "05f31da497315877347f7d780e0e6f4c9c4799c8becee3bdb192a8420ff6e6dd",
    "block_clauses": 238140,
    "block_bytes": 6974640,
    "input_prefix_equal_to_named_file": true,
    "strengthened_sha256": "ae3b8309601d115e2258782ae3cb793f4dc4b5950064b9536b1eca61521f783a",
    "strengthened_bytes": 38353647,
    "regeneration": {
      "base_sha256": "42a5f30453bba3eb423e78b99b1a8fe6039e1c91c32b6ff1dd72f498fa8e0aac",
      "base_header": [
        461370,
        1629644
      ],
      "cube_clauses": 158,
      "B_C311_metadata_sha256": "bfa298eea4a6b102a16e15663d42c2cdf86ab7ab093f86bdecb7d8bf8d28a056",
      "B_C311_bound_to_oracle_base_wrapper_encoder": true,
      "method": "gram_encB.py stdout (k3_cube_certify_r3 method) + k3_cubes C311"
    },
    "block_map": "k3_cubes.variable_map(); equal to encoder B's map by the PASS oracle"
  },
  "result": {
    "started_at": "2026-10-18T04:59:30-07:00",
    "finished_at": "2026-10-18T06:10:08-07:00",
    "seconds": 4237.757,
    "solver_command": [
      "/opt/homebrew/Cellar/kissat/4.0.4/bin/kissat",
      "-q",
      "-f",
      "--time=3600",
      "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/evidence/k3cubes/C311cuts_B_r6/C311cuts_B.solver-cnf.fifo",
      "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/evidence/k3cubes/C311cuts_B_r6/C311cuts_B.drat.fifo"
    ],
    "checker_command": [
      "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/env/drat-trim/drat-trim",
      "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/evidence/k3cubes/C311cuts_B_r6/C311cuts_B.checker-cnf.fifo",
      "-i",
      "-t",
      "7200"
    ],
    "solver_rc": 20,
    "checker_rc": 0,
    "checker_status_lines": [
      "s VERIFIED"
    ],
    "solver_status_lines": [
      "s UNSATISFIABLE"
    ],
    "status_parse_rule": "bytes; remove only b'\\r'; split b'\\n'; lines starting b's '; no stripping",
    "transport_verified": true,
    "peak_sampled_aggregate_rss_bytes": 1467531264,
    "safety_stop_reason": null,
    "stop_error": null,
    "children_alive_after_stop": [],
    "feeds": {
      "solver": {
        "bytes_written": 38353647,
        "sha256": "ae3b8309601d115e2258782ae3cb793f4dc4b5950064b9536b1eca61521f783a"
      },
      "checker": {
        "bytes_written": 38353647,
        "sha256": "ae3b8309601d115e2258782ae3cb793f4dc4b5950064b9536b1eca61521f783a"
      }
    },
    "feed_threads_alive_after_join": [],
    "solver_binary": "/opt/homebrew/Cellar/kissat/4.0.4/bin/kissat",
    "solver_binary_sha256": "05d6f3e9c402a1fe8853b0746e384e1b3d1c4a550e255f11daa2461d279aa848",
    "checker_binary_sha256": "111b0405566d55629f5d391b80b3220cc7a3ebc3cd406a35895ff65cc9acd5e4",
    "checker_source_sha256": "d834b649f437e091597f5347f259b9f681087f89ca0844d0cee250a1a1a0c2ee",
    "solver_log_sha256": "bde6e1eede96772c07c8ce29fd18088863815bd043aa59a06f11f5838cf8a162",
    "checker_log_sha256": "0cb8eea1761b0f071a72ec2b2ac8615f464bb0dfd7f7f816a7e55e18f1bf7587",
    "checkpoint_log_sha256": "257b7bb1aa98b634bedaf58e46af33c324c9e427db8038f7d3d3d96d651b6022",
    "native_limits_seconds": {
      "solver": 3600,
      "checker": 7200
    },
    "wall_guard_seconds": 7320,
    "transport": "CNF bytes fed from memory into two FIFOs (solver, checker) with per-feed SHA; binary DRAT solver -> FIFO -> drat-trim stdin -i; nonblocking FIFO startup; keepalive writer",
    "storage": "no CNF or proof file; logs, checkpoints and one receipt only"
  },
  "feeds_match_strengthened": true,
  "finished_at": "2026-10-18T06:10:08-07:00",
  "quarantine_present": false,
  "planned_new_retained_bytes": 10485760,
  "environment": {
    "executable": "/Library/Developer/CommandLineTools/usr/bin/python3",
    "version": "3.9.6 (default, Aug 13 2025, 15:58:52) \n[Clang 17.0.0 (clang-1700.3.19.1)]",
    "isolated": true,
    "dont_write_bytecode": true,
    "modules": {
      "gram_enc": {
        "path": "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/code/gram_enc.py",
        "sha256": "b2c206d8bf4896868fb4e45cd87c633a6cfbb0d62c8fdb62b146ac84a7d38833"
      },
      "k3_cubes": {
        "path": "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/code/k3_cubes.py",
        "sha256": "70c79c624dd4c4ad0929a41790b7674eaa7343f3fcb5802c5e0c1abdbfb30550"
      },
      "k3_cuts_r1": {
        "path": "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/code/k3_cuts_r1.py",
        "sha256": "0ec92c861024a728aa38d238fda2d7f5f056fae12cb0f474a15db0335b6e1b0a"
      },
      "k3_lex": {
        "path": "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/code/k3_lex.py",
        "sha256": "2b721e85812cd7b3438771868f63da1e10f3fbeed6551f7888f74a399e159b10"
      },
      "gram_certify_r4": {
        "path": "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/code/gram_certify_r4.py",
        "sha256": "ec540a8700b7933b71605e7b03f86d5ef52ad258a5895d0b558db9819f0fa18a"
      },
      "proof_stream": {
        "path": "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/code/proof_stream.py",
        "sha256": "aa0d5a0bf2fa144a9ec2b7be9b4c7f5de15e8c8a07008780e3966552a56d05de"
      }
    },
    "pid": 60540,
    "driver": {
      "path": "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/code/k3_cuts_certify_r6.py",
      "sha256": "12b141fd8e1e2997dec8966d66b2e5b1532069b3bd579f676201514cf271db91"
    }
  },
  "driver_sha256": "12b141fd8e1e2997dec8966d66b2e5b1532069b3bd579f676201514cf271db91",
  "acceptance_also_requires": "the supervisor record for this run: completed_cleanly true, no trip, no quarantine",
  "authority": "Parent AMENDMENT-4 disposition 3c9373c0...4e44 decisions 1-6; parent source reviews; frozen AMENDMENT-4.r4 and K3-CUTS-CERT-DELTA.r6 (attempt after the external floor stop at 04:09:50)",
  "scope": "One strengthened C311 input on one route; parent replay and composition review remain separate"
}
```

## Exact helper sources (v11)

```python
 312  def _pump(stream, sink, state):
 313      """Reader thread: drains one helper stream. Records an explicit EOF, or the exception that ended it (v11 (3))."""
 314      try:
 315          while True:
 316              chunk = stream.read(1 << 16)
 317              if not chunk:
 318                  state["eof"] = True
 319                  return
 320              sink.append(chunk)
 321      except BaseException as e:
 322          state["exception"] = repr(e)
 323  
 324  
 325  def helper_reap(p, box, ev, flags):
 326      """One waitpid on the owned helper. Ownership ends with the first statement after a successful wait, or on ECHILD
 327      (lost child: recorded, and the helper result is then not ok)."""
 328      try:
 329          pid, st = os.waitpid(box["owned"], flags)
 330      except ChildProcessError as e:
 331          box["owned"] = None
 332          ev["lost_child"] = repr(e)
 333          return
 334      if pid:
 335          box["owned"] = None
 336          p.returncode = ev["rc"] = os.waitstatus_to_exitcode(st)
 337  
 338  
 339  def run_helper(argv, limit=HELPER_LIMIT, term_wait=HELPER_TERM_WAIT):
 340      """Bounded, owned scan helper (ps, lsof), started in its own session: pgid = sid = helper pid, never in this
 341      launcher's group or in any supervised group. stdout and stderr are drained by reader threads. Past `limit` s, or on
 342      an exception after Popen, exactly one SIGTERM goes to the owned, unreaped child (its PID is reserved), then a
 343      bounded wait of `term_wait` s; if the child is still unreaped, a blocking wait with no further signal. Never
 344      SIGKILL, never a subprocess timeout. ok only for rc 0, empty stderr, no SIGTERM, no exception, no lost child, no
 345      wait error, and both reader threads finished with an explicit EOF and no exception."""
 346      t0 = time.monotonic()
 347      ev = {"argv": argv, "pid": None, "pgid": None, "sid": None, "rc": None, "term_sent_after": None,
 348            "unreaped_after_term_wait": False, "blocking_wait": False, "exception": None, "lost_child": None,
 349            "wait_errors": [], "readers_finished": None, "readers": None, "stdout": "", "stderr": "", "seconds": None,
 350            "ok": False}
 351      p = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
 352                           cwd=K.TMP, env=K.ENV, start_new_session=True)
 353      box = {"owned": p.pid}                          # registration: the statement right after Popen
 354      out, err, readers = [], [], []
 355      rstate = {"stdout": {"eof": False, "exception": None}, "stderr": {"eof": False, "exception": None}}
 356      try:
 357          try:
 358              ev["pid"] = box["owned"]
 359              for key, stream, sink in (("stdout", p.stdout, out), ("stderr", p.stderr, err)):
 360                  readers.append(threading.Thread(target=_pump, args=(stream, sink, rstate[key]), daemon=True))
 361                  readers[-1].start()
 362              try:
 363                  ev["pgid"], ev["sid"] = os.getpgid(ev["pid"]), os.getsid(ev["pid"])
 364              except OSError as e:                    # the helper may already have exited (still unreaped)
 365                  ev["pgid"] = ev["sid"] = repr(e)
 366              while box["owned"] is not None:
 367                  helper_reap(p, box, ev, os.WNOHANG)
 368                  if box["owned"] is None:
 369                      break
 370                  elapsed = time.monotonic() - t0
 371                  if ev["term_sent_after"] is None and elapsed >= limit:
 372                      os.kill(box["owned"], signal.SIGTERM)       # owned => unreaped => PID reserved
 373                      ev["term_sent_after"] = round(elapsed, 3)
 374                  elif ev["term_sent_after"] is not None and elapsed >= limit + term_wait:
 375                      ev["unreaped_after_term_wait"] = True
 376                      break
 377                  time.sleep(0.02)
 378          except BaseException as exc:
 379              ev["exception"] = repr(exc)
 380              if box["owned"] is not None and ev["term_sent_after"] is None:
 381                  try:
 382                      os.kill(box["owned"], signal.SIGTERM)
 383                      ev["term_sent_after"] = round(time.monotonic() - t0, 3)
 384                  except BaseException as e:
 385                      ev["wait_errors"].append(repr(e))
 386              end = time.monotonic() + term_wait
 387              while box["owned"] is not None and time.monotonic() < end:
 388                  try:
 389                      helper_reap(p, box, ev, os.WNOHANG)
 390                  except BaseException as e:
 391                      ev["wait_errors"].append(repr(e))
 392                  if box["owned"] is not None:
 393                      time.sleep(0.02)
 394              ev["unreaped_after_term_wait"] = box["owned"] is not None
 395      finally:
 396          while box["owned"] is not None:             # no further signals: wait for the known child to exit
 397              ev["blocking_wait"] = True
 398              try:
 399                  helper_reap(p, box, ev, 0)
 400              except BaseException as e:
 401                  ev["wait_errors"].append(repr(e))
 402                  time.sleep(0.25)
 403      for t in readers:
 404          t.join(10)
 405      ev["readers_finished"] = len(readers) == 2 and not any(t.is_alive() for t in readers)
 406      ev["readers"] = rstate
 407      if ev["readers_finished"]:
 408          p.stdout.close()
 409          p.stderr.close()
 410      ev["stdout"] = b"".join(out).decode("utf-8", "replace")
 411      ev["stderr"] = b"".join(err).decode("utf-8", "replace")
 412      ev["seconds"] = round(time.monotonic() - t0, 3)
 413      ev["ok"] = (ev["rc"] == 0 and ev["term_sent_after"] is None and ev["exception"] is None
 414                  and ev["lost_child"] is None and not ev["wait_errors"] and ev["readers_finished"]
 415                  and all(s["eof"] and s["exception"] is None for s in rstate.values()) and ev["stderr"] == "")
 416      return ev
```

bklib's `_run_text` (unchanged from v1-v3; not called by v11 or by replay_B_v4) is quoted in `review-packet-v10.md`.

## Copy-in and launch plan (after Codex re-review and Main's GO)

1. After B_C321-a3 ends and is assembled with `assemble_B_v8.py`: `cp -n staging-Bcuts/{bklib_v3.py,compose_Bcuts_v1.py,replay_B_v4.py,launch_B_v9.py,assemble_B_v9.py,launch_B_v10.py,assemble_B_v10.py,launch_B_v11.py,assemble_B_v11.py} scripts/`. Then re-hash each file against the table above.
2. `replay_B_v4.py regen B_C311cuts` precheck (B_C411 reuses `receipts/regen-B_C411-r2.json`).
3. `launch_B_v11.py run B_C411 --label B_C411-p1 --regen-tag r2`. After it ends cleanly: `launch_B_v11.py run B_C311cuts --label B_C311cuts-p1`. Assemble each with `assemble_B_v11.py`.

