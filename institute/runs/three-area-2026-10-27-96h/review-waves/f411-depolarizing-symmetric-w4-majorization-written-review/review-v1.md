# f411 WRITTEN review-v1 — complete return

**Scoped mathematical verdict: SUPPORTED.**  
**Findings: 0 FATAL / 0 MAJOR / 0 MINOR.**

The candidate’s actual-channel calculation, complete Bernstein certificate, physical-parameter extension, arbitrary-complex-projector quantifier, local-unitary/finite-mixture extension, and strict separation from the prior Class A/B hull admit the written reconstruction below. This is a **same-harness written review**, not the separate FINITE or PUBLIC gate, and does not itself change the parent candidate’s adoption status.

## 1. Binding, exposure, and method record

Wave:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f411-depolarizing-symmetric-w4-majorization-written-review/`

The manifest and receipt identifiers supplied by the caller are:

- Manifest: `3aa23f2fcfb72dcc0f5aeca7094fbddb0af06cbb379d53bf39750fa2f60ac638`.
- Freeze receipt: `24f49bc47f81cffef9fe5955db19cc96da629a1e8dfa110c1ef5a36f48e8dbb6`.
- Packet, as recorded in the parent receipt: `6b7a43a8778486d1cf7d4843912b985ef59b59e4d3de346b8a9c2a5f22a0377f`.

These hashes are **parent-supplied metadata**, not independently measured reviewer hashes.

I read the complete manifest, freeze receipt, all seven listed status-only controls, dispatch receipt, and parent metadata supply **before sending the administrative pre-body ACK to Main**. I then read the complete literal packet, in order, using these raw windows: LF 1–20, 21–40, 41–60, 61–80, 81–100, 101–120, 121–140, 141–160, 161–180, and 181–188. This includes all three source endings.

The mathematical inputs read were:

| ID | Frozen source | Complete coverage | Parent-supplied SHA-256 |
|---|---|---:|---|
| S1 | `review-waves/f410-parent-symmetric-four-qubit-w-channel-original-sector/author-candidate-v1.md` | LF 1–101 | `8802cec012ddeac98128311040f5a14fb3067dc17eb8833d9f34deca15894b12` |
| S2 | `dispositions/physics-2-two-coefficient-and-paired-repetition-all-prefix-majorization-parent-v1.md` | LF 1–48 | `8522551e1088a796288c73c9b1aad8fa40e197d74b6f7d41447392d07370d6c0` |
| S3 | `dispositions/physics-2-depolarizing-balanced-rank-prefix-parent-v1.md` | LF 1–37 | `cdda493b043002b208d8f92b7da352d2f165f6e03c07481a439b596be7b8b38d` |

Paths in this table are relative to the run root.

**Method boundaries maintained:**

- The seven controls were used only for status and exclusion boundaries.
- Held L1, CORE, PH-v8/registration consumers, AME-t28/compression consumers, privacy diagnostics, and other excluded payloads were not mathematical inputs.
- I did not follow the author-program, computation-output, or earlier-review links appearing in the packet.
- I did not read FINITE/PUBLIC sibling work.
- I performed no scientific execution, CAS/interpreter work, selected-instance probe, numerical search, or replay.
- The calculations below are written derivations of the entire prescribed parameter family and certificate, not new selected diagnostics.
- No external-model CLI, installation, build, test, formatter, publication, or working-tree write was performed.
- An assigned-path read-only `git diff` emitted no patch text; no conclusion about tracking status or source immutability is inferred from that absence.

The latest supplied clock is the **parent’s actual `/bin/date` observation, `2026-10-30T10:51:32-0700 PDT`**. It is not a reviewer-native start/completion observation or an elapsed-time measurement.

This complete body is returned for parent materialization as `review-v1.md`; it has not been written into the wave by this read-only role.

## 2. Per-claim dispositions

| Claim | Disposition | Exact scope / anchors |
|---|---|---|
| Actual physical matrix entries and nine-group spectrum | **SUPPORTED** | Reconstructed below from matrix units; S1 LF 23–44. |
| All output/reference degree-four Bernstein coefficients | **SUPPORTED** | Reconstructed below, including both endpoint columns; S1 LF 50–84. |
| Complete 5×17 minimum-gap certificate and all sixteen prefixes | **SUPPORTED** | All rows reproduced below; crossings, multiplicities, and degeneracies do not require a fixed output ordering. |
| Full physical interval and arbitrary complex consuming projector | **SUPPORTED** | Full transpose/spin flip and the receiving projector transformation checked explicitly; S1 LF 86. |
| Local-unitary orbit and finite convex hull with prior A/B class | **SUPPORTED** | Physical covariance and same-projector averaging; S1 LF 17, 88; S2 LF 7–18, 32. |
| W lies outside the entire prior A/B convex hull | **SUPPORTED** | Reduced-support/product-ray and purity argument below; S1 LF 19; S2 LF 9–14. |
| Reported parent executable histories and counts | **INCONCLUSIVE as independent execution/provenance checks** | S1 LF 90–97 was read as attributed reporting. Linked programs/receipts were not inspected or run and are unnecessary premises for this written proof. |
| Worldwide priority or precise relationship to the mentioned published comparators | **INCONCLUSIVE** | No primary-literature comparison was performed in this WRITTEN role. The candidate properly withholds novelty and original-target closure; S1 LF 3, 101. |

No mathematical claim in the assigned candidate was refuted.

## 3. Reconstruction of the actual physical output

Write

\[
\rho_W=|W_4\rangle\langle W_4|
=\frac14\sum_{i,j=1}^4 |e_i\rangle\langle e_j|,
\]

where \(e_i\) is the computational string with its unique occupied site at \(i\).

First take \(p=1-t\), \(0\le t\le1\), and put

\[
a=\frac{1+t}{2},\qquad b=\frac{1-t}{2}.
\]

The four one-qubit matrix-unit actions are

\[
\begin{aligned}
\Phi_{1-t}(|0\rangle\langle0|)
 &=a|0\rangle\langle0|+b|1\rangle\langle1|,\\
\Phi_{1-t}(|1\rangle\langle1|)
 &=b|0\rangle\langle0|+a|1\rangle\langle1|,\\
\Phi_{1-t}(|0\rangle\langle1|)
 &=t|0\rangle\langle1|,\\
\Phi_{1-t}(|1\rangle\langle0|)
 &=t|1\rangle\langle0|.
\end{aligned}
\]

These determine every entry of the four-qubit output.

### 3.1 Diagonal entries

Let \(x\) have Hamming weight \(k\).

In the contribution of \(|e_i\rangle\langle e_i|\):

- If \(i\) is occupied in \(x\), the contribution is
  \(a^{5-k}b^{k-1}\); there are \(k\) such \(i\).
- If \(i\) is unoccupied in \(x\), the contribution is
  \(a^{3-k}b^{k+1}\); there are \(4-k\) such \(i\).

Thus, for \(1\le k\le3\),

\[
d_k=\frac{k a^{5-k}b^{k-1}+(4-k)a^{3-k}b^{k+1}}4.
\]

The two singleton blocks are

\[
d_0=a^3b,\qquad d_4=ab^3.
\]

There are no other contributions to a diagonal entry: an input off-diagonal matrix unit retains off-diagonal factors at its two differing sites.

### 3.2 Off-diagonal entries

For \(i\ne j\), the term \(|e_i\rangle\langle e_j|\) contains one factor \(|1\rangle\langle0|\), one factor \(|0\rangle\langle1|\), and two factors \(|0\rangle\langle0|\).

A nonzero output entry therefore has:

- \(x_i=1,y_i=0\);
- \(x_j=0,y_j=1\);
- equal bits in \(x,y\) at the other two sites.

Consequently \(x,y\) have equal weight and differ by exactly one occupied-site exchange. If their weight is \(k\), the two unchanged sites contain \(k-1\) ones and \(3-k\) zeros. The entry is therefore

\[
g_k=\frac{t^2 a^{3-k}b^{k-1}}4,\qquad 1\le k\le3.
\]

The ordered pair \((i,j)\) is uniquely determined by \((x,y)\), so there is no extra factor of two.

This proves both the Hamming-weight block decomposition and the absence of every unlisted off-diagonal entry:

\[
M_k=d_k I+g_k A(J(4,k)).
\]

### 3.3 Johnson spectra and all sixteen eigenvalues

For \(k=1,3\), the Johnson graph is \(K_4\). Its adjacency matrix has eigenvalues \(3\) once and \(-1\) three times.

For \(k=2\), let \(B\) be the unsigned vertex-edge incidence matrix of \(K_4\). Then

\[
B^\mathsf TB=2I_6+A(J(4,2)),
\qquad
BB^\mathsf T=2I_4+J_4.
\]

The latter matrix has eigenvalues \(6\) once and \(2\) three times, hence rank four. Thus \(B^\mathsf TB\) has eigenvalues \(6,2,2,2,0,0\), and \(A(J(4,2))\) has eigenvalues

\[
4\ \text{once},\qquad 0\ \text{three times},\qquad -2\ \text{twice}.
\]

The actual output spectrum is therefore:

| Group | Multiplicity | Eigenvalue |
|---|---:|---|
| \(0\) | 1 | \(a^3b\) |
| \(1+\) | 1 | \(d_1+3g_1\) |
| \(1-\) | 3 | \(d_1-g_1\) |
| \(2+\) | 1 | \(d_2+4g_2\) |
| \(2\,0\) | 3 | \(d_2\) |
| \(2-\) | 2 | \(d_2-2g_2\) |
| \(3+\) | 1 | \(d_3+3g_3\) |
| \(3-\) | 3 | \(d_3-g_3\) |
| \(4\) | 1 | \(ab^3\) |

The multiplicities sum to sixteen.

All expressions are polynomials with nonnegative integer exponents. The endpoints therefore require neither division nor limiting choices: at \(t=0\), all sixteen eigenvalues coalesce at \(1/16\); at \(t=1\), the \(1+\) eigenvalue is one and all others are zero. Johnson eigenspaces can be chosen independently of \(t\), so degeneracies and later crossings do not invalidate these sixteen polynomial labels.

## 4. Independent derivation of every Bernstein coefficient

Let \(u=1-t\). Then

\[
a=t+\frac u2,\qquad b=\frac u2,
\qquad
B_j^4(t)=\binom4j t^j u^{4-j}.
\]

Define the reference polynomial

\[
R_r=a^{4-r}b^r,\qquad 0\le r\le4.
\]

Expanding directly,

\[
R_r
=\sum_{j=0}^{4-r}
\binom{4-r}{j}\frac{t^j u^{4-j}}{2^{4-j}}.
\]

Its degree-four Bernstein coefficient is consequently

\[
[B_j^4]R_r=
\frac{\binom{4-r}{j}}{2^{4-j}\binom4j},
\]

with an out-of-range binomial interpreted as zero.

Multiplying every coefficient by \(192\) gives:

| Reference polynomial | \(j=0\) | \(j=1\) | \(j=2\) | \(j=3\) | \(j=4\) |
|---|---:|---:|---:|---:|---:|
| \(R_0=a^4\) | 12 | 24 | 48 | 96 | 192 |
| \(R_1=a^3b\) | 12 | 18 | 24 | 24 | 0 |
| \(R_2=a^2b^2\) | 12 | 12 | 8 | 0 | 0 |
| \(R_3=ab^3\) | 12 | 6 | 0 | 0 | 0 |
| \(R_4=b^4\) | 12 | 0 | 0 | 0 | 0 |

These are derived coefficients, not coefficients inferred from values at sampled \(t\).

For the output diagonal polynomials,

\[
\begin{aligned}
d_0&=R_1,&
d_1&=(R_0+3R_2)/4,\\
d_2&=(R_1+R_3)/2,&
d_3&=(3R_2+R_4)/4,&
d_4&=R_3.
\end{aligned}
\]

For the off-diagonal polynomials,

\[
g_k=\frac14t^2
\left(t+\frac u2\right)^{3-k}
\left(\frac u2\right)^{k-1}.
\]

For \(j\ge2\), this gives

\[
[B_j^4]g_k
=
\frac{\binom{3-k}{j-2}}{2^{6-j}\binom4j},
\]

and the \(j=0,1\) coefficients vanish. Thus their scaled vectors are

\[
\begin{aligned}
192\,c(g_1)&=(0,0,2,12,48),\\
192\,c(g_2)&=(0,0,2,6,0),\\
192\,c(g_3)&=(0,0,2,0,0).
\end{aligned}
\]

Combining these expressions proves the following complete output coefficient table:

| Output group | Multiplicity | \(j=0\) | \(j=1\) | \(j=2\) | \(j=3\) | \(j=4\) |
|---|---:|---:|---:|---:|---:|---:|
| \(0\) | 1 | 12 | 18 | 24 | 24 | 0 |
| \(1+\) | 1 | 12 | 15 | 24 | 60 | 192 |
| \(1-\) | 3 | 12 | 15 | 16 | 12 | 0 |
| \(2+\) | 1 | 12 | 12 | 20 | 36 | 0 |
| \(2\,0\) | 3 | 12 | 12 | 12 | 12 | 0 |
| \(2-\) | 2 | 12 | 12 | 8 | 0 | 0 |
| \(3+\) | 1 | 12 | 9 | 12 | 0 | 0 |
| \(3-\) | 3 | 12 | 9 | 4 | 0 | 0 |
| \(4\) | 1 | 12 | 6 | 0 | 0 | 0 |

Every numerical entry in the candidate’s output coefficient table follows from these identities.

## 5. Complete minimum-gap table and its universal implication

### 5.1 Fixed reference order

For \(0\le t\le1\), \(a\ge b\ge0\). Adjacent reference groups obey

\[
a^{4-r}b^r-a^{3-r}b^{r+1}
=t\,a^{3-r}b^r\ge0,
\qquad 0\le r\le3.
\]

This proves the reference order without dividing by \(a\) or \(b\), including both endpoints:

\[
R_0\ \text{once},\quad
R_1\ \text{four times},\quad
R_2\ \text{six times},\quad
R_3\ \text{four times},\quad
R_4\ \text{once}.
\]

### 5.2 Coefficientwise maxima

For clarity, “\(x\) repeated \(m\)” below means \(m\) separate coefficient positions.

The output coefficients sorted in decreasing order, independently for each \(j\), are:

| \(j\) | Sorted output coefficients, scaled by 192 |
|---|---|
| 0 | \(12\) repeated 16 |
| 1 | \(18;\ 15\) repeated \(4;\ 12\) repeated \(6;\ 9\) repeated \(4;\ 6\) |
| 2 | \(24\) repeated \(2;\ 20;\ 16\) repeated \(3;\ 12\) repeated \(4;\ 8\) repeated \(2;\ 4\) repeated \(3;\ 0\) |
| 3 | \(60;\ 36;\ 24;\ 12\) repeated \(6;\ 0\) repeated \(7\) |
| 4 | \(192;\ 0\) repeated \(15\) |

The corresponding reference coefficients, kept in the fixed reference eigenvalue order, are:

| \(j\) | Reference coefficients, scaled by 192 |
|---|---|
| 0 | \(12\) repeated 16 |
| 1 | \(24;\ 18\) repeated \(4;\ 12\) repeated \(6;\ 6\) repeated \(4;\ 0\) |
| 2 | \(48;\ 24\) repeated \(4;\ 8\) repeated \(6;\ 0\) repeated \(5\) |
| 3 | \(96;\ 24\) repeated \(4;\ 0\) repeated \(11\) |
| 4 | \(192;\ 0\) repeated \(15\) |

These multiplicity lists account for all sixteen positions in each column.

The successive differences “reference coefficient minus sorted output coefficient” are therefore:

- \(j=0,4\): sixteen zeros.
- \(j=1\):
  \[
  (6,3,3,3,3,0,0,0,0,0,0,-3,-3,-3,-3,-6).
  \]
- \(j=2\):
  \[
  (24,0,4,8,8,-8,-4,-4,-4,-4,0,-8,-4,-4,-4,0).
  \]
- \(j=3\):
  \[
  (36,-12,0,12,12,-12,-12,-12,-12,0,0,0,0,0,0,0).
  \]

Their cumulative sums, starting at \(k=0\), prove the complete table:

| \(j\) | \(192G_{j,k}\), for \(k=0,1,\ldots,16\) |
|---|---|
| 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| 1 | 0, 6, 9, 12, 15, 18, 18, 18, 18, 18, 18, 18, 15, 12, 9, 6, 0 |
| 2 | 0, 24, 24, 28, 36, 44, 36, 32, 28, 24, 20, 20, 12, 8, 4, 0, 0 |
| 3 | 0, 36, 24, 24, 36, 48, 36, 24, 12, 0, 0, 0, 0, 0, 0, 0, 0 |
| 4 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |

Thus all 85 entries of the prescribed 5×17 table are established and nonnegative.

### 5.3 Why this proves every subset, crossing, and projector

Let \(\lambda_i(t)\), \(1\le i\le16\), denote the sixteen polynomial eigenvalue positions, with multiplicities retained. Let \(c_{j,i}\) be their Bernstein coefficients, and let \(r_{j,k}\) be the coefficient of the ordered reference \(k\)-prefix.

For any fixed subset \(I\) of \(k\) positions,

\[
\sum_{i\in I}c_{j,i}
\le \text{sum of the \(k\) largest coefficients in column }j.
\]

Hence the table proves

\[
r_{j,k}-\sum_{i\in I}c_{j,i}\ge G_{j,k}\ge0
\]

for every \(j\). Since each \(B_j^4(t)\ge0\),

\[
K_k(D_t)-\sum_{i\in I}\lambda_i(t)
=
\sum_{j=0}^4
\left(r_{j,k}-\sum_{i\in I}c_{j,i}\right)B_j^4(t)
\ge0.
\]

This holds for **every** subset \(I\). Taking the maximum over subsets proves

\[
K_k(\Lambda_{1-t}(\rho_W))\le K_k(D_t),
\qquad k=1,\ldots,16.
\]

The subsets maximizing different coefficient columns need not coincide. They serve only as separate upper bounds on the coefficients of every fixed subset. No assertion of simultaneous maximization is used.

Likewise, no output eigenvalue ordering is assumed to persist with \(t\). At each \(t\), whichever subset realizes the top-\(k\) sum is among the subsets already bounded. Repeated eigenvalues, crossings, and endpoint degeneracies are therefore included.

Finally, the Ky Fan variational characterization applies to **every complex orthogonal rank-\(k\) projector**. In an output eigenbasis, the diagonal entries of such a projector lie in \([0,1]\) and sum to \(k\), so its trace against the output is at most the largest \(k\)-eigenvalue sum. Therefore

\[
\operatorname{Tr}\!\left(Q\Lambda_{1-t}(\rho_W)\right)
\le K_k(D_t)
\]

for every consuming projector stated in the candidate.

## 6. Negative branch and consuming-projector transport

Define the one-qubit linear spin-flip map

\[
\mathcal S(X)=YX^\mathsf TY.
\]

For every \(2\times2\) matrix,

\[
\mathcal S(X)=\operatorname{Tr}(X)I-X.
\]

Consequently,

\[
\begin{aligned}
\mathcal S(\Phi_{1-t}(X))
&=\mathcal S\!\left(tX+\frac{1-t}{2}\operatorname{Tr}(X)I\right)\\
&=-tX+\frac{1+t}{2}\operatorname{Tr}(X)I\\
&=\Phi_{1+t}(X).
\end{aligned}
\]

Tensoring this identity over all four sites gives, with \(F=Y^{\otimes4}\),

\[
\Lambda_{1+t}(\rho)
=F\,[\Lambda_{1-t}(\rho)]^\mathsf T F.
\]

This is a **full transpose**, not a partial transpose. The equality holds for arbitrary four-qubit input operators, including entangled densities.

The right side has the same spectrum as \(\Lambda_{1-t}(\rho)\). On the product input, the negative branch exchanges \(a,b\) at every site, leaving the reference eigenvalue multiset unchanged.

The consuming-side transformation is also correct. Here \(F^\mathsf T=F\), and

\[
\operatorname{Tr}\!\left(QF A^\mathsf T F\right)
=
\operatorname{Tr}\!\left(FQ^\mathsf TF\,A\right).
\]

If \(Q\) is a complex orthogonal rank-\(k\) projector, then

\[
Q'=FQ^\mathsf TF
\]

is again a complex orthogonal rank-\(k\) projector. Thus the positive-branch inequality receives and processes precisely the projector obtained from the negative branch; it is not restricted to real \(Q\).

For \(1\le p\le4/3\), \(p=1+t\) has \(0\le t\le1/3\), which lies inside the positive-branch proof interval. Together with \(0\le p\le1\), this establishes the entire physical interval.

## 7. Local-unitary orbit and finite convex mixtures

For any physical one-qubit unitary \(U\),

\[
\Phi_p(UXU^\dagger)=U\Phi_p(X)U^\dagger.
\]

Therefore the fourfold channel is covariant under arbitrary physical local product unitaries \(V\). For any fixed consuming projector \(Q\),

\[
\operatorname{Tr}\!\left(Q\Lambda_p(V\rho_WV^\dagger)\right)
=
\operatorname{Tr}\!\left(V^\dagger QV\,\Lambda_p(\rho_W)\right)
\le K_k(D_t).
\]

The transformed projector is admissible for every \(V\); no common maximizing projector is needed.

Now let a density be any finite mixture of such local-unitary W images and members of the previously adopted class \(C\) from S2. For the **same** \(Q\), linearity gives the weighted sum of inequalities, each with the same bound \(K_k(D_t)\). Because the weights sum to one, the mixture satisfies that bound too.

The imported statement from S2 is only its adopted all-physical-\(p\), all-projector, all-prefix theorem on its explicitly defined finite Class A/B hull. No input-independent channel or logical-unitary covariance is imported or required here.

## 8. Strict separation from the complete prior A/B convex hull

Fix any physical pairing \(P|P^c\) into two pairs. By permutation symmetry,

\[
|W_4\rangle
=
\frac1{\sqrt2}
\left(
|\psi^+\rangle_P|00\rangle_{P^c}
+
|00\rangle_P|\psi^+\rangle_{P^c}
\right),
\]

where

\[
|\psi^+\rangle=(|01\rangle+|10\rangle)/\sqrt2.
\]

The two factors on each side are orthonormal. Thus the Schmidt rank across every such cut is two, and the reduced support on either pair is exactly

\[
L=\operatorname{span}\{|00\rangle,\ |01\rangle+|10\rangle\}.
\]

A vector in this support has the form

\[
x|00\rangle+y(|01\rangle+|10\rangle),
\]

with coefficient matrix

\[
\begin{pmatrix}
x&y\\
y&0
\end{pmatrix}.
\]

It is a nonzero product vector exactly when this matrix has rank one. Its determinant is \(-y^2\), which over the complex numbers vanishes exactly when \(y=0\). Hence **\(L\) contains exactly one product ray**.

### 8.1 Exclusion of Class A

A Class A pure vector is a sum of at most two strings from one physical local orthonormal product basis. Across a paired cut it therefore has the form

\[
c_0\,u_0\otimes v_0+c_1\,u_1\otimes v_1,
\]

where each \(u_i\) and \(v_i\) is a product vector on its physical pair.

If its Schmidt rank across that cut is two, the two \(u_i\) are independent and both lie in the reduced support. That support consequently contains at least two independent product rays.

W has rank two but its reduced support has only one product ray. It cannot be Class A.

### 8.2 Exclusion of Class B

For a Class B state, choose its defining pairing and local physical bases. On either pair, the state is supported in a locally rotated repetition space

\[
E=\operatorname{span}\{|e_0f_0\rangle,\ |e_1f_1\rangle\}.
\]

The two displayed vectors are independent product vectors.

If the pure W density were a Class B density, its pair reduction would be supported in \(E\). Its rank is two, so its support would equal \(E\), contradicting the one-product-ray property.

This argument applies to every allowed pairing because W is permutation symmetric. Physical local product unitaries preserve product rays and independence, so changing local bases cannot avoid the contradiction.

### 8.3 Exclusion of the entire convex hull

Suppose a rank-one density \(P_W\) had a finite positive decomposition

\[
P_W=\sum_\ell w_\ell \sigma_\ell,
\qquad w_\ell>0,
\]

with each \(\sigma_\ell\) an allowed A/B density.

For every \(z\perp W\),

\[
0=\langle z|P_W|z\rangle
=\sum_\ell w_\ell\langle z|\sigma_\ell|z\rangle.
\]

Every summand is nonnegative. Thus each \(\sigma_\ell\) vanishes on the orthogonal complement of W. Positivity then forces its support into \(\operatorname{span}\{W\}\), and unit trace forces \(\sigma_\ell=P_W\).

That would put W itself in A or B, already excluded. Hence W lies outside the entire prior finite convex hull.

This establishes a **strict state-class enlargement**. It does not use Schmidt rank alone: rank two is used to identify the full reduced support, and the decisive invariant is the number of product rays in that support.

## 9. Source, priority, and original-target ceiling

The following distinctions remain necessary:

1. S2 supplies a prior full-majorization theorem on its explicit Class A/B hull, not all four-qubit densities.
2. S3 supplies unrestricted-density prefixes only for \(k\in\{5,6,10,11\}\). Its statement is not an unrestricted all-prefix theorem.
3. The present reconstruction adds full majorization on the equal-amplitude W local-unitary orbit and the stated finite hull. It does not establish all unequal-amplitude W states.
4. No theorem for all \(1|3\)-separable states, all biseparable states, unrestricted \(k=3\), or the original whole target follows by combining those scopes.
5. No published log-determinant or approximate-majorization statement has been imported as a premise. The precise literature comparison remains for the separate PUBLIC gate.
6. This review is not a novelty certificate, original-source authenticity audit, human review, independent-model-family review, or formal/kernel proof.
7. The reported parent computations and their control counts remain attributed reports in this review. The written proof above does not depend on their execution or outcome.

## 10. Final verdict fields

**overall_correctness:** correct

**explanation:** The scoped candidate is supported by a complete written derivation of the actual physical output, all coefficient vectors, the entire 5×17 certificate, the negative-branch projector transport, and the strict Class A/B hull separation. No actionable mathematical defect was found; separate finite execution, public-source comparison, and parent adoption remain outside this verdict.

**confidence:** 0.98