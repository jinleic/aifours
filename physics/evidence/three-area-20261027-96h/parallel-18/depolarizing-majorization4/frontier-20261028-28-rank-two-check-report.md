# Exact finite checks of the rank-two overlap bound

Candidate `frontier-20261028-23-rank-two-overlap-gap.md` SHA256 `4917d95af26860125badcd88ab1eed087bf1bd6e32c535cef6a7f731f1dfea4e`; exact checker `frontier-20261028-24-rank-two-gap-check.py` SHA256 `08d8d60534b4fc8323bcfedbbc01c0ede468da79ff215883648aa6922f198d2d`. The checker uses the pinned exact matrix helpers `frontier-20261028-12-bloch-gap-check.py` SHA256 `72c3efd28cda8e50e01021f9446e8eb6fb29102973de4b28b9ae56ef89718a87` and `frontier-20261028-09-exact-one-uniform-check.py` SHA256 `ca5c9fc326c1a17a4035b758757a74b8b5222081015eaa9da9928b0646b357da`. Native hash clock: **Wed Oct 28 17:41:44 PDT 2026**. Before the intervening f49 review, the command `python3 -B physics/evidence/three-area-20261027-96h/parallel-18/depolarizing-majorization4/frontier-20261028-24-rank-two-gap-check.py` ran from the repo root and exited0.

Exact Fraction complex-pair arithmetic checked five physical pure states, two complex rank-three projectors and seven rational physical parameters: **70 actual-pair inequalities**. For each state/parameter it checked the full 16×16 polynomial identity \(K^3-AK^2+(A-B)Bd^2K=0\), **35 matrix cases**, and the claimed domination of the predecessor's lower bound; square-root comparisons are done by exact nonnegative rational inequalities, not floats. Two complete Pauli Kraus-mixture matrices were independently compared entry-for-entry to sequential original-channel outputs for a genuinely complex input.

For \((3|0000\rangle+4i|1111\rangle)/5\), \(p=4/5\) or \(6/5\), the exact input invariant \(d=7/25\). The predecessor's lower bound is \(659/15625\); the rank-two bound is
\[
\frac{1385-\sqrt{2977}}{31250}\in
\left(\frac{133}{3125},\frac{1331}{31250}\right),
\]
using \(54^2<2977<55^2\), and is strictly larger than the predecessor. For two different actual complex rank-three projectors the exact original-channel trace gaps are \(56/625\) and \(81/625\), respectively, both above that bound. These are same-P trace checks, not asserted complete spectra for this case and not counterexamples.

The matrix-rank optimization proof and the all-variable inequality still require disjoint written review; the finite cases are not universal proof, formal verification, novelty clearance or a solution of the unrestricted global k3 residual.
