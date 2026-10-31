# F511 WRITTEN review — Four-qubit two-excitation Dicke all-prefix orbit theorem

**Overall correctness: correct within the frozen, explicitly restricted scope.**  
**Confidence: 0.99.**  
**Findings: 0 FATAL / 0 MAJOR / 0 MINOR.**

The actual Dicke marginals, compatible-layer diagonalization, all sixteen prefix gaps, physical negative-branch transport, local-unitary and convex-mixture extensions, and strict separation from the named earlier hulls are supported by written reconstruction. This does not establish unrestricted four-qubit majorization, novelty, or independent-family/human/kernel verification, and it does not constitute parent adoption.

## 1. Review identity, coverage and process

This is the full review body for the frozen wave `f511-four-qubit-two-excitation-dicke-all-prefix-orbit-review`. No repository file was edited; this body is returned for parent materialization.

Parent-supplied freeze identifiers:

- Manifest SHA256: `aea343580cd435ad7b0dd2103ee0f81c22412e89348bc3d009d2f186027c4916`.
- Freeze-receipt SHA256: `8a72cea12effa2d3fb32f2377935b7e9bc5088118a7348584c183ef0c81ea72d`.
- Literal-packet SHA256: `d6297fcdb769936d50339c7be539131ee912ca48aa90f1f5600130f30dcf2a9c`.

These hashes, byte counts and clocks are **parent-attributed metadata**, not independently executed child hash or clock observations.

Before mathematical packet access, I completely read:

1. `manifest-v1.json`, LF 1–139.
2. `freeze-receipt-v1.json`, LF 1–73.
3. `parent-dispatch-receipt-v1.json`, through its ending.
4. `parent-live-metadata-supply-v1.json`, through its ending.
5. All eleven `controls_before_body`, through their endings, solely for permissions, exclusions, historical status and transport qualifications.

I then sent an administrative pre-body acknowledgement to `agent://Main`. The tool returned **“Delivered to Main.”** This occurred before the first mathematical packet read.

After that delivery, I read the entire `literal-packet-v1.md` in contiguous, ordered raw windows of at most twenty LF: 1–20, 21–40, continuing through 621–640 and 641–654. All source endings were included:

| Frozen input | Complete logical source coverage | Packet ending |
|---|---:|---:|
| S1: F481 author candidate | 1–523 | 525 |
| S2: adopted Class A/B disposition | 1–48 | 573 |
| S3: adopted symmetric-W4 disposition | 1–42 | 615 |
| S4: adopted three-qubit/biseparable disposition | 1–39 | 654 |

S1 has 522 LF delimiters and 523 logical source lines; the final logical line was read. No elision or truncated-line marker appeared in these raw packet reads. Mathematical reconstruction began only after the complete packet ending.

**Methods actually used:** written algebra and reasoning on the frozen author’s formal parameters and explicitly supplied Dicke state.

**NOT RUN:** scientific code, CAS, interpreter, solver, enumeration, numerical experiments, finite replay, builds, tests, linters, formatters, external-model CLI or paid/heavy execution. No additional source, linked review, sibling scientific body, author code or held payload was opened. No new selected mathematical instance or private probe was introduced.

The F439/F444/F448 episodes and every other listed held episode and consumer remain **HELD/ZERO/NONINPUT**. Their status controls supplied no mathematical premise.

The historical transport qualifications are retained: F480’s transcript-only acknowledgement and F481/F483’s local-only pre-body acknowledgements are not represented as direct delivery. Under owner addendum 2, those transport faults alone do not automatically establish mathematical invalidity. This review does not backdate or repair their delivery history.

## 2. Exact source and import boundaries

The mathematical candidate reviewed here is **F511 S1**, namely the complete F481 author body. References inside that body to its earlier “S1/S2/S3/S4” concern the F481 packet’s original labels, not the present packet’s labels.

The present review uses:

- **F511 S1:** the actual Dicke state, expansion, marginal matrices, graph blocks, spectra, prefix tables and transport proof, reconstructed below.
- **F511 S2, LF 9–14:** the definitions of Class A, Class B and their finite convex hull.
- **F511 S3, LF 7–13:** the symmetric-W4 local-unitary orbit, its convex extension and paired-cut structure.
- **F511 S4, LF 11–17:** the exact previously adopted three-qubit and four-qubit biseparable scopes.
- **F511 S4, LF 3 and 35:** the frozen attribution of the compatible three-qubit weighted marginal result to Song–Chen.

No earlier finite experiment, reported reviewer verdict or unreviewed three-qubit theorem is a premise for the Dicke calculation. The earlier-class definitions are sufficient for the separation argument; their linked proof and executable bodies were not followed.

## 3. Claim dispositions

| Claim | Disposition | Principal source location |
|---|---|---|
| Actual pair and triple Dicke reductions | **SUPPORTED** | S1 LF 243–274 |
| Physical four-qubit marginal-layer expansion and product reference | **SUPPORTED** | S1 LF 76–137 |
| Johnson-block construction and complete spectra | **SUPPORTED** | S1 LF 276–347 |
| Simultaneous decreasing layer ordering, multiplicities \(1,2,3,6,4\) | **SUPPORTED** | S1 LF 316–347 |
| Complete sixteen-row Dicke prefix-gap table | **SUPPORTED** | S1 LF 349–377 |
| Fixed-complex-projector bound and exact output-prefix gap | **SUPPORTED** | S1 LF 379–424 |
| Full physical interval, including negative branch | **SUPPORTED** | S1 LF 426–445 |
| Arbitrary physical local bases and finite mixtures | **SUPPORTED** | S1 LF 447–454 |
| Genuine four-party entanglement and strict named-hull separation | **SUPPORTED** | S1 LF 456–477 |
| Stated invariant-sector identities and restricted prefix conclusion | **SUPPORTED at their stated scope** | S1 LF 139–241 |
| Unrestricted four-qubit or general-blocklength closure | **NOT ESTABLISHED**, correctly excluded | S1 LF 479–513, 523 |
| Mathematical or method novelty | **INCONCLUSIVE / not claimed** | S1 LF 515–521; S4 LF 35 |

No assigned mathematical claim is refuted by this review.

## 4. Actual-state marginal reconstruction

Write the author’s fixed state as

\[
|D\rangle=\frac1{\sqrt6}\sum_{|x|=2}|x\rangle,
\qquad \rho_D=|D\rangle\langle D|.
\]

Permutation symmetry means a calculation on one indicated pair or triple applies to every corresponding physical subset. It does not permit replacing the marginals by independently chosen densities.

### 4.1 One-body and three-body reductions

Across a \(1|3\) cut,

\[
|D\rangle
=\frac1{\sqrt2}
\left(
|0\rangle|D_3^{(2)}\rangle+
|1\rangle|D_3^{(1)}\rangle
\right).
\]

The two three-qubit vectors are normalized and orthogonal because they have different excitation numbers. Therefore

\[
\rho_i=\frac{I_2}{2},
\qquad
\rho_{ijk}
=\frac12|D_3^{(1)}\rangle\langle D_3^{(1)}|
+\frac12|D_3^{(2)}\rangle\langle D_3^{(2)}|.
\]

Consequently the actual lifted one-body sum is

\[
H_1=\sum_i\rho_i\otimes I_{i^c}=2I_{16}.
\]

These are S1’s equations (12) and the stated one-body reduction.

### 4.2 Pair reduction

Across \(12|34\), the author’s expansion is

\[
|D\rangle
=\frac1{\sqrt6}|00\rangle|11\rangle
+\sqrt{\frac23}|\psi^+\rangle|\psi^+\rangle
+\frac1{\sqrt6}|11\rangle|00\rangle,
\]

where \(|\psi^+\rangle=(|01\rangle+|10\rangle)/\sqrt2\). Its three right-hand vectors are orthonormal. Thus every pair marginal is

\[
\rho_{ij}
=\frac16|00\rangle\langle00|
+\frac23|\psi^+\rangle\langle\psi^+|
+\frac16|11\rangle\langle11|.
\]

In the physical computational basis its equal-bit diagonal entries are \(1/6\), its distinct-bit diagonal entries are \(1/3\), and its \(01\leftrightarrow10\) entries are \(1/3\). No other entries occur. This verifies S1’s equations (10)–(11).

### 4.3 Spin flip

On a weight-two four-qubit basis vector, \(Y^{\otimes4}\) sends it to its complementary weight-two vector with positive sign. The equal sum is invariant, and \(|D\rangle\) is real. Hence

\[
Y^{\otimes4}\rho_D^T Y^{\otimes4}=\rho_D.
\]

This is an actual-state property, not an independent-marginal assumption.

## 5. Physical expansion and exact reference

For \(0\le t\le1\), put

\[
b=\frac{1-t}{2},\qquad a=t+b=\frac{1+t}{2},
\qquad
T_t(X)=tX+b\operatorname{Tr}(X)I_2.
\]

Selecting the retained physical legs in the tensor product gives

\[
T_t^{\otimes4}(\rho)
=t^4\rho+t^3bH_3+t^2b^2H_2+tb^3H_1+b^4I_{16}.
\]

Each \(H_j\) already sums over all subsets of size \(j\), so no additional binomial coefficient belongs in front of it. The lifted marginal traces are \(8,24,32\) for \(H_3,H_2,H_1\), respectively, and the total output trace is

\[
t^4+8t^3b+24t^2b^2+32tb^3+16b^4=(t+2b)^4=1.
\]

For the product input \(|0000\rangle\), a weight-\(w\) basis vector has layer values \(\binom{4-w}{j}\). The nonconstant layer spectra are consequently

\[
\begin{aligned}
L_4&=(1,0^{\times15}),\\
L_3&=(4,1^{\times4},0^{\times11}),\\
L_2&=(6,3^{\times4},1^{\times6},0^{\times5}),\\
L_1&=(4,3^{\times4},2^{\times6},1^{\times4},0).
\end{aligned}
\]

They are simultaneously decreasing in Hamming-weight order. Their weighted sum is exactly

\[
D_t=\operatorname{diag}(a,b)^{\otimes4},
\]

with ordered values \(a^{4-w}b^w\) and multiplicities \(1,4,6,4,1\). Thus, with \(R_j(k)=K_k(L_j)\),

\[
K_k(D_t)
=t^4+t^3bR_3(k)+t^2b^2R_2(k)+tb^3R_1(k)+kb^4.
\]

This confirms that the consuming reference is the actual product-reference prefix, not a looser sum of unrelated bounds.

## 6. Complete compatible-layer diagonalization

Let \(\mathcal E_w\) be the physical weight-\(w\) subspace. Let \(A_w\) connect two strings when one occupied position is exchanged with one unoccupied position.

### 6.1 Adjacency spectra

For \(w=1,3\),

\[
A_w=J_4-I_4,
\]

so its spectrum is \(3,(-1)^{\times3}\).

For \(w=2\), let \(M\) exchange each two-element subset with its complement. There are three disjoint complement pairs. Thus \(M\) has \(+1\) and \(-1\) eigenspaces of dimension three each. Since the only nonadjacent distinct weight-two strings are complements,

\[
A_2=J_6-I_6-M.
\]

The constant vector has eigenvalue \(4\). The remaining two-dimensional \(M=+1\) space has eigenvalue \(-2\), while the three-dimensional \(M=-1\) space has eigenvalue \(0\). This yields

\[
\operatorname{spec}(A_2)=
\bigl(4,0^{\times3},(-2)^{\times2}\bigr)
\]

without importing an external graph-spectrum theorem.

### 6.2 Two-body layer

The pair reduction gives

\[
H_2|_{\mathcal E_w}
=d_wI+\frac13A_w,
\]

where

\[
d_w=
\frac{\binom w2+\binom{4-w}2}{6}
+\frac{w(4-w)}3.
\]

For \(w=0,1,2,3,4\), these values are

\[
1,\quad\frac32,\quad\frac53,\quad\frac32,\quad1.
\]

### 6.3 Three-body layer

Each nonzero entry of either excitation block in a triple marginal is \(1/6\). Adjacent global strings agree at two possible omitted positions, producing total off-diagonal entry \(1/3\). Complementary weight-two strings agree at no position and produce no such entry.

The diagonal counts give

\[
H_3|_{\mathcal E_w}
=e_wI+\frac13A_w,
\qquad
(e_0,e_1,e_2,e_3,e_4)
=\left(0,\frac12,\frac23,\frac12,0\right).
\]

In particular \(d_w=e_w+1\), verifying \(H_2=I+H_3\) directly on every physical block.

### 6.4 Simultaneous ordered spectrum

Combining these blocks gives precisely the author’s common subspaces:

| Actual subspace | Multiplicity | \(\rho_D\) | \(H_3\) | \(H_2\) | \(H_1\) |
|---|---:|---:|---:|---:|---:|
| Constant vector in \(\mathcal E_2\), namely \(D\) | 1 | 1 | 2 | 3 | 2 |
| Constant vectors in \(\mathcal E_1,\mathcal E_3\) | 2 | 0 | \(3/2\) | \(5/2\) | 2 |
| \(A_2=0\) subspace | 3 | 0 | \(2/3\) | \(5/3\) | 2 |
| Sum-zero spaces in \(\mathcal E_1,\mathcal E_3\) | 6 | 0 | \(1/6\) | \(7/6\) | 2 |
| \(\mathcal E_0,\mathcal E_4\), and \(A_2=-2\) subspace | 4 | 0 | 0 | 1 | 2 |

The multiplicities sum to sixteen. The traces are

\[
\operatorname{Tr}H_2=3+5+5+7+4=24,
\qquad
\operatorname{Tr}H_3=2+3+2+1=8.
\]

Each column is decreasing in this same row order. These are compatible operators derived from one physical density, not separately optimized marginal spectra.

## 7. All sixteen prefix gaps

Let \(S(k)=K_k(H_3)\). The reconstructed spectrum gives

\[
S(k)=
\begin{cases}
(3k+1)/2,&1\le k\le3,\\
2k/3+3,&3\le k\le6,\\
k/6+6,&6\le k\le12,\\
8,&12\le k\le16.
\end{cases}
\]

The formulas agree at every shared endpoint. Since \(H_2=I+H_3\),

\[
K_k(H_2)=k+S(k),\qquad K_k(H_1)=2k.
\]

The reference cumulative sums are

\[
R_3(k)=
\begin{cases}
k+3,&1\le k\le5,\\
8,&5\le k\le16,
\end{cases}
\]

\[
R_2(k)=
\begin{cases}
3k+3,&1\le k\le5,\\
k+13,&5\le k\le11,\\
24,&11\le k\le16,
\end{cases}
\]

and

\[
R_1(k)=
\begin{cases}
3k+1,&1\le k\le5,\\
2k+6,&5\le k\le11,\\
k+17,&11\le k\le15,\\
32,&15\le k\le16.
\end{cases}
\]

Subtracting these exact cumulative formulas reconstructs **every row** of S1’s table:

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

Here \(\Delta_j(k)=R_j(k)-K_k(H_j)\). All entries are nonnegative, with \(\Delta_2(k)>0\) for every proper prefix.

## 8. Common-projector bound and exact output ordering

For any one fixed complex orthogonal rank-\(k\) projector \(Q\),

\[
\begin{aligned}
\operatorname{Tr}\!\left[QT_t^{\otimes4}(\rho_D)\right]
={}&t^4\operatorname{Tr}(Q\rho_D)
+t^3b\operatorname{Tr}(QH_3)\\
&+t^2b^2\operatorname{Tr}(QH_2)
+2ktb^3+kb^4.
\end{aligned}
\]

Applying each Ky Fan inequality to this **same** \(Q\), together with \(\operatorname{Tr}(Q\rho_D)\le1\), yields

\[
\operatorname{Tr}\!\left[QT_t^{\otimes4}(\rho_D)\right]\le K_k(D_t).
\]

No simultaneous attainment of separate layer maxima is required for that inequality.

The stronger exact-prefix identity is also justified: the actual layers have the simultaneous decreasing basis reconstructed above. Their five output eigenvalues, with multiplicities \(1,2,3,6,4\), are

\[
\begin{aligned}
\mu_1&=t^4+2t^3b+3t^2b^2+2tb^3+b^4,\\
\mu_2&=\frac32t^3b+\frac52t^2b^2+2tb^3+b^4,\\
\mu_3&=\frac23t^3b+\frac53t^2b^2+2tb^3+b^4,\\
\mu_4&=\frac16t^3b+\frac76t^2b^2+2tb^3+b^4,\\
\mu_5&=t^2b^2+2tb^3+b^4=a^2b^2.
\end{aligned}
\]

Their successive differences are

\[
t^4+\frac{t^3b+t^2b^2}{2},\quad
\frac56(t^3b+t^2b^2),\quad
\frac12(t^3b+t^2b^2),\quad
\frac16(t^3b+t^2b^2),
\]

all nonnegative. Hence there is no omitted crossing regime, and

\[
K_k(D_t)-K_k(T_t^{\otimes4}(\rho_D))
=t^3b\Delta_3(k)+t^2b^2\Delta_2(k)+tb^3\Delta_1(k).
\]

This verifies S1’s exact identity (18). For \(0<t<1\), its right-hand side is strictly positive for every proper prefix because \(t^2b^2>0\) and \(\Delta_2(k)>0\).

At \(t=0\), both outputs are \(I_{16}/16\). At \(t=1\), both have pure spectra. No division by a vanishing coefficient or eigenvalue gap is used.

## 9. Consuming-side transport: negative branch, local bases and mixtures

The one-qubit identity

\[
\mathcal J(X)=YX^TY=\operatorname{Tr}(X)I_2-X
\]

implies \(T_{-t}=\mathcal J\circ T_t\). Tensoring all four physical legs therefore gives

\[
T_{-t}^{\otimes4}(\rho)
=W_4[T_t^{\otimes4}(\rho)]^TW_4,
\qquad W_4=Y^{\otimes4}.
\]

This is **full transpose**, not partial transpose. Since \(W_4^T=W_4\), the consuming functional is

\[
\operatorname{Tr}\!\left[QT_{-t}^{\otimes4}(\rho)\right]
=\operatorname{Tr}\!\left[Q'T_t^{\otimes4}(\rho)\right],
\qquad Q'=W_4Q^TW_4.
\]

Transpose preserves the Hermitian-projector identity and rank, and unitary conjugation preserves both. Thus \(Q'\) is an allowed complex orthogonal rank-\(k\) projector. The already-proved positive-branch bound explicitly receives this transported projector; it is not silently replaced by the original \(Q\).

For the physical negative branch, \(p=1+t\) with \(0\le t\le1/3\). The positive-branch proof holds on the larger interval \(0\le t\le1\), so the complete physical interval \(0\le p\le4/3\) is covered.

For a physical local product unitary \(V\), depolarizing covariance gives

\[
\Phi_p^{\otimes4}(V\rho_DV^\dagger)
=V\Phi_p^{\otimes4}(\rho_D)V^\dagger.
\]

The bound is consumed with \(V^\dagger QV\), again preserving rank and orthogonality. For a finite mixture, linearity applies to the original fixed \(Q\) and each component has the same reference \(K_k(D_t)\). This establishes the stated orbit and finite-convex-hull theorem without independent marginal choices or an input-independent postprocessing assertion.

## 10. Genuine entanglement and strict earlier-hull separation

The reconstructed \(1|3\) decomposition has two nonzero Schmidt coefficients \(1/\sqrt2,1/\sqrt2\). The reconstructed \(2|2\) decomposition has three nonzero Schmidt coefficients

\[
\frac1{\sqrt6},\quad \sqrt{\frac23},\quad\frac1{\sqrt6}.
\]

Permutation symmetry covers all four singleton cuts and all three paired cuts. Thus \(D\) is entangled across every bipartition, with paired-cut Schmidt rank three.

The separation interfaces are exact:

- **Class A:** a sum of at most two physical product-basis vectors has Schmidt rank at most two across every paired cut.
- **Class B:** its defining repetition support has dimension two on either side of at least one paired cut. Every pure vector in that support has Schmidt rank at most two across that cut. Physical local unitaries and permutations preserve the relevant rank statement.
- **Symmetric-W4 orbit:** across a paired cut, \(W_4\) is a sum of two orthogonal product terms,
  \[
  \frac1{\sqrt2}\left(|\psi^+\rangle|00\rangle+
  |00\rangle|\psi^+\rangle\right),
  \]
  and therefore has Schmidt rank two. Local product unitaries preserve it.
- **Biseparable pure states:** these have Schmidt rank one across at least one bipartition, unlike \(D\).

For convex-hull exclusion, suppose a finite positive mixture equals \(\rho_D\). Every vector orthogonal to \(D\) has zero expectation in that mixture, so each positive-weight positive component has zero expectation on the entire orthogonal complement. Positivity forces each component’s support into the single ray \(\mathbb C D\); after normalization, each component is \(\rho_D\).

Therefore mixing Class A, mixed Class B, W4-orbit or biseparable components cannot produce \(\rho_D\). In particular,

\[
\rho_D\notin
\operatorname{conv}\!\left(
C_{A/B}\cup C_{W4}\cup \mathrm{Bisep}
\right).
\]

This proves strict addition relative to the named frozen classes. It is not an exhaustive comparison with every earlier regional sector and supplies no novelty conclusion.

## 11. Invariant-sector statement and remaining obligations

The broader invariant-sector calculation in S1 is consistent with the Dicke proof.

Tensor expansion of \(\mathcal J\) gives

\[
\widetilde\rho=I-H_1+H_2-H_3+\rho.
\]

If \(\widetilde\rho=\rho\), each one-body marginal is spin-flip invariant and equals \(I_2/2\). Consequently \(H_1=2I\) and

\[
H_2=I+H_3.
\]

Each invariant three-body marginal commutes with its spin-flip antiunitary, whose square is \(-I\). Its eigenvalues therefore occur in orthogonal pairs; trace one implies its largest eigenvalue is at most \(1/2\). Thus

\[
0\le H_3\le2I,\qquad \operatorname{Tr}H_3=8.
\]

For a fixed rank-\(k\) projector,

\[
h_3\le\min(2k,8),\qquad
\operatorname{Tr}(QH_2)=k+h_3.
\]

Substitution into the displayed reference cumulative sums confirms S1’s \(A_k,B_k,C_k\) table. Only \(A_4\) is negative; every \(B_k,C_k\) is nonnegative. The fourth-prefix deficit is exactly

\[
-t^3b+3t^2b^2+5tb^3
=\frac{tb}{4}(5-4t-5t^2),
\]

which is nonnegative for

\[
0\le t\le t_*=\frac{\sqrt{29}-2}{5},
\]

and vanishes at \(t=1\). The asserted physical interval

\[
p\in\left[\frac{7-\sqrt{29}}5,\frac43\right]\cup\{0\}
\]

follows with the already-checked negative-branch transport.

For \(t_*<t<1\), this relaxation does not prove the invariant sector’s fourth prefix. It is not a physical counterexample. The exact Dicke calculation closes that residual on the stated orbit and its finite convex hull, not on every invariant density.

Outside the invariant sector, neither \(H_1=2I\) nor \(H_2=I+H_3\) has been proved or assumed. S1 correctly retains the unrestricted two-body obligations

\[
K_k(H_2(\rho))\le
\begin{cases}
3k+3,&2\le k\le5,\\
k+13,&6\le k\le10,
\end{cases}
\]

and the separate three-body obligations \(K_2\le5\), \(K_3\le6\), \(K_4\le7\). No unrestricted four-qubit channel conclusion follows from the reviewed state class.

## 12. Prior-source and assurance qualification

The frozen packet credits Song–Chen’s Proposition 3 as direct prior for the compatible weighted **three-qubit** marginal result. F511 S4 supports that attribution at the supplied documentary scope. I did not inspect the public paper in this duty and do not claim an independent bibliographic, authenticity, proof-validity or novelty audit.

The Dicke marginal and spectral proof above does not require that three-qubit result. Nor does it rely on the earlier author’s unreviewed three-qubit proof or on reported finite verification.

**Final disposition:** the assigned Dicke all-physical-parameter, all-sixteen-prefix orbit theorem, its finite-mixture extension and strict named-hull separation are **SUPPORTED by this same-harness written reconstruction**, with **0 FATAL / 0 MAJOR / 0 MINOR** findings. Parent adoption remains a separate decision; unrestricted original-target closure remains **NOT PROVED**.