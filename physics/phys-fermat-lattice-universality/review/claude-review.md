# Referee report: `review/proof-r1.md` (Theorem U)

**Scope.** I worked read-only. I read all 236 lines of the proof, Tevet pp. 1–13, McMullen pp. 1–12, and the other in-scope files. `RESULTS.md` is the same text as the proof and adds no evidence. I executed nothing, and I did not count the §8 protocol, which has not been run, as evidence.

## (1) Verdict: **CORRECT**

I found no mathematical gap. I checked every equation by hand. F1–F5 below are editorial: none of them needs a change to a definition, the construction, a constant, or a conclusion. This is not a formal-kernel certification and not a novelty or priority assessment.

`★ Insight ─────────────────────────────────────`
- §2 uses a classical fact: every point of the modular surface lies on a bounded geodesic. In the frame of `B=[[A,Aβ],[C,−Cu]]`, applying `diag(s,1/s)` to the lattice traces the geodesic with endpoints `β` and `−u`. Changing the frame through `t` changes the direction, and the winning-set step picks a direction where both endpoints are badly approximable.
- §3 builds one α by hand whose geodesic follows that bounded two-sided geodesic for longer and longer stretches. Every digit comes from `{1..M}`, so α's own geodesic also stays bounded. The proof never relies on a "dense but unbounded" geodesic.
`─────────────────────────────────────────────────`

## (2) Findings, most severe first (none blocking)

**F1 – Low: a standard lemma is used without proof or citation** (`proof-r1.md:149`, `:190`, `:206-208`)
- **What the proof does:** at all three points it proves the two Kuratowski conditions: every point of the limit is approached by points of the sets, and every limit of points from the sets lies in the limit. It then concludes convergence "in the Chabauty–Fell topology".
- **The source mismatch:** Tevet defines this topology by a metric (p. 2). Tevet's Prop. 3 (p. 3) proves only the other direction: metric convergence implies the Kuratowski description.
- **Missing step (two lines):**
  - Suppose `x_k ∈ A_k ∩ B̄_{1/ε}` stayed at distance at least ε from `A`. Compactness gives a limit point at distance at least ε from `A`, which contradicts the second condition.
  - For the other inclusion, cover `A ∩ B̄_{1/ε}` by finitely many ε/2-balls centred on points of `A`, and apply the first condition at each centre.
  - Alternatively, the convergence of basis matrices in (7) and the bounds (8)–(9), which hold uniformly on balls, give `Δ → 0` directly.

**F2 – Low: one step in §6 is not stated** (`:206-212`)
- The passage from `Y_{m_k} → BZ²` and `ω_k = e^{2πi m_k α} → e^{iθ}` to `X_α − P_{m_k} = ω_k Y_{m_k} → e^{iθ}BZ²` (and then adding `b`) needs one sentence.
- It holds because rotations about 0 are isometries that preserve balls centred at 0, and `|ω_k w − e^{iθ}w| ≤ |ω_k − e^{iθ}|·|w|`.
- This is exactly where the analysis-frame rotation of `:157-159` is removed, so it should be said explicitly.

**F3 – Low: two different definitions of "badly approximable"** (`:19`)
- The proof's definition of Bad is McMullen's `D(SL₂Z)` (p. 3): an inequality that holds uniformly over all fractions p/q.
- Tevet's definition (p. 1) is `c_α = liminf q_j|q_jα−p_j| > 0`. His "if and only if bounded" statement on p. 6 is about his own definition, so the citation does not quite fit.
- Both directions the proof needs follow from the identity behind (4): `q_j|q_j x−p_j| = 1/(x_{j+1}+q_{j−1}/q_j)`.
  - Membership of r and u in `D(SL₂Z)` with constant C implies every partial quotient is less than 1/C (needed at `:85`).
  - Digits at most M imply `c_α ≥ 1/(M+2)` (needed at `:93`).
- So the α produced is badly approximable in Tevet's own sense, which is the sense of the p. 12 question.

**F4 – Low: more is imported than needed** (`:24-25`, `:67-71`)
- McMullen states property (2), countable intersections, as "straightforward" without proof. Under his rule that A wins when `∩B_i` meets E, the radii need not shrink, so the intersection claim needs an extra device.
- In this one-dimensional, bi-Lipschitz case both imported steps are elementary. I checked both:
  - **(a) Transport:** preimages of intervals under a homeomorphism of ℝ are intervals. With `β = β'/L²`, moves in the game for G⁻¹(Bad) pull back to legal moves in the game for Bad, and A's replies push forward to legal moves.
  - **(b) Intersection:** A plays E₁'s β³-strategy in rounds 1, 4, 7, …, E₂'s in rounds 2, 5, 8, …, and blocks a centred ball in rounds 3, 6, 9, …. Each blocking round forces `|B_{i+1}| ≤ (1−β)|B_i|/2`. Each subgame is a legal β³-game, so `∩B_i` is a single point lying in `E₁ ∩ E₂`.
- With these written in, the only non-elementary import left is McMullen's Theorem 1.3 (or, classically, Schmidt's theorem that Bad is winning).

**F5 – Cosmetic**
- `:81`: "Because β is irrational, a≥1" — the bound `a ≥ 1` comes from `β > 1` (`:53`); irrationality only gives `r ≠ 0`.
- `:25`: "radii tending to zero" is unnecessary. `∩B_i ⊂ B_1 ⊂ I` already gives `E ∩ I ≠ ∅`.

**F6 – Outside the proof; for the finite-verification review** (`:227`)
- The four protocol examples have `x ∈ {0, 0, 1/2, 1/3}`, which breaks the normalisation `x > 1` at `:35`.
- For `x = 0`, the bound `h/x` at `:39` is undefined. The correct range there is just `t > h`.
- The examples are still valid inputs for §§3–6, which only need `t > 0`, `β > 1`, `0 < u < 1` and both ratios badly approximable. I checked u ≈ 0.618, 0.848, 0.109 and 0.261. The β values are quadratic irrationals, so the §2 winning-set step is skipped. The protocol should say so.
- Hand sanity check: the square example gives `r = u = 1/φ` and `a = 1`, so every digit, padding included, is 1. Then `α = 1/φ`, `c = 1/√5`, `c̃ = −1/√5`, which is Tevet's sunflower data.

**F7 – Problem in the source; no effect on Theorem U** (Tevet p. 2 vs pp. 9–11)
- Theorem 2 as displayed on p. 2 uses the matrix `[[1,c],[β,c̃/β]]`. Tevet's own derivation (p. 9) and Part 2 (pp. 10–11) give `[[1,β],[c,c̃/β]]`.
- The proof's `B` agrees with the pp. 9–11 form, with `t = A`, `c = 1/(β+u)`, `c̃ = −βu/(β+u)`.
- The two forms are not equivalent. For the golden angle the correct family is the closed geodesic with endpoints `(φ, −1/φ)`, which passes through the square lattice. The p. 2 display gives the endpoints `(1/√5, −1/(√5φ²))`, which are not Galois conjugates of each other.
- Anyone checking the proof against the literal p. 2 display would get false alarms.

### Audit checklist (all pass)

| Item | Check performed |
|---|---|
| Quantifiers | For every Λ there is α; for every rotation S and offset b there are translations. α is fixed before S and b; `m_k` depends only on the target angle θ. |
| Signs and determinants | `det(V,W) = |V|²·Im(W/V) = −π`. (1): `AC(β+u) = tA²h(t+1/t) = h|V|² = π`. `det B = det B_k = −π`. The integer basis has determinant `(−1)^j = +1` for even j. The scaling in (10) has determinant 1. |
| Continued-fraction indices | `r₁` at `j_k`, `a` at `j_k+1`, `u₁` at `j_k+2`. `α_{j+1} = a+u_j`. (4) uses `δ_j = (−1)^j/(q_jα_{j+1}+q_{j−1})`; (5) uses `δ_{j+1} = −δ_j/α_{j+2}`. |
| Bounded digits | All digits lie in `{1..M}`. The digit word is one fixed sequence, not rebuilt at each stage. |
| Extension of g | g is a Möbius map with a pole at β = x, so an extension is needed. G is a C¹ bijection with `|G'|` between `h²/(b₀−x)²` and `h²/(a₀−x)²`. |
| Rounding n | `|√n_k − q_j/(2A)| ≤ A/q_j → 0`. |
| Taylor bounds (8)/(9) | (8): the error splits into three terms bounded by `3R²/4ρ`, `2R²/ρ` and `2R²/ρ`. (9): `|tan θ| ≤ R/(ρ−R)` gives `|v| ≈ 1.51R < 3R`, and `ρ ≥ 12R` is exactly what (8) needs at radius 3R. |
| Phase window | `b_k ≤ √n_k = o(n_k)`, so the scaling in (10) tends to the identity. The ε-net is uniform, so the full sequence converges, not just a subsequence. |
| Escape to infinity | `|b − P_{m_k}| ≥ √m_k − |b| → ∞`. |

## (3) Imported-source hypotheses checked

- **Tevet p. 1:** the spiral is `√n·e^{2πiαn}`. Whether n starts at 0 or 1 does not matter, because that one point moves off to infinity under the translations. Bad means α is irrational and `c_α > 0`.
- **Tevet p. 2:** the topology is given by `d = min{1,Δ}`, and a Chabauty limit is the limit of translates `T_nX` with `T_n(0) → ∞`. The proof uses `T_k(z) = z − P_{m_k} + b`, which is a pure translation, and gets convergence of the full sequence.
- **Tevet p. 12:** the question ("every lattice with co-volume π … some Fermat spiral") reads "for every Λ there is an α". Theorem U with S = I, b = 0 is exactly that.
- **McMullen (1.2):** quasisymmetry is defined metrically, so orientation reversal is allowed. G⁻¹ satisfies it with ratio `k = L₂/L₁`.
- **McMullen (1.4)–(1.5):** the absolute game for β in (0, 1/3). Player B chooses the first ball freely, so a winning set meets every open interval.
- **McMullen p. 3:** `D(SL₂Z) = {x : |x−p/q| > C/q² for all p/q}`, which excludes rationals. Theorem 1.3 applies with `Γ = PSL₂(ℤ)` and n = 1: a lattice with a cusp at infinity.
- **McMullen Theorem 2.2:** it requires a global homeomorphism of ℝⁿ. That is why the proof extends g to G.

## (4) What this proves and what it does not

**Proves.** Assuming McMullen's Theorem 1.3 and the standard facts in F1–F3, Theorem U holds as stated. So Tevet's p. 12 question has a positive answer in the "for every lattice, some α" reading, using Tevet's own definitions of Chabauty limit and badly approximable. One α covers every rotated translate of a given lattice.

**Does not prove.**
- **A single α for all lattices.** That stronger statement is actually false. For badly approximable α the spiral is Delone (Akiyama, cited by Tevet on p. 3), and Tevet's Prop. 4 passes its minimum point spacing to every limit. But lattices of covolume π can have arbitrarily short vectors. The proof's §7 correctly disclaims this.
- It also gives no effective or uniform digit bound, no algorithm from real-number input, nothing for α that are not badly approximable, nothing on Cao's energy or chirality conjecture, no formal verification, and no priority claim.
