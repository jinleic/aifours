# Addendum 3: gn(R-minus) <= 716/107

**Status: WRITTEN with an exact rational dual certificate, independently checked in kernel.**

This adds to the following, none of which is revised:
* `frontier-20261029-upper-bound-10834-1619-v1.md` (SHA-256 `c01ded9d20651d455adf14f50b86b54ac478351153b03ef875cdf7a4fa32f371`);
* addendum 1, `frontier-20261029-upper-bound-977-146-addendum-1.md` (SHA-256 `d89238e0bb1ca3a55ba6d2438258bc0d40fbaafcf64d3990f959c1a39df7b924`);
* addendum 2, `frontier-20261029-upper-bound-890-133-addendum-2.md` (SHA-256 `c9e6c8bb345a487287d30a4a43cd7839a3d3c775ac2d5829af3b9778b69c9983`).

The validity argument is unchanged: symmetrize by the product of eight relabelled copies of the strategy, then apply the copy lemma sequentially. No review, formalization or novelty audit has been performed.

## Statement

`gn(R^-) <= 716/107 = 6.6915887850...`

This is `2/14231` (about `1.4e-4`) below `890/133` and `13/29532` (about `4.4e-4`) below the publisher bound `1847/276`.

## New ingredient: iterating the copy of X4

The model is the 890/133 model plus three three-step programs. Each starts with program m2 of addendum 2 and copies X4 a further time. The certificate uses:

| Program | Steps | Rows used |
|---|---|---|
| m4 | `c0` copy of X2 over X{1,4,5,6,7,8,9,10}; `c1` copy of X4 over X{1,2,5,6,7,8,10} plus `c0`; `c2` copy of X4 over X{1,2,5,6,7,8,10} plus `c0,c1` | 85 copy/independence rows; 433 Shannon rows on its 13 variables |
| m0 | `c0` as above; `c1` copy of X2 over X{1,4,5,6,7,8,9,10} plus `c0` | 33 copy/independence rows; 84 Shannon rows |
| m1 | `c0` as above; `c1` copy of X3 over X{1,4,5,6,7,8,9,10} plus `c0` | 4 copy/independence rows; 8 Shannon rows |
| m5 | as m4, but the third copy is over X{1,2,5,6,7,8,9} plus `c0,c1` | 2 copy/independence rows; 5 Shannon rows |

Programs m2 and m3 are present in the model but carry no certificate rows; m2's steps are the first two steps of m4. In m4, `c1` and `c2` are two copies of X4 that are conditionally independent given X{1,2,5,6,7,8,10} and `c0`, with `c2` also independent of `c1` given that set. Each step applies the copy lemma to the joint law of all variables existing before it, so every program row is valid for every entropic profile.

## How it was found

1. **Three-step screen.** The family was m2 followed by one more copy of `X_s` over `V` minus `s` minus `W`, plus copies `(c0,c1)` or `(c1)`, where `W` is a set of 1 or 2 vertices meeting `N(s)`. File: `frontier-20261029-multistep-programs-G3.json`, SHA-256 `8ad13b417c34b40796ebd2f0d3eb97eb3451f0b305765d63df06e086d65a89d5`, 716 programs.
2. **Screening point.** The family was screened at the 890/133 central point v12a with the minimum-violation screen of addendum 2 (`frontier-20261029-multistep-screen-v4.py`). The screen file `frontier-20261029-multistep-screen4-G3-v12a-239.jsonl` (SHA-256 `5c9feefd5d5a5aa65e67cd7ba7d606f564c661a30aaeba543292815122a123c2`) gave leads 254, 260 and 262, with violations `3.2e-5`, `9.9e-5` and `2.9e-5`. All three copy X4 a third time.
3. **DFZ cuts on m2.** Two rounds of DFZ instances on the m2 variable set were also added (`frontier-20261029-branch-dfz-scan3-v12a-m2.json`, SHA-256 `49a1d96b317f5334c23b3a746f2fa9f505d1c0ded9e750b35683933d764223ab`, and `-v12b-m2.json`, SHA-256 `ad3faf2ac113222d4d00589bf33240caab12efa50f5fdc129acab434d3b43f78`; scanner `frontier-20261029-branch-dfz-scan-v3.py`, SHA-256 `3e98cbaf5eaf2a2c616e1933d3dd109ef47ce6e3dac3312f9ea6ed0f933d7c9c`). They moved the floating value only to 6.6917215 (`frontier-20261029-central-point-v12b.json`, SHA-256 `aa9ac6943becd1ff8f17e776b86275ece46ac10a52606e66fd34226874af835b`). A further round found nothing (`frontier-20261029-loop13-log.json`, SHA-256 `7781cb1f4db4fbeaf3fe1453e528f12c39eb3d1bfa653cc7ae1233f1dc4fbda5`; driver `frontier-20261029-central-loop-v13.py`, SHA-256 `e9772f58f218c58fe42ab46c42d44a292d75a4780b787d2cef05fea4e9c5262b`). None of these cuts appears in the final certificate.

## Re-solve, certificate and check

* **Programs.** `frontier-20261029-programs-lead2.json`, SHA-256 `bfa09a940b9038d0b54bf3b612b3b43a0a3ca9687fc8b30d976d700ea9f36fac`, holds m0-m2 of addendum 2 and the three leads as m3-m5.
* **Central re-solve.** `frontier-20261029-central-solve-v12.py`, with the same extra branches and DFZ cut files as above, gives 6.6915887832. Saved as `frontier-20261029-central-point-v12c.json`, SHA-256 `b488a1be6dcf88331152cd01a6db8632df368b754f281f11da761fe565f371bb`.
* **Certificate.** Producer `frontier-20261029-copy-certificate-producer-v7.py` (SHA-256 `6f98166ff502af772313554182a20c40d6ac66d43fc1e2dff519e0c70e7a5e6f`) writes `frontier-20261029-certificate-v12c.json`, SHA-256 `6d5dc5c62833243db23870bcc34f3869149bd48e13843bee4ca977cd04eca886`. It has 2,377 rows and the cap multipliers sum to `716/107`:

  | Row kind | Count |
  |---|---|
  | CMIs | 1,504 |
  | monotonicity | 37 |
  | FDs | 10 |
  | caps | 3 |
  | symmetry | 516 |
  | publisher copy | 118 |
  | publisher independence | 3 |
  | extra-branch copy | 58 |
  | extra-branch independence | 3 |
  | program copy | 117 |
  | program independence | 7 |
  | original-variable DFZ instance (item `3 7 2 2 3 0 0 3 2`) | 1 |

* **Independent check.** `frontier-20261029-dfz-certificate-check-v5.py` (SHA-256 `26bd124a5bbdfe39088778fbd9e97bc707ee8ec938bf574197a3417273f61f49`, unchanged since addendum 2) returns `all_checked`, bound `716/107`. Its three negative controls are rejected. Receipt `frontier-20261029-certificate-v12c-check-result.json`, SHA-256 `76347dcfce0deb55e682506622da7cbbb7c9c3bc4b9e8df0131ba009e2a978fc`. It uses the same DFZ re-derivation receipts as addendum 2.
* **Program-mutation controls.** `frontier-20261029-certificate-v12c-program-controls.json`, SHA-256 `7d362ec60b790d69d9b7b9bc0cc919a996163808b067fe215819d505780bb728`.
  * For m0, m1 and m4, each of these mutations breaks the identity or the row reconstruction:
    * changing the last step's copied variable;
    * dropping the newest copy from the last over-set;
    * dropping the last step.
  * m5 uses only rows that do not depend on its third step, so mutations of that step survive. This is expected: a mutated program is still a valid copy program.

## Limits

* The interval is now `20/3 <= gn(R^-) <= 716/107`, subject to review.
* The decrease comes from iterated copies of one variable, so further iterations or analogous chains may lower the bound again. The screens are floating and exploratory; only the exact certificate carries the claim.
