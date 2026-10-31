# f363 author candidate — Constructive same-projector alignment on two-level and paired-repetition sectors

**Status: AUTHOR / UNREVIEWED.** This candidate proves a restricted-sector theorem beyond both supplied sufficient regions: the low-polarization pure-state convex hull and the all-density window around \(p=1\). It does **not** close unrestricted four-qubit \(k_3\).

The new ingredient is a constructive representation of the **actual channel output** as a convex combination of unitary conjugates of the product output. It controls one common complex projector without separately maximizing \(B,C_1,C_2\). A further block argument covers arbitrary complex densities on a four-dimensional paired-repetition subspace, not merely two-term GHZ states.

No scientific executable or numerical experiment was used. All calculations below are exact written calculations.

## 1. Exact theorem

Let
\[
\Phi_p(X)=(1-p)X+\frac p2\operatorname{Tr}(X)I,
\qquad \Lambda_p=\Phi_p^{\otimes4}.
\]
For physical \(0\le p\le4/3\), put
\[
t=|1-p|,\qquad a=\frac{1+t}{2},\qquad b=\frac{1-t}{2},
\]
and define the product-reference output
\[
D_t=\operatorname{diag}(a,b)^{\otimes4}.
\]
Its top-three sum is
\[
R_3(t)=a^4+2a^3b,\qquad
16R_3(t)=3+8t+6t^2-t^4.
\]

Define \(\mathcal C\) as the finite convex hull of these two classes. Local product bases and the physical-qubit pairing may differ between components of a convex decomposition.

- **Class A:** Pure states having at most two nonzero coefficients in some orthonormal product basis of the four physical qubits.
- **Class B:** Arbitrary complex density operators supported on a subspace locally unitarily equivalent, after a qubit permutation, to
  \[
  \mathcal S=\operatorname{span}\{|00\rangle,|11\rangle\}
  \otimes
  \operatorname{span}\{|00\rangle,|11\rangle\}.
  \]
  The logical two-qubit density inside this four-dimensional subspace is unrestricted.

### Theorem

For every \(\rho\in\mathcal C\), every physical \(p\), every \(k=1,\ldots,16\), and every complex orthogonal rank-\(k\) projector \(Q\),
\[
\boxed{\operatorname{Tr}\!\left(Q\Lambda_p(\rho)\right)\le K_k(D_t).}
\]
In particular,
\[
\boxed{K_3(\Lambda_p(\rho))\le R_3(t).}
\]

More constructively, for each such \(\rho,p\), there is a finite ensemble satisfying
\[
\boxed{\Lambda_p(\rho)=\sum_j w_jU_jD_tU_j^\dagger,\qquad
w_j\ge0,\quad\sum_jw_j=1.}
\]
The ensemble may depend on \(\rho,p\), but **does not depend on the consuming projector \(Q\)**. This is a state-dependent certificate, not a claim that one fixed postprocessing channel works for every input.

The all-\(k\) assertion is full output majorization **on \(\mathcal C\) only**. Unrestricted \(k_3\) and unrestricted full majorization remain open.

This class includes:

- arbitrary-phase four-qubit GHZ states with **every** population \(u\in[0,1]\);
- three-qubit GHZ states times a pure spectator;
- every complex X density in any product basis;
- every state separable across a \(2|2\) partition;
- arbitrary logical states, including states entangled across the two physical pairs, supported on the paired-repetition subspace.

## 2. Actual same-\(Q\) joint-layer inequality

Write a four-qubit density in Pauli weights as
\[
\rho=\frac1{16}(I+C_1+C_2+C_3+C_4).
\]
Set
\[
W=Y^{\otimes4},\qquad
\widetilde\rho=W\rho^TW,
\]
\[
\alpha=\frac{t^3(1+t)}2,\qquad
\beta=\frac{t^3(1-t)}2,\qquad
B=\alpha\rho-\beta\widetilde\rho.
\]
Spin flip multiplies weight \(w\) by \((-1)^w\). Comparing Pauli coefficients therefore gives, for arbitrary \(\rho\),
\[
\Lambda_{1-t}(\rho)
=
B+\frac{1-t^4}{16}I
+\frac{t-t^3}{16}C_1
+\frac{t^2-t^4}{16}C_2.
\]

The theorem proves the following **joint inequality at the same arbitrary complex rank-three \(Q\)**:
\[
\boxed{
16\operatorname{Tr}(QB)
+(t-t^3)\operatorname{Tr}(QC_1)
+(t^2-t^4)\operatorname{Tr}(QC_2)
\le 8t+6t^2+2t^4
}
\tag{J}
\]
for every \(\rho\in\mathcal C\) and \(0\le t\le1\).

Indeed, the identity contribution is \(3(1-t^4)\), and
\[
16R_3-3(1-t^4)=8t+6t^2+2t^4.
\]

The proof below controls the combined operator before optimizing \(Q\). It neither adds separately attained maxima nor assumes those maximizers coincide.

On the physical negative-Bloch branch, \(p=1+t\), the actual consuming projector is
\[
Q'=WQ^TW.
\]
Applying (J) to \(Q'\) gives the original observable bound on that branch.

The universal all-density version of (J) is **not** claimed. Neither is the stronger unproved f345 joint-slack condition adopted.

## 3. Common-projector and block-assembly facts

Suppose
\[
H=\sum_jw_jU_jDU_j^\dagger.
\]
For one fixed arbitrary complex rank-\(k\) projector \(Q\),
\[
\operatorname{Tr}(QH)
=\sum_jw_j\operatorname{Tr}(U_j^\dagger Q U_jD)
\le\sum_jw_jK_k(D)=K_k(D).
\]
To justify the inequality, diagonalize \(D\). The diagonal entries of a rank-\(k\) projector belong to \([0,1]\) and sum to \(k\), so their trace against \(D\) is at most the sum of its \(k\) largest eigenvalues.

No common maximizing projector across summands is assumed.

We also need a block-assembly fact. If \(D,H\) share a block decomposition and each \(H_j\) is a finite convex combination of unitary conjugates of \(D_j\), choose the block unitaries independently and take their direct sum. Products of the block probabilities give a finite ensemble of whole-space unitaries sending \(D\) to \(H\) in expectation. This remains valid for unequal block traces and zero blocks.

## 4. Proof for two-level inputs

### 4.1 Reduction and literal output

For positive Bloch parameter write
\[
\mathcal D_t=\Phi_{1-t}.
\]
Its elementary action is
\[
\mathcal D_t(|0\rangle\langle0|)=\operatorname{diag}(a,b),
\]
\[
\mathcal D_t(|1\rangle\langle1|)=\operatorname{diag}(b,a),
\qquad
\mathcal D_t(|0\rangle\langle1|)=t|0\rangle\langle1|.
\]

Local-unitary covariance follows directly from the channel definition. By local basis changes, bit flips and a permutation, a two-coefficient input reduces to an \(m\)-qubit cat times \(4-m\) pure spectators, where \(1\le m\le4\):
\[
|\psi\rangle
=\sqrt u\,|0^m\rangle
+e^{i\phi}\sqrt{1-u}\,|1^m\rangle.
\]
One-coefficient inputs are products.

On the active qubits pair every bitstring \(x\) with its complement \(\bar x\). Set
\[
d_x=a^{m-|x|}b^{|x|}.
\]
The product reference on that pair is
\[
\operatorname{diag}(d_x,d_{\bar x}).
\]

Every non-endpoint pair has actual output block
\[
\operatorname{diag}
\left(
ud_x+(1-u)d_{\bar x},
(1-u)d_x+ud_{\bar x}
\right).
\]
It is exactly \(u\) times the reference block plus \(1-u\) times its conjugate by the two-dimensional swap. There are no non-endpoint coherences.

On \(\{|0^m\rangle,|1^m\rangle\}\), the actual block is
\[
\begin{pmatrix}
ua^m+(1-u)b^m&
t^m\sqrt{u(1-u)}e^{-i\phi}\\
t^m\sqrt{u(1-u)}e^{i\phi}&
(1-u)a^m+ub^m
\end{pmatrix}.
\tag{1}
\]
These formulas follow from the displayed single-qubit action, not an erasure bound.

### 4.2 Endpoint alignment

Put
\[
\delta=a^m-b^m,\qquad z=2u-1.
\]
For \(0<t\le1\), \(\delta>0\). The endpoint eigenvalues are
\[
\frac{a^m+b^m}{2}\pm h,
\]
where
\[
4h^2=z^2\delta^2+(1-z^2)t^{2m}.
\tag{2}
\]

Since \(a=b+t\) and \(b\ge0\), the binomial expansion gives
\[
\delta=(b+t)^m-b^m\ge t^m.
\]
Consequently,
\[
\boxed{2h\le\delta.}
\tag{3}
\]

This is the load-bearing alignment inequality. The actual coherent block is no more polarized than the corresponding product-reference block, although its off-diagonal entry can be nonzero and its eigenbasis complex.

Let \(V_0\) diagonalize (1), placing the larger eigenvalue first, and set
\[
q_0=\frac12+\frac h\delta\in[1/2,1].
\]
Then (1) equals
\[
V_0\left[
q_0\operatorname{diag}(a^m,b^m)
+(1-q_0)X\operatorname{diag}(a^m,b^m)X
\right]V_0^\dagger.
\]

On every other complement pair set \(q_j=u\). Independently swap or do not swap each pair, with the corresponding probabilities, then apply \(V_0\) on the endpoint pair and the identity elsewhere.

This explicitly represents the actual output as a finite mixture of unitary conjugates of
\[
\operatorname{diag}(a,b)^{\otimes m}.
\]
At \(m=4\), there are at most \(2^8=256\) choices. Degenerate pair eigenvalues and zero weights cause no difficulty.

At \(t=0\), both actual and reference outputs equal \(I/2^m\); use the identity ensemble without dividing by \(\delta\). At \(t=1\), the construction remains valid, including zero reference eigenvalues.

Tensor the ensemble unitaries with the identity on the spectators. Their reference output is \(\operatorname{diag}(a,b)^{\otimes(4-m)}\), giving the full reference \(D_t\). Undoing local basis changes only conjugates the ensemble.

This proves Class A.

### 4.3 Directly checkable mixed-state membership

Every complex X density is a direct sum of positive \(2\times2\) blocks on complement pairs. Spectrally decompose each block: every resulting pure state has at most two coefficients. Their nonnegative trace weights yield a covered convex decomposition.

Another sufficient condition is row diagonal dominance in a product basis:
\[
\rho_{xx}\ge\sum_{y\ne x}|\rho_{xy}|.
\]
For each nonzero \(z=\rho_{xy}\), use the unnormalized vector
\[
|v_{xy}\rangle
=\sqrt{|z|}
\left(|x\rangle+e^{-i\arg z}|y\rangle\right).
\]
Its outer product supplies the off-diagonal entry \(z\) and diagonal contributions \(|z|\) at \(x,y\). The remaining diagonal entries are nonnegative by the stated condition. This gives an explicit decomposition into covered states.

Neither argument infers mixed-state membership from small marginal Bloch radii.

## 5. Proof for arbitrary paired-repetition densities

This extends the theorem beyond two-coefficient states. It uses literal blocks of the channel on the specified support, not an original four-qubit one-erasure Ky Fan premise.

### 5.1 Exact one-pair map

Let
\[
V|0\rangle=|00\rangle,\qquad V|1\rangle=|11\rangle.
\]
For a logical \(2\times2\) matrix \(X\), applying \(\mathcal D_t^{\otimes2}\) to \(VXV^\dagger\) produces no matrix elements between
\[
E=\operatorname{span}\{|00\rangle,|11\rangle\},
\qquad
O=\operatorname{span}\{|01\rangle,|10\rangle\}.
\]

Set
\[
h=a^2+b^2=\frac{1+t^2}{2},\qquad
\ell=ab=\frac{1-t^2}{4},
\qquad
\gamma=\frac th=\frac{2t}{1+t^2}.
\]
Then \(h>0\), \(0\le\gamma\le1\), and \(h+2\ell=1\).

Define the logical dephasing channel
\[
\mathcal Z_t(X)=\frac{1+t}{2}X+\frac{1-t}{2}ZXZ,
\]
and
\[
F=\mathcal Z_t\circ\mathcal D_\gamma.
\]
The exact physical output is the direct sum
\[
E:\quad hF(X),
\qquad
O:\quad \ell\operatorname{Tr}(X)I_2.
\tag{4}
\]

Entrywise, its \(E\) block is
\[
\begin{pmatrix}
a^2X_{00}+b^2X_{11}&t^2X_{01}\\
t^2X_{10}&b^2X_{00}+a^2X_{11}
\end{pmatrix}.
\]
The identities
\[
h\gamma=t,\qquad ht\gamma=t^2
\]
verify all entries. Each odd diagonal is \(\ell\operatorname{Tr}(X)\). Thus (4) is an exact identity, not a spectral estimate.

### 5.2 Logical comparisons derived here

Define
\[
d=\operatorname{diag}(a^2/h,b^2/h)
=\operatorname{diag}\left(\frac{1+\gamma}{2},\frac{1-\gamma}{2}\right).
\]

For any logical one-qubit density \(\eta\), \(\mathcal D_\gamma(\eta)\) lies in the convex hull of unitary conjugates of \(d\): diagonalize \(\eta\), use covariance on each pure component, and average. Applying \(\mathcal Z_t\), explicitly a mixture of two unitary conjugations, preserves this conclusion. Hence
\[
F(\eta)\in\operatorname{conv}\{UdU^\dagger\}.
\tag{5}
\]

For a complex pure logical two-qubit state \(\omega\), the Schmidt decomposition supplies logical local unitaries carrying it to
\[
\sqrt u\,|00\rangle+\sqrt{1-u}\,|11\rangle.
\]
Covariance and the \(m=2\) result already proved show that
\[
\mathcal D_\gamma^{\otimes2}(\omega)
\in\operatorname{conv}\{U(d\otimes d)U^\dagger\}.
\]
Spectrally decompose mixed \(\omega\) and average. Finally apply \(\mathcal Z_t^{\otimes2}\), an explicit four-term random-unitary mixture. Thus, for **every** logical two-qubit density,
\[
(F\otimes F)(\omega)
\in\operatorname{conv}\{U(d\otimes d)U^\dagger\}.
\tag{6}
\]

No four-qubit target theorem is assumed here. The needed two-qubit assertion was derived from the two-level block calculation and the Schmidt decomposition.

### 5.3 Four physical blocks

Encode an arbitrary logical density:
\[
\rho=(V\otimes V)\omega(V\otimes V)^\dagger.
\]
Let \(\omega_A,\omega_B\) be its logical marginals. Tensoring the exact map (4) gives
\[
\begin{array}{c|c}
\text{block}&\text{actual output}\\ \hline
EE&h^2(F\otimes F)(\omega)\\
EO&h\ell F(\omega_A)\otimes I_2\\
OE&h\ell I_2\otimes F(\omega_B)\\
OO&\ell^2I_4
\end{array}
\tag{7}
\]
with trace factors
\[
h^2,\quad2h\ell,\quad2h\ell,\quad4\ell^2,
\]
which sum to one.

The product reference \(D_t\) has corresponding blocks
\[
\begin{array}{c|c}
EE&h^2d\otimes d\\
EO&h\ell d\otimes I_2\\
OE&h\ell I_2\otimes d\\
OO&\ell^2I_4.
\end{array}
\tag{8}
\]

Equations (5)–(6) give a finite random-unitary representation from each reference block to the actual block; \(OO\) is unchanged. The block-assembly fact yields a finite random-unitary representation on all sixteen dimensions.

This proves Class B, including arbitrary logical correlations and mixed states. Local covariance and physical-qubit permutation invariance give the stated transformed versions. Averaging the representations proves the theorem on \(\mathcal C\).

In particular, a state separable across a \(2|2\) partition is covered: decompose into products of two-qubit pure states and Schmidt-decompose each physical pair. Each resulting component is locally supported on the specified paired subspace.

## 6. Physical range, reflection and complex projectors

For \(q=1-p\), the one-qubit channel has Pauli-mixture probabilities
\[
\frac{1+3q}{4}\quad\text{for }I,
\qquad
\frac{1-q}{4}\quad\text{for each of }X,Y,Z.
\]
These are nonnegative precisely for
\[
-\frac13\le q\le1,
\qquad\text{equivalently}\qquad
0\le p\le\frac43.
\]

The full-transpose spin flip \(S(A)=WA^TW\) changes weight \(w\) by \((-1)^w\), hence
\[
\Lambda_{1+t}(\rho)=S(\Lambda_{1-t}(\rho)).
\]
This is full transposition, not partial transposition.

For any complex orthogonal rank-\(k\) projector \(Q\),
\[
Q'=WQ^TW
\]
is another such projector. Since \(W^T=W\),
\[
\operatorname{Tr}(QS(A))=\operatorname{Tr}(Q'A).
\]
Therefore the actual observable bound transports to the physical negative branch \(0\le t\le1/3\).

The constructive statement itself transports because \(D_t\) is real diagonal:
\[
S(UD_tU^\dagger)
=(W\overline U)D_t(W\overline U)^\dagger.
\]
The endpoint \(t=0\) and physical endpoint \(t=1\) were included without division by a vanishing quantity.

## 7. Exact high-polarization example with actual maximizing complex \(Q\)

This is a fresh **written exact calculation**, not numerical evidence.

Choose
\[
|\psi\rangle=\frac{3|0000\rangle+i|1111\rangle}{\sqrt{10}},
\qquad \rho=|\psi\rangle\langle\psi|,
\qquad p=\frac12.
\]
Normalization makes \(\rho\) a positive rank-one density. Its two coefficients give Schmidt rank two across every nontrivial bipartition.

All local radii equal \(4/5\), so
\[
s=\frac{64}{25}>\frac14,\qquad
L=\frac{32}{5},\qquad
\tau=\frac9{25},
\]
\[
c=\sqrt{234},\qquad
\kappa=\frac{226}{25}-\sqrt{234}<0.
\]
Indeed \(\sqrt{234}>15>226/25\).

Thus this state lies outside both the advertised low-polarization sector and the more general \(\kappa\ge0\) certificate. As a pure state, it cannot be a mixture of distinct low-sector pure states. Also \(p=1/2\) is outside \([141/142,143/142]\).

Here
\[
t=\frac12,\quad a=\frac34,\quad b=\frac14.
\]
The Pauli probabilities are \(5/8,1/8,1/8,1/8\), explicitly verifying complete positivity.

The actual output has only one non-diagonal block, on \(\{|0000\rangle,|1111\rangle\}\):
\[
\begin{pmatrix}
73/256&-3i/160\\
3i/160&9/256
\end{pmatrix}.
\tag{9}
\]
All other entries are diagonal:
\[
\begin{array}{c|c|c}
\text{Hamming weight}&\text{value}&\text{multiplicity}\\ \hline
1&123/1280&4\\
2&9/256&6\\
3&27/1280&4.
\end{array}
\]
This specifies the entire output.

Let \(v=\sqrt{409}\). The endpoint eigenvalues are
\[
x_\pm=\frac{41}{256}\pm\frac v{160}.
\]
Since \(20<v<21\),
\[
x_+>\frac{123}{1280},
\qquad
x_-<\frac9{256}<\frac{123}{1280}.
\]
Consequently,
\[
\boxed{
K_3=\frac{451+8\sqrt{409}}{1280},
\qquad R_3=\frac{675}{1280},
\qquad
R_3-K_3=\frac{28-\sqrt{409}}{160}>0.
}
\]

An actual maximizing complex rank-three projector is
\[
Q=|\chi\rangle\langle\chi|
+|0001\rangle\langle0001|
+|0010\rangle\langle0010|,
\]
where
\[
|\chi\rangle
=
\sqrt{\frac{v+20}{2v}}\,|0000\rangle
+i\sqrt{\frac{v-20}{2v}}\,|1111\rangle.
\]
These vectors are normalized and orthogonal; multiplying (9) by \(\chi\) gives \(x_+\chi\).

### Alignment at this same \(Q\)

Here
\[
C_1=\frac45\sum_iZ_i,\qquad
C_2=\sum_{i<j}Z_iZ_j.
\]
The only nonzero block of \(B\) is
\[
\begin{pmatrix}
13/160&-3i/160\\
3i/160&-3/160
\end{pmatrix}.
\]
Direct calculation gives
\[
\operatorname{Tr}(QB)=\frac{5+169/v}{160},
\]
\[
\operatorname{Tr}(QC_1)=\frac{16}{5}+\frac{64}{v},
\qquad
\operatorname{Tr}(QC_2)=6.
\]

At \(t=1/2\), the left side of (J) is
\[
\frac{113}{40}+\frac v{10},
\]
and its right side is \(45/8\). Its exact joint slack is
\[
\frac{28-v}{10}=16(R_3-K_3)>0.
\]

This \(Q\) does **not** maximize the layers separately:
\[
K_3(B)=\frac{5+\sqrt{73}}{160}>\operatorname{Tr}(QB),
\]
\[
K_3(C_1)=\frac{32}{5}>\operatorname{Tr}(QC_1),
\qquad
K_3(C_2)=12>6.
\]
The first strict inequality follows from \(73\cdot409>169^2\); the second from \(v>20\). There is no hidden coincidence of separate maximizers.

## 8. Exact four-coefficient example showing a strict enlargement

Let
\[
|\phi\rangle=\frac{3|00\rangle+i|11\rangle}{\sqrt{10}},
\qquad
|\psi\rangle=|\phi\rangle_{12}\otimes|\phi\rangle_{34},
\qquad p=\frac12.
\]
This normalized pure state belongs to Class B.

Across the cut \(13|24\), its four nonzero Schmidt coefficients are
\[
\frac9{10},\quad\frac3{10},\quad\frac3{10},\quad\frac1{10}.
\]
Every two-coefficient product-basis state has Schmidt rank at most two across every cut, even after local basis changes. Hence this state is not in Class A. Purity also rules out a mixture of different Class-A pure states.

Its local radii are again \(4/5\), so it is outside the old low-polarization pure sector.

The actual single-pair output has even block
\[
\begin{pmatrix}
41/80&-3i/40\\
3i/40&9/80
\end{pmatrix},
\]
and odd diagonal values \(3/16,3/16\). Its even eigenvalues are
\[
L_\pm=\frac{25\pm2\sqrt{73}}{80}.
\]
Writing \(\ell=3/16\), one has
\[
L_+>\ell>L_-\ge0.
\]
The actual four-qubit output is exactly the tensor square of this specified pair output. Its three leading eigenvalues are therefore \(L_+^2\) and two copies of \(L_+\ell\). Thus
\[
\boxed{
K_3=\frac{1667+160\sqrt{73}}{6400},
\qquad
R_3-K_3=\frac{427-40\sqrt{73}}{1600}>0.
}
\]
Positivity follows already from \(\sqrt{73}<9\).

An actual maximizing projector is obtained by putting \(w=\sqrt{73}\) and
\[
|\zeta\rangle
=
\sqrt{\frac{w+8}{2w}}\,|00\rangle
+i\sqrt{\frac{w-8}{2w}}\,|11\rangle,
\]
then projecting onto the three orthonormal vectors
\[
\zeta\otimes\zeta,\qquad
\zeta\otimes|01\rangle,\qquad
|01\rangle\otimes\zeta.
\]
Their eigenvalues are respectively \(L_+^2,L_+\ell,L_+\ell\).

Thus the paired-sector extension is nonredundant, with a fully specified actual state, parameter, output and maximizing complex projector.

## 9. Exact advance and remaining gap

**Established by the written derivation:**

1. A constructive unitary-orbit certificate for all two-level inputs and their convex mixtures.
2. A strict enlargement to arbitrary complex densities on paired-repetition support.
3. The full physical parameter range and all complex projectors.
4. The actual same-\(Q\) joint inequality (J) for \(B,C_1,C_2\) on this class.
5. All Ky Fan inequalities on this restricted class.
6. Two exact high-polarization checks with complete outputs and maximizing complex projectors.

**Not established:**

- unrestricted complex-density \(k_3\);
- the f345 joint-slack inequality for arbitrary states;
- unrestricted all-index majorization;
- coverage of arbitrary pure states with three or more coefficients outside the paired support;
- membership in \(\mathcal C\) from local marginal radii alone;
- any physical counterexample;
- novelty, public priority, independent-model-family, human or formal/kernel assurance.

This is scoped progress on the **actual original channel and common-projector target**, not closure by a surrogate. The global high-polarization alignment obligation remains unpaid outside the proved class.

## 10. Methods, read chronology and provenance

**Actual runtime model:** `anthropic/claude-fable-5-1`, as supplied by the session. This was a same-harness GENERAL AUTHOR duty, not independent-family review or original-owner provider recovery.

I read the required memory summary and written-disposition skill first. Its historical written-only restrictions were not substituted for this manifest’s expressly restored GENERAL AUTHOR permissions.

Before mathematical derivation, I read:

- the complete manifest and freeze receipt;
- all six named status/permission controls;
- the entire literal packet in ascending raw windows: 1–250, 251–500, 501–750, 751–1000, and 1001–1100, with the last ending at actual packet line 1067.

This included S1 lines 1–38, S2 logical lines 1–387, S3 logical lines 1–623, and S4 lines 1–17 through their endings. No linked held scientific payload or method/selection/proof/confidence consumer was opened.

Derivation followed those complete reads. A substantive written checkpoint was retained at `local://f363-substantive-checkpoint-v1.md` after the two-level proof and first exact case. The paired-sector extension and second exact case followed that checkpoint.

The subsequently read parent metadata supplies **parent-observed**, not child-executed, live pins:
  
| Artifact | SHA-256 | Bytes / LF |
|---|---|---:|
| Manifest | `3032407ff31379bc796daacf6a6555ae707b2350f88819a46601b977a903278b` | 6363 / 106 |
| Receipt | `9cb897d18be64ca2400b22f7036974c07b767d25ee55ce8e25435606278be1ba` | 2888 / 73 |
| Packet | `f9cbc70cb240cacf1f4e106fbec4291a3db7ce11c720078c143b5642cbed5751` | 54924 / 1067 |
| S1 | `b8587c7aef665460e042c3f87295e0fc9062c201ab2d43150d89faa1259073c1` | 6241 / 38 |
| S2 | `22851a57a04a9ff9f7ea44b13ec3fd8677af03f92f3a3ca62da5de049d3d89cc` | 14219 / 386 |
| S3 | `c9dd72a303f27161cc838c82a58a6a433d702bf932e147c3d5f2d81082c1d4b7` | 22387 / 622 |
| S4 | `bb16e861cedad17fc2a9eb9520dba4cb7bdbd69ad3cd510df2e7bd59060f8b54` | 4873 / 17 |

S2 and S3 respectively have 387 and 623 logical lines because their final lines are unterminated. Parent metadata also reports that all six control pins matched.

The parent’s supplied clock was **2026-10-30T09:21:00-0700 PDT**. After the complete local candidate was written, Main supplied a fresh parent-native observation, **2026-10-30T09:30:30-0700 PDT**. Neither is relabeled as my native start, private derivation time or exact completion time. No continuous-supervision claim is made.

Scientific methods were exact written algebra, constructive finite-dimensional unitary mixtures and the two fully displayed exact examples. No interpreter, CAS, solver, numerical experiment, build, lint, formatter, external-model CLI, installation, remote campaign or public-source lookup was run. Consequently there is no executed scientific source code or stdout to report. The entrywise matrices and ensemble construction above supply reproducibility.

Named mathematical imports are finite-dimensional Hermitian spectral decomposition, the Schmidt decomposition, Pauli transpose identities and elementary binomial/tensor algebra. The variational, block-assembly, unitary-mixture and logical two-qubit comparisons were derived explicitly. There are no external citations or unproved load-bearing scientific imports.

No source snapshot was edited. Only permitted local scratch artifacts were written:

- `local://f363-author-candidate-v1.md`
- `local://f363-substantive-checkpoint-v1.md`
- `local://f363-parent-clock-addendum-v1.md`

The complete scientific body is returned above for parent materialization without a working-tree-write bypass.

**Final status: UNREVIEWED restricted-sector proof with a constructive same-\(Q\) certificate; unrestricted four-qubit complex-density \(k_3\) remains OPEN.**