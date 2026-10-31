# Written review: Amosov Proposition 4 ancillary orbit-span obstruction

**Role:** WRITTEN  
**Disposition:** **SUPPORTED at the stated proof-step scope.** The frozen candidate correctly refutes the ancillary orbit-dimension and irreducibility assertions in the accessible public manuscript. It does **not** refute Proposition 4’s majorization inequality.

This is the complete materializable review body. No working-tree file was written under the read-only assignment.

## 1. Frozen inputs, read frontier, and method

The following identities are **parent-supplied metadata**, not independently computed child hashes or clocks:

| Record | SHA-256 |
|---|---|
| Manifest | `22198ff8aa7686068ccc621180b17a96f870c82931af27c0e3d443f5d651668b` |
| Freeze receipt | `9b21071c6076b19d72fbe90ee4e77f6421ea4e001341021f99f0a4c16d6cd880` |
| Literal packet | `6e0619d5b15ccfb7c672945de101fad2dbe5e4ddc3fab2a5448be684781234b7` |

Before opening mathematical bodies, I read the complete manifest, freeze receipt, all seven declared status-only controls, the parent metadata supply, and dispatch receipt. I then sent an administrative pre-body ACK to Main.

The complete literal packet was subsequently read **in order, raw, LF 1–485**, in windows of at most 20 lines, including every source ending:

- **S1:** author candidate, labelled LF 1–44.
- **S2:** bounded public Proposition 4 reader excerpt, LF 1–33.
- **S3:** bounded source-audit return, labelled LF 1–406.

S3 was used as the expressly authorized source-status context, **not as a mathematical proof premise**.

After completing that packet, I directly inspected the relevant public manuscript passages:

- [Amosov v6, §5, Eqs. (14)–(16)](https://arxiv.org/html/2103.08515v6#S5).
- [§6, Proposition 1 and Proposition 4, including its complete displayed proof](https://arxiv.org/html/2103.08515v6#S6).
- Proposition 5’s statement and opening proof step, specifically its invocation of Proposition 4.

The reconstruction below is written mathematics. **No scientific code, interpreter, calculator, CAS, solver, enumeration, numerical replay, new selected example, sibling output, author program, or held scientific payload was used.** No independent finite execution or child-native clock/hash verification is claimed.

## 2. Exact public assertion under review

The public Proposition 4 assumes an output-majorization bound

\[
\lambda\!\left(\Phi(|e\rangle\langle e|)\right)\prec q
\]

for **every unit vector \(e\in H\)** and claims an ancillary extension for **every unit vector \(f\in K\otimes H\)**.

There is no product-state or Schmidt-rank-one restriction on \(f\) in the inspected statement. This is preserved in **S2 LF 10–21**.

Its proof introduces

\[
\mathcal L=\operatorname{span}\{(I_K\otimes U_g)f:g\in G\}.
\]

After asserting that the \(n^2\) matrices \(U_g\) are linearly independent, it states “Hence \(\dim\mathcal L=n\)” and identifies the restricted action with an irreducible \(n\)-dimensional representation. These are the assertions preserved in **S2 LF 25–26**.

**Assessment: SUPPORTED.** S1 accurately identifies the literal assertion and its unrestricted ancillary quantifier.

## 3. Independent reconstruction of the admissible Pauli example

### 3.1 Group, subgroup, and projective representation

Let

\[
G=\mathbb Z_2\times\mathbb Z_2,\qquad
H=K=\mathbb C^2,\qquad n=2,
\]

and define

\[
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
U_{(a,b)}=X^aZ^b.
\]

All exponents and group coordinates are taken modulo two. Since \(ZX=-XZ\),

\[
U_{(a,b)}U_{(c,d)}
=(-1)^{bc}U_{(a+c,b+d)}.
\]

Thus this is a unitary **projective** representation, with scalar multiplier \((-1)^{bc}\). In particular, the fact that \(G\) is Abelian does not force this projective representation to be one-dimensional.

Take

\[
T=\{(0,0),(0,1)\}.
\]

Because \(G\) is Abelian, \(T\) is normal and Abelian. The restriction to \(T\) is the ordinary unitary representation \(\{I,Z\}\), since \(Z^2=I\), and

\[
|G/T|=2=n,\qquad |G|=4=n^2.
\]

These meet the group and representation hypotheses relevant to the example. The associated basis permutation is explicitly

\[
\alpha_{[(a,b)]}(j)=j+a\pmod 2.
\]

### 3.2 Irreducibility and matrix independence

A nonzero proper subspace of \(\mathbb C^2\) would be a line. Any line invariant under \(Z\) must be one of its two eigenspaces, whereas \(X\) exchanges those eigenspaces. Therefore no line is invariant under both \(X\) and \(Z\), and the projective representation is irreducible.

The four matrices are also linearly independent over \(\mathbb C\). Indeed,

\[
aI+bZ+cX+dXZ
=
\begin{pmatrix}
a+b&c-d\\
c+d&a-b
\end{pmatrix}.
\]

If this matrix vanishes, its diagonal equations give \(a=b=0\), and its off-diagonal equations give \(c=d=0\). Hence

\[
\operatorname{span}_{\mathbb C}\{I,Z,X,XZ\}
=\operatorname{End}(\mathbb C^2).
\]

**Assessment: SUPPORTED.** The example satisfies, rather than evades, the matrix-independence premise used in the public argument.

### 3.3 Four orthogonal orbit vectors

For the frozen selected vector

\[
f=\frac{|00\rangle+|11\rangle}{\sqrt2},
\]

the four orbit vectors are

\[
\begin{aligned}
(I\otimes I)f&=\frac{|00\rangle+|11\rangle}{\sqrt2},\\
(I\otimes Z)f&=\frac{|00\rangle-|11\rangle}{\sqrt2},\\
(I\otimes X)f&=\frac{|01\rangle+|10\rangle}{\sqrt2},\\
(I\otimes XZ)f&=\frac{|01\rangle-|10\rangle}{\sqrt2}.
\end{aligned}
\]

The sign in the final expression follows from \(XZ|0\rangle=|1\rangle\) and \(XZ|1\rangle=-|0\rangle\).

Each vector has norm one. The first pair and second pair have disjoint computational-basis support; within each pair, the inner product is \((1-1)/2=0\). They are therefore an orthonormal basis of \(K\otimes H\). Consequently,

\[
\boxed{\mathcal L=K\otimes H,\qquad \dim\mathcal L=4\ne n.}
\]

Furthermore,

\[
K\otimes H
=(|0\rangle\otimes H)\oplus(|1\rangle\otimes H)
\]

is an orthogonal decomposition into invariant subspaces. On each summand, \(I_K\otimes U_g\) acts as \(U_g\). Thus the restricted action is **two equivalent irreducible two-dimensional copies**, not one irreducible representation.

**Assessment: SUPPORTED for S1 LF 15–30.**  
**Public intermediate assertions: REFUTED.**

## 4. Channel admissibility and the selected majorization inequality

### 4.1 Physical channel and single-use reference

Use precisely the frozen weights

\[
\pi_I=\frac58,\qquad
\pi_Z=\pi_X=\pi_{XZ}=\frac18.
\]

They are nonnegative and sum to one, so their unitary mixture is a completely positive trace-preserving channel.

For every \(A\in M_2(\mathbb C)\), the Pauli identity

\[
A+ZAZ^*+XAX^*+(XZ)A(XZ)^*
=2\operatorname{Tr}(A)I
\]

gives

\[
\Phi(A)
=\frac12A+\frac14\operatorname{Tr}(A)I.
\]

This is exactly the assignment’s depolarizing convention at \(p=1/2\). For any unit \(e\),

\[
\Phi(|e\rangle\langle e|)
=\frac12|e\rangle\langle e|+\frac14I,
\]

whose eigenvalues are

\[
q=\left(\frac34,\frac14\right).
\]

The single-use premise holds with equality for every pure input, including complex inputs.

### 4.2 Actual Eq. (16) cross-coset ordering

The ordered cosets are

\[
T=\{I,Z\},\qquad XT=\{X,XZ\},
\]

with marginal weights

\[
p_0=\frac58+\frac18=\frac34,\qquad
p_1=\frac18+\frac18=\frac14.
\]

The inspected Eq. (16) requires that every individual weight in a later coset be at most every individual weight in an earlier coset. Here every later weight is \(1/8\), while the earlier weights are \(5/8\) and \(1/8\). Therefore every required comparison holds.

This checks the literal cross-coset condition, not merely an ordering of the two marginal sums.

**Assessment: SUPPORTED for the admissibility statements in S1 LF 32.**

### 4.3 Bell output: rank, spectrum, and every prefix

Let the four orthonormal orbit vectors above be \(b_I,b_Z,b_X,b_{XZ}\). Directly from the channel definition,

\[
(\operatorname{id}\otimes\Phi)(|f\rangle\langle f|)
=
\frac58|b_I\rangle\langle b_I|
+\frac18\sum_{g\ne I}|b_g\rangle\langle b_g|.
\]

Thus the output has rank four and spectrum

\[
\mu=\left(\frac58,\frac18,\frac18,\frac18\right).
\]

The same conclusion follows independently from

\[
\operatorname{Tr}_H(|f\rangle\langle f|)=\frac12I_K,
\]

which yields

\[
(\operatorname{id}\otimes\Phi)(|f\rangle\langle f|)
=\frac12|f\rangle\langle f|+\frac18I_4.
\]

The relevant comparison vector in this \(n=N=2\) case is

\[
\widetilde q=\left(\frac34,\frac14,0,0\right).
\]

All majorization prefixes are:

| \(k\) | \(\sum_{j=1}^k\mu_j^\downarrow\) | \(\sum_{j=1}^k\widetilde q_j^\downarrow\) |
|---:|---:|---:|
| 1 | \(5/8\) | \(3/4\) |
| 2 | \(3/4\) | \(1\) |
| 3 | \(7/8\) | \(1\) |
| 4 | \(1\) | \(1\) |

Therefore

\[
\boxed{\mu\prec\widetilde q.}
\]

**Assessment: SUPPORTED.** The selected example satisfies the proposition’s claimed inequality. Its rank-four output refutes the proof’s reduction to an equivalent two-dimensional channel, **not the inequality itself**.

## 5. Correct general orbit-dimension statement

Here is the precise general result needed for S1 LF 36–38.

**Statement.** Let \(\dim H=n\), \(\dim K=N\), and assume

\[
\operatorname{span}_{\mathbb C}\{U_g:g\in G\}
=\operatorname{End}(H).
\]

For nonzero \(f\in K\otimes H\) of Schmidt rank \(r\), write

\[
f=\sum_{i=1}^r s_i e_i\otimes h_i,
\]

where \(s_i>0\), and both displayed vector families are orthonormal. Then

\[
\boxed{
\mathcal L=\operatorname{span}\{e_1,\ldots,e_r\}\otimes H,
\qquad
\dim\mathcal L=nr.
}
\]

**Proof.** Linearity and the spanning hypothesis give

\[
\mathcal L
=\{(I_K\otimes A)f:A\in\operatorname{End}(H)\}.
\]

Every vector on the right lies in \(E\otimes H\), where \(E=\operatorname{span}\{e_i\}_{i=1}^r\).

Conversely, take an arbitrary vector \(\sum_i e_i\otimes y_i\in E\otimes H\). Define

\[
A=\sum_{i=1}^r s_i^{-1}|y_i\rangle\langle h_i|.
\]

Because \(\langle h_i|h_j\rangle=\delta_{ij}\), this is a complex-linear operator satisfying \(Ah_i=s_i^{-1}y_i\). Hence

\[
(I_K\otimes A)f=\sum_{i=1}^r e_i\otimes y_i.
\]

Thus every vector of \(E\otimes H\) lies in \(\mathcal L\), proving equality and the dimension formula.

The rank-one operator construction explicitly handles the bra conjugation; it does not assume real coefficients. Equivalently, the kernel of \(A\mapsto(I\otimes A)f\) consists of operators annihilating \(\operatorname{span}\{h_i\}\), with dimension \(n(n-r)\), giving image dimension \(n^2-n(n-r)=nr\).

If \(U_g\) is irreducible on \(H\), its action on \(\mathcal L=E\otimes H\) is the orthogonal direct sum of \(r\) equivalent irreducible copies. Therefore, under these hypotheses,

\[
\dim\mathcal L=n
\quad\Longleftrightarrow\quad r=1,
\]

and the restricted action is irreducible exactly at that Schmidt-rank-one boundary.

This holds for arbitrary finite \(N\), with \(1\le r\le\min(N,n)\). The action on the entire \(K\otimes H\) has \(N\) copies; the cyclic orbit span has \(r\) copies.

**Scope qualification:** the formula was proved under the operator-spanning hypothesis. No formula for arbitrary non-spanning families is asserted, and spanning all of \(\operatorname{End}(H)\) is not claimed to be necessary for a particular individual vector to have a particular orbit dimension.

**Assessment: SUPPORTED for S1 LF 36–38.**

## 6. Proof impact and repair boundary

### 6.1 The displayed reduction fails

The source uses the asserted dimension and irreducibility to identify the restricted ancillary action with the original representation and conclude that the restricted channel has the same characteristics as \(\Phi\).

For the admissible Bell example, the spaces have different dimensions, the representations have different multiplicities, and the ancillary output has rank four while every output on \(H=\mathbb C^2\) has rank at most two. The stated equivalence cannot hold.

This is a **load-bearing proof obstruction**, not a harmless change in notation.

### 6.2 Replacing \(n\) by \(nr\) does not complete the proof

The corrected identification is with

\[
I_E\otimes U_g,\qquad \dim E=r,
\]

and consequently with the channel \(\operatorname{id}_E\otimes\Phi\), not with \(\Phi\) alone.

Representation decomposition does not make an arbitrary input block diagonal. In Schmidt form, the output contains all terms

\[
\sum_{i,j=1}^r
s_i s_j\,|e_i\rangle\langle e_j|
\otimes\Phi(|h_i\rangle\langle h_j|).
\]

The off-diagonal \(i\ne j\) terms remain. A majorization bound for individual pure outputs of \(\Phi\) does not, by the displayed representation argument, establish the required bound for this coherent block matrix.

For **\(r=1\)**, the original reduction does become valid:

\[
(\operatorname{id}\otimes\Phi)
(|e\otimes h\rangle\langle e\otimes h|)
=
|e\rangle\langle e|\otimes\Phi(|h\rangle\langle h|),
\]

so its spectrum is the single-use spectrum padded with zeros. That is a genuine product-input repair, but it does not prove the unrestricted ancillary proposition.

### 6.3 Downstream reliance is real, but falsity is not established

The opening proof of public Proposition 5 explicitly invokes Proposition 4 to bound the spectrum of \((\operatorname{id}\otimes\Omega)(|f\rangle\langle f|)\). Thus the defective ancillary argument lies on the manuscript’s stated tensorization proof chain.

The warranted conclusion is that this chain **cannot be accepted on the strength of the inspected argument**. It is not a counterexample to Proposition 5, its arbitrary-use iteration, or any capacity conclusion independently established elsewhere.

## 7. Claim-by-claim disposition

| Claim | Disposition |
|---|---|
| Proposition 4 permits arbitrary ancillary \(f\) | **SUPPORTED** |
| Its displayed proof asserts dimension \(n\) and irreducibility | **SUPPORTED** |
| The frozen Pauli/Bell example meets the relevant hypotheses | **SUPPORTED** |
| Its orbit span has dimension four and two irreducible copies | **SUPPORTED** |
| The source’s dimension/irreducibility assertions hold for that example | **REFUTED** |
| The selected channel obeys the actual Eq. (16) ordering | **SUPPORTED** |
| Its single-use reference is \((3/4,1/4)\) | **SUPPORTED** |
| The Bell output has spectrum \((5/8,1/8,1/8,1/8)\) | **SUPPORTED** |
| That spectrum is majorized by \((3/4,1/4,0,0)\) | **SUPPORTED** |
| The general orbit dimension is \(nr\) under the stated spanning hypothesis | **SUPPORTED** |
| Correcting the dimension alone repairs the unrestricted proof | **REFUTED** |
| Proposition 4’s inequality is false | **INCONCLUSIVE; not established by this work** |
| Proposition 5 or unrestricted product-output majorization is false | **INCONCLUSIVE; not established by this work** |
| The four-qubit original target is proved or refuted | **Not established** |
| The subscription journal text has the same defect | **INCONCLUSIVE; text identity not checked** |
| The observation is novel or resolves the 2026 literature tension | **INCONCLUSIVE** |

## 8. Findings, assurance ceiling, and verdict

### Candidate findings

**0 FATAL / 0 MAJOR / 0 MINOR findings against frozen S1.** No candidate correction is requested: its mathematical assertions and explicit limitations survive this written reconstruction.

### External source-proof classification

There is **one MAJOR source-proof obstruction**, located at **S2 LF 25–26**: linear independence of the \(U_g\) does not imply an \(n\)-dimensional irreducible ancillary cyclic span for arbitrary \(f\). The admissible Bell example gives dimension four, and the general reconstruction gives dimension \(nr\).

This classification concerns the **public proof as written**. It is not a theorem-level counterexample or a patch-introduced defect in S1.

### Assurance ceiling

This return supplies an independent written reconstruction of the frozen example and orbit-dimension formula. It supplies **no executed finite-check credit**, formal/kernel verification, human review, independent-model-family verification, journal-text comparison, exhaustive literature search, novelty clearance, or original-target acceptance. Parent independent review and disposition remain mandatory.

**Overall correctness:** correct.

**Explanation:** The candidate correctly identifies and demonstrates a false, load-bearing intermediate assertion in the accessible public Proposition 4 proof. The same admissible example satisfies the selected majorization inequality, so the justified disposition is a proof-step counterexample—not a refutation of the proposition, tensor-product conjecture, or four-qubit target.

**Confidence:** 0.99 for this exact written-review scope.