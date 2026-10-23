# Minimal SCV of ME(≤3) — integration proof, version 3 (worker candidate)

Worker `MathPhaseType3`, lane `mathematics/evidence/six-lane-20261016/me3-minimum-scv/`, 2026-10-18 PDT.

**Status.** This is a worker candidate. It is unreviewed by the parent and by the hostile reviews, and the parent's
independent replay is still pending. Correctness only: no novelty, priority or "first" claim. v1
(`proof/me3-theorem-v1.md`, sha 3ec36afa…8593) and v2 (`proof/me3-theorem-v2.md`, sha 1fcbca21…ef25) are kept
unchanged. v3 differs from v2 only in the title, this status paragraph and the independent-replay bullets of §7.
v2 quoted an interim replay margin and had the G replay still pending; v3 records the final results from
`reductions/replay/REPLAY-STATUS-v2.md` (sha af02cc29…14fd).

**Scope.** This is the frozen contract's statement: HSTZ 2016 Definitions 1, 2 and 5, with the constant v_cos
defined as the minimum over the cos family. It is the separately published ME(3) conjecture, and not the book's
general minimal-representation question.

## 0. Statement

**Theorem.** Every continuous X ∈ ME(≤3) satisfies SCV(X) = m₀m₂/m₁² − 1 ≥ v_cos, where
v_cos := min_{ω>0, φ∈ℝ} SCV(e^{−t}(1 − cos(ωt − φ))). The minimum is attained in the cos family (case D1).
Densities with only real exponents have SCV ≥ Δ₃ > 0.2765. Every density in a strictly-dominant-real-pole cone
(case D2) has SCV > v_cos.

**Proof architecture.**
* Written reductions (§1, imported from `reductions/`; proved by the subagent `ME3Reductions` and re-read here).
* Two elementary written lemmas: Lemma D (§2) and the Lemma M continuation argument (§3).
* Seven certified ball-arithmetic computations over compact charts that together cover every D2 pole
  configuration. Each has an exact-rational leaf record and an independent geometric coverage audit (§4).

Imports: finite-dimensional convexity, the mean value theorem, Taylor's theorem with integral remainder, power
series of log, and the correctness of Arb ball arithmetic (python-flint 0.9.0, 128-bit working precision).

## 1. Reductions imported

Source: `reductions/proof/reductions-v1.md`, sha ad6c5091da11c6f236e24d7fb0dc389b2ef99045b50141411d62dc748dd45536,
together with `reductions/STATUS.md`, sha 61776330…2c76, which holds the run hashes.

* **L1–L2.**
  * Continuous ME(≤3) densities are exactly the normalized nonzero elements of the cones K_E of nonnegative
    exponential polynomials with admissible exponent multisets |E| ≤ 3.
  * SCV is invariant under scaling and time scaling.
  * SCV/(1+SCV) = min_θ R_θ, with R_θ(f) = ∫(t−θ)²f/(θ²∫f) (Lemma 2.2).
  * The infimum over K_E∖0 is attained on an extreme ray (Lemma 2.4).
  * Assembly (Cor. 2.6): the infimum over ME(≤3) equals min(I_R, I_1, I_2).
  * Lower-order laws are covered by the inclusion K_E ⊆ K_{E′} (Lemma 2.5). The outline's "face" claim is false.
* **L3–L4.** With real exponents, SCV ≥ Δ₃ ∈ (0.2765825307809456, 0.2765825307809457). An exact identity gives
  Δ₃ > 1/4.
* **L5.**
  * The D1 extreme rays are the cos family, so I_1 = v_cos.
  * The minimum is attained (Thm 5.6).
  * Certified bounds: 0.20090156350055 ≤ v_cos < U = 0.20090156350055695880138068… (runs ctl-c-v2, ctl-f-main-v1).
* **L6.** In D2 (real pole 1, pair 1 + ξ and 1 + ξ̄, ξ = δ − iω, δ, ω > 0, r = δ/ω):
  * the extreme rays are e^{−t}h_τ, with φ = ωτ ∈ [0, θ₁(r)];
  * θ₁ is C¹ and strictly decreasing, from 2π (r → 0⁺) to π (r → ∞);
  * the moments are m_k = k!(1 − Re(cζ^{k+1})), with c = (1 − ir)e^{(r−i)φ} and ζ = 1/(1 + δ − iω).

Fixed constants: T := 11/50, κ := 1/(1+T) = 50/61, ρ := T/(1+T) = 1 − κ. Note that v_cos < U < T.

## 2. Lemma D (elementary dual sufficient condition)

Fix δ ≥ 0 and ω > 0, and let ξ = δ − iω. Every f in the cone K with exponents {−1, −(1+ξ), −(1+ξ̄)} has the form
f = e^{−t}H with H(t) = a + Re(ce^{−ξt}) ≥ 0 on [0, ∞), and a ≥ 0. (If δ > 0, let t → ∞. If δ = 0, average H over
one period.) Let Q_T(y) := (κy² − 2y + 2)/y³. Then Q_T(y) > 0 for y > 0, because κ > 1/2.

**Lemma D.** Suppose that for every θ > 0, W(θ) := Q_T(θ(1+ξ))/Q_T(θ) is a finite combination Σλ_k e^{−ξt_k}
with λ_k ≥ 0, Σλ_k ≤ 1 and t_k ≥ 0. Then SCV(f) ≥ T for every f ∈ K∖0.

*Proof.*
1. With q_θ(t) := (t−θ)² − ρθ², we have ∫₀^∞ q_θ e^{−zt} dt = θ³Q_T(θz) for Re z > 0. Hence
   ∫q_θ f = θ³Q_T(θ)·[a + Re(cW)].
2. Now a + Re(cW) = (1 − Σλ_k)a + Σλ_k H(t_k) ≥ 0.
3. Therefore R_θ(f) ≥ ρ for every θ, and Lemma 2.2 gives SCV ≥ T. ∎

Certificate forms (each is an explicit finite combination; no closure or limit is used, and the weight on 0 is
justified by a ≥ 0):
* RADIAL: there is an argument α ≥ 0 of W, of any branch, with |W| ≤ e^{−δα/ω}. Take t = α/ω and
  λ = |W|e^{δα/ω} ≤ 1. W = 0 is trivially admissible. If g is a continuous logarithm of W along a path and
  Im g ≥ 0, then α = Im g is admissible, and the condition reads Φ := ω Re g + δ Im g ≤ 0.
* SMALL: |W| ≤ e^{−2πδ/ω}. This is RADIAL with α = Arg₊ ∈ [0, 2π).
* TRIANGLE: W = a′ + b′e^{−ξt′}, with a′, b′ ≥ 0, a′ + b′ ≤ 1 and t′ ≥ 0.

Parametrization. Put s = θ/(1+θ) ∈ (0, 1), N₁ = κs² − 2s(1−s) + 2(1−s)² > 0 and zz = 1/(1+ξ). Then
W = zz(w₁ + zz(w₂ + zz·w₃)), with w₁ = κs²/N₁, w₂ = −2s(1−s)/N₁ and w₃ = 2(1−s)²/N₁. (Multiply N(θz)/(N(θ)z³) by
(1−s)².) Boxes may contain s ∈ {0, 1}; their enclosures still contain the true values for every s ∈ (0, 1).

## 3. Lemma M and the continuation argument (primal chart P)

Let R_P := [0, 3] × [1/5, 40] × [0, 31416/5000] in (r, ω, φ). For feasible points let S(r, ω, φ) be the SCV of the
extreme ray: e^{−t}h_{φ/ω} if r > 0, and the D1 ray if r = 0. The closed-form moments are analytic in (r, ω, φ),
including at r = 0. With a_k = m_k/k!:
* 1 + S = 2a₀a₂/a₁²;
* ∂_r log(1+S) = D/(a₀a₁a₂), where D := a₀′a₁a₂ + a₀a₁a₂′ − 2a₀a₁′a₂;
* a_k′ = −Re(cζ^{k+1}[φ + (r−i)/(1+r²) − (k+1)ωζ]), an exact sympy identity (run v01).

**Certificate.**
* Run c03 used spec `code/spec_primal_P_v1.json`, sha 6339c775…759c, frozen before the run. It tiles R_P into
  945,680 closed boxes, each of which is INFEAS (no feasible point: φ > θ₁(r) everywhere), SGE (S > T everywhere)
  or DPOS (a₀, a₁, a₂ > 0 and ∂_r S > 0 everywhere).
* Counts: SGE 891,318; DPOS 8,018; INFEAS 46,344; FAIL 0.
* Independent audit a01 replays the split rule from geometry alone: tiling_ok.
* The DPOS leaves lie in r ≤ 0.2344, ω ∈ [0.5887, 1.6614] and φ ≤ 0.7363 (bounding box).

**Lemma M.** For every feasible (r₀, ω₀, φ₀) ∈ R_P with r₀ > 0, S(r₀, ω₀, φ₀) > v_cos.

*Proof.*
1. If S(r₀, ω₀, φ₀) ≥ T we are done, since T > v_cos. Otherwise put σ(r) := S(r, ω₀, φ₀) on [0, r₀]. These points
   are feasible: for 0 < r ≤ r₀ we have φ₀ ≤ θ₁(r₀) ≤ θ₁(r) because θ₁ is decreasing, and r = 0 is D1. They also
   lie in R_P. The function σ is continuous on [0, r₀] and C¹ on (0, r₀].
2. Let J := {r : σ < T on [r, r₀]} and r* := inf J.
3. For r ∈ (r*, r₀], any leaf box containing (r, ω₀, φ₀) contains a feasible point with S < T. So it is neither
   INFEAS nor SGE, hence it is DPOS, and σ′(r) > 0. Thus σ is strictly increasing on (r*, r₀].
4. If r* > 0, continuity gives σ(r*) ≥ T, while monotonicity gives σ(r*) ≤ σ(r₀) < T, a contradiction. So
   r* = 0, and σ(r₀) > σ(0) = SCV(e^{−t}(1 − cos(ω₀t − φ₀))) ≥ v_cos. ∎

## 4. Far region: six dual charts, all certified

The specification is `proof/charts-spec-v1.md` (sha 5a43c252…1ff1), together with `code/spec_dual_v1.json`
(sha 23dd1dad…f6c1; receipt `receipts/spec-dual-freeze-v1.json`, sha 69f60dc5…40c4, frozen at 04:41:52) and, for
SWC only, `code/spec_dual_v2.json` (sha d9b490ef…8930; receipt `receipts/spec-dual-freeze-v2.json`, sha
60c540ad…cfe1, frozen at 04:50:47).

**Implementation change, SWC chart.**
* The corner series coefficients use p = (s(1−s)(1 + i√(2κ−1)) − κs²)/N₁. This equals the spec text's
  (−A + i√(4B − A²))/2, because 2Re p = −A and |p|² = B. It avoids a square root of a ball whose radicand 4B − A²
  suffered cancellation near s = 1.
* The failing calibration attempts are kept: k04 (spec root) and k03 (linear recurrence).
* Library `code/me3dual_v8.py`, sha 5f3e7675…d1ea; driver `code/cert_dual_v6.py`, sha abffeefd…7339.
* The other dual charts ran `code/cert_dual_v5.py` + `code/me3dual_v7.py`. Their tests are those of
  `me3dual_v6.py`/`v4.py`/`v3.py`, as listed in the spec.

| Chart | Assigned pole set (δ, ω) | Run | Leaves (outcomes) | Evals | Audit (tiling_ok) | leaves.txt.gz sha256 |
|---|---|---|---|---|---|---|
| P (primal) | ω ∈ [1/5, 40], δ ≤ 3ω | c03-primalP | 945,680 (SGE 891,318 / DPOS 8,018 / INFEAS 46,344) | 1,829,920 | a01-coverP ✓ | b2773bab… |
| G | δ ∈ [0, 64], ω ∈ [1/5, 640], minus P | d01-G | 20,579,480 (radial 10,348,560 / small 10,202,984 / radial-mvf 8,385 / SKIP-in-P 19,551) | 41,152,160 | b01-cover-G ✓ (19,551 SKIP rules re-checked) | 565c8d41… |
| SWB | δ ∈ [3/10, 64], 0 < ω ≤ 1/5 | d01-SWB | 8,196,408 (bedge 8,144,675 / bedge-mvf 51,733) | 16,392,304 | b01-cover-SWB ✓ | 05117eee… |
| SWC | δ ∈ [0, 3/10], 0 < ω ≤ 1/5 | d02-SWC | 34,304 (corner 815 / corner-mvf 33,489) | 68,512 | b02-cover-SWC ✓ | 0b0f7640… |
| LW | δ ∈ [0, 64], ω ≥ 640 | d01-LW | 1,250 (small) | 2,388 | b01-cover-LW ✓ | 16f11db8… |
| LD1 | δ ≥ 64, all ω, s ∈ [1/16, 1] | d01-LD1 | 5,954 (ld1) | 11,803 | b01-cover-LD1 ✓ | 2d1fbe94… |
| LD2 | δ ≥ 64, all ω, s ∈ [0, 1/16] | d01-LD2 | 57,813 (ld2 56,933 / SKIP 880) | 115,570 | b01-cover-LD2 ✓ (880 SKIP rules re-checked) | 1454e031… |

All seven have certificate_ok = true, with 0 FAIL and no evaluation cap reached. The certificate index is
`runs/i01-index/certificate_index.json` (sha edb78933…7b0e). It lists for each run the spec hash, the code hashes
taken from the pre-run receipt, the leaf-file hashes, wall time, max RSS and the audit result. All counts match the
audits.

**Coverage of the D2 pole set.**
* δ ≥ 64: LD1 ∪ LD2.
* δ < 64 and ω ≥ 640: LW.
* δ < 64 and ω ∈ [1/5, 640]: P, if ω ≤ 40 and δ ≤ 3ω; otherwise G.
* δ < 64 and ω < 1/5: SWC (δ ≤ 3/10) or SWB (δ ≥ 3/10).

Every dual chart covers s ∈ [0, 1], hence every θ > 0. In each dual chart, every certified leaf gives, for every
point (s, δ, ω) of its box, one of RADIAL, SMALL or TRIANGLE (the justifications are in charts-spec-v1.md). By
Lemma D, every density with poles in a dual-assigned configuration has SCV ≥ T > v_cos.

## 5. Assembly

Let X be a continuous ME(≤3) law.
* Real exponents: SCV ≥ Δ₃ > U > v_cos.
* Otherwise, after time scaling, X lies in a D cone (δ ≥ 0, ω > 0).
  * D1 (δ = 0): SCV ≥ v_cos by definition.
  * D2 configurations in a dual-assigned set: SCV ≥ T > v_cos.
  * The remaining D2 configurations (ω ∈ [1/5, 40], r ≤ 3): by L2 the cone minimum is attained on an extreme ray,
    and by Lemma M it exceeds v_cos.
* Attainment: L5 Theorem 5.6. ∎

## 6. Correctness dependencies and limits

* **Certified computations.** They rely on four things: Arb's outward-correct ball arithmetic; the code implementing
  the stated formulas (the derivative is checked by an exact sympy identity, v01, and the moments by 40-digit
  quadrature, v01); the deterministic split rule; and the frozen specs.
* **Coverage.** Each leaf record is audited by code that does not evaluate any test. The parent will rebuild the
  evaluators from the definitions.
* **Data.** About 101 MB of leaf records (all compressed).
* **Not done.** No Lean or kernel check, and no human referee. This is not the book's general question.

## 7. Controls and replays

* **Negative controls, run n01** (`runs/n01-controls/controls.json`, sha 3ea93340…88a6). Each fails for the intended
  reason:
  * M1: the primal chart without DPOS FAILs near the D1 optimum (1024 FAIL boxes; S < T there).
  * M2: with the derivative sign flipped, it FAILs.
  * M3: the dual GENERAL test FAILs inside the valley.
  * M4: the corner chart with T′ = 3/10 > Δ₃ FAILs.
  * M5: the INFEAS predicate never fires on boxes that contain feasible points.
  * M6: the same small primal region with DPOS is certified.
* **Audit mutants, n02/n03.** A dropped leaf, a FAIL label, a flipped path bit and a false SKIP are each rejected
  by `check_cover_v2.py`.
* **Independent replay by ME3Reductions.** Final status: `reductions/replay/REPLAY-STATUS-v2.md`, sha
  af02cc293f26722a8b7304aac5f305d3e173af766e892fef4e83493247b514fd. This is a point-evaluation smoke test (mpmath,
  50 digits), not a certificate. The evaluators were written from the definitions (reductions-v1 Lemmas 6.4–6.6;
  the Lemma D statement and the charts-spec-v1 maps) and import nothing from the lane code. All its runs were
  launched through `code/run_v1.sh` with pre/post receipts.
  * Primal, 948 sampled leaves (midpoint, 8 corners and 26 extra points each): 0 violations. Minimum margins:
    S − T ≥ 0.011273 on SGE leaves (30,409 feasible points); ∂S/∂r ≥ 0.0983 on DPOS leaves; φ − θ₁ ≥ 4.23e−4 on
    INFEAS leaves. ∂S/∂r agrees with central differences, and at 24 points the closed-form moments match direct
    quadrature to 9e−30.
  * Primal, all 945,680 c03 leaves (`runs/rp-primal-full-v2`), using its own box rebuild:
    * The rebuild reproduces the 948 sample boxes exactly, and the leaves tile all 61,440 cells.
    * SGE: min S − T = 0.0078155 over 861,780 feasible midpoints.
    * DPOS: min ∂S/∂r = 0.0801 over 72,162 points.
    * INFEAS: each leaf passes at its worst corner (r_lo, φ_lo) at 50 digits; min g − 1 = 1.58e−4.
  * Dual samples, 0 violations in every chart. The exact spiral-hull membership test (radial, or chord when
    α > θ₁) agrees with a 2880-direction support-function check; every point fell in the radial branch.
    | Chart | Boxes | Points | Min margin |
    |---|---|---|---|
    | G | 1025 + 3 SKIP | 35,875 | 0.0289 |
    | SWC | 353 | 12,148 | 6.2e−9 |
    | SWB | 1000 | 34,892 | 4.6e−3 |
    | LW | 23 | 778 | 0.868 |
    | LD1 | 112 | 3,767 | 0.346 |
    | LD2 | 1072 + 18 SKIP | 37,324 | 0.0288 |
  * All SKIP boxes satisfy their exact skip rules. One G SKIP box is exactly on the P boundary,
    δ_hi = 3ω_lo = 51/80, which is allowed because P is closed.
  * The SWC margin is tiny at δ = ω → 0, where W → 1. That is the expected corner degeneracy, which the
    certified corner series handles analytically. It is not a near-violation.
  * Mutation controls: 3 bad primal boxes gave 105/105 violations, and a dual box with |W| = 1.014 was flagged
    at 35/35 points. A SKIP box outside P and a FAIL leaf were also reported.
* **Contract controls, by the reductions subagent.**
  * Erlang-3 gives 1/3.
  * Δ₃ = 0.27658253078094566…
  * v_cos ≈ 0.200901563500556959, inside the contract band 0.20090144–0.20090185.
  * The literal HSTZ eq. (4) reading gives 1.5757 and is rejected.
  * An infeasible D2 ray is detected as negative.
