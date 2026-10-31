# Author candidate: exact defect and enlarged-hull separation for a physical four-qubit family

**Status and scope.** This is a fresh, written GENERAL AUTHOR candidate, not a parent disposition, independent review, family/human acceptance, or formal-kernel proof. The defect, range and hull arguments below are self-contained finite-dimensional calculations. The packet's f852 candidate contains additional channel-majorization claims; I do not independently establish those claims here. The old-region labels and named classes used for comparison are those stated in the packet. No global entanglement classification, global channel theorem, literature novelty, or priority is claimed.

## 1. Objects and exact claims

Let
\[
 D=\frac1{\sqrt6}\sum_{|x|=2}|x\rangle,\quad
 y=\frac{|0000\rangle+|1111\rangle}{\sqrt2},\quad
 z=\frac{|0000\rangle-|1111\rangle}{\sqrt2},\quad v=|0000\rangle.
\]
For every real \(C\in[1/6,1/3]\), put
\[
 c=\sqrt{\frac{1+C}{2}},\quad s=\sqrt{\frac{1-C}{2}},\quad
 |\psi\rangle=cD+is y,\quad P=|v\rangle\langle v|,
\]
and for every \(q\in[0,1]\) define
\[
 X_q=(1-q)|\psi\rangle\langle\psi|+qP,\qquad
 \rho_{q,U}=UX_qU^\dagger,\quad U=U_1\otimes U_2\otimes U_3\otimes U_4,\quad U_i\in U(2).
\]
The required original parameter box is \(0\le q\le1/8\); the algebraic conclusions below are in fact given for the larger interval \(0\le q\le1\), except where the box is explicitly required. Here \(D,y,z\) are orthonormal, \(c,s>0\), \(c^2+s^2=1\), \(c^2-s^2=C\), and \(v=(y+z)/\sqrt2\). In particular \(\psi\) and \(v\) are unit but **not orthogonal**:
\[
 \langle\psi|v\rangle=-\frac{is}{\sqrt2},\qquad
 |\langle\psi|v\rangle|^2=\frac{1-C}{4}.
\]
Let \(F=Y^{\otimes4}\), \(\Theta=FK\), where \(K\) is computational-basis conjugation, and let
\[
 \widetilde R=F R^T F,\qquad \Delta(R)=\frac{R-\widetilde R}{2},\qquad
 d(R)=\|\Delta(R)\|_1.
\]
For a nonzero pure vector \(w\), define the scale-independent quantity
\[
 \eta(w)=\frac{|\langle w|\Theta w\rangle|^2}{\langle w|w\rangle^2}
 =\frac{|w^TFw|^2}{\|w\|^4}.
\]
Let \(\mathcal H\) be the convex hull of **all** normalized pure states that are biseparable across at least one of the seven physical cuts, or have \(\eta=0\), or have \(\eta=1\). Then, for every \(C\in[1/6,1/3]\), \(q\in[0,1]\), and \(U_i\in U(2)\):

1. The spectrum of \(\Delta(\rho_{q,U})\) is \(\{r,-r,0^{\times14}\}\), where
   \[
   r=\frac12\sqrt{q^2+(1-q)^2(1-C^2)},\qquad
   d(\rho_{q,U})^2=q^2+(1-q)^2(1-C^2).
   \]
   It is nonzero throughout the stated domain. On the original box the exact uniform minimum is \(401/576\), attained at \(C=1/3,q=1/8\), independently of \(U\). For \(q=0\), \(\eta(\psi)=C^2\in[1/36,1/9]\).
2. \(\rho_{q,U}\) is genuinely four-partite entangled for every \(0\le q<1\), in the mixed-state sense of not being a convex mixture of pure states separable across varying cuts. At \(q=1\) it is fully separable.
3. The enlarged hull has the exact intersection criterion
   \[
   \rho_{q,U}\in\mathcal H\quad\Longleftrightarrow\quad
   q\ge(1-q)C\quad\Longleftrightarrow\quad q\ge\frac{C}{1+C}.
   \tag{A}
   \]
   Thus the entire original box lies outside \(\mathcal H\), since \(q/(1-q)\le1/7<1/6\le C\). The endpoint inequality is included in (A). In particular, the mixed states with \(0<q\le1/8\) are genuinely entangled and outside this enlarged hull, not merely outside a collection of pure rays.

The boxed-domain minimum exceeds the packet's mixed-region bound \(3/13\). At \(q=0\), the pure-region parameter is below the packet's \(55/72\); at \(0<q\le1/8\) the input is rank two and that pure-state criterion is not applicable. These are comparisons with the specified sufficient regions, not claims that failure of a sufficient condition disproves any channel property.

## 2. Antiunitary phases, defect spectrum, and rank

Since \(Y|0\rangle=i|1\rangle\), \(Y|1\rangle=-i|0\rangle\),
\[
 F|x\rangle=(-1)^{|x|}|\bar x\rangle.
\]
Consequently \(\Theta D=D\), \(\Theta y=y\), and \(\Theta z=-z\). Also \(F^*=F\), \(F^2=I\), so \(\Theta^2=I\). Complex conjugation changes the \(i\) in \(\psi\), hence
\[
 \Theta\psi=cD-is y,\quad \Theta v=(y-z)/\sqrt2,
 \quad \langle\psi|\Theta\psi\rangle=c^2-s^2=C.
\]
The last identity is real in this displayed phase convention, although its modulus is the invariant assertion.

In the **orthonormal** physical basis \((D,y,z)\), with zero action on its orthogonal complement, the actual difference \(\Delta(X_q)\) is
\[
 \begin{pmatrix}
 0&-i(1-q)cs&0\\
 i(1-q)cs&0&q/2\\
 0&q/2&0
 \end{pmatrix}.
 \tag{1}
\]
For example, the \(q/2\) entries come from \((P-\widetilde P)/2\); the \(-i(1-q)cs\) entry comes from \((|\psi\rangle\langle\psi|-|\Theta\psi\rangle\langle\Theta\psi|)/2\). The characteristic polynomial of (1) is
\[
 \lambda\bigl(\lambda^2-[(1-q)^2c^2s^2+q^2/4]\bigr).
\]
Thus the sixteen eigenvalues and trace norm are exactly those in Claim 1, because \(4c^2s^2=1-C^2\). There are fourteen zero eigenvalues, including the third zero in (1). At \(q=0\) the nonzero pair is \(\pm cs\); at \(q=1\) it is \(\pm1/2\).

For the minimum, \(1-C^2\ge8/9\), with equality exactly at \(C=1/3\). For every \(q\in[0,1/8]\),
\[
 \partial_q\{q^2+(1-q)^2(1-C^2)\}
 =2[q-(1-q)(1-C^2)]
 \le 2(1/8-7/9)<0.
\]
Therefore the minimum over the box occurs at \(q=1/8,C=1/3\), and equals
\[
 \frac1{64}+\frac{49}{64}\frac89=\frac{401}{576}>\frac3{13}.
\]

For the rank boundary, \(\psi,v\) are linearly independent because the \(D\)-coefficient of \(\psi\) is nonzero. The Gram determinant is
\[
 1-|\langle\psi|v\rangle|^2=\frac{3+C}{4}>0.
\]
The two possibly nonzero eigenvalues of \(X_q\) are
\[
 \lambda_\pm(X_q)=\frac{1\pm\sqrt{1-q(1-q)(3+C)}}2.
 \tag{2}
\]
Indeed the trace is one and their product is \(q(1-q)(3+C)/4\). Accordingly \(X_q\) has rank two exactly when \(0<q<1\), and rank one at \(q=0\) and \(q=1\). Its actual range is \(W=\operatorname{span}_{\mathbb C}\{\psi,v\}\) for \(0<q<1\), \(\mathbb C\psi\) at \(q=0\), and \(\mathbb Cv\) at \(q=1\).

For each \(U_i\in U(2)\), the explicit identity
\[
 YU_i^*Y=(\det U_i)^*U_i
\]
gives, with \(\delta=\prod_i\det U_i\),
\[
 \Theta U=\delta^*U\Theta,\qquad
 \widetilde{(URU^\dagger)}=U\widetilde R U^\dagger.
 \tag{3}
\]
Thus \(\Delta(URU^\dagger)=U\Delta(R)U^\dagger\), and \(\eta(Uw)=\eta(w)\). The phase in (3) cancels for densities; it is not necessary or generally correct to assert \(\Theta U=U\Theta\) without that phase.

## 3. Every range vector on all seven physical bipartitions

Fix \(w=a\psi+bv\in W\), with \(a,b\in\mathbb C\). We prove that every nonzero \(w\) with \(a\ne0\) has Schmidt rank at least two on each of the four 1|3 and three 2|2 cuts, whereas \(a=0\) gives the single fully product ray \(v\).

For any singleton \(i\in\{1,2,3,4\}\), with the remaining three qubits in any fixed order, the two physical coefficient rows are
\[
 \begin{aligned}
 R_0&=(b+ias/\sqrt2)|000\rangle
       +\frac{ac}{\sqrt6}(|011\rangle+|101\rangle+|110\rangle),\\
 R_1&=\frac{ac}{\sqrt6}(|001\rangle+|010\rangle+|100\rangle)
       +\frac{ias}{\sqrt2}|111\rangle.
 \end{aligned}\tag{4}
\]
Their supports lie in residual weights \(\{0,2\}\) and \(\{1,3\}\), respectively. For \(a\ne0\), the displayed \(ac\)-terms make both rows nonzero; disjoint support makes them independent. Thus the Schmidt rank is exactly two on each of \(1|234,2|134,3|124,4|123\).

For any balanced cut \(12|34,13|24,14|23\), use ordered pair bases \(00,01,10,11\). The actual coefficient matrix, after the corresponding qubit permutation, is
\[
 M(w)=
 \begin{pmatrix}
 b+ias/\sqrt2&0&0&ac/\sqrt6\\
 0&ac/\sqrt6&ac/\sqrt6&0\\
 0&ac/\sqrt6&ac/\sqrt6&0\\
 ac/\sqrt6&0&0&ias/\sqrt2
 \end{pmatrix}.\tag{5}
\]
The rows/columns split into disjoint \(\{00,11\}\) and \(\{01,10\}\) blocks. For \(a\ne0\), the second block has rank one and the first has nonzero off-diagonal \(ac/\sqrt6\), hence rank at least one. The total rank is at least two; more precisely it is two if
\[
 (b+ias/\sqrt2)(ias/\sqrt2)-(ac/\sqrt6)^2=0,
\]
and three otherwise. For \(a=0,b\ne0\), both (4) and (5) have rank one. Permutation invariance of both \(\psi\) and \(v\) justifies using the same forms for all seven explicitly named cuts. Local unitaries preserve each cut's Schmidt rank.

For a positive decomposition \(X_q=\sum_j p_j|w_j\rangle\langle w_j|\), \(p_j>0\), every \(w_j\) lies in \(\operatorname{range}X_q\): if \(n\in\ker X_q\), then \(0=\sum_j p_j|\langle n|w_j\rangle|^2\). A pure biseparable vector lies on at least one of the seven product-across-cut loci, and (4)–(5) show that the only such ray in \(W\) is \(v\). Thus for \(0<q<1\), any biseparable decomposition would consist entirely of \(v\) and give \(P\), contrary to rank two. At \(q=0\), the range is the non-biseparable ray \(\psi\). At \(q=1\), the state is \(P\). This proves Claim 2, including the rank-one endpoints, and local unitaries give the result for \(\rho_{q,U}\).

## 4. Exact eta-zero and eta-one rays inside the physical span

Write \(w=a\psi+bv\). Since \(F\) is real symmetric, direct expansion on \((D,y,z)\) gives
\[
 w^TFw=a^2C+i\sqrt2\,ab s.\tag{6}
\]
For \(a=0\), \(v^TFv=0\). For \(a\ne0\), rescale to \(a=1\); \(\eta(w)=0\) if and only if the numerator in (6) vanishes, i.e. exactly when
\[
 w=x_N:=\psi+i\frac{C}{\sqrt2s}v.
 \tag{7}
\]
Thus the complete eta-zero ray list is \(\mathbb Cv\) and \(\mathbb Cx_N\).

For \(\eta=1\), equality in Cauchy–Schwarz gives \(\Theta w=e^{i\varphi}w\). The ray \(v\) is not eta-one. For \(a\ne0\), rescale to \(a=1\), so the nonzero \(D\)-coefficient \(c\) is real. Since \(\Theta D=D\), equality then forces \(e^{i\varphi}=1\). In
\[
 w=cD+(is+b/\sqrt2)y+(b/\sqrt2)z,
\]
\(\Theta w=w\) requires the \(z\)-coefficient to be purely imaginary and the \(y\)-coefficient real. The first makes \(b\) purely imaginary, and the second then makes \(is+b/\sqrt2=0\). Hence the **only** eta-one ray is
\[
 x_I:=\psi-i\sqrt2s\,v=cD-isz.\tag{8}
\]
Conversely \(\Theta x_I=x_I\), and (6) vanishes for \(x_N\), establishing both directions rather than only listing candidates. The range \(1/6\le C\le1/3\) ensures \(s>0\) and all these rays are distinct. Their physical norms are
\[
 \|x_I\|^2=1,\qquad \|x_N\|^2=\frac1{1-C},\qquad \|v\|^2=1.\tag{9}
\]
For (9), for instance, \(\|x_N\|^2=1+C+C^2/(1-C)=1/(1-C)\); the cross term is essential because \(\psi\) and \(v\) are not orthogonal.

## 5. Positive range restriction and the nonorthogonal-coordinate cone

The pure-state sets defining \(\mathcal H\) are compact: the seven product-across-cut sets are compact, as are the eta-zero and eta-one level sets on the unit sphere. Their finite union is compact, so its convex hull consists of finite convex combinations, e.g. by Carathéodory in the real trace-one Hermitian space. Hence the positive-range argument in §3 applies to every member of \(\mathcal H\), without silently assuming an unproved decomposition or closure convention.

Define the injective synthesis map \(S:\mathbb C^2\to W\) by \(S e_1=\psi,\ S e_2=v\). Its Gram matrix is
\[
 G=S^\dagger S=\begin{pmatrix}1&-is/\sqrt2\\ is/\sqrt2&1\end{pmatrix},
 \qquad \det G=(3+C)/4>0.
\]
If an operator is supported on \(W\), its coordinate representation \(S M S^\dagger\) is unique, since the left inverse \(L=(S^\dagger S)^{-1}S^\dagger\) gives \(M=L(SMS^\dagger)L^\dagger\). This is a coordinate **congruence**, not an orthonormal-basis matrix: in general \(\operatorname{Tr}(SMS^\dagger)=\operatorname{Tr}(GM)\), not \(\operatorname{Tr}M\).

Put \(A=\sqrt2s=\sqrt{1-C}\), \(B=C/A\). By the complete ray classification, any hypothetical \(X_q\in\mathcal H\), even at a rank-one endpoint, must be expressible with \(\alpha,\beta,\gamma\ge0\) as
\[
 X_q=\alpha|x_I\rangle\langle x_I|
       +\beta|x_N\rangle\langle x_N|
       +\gamma|v\rangle\langle v|.\tag{10}
\]
All physical normalization factors have been absorbed into these nonnegative coefficients. In the \((\psi,v)\) coordinates, the three column vectors are \((1,-iA)^T,(1,iB)^T,(0,1)^T\). Since the coordinate matrix of \(X_q\) is \(\operatorname{diag}(1-q,q)\), (10) is equivalent to
\[
 \alpha+\beta=1-q,\quad \alpha A=\beta B,\quad
 q=\alpha A^2+\beta B^2+\gamma.\tag{11}
\]
Here \(A+B=1/A\), so the unique solution to the first two equations is
\[
 \alpha=(1-q)C,\qquad \beta=(1-q)(1-C),
\]
and the third becomes
\[
 q=(1-q)C+\gamma.\tag{12}
\]
Therefore membership forces \(q\ge(1-q)C\). This conclusion at \(q=0\) is valid despite the actual range being only \(\mathbb C\psi\): range is merely **contained** in \(W\), and the resulting nonnegative cone equations still apply.

Conversely, if \(q\ge(1-q)C\), all three coefficients just found, with \(\gamma=q-(1-q)C\), are nonnegative and satisfy (11), so (10) is an actual decomposition into the defining pure-state classes. Explicitly, with \(\widehat x_N=\sqrt{1-C}\,x_N\), the normalized probabilities are
\[
 p_I=(1-q)C,\qquad p_N=1-q,\qquad p_v=q-(1-q)C,
 \quad p_I+p_N+p_v=1,
\]
and
\[
 X_q=p_I|x_I\rangle\langle x_I|
     +p_N|\widehat x_N\rangle\langle\widehat x_N|
     +p_v|v\rangle\langle v|.\tag{13}
\]
At equality \(p_v=0\); at \(q=1\), only \(v\) remains. Thus (A) is both necessary and sufficient. Because local unitaries preserve each of biseparability, eta-zero and eta-one, they preserve \(\mathcal H\) in both directions, proving the exact criterion for every \(U\).

## 6. Relation to the named older hull and limits

Every spin-flip-invariant mixed density lies in the eta-one portion of \(\mathcal H\). Indeed \(\Theta^2=I\) supplies an orthonormal \(\Theta\)-fixed basis: the fixed real vectors span the Hilbert space over \(\mathbb C\), and real Gram–Schmidt yields such a basis. In it an invariant Hermitian density is real symmetric, so it has a real orthonormal eigenbasis; each eigenvector is \(\Theta\)-fixed and has eta one. Conversely, a mixture of eta-one pure densities is spin-flip invariant. The Dicke ray is eta one and stays so under local unitaries by (3). A coherent superposition of the vacuum and a one-excitation W vector has eta zero, since \(F\) maps its weight-0/1 support to weight-4/3 support; its local-unitary orbit stays eta zero. All biseparable mixed states are in the convex hull of pure biseparable states. Thus the four packet-named classes and their mixed convex hull are contained in \(\mathcal H\); the proof separates the original box from this explicitly larger hull.

The f852 packet body also claims actual all-\(p\), all-prefix channel majorization. That channel result is **not** derived or independently certified by this narrower defect/hull candidate. If a combined channel-and-separation conclusion is desired, its channel half is conditional on independently checking the f852 §§2–5 argument. Likewise, the packet S2's linked invariant-sector and prior-region proof bodies were not supplied as complete sources here and were not opened; any use of their historical channel claims is a separately named conditional import, not needed for the algebra above. Failure of these sufficient-region tests does not establish a channel counterexample. No statement is made about all four-qubit states, optimum hulls beyond the exact one defined here, novelty, external acceptance, or publication.

## 7. Complete input and process declaration

Before mathematical body reading or reasoning, I read the manifest, freeze receipt, final pre-dispatch binding, parent live metadata supply, actual dispatch receipt, and all 22 manifest-listed controls for **status and permissions only**. Initial non-raw displays of four administrative JSONs elided blocks; complete raw rereads recovered them before the acknowledgement. The initial non-raw dispatch receipt displayed all 46 lines; it was also reread raw after the packet. General skills and the required memory summary were administrative only; the summary displayed some clipped long lines and was not a mathematical input. The prebody acknowledgement was written as `prebody-ack-v1.md` and sent directly to Main before opening the packet.

I read the sole literal packet part completely and serially in raw windows 1–20, 21–40, 41–60, 61–80, 81–100, 101–120, 121–140, 141–160, 161–180, 181–200, 201–220, 221–240, 241–260, and 261–276, including the ending. No packet window displayed clipping. The parent-supplied total is 27,230 bytes, so every raw window was under 30,000 bytes as well as at most 20 LF. Parent metadata supplies part SHA-256 `5cc20c2d1bd4ccc8ae95dc40dfce934e9dc9aae66147352a651cade9b7ceb826`, S1 complete LF 1–219 SHA-256 `098435386c86deeb036faa455fe17ca43ae613fc25a2cc62060a4cbb6b63fcd2`, and S2 complete LF 1–47 SHA-256 `4d9f3d97723cafe956eaf7c151506249e08c246bb35b59436fe64b015558eaff`. These are supplied metadata pins, not hashes independently computed by this worker.

All genuinely held episodes and all their proof/method/selection/planning/verification/reporting/confidence/downstream consumers remained NONINPUT. No linked source or unlisted mathematical file was opened. No scientific code, child subprocess, shell command, test, compilation, scientific evaluation, network or external-model call was executed; no verifier source was prepared, so there is no prepared-code hash or computational-verification claim. Parent disposition and independent review remain separate.
