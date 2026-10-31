# F507 written review — coherent vacuum–\(W_4\) actual \(H_3\) layer

**Role:** WRITTEN  
**Disposition:** SUPPORTED within the frozen \(H_3\) and second-moment scope.  
**Mathematical findings:** **0 FATAL / 0 MAJOR / 0 MINOR.**  
**Original unrestricted four-qubit target:** NOT PROVED.

This is the complete proposed `review-v1.md` body for parent materialization. No repository file was written.

## 1. Binding, coverage, and process

The reviewed wave is:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f507-coherent-vacuum-w4-actual-h3-layer-written-review/`

The supplied bindings are:

- Manifest SHA256: `6d86d95b51c0d52a241e837f55d7de29c8ab5a854a6aa386db95a2318074a50e`
- Freeze-receipt SHA256: `98296aa5c0743dd3bb0b77b75e21a478e4eabec58b5a74485d3f92ed5c3d2007`
- Packet SHA256, as recorded in the receipt and parent metadata: `94c5697f378d9872a120e98c2302685b73aa82a3c6860cf2e17f656ee6382997`

These are **parent-attributed metadata**, not independently executed child hash observations.

Before any mathematical packet read, I completely read:

- The manifest and freeze receipt.
- The dispatch receipt and parent live-metadata supply.
- All eleven manifest-listed permission, quarantine, and transport controls, through their endings.

I then sent an administrative pre-body ACK to `agent://Main`. The tool returned **“Delivered to Main.”** This is observed direct delivery of this reviewer’s ACK, not merely a transcript-only or local-file acknowledgment.

Afterward, I read the entire literal packet in consecutive, ordered, raw windows of at most twenty lines, through packet line **771**:

- **S1:** F480 author candidate, logical lines **1–730**, including its ending.
- **S2:** Earlier three-qubit/biseparable disposition, lines **1–39**, including its ending.

Only after completing those reads did I reconstruct the mathematics below.

### Execution and exposure

- Scientific code, CAS, numerical experiments, selected-instance checks, solvers, builds, tests, linters, and formatters: **NOT RUN**.
- No new chosen parameter instance was used, privately or publicly.
- No sibling return, additional scientific source, author code, excluded link, or held mathematical payload was opened.
- Quarantine controls were used only for status and exclusions.
- One permitted, read-only `git diff` restricted to this wave’s manifest, receipt, and packet returned no output. This is neither mathematical verification nor source-hash verification.
- No child-native clock or hash execution is claimed.

The pre-existing F480 transport qualification remains unchanged: its author ACK was transcript-recorded, with no observed direct delivery. That historical noncompliance is **not** automatically a mathematical invalidation under owner addendum 2. This review does not backdate or repair that transport history.

## 2. Scope and claim dispositions

| Claim | Review disposition |
|---|---|
| Actual compatible three-body marginals of the coherent vacuum–\(W_4\) family | **SUPPORTED** |
| Explicit \(A_3\), three \(B_2\) blocks, and seven zeros | **SUPPORTED** |
| \(H_3(\lvert\psi_q\rangle\langle\psi_q\rvert)\prec L_3\) for every \(q\in[0,1]\) | **SUPPORTED** |
| Corresponding \(H_3\) bounds under physical local unitaries and finite convex mixtures | **SUPPORTED** |
| Unrestricted-density second-moment sufficient condition | **SUPPORTED** |
| Pure-state identity \(\operatorname{Tr}H_3^2=8+3S_1+2\eta\) | **SUPPORTED** |
| Universal \(H_3\) majorization without the family or sufficient-condition restrictions | **INCONCLUSIVE / NOT PROVED**, as the author states |
| Separate \(H_2\) proof, full-channel assembly, and strict comparison with earlier adopted classes | **INCONCLUSIVE IN THIS REVIEW**: outside F507’s assigned mathematical audit |
| Literature novelty, independent-family, human, or kernel verification | **NOT ESTABLISHED** |

No substantive theorem from S2 is needed for the supported conclusions. In particular, the three-qubit Kramers-pair argument is **not** imported into four qubits.

## 3. Reconstruction of the actual \(H_3\) operator

### 3.1 Compatible marginals

Write

\[
|\psi_q\rangle=\sqrt q\,|\varnothing\rangle+
\frac{\sqrt r}{2}\sum_{j=1}^4|j\rangle,
\qquad r=1-q,\qquad u=\sqrt{qr}.
\]

For an erased qubit \(i\), the two conditional vectors are

\[
|v_i\rangle=\sqrt q\,|000\rangle+
\frac{\sqrt r}{2}\sum_{j\ne i}|j\rangle,
\qquad
\frac{\sqrt r}{2}|000\rangle.
\]

Therefore

\[
\rho_{\bar i}=|v_i\rangle\langle v_i|
+\frac r4|000\rangle\langle000|.
\]

This reconstructs S1:130–140 directly from the **same physical four-qubit state**. No independently chosen marginal is substituted.

Summing the physically placed lifts gives the entries listed in S1:210–218:

- Vacuum diagonal \(4q+r=4-3r\).
- Each singleton diagonal \(q+r=1\).
- Each pair diagonal \(r/2\).
- Singleton exchange entry \(r/2\).
- Pair exchange entry \(r/4\) when the pairs share one site.
- Vacuum–singleton entry \(3u/2\).
- Singleton–containing-pair entry \(u/2\).
- All remaining entries zero.

In particular, every vector of weight three or four is annihilated.

### 3.2 Explicit invariant decomposition

Let \(C\) be the \(4\times6\) incidence matrix from pair coordinates to singleton coordinates:

\[
C_{i,\{j,k\}}=
\begin{cases}
1,&i\in\{j,k\},\\
0,&\text{otherwise}.
\end{cases}
\]

In the weight-zero, weight-one, and weight-two spaces, the operator is

\[
H_3=
\begin{pmatrix}
4-3r & \frac{3u}{2}\mathbf1_4^\dagger & 0\\
\frac{3u}{2}\mathbf1_4 &
(1-\frac r2)I_4+\frac r2J_4 &
\frac u2 C\\
0&\frac u2 C^\dagger&\frac r4 C^\dagger C
\end{pmatrix},
\]

together with five zero dimensions from weights three and four.

The incidence identities are

\[
CC^\dagger=2I_4+J_4.
\]

Thus \(C\) has rank four and a two-dimensional kernel. That kernel supplies two further zero dimensions.

The symmetric singleton and pair vectors satisfy

\[
C|D_2\rangle=\sqrt6\,|D_1\rangle,
\qquad
C^\dagger|D_1\rangle=\sqrt6\,|D_2\rangle.
\]

For a unit zero-sum vector \(f\), the author’s normalized vectors satisfy

\[
C|f;2\rangle=\sqrt2\,|f;1\rangle,
\qquad
C^\dagger|f;1\rangle=\sqrt2\,|f;2\rangle.
\]

The normalization follows from

\[
\sum_{i<j}|f_i+f_j|^2=2\sum_i|f_i|^2
\quad\text{when}\quad \sum_i f_i=0.
\]

Consequently, an orthonormal basis of the zero-sum singleton space gives three orthogonal two-dimensional invariant blocks. This establishes the consuming invariant spaces explicitly; no unproved permutation-symmetry decomposition is required.

The resulting blocks are exactly

\[
A_3=
\begin{pmatrix}
4-3r&3u&0\\
3u&1+\frac32r&\sqrt{\frac32}u\\
0&\sqrt{\frac32}u&\frac32r
\end{pmatrix}
\]

and three copies of

\[
B_2=
\begin{pmatrix}
1-\frac r2&u/\sqrt2\\
u/\sqrt2&r/2
\end{pmatrix},
\]

with **seven additional zero eigenvalues**, as claimed in S1:220–239.

The dimensions account for all sixteen physical dimensions:

\[
3+3\cdot2+7=16.
\]

### 3.3 Positivity, traces, and eigenvalue bounds

Because these are restrictions of the actual positive marginal sum, both blocks are positive semidefinite. Their traces are

\[
\operatorname{Tr}A_3=5,\qquad
\operatorname{Tr}B_2=1.
\]

Hence every \(B_2\) eigenvalue is at most one. Independently,

\[
\det B_2
=\left(1-\frac r2\right)\frac r2-\frac{u^2}{2}
=\frac{r^2}{4},
\]

which gives the author’s eigenvalues

\[
\frac{1\pm\sqrt{1-r^2}}2.
\]

For every four-qubit density operator, not just this family,

\[
0\le \rho_{\bar i}\otimes I_i\le I_{16},
\]

so

\[
0\le H_3\le4I_{16}.
\]

In particular, \(\lambda_{\max}(A_3)\le4\).

Finally,

\[
\operatorname{Tr}H_3=5+3\cdot1=8,
\]

also agreeing with the direct trace of four lifted, trace-one three-qubit marginals.

## 4. Reconstruction of every \(H_3\) prefix

The reference is

\[
L_3=(4,1,1,1,1,0^{\times11}).
\]

Consider a top-\(k\) spectral selection for \(1\le k\le4\), and let \(j\) selected eigenvalues come from \(A_3\). Every other eigenvalue is at most one.

- **\(j=0\):** the sum is at most \(k\).
- **\(j=1\):** the sum is at most \(4+(k-1)=k+3\).
- **\(j\ge2\):** positivity and \(\operatorname{Tr}A_3=5\) give a sum at most
  \[
  5+(k-j)\le k+3.
  \]

Therefore

\[
K_k(H_3)\le k+3,\qquad 1\le k\le4.
\]

For \(5\le k\le16\), positivity and total trace eight give

\[
K_k(H_3)\le8,
\]

with equality of the complete traces at \(k=16\). These are precisely all prefixes of \(L_3\).

Thus S1:259–275 proves

\[
\boxed{H_3(|\psi_q\rangle\langle\psi_q|)\prec L_3
\quad\text{for every }q\in[0,1].}
\]

No parameter-dependent division or eigenvalue-gap assumption occurs. The closed endpoints are included.

### Physical phases, local unitaries, and mixtures

The phase reduction in S1:96 is valid: one global phase and four physical local diagonal phases remove the vacuum and single-excitation phases without changing the coefficient moduli.

For an arbitrary physical local unitary \(V\),

\[
H_3(V\rho V^\dagger)=VH_3(\rho)V^\dagger.
\]

For finite mixtures, \(H_3\) is linear and each Ky Fan sum is convex. Equivalently, the same arbitrary complex consuming projector can be used componentwise. Hence the **\(H_3\)** conclusion extends to the stated local-unitary orbit and its finite convex hull.

This extension does not, by itself, establish the author’s separate full-channel claim.

## 5. Unrestricted-density second-moment certificate

Let \(H=H_3(\rho)\) for an arbitrary four-qubit density operator. Universally,

\[
H\ge0,\qquad \operatorname{Tr}H=8,\qquad H\le4I_{16}.
\]

For \(x=K_k(H)\), applying Cauchy–Schwarz separately to the top \(k\) and remaining \(16-k\) eigenvalues yields

\[
\operatorname{Tr}H^2
\ge f_k(x):=\frac{x^2}{k}+\frac{(8-x)^2}{16-k}.
\]

Its derivative is

\[
f_k'(x)=\frac{32(x-k/2)}{k(16-k)}.
\]

Thus \(f_k\) is strictly increasing throughout the forbidden region beyond each relevant prefix boundary. At those boundaries,

\[
f_2(5)=\frac{92}{7},\qquad
f_3(6)=\frac{160}{13},\qquad
f_4(7)=\frac{37}{3}.
\]

The minimum is \(160/13\), since

\[
\frac{92}{7}-\frac{160}{13}=\frac{76}{91}>0,
\qquad
\frac{37}{3}-\frac{160}{13}=\frac1{39}>0.
\]

Consequently, if

\[
\operatorname{Tr}H^2\le\frac{160}{13},
\]

a violation of any of \(K_2\le5\), \(K_3\le6\), or \(K_4\le7\) would force a **strictly larger** second moment. The first prefix follows from \(H\le4I\), and the prefixes from five onward follow from positivity and trace eight.

Therefore S1:595–619 establishes

\[
\boxed{\operatorname{Tr}[H_3(\rho)^2]\le\frac{160}{13}
\ \Longrightarrow\ H_3(\rho)\prec L_3.}
\]

The equality case is safe. This is a sufficient condition, not a necessary condition or an unrestricted majorization theorem.

## 6. Pure-state Pauli and spin-flip reconstruction

Use the author’s convention

\[
\rho=\frac{I+C_1+C_2+C_3+C_4}{16},
\qquad
S_j=\sum_{\operatorname{wt}(P)=j}(\operatorname{Tr}\rho P)^2.
\]

For pure \(\rho\), summing the one-qubit purities gives

\[
\sum_i\operatorname{Tr}\rho_i^2=\frac{4+S_1}{2}.
\]

Summing the complementary three-qubit purities gives

\[
\sum_i\operatorname{Tr}\rho_{\bar i}^2
=\frac{4+3S_1+2S_2+S_3}{8}.
\]

Complementary purities agree for every pure bipartition. Equating these expressions yields

\[
S_3=12+S_1-2S_2.
\]

Global purity gives

\[
1+S_1+S_2+S_3+S_4=16,
\]

and therefore

\[
S_4=3-2S_1+S_2.
\]

Now set

\[
\Theta=Y^{\otimes4}\mathcal K,\qquad
\widetilde\rho=\Theta\rho\Theta^{-1},
\qquad
\eta=\operatorname{Tr}(\rho\widetilde\rho).
\]

For four qubits,

\[
\Theta^2=+I.
\]

There is no general Kramers orthogonality. For pure \(\rho\),

\[
\eta=|\langle\psi|\Theta\psi\rangle|^2.
\]

Spin flip changes the sign of each odd-weight Pauli term, so

\[
16\eta=1-S_1+S_2-S_3+S_4.
\]

Substituting the preceding identities gives

\[
S_2=S_1+2+4\eta.
\]

The actual lifted marginal sum is

\[
H_3=\frac{4I+3C_1+2C_2+C_3}{8}.
\]

Pauli orthogonality then gives

\[
\begin{aligned}
\operatorname{Tr}H_3^2
&=4+\frac94S_1+S_2+\frac14S_3\\
&=7+\frac52S_1+\frac12S_2\\
&=\boxed{8+3S_1+2\eta}.
\end{aligned}
\]

Thus S1:623–670 establishes the claimed pure-state certificate

\[
\boxed{3S_1+2\eta\le\frac{56}{13}
\ \Longrightarrow\ H_3(\rho)\prec L_3.}
\]

The author’s \(\eta=0\) statement for the coherent vacuum–\(W_4\) family also follows from its weight-zero/one support and the spin-flipped weight-three/four support. That family-specific orthogonality has not been generalized to arbitrary four-qubit pure states.

## 7. Findings, boundaries, and residual

### Mathematical findings

**FATAL: 0. MAJOR: 0. MINOR: 0.**

The requested block construction, invariant-space routing, positivity, trace accounting, eigenvalue bounds, all-prefix allocation, second-moment threshold, equality handling, and four-qubit Pauli identity are supported by the written reconstructions above.

### Retained qualifications

- The F480 transcript-only ACK history remains a disclosed transport fault, not a repaired direct-delivery record.
- All designated held episodes and their consumers remain NONINPUT. This review rehabilitates none of them.
- S2 was completely read but is not a load-bearing mathematical import here.
- The author’s \(H_2\), full-channel, genuine-entanglement comparison, and strict-enlargement arguments require their own assigned review dispositions.
- This is same-harness written reconstruction, not independent-family, human, formal/kernel, or novelty certification.

### Literal unrestricted residual

For an arbitrary complex pure input outside the supported family and sufficient-condition region, the remaining \(H_3\) inequalities are still

\[
K_2(H_3)\le5,\qquad
K_3(H_3)\le6,\qquad
K_4(H_3)\le7.
\]

No replacement for the family’s explicit block constraints has been proved here. Failure of the second-moment condition proves neither a layer violation nor an actual-channel violation. No physical counterexample is constructed.

**Completed return:** full written support for the frozen coherent vacuum–\(W_4\) \(H_3\) theorem and unrestricted-input second-moment sufficient certificate, with no mathematical findings in that scope. Adoption remains a parent disposition.

overall_correctness: correct

explanation: The actual compatible-marginal construction yields the claimed \(A_3\), three \(B_2\) blocks, and seven zeros, and its bounds prove every \(H_3\) prefix throughout the complete parameter interval. The unrestricted second-moment certificate and pure-state Pauli identity are also supported; this verdict does not accept the separately assigned \(H_2\)/channel claims or close the unrestricted four-qubit target.

confidence: 0.99