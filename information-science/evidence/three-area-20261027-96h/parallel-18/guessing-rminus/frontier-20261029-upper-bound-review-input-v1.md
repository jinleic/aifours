# Self-contained review input: copy-LP upper bounds for gn(R-minus), source-first

Author: InfoGuessingRminus-2 (original author).

This packet is meant as the single entry point for a fresh review of the four exact upper bounds:

| Bound | Value |
|---|---|
| 10834/1619 | 6.691785 |
| 977/146 | 6.691781 |
| 890/133 | 6.691729 |
| 716/107 | 6.691589 |

It uses no review return or parent assessment of any kind, and it replaces no earlier file: all cited files are byte-pinned and unchanged. Section 0 must be read before every other section.

## 0. Required pre-source erratum (read first)

**Erratum.** `frontier-20261028-full-source-lp-optimum-v1-erratum-1.md`, SHA-256 `c64e2a1a3a78d1d71f76d9f04903408e619168945b959d787b06938f8ba6ded9`. It concerns the source packet `frontier-20261028-full-source-lp-optimum-v1.md`, SHA-256 `08af469a09689dcdf40b07bbb086c851349141f582b92714b92d5a7eef63fcdd`.

**The correction.** That packet's "Exact LP scope" paragraph cites the publisher's Remark 3.8 for the omitted cross-branch Shannon inequalities. The correct reference is **Remark 5.4**: extracted text lines 985-995, see Section 1. Theorem 5.2 item 2 (lines 949-955) fixes the three elemental variable sets.

**Its effect here.** Every model below includes the publisher's three branches exactly as separate elemental variable sets. No inequality mixes variables of different branches. Each added copy program is again its own separate variable set.

## 1. Named sources

**Publisher (R-minus, Theorem 5.2).** E. Gurpinar, Kybernetika 60 (2024) 553-575.
* Local copy `institute/runs/three-area-2026-10-27-96h/public-sources/gurpinar-kybernetika60-2024-553-575.pdf`, SHA-256 `373e8a2567fc7de9d40d0e5fabca9655cbb7b689a162005262b4f4d432bb46d8`.
* Extracted text `gurpinar-publisher-layout-v1.txt` (this root), SHA-256 `98d1dba760d383db92948026002bfa7dd95ebbe558cf1917f0c471189b528c88`.
* Locations in the extracted text:

  | Item | Lines |
  |---|---|
  | R-minus defined as R minus the edge 9-10 | 873-874 |
  | Fig. 2 (printed p570) | 878-897 |
  | Fractional clique cover lower bound 20/3 | 901-902 |
  | Earlier DFZ-based bound 59767/8929 from [1] | 905-906 |
  | Theorem 5.2 with its copy steps 1(a)-(c), elemental sets 2 and symmetry constraints 3 | 933-958 |
  | Remark 5.4 | 985-995 |

**BCDRV ([1] of the publisher).** Baber, Christofides, Dang, Riis, Vaughan, arXiv:1410.8349v2. Local copy `institute/runs/three-area-2026-10-27-96h/public-sources/bcdrv-1410.8349v2.html`, SHA-256 `3a270e579f080067717d90e25b6e59d29615a543ff30b1abfb9b5e2fae31337d`.

**DFZ.** Dougherty, Freiling, Zeger, *Non-Shannon information inequalities in four random variables*, arXiv:1104.3602.
* PDF `frontier-20261029-dfz-source/dfz-1104.3602.pdf`, SHA-256 `0e46a1700e59d99a6dafc6340d87ac85f9709ff91d1d539409f060ba39cd52b3`.
* TeX `frontier-20261029-dfz-source/src/nonShannon.tex`, SHA-256 `ab01cd4113f334715d6e80b538bfcca657d659380504be916de2bd43857e732c`.

## 2. The contract

### 2.1 Graph

Vertices `1..10`. The 26 edges are listed below. They were visually transcribed from the publisher's Fig. 2: 3-4 is an edge, 9-10 is absent. The transcription is pinned in `frontier-20261028-weighted-law-certificate-v1.md` (SHA-256 `d223232b8978a18bba5542fcdcdd133cbbc7f321ac057f8278850674b37d2f96`, Section 1).

```
12 13 14 15 16 17 23 27 29 2-10 34 38 39 45 48 4-10
56 59 5-10 67 68 69 78 7-10 89 8-10
```

Neighbourhoods:

| v | N(v) |
|---|---|
| 1 | 2,3,4,5,6,7 |
| 2 | 1,3,7,9,10 |
| 3 | 1,2,4,8,9 |
| 4 | 1,3,5,8,10 |
| 5 | 1,4,6,9,10 |
| 6 | 1,5,7,8,9 |
| 7 | 1,2,6,8,10 |
| 8 | 3,4,6,7,9,10 |
| 9 | 2,3,5,6,8 |
| 10 | 2,4,5,7,8 |

Every checker hard-codes this table and re-verifies the edge count 26 and the two automorphisms below.

### 2.2 Game and entropy reduction

**Rows from a strategy.** Fix an alphabet of size `q` and a guessing strategy: full-domain decoders `f_v` on the neighbour tuple. Let `W` be its winning set, and let `X` be uniform on `W`. Then:
* `H(X_V) = log|W|`;
* `H(X_v | X_N(v)) = 0`: these are the ten FD rows `h(N(v)+v) = h(N(v))`;
* `H(X_v) <= log q`: these are the cap rows `h(v) <= 1` after dividing by `log q`.

**What a certificate proves.** An exact identity `sum(w_i * row_i) = h(V)` is a certificate if:
* every inequality row is valid for the constructed variables and carries the stated sign;
* the caps carry nonnegative weights `c_v`.

Such a certificate gives `log_q|W| <= sum_v c_v` for every `q` and every strategy, hence the same bound for the (asymptotic) guessing number.

### 2.3 Symmetrization

The two generators below are graph automorphisms, checked in code. They generate an eight-element group `G`:

| Generator | Images of 1..10 |
|---|---|
| `g1` | 8,10,7,6,9,3,4,1,2,5 |
| `g2` | 1,5,6,7,2,3,4,8,9,10 |

**Replacing the strategy by a symmetric one.** Take independent copies of the whole law, one per element of `G`, and set `Y_v = (X^(g)_{g(v)})_g`. This is again a strategy for the same graph, on alphabet `q^8`. Its entropy profile satisfies `H(Y_S) = sum_g H(X_{g(S)})`, so it is `G`-invariant. Hence the symmetry rows `h(S) = h(g1(S)) = h(g2(S))` may be imposed. This is the argument of `frontier-20261028-gurpinar-certificate-audit-v1.md` §3 (SHA-256 `d0b494122660394b46d8ce647ed17e2f890c1f3ccf393cd4e44ccc48e87dcaf6`); the publisher's item 3 also imposes symmetry.

### 2.4 Copy lemma, applied sequentially

Given the joint law of the existing variables, a copy step introduces new variables:
* jointly, the new variables have the law of the copied tuple together with the over-set;
* they are conditionally independent of all existing variables given the over-set.

This is realized by sampling from the conditional kernel. Every copy marginal equality `h(U + new_Q) = h(U + old_Q)` then holds, for `U` any subset of the over-set variables and `Q` any nonempty subset of the step's entries. So does the step independence `I(new ; existing | over) = 0`. A program applies such steps in order, each on the joint law of all variables created so far; elemental Shannon inequalities hold on its whole variable set. Steps may copy an atomic tuple (one variable for a whole tuple), as in the DFZ proofs.

**The publisher's three branches.** These are Theorem 5.2 items 1(a)-(c), in the variable naming `a..j` = `X1..X10`:
1. `b'0` copies `X2` over `X{1,4,5,6,7,8,9,10}`.
2. `(d'1,e'1)` copies `(X4,X5)` over `X{1,2,3,6,7,8,9}`. Then `g'2` copies `X7` over `X{1,2,3,4,6,8,9}` plus `e'1`.
3. `(f'3,g'3)` copies `(X6,X7)` over `X{1,2,3,4,5,8,9,10}`. Then `h'4` copies `X8` over `X{1,2,3,4,5,6,9,10}` plus `f'3`.

The elemental sets are exactly those of item 2, one per branch, with no cross-branch rows (Section 0). The exact optimum of this publisher LP is `1847/276`, as recorded in the source packet of Section 0, read with the erratum.

**Added structures.** Their exact specifications are embedded in each certificate:
* Extra single-copy branches, as data `extra_single_copies`.
* Copy programs, as data `programs`. The format: integers are originals, `c<j>` is the j-th copy of that program, and a list is an atomic tuple copy.

### 2.5 DFZ rows

A DFZ row is a conditional instance of one coefficient tuple from the DFZ TeX four-copy list: disjoint role blocks `A,B,C,D` and conditioning block `Z`. It is used only if that tuple was re-derived exactly from its own copy steps by `frontier-20261029-dfz-inequality-verify.py` (SHA-256 `c2db2bad5be6e747b30abce3e9abb46f83b2b49703dc5e976cfa7ca70b44e650`).

**Receipts.**

| File | SHA-256 | Content |
|---|---|---|
| `frontier-20261029-dfz-inequality-verify-result.json` | `12f6aa96a6ec70ee6622e4d6981d98d3e3d89ff717f061c137d8c1e52699a727` | five items and Zhang-Yeung |
| `frontier-20261029-dfz-inequality-verify-base-used.json` | `206f4a17575c632b3185030d2c58dd9c6bc47c098a93961eb6d827afa27434e5` | base-used items |
| `frontier-20261029-dfz-inequality-verify-v9b.json` | `614fda6760c476ff15330dc489dbb463930261808740c708cbcefb1048a574e5` | item 3 5 6 2 3 0 0 3 0 |

**Negative control.** `frontier-20261029-dfz-inequality-verify-ingleton-control.json` (SHA-256 `b2c9869f864c79eed826ef49f44c2d3e84b440039c0fbf675074b1d63564db97`) shows that Ingleton is rejected with a three-step program, while Zhang-Yeung is accepted.

## 3. Certificates and their exact dependencies

| Bound | Certificate (SHA-256) | Checker (SHA-256) | Receipt (SHA-256) | Packet |
|---|---|---|---|---|
| 10834/1619 | `frontier-20261029-dfz-certificate-gurpinar-sym-v1.json` (`23de71c60395cc02170b4d80cbcd5ed3ebfff0243fd61f3a1bf9dfdd6df7f3ad`) | `frontier-20261029-dfz-certificate-check-v2.py` (`6c0a9c8f196cc39c4f13804a0827c4aa42606a4850e43091cef15763be47cce5`) | `frontier-20261029-dfz-certificate-gurpinar-sym-check-result.json` (`9c536cd1b260d7f30116cea04c8184adae55e3368ab72354c9f81a66fdd04545`) | `frontier-20261029-upper-bound-10834-1619-v1.md` (`c01ded9d20651d455adf14f50b86b54ac478351153b03ef875cdf7a4fa32f371`) |
| 977/146 | `frontier-20261029-certificate-v9b.json` (`b318c80e51a787567e4c156fb57f965e1b128787767ac5d1594bf37538d29cb5`) | `frontier-20261029-dfz-certificate-check-v4.py` (`06b73587d6287929f9d81bfc2218460b2a417ee69d0a0deacb26f9e296b4ce87`) | `frontier-20261029-certificate-v9b-check-result.json` (`f85dcf47251d819e929c50318e11be3650ef8511fbfe52b941cdab116343afb5`) | addendum 1 (`d89238e0bb1ca3a55ba6d2438258bc0d40fbaafcf64d3990f959c1a39df7b924`) |
| 890/133 | `frontier-20261029-certificate-v12a.json` (`df50e7ca467c8a2e1bd811a4a510e6dbeba169b002a1f0cff5c992eb6a2afcea`) | `frontier-20261029-dfz-certificate-check-v5.py` (`26bd124a5bbdfe39088778fbd9e97bc707ee8ec938bf574197a3417273f61f49`) | `frontier-20261029-certificate-v12a-check-result.json` (`4d58f2ee84824abd1d1fdfee7579d3d66dff2722ed7a7be3c5d56cd768c3456f`) | addendum 2 (`c9e6c8bb345a487287d30a4a43cd7839a3d3c775ac2d5829af3b9778b69c9983`) |
| 716/107 | `frontier-20261029-certificate-v12c.json` (`6d5dc5c62833243db23870bcc34f3869149bd48e13843bee4ca977cd04eca886`) | same v5 checker | `frontier-20261029-certificate-v12c-check-result.json` (`76347dcfce0deb55e682506622da7cbbb7c9c3bc4b9e8df0131ba009e2a978fc`) | addendum 3 (`47f43747fea6c4b085c1b0969a2825c8aaee1c7da41ee7cfde415eb3bfd2df63`) |

**What each checker does.** It rebuilds every row from its semantic description with Fractions:
* Shannon rows on the stated variable set;
* FD, cap and symmetry rows;
* the publisher branches, transcribed independently;
* the extra branches and programs declared in the certificate;
* DFZ instances, admitted only with a receipt from Section 2.5.

It checks signs and the exact identity, and recomputes the bound as the sum of cap multipliers. It also runs negative controls (flipped sign, changed cap multiplier, dropped DFZ receipt). The program-mutation controls for 890/133 and 716/107 are in `frontier-20261029-certificate-v12a-program-controls.json` (`29726c26a1dd0ab7c2e5fea4e2539f0fc2bc61bd82141625246e41b4460013ba`) and `frontier-20261029-certificate-v12c-program-controls.json` (`7d362ec60b790d69d9b7b9bc0cc919a996163808b067fe215819d505780bb728`).

**Each certificate is a standalone proof of its bound.** The best bound, `716/107`, depends only on the following, all byte-pinned above:
* Section 2: the graph, game and reduction, symmetrization, copy lemma, and the one DFZ item `3 7 2 2 3 0 0 3 2` (receipt `-result.json` or `-base-used.json`);
* certificate v12c;
* checker v5.

**Reproducing the DFZ-only value.** As a sanity check, the base Shannon+DFZ cutting plane reproduces the BCDRV DFZ value `59767/8929` exactly. Certificate-check receipt `frontier-20261029-dfz-certificate-base-check-result.json`, SHA-256 `408b877a02e5a13a4432e3b14eedc5f7d06cd413981e285a237ceeb30cad2151`.

## 4. What a reviewer should check

1. The graph transcription against Fig. 2.
2. The entropy reduction and the symmetrization argument (Section 2.2-2.3).
3. Sequential copy-lemma validity of every declared program, including atomic-tuple entries (none are used in these certificates).
4. The DFZ re-derivation script and its receipts against the TeX list.
5. That each checker's row rebuild is independent of the producer. The producers are `frontier-20261029-copy-certificate-producer-v6.py` and `-v7.py`; the checkers were written separately but in the same harness.
6. The exact identity, by rerunning the checker.

**Limits.** All four bounds are WRITTEN with machine-checked exact identities in this harness. There has been no proof-assistant formalization, no cross-model or human review, and no novelty audit. The lower bound remains `20/3`.
