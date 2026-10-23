# Independent point-evaluation replay of the D2 certificate leaves — STATUS v1

Written 2026-10-18 05:06 PDT (host clock) by `MathPhaseType3.ME3Reductions` for the integration owner `MathPhaseType3`.
**EXPLORATORY smoke test. Point evaluations are not a certificate.** The replay checks that every sampled leaf's claimed
outcome holds at its sampled points. It does not re-certify any box.

**Independence.** The evaluators were written from the definitions: reductions-v1.md Lemmas 6.4–6.6 for the primal, and
the Lemma D statement plus charts-spec-v1.md variable maps for the dual. Nothing from `L/code/` is imported. The only
shared file is `code/lane_guard.py`, a byte-identical copy of the lane's no-deletion guard (sha256 5589b0a7…c484). All
runs go through the lane launcher `code/run_v1.sh` (sha256 0cfcb20c…af40), with receipts in `receipts/`. Arithmetic is
mpmath at mp.dps = 50.

## Points per box

* PRIMARY (as specified): the midpoint and the 8 corners.
* EXTRA: the other 18 points of the 3×3×3 grid, plus the 8 corners moved 1/64 of the way toward the midpoint.

Every point is an exact rational in the chart variables.

## 1. Primal chart P (`code/replay_primal_v1.py`, run `rp-primal-v1`, exit 0)

**Method.**
* Input: `runs/a01-coverP/sample_boxes.txt` (sha256 b522bfe74c1612c0adabd2094c7f53e2854545daca0b5778c12c606857f98f0b),
  948 boxes: SGE 895, DPOS 9, INFEAS 44.
* Moments: a_k = 1 − Re[cζ^{k+1}], with c = (1 − ir)e^{(r−i)φ} and ζ = 1/(1 + rω − iω). Then S = 2a₀a₂/a₁² − 1.
* ∂S/∂r at fixed (ω, φ): analytic, using dc/dr = e^{(r−i)φ}(φ(1 − ir) − i) and dζ/dr = −ωζ². Cross-checked by mpmath
  central differences: 0 disagreements above 1e−30 relative.
* Feasibility: r = 0 means D1, where every φ is feasible. For r > 0, feasible means φ ≤ θ1(r); θ1 was found by bracketed
  root finding with a verified sign change of g_r − 1 (1560 values). This agrees with the sign of h_τ(0) = 1 − g_r(φ)
  at every point: 0 inconsistencies.
* Closed-form moments vs direct mpmath quadrature of ∫t^k e^{−t}h_τ(t)dt at 24 box midpoints: maximum difference
  8.97e−30.

**Results.** 0 violations. Point counts and margins (primary / extra):

| Leaf type | Points (primary / extra) | Check | Min margin (primary / extra) | Argmin (primary) |
|---|---|---|---|---|
| SGE | 8055 / 23270 (30409 feasible) | S > 11/50 at feasible points | 0.0112729292 / 0.0112831387 | box 36, (7/64, 853/1280, 74613/320000) |
| DPOS | 81 / 234 | ∂S/∂r > 0 at all points | 0.0983354507 / 0.0983646662 | box 24, (3/128, 8331/12800, 11781/64000) |
| INFEAS | 396 / 1144 | φ > θ1(r) at all points | 4.2298171e−4 / 4.2298171e−4 | box 457, (87/64, 7449/6400, 302379/80000) |

The whole-box claims also held at every point: SGE boxes have a₁ > 0 and S > T at infeasible points too, and DPOS
boxes have a_k > 0. 0 exceptions.

## 2. Dual charts (`code/replay_dual_v1.py`, exit 0 for each)

**Method.**
* W = Q(μ(1+ξ))/Q(μ), with Q(y) = (κy² − 2y + 2)/y³, κ = 50/61, μ = s/(1−s) and ξ = δ − iω. At the endpoints use the
  limits W = (1+ξ)^{−3} (s = 0) and (1+ξ)^{−1} (s = 1).
* Exact membership in H = conv({0} ∪ {e^{−ξt}}):
  * r = 0: |W| ≤ 1.
  * r > 0: let α ∈ [0, 2π) be the smallest nonnegative argument of W. If α ≤ θ1(r), require |W| ≤ e^{−rα}.
  * Otherwise W must lie on the 0-side of the chord from 1 to e^{(−r+i)θ1}. That chord is tangent to the spiral exactly
    when g_r(θ1) = 1 (derived and checked here).
* Cross-check: the exact support function σ(ψ) = max(0, cos ψ, cos γ·e^{−r((ψ−γ) mod 2π)}), γ = arctan r, tested on a
  2880-direction float64 grid. 0 disagreements. The float check is inconclusive (|value| < 1e−12) at 425 LD2 points, where
  |W| and the bound are tiny in absolute terms; the exact 50-digit test decides those.
* Q was checked against the Laplace transform of q(t) = (t−1)² − 11/61 by quadrature at 3 complex y; the difference
  is below 1e−20.
* Non-physical sample points were skipped and counted: ω = 0, ν = 0, d = 0, β = 0 and β ≥ π/2.

| Chart | Run | Input (sha256) | Boxes | Tested points (primary / extra) | Skipped non-physical | Violations | Min margin (primary / extra) |
|---|---|---|---|---|---|---|---|
| SWC | rp-dual-SWC-v1 | b02-cover-SWC (726910dd…6517) | 353 CERT | 3085 / 9063 | 207 (ω = 0) | 0 | 3.0007e−5 / 6.18e−9 |
| SWB | rp-dual-SWB-v1 | b01-cover-SWB (cb606424…09fc) | 1000 CERT | 8952 / 25940 | 108 (ω = 0) | 0 | 4.5857e−3 / 4.5892e−3 |
| LW | rp-dual-LW-v1 | b01-cover-LW (032c4c61…388d) | 23 CERT | 195 / 583 | 27 (ν = 0) | 0 | 0.86790 / 0.86802 |
| LD1 | rp-dual-LD1-v1 | b01-cover-LD1 (e3c8728c…23bb) | 112 CERT | 940 / 2827 | 153 (β ∉ (0, π/2), d = 0) | 0 | 0.34678 / 0.34646 |
| LD2 | rp-dual-LD2-v1 | b01-cover-LD2 (06ab063e…388d) | 1072 CERT + 18 SKIP | 9563 / 27761 | 196 | 0; SKIP rule holds on all 18 | 0.028790 / 0.028805 |
| G | — | not yet available | — | — | — | — | — |

Notes on the dual results:
* The margin is absolute (e^{−rα} − |W|, or 1 − |W|). SWC's smallest margins occur where δ and ω both tend to 0, at
  the corner where W → 1. The extra-point minimum is at s = 6913/8192, δ = ω = 1/5120.
* Every tested point fell in the radial or disk branch. The chord branch never triggered on these samples, so all
  verdicts come from the radial or disk test.
* 889 LD2 points lie outside LD2's assigned set: they are in CERT boxes straddling s = 1/16 or d = 1/65. They were
  tested anyway and pass.

## 3. Mutation controls (each must be flagged; exit 1 is the expected outcome)

* `rp-mkmut-v1` exit 1. **Failed attempt, kept**: its θ1 findroot did not converge. `rp-mkmut-v2` (θ1 by bisection)
  exit 0 and wrote the mutated inputs.
* `rp-mut-primal-v1` exit 1 (expected). All 3 mutated boxes were flagged, at all 35 points each (105 violations):
  * an SGE box at the D1 minimizer, S = 0.2009026 < 0.22;
  * an INFEAS box at φ ∈ [1, 2], with φ − θ1 = −3.546;
  * a DPOS box at (r, ω, φ) ≈ (2.75, 32, 3.4031), with ∂S/∂r = −23.4777.
* `rp-mut-dualG-v1` exit 1 (expected):
  * a CERT box at δ ≈ 0, ω = 1.0359, s ≈ 0.729 has |W| = 1.0141 > 1 and was flagged at all 35 points;
  * a SKIP box violating the G rule (ω_hi = 50) was flagged;
  * a FAIL leaf was reported.

## 4. Files (sha256)

| File | sha256 |
|---|---|
| code/replay_primal_v1.py | 6494c694be9c622d422f5099a8d81a247dd6a947f671c3390b0292a108ff097f |
| code/replay_dual_v1.py | 8e1bc61b9c0da6b9c78c18fdbb8e0d84bc1600941d0ba1c5b9c0c759ba8bd53a |
| code/mk_mutations_v1.py (failed attempt) | 4297979e3f2aa00f98a52c709328ef81eb54ad1903a56f60fac8b6d9112450f5 |
| code/mk_mutations_v2.py | e493f2429e954d02dd816a8f3213153a4856284d172a61e2c853219ea941621a |
| code/lane_guard.py | 5589b0a75abf43d98c14a4b68a42ef1ea02b10829a5e67ee5fa298176c7ba484 |
| runs/rp-primal-v1/replay_primal.json | 997904227ef110bfe1fb2c422f122a20731b53db4c32b6b4e968c66c0f199119 |
| runs/rp-dual-SWC-v1/replay_dual_SWC.json | 9791bdbd2dc3b964bce79d03f793679a4515338e77ad3974594a6db9b7440280 |
| runs/rp-dual-SWB-v1/replay_dual_SWB.json | 3c96f2cd9aa61cb671dc6b3d02d35982dfa5f071f14ded3c51cdccfd17bc409a |
| runs/rp-dual-LW-v1/replay_dual_LW.json | 511348f38cfc9a72d47b558638418ee3d171bdaff5b50d4c74eae5084ae8ec45 |
| runs/rp-dual-LD1-v1/replay_dual_LD1.json | d71516abb1c84f757493cf8370083fa6ee2b0e19869f50def26c8272da96dd25 |
| runs/rp-dual-LD2-v1/replay_dual_LD2.json | e561a0f2f4ead09d738fb1ab0704ea45c76e23606e56c5fbd93a6a77e383816b |
| runs/rp-mkmut-v2/primal_mutations.txt | 078042f71d1b68ed3325aafc884ccb3390a560d80573ff499e28420328119051 |
| runs/rp-mkmut-v2/dualG_mutations.txt | f8ca660547c77d0b4ab37ae2a24f8d3e498e98167fe97101a77c27a36b8bf17e |
| runs/rp-mut-primal-v1/replay_primal.json | e71341144cf1519b519263946f93279e02c38b3486230b7c629661e9a0c9e588 |
| runs/rp-mut-dualG-v1/replay_dual_G.json | 5e37b4f776aad5eb4f968986d76aa8a9d5945a7b34acec244c2f87d50f15554e |

The per-box minimum margins are in `runs/<run>/per_box_min_margin*.txt`. The stdout and stderr hashes are in the post
receipts.

**Pending:** the G chart (no `b0X-cover-G` sample file at 05:04 PDT).
