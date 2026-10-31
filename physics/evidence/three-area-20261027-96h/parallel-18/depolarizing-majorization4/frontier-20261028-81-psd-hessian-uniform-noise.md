# A positive-semidefinite weight-two Hessian and a larger k3 noise candidate

**HIGH-CONSEQUENCE CONDITIONAL AUTHOR CANDIDATE — NOT ADOPTED.** The following strengthens the unreviewed uniform-high-noise predecessor `frontier-20261028-59-uniform-high-noise-k3.md` (SHA256 `6f13422e52e6761a3d0d325df821ca78a721ea9c3ad1c8d321043bf93eeb2752`) and the off-block estimates in `frontier-20261028-77-offblock-uniform-noise.md` (SHA256 `04de53eea1187e9a890f263c954c3e05abe7c1e621817bfea24c811ca23eafb2`). Conditional on the complete predecessor reasoning and the new derivation below, it proposes original k3 for **every** four-qubit density and actual complex rank-three P when
\[
 |1-p|\le8\cdot10^{-5}\quad (0\le p\le4/3).\tag{1}
\]
This is not an all-p/all-k solution, a novelty or priority claim, or formal/independent-family/human acceptance. Prior process and quarantine records are not cured or treated as mathematical premises.

## Exact new weight-two inequality

Adopt the predecessor's notation \(t=1-p\ge0\), \(a=(1+t)/2\), \(b=(1-t)/2\), and the product-normal-direction second-order scalar/matrix \(A_2,M_2\). For a normalized weight-two direction \(v=\sum_{i<j}c_{ij}|ij\rangle\), let \(T_{ii}=0,T_{ij}=T_{ji}=c_{ij}\), \(\Gamma=TT^\dagger\), \(n_i=\Gamma_{ii}\). Then \(\Gamma\ge0\), \(\sum_i n_i=2\), and the already written exact Hessian formula rearranges as
\[
\begin{aligned}
 A_2&=-a^2t(1-t^2),\\
 M_2&=ab\,t(1+t)\left[-(1-t)I+t\Gamma+(1-2t)\operatorname{diag}(n)\right].
\end{aligned}\tag{2}
\]
For \(0<t\le1/2\), the matrix \(K=t\Gamma+(1-2t)\operatorname{diag}(n)\) is positive semidefinite and has trace \(2(1-t)\). Therefore its two largest eigenvalues sum to at most its trace, and **\(K_2(M_2)\le0\)**. This is stronger than the predecessor's Frobenius estimate and implies
\[
 A_2+K_2(M_2)\le-a^2t(1-t^2).\tag{3}
\]
It does not claim that all individual eigenvalues of \(M_2\) are nonpositive, nor does it establish global k3 by itself.

For \(0<t\le1/1000\), \(a^2(1-t^2)\ge999999/4000000>15/64\). The predecessor's exact weight-three and weight-four factorizations give still larger positive margins, at least \(45/98\) and \(2047/2048\) times t respectively. Mixed-weight additivity and top-two subadditivity therefore give
\[
 A+K_2(M)\le-\frac{15}{64}t,\tag{4}
\]
so the corresponding rescaled top3 second-order coefficient is at most \(-15/4\).

## Uniform remainder and explicit interval

Use the exact Pauli/off-block bounds proved in the unreviewed 77 predecessor for \(t\le1/1000\): reference gap \(\ge2\), \(\|D\|\le5\), \(\|V\|<23/1000\), \(\|W\|<17\), \(\|S_1\|<3/250\), \(\|Q\|<17\), and \(\|S_2\|<41/10\). For \(|\epsilon|\le3/100\), the exact normalization remainder now obeys
\[
 \|R\|\le\|V\|+|\epsilon|\|W\|<23/1000+51/100<27/50.
\]
The first unitary block conjugation's cubic matrix-remainder coefficient is below
\[
 5(3/125)^3/3+(23/1000)(3/125)^2+2(17)(3/125)+27/50<7/5.
\]
The second's total coefficient is below
\[
 5(41/5)^2(3/100)+2(23/1000)(41/5)
 +2(17)(41/5)(3/100)+7/5
 =12642/625<203/10.\tag{5}
\]
Both exponential norm factors are below2, and the leading 1+4 blocks remain separated: the actual and block-diagonal perturbations of D have norms below0.017, compared to a gap at least2. Rank-three Weyl error is at most three times the matrix error. At \(\epsilon_0=3/100\),
\[
 3(203/10)\epsilon_0=1827/1000<15/8,
\]
so (4) and the predecessor's block comparison give the **same-input, actual-projector** local original-k3 gap
\[
 R_3(p)-K_3(\Lambda_p\rho)\ge\frac{15t\epsilon^2}{128}
\quad (0<t\le1/1000,\ 0\le\epsilon\le3/100).\tag{6}
\]

For inputs whose closest-product gauge has \(\epsilon>3/100\), the predecessor's actual-marginal union bound yields \(8-L>2\epsilon_0^2/(1+\epsilon_0^2)=18/10009\). Its common-P first-order bound has coefficient less than20. At \(t\le8/100000\),
\[
20t\le1/625<18/10009<8-L.
\]
Thus all far pure inputs satisfy the original k3 comparison, the local case follows from (6), and products have the reference spectrum. A single actual P is fixed while averaging any finite pure decomposition of a mixed input. The exact four-site transpose/spin-flip mirror covers the negative-shrink physical interval. This completes the **conditional** reasoning for (1); it does not certify the predecessor or any p outside (1).

## Actual checks and review limits

`frontier-20261028-80-psd-hessian-check.py`, SHA256 `11776cf1b28f6e13661a1f5532477e6ca15086a53bed5ab18065de013ed3d1cd`, ran `python3 -B ...` from repo root, exit0. Exact Gaussian-rational calculations verified (2)'s PSD decomposition on 60 actual complex weight-two directions at \(t=1/1000,1/10,1/2\), checked five mixed-weight margins at \(t=1/1000\), and checked the scalar constants in (5), \(\epsilon_0\), and the far inequality. The PSD conclusion for **every** direction follows from the written \(\Gamma\ge0\) and nonnegative coefficients, not from 60 examples.

The original Hessian identities have the separate finite polarization/interpolation audit in `frontier-20261028-74-hessian-polynomial-audit-report.md`; the off-block bounds have exact and bounded floating audits named in the 77 predecessor. These checks do not establish the all-state theorem, and the necessary predecessor 59, off-block derivation, new PSD argument, norm budgets and same-P bridges require complete disjoint written review. Native checker-pin clock **Wed Oct 28 18:59:05 PDT 2026**.
