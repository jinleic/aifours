# Stronger original k3 lower bound using the common overlap

**Author-written successor** to `frontier-20261028-11-bloch-gap.md`, not a global k3 proof. It keeps the overlap of the **same** input and projector rather than dropping it from the two-erasure estimate. It has not received independent written review, formal verification or novelty clearance; historical held results are not taken as premises.

For every pure four-qubit density \(\rho\), every actual complex rank-three orthogonal projector \(P\), and every physical parameter \(0\le p\le4/3\), put \(R=\sum_i r_i\), where \((1\pm r_i)/2\) are the local marginal eigenvalues, and \(s=\min(p,2-p)\). Then
\[
\begin{aligned}
R_3(p)-\operatorname{Tr}[P\Lambda_p(\rho)]\ge{}&
\frac{s(1-s)}{16}\left[8s-R(4-s^2)\right]\\
&+\min\!\left\{(1-s)^4,\;\frac{s^2(1-s)^2}{4}\right\}.\tag{1}
\end{aligned}
\]
The added term is nonnegative and positive for \(0<s<1\). Hence this bound strictly improves the previous one there, though it can still be negative and does not settle the original general case. It extends, for fixed \(p\) and a fixed cap \(R_0\), with \(R_0\) on the right, to the closed convex hull of pure states whose total radius is at most \(R_0\); the same \(P\) is used for every summand.

For \(0<s<1\), the bound is nonnegative when
\[
R\le\begin{cases}
\displaystyle\frac{4s(3-s)}{4-s^2},&0<s\le2/3,\\[4pt]
\displaystyle\frac{8s+16(1-s)^3/s}{4-s^2},&2/3\le s<1.
\end{cases}\tag{2}
\]
Strict inequality gives a strict gap. At \(s=2/3\), both thresholds equal \(7/4\). This is only a sufficient state/noise region and does not cover the unconstrained genuinely entangled complement.

## Proof

On \(0\le p\le1\), use the same-pair erasure notation \(t_m=\operatorname{Tr}(P\sum_{|S|=m}E_S(\rho))\), the exact reference coefficients \((1,3,3,5/4,3/16)\), and the previously derived elementary pure-input estimates
\[
t_1\le3+R/4,\qquad t_3\le(12+3R)/16,\qquad t_4=3/16.
\]
These follow directly from Schmidt coefficients and simultaneous diagonalization of the one-qubit marginals, respectively; their full derivation appears in the predecessor. Put \(x=t_0=\operatorname{Tr}(P\rho)\in[0,1]\), \(q=1-p\), and \(y=\operatorname{Tr}(P\widetilde\rho)\in[0,1]\), where \(\widetilde\rho=\sigma_y^{\otimes4}\rho^T\sigma_y^{\otimes4}\). The exact global spin-flip/erasure identity gives
\[
4t_2=y-x+2t_1+8t_3-3
\le 10-x+2R,\qquad t_2\le\frac52-\frac x4+\frac R2.\tag{3}
\]
Subtracting from the fixed product reference termwise in the original channel expansion yields
\[
\begin{aligned}
R_3(p)-\operatorname{Tr}[P\Lambda_p(\rho)]\ge{}&
q^4(1-x)-\frac R4pq^3
+\left(\frac12+\frac x4-\frac R2\right)p^2q^2\\
&+\left(\frac12-\frac{3R}{16}\right)p^3q\\
={}&\frac{pq}{16}\left[8p-R(4-p^2)\right]
+q^4(1-x)+\frac{p^2q^2}{4}x.
\end{aligned}
\]
Since \(0\le x\le1\), the last two terms are a convex combination of \(q^4\) and \(p^2q^2/4\), hence at least their minimum. The derivation uses one actual \((\rho,P)\), never independently optimized layer values.

For \(1\le p\le4/3\), the exact physical mirror \(\Lambda_p(X)=U\Lambda_{2-p}(X)^TU\), \(U=\sigma_y^{\otimes4}\), maps the single projector to \(UP^TU\) and leaves \(\rho,R\) and the product-reference spectrum unchanged. This gives (1) with \(s=2-p\). The endpoints are valid without division. Equation (2) only divides by \(s\) for \(0<s<1\).
