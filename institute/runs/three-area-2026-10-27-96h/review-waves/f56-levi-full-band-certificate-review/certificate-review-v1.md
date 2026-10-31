# f56 — Independent same-harness code/certificate soundness review of the registered A(r,s) level-four full-band candidate

Reviewer: review wave `f56-levi-full-band-certificate-review` (same harness as the author; **not** blind, human, cross-vendor, Lean or novelty verification). Observed `/bin/date` before this write: **2026-10-28T18:37:38-0700 PDT**. First clock of this review: 17:47:45 PDT (manifest `observed_clock_before_creation` 17:47:03). Authority and scope: `manifest-v1.json` in this directory. All work was written only under this directory; nothing under the evidence root was executed in place, written, or deleted by me.

## 0. Verdict at the exact scope

**FATAL: 0. MAJOR: 0. MINOR: 7 (interface/documentation/coverage items, none mathematical).**

Independent reconstruction result: every one of the 64 critical-degree classes and every one of the 192 rectangle classes was rebuilt from the printed definitions by separately written review-side programs (no author module imported) and bound exactly to the author's certificate data (complement words, kernel coefficient vectors, pivot rows, full symbolic determinant polynomials, statuses). All 244 + 516 grid determinants and all 144 one-sign/nonzero/degree-bounded polynomials were re-derived symbolically and agree coefficient-by-coefficient. Thirteen original three-generator cases (including seven at (3,3,4), never cross-checked by the author) agree with the eight-letter model and have zero simultaneous kernel. Eleven + five intended-reason corruptions were all rejected for their intended reasons.

What this does **not** establish: the representation-theoretic reductions (level-one adjoint identification, free-Levi semidirect source theorem, Levi-weight finite-critical-set reduction, first-defect induction, chain theorem) are *written* arguments; I audited them by reading and by hand-checking every displayed identity (Section 4), and a passing program is not a proof of them. The named classical imports (PBW/free positive source, Serre/simplicity of sl3) and the two parent dispositions remain imports. No claim about the printed arbitrary-GCM Conjecture 1, other levels, novelty, or Lean/kernel status follows from this review.

## 1. Input binding and coverage

All nine manifest sources were hash-verified before reading (SHA-256, byte and LF counts identical to the manifest) and read **completely** with `:raw` selectors:

| # | file | SHA-256 (prefix) | LF | read |
|---|---|---|---:|---|
| 1 | written-releases/math-3-positive-freeness-pbw-transcription-addendum-v1.json | 21b5b074 | 12 | 1–12 |
| 2 | written-releases/math-3-serre-family-packet-v1.md | 8b811cbc | 100 | 1–100 (truncated lines 14, 20, 73 re-read raw) |
| 3 | dispositions/math-3-full-cartan-radical-serre-containment-and-first-defect-parent-v1.md | 08217c89 | 34 | 1–34 |
| 4 | dispositions/math-3-preliminary-free-lie-and-serre-transport-parent-v1.md | f08daf3e | 26 | 1–26 |
| 5 | kac-moody/frontier-20261028-fixed-levi-level1-independent-v1.md | a001ed19 | 136 | 1–136 |
| 6 | kac-moody/frontier-20261028-Levi-free-quotient-critical-reduction-v1.md | e5ca9ebf | 144 | 1–144 |
| 7 | kac-moody/frontier-20261028-two-horizontal-chain-theorem-v1.md | d3cf1666 | 193 | 1–193 |
| 8 | kac-moody/frontier-20261028-level4-rectangle-certificate-v1.md | 887573ec | 156 | 1–156 |
| 9 | kac-moody/frontier-20261028-registered-level4-full-band-candidate-v1.md | bf7b47ce | 154 | 1–154 |

Operative code read completely before any execution (all hashes equal those printed in the manuscripts): `levi-lie-engine.py` af6669d7 (187 LF), `levi-critical-minors.py` 524da22e (92), `levi-critical-alternates.py` 3d2e9d88 (63), `levi-critical-independent-replay.py` 4b79f8cb (263 LF/10354 B), `214-independent-replay.py` 02e8e0c0 (267), `lift-exact.py` 3511d07f (358), `levi-level1-check.py` 531d835c (99), `symbolic-minors.py` 91540e42 (159), `horizontal-kernel-minors.py` 38c56505 (113), `224-alternate-minors.py` 405b3cc8 (84), `horizontal-independent-replay.py` ab2643d4 (125), `central-predecessor-replay.py` d8d42aa1 (47), `predecessor-certificates.py` 9669154f (41), `predecessor-independent-replay.py` 5b372109 (36), `chain-check.py` dbcf8bd3 (114), `original-Levi-48-check.py` 6372b14c (38), `original-Levi-crosscheck.py` 2b6e14cf (46). Certificate/result JSONs (all 30 `frontier-20261028-*.json`, hashes in my shell log, e.g. critical minors 2c8796b6, alternates 232fe13a, replay output af07046b 517 LF/13344 B, 214 minors 15ee2351, predecessor certs 39742fa1, 224 minors 08725d2f, 224 alternates 46b037e9, 221/222/223 aa9f38f9/94e2bac3/a4c58943, 48-check f028e22d, crosscheck 603645a7, lift-114 6d228bf0, chain results 6277cfd2, level1 results a526e5b0) were inspected through structured queries and then consumed in full by my verifiers. Files under the evidence root outside the manifest (in particular new author `level5-*`/`level6-*` files that appeared during this review) were **not opened**.

Book problem vs registered family: the packet (source 2, S2|70) fixes the registered scope — A(r,s)=[[2,−1,−1],[−1,2,−1],[−r,−s,2]], full Cartan realization, J vs τ at all positive degrees with α₃≤4, all r,s≥1 — which is a family/level subproblem of the printed Conjecture 1 (S2|37–38). Every statement below is at that registered scope only.

## 2. Dependency and helper trace (what actually executes)

Import graph, traced from the source text (all `importlib.util.spec_from_file_location` on sibling files; Python standard library only — `fractions`, `itertools`, `json`, `collections`, `functools`, `random`, `argparse`, `pathlib`; no sympy/numpy):

- **Critical producer**: `levi-critical-minors.py` → `levi-lie-engine.py` (→ `lift-exact.py` for `Span`, `lyndon_bracket`, `is_lyndon`, `letter`, `bracket`, `fits`, `rank`, `kernel_with_coefficients`, `combine`; → `levi-level1-check.py` for matrix-unit `unit/add/bracket`) and → `symbolic-minors.py` (→ `lift-exact.py`) for `diff`/`determinant` (subset-DP permutation expansion, sign by inversion parity — correct). Output `levi-critical-minors-v1.json`.
- **Alternates**: `levi-critical-alternates.py` → `levi-critical-minors.py` (hence the whole producer stack); seeded `random.Random(1030+j)` row-order shuffles; output `levi-critical-alternates-v1.json` (3 cases, attempts 1/1/2).
- **Critical replay**: `levi-critical-independent-replay.py` → **only** `214-independent-replay.py` (`ReducedSpace` Gauss–Jordan, `bracket`, `e`, `nested`, `standard_bracket`, `lyndon`, `add_scaled`, `determinant`, `eval_polynomial`). It does not import the Levi engine (claim in source 9 §6 verified). It re-types the matrix-unit `BASIS`, `WEIGHTS`, the local f3 table and the h3 scalar from the manuscripts — shared *mathematical inputs* with the producer, not independently derived in code (closed by my Section B below).
- **Cross-model checks**: `original-Levi-48-check.py` → `levi-lie-engine.py`, reads `lift-{114,224,324}-rs1to4.json` (made by `lift-exact.py`); `original-Levi-crosscheck.py` → `lift-exact.py` + `levi-lie-engine.py` (4 cases).
- **Rectangle**: producers `symbolic-minors.py`, `horizontal-kernel-minors.py` (→ `symbolic-minors.py`), `224-alternate-minors.py` (→ `horizontal-kernel-minors.py`), `predecessor-certificates.py` (→ `symbolic-minors.py`), all on `lift-exact.py`; replays `214-independent-replay.py` (standalone), `horizontal-independent-replay.py` (→ 214 replay), `central-predecessor-replay.py` (→ horizontal replay), `predecessor-independent-replay.py` (→ 214 replay). Two linear-algebra/bracket stacks therefore exist in the union: `lift-exact.py` (producers, triangular least-word echelon) and `214-independent-replay.py` (replays, Gauss–Jordan least-word). Everything else is a thin driver.

Mathematical-to-code caller: source 6 (3.1)–(4.3) ↔ `levi-lie-engine.py` `seed()`, `local_f3()`, `action_letter('h3')`, `WEIGHTS`, `BASIS`; source 8 (2.2) ↔ `lift.lowering` / `ind.lower` (right-Cartan tail asserted to cancel on every input); source 9 §5 class rule ↔ `r0=4 if rc=='>=4'`, `dr`/`ds` first differences at r0+1/s0+1. All exclusive-create guards (`dest.exists()`→error, `open(...,'x')`, `FileExistsError`) are present in every writer.

## 3. Code audit of the producer/replay pipeline (findings with lines)

Correct as implemented (checked by reading and by independent reconstruction):

- **Full ideal spans.** The P-ideal generated by ρ₃₁=−(ad m₀)^r m₁ at (1,0,r+1) and ρ₃₂=−(ad m₀)^s m₂ at (0,1,s+1) is closed under ad e₁, ad e₂ (Levi derivations) and left bracket with every letter m₀…m₇ (`ideal_bases`, engine L116–136). Since P=l₊⋉F(M) is generated by e₁,e₂,M and ad[a,b]=[ad a,ad b], this is the full ideal; the `fits(bound)` pruning is safe because all generators have nonnegative degree. Target ideals are the full direct sum at α−ε_i (`target_ideal`, L139–147).
- **Quotient basis.** Complement = Lyndon brackets independent modulo the ideal (`case()`, producer L30–35); my reconstruction verified each certificate complement word is Lyndon, of the right degree, independent modulo my own ideal, and that complement+ideal spans my own free source (Lyndon count = right-nested rank at every degree).
- **Horizontal kernel.** `kernel_with_coefficients` on the f1/f2 components of the T-reduced columns (producer L37–40) is the joint kernel on the quotient; my own nullspace agrees as a subspace in all 40 nonzero classes.
- **f3 matrix.** Producer: tensor-suffix formula with asserted zero degree-zero tail (engine L80–97); replay: Lyndon-tree Jacobi (L105–118); mine: right-nested recursion. Three different algorithms agree. Affineness in r and s and absence of an r·s term were checked by second differences (my verifier), not assumed.
- **Zero classes.** ZERO_SOURCE (3,2,4)(1,1): free 36 = ideal 36 in my model, and free 140 = ideal 140 in the original model. ZERO_HORIZONTAL (3,3,3)×16 and (4,4,4)×7: horizontal rank = m in my model; (3,3,3) also in the original model at (1,1),(2,3),(4,4).
- **Pivot selection.** Pivot words are the leading words of an echelon of the base f3 columns (producer L44–48); the corresponding minor is therefore nonsingular at the baseline, which the asserted nonzero constant records. Statuses: `CERTIFIED_ONE_SIGN` iff all nonzero coefficients share one sign.
- **Alternate minors.** Exactly the three producer `MIXED_SIGNS_NEEDS_ANALYSIS` classes ((3,2,4)(≥4,3), (3,2,4)(≥4,≥4), (4,4,4)(≥4,≥4)) are replaced; the alternates keep `source_dim`, `horizontal_kernel_dim`, `source_words`, `horizontal_kernel_coefficients` byte-identical and change only pivots/polynomial/status; I re-derived the producer's *original* mixed polynomials from their recorded pivots (they are genuinely mixed) and the alternates' polynomials from the alternate pivots (one-signed). Same for the two (2,2,4) replacements.
- **Degree bounds / grid.** k×k matrix affine in (x,y) ⇒ degree ≤k per variable and total; the (k+1)×(k+1) grid identity is a valid binding; the critical replay additionally asserts `x_power<=k and y_power<=k` (L225). One-signed coefficients plus nonzero constant ⇒ nonzero for all x,y≥0.
- **16 classes.** For n≤4 the node-3 seed of exponent r+1 fits iff r≤3; r≥4 classes have literally identical ideal spans — I verified span equality (dimension and mutual containment at every degree ≤α) at r₀+1, r₀+5 (and s, and (+3,+3)) in all 28 classes with a `>=4` component, and in the original model at (3,3,4) for (5,5) vs (4,4).

MINOR findings (none affects the mathematics):

- **M1 — undocumented normal-form convention binding the certificates.** "Target word pivots" and the determinant polynomials are coordinates of the quotient F/T in the reduced normal form whose leading terms are the lexicographically *least* words of T (letter order 0<…<7, resp. 1<2<3). Neither the JSONs nor the manuscripts state this; a replay with another canonical complement produces different pivot sets/polynomials. Evidence: my first verifier run used max-word pivots and failed to bind at (3,2,4)(1,3), pivot `116` ("pivot row absent from f3 image"); after switching to the least-word form every binding succeeded. Injectivity is convention-free; only the *replayability* of the printed rows depends on it. Suggest one sentence in the certificate format.
- **M2 — producer record format inconsistency.** All 32 `ZERO_HORIZONTAL_KERNEL` records of `221`/`222` omit `source_basis_lyndon_words` (the Levi producer includes `source_words` in the same situation). The author disclosed the resulting `KeyError` and repaired only the replay driver (`central-predecessor-replay.py` L19–27). My rectangle verifier builds its own complement for those records (k=0 is complement-independent).
- **M3 — rectangle replays do not enforce the printed polynomial's degree.** `214-independent-replay.py` (L225–231) and `horizontal-independent-replay.py` (L88–92) check nonzero constant, one sign and the grid, but never assert per-variable degree ≤ matrix size (the critical replay does, L225). A tampered higher-degree term would pass their grid. This confirms the F55 hazard for the 192 rectangle classes; it is closed here by exact symbolic reconstruction of all 256 polynomials (max per-variable and total degree ≤ size in every class; equality to the certificate coefficient-by-coefficient).
- **M4 — set/routing invariants are counted, not enforced, by the replays.** Critical replay: `assert len(alt)==3` (L243), `assert len(cases)==16` (L248); no assertion that the degree blocks are exactly {(3,2,4),(3,3,3),(3,3,4),(4,4,4)} or that the 16 classes are the full {1,2,3,≥4}² product; `central-predecessor-replay.py` L17 even consumes the producer's `all_classes_covered` flag as a precondition. Closed by my exact-set enforcement (`enforce_sets` and the rectangle driver) and by a metadata scan recomputing 172/187/110/47/244 determinant counts from grid sizes.
- **M5 — cross-model corroboration gap.** The union's original-vs-Levi comparisons cover (1,1,4),(2,2,4),(3,2,4) for r,s∈{1..4} and (3,3,3) once; **(3,3,4) and (4,4,4) were never compared with the original three-generator algebra.** I added (3,3,4) at seven parameter pairs (all agree). (4,4,4) still has no original-model cross-check (free dimension 2880 at total degree 12 exceeds a bounded one-worker exact run); its validity rests on the written free-Levi theorem plus my independent eight-letter reconstruction. Named trust limit.
- **M6 — unverifiable or imprecise prose.** Source 9 §6 "reported wall time 17.67 seconds" is not recorded in any artifact (my relocated re-run: 18.3 s, consistent). Source 9 §6 describes the replay's import as "my independently written generic sparse-elimination/determinant helper": accurate, but that helper is also the engine of all rectangle replays, and the replay re-types the model inputs (basis, local f3 table, h3 scalar) rather than deriving them. Source 6 engine docstring/`caution` string reads "kernel zero does imply original LIFT" — consistent with §6 of source 6 but easy to misread.
- **M7 — process observation (not a defect of the candidate).** During this review the evidence root gained many new author files (`frontier-20261028-level5-*`, `level6-*`, `invariant5-*`, `frontier-review-f50-ph7-algebraic-endpoint-v4-v1.md`) and `__pycache__/frontier-20261028-levi-critical-independent-replay.cpython-314.pyc` was refreshed by a process other than mine (consistent with the parent's announced in-place shared-engine replay). All 24 pinned source/code/certificate files re-hashed identical at 18:36:28 PDT.

## 4. Written-mathematics audit (hand checks performed)

Read in full; every displayed identity below was recomputed by hand and, where marked, also by my Section A/B code.

- **Level one (source 5).** Operator identity x²y²=y²x²+4zxy−2z² (derived from yx=xy−z, z central); consequences z²v=2zxyv, x²yv=2zxv, z²xv=0 (factor 3), z²yv=0 (factor 3), z³v=0; the eight normal words (3.2) and the reduction of every x^a z^b y^c v to them; matrix-unit images (4.1) [code A], rank 8 [code A], weights (4.3) [code A]; ψ intertwines f₁,f₂,h₁,h₂ by word-length induction using [f_i,e_j]=−δ_ij h_i and h_i e_j=e_j h_i+a_ij e_j in both algebras (rows 1–2 of A(r,s) restricted to columns 1–2 equal the A2 matrix) — sound; kernel is an ideal of simple sl3, v≠0 since otherwise h₃∈K∩h=0; (5.1)–(5.3): 2A_p−B_p=c_p1, −A_p+2B_p=c_p2, λ_p=c_p3+c_p1+c_p2, and (5.3) reproduces the root pairing (c_p1 a+c_p2 b+c_p3) on all eight vectors [code A]; §6 T₁→S₁ iso (node-3 seeds have level ≥2) and D∩level-one is an sl3-submodule of the adjoint, excluded because f₃e₃=−h₃∉D. Sound.
- **Free-Levi source (source 6).** K=K₊⊕K₋ by the subset specialization of the adopted action lemma; both universal maps n₊(T)→P and P→n₊(T) (the latter via l₊↪n₊(T), free-Lie extension of M↪n₊(T), and the "derivation along a homomorphism" argument for compatibility of [g,·]); compositions fix generators; J₊/K₊ = P-ideal of ρ₃₁,ρ₃₂ with (3.1) sign/exponent bookkeeping; S_n≅F_n(M)/I_n for n≥1; local table (4.2): [f₃,m₁]=[e₁,−h₃]=−r e₁, [f₃,m₃]=−(r+s)[e₁,e₂], [f₃,m₄]=[e₁,−s e₂], [f₃,m₅]=r(ad e₁)²e₂∈K, [f₃,m₆]=s(ad e₂)²e₁∈K, [f₃,m₇]=0 [all re-derived in the original algebra by tree Leibniz, code B]; (4.3) h₃ scalar = a₃₁a+a₃₂b+a₃₃ [code B]; the lift D₃: F(M)→(l₊⊕Ch₃)⋉F(M) is a derivation along π agreeing with ad f₃ on M, hence D₃(I_n)⊂I_{n−1} — this is the mathematical reason the "ideal derivative escaped target" assertions must pass; §5 sl2 identity f e^{N+1}x=−(N+1)(μ+N)e^N x gives μ=−N≤0, weights (5.1), inequalities (5.2), and the sets of sizes 2/5/8/13 with outside-rectangle residue {(3,3)} at n=3 and {(2,3),(3,2),(3,3),(4,4)} at n=4 [code D]. Sound.
- **Chain theorem (source 7).** (4.1) by induction ([f₃,X_{k+1}]=(k+1)(r−k)X_k), (4.2), (4.3) ([f₁,V₀]=(n+1)Y_n, [f₁,V₁]=−Y_n); ideal spans (3.2)/(3.3) by descendant bookkeeping; Cases I–III coefficient recursions and positivity of every divisor used (a(r−a+1), (n−b)(s−n+b+1), n(s−n+1)+(n+1)r, (j+1)(r−j)); §6 boundary degrees and least-height induction. Sound.
- **Rectangle (source 8).** Lowering formula (2.2) and right-Cartan cancellation; class constancy; full-column vs horizontal-kernel/f₃ methods; §6 predecessor list and the node-swap mirror (C→C′ realization of A(s,r), fixes node 3 and all extra Cartan labels); level-zero positive Levi spanned by e₁,e₂,[e₁,e₂]. §4/§5 tables transcribe the certificate bytes exactly (checked).
- **Full-band union (source 9).** Chronology of writes/post-run clocks (17:07:21 chain → 17:17:18 rectangle → 17:27:17 level one (checker 17:26:45) → 17:34:40 free-Levi → replay post-run 17:40:08 → 48-check 17:42:48 → 17:43:10 union) is consistent; every cited hash is live-identical; §5 table (classes/zero/max k/determinants 92,0,136,16) equals my own grid counts; first-defect step: least total height in the downward-closed band, lowerings land in lower band degrees, root-zero defect 0, or mixed-sign zero spaces; level-zero base: a root-graded ideal of sl3⊕(extra Cartan) with zero Cartan part is zero. Sound at the stated conditional scope.

Open mathematical trust limits (not defects): PBW/free positive source (named import, normalized transcription per source 1); Serre presentation/simplicity of sl3 (named); parent dispositions 3–4 (same-harness written support); same-harness, non-blind review; no Lean/kernel; no novelty assessment.

## 5. Independent reconstruction actually run (review-side programs, no author imports)

Programs (final hashes): `f56-independent-verifier.py` SHA-256 `51922e48e0f2b8fa78eea63f5865f78b89b53b22fd122afbad4c1e41bda961e7` (973 LF); `f56-rectangle-independent-verifier.py` `a9a63f87fbd4a3e5391674f52c0f9ce2f9fba624ece5aaef010dda7823a976da`; `f56-original-model-crosscheck.py` `bcc49981636ad47ea81351fb8ba3eb9913ff9e8e52811371255a2df699965dda`. Python 3.14.3 (`/opt/homebrew/opt/python@3.14/bin/python3.14`), standard library only, exact `fractions.Fraction`; one process at a time.

What each program **rebuilds from scratch** vs **takes from the certificate** (then compares):

| datum | rebuilt by me | from certificate | binding check |
|---|---|---|---|
| sl3 matrix-unit model, 8 vectors, relations, weights, (5.1)–(5.3) | yes (3×3 matrices) | — | equality with (4.1)/(4.3) |
| local f₁/f₂/f₃/e₁/e₂/e₁₂/h₃ actions on m₀…m₇ | yes, in the **original** algebra by tree Leibniz, compared modulo my own K-ideal | — | equality with the matrix-unit coordinates |
| level-one dimension table of F/K, a,b≤4, r,s∈{(1,1),(2,3),(4,4),(3,7)} | yes | — | equals (4.3), zero elsewhere |
| free source at each critical degree (Lyndon basis; right-nested spanning rank) | yes | — | counts equal |
| full node-3 ideal and 3 target ideals; class constancy at r₀+1,r₀+5,(+3,+3) | yes (own Gauss–Jordan closure) | — | dims and spans |
| quotient source dim m; complement validity | yes | complement words | words Lyndon, independent mod my ideal, span my source |
| joint horizontal kernel (own nullspace) and k | yes | kernel coefficient vectors | same subspace |
| f₃ columns via right-nested recursion; affineness/second differences; no r·s term | yes | — | asserted |
| symbolic k×k determinant in Q[x,y] (own expansion) | yes | pivot rows, polynomial | coefficient-by-coefficient equality; degree ≤k (x, y, total); nonzero constant; one sign |
| numeric grid {0..k}² determinants | yes | — | equal to own polynomial |
| direct simultaneous quotient-kernel rank at up to 6 sample points per class | yes | — | all 0 (131 points critical, 131 rectangle; 165 full-rank points) |
| original mixed producer minors | re-derived from recorded pivots | — | confirmed mixed; alternate pivots differ |
| degree blocks, class product, replacement keys, statuses | — | — | enforced exactly |

**Run log (actual commands, exits, clocks).**

1. `python3 f56-independent-verifier.py` — 18:07:53→18:10:25 PDT, exit 0, internal 98.5 s (`real 1m38.7s`). Output `f56-independent-verifier-result-v1.json` SHA-256 `477508c2…` (produced by the pre-control-hook version of the script; identical mathematics). Final pinned re-run `python3 f56-independent-verifier.py --output f56-independent-verifier-result-v2.json` — 18:33:53→18:35:36, exit 0, 102.95 s; `f56-independent-verifier-result-v2.json` SHA-256 `03e2fc00796187a65f00add18a52c99a67b480e62623ba7944a61e042248416e`; v1 == v2 apart from `elapsed_seconds`. Totals: 64 classes = 1 zero-source + 23 zero-horizontal + 40 certified; grid points 92/0/136/16 = 244.
2. `python3 f56-rectangle-independent-verifier.py` — 18:22:08→18:22:27, exit 0, 19.3 s; `f56-rectangle-independent-verifier-result-v1.json` SHA-256 `cdcc274cb5e39bfb1c0a096cd7fc7a441131f301598b5188b06cadf7d0deda0d`. Totals: 192 classes = 56 zero-source + 32 zero-horizontal + 104 certified; grid points 172+187+110+47 = 516. (A first attempt at 18:21:44 stopped with `KeyError: 'source_basis_lyndon_words'` on the (2,2,1) producer records — finding M2 — and the verifier was given an own-complement path before the successful run.)
3. `python3 f56-original-model-crosscheck.py` — 18:22:37→18:33:15, exit 0, `real 10m37.8s` (`user 28m14s`, interpreter-internal threading; single process); `f56-original-model-crosscheck-result-v1.json` SHA-256 `60ec9a313c5a520311168ec1a0666f0d51e58c1d7f0668a0c09b6fcd99ab1624`.
4. Controls, Levi verifier, `--only 3,2,4` (18:11:45→18:21:27): all exit 1 for the intended reason —
   `local_m4_r` (−r instead of −s in [f₃,m₄]) → `ideal derivative escaped target ideal` at (1,2); `h3_const` (2→1) → same; `drop_rho32` → `source dim` 0≠12 at (1,1); `swap_f1_f2` → `f action mismatch` already in Section B; `no_letter_closure` → `source dim` 0≠36; `cert_words` → `certificate vector not in horizontal kernel`; `cert_kernel` → same; `cert_pivot` → `determinant polynomial mismatch` at (1,3) (−39/2 vs −15/2; the (1,2) swap happened to give an equal 2×2 value, so detection came one class later); `cert_sign` → polynomial mismatch at (1,≥4) (sign of y²); `use_original_mixed` → refused (`MIXED_SIGNS_CONFIRMED_NOT_A_CERTIFICATE` is not accepted as coverage) after 14 classes; `weights_m7` → degree assertion before any class.
5. Controls, rectangle verifier (18:33:34→18:33:46): `cert_sign` (2,1,4) → polynomial mismatch at (2,≥4); `cert_pivot` (2,1,4) → mismatch at (1,3); `cert_words` (2,2,4) → `complement word dependent modulo ideal`; `cert_kernel` (2,2,4) → `certificate kernel is not the own kernel`; `use_original_mixed` (2,2,4) → refused after 14 classes.
6. Relocated copy of the **author's** replay (`f56-relocated-author-replay/`, copies of 4b79f8cb, 02e8e0c0, 2c8796b6, 232fe13a; `cp -n`): 18:35:50→18:36:08, exit 0, `real 18.3s`, printed `PASS all64 classes, 244 determinants`; regenerated output byte-identical to the pinned `af07046b…` (`cmp` clean). This shows determinism/immutability of the author's replay, not independence.
7. Metadata scan (no reconstruction) of all rectangle certificates: class order = full product in all 12 files; `224` mixed set = alternate set = {(≥4,3),(≥4,≥4)}; alternates keep producer data; all printed degrees ≤ size; replay JSON determinant counts equal grid-size sums (172/187/110/47; critical 244).

### 5.1 Critical degrees — own values per class (all equal the certificate; "(alt)" = alternate minor replaced the producer's mixed one)

|degree|r|s|free dim|ideal dim|m|k|own status|poly terms|const sign|deg x/y/total|grid|
|---|---|---|---:|---:|---:|---:|---|---:|---|---|---:|
|(3, 2, 4)|1|1|36|36|0|0|ZERO_SOURCE|0|||0|
|(3, 2, 4)|1|2|36|31|5|2|CERTIFIED_ONE_SIGN|1|+|0/0/0|1|
|(3, 2, 4)|1|3|36|26|10|2|CERTIFIED_ONE_SIGN|1|-|0/0/0|1|
|(3, 2, 4)|1|>=4|36|24|12|2|CERTIFIED_ONE_SIGN|3|+|0/2/2|3|
|(3, 2, 4)|2|1|36|29|7|3|CERTIFIED_ONE_SIGN|1|+|0/0/0|1|
|(3, 2, 4)|2|2|36|18|18|5|CERTIFIED_ONE_SIGN|1|-|0/0/0|1|
|(3, 2, 4)|2|3|36|13|23|5|CERTIFIED_ONE_SIGN|1|-|0/0/0|1|
|(3, 2, 4)|2|>=4|36|11|25|5|CERTIFIED_ONE_SIGN|6|+|0/5/5|6|
|(3, 2, 4)|3|1|36|21|15|4|CERTIFIED_ONE_SIGN|1|-|0/0/0|1|
|(3, 2, 4)|3|2|36|10|26|6|CERTIFIED_ONE_SIGN|1|+|0/0/0|1|
|(3, 2, 4)|3|3|36|5|31|6|CERTIFIED_ONE_SIGN|1|+|0/0/0|1|
|(3, 2, 4)|3|>=4|36|3|33|6|CERTIFIED_ONE_SIGN|7|+|0/6/6|7|
|(3, 2, 4)|>=4|1|36|18|18|4|CERTIFIED_ONE_SIGN|5|+|4/0/4|5|
|(3, 2, 4)|>=4|2|36|7|29|6|CERTIFIED_ONE_SIGN|6|+|5/0/5|7|
|(3, 2, 4)|>=4|3|36|2|34|6|CERTIFIED_ONE_SIGN (alt)|6|-|5/0/5|7|
|(3, 2, 4)|>=4|>=4|36|0|36|6|CERTIFIED_ONE_SIGN (alt)|26|+|5/5/6|49|
|(3, 3, 3)|1|1|18|16|2|0|ZERO_HORIZONTAL_KERNEL|0|||0|
|(3, 3, 3)|1|2|18|10|8|0|ZERO_HORIZONTAL_KERNEL|0|||0|
|(3, 3, 3)|1|3|18|8|10|0|ZERO_HORIZONTAL_KERNEL|0|||0|
|(3, 3, 3)|1|>=4|18|8|10|0|ZERO_HORIZONTAL_KERNEL|0|||0|
|(3, 3, 3)|2|1|18|10|8|0|ZERO_HORIZONTAL_KERNEL|0|||0|
|(3, 3, 3)|2|2|18|4|14|0|ZERO_HORIZONTAL_KERNEL|0|||0|
|(3, 3, 3)|2|3|18|2|16|0|ZERO_HORIZONTAL_KERNEL|0|||0|
|(3, 3, 3)|2|>=4|18|2|16|0|ZERO_HORIZONTAL_KERNEL|0|||0|
|(3, 3, 3)|3|1|18|8|10|0|ZERO_HORIZONTAL_KERNEL|0|||0|
|(3, 3, 3)|3|2|18|2|16|0|ZERO_HORIZONTAL_KERNEL|0|||0|
|(3, 3, 3)|3|3|18|0|18|0|ZERO_HORIZONTAL_KERNEL|0|||0|
|(3, 3, 3)|3|>=4|18|0|18|0|ZERO_HORIZONTAL_KERNEL|0|||0|
|(3, 3, 3)|>=4|1|18|8|10|0|ZERO_HORIZONTAL_KERNEL|0|||0|
|(3, 3, 3)|>=4|2|18|2|16|0|ZERO_HORIZONTAL_KERNEL|0|||0|
|(3, 3, 3)|>=4|3|18|0|18|0|ZERO_HORIZONTAL_KERNEL|0|||0|
|(3, 3, 3)|>=4|>=4|18|0|18|0|ZERO_HORIZONTAL_KERNEL|0|||0|
|(3, 3, 4)|1|1|65|64|1|1|CERTIFIED_ONE_SIGN|1|+|0/0/0|1|
|(3, 3, 4)|1|2|65|50|15|4|CERTIFIED_ONE_SIGN|1|+|0/0/0|1|
|(3, 3, 4)|1|3|65|40|25|4|CERTIFIED_ONE_SIGN|1|+|0/0/0|1|
|(3, 3, 4)|1|>=4|65|37|28|4|CERTIFIED_ONE_SIGN|5|-|0/4/4|5|
|(3, 3, 4)|2|1|65|50|15|4|CERTIFIED_ONE_SIGN|1|+|0/0/0|1|
|(3, 3, 4)|2|2|65|26|39|8|CERTIFIED_ONE_SIGN|1|-|0/0/0|1|
|(3, 3, 4)|2|3|65|16|49|8|CERTIFIED_ONE_SIGN|1|-|0/0/0|1|
|(3, 3, 4)|2|>=4|65|13|52|8|CERTIFIED_ONE_SIGN|9|-|0/8/8|9|
|(3, 3, 4)|3|1|65|40|25|4|CERTIFIED_ONE_SIGN|1|-|0/0/0|1|
|(3, 3, 4)|3|2|65|16|49|8|CERTIFIED_ONE_SIGN|1|-|0/0/0|1|
|(3, 3, 4)|3|3|65|6|59|8|CERTIFIED_ONE_SIGN|1|-|0/0/0|1|
|(3, 3, 4)|3|>=4|65|3|62|8|CERTIFIED_ONE_SIGN|9|+|0/8/8|9|
|(3, 3, 4)|>=4|1|65|37|28|4|CERTIFIED_ONE_SIGN|5|+|4/0/4|5|
|(3, 3, 4)|>=4|2|65|13|52|8|CERTIFIED_ONE_SIGN|9|-|8/0/8|9|
|(3, 3, 4)|>=4|3|65|3|62|8|CERTIFIED_ONE_SIGN|9|-|8/0/8|9|
|(3, 3, 4)|>=4|>=4|65|0|65|8|CERTIFIED_ONE_SIGN|45|-|8/8/8|81|
|(4, 4, 4)|1|1|84|82|2|0|ZERO_HORIZONTAL_KERNEL|0|||0|
|(4, 4, 4)|1|2|84|63|21|0|ZERO_HORIZONTAL_KERNEL|0|||0|
|(4, 4, 4)|1|3|84|51|33|0|ZERO_HORIZONTAL_KERNEL|0|||0|
|(4, 4, 4)|1|>=4|84|48|36|0|ZERO_HORIZONTAL_KERNEL|0|||0|
|(4, 4, 4)|2|1|84|63|21|0|ZERO_HORIZONTAL_KERNEL|0|||0|
|(4, 4, 4)|2|2|84|30|54|1|CERTIFIED_ONE_SIGN|1|-|0/0/0|1|
|(4, 4, 4)|2|3|84|18|66|1|CERTIFIED_ONE_SIGN|1|+|0/0/0|1|
|(4, 4, 4)|2|>=4|84|15|69|1|CERTIFIED_ONE_SIGN|1|+|0/0/0|2|
|(4, 4, 4)|3|1|84|51|33|0|ZERO_HORIZONTAL_KERNEL|0|||0|
|(4, 4, 4)|3|2|84|18|66|1|CERTIFIED_ONE_SIGN|1|+|0/0/0|1|
|(4, 4, 4)|3|3|84|6|78|1|CERTIFIED_ONE_SIGN|1|+|0/0/0|1|
|(4, 4, 4)|3|>=4|84|3|81|1|CERTIFIED_ONE_SIGN|2|-|0/1/1|2|
|(4, 4, 4)|>=4|1|84|48|36|0|ZERO_HORIZONTAL_KERNEL|0|||0|
|(4, 4, 4)|>=4|2|84|15|69|1|CERTIFIED_ONE_SIGN|2|+|1/0/1|2|
|(4, 4, 4)|>=4|3|84|3|81|1|CERTIFIED_ONE_SIGN|2|+|1/0/1|2|
|(4, 4, 4)|>=4|>=4|84|0|84|1|CERTIFIED_ONE_SIGN (alt)|2|-|0/1/1|4|

Replaced minors re-derived: (3,2,4)(≥4,3) producer pivots `017,035,045,053,071,125` mixed → alternate `503,116,215,313,350,125`, polynomial −22004736 −145167872/7·x −… −24576/7·x⁵ (all negative); (3,2,4)(≥4,≥4) producer pivots as above mixed → alternate `441,450,504,331,053,116`, 26 positive terms, constant 27993600, total degree 6; (4,4,4)(≥4,≥4) producer pivot `167` (9 + mixed x,y terms) → alternate `456`, polynomial −6−2y.

### 5.2 Rectangle — own block summary (all 192 classes bound; (2,2,4) alternates re-derived: (≥4,3) constant −210726912/343, 8 negative terms, degree 7; (≥4,≥4) constant 559971360/343, 36 positive terms, total degree 7)

|degree|mode|zero-source|zero-horizontal|certified|max m|max k|grid points|
|---|---|---:|---:|---:|---:|---:|---:|
|(2, 1, 4)|FULL|2|0|14|10|0|172|
|(2, 0, 1)|FULL|16|0|0|0|0|0|
|(2, 0, 2)|FULL|16|0|0|0|0|0|
|(2, 0, 3)|FULL|8|0|8|1|0|15|
|(2, 0, 4)|FULL|12|0|4|1|0|10|
|(2, 1, 1)|FULL|0|0|16|1|0|25|
|(2, 1, 2)|FULL|0|0|16|3|0|47|
|(2, 1, 3)|FULL|1|0|15|6|0|90|
|(2, 2, 1)|HORIZONTAL|0|16|0|1|0|0|
|(2, 2, 2)|HORIZONTAL|0|16|0|4|0|0|
|(2, 2, 3)|HORIZONTAL|0|0|16|13|3|47|
|(2, 2, 4)|HORIZONTAL|1|0|15|25|7|110|

### 5.3 Original three-generator cross-model check (own implementation; six seeds; tree-Leibniz lowerings)

|degree|r|s|free dim|ideal dim|m (own original)|m (Levi class)|T dim|rank|simultaneous kernel|joint horizontal kernel (own / Levi)|seconds|
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
|(3, 2, 4)|1|1|140|140|0|0|155|0|0|0 / 0|5.4|
|(3, 2, 4)|2|2|140|122|18|18|133|18|0|5 / 5|4.8|
|(3, 2, 4)|4|4|140|104|36|36|108|36|0|6 / 6|5.1|
|(3, 3, 3)|1|1|186|184|2|2|207|2|0|0 / 0|10.2|
|(3, 3, 3)|2|3|186|170|16|16|185|16|0|0 / 0|9.6|
|(3, 3, 3)|4|4|186|168|18|18|181|18|0|0 / 0|9.7|
|(3, 3, 4)|1|1|420|419|1|1|464|1|0|1 / 1|93.4|
|(3, 3, 4)|1|2|420|405|15|15|446|15|0|4 / 4|87.0|
|(3, 3, 4)|2|2|420|381|39|39|416|39|0|8 / 8|83.3|
|(3, 3, 4)|2|3|420|371|49|49|401|49|0|8 / 8|82.5|
|(3, 3, 4)|3|3|420|361|59|59|386|59|0|8 / 8|82.6|
|(3, 3, 4)|4|4|420|355|65|65|376|65|0|8 / 8|81.5|
|(3, 3, 4)|5|5|420|355|65|65|376|65|0|8 / 8|81.6|

These are finite sampled corroborations of the free-Levi identification (source 6 (0.1)/(3.2)) at the critical degrees, not a proof for unbounded parameters; (4,4,4) is not covered (M5).

## 6. Exact coverage statement and named trust limits

Covered independently: the entire computer-assisted part of the candidate — all 256 degree/class records, every full ideal span (critical: eight-letter model; rectangle: original model), quotient bases, horizontal kernels, f₃ matrices (three algorithms), zero classes, all five alternate substitutions, polynomial degree bounds (per variable and total), sign/constant certificates, class constancy, affineness, exact set/routing identities; the level-one model and the local bracket tables re-derived in the original algebra; the finite critical sets. Not covered by any program and resting on written argument plus named imports: the free-Levi semidirect isomorphism as an all-parameter theorem (sampled at 13 + the author's 52 cases), the Levi-weight reduction, the first-defect induction, the chain theorem's all-n quantifier (sampled by the author at 144 cases, not re-run by me), the parent dispositions and PBW. Not performed: Lean/kernel, human, cross-vendor or novelty verification; (4,4,4) original-model cross-check; any reading of files outside the manifest.

Conclusion for Main: at the exact registered scope the candidate's **code and certificates are sound** as far as an independent same-harness reconstruction can show (no FATAL/MAJOR), with seven MINOR interface/documentation/coverage items. Adoption of the registered A(r,s), α₃≤4 band remains a decision about the *written* reductions and the named imports; a passing program — mine or the author's — does not by itself prove the representation-theoretic steps or the registered band.

## 7. Artifacts and clocks

Directory: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f56-levi-full-band-certificate-review/` — this report `certificate-review-v1.md`; `f56-independent-verifier.py` (51922e48…), `f56-independent-verifier-result-v1.json` (477508c2…), `f56-independent-verifier-result-v2.json` (03e2fc00…), `f56-rectangle-independent-verifier.py` (a9a63f87…), `f56-rectangle-independent-verifier-result-v1.json` (cdcc274c…), `f56-original-model-crosscheck.py` (bcc49981…), `f56-original-model-crosscheck-result-v1.json` (60ec9a31…), `f56-relocated-author-replay/` (four `cp -n` copies, regenerated replay output af07046b…, `__pycache__`), plus the parent's own `parent-full-certificate-*` files (not mine; not read as evidence). Evidence root: untouched by me; all pinned bytes re-hashed identical at 18:36:28 PDT. No external model/paid API, author contact, Git action, deletion, secret access or infrastructure change occurred. Observed clock before this write: 2026-10-28T18:37:38-0700 PDT.
