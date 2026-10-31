# Addendum 4: gn(R-minus) <= 2603/389

**Status.** WRITTEN with an exact rational dual certificate, independently checked in the kernel. No review, formalization or novelty audit has been performed.

**Scope.** This adds to the self-contained review input `frontier-20261029-upper-bound-review-input-v1.md` (SHA-256 `e8c46fc195dd22ebcd28e485587a9872582a99ed89b25ce8d2e2ba4cee9e505a`). Read its Section 0 first: it is the pre-source erratum `c64e2a1a3a78d1d71f76d9f04903408e619168945b959d787b06938f8ba6ded9`. It also adds to addenda 1-3, which are unchanged. The graph, FD, cap, symmetry, copy-program and DFZ contract is that packet's Section 2, unchanged.

## Statement

`gn(R^-) <= 2603/389 = 6.6915167095...`

This is `3/41623` (about `7.2e-5`) below `716/107` and `55/107364` (about `5.1e-4`) below the publisher bound `1847/276`.

## New ingredient: four-step copy programs

All copies below are over fixed base sets:
* `T2 = X{1,4,5,6,7,8,9,10}` for copies of X2;
* `T4 = X{1,2,5,6,7,8,10}` for copies of X4.

Each step also conditions on every earlier copy of its program.

| Program | Copy sequence | Steps |
|---|---|---|
| m5 | `X2, X4, X4, X4` | `c0` copy of X2 over `T2`; `c1` copy of X4 over `T4+c0`; `c2` copy of X4 over `T4+c0,c1`; `c3` copy of X4 over `T4+c0,c1,c2` |
| m4 | `X2, X4, X4, X2` | as m5, but `c3` is a copy of X2 over `T2+c0,c1,c2` |

**Validity.** The sequential copy lemma applies (review input §2.4). Each program has its own variable set of 14 variables, with all elemental Shannon rows on it and no rows across programs.

## How it was found

The four-step family consisted of m4 of addendum 3, followed by one hand-chosen copy step around vertex 3. File `frontier-20261029-multistep-programs-H4.json`, SHA-256 `8a57520a266c985e2ac938faa966c137dff256e8f60f91a4f73d9b7e3d3cb8ec`, 20 programs.

It was screened at the 716/107 central point v12c. Leads:

| Lead | Program | Violation |
|---|---|---|
| 0 | X2 copied again | `2.1e-5` |
| 8 | X4 copied a third time | `4.1e-5` |

Screen files: `frontier-20261029-multistep-screen4-H4-v12c-0.jsonl` and `-10.jsonl`.

**Re-solve.** The program file `frontier-20261029-programs-lead3.json`, SHA-256 `984bd9013b9b9d50bd3e2aaf8c1aa2ebdc1dce12ba47f109231521d1dfea8801`, is a lean set: the programs used by the 716/107 certificate plus the two leads. With only the base and b1 DFZ cut files, the floating value is 6.6915167070. Central point `frontier-20261029-central-point-v12d.json`, SHA-256 `d8754b57a87720261874cf3f1cf9d65bde3a81c7622140f1b77a29f837a6aa4d`; 1.66M rows.

## Certificate and check

**Producer.** `frontier-20261029-copy-certificate-producer-v7.py`, SHA-256 `6f98166ff502af772313554182a20c40d6ac66d43fc1e2dff519e0c70e7a5e6f`.

**Certificate.** `frontier-20261029-certificate-v12d.json`, SHA-256 `4e30a96016ab5905ff6ec001315022cf31246495e5ae751433a5d9e45b2c1667`, with 3,300 rows. The cap multipliers sum to `2603/389`.

| Row kind | Count |
|---|---|
| CMIs | 2,240 |
| Monotonicity | 42 |
| FDs | 10 |
| Caps | 3 |
| Symmetry | 523 |
| Publisher copy | 133 |
| Publisher independence | 3 |
| Extra-branch copy | 42 |
| Extra-branch independence | 2 |
| Program copy | 292 |
| Program independence | 9 |
| Original-variable DFZ instance (item `3 7 2 2 3 0 0 3 2`) | 1 |

Program rows by program:
* m5: 210 copy/independence rows and 1,044 Shannon rows;
* m4: 84 copy/independence rows and 238 Shannon rows;
* m2 (`X2, X4, X4`): 7 copy/independence rows and 15 Shannon rows, none depending on its last step.

Programs m0, m1 and m3 are unused.

**Independent check.** `frontier-20261029-dfz-certificate-check-v5.py`, SHA-256 `26bd124a5bbdfe39088778fbd9e97bc707ee8ec938bf574197a3417273f61f49`, unchanged:
* result `all_checked`, bound `2603/389`;
* three negative controls rejected;
* receipt `frontier-20261029-certificate-v12d-check-result.json`, SHA-256 `6a54f6901384938587d9925472f2befc727c9b7c1e43e69e4a79c59735a4a70c`.

It uses the same DFZ receipts as the review input §2.5.

**Program-mutation controls.** `frontier-20261029-certificate-v12d-program-controls.json`, SHA-256 `e9b8637e90a723a70b0785194ba91bc2b2fcb2b57fff10162ba738059f3acf21`.
* For m4 and m5, changing the last step's copied variable breaks the identity, and dropping the newest copy from its over-set breaks the reconstruction.
* m2's last step is unused.

## Limits

The interval is now `20/3 <= gn(R^-) <= 2603/389`, subject to review. The successive decreases from deeper copy chains on X2/X4 are:

| Bound | Decrease |
|---|---|
| 890/133 | 5.2e-5 |
| 716/107 | 1.4e-4 |
| 2603/389 | 7.2e-5 |

Five-step chains are being screened; they have 15 variables per program, so LP size is now the main cost.
