# Lean formalization: random 3-SAT at 4.26718, 4-SAT at 9.934, 5-SAT at 21.123, general arity

Owner lane: `physics/evidence/hard-continuation-20261015/formal/` (phys-p0422 continuation,
2026-10-15 PT). Compact hand-off for the parent: [`handoff/`](handoff/README.md).

## Result

Lean 4.24.0 with Mathlib `f897ebcf` kernel-checks the following theorems. Only
`propext`, `Classical.choice` and `Quot.sound` are used. There is no `sorry`, extra axiom or
`native_decide`.

```lean
-- KSatUpper/Threshold.lean
theorem KSatUpper.satisfiabilityProbability_4SAT_tendsto_zero :
    Tendsto (fun n : ℕ => satisfiabilityProbability 4 n (249*n/25)) atTop (nhds 0)
theorem KSatUpper.satisfiabilityProbability_5SAT_tendsto_zero :
    Tendsto (fun n : ℕ => satisfiabilityProbability 5 n (1057*n/50)) atTop (nhds 0)
-- continuation laws L4/L5 (six atoms), compatibility rows of certificates/trials.json
theorem KSatUpper.satisfiabilityProbability_4SAT_9934_tendsto_zero :
    Tendsto (fun n : ℕ => satisfiabilityProbability 4 n (4967*n/500)) atTop (nhds 0)
theorem KSatUpper.satisfiabilityProbability_5SAT_21123_tendsto_zero :
    Tendsto (fun n : ℕ => satisfiabilityProbability 5 n (21123*n/1000)) atTop (nhds 0)
-- regression control: the new general route reproduces the upstream k = 3 endpoint
theorem KSatUpper.satisfiabilityProbability_3SAT_tendsto_zero :
    Tendsto (fun n : ℕ => satisfiabilityProbability 3 n (1067*n/250)) atTop (nhds 0)
-- KSatUpper/ThresholdK3.lean: six-atom k = 3 law, chunked kernel certificates (≤ 4 GiB)
theorem KSatUpper.satisfiabilityProbability_3SAT_42672_tendsto_zero :
    Tendsto (fun n : ℕ => satisfiabilityProbability 3 n (2667*n/625)) atTop (nhds 0)
theorem KSatUpper.satisfiabilityProbability_3SAT_426718_tendsto_zero :
    Tendsto (fun n : ℕ => satisfiabilityProbability 3 n (213359*n/50000)) atTop (nhds 0)

-- KSatUpper/GeneralThreshold.lean: every arity k = m+1, every finite rational trial law
theorem KSatUpper.tendsto_zero_of_criterion {p : ℕ} (T : TrialLaw p) (m : ℕ) {α : ℝ}
    (hα : 0 ≤ α) (cutoff : ℕ) (hΨ : Criterion.finiteAnalyticBound T m α cutoff < 0) :
    Tendsto (fun n : ℕ => satisfiabilityProbability (m + 1) n ⌊α*n⌋₊) atTop (nhds 0)
```

`satisfiabilityProbability k n M` (`KSatUpper/Model.lean`, 49 lines and Mathlib-only) is the
fraction of satisfiable formulas among all `Fin M → Clause k n`. A clause is an injective
ordered `k`-tuple of variables with `k` falsifying signs, so `M` iid uniform legal signed
clauses are drawn with replacement. `249*n/25 = ⌊9.96 n⌋`, `1057*n/50 = ⌊21.14 n⌋`,
`4967*n/500 = ⌊9.934 n⌋`, `21123*n/1000 = ⌊21.123 n⌋`, `2667*n/625 = ⌊4.2672 n⌋` and
`213359*n/50000 = ⌊4.26718 n⌋`.
This is the model of the frozen contract and of the written proof
`institute/runs/hard-2026-10-15/problems/phys-p0422/attack-e2/notes/PROOF.md`.

`Criterion.finiteAnalyticBound T m α T₀` is exactly `Psi_T` of PROOF.md §1 for arity
`k = m+1`:
`-Σ_{j=1}^{T₀} μ_j²/j - m α E log(1 - R_1⋯R_{m+1})`, with
`μ_j = Σ_i (-1)^i C(j,i) exp(((m+1)α/2)(ν_i - 1))` and `ν_i = E(1 - R_1⋯R_m)^i`.
The moment `ν_i` is stated as an exact rational (`TrialSpec.markMoment`) and proved equal to
the product-law integral (`Trial.integral_mark_pow`).

Kernel certificates are in `KSatUpper/Certificates.lean`. Each one is a `decide +kernel` over
exact rationals, taking about 45 s:

| arity | α | trial law | proved bound on `Psi_128` |
|---|---|---|---|
| 4 | 249/25 | rates 1745, 7707, 4454; weights 2946, 3363, 3691 (/10000) | `≤ -1/1000` |
| 5 | 1057/50 | rates 5391, 3691, 7344; weights 1009, 6190, 2801 (/10000) | `≤ -1/2500` |
| 4 | 4967/500 | six-atom law L4, `TrialData.trialL4` | `≤ -1/20000` |
| 5 | 21123/1000 | six-atom law L5, `TrialData.trialL5` | `≤ -1/100000` |
| 3 (control) | 1067/250 | 1/20, 2/5, 17/20; 1/4, 1/2, 1/4 | `≤ -1/100000` |

L4 and L5 are copied from `physics/evidence/hard-continuation-20261015/certificates/trials.json`
(SHA-256 `1cdc03c2…0913e`, rows `k4_T128` and `k5_T128`).

The kernel-checked control theorems `control4_low` and `control5_low` prove the certificate
value is positive at 9.90 (k=4) and 21.10 (k=5) with the three-atom laws.
`controlL4_low` and `controlL5_low` do the same at 9.926 and 21.118 with L4 and L5, just
below the certified densities.

The T=512 headline row (`k4_T512`, α = 3973/400 = 9.9325) is **UNKNOWN**. A
precision-parameterized certificate (output grid `2^-600`) evaluates to about -0.000006, at
most -1/200000, in 123 s (2.25 GB RSS). That is evaluation, not proof. The kernel
`decide` of the same value reached 10.4 GB RSS after 30 s and was stopped by the 6 GiB
watchdog. No T=512 statement is claimed; see `archive/t512-attempt/`.

`NumericalCriterion.finiteAnalyticBound_le_cert` proves for every input that the computed
value bounds `Psi` from above. The exponentials use the tangent bound with outward rounding
after 160 squarings. The alternating sums use signed interval arithmetic. The edge term uses
exact moments `E(R_1⋯R_{m+1})^h = C_h^{m+1}` with a proved geometric tail.
`audit/EvalCertificateValues.lean` evaluates the same functions and gives -0.001463,
-0.000463 and -0.000011. These match the earlier Python producers: k=4 gave -0.0014626, k=5
gave -0.00046294, and the k=3 reference -0.0000112.
`audit/EvalContinuationValues.lean` gives -0.000055 (L4 at 9.934) and -0.000012 (L5 at
21.123). It also gives +0.001794 and +0.000649 at 9.90 and 21.10, and +0.000380 and
+0.000132 at 9.926 and 21.118.

## Random 3-SAT below 4.268: chunked kernel certificates

Added 2026-10-16. The law is the six-atom k=3 law of the rows `k3_T128_compat_4.2672` and
`k3_T128_compat_4.26718` of
`physics/evidence/hard-continuation-20261015/k3-extension/certificates/compat-trials.json`
(SHA-256 `7b0d2615…c93ad044`), copied as exact rationals into `KSatUpper/TrialDataK3.lean`.

- **Edge truncation `N = 256`.** The maximum rate is `u = 239949/250000 ≈ 0.96`, so
  `u^3 ≈ 0.884` and the proved geometric tail `m α (u^3)^(N+1)/(1-u^3)` matters. At α = 4.2672
  it is 0.0247 for `N = 64`, 9.3e-6 for `N = 128`, 3.5e-9 for `N = 192` and 1.3e-12 for
  `N = 256` (`logs/eval-k3-values.log`), against certified margins of order 1e-7.
- **Certificates.** `CertificatesK3.cert_42672 : certUpper … (2667/625) 128 256 u ≤ -1/500000`
  (value -2.4918e-6) and `cert_426718 : certUpper … (213359/50000) 128 256 u ≤ -1/2000000`
  (value -6.537e-7).
- **Controls.** `CertificatesK3Controls.control_42671_low` and `control_426717_low` prove
  `0 < certUpper` for the same law at 4.2671 (+6.70e-6) and 4.26717 (+2.65e-7). Comparator
  rejects the endpoint statements with densities altered to 4.2671 and 4.26717. The kernel
  rejects four altered inputs: the 4.2671 moments with the 4.26718 bound, the bound -1/250000
  at 4.2672, the `N = 256` edge literal against `N = 64`, and one table entry raised by `2^-160`.

**Memory finding (correction).** One `decide +kernel` over `certUpper` at `T = 128` peaks at
about 12 GB of RSS. This holds for every monolithic certificate, including the earlier accepted
ones in `Certificates.lean` (the L4 certificate measured 12.2 GB on 2026-10-16). Their earlier
build, Comparator and fresh-replay runs were not memory-measured, and this README did not say
so; they exceed the lane's 4 GiB per-process target and were not re-run. Probes
(`archive/k3-memory-probes/`) put the cost in the exponential table plus the alternating vertex
sums (about 9.4 GB above the 2.7 GB import base); `ν_j` and the edge sum are negligible.

**Chunked design.** `NumericalCriterionTables` proves, without computation, that `certUpper`
equals the same expression with any literal table that agrees with the computed one entry by
entry, that the vertex term can be computed from the alternating moments `momentLower`, and
that a rational bound on the edge term can be substituted on either side.
`tools/gen_k3_tables.py` materializes table entries, moments and edge bounds as dyadic literals
(`K3Data`, data only), and each literal group is re-proved from its definition by its own small
`decide +kernel` module. Per density there are 22 table chunks (6 entries each), 15 moment chunks
(at most 600 summands), one edge bound and one final value: 156 check modules for the four
densities. Each was built alone under a 4 GiB RSS watchdog (`tools/watch_cmd.py`); the largest
peak was 3.46 GB including the import base (`logs/memory-k3.jsonl`). The statements are those of
the superseded monolithic module, which completed at 12.5 GB and is kept in
`archive/k3-monolithic-12GiB/`. `ThresholdK3` imports no monolithic certificate, so its whole
closure can be replayed within the cap.

**T = 256 (`k3_T256_compat_4.26685`): UNKNOWN.** The interpreted, precision-parameterized value
(output grid `2^-300`, `N = 512`) is -4.18e-7, within -3/10000000, and +5.06e-7 at 4.26684. That
is evaluation, not proof. The monolithic kernel run was stopped by the 6 GiB watchdog at 6.4 GB
after 17 s (`archive/k3-t256-attempt/`); a chunked T = 256 run was not attempted.

## What was generalized

The starting point is upstream [yamelton/sat-upper-4268](https://github.com/yamelton/sat-upper-4268) at commit
`87fb64825b24159418aa0cdca830a76a9d85ff84` (Apache-2.0; tree `bf6bf190`). It is a complete
k=3-only development with a hard-coded `Fin 3`, cubic remainder, coefficients 1/2/3, a
`(1067/250)` density and four equally likely labels.
`tools/check_upstream_derivation.py` classifies our 60 modules (4,126 lines):

- **20 verbatim**: identical after `SatUpper → KSatUpper`. These are generic, such as the
  integer minimum, Poisson configurations, replica moments, log series, Gibbs ratio,
  variance, exponential grid and enclosures.
- **32 derived**: rewritten for arity `m+1` and weighted trial laws. The changes cover:
  - the degree-`(m+1)` remainder `B^(m+1)-(m+1)BC^m+mC^(m+1) ≥ 0`, by an induction plus
    PROOF.md (F) as a closed factorization;
  - insertion factors for `m+1` literals;
  - `m`-warning sites;
  - binomial/Poisson replacement with coefficients `1, m, m+1`;
  - site laws over `Fin m`;
  - the distinct-variable transfer `n^k/(n)_k ≤ exp(k²/n)` for `2k ≤ n`;
  - de-Poissonization;
  - general `α`.
- **8 new**: `TrialSpec` and `Trial` (weighted trial laws and their integrals),
  `ReplicaPoly` (which replaces `ReplicaCubic`), `Criterion`, `NumericalCriterion`,
  `TrialData`, `Certificates` and `GeneralThreshold`. The upstream `Witness`,
  `WitnessVertex`, `TrialFields`, `Numerical*`, `ReplicaCubic` and `LogEnclosures` have no
  counterpart; their roles are taken by these modules.

Since 2026-10-16 the library has 223 modules (20 verbatim, 32 derived, 171 new); 156 of the new
ones are generated `K3Check*` modules.

The upstream k=3 project builds here unchanged in 96 s, and its endpoint uses only the
three standard axioms (`logs/upstream-build.log`, `logs/upstream-axioms.log`). This
development imports no upstream module; every proof is re-checked by our own build.

## Verification performed

| check | result | evidence |
|---|---|---|
| `lake build` (61 modules incl. root), after adding L4/L5 | success, no warnings, 389 s | `logs/build-3.log` |
| axiom union over all 682 `KSatUpper` constants (534 theorems) | `propext, Quot.sound, Classical.choice` | `logs/audit-final.log` |
| endpoint `example`s against the displayed statements, all 5 | pass | `audit/Audit.lean` |
| lexical scan (sorry/admit/axiom/native_decide/…; positive and comment controls) | 60 files, 0 flagged | `logs/scan-library.json` |
| Comparator, endpoints (5 theorems: 9.96, 21.14, 9.934, 21.123, 4.268) | `Solution valid.`, `Your solution is okay!`, 240 s | `comparator/receipts/endpoints.json` |
| Comparator, general theorem | accepted, 55 s | `comparator/receipts/general.json` |
| Comparator controls: match / changed statement / `sorry` / extra axiom / changed def | 1 accepted; 4 rejected with the expected messages | `comparator/receipts/control-*.json` |
| Comparator altered-density controls on real targets: 9.90 (old k=4), 9.926 (L4), 21.118 (L5); `∀→∃` in `Violates` | all rejected (statement mismatch; `Const does not match … Violates`) | same |
| lean4checker v4.24.0 replay of every declaration of all 61 modules (before L4/L5) | 0 failures (735 s) | `logs/lean4checker-modules.log` |
| lean4checker `--fresh KSatUpper.Threshold`, final module including L4/L5 (all imported constants, fresh kernel environment) | EXIT 0, 1178 s | `logs/lean4checker-fresh-Threshold.log` |
| kernel-level altered-input controls (8) | all rejected: density 9.90 and 21.10 certificates, k=5 bound tightened to -1/2000, L4 at 9.926, L5 at 21.118, wrong arity, wrong density, invalid weights | `controls/receipt.json` |
| kernel-checked control theorems | `0 < certUpper` at 9.90 and 21.10 (three-atom laws) and at 9.926 and 21.118 (L4/L5) | `Certificates.control*_low` |
| T=512 headline (L4, 9.9325) | **UNKNOWN**: kernel `decide` stopped at 10.4 GB RSS after 30 s (6 GiB cap) | `archive/t512-attempt/` |
| k=3 chunked: 156 check modules, 2 assembly modules and `ThresholdK3`, each built alone under a 4 GiB cap | all succeeded; max peak 3.46 GB | `logs/memory-k3.jsonl` |
| full `lake build` (224 modules) and audit (1074 constants, 902 theorems), under the cap | success, no warnings; axioms `propext, Quot.sound, Classical.choice` | `logs/build-5.log`, `logs/audit-final.log`, `logs/memory-final.jsonl` |
| lexical scan after the k=3 work | 223 files, 0 flagged | `logs/scan-library.json` |
| Comparator, k=3 endpoints (4.2672, 4.26718) | accepted, 161 s, peak 3.40 GB | `comparator/receipts/endpoints-k3.json` |
| Comparator, general theorem (rerun) | accepted, 55 s, peak 3.49 GB | `comparator/receipts/general.json` |
| Comparator altered-density controls 4.2671 and 4.26717 | both rejected (statement mismatch) | `comparator/receipts/control-EndpointsWrongDensityK3*.json` |
| lean4checker `--fresh KSatUpper.ThresholdK3` (every imported constant, Mathlib included, fresh kernel environment) | EXIT 0, 919 s, peak 3.65 GB | `logs/lean4checker-fresh-ThresholdK3.log` |
| kernel-level k=3 controls (4) and the three cheap old controls, rerun under the cap | all rejected as expected | `controls/receipt.json` |

The rows above the k=3 rows ran before the memory finding; their monolithic certificate checks
used about 12 GB per process.

On the T=512 bottleneck: the following is [INFERENCE], not a profile. The exact rational
moments `ν_j` for `j ≤ 512` have denominators up to about `10^(18·512)`, roughly 30k bits,
and there are about 131k terms. The kernel caches every intermediate value. The exponential
table, at about 513 × 620 squarings of 2.5k-bit numbers, is much smaller. Materializing
table entries as literals would not remove the cost of `ν_j`. Bounding kernel memory would
need outward-rounded interval enclosures of `ν_j`, chunked into separate `decide`
theorems, which is a redesign rather than a small change. Falsifier: a T=512 run that
measures the RSS of the `ν_j` stage alone.

## Exact trust base and limits

- **Trusted**: the Lean 4.24.0 kernel (release asset SHA-256 `17ee5547…5adf`, equal to
  GitHub's digest); Mathlib `f897ebcf` definitions (Real, Filter, Finset, PMF, Measure.pi);
  the 49-line model file; the definitions in `TrialSpec`/`Criterion` for the general theorem.
  The Mathlib build came from the official cache (7,335 files).
- **Comparator**: built at `90100840` with a one-line Lean 4.24 compatibility patch,
  `logs/comparator-4.24-compat.patch` (`.regular n.toUInt32`). It uses lean4export
  `8c79d2ea`, whose only change is its toolchain file (`logs/lean4export-4.24-toolchain.patch`).
  The comparison has these limits:
  - macOS has no landrun. `env/bin/landrun` is an unsandboxed shim, and every log says
    `THIS IS NOT REAL LANDRUN`.
  - The solution modules were new, but they import `KSatUpper` oleans that were built
    beforehand.
  - The in-process replay printed 17 `PANIC … duplicate normalized declaration name` lines
    for clashing private core/Mathlib names (e.g. `List.merge.eq_def`). In Lean 4.24,
    `addDeclCore` kernel-checks a declaration before that bookkeeping step, and the panic
    leaves the map unchanged. lean4checker, which replays into `Kernel.Environment` directly,
    gives an independent replay.

  So this is statement, axiom and kernel checking, not adversarially hardened verification.
- No external kernel such as nanoda was used. No human has reviewed this formal development.

## Proven vs not proven

Proven, kernel-checked:
- the general-arity criterion theorem: PROOF.md §§2–7 for every `k = m+1 ≥ 1`;
- the k=4 and k=5 endpoints (9.96, 9.934; 21.14, 21.123) and the k=3 regression endpoint
  (4.268), whose monolithic certificates need about 12 GB per kernel check;
- the k=3 endpoints at 4.2672 and 4.26718, whose chunked certificates, Comparator check and full
  fresh replay each fit in 4 GiB per process;
- the certificates and controls listed above.

Not formalized or not claimed:
- **Exponential rate.** PROOF.md (Q) gives the rate `exp(-2c²n/α)` via Hoeffding. The Lean
  proof uses Chebyshev with linear variance and shows only that the probability tends to zero.
- **Constants.** `c0`, `N0` and `y = 20` of (B)/(P) are not formalized. The limit argument
  chooses `y`.
- **Repeated-to-distinct transfer.** PROOF.md (O) uses a resampling coupling; the Lean proof
  uses the counting ratio `exp(k²α)` instead. Both are valid, but only the latter is
  formalized.
- **Out of scope.** Optimality, thresholds, and the cavity values 9.931 and 21.117.
- **Separate questions.** The novelty and significance of the constants are not settled by
  this work, and comparing 4.26718 with Vorobyev's Lean-checked 4.268 is the parent's job. The
  principle is prior art (Franz–Leone; Lelarge–Oulamara; Vorobyev for k=3). The formal proof
  establishes correctness only.

## Reproduce

```sh
F=$PWD   # this formal/ directory
export PATH=$F/env/toolchains/lean-4.24.0-darwin_aarch64/bin:$PATH LEAN_NUM_THREADS=4 \
       MATHLIB_CACHE_DIR=$F/env/mathlib-cache
cd lean && lake build && lake env lean ../audit/Audit.lean && cd ..
python3 tools/scan_sources.py lean/KSatUpper
python3 tools/make_challenge.py --check
FORMAL=$F python3 tools/run_comparator.py endpoints-k3 general control-EndpointsWrongDensityK3a \
  control-EndpointsWrongDensityK3b       # the default list includes ~12 GB monolithic replays
FORMAL=$F python3 tools/run_controls.py CertK3TblLowDensity CertK3TblTooStrong CertK3TblShortEdge \
  CertK3TblTamper WrongArity WrongDensity BadTrialWeights
tools/run_k3_chunked.sh $F data && tools/run_k3_chunked.sh $F checks 6 600   # each process ≤ 4 GiB
tools/run_lean4checker.sh $F --fresh KSatUpper.ThresholdK3
```

The environment rebuild is described in `handoff/README.md`. Heavy local directories are
git-ignored and are not deliverables: `env/` holds the toolchain, packages, Mathlib cache,
comparator, lean4export and lean4checker, and `lean/.lake` holds build outputs.
`upstream/sat-upper-4268` is the pinned read-only clone. `archive/` holds unused scaffolding,
which was moved rather than deleted.
