# f428 — Complete WRITTEN review

**Overall correctness: correct at the frozen Theorem A/Theorem B scope.**  
**Confidence: 0.97.**  
**Findings:** No actionable mathematical correctness defect found in the parity-sector proof or its four-qubit spectator/finite-hull extension. No FATAL or MAJOR mathematical finding is raised.

The coupled estimates support all eight three-qubit prefixes for arbitrary complex parity-preserving densities, and the tensor/convexity argument supports all sixteen prefixes on the stated four-qubit sector. This is a same-harness written review, not parent adoption, independent-family review, human review, kernel certification, executable verification, unrestricted-target closure, or novelty determination.

## 1. Reviewed material and process boundary

I read the manifest, freeze receipt, parent live metadata supply, and all seven prescribed status-only controls before sending the direct administrative pre-body ACK to Main. I then read the complete literal packet sequentially in raw windows of at most 20 LF, through its ending: packet lines 1–713, containing S1 source lines 1–711. No packet range was skipped or elided.

The assigned identities are:

- Manifest: `10abd595dce2a2fe633078eae1287e065cb4b62a517088e18d6fab3dda19e6f3`.
- Freeze receipt: `7d08a7bb40d094c9c24a9618c6dd8654bb77aac2d7df213f6b99cfec0dda97ec`.
- Literal packet: `1aa9ee1517f0de00b6ae85583790e695a8a64947b4141ecadf1497e9a332b31c`.
- Candidate S1: `335838f36bc59bafd01f829369f0d996ebb169145c05a8f7b8a43b884280e1ff`, at `review-waves/f397-depolarizing-unrestricted-or-three-qubit-bridge-frontier/review-v1.md`.

The clock `2026-10-30T11:02:48-0700 PDT` and the live SHA/byte/LF matches are **parent-supplied observations**, not my native measurements or start/completion times.

All genuinely held payloads and their method, selection, planning, confidence, correctness, and reporting consumers remained NONINPUT. I did not follow excluded links or consult prior reviewer bodies, sibling work, author code, or external sources. No selected diagnostic was introduced. The arithmetic below reconstructs the universal argument and the example explicitly assigned for review; no scientific executable, CAS, interpreter, solver, enumeration, replay, test, build, formatter, network request, model CLI, paid campaign, or remote computation was used.

No repository file was written. This message is the complete review body for parent materialization; it does not claim materialization or adoption.

## 2. Claim dispositions

| Claim | Disposition | Source LF |
|---|---|---|
| Actual complex parity-sector output matrices, including the conjugated complementary block | **SUPPORTED** | 144–215 |
| \(A\ge0\), \(\operatorname{Tr}A=1\); \(B\le I\); at most one negative eigenvalue of \(B\) | **SUPPORTED** | 232–260 |
| Uniform bound \(\gamma\le\max\{0,(3t-1)/4\}\), including zero populations | **SUPPORTED** | 262–297 |
| Concentration bounds and \(\delta\le\varepsilon,\ 2\delta\le abt\) | **SUPPORTED** | 299–338 |
| Both ordered four-dimensional block majorants, with every prefix | **SUPPORTED** | 340–378 |
| Ordered direct-sum majorant and all eight reference-prefix inequalities | **SUPPORTED** | 380–406 |
| Arbitrary complex consuming projectors | **SUPPORTED** | 99–140, 380–404 |
| Odd parity, mixed parity-preserving densities, and physical local bases | **SUPPORTED** | 410–422 |
| Full physical parameter range and full-transpose projector transport, including odd \(n\) | **SUPPORTED** | 424–464 |
| Actual four-qubit spectator products and arbitrary finite mixtures, all sixteen prefixes | **SUPPORTED** | 468–508 |
| Separation of the displayed \(W\)-spectator state from the explicitly described Class A/Class B families | **SUPPORTED** | 512–563 |
| Identification and previously adopted majorization theorem of the historical Class A/Class B hull | **INCONCLUSIVE as an external import in this packet** | 565–571 |
| Displayed physical spectra, complex projectors, and localization of the blockwise counterexample | **SUPPORTED** | 575–654 |
| External literature attribution, priority, and resolution of older stronger printed claims | **INCONCLUSIVE / not audited here** | 658–691 |

The conditional import qualification in the historical-hull row does not affect Theorem A or Theorem B: neither proof uses that import.

## 3. Reconstruction of the physical output

Let \(r_i=|c_i|^2\), \(R=cc^\dagger\), \(D=\operatorname{diag}(r_i)\), and use the author’s paired bases
\[
e=(000,011,101,110),\qquad \bar e_i=e_i\oplus111.
\]
For
\[
T_t(X)=tX+b\operatorname{Tr}(X)I,\qquad
a=\frac{1+t}{2},\quad b=\frac{1-t}{2},
\]
a diagonal one-qubit matrix unit is retained with weight \(a\) and flipped with weight \(b\); an off-diagonal matrix unit is multiplied by \(t\).

Every distinct pair \(e_i,e_j\) differs on exactly two positions.

In the input-parity output block:

- Its \(i\)-th diagonal entry is
  \[
  a^3r_i+ab^2(1-r_i)=c_0+at\,r_i,
  \]
  because \(a^3-ab^2=at\).
- Its \(ij\)-th off-diagonal entry is
  \[
  at^2c_i\overline{c_j}.
  \]

Therefore
\[
M_E=c_0I+at\bigl((1-t)D+tR\bigr)=c_0I+atA.
\]

In the complementary-parity block:

- Its \(i\)-th diagonal entry is
  \[
  b^3r_i+a^2b(1-r_i)=d-bt\,r_i.
  \]
- Complementing the output pair reverses the differing-bit orientation of the relevant input matrix unit. Its \(ij\)-th off-diagonal entry is consequently
  \[
  bt^2\overline{c_i}c_j.
  \]

Thus
\[
M_O=dI-bt\,\overline{B},\qquad B=(1+t)D-tR.
\]

This verifies the entrywise conjugation in S1 LF 184–188; replacing it by an unqualified real-coefficient formula would not be justified. No such replacement is needed here.

Both \(A\) and \(B\) are Hermitian and have trace one. The block traces are
\[
\operatorname{Tr}M_E=4c_0+at=u+3c_0,\qquad
\operatorname{Tr}M_O=4d-bt=3d+\ell.
\]

The labels above initially refer to an even input. For an odd input, the same calculation applies with the input-parity and complementary-parity sectors interchanged, or follows by the stated local covariance.

## 4. Reconstruction of the coupled estimates

### 4.1 Positivity, negative inertia, and \(B\le I\)

Since \(0\le t\le1\),
\[
A=(1-t)D+tR\ge0,\qquad \operatorname{Tr}A=1.
\]

For \(v\perp c\),
\[
v^\dagger Bv=(1+t)v^\dagger Dv\ge0.
\]
A two-dimensional negative spectral subspace would intersect \(c^\perp\) nontrivially, contradicting this inequality. Hence \(B\) has at most one negative eigenvalue.

The complex Gram identity is correct:
\[
I-2D+R=
\sum_{i<j}
(\overline{c_j}e_i+\overline{c_i}e_j)
(\overline{c_j}e_i+\overline{c_i}e_j)^\dagger.
\]
Its \(i\)-th diagonal entry is \(1-r_i\), and its \(ij\)-th off-diagonal entry is \(c_i\overline{c_j}\), exactly as on the left. It proves \(2D-R\le I\). Since
\[
B=(1-t)D+t(2D-R),\qquad D\le I,
\]
we obtain \(B\le I\).

These arguments allow arbitrary phases and zero coefficients.

### 4.2 Uniform negative-eigenvalue bound

Cauchy–Schwarz gives \(R\le4D\), without dividing by any population. Thus, for \(t\le1/3\),
\[
B\ge(1-3t)D\ge0,
\]
so \(\gamma=0\).

For \(t>1/3\), put \(g=(3t-1)/4>0\). The function
\[
f(r)=\frac{r}{g+(1+t)r}
\]
is concave on \(r\ge0\). Therefore
\[
\sum_i\frac{r_i}{g+(1+t)r_i}
\le 4f(1/4)=\frac1t.
\]
For every vector \(z\), weighted Cauchy–Schwarz then gives
\[
t|c^\dagger z|^2
\le
\sum_i\bigl(g+(1+t)r_i\bigr)|z_i|^2.
\]
Consequently \(tR\le gI+(1+t)D\), or \(B\ge-gI\).

All denominators in this branch are positive even when some \(r_i=0\). The boundary \(t=1/3\) is covered by the first branch. Hence
\[
\gamma\le\max\left\{0,\frac{3t-1}{4}\right\}
\le\frac{1+t}{4}=\frac a2,
\]
and therefore
\[
2\delta=2bt\gamma\le abt.
\]

The displayed \(1/t\) occurs only inside the \(t>1/3\) branch. Endpoint validity does not depend on interpreting that expression at zero.

### 4.3 Deficit pays for excess

Let \(m=\max_i r_i\). Since \(R\le I\) and \(D\le mI\),
\[
\alpha\le t+(1-t)m,
\qquad
1-\alpha\ge(1-t)(1-m).
\]

Choose a maximizing index \(j\) and write \(c=c_je_j+q\). The inequality
\[
(c_je_j+q)(c_je_j+q)^\dagger
\le2m e_je_j^\dagger+2qq^\dagger
\]
implies
\[
R-2D\le2qq^\dagger\le2(1-m)I.
\]
Thus
\[
-B=-(1-t)D+t(R-2D)\le2t(1-m)I,
\qquad \gamma\le2t(1-m).
\]

Using \(t\le a\) and \(1-t=2b\),
\[
\delta\le2bt^2(1-m)
\le2abt(1-m)
\le at(1-\alpha)=\varepsilon.
\]

This is uniform in every normalized complex coefficient vector. No positivity assumption on individual populations, selected input restriction, or eigenvalue-gap assumption enters.

## 5. Every block prefix and the full eight-prefix comparison

### 5.1 Input-parity block

The eigenvalues of \(M_E\) are at least \(c_0\). Its largest eigenvalue satisfies
\[
\lambda_{\max}(M_E)
=c_0+at\alpha
=u-\varepsilon
\le u-\delta.
\]
Its trace is \(u+3c_0\). Hence the four Ky Fan bounds are
\[
K_1(M_E)\le u-\delta,\quad
K_2(M_E)\le u+c_0,\quad
K_3(M_E)\le u+2c_0,\quad
K_4(M_E)=u+3c_0.
\]
These are precisely the prefixes of
\[
(u-\delta,c_0+\delta,c_0,c_0).
\]

### 5.2 Complementary block

Because entrywise conjugation preserves the spectrum of Hermitian \(B\), the established spectral properties apply to \(M_O\).

The bound \(B\le I\) gives
\[
\lambda_{\min}(M_O)\ge d-bt=\ell.
\]
At most one eigenvalue of \(M_O\) can exceed \(d\), and its largest eigenvalue is at most \(d+\delta\). Therefore
\[
K_1(M_O)\le d+\delta,\quad
K_2(M_O)\le2d+\delta,\quad
K_3(M_O)\le3d,\quad
K_4(M_O)=3d+\ell.
\]
These are the prefixes of
\[
(d+\delta,d,d-\delta,\ell).
\]

### 5.3 Ordering

The needed ordering follows from \(2\delta\le abt\) and
\[
u-d=a^2t,\quad d-c_0=abt,\quad
u-c_0=at,\quad d-\ell=bt.
\]
In particular,
\[
u-\delta\ge d+\delta,\qquad
d-\delta\ge c_0+\delta,
\]
and the internal orders of both block majorants also hold. The full ordered majorant is therefore
\[
v=(u-\delta,d+\delta,d,d-\delta,c_0+\delta,c_0,c_0,\ell).
\]

The direct-sum Ky Fan allocation formula applies to every \(k=0,\ldots,8\); it does not require the consuming projector to be block diagonal. Comparing \(v\) with
\[
r=(u,d,d,d,c_0,c_0,c_0,\ell)
\]
gives the eight cumulative differences
\[
(\delta,0,0,\delta,0,0,0,0).
\]
Every difference is nonnegative, and the total traces agree. This establishes all eight prefixes simultaneously.

For any complex orthogonal rank-\(k\) projector \(Q\), the eigenbasis diagonal entries satisfy \(0\le q_i\le1\) and \(\sum_iq_i=k\), proving
\[
\operatorname{Tr}(QX)\le K_k(X).
\]
Thus no real-projector restriction or separate optimization of layerwise projectors has entered.

### 5.4 Endpoints and ties

At \(t=0\), both output blocks are \(I_4/8\), and \(\delta=0\). At \(t=1\), the input-parity block is \(R\), the complementary block is zero, and again \(\delta=0\). Both agree with their reference spectra.

All inequalities are closed inequalities on \(0\le t\le1\). Zero populations, rank drops, and repeated eigenvalues require neither limiting diagonalizers nor division by vanishing quantities.

## 6. Mixed states, physical bases, and the negative branch

The local unitary \(X^{\otimes3}\) exchanges the two parity sectors, and \(T_t\) is locally unitary covariant. The pure-state result therefore covers odd parity.

If \([\rho,Z^{\otimes3}]=0\), its two positive parity blocks admit finite spectral decompositions into pure parity eigenstates. Ky Fan convexity applies to their outputs with the **same** reference \(D_{3,t}\). This proves the mixed-state assertion, including arbitrary complex coherences inside each block.

Each traceless Hermitian one-qubit unitary is a local-unitary conjugate of \(Z\). Covariance therefore supplies exactly the physical local-basis formulation stated in Theorem A. It does not imply a theorem for arbitrary cross-parity coherences.

For the physical negative Bloch parameter, write \(s=1-p=-t\). The identity
\[
\mathcal J(X)=YX^TY=\operatorname{Tr}(X)I-X
\]
gives \(T_{-t}=\mathcal J\circ T_t\), so
\[
T_{-t}^{\otimes n}(\rho)
=W_n[T_t^{\otimes n}(\rho)]^TW_n,
\qquad W_n=Y^{\otimes n}.
\]
This uses the **full transpose** and preserves the spectrum.

The projector transport is also correct for odd \(n\). Indeed,
\[
\operatorname{Tr}(QW_nX^TW_n)
=\operatorname{Tr}\bigl((W_nQW_n)^TX\bigr).
\]
Although \(W_n^T=(-1)^nW_n\), its two appearances cancel the sign:
\[
(W_nQW_n)^T=W_nQ^TW_n.
\]
Thus \(Q'=W_nQ^TW_n\) is an orthogonal rank-\(k\) projector with the claimed expectation. No odd-\(n\) sign remains.

The negative physical branch requires only \(0\le t\le1/3\). The product-reference outputs with one-qubit eigenvalues \((b,a)\) have the same tensor-power spectra as \(D_{n,t}\).

**Theorem A is therefore supported for every stated density, projector, prefix, and physical parameter.**

## 7. Actual four-qubit spectator and finite-hull extension

For positive matrices \(X\prec X_0\), \(Y\prec Y_0\), diagonalizing \(X\) with nonnegative eigenvalues \(x_i\) gives
\[
K_k(X\otimes Y)
=\max_{\sum_i k_i=k}\sum_i x_iK_{k_i}(Y)
\le K_k(X\otimes Y_0).
\]
Diagonalizing \(Y_0\), whose eigenvalues are likewise nonnegative, and applying \(X\prec X_0\) yields
\[
K_k(X\otimes Y_0)\le K_k(X_0\otimes Y_0).
\]
Trace equality completes tensor preservation. Zero eigenvalues do not obstruct either allocation argument.

An arbitrary one-qubit density with Bloch length \(r_\sigma\le1\) has output eigenvalues
\[
\frac{1+tr_\sigma}{2},\qquad \frac{1-tr_\sigma}{2},
\]
up to ordering, so its output is majorized by \(\operatorname{diag}(a,b)\). Combining this with Theorem A proves
\[
\Phi_p(\sigma)\otimes\Phi_p^{\otimes3}(\tau)\prec D_{4,t}.
\]

Changing the physical spectator only permutes physical tensor factors. Changing the local bases only applies covariance. Finally, every finite mixture uses the same reference spectrum, so Ky Fan convexity proves all sixteen prefixes even when spectator, bases, and factors vary between components.

For every complex rank-three projector this includes
\[
\operatorname{Tr}\!\left[Q\Phi_p^{\otimes4}(\rho)\right]
\le a^4+2a^3b.
\]

**Theorem B is supported on exactly the stated finite convex hull.** It does not extend to general \(1|3\)-separable inputs unless their three-qubit factors meet Theorem A’s condition.

## 8. Strictness and its exact import boundary

For the displayed complex \(W\) factor, the two-qubit Schmidt support in S1 LF 528–536 consists of coefficient matrices
\[
\begin{pmatrix}u&v\\iv&0\end{pmatrix}.
\]
Their determinant is \(-iv^2\), so this support has only one product-vector direction. A tensor-rank-two decomposition with Schmidt rank two across that cut would supply two independent product vectors spanning the support. Hence the \(W\) factor has tensor rank three.

Contracting the pure spectator with its bra recovers that factor, so adjoining the spectator cannot make the state a sum of two physical product vectors. This excludes every Class A vector satisfying the stated rank-two structural condition, in any local bases.

For any pairing, the pair containing the spectator has reduced range
\[
|0\rangle\otimes\mathbb C^2.
\]
A Class B code of the displayed form has identity reduced projector on either retained qubit. In contrast, tracing the projector onto the displayed range over the nonspectator gives \(2|0\rangle\langle0|\). Both spaces have dimension two, so containment would require equality, which is impossible. This excludes the stated Class B codes for every pairing and physical local basis.

A pure density in a finite convex combination of positive densities forces every positive-weight component to have the same one-dimensional support. Thus the displayed state is outside the convex hull of those explicitly characterized families.

What this packet does **not** independently supply is the prior source establishing that these are exactly the historically adopted Classes A/B and that their entire old hull has the previously accepted majorization theorem. Consequently:

- The separation proof relative to the explicit structures is **SUPPORTED**.
- The historical identification and old-hull theorem remain **exact-scope imports**, not newly verified here.
- Theorem B and its nonempty four-qubit sector do not depend on either historical import.
- If the historical imports hold at precisely those scopes, adjoining the new sector gives the claimed strict extension.

This qualification is not a counterexample to the separation argument.

## 9. Assigned physical example and localization of the failed premise

I reconstructed the **displayed** example at \(t=3/4\), \(a=7/8\), \(b=1/8\); no additional test input was selected.

In the odd input basis, the coefficient vector is \((0,1,i,1)/\sqrt3\). On its three-dimensional support, \(D=I/3\) and \(R\) is a rank-one projector. Therefore \(A\) has eigenvalues
\[
5/6,\ 1/12,\ 1/12,\ 0,
\]
and \(B\) has eigenvalues
\[
-1/6,\ 7/12,\ 7/12,\ 0.
\]
The input-parity output block has spectrum
\[
(287,35,35,7)/512,
\]
while its complementary, even-parity block has spectrum
\[
(57,49,21,21)/512.
\]
Their ordered union is exactly
\[
(287,57,49,35,35,21,21,7)/512.
\]

The reference spectrum and all eight cumulative differences in S1 LF 595–600 are correct:
\[
r=(343,49,49,49,7,7,7,1)/512,
\]
\[
\text{reference minus actual prefixes}
=(56,48,48,62,34,20,6,0)/512.
\]

The vectors \(\psi_W,\eta,000\) are orthonormal. They select output eigenvalues \(287/512,57/512,49/512\), respectively, so
\[
\operatorname{Tr}(Q_3X)=393/512<441/512.
\]
For the pure spectator, its \(|0\rangle\) output weight is \(7/8\). Hence the stated \(Q_4\) expectation and reference bound are
\[
2751/4096<3087/4096,
\]
with slack \(21/256\), as printed.

Finally, the two corresponding even output blocks have equal trace but spectra
\[
(57,49,21,21)/512,\qquad (49,49,49,1)/512.
\]
The complex vector \(\eta\) attains \(57/512>49/512\). This genuinely refutes the auxiliary assertion of **separate parity-block majorization by corresponding product-reference blocks**. It does **not** refute full output majorization; the complete prefix list proves the opposite for this example.

## 10. Imports, paid obligations, unpaid obligations, and verdict

### Paid by this written review

- Actual complex physical output entries and complementary-block conjugation.
- Gram identity, negative inertia, uniform and concentration-dependent bounds.
- Both four-dimensional majorants, their ordering, and every block prefix.
- Direct-sum consumption by arbitrary complex projectors and every three-qubit prefix.
- All zero-population, endpoint, and tie cases.
- Mixed parity states, physical local bases, full-transpose negative-branch transport.
- Actual four-qubit spectator products and arbitrary stated finite mixtures.
- The displayed physical example and the exact scope of its failed blockwise premise.
- Structural separation from the explicitly described Class A/Class B families.

### Unpaid or outside scope

- Cross-parity coherences \(C=\Pi_+\rho\Pi_-\ne0\).
- Arbitrary complex three-qubit densities.
- General \(1|3\)-separable four-qubit inputs.
- Arbitrary genuinely four-qubit inputs, unrestricted \(k=3\), or unrestricted all-prefix majorization.
- Independent verification of the historical old-hull import.
- Literature/source-access adjudication, including older formally stronger printed claims and unresolved proof-validity questions.
- Novelty or priority.
- A separately commissioned executable physical-channel check.
- Independent-family, human, kernel, and parent-acceptance gates.

**Final disposition:** The frozen parity-sector theorem and the stated four-qubit spectator/finite-hull theorem are **SUPPORTED by complete written reconstruction**. No mathematical bug was found in their load-bearing chain. Their acceptance, any incorporation into the historical hull, and any subsequent research authorization remain parent decisions; no such adoption is claimed here.