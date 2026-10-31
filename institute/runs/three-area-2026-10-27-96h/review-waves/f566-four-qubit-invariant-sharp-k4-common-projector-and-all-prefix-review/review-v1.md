# F566 — WRITTEN review of the invariant-sector sharp fourth prefix

**Disposition: SUPPORTED at the stated invariant-sector scope.**  
**Findings: 0 FATAL / 0 MAJOR / 0 MINOR.**  
**Scientific execution: NOT RUN.**

This is the complete review body for parent materialization as `review-v1.md` in the assigned F566 wave. No repository file was written. This return supplies one same-harness written review, not parent adoption, a finite-execution result, independent-family verification, human verification, or kernel certification.

## 1. Binding, chronology, and exclusions

Before mathematical-body access, I completely read:

- `manifest-v1.json`, lines 1–119;
- `freeze-receipt-v1.json`, lines 1–47;
- the parent dispatch receipt;
- `parent-live-metadata-supply-v1.json` through its ending;
- all twelve listed status-only controls through their endings.

I then delivered a direct administrative pre-body ACK to `agent://Main`. Only afterward did I read the complete literal packet in ordered raw windows of at most twenty lines, from packet line 1 through its final line 742. Mathematical reconstruction began after that complete read.

The frozen bindings are:

| Item | SHA256 |
|---|---|
| Manifest | `7f09068e6465cba5d7862053be5d969e181fde4545952404b47751926a4e3e77` |
| Freeze receipt | `e1f4cb1abd998e7b15e4c5402cf5dbff19c4460bede1458adf3b210abd399c3b` |
| Literal packet | `4bb2db14e2461f4a7f4150e3222f203aa87822da004f0fc05f14402392847efc` |
| S1, complete F558 author candidate | `e300afac40b19341a321be3e9acd84c1d9c81bd10e6f1d3638733087faf3ee51` |
| S2, earlier scoped parent disposition | `7bb4ba23f47f1ab1c22ea37ed22a873f6073718913a0cd8715b3ca3d070d66ca` |

These hashes, byte counts, LF counts, and the clock `2026-10-30T13:31:55-0700 PDT` are **parent-observed metadata**, not my own hash execution or native start-clock observation.

Complete mathematical source coverage was:

- **S1:** logical source lines 1–698, including the final scope and assurance paragraph. The supplied metadata records 697 LF characters.
- **S2:** source lines 1–42, including its final unpaid-scope qualification.

No linked reviewer body, author code, sibling return, excluded source, or held scientific payload was opened. S2’s reported earlier executions were not rerun and are not credited as verification of the present candidate. All held episodes and their proof, method, selection, planning, confidence, and reporting consumers remain NONINPUT.

No new selected parameter, state, word, gauge, or auxiliary instance was introduced. The only explicit sharp input evaluated below is the author’s already specified \(x_*\) and its specified physical projector. No program, CAS, interpreter, solver, enumeration, test, build, formatter, external-model CLI, or scientific replay was used.

## 2. Exact scope reviewed

For an actual four-qubit density, define the lifted physical marginal sums
\[
H_j(\rho)=\sum_{|S|=j}\rho_S\otimes I_{S^c}.
\]
The assigned sector is
\[
\rho\ge0,\qquad \operatorname{Tr}\rho=1,\qquad
\widetilde\rho:=Y^{\otimes4}\rho^T Y^{\otimes4}=\rho.
\]

The candidate’s principal new assertion is
\[
K_4(H_3(\rho))\le6
\]
throughout this **entire mixed invariant sector**, with an actual attainable equality case.

For
\[
t=|1-p|,\qquad a=\frac{1+t}{2},\qquad b=\frac{1-t}{2},
\qquad D_t=\operatorname{diag}(a,b)^{\otimes4},
\]
the resulting exact sector maximum is
\[
\max_{\rho=\widetilde\rho}
K_4\!\left(\Phi_p^{\otimes4}(\rho)\right)
=\frac{1+4t^2-t^4}{4}.
\]
The claimed fourth-prefix reference gap is
\[
K_4(D_t)-\frac{1+4t^2-t^4}{4}
=\frac{t(1-t)(5-t^2)}8.
\]

The all-prefix claim is
\[
\Phi_p^{\otimes4}(\rho)\prec D_t
\]
for every such mixed density, every physical \(0\le p\le4/3\), and all sixteen prefixes. The following reconstruction supports those assertions at precisely that scope.

## 3. Actual invariant-sector identities and channel consumer

**Source anchors: S1 lines 102–151.**

For one qubit,
\[
\mathcal J(X)=YX^TY=\operatorname{Tr}(X)I-X.
\]
Expanding the four tensor factors, with \(\operatorname{Tr}\rho=1\), gives
\[
\widetilde\rho=I-H_1+H_2-H_3+\rho.
\]

The reduced one-qubit density of an invariant input is itself invariant under the one-qubit spin flip. Hence
\[
\rho_i=I/2,\qquad H_1=2I_{16}.
\]
Substituting \(\widetilde\rho=\rho\) into the preceding expansion gives
\[
H_2=I_{16}+H_3.
\]
These are identities of the actual compatible lifted marginals of the same input, not separately optimized marginal spectra.

Also,
\[
H_3\ge0,\qquad \operatorname{Tr}H_3=4\cdot2=8.
\]

On the nonnegative-retention branch, write
\[
T_t(X)=tX+b\operatorname{Tr}(X)I.
\]
Its actual tensor expansion is
\[
T_t^{\otimes4}(\rho)
=t^4\rho+t^3bH_3+t^2b^2H_2+tb^3H_1+b^4I.
\]
Each subset already occurs once in \(H_j\); no additional binomial coefficient belongs outside those sums.

Using the invariant-sector identities,
\[
\begin{aligned}
T_t^{\otimes4}(\rho)
&=t^4\rho+(t^3b+t^2b^2)H_3
 +(t^2b^2+2tb^3+b^4)I\\
&=t^4\rho+\alpha H_3+\beta I,
\end{aligned}
\]
where
\[
\alpha=t^2ab,\qquad \beta=a^2b^2,
\qquad a=t+b.
\]
This identity does not require \(\rho\) and \(H_3\) to commute.

**Status: SUPPORTED.**

## 4. Complete mixed-state reduction and physical local normal form

**Source anchors: S1 lines 156–277.**

### 4.1 Real invariant pure decomposition

Let
\[
\Theta_4=Y^{\otimes4}\mathcal K.
\]
Its square is \(+I\), not \(-I\). Thus no four-qubit Kramers pairing is available or needed.

Use the author’s two-qubit basis
\[
m_1=i\Phi^+,\quad m_2=\Phi^-,
\quad m_3=\Psi^+,\quad m_4=i\Psi^-.
\]
Every \(m_j\) is fixed by \(Y^{\otimes2}\mathcal K\), so every
\[
m_j^{12}\otimes m_k^{34}
\]
is fixed by \(\Theta_4\). In this sixteen-dimensional orthonormal basis, \(\Theta_4\) is coefficientwise conjugation.

Consequently, an invariant Hermitian density has a real symmetric positive matrix in this basis. Real spectral decomposition therefore supplies
\[
\rho=\sum_\ell w_\ell|\psi_\ell\rangle\langle\psi_\ell|,
\quad
w_\ell\ge0,\quad \sum_\ell w_\ell=1,\quad
\Theta_4\psi_\ell=\psi_\ell.
\]
This covers all mixed invariant densities, including degeneracies.

### 4.2 The six generator matrices are physical

Direct application of the six specified physical generators gives the following complete action table:

| Generator | Image of \(m_1\) | Image of \(m_2\) | Image of \(m_3\) | Image of \(m_4\) |
|---|---|---|---|---|
| \(-iX\otimes I\) | \(m_3\) | \(m_4\) | \(-m_1\) | \(-m_2\) |
| \(-iI\otimes X\) | \(m_3\) | \(-m_4\) | \(-m_1\) | \(m_2\) |
| \(-iZ\otimes I\) | \(m_2\) | \(-m_1\) | \(-m_4\) | \(m_3\) |
| \(-iI\otimes Z\) | \(m_2\) | \(-m_1\) | \(m_4\) | \(-m_3\) |
| \(-iY\otimes I\) | \(-m_4\) | \(m_3\) | \(-m_2\) | \(m_1\) |
| \(-iI\otimes Y\) | \(m_4\) | \(m_3\) | \(-m_2\) | \(-m_1\) |

With the author’s convention \(S_{jk}m_j=m_k\) and \(S_{jk}m_k=-m_j\), these are exactly
\[
\begin{array}{ll}
S_{13}+S_{24},&S_{13}-S_{24},\\
S_{12}-S_{34},&S_{12}+S_{34},\\
-S_{14}+S_{23},&S_{14}+S_{23}.
\end{array}
\]

For each axis, the two physical generators act on different qubits and commute. Their half-sums and half-differences therefore exponentiate to each individual plane rotation. Products of these rotations realize every \(SO(4)\) matrix. The construction uses only products of single-qubit \(SU(2)\) unitaries, not arbitrary entangling two-qubit unitaries.

### 4.3 Proper-orthogonal SVD supplies the asserted form

For an invariant pure vector, its coefficient matrix is real:
\[
|\psi\rangle=\sum_{j,k}A_{jk}m_j^{12}\otimes m_k^{34},
\qquad A\in\mathbb R^{4\times4},\quad \|A\|_F=1.
\]
A real SVD can have both orthogonal factors made proper by absorbing their reflection signs into the real diagonal entries:
\[
A=L\operatorname{diag}(d_1,d_2,d_3,d_4)R^T,
\qquad L,R\in SO(4).
\]
The physical actions \(L^T\) on pair \(12\) and \(R^T\) on pair \(34\) transform the coefficient matrix to the displayed diagonal.

The Bell-product expansions give
\[
\begin{aligned}
m_1\otimes m_1&=-(e_0^++e_1^+)/\sqrt2,\\
m_2\otimes m_2&=(e_0^+-e_1^+)/\sqrt2,\\
m_3\otimes m_3&=(e_2^++e_3^+)/\sqrt2,\\
m_4\otimes m_4&=(-e_2^++e_3^+)/\sqrt2.
\end{aligned}
\]
Thus the transformed state is exactly
\[
|\psi(x)\rangle=\sum_{j=0}^3x_je_j^+,
\qquad x\in\mathbb R^4,\quad \|x\|=1,
\]
with
\[
x_0=\frac{-d_1+d_2}{\sqrt2},\quad
x_1=\frac{-d_1-d_2}{\sqrt2},\quad
x_2=\frac{d_3-d_4}{\sqrt2},\quad
x_3=\frac{d_3+d_4}{\sqrt2}.
\]
The conversion is orthogonal and preserves the squared norm.

Finally, for every physical product unitary,
\[
H_3(U\rho U^\dagger)=UH_3(\rho)U^\dagger.
\]
This follows by tracing and lifting on the actual tensor positions. Therefore the normal-form reduction preserves the spectrum being bounded.

**Status: SUPPORTED for every invariant pure state, with a complete mixed invariant decomposition.**

## 5. Actual physical error blocks, including the \(Y\)-signs

**Source anchors: S1 lines 279–390.**

The physical one-qubit Pauli twirl gives
\[
I_i\otimes(\rho_x)_{\bar i}
=\frac12\left(\rho_x+X_i\rho_xX_i
+Y_i\rho_xY_i+Z_i\rho_xZ_i\right).
\]
Summing the four actual three-body marginal lifts yields
\[
H_3(\rho_x)
=2\rho_x+\frac12\sum_{i=1}^4
\left(
|X_i\psi\rangle\langle X_i\psi|
+|Y_i\psi\rangle\langle Y_i\psi|
+|Z_i\psi\rangle\langle Z_i\psi|
\right).
\]

These twelve vectors are generated from the same physical state.

The \(X\), \(Y\), and \(Z\) vectors lie, respectively, in the mutually orthogonal spaces with bases \(f_i^+\), \(f_i^-\), and \(e_j^-\). All three spaces are orthogonal to the even-complement symmetric space containing \(\psi(x)\).

On the ordered \(f_i^+\) basis,
\[
M_X=
\begin{pmatrix}
x_0&x_1&x_2&x_3\\
x_1&x_0&x_3&x_2\\
x_2&x_3&x_0&x_1\\
x_3&x_2&x_1&x_0
\end{pmatrix}.
\]
The nontrivial \(x_1,x_2,x_3\) permutations are, respectively,
\((12)(34)\), \((13)(24)\), and \((14)(23)\), obtained by applying the physical bit flips to the displayed even-complement pairs.

For \(Y_i\), the weight-zero/four pair contributes \(if_i^-\), whereas each weight-two complement pair contributes minus \(i\) times the corresponding \(f^-_j\). Therefore the physical column matrix is
\[
iM_X(x_0,-x_1,-x_2,-x_3).
\]
The overall \(i\) cancels in the outer-product block. This verifies the author’s \(M_Y\), including the relative signs.

For \(Z_i\), the signs of the four even-complement representatives give
\[
M_Z=\operatorname{diag}(x_0,x_1,x_2,x_3)
\begin{pmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{pmatrix}.
\]
Consequently,
\[
M_ZM_Z^T=4\operatorname{diag}(x_0^2,x_1^2,x_2^2,x_3^2).
\]

The other two matrices are diagonalized by the four Hadamard sign vectors. Hence the complete actual spectrum is
\[
\operatorname{spec}H_3(\rho_x)
=\left\{2,\frac{c_1}{2},\ldots,\frac{c_{12}}2,0,0,0\right\},
\]
with exactly the twelve \(c\)’s in S1 equations (23)–(25). The three additional zeros come from the orthogonal complement of \(\psi(x)\) inside \(\operatorname{span}\{e_j^+\}\).

The derivation accounts for all sixteen dimensions and every physical marginal contribution. It does not replace actual marginals by an independently chosen frame or spectral relaxation.

**Status: SUPPORTED.**

## 6. Three-basis Gram inequality and the sharp sector bound

**Source anchors: S1 lines 392–448.**

The twelve quantities have the common form
\[
c_v(x)=4|\langle v,x\rangle|^2
\]
for the union of:

1. the coordinate basis;
2. the four normalized sign vectors in equation (24);
3. the four normalized sign vectors in equation (25).

Each sign quartet is an orthonormal basis. Within a quartet, distinct sign rows differ in two positions, so their dot product is zero. Across the two sign quartets, the rows differ in one or three positions, producing normalized dot product \(1/2\) or \(-1/2\). Coordinate/sign overlaps also have absolute value \(1/2\).

Thus any three distinct frame vectors have Gram matrix \(G\) with diagonal entries \(1\) and off-diagonal entries of absolute value at most \(1/2\). For arbitrary real \(z\),
\[
\begin{aligned}
z^TGz
&\le\sum_i z_i^2+\sum_{i<j}|z_iz_j|\\
&\le2\sum_i z_i^2.
\end{aligned}
\]
The second inequality follows by summing
\(2|z_iz_j|\le z_i^2+z_j^2\) over the three pairs.

Therefore \(G\le2I\). Equivalently, the associated three-column frame operator has norm at most \(2\), giving
\[
\sum_{i=1}^3|\langle v_i,x\rangle|^2\le2
\qquad(\|x\|=1).
\]
Selecting the labels of the three largest \(c\)’s proves
\[
c_{(1)}+c_{(2)}+c_{(3)}\le8.
\]

Each individual \(c_v\le4\). The explicit eigenvalue \(2\) is therefore always among the largest eigenvalues, including degeneracies, and
\[
K_4(H_3(\rho_x))
=2+\frac12(c_{(1)}+c_{(2)}+c_{(3)})
\le6.
\]
The same spectrum gives \(0\le H_3(\rho_x)\le2I\).

For an arbitrary mixed invariant density, apply the physical covariance to each pure component and then use linearity of \(H_3\) and Ky Fan convexity:
\[
\begin{aligned}
K_4(H_3(\rho))
&\le\sum_\ell w_\ell
K_4\!\left(H_3(|\psi_\ell\rangle\langle\psi_\ell|)\right)\\
&\le6.
\end{aligned}
\]
Likewise \(H_3(\rho)\le2I\) extends by convexity of the operator inequality.

The real coordinates here describe a normal form for the **state**. They impose no realness restriction on consuming projectors. The spectral Ky Fan bound applies to every complex orthogonal rank-four projector.

**Status: SUPPORTED throughout the entire mixed invariant sector.**

## 7. Author’s actual extremizer and common-projector sharpness

**Source anchors: S1 lines 450–506.**

Use precisely the author’s specified input:
\[
x_*=\frac{(2,1,1,0)}{\sqrt6},
\qquad
|\psi_*\rangle=\frac{2e_0^++e_1^++e_2^+}{\sqrt6}.
\]
Its computational amplitudes are
\[
|\psi_*\rangle
=\frac{|0000\rangle+|1111\rangle}{\sqrt3}
+\frac{|0011\rangle+|1100\rangle+|0101\rangle+|1010\rangle}
{\sqrt{12}}.
\]
The squared amplitudes sum to one. Its even-complement symmetric terms are fixed by \(\Theta_4\), so this is an actual normalized invariant pure input.

Substituting this author-specified \(x_*\) into the three displayed bases gives:

| Basis | Four \(c\)-values in displayed order |
|---|---|
| Coordinate | \(8/3,\ 2/3,\ 2/3,\ 0\) |
| Equation (24) | \(8/3,\ 2/3,\ 2/3,\ 0\) |
| Equation (25) | \(0,\ 2/3,\ 2/3,\ 8/3\) |

Therefore
\[
\operatorname{spec}H_3(\rho_*)
=\left(2,(4/3)^{\times3},(1/3)^{\times6},0^{\times6}\right).
\]

The specified vectors
\[
\psi_*,\qquad e_0^-,
\qquad \frac{f_1^++f_2^++f_3^++f_4^+}{2},
\qquad \frac{f_1^--f_2^--f_3^-+f_4^-}{2}
\]
are normalized and mutually orthogonal, lying in the four orthogonal spaces already identified.

The \(Z\)-vector has eigenvalue
\[
2x_0^2=4/3.
\]
The specified \(X\)- and \(Y\)-vectors are Hadamard eigenvectors whose corresponding error-matrix eigenvalues have squared magnitude \(8/3\); the factor \(1/2\) in the actual \(H_3\) blocks gives \(4/3\) in each case. The vector \(\psi_*\) has \(H_3\)-eigenvalue \(2\).

Thus the author’s rank-four projector \(Q_*\) satisfies simultaneously
\[
\operatorname{Tr}(Q_*\rho_*)=1,
\qquad
\operatorname{Tr}(Q_*H_3(\rho_*))=2+3\cdot\frac43=6.
\]

This is an actual common-projector certificate, not equality in incompatible independent marginal optimizations. It proves attainability of the universal bound.

**Status: SUPPORTED.**

## 8. Exact fourth output maximum, ordering, and reference gap

**Source anchors: S1 lines 508–561.**

For any complex rank-four orthogonal projector \(Q\), let
\[
q=\operatorname{Tr}(Q\rho),\qquad
h_3=\operatorname{Tr}(QH_3(\rho)).
\]
The actual output identity gives
\[
\operatorname{Tr}[QT_t^{\otimes4}(\rho)]
=t^4q+\alpha h_3+4\beta
\le t^4+6\alpha+4\beta.
\]
All coefficients used in this inequality are nonnegative.

Since \(ab=(1-t^2)/4\),
\[
t^4+6\alpha+4\beta
=\frac{1+4t^2-t^4}{4}.
\]

For the actual sharp input, \(\rho_*\) is the projector onto the \(H_3\)-eigenvector of eigenvalue \(2\). The complete output spectrum is therefore
\[
\begin{array}{c|c}
\text{Eigenvalue}&\text{Multiplicity}\\ \hline
t^4+2\alpha+\beta&1\\
\frac43\alpha+\beta&3\\
\frac13\alpha+\beta&6\\
\beta&6
\end{array}
\]
and its successive differences are
\[
t^4+\frac23\alpha,\qquad
\alpha,\qquad
\frac13\alpha.
\]
They are nonnegative on \(0\le t\le1\). Thus \(Q_*\) is a top-four projector throughout the full interval, with endpoint degeneracies allowed. It attains the bound simultaneously in \(q\) and \(h_3\).

This establishes an exact maximum over the whole invariant sector, not merely an upper bound.

For the reference, the decreasing spectrum has one \(a^4\) term followed by four \(a^3b\) terms, so
\[
K_4(D_t)=a^4+3a^3b.
\]
Subtracting the exact sector maximum yields
\[
\begin{aligned}
K_4(D_t)-F_4(t)
&=t^3b+5t^2b^2+5tb^3\\
&=tb(t^2+5tb+5b^2)\\
&=\frac{t(1-t)(5-t^2)}8.
\end{aligned}
\]
This is strictly positive when \(0<t<1\) and zero at the two stated endpoints.

**Status: SUPPORTED, including exact attainability and spectral co-ordering.**

## 9. Complete sixteen-prefix physical deficit table

**Source anchors: S1 lines 563–641.**

For the pure product reference, a computational basis vector of Hamming weight \(w\) has layer eigenvalues
\[
\binom{4-w}{3},\qquad
\binom{4-w}{2},\qquad
4-w.
\]
These reproduce the stated \(L_3,L_2,L_1\), in the same decreasing Hamming-weight order as \(D_t\).

Their cumulative prefixes, together with the universal \(H_3\) bounds used by the candidate, are:

| \(k\) | \(R_3(k)\) | \(R_2(k)\) | \(R_1(k)\) | \(m_k\) | \(A_k\) | \(B_k\) | \(C_k\) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 6 | 4 | 2 | 2 | 3 | 2 |
| 2 | 5 | 9 | 7 | 4 | 1 | 3 | 3 |
| 3 | 6 | 12 | 10 | 6 | 0 | 3 | 4 |
| 4 | 7 | 15 | 13 | 6 | 1 | 5 | 5 |
| 5 | 8 | 18 | 16 | 8 | 0 | 5 | 6 |
| 6 | 8 | 19 | 18 | 8 | 0 | 5 | 6 |
| 7 | 8 | 20 | 20 | 8 | 0 | 5 | 6 |
| 8 | 8 | 21 | 22 | 8 | 0 | 5 | 6 |
| 9 | 8 | 22 | 24 | 8 | 0 | 5 | 6 |
| 10 | 8 | 23 | 26 | 8 | 0 | 5 | 6 |
| 11 | 8 | 24 | 28 | 8 | 0 | 5 | 6 |
| 12 | 8 | 24 | 29 | 8 | 0 | 4 | 5 |
| 13 | 8 | 24 | 30 | 8 | 0 | 3 | 4 |
| 14 | 8 | 24 | 31 | 8 | 0 | 2 | 3 |
| 15 | 8 | 24 | 32 | 8 | 0 | 1 | 2 |
| 16 | 8 | 24 | 32 | 8 | 0 | 0 | 0 |

Here
\[
A_k=R_3(k)-m_k,\quad
B_k=R_2(k)-k-m_k,\quad
C_k=R_1(k)-2k,
\]
and
\[
m_4=6,\qquad m_k=\min(2k,8)\quad(k\ne4).
\]
Thus the newly repaired fourth row is exactly \((1,5,5)\), as asserted.

For one fixed complex rank-\(k\) projector \(Q\), the actual same-input relations are
\[
q\le1,\qquad h_1=2k,\qquad h_2=k+h_3,\qquad h_3\le m_k.
\]
Subtracting its physical output expectation from the reference prefix gives
\[
\begin{aligned}
K_k(D_t)-\operatorname{Tr}[QT_t^{\otimes4}(\rho)]
={}&t^4(1-q)+t^3b(R_3-h_3)\\
&+t^2b^2(R_2-k-h_3)+tb^3(R_1-2k)\\
\ge{}&t^4(1-q)+t^3bA_k+t^2b^2B_k+tb^3C_k\\
\ge{}&0.
\end{aligned}
\]

Every coefficient in every row is nonnegative. At every proper prefix, \(B_k>0\); since \(t^2b^2>0\) for \(0<t<1\), every proper prefix inequality is strict in that open interval.

At \(t=0\), the actual output and reference are both \(I/16\). At \(t=1\), the pure reference spectrum majorizes every density. The proof does not divide by a parameter or require a nonzero spectral gap, so neither endpoint is lost.

**Status: SUPPORTED for all sixteen prefixes.**

## 10. Negative branch and arbitrary complex consuming projectors

**Source anchors: S1 lines 643–666.**

The one-qubit identity is
\[
T_{-t}=\mathcal J\circ T_t.
\]
On all four physical qubits, with \(W=Y^{\otimes4}\),
\[
T_{-t}^{\otimes4}(\rho)
=W[T_t^{\otimes4}(\rho)]^T W.
\]
This is a full transpose of the complete output, not a partial transpose.

Here
\[
W^T=W=W^\dagger,\qquad W^2=I.
\]
For every complex orthogonal projector \(Q\),
\[
\begin{aligned}
\operatorname{Tr}\!\left[QW A^T W\right]
&=\operatorname{Tr}\!\left[(WQW)^T A\right]\\
&=\operatorname{Tr}\!\left[WQ^TW\,A\right].
\end{aligned}
\]
Thus the correct transported projector is
\[
Q'=WQ^TW.
\]
Transpose preserves the rank and idempotence of \(Q\), and \(Q^T\) is Hermitian when \(Q\) is Hermitian. Conjugation by \(W\) preserves these properties. Therefore \(Q'\) is a complex orthogonal projector of the same rank.

Every preceding fixed-projector inequality consequently applies to the physical negative-retention branch. Full-transpose conjugation also preserves the complete sharp-output spectrum. The transported author projector supplies the corresponding sharp top-four projector on that branch.

The physical parameter ranges are correctly matched:
\[
p\le1:\ t=1-p\in[0,1],\qquad
1<p\le4/3:\ t=p-1\in(0,1/3].
\]

**Status: SUPPORTED over the entire physical interval \(0\le p\le4/3\).**

## 11. Boundary and consumer audit

The complete physical chain is present:

| Produced object or bound | Actual consumer | Review result |
|---|---|---|
| Real invariant decomposition | Pure-state spectral reduction and mixed convex extension | Complete |
| Pairwise \(SO(4)\) action | Physical one-qubit-unitary normal form | Complete; no entangling substitute |
| \(M_X,M_Y,M_Z\) | Actual Pauli-twirl blocks of \(H_3\) | Complete, including \(Y\)-signs |
| Twelve frame quantities | Complete sixteen-dimensional \(H_3\) spectrum | Complete, with all zeros and multiplicities |
| Three-vector Gram bound | Three largest \(c\)’s and \(K_4(H_3)\) | Complete |
| Sharp physical input and \(Q_*\) | Same-input values \(q=1,h_3=6\) | Complete |
| \(K_4(H_3)\le6\) | Actual output identity \(t^4\rho+\alpha H_3+\beta I\) | Complete |
| Sharp output eigenvalues | Top-four ordering for all \(t\), including endpoints | Complete |
| Updated \(m_4=6\) | Full sixteen-row physical deficit table | Complete |
| Negative-retention output | Full-transpose projector transport | Complete for arbitrary complex projectors |

In particular, the frame calculation is not standing alone as a weak shadow witness: its connection to the actual physical marginals is explicitly established, and sharpness is certified by an actual state and a single actual projector.

## 12. Per-claim disposition and scope ceiling

| Claim | Status |
|---|---|
| Invariant-sector marginal identities and exact channel reduction | **SUPPORTED** |
| Physical local-unitary normal form for every invariant pure input | **SUPPORTED** |
| Exact compatible \(H_3\) error blocks and full spectrum | **SUPPORTED** |
| Three-basis Gram argument and \(K_4(H_3)\le6\) | **SUPPORTED** |
| Extension to every mixed invariant density | **SUPPORTED** |
| Specified physical equality input and common projector | **SUPPORTED** |
| Exact maximum fourth output prefix | **SUPPORTED** |
| Exact positive product-reference fourth-prefix gap | **SUPPORTED** |
| Complete all-prefix table and interior strictness | **SUPPORTED** |
| Endpoint treatment and physical negative branch | **SUPPORTED** |
| Unrestricted inputs with \(\rho\ne\widetilde\rho\) | **NOT PROVED; outside accepted scope** |
| General blocklength or arbitrary ancillary tensorization | **NOT PROVED; outside accepted scope** |
| Printed-source equivalence or novelty | **INCONCLUSIVE; not investigated here** |
| New finite-execution, independent-family, human, or kernel assurance | **NOT PERFORMED** |

S2 records an earlier invariant-sector result with an unpaid fourth-prefix interval. The present reconstruction supports closing that interval for the entire invariant sector directly from the fresh S1 proof. It does not infer unrestricted four-qubit closure from the Dicke orbit or any other subclass. S2’s separate Dicke-orbit, hull-separation, and historical finite-check assertions are not newly adjudicated by this duty.

## Findings and verdict

**No reportable mathematical defect found: 0 FATAL / 0 MAJOR / 0 MINOR.**

**overall_correctness: correct**

**explanation:** The candidate supplies a complete written proof of the sharp bound \(K_4(H_3)\le6\) for every mixed spin-flip-invariant four-qubit density, an actual common-projector extremizer, and the claimed exact fourth-output maximum and reference gap. The full physical sixteen-prefix argument, endpoint treatment, and arbitrary-complex-projector negative-branch transport are supported; unrestricted four-qubit closure and all additional assurance or novelty claims remain excluded.

**confidence: 0.98**