# Exact checks of the PSD-Hessian k3 successor

The unreviewed conditional candidate `frontier-20261028-81-psd-hessian-uniform-noise.md`, SHA256 `49019845e5ca92b1a90f8c0199c0fcc2ba37301b720117839c42b13469422760`, proposes original k3 for every four-qubit density and actual complex rank-three P when \(|1-p|\le8\cdot10^{-5}\), contingent on the entire pending Hessian/block predecessor. This evidence does not prove that universal theorem, a full all-p result, novelty or formal/independent-family acceptance.

## Exact weight-two and scalar checks

`frontier-20261028-80-psd-hessian-check.py`, SHA256 `11776cf1b28f6e13661a1f5532477e6ca15086a53bed5ab18065de013ed3d1cd`, ran `python3 -B ...` from repo root, exit0. It verifies the exact weight-two decomposition
\[
M_2=ab\,t(1+t)\bigl[-(1-t)I+K\bigr],\qquad
K=t\Gamma+(1-2t)\operatorname{diag}(n),\quad \operatorname{Tr}K=2(1-t)
\]
for 60 complex rational directions at `t=1/1000,1/10,1/2`; five mixed-weight rational cases check the new \(15t/64\) scalar margin at `t=1/1000`. The universal PSD implication is written in the candidate and is not inferred from these finite cases. Exact scalar checks give `Q_offblock_upper=250781/31250 < 81/10`, first remainder coefficient `21188067/15625000 < 7/5`, second coefficient `12642/625 < 203/10`, epsilon `3/100` and proposed shrinkage `1/12500`; all constant comparisons returned true. The checker imports the previously pinned exact Hessian helpers.

## Original channel at both exact proposed endpoints

`frontier-20261028-82-psd-endpoint-check.py`, SHA256 `2ff37e6ea3f11d8e5c7046a473f2cc07926f1bb39afe77e46ace1e2326d231a0`, ran with single-threaded BLAS and `python3 -B`, exit0. Its actual pure input is
\[
 (1500|0000\rangle+|0011\rangle+2i|0111\rangle+2|1111\rangle)/\sqrt{2250009}.
\]
At both exact physical parameters `12499/12500` and `12501/12500`, the complete original Pauli Kraus and sequential channel matrices agree entrywise in Gaussian-rational arithmetic. Sixteen positive LDL pivots certify each output positive, another 16 certify the stated rational upper bound on its largest eigenvalue, and exact inertia `(15 positive,1 negative,0 zero)` certifies the rational upper bound on its second/third eigenvalues. Thus at each endpoint the actual output top3 is strictly below
\[
 \frac{3750800043201}{20000000000000},
\]
while the actual product reference top3 is
\[
 \frac{73257813437499999}{390625000000000000}.
\]
Their exact positive difference is
\[
 \frac{374921871}{1562500000000000000}.
\]
The checker also constructs one actual rank-three projector and its deterministic spin-flipped transpose, verifies their exact projection identities and records the same-P trace `164830739343750935299999/878909765625000000000000`. Decimal eigenvalues in the console are observations only; LDL/inertia is the certificate.

Native hashes/clock **Wed Oct 28 19:05:05 PDT 2026**. The two endpoint checks cover only this one input. Full disjoint written review of the h2 PSD inequality, h3/h4 predecessors, global product gauge, both unitary remainder bounds, far-case threshold and mixed/signed-noise transport remains essential before the all-density interval can be accepted.
