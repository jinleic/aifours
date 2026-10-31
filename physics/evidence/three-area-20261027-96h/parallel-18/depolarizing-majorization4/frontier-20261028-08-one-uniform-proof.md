# Original k3 bound with an explicit gap for one-uniform pure states

**Author candidate, ordinary written mathematics; not a full original-domain proof.** The class below contains genuinely multipartite-entangled inputs but is a proper class. No novelty, independent-family review, formal verification, or coverage of all mixed inputs with maximally mixed one-qubit marginals is asserted. The derivation is supplied in full and does not import a historical held result as a premise; prior exposure/process history is not erased.

## Statement

Let \(\Phi_p(X)=(1-p)X+(p/2)\operatorname{Tr}(X)I_2\), \(\Lambda_p=\Phi_p^{\otimes4}\), and \(0\le p\le4/3\). Suppose \(\rho\) lies in the **convex hull of pure four-qubit states whose four one-qubit marginals are exactly \(I_2/2\)**. Let \(P\) be any actual complex rank-three orthogonal projector. Put
\[
 s=\min\{p,2-p\},\quad a=1-s/2,\quad b=s/2,\quad R_3(p)=a^4+2a^3b.
\]
Then
\[
 \operatorname{Tr}[P\Lambda_p(\rho)]
 \le R_3(p)-\frac12s^2(1-s).\tag{A}
\]
Thus the original output Ky-Fan-3 sum obeys the same inequality. The margin is strictly positive for \(0<p<4/3\), \(p\ne1\), and also at \(p=4/3\); at \(p=0,1\) it vanishes. Both density and projector are the original actual objects, and the same \(P\) is used through every term. The convex-hull scope is explicit: it is **not** a claim for every mixed state with maximally mixed local marginals.

## Pure-input proof

First take \(0\le p\le1\) and a pure input \(\rho=|\psi\rangle\langle\psi|\) with each local marginal \(I_2/2\). Define \(E_i(X)=I_i\otimes\operatorname{Tr}_iX/2\), restoring original tensor order, \(E_S=\prod_{i\in S}E_i\), and
\[
T_m=\sum_{|S|=m}E_S(\rho),\qquad t_m=\operatorname{Tr}(PT_m).
\]
All \(E_i\) commute, so
\[
\operatorname{Tr}[P\Lambda_p(\rho)]
=\sum_{m=0}^4(1-p)^{4-m}p^m t_m.\tag{B}
\]

1. \(t_0=\operatorname{Tr}(P\rho)\le1\), and \(T_4=I_{16}/16\), hence \(t_4=3/16\).
2. Across each one-versus-three cut, the pure input has Schmidt coefficients \(1/\sqrt2,1/\sqrt2\). Thus \(E_i(\rho)=I_i\otimes\rho_{\bar i}/2\) has exactly four nonzero eigenvalues, each \(1/4\). Any rank-three projector captures at most \(3/4\); summing gives \(t_1\le3\).
3. \(T_3=\frac18\sum_i \rho_i\otimes I_{\bar i}=I_{16}/4\), so \(t_3=3/4\) exactly.
4. Define \(Y=\sigma_y^{\otimes4}\) and \(\widetilde\rho=Y\rho^T Y\). The one-qubit identity \(\sigma_yX^T\sigma_y=\operatorname{Tr}(X)I_2-X=2E_i(X)-X\), tensored on all four sites, gives the **operator** identity
\[
\widetilde\rho=T_0-2T_1+4T_2-8T_3+16T_4.\tag{C}
\]
This uses the original computational-basis global transpose. \(\widetilde\rho\) is a density, so \(0\le\operatorname{Tr}(P\widetilde\rho)\le1\). Solving (C) for \(t_2\), and using the same \(P,\rho\) throughout,
\[
4t_2=\operatorname{Tr}(P\widetilde\rho)-t_0+2t_1+8t_3-16t_4
\le1+6+6-3=10,
\quad\text{hence }t_2\le5/2.\tag{D}
\]

For a pure product reference and one fixed maximizing rank-three projector, its layer coefficients are \((1,3,3,5/4,3/16)\). One direct derivation is to choose \(|0000\rangle\) and the span of \(|0000\rangle,|1000\rangle,|0100\rangle\); at erasure size \(m\) the coefficient is \(2^{-m}[\binom4m+2\binom3{m-1}]\). Comparing those coefficients with the four bounds above in (B), including the SAME \(P\), yields
\[
R_3(p)-\operatorname{Tr}[P\Lambda_p(\rho)]
\ge\frac12p^2(1-p)^2+\frac12p^3(1-p)
=\frac12p^2(1-p).
\]
No term in the comparison is assigned an independent optimizer.

## Mixtures and the full physical interval

For an arbitrary finite convex combination of such pure inputs, the same \(P,p\) applies to each summand and the trace is affine, so the identical bound holds. In finite dimensions the closed convex hull has the same bound by continuity.

For \(1\le p\le4/3\), put \(p'=2-p\in[2/3,1]\). The single-qubit identity above implies
\[
\Lambda_p(X)=Y\Lambda_{p'}(X)^T Y.
\]
Therefore \(\operatorname{Tr}[P\Lambda_p(\rho)]=\operatorname{Tr}[YP^TY\,\Lambda_{p'}(\rho)]\), with \(YP^TY\) again a rank-three orthogonal projector; the product-reference spectra at \(p\) and \(p'\) are equal. Applying the preceding result to this deterministic projector and the SAME \(\rho\) gives (A). The finite-dimensional Ky-Fan variational principle then gives the stated spectrum bound.

The original unresolved complement is all physical inputs outside this specified convex hull. The two global coefficient inequalities in `frontier-20261028-06-erasure-certificate.md` remain unproved; this proposition does not assert them.
