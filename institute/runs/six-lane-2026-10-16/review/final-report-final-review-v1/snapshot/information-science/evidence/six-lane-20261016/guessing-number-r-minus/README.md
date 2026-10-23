# info-1 replacement / guessing-number-r-minus — six-lane run 2026-10-16

> **Final status correction (recorded after the host-clock reading 2026-10-16 23:50:34 PDT, the last `date` output before this edit; lane closed).**
>
> - The parent accepted rotation, and the slot moved to `../cdf211-k7/`.
> - Graph binding is DISCHARGED by the parent: `review/guessing-graph-parent-binding.json` and the pinned
>   `guessing-balancing-parent-inputs-v1`. Every "graph binding pending" or "still binding" phrase below is
>   stale.
> - Lemma B and the Φ-equivalence passed parent mechanics and a Claude hostile review, within the
>   parent's stated scope limits.
> - Codex (C1) and (C2) remain UNPROMOTED. The Codex exit status is unrecorded, and the numeric identity
>   checks do not certify the proofs.
> - gn(R^-) is unchanged: 20/3 ≤ gn ≤ 1847/276.
> - No further binary windows or LP retries.

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
- FLOAT, done. The Gürpınar three-block replay (his copy steps (a)–(c) plus Aut symmetry, 16383
  columns, 351788 rows) gives 6.692028956 vs 1847/276 = 6.692028986, a difference of −3.0e-8.
  - Run: HiGHS ipm, crossover off, model status "Unknown"; 48.6 s.
  - Two earlier attempts produced no value: a background nohup run throttled to about 2% CPU was
    killed, and a simplex run hit the 3600 s tool timeout. Both are logged in `evidence/gurpinar-replay.log`.
  - This validates the lane's copy-LP machinery against the published value. It is not an exact
    certificate. Output: `evidence/gurpinar-replay-float.json`, `evidence/gurpinar-master-hbase.npy`.

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
- EXACT (Shannon + FD level) `code/avg_ratio_certs.py` → `evidence/certs/avg-ratio-9vertex.json` (exit 0):
  - For every w, h(V−w) ≤ (2/3) Σ_{v≠w} h(v) holds on FD-consistent polymatroids of R^- − w. The
    rational multipliers are checked coefficient-wise in Fractions with residual 0.
  - Hence any FD-consistent distribution on R^- with a constant vertex has Φ ≥ 0. A product factor
    with Φ < 0 must have H(X_v) > 0 at all 10 vertices.
  - Negative control (`evidence/certs/avg-ratio-negative-control.json`): on the whole graph the
    scheme returns λ = 39/58 ≠ 2/3 and refuses. It gives the exact Shannon average bound
    h(V) ≤ (39/58) Σ_v h(v), i.e. 195/29.

**Biased binary windows: global nonlinear-code search under the frozen max_v rule (2026-10-16 21:30 PDT).**

- Setup:
  - A binary FD-consistent code with N words and every column having ≤ m ones (WLOG minority symbol
    1, since translation is a confusion-graph automorphism).
  - It gives gn(R^-) ≥ log2 N / h2(m/N) via an elementary type-class bridge:
    - restrict C^n to sequences using each codeword exactly n/N times, giving ≥ N^n/(n+1)^N words;
    - every vertex alphabet then has size ≤ C(n, nm/N) ≤ 2^{n h2(m/N)}.
  - Exact criterion: (m^m (N−m)^{N−m})^20 > N^{17N}.
  - The 30 windows with 20/3 < ratio ≤ 1847/276 are searched (`code/biased_binary_search.py`,
    CP-SAT, 3 workers, 120 s each).
- Controls behave:
  - positive (64,32): found, FD verified;
  - negative (88,34) and (41,9), whose ratios exceed 1847/276: INFEASIBLE.
- Results (`evidence/biased-binary-search.jsonl`):
  - INFEASIBLE for 18 windows, N = 41..97. These are CP-SAT solver claims; no independent proof log
    exists.
  - UNKNOWN for 12 windows, N = 98..103, where m ranges 43..51; (102,51) is the plain 102-word
    question. UNKNOWN is not UNSAT.
  - 600 s retry (`code/biased_binary_retry.py`, `evidence/biased-binary-retry600.log`, seed 1):
    - (98,43) INFEASIBLE in 356 s.
    - (99,44), (99,45), (100,46), (101,47), (101,48) and (102,48) UNKNOWN at 600 s.
    - The original job (bg_336) ended with the agent turn after (102,48). The remaining parent-approved
      windows (102,49..51) and (103,50..51) were resumed at the same 600 s limit (started
      2026-10-16T22:51:22-0700). All five are UNKNOWN at 600 s.
  - FINAL: 19 of 30 windows INFEASIBLE (CP-SAT claims, no independent proof logs) and 11 UNKNOWN.
    No code found. Per the parent, no further retries or new windows.
- Removing words preserves (·, m), so infeasibility at (N, m) also excludes every larger N at the same m.

**Option-2 cycle (started 2026-10-16 22:45 PDT): worker-proved claim that Φ ≥ 0 is equivalent to gn(R^-) = 20/3.**

Status: Lemma B and the equivalence were WORKER-PROVED. Later parent messages report:

- Exact parent mechanics passed at 2026-10-16 22:54:23 PDT (parent receipt
  `review/guessing-balancing-parent-check.json`).
- A Claude hostile mathematical review returned ACCEPT (`review/guessing-balancing-review.note.md`).
  Both paths are parent-owned, outside this lane.
- The parent is still binding the graph transcription to the source figure.

Scope of use, as set by the parent:

- Only this transcribed graph, with all FDs holding and the strict inequality |C|^3 > ∏_v |A_v|^2.
- It certifies the existence of an enlarged triangle-padded witness beating 20/3. It does NOT say that
  the original code padded to its maximum alphabet beats 20/3, and it does NOT make
  10 log|C| / Σ_v log|A_v| an achieved rate.
- Any claimed achieved rate needs the explicit P, k, e_T and s together with an exact check
  |P|^3 > s^20. Equality is not an improvement.
- The parent permits the aggregate test as a theorem-based search gate within these limits.

K_T(q) below is the q^2-word parity code {x_a + x_b + x_c ≡ 0 mod q} on the 3 triangle vertices, not
a repetition code.

Lemma B (balancing by triangle padding). Exact arithmetic checks are in `code/balancing_lemma.py` →
`evidence/balancing-lemma-check.json` (exit 0). Claim: if an FD-consistent code C on R^- with projection
alphabets A_v satisfies |C|^3 > ∏_v |A_v|^2, then gn(R^-) > 20/3.

- Ingredients:
  - For a triangle T and q ≥ 1, the clique code K_T(q) (sum = 0 mod q on T, constant elsewhere) is
    FD-consistent. It has q^2 words, alphabet q on T and 1 off T, so Φ(K_T) = 2·3·log q − 3·2·log q = 0.
  - Products of FD-consistent codes are FD-consistent, entropies and log-sizes add, and alphabet
    padding is harmless.
  - The 10 BCDRV cover triangles have an invertible incidence matrix B, with B^{-1}·1 = (1/3)·1
    (exact Fractions). R^- has 16 triangles in total.
- Construction:
  - Let g = 3 log2|C| − 2 Σ_v log2|A_v| > 0 and α_v = k log2|A_v|.
  - Choose L = 3 max_T (B^{-1}α)_T and y = B^{-1}(L·1 − α) ≥ 0, then set e_T = ⌊y_T⌋ and
    q_T = 2^{e_T}.
  - Every vertex log-size of P = C^k × ∏_T K_T(q_T) lies in (L − 3, L].
  - Padding to the maximum s gives 3 log2|P| − 20 log2 s = k·g − 2 Σ_v δ_v with 0 ≤ δ_v < 3. This is
    positive once k·g > 60.
  - BCDRV §3 gives gn(G,s) ≤ gn(G) for every s (TeX lines 407–409), hence gn(R^-) > 20/3.
- Checks and controls:
  - Fan code (625, alphabet 4, g = −12.14): refused. Cover code (2^20, alphabet 8, g = 0): refused.
  - Synthetic inputs are arithmetic tests only, not codes: (102, all 2) gives k = 3531 with exact
    margin 61 bits; a mixed 2/3 alphabet case is also accepted.
  - Mechanics: the fan code × K_{4,8,10}(3) × K_{1,2,3}(2) (22500 words) passes the brute-force FD
    check, and a one-symbol mutation fails it.

Types bridge (standard method of types; Cover–Thomas Thm 11.1.3/11.1.4).

- Let p be a distribution on an FD-consistent code with rational p(c) = n_c/N and Φ(p) < 0.
- Take the sequences in C^{mN} that use each codeword exactly m·n_c times. They form an FD-consistent
  code C_m with log2|C_m| ≥ mN·H(p) − |C| log2(mN+1).
- Its vertex-v projection lies in one type class of size ≤ 2^{mN·H(p_v)}.
- Hence 3 log2|C_m| − 2 Σ_v log2|A'_v| ≥ −mN·Φ(p) − 3|C| log2(mN+1) > 0 for large m, and Lemma B
  applies.
- Irrational p is handled by continuity on the fixed support.

Consequences, with full quantifiers.

- Main equivalence: gn(R^-) = 20/3 ⟺ Φ(p) = 2 Σ_v H(X_v) − 3 H(V) ≥ 0 for every finite distribution
  supported on an FD-consistent code ⟺ |C|^3 ≤ ∏_v |A_v|^2 for every FD-consistent code.
  - (⇐) The uniform distribution on a code over [s] gives 3 log|C| ≤ 2·10·log s.
  - (⇒) This is Lemma B plus the types bridge.
- The parent reports exact mechanics passed and a Claude hostile review ACCEPT (see Status above).
  Within the parent's scope limits, orbit-unbalanced codes or distributions with Φ < 0 are now
  admissible as a search gate. The parent is still binding the graph transcription.
- [Proof sketch, not machine-checked] Group form. gn(R^-) > 20/3 ⟺ there is a finite group G with
  subgroups G_v such that ∩_{u∈N(v)} G_u ≤ G_v for all v and ∏_v |G_v|^2 > |G|^17 · |∩_v G_v|^3.
  - (⇐) The group code {(gG_v)_v} plus Lemma B.
  - (⇒) The Chan–Yeung S_n type-class construction, which keeps exact FDs because the stabiliser of
    the N(v)-columns fixes the v-column.
- LP transfer (proof). The feasible base vectors of any Shannon + FD + copy-lemma LP form a convex
  cone containing all entropic FD-consistent vectors, including the triangle codes. Padding then
  shows: the LP proves Φ ≥ 0 ⟺ its max-normalised optimum (h(v) ≤ 1) is ≤ 20/3. Every known LP
  fails this; Gürpınar gives 1847/276 > 20/3, and the replay above agrees numerically.

Φ on existing exactly FD-checked codes (`code/phi_codes.py` → `evidence/phi-existing-codes.json`;
these are evaluations, not new searches).

| Code | Uniform Φ | Float min over weights | Note |
|---|---|---|---|
| CP-SAT 88-word | 0.538 | 0.424 (full support) | |
| control 64-word | 1.994 | → 0 | collapses to a triangle sub-code |
| fan 625 | 6.99 | → 0 | collapses to a point |

No Φ < 0 was found.

**Obstruction for this representation (option 2).**

1. Proving Ing + 3S ≥ 0 for all codes is the open problem itself (equivalence above), not a weaker
   surrogate.
2. Ingleton-conclusion conditional inequalities cannot work. The exact 625-word fan code satisfies
   all global FDs and violates all 8 diamond Ingletons, so no inequality whose hypotheses are implied
   by the R^- FDs can conclude any diamond Ingleton.
3. Kaced–Romashchenko-type inequalities with a functional-dependence hypothesis (H(C|AB) = 0 and
   I(A;B|C) = 0 ⇒ Ingleton) need I(A;B|C,Z) = 0. When that CI is forced by FD closure (A or B
   ⊆ cl(C ∪ Z)), Ingleton already follows from Shannon:
   - with A = f(C,Z), I(C;D|Z) = I(A;D|Z) + I(C;D|A,Z);
   - I(A;D|Z) ≤ I(A;B|Z) + I(A;D|B,Z) ≤ I(A;B|Z) + I(C;D|B,Z).
   So these give nothing beyond Shannon. Boege's ten CI sets were killed earlier.
4. Copy-lemma LPs must reach exactly 20/3 in max normalisation (LP transfer), against a best known
   1847/276.

**Codex consult on the option-2 bottleneck.**

- Run: gpt-6.1-sol max, read-only, empty workdir. It is cross-vendor relative to this lane and
  same-vendor relative to the current parent.
- Receipt `review/codex-phi-receipt.txt`: output complete (stderr ends "tokens used 27,230"); exit
  status unrecorded because the wrapper hung and the lane terminated it.
- Output: `review/codex-phi-out.md`. It proves two construction obstructions (C) and neither proves
  (A) nor refutes (B).

Both claims are Codex-proved, re-derived by hand in the lane, and UNPROMOTED.

- **(C1) Group-homomorphism codes.**
  - Claim: let K be a subgroup of a product of finite groups A_1 × … × A_10 (coordinatewise product)
    satisfying the R^- FDs. Then EVERY distribution on any coset of K has Φ ≥ 0.
  - Doubling step: with Y, Y' iid and T = YY',
    2Φ(Y) = Φ(T) + E_t Φ(Y'|T=t) + 2 Σ_v I(Y'_v; T_{−v} | T_v).
    A maximum-entropy minimiser of Φ is therefore uniform on a subgroup J.
  - Uniform step: on J the coordinate kernels are normal. In each Z-slice, the coset of
    (L∩N_3)(L∩N_10) is extractable common information of X_3 and X_10, with
    H(W) = I(X_3; X_10 | Z = z). This forces the diamond Ingleton, so Φ = Ing + 3S ≥ 0.
  - Coverage: every linear or abelian code and all their reweightings. Over a finite field, a
    counterexample must break an FD on its affine span.
- **(C2) Correlated proper gadgets.**
  - Claim: suppose X_v = (Y^1_v, …, Y^r_v), and every component's projected code is FD-consistent with
    a constant coordinate. Then Φ(X) = Σ_a E Φ(Y^a | Y^{<a}) + 2 Σ_{a,v} I(Y^a_v; Y^{<a}_{−v} | Y^{<a}_v),
    and this is ≥ 0 by the exact 9-vertex lemma.
  - Consequence: correlated products or restrictions of local gadgets (fan-type, triangle-type) can
    never give Φ < 0.
- **Lane numeric checks** (`code/check_codex_phi_identities.py` → `evidence/codex-phi-identity-checks.json`,
  all_ok):
  - the doubling identity on three random F_2 subcodes and on a non-abelian S_3 × S_3 code embedded
    in S_3^10, |diff| < 1e-12;
  - the chain identity on random two-component laws, exact;
  - one minimisation-lemma instance: subgroup minimum 0 over all 67 subgroups, float law minimum
    6.7e-4, not below it.
- Not covered: general nonlinear codes, and coset (group-characterisable) codes whose coordinate
  subgroups are non-normal.

Recommendation: rotate the slot. Proving Φ ≥ 0 (option 2) is the open problem itself, and no new
valid inequality family is in hand. If the slot instead continues on constructions, (C1), (C2) and
the 9-vertex lemma leave one natural target, the group form of Lemma B with NON-normal subgroups:
find G and G_v with ∩_{u∈N(v)} G_u ≤ G_v and ∏_v |G_v|^2 > |G|^17 |∩_v G_v|^3. Ingleton-violating
families such as PGL(2,q) are the obvious candidates; GAP is not installed here.

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
| Copy lemma (float, exploratory) | targeted single copy X10' over {1,2,3,5,6,7,8,9} + symmetry: 6.69403; best 2-block combo 6.693548 (≈ DFZ, above Gürpınar 1847/276 = 6.69203); brute-force two-step search stopped after 2 configs (both 6.69403). Gürpınar 3-block replay: 6.692028956 (float calibration only) | `evidence/copy-*.json*`, `evidence/gurpinar-replay-float.json` |
| Delsarte/Lovász LP | exponent 6.74 (q=2) to 6.97 (q=16): useless | `evidence/delsarte-lp-Rminus-float.jsonl` |
| q=2 search | CP-SAT best verified code 88 (needs 102), bound 121; weight optimisation on it: ratio ≈ 6.45 | `evidence/mis-q2-Rminus-600s.json` |
| Prior-art screen | EulerSolve index, Zenodo API, Riis 2026 Term-Coding TeX, openai/math tree: no claim on gn(R^-) | `sources/prior-art-screen-gn.json` |
| Codex delegate 1 | completed 20:42 PDT, exit 0 (first launch exit 127, never started; recorded). Its fan-code construction was verified exactly by the lane. Its rate claims are hand-computed, not relied on | `review/codex-diamond-*`, `evidence/fan-code-check.json` |
| Lemma B / equivalence | worker-proved. Parent reports exact mechanics passed and a Claude hostile review ACCEPT; graph binding pending. Φ ≥ 0 for all FD-consistent distributions ⟺ gn(R^-) = 20/3 | `code/balancing_lemma.py`, `evidence/balancing-lemma-check.json` |
| Codex delegate 2 (option 2) | output complete, exit status unrecorded (wrapper hung). Obstructions (C1) group-homomorphism codes and all their reweightings, and (C2) correlated proper gadgets: Φ ≥ 0. Identities checked numerically. No proof of (A), no refutation (B) | `review/codex-phi-*`, `evidence/codex-phi-identity-checks.json` |

Exact items are rational LP certificates or exact finite checks. All other entries are floating or
exploratory and carry no claim.
