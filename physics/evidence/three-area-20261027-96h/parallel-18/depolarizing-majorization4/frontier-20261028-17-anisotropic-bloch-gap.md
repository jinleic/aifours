# Anisotropic local-radius bound for original four-qubit k3

**Author-written successor to `frontier-20261028-14-sharpened-bloch-gap.md`; not a global proof.** This retains the exact ordering of the four local marginal radii rather than replacing them all by their sum. No independent written/model/human review, formal verification or novelty clearance is claimed. The parent, not this artifact, decides any adoption; historical process records are not cured.

## Statement

For any pure four-qubit density \(\rho\), order the one-qubit Bloch radii \(0\le r_1\le r_2\le r_3\le r_4\le1\), and write
\[
R=r_1+r_2+r_3+r_4,\qquad L=r_1+r_2+3r_3+3r_4.
\]
For every actual complex rank-three projector \(P\) and physical \(p\in[0,4/3]\), let \(s=\min(p,2-p)\), \(q=1-s\), and \(h=\min(q^4,s^2q^2/4)\). Then
\[
\boxed{R_3(p)-\operatorname{Tr}[P\Lambda_p(\rho)]
\ge\frac{sq}{16}\Bigl[8s-(2-s)(2qR+sL)\Bigr]+h.}\tag{1}
\]
The right-hand side can be negative. Whenever it is nonnegative, the original Ky-Fan-3 product-reference inequality follows for the given pure input; when it is positive the gap is strict. A fixed-parameter closed-convex-hull extension is valid when all component pure inputs have a common upper cap on \((2-s)(2qR+sL)\). It is not valid merely from the marginals of an arbitrary mixed density without such a decomposition.

Compared to the predecessor's bound using only \(R\), the new right-hand side improves it by exactly
\[
\frac{s^2q(2-s)}{16}(3R-L)
=\frac{s^2q(2-s)}8(r_1+r_2)\ge0.
\]
In particular, the four-qubit W state has all \(r_i=1/2\), so \(R=2,L=4\). At \(p=2/3\) and \(p=4/3\), equation (1) gives the strict lower gap \(1/81\); the coarser predecessor gives a negative bound there. This is a concrete proper-family example of the stronger certificate, not a claim that W is new or that arbitrary states are covered.

## Derivation

For \(0\le p\le1\), use one actual pair \((\rho,P)\), \(q=1-p\), and \(t_m=\operatorname{Tr}[P\sum_{|S|=m}E_S(\rho)]\). From the Schmidt spectrum of each single-erasure output,
\[
t_1\le3+R/4.
\]
The three-erasure output is a sum of commuting one-qubit marginals, so its three largest eigenvalues yield
\[
t_3\le(12+L)/16.
\]
The exact spin-flip identity gives, with \(x=t_0\in[0,1]\) and \(y=\operatorname{Tr}(P\widetilde\rho)\le1\),
\[
4t_2=y-x+2t_1+8t_3-3
\le10-x+(R+L)/2,
\qquad t_2\le5/2-x/4+(R+L)/8.
\]
The same fixed product reference has erasure coefficients \((1,3,3,5/4,3/16)\); subtracting termwise in the original channel expansion, with nonnegative weights, gives
\[
\begin{aligned}
R_3(p)-\operatorname{Tr}[P\Lambda_p(\rho)]\ge{}&
q^4(1-x)-\frac R4pq^3
+\left(\frac12+\frac x4-\frac{R+L}{8}\right)p^2q^2\\
&+\frac{8-L}{16}p^3q\\
={}&q^4(1-x)+\frac{p^2q^2}4x\\
&+\frac{pq}{16}\Bigl[8p-(2-p)(2qR+pL)\Bigr].
\end{aligned}
\]
The first two terms form a convex combination, bounded below by \(\min(q^4,p^2q^2/4)\). The identity \(\Lambda_p(X)=U\Lambda_{2-p}(X)^TU\), \(U=\sigma_y^{\otimes4}\), transfers the result from \([0,1]\) to \([1,4/3]\) with the deterministic rank-three projector \(UP^TU\), the same input \(\rho\), the same local radii and identical product-reference spectrum. The endpoints require no division.

This certificate is inconclusive for pure inputs where its lower bound is negative and for mixed inputs not decomposed as above; other separately supported scopes may cover some such cases. It does not settle the remaining all-variable problem.
