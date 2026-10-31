# Independent written review (slice `written`): candidate global AME(4,6) support lower bound 45

Reviewer: same-harness independent agent for review wave **f107** (not the author PhysicsAME46-2). Native clock from `/bin/date` immediately before composing this file: `2026-10-28T20:48:13-0700 PDT`; this is a prewrite clock, not a completion time. Pins were verified at `2026-10-28T19:11:08-0700 PDT`.

Manifest: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f107-ame-global-support-lower45/manifest-v1.json`, SHA-256 `b1565273e7c79e38346cc455e1a6e93943da91421f6d003d523b3005cb3b9300` (observed; matches the assignment pin).

This review is same-harness: it is not cross-vendor, human, formal/kernel, source-priority, or novelty verification. No author contact, external model, paid API, publication, deletion, Git, or infrastructure action was taken. The sibling slice's files (`finite-check-v1.py`, `finite-receipt-v1.json`, `finite-review-v1.md`) appeared in this directory during the review and were **not** read or used; the only artifacts cited below are the manifest inputs and my own `proof-*` files.

## 0. Verdict

**No FATAL or MAJOR defect found.** Every proposition of the candidate reconstructs from the pinned texts; each of the five assignment targets (a)–(e) is re-derived in §3 below, and my own exhaustive finite controls (§4) found no counterexample to any structural claim. Two MINOR presentational points are recorded in §6. The result remains **conditional** on (i) the pinned ≥42 and ≥44 dependencies and the 2n+2 lemma, which I also reconstructed (§2), and (ii) the external classical no-OLS(6) theorem (Tarry), which the candidate imports; my own exhaustive search reproduces that import (§4.5) as a control, not as a replacement for the classical proof. Limits are in §7.

## 1. Pins and reading order (all verified: SHA-256, bytes, LF)

| # | file (`…/physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/`) | SHA-256 | bytes | LF | status |
|---|---|---|---|---|---|
| 1 | `frontier-20261028-global-ame46-lower42-review-packet-v2.md` | `50e97ebd…edf` | 11168 | 107 | match |
| 2 | `frontier-20261028-global-ame46-support-lower44-v1.md` | `89e2de23…a30` | 10465 | 79 | match |
| 3 | `frontier-20261028-unitary-two-excess-classification-v1.md` | `4a6d012d…bd0` | 5264 | 43 | match |
| 4 | `frontier-20261028-global-ame46-support-lower45-v1.md` | `26a4115f…121` | 15561 | 103 | match |
| 5–10 | six author control files (`eight-residual-rectangle-parity-v1.{py,json}`, `eight-residual-mixed-direct-v1.{py,json}`, `three-qubit-shadow-control-v1.{py,json}`) | as pinned | as pinned | as pinned | match |

Full digests: 1 `50e97ebd0a30f2bcb1999fa85896f88bf4590d89fd897c60d9de53fe5775bedf`; 2 `89e2de23d4777697bd4e2b55e5925f3bd50f5f07c2e0e18aeb548ddd70052a30`; 3 `4a6d012d39ae8ae3acd0bb2ba04d0f79c824a9002633a0d2a45d91038119bec0`; 4 `26a4115ff62f56320af2647c550072255d0ab7c6c90de49ef83025d9219a1121`; 5 `e8fd4a05b0305fe399b39230c965cffb9110d68701346d258b34b8a5525950ee`; 6 `78fb02b43d535fb1228c3e940b5c45afabb49278c2aeb0816ff1bd9fa4886494`; 7 `77cb2b5ebaca90b43c06f996a1d4279be19130d4a2751d89808bc21d73741a82`; 8 `3c7e09fc9bfcb4dd20d5c8149feddad2a5722893c58117a69f0d02d8fa320cc2`; 9 `9ed98305b8ad05ce15642dc05da8a3024a7d352929bdb53b4f062b7feee72017`; 10 `2db5eeabadae4bcee850cd0078622e49777bfadeb4a2f478c3ac8940bb685f96`. The four mathematical bodies were read in full and in order. Author control files were read for scope only (receipts: 144 parity forms / 576 mixed supports / all 576 with AD|BC overlap; parity masks 216/108, 72, 24/24); none was executed or imported.

Notation below follows the candidate: `P` = coefficients of modulus 1/6 (`t = |P|`), `E` = remaining support, `n = 36 − t`, `N = t + |E|`.

## 2. Dependencies reconstructed

### 2.1 ≥42 packet (input 1)

- Row/column norms of the 36×36 unitary `U = 6ψ` are 1 in every 2|2 cut, so a modulus-1/6 coefficient is the unique nonzero of its row and column in every cut; two P entries never share two coordinates; after removing the t singleton rows/columns the residual n×n block is unitary with no singleton row or column (a singleton would have modulus 1/6 and belong to P). Hence `|π_ij(E)| = n` with ≥2 extensions each, and `N ≥ t + 2n = 72 − t`. Checked.
- `t = 36` ⇒ all six pair projections of P bijective ⇒ a pair of orthogonal Latin squares of order 6 (coordinates 3,4 as functions of (1,2)); `t = 35` ⇒ 1×1 residual singleton. Checked; the OLS step is the Tarry import.
- Incidence lemma: for coordinate i with r values, every fiber varies in ≥2 other coordinates (a one-coordinate variation contradicts the two-extension rule), and `Σ_v(|π_j(E_v)| − 1) = n − r`, so `2r ≤ 3(n − r)`, `r ≤ ⌊3n/5⌋`. Checked. `n ∈ {2,3}` ⇒ `r ≤ 1` ⇒ contradiction. Checked.
- `n = 4`: all coordinates binary, residual 4×4 unitary blocks ⇒ `φ = 3ψ_E` is AME(4,2); the Pauli/spin-flip argument gives `Tr(ρρ̃) = (1 − 12 + 3)/16 = −1/2 < 0`. I re-derived the weight bookkeeping (weight-3 sum 12 from four 3-qubit marginals of purity 1/2, weight-4 sum 3) and the sign rule `Y P̄ Y = −P` for `P ∈ {X,Y,Z}`. Checked.
- `n = 5`: equality in the incidence count forces three 2×2 fibers, each fixing one coordinate; the XOR condition `e_j ≠ e_k` for all three pairs is unsatisfiable. I re-derived the five-point count (base 4 + exactly one added edge point, the two possible new points being distinct). Checked.

### 2.2 ≥44 (input 2)

- One-excess lemma (`2n+1` impossible) and `2n` lemma (`n` even, support = disjoint full 2×2 blocks): both follow from "two rows meeting in one column cannot be orthogonal"; checked, including the 6-cycle unique-overlap step.
- `N = 42` ⇒ `t = 30, n = 6, |E| = 12`, each residual row/column degree exactly 2, alphabets ≤3, patterns (3,3,3,3) or one binary. Four-point fibers; a fiber is correlated on at most one pair; all-ternary excluded by the square-intersection count (7 > 6) needing ≥6 correlations from ≤3. One-binary case: `E = S × {b_0,b_1}`, graph on S with the involution `r ↦ −1/r̄` (fixed-point-free, so bipartite), 2-colouring gives six words pair-disjoint from each other and from P ⇒ 36 pair-injective words ⇒ OLS(6). Checked in every step, including that the two columns in the (B, shared-coordinate) cut are supported on exactly the two B rows by pair-injectivity of S.
- `N = 43` ⇒ `(t,n,|E|) ∈ {(30,6,13),(29,7,14)}`, excluded by the two lemmas. Checked.

### 2.3 Unitary 2n+2 classification (input 3) — checked only at its pinned source

Degree patterns (4,2,…) and (3,3,2,…). One degree-4 row: neighbours use two disjoint pairs; two degree-2 rows on the same pair would span C² and force the degree-4 row's restriction to vanish; a single neighbour makes columns a,b orthonormal on two rows, so the 2×2 block is unitary and the degree-4 row would have norm > 1. Two degree-3 rows: share 0 or 2 columns ⇒ a column of degree 1; share 3 ⇒ exactly one degree-2 neighbour ⇒ an 8-entry 3×3 direct summand, remainder a union of 2×2 blocks ⇒ `n` odd. The 3×3 real example is orthogonal (row inner products 0, norms 1). Checked. Independent finite control at the pinned sizes: no admissible 6×6 pattern with 13 or 14 entries and no 7×7 pattern with 15 (§4.1).

## 3. Reconstruction of the candidate (input 4)

### 3.1 Reduction to `t = 28, n = 8, |E| = 16`

`N = 44` and `N ≥ 72 − t`, `t ≤ 30` give `t ∈ {28,29,30}`. `t = 29`: `|E| = 15 = 2·7+1` (one-excess lemma). `t = 30`: `|E| = 14 = 2·6+2` with `n = 6` even (2n+2 lemma). Remaining `t = 28`, `n = 8`, `|E| = 16 = 2n`: every residual row and column in every cut has degree exactly 2, so every pair projection has 8 values with exactly 2 extensions each. Checked. (The ≥44 `2n` lemma additionally says the residual support in each cut is four disjoint 2×2 blocks; the candidate does not need this, but my controls use it as the necessary "no unique overlap" filter.)

### 3.2 Alphabet and balanced-fiber facts (§2 of the candidate)

`r_i ≤ ⌊24/5⌋ = 4`; no constant coordinate (≤4 < 8); a binary coordinate cannot pair with a binary or ternary one (≤6 < 8), so the patterns are exactly `(2,4,4,4)`, `(3,3,3,3)`, `(3,3,3,4)`, `(3,3,4,4)`, `(3,4,4,4)`, `(4,4,4,4)`. For a size-4 coordinate A: each fiber varies in ≥2 coordinates, each varying coordinate contributes ≥2 values × 2 extensions, so fibers have ≥4 points; 4·4 = 16 forces exactly 4, and `4 = 2·(#values)` forces every other coordinate to take exactly 2 values twice per fiber. A 2×2 table with margins (2,2) is full or correlated; two correlations would make the fiber a function of one bit (≤2 points). The A–j incidence graph for size-4 j is 2-regular on 4+4 vertices: an 8-cycle or two `K_{2,2}`; no row set occurs three times. All checked. My enumeration confirms exactly these six patterns occur and no alphabet exceeds 4 even when the search allows 6 symbols (§4.3).

### 3.3 (a) Fiberwise-free coordinate selection (§3)

Assume pair (j,k) correlated in all four A-fibers; then B is free and `E = ⋃_{s∈S}{s}×B_s` with `|S| = 8`, `|B_s| = 2`, and the three projections of S injective (each has 8 values). For triples sharing coordinate X ∈ {A,j,k}, take the cut with rows (X,B) and columns the other two coordinates: by injectivity the two columns are supported exactly on `{x}×B_s` and `{x}×B_{s'}` with all entries nonzero, so orthogonality forbids `|B_s ∩ B_{s'}| = 1`: the sets are **equal or disjoint** (this covers the unequal case). On equal-set edges `r_{s'} = −1/r̄_s`; `r ↦ −1/r̄` is an involution without nonzero fixed point (`|r|² = −1`), so every equal-set component is bipartite with one common set, and a 2-colouring picks `b_0`/`b_1`; disjoint-set edges differ automatically; non-adjacent triples share no coordinate. Hence the 8 selected words are pairwise pair-distinct, and they are pair-disjoint from P because they sit in residual rows. 28 + 8 = 36 pair-injective words over 6 symbols ⇒ every pair projection bijective ⇒ coordinates 3,4 are orthogonal Latin squares of order 6 ⇒ contradiction with no-OLS(6). Therefore each of the three pairs among the non-A coordinates is full in ≥1 fiber. Checked; no gap found. (Note that for the same-fiber edge, sharing A, the two B-sets are the fiber's set, so equality is automatic and the same orthogonality relation holds.)

### 3.4 (b) Rectangle parity R44/R34 for all permitted incidence graphs (§4)

Equation (2): global multiplicities are 0 or 2, correlated fibers contribute 0 or 2 per pair, so the full fibers satisfy `Σ_{g∈F} u_g v_g^T = 0` over F₂. `|F| = 1` is impossible (nonzero rank-one tensor). `|F| = 3`: if `u_1 ≠ u_2` and `v_1 ≠ v_2` the first two terms have rank 2 ≠ 1; if `u_1 = u_2` then `u_1(v_1+v_2)^T = u_3v_3^T` forces `u_3 = u_1` (or `v_1 = v_2`, leaving `u_3v_3^T = 0`), i.e. three identical row sets on one side — excluded on both sides (2-regular size-4 graph; `{H,H,L_1,L_2}` for the (2,3,3) size-3 graph). `|F| = 2` ⇒ equal rank-one tensors ⇒ equal row sets on both sides. For 4/4: `|F| = 2` splits both graphs along F; `|F| = 4` gives `U^T V = 0`, rank(8-cycle) = 3, rank(two `K_{2,2}`) = 2, `rank U + rank V ≤ 4` ⇒ both rank 2; `ker U^T = {0, 1100, 0011, 1111}` (fiber-pair indicators) and weight-2 columns of V must be pair indicators ⇒ same partition. **R44 checked.** For the (2,3,3) size-3 graph I recomputed the kernel of `[(0,1,1),(0,1,1),(1,1,0),(1,0,1)]^T`: `x_2 = x_3`, `x_0 + x_1 = x_2` ⇒ `{0000,1100,1011,0111}`, unique weight-2 vector `1100 = P`; `|F| = 4` would force all four weight-2 columns of the 4-graph to equal P, emptying rows 2,3; `|F| = 2` ⇒ F = P and the 4-graph splits along P. **R34 checked.** The `{H,H,L_1,L_2}` form is forced by the degree equations `n_1+n_2 = 2`, `n_H+n_1 = 3`, `n_H+n_2 = 3`. "All permitted graphs": my own enumeration of all 90 2-regular 4×4 graphs and all 36 labelled (2,3,3) 4×3 graphs, over every nonempty F, found zero-parity masks only of sizes 2 and 4 for 4/4 (216/108), only size 2 for 3/4 (216), and for 3/3 only `same duplicate pair ⇒ |F| = 2 = that pair` (216) and `different duplicate pairs ⇒ |F| = 4` (216), with zero violations of R44/R34 or of the §7 3/3 dichotomy (§4.2).

### 3.5 (c) Group states and the shadow bound (§5)

Shadow bound: all weight-1/2 Pauli coefficients vanish, so `ρ = I/8 + (1/8)Σ_{w=3} r_P P` and `Y^{⊗3} ρ̄ Y^{⊗3} = I/4 − ρ ≥ 0`, eigenvalues ≤ 1/4, rank ≥ 4; a purifier of dimension ≤3 cannot exist. Checked (identity also verified numerically, §4.4). Group marginals: for the fiber pair `{g_1,g_2}` with `C ∈ C_1`, `D ∈ D_1`, the 8 group entries occupy, in each of the cuts with rows (A,C), (A,D), (C,D), exactly `8/2 = 4` rows which are the full products `{g_1,g_2}×C_1`, `{g_1,g_2}×D_1`, `C_1×D_1`; each such row of `U` has all its nonzeros inside the group (an entry with `c ∈ C_1` lies in fiber `g_1` or `g_2`; an entry with `c ∈ C_1, d ∈ D_2` cannot exist), so the rows are orthonormal within the group; with `φ = 3ψ_group` (norm² `4/36`) each flattening is `U_rows/2`, giving `ρ_{AC} = ρ_{AD} = ρ_{CD} = I_4/4`. **All three two-qubit marginals of `ρ_{ACD}` are maximally mixed**, and `rank ρ_{ACD} ≤` number of B values in the group. Checked. In §6 the fourth dimension is 2 (all-size-4, B splits by R44) or ≤3 (B of size 2 or 3). My enumeration shows every shadow-route survivor has exactly 2 B values per group (§4.3).

### 3.6 Case split with ≤1 non-size-4 coordinate (§6)

(4,4,4,4): §3 gives nonempty F for all three pairs; R44 on (B,C) and (B,D) forces the same partition for all three incidence graphs; shadow with dimension 2. (2,4,4,4)/(3,4,4,4): only the (C,D) pair is used, R44 splits C and D, shadow with dimension ≤3. R34 is **not** used here — correctly, because the (2,3,3) hypothesis need not hold (see §6 M1). Checked.

### 3.7 (d) The (3,3,4,4) one-overlap contradiction (§7)

With B, C ternary the B–C projection has 8 of 9 cells, missing `(ℓ_B,ℓ_C)`; B-fiber sizes are `2·deg = (4,6,6)`, so the A–B graph has degrees (2,3,3) and row sets `{H,H,L_1,L_2}`, defining `P_B` (fibers using `H_B`); likewise `P_C`. §3 gives nonempty `F_BD`, `F_CD`; R34 gives `F_BD = P_B`, `F_CD = P_C` and the D-graph splits along both, so `P_C ∈ {P_B, P_B^c}`. If `P_C = P_B`: `|F_BC| = 4` fails because the low-C column `P_B^c` is not in `ker U_B^T`; `|F_BC| = 2` forces `F_BC = P_B`; then fibers in `P_B^c` are correlated on BC, BD, CD — three correlations. If `P_C = P_B^c`: `|F_BC| = 2` would need `P_B = P_C`; so `F_BC` = all four fibers. I verified this parity configuration is consistent (every B–C pair except `(ℓ,ℓ)` gets multiplicity exactly 2), so the contradiction must and does come from unitarity: in fiber `a ∈ P_B`, CD is correlated, B free over `H_B = {h_1,h_2}`, C uses `{ℓ_C,h_C}`; in fiber `a' ∈ P_C`, BD is correlated, C free over `H_C`, B uses `{ℓ_B,h'_B}`. In the AD|BC cut, row `(a,d_i)` with `c_i = h_C` is supported on `{(h_1,h_C),(h_2,h_C)}`, row `(a',d'_i)` with `b_i = h'_B` on `{(h'_B,h_1'),(h'_B,h_2')}`; since `h'_B ∈ H_B` and `h_C ∈ H_C` the supports meet in exactly `{(h'_B,h_C)}`, so two rows of a unitary have a one-term inner product. Checked. My enumeration: all 162 labelled (3,3,4,4) supports exhibit a unique **row** overlap in exactly this cut (rows = the two size-4 coordinates, columns = the two size-3 coordinates); explicit witness in §4.3.

### 3.8 (e) Maximal-word counts with three or four ternary alphabets (§8)

For ternary B: the B–C projection misses only `(ℓ_B,ℓ_C)`; `ℓ_B` has 2 E-pairs with every other coordinate (fiber 4), each high symbol 3 (fiber 6); P rows with `B = b` number `6 − deg`, each holding one P word: **4 words for a low symbol, 3 per high symbol**; inactive symbols give 6 each (total `3·6 + 4 + 3 + 3 = 28` ✓). A P word with a high symbol at one ternary party cannot be active at another ternary party (all those pairs are E rows).

Four ternary: `4·2·3 = 24` distinct high words (disjoint across parties since a high word is inactive elsewhere), 4 remaining words must carry all four `ℓ` occurrences at every party ⇒ four identical words (indeed the single P row `(ℓ_A,ℓ_B)` would need four words). Checked.

Three ternary + D of size 4: 18 high words; a high symbol h has 3 active D partners in E, so of its 3 P rows `(h,d)` exactly one has active d ⇒ 6 active-D occurrences among the 18; each active d has D-fiber 4 ⇒ 2 E-pairs with A ⇒ 4 P words ⇒ 16 occurrences; the 10 non-high words must all be D-active; but the 4 words with `B = ℓ_B` are among those 10 and can use only `4 − 2 = 2` active D values outside E, each at most once by pair-injectivity ⇒ ≤2 < 4. Checked. My enumeration confirms, for every (3,3,3,x) support, fiber sizes (4,6,6) and P-word counts {3,3,4} per ternary coordinate, and an exact search finds **no** 28-word completion for any of the 1290 (3,3,3,4) or 296 (3,3,3,3) supports (§4.3) — the counting conclusion is confirmed by direct search without using the counting.

## 4. Independent finite controls (reviewer artifacts in this directory)

- `proof-independent-controls-v1.py` SHA-256 `d84482fefea70b60131d7acdc8ec4f2182c32e2f1dc5a5d342a8f42048398849` (27222 B); receipt `proof-independent-controls-v1.json` SHA-256 `26882692fb26472cdf20d1c0281eeebf3f80b36f3432b452989308df6ed412f3` (5828 B); optional survivor receipt `proof-independent-controls-v1-survivors.json` SHA-256 `92c62332f089450e5ab96088c9926f48561f55e16b32715f91fe3210ab14fc40`.
- `proof-ols6-control-v1.py` SHA-256 `ddb6a791a0a970a46a02af795703e53a6d7426ddfcf9698551638f1bcc956b77`; receipt `proof-ols6-control-v1.json` SHA-256 `530b4ba2b08fdbc32ee8e08e7670753dadd0bd24e4e573f5352bde94a6c014a4`.
- Run: `python3 -B proof-independent-controls-v1.py proof-independent-controls-v1.json --survivor-pcompletion` (Python 3.14.3, numpy 2.4.3; 427 s main, 1408 s survivor step; started `2026-10-28T20:18:50-0700 PDT`). No author code imported or executed.

### 4.1 Unitary support patterns (rows/columns degree ≥2, no unique row or column overlap)
`n=6, 13 entries: 0`; `n=6, 14: 0`; `n=7, 15: 0`; `n=8, 16: 105`, all unions of four 2×2 blocks; positive controls `n=3, 8: 3`; `n=5, 12: 40` (30 of shape 3×3₈+2×2, 10 with rectangular 2×3/3×2 components); `n=7, 16: 525` (315 of shape 3×3₈+2×2+2×2, 210 with rectangular components). Rectangular components cannot carry a unitary, consistent with the source's own correction note; this control did not apply the square-component filter.

### 4.2 F₂ parity lemmas over all permitted graphs
90 two-regular 4×4 graphs; 36 labelled (2,3,3) 4×3 graphs. R44: zero-parity masks `{2: 216, 4: 108}`, violations 0. R34: `{2: 216}`, violations 0. 3/3: `same_dup_F2: 216`, `diff_dup_F4: 216`, violations 0. (Author receipt values 216/108, 72, 24/24 agree after dividing by the 3 and 9 low-symbol labellings my enumeration keeps.)

### 4.3 Exhaustive residual supports for `t = 28`
All 16-point sets in `[6]^4` whose six pair projections have 8 values of multiplicity exactly 2, generated in lexicographic order with restricted-growth labels (at least one representative per labelling class; 1,456,791 nodes, 49 s): **4374** labelled supports; maximal residual alphabet **4** (allowing 6); by sorted sizes `(2,4,4,4) 1751`, `(3,3,3,3) 296`, `(3,3,3,4) 1290`, `(3,3,4,4) 162`, `(3,4,4,4) 800`, `(4,4,4,4) 75` — exactly the six patterns of §3.2.
No-unique-overlap filter (necessary for unitarity, all three cuts): survivors 2682 = `(2,4,4,4) 1751`, `(3,3,3,3) 56`, `(3,4,4,4) 800`, `(4,4,4,4) 75`; removed all 1290 `(3,3,3,4)`, all 162 `(3,3,4,4)`, 240 `(3,3,3,3)`.
`(3,3,4,4)`: 162/162 have a unique row overlap in the cut (size-4,size-4)|(size-3,size-3). Example (coordinates 0,1 of size 4; 2,3 of size 3): `E = {0000,0001,0110,0111,1010,1011,1120,1121,2200,2220,2302,2322,3202,3222,3301,3321}`; rows `(0,0)` → columns `{(0,0),(0,1)}` and `(2,2)` → `{(0,0),(2,0)}` meet only in `(0,0)`.
Structure on the 2626 survivors with a size-4 coordinate: balanced-fiber failures 0; non-full/non-correlated tables 0; fibers with two correlations 0; R44 failures 0 over 1353 nonempty-F 4/4 pairs. Routes: some pair all-correlated (§3 route) `(2,4,4,4) 1421`, `(3,4,4,4) 96`, `(4,4,4,4) 9`; all pairs have a full fiber (§5/6 route) `330 / 704 / 66`; in every §5/6-route support the C and D graphs split with one common partition and each group has exactly **2** B values. The size-3 coordinate of every `(3,4,4,4)` survivor has A-degree pattern **(2,2,4)** (800/800), outside R34's (2,3,3) hypothesis — see M1.
Exact 28-word completion search (support only, no unitarity, MRV backtracking, uncapped): `(3,3,3,4)`: 0 of 1290 (max 5806 nodes); `(3,3,3,3)`: 0 of 296 (max 730). Bounded survivor search (cap 20,000 nodes each): `(3,4,4,4)` 0 of 800 (max 31 nodes, all exhausted); `(4,4,4,4)` 0 of 75 (max 9, exhausted); `(3,3,3,3)` 0 of 56 (exhausted); `(2,4,4,4)` 0 found, 838 exhausted, **913 capped (inconclusive)**.

### 4.4 Shadow-bound sharpness and identity
Three-qubit marginal of a five-qubit-code logical state (my own stabilizer construction): eigenvalues `(0,0,0,0,¼,¼,¼,¼)`, rank 4, all two-qubit marginals `I/4`, and `Y^{⊗3} ρ̄ Y^{⊗3} = I/4 − ρ` holds to 1e-10. Also checked inline: `f(r) = −1/r̄` is an involution with no fixed point on random nonzero complex r; the hypothetical AME(4,2) value `Tr(ρρ̃) = −1/2`.

### 4.5 No-OLS(6) import reproduced
`proof-ols6-control-v1.py` searches `OA(n²,4,n,2)` by the same MRV routine with two standard reductions (first row `(0,b,b,b)`, first column `c = a`): orders 3,4,5,7 found (witnesses verified pair-injective; 7, 13, 52, 758,951 nodes); **order 6: none, exhaustive, 1,580,005 nodes, 55.6 s, uncapped**. This validates the completion routine and reproduces Tarry's theorem inside this harness; it does not replace the classical proof as the candidate's named import.

## 5. Counterexample attempts (all failed to break the candidate)

1. Tried to realise an alphabet pattern outside the six listed (e.g. `(2,2,4,4)`, `(2,3,4,4)`, a size-5 alphabet): the exhaustive search with 6 symbols produced none; the incidence bound `r ≤ 4` and the product bounds are confirmed.
2. Tried to find a 4-point balanced fiber with two correlations or a non-full/non-correlated 2×2 table: none in 2626 survivors.
3. Tried to break R44 with an 8-cycle paired with a two-`K_{2,2}` graph and `|F| = 4`: rank inequality excludes it; enumeration found 0 violations over 90×90 graphs × 15 masks.
4. Tried to break R34 via a (2,2,4) size-3 graph (row sets `{L,L,L',L'}`-type with a triple-repeated symbol): such graphs are outside the lemma's hypothesis, and they occur only in `(3,4,4,4)` where the candidate does not apply R34; in `(3,3,4,4)` the second ternary coordinate forces (2,3,3) (all 162 supports: fiber sizes (4,6,6)).
5. Tried the `P_C = P_B^c` parity configuration as a would-be support counterexample: it is parity-consistent (multiplicities all 2), so I checked the one-overlap step explicitly; every one of the 162 supports has the predicted row overlap.
6. Tried to find a 28-word maximal completion for a `(3,3,3,x)` support to defeat the counting: none exists (exact search).
7. Tried a group with ≥4 B values to defeat the shadow bound in the §5/6 route: every group has exactly 2.

## 6. Findings

- **MINOR M1 (clarity, no logical gap).** R34 is stated for "a 3/4 pair" with the hypothesis "size-3 graph with degrees (2,3,3)". The hypothesis is only established in §7 (two ternary coordinates) and in fact fails in every `(3,4,4,4)` support (degree pattern (2,2,4)). §6 correctly uses only R44 for `(3,4,4,4)`; a one-line remark in §6 that R34 is inapplicable there would prevent misuse. Evidence: §4.3 (`size3_degree_patterns`).
- **MINOR M2 (presentation).** §4 cites the `{H,H,L_1,L_2}` row-set multiset before §7 derives it from the (4,6,6) fiber sizes; a forward reference should be stated. No mathematical effect.
- **Observation (not a defect).** Support-only maximal-word completion is already impossible for all `(3,4,4,4)` and `(4,4,4,4)` labelled supports (and 838 of 1751 `(2,4,4,4)`), which suggests those cases might admit a counting proof without unitarity; the 913 capped `(2,4,4,4)` cases leave unitarity (§3/§5) necessary as written. This is a possible simplification, not a requirement.
- No FATAL or MAJOR item. No step relies on author normal-form samples: every finite claim above was re-derived analytically and separately re-enumerated here.

## 7. Boundaries and limits

- **External import.** The candidate's only named mathematical import is the classical no-OLS(6) theorem (Tarry 1900), used in the ≥42 `t = 36` step, the ≥44 one-binary step, and the candidate's §3. This review did not read or verify the classical source; §4.5 is an in-harness exhaustive reproduction only.
- **Global bound.** As reconstructed, the statement is: every normalized complex AME(4,6) state, in every local product basis, has support ≥45. It combines the ≥42 packet (at most 30 maximal coefficients, `N ≥ 72 − t`), the ≥44 exclusion of `N ∈ {42,43}`, and this candidate's exclusion of `N = 44`. The argument is basis-agnostic because it uses only that every 2|2 flattening of ψ is `(1/6)×` unitary in the chosen product basis.
- **Stronger-proof limits.** `N = 45` is not excluded: `t ≥ 27` and the pinned lemmas leave exactly `(t,n,|E|) = (30,6,15)` (`2n+3`) and `(29,7,16)` (`2n+2` with n odd, allowed shape 3×3₈ ⊕ 2×2 ⊕ 2×2) as live cases [INFERENCE from the pinned lemmas; not claimed by the candidate]. The gap 45 ≤ m ≤ 60 to the cited 60-term witness remains open; the witness and the cited 38 bound were not accessed or verified here.
- **Novelty/priority.** Not audited; no external source (including arXiv:2610.16673) was accessed. The comparison with the cited 38 is the author's statement only.
- **Verification class.** Same-harness, single-reviewer, written plus exact finite controls; not human, formal/kernel, cross-vendor, or independent-family verification. Finite controls cover supports and parity exhaustively but cannot replace the unitarity steps (§3 involution, §5 shadow bound), which were verified analytically.
- **Artifacts.** Only `proof-*` files were created in this review directory; nothing in the evidence tree was modified.
