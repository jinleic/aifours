# f306 written audit — full text for `review-v1.md`

**Disposition:** The main sufficient implication is **SUPPORTED, conditionally**. The manuscript is **not correct in all its ancillary claims**: its proposed all-parameter free-source injectivity condition is structurally obstructed by the imported Serre seeds.

**Findings:** **0 FATAL / 2 MAJOR / 1 MINOR.** No whole-level-8 vanishing theorem, all-level result, or numerical contraction determinant is accepted.

## 1. Coverage, process and imports

The working-tree ACK-file write was refused by the tool. No alternative filesystem-writing mechanism was used; this complete review is returned for parent materialization.

Before mathematical input, I read the complete manifest, freeze receipt and three status-only controls, checked their hashes, and sent an administrative PRE-BODY ACK. The manifest and receipt match:

- Manifest: `014ac8d47c85ec26397788c8cfd570f723f9e9ab13852a1595cc9b736c8c5021`.
- Freeze receipt: `ae409899654ce8139901460a58f41d5448dd7a14dac08d9e3a2b91418ae0b2f8`.

I then read the entire 172-LF ordered literal packet, including its ending, in consecutive raw windows of at most 20 LF, before deriving. This covers:

- **S1:** the complete 69-LF GCI manuscript, SHA `1dd5a536d52fff8f5a995f3b7c4cd27fc4f0098188ffc248e62303d73e3881ca`.
- **S2:** the complete 27-LF f276 conditional disposition, SHA `09d94aacd14c652568da68facca73f79121fb8b2f0a7b30a4cdd703204230c0e`.
- **S3:** the complete 74-LF displayed presentation, SHA `b415be711bf075210e2154db9812b024cb2282dfd38c3ae2fd9fb97315234030`.

The packet and all three source hashes match their frozen values. No truncated packet window required recovery.

Fresh UTC observations were **13:54:56**, **13:58:44**, **14:02:01**, and **14:04:35** on 2026-10-30. The audit used written, universally quantified algebra only. Executable operations were limited to hashes and dates. No scientific interpreter, CAS, solver, enumeration, selected-parameter experiment, author code, external-model CLI, build, test, linter or formatter was used. Two unsolicited peer administrative ACKs arrived; neither contained a mathematical review body, and neither was mathematical input.

The source theorem is imported **only at S2’s stated conditional boundary and S3’s exact presentation**. I do not independently authenticate its underlying longer manuscript, the historical book transcription, preliminary-algebra PBW claims, or excluded numerical evidence. The finite-dimensional representation-theoretic imports are ordinary characteristic-zero complete reducibility and lowest-vector theory. The trace calculations below are reconstructed algebraically, not accepted as imported “spot values.” The displayed \(8\otimes8\) decomposition is unnecessary.

## 2. Findings

### M1 — Prove lowest-space stability before replacing GCI by determinants

**Severity:** MAJOR  
**Priority:** 2  
**Confidence:** 0.99  
**file_path:** `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/kac-moody/frontier-20261030-level8-global-contraction-bridge-v1.md`  
**line_start:** 41  
**line_end:** 41

Lemma 2 establishes preservation of horizontal degree in the full free level, not preservation of \(M_{(a,b)}=\ker(F_1,F_2)\cap L_n(V)_{(a,b)}\). The manuscript expressly leaves lowest-space stability as an unproved conjunct, so it cannot then eliminate that conjunct and define endomorphism determinants on \(M_{(a,b)}\) solely “by Lemma 2.” Retain conjunct (i) in the determinant reformulation, or supply the invariant-pairing proof that makes these restrictions endomorphisms. Section 4 below supplies such a proof prospectively; it does not make the manuscript’s original justification complete.

### M2 — Remove the obstructed all-parameter GCI reformulation

**Severity:** MAJOR  
**Priority:** 2  
**Confidence:** 1.00  
**file_path:** `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/kac-moody/frontier-20261030-level8-global-contraction-bridge-v1.md`  
**line_start:** 55  
**line_end:** 57

E2 is not equivalent to pointwise \(\mathrm{GCI}_8(r,s)\), and the imported nonzero Serre seeds obstruct the proposed all-parameter free-source injectivity target. For every positive \(r,s\), \(q_r\in P_{r+1}\cap I_{r+1}\) is nonzero and killed by all three original lowerings; hence the manuscript’s eight-word identity gives \(\Omega_{r+1}q_r=0\), with the analogous statement for \(q_s\) at level \(s+1\). Thus, at every fixed \(n\ge2\), the all-parameter GCI condition fails on the permitted seed-level loci \(r+1=n\) or \(s+1=n\). These vectors vanish in the quotient \(S\), so this obstruction does not refute the desired quotient-level lowering statement. Keep the sufficient conditional bridge, but do not present universal free-source GCI as an equivalent or dischargeable premise for the entire parameter domain.

### m1 — Distinguish an affine matrix pencil from its determinant polynomial

**Severity:** MINOR  
**Priority:** 2  
**Confidence:** 0.99  
**file_path:** `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/kac-moody/frontier-20261030-level8-global-contraction-bridge-v1.md`  
**line_start:** 41  
**line_end:** 41

Lemma 1 proves that the matrix pencil is affine in \(r,s\), not that its determinant is an affine polynomial. On a block of dimension \(d\), it establishes a determinant polynomial of total degree at most \(d\); reduction to degree at most one would require a separate argument. Replace “an affine polynomial condition,” and the corresponding “affine determinant conditions” at LF51, by “nonvanishing of the determinant of an affine matrix pencil.” This audit does not assert a particular nonlinear determinant for an uncomputed block.

## 3. Basis, theta signs, Gram and actual lowering action

### 3.1 Eight-letter basis and theta-duals — SUPPORTED

Using the universal matrix-unit identity

\[
[E_{ab},E_{cd}]=\delta_{bc}E_{ad}-\delta_{da}E_{cb},
\]

the given finite-Levi action produces exactly

\[
(B_0,\ldots,B_7)
=(E_{31},-E_{32},E_{21},H_{13},H_{12},
  -E_{12},-E_{23},-2E_{13}).
\]

These matrices label the finite module; they are **not** a matrix-multiplication model for the free Lie algebra or for positive/negative cross-brackets in \(T\).

For a bracket expression containing \(m\) simple positive generators, applying \(-\theta\) gives sign \((-1)^{m+1}\) after replacing every \(e_i\) by \(f_i\), without reversing bracket order. This verifies all eight displayed duals:

\[
\begin{aligned}
w_0&=f_3,&
w_1&=-[f_1,f_3]=[f_3,f_1],\\
w_2&=-[f_2,f_3]=[f_3,f_2],&
w_3&=[f_{12},f_3],\\
w_4&=[f_1,[f_2,f_3]],&
w_5&=-[f_{12},[f_1,f_3]],\\
w_6&=-[f_{12},[f_2,f_3]],&
w_7&=[f_{12},[f_{12},f_3]].
\end{aligned}
\]

Here \(f_{12}=[f_1,f_2]\). There is no theta-sign error.

For completeness, the finite simple-lowering actions on the entire basis are

\[
\begin{aligned}
F_1(u_0,\ldots,u_7)
 &=(0,u_0,0,u_2,2u_2,u_4,0,2u_6),\\
F_2(u_0,\ldots,u_7)
 &=(0,0,u_0,-u_1,u_1,0,u_3-u_4,-2u_5).
\end{aligned}
\]

These follow from the same matrix-unit identity and agree with the fixed adjoint-module conventions.

### 3.2 Complete Gram table — SUPPORTED

The bilinear form uses ordinary transpose, not complex conjugation. For matrix units,

\[
\operatorname{tr}(E_{ab}E_{cd}^{T})
=\delta_{ac}\delta_{bd}.
\]

Consequently, all six off-diagonal basis matrices are mutually orthogonal and orthogonal to the two diagonal matrices. Their squared pairings are \(1,1,1,1,1,4\). The remaining block follows from

\[
\operatorname{tr}(H_{13}^{2})=2,\qquad
\operatorname{tr}(H_{12}^{2})=2,\qquad
\operatorname{tr}(H_{13}H_{12})=1.
\]

Thus the complete table is

\[
G=\operatorname{diag}
\left(1,1,1,
\begin{pmatrix}2&1\\1&2\end{pmatrix},
1,1,4\right),
\]

with the displayed two-dimensional block occupying indices \(3,4\). It is nonsingular, with determinant \(12\). This verifies the defining Gram matrix algebraically; it accepts no determinant of \(\Omega_n\).

### 3.3 Actual \(F_3\) action and affinity — SUPPORTED for \(n\ge2\)

The Chevalley relations give

\[
F_3(u_0,\ldots,u_7)
=(-h_3,-r e_1,-s e_2,-(r+s)e_{12},-s e_{12},0,0,0).
\]

The final three zeros follow respectively from the fixed finite-Levi Serres and \([e_{12},e_{12}]=0\).

There is an important typing qualification: \(F_3\) is not an endomorphism-valued derivation of \(L(V)\) at degree one; its letter values lie in \(T_0\). Its Jacobi extension is the actual adjoint action in \(T\). For every \(n\ge2\), it does map \(L_n(V)\) into \(L_{n-1}(V)\).

The affine assertion survives this qualification. For a letter of charge \((a_i,b_i)\),

\[
[h_3,u_i]=(2-r a_i-s b_i)u_i.
\]

Each Jacobi term contains one application of \(F_3\): either a parameter-linear finite-Levi action, or the single \(h_3\) action above. No second parameter-dependent factor is introduced. Induction on bracket length therefore proves affinity of \(F_3\), and hence of all \(W_j\) and \(\Omega_n\), on the fixed free-level spaces.

This argument uses the full Cartan relations and does not discard additional Cartan directions.

### 3.4 Eight-word table on lowest vectors — SUPPORTED

Let \(A=F_{12}\), let \(F_1x=F_2x=0\), and put \(d=F_3x\). Then \(Ax=0\). Expanding the eight stated commutators gives, in order,

\[
(W_0,\ldots,W_7)x
=(d,-F_1d,-F_2d,Ad,F_1F_2d,
  -AF_1d,-AF_2d,A^2d).
\]

In particular, both mixed negative signs and the final positive sign are correct. This establishes

\[
F_3x=0\quad\Longrightarrow\quad\Omega_nx=0
\]

on the lowest space. It does not establish the converse.

### 3.5 Degree preservation — SUPPORTED

Every \(W_j\) lowers level by one and horizontal charge by the charge of \(u_j\). Since \(G^{-1}\) only couples equal-charge indices, every summand \(\operatorname{ad}u_i\,W_j\) has total charge zero. This proves full horizontal-block preservation, separately from lowest-space preservation.

## 4. Lowest-space stability: missing in the manuscript, recoverable in writing

**Mathematical identity: SUPPORTED by the following reviewer reconstruction.**  
**Claim that Lemma 2 alone establishes it: REFUTED.**

For arbitrary \(g,U,V\in\mathfrak{sl}_3\), finite Chevalley involution is \(\theta(g)=-g^T\), and

\[
\operatorname{tr}([g,U]V^T)
+\operatorname{tr}\!\left(U[-g^T,V]^T\right)=0.
\]

For \(J(v)=-\theta(v)\),

\[
[g,J(v)]=J([\theta(g),v]).
\]

These identities prove that the displayed Gram pairing between \(V\) and its negative theta-image is finite-Levi invariant. Its nondegeneracy therefore makes

\[
t=\sum_{i,j}(G^{-1})_{ij}u_i\otimes w_j
\]

an invariant coevaluation tensor.

The map sending \(u\otimes w\) to \(\operatorname{ad}u\,\operatorname{ad}w\) is equivariant. Hence

\[
[\operatorname{ad}g,\Omega_n]=0
\]

for every finite-Levi \(g\), and in particular \(\Omega_n(P_n)\subseteq P_n\).

This supplies a prospective completion of the stability argument, uniformly in parameters and levels. It is not a proof contained in S1, nor does it establish injectivity.

## 5. Ideal descent, the level-two boundary and lowest lifts

### 5.1 Ideal stability — SUPPORTED at the f276 boundary

S2 imports that the whole positive ideal is stable under every original lowering, finite-Levi action and positive bracket. Since the \(w_j\) are Lie words in original lowerings, each \(W_j\) preserves that ideal with the stated level shift. Every \(\operatorname{ad}u_i\) also preserves it.

At the required boundary \(n=2\), there is no appeal to an undefined positive \(I_0\). Both seed levels are at least two, so \(I_1=0\). Consequently,

\[
W_j(I_2)\subseteq I_1=0.
\]

The contraction is therefore well-defined at this boundary. With lowest-space stability,

\[
\Omega_n(N_n)\subseteq N_n.
\]

### 5.2 Finite-dimensional quotient injectivity — SUPPORTED

Lemma 5 is valid. Its abbreviated proof needs the finite-dimensional surjectivity step: injectivity of \(\Omega|_N\), together with \(\Omega(N)\subseteq N\), gives

\[
\dim\Omega(N)=\dim N,\qquad \Omega(N)=N.
\]

Thus \(\Omega x\in N\) has a preimage \(y\in N\), and injectivity on \(P\) gives \(x=y\in N\). No injectivity is inferred merely from the name GCI; the argument uses its explicit injectivity hypothesis.

### 5.3 Lowest lifting — SUPPORTED

Each \(L_n(V)\) is finite-dimensional, and \(I_n\) is finite-Levi stable. Complete reducibility supplies a stable complement \(W\), and the quotient identifies \(W\) with \(S_n\). Taking joint kernels of the two finite simple lowerings yields

\[
P_n/N_n\cong\ker(F_1,F_2\mid S_n).
\]

Every quotient-lowest vector therefore has a genuinely lowest free lift. This is stronger than merely lifting a representative and is exactly what the bridge proof needs.

## 6. Main sufficient implication — SUPPORTED, conditionally

For a quotient joint-kernel vector, take a lowest lift \(x\in P_n\). Root grading and quotient compatibility give

\[
F_3x\in I_{n-1}.
\]

The eight-word table and ideal stability then imply

\[
\Omega_nx\in I_n.
\]

Lowest-space stability places this image in \(N_n\). Finite-dimensional descent makes the induced contraction on \(P_n/N_n\) injective whenever the explicitly assumed free-source contraction is injective. Therefore the original quotient vector is zero.

This proves the stated implication for each \(n\ge2\), including its conditional \(n=8\) specialization. It does **not** prove GCI at any parameter pair.

The charge-bound argument at LF51 is also **SUPPORTED**:

\[
2a-b\le n,\qquad 2b-a\le n
\]

imply \(a,b\le n\) and \(a+b\le2n\). This gives a finite containing set, not an exact lowest-space census.

## 7. Uniform seed obstruction — REFUTES the all-parameter GCI proposal

This is a universally quantified argument using the two required imported seed families, not a selected parameter or root test.

For every positive \(r,s\),

\[
q_r=-(\operatorname{ad}u_0)^r u_1
=(\operatorname{ad}e_3)^{r+1}e_1
\]

is nonzero in the free source by S2. The complete finite-lowering tables show \(F_1q_r=F_2q_r=0\).

Put \(E=\operatorname{ad}e_3\), \(F=\operatorname{ad}f_3\), \(H=\operatorname{ad}h_3\). Since \(Fe_1=0\) and \(He_1=-r e_1\), the symbolic \(\mathfrak{sl}_2\) identity is

\[
FE^k e_1=k(r-k+1)E^{k-1}e_1.
\]

At the seed exponent this gives \(F_3q_r=0\). Therefore

\[
0\ne q_r\in P_{r+1}\cap I_{r+1},
\qquad
\Omega_{r+1}q_r=0.
\]

The identical argument gives

\[
0\ne q_s\in P_{s+1}\cap I_{s+1},
\qquad
\Omega_{s+1}q_s=0.
\]

Thus, uniformly,

\[
\neg\mathrm{GCI}_{r+1}(r,s),\qquad
\neg\mathrm{GCI}_{s+1}(r,s).
\]

For every fixed \(n\ge2\), the proposed universal parameter assertion encounters these permitted seed-level loci. Its failure is therefore established without computing any contraction matrix or determinant.

There is no contradiction with possible quotient injectivity: these seeds are zero in \(S\). The free-source premise is strictly more demanding than what the bridge needs to conclude about the quotient. The audit establishes no necessary equivalence between GCI and desired lowering injectivity.

## 8. Determinant reformulation and node exchange

### 8.1 Determinants

- **SUPPORTED after lowest-space stability is supplied:** on fixed lowest charge blocks, the matrices are affine pencils \(A+rB+sC\), and nonzero determinants characterize their injectivity.
- **INCONCLUSIVE:** the stronger literal claim that those determinant polynomials themselves are affine. Lemma 1 does not establish it.
- **REFUTED:** treating pointwise E1 and universally quantified E2 as equivalent forms of the same fixed-parameter premise. E2 is additionally obstructed as shown above.

No block dimension, rank, determinant value, or nonvanishing region has been evaluated.

### 8.2 Node-exchange covariance — SUPPORTED by complete algebraic reconstruction

The exact basis transformation is

\[
\sigma(u_0,\ldots,u_7)
=(u_0,u_2,u_1,-u_3,u_4-u_3,-u_6,-u_5,u_7).
\]

It preserves the full displayed Gram matrix. On the only nontrivial mixed block, this follows by substituting \((-u_3,u_4-u_3)\) into the already verified Gram pairing; the other transformations are exchanges or sign changes with matching Gram entries.

Because \(\sigma\theta=\theta\sigma\), the same transformation applies to the negative theta-image. Consequently the coevaluation tensor is covariant, and

\[
\sigma\Omega_n(r,s)=\Omega_n(s,r)\sigma.
\]

The isomorphism exchanges lowest charge blocks \((a,b)\) and \((b,a)\). Once their restrictions are defined using lowest-space stability, conjugacy proves

\[
\det\Omega_{(a,b),n}(r,s)
=
\det\Omega_{(b,a),n}(s,r).
\]

This is an identity of determinant polynomials, not an assertion that either side is nonzero.

## 9. Final boundary

The manuscript’s **main sufficient bridge survives** at its exact conditional source/import boundary. Lowest-space stability can be supplied by the uniform invariant-pairing argument above. The explicit injectivity premise remains unproved pointwise and is **false as a universal free-source requirement** because of the nonzero Serre seeds.

No original-target solution, level-8 determinant certificate, all-level vanishing, \(J=\tau\) conclusion, numerical acceptance, source authentication, or independent-family/formal certification is delivered.

**overall_correctness:** incorrect

**explanation:** The conditional whole-level bridge is supported, but the determinant reformulation drops an unproved stability conjunct, confuses matrix affinity with determinant affinity, and presents an all-parameter free-source injectivity condition obstructed by the imported Serre seeds. These ancillary defects do not refute the bridge implication or the desired quotient-level statement.

**confidence:** 0.99