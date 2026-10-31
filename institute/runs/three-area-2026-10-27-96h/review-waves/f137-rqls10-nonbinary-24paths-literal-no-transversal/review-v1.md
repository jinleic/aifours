# f137 review v1 — "All 24 literal nonbinary q18 affine paths have no transversal" (PhysicsRQLS10-2, slot physics-5)

**Reviewer artifact.** Same-harness scientific review; NOT human, NOT independent-family, NOT formal/kernel, NOT novelty clearance.
Manifest: `review-waves/f137-rqls10-nonbinary-24paths-literal-no-transversal/manifest-v1.json`, SHA-256 `c1147e9f3f54260e2cdbc78a605ecfc822af0d102ddfdd9ee5e64a47f3925420` (4565 bytes; verified at `2026-10-28T20:34:17-0700 PDT`).
Last `/bin/date` observed before composing this file: `2026-10-28T21:08:12-0700 PDT` (receipt in the bash log; the post-write clock is reported in the reviewer's hand-off message, not back-dated here).
No author contact, web search, external model, Git, deletion, publication or infrastructure action was performed. No author checker was executed or imported; all evidence below comes from reviewer-written code in this directory (`reviewer-*` files, SHAs in §7).

## 0. Verdict (exact scope)

**MINOR findings only; no FATAL, no MAJOR.** The literal theorem — *for each of the 24 specified one-parameter diagonal paths `K(z) = H ⊙ z^{Σ_j co_j M_j}`, for every unit `z`, every physical K-row order `σ`, every transversal permutation `π`, with arbitrary row/column phases and column permutations of `K`, the Fourier-product QLS of `K(z)` has no orthogonal transversal* — is **reconstructed and independently re-established** by the reviewer under the definitions in §1, with the coverage map in §4. The verdict is conditional on: (i) the reconstructed definition of "Fourier-product QLS" and "orthogonal transversal" (§1, finding F4); (ii) the literal bytes of the two data files that define the objects (§2, finding F3); (iii) the same-harness caveat above.

**Explicitly: nothing beyond the 24 literal paths follows.** No statement about any other direction of the four-parameter affine families, any "multiphase"/multi-parameter torus, any BH(10,18) classification, unrestricted QLS10, the "1-RQLS10" target, binary-gaugeability, the q6 theorem, or catalog completeness is established, reviewed, or implied by this review (§4.3).

## 1. Objects and definitions as reconstructed by the reviewer

The two candidate files do not restate the QLS/transversal definitions; the reviewer reconstructed them from the author's scripts (read only) and the predecessor text ("full column orthogonality and row-difference 5 force both even- and odd-half sums to vanish").

* `H` = the 10×10 BH(10,6) exponent matrix given by catalog line `class` (`H[t][c] = line[6+10t+c] − '0'`), `M_j` = four rectangle masks (rows×columns), `co_j ∈ {1,2}`, `R = Σ_j co_j M_j` (integer, `0 ≤ R ≤ 6`), `K(z)[t][c] = ζ6^{H[t][c]} z^{R[t][c]}`, `|z| = 1`. At `z = ζ18`, `K = ζ18^{3H+R}` (the "q18" matrix; the record field `K_exponents_mod18` equals `3H+R mod 18` for all 24 cases — verified).
* **Fourier-product QLS** of a 10×10 complex Hadamard `K` with physical row order `σ ∈ S10`: cell `(r,d)`, `r,d ∈ Z10`, carries the vector `v_{r,d}(t) = ζ10^{rt} · K[σ(t)][d]`, `t ∈ Z10`. Each QLS row `{v_{r,d}}_d` is `diag(ζ10^{rt})` applied to the columns of `K` (orthonormal ⇔ `K` Hadamard); each QLS column `{v_{r,d}}_r` is the Fourier basis times a unimodular diagonal (orthonormal). Row phases of `K` act as a common diagonal unitary, column phases rescale rays, column permutations relabel QLS columns — all harmless for transversals, as the candidate states.
* **Orthogonal transversal**: a permutation `π` of `Z10` such that `{v_{r,π(r)}}_{r}` is orthonormal (one cell per QLS row and per QLS column). "Even allowing repeated rays" is harmless under this definition (two equal rays are not orthogonal).

## 2. Inputs (all re-hashed; all `match: true`) and data dependencies

| role | file (…/parallel-18/rqls10/) | SHA-256 | bytes/LF |
|---|---|---|---|
| predecessor candidate | `frontier-20261028-nonbinary-affine-24paths-no-transversal-v1.md` | `0307896e…1cfc9f2` | 4968/37 |
| literal candidate | `frontier-20261028-nonbinary-affine-24paths-literal-no-transversal-v1.md` | `89b7cec4…c3c8662e` | 4216/23 |
| author 24-path replay (read only) | `frontier-20261028-nonbinary-affine-24paths-replay-v1.py` | `0994d524…098c53e` | 4377/108 |
| author 16-path replay (read only) | `frontier-20261028-nonbinary-affine-16paths-replay-v1.py` | `eaf4daab…6976f996` | 4549/108 |
| author μ6 endpoint certificate | `frontier-20261028-nonbinary-eight-endpoints-v1.json` | `4de192d6…1cf60927a2`† | 141152/1 |
| author endpoint replay (read only) | `frontier-20261028-nonbinary-eight-endpoints-replay-v1.py` | `4e0a6ba3…cf60927a2` | 2890/52 |
| author replay result | `frontier-20261028-nonbinary-eight-endpoints-replay-result-v1.json` | `239bee33…d67dc1052` | 188/8 |

† full: `4de192d65346522eb77f80424f3a808645e11dd26c63e221e14044ae73ed3cd2`. Full values of all seven are in the manifest and were reproduced byte-for-byte (receipt `2026-10-28T20:34:17-0700 PDT`).

**Data dependencies not listed in the manifest but required to fix the objects** (finding F3): `frontier-20261028-q18-nonbinary-twentyfour-v1.json` SHA `776515e99bfc2b04ea7511ab14e971dfa4f0b8bc285df517e5cc5d47c92c11d2` (486186 bytes, 1 LF; matches the SHA cited in both candidates) and `frontier-20261028-aalto-bh10-6-catalog-v1.txt` SHA `3aab0ddb9d500946fbb45909fb6d5f6c46402033e2b26b797fce7a2a3547e281` (3638 bytes, 34 LF; referenced by file name only in the author scripts). The author result files cited by SHA in the candidates were hashed and match (`99554b30…`, `6a07716f…`); the 24-path replay result was read for its per-case counts only. All 34 catalog lines are BH(10,6) by the reviewer's exact check; classes used: 5 (cases 0–3), 7 (cases 4–11), 8 (12–15), 9 (16–19), 13 (20–23).

## 3. Reconstructed argument and reviewer verification

### 3.1 `K(z)` is Hadamard for every unit `z` — verified (24/24)
Row orthogonality as an identity of Laurent polynomials: for rows `r≠s`, `Σ_c ζ6^{H[r][c]−H[s][c]} z^{R[r][c]−R[s][c]} ≡ 0` in `Q(ω)[z,z⁻¹]`; computed with the reviewer's `Q(ω)` arithmetic (basis `1, ω`, `ω² = −1−ω`, `ζ6 = 1+ω`). Column orthogonality follows (square matrix). Also verified exactly at all 72 phases `ζ72^s` in the `Φ72` power basis (`reviewer-endpoints-result-v1.json: hadamard_failures_over_24x72 = 0`).

### 3.2 Half-graph necessity lemma — reconstructed proof
Let `T = {(r,π(r))}` be a transversal and `E = σ({0,2,4,6,8})`. For `r ∈ Z10`, cells `(r,π(r))` and `(r+5,π(r+5))` have inner product `Σ_t (−1)^t conj(K[σ(t)][π(r)]) K[σ(t)][π(r+5)] = 0`; adding/subtracting full column orthogonality (`π(r) ≠ π(r+5)`) gives vanishing even-coordinate and odd-coordinate half sums. The five pairs `{π(r),π(r+5)}`, `r=0..4`, partition the 10 columns ⇒ a **perfect matching in the E-half-graph** on columns (edge `(c,d)` iff `Σ_{t∈E} conj(K[t][c])K[t][d] = 0`). The `E` and `E^c` half-graphs coincide (full sums vanish). Since `σ` is arbitrary, the 252 five-subsets exhaust all cases. Sound.

### 3.3 Root-closure lemma (why unit roots satisfy `z^72 = 1`) — reconstructed and independently re-tested
For `E`, `c<d`, `P(z) = Σ_{t∈E} ζ6^{H[t][d]−H[t][c]} z^{R[t][d]−R[t][c]}` (powers of `z` removed, made monic). If `|z|=1` and `P(z)=0` then `conj(P(z)) = z^{−deg P}·P*(z) = 0` for the reversed-conjugate `P*(z) = Σ conj(a_k) z^{deg−k}`, so `z` is a root of `G = gcd(P,P*)` in `Q(ω)[z]` (the Euclidean gcd is field-independent, so this captures all common complex roots). "`rad(G) | z^72 − 1`" ⇔ every root of `G` is a 72nd root of unity ⇔ every unit root of `P` lies in μ72.
*Repeated-root issue.* `z^72−1` is squarefree, so the earlier test "`G | z^72−1`" fails whenever `G` has a repeated μ72 root although the conclusion still holds; the author's correction (squarefree part `G/gcd(G,G')`) is sound. **Reviewer method (different):** layer stripping — repeatedly divide `G` by `gcd(G, z^72−1)` until constant; fail iff a non-constant remainder has trivial gcd. Results (`reviewer-paths-result-v1.json`): 272160 half-polynomials, 11264 identically zero (identity edges), **1495 distinct monic normal forms globally**, per-case distinct counts **identical** to the author's replay result (648, 672, 333, 327, 330, 324, 639, 339, 341, 341, 341 …); layer-stripping closure holds for **all 1495**; the naive test fails for exactly 6 polynomials in each of cases **8–11 and 20–23** (48 total), all with repeated gcd roots — precisely the author's account. Numeric cross-check (`numpy.roots`): 564 unit-modulus roots over all 1495 polynomials, worst distance to μ72 = 2.5e-8. Cyclotomic census: gcds contain `Φ_d` parts for `d ∈ {1,2,3,4,6,8,9,12,18,24,36}` — non-μ6 phases genuinely occur, so the 66-phase endpoint scan (3.5) is necessary, not decorative.

### 3.4 Generic phases `z ∉ μ72` — verified
For such `z` every nonzero `P` is nonzero at `z`, so the half-graph equals the identity-edge graph (edges with `P ≡ 0`). Reviewer: all 24×252 identity-edge graphs have **no perfect matching** (explicit enumeration of the 945 perfect matchings of `K10` as 45-bit masks; author used recursive bitmask search). Hence no transversal for any unit `z ∉ μ72`.

### 3.5 Phases in μ72∖μ6 (66 per path) — verified
Exact half-graphs at `K = ζ72^{12H + sR}` in the reviewer's `Q(ζ72) = Q[x]/(x^24 − x^12 + 1)` power basis (author used the `Q(ζ8)⊗Q(ζ9)` tensor basis), numpy subset sums, 945-matching test, 3456 random entries re-derived scalar-exactly and numerically with 0 mismatches: **no matching half for any of the 24 paths at any of the 66 phases.**

### 3.6 μ6 phases for the 16 paths (cases 0–3, 12–23) — verified; no catalog import needed
Same computation at `s ∈ {0,12,…,60}`: no matching half at any phase. Together with 3.3–3.5 these 16 paths are closed for all `|z|=1` using only the literal `H` line (no completeness of the 34-class catalog, no q6 theorem). Reviewer recomputed the partition {0–3,12–23} vs {4–11} from scratch (the author's 16-path replay reads it from a squarefree-result file; moot here).

### 3.7 μ6 phases for cases 4–11 (48 endpoints) — verified three ways
(a) **Pair structure.** At each of the 48 endpoints exactly two five-subsets have a perfect matching and they are complementary (`exactly_one_complementary_pair = true` for 48/48); the normalized half `E0 ∋ 0` equals the author's `even_half` in all 48 records. The 48 graphs were recomputed directly in `Q(ζ6)` and agree with the `Φ72` graphs.
(b) **Normalization (symmetry caller) — re-derived.** Coordinate shift `σ'(t)=σ(t+1)` gives `v'_{r,d} = ζ10^{−r}·(cyclic shift of v_{r,d})`, preserving all inner products and swapping `E ↔ E^c`; shift by 2 places K-row 0 at coordinate 0; the QLS row shift `r ↦ r+r0` is the common diagonal unitary `diag(ζ10^{r0 t})`, placing the transversal's column-0 cell at `(0,0)`. Hence WLOG `σ(0)=0`, `σ(even)=E0`, `(0,0) ∈ T`: `4!·5! = 2880` orders. (c) **Row-digit obstruction.** `⟨v_{0,0}, v_{r,d}⟩ = Σ_t ζ10^{rt} ζ6^{K[σ(t)][d]−K[σ(t)][0]}` computed exactly for all 48×2880×9×9 = 11 197 440 sums in the reviewer's **`Q(ζ3)⊗Q(ζ5)` tensor basis** (own conventions, `ζ30^e = (−1)^e ζ3^e ζ5^e`) and in the `Φ30` power basis, plus floating point: 0 disagreements. The author's digit (always `1`) is an obstructing row in **all 138 240 orders**; in fact rows `{1,3,7,9}` obstruct in every order at every endpoint, every order has 4–8 obstructing rows, and no order lacks one. A row with no orthogonal candidate in columns 1..9 cannot be filled by a transversal containing `(0,0)` — contradiction. Sound.
(d) **Normalization-free confirmation (does not use (b)).** For all 48 endpoints, all `2·5!·5! = 28 800` physical orders with `σ(even) ∈ {E0, E0^c}` (positions arbitrary, `σ(0)` free) and `π(0)` free, exact backtracking over `π` with the full 10×10×9 orthogonality table per order: **1 382 400 orders, 0 transversals** (2880 table entries re-derived scalar-exactly, 0 mismatches). Only the half-graph lemma 3.2 is used.

### 3.8 Author certificate format — consistent
48 records keyed `(case, phase6, even_half)`, `digits` length 2880, enumeration order `[0,b0,a0,b1,a1,…]` over `permutations(E0∖{0}) × permutations(E0^c)`; all digits are `'1'`. The author replay result (`239bee33…`) reports `halfgraphs 12096, normalized_matching_halves 48, row_orders 138240` — consistent with the reviewer's counts. The author replay was **not executed**.

## 4. Coverage map (which endpoints are covered by which argument)

| region of `|z| = 1` | paths | closing argument | reviewer evidence |
|---|---|---|---|
| `z ∉ μ72` | all 24 | root closure (3.3) + identity-edge graphs have no PM (3.4) | 1495/1495 closure, 6048/6048 graphs no PM |
| `z ∈ μ72∖μ6` (66 phases) | all 24 | explicit `Q(ζ72)` half-graphs, no PM (3.5) | 24×66×252 graphs, 0 PM |
| `z ∈ μ6` (6 phases) | 0–3, 12–23 | explicit half-graphs, no PM (3.6) | 16×6×252 graphs, 0 PM |
| `z ∈ μ6` (6 phases) | 4–11 | one matching pair + normalization + row-digit obstruction (3.7a–c); independently normalization-free search (3.7d) | 48/48 pairs; 138 240/138 240 digits; 1 382 400 orders, 0 transversals |

### 4.3 What does NOT follow (explicit)
Other phase directions of the four-parameter families; any multi-parameter ("multiphase") torus; any BH(10,18) classification or completeness; unrestricted or non-product QLS10; the maximal 1-RQLS10 target; "none is a 1-RQLS"; binary-gaugeability / F3 certificates (`row_gauge_obstruction_digits`, not examined); the predecessor's q6 theorem and the 34-class classification (not needed, not reviewed); novelty.

## 5. Controls (all reviewer-written; `reviewer-controls-result-v1.json`, 186.9 s, `2026-10-28T21:04:56 → 21:08:03 -0700`)

| id | control | result |
|---|---|---|
| A | root closure must-pass: `Φ6`, `Φ6²`, `(z−1)²`, `z²+1`, `z³−2`, `Φ72`, `Φ9`, `Φ8³`; must-fail: `z²−z/2+1`, `Φ6·(z²−z/2+1)`, `Φ5`, `Φ7`, `Φ16`, `Φ144`, `Φ72·Φ5`; naive test fails on `Φ6²`; **mutation** of a real case-8 polynomial with a repeated μ72 root: ×`(z²−z/2+1)` → fail, ×`Φ6` → pass | PASS |
| B | 48 real `E0` half-graphs have a PM (**positive**), 40 real identity graphs none, 40/40 **planted** perfect matchings detected | PASS |
| C | catalog line 7 is BH(10,6); one-entry mutation breaks 9 column pairs | PASS |
| D | **digit mutation**: replacing every author digit by a non-obstructing row is rejected 138 240/138 240; **planted** orthogonal candidate (column 5 := column 0 in physical order) makes row 1 non-obstructing (candidate `d=5`); scalar routine matches the vectorized one | PASS |
| E | normalization-free exhaustive transversal search (3.7d) | PASS (0 transversals) |
| F | **odd-order end-to-end positive control**: `n=5`, `K=F5`: transversal finder finds the diagonal transversal (and `π=(0,2,4,1,3)`, `(0,3,1,4,2)`), row-obstruction routine reports no obstructing row for `σ=id` | PASS |
| G | even-order positive-control searches (see F1) | no transversal found anywhere |

## 6. Findings

* **F1 — MINOR (significance, not correctness) [INFERENCE flagged].** The requested "known case with a transversal" at **even** order could not be produced: exhaustive exact searches found no Fourier-product transversal for order 4 (Klein, `F4`; and the complete family `F4(x)`, 720-point grid, min max-offdiagonal 2.0), order 6 (Tao `S6`, `F6`), order 10 (block `F2⊗F5`, all 362 880 normalized `σ`; permuted-Fourier family `ζ10^{ρ(t)τ(r)−tr}`, 970 496 random `ρ` with full `τ` backtracking); unconstrained numeric optimization over **all** unimodular `K` (loss `‖K*K−nI‖²+‖(F⊙K)*(F⊙K)−nI‖²`) reaches 0 at `n=5` but stalls at ≈4.7n for `n=4,6,8,10` (60 restarts each). For `n=4` the reviewer's hand reduction (parity blocks are 2×2 Hadamard; pair conditions force `d=±1`, then a contradiction in the `(2,3)` pair) gives a full proof of impossibility. **If** "no Fourier-product QLS of even order has a transversal" is a general (possibly known) theorem, the 24-path result and the q6 theorem are special cases with no independent content; the reviewer could not check the literature (no web search). The candidate claims no novelty, so this does not affect its correctness verdict, but the parent should weigh it before any registration/consumption.
* **F2 — MINOR (documentation).** `frontier-20261028-q18-nonbinary-twentyfour-v1.json` has `scope: "12 literal q18 matrices…"` but 24 records; both author replay docstrings say "12 selected paths" although they process 24/16.
* **F3 — MINOR (process).** The manifest lists neither data file that defines the objects (twentyfour JSON, catalog). The literal candidate cites the twentyfour JSON by SHA (matches); the catalog is identified only by file name in the scripts. SHAs recorded in §2; the verdict is conditional on these bytes.
* **F4 — MINOR (definitional).** Neither candidate file restates the QLS/transversal definitions; the verdict is relative to §1. If a weaker notion of "transversal" (any 10 mutually orthogonal cells without the one-per-row/column constraint) were intended, lemma 3.2 would not apply and the theorem would need a different proof.
* **F5 — INFO.** The predecessor's §1 claims about `z=ζ18` (maximal 100-ray, not binary-gaugeable, "none is a 1-RQLS") are outside this assignment and were not verified. The 24-path replay result's scope string "six q6 endpoints conditional" is correct for that file; the literal candidate resolves those endpoints.

No FATAL or MAJOR finding. INCONCLUSIVE items: none within scope.

## 7. Reviewer artifacts (this directory; SHA-256, bytes/LF; receipt `2026-10-28T21:08:12-0700 PDT`)

| file | SHA-256 | bytes/LF |
|---|---|---|
| `reviewer-cyclo-v1.py` (exact arithmetic library + self-tests) | `d431b6fe55e155bdaa8f9df74710a560cdad59d8fd0ac0b445adadbce853cf8b` | 13229/339 |
| `reviewer-paths-v1.py` | `d847073e76f93dede9cc38ea6aed6b12d20104de9cfdebe5e3e3600f9d858db1` | 9868/166 |
| `reviewer-paths-result-v1.json` (`20:49:36 → 20:49:46`) | `9a786b64c434496c260e21174f259d2c72740a98da738849ea11b0aee5f4bd9b` | 17743/864 |
| `reviewer-endpoints-v1.py` | `d9a61469dafafdc1be62c870cd5a1c3fd3285f688815637329ce8c78122544e8` | 12150/176 |
| `reviewer-endpoints-result-v1.json` (`20:51:32 → 20:51:38`) | `31d99ef73a9fdb0315384f283eef8b01a96debff250b95b2e7b591e20f1d9d55` | 47371/4049 |
| `reviewer-controls-v1.py` | `0946102f3cf6cf79d7c0a7f2b393a34c932232017a1933e4a076d89fff93b7ae` | 16394/235 |
| `reviewer-controls-result-v1.json` (`21:04:56 → 21:08:03`) | `8a35ebd97ea3b7c9d87a42dfc1aff39803178eeb1574290fd9d2299f2855e0d6` | 5922/302 |
| `reviewer-positive-search-v1.py` / `-result-v1.json` (`20:53:53`, 240 s) | `c22f884b…fbb3c` / `05d8ffed…5cace` | 5732/121, 529/30 |
| `reviewer-positive-search2-v1.py` / `-result-v1.json` (`20:57:54`, 47 s) | `4495e500…05f5fb` / `2b40698a…94f680` | 4510/83, 503/30 |
| `reviewer-positive-search3-v1.py` / `-result-v1.json` (`21:00:41`, 14 s) | `96a43c1d…91aa7` / `9b8318d0…94e497` | 3174/51, 1047/69 |

Full SHAs of the abbreviated entries: `c22f884bdd5caf9170239382b19860803220430f777fbaf3dc26bd1c5f7fbb3c`, `05d8ffed115097d54ea7fb222bc7cac27e00987c74d5b275c6ac518bf845cace`, `4495e5000fd6030f8ffb733581daa27dfffcd876a8982b552e5b3abbe105f5fb`, `2b40698a1a99f178b6673428b9a3075ffd8059b450d0e1ad4eff90cef594f680`, `96a43c1db1b029650bf127dac9c19fa926dfe5ced90aa47685fedccf06891aa7`, `9b8318d0aa6199d9cb56204cb00babf4d27e2c75bb68a2eb5b67293a9494e497`. Environment: Python 3.14.3, numpy 2.4.3, macOS arm64; no sympy; nothing executed outside this directory's reviewer scripts.
