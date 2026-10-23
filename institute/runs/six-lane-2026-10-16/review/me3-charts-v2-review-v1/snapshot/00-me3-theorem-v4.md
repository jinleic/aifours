# Minimal SCV of ME(≤3) — integration proof, version 4 (repaired worker candidate)

Worker `MathPhaseType3`, lane `mathematics/evidence/six-lane-20261016/me3-minimum-scv/`, 2026-10-18 PDT.

**Status.**
* This is a worker candidate, pinned in `receipts/me3-candidate-pin-v2.json`.
* Correctness only. There is no novelty, priority or "first" claim.
* v1–v3 are kept unchanged. **v3 and pin v1 are INVALID.** Their corner chart SWC rested on run d02, whose library
  `me3dual_v8.py:28` rounded the series coefficients 3(−1)^j/j to binary floats before ball arithmetic. Hostile review
  `review/me3-charts-codex-v1.note.md` (sha 55caa19e…acfb), finding 1, FATAL.
* v4 makes these changes:
  1. **SWC repaired.** The chart now uses `me3dual_v9.py`, exact coefficients, spec v3 and run d03-SWC (§4).
  2. **Reductions v2 imported.** It adds an explicit positive-mass hypothesis, gives an exact rational upper
     separation for v_cos and an exact certificate for Δ₃, relabels the contract-band check as exploratory, and keeps
     the lower bound on v_cos optional and unused (§1). Source: review `review/me3-reductions-codex-v1.note.md` (sha
     a6d34ecb…1328).
  3. **Narrower LD1/LD2 quantifiers.** They now range over the physical domain, and the s-coverage is stated as a
     union (`proof/charts-spec-v2.md`).
  4. **Hardened coverage audits.** `check_cover_v3.py` is used for all seven charts.
  5. **Float-contamination audits.** One audit is by the worker; an independent one is by a subagent (§6).
  6. **Dependency closure.** The runtime identity and the binding-semantics smoke are recorded; trusted imports are
     separated from audited code (§6).
  7. **Parent replay.** The parent's full replay of chart P passed (§7).

## 0. Statement

**Theorem.** Let X be a continuous ME(≤3) law; its density f satisfies f ≥ 0, ∫f = 1 and ∫(1+t²)f < ∞. Then
SCV(X) = m₀m₂/m₁² − 1 ≥ v_cos, where v_cos := min_{ω>0, φ∈ℝ} SCV(e^{−t}(1 − cos(ωt − φ))). Moreover:
* the minimum is attained in the cos family (case D1);
* densities with only real exponents have SCV ≥ Δ₃ > 553/2000;
* every density in a strictly-dominant-real-pole cone (case D2) has SCV > v_cos.

Imports:
* finite-dimensional convexity, the mean value theorem, Taylor's theorem with remainder, and power series of log;
* the correctness of FLINT 3.6.0 / Arb outward-rounded ball arithmetic;
* the python-flint 0.9.0 conversion semantics listed in §6.

## 1. Reductions imported (`reductions/proof/reductions-v2.md`, sha bd497389…1e3f; `reductions/STATUS-v2.md`, sha a644d430…d27e)

Reductions v1 (sha ad6c5091…5536) is kept. Parent audit PASS: `review/me3-parent-primal-reductions-v1/RESULT-v1.json`,
sha 9a72e3e7133de30301785af96604b31838b9726d94055717291f3111744c65e3, run x01-red-checks.

* **L1–L2.**
  * Domain: measurable f ≥ 0 with 0 < ∫f and ∫(1+t²)f < ∞ (positive-mass hypothesis; Remark 2.3a shows every
    application satisfies it).
  * Continuous ME(≤3) densities are the normalized nonzero elements of the cones K_E (|E| ≤ 3).
  * SCV is scale- and time-scale invariant.
  * SCV/(1+SCV) = min_θ R_θ, with R_θ(f) = ∫(t−θ)²f/(θ²∫f).
  * Cone minima are attained on extreme rays.
  * Assembly: inf over ME(≤3) = min(I_R, I_1, I_2).
  * Inclusion K_E ⊆ K_{E′}.
* **L3–L4, exact.** Real exponents give SCV ≥ Δ₃, where Δ₃ is the root in [1/4, 1/3] of
  h(y) = 32y³ − 144y² + 135y − 27.
  * h′(y) = 96(y − 3/2)² − 81 ≥ 149/3 > 0 on [1/4, 1/3].
  * h(553/2000) = −1293623/250000000 < 0, hence Δ₃ > 553/2000 = 0.2765.
  * Verification is exact (Fractions) in `reductions/runs/exact-certs-v1/exact_certs.json`, sha b18d5163…0a04: 47/47
    checks, with wrong controls failing.
* **L5, exact upper separation.** In the D1 moment formula with ω = 1, cos φ = 35/37 and sin φ = 12/37:
  * (m₀, m₁, m₂) = (27, 62, 171)/74 and SCV = 773/3844 < 1007/5000 < 11/50.
  * Hence **v_cos ≤ 773/3844 < T = 11/50 and v_cos < 553/2000 < Δ₃**.
  * Attainment holds by continuity, the proven uniform tails and phase periodicity (Thm 5.6; the minimizer has
    1/4 < ω < 4).
  * The Arb point bound U and the lower bound v_cos ≥ 0.20090156350055 are **optional and unused**. The lower bound
    is certified twice:
    * by the subagent's `ctl_f_d1bnb_v1.py` (sha 508b1488…41b7), with empty-stack completion;
    * independently by the parent desk (RESULT-v1 run d1b-lower-worker-L).
  * The contract-band check of `ctl_c_vcos_v2.py` is EXPLORATORY: it tests the Newton value, and its STOP only prints.
* **L6.** In D2 (real pole 1, pair 1 + ξ and 1 + ξ̄, ξ = δ − iω, δ, ω > 0, r = δ/ω):
  * the extreme rays are e^{−t}h_τ with φ = ωτ ∈ [0, θ₁(r)];
  * θ₁ is C¹ and strictly decreasing, from 2π to π;
  * m_k = k!(1 − Re(cζ^{k+1})), with c = (1 − ir)e^{(r−i)φ} and ζ = 1/(1 + δ − iω).

Constants: T = 11/50, κ = 1/(1+T) = 50/61 and ρ = T/(1+T). By L5, v_cos ≤ 773/3844 < T.

## 2. Lemma D (unchanged from v3 §2)

Every f ∈ K = cone{e^{−t}, e^{−(1+ξ)t}, e^{−(1+ξ̄)t}} with f ≥ 0 has the form f = e^{−t}H with
H = a + Re(ce^{−ξt}) ≥ 0 and a ≥ 0. Let Q_T(y) = (κy² − 2y + 2)/y³ > 0 for y > 0.

**Lemma D.** Suppose that for every θ > 0, W(θ) := Q_T(θ(1+ξ))/Q_T(θ) equals some finite sum Σλ_k e^{−ξt_k} with
λ_k ≥ 0, Σλ_k ≤ 1 and t_k ≥ 0. Then SCV ≥ T on K∖0.

*Proof.* As in v3: ∫q_θ f = θ³Q_T(θ)[a + Re(cW)], and a + Re(cW) = (1 − Σλ_k)a + Σλ_k H(t_k) ≥ 0. ∎

Certificate forms:
* RADIAL: there is an argument α ≥ 0 of W with |W| ≤ e^{−δα/ω}.
* SMALL: |W| ≤ e^{−2πδ/ω}.
* TRIANGLE: W = a′ + b′e^{−ξt′} with a′, b′ ≥ 0, a′ + b′ ≤ 1 and t′ ≥ 0.

Hostile review verdict: Lemma D and all three certificates are valid, including the zero cases.

Parametrization: s = θ/(1+θ), W = zz(w₁ + zz(w₂ + zz·w₃)) with zz = 1/(1+ξ).

## 3. Lemma M (unchanged from v3 §3; review verdict: valid)

Chart P = [0, 3] × [1/5, 40] × [0, 31416/5000] in (r, ω, φ). Run c03 tiles P into 945,680 boxes:
* INFEAS: 46,344;
* SGE (S > T): 891,318;
* DPOS (a₀, a₁, a₂ > 0 and ∂_r S > 0): 8,018.

**Lemma M.** Every feasible (r₀, ω₀, φ₀) ∈ P with r₀ > 0 has S > v_cos.

*Proof.* If S ≥ T > v_cos we are done. Otherwise put σ(r) = S(r, ω₀, φ₀) on [0, r₀].
1. The path stays feasible and inside P, because θ₁ is decreasing.
2. Let r* = inf{r : σ < T on [r, r₀]}. On (r*, r₀], every covering leaf is DPOS, so σ is strictly increasing there.
3. r* > 0 would force σ(r*) ≥ T > σ(r₀) ≥ σ(r*), a contradiction. So r* = 0.
4. Hence σ(r₀) > σ(r₀/2) ≥ σ(0) ≥ v_cos. ∎

## 4. Far region: six dual charts, all certified (SWC repaired)

Specification: `proof/charts-spec-v2.md` (sha d401774e…d5437). It supersedes v1 (5a43c252…1ff1) in exactly four
points: the SWC coefficients, the LD physical-domain quantifiers with the s-union, the checker v3, and the version
table.

| Chart | Assigned set | Run (spec; driver + library) | Leaves (outcomes) | Audit (check_cover_v3) |
|---|---|---|---|---|
| P | ω ∈ [1/5, 40], δ ≤ 3ω | c03 (spec_primal_P_v1; cert_primal_v3) | 945,680 (SGE 891,318 / DPOS 8,018 / INFEAS 46,344) | b03-cover-P ✓ |
| G | δ ∈ [0, 64], ω ∈ [1/5, 640] minus P | d01-G (spec_dual_v1; cert_dual_v5 + me3dual_v7) | 20,579,480 (radial 10,348,560 / small 10,202,984 / radial-mvf 8,385 / SKIP-in-P 19,551) | b03-cover-G ✓, 19,551 SKIP re-checked |
| SWB | δ ∈ [3/10, 64], 0 < ω ≤ 1/5 | d01-SWB (spec_dual_v1; cert_dual_v5 + me3dual_v7) | 8,196,408 (bedge 8,144,675 / bedge-mvf 51,733) | b03-cover-SWB ✓ |
| **SWC** | δ ∈ [0, 3/10], 0 < ω ≤ 1/5 | **d03-SWC (spec_dual_v3; cert_dual_v7 + me3dual_v9)** | 34,304 (corner 815 / corner-mvf 33,489) | b03-cover-SWC ✓ |
| LW | δ ∈ [0, 64], ω ≥ 640 | d01-LW (spec_dual_v1) | 1,250 (small) | b03-cover-LW ✓ |
| LD1 | δ ≥ 64, s ∈ [1/16, 1), physical points | d01-LD1 (spec_dual_v1) | 5,954 (ld1) | b03-cover-LD1 ✓ |
| LD2 | δ ≥ 64, s ∈ (0, 1/16], physical points | d01-LD2 (spec_dual_v1) | 57,813 (ld2 56,933 / SKIP 880) | b03-cover-LD2 ✓, 880 SKIP re-checked |

Every run has certificate_ok, 0 FAIL and no cap hit.

**Audits.** Checker v3 hard-codes each chart's outcome set, domain, parameters and variable order; it rejects FAIL
unconditionally, checks every depth against max_depth, and verifies each leaf file's line hash and counts against the
run summary. Index: `runs/i02-index/certificate_index.json`, sha 0880b038…4020.

**SWC repair.**
* Spec v3 (sha 43d2e22e…d936) was frozen at 05:50:53 in `receipts/spec-dual-freeze-v3.json`, with the transitive code
  hashes, before d03 ran.
* d03 computes c_j = (−2Re(p^j) + 3(−1)^j)/j in ball arithmetic.
* Its leaf record is byte-identical to d02's (leaves sha 0b0f7640…db75, lines sha b664505e…f77c). The rounding
  flipped no decision, but validity rests on d03 alone.

**Coverage of D2** (charts-spec-v2):
* δ ≥ 64: LD1 ∪ LD2, physical points, all s ∈ (0, 1).
* δ < 64 and ω ≥ 640: LW.
* δ < 64 and ω ∈ [1/5, 640]: P or G.
* δ < 64 and ω < 1/5: SWC (δ ≤ 3/10) or SWB (δ ≥ 3/10).

Every dual leaf certifies RADIAL, SMALL or TRIANGLE at each physical point of its box. By Lemma D every density with
dual-assigned poles has SCV ≥ T > v_cos.

## 5. Assembly

Let X be a continuous ME(≤3) law.
* Real exponents: SCV ≥ Δ₃ > 553/2000 > 773/3844 ≥ v_cos.
* Otherwise, after time scaling, X lies in a D cone.
  * D1: SCV ≥ v_cos by definition.
  * D2 with dual-assigned poles: SCV ≥ T > 773/3844 ≥ v_cos.
  * The remaining D2 cones (ω ∈ [1/5, 40], r ≤ 3): the cone minimum is attained on an extreme ray (L2), and every
    extreme ray has S > v_cos (Lemma M).
* Attainment: L5. ∎

## 6. Dependencies, trusted imports and audited code

**Trusted (imported, not proved here).**
* FLINT 3.6.0 / Arb outward-correct ball arithmetic: elementary functions, comparisons, union, intersection and
  upper().
* Python 3.14.3 semantics.
* python-flint 0.9.0 conversions:
  * Python ints enter exactly or as enclosing balls, never via float;
  * fmpq becomes an enclosing ball;
  * a float becomes its exact binary value;
  * comparisons of overlapping or non-finite balls are False.

These binding semantics were **smoke-tested** on the installed build in run s02 (`code/binding_smoke_v2.py`, sha
8db84074…eaccc; `binding.json`, sha e4414ccc…19e7; 16/16). This is not a proof. s01 is kept: one wrong expectation
about a big integer.

**Runtime identity** (run r01, `runtime.json`, sha 679b845e…7ce2):
* interpreter `/opt/homebrew/Cellar/python@3.14/3.14.3_1/…/bin/python3.14` with its sha;
* the framework library sha;
* sha and size of every file of the python-flint package and distribution (103 + 12 files).

All certified runs used this venv (`run_v1.sh`).

**Audited (Python code on certified paths).**
* **Float contamination, worker audit** `proof/float-audit-v1.md` (sha e04753f8…1c8c), run f01:
  * 269 static sites;
  * a dynamic type trace over 906 sites, 0 outcome mismatches.
* **Independent subagent audit** `independent-float-audit/report-v1.md` (sha 6c9aa985…2ded): 556 sites classified,
  **0 DEFECT on certified paths**, with an AST-scan cross-check. Its errata, which the file cannot correct because it
  is create-once, were reported in its final message: check_cover_v1's hash ends …0b9e, and the header time should
  read 06:15.
* **Concordance.** Both audits find exactly one defect class, the corner coefficient 3(−1)^j/j:
  * live only in v8:28 (d02, invalid);
  * dead in v7:35, v3:220 and v3:217.

  Both find floats only in the G-chart TRIANGLE-angle heuristic. That heuristic gives θ′ ≥ 31415/10⁴ > 0, which is
  all TRIANGLE needs, and in logging.
* **Unused v3 B-edge test.** The independent audit also notes that unused `me3dual_v3.test_bedge` could map a NaN C
  to 0. The live `me3dual_v6.test_bedge` guards this with finiteness checks.
* **lane_guard.py** (sha 5589b0a7…a484; source pinned) has no arithmetic. On import it disables deletion, rename and
  tempfile creation, and provides exclusive-create helpers.
* **Spec binding limit.** The launcher's receipts hash code, not spec JSONs. The specs are bound instead by:
  * the dual freeze receipts v1/v2/v3;
  * the primal spec's creation before c03 (mtime 03:32:03, before the c03 pre-receipt at 03:32:09);
  * the indexes and pin manifests;
  * the parent's re-hash, which found it unchanged.

**Not done.** No Lean or kernel check; no human referee. This is not the book's general minimal-representation
question.

## 7. Controls and replays

* **n01 controls** (v3): M1–M6 as intended.
* **n04 controls** (v9):
  * the corner test FAILs at T′ = 3/10, with 70 FAIL boxes;
  * a positive control certifies;
  * coefficient exactness: the exact Ig₂₀ = 1048575/524288 at (s, ξ) = (0, 1/2) lies inside the v9 ball and outside
    the v8 ball.
* **Checker mutants** n02/n03 (v2) and n06/n07 (v3). All nine v3 mutants are rejected for the intended reason:
  * an unknown CERT tag, and FAIL;
  * depth 25 > 24;
  * a CERT:corner leaf in G, and a SKIP:in-primal-P leaf in LD2;
  * a wrong SWC δ-domain, and a wrong G P_r_hi;
  * a summary not certificate_ok, and a mismatched summary.
* **Parent primal desk**, own evaluator (RESULT-v1, sha 9a72e3e7…65e3):
  * full replay of chart P: 945,680/945,680 leaves, 61,440/61,440 cells;
  * reductions audit: PASS.
* **ME3Reductions point replay** (`reductions/replay/REPLAY-STATUS-v2.md`): 0 violations in P and in every dual sample.
  The SWC samples apply to d03's identical boxes.
* **Parent dual desk replay** of all dual charts, with SWC against d03: pending after pin v2.

## 8. Invalid or superseded evidence (kept)

* Pin v1 (`receipts/me3-candidate-pin-v1.json`) and proof v3.
* Run d02-SWC, with `me3dual_v8.py`, `cert_dual_v6.py`, `spec_dual_v2.json` and `receipts/spec-dual-freeze-v2.json`.
* Calibrations k01–k05; the damaged or never-executed libraries me3dual_v1 and me3dual_v5; and index_certificates_v1.
  `me3dual_v4.py` was never executed as its own chart library. Its `test_ld1` and `test_ld2` are superseded (dead),
  while its `W_generic`, `W_enclosure` and `test_general` are live in chart G via `me3dual_v6`.
* Binding smoke s01; reductions audit-bnb-v1.
