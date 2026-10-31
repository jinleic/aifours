# A new upper bound: gn(R-minus) <= 10834/1619 < 1847/276

**Status: WRITTEN with an exact rational dual certificate, independently checked in kernel.** Scientific review, proof-assistant formalization and a novelty audit have not been performed. The lower bound `20/3` is unchanged.

## Statement

For the graph R-minus (ten vertices, the 26 edges of the pinned definition, vertices `1,...,10` named `a,...,j`):

`gn(R^-) <= 10834/1619 = 6.6917850525...`

This improves the publisher bound `1847/276 = 6.6920289855...` (difference `109/446844`) and the earlier DFZ bound `59767/8929 = 6.6935827...`.

## The linear program

Variables: the 16,383 joint entropies of the publisher's symmetric three-branch copy LP (`frontier-20261028-full-source-lp-optimum-v1.md`, read with erratum `frontier-20261028-full-source-lp-optimum-v1-erratum-1.md`), namely the 1,023 original subsets and the auxiliaries of the branches

1. `b'0` copies `b` over `a,d,e,f,g,h,i,j`;
2. `(d'1,e'1)` copies `(d,e)` over `a,b,c,f,g,h,i`, then `g'2` copies `g` over `a,b,c,d,e'1,f,h,i`;
3. `(f'3,g'3)` copies `(f,g)` over `a,b,c,d,e,h,i,j`, then `h'4` copies `h` over `a,b,c,d,e,f,f'3,i,j`.

Rows: every elemental Shannon inequality of the original set and of each branch set; caps `h(v)<=1`; the ten graph FD equalities; every copy marginal equality and copy conditional-independence equality; invariance of the original profile under the two generators of the eight-element automorphism group; and **conditional union instances of published Dougherty–Freiling–Zeger inequalities** on the original variables.

As a control, without DFZ rows this program (`frontier-20261029-dfz-cutting-plane-v3.py`, SHA-256 `c4088df8b86449aeb8320522dbab3c665e4da3d07fb9aa7dae3af0acc88db43b`) returns exactly the publisher optimum `6.692028985507248` (receipt `frontier-20261029-dfz-cutting-plane-gurpinar-sym-baseline.json`, SHA-256 `554914edb436186360f25d52809d3398c90ca082679e49c0a914948c530cd788`).

## How the cuts were found

The publisher optimum `h*` violates DFZ instances (`frontier-20261029-hstar-dfz-separation-v1.md`). A cutting-plane run preloaded with the 954 instances found by the Shannon-only DFZ run and then rescanning all 27,459,960 conditional union assignments of all 240 listed inequalities converged after one solve: the optimum `6.691785052501545` satisfies every scanned instance (receipt `frontier-20261029-dfz-cutting-plane-gurpinar-sym-result.json`, SHA-256 `5a544c2bf5816b1e7aa998d045f2caa34edec81c4c770bfd396b531c6f95527c`).

## Exact certificate

`frontier-20261029-dfz-certificate-producer-v3.py` (SHA-256 `af0cdfbceca5a57ec1546fec9babe34ba502804d9f6a849b296c0aee6d61fe10`) re-solves the final program by IPM with crossover, takes the 1,661-row basic dual support, and solves the dual identity exactly over the rationals. Certificate `frontier-20261029-dfz-certificate-gurpinar-sym-v1.json`, SHA-256 `23de71c60395cc02170b4d80cbcd5ed3ebfff0243fd61f3a1bf9dfdd6df7f3ad`:

`h(V) = sum_i w_i row_i` coefficientwise, with `w_i <= 0` on every `>=0` row and `w_i >= 0` on the cap rows, so `h(V) <= sum(cap multipliers) = 10834/1619`.

Row kinds in the support: 952 elemental CMIs, 21 monotonicity rows, 10 FD equalities, 3 caps, 197 copy marginal equalities, 5 copy independence equalities, 471 symmetry equalities, and **2 DFZ instances**, of the four-copy items `2 5 2 1 2 0 0 2 0` (copy steps `rs ad bc.t c abr.`) and `3 7 2 2 3 0 0 3 2` (copy steps `rs bd ac.t c abs.u t bcr.`).

## Independent check

`frontier-20261029-dfz-certificate-check-v2.py` (SHA-256 `6c0a9c8f196cc39c4f13804a0827c4aa42606a4850e43091cef15763be47cce5`) shares no row-building code with the producer. It rebuilds every row from its semantic description with Fractions, re-encodes the three copy branches independently, re-verifies both automorphism generators, requires each DFZ tuple to appear as exactly re-derived in `frontier-20261029-dfz-inequality-verify-result.json` (SHA-256 `12f6aa96a6ec70ee6622e4d6981d98d3e3d89ff717f061c137d8c1e52699a727`), checks every sign and the coefficient identity, and recomputes the bound `10834/1619`. Negative controls (flipped CMI sign, doubled cap multiplier, removed DFZ verification) are all rejected. Receipt `frontier-20261029-dfz-certificate-gurpinar-sym-check-result.json`, SHA-256 `9c536cd1b260d7f30116cea04c8184adae55e3368ab72354c9f81a66fdd04545`.

## Why every row is valid for the guessing number

Let `X` be the uniform law on the fixed-point set of any strategy with alphabet size `q`. For each of the eight automorphisms `g` take an independent relabeled copy `X^g` (vertex `v` receives `X^g_{g(v)}`), and let vertex `v` hold the tuple `Y_v=(X^g_{g(v)})_g`. `Y` is again a law of fixed points of a strategy on R-minus (each coordinate is determined by the neighbours' coordinates), its entropy vector is the sum of the eight relabeled vectors, and `H(Y_v)<=8 log q`. Dividing by `8 log q` gives an **entropic** vector that satisfies the caps, the FD equalities and the invariance rows, with the same normalized `h(V)` as `X`. It satisfies Shannon and both DFZ inequalities (each holds for every joint distribution), and the copy lemma applied to `Y` itself supplies exact copy variables satisfying every copy equality and every branch Shannon row. Hence every guessing strategy has `log_q(fixed points) <= 10834/1619`.

Imports: Shannon inequalities; the copy lemma; the standard entropy reduction of the guessing number; the two DFZ inequalities, each re-derived exactly from the copy lemma here rather than cited.

## Limits

This is a better entropy LP bound, not an evaluation of `gn(R^-)`. The interval is now `20/3 <= gn(R^-) <= 10834/1619`. Further DFZ instances on copy variables, other non-Shannon inequalities and further copy structures may lower it again; whether `20/3` is the true value remains open.
