# Four-qubit invariant sector and two-excitation Dicke all-prefix orbit

**Disposition: same-harness written support plus independently authored finite corroboration, parent-run once.** Two distinct scopes are adopted below. Neither is an unrestricted four-qubit or general-blocklength theorem. Song–Chen’s earlier weighted compatible three-qubit proposition is not used as a four-qubit theorem; novelty is not certified.

For the physical channel \(\Phi_p(X)=(1-p)X+(p/2)\operatorname{Tr}(X)I_2\), \(0\le p\le4/3\), put \(t=|1-p|\), \(a=(1+t)/2\), \(b=(1-t)/2\), and \(D_t=\operatorname{diag}(a,b)^{\otimes4}\). For an ACTUAL four-qubit density, \(H_j=\sum_{|S|=j}\rho_S\otimes I_{S^c}\), on its physical tensor positions. The decreasing product-reference layer spectra are \(L_3=(4,1^{\times4},0^{\times11})\), \(L_2=(6,3^{\times4},1^{\times6},0^{\times5})\), and \(L_1=(4,3^{\times4},2^{\times6},1^{\times4},0)\); they are co-ordered. For the nonnegative-retention branch, \(T_t^{\otimes4}(\rho)=t^4\rho+t^3bH_3+t^2b^2H_2+tb^3H_1+b^4I\). No extra binomial factors occur outside the actual subset sums.

## 1. Every mixed spin-flip-invariant four-qubit density

Suppose \(\widetilde\rho=Y^{\otimes4}\rho^TY^{\otimes4}=\rho\). Then the SAME density satisfies
\[
H_1=2I,\qquad H_2=I+H_3,\qquad0\le H_3\le2I,\quad\operatorname{Tr}H_3=8.
\]
Every invariant three-qubit marginal commutes with its spin-flip antiunitary of square \(-I\); orthogonal eigenvalue pairing bounds that marginal by \(I/2\). This proves the last operator inequality, including for mixed inputs. It is not an independent-marginal maximization.

**All sixteen \(H_2\) prefixes:** \(H_2\prec L_2\). **Actual physical channel:** every complex rank-\(k\) orthogonal-projector prefix against \(D_t\) holds for every physical \(p\) whenever \(k\ne4\). The fourth prefix, hence full output majorization, also holds for
\[
0\le t\le t_*=(\sqrt{29}-2)/5\quad\text{or }t=1,
\qquad\text{equivalently}\qquad p\in[(7-\sqrt{29})/5,4/3]\cup\{0\}.
\]
Indeed one common projector gives \(h_3\le\min(2k,8)\), \(h_2=k+h_3\), \(h_1=2k\) and \(\operatorname{Tr}(Q\rho)\le1\). In the complete sixteen-row reference-deficit table only the \(H_3\) coefficient at \(k=4\) is negative. Its total lower bound is exactly \(tb(5-4t-5t^2)/4\). A negative value of THIS RELAXATION outside the stated region is **not** a physical counterexample or a failure of actual majorization.

## 2. Full all-physical-parameter theorem for the Dicke2 orbit and mixtures

Let \(|D\rangle=6^{-1/2}\sum_{|x|=2}|x\rangle\). Every physical local-unitary conjugate of \(|D\rangle\langle D|\), and every finite convex mixture of such conjugates, obeys \(\Phi_p^{\otimes4}(\rho)\prec D_t\) for **every** physical \(p\in[0,4/3]\) and all sixteen prefixes.

The actual \(\rho_D,H_3,H_2,H_1\) share five decreasing subspaces of multiplicities \(1,2,3,6,4\), with respective eigenvalue tuples
\[
(1,2,3,2),\quad(0,3/2,5/2,2),\quad(0,2/3,5/3,2),\quad(0,1/6,7/6,2),\quad(0,0,1,2).
\]
They follow from actual physical marginal matrices and weight-block adjacency \(J_4-I_4\) or \(J_6-I_6-M\), not separately chosen marginal spectra. Their exact output-prefix gap is \(t^3b\Delta_3(k)+t^2b^2\Delta_2(k)+tb^3\Delta_1(k)\); every coefficient is nonnegative, and \(\Delta_2(k)>0\) at each proper prefix. Thus all proper prefixes are strict when \(0<t<1\). At \(t=0\) both outputs are maximally mixed; at \(t=1\) both have pure spectra. Output co-ordering is proved, not assumed across potential eigenvalue crossings.

For the physical negative branch the map is a **full** transpose conjugation, and the same consuming projector is transported to \(Q'=Y^{\otimes4}Q^TY^{\otimes4}\), with rank and orthogonality preserved. Local covariance transports it again by the actual local unitary; linearity for this fixed projector proves the finite-mixture theorem. No partial-transpose or independently selected consuming projector is substituted.

The pure Dicke state has Schmidt rank2 on every singleton cut and3 on every paired cut. Hence it is genuinely four-partite entangled and lies outside the combined earlier finite convex hull of the named Class A/B, symmetric-W4 orbit and biseparable sets: a positive mixture equal to a pure density must have every component supported on that same ray. This is a **strict extension relative to those named classes**, not a survey-wide novelty claim. Arbitrary invariant densities and arbitrary Dicke-orbit mixtures are NOT all claimed genuinely entangled.

## Evidence and scope ceiling

[Complete original f481 author](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f481-four-qubit-compatible-two-body-layer-or-coaligned-marginal-frontier/review-v1.md) · [f510 invariant-sector review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f510-four-qubit-spinflip-invariant-common-projector-sector-review/review-v1.md) · [f511 Dicke/orbit/hull review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f511-four-qubit-two-excitation-dicke-all-prefix-orbit-review/review-v1.md) · [f512 independent report/source](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f512-four-qubit-dicke-and-spinflip-sector-independent-finite-check/review-v1.md) · [materialized independent source](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f512-four-qubit-dicke-and-spinflip-sector-independent-finite-check/independent-four-qubit-dicke-spinflip-finite-v1.py) · [parent actual one-shot receipt](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f512-four-qubit-dicke-and-spinflip-sector-independent-finite-check/parent-independent-finite-run-v1-receipt.json). Parent full displayed coverage:523 author,353/566 written and1002 finite-report/source logical lines. Both written scopes have0F/0M/0m; parent reconstructed all physical blocks, complete prefix tables, invariant-sector exceptional prefix, actual complex-projector transport and pure-state hull separation.

After full static source review and parent GO, the independently authored stdlib checker was parent-run ONCE: exit0, empty stderr,0.851s. Actual observed:22 exact characteristic-polynomial comparisons;64 exact Dicke output-prefix comparisons; five actual invariant densities times four physical parameters,20 cases/320 **NUMERICAL** output-prefix comparisons; exact physical Pauli-versus-erasure equality and complex-projector transport; eleven intended-reason mutations. The general selected spectra use realified Jacobi arithmetic with prefix tolerance2e−9/residual tolerance1e−10; observed maximum eigenpair residual3.044e−15 and pair gap3.331e−16. These numerical cases are not exact spectral certificates. Exact marginal/layer/polynomial/selected-Dicke/transport checks use Gaussian-rational arithmetic. No finite sample replaces either written universal scoped theorem.

The original f481 local-only pre-body ACK qualification remains in the [transport disclosure](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/parent-f479-f481-f483-local-prebody-ack-transport-disclosure-v1.json); it is not backdated as direct delivery or treated as automatic mathematical invalidity. F508/f513 and all earlier genuinely held episodes AND consumers remain NONINPUT. The separate coherent-vacuum-W4 candidate is not adopted by this record. Unrestricted four-qubit \(H_2/H_3\), arbitrary-noise fourth prefix for the whole invariant sector, unrestricted channel theorem, general blocklength, original printed-source equivalence, independent-family/human/kernel assurance and novelty remain unpaid.
