# Review f118-privacy-occupied-cap-finite-dual — review-v1

**Kind:** INDEPENDENT_SAME_HARNESS_SCIENTIFIC_REVIEW (written review + reviewer-built controls).
**Observed clock before this file was written:** `2026-10-29T03:05:49Z` (= `2026-10-28T20:05:49-0700 PDT`, `/bin/date`).
**Verdict:** **MINOR only** — no FATAL, no MAJOR. Every load-bearing step of the candidate's written argument reconstructs; all rational/polynomial content is verified exactly; the transcendental content (π, arcsin) is verified by 50-digit evaluation of reviewer-derived closed forms (labelled diagnostic, not proof). No exact counterexample exists to any stated step; the negative controls confirm that the two steps a wrong proof would most plausibly break (occupied-cap accounting, sublevel containment) are genuinely load-bearing and are correctly handled.
**Not claimed here (per manifest):** no finite-b optimality, no novelty clearance, no formal/kernel proof, no human review, no independent-model-family review. Same-harness only.

## 0. Bindings (verified before reading)

| item | path | SHA-256 | bytes | LF |
|---|---|---|---|---|
| manifest | `.../review-waves/f118-privacy-occupied-cap-finite-dual/manifest-v1.json` | `f650d734052325037c8a33f673a2adf6b35505976e168becf2d1ee679d6ac481` | 1814 | — |
| input 1 (only input, read complete, `:raw`) | `.../parallel-18/privacy-diamond-mse/frontier-20261028-overlap-corrected-finite-dual-v1.md` | `d57a58caedd6efd0751c5a4c6059c5c86db31446811e08bab317531da7d124f3` | 5928 | 100 |

Read order honoured (manifest, then the single input, in full). The earlier candidate the author compares against (`frontier-20261028-finite-privacy-dual-bound-v1.md`, SHA `312c990f…`) is **not** in the manifest read order and was **not opened**; the strict-improvement claim is therefore checked only against the *explicitly reconstructed* looser root (§3.6 below), exactly as the manifest scope requires. No author code was executed (the input contains only printed floats, no code).

## 1. Setting as I reconstructed it (no author result assumed)

ε>0, b=e^{−ε}∈(0,1), κ≥0. D = closed ℓ1 unit diamond, |D|=2. Privacy: for every Borel A and every h∈D, μ(A) ≤ b^{−1} μ(A+h) (all-event, full closed diamond; D symmetric so both directions). φ(x)=|x|²+κ‖x‖₁, G(T)=∫_{ℝ²}(T−φ)₊, d=∫_Dφ, d(T)=∫_D(φ−T)₊. Claim (2): J+κL ≥ B with B the unique positive root of (1): (1−b)G(B)+2bB=bd.

## 2. Step-by-step written reconstruction and verdicts

| # | Candidate step | My reconstruction | Verdict | Control |
|---|---|---|---|---|
| 2.1 | All-event privacy ⇒ μ≪Leb with density ≤1/(2b) | ∫_Dμ(A+h)dh=∫|D∩(x−A)|dμ(x)≤|A| (Fubini); so 2μ(A)≤b^{−1}|A|. Null sets ⇒ μ-null ⇒ absolutely continuous; density ≤1/(2b) a.e. | correct (written) | measure-theoretic, no machine control |
| 2.2 | All-point representative p=limsup μ(B_ρ(x))/|B_ρ| obeys privacy pointwise, equals density a.e., p≤M everywhere | limsup of μ(B_ρ(x))≤b^{−1}μ(B_ρ(x+h)) gives p(x+h)≥b p(x) for every x, h∈D; Lebesgue differentiation gives p=density a.e. (so p is Lebesgue-measurable); μ(B_ρ(x))≤M|B_ρ| gives p≤M everywhere | correct (written) | none |
| 2.3 | Near-peak x0 with p(x0)≥(1−η)M; floor ℓ=(1−η)bM on E=x0+D | {density>(1−η)M} has positive measure and p=density a.e. ⇒ such x0 exists; p(x0+h)≥b p(x0)≥ℓ for all h∈D (closed) | correct | none |
| 2.4 | (4): 0≤g=p−ℓ1_E≤M−ℓ1_E, ∫g=1−2ℓ | holds **everywhere** (not just a.e.); cap function M−ℓ1_E ≥ M−ℓ = M(1−(1−η)b) > 0; 2ℓ ≤ (1−η)·2bM ≤ (1−η) < 1 since M≤1/(2b) | correct | S4.a (admissible densities obey these constraints and V≥B) |
| 2.5 | Capped bathtub: ∫φg ≥ T(1−2ℓ)−MG(T)+ℓ∫_E(T−φ)₊ | (φ−T)g ≥ −(T−φ)₊g ≥ −(T−φ)₊(M−ℓ1_E) pointwise, integrate | correct | S4.b negative (over-tight cap M−2ℓ is refuted) |
| 2.6 | (5): add floor ℓ∫_Eφ, combine | ℓ[∫_E(T−φ)₊ + ∫_Eφ − 2T] = ℓ∫_E[(T−φ)₊+φ−T] = ℓ∫_E(φ−T)₊ using |E|=2 | correct, exact identity | S4.b negative (forgotten floor mass is refuted) |
| 2.7 | Translate minimizer: ∫_{x0+D}(φ−T)₊ ≥ ∫_D(φ−T)₊ | ψ=(φ−T)₊ even and convex (φ even convex, (·−T)₊ convex nondecreasing); x0↦∫_Dψ(x0+h)dh convex (integral of convex translates) and even (D symmetric); f(x0)=(f(x0)+f(−x0))/2≥f(0) | correct | S5 exact polygon-clipping: strict increase at 8 nonzero shifts × 3 levels, evenness, midpoint convexity |
| 2.8 | (6) and unique positive root of G(T)=b d(T) | G strictly increasing on T>0 (G′=|{φ<T}|>0), d(T) continuous, nonincreasing (strictly decreasing only on [0,1+κ], then 0), G(0)−bd<0, →+∞ | correct (wording "decreases" slightly loose, see MINOR-2) | S4.a: h_L(B_lo)<0<h_L(B_hi) |
| 2.9 | η→0 gives (2) | at T=B: J+κL ≥ B − ηbM d(B); M fixed, B independent of η | correct | — |
| 2.10 | (7): G(T)−d(T) ≥ 2T−d | G≥∫_D(T−φ)₊ and (T−φ)₊−(φ−T)₊=T−φ; equality iff {φ<T}⊂D | correct | S1.g exact (L-only): equality for T≤1, slack (2/3)(T−1)²(T+2) beyond; S2.f (κ=0, T=1/3) to 1e-25 |
| 2.11 | B ≤ d/2 < κ+1/2 | G(d/2)−b d(d/2) ≥ (1−b)d(d/2) ≥ 0 and the root function is strictly increasing. In fact **strict**: at T=d/2 the sublevel is inside D, so (7) is an equality and G(d/2)−b d(d/2)=(1−b)G(d/2)>0. d/2=1/3+2κ/3<1/2+κ. | correct (candidate's "≤" is the weaker true statement) | S1.d, S1.h (16/81 exact), S6.b |
| 2.12 | {φ≤B}⊂D | ‖x‖₁>1 ⇒ |x|²≥‖x‖₁²/2>1/2 ⇒ φ>1/2+κ>d/2≥B | correct | S1.j exact Cauchy–Schwarz; S6.c |
| 2.13 | d(B)=d−2B+G(B) ⇒ (1) | ∫_D(φ−B)₊=∫_D(φ−B)+∫_D(B−φ)₊ and the last equals G(B) **only because of 2.12** | correct; containment is load-bearing | S1.i (fails at T=3/2), S7 negative (rectangle) |
| 2.14 | Root of (1) unique, equals the dual root | Φ(T)=(1−b)G(T)+2bT strictly increasing from 0 to ∞ | correct | S4.a, S6.b |
| 2.15 | Strict improvement over looser root G(B_old)+2bB_old=bd | Φ(B_old)=bd−bG(B_old)<bd ⇒ B>B_old. I reconstructed the looser root independently: with residual cap M on E as well, the dual is T+M[(1−η)b(d−2T)−G(T)], root G+2bT=bd. | correct | S2.a, S4.a (exact), S6.b |
| 2.16 | (3) at κ=0 | G=πT²/2 (polar, exact); quadratic (1−b)πB²+4bB−4b/3=0; rationalized with (√(b²+c)−b)(√(b²+c)+b)=c, c=(π/3)b(1−b) | correct; limits 1/3 (b→1) and (2/√(3π))√b (b→0) verified | S2.a–S2.d |
| 2.17 | §5 floats | reproduced from my closed forms to <4e-17 at all four b | consistent | S2.e |
| 2.18 | (8) | feasibility ⇒ B≤J+κL≤H; Φ increasing ⇒ Φ(H)≥bd ⇔ b≤G(H)/(d−2H+G(H)), denominator >0 since H<d/2. (Sublevel containment at H is *not needed* for (8).) | correct | S3.b exact (300 random) |
| 2.19 | G(H)≤2H³/(3κ²) | φ≥κ‖x‖₁ ⇒ (T−φ)₊≤(T−κ‖x‖₁)₊; substitution y=κx; ∫(T−‖y‖₁)₊=∫₀ᵀ2s²ds=2T³/3 | correct | S1.f exact; S6.a (closed-form G_κ ≤ bound, and ≥ a lower bound t⁴+(2κ/3)t³) |
| 2.20 | (9) with κ=2r/(1−6r) | H=3ℓr(1−2r)/(1−6r), d−2H=(2/3)(1−2r)(1−9j)/(1−6r) (so H<d/2 ⇔ j<1/9 exactly), 2H³/(3κ²)=(9/2)ℓ³r(1−2r)³/(1−6r); t/(d−2H+t) increasing; ratio simplifies exactly to ℓ³F(r)/(1−9j+ℓ³F(r)), F(r)=27r(1−2r)²/4 | correct; strictly below the looser form ℓ³F(r)/(1−9j) for j>0 | S3.c–S3.e exact at 141 (r,ℓ) points (27 r × 8 ℓ exceed all cross-multiplied degrees ⇒ polynomial identity) |
| 2.21 | (10) L-only | d=4/3, G=2T³/3, root≤2/3<1 so containment holds; ratio = ℓ³/(2−3ℓ+ℓ³), denominator (ℓ−1)²(ℓ+2)>0; equals 1 at ℓ=2/3 (vacuous boundary) | correct | S3.f, S3.g exact |
| 2.22 | (11) κ=0 | (πj²/2)/(2/3−2j+πj²/2) ×6/6 = 3πj²/(4−12j+3πj²); denominator >0 for j<1/3 (indeed for all j: discriminant 144−48π<0) | correct | S3.h exact coefficients, S3.i–j |
| 2.23 | "(9)–(11) strictly improve … whenever budgets positive and denominators have stated signs" | each new denominator = looser denominator + a strictly positive term | correct relative to the reconstructed looser forms | S3.e, S3.f, S3.i |

Uniformity scope: (2) holds for each fixed (b,κ) uniformly over **all** all-event closed-diamond-private laws, including those with J or L infinite (trivially). (8)–(11) are necessary conditions on budget pairs (j,ℓ) for feasibility at privacy b; they are not sufficiency or optimality statements, exactly as the candidate says.

## 3. Findings

**FATAL:** none. **MAJOR:** none.

**MINOR (presentation only; nothing changes the mathematics):**
1. Notation clash: `ell` denotes the floor level ℓ=(1−η)bM in §2 and the L-budget in §4 and (9)–(10). A reader can misread (9)'s ℓ³F(r) as the floor level.
2. §2: "d(T) decreases continuously from d>0 to 0" — d(T) is nonincreasing, strictly decreasing only on [0, 1+κ] and identically 0 afterwards; uniqueness of the root is unaffected because G is strictly increasing.
3. §4: "The same sublevel containment applies at H" is true but not used in deriving (8); only monotonicity of Φ and d−2H>0 are needed.
4. §1: the characterization "it forgot that the residual cap is lower…" refers to a document outside the read order; I verified only that the *reconstructed* cap-M-everywhere dual has root G+2bT=bd and is strictly weaker.
5. §5: the example coefficients 121/512, 25/64, 49/108 are F(r) at r=1/24, 1/12, 1/9 respectively; the r values are not stated.
6. §3: "B≤d/2" can be sharpened to B<d/2 (2.11); "φ(x)≥1/2+κ" outside the closed diamond is in fact strict.
7. §2 (4): "almost everywhere" is weaker than what holds (everywhere, for the all-point representative); harmless.

**Observations (not defects):** (i) As b→1 the bound stays ≤ d/2 while no probability law is invariant under all diamond shifts; so the bound is far from tight near b=1 — consistent with the candidate's explicit "necessary lower bound, not finite-b exactness". (ii) Diagnostic only: an explicit ε-private staircase family (core diamond of radius δ, density M b^k on successive ℓ1 shells) reaches J/B₀≈4.2 at b=0.01, L/B_L≈1.9, so the bound is not vacuous at small b; this is not an optimality statement. (iii) The dual bound equals the exact minimum of the *relaxed* problem {0≤p≤M, p≥bM on D, ∫p=1} minimized over M (V(B)=B identity, S4.a/S6.b); any strengthening must use more of the privacy constraint than the floor and cap.

## 4. Controls actually run (reviewer-built; receipt)

**Script:** `reviewer-f118-controls-v2.py`, SHA-256 `084f821299bef8684ed6d7d017f43242979688decbdc09f270e0f5fe55387209`, 36253 B. Exact arithmetic = `fractions.Fraction`; `mpmath` 1.4.1 at 50 digits for labelled diagnostics; `mp.quad` only to cross-check reviewer-derived closed forms (kink-split), never as proof of an inequality. Python 3.14.3, macOS 27.0.1 arm64. No package was installed; no author code executed.
**Run (single successful run):** pre-run `/bin/date` `2026-10-29T03:04:34Z`; script clock start `2026-10-29T03:04:34.894920+00:00`, end `2026-10-29T03:04:41.154536+00:00`, elapsed 6.26 s; post-run `/bin/date` `2026-10-29T03:04:42Z`. **44 checks, 44 PASS, 0 FAIL.**
**Outputs:** `reviewer-f118-controls-output-v2.txt` SHA `880b6816f374781842c6f867502729052885b34c381e0b6f4a67d9992cb3f0b7` (11738 B); `reviewer-f118-receipt-v2.json` SHA `94042148c45395c7a58cb4161856a0976bc30859d7e0822194b1d5991f20cee6` (14838 B; embeds script/input/manifest SHAs, clocks, all 44 check records).

Control inventory (S-labels as in the output):
- S0 bindings; S1 exact diamond integrals (d=2/3+4κ/3, |D|=2, G_L=2T³/3, scaling 2T³/(3κ²)), (7) exact, containment identity holds/fails exactly where it should, Cauchy–Schwarz.
- S2 (diagnostic, 50 digits): (3) solves (1) with |res|<1e-45; explicit quadratic root = rationalized form to 1e-44; limits; §5 floats reproduced; d₀(1/3)=π/18 to 1e-25.
- S3 exact: (8) equivalence (300 random), (9) identity at 141 points, premise j<1/9 ⇔ H<d/2, strictness vs looser forms, (10) denominator factorization, (11) coefficients.
- S4 exact (L-only, 90-step rational bisection): B<2/3, root identification, B_old<B at six b; 403 explicit admissible densities per b all cost ≥B with min at fill level t=B (V(B)=B); **negative controls**: an over-tight cap (M−2ℓ on E) and a forgotten floor mass (∫g=1) each produce a "bound" exceeding the cost of an explicit admissible density (e.g. b=1/10: B=0.4293, wrong-cap 0.4398, wrong-mass 0.6057, explicit density costs 0.4293).
- S5 exact polygon clipping: ∫_{x0+D}(‖x‖₁−T)₊ reproduces d_L(T) at x0=0 (independent of the layer-cake formula), strictly larger at every nonzero shift tested, even, midpoint-convex.
- S6 (diagnostic): reviewer closed form G_κ(T)=πU⁴/2−2U⁴asin(a/U)−(10a/3)W³−2a³W+4a²U²−8a⁴/3 (a=κ/2, U²=T+2a², W²=U²−a²) cross-checked against two independent 1-D quadratures (<1e-30) and derivative; for b∈{.01,.1,.5,.9}×κ∈{0,.1,.5,1,3}: B>B_old, B<d/2<κ+1/2, V(B)=B to 1e-40; root of (1) also solves G=b·∫_D(φ−T)₊ with the kinked integral computed to 1e-25.
- S7 exact **negative sublevel control**: for the rectangle D′=[−2,2]×[−1/4,1/4] (|D′|=2, L-only) containment fails (true dual root 0.849>c=0.25 at b=1/2); the (1)-form root (0.8900) exceeds the true dual root (0.8492) and is refuted by an explicit admissible density costing 0.849180; all explicit densities still cost ≥ the true dual root. Hence the candidate's containment lemma is exactly what licenses the reduction to (1), and it holds for the diamond.
- S8 exact **positive control**: explicit ε-private staircase laws (privacy verified: shell index moves ≤1 under any ℓ1 shift ≤1, 2000 random exact pairs) with exact rational J, L for 4 b × 5 δ all satisfy L≥B_L (exact), J≥B₀ (exact with π>3.14159265358979), M≤1/(2b), and J+κL≥B_κ for κ=1/2,1 (diagnostic); product-Laplace law likewise. No counterexample found.

**Failed first attempt (preserved, not deleted):** `reviewer-f118-controls-v1.py` SHA `4555b0c43718f0c33868d5d7588c2fb11cefc3c3a56de4e0fb1222090407f1a0` was run once at `2026-10-29T03:03:27Z`; its S2.b check (`mp.polyroots`) raised `NoConvergence` at b=0.999999 after 13 passing checks — a reviewer-tooling defect, not a mathematical finding. Partial record: `reviewer-f118-controls-output-v1.txt` SHA `d6b6a4bb34d710074c73e7e3735afa8d764c3b9d31138ddeaaeaddcc28c9863e` (24 lines). v2 differs from v1 only in that check (explicit quadratic formula), the header comment, and the output/receipt file names (diff recorded in the session; three hunks).
**Known cosmetic defects of the v2 run (disclosed):** the first banner line of the output still prints the string `reviewer-f118-controls-v1.py` (the `self_sha256` line correctly binds v2); and the process exit code was 120 because Python's shutdown flush touched the explicitly closed Tee file after the summary and receipt were fully written. Neither affects any check.

## 5. Status statement

Written analysis complete for every equation (1)–(11) and every unnumbered load-bearing claim of the input, with independent reconstruction and the controls above. Status at this scope: **MINOR only; no FATAL/MAJOR; no INCONCLUSIVE item remains**. Conditionality: the measure-theoretic steps 2.1–2.3 and 2.9 are verified as written mathematics only (standard analysis; no machine control possible). This review is same-harness and grants no human, independent-family, kernel/formal, or novelty clearance and makes no finite-b optimality claim.
