# F464 — Complete written review of the arbitrary three-qubit spin-flip proof

**Proposed destination:** `f464-arbitrary-three-qubit-spinflip-paired-projection-proof-review/review-v1.md`

**Status:** Completed WRITTEN review; returned in full for parent materialization. No repository file was written. This is a reviewer’s scoped reconstruction, **not parent adoption, novelty certification, independent-family acceptance, or formal/kernel verification**.

## 1. Assignment, provenance, and complete coverage

The reviewed assignment is the frozen F464 manifest:

- Manifest SHA256: `e16d088715850a2250fef237c0b883f47b7953c52073530b6e0c6990d18abf7c`.
- Freeze-receipt SHA256: `256f60e56c5dafae93e9cd27416512d2fea06da0413d87f156a0d38b8f8f6677`.
- Literal-packet SHA256: `e917b233ca7faec0c65f316b5a78fdb916436ff788167c21e5c890f77f746a89`.

These hashes, byte/LF counts, and the observation `2026-10-30T11:57:24-0700 PDT` are **parent-attributed metadata** from the supplied records. I did not execute hashing or obtain a child-native clock. The parent’s observation is not represented as my native start time.

Before opening mathematical bodies, I read:

1. The complete 107-line manifest.
2. The complete 47-line freeze receipt.
3. All ten listed permission/status controls, through their endings.
4. The parent dispatch receipt.
5. The complete parent live-metadata supply.

I then sent the required **direct administrative pre-body ACK** to Main. Only afterward did I read the literal mathematical packet.

The packet was read completely, in order, using exact raw windows of at most 20 lines: `1–20`, `21–40`, continuing consecutively through `801–820`, then `821–826`. Both source endings were displayed. No elision was encountered.

### Scientific source coverage

| Source | Complete body read | Use in this review |
|---|---:|---|
| **S1:** F463 `review-v1.md`, SHA256 `3e2cab0b74bc61af6179c442d0098a56d1f209e8dc7f39b6dd601cf1b0025907` | Logical lines **1–783**, including the ending; parent reports 782 LF characters | Current author proof candidate, reconstructed below |
| **S2:** parity/spectator parent disposition, SHA256 `c4c9a989cbb3b13f5bde657224666035588f73842b02249202e3d5b242f4b5e9` | Lines **1–41**, including the ending | Previously adopted **parity-sector-only** scope and historical comparison; not an arbitrary-three-qubit proof premise |

The difference between S1’s reported LF-character count and its 783 logical lines is retained as supplied metadata, not silently normalized.

The quarantine controls were used **only for status and exclusions**. No linked held payload, prior reviewer return, sibling result, author program, or additional source was opened. In particular, the F439/F444/F448 episodes and all genuine held-episode consumers remained NONINPUT.

All mathematics below is written reconstruction using formal parameters or the author’s expressly supplied state, parameter, and projector. No additional selected diagnostic instance was introduced.

## 2. Findings and per-claim disposition

**Mathematical findings: 0 FATAL / 0 MAJOR / 0 MINOR.**

Here **SUPPORTED** means that the stated derivation was reconstructed at its specified written scope. It does not mean that the reviewer grants adoption or any stronger acceptance category.

| Claim | Disposition | Source scope |
|---|---|---|
| Actual lifted marginal sums, traces, and spin-flip inclusion–exclusion identity | **SUPPORTED** | S1:114–214 |
| Complete paired eigenbasis and convex decomposition into complementary rank-four projections, including endpoint and half-eigenvalue degeneracies | **SUPPORTED** | S1:231–300 |
| Antiunitary trace argument, compression spectrum, and all-prefix \(H_2\) majorant | **SUPPORTED** | S1:302–356 |
| \(H_1\) mixed-unitary majorant | **SUPPORTED** | S1:360–395 |
| All eight output prefixes for arbitrary complex three-qubit densities | **SUPPORTED** | S1:399–498 |
| Full physical interval and consuming-projector transport for the negative branch | **SUPPORTED** | S1:502–549 |
| Supplied state’s exclusion from every local-parity sector and its convex hull | **SUPPORTED** | S1:553–607 |
| Supplied exact physical-channel expectation | **SUPPORTED as written exact arithmetic**, not an executed finite check | S1:609–651 |
| All sixteen prefixes for the full four-qubit \(1|3\)-separable hull | **SUPPORTED** | S1:655–726 |
| Public-literature summaries and historical process assertions | **Not independently adjudicated**; no additional source/history audit performed | S1:53–90, 747–758 |
| Unrestricted four-qubit theorem, general blocklength/dimension, arbitrary ancillary tensorization, novelty/priority | **Not established by this review** | S1:772–783 |

The load-bearing argument and every downstream mathematical consumer are reconstructed next.

## 3. Actual marginal sums and the spin-flip coupling

Write \(\rho_S\) for the partial trace onto the indicated physical factors. The author’s operators are

\[
H_1=
\rho_A\otimes I_B\otimes I_C+
I_A\otimes\rho_B\otimes I_C+
I_A\otimes I_B\otimes\rho_C
\]

and

\[
H_2=
\rho_{AB}\otimes I_C+
\rho_{AC}\otimes I_B+
I_A\otimes\rho_{BC},
\]

where the \(AC\) term is embedded on the actual \(A,C\) factors, rather than reinterpreted as an adjacent-factor operator.

Each lifted one-body term has trace four, and each lifted two-body term has trace two. Thus

\[
H_1,H_2\ge0,\qquad
\operatorname{Tr}H_1=12,\qquad
\operatorname{Tr}H_2=6.
\]

For \(Y\) the Pauli matrix and \(\mathcal K\) computational-basis conjugation, set

\[
\Theta=Y^{\otimes3}\mathcal K.
\]

Since \(\overline Y=-Y\) and \(Y^2=I\),

\[
\Theta^2=-I.
\]

For Hermitian \(X\), the antiunitary conjugate is

\[
\widetilde X=\Theta X\Theta^{-1}
=Y^{\otimes3}X^T Y^{\otimes3}.
\]

The one-qubit linear identity

\[
YX^TY=\operatorname{Tr}(X)I-X
\]

can be tensored and expanded. For a normalized three-qubit density it gives exactly

\[
\widetilde\rho=I-H_1+H_2-\rho.
\]

This is an identity for the actual complete density, including complex cross-parity coherences. No pinching, spectral surrogate, partial transpose, or local-basis normal form is involved.

For a pure normalized input \(\rho=|\psi\rangle\langle\psi|\), antiunitarity and \(\Theta^2=-I\) imply

\[
\langle\Theta\psi,\psi\rangle=0.
\]

Consequently

\[
P=\rho+\widetilde\rho
\]

is an orthogonal rank-two projection. Conjugating twice acts trivially on operators, so \(\widetilde P=P\).

Rearranging inclusion–exclusion gives

\[
H_2=P+H_1-I.
\]

Each one-qubit density is transformed to its complementary density, while identity factors stay identities. Hence

\[
\widetilde H_1=3I-H_1.
\]

Conjugating the preceding expression for \(H_2\) and adding produces

\[
\boxed{H_2+\widetilde H_2=I+2P.}
\]

Both summands are positive: \(H_2\) by its physical marginal construction, and \(\widetilde H_2\) by full antiunitary conjugation. This proves the precise coupling used subsequently.

## 4. Independent reconstruction of the paired-projection lemma

### 4.1 Normalization is valid without commutativity

Let

\[
G=I+2P,\qquad
Z=G^{-1/2}H_2G^{-1/2}.
\]

The spectrum of \(G\) is three on \(\operatorname{ran}P\) and one on its orthogonal complement. Thus \(G\) is invertible, and its real functional calculus is invariant under \(\Theta\).

Applying that invariance to the exact coupling yields

\[
Z+\widetilde Z=I.
\]

Both terms are positive, so \(0\le Z\le I\). This step uses congruence by \(G^{-1/2}\), **not** an assumption that \(H_2\) commutes with \(G\).

### 4.2 Complete paired eigenbasis, including all degeneracies

If \(Zu=\lambda u\), then

\[
Z\Theta u=(1-\lambda)\Theta u.
\]

For an eigenvalue different from \(1/2\), \(\Theta\) therefore maps its eigenspace antiunitarily and bijectively onto the complementary eigenspace. Choosing an orthonormal basis in one eigenspace and applying \(\Theta\) gives an orthonormal basis in the other. Distinct eigenspaces of the Hermitian \(Z\) are orthogonal.

This covers eigenvalues zero and one as well: they are paired directly, and no inverse eigenvalue or eigenvalue-gap division is used.

The \(1/2\)-eigenspace is \(\Theta\)-invariant. Within it, any abstract unit vector \(u\) is orthogonal to \(\Theta u\). The orthogonal complement of their span inside that eigenspace is again \(\Theta\)-invariant: antiunitarity preserves orthogonality to both members of the pair, using \(\Theta^2=-I\). Repeating this construction exhausts the eigenspace in orthonormal pairs. Its dimension is therefore even.

Accordingly the entire eight-dimensional space has an orthonormal eigenbasis

\[
u_1,\Theta u_1,\ldots,u_4,\Theta u_4,
\]

and

\[
Z=\sum_{i=1}^{4}
\left[
\lambda_i|u_i\rangle\langle u_i|
+(1-\lambda_i)|\Theta u_i\rangle\langle\Theta u_i|
\right],
\qquad 0\le\lambda_i\le1.
\]

This establishes completeness, including arbitrary multiplicities and the half-eigenvalue case; it is not merely a nondegenerate-eigenvalue argument.

### 4.3 The sixteen weights give the actual effect

For each binary string \(s\in\{0,1\}^4\), let \(\Pi_s\) select \(u_i\) when \(s_i=0\), and \(\Theta u_i\) when \(s_i=1\).

Each \(\Pi_s\) is an orthogonal rank-four projection. Conjugation exchanges the two selected rays in each pair; the minus sign in \(\Theta(\Theta u_i)=-u_i\) does not change a ray projection. Therefore

\[
\widetilde\Pi_s=I-\Pi_s.
\]

Give it weight

\[
w_s=\prod_{i=1}^4
\begin{cases}
\lambda_i,&s_i=0,\\
1-\lambda_i,&s_i=1.
\end{cases}
\]

There are sixteen nonnegative weights, and

\[
\sum_s w_s=\prod_i[\lambda_i+(1-\lambda_i)]=1.
\]

The coefficient of \(|u_i\rangle\langle u_i|\) in their weighted projection sum is \(\lambda_i\); the coefficient of its paired ray is \(1-\lambda_i\). Hence

\[
Z=\sum_s w_s\Pi_s,\qquad
H_2=\sum_s w_sX_s,\qquad
X_s=G^{1/2}\Pi_sG^{1/2}.
\]

Zero weights at endpoint eigenvalues cause no difficulty. These are projections constructed from the **actual \(Z\)**, not independently chosen spectral shadows.

### 4.4 Antiunitary trace conjugation is handled correctly

Set \(r=\operatorname{Tr}(P\Pi_s)\). The trace is real because \(P,\Pi_s\) are Hermitian and cyclicity gives

\[
\overline{\operatorname{Tr}(P\Pi_s)}
=\operatorname{Tr}(\Pi_sP)
=\operatorname{Tr}(P\Pi_s).
\]

Antiunitary conjugation conjugates the trace and preserves products. Using the invariances established above,

\[
\overline r
=\operatorname{Tr}\!\left(\widetilde P\,\widetilde\Pi_s\right)
=\operatorname{Tr}\!\left(P(I-\Pi_s)\right)
=2-r.
\]

Thus \(r=1\).

This does not assume \(P\Pi_s=\Pi_sP\), nor does it incorrectly treat antiunitary conjugation as complex-linear.

### 4.5 Compression and the actual nonzero spectrum

On \(V_s=\operatorname{ran}\Pi_s\), the compression

\[
C_s=\Pi_sP\Pi_s\big|_{V_s}
\]

is positive, has rank at most two, and has trace one. Its four eigenvalues can therefore be written

\[
\eta,\ 1-\eta,\ 0,\ 0,\qquad 0\le\eta\le1.
\]

The statement includes rank-one compression through a zero member of the displayed pair.

To identify the spectrum of \(X_s\), use the map

\[
A_s:V_s\longrightarrow\mathbb C^8,\qquad
A_sv=G^{1/2}v.
\]

Then

\[
A_sA_s^\dagger=X_s,\qquad
A_s^\dagger A_s
=\Pi_sG\Pi_s\big|_{V_s}
=I_{V_s}+2C_s.
\]

The nonzero spectra of these two products coincide. Since \(G^{1/2}\) is invertible, \(A_s\) has rank four. The complete spectrum of \(X_s\) is therefore

\[
1+2\eta,\quad 3-2\eta,\quad 1,\quad 1,\quad 0,\quad0,\quad0,\quad0,
\]

up to decreasing rearrangement.

The first two displayed entries are both at least one and at most three. Their sum is four. Consequently the eight ordered prefixes satisfy

\[
K_1(X_s)\le3,\qquad
K_2(X_s)=4,\qquad
K_3(X_s)=5,\qquad
K_k(X_s)=6\quad(4\le k\le8).
\]

These are precisely the prefixes of, or bounds by,

\[
L_2=\operatorname{diag}(3,1,1,1,0,0,0,0).
\]

The traces agree. Thus \(X_s\prec L_2\).

Ky Fan convexity applied to the actual convex decomposition proves

\[
H_2(\rho)\prec L_2
\]

for pure inputs. Since \(H_2\) is linear in the input, spectral decomposition of an arbitrary mixed density and another application of convexity prove the same statement for **every complex three-qubit density**.

This closes the new paired-projection obligation.

## 5. The one-body majorant and all eight channel prefixes

### 5.1 One-body majorization

Diagonalize each actual marginal as

\[
\rho_i=V_i\operatorname{diag}(q_i,1-q_i)V_i^\dagger,
\qquad 0\le q_i\le1.
\]

The computational-basis operator obtained by summing the three lifted \(|0\rangle\langle0|\) factors has spectrum

\[
L_1=\operatorname{diag}(3,2,2,2,1,1,1,0).
\]

Conjugating it by

\[
U_s=\bigotimes_i V_iX^{s_i}
\]

and averaging the independent bits with probabilities \(q_i,1-q_i\) gives exactly the three prescribed lifted marginals. Identities on the other factors are unchanged. Hence

\[
H_1(\rho)\prec L_1.
\]

Arbitrary complex marginal eigenbases are allowed; no joint pure-state normal form is imposed.

### 5.2 Actual tensor expansion and its consuming projector

For

\[
T_t(X)=tX+b\operatorname{Tr}(X)I,\qquad
b=\frac{1-t}{2},\qquad 0\le t\le1,
\]

the actual tensor expansion is

\[
T_t^{\otimes3}(\rho)
=t^3\rho+t^2bH_2+tb^2H_1+b^3I.
\]

For the **same arbitrary complex orthogonal rank-\(k\) projector \(Q\)** throughout,

\[
\operatorname{Tr}\!\left[QT_t^{\otimes3}(\rho)\right]
\le
t^3+t^2bK_k(L_2)+tb^2K_k(L_1)+kb^3.
\]

All coefficients are nonnegative. The step \(\operatorname{Tr}(Q\rho)\le1\) holds for every density and every \(k\ge1\).

For the product input \(|000\rangle\), its density, its two marginal sums, and the identity are all diagonal and co-ordered by Hamming weight. Their spectra are respectively

\[
(1,0,\ldots,0),\quad L_2,\quad L_1,\quad I.
\]

Their weighted sum is exactly

\[
D_{3,t}=\operatorname{diag}(a,b)^{\otimes3},
\qquad a=t+b=\frac{1+t}{2}.
\]

Thus the preceding upper bound is exactly \(K_k(D_{3,t})\), not an enlarged relaxation.

Writing \(u=a^3\), \(d=a^2b\), \(c=ab^2\), and \(\ell=b^3\), the complete reference spectrum is

\[
(u,d,d,d,c,c,c,\ell).
\]

Its eight prefixes are

\[
u,\quad u+d,\quad u+2d,\quad u+3d,\quad
u+3d+c,\quad u+3d+2c,\quad u+3d+3c,\quad1.
\]

Taking the maximum over all rank-\(k\) projectors proves the claimed eight output-prefix bounds.

There is no incompatible-maximizer error: actual summands are bounded for one fixed \(Q\), while only the **reference** summands need common ordering to identify the resulting bound.

### 5.3 Endpoints

No division by \(t\), \(b\), marginal populations, or eigenvalue gaps occurs.

- At \(t=0\), the expansion gives \(I/8\).
- At \(t=1\), it reduces to the density bound by a pure reference.
- The normalizing operator \(G\) remains invertible independently of these channel endpoints.

## 6. Full physical interval and negative-branch dispatch

For the stated channel, \(s=1-p\) lies in \([-1/3,1]\). The displayed Pauli probabilities give precisely that physical interval.

Let

\[
\mathcal J(X)=YX^TY=\operatorname{Tr}(X)I-X.
\]

Direct substitution gives

\[
T_{-t}=\mathcal J\circ T_t.
\]

Tensoring this identity gives, for \(W_n=Y^{\otimes n}\),

\[
T_{-t}^{\otimes n}(\rho)
=W_n[T_t^{\otimes n}(\rho)]^TW_n.
\]

This is a **full transpose**, followed by unitary conjugation. It preserves the complete spectrum.

The consuming projector is correctly transported:

\[
\operatorname{Tr}[QT_{-t}^{\otimes n}(\rho)]
=\operatorname{Tr}[Q'T_t^{\otimes n}(\rho)],
\qquad Q'=W_nQ^TW_n.
\]

Indeed transposing \(W_nQW_n\) produces two factors \(W_n^T=(-1)^nW_n\), whose signs cancel. Thus \(Q'\) is again a complex orthogonal projector with the same rank, including odd \(n\).

The physical negative branch requires only \(t\le1/3\), already included in the positive-\(t\) proof. The reference’s one-qubit eigenvalues are \(a,b\), possibly exchanged before ordering. Therefore Theorem A holds throughout \(0\le p\le4/3\).

## 7. Review of the expressly supplied example

Only the author’s supplied state and supplied physical parameter/projector are evaluated here:

\[
|\psi_*\rangle
=\frac{|000\rangle+|001\rangle+|010\rangle+|100\rangle}{2}.
\]

### 7.1 Exclusion from all local-parity sectors

Each single-qubit marginal is

\[
m=
\begin{pmatrix}
3/4&1/4\\
1/4&1/4
\end{pmatrix}
=\frac12\left(I+\frac{X+Z}{2}\right),
\]

with distinct eigenvalues \((1\pm1/\sqrt2)/2\).

If the pure state were an eigenvector of a product \(A_1\otimes A_2\otimes A_3\) of traceless Hermitian one-qubit unitaries, conjugation invariance of its density and partial trace would imply \(A_imA_i=m\). Nondegeneracy then forces

\[
A_i=\pm H,\qquad H=(X+Z)/\sqrt2.
\]

For the supplied state, the Hadamard-sign sum stated by the author is ten, with normalization \(4\sqrt8\). Hence

\[
\langle\psi_*|H^{\otimes3}|\psi_*\rangle
=\frac{5}{4\sqrt2},
\qquad
\left|\langle\psi_*|H^{\otimes3}|\psi_*\rangle\right|^2
=\frac{25}{32}<1.
\]

A normalized eigenvector of this Hermitian unitary would instead have expectation of modulus one. Changing local signs changes only the overall sign. This excludes every physical local-parity representation.

A positive convex decomposition of a rank-one density can have positive-weight components only on that same ray. Since this ray belongs to no local-parity sector, its density also lies outside the convex hull of all those sectors.

### 7.2 Exact supplied physical expectation

At the supplied parameter

\[
p=\frac14,\qquad t=\frac34,\qquad b=\frac18,\qquad a=\frac78,
\]

take the supplied \(Q_*=\rho_*=|\psi_*\rangle\langle\psi_*|\).

Written multiplication gives \(\operatorname{Tr}(m^2)=3/4\). Therefore

\[
\operatorname{Tr}(Q_*H_1)=\frac94.
\]

Purity equates the nonzero spectra of each complementary pair of marginals, so also

\[
\operatorname{Tr}(Q_*H_2)=\frac94.
\]

The actual channel expectation is consequently

\[
t^3+\frac94(t^2b+tb^2)+b^3
=\frac{432+189+2}{1024}
=\frac{623}{1024}
<\frac{686}{1024}
=a^3.
\]

This supports the author’s exact calculation. It is one supplied physical expectation, **not a largest-eigenvalue calculation, executed finite verification, or substitute for the universal proof**.

## 8. Full four-qubit \(1|3\)-separable consequence

The one-qubit channel output for any density has ordered eigenvalues

\[
\frac{1+tr}{2},\quad \frac{1-tr}{2},\qquad 0\le r\le1,
\]

and is therefore majorized by \(D_{1,t}=\operatorname{diag}(a,b)\).

The positive tensor-preservation step is valid. If \(x_i\ge0\) are the eigenvalues of \(X\), then, with integer prefix allocations and \(K_0=0\),

\[
K_k(X\otimes Y)
=\max_{\substack{0\le k_i\le\dim Y\\\sum_i k_i=k}}
\sum_i x_iK_{k_i}(Y).
\]

Thus \(Y\prec Y_0\) implies

\[
K_k(X\otimes Y)\le K_k(X\otimes Y_0).
\]

Applying the same argument after exchanging tensor factors, using positivity of \(Y_0\) and \(X\prec X_0\), proves

\[
X\otimes Y\prec X_0\otimes Y_0.
\]

Trace equality is preserved.

Theorem A therefore gives, for arbitrary one-qubit \(\sigma\) and arbitrary three-qubit \(\tau\),

\[
\Phi_p(\sigma)\otimes\Phi_p^{\otimes3}(\tau)
\prec D_{1,t}\otimes D_{3,t}=D_{4,t}.
\]

For a separable mixture, linearity and the **same fixed consuming projector** give the same reference bound component by component. Physical permutations of the qubits are unitary conjugations and commute with the identical local-channel construction. The spectator position can consequently vary between mixture components.

The ordered reference spectrum has multiplicities

\[
a^4,\quad
a^3b\ (4),\quad
a^2b^2\ (6),\quad
ab^3\ (4),\quad
b^4.
\]

All sixteen prefixes follow, including

\[
K_3\!\left(\Phi_p^{\otimes4}(\rho)\right)
\le a^4+2a^3b
\]

on the complete convex hull of the four \(1|3\)-separable classes.

This audits the downstream use of the new \(H_2\) value through the channel expansion, Theorem A, tensor preservation, and the final mixture bound. No producer-side result is left without its consuming inequality being checked.

## 9. Exact imports, execution boundary, and residual claims

### Imports and source limits

The arbitrary-three-qubit proof reconstructed above is self-contained apart from elementary finite-dimensional spectral facts, antiunitary identities, and Ky Fan variational/convexity properties, whose relevant uses have been displayed.

S2 supplies only its recorded parity-sector scope and historical comparison. Its linked author bodies, finite verifier, receipts, earlier hulls, and source-obstruction documents were **not opened or imported as fresh mathematical premises**.

The public-paper summary in S1 was read as part of the assigned candidate, but the paper itself was not followed under this WRITTEN scope. Its current content, source-wide status, and priority implications are therefore not independently certified here. They are unnecessary to the proof.

Descriptions of older proof gaps or weakened spectral countermodels are **not converted into counterexamples to the older stated theorems**.

### Execution and finite-check accounting

- Scientific code produced: **none**.
- Scientific executable, interpreter, CAS, solver, enumeration, or replay: **NOT RUN**.
- Scientific argv: **none**.
- Author program: **not supplied or read**.
- Build, test, lint, formatter: **NOT RUN**.
- New public-source follow-up: **none**.
- Independent finite-check verdict: **NOT RUN**, not PASS.
- Exact calculations above: written algebra and arithmetic on formal parameters or the expressly supplied author instance.
- Metadata hashing and clocks: parent-attributed only.

No numerical tolerance, floating-point result, or interval certificate is used to establish a universal inequality.

### Remaining scope

This review supports the written derivations of:

1. \(H_2(\rho)\prec(3,1,1,1,0,0,0,0)\) for every complex three-qubit density.
2. All eight depolarizing-output prefixes for those densities throughout the full physical interval.
3. All sixteen prefixes on the entire four-qubit \(1|3\)-separable hull.

A separately established theorem covering every \(2|2\)-separable class could be combined with item 3, by the same convexity principle, to cover **all biseparable four-qubit states**. No complete \(2|2\) theorem was independently imported or audited in this assignment, so that broader union is not granted here.

Neither that possible biseparable union nor the present \(1|3\) result establishes unrestricted four-qubit majorization. The unrestricted four-qubit \(k=3\) target remains unclosed by this proof. No general blocklength, general local dimension, arbitrary ancillary tensorization, novelty, priority, human review, independent-family review, or formal/kernel acceptance is inferred.

## 10. Verdict fields

**Overall correctness: correct.**

The complete paired-projection lemma and its downstream uses reconstruct without a mathematical defect at the frozen scope. The proof establishes arbitrary-complex three-qubit output majorization and its full four-qubit \(1|3\)-separable consequence, while leaving unrestricted four-qubit and novelty claims outside the result.

**Confidence: 0.97.**

**Final disposition:** Return this completed written review for parent consideration and materialization; **no self-acceptance or automatic adoption**.