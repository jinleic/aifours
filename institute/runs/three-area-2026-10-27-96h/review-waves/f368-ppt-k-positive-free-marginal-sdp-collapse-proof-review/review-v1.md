# f368 — Complete written review of the free-marginal PPT SDP characterization

**Verdict: SUPPORTED at the exact frozen §5 scope.** No FATAL, MAJOR, or MINOR mathematical finding was identified. The claimed characterization is correct for the literal SDP in arXiv:2508.21348v2, Eq. (6), with both marginals free density operators, for every Hermiticity-preserving complex-linear map \(\Phi:M_d\to M_d\), \(d\ge1\), and integer \(k\ge2\).

This is the complete review body for parent materialization as this wave’s `review-v1.md`. No working-tree write was attempted: the available write tool does not provide a permitted working-tree destination, and the shell restrictions prohibit a writing bypass.

## 1. Inputs, chronology, and verification limits

### Frozen inputs

The following pins are **parent-supplied metadata**, not hashes executed by this reviewer:

- Manifest: `1d899e651a0690da97949280cc1eed62e07e4ee70d2bea5921b295f9fa52b28e`
- Freeze receipt: `064c2a24744481b67381b403ac22ad67d39522c9462499ecd3964835d0e3e75e`
- Literal packet: `1edf128e6f4f062ae3d26b872ba5577cd8350432e9a3d362ee06cbeec79d75f3`

Source identifiers below refer to:

- **S1:** `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f362-ppt44-actual-witness-or-global-obstruction-frontier/review-v1.md`  
  SHA256 `1fbc6f48356fc00fc73024a0e06a3dd0f8133e75529275f64a458bd746d533bc`; supplied source lines 1–502.
- **S2:** `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/source-screens/ppt-paper-eq6-source-snapshot-v1.md`  
  SHA256 `31f3eb6815db1ef23519a69015b6519413f3c258f87642dd7eafec65309c7ccd`; lines 1–41.
- **S3:** `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/source-screens/ppt-k-positive-paper-equation6-literal-scope-v1.json`  
  SHA256 `27488a2e09e84bf62f2ce8d2db8c41fcc4586587aebd03462b43eba39f423f70`; lines 1–17.

### Read and exposure chronology

I read the complete manifest, freeze receipt, dispatch receipt, parent metadata supply, and all seven named status/permission controls before sending Main a direct administrative **pre-body ACK**. The controls were used only for permissions and exclusions; no excluded links were followed.

After that ACK, I read the entire literal packet consecutively in raw windows of at most 20 lines, through packet line 562, including every source ending. S1’s other sections were read for complete context but are **not mathematically accepted by this §5 review**.

After packet completion, I consulted the already-named [public v2 source](https://arxiv.org/html/2508.21348v2). A targeted search exposed scattered primary-source snippets; bounded rendered reads then confirmed §2’s unnormalized Choi definition and Proposition 1, and §3.3’s Eqs. (6)–(8). An attempted raw URL range returned site-chrome HTML and supplied no mathematical premise. I did not inspect ancillary implementation code or other paper versions.

S1 lines 18–30 report the author’s own earlier packet/source-lead chronology. That remains an attributed author disclosure, not a chronology independently certified by this reviewer.

The parent supplied clock observations `2026-10-30T09:31:55-0700 PDT` and, upon my request, `2026-10-30T09:39:07-0700 PDT`. Neither is represented as my native execution, exact start, private derivation, or completion time.

**Methods:** written reconstruction only. No scientific executable, CAS, solver, enumeration, numerical replay, or newly selected mathematical example was used. The \(d=4,k=2\) calculation below reviews the source-supplied example. No sibling return, held scientific payload, or its consumers was accessed.

## 2. Claim-by-claim disposition

| Claim and source lines | Disposition |
|---|---|
| Eq. (6) has two independently free density marginals, so its feasible \(P\) are exactly trace-one PPT operators on \(Aa\mid Bb\). S1:317–331; S2:17–34; S3:13–15. | **SUPPORTED** |
| With the paper’s unnormalized Choi convention, regrouping yields \(C(\Phi\otimes\mathrm{id}_k)=kC(\Phi)\otimes D_k\). S1:337–368. | **SUPPORTED** |
| The displayed \(P_\psi\) is PSD, has trace \(1+d^2(k^2-1)\), and becomes a feasible PPT density operator after normalization. S1:370–398. | **SUPPORTED** |
| A negative Choi eigenvalue \(\lambda\) produces normalized objective \(k\lambda/[1+d^2(k^2-1)]<0\). S1:400–405. | **SUPPORTED** |
| CP maps have nonnegative objective everywhere, while the displayed \(P_0\) is feasible with zero objective. S1:407–416. | **SUPPORTED** |
| Thus \(f_k(\Phi)\ge0\) iff \(\Phi\) is CP; moreover CP gives \(f_k=0\), and non-CP gives \(f_k<0\). S1:342–351. | **SUPPORTED**, including arbitrary complex \(\psi\), \(k=2\), and \(d=1\); \(k=1\) excluded |
| The source-supplied \(d=4,k=2\) example is 2-positive but non-CP and has the displayed negative feasible objective and partial-transpose spectrum. S1:420–449. | **SUPPORTED** |
| This does not contradict the paper’s sufficient implication, exclude higher hierarchies, or supply a \(4\times4\) PPT/SN-\(3\) witness. S1:451–453. | **SUPPORTED as the necessary scope boundary** |

No conclusion is reached here on S1’s separate physical-state/completion results, unrestricted original-target existence, exhaustive literature status, or novelty.

## 3. Exact comparison with the quoted v2 optimization

The quoted Eq. (6), also visibly present in the [v2 primary source, §3.3](https://arxiv.org/html/2508.21348v2#S3.SS3), is

\[
F(\Phi)=
\min_{\substack{
P\ge0,\ \rho,\omega\in\mathbb D(\mathbb C^d\otimes\mathbb C^k)\\
\operatorname{Tr}_1P=\omega,\ 
\operatorname{Tr}_2P=\rho,\ 
P^{T_1}\ge0}}
\operatorname{Tr}\!\left(C(\Phi\otimes\operatorname{id}_k)P\right).
\]

Both \(\rho\) and \(\omega\) are optimization variables. They are not fixed data, are not required to coincide, and impose no restriction beyond being the actual reduced density operators of \(P\).

Taking the trace of either marginal constraint gives \(\operatorname{Tr}P=1\). Conversely, every PSD trace-one \(P\) has PSD trace-one reductions, which can be chosen as those variables. Thus, writing the first physical party as \(Aa\) and the second as \(Bb\),

\[
\mathcal F=
\left\{
P\ge0:\operatorname{Tr}P=1,\ P^{T_A T_a}\ge0
\right\}.
\]

This is exactly the set of PPT density operators on \(\mathbb C^{dk}\otimes\mathbb C^{dk}\). It is a nonempty compact set. Hermiticity preservation makes the Choi objective Hermitian, so its minimum exists and is finite.

In particular, there is no hidden requirement that \(P\) be a product operator or separable, and no hidden fixed-marginal or extension constraint. The characterization reviewed here depends on this exact feasible set.

## 4. Independent reconstruction of the classification

### 4.1 Unnormalized Choi matrix and the physical cut

The paper defines

\[
C(\Phi)=
\sum_{i,j=1}^d E_{ij}\otimes\Phi(E_{ij}),
\]

using the unnormalized vector \(\sum_i|ii\rangle\). Consequently,

\[
C(\operatorname{id}_k)
=
\sum_{\alpha,\beta=1}^k
|\alpha\rangle\langle\beta|
\otimes|\alpha\rangle\langle\beta|
=
kD_k,
\qquad
D_k=|\omega_k\rangle\langle\omega_k|,
\quad
|\omega_k\rangle=\frac1{\sqrt{k}}\sum_\alpha|\alpha\alpha\rangle.
\]

Let the coordinate permutation \(R\) take the order \(AaBb\) to \(ABab\). Expanding in matrix units gives

\[
R\,C(\Phi\otimes\operatorname{id}_k)\,R^\dagger
=
C(\Phi)_{AB}\otimes C(\operatorname{id}_k)_{ab}
=
kC(\Phi)_{AB}\otimes D_{k,ab}.
\]

This regrouping is bookkeeping, **not a change of physical bipartition**. In the regrouped notation, Eq. (6)’s first-party transpose remains \(T_A T_a\), not \(T_A T_B\) and not merely an ancillary transpose.

No trace-preservation, unitality, or positivity assumption on \(\Phi\) is needed.

### 4.2 PSD candidate and its normalization

Write \(C=C(\Phi)\). If \(C\not\ge0\), Hermiticity supplies a unit eigenvector \(\psi\), possibly complex, with eigenvalue \(\lambda<0\). Put

\[
Q=|\psi\rangle\langle\psi|,
\qquad
P_\psi=Q\otimes D_k+
I_{AB}\otimes(I_{ab}-D_k).
\]

Both summands are PSD because \(D_k\) is an orthogonal projector. Furthermore,

\[
Z:=\operatorname{Tr}P_\psi
=
1+d^2(k^2-1)>0.
\]

Thus \(\widehat P_\psi=P_\psi/Z\) is a density operator.

Its marginals satisfy the actual free-marginal constraints explicitly. With
\(q_A=\operatorname{Tr}_B Q\) and \(q_B=\operatorname{Tr}_A Q\),

\[
\operatorname{Tr}_{Bb}\widehat P_\psi
=
\frac{q_A+d(k^2-1)I_A}{Z}
\otimes\frac{I_a}{k},
\]

\[
\operatorname{Tr}_{Aa}\widehat P_\psi
=
\frac{q_B+d(k^2-1)I_B}{Z}
\otimes\frac{I_b}{k}.
\]

Both expressions are PSD and trace one. They can therefore be used as the optimization variables \(\rho\) and \(\omega\), with the appropriate source ordering.

### 4.3 Arbitrary complex \(\psi\) and the correct transpose spectrum

For an arbitrary complex unit vector, take a Schmidt decomposition

\[
|\psi\rangle=(U\otimes V)\sum_i s_i|ii\rangle,
\qquad
s_i\ge0,\quad \sum_i s_i^2=1.
\]

Under partial transpose on \(A\), the local change of basis becomes the unitary conjugation by \(\overline U\otimes V\). Hence the spectrum of \(Q^{T_A}\) is

\[
s_i^2,\qquad +s_is_j,\qquad -s_is_j\quad(i<j),
\]

together with any zero eigenvalues. This argument does not assume real coordinates.

In particular,

\[
-\frac12 I\le Q^{T_A}\le I,
\]

because \(2s_is_j\le s_i^2+s_j^2\le1\). The author’s weaker bound
\(\|Q^{T_A}\|_\infty\le1\) is also correct.

### 4.4 Transposing both \(A\) and \(a\)

Let \(V_k\) be the ancillary swap and
\(\Pi_\pm=(I\pm V_k)/2\). Since \(D_k^{T_a}=V_k/k\),

\[
\begin{aligned}
P_\psi^{T_A T_a}
&=
Q^{T_A}\otimes\frac{V_k}{k}
+
I\otimes\left(I-\frac{V_k}{k}\right)\\
&=
\frac{Q^{T_A}+(k-1)I}{k}\otimes\Pi_+
+
\frac{-Q^{T_A}+(k+1)I}{k}\otimes\Pi_-.
\end{aligned}
\]

The two ancillary projectors have orthogonal ranges. The coefficient bounds are

\[
\frac{Q^{T_A}+(k-1)I}{k}
\ge
\frac{k-\tfrac32}{k}I,
\qquad
\frac{-Q^{T_A}+(k+1)I}{k}
\ge I.
\]

They are PSD for every \(k\ge2\). In particular, **\(k=2\) is included**: the stronger bounds give \(I/4\) and \(I\), respectively. Even the author’s coarser norm bound gives a valid nonnegative symmetric-block bound at the \(k=2\) endpoint; no strict-positivity premise is needed.

Therefore \(\widehat P_\psi\) is PPT across precisely \(Aa\mid Bb\), and is feasible for Eq. (6).

### 4.5 Exact negative objective

Using \(D_k^2=D_k\), \(\operatorname{Tr}D_k=1\), and \(D_k(I-D_k)=0\),

\[
\begin{aligned}
\operatorname{Tr}\!\left((kC\otimes D_k)P_\psi\right)
&=
k\operatorname{Tr}(CQ)\operatorname{Tr}(D_k^2)\\
&\quad+
k\operatorname{Tr}(C)\operatorname{Tr}\!\left(D_k(I-D_k)\right)\\
&=k\lambda.
\end{aligned}
\]

Thus

\[
f_k(\Phi)
\le
\operatorname{Tr}\!\left((kC\otimes D_k)\widehat P_\psi\right)
=
\frac{k\lambda}{1+d^2(k^2-1)}
<0.
\]

The displayed fraction is the **exact objective of this feasible point** and an upper bound on the minimum. It is not asserted to equal the minimum generally. S1 makes this distinction correctly.

### 4.6 CP case and the zero-objective feasible point

If \(C\ge0\), then \(kC\otimes D_k\ge0\), so its trace pairing with every feasible \(P\ge0\) is nonnegative.

For \(k\ge2\), define

\[
P_0=
\frac{I_{AB}\otimes(I_{ab}-D_k)}
{d^2(k^2-1)}.
\]

Its denominator is positive, and it is PSD and trace one. Its partial transpose is

\[
P_0^{T_A T_a}
=
\frac{I_{AB}\otimes(I_{ab}-V_k/k)}
{d^2(k^2-1)}
\ge0,
\]

because the swap has eigenvalues \(\pm1\), giving eigenvalues \(1-1/k\) and \(1+1/k\) in the ancillary factor. Its marginals are maximally mixed density operators, and its objective is zero by \(D_k(I-D_k)=0\).

Therefore \(f_k(\Phi)\le0\) for every Hermiticity-preserving \(\Phi\), and in the CP case the nonnegative lower bound forces

\[
f_k(\Phi)=0.
\]

For completeness, the Choi–CP equivalence here requires no unverified specialized import. CP implies \(C\ge0\) by applying \(\operatorname{id}_d\otimes\Phi\) to the unnormalized maximally entangled projector. Conversely, a positive decomposition \(C=\sum_\ell|w_\ell\rangle\langle w_\ell|\), with
\(w_\ell=\sum_i|i\rangle\otimes K_\ell|i\rangle\), gives
\(\Phi(X)=\sum_\ell K_\ell X K_\ell^\dagger\) by comparison of Choi coefficients.

Combining the two directions proves

\[
\boxed{
f_k(\Phi)\ge0
\iff C(\Phi)\ge0
\iff\Phi\text{ is CP},
}
\]

with \(f_k=0\) exactly in the CP case and \(f_k<0\) otherwise.

### 4.7 Boundary cases

- **\(d=1\):** Here \(Q=1\), so \(P_\psi=I_{k^2}\) and \(Z=k^2\). The PPT and normalization arguments remain valid. The \(P_0\) denominator also remains positive for \(k\ge2\). Thus the classification includes this boundary for the literal SDP expression.
- **\(k=2\):** Both swap sectors are covered by the explicit bounds above. There is no omitted equality case or limiting argument.
- **\(k=1\):** Explicitly excluded. Then \(I_{k^2}-D_k=0\), \(P_0\) is undefined, and the proposed \(P_\psi\) reduces to \(Q\), whose partial transpose need not be PSD. Nothing in the reviewed theorem extends its characterization or CP-zero conclusion to \(k=1\).

## 5. Review of the source-supplied \(d=4,k=2\) example

This is S1’s assigned example, not a newly selected diagnostic.

Let

\[
C=2I_{16}-|\Omega_4\rangle\langle\Omega_4|,
\qquad
|\Omega_4\rangle=\sum_{i=0}^3|ii\rangle.
\]

It is the Choi matrix of the Hermiticity-preserving map
\(\Phi(X)=2\operatorname{Tr}(X)I_4-X\).

For every complex matrix \(X\) of rank at most two,

\[
\langle\operatorname{vec}X|C|\operatorname{vec}X\rangle
=
2\|X\|_F^2-|\operatorname{Tr}X|^2
\ge0.
\]

Indeed, an SVD gives

\[
|\operatorname{Tr}X|
\le\sum_j\sigma_j(X)
\le\sqrt{\operatorname{rank}X}\,
\left(\sum_j\sigma_j(X)^2\right)^{1/2}
\le\sqrt2\,\|X\|_F.
\]

The link to 2-positivity is the standard Choi block-positivity equivalence stated in the primary paper’s Proposition 1. It can also be checked directly: if
\(v=\sum_{a=1}^r|a\rangle x_a\),
\(w=\sum_{a=1}^r|a\rangle y_a\), and
\(z=\sum_{a=1}^r\overline{x_a}\otimes y_a\), then

\[
\langle w|(\operatorname{id}_r\otimes\Phi)(|v\rangle\langle v|)|w\rangle
=
\langle z|C|z\rangle.
\]

For \(r=2\), \(z\) has Schmidt rank at most two; positivity follows on rank-one inputs and then on all PSD inputs. Thus the example is genuinely 2-positive over complex vectors.

For \(\psi=\Omega_4/2\),

\[
C\psi=-2\psi.
\]

The prescribed feasible operator therefore has

\[
Z=1+16(4-1)=49,
\qquad
\operatorname{Tr}\!\left(
C(\Phi\otimes\operatorname{id}_2)\frac{P_\psi}{49}
\right)
=-\frac4{49}.
\]

Also \(Q^{T_A}=V_4/4\). On the original and ancillary swap eigenspaces, with eigenvalues \(\sigma,\tau\in\{+1,-1\}\),

\[
P_\psi^{T_A T_a}
=
I+\left(\frac{V_4}{4}-I\right)\otimes\frac{V_2}{2}
\]

has eigenvalue

\[
1+\left(\frac{\sigma}{4}-1\right)\frac{\tau}{2}.
\]

These are exactly

\[
\frac38,\quad\frac58,\quad\frac{11}{8},\quad\frac{13}{8},
\]

confirming S1’s stated positive spectrum. Thus this 2-positive, non-CP map fails the relaxation’s nonnegative criterion, as claimed.

The feasible state is on \(\mathbb C^8\otimes\mathbb C^8\), not the original \(\mathbb C^4\otimes\mathbb C^4\) target.

## 6. Imports, interpretation, and acceptance boundary

The load-bearing source import is the **literal v2 SDP**, including its independently free density marginals, first-party transpose, and unnormalized Choi convention. The mathematical reconstruction above uses finite-dimensional spectral, Schmidt, and singular-value decompositions; the Choi–CP bridge and the example’s block-positivity bridge are explicitly explained.

The result is stronger information about the written optimization, **not a falsification of the paper’s sufficient implication**. Product density operators belong to the PPT feasible set, so the paper’s inequality

\[
F(\Phi)\le
\min_{\rho,\omega}
\operatorname{Tr}\!\left(
C(\Phi\otimes\operatorname{id}_k)(\rho\otimes\omega)
\right)
\]

and consequent implication \(F(\Phi)\ge0\Rightarrow\Phi\) is \(k\)-positive remain correct. The characterization shows that, for \(k\ge2\), this particular sufficient criterion accepts exactly CP maps. It therefore cannot certify a non-CP 2-positive map.

This review establishes none of the following:

- A defect in the paper’s stated sufficient-condition theorem.
- Impossibility for higher hierarchy levels, additional extension constraints, fixed-marginal formulations, or materially different certificates.
- An actual \(4\times4\) PPT state of Schmidt number at least three, or an unrestricted no-go theorem for that target.
- Exhaustive literature status, priority, or novelty.
- Independent-model-family, human, formal/kernel, or numerical-execution verification.

Parent disposition remains separate from this same-harness written review.

## Findings

None within the frozen §5 mathematical scope: **0 FATAL, 0 MAJOR, 0 MINOR**.

## Overall correctness

**correct**

## Explanation

The candidate correctly identifies the literal free-marginal feasible set and supplies a normalized PPT operator with negative objective for every negative Choi eigenvalue when \(k\ge2\). A separate feasible zero-objective operator proves the CP value is exactly zero, without contradicting the paper’s correct sufficient implication or closing the original \(4\times4\) target.

## Confidence

**0.99**, for the exact written mathematical scope above; not a provenance, novelty, formal-verification, or original-target acceptance certificate.