# Independent checker report (checker_v1, standard library, one process)

- Verdict: **PASS** (failures 0, incomplete parts 0)
- Checker: `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset6-independent-checker-v1/tmp/dev/checker_dev_r1.py` sha256 `322326232519e57402bedb263d94654d18552945fb9d87385295bd6db4cec28d`
- Elapsed: 40.0 s (one process, no numpy)

## Inputs (sha256)

- `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset6/evidence/engine-v3-core56/run.json` 6d8dc91dc6160a9a141da7e9bd0edba1b446aa2aaf9959e92fd05ac14babe754 (2853 bytes)
- `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset6/evidence/engine-v3-core56/orbits.jsonl.gz` a580c5801b03ed84edcdf9f58618b4fb0c0d390549dab31527d8a9da20f4dc49 (407387 bytes)
- `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset6/evidence/engine-v3-core56/rlp_duals.json` bbf91e057072d2840ee478a813dbebdc2266e6587e20e1c876b8da16177895ef (106879 bytes)
- `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset6/evidence/engine-v3-core56/survivors.json` 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 (2 bytes)
- `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset6/evidence/engine-v3-run.sha256` f69b8b2288a2cb4285eba8f39a45510e2aa456b725b08fb7cc6358245790bf73 (974 bytes)
- orbits.jsonl (uncompressed) f4f69363a1a602ec56f3a957566e566d2f03f988792a8d04565d2cce31976579; equals run.json field: True

## Per type

| type | leaves (mine) | leaves (run.json) | hash match | edge-DFS = primary | orbit lines | orbits (run.json) | coverage ok | verified | failed | incomplete |
|---|---|---|---|---|---|---|---|---|---|---|
| `(None, 0, None)` | 64940 | 64940 | True | True | 478 | 478 | True | 478 | 0 | 0 |
| `(None, 0, 0)` | 92937 | 92937 | True | True | 2268 | 2268 | True | 2268 | 0 | 0 |
| `(0, 1, None)` | 137789 | 137789 | True | True | 2964 | 2964 | True | 2964 | 0 | 0 |
| `(0, 1, 0)` | 200741 | 200741 | True | True | 4466 | 4466 | True | 4466 | 0 | 0 |
| `(0, 1, 1)` | 222701 | 222701 | True | True | 16414 | 16414 | True | 16414 | 0 | 0 |
| `(0, 2, None)` | 211192 | 211192 | True | True | 4344 | 4344 | True | 4344 | 0 | 0 |
| `(0, 2, 0)` | 307224 | 307224 | True | True | 6475 | 6475 | True | 6475 | 0 | 0 |
| `(0, 2, 1)` | 337507 | 337507 | True | True | 23715 | 23715 | True | 23715 | 0 | 0 |

## Per rule (all types)

| rule | lines | verified | failed | incomplete |
|---|---|---|---|---|
| K | 55159 | 55159 | 0 | 0 |
| RLP | 5513 | 5513 | 0 | 0 |
| PB | 55 | 55 | 0 | 0 |
| FH5 | 134 | 134 | 0 | 0 |
| N26 | 108 | 108 | 0 | 0 |
| RPLP | 155 | 155 | 0 | 0 |

## Global

- lines_parsed: 61124
- lines_malformed: 0
- survive_lines: 0
- survivors_json_empty: True
- total_orbits_match: True
- rlp_dual_entries: 1346
- rlp_keys_checked: 1275
- rlp_keys_passed: 1275
- rlp_keys_failed: 0
- rlp_dual_entries_unused: 71
- leaves_total_mine: 1575031
- manifest_lists_input_hashes: {'run.json': True, 'orbits.jsonl.gz': True, 'rlp_duals.json': True, 'survivors.json': True}
- FH5: {'lines': 134, 'nodes': 35280, 'max_seconds': 0.092, 'engine_counts_equal_full_space': 134, 'full_space_sum_per_placement': 26412500}
- types cover: {'placements': 91, 'placements_per_type': {'(None, 0, None)': 1, '(None, 0, 0)': 6, '(0, 1, None)': 6, '(0, 1, 0)': 6, '(0, 1, 1)': 30, '(0, 2, None)': 6, '(0, 2, 0)': 6, '(0, 2, 1)': 30}, 'stabiliser_sizes': {'(None, 0, None)': 720, '(None, 0, 0)': 120, '(0, 1, None)': 120, '(0, 1, 0)': 120, '(0, 1, 1)': 24, '(0, 2, None)': 120, '(0, 2, 0)': 120, '(0, 2, 1)': 24}, 'each_placement_maps_to_exactly_one_type': True}
