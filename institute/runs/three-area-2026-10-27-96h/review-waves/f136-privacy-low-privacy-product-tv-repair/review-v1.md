# Review f136 — low-privacy nearest-TV repair of the half-offset product (candidates 1–4)

**Reviewer artifact (same-harness, written-level review). Observed clock before composing: `2026-10-29T03:51:59Z` (= `Wed Oct 28 20:51:59 PDT 2026`).**
Assignment: `manifest-v1.json` (SHA256 `3bcd00161a5080a308563776e4ee6950763bd04abec878dbbc3315e478005280`, 2910 B, re-hashed by reviewer at `2026-10-29T03:34:09Z`), extended additively by `manifest-v2.json` (SHA256 `35f892c7078a09a2db983f905718d08c131be413ff924c5d7ded5c9b02f4c636`, 3984 B, re-hashed at `2026-10-29T03:40:24Z`, predecessor SHA recorded in v2 matches v1). Candidates 1–3 were reviewed under v1 first; candidate 4 afterwards under v2, in the declared order.

This is NOT human, independent-family, formal/kernel, or novelty clearance. No author contact, web search, external model, Git, deletion, publication or infrastructure action was performed. No author checker was imported or executed; all controls below are reviewer-written from scratch (`reviewer-controls-c123-v1.py`, `reviewer-controls-c4-v1.py`).

## 0. Input verification (reviewer re-hash, all in declared order)

| role | file | SHA256 (full) | bytes | LF | match |
|---|---|---|---|---|---|
| candidate 1 | `…/privacy-diamond-mse/frontier-20261028-low-privacy-product-tv-repair-v1.md` | `5f2a697663d841655471edb5c704ec74d96a72cd4f4fd87221314a84c0f8b92e` | 4213 | 64 | yes (`2026-10-29T03:34:15Z`) |
| candidate 2 | `…/frontier-20261028-sharp-corner-tv-bound-v1.md` | `b8aadd5e5d9642f00ddf8baed7f13bed96aa2a81ba5e1ad53c3ee16c8205dab5` | 3327 | 47 | yes (same call) |
| candidate 3 | `…/frontier-20261028-clipped-square-tv-correction-v1.md` | `933d9c66478356a13aab82d00f1c53ea988935433f053a19f685c6c03cbad94b` | 4257 | 66 | yes (same call) |
| candidate 4 (v2) | `…/frontier-20261028-second-order-global-tv-repair-v1.md` | `36b8de16c1306d14cc396bd0ab270556a974b1a8146f76c9705cd54efa4fc6ae` | 5300 | 78 | yes (`2026-10-29T03:46:11Z`) |

Directory prefix: `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/`. No overlay/erratum files were declared by either manifest. Each file was read completely (`:raw`).

## 1. Conventions fixed by the reviewer (the candidates leave them implicit)

* `b = e^{-ε} ∈ (0,1)`, `m = b/(1-b)`, `S = [-1/2,1/2]²`, `D = {‖v‖₁ ≤ 1}` (closed), `|D| = 2`.
* **Full-D ε-privacy of a law μ**: `μ(A) ≤ e^{ε} μ(A+v)` for every Borel `A` and every `v ∈ D` (additive-noise ε-DP under ℓ₁-sensitivity 1). Equivalently `μ(A+v) ≥ b μ(A)`.
* 1D half-offset staircase: density `b^{n(x)}/Z₁`, `n(x) = ⌈max(|x|-1/2,0)⌉`, `Z₁ = 1+2m = (1+b)/(1-b)`. `Q` = product; density `b^{n₁+n₂}/Z₁²`; `q₀ := Q`-density on `S` `= 1/Z₁² = ((1-b)/(1+b))²`. `Q` is not full-D private (control K-neg: the pair `(0.45,0.45)→(0.55,0.55)` at ℓ₁ distance 1/5 has density ratio `b² < b`).
* Shell law with convex core `K`: `p_K(x) = b^{n_K(x)}/Z_K`, `n_K(x) = min{k ≥ 0 : x ∈ K + kD}`.
* `TV(μ,ν) = sup_A |μ(A)-ν(A)| = ∫(f-g)₊`. All candidate formulas are consistent with this normalisation.
* `T*(b) = inf{TV(μ,Q) : μ full-D private Borel law}`.

## 2. Reviewer's reconstruction of the shared lemmas

### 2.1 All-point density representative (asserted without proof by all four candidates)

Every candidate uses "a full-private μ has an all-point bounded density f with `f(y) ≥ b f(x)` whenever `‖y-x‖₁ ≤ 1`". None proves it. It is true; reviewer's proof:

*Absolute continuity.* If `|N| = 0` then `∫_D μ(N+v) dv = ∫ |D ∩ (z-N)| dμ(z) = 0`, so `μ(N+v) = 0` for a.e. `v ∈ D`, and privacy gives `μ(N) ≤ e^{ε} μ(N+v) = 0`. Hence `μ ≪ Leb` with density `f`.
*Representative.* For rational `r>0` put `m_r(x) = μ(B_r(x))/|B_r|` (Borel in `x`). Averaging the hypothesis with `A = B_r(x)` over `v ∈ D`: `μ(B_r(x)) ≤ (e^{ε}/|D|) ∫_D μ(B_r(x+v)) dv ≤ (e^{ε}/2)|B_r|`, so `m_r ≤ e^{ε}/2`. Define `f̃(x) = limsup_{r↓0, r∈ℚ} m_r(x)`: Borel, `0 ≤ f̃ ≤ e^{ε}/2` everywhere, `f̃ = f` a.e. (Lebesgue differentiation), and since `m_r(x) ≤ e^{ε} m_r(x+v)` for all `x`, all `v ∈ D`, the limsup gives `f̃(x) ≤ e^{ε} f̃(x+v)`, i.e. `f̃(y) ≥ b f̃(x)` for all `y-x ∈ D`. ∎
(An alternative that avoids any pointwise representative: the averaged inequality `∫_K f ≥ b ∫_K μ(C_y)/|C_y| dy` follows from the measure form by Fubini over shifts `v = y-x ∈ D`.) **Status: MINOR gap in all four texts; closed by this lemma.**

### 2.2 Full-D privacy of the shell laws — PROVED

For convex `D ∋ 0`, `kD + D = (k+1)D` (exact hull identity checked for k=1,2,3, control K). If `x' - x ∈ D` and `x ∈ K + n_K(x)D` then `x' ∈ K + (n_K(x)+1)D`, so `n_K(x') ≤ n_K(x)+1` and `p_K(x') ≥ b p_K(x)` **for every pair, pointwise**; integrating over `A` gives `P_K(A+v) ≥ b P_K(A)` for all Borel `A`, `v ∈ D`. This holds for the closed diamond (hence also the open one). The candidates' one-line justification ("a D shift changes the shell index by at most 1") is complete modulo this trivial convexity identity. Random-pair control: 3110 D-shift pairs, 0 index jumps > 1 for `P_S` and `P_t`; negative controls (Q itself; half-width shells) do jump by 2. **Verdict: full-D privacy of `P_S` and of every `P_t` (0<t<1/2) is proved.**

## 3. Candidates 1 and 2 — δ-family lower bounds

Reconstruction (all verified):
* Corner region of quadrant σ: `y = (½+a, ½+c)`, `a,c>0`, `a+c<1-δ`. Q-index there is exactly `(1,1)` so `q = b² q₀`; area of the four triangles `|K_δ| = 2(1-δ)²`.
* Overlap: `S ∩ (y-D) = C_y = {u,v ≥ 0, u+v ≤ d}`, `d = 1-a-c`, `|C_y| = d²/2` (exact clipping, control H, four sample points).
* Privacy + averaging over `C_y`: `f(y) ≥ b μ(C_y)/|C_y|`; TV: `μ(C_y) ≥ q₀|C_y| - T` ⇒ `f(y) ≥ b(q₀ - 2T/d²)` (valid even if the bracket is negative).
* Integration with area element `r dr` (`r=a+c`) over four quadrants: `μ(K_δ) ≥ 2b q₀(1-δ)² - 8bT ∫₀^{1-δ} r/(1-r)² dr`, and `∫₀^{1-δ} r/(1-r)² dr = 1/δ + log δ - 1 ≥ 0` (mpmath quadrature vs closed form at five δ, control I).
* With `T ≥ μ(K_δ) - b²q₀|K_δ|`: **`T ≥ 2b(1-b)q₀(1-δ)² / [1 + 8b(1/δ + log δ - 1)]`** for every `δ∈(0,1)`, every `b∈(0,1)`, every full-D private μ (candidate 2 eq. (1), candidate 3 eq. (6)).
* Candidate 1's cruder version with the side-`δ/4` corner square (`‖y-x‖₁ ≤ 1-δ/2 < 1`): `T(1 + 32b(1-δ)²/δ²) ≥ 2b(1-b)q₀(1-δ)²` — verified.
* Asymptotics: `δ = 2√b` is the optimiser of the candidate-2 family to leading order (grid argmax 0.0193 vs 0.0200 at b=1e-4, 0.00200 vs 0.00200 at b=1e-6) and gives `2b - 16 b^{3/2} + O(b²|log b|)`; `(2b-L)/b^{3/2}` = 14.70, 15.51, 15.82 at b = 1e-4, 1e-5, 1e-6. Candidate 1's `δ = b^{1/3}` gives `2b - O(b^{4/3})`: `(2b-L₁)/b^{4/3}` = 8.2, 15.5, 26.4, 39.3, 50.8 at b = 1e-2 … 1e-6, bounded and converging slowly towards the limiting constant 68 = 2·(2+32) of `2b(1-δ)²/(1+32δ(1-δ)²)` [reviewer expansion]; the O(b^{4/3}) claim is correct but weaker and superseded.
* Consistency controls: `L_c2 ≤ U_clip(b,t)` and `L_c2 ≤ U_square` (and `L_c1 ≤ U_square`) at all 21 tested (b,δ) pairs, b ∈ {1/16, 1/81, 1/256}; chain positive control with μ = `P_S` (`μ(K)=0.018647 ≥ rhs=0.005544` at b=1/10, δ=3/5; pointwise `f(y) = b μ(C_y)/|C_y|` holds with equality for `P_S`); negative controls: μ = Q (T=0) violates the chain (`Q(K)=0.002142 < b q₀|K| = 0.021421`), and the "naive" bound without TV correction, `2b(1-b)q₀`, EXCEEDS the exact upper bound of a genuine private law (`0.02321 > U_clip = 0.02137` at b=1/81) — so the TV-correction term is essential, not decorative.

**Verdict (lower bound, candidates 1–2): VERIFIED at written level; MINOR (shared representative lemma, §2.1).** Dependencies: definition of privacy in §1; TV = sup over sets.

## 4. Square-core upper law `P_S` (candidates 1–2)

* `|S+tD| = 1+4t+2t²` (exact hull areas at t = 1/3, 1/2, 1, 7/5, 3); shell k area `4k+2`; `Z_S = 1+6m+4m²` (rational identity `1 + 4b/(1-b)² + 2b/(1-b)`; partial sums).
* `n_S(x) = ⌈a₁+a₂⌉`, `k = ⌈a₁⌉+⌈a₂⌉-⌈a₁+a₂⌉ ∈ {0,1}`; `q/p_S = C b^k`, `C = Z_S/Z₁² = (1+4b-b²)/(1+b)² > 1`, `Cb < 1` for all b∈(0,1) (because `1+b-3b²+b³ = (1-b)(1+2b-b²) > 0`).
* `{k=1}` = triangle of area ½ in every outside unit cell pair; `Q(k=1) = 2m²/(1+2m)² = 2b²/(1+b)²`.
* `TV(Q,P_S) = Q(k=1)[1/(Cb)-1] = (1-Q(k=1))(1-1/C) = 2b(1-b)(1+2b-b²)/[(1+b)²(1+4b-b²)] = U_square` (both expressions agree exactly at five b; `U_square(1/10) = 2142/16819`, `U_square(1/2) = 14/99` as stated).
* **Brute-force TV** (reviewer's exact rational cell×shell integration, Sutherland–Hodgman clipping, tail bracket from the exact block mass): b=1/10: `U_square - tv_block = 4.281e-8 ∈ [0, 3.636e-7]`; b=1/3: `2.540e-6 ∈ [0, 1.694e-5]`; b=1/2: `9.864e-6 ∈ [0, 8.138e-5]`. Negative control: wrong normaliser `Z₁²` destroys the match (`tv_bad = 0`).
* `U_square = 2b - 10b² + O(b³)` (`(2b-U_square)/b² → 10.0000`).

**Verdict (square-core upper bound): VERIFIED exactly; no gap.**

## 5. Clipped-square upper law `P_t` (candidate 3; reused by candidate 4)

* `K_t = S ∩ {‖x‖₁ ≤ 1-t}`, `|K_t| = 1-2t²` (exact, four t); octagon with four axis edges of length `1-2t` (support `h_D = 1`) and four diagonal edges of length `t√2` (support `h_D = 1/√2`): mixed term `4(1-2t)+4t = 4-4t`; **`|K_t+kD| = (1-2t²) + (4-4t)k + 2k²`** verified exactly for t∈{1/10,1/8,1/4,2/5}, k∈{1/2,1,2,3}; negative control: the unclipped-perimeter formula `4k` differs at every tested point. Shell-k area `4k+2-4t`; `Z_t = (1-2t²)+(6-4t)m+4m²`.
* Inside S: `K_t` index 0, clipped corners index 1 (distance `t-(u+v) < 1`), so `P_t(S) = [A+b(1-A)]/Z_t`, `Q(S) = q₀`.
* Sign condition `q₀Z_t ≥ 1 ⇔ 2b-2b²-2t²-4bt+4bt²-2b²t²+4b²t ≥ 0`; with candidate 3's `t = (1-b^{1/4})√b`: `q₀Z_t-1 = 4b^{5/4}-6b^{3/2}+O(b^{7/4})` (reviewer expansion; numerically `3.44e-5` vs `4b^{5/4}=4e-5` at b=1e-4, `3.94e-10` at b=1e-8, matching the author's two reported points independently). It already holds at b=1/16 (`+0.0535`) and on the grid b=k/4000, k=1..3999 (float root rationalised) — no failure. Negative control: `t = √b` exactly violates it at every tested b (as the candidate's choice of a slightly smaller t anticipates).
* Outside S, reviewer's exact decomposition under the sign condition (not just O-bounds):
  `TV(Q,P_t) = [q₀ - (A+b(1-A))/Z_t] + (4-4t²)·b(q₀-1/Z_t) + 4t²·(bq₀ - b²/Z_t) + ∫_{Q-index≥2}(q-p_t)₊ =: E_clip(b,t) + R`, with `0 ≤ R ≤ Q(index≥2) = (8b²-4b³)/(1+b)²`.
  - one-axis strips inside `K_t+D` (index exactly 1): mismatch `b(q₀-1/Z_t) = b(q₀Z_t-1)/Z_t` per unit area, i.e. `O(b^{9/4})` for candidate 3's t and `O(b^{5/2})` for candidate 4's t ("both densities b[1+O(b)]" ✓);
  - strip ends outside `K_t+D`: for `x=(½+a, ±(½-u))`, `u<t`, the ℓ₁ distance to `K_t` is exactly `a+t-u` (nearest point `(½-(t-u), ½-u)`), so exclusion ⇔ `a > 1-(t-u)`; per strip end `∫₀^t (t-u)du = t²/2`, eight ends ⇒ **area exactly `4t²`** (exact clipping: `1/25, 1/16, 1/4, 16/25` at t = 1/10, 1/8, 1/4, 2/5), and these points lie in `K_t+2D` (index 2);
  - Q-index ≥ 2 tail: `1-q₀(1+4b) = (8b²-4b³)/(1+b)²`.
  So the explicit finite-b statement is **`T* ≤ TV(Q,P_t) ≤ U_clip(b,t) := E_clip(b,t) + (8b²-4b³)/(1+b)²` whenever `0<t<½` and `q₀Z_t ≥ 1`** — this supplies the "absolute constants" the candidates leave implicit.
* Brute-force TV (exact, 5–6 cells each side) with candidate 3's t: b=1/16: `E=0.0737996989 ≤ tv=0.0751695846 ≤ U=0.1006163079`, and `tv < U_square = 0.0933930644`; b=1/81: `0.0201859463 ≤ 0.0201997187 ≤ 0.0213683700` (`U_square = 0.0232353878`); b=1/256: `0.0069954043 ≤ 0.0069958508 ≤ 0.0071162899` (`U_square = 0.0076621427`). `(tv-E)/b³ ≈ 5.6–7.5`, i.e. the omitted index-≥2 positive part is O(b³), far below the O(b²) budget.
* Core deficit expansion (reviewer): `Q(S)-P_t(S) = 2b - 4bt - 18b² + 10bt² + O(b^{5/2})`; with `t=(1-b^{1/4})√b`: `TV ≤ 2b - 4b^{3/2} + 4b^{7/4} + O(b²)`, i.e. candidate 3's (5). Numerically `(2b-E_clip)/b^{3/2} = 3.65, 3.81, 3.92` at b = 1e-4, 1/160000, 1/6250000 (`4-4b^{1/4}` = 3.60, 3.80, 3.92).
* Candidate 4's choice `t = √b-2b` (>0 iff b<1/4): `q₀Z_t - 1 = 4b^{3/2} + O(b²)` (ratio `(q₀Z_t-1)/b^{3/2}` = 4.006, 4.018, 4.002, 4.0002 at b=1e-2…1e-8); sign condition holds on the grid b=k/4000, k=1..999 (all b<1/4), no failure; brute force at b = 1/16, 1/100, 1/400: `tv ∈ [E_clip, U_clip]` and `(tv-2b+4b^{3/2})/b² = 3.24, 3.62, 3.80`; exact `E_clip`: `(E_clip-2b+4b^{3/2})/b² = 3.56, 3.96, 3.996, 3.9996` at b = 1e-2, 1e-4, 1e-6, 1e-8. Hence **`TV(Q,P_{√b-2b}) = 2b - 4b^{3/2} + 4b² + O(b^{5/2})`** (reviewer refinement of candidate 4's `+O(b²)`).

**Verdict (clipped-square upper bound, both t choices): VERIFIED at written level; MINOR: thresholds/constants were implicit, now explicit via `U_clip`.**

## 6. Candidate 4 — second-order lower bound via nested essinf floors

Reconstruction (every step checked):
* (4): `e = (q₀-f)₊` on S, `∫_S e ≤ ∫(q-f)₊ = T`, `0 ≤ e ≤ q₀` ✓.
* (5): with the pointwise representative (§2.1), for `y` in corner σ with `d = 1-a-c`: `f(y) ≥ b·sup_{C_σ(d)} f ≥ b·ess sup_{C_σ(d)} f ≥ b·ess sup_{C_σ(d)}(q₀-e) = b(q₀ - h_σ(d))`, `h_σ(d) = ess inf_{C_σ(d)} e` ✓ (overlap `= C_σ(d)` exactly, control 5: equals depth `d`, not `d+1/10`). `h_σ` is nonincreasing (hence Borel), values in `[0,q₀]` ✓.
* (6) — stated tersely ("monotonicity of h and (4) imply"); the needed argument is: for each rational `d`, `e ≥ h_σ(d)` a.e. on `C_σ(d)`; off the countable union of exceptional null sets, a point of depth `s<½` satisfies `e(x) ≥ h_σ(d)` for all rational `d>s`, hence `e(x) ≥ h_σ(s+)`; `h_σ(s+) = h_σ(s)` except at countably many s; area element of depth is `s ds`; so `∫_{C_σ(½)} e ≥ ∫₀^{½} s h_σ(s) ds`. The four depth-½ triangles are pairwise disjoint up to null boundaries and inside S (exact clipping, control 4) ⇒ `Σ_σ ∫₀^{½} s h_σ ds ≤ T` ✓.
* (7) bathtub with increasing weight `w(s)=s` and cap `q₀`: `∫ s h ≥ H²/(2q₀)`, equality for `h = q₀·1_{[0,H/q₀]}` (400 random exact step functions, equality cases; negative control: `h = 3q₀` on `[0,1/20]` violates it, so the cap is essential) ✓. Monotonicity is not even needed here.
* Cauchy–Schwarz over four corners: `Σ H_σ ≤ √(4·2q₀ Σ M_σ) ≤ √(8q₀T)` ✓.
* (8): `∫₀^{½}(1-d)h ≤ H_σ`; for `d≥½`, `h_σ(d) ≤ h_σ(½)` and `∫_{½}^1(1-d)dd = 1/8`, while `M_σ ≥ h_σ(½)/8`; so `Σ ∫₀^1 (1-d)h_σ ≤ √(8q₀T) + Σ M_σ ≤ √(8q₀T) + T` ✓.
* (9): integrating (5) over the four outside triangles `K` (area 2, Q-density `b²q₀`), `∫_{K_σ} h_σ(1-a-c) da dc = ∫₀^1 (1-d) h_σ(d) dd` (exact band areas `((1-d₀)²-(1-d₁)²)/2`, control 4): `μ(K) ≥ 2bq₀ - b[√(8q₀T)+T]`, and `T ≥ μ(K) - 2b²q₀` ⇒ **`(1+b)T + b√(8q₀T) ≥ 2b(1-b)q₀`** ✓. Positive control μ = `P_S` (e constant `= q₀-1/Z_S > 0`): (6), (8), integrated (5) (with equality) and (9) all hold at b = 1/10, 1/3; negative control μ = Q (T = 0): (9) fails.
* (2): the quadratic in `√T` is increasing on `√T ≥ 0` and negative at 0, so (9) ⇔ `T ≥ s₀²`, `s₀ = 2B/(A+√(A²+4(1+b)B))`, `A = b√(8q₀)`, `B = 2b(1-b)q₀` ✓ (60-digit check: residual of (9) at `T=(2)` below 1e-50 at six b; `0.999·(2)` violates, `1.001·(2)` satisfies).
* Expansion (reviewer): `(2) = 2b(1-b)²q₀/[1+√b+b/2+…]² = 2b - 4b^{3/2} - 8b² + O(b^{5/2})`; independently recomputed diagnostics `[(2)-2b+4b^{3/2}]/b² = -7.778861, -7.977988, -7.997800` at b = 1e-4, 1e-6, 1e-8 — these coincide with the author's reported Decimal values, now reproduced by reviewer code.
* Consistency: `(2) ≤ TV(Q,P_S)` at b = 1/10, 1/3, 1/2 and `(2) ≤ TV(Q,P_t)` at b = 1/16, 1/100, 1/400 (brute force); `(2)` dominates the best candidate-2 bound at every tested b (ratio of deficits `(2b-L₂)/(2b-L₄)` → 3.95 ≈ 16/4).

**Verdict (candidate 4 lower bound): VERIFIED at written level; MINOR: (6) needs the countable-depth a.e. argument above; representative lemma §2.1.** The bound (2) holds for every b∈(0,1) and every full-D private μ, with no δ parameter.

## 7. Verdicts (as requested, separately)

1. **Lower bound (candidates 1–2, δ-family):** VERIFIED. Exact finite statement `T*(b) ≥ 2b(1-b)q₀(1-δ)²/[1+8b(1/δ+log δ-1)]` for all δ,b∈(0,1); `δ=2√b` ⇒ `T* ≥ 2b - 16b^{3/2} - O(b²|log b|)`. Candidate 1's `O(b^{4/3})` version is correct but superseded. MINOR: §2.1.
2. **Lower bound (candidate 4, essinf/bathtub):** VERIFIED. `T*(b) ≥ [2B/(A+√(A²+4(1+b)B))]²` for all b∈(0,1) `= 2b - 4b^{3/2} - 8b² + O(b^{5/2})`. MINOR: §2.1, §6 (6).
3. **Square-core upper bound:** VERIFIED exactly, `T* ≤ U_square(b) = 2b - 10b² + O(b³)`; brute-force TV agrees within the exact tail bracket at b = 1/10, 1/3, 1/2.
4. **Clipped-square upper bound:** VERIFIED. Explicit: `T* ≤ E_clip(b,t) + (8b²-4b³)/(1+b)²` for `0<t<½`, `q₀Z_t ≥ 1`. With `t=(1-b^{1/4})√b`: `2b - 4b^{3/2} + O(b^{7/4})` (candidate 3); with `t=√b-2b`: `2b - 4b^{3/2} + 4b² + O(b^{5/2})` (candidate 4, reviewer-sharpened).
5. **Θ(b^{3/2}) conclusion (candidate 3):** VERIFIED: `4b^{3/2} - O(b^{7/4}) ≤ 2b - T* ≤ 16b^{3/2} + O(b²|log b|)`.
6. **Second-order asymptotic (candidate 4):** VERIFIED: `T*(b) = 2b - 4b^{3/2} + O(b²)`. Reviewer refinement [INFERENCE from the verified expansions + exact controls, not an author claim]: the b² coefficient of `T*` satisfies `-8 ≤ liminf ≤ limsup ≤ 4`.
7. **Full privacy of the shell laws:** PROVED for `P_S` and every `P_t` (§2.2), pointwise for the closed diamond.

**Overall: no FATAL, no MAJOR. MINOR items M1–M4 below. Not INCONCLUSIVE.**

## 8. Findings

* **M1 (c1–c4):** the all-point bounded density representative is asserted, not proved; closed by §2.1 (or the Fubini-averaged form). Load-bearing for every lower bound.
* **M2 (c4 eq. (6)):** the passage from essinf floors to the first-moment inequality needs the countable-depth a.e. argument (§6); as written it is a one-clause assertion.
* **M3 (c3, c4):** "sufficiently small b", "absolute constants" are not quantified; the explicit finite-b bound `U_clip` and the polynomial sign condition make them effective (holds on the whole tested grid, including b=1/16).
* **M4 (c1 §4):** the "half-diamond radial upper `6840/19481`, `16/153`" comparison refers to a law outside the inputs; not verifiable here and not load-bearing.
* No claim of finite-b optimality, novelty, or exact b² coefficient is made by the candidates; none is granted here.

## 9. Control receipts (reviewer-written, from scratch; see directory)

| artifact | SHA256 | note |
|---|---|---|
| `reviewer-controls-c123-v1.py` | `a5eecf10426d5409511d6ce69645075746a48f97537f923405d6236f492b7541` | run start `2026-10-29T03:45:20Z`, end `03:45:26Z`; **196 PASS / 0 FAIL** (first run at `03:44:51Z` had 4 FAILs caused by a typo in the reviewer's own `Z_t` test expression, `(4-4t)m` instead of `(2-4t)m`; corrected, file hash above is the corrected version) |
| `reviewer-controls-c123-v1-output.txt` | `e0c8ca932569e70344b60b323537c2f3c5fae1cec10a5a4d95c1f00db30f3164` | |
| `reviewer-controls-c4-v1.py` | `a3f4e373e6a46aaac8a8215cebd06846aab1e6a2054e68abba99b4f5178ef943` | run start `2026-10-29T03:50:07Z`, end `03:50:12Z`; **60 PASS / 0 FAIL** |
| `reviewer-controls-c4-v1-output.txt` | `b10657b458632ac841f0697d2479b34319798731dc304f01bc223d14b36b44bd` | |

Positive controls: exact Minkowski areas, normalisers, closed-form/brute-force TV agreement within exact tail brackets, chain on μ=`P_S`, bathtub equality cases, root/threshold identity. Negative controls: unclipped-perimeter formula, `t=√b` sign violation, wrong normaliser, Q and half-width shells violating the index-jump property, Q violating the chain and (9), the naive no-TV-correction bound exceeding a genuine private law's TV, bathtub cap violation. Python 3.14.3, `fractions`/`mpmath` only. An additional one-off grid check (sign condition over b=k/4000) is recorded in the receipts file.

## 10. Scope statement

Same-harness written review by one reviewer; not human, not independent-family, not formal/kernel, not novelty clearance; no exact finite-b optimum, no J-functional statement, no statement about any held historical outcome is used or implied.
