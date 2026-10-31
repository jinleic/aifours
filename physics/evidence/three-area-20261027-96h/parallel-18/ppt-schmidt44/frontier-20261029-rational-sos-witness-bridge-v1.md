# Exact rational certificates for the 4×4 PPT/SR2-witness target

**Owner:** PhysicsPPT44-2  
**Actual clock before writing:** Thu Oct 29 10:04:33 PDT 2026  
**Status:** WRITTEN, unreviewed. Novelty **UNCLEAR**. The unrestricted existence question—whether some 4×4 PPT state has Schmidt number at least 3—remains **OPEN**. The separate, historical parent status label **N4 UNKNOWN remains unchanged**; it is not used as a name for the mathematical target here.

This packet establishes a complete, finite **rational sum-of-squares certificate format** for a positive answer to the full target, and a fixed-margin certificate search for the explicit 4×5 Krebs–Gachechiladze source. It does **not** exhibit a detecting witness, a sum-of-squares certificate for such a witness, or a 4×4 target state. The theorem makes an exact witness search possible in principle, not necessarily feasible in practice.

## 1. The common algebraic test set

For output dimension \(q\in\{4,5\}\), write \(A\in\mathbb C^{4\times2}\), \(B\in\mathbb C^{q\times2}\), and

\[
X=AB^T,\quad x=\operatorname{vec}(X),\qquad
K_q=\{(A,B): A^*A=I_2,\ \|B\|_F^2=1\}.
\]

The real and imaginary parts of \(A,B\) are \(N=16+4q\) real variables. In particular, \(N=32\) for the target and \(N=36\) for the 4×5 source. Every point in \(K_q\) gives \(\|X\|_F=1\) and \(\operatorname{rank}X\le2\). Conversely, every unit-Frobenius matrix of rank at most two has such a factorization: extend an orthonormal basis for its column space to two columns of \(A\), then take \(B^T=A^*X\). Thus this parameterizes **all** normalized Schmidt-rank-at-most-two vectors, with redundancy but no excluded chart or rank-one boundary.

Let \(g_1,g_2\) be the two real column-norm equations of \(A^*A-I_2\), \(g_3,g_4\) its real and imaginary offdiagonal equations, and \(g_5=\|B\|_F^2-1\). The redundant ball polynomial

\[
b(x)=3-\sum_{i=1}^{N}x_i^2
\]

vanishes on \(K_q\): \(\|A\|_F^2=2\) and \(\|B\|_F^2=1\). For a rational Gaussian Hermitian \(W\) on \(\mathbb C^4\otimes\mathbb C^q\), define the rational real quartic

\[
f_W(A,B)=\langle\operatorname{vec}(AB^T),W\operatorname{vec}(AB^T)\rangle.
\]

## 2. Exact finite SOS certificate

For a positive rational \(\gamma\), the following identity is an immediately checkable sufficient certificate of strict 2-block positivity:

\[
f_W-\gamma=\sum_{j=1}^J p_j(x)^2
+b(x)\sum_{j=1}^L r_j(x)^2+\sum_{h=1}^{5} u_h(x)g_h(x),\tag{1}
\]

where \(p_j,r_j,u_h\in\mathbb Q[x_1,\ldots,x_N]\). On \(K_q\), every equality and \(b\) vanish, hence \(f_W\ge\gamma>0\). Homogeneity then gives nonnegativity on every Schmidt-rank-at-most-two vector, including the zero vector.

**Named import: rational Putinar completeness.** Victoria Powers, *Rational certificates of positivity on compact semialgebraic sets*, [arXiv:0911.1331v1, Theorem 6](https://arxiv.org/pdf/0911.1331v1), proves that a rational polynomial strictly positive on a rational basic semialgebraic set has a rational sum-of-squares quadratic-module representation when an explicit generator \(N-\sum x_i^2\) is included. Apply it to the generators \(g_h,-g_h\) and \(b\). Combining their SOS multipliers gives the unrestricted rational multipliers \(u_h\) in (1). Consequently, whenever \(f_W-\gamma\) is **strictly** positive on \(K_q\), an identity of the form (1) exists with finite, but unspecified, degree and rational coefficient height. This external theorem is not reproved or formally verified here.

## 3. Full-target equivalence, with fixed rational margins

**Claim.** A 4×4 PPT state of Schmidt number at least 3 exists if and only if there exist:

1. rational Gaussian Hermitian \(16\times16\) matrices \(\rho,W\);
2. exact rational PSD certificates for \(\rho-I_{16}\ge0\) and \(\rho^\Gamma-I_{16}\ge0\);
3. \(\operatorname{Tr}(W\rho)\le-1\); and
4. a finite rational identity (1) for \(q=4\) and \(\gamma=1/2\).

Here \(\rho\) is unnormalized. Rational PSD certificates may be exact LDLᵀ/LDL* decompositions with nonnegative rational pivots, including correct treatment of zero blocks.

**Proof: certificate ⇒ target.** Conditions 2 and 3 make \(\rho\) a nonzero PPT operator and pair it negatively with \(W\). Identity (1) makes \(W\) 2-block-positive. Normalizing \(\rho\) preserves PPT and the negative pairing, so it cannot be a mixture of Schmidt-rank-at-most-two vectors.

**Proof: target ⇒ certificate.** Suppose a normalized PPT state \(\rho_0\) has Schmidt number at least 3. The normalized Schmidt-number-at-most-two set is compact and convex, so strict separation gives a Hermitian 2-block-positive \(W_0\) with \(\operatorname{Tr}(W_0\rho_0)<0\). Add a sufficiently small multiple of the identity to \(W_0\) to obtain a strictly 2-block-positive separator, and add a sufficiently small identity term to \(\rho_0\) so that both it and its partial transpose are positive definite without losing negativity. These are open strict inequalities in finite-dimensional matrix entries. Approximate both matrices by rational Gaussian Hermitian matrices while preserving all of them. Multiply \(W\) by a positive rational so its minimum on normalized SR≤2 vectors is at least 1. Multiply \(\rho\) by a positive rational so that \(\rho-I\ge0\), \(\rho^\Gamma-I\ge0\), and \(\operatorname{Tr}(W\rho)\le-1\). Finally \(f_W-1/2\) is strictly positive on \(K_4\), so the named rational Putinar theorem supplies finite rational coefficients for (1). ∎

**Effective meaning.** One can dovetail over rational matrix entries, rational polynomial coefficients and increasing degree/height, checking all equalities and inequalities exactly. The search halts with a finite positive certificate if the target is true; no bound on the first successful degree, coefficient height, time, or memory is asserted. If the target is false, this positive-certificate enumeration need not halt. This is not an executed search and is not a claim that a 4×4 pair has been found.

## 4. Fixed actual-state witness target: 4×5 KG source

Use the explicitly defined unnormalized state

\[
\begin{aligned}
\rho_{\rm KG}&=[00+11+22]+[01+12]+[10-21]\\
&\quad+3([02+34]+[20+33]+[04]+[23]+[30]+[32]),\qquad\operatorname{Tr}\rho_{\rm KG}=31.
\end{aligned}
\]

Its precise 4×5 state comes from Krebs–Gachechiladze, [arXiv:2509.07086v1](https://arxiv.org/pdf/2509.07086), Theorem 5 and Eq. (11). Its PSD/PPT ranks \((9,10)\) and the five-term degree-four range identity forcing \(\psi_{00}=0\) on all SR≤2 range vectors were independently checked by exact rational/integer arithmetic in `frontier-20261029-kg45-source-check.py`, SHA-256 `8a9f5ba28a8c90e7ccc197e13b39754552c8c3ee38f76e2fab5bc31e69be40b2`. These are exact arithmetic checks and written deductions, **not** proof-assistant or formal-kernel verification.

There exists a **rational**, effective-\(T^2\)-invariant Hermitian \(20\times20\) matrix \(W\), in the 34-real-dimensional block space below, satisfying

\[
\operatorname{Tr}(W\rho_{\rm KG})<-1/4,\qquad
f_W>1/124\quad\text{on }K_5.\tag{2}
\]

To see this, strict separation of the known SN≥3 source from the closed SR≤2 cone yields \(W_0\) 2-block-positive with \(\operatorname{Tr}(W_0\rho_{\rm KG})=-1\). Average it over the source's compact local symmetry; 2-block positivity and the trace are unchanged. Then \(W_0+I/62\) has SR2 margin \(1/62\) and pairing \(-1/2\). Rational approximation within operator norm \(1/248\), inside the invariant block space, leaves a margin greater than \(3/248>1/124\) and pairing below \(-3/8<-1/4\). Therefore \(f_W-1/124>0\) on \(K_5\), and the named theorem proves that some finite rational identity (1) exists. **No such \(W\) or SOS identity has yet been produced.**

The exact effective \(T^2\) weights are given by \(f=(0,\delta,2\delta,\xi)\), \(g=(0,-\delta,-2\delta,2\delta-\xi,-2\delta-\xi)\), with a global phase omitted. The nontrivial equal-weight blocks are

\[
\{00,11,22\},\quad\{01,12\},\quad\{02,34\},\quad
\{10,21\},\quad\{20,33\},
\]

and the remaining nine basis vectors are singletons. They give \(9+4\cdot4+9=34\) real Hermitian coordinates. This is a two-parameter relative torus; the earlier checkpoint's three-parameter wording was corrected in `frontier-20261029-torus-dimension-erratum-v1.json`.

Given an actual certificate for (2), Choi duality supplies an exactly 2-positive map \(M_4\to M_5\) that detects this source. It is **not** enough by itself for a 4×4 result. One must additionally find a Schmidt-rank-at-most-four negative vector for the corresponding link operator, or a rank-four Bob filter and a common SR2-positive separator with negative pairing, as in the previously reported filter-lift bridge. No such rank-four negative vector is currently certified.

## 5. Executable exact verifier and honest control

`frontier-20261029-kg45-rational-sos-verify.py` has SHA-256 `84218aa99d49c89c64a106cf3cd34c98d9e4260f1eb26e6e26ab259598443e7c`. It reads a candidate's sparse rational Gaussian upper triangle, rational SOS polynomials and five rational equality multipliers; it checks the \(T^2\) block condition, (1) with \(\gamma=1/124\) as an exact polynomial identity, and the strict rational pairing \(\operatorname{Tr}(W\rho_{\rm KG})<-1/4\). A pass would certify a 4×5 detecting witness, not the 4×4 target.

The exercised **non-detecting** control is \(W=I_{20}\), for which the verifier checks the exact identity

\[
\begin{aligned}
f_I-\tfrac1{124}&=
(\tfrac{30}{31})^2+(\tfrac7{31})^2+(\tfrac2{31})^2+(\tfrac1{62})^2
+g_1\|B_1\|^2+g_2\|B_2\|^2\\
&\quad+2g_3\operatorname{Re}s_B+2g_4\operatorname{Im}s_B+g_5,
\quad s_B=\sum_j B_{j1}\overline{B_{j2}}.
\end{aligned}
\]

The self-check reported 321 monomials on each side, rejected two corrupted identities, and confirmed \(\operatorname{Tr}(I\rho_{\rm KG})=31>0\). Four additional exact parser/control exercises rejected a non-detecting certificate, a corrupted identity, a non-invariant entry and a duplicate matrix entry; a Gaussian-rational offdiagonal evaluation agreed exactly. These exercises do not constitute a candidate witness or a formal-kernel proof.

## 6. Open work and source boundary

The immediate executable target is to produce explicit rational \(W,p_j,r_j,u_h\) satisfying (1) and (2), then seek and exactly certify a rank-at-most-four negative link vector. The existence proof gives neither a useful degree bound nor a computational runtime; an unbounded SOS enumeration was **not** started. The original 4×4 problem remains open. Prior-art novelty has not been established. No independent scientific review, external-model review, or proof-assistant verification was performed. The historical f161/f162 held episodes, old JL audit and selected-parameter consumers were not opened or used.
