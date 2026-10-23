# LKTS(57) and LKTS(87): existence theorems checked by the Lean kernel

**Result.** The Lean 4.34.1 kernel accepts these two theorems, built from the pinned raw certificates:

```lean
Kirkman.KernelCert.exists_lkts57 : ∃ (B : Fin 55 → Kirkman.Blocks 57), Kirkman.IsLKTS B
Kirkman.KernelCert.exists_lkts87 : ∃ (B : Fin 85 → Kirkman.Blocks 87), Kirkman.IsLKTS B
```

For both, `#print axioms` reports `[propext, Classical.choice, Quot.sound]`. Each is a finite existence theorem for one order only. Neither proves `Kirkman.FullGoal`, the statement for every t ≥ 1. No novelty or priority claim is made.

## Is the statement faithful?

- **Definitions.** `LktsKernel/PriorFormal.lean` is a byte-identical copy of `../lkts57-construction-snapshot-v1/PriorFormal.lean` (SHA-256 `a39613c9…2dee`). The `gen`, `57` and `87` targets of `reproduce.sh` stop if that hash changes. `IsSTS`, `IsParallelClass`, `IsResolution`, `IsKTS` and `IsLKTS` are used unchanged; their `#print` output is in `logs/Cert57.build.log`.
- **Witness.** The witness is `blocksOf v data`:
  - `blocksOf v d i = {T : Triple v | ∃ c : Fin ((v-1)/2), ∃ r : Fin (v/3), T.val = rowSet v (rowAt d i c r)}`.
  - `rowSet v (a,b,c) = {x : Fin v | x.val = a ∨ x.val = b ∨ x.val = c}`.
  - `rowAt d i c r` is row `r` of `CLASS c` of `KTS i` of the raw file.
  - `lkts57_blocks_spec` and `lkts87_blocks_spec` restate this by `Iff.rfl`. The resolution classes are `classesOf v d i c`.
- **Data binding.** `gen_data.py` checks the raw file's SHA-256 and copies every row verbatim in raw order. It does not sort or repair anything. Two successive regenerations of all generated modules gave identical hashes (`logs/post-regen.sha256`, `logs/regen2.sha256`). Between the first two generations only the `Cert*` files changed, by one added `set_option pp.funBinderTypes` display line (`logs/pre-regen.sha256`).

| input | SHA-256 | systems × classes × rows |
|---|---|---|
| `lkts57-construction-snapshot-v1/lkts57_g513.txt` | `09a9d8ca…5f09` | 55 × 28 × 19 = 29,260 |
| `lkts87-parent-inputs-v1/lkts87_g903.txt` | `65ab29ae…273e` | 85 × 43 × 29 = 105,995 |

## How the kernel checks it

`isLKTS_of_check` (in `LktsKernel/Generic.lean`) is proved once, for every `v` and every data list `d`. Its hypotheses are Boolean or list facts, not design properties:

1. `d.length = v - 2`, proved by `rfl`.
2. `∀ s ∈ d, sysOK v (fullPairs v) s = true`, proved by one `decide +kernel` per system. Each system must have:
   - `(v-1)/2` classes of `v/3` rows;
   - every row strictly increasing and `< v`;
   - in each class, point masks that are pairwise disjoint and whose union is `2^v - 1`;
   - class pair masks (bit `v·x+y`) that are pairwise disjoint and whose union is the mask of all pairs.
3. `(allRows d).Nodup`, proved by `nodup_of_rankFold`. A bitmask fold sets bit `rank(row)`, the colexicographic rank, and fails on any repeat.
   - It is evaluated in kernel segments: 5 for 57 and 11 for 87. The hexadecimal accumulators between segments are claims that the kernel checks, joined by `rankFold_append`.
   - The final accumulators are `2^29260 - 1` and `2^105995 - 1`. They are recorded but not needed.
4. `(v-2)·((v-1)/2·(v/3)) = choose v 3`, proved by `decide +kernel`.

From these hypotheses the generic proof derives the rest:
- **Uniqueness.** Pair uniqueness and point uniqueness come from mask disjointness.
- **Injectivity.** The row map `Fin (v-2) × Fin ((v-1)/2) × Fin (v/3) → Triple v` is injective:
  - rows in different systems are distinct by `Nodup`;
  - rows in different classes of one system are distinct by the class pair masks;
  - rows in one class are distinct by the point masks.
- **Bijectivity and coverage.** Counting (`Fintype.card_finset_len`) makes the injective map bijective, which gives coverage of every triple without a triple scan.
- **Disjointness.** Constituents and classes are disjoint because the map is injective.

All kernel arithmetic is on `Nat` literals. The Lean kernel evaluates these with GMP; this is the standard kernel acceleration that plain `decide` also relies on. Nothing uses `native_decide`, `Lean.ofReduceBool`, `sorry`, a new `axiom`, `implemented_by` or `extern`. The data modules use `set_option maxHeartbeats 0` and `maxRecDepth 4096`; these are elaborator limits only, needed to parse the large literals.

## Measured (this Mac, `lean -j 4`, `/usr/bin/time -l`)

| step | wall | peak RSS | exit |
|---|---|---|---|
| PriorFormal (frozen copy) | 1.68 s | 1.68 GB | 0 |
| Generic (checker + soundness) | 2.05 s | 1.72 GB | 0 |
| Data57 | 12.6 s | 1.88 GB | 0 |
| **Cert57** (55 `sysOK` + 5 rank segments + theorem) | **35.1 s** | **2.11 GB** | **0** |
| Data87 | 74.1 s | 6.59 GB | 0 |
| **Cert87** (85 `sysOK` + 11 rank segments + theorem) | **132.7 s** | **2.70 GB** | **0** |

The largest RSS, 6.59 GB, is the elaborator parsing the 105,995-row literal with four threads, not kernel work. All build logs are in `logs/`.

## Altered-certificate controls (`controls/`, `make_controls.py`)

| control | change | full pipeline (`Cert57Swap` / `Cert57Dup`) | positive diagnostics (`Diag57*`, exit 0) |
|---|---|---|---|
| swap (`c9d9c0d2…52a2`) | KTS 0 CLASS 0: `0 19 38`, `1 7 11` → `0 11 19`, `1 7 38` | **exit 1**. The kernel rejects `data57swap_sys0`, then `_rank3` and `_rank4`; the final theorem depends on `sorryAx` | Every class of the altered KTS 0 is still a partition. `swap_sys0_fail` shows `sysOK = false` for KTS 0. `swap_not_sts` proves that KTS 0 is **not an STS**: pair {0,11} lies in blocks {0,11,19} and {0,11,14}. Hence `swap_not_lkts` |
| dupsys (`afe7e17c…2b35`) | classes of KTS 54 replaced by a copy of KTS 0 | **exit 1**. The kernel rejects **only** `data57dup_rank4`; `data57dup_sys` still depends only on `propext` | `dup_sys54_ok` shows the copied system passes `sysOK`. `dup_rankFold_fails` holds. `dup_not_lkts` proves the constituents are **not pairwise disjoint**: {0,19,38} lies in both constituent 0 and constituent 54 |

The swap control necessarily breaks two things. It breaks the STS property of KTS 0. Because an LKTS uses every triple exactly once, the new triples also already occur in KTS 43 and KTS 48. The dupsys control isolates the cross-system check.

## Independent replay (`leanchecker`, the toolchain's lean4checker)

`sh reproduce.sh replay57` and `sh reproduce.sh replay87` re-check every declaration of each compiled module with the kernel, in a new process, against the imported environment. All runs exited 0, and each verbose log contains its `replaying <module>` line:

| module | wall | peak RSS |
|---|---|---|
| PriorFormal / Generic | 2.4 s / 2.5 s | 1.34 GB |
| Data57 / Data87 | 1.8 s / 1.9 s | 0.40 / 0.41 GB |
| Cert57 | 36.4 s | 1.72 GB |
| Cert87 | 138.5 s | 2.12 GB |

**Fresh-environment replay.** `sh fresh_replay.sh LktsKernel.Cert57` and `sh fresh_replay.sh LktsKernel.Cert87` run `leanchecker --fresh`. It replays every constant the certificate depends on into an empty kernel environment: Init, the imported Mathlib closure, PriorFormal, Generic, the data and the certificate. Both exited 0:

| module | wall | peak RSS |
|---|---|---|
| Cert57 | 135.5 s | 2.05 GB |
| Cert87 | 224.7 s | 2.30 GB |

The logs are `logs/replay-fresh.*`.

**Limit.** These replays run the same Lean kernel implementation in a separate process. They are not an independent kernel such as nanoda or lean4lean, and no Comparator run was made.

## Environment and deviation

- **Toolchain.** Lean 4.34.1 (commit `5045d005…`) from `~/.elan`.
- **Cache.** The cache named in the assignment, `scratch/rh-quasi-lean-2026-10-07/lean`, no longer exists. A whole-filesystem search found no copy.
- **Substitute.** The only Lean 4.34.1 project with a fully built Mathlib is `/private/tmp/seymour-lean-20261014-68365` (an openai/math-style project, Mathlib `d13f23b7…`). It is used read-only through `LEAN_PATH` (`lean_env.sh`), with no `lake` and no writes to the cache.
- **Check on the substitute.** The frozen PriorFormal compiles there unchanged; its 25 axiom reports are all standard (`attempts/00-env-smoke`).
- **Limits.** At most 4 Lean threads (`-j 4`); peak RSS below 8 GiB; no downloads. No delegate or external model was used for this lane; this worker is anthropic/claude-opus-5-5. Timestamps are from the host clock.

## Reproduce

```sh
sh reproduce.sh gen        # regenerate modules from the raw files (SHA-256 checked)
sh reproduce.sh 57         # PriorFormal, Generic, Data57, Cert57
sh reproduce.sh 87         # ... Data87, Cert87
sh reproduce.sh controls   # Cert57Swap/Cert57Dup must fail; Diag57Swap/Diag57Dup must pass
sh reproduce.sh replay57   # leanchecker -v on the four modules (same for replay87)
sh fresh_replay.sh LktsKernel.Cert57   # leanchecker --fresh, guarded at 7.5 GiB (same for Cert87)
python3 write_result.py    # rebuild result.json from the files and logs
```

## Files

- **Lean sources.**
  - `LktsKernel/PriorFormal.lean` (frozen copy) and `Generic.lean` (checker, soundness).
  - `Data57.lean`, `Data87.lean` (generated data).
  - `Cert57.lean`, `Cert87.lean` (generated certificates).
  - `Control/` (control data, certificates and diagnostics).
- **Scripts.** `gen_data.py`, `gen_cert.py`, `make_controls.py`, `lean_env.sh`, `build_module.sh`, `reproduce.sh`, `fresh_replay.sh`, `write_result.py`.
- **Outputs.** `build/` (oleans), `logs/` (every build and replay log, with time and RSS).
- **Earlier attempts.** `attempts/NOTES.md`. It covers the environment smoke test, the data-elaboration failures (heartbeat limit, recursion depth), kernel profiling, and the first design. That design passed for 57 at 5.29 GB but would not fit 87, so it was superseded.
- **Summary.** `result.json`.
