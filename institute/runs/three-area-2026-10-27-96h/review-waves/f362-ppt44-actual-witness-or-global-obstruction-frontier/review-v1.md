# f362 — Author candidate: actual \(4\times4\) family exclusion and an exact detector-certification obstruction

**Status: UNREVIEWED author result. The unrestricted original \(4\times4\) target is NOT PROVED or REFUTED.**

This return supplies:

1. An explicit actual \(4\times4\) PPT state with an exact Schmidt-number-\(2\) decomposition, falsifying the proposed intermediate-state route to Schmidt number \(3\).
2. A full-family exclusion: **every positive semidefinite completion of its specified separable local compression has Schmidt number at most \(2\)**, including arbitrary coherent completion blocks—not merely the displayed state or a fixed detector.
3. A separate exact obstruction to a public-source detector-certification route: for the free-marginal PPT relaxation in arXiv:2508.21348v2, **when \(k\ge2\), passing the relaxation is equivalent to complete positivity**. Consequently, that relaxation cannot certify any non-CP \(2\)-positive detector.
4. A primary-source comparison distinguishing the existing \(4\times5\) construction, symplectic-family exclusions, and recent asymptotic results from the unrestricted \(4\times4\) question.

No global novelty or exhaustive literature-status claim is made.

---

## 1. Input, ordering, and execution disclosure

I read the complete manifest and receipt, all six status/permission controls, and the entire literal packet through its ending. The controls were fetched concurrently after the manifest/receipt; the scientific packet was then read in its declared order, **S1 followed by S2**.

The parent’s optional Krebs–Gachechiladze public-source lead arrived before the packet read finished. I subsequently read the actual public primary sources; the scientific derivations below followed the completed packet read. No historical held scientific payload was supplied or used.

The following pin matches are **parent-reported metadata**, not child-executed hashes:

- Manifest: `bdad2208873b61a9c35084764a4735e87ee28ba8c52c9f3d7b616367ad35f3ac`
- Receipt: `ab9b4bb25cace68766da9db9d30901a17ad3bd0926833d68838b69b93ae9b0e9`
- Packet: `3002b52d16ffa31e465991f7f58e83e8b8c953f908d0bf06b5e328a2b7e7af6d`

The supplied parent clock observations were `2026-10-30T09:13:58-0700 PDT` and, following the substantive research checkpoint, `2026-10-30T09:21:28-0700 PDT`. Neither is represented as my exact start, derivation, or completion time.

**Execution:** no scientific executable, numerical scan, SDP solver, external-model CLI, installation, or infrastructure action was run. All new results below are written exact mathematics. No working-tree candidate file was written; this is the complete body for Main materialization as `author-candidate-v1.md`.

---

## 2. Conventions and original target

Write
\[
[v]=|v\rangle\langle v|,\qquad
\operatorname{vec}(X)=\sum_{i,j}X_{ij}|ij\rangle.
\]
Partial transpose \(\Gamma\) acts on Bob unless specified otherwise.

The original positive target requires an actual operator on
\(\mathbb C^4\otimes\mathbb C^4\) satisfying
\[
\rho\ge0,\qquad \rho^\Gamma\ge0,\qquad
\operatorname{Tr}\rho=1,\qquad \operatorname{SN}(\rho)\ge3.
\]
An explicit detector certificate would additionally require a Hermitian \(W\) with
\[
\langle\operatorname{vec}(X)|W|\operatorname{vec}(X)\rangle\ge0
\quad\text{for every complex }X\in M_4,\ \operatorname{rank}X\le2,
\]
and \(\operatorname{Tr}(W\rho)<0\).

No such pair, alternative \(4\times4\) lower certificate, or unrestricted no-go is claimed here.

---

## 3. Actual \(4\times4\) route: an exact PPT state whose Schmidt number is \(2\)

Define
\[
\begin{aligned}
A&=|00\rangle+|11\rangle+|22\rangle,\\
B&=|01\rangle+|12\rangle,\\
D&=|10\rangle-|21\rangle,\\
E&=|20\rangle+|33\rangle,
\end{aligned}
\]
and the actual \(4\times4\) operator
\[
R=[A]+[B]+[D]
  +3\bigl([02]+[E]+[23]+[30]+[32]\bigr).
\tag{1}
\]

This is the one-extension intermediate route suggested by the local-extension construction, not the frozen \(4\times5\) state. The corresponding intermediate-state limitation is discussed in Krebs–Gachechiladze, [arXiv:2509.07086v1, Supplementary Material E](https://arxiv.org/html/2509.07086v1#A5). The following certificates are explicit reconstructions.

### 3.1 Exact state positivity and normalization

Equation (1) is a positive sum of projectors. Its displayed vectors have mutually disjoint computational supports, so
\[
\operatorname{rank}R=8,\qquad
\operatorname{Tr}R=3+2+2+3(1+2+1+1+1)=25.
\]
Thus \(\rho_0=R/25\) is a state.

### 3.2 Exact partial-transpose positivity

Direct partial transposition gives
\[
\begin{aligned}
R^\Gamma={}&[\,|01\rangle+|10\rangle\,]
+[\,|12\rangle+|21\rangle\,]\\
&+[\,|02\rangle+|11\rangle-|20\rangle\,]
+2[\,|02\rangle+|20\rangle\,]\\
&+3[\,|23\rangle+|30\rangle\,]
+[00]+[22]+3[33]+3[32].
\end{aligned}
\tag{2}
\]
Every summand is positive semidefinite, proving \(R^\Gamma\ge0\) exactly.

For example, the only three-coordinate block, in the order
\((02,11,20)\), is
\[
\begin{pmatrix}
3&1&1\\
1&1&-1\\
1&-1&3
\end{pmatrix}
=
\begin{pmatrix}1\\1\\-1\end{pmatrix}
\begin{pmatrix}1&1&-1\end{pmatrix}
+
2\begin{pmatrix}1\\0\\1\end{pmatrix}
\begin{pmatrix}1&0&1\end{pmatrix}.
\]
The nine vectors in (2) are independent, so
\(\operatorname{rank}R^\Gamma=9\). Positivity does not depend on numerical eigenvalue tolerances.

### 3.3 Exact Schmidt-rank-\(\le2\) decomposition

For \(z\in\{1,i,-1,-i\}\), put
\[
v_z=B+zA-z^2D+z^{-1}|02\rangle.
\tag{3}
\]
Each \(v_z\) has Schmidt rank at most \(2\), because
\[
\begin{aligned}
v_z={}&
 (|0\rangle+z|1\rangle+z^2|2\rangle)
 \otimes(|1\rangle+z^{-1}|2\rangle)\\
&+(z|0\rangle-z^2|1\rangle)\otimes|0\rangle.
\end{aligned}
\tag{4}
\]
This is an exact sum of two product vectors over \(\mathbb C\).

The four powers with exponents \(-1,0,1,2\) are distinct modulo \(4\). Root-of-unity averaging therefore cancels every cross term:
\[
\frac14\sum_{z\in\{1,i,-1,-i\}}[v_z]
=[A]+[B]+[D]+[02].
\tag{5}
\]
Consequently,
\[
R=
\frac14\sum_z[v_z]
+2[02]+3[E]+3[23]+3[30]+3[32].
\tag{6}
\]
Every term in (6) has Schmidt rank at most \(2\). Hence
\[
\operatorname{SN}(\rho_0)\le2.
\]

This is a finite **exact decomposition certificate**, not a finite scan intended to establish universal positivity.

### 3.4 The state is entangled, so its Schmidt number is exactly \(2\)

Projecting both parties onto coordinates \(0,1,2\) gives
\[
R_3=[A]+[B]+[D]+3[02]+3[20].
\]
Its range consists of coefficient matrices
\[
X=
\begin{pmatrix}
a&b&c\\
d&a&b\\
e&-d&a
\end{pmatrix}.
\]
If \(X\) has complex rank at most \(1\), its upper-left and lower-right \(2\times2\) minors vanish:
\[
a^2-bd=0,\qquad a^2+bd=0.
\]
Thus \(a=0\). Every product vector in \(\operatorname{range}R_3\) therefore has zero \(00\) coefficient.

In any positive pure-state decomposition of \(R_3\), every constituent vector belongs to \(\operatorname{range}R_3\): a vector in its kernel has zero squared overlap with every constituent. A separable decomposition would consequently imply
\(\langle00|R_3|00\rangle=0\), whereas this entry equals \(1\).

Therefore \(R_3\), and hence \(R\), is entangled. Combining this with (6),
\[
\boxed{\rho_0=R/25\text{ is an actual }4\times4\text{ PPT state with }
\operatorname{SN}(\rho_0)=2.}
\tag{7}
\]

In particular, **no universally complex-rank-\(\le2\) nonnegative detector can have negative pairing with this state**: applying its defining inequality to every term of (6) gives \(\operatorname{Tr}(WR)\ge0\).

---

## 4. Full-family exclusion: arbitrary coherent completions cannot repair this route

The preceding failure is not limited to one state or one detector.

### 4.1 General local-completion lemma

Let \(Q_B\) be a codimension-one local projection and let
\(Q=I_A\otimes Q_B\). Relative to retained and removed Bob coordinates, write any positive semidefinite operator as
\[
\rho=
\begin{pmatrix}
C&Z\\ Z^\dagger&D
\end{pmatrix},
\qquad C=Q\rho Q.
\]
If \(C\) is separable, then
\[
\boxed{\operatorname{SN}(\rho)\le2.}
\tag{8}
\]
No PPT assumption is needed for this lemma.

**Proof.** Positivity implies
\[
\operatorname{range}Z\subseteq\operatorname{range}C,\qquad
D-Z^\dagger C^+Z\ge0,
\]
where \(C^+\) is the Moore–Penrose inverse. The range inclusion follows by testing the quadratic form against a vector in \(\ker C\); the Schur inequality follows by choosing retained component \(-C^+Zy\).

Take a finite separable conic decomposition
\[
C=\sum_j[u_j],\qquad u_j=a_j\otimes b_j.
\]
Define
\[
\widetilde u_j=
\begin{pmatrix}
u_j\\Z^\dagger C^+u_j
\end{pmatrix}.
\]
Then
\[
\sum_j[\widetilde u_j]=
\begin{pmatrix}
C&Z\\ Z^\dagger&Z^\dagger C^+Z
\end{pmatrix}.
\]
The added component occupies one Bob coordinate, so it is a product vector. Each \(\widetilde u_j\) has Schmidt rank at most \(2\). The remaining positive operator \(D-Z^\dagger C^+Z\) occupies that same single Bob coordinate and is separable. This proves (8). If \(C=0\), positivity forces \(Z=0\), and the conclusion is immediate. ∎

This reconstructs the relevant Schur-complement mechanism of [Krebs–Gachechiladze v1, Theorem 2](https://arxiv.org/html/2509.07086v1#Thmobservation2), rather than treating that theorem as an unexplained import.

### 4.2 Exact separable compression of the displayed state

Delete Bob coordinate \(0\):
\[
Q_B=|1\rangle\langle1|+|2\rangle\langle2|+|3\rangle\langle3|.
\]
For
\[
p_z=(|0\rangle+z|1\rangle+z^2|2\rangle)
       \otimes(|1\rangle+z^{-1}|2\rangle),
\]
the retained block of (1) is
\[
C_0=QRQ
=\frac14\sum_z[p_z]
 +2[02]+3[23]+3[33]+3[32].
\tag{9}
\]
This is explicitly separable.

It follows from (8) that
\[
\boxed{
\text{Every PSD }4\times4\text{ completion with }Q\rho Q=C_0
\text{ has Schmidt number }\le2.
}
\tag{10}
\]
The same holds for \(Q\rho Q=tC_0\), \(t\ge0\).

The completion blocks \(Z,D\) are otherwise arbitrary, subject only to positivity. Thus changing coherent couplings to Bob coordinate \(0\), changing their phases, or changing the removed-coordinate block cannot create Schmidt number \(3\) while retaining this compression. All PPT completions are included.

### 4.3 A broader actual \(4\times4\) PPT family

The fixed compression can be generalized. Decompose the retained \(12\)-dimensional space into
\[
\begin{aligned}
\mathcal E&=\operatorname{span}\{|0\rangle,|1\rangle,|2\rangle\}_A
             \otimes\operatorname{span}\{|1\rangle,|2\rangle\}_B,\\
\mathcal F&=\operatorname{span}\{|0\rangle,|1\rangle,|2\rangle\}_A
             \otimes\operatorname{span}\{|3\rangle\}_B,\\
\mathcal G&=\operatorname{span}\{|3\rangle\}_A
             \otimes\operatorname{span}\{|1\rangle,|2\rangle,|3\rangle\}_B.
\end{aligned}
\]
These are mutually orthogonal and their direct sum is \(\operatorname{range}Q\).

Suppose \(\rho\) is any \(4\times4\) PPT state and \(Q\rho Q\) is block diagonal across \(\mathcal E,\mathcal F,\mathcal G\). Its \(\mathcal E\) block is a \(3\times2\) PPT operator, so it is separable by **Theorem 3** of Horodecki–Horodecki–Horodecki, [arXiv:quant-ph/9605038v2](https://arxiv.org/html/quant-ph/9605038v2#Thmtheorem3). The theorem states PPT iff separable on \(2\times2\) and \(2\times3\); swapping parties gives the required \(3\times2\) case. It applies to unnormalized nonzero positive operators after normalization.

The \(\mathcal F,\mathcal G\) blocks each have a one-dimensional local factor, so they are separable. Therefore \(Q\rho Q\) is separable and (8) yields
\[
\boxed{
\rho\text{ PPT and }Q\rho Q
\text{ block diagonal across }\mathcal E,\mathcal F,\mathcal G
\ \Longrightarrow\ \operatorname{SN}(\rho)\le2.
}
\tag{11}
\]

This excludes arbitrary \(3\times2\) PPT retained blocks and arbitrary PSD coherent completions, not just the original grid weights.

**Boundary:** there is no proof that an arbitrary \(4\times4\) PPT state can be put into this retained-block form. Equation (11) is a family exclusion, not a global no-go.

---

## 5. Exact obstruction to the free-marginal PPT detector-certification route

### 5.1 The primary-source relaxation

Vom Ende–Khatri–Denisov, [arXiv:2508.21348v2, §3.3, Eq. (6)](https://arxiv.org/html/2508.21348v2#S3.SS3), define a sufficient condition for \(k\)-positivity using
\[
f_k(\Phi)=
\min\left\{
\operatorname{Tr}\!\left(C(\Phi\otimes\operatorname{id}_k)P\right):
P\ge0,\ P^{T_1}\ge0,\
\operatorname{Tr}_1P=\omega,\
\operatorname{Tr}_2P=\rho
\right\},
\tag{12}
\]
where both marginals \(\rho,\omega\) are optimization variables ranging over density matrices.

Thus the feasible set is precisely the PPT density matrices on
\(\mathbb C^{dk}\otimes\mathbb C^{dk}\). Their condition \(f_k(\Phi)\ge0\) is valid as a sufficient condition.

The route investigated here was to use (12) to certify a non-CP \(2\)-positive detector. The following theorem rules that out exactly.

### 5.2 Classification theorem

Use the paper’s unnormalized Choi convention
\[
C(\Phi)=\sum_{i,j=1}^d|i\rangle\langle j|
                   \otimes\Phi(|i\rangle\langle j|).
\]
For every Hermiticity-preserving \(\Phi:M_d\to M_d\) and every integer \(k\ge2\),
\[
\boxed{
f_k(\Phi)\ge0
\iff C(\Phi)\ge0
\iff\Phi\text{ is completely positive}.
}
\tag{13}
\]
More precisely, \(f_k(\Phi)=0\) in the CP case and \(f_k(\Phi)<0\) otherwise.

**Proof.** Write \(C=C(\Phi)\), and define on the ancillary \(k\times k\) space
\[
|\omega_k\rangle=\frac1{\sqrt k}\sum_{\alpha=1}^k|\alpha\alpha\rangle,
\qquad D_k=[\omega_k].
\]
Let \(V_k\) be the ancillary swap, so \(D_k^\Gamma=V_k/k\).

Regroup tensor factors as
\[
(Aa)\mid(Bb),
\]
where \(A,B\) are the original Choi parties and \(a,b\) are the ancillary parties. Under this explicit permutation,
\[
C(\Phi\otimes\operatorname{id}_k)=kC_{AB}\otimes D_{k,ab}.
\tag{14}
\]

If \(C\not\ge0\), choose a unit vector \(\psi\) with
\[
\langle\psi|C|\psi\rangle=\lambda<0.
\]
Define
\[
P_\psi=[\psi]\otimes D_k+
             I_{d^2}\otimes(I_{k^2}-D_k).
\tag{15}
\]
Both terms are PSD and
\[
\operatorname{Tr}P_\psi=1+d^2(k^2-1).
\tag{16}
\]

For every complex unit bipartite \(\psi\),
\(\|[\psi]^\Gamma\|_\infty\le1\). Indeed its partial-transpose eigenvalues are \(s_i^2\) and \(\pm s_i s_j\), where \(s_i\) are Schmidt coefficients.

Let \(\Pi_\pm=(I\pm V_k)/2\). Transposing party \(Aa\) in (15) gives
\[
\begin{aligned}
P_\psi^\Gamma
={}&\frac1k\bigl([\psi]^{\Gamma_A}+(k-1)I\bigr)\otimes\Pi_+\\
&+\frac1k\bigl(-[\psi]^{\Gamma_A}+(k+1)I\bigr)\otimes\Pi_-.
\end{aligned}
\tag{17}
\]
Both coefficients are PSD when \(k\ge2\). Therefore the normalization of \(P_\psi\) is feasible in (12), with its actual reduced states as the free marginals.

Using \(D_k(I-D_k)=0\), equations (14)–(16) give
\[
f_k(\Phi)\le
\frac{k\lambda}{1+d^2(k^2-1)}<0.
\tag{18}
\]

Conversely, if \(C\ge0\), then (14) is PSD and its pairing with every feasible \(P\ge0\) is nonnegative.

Finally,
\[
P_0=
\frac{I_{d^2}\otimes(I_{k^2}-D_k)}
     {d^2(k^2-1)}
\]
is a PPT density matrix: its partial transpose is proportional to
\(I\otimes(I-V_k/k)\ge0\). Its objective is zero. Hence \(f_k(\Phi)\le0\) always, completing the classification. ∎

### 5.3 Exact selected control in the relevant \(d=4,k=2\) setting

Take
\[
C=2I_{16}-[\Omega_4],\qquad
\Omega_4=\sum_{i=0}^3|ii\rangle.
\]
This is universally \(2\)-block positive over complex matrices:
\[
\langle\operatorname{vec}X|C|\operatorname{vec}X\rangle
=2\|X\|_F^2-|\operatorname{Tr}X|^2\ge0
\quad(\operatorname{rank}X\le2),
\]
because
\[
|\operatorname{Tr}X|\le\|X\|_*
\le\sqrt2\,\|X\|_F.
\]
Nevertheless, for \(\psi=\Omega_4/2\), \(C\psi=-2\psi\).

The exact PPT test operator (15) has trace \(49\), and its normalized objective is
\[
\operatorname{Tr}\!\left(
C(\Phi\otimes\operatorname{id}_2)\frac{P_\psi}{49}
\right)=-\frac4{49}.
\tag{19}
\]
Its unnormalized partial transpose has eigenvalues among
\[
\frac38,\quad\frac58,\quad\frac{11}8,\quad\frac{13}8,
\]
obtained from the commuting original and ancillary swaps. Thus this is an exact falsification of the attempted certification route, even for an explicitly proved \(2\)-positive map.

**Dimensional boundary:** \(P_\psi/49\) is an \(8\times8\) state used only as a feasible point of the relaxation. It is not a \(4\times4\) target witness.

**Method boundary:** theorem (13) concerns exactly Eq. (6), with free marginals and the stated PPT constraint. It does not exclude higher hierarchies or materially different certificates. It does not invalidate the paper’s sufficient-condition implication; it shows that this implication cannot certify a non-CP \(2\)-positive map.

---

## 6. Primary-source comparison and exact dimensional boundaries

| Primary source actually read | Exact result inspected | Consequence for this assignment |
|---|---|---|
| Krebs–Gachechiladze, [2402.12966v1](https://arxiv.org/html/2402.12966v1), Result 1 and Appendix B | PPT Schmidt number \(3\) in \(5\times5\), proved through vanishing complex minors | Not \(4\times4\); the paper’s other displayed low-Alice example is \(4\times12\). |
| Krebs–Gachechiladze, [2509.07086v1](https://arxiv.org/html/2509.07086v1), Theorem 5, Eq. (11), SM D–E | PPT Schmidt number \(3\) in \(4\times5\); its Eq. (11) range has the frozen S1 coefficient pattern. SM E identifies the intervening \(4\times4\) state as still SN \(2\). | The extra Bob coordinate is substantive. The frozen integer detector is not thereby attributed to this paper. Sections 3–4 above give explicit certificates and a completion-family exclusion. |
| Park, [2602.09860v3](https://arxiv.org/html/2602.09860v3), Corollary 4.3 and Theorem 4.4 | Every PPT state in the specified \(S\otimes\bar S\) or \(S\otimes S\) symplectic-invariant family has SN at most \(d/2\), for even \(d\ge4\) and skew-unitary twisting matrix | At \(d=4\), this excludes the full specified symmetry family, not arbitrary \(4\times4\) PPT states. |
| Johnston–Lovitz, [2609.11849v1](https://arxiv.org/html/2609.11849v1), Theorems 1 and 7, Lemma 6 | Constructive lower bound \(\left\lceil(m+n-\sqrt{(m-n)^2+4(m+n-1)})/2\right\rceil\) | At \(4\times4\), this is \(4-\lfloor\sqrt7\rfloor=2\), not \(3\). At \(4\times8\), it gives \(3\), still outside the target. |
| Vom Ende–Khatri–Denisov, [2508.21348v2](https://arxiv.org/html/2508.21348v2), §3.3, Eqs. (6)–(8) | The free-marginal PPT sufficient condition for \(k\)-positivity | Section 5 proves its exact obstruction for the intended non-CP \(2\)-positive-detector use. |
| Horodecki–Horodecki–Horodecki, [quant-ph/9605038v2](https://arxiv.org/html/quant-ph/9605038v2), Theorem 3 and proof | PPT iff separable on \(2\times2\) and \(2\times3\) | Named external import used only for the \(3\times2\) block in (11). |

For the Johnston–Lovitz route, Lemma 6 requires
\[
(m-r)(n-r)>\dim\mathcal S.
\]
Its chosen low-rank starting support has dimension \(m+n-1\). At \(m=n=4\), the desired \(r=2\) application would require
\[
4>7,
\]
which is false. This identifies a failed hypothesis, **not** an SN-\(\le2\) proof for their particular \(4\times4\) perturbation states.

The frozen S1 filter gap remains a **fixed state–detector bridge obstruction**. It must not be promoted to a Schmidt-number upper bound on every filtered state. Likewise, frozen S2 excludes its specified skew-unitary detector/filter route, not general \(4\times4\) PPT/SN-\(\ge3\) existence.

---

## 7. Result, evidence, and remaining gaps

### Established by the written author arguments

- An actual \(4\times4\) state \(R/25\), with exact PSD and partial-transpose PSD decompositions, has **Schmidt number exactly \(2\)**.
- Every PSD completion of its separable Bob-delete-\(0\) compression has SN at most \(2\), with arbitrary coherent completion blocks.
- More broadly, the actual \(4\times4\) PPT retained-block family in (11) cannot supply SN \(3\).
- The precise free-marginal PPT relaxation (12) cannot certify any non-CP \(2\)-positive detector; its nonnegative region is exactly the CP cone.

### Not established

- An actual \(4\times4\) PPT state of SN at least \(3\).
- A universally complex-rank-\(\le2\) detector with negative pairing against such a state.
- A universal \(4\times4\) PPT/SN-\(\le2\) theorem.
- Exhaustive current literature status, priority, or novelty.

### Verification boundary

All new claims remain **UNREVIEWED** pending a disjoint check and parent disposition. No human, independent-model-family, formal/kernel, numerical-experiment, or novelty verification is claimed. There is no scientific execution code or execution output to report: the complete exact inputs, algebraic certificates, and derived results are given above.

**Disposition for the frozen target:** no unrestricted closure; substantive actual-family impossibility and a separate exact falsified detector-certification route are supplied without substituting \(4\times5\), \(4\times8\), \(8\times8\), or a restricted filter obstruction for the original \(4\times4\) problem.