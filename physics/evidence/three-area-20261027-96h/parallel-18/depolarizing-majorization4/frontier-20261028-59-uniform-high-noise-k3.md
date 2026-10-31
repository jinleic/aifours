# Candidate: an explicit uniform high-noise interval for original four-qubit k3

**HIGH-CONSEQUENCE AUTHOR-WRITTEN CANDIDATE — INDEPENDENT REVIEW REQUIRED.** The proposed statement is substantially stronger than the preceding \(\forall\rho\exists\epsilon_\rho\) result. It does **not** settle arbitrary physical p, any other k, current priority or novelty. The numerical constant below is intentionally very conservative. No historical held result is treated as a mathematical premise; prior process/exposure history is not cured. All estimates and their exact arithmetic are supplied for direct review.

## 1. Proposed original-channel theorem

Let \(\Phi_p(X)=(1-p)X+(p/2)\operatorname{Tr}(X)I_2\), \(\Lambda_p=\Phi_p^{\otimes4}\), and let \(R_3(p)\) be the top-three output eigenvalue sum for a pure product input. For every four-qubit density \(\rho\), every actual complex rank-three orthogonal projector \(P\), and every physical p satisfying
\[
 |1-p|\le10^{-33},
\]
the candidate proves
\[
 \operatorname{Tr}[P\Lambda_p(\rho)]\le R_3(p).\tag{1}
\]
Hence the original \(k=3\) spectral majorization inequality holds on that **uniform** interval. The statement includes arbitrary pure, mixed and genuinely multipartite-entangled inputs, both sides of \(p=1\), and endpoints. Its explicit interval is not claimed optimal, and no result is claimed outside it.

The proof has three pieces: a uniform strict product-boundary second-order estimate; a quantitative gap away from product states; and affinity for mixed states with the SAME \(P\). The rescaled-noise matrix below avoids division singularities as \(p\to1\).

## 2. Product gauge and second-order coefficients

By the exact channel mirror, it suffices to take shrinkage \(t=1-p\in[0,1/4]\); for the negative-shrink side the one actual projector changes deterministically to \(Y^{\otimes4}P^TY^{\otimes4}\) and the input and reference spectrum are unchanged.

For a normalized pure \(\psi\), let
\[
 m(\psi)=\max_{u_1,\ldots,u_4}|\langle u_1u_2u_3u_4|\psi\rangle|^2.
\]
The maximum exists. Choose such a product maximizer and local unitary bases making it \(|0000\rangle=:|0\rangle\). If \(m>0\), varying one local ket in an arbitrary complex tangent direction at the maximum gives \(\langle i|\psi\rangle=0\) for each of the four weight-one basis vectors \(|i\rangle\). After a global phase,
\[
 |\psi\rangle=\frac{|0\rangle+\epsilon|v\rangle}{\sqrt{1+\epsilon^2}},\qquad
 \epsilon=\sqrt{(1-m)/m},\quad \|v\|=1,
\]
where v is supported on weights2,3,4; \(\epsilon=0\) is the product state. Local channel covariance preserves the output spectrum.

Write \(a=(1+t)/2,b=(1-t)/2\), and \(\lambda_h=a^{4-h}b^h\). At the reference product input, \(\lambda_0\) has multiplicity1 and \(\lambda_1\) multiplicity4. For fixed \(v\), put
\[
V=\Lambda_{1-t}(|v\rangle\langle0|+|0\rangle\langle v|),\quad
W=\Lambda_{1-t}(|v\rangle\langle v|)-\Lambda_{1-t}(|0\rangle\langle0|).
\]
The first-order compression of V to the weight0/weight1 spaces is zero. Let i,j range over the four weight-one basis indices and k over weights2–4. Define the **actual** second-order scalar and Hermitian 4×4 matrix
\[
A=W_{00}+\sum_k\frac{|V_{k0}|^2}{\lambda_0-\lambda_{|k|}},\qquad
M_{ij}=W_{ij}+\sum_k\frac{V_{ik}V_{kj}}{\lambda_1-\lambda_{|k|}}.\tag{2}
\]
Write \(K_2(M)=\lambda_1(M)+\lambda_2(M)\) for its two largest *algebraic* eigenvalues. In §4 below the uniform perturbation argument justifies that the second-order change of the actual output top3 is \(A+K_2(M)\).

The channel commutes with global excitation-phase rotations. Therefore, if \(v=v_2+v_3+v_4\), the quantities in (2) have **no cross-weight terms**: \(A=\sum_h A(v_h)\), \(M=\sum_h M(v_h)\). This follows directly from the input/output excitation-number difference of every matrix unit; in the virtual sum, a weight-h direction couples a weight-one output only to weight h+1. For normalized v, put \(m_h=\|v_h\|^2\). The variational definition gives \(K_2(\sum_hM_h)\le\sum_hK_2(M_h)\), so it is enough to bound each normalized weight separately and multiply by its \(m_h\).

## 3. Uniform negative second-order bound

All formulas in this section are for \(0<t<1\). The exact coefficient identities were independently exercised over rational complex directions, including mixed weights, as described in §7.

### Weight 2

Let \(v_2=\sum_{i<j}c_{ij}|ij\rangle\), \(\sum_{i<j}|c_{ij}|^2=1\), and let \(T\) be the symmetric zero-diagonal matrix with \(T_{ij}=c_{ij}\). Put \(\Gamma=TT^\dagger\), \(n_i=\Gamma_{ii}\), \(u=t(1-t^2)\). Direct single-site channel matrix-unit calculation gives
\[
A_2=-a^2u,\quad (M_2)_{ii}=-abu(1-n_i),\quad
(M_2)_{ij}=ab\,t^2(1+t)\Gamma_{ij}\ (i\ne j).\tag{3}
\]
Here \(\Gamma\ge0\), \(\operatorname{Tr}\Gamma=2\), \(0\le n_i\le1\). Set \(X=\sum_i n_i^2\in[1,2]\). Since \(\operatorname{Tr}\Gamma^2\le4\), (3) implies
\[
\frac{\|M_2-\operatorname{Tr}(M_2)I/4\|_F^2}
 {a^2b^2t^2(1+t)^2}
\le(1-t)^2(X-1)+t^2(4-X)\le3.\tag{4}
\]
The last expression is affine in X; its endpoint values are \(3t^2\le3\) and \((1-t)^2+2t^2\le2\). For any rank-two projection Q in dimension4, \(\|Q-I/2\|_F=1\), and \(\operatorname{Tr}M_2=-2abu\). Thus
\[
K_2(M_2)\le-ab u+\|M_2-\operatorname{Tr}(M_2)I/4\|_F
<-ab u+\tfrac78a u,
\]
because \(\sqrt3/2<7/8\) and \(u=2bt(1+t)\). With \(a+b=1\),
\[
 A_2+K_2(M_2)\le-\frac{a u}{8}.\tag{5}
\]

### Weight 3

Write \(v_3=\sum_i g_i|\bar i\rangle\), where \(|\bar i\rangle\) has ones except at i and \(\sum_i|g_i|^2=1\), and set \(D=1-ab=(3+t^2)/4\). Direct calculation gives
\[
\begin{aligned}
A_3&=-atD+\frac{at^5}{D},\\
M_3&=-a^2btI-b^2t(1+t)\operatorname{diag}(|g_i|^2)
 +\left(t^2b^2+\frac{t^5b}{D}\right)\bar g\bar g^\dagger.
\end{aligned}\tag{6}
\]
Discard the negative diagonal and bound the rank-one positive part by its trace. Then
\[
\begin{aligned}
A_3+K_2(M_3)
&\le-atD-2a^2bt+t^2b^2+\frac{t^5}{D}\\
&=-\frac{t(1-t)(15+24t+38t^2+32t^3+3t^4)}{32D}.\tag{7}
\end{aligned}
\]

### Weight 4 and a common margin

For \(v_4\) equal to \(|1111\rangle\) up to phase, put \(D_4=a^2+b^2=(1+t^2)/2\). Then
\[
A_4=-tD_4+\frac{t^7}{D_4},\qquad M_4=-abtI,
\qquad A_4+K_2(M_4)=-t+\frac{t^7}{D_4}.\tag{8}
\]
Equations (5), (7), (8), weight additivity and top-two subadditivity imply, for **every unit complex v supported on weights2–4** and \(0<t\le1/4\),
\[
 A+K_2(M)\le-\frac{15}{256}t.\tag{9}
\]
Indeed \(a(1-t^2)/8\ge15/256\); the magnitude in (7), divided by t, is at least \(45/98>15/256\); the magnitude in (8), divided by t, is at least \(2047/2048>15/256\). The weight-2 margin is the conservative **15/256**, not the larger figure emitted by an earlier exploratory checker: that exploratory figure used the invalid simplification \(a-ab=at\). The checker was corrected and rerun **before its final pin**; no earlier theorem was reported from the erroneous figure.

## 4. A uniform finite-dimensional perturbation bound

For arbitrary four-qubit X and \(t>0\), define the rescaled linear map
\[
\mathcal H_t(X)=\frac{16\Lambda_{1-t}(X)-\operatorname{Tr}(X)I}{t}
=\sum_{k=1}^4t^{k-1}\sum_{\operatorname{wt}(w)=k}\operatorname{Tr}(X\sigma_w)\sigma_w,
\]
which extends polynomially to \(t=0\). Put \(H_t(\epsilon)=\mathcal H_t(\rho(\epsilon))\). For \(t\in[0,1/4]\), the weight-0, weight-1 and remaining reference blocks have **rescaled** spectral gaps
\[
 d_0-d_1=2(1+t)^3\ge2,\qquad
 d_1-d_2=2(1+t)^2(1-t)\ge3/2.\tag{10}
\]
No spectral gap between individual directions inside the fourfold block is assumed.

For \(|\epsilon|\le1\), writing \(H=D+\epsilon V_H+\epsilon^2W_H+\epsilon^3R\), the finite Pauli-string counts `(12,54,108,81)` and \(t\le1/4\) give
\[
\|\mathcal H_t(X)\|\le34\|X\|_1,\quad
\|D\|\le6,\quad \|V_H\|,\|W_H\|\le68,\quad \|R\|\le136.\tag{11}
\]
Indeed the trace norms of \(|v\rangle\langle0|+|0\rangle\langle v|\) and \(|v\rangle\langle v|-|0\rangle\langle0|\) are2. Normalization gives the stated cubic remainder. The first-order compression of \(V_H\) to the two leading blocks is zero.

For completeness, one elementary uniform block diagonalization gives a **conservative explicit remainder**. Let the three reference blocks be weight0, weight1 and the rest. Set the off-block entries of an anti-Hermitian \(S_1\) to \(-(V_H)_{ij}/(d_i-d_j)\) and its within-block entries to0. By (10), \(\|S_1\|\le800\) using the 16×16 Frobenius bound. For \(|\epsilon|\le10^{-6}\), the unitary conjugation \(e^{-\epsilon S_1}He^{\epsilon S_1}\) eliminates first-order off-blocks. Its second coefficient is
\[
Q=W_H+[V_H,S_1]+\tfrac12[[D,S_1],S_1],\qquad
\|Q\|<7{,}788{,}868<8\cdot10^6.
\]
Using \(\|[X,Y]\|\le2\|X\|\|Y\|\) and \(e^{2|\epsilon|\|S_1\|}<2\), the cubic remainder after this first conjugation has norm less than \(9\cdot10^9|\epsilon|^3\). Define anti-Hermitian \(S_2\) from the off-block entries of Q by the same divided-gap rule; \(\|S_2\|<10^8\). Conjugating next by \(e^{\epsilon^2S_2}\) removes all second-order off-blocks. Its total cubic remainder is bounded by
\[
\begin{aligned}
&6(2\cdot10^8)^2(10^{-6})
 +2(68)(2\cdot10^8)
 +2(8\cdot10^6)(2\cdot10^8)(10^{-6})+9\cdot10^9\\
&=279{,}400{,}000{,}000<10^{12},
\end{aligned}\tag{12}
\]
times \(|\epsilon|^3\). The first-order block diagonal is a pinching of \(V_H\), hence has norm at most68 and vanishes on the two leading blocks. The leading second-order blocks are exactly the rescaled versions of A and M in (2). The remaining block stays separated by the gaps in (10) for \(|\epsilon|\le10^{-6}\), using (11) and the displayed coefficient bounds. Weyl's variational estimate bounds the top-three sum error by three times the norm remainder. All constants are uniform over \(t\in[0,1/4]\) and unit complex v.

By (9), the second-order coefficient of the top-three sum of H is at most \(-16(15/256)=-15/16\). Thus, with \(\epsilon_0=10^{-15}\),
\[
K_3(H_t(\epsilon))\le K_3(H_t(0))
-\left(\frac{15}{16}-3\cdot10^{12}\epsilon\right)\epsilon^2
\le K_3(H_t(0))-\frac{15}{32}\epsilon^2.\tag{13}
\]
Here \(3\cdot10^{12}\epsilon_0=0.003<15/32\). Scaling back gives the local original-output gap
\[
 R_3(p)-K_3(\Lambda_p(|\psi\rangle\langle\psi|))
 \ge\frac{15t\epsilon^2}{512}\quad
 (0<t\le1/4,\ 0\le\epsilon\le10^{-15}).\tag{14}
\]
The bound uses the actual top eigenspaces and allows arbitrary complex v; it does not assume product-only maximizers of an auxiliary frame.

## 5. All remaining pure states and all mixed states

Let \(r_1\le\cdots\le r_4\) be the actual pure input's local Bloch radii, \(S=\sum r_i^2\), \(L=r_1+r_2+3r_3+3r_4\), and \(\delta=8-L\). The common-P Pauli/HS derivation gives, for every actual rank3 P,
\[
16\left(R_3(p)-\operatorname{Tr}[P\Lambda_p(\rho)]\right)
\ge t[\delta-t(\sqrt{39(15-S)}-5)].\tag{15}
\]
To connect this to the product-overlap gauge, choose a dominant eigenvector of every local marginal. The four corresponding one-site projectors commute; their union bound gives
\[
1-m(\psi)\le\frac12\sum_i(1-r_i)\le\frac{8-L}{2}=\frac\delta2.\tag{16}
\]
If the local product gauge has \(\epsilon>10^{-15}\), then \(m<1/(1+10^{-30})\), so (16) yields \(\delta>10^{-30}\). Since \(\sqrt{39(15-S)}-5<20\), for \(0<t\le10^{-33}\) the right side of (15) is strictly positive. If \(\epsilon\le10^{-15}\), the local estimate (14) applies, with equality only at \(\epsilon=0\). Thus every pure input satisfies the original k3 inequality for \(0\le t\le10^{-33}\).

For an arbitrary density \(\rho=\sum_jw_j|\psi_j\rangle\langle\psi_j|\), apply the pure result to the SAME actual P in each term and use affinity of \(\Lambda_p\) and trace. Taking the maximum over rank-three P proves (1). At \(t=0\), every output is exactly \(I/16\). This is a uniform, all-density k3 interval only; nothing in the argument proves the original inequality outside it.

## 6. Provenance and verification boundary

The local 2/3/4-weight derivations, direct block perturbation argument, same-P far bound, and compact-free explicit overlap estimate are written above. No SZ/other outside theorem or historical scientific result is imported; ordinary finite-dimensional spectral/trace/commutator facts are used. The existing frame-saturation and pointwise-eigenvalue counterexamples remain consistent: the proof never assumes any individual excited eigenvalue is bounded by the reference, or that only product states saturate an auxiliary frame bound.

## 7. Exact finite and constant checks actually run

`frontier-20261028-57-product-hessian-exact.py`, SHA256 `647ca9ef45936094b0414d143a475fed4089dd263a3b32885221ff338d87c0ec`, ran under `python3 -B` from repo root, exit0. Exact Gaussian-rational arithmetic checked weight2, weight3, weight4 and mixed-weight formulas on 60 instances each at shrinkages `1/100,1/10,1/4,1/2,4/5`, including the conservative \(15t/256\) coefficient for the first three.

`frontier-20261028-58-uniform-noise-exact-check.py`, SHA256 `11860f6c7f5b875de1375d258e7d949e0561b907781c3a55b58a1b54129470b3`, ran under `python3 -B`, exit0. It checked the same formulas for selected complex rational directions at the exact extreme shrinkage \(10^{-33}\), at \(10^{-6}\), and at \(1/4\), and checked the rational coefficient/gap/remainder-budget inequalities used in (10)–(12). The extremal t was a Python `Fraction`, not a floating-point channel evaluation.

Native checker-pin clock **Wed Oct 28 18:29:41 PDT 2026**. These are bounded finite checks, not formal verification of the all-variable matrix proof. In particular, the global uniform interval in §1 is an AUTHOR CANDIDATE pending full disjoint written and independent numerical/algebraic review; no parent adoption or original all-p solution is claimed.
