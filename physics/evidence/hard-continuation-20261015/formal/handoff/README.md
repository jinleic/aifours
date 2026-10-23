# Hand-off: Lean formalization for phys-p0422 (k=3 at 4.26718, k=4 at 9.934, k=5 at 21.123, general k)

This bundle holds only new load-bearing sources, checkers, receipts and data; heavy dependencies
must be re-downloaded. The full evidence and trust analysis are in `../README.md`.

## Claims (kernel-checked; only `propext`, `Classical.choice`, `Quot.sound`)

- `KSatUpper.satisfiabilityProbability_3SAT_42672_tendsto_zero`:
  `Tendsto (fun n : ℕ => satisfiabilityProbability 3 n (2667*n/625)) atTop (nhds 0)`.
- `KSatUpper.satisfiabilityProbability_3SAT_426718_tendsto_zero`: the same at `213359*n/50000`,
  that is `⌊4.26718 n⌋`. The law is the six-atom law of
  `physics/evidence/hard-continuation-20261015/k3-extension/certificates/compat-trials.json`
  (SHA-256 `7b0d2615eaf8ba45bbcf47a81caf2985699400592ac4c4fa84bfc156c93ad044`), with `T = 128`
  and edge truncation `N = 256`. The certificates are chunked; every Lean process of the build,
  the Comparator check and the fresh lean4checker replay stayed under 4 GiB (max 3.65 GB).
- `satisfiabilityProbability_4SAT_tendsto_zero` (9.96), `..._4SAT_9934_...` (9.934),
  `..._5SAT_...` (21.14), `..._5SAT_21123_...` (21.123) and the k=3 regression
  `..._3SAT_tendsto_zero` (4.268). Their certificates are monolithic: one kernel check needs
  about 12 GB, which exceeds the lane's 4 GiB target (measured 2026-10-16, not before).
- `KSatUpper.tendsto_zero_of_criterion`: for every arity `m+1`, finite rational trial law and
  density `α ≥ 0`, `Psi < 0` implies the limit 0 at `⌊α n⌋`.
- UNKNOWN: T=512 k=4 at 9.9325 and T=256 k=3 at 4.26685 (evaluations only; kernel runs were
  stopped by the 6 GiB watchdog).

Not proven: the exponential rate (only the limit 0), explicit `c0`/`N0`, the PROOF.md (O)
coupling, thresholds. Novelty and the comparison with Vorobyev's 4.268 are outside this lane.

## Input pins

| item | pin |
|---|---|
| Lean | `leanprover/lean4:v4.24.0`, `lean-4.24.0-darwin_aarch64.tar.zst` SHA-256 `17ee554702c199fc03f37b1c3708245671c93f5d932dcff55a03fa6cdb5e5adf` |
| Mathlib | `f897ebcf72cd16f89ab4577d0c826cd14afaafc7` (tag v4.24.0); other packages as in `lean/lake-manifest.json` |
| upstream (derivation source, Apache-2.0) | `https://github.com/yamelton/sat-upper-4268` commit `87fb64825b24159418aa0cdca830a76a9d85ff84` |
| k=4/k=5 trial data | `institute/runs/hard-2026-10-15/problems/phys-p0422/attack-e2/certificates/trials.json`; `physics/evidence/hard-continuation-20261015/certificates/trials.json` (SHA-256 in `result.json`) |
| k=3 trial data | `physics/evidence/hard-continuation-20261015/k3-extension/certificates/compat-trials.json` (SHA-256 above) |
| Comparator | `https://github.com/leanprover/comparator` `90100840fd3e19d94143dea4fb8b2961e404efa0` + `patches/comparator-4.24-compat.patch` |
| lean4export | `https://github.com/leanprover/lean4export` `8c79d2ea00a0c7397a21d898295f587ffc963496` + `patches/lean4export-4.24-toolchain.patch` |
| lean4checker | `https://github.com/leanprover/lean4checker` tag `v4.24.0` (`da26eb05`) |

## Rebuild and check (macOS arm64)

Run from a directory laid out like `../` (with `env/` holding the toolchain, the Mathlib cache,
comparator, lean4export, lean4checker and the landrun shim `tools/landrun-shim.sh` as
`env/bin/landrun`):

```sh
F=$PWD
export PATH=$F/env/toolchains/lean-4.24.0-darwin_aarch64/bin:$PATH LEAN_NUM_THREADS=2 \
       MATHLIB_CACHE_DIR=$F/env/mathlib-cache
(cd lean && lake exe cache get)
tools/run_k3_chunked.sh $F data && tools/run_k3_chunked.sh $F checks 6 600   # k=3, each ≤ 4 GiB
(cd lean && lake build && lake env lean ../audit/Audit.lean)   # also builds the 12 GB monolithic certificates
python3 tools/scan_sources.py lean/KSatUpper && python3 tools/make_challenge.py --check
FORMAL=$F python3 tools/run_comparator.py endpoints-k3 general control-EndpointsWrongDensityK3a \
  control-EndpointsWrongDensityK3b
FORMAL=$F python3 tools/run_controls.py CertK3TblLowDensity CertK3TblTooStrong CertK3TblShortEdge \
  CertK3TblTamper WrongArity WrongDensity BadTrialWeights
tools/run_lean4checker.sh $F --fresh KSatUpper.ThresholdK3
```

Wrap any of these in `python3 tools/watch_cmd.py 4194304 <log> -- …` to enforce the 4 GiB cap.

## Contents

- `lean/`: the library `KSatUpper/` (223 modules plus root, including `K3Data` and the 156
  generated `K3Check*` modules), the Comparator `KSatChallenge/` and `KSatSolution/`.
- `audit/`, `controls/`, `tools/`, `patches/`, `comparator/` (configs and receipts, logs gzipped),
  `logs/` (audit, scans, memory logs, evaluations, lean4checker logs, upstream baseline).
- `archive/MANIFEST.json` and the k=3 probe results; superseded attempts stay in `../archive/`.
- `result.json` (structured summary with source SHA-256), `SHA256SUMS` (every other file),
  `LICENSE` and `NOTICE.upstream` (upstream Apache-2.0).
