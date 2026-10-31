# Addendum 2: gn(R-minus) <= 890/133

**Status: WRITTEN with an exact rational dual certificate, independently checked in kernel.** This file adds to `frontier-20261029-upper-bound-10834-1619-v1.md` (SHA-256 `c01ded9d20651d455adf14f50b86b54ac478351153b03ef875cdf7a4fa32f371`) and `frontier-20261029-upper-bound-977-146-addendum-1.md` (SHA-256 `d89238e0bb1ca3a55ba6d2438258bc0d40fbaafcf64d3990f959c1a39df7b924`). The validity argument of the first file applies unchanged: symmetrize by taking the product of eight relabelled copies of the strategy, then apply the copy lemma, now sequentially. No review, formalization or novelty audit has been performed.

## Statement

`gn(R^-) <= 890/133 = 6.6917293233...`.

This is `1/19418` below `977/146` and `11/36708` (about `3.0e-4`) below the publisher bound `1847/276`.

## New ingredient: a two-step copy program

**Program m2.**
1. `c0` is a copy of `X2` over `X{1,4,5,6,7,8,9,10}`. This is the publisher's branch-1 copy.
2. `c1` is a copy of `X4` over `X{1,2,5,6,7,8,10}` together with `c0`.

Each step applies the copy lemma to the joint law of every variable that exists before it. The new copy has the copied variable's joint law with the over-set, and it is conditionally independent of all existing variables given that over-set.

The branch carries:
* every elemental Shannon inequality on the twelve variables;
* every marginal equality `h(U+c) = h(U+X)` for `U` inside the over-set;
* both step independences.

So it is valid for every entropic profile of the original variables. The order matters: the second step conditions on the first copy, so this is not a pair of single-copy branches.

## How it was found

1. **Central point.** The 977/146 program plus later rounds of branch DFZ cuts was solved by IPM without crossover. The resulting central point v9e has value 6.6917808101, i.e. 977/146 up to tolerance: no change.
2. **Ingleton census.** At v9e every Ingleton instance on disjoint groups of at most two variables holds (minimum `1.2e-11`).
   * A four-group polymatroid that meets Ingleton is a limit of linear rank functions, so it satisfies every valid four-group inequality.
   * This explains why more conditional DFZ instances stopped cutting.
3. **New screen.** `frontier-20261029-multistep-screen-v3.py` (SHA-256 `b34d734202e66eb382723358d5058e4ee0c457164faf74ef66ef5e48a2c9e45a`) fixes the original coordinates to the central point. It then minimizes the uniform violation `t` of all branch rows by IPM.
   * **Controls at v9e.** The three publisher branches and the extra branches all give `t < 3e-9` (`frontier-20261029-multistep-screen3-controls-v9e.jsonl`, SHA-256 `b56081b7202920371c306c8dcab44ffa09619080f5532335cc68edb1b4be89fc`).
   * **Correction.** It also showed that an earlier hard-feasibility "Infeasible" status (X3 over X{1,2,5,6,9,10}) was tolerance noise: `t = 2.1e-9` (`frontier-20261029-multistep-screen3-controls-v9b.jsonl`, SHA-256 `9fa6c3e89c77a3e02af086ef62953b8babe2b9a2d4a826061ef4533f1ed14c65`).
4. **Leads.** The candidate family was one extra copy step appended to branch b1 and to the extra single-copy branches (`frontier-20261029-multistep-programs-E1E2.json`, SHA-256 `f1feb244420fd71ef1b3b2594ff25114e0a8c7c8cb07bc079e603f4704a003b1`). In the screened part (`frontier-20261029-multistep-screen3-E1E2-v9e-0.jsonl`, SHA-256 `58e9b63f8f018edbd9804f322e823fd181bc6f0ec5fdd69294c87f6c939b5b4d`) it gave three leads with `t` far above noise:

   | Index | Program | t |
   |---|---|---|
   | 40 | `b1+copy2-minus3` | `3.3e-4` |
   | 75 | `b1+copy3-minus2` | `3.3e-4` |
   | 130 | `b1+copy4-minus3-9` | `8.3e-5` |

   Programs 40 and 75 copy X2 (respectively X3) a second time over X{1,4,5,6,7,8,9,10} plus `c0`. Program 130 is m2 above.

## Re-solve, certificate and check

* **Program file.** `frontier-20261029-programs-lead1.json`, SHA-256 `ee4e88883984bbb5900e165a08e3e89c8d34bc99e47f8a5da1eb2228c125c7a0`, holds the three programs.
* **Re-solve.** `frontier-20261029-central-solve-v12.py` (SHA-256 `fd3e75372733cdd9bddca470c925dfc6291ad289cdee4c479c2cd1630de48b2f`; it compiles programs with `frontier-20261029-multistep-screen-v4.py`, SHA-256 `eeb1726b30f9791af9317535257438114cf7d28f315146016652f89167433010`). The model is:
  * the symmetric publisher LP;
  * the extra branches `frontier-20261029-extra-copies-round1.json` (SHA-256 `335708b70f2f9206e48063d888c33bb13d50fa85d38389cc707c7765a0185e26`);
  * the three programs;
  * the earlier DFZ cut files.

  It gives value 6.6917292944, saved as `frontier-20261029-central-point-v12a.json` (SHA-256 `20b87ff09999279ad662cfafea34b45543b165d8df1fc05a55fe979c7b2332fe`).
* **Producer.** `frontier-20261029-copy-certificate-producer-v7.py` (SHA-256 `6f98166ff502af772313554182a20c40d6ac66d43fc1e2dff519e0c70e7a5e6f`) takes the crossover basic dual and solves it exactly with flint. The certificate is `frontier-20261029-certificate-v12a.json`, SHA-256 `df50e7ca467c8a2e1bd811a4a510e6dbeba169b002a1f0cff5c992eb6a2afcea`, with 2,115 rows:

  | Row kind | Count |
  |---|---|
  | CMIs | 1,253 |
  | monotonicity | 27 |
  | FDs | 10 |
  | caps | 3 |
  | symmetry equalities | 534 |
  | publisher copy equalities | 153 |
  | publisher independences | 5 |
  | extra-branch copy equalities | 64 |
  | extra-branch independences | 3 |
  | program copy equalities (all in m2) | 60 |
  | program independences (m2) | 2 |
  | original-variable DFZ instance (item `3 7 2 2 3 0 0 3 2`) | 1 |

  The cap multipliers sum to `890/133`.
  * Programs 40 and 75 carry no certificate rows: the improvement comes from m2 alone.
  * The branch-1 DFZ instance of the 977/146 certificate is no longer used.
* **Independent checker.** `frontier-20261029-dfz-certificate-check-v5.py` (SHA-256 `26bd124a5bbdfe39088778fbd9e97bc707ee8ec938bf574197a3417273f61f49`) recompiles each declared program with its own code. It checks that every reference exists before its step, that over-sets precede the step, and every copy-subset relation. It then rebuilds every row, requires the exact re-derivation of the DFZ item from the existing receipts, and checks signs and the identity. Result: `all_checked`, bound `890/133`. The negative controls were rejected (flipped sign, changed cap, dropped DFZ receipt). Receipt `frontier-20261029-certificate-v12a-check-result.json`, SHA-256 `4d58f2ee84824abd1d1fdfee7579d3d66dff2722ed7a7be3c5d56cd768c3456f`. The DFZ receipts used:
  * `frontier-20261029-dfz-inequality-verify-result.json` (SHA-256 `12f6aa96a6ec70ee6622e4d6981d98d3e3d89ff717f061c137d8c1e52699a727`);
  * `-base-used.json` (SHA-256 `206f4a17575c632b3185030d2c58dd9c6bc47c098a93961eb6d827afa27434e5`);
  * `-v9b.json` (SHA-256 `614fda6760c476ff15330dc489dbb463930261808740c708cbcefb1048a574e5`).
* **Program controls.** These are in `frontier-20261029-certificate-v12a-program-controls.json`, SHA-256 `29726c26a1dd0ab7c2e5fea4e2539f0fc2bc61bd82141625246e41b4460013ba`. Each of the following mutations of m2 makes the checker fail:
  * step 2 copies X5 instead of X4;
  * step 1 copies X3 instead of X2;
  * `c0` is dropped from the step-2 over-set;
  * the step-1 over-set is shrunk.

## Limits

* The interval is now `20/3 <= gn(R^-) <= 890/133`, subject to review.
* The multi-step screen is exploratory and floating. Only the exact certificate carries the claim.
* A double-copy family of 3,698 two-step programs is being screened at v12a. Further decreases are possible.
