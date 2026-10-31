# author-candidate-v1.md — Exact exclusion of the Eq. (10) detector family and its small-time semigroups

**Wave:** `f382-ppt44-original-two-positive-detector-or-state-frontier`  
**Status:** **AUTHOR CANDIDATE / UNREVIEWED. No author self-adoption or novelty claim.**  
**Original target:** **NOT CLOSED.**

This manuscript supplies a dimension-matched, exact falsification of a proposed source of genuine \(2\)-positive detectors:

1. The literal \(d=4\) map in arXiv:2508.21348v2, Eq. (10), is **not \(2\)-positive**.
2. For its entire family of nonnegative scalar multiples, arbitrary depolarizing offsets, and arbitrary completely positive complex Schur-map additions, **\(2\)-positivity is equivalent to complete positivity**, with an exact threshold. Consequently, this whole family cannot provide the required detector.
3. Every complex-\(K\) semigroup generated from a member below that threshold fails \(2\)-positivity throughout an explicit initial time interval.
4. For the original seed with \(K=0\), an exact formula proves failure of \(2\)-positivity for
   \[
   0<t\le \frac32\log 2.
   \]

These are direct rank-two and spectral arguments about actual \(4\times4\) maps. They do **not** rely on the free-marginal SDP, a \(4\times5\) embedding, or the already-known separable-compression/SN-\(2\) construction.

---

## 1. Access, chronology, and verification boundary

### Frozen inputs

I read the complete manifest, freeze receipt, and all seven status/permission controls before the scientific packet:

- prospective author-method restoration;
- owner frontier-first addendum;
- L1 diagnostic quarantine;
- privacy-parameter diagnostic quarantine;
- CORE-GRAM diagnostic quarantine;
- AME held-compression consumer quarantine;
- PH held-registration/report-consumer quarantine.

They were used as status and permission controls only. I did not follow their held scientific links or consume the excluded mathematical payloads, report consumers, v8, or cp116.

I then read the ordered scientific packet:

- **S1:** separable-compression/intermediate-state disposition, lines 1–34;
- **S2:** exact free-marginal SDP/CP-collapse disposition, lines 1–33;
- **S3:** complete f362 author return, through its logical line 502.

Three overlong S1/S2 footer lines were initially truncated by the reader. I fetched their complete raw text after the sequential packet pass and before the new primary-source investigation and derivations. Thus, I do not describe the initial display alone as a complete byte-level read.

The following pin matches are **parent-supplied metadata**, not hashes executed by this author:

| Artifact | SHA-256 |
|---|---|
| Manifest | `0019f1619ae6e000dc32e8e20f95376ed10c1caf2f53f6198bfd1d3a3817c86b` |
| Freeze receipt | `2cbf3295723ce317c2590ffa0c216d8dee2292cb633ea9638eebc9a946453f18` |
| Literal packet | `4c445ca73381c7fbdf989a24ded4c79e3d1c4852a132e314c4dc152efe72749f` |

### Public-source access

After the packet read, I inspected the actual public HTML of [vom Ende–Khatri–Denisov, arXiv:2508.21348v2](https://arxiv.org/html/2508.21348v2), specifically:

- the Choi convention and rank-\(k\) characterization in Proposition 1;
- §4.1, Propositions 3–4 and their proofs;
- §4.2, Workflow 1, its seed requirements, Eq. (10), and its positivity footnote.

Bounded web searches were also attempted. They did not establish priority, novelty, exhaustive current status, or an alternative dimension-matched \(2\)-positive nondecomposable seed. Search-result absence is not treated as evidence of novelty.

### Clocks and checkpoints

The parent supplied observations:

- `2026-10-30T10:13:02-0700 PDT`;
- `2026-10-30T10:23:44-0700 PDT`.

Neither is represented as my native start, derivation, or completion time. Substantive checkpoint messages reported the seed counterexample, the full repaired-family theorem, and the semigroup results. The later observation was explicitly supplied by the parent in response to the clock request.

### Execution and materialization

No scientific executable, numerical optimization, random scan, solver, build, installation, external-model CLI, or remote scientific job was run. No working-tree file was written.

The available role restricts execution and working-tree writing. Accordingly:

- the arguments below are **written exact mathematics**;
- the complete optional finite-check source is included in §8;
- its status is **NOT_RUN**;
- no stdout, exit status, measured runtime, or computational PASS is claimed.

This is the complete manuscript for parent materialization, not merely a clock addendum.

---

## 2. Actual target and public-source limitation

Use
\[
\operatorname{vec}(X)=\sum_{i,j=1}^{4}X_{ij}|ij\rangle,
\qquad
C(\Psi)=\sum_{i,j=1}^{4}|i\rangle\langle j|\otimes\Psi(E_{ij}).
\]

The positive target requires an actual state on
\(\mathbb C^4\otimes\mathbb C^4\) satisfying
\[
\rho\ge0,\qquad
\rho^{\Gamma_B}\ge0,\qquad
\operatorname{Tr}\rho=1,
\]
and a Hermitian \(W\) satisfying the **full complex quantifier**
\[
\langle\operatorname{vec}(X)|W|\operatorname{vec}(X)\rangle\ge0
\quad
\text{for every }X\in\mathbb C^{4\times4}
\text{ with }\operatorname{rank}X\le2,
\tag{1}
\]
but
\[
\operatorname{Tr}(W\rho)<0.
\tag{2}
\]

Alternatively, a negative resolution would prove
\[
\operatorname{SN}(\rho)\le2
\quad\text{for every \(4\times4\) PPT state.}
\tag{3}
\]

No pair satisfying (1)–(2), and no theorem (3), is supplied here.

The source’s [Workflow 1](https://arxiv.org/html/2508.21348v2#Thmworkflow1) starts with an **already \(k\)-positive**, nondecomposable seed, with an additional conditional-complete-positivity restriction. It does not manufacture \(k=2\) positivity from a seed known only to be positive.

Moreover, the source explicitly says in its [Eq. (10) discussion and footnote](https://arxiv.org/html/2508.21348v2#S4.E10) that it did not prove even ordinary positivity of that particular \(d=4\) seed; its evidence there is numerical sampling.

The results below do **not** refute the paper’s ordinary-positivity claim or its general semigroup theorem. They refute the additional premise that its displayed \(d=4\) example can simply be used as a genuine \(2\)-positive seed.

---

## 3. Exact Choi structure and the original seed counterexample

### 3.1 Literal source map

In one-based indices, let
\[
\Phi(X)=\frac13
\begin{pmatrix}
x_{11}+x_{22}+x_{33}&x_{12}&x_{13}&x_{14}\\
x_{21}&x_{22}+x_{33}+x_{44}&x_{23}&x_{24}\\
x_{31}&x_{32}&x_{33}+x_{44}+x_{11}&x_{43}\\
x_{41}&x_{42}&x_{34}&x_{44}+x_{11}+x_{22}
\end{pmatrix}.
\tag{4}
\]

Define
\[
\mathcal D=\operatorname{span}\{|11\rangle,|22\rangle,|33\rangle,|44\rangle\},
\qquad
\mathcal B=\operatorname{span}\{|34\rangle,|43\rangle\}.
\]

The Choi matrix is block diagonal across \(\mathcal D\), \(\mathcal B\), and the remaining ten computational basis vectors.

On \(\mathcal D\),
\[
C(\Phi)|_{\mathcal D}=\frac13 M,
\qquad
M=J_4-E_{34}-E_{43},
\tag{5}
\]
where \(J_4\) is the all-ones matrix.

On \(\mathcal B\), in the order \((34,43)\),
\[
C(\Phi)|_{\mathcal B}
=\frac13
\begin{pmatrix}
0&1\\
1&1
\end{pmatrix}.
\tag{6}
\]

For the other off-diagonal product kets \(|ij\rangle\), \(i\ne j\), the diagonal weight is \(0\) when \(j=i+1\pmod4\), and \(1/3\) otherwise. There are no additional couplings.

These statements follow directly by applying (4) to every \(E_{ij}\). In particular, the swapped \(34/43\) entries produce the off-diagonal coupling in (6); they must not be read as ordinary identity-map coherences on \(\mathcal D\).

### 3.2 An elementary rank-two counterexample

Take
\[
\psi=|34\rangle-|43\rangle.
\]
Its coefficient matrix has rank exactly \(2\), and
\[
\langle\psi|C(\Phi)|\psi\rangle
=\frac13(0+1-2)
=-\frac13.
\tag{7}
\]

Thus \(\Phi\) is **not \(2\)-positive**.

This is an exact violation of the required rank-\(\le2\) quantifier. It is not a finite search intended to infer universal positivity.

For later use, put
\[
q=\frac{\sqrt5-1}{2},
\qquad
r=\frac q3=\frac{\sqrt5-1}{6},
\qquad
\eta=\frac{|34\rangle-q|43\rangle}{\sqrt{1+q^2}}.
\tag{8}
\]
Since \(q^2=1-q\), equation (6) gives
\[
C(\Phi)\eta=-r\eta.
\tag{9}
\]
The vector \(\eta\) has Schmidt rank \(2\) and is orthogonal to
\[
\Omega=\sum_{i=1}^4|ii\rangle.
\tag{10}
\]

---

## 4. Whole-family theorem: noise and arbitrary CP Schur additions do not produce a detector

### Theorem 1 — Exact \(2\)-positivity/CP threshold

Let

- \(\lambda\ge0\);
- \(\delta\in\mathbb R\);
- \(S\in M_4(\mathbb C)\) be any positive semidefinite Hermitian matrix;
- \(\Delta(X)=\operatorname{Tr}(X)I_4\);
- \(\mathcal M_S(X)=S\circ X\), the Schur multiplier.

Define
\[
\Psi_{\lambda,\delta,S}
=\lambda\Phi+\delta\Delta+\mathcal M_S.
\tag{11}
\]

Then
\[
\boxed{
\Psi_{\lambda,\delta,S}\text{ is \(2\)-positive}
\iff
\Psi_{\lambda,\delta,S}\text{ is CP}
\iff
\delta\ge\lambda\frac{\sqrt5-1}{6}.
}
\tag{12}
\]

The assertion includes arbitrary complex \(S\ge0\), singular \(S\), \(\lambda=0\), and negative \(\delta\).

### Proof: necessity from a genuine rank-two vector

The Choi matrix of \(\mathcal M_S\) is supported entirely on \(\mathcal D\), where it equals \(S\). Also,
\[
C(\Delta)=I_{16}.
\]

Consequently the \(\mathcal B\) block of (11) is
\[
B_{\lambda,\delta}
=
\begin{pmatrix}
\delta&\lambda/3\\
\lambda/3&\delta+\lambda/3
\end{pmatrix}.
\tag{13}
\]

The vector \(\eta\) from (8) remains an eigenvector, independently of \(S\), with
\[
\langle\eta|C(\Psi_{\lambda,\delta,S})|\eta\rangle
=\delta-\lambda r.
\tag{14}
\]

If \(\delta<\lambda r\), this is negative on a complex Schmidt-rank-\(2\) vector. Therefore \(2\)-positivity requires
\[
\delta\ge\lambda r.
\tag{15}
\]

This necessity is not obtained from a CP relaxation: it directly tests the actual rank-two condition.

### Proof: the same threshold makes the entire Choi matrix PSD

Assume (15). Since \(\lambda\ge0\), it follows that \(\delta\ge0\).

The eigenvalues of the \(\mathcal B\) block are
\[
\delta+\lambda\frac{1\pm\sqrt5}{6},
\]
so that block is PSD.

All remaining off-diagonal product-ket blocks are scalar:
\[
\delta
\quad\text{or}\quad
\delta+\lambda/3,
\]
hence nonnegative.

It remains to check the full \(\mathcal D\) block
\[
H=\delta I_4+\frac{\lambda}{3}M+S.
\tag{16}
\]

The spectrum of \(M\) is
\[
\left\{
0,\ 1,\ \frac{3-\sqrt{17}}2,\ \frac{3+\sqrt{17}}2
\right\}.
\tag{17}
\]

Indeed:

- \((1,-1,0,0)\) has eigenvalue \(0\);
- \((0,0,1,-1)\) has eigenvalue \(1\);
- on the orthonormal basis
  \[
  \frac{(1,1,0,0)}{\sqrt2},
  \quad
  \frac{(0,0,1,1)}{\sqrt2},
  \]
  the remaining block is
  \[
  \begin{pmatrix}2&2\\2&1\end{pmatrix}.
  \]

The threshold needed for \(\delta I+\lambda M/3\ge0\) is therefore
\[
\delta\ge\lambda\frac{\sqrt{17}-3}{6}.
\tag{18}
\]

But
\[
\frac{\sqrt5-1}{6}>
\frac{\sqrt{17}-3}{6},
\tag{19}
\]
because \(\sqrt5+2>\sqrt{17}\), equivalently \(\sqrt5>2\).

Thus (15) implies (18). Adding arbitrary complex \(S\ge0\) preserves positivity. Hence every block of \(C(\Psi_{\lambda,\delta,S})\) is PSD, proving complete positivity.

CP implies \(2\)-positivity, completing the equivalences. ∎

### Consequence for the original target

Every member of (11) that satisfies the genuine rank-two detector requirement is already PSD as a Choi matrix. Therefore it has nonnegative pairing with **every** positive state:
\[
\operatorname{Tr}\bigl(C(\Psi_{\lambda,\delta,S})\rho\bigr)\ge0
\qquad(\rho\ge0).
\tag{20}
\]

It cannot provide (2), even before imposing PPT.

This excludes, in particular:

- white-noise repair of the displayed source seed;
- adding any nonnegative multiple of the identity map, since its Schur matrix is a nonnegative multiple of \(J_4\);
- adding any collection of diagonal Kraus-operator CP maps;
- arbitrary combinations of those repairs.

### Invertible local filtering

The same exclusion holds for every invertible local congruence
\[
W'=(A\otimes B)\,C(\Psi_{\lambda,\delta,S})\,(A\otimes B)^\dagger,
\qquad A,B\in GL_4(\mathbb C).
\tag{21}
\]

Invertible local transformations preserve Schmidt rank, and congruence in both directions preserves PSD. Below threshold, the transformed vector
\[
\bigl((A^\dagger)^{-1}\otimes(B^\dagger)^{-1}\bigr)\eta
\]
still has Schmidt rank \(2\) and negative expectation. At or above threshold, \(W'\ge0\).

No corresponding statement is made for arbitrary noninvertible filters or arbitrary additional CP perturbations outside the Schur class.

### Exact written selected controls

These are hand-derived exact controls, **not executed experiments**:

- With \(\lambda=1,\delta=1/5\), for every \(S\ge0\),
  \[
  v=|34\rangle-\frac35|43\rangle
  \quad\Longrightarrow\quad
  \langle v|C(\Psi_{1,1/5,S})|v\rangle=-\frac1{125}.
  \tag{22}
  \]
- With \(\lambda=1,\delta=5/24\), the pair-block determinant is
  \[
  \det B_{1,5/24}=\frac1{576}>0.
  \tag{23}
  \]
  Moreover \(5/24>r\), since \(9>4\sqrt5\), so the whole family is on the CP side.

---

## 5. Every complex-\(K\) generator: CP trajectory or initial failure of \(2\)-positivity

The source workflow permits an arbitrary complex matrix \(K\). The seed defect cannot be repaired merely by that choice.

### Theorem 2 — Quantitative initial-time dichotomy

Under the hypotheses of Theorem 1, let
\[
L_K(X)=KX+XK^\dagger+\Psi_{\lambda,\delta,S}(X),
\qquad K\in M_4(\mathbb C).
\tag{24}
\]

Then:

1. If \(\delta\ge\lambda r\), \(e^{tL_K}\) is CP for every \(t\ge0\).
2. If \(\delta<\lambda r\), \(e^{tL_K}\) is not \(2\)-positive for every
   \[
   0<t\le\tau,
   \tag{25}
   \]
   where
   \[
   a=\lambda r-\delta>0,
   \]
   \[
   M=2\|K\|_{\mathrm{op}}+\lambda+4|\delta|+\max_i S_{ii},
   \]
   and
   \[
   \tau=\min\left\{\frac1M,\frac{a}{12M^2}\right\}>0.
   \tag{26}
   \]

### Proof of the CP case

Theorem 1 makes \(\Psi_{\lambda,\delta,S}\) CP.

The map
\[
e^{t(K(\cdot)+(\cdot)K^\dagger)}
\]
is conjugation by \(e^{tK}\), hence CP. The exponential of a CP map is also CP: its power series is a norm limit of positive linear combinations of compositions of CP maps, including the identity map.

The Lie–Trotter product formula therefore makes \(e^{tL_K}\) CP. This is the standard CP-semigroup mechanism also used in the source’s [Proposition 3](https://arxiv.org/html/2508.21348v2#Thmproposition3).

### Proof of the initial rank-two violation

For \(v_K=(I\otimes K)\Omega\),
\[
C(K(\cdot)+(\cdot)K^\dagger)
=|v_K\rangle\langle\Omega|
 +|\Omega\rangle\langle v_K|.
\tag{27}
\]

Since \(\eta\perp\Omega\),
\[
\langle\eta|C(L_K)|\eta\rangle
=\delta-\lambda r=-a.
\tag{28}
\]
Also
\[
\langle\eta|C(\operatorname{id})|\eta\rangle=0.
\]

Thus the first derivative is negative for **every complex \(K\)**. For completeness, the following bound makes the time interval explicit.

Use the norm induced by the Hilbert–Schmidt norm on \(M_4\). We have
\[
\|\Phi\|_{2\to2}=1,\qquad
\|\Delta\|_{2\to2}=4,\qquad
\|\mathcal M_S\|_{2\to2}=\max_i S_{ii}.
\tag{29}
\]

For the first identity, the diagonal sector is the normal circulant matrix \((J-P)/3\), whose eigenvalues have moduli \(1,1/3,1/3,1/3\); the off-diagonal sector is \(1/3\) times a permutation. Here \(P\) is the cyclic forward shift. The Schur identity follows from \(S\ge0\), which gives \(|S_{ij}|\le\max_i S_{ii}\).

Hence \(\|L_K\|_{2\to2}\le M\).

Let
\[
R_t=e^{tL_K}-\operatorname{id}-tL_K.
\]
Then
\[
\|R_t\|_{2\to2}
\le \frac{t^2M^2}{2}e^{tM}.
\tag{30}
\]

Choi reshuffling preserves the Frobenius norm, and a \(16\times16\) matrix has Frobenius norm at most four times its operator norm. Consequently
\[
\|C(R_t)\|_{\mathrm{op}}
\le4\|R_t\|_{2\to2}.
\tag{31}
\]

Equations (28)–(31) imply
\[
\langle\eta|C(e^{tL_K})|\eta\rangle
\le -at+2t^2M^2e^{tM}.
\tag{32}
\]

For \(t\le1/M\), use \(e^{tM}\le e<3\). For \(t\le a/(12M^2)\), the remainder is at most \(at/2\). Therefore
\[
\langle\eta|C(e^{tL_K})|\eta\rangle
\le-\frac{at}{2}<0
\]
throughout (25). The testing vector has Schmidt rank \(2\). ∎

### Exact boundary of this theorem

This is an initial-time result, not a statement about every later time.

A trajectory below threshold could conceivably enter the \(2\)-positive cone later while still outside CP. Establishing that—and establishing nondecomposability with a genuine PPT negative pairing—requires additional proof. Neither the source’s ordinary-positivity numerics nor Theorem 2 supplies it.

---

## 6. Exact longer interval for the source trajectory \(e^{t\Phi}\)

For the original source seed and \(K=0\), a direct exponential calculation gives a substantially longer explicit exclusion interval.

### Theorem 3

For the literal map (4),
\[
\boxed{
e^{t\Phi}\text{ is not \(2\)-positive whenever }
0<t\le\frac32\log2.
}
\tag{33}
\]

### Proof

Put \(u=t/3\).

On diagonal matrices, \(3\Phi\) is represented by
\[
A=J_4-P,
\]
where \(P e_i=e_{i+1}\), cyclically. Since \(J_4\) and \(P\) commute,
\[
e^{uA}
=e^{-uP}+\frac{e^{3u}-e^{-u}}4J_4.
\tag{34}
\]

In particular, the forward and backward transition coefficients are
\[
p_-=\frac{e^{3u}-e^u-2\sin u}{4},
\qquad
p_+=\frac{e^{3u}-e^u+2\sin u}{4}.
\tag{35}
\]

On the special off-diagonal pair,
\[
e^{t\Phi}(E_{34})
=\cosh u\,E_{34}+\sinh u\,E_{43},
\]
and analogously with \(34\) and \(43\) interchanged.

Thus the Choi block on \(\mathcal B\) is
\[
B_t=
\begin{pmatrix}
p_-&\sinh u\\
\sinh u&p_+
\end{pmatrix}.
\tag{36}
\]

Its determinant simplifies exactly:
\[
\begin{aligned}
\det B_t
&=\frac{(e^{3u}-e^u)^2-4\sin^2u}{16}-\sinh^2u\\
&=\frac{(e^{4u}-4)\sinh^2u-\sin^2u}{4}.
\end{aligned}
\tag{37}
\]

If \(0<u\le(\log2)/2\), then \(e^{4u}\le4\) and \(\sin u>0\), so
\[
\det B_t<0.
\tag{38}
\]

An explicit negative rank-two vector is also available. The matrix \(A\) is entrywise nonnegative, and
\[
A^2=2J_4+P^2.
\]
Therefore the forward transition coefficient satisfies \(p_-\ge u^2>0\). Set
\[
z_t=\sinh u\,|34\rangle-p_-|43\rangle.
\tag{39}
\]
Both displayed coefficients are nonzero, so its coefficient matrix has rank \(2\), and
\[
\langle z_t|C(e^{t\Phi})|z_t\rangle
=p_-\det B_t<0.
\tag{40}
\]

Since \(t=3u\), this proves (33). ∎

This interval contains the source’s numerically discussed small-time \(d=4\) region. The conclusion is only that those maps fail the **\(k=2\)** requirement. It neither establishes nor refutes their ordinary positivity or the source’s numerical nondecomposability observations.

---

## 7. Contribution, prior-public material, and unpaid steps

| Claim | Classification | Boundary |
|---|---|---|
| Choi rank-\(k\) characterization | Prior public | Source Proposition 1; not advertised as new science |
| Workflow requires an already \(k\)-positive seed | Prior public, actually read | Its displayed \(d=4\) example cannot simply be presumed \(2\)-positive |
| Eq. (10) fails \(2\)-positivity | Exact written author proof, unreviewed | Equation (7), actual \(4\times4\), rank-two violation |
| Entire noise-plus-complex-CP-Schur family has \(2\)-positive cone equal to CP cone | Exact written author proof, unreviewed | All parameters and all complex PSD Schur matrices in Theorem 1 |
| Arbitrary complex-\(K\) initial-time failure | Exact written author proof, unreviewed | Explicit interval only; later times unpaid |
| \(K=0\) failure on \(0<t\le(3/2)\log2\) | Exact written author proof, unreviewed | Analytic interval, not a numerical scan |
| Selected rational controls | Written exact finite identities | Not executed |
| Optional replay program | NOT_RUN | No computational verification claimed |
| Novelty or priority | Unresolved | Bounded searches are insufficient |
| Actual \(4\times4\) PPT/SN-\(\ge3\) state–detector pair | Not obtained | Original positive target remains open in this return |
| All-\(4\times4\)-PPT SN-\(\le2\) theorem | Not obtained | No unrestricted obstruction claimed |

### What this removes

The source’s actual \(d=4\) seed, its entire depolarizing-plus-CP-Schur repair family, their invertible local-filter orbits, and the specified initial semigroup regimes cannot supply the required genuine rank-two detector.

This is a new calculation in this return, **not a claim of literature novelty**. It is not a restatement of the earlier separable-core lemma or the free-marginal SDP collapse.

### Precise unpaid scientific obligations

For full closure, one still needs either:

- an actual \(4\times4\) PPT state and a globally complex-rank-\(\le2\)-nonnegative detector with negative pairing; or
- a proof covering every \(4\times4\) PPT state.

For later-time semigroups outside the affine family of Theorem 1, the missing steps remain:

1. a genuine global \(2\)-positivity certificate, not random testing;
2. a nondecomposability/PPT-negative-pairing certificate;
3. exact dimension matching and normalization.

The nonseparable-\(3\times4\)-core route is not resolved here.

All new author claims require a disjoint check and a separate parent disposition. No human, independent-model-family, formal/kernel, exhaustive-literature, or novelty acceptance is claimed.

---

## 8. Optional exact finite replay — complete source, NOT_RUN

**Proposed filename:** `f382-eq10-exact-check-v1.py`  
**Proposed argv:** `python3 f382-eq10-exact-check-v1.py`  
**Execution status:** **NOT_RUN.**

The program uses only Python’s standard library, performs no file or network writes, and has a cooperative 55-second guard. Its checks are finite corroboration of transcription, block identities, selected controls, and the first thirteen Taylor-coefficient matrices. They do **not** replace the universal written proofs.

Each inline-code line below is one literal source line, in sequence; omit the delimiting backticks when materializing. Blank lines are optional.

`from fractions import Fraction as Q`  
`from itertools import combinations`  
`from time import monotonic`  
`started = monotonic()`  
`def require(ok, message):`  
`  if not ok:`  
`    raise RuntimeError(message)`  
`  if monotonic() - started > 55:`  
`    raise RuntimeError("INCOMPLETE: cooperative deadline reached")`  
`def zero(n):`  
`  return [[Q(0) for _ in range(n)] for _ in range(n)]`  
`def eye(n):`  
`  A = zero(n)`  
`  for i in range(n):`  
`    A[i][i] = Q(1)`  
`  return A`  
`def unit(i, j):`  
`  A = zero(4)`  
`  A[i][j] = Q(1)`  
`  return A`  
`def scale(A, s):`  
`  return [[s * x for x in row] for row in A]`  
`def multiply(A, B):`  
`  n = len(A)`  
`  return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]`  
`def charpoly(A):`  
`  n = len(A)`  
`  B = eye(n)`  
`  coefficients = [Q(1)]`  
`  for k in range(1, n + 1):`  
`    AB = multiply(A, B)`  
`    c = -sum(AB[i][i] for i in range(n)) / k`  
`    coefficients.append(c)`  
`    B = [[AB[i][j] + (c if i == j else Q(0)) for j in range(n)] for i in range(n)]`  
`  return coefficients`  
`def determinant(A):`  
`  if not A:`  
`    return Q(1)`  
`  return (-1) ** len(A) * charpoly(A)[-1]`  
`def submatrix(A, indices):`  
`  return [[A[i][j] for j in indices] for i in indices]`  
`def psd_by_principal_minors(A):`  
`  n = len(A)`  
`  for size in range(1, n + 1):`  
`    for indices in combinations(range(n), size):`  
`      if determinant(submatrix(A, indices)) < 0:`  
`        return False`  
`  return True`  
`def phi(A):`  
`  B = [row[:] for row in A]`  
`  for i in range(4):`  
`    B[i][i] = sum(A[j][j] for j in range(4) if j != (i - 1) % 4)`  
`  B[2][3] = A[3][2]`  
`  B[3][2] = A[2][3]`  
`  return scale(B, Q(1, 3))`  
`def depolarizing(A):`  
`  return scale(eye(4), sum(A[i][i] for i in range(4)))`  
`def repaired(A, S, delta):`  
`  B = phi(A)`  
`  tr = sum(A[i][i] for i in range(4))`  
`  return [[B[i][j] + S[i][j] * A[i][j] + (delta * tr if i == j else Q(0)) for j in range(4)] for i in range(4)]`  
`def choi_images(images):`  
`  C = zero(16)`  
`  for i in range(4):`  
`    for j in range(4):`  
`      Y = images[4 * i + j]`  
`      for a in range(4):`  
`        for b in range(4):`  
`          C[4 * i + a][4 * j + b] = Y[a][b]`  
`  return C`  
`def choi(operation):`  
`  return choi_images([operation(unit(i, j)) for i in range(4) for j in range(4)])`  
`def quadratic(C, v):`  
`  return sum(v[i] * C[i][j] * v[j] for i in range(16) for j in range(16))`  
`D = [0, 5, 10, 15]`  
`Bpair = [11, 14]`  
`omega = [Q(int(i in D)) for i in range(16)]`  
`expected_identity_choi = [[omega[i] * omega[j] for j in range(16)] for i in range(16)]`  
`require(choi(lambda A: A) == expected_identity_choi, "known-true identity Choi convention failed")`  
`require(choi(depolarizing) == eye(16), "known-true depolarizing Choi convention failed")`  
`M = [[Q(1) for _ in range(4)] for _ in range(4)]`  
`M[2][3] = M[3][2] = Q(0)`  
`require(charpoly(M) == [Q(1), Q(-4), Q(1), Q(2), Q(0)], "M characteristic polynomial mismatch")`  
`require(charpoly([[Q(0), Q(1)], [Q(1), Q(1)]]) == [Q(1), Q(-1), Q(-1)], "pair characteristic polynomial mismatch")`  
`C = choi(phi)`  
`expected = zero(16)`  
`for i in range(4):`  
`  for j in range(4):`  
`    expected[5 * i][5 * j] = M[i][j] / 3`  
`    if i != j:`  
`      expected[4 * i + j][4 * i + j] = Q(int(j != (i + 1) % 4), 3)`  
`expected[11][14] = expected[14][11] = Q(1, 3)`  
`require(C == expected, "literal Eq10 Choi block decomposition mismatch")`  
`simple = [Q(0) for _ in range(16)]`  
`simple[11], simple[14] = Q(1), Q(-1)`  
`require(quadratic(C, simple) == Q(-1, 3), "original rank-two counterexample mismatch")`  
`u = [Q(1), Q(2), Q(-1), Q(0)]`  
`v = [Q(0), Q(1), Q(1), Q(2)]`  
`Sgram = [[u[i] * u[j] + v[i] * v[j] for j in range(4)] for i in range(4)]`  
`require(psd_by_principal_minors(Sgram), "selected Schur Gram matrix failed PSD check")`  
`test_vector = [Q(0) for _ in range(16)]`  
`test_vector[11], test_vector[14] = Q(1), Q(-3, 5)`  
`for S in [zero(4), Sgram]:`  
`  negative = choi(lambda A: repaired(A, S, Q(1, 5)))`  
`  require(quadratic(negative, test_vector) == Q(-1, 125), "selected negative noise control mismatch")`  
`  positive = choi(lambda A: repaired(A, S, Q(5, 24)))`  
`  H = submatrix(positive, D)`  
`  P = submatrix(positive, Bpair)`  
`  require(determinant(P) == Q(1, 576), "selected positive pair determinant mismatch")`  
`  require(psd_by_principal_minors(H), "selected positive correlated block failed")`  
`  require(psd_by_principal_minors(P), "selected positive pair block failed")`  
`  for a in range(16):`  
`    if a not in D and a not in Bpair:`  
`      require(positive[a][a] >= 0, "selected scalar block is negative")`  
`    for b in range(16):`  
`      same_block = (a in D and b in D) or (a in Bpair and b in Bpair)`  
`      if a != b and not same_block:`  
`        require(positive[a][b] == 0, "unexpected coupling between Choi blocks")`  
`images = [unit(i, j) for i in range(4) for j in range(4)]`  
`for n in range(13):`  
`  actual = choi_images(images)`  
`  sin_derivative = (0, 1, 0, -1)[n % 4]`  
`  cos_derivative = (1, 0, -1, 0)[n % 4]`  
`  population = [`  
`    Q(3 ** n + 1 + 2 * cos_derivative, 4),`  
`    Q(3 ** n - 1 - 2 * sin_derivative, 4),`  
`    Q(3 ** n + 1 - 2 * cos_derivative, 4),`  
`    Q(3 ** n - 1 + 2 * sin_derivative, 4),`  
`  ]`  
`  predicted = zero(16)`  
`  for i in range(4):`  
`    for j in range(4):`  
`      predicted[4 * i + j][4 * i + j] = population[(j - i) % 4]`  
`      if i != j:`  
`        special = {i, j} == {2, 3}`  
`        predicted[5 * i][5 * j] = Q(int(n % 2 == 0)) if special else Q(1)`  
`  predicted[11][14] = predicted[14][11] = Q(n % 2)`  
`  require(actual == predicted, "semigroup derivative matrix mismatch at order " + str(n))`  
`  if n < 12:`  
`    images = [scale(phi(A), Q(3)) for A in images]`  
`require(True, "final cooperative deadline check")`  
`print("Exact finite controls and coefficient checks through order 12 passed.")`  
`print("Selected negative quadratic: -1/125")`  
`print("Selected positive pair determinant: 1/576")`  
`print("These finite checks do not prove the universal theorems or the original PPT/SN3 target.")`

**No output from this program has been observed.**

---

**Final author disposition:** The unrestricted original \(4\times4\) PPT/SN-\(\ge3\) problem remains unresolved. This return instead provides a self-contained, exact exclusion of a concrete public-seed detector family and its specified small-time semigroup routes, with all complex rank-two quantifiers respected, no substitution of the earlier known SN-\(2\) family, and no scientific adoption or novelty claim.