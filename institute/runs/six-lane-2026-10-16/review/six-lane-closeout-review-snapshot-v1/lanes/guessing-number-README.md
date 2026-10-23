# info-1 replacement / guessing-number-r-minus — six-lane run 2026-10-16

Lane owner: worker `InfoBalanced`. The slot was switched from `balanced242`, which is preserved and now
parent-owned (`institute/runs/six-lane-2026-10-16/transitions.json`). Every new file is in this directory.
Prior sources are read-only.

## Frozen target (recorded 2026-10-16 ~20:20 PDT, after the first replay gates and before any construction
## search or new-inequality LP)

**Claim to settle.** Determine the asymptotic guessing number `gn(R^-)` of the 10-vertex undirected graph
`R^-`. Its edges, re-derived from the original Figure 1 PostScript (`code/graphs.py`, `code/verify_graph.py`),
are:

`12 13 14 15 16 17 23 27 29 2-10 34 38 39 45 48 4-10 56 59 5-10 67 68 69 78 7-10 89 8-10`

The graph R adds the edge 9-10. Either outcome counts as a full resolution:
- an exact rational certificate that `gn(R^-) <= 20/3`, using only inequalities valid for entropy vectors
  of exact winning sets (functional dependencies `H(X_v | X_{N(v)}) = 0`);
- or an explicit winning set `C` over an alphabet of size `s` with `|C|^3 > s^20`, verified by brute-force
  decoding (or an equivalent explicit FD-consistent distribution plus the typicality bridge,
  `gn >= H(V)/max_v H(v)`, written out).

An upper bound strictly between 20/3 and 1847/276 is partial.

**Primary status.**
- Baber–Christofides–Dang–Riis–Vaughan, arXiv:1410.8349v2 (TeX in `sources/tex/`): Section 8 says R^- is
  the only undirected graph on at most 10 vertices whose guessing number is undetermined. It reports
  Sh = 114/17, ZY = 1212/181, DFZ = 59767/8929 and Ingl = 20/3.
- Gürpınar, arXiv:2310.09232v2 / Kybernetika 60(5) 2024 (TeX and annex in `sources/tex-gurpinar/`):
  `gn(R^-) <= 1847/276`, by three copy-lemma steps plus symmetry. The value is still unknown.
- Prior-art screen (EulerSolve index, Zenodo API, Riis 2026 Term-Coding TeX, openai/math tree) recorded in
  `sources/prior-art-screen-gn.json`: no claim on gn(R^-) found. A search miss is not novelty.

**Attack protocol.**
1. Replay gates: graph, fractional cover 10/3, Shannon 114/17 and 27/4, and Ingleton 20/3. Floating
   solves first, exact rational certificates afterwards.
2. Test the parent's idea: conditional Ingleton instances whose hypotheses are FD-forced (Boege's ten
   minimal sets).
3. Then either new valid inequality families (copy lemma / conditional non-Shannon / diamond-FD region)
   with exact certification, or a nonlinear FD-consistent construction.

## Status (live)

**Checkpoint 2026-10-16 20:52 PDT: route (B) refuted exactly; no gn change.**

- EXACT (finite check). An explicit global code on R^- violates all 8 diamond conditional Ingletons
  at once. The construction is the Codex delegate's (gpt-6.1-sol max, read-only, receipt
  `review/codex-diamond-receipt.txt`, exit 0); the lane re-verified it independently.
  - Fan gadget (T,A,B,C,D) uses the 5 binary words 00000, 00110, 10010, 11110 and 10001.
  - It is placed on the fans (1;2,3,4,5), (1;2,7,6,5), (8;10,4,3,9) and (8;10,7,6,9).
  - Result: 625 words, alphabet 4 at every vertex, all global FDs hold.
  - For each diamond, I(P;Q|Z) = I(U;V|ZP) = I(U;V|ZQ) = 0 holds by integer cross-products, while
    I(U;V|Z) ≠ 0.
  - A mutation control (one gadget word changed) fails the FD check.
  - Rate: log_4 625 ≈ 4.64; entropy ratio ≈ 4.78. Both are < 20/3, so this is not a lower-bound gain.
  - Consequence: gn = 20/3 cannot be proved by showing a diamond conditional Ingleton holds for every
    R^- code. A proof must trade the Ingleton gap against the certificate's Shannon slack S.
  - Evidence: `code/verify_fan_code.py` (exit 0), `evidence/fan-code-check.json`.
- FLOAT. Diamond-FD distributions reach Ingleton score Ing/H(PQ) = −0.08937 with binary P,Q and a
  non-uniform law (the 4-atom value). Uniform AND/OR gives only −0.06128. Type classes make uniform
  codes approach the same score. (`code/diamond_score_search.py`)
- FLOAT. Adding Ing_i(·|Z_i) ≥ −c·H(P_iQ_i|Z_i) on all 8 diamonds gives:

  | c | Shannon | + copy A |
  |---|---|---|
  | 0.06128 | 6.690251 | 6.688426 |
  | 0.0894 | 6.696336 | 6.69403 |

  The true diamond-FD c is at least 0.0894, so local diamond-score inequalities cannot beat
  Gürpınar's 1847/276, let alone reach 20/3. (`evidence/ingleton-score-lp-float.json`)
- FLOAT. The conditional diamond profile at the LP optima (`evidence/diamond-profile-float.json`) has
  Ingleton score −0.1395 under Shannon and −0.088 under copy A.
- RUNNING. Gürpınar three-block replay, which writes `evidence/gurpinar-replay-float.json`.

**Frozen obligation for unequal alphabets (2026-10-16 21:00 PDT, before any unequal-alphabet run).**

- Aut(R^-) has order 8 and three vertex orbits: O1 = {1,8}, O2 = {2,5,9,10}, O3 = {3,4,6,7}. It is not
  vertex-transitive: the hubs have degree 6, and the degree-5 vertices see 1 hub (O2) or 2 hubs (O3).
  Taking products of a code's 8 automorphic images balances log|A_v| only within each orbit.
- A claim gn(R^-) > 20/3 from codes with unequal alphabets requires all of the following:
  - explicit codes C_1..C_r, each exactly verified FD-consistent on R^-;
  - nonnegative integers k_i such that P = ∏ C_i^{k_i}, padded to s = max_v ∏ |A_{i,v}|^{k_i}, satisfies
    |P|^3 > s^20 by exact integer comparison.
  - Equivalently: the time-sharing LP max Σ λ_i log|C_i| s.t. Σ λ_i log|A_{i,v}| ≤ 1 for EVERY v (a max,
    not an average) exceeds 20/3 at a rational λ.
- Necessary only:
  - |C| > (∏_v |A_v|)^{2/3}, the average condition;
  - H(V) > (2/3) Σ_v H(X_v) for a distribution.
  - A distribution counts only through H(V) / max_v H(X_v), together with a proved typicality bridge.
- Exact identity on FD-consistent vectors, from certificate diamond_3_10_4_8:
  - (2/3) Σ_v H(X_v) − H(V) = S + Ing/3, so Φ := Ing + 3S = 2 Σ_v H(X_v) − 3 H(V).
  - Φ is additive over products.
  - Any product or time-sharing construction beating 20/3 needs a factor with Φ < 0. Uniform alphabets
    beating 20/3 force Σ Φ_i < 0.

**Whole-graph compensation (2026-10-16 21:00 PDT).**

- EXACT identity. `code/s_explicit.py` checks the certificate coefficient-wise in Fractions and lists S as
  155 named elemental terms with multipliers. By conditioning-set size |K| = 0..8 the counts are
  22, 34, 27, 21, 14, 17, 13, 4, 3. Output: `evidence/S-explicit-diamond-3-10-4-8.json`.
- Cover code (positive control, exact GF(2) ranks): S = 0, Ing = 0, identity residual 0.
- 625-word fan code (float entropies from exact counts):
  - Ing = −0.098045 = −(4/5)δ;
  - S = 2.362857 over 74 positive terms, so Φ = Ing + 3S = 6.9905 > 0.
  - Compensation fails by a factor of about 70. The largest weighted terms are I(3;4|5,6,7), I(8;10),
    I(6;7|4), I(1;2), I(6;9), I(8;9|1,7), I(5;6|3) and I(2;5). The gadget's biased bits create pairwise
    dependence that the certificate charges.
- FLOAT screen (`code/avg_ratio_subgraphs.py`, `evidence/avg-ratio-subgraphs-float.json`):
  - With Σ_v h(v) = 1, Shannon + FD gives max h = 2/3 on every 9-vertex induced subgraph. So at the
    Shannon level, no distribution with a constant vertex has Φ < 0.
  - The whole graph allows 0.672414 (×10 = 6.724138).
  - Consequence (float, not yet certified): a useful product factor must use all 10 vertices.

| Gate | Result | Evidence |
|---|---|---|
| Figure-1 edge extraction | 27 node-to-node strokes = R (one degenerate glyph stroke ignored); R^- = R − {9,10}; BCDRV cover cliques present | `evidence/verify-graph.json` |
| Lower bound 20/3 (exact) | explicit alphabet-8 cover code, 2^20 words, brute-force decoding and FD check pass | `code/verify_cover_code.py`, `evidence/cover-code-check.json` |
| Shannon (EXACT) | Sh(R^-) <= 114/17 and Sh(R) <= 27/4: rational dual certificates; identity checked in Fractions and re-checked by an independent parser (rows literally elemental / FD) | `evidence/certs/shannon_*.json`, `evidence/certs-independent-check.json` |
| Aut(R^-) | order 8 by brute force over 10!; = <(1 8)(2 10 5 9)(3 7 4 6),(2 5)(3 6)(4 7)> | inline run |
| Ingleton (float) | disjoint instances: no cut; Z-conditional instances: one round reaches 20/3 | `evidence/ingleton-*.json` |
| Parent idea (FD-forced Boege hypotheses) | quick kill: no valid instance cuts the Shannon optimum; FD-forced CIs are LP equalities, so masks are Shannon-redundant | `evidence/cond-ingleton-valid-Rminus.json` |
| **Key obstruction (EXACT LP facts)** | each of exactly 8 diamond instances Ing(U,V;P,Q \| rest), (2,4;1,3) (2,6;1,7) (3,5;1,4) (5,7;1,6) (3,10;4,8) (4,9;3,8) (6,10;7,8) (7,9;6,8), ALONE with Shannon+FD gives h(V) <= 20/3 (multiplier 1/3, u_v = 2/3). Hence any strategy beating 20/3 violates all 8 | `evidence/certs/diamond_*.json`, `evidence/single-ingleton-instances.json` |
| Diamond FDs do not imply Ingleton (EXACT) | AND/OR 4-atom: all four diamond FDs hold, I(U;V\|P)=I(U;V\|Q)=I(P;Q)=0, Ingleton = −5/2 + (3/2)log2 3 < 0 since 27 < 32 | `code/diamond_and_or.py`, `evidence/diamond-and-or-exact.json` |
| ZY (float) | Z-conditional Zhang–Yeung cuts reproduce BCDRV ZY = 1212/181 | `evidence/zy-cond-cg-Rminus.json` |
| Copy lemma (float, exploratory) | targeted single copy X10' over {1,2,3,5,6,7,8,9} + symmetry: 6.69403; best 2-block combo 6.693548 (≈ DFZ, above Gürpınar 1847/276 = 6.69203); two-step search running | `evidence/copy-*.json*` |
| Delsarte/Lovász LP | exponent 6.74 (q=2) to 6.97 (q=16): useless | `evidence/delsarte-lp-Rminus-float.jsonl` |
| q=2 search | CP-SAT best verified code 88 (needs 102), bound 121; weight optimisation on it: ratio ≈ 6.45 | `evidence/mis-q2-Rminus-600s.json` |
| Prior-art screen | EulerSolve index, Zenodo API, Riis 2026 Term-Coding TeX, openai/math tree: no claim on gn(R^-) | `sources/prior-art-screen-gn.json` |
| Codex delegate | completed 20:42 PDT, exit 0 (first launch exit 127, never started; recorded). Its fan-code construction was verified exactly by the lane. Its rate claims are hand-computed, not relied on | `review/codex-diamond-*`, `evidence/fan-code-check.json` |

Exact items are rational LP certificates or exact finite checks. All other entries are floating or
exploratory and carry no claim.
