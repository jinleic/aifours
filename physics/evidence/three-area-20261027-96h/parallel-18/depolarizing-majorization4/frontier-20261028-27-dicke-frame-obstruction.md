# Exact counterexample to a proposed Pauli-frame shortcut

**Result:** the auxiliary premise \(\lambda_2(F(\rho))\le2\) is **false even for an actual pure genuinely four-partite-entangled input**, where
\[
F(\rho)=\sum_{i=1}^4\sum_{a\in\{x,y,z\}}
 \sigma_i^a\rho\sigma_i^a.
\]
This is **not** a counterexample to the original depolarizing majorization conjecture, and it does not refute the still-unproved possible bound \(\|F(\rho)\|_{(3)}\le8\). It eliminates a proposed shortcut: one cannot prove that rank-three bound by assuming the second and third frame eigenvalues are separately at most2. No novelty claim or independent-family review is made.

## Exact physical witness and analytic spectrum

Let
\[
|D^4_2\rangle=\frac1{\sqrt6}\sum_{|x|=2}|x\rangle,
\qquad \rho=|D^4_2\rangle\langle D^4_2|.
\]
All four one-qubit marginals are \(I/2\). Across any two-versus-two partition, permutation symmetry reduces the Schmidt expression to
\[
|D^4_2\rangle=
\frac1{\sqrt6}|00\rangle|11\rangle+
\frac2{\sqrt6}|\Psi^+\rangle|\Psi^+\rangle+
\frac1{\sqrt6}|11\rangle|00\rangle,
\quad |\Psi^+\rangle=(|01\rangle+|10\rangle)/\sqrt2.
\]
There are three nonzero Schmidt coefficients. Together with the one-qubit cuts, this is an actual genuinely multipartite-entangled pure state, not a relaxed block or nonphysical density.

Compute \(F(\rho)\) by Hamming-weight subspaces in the computational basis:

- On weights 0 and 4 it vanishes.
- On each of the weight-1 and weight-3 four-dimensional subspaces, the diagonal entries are 1 and all off-diagonal entries are \(2/3\). The eigenvalues are \(3\) once and \(1/3\) three times in each block.
- On the weight-2 six-dimensional subspace, the diagonal is \(2/3\); the entry between complementary two-subsets is \(-2/3\); all other off-diagonal entries vanish. The three complementary 2×2 blocks therefore give \(4/3\) three times and 0 three times.

Thus the full exact spectrum is
\[
3^{(2)},\quad (4/3)^{(3)},\quad (1/3)^{(6)},\quad 0^{(5)},
\]
so \(\lambda_2=3>2\) and the top-three sum is \(22/3<8\). An actual rank-three maximizer for this auxiliary frame is the span of the normalized symmetric weight-1 state, the normalized symmetric weight-3 state, and \((|0011\rangle-|1100\rangle)/\sqrt2\). This witnesses the stated frame spectrum but is not an original-channel violation.

## Original-channel physicality and eigenvalue check

The same exact input was applied to the **original** four-qubit channel independently both by sequential local partial-trace maps and by its full Pauli Kraus mixture. At each of the two physical parameters \(p=2/3,4/3\), exact rational rank calculations give the full original-output spectrum
\[
(1/9)^{(1)},\ (7/81)^{(2)},\ (16/243)^{(3)},\
(13/243)^{(6)},\ (4/81)^{(4)}.
\]
Its top-three sum is \(23/81\), while the actual pure-product reference top-three sum is \(32/81\); the gap is \(1/9>0\). The actual common rank-three projector onto the symmetric weight-1, weight-2 and weight-3 states has exact trace \(23/81\) at **both** parameters. The checker verifies this projector is Hermitian, idempotent and trace3, and verifies the input is Hermitian, idempotent and trace1. No violation of the original channel is asserted.

## Executed evidence and limits

The numerical premise scout `frontier-20261028-25-pauli-spectrum-scout.py` SHA256 `b889c73ed7bbe96724963788cb9e1b51e4537633729843a4fd18dac2a06a1d30` ran 120 random starts, seed2026102825, ≤100 gradient steps; it returned a second eigenvalue `2.9999781593063792` with eigensolver residual `9.666379811717375e-16`. This led to the exact witness, and is not itself an exact certificate.

The exact check `frontier-20261028-26-dicke-pauli-counterexample.py` SHA256 `aefeea6ddc56b72a16a90e795232b1837830284f5e4d597088e6f2914d2e1925` imports `frontier-20261028-18-anisotropic-w-check.py` SHA256 `29935ef6e2d288686a4cfcf7c3e1e6483895e00e124f2bce2a2683ea909f4a0a`, which in turn imports the already pinned `frontier-20261028-12-bloch-gap-check.py` and `frontier-20261028-09-exact-one-uniform-check.py`. Ran `python3 -B physics/evidence/three-area-20261027-96h/parallel-18/depolarizing-majorization4/frontier-20261028-26-dicke-pauli-counterexample.py` from repo root; exit0, integer/Fraction complex-pair arithmetic only. It directly constructs all 12 local-Pauli conjugations, independently checks \(F=4\sum_iE_i(\rho)-4\rho\), checks the auxiliary spectrum by exact matrix ranks, recomputes both original channels from all Pauli Kraus terms, checks every original-output spectral multiplicity via exact ranks and verifies both actual rank-three projectors. Native metadata clock after this final run **Wed Oct 28 17:34:31 PDT 2026**.

This exact finite counterexample rules out only the named second-eigenvalue premise. The actual common-projector first/second erasure inequalities and the original full all-variable k3 problem remain unproved.
