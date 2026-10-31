# F528 — Fresh WRITTEN review of the coherent vacuum–\(W_4\) family

**Disposition:** SUPPORTED at the stated family, local-unitary, and finite-convex-mixture scopes.  
**Mathematical findings:** **0 FATAL / 0 MAJOR / 0 MINOR.**  
**Original unrestricted four-qubit targets:** **NOT PROVED.**

This is a fresh written reconstruction from the four frozen original inputs. It does not use, resume, or salvage F508 or any other held mathematical episode.

## 1. Provenance, complete reading, and methods

### Frozen identification

Wave:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f528-fresh-coherent-vacuum-w4-h2-channel-replacement-review/`

Parent-supplied metadata:

- Manifest SHA256: `d0b855f9853ced6dec51b6269f6eb44e85da87a8c6b3e1626949841d2f96885c`
- Freeze-receipt SHA256: `e37fe74d2eb7c63619112b4b22e776bba0ccec1db99aa6d4eb93046a5908bc40`
- Literal-packet SHA256: `ec090ccf89dd4c60628f74759d2e430b01893deda0f99e36336a85dc441cd375`
- Packet size and LF count: 50,832 bytes, 861 LF.
- Parent-observed metadata clock: `2026-10-30T12:40:23-0700 PDT`.

These hashes, sizes, counts, and that clock are attributed to the parent’s `parent-live-metadata-supply-v1.json`. I did not independently execute hashing or obtain a native start/clock observation.

### Read order and coverage

Before reading the mathematical packet, I read:

1. The complete manifest, including its untruncated audit mandate and ending.
2. The complete freeze receipt.
3. All thirteen declared status-only controls, including their endings.
4. The parent’s live metadata supply.

I then sent a **direct administrative PRE-BODY ACK to `agent://Main`**. The tool reported successful delivery. Only afterward did I open the mathematical packet.

I read every packet line in order, using raw windows of at most twenty LF: the forty-three successive windows covering 1–860, followed by 861. This includes:

- **S1:** packet-labelled source lines 1–730, including its final `confidence` line;
- **S2:** lines 1–48;
- **S3:** lines 1–42;
- **S4:** lines 1–39.

The source LF count of 729 for S1 and its packet-labelled logical ending at line 730 are both preserved as supplied; I do not substitute one for the other.

Source abbreviations below refer exclusively to:

- **S1:** `review-waves/f480-four-qubit-genuine-entanglement-three-body-marginal-sum-frontier/review-v1.md`, SHA256 `829ed2c87f5f44fa6cbb61f294c69b8a6cb66e75e1d516701c0d6ab5569d0b34`.
- **S2:** `dispositions/physics-2-two-coefficient-and-paired-repetition-all-prefix-majorization-parent-v1.md`, SHA256 `8522551e1088a796288c73c9b1aad8fa40e197d74b6f7d41447392d07370d6c0`.
- **S3:** `dispositions/physics-2-symmetric-w4-orbit-all-prefix-majorization-parent-v1.md`, SHA256 `b15be59978ee1c50fe2b9a8ff91051df937fefb67e38b7183f5e634a2bdacab0`.
- **S4:** `dispositions/physics-2-all-three-qubit-and-four-qubit-biseparable-majorization-parent-v1.md`, SHA256 `cef7da09334dd4288d166782c9629daa3aeaef6af1db2ffd98ec012fe233fa93`.

All are under the assigned run root.

### Execution and exclusion boundaries

- Scientific execution, code, CAS, solvers, enumeration, numerical experiments, builds, tests, linters, and formatters: **NOT RUN**.
- No new private or public selected diagnostic parameter, frequency, support, or matrix instance was used. The reasoning below uses formal parameters and the author-explicit endpoints.
- No sibling return, prior stopped-review body, author calculation code, new scientific source, or held mathematical payload was opened.
- Links inside the frozen sources were not followed.
- All quarantine records were used for status and exclusion only.
- One read-only `git diff` restricted to this wave’s manifest, receipt, and packet returned no output. This is neither an independent hash check nor mathematical verification.
- No repository file was written. This complete body is returned for parent materialization; no alternative write mechanism or shell bypass was used.
- No independent-model-family, human, formal/kernel, novelty, or clean-cognition assurance is asserted.

The F480 transport history remains exactly as disclosed: its pre-body ACK was printed in the transcript, without observed separate direct delivery. That historical noncompliance is not silently repaired and is not treated as automatic mathematical falsity.

## 2. Claim-by-claim verdicts

| Claim | Frozen location | Verdict |
|---|---|---|
| Compatible three- and two-body marginal formulas | S1 LF130–154 | **SUPPORTED** |
| Physical orthogonal decomposition and the stated \(H_3,H_2\) blocks | S1 LF158–239, 281–320 | **SUPPORTED** |
| All \(H_3\) prefixes for the entire coherent family | S1 LF241–275 | **SUPPORTED** |
| All seven stated leading-principal-determinant identities and their required sign/inertia consequences | S1 LF324–393 | **SUPPORTED** |
| All \(H_2\) prefixes, including direct-sum assembly and endpoints | S1 LF395–415 | **SUPPORTED** |
| Positive-branch actual-channel bound for the same arbitrary complex consuming projector | S1 LF419–486 | **SUPPORTED** |
| Physical negative branch using full transpose and the transported projector | S1 LF488–510 | **SUPPORTED** |
| Arbitrary physical local-unitary images and finite mixtures | S1 LF512–522 | **SUPPORTED** |
| Genuine four-party entanglement for \(q<1\) | S1 LF526–550 | **SUPPORTED** |
| Separation from Class A/B, the equal-\(W_4\) orbit, and their stated hull for \(0<q<1\) | S1 LF552–587; S2 LF9–18; S3 LF7–13 | **SUPPORTED** |
| Unrestricted-input second-moment sufficient condition for \(H_3\) | S1 LF589–619 | **SUPPORTED** |
| Pure-state spin-flip and moment identities | S1 LF621–675 | **SUPPORTED** |
| Independent verification of the external printed-prior/source-authenticity claims | S1 LF677–683 | **INCONCLUSIVE in this duty**; no external source was opened. The frozen S4 qualification is retained at its stated scope. |
| Unrestricted four-qubit \(H_3\) majorization or unrestricted all-prefix channel theorem | S1 LF695–716 | **INCONCLUSIVE / NOT PROVED**, consistently with the author’s express residual. |

No claimed mathematical conclusion in the assigned family proof was refuted.

## 3. Reconstruction of the compatible marginals

Write
\[
r=1-q,\qquad u=\sqrt{qr},\qquad u^2=r(1-r),
\]
and
\[
|\psi_q\rangle=\sqrt q\,|0000\rangle+
\frac{\sqrt r}{2}\sum_{j=1}^{4}|e_j\rangle .
\]

For an erased qubit \(i\), the two conditional vectors are
\[
v_i=\sqrt q\,|000\rangle+
\frac{\sqrt r}{2}\sum_{j\ne i}|e_j\rangle,
\qquad
\frac{\sqrt r}{2}|000\rangle .
\]
Their outer products give exactly
\[
\rho_{\bar i}=|v_i\rangle\langle v_i|
+\frac r4|000\rangle\langle000|.
\]

For a retained pair \(i,j\), the vacuum conditional vector is
\[
v_{ij}=\sqrt q\,|00\rangle+
\frac{\sqrt r}{2}(|10\rangle+|01\rangle).
\]
The two erased single excitations contribute \(r/4\) each to the same pair vacuum. Therefore
\[
\rho_{ij}=|v_{ij}\rangle\langle v_{ij}|
+\frac r2|00\rangle\langle00|.
\]

These are compatible reductions of one normalized physical state, not independently chosen marginal matrices. In particular, in the pair basis their diagonal entries are
\[
q+\frac r2,\quad \frac r4,\quad \frac r4,\quad0,
\]
their vacuum–single entries are \(u/2\), and their single-excitation exchange entry is \(r/4\).

### Entries of \(H_2\)

On a computational string of weight \(k\), there are \(\binom{4-k}{2}\) retained pairs containing no excitation and \(k(4-k)\) containing exactly one. Thus its diagonal is
\[
\left(q+\frac r2\right)\binom{4-k}{2}
+\frac r4k(4-k)
=
q\binom{4-k}{2}+\frac{3r}{4}(4-k).
\]

Two weight-\(k\) strings differing by one exchange have exactly one retained pair that contributes the exchange entry, giving \(r/4\).

Between a weight-\(k\) string and a containing weight-\((k+1)\) string, the newly excited qubit must be paired with an unexcited spectator. There are \(3-k\) such choices, giving
\[
\frac{3-k}{2}u.
\]

This independently recovers S1 (16)–(17).

### Entries of \(H_3\)

The same conditional-vector calculation gives:

- weight-zero diagonal \(4q+r=4-3r\);
- weight-one diagonal \(q+r=1\);
- weight-two diagonal \(2(r/4)=r/2\);
- exchange entries \(r/2\) at weight one and \(r/4\) at weight two;
- vacuum–single entries \(3u/2\);
- single–containing-pair entries \(u/2\);
- no other entries.

This recovers the full list at S1 LF210–218.

## 4. Reconstruction of the physical block decomposition

Let \(f\in\mathbb C^4\) have norm one and \(\sum_i f_i=0\). Use the author’s three vectors
\[
|f;1\rangle=\sum_i f_i|i\rangle,
\quad
|f;2\rangle=\frac1{\sqrt2}\sum_{i<j}(f_i+f_j)|ij\rangle,
\quad
|f;3\rangle=\sum_{|S|=3}\left(\sum_{i\in S}f_i\right)|S\rangle.
\]

The norm identity
\[
\sum_{i<j}|f_i+f_j|^2=2\sum_i|f_i|^2
\]
and polarization show that the middle map preserves inner products after its \(1/\sqrt2\) normalization. For weight three, the coefficient on the complement of \(i\) is \(-f_i\), so that map also preserves inner products.

The upward incidence maps have coefficient \(\sqrt2\) between these vectors:

- From weight one to a pair \(\{i,j\}\), the coefficient is \(f_i+f_j\).
- From weight two to a triple, each \(f_i\) occurs twice in the sum over its three pairs, giving \(\sqrt2\sum_{i\in S}f_i\).

On normalized symmetric vectors the corresponding coefficients are
\[
2,\sqrt6,\sqrt6,2.
\]

The exchange adjacency acts by:

- \(k(4-k)\) on the symmetric weight-\(k\) vector;
- \(-1,0,-1\) on the three \(f\)-vectors;
- \(-2\) on the residual weight-two incidence kernel.

For the last statement, if
\[
\sum_{j\ne i}z_{\{i,j\}}=0
\]
for each \(i\), then at pair \(\{i,j\}\) the exchange sum is
\[
\sum_{\ell\ne i,j}(z_{\{i,\ell\}}+z_{\{j,\ell\}})
=-2z_{\{i,j\}}.
\]
The incidence maps out of that residual space vanish. Its dimension is two: the vertex–pair incidence map has rank four, since its adjoint has coefficients \(c_i+c_j\), and vanishing of all those coefficients forces \(c=0\).

Consequently the stated decomposition has dimension
\[
5+3\cdot3+2=16
\]
and is an orthogonal decomposition of the actual physical Hilbert space.

Substitution of the entries above yields
\[
H_3\cong A_3\oplus B_2^{\oplus3}\oplus0_7,
\]
where
\[
A_3=
\begin{pmatrix}
4-3r&3u&0\\
3u&1+\frac32r&\sqrt{\frac32}u\\
0&\sqrt{\frac32}u&\frac32r
\end{pmatrix},
\qquad
B_2=
\begin{pmatrix}
1-\frac r2&u/\sqrt2\\
u/\sqrt2&r/2
\end{pmatrix}.
\]

Similarly,
\[
H_2\cong A_4\oplus B_3^{\oplus3}\oplus I_2\oplus0,
\]
with
\[
A_4=
\begin{pmatrix}
6-3r&3u&0&0\\
3u&3&\sqrt6u&0\\
0&\sqrt6u&1+\frac32r&\sqrt{\frac32}u\\
0&0&\sqrt{\frac32}u&\frac32r
\end{pmatrix},
\]
and
\[
B_3=
\begin{pmatrix}
3-r&\sqrt2u&0\\
\sqrt2u&1+\frac r2&u/\sqrt2\\
0&u/\sqrt2&r/2
\end{pmatrix}.
\]

In particular, the residual weight-two block of \(H_2\) is exactly \(I_2\): its diagonal is \(1+r/2\), and the exchange contribution is \(-r/2\).

All these blocks are positive semidefinite because they are restrictions of the actual positive marginal sums. Their traces are
\[
\operatorname{Tr}A_3=5,\quad
\operatorname{Tr}B_2=1,\quad
\operatorname{Tr}A_4=10,\quad
\operatorname{Tr}B_3=4.
\]
Thus
\[
\operatorname{Tr}H_3=8,\qquad
\operatorname{Tr}H_2=10+3\cdot4+2=24.
\]

## 5. Complete \(H_3\) prefix proof

Every lifted density operator is bounded above by identity. Hence
\[
0\le H_3\le4I.
\]
In particular every eigenvalue of \(A_3\) is at most four.

Positivity and trace one of \(B_2\) bound all of its eigenvalues by one. Its determinant is
\[
\left(1-\frac r2\right)\frac r2-\frac{u^2}{2}
=\frac{r^2}{4},
\]
so its displayed eigenvalues
\[
\frac{1\pm\sqrt{1-r^2}}2
\]
are also correct.

For \(1\le k\le4\), take any selection of \(k\) eigenvalues of the direct sum and let \(j\) come from \(A_3\).

- For \(j=0\), the sum is at most \(k\).
- For \(j=1\), it is at most \(4+k-1=k+3\).
- For \(j\ge2\), positivity and \(\operatorname{Tr}A_3=5\) give at most
  \[
  5+k-j\le k+3.
  \]

Taking the maximum over selections proves
\[
K_k(H_3)\le k+3,\qquad 1\le k\le4.
\]
For \(k\ge5\), positivity and trace eight give \(K_k(H_3)\le8\). These are exactly the prefixes of
\[
L_3=(4,1,1,1,1,0^{\times11}).
\]

This reconstructs the entire \(H_3\) result; it is not a conditional import from another review.

## 6. Complete determinant and inertia reconstruction for \(H_2\)

For a symmetric tridiagonal matrix with diagonal \(d_j\) and successive off-diagonals \(e_j\), its leading determinants satisfy
\[
D_0=1,\quad D_1=d_1,\quad
D_j=d_jD_{j-1}-e_{j-1}^2D_{j-2}.
\]
I use this identity with the formal relation \(u^2=r(1-r)\).

### 6.1 The block \(B_3\)

For \(3I-B_3\), the diagonal is
\[
r,\quad2-\frac r2,\quad3-\frac r2,
\]
and the squared off-diagonals are \(2u^2,u^2/2\). Therefore
\[
D_1=r,
\]
\[
D_2=r\left(2-\frac r2\right)-2r(1-r)
=\frac32r^2,
\]
and
\[
D_3=
\left(3-\frac r2\right)\frac32r^2
-\frac12r(1-r)\,r
=\frac{r^2(16-r)}4.
\]

All three are strictly positive for \(0<r\le1\). At the author-explicit endpoint \(r=0\),
\[
3I-B_3=\operatorname{diag}(0,2,3).
\]
Thus \(B_3\le3I\) on the entire closed interval.

Together with \(B_3\ge0\) and trace four, this proves
\[
B_3\prec(3,1,0):
\]
the first prefix is at most three, the second at most the total four, and the traces agree.

### 6.2 The block \(A_4\)

The universal bound \(H_2\le6I\) gives
\[
\lambda_{\max}(A_4)\le6.
\]

For \(M=A_4-I\), the diagonal is
\[
5-3r,\quad2,\quad\frac32r,\quad\frac32r-1,
\]
and the squared off-diagonals are
\[
9u^2,\quad6u^2,\quad\frac32u^2.
\]

The recurrence gives
\[
p_1=5-3r,
\]
\[
p_2=2(5-3r)-9r(1-r)
=10-15r+9r^2,
\]
\[
\begin{aligned}
p_3
&=\frac32r\,p_2-6r(1-r)(5-3r)\\
&=\frac32r(3r-2)(5-r),
\end{aligned}
\]
and
\[
\begin{aligned}
p_4
&=\left(\frac32r-1\right)p_3
-\frac32r(1-r)p_2\\
&=\frac34r^2(9r^2+9r-14).
\end{aligned}
\]

Thus all four identities in S1 (24) are recovered.

On \([0,1]\),
\[
p_1\ge2>0,
\qquad
p_2=9\left(r-\frac56\right)^2+\frac{15}{4}>0.
\]
The leading \(2\times2\) block \(T\) of \(M\) is therefore positive definite throughout. Let \(C\) be its \(2\times2\) Schur complement. Congruence gives
\[
M\sim T\oplus C,
\qquad
C_{11}=\frac{p_3}{p_2},
\qquad
\det C=\frac{p_4}{p_2}.
\]

There are two exhaustive cases.

**If \(p_4\le0\):** \(\det C\le0\), so a real symmetric \(2\times2\) matrix \(C\) cannot have two strictly negative eigenvalues.

**If \(p_4>0\):** necessarily
\[
r>\frac{\sqrt{65}-3}{6}>\frac23.
\]
The latter comparison follows from \(\sqrt{65}>7\). Hence \(p_3>0\), so \(C_{11}>0\) and \(\det C>0\); therefore \(C\) is positive definite.

In both cases \(M\) has at most one strictly negative eigenvalue. At \(r=0\), the explicit matrix
\[
M=\operatorname{diag}(5,2,0,-1)
\]
confirms the same conclusion, including its zero eigenvalue.

Let the eigenvalues of \(A_4\) decrease as \(\alpha_1,\ldots,\alpha_4\). The inertia conclusion says \(\alpha_3\ge1\). Since \(A_4\ge0\),
\[
K_2(A_4)=10-\alpha_3-\alpha_4\le9.
\]
Also
\[
K_1(A_4)\le6,\qquad K_3(A_4)\le10,\qquad K_4(A_4)=10.
\]
Therefore
\[
A_4\prec(6,3,1,0).
\]

No eigenvalue-gap assumption or division by \(r\), \(q\), or \(u\) is hidden in this argument. The only Schur-complement denominator used is \(p_2\), which has a uniform strictly positive bound.

### 6.3 Direct sums and every prefix

For Hermitian blocks,
\[
K_k\!\left(\bigoplus_jX_j\right)
=
\max_{\substack{0\le k_j\le\dim X_j\\ \sum_jk_j=k}}
\sum_jK_{k_j}(X_j).
\]
Apply each block majorization to the same allocation, and then maximize. This proves direct-sum majorization here.

The resulting reference union is
\[
(6,3,1,0)
\oplus(3,1,0)^{\oplus3}
\oplus(1,1)
\oplus(0).
\]
Its decreasing rearrangement is
\[
L_2=(6,3^{\times4},1^{\times6},0^{\times5}).
\]
Dimensions and traces agree exactly, proving all sixteen \(H_2\) prefixes.

### 6.4 Author-explicit endpoints

At \(r=0\), the blocks are diagonal and assemble exactly to \(L_3\) and \(L_2\).

At \(q=0\), hence \(r=1,u=0\), the displayed blocks remain valid without a limiting prescription. In particular,
\[
A_4=\operatorname{diag}\left(3,3,\frac52,\frac32\right),
\quad
B_3=\operatorname{diag}\left(2,\frac32,\frac12\right).
\]
The determinant and inertia argument already includes this endpoint. The \(H_3\) proof likewise remains valid there. No additional selected instance is needed.

## 7. Reconstruction of the actual channel and its consuming interface

### 7.1 Universal one-body layer

Diagonalize each one-qubit marginal:
\[
\rho_i=V_i\operatorname{diag}(z_i,1-z_i)V_i^\dagger.
\]
For
\[
R_1=\sum_i |0\rangle\langle0|_i\otimes I_{\bar i},
\]
average conjugation by \(\bigotimes_iV_iX^{s_i}\), where the independent bits have probabilities \(z_i,1-z_i\).

The average of each summand is its actual lifted marginal, so the average is exactly \(H_1(\rho)\). Convexity of each Ky Fan sum therefore gives
\[
H_1(\rho)\prec
(4,3^{\times4},2^{\times6},1^{\times4},0)=L_1.
\]

This does not require the different marginals to share an eigenbasis.

### 7.2 Positive branch: one common complex projector

For
\[
T_t(X)=tX+b\,\operatorname{Tr}(X)I,\qquad b=\frac{1-t}{2},
\]
the tensor expansion is
\[
T_t^{\otimes4}(\rho)=
t^4\rho+t^3bH_3(\rho)+t^2b^2H_2(\rho)+tb^3H_1(\rho)+b^4I.
\]

Fix one arbitrary complex orthogonal rank-\(k\) projector \(Q\). On the claimed pure family,
\[
\begin{aligned}
\operatorname{Tr}\bigl[QT_t^{\otimes4}(\rho)\bigr]
\le{}&t^4+t^3bK_k(L_3)+t^2b^2K_k(L_2)\\
&+tb^3K_k(L_1)+kb^4 .
\end{aligned}
\]
Every coefficient is nonnegative for \(0\le t\le1\). Each layer bound is applied to this same \(Q\); no separately maximizing projector is substituted into the actual output.

The necessary reference-side equality also holds. On the author’s product reference \(|0000\rangle\), all coefficient operators are diagonal and co-ordered by Hamming weight \(w\), with entries
\[
\mathbf1_{w=0},\quad
\binom{4-w}{3},\quad
\binom{4-w}{2},\quad
4-w,\quad1.
\]
Their weighted sum has entry
\[
\sum_{m=0}^{4-w}\binom{4-w}{m}t^mb^{4-m}
=b^w(t+b)^{4-w}.
\]
With \(a=t+b\), these are exactly the entries of
\[
D_t=\operatorname{diag}(a,b)^{\otimes4}.
\]
Because \(a\ge b\ge0\), their Hamming-weight order is decreasing. Thus the sum of reference prefix bounds is exactly \(K_k(D_t)\), including partial selections inside tied weight spaces.

Taking the maximum over consuming projectors proves
\[
T_t^{\otimes4}(\rho)\prec D_t.
\]

### 7.3 Negative branch: full transpose, not partial transpose

For a qubit,
\[
\mathcal J(X)=YX^TY=\operatorname{Tr}(X)I-X,
\]
and
\[
\mathcal J\circ T_t=T_{-t}.
\]
Tensoring all four factors gives
\[
T_{-t}^{\otimes4}(\rho)
=W[T_t^{\otimes4}(\rho)]^TW,
\qquad W=Y^{\otimes4}.
\]
This is a full transpose on the entire output, followed by unitary conjugation. It preserves its spectrum.

The consuming-side identity is
\[
\operatorname{Tr}\!\left[QW A^TW\right]
=
\operatorname{Tr}\!\left[(WQ^TW)A\right].
\]
Here \(W^T=W\) for four qubits. The transported
\[
Q'=WQ^TW
\]
is again an orthogonal projector of rank \(k\), including for non-real \(Q\). Hence the already-proved positive-branch bound applies to the actual negative-branch expectation.

For the physical range \(0\le p\le4/3\), the negative branch has \(t=p-1\le1/3\), contained in the positive proof’s \(0\le t\le1\) interval.

### 7.4 Local unitaries, phases, and mixtures

Actual physical local unitaries satisfy
\[
H_m(V\rho V^\dagger)=VH_m(\rho)V^\dagger,
\]
and the depolarizing channel has the corresponding local covariance. Moving \(V\) to the consuming projector preserves orthogonality and rank.

The phase claim also has the correct physical scope: a global phase fixes the vacuum coefficient when present, and the four independent local diagonal phases remove the phases on the four single-excitation coefficients.

For a finite mixture, keep \(Q\) fixed and use linearity:
\[
\operatorname{Tr}\!\left[Q\Lambda_p\!\left(\sum_jw_j\rho_j\right)\right]
=\sum_jw_j\operatorname{Tr}[Q\Lambda_p(\rho_j)]
\le K_k(D_t).
\]
The common reference is independent of \(q\), phases, and local bases. Thus differing choices between mixture components cause no routing or common-projector gap.

The actual channel conclusion therefore holds for all sixteen prefixes throughout the claimed physical interval.

## 8. Genuine entanglement and strict hull enlargement

### 8.1 All seven bipartitions

For every \(r>0\), across a \(1|3\) cut the two conditional vectors are
\[
\sqrt q\,|000\rangle+
\frac{\sqrt r}{2}\sum_{j\ne i}|e_j\rangle,
\qquad
\frac{\sqrt r}{2}|000\rangle .
\]
They are linearly independent, giving Schmidt rank two across each of the four such cuts.

Across any \(2|2\) cut, in the bases \((|00\rangle,|w\rangle)\), where
\[
|w\rangle=(|01\rangle+|10\rangle)/\sqrt2,
\]
the coefficient matrix is
\[
\begin{pmatrix}
\sqrt q&\sqrt{r/2}\\
\sqrt{r/2}&0
\end{pmatrix}.
\]
Its determinant is \(-r/2\ne0\), so all three balanced cuts also have Schmidt rank two.

The pure state is therefore product across none of the seven cuts. It is genuinely four-party entangled, including the \(q=0\) endpoint.

### 8.2 Class A/B exclusion

Every pair reduction has rank two with support
\[
\operatorname{span}\{|00\rangle,|w\rangle\}.
\]
A general vector in this support has coefficient matrix
\[
\begin{pmatrix}
x&y/\sqrt2\\
y/\sqrt2&0
\end{pmatrix},
\]
whose determinant is \(-y^2/2\). Over complex coefficients it vanishes exactly when \(y=0\). Thus the support contains exactly one product ray.

For **Class A**, if a two-coefficient physical-product-basis state has rank two across a paired cut, its pair support is spanned by the two independent product substrings of those two basis strings. It therefore contains two independent product rays. If it instead has rank one across that cut, it cannot equal the present state, which has rank two across every paired cut.

For **Class B**, use its actual encoded pairing. Its pair reduction is supported in a two-dimensional repetition space spanned by two physical product vectors. If its pair reduction has rank two, its support equals that repetition space and contains both independent product rays. The present state’s rank-two support cannot equal it.

Physical local unitaries preserve product vectors and their independence. The present one-product-ray property holds for all three pairings, so permitting any Class B pairing does not evade the argument.

This uses exactly the definitions at S2 LF11–12; it does not silently enlarge Class A to sums of two nonorthogonal product vectors.

### 8.3 Equal-\(W_4\) orbit exclusion

The actual one-qubit marginal is
\[
m_q=
\begin{pmatrix}
1-r/4&u/2\\
u/2&r/4
\end{pmatrix},
\]
and
\[
\det m_q
=\frac r4-\frac{r^2}{16}-\frac{r(1-r)}4
=\frac{3r^2}{16}.
\]
For \(0<q<1\), one has \(0<r<1\), so this differs from the equal-\(W_4\) determinant \(3/16\). Local unitaries preserve marginal spectra, excluding its entire physical local-unitary orbit.

### 8.4 Convex hulls

If a positive mixture equals a rank-one density, every positive-weight component must be supported on that same ray: its expectation on every vector orthogonal to the ray is a sum of nonnegative terms equal to zero. Normalization then makes every component equal to that pure density.

Consequently, for \(0<q<1\), the new pure states cannot be mixtures of the excluded Class A/B or equal-\(W_4\) states. Their genuine entanglement also excludes the biseparable class stated at S4 LF17.

The exact strict-enlargement conclusion is therefore valid: **adjoining this family to the specified previously supported classes strictly enlarges their hull.** This does not assert that the new family alone contains every earlier class, or that the certificate is a literature-first result.

## 9. Second-moment certificate and four-qubit spin flip

### 9.1 Unrestricted density-operator certificate

For an arbitrary four-qubit density,
\[
H_3\ge0,\qquad \operatorname{Tr}H_3=8,\qquad H_3\le4I.
\]
If \(x=K_k(H_3)\), Cauchy–Schwarz within the top and remaining eigenvalue groups yields
\[
\operatorname{Tr}(H_3^2)\ge
F_k(x):=\frac{x^2}{k}+\frac{(8-x)^2}{16-k}.
\]
At the three intermediate reference boundaries,
\[
F_2(5)=\frac{92}{7},\qquad
F_3(6)=\frac{160}{13},\qquad
F_4(7)=\frac{37}{3}.
\]
The minimum is \(160/13\), since
\[
\frac{92}{7}-\frac{160}{13}=\frac{76}{91}>0,
\qquad
\frac{37}{3}-\frac{160}{13}=\frac1{39}>0.
\]

Moreover,
\[
F_k'(x)=\frac{32(x-k/2)}{k(16-k)},
\]
which is strictly positive above each displayed boundary. Therefore a strict violation of any of those three prefix bounds forces the moment strictly above its boundary threshold. The condition
\[
\operatorname{Tr}(H_3^2)\le\frac{160}{13}
\]
excludes all three violations. The first prefix follows from \(H_3\le4I\), and prefixes five onward from positivity and trace eight. Thus the stated sufficient condition is correct, including equality.

### 9.2 Pure-state expression

Write
\[
\rho=\frac{I+C_1+C_2+C_3+C_4}{16},
\qquad
S_j=\sum_{\operatorname{wt}(P)=j}(\operatorname{Tr}\rho P)^2.
\]

Equality of complementary pure-state marginal purities, summed over the four \(1|3\) cuts, gives
\[
2+\frac12S_1
=\frac18(4+3S_1+2S_2+S_3),
\]
hence
\[
S_3=12+S_1-2S_2.
\]
Global purity then gives
\[
S_4=3-2S_1+S_2.
\]

For four qubits,
\[
\Theta=Y^{\otimes4}\mathcal K,\qquad \Theta^2=+I.
\]
No general orthogonality follows. Its actual overlap is
\[
\eta=\operatorname{Tr}(\rho\widetilde\rho)
=|\langle\psi|\Theta\psi\rangle|^2.
\]
The spin flip changes the sign of odd-weight Pauli terms, so
\[
16\eta=1-S_1+S_2-S_3+S_4.
\]
Substitution yields
\[
S_2=S_1+2+4\eta.
\]

A weight-\(j\) Pauli term survives exactly \(4-j\) single-site traces, each with the appropriate factor two. Therefore
\[
H_3=\frac{4I+3C_1+2C_2+C_3}{8}.
\]
Pauli orthogonality gives
\[
\begin{aligned}
\operatorname{Tr}(H_3^2)
&=4+\frac94S_1+S_2+\frac14S_3\\
&=8+3S_1+2\eta.
\end{aligned}
\]
Thus
\[
3S_1+2\eta\le\frac{56}{13}
\]
is exactly the stated pure-state sufficient condition.

For the coherent family, its weight-zero/one support and its spin flip’s weight-three/four support are orthogonal, so \(\eta=0\) there. This is a support-specific fact, not an invalid four-qubit Kramers argument.

The moment certificate remains only an \(H_3\) sufficient condition. It does not by itself provide the unrestricted \(H_2\) premise required for this layerwise channel route.

## 10. Exact import boundaries and remaining obligations

The family proof above is reconstructed directly from S1. It does not need:

- the unreviewed F463 candidate as a premise;
- the external Song–Chen theorem as a premise;
- the earlier equal-\(W_4\) coefficient certificate as a premise;
- any stopped-review mathematical output.

S2 supplies the exact prior Class A/B definitions and scoped adopted conclusion. S3 supplies the exact equal-\(W_4\) orbit/hull scope. S4 supplies the separately stated all-biseparable scope and its prior-work qualification. I have not independently re-audited the linked author bodies, code, external publications, or historical finite-run receipts.

In particular:

- S2 alone must not be relabelled an all-\(1|3\)-separable theorem.
- S4’s all-biseparable conclusion must not be relabelled an unrestricted four-qubit theorem.
- The prior-work discussion supplies no novelty certification here.
- The historical finite checks are not executions by this reviewer and are not substitutes for the continuum reconstruction above.

For general compatible four-qubit pure inputs outside the proved sufficient classes, the unpaid \(H_3\) inequalities remain
\[
K_2(H_3)\le5,\qquad
K_3(H_3)\le6,\qquad
K_4(H_3)\le7.
\]
The first unproved extension step is a replacement for this family’s permutation-symmetry block constraints.

The unrestricted channel conclusion also remains unpaid. This layerwise route would additionally need a general \(H_2\) bound; a failure of an isolated layer bound would not itself establish a violation of the actual positively weighted channel output.

No physical counterexample, unrestricted four-qubit closure, unrelated AME claim, all-blocklength tensorization, arbitrary-dimension theorem, or ancillary extension follows from this review.

## 11. Findings and final verdict

**Findings:** None at the assigned mathematical scope. The compatible blocks, all claimed determinant identities, inertia argument, direct-sum prefixes, common-projector channel assembly, full-transpose transport, endpoint treatment, and strictness arguments have written support as reconstructed above.

The separately disclosed F480 ACK transport history remains historical process noncompliance; this return neither backdates delivery nor converts it into a new mathematical defect.

**overall_correctness: correct**

**explanation:** The complete coherent vacuum–\(W_4\) family proof supports both marginal-layer majorizations and all actual physical depolarizing-output prefixes, including arbitrary complex local-unitary images and finite mixtures; its strict enlargement and second-moment claims also withstand written reconstruction. This is scoped same-harness written support, not parent adoption, independent-family/kernel verification, novelty certification, or closure of the unrestricted four-qubit targets.

**confidence: 0.97**