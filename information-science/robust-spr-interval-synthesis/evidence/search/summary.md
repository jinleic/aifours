# Falsification searches (exploratory; Empirical evidence only)

All runs 2026-10-14 on the Mac Studio, Python 3.14.3 (`work/requirements.txt`), from
`ai4s/robust-spr-interval-synthesis/work` with `PYTHONPATH=.`; `$PY` =
`/Users/jinleic/jinleic-workspace/scratch/ai4s-robust-spr-interval-synthesis/venv/bin/python`,
`$R` = `/Users/jinleic/jinleic-workspace/scratch/ai4s-robust-spr-interval-synthesis/runs`
(raw JSONL records there, not synced). Floating-point grid tests are relaxations and screens; none
of the numbers below is a certificate of synthesizability over the continuum, and no counterexample
was certified. "Grid-feasible" means a numerically found witness satisfies the grid constraints.

## S1. Random near-boundary stable monic boxes (angular margin delta*)

Command: `$PY search_random.py N 400 20000 $R/rand400v2_nN.jsonl 4` for N = 5, 6, 7, 8
(random Hurwitz center with mixed real/complex roots, random relative width directions, scaled to
(1 - eps) times the numerical stability radius, eps log-uniform in [1e-4, 10^-0.5]; grid 1500
log-spaced t in [1e-7, 1e7] plus band-edge points; LP bisection tol 1e-3).
Result: 400 boxes per order, **0 grid-infeasible**; smallest delta* / delta_win ratio rho:
n = 5: 0.124, n = 6: 0.049, n = 7: 0.125, n = 8: 0.094. (An earlier run with a max-over-corners row
normalization, files `rand400_nN.jsonl`, gave the same 0 infeasible; that normalization could only
create false infeasibility flags — it did at one n = 6 point in an eps-scan before the fix, see S2.)

## S2. eps-scans toward the boundary

Command: `$PY eps_scan.py N SEED` for the worst S1 samples (5 20051, 6 20248, 7 20244, 8 20264),
grid 4000 points, tol 1e-4; outputs `eps_scan_nN_seedSEED.txt` (regenerated with the fixed code;
`eps_scan.txt` is a superseded interleaved file). delta* decreases toward 0 as eps -> 0 (n = 5:
0.456 at eps = 0.1, 2.3e-3 at eps = 1e-6; n = 6: 0.195 -> 1.0e-3; n = 7: 0.188 -> 3.3e-3; n = 8:
0.452 -> 1.1e-2), while the window width delta_win stays near its eps = 0 value: the pinned double
contact at the closing gap (Prop. D) drives delta* -> 0, so delta* or rho near the boundary is not
a measure of nearness to a counterexample. Negative control: before the per-corner normalization
fix, n = 6 at eps = 1e-6 was flagged "infeasible"; after the fix delta* = 1.0e-3 > 0 (n = 6 is a
theorem, so the flag was an artifact).

## S3. Non-monic boxes (variant, Prop. E)

Command: `$PY search_nonmonic.py N 150 500 $R/nonmonic_nN.jsonl 1`, N = 3, 4, 5 (leading interval
uncertain). 150 boxes each, 0 grid-infeasible; min delta* 9.8e-4, 8.2e-5, 5.2e-3.

## S4. Fully-closed marginal boxes (closed problem, Prop. D, Lemma C)

Random walk restricted to the realizable set (all n-2 gaps closed):
`$PY closed_mcmc.py N STEPS 101 $R/closed_mcmc_big_nN.jsonl 10` (STEPS = 20000, N = 7..11;
pilot `closed_mcmc.py N 3000 11 ...` for N = 5..8). Every 10th state is tested with a float LP
(beta >= 0, sum beta = 1, exact double-contact equalities). Records are correlated walk states, not
independent boxes. Solver status was 0 (optimal) in every test.
Tested states: n = 5, 6: 300 each; n = 7..11: 2000 each. Negative restricted-LP optimum: n <= 9: 0;
n = 10: 596; n = 11: 36. (n = 12: no realizable start found by the Nelder-Mead start search.)

Re-test of ALL 632 negative cases plus 30 random positive cases for each n = 7..11 (782 cases):
`$PY closed_recheck.py $R/recheck_list.txt $R/recheck_out.jsonl 4 40` — endpoints and the 3-dim
contact null space rebuilt in 40-digit arithmetic (contact rank n-2 confirmed numerically:
smallest contact singular value >= 3.0e-6), unit-normalized rows rounded to float64, grid
feasibility decided by an exhaustive six-chart LP (lambda_q = +-1, |lambda_j| <= 1), witness
validated against all rows. Result: **782/782 grid-feasible**, witness min-row >= 6.5e-4 (unit-row
metric) in every case, and every witness beta has all coefficients positive. So the 632 float
negatives were artifacts of the ill-conditioned (n+1)-dimensional float LP. Earlier single-case
probe: `closed_exact3.py` (40 cases, same conclusion).

Adversarial minimization of the 3-dim closed margin (float64 null space, unit rows, LP over the box
|lambda_k| <= 1; a ranking heuristic only): `$PY closed_opt.py N 1 4000 $R/closed_opt_nN_s1.json`,
N = 6..9, CMA-ES 4000 evaluations. This margin is >= 0 by construction (lambda = 0 is admissible), so
only a strictly positive value is informative: it means a strictly grid-feasible closed numerator
exists. Smallest margins found: 6.8e-3 (n = 6), 1.0e-3 (n = 7), 5.3e-4 (n = 8), 2.3e-2 (n = 9); an
earlier n = 6 run with a constant penalty (output file overwritten, value from its console log only)
reported 1.0e-4. All evaluated configurations were strictly
grid-feasible; margins also approach 0 at degenerate configurations for n = 6 (where the theorem
holds), so small values are not evidence of a counterexample. (Early exploratory scripts not used for
evidence: `tau_scan.py` — the monic Re-margin saturates at 1 and is uninformative; `closed_search.py`
— rejection-sampling pilot superseded by `closed_mcmc.py`.)

## S5. Census of alternation configurations (bookkeeping)

`$PY enumerate_configs.py 9` → `alternation_census.txt`. Generalizes the quintic manuscript's
enumeration (numerator-interval sequences, alternating orientations, denominator region order,
<= floor(n/2) positive contacts per vertex). Reproduces the quintic Table 2 configurations Q1–Q5
among its 8 n = 5 survivors (the other 3 are removed by the manuscript's Lemma 5.3). Survivors after
region order and multiplicity: n = 5: 8, n = 6: 48, n = 7: 207, n = 8: 1128, n = 9: 4176.
