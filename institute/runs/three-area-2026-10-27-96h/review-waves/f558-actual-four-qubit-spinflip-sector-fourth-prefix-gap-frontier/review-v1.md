# Author candidate v1 — Sharp fourth-prefix bound for every spin-flip-invariant four-qubit density

**Status: GENERALAUTHOR / FRESH WRITTEN PROOF CANDIDATE / NOT INDEPENDENTLY ACCEPTED.**

**Materialization:** Complete body for `author-candidate-v1.md` in F558, returned for Main materialization under the read-only runtime assignment. No repository file was written.

**Scientific execution:** NOT RUN. No program, numerical experiment, CAS, solver, build, test, external-model CLI or new public-source inspection was used. All mathematical calculations below are exact written algebra.

## 1. Result and exact target relation

Let
\[
\Phi_p(X)=(1-p)X+\frac p2\operatorname{Tr}(X)I_2,
\qquad 0\le p\le\frac43,
\]
and put
\[
t=|1-p|,\qquad a=\frac{1+t}{2},\qquad b=\frac{1-t}{2},
\qquad D_t=\operatorname{diag}(a,b)^{\otimes4}.
\]
For an actual four-qubit density define, on the indicated physical tensor positions,
\[
H_j(\rho)=\sum_{|S|=j}\rho_S\otimes I_{S^c}.
\]

This candidate proves the following scoped statements.

### Candidate theorem

For every actual density
\[
\rho\ge0,\qquad \operatorname{Tr}\rho=1,\qquad
\widetilde\rho:=Y^{\otimes4}\rho^T Y^{\otimes4}=\rho,
\]
one has the **sharp compatible-layer bound**
\[
\boxed{K_4(H_3(\rho))\le6.}
\tag{1}
\]

Consequently, for every physical \(p\), every complex orthogonal rank-four projector \(Q\), and the **same** actual \(\rho\),
\[
\boxed{
\operatorname{Tr}[Q\Phi_p^{\otimes4}(\rho)]
\le F_4(t):=\frac{1+4t^2-t^4}{4}.
}
\tag{2}
\]
This is sharp over the entire invariant sector. Its exact difference from the product-reference fourth prefix is
\[
\boxed{
K_4(D_t)-F_4(t)
=\frac{t(1-t)(5-t^2)}8.
}
\tag{3}
\]
The difference is strictly positive for \(0<t<1\).

Together with the complete common-projector table below, this proves
\[
\boxed{\Phi_p^{\otimes4}(\rho)\prec D_t}
\tag{4}
\]
for **every mixed spin-flip-invariant four-qubit density, every physical \(p\), and all sixteen prefixes**.

Thus the previously unpaid invariant-sector fourth-prefix interval
\[
\frac{\sqrt{29}-2}{5}<t<1
\]
is covered by this written candidate. The argument does not merely make the earlier negative relaxation less negative: it establishes a sharp inequality for actual compatible marginal layers and gives an actual common-projector extremizer.

**Not claimed:** unrestricted four-qubit inputs with \(\widetilde\rho\ne\rho\), general blocklength, arbitrary ancillary tensorization, source equivalence, novelty, independent-family/human/kernel verification, or parent acceptance.

## 2. Read chronology and permissions

Before mathematical-body access, I completely read:

- the F558 manifest, LF 1–129;
- the freeze receipt, LF 1–60;
- all twelve declared status/permission controls and their endings;
- the parent-live-metadata supply and dispatch receipt.

I then delivered a **direct pre-body ACK to `agent://Main`**. Only afterward I read the entire literal packet through ordered raw ranges of at most twenty LF, ending at packet LF 606. Complete source coverage was:

- S1: logical source lines 1–42;
- S2: logical source lines 1–523;
- S3: logical source lines 1–39.

Fresh derivation began only after that complete read.

The following metadata are **parent-attributed observations**, not my own hashing or native clock execution:

- Manifest SHA256: `9053932e8e8e486c58d52eefe67b81f4f8f96b41148ec04a8270ed37c544d731`.
- Freeze-receipt SHA256: `4df6199136cb408b2ae96038f8b9d9e7dd08624fe3d75c0a0adb0f4862db69fe`.
- Packet SHA256: `23627c2faf36c4f592173d98e74222b543106f703925d403b27634ebe2c5568e`.
- Parent metadata clock: `2026-10-30T13:14:09-0700 PDT`.

S2 was read as candidate material, not silently adopted as an accepted premise. The load-bearing mathematics used below is reconstructed explicitly. S3 supplies context only; no three-qubit-to-four-qubit tensorization is imported.

All held episodes and all their method, selection, planning, confidence, proof and reporting consumers remain **NONINPUT**. No linked sibling return, held scientific payload or excluded diagnostic record was opened. No clean-cognition certificate is asserted.

## 3. Exact invariant-sector identities

For one qubit,
\[
\mathcal J(X):=YX^TY=\operatorname{Tr}(X)I_2-X.
\tag{5}
\]
Tensor expansion gives, for four qubits,
\[
\widetilde\rho=I-H_1+H_2-H_3+\rho.
\tag{6}
\]
Partial trace commutes with the corresponding spin flip. Hence invariant \(\rho\) has
\[
\rho_i=I_2/2,\qquad H_1=2I_{16}.
\]
Using \(\widetilde\rho=\rho\) in (6),
\[
\boxed{H_2=I_{16}+H_3.}
\tag{7}
\]
Also,
\[
H_3\ge0,\qquad \operatorname{Tr}H_3=8.
\tag{8}
\]

For
\[
T_t(X)=tX+b\operatorname{Tr}(X)I_2,
\]
the actual subset expansion is
\[
T_t^{\otimes4}(\rho)
=t^4\rho+t^3bH_3+t^2b^2H_2+tb^3H_1+b^4I.
\tag{9}
\]
There are no additional binomial factors outside these subset sums.

Substituting (7) and \(H_1=2I\), and using \(t+b=a\), gives the particularly useful exact identity
\[
\boxed{
T_t^{\otimes4}(\rho)
=t^4\rho+\alpha H_3+\beta I,
\qquad
\alpha=t^2ab,\quad \beta=a^2b^2.
}
\tag{10}
\]
This holds for mixed invariant densities, without any commutation assumption between \(\rho\) and \(H_3\).

The new task is therefore to bound the actual compatible \(H_3\), rather than independently replacing
\(\operatorname{Tr}(Q\rho)\) by \(1\) and \(\operatorname{Tr}(QH_3)\) by \(8\).

## 4. Reduction of invariant mixed densities to invariant pure densities

Let
\[
\Theta_4=Y^{\otimes4}\mathcal K.
\]
Here
\[
\Theta_4^2=+I,
\]
not \(-I\). No four-qubit Kramers pairing is used.

Consider the two-qubit orthonormal basis
\[
m_1=i\Phi^+,\qquad m_2=\Phi^-,
\qquad m_3=\Psi^+,\qquad m_4=i\Psi^-,
\]
where
\[
\Phi^\pm=(|00\rangle\pm|11\rangle)/\sqrt2,\qquad
\Psi^\pm=(|01\rangle\pm|10\rangle)/\sqrt2.
\]
Every \(m_j\) is fixed by \(Y^{\otimes2}\mathcal K\). Therefore every product
\[
m_j^{12}\otimes m_k^{34}
\]
is fixed by \(\Theta_4\).

In this sixteen-dimensional basis, \(\Theta_4\) is coefficientwise complex conjugation. An invariant Hermitian density is consequently a **real symmetric positive matrix**. Its real spectral decomposition gives
\[
\rho=\sum_\ell w_\ell|\psi_\ell\rangle\langle\psi_\ell|,
\qquad
w_\ell\ge0,\quad \sum_\ell w_\ell=1,
\qquad \Theta_4\psi_\ell=\psi_\ell.
\tag{11}
\]
Thus it suffices to prove (1) for invariant pure states and then use linearity of \(H_3\) and convexity of \(K_4\).

## 5. Physical local-unitary normal form for an invariant pure state

This section proves the required normal form rather than assuming a classification theorem.

### 5.1 Local two-qubit actions realize every real \(SO(4)\) rotation

On the ordered basis \(m_1,\ldots,m_4\), let \(S_{jk}\), \(j<k\), send
\[
m_j\mapsto m_k,\qquad m_k\mapsto-m_j
\]
and annihilate the other two basis vectors.

Direct application of the physical one-qubit generators gives:

| Physical generator on the pair | Real matrix in the \(m\)-basis |
|---|---|
| \(-iX\otimes I\) | \(S_{13}+S_{24}\) |
| \(-iI\otimes X\) | \(S_{13}-S_{24}\) |
| \(-iZ\otimes I\) | \(S_{12}-S_{34}\) |
| \(-iI\otimes Z\) | \(S_{12}+S_{34}\) |
| \(-iY\otimes I\) | \(-S_{14}+S_{23}\) |
| \(-iI\otimes Y\) | \(S_{14}+S_{23}\) |

For each axis, the two physical generators commute because they act on different qubits. Their sums and differences therefore realize every elementary rotation
\[
\exp(\theta S_{jk})
\]
as a product of physical one-qubit \(SU(2)\) rotations. Every real \(SO(4)\) matrix is a product of these elementary plane rotations, for example by Givens elimination. Hence **every \(SO(4)\) matrix in this basis is realized by a physical product unitary on the pair**.

No entangling two-qubit unitary is introduced.

### 5.2 Real singular-value decomposition

Write an invariant pure vector as
\[
|\psi\rangle=\sum_{j,k=1}^4 A_{jk}\,
m_j^{12}\otimes m_k^{34},
\qquad A\in\mathbb R^{4\times4},
\qquad \|A\|_F=1.
\tag{12}
\]
A real singular-value decomposition, with possible reflection signs absorbed into the diagonal, gives
\[
A=L\,\operatorname{diag}(d_1,d_2,d_3,d_4)\,R^T,
\qquad L,R\in SO(4),\qquad d_j\in\mathbb R.
\tag{13}
\]
The preceding construction realizes \(L^T\) on qubits \(1,2\) and \(R^T\) on qubits \(3,4\), each using only physical one-qubit unitaries. The transformed coefficient matrix is diagonal.

Expanding
\(\sum_j d_jm_j\otimes m_j\)
in the computational basis yields the normal form
\[
\boxed{
|\psi(x)\rangle=x_0e_0^++x_1e_1^++x_2e_2^++x_3e_3^+,
\qquad x\in\mathbb R^4,\quad \|x\|=1,
}
\tag{14}
\]
where
\[
\begin{aligned}
e_0^\pm&=(|0000\rangle\pm|1111\rangle)/\sqrt2,\\
e_1^\pm&=(|0011\rangle\pm|1100\rangle)/\sqrt2,\\
e_2^\pm&=(|0101\rangle\pm|1010\rangle)/\sqrt2,\\
e_3^\pm&=(|0110\rangle\pm|1001\rangle)/\sqrt2.
\end{aligned}
\tag{15}
\]
For example the coefficient conversion is
\[
x_0=\frac{-d_1+d_2}{\sqrt2},\quad
x_1=\frac{-d_1-d_2}{\sqrt2},\quad
x_2=\frac{d_3-d_4}{\sqrt2},\quad
x_3=\frac{d_3+d_4}{\sqrt2}.
\]
It preserves the squared norm.

Finally, for every physical product unitary \(U\),
\[
H_3(U\rho U^\dagger)=U H_3(\rho)U^\dagger.
\tag{16}
\]
Therefore the normal-form reduction preserves the spectrum whose fourth prefix is being bounded.

## 6. Exact actual-marginal error blocks

Let \(\rho_x=|\psi(x)\rangle\langle\psi(x)|\). The Pauli-twirl identity on physical qubit \(i\) is
\[
I_i\otimes(\rho_x)_{\bar i}
=\frac12\left(\rho_x+X_i\rho_xX_i
+Y_i\rho_xY_i+Z_i\rho_xZ_i\right).
\tag{17}
\]
Summing its four actual lifted marginals gives
\[
\boxed{
H_3(\rho_x)
=2\rho_x+\frac12\sum_{i=1}^4
\left(
|X_i\psi(x)\rangle\langle X_i\psi(x)|
+|Y_i\psi(x)\rangle\langle Y_i\psi(x)|
+|Z_i\psi(x)\rangle\langle Z_i\psi(x)|
\right).
}
\tag{18}
\]
All twelve error vectors come from the **same physical pure input**.

Let \(w_i\) be the computational string with its unique \(1\) in position \(i\), and put
\[
f_i^\pm=(|w_i\rangle\pm|\overline{w_i}\rangle)/\sqrt2.
\]
The \(X_i\psi\), \(Y_i\psi\), and \(Z_i\psi\) lie respectively in the mutually orthogonal spaces
\[
\operatorname{span}\{f_i^+\},\qquad
\operatorname{span}\{f_i^-\},\qquad
\operatorname{span}\{e_j^-\}.
\]
These spaces are also orthogonal to \(\psi(x)\).

Using these ordered bases, the columns of the four error vectors are the following matrices; the \(Y\)-columns have an overall factor \(i\), irrelevant to their outer products:
\[
M_X=
\begin{pmatrix}
x_0&x_1&x_2&x_3\\
x_1&x_0&x_3&x_2\\
x_2&x_3&x_0&x_1\\
x_3&x_2&x_1&x_0
\end{pmatrix},
\tag{19}
\]
\[
M_Y=M_X(x_0,-x_1,-x_2,-x_3),
\tag{20}
\]
and
\[
M_Z=\operatorname{diag}(x_0,x_1,x_2,x_3)
\begin{pmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{pmatrix}.
\tag{21}
\]

Thus the actual blocks in (18) are
\[
\frac12M_XM_X^T,\qquad
\frac12M_YM_Y^T,\qquad
\frac12M_ZM_Z^T.
\]
The remaining three-dimensional subspace of
\(\operatorname{span}\{e_j^+\}\), orthogonal to \(\psi(x)\), has eigenvalue zero.

The Hadamard eigenvectors diagonalize \(M_X\) and \(M_Y\), while
\[
M_ZM_Z^T=4\operatorname{diag}(x_0^2,x_1^2,x_2^2,x_3^2).
\]

Consequently the complete \(H_3\) spectrum is
\[
\boxed{
\operatorname{spec}H_3(\rho_x)
=\left\{2,\ \frac{c_1(x)}2,\ldots,\frac{c_{12}(x)}2,\ 0,0,0\right\},
}
\tag{22}
\]
where the twelve \(c\)'s are
\[
4x_0^2,\quad4x_1^2,\quad4x_2^2,\quad4x_3^2,
\tag{23}
\]
together with
\[
\begin{aligned}
&(x_0+x_1+x_2+x_3)^2,\\
&(x_0+x_1-x_2-x_3)^2,\\
&(x_0-x_1+x_2-x_3)^2,\\
&(x_0-x_1-x_2+x_3)^2,
\end{aligned}
\tag{24}
\]
and
\[
\begin{aligned}
&(x_0-x_1-x_2-x_3)^2,\\
&(x_0-x_1+x_2+x_3)^2,\\
&(x_0+x_1-x_2+x_3)^2,\\
&(x_0+x_1+x_2-x_3)^2.
\end{aligned}
\tag{25}
\]

These formulas retain every physical marginal contribution and every multiplicity.

## 7. Three real bases give the sharp fourth-prefix bound

The twelve numbers in (23)–(25) have the form
\[
c_v(x)=4|\langle v,x\rangle|^2
\]
for the union of three real orthonormal bases:

1. the four coordinate vectors;
2. one half of the four sign vectors in (24);
3. one half of the four sign vectors in (25).

For distinct vectors in this twelve-vector set,
\[
|\langle u,v\rangle|\le\frac12:
\]
the inner product is zero within a basis and has absolute value \(1/2\) between different bases.

Choose any three distinct vectors \(v_1,v_2,v_3\) from this set and let \(G\) be their \(3\times3\) Gram matrix. For every real \(z\),
\[
\begin{aligned}
z^TGz
&\le \sum_i z_i^2+\sum_{i<j}|z_i z_j|\\
&\le 2\sum_i z_i^2.
\end{aligned}
\]
Hence \(G\le2I\). Equivalently,
\[
\sum_{i=1}^3|\langle v_i,x\rangle|^2\le2
\qquad(\|x\|=1).
\]
It follows that the sum of the three largest members of (23)–(25) obeys
\[
\boxed{c_{(1)}(x)+c_{(2)}(x)+c_{(3)}(x)\le8.}
\tag{26}
\]
Also each \(c_v(x)\le4\). Thus the eigenvalue \(2\) in (22) is a largest eigenvalue, including all degeneracies, and
\[
K_4(H_3(\rho_x))
=2+\frac12\bigl(c_{(1)}+c_{(2)}+c_{(3)}\bigr)
\le6.
\tag{27}
\]
The same spectrum also gives
\[
0\le H_3(\rho_x)\le2I.
\]

By the invariant pure decomposition (11), covariance (16), and Ky Fan convexity,
\[
K_4(H_3(\rho))
\le\sum_\ell w_\ell K_4(H_3(|\psi_\ell\rangle\langle\psi_\ell|))
\le6
\]
for every mixed invariant density. Likewise \(H_3(\rho)\le2I\).

This proves (1) without using a four-qubit Kramers argument or independently chosen marginal matrices.

## 8. Exact sharp physical input and common projector

The bound \(6\) is attained. Choose
\[
x_*=\frac{(2,1,1,0)}{\sqrt6},
\qquad
|\psi_*\rangle=\frac{2e_0^++e_1^++e_2^+}{\sqrt6}.
\tag{28}
\]
In computational coordinates,
\[
|\psi_*\rangle
=\frac{|0000\rangle+|1111\rangle}{\sqrt3}
+\frac{|0011\rangle+|1100\rangle+|0101\rangle+|1010\rangle}{\sqrt{12}}.
\tag{29}
\]
It is normalized, and every displayed even-complement vector is fixed by \(\Theta_4\). Thus \(\rho_*=|\psi_*\rangle\langle\psi_*|\) is an actual positive trace-one invariant density.

At \(x_*\), the twelve \(c\)'s are
\[
(8/3)^{\times3},\qquad(2/3)^{\times6},\qquad0^{\times3}.
\]
Therefore
\[
\boxed{
\operatorname{spec}H_3(\rho_*)
=\left(2,(4/3)^{\times3},(1/3)^{\times6},0^{\times6}\right).
}
\tag{30}
\]
In particular \(K_4(H_3(\rho_*))=6\).

An explicit common rank-four projector is obtained from the orthonormal vectors
\[
\psi_*,\qquad
u_Z=e_0^-,
\qquad
u_X=\frac{f_1^++f_2^++f_3^++f_4^+}{2},
\qquad
u_Y=\frac{f_1^--f_2^--f_3^-+f_4^-}{2}.
\]
Set
\[
Q_*=|\psi_*\rangle\langle\psi_*|
+|u_Z\rangle\langle u_Z|
+|u_X\rangle\langle u_X|
+|u_Y\rangle\langle u_Y|.
\tag{31}
\]
Equations (19)–(21) give eigenvalue \(4/3\) on each of \(u_Z,u_X,u_Y\). Consequently the **same projector** satisfies
\[
\boxed{\operatorname{Tr}(Q_*\rho_*)=1,\qquad
\operatorname{Tr}(Q_*H_3(\rho_*))=6.}
\tag{32}
\]

This is a sharpness certificate for a positive bound, **not a counterexample**.

## 9. Sharp fourth output prefix and exact positive reference gap

Let \(Q\) be any complex orthogonal rank-four projector and put
\[
q=\operatorname{Tr}(Q\rho),\qquad h_3=\operatorname{Tr}(QH_3(\rho)).
\]
Equations (1) and (10), applied to that same \(Q\), give
\[
\operatorname{Tr}[QT_t^{\otimes4}(\rho)]
=t^4q+\alpha h_3+4\beta
\le t^4+6\alpha+4\beta.
\tag{33}
\]
Since \(ab=(1-t^2)/4\),
\[
t^4+6t^2ab+4a^2b^2
=\frac{1+4t^2-t^4}{4}.
\tag{34}
\]

For the actual sharp input (28), its complete channel spectrum is
\[
\begin{array}{c|c}
\text{Eigenvalue}&\text{Multiplicity}\\ \hline
t^4+2\alpha+\beta&1\\
\frac43\alpha+\beta&3\\
\frac13\alpha+\beta&6\\
\beta&6
\end{array}
\tag{35}
\]
in decreasing order. The successive differences are
\[
t^4+\frac23\alpha,\qquad \alpha,\qquad \frac13\alpha,
\]
all nonnegative. Hence \(Q_*\) is a top-four projector throughout \(0\le t\le1\), with degeneracies permitted, and equality holds in (33).

Thus (34) is the **exact maximum fourth output prefix over the whole invariant sector**, not merely a possibly unattainable sum of separate bounds.

For the reference,
\[
K_4(D_t)=a^4+3a^3b.
\]
Using the actual reference layers, or direct expansion,
\[
\begin{aligned}
K_4(D_t)-F_4(t)
&=t^3b+5t^2b^2+5tb^3\\
&=tb\left(t^2+5tb+5b^2\right)\\
&=\frac{t(1-t)(5-t^2)}8.
\end{aligned}
\tag{36}
\]
This proves (2)–(3). In particular, the entire previously unpaid high-retention fourth-prefix interval has a strictly positive uniform reference gap.

## 10. All sixteen prefixes, with one consuming projector

For completeness, the product-reference layer spectra are
\[
L_3=(4,1^{\times4},0^{\times11}),
\]
\[
L_2=(6,3^{\times4},1^{\times6},0^{\times5}),
\]
\[
L_1=(4,3^{\times4},2^{\times6},1^{\times4},0).
\]
They share their decreasing Hamming-weight order. Write \(R_j(k)=K_k(L_j)\). Then
\[
K_k(D_t)
=t^4+t^3bR_3(k)+t^2b^2R_2(k)+tb^3R_1(k)+kb^4.
\tag{37}
\]

For any fixed complex rank-\(k\) projector,
\[
q=\operatorname{Tr}(Q\rho)\le1,\qquad
h_1=2k,\qquad h_2=k+h_3.
\]
Positivity, trace \(8\), \(H_3\le2I\), and the new bound give
\[
h_3\le m_k,\qquad
m_k=
\begin{cases}
6,&k=4,\\
\min(2k,8),&k\ne4.
\end{cases}
\tag{38}
\]
Define
\[
A_k=R_3(k)-m_k,\quad
B_k=R_2(k)-k-m_k,\quad
C_k=R_1(k)-2k.
\]
The complete table is:

| \(k\) | \(A_k\) | \(B_k\) | \(C_k\) |
|---:|---:|---:|---:|
| 1 | 2 | 3 | 2 |
| 2 | 1 | 3 | 3 |
| 3 | 0 | 3 | 4 |
| 4 | 1 | 5 | 5 |
| 5 | 0 | 5 | 6 |
| 6 | 0 | 5 | 6 |
| 7 | 0 | 5 | 6 |
| 8 | 0 | 5 | 6 |
| 9 | 0 | 5 | 6 |
| 10 | 0 | 5 | 6 |
| 11 | 0 | 5 | 6 |
| 12 | 0 | 4 | 5 |
| 13 | 0 | 3 | 4 |
| 14 | 0 | 2 | 3 |
| 15 | 0 | 1 | 2 |
| 16 | 0 | 0 | 0 |

Subtracting the actual physical expectation (9) from (37), for this same \(Q\), gives
\[
\begin{aligned}
K_k(D_t)-\operatorname{Tr}[QT_t^{\otimes4}(\rho)]
={}&t^4(1-q)
+t^3b(R_3(k)-h_3)\\
&+t^2b^2(R_2(k)-k-h_3)
+tb^3(R_1(k)-2k)\\
\ge{}&t^4(1-q)+t^3bA_k+t^2b^2B_k+tb^3C_k\\
\ge{}&0.
\end{aligned}
\tag{39}
\]
All coefficients are now nonnegative, including the formerly exceptional fourth row.

Moreover, \(B_k>0\) for every proper prefix. Therefore all proper output prefixes are strictly below their product-reference prefixes when \(0<t<1\).

At \(t=0\), both outputs are maximally mixed. At \(t=1\), the pure product reference majorizes every density. No division by a parameter or spectral gap excludes either endpoint.

## 11. Physical negative branch and arbitrary complex projectors

For one qubit,
\[
T_{-t}=\mathcal J\circ T_t.
\]
On the full four-qubit system, with \(W=Y^{\otimes4}\),
\[
T_{-t}^{\otimes4}(\rho)
=W[T_t^{\otimes4}(\rho)]^T W.
\tag{40}
\]
This is **full transpose**, not partial transpose.

For every complex orthogonal projector \(Q\),
\[
\operatorname{Tr}[QT_{-t}^{\otimes4}(\rho)]
=\operatorname{Tr}[Q'T_t^{\otimes4}(\rho)],
\qquad Q'=WQ^TW.
\tag{41}
\]
Because \(W^T=W=W^\dagger\), \(Q'\) is an orthogonal projector of the same rank. Thus every preceding common-projector inequality transports to the physical branch \(p>1\), where \(t=p-1\le1/3\).

The sharp input likewise retains the spectrum (35) under this full-transpose conjugation. Consequently the sharp fourth-prefix formula and all-prefix theorem hold over the entire physical interval \(0\le p\le4/3\).

## 12. Scope ceiling and independent-check obligations

The substantive new written candidate is:

1. a physical local-unitary normal form for every invariant pure four-qubit state;
2. exact compatible \(H_3\) error blocks;
3. the sharp bound \(K_4(H_3)\le6\) for every invariant mixed density;
4. the exact invariant-sector maximum fourth output prefix
   \[
   \frac{1+4t^2-t^4}{4};
   \]
5. its exact positive product-reference gap
   \[
   \frac{t(1-t)(5-t^2)}8;
   \]
6. full all-physical-parameter, all-prefix majorization on the entire invariant sector.

The argument does not substitute another named orbit for the assigned mixed-state sector. The explicit sharp state certifies attainability of the sector-wide bound; it is not the restriction defining the theorem.

**Unrestricted four-qubit closure remains NOT PROVED.** Outside \(\widetilde\rho=\rho\), the identities \(H_1=2I\) and \(H_2=I+H_3\), the real invariant pure decomposition, and the resulting channel reduction have not been established and cannot be imported.

Before adoption, a disjoint check should reconstruct the load-bearing steps:

- the six physical generator matrices and proper-orthogonal SVD reduction;
- the actual error matrices (19)–(21), including the \(Y\)-signs;
- the twelve-vector frame and three-vector Gram inequality;
- the mixed-state convex extension;
- the explicit physical extremizer and common projector;
- the sharp output spectrum, reference-gap factorization, complete prefix table, and full-transpose projector transport.

No such independent check occurred in this duty. No numerical evidence is offered as universal proof. No source-equivalence, novelty, independent-family, human, kernel, or final research-program completion claim is made. All genuinely held episodes and consumers remain **HELD/ZERO/NONINPUT**.