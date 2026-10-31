# 4×4 PPT Schmidt-number target: consolidated written packet

**Owner:** PhysicsPPT44-2  
**Actual clock before writing:** Wed Oct 28 21:55:42 PDT 2026  
**Status:** UNREVIEWED WRITTEN CANDIDATE. Novelty **UNCLEAR**. The unrestricted target remains **OPEN**: no 4×4 PPT state with Schmidt number at least 3 and globally valid negative Schmidt-rank-two witness is constructed, and no proof that all 4×4 PPT states have Schmidt number at most 2 is claimed.

This packet contains (A) an all-parameter decomposability candidate for the phase-covariant witnesses whose correlated block is gaugeable to a Z-matrix, (B) an exact rank-two minimization equivalence for a wider, possibly phase-frustrated, balanced-weight class, and (C) the still-open routes. The only non-elementary import in (A) is the 3×3 theorem stated exactly below. Exact arithmetic checks apply only to the explicit example, not to the universal written arguments.

## Definitions and imported 3×3 theorem

Write \([x]=|x\rangle\langle x|\); use computational tensor basis \(|ij\rangle\), \(0\le i,j\le3\). Bob partial transpose is \(\Gamma\). A Hermitian \(W\) is **2-block positive** when \(\langle X|W|X\rangle\ge0\) for every coefficient matrix \(X\) of rank at most two. A **decomposable** \(W\) has the form \(A+B^\Gamma\) with \(A,B\ge0\). Such an operator is nonnegative on every PPT \(\rho\), since \(\operatorname{Tr}(W\rho)=\operatorname{Tr}(A\rho)+\operatorname{Tr}(B\rho^\Gamma)\ge0\).

**Named import.** Yang, Leung and Tang, *All 2-positive linear maps from \(M_3(\mathbb C)\) to \(M_3(\mathbb C)\) are decomposable*, [arXiv:1603.03534](https://arxiv.org/abs/1603.03534), [Theorem 3.2](https://ar5iv.labs.arxiv.org/html/1603.03534#S3.Thmthm2): every 2-positive or 2-copositive map \(M_3(\mathbb C)\to M_3(\mathbb C)\) is a sum of a completely positive and a completely copositive map. By the standard Choi correspondence, a 2-block-positive 3×3 operator is therefore decomposable. In local dimension at most two every vector has Schmidt rank at most two, so a 2-block-positive operator is PSD. This imported theorem is **not reproved here**.

## A. Z-correlated witnesses: proposed general theorem

### A.1 Statement

Suppose \(W\) is invariant under all diagonal \(U\otimes\overline U\), and after one local diagonal phase gauge has the form

\[
W=\sum_{i\ne j}d_{ij}[ij]+\sum_i a_i[ii]
 -\sum_{i<j}k_{ij}(|ii\rangle\langle jj|+|jj\rangle\langle ii|),\qquad k_{ij}\ge0.
\]

**Claim A.** If \(W\) is 2-block positive, then it is decomposable. No common diagonal coefficient, product-metric form, equal \(d_{ij}\), rank-one negative correlated term, or symmetry among \(k_{ij}\) is assumed. Testing product basis vectors gives \(a_i\ge0\) and \(d_{ij}\ge0\). An arbitrary number of aligned negative projectors with a common phase gauge and entrywise nonnegative correlated sum is included. A local diagonal unitary can be undone on both PSD summands, so the conclusion is invariant under the stated gauge.

### A.2 Rank-two matching lemma and the Z-matrix lemma

Set \(q_{ij}=\sqrt{d_{ij}d_{ji}}\). Testing \(x|ii\rangle+y|jj\rangle\) for arbitrary complex \(x,y\) shows

\[
\begin{pmatrix}a_i&-k_{ij}\\-k_{ij}&a_j\end{pmatrix}\ge0,
\quad\text{so }a_i a_j\ge k_{ij}^2.\tag{1}
\]

For a perfect matching \(M=\{ij,kl\}\), and arbitrary \(z\in\mathbb R_+^4\), use a coefficient matrix with two disjoint rank-one 2×2 blocks and diagonal entries \(z_i\). In a block \(ij\), set offdiagonals \(u\) and \(z_i z_j/u\). Optimizing their costs gives the infimum \(2q_{ij}z_i z_j\). Thus 2-block positivity entails

\[
f_M(z):=\sum_i a_i z_i^2-2\sum_{i<j}k_{ij}z_i z_j
       +2\sum_{ij\in M}q_{ij}z_i z_j\ge0.\tag{2}
\]

When a coefficient or \(z_i z_j\) is zero, this inequality follows by the corresponding finite-\(u\) test and a limit; no nonnormalizable vector is asserted to be a witness.

A real symmetric **Z-matrix** is a matrix with nonpositive offdiagonals. If such an \(H\) is copositive, i.e. \(z^T H z\ge0\) for every \(z\ge0\), then \(H\ge0\): for any real \(x\), \(x^T Hx\ge |x|^T H|x|\ge0\), and complex positivity follows by splitting real and imaginary parts.

For later use, if \(0\le c_{ij}\le q_{ij}\) and \(q_{ij}>0\), define the PSD block on \((|ij\rangle,|ji\rangle)\)

\[
B_{ij}(c)=\frac{c_{ij}}{q_{ij}}
 \begin{pmatrix}d_{ij}&-q_{ij}\\-q_{ij}&d_{ji}\end{pmatrix}.\tag{3}
\]

If \(q_{ij}=0\), necessarily \(c_{ij}=0\); set \(B_{ij}=0\). The residual diagonal terms on \(|ij\rangle,|ji\rangle\) are nonnegative, and \(B_{ij}^\Gamma\) has correlated offdiagonal \(-c_{ij}\).

### A.3 Exhaustive graph split

Let \(G\) have vertices \(0,1,2,3\) and edge \(ij\) exactly when \(q_{ij}<k_{ij}\). Every such graph is either disconnected, contains a perfect matching, or is a spanning star. Indeed, a connected graph without two disjoint edges has pairwise intersecting edges; the only possibilities are a star or a triangle, and a triangle leaves the fourth vertex isolated.

**Disconnected.** Every connected component \(C\) has at most three vertices. For each cross-component pair, \(q_{ij}\ge k_{ij}\); use (3) with \(c_{ij}=k_{ij}\), or zero if both vanish. These blocks cancel the cross-component correlated terms and leave nonnegative diagonal cross-pair residuals. The restriction \(W_C\) to \(\operatorname{span}\{|ij\rangle:i,j\in C\}\) remains 2-block positive. It is PSD for \(|C|\le2\), and decomposable for \(|C|=3\) by the exact 3×3 import above. Lift the component decompositions and add the cross-pair PSD residuals and \(\sum B_{ij}^\Gamma\).

**Perfect matching.** Let \(M\) consist of two low edges. Use (3) with \(c_{ij}=q_{ij}\) on these edges and zero elsewhere. The correlated block of the residual \(A=W-B^\Gamma\) has diagonal \(a_i\), matched offdiagonals \(q_{ij}-k_{ij}<0\), and unmatched offdiagonals \(-k_{ij}\le0\). Its quadratic form on \(z\ge0\) is exactly \(f_M(z)\), hence is PSD by the Z-matrix lemma. All remaining \(|ij\rangle\) diagonal entries are nonnegative. Therefore \(W=A+B^\Gamma\).

### A.4 Spanning-star Schur comparison

Let the star center be 0, leaves \(1,2,3\). Put

\[
t_i=k_{0i}>0,\quad b_i=t_i-q_{0i}\in(0,t_i],\quad
s_{ij}=q_{ij}-k_{ij}\ge0\quad(i,j\in\{1,2,3\}).
\]

By (1), \(a_0>0\) and \(a_i\ge t_i^2/a_0\). Choose \(c_{0i}=q_{0i}\) and, on leaf pairs,

\[
c_{ij}=\min\!\left(q_{ij},\; k_{ij}+\frac{b_i b_j}{a_0}\right).
\]

Use the PSD blocks (3). The residual \(A=W-B^\Gamma\) has nonnegative offdiagonal-basis diagonal entries. Its correlated block has center diagonal \(a_0\), leaf diagonals \(a_i\), center-leaf entries \(-b_i\), and leaf-leaf entries \(\min(s_{ij},b_i b_j/a_0)\). Its Schur complement at \(a_0\) is the Z-matrix \(R\) with

\[
R_{ii}=r_i:=a_i-\frac{b_i^2}{a_0}\ge a_i-\frac{t_i^2}{a_0}\ge0,
\quad R_{ij}=-h_{ij},\quad
h_{ij}:=\max\!\left(0,\frac{b_i b_j}{a_0}-s_{ij}\right).\tag{4}
\]

If every leaf pair satisfies \(s_{ij}>t_i t_j/a_0\), then every \(h_{ij}=0\) and \(R\ge0\). Otherwise choose a leaf pair \(jk\) with \(s_{jk}\le t_j t_k/a_0\), and let \(i\) be the third leaf. In the matching inequality (2) for \(M=\{0i,jk\}\), set

\[
z_0=\frac{b_i z_i+t_j z_j+t_k z_k}{a_0}\ge0.
\]

For all nonnegative \((z_i,z_j,z_k)\), the resulting form \(z^T C z\) is nonnegative, where

\[
\begin{aligned}
&C_{ii}=r_i,\quad C_{jj}=a_j-t_j^2/a_0,\quad C_{kk}=a_k-t_k^2/a_0,\\
&C_{ij}=-k_{ij}-b_i t_j/a_0,\quad C_{ik}=-k_{ik}-b_i t_k/a_0,\quad
 C_{jk}=s_{jk}-t_j t_k/a_0\le0.
\end{aligned}\tag{5}
\]

Every entry of \(R-C\) is nonnegative. For the diagonals use \(b_j\le t_j\). For \(ij\) and \(ik\), (4) gives \(h_{ij}\le b_i b_j/a_0\le b_i t_j/a_0\), and \(k_{ij}\ge0\). For \(jk\), if \(s_{jk}\le b_jb_k/a_0\), then \(R_{jk}=s_{jk}-b_jb_k/a_0\ge C_{jk}\); otherwise \(R_{jk}=0\ge C_{jk}\). Consequently \(z^T Rz\ge z^T Cz\ge0\) for all \(z\ge0\). Since \(R\) is a Z-matrix, it is PSD. Its positive Schur complement proves the correlated block of \(A\) PSD and completes the written proof of Claim A.

### A.5 Exact nontrivial example and check scope

Let \(\omega=\sum_i|ii\rangle\), \(v=|00\rangle+|11\rangle\), and

\[
\begin{aligned}
W_0&=\tfrac12 I+3\sum_i[ii]-[\omega],\\
W_*&=W_0+\tfrac1{10}[11]+\tfrac15[22]+\tfrac3{10}[33]
 +\tfrac{11}{20}([12]+[21])
 +\tfrac32([13]+[31])+\tfrac52([23]+[32])
 +\tfrac1{100}(2I-[v]).
\end{aligned}
\]

\(W_0\) is 2-block positive: it equals \(\frac14(2I-[\omega])+\frac34(4\sum_i[ii]-[\omega])\), and the two summands are nonnegative on rank-two vectors by \(|\operatorname{tr}X|^2\le2\|X\|_F^2\) and \(|\sum_iX_{ii}|^2\le4\sum_i|X_{ii}|^2\). Every added term is PSD, including \(2I-[v]\) since \(\|v\|^2=2\). The negative correlated matrix \([\omega]+[v]/100\) has rank 2, so this is not just the single-projector subcase. Nevertheless

\[
\langle\omega|W_*|\omega\rangle=-34/25,\qquad
\langle02+20|W_*^\Gamma|02+20\rangle=-24/25,
\]

so \(W_*\) is neither PSD nor coPSD. The exact Fraction checker
`frontier-20261028-Z-correlated-star-check.py` (SHA-256 `1b5d0bcc4e01e7d5d0805bbc8b18545d0881f2a9deb3eea63a51913fcaa3b7af`) was run as `PYTHONDONTWRITEBYTECODE=1 /usr/bin/env python3 frontier-20261028-Z-correlated-star-check.py`. It checked PSD ranks 8 and 6 for the example's \(A,B\), PSD of its \(R,C\), entrywise \(R-C\ge0\), the nonzero deficit \(119/5020\), and the two displayed negative tests. It does **not** verify the universal graph or Schur proof.

## B. Exact rank-two minimization for balanced reciprocal weights

### B.1 Statement

For any \(n\), consider a phase-covariant Hermitian operator with arbitrary Hermitian correlated block \(H\) and offdiagonal-basis weights

\[
d_{ij}=q\,r_i/r_j,\qquad q\ge0,\quad r_i>0\quad(i\ne j).
\]

For \(x\in\mathbb R_+^n\), write \(S=\sum_i x_i\), \(L=\max_i x_i\), and

\[
m(x)=\begin{cases}S^2/2,&L\le S/2,\\L^2+(S-L)^2,&L\ge S/2.\end{cases}\tag{6}
\]

**Claim B.** The operator is 2-block positive **if and only if**, for every \(z\in\mathbb C^n\),

\[
z^*Hz+q\left(m(|z|)-\sum_i|z_i|^2\right)\ge0.\tag{7}
\]

This permits arbitrary nonuniform diagonal of \(H\) and arbitrary frustrated complex phases. Equal geometric means \(\sqrt{d_{ij}d_{ji}}=q\) alone do not imply the required common reciprocal weights \(r_i\).

### B.2 Proof of the equivalence

For a rank-at-most-two coefficient matrix \(X\) with diagonal \(z\), let \(T=\operatorname{diag}(\sqrt{r_i})\) and \(Y=TXT^{-1}\). Rank and diagonal are unchanged, and the weighted offdiagonal cost becomes \(q\sum_{i\ne j}|Y_{ij}|^2\). If \(s_1\ge s_2\ge0\) are the singular values of \(Y\), then \(s_1\ge L\), while \(s_1+s_2\ge S\): multiply \(Y\) by a diagonal unitary aligning its diagonal phases and use trace norm duality. Minimizing \(s_1^2+s_2^2\) under these two inequalities gives exactly (6). Hence \(\|Y\|_F^2\ge m(|z|)\).

The bound is attained for **every** \(z\). For \(L\ge S/2\), choose a real \(n\times2\) matrix \(V\) whose row for a maximal component is \((\sqrt L,0)\) and whose other rows are \((0,\sqrt{x_i})\). For \(L\le S/2\), the elementary polygon inequality supplies angles \(\theta_i\) with \(\sum_i x_i e^{2i\theta_i}=0\); choose rows \(\sqrt{x_i}(\cos\theta_i,\sin\theta_i)\). Then \(V^TV=(S/2)I\). In both cases \(G=VV^T\) has diagonal \(x\), rank at most 2, and Frobenius norm squared \(m(x)\). Left-multiplying by the diagonal phase matrix with entries \(e^{i\arg z_i}\) gives a rank-two \(Y\) with diagonal \(z\); \(X=T^{-1}YT\) attains the weighted cost. Thus (7) is both necessary and sufficient. For example, \(x=(1,1,1,1)\) gives \(m=8\), while \(x=(3,1,1,0)\) gives \(m=13\); both are attained by explicit disjoint rank-one blocks.

## C. Exact remaining route and limits

A 4×4 phase-covariant Hermitian witness has arbitrary Hermitian \(H\) on \(|ii\rangle\) and diagonal coefficients on \(|ij\rangle\), \(i\ne j\). The disconnected-graph argument above still works with arbitrary complex \(H_{ij}\), replacing \(k_{ij}\) by \(|H_{ij}|\) and choosing the phase of each PSD pair block to cancel \(H_{ij}\). Therefore its graph \(\sqrt{d_{ij}d_{ji}}<|H_{ij}|\) must be connected if it is to be 2-block positive and indecomposable. Subject to **Claim A**, any gauge-balanced correlated phase pattern is also excluded: along every oriented cycle the product of \(-H_{ij}/|H_{ij}|\) must equal 1 for a gauge to make all offdiagonals nonpositive. A remaining phase-covariant candidate must therefore have a frustrated cycle and connected low graph. Frustration can be real, e.g. a triangle whose edge product is positive; it need not involve genuinely complex entries.

Claim B supplies an exact continuous rank-two inequality only for **balanced reciprocal** offdiagonal weights. It does not certify any candidate in that inequality's remaining region. Also open are witnesses with non-diagonal background, non-phase-covariant couplings, or phase patterns not covered by Claim A. None of these necessary screens is a sufficient positivity or indecomposability criterion. No missing nonunitary/marginal-normalization branch, held historical selected episode, or held consumer is imported into this packet.

## Prior-art triage; novelty unclear

1. Li and Wu, [arXiv:1704.01288v1](https://arxiv.org/html/1704.01288v1), Theorem 2.8, prove 2-positivity implies complete positivity for a particular single-permutation D-type family with no fixed points. That is an existing, stronger conclusion for a narrower special class; it must not be attributed to this packet.
2. Gulati, Nechita and Park, [arXiv:2509.15201v4](https://arxiv.org/html/2509.15201v4), Sections 5–7, give pairwise decomposability criteria and 4×4 positive indecomposable phase-covariant maps. Their Example 5.8 is **not** 2-positive on its stated \(1/2\le\lambda<1\) interval: in their DUC Choi convention \(|00\rangle+|11\rangle\) has expectation \(-2\lambda\), and in their CDUC convention \(|01\rangle+|10\rangle\) has expectation \(-2\). Their positive/indecomposable conclusions are source assertions, not independently reproved here.

These are prior-art triage only; neither source has been exhaustively screened for the full scope of Claims A or B. **Novelty remains unclear.** Independent scientific review, formal verification, and a target PPT/SN3 witness are all absent.
