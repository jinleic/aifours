# Actual d=4 Werner rank-two frontier: a CORE-GRAM counterexample and paid open regions

**Status: AUTHOR CANDIDATE, written argument only, not independently reviewed or parent-disposed.** The counterexample below is to the proposed sufficient CORE-GRAM premise on an actual pair of doubly orthonormal singular frames. It is **not** a counterexample to the original Werner two-copy inequality. I also give two independently stated sufficient regions, an exact residual equivalent to the original rank-two dual question, and an explicit irreducible physical pair in one region. No novelty, kernel, human, independent-family, or acceptance claim is made.

## 1. Scope, notation and imported facts

All spaces and matrices are complex. Let \(H=\mathbb C^4\otimes\mathbb C^4\), and put
\[
 F(R)=\bigl((\operatorname{Tr}_B R)_0,(\operatorname{Tr}_A R)_0\bigr),\quad
 q(R)=\|F(R)\|_F^2
 =\|\operatorname{Tr}_B R\|_F^2+\|\operatorname{Tr}_A R\|_F^2-\tfrac12|\operatorname{Tr}R|^2.
\]
The subscript 0 subtracts \(\operatorname{Tr}(R)I_4/4\). Inner products are conjugate-linear in the first entry. The original dual target is \(q(R)\le 2\|R\|_F^2\) for every \(R\) of rank at most two. From clean packet S1, uniformly over all such \(R\), this is equivalent to the original physical statement \(S_2(A\otimes I+I\otimes B)\le 2L\) for all traceless complex \(4\times4\) matrices \(A,B\), where \(L=\|A\|_F^2+\|B\|_F^2\). This is a **double-universal** equivalence, not a fixed-pair equivalence.

Take an actual doubly orthonormal frame: \(\langle u_i,u_j\rangle=\langle v_i,v_j\rangle=\delta_{ij}\), and set
\[
 x_i=|u_i\rangle\langle v_i|,\quad c_i=\operatorname{Tr}x_i=\langle v_i,u_i\rangle,\quad
 C_{12}=\langle\operatorname{Tr}_B x_1,\operatorname{Tr}_B x_2\rangle+
 \langle\operatorname{Tr}_A x_1,\operatorname{Tr}_A x_2\rangle,
\]
\[
 4p_i=1+|c_i|^2-\|\operatorname{Tr}_B x_i\|_F^2-\|\operatorname{Tr}_A x_i\|_F^2.
\]
These definitions fix all complex conjugations. The rank-one swap identity imported from S1 gives \(p_i\ge0\): its right side is the expectation of \((I-F_A)(I-F_B)\) in \(u_i\otimes v_i\), and the commuting swap factors are positive semidefinite. Consequently \(q(x_i)=1+|c_i|^2/2-4p_i\le3/2\). Define
\[
 G(R)=\|R\|_F^2+|\operatorname{Tr}R|^2-\|\operatorname{Tr}_B R\|_F^2-\|\operatorname{Tr}_A R\|_F^2.
\]
Thus \(q(R)=\|R\|_F^2+|\operatorname{Tr}R|^2/2-G(R)\). For \(R=z_1x_1+z_2x_2\), frame orthogonality gives
\[
 G(R)=4p_1|z_1|^2+4p_2|z_2|^2+2\operatorname{Re}\!\left[\overline{z_1}z_2(\overline{c_1}c_2-C_{12})\right].\tag{1}
\]
For the real example below, \(\overline{c_1}c_2=c_1\overline{c_2}\), so it also directly matches the S1 displayed convention. CORE-GRAM asks that the mixed term be bounded below by \(-4\sqrt{p_1p_2}\) for every actual frame; its phase-uniform form is equivalent to positive semidefiniteness of the \(2\times2\) Gram matrix of \(G\). S1 asserts only the conditional implication CORE-GRAM \(\Rightarrow\) Q \(\Rightarrow\) T2, not the converse.

## 2. Exact counterexample with both \(p_i>0\)

Use computational kets \(|ij\rangle\), with indices \(0,1,2,3\). Let
\[
 |a\rangle=(4|00\rangle+2|11\rangle+2|22\rangle+|33\rangle)/5,
\]
\[
 u_1=|01\rangle,\qquad v_1=-(6|01\rangle+8|02\rangle+|10\rangle)/\sqrt{101},\qquad u_2=v_2=a.
\]
Each vector has norm one; \(u_1\perp u_2\) and \(v_1\perp v_2\). This is an actual singular frame, not an auxiliary relaxation. Put \(\rho=\operatorname{diag}(16,4,4,1)/25\), and let \(E_{ij}=|i\rangle\langle j|\) on a local four-dimensional space. Direct partial traces are
\[
 \operatorname{Tr}_B x_1=-6E_{00}/\sqrt{101},\quad
 \operatorname{Tr}_A x_1=-(6E_{11}+8E_{12})/\sqrt{101},\quad
 \operatorname{Tr}_B x_2=\operatorname{Tr}_A x_2=\rho.
\]
Moreover \(c_1=-6/\sqrt{101}\), \(c_2=1\), \(\operatorname{Tr}\rho^2=289/625\), and
\[
 4p_1=1/101,\quad 4p_2=672/625,\quad C_{12}=-24/(5\sqrt{101}),\quad
 \overline{c_1}c_2-C_{12}=-6/(5\sqrt{101}).
\]
Hence both \(p_1=1/404\) and \(p_2=168/625\) are strictly positive, but
\[
 -\frac{6}{5\sqrt{101}}< -\frac{4\sqrt{42}}{25\sqrt{101}}
 =-4\sqrt{p_1p_2},
\]
since \(30>4\sqrt{42}\), equivalently \(900>672\). Thus the proposed CORE-GRAM inequality is **false even on actual d=4 frames with both diagonal gaps strictly positive**. No physical conclusion follows solely from this failure.

Make the corresponding rank-two operator completely explicit:
\[
 R=x_1+\frac{x_2}{\sqrt{101}}
 =\frac1{\sqrt{101}}\left(|a\rangle\langle a|-6|01\rangle\langle01|-8|01\rangle\langle02|-|01\rangle\langle10|\right).\tag{2}
\]
The first displayed SVD has singular values \(1,1/\sqrt{101}\); the two frames were checked above. Equivalently, the full \(16\times16\) matrix is specified by (2), where \(|a\rangle\langle a|=(1/25)\sum_{i,j=0}^3 b_i b_j|ii\rangle\langle jj|\) with \(b=(4,2,2,1)\). In particular,
\[
 \|R\|_F^2=102/101,\quad \operatorname{Tr}R=-5/\sqrt{101},
\]
\[
 \|\operatorname{Tr}_B R\|_F^2=17989/63125,\quad
 \|\operatorname{Tr}_A R\|_F^2=61589/63125,
\]
\[
 G(R)=-203/63125<0,\qquad q(R)=143531/126250<255000/126250=2\|R\|_F^2.\tag{3}
\]
For example, the first marginal is \(\operatorname{diag}(-134,4,4,1)/(25\sqrt{101})\), and the second is \([\operatorname{diag}(16,-146,4,1)-200E_{12}]/(25\sqrt{101})\). These display exactly how (3) is obtained. The frame-failure and \(G(R)<0\) are genuine; the actual \(q\)-inequality holds with a large strict margin. Thus neither (2) nor anything here refutes Q or T2.

This witness is not among the clean packet's named easy dual classes: its trace is nonzero; its range is \(\operatorname{span}\{|01\rangle,a\}\), whereas its adjoint range is \(\operatorname{span}\{v_1,a\}\), so it is not EP; and \(C_{12}\ne0\). Since the range contains \(a\), whose Schmidt rank is four, each common local support has dimension four. These statements concern this actual \(R\), not a projection of it.

The failure is not confined to a zero-gap boundary. The strict inequality and \(p_i>0\) persist on an open neighborhood in the product of two complex Stiefel manifolds. In fact, set
\[
 w=(|00\rangle+|11\rangle+|22\rangle-8|33\rangle)/\sqrt{67},\quad
 u_1(\epsilon)=\frac{u_1+\epsilon w}{\sqrt{1+\epsilon^2}},\quad
 v_1(\epsilon)=\frac{v_1+\epsilon w}{\sqrt{1+\epsilon^2}},
\]
with real \(\epsilon\), and keep \(u_2=v_2=a\). All required orthogonality is exact because \(w\perp a,u_1,v_1\). For sufficiently small nonzero \(\epsilon\), both first vectors also have Schmidt rank four: the determinant of the coefficient matrix of \(u_1(\epsilon)\) is nonzero, and for \(v_1(\epsilon)\) it is a nonzero multiple of \(\epsilon^2(\epsilon^2/67-6/101)\). Continuity preserves the strict CORE-GRAM failure, positive \(p_i\), the nonzero trace for the weights in (2), and the strict Q margin. The two fixed second vectors already have full Schmidt rank; consequently full-Schmidt-frame examples form a nonempty open set. This is a written existence argument, not a numerical experiment or a claimed physical counterexample.

## 3. An actual-frame uniform Q region, and the exact remaining frame inequality

For any actual doubly orthonormal frame, write \(q_i=q(x_i)\), \(h=\langle F(x_1),F(x_2)\rangle=C_{12}-\tfrac12\overline{c_1}c_2\), and \(\alpha_i=2-q_i=1-|c_i|^2/2+4p_i\). The rank-one swap bound gives \(q_i\le3/2\), hence \(\alpha_i\ge1/2\). For **every complex** \(z_1,z_2\),
\[
 q(z_1x_1+z_2x_2)\le (|z_1|\sqrt{q_1}+|z_2|\sqrt{q_2})^2
 \le(q_1+q_2)(|z_1|^2+|z_2|^2).\tag{4}
\]
The first inequality is the triangle inequality in the direct-sum Hilbert space of traceless marginals; the second is Cauchy–Schwarz, and the last sum is exactly \(\|z_1x_1+z_2x_2\|_F^2\). Therefore **if \(q_1+q_2\le2\), Q holds on the entire actual two-dimensional span**, for arbitrary complex coefficients, including all singular-value ratios and phases. In invariant frame data this sufficient criterion reads
\[
 4(p_1+p_2)\ge\tfrac12(|c_1|^2+|c_2|^2).\tag{5}
\]
For the frame in Section 2,
\[
 q_1=118/101,\quad q_2=531/1250,\quad q_1+q_2=201131/126250<2,\quad h=-9/(5\sqrt{101}).
\]
Thus this uniformly paid actual-frame region includes (2), including its nonzero trace, non-EP, nonzero cross term, and full common local supports, and includes nearby frames by strictness. In this precise sense its **union** with the packet's already paid dual classes strictly extends those classes. It is not asserted that (5) individually contains all previously paid classes. The separately-2+2 result in S3 is instead a class of physical pairs, so it cannot literally be compared by set inclusion to a class of \(R\)'s.

A second, coefficient-dependent consequence of (4) is that Q holds whenever the actual SVD weights \(s_1\ge s_2\ge0\) obey
\[
 (s_1\sqrt{q_1}+s_2\sqrt{q_2})^2\le2(s_1^2+s_2^2).
\]
In particular the frame-independent sufficient ratio \(s_2/s_1\le3-2\sqrt2\) follows from \(q_i\le3/2\); the zero-operator and rank-one boundaries are immediate. This ratio is only sufficient and does not replace the original target.

There is also an exact, not merely sufficient, frame residual. The Hermitian matrix of \(q\) on the actual span is \(\begin{pmatrix}q_1&h\\\bar h&q_2\end{pmatrix}\). Since \(\alpha_i>0\), Q holds for **all** complex coefficients in this frame exactly when
\[
 |C_{12}-\tfrac12\overline{c_1}c_2|^2\le
 \left(1-\tfrac12|c_1|^2+4p_1\right)
 \left(1-\tfrac12|c_2|^2+4p_2\right).\tag{6}
\]
Because every rank-at-most-two operator has such an SVD, (6) for every actual frame is equivalent to the original Q, and, via the S1 imported double-universal equivalence, to the original T2. Inequality (4) pays all frames with \(q_1+q_2\le2\); the exact unpaid step is (6) on the remaining actual frames \(q_1+q_2>2\). By contrast, the CORE-GRAM condition is a different, now-refuted sufficient condition.

For Section 2's frame the determinant in (6) is explicitly positive:
\[
 \alpha_1\alpha_2-|h|^2
 =\frac{84}{101}\frac{1969}{1250}-\frac{81}{2525}
 =\frac{80673}{63125}>0.
\]
This is another exact confirmation that the entire complex span obeys Q despite failing CORE-GRAM.

If a future actual frame strictly violates (6), this is not merely an auxiliary warning: set \(z_1=h\), \(z_2=\alpha_1\), and \(R=z_1x_1+z_2x_2\). Then
\[
 2\|R\|_F^2-q(R)=\alpha_1(\alpha_1\alpha_2-|h|^2)<0.
\]
The rank is two because \(h\ne0\) and \(\alpha_1>0\). Moreover the actual traceless physical matrices
\(A=(\operatorname{Tr}_B R)_0\), \(B=(\operatorname{Tr}_A R)_0\) have \(L=q(R)>0\) and \(\langle R,A\otimes I+I\otimes B\rangle=q(R)\). Rank-two Ky Fan duality gives \(S_2(X)\ge q(R)^2/\|R\|_F^2>2L\). Thus an exact violation of (6), accompanied by the frame and these matrices, would refute T2. No such violation is claimed here.

## 4. A separate open physical-pair region beyond separately 2+2

For traceless \(A,B\), put \(X=A\otimes I+I\otimes B\) and let \(\sigma_1\ge\sigma_2\ge\cdots\) be its singular values. The rank-one dual and the swap bound yield
\[
 \sigma_1^2\le\tfrac32 L.\tag{7}
\]
Indeed, for a normalized leading singular dyad \(x=|u\rangle\langle v|\), \(\sigma_1^2=|\langle x,X\rangle|^2\le Lq(x)\le3L/2\). Hence, if \(X\ne0\) and
\[
 \sigma_2/\sigma_1\le1/\sqrt3,\tag{8}
\]
then \(S_2(X)\le(1+1/3)\sigma_1^2\le2L\). Equality and zero boundaries are included. This is a sufficient physical-pair condition, not a global proof; strict inequality in (8) gives a genuine open region.

The region is not contained in S3's separately 2+2-reducing pair class. Let
\[
 D=\operatorname{diag}(3,-1,-1,-1),\quad N=E_{01}+E_{12}+E_{23},\quad A=B=M=D+N/10.
\]
Both are traceless. For \(X_0=D\otimes I+I\otimes D\), the singular values are 6 once and 2 fifteen times. Since \(\|N\|_{\rm op}=1\), \(\|X-X_0\|_{\rm op}\le1/5\). The singular-value perturbation inequality gives \(\sigma_1(X)\ge29/5\) and \(\sigma_2(X)\le11/5\), so \(\sigma_2/\sigma_1\le11/29<1/\sqrt3\). In fact \(S_2(X)\le(1443/841)L<2L\); here \(L=1203/50\).

Each \(M\) is unitarily irreducible. To see this directly, the 3-eigenspace of \(M\) is \(\operatorname{span}\{e_0\}\). If an orthogonal projection \(P\) commutes with \(M\), then \(Pe_0\) is either \(0\) or \(e_0\); since \(P\) is Hermitian it also commutes with \(M^\dagger\). The cyclic chain
\((M^\dagger-3I)e_0=e_1/10\), \((M^\dagger+I)e_1=e_2/10\), \((M^\dagger+I)e_2=e_3/10\)
forces respectively \(P=0\) or \(P=I\). Thus no 2+2 reducing decomposition exists. Also \(M^2\) is upper triangular with nonzero \((0,1)\) entry \(1/5\), hence is nonnormal (a normal upper-triangular matrix is diagonal). Both squared matrices are nonnormal. Strict singular-gap and irreducibility persist under sufficiently small traceless perturbations: for irreducibility, injectivity of \(T\mapsto[T,M]\) on the compact unit sphere of traceless Hermitian \(T\) is an open condition. Consequently the union of (8)'s physical class with the separately-2+2 class is strictly larger, and the added portion includes an open set of pairs with both squares nonnormal. No claim is made that this example lies outside every other independently known physical class, or that this observation is novel.

## 5. Provenance, methods and unpaid frontier

- Chronology: before any mathematical derivation I read the complete assigned manifest and freeze receipt, all parent predispatch metadata and the actual dispatch receipt, and all 15 supplied status-only controls through their endings. I sent a direct pre-body ACK to Main, then read the entire 81-LF literal packet in ordered raw windows of at most 20 LF, including its last line. Only after that did I derive the mathematics above. The native clock observed before composing this record was 2026-10-30T15:10:42-0700 PDT; it is not a claim about private thought timing.
- Clean packet imports: S1 rank-two dual equivalence and rank-one swap identity, S2 transpose qualification before S3, S3 separately-2+2 physical class, and S4 common-local-qubit support class. Parent metadata reports the packet SHA-256 as `acb4e7028f4d4daed28fc6ba210cc3592f50118d3bb3b85d5f2b993b114ab15c`; manifest and freeze pins are those assigned in the dispatch. This is parent-reported metadata, not a new child hash check. All held episodes and all their consumers remain NONINPUT. No public source or sibling science was read.
- Child scientific execution: **NOT RUN**. All formulas, examples, norm values, determinants, and proofs above are written derivations; no CAS, source execution, solver, or numerical sampling was used. No bounded source is proposed or silently treated as run. Prospective independent checking must review the actual complete body and exact calculations, followed by parent disposition; none has occurred in this record.
- Unpaid: (6) on all remaining actual doubly orthonormal frames; unrestricted Q/T2; q3/T3 and any global/distillability claim; publication/priority/novelty; independent-family, human and kernel checks. The strict CORE-GRAM failure is not a T2 failure, and the open physical region is not a proof of T2 for every pair. S4 projector conclusions have their own stated hypotheses; the physical example is not claimed to evade every such condition.
