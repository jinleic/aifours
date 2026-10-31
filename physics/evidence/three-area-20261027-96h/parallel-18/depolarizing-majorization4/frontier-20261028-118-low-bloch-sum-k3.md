# An unequal-marginal all-noise k3 region from the physical spin-flip dual

**HIGH-CONSEQUENCE WRITTEN AUTHOR CANDIDATE — NOT ADOPTED.** For any pure four-qubit state with actual local Bloch radii `r_i`, `S=sum_i r_i^2`, and full-spin-flip overlap `C=|<psi|Y^tensor4 conjugate(psi)>|^2`, the following pair of inequalities is a sufficient condition for the original k3 comparison at **every** physical noise and every actual complex rank-three test projector:

\[
\sum_i r_i\le2,\qquad 4S+8C\le64/9.\tag{1}
\]

The same bound holds for the actual convex hull of such pure inputs. This physical-input region allows unequal radii and includes GME states outside the earlier equal-radius candidate `frontier-20261028-114-equal-marginal-k3.md`. It does not prove global k3, cover every state with small Bloch sum, establish novelty, or transfer an earlier gate. The written proof needs disjoint review; no formal/human/stronger-family acceptance or process-history cure is claimed.

## 1. The spin-flip dual without equal-marginal assumptions

Let `rho=|psi><psi|`, `tilde rho=Y^tensor4 rho^T Y^tensor4`, and

\[
H_1(\rho)=\sum_i I_{\bar i}\otimes\rho_i,\qquad
M(\rho)=H_1(\rho)-\rho.
\]

Each local Schmidt rank is at most two, hence `I_bar_i tensor rho_i>=rho/2`. Summing over the four sites gives `H1(rho)>=2rho` and `M(rho)>=0`. The same facts hold for `tilde rho`, which is pure and has the SAME local radii.

The smallest eigenvalue of `H1(tilde rho)` is the sum of the four local minority eigenvalues,

\[
\lambda_{\min}H_1(\widetilde\rho)
=\sum_i(1-r_i)/2=(4-\sum_i r_i)/2\ge1.
\]

Thus `H1(tilde rho)-I` is PSD. Subtracting the rank-one projector `tilde rho` can create at most one negative eigenvalue, so the second smallest eigenvalue of `M(tilde rho)` is at least one, while its smallest is nonnegative. The exact full-spin-flip identity

\[
H_1(\rho)+\widetilde\rho=4I-M(\widetilde\rho)
\]

therefore gives

\[
\lambda_1(H_1+\widetilde\rho)\le4,
\quad \lambda_2(H_1+\widetilde\rho)\le3,
\quad K_3(H_1+\widetilde\rho)\le10.\tag{2}
\]

This is the actual second-target trace bound from 106 for these **input states**, not a proof of the corresponding operator inequality for every Q.

## 2. Same-input frame moment and original channel

For the same pure rho, the explicit Pauli-sector calculation reconstructed in 114 §3 gives

\[
\operatorname{Tr}F(\rho)=12,\qquad
\operatorname{Tr}F(\rho)^2=16+4S+8C,
\quad F(\rho)=\sum_{i,a}\sigma_i^a\rho\sigma_i^a.
\]

Let `x=K3(F)`. Because rho is pure, F is the sum of twelve rank-one Pauli-error projectors and has rank at most 12. Cauchy–Schwarz on the largest three and at most nine remaining nonzero eigenvalues yields `Tr F^2>=x^2/3+(12-x)^2/9`. The right side is strictly increasing for `x>=8`. At x=8 it is `208/9`, so the second condition in (1) gives `Tr F^2<=208/9` and hence `K3(F)<=8`.

For any **same actual rank-three Q**, use `Tr Qrho<=1`, (2), and `Tr QF<=8`. With the normalized-erasure layers `T_m=sum_|A|=m E_A(rho)`, the full spin flip and Pauli twirl give

\[
T_1=\rho+F/4,\qquad
4T_2=H_1+\rho+\widetilde\rho+F/2-I.
\]

Consequently `Tr QT1<=3` and `4 Tr QT2<=10+1+4-3=12`. The remaining layers obey `Tr Qrho<=1`, `Tr QT3<=5/4`, and `Tr QT4=3/16`. Multiply these SAME-Q bounds by the nonnegative erasure coefficients for `0<=p<=1` to obtain the actual pure-product reference top3. The full-transpose global spin-flip map supplies `1<=p<=4/3`; the SAME Q is fixed during affine averaging over any finite pure decomposition from the specified class. This is a complete written implication of (1), not a claim that either inequality automatically holds for every physical state.

## 3. An exact GME input outside the previous equal-radius and named families

Consider

\[
|\psi\rangle=(|0001\rangle+2|0010\rangle+2|1100\rangle)/3.
\]

Its exact local radii are `(1,1,1,7)/9`, so they are unequal and sum to `10/9<2`. It has `S=52/81`, `C=0`, and `4S=208/81<64/9`; hence it lies in (1), outside the input scope of 114. Its seven exact Schmidt-cut ranks are `2,2,2,2,2,3,3`, so it is GME.

All four local marginals are nondegenerate in Z, while the support mixes odd and even parity, excluding any local-unitary product-Pauli parity eigenstate and the paired-parity subfamily by the argument in 116. Its `(1,3)|(2,4)` cut has Schmidt rank three, excluding all LU images and pure convex-hull members of vacuum-plus-single-excitation states. A symmetric state up to local unitaries has all local radii equal, so this one is not in that named family. Across `(1,2)|(3,4)`, its largest squared Schmidt coefficient is `5/9`, which upper-bounds maximal product overlap and excludes the cited `G>=124/125` near-product region. Other older F2/covariance/regional criteria are not checked; no global novelty or exhaustive prior-region exclusion is claimed.

## 4. Executed exact checks

`frontier-20261028-117-unequal-marginal-check.py`, SHA256 `3ed501c65aa7b2110f0153ab216011c8e11d7890587ffc5b7d38a0a9da9e2ad7`, ran with `python3 -B` and single-threaded BLAS, exit0. Exact Fraction/Gaussian-rational arithmetic checks purity, all four local marginals and radii, `S=52/81`, `C=0`, the seven stated cut ranks, the pair-12 and pair-13 purities `41/81` and `11/27`, and `Tr F^2=1504/81<880/39`. It also confirms the pair-12 largest eigenvalue `5/9` and the exact original sequential/Pauli channel equality at `p=2/3,4/3`. Exact LDL gives `lambda1<3/25`, exact inertia `(15,1,0)` gives `lambda2<19/200`, hence the true original top3 is `<31/100<32/81`, with certified gap `689/8100`. One actual rank-three test and its reflected partner have exact trace `172/729`. The example and two noise checks are finite evidence, not a proof of (1). Native checker-pin clock `Wed Oct 28 21:21:22 PDT 2026`.

A full disjoint review must reconstruct the local-Schmidt operator bound, the **one-rank** inertia argument, spin-flip covariance, the 114 Pauli-moment derivation, every same-Q layer/reference coefficient and the mixed-state and reflected-noise applications. The missing global k3 proof and the operator targets beyond (1) remain open.
