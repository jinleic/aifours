# info-5 — exact R-minus target and first written attack

Observed immediately before this freeze: `2026-10-23T14:01:14-0700` (`/bin/date`). Owner: InfoGuessingRminus. Only this directory is writable. Contract-v2 and both operative parent errata apply; the round ends 2026-10-27T12:35:38-07:00.

## Literal target and graph

Determine the asymptotic guessing number of the following **one fixed** undirected loopless graph on V={1,...,10}, or obtain a rigorous numerical improvement of the matched unrestricted interval

`20/3 <= gn(R-minus) <= 1847/276`.

Its 26 unordered edges, with both sight directions present, are

`12 13 14 15 16 17 23 27 29 2-10 34 38 39 45 48 4-10 56 59 5-10 67 68 69 78 7-10 89 8-10`.

This is BCDRV Figure 1's graph R with **only** edge {9,10} removed, not a graph guessed from the nickname. I read the original-source figure render and the earlier parent edge-binding receipt. The input pins below bind that identification.

For each integer s>=2 let A_s={0,...,s-1}. For every v choose an arbitrary deterministic function f_v:A_s^{N(v)} -> A_s. Let C_f be the set of x in A_s^10 satisfying x_v=f_v(x_{N(v)}) simultaneously for all v. Define

`gn(R-minus,s)=log_s max_f |C_f|`,

`gn(R-minus)=lim_{s->infinity} gn(R-minus,s)=sup_{s>=2} gn(R-minus,s)`.

The existence/equality of the limit and supremum is imported from BCDRV §3, also stated as Gürpınar Definition 2.17. No restriction to prime-power alphabets, scalar-linear strategies, uniform vertex marginals, a symmetry group, group codes or a fixed finite s is part of the full target. Randomized strategies do not improve the optimum (BCDRV §2).

A finite set C is FD-consistent exactly when x_{N(v)}=y_{N(v)} implies x_v=y_v for every x,y in C and v. Every distribution on such a support satisfies H(X_v|X_{N(v)})=0. Entropies below use one fixed logarithm base.

## Book versus modern question

The book source is the information-science volume, Science Press 2011, ISBN 978-7-03-031911-1, linked by the earlier six-lane screen to 网络中的信息流最大化 pp.423–424 and 网络信息论 pp.417–419 (PDF offset +21). R-minus is a **later concrete network-coding/guessing-game descendant**, not the book's literal printed question: BCDRV's graph appeared in 2014. The source-volume identity is routed by `books/README.md`; no claim of solving a verbatim book entry will follow from a scoped barrier.

## Current primary baseline and source headroom

1. Baber–Christofides–Dang–Riis–Vaughan, [arXiv:1410.8349v2](https://arxiv.org/html/1410.8349v2), §§2–3, Figure 1, §6 and §8, actually read through source anchors/body: fractional clique cover 10/3; lower bound 20/3; Shannon 114/17; Zhang–Yeung 1212/181; DFZ 59767/8929; Ingleton 20/3. The source explicitly asks whether nonlinear strategies exceed 20/3 or entropy inequalities push the upper bound to it. The HTML's renderer date is not a new paper date; use the arXiv version identity.
2. Gürpınar, [Kybernetika 60(5), 553–575 (2024)](https://www.kybernetika.cz/content/2024/5/553/paper.pdf), Definitions 2.13–2.17, §5.2 and Theorem 5.2, actually read: `gn(R-minus)<=1847/276`, with three copy-lemma blocks and symmetry, and the guessing number remains unknown. DOI 10.14736/kyb-2024-5-0553. This is the strongest matched unrestricted bound found, **not a freshness theorem**.
3. Prior dossier `information-science/evidence/six-lane-20261016/guessing-number-r-minus/README.md` and its receipts were read in full. Its triangle balancing / Phi equivalence and eight conditional-diamond certificates are baselines, NOT discoveries of this slot. The 625-word fan code refutes universal diamond Ingleton; all previous LP/code-search misses and timeouts remain non-results. The two old group/proper-gadget obstruction manuscripts were unpromoted, and will not be silently relabelled new.
4. New source input: Craven, [arXiv:2505.22565v1](https://arxiv.org/pdf/2505.22565), Theorem 1.1 and §§2–3, actually read. Metacyclic groups satisfy Ingleton. His discussion explicitly corrects the old purported nilpotent proof: **nilpotent groups are not generally certified Ingleton by that earlier source**. The new §5 classification also identifies PSL2(11) as a violator; a PGL argument must therefore not assume its index-two PSL subgroup is harmless.
5. Tertooy, [arXiv:2606.21404v1](https://arxiv.org/pdf/2606.21404), Theorem 2.1, actually read, gives current subgroup-classification routing for PGL2(q). The exceptional symmetric/alternating case is compressed in that theorem, so the detailed Dickson source still must be read for a complete application.
6. Mao–Hassibi, [arXiv:0910.1335](https://arxiv.org/pdf/0910.1335), §§I, III–V, actually read: uniform coset entropy formula and the standard PGL2(p), p>=5, family of Ingleton violations. Its smallest-violator statement is computer-assisted prior literature, not this worker's certificate.

Fresh search queries included exact `1847/276`, the graph nickname with guessing number, Gurpinar/Gürpınar with guessing, and recent guessing-number/non-Shannon work. Broad name queries produced much irrelevant material and are not an exhaustive screen. Relevant 2026 Riis term-coding abstracts (2601.16614 and 2602.08110) were read; the earlier pinned TeX screen found no R-minus result. No later matched improvement or resolution was found in the read scope. The latest accessible explicit open statement remains Gürpınar 2024. This gives **PRIMARY-ATTESTED-OPEN-2024 / CURRENT-RESOLUTION-NOT-FOUND**, not certified openness as of today.

Mandatory corpus screen: local `math/lean/docs` and `math/preprints` were searched for guessing, Ingleton/non-Shannon/graph-entropy, Baber/Riis and Gurpinar terms; only unrelated guessing/substring hits appeared. Remote openai/math README and current `CONTENTS.md` (719 manuscripts/372 families) were read/searched; no matched family appeared. This is a catalogue/topic screen, not a proof that every remote manuscript is irrelevant.

## First bounded attack and missing ingredient

The old dossier identifies **non-normal-subgroup group-characterizable constructions**, especially PGL2(p), as the natural remaining construction route. I choose a written **conditional subgroup-localization barrier** for that exact route rather than rerunning its old LPs or binary windows:

- For any uniform group code X_v=gH_v, a conditional distribution after fixing the six variables outside a certificate diamond is a coset distribution on L=intersection_{z in Z} H_z.
- A Phi-negative code must violate every one of the eight conditional diamond Ingletons, so each corresponding L must itself contain an Ingleton offender.
- Use metacyclic Ingleton and the detailed projective subgroup classification to test whether this forces a common normal subgroup into all ten H_v and collapses the entropy profile to a harmless quotient. In particular, test **all subgroups** of PGL2(p), not only the four subgroups in the familiar Mao–Hassibi violation.

The missing ingredient for this route is a completely written, correctly oriented localization/quotient argument together with a primary-source-verified subgroup exhaustion. It is not enough that the ambient group violates the unconditioned Ingleton inequality.

**Consequential delta sought:** a complete all-prime exclusion of the PGL2(p) uniform non-normal coset route (and any justified extensions), which would be a new scoped exact barrier compared with the earlier normal-kernel/proper-gadget baselines. It would not change the unrestricted numeric interval. A genuine new entropy inequality or numeric improvement remains preferable if the written analysis yields one.

**Verification:** freeze a complete proof snapshot and hash it; parent and a genuinely different task agent reconstruct it. Classical imports, computational prior-art imports, proof scope, novelty and significance are separate. No scientific executable check is authorized or planned by this freeze. A later entropy LP/code search requires its own exact parent GO.

**Redirect condition:** if the full subgroup classification or current literature defeats the proposed exclusion, record the actual counterexample/source and continue within the same R-minus problem on a genuinely surviving route. If current primary work already settles gn(R-minus), report to parent and propose a distinct collision-checked problem; do not retain a solved target in the active-unsolved count. Do not turn a standard Ingleton corollary into a claimed universal bound.

## Exact read-only baseline pins (SHA-256)

All paths here are relative to `/Users/jinleic/repos/aifours/`.

- Prior dossier README: `83dd254f95421bcc117d0511b5a7ae9b1eb3f0eb87f09df17e741ec4696a2a5c`.
- Prior `code/graphs.py`: `f1550e4287b9192ed21e2846095da5e7a58ef3169726e8039f9e9de0b91b72c4`.
- `sources/tex/RGraph.ps`: `0913813c0e110f1ec2d29b3839bad7b6f0ddeaa29ff57dac830b257b1279a403`.
- `sources/tex/GuessingGamesNonShannon.tex`: `76d8d5b3a3b733d3322780a75a64b2d32b09b1743dcb5189ceedc7192b6394dd`.
- `sources/Kybernetika_60-2024-5_1.pdf`: `2ce2db1a038aecf3b206c2b105b93c13f02e183f4214e207dc596c15a83e5129`.
- `evidence/certs/diamond_3_10_4_8.json`: `4b058c8a8718ad023d0e9d81f1bf62cf885659498d7194008823539fbc210ab0`.

These six entries are all under the prior dossier root named above. The original figure binding receipt is `institute/runs/six-lane-2026-10-16/review/guessing-graph-parent-binding.json`; it pins the original arXiv source archive as `0fe57c62a08d81b4229ee3793d6038cb450365bb3665286516740bea17ce5f65` and the PostScript member as above. Those historical checks were read, **not rerun**.
