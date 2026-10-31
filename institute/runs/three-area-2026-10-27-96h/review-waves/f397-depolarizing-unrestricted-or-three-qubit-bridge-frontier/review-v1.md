# Author candidate v1 — Full depolarizing-output majorization on the three-qubit parity sector and a strict four-qubit extension

**Status: AUTHOR / UNREVIEWED.** This is a written proof candidate, not an independent review, finite-check result, parent adoption, novelty determination, or unrestricted-target closure.

**Materialization:** Complete body returned for Main to place in the assigned wave’s `author-candidate-v1.md`. No repository file was written and no scientific program was executed by this author role.

## 1. Result and exact relation to the target

Write
\[
\Phi_p(X)=(1-p)X+\frac p2\operatorname{Tr}(X)I,
\qquad 0\le p\le\frac43,
\]
and put
\[
t=|1-p|,\qquad a=\frac{1+t}{2},\qquad b=\frac{1-t}{2},
\qquad D_{n,t}=\operatorname{diag}(a,b)^{\otimes n}.
\]
For a Hermitian matrix \(X\), let \(K_k(X)\) be its \(k\) largest eigenvalues summed.

### Theorem A — Entire three-qubit parity-preserving sector

For **every complex three-qubit density operator** \(\rho\) satisfying
\[
[\rho,Z\otimes Z\otimes Z]=0,
\]
every physical \(p\in[0,4/3]\), every \(k=1,\ldots,8\), and every complex orthogonal rank-\(k\) projector \(Q\),
\[
\operatorname{Tr}\!\left[Q\Phi_p^{\otimes3}(\rho)\right]
\le K_k\!\left(\Phi_p^{\otimes3}(\rho)\right)
\le K_k(D_{3,t}).
\tag{1}
\]

The same statement holds after arbitrary physical local-unitary changes of basis. Equivalently, the commutation condition can be
\[
[\rho,A_1\otimes A_2\otimes A_3]=0,
\]
where each \(A_i\) is a traceless Hermitian one-qubit unitary.

This is not merely an \(X\)-density or diagonal-state theorem: in a fixed parity basis, the two \(4\times4\) positive blocks are otherwise arbitrary complex matrices. The fixed-basis state sector has real affine dimension \(31\).

### Theorem B — Four-qubit tensor and finite-mixture extension

Let \(\mathcal S\) be the finite convex hull of four-qubit states of the following form:

* choose any physical qubit as spectator;
* put an arbitrary one-qubit density \(\sigma\) on it;
* put a three-qubit density \(\tau\) satisfying Theorem A in some physical local bases on the remaining qubits;
* allow the spectator, local bases, states, and decomposition choices to differ between mixture components.

Then, for every \(\rho\in\mathcal S\), every physical \(p\), every \(k=1,\ldots,16\), and every complex orthogonal rank-\(k\) projector \(Q\),
\[
\operatorname{Tr}\!\left[Q\Phi_p^{\otimes4}(\rho)\right]
\le K_k\!\left(\Phi_p^{\otimes4}(\rho)\right)
\le K_k(D_{4,t}).
\tag{2}
\]

Moreover, \(\mathcal S\) contains pure states outside the previously adopted Class A/Class B convex hull. Section 8 proves this using a complex \(W_3\) state with a pure spectator. Thus adjoining \(\mathcal S\) to that hull gives a **strict extension**, rather than a constant refinement or repackaging of its existing sectors.

### What is not proved

This manuscript does **not** prove:

* majorization for arbitrary complex three-qubit input;
* majorization for every \(1|3\)-separable four-qubit state;
* unrestricted four-qubit \(k=3\);
* unrestricted four-qubit all-prefix majorization.

The new result is the complete parity-preserving three-qubit sector, its local-basis versions, and the stated four-qubit tensor/mixture extension.

---

## 2. Provenance, methods, and source coverage

The manifest, freeze receipt, parent metadata supply, all seven status controls, and the complete ordered packet S1–S3 were read before the derivation reported here. Held scientific payloads and their consumers were not opened as research inputs.

The SHA/byte/LF observations and the supplied clock are **parent-attributed metadata**, not child-native hashing, execution, start, or completion observations. No child-native completion time is asserted.

The scientific methods used were written algebra, fresh selected examples, and public primary-source reading, as permitted by this GENERAL AUTHOR assignment. There was:

* no scientific executable, solver, CAS, or numerical run;
* no package installation, external-model CLI, paid campaign, or remote computation;
* no use of an observed program output as evidence.

All numerical fractions below are **written exact arithmetic**, not stdout or an executed finite diagnostic.

The initial substantive checkpoint described the excitation-number-preserving subsector. The completed argument below establishes the larger parity-preserving sector.

The public paper [Song–Wang–Tomamichel–Fang, arXiv:2609.37240v1](https://arxiv.org/html/2609.37240v1) was read at its introduction, Theorem 4 and proof, Remark 5, discussion, and Appendix A.1. Section 10 distinguishes its published conclusions from the present exact-prefix claim.

The new proof below does not use the low-polarization or small-\(t\) certificates in S2/S3, or any held one-erasure/L1 or CORE-GRAM result.

---

## 3. Elementary spectral tools

### 3.1 Complex projectors

For a Hermitian \(X\) with ordered eigenvalues \(\lambda_1\ge\cdots\ge\lambda_m\), and any complex orthogonal rank-\(k\) projector \(Q\), write its diagonal entries in an eigenbasis of \(X\) as \(q_i\). Then
\[
0\le q_i\le1,\qquad \sum_iq_i=k,
\qquad
\operatorname{Tr}(QX)=\sum_i\lambda_iq_i
\le\sum_{i=1}^k\lambda_i.
\]
Equality is attained by the top-eigenspace projector. This proves the complex-projector Ky Fan characterization used throughout.

### 3.2 Direct sums

If \(X_j\) and \(Y_j\) have the same dimensions and traces, and
\[
K_\ell(X_j)\le K_\ell(Y_j)
\]
for every block and every index, then
\[
\bigoplus_jX_j\prec\bigoplus_jY_j.
\tag{3}
\]
Indeed,
\[
K_k\!\left(\bigoplus_jX_j\right)
=\max_{\substack{0\le k_j\le\dim X_j\\\sum_jk_j=k}}
\sum_jK_{k_j}(X_j),
\]
and the componentwise bounds apply to every allocation.

This is a statement about the full matrix. It does not restrict the consuming projector to be block diagonal.

### 3.3 Finite mixtures

If every \(X_j\) is majorized by the same \(D\), then, for nonnegative weights summing to one,
\[
K_k\!\left(\sum_jw_jX_j\right)
\le\sum_jw_jK_k(X_j)
\le K_k(D).
\tag{4}
\]
The first inequality follows immediately from the projector variational characterization.

---

## 4. Actual output of a pure parity eigenstate

First consider the nonnegative Bloch-parameter channel
\[
T_t(X)=tX+b\,\operatorname{Tr}(X)I,
\qquad 0\le t\le1.
\]

Choose the even-parity basis
\[
e_1=000,\quad e_2=011,\quad e_3=101,\quad e_4=110,
\]
and its complementary odd-parity basis
\[
\bar e_i=e_i\oplus111.
\]
Let
\[
|\psi\rangle=\sum_{i=1}^4c_i|e_i\rangle,
\qquad \sum_i|c_i|^2=1,
\]
with arbitrary complex coefficients, including zero coefficients. Define
\[
R=cc^\dagger,\qquad D=\operatorname{diag}(|c_1|^2,\ldots,|c_4|^2),
\]
and
\[
A=(1-t)D+tR,\qquad B=(1+t)D-tR.
\tag{5}
\]

Set
\[
u=a^3,\qquad d=a^2b,\qquad c_0=ab^2,\qquad \ell=b^3.
\]

The **actual physical output** is block diagonal in these two parity bases, with blocks
\[
M_E=c_0I_4+atA,
\qquad
M_O=dI_4-bt\,\overline B.
\tag{6}
\]

Here the bar is entrywise complex conjugation, not partial transpose.

### Verification of (6)

Every two distinct even-parity basis strings have Hamming distance two.

For the even output block:

* the diagonal transition probability is \(a^3\) from the same string and \(ab^2\) from each other even string;
* an input off-diagonal matrix unit differs on two qubits, supplying \(t^2\), while its common bit is retained with probability \(a\).

Thus its diagonal entries are \(c_0+at|c_i|^2\), and its off-diagonal entries are \(at^2c_i\overline{c_j}\), giving \(M_E\).

For the complementary odd block:

* the diagonal transition probability is \(b^3\) from \(e_i\) to \(\bar e_i\), and \(a^2b\) from any other \(e_j\);
* the relevant off-diagonal input orientation is reversed, with common-bit factor \(b\).

Its diagonal entries are \(d-bt|c_i|^2\), and its off-diagonal entries are \(bt^2\overline{c_i}c_j\), giving \(M_O\).

In particular,
\[
\operatorname{Tr}M_E=u+3c_0,\qquad
\operatorname{Tr}M_O=3d+\ell.
\tag{7}
\]

No output-spectrum conjecture has been assumed in obtaining these blocks.

---

## 5. Coupled block estimate

The key point is to compare the two blocks **jointly**. Separate blockwise product-reference majorization is false; Section 9 supplies an actual physical counterexample to that auxiliary premise.

Let
\[
\alpha=\lambda_{\max}(A),\qquad
\gamma=\max\{0,-\lambda_{\min}(B)\},
\qquad
\delta=bt\gamma.
\tag{8}
\]

### 5.1 Basic properties of \(A\) and \(B\)

The matrix \(A\) is positive semidefinite and has trace one.

The matrix \(B\) has at most one negative eigenvalue: on the codimension-one subspace orthogonal to \(c\), its quadratic form is
\[
(1+t)v^\dagger Dv\ge0.
\]

Also,
\[
B\le I.
\tag{9}
\]
To see this, put \(B_1=2D-R\). The exact complex Gram identity
\[
I-2D+R
=
\sum_{i<j}
(\overline{c_j}e_i+\overline{c_i}e_j)
(\overline{c_j}e_i+\overline{c_i}e_j)^\dagger
\ge0
\tag{10}
\]
gives \(B_1\le I\). Since
\[
B=(1-t)D+tB_1,\qquad D\le I,
\]
equation (9) follows.

### 5.2 A uniform bound on the negative eigenvalue

For \(t\le1/3\), Cauchy–Schwarz gives \(R\le4D\), so
\[
B\ge(1-3t)D\ge0.
\]

For \(t>1/3\), set
\[
g=\frac{3t-1}{4}>0.
\]
The function \(r\mapsto r/(g+(1+t)r)\) is concave on \(r\ge0\). Consequently,
\[
\sum_{i=1}^4\frac{|c_i|^2}{g+(1+t)|c_i|^2}
\le
4\,\frac{1/4}{g+(1+t)/4}
=\frac1t.
\]
Weighted Cauchy–Schwarz therefore gives
\[
tR\le (1+t)D+gI,
\qquad B\ge-gI.
\]
Together these show
\[
\gamma\le\max\left\{0,\frac{3t-1}{4}\right\}
\le\frac{1+t}{4}=\frac a2.
\tag{11}
\]
In particular,
\[
2\delta\le abt.
\tag{12}
\]

This argument includes zero populations: the denominators are strictly positive in the branch where they are used.

### 5.3 The upper-block deficit pays for the lower-block excess

Let \(m=\max_i|c_i|^2\). Since \(R\) has norm one,
\[
\alpha\le t+(1-t)m.
\tag{13}
\]

Choose \(j\) with \(|c_j|^2=m\), and write \(c=c_je_j+q\), where \(\|q\|^2=1-m\). The elementary matrix inequality
\[
R\le2m\,e_je_j^\dagger+2qq^\dagger
\]
implies
\[
R-2D\le2qq^\dagger\le2(1-m)I.
\]
It follows that
\[
-B=-(1-t)D+t(R-2D)\le2t(1-m)I,
\]
and hence
\[
\gamma\le2t(1-m).
\tag{14}
\]

Define
\[
\varepsilon=at(1-\alpha).
\]
Equations (13)–(14), \(1-t=2b\), and \(t\le a\) imply
\[
\delta
\le2bt^2(1-m)
\le2abt(1-m)
\le\varepsilon.
\tag{15}
\]

This is a universal coupled estimate for every normalized complex \(c\), not an input-conditioned numerical certificate.

### 5.4 Four-dimensional block majorants

From (6), \(A\ge0\), and (15),
\[
\lambda_{\min}(M_E)\ge c_0,\qquad
\lambda_{\max}(M_E)\le u-\delta.
\]
Using its trace from (7), these bounds establish
\[
M_E\prec
\operatorname{diag}(u-\delta,c_0+\delta,c_0,c_0).
\tag{16}
\]
For example, the top-two bound is its trace minus two eigenvalues each at least \(c_0\), namely \(u+c_0\); the top-three bound is \(u+2c_0\). These are exactly the corresponding sums on the right.

For \(M_O\):

* \(B\le I\) gives \(\lambda_{\min}(M_O)\ge d-bt=\ell\);
* at most one eigenvalue exceeds \(d\);
* its largest eigenvalue is at most \(d+\delta\).

Together with (7), these imply
\[
M_O\prec
\operatorname{diag}(d+\delta,d,d-\delta,\ell).
\tag{17}
\]
The top-two bound is \(2d+\delta\), and the top-three bound is the trace minus the smallest eigenvalue, at most \(3d\).

All displayed majorants are ordered. Indeed, (12) gives
\[
d-\delta\ge c_0+\delta,\qquad
u-\delta\ge d+\delta,
\]
because
\[
d-c_0=abt,\qquad u-d=a^2t,\qquad b\le a.
\]
It also ensures the internal ordering needed in (16)–(17).

### 5.5 Full eight-eigenvalue comparison

By the direct-sum lemma, the full output is majorized by the ordered vector
\[
v=(u-\delta,\ d+\delta,\ d,\ d-\delta,\ c_0+\delta,\ c_0,\ c_0,\ \ell).
\tag{18}
\]
The ordered product-reference spectrum is
\[
r=(u,d,d,d,c_0,c_0,c_0,\ell).
\tag{19}
\]

The eight prefix differences \(\sum_{i\le k}(r_i-v_i)\) are exactly
\[
(\delta,0,0,\delta,0,0,0,0).
\tag{20}
\]
They are nonnegative. Therefore
\[
T_t^{\otimes3}(|\psi\rangle\langle\psi|)\prec D_{3,t}.
\tag{21}
\]

The intermediate majorant depends on the input and \(t\), but **not on the consuming projector**. It establishes all prefixes simultaneously.

No division by \(t\), \(a-b\), a population, a block trace, or an eigenvalue gap occurs. At \(t=0\) the output is \(I_8/8\); at \(t=1\) a pure input has the pure reference spectrum. Rank drops and eigenvalue ties require no separate diagonalizer choice.

---

## 6. Mixed parity states, local bases, and the negative branch

### 6.1 Odd parity and arbitrary mixed parity blocks

The local unitary \(X^{\otimes3}\) exchanges the two parity sectors. Local covariance of \(T_t\) therefore transfers (21) to every pure odd-parity state.

If \([\rho,Z^{\otimes3}]=0\), each of its two positive \(4\times4\) blocks has a finite spectral decomposition into pure parity eigenstates. Applying (4) proves the result for every mixed parity-preserving input.

For any one-qubit unitary \(U\),
\[
T_t(UXU^\dagger)=UT_t(X)U^\dagger.
\]
Thus arbitrary complex physical local bases are permitted.

### 6.2 Full physical parameter range

Write \(s=1-p\). The channel is completely positive precisely for
\[
-\frac13\le s\le1,
\]
as seen from its Pauli probabilities
\[
q_I=\frac{1+3s}{4},\qquad q_X=q_Y=q_Z=\frac{1-s}{4}.
\]

For one qubit, define the spin flip
\[
\mathcal J(X)=YX^TY=\operatorname{Tr}(X)I-X.
\]
Then \(T_{-t}=\mathcal J\circ T_t\). Consequently, for every \(n\),
\[
T_{-t}^{\otimes n}(\rho)
=
W_n\,[T_t^{\otimes n}(\rho)]^T W_n,
\qquad W_n=Y^{\otimes n}.
\tag{22}
\]
This is **full transpose**, not partial transpose, so the spectra agree.

For an arbitrary complex rank-\(k\) projector \(Q\),
\[
\operatorname{Tr}\!\left[Q\,T_{-t}^{\otimes n}(\rho)\right]
=
\operatorname{Tr}\!\left[Q'\,T_t^{\otimes n}(\rho)\right],
\qquad
Q'=W_nQ^TW_n,
\tag{23}
\]
and \(Q'\) is again a complex orthogonal rank-\(k\) projector.

The physical negative branch only requires \(0\le t\le1/3\), already included in the positive-\(t\) proof.

Finally, when \(p>1\), a pure one-qubit product input produces \(\operatorname{diag}(b,a)\), rather than \(\operatorname{diag}(a,b)\). Their tensor powers have identical spectra. Thus the reference in (1) is exactly the original product-output reference spectrally throughout the physical range.

This completes Theorem A.

---

## 7. Tensoring and finite mixtures: proof of Theorem B

Here is a direct spectral proof of tensor preservation, without assuming an input-independent postprocessing channel.

Suppose positive matrices \(X\prec X_0\) and \(Y\prec Y_0\). Diagonalize \(X\), with nonnegative eigenvalues \(x_i\). Then
\[
K_k(X\otimes Y)
=
\max_{\substack{0\le k_i\le\dim Y\\\sum_i k_i=k}}
\sum_i x_iK_{k_i}(Y)
\le K_k(X\otimes Y_0).
\]
Now diagonalize \(Y_0\) and apply the same argument with \(X\prec X_0\). This proves
\[
X\otimes Y\prec X_0\otimes Y_0.
\tag{24}
\]

For an arbitrary one-qubit density \(\sigma\), its output eigenvalues are
\[
\frac{1+tr_\sigma}{2},\qquad \frac{1-tr_\sigma}{2},
\qquad 0\le r_\sigma\le1,
\]
up to ordering on the negative branch. Hence
\[
\Phi_p(\sigma)\prec\operatorname{diag}(a,b).
\]
Theorem A and (24) give
\[
\Phi_p(\sigma)\otimes\Phi_p^{\otimes3}(\tau)
\prec D_{4,t}.
\]
Physical qubit permutations are unitary conjugations. Equation (4) then proves the result for every finite mixture specified in Theorem B, even when its spectator and local bases vary by component.

In particular, for every such input and the **same arbitrary complex rank-three projector** \(Q\),
\[
\operatorname{Tr}\!\left[Q\Phi_p^{\otimes4}(\rho)\right]
\le a^4+2a^3b.
\tag{25}
\]
There is no sum of separately attained Pauli-layer maxima.

---

## 8. Strict enlargement beyond Classes A/B

Consider
\[
|\Omega\rangle
=
|0\rangle\otimes
\frac{|100\rangle+i|010\rangle+|001\rangle}{\sqrt3}.
\tag{26}
\]
Its three-qubit factor has odd parity, so Theorem B applies.

### 8.1 It is not Class A

The three-qubit \(W\) factor has tensor rank three. A short proof suffices here.

Across its first qubit versus the remaining two, the two-qubit Schmidt support is
\[
\operatorname{span}\{|00\rangle,\ i|10\rangle+|01\rangle\}.
\]
A vector in this support has coefficient matrix
\[
\begin{pmatrix}u&v\\iv&0\end{pmatrix},
\]
whose determinant is \(-iv^2\). Thus the support contains only one product-vector direction.

A three-qubit tensor-rank-two state with Schmidt rank two across that cut would instead supply two independent product vectors spanning this support. Contradiction.

Factoring or contracting the pure spectator cannot reduce the three-qubit factor to tensor rank two. Every Class A vector is a sum of at most two product vectors. Therefore \(\Omega\) is not Class A in any physical local bases.

### 8.2 It is not Class B for any pairing

In any pairing, one encoded pair contains the pure spectator. Its reduced density has the form
\[
|0\rangle\langle0|\otimes\rho_j,
\]
where \(\rho_j\) has rank two. Its range is consequently the two-dimensional space
\[
|0\rangle\otimes\mathbb C^2.
\]

A Class B pair code has the form
\[
E=\operatorname{span}\{|u_0v_0\rangle,\ |u_1v_1\rangle\},
\]
with both local pairs orthonormal. Its projector has first-qubit partial trace \(I_2\). The projector onto \(|0\rangle\otimes\mathbb C^2\), by contrast, has first-qubit partial trace \(2|0\rangle\langle0|\). The two spaces cannot coincide. Since both have dimension two, the required range containment is impossible.

Thus \(\Omega\) is not Class B for any pairing or physical local bases.

### 8.3 Convex-hull consequence

A rank-one density cannot be a nontrivial convex mixture of positive densities with different supports. Hence \(|\Omega\rangle\langle\Omega|\) is outside the entire old Class A/Class B convex hull.

Using the scoped S1 theorem as the existing import,
\[
\mathcal C_{\rm new}
=
\operatorname{conv}(\mathcal C_{\rm old}\cup\mathcal S)
\]
therefore has full majorization and strictly contains \(\mathcal C_{\rm old}\). The proof of the new sector itself did not depend on S1.

---

## 9. Exact physical example and a falsified blockwise premise

These are written exact calculations, not an executed diagnostic.

Take
\[
p=\frac14,\quad t=\frac34,\quad a=\frac78,\quad b=\frac18,
\]
and
\[
|\psi_W\rangle=\frac{|100\rangle+i|010\rangle+|001\rangle}{\sqrt3}.
\]

The ordered spectrum of the actual three-qubit output is
\[
\frac1{512}(287,57,49,35,35,21,21,7).
\tag{27}
\]
The product-reference spectrum is
\[
\frac1{512}(343,49,49,49,7,7,7,1).
\tag{28}
\]
Their ordered prefix differences, reference minus actual, are
\[
\frac1{512}(56,48,48,62,34,20,6,0).
\tag{29}
\]

For example, in the four-dimensional odd input basis the coefficient vector is \((0,1,i,1)/\sqrt3\). The nonzero eigenvalues of \(A\) are \(5/6,1/12,1/12\); those of \(B\) are \(-1/6,7/12,7/12\), with one additional zero in each matrix. Substitution into (6) gives (27).

### Actual complex rank-three projector

Put
\[
|\eta\rangle=\frac{|011\rangle-i|101\rangle+|110\rangle}{\sqrt3},
\]
and
\[
Q_3=
|\psi_W\rangle\langle\psi_W|
+|\eta\rangle\langle\eta|
+|000\rangle\langle000|.
\]
The three vectors are orthonormal, and \(Q_3\) is a genuinely complex rank-three orthogonal projector. It selects the top three eigenvalues in (27):
\[
\operatorname{Tr}[Q_3T_t^{\otimes3}(|\psi_W\rangle\langle\psi_W|)]
=\frac{393}{512}
<\frac{441}{512}=K_3(D_{3,t}).
\]

For the actual four-qubit input \(\Omega\) in (26), use
\[
Q_4=|0\rangle\langle0|\otimes Q_3.
\]
This is a complex rank-three projector on the full sixteen-dimensional space, and
\[
\operatorname{Tr}[Q_4\Phi_{1/4}^{\otimes4}(|\Omega\rangle\langle\Omega|)]
=\frac{2751}{4096}
<\frac{3087}{4096}
=a^4+2a^3b.
\tag{30}
\]
The slack is \(21/256\).

### Separate parity-block majorization is false

For this same physical input, the even output block has spectrum
\[
\frac1{512}(57,49,21,21).
\]
For the pure product input \(|100\rangle\), the corresponding even output block has spectrum
\[
\frac1{512}(49,49,49,1).
\]
The complex projector \(|\eta\rangle\langle\eta|\) attains \(57/512\) on the first block, exceeding the second block’s largest eigenvalue \(49/512\).

Thus one cannot prove the theorem by independently majorizing each actual parity block by its corresponding product-reference block. The coupled deficit/excess argument is essential.

This is **not** a counterexample to full output majorization; (27)–(29) show the full comparison holds.

---

## 10. Prior attribution and other negative findings

### Published log-determinant ordering is not the exact-prefix result

[Song, Wang, Tomamichel, and Fang, arXiv:2609.37240v1, Theorem 4](https://arxiv.org/html/2609.37240v1#Thmtheorem4) establish shifted-log-determinant ordering for all blocklengths and arbitrary inputs. Their Theorem 1 gives approximate majorization, not exact majorization.

Their [Appendix A.1](https://arxiv.org/html/2609.37240v1#A1.SS1) explicitly uses arbitrary states—not asserted channel outputs—
\[
X=\operatorname{diag}(0.42,0.29,0.29),\qquad
Y=\operatorname{diag}(0.40,0.35,0.25),
\]
for which
\[
\det(hI+X)-\det(hI+Y)=\frac h{5000}+\frac{161}{500000}>0
\]
for every \(h>0\), although \(K_1(X)>K_1(Y)\).

Consequently, that published theorem alone is not a proof of the exact target. It is not claimed as new here or used as a substitute for Section 5.

[King’s primary paper](https://arxiv.org/abs/quant-ph/0204172) establishes the depolarizing-channel norm-multiplicativity result; the all-\(q\) output ordering is also stated explicitly in Song et al., Remark 5. Those known norm inequalities are not substituted for exact prefixes here.

### A cluster-state route does not enlarge the old sector

A four-qubit line-cluster enlargement was rejected as redundant. Its stabilizers include \(X_1Z_2\) and \(Z_3X_4\), constraining the two pairs \(12\) and \(34\) to two-dimensional local-basis repetition codes. It is therefore already Class B. It is not counted as a new sector.

### Parity pinching does not close the unrestricted problem

Pinching an arbitrary input into its two parity blocks removes cross-parity coherences. Such pinching makes the output more mixed; that implication is in the wrong direction for promoting the present upper bounds to the original unpinched output.

No theorem for arbitrary cross-parity coherences is supplied here.

### Novelty boundary

No exhaustive primary-source priority audit was completed for this exact parity-sector theorem. The proof is an author candidate, not a novelty claim. The public results above retain their attribution.

---

## 11. Exact unpaid obligations and assurance ceiling

The unresolved scientific step for arbitrary three-qubit input is control of
\[
C=\Pi_+\rho\Pi_-,
\]
where \(\Pi_\pm\) are the parity projectors. The present proof treats arbitrary positive diagonal blocks but assumes \(C=0\). Convexity and pinching do not remove that obligation.

Accordingly:

* the unrestricted three-qubit bridge remains open;
* general \(1|3\)-separable four-qubit majorization remains open;
* arbitrary genuinely four-qubit input, including the unrestricted \(k=3\) and all-prefix targets, remains open.

The outstanding acceptance gates are a disjoint reconstruction of every load-bearing inequality, a separately attributed finite physical-channel check if commissioned, and parent disposition. None has been performed by this author return.

**Completed author deliverable:** a self-contained all-prefix/all-physical-parameter proof candidate for every complex parity-preserving three-qubit density, a rigorous tensor/finite-mixture extension, a proof that the resulting four-qubit enlargement is strict, and an exact physical complex-projector example exposing why independent blockwise majorization would fail.