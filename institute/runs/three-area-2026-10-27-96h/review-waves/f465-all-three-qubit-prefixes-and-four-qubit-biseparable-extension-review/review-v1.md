# F465 — Complete WRITTEN review

**Candidate:** Arbitrary complex three-qubit depolarizing-output majorization and its four-qubit \(1|3\)-separable extension.  
**Review result:** **SUPPORTED by the written reconstruction below.**  
**Findings:** **0 FATAL / 0 MAJOR / 0 MINOR.**  
**Acceptance boundary:** This is a same-harness written review, not a parent disposition, finite verification, independent-model-family review, human review, formal/kernel proof, or novelty determination.

No repository file was written. This is the complete body for parent materialization as the assigned wave’s `review-v1.md`.

## 1. Process, coverage, and evidence attribution

Before reading mathematical packet content, I read:

- The complete manifest, lines 1–120.
- The complete freeze receipt, lines 1–60.
- Every listed permission/status control through its ending.
- The complete parent live-metadata supply.

I then sent the required direct administrative pre-body ACK to Main. Only afterward did I read the complete literal packet, sequentially and raw, in windows of at most 20 lines: \(1\!-\!20,\ldots,841\!-\!860,861\!-\!875\). No packet elision remained.

Complete mathematical coverage was:

| Input | Coverage |
|---|---|
| S1 — F463 author candidate | All logical lines 1–783, including its ending |
| S2 — Adopted Class A/B disposition | All lines 1–48, including its ending |
| S3 — Adopted symmetric-W4 disposition | All lines 1–42, including its ending |

The wave’s dispatch receipt was also read completely.

The following are **parent-observed metadata**, not independently executed child measurements:

- Manifest SHA: `fae2be1192c7b05f436e27c42c40951f4f50faff6f2b2a383e21a4960a6d938a`.
- Receipt SHA: `4dcb81050d1d9c90106c314322975cc9dfa6bc0b5f3a1fb187eec81ca59624aa`.
- Packet SHA: `d0734474d26cb858b40b8ccd0a887a14d44cc08e1773139c64dbea552eb56eb6`.
- S1 SHA: `3e2cab0b74bc61af6179c442d0098a56d1f209e8dc7f39b6dd601cf1b0025907`.
- S2 SHA: `8522551e1088a796288c73c9b1aad8fa40e197d74b6f7d41447392d07370d6c0`.
- S3 SHA: `b15be59978ee1c50fe2b9a8ff91051df937fefb67e38b7183f5e634a2bdacab0`.

The supplied clock observation, `2026-10-30T11:57:24-0700 PDT`, is attributed to the parent. It is not my native start or completion time. I did not independently execute date, hashing, byte-equality, or LF-count commands.

### Method restrictions observed

This review used written algebra on the candidate’s formal variables and the expressly assigned \(\psi_*\) example only.

- Scientific code, CAS, interpreter, solver, enumeration, replay, builds, tests, linters, and formatters: **NOT RUN**.
- Fresh privately chosen mathematical instances: **none used**.
- Author programs, sibling review bodies, linked executable sources, and new public sources: **not opened**.
- F439/F444/F448 and other genuine held episodes and their consumers: **NONINPUT**.
- Status controls supplied exclusions only, not mathematical premises.
- No scientific executable source or argv was produced for this WRITTEN role.
- The finite evidence described in S2/S3 was not independently replayed here.

No assertion is made about unobservable cognition or about independently establishing the author’s reported historical chronology.

## 2. Claim-by-claim disposition

| Claim | Disposition | Principal evidence |
|---|---|---|
| Actual erasure expansion and its normalizations | **SUPPORTED** | S1 LF 116–138, 401–415 |
| Pure-input spin-flip coupling | **SUPPORTED** | S1 LF 141–214 |
| Load-bearing paired-projection proof of \(H_2\prec L_2\) | **SUPPORTED** | S1 LF 222–356; reconstruction below |
| \(H_1\prec L_1\) without a shared input normal form | **SUPPORTED** | S1 LF 362–395 |
| All eight prefixes for arbitrary complex three-qubit densities | **SUPPORTED** | S1 LF 417–490 |
| Full physical interval and complex-projector transport | **SUPPORTED** | S1 LF 492–549 |
| Assigned example lies outside every local-parity sector and their convex hull | **SUPPORTED** | S1 LF 555–605 |
| Assigned same-\(Q\) expectation \(623/1024\) | **SUPPORTED**, as an expectation, not a largest-eigenvalue calculation | S1 LF 609–649 |
| All sixteen prefixes on arbitrary \(1|3\)-separable inputs, including varying-cut mixtures | **SUPPORTED** | S1 LF 657–724 |
| All four-qubit biseparable inputs after importing the adopted all-\(2|2\) theorem | **SUPPORTED**, with that exact import | S2 LF 7–18, 32–34 |
| Unrestricted four-qubit majorization or unrestricted four-qubit \(k=3\) closure | **NOT ESTABLISHED** | Explicitly excluded by S1 LF 772–779 |
| Novelty, priority, or validity/equivalence of older printed source proofs | **INCONCLUSIVE / NOT AUDITED** | Not a premise of this reconstruction |

The last two rows are scope boundaries, not defects in the candidate’s stated theorem.

## 3. Actual channel expansion and normalization

Write
\[
T_t(X)=tX+b\,\operatorname{Tr}(X)I_2,\qquad
b=\frac{1-t}{2},\qquad 0\le t\le1,
\]
and
\[
a=t+b=\frac{1+t}{2}.
\]

For a trace-one three-qubit density \(\rho\), use the actual physical-factor lifts
\[
H_1=
\rho_A\otimes I_{BC}
+\rho_B\otimes I_{AC}
+\rho_C\otimes I_{AB},
\]
and
\[
H_2=
\rho_{AB}\otimes I_C
+\rho_{AC}\otimes I_B
+\rho_{BC}\otimes I_A.
\]

Identity factors here are **unnormalized**. Consequently,
\[
\operatorname{Tr}H_1=3\cdot4=12,\qquad
\operatorname{Tr}H_2=3\cdot2=6.
\]

Expanding the three factors of \(T_t\), classified by the number of trace-and-replace factors, gives exactly
\[
T_t^{\otimes3}(\rho)
=t^3\rho+t^2bH_2+tb^2H_1+b^3I_8.
\]

There is no missing binomial coefficient: the three terms of each marginal sum already enumerate the corresponding choices of replaced factors. Its trace is
\[
t^3+6t^2b+12tb^2+8b^3
=(t+2b)^3=1.
\]

This is an expansion of the actual channel on the actual input. It does not replace actual marginals by independently chosen matrices.

On the negative physical branch, this nonnegative-coefficient expansion is applied to the positive companion \(T_t\); the negative channel is handled separately by full-transpose transport in Section 7 below.

## 4. Independent reconstruction of the load-bearing \(H_2\) lemma

The claim to establish is
\[
H_2(\rho)\prec
L_2=\operatorname{diag}(3,1,1,1,0,0,0,0)
\]
for every three-qubit density, with no restriction to parity, real amplitudes, or particular local bases.

### 4.1 Actual pure-input coupling

Define the antiunitary
\[
\Theta=Y^{\otimes3}\mathcal K.
\]
Since \(\overline Y=-Y\),
\[
\Theta^2=-I.
\]
For Hermitian \(X\), let
\[
\widetilde X=\Theta X\Theta^{-1}
=Y^{\otimes3}X^TY^{\otimes3}.
\]

The one-qubit identity
\[
YX^TY=\operatorname{Tr}(X)I-X
\]
holds without a reality assumption. Tensor-expanding it on the actual three-qubit density yields
\[
\widetilde\rho=I-H_1+H_2-\rho.
\]

Now suppose \(\rho=|\psi\rangle\langle\psi|\). Antiunitarity and \(\Theta^2=-I\) imply
\[
\langle\psi,\Theta\psi\rangle=0.
\]
Thus
\[
P=\rho+\widetilde\rho
\]
is an orthogonal rank-two projection. It satisfies \(\widetilde P=P\).

Rearranging the actual marginal identity gives
\[
H_2=P+H_1-I.
\]
Each one-qubit density is transformed into its complementary density, while identity factors are unchanged, so
\[
\widetilde H_1=3I-H_1.
\]
Therefore
\[
H_2+\widetilde H_2=I+2P.
\]

Both terms on the left are positive. Positivity of the first follows from its marginal construction; positivity of the second follows from antiunitary conjugation.

The rank-two projection in this equation comes from the same actual pure input as \(H_2\). No freely chosen marginal-spectrum substitute has been introduced.

### 4.2 Reduction to complementary paired contractions

Put
\[
G=I+2P,\qquad
Z=G^{-1/2}H_2G^{-1/2}.
\]
The eigenvalues of \(G\) are \(3\) on \(\operatorname{ran}P\) and \(1\) on its orthogonal complement. Hence \(G\) is invertible in every case.

Because \(G\) is \(\Theta\)-invariant, its positive inverse square root is also \(\Theta\)-invariant. Congruencing the preceding coupling therefore gives
\[
Z+\widetilde Z=I,\qquad 0\le Z\le I.
\]

No commutation between \(G\) and \(H_2\) is assumed or needed. In particular, this step does not identify the eigenvalues of \(H_2\) by multiplying eigenvalues of \(G\) and \(Z\).

If \(Zu=\lambda u\), then
\[
Z(\Theta u)=(1-\lambda)\Theta u.
\]
Complementary eigenspaces are therefore paired by \(\Theta\). For the \(1/2\)-eigenspace, \(\Theta\) preserves the space and has square \(-I\); choosing a unit vector and its orthogonal partner, then proceeding in their invariant orthogonal complement, supplies an orthonormal paired basis there as well.

Thus the full eight-dimensional space admits an orthonormal basis
\[
u_1,\Theta u_1,\ldots,u_4,\Theta u_4
\]
such that
\[
Z=\sum_{i=1}^4
\left(
\lambda_i|u_i\rangle\langle u_i|
+(1-\lambda_i)|\Theta u_i\rangle\langle\Theta u_i|
\right),
\qquad 0\le\lambda_i\le1.
\]

Select one vector from each pair. Each selection defines a rank-four orthogonal projector \(\Pi_s\) satisfying
\[
\widetilde\Pi_s=I-\Pi_s.
\]
Giving a selection the product of its four corresponding probabilities produces nonnegative weights \(w_s\) summing to one, with
\[
Z=\sum_s w_s\Pi_s.
\]
This remains valid when eigenvalues equal \(0\), \(1\), or \(1/2\).

It follows that
\[
H_2=\sum_s w_sX_s,\qquad
X_s=G^{1/2}\Pi_sG^{1/2}.
\]

### 4.3 Spectrum of each congruenced projection

Fix one such \(\Pi=\Pi_s\). Since \(P\) is \(\Theta\)-invariant,
\[
\overline{\operatorname{Tr}(P\Pi)}
=\operatorname{Tr}(P(I-\Pi)).
\]
The trace of a product of two Hermitian matrices is real. Because \(\operatorname{Tr}P=2\), this establishes
\[
\operatorname{Tr}(P\Pi)=1.
\]

On the four-dimensional range of \(\Pi\), the compression \(\Pi P\Pi\) is positive, has rank at most two, and has trace one. Consequently its eigenvalues can be written as
\[
\eta,\quad 1-\eta,\quad0,\quad0,
\qquad 0\le\eta\le1,
\]
including the rank-one cases.

The nonzero eigenvalues of
\[
X=G^{1/2}\Pi G^{1/2}
\]
are the eigenvalues of the compression of \(G\) to \(\operatorname{ran}\Pi\). This follows from the equality of the nonzero spectra of \(BB^\dagger\) and \(B^\dagger B\), taking \(B=G^{1/2}\Pi\).

That compression is
\[
I_{\operatorname{ran}\Pi}+2\Pi P\Pi.
\]
Hence the full spectrum of \(X\), before rearrangement, is
\[
1+2\eta,\quad3-2\eta,\quad1,\quad1,\quad0,\quad0,\quad0,\quad0.
\]

The first two displayed eigenvalues are both at least \(1\), at most \(3\), and sum to \(4\). Its decreasing prefixes therefore obey
\[
K_1(X)\le3,\quad K_2(X)=4,\quad
K_3(X)=5,\quad K_k(X)=6\quad(4\le k\le8).
\]
These are precisely the prefix bounds supplied by \(L_2\), with equal total trace. Thus
\[
X_s\prec L_2
\]
for every selection.

Convexity of each Ky Fan prefix now proves
\[
H_2\prec L_2
\]
for every pure input.

The auxiliary \(X_s\) need not themselves be physical marginal sums. Their physical realization is not asserted or required: the actual \(H_2\) has been explicitly expressed as their convex combination.

### 4.4 Every mixed complex input

For an arbitrary spectral decomposition
\[
\rho=\sum_j r_j|\psi_j\rangle\langle\psi_j|,
\]
linearity of \(H_2\) gives
\[
H_2(\rho)=\sum_jr_jH_2(|\psi_j\rangle\langle\psi_j|).
\]
Applying the pure-state result and Ky Fan convexity proves the same majorization for every mixed density.

One does **not** need a common rank-two \(P\) for all components or for the mixed density itself.

**Conclusion:** The paired-projection lemma is supported for its full stated quantifiers. I find no unpaid gate in this argument.

## 5. The \(H_1\) majorant requires no shared normal form

Diagonalize the three one-qubit marginals separately:
\[
\rho_i=V_i\operatorname{diag}(q_i,1-q_i)V_i^\dagger.
\]
There is no requirement that these eigenbases put the full input into any particular normal form.

Let
\[
L_1^{\mathrm{comp}}
=\sum_{i=A,B,C}|0\rangle\langle0|_i\otimes I_{\bar i}.
\]
Its spectrum, in increasing Hamming-weight order, is
\[
L_1=\operatorname{diag}(3,2,2,2,1,1,1,0).
\]

Choose the three bits independently, with probabilities \(q_i\) and \(1-q_i\), and conjugate \(L_1^{\mathrm{comp}}\) by
\[
U_s=\bigotimes_i V_iX^{s_i}.
\]
Averaging replaces the distinguished one-qubit projector in the \(i\)-th summand by exactly \(\rho_i\), while leaving its identity factors unchanged. The average is therefore exactly \(H_1\).

It follows that
\[
H_1\prec L_1.
\]
Arbitrary complex \(V_i\), degenerate marginals, and endpoint probabilities cause no problem.

## 6. Same-\(Q\) combination yields the exact reference

Fix an arbitrary complex orthogonal rank-\(k\) projector \(Q\), with \(1\le k\le8\). The actual expansion gives
\[
\begin{aligned}
\operatorname{Tr}\!\left[QT_t^{\otimes3}(\rho)\right]
&=t^3\operatorname{Tr}(Q\rho)
+t^2b\operatorname{Tr}(QH_2)
+tb^2\operatorname{Tr}(QH_1)+kb^3\\
&\le t^3+t^2bK_k(L_2)+tb^2K_k(L_1)+kb^3.
\end{aligned}
\]

The same \(Q\) occurs in every actual term. All coefficients are nonnegative. The bounds on its terms are uniform; simultaneous attainment for the actual input is neither asserted nor needed.

The relevant prefix lists are
\[
K_k(L_2):\quad 3,4,5,6,6,6,6,6,
\]
and
\[
K_k(L_1):\quad 3,5,7,9,10,11,12,12.
\]

For the product input \(|000\rangle\langle000|\), the reference matrices \(\rho_0\), \(H_2(\rho_0)\), \(H_1(\rho_0)\), and \(I\) are all diagonal in a common decreasing order indexed by Hamming weight. Their weighted entries at weights \(0,1,2,3\) are
\[
\begin{aligned}
&t^3+3t^2b+3tb^2+b^3=a^3,\\
&t^2b+2tb^2+b^3=a^2b,\\
&tb^2+b^3=ab^2,\\
&b^3.
\end{aligned}
\]

Because \(a\ge b\ge0\), this order is decreasing, including tied cases. The upper bound is consequently **exactly**
\[
K_k\!\left(\operatorname{diag}(a,b)^{\otimes3}\right),
\]
not a larger relaxed bound.

With
\[
u=a^3,\quad d=a^2b,\quad c=ab^2,\quad \ell=b^3,
\]
the eight prefixes are
\[
u,\quad u+d,\quad u+2d,\quad u+3d,\quad
u+3d+c,\quad u+3d+2c,\quad u+3d+3c,\quad1.
\]

Maximizing the left side over \(Q\) proves all eight output-prefix inequalities. The final traces agree, so this is majorization, not merely weak majorization.

Nothing in this argument pinches parity, discards a cross-parity block, or restricts amplitudes to be real.

## 7. Physical interval, negative branch, and endpoints

Let \(s=1-p\). The stated physical interval is
\[
-\frac13\le s\le1,
\]
consistent with the Pauli probabilities
\[
q_I=\frac{1+3s}{4},\qquad
q_X=q_Y=q_Z=\frac{1-s}{4}.
\]

For \(s\ge0\), the preceding proof applies with \(t=s\). For \(s=-t\), define
\[
\mathcal J(X)=YX^TY=\operatorname{Tr}(X)I-X.
\]
Direct substitution gives
\[
T_{-t}=\mathcal J\circ T_t.
\]
Thus, with \(W_n=Y^{\otimes n}\),
\[
T_{-t}^{\otimes n}(\rho)
=W_n[T_t^{\otimes n}(\rho)]^TW_n.
\]

This is **full transpose**, not partial transpose. It preserves the spectrum after unitary conjugation.

For an arbitrary complex orthogonal projector \(Q\),
\[
\operatorname{Tr}\!\left[QT_{-t}^{\otimes n}(\rho)\right]
=\operatorname{Tr}\!\left[Q'T_t^{\otimes n}(\rho)\right],
\qquad Q'=W_nQ^TW_n.
\]
Indeed, transposing \(W_nQW_n\) introduces two factors from
\(W_n^T=(-1)^nW_n\); they cancel. There is no residual minus sign when \(n\) is odd. The transported \(Q'\) remains an orthogonal projector of the same rank.

The physical negative branch needs only \(0\le t\le1/3\). No claim that \(\mathcal J\) is completely positive is required.

The endpoint handling is also sound:

- \(t=0\): the three-qubit output and reference are \(I_8/8\).
- \(t=1\): the reference is pure, and the bound reduces to \(\operatorname{Tr}(Q\rho)\le1\).
- \(p=4/3\): covered by the negative branch at \(t=1/3\).
- \(G\) always has eigenvalues \(1\) and \(3\).
- No argument divides by a population, spectral gap, \(t\), \(b\), or a marginal eigenvalue.

This establishes Theorem A for every stated physical parameter and every complex input/projector.

## 8. Expressly assigned non-parity example

Take only the assigned state
\[
|\psi_*\rangle
=\frac{|000\rangle+|001\rangle+|010\rangle+|100\rangle}{2}.
\]

### 8.1 Exclusion of every local-parity representation

Each one-qubit marginal is
\[
m=\begin{pmatrix}3/4&1/4\\1/4&1/4\end{pmatrix}
=\frac12\left(I+\frac{X+Z}{2}\right),
\]
with distinct eigenvalues
\[
\frac{1\pm1/\sqrt2}{2}.
\]

If \(\psi_*\) were an eigenvector of
\(A_1\otimes A_2\otimes A_3\), with each \(A_i\) a traceless Hermitian one-qubit unitary, invariance of its density under that product unitary would imply
\[
A_imA_i=m.
\]
Hence \(A_i\) commutes with \(m\). Its nondegeneracy forces
\[
A_i=\pm H,\qquad H=\frac{X+Z}{\sqrt2}.
\]

For the assigned support, the Hadamard signs sum to \(4+2+2+2=10\), so
\[
\langle\psi_*|H^{\otimes3}|\psi_*\rangle
=\frac{10}{4\sqrt8}
=\frac5{4\sqrt2}.
\]
Its squared magnitude is
\[
\frac{25}{32}<1.
\]
Changing local signs changes only the overall sign. This contradicts the unit-magnitude expectation required of a parity eigenvector.

A rank-one density commuting with a parity observable must lie in one of its eigenspaces. Therefore the assigned density is outside every local-basis parity-preserving sector.

Moreover, if a positive convex combination equals a rank-one density, each positive-weight component is supported on that same ray. Thus a convex combination of local-basis parity-preserving densities cannot produce this density either.

The example therefore genuinely demonstrates coverage beyond the local-parity hull.

### 8.2 Exact same-projector channel expectation

For the assigned
\[
p=\frac14,\qquad t=\frac34,\qquad b=\frac18,
\]
take the actual projector
\[
Q_*=|\psi_*\rangle\langle\psi_*|.
\]

The displayed marginal gives
\[
\operatorname{Tr}(m^2)=\frac34.
\]
The expectation of each lifted one-body marginal equals its marginal purity. For this pure input, each complementary two-body marginal has the same nonzero spectrum as its one-body complement. Therefore
\[
\operatorname{Tr}(Q_*H_1)
=\operatorname{Tr}(Q_*H_2)=\frac94.
\]

Using the actual channel expansion,
\[
\begin{aligned}
\operatorname{Tr}\!\left[Q_*T_{3/4}^{\otimes3}(Q_*)\right]
&=t^3+\frac94(t^2b+tb^2)+b^3\\
&=\frac{432+189+2}{1024}\\
&=\frac{623}{1024}.
\end{aligned}
\]
The rank-one product-reference bound is
\[
a^3=\left(\frac78\right)^3
=\frac{686}{1024}.
\]

This confirms the exact stated **same-\(Q\) expectation**. It does not calculate or identify the largest output eigenvalue, and it is not finite executable verification or a substitute for the universal proof.

## 9. Positive tensor preservation and the full \(1|3\) extension

Set \(K_0=0\). If \(X,Y\) are positive and \(x_i\) are the eigenvalues of \(X\), the direct-sum decomposition of \(X\otimes Y\) gives
\[
K_k(X\otimes Y)
=\max_{\substack{0\le k_i\le\dim Y\\\sum_i k_i=k}}
\sum_i x_iK_{k_i}(Y).
\]

If \(Y\prec Y_0\), every term is bounded by the corresponding expression using \(Y_0\), because \(x_i\ge0\). Hence
\[
K_k(X\otimes Y)\le K_k(X\otimes Y_0).
\]
Diagonalizing positive \(Y_0\) and applying the same reasoning to \(X\prec X_0\) gives
\[
X\otimes Y\prec X_0\otimes Y_0.
\]
Trace equality supplies the final majorization equality. Zero eigenvalues require no separate division or limiting argument.

For every one-qubit density \(\sigma\), its physical channel output has ordered eigenvalues
\[
\frac{1+tr}{2},\quad\frac{1-tr}{2},
\qquad0\le r\le1,
\]
and is majorized by \(D_{1,t}=\operatorname{diag}(a,b)\).

Combining this fact with Theorem A yields
\[
\Phi_p(\sigma)\otimes\Phi_p^{\otimes3}(\tau)
\prec D_{1,t}\otimes D_{1,t}^{\otimes3}
=D_{1,t}^{\otimes4}
\]
for arbitrary one-qubit \(\sigma\) and arbitrary three-qubit \(\tau\).

For a state separable across a specified \(1|3\) cut, linearity and a fixed consuming \(Q\) permit averaging this bound over its product decomposition. Physical qubit permutations intertwine the identical local channels and preserve projector rank. Consequently the singleton position can also vary between mixture components.

The reference spectrum is
\[
a^4,\quad
a^3b\ \text{(four copies)},\quad
a^2b^2\ \text{(six copies)},\quad
ab^3\ \text{(four copies)},\quad
b^4.
\]
Thus all sixteen prefixes follow, including
\[
K_3\le a^4+2a^3b.
\]

This proves the candidate’s full \(1|3\)-separable assertion, not merely a product-with-pure-spectator special case.

## 10. Parent-requested all-biseparable corollary

The exact additional import is the already adopted S2 theorem:

> For every four-qubit state separable across any fixed \(2|2\) cut, and for mixtures across the balanced cuts, every physical \(p\) and every complex rank-\(k\) projector satisfy the product-reference prefix bound for all \(k=1,\ldots,16\).

This scope is explicitly supplied by S2 LF 7–18 and 32–34. I have not followed its author/reviewer/program links or independently recertified its historical finite checks.

There are seven nontrivial **unordered** four-qubit bipartitions:

- Four \(1|3\) cuts, covered by the reconstruction above.
- Three \(2|2\) cuts, covered by the exact retained S2 import.

A biseparable density is a convex combination of densities separable across these cuts; its cut may vary by component. Every component obeys the same reference bound at the same \(p\). For any fixed complex rank-\(k\) projector,
\[
\operatorname{Tr}\!\left[Q\Phi_p^{\otimes4}(\rho)\right]
\le\sum_jw_jK_k(D_{1,t}^{\otimes4})
=K_k(D_{1,t}^{\otimes4}).
\]
Trace equality then proves
\[
\boxed{\Phi_p^{\otimes4}(\rho)\prec D_{1,t}^{\otimes4}}
\]
for **every four-qubit biseparable density**, every physical \(p\), and all sixteen prefixes.

This is a convex-hull argument; it does not require a common cut, common local bases, common maximizing projector, or input-independent postprocessing channel.

S3’s symmetric-W4 theorem is a separately retained sector. It is not needed for this corollary, and I do not use a claimed set-inclusion or strictness relation between the new biseparable result and the entire earlier Class A/B/W4 hull.

## 11. Exact residuals and nonconclusions

The written reconstruction establishes unrestricted complex **three-qubit** majorization and, with the stated import, all **four-qubit biseparable** majorization.

It does not establish:

- Majorization for every genuinely four-party-entangled input.
- Unrestricted four-qubit \(k=3\) or all-index closure.
- General blocklength, general local dimension, or arbitrary auxiliary-channel tensorization.
- Validity of the older full group-channel propositions or their iteration.
- A statement counterexample merely from an older source-proof gap.
- Novelty, priority, or equivalence to an uninspected journal proof.

The public-literature descriptions in S1/S3 are not premises of this proof. I did not independently audit those publications in this WRITTEN duty. Neither their validity nor their falsity follows from this review.

## 12. Final verdict

**Findings:** None. **0 FATAL / 0 MAJOR / 0 MINOR.**

**Overall correctness:** correct.

**Explanation:** The load-bearing \(H_2\) paired-projection lemma withstands the independent written reconstruction, and its combination with the co-ordered actual erasure expansion proves all eight prefixes for arbitrary complex three-qubit densities. Positive tensor preservation and convexity establish every \(1|3\)-separable four-qubit case; importing the supplied adopted all-\(2|2\) theorem then establishes all biseparable four-qubit cases, without closing the unrestricted four-qubit target.

**Confidence:** 0.97.

**Disposition boundary:** Supported written-review return only. Parent acceptance/materialization remains required; no automatic adoption, novelty, independent-family, human, kernel, or unrestricted-four-qubit credit is asserted.