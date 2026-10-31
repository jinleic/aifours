# Author candidate: phase-locked Dicke–cat–vacuum high-defect family

**Status:** Fresh written author candidate, not a parent disposition, independent review, formal proof, publication-priority claim, or global four-qubit theorem. The argument below is self-contained apart from elementary finite-dimensional linear algebra, the standard four-spin angular-momentum decomposition, and the definitions in the frozen packet. In particular, it does **not** import the missing body of the packet's linked invariant-sector theorem, the prior pure-region theorem, or any held episode. The packet's disposition S1 is used to identify the comparison regions and named prior classes, not as a load-bearing proof of the result below. Literature-wide novelty is not assessed.

## 1. Exact statement and domain

Put

\[
 D={1\over\sqrt6}\sum_{|x|=2}|x\rangle,\qquad
 y={|0000\rangle+|1111\rangle\over\sqrt2},\qquad v=|0000\rangle.
\]
For **every** real \(C,q\) and local unitary \(U=U_1\otimes U_2\otimes U_3\otimes U_4\) satisfying

\[
 {1\over6}\le C\le {1\over3},\qquad 0\le q\le {1\over8},\qquad U_i\in U(2),
\]
let

\[
 c=\sqrt{(1+C)/2},\quad s=\sqrt{(1-C)/2},\quad
 \psi=cD+i s y,\quad P=|v\rangle\langle v|,\quad
 \rho=U\bigl((1-q)|\psi\rangle\langle\psi|+qP\bigr)U^\dagger.
\]
Call these the **phase-locked Dicke–cat–vacuum densities**. For every physical \(p\in[0,4/3]\), set \(t=|1-p|\), \(b=(1-t)/2\), and

\[
 D_t=\operatorname{diag}((1+t)/2,(1-t)/2)^{\otimes4}.
\]
Then, for every rank \(k=1,\ldots,16\) and every complex Hermitian rank-\(k\) projector \(Q\) on the **actual** four-qubit Hilbert space,

\[
 \operatorname{Tr}\!\left[Q\,\Phi_p^{\otimes4}(\rho)\right]\le K_k(D_t),
 \qquad K_k(A)=\sum_{j=1}^k\lambda_j^{\downarrow}(A).
\]
The rank-16 prefix is equality. Hence the actual output spectrum is majorized by the product reference in **all sixteen prefixes**, including all boundaries. For \(0<t<1\), a stronger bound holds for \(1\le k\le11\):

\[
 \operatorname{Tr}[Q\,\Phi_p^{\otimes4}(\rho)]
 \le K_k(D_t)-(1-q)g_k t^2 b^2,\quad
 g_k=\begin{cases}3,&1\le k\le5,\\5,&6\le k\le11.\end{cases}
\]
For the nonpositive-retention interval only \(0<t\le1/3\) is physical; the same bound holds there by the full-transpose transport in §5.

Every member is non-spin-flip-invariant and genuinely four-party entangled. Its **actual** defect obeys the exact formula

\[
 d^2=q^2+(1-q)^2(1-C^2)\ge {401\over576}>{3\over13}.
\]
When \(q=0\), the state is pure with \(\eta=C^2\in[1/36,1/9]\), strictly below \(55/72\). When \(q>0\), it has rank two, so the packet's pure-input \(\eta\)-criterion is inapplicable, while the mixed defect criterion is violated. Thus the entire family is outside the two adopted defect regions, not just outside their numerical endpoints. Moreover §6 proves it lies outside a specified **larger hull** containing all four classes named in S1. These are sufficient, explicitly quantified results, not a statement that this parameter box is maximal or that other states fail.

## 2. Actual reduced states and the positive-retention expansion

It suffices initially to take \(U=I\). For a density \(X\), let

\[
 H_j(X)=\sum_{|S|=j}\operatorname{Tr}_{S^c}(X)\otimes I_{S^c},\qquad j=0,1,2,3,4,
\]
with factors restored to their original qubits; \(H_0(X)=I\), \(H_4(X)=X\). For \(0\le t\le1\), the actual channel is

\[
 \Phi_{1-t}^{\otimes4}(X)=\sum_{j=0}^4 t^j b^{4-j}H_j(X).
\]
Every term is the corresponding marginal of the **same** \(X\). For the product \(P\), each \(H_j(P)\) is diagonal: on a bit string of Hamming weight \(h\), its eigenvalue is \(\binom{4-h}{j}\), interpreted as zero when \(j>4-h\). All layers are coordered by increasing \(h\), so for every \(k\)

\[
 K_k(D_t)=\sum_{j=0}^4 t^j b^{4-j}K_k(H_j(P)). \tag{1}
\]
This is equality with the actual product reference, not a sum of incompatible optimizations.

Direct partial tracing gives, for every singleton, \(\psi_i=I/2\), and for every pair \(ij\), in the basis \(00,01,10,11\),

\[
 (\psi\psi^\dagger)_{ij}=
 \begin{pmatrix}a&0&0&0\\0&r&r&0\\0&r&r&0\\0&0&0&a\end{pmatrix},\quad
 a={c^2\over6}+{s^2\over2},\quad r={c^2\over3}. \tag{2}
\]
The reason the two-body cross term vanishes is explicit: \(\operatorname{Tr}_{\overline{ij}}|y\rangle\langle D|=(|00\rangle\langle11|+|11\rangle\langle00|)/\sqrt{12}\) is Hermitian, so the relative phase \(i\) cancels it against its adjoint. The singleton cross trace is zero. Consequently

\[
 H_1(\psi\psi^\dagger)=2I,\qquad
 H_2(\psi\psi^\dagger)=c^2H_2(DD^\dagger)+s^2H_2(yy^\dagger). \tag{3}
\]
Both are actual marginal identities, not independently chosen local data.

## 3. Independent exact \(H_2\) and \(H_3\) bounds

Write \(J_\alpha=\tfrac12\sum_i\sigma_\alpha^{(i)}\), \(J^2=J_x^2+J_y^2+J_z^2\). Directly from (2), or from the pair Pauli coefficients, one obtains

\[
 H_2(DD^\dagger)=I+{1\over3}J^2-{1\over2}J_z^2,\qquad
 H_2(yy^\dagger)=I+{1\over2}J_z^2. \tag{4}
\]
For four spins \(1/2\), pairwise addition gives \(2\cdot j=0\oplus3\cdot j=1\oplus1\cdot j=2\). The possible eigenvalues of the first operator are respectively

\[
 \begin{array}{c|c|c}
 j& m & 1+j(j+1)/3-m^2/2\\\hline
 0&0&1\\
 1&0,\ |m|=1&5/3,\ 7/6\\
 2&0,\ |m|=1,\ |m|=2&3,\ 5/2,\ 1
 \end{array}
\]
and those of the second are \(1+m^2/2\), with \(|m|\le2\). Hence, using (3),

\[
 I\le H_2(\psi\psi^\dagger)\le3I,\quad
 \operatorname{Tr}H_2(\psi\psi^\dagger)=24. \tag{5}
\]
The reference layer has spectrum \((6,3^{\times4},1^{\times6},0^{\times5})\). Its prefixes are \(3k+3\) for \(1\le k\le5\), \(k+13\) for \(6\le k\le11\), and 24 thereafter. From (5), its actual competitor satisfies \(K_k\le3k\), \(K_k\le k+8\) (subtract at least \(16-k\) from the trace), and \(K_k\le24\). Thus

\[
 H_2(\psi\psi^\dagger)\prec H_2(P),\quad
 K_k(H_2(P))-K_k(H_2(\psi\psi^\dagger))\ge g_k\quad(1\le k\le11). \tag{6}
\]
No invariant-sector theorem is used here.

For \(H_3\), let \(A_i=\psi_{\bar i}\otimes I_i\). Since \(\psi\) is pure and every singleton is \(I/2\), \(\operatorname{Tr}A_i^2=2\operatorname{Tr}\psi_i^2=1\). For \(i\ne j\), the partial-trace identity gives \(\operatorname{Tr}A_iA_j=\operatorname{Tr}\psi_{\overline{ij}}^2\). Formula (2) gives

\[
 \operatorname{Tr}\psi_{ij}^2=2a^2+4r^2
 ={1\over2}-{1-C^2\over6},\qquad
 \operatorname{Tr}H_3(\psi\psi^\dagger)^2=4+12\operatorname{Tr}\psi_{ij}^2=8+2C^2\le10. \tag{7}
\]
Each \(A_i\) is positive and at most \(I\), and \(\operatorname{Tr}H_3=8\). The product layer has spectrum \((4,1^{\times4},0^{\times11})\). Its first four prefixes are 4,5,6,7 and all later ones are 8. For the actual \(H_3\), the first prefix is at most 4, while Cauchy–Schwarz and (7) give

\[
 K_2\le\sqrt{20}<5,\quad K_3\le\sqrt{30}<6,\quad K_4\le\sqrt{40}<7;
\]
all later prefixes are at most its trace 8. Therefore

\[
 H_3(\psi\psi^\dagger)\prec H_3(P). \tag{8}
\]
Finally \(H_1(\psi\psi^\dagger)=2I\prec H_1(P)\), since the latter has the same trace 32, and \(H_4(\psi\psi^\dagger)\) and \(H_4(P)\) are both rank-one densities. The \(H_0\) layers coincide.

## 4. One physical complex projector, not separate marginal optimizers

Let \(X=(1-q)\psi\psi^\dagger+qP\) and fix **one arbitrary** complex rank-\(k\) projector \(Q\). Linearity of physical partial traces gives \(H_j(X)=(1-q)H_j(\psi\psi^\dagger)+qH_j(P)\). Applying the variational bound to this very \(Q\), (6), (8), and the remaining layer bounds yields

\[
 \operatorname{Tr}[QH_j(X)]\le K_k(H_j(P))\quad(j=0,1,2,3,4),
\]
and for \(j=2\), \(k\le11\), the right side improves by \((1-q)g_k\). Multiply by the nonnegative actual channel coefficients and use (1). This proves the stated all-prefix inequality and gap for \(0\le t\le1\). No projector, input, or set of marginals is substituted between the layers. The individual uses of \(K_k\) are upper bounds for the same \(Q\), not a claim that different optimizing projectors coincide; coordering is invoked only for the actual product reference.

For arbitrary \(U\), local-unitary covariance of each depolarizing factor gives \(\Phi_p^{\otimes4}(UXU^\dagger)=U\Phi_p^{\otimes4}(X)U^\dagger\); apply the proven bound to the same transported physical projector \(U^\dagger Q U\). This establishes the entire local-unitary family.

## 5. Negative retention and endpoints

Let \(Y_4=Y^{\otimes4}\). The one-qubit identity \(Y A^T Y=(\operatorname{Tr}A)I-A\) gives, for \(t\ge0\),

\[
 \Phi_{1+t}^{\otimes4}(X)=Y_4\bigl(\Phi_{1-t}^{\otimes4}(X)\bigr)^T Y_4.
\]
Here \(T\) is the **full four-qubit transpose**. Thus

\[
 \operatorname{Tr}[Q\Phi_{1+t}^{\otimes4}(X)]
 =\operatorname{Tr}[(Y_4Q^TY_4)\Phi_{1-t}^{\otimes4}(X)],
\]
where \(Y_4Q^TY_4\) is one physical complex rank-\(k\) projector. Use that same transported projector for the whole mixture and all its layers. Physical negative retention is exactly \(p\in[1,4/3]\), so \(t\le1/3\); the positive-retention comparison uses \(1-t\in[2/3,1]\).

At \(p=0\), \(b=0\) and the bound reduces to that of a density against a rank-one reference. At \(p=1\), \(t=0\), the actual output and reference are both \(I/16\). At \(p=4/3\), \(t=1/3\) and the full-transpose proof applies, with the displayed strictly positive gap for ranks 1–11. The parameter endpoints \(C=1/6,1/3\) and \(q=0,1/8\) were not excluded in any inequality.

## 6. Exact high defect, genuine entanglement, and separation from the named older hull

Set \(z=(|0000\rangle-|1111\rangle)/\sqrt2\). Under the four-qubit spin flip, \(D,y\) are fixed and \(z\) changes sign. In the orthonormal basis \((D,y,z)\), the actual \(\Delta=X-(X+\widetilde X)/2\) is

\[
 \begin{pmatrix}
 0&-i(1-q)cs&0\\ i(1-q)cs&0&q/2\\0&q/2&0
 \end{pmatrix},
\]
with zero on its orthogonal complement. Its nonzero eigenvalues are \(\pm\sqrt{(1-q)^2c^2s^2+q^2/4}\), so \(d^2=\|\Delta\|_1^2=q^2+(1-q)^2(1-C^2)\). Since \(1-C^2\ge8/9\) and \(q^2+(1-q)^2(8/9)\) decreases throughout \([0,1/8]\), the exact uniform minimum is \(1/64+(49/64)(8/9)=401/576\). For \(q=0\), \(\langle\psi|\Theta_4\psi\rangle=C\), so \(\eta=C^2\). Local unitaries preserve these values: \(Y U_i^*Y\) is \(U_i\) times a phase, which cancels for density matrices.

The stronger hull separation is as follows. Define \(\mathcal H\) as the convex hull of **all** pure biseparable four-qubit states, **all** pure states with \(\eta=0\), and **all** pure states with \(\eta=1\). This enlarged hull contains S1's named biseparable, eta-zero coherent-vacuum–W4-orbit, and eta-one invariant/Dicke-orbit classes. It also contains every spin-flip-invariant mixed state: in a basis fixed by the antiunitary involution \(\Theta_4\), its density matrix is real symmetric and has a real orthonormal eigenbasis, hence a convex decomposition into eta-one pure states.

For \(U=I\), put \(W=\operatorname{span}_{\mathbb C}\{\psi,v\}\). Any vector \(a\psi+bv\in W\) with \(a\ne0\) is entangled across **each** bipartition. Indeed, for a 1|3 cut its two rows have disjoint weight supports \(\{0,2\}\) and \(\{1,3\}\), each nonzero because of the \(a cD\) term. For a 2|2 cut, the coefficient matrix has a nonzero block on rows/columns \(01,10\), and a separate block on rows/columns \(00,11\) whose off-diagonal entries are \(ac/\sqrt6\); its rank is at least two. Permutation symmetry covers all seven cuts. Thus the only biseparable ray in \(W\) is \(v\).

The remaining eligible rays in \(W\) can also be determined exactly. Up to scalar, the only eta-one ray with \(a\ne0\) is

\[
 x_I=\psi-i\sqrt2\,s\,v,
\]
by the equality case of Cauchy–Schwarz for \(|\langle x|\Theta_4x\rangle|=\|x\|^2\). The only eta-zero ray with \(a\ne0\) is

\[
 x_N=\psi+i{C\over\sqrt2s}\,v,
\]
because, with \(F=Y^{\otimes4}\),
\[
 (a\psi+bv)^T F(a\psi+bv)=a^2C+i\sqrt2\,ab s. \tag{9}
\]
The ray \(v\) itself has eta zero. These formulas are nondegenerate throughout the stated closed parameter range.

Suppose for contradiction that \(X\in\mathcal H\). Positivity implies that every pure constituent of any such decomposition lies in \(\operatorname{range}X\subseteq W\). Write its resulting coordinate matrix in the linearly independent (not necessarily orthogonal) basis \((\psi,v)\). For nonnegative \(\alpha,\beta,\gamma\), it must have the form

\[
 \alpha|x_I\rangle\langle x_I|+\beta|x_N\rangle\langle x_N|+\gamma|v\rangle\langle v|,
\]
where normalization factors have been absorbed into the coefficients. Coordinate comparison with \((1-q)|\psi\rangle\langle\psi|+q|v\rangle\langle v|\) yields

\[
 \alpha+\beta=1-q,\qquad
 \alpha\sqrt2s=\beta {C\over\sqrt2s},\qquad
 q=\alpha(2s^2)+\beta {C^2\over2s^2}+\gamma
 =(1-q)C+\gamma. \tag{10}
\]
But \(q/(1-q)\le1/7<1/6\le C\), a contradiction. This also covers \(q=0\), when \(\operatorname{range}X\) is one-dimensional. Hence every member is outside \(\mathcal H\), and in particular is genuinely four-party entangled, since every biseparable density belongs to \(\mathcal H\). Local unitaries preserve all three defining classes of \(\mathcal H\), so the conclusion persists for arbitrary \(U\).

An exact anchor is \(C=1/3\), \(q=1/8\), \(U=I\): \(\psi=\sqrt{2/3}D+i\sqrt{1/3}y\), its pure-component eta is \(1/9\), and the actual mixed density has \(d^2=401/576\). This is an identity within the proved family, not a numerical sample used as a universal argument.

## 7. Scope, imports, and process declaration

* The theorem is for the stated density family, all local unitaries, every physical \(p\), and every actual complex rank-\(k\) projector. It establishes no majorization theorem for arbitrary high-defect four-qubit states and no optimality or no-go result outside the box. The gap is a sufficient lower bound, not claimed sharp. No source equivalence, global/blocklength result, literature priority, human/family review, or formal-kernel acceptance is claimed.
* No unavailable mathematical source body is used as a load-bearing import. The source S1's comparison labels and thresholds are the only prior-result references; its linked proof/review/checker bodies were not opened and are not silently imported. If a later report wishes to claim the old classes actually have the channel property, that is a separate conditional historical import, not needed for this proof or the hull-separation calculation.
* Before any mathematical body or reasoning I read the manifest, freeze receipt, final binding, parent-live metadata, actual-dispatch receipt, and all 22 manifest-listed controls as status/permissions only. I wrote `prebody-ack-v1.md` and directly delivered the required ACK to Main before opening the body. The initial non-raw administrative displays elided JSON blocks; complete raw administrative rereads recovered those blocks. The separately read general memory-summary display clipped long lines; it was not a mathematical or load-bearing input. The written-math skill was read as procedural context.
* The **entire single literal part**, including its ending, was then read in order in raw windows 1–20, 21–40, and 41–53. The supplied part metadata records 9,698 bytes total, so each window is below 30,000 bytes; no packet clipping was displayed. The packet reports complete S1 LF 1–47 and terminal LF. Parent metadata supplies part SHA-256 `920c924e8865fb9d7b5230517d3e7800bd08e951c8db474a92e6986e107512a3` and S1 SHA-256 `4d9f3d97723cafe956eaf7c151506249e08c246bb35b59436fe64b015558eaff`; these are supplied pins, not independently recomputed hashes.
* All genuine held episodes and all their method/selection/proof/planning/verification/reporting/confidence/downstream consumers remained NONINPUT. No source link was followed, scientific program or child subprocess executed, external model/network used, test/build performed, or verifier source prepared. Accordingly there is no prepared-code hash and no computational verification claim. Independent reconstruction and parent disposition remain separate.
