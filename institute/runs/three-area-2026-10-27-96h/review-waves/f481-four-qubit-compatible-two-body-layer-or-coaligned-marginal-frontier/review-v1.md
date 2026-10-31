# Author candidate v1 — Actual four-qubit compatible marginal layers, a common-projector spin-flip sector, and full majorization for the two-excitation Dicke orbit

**Status: GENERAL AUTHOR / WRITTEN PROOF CANDIDATE / NOT INDEPENDENTLY ACCEPTED.**

**Materialization:** Complete body for `author-candidate-v1.md` in F481. Also retained at `local://f481-author-candidate-v1.md`. No repository file was written. Scientific code, numerical calculations, CAS, solvers, builds, tests and external-model execution: **NOT RUN**. All displayed calculations are fresh exact written algebra.

## 1. Results and original-target boundary

Let
\[
\Phi_p(X)=(1-p)X+\frac p2\operatorname{Tr}(X)I_2,
\qquad 0\le p\le\frac43,
\]
put \(t=|1-p|\), \(a=(1+t)/2\), \(b=(1-t)/2\), and write
\[
D_t=\operatorname{diag}(a,b)^{\otimes4}.
\]
For Hermitian \(X\), let \(K_k(X)\) be its largest-\(k\) eigenvalue sum.

This candidate establishes the following explicitly scoped statements.

1. **Broad common-projector sector.** For every four-qubit density \(\rho\) invariant under the full spin flip
   \[
   \widetilde\rho=Y^{\otimes4}\rho^TY^{\otimes4}=\rho,
   \]
   every complex orthogonal rank-\(k\) projector satisfies the product-reference output bound for every physical \(p\) and every \(k\ne4\). The missing fourth prefix is also proved uniformly when
   \[
   0\le t\le t_*:=\frac{\sqrt{29}-2}{5},
   \]
   and at \(t=1\). Thus this whole sector has full output majorization for physical
   \[
   p\in\left[\frac{7-\sqrt{29}}5,\frac43\right]\cup\{0\}.
   \]
   The derivation uses the actual common-projector identity \(H_2=H_3+I\), not independent optimization of incompatible marginal layers. In this sector the requested separate \(H_2\) majorant is proved for every prefix, without a noise restriction.

2. **Full physical interval on a genuinely four-partite orbit.** For
   \[
   |D\rangle=|D_4^{(2)}\rangle
   =\frac{|0011\rangle+|0101\rangle+|0110\rangle+|1001\rangle+|1010\rangle+|1100\rangle}{\sqrt6},
   \qquad \rho_D=|D\rangle\langle D|,
   \]
   for every local product unitary \(V\), every physical \(p\), and every complex orthogonal rank-\(k\) projector \(Q\),
   \[
   \operatorname{Tr}[Q\Phi_p^{\otimes4}(V\rho_DV^\dagger)]
   \le K_k(D_t),\qquad k=1,\ldots,16.
   \]
   The same holds for every finite mixture of these local-unitary images. The proof includes exact compatible \(H_2\) and \(H_3\) spectra and all sixteen prefix gaps. This closes the fourth-prefix gap for this orbit even in the high-polarization region left unpaid by statement 1.

3. **Strict enlargement relative to the frozen adopted hull.** This pure Dicke state is outside the Class A/B hull in S3, outside the symmetric-W orbit hull in S4, and outside the biseparable set. Consequently, conditional on acceptance of this candidate, adjoining its local-unitary orbit genuinely enlarges the union of those two frozen adopted hulls. This is a statement relative to those named inputs, not an exhaustive comparison with every earlier regional sector or a novelty claim.

**Not established:** unrestricted four-qubit \(H_2\) majorization for every actual density, a physical counterexample to that assertion, unrestricted four-qubit channel majorization, or general blocklength. The unrestricted target is not declared solved. The permitted fallback—an actual genuinely four-partite class with a complete physical common-projector proof—is supplied.

## 2. Input coverage, acknowledgment and methods

Before mathematical packet access I read the complete manifest, freeze receipt, parent-live-metadata supply, dispatch receipt and all ten declared status/permission controls. I then recorded the pre-body acknowledgment at `local://f481-prebody-ack-v1.md`.

Only afterward I read the complete ordered literal packet through raw ranges 1–20, 21–40, and so on through 861–880 and 881–887, each containing at most 20 LF. This includes all endings:

- S1: logical source lines 1–783, the unreviewed F463 three-qubit candidate;
- S2: lines 1–12, the frozen Song–Chen direct-prior excerpt;
- S3: lines 1–48, the adopted Class A/B disposition;
- S4: lines 1–42, the adopted symmetric-W disposition.

Parent-supplied pins:

- Manifest: `b20d7ec1291d4c0141a1b588852d9ac0823bef09d21a655c71a03f1a331b8a88`.
- Freeze receipt: `4fb281acea6a8712e90395b71e39326a8d0d387b43c2afa808a9c544efb4a778`.
- Literal packet: `eec5650f88a53d6aff09668bb808efe9b341790776a6acb3959e7b596026d029`.

The clock `2026-10-30T12:13:16-0700 PDT`, hashes, byte counts and LF counts are parent-attributed observations. I did not execute native clock or hashing commands and do not describe the pins as child-verified.

After completing the packet I developed the arguments below by written algebra, selecting the Dicke state during this GENERAL AUTHOR duty. No additional source, linked sibling return, author code, held scientific payload or held consumer was opened. F439/F444/F448 and every genuinely held episode and consumer remain NONINPUT; their controls were read for status only. S1 remains unreviewed and its claimed theorems are not premises here. S3/S4 supply only their stated adopted-class comparison. No public webpage was opened; the Song–Chen bibliographic reference is inherited from the frozen excerpt, not a fresh source inspection.

There is no scientific program or executed experiment to reproduce. Exact input, marginal matrices, graph matrices, eigenvalues and every arithmetic prefix gap are provided below. The ≤55-second optional-calculation allowance was not exercised. No clean-cognition, independent-model-family, human, kernel, novelty or adoption assurance is asserted.

## 3. The actual physical expansion and reference multiplicities

For any four-qubit density, define
\[
H_j(\rho)=
\sum_{\substack{S\subseteq\{1,2,3,4\}\\|S|=j}}
\rho_S\otimes I_{S^c},
\qquad j=0,\ldots,4,
\]
with every tensor factor placed on its indicated physical qubit, \(H_0=I_{16}\), and \(H_4=\rho\). In particular, \(H_2\) contains the six marginals of one and the same actual density. All these operators are positive, and
\[
\operatorname{Tr}H_1=32,\qquad
\operatorname{Tr}H_2=24,\qquad
\operatorname{Tr}H_3=8.
\]

For the nonnegative branch define
\[
T_t(X)=tX+b\operatorname{Tr}(X)I_2,
\qquad b=(1-t)/2.
\]
Choosing the retained subset in the tensor expansion gives exactly
\[
\boxed{
T_t^{\otimes4}(\rho)
=t^4\rho+t^3bH_3+t^2b^2H_2+tb^3H_1+b^4I_{16}.
}
\tag{1}
\]
There are no extra binomial factors multiplying the \(H_j\): their definitions already sum over subsets. Its trace is
\[
t^4+8t^3b+24t^2b^2+32tb^3+16b^4=(t+2b)^4=1.
\]

For the product input \(|0000\rangle\), order the basis by Hamming weight. Its four nonconstant reference layers have decreasing spectra
\[
L_4=(1,0^{\times15}),
\]
\[
L_3=(4,1^{\times4},0^{\times11}),
\]
\[
\boxed{L_2=(6,3^{\times4},1^{\times6},0^{\times5}),}
\]
\[
L_1=(4,3^{\times4},2^{\times6},1^{\times4},0).
\]
These reference matrices have a common decreasing basis. Let \(R_j(k)=K_k(L_j)\). Their positively weighted sum in (1) is exactly \(D_t\), not a larger relaxation. At weights \(0,1,2,3,4\), its entries are respectively \(a^4,a^3b,a^2b^2,ab^3,b^4\), with multiplicities \(1,4,6,4,1\). Thus, for \(k\ge1\),
\[
K_k(D_t)
=t^4+t^3bR_3(k)+t^2b^2R_2(k)+tb^3R_1(k)+kb^4.
\tag{2}
\]

We use only the variational identity
\[
K_k(X)=
\max_{\substack{Q=Q^\dagger=Q^2\\\operatorname{rank}Q=k}}
\operatorname{Tr}(QX),
\tag{3}
\]
its convexity consequence, and the explicitly derived spectra below. Projectors may be arbitrary complex projectors.

## 4. A broad spin-flip-invariant compatible sector

Put \(W_n=Y^{\otimes n}\) and
\[
\mathcal J(X)=YX^TY=\operatorname{Tr}(X)I_2-X.
\]
Tensor expansion of this one-qubit identity gives, for four qubits,
\[
\widetilde\rho=I-H_1+H_2-H_3+\rho.
\tag{4}
\]
Suppose now that \(\widetilde\rho=\rho\). Partial trace commutes with the appropriate tensor spin flip: on a traced-out leg,
\[
\operatorname{Tr}\mathcal J(X)=\operatorname{Tr}X.
\]
Hence each one-qubit marginal satisfies \(\mathcal J(\rho_i)=\rho_i\), so
\[
\rho_i=I_2/2,\qquad H_1=2I_{16}.
\]
Equation (4) consequently becomes
\[
\boxed{H_2=I_{16}+H_3.}
\tag{5}
\]
This is an exact identity for the compatible layers and for every consuming projector.

Each three-qubit marginal \(\sigma\) is invariant under the antiunitary
\[
\Theta_3=W_3\mathcal K,\qquad \Theta_3^2=-I.
\]
If \(\sigma u=\lambda u\), invariance gives
\(\sigma\Theta_3u=\lambda\Theta_3u\); the two vectors are orthogonal because \(\Theta_3^2=-I\). The largest eigenvalue is therefore at least doubly represented and cannot exceed \(1/2\), since \(\operatorname{Tr}\sigma=1\). Thus every lifted three-body term is between \(0\) and \(I/2\), giving
\[
0\le H_3\le2I,\qquad
\operatorname{Tr}H_3=8,\qquad
I\le H_2\le3I.
\tag{6}
\]
No pure-input assumption was used.

For one fixed rank-\(k\) projector set
\[
h_3=\operatorname{Tr}(QH_3).
\]
Equations (5)–(6) give
\[
h_3\le m_k:=\min(2k,8),\qquad
\operatorname{Tr}(QH_2)=k+h_3.
\tag{7}
\]
The second equality is where the common-projector coupling enters. It is not a sum of separate attained maxima.

Define
\[
A_k=R_3(k)-m_k,\quad
B_k=R_2(k)-k-m_k,\quad
C_k=R_1(k)-2k.
\]
Direct use of the displayed reference spectra gives the complete table:

| \(k\) | \(A_k\) | \(B_k\) | \(C_k\) |
|---:|---:|---:|---:|
| 1 | 2 | 3 | 2 |
| 2 | 1 | 3 | 3 |
| 3 | 0 | 3 | 4 |
| 4 | −1 | 3 | 5 |
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

In particular, all \(B_k\ge0\); (7) proves the requested separate \(H_2\prec L_2\) for this entire invariant sector.

Using \(\operatorname{Tr}(Q\rho)\le1\) in the actual expansion, for the same \(Q\),
\[
K_k(D_t)-\operatorname{Tr}[QT_t^{\otimes4}(\rho)]
\ge t^3bA_k+t^2b^2B_k+tb^3C_k.
\tag{8}
\]
For every \(k\ne4\), the right side is nonnegative for all \(0\le t\le1\). For \(k=4\), it is
\[
\begin{aligned}
-t^3b+3t^2b^2+5tb^3
&=tb(-t^2+3tb+5b^2)\\
&=\frac{tb}{4}(5-4t-5t^2).
\end{aligned}
\tag{9}
\]
This is nonnegative for
\[
0\le t\le\frac{\sqrt{29}-2}{5},
\]
and is zero at \(t=1\). This proves statement 1 after the negative-branch transport in Section 8.

For \(t_*<t<1\), (9) becomes negative as an upper-bound deficit. This is **only a failure of this relaxation to prove the fourth prefix**, not a physical state, projector, layer counterexample or channel counterexample. All other prefixes—including the original rank-three target—remain proved throughout this invariant sector.

## 5. The actual two-excitation Dicke marginals

For the explicitly displayed \(\rho_D\), all marginals arise from that one physical pure state. Permutation symmetry allows any indicated subset to be used in these formulas.

Each one-qubit marginal is \(I_2/2\). For any pair,
\[
\rho_{ij}
=\frac16|00\rangle\langle00|
+\frac23|\psi^+\rangle\langle\psi^+|
+\frac16|11\rangle\langle11|,
\qquad
|\psi^+\rangle=(|01\rangle+|10\rangle)/\sqrt2.
\tag{10}
\]
For example, the Schmidt expansion across \(12|34\) is
\[
|D\rangle
=\frac1{\sqrt6}|00\rangle|11\rangle
+\sqrt{\frac23}|\psi^+\rangle|\psi^+\rangle
+\frac1{\sqrt6}|11\rangle|00\rangle.
\tag{11}
\]
For any triple,
\[
\rho_{ijk}
=\frac12|D_3^{(1)}\rangle\langle D_3^{(1)}|
+\frac12|D_3^{(2)}\rangle\langle D_3^{(2)}|.
\tag{12}
\]
Here \(|D_3^{(r)}\rangle\) is the normalized equal sum of the three strings with \(r=1\) or \(r=2\) excitations. Formula (12) follows by conditioning the omitted qubit on 1 or 0; both alternatives have probability \(1/2\).

The global spin flip exchanges each weight-two basis string with its complement with positive sign, so \(\widetilde\rho_D=\rho_D\). Thus this state belongs to Section 4’s sector, but its additional exact spectral structure will close the remaining high-polarization fourth prefix.

## 6. Exact layer diagonalization, including all multiplicities

Let \(\mathcal E_w\) be the span of weight-\(w\) computational basis strings. On \(\mathcal E_w\), let \(A_w\) be the adjacency matrix connecting two strings when one excitation is moved to an empty position. This is the Johnson graph \(J(4,w)\).

For \(w=1,3\), it is \(K_4\), with eigenvalues \(3,-1,-1,-1\). For \(w=2\), index the six two-element subsets, let \(M\) exchange each subset with its complement, and let \(J_6\) be the all-ones matrix. Then
\[
A_2=J_6-I-M.
\]
The constant vector has eigenvalue 4. The \(+1\) eigenspace of \(M\), orthogonal to the constant vector, has dimension 2 and eigenvalue \(-2\) for \(A_2\). The \(-1\) eigenspace of \(M\) has dimension 3 and eigenvalue 0 for \(A_2\). This proves the full spectrum
\[
4,\quad 0^{\times3},\quad (-2)^{\times2}
\]
without an external graph-theory premise.

In (10), a pair with equal bits contributes diagonal \(1/6\), a pair with distinct bits contributes diagonal \(1/3\), and swapping 01 with 10 contributes off-diagonal \(1/3\). Therefore
\[
H_2|_{\mathcal E_w}=d_wI+\frac13A_w,
\]
\[
d_w
=\frac{\binom w2+\binom{4-w}2}{6}
+\frac{w(4-w)}3.
\tag{13}
\]
The values of \(d_w\) for \(w=0,1,2,3,4\) are
\[
1,\quad 3/2,\quad 5/3,\quad 3/2,\quad 1.
\]

Likewise, every nonzero entry within either three-body component in (12) is \(1/6\). For adjacent weight-\(w\) strings, exactly two omitted positions agree, each contributing \(1/6\). The three-body sum is consequently
\[
H_3|_{\mathcal E_w}=e_wI+\frac13A_w,
\tag{14}
\]
where
\[
e_w=0,\quad 1/2,\quad 2/3,\quad 1/2,\quad 0
\]
respectively. At weights 0 and 4, \(A_w=0\). At weight 2, nonadjacent complementary strings differ at every position and receive no three-body off-diagonal contribution.

Combining (13)–(14) gives a simultaneous decreasing list for all four layers. Each row below denotes an actual orthogonal subspace, not independently chosen eigenvectors:

| Actual subspace | Multiplicity | \(\rho_D\) | \(H_3\) | \(H_2\) | \(H_1\) |
|---|---:|---:|---:|---:|---:|
| Symmetric vector in weight 2, namely \(D\) | 1 | 1 | 2 | 3 | 2 |
| Symmetric vectors in weights 1 and 3 | 2 | 0 | \(3/2\) | \(5/2\) | 2 |
| \(A_2=0\) subspace in weight 2 | 3 | 0 | \(2/3\) | \(5/3\) | 2 |
| Sum-zero subspaces in weights 1 and 3 | 6 | 0 | \(1/6\) | \(7/6\) | 2 |
| Weights 0 and 4, and \(A_2=-2\) subspace | 4 | 0 | 0 | 1 | 2 |

In particular,
\[
\lambda(H_2)
=\left(
3,(5/2)^{\times2},(5/3)^{\times3},
(7/6)^{\times6},1^{\times4}
\right),
\tag{15}
\]
\[
\lambda(H_3)
=\left(
2,(3/2)^{\times2},(2/3)^{\times3},
(1/6)^{\times6},0^{\times4}
\right).
\tag{16}
\]
The dimensions sum to 16. The traces are respectively
\[
3+5+5+7+4=24,\qquad 2+3+2+1=8,
\]
agreeing with the actual marginal multiplicities. Also \(H_2=I+H_3\), as independently forced by (5).

## 7. All sixteen exact Dicke prefix gaps and the physical channel

For this state define
\[
\Delta_j(k)=R_j(k)-K_k(H_j(\rho_D)),
\qquad j=1,2,3.
\]
The exact complete table from (15)–(16) and \(H_1=2I\) is:

| \(k\) | \(\Delta_1(k)\) | \(6\Delta_2(k)\) | \(6\Delta_3(k)\) |
|---:|---:|---:|---:|
| 1 | 2 | 18 | 12 |
| 2 | 3 | 21 | 9 |
| 3 | 4 | 24 | 6 |
| 4 | 5 | 32 | 8 |
| 5 | 6 | 40 | 10 |
| 6 | 6 | 36 | 6 |
| 7 | 6 | 35 | 5 |
| 8 | 6 | 34 | 4 |
| 9 | 6 | 33 | 3 |
| 10 | 6 | 32 | 2 |
| 11 | 6 | 31 | 1 |
| 12 | 5 | 24 | 0 |
| 13 | 4 | 18 | 0 |
| 14 | 3 | 12 | 0 |
| 15 | 2 | 6 | 0 |
| 16 | 0 | 0 | 0 |

Every entry is nonnegative. Thus both requested compatible two-body majorization and the three-body reference majorization hold on this orbit.

For every fixed complex rank-\(k\) projector, use the actual expansion (1):
\[
\begin{aligned}
\operatorname{Tr}[QT_t^{\otimes4}(\rho_D)]
&=t^4\operatorname{Tr}(Q\rho_D)
+t^3b\operatorname{Tr}(QH_3)
+t^2b^2\operatorname{Tr}(QH_2)
+2ktb^3+kb^4\\
&\le t^4+t^3bR_3(k)+t^2b^2R_2(k)+tb^3R_1(k)+kb^4\\
&=K_k(D_t).
\end{aligned}
\tag{17}
\]
This is a common-consuming-projector proof. It does not assume separate actual maxima can be attained together.

In fact the simultaneous decreasing table in Section 6 proves the stronger exact identity
\[
\boxed{
K_k(D_t)-K_k(T_t^{\otimes4}(\rho_D))
=t^3b\Delta_3(k)+t^2b^2\Delta_2(k)+tb^3\Delta_1(k).
}
\tag{18}
\]
Both actual and reference coefficient matrices are co-ordered. For \(0<t<1\), \(t^2b^2>0\), and every \(\Delta_2(k)>0\) for \(1\le k\le15\); hence every proper output prefix is strictly below the product prefix on this interval.

For completeness the actual full channel eigenvalues, in decreasing order, are the following five expressions with multiplicities \(1,2,3,6,4\):
\[
\begin{aligned}
& t^4+2t^3b+3t^2b^2+2tb^3+b^4,\\
& \frac32t^3b+\frac52t^2b^2+2tb^3+b^4,\\
& \frac23t^3b+\frac53t^2b^2+2tb^3+b^4,\\
& \frac16t^3b+\frac76t^2b^2+2tb^3+b^4,\\
& t^2b^2+2tb^3+b^4=a^2b^2.
\end{aligned}
\tag{19}
\]
The successive differences are
\[
t^4+\frac{t^3b+t^2b^2}{2},\quad
\frac{5(t^3b+t^2b^2)}6,\quad
\frac{t^3b+t^2b^2}{2},\quad
\frac{t^3b+t^2b^2}{6},
\]
so their asserted order has no unexamined eigenvalue crossing. Equations (15)–(19) are exact written derivations, not program output.

No divisions by \(t\), \(b\), populations, eigenvalue gaps or marginal eigenvalues occur. At \(t=0\), actual and reference outputs are \(I_{16}/16\). At \(t=1\), both have pure spectra. Thus degeneracies and both endpoints are included.

## 8. Physical negative branch, local bases and mixtures

The one-qubit identity
\[
T_{-t}=\mathcal J\circ T_t
\]
gives, on the full four-qubit system,
\[
T_{-t}^{\otimes4}(\rho)
=W_4[T_t^{\otimes4}(\rho)]^TW_4.
\tag{20}
\]
This is full transpose, not partial transpose. Hence output spectra agree for the two signs. For any complex orthogonal projector,
\[
\operatorname{Tr}[QT_{-t}^{\otimes4}(\rho)]
=\operatorname{Tr}[Q'T_t^{\otimes4}(\rho)],
\qquad Q'=W_4Q^TW_4,
\tag{21}
\]
and \(Q'\) is an orthogonal projector of the same rank. Here \(W_4^T=W_4\). The physical branch \(p>1\) has \(0<t\le1/3\), so it is included both in Section 4’s full-prefix region and in the all-\(t\) Dicke proof.

For a local product unitary \(V\), depolarizing covariance gives
\[
\Phi_p^{\otimes4}(V\rho_DV^\dagger)
=V\Phi_p^{\otimes4}(\rho_D)V^\dagger.
\]
The projector \(V^\dagger QV\) remains a rank-\(k\) projector. Linearity for a fixed \(Q\) then proves the same bound for every finite convex mixture of such local-unitary images, with different bases in different components. No input-independent postprocessing channel is asserted.

The broad sector in Section 4 also permits arbitrary physical local bases. The spin-flip map is covariant under local unitary conjugation: determinant phases cancel at density-operator level. Alternatively its bound is applied directly to any density satisfying \(\widetilde\rho=\rho\), without choosing a local normal form.

## 9. Genuine four-party content and comparison with the frozen adopted classes

Across every \(1|3\) cut, \(\rho_D\) has Schmidt coefficients
\[
1/\sqrt2,\quad1/\sqrt2.
\]
Across every \(2|2\) cut, (11) gives three nonzero Schmidt coefficients
\[
1/\sqrt6,\quad\sqrt{2/3},\quad1/\sqrt6.
\]
Therefore it is entangled across every bipartition.

A positive mixture equal to a rank-one density must have every positive-weight component supported on the same one-dimensional ray: its expectation on every vector orthogonal to that ray is zero, and positivity forces each component’s corresponding expectations to vanish. Thus a pure state entangled across every cut is not a mixture of states separable across varying cuts. This proves \(\rho_D\) is not biseparable.

For the particular frozen comparison:

- A Class A vector, with at most two physical product-basis coefficients, has Schmidt rank at most 2 across every paired cut.
- A pure Class B vector is supported in a two-dimensional repetition subspace on each side of at least one paired cut, so has Schmidt rank at most 2 across that paired cut. This remains true in arbitrary physical local bases and for any pairing.
- Every symmetric-W local-unitary image has paired-cut Schmidt rank 2.
- The Dicke vector has rank 3 across every paired cut, invariant under local unitaries and permutations.

Consequently \(\rho_D\) is in none of those pure classes. The same rank-one-mixture argument excludes it from the convex hull of their union, including mixtures of mixed Class B densities. It is therefore a strict additional pure direction relative to S3 and S4. If this candidate is accepted, convexity permits adjoining its whole orbit to those previously adopted classes, while preserving every exact projector and physical-parameter bound. This statement does not adopt the present candidate automatically or reclassify S1.

## 10. Exact remaining unrestricted obligations

The original unrestricted problem still ranges over every actual four-qubit density, including densities with \(\widetilde\rho\ne\rho\). Such inputs generally do not have \(H_1=2I\) or \(H_2=I+H_3\). No inference from this sector establishes those identities generally.

For unrestricted \(H_2\), the first prefix is immediate from \(\rho_{ij}\le I\), giving \(H_2\le6I\). Prefixes 11–16 are immediate from positivity and total trace 24. The still-unproved unrestricted inequalities are precisely
\[
K_k(H_2(\rho))\le
\begin{cases}
3k+3,&2\le k\le5,\\
k+13,&6\le k\le10.
\end{cases}
\tag{22}
\]
This return supplies neither a proof of (22) outside the stated sector nor a compatible physical counterexample.

For unrestricted \(H_3\), the elementary bounds settle the first prefix by \(H_3\le4I\) and prefixes 5–16 by trace 8. Its separate missing prefixes are
\[
K_2\le5,\qquad K_3\le6,\qquad K_4\le7.
\]
These observations are not presented as a substitute for the original channel target.

Without separate layer bounds, the exact unrestricted positive-branch common-projector obligation is, for every actual \(\rho\), every rank-\(k\) complex projector \(Q\), and every \(0\le t\le1\),
\[
\begin{aligned}
&t^4\bigl(1-\operatorname{Tr}(Q\rho)\bigr)
+t^3b\bigl(R_3(k)-\operatorname{Tr}(QH_3)\bigr)\\
&\quad+t^2b^2\bigl(R_2(k)-\operatorname{Tr}(QH_2)\bigr)
+tb^3\bigl(R_1(k)-\operatorname{Tr}(QH_1)\bigr)
\ge0.
\end{aligned}
\tag{23}
\]
This is exactly the difference between (2) and the actual physical expectation in (1). In particular all terms must use the same \(Q\). Sections 4 and 7 prove (23) on their declared actual-state scopes; the general assertion is unpaid. Within the invariant sector, the only unpaid all-noise prefix left by Section 4 is \(k=4\) with \(t_*<t<1\), and Section 7 closes that residual on the Dicke orbit and its finite convex hull.

No freely selected incompatible marginals, rank-only relaxation, or failure of a bound is called a physical counterexample. A failure of a layer would not by itself refute (23); this candidate provides no such counterexample to either layer or channel.

## 11. Prior-source qualification and acceptance status

The frozen S2 excerpt attributes the arbitrary shared-three-qubit weighted two-body theorem to [Zhiwei Song and Lin Chen, *A counterexample to the strong spin alignment conjecture*, arXiv:2603.25410v1, Proposition 3](https://arxiv.org/html/2603.25410v1). Equal weights give the exact three-qubit \(H_2\) theorem. It is **DIRECT PRIOR**, not a new theorem of this duty, and it is not an unrestricted four-qubit theorem. It is not needed as a premise for the four-qubit calculations above. The source’s incompatible-marginal strong-alignment counterexample is not imported as a physical channel example.

S1’s claimed three-qubit proof and \(1|3\)-separable consequence remain unreviewed inputs. Reading them did not accept them; neither supplies a hidden tensorization premise here. S3 and S4 retain only their declared adopted scopes. Their descriptions of older stronger printed claims do not establish validity, falsity, source equivalence or priority for this candidate. No source-miss or method-novelty claim is made.

All claims in this return remain AUTHOR / WRITTEN PROOF CANDIDATE until disjoint reconstruction and parent disposition. Load-bearing checks are the invariant-sector marginal/antiunitary argument, the actual multiplicities in (1), the combinatorial blocks (13)–(14), the sixteen-entry prefix tables, and full-transpose projector transport. No independent finite run or independent-family, human or formal/kernel verification has occurred in this duty.

**Completed deliverable:** an actual compatible-state proof of every two-body-layer prefix on the full spin-flip-invariant sector; a common-projector physical-channel bound on that sector for every prefix except the explicitly isolated fourth-prefix region; and a complete all-physical-parameter, all-prefix theorem for the genuinely four-partite two-excitation Dicke local-unitary orbit and its finite convex hull, with exact spectra and literal residual obligations. **Unrestricted four-qubit closure remains NOT PROVED. All scientific execution is NOT RUN; all genuine held episodes and consumers remain NONINPUT.**