# Exact SPR spot-check log

Date: 2026-10-14 (America/Los_Angeles). Working directory for shell commands: `/Users/jinleic/jinleic-workspace`.

## Result

| Test | Exactly stable boxes | Exactly certified numerators | Unresolved failures |
|---|---:|---:|---:|
| Sextic random near-boundary boxes | 200 | 200 | 0 |
| Sextic adversarial lightly damped boxes | 12 | 12 | 0 |
| Sextic degenerate-interval boxes | 24 | 24 | 0 |
| Quintic random near-boundary boxes | 200 | 200 | 0 |
| Quintic adversarial lightly damped boxes | 12 | 12 | 0 |
| **Total** | **448** | **448** | **0** |

All 448 rational boxes are distinct. No nonzero coefficient width collapsed during rationalization. All 1,792 corner pairing polynomials have positive constant and leading coefficients and exactly zero positive real roots, established with rational Sturm counts inside strict rational Cauchy bounds. Stability is checked by exact rational Routh tests on all four Kharitonov corners. An independent exact Hurwitz-determinant comparison agreed on 100 seeded polynomials.

- `exact_verify.py`: **31/31 self-tests passed**, including non-SPR, one-unstable-corner, bogus Gordan, negative weights, positive multiple roots, and an extremely narrow negative pocket.
- Sextic construction: **236/236 certified**. Of these, **220** use (3.6), (4.1)--(4.14); **16** use fixed-even-part Lemma 2.3. The latter needed at most 12 exact epsilon halvings. No construction, rationalization, or final rounding failure occurred.
- Proposition 4.1: all **220** applicable sampled cases passed the 50-digit checks of `B < rho < b`, all four value/derivative contacts, coefficient signs, and root locations (4.17)--(4.18). Maximum relative contact residual: `1.836985487815e-50`; diagnostic threshold: `1e-25`. Equations (3.7), (3.8), (4.4)--(4.6), and (4.22) were also checked numerically. Fixed-even cases are not counted as Proposition 4.1 tests here, although the generic summary's `formula_audits_pass` field includes both construction branches.
- Example (7.1): both the paper's simpler numerator `(s+1)^6` and the explicit constructed numerator passed exact full-box certification; its Proposition 4.1 diagnostics passed too.
- Quintic synthesis: **212/212** first LP candidates passed at the first numerator rationalization (`max_den=10^6`). No LP recovery/refinement or infeasibility certificate was needed. **208** candidates used 40 exchange iterations: this is not a claim of LP optimality or convergence; exact positivity of the resulting numerator is independently certified.
- **No discrepancy was observed between the tested paper formulas and the stated properties.** Layout extraction was used to disambiguate the squared gap denominators in (4.7)--(4.8); this was an extraction ambiguity, not a paper correction.

## Sampling and resources

Seed: `20261014`. Every nonsingleton box starts from a stable real-factor polynomial and independent width directions; `sprlib.stability_radius(..., iters=60)` finds the numerical radial boundary, then the radius is multiplied by `1-epsilon`, with epsilon log-uniform on `[1e-4, 0.3]`. Observed epsilon ranges: sextic `[0.00010496317193796386, 0.2871155697554024]`; quintic `[0.00010942904445965303, 0.28063478406289044]`. Modes include real poles, complex pairs, clustered frequencies, wide frequency scales, and adversarial damping in `[1e-4, 1e-2]`. Rationalization follows sampling; exact certification concerns the resulting rational box, not an automatic enclosure of its floating precursor.

Python `3.14.3`; NumPy `2.5.4`; SciPy `1.18.1`; SymPy `1.14.0`; mpmath `1.3.0`. Single sequential process; BLAS and HiGHS threads set to one. Observed peak RSS: `184795136` bytes (about 176.2 MiB), below 4 GiB. Campaign elapsed time: `1690.152086` seconds; CPU time: `1644.819389` seconds. Sextic cases: `7.879127` seconds; quintic cases: `1682.246329` seconds. All launched processes finished.

## Exact commands and outcomes

The initial extraction command exited 2 because the evidence subdirectory did not yet exist:

```sh
pdftotext -layout scratch/ai4s-robust-spr-interval-synthesis/arxiv-2609.26541v2.pdf ai4s/robust-spr-interval-synthesis/evidence/spotcheck/sextic-layout.txt
```

The following command created the assigned directory and succeeded (exit 0); Poppler emitted `Syntax Warning: Mismatch between font type and embedded font file`:

```sh
mkdir -p ai4s/robust-spr-interval-synthesis/evidence/spotcheck && pdftotext -layout scratch/ai4s-robust-spr-interval-synthesis/arxiv-2609.26541v2.pdf ai4s/robust-spr-interval-synthesis/evidence/spotcheck/sextic-layout.txt
```

Both standalone Python commands below were invoked with `subprocess.run(..., capture_output=True, text=True)` and this explicit environment overlay (in addition to inherited environment):

```text
PYTHONPATH=/Users/jinleic/jinleic-workspace/ai4s/robust-spr-interval-synthesis/work
PYTHONDONTWRITEBYTECODE=1
OMP_NUM_THREADS=1
OPENBLAS_NUM_THREADS=1
MKL_NUM_THREADS=1
VECLIB_MAXIMUM_THREADS=1
NUMEXPR_NUM_THREADS=1
HIGHS_THREADS=1
```

```sh
/Users/jinleic/jinleic-workspace/scratch/ai4s-robust-spr-interval-synthesis/venv/bin/python /Users/jinleic/jinleic-workspace/ai4s/robust-spr-interval-synthesis/work/exact_verify.py
/Users/jinleic/jinleic-workspace/scratch/ai4s-robust-spr-interval-synthesis/venv/bin/python /Users/jinleic/jinleic-workspace/ai4s/robust-spr-interval-synthesis/work/sextic_construction.py
```

Both exited 0 without stderr; elapsed times were `0.420205` and `0.224909` seconds respectively. Their stdout was saved as `self-test.json` and `example-7-1.json`.

The complete sampling command was:

```sh
env PYTHONPATH=/Users/jinleic/jinleic-workspace/ai4s/robust-spr-interval-synthesis/work PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 HIGHS_THREADS=1 /Users/jinleic/jinleic-workspace/scratch/ai4s-robust-spr-interval-synthesis/venv/bin/python ai4s/robust-spr-interval-synthesis/work/spotcheck.py --random-count 200 --degenerate-count 24 --adversarial-count 12 --seed 20261014 --prefix spotcheck
```

Exit 0. SciPy emitted its documented forwarding warning: `Unrecognized options detected: {'threads': 1}. These will be passed to HiGHS verbatim.` This option enforces the HiGHS one-thread limit. It is not a solver failure and was not suppressed.

## Artifacts and limits

- `spotcheck-summary.json`: counts, versions, resource measurements, command, and code SHA-256 values.
- `spotcheck-n6-cases.jsonl`, `spotcheck-n5-cases.jsonl`: complete rational endpoints, numerators, exact corner certificates, sampling provenance, numerical construction/LP data, and per-case timings.
- `receipt.json`: independent artifact recount, source-paper and evidence hashes, command receipts, and scope notes.
- `self-test.json`, `example-7-1.json`, `sextic-layout.txt`: control/example output and source formula extraction.
- No failing-case files were generated because there were no rejected final certificates or recovery cases. The runner retains full investigation files if future runs encounter them. It uses exclusive output creation; use a new `--prefix` for another run rather than overwriting evidence.

These are exact arithmetic certificates for sampled rational boxes, not proofs of either general theorem. The 50-digit formula diagnostics are numerical, not algebraic interval proofs. No Lean kernel replay/build was performed, no theorem-wide coefficient-certificate audit is claimed, and no certified optimal synthesis margin is claimed. `sprlib.py` was reused unchanged. No network downloads, Git operations, dependency installation, or file deletions were performed.
