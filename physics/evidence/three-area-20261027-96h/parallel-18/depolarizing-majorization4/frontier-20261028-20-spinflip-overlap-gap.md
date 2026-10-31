# Original k3 bound with exact spin-flip overlap

**Author-written successor** to `frontier-20261028-17-anisotropic-bloch-gap.md`. It is an all-pure-state/all-actual-projector lower bound, not an all-state majorization proof: its right-hand side can be negative. No external-model/human/formal review, novelty clearance or historical process cure is claimed.

## Statement

For every pure four-qubit \(\rho=|\psi\rangle\langle\psi|\), let \(r_1\le r_2\le r_3\le r_4\) be the local Bloch radii, \(R=\sum r_i\), \(L=r_1+r_2+3r_3+3r_4\), and
\[
\widetilde\psi=\sigma_y^{\otimes4}\overline\psi,\qquad
c=|\langle\psi|\widetilde\psi\rangle|,\qquad d=\sqrt{1-c^2}.
\]
For every actual complex rank-three projector \(P\) and every physical \(p\in[0,4/3]\), write \(s=\min(p,2-p)\), \(q=1-s\), \(A=q^4\), \(B=s^2q^2/4\). Then
\[
 R_3(p)-\operatorname{Tr}[P\Lambda_p(\rho)]
 \ge\frac{sq}{16}\Bigl[8s-(2-s)(2qR+sL)\Bigr]
 +B-d\,(B-A)_+.\tag{1}
\]
Here \((v)_+=\max(v,0)\). This improves the preceding anisotropic bound by exactly
\[
 (1-d)(B-A)_+\ge0.
\]
It is strictly stronger when \(2/3<s<1\) and \(c>0\). As before, nonnegative right side suffices for the original k3 comparison, and a strictly positive right side supplies an explicit gap. The same fixed-parameter bound with fixed caps \(R\le R_0,L\le L_0,d\le d_0\) extends to the closed convex hull of those pure inputs by affinity in the SAME \(P\); arbitrary mixed-state marginal data alone do not prove such a decomposition.

## Proof

It suffices first to take \(0\le p\le1\), with \(s=p\), \(q=1-p\). Use one actual pair \((\rho,P)\) and \(t_m=\operatorname{Tr}[P\sum_{|S|=m}E_S(\rho)]\), \(x=t_0\), \(y=\operatorname{Tr}(P\widetilde\rho)\), where \(\widetilde\rho=|\widetilde\psi\rangle\langle\widetilde\psi|\). The exact spin-flip identity and ordinary Schmidt/marginal diagonalizations give
\[
4t_2=y-x+2t_1+8t_3-3,\quad
 t_1\le3+R/4,\quad t_3\le(12+L)/16.
\]
Set \(z=1-x\in[0,1]\). Since \(y\le1\), \(y-x\le z\). Separately \(D=\widetilde\rho-\rho\) has trace0, rank at most2 and \(\operatorname{Tr}D^2=2(1-c^2)\); its only possible nonzero eigenvalues are \(\pm d\). Because \(P\) is an orthogonal projector, \(\operatorname{Tr}(PD)\le d\). Both estimates are for the SAME projector, hence
\[
y-x\le\min(d,z).
\]
Substitution into the original-channel erasure expansion and subtraction from the fixed product-reference coefficients yields
\[
 R_3(p)-\operatorname{Tr}[P\Lambda_p(\rho)]
 \ge\frac{pq}{16}\Bigl[8p-(2-p)(2qR+pL)\Bigr]
 +Az+B(1-\min(d,z)).\tag{2}
\]
For \(0\le z\le d\), the last expression is \(B+(A-B)z\); for \(d\le z\le1\), it is \(Az+B(1-d)\). Its minimum is \(B\) if \(A\ge B\), and \(B-d(B-A)\) if \(A<B\), i.e. \(B-d(B-A)_+\). This proves (1) on \([0,1]\) including degenerate \(c=0,1\) and endpoint cases.

For \(1\le p\le4/3\), the exact mirror identity \(\Lambda_p(X)=U\Lambda_{2-p}(X)^TU\), \(U=\sigma_y^{\otimes4}\), transforms the actual \(P\) to the actual rank-three \(UP^TU\) while leaving \(\rho,R,L,c,d\) and the reference spectrum unchanged. This proves (1) on the full physical interval. The projected trace bound holds uniformly in \(P\), so Ky-Fan variational maximization gives the corresponding original-spectrum bound. The full global problem remains unproved wherever this lower bound is negative, except where separately supported results apply.
