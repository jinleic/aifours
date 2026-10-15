# Referee report: norm-ranked lattice spiral (`review/input/RESULTS.md`)

## Verdict: correct

The theorem at `review/input/RESULTS.md:28-49` is proved as written, for every fixed n ≥ 2, under the source's own definitions. I found no blocking defect, no counterexample and no gap in any quantifier. The four notes F1–F4 below are editorial and don't affect validity. If your rubric counts any textual edit as a "fix", F1 is the only item in the mathematical text, and it needs one sentence.

**No unresolved lemma remains for the n ≥ 3 existence question on p23.** This verdict covers the mathematics only. It does not certify novelty or priority.

For independence, I did not run `verify.py` and did not open `review/claude-output.json`.

`★ Insight ─────────────────────────────────────`
- The proof turns on one inequality: |k^{1/n} − c·r| ≤ |k − V_n r^n| / (c·r)^{n−1}. The radial correction tends to zero exactly when the lattice-ball discrepancy is o(r^{n−1}) at both ends of every tie shell. That is why the classical Landau exponent n(n−1)/(n+1) carries the argument and the leading volume term alone does not.
- Ties are handled by bounding both N_<(r) and N(r). The order inside a shell therefore never matters.
`─────────────────────────────────────────────────`

## 1. Does the construction fit the source's definitions?

I checked this against the rendered PDF pages.

| What the source requires | Where | How the construction meets it |
|---|---|---|
| Uniformly discrete (inf over x≠y of ‖x−y‖ > 0) and relatively dense (sup over x of inf over y of ‖x−y‖ < ∞) | p1 | (5.4), (5.5) |
| Spiral set: s_k = k^{1/n}·u_k for **any** sequence u_k on the sphere | p2–3, eq. (1.3) | ‖s_k‖ = k^{1/n} exactly. Repeated directions (z and 2z) are allowed. |
| A "spiral" set need not look like a spiral | p2, footnote 1 | — |
| Density: for **every** bounded measurable X with λ(∂X) = 0, #{k: s_k ∈ RX}/R^n → r·λ(X) | p22 | (2.3), with real R |
| Caps C(w,ρ) = {u : d(w,u) ≤ ρ} are closed, any ρ > 0; ∂D = closure minus interior | p4–5 | §7 |
| r = V_n^{−1} (a superscript inverse, not V_{n−1}) | p22 and p23, checked visually | Forced by (7.2) |

pp1–5 and pp22–23 contain no requirement of continuity, a bounded step between consecutive points, an orbit structure, or distinct directions.

**Scope note.** In this construction the jump between consecutive points is unbounded. Example in n = 3: z₂₆ = (1,1,1) is the last vector of shell 3 and z₂₇ = (−2,0,0) is the first of shell 4, so ‖s₂₇ − s₂₆‖ ≈ 5.29. At shell transitions the jump grows like about 2k^{1/n}. The source allows this, and `RESULTS.md:12` disclaims it, but a reader who expects spiral-like steps would need a different construction.

## 2. Step-by-step audit, with independent re-derivations

### §3: ball count (3.1)

- **(3.2), Fourier transform of the ball.** I recomputed it. Slicing gives V_{n−1}·2R^n ∫₀¹ (1−v²)^{(n−1)/2} cos(2πqRv) dv. Applying DLMF 10.9.4 with ν = n/2 and multiplying by V_{n−1} = π^{(n−1)/2}/Γ((n+1)/2) gives exactly R^{n/2} q^{−n/2} J_{n/2}(2πRq). As ξ → 0 the formula tends to V_n R^n, as it should.
- **(3.4), the n = 3 formula.** I recomputed it by direct integration: 2π∫₀^R (R²−t²) cos(ωt) dt = 4π(sin ωR − ωR cos ωR)/ω³ with ω = 2πq, which is the stated formula. It also matches the closed form of J_{3/2}. It is bounded by (1+2πRq)/(2π²q³) ≤ C·R·q^{−2}, so n = 3 needs no Bessel asymptotics.
- **(3.3), decay bound.** It needs 2πR|ξ| ≥ 1, which holds for R ≥ 1 and every nonzero integer frequency ℓ.
- **(3.5), the sandwich.** The exp bump vanishes for |y| ≥ ε. If |x| > R, then |x−y| > R−ε, so f₋(x) = 0. If |x| ≤ R, then |x−y| ≤ R+ε, so f₊(x) = 1. This handles the closed boundary correctly, and R−ε ≥ 1.
- **(3.6), Poisson summation.** The convolution theorem and the scaling φ̂_ε(ξ) = φ̂(εξ) are right under the stated convention. Poisson summation is applied to smooth compactly supported functions, never to indicators.
- **(3.7), the frequency sum.** The exponent after counting annuli is (n−3)/2 > −1 for n ≥ 2. The upper tail only needs M > (n−1)/2.
- **(3.8), the error balance.** The term R^{n−1}·ε is the continuous volume difference V_n[(R±ε)^n − R^n]. No thin-shell lattice count is assumed. With ε = R^{−β} and β = (n−1)/(n+1), both terms are of order R^{n(n−1)/(n+1)}, and α_n − (n−1) = −β for every n ≥ 2.

### §4: ties

- Both endpoints in (4.1) are right.
- (4.2): N(R) is constant just below r, and the O-constant is uniform in R, so the bound passes to the left limit.
- (4.4) just drops nonnegative terms from the denominator.
- The bound depends only on r. It therefore holds for every rank inside a shell, under any ordering of the shell.

### §5: separation and covering

- **Every pair i < j is covered.** If i ≥ K, (5.1) applies. If i < K and j ≥ L, (5.2) applies. If i < K and j < L, (5.3) applies, since K ≤ L means both indices are below L. These cases are exhaustive.
- **K exists** because δ_k ≤ C·r_k^{−β} and r_k is nondecreasing and unbounded.
- **(5.3).** By concavity, j^{1/n} − i^{1/n} ≥ g(j) ≥ g(L−1) ≥ g(L) > 0, where g(m) = m^{1/n} − (m−1)^{1/n}.
- **Covering (5.5).** Rounding each coordinate gives a lattice point within c√n/2. If that point is the origin, replacing it with e₁ costs at most c more.

### §6: density for every bounded Jordan set

- The argument uses only four facts: ∂X is compact with measure zero; it has a finite open-box cover U; h = dist(∂X, Uᶜ) > 0; and a closed segment is connected, so a segment meeting both X and its complement meets ∂X.
- No convexity, connectedness, closedness or smoothness of X is used.
- I checked the argument against an open ball, a disconnected X, a single point (λ = 0), sets containing the origin, and the fact that every nonempty bounded X has nonempty boundary. It holds in each case.
- Bounding the count in U by the sum of the box counts handles overlapping boxes.

### §7: cap equidistribution

- A nonzero s_k has a unique polar decomposition, so #(S ∩ N^{1/n}X_C) = #{k ≤ N : u_k ∈ C} holds exactly.
- The boundary of X_C lies in {0}, the cone over the cap's boundary, and the closed cap at radius 1. All three are null for every closed cap with ρ > 0, including ρ ≥ π.
- (7.2) gives the normalization: s_k is in the closed ball of radius R exactly when k ≤ R^n, so the count is ⌊R^n⌋ and r must be 1/V_n.
- **A strength:** equidistribution is derived directly from (2.3). The proof does not rely on the authors' unproved "elementary adaptation" if-and-only-if remark on p22.

### §8: the generator

- The retained set {0 < ‖z‖ ≤ M} is closed downward in the global order, because every coordinate satisfies |z_i| ≤ ‖z‖ ≤ M. Its sorted prefix is therefore the global prefix.
- Every nonzero z gets a finite rank, at most N(‖z‖). The enumeration is a bijection from the positive integers onto Z^n \ {0}, nonprimitive vectors included, and all keys are exact integers.
- `verify.py:40-41`: `lexsort` treats the last key as primary, so the keys (z_n, …, z₁, ‖z‖²) give exactly the order (‖z‖², z₁, …, z_n).
- `verify.py:55` doubles M at each step, which is a valid way to "increase M".

## 3. Quantifier check

| Quantifier | Status |
|---|---|
| Every real radius R | ✓ for R ≥ 2; see F1 for R < 2 |
| Every rank in a tied shell, including partial cuts | ✓ |
| Every pair, including the finite prefix and cross-prefix pairs | ✓ |
| Every point of space, including near the origin | ✓ |
| Every bounded Jordan set, including nonconvex, disconnected, nonclosed and null sets | ✓ |
| Every closed cap with ρ > 0, including the full sphere | ✓ |
| Every fixed n ≥ 2 | ✓ Constants depend on n; no uniformity in n is claimed. |

## 4. Findings, by severity

**Critical: none. Major: none.**

- **F1 (minor, editorial) — `RESULTS.md:59-63` versus `:151-156`.** (3.1) is proved only for R ≥ 2, but (4.2)–(4.3) are used for every shell. That includes r ∈ {1, √2, √3, 2}, and the left limit at r = 2 is taken through R < 2. This is harmless: on [1, 2] both N₀ and V_n R^n are bounded and R^α ≥ 1, so (3.1) holds for all R ≥ 1 with a larger constant. **Fix:** add one sentence saying so, or say that finitely many shells are absorbed into the constant in (2.2).
- **F2 (minor, clarity) — `:30`, `:51`, `:176`.** "Effectively constructible" applies to the sequence only. K, L, η_n and D_n are proved to exist but are not computed, because they inherit the unspecified constant in (3.1). The source only asks for existence, so this is not a defect. **Fix:** add one sentence so the "effective" claim is not read as covering the Delone constants.
- **F3 (editorial) — `:220`.** In "…meets the boundary, or one endpoint is itself on it", the second clause is redundant because a closed segment is connected. **Fix:** state directly that dist(c_n z_k/R, ∂X) ≤ δ_k/R ≤ D_n/R < h.
- **F4 (bookkeeping, not mathematics) — `:277`.** This line says the numerical outputs and referee dispositions "are integrated into this section", but the frozen copy contains neither. **Fix:** integrate them or reword before release.

## 5. Standard inputs versus new bridges

**Standard results the proof relies on:**
- The ball's Fourier transform via DLMF 10.9.4.
- The bound J_ν(x) = O(x^{−1/2}) from DLMF 10.17.3. This is not needed for n = 3, because of (3.4).
- Poisson summation for smooth compactly supported functions.
- Landau's smoothing bound (3.1).
- Lebesgue's criterion (a bounded set is Jordan measurable iff its boundary is null) and lattice counting in Jordan sets.
- Polar coordinates.

**New bridges, all verified above:**
1. Re-ranking the lattice radially, s_k = k^{1/n}·z_k/‖z_k‖, combined with discrepancy bounds at both ends of each tie shell, gives δ_k = O(r^{−β}) uniformly across ties.
2. The explicit split of all pairs that handles the finite prefix.
3. Transferring Jordan density through a bounded displacement. The idea is standard in spirit and is written correctly here.
4. The exact cone identity that turns (2.3) into cap equidistribution.

## 6. The numerical record (evidence only, not proof)

I did not run anything; these are hand checks against the frozen JSON.

- **Count errors** match 1 + N − (4π/3)r³. For example, at r = 8: 2109 − 2144.66 = −35.66.
- **Closed-hemisphere excess** matches the prediction 1/2 + 3/(8r) from the lattice points on the equatorial plane. At N = 50000 (r ≈ 22.85) this predicts 0.5164, and the JSON shows 0.51644. At N = 1000 it predicts about 0.56, and the JSON shows 0.56.
- **The axis-0 asymmetry** at N = 10000 (0.5309 versus 0.5251) comes from the last partial shell being cut in lexicographic order by z₁. This is consistent with the stated tie order.
- **The box-count oscillation** (e.g. 342/12³ = 0.198 against the limit 0.2387) is a rounding-down effect at the box edges, ⌊3.72⌋ = 3. The write-up correctly does not claim these counts are monotone.
- **The sampled separation (1.356) and covering radius (1.378)** are not global constants, and the proof never uses them.

`★ Insight ─────────────────────────────────────`
- Only tail separation actually needs δ_k → 0 (strictly, δ_k < c_n/2 eventually). Covering (5.5) and the density transfer (6.2) only need sup δ_k < ∞. The sub-(n−1) discrepancy is therefore what secures uniform discreteness. Without explicit constants, even the trivial O(R) Gauss bound in the plane would not be enough.
- Caps whose boundary contains a lattice plane converge at the slow rate N^{−1/3}. That fully explains the 0.56 → 0.528 → 0.516 sequence, with no defect in the equidistribution argument.
`─────────────────────────────────────────────────`

## 7. Bottom line on the source question

Under the definitions on pp1–5 and p22 of arXiv:2010.06428v3, the construction gives, for every n ≥ 3 (and also n = 2), a spiral Delone set with asymptotic density V_n^{−1} over all bounded Jordan sets, and its directions are equidistributed over caps. That answers the p23 question affirmatively, and no lemma is left open.

This report does not certify:
- novelty or priority;
- numerical values of the Delone constants;
- any spiral-like property beyond the source's definition.
