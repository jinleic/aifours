# Difficult-problem run — 2026-10-15

Owner request: run three difficult problems in parallel, one from each source volume, with a six-hour
target per problem, and keep the work in `/Users/jinleic/repos/aifours`.

| Volume | Article | Selected target | Baseline before launch | Six-hour success boundary |
|---|---|---|---|---|
| Mathematics | `math-p0039` 凯莱 (Cayley) 图和相关的问题 | Geometric nonexistence of non-Desarguesian flag-transitive projective planes, stated by the article | Thas–Zagier: no such plane of order `n < 2×10^11` | A verified longer finite range is partial; the all-orders conjecture remains open unless proved |
| Information science | `info-p0403` 弹性布尔函数的非线性度的紧上界 | Is there a balanced nine-variable Boolean function with nonlinearity at least 242? | Best located balanced value: 240 | An explicit verified truth table settles existence; class or local exclusions are partial |
| Physics | `phys-p0422` 用统计物理学方法处理约束满足问题面临的五个挑战 | Rigorous upper bounds on random 4-SAT and 5-SAT thresholds | 10.23 and 21.33 in the opened Achlioptas–Peres table | Fully proved smaller bounds are partial progress on Challenge 5, not exact thresholds |

The budget is a 21,600-second ceiling per problem, not a guarantee of continuous model work or of a
result. See [`config.json`](config.json) for stage allocations and [`selection.json`](selection.json)
for frozen questions, input hashes, resource limits, and scope rules.

Batch 01 began at 04:03:10 PT. Its preserved receipts are in [`batches/01/`](batches/01/receipt.json):
mathematics closed `unverified`; information science and physics timed out in identification.
With owner approval, batch 02 restarted all three at 12:02:24 PT with fresh six-hour budgets. All three
closed `unverified` after referee `accept-with-fixes`, using 0.9 h (math), 1.6 h (information science)
and 0.9 h (physics). Receipts are in [`batches/02/`](batches/02/receipt.json). Batch 03 ran from
14:23:47 to 17:36:09 PT as attack-stage requeues inside the same approved budget. All three again closed
`unverified` after `accept-with-fixes`. Referees judged no claim wrong and requested only wording or
control fixes. The wrapper's parent check passed all 36 claim contracts; 32 had executable replay
commands and four were proof-only entries. Receipts are in [`batches/03/`](batches/03/receipt.json).
No batch 04 ran because the approved 18:02:24 PT cutoff left too little time. Results, extra parent
checks and budget accounting are in [`hard-2026-10-15-outcomes.md`](../../review/hard-2026-10-15-outcomes.md).

The owner later authorized continued scientifically reasonable research beyond that cutoff.
The [separate continuation ledger](../../review/continuation-20261015/outcomes.md) records its
longer exact plane exclusion, accepted Boolean residue-type obstruction and numerical/formal SAT
endpoints. Those findings do not rewrite this run's records or create a batch 04 verdict.


Start from the repository root:

```sh
institute/launch_tmux.sh
```

Inspect progress:

```sh
tmux attach -t aifours-hard-20261015
python3 -B /Users/jinleic/jinleic-workspace/research-institute/explorer/ri.py --root institute/runs/hard-2026-10-15 status
```

After completion, the wrapper has already replayed delivered claim commands on sandboxed temporary snapshots;
the exact receipt is `parent-check.json` and its log is `parent-check.log`. A manual rerun is:

```sh
python3 -B institute/check_run.py institute/runs/hard-2026-10-15
```

Records under `problems/` and generated `INDEX.md`/`TABLE.md` are the authority. Do not edit them.
