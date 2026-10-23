# Minimal SCV of ME(3): every order-≤3 matrix-exponential law has SCV ≥ v_cos? (math-1 successor, transition 41)

Lane owner and integration owner: worker `MathPhaseType3`. Lane directory created 2026-10-18 02:42:58 PDT (host
clock) with a plain `mkdir` that refuses an existing path. Everything outside this directory is read-only for this
lane. This README was written **before any calculation** in this lane; before it, the worker only read the contract
and the screen. **No novelty, priority or "first" claim.** Correctness, novelty and significance stay separate.

Frozen inputs (sha256 recomputed by this worker 2026-10-18 02:31 PDT):

| Input | Path (under `institute/runs/six-lane-2026-10-16/`) | sha256 |
|---|---|---|
| Frozen contract | `screening/math-1-me3-minimum-scv-contract.json` | `1a72a6f057ed4e1cb005386b228b06a1f339fb9579cbce9a5df7952a4f8a4f15` (matches the parent pin) |
| Pre-freeze screen | `screening/math-1-me3-minimum-scv-screen-v1.md` | `3e7246ba96d45c4fbe982d73a329893b617860c47d63e577ad9fd75ec1fe99c7` (matches the parent pin) |

The previous math-1 target (Commault–Mocanu 2003 Conjecture 1, lane `phase-type-complex3`) is closed. That lane is
not edited further.

## 1. Exact question (contract `exact_statement`)

* **Class ME(≤3).** X ≥ 0 is continuous with F(t) = Pr(X < t) = 1 − α e^{At} 𝟙, where α is a real 1×n row vector
  and A a real n×n matrix, with n ≤ 3 (HSTZ 2016 Definitions 1–2). Its density f(t) = −α A e^{At} 𝟙 ≥ 0 on [0, ∞).
  There is no sign structure on α or A.
* **Objective.** SCV(X) = m0·m2/m1² − 1, where m_k = ∫ t^k f (HSTZ Definition 5, which they call "cv").
* **Constant.** v_cos := min over ω > 0, φ ∈ ℝ of SCV(e^{−t}(1 − cos(ωt − φ))). The literal decimal 0.200902 is a
  rounded value and is never used as the bound.
* **Positive.** A written proof that SCV ≥ v_cos for every X in ME(≤3), covering every pole configuration (A: three
  distinct real; B: double + simple real; C: triple real; D1: real + complex pair with equal damping; D2: real pole
  strictly dominant over the complex pair; and lower-order degenerations). Every certified computation must be fully
  specified and re-runnable, with every unbounded parameter tail covered by a written lemma.
* **Negative.** An explicit ME(3) representation with a certified f ≥ 0 on all of [0, ∞) and a certified SCV < v_cos.

## 2. Baseline and headroom (contract)

PH(3): 1/3 (Aldous–Shepp). ME(2): 1/2. Real poles at order 3: 0.276583, reported. Common damping (D1): reduces to
the cos family (Battagliola–Peralta arXiv:2609.14612, numerical only). The open part is the global bound,
including D2. Common damping alone, real poles alone, finite scans or higher orders are PARTIAL, not the gate.
Competitor risk is high (Battagliola/Peralta 2026).

## 3. Representation and plan (worker's own; the contract's parent hint is UNTRUSTED and re-derived)

**R1. Structure.** An ME(≤3) density is a nonnegative exponential polynomial f(t) = Σ p_j(t) e^{−s_j t}, of total
order ≤ 3, with Re s_j > 0 for every contributing exponent. A contributing complex pair cannot dominate. "Continuous"
excludes an atom, and SCV is invariant under scaling f and under time scaling t ↦ ct.

**R2. Ratio form.** SCV/(1+SCV) = min_{θ>0} ∫(t−θ)² f / (θ² ∫ f), a minimum of ratios of linear functionals. For
fixed exponents, the nonnegative densities form a closed pointed cone of dimension ≤ 3, so the infimum of SCV over
that cone is attained on an extreme ray. Extreme-ray families, all to be proved:
* real exponents: a double zero at τ ∈ [0, ∞), giving the Hermite–Genocchi mixtures of (t−τ)² e^{−μt}; boundary
  rays have lower order;
* D1: e^{−t}(1 − cos(ωt − φ)), which gives v_cos by definition;
* D2, with real pole 1 and pair −(1+δ) ± iω, δ > 0: f = e^{−t} h, where
  h(t) = 1 − e^{−δ(t−τ)}(cos ω(t−τ) + (δ/ω) sin ω(t−τ)) and τ ∈ [0, τ₁(δ, ω)].

**R3. Real poles.** Every component has SCV ≥ Δ₃ := min_τ SCV(e^{−t}(t−τ)²), so a real-pole ME(≤3) law has
SCV ≥ Δ₃. This needs a rigorous bound Δ₃ > v_cos: an exact polynomial certificate plus an interval upper bound on
v_cos taken at one explicit point.

**R4. D2 crux: monotone-path strategy (the worker's plan; it may fail and be replaced by a versioned plan).**
Parameters (r = δ/ω, ω, φ = ωτ). Feasibility is φ ≤ θ₁(r), with θ₁ decreasing in r and θ₁(0) = 2π, which is still
to be proved. So the path (r', ω, φ), r' ∈ [0, r], stays feasible and ends in D1 (r' = 0), where SCV ≥ v_cos by
definition.
* Lemma M (target): for some threshold T > v_cos, ∂S/∂r > 0 at every feasible D2 point with S < T. Then any D2 point
  with S < T is joined by a path of increasing S from D1, so S > v_cos. Points with S ≥ T are fine.
* Lemma M is proved by (i) written tail lemmas showing {S < T} lies in an explicit compact box, and (ii) an interval
  branch-and-bound over that box with three certified box outcomes: S ≥ T, ∂S/∂r > 0, or infeasible.
* T, the box, the tail constants, the arithmetic library/precision and the subdivision rules are frozen in a versioned
  spec file BEFORE the certified run. Exploratory numerics happen first and are labelled exploratory.
* If Lemma M is false for every usable T, the obstruction is recorded and another route is chosen. One candidate is
  the dual (θ = 1) membership W = Q(μ+x−iy)/Q(μ) ∈ conv(log-spiral).

**R5. Attainment.** The cos-family minimum is attained, by D1 tail lemmas at ω → 0 and ω → ∞.

## 4. Deliverables

1. `proof/` — written theorem (or obstruction) with every lemma proved, the imports listed, and an exact statement of
   covered and uncovered domains. Partial results are labelled PARTIAL.
2. `code/`, `runs/`, `receipts/` — exploratory numerics (labelled) and certified computations. Each script's sha256
   is recorded in a receipt **before** execution; outputs are hashed after; parameters, seeds, precision, wall time
   and max RSS are recorded. There are no in-place code edits: fixes go into new versioned files, and failed attempts
   stay.
3. An optional split (parent-permitted): one subagent may own `reductions/` (R1–R3, R5, the v_cos controls) with
   disjoint ownership. This worker owns everything else and integrates.

## 5. Stop rules (contract)

* Priority hit (an earlier proof or counterexample) relayed by the parent → stop.
* Certified counterexample → switch to disproof verification.
* v_cos outside 0.20090144–0.20090185 → convention error; stop and report.
* Stop scientific work at 2026-10-18 18:00 PDT (deadline 18:31:43). If the global bound is not certified by then,
  report PARTIAL with the exact uncovered region.
* Finite numerics never prove an all-parameter claim. Timeouts are UNKNOWN.

## 6. Native caps and environment

* math-1 combined: ≤ 4 busy processes, ≤ 8 GiB RSS; new lane data ≤ 1 GiB; chunks ≤ 10800 s; caps never raised.
* Every native run: fresh gate free ≥ 12.2e9 B + projected growth, continuous 12e9 floor; `TMPDIR=<lane>/tmp/`;
  `ulimit -t` CPU cap; `/usr/bin/time -l`; launched by guarded bash async jobs. No SIGKILL, Popen.kill or
  subprocess.run(timeout), and no native child under an eval deadline.
* Interpreter, used read-only: `information-science/evidence/six-lane-20261016/robust-spr/code/venv/bin/python`
  (Python 3.14.3, python-flint 0.9.0, sympy 1.14.0, mpmath 1.3.0), run with `-B` and `PYTHONDONTWRITEBYTECODE=1`.
  No installs, model CLIs or Git. Primary sources may be fetched read-only (public URLs) into `sources/`.

## 7. Controls (contract, planned before any run)

Erlang-3 gives 1/3. The real-pole kernel minimum gives ≈ 0.276583. The cos-family minimum gives v_cos to ≥ 12 digits,
inside 0.20090144–0.20090185. The literal HSTZ eq. (4)/Table 2 reading gives ≈ 1.5757 and is rejected. A deliberately
infeasible D2 ray (τ > τ₁) is detected as negative somewhere. Mutated certificate boxes or bounds fail for the
intended reason. Tail-lemma constants are checked at sample points.

## 8. Log (append-only)

| PDT | Event | Result |
|---|---|---|
| 10-18 02:31 | Contract and screen read; hashes match the parent pins | — |
| 10-18 02:42:58 | Lane created; README written before any calculation | this file |
| 10-18 02:43–02:44 | Freeze receipt `receipts/readme-freeze-v1.json` (README sha `b6185504…2445`); lane guard copied (`cp -n`, sha `5589b0a7…`); launcher `code/run_v1.sh`; HSTZ 2016 PDF fetched read-only to `sources/hstz2016-osafarepew.pdf` (sha `52943dda…0d63`) and read (Defs 1, 2, 5, eq. (4), Tables 1–2); arXiv abstracts 2608.29143 and 2609.14612 read (scopes: one repeated real pole; common damping) | — |
| 10-18 02:45 | x01 exploration crashed (math.exp overflow in θ₁ at r = 1000); x02 v2 (overflow fix) | D1 min 0.2009015635005571 at (ω, φ) = (1.03593297, 0.33703826), 1/S = 4.977562058630903; D2 grid min 0.20107 at r = 1e-4; sublevel {S < T}: T = 0.22 → r ≤ 0.1, ω ∈ [0.69, 1.37], φ ∈ [0.14, 0.54], min ∂S/∂r 0.114 > 0; T = 0.27 has ∂S/∂r < 0 near φ ≈ θ₁(r) |
| 10-18 02:46 | Subagent `ME3Reductions` spawned with disjoint ownership of `reductions/` (lemmas L1–L6 and contract controls) | running |
| 10-18 02:55 | x03 exploration (overflow-free ε-form) | regional minima: ω ≥ 2 → 0.305; ω ≤ 0.3 → 0.261; r ≥ 0.3 → 0.248; boundary family φ = θ₁(r) ≥ 0.25 → 0.25 as r → 0; D1 at φ = 0: exactly 0.25 at ω = 1 (hand: 1 + S = 2(x² + 3x + 6)/(x + 3)², x = ω²). Small-ω float values carry cancellation error ~1e-4 (artifact) |
| 10-18 03:00–03:05 | **Representation decision (versioned in code docstrings):** T = 11/50. Valley V = {r ∈ [0, 3/10], ω ∈ [9/20, 19/10]} is handled in the PRIMAL by Lemma M (outcomes SGE / DPOS / INFEAS). The far region (all other (δ, ω)) is handled in the DUAL by the elementary sufficient test: for every μ > 0, W = Q_T(μ(1+ξ))/Q_T(μ) = |W|e^{iα}, α ∈ [0, 2π), satisfies ω log|W| + δα ≤ 0 (then W ∈ conv{0, e^{−ξt}} ⊂ the spiral hull, which implies S ≥ T for every density with those poles). Five compact charts with stable formulas: corner, B-edge, general, large-δ, large-ω | the dual removes the τ-subregimes and all tails become algebraic |
| 10-18 03:06 | v01 formula checks | exact sympy: ∂P_k/∂r identity (k = 0, 1, 2), the real form of h, h′ and the double zero; 40-digit quadrature agrees with the closed-form moments (max rel. err 2.8e−40); sinc representation; primal/dual sign agreement 9/9 |
| 10-18 03:07–03:13 | c01 valley v1 (naive balls) | box explosion (38.8M evals, 0 FAIL so far); stopped by worker SIGTERM. SIGTERM went first to `/usr/bin/time` (which does not forward it), then to the Python child. Exit 143, **no conclusion**. The child's stdout grew after the post receipt was written, so the receipt hash covers an earlier prefix. Lesson: SIGTERM the Python child; use no harness deadline |
| 10-18 03:15 | c02 valley v2 (naive + mean-value form via jets) | **certificate_ok: 98,914 evals in 5.9 s, FAIL 0**: SGE 41,865, DPOS 7,427, INFEAS 5,733. DPOS bounding box r ≤ 0.2375, ω ∈ [0.6, 1.65], φ ≤ 0.736. Leaf-list sha `906a6e59…5c0b` |
| 10-18 03:14–03:22 | k01 dual calibration (EXPLORATORY), `me3dual_v2.py` + `cert_dual_v1.py` | only LW certified; C failed the Re g′ sign test; G was mis-split (relative widths over a 512-wide range); kept as a failed calibration |
| 10-18 03:23–03:25 | x04 dual landscape (EXPLORATORY, mpmath points) | the radial sufficient test fails at 22 grid points, all with r ∈ [0.316, 1.0], ω ∈ [1, 5]; W lies below the real axis there (chord region). All 22 lie inside the enlarged primal region P below |
| 10-18 03:25 | Checkpoint 1 sent to parent | — |
| 10-18 ~03:30 | Parent: c02 is a candidate/partial until the parent evaluator and coverage audit; freeze each chart's domain, transformations, feasibility, arithmetic, split/termination rules and coverage outputs before a certified run; justify the radial test's closure, 0-limit and arg branch; triangle/chord handling must cover every missing branch; tails must be uniform/compactified; write the Lemma M continuation rigorously; record which boxes use which outcome and check their union independently. Process: target the owned child, no SIGKILL | adopted |
| 10-18 03:32–03:34 | **c03 primal region P** (`spec_primal_P_v1.json`, frozen before run; `cert_primal_v3.py`): r ∈ [0, 3], ω ∈ [1/5, 40], φ ∈ [0, 31416/5000] | **certificate_ok**: 1,829,920 evals, 116.6 s, FAIL 0; leaves SGE 891,318 / DPOS 8,018 / INFEAS 46,344; DPOS bounding box r ≤ 0.2344, ω ∈ [0.5887, 1.6614], φ ≤ 0.7363; leaf-lines sha `74d67a57…92a5`; full leaf record `runs/c03-primalP/leaves.txt.gz` |
| 10-18 03:36 | a01 independent coverage audit of c03 (`check_cover_v1.py`: replays the split rule from geometry only) | **tiling_ok**: 945,680 leaves, all 61,440 cells, outcome counts match; 948 sampled exact boxes in `runs/a01-coverP/sample_boxes.txt` for re-evaluation |
| 10-18 03:37–04:19 | k02 dual calibration v2 (EXPLORATORY, `me3dual_v3.py` + `cert_dual_v2.py`, charts SWC/SWB/G/LW/LD1/LD2) | LW and LD1 certified; SWC (N = 60 series: the ball recursion inflates), SWB (nan from complex division in g‴), G (naive W ball contains 0 for small s, large ξ) and LD2 (Re P̂ > 0 requirement wrong for β > π/4) fail. Debug runs x05 (G box) and x07 (B-edge box); x06 corner point margins: max_s Ψ ≤ −0.0366 and min Im g/ω ≥ 0.297 on the corner grid |
| 10-18 03:56 | Subagent `ME3Reductions` finished: `reductions/proof/reductions-v1.md` (sha `ad6c5091…5536`), `reductions/proof/vcos-lower-bound-v1.md` (sha `01821b4c…9e20`), `reductions/STATUS.md` (sha `61776330…2c76`). L1–L6 proved in text; outline step "lower-order densities embed as faces" is false and is replaced by the inclusion K_E ⊆ K_E′ (Lemma 2.5); certified 0.20090156350055 ≤ v_cos < U = 0.200901563500556958801…; Δ₃ ∈ (0.2765825307809456, 0.2765825307809457) | imported into the integration |
| 10-18 04:2x | Library versions: `me3dual_v3.py` was used only in calibration; `me3dual_v4.py` was never executed and is superseded; `me3dual_v5.py` was never executed and was damaged by an editing slip; **`me3dual_v6.py` is for certified use** (W via the w_k zz^k form plus the complex mean-value enclosure; real-arithmetic B-edge; LD argument choices with a conservative (1 − d) factor). Driver `cert_dual_v4.py` (identical to v2 except that it imports v6) | k03 calibration v3 launched (EXPLORATORY) |
| 10-18 04:24:28 | Label corrections from host mtimes: the subagent row "03:56" should read 03:41:53 (STATUS.md mtime; reductions-v1.md 03:31:02, vcos-lower-bound-v1.md 03:39:46). The row "04:2x" should read 04:23:36–04:24:05 (me3dual_v6.py 04:23:36, cert_dual_v4.py 04:23:44, first k03 pre-receipt 04:23:58). The parent message row "~03:30" is approximate; that message arrived between the 03:25 checkpoint and the c03 launch at 03:32:09 | hashes unchanged |
| 10-18 04:23:58–04:39:10 | k03 calibration v3 (EXPLORATORY, `cert_dual_v4.py` + `me3dual_v6.py`) | LD1, LD2 and LW certified. G and SWB had no FAIL but hit the calibration eval caps. SWC still failed: the linear recurrence for P_j inflated (fixed in v7: complex powers) |
| 10-18 04:40:41–04:48:24 | k04 calibration (SWC, `cert_dual_v5.py` + `me3dual_v7.py`) | still FAIL at s ≈ 0.9 near ξ = 0. Debug x08: the ball of 4B − A² contained 0 (cancellation of two terms near 5.2). Fix v8: the exact root p = (s(1−s)(1 + i√(2κ−1)) − κs²)/N₁, with |p|² = B and 2Re p = −A, avoids any square root of a ball |
| 10-18 04:41:52 | **Dual certified spec v1 frozen** (`receipts/spec-dual-freeze-v1.json`: `code/spec_dual_v1.json` sha `23dd1dad…f6c1`, `proof/charts-spec-v1.md` sha `5a43c252…1ff1`, all library hashes) | then d01 runs launched (`cert_dual_v5.py` + `me3dual_v7.py`) |
| 10-18 04:49:47–04:50:13 | k05 calibration (SWC, `cert_dual_v6.py` + `me3dual_v8.py`) | certificate_ok in 68,512 evals |
| 10-18 04:50:47 | **SWC certified spec v2 frozen** (`receipts/spec-dual-freeze-v2.json`: `code/spec_dual_v2.json` sha `d9b490ef…8930`, `cert_dual_v6.py` sha `abffeefd…7339`, `me3dual_v8.py` sha `5f3e7675…d1ea`). The non-corner tests in v8 are re-exports of v7/v6 | d02-SWC launched |
| 10-18 04:51 | Certified: **d01-LD1** (5,954 CERT), **d01-LD2** (56,933 CERT + 880 SKIP), **d01-LW** (1,250 CERT), **d02-SWC** (34,304 CERT, 68,512 evals); all certificate_ok, 0 FAIL. Audits b01-cover-LD1/LD2/LW and b02-cover-SWC: tiling_ok, all cells, LD2's 880 SKIP rules re-checked | G and SWB still running (0 FAIL so far) |
| 10-18 04:52 | Controls n01 (`controls_v1.py`), all as intended: M1 primal without DPOS → 1024 FAIL; M2 flipped derivative → 1024 FAIL; M3 dual GENERAL test inside the valley → 195 FAIL; M4 corner chart with T′ = 3/10 > Δ₃ → 70 FAIL; M5 INFEAS never fires on boxes with feasible points; M6 positive control certified (31 DPOS). Audit mutants n02/n03: dropped leaf, FAIL label, flipped path bit and false SKIP are all rejected by `check_cover_v2.py` | — |
| 10-18 04:54 | Checkpoint 2 sent to parent; subagent tasked with an independent mpmath replay of sampled leaves (writes only under `reductions/replay/`) | — |
| 10-18 04:53:56 | **d01-SWB** certified: 8,196,408 leaves (bedge 8,144,675 / bedge-mvf 51,733), 16,392,304 evals, 709 s. Audit b01-cover-SWB (04:54:18–04:54:28): tiling_ok, 512/512 cells | — |
| 10-18 05:15:04 | Parent asked for a capacity confirmation; confirmed ≤ 2 busy processes for worker + subagent combined (only d01-G was running) | subagent limited to 1 process |
| 10-18 05:17:42 | **d01-G** certified: 20,579,480 leaves (radial 10,348,560 / small 10,202,984 / radial-mvf 8,385 / SKIP-in-P 19,551), 41,152,160 evals, 2142 s. Audit b01-cover-G (05:17:49–05:18:10): tiling_ok, 6800/6800 cells, 19,551 SKIP rules re-checked | all seven charts certified |
| 10-18 05:18:20 | Certificate index i01 (`index_certificates_v2.py`; v1 was never executed and damaged by an editing slip): all seven runs certificate_ok, audits tiling_ok, counts match (`runs/i01-index/certificate_index.json`, sha `edb78933…7b0e`) | — |
| 10-18 05:2x | Proofs written: `proof/me3-theorem-v2.md` (sha `1fcbca21…ef25`) and `proof/me3-theorem-v3.md` (sha `30f6acff…9e87`); v3 changes only the status and the §7 replay bullets to the subagent's final results. Subagent final: `reductions/replay/REPLAY-STATUS-v2.md` (sha `af02cc29…14fd`), 0 violations in P (948 samples plus all 945,680 leaves at midpoints) and in every dual chart sample; mutations flagged | — |
| 10-18 05:29:29 | **Candidate pinned**: `receipts/me3-candidate-pin-v1.json` (sha `8bd1b39e…a859`); manifest `runs/p01-pin/manifest.json` (sha `91542ccd…2453`, 478 files). Status CANDIDATE, full statement with no uncovered pole region; unreviewed, correctness only | parent replay and hostile reviews pending |
| 10-18 05:29:44 | Label corrections from host mtimes: the "05:2x" row should read proof v2 05:19:24, REPLAY-STATUS-v2 05:20:36, proof v3 05:28:52. The SWB row (04:53:56) was appended after the 04:54 checkpoint row; order in this table is append order, not event order | hashes unchanged |
| 10-18 ~05:40 | Parent relayed hostile chart review `review/me3-charts-codex-v1.note.md` (sha `55caa19e…acfb`): **FATAL** — `me3dual_v8.py:28` `3 * (-1) ** j / j` is a Python float (int/int) rounded before Arb, so the SWC coefficients were not enclosed. **Pin v1 and d02-SWC are therefore INVALID** (kept as failed evidence). Also MAJOR dependency gaps (lane_guard, runtime/build identity) and MINORs (checker outcome sets, LD quantifiers). A second review, `review/me3-reductions-codex-v1.note.md` (sha `a6d34ecb…1328`), returned ACCEPT-WITH-FIXES for L1–L6 | repair started |
| 10-18 05:50:53 | **SWC spec v3 frozen** (`receipts/spec-dual-freeze-v3.json`; `code/spec_dual_v3.json` sha `43d2e22e…d936`; `cert_dual_v7.py` sha `72fb546a…4f3f`; `me3dual_v9.py` sha `77a826c0…d341` with c_j = (−2Re(p^j) + 3(−1)^j)/j in ball arithmetic; transitive code hashes recorded) | d03-SWC launched |
| 10-18 05:51:20 | **d03-SWC certified**: 34,304 leaves (corner 815 / corner-mvf 33,489), 68,512 evals, 0 FAIL. Its leaf record is byte-identical to d02's (sha `0b0f7640…db75`; same decisions), but validity rests on d03 | — |
| 10-18 05:53:05–05:54:03 | Hardened checker `check_cover_v3.py` (hard-coded outcome sets and domains, FAIL rejected unconditionally, depth bound, leaf-hash and counts bound to the run summary): b03-cover-P/SWC/LW/LD1/LD2/SWB/G all audit_ok | — |
| 10-18 05:54:36 | Float audit f01 (`audit_float_v1.py`): 269 static sites. Dynamic type trace: 906 sites, 472 exercised, 0 outcome mismatches. Flags only in the G TRIANGLE-angle heuristic (OK-heuristic). DEFECT class = corner coefficients only: v8:28 on a certified path (d02); v7:35 and v3:217/220 dead. Written up in `proof/float-audit-v1.md` | subagent `ME3FloatAudit` is auditing independently (`independent-float-audit/`) |
| 10-18 05:58–05:59 | n04 controls (v9): M4v9 corner at T′ = 3/10 → 70 FAIL; M7v9 positive control certified; M8: the exact Ig₂₀ = 1048575/524288 at (s, ξ) = (0, 1/2) is inside the v9 ball and outside the v8 ball. r01 runtime identity (Python 3.14.3, python-flint 0.9.0, FLINT 3.6.0; interpreter and flint distribution file hashes). s01 binding smoke v1 failed one check (it expected `==` for a 133-bit int at 128 bits; wrong expectation, kept); s02 (v2) all 16 checks pass | — |
| 10-18 05:59:20–06:02:28 | n06/n07 checker-v3 mutation controls: CERT:not-a-test, FAIL, depth 25 > 24, CERT:corner in G, SKIP:in-primal-P in LD2, SWC δ-domain 1/4, G P_r_hi = 4, summary certificate_ok false, and LW leaves against LD1's summary — all 9 rejected for the intended reason. Resource note: n06 read the 20.6M-line G record in memory, peak RSS 3.6 GB for about 3 min (single process; within the math-1 8 GiB total) | — |
| 10-18 06:04:15 | Certificate index v3 (`index_certificates_v3.py`, run i02): all seven charts certified and audited with checker v3; d02-SWC listed INVALID | — |
| 10-18 06:05 | Checkpoint to parent. Parent reply: its primal desk's full replay of P passed (945,680/945,680, own evaluator), its reductions audit passed, and it independently certified v_cos ≥ 0.20090156350055 (`review/me3-parent-primal-reductions-v1/RESULT-v1.json`, sha `9a72e3e7…65e3`); the bound is optional | — |
| 10-18 06:12 | Subagent `ME3Reductions` final: `reductions/proof/reductions-v2.md` (sha `bd497389…1e3f`) and `reductions/STATUS-v2.md` (sha `a644d430…d27e`). Adds the positive-mass hypothesis and relabels the contract-band check EXPLORATORY. Exact certificates: `exact-certs-v1`, 47/47 pass (v_cos ≤ 773/3844 < 11/50; Δ₃ > 553/2000 via h); wrong controls fail. The lower bound is kept OPTIONAL and unused (ctl_f completion requires an empty stack; audit-bnb-v2) | — |
| 10-18 06:15 | Subagent `ME3FloatAudit` final: `independent-float-audit/report-v1.md` (sha `6c9aa985…2ded`). 556 sites, 0 DEFECT on certified paths; the same dead defect sites (v7:35, v3:217/220); floats only in the G-angle heuristic and logging. Errata from its final message: check_cover_v1's hash ends …0b9e, and the header time is 06:15 | concordant with `proof/float-audit-v1.md` |
| 10-18 06:1x | Written: `proof/charts-spec-v2.md` (sha `d401774e…d5437`) and `proof/me3-theorem-v4.md` (sha `98c4389f…8fc6`) | — |
| 10-18 06:18:21 | **Candidate pinned v2**: `receipts/me3-candidate-pin-v2.json` (sha `c9a1eb6d…796c`); manifest `runs/p02-pin/manifest.json` (sha `0079b3dd…17b3`, 686 files, 100 key files). Pin v1 and d02-SWC are kept as INVALID evidence | parent dual desk replay of SWC against d03 pending |
| 10-18 06:19:04 | Label corrections from host mtimes: `proof/float-audit-v1.md` 06:00:08; `proof/charts-spec-v2.md` 06:01:12 (row "06:1x"); `reductions/proof/reductions-v2.md` 06:11:00 and `STATUS-v2.md` 06:12:09 (row "06:12"); `independent-float-audit/report-v1.md` 06:15:16; `proof/me3-theorem-v4.md` 06:17:59. The "~05:40" row is approximate: the parent message arrived between 05:29:44 and the spec-v3 freeze at 05:50:53 | hashes unchanged |
| 10-18 06:2x–06:36 | Parent relayed the hostile delta review of pin v2, `review/me3-charts-v2-delta-codex-v1.note.md` (sha `df03a74a…e474`): the SWC repair PASSES statically and there is no live float defect. Overall INCONCLUSIVE, citing missing snapshot provenance plus findings 1 (MAJOR: theorem v4 §2 writes the cone as `cone{…}`), 3 (checker v3 does not authenticate the spec/summary/run pairing), 4 ("Every dual leaf"), 5 (reductions-v2 LF373: the resultant is 432·h) and 6 (comparison contract overstated) | narrowly versioned repairs; no evaluator or geometry change |
| 10-18 06:40 | Subagent `ME3Reductions`: `reductions/proof/reductions-v3.md` (sha `e5c75b24…b15c`; v2 plus the LF373 fix only), diff `reductions-v3.diff-from-v2.txt` (sha `a8cd11c5…8251`), exact check `resultant-check-v1` (Res = 432·h, monic normalization h/32, the wrong v2 wording evaluates to False), `STATUS-v3.md` (sha `bd081bb7…12f6`) | — |
| 10-18 06:42:51–06:42:53 | **Provenance binding audit b04** (`code/bind_audit_v1.py`, sha `41b3ed03…7ca0`; `runs/b04-bind/binding.json`, sha `99beab1c…e23b`), anchored at pin v2. Checks B1–B6: pin, manifest and key files; freeze receipts (P: hash-record chain); launch receipts; summary identity, including evaluations = 2·leaves − cells; geometry-audit binding; index i02. **All seven charts are bound.** Controls C1, C1b, C2, C3, C4, C5 and C6 are all rejected with their required reasons. C2 (interior SWC breakpoint 1/16 → 1/17) fails only the hash bindings B1/B2/B6, with no identity- or geometry-level failure | — |
| 10-18 06:43:23 | Smoke s03 (`binding_smoke_v3.py`): **failed attempt (kept)**. Its B10a wrongly expected the union-built ball [1, 2] to satisfy `<= 2`; the union's radius is rounded up, so Arb correctly refuses. The other 5 checks pass. Log of [−1, 1], of [0, 1] and of exact 0 all give nan with False comparisons | — |
| 10-18 06:44:44 | Smoke s04 (`binding_smoke_v4.py`, sha `2453d319…97dd`; `binding.json`, sha `963d31b9…6dc5`): comparison contract 6/6. A True comparison is certified; a False one carries no information. Equal exact points satisfy non-strict comparisons, and indeterminate balls compare False | — |
| 10-18 06:45–06:50 | Parent relayed the Claude reductions review `review/me3-reductions-claude-v1.note.md` (sha `68cd8dd9…ed6e`): ACCEPT-WITH-FIXES, 0 FATAL, 0 MAJOR, 6 MINOR. `reductions-v3.md` already existed (resultant fix only), so the single combined version is **reductions-v4** (tasked to `ME3Reductions`). Also written: `proof/float-audit-v1-erratum-1.md` (comparison contract) and `code/pin_candidate_v3.py` | proof v5 and pin v3 follow |
| 10-18 06:58 | Subagent `ME3Reductions` final: `reductions/proof/reductions-v4.md` (sha `be1f7190…6eb1`) is v3 plus Claude MINOR-1…6: Cor 5.7 equality for some minimizer; an exact essential chain via Lemma 4.2 and 773/3844; Lemma 2.4 + 5.1 citations; new **Cor 7.2 (strictness per cone)** with Remark 7.2a; the lower bound relabelled conditional; and housekeeping. Also: diff `reductions-v4.diff-from-v3.txt` (sha `5a6a37f4…b08b`, 15 hunks), `STATUS-v4.md` (sha `1ffe3de8…0e50`) with a static note on ctl_f's exact parsing and NaN handling, and the exact check `alt-route-check-v1` for Remark 5.6a (5/5, with a wrong control failing) | Codex resultant fix retained |
| 10-18 07:0x | `proof/me3-theorem-v5.md` (sha `1504ec69…ec60`) and its exact diff from v4, `proof/me3-theorem-v5.diff-from-v4.txt` (sha `a0cc0323…8585`, 11 hunks). v5 restores the explicit cone K in §2; says "Every CERT leaf", with the SKIP-leaf coverage stated; adds the binding audit b04 to §4 and §6; restates the comparison contract; imports reductions v4; makes D1 cite Cor 5.7; and makes strict D2 cite Cor 7.2 per cone. Erratum `proof/float-audit-v1-erratum-1.md` (sha `1a0f6a94…a636`) | pin v3 next |
| 10-18 07:01:03 | **Candidate pinned v3**: `receipts/me3-candidate-pin-v3.json` (sha `fa9327f2…8b4b`); manifest `runs/p03-pin/manifest.json` (sha `b45d27e8…91f6`, 735 files, 184 key files: charts-spec-v1, every receipt of the active runs and audits, the binding audit and its mutants, smoke s04, proof v5 with its diff, reductions v4 with its diff, and the external review and closure hashes). The pin asserts that binding audit b04 is clean. Pin v2 and proof v4 are SUPERSEDED for document reasons only; pin v1 and d02 remain INVALID | no certificate or evaluator changed since pin v2 |
| 10-18 07:01:13 | Label corrections from host mtimes: erratum 06:48:05; `pin_candidate_v3.py` 06:49:04; reductions-v4 06:56:53 and STATUS-v4 06:58:25 (row "06:58"); proof v5 and its diff 07:00:29 (row "07:0x"). Disk: about 12.74e9 B free at 07:01, close to the 12.2e9 launch gate, cause unknown; the lane totals 151 MB | no further launches planned |
| 10-18 07:02–07:05 | Shared-volume disk event, per parent notices. Free space fell to ~12.44e9 at 07:02, then below the 12e9 floor at ~07:04:1x (11.84e9, observed by another desk), then recovered to 14.5e9 at 07:04:23 through a system-side release; cause unidentified. This lane had **no process running** throughout (one-time check at 07:02:07: none; lane 154,500 KiB, unchanged since 07:01:03), so **no item of this lane was floor-stopped** and nothing is recorded as UNKNOWN. Reported to the parent: no bulk writer | holding new launches; none planned |
| 10-18 07:5x–07:55:10 | Parent delta audit of pin v3 (`review/me3-parent-delta-audit-v1/RESULT-v1.json`, sha `6947d938…3422`; `AUDIT-DELTA-v1.md`, sha `a0b48503…6605`): COVERED-WITH-NOTES, no GAP, 77 exact checks. On the parent's request, wrote the static wording-and-provenance erratum **`proof/me3-theorem-v5-erratum-1.md`** (sha `9f1e72e8…e7b4`, created new, finalized 07:55:10). It covers E1 (N1, "real span" → real-coefficient span including the sine term), E2 (N2, the primal desk audited reductions v1 only; v2–v4 are covered by the delta audit), E3 (N4, δ = 0 points of G SKIP boxes are D1, handled by Cor 5.7), E4 (N5, reductions-v4 LF48–55 header), E5 (N6, the density clause is a consequence of L1(a)(3)) and E6 (N3, the full Lemma M steps, added beyond the request); N7 needs no change. v5, reductions-v4, the charts, the certificates and pin v3 (`fa9327f2…8b4b`) are unchanged (hashes re-checked at 07:55) | no re-pin, per parent |
| 10-18 08:0x–08:15:59 | Final math reviews, relayed by the parent: Claude `review/me3-v5-math-claude-v1.note.md` (sha `65c5ef6e…ae24`), ACCEPT-WITH-FIXES with 0 FATAL, 0 MAJOR and 8 textual MINOR findings; Codex SWC follow-up `review/me3-v5-math-swc-followup-codex-v1.note.md` (sha `acb04f46…67dd`), ACCEPT-WITH-FIXES, whose sole MINOR is the "real span" wording. Wrote the static erratum **`proof/me3-theorem-v5-erratum-2.md`** (sha `bef33e91…243b`, created new, frozen 08:15:59; no computation). It maps m1–m8: m1, real-coefficient basis at LF129–130; m2, Lemma D proved in full (q_θ, Laplace identity, Q_T > 0, SCV equivalence, finite certificates, w and N₁), v3's invalidity limited to its SWC evidence, imports extended to reductions v4 and the replayed leaf predicates; m3, method table for α ≥ 0 (G branches, SWB/SWC Im g, LD candidates, fallback and mvt0), quoting the parent dual derivation (sha `a6b69bba…0273`); m4, LD outer boxes and β_top = 15708/10000 < 3 < π; m5, LD2 SKIP statement restricted to the target domain; m6, physical points and padding faces of G, SW and LW; m7, feasible, a_k, S = S₂, ∂_r at fixed (ω, φ), R_P and P̄ = {1/5 ≤ ω ≤ 40, 0 ≤ δ ≤ 3ω}, with the assignment and the harmless overlap with LD; m8, the D-cone split cited to reductions-v4 L1(a), Lemma 1.2, the normal forms and Cor 2.6. It includes a precedence table against erratum 1. v5, erratum 1, charts-spec-v2, reductions v4 and pin v3 are unchanged (re-hashed at 08:16); the SHA was sent to the parent at about 08:17 | no re-pin, per parent |
| 10-18 08:19–08:22:22 | Codex reductions delta review `review/me3-reductions-v4-delta-codex-v1.note.md` (sha `60d659ed…8825`): ACCEPT-WITH-FIXES with 0 FATAL, 0 MAJOR and 1 MINOR; the earlier six findings are verified fixed. On the parent's request, wrote the static erratum **`reductions/proof/reductions-v4-erratum-1.md`** (sha `4e5564eb…1085`, created new, frozen 08:22:22; no computation). It quotes reductions-v4 LF777–779 verbatim (Remark 7.2a, "If the theorem holds …"; checked byte-identical) and replaces it. The faulty sentence is deleted, "supplies it" becomes "supplies strictness", and the review's repair sentence is appended verbatim: "Once Lemmas D/M and Corollary 7.2 establish strictness on every D2 cone, Corollary 7.1(2) implies that I_2 = v_cos is an unattained infimum." It adds a three-step justification, a note that each cone has a positive gap but there is no uniform gap, and propagation pointers for findings 3 and 5. reductions-v4, STATUS-v4, the v3→v4 diff and pin v3 are unchanged (re-hashed at 08:22). Erratum 2 of this family is reserved for any MINORs from the pending Claude reductions delta review | no re-pin, per parent |
| 10-18 08:23–08:26:38 | Codex review of erratum 2, `review/me3-v5-erratum2-codex-v1.note.md` (sha `d7c7b735…9605`): ACCEPT-WITH-FIXES with 0 FATAL, 0 MAJOR and 3 wording MINORs; m1–m8 all answered. Wrote the static erratum **`proof/me3-theorem-v5-erratum-3.md`** (sha `b1d3de66…ac3d`, created new, frozen 08:26:38; no computation). Each old passage is quoted verbatim and checked byte-identical by script. F1: erratum-2 LF107–108, Q_T defined on ℂ∖{0} with positivity stated for real y > 0. F2: the δ = 0 aside at erratum-2 LF286–287 and erratum-1 LF83–84 (the review's "SOURCE01" is erratum 1, per its prompt manifest): CERT predicates stay valid at δ = 0, but SCV ≥ T for a whole D1 cone needs complete CERT coverage of every s (e.g. 0 < ω ≤ 1/5 or ω > 40); the unrestricted reading is false at ω = 1 (773/3844 < T); unused by the assembly. charts-spec-v2 LF83–84 (LD s-union, δ ≥ 64) makes no D1 claim and needs no change. F3: erratum-2 LF376–377 now reads "a ≥ \|c\| > 0, since the pair contributes" in §2 notation, with no such bound claimed for D2. Precedence: erratum 3 > erratum 2 > erratum 1 > v5. All earlier files and pin v3 are unchanged (re-hashed at 08:26) | no re-pin, per parent |
| 10-18 08:28–08:30:54 | Parent gate verdict `review/me3-minimum-scv-parent-gate-verdict-v1.md` (sha `e4f88f92…c788`): GATE MET, CORRECTNESS-ACCEPTED, NOVELTY-UNCLEAR. Last editorial item: the Claude reductions delta review `review/me3-reductions-v4-delta-b-claude-v1.note.md` (sha `69368845…30ba`), ACCEPT-WITH-FIXES with 0 FATAL, 0 MAJOR and 4 editorial MINORs, essential path accepted as written. Wrote the static erratum **`reductions/proof/reductions-v4-erratum-2.md`** (sha `6e644c4a…494c`, created new, frozen 08:30:54; no computation). All seven old passages are quoted verbatim and checked byte-identical by script. MINOR-A: v_cos := inf SCV(f_{ω,φ}) defined in the §5 Setting (LF464–465), independent of rate and of the cos² convention by Lemma 1.4, attained by Thm 5.6; LF20–21 reworded (with reading notes for LF469 and LF547). MINOR-B: LF553–554 replaced by the review's wording (1/5 in window and tail, 21/104 > 0.2014, 773/3844 < 1/4 < Δ3). MINOR-C: LF424–425 "Consequently, since (3) gives s(x1) < 1/3 < 1/2 < s(x3) < s(x2), …", with distinctness made explicit. MINOR-D: m* → v* (LF534–538), m_K → v_K (LF770–774). Notes: N1, LF777–778 is already handled by reductions-v4 erratum 1; N2, LF339–340 now cites the Remark 2.3a(2) majorant. Precedence: erratum 2 > erratum 1 > v4. All earlier files and pin v3 are unchanged (re-hashed at 08:31). **ME3 work complete** | no re-pin, per parent |
