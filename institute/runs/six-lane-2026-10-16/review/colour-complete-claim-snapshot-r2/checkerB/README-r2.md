# checkerB r2: hardened central-box checker

This is the r2 request from `PhysRandomColour`, passed on from Main via the lane owner. Only new files were created.

All times are host clock (`date`, PDT, 2026-10-17):

| step | time |
|---|---|
| pinned hashes verified | 02:22:23, re-verified 02:27:53 |
| r2 copies made | 02:23 |
| runs | 02:26:29–02:27:21 |
| this file written | 02:28:29 |

## Pinned files (not modified)

Hashes were identical before and after this work.

| file | sha256 |
|---|---|
| `code/cb_common.py` | `9d3ad5abb52c3ac9ad1bc1027ae9618040d01b3f7e6266f48651ca91ba183726` |
| `code/central_iv.py` | `cca710e9efeeb98358ae4407457505856927b10210d7d884a9a350f1bc99f9e0` |
| `code/cells_iv.py` | `ea8aca331111d764441d505ced5132b01173e251348f69dca4b42fa5364c7c3b` |
| `evidence/cells_iv_all9_final.json` | `ec4f8fe99a015b4fa15b0955e2c5a516d054cb28184b0ba66b0e6714a137449b` |
| `evidence/central_iv_r0_1e-4_eps3_20_NC8.json` | `ef0de716e6e8700734d08c76433c6c0b3b84ece4f9b7a957a092287b8a57d598` |
| `evidence/central_iv_negctl_eps0_NC4.json` | `3c87321580bc771f57659d66950ba32c9de08bfc40e682ca58675835efa8ecc8` |

## New files

| file | sha256 |
|---|---|
| `code/cb_common_r2.py` | `805efe3f97d3a55068eef954f1f6d21782beb0a9b1a5c93542cdfb5352e58495` |
| `code/central_iv_r2.py` | `6ae81c06ed109416884740cfac65d8df978fadde974bf8235c292402276645c4` |
| `evidence/central_iv_r2_pos.json` | `7c07f5a29fc8c9aa3aee0b42549b629adf9e4de50be94817724903c15927f72b` |
| `evidence/central_iv_r2_negctl.json` | `a4dea938be7c3500a62854202cf331da652aa1e9cc6820d4ba577b08a910d472` |
| `evidence/central_iv_r2_runs.json` | `54fe90184b06949709570406af58db81cf97aedeafa2b14e9214a8aeb8e215c0` |

- **What `central_iv_r2_runs.json` holds:** for every run, the command, the `date` before and after, the exit code, and stdout/stderr. For the positive and negative runs, stdout is truncated in the log. Its recorded sha256 equals the sha256 of the corresponding `--out` file.
- **Scripts used by the runs:** `central_iv_r2_pos.json` records `script_sha256`, and the values equal the two code hashes above, so the runs used these exact scripts.
- **Run harness:** Python `subprocess.run`, one process at a time, with `cwd=checkerB/` and `PYTHONOPTIMIZE` removed from the child environment.
- **Stack:** CPython 3.13.9 (lane `.venv`), mpmath 1.3.0, 128-bit intervals.

## What changed (r2 = copy of the pinned files plus hardening; the mathematics is identical)

### (a) Refusal under `-O`

- **Where:** `central_iv_r2.py:106-111`. This runs before `cb_common_r2` is imported (line 115) and before any certificate code.
- **Trigger:** `sys.flags.optimize != 0`, which covers `-O`, `-OO` and `PYTHONOPTIMIZE`.
- **Output:** a JSON line `{"verdict": "REFUSED", ...}` on stdout and a message on stderr.
- **Result:** exit code 3; no output file is written.

### (b) Every assert replaced by an explicit check

- **Mechanism:** each check is `require(cond, id, reason)`, defined at `cb_common_r2.py:26-37`.
  - On failure it raises `CheckFailed`.
  - `main` (`central_iv_r2.py:626-631`) turns that into `verdict: FAIL`, adds the reason to `fail_reasons`, writes the JSON, and exits with code 1.
  - The id is the pinned file and line that held the assert.
- **Execution counts:** `explicit_checks_executed` in the output JSON records how many times each check ran. The counts below come from the positive run.
- **No asserts remain:** a grep for `^\s*assert` finds no assert statements in either r2 file.

| pinned line | pinned statement | r2 line | runs |
|---|---|---|---|
| `cb_common.py:45` | `assert len(SPECTRA) == 36` | `cb_common_r2.py:66` | 1 |
| `cb_common.py:47` | `assert phi_sum(p) == phi_closed_form(*p)` (grid {0..5}^4) | `cb_common_r2.py:68` | 1296 |
| `cb_common.py:63` | `assert len(edges) == 18 and len(seen) == 36` (runs at import) | `cb_common_r2.py:85` | 1 |
| `cb_common.py:97` | `assert nv[u] == Fr(1, 9) + sum(...)` | `cb_common_r2.py:120` | 729 |
| `cb_common.py:98` | `assert nine_values(nstar) == [Fr(1, 9)] * 9` | `cb_common_r2.py:122` | 1 |
| `cb_common.py:132` (not an assert) | `piv = next(...)` in `inv` (StopIteration if singular) | `cb_common_r2.py:156-157` | 37 |
| `cb_common.py:168` | `assert` symmetry in `is_pos_def_exact` | `cb_common_r2.py:193` | 33 |
| `central_iv.py:158` | `assert cb.check_spectra() and cb.check_arows()` | `central_iv_r2.py:185` | 1 |
| `central_iv.py:161` | `assert B^T B == 4 I` | `central_iv_r2.py:188` | 1 |
| `central_iv.py:162` | `assert B^T 1 == 0` | `central_iv_r2.py:189` | 1 |
| `central_iv.py:165` | `assert phi1 == 900 == Phi(1,1,1,1)` | `central_iv_r2.py:192` | 1 |
| `central_iv.py:167` | `assert mstar == [5/4]*4` | `central_iv_r2.py:194` | 1 |
| `central_iv.py:174` | `assert Wv == lam v` (W2 eigenvectors) | `central_iv_r2.py:201` | 4 |
| `central_iv.py:180` | `assert cb.is_pos_def_exact(X0)` | `central_iv_r2.py:207` | 1 |
| `central_iv.py:182` | `assert` rows of R(0) sum to 0 | `central_iv_r2.py:209` | 1 |
| `central_iv.py:186` | `assert sum_u A_u == 0` | `central_iv_r2.py:213` | 1 |
| `central_iv.py:204` | `assert Rbar == B Xmin^-1 B^T` | `central_iv_r2.py:232` | 1 |
| `central_iv.py:208` | `assert sum_u l_u == 0` | `central_iv_r2.py:236` | 1 |
| `central_iv.py:222` | `assert all(nlo > 0)` | `central_iv_r2.py:251` | 1 |
| `central_iv.py:239` | `assert part == 1` ({2,3,5}-units) | `central_iv_r2.py:268` | 10 |
| `central_iv.py:250` | `assert ubar0 == lstar` (Ubar(0) = L*) | `central_iv_r2.py:279` | 1 |
| `central_iv.py:455` | `assert a.prec >= 128` | parse check `prec_arg` `central_iv_r2.py:555-559` plus `require` at line 576 | 1 |

Other hardening (these were not asserts):

| pinned line(s) | r2 line(s) | change |
|---|---|---|
| `central_iv.py:136` (`raise ArithmeticError`) and any exception inside a (Q) sub-box | `central_iv_r2.py:395-401` | The pinned script aborted with a traceback and gave no verdict. r2 marks that sub-box as failed, so the verdict is FAIL. |
| import of `cb_common` (`central_iv.py:91`) | `central_iv_r2.py:114-118` | An import-time check failure gives `verdict FAIL` and exit 1. |
| `central_iv.py:273-275` (`all(...)` over vertices, which short-circuits) | `central_iv_r2.py:304-312` | Every vertex is checked and counted. |
| `central_iv.py:289` (C pass) | `central_iv_r2.py:331` | Pass requires all of: the vertex set is exactly {-1,1}^4; 16 vertices checked; 16 negative definite; 16 with margin δ; δ > 0. |
| `central_iv.py:428` (Q pass) | `central_iv_r2.py:463-465`, `489-491` | Pass requires all of: the grid tiles [-γ, γ]^3 exactly (first edge −γ_i, last edge γ_i, strictly increasing); NC³ distinct sub-boxes visited, checked and passed; min Gershgorin bound > 0. |
| `central_iv.py:505` (exit status) | `central_iv_r2.py:630-650` | Adds `verdict`, `exit_code`, `fail_reasons` and `explicit_checks_executed` to the output. |

### (c) Argument checks

- **Where:** `central_iv_r2.py:511-569`.
- **Behaviour:** an invalid argument prints `{"verdict": "FAIL", "stage": "argument parsing", "reason": ...}` and exits with code 2.

| argument | requirement |
|---|---|
| `--nc` | integer ≥ 1 |
| `--eps` | exact rational literal ≥ 0. `nan`, `inf`, `1/0`, non-numbers and negative values are rejected. `eps = 0` is accepted, because it is the negative control. |
| `--r0` | exact rational with 0 < r0 < 1/36, so every n^u > 0 on B0 |
| `--prec` | integer ≥ 128 |

**PASS rule:** PASS only if no explicit check failed, all NC³ (Q) sub-boxes were checked and passed with an exact tiling, and all 16 (C) vertices were checked and passed.

**Exit codes:** 0 PASS, 1 FAIL, 2 invalid arguments, 3 refused under `-O`.

## Commands and results (run from `checkerB/`)

| run | command | `date` start–end | exit | result |
|---|---|---|---|---|
| `-O` refusal | `../.venv/bin/python -O code/central_iv_r2.py --r0 1/10000 --eps 3/20 --nc 8 --prec 128 --out evidence/central_iv_r2_pos.json` | 02:26:29–02:26:29 | **3** | REFUSED; stderr message; no output file written (checked) |
| arg check | `... code/central_iv_r2.py --nc 0` | 02:26:34 | **2** | `NC must be >= 1, got 0` |
| arg check | `... --nc -2` / `--nc 2.5` | 02:26:34 | **2** / **2** | `NC must be >= 1` / `NC must be an integer` |
| arg check | `... --nc 8 --eps -3/20` (space form) | 02:26:34–02:26:35 | **2** | Rejected as `expected one argument`: argparse reads `-3/20` as an option. The `eps >= 0` check itself is shown by the next row. |
| arg check | `... --eps=-3/20` / `--eps=-0.15` | 02:26:42 | **2** / **2** | `eps must be a rational >= 0` |
| arg check | `... --eps nan` / `inf` / `1/0` / `abc` | 02:26:35 | **2** each | `... is not an exact rational literal` |
| arg check | `... --prec 64`, `--r0 1/36`, `--r0 0`, `--nc=0 --eps 0` | 02:26:35–02:26:42 | **2** each | each reason recorded in `central_iv_r2_runs.json` |
| positive | `../.venv/bin/python code/central_iv_r2.py --r0 1/10000 --eps 3/20 --nc 8 --prec 128 --out evidence/central_iv_r2_pos.json` | 02:26:49–02:27:12 | **0** | **PASS** (details below) |
| negative control | `../.venv/bin/python code/central_iv_r2.py --eps 0 --nc 4 --out evidence/central_iv_r2_negctl.json` | 02:27:18–02:27:21 | **1** | **FAIL** (details below) |

**Positive run: PASS.**
- (Q): 512/512 sub-boxes checked and passed; tiling exact. Min Gershgorin lower bound 0.070803368; min leading minor 0.004401106.
- (C): 16/16 vertices negative definite, with δ = 1176209/10⁶.
- Every explicit check in the table above held.
- Runtime 22.6 s; peak RSS 27.1 MiB.
- The margins are the same as in the pinned output (`ef0de716…`).

**Negative control (eps = 0): FAIL.**
- Reason: `(Q) failed: 0/64 sub-boxes passed (64 checked, tiling_exact = True, ...)`.
- All 64 sub-boxes fail the Gershgorin test, with lower bounds between −0.0302 and −0.0282.
- (C) passes on its own (16/16, δ = 2289267/10⁶), but the overall verdict is FAIL.

## Pinned `cells_iv.py` (`ea8aca33…`): a vertex with n^u = 0

- **`cells_iv.py:225`:** `nvals = [cb.nine_values(v) for v in verts]` computes the nine n^u at each vertex.
  - These are exact `Fraction`s: the vertices are exact rationals from the exact-midpoint bisection.
  - (7.2) is evaluated in `cb_common.py:81-87`.
- **`cells_iv.py:226-227`:** if any n^u < 0 at a vertex, the leaf is invalid.
- **`cells_iv.py:228`:** `active` keeps only the classes u with n^u > 0 at one or more vertices (exact comparison). A class with n^u = 0 at all five vertices gets no a_u computed and no mu0 positivity check (loop at lines 230-235).
- **`cells_iv.py:238-242`:** for each vertex, `U = iv.mpf(0)`. Then, for each active u, line 241 tests `if n > 0:` on the exact `Fraction`. Only when n > 0 does line 242 add `ivq(n) * au[u] + self.nlogn15(n)`.
- **`cells_iv.py:176-184`:** `nlogn15` is the only place where (3/2)·n·ln n is evaluated (line 180, `iv.log(nv)`). It is called only from line 242, so only with n > 0.

**Conclusion:** a vertex with n^u = 0 contributes exactly 0 for class u. The 0·log 0 term (and the n·a_u term) is skipped by the exact rational test. It is not evaluated in interval arithmetic, and `iv.log` is never called at 0. This matches the frozen-scheme convention that terms with n^u = 0 are 0, which is the continuous extension used by the convexity-in-n argument.
