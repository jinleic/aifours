# Exact rank-two overlap optimization for original k3

**Author-written successor** to `frontier-20261028-20-spinflip-overlap-gap.md`; this improves a universal input-dependent lower bound, but can still be negative and does **not** prove full k3 majorization. No configured-family/human/formal review, novelty clearance or historical process cure is claimed.

## Statement

For any pure four-qubit \(\rho=|\psi\rangle\langle\psi|\), order its local Bloch radii \(r_1\le\cdots\le r_4\) and put \(R=\sum_i r_i\), \(L=r_1+r_2+3r_3+3r_4\). Let \(\widetilde\psi=\sigma_y^{\otimes4}\overline\psi\), \(c=|\langle\psi|\widetilde\psi\rangle|\), and \(d=\sqrt{1-c^2}\). For physical \(p\in[0,4/3]\), write \(s=\min(p,2-p)\), \(q=1-s\), \(A=q^4\), \(B=s^2q^2/4\). Then every actual complex rank-three orthogonal projector \(P\) satisfies
\[
\begin{aligned}
R_3(p)-\operatorname{Tr}[P\Lambda_p(\rho)]\ge{}&
\frac{sq}{16}\bigl[8s-(2-s)(2qR+sL)\bigr]\\
&+B+\frac A2-\frac12\sqrt{A^2+4B(B-A)_+d^2}.
\end{aligned}\tag{1}
\]
The right side is at least the preceding spin-flip-overlap lower bound. If \(0<d<1\), \(A>0\) and \(B>A\), it is strictly larger. A fixed-parameter closed-convex-hull extension is valid with common upper caps on \(R,L,d\) for the pure components, since the same projector is used and the displayed right side is nonincreasing in each cap. No claim follows from the local marginals of an arbitrary mixed density alone.

## Proof and exact projector minimization

For \(0\le p\le1\), set \(s=p,q=1-p\). Using the same actual \((\rho,P)\), write \(x=\operatorname{Tr}(P\rho)\), \(y=\operatorname{Tr}(P\widetilde\rho)\), where \(\widetilde\rho=|\widetilde\psi\rangle\langle\widetilde\psi|\). The original erasure expansion, fixed reference coefficients, \(t_1\le3+R/4\), \(t_3\le(12+L)/16\), and the exact spin-flip identity for \(t_2\) give the all-pair bound
\[
R_3(p)-\operatorname{Tr}[P\Lambda_p(\rho)]
\ge\frac{pq}{16}[8p-(2-p)(2qR+pL)]
 +A(1-x)+B(1+x-y).\tag{2}
\]
Those elementary reductions are explicitly derived in the predecessor and use no independently chosen marginal or projector. Define the **actual** Hermitian rank-at-most-two operator
\[
K=(A-B)\rho+B\widetilde\rho.
\]
The last terms in (2) equal \(A+B-\operatorname{Tr}(PK)\). We minimize this expression over actual rank-three projectors using the Ky-Fan principle in the 16-dimensional space.

If \(A\ge B\), then \(K\ge0\), has rank at most two and trace \(A\). The sum of its three largest eigenvalues is exactly \(A\), so the minimum is \(B\). If \(A<B\), in the span of \(\psi,\widetilde\psi\) the trace of \(K\) is \(A\) and its determinant is \((A-B)B(1-c^2)=-(B-A)Bd^2\). Its two possible nonzero eigenvalues are therefore
\[
\lambda_{\pm}=\frac{A\pm\sqrt{A^2+4B(B-A)d^2}}2.
\]
Since \(\lambda_-\le0\), and the 16-dimensional space has at least two additional zero eigenvalues, the sum of the top three is \(\lambda_+\). Thus the exact minimum is \(B+A/2-\tfrac12\sqrt{A^2+4B(B-A)d^2}\). The formula also holds when \(c=1\), rank drops, or a coefficient vanishes. Combining cases gives (1) with \((B-A)_+\); this is the **exact** minimization of the particular retained-overlap expression, not a claim that the earlier layer bounds are simultaneously sharp.

When \(A<B\), compare with the predecessor's term \(B-d(B-A)\). Both \(A+2d(B-A)\) and the square root are nonnegative and
\[
[A+2d(B-A)]^2-[A^2+4B(B-A)d^2]
=4A(B-A)d(1-d)\ge0.
\]
This proves domination, with strictness under the stated interior conditions. For \(A\ge B\), both terms equal \(B\).

For \(1\le p\le4/3\), the exact channel mirror \(\Lambda_p(X)=U\Lambda_{2-p}(X)^TU\), \(U=\sigma_y^{\otimes4}\), changes \(P\) deterministically to \(UP^TU\) but leaves the input \(\rho\), the parameters \(R,L,c,d\), and the product-reference spectrum unchanged. Thus (1) holds throughout the physical interval, with endpoints included without division. No external theorem beyond the stated finite-dimensional spectral/Ky-Fan facts is used.
