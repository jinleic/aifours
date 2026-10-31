# Exact finite checks of the Bloch-radius k3 candidate

Candidate `frontier-20261028-11-bloch-gap.md` SHA256 `dfebdc80d1d72523f26c3603ba04dbd14ac17cfe38d6f1b5288db67e72212245`; checker `frontier-20261028-12-bloch-gap-check.py` SHA256 `72c3efd28cda8e50e01021f9446e8eb6fb29102973de4b28b9ae56ef89718a87`. Checker imports the exact integer/Fraction matrix helpers in `frontier-20261028-09-exact-one-uniform-check.py`, SHA256 `ca5c9fc326c1a17a4035b758757a74b8b5222081015eaa9da9928b0646b357da`. Native observation after run/pins: **Wed Oct 28 17:13:41 PDT 2026**. Ran `python3 physics/evidence/three-area-20261027-96h/parallel-18/depolarizing-majorization4/frontier-20261028-12-bloch-gap-check.py` from the repo root, exit0, with exact rational pairs and no floating point.

The checker independently constructs exact matrices for four pure states (product, W, unequal GHZ amplitudes 3/5 and 4/5, equal GHZ), verifies their purity/trace, evaluates their diagonal one-qubit marginals and the actual complex rank-three projector from `frontier-20261028-10-one-uniform-check-report.md`. It checks 20 pairs of named state and physical rational parameter `0,1/2,2/3,1,4/3`, including each printed layer upper bound and the candidate trace inequality. For the unequal-GHZ state at `p=2/3` and `4/3`, it also independently constructs the entire fourfold original Pauli Kraus mixture with exact rational weights and checks all matrix entries against sequential application of the original channel.

|state|p|sum of local radii R|same-physical-P trace|product-reference top3|reference minus that trace|candidate lower bound|
|---|---:|---:|---:|---:|---:|---:|
|unequal GHZ 3/5,4/5|2/3|28/25|7/27|32/81|11/81|38/2025|
|unequal GHZ 3/5,4/5|4/3|28/25|7/27|32/81|11/81|38/2025|
|equal GHZ|2/3|0|7/27|32/81|11/81|2/27|
|W|2/3|2|5/27|32/81|17/81|-2/81|
|product|2/3|4|7/27|32/81|11/81|-10/81|

These are exact traces for one stated rank-three projector, not the exact output top3 for those examples. No putative physical violation was found or claimed. A negative lower bound, as for the W and product examples here, is an inconclusive certificate, not a counterexample. The 20 checks cannot establish the universal pure-state inequality or global majorization. The written candidate requires independent review; it makes no novelty, formal-proof, independent-family, or global-k3 claim.
