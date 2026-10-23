# M7 B-side parent replay desk: review packet v12 (narrow delta on v11)

Generated 2026-10-18T08:33:53-07:00 by M7BCubeParentReplay. It builds on `review-packet-v11.md` (2fa3d8ba8bdcfdc93b8c0f8ecb406ed1ce4fde0826004947939cf48f9b8fd59c), which Codex reviewed: `review/m7-launch-v11-codex-v1.note.md` 5435 B sha256 `d7ed4c3a078ba765e735b262a29488bcc60ec1256e82243b926454c8abe8c61a`, GO-WITH-FIXES.

The v12 set stays in `staging-Bcuts/` until GO. It is then copied with `cp -n` into a NEW directory `scripts-v12/` and re-hashed. bklib_v4 takes SCRIPTS from its own directory, so the v12 set never touches `scripts/`, whose recording the v11 run B_C411-p1 binds while it is live. B_C311cuts-p1 and A_C311cuts-p1 launch only under v12, after Codex's delta review and Main's GO.

## Files of the v12 set (`staging-Bcuts/` -> `scripts-v12/`)

| file | bytes | sha256 | note |
|---|---|---|---|
| `launch_B_v12.py` | 81680 | `b276de43082f0ea35d1283c22d5caa35f7b33762a18387295a57fb0af7a79fe1` | slots, admission lock, MINOR fix, bklib_v4/replay_B_v5 |
| `assemble_B_v12.py` | 52439 | `e8ed3398c0acbf007aef2583dfd9c62169f62f78478742fea8c0780ae7744d32` | route-A item texts and scope |
| `bklib_v4.py` | 51825 | `6884ff96d2c25e4b59e2b71e053ffba51997fee6350a249a4b47d1a707739af3` | A_C311cuts item, route-aware evidence, SCRIPTS = own dir |
| `replay_B_v5.py` | 24820 | `2278ab9fc257e9616e96df9d6dca54464975fd4ac9a51fbd40e9d2e99d7e0ec0` | import bklib_v4, item-aware scope text |
| `compose_Acuts_v1.py` | 8511 | `286f3c9bab12953782549abb5b3e151744356ca041cd70ff2c337831c3732f39` | NEW route-A composition |
| `compose_Bcuts_v1.py` | 8586 | `a5d303fda264026ae9ed644618da0d9142dfeaf6e98ec065bfbcc630a96907dc` | unchanged (v9-reviewed), copied for the self-contained set |
| `compose_B_v1.py` | 6855 | `d1377f8686727e80a931190034a18f25af617cfbad283f9602d63acf56459283` | unchanged (from scripts/), copied for the self-contained set |

Diff: `scripts-v11-to-v12.diff` 72535 B sha256 `729b65e6696455b41ad21d97d0e954cbded4a648653bb90b78ef98eb8f7ce704` (launch_B_v11 -> v12, assemble_B_v11 -> v12, bklib_v3 -> v4, replay_B_v4 -> v5, new compose_Acuts_v1).

## Changes

1. **Codex v11 MINOR.** In `mode_run` (855-1023), the pre-spawn guard compares the unrounded `age = time.time() - stab2.t_last_epoch` with 0..30 s. Only the recorded `monitor_last_sample_age_seconds` is rounded.
2. **Slots (Main approved).** `run ITEM --label L --slot {1,2} [--regen-tag T]`.
   - `launcher_slot` (513-527) attributes each desk attempt process through the first launcher in its ancestry: `--slot N` gives N; `LEGACY_SLOTS` gives B_C321-a3 (v8) slot 2 and B_C411-p1 (v11) slot 1; anything else is `unknown`.
   - `admission_v12` (704-715) requires the target slot to be free of desk attempts and no `unknown` attribution. This replaces v11's `desk_idle`.
   - The lane totals are unchanged: <= 2 busy at launch, so <= 4 after; lane RSS + 2 GiB <= 8 GiB; ancestry headroom >= the fixed cap, so two 2.8 GB caps fit. The single-admitter invariant and the route-A5 foreign-native rule are unchanged.
   - `DESK_ATTEMPT` now also matches `compose_A*`.
3. **One admission at a time.** `try_lock`/`unlock` (718-724/727-728) take a non-blocking flock on `locks/admission.lock` (empty file, created once, e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855).
   - The lock is taken before the final census and held through spawn and the gate receipt.
   - It is released by a daemon `threading.Timer` 90 s after the spawn, so the new natives are visible to the next census; at once on refusal; or at exit.
   - If the lock is busy, that cycle is not admitted.
4. **Route-A item A_C311cuts** (`bklib_v4`, `compose_Acuts_v1`); see below. Kissat replays it (item deviation D38, approved by Main).
5. **Separate script directory.** bklib_v4 sets `SCRIPTS = dirname(abspath(__file__))`, so the v12 set runs from `scripts-v12/` with its own script hashes. replay_B_v5 also names the item and its composition in the driver scope text.

## Self-test (`receipts/test-v12-selftest.selftest.json`)

- 21774 B sha256 `ebac2b61019a919ad08b256e02afa4dbe18870333075ac222bf87b5b4104a24f`; all_ok True; launcher `b276de43082f0ea35d1283c22d5caa35f7b33762a18387295a57fb0af7a79fe1`; bklib_v4 `6884ff96d2c25e4b59e2b71e053ffba51997fee6350a249a4b47d1a707739af3`.
- Slot attribution cases: {"v12_slot_2": 2, "v12_slot_1_tagged": 1, "legacy_v11_B_C411_p1_slot_1": 1, "legacy_v8_a3_slot_2": 2, "legacy_unlisted_label_unknown": "unknown", "v12_without_slot_unknown": "unknown", "no_launcher_unknown": "unknown"}.
- Lock steps [fd1 acquire, fd2 acquire, fd2 after fd1 release]: [true, false, true].
- The v11 helper, parser and reader cases all pass again.
- Census tries ['unresolved', 'complete']. Occupied slots ['2']; the desk attempts are B_C321-a3's: [[73730, 'Python', 2], [75097, 'Python', 2], [75099, 'Python', 2], [75121, 'drat-trim', 2]]. Busy 1.
- Informational admissions: slot 1 why []; slot 2 why ['target_slot_free_of_desk_attempts']. Monitor: ok True, age 5.6 s.

Static checks (no receipt; observed stdout):
- `compose_Acuts_v1.py C311` from staging: stdout sha256 18583aabb486b2d7fdf2159ed2172c9dfc9b29bbd2e50c63a5d7d94d44ba2e5e. The base, source-cube, input, block and output pins were asserted in-process; base empty-clause lines 0.
- With staged bklib_v4, `producer_evidence` is consistent for B_C321 (20 checks), B_C411 (20), B_C311cuts (22) and A_C311cuts (28).
- `check_regen` on the staged compose outputs gives, for A and B cuts: cnf_hash_match, meta_agreement, cuts pins, and for A also the lex agreement (counts, per-generator counts, generators, source cube), all true.

## Route-A provenance (hash-pinned copies in `review-packet-v12-sources/`)

| lane file (M7-relative) | copy | bytes | sha256 (pin) | role |
|---|---|---|---|---|
| `evidence/k3cubes/C311cuts_A_r9/C311cuts_A.json` | `evidence__k3cubes__C311cuts_A_r9__C311cuts_A.json` | 8289 | `88c154b75e9fa7acb3ec05867d0542b6be4b349c189931ad5217a4f16235f37f` | producer route-A attempt-5 (r9) receipt |
| `code/k3_cuts_certify_r9.py` | `code__k3_cuts_certify_r9.py` | 34029 | `2f0ced454369242c47ee0f1446f433f92230aa58da4af3c3311aed7476077ed3` | producer driver r9 (receipt driver_sha256): regenerate_a/prepare |
| `review/K3-CUTS-CERT-DELTA.r9.json` | `review__K3-CUTS-CERT-DELTA.r9.json` | 17614 | `76f68d348e2265796696ae4dd9626a3855478748f8c236bfaa4ad57c90525487` | delta r9 (receipt bindings.delta_sha256) |
| `explore/k3lex/A_C311.meta.json` | `explore__k3lex__A_C311.meta.json` | 1404 | `7bef0b78007151d94661181244fa8614c114705522b58fc16cf287014bde190d` | route-A input (lex) metadata |
| `explore/k3cubes/A_C311.meta.json` | `explore__k3cubes__A_C311.meta.json` | 814 | `3b2ab04f2b42b799169bdccf3d868f544ba571ff1d72e18d0cf68187a0f4d9ed` | route-A source cube metadata |
| `evidence/k3cubes/C311cuts_A_r9/C311cuts_A.checker.log` | `evidence__k3cubes__C311cuts_A_r9__C311cuts_A.checker.log` | 4407 | `d9f86ef6047881f25cff8eb8dc43e8bc81381a9f1f5ac3264c34419714ff89f1` | producer checker log (lane drat-trim) |
| `review/K3-CUTS-CERT-DELTA.r6.json` | `review__K3-CUTS-CERT-DELTA.r6.json` | 13865 | `899a04375ca79ca39de9d315a6a3be2bc8157746fa278d6741f7432c72830681` | delta r6 (route B; newly checked by bklib_v4) |

gram_enc, k3_cubes, k3_lex and k3_cuts_r1, at the same pins as the receipt's `environment.modules`, are in `review-packet-v11-sources/`.

### Producer route-A composition: `code__k3_cuts_certify_r9.py`

```python
  85  BLOCK_SHA = "05f31da497315877347f7d780e0e6f4c9c4799c8becee3bdb192a8420ff6e6dd"
```
```python
  86  BLOCK_CLAUSES = 238140
```
```python
 120  def dimacs_line(clause):
 121      return (" ".join(map(str, clause)) + " 0\n").encode()
```
```python
 124  def dimacs_header(nv, nc):
 125      return ("p cnf %d %d\n" % (nv, nc)).encode()
```
```python
 128  def digest(parts):
 129      h = hashlib.sha256()
 130      for part in parts:
 131          h.update(part)
 132      return h.hexdigest()
```
```python
 249  def regenerate_a(route):
 250      with open(lane_path(route["source_meta"])) as f:
 251          source_meta = json.load(f)
 252      with open(lane_path(route["input_meta"])) as f:
 253          input_meta = json.load(f)
 254      ok = (sha(lane_path(route["source_meta"])) == route["source_meta_sha256"]
 255            and sha(lane_path(route["input_meta"])) == route["input_meta_sha256"]
 256            and source_meta["cnf_sha256"] == route["source_cube_sha256"]
 257            and source_meta["base_cnf_sha256"] == route["base_sha256"]
 258            and source_meta["base_encoder_sha256"] == CODE_PINS["gram_enc.py"]
 259            and source_meta["wrapper_sha256"] == CODE_PINS["k3_cubes.py"]
 260            and input_meta["source_cube_cnf_sha256"] == route["source_cube_sha256"]
 261            and input_meta["cnf_sha256"] == route["input_sha256"]
 262            and input_meta["wrapper_sha256"] == CODE_PINS["k3_lex.py"]
 263            and input_meta["cube_wrapper_sha256"] == CODE_PINS["k3_cubes.py"]
 264            and input_meta["finite_controls_status"] == "PASS")
 265      if not ok:
 266          raise AssertionError("A lex/source metadata differ from the pins")
 267      vmap = k3_cubes.variable_map()
 268      F, actual_map = gram_enc.build(3, None, True, True, None)
 269      expected_map = {"%d|%d,%d|%d,%d" % (a, p[0], p[1], q[0], q[1]): v for (a, p, q), v in vmap.items()}
 270      if actual_map != expected_map:
 271          raise AssertionError("encoder A map differs from the cube wrapper map")
 272      nv, nbase = F.nv, len(F.cl)
 273      base_body = b"".join(dimacs_line(cl) for cl in F.cl)
 274      del F, actual_map
 275      if digest([dimacs_header(nv, nbase), base_body]) != route["base_sha256"]:
 276          raise AssertionError("regenerated A base differs from its metadata hash")
 277      cube, _, _ = k3_cubes.cube_clauses(vmap, "C311")
 278      cube_body = b"".join(dimacs_line(cl) for cl in cube)
 279      if digest([dimacs_header(nv, nbase + len(cube)), base_body, cube_body]) != route["source_cube_sha256"]:
 280          raise AssertionError("regenerated A original C311 differs from its pin")
 281      lex_nv, lex = nv, []
 282      for gen in k3_lex.generators("C311"):
 283          perm = k3_lex.image(vmap, gen)
 284          lex_nv, clauses = k3_lex.lex_clauses(sorted(perm.items()), lex_nv)
 285          lex.extend(clauses)
 286      if len(lex) != input_meta["extra_clauses"] or lex_nv - nv != input_meta["new_auxiliaries"]:
 287          raise AssertionError("regenerated lex clauses differ from the lex metadata counts")
 288      body = b"".join([base_body, cube_body, b"".join(dimacs_line(cl) for cl in lex)])
 289      del base_body, cube_body
 290      nc = nbase + len(cube) + len(lex)
 291      return (lex_nv, nc), body, {"base_sha256": route["base_sha256"], "source_cube_sha256": route["source_cube_sha256"],
 292                                  "base_header": [nv, nbase], "cube_clauses": len(cube), "lex_clauses": len(lex),
 293                                  "lex_auxiliaries": lex_nv - nv, "method": "gram_enc.build + k3_cubes C311 + k3_lex make"}
```
```python
 329  def prepare(route_name, oracle):
 330      """Regenerate the named input in memory, append the re-emitted block, and assert every pre-solve binding."""
 331      route = ROUTES[route_name]
 332      if route_name == "A":
 333          (nv, nc), body, regen = regenerate_a(route)
 334      else:
 335          (nv, nc), body, regen = regenerate_b(route, oracle)
 336      input_parts = [dimacs_header(nv, nc), body]
 337      check_header(input_parts, route["input_header"])
 338      check_body(body, nc)
 339      check_input(input_parts, route["input_sha256"])
 340      check_prefix_against_file(lane_path(route["input"]), input_parts)
 341      clauses = k3_cuts_r1.emit(k3_cubes.variable_map())
 342      block = b"".join(dimacs_line(c) for c in clauses)
 343      check_block(block, clauses)
 344      del clauses
 345      parts = [dimacs_header(nv, nc + BLOCK_CLAUSES), body, block]
 346      check_header(parts, route["strengthened_header"])
 347      check_body(block, BLOCK_CLAUSES)
 348      strengthened_sha = digest(parts)
 349      return {"parts": parts, "sha256": strengthened_sha, "bytes": sum(len(p) for p in parts),
 350              "summary": {"instance": route["instance"], "input": route["input"], "input_sha256": route["input_sha256"],
 351                          "input_header": list(route["input_header"]), "strengthened_header": [nv, nc + BLOCK_CLAUSES],
 352                          "block_sha256": BLOCK_SHA, "block_clauses": BLOCK_CLAUSES, "block_bytes": len(block),
 353                          "input_prefix_equal_to_named_file": True, "strengthened_sha256": strengthened_sha,
 354                          "strengthened_bytes": sum(len(p) for p in parts), "regeneration": regen,
 355                          "block_map": "k3_cubes.variable_map(); equal to encoder B's map by the PASS oracle"}}
```

ROUTES['A'] is lines 93-113: input explore/k3lex/A_C311.cnf 059be616...8c4f, lex meta 7bef0b78..., source cube 7fca33f1..., source meta 3b2ab04f..., base d0d884f9..., headers (107513, 659168)/(107513, 897308), solver cadical 601c9fa8....

### Lex functions (`review-packet-v11-sources/code__k3_lex.py`) and `gram_enc.build`

```python
  25  def generators(cube):
  26      out = [{"rows": [i, i + 1]} for i in range(2, 6)]
  27      out.extend({"columns": [i, i + 1]} for i in (1, 2))
  28      if cube == "C311":
  29          out.append({"columns": [4, 5], "squares": [2, 3]})
  30      elif cube == "C321":
  31          out.append({"columns": [4, 5]})
  32      else:
  33          out.extend(({"columns": [3, 4]}, {"columns": [5, 6], "squares": [2, 3]}))
  34      return out
```
```python
  43  def image(vmap, gen):
  44      result = {}
  45      for (a, p, q), v in vmap.items():
  46          a2 = swap(a, gen.get("squares"))
  47          p2 = (swap(p[0], gen.get("rows")), swap(p[1], gen.get("columns")))
  48          q2 = (swap(q[0], gen.get("rows")), swap(q[1], gen.get("columns")))
  49          result[v] = vmap[(a2, min(p2, q2), max(p2, q2))]
  50      assert set(result) == set(result.values()) == set(range(1, 2647))
  51      return result
```
```python
  54  def lex_clauses(pairs, nv):
  55      clauses, prefix = [], None
  56      pairs = [(x, y) for x, y in pairs if x != y]
  57      for i, (x, y) in enumerate(pairs):
  58          guard = [-prefix] if prefix is not None else []
  59          clauses.append(guard + [-x, y])
  60          if i + 1 == len(pairs):
  61              continue
  62          nv += 1
  63          next_prefix = nv
  64          # If the previous prefix and the next pair are equal, equality of
  65          # the extended prefix must be true. No reverse implication is needed.
  66          clauses.append(guard + [-x, -y, next_prefix])
  67          clauses.append(guard + [x, y, next_prefix])
  68          prefix = next_prefix
  69      return nv, clauses
```
`gram_enc.build` is lines 54-150 of `review-packet-v11-sources/code__gram_enc.py`; both the producer and the desk call `build(3, None, True, True, None)`.

### The desk's restatement: `compose_Acuts_v1.py` `main` (lines 74-148)

```python
  74  def main():
  75      t0 = time.monotonic()
  76      if len(sys.argv) != 2 or sys.argv[1] != "C311":
  77          raise SystemExit(__doc__)
  78      mods = {}
  79      for name in ("gram_enc", "k3_cubes", "k3_lex", "k3_cuts_r1"):
  80          mods[name] = load(name)
  81      enc, k3, lex, cuts = (mods[n][0] for n in ("gram_enc", "k3_cubes", "k3_lex", "k3_cuts_r1"))
  82      if not (k3.gram_enc is enc and lex.k3_cubes is k3 and cuts.k3_cubes is k3 and cuts.k3_lex is lex
  83              and cuts.gram_enc is enc):
  84          raise SystemExit("a lane module bound an unverified dependency")
  85      cov = k3.coverage()
  86      vmap = k3.variable_map()
  87      t_enc = time.monotonic()
  88      F, amap = enc.build(3, None, True, True, None)
  89      enc_seconds = round(time.monotonic() - t_enc, 3)
  90      expected_map = {"%d|%d,%d|%d,%d" % (a, p[0], p[1], q[0], q[1]): v for (a, p, q), v in vmap.items()}
  91      if amap != expected_map:
  92          raise SystemExit("encoder A map differs from the cube wrapper map")
  93      nv, nbase = F.nv, len(F.cl)
  94      base_body = lines(F.cl)
  95      del F, amap
  96      if (nv, nbase) != BASE_HEADER or hashlib.sha256(header(nv, nbase) + base_body).hexdigest() != BASE_SHA256:
  97          raise SystemExit("regenerated encoder-A base differs from the pin")
  98      empty_clause_lines = sum(1 for ln in base_body.split(b"\n")[:-1] if ln.split() == [b"0"])
  99      cube, units, twins = k3.cube_clauses(vmap, "C311")
 100      cube_body = lines(cube)
 101      source_sha = hashlib.sha256(header(nv, nbase + len(cube)) + base_body + cube_body).hexdigest()
 102      if source_sha != SOURCE_CUBE_SHA256:
 103          raise SystemExit("regenerated A original C311 %s differs from the pin" % source_sha)
 104      lex_nv, lex_cl, per_gen = nv, [], []
 105      for gen in lex.generators("C311"):
 106          perm = lex.image(vmap, gen)
 107          lex_nv, clauses = lex.lex_clauses(sorted(perm.items()), lex_nv)
 108          lex_cl.extend(clauses)
 109          per_gen.append({"generator": gen, "clauses": len(clauses)})
 110      body = base_body + cube_body + lines(lex_cl)
 111      del base_body, cube_body
 112      nc_in = nbase + len(cube) + len(lex_cl)
 113      input_sha = hashlib.sha256(header(lex_nv, nc_in) + body).hexdigest()
 114      if input_sha != INPUT_SHA256 or (lex_nv, nc_in) != INPUT_HEADER:
 115          raise SystemExit("regenerated lex input %s %r differs from the pin" % (input_sha, (lex_nv, nc_in)))
 116      block_clauses = cuts.emit(k3.variable_map())
 117      block = lines(block_clauses)
 118      block_sha = hashlib.sha256(block).hexdigest()
 119      if block_sha != BLOCK_SHA256 or len(block_clauses) != BLOCK_CLAUSES:
 120          raise SystemExit("cut block %s (%d clauses) differs from the pin" % (block_sha, len(block_clauses)))
 121      out = header(lex_nv, nc_in + len(block_clauses)) + body + block
 122      out_sha = hashlib.sha256(out).hexdigest()
 123      if out_sha != OUTPUT_SHA256 or (lex_nv, nc_in + len(block_clauses)) != OUTPUT_HEADER:
 124          raise SystemExit("strengthened output %s differs from the pin" % out_sha)
 125      info = {"cube": "C311", "encoder": "A", "kind": "lex C311 + AMENDMENT-4 cuts (route A)",
 126              "modules": {n: {"path": LANE_CODE + "/" + PINS[n][0], "sha256": m[1], "bytes": m[2]}
 127                          for n, m in mods.items()},
 128              "gram_enc_build": {"call": "build(3, None, True, True, None)", "seconds": enc_seconds,
 129                                 "map_equals_wrapper_map": True},
 130              "coverage": {"status": cov["status"], "n_valid": cov["n_valid"],
 131                           "complete_disjoint_cover": cov["complete_disjoint_cover"]},
 132              "vmap_entries": len(vmap),
 133              "base_cnf_sha256": BASE_SHA256, "base_header": [nv, nbase], "base_empty_clause_lines": empty_clause_lines,
 134              "support_sets": [sorted(S) for S in k3.CUBES["C311"]], "cube_unit_clauses": units,
 135              "same_ray_identities": json.loads(json.dumps(twins)), "extra_clauses": len(cube),
 136              "source_cube_sha256": source_sha,
 137              "lex_generators": json.loads(json.dumps(per_gen)), "lex_clauses": len(lex_cl),
 138              "lex_auxiliaries": lex_nv - nv,
 139              "input_sha256": input_sha, "input_header": [lex_nv, nc_in],
 140              "block_sha256": block_sha, "block_clauses": len(block_clauses), "block_bytes": len(block),
 141              "out_header": [lex_nv, nc_in + len(block_clauses)], "out_bytes": len(out), "out_sha256": out_sha,
 142              "python": sys.version.split()[0], "python_executable": sys.executable,
 143              "ru_maxrss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 144              "seconds": round(time.monotonic() - t0, 3)}
 145      sys.stdout.buffer.write(out)
 146      sys.stdout.buffer.flush()
 147      sys.stderr.write(json.dumps(info, sort_keys=True) + "\n")
 148      sys.stderr.flush()
```

Correspondence with `regenerate_a`/`prepare`:
- the same map check, base body and base pin;
- the same cube lines and source-cube pin;
- the same lex loop: generators in order, `image`, `lex_clauses(sorted(perm.items()), lex_nv)`;
- the same input = header(lex_nv, nbase + cube + lex) + body, and pin;
- the same block = emit(k3_cubes.variable_map()) and pin;
- the same output = header(lex_nv, nc + 238140) + body + block, and pin 18583aab....
The receipt reports base header [96978, 627398], cube 158, lex 31612 clauses / 10535 auxiliaries, input (107513, 659168) and strengthened (107513, 897308), 24,477,803 B. compose_Acuts asserts the same values.

### The route-A producer receipt, embedded (`evidence__k3cubes__C311cuts_A_r9__C311cuts_A.json`)

```json
{
  "route": "A",
  "status": "VERIFIED_UNSAT_CASE",
  "verified_unsat": true,
  "started_at": "2026-10-18T07:20:37-07:00",
  "supervisor": {
    "supervisor_pid": 74322,
    "supervisor_script": "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/code/supervise_r3.py",
    "supervisor_sha256": "0ee8f39496fa3d6051639e99f10d907b8adadcb5d3446f2bb6242c924a83ec4d",
    "supervisor_record": "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/evidence/k3cubes/C311cuts_A_r9.supervisor.json"
  },
  "bindings": {
    "amendment_sha256": "75ac7aece0f050160bf147be91eec906ab99e68294bf9f70feb453b9bcbd9a91",
    "delta_sha256": "76f68d348e2265796696ae4dd9626a3855478748f8c236bfaa4ad57c90525487",
    "generator_receipt_sha256": "9624d6127890f90a279ab398888524ed0c5e89376b428e68130ad3bab6db4a24",
    "controls_receipt_sha256": "bb9445a2e62d7ed970bf031784934bfa85dc7c43f552554bf178720128beb3e3",
    "supervisor_controls_receipt_sha256": "3c77be50cbbd9bc07cf44036ac40ab14d21f5805ea03a895bf68f3b11de799de",
    "oracle_receipt_sha256": "6e2bd95ee38c615ab2a1a6282531da730b2bf0cc45e104e95b850102e0b1952c",
    "expected_strengthened_sha256": "18583aabb486b2d7fdf2159ed2172c9dfc9b29bbd2e50c63a5d7d94d44ba2e5e"
  },
  "outer_gates": [
    {
      "at": "2026-10-18T07:20:37-07:00",
      "phase": "before in-memory regeneration and appending",
      "available_bytes": 189303607296,
      "launch_threshold_bytes": 12200000000,
      "projected_retained_growth_bytes": 10485760,
      "status": "PASS"
    },
    {
      "at": "2026-10-18T07:20:39-07:00",
      "phase": "before the native proof pipeline",
      "available_bytes": 189303508992,
      "launch_threshold_bytes": 12200000000,
      "projected_retained_growth_bytes": 10485760,
      "status": "PASS"
    }
  ],
  "prepared": {
    "instance": "lex C311 (AMENDMENT-3) + AMENDMENT-4 cuts, encoder A",
    "input": "explore/k3lex/A_C311.cnf",
    "input_sha256": "059be6164176ee93c94d93bd47fa1d365477b6c94f3aa867df991f677e1a8c4f",
    "input_header": [
      107513,
      659168
    ],
    "strengthened_header": [
      107513,
      897308
    ],
    "block_sha256": "05f31da497315877347f7d780e0e6f4c9c4799c8becee3bdb192a8420ff6e6dd",
    "block_clauses": 238140,
    "block_bytes": 6974640,
    "input_prefix_equal_to_named_file": true,
    "strengthened_sha256": "18583aabb486b2d7fdf2159ed2172c9dfc9b29bbd2e50c63a5d7d94d44ba2e5e",
    "strengthened_bytes": 24477803,
    "regeneration": {
      "base_sha256": "d0d884f9a0f9715b256da68be97408ae4a55c88d76183c02246a570f115a4388",
      "source_cube_sha256": "7fca33f1e6324cbe17bc44bbea7f8d9188bcac187252d766fb0fa5e39e1c2001",
      "base_header": [
        96978,
        627398
      ],
      "cube_clauses": 158,
      "lex_clauses": 31612,
      "lex_auxiliaries": 10535,
      "method": "gram_enc.build + k3_cubes C311 + k3_lex make"
    },
    "block_map": "k3_cubes.variable_map(); equal to encoder B's map by the PASS oracle"
  },
  "result": {
    "started_at": "2026-10-18T07:20:39-07:00",
    "finished_at": "2026-10-18T08:19:11-07:00",
    "seconds": 3511.49,
    "solver_command": [
      "/opt/homebrew/Cellar/cadical/3.0.1/bin/cadical",
      "-q",
      "-t",
      "3600",
      "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/evidence/k3cubes/C311cuts_A_r9/C311cuts_A.solver-cnf.fifo",
      "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/evidence/k3cubes/C311cuts_A_r9/C311cuts_A.drat.fifo"
    ],
    "checker_command": [
      "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/env/drat-trim/drat-trim",
      "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/evidence/k3cubes/C311cuts_A_r9/C311cuts_A.checker-cnf.fifo",
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
    "peak_sampled_aggregate_rss_bytes": 1115865088,
    "safety_stop_reason": null,
    "stop_error": null,
    "children_alive_after_stop": [],
    "feeds": {
      "solver": {
        "bytes_written": 24477803,
        "sha256": "18583aabb486b2d7fdf2159ed2172c9dfc9b29bbd2e50c63a5d7d94d44ba2e5e"
      },
      "checker": {
        "bytes_written": 24477803,
        "sha256": "18583aabb486b2d7fdf2159ed2172c9dfc9b29bbd2e50c63a5d7d94d44ba2e5e"
      }
    },
    "feed_threads_alive_after_join": [],
    "solver_binary": "/opt/homebrew/Cellar/cadical/3.0.1/bin/cadical",
    "solver_binary_sha256": "601c9fa8ba5d09fd81bb00c89b3e54832f138bccc3422bd8652e8cda4d74d1fa",
    "checker_binary_sha256": "111b0405566d55629f5d391b80b3220cc7a3ebc3cd406a35895ff65cc9acd5e4",
    "checker_source_sha256": "d834b649f437e091597f5347f259b9f681087f89ca0844d0cee250a1a1a0c2ee",
    "solver_log_sha256": "bde6e1eede96772c07c8ce29fd18088863815bd043aa59a06f11f5838cf8a162",
    "checker_log_sha256": "d9f86ef6047881f25cff8eb8dc43e8bc81381a9f1f5ac3264c34419714ff89f1",
    "checkpoint_log_sha256": "835f2b04f9e03bd7427c201b46c7d6b1f1fef007367f676aa0a83690975e539c",
    "native_limits_seconds": {
      "solver": 3600,
      "checker": 7200
    },
    "wall_guard_seconds": 7320,
    "transport": "CNF bytes fed from memory into two FIFOs (solver, checker) with per-feed SHA; binary DRAT solver -> FIFO -> drat-trim stdin -i; nonblocking FIFO startup; keepalive writer",
    "storage": "no CNF or proof file; logs, checkpoints and one receipt only"
  },
  "feeds_match_strengthened": true,
  "finished_at": "2026-10-18T08:19:11-07:00",
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
    "pid": 74323,
    "driver": {
      "path": "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/code/k3_cuts_certify_r9.py",
      "sha256": "2f0ced454369242c47ee0f1446f433f92230aa58da4af3c3311aed7476077ed3"
    }
  },
  "driver_sha256": "2f0ced454369242c47ee0f1446f433f92230aa58da4af3c3311aed7476077ed3",
  "acceptance_also_requires": "the supervisor record for this run: completed_cleanly true, no trip, no quarantine",
  "authority": "Parent AMENDMENT-4 disposition 3c9373c0...4e44 decisions 1-6; parent source reviews; frozen AMENDMENT-4.r4 and K3-CUTS-CERT-DELTA.r9 (route A attempt 5 after the external floor stop at 07:10:39)",
  "scope": "One strengthened C311 input on one route; parent replay and composition review remain separate"
}
```

## Launch plan (after Codex's delta review and Main's GO)

1. `mkdir scripts-v12 && cp -n staging-Bcuts/{launch_B_v12.py,assemble_B_v12.py,bklib_v4.py,replay_B_v5.py,compose_Acuts_v1.py,compose_Bcuts_v1.py} scripts/compose_B_v1.py scripts-v12/`, then re-hash against the table above.
2. Prechecks: `scripts-v12/replay_B_v5.py regen B_C311cuts` and `regen A_C311cuts`. Each is a short encoder run under the driver gate; while it runs it is an `unknown` desk attempt and blocks admissions.
3. `scripts-v12/launch_B_v12.py run B_C311cuts --label B_C311cuts-p1 --slot 2` (slot 2 is free after a3). Then `run A_C311cuts --label A_C311cuts-p1 --slot N` in the first slot that frees, only while launch + 10,380 s <= 17:57 (enforced by deadline_ok).

