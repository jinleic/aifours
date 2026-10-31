# f392 WRITTEN review — Eq. (10) semigroup initial-interval proofs

**Intended materialization:** `institute/runs/three-area-2026-10-27-96h/review-waves/f392-ppt-eq10-semigroup-initial-interval-proof-review/review-v1.md`

**Verdict:** **SUPPORTED within the frozen Theorems 2–3 / §§5–6 scope**, including the independently reconstructed antecedents required from Eq. (10) and Theorem 1.

**Findings:** **0 FATAL / 0 MAJOR / 0 MINOR.**

This complete review incorporates the additional parent-supplied clock below. That addition is metadata only: it does not change the scientific conclusions or represent a new derivation, check, or execution. This is written mathematical review, not computational verification, a novelty determination, original-target closure, or a parent disposition. The candidate remains **UNREVIEWED pending parent disposition**.

## 1. Provenance, access, and execution boundary

### Frozen artifacts

The following hashes, byte counts, and LF counts are **parent-supplied metadata**, including the parent’s live match observation. I did not execute independent hashing.

| Artifact | SHA-256 | Bytes / LF |
|---|---|---|
| Manifest | `cc200caa1ae035004cf6b2c4d16fcd908ab5ecd43a6cb91e308413c23bd4ed8e` | 5,486 / 89 |
| Freeze receipt | `ae0d7bbee5bd258a52ad6ee7d38bb4fff5b9cc8ec8a8fb62a58726ba15b8651f` | 1,882 / 47 |
| Literal packet | `e1eddb83568214b2f40b672fd7c1eee3d70c1fed25d19f3127d1e43271741286` | 36,265 / 731 |
| S1, complete source file | `1365bde68234dff06aabd798acd0c740040e6560abb3da708404af43dad99dd6` | 28,388 / 823 |
| S2, preserved source-reader excerpt | `2f9fb815902e8271bc04f927c5e8aa7c68fbb55e4344c36401553083c66ee1ba` | 10,366 / 66 |

Actual mathematical read coverage was **S1 LF1–663 and S2 LF1–66**, exactly as frozen. S1 LF664–823 was not read; no authored checker was accessed.

### Read order

Before mathematical packet access, I read:

1. The complete manifest.
2. The complete freeze receipt.
3. All seven listed status-only controls.
4. The complete parent live-metadata supply.

I then sent a **direct administrative pre-body ACK to Main** before opening the mathematical packet. After that ACK, I read the complete literal packet consecutively in **raw windows of at most 20 LF**, through packet LF731, including both source endings. No elision was observed in those raw packet reads. Reconstruction followed that complete read.

The quarantine controls were status-only inputs. I did not follow their excluded scientific links or use held payloads, outcomes, planning, selection, confidence, or report consumers, including PH v8/cp116 and the held AME route. References in the manuscript to earlier work were not treated as accepted mathematical premises.

S2 is the frozen reader excerpt, not a complete-paper read or a fresh fetch of the public article.

### Clocks and materialization

Parent supplied these actual metadata observations:

- `2026-10-30T10:34:20-0700 PDT`;
- `2026-10-30T10:38:15-0700 PDT`;
- **Supplemental observation:** `2026-10-30T10:39:58-0700 PDT`.

None is my native start, derivation, or completion time. Substantive checkpoints reported the completed packet read, reconstructed norm/remainder argument, and reconstructed cyclic-population and rank-two-vector argument.

No scientific execution, selected new probe, CAS, interpreter, solver, enumeration, replay, authored checker, sibling outcome, build, lint, formatter, external-model CLI, installation, or remote scientific job was used. No working-tree file was written. This complete final body is supplied for parent materialization without bypassing the tool restriction.

## 2. Exact scope and assumptions

The reviewed map is the literal \(d=4\) [source Eq. (10)](https://arxiv.org/html/2508.21348v2#S4.E10), preserved in **S2 LF53–59** and transcribed in **S1 LF138–148**:

\[
\Phi(X)=\frac13
\begin{pmatrix}
x_{11}+x_{22}+x_{33}&x_{12}&x_{13}&x_{14}\\
x_{21}&x_{22}+x_{33}+x_{44}&x_{23}&x_{24}\\
x_{31}&x_{32}&x_{33}+x_{44}+x_{11}&x_{43}\\
x_{41}&x_{42}&x_{34}&x_{44}+x_{11}+x_{22}
\end{pmatrix}.
\]

The conventions are

\[
C(T)=\sum_{i,j=1}^{4}|i\rangle\langle j|\otimes T(E_{ij}),
\qquad
\Omega=\sum_{i=1}^{4}|ii\rangle.
\]

For Theorem 2, the exact assumptions are

\[
\lambda\ge0,\qquad \delta\in\mathbb R,\qquad
S=S^\dagger\ge0,\qquad K\in M_4(\mathbb C),
\]

\[
\Delta(X)=\operatorname{Tr}(X)I_4,\qquad
\mathcal M_S(X)=S\circ X,
\]

\[
\Psi=\lambda\Phi+\delta\Delta+\mathcal M_S,\qquad
L_K(X)=KX+XK^\dagger+\Psi(X).
\]

No trace-preservation, unitality, reality of \(S\) or \(K\), or ordinary positivity of \(\Phi\) is assumed.

Theorem 3 concerns precisely \(e^{t\Phi}\): the original seed, \(K=0\), with no depolarizing or Schur addition.

The reconstruction uses finite-dimensional linear algebra, elementary exponential series, and the finite-dimensional Lie–Trotter product formula. The needed Choi implications are explained below; no prior review result is imported.

## 3. Independently reconstructed Eq. (10) and threshold antecedents

**Relevant source:** S1 LF138–218 and LF225–352.

### 3.1 Choi blocks and the rank-two vector

For a diagonal input \(E_{ii}\), the output has diagonal weight \(1/3\) except at output index \(i+1\pmod4\), where it is zero. For off-diagonal matrix units,

\[
\Phi(E_{ij})=\frac13E_{ij}
\quad\text{unless }(i,j)\in\{(3,4),(4,3)\},
\]

where

\[
\Phi(E_{34})=\frac13E_{43},\qquad
\Phi(E_{43})=\frac13E_{34}.
\]

Consequently, on

\[
\mathcal D=\operatorname{span}\{|11\rangle,|22\rangle,|33\rangle,|44\rangle\},
\]

the Choi matrix is

\[
C(\Phi)|_{\mathcal D}=\frac13M,\qquad
M=J_4-E_{34}-E_{43}.
\]

On

\[
\mathcal B=\operatorname{span}\{|34\rangle,|43\rangle\},
\]

in that order, it is

\[
C(\Phi)|_{\mathcal B}
=\frac13\begin{pmatrix}0&1\\1&1\end{pmatrix}.
\]

The other ten product-basis vectors have uncoupled scalar weights \(0\) or \(1/3\). This verifies that the transposed \(34/43\) coherences have been placed in the correct Choi block rather than incorrectly retained as ordinary coherences on \(\mathcal D\).

Set

\[
q=\frac{\sqrt5-1}{2},\qquad
r=\frac q3=\frac{\sqrt5-1}{6},\qquad
\eta=\frac{|34\rangle-q|43\rangle}{\sqrt{1+q^2}}.
\]

Because \(q^2=1-q\),

\[
\begin{pmatrix}0&1\\1&1\end{pmatrix}
\begin{pmatrix}1\\-q\end{pmatrix}
=
-q\begin{pmatrix}1\\-q\end{pmatrix},
\]

so

\[
C(\Phi)\eta=-r\eta.
\]

Both nonzero coefficients occupy different rows and columns of its coefficient matrix. Thus \(\eta\) has Schmidt rank exactly two. Its support is off the diagonal, so

\[
\langle\Omega,\eta\rangle=0.
\]

A negative Choi expectation on such a vector genuinely refutes \(2\)-positivity. Indeed, for a Schmidt decomposition \(v=\sum_{a=1}^{r}u_a\otimes w_a\), \(r\le2\),

\[
\langle v,C(T)v\rangle
=
\sum_{a,b}
\left\langle w_a,
T\!\left(|\overline{u_a}\rangle\langle\overline{u_b}|\right)
w_b\right\rangle.
\]

This is an expectation of \((\mathrm{id}_r\otimes T)\) applied to a positive rank-one operator. It must be nonnegative if \(T\) is \(2\)-positive.

### 3.2 Exact CP threshold, without importing Theorem 1 as a premise

Directly,

\[
C(\Delta)=I_{16},\qquad
C(\mathcal M_S)=\sum_{i,j}S_{ij}|ii\rangle\langle jj|.
\]

Thus the Schur term is supported on \(\mathcal D\), where its matrix is the full complex Hermitian PSD matrix \(S\). In particular, it annihilates \(\eta\), and

\[
C(\Psi)\eta=(\delta-\lambda r)\eta.
\]

Therefore

\[
\delta<\lambda r
\quad\Longrightarrow\quad
\Psi\text{ is not \(2\)-positive}.
\]

For sufficiency, the \(\mathcal B\) eigenvalues are

\[
\delta+\lambda\frac{1\pm\sqrt5}{6}.
\]

The remaining scalar blocks are \(\delta\) or \(\delta+\lambda/3\).

For the \(\mathcal D\) block, \(M\) has eigenvalues

\[
0,\quad 1,\quad \frac{3-\sqrt{17}}2,\quad
\frac{3+\sqrt{17}}2.
\]

To derive this, the antisymmetric vectors on the first and last pairs give eigenvalues \(0\) and \(1\). On the orthonormal symmetric-pair basis, the remaining matrix is

\[
\begin{pmatrix}2&2\\2&1\end{pmatrix},
\]

whose characteristic polynomial is \(x^2-3x-2\).

Moreover,

\[
r=\frac{\sqrt5-1}{6}>
\frac{\sqrt{17}-3}{6}.
\]

The comparison follows by squaring the positive quantities in
\(\sqrt5+2>\sqrt{17}\), reducing it to \(\sqrt5>2\).

Hence \(\delta\ge\lambda r\) makes every block of

\[
C(\Psi)=\lambda C(\Phi)+\delta I_{16}+C(\mathcal M_S)
\]

PSD, including the \(\mathcal D\) block after adding arbitrary complex \(S\ge0\).

A PSD Choi matrix yields a Kraus representation: decompose it as \(\sum_\ell |v_\ell\rangle\langle v_\ell|\), write \(v_\ell=(I\otimes A_\ell)\Omega\), and use injectivity of the Choi representation to obtain \(T(X)=\sum_\ell A_\ell X A_\ell^\dagger\). Thus it implies complete positivity. Complete positivity implies \(2\)-positivity.

This independently establishes the exact antecedent

\[
\boxed{\Psi\text{ is \(2\)-positive}
\iff \Psi\text{ is CP}
\iff \delta\ge\lambda r.}
\]

It covers the stated complex and singular \(S\), \(\lambda=0\), and real \(\delta\), without adding assumptions.

## 4. Theorem 2: every complex \(K\)

**Relevant source:** S1 LF409–526.

### 4.1 Above threshold: CP at all nonnegative times

If \(\delta\ge\lambda r\), the preceding reconstruction proves that \(\Psi\) is CP.

Write \(A_K(X)=KX+XK^\dagger\). For every \(h\ge0\),

\[
e^{hA_K}(X)=e^{hK}Xe^{hK^\dagger},
\]

which is CP for arbitrary complex \(K\). This does **not** require \(A_K\) itself to be CP.

Also,

\[
e^{h\Psi}=\sum_{n=0}^{\infty}\frac{h^n}{n!}\Psi^n
\]

is CP: every summand is a nonnegative multiple of a CP composition, the identity term is CP, and the CP cone is norm-closed.

The Lie–Trotter formula gives

\[
e^{tL_K}
=
\lim_{n\to\infty}
\left(e^{(t/n)A_K}e^{(t/n)\Psi}\right)^n.
\]

Every approximant is CP, so

\[
\boxed{\delta\ge\lambda r
\Longrightarrow e^{tL_K}\text{ is CP for every }t\ge0.}
\]

This supports S1 LF424 and LF443–453.

### 4.2 Below threshold: the first derivative is negative independently of \(K\)

Let

\[
v_K=(I\otimes K)\Omega.
\]

Applying the Choi definition directly to left and right multiplication gives

\[
C(A_K)
=
|v_K\rangle\langle\Omega|
+
|\Omega\rangle\langle v_K|.
\]

Since \(\eta\perp\Omega\),

\[
\langle\eta,C(A_K)\eta\rangle=0.
\]

Also \(C(\mathrm{id})=|\Omega\rangle\langle\Omega|\), so its expectation on \(\eta\) is zero. Thus, with

\[
a=\lambda r-\delta>0,
\]

one obtains

\[
\langle\eta,C(L_K)\eta\rangle=-a.
\]

No restriction on the entries, spectrum, normality, or Hermitian part of \(K\) is needed. This supports S1 LF457–476.

### 4.3 Exact Hilbert–Schmidt induced norms

Use the induced \(2\to2\) norm on \(M_4\) with its Hilbert–Schmidt norm.

**The Eq. (10) map.** On the diagonal sector, \(3\Phi\) is

\[
A=J_4-P,\qquad Pe_i=e_{i+1}
\]

with cyclic indices. The commuting matrices \(J_4\) and \(P\) are simultaneously diagonalized by the cyclic Fourier basis. The constant mode of \(A\) has eigenvalue \(3\); its other three eigenvalues have modulus \(1\). Therefore the diagonal-sector norm of \(\Phi\) is \(1\).

On the orthogonal off-diagonal sector, \(\Phi\) is \(1/3\) times the permutation swapping \(E_{34}\) and \(E_{43}\) and fixing the other off-diagonal matrix units. Its norm is \(1/3\). Consequently,

\[
\|\Phi\|_{2\to2}=1.
\]

**The depolarizing map.** Cauchy–Schwarz gives

\[
|\operatorname{Tr}X|\le\|I_4\|_2\|X\|_2=2\|X\|_2,
\]

and \(\|\operatorname{Tr}(X)I_4\|_2=2|\operatorname{Tr}X|\). Equality is attained along the identity direction, so

\[
\|\Delta\|_{2\to2}=4.
\]

**The complex Schur map.** The matrix units form an orthonormal eigenbasis for this superoperator, hence

\[
\|\mathcal M_S\|_{2\to2}=\max_{i,j}|S_{ij}|.
\]

For complex \(S\ge0\), its \(2\times2\) principal minors imply

\[
|S_{ij}|^2\le S_{ii}S_{jj},
\]

so the maximum is exactly the largest diagonal entry:

\[
\|\mathcal M_S\|_{2\to2}=\max_i S_{ii}.
\]

Finally,

\[
\|A_K\|_{2\to2}\le2\|K\|_{\mathrm{op}},
\]

which is an upper bound, not an asserted equality. Therefore

\[
\|L_K\|_{2\to2}\le
M:=2\|K\|_{\mathrm{op}}+\lambda+4|\delta|+\max_iS_{ii}.
\]

The denominator used in the proposed interval is valid below threshold: since \(0<r<1\),

\[
0<a=\lambda r-\delta
\le\lambda+|\delta|\le M.
\]

In particular, **\(M>0\)** whenever this branch is invoked.

This supports S1 LF435–440 and LF478–488, including the complex-Schur and zero-denominator boundaries.

### 4.4 Reshuffling factor, remainder, and inclusive endpoint

Set

\[
R_t=e^{tL_K}-\mathrm{id}-tL_K.
\]

The exponential series yields

\[
\|R_t\|_{2\to2}
\le\sum_{n\ge2}\frac{(tM)^n}{n!}
\le\frac{t^2M^2}{2}e^{tM}.
\]

Let \(\mathsf R_t\) denote its \(16\times16\) superoperator matrix in the orthonormal matrix-unit basis. Choi reshuffling permutes its entries, so

\[
\|C(R_t)\|_F=\|\mathsf R_t\|_F.
\]

Because a \(16\times16\) matrix has at most 16 singular values,

\[
\|\mathsf R_t\|_F\le4\|\mathsf R_t\|_{\mathrm{op}}
=4\|R_t\|_{2\to2}.
\]

Thus the required factor is indeed **four**:

\[
\|C(R_t)\|_{\mathrm{op}}
\le4\|R_t\|_{2\to2}.
\]

Using the normalized vector \(\eta\),

\[
\langle\eta,C(e^{tL_K})\eta\rangle
\le-at+2t^2M^2e^{tM}.
\]

Define

\[
\tau=\min\left\{\frac1M,\frac{a}{12M^2}\right\}>0.
\]

For every \(0<t\le\tau\),

\[
e^{tM}\le e<3
\]

and

\[
2t^2M^2e^{tM}
<6t^2M^2
\le\frac{at}{2}.
\]

Consequently,

\[
\boxed{
\langle\eta,C(e^{tL_K})\eta\rangle
\le-\frac{at}{2}<0
\qquad(0<t\le\tau).
}
\]

This proves failure of \(2\)-positivity on the **inclusive** claimed initial interval. The constant \(12\), the Frobenius factor \(4\), and the endpoint inclusion are justified.

This supports S1 LF490–520.

**Quantifier boundary:** every fixed finite complex \(K\) has the displayed parameter-dependent positive interval. This is not a common positive lower bound on the interval length over unbounded \(K\).

## 5. Theorem 3: complete \(K=0\) evolution and explicit negative vector

**Relevant source:** S1 LF530–619.

Put \(u=t/3\).

### 5.1 Full cyclic population orientation

For a diagonal input, \(3\Phi\) acts as

\[
A=J_4-P,\qquad Pe_i=e_{i+1}.
\]

This orientation is important: input population at \(i\) has its missing first-order output at \(i+1\), not at \(i-1\).

Since \(P\) commutes with \(J_4\),

\[
e^{uA}
=e^{-uP}+\frac{e^{3u}-e^{-u}}4J_4.
\]

Grouping the exponential series according to powers of \(P\) modulo four gives

\[
e^{-uP}=c_0I+c_1P+c_2P^2+c_3P^3,
\]

where

\[
c_0=\frac{\cosh u+\cos u}{2},\qquad
c_1=-\frac{\sinh u+\sin u}{2},
\]

\[
c_2=\frac{\cosh u-\cos u}{2},\qquad
c_3=-\frac{\sinh u-\sin u}{2}.
\]

Adding the common \(J_4\) coefficient gives the four population coefficients

\[
d_0=\frac{e^{3u}+e^u+2\cos u}{4},
\qquad
d_2=\frac{e^{3u}+e^u-2\cos u}{4},
\]

\[
p_-=\frac{e^{3u}-e^u-2\sin u}{4},
\qquad
p_+=\frac{e^{3u}-e^u+2\sin u}{4}.
\]

With output index as row and input index as column, the complete population matrix is

\[
e^{uA}=
\begin{pmatrix}
d_0&p_+&d_2&p_-\\
p_-&d_0&p_+&d_2\\
d_2&p_-&d_0&p_+\\
p_+&d_2&p_-&d_0
\end{pmatrix}.
\]

Thus \(p_-\) is the forward coefficient \(i\mapsto i+1\), and \(p_+\) is the backward coefficient \(i\mapsto i-1\). In particular, the Choi diagonal weights on \(|34\rangle\) and \(|43\rangle\) are respectively \(p_-\) and \(p_+\).

This independently supports the orientation and formulas in S1 LF549–565.

### 5.2 Complete off-diagonal action and the Choi pair

For the ten off-diagonal matrix units outside the special pair,

\[
e^{t\Phi}(E_{ij})=e^uE_{ij}.
\]

On the special pair, the generator is \(1/3\) times the transposition matrix, so

\[
e^{t\Phi}(E_{34})
=\cosh u\,E_{34}+\sinh u\,E_{43},
\]

\[
e^{t\Phi}(E_{43})
=\cosh u\,E_{43}+\sinh u\,E_{34}.
\]

Together with the population matrix above, these formulas specify the evolution on every matrix unit.

Under the stated Choi convention, the \(\sinh u\) terms connect \(|34\rangle\) to \(|43\rangle\). Therefore

\[
B_t=C(e^{t\Phi})|_{\mathcal B}
=
\begin{pmatrix}
p_-&\sinh u\\
\sinh u&p_+
\end{pmatrix}.
\]

The \(\cosh u\) terms instead connect \(|33\rangle\) and \(|44\rangle\) on \(\mathcal D\); they do not replace the displayed off-diagonal entries of \(B_t\).

This supports S1 LF568–582 and checks the resulting Choi-index placement explicitly.

### 5.3 Determinant and inclusive interval

Direct multiplication gives

\[
p_-p_+
=\frac{(e^{3u}-e^u)^2-4\sin^2u}{16}.
\]

Since

\[
e^{3u}-e^u=2e^{2u}\sinh u,
\]

the determinant is

\[
\boxed{
\det B_t
=
\frac{(e^{4u}-4)\sinh^2u-\sin^2u}{4}.
}
\]

For

\[
0<u\le\frac{\log2}{2},
\]

one has \(e^{4u}\le4\) and \(\sin u>0\). Hence

\[
\det B_t<0.
\]

The determinant remains strictly negative at the upper endpoint: there the first term in the numerator vanishes, while the subtracted sine square does not.

This supports S1 LF585–598.

### 5.4 Positivity of \(p_-\) and an actual rank-two negative vector

The matrix \(A=J_4-P\) is entrywise nonnegative, and

\[
A^2
=J_4^2-J_4P-PJ_4+P^2
=2J_4+P^2.
\]

Every entry of every nonnegative power \(A^n\) is nonnegative. In a forward position \((i+1,i)\), the \(I\) and \(A\) contributions vanish, while the corresponding \(A^2\) entry is \(2\). Therefore the exponential series gives

\[
p_-\ge\frac{u^2}{2}\,2=u^2>0
\qquad(u>0).
\]

Let \(s=\sinh u>0\) and define

\[
z_t=s\,|34\rangle-p_-|43\rangle.
\]

Both coefficients are nonzero. Its coefficient matrix therefore has rank exactly two. Its Choi expectation is

\[
\begin{aligned}
\langle z_t,C(e^{t\Phi})z_t\rangle
&=p_-s^2-2p_-s^2+p_+p_-^2\\
&=p_-(p_-p_+-s^2)\\
&=p_-\det B_t\\
&<0.
\end{aligned}
\]

Thus this is an explicit rank-two violation, not merely an unspecified negative eigenvalue of a larger matrix.

Since \(t=3u\),

\[
\boxed{
e^{t\Phi}\text{ is not \(2\)-positive for every }
0<t\le\frac32\log2.
}
\]

This supports S1 LF601–617.

The interval is **analytically certified**, not claimed to be the maximal failure interval or the exact time at which \(2\)-positivity first becomes possible.

## 6. Claimwise disposition

| Claim | Disposition | Source LF and exact qualification |
|---|---|---|
| Literal Eq. (10) transcription and needed Choi blocks | **SUPPORTED** | S1 LF138–181; S2 LF53–59. Derived from matrix-unit action. |
| Needed \(\eta\), Schmidt rank two, eigenvalue \(-r\), and \(\eta\perp\Omega\) | **SUPPORTED** | S1 LF201–218. Independently reconstructed. |
| Exact threshold for the stated affine complex-PSD-Schur family | **SUPPORTED** | S1 LF225–352. Reconstructed as a necessary antecedent, not imported from another gate. |
| Complex-\(K\) Choi formula and cancellation | **SUPPORTED** | S1 LF457–476. No restriction on complex \(K\). |
| Exact HS norms and stated \(M\) bound | **SUPPORTED** | S1 LF435–440, LF478–488. Includes complex \(S\) and proof that \(M>0\) below threshold. |
| Factor-four reshuffling bound and exponential remainder | **SUPPORTED** | S1 LF490–512. |
| Constant \(12\) and inclusive \(0<t\le\tau\) | **SUPPORTED** | S1 LF515–520. |
| Above-threshold CP trajectory at every \(t\ge0\) | **SUPPORTED** | S1 LF424, LF443–453. Closed CP cone and Lie–Trotter argument. |
| Full cyclic population orientation and \(p_\pm\) | **SUPPORTED** | S1 LF549–565. Full population matrix supplied in this review. |
| Hyperbolic transpose pair and its Choi placement | **SUPPORTED** | S1 LF568–582. |
| Exact determinant formula | **SUPPORTED** | S1 LF585–592. |
| \(p_-\ge u^2\), actual rank-two vector, inclusive longer interval | **SUPPORTED** | S1 LF595–617. |
| Later-time \(2\)-positivity or all-generator exclusion beyond these intervals | **INCONCLUSIVE / NOT ESTABLISHED** | Correctly left unpaid at S1 LF522–526 and LF652–656. |
| Selected rational controls elsewhere in Theorem 1 | **INCONCLUSIVE IN THIS REVIEW** | S1 LF389–405 was read as source claims, but is outside this audit and was not used as evidence. |
| Computational verification | **NOT_RUN** | No program, finite replay, or scientific execution was performed. |
| Literature novelty or priority | **INCONCLUSIVE** | No exhaustive literature audit was performed; no novelty acceptance follows from this proof review. |
| Original \(4\times4\) PPT/Schmidt-number target | **INCONCLUSIVE / NOT CLOSED** | Neither the required state–detector pair nor a theorem covering every \(4\times4\) PPT state is supplied. |

## 7. Boundaries and unpaid gates

1. **\(2\)-positivity is not ordinary positivity.** The witnesses above have Schmidt rank two. They refute the \(k=2\) requirement; they do not refute \(k=1\) positivity. No ordinary-positivity proof or counterexample is established here.

2. **The source workflow does not supply an unproved \(k=2\) seed premise.** The preserved [Workflow 1](https://arxiv.org/html/2508.21348v2#Thmworkflow1), S2 LF17–34, starts with an already \(k\)-positive seed. The Eq. (10) discussion at S2 LF58 reports numerical evidence rather than an ordinary-positivity proof. Its sampling and nondecomposability numerics were not independently verified in this review.

3. **The all-\(K\) conclusion is an initial-time conclusion below threshold.** No impossibility is proved for every later time or every generator. Later-time global complex \(2\)-positivity, nondecomposability, and a genuine PPT-negative pairing remain separate obligations.

4. **The \(K=0\) result is for the exact source trajectory.** It does not automatically cover arbitrary offsets, Schur additions, or other generators on that longer interval.

5. **Universal proof and finite evidence remain distinct.** The review supports the universal parameter and time statements through symbolic written arguments. It does not report computational PASS, finite-test coverage, or execution-derived confidence.

6. **No full original-target closure follows.** A valid positive resolution still needs an actual \(4\times4\) PPT state and a globally complex-rank-\(\le2\)-nonnegative detector with negative pairing. A negative resolution still needs a proof covering every \(4\times4\) PPT state.

7. **Acceptance remains separate.** No formal/kernel, human, independent-model-family, exhaustive-literature, novelty, or parent acceptance is claimed. Existing holds are not rehabilitated by this return.

## 8. Final verdict fields

**overall_correctness:** correct within the frozen audited scope.

**explanation:** The required Eq. (10) antecedents, all-complex-\(K\) quantitative initial-time argument, and complete \(K=0\) cyclic-population/transposed-coherence calculation reconstruct without a correctness defect. The inclusive interval endpoints and actual rank-two negative vectors are justified; later-time behavior, ordinary positivity, novelty, computational verification, and original-target closure remain outside the established result.

**confidence:** 0.98.

**FATAL / MAJOR / MINOR:** **0 / 0 / 0**.