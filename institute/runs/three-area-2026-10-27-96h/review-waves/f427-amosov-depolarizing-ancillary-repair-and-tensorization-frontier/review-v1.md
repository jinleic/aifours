# Depolarizing ancillary repair and the remaining tensorization gap

**Status: GENERAL AUTHOR RESULT — independent review and parent disposition required.**

**Main results.** The ancillary majorization statement is proved below for a depolarizing channel in every dimension, with an arbitrary ancilla, throughout the full completely positive parameter interval. Separately, an exact four-dimensional operator construction shows that the facts cited in the final step of Amosov’s Proposition 5—its weight ordering and Eqs. (23)–(25)—do **not**, by themselves, imply the claimed product-reference majorization, even when the conjugations and consuming projector are genuine and shared. That construction is **not** an admissible two-channel counterexample: it violates a necessary conditional-output constraint. Consequently, neither Proposition 5 nor unrestricted tensor-product depolarizing majorization is proved or refuted here.

## 1. Inputs, actual reading, and method

The supplied frozen identity is:

- Manifest: `eb3bbd1cccbb1864138b9cb9422009c73114c3ba3fbf7f6925678cc981b57111`.
- Receipt: `21df5e902932c2f11108c1378d12bee6a42543d11d6be25dd64fc49e67e9bd43`.

These hashes, lengths, and the recorded clock are **parent-supplied metadata**, not child-native hash or clock observations.

Before reading the scientific packet, I read the complete manifest, receipt, seven named status/permission controls, dispatch receipt, and parent live-metadata supply. I then read the literal packet in order, lines 1–533, including the complete endings of S1–S4.

I subsequently opened the actual public manuscript [Amosov, arXiv:2103.08515v6](https://arxiv.org/html/2103.08515v6), reading the relevant definitions and hypotheses in §§5–6, the complete proofs of Propositions 4–5 and their stated iteration, and §7 Example 1. I also inspected its conclusion. For the literature-status distinction, I opened [Song–Wang–Tomamichel–Fang, arXiv:2609.37240v1, §1](https://arxiv.org/html/2609.37240v1#S1), where unrestricted exact depolarizing majorization is explicitly presented as a conjecture.

The derivations below were made **after** reading the packet, including the parent’s orbit obstruction and the assigned depolarizing hint. They are not blind reconstructions.

- No held scientific payload or its consumers were opened.
- No sibling research return or scientific program was read.
- No scientific executable, CAS, numerical experiment, build, test, or formatter was run.
- The new selected construction in §5 is written exact algebra under the GENERAL AUTHOR permission.
- No filesystem artifact was written under this read-only role. This is the complete materializable body for `author-candidate-v1.md`.
- No child-native completion clock or elapsed duration is asserted.

## 2. What the inspected source actually claims

In [§5, Eqs. (14)–(16)](https://arxiv.org/html/2103.08515v6#S5), the manuscript considers mixed-unitary channels

\[
\Phi(X)=\sum_{g\in G}\pi_gU_gXU_g^\dagger
\]

with an appropriate projective representation and normal Abelian subgroup \(T\). Its reference probabilities are the ordered coset sums

\[
p_j=\sum_{t\in T}\pi_{g_jt},
\]

and Eq. (16) requires

\[
j>k\quad\Longrightarrow\quad
\pi_{g_jt}\le \pi_{g_ks}
\qquad(s,t\in T).
\]

In [§6](https://arxiv.org/html/2103.08515v6#S6):

1. **Proposition 4** claims that a pure-input output-majorization bound by \(q\) persists after adjoining an identity-channel ancilla, with \(q\) padded by zeros.
2. **Proposition 5** claims the product-reference bound
   \[
   \lambda((\Phi\otimes\Omega)(|f\rangle\langle f|))
   \prec (p\otimes q)^\downarrow.
   \]
3. The proof of the main theorem explicitly iterates Proposition 5 to arbitrary tensor powers.

The subscription journal’s mathematical text was **not** compared with the accessible manuscript. Nothing below establishes their byte or mathematical identity.

## 3. The ancillary orbit claim is false, but that does not refute majorization

The manuscript’s Proposition 4 proof introduces

\[
L=\operatorname{span}\{(I\otimes U_g)f:g\in G\}
\]

and asserts that \(\dim L=d\) and the restricted representation is irreducible.

### Exact rederivation of the obstruction

Take two qubits, the projective Pauli representation

\[
I,\quad Z,\quad X,\quad XZ,
\]

and

\[
f=\frac{|00\rangle+|11\rangle}{\sqrt2}.
\]

Its orbit consists of

\[
\frac{|00\rangle+|11\rangle}{\sqrt2},\quad
\frac{|00\rangle-|11\rangle}{\sqrt2},\quad
\frac{|01\rangle+|10\rangle}{\sqrt2},\quad
\frac{|01\rangle-|10\rangle}{\sqrt2}.
\]

These are four orthonormal vectors. Thus \(\dim L=4\), not \(2\). The restricted action is two copies of the two-dimensional representation.

More generally, **when the matrices \(U_g\) span \(M_d\)**, write

\[
f=\sum_{i=1}^{r}s_i e_i\otimes h_i,\qquad s_i>0.
\]

The vectors \(Ah_i\), \(i=1,\ldots,r\), can be independently prescribed by choosing \(A\in M_d\). Hence

\[
L=\operatorname{span}\{e_1,\ldots,e_r\}\otimes\mathbb C^d,
\qquad
\dim L=rd.
\]

The claimed dimension and irreducibility hold only at Schmidt rank one under this spanning hypothesis.

### Explicit non-refutation

For the physical qubit depolarizing channel at \(p=1/2\), the Pauli weights are

\[
(5/8,1/8,1/8,1/8).
\]

Its single-qubit pure-output spectrum is \((3/4,1/4)\). The Bell input above gives ancillary-output spectrum

\[
(5/8,1/8,1/8,1/8)
\prec (3/4,1/4,0,0).
\]

Thus the selected example falsifies the **dimension/irreducibility step**, while satisfying the claimed spectral bound.

## 4. Complete repair for one depolarizing leg

### Theorem — arbitrary-dimensional depolarizing channel, arbitrary ancilla

Let \(d\ge2\),

\[
0\le p\le\frac{d^2}{d^2-1},
\qquad
\mathcal D_{p,d}(X)
=(1-p)X+\frac pd\operatorname{Tr}(X)I_d.
\]

Set

\[
t=1-p,\qquad b=\frac pd,\qquad \alpha=t+b,
\]

and let \(q_{p,d}\) be the decreasing rearrangement of

\[
(\alpha,\underbrace{b,\ldots,b}_{d-1}).
\]

For every finite-dimensional ancilla \(A\) and every density operator \(\rho_{AB}\), including mixed inputs,

\[
\boxed{
\lambda\!\left((\operatorname{id}_A\otimes\mathcal D_{p,d})
(\rho_{AB})\right)
\prec q_{p,d}\oplus0.
}
\]

The zeros pad the reference to the actual output dimension.

Equivalently, for every complex orthogonal rank-\(k\) projector \(P\), with \(\rho_A=\operatorname{Tr}_B\rho_{AB}\),

\[
\operatorname{Tr}\!\left[
P\left(t\rho_{AB}+b\rho_A\otimes I_d\right)
\right]
\le
\begin{cases}
t+kb,&t\ge0,\quad 1\le k<d,\\[2mm]
kb,&t<0,\quad 1\le k<d,\\[2mm]
1,&k\ge d.
\end{cases}
\]

These are exactly the prefixes of the correctly sorted reference.

### Proof

The channel identity gives

\[
R:=(\operatorname{id}_A\otimes\mathcal D_{p,d})(\rho_{AB})
=t\rho_{AB}+b\rho_A\otimes I_d.
\]

The normalized Choi operator of \(\mathcal D_{p,d}\) is

\[
t|\Omega_d\rangle\langle\Omega_d|
+\frac{p}{d^2}I_{d^2}.
\]

Its eigenvalues are

\[
1-p+\frac{p}{d^2},
\qquad
\frac{p}{d^2}\quad(d^2-1\text{ times}),
\]

so it is positive throughout the stated interval. Therefore \(R\ge0\), and \(\operatorname{Tr}R=1\).

Also,

\[
0\le \rho_A\le I_A,
\qquad
0\le \rho_A\otimes I_d\le I_{AB}.
\]

**Case \(t\ge0\).** For every rank-\(k\) projector,

\[
\operatorname{Tr}(PR)
=t\operatorname{Tr}(P\rho_{AB})
+b\operatorname{Tr}(P(\rho_A\otimes I_d))
\le t+bk.
\]

Here the sorted reference is

\[
q_{p,d}=(t+b,b,\ldots,b),
\]

whose first \(k<d\) entries sum to \(t+kb\).

**Case \(t<0\).** Since \(\rho_{AB}\ge0\),

\[
R\le b\rho_A\otimes I_d\le bI_{AB}.
\]

Consequently,

\[
\operatorname{Tr}(PR)\le bk.
\]

In this case \(t+b<b\), and the sorted reference is

\[
q_{p,d}=(\underbrace{b,\ldots,b}_{d-1},t+b).
\]

Its first \(k<d\) entries sum to \(kb\).

For either sign, when \(k\ge d\),

\[
\operatorname{Tr}(PR)\le\operatorname{Tr}R=1,
\]

which equals the corresponding padded-reference prefix. Maximizing over \(P\) proves the majorization statement. ∎

### Endpoints, ancillas, and sharpness

- At \(p=0\), the reference is \((1,0,\ldots,0)\).
- At \(p=1\), both formulas give the uniform reference on \(d\) entries.
- At \(p=d^2/(d^2-1)\), the sorted reference is
  \[
  \left(
  \underbrace{\frac{d}{d^2-1},\ldots,
  \frac{d}{d^2-1}}_{d-1},
  \frac1{d+1}
  \right).
  \]
  No endpoint limit or division by \(t\) is needed.
- Product pure inputs attain the reference, so all its prefix constants are sharp.
- The same finite-rank projector proof applies to trace-class density operators on an infinite-dimensional ancilla, with the usual zero-padded spectral interpretation.

This proof does not use the disputed orbit dimension, a representation decomposition, a selected eigenbasis, or a qubit-only transpose trick.

**Scope boundary:** this is a proof of the **depolarizing specialization**. General group-channel Proposition 4 is not adjudicated in this return.

## 5. Exact same-projector countermodel to the cited Proposition 5 implication

The final step of the inspected Proposition 5 proof says it combines the weight ordering with Eqs. (24) and (25). Equation (23) supplies the underlying twirl identity.

The following construction shows that those displayed facts are insufficient **even when all conjugated states come from one genuine Pauli orbit and the same projector consumes every term**.

### 5.1 State, marginal, and channel

Take \(H=K=\mathbb C^2\), in basis

\[
|00\rangle,\ |01\rangle,\ |10\rangle,\ |11\rangle.
\]

Define

\[
v=\frac{\sqrt3\,|01\rangle+|10\rangle}{2},
\]

\[
R=\frac23|00\rangle\langle00|+\frac13|v\rangle\langle v|,
\qquad
Q=|00\rangle\langle00|+|v\rangle\langle v|.
\]

Thus \(R\) is a density operator, \(Q\) is an actual orthogonal rank-two projector, and

\[
\lambda(R)=(2/3,1/3,0,0)
\prec q\oplus0,
\qquad q=(3/4,1/4).
\]

Its second-system marginal is exactly

\[
\sigma=\operatorname{Tr}_H R
=\operatorname{diag}(3/4,1/4).
\]

Let

\[
\Phi=\mathcal D_{1/2,2}
=\frac58\operatorname{Ad}_I+
\frac18\operatorname{Ad}_Z+
\frac18\operatorname{Ad}_X+
\frac18\operatorname{Ad}_{XZ}.
\]

With \(T=\{I,Z\}\), the ordered coset sums are

\[
p=(3/4,1/4),
\]

and Eq. (16) holds: every weight in the later coset is \(1/8\), no larger than either earlier-coset weight.

### 5.2 The displayed constraints hold

The exact Pauli twirl gives the source’s Eq. (23):

\[
\sum_{U\in\{I,Z,X,XZ\}}
(U\otimes I)R(U^\dagger\otimes I)
=2I_H\otimes\sigma.
\]

Therefore every unit vector \(h\) satisfies

\[
\sum_U
\langle h|(U\otimes I)R(U^\dagger\otimes I)|h\rangle
=2\langle h|I_H\otimes\sigma|h\rangle
\le\frac32<2.
\]

This satisfies Eq. (24), **and even its sharper bound using the actual marginal**.

Every conjugated state has the same spectrum as \(R\). Thus, for every rank-\(k\) projector \(P\),

\[
\operatorname{Tr}\!\left[
P(U\otimes I)R(U^\dagger\otimes I)
\right]
\le K_k(q\oplus0),
\]

which is Eq. (25), simultaneously for all \(P\), \(k\), and \(U\).

For the **same** consuming projector \(Q\), the entries can be displayed explicitly:

| Consuming vector | \(I\) | \(Z\) | \(X\) | \(XZ\) |
|---|---:|---:|---:|---:|
| \(|00\rangle\) | \(2/3\) | \(2/3\) | \(1/12\) | \(1/12\) |
| \(v\) | \(1/3\) | \(1/12\) | \(1/6\) | \(1/6\) |
| Sum over \(Q\) | \(1\) | \(3/4\) | \(1/4\) | \(1/4\) |

These are actual matrix elements of the displayed operators, not independently assigned or LP-relaxed weights.

### 5.3 The proposed product-reference conclusion fails

Put

\[
Y=(\Phi\otimes\operatorname{id})(R).
\]

The table gives

\[
\operatorname{Tr}(QY)
=\frac58+\frac18\left(\frac34+\frac14+\frac14\right)
=\frac{25}{32}.
\]

But

\[
(p\otimes q)^\downarrow
=\left(\frac9{16},\frac3{16},\frac3{16},\frac1{16}\right),
\qquad
K_2(p\otimes q)=\frac34=\frac{24}{32}.
\]

Hence

\[
\boxed{\operatorname{Tr}(QY)=\frac{25}{32}
>\frac34=K_2(p\otimes q).}
\]

For an additional exact spectral description,

\[
Y=\frac1{48}
\begin{pmatrix}
25&0&0&0\\
0&9&2\sqrt3&0\\
0&2\sqrt3&11&0\\
0&0&0&3
\end{pmatrix},
\]

with decreasing eigenvalues

\[
\frac{25}{48},\quad
\frac{10+\sqrt{13}}{48},\quad
\frac{10-\sqrt{13}}{48},\quad
\frac3{48}.
\]

Thus

\[
K_2(Y)=\frac{35+\sqrt{13}}{48}
>\frac{36}{48}=\frac34.
\]

This proves the following precise failed implication:

> Weight ordering (16), the exact twirl (23), row bounds (24), and all conjugated-state Ky Fan bounds (25) do not imply the product-reference bound, even with a genuine common unitary orbit, a genuine common projector, and a marginal already majorized by \(q\).

## 6. Why this is not a counterexample to Proposition 5

The state \(R\) above cannot be an intermediate state

\[
R=(\operatorname{id}\otimes\Omega)(|f\rangle\langle f|)
\]

for an \(\Omega\) satisfying the proposition’s stated pure-output bound by \(q=(3/4,1/4)\).

### Necessary conditional-output constraint

For any ancilla vector \(a\), define

\[
f_a=(\langle a|\otimes I)f,\qquad
C_a=(\langle a|\otimes I)R(|a\rangle\otimes I).
\]

An actual intermediate state necessarily satisfies

\[
C_a=\Omega(|f_a\rangle\langle f_a|).
\]

Writing \(w_a=\|f_a\|^2=\operatorname{Tr}C_a\), the pure-output hypothesis implies, whenever \(w_a>0\),

\[
\boxed{\lambda(C_a)\prec w_aq.}
\]

These conditional constraints are not consequences of merely knowing the global spectrum and the marginal spectrum.

In the construction,

\[
\operatorname{Tr}_K R
=\operatorname{diag}(11/12,1/12),
\]

whereas

\[
C_1=(\langle1|\otimes I)R(|1\rangle\otimes I)
=\frac1{12}|0\rangle\langle0|.
\]

Its largest eigenvalue is \(1/12\), while the necessary bound is

\[
\frac1{12}q_0=\frac1{16}.
\]

It violates the conditional-output constraint. Equivalently, any such \(\Omega\) would have to map a normalized pure conditional input to \(|0\rangle\langle0|\), contradicting its \(3/4\) maximum-eigenvalue bound.

For completeness, \(R\) can be generated using an **excluded** CPTP channel. Take

\[
f_{\rm bad}
=\sqrt{\frac{11}{12}}|00\rangle+
\sqrt{\frac1{12}}|11\rangle
\]

and Kraus operators

\[
A_0=\sqrt{\frac3{11}}|1\rangle\langle0|
+|0\rangle\langle1|,
\qquad
A_1=\sqrt{\frac8{11}}|0\rangle\langle0|.
\]

They satisfy \(\sum_iA_i^\dagger A_i=I\), and their channel produces \(R\) from \(f_{\rm bad}\). But it maps \(|1\rangle\langle1|\) to the pure state \(|0\rangle\langle0|\), and is not unital. It therefore fails both the chosen \(q\) bound and the mixed-unitary requirement.

**Consequently:** §5 is an exact countermodel to the **weakened proof implication**, not an admissible physical counterexample to the full two-channel proposition.

A repair must use additional structure from the actual \(\Omega\)—at least enough to exclude this construction. The conditional-output constraints above are necessary; no sufficiency theorem for them is claimed here.

## 7. Precise remaining original-target obligation

The one-leg theorem does not tensorize merely by replacing the identity ancilla with another noisy channel.

For example, for qubits, let

\[
R_m=(\operatorname{id}_2\otimes
\mathcal D_{p,2}^{\otimes m})(|f\rangle\langle f|),
\]

\[
\sigma_m=\mathcal D_{p,2}^{\otimes m}
(\operatorname{Tr}_{H_1}|f\rangle\langle f|).
\]

The next output is exactly

\[
(\mathcal D_{p,2}\otimes\operatorname{id})(R_m)
=(1-p)R_m+\frac p2I_2\otimes\sigma_m.
\]

To obtain unrestricted induction, one still needs, for every admissible \(f\), every rank \(k\), and the **same** projector \(Q\),

\[
\operatorname{Tr}\!\left[
Q\left((1-p)R_m+\frac p2I_2\otimes\sigma_m\right)
\right]
\le K_k(q_{p,2}^{\otimes(m+1)}).
\]

The construction in §5 shows why global and marginal majorization plus the displayed twirl estimates do not establish that joint inequality. It does not settle the inequality on the actual admissible family \(R_m\).

For a single depolarizing \(\Omega=\mathcal D_{r,\ell}\), the actual blocks retain substantially more information. If \(f=\sum_i|i\rangle\otimes f_i\), then

\[
(R_\Omega)_{ij}
=(1-r)|f_i\rangle\langle f_j|
+\frac r\ell\langle f_j|f_i\rangle I_\ell.
\]

Those coupled block identities must not be replaced by freely chosen eigenvalue or projector weights. No proof of the required unrestricted same-projector bound from this structure is supplied here.

## 8. Disposition by claim

| Claim | Result of this assignment |
|---|---|
| The ancillary orbit always has dimension \(d\) | **False**, with exact Bell-orbit rederivation. |
| That false dimension step refutes Proposition 4’s inequality | **No.** |
| Depolarizing ancillary majorization, every \(d\), every ancilla, full physical \(p\) interval | **Complete written proof above**, including mixed inputs and endpoints; independent review pending. |
| General group-channel Proposition 4 | **Not adjudicated here.** |
| The cited facts (16), (23)–(25) suffice for the product-reference conclusion | **False as a standalone implication**, by the exact common-orbit/common-projector construction. |
| The construction refutes full Proposition 5 | **No:** it violates a necessary admissibility constraint. |
| Proposition 5 or unrestricted all-\(n\) depolarizing majorization | **Neither proved nor refuted.** |
| Unrestricted four-qubit original target | **Not closed.** |
| Earlier scoped Class A/B results | Unchanged; no additional proof credit is claimed. |
| Novelty or priority | **Unresolved.** |

The newer paper’s [Eq. (2)](https://arxiv.org/html/2609.37240v1#S1) confirms that **that inspected paper** treats unrestricted exact majorization as conjectural. This does not establish worldwide status, invalidate the older statement, or certify novelty of either result here.

The mathematical adoption priorities are: independently check the complete one-leg proof and the exact operator countermodel; then require an actual admissibility-sensitive tensorization argument before importing the older unrestricted claim. Publication metadata or the false orbit step cannot substitute for that argument.

**Execution evidence:** none—no scientific code was run, so there are no program outputs, numerical tolerances, or finite-test results to report. All calculations displayed above are exact written algebra. No human, external-model-family, formal/kernel, journal-text-equivalence, or novelty assurance is claimed.

**Overall correctness:** **incorrect for the inspected proof chain as written**, not a verdict that its theorem is false.

**Explanation:** Its ancillary orbit assertion is false, and the final combination of the displayed tensorization estimates is insufficient even for exact common-projector Pauli-orbit data. The depolarizing ancillary specialization has a direct replacement proof, but unrestricted tensorization remains unestablished by this return.

**Confidence:** 0.99 in the explicit identities and scoped logical distinctions, subject to independent review and parent disposition.