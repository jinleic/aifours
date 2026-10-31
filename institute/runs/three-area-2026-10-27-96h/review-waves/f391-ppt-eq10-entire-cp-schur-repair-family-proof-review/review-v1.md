# F391 — Written review of the Eq. (10) CP-Schur repair family

**Role:** WRITTEN  
**Reviewed scope:** Theorem 1 and §§2–4 of S1, including the literal-map reconstruction, rank-two counterexample, entire repair-family threshold, nonsingular local-filter corollary, and the two supplied rational controls.  
**Reviewer result:** **SUPPORTED at this exact scope.**  
**Findings:** **0 FATAL / 0 MAJOR / 0 MINOR.**  
**Acceptance status:** **UNREVIEWED pending separate parent disposition.** This return does not itself adopt the candidate.

This is the complete review body for parent materialization as the wave’s `review-v1.md`. No working-tree write or filesystem/execution bypass was performed.

## 1. Inputs, read coverage, and method

### Frozen inputs

The controlling manifest is:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f391-ppt-eq10-entire-cp-schur-repair-family-proof-review/manifest-v1.json`

- Manifest SHA-256: `e8917876d91e96edfc06767a1aa1828f7f673794759d89262e32be88cca72827`
- Freeze-receipt SHA-256: `512b2119d5952b010888489126160d79d6f838208b8fc6a52bba3773b68f030a`
- Literal-packet SHA-256: `e1eddb83568214b2f40b672fd7c1eee3d70c1fed25d19f3127d1e43271741286`

Mathematical inputs were exactly:

1. **S1:** `review-waves/f382-ppt44-original-two-positive-detector-or-state-frontier/review-v1.md`
   - Whole-file SHA-256: `1365bde68234dff06aabd798acd0c740040e6560abb3da708404af43dad99dd6`
   - Parent-supplied whole-file metadata: 28,388 bytes, 823 LF.
   - **Allowed and read:** LF1–663 only.
   - The authored checker and excluded suffix were not read or used.

2. **S2:** `source-screens/f382-public-equation10-and-workflow-reader-excerpt-v1.md`
   - SHA-256: `2f9fb815902e8271bc04f927c5e8aa7c68fbb55e4344c36401553083c66ee1ba`
   - Parent-supplied metadata: 10,366 bytes, 66 LF.
   - **Allowed and read:** LF1–66, complete.
   - Public-source URL: https://arxiv.org/html/2508.21348v2
   - This is the frozen rendered-reader excerpt, not independently fetched original HTML or a complete-paper read.

The hashes, byte counts, LF counts, and their live agreement are **parent-supplied metadata**, not hashes or measurements executed by this reviewer.

### Read order and exclusions

Before any mathematical packet read, I completely read:

- Manifest LF1–89;
- Freeze receipt LF1–47;
- All seven listed controls, including their endings: frontier-first addendum, L1 quarantine, written-duty deviations, PH-consumer quarantine, AME-consumer quarantine, CORE-GRAM quarantine, and privacy-parameter quarantine;
- Parent live-metadata supply LF1–80.

I then sent a direct administrative pre-body ACK to Main. Only afterward did I read the **entire ordered literal packet, LF1–731**, sequentially in raw windows of at most 20 LF, including both source endings, before deriving the mathematics below.

S2 LF66 advertises additional material outside the retained URL excerpt. That is not an omitted portion of the frozen packet; I did not follow it or claim to have read the whole paper.

All historical held payloads and their consumers remained NONINPUT. No linked held scientific body, current sibling outcome, or authored checker was consulted.

### Execution and clocks

This review used written symbolic reconstruction only:

- No scientific code, CAS, interpreter, solver, enumeration, replay, numerical test, or new selected-instance probe;
- No build, lint, test, formatter, installation, external-model CLI, paid run, remote job, deletion, commit, push, or publication;
- The supplied rational examples were audited as **source-provided claims**, not adopted as evidence without derivation.

A substantive checkpoint was delivered after the complete packet read and reconstruction.

The last received fresh clock was **the parent’s actual `/bin/date` observation, `2026-10-30T10:39:00-0700 PDT`**. The earlier parent observation was `2026-10-30T10:34:20-0700 PDT`. Neither is represented as this reviewer’s native start, derivation, or completion time. No independently observed reviewer completion time or continuous-runtime claim is made.

## 2. Claimwise disposition

| Claim | Source LF | Reviewer disposition |
|---|---|---|
| Literal Eq. (10), all 16 matrix-unit images, Choi blocks and zero locations | S1 LF89–94, 139–181; S2 LF53–58 | **SUPPORTED** |
| The seed fails 2-positivity on the stated rank-two vector | S1 LF185–199 | **SUPPORTED** |
| The normalized \(\eta\) has Schmidt rank two and eigenvalue \(-(\sqrt5-1)/6\) | S1 LF201–218 | **SUPPORTED** |
| For every \(\lambda\ge0\), real \(\delta\), and complex Hermitian \(S\ge0\), 2-positivity iff CP iff \(\delta\ge\lambda r\) | S1 LF225–352 | **SUPPORTED** |
| The result includes \(\lambda=0\), singular \(S\), negative offsets, and threshold equality | S1 LF229–254 and proof | **SUPPORTED** |
| No hidden Schur contribution acts outside \(\mathcal D\) | S1 LF258–277, 307–350 | **SUPPORTED** |
| The family cannot provide the required negative state pairing when it satisfies the rank-two condition | S1 LF354–370 | **SUPPORTED**, restricted to this family |
| Invertible local-filter corollary | S1 LF372–387 | **SUPPORTED**, nonsingular filters only |
| Both supplied rational controls | S1 LF389–405 | **SUPPORTED by written identities**, not executed |
| Workflow requires an already \(k\)-positive seed; Eq. (10)’s positivity evidence is ordinary-positivity sampling | S1 LF126–130; S2 LF17–34, 58–59 | **SUPPORTED as the frozen source’s content** |
| Ordinary positivity of Eq. (10) for all inputs | S2 LF58 | **INCONCLUSIVE in this review**; neither proved nor refuted |
| Semigroup Theorems 2–3 | S1 LF409–619 | **Outside audited scope; no verdict adopted** |
| Novelty or priority | S1 LF635, 643, 660 | **INCONCLUSIVE; not established** |
| A \(4\times4\) PPT/SN-\(\ge3\) state–detector pair, or an unrestricted PPT/SN-\(\le2\) theorem | S1 LF96–124, 645–658 | **Not established; original target remains open** |

No claim in the audited theorem required a REFUTED disposition.

## 3. Conventions and all 16 matrix-unit images

Let \(E_{ij}=|i\rangle\langle j|\), and retain the candidate’s exact conventions:

\[
\operatorname{vec}(X)=\sum_{i,j}X_{ij}|ij\rangle,
\qquad
C(\Theta)=\sum_{i,j}E_{ij}\otimes\Theta(E_{ij}).
\]

The literal source map is

\[
\Phi(X)=\frac13
\begin{pmatrix}
x_{11}+x_{22}+x_{33}&x_{12}&x_{13}&x_{14}\\
x_{21}&x_{22}+x_{33}+x_{44}&x_{23}&x_{24}\\
x_{31}&x_{32}&x_{33}+x_{44}+x_{11}&x_{43}\\
x_{41}&x_{42}&x_{34}&x_{44}+x_{11}+x_{22}
\end{pmatrix}.
\]

This agrees with S2 LF55, including the swapped \(34/43\) entries.

Applying this definition to every matrix unit gives the following complete table. The entry in row \(i\), column \(j\) is \(3\Phi(E_{ij})\):

| \(i\backslash j\) | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| 1 | \(E_{11}+E_{33}+E_{44}\) | \(E_{12}\) | \(E_{13}\) | \(E_{14}\) |
| 2 | \(E_{21}\) | \(E_{11}+E_{22}+E_{44}\) | \(E_{23}\) | \(E_{24}\) |
| 3 | \(E_{31}\) | \(E_{32}\) | \(E_{11}+E_{22}+E_{33}\) | \(E_{43}\) |
| 4 | \(E_{41}\) | \(E_{42}\) | \(E_{34}\) | \(E_{22}+E_{33}+E_{44}\) |

Thus all 16 Choi blocks, not merely selected coherences, have been accounted for.

### Why the complex rank-two condition is the relevant one

For completeness, the Choi characterization can be obtained without importing an unread proposition.

For arbitrary \(x_a,y_a\in\mathbb C^4\), let

\[
z=\sum_{a=1}^{k}x_a\otimes y_a,\quad
u=\sum_{a=1}^{k}|a\rangle\otimes\overline{x_a},\quad
v=\sum_{a=1}^{k}|a\rangle\otimes y_a.
\]

Direct expansion with the stated Choi convention gives

\[
\langle z,C(\Theta)z\rangle
=
\left\langle v,
(\operatorname{id}_k\otimes\Theta)(|u\rangle\langle u|)
v\right\rangle.
\]

Every vector of Schmidt rank at most \(k\) admits the displayed decomposition, and \(u,v\) range over arbitrary corresponding vectors. Positivity on all rank-one positive inputs extends to all positive inputs by spectral decomposition. Therefore

\[
\Theta\text{ is \(k\)-positive}
\iff
\langle z,C(\Theta)z\rangle\ge0
\quad\text{for every complex }z\text{ of Schmidt rank }\le k.
\]

Also, \(C(\Theta)\ge0\) is equivalent to complete positivity: a positive spectral factorization of \(C(\Theta)\) reshapes into Kraus vectors \((I\otimes K_\alpha)\Omega\), and conversely Kraus maps have such a positive Choi factorization.

The theorem uses the standard **inclusive** cone convention: CP maps are \(2\)-positive. The source’s additional convention that “\(k\)-positive” implicitly excludes CP, stated in S2 LF9, must not be substituted into the theorem’s equivalence.

## 4. Complete Choi block decomposition

Define

\[
\mathcal D=\operatorname{span}\{|11\rangle,|22\rangle,|33\rangle,|44\rangle\},
\qquad
\mathcal B=\operatorname{span}\{|34\rangle,|43\rangle\}.
\]

The ordinary off-diagonal matrix-unit images contribute

\[
E_{ij}\otimes E_{ij}=|ii\rangle\langle jj|.
\]

The two exceptional images contribute instead

\[
E_{34}\otimes E_{43}=|34\rangle\langle43|,
\qquad
E_{43}\otimes E_{34}=|43\rangle\langle34|.
\]

Consequently, on \(\mathcal D\),

\[
C(\Phi)|_{\mathcal D}=\frac13M,\qquad
M=
\begin{pmatrix}
1&1&1&1\\
1&1&1&1\\
1&1&1&0\\
1&1&0&1
\end{pmatrix}
=J_4-E_{34}-E_{43}.
\]

On \(\mathcal B\), ordered as \((34,43)\),

\[
C(\Phi)|_{\mathcal B}
=\frac13T,\qquad
T=\begin{pmatrix}0&1\\1&1\end{pmatrix}.
\]

The four zero diagonal locations in the full computational basis are exactly

\[
|12\rangle,\quad |23\rangle,\quad |34\rangle,\quad |41\rangle.
\]

The first, second, and fourth of these are scalar zero blocks. The third belongs to the coupled block \(\mathcal B\), whose other diagonal entry, at \(|43\rangle\), is \(1/3\).

The remaining seven scalar blocks, each of weight \(1/3\), are

\[
|13\rangle,\ |14\rangle,\ |21\rangle,\ |24\rangle,\
|31\rangle,\ |32\rangle,\ |42\rangle.
\]

This accounts for dimensions \(4+2+3+7=16\), with no omitted coupling.

## 5. Exact rank-two violations

### The elementary witness

For the source-provided vector

\[
\psi=|34\rangle-|43\rangle,
\]

the nonzero coefficient submatrix is

\[
\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\]

so the coefficient matrix has rank exactly two. The Choi expectation is

\[
\langle\psi,C(\Phi)\psi\rangle
=\frac13(0+1-2)=-\frac13.
\]

This is the expectation of the **unnormalized** vector specified in S1. It proves failure of \(2\)-positivity directly; no inference from a CP relaxation or from sampled positivity is involved.

### The normalized eigenvector

Let

\[
q=\frac{\sqrt5-1}{2},\qquad
r=\frac q3=\frac{\sqrt5-1}{6},\qquad
\eta=\frac{|34\rangle-q|43\rangle}{\sqrt{1+q^2}}.
\]

Here \(q>0\) and \(q^2+q=1\). Therefore

\[
T\binom{1}{-q}
=
\binom{-q}{1-q}
=
\binom{-q}{q^2}
=
-q\binom{1}{-q}.
\]

It follows that

\[
C(\Phi)\eta=-r\eta.
\]

Both coefficients are nonzero, and the corresponding \(2\times2\) coefficient submatrix has nonzero determinant. Hence \(\eta\) has Schmidt rank exactly two. Its support also gives \(\eta\perp\Omega\).

These reconstruct S1 LF185–218 exactly.

## 6. Universal repair-family theorem

Assume exactly

\[
\lambda\ge0,\qquad \delta\in\mathbb R,\qquad
S=S^\dagger\ge0,
\]

and define

\[
\Delta(X)=\operatorname{Tr}(X)I_4,\qquad
\mathcal M_S(X)=S\circ X,\qquad
\Psi=\lambda\Phi+\delta\Delta+\mathcal M_S.
\]

The normalization matters: \(\Delta\) here is the **unnormalized** trace-to-identity map.

### No hidden Schur effect outside \(\mathcal D\)

Directly,

\[
C(\Delta)=I_{16},
\qquad
C(\mathcal M_S)=\sum_{i,j}S_{ij}|ii\rangle\langle jj|.
\]

Thus the Schur contribution is exactly \(S\) on \(\mathcal D\) and zero on its orthogonal complement. Complex phases in \(S\) create no coupling to \(\mathcal B\) or to the ten scalar blocks.

The complete block structure of \(C(\Psi)\) is therefore:

\[
H=\delta I_4+\frac{\lambda}{3}M+S
\quad\text{on }\mathcal D;
\]

\[
B_{\lambda,\delta}
=
\begin{pmatrix}
\delta&\lambda/3\\
\lambda/3&\delta+\lambda/3
\end{pmatrix}
=\delta I_2+\frac{\lambda}{3}T
\quad\text{on }\mathcal B;
\]

three scalar blocks equal to \(\delta\), and seven equal to \(\delta+\lambda/3\).

### Necessity from the genuine rank-two quantifier

Because \(\eta\) lies in \(\mathcal B\),

\[
\langle\eta,C(\Psi)\eta\rangle=\delta-\lambda r.
\]

The Schur term vanishes identically on this vector, for every allowed complex \(S\). Therefore

\[
\Psi\text{ \(2\)-positive}
\Longrightarrow
\delta\ge\lambda r.
\]

This is a direct necessity for \(2\)-positivity, not merely a necessary condition for CP.

### Independent reconstruction of the \(\mathcal D\)-block spectrum

The orthogonal directions

\[
(1,-1,0,0),\qquad (0,0,1,-1)
\]

have \(M\)-eigenvalues \(0\) and \(1\), respectively.

On the orthonormal complementary basis

\[
f_1=\frac{(1,1,0,0)}{\sqrt2},
\qquad
f_2=\frac{(0,0,1,1)}{\sqrt2},
\]

one has

\[
Mf_1=2f_1+2f_2,\qquad Mf_2=2f_1+f_2.
\]

The restricted matrix is therefore

\[
\begin{pmatrix}2&2\\2&1\end{pmatrix},
\]

with characteristic polynomial \(\mu^2-3\mu-2\). Hence

\[
\operatorname{spec}(M)
=
\left\{0,\ 1,\ \frac{3-\sqrt{17}}2,\ \frac{3+\sqrt{17}}2\right\}.
\]

This independently verifies the load-bearing spectrum in S1 LF313–334.

### Sufficiency on the entire complex space

Suppose \(\delta\ge\lambda r\). Since \(\lambda\ge0\), also \(\delta\ge0\).

The characteristic polynomial of \(T\) is \(t^2-t-1\). Thus the eigenvalues of \(B_{\lambda,\delta}\) are

\[
\delta+\lambda\frac{1-\sqrt5}{6},
\qquad
\delta+\lambda\frac{1+\sqrt5}{6},
\]

both nonnegative under the assumed threshold.

All ten scalar blocks are nonnegative.

For the remaining block, the spectrum just reconstructed gives

\[
\lambda_{\min}\left(\delta I_4+\frac{\lambda}{3}M\right)
=
\delta-\lambda\frac{\sqrt{17}-3}{6}.
\]

The required threshold comparison is strict:

\[
\frac{\sqrt5-1}{6}>
\frac{\sqrt{17}-3}{6}.
\]

Indeed, \(\sqrt5+2>\sqrt{17}\), since both sides are positive and

\[
(\sqrt5+2)^2-17=4(\sqrt5-2)>0.
\]

Therefore \(\delta I_4+\lambda M/3\ge0\). Adding the arbitrary complex Hermitian PSD matrix \(S\) preserves positivity. Hence \(H\ge0\), and every block of \(C(\Psi)\) is PSD.

Combining this with necessity and CP implying \(2\)-positivity proves the universal statement:

\[
\boxed{
\Psi_{\lambda,\delta,S}\text{ is \(2\)-positive}
\iff
\Psi_{\lambda,\delta,S}\text{ is CP}
\iff
\delta\ge\lambda\frac{\sqrt5-1}{6}.
}
\]

### Boundary and degenerate cases

The proof covers all named cases without continuity assumptions or inverses of \(S\):

- **\(\lambda=0\):** The pair block is \(\delta I_2\), so necessity is exactly \(\delta\ge0\). For \(\delta\ge0\), the complete Choi matrix is positive.
- **Singular \(S\), including \(S=0\):** Only \(S\ge0\) is used. No strict positivity or factorization inverse is required.
- **Negative \(\delta\):** Since \(\lambda r\ge0\), the same \(\eta\) gives strictly negative expectation.
- **Threshold equality:** The smaller pair-block eigenvalue is zero, not negative; all other blocks remain PSD.
- **Arbitrary complex PSD \(S\):** The argument uses Hermitian positive semidefiniteness, not real entries or entrywise nonnegativity.

The result is not extended to negative \(\lambda\), indefinite \(S\), or arbitrary CP additions outside the Schur class.

## 7. Detector exclusion and nonsingular local filters

When the family satisfies the genuine rank-two nonnegativity condition, the theorem makes its entire Choi matrix PSD. Consequently, for every positive state \(\rho\),

\[
\operatorname{Tr}(C(\Psi)\rho)
=
\operatorname{Tr}\!\left(\rho^{1/2}C(\Psi)\rho^{1/2}\right)
\ge0.
\]

Thus this family cannot supply the required negative pairing, **even before imposing PPT**. This is a family exclusion, not a theorem about every \(4\times4\) detector or PPT state.

The named repair subclasses are included:

- A nonnegative identity-map addition has Schur matrix \(tJ_4\), \(t\ge0\).
- A CP map with diagonal Kraus operators has Schur matrix
  \[
  S_{ij}=\sum_\alpha d_{\alpha i}\overline{d_{\alpha j}},
  \]
  which is PSD.
- Sums of such additions remain in the same class.

For \(A,B\in GL_4(\mathbb C)\), let

\[
L=A\otimes B,\qquad W'=LC(\Psi)L^\dagger.
\]

At or above threshold, congruence preserves PSD.

Below threshold, use exactly the candidate’s pullback vector

\[
z=(L^\dagger)^{-1}\eta
=
\left((A^\dagger)^{-1}\otimes(B^\dagger)^{-1}\right)\eta.
\]

Then

\[
\langle z,W'z\rangle
=
\langle\eta,C(\Psi)\eta\rangle
=
\delta-\lambda r<0.
\]

Under the adopted vectorization,

\[
(A\otimes B)\operatorname{vec}(X)
=\operatorname{vec}(AXB^T).
\]

Multiplication on both sides by invertible matrices preserves rank. Hence the pullback vector still has Schmidt rank exactly two.

This proves S1 LF372–385. The explicit exclusion of noninvertible filters in LF387 is necessary and correctly retained: a singular filter can destroy the invertible pullback argument.

## 8. Supplied rational controls: written checks only

These are the two examples already specified in S1, not newly selected probes.

### Control 1

For \(\lambda=1\), \(\delta=1/5\), and

\[
v=|34\rangle-\frac35|43\rangle,
\]

the Schur contribution again vanishes. Direct substitution into the pair-block quadratic form gives

\[
\begin{aligned}
\langle v,C(\Psi_{1,1/5,S})v\rangle
&=\frac15\left(1+\frac9{25}\right)
+\frac13\left(\frac9{25}-\frac65\right)\\
&=\frac{34}{125}-\frac7{25}\\
&=-\frac1{125}.
\end{aligned}
\]

This verifies S1 LF393–398 for every allowed \(S\).

### Control 2

For \(\lambda=1\), \(\delta=5/24\),

\[
B_{1,5/24}=\frac1{24}
\begin{pmatrix}5&8\\8&13\end{pmatrix},
\]

so

\[
\det B_{1,5/24}
=\frac{65-64}{576}
=\frac1{576}>0.
\]

Also,

\[
\frac5{24}>r
\iff
9>4\sqrt5,
\]

and the last comparison follows by squaring positive quantities: \(81>80\).

Therefore the **universal theorem**, not the pair-block determinant alone, puts the whole family at this offset on the CP side.

These are exact written finite identities. They are not executed tests and do not independently substitute for the universal proof.

## 9. Public-source limitation and unpaid gates

S2 LF17–34 requires an already \(k\)-positive seed and discusses further nondecomposability and conditional-complete-positivity conditions. Nothing in that excerpt manufactures \(2\)-positivity from ordinary positivity.

S2 LF58 explicitly describes sampling ordinary pure-state inputs and says that ordinary positivity of Eq. (10) was not proved. The negative vectors above have Schmidt rank two, not one. They therefore establish failure of \(2\)-positivity without establishing failure of ordinary positivity.

Accordingly:

- The paper’s ordinary-positivity claim is **not refuted here**.
- The general workflow theorem is **not refuted or re-proved here**.
- The semigroup arguments in S1 §§5–6 were read as required context but were not used as premises, reconstructed, or adopted in this review.
- No literature novelty, priority, exhaustive source status, human review, independent-model-family review, or formal/kernel verification is established.
- No conclusion about a separate SPR fixed-\(F\) versus all-eight strict-negative condition is made; those objects were not inputs to this PPT-map audit.

The original target still requires either:

1. An actual normalized \(4\times4\) PPT state \(\rho\) and a Hermitian detector \(W\) nonnegative on **every complex coefficient matrix of rank at most two**, with \(\operatorname{Tr}(W\rho)<0\); or
2. An unrestricted proof that every \(4\times4\) PPT state has Schmidt number at most two.

Neither is supplied by this family exclusion. Arbitrary non-Schur CP perturbations, singular local filters, and later-time semigroup behavior remain outside this accepted proof scope.

## 10. Final verdict

**Overall correctness:** correct **for the frozen Theorem 1 / §§2–4 audit only**.

**Explanation:** The literal matrix-unit reconstruction yields exactly the claimed Choi blocks. The rank-two eigenvector forces the stated threshold independently of every complex PSD Schur addition, and the independently reconstructed diagonal-block spectrum proves that the same threshold makes the entire Choi matrix PSD, including all boundary cases. The nonsingular-filter corollary and both provided rational identities also hold; no broader original-target, semigroup, ordinary-positivity, or novelty conclusion is adopted.

**Confidence:** 0.99 within this audited scope.

**Mathematical findings:** 0 FATAL / 0 MAJOR / 0 MINOR. No additional reviewer-process violation was observed in this assignment; this is not a retrospective cognition or chronology certification for other episodes.

**Parent disposition remains required.** The cutoff remains **2026-10-31T21:23:27Z**.