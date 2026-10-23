# Exact checker controls: receipt (v1)

All runs are standard-library exact arithmetic in Q(zeta_8). They ran at 14:17:06-14:17:13 PDT, after the sources
were frozen and before the 14:19:49 disk-floor observation. Every run used the Python 3.14.3 interpreter
(/opt/homebrew/bin/python3.14) with PYTHONDONTWRITEBYTECODE=1 and TMPDIR = lane tmp/.

## Frozen sources

| file | sha256 |
|---|---|
| exact_rqls_checker_v1.py | 90aaf3beefd049087b7b3d5f00644884a7a99bebcdfdbf90d26c2985cbe89a5d |
| controls/build_controls_v1.py | 5ad382d173d248dbeeb993413b346dfc036cfdcec55e7dfa7d03840cc8916a9d |
| controls/zhang_cao_ex24_cells.json | ec2bd177b32f17b61d98193fa2b54146aef4ffe50b02b5c78c3b3b43e935fdf5 |

zhang_cao_ex24_cells.json holds the extracted strings of Example 2.4. Its provenance is the arXiv e-print
2608.29201v2: tar.gz sha256 127bef18...7d21b6, RQLS.tex raw sha256 39d0e4b6...c417f.

## Commands

```
cd controls && TMPDIR=<lane>/tmp PYTHONDONTWRITEBYTECODE=1 python3.14 build_controls_v1.py
for f in C1..C5: python3.14 ../exact_rqls_checker_v1.py $f.json   # summary fields printed via /usr/bin/python3 json filter
```

## Generated instances

| file | sha256 |
|---|---|
| C1_ex24_positive.json | da95d0921259bae04a679adf47fd6b09620bf3d5e06dd5decc92b1220bb5b18c |
| C2_classical_nonparallel_negative.json | 3c91eabd80f1212ecac6a0d586a0b7e643b36b2f5c1a6833b6ec05f49642b4bc |
| C3_phase_mutation_negative.json | bbf612577e3a1f62d8cd5192c9ac20a254f60af9e7ad8f9a04a7953d89a8385c |
| C4_latin_mutation_negative.json | 6e7f9e63a7ff9c22b2895060b8a71828182a63f9b24d9fb38f803d918cf4effe |
| C5_norm_mutation_negative.json | c1ad2a56c25d2fa782957d4f15df8f4fb3334c9501ad117dce2749de5eec7f82 |

## Results (observed; all matched intent)

| control | intent | ALL_PASS | P1 | P2 | P3 | P4 | details | exit |
|---|---|---|---|---|---|---|---|---|
| C1 source Example 2.4 | positive | True | T | T | T | T | 0 non-orthogonal pairs; 64 distinct rays; 2016 pairs; 24 lines | 0 |
| C2 classical GF(8) mate | P4-only failure | False | T | T | T | **F** | 224 parallel pairs = 8 * C(8,2); 8 rays | 1 |
| C3 phase mutation | P3 failure | False | T | T | **F** | T | 5 non-orthogonal line pairs | 1 |
| C4 B swap | P1 failure | False | **F** | T | T* | T | columns 0, 1 of B not permutations (*class lines skipped when P1 fails) | 1 |
| C5 norm mutation | P2 failure | False | T | **F** | T | T | cell (2,0) norm != n | 1 |

## Side result

The exact checker confirms that source Example 2.4 (v = 8) is a maximal-cardinality 1-RQLS(8): 64 pairwise
non-parallel rays, and all 24 lines are ONBs in Q(zeta_8). This concerns order 8 only. It says nothing about
order 10.

## Limitations

- The checker is a single implementation. Independent implementations would be required before any gate.
- No order-10 candidate exists to check.
