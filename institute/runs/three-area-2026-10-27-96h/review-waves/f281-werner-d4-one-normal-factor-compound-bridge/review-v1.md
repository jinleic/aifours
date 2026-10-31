# f281 — one-normal-factor compound bridge — review v1

## 1. Verdict and exact scope

**Mathematical verdict: 0 FATAL / 0 MAJOR / 0 MINOR.**

**Overall correctness: correct within the stated scope and the explicitly named f274 import.** Confidence: **0.97** for this written-mathematical assessment, not for provenance or excluded assurance categories.

The proof establishes exactness of the optimized compound certificate under the common-basis linear-forest hypothesis, and supplies an additional basis-invariant sufficient region. It does **not** establish \(\eta\le 2L\) for every one-normal pair, let alone unrestricted T2/T3/Z2. No adoption decision is made here. Reviewer process qualifications, including compulsory extra-manifest process reads, are disclosed in section 8 rather than silently waived.

## 2. Frozen inputs and dependency boundary

The assigned directory is:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f281-werner-d4-one-normal-factor-compound-bridge/`

Source labels:

- **W:** `manifest-v1.json` in the assigned directory.  
  SHA-256: `00e39b00c7d93923ff80e14df7c9520a0582bc826b7b262d892bad139d075cbc`  
  **4122 bytes / 36 LF**.

- **M:** `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart/frontier-20261029-d4-one-normal-factor-compound-bridge-v1.md`  
  SHA-256: `70fb5dca24b0d058d47459eb3d52f98bc2fbef8b5c54c867473ca5830005ba70`  
  **13789 bytes / 103 LF**.

- **N:** `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/physics-1-werner-d4-t2-additive-compound-perron-certificate-and-open-complement-parent-v1.md`  
  SHA-256: `86600a440a72443460875bb832d0c71eb9b4f8ca58bd9cbf10080653d41a5655`  
  **5741 bytes / 22 LF**.

Each object’s SHA-256, byte count, and LF count matched **before its body was displayed**. A later metadata-only check found the same three hashes/counts and confirmed a **final LF in all three files**. Thus the displayed terminal windows include the actual endings, without an undisplayed unterminated suffix.

The named conditional import is **f274**, at N LF 5–9: the additive-compound definition and eigenvalues; \(S_2\le\eta\); the real-symmetric hard-core compression identity/bound; and normal-pair exactness. I reconstructed the portions used below.

N’s other adopted region, prior review outcome, and historical verification statements are not substitute evidence for M. I did not open any review, disposition, source, or script merely referenced inside M or N. In particular, the f168 document was not an additional input; the narrow one-supported-site fact invoked at M LF 50 is reconstructed below instead of importing its unseen proof or any broader claim.

## 3. LF-located findings

**None.** There is no FATAL, MAJOR, or MINOR mathematical finding to quote as a defective assertion.

The following exact source phrases delimit this verdict and are not findings:

- **M LF 42:** “If a single site-2 basis V makes the offdiagonal graph of **each** H_i(V) a linear forest”.
- **M LF 46:** “permutations and diagonal gauges in Lemma 2.1 are only devices for calculating each block's invariant radius, not fictitious independently chosen physical V's.”
- **M LF 28:** “Minimizing (1) over V produces a **restricted-basis upper bound** on η”.
- **M LF 99:** “We have neither a proof that this minimax is ≤2L nor a basis-independent lower bound >2L”.

## 4. Independent written reconstruction

### 4.1. Compound certificate and exact 120-dimensional reduction

For traceless \(A,B\), direct expansion gives

\[
\|A\otimes I+I\otimes B\|_F^2
=4(\|A\|_F^2+\|B\|_F^2)=4L,
\]

because the mixed trace vanishes. If \(H\) has eigenvalues
\(\lambda_1\ge\cdots\ge\lambda_{16}\ge0\), its additive second compound has eigenvalues \(\lambda_p+\lambda_q\), \(p<q\). Consequently,

\[
\lambda_{\max}K(H)=S_2(X).
\]

For every local basis, the Rayleigh comparison

\[
|z^\dagger Kz|
\le |z|^{T}|K||z|
\]

implies \(S_2(X)\le\rho(|K|)\). Here \(|K|\) is real symmetric nonnegative, so its largest eigenvalue is its Perron root; no unsupported spectral-radius assertion for a general nonsymmetric matrix is involved. The minimum defining \(\eta\) is attained because \(U(4)\times U(4)\) is compact and the relevant symmetric-matrix eigenvalues are continuous.

When \(A\) is diagonal, \(X\) is the direct sum of \(B+a_iI\). For one fixed common \(V\) on site 2, \(H\) is therefore the direct sum of the four \(H_i(V)\). Exterior squaring gives exactly:

- four same-block spaces, each of dimension \(\binom42=6\);
- six cross-block spaces, each of dimension \(4\cdot4=16\).

Thus \(4\cdot6+6\cdot16=120\). There is no missing sector.

The same-block operator is \(K(H_i)\). On the \((i,j)\) cross sector it is

\[
H_i\otimes I+I\otimes H_j.
\]

The two offdiagonal summands have disjoint support: one changes the first coordinate and the other the second. Their only overlap is on the diagonal, where both entries are nonnegative because \(H_i,H_j\) are PSD. Taking entrywise modulus therefore gives exactly

\[
|H_i|\otimes I+I\otimes|H_j|.
\]

Its Perron root is \(r_i+r_j\), either by the tensor-product eigenbasis or by the largest-eigenvalue formula for a symmetric Kronecker sum.

This proves M LF 24 exactly:

\[
\rho(|K(H)|)=
\max\left\{
\max_i\rho(|K(H_i)|),\
\max_{i<j}\bigl[\rho(|H_i|)+\rho(|H_j|)\bigr]
\right\}.
\]

All four \(H_i\) in this identity use the **same \(V\)**. Minimizing this expression over \(V\) fixes \(A\) in a diagonal basis, hence gives an upper bound on the unrestricted minimum \(\eta\), not an equality with that minimum in general. This direction is correctly stated at M LF 28 and is essential to the unpaid-step boundary.

### 4.2. Linear-forest exactness and evaluation-only gauges

A diagonal phase gauge makes every edge of each path component of \(H\) positive: there is no cycle consistency condition. A vertex permutation places each component consecutively. Such transformations induce a monomial unitary on the wedge basis, so taking entrywise moduli changes only by permutation similarity. Both modulus radii are unchanged.

After this ordering and gauge, the only offdiagonal one-particle moves are between consecutive vertices within a path. An allowed move of one of two occupied distinct vertices cannot overtake the other occupied vertex: the move would have to collide with it. Components placed consecutively also cannot exchange particles. Therefore the fermionic reordering sign on every nonzero compound offdiagonal entry is positive. Its diagonal is \(h_{pp}+h_{qq}\ge0\).

Both \(H\) and \(K(H)\) are now entrywise nonnegative as well as Hermitian PSD, giving

\[
\rho(|H|)=\lambda_1(H),\qquad
\rho(|K(H)|)=\lambda_1(H)+\lambda_2(H).
\]

Applying these **numerical identities** separately to the \(H_i\) in the already fixed common basis is legitimate even if their paths, orderings, and phases differ. It does not implement four different physical site-2 bases. In particular, the original cross-sector radius remains \(r_i+r_j\), with each \(r_i\) evaluated through its invariant single-block identity.

The resulting maximum consists of the largest within-block eigenvalue pair and the largest pair drawn from distinct blocks. These exhaust every possible pair among the eigenvalues of \(\bigoplus_iH_i\). Hence the radius in this actual admissible basis equals \(S_2(X)\). Together with the universal lower bound \(S_2\le\eta\), this proves

\[
\eta=S_2
\]

under M LF 42’s common-basis hypothesis.

### 4.3. Final \(S_2\le2L\) for one normal factor: narrow fact reconstructed

This step is not supplied by an unrestricted spectral-radius lemma or an arbitrary-\(T\) norm inequality. The following reconstructs the qualified one-supported-site argument needed at M LF 50.

Use matrix vectorization with the two output/input site pairs grouped together. Let

\[
\omega=\sum_{k=1}^4e_k\otimes e_k,\qquad
P=\frac{|\omega\rangle\langle\omega|}{4}
\]

on one site pair. Define

\[
R=P_1\otimes(I-P_2)+(I-P_1)\otimes P_2,
\qquad
Q_j=I-2P_j.
\]

Then \(R\) is an orthogonal projection and

\[
Q_1\otimes Q_2=I-2R.
\]

Tracelessness implies that \(\operatorname{vec}(X)\), for \(X=A\otimes I+I\otimes B\), lies in the range of \(R\).

Compress the input leg of \(Q_1\) to any two-dimensional subspace \(E\). After a paired conjugate change of basis, its nontrivial part on the corresponding two-dimensional output space \(F\) and \(E\) is

\[
I_{F\otimes E}-\frac{|\omega_2\rangle\langle\omega_2|}{2}.
\]

This has the positive-product Haar decomposition

\[
3\int
\bigl(I_F-|\bar u\rangle\langle\bar u|\bigr)
\otimes |u\rangle\langle u|\,d\mu(u),
\]

where \(\mu\) is normalized Haar measure on unit vectors of \(\mathbb C^2\). The identity follows from

\[
\int |\bar u\rangle\langle\bar u|
\otimes|u\rangle\langle u|\,d\mu(u)
=
\frac{I+|\omega_2\rangle\langle\omega_2|}{6}.
\]

The remaining output space contributes the separable positive operator \(I_{F^\perp}\otimes I_E\). A one-dimensional support can be enlarged to two dimensions before compression.

On the other site, a vector represented by a matrix \(C\) of rank at most two satisfies

\[
\langle\operatorname{vec}(C),Q_2\operatorname{vec}(C)\rangle
=
\|C\|_F^2-\frac{|\operatorname{Tr}C|^2}{2}\ge0,
\]

because

\[
|\operatorname{Tr}C|
\le \sigma_1(C)+\sigma_2(C)
\le\sqrt2\,\|C\|_F.
\]

Contracting a global Schmidt-rank-at-most-two vector against a product vector on the first site leaves a matrix of rank at most two on the second site. Integrating the preceding nonnegative expectations against the positive-product decomposition proves

\[
\langle \operatorname{vec}(Y),(I-2R)\operatorname{vec}(Y)\rangle\ge0
\]

whenever \(\operatorname{vec}(Y)\) has Schmidt rank at most two and the stated two-dimensional support on one input leg. Consequently,

\[
\|R\operatorname{vec}(Y)\|^2\le\frac{\|Y\|_F^2}{2}.
\]

For normal \(A\), choose its diagonal basis and choose the top two right singular vectors of \(X\) inside its direct-sum blocks. They involve at most two site-1 labels, including in degenerate cases. Let \(\Pi\) be their rank-two orthogonal projection, let \(s=S_2(X)\), and put \(Y=X\Pi\). Then:

- \(\operatorname{rank}Y\le2\);
- its input site-1 leg has support of dimension at most two;
- \(\|Y\|_F^2=s\);
- \(\langle Y,X\rangle=s\).

Since \(\operatorname{vec}(X)\) is in the range of \(R\),

\[
s^2
=|\langle Y,X\rangle|^2
\le
\|R\operatorname{vec}(Y)\|^2\|X\|_F^2
\le\frac{s}{2}(4L).
\]

For \(s>0\), this gives \(s\le2L\); for \(s=0\), the result is immediate.

This proves precisely the one-normal inequality needed in Theorem 2.2. It does not claim certificate exactness for an arbitrary one-normal pair.

### 4.4. Concrete structural classes

For a single common unitary block decomposition of \(B\) into blocks of size at most two, every shifted Gram matrix \(H_i\) has that same decomposition. Each two-vertex Hermitian block has at most one edge. No separate block-trace condition occurs anywhere in this argument; only global \(\operatorname{Tr}B=0\) is needed for the stated \(L\) and T2 normalization.

If \(B\) is upper or lower bidiagonal in one unitary basis, \(B^\dagger B\) is tridiagonal in that basis. Therefore

\[
B^\dagger B+\bar a_iB+a_iB^\dagger+|a_i|^2I
\]

has a subgraph of a path for every \(i\).

The four-vertex nilpotent shift is a genuine irreducible nonnormal example: it and its adjoint generate endpoint projections and then all matrix units, so an orthogonal reducing projection must be scalar. A nonzero scalar multiple does not change that conclusion.

Thus the theorem genuinely includes nonnormal \(B\) outside the normal-pair class. The more general common-\(H_i\) graph criterion need not be replaced by either of these two concrete sufficient examples.

### 4.5. PSD4 compound estimate, including constants and degeneracies

Write \(t=\operatorname{Tr}H\) and \(h=\|H\|_F\). For PSD \(H\), its diagonal is nonnegative and the compound entries give the exact hard-core symmetric compression

\[
|K(H)|=
J_+^\dagger\bigl(|H|\otimes I+I\otimes|H|\bigr)J_+.
\]

Since \(J_+\) is an isometry, a Rayleigh quotient bounds its largest eigenvalue by

\[
2\rho(|H|)\le2h.
\]

This is a real-symmetric compression argument, not a general nonnegative-compression rule.

For \(H=uu^\dagger\), let \(s_i=|u_i|\). The embedding of a real unit pair vector is a real symmetric zero-diagonal \(4\times4\) matrix \(W\) with \(\|W\|_F=1\). Its Rayleigh quotient is \(2\|Ws\|^2\). Since \(\operatorname{Tr}W=0\), any eigenvalue \(\mu\) obeys

\[
\mu^2\le3\sum_{\text{other eigenvalues}}\nu^2,
\]

and hence \(\|W\|_{\rm op}^2\le3/4\). The quotient is at most \(3\|u\|^2/2\).

For general PSD \(H\), decompose it into positive rank-one summands, apply the entrywise triangle inequality to their compounds, monotonicity of the Perron root, and subadditivity of \(\lambda_{\max}\) for real symmetric matrices. This gives

\[
\rho(|K(H)|)\le\frac{3t}{2}.
\]

The constant is attained when all \(|u_i|\) are equal. If \(|u_i|^2=c\), then \(|K(H)|\) has diagonal \(2c\) and offdiagonal \(c\) on \(J(4,2)\), whose degree is four. Its Perron root is \(6c=3t/2\). This is an all-variable equality construction, not a finite diagnostic used to prove the bound.

For the centered estimate, set \(H=\alpha I+C\), \(\alpha\ge0\). Even when \(C\) is not PSD, the diagonal inequality

\[
|c_{pp}+c_{qq}|\le|c_{pp}|+|c_{qq}|
\]

gives entrywise domination by

\[
J_+^\dagger\bigl(|C|\otimes I+I\otimes|C|\bigr)J_+.
\]

Thus \(\rho(|K(C)|)\le2\|C\|_F\), and the triangle inequality gives

\[
\rho(|K(H)|)
\le2\alpha+2\sqrt{h^2-2\alpha t+4\alpha^2}.
\]

Put \(d=\sqrt{h^2-t^2/4}\). PSD implies \(0\le d\le\sqrt3\,t/2\). For \(d>0\), minimizing the preceding expression gives

\[
\alpha=\frac t4-\frac{d}{2\sqrt3}\ge0
\]

and value \(t/2+\sqrt3\,d\). If \(d=0\), then \(H=(t/4)I\), and \(\alpha=t/4\) gives the same value directly; \(H=0\) is included.

Therefore,

\[
\rho(|K(H)|)\le
\min\left\{
\frac{3t}{2},\
2h,\
\frac t2+\sqrt3\sqrt{h^2-\frac{t^2}{4}}
\right\}
\]

holds with the stated constants. The combined bound is sharp, in particular at the uniform-modulus rank-one examples above and at scalar PSD matrices for the centered term.

### 4.6. Basis invariants and sufficient inequalities

Tracelessness of \(B\) gives \(t_i=b+4|a_i|^2\). Expanding

\[
H_i=B^\dagger B+\bar a_iB+a_iB^\dagger+|a_i|^2I
\]

yields

\[
h_i^2=
p+4|a_i|^2b+4|a_i|^4
+4\operatorname{Re}(\bar a_i u)
+2\operatorname{Re}(\bar a_i^{\,2}v),
\]

with \(b,p,u,v\) exactly as defined at M LF 83. The two contributions of \(2|a_i|^2b\) add to the stated coefficient four; the terms linear in \(\operatorname{Tr}B\) vanish. All these traces, and \(t_i,h_i\), are invariant under the one common conjugation of \(B\).

The same-block radius is bounded by the minimum in Lemma 3.1, and each cross-block radius by \(h_i+h_j\). Thus the two inequalities (5) bound the exact A-diagonal radius by \(2L\) in **every** site-2 basis. They are sufficient for the actual \(\eta\), without requiring simultaneous diagonalization and without asserting necessity.

### 4.7. Equal eigenvalue moduli and strict case

If all \(|a_i|=r\), then

\[
\|A\|_F^2=4r^2,\qquad t_i=b+4r^2=L.
\]

PSD gives \(h_i\le t_i=L\). The same-block upper bound is at most \(3L/2\), while every cross upper bound is at most \(2L\). Hence (5) holds for every traceless \(B\).

For four distinct \(a_i\) and \(L>0\), equality \(h_i=L\) is possible only when \(H_i\) has rank one. Two different shifts cannot both have rank at most one: their difference is \((a_i-a_j)I\), of rank four, while the rank of a difference of two rank-one matrices is at most two. As \(t_i=L>0\), no \(H_i\) has rank zero.

Thus at most one \(h_i\) equals \(L\), every cross sum is strictly below \(2L\), and the same-block terms are at most \(3L/2<2L\). The maximum of finitely many such strict bounds remains strict. This proves \(\eta<2L\) under exactly the stated distinctness and positivity hypotheses.

### 4.8. Relative openness and scope of structural extension

At \(B=0\) and a nonzero normal traceless \(A\) with four distinct equal-modulus eigenvalues, the strict inequalities just proved hold. Eigenvalues can be labeled continuously locally on the normal simple-spectrum stratum, and the trace/norm expressions are continuous, so strictness persists in the claimed relative neighborhood.

For a fixed reducing dimension \(k\), the complex Grassmannian contributes \(2k(4-k)\) real parameters, while the two unrestricted blocks with only one global complex trace constraint contribute \(30-4k(4-k)\). The total is

\[
30-2k(4-k)<30.
\]

For upper bidiagonal traceless matrices there are six complex parameters, hence twelve real parameters, and conjugation by \(U(4)\) adds at most sixteen: total at most \(28<30\). Lower bidiagonal matrices are covered by reversing the basis. Countable smooth charts and the dimension/Sard argument give empty interior. Compactness of the projections/unitaries, together with Frobenius boundedness of the corresponding blocks, proves closedness under convergent sequences.

The square-normal locus is a proper real-algebraic locus: the length-four shift has nonnormal square, so the commutator polynomial defining it is not identically zero on traceless matrices. Its complement is dense and open. Intersecting these dense open complements inside the strict \(B\)-neighborhood gives the claimed irreducible, non-bidiagonalizable \(B\) with \(B^2\) nonnormal.

This verifies existence outside the **two concrete \(B\)-classes** at M LF 54–55. It is not a converse characterization of the more general simultaneous \(H_i\)-forest condition at M LF 42, and no such converse is used in this review. The open neighborhood is relative to normal \(A\), not an ambient open set of all matrix pairs.

### 4.9. Disclosed diagnostics: independently checked, not theorem evidence

The author’s disclosed symbolic diagnostics were not used as premises for the theorem, sufficient region, provenance, or adoption. Their descriptions can nevertheless be checked by written algebra, as requested.

**Branching tree, M LF 93.** The star adjacency has eigenvalues \(\sqrt3,0,0,-\sqrt3\), giving the stated PSD threshold and

\[
\lambda_1(H)+\lambda_2(H)=2t+\sqrt3|s|.
\]

In the two-particle graph, the three configurations containing the center connect to the three configurations containing two leaves; every vertex has degree two and the connected graph is \(C_6\). Thus the compound modulus is

\[
2tI+|s|\operatorname{Adj}(C_6),
\]

with Perron root \(2t+2|s|\). This is strictly larger for \(s\ne0\). It disproves a blanket extension of the single-block exactness lemma from paths to all trees; it is not a physical \(\eta\) counterexample.

**Sufficient-test limitation, M LF 95.** Here \(P\) uses the rank-one **orthogonal projector** convention explicitly given by the named import at N LF 9, not an arbitrary rank-one matrix. Writing \(q=|s|^2\), \(A=B=s(4P-I)\) gives \(L=24q\) and \(\eta=40q\). The \(3s\) block has eigenvalues \(36q,4q,4q,4q\), so \(t=48q\) and \(h^2=1344q^2\). The three bounds are

\[
72q,\quad16\sqrt{21}\,q,\quad72q;
\]

their minimum is \(72q>48q\). This demonstrates non-necessity of (5), not failure of the certificate.

**Centering, M LF 97.** With the same projector convention and \(B=0\), the \(3s\) block is \(9qI\): \(t=36q\), \(h=18q\), and the centered expression is \(18q\). The best uncentered expression is \(36q>2L=24q\). The remaining blocks have \(h=2q\), so the largest cross upper bound is \(20q<24q\). The diagnostic’s stated role and constants are correct.

These are auxiliary identities only. No author program, numerical search, selected physical q-value, or executable mathematical control was run or credited.

## 5. Per-claim dispositions

“SUPPORTED” below means same-harness written reconstruction of the identified statement, with the named dependency boundaries; it is not a parent disposition.

| Claim | Source LF | Disposition | Boundary / named import |
|---|---|---|---|
| Compound definition, \(S_2\le\eta\), attained minimum | M 11–15; N 5–6 | SUPPORTED | f274 definitions and certificate; reconstructed in 4.1 |
| Exact \(120=4\times6+6\times16\) sector reduction and max-radius formula | M 17–28 | SUPPORTED | One common \(V\); \(A\) held diagonal; restricted minimum is only an upper bound on \(\eta\) |
| Single PSD linear-forest modulus exactness | M 32–40 | SUPPORTED | Path components, not arbitrary trees |
| Common-basis linear-forest \(\eta=S_2\) | M 42–48 | SUPPORTED | Independent per-block monomial operations are evaluation-only |
| \(S_2\le2L\) for normal \(A\), as used in Theorem 2.2 | M 50 | SUPPORTED | Narrow one-supported-site fact reconstructed in 4.3; no unseen f168 statement imported |
| Globally traceless \(2+2\) reducible and unitarily bidiagonal \(B\) consequences, including irreducible nonnormal examples | M 54–58 | SUPPORTED | No separate block-trace assumption |
| PSD4 minimum bound and sharp \(3t/2\) constant | M 62–72 | SUPPORTED | f274 real-symmetric compression, plus rank-one decomposition and centered proof |
| Trace expansion and basis-invariant sufficient condition | M 76–85 | SUPPORTED | Sufficient, not necessary; valid under every common \(V\) |
| Four equal \(A\)-eigenvalue moduli: \(\eta\le2L\) for every traceless \(B\) | M 87 | SUPPORTED | \(A\) normal; includes degenerate and zero cases without claiming strictness there |
| Strict \(\eta<2L\) for four distinct eigenvalues and \(L>0\) | M 87 | SUPPORTED | Rank-one shift obstruction explicitly checked |
| Relative-open sufficient region and existence of irreducible non-bidiagonalizable \(B\) with nonnormal square | M 89 | SUPPORTED | Relative to normal simple-spectrum \(A\); escape from concrete examples, not a converse classification of the full graph hypothesis |
| Branching-tree diagnostic | M 93 | SUPPORTED as an auxiliary identity only | Non-evidence for physical \(\eta\) bounds; independently checked in 4.9 |
| Non-necessity and centering diagnostics | M 95,97; N 9 | SUPPORTED as auxiliary identities only | \(P\) is the imported rank-one orthogonal projector; not a general rank-one matrix |
| \(\eta\le2L\) for every one-normal pair outside the sufficient classes | M 99 | INCONCLUSIVE / expressly open | No upper bound on the remaining common-\(V\) minimax established |
| Author exposure, proposal ordering, absence of undisclosed earlier work, and historical provenance | M 3,5,7,103; N 12,22 | INCONCLUSIVE | No permitted record establishes these historical assertions; they are not theorem premises |
| Global T2/T3/Z2, certificate necessity, global equality classification, novelty, or stronger assurance | M 5,103; N 12 | INCONCLUSIVE / not claimed | No such conclusion follows from this review |

There is no REFUTED mathematical claim in the pinned scope.

## 6. Remaining obligation and prohibited inferences

For normal \(A\) outside (5), and \(B\) outside the common-\(H_i\) linear-forest hypothesis, the packet leaves the common-\(V\) minimax of M LF 24 uncontrolled. Four individually diagonalizable PSD matrices do not supply a simultaneous site-2 basis. Nothing in the proof allows independently optimized \(V_i\) to replace the single \(V\).

Even a lower bound above \(2L\) for the A-diagonal restricted minimum would not refute \(\eta\le2L\): another site-1 unitary \(U\) remains available. Conversely, failure of a Frobenius sufficient test does not imply failure of \(\eta\). The diagnostic at M LF 95 illustrates exactly that distinction.

No unrestricted nonnegative spectral-radius compression principle, arbitrary-\(T\) \(4\times2\) norm estimate, global T2/T3/Z2 lemma, held result, or prior review verdict is imported to fill this gap.

## 7. Complete display-coverage receipt

All entries below were separate **raw** displays. Every window contains at most 15 LF. The order shown is the actual order. No mathematical consideration or mathematical note-taking began until all twelve displays were complete.

| Order | Object | Raw LF window | LF in window |
|---|---|---|---:|
| 1 | W | 1–15 | 15 |
| 2 | W | 16–30 | 15 |
| 3 | W | 31–36, actual ending | 6 |
| 4 | M | 1–15 | 15 |
| 5 | M | 16–30 | 15 |
| 6 | M | 31–45 | 15 |
| 7 | M | 46–60 | 15 |
| 8 | M | 61–75 | 15 |
| 9 | M | 76–90 | 15 |
| 10 | M | 91–103, actual ending | 13 |
| 11 | N | 1–15 | 15 |
| 12 | N | 16–22, actual ending | 7 |

Coverage is **W 36/36 LF, M 103/103 LF, N 22/22 LF**. No body redisplays occurred. There were no status-only context inputs. The later metadata pass read only these same permitted objects and displayed no body content.

## 8. Native clocks, controls, and additive process disclosure

The following are literal `/bin/date -u` observations in UTC, not inferred creation times or backdated labels:

| Observed native clock | Phase / observation |
|---|---|
| 2026-10-30T03:24:10Z | Before manifest metadata verification and manifest display |
| 2026-10-30T03:24:28Z | Before manuscript metadata verification and manuscript display |
| 2026-10-30T03:24:55Z | Before named-import metadata verification and named-import display |
| 2026-10-30T03:25:07Z | After all twelve raw displays; boundary before mathematical reconstruction |
| 2026-10-30T03:31:59Z | Before report-composition phase |
| 2026-10-30T03:33:45Z | Before final metadata-only integrity / terminal-LF pass |
| 2026-10-30T03:33:46Z | After that metadata pass |
| 2026-10-30T03:34:15Z | Before output-attempt phase |
| 2026-10-30T03:38:11Z | After repository-path write refusal; before in-channel delivery |

Initial metadata was obtained with SHA-256 and byte/LF count utilities. The final metadata-only Python command recomputed SHA-256, bytes, LF, and final-LF flags for W, M, N; all matched and all final-LF flags were True. The post-command date was reached through an `&&` chain, establishing metadata-command exit status zero.

All shell calls had a 120-second hard cap and returned successfully. No mathematical executable was run, so there is no positive-control, negative-control, timeout, or failed-control result to misrepresent as acceptance. No reviewer mathematical script or other control artifact was created.

**Additive process disclosure:** Before opening W, I performed compulsory harness process-only reads of `memory://root/memory_summary.md` and `skill://aifours-written-math-acceptance-protocol`. These were not listed mathematical inputs. They supplied general process instructions, not evidence for this manuscript. This extra-manifest process access and its pre-manifest ordering are disclosed explicitly; I do not silently exempt them from the parent’s assessment of the literal manifest-first / listed-files-only rule.

No mathematical content was considered or compared before completing W, M, and N in the prescribed display order. No other extra-manifest file body, sibling review, prior wave output, held/withdrawn/ZERO/quarantined material, author script, network resource, or external model was opened or used.

The final terminal-LF confirmation occurred after mathematical reconstruction, not before it; the initial pre-body hash/bytes/LF verifications had already matched. This timing is disclosed rather than represented as an earlier observation. The confirmation showed no hidden suffix or display gap.

No frozen input, manifest, disposition, ledger, or README was changed. There was no backdating and no alteration or erasure of an unsuccessful control.

The write tool refused the intended repository path because it supports only device transport and session-scratch writes. No review file was created by that attempt; this complete in-channel review is the fallback deliverable authorized by W.

The historical source statements at M LF 3,5,7,103 and N LF 18–22 remain historical assertions, not reviewer-observed events. In particular, the completeness of an author’s disclosure cannot be certified by this review.

## 9. Assurance boundary

This is a **same-harness written-mathematics review** of the two pinned mathematical bodies, after complete bounded-window display.

It is **not** a human review, an independent-model-family review, a formal or kernel/Lean check, a novelty/SOTA audit, an operational certificate, a source-history investigation, or a parent adoption. The review supports only the qualified mathematical statements tabulated above. Provenance and the expressly open global or remaining one-normal claims remain **INCONCLUSIVE**.
