# f532 — WRITTEN review of the explicit forty-ray cyclic four-sector construction

**Verdict: SUPPORTED at the exact forty-ray \(\mathbb C^4\) scope.**  
**Findings: 0 FATAL / 0 MAJOR / 0 MINOR.**

The displayed vectors give forty pairwise nonparallel unit vectors on \(S=\{0,1,5,6\}\), and every one of the ten physical rows, ten columns and ten cyclic symbol classes restricts to an orthonormal basis of \(\mathbb C^4\). This does **not** supply the complementary sixty-ray \(\mathbb C^6\) construction or settle the original hundred-ray target.

## 1. Review boundary and process record

The reviewed frozen wave is:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f532-rqls10-explicit-forty-ray-four-sector-physical-review/`

Binding metadata:

- Manifest SHA-256: `2aa579fabe69d82fab68660ba7393324fbaf3cd6feea476c947fa52c365d04b1`.
- Freeze-receipt SHA-256: `e0f2018cf22473b3324972af4caba5b82f1c46a19525ab49dd7af4a3089cc734`.
- Literal-packet SHA-256: `8a001dba7c28d067319f951e9a51b2ded2da18f44eb321007018eda6fc68f461`.

These live hashes, byte/LF counts and the supplied clock observation are **parent-observed metadata**, not my own hash execution or native start observation.

Before reading the mathematical packet, I completed the manifest, freeze receipt, dispatch receipt, parent metadata supply and all twelve manifest-listed permission/status controls, including their endings. I then sent the direct pre-body ACK to Main. Subsequently I read the entire 363-LF literal packet in consecutive raw windows of at most twenty LF, through its ending, before deriving.

The mathematical input was exactly:

- **S1:** f496 `review-v1.md`, SHA-256 `b12cd548fbb850d1c13d2cb06cc0e2a47adf7a34b919bec68bff70d4ed0a6784`, **LF1–332 only**. The whole source has 584 LF; its optional checker and subsequent excluded material were not read.
- **S2:** `physics-5-rqls10-binary-sector-and-cyclic-rank4-family-exclusions-parent-v1.md`, SHA-256 `a4c7197d031810d9986249612b98749efc2edf705986808b718c609b9704152b`, **LF1–29 completely**.

All citations below refer to those source-line labels in the literal packet.

**Method:** written reconstruction only. No new selected parameter or orientation instance, scientific code, interpreter/CAS, enumeration, replay, external source, sibling return or held mathematical payload was used. The status controls were read only as exclusions. No scientific execution or workspace-file write was performed in this review; this full body is returned for parent materialization.

The parent reports one subsequent exact **author-code** execution with exit zero. I did not inspect or use that code/run receipt as proof, and that execution is not an independent finite verification. S1’s NOTRUN statement is its author-time evidence classification, not a claim that no subsequent parent execution occurred.

## 2. Per-claim dispositions

| Claim | Disposition | Source scope |
|---|---|---|
| The CRT formulas select exactly forty physical cells of \(H_S\). | **SUPPORTED** | S1 LF41–71 |
| The formulas specify forty unit vectors with no unresolved parameter or equation-solving step. | **SUPPORTED** | S1 LF73–172 |
| The unitary recurrence, commuting involutions and two closing identities hold exactly. | **SUPPORTED** | S1 LF95–108, LF174–218 |
| The actual cell assignment has the stated row/column/symbol eigenvalue signs. | **SUPPORTED** | S1 LF144–170, LF222–249 |
| All thirty physical restricted contexts are ONBs. | **SUPPORTED** | S1 LF251–274 |
| All forty rays are pairwise nonparallel. | **SUPPORTED** | S1 LF276–294 |
| Cell relabeling realizes all ten supports consisting of two antipodal pairs. | **SUPPORTED** | S1 LF296–304 |
| For this fixed cyclic \(4+6\) support branch, completing the hundred-ray object is equivalent to supplying the stated sixty-ray \(\mathbb C^6\) complement. | **SUPPORTED** | S1 LF306–316 |
| Such a six-dimensional complement cannot itself split into smaller actual orthogonal ray sectors under global nonparallelness. | **SUPPORTED**, using the cyclic even-sector statement at its stated scope | S1 LF318; S2 LF7, LF11–13 |
| A sixty-ray complement exists, or is impossible. | **INCONCLUSIVE / NOT PROVED** | Neither is supplied |
| The unrestricted original hundred-ray target, rank-28 \(5+5\) branch, or other residual support orbit is settled. | **NOT PROVED; expressly excluded** | S1 LF15–17, LF325–330 |

No reviewed construction claim is refuted.

## 3. Exact physical support and all thirty contexts

Write the row and column coordinates as

\[
r\leftrightarrow(a,u)=(r\bmod5,r\bmod2),\qquad
c\leftrightarrow(b,v)=(c\bmod5,c\bmod2),
\]

with inverse

\[
\operatorname{crt}(a,u)=a+5((u-a)\bmod2).
\]

Thus \((a,u)\) and \((b,v)\) specify actual row and column indices modulo ten.

Because the two lifts of residue \(0\) modulo five are \(0,5\), and those of residue \(1\) are \(1,6\),

\[
c-r\in\{0,1,5,6\}\pmod{10}
\iff b-a\in\{0,1\}\pmod5.
\]

Consequently the selected cells are exactly the ten disjoint four-cell blocks

\[
A_a=\{((a,u),(a,v)):u,v\in\{0,1\}\},
\]

\[
B_a=\{((a,u),(a+1,v)):u,v\in\{0,1\}\},
\qquad a\in\mathbb Z_5.
\]

There are therefore exactly \(10\cdot4=40\) selected cells.

The actual physical context routing is as follows.

- **Row \((a,u)\):** \(A_a\) and \(B_a\), each restricted to that \(u\), with both values of \(v\).
- **Column \((b,v)\):** \(A_b\) and \(B_{b-1}\), each restricted to that \(v\), with both values of \(u\).
- **Cyclic symbol \((s,w)\):** this means
  \[
  r+c\equiv s\pmod5,\qquad u+v\equiv w\pmod2.
  \]
  Set \(a=3s\pmod5\). The selected cells are precisely the two appropriate cells of \(A_a\) and the two appropriate cells of \(B_{a+2}\).

For the last assertion, an \(A_j\)-cell has symbol residue \(2j\), whereas a \(B_j\)-cell has residue \(2j+1\). Since \(2^{-1}=3\) in \(\mathbb Z_5\),

\[
2j=s\implies j=a,\qquad
2j+1=s\implies j=a+2.
\]

The parity condition supplies two cells in each block. These formulas cover all ten contexts of each physical type, rather than selected rows or symbol classes.

## 4. Complete exact vector assignment

Use the Pauli matrices

\[
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
Y=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\]

and

\[
N(\theta)=\cos\theta\,Z+\sin\theta\,X.
\]

The author-specified angles are

\[
\theta_1=0,\qquad
\theta_2=\frac{\pi}{4},\qquad
\theta_3=\frac{\pi}{8},\qquad
\theta_4=\frac{3\pi}{8},
\quad N_i=N(\theta_i).
\]

The five unitaries are exactly

\[
U_0=I,\quad
U_1=-Z,\quad
U_2=-e^{-iY\pi/4},\quad
U_3=N(-\pi/8),\quad
U_4=-iY.
\]

Define

\[
w_0^\epsilon=\frac1{\sqrt2}\binom{1}{\epsilon i},
\qquad \epsilon\in\{+1,-1\},
\]

and, for \(1\le i\le4\),

\[
w_i^+=
\binom{\cos(\theta_i/2)}{\sin(\theta_i/2)},\qquad
w_i^-=
\binom{-\sin(\theta_i/2)}{\cos(\theta_i/2)}.
\]

These are orthonormal eigenvector pairs of \(Y\) and \(N_i\), respectively.

The four-component vectors, in \(\mathbb C^2\oplus\mathbb C^2\), are

\[
Q_i^{\mathsf U}(\epsilon,\eta)
=
\frac1{\sqrt2}
\begin{pmatrix}
w_i^\epsilon\\
\eta U_i^\dagger w_i^\epsilon
\end{pmatrix},
\]

\[
Q_i^{\mathsf V}(\epsilon,\eta)
=
\frac1{\sqrt2}
\begin{pmatrix}
w_i^\epsilon\\
-i(-1)^i\eta U_i^\dagger w_i^\epsilon
\end{pmatrix},
\qquad \epsilon,\eta\in\{+1,-1\}.
\]

The complete lookup and physical-observable assignment are:

| \(a\) | \(A_a\): \((i,\text{branch})\) | \(B_a\): \((i,\text{branch})\) | \(R_a\) | \(C_a\) | \(D_a\) |
|---:|---|---|---|---|---|
| 0 | \((0,\mathsf U)\) | \((4,\mathsf V)\) | \(b_4\) | \(t_0\) | \(g_0\) |
| 1 | \((3,\mathsf V)\) | \((2,\mathsf V)\) | \(b_2\) | \(b_3\) | \(g_3\) |
| 2 | \((1,\mathsf V)\) | \((0,\mathsf V)\) | \(b_0\) | \(b_1\) | \(g_1\) |
| 3 | \((4,\mathsf U)\) | \((3,\mathsf U)\) | \(t_3\) | \(t_4\) | \(g_4\) |
| 4 | \((2,\mathsf U)\) | \((1,\mathsf U)\) | \(t_1\) | \(t_2\) | \(g_2\) |

For every physical cell, use the indicated \(i\) and branch and set

\[
q_{A_a;u,v}
=
Q_i^{\text{branch}}\bigl((-1)^{u+v},(-1)^v\bigr),
\]

\[
q_{B_a;u,v}
=
Q_i^{\text{branch}}\bigl(-(-1)^{u+v},-(-1)^u\bigr).
\]

Together with the CRT inverse, these formulas specify all forty physical four-component vectors exactly.

## 5. Operator reconstruction, including the closing vertices

### 5.1 The unitary recurrence

The Pauli multiplication rule gives the formal identity

\[
N(\alpha)N(\beta)=e^{-iY(\alpha-\beta)}.
\]

Using the displayed author angles,

\[
N_2N_1=N_4N_3=e^{-iY\pi/4}.
\]

It follows that the stated list of \(U_i\) satisfies

\[
U_i=(-1)^iN_iU_{i-1},\qquad 1\le i\le4,
\]

including

\[
U_3=N(\pi/8)e^{-iY\pi/4}=N(-\pi/8),
\]

and

\[
U_4=N_4N_3N_2N_1=e^{-iY\pi/2}=-iY.
\]

Thus the explicit list and recurrence agree; closure is exact.

### 5.2 Involutions and commutation

Define

\[
T(U)=\begin{pmatrix}0&U\\U^\dagger&0\end{pmatrix},
\qquad J(U)=T(iU),
\]

\[
t_i=T(U_i),\qquad b_i=(-1)^iJ(U_i),
\]

\[
g_0=\operatorname{diag}(Y,Y),
\]

\[
g_i=
\operatorname{diag}\bigl(N_i,U_{i-1}^\dagger N_iU_{i-1}\bigr)
\quad(1\le i\le4).
\]

Every displayed matrix is a Hermitian involution. For \(t_i,b_i\), the off-diagonal blocks are unitary and the trace is zero. For \(g_i\), both diagonal blocks are traceless two-dimensional Hermitian involutions. Each therefore has two \(+1\) and two \(-1\) eigenvalues.

For \(1\le i\le4\), block multiplication shows that \(g_i\) commutes with both \(T(U_{i-1})\) and \(J(U_{i-1})\). The recurrence then gives

\[
t_i=(-1)^ig_it_{i-1},\qquad
b_i=-(-1)^ig_ib_{i-1},
\]

with commuting factors.

Also,

\[
U_i^\dagger N_iU_i
=
U_{i-1}^\dagger N_iU_{i-1}.
\]

Hence, writing \(K_0=Y\) and \(K_i=N_i\) otherwise,

\[
g_i=\operatorname{diag}(K_i,U_i^\dagger K_iU_i)
\]

for every \(i\). This is the form needed to check the proposed eigenvectors directly.

For the closing identities, \(U_4=-iY\) gives

\[
b_4=T(Y)=g_0t_0,
\]

and direct block multiplication gives

\[
b_0t_4
=
\begin{pmatrix}0&iI\\-iI&0\end{pmatrix}
\begin{pmatrix}0&-iY\\iY&0\end{pmatrix}
=-\operatorname{diag}(Y,Y)
=-g_0.
\]

The factors commute here as well. Both closing identities, including their signs, are therefore supported.

### 5.3 The proposed joint eigenbases

Direct substitution yields

\[
g_iQ_i^{\mathsf U}(\epsilon,\eta)
=\epsilon Q_i^{\mathsf U}(\epsilon,\eta),\qquad
t_iQ_i^{\mathsf U}(\epsilon,\eta)
=\eta Q_i^{\mathsf U}(\epsilon,\eta),
\]

and

\[
g_iQ_i^{\mathsf V}(\epsilon,\eta)
=\epsilon Q_i^{\mathsf V}(\epsilon,\eta),\qquad
b_iQ_i^{\mathsf V}(\epsilon,\eta)
=\eta Q_i^{\mathsf V}(\epsilon,\eta).
\]

Within either fixed branch,

\[
\left\langle Q_i^{\text{branch}}(\epsilon,\eta),
Q_i^{\text{branch}}(\epsilon',\eta')\right\rangle
=
\delta_{\epsilon,\epsilon'}\frac{1+\eta\eta'}2.
\]

Thus all four vectors form an ONB, with every pair of joint eigenvalue signs occurring once. This establishes the one-dimensional joint eigenspaces explicitly, rather than assuming that commuting involutions must have four independent joint eigenvectors.

### 5.4 All ten block triples and their signs

The recurrence and closing identities give the following complete table:

| \(a\) | \(A_a\): \((R_a,C_a,D_a)\) | \(B_a\): \((R_a,C_{a+1},D_{a-2})\) |
|---:|---|---|
| 0 | \((g_0t_0,t_0,g_0)\) | \((b_4,-g_4b_4,g_4)\) |
| 1 | \((g_3b_3,b_3,g_3)\) | \((b_2,-g_2b_2,g_2)\) |
| 2 | \((g_1b_1,b_1,g_1)\) | \((b_0,-g_0b_0,g_0)\) |
| 3 | \((g_4t_4,t_4,g_4)\) | \((t_3,-g_3t_3,g_3)\) |
| 4 | \((g_2t_2,t_2,g_2)\) | \((t_1,-g_1t_1,g_1)\) |

Each triple consists of commuting involutions. Its product is \(+I\) in the \(A\)-column and \(-I\) in the \(B\)-column.

In the \(A\)-blocks the joint labels \((\epsilon,\eta)\) give observable signs

\[
(R,C,D)=(\epsilon\eta,\eta,\epsilon).
\]

In the \(B\)-blocks they give

\[
(R,C,D)=(\eta,-\epsilon\eta,\epsilon).
\]

Substituting the actual bit-to-label assignment therefore gives exactly

| Physical cell | Row sign | Column sign | Symbol sign |
|---|---|---|---|
| \(A_a;u,v\) | \((-1)^u\) | \((-1)^v\) | \((-1)^{u+v}\) |
| \(B_a;u,v\) | \(-(-1)^u\) | \(-(-1)^v\) | \(-(-1)^{u+v}\) |

The \(B_a\) observables are specifically \(R_a,C_{a+1},D_{a-2}\). Thus the consuming physical row, column and symbol routes match the producer lookup, including the modulo-five shifts.

## 6. Proof of all thirty physical ONBs

Each map from the four bit pairs \((u,v)\) to \((\epsilon,\eta)\) is bijective. Every \(A_a\) and \(B_a\) is consequently a complete four-vector ONB.

Now quantify over all physical contexts.

### Rows

For every \(a\in\mathbb Z_5\) and \(u\in\mathbb Z_2\):

- The two \(A_a;u,v\) vectors are orthonormal and lie in
  \[
  R_a=(-1)^u.
  \]
- The two \(B_a;u,v\) vectors are orthonormal and lie in
  \[
  R_a=-(-1)^u.
  \]

These are complementary two-dimensional eigenspaces. Their four-vector union is an ONB of \(\mathbb C^4\). This proves all ten row assertions.

### Columns

For every \(b\in\mathbb Z_5\) and \(v\in\mathbb Z_2\):

- The two relevant \(A_b\)-vectors occupy \(C_b=(-1)^v\).
- The two relevant \(B_{b-1}\)-vectors occupy \(C_b=-(-1)^v\).

Again they span complementary two-dimensional eigenspaces, proving all ten column assertions.

### Cyclic symbols

For every \((s,w)\in\mathbb Z_5\times\mathbb Z_2\), put \(a=3s\). The physical support calculation identifies the context as the relevant pairs in \(A_a\) and \(B_{a+2}\).

- The \(A_a\)-pair occupies \(D_a=(-1)^w\).
- The \(B_{a+2}\)-pair occupies \(D_{(a+2)-2}=D_a=-(-1)^w\).

Each pair is orthonormal within its block. They span complementary two-dimensional eigenspaces, proving all ten symbol assertions.

Therefore all **thirty** physical restricted contexts are ONBs.

## 7. Proof that the forty rays are globally distinct

The first two-component block of every vector is the nonzero vector \(w_i^\epsilon/\sqrt2\).

For different \(i\), these first-block rays are disjoint. Indeed, two traceless Hermitian involutions on \(\mathbb C^2\) sharing an eigenray also share its orthogonal complement, so they must agree up to sign. The five displayed axes

\[
Y,\quad Z,\quad N(\pi/4),\quad N(\pi/8),\quad N(3\pi/8)
\]

are pairwise unequal up to sign. The \(Y\)-axis is distinct from the real \(XZ\)-plane axes, and the four author-specified planar angles are distinct modulo \(\pi\).

For a fixed \(i\), different \(\epsilon\) already have orthogonal first-block rays. For fixed \(i,\epsilon\), all four vectors have exactly the same upper block. Their lower-block multipliers are

\[
+1,\ -1,\ +i,\ -i
\]

in some order. The lower block is nonzero because \(U_i\) is unitary. Any projective equality would have scalar \(1\), forced by the identical nonzero upper block, and would then require equal lower multipliers. None coincide.

The lookup uses each \((i,\mathsf U)\) and each \((i,\mathsf V)\) exactly once. Thus there are eight distinct rays per \(i\), giving exactly **forty pairwise nonparallel unit vectors**.

## 8. Affine transport and the precise sixty-ray obligation

For every unit \(h\in\mathbb Z_{10}^{\times}\) and \(t\in\mathbb Z_{10}\),

\[
(r,c)\longmapsto(hr,hc+t)
\]

permutes rows and columns, sends cyclic symbol \(r+c\) to \(h(r+c)+t\), and sends the support to \(H_{hS+t}\). Transporting the assignment therefore preserves every proved ONB condition and global ray distinctness. No unitary covariance of the rays is assumed.

The antipodal pairs correspond to the five residues modulo five. The support \(S\) is two such pairs. Given any two distinct residues, translation and multiplication by a nonzero residue send \(\{0,1\}\) to that pair; each nonzero residue has a unit lift modulo ten. The orbit is therefore exactly the

\[
\binom52=10
\]

supports consisting of two antipodal pairs.

For any fixed support in this orbit, the complementary cells have CRT description

\[
b-a\in\{2,3,4\}\pmod5.
\]

There are sixty such cells and six in every physical row, column and cyclic symbol class.

The remaining extension problem is exactly to supply **sixty pairwise nonparallel unit vectors in \(\mathbb C^6\)** on those cells such that all thirty restricted contexts are six-element ONBs.

- **Necessity:** a full realization with this actual orthogonal \(4+6\) sector decomposition restricts to those sixty vectors.
- **Sufficiency:** take the orthogonal direct sum of the proved forty-ray assignment and any such sixty-ray assignment. Every full context is then a ten-element ONB. Rays in opposite summands cannot be parallel.

This equivalence concerns the specified cyclic \(4+6\) branch. It does not assert that every possible solution of the unrestricted original target must have that decomposition.

### Smaller sector splitting

The two-dimensional obstruction is valid: in an actual two-dimensional ray sector, a row and column through a selected cell each contain exactly two sector rays. Their other selected cells are distinct, but both rays lie in the same one-dimensional orthogonal complement of the shared ray. They are therefore parallel, contrary to global nonparallelness.

The cyclic even-sector input is S2 LF11–13, at the actual-sector scope of S2 LF7. Its cyclic specialization also follows directly: parity satisfies \(w=u+v\pmod2\). Counting sector incidences in the five odd rows, five odd columns and five odd symbol classes gives \(15d\); each selected cell contributes an even number to this total. Hence \(d\) is even.

A six-dimensional complement cannot consequently split into smaller positive actual sectors: all summand dimensions would be even, and no summand can have dimension two. This does not construct or exclude an unsplit six-dimensional complement.

## 9. Imports, findings and final limits

**Exact imports used**

- S2 LF7: the physical meaning of an actual orthogonal ray sector and its exact context counts.
- S2 LF11–13: the cyclic even-sector conclusion, also reconstructed above.
- S1 LF41–318: the displayed construction and statements audited here.

The forty-ray construction itself does not rely on an external theorem, the author checker, a run result, prior reviewer acceptance, the earlier mask-exclusion proof, or an assumed symmetry of the ray assignment. The other S2 historical proof/execution statements were not promoted into fresh verification claims.

**FATAL: 0. MAJOR: 0. MINOR: 0.**

**Overall correctness: correct.** The frozen author construction is supported at its exact forty-ray \(\mathbb C^4\) scope by the complete written reconstruction above. The complementary sixty-ray problem and the original hundred-ray target remain unproved; this return supplies neither the other WRITTEN gate nor the independent FINITE gate.

**Confidence: 0.97**, limited to the stated written verdict. No independent-family, human, formal/kernel, novelty or worldwide-priority assurance is claimed.