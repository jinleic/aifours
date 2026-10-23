# Failed and superseded attempts (kept, not deleted)

All runs used the same read-only environment as the final build (`lean_env.sh`).

## 00-env-smoke

The frozen `PriorFormal.lean`, compiled as module `Lkts57Kernel.PriorFormal` before the directory
was renamed to `LktsKernel`: exit 0, 6.14 s wall, 1.68 GB peak RSS, 25 `#print axioms` reports, all
`[propext, Classical.choice, Quot.sound]`.  It showed that the substitute Mathlib cache accepts the
frozen file unchanged.

## Data module elaboration (logs overwritten; values copied from the console at the time)

1. One nested literal `def data : List (List (List (Nat × Nat × Nat)))` holding all 29,260 rows:
   `error: (deterministic) timeout at whnf, maximum number of heartbeats (200000)` at line 813, col
   43; 12.85 s, 1.08 GB peak RSS.  This was an elaboration resource limit, not a kernel or
   certificate failure.
2. The same with `set_option maxHeartbeats 0`: `error: maximum recursion depth has been reached` at
   19:4; 23.77 s, 1.55 GB peak RSS.
3. Final layout: one definition per system with `set_option maxRecDepth 4096`, plus a list of the
   55 (or 85) system constants.  Data57: exit 0, 14.5 s, 1.88 GB.  These logs went to
   `logs/Data57.build.*` and were overwritten by later builds of the same module, so only the values
   above, copied from the console at the time, survive.

## 01-probes

`Probe2.lean` checks lemma names in the substitute Mathlib.  It also shows that `omega` closes the
six-disjunction sorted-triple goal and that `decide +kernel` proves the `choose` identities.

## 02-profile (measured, kept with logs)

| probe | wall | peak RSS |
|---|---|---|
| imports only (baseline) | 1.25 s | 1.63 GB |
| `dataOK 57 data57` (v1 checker, one declaration) | 17.43 s | 5.11 GB |
| v1 `chunkOK` window 0 (all rows scanned) | 8.43 s | 3.37 GB |
| v1 `chunkOK` window 3 | 5.98 s | 2.86 GB |
| traverse `allRows data57` (length) | 3.75 s | 2.40 GB |
| traverse `data57.flatten.flatten` (length) | 2.87 s | 2.17 GB |
| `allRows.all (rowOK 57)` | 7.93 s | 3.22 GB |
| same with kernel-primitive Nat ops | 4.58 s | 2.52 GB |
| `code` via notation | 5.68 s | 2.75 GB |
| `code` via primitives | 4.32 s | 2.48 GB |

Conclusion: kernel memory per declaration grows with the rows touched in that declaration
(roughly 20 KB per row only to traverse, about 120 KB per row for the v1 `dataOK`), and the kernel
frees it between declarations.

## 03-v1-single-dataOK-chunks (passed for 57; superseded)

Sources, logs and timing are in that directory.  It used one `dataOK` declaration and four code-window
scans.  It produced a kernel-checked `exists_lkts57` with axioms `[propext, Classical.choice,
Quot.sound]` in 41.35 s with 5.29 GB peak RSS.  It was replaced, before any result was reported,
because it would not fit LKTS(87) in one declaration.  v2 uses one `sysOK` declaration per system
and a chained rank fold proving `(allRows d).Nodup`.  For v=57, v2 took 33.4 s and 2.12 GB.
