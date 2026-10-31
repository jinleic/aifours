# F565 — Written reconstruction of the physical normal form and compatible marginal blocks

**Overall correctness: correct.** The candidate’s physical local-unitary normal form, complete compatible \(H_3\) spectrum, sharp fourth-prefix bound, and invariant-sector majorization theorem are supported by the written reconstruction below. No mathematical defect was found within the stated spin-flip-invariant four-qubit scope.

**Findings:** **0 FATAL / 0 MAJOR / 0 MINOR.**  
**Confidence:** **0.98**, for the stated mathematical scope under written review—not kernel, human, independent-family, novelty, or source-equivalence certification.

**Materialization:** This is the complete review body for Main to materialize as this wave’s `review-v1.md`. No repository file was written.

## 1. Frozen inputs, chronology, and method

The reviewed wave is:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f565-four-qubit-invariant-physical-so4-normal-form-and-marginal-block-review/`

Frozen identifiers:

- Manifest SHA256: `87e393835248948e14bb4a5afdbf1d6ea8ca5e5d619ab74aca0e2b1ffef7fa02`.
- Freeze-receipt SHA256: `9fca801cd695bbd1c45ad61c81fe8419343af5410d18b2c799bf1a8a5cdb0229`.
- Packet SHA256: `4bb2db14e2461f4a7f4150e3222f203aa87822da004f0fc05f14402392847efc`.
- S1, complete F558 author candidate: SHA256 `e300afac40b19341a321be3e9acd84c1d9c81bd10e6f1d3638733087faf3ee51`, logical source lines 1–698.
- S2, prior invariant-sector/Dicke disposition: SHA256 `7bb4ba23f47f1ab1c22ea37ed22a873f6073718913a0cd8715b3ca3d070d66ca`, source lines 1–42.

Hashes, byte counts, LF counts, and the clock `2026-10-30T13:31:55-0700 PDT` are **parent-supplied metadata observations** from `parent-live-metadata-supply-v1.json`, not my own hash execution or native start time.

Before mathematical packet access, I completely read:

1. The manifest and freeze receipt, including their endings.
2. All twelve listed status-only controls, including their endings.
3. The complete parent metadata supply.

I then delivered the required **direct pre-body ACK to `agent://Main`**. Only afterward did I read the complete literal packet in ordered, raw windows of at most twenty LF: packet lines 1–742, ending with S2 line 42. No displayed elision required recovery. Derivation began after completion of that read.

**Method:** Written, exact algebra only. No scientific code, interpreter, CAS, enumeration, numerical experiment, solver, build, test, formatter, external-model CLI, new public source, author code, sibling return, or held mathematical payload was used. No additional selected parameter, state, angle, generator, or gauge diagnostic was introduced. The explicit sharp input checked below is the one already specified by S1.

All held episodes and their proof, method, selection, planning, confidence, and reporting consumers remain **HELD/ZERO/NONINPUT**. This is not a clean-cognition certificate.

## 2. Scope and import accounting

The candidate concerns actual densities satisfying

\[
\rho\ge0,\qquad \operatorname{Tr}\rho=1,\qquad
\widetilde\rho=Y^{\otimes4}\rho^TY^{\otimes4}=\rho.
\]

Its physical marginal layers are

\[
H_j(\rho)=\sum_{|S|=j}\rho_S\otimes I_{S^c},
\]

with the factors placed on their actual tensor positions.

S2 supplies the **previously adopted scope and residual**, not proof of the new normal form or sharp fourth-prefix inequality. Its linked reviews, code, and execution receipts were not followed. The new argument below is reconstructed from S1 itself using elementary linear algebra, physical Pauli actions, partial traces, and the Ky Fan variational principle.

In particular:

- No three-qubit result is tensorized into a four-qubit theorem.
- No four-qubit Kramers pairing is assumed.
- No independently chosen marginals replace compatible marginals.
- No entangling pair unitary substitutes for physical one-qubit operations.
- No finite check is represented as universal proof.

## 3. Antiunitary real structure and the mixed-state reduction

**Status: SUPPORTED.**  
**Anchors:** S1 lines 156–192.

For one qubit, \(Y\overline Y=-I\). Therefore

\[
\Theta_4^2
=(Y^{\otimes4}\mathcal K)^2
=(-I)^{\otimes4}=I.
\]

The author correctly uses square \(+I\), not a Kramers antiunitary of square \(-I\).

For the declared pair basis

\[
m_1=i\Phi^+,\quad m_2=\Phi^-,
\quad m_3=\Psi^+,\quad m_4=i\Psi^-,
\]

the real Bell vectors have spin-flip signs

\[
\Theta_2\Phi^+=-\Phi^+,\quad
\Theta_2\Phi^-=\Phi^-,\quad
\Theta_2\Psi^+=\Psi^+,\quad
\Theta_2\Psi^-=-\Psi^-.
\]

Antilinearity changes the sign of the displayed factors \(i\), so **all four \(m_j\) are fixed by \(\Theta_2\)**. Consequently all sixteen products \(m_j^{12}\otimes m_k^{34}\) are fixed by \(\Theta_4\).

In this product basis, \(\Theta_4\) is coefficientwise conjugation. Thus an invariant Hermitian density is a real symmetric positive matrix. The real spectral theorem supplies

\[
\rho=\sum_\ell w_\ell|\psi_\ell\rangle\langle\psi_\ell|,
\qquad
w_\ell\ge0,\quad \sum_\ell w_\ell=1,\quad
\Theta_4\psi_\ell=\psi_\ell.
\]

This is a decomposition of **every density in the assigned invariant sector**, not an assumption that the density already belongs to a named pure-state orbit.

Linearity of \(H_3\) and Ky Fan convexity then permit passage from a bound for every invariant pure input to every mixed invariant input.

## 4. All six physical generators and the \(SO(4)\) interface

**Status: SUPPORTED.**  
**Anchors:** S1 lines 198–223.

Use the author’s convention

\[
S_{jk}m_j=m_k,\qquad S_{jk}m_k=-m_j.
\]

Equivalently, \(S_{jk}=E_{kj}-E_{jk}\).

The physical computational-basis actions are

\[
\begin{aligned}
(-iX\otimes I)|ab\rangle&=-i|\bar a\,b\rangle,\\
(-iI\otimes X)|ab\rangle&=-i|a\,\bar b\rangle,\\
(-iZ\otimes I)|ab\rangle&=-i(-1)^a|ab\rangle,\\
(-iI\otimes Z)|ab\rangle&=-i(-1)^b|ab\rangle,\\
(-iY\otimes I)|ab\rangle&=(-1)^a|\bar a\,b\rangle,\\
(-iI\otimes Y)|ab\rangle&=(-1)^b|a\,\bar b\rangle.
\end{aligned}
\]

Substitution of the four declared \(m_j\) gives the following complete column descriptions. The tuple in the middle column is \((Gm_1,Gm_2,Gm_3,Gm_4)\), so it specifies every entry of the corresponding real matrix.

| Physical generator \(G\) | Complete ordered column actions | Real matrix |
|---|---|---|
| \(-iX\otimes I\) | \((m_3,m_4,-m_1,-m_2)\) | \(S_{13}+S_{24}\) |
| \(-iI\otimes X\) | \((m_3,-m_4,-m_1,m_2)\) | \(S_{13}-S_{24}\) |
| \(-iZ\otimes I\) | \((m_2,-m_1,-m_4,m_3)\) | \(S_{12}-S_{34}\) |
| \(-iI\otimes Z\) | \((m_2,-m_1,m_4,-m_3)\) | \(S_{12}+S_{34}\) |
| \(-iY\otimes I\) | \((-m_4,m_3,-m_2,m_1)\) | \(-S_{14}+S_{23}\) |
| \(-iI\otimes Y\) | \((m_4,m_3,-m_2,-m_1)\) | \(S_{14}+S_{23}\) |

All six signs in S1 are correct.

Writing these generators as \(G_{X1},G_{X2},\ldots\), their combinations give

\[
\begin{aligned}
S_{13}&=(G_{X1}+G_{X2})/2,&
S_{24}&=(G_{X1}-G_{X2})/2,\\
S_{12}&=(G_{Z1}+G_{Z2})/2,&
S_{34}&=(G_{Z2}-G_{Z1})/2,\\
S_{14}&=(G_{Y2}-G_{Y1})/2,&
S_{23}&=(G_{Y1}+G_{Y2})/2.
\end{aligned}
\]

Within each displayed pair, the two physical generators commute because they act on different qubits. Therefore exponentiation of these sums and differences factors into actual one-qubit \(SU(2)\) rotations. Every elementary plane rotation \(\exp(\theta S_{jk})\) is physically realizable in this way.

Givens elimination generates every member of \(SO(4)\) from these plane rotations. Hence the author has established **surjectivity onto the required proper real orthogonal actions using physical product unitaries**, rather than merely equality of dimensions or an unexplained \(SO(4)\) identification.

## 5. Signed real SVD, coefficient transport, and normal form

**Status: SUPPORTED.**  
**Anchors:** S1 lines 225–277.

Write

\[
|\psi\rangle=\sum_{j,k}A_{jk}m_j^{12}\otimes m_k^{34},
\qquad A\in\mathbb R^{4\times4},\quad \|A\|_F=1.
\]

An ordinary real SVD has orthogonal factors. Absorbing their possible reflection signs into the diagonal gives

\[
A=LDR^T,\qquad L,R\in SO(4),\qquad D=\operatorname{diag}(d_j),
\]

with real, not necessarily nonnegative, \(d_j\). This remains valid when singular values vanish: diagonal sign matrices can adjust the determinants without changing diagonality.

The coefficient transformation under pair actions \(O_{12},O_{34}\) is

\[
A\longmapsto O_{12}A\,O_{34}^T.
\]

Consequently the physically available choices \(O_{12}=L^T\), \(O_{34}=R^T\) produce

\[
L^TAR=D.
\]

There is no transpose mismatch on the second pair.

Expansion of the four diagonal tensor terms gives

\[
\begin{aligned}
m_1\otimes m_1&=-(e_0^++e_1^+)/\sqrt2,\\
m_2\otimes m_2&=(e_0^+-e_1^+)/\sqrt2,\\
m_3\otimes m_3&=(e_2^++e_3^+)/\sqrt2,\\
m_4\otimes m_4&=(-e_2^++e_3^+)/\sqrt2.
\end{aligned}
\]

Thus the author’s conversion is exactly

\[
x=\frac1{\sqrt2}
(-d_1+d_2,\,-d_1-d_2,\,d_3-d_4,\,d_3+d_4),
\]

and preserves \(\|x\|^2=\sum_jd_j^2=1\).

Every invariant pure input therefore has the stated normal form

\[
\psi(x)=\sum_{j=0}^3x_je_j^+,\qquad x\in\mathbb R^4,\quad \|x\|=1,
\]

after a physical unitary \(U_1\otimes U_2\otimes U_3\otimes U_4\).

For each actual subset marginal,

\[
(U\rho U^\dagger)_S=U_S\rho_SU_S^\dagger.
\]

Lifting by the identity and summing establishes

\[
H_3(U\rho U^\dagger)=UH_3(\rho)U^\dagger.
\]

Accordingly, the normal-form reduction preserves precisely the spectrum consumed by the Ky Fan bound. It is not a replacement of the physical marginal map by an unrelated normal-form operator.

## 6. Physical partial trace, all error routes, and complete blocks

**Status: SUPPORTED.**  
**Anchors:** S1 lines 279–390.

For a general operator written in blocks on physical qubit \(i\), summing its four Pauli conjugates cancels off-diagonal blocks and gives twice the identity on \(i\) tensored with its partial trace. Hence

\[
I_i\otimes\rho_{\bar i}
=\frac12(\rho+X_i\rho X_i+Y_i\rho Y_i+Z_i\rho Z_i).
\]

The factor \(1/2\) is correct. Summation over the four physical qubits yields

\[
H_3(\rho_x)
=2\rho_x+\frac12\sum_{i=1}^4
\bigl(
|X_i\psi\rangle\langle X_i\psi|
+|Y_i\psi\rangle\langle Y_i\psi|
+|Z_i\psi\rangle\langle Z_i\psi|
\bigr).
\]

All twelve vectors come from this same \(\rho_x\).

Using the author’s actual strings \(w_i\), the complete routes are:

- \(X_i\psi\) into the ordered \(f^+\) basis;
- \(Y_i\psi/i\) into the ordered \(f^-\) basis;
- \(Z_i\psi\) into the ordered \(e^-\) basis.

Their coordinate columns are:

| Physical qubit \(i\) | \(X_i\psi\) | \(Y_i\psi/i\) | \(Z_i\psi\) |
|---|---|---|---|
| 1 | \((x_0,x_1,x_2,x_3)\) | \((x_0,-x_1,-x_2,-x_3)\) | \((x_0,x_1,x_2,x_3)\) |
| 2 | \((x_1,x_0,x_3,x_2)\) | \((-x_1,x_0,-x_3,-x_2)\) | \((x_0,x_1,-x_2,-x_3)\) |
| 3 | \((x_2,x_3,x_0,x_1)\) | \((-x_2,-x_3,x_0,-x_1)\) | \((x_0,-x_1,x_2,-x_3)\) |
| 4 | \((x_3,x_2,x_1,x_0)\) | \((-x_3,-x_2,-x_1,x_0)\) | \((x_0,-x_1,-x_2,x_3)\) |

This reproduces S1’s \(M_X\), \(M_Y=M_X(x_0,-x_1,-x_2,-x_3)\), and \(M_Z\) in full. In particular, the common \(i\) multiplying the \(Y\)-columns is correct and cancels in their outer products.

The four spaces

\[
\operatorname{span}\{e_j^+\},\quad
\operatorname{span}\{e_j^-\},\quad
\operatorname{span}\{f_i^+\},\quad
\operatorname{span}\{f_i^-\}
\]

are mutually orthogonal and together have dimension sixteen. The error blocks occupy the last three designated four-dimensional spaces. On the first space, \(2\rho_x\) has eigenvalue \(2\) along \(\psi(x)\) and **three additional zero eigenvalues**.

For the Hadamard sign matrix

\[
H=\begin{pmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{pmatrix},
\qquad HH^T=4I,
\]

the normalized rows diagonalize \(M_X\). Its four eigenvalues are the signed sums in S1 equation (24). Replacing \(x\) by \((x_0,-x_1,-x_2,-x_3)\) gives exactly equation (25) for \(M_Y\). Also

\[
M_ZM_Z^T=4\operatorname{diag}(x_0^2,x_1^2,x_2^2,x_3^2).
\]

Therefore the **complete** physical spectrum is

\[
\operatorname{spec}H_3(\rho_x)
=\left\{2,\frac{c_1}2,\ldots,\frac{c_{12}}2,0,0,0\right\},
\]

with exactly the twelve \(c\)’s in S1 equations (23)–(25), including all multiplicities.

As a normalization check within this general formula, each error block has trace \(2\), while \(2\rho_x\) has trace \(2\); the total is \(8\), as required by four lifted trace-one marginals.

## 7. Twelve-vector bound and mixed-sector extension

**Status: SUPPORTED.**  
**Anchors:** S1 lines 392–448.

The twelve \(c\)’s have the form

\[
c_v(x)=4|\langle v,x\rangle|^2
\]

for three real orthonormal bases: the coordinate basis, half the even-parity sign vectors in equation (24), and half the odd-parity sign vectors in equation (25).

Within each basis, distinct vectors are orthogonal. Coordinate/sign overlaps have magnitude \(1/2\). Between the two sign bases, the sign patterns differ in an odd number of places, giving unnormalized dot product \(2\) or \(-2\), hence normalized magnitude \(1/2\). Thus every distinct pair in the union satisfies

\[
|\langle u,v\rangle|\le\frac12.
\]

For any three selected members, their Gram matrix obeys

\[
z^TGz
\le \sum_i z_i^2+\sum_{i<j}|z_iz_j|
\le2\sum_i z_i^2.
\]

The last inequality follows from the nonnegativity of the sum of the three squared differences of \(|z_i|\). The corresponding frame operator consequently has norm at most \(2\). It follows, for every unit \(x\), that

\[
c_{(1)}+c_{(2)}+c_{(3)}\le8.
\]

Also every \(c_v\le4\), so the separately displayed eigenvalue \(2\) is always a largest eigenvalue, including ties. Hence

\[
K_4(H_3(\rho_x))
=2+\frac12(c_{(1)}+c_{(2)}+c_{(3)})
\le6,
\]

and \(H_3(\rho_x)\le2I\).

The physical covariance and the complete real pure-state decomposition established above now give

\[
K_4(H_3(\rho))
\le\sum_\ell w_\ell K_4(H_3(\rho_{\psi_\ell}))
\le6
\]

for **every mixed invariant density**. The operator inequality \(H_3(\rho)\le2I\) extends by the same convex decomposition.

This checks the whole assigned sector, not only the displayed normal-form family in its original coordinates.

## 8. Author-specified physical extremizer and common projector

**Status: SUPPORTED.**  
**Anchors:** S1 lines 450–506.

The already specified input is

\[
x_*=(2,1,1,0)/\sqrt6,\qquad
\psi_*=(2e_0^++e_1^++e_2^+)/\sqrt6.
\]

It is normalized and fixed by \(\Theta_4\). Its density is therefore an actual positive trace-one invariant input.

In the declared order, the three groups of \(c\)’s are

\[
\begin{aligned}
c_Z&=(8/3,\,2/3,\,2/3,\,0),\\
c_X&=(8/3,\,2/3,\,2/3,\,0),\\
c_Y&=(0,\,2/3,\,2/3,\,8/3).
\end{aligned}
\]

Thus

\[
\operatorname{spec}H_3(\rho_*)
=\left(2,(4/3)^{\times3},(1/3)^{\times6},0^{\times6}\right),
\]

and its fourth prefix is exactly \(6\).

The author’s four projector vectors are mutually orthonormal because they lie in the distinct spaces \(\psi_*\), \(e^-\), \(f^+\), and \(f^-\). The block formulas give:

- eigenvalue \(2\) on \(\psi_*\);
- eigenvalue \(4/3\) on \(u_Z=e_0^-\);
- eigenvalue \(4/3\) on the all-plus Hadamard vector \(u_X\);
- eigenvalue \(4/3\) on the stated \(u_Y=(f_1^--f_2^--f_3^-+f_4^-)/2\).

Consequently the **same physical rank-four projector** satisfies

\[
\operatorname{Tr}(Q_*\rho_*)=1,\qquad
\operatorname{Tr}(Q_*H_3(\rho_*))=6.
\]

There is no incompatible-projector substitution in the attainability argument.

## 9. Exact channel reduction, sharp output prefix, and reference gap

**Status: SUPPORTED.**  
**Anchors:** S1 lines 102–151 and 508–561.

The one-qubit identity

\[
YX^TY=\operatorname{Tr}(X)I-X
\]

gives the four-qubit inclusion–exclusion formula

\[
\widetilde\rho=I-H_1+H_2-H_3+\rho.
\]

Partial trace commutes with the corresponding spin flip. Hence invariant singleton marginals equal \(I/2\), so \(H_1=2I\), and invariance in the last display gives

\[
H_2=I+H_3.
\]

For \(b=(1-t)/2\), \(a=t+b\), the actual subset expansion is

\[
T_t^{\otimes4}(\rho)
=t^4\rho+t^3bH_3+t^2b^2H_2+tb^3H_1+b^4I.
\]

Substitution yields

\[
T_t^{\otimes4}(\rho)
=t^4\rho+\alpha H_3+\beta I,
\qquad
\alpha=t^2ab,\quad\beta=a^2b^2.
\]

No commutation of \(\rho\) and \(H_3\) is needed for this identity or its general bound.

For every complex orthogonal rank-four projector,

\[
\operatorname{Tr}(QT_t^{\otimes4}(\rho))
\le t^4+6\alpha+4\beta
=\frac{1+4t^2-t^4}{4}.
\]

The displayed extremizer attains this bound with \(Q_*\). Its full output spectrum is

\[
t^4+2\alpha+\beta,\quad
(\tfrac43\alpha+\beta)^{\times3},\quad
(\tfrac13\alpha+\beta)^{\times6},\quad
\beta^{\times6}.
\]

The adjacent differences are \(t^4+\frac23\alpha\), \(\alpha\), and \(\frac13\alpha\), all nonnegative. Thus \(Q_*\) remains a top-four projector throughout \(0\le t\le1\), including degeneracies.

For the product reference, \(K_4(D_t)=a^4+3a^3b\). Subtraction gives

\[
\begin{aligned}
K_4(D_t)-F_4(t)
&=t^3b+5t^2b^2+5tb^3\\
&=tb(t^2+5tb+5b^2)\\
&=\frac{t(1-t)(5-t^2)}8.
\end{aligned}
\]

The sharpness and factorization claims are therefore supported. The gap is strictly positive for every \(0<t<1\).

## 10. Complementary audit: every prefix and both physical branches

**Status: SUPPORTED.**  
**Anchors:** S1 lines 563–666.

I also reconstructed the complementary all-prefix and negative-branch argument rather than leaving those claims outside this review.

For a pure product input, the physical reference layers have eigenvalues determined by Hamming weight:

\[
L_3=(4,1^{\times4},0^{\times11}),\quad
L_2=(6,3^{\times4},1^{\times6},0^{\times5}),\quad
L_1=(4,3^{\times4},2^{\times6},1^{\times4},0).
\]

They share decreasing Hamming-weight order, as does \(D_t\). Thus their prefix expansion in S1 equation (37) is valid.

For one fixed complex rank-\(k\) projector,

\[
q\le1,\quad h_1=2k,\quad h_2=k+h_3,\quad h_3\le m_k,
\]

where \(m_4=6\) and \(m_k=\min(2k,8)\) otherwise. The complete deficit table reconstructs as follows:

| \(k\) | \(m_k\) | \(A_k\) | \(B_k\) | \(C_k\) |
|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 3 | 2 |
| 2 | 4 | 1 | 3 | 3 |
| 3 | 6 | 0 | 3 | 4 |
| 4 | 6 | 1 | 5 | 5 |
| 5 | 8 | 0 | 5 | 6 |
| 6 | 8 | 0 | 5 | 6 |
| 7 | 8 | 0 | 5 | 6 |
| 8 | 8 | 0 | 5 | 6 |
| 9 | 8 | 0 | 5 | 6 |
| 10 | 8 | 0 | 5 | 6 |
| 11 | 8 | 0 | 5 | 6 |
| 12 | 8 | 0 | 4 | 5 |
| 13 | 8 | 0 | 3 | 4 |
| 14 | 8 | 0 | 2 | 3 |
| 15 | 8 | 0 | 1 | 2 |
| 16 | 8 | 0 | 0 | 0 |

Here

\[
A_k=R_3(k)-m_k,\quad
B_k=R_2(k)-k-m_k,\quad
C_k=R_1(k)-2k.
\]

For that same consuming projector,

\[
K_k(D_t)-\operatorname{Tr}(QT_t^{\otimes4}(\rho))
\ge t^4(1-q)+t^3bA_k+t^2b^2B_k+tb^3C_k
\ge0.
\]

Every coefficient is nonnegative. Since \(B_k>0\) for each proper prefix, every proper inequality is strict when \(0<t<1\). At \(t=0\), the output and reference are maximally mixed; at \(t=1\), the pure reference majorizes every density.

Finally,

\[
T_{-t}=\mathcal J\circ T_t,\qquad
T_{-t}^{\otimes4}(\rho)=W[T_t^{\otimes4}(\rho)]^TW,
\quad W=Y^{\otimes4}.
\]

This is full transpose. Because \(W^T=W=W^\dagger\) and \(W^2=I\),

\[
Q'=WQ^TW
\]

is an orthogonal projector of the same rank, and

\[
\operatorname{Tr}(QT_{-t}^{\otimes4}(\rho))
=\operatorname{Tr}(Q'T_t^{\otimes4}(\rho)).
\]

Thus the consuming-side projector transport is correct, and all preceding inequalities apply on the physical negative-retention branch \(t=p-1\le1/3\). Spectral preservation also transports the sharp fourth-prefix example.

## 11. Per-claim disposition and exact ceiling

| Claim | Written disposition |
|---|---|
| \(\Theta_4^2=I\), fixed magic-pair product basis, real invariant pure decomposition | **SUPPORTED** |
| All six physical generator matrices and realization of every required \(SO(4)\) action by pair-local product unitaries | **SUPPORTED** |
| Proper-orientation signed SVD, \(A\mapsto L^TAR\), and the declared real \(x\) conversion | **SUPPORTED** |
| Physical \(H_3\) covariance and coverage of every invariant pure input | **SUPPORTED** |
| Partial-trace factor \(1/2\), all twelve physical error routes, \(Y\)-phase, all blocks and multiplicities | **SUPPORTED** |
| Complete twelve-\(c\) spectrum and three-vector Gram bound | **SUPPORTED** |
| \(K_4(H_3(\rho))\le6\) for every mixed invariant density | **SUPPORTED** |
| Author-specified physical equality input and same rank-four projector | **SUPPORTED** |
| Exact maximum fourth output prefix and exact positive reference gap | **SUPPORTED** |
| All sixteen prefixes, endpoints, arbitrary complex orthogonal projectors, and both physical branches | **SUPPORTED** |
| Unrestricted four-qubit inputs, general blocklength, arbitrary ancillary tensorization | **NOT PROVED; outside the candidate’s claim** |
| Printed-source equivalence, novelty, independent-family/human/kernel acceptance | **NOT ESTABLISHED; not claimed** |

### Final verdict

The fresh candidate closes the previously residual fourth-prefix interval **for the entire mixed spin-flip-invariant four-qubit sector**, and its proof supports

\[
\boxed{
\Phi_p^{\otimes4}(\rho)\prec
\operatorname{diag}\!\left(\frac{1+|1-p|}{2},
                         \frac{1-|1-p|}{2}\right)^{\otimes4}
}
\]

for every actual invariant density and every physical \(0\le p\le4/3\).

This return constitutes **one same-harness written reconstruction**. It is not parent adoption or a substitute for the separately assigned written and finite gates. No unrestricted four-qubit or general-target closure follows, and all genuinely held episodes and consumers remain **NONINPUT**.