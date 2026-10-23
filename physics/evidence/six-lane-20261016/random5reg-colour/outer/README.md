# outer/ — outer cell certificates for Hypothesis 1.1 (frozen scheme, r1 = 1/10000)

Worker PhysRandomColour.OuterBnB. Started 2026-10-17 00:08:47 PDT; results final 01:10 PDT (host clock).
Scheme: `../README.md`, section "FROZEN: outer cell certificate scheme" (00:07:54 PDT). Items 1-4 are unchanged.
This lane covers Delta minus the central box |n_k - 1/9| <= 1/10000 (k = 00,01,10,11). The lane owner certifies
the central box separately.

## Result (checker A: python-flint arb, 200-bit, exact rational bisection replay, `--require-r0 1/10000`)

All nine facet cones Sigma_u were certified directly. No symmetry argument was used.

| cone u | verdict | dual leaves | central leaves | tree nodes | max depth | min margin L* - max U (arb) | producer CPU s | checker s |
|---|---|---|---|---|---|---|---|---|
| (0,0) | PASS | 33,032 | 508 | 67,079 | 54 | 1.72727e-11 | 277.1 | 39.3 |
| (0,1) | PASS | 33,032 | 508 | 67,079 | 54 | 1.72720e-11 | 257.5 | 39.6 |
| (0,2) | PASS | 31,946 | 486 | 64,863 | 54 | 1.72740e-11 | 262.8 | 38.1 |
| (1,0) | PASS | 33,030 | 508 | 67,075 | 54 | 1.72707e-11 | 256.6 | 39.6 |
| (1,1) | PASS | 33,032 | 508 | 67,079 | 54 | 1.72722e-11 | 292.6 | 39.3 |
| (1,2) | PASS | 31,948 | 486 | 64,867 | 54 | 1.72741e-11 | 253.4 | 38.3 |
| (2,0) | PASS | 31,946 | 486 | 64,863 | 54 | 1.72727e-11 | 274.2 | 38.2 |
| (2,1) | PASS | 31,948 | 486 | 64,867 | 54 | 1.72729e-11 | 258.7 | 38.3 |
| (2,2) | PASS | 31,638 | 640 | 64,555 | 53 | 6.22128e-11 | 255.2 | 41.5 |
| total | 9/9 PASS | 291,552 | 4,616 | 592,327 | | 1.7271e-11 | 2,388 | 352 (359 wall) |

- No leaf was rejected, so no leaf had to be re-produced.
- Each `evidence/coneIJ.check.json` stores the exact arb interval of the minimum margin, the sha256 of the certificate, and start/finish stamps.
- The smallest margins (about 1.7e-11) belong to dual cells touching the central box. For example, cone (0,0) node 4132 has its centroid at r = |n - n*|_F = 1.4e-4. There the true gap is only about 1.16 r^2 = 2e-8.
- Arb enclosure widths are about 1e-57. An independent interval checker (checker B) should run at 100 bits or more.
- Cone counts fall into three groups: {00, 01, 10, 11}, {02, 12, 20, 21} and {22}. [INFERENCE] The box is defined in the coordinates n00, n01, n10 and n11, so it is not invariant under the order-72 group, and the producer's tie-breaks depend on vertex order.

What the trusted code checks per cone:
- The tree replays to a partition of Sigma_u = conv(n*, P_sigma/3 : sigma(i) != j), using exact rational midpoints.
- Every 'C' leaf has all 5 vertices in the box. The box is convex, so the whole cell lies inside it.
- Every 'D' leaf satisfies U_y(v) < L* = (5/2) ln 5 + ln(25/24) at all 5 vertices. Here y is in Q^18, the mu0^u are positive rationals, and a_u is as in frozen item 1.
- The frozen chain then gives ln F < L* on the cell. This depends on two lane lemmas that are not re-checked here: slice concavity of psi, and max-entropy duality.

## Files

- `code/bnb_produce.py`: producer. It is a float search only and is never trusted.
- `code/fastdual.py`: vectorised float numerics: the inner Newton solver for the 9 classes, the dual Newton solver, and the float replica of a_u.
- `code/cert_cells.py`: checker A.
- `code/mutation_controls.py`: mutation controls for checker A.
- `code/run_cones.sh`: sequential produce-then-check driver. It runs resumable producer chunks of 25 minutes or less.
- `code/summarize.py`: writes `evidence/summary.json`.
- `code/model.py`, `code/dual.py`: verbatim copies of `../code/`, kept for reference. The outer code does not import them.
- `evidence/coneIJ.json`: certificate trees.
- `evidence/coneIJ.check.json`: checker results. The matching `.check.stdout` and `.check.stderr` files are also kept.
- `evidence/coneIJ.log`: producer logs. They contain the run configuration, progress lines every 30 s, per-job statistics and location histograms, and host timestamps.
- `evidence/driverA.log`, `evidence/driverB.log`: driver logs.
- `evidence/resources/*.time`: `/usr/bin/time -l` output: wall time, CPU time and maximum RSS.
- `evidence/summary.json`: collected per-cone results and resource usage.
- `evidence/profile_cone00_bfs_*.log`: level-by-level profiling runs.
- `evidence/mutations/`: the base certificate and the mutation results.
- `evidence/SHA256SUMS`: hashes of all code and evidence files.
- `archive/work-dirs/coneIJ.work/`: the producer's persisted per-job subtrees (`job_000.json` … `job_031.json`) and `top.json`. These are superseded by the assembled trees and were moved out of `evidence/` after checking. No production job ran longer than the 240 s save interval, so no partial states were written in production.
- `archive/bnb_produce_orig.py`: copy of `../code/bnb_produce.py`.
- `archive/profile_cone00_bfs_killed_at_level10.log`: the first profiling attempt. It was killed when its launching shell exited.

## Commands (from the lane root, `.venv/bin/python` = CPython 3.13.9, numpy 2.5.4, python-flint 0.9.0)

```
.venv/bin/python outer/code/bnb_produce.py FI FJ 1/10000 outer/evidence/coneIJ.json --workdir outer/evidence/coneIJ.work \
    --top-depth 5 --time-limit 1500 --save-every 240 --progress-every 30 --log outer/evidence/coneIJ.log
.venv/bin/python outer/code/cert_cells.py outer/evidence/coneIJ.json outer/evidence/coneIJ.check.json --require-r0 1/10000
outer/code/run_cones.sh "01 02 10 11"
outer/code/run_cones.sh "12 20 21 22"
.venv/bin/python outer/code/bnb_produce.py 0 0 1/10000 /tmp/unused.json --bfs-profile --time-limit 720 --log outer/evidence/profile_cone00_bfs_emetric_mm3.log
.venv/bin/python outer/code/mutation_controls.py outer/evidence/cone00.json outer/evidence/mutations/results_cone00_r1_1over10000.json
.venv/bin/python outer/code/mutation_controls.py outer/evidence/mutations/base_cone00_r1_1over20.json outer/evidence/mutations/results_base_r1_1over20.json
```

`run_cones.sh` runs the first two commands for each listed cone and resumes after exit code 3. Cone (0,0) was run by hand with the same flags. Producer defaults:
- `--safety 5e-12`: accept only if float max U < L* - 5e-12;
- `--split emetric`;
- `--minimax-iters 3`;
- `--lam-eps 1e-3`;
- reuse of the parent's leaf data is on.

## Producer changes against `../code/bnb_produce.py` (heuristics only; frozen items 1-4 untouched)

1. **Instrumentation and persistence.**
   - Progress lines every 30 s go to the producer log. They report cells evaluated, new and reused dual leaves, central leaves, splits, open stack, depth, minimum margin, ms per evaluation, the minimum r and n^u of accepted cells, and histograms of evaluated and accepted cells by dyadic r = |centroid - n*|_F and by decade of the centroid's minimum n^u.
   - Work is split into 32 top-level job cells (depth 5). Each job is an explicit-stack DFS. Its emitted preorder prefix and open stack are saved atomically every 240 s and at the time limit. Rerunning the same command resumes.
   - Resume was exercised on base certificate A: its log `evidence/mutations/base_cone00_r1_1over20.produce.log` shows a 40 s limit, then "time limit, partial saved", then "resume". The assembled tree passes checker A.
   - The `--bfs-profile` mode logs per level.
   - Vertices are exact integers over 9 * 2^240, so central-leaf decisions and midpoints agree exactly with the checker.
2. **Per-cell y (minimax over the 5 vertices).**
   - The leaf data of the parent's best candidate is tried first, with no solve.
   - Then y is set to the dual optimum at the centroid, warm-started from the parent.
   - If that fails, phi(lambda) = min_y sum_v lambda_v U_y(v) is maximised over vertex weights. phi(lambda) equals ln F(n_lambda) plus the Jensen gap of (3/2) sum n ln n. The maximiser lambda gives the y that minimises max_v U_y(v).
   - Each step solves a 5-variable QP model of phi: Q = G H^-1 G^T, with G the vertex gradients in y and H the dual Hessian. It uses active-set enumeration with lambda_v >= 1e-3, followed by a warm dual Newton solve at n_lambda.
   - If the QP optimum is >= L*, no y can pass, so the cell is split at once.
   - mu0^u = exp(theta^u) at the float inner optimum. The y and mu0 values are the exact hex floats.
3. **Split rule.** Bisect the longest edge in the metric sum_u (dn^u)^2 / n^u_mid.
4. **Speed.** The inner problem is batched over the 9 classes. One dual solve takes 0.9-1.9 ms, against 3.5-7.4 ms for `solve_dual` in `../code/dual.py` at the same 4 test points (measured 00:16). An evaluated node averages about 4.2 ms on the loaded host.

## Checker A changes against `../code/cert_cells.py` (no semantic change)

The `a_bound` and vertex inequalities are unchanged, and so are the 'C' test, the exact rational replay, the root, L*, and the 200-bit precision. The flag `--prec` must be at least 128.

Additions:
- The result JSON.
- Positions of failed leaves.
- A graceful FAIL with a reason for truncated, trailing or malformed trees.
- `--require-r0`, which fails the run if `cert['r0']` differs from the frozen r1.
- A cache of the vector (a_u) keyed by the leaf's literal strings. Identical strings give identical rationals. The cache had 0 hits in these trees.

## Profiling: where the cells are, and per-cell cost

Source: `evidence/profile_cone00_bfs_emetric_mm3.log`. This is the complete BFS of cone (0,0): 279 s, 66,571 evaluated nodes, 55 levels.

**Leaves near n\*.**
- From r = 2^-5 down to r = 2^-12, each factor-2 shell of r holds a nearly constant ~2,650 dual leaves.
- The shells hold 2,656 / 2,672 / 2,640 / 2,656 / 2,656 / 2,632 / 2,632 / 2,632 leaves, then 2,368 in [2^-13, 2^-12).
- So the refinement is scale invariant. In total, 23,564 of 33,032 leaves lie at r < 1/16.
- The cost grows linearly in log(1/r1), by about 2,650 leaves per cone for each halving of r1.

**Leaves far from n\*.**
- 9,468 leaves lie at r >= 1/16: 2,848 in [1/4, 1/2), 3,864 in [1/8, 1/4) and 2,756 in [1/16, 1/8).
- This region includes the P/3 corners and the secondary maxima.

**Leaves near the boundary.**
- By centroid minimum n^u, the leaves split as 19,716 (>= 0.1), 11,116 ([0.01, 0.1)), 2,104 ([1e-3, 1e-2)) and 96 ([1e-4, 1e-3)).
- So the boundary layer is not the bottleneck.

**Cost.**
- About 4.2 ms per evaluated node, with 1.29 dual solves per node.
- Of the 27,212 newly solved leaves, 23,682 passed only after the minimax step. Another 5,820 leaves reused the parent's data.

**Heuristic comparison on the same cone (BFS).**
- Same minimax method, Frobenius longest-edge split (`profile_cone00_bfs_euclid_mm3.log`): finished with 35,861 dual leaves and 72,301 nodes in 301 s.
- Original heuristics, centroid y with Frobenius split (`profile_cone00_bfs_euclid_centroid.log`): stopped at its 600 s cap during level 49. By then it had 99,023 dual leaves and about 3,900 cells still open (2,535 unprocessed at level 49 plus 1,378 in the next frontier). Their parents, split at level 48, all lay at r < 2^-10. It used about 7,300-8,900 leaves per dyadic shell near n* and 39,927 leaves at r >= 1/16.
- With the same split rule, the minimax y (with leaf reuse) therefore cuts the leaf count by at least 2.8x. The weighted split saves a further 8%.
- This is consistent with the earlier prototypes not finishing within 15-30 minutes: they used centroid y and a dual solver about 4x slower. [INFERENCE: those runs were not repeated here.]

## Mutation controls for checker A (`evidence/mutations/`)

Two base certificates were used:
- **Base A** is a small finished certificate, `base_cone00_r1_1over20.json`: cone (0,0) at r0 = 1/20, with 9,122 dual and 570 central leaves. The same producer code made it at 00:22-00:24.
- **Base B** is the real `cone00.json`.

"leaf m" is the leaf with the smallest float margin:
- In base A it is node 18851, with r = 0.19.
- In base B it is node 4132, next to the box.

The results JSON calls this leaf `nstar`. "leaf s" is the tightest leaf with r > 0.35, in a P/3 corner.

| id | mutation | base A | base B |
|---|---|---|---|
| g | none (control) | PASS | PASS |
| a | largest y_e of leaf m times 1.1 | FAIL, 1 leaf, margin -1.06e-2 | FAIL, 1 leaf, -1.39e-5 |
| a | largest y_e of leaf s times 1.1 | FAIL, 1 leaf, -3.46e-3 | FAIL, 1 leaf, -3.46e-3 |
| b | mu0^u of leaf m replaced by mu0^u * (1,1,1,2^10) | FAIL, 1 leaf, -2.71 | FAIL, 1 leaf, -1.90 |
| b | the same for leaf s | FAIL, 1 leaf, -5.90 | FAIL, 1 leaf, -3.87 |
| c | L* lowered by 0.02 (checker constant patched in-process) | FAIL, 8,978/9,122 leaves | FAIL, 32,888/33,032 leaves |
| d | one 81-node subtree dropped (second child of split node 8) | FAIL, "tree truncated" | FAIL, "tree truncated" |
| e | r0 set to 1/5000 and checked with `--require-r0 1/10000` | FAIL, r0 guard, and 570 'C' leaves outside the smaller box | FAIL, r0 guard only, 0 leaf failures |
| f | leaf m relabelled 'C' | FAIL, 1 leaf | FAIL, 1 leaf |

Details for (c):
- In both bases, the rejected set equals the float prediction (all leaves with float margin < 0.02).
- It contains 1,344 of the 1,392 leaves with r > 0.35, which are the cells near the secondary maxima and P/3, as intended.
- It also contains almost every other leaf, because branch-and-bound leaves are refined only until they pass, so most leaf margins are below 0.02.
- In base B, 27,176 of the rejected leaves lie at r < 0.15.

Details for (e), base B: a larger box makes every 'C' leaf pass, so the `--require-r0` guard is what rejects it. The frozen-constant check must stay in the trusted invocation.

## Resources and limits observed

- At most 2 concurrent CPU processes were used.
- Producer RSS was 186-195 MiB, checker RSS 269-280 MiB, mutation runs 298 MiB (base A) and 771 MiB (base B).
- The longest single command was the 600 s capped profile. The drivers ran about 20 minutes each, as sequences of commands of 5 minutes or less. Every cone finished in its first 25-minute chunk.
- Producer wall time was 255-295 s per cone, and checker wall time 39-42 s per cone (`evidence/resources/`).

## Not covered here

- The central box |n_k - 1/9| <= 1/10000 (lane owner).
- Checker B, the independent mpmath.iv replay.
- The lemmas the leaf inequality relies on: slice concavity of psi, and max-entropy duality.
- The bridge to F and Lemmas 5.6-5.10.
- Symmetry fallback: not needed, since all nine cones were certified directly. If only cone (0,0) were to be trusted, the order-72 group (relabelling C1, relabelling C2, swap) maps Sigma_(0,0) onto every Sigma_u while preserving S, w, Phi, the pairing system and F. That argument is not part of this certificate.
