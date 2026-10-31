# Exact finite checks of the one-uniform k3 candidate

Author candidate `frontier-20261028-08-one-uniform-proof.md` SHA256 `980d9f111f3fb685dfec9449b8bfcb325f3761a19ec91bea0615401d7d46cb38`. Exact checker `frontier-20261028-09-exact-one-uniform-check.py` SHA256 `ca5c9fc326c1a17a4035b758757a74b8b5222081015eaa9da9928b0646b357da`. Actual native metadata clock **Wed Oct 28 17:11:35 PDT 2026**. Ran `python3 physics/evidence/three-area-20261027-96h/parallel-18/depolarizing-majorization4/frontier-20261028-09-exact-one-uniform-check.py` from the repository root, exit0; uses Python integers and `fractions.Fraction`, no floats.

The checker explicitly multiplies the four exact one-qubit Pauli matrices to check the spin-flip sign identity. It checks the coefficient identity for each of 256 four-site Pauli-label strings using the exact scalar count determined by Pauli weight; it does **not** independently construct 256 full tensor matrices. Separately it constructs exact 16×16 complex-rational matrices for a GHZ density and a genuinely complex rank-three projector and checks the full spin-flip/layer matrix identity for each. Exact matrix multiplication verifies that the state and projector are Hermitian idempotents with traces 1 and 3, respectively; each one-qubit state marginal is exactly \(I/2\).

The pair is \(\rho=|\mathrm{GHZ}\rangle\langle\mathrm{GHZ}|\), \(|\mathrm{GHZ}\rangle=(|0000\rangle+|1111\rangle)/\sqrt2\), and projector range \(|0000\rangle,|1111\rangle,(|0011\rangle+i|1100\rangle)/\sqrt2\). Its exact same-pair layer traces are `(1, 2, 7/4, 3/4, 3/16)`. At four rational physical noise parameters, sequential original channel application was compared entry-for-entry with its erasure expansion and the exact GHZ output matrix pattern. Its block and diagonal eigenvalues were compared exactly, yielding:

|p|same-P output trace|actual GHZ output top3|actual product-reference top3|exact spectral gap|candidate bound's required gap|
|---|---:|---:|---:|---:|---:|
|0|1|1|1|0|0|
|1/2|91/256|97/256|135/256|19/128|1/16|
|1|3/16|3/16|3/16|0|0|
|4/3|7/27|22/81|32/81|10/81|2/27|

The original channel at these parameters has nonnegative Pauli Kraus weights; the trace and eigenvalue values are exact. This verifies the named finite identities and pair only, not every state, projector or parameter. The all-variable proposition remains an author-written candidate pending independent written review; the experiment is not a formal proof, configured-family review, novelty assessment, or original global k3 resolution. The original open complement and all historical qualifications remain as stated in the candidate.
