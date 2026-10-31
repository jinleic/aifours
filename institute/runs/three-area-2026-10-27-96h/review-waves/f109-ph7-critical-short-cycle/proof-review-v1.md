# f109 proof review — PH7 critical-ratio short-cycle theorem (z = 8/9)

Native clock observed immediately before writing: **2026-10-28T19:39:16-0700 PDT** (`/bin/date`). Manifest `manifest-v1.json` SHA-256 `8f1fa208bdb84a0fbbb44c12c9a1ce22af20a9076ec5ec650babb09db0cb4f75` verified; all seven inputs read completely in manifest order and every full SHA-256 / byte count / LF count matched the manifest (`shasum -a 256`, `wc -c`, `grep -c ''`).

This is a same-harness mathematical/caller review. It is not a human, independent-family, formal/kernel, or novelty verification. The author's checker, certificate and replay were **read only**; nothing from them was imported or executed, and no evidence below derives from running them. No author contact, external model, paid API, held payload, deletion, Git, publication or infrastructure action occurred. The sibling `certificate-*` artifacts present in this directory were not opened.

## Verdict

| Object | Verdict | Condition |
|---|---|---|
| Spectral theorem (§1 general statement: no irreducible 7×7 Metzler, spectral bound 0, `D(y) | χ`, girth ≥ 5) | **MINOR — 0 FATAL / 0 MAJOR / 3 MINOR (expository)** | conditional on the named pending finite certificate **(POS)**: `Dpol > 0` and `Npol > 0` on the open orthant `(0,∞)^5` |
| PH caller (any actual PH realization with ≤ 7 states at `z = 8/9` has a directed 2-, 3- or 4-cycle) | **0 FATAL / 0 MAJOR / 0 MINOR** | conditional on the named irreducibility/normalization import (`z > 1/2` theorem) and on the spectral theorem above |

Everything in the written argument other than (POS) was reconstructed independently and verified exactly (see §2–§4). (POS) was treated, per assignment, as a separately pending finite-certificate obligation; this review did **not** certify it, but an exact/heuristic counterexample search found **no** nonpositive point and the margins at `z = 8/9` are healthy (§4). No global 8/9 existence/exclusion claim is made or supported here; the conclusion is only the short-cycle necessary condition.

## 1. Scope actually covered

Reviewed: (a) the permutation-expansion claim that girth ≥ 5 fixes the `y^6..y^3` coefficients to the diagonal product; (b) the (PQ)/(E) linear system and its closed-form coefficients; (c) `den/tn/rn`, `Dpol`, `Npol`, integrality, degrees, term counts, coefficient digests, Cramer and discriminant identities; (d) exact boundary/cancellation counterexample search for (POS); (e) the written Bernstein-cover positivity *logic* (not the leaf data); (f) the PH caller: transform → `D(y)` divisibility, shift/scale normalization, use of the import; (g) the side claim "5 of the 14 eight-edge shapes have girth ≥ 5".

Not covered: leaf-by-leaf verification of the 513/657 dyadic cover (sibling certificate review); re-proof of the imported irreducibility theorem; novelty; whether any PH7 realization exists at 8/9.

## 2. Independent reconstruction (exact, stdlib only)

Artifacts (mine, exclusive, this directory):

- `proof-reconstruct-v1.py` 420 LF / 21028 B, SHA-256 `a174de21ebf2b5363fb47f46b33179e472a391090235497a730c09a781d4f993`; its log `proof-reconstruct-v1.log` 85 LF / 8981 B, SHA-256 `0c856b0a1c00c0fa38c72486118414c707b1aadd501afdc38c209c32ad6bd217`. Final line `ALL PROOF-REVIEWER RECONSTRUCTION ASSERTIONS PASSED`, exit 0, ~57 s, Python 3.14.3, `fractions`/`itertools`/`hashlib`/`json`/`math`/`random` only.
- `proof-examples-v1.py` 112 LF / 6065 B, SHA-256 `eaba3c86a2e96364d8bcde772cae5cb97293751c6d483eaa93f4d89d5995745d`; log `proof-examples-v1.log` 48 LF / 4547 B, SHA-256 `06dddc34e049e4f17e857cefa42d071abc5999df4b5d89e592a0ede6c1794143`.

The only author data consumed are the two coefficient digests copied from the pinned certificate JSON, used solely as comparison targets.

### 2.1 Coefficient claim (manuscript §2)

`det(yI−G) = Σ_σ sgn σ ∏ (yI−G)_{i,σ(i)}`. A nonidentity σ contributes only if every nontrivial cycle of σ is a directed cycle of the off-diagonal support; with no directed cycle of length ≤ 4 and seven vertices, σ has exactly one nontrivial cycle of length 5, 6 or 7, so its term has `y`-degree ≤ 2. Hence the `y^6, y^5, y^4, y^3` coefficients are `e_1..e_4(u)` of the diagonal rates — for any number of edges, overlapping cycles, or non-normality. Equivalent trace view: for `k ≤ 4` every closed walk of length `k` is a pure self-loop walk, so `tr G^k = Σ(−u_i)^k`, and Newton's identities give the same four equations.

Exact check (Faddeev–LeVerrier over `Fraction`, random positive rational rates/weights, 3 trials each): theta 5/7, theta 6/7, theta {1,3}/ℓ₃=4, the 7-cycle, and five random **maximal** girth-5 supergraphs with 11–12 edges all satisfy `c_{7−k} = e_k(diag)`, `k=1..4`; controls with a 4-cycle or a 2-cycle break it (and girth-5 graphs with a 5-cycle already change `y^2`, as expected). PASS.

### 2.2 The (PQ)/(E) system, two independent derivations

*Route A (direct y-coefficient matching, seven symbolic variables u₀..u₄, t, r):* `D(y) = y[(y+1)^2+8/9]^2 = y^5 + 4y^4 + (70/9)y^3 + (68/9)y^2 + (289/81)y`. Matching `y^6, y^5` gives exactly the manuscript's (PQ); substituting into `y^4, y^3` gives `E4, E3`, verified affine in `(t, r)` with no `t·r` term, and with closed forms (my hand derivation, confirmed symbolically)

    a00 = s2 − 4s1 + 74/9,   a01 = s1 − 4,       b0 = s3 − 4s2 + (74/9)s1 − 28/3,
    a10 = s3 − (70/9)s1 + 212/9,   a11 = s2 − 70/9,   b1 = s4 − (70/9)s2 + (212/9)s1 − 1007/27.

*Route B (power series / [2/2] Padé, my own formulation):* reverse the polynomial. With `Ŝ(w) = ∏_{i≤5}(1+u_i w)` and `D̂(w) = (1+2w+(17/9)w^2)^2`, the matching of the top five coefficients is `Ŝ(w)(1+tw+rw^2) ≡ D̂(w)(1+pw+qw^2) (mod w^5)`. Multiplying by `D̂^{-1} = Σ h_k w^k` with `h = (1, −4, 74/9, −28/3, 1/27)` (exact series of `(1+2w+17w²/9)^{-2}`) kills `p, q` from the `w^3, w^4` equations and gives, with `σ_k = Σ_j s_j h_{k−j}`,

    σ2·t + σ1·r = −σ3,    σ3·t + σ2·r = −σ4,

i.e. `1+tw+rw^2` is the [2/2] Padé numerator of `D̂/Ŝ`. Verified symbolically: `E4 = σ3 + σ2 t + σ1 r`, `E3 = (σ4+4σ3) + (σ3+4σ2) t + (σ2+4σ1) r`, so the two systems are row-equivalent with the **same** determinant and solution:

    den = σ2² − σ1σ3,   tn = σ1σ4 − σ2σ3,   rn = σ3² − σ2σ4   (identical to the author's a/b-form den, tn, rn).

Cramer identities `a00·tn + a01·rn + b0·den = 0`, `a10·tn + a11·rn + b1·den = 0` hold as polynomial identities. PASS.

### 2.3 Dpol, Npol, digests, discriminant identity

`81·den` and `−19683·(tn² − 4·rn·den)` are integer polynomials; 81 and 19683 are exactly the least common denominators of `den` and of the discriminant numerator. Term counts **96 / 1753**, individual degrees **[2]^5 / [4]^5** — as stated. My canonical digests (`sorted [[exponents], str(int)]`, compact JSON, SHA-256) equal the certificate's `5449296f…4009` (D) and `7c1ebd08…f69e` (N). Polynomial identity `3·Dpol²·(tn²−4·rn·den) = −Npol·den²` verified, i.e. `t² − 4r = −Npol/(3·Dpol²)` exactly. `Dpol(0) = 2452`, `Npol(0) = 91421104`. PASS.

Logic check: given `den ≠ 0` the solution `(t, r)` is unique; given `Npol > 0` it has `t² − 4r < 0`, while real `v1, v2` force `(v1−v2)² = t² − 4r ≥ 0`. Nothing about `Q`'s roots, hidden/visible coincidences, edge weights, or the lower coefficients is used. Correct.

## 3. PH caller, reconstructed directly

1. **Transform → `D(y) | χ_G`.** `H(s) = α(sI−T)^{-1}ω = n(s)/χ_T(s)` with `n` a polynomial (adjugate). `H` in lowest terms is `c(a²+b²)²/[(s+c)((s+a)²+b²)²]` (constant numerator ≠ 0), so `(s+c)((s+a)²+b²)² · n(s) = c(a²+b²)² · χ_T(s)` and the reduced denominator divides `χ_T`. With `G = (T+cI)/d`, `χ_G(y) = d^{-7} χ_T(dy − c)`, and `(dy)((dy−c+a)²+b²)² = d^5 · y[(y+1)² + b²/d²]² = d^5 D(y)` at `z = b²/d² = 8/9`. Hence `D | χ_G`, with multiplicities, regardless of extra cancellations or repeated hidden roots. Reconstructed, correct.
2. **Normalization.** Shift by `cI` and scaling by `1/d > 0` preserve the off-diagonal support (so the cycle statement transfers to `T`), the Metzler property, irreducibility, and map the spectral bound `s(T) = −c` (import) to `s(G) = 0`.
3. **Import use.** The named `z > 1/2` theorem (`8/9 > 1/2`) supplies: exactly seven states, strong connectivity, `s(T) = −c`. Then Perron–Frobenius for the irreducible Metzler `G` gives a positive right null vector `v`, and row `i` of `Gv = 0` gives `u_i = Σ_{j≠i} G_ij v_j / v_i > 0` because an irreducible matrix of order ≥ 2 has an off-diagonal positive entry in every row.
4. **Conclusion.** If the support graph had no directed cycle of length ≤ 4, §2 applies to the actual seven positive rates (any five chosen) and contradicts (POS). Hence a 2-, 3- or 4-cycle exists. Valid, conditional exactly on the import and (POS).

Consistency with the prior disposition: the 7-cycle (girth 7) is excluded by both the earlier "simple nonreal roots" argument and by this theorem; no tension.

## 4. (POS): pending obligation, counterexample search, boundaries, cancellations

**Status: not certified by this review.** It is a finite, mechanically checkable claim; the manuscript's own cover logic (§4) is sound as written (checked: compactification `u = x/(1−x)` is a bijection `(0,1)→(0,∞)` with positive Jacobian factor `(1−x)^d`; tensor Bernstein coefficients are monomial coefficients divided by binomials; nonnegative coefficients on a box give `P̃ ≥ 0` there; midpoint de Casteljau with common scale `2^d` preserves signs; and strict positivity at every point of the open cube follows from "every leaf corner inside the open cube has a strictly positive coefficient" **together with** "every coordinate split at least once" — for a point `x` of a closed leaf box inside the open cube, pick for each coordinate either `x_j` itself if it is a box endpoint, or the box endpoint lying in `(0,1)` (exists because the box width is ≤ 1/2); that corner's basis function is positive at `x` and its coefficient is `> 0`).

**Exact search (all with `Fraction`, no floats in the verdict):**
- 24-point boundary battery including `u = ε·1` and `u = M·1` for `ε = 10⁻⁹, 10⁻⁶, 10⁻³`, `M = 10³, 10⁶, 10⁹`, mixed `(ε,ε,ε,ε,4)`, `(1,1,ε,ε,ε)`, `(2,2,ε,ε,ε)`, `(17/9,17/9,1,1,1)`, `(4/3,4/3,4/3,.01,.01)`, `(4,0,0,0,0)` (closed-boundary probe), `(1,2,3,4,5)`, `(1/2,1,2,4,8)`: all `D, N > 0`; battery minima `D = 112`, `N = 181504` at `u = 1`.
- 3000 random rational points `u_i ∈ {a/b : 1 ≤ a,b ≤ 2000}`: all positive; min `D ≈ 121.1`, min `N ≈ 1.04·10⁵`.
- Float global searches (400 random-restart adaptive local searches in log-coordinates over `[e⁻⁹, e⁷]`, raw and scale-normalized objectives), each best point re-evaluated **exactly** at a nearby rational: `min den = 112/81` at `u = (1,1,1,1,1)`; `min(−disc) ≈ 4.5439` at `u ≈ 1.2118·1` (`N ≈ 8.94·10⁴`). No nonpositive value anywhere.
- Exact diagonal analysis: `D(x·1) = 4050x⁴ − 12960x³ + 16110x² − 9540x + 2452 = 112 + (x−1)²(4050x² − 4860x + 2340)`, and the cofactor has discriminant `−14288400 < 0`, so `D(x·1) ≥ 112` for **all real** `x` with equality only at `x = 1` — consistent with the global float minimum. `N(x·1)` is a degree-10 polynomial with `N(0) = 91421104`, leading coefficient `86113125 > 0`, minimum on `(0,4]` (step 10⁻⁴) `≈ 89437.7254` at `x = 1.2118`.
- Asymptotics (hand + exact at `10⁹`): all limits `u → 0`, `u → ∞` (any subset) keep `den > 0` and `disc < 0`; no boundary degeneracy at `z = 8/9`.

**Exact quantitative examples at `z = 8/9`** (five chosen rates → unique `(t, r)`):

| u₁..u₅ | den | Dpol | Npol | t | r | t²−4r |
|---|---|---|---|---|---|---|
| (1,1,1,1,1) | 112/81 | 112 | 181504 | 19/7 | 64/21 | −709/147 |
| (4/5)·1 | 3844/2025 | 3844/25 | 6573209248/15625 | 346/155 | 393323/144150 | −427498/72075 |
| (1,2,3,4,5) | 90292/81 | 90292 | 185884623424 | −14268/22573 | 135433/67719 | −11617788964/1528620987 |
| (1/10)·1 | 329309/16200 | 329309/200 | 674863265216869/16000000 | 15858469/6586180 | 271275683/98792700 | < 0 |

Each satisfies `t²−4r = −Npol/(3·Dpol²)` exactly. For `u = 1` the two "remaining rates" would be `19/14 ± i·√2127/42` — non-real; the power sums `Σ(−u_i)^k`, `k=1..4`, of `(−1)^×5` plus this pair equal those of `(0, −1±i√(8/9) ×2, ν₁, ν₂)` to 10⁻¹⁵ (float cross-check of the Newton-identity view).

**Cancellation cases.** Hidden roots equal to visible roots, a hidden root at 0, multiple-of-D characteristic polynomials, defective `G`, or arbitrary edge weights do not touch the argument: the four matched coefficients depend only on the diagonal and `D | χ` is all that is used. No counterexample route exists through cancellation.

**Control — the obstruction is `z`-specific, not inherited from `z > 1/2`.** At `z = 1/2`, `u = (1,1,1,1,1)` gives `σ = (1, 1, −1, 1, −1/4)` and **`den = 0` exactly**; nearby, `u = (1,1,1,1,3/2)` gives `t = 13/2`, `r = 4`, `t²−4r = 105/4 > 0`, i.e. real positive `v₁,₂ = (13 ± √105)/4`, so the spectral top-coefficient obstruction is void at `z = 1/2` (this says nothing about PH realizability there). Heuristic minima of `den` / `−disc` are negative for `z ∈ {0.05, 0.25}`, ≈0 / negative at `z = 1/2`, and positive for `z ∈ {8/9, 1, 2, 5}`. The manuscript correctly claims only `z = 8/9`.

## 5. Side claim: eight-edge shapes

Strongly connected simple digraphs on 7 vertices with 8 edges = one ear on a cycle: enumerated both as theta `(ℓ₁ ≤ ℓ₂, ℓ₃)` / figure-eight `(a ≤ b)` and as cycle+ear `(c₁, ℓ, k)` (duplicate edges and self-loops excluded), canonicalized over all 5040 vertex permutations: both give the **same 14** classes (11 thetas + 3 figure-eights). Girth ≥ 5 for exactly **5**, all thetas: `(1,2,5)` g6, `(1,3,4)` g5 (the "full 5-/7-cycle theta"), `(2,2,4)` g6, `(2,3,3)` g5, `(3,3,2)` g5; every figure-eight has girth ≤ 4. Matches the manuscript.

## 6. Findings

- **MINOR-1 (exposition, §4).** The step "every leaf corner in the open cube has strictly positive coefficient ⇒ strict positivity at every interior point" needs the corner-selection argument spelled out in §4 above (it uses "each coordinate split at least once"); the ingredients are present in the manuscript but the inference is only asserted.
- **MINOR-2 (statement sharpness).** "Irreducible" and "spectral bound 0" are used solely to obtain `u_i > 0`; the proof actually shows: *no real 7×7 matrix with all diagonal entries negative, support graph of directed girth ≥ 5, and `D | χ` exists* (Metzler not needed). Stating the dependence would make the hypotheses' role transparent.
- **MINOR-3 (reader guidance).** Because (POS) fails at `z = 1/2` (den = 0 at `u = 1`), a sentence noting that the 8/9 certificate does not transfer to the import's `z > 1/2` range without re-certification would prevent over-reading.

No FATAL or MAJOR defect was found in the written mathematics or in the caller.

## 7. Explicitly imported / unverified here

1. **(POS)** — `Dpol > 0`, `Npol > 0` on `(0,∞)^5`: pending finite-certificate obligation; not certified by this review (evidence in §4 is exact at points but not a proof).
2. **Irreducibility/normalization import** (`z > 1/2`: seven states, strong connectivity, `s(T) = −c`): read in full, not re-proved.
3. Perron–Frobenius for irreducible Metzler matrices; Cramer/adjugate representation of the transfer function; Newton's identities. Standard, not re-derived.
4. The author's checker/certificate/replay: read, not executed; no evidence derived from them beyond the two digest strings used as comparison targets.

## 8. Boundary of this review

Same-harness, single reviewer, exact arithmetic where stated, floating heuristics only in search steps that were re-confirmed exactly. Not a human proof, not a formal/kernel proof, not an independent-family review, not a novelty assessment. It establishes no existence or exclusion of a PH7 realization at `z = 8/9`, no minimum-order value, and nothing for other `z`.

END — spectral short-cycle theorem: 0 FATAL / 0 MAJOR / 3 MINOR conditional on the pending (POS) certificate; PH caller: no defect conditional on the named import. Clock before writing: 2026-10-28T19:39:16-0700 PDT.
