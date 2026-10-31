# Common-projector Pauli bound and a state-dependent high-noise k3 interval

**Author-written result; not a uniform-in-state noise interval or global k3 proof.** All input states/projectors below are actual, and the same rank-three \(P\) is used for every Pauli weight. The all-variable algebra needs disjoint review; no novelty, formal/kernel, independent-family or historical-process cure is claimed.

## Exact projector bound

For every complex rank-three orthogonal projector \(P\) on four qubits define
\[
B_1(P)=\sum_{i=1}^4\sum_{a=x,y,z}\bigl(\operatorname{Tr}P\sigma_i^a\bigr)^2.
\]
Then **\(B_1(P)\le20\)**, and 20 is attained by the projector onto \(|0000\rangle,|0001\rangle,|0010\rangle\).

To prove it, independently rotate each local basis so the vector of the three single-site traces points along its local \(Z\) axis. In the resulting product basis put \(p_x=\langle x|P|x\rangle\); then \(0\le p_x\le1\) and \(\sum_xp_x=3\), while
\[
B_1(P)=\sum_{i=1}^4\left(\sum_{x\in\{0,1\}^4}(-1)^{x_i}p_x\right)^2.
\]
This is convex in \((p_x)\). Every vertex of the compact hypersimplex \(0\le p_x\le1,\sum p_x=3\) has exactly three coordinates equal to1 and the rest0: two fractional coordinates could otherwise be perturbed in opposite directions. A convex function is bounded above by its maximum over those vertices. For any three distinct cube vertices, the sum of their three pairwise Hamming distances is at least4: at least two coordinates are nonconstant and each contributes exactly2 to that sum. If their sign vectors are \(s_x\in\{\pm1\}^4\), then
\[
\left\|s_u+s_v+s_w\right\|^2
=36-4\bigl(d(u,v)+d(u,w)+d(v,w)\bigr)\le20.
\]
The displayed three computational basis states attain distances1,1,2 and equality. This proof does not restrict \(P\) to diagonal or separable projectors; diagonal entries are used only after the allowed local rotation.

## Pure-input common-P bound

Let \(\rho\) be any pure four-qubit input. Order local Bloch radii \(0\le r_1\le r_2\le r_3\le r_4\le1\), and put
\[
S=\sum_i r_i^2,\quad L=r_1+r_2+3r_3+3r_4,\quad
C=|\langle\psi|Y^{\otimes4}\bar\psi\rangle|^2,\quad t=|1-p|.
\]
For every physical \(p\in[0,4/3]\) and every actual rank-three \(P\),
\[
16\operatorname{Tr}[P\Lambda_p(\rho)]
\le 3+tL+t^2\sqrt{39(15-S)}.\tag{1}
\]
For positive shrinkage, Pauli expansion gives
\[
16\operatorname{Tr}(P\Lambda_p\rho)
=3+t C_1+\sum_{k=2}^4t^k C_k,
\quad C_k=\sum_{\operatorname{wt}(w)=k}
\operatorname{Tr}(P\sigma_w)\operatorname{Tr}(\rho\sigma_w).
\]
The weight-one term is \(C_1=\operatorname{Tr}(PH)\), where \(H=\sum_i\vec r_i\cdot\vec\sigma_i\). Its commuting eigenvalues are \(\pm r_1\pm\cdots\pm r_4\); the top-three sum is \(3\sum_i r_i-2(r_1+r_2)=L\), including ties. Thus \(C_1\le L\). Pauli Parseval gives \(\sum_{k\ge1}B_k(P)=16\operatorname{Tr}P^2-(\operatorname{Tr}P)^2=39\), while for a pure input \(\sum_{k\ge2}A_k(\rho)=16-1-S=15-S\). Cauchy–Schwarz and \(t^k\le t^2\) for \(k\ge2\), \(0\le t\le1\), yield the remainder in (1). If \(1-p<0\), the exact four-site spin-flip mirror replaces \(P\) by the actual rank-three \(Y^{\otimes4}P^TY^{\otimes4}\), leaving \(\rho,t,r_i\) and the product-reference spectrum unchanged.

The exact reference is \(16R_3(p)=3+8t+6t^2-t^4\). Thus for every actual \((\rho,P)\),
\[
16\bigl(R_3(p)-\operatorname{Tr}[P\Lambda_p\rho]\bigr)
\ge t\Bigl[(8-L)-t\bigl(\sqrt{39(15-S)}-5\bigr)\Bigr],\tag{2}
\]
because \(t^4\le t^2\). Every non-product pure state has \(L<8\): equality would force all four local radii1, hence a pure product. Therefore each fixed non-product pure input has an **explicit positive**, state-dependent original-k3 neighborhood of full depolarization:
\[
0<t<\min\left\{1,\frac{8-L}{\sqrt{39(15-S)}-5}\right\}.\tag{3}
\]
The denominator is positive since \(S\le4\). At \(t=0\) the output and product reference both equal \(I/16\). A pure product input has the exact reference spectrum for every physical p. The threshold in (3) can tend to zero as inputs approach a product state; it is NOT a uniform all-state interval and says nothing about a mixed state unless a valid uniformly controlled pure-state decomposition is supplied.

## Optional tighter scalar relaxation

For a pure input, use the exact invariant identities from `frontier-20261028-39-fourqubit-purity-certificate.md`: \(A_1=S\), \(A_2=2+S+4C\), \(A_3=8-8C-S\), \(A_4=5-S+4C\). Set
\[
u=t^2S,\quad v=t^4A_2+t^6A_3+t^8A_4,\quad b_0=L^2/S\quad(S>0).
\]
For the same projector let \(b=B_1(P)\). Weight-one Cauchy–Schwarz gives \(C_1\le\min(L,\sqrt{Sb})\), and the higher weights give a contribution at most \(\sqrt{v(39-b)}\). Because \(L^2\le20S\), if \(b>b_0\) the expression is no larger than at \(b_0\); if \(b\le b_0\) use the Cauchy bound. Hence the ENTIRE actual pair obeys
\[
16\operatorname{Tr}[P\Lambda_p\rho]\le3+
\max_{0\le b\le b_0}\left(\sqrt{ub}+\sqrt{v(39-b)}\right).\tag{4}
\]
The scalar objective is concave. If \(u+v>0\), its unrestricted maximum is at \(b_*=39u/(u+v)\); evaluate (4) at \(\min\{b_0,b_*\}\). If \(S=0\), the weight-one term vanishes and use \(3+\sqrt{39v}\). If \(t=0\), both \(u,v\) vanish and the bound is3. This is a rigorous relaxation, not a claim that its maximizing b is realizable by a rank-three projector.

The full unrestricted k3 problem remains open outside the guaranteed state-dependent interval, and the sharp general one-/two-erasure layer inequalities are not established by this argument.
