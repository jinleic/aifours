# Bounded original-channel k3 seesaw — actual run

Scientific script: `frontier-20261028-02-physical-seesaw.py`, SHA256 `73d4befebd61820df000ef49c3f768844828e7cb137cb4caa5a0510337ec7587`. Independently written exact parameter-mirror proposition: `frontier-20261028-01-spectral-mirror.md`, SHA256 `4fb86d219a99daf54cbe7ab6c37a6a7fbd11c40009879d63ae135c5195cb4b1c`. Native observation after the run and pins: **Wed Oct 28 17:03:11 PDT 2026**. Run: `env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 physics/evidence/three-area-20261027-96h/parallel-18/depolarizing-majorization4/frontier-20261028-02-physical-seesaw.py` from the repository root, exit 0. Runtime: installed NumPy; no SciPy. Seed 20261028, 12 complex pure-state starts per parameter, at most 80 actual alternating steps per start. The seven parameters are exact rationals in the source and binary floating approximations in the run.

The algorithm alternates (i) the actual three-dimensional top eigenspace of the original channel output of an actual pure input and (ii) the top eigenvector of the self-adjoint original channel acting on that **same** rank-three projector. The final result is recomputed from the physical original fourfold Pauli Kraus mixture, its output eigenvalues, and the actual product-reference output eigenvalues; the final same-pair projector trace is also checked. The sample and stopping rules do not certify the global optimum.

|p|largest final numerical k3 output minus product-reference k3 across the 12 starts|smallest among the 12|best-start steps|
|---|---:|---:|---:|
|1/6|-6.827871601444713e-14|-1.468825061579082e-13|54|
|1/3|-1.0325074129013956e-14|-2.864375403532904e-14|27|
|1/2|-2.220446049250313e-16|-5.218048215738236e-15|15|
|2/3|3.3306690738754696e-16|-5.551115123125783e-16|9|
|3/4|3.3306690738754696e-16|-4.440892098500626e-16|8|
|5/4|4.440892098500626e-16|-3.885780586188048e-16|8|
|4/3|4.996003610813204e-16|-1.1657341758564144e-15|10|

The largest returned numerical candidate was at p=4/3. Independent original Pauli-mixture recomputation gave output top3 `0.3950617283950623`, reference top3 `0.3950617283950617`, gap `6.106226635438361e-16`; the same actual projector trace gave the same reported gap. This is at roundoff scale and is **not** a strict physical violation or an exact/rational witness. The script's thresholded `candidate_over_1e-9` was `false`.

**Physicality and implementation checks, numerical only:** the chosen input's trace was `1.0000000000000013` and smallest computed eigenvalue `-4.805740093406808e-17`; the independently constructed physical-channel output's smallest eigenvalue was `0.012345679012345687`. Its projector had trace `2.9999999999999996`, idempotence maximum-entry residual `1.1102230246251565e-16`, and Hermiticity residual `0.0`. The direct projector trace imaginary part had magnitude `4.4181238528784306e-18`. The negative input eigenvalue is numerical roundoff, not an exact PSD certificate.

On the run's validation instances, maximum entry disagreement between independent partial-trace and Pauli-mixture channel constructions was `9.159339953157541e-16`; maximum reference-formula error was `5.551115123125783e-17`. For 40 random density/projector mirror checks at five physical mirror parameters, maximum spectral discrepancy was `1.942890293094024e-16`, maximum paired-projector trace discrepancy `5.552639573108236e-17`, and maximum mirrored-projector idempotence discrepancy `3.3306690738754696e-16`. These support implementation consistency only; the written mirror proof, not these samples, supplies its stated universal claim.

No earlier held result is used as a validated mathematical premise. No global k3 proof, rigorously certified violation, formal proof, independent-family review, novelty clearance, or extension to unsampled parameters is claimed. The remaining problem is the all-variable actual-density/actual-complex-rank-three-projector inequality on the reduced physical domain `0<=p<=1`.
