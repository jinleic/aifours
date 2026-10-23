# Research institute — bounded parallel visits

The owner requested three difficult book problems on 2026-10-15: one mathematics, one information-science,
and one physics problem, with a six-hour budget per problem and all three running concurrently.

[`run_parallel.py`](run_parallel.py) runs the existing institute's complete visit lifecycle, not a new
scientific workflow: identify → literature → frozen-contract attack → sandboxed replay → independent
referee → novelty check. The original sequential engine remains a read-only external dependency at
`/Users/jinleic/jinleic-workspace/research-institute/explorer/ri.py`; its SHA-256 is pinned by each selection.
It uses the delegate models from the workspace's `DELEGATE_MODELS.json` without changing them.

## Budget

The limits below apply separately to each of the three visits. They are ceilings, not promises of a
solution or of six hours of continuous model work. A visit may close earlier for prior art, no precise
question, a settled result, or a justified scientific stop. There is no automatic refill or revisit.

The owner authorized fresh six-hour allocations after the first batch's identification failures.
That recovery, batch 02 (engine epoch 1), began at **12:02:24 PT on 2026-10-15**. Batch 03 (engine
epoch 2) used only the unused allocation, with no fresh budget. It reused the identification and literature gates.

| Allocation | Math minutes | Info minutes | Physics minutes |
|---|---:|---:|---:|
| Consumed in batch 02 (epoch 1) | 55.4 | 93.5 | 54.1 |
| Batch 03 attack ceiling | 204.6 | 166.5 | 205.9 |
| Batch 03 replay ceiling | 30 | 30 | 30 |
| Batch 03 independent-review ceiling | 45 | 45 | 45 |
| Batch 03 novelty-check ceiling | 15 | 15 | 15 |
| Overhead and teardown reserve | 10 | 10 | 10 |
| **Cumulative fresh allocation** | **360** | **360** | **360** |

The table contains rounded ceilings, not time already spent. The original recovery wall-clock cutoff
is **18:02:24 PT** and takes precedence over any unused stage quota. A one-off process-exit watcher
requests graceful supervisor shutdown at 18:00:24 PT if that exact supervisor is still running;
it checks the run identity and PID/start identity before signalling. It installs no recurring scheduler.
See [`review/approved-deadline-watchdog.json`](review/approved-deadline-watchdog.json).
Parent replay of finalized artifacts is reported separately from model/engine-attempt time.
Actor limits are four CPU threads, 4 GB RAM, and 1 GB new disk per problem.

Usage limits, auth or CLI faults, an exhausted subscription window, low disk, credential material in
output, operator interruption, or an unexpected lane crash stop all three visits rather than producing
bogus outcomes. A lane-specific failure or an expired lane stops only that lane. The batch is `done`
only if every visit closed with a research outcome; otherwise `run.json` says `incomplete` or `stopped`.
Approved requeues open new epochs with separate runtime caches, retaining earlier records and source
renders. Validation still refuses live executors from any earlier epoch. The checker reports current
epoch and lifetime usage separately; the owner-approved recovery must also sum epochs 1 and 2.
Final usage was 246.9, 166.8 and 79.9 minutes for mathematics, information science and physics.

## Selection and launch

Selection catalogs and original page images live under the three volume evidence directories:

- [Mathematics](../mathematics/evidence/mathematics-hard-20261015/catalog.md)
- [Information science](../information-science/evidence/information-science-hard-20261015/catalog.md)
- [Physics](../physics/evidence/physics-hard-20261015/catalog.md)

The selected IDs, baseline, bounded attack, review requirements, and source pins are frozen in the run's
`selection.json`. The launcher refuses a closed article, existing AI4S ownership, a duplicate or missing
volume, a changed engine or source PDF, quotas that do not leave the reserve, run data outside
`institute/runs/<run>/`, a live executor recorded by any runner, or a resumed record that this launcher
did not start or whose contract pins another selection. Selected source bundles and feasibility
prototypes are hash-checked and copied into the isolated attack directory as `selection-inputs/`.

From the repository root:

```sh
python3 -B institute/run_parallel.py institute/runs/hard-2026-10-15/selection.json --check
caffeinate -i python3 -B institute/run_parallel.py institute/runs/hard-2026-10-15/selection.json
```

Run the second command in a real terminal or tmux. Do not install a scheduler. Ctrl-C or SIGTERM stops
all three visits. Each lane latches the first signal, ignores later ones during teardown, lets the
engine's watchdog stop its executor, then sweeps any remaining descendants. Model and replay executor
PID/start identities are published in each lane's liveness file and retained by the supervisor,
including descendant identities, so an abruptly killed lane can still be cleaned up. One supervisor holds
the original machine-wide kernel lock; forked lanes inherit it, so live orphans still exclude another
runner. Each lane has isolated machine-local work and liveness state under
`~/.local/state/research-explorer/parallel/`; the launcher checks both those files and the original
engine's liveness file before starting. The scientific interpreter is
`~/.local/state/research-explorer/venv/bin/python`; no vanished workspace scratch environment was restored.

## Records and evidence

The run directory owns `problems/<id>/record.json` and `attack-e<epoch>/` exactly as the original engine
does. Never hand-edit these or generated `INDEX.md`/`TABLE.md`. `run.json` is the supervisor receipt;
`problems/<id>/lane.json` records each lane's PID, allocation, elapsed time, and stopping status. Only
the supervisor renders shared indexes. Requeues append epochs through the original engine; they must
not reset a consumed budget without fresh owner authorization. Terminal summary, extra parent checks
and budget accounting for the 2026-10-15 run: [`review/hard-2026-10-15-outcomes.md`](review/hard-2026-10-15-outcomes.md).

The owner subsequently authorized continued reasonable research beyond that completed allocation.
The [continuation contract](review/continuation-20261015/README.md) preserves the new obligations;
the [continuation outcome ledger](review/continuation-20261015/outcomes.md) records the longer
finite exclusion, Boolean structural obstruction and numerical/formal SAT endpoints. These are
later, separately checked findings, not new engine verdicts. No batch 04 or scheduler ran.
The launcher's six-hour visit checkpoints remain, but are no longer a total research limit.
More engine time still uses explicit `ri.py requeue`; prior records and attack snapshots are unchanged.

The frozen attack contract binds exactly one owner-selected target. It records the identified
counterpart, any other questions the literature stage proposed, and the selection's SHA-256. A finite
range or special case remains a sub-question; it does not settle the book's full conjecture. Search
misses do not establish openness or novelty. A model referee's acceptance is not human peer review.

## Verification

```sh
python3 -B institute/tests/test_parallel.py
python3 -B /Users/jinleic/jinleic-workspace/research-institute/explorer/test_ri.py
```

The seventeen launcher checks make no model calls. They exercise real process overlap and kernel-lock
exclusion; normal and forced cancellation; crashed workers and reparented model/replay executors;
shared deadlines; completed-sibling classification; target binding; input pins; path containment; and
approved requeue behavior with fresh caches and a selected-question identification prompt. The original
engine has 34 passing contract tests. Five parent-checker tests exercise sandboxed claim replay,
rejected counterexamples, live-snapshot refusal, permitted snapshot writes, denied outside writes,
and separate current-epoch/lifetime budget accounting. Observed recovery results:
[`review/recovery-smoke.json`](review/recovery-smoke.json); initial results:
[`review/parallel-smoke.json`](review/parallel-smoke.json). Generated records own scientific outcomes.

Historical design and calibration: [`docs/DESIGN.md`](docs/DESIGN.md),
[`docs/smoke-2026-10-14.md`](docs/smoke-2026-10-14.md).
