# Independent point-evaluation replay of the D2 certificate leaves — STATUS v2 (final)

Written 2026-10-18 05:20 PDT (host clock) by `MathPhaseType3.ME3Reductions` for the integration owner `MathPhaseType3`.
This file supersedes `REPLAY-STATUS-v1.md`, which is kept: v2 adds the G chart and the full-leaf primal replay.

**EXPLORATORY smoke test. Point evaluations are not a certificate.** The replay checks that every leaf's claimed outcome
holds at the evaluated points. It does not re-certify any box.

**Independence.** The evaluators were written from the definitions: reductions-v1.md Lemmas 6.4–6.6 for the primal, and
the Lemma D statement plus the charts-spec-v1.md variable maps for the dual. Nothing from `L/code/` is imported. The only
shared file is `code/lane_guard.py`, a byte-identical copy of the lane guard (5589b0a7…c484). Lane files read as
definitions or metadata only:
* `code/spec_primal_P_v1.json`: region, grid and split rule;
* `code/check_cover_v1.py` lines 37–38 and 97–98: sampling convention and cell order. The cell order was then
  re-derived independently from the samples;
* the owner's cover receipts: sample strides.

All runs go through `code/run_v1.sh` (0cfcb20c…af40) with receipts in `receipts/`, one process at a time. Arithmetic is
mpmath at dps 50. Every pre-receipt code hash equals the current file, so nothing was edited after it was run.

## 1. Primal chart P

### 1a. The 948 sampled leaves (`code/replay_primal_v1.py`, run `rp-primal-v1`, exit 0)

**Method.**
* Input: `runs/a01-coverP/sample_boxes.txt` (b522bfe74c1612c0adabd2094c7f53e2854545daca0b5778c12c606857f98f0b):
  SGE 895, DPOS 9, INFEAS 44.
* Points per box: PRIMARY = midpoint and 8 corners; EXTRA = the other 18 points of the 3×3×3 grid, plus the 8 corners
  moved 1/64 toward the midpoint.
* Moments: a_k = 1 − Re[cζ^{k+1}], with c = (1 − ir)e^{(r−i)φ} and ζ = 1/(1 + rω − iω). S = 2a₀a₂/a₁² − 1.
* ∂S/∂r at fixed (ω, φ): analytic, using dc/dr = e^{(r−i)φ}(φ(1−ir) − i) and dζ/dr = −ωζ². It agrees with central
  differences at every DPOS point.
* Feasibility: r = 0 means every φ is feasible. For r > 0, feasible means φ ≤ θ1(r), with θ1 computed by verified
  bracketed root finding. This agrees with the sign of h(0) = 1 − g_r(φ) at every point.
* Closed-form moments vs direct quadrature of ∫t^k e^{−t}h_τ at 24 midpoints: differences ≤ 9e−30.

**Results.** 0 violations.

| Leaf type | Points (primary / extra) | Check | Min margin (primary / extra) | Where |
|---|---|---|---|---|
| SGE | 8055 / 23270 (30409 feasible) | S > 11/50 at feasible points | 0.0112729 / 0.0112831 | box 36, (7/64, 853/1280, 74613/320000) |
| DPOS | 81 / 234 | ∂S/∂r > 0 everywhere | 0.0983355 / 0.0983647 | box 24, (3/128, 8331/12800, 11781/64000) |
| INFEAS | 396 / 1144 | φ > θ1(r) everywhere | 4.2298e−4 | box 457, (87/64, 7449/6400, 302379/80000) |

The whole-box claims also hold at all points: SGE boxes have a₁ > 0 and S > T at infeasible points too, and DPOS boxes
have a_k > 0.

### 1b. EXTRA: all 945,680 leaves of c03 (`code/replay_primal_full_v2.py`, run `rp-primal-full-v2`, exit 0)

* `rp-primal-full-v1` exited 2 and is **kept as a failed attempt**. It used the wrong sample offset: the audit samples
  the 1-based counter n with n % 997 = 0.
* Leaf file `runs/c03-primalP/leaves.txt.gz`. Its uncompressed sha256, 74d67a57…a5, equals c03's `leaf_lines_sha256`.
* **Independent box reconstruction:**
  * The split axis depends only on depth; the sequence is w,r,w,r,w,p,r,w,p,….
  * The cell order is r-major, i.e. (r, ω, φ) from most to least significant. It is the unique one of 6 axis orders
    that reproduces all 948 sample boxes exactly, at offset 996.
* **Independent tiling audit:** all 61440 cells are present and contiguous. Every cell's path set is prefix-free with
  Kraft sum exactly 1, i.e. a complete binary tree. **TILING OK.**
* **Evaluation results:** 0 violations, 0 whole-box-claim issues.
  * SGE: 891,318 midpoints, of which 861,780 are feasible. Min S − 11/50 = 0.0078155, at leaf 75489, midpoint
    (23/256, 36309/51200, 27489/128000).
  * DPOS: 8018 leaves × 9 points. Min ∂S/∂r = 0.080120, at leaf 35192, (3/128, 1507/2560, 3927/20000).
  * INFEAS: 46,344 leaves, tested at the worst corner (r_lo, φ_lo). Every leaf has r_lo > 0, φ_lo ∈ (π, 2π) and
    g_{r_lo}(φ_lo) − 1 > 0, with minimum 1.58e−4 at leaf 55876, (r_lo, φ_lo) = (5/64, 428043/80000). Because θ1
    decreases and g_r increases on [π, 2π] (L6.5), this means φ > θ1(r) on each whole box (50-digit evaluation, not
    interval arithmetic). The midpoints are infeasible too.

## 2. Dual charts — sampled leaves (`code/replay_dual_v1.py`, exit 0 for each)

**Method.**
* W = Q(μ(1+ξ))/Q(μ), with Q(y) = (κy² − 2y + 2)/y³, κ = 50/61, μ = s/(1−s) and ξ = δ − iω. At the endpoints use the
  limits (1+ξ)^{−3} (s = 0) and (1+ξ)^{−1} (s = 1).
* Exact membership in H = conv({0} ∪ {e^{−ξt} : t ≥ 0}), with r = δ/ω:
  * r = 0: |W| ≤ 1.
  * r > 0, with α ∈ [0, 2π) the smallest nonnegative argument of W: if α ≤ θ1(r), require |W| ≤ e^{−rα} (radial).
  * Otherwise W must lie on the 0-side of the chord from 1 to P1 = e^{(−r+i)θ1}. That chord is tangent to the spiral at
    P1 exactly when g_r(θ1) = 1.
  * Why this is exact: the boundary of H is the spiral arc for θ ∈ [0, θ1] followed by that tangent chord. The curve
    turns monotonically, by θ1 along the arc plus 2π − θ1 at the corner 1, so it is convex. H is star-shaped from 0.
* Cross-check: the exact support function σ(ψ) = max(0, cos ψ, cos γ·e^{−r((ψ−γ) mod 2π)}), γ = arctan r, tested on
  2880 directions in float64. 0 disagreements on every chart. 425 LD2 points, where |W| is tiny in absolute terms, are
  float-inconclusive; the 50-digit exact test decides them.
* Q was checked against the Laplace transform of (t−1)² − 11/61 by quadrature, to within 1e−20.
* Chart variables are converted to (s, δ, ω) in the script (LW ν = 1/ω; LD1 (s, d, β); LD2 (χ, ρ_t, β)). Non-physical
  points (ω = 0, ν = 0, d = 0, β ∉ (0, π/2)) are skipped and counted.

| Chart | Run | Input sample (sha256) | Boxes | Tested points (prim / extra) | Non-physical skipped | Violations | Min margin (prim / extra) |
|---|---|---|---|---|---|---|---|
| G | rp-dual-G-v1 | b01-cover-G (3353fbcc960ce05bde217bdcd64cf65968afb0eb705fbad011490750d059d283) | 1025 CERT (514 radial, 511 small) + 3 SKIP | 9225 / 26650 | 0 | **0**; all 3 SKIP boxes lie in P | 0.028935 / 0.028934 |
| SWC | rp-dual-SWC-v1 | b02-cover-SWC (726910dd…6517) | 353 CERT | 3085 / 9063 | 207 | **0** | 3.0007e−5 / 6.18e−9 |
| SWB | rp-dual-SWB-v1 | b01-cover-SWB (cb606424…09fc) | 1000 CERT | 8952 / 25940 | 108 | **0** | 4.5857e−3 / 4.5892e−3 |
| LW | rp-dual-LW-v1 | b01-cover-LW (032c4c61…388d) | 23 CERT | 195 / 583 | 27 | **0** | 0.86790 / 0.86802 |
| LD1 | rp-dual-LD1-v1 | b01-cover-LD1 (e3c8728c…23bb) | 112 CERT | 940 / 2827 | 153 | **0** | 0.34678 / 0.34646 |
| LD2 | rp-dual-LD2-v1 | b01-cover-LD2 (06ab063e…388d) | 1072 CERT + 18 SKIP | 9563 / 27761 | 196 | **0**; SKIP rule holds on all 18 | 0.028790 / 0.028805 |

**G SKIP:in-primal-P check.** A box lies in P = {ω ∈ [1/5, 40], δ ≤ 3ω} iff ω_lo ≥ 1/5, ω_hi ≤ 40 and δ_hi ≤ 3ω_lo;
this is exact, because the worst point of the box is (δ_hi, ω_lo). All 3 sampled SKIP leaves pass:
* δ ∈ [643/16, 161/4], ω ∈ [215/16, 27/2];
* δ ∈ [901/16, 451/8], ω ∈ [301/16, 151/8];
* δ ∈ [5/8, 51/80], ω ∈ [17/80, 9/40]. Here δ_hi = 3ω_lo = 51/80 holds with equality; the boundary is inclusive.

**Notes.**
* G min margin: box 120, (s, δ, ω) = (3/256, 4069/64, 233/64).
* SWC's smallest margins are at δ = ω → 0, where W → 1.
* 39 G points and 889 LD2 points lie outside their chart's assigned set (CERT boxes straddling a chart boundary). They
  were tested anyway and pass.
* Every tested dual point fell in the radial or disk branch; the chord branch never triggered.

## 3. Mutation controls (each must be flagged; exit 1 is the expected outcome)

* `rp-mkmut-v1` exit 1: **failed attempt, kept**, because its θ1 findroot did not converge. `rp-mkmut-v2` exit 0
  generated the inputs.
* `rp-mut-primal-v1`: all 3 mutated boxes were flagged at all 35 points each (105 violations):
  * an SGE box at the D1 minimizer, S = 0.2009026;
  * an INFEAS box at φ ∈ [1, 2], with φ − θ1 = −3.546;
  * a DPOS box at (2.75, 32, 3.4031), with ∂S/∂r = −23.478.
* `rp-mut-dualG-v1`:
  * a CERT box at δ ≈ 0, ω = 1.0359, s ≈ 0.729 has |W| = 1.0141 and was flagged at all 35 points;
  * a SKIP box with ω_hi = 50 broke the P rule and was flagged;
  * a FAIL leaf was reported.

## 4. Files (sha256)

| File | sha256 |
|---|---|
| code/replay_primal_v1.py | 6494c694be9c622d422f5099a8d81a247dd6a947f671c3390b0292a108ff097f |
| code/replay_dual_v1.py | 8e1bc61b9c0da6b9c78c18fdbb8e0d84bc1600941d0ba1c5b9c0c759ba8bd53a |
| code/replay_primal_full_v1.py (failed attempt) | fe7a95214d38b4cab2df76de3068d666ead36a42a30924f82fee833b4c6f2183 |
| code/replay_primal_full_v2.py | 9e44c891270068cc26152e8871bfa9d24b62d72a4f8b3dff71b29995fc1e8762 |
| code/mk_mutations_v1.py (failed attempt) | 4297979e3f2aa00f98a52c709328ef81eb54ad1903a56f60fac8b6d9112450f5 |
| code/mk_mutations_v2.py | e493f2429e954d02dd816a8f3213153a4856284d172a61e2c853219ea941621a |
| code/replay_dual_full_v1.py (**written, never executed**, per the capacity rule) | 820513de587168a788dac169274e9b10220684a5f9bf5905976e0a5c82a2a0c5 |
| code/lane_guard.py | 5589b0a75abf43d98c14a4b68a42ef1ea02b10829a5e67ee5fa298176c7ba484 |
| runs/rp-primal-v1/replay_primal.json | 997904227ef110bfe1fb2c422f122a20731b53db4c32b6b4e968c66c0f199119 |
| runs/rp-primal-full-v2/replay_primal_full.json | 51f723522c93706397748dce57472359ff8446dac843e9e665bd11ebe32d4a6e |
| runs/rp-primal-full-v1/replay_primal_full.json (failed attempt) | 6096098203d896e4a3fe737da81ede4e248e71290d374b8bd9163d8839bd1b03 |
| runs/rp-dual-G-v1/replay_dual_G.json | 052705abc4c6db01df2d5db8dd96d304098ac0bbe76609eafd44f320734d7d00 |
| runs/rp-dual-SWC-v1/replay_dual_SWC.json | 9791bdbd2dc3b964bce79d03f793679a4515338e77ad3974594a6db9b7440280 |
| runs/rp-dual-SWB-v1/replay_dual_SWB.json | 3c96f2cd9aa61cb671dc6b3d02d35982dfa5f071f14ded3c51cdccfd17bc409a |
| runs/rp-dual-LW-v1/replay_dual_LW.json | 511348f38cfc9a72d47b558638418ee3d171bdaff5b50d4c74eae5084ae8ec45 |
| runs/rp-dual-LD1-v1/replay_dual_LD1.json | d71516abb1c84f757493cf8370083fa6ee2b0e19869f50def26c8272da96dd25 |
| runs/rp-dual-LD2-v1/replay_dual_LD2.json | e561a0f2f4ead09d738fb1ab0704ea45c76e23606e56c5fbd93a6a77e383816b |
| runs/rp-mkmut-v2/primal_mutations.txt | 078042f71d1b68ed3325aafc884ccb3390a560d80573ff499e28420328119051 |
| runs/rp-mkmut-v2/dualG_mutations.txt | f8ca660547c77d0b4ab37ae2a24f8d3e498e98167fe97101a77c27a36b8bf17e |
| runs/rp-mut-primal-v1/replay_primal.json | e71341144cf1519b519263946f93279e02c38b3486230b7c629661e9a0c9e588 |
| runs/rp-mut-dualG-v1/replay_dual_G.json | 5e37b4f776aad5eb4f968986d76aa8a9d5945a7b34acec244c2f87d50f15554e |
| REPLAY-STATUS-v1.md (superseded) | c54e9012c53817958667e51b716941a331944696107388390353162b65a9d594 |

The per-box minimum margins are in `runs/<run>/per_box_min_margin*.txt`. The stdout, stderr, exit codes, wall times
and max RSS are in the post receipts.
