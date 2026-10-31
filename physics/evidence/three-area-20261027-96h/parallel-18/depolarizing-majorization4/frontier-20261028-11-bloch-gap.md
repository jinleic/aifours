# Original k3: quantitative pure-input bound from local Bloch radii

**Status:** author-written all-parameter actual-pair inequality; independent written review and novelty clearance not performed. It is not a global k3 proof: the displayed lower bound can be negative. No historically held result is imported as a mathematical premise, and prior exposure/process history is not erased.

## Statement

For every pure four-qubit state \(\rho\), define \(r_i\in[0,1]\) by the eigenvalues \((1\pm r_i)/2\) of its \(i\)-th one-qubit marginal, and let \(R=\sum_i r_i\). For every actual complex rank-three orthogonal projector \(P\) and every physical depolarizing parameter \(0\le p\le4/3\), put \(s=\min\{p,2-p\}\in[0,1]\). The original-channel product-reference margin obeys
\[
 R_3(p)-\operatorname{Tr}[P\Lambda_p(\rho)]
 \ge\frac{s(1-s)}{16}\bigl(8s-R(4-s^2)\bigr).\tag{1}
\]
When \(0<s<1\) and \(R<8s/(4-s^2)\), the right-hand side is strictly positive, so the original k3 majorization bound holds with an explicit positive gap. At equality in that condition the bound is nonnegative. For a fixed \(p\) and fixed \(R_0\), the same inequality with \(R_0\) on the right holds on the closed convex hull of pure inputs with \(R\le R_0\): the same \(P\) is used for every summand, and the trace is affine and continuous. In particular this gives a uniform positive gap when \(R_0<8s/(4-s^2)\). It is NOT a statement that the radii of an arbitrary mixed input alone certify such a decomposition.

At \(R=0\), (1) becomes the one-uniform bound \(s^2(1-s)/2\). For parameters and inputs with negative right side, (1) remains valid but does not decide original k3.

## Derivation on \(0\le p\le1\)

With \(E_i(X)=I_i\otimes\operatorname{Tr}_iX/2\), write \(T_m=\sum_{|S|=m}E_S(\rho)\), \(t_m=\operatorname{Tr}(PT_m)\), and use the exact same-pair expansion
\[
\operatorname{Tr}[P\Lambda_p(\rho)]
=\sum_{m=0}^4 (1-p)^{4-m}p^m t_m.\tag{2}
\]
The reference coefficients for one actual fixed product projector are \((1,3,3,5/4,3/16)\). Trivially \(t_0\le1\), \(t_4=3/16\).

Across cut \(i\mid\bar i\), purity gives two Schmidt eigenvalues \((1\pm r_i)/2\). Thus \(E_i(\rho)\) has two copies of each half-Schmidt eigenvalue, and a rank-three projector captures at most \((3+r_i)/4\). Consequently
\[
 t_1\le3+R/4.\tag{3}
\]
Independently, \(T_3=(1/8)\sum_i\rho_i\otimes I_{\bar i}\). If \(r_1\le r_2\le r_3\le r_4\) after relabeling, direct simultaneous diagonalization gives
\[
 t_3\le\frac{12+r_1+r_2+3r_3+3r_4}{16}
 \le A:=\frac{12+3R}{16}.\tag{4}
\]
The inequality is still valid if this coarse \(A\) exceeds the sharper universal \(5/4\).

Define \(\widetilde\rho=\sigma_y^{\otimes4}\rho^T\sigma_y^{\otimes4}\). It is an actual density. Tensoring the elementary one-qubit identity \(\sigma_yX^T\sigma_y=2E_i(X)-X\) gives
\[
\widetilde\rho=T_0-2T_1+4T_2-8T_3+16T_4.
\]
Thus, using the SAME \(P\), \(0\le\operatorname{Tr}(P\widetilde\rho)\le1\), \(t_0\ge0\), (3), and (4),
\[
 t_2\le\frac{1+2(3+R/4)+8A-3}{4}
 =\frac52+\frac R2.\tag{5}
\]
Subtract the bounds (3)–(5) termwise from the fixed product reference using nonnegative coefficients in (2). Even when an individual resulting lower bound is negative, the inequality remains valid:
\[
\begin{aligned}
R_3(p)-\operatorname{Tr}[P\Lambda_p(\rho)]\ge{}&
-\frac R4p(1-p)^3
+\left(\frac12-\frac R2\right)p^2(1-p)^2\\
&+\left(\frac12-\frac{3R}{16}\right)p^3(1-p)\\
={}&\frac{p(1-p)}{16}\bigl(8p-R(4-p^2)\bigr).
\end{aligned}\tag{6}
\]
No optimized marginal, state or projector was substituted for the common actual pair.

## Mirror and endpoints

For \(p\in[1,4/3]\), set \(p'=2-p\). The same elementary transpose identity gives \(\Lambda_p(X)=U\Lambda_{p'}(X)^TU\), \(U=\sigma_y^{\otimes4}\), and \(\operatorname{Tr}[P\Lambda_p(\rho)]=\operatorname{Tr}[UP^TU\,\Lambda_{p'}(\rho)]\). The transformed projector is still one actual rank-three orthogonal projector, while \(\rho\) and all \(r_i\) are unchanged. The product-reference spectrum is unchanged, establishing (1) for the whole physical interval. \(p=0,1\) are included without division; their right-hand side vanishes.

This is a sufficient, state-and-parameter-dependent original-channel result only. The general genuinely entangled residual where \(R>8s/(4-s^2)\), and the exact global layer inequalities, remain open.
