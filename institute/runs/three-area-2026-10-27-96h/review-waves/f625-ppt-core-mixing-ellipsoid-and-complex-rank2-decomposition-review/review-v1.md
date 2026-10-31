# f625 — Complete WRITTEN review

**Reviewer:** ReviewF625CoreMixUpper  
**Role:** WRITTEN; child scientific execution **NOT RUN**  
**Findings:** **0 FATAL / 0 MAJOR / 0 MINOR**  
**overall_correctness:** correct  
**confidence:** 0.98

**explanation:** The frozen candidate supplies valid positive complex Schmidt-rank-at-most-two decompositions on the stated ellipsoid and both additional coordinate lines. Its physical-filter normalization, actual operator and partial transpose, full local supports, entanglement lower bound, and covered-kernel extension are consistent. This supports the specified proper-family PPT/SN2 result, not unrestricted \(4\times4\) PPT/SN3 existence or impossibility.

## 1. Input bindings, chronology and process scope

Reviewed wave:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f625-ppt-core-mixing-ellipsoid-and-complex-rank2-decomposition-review/`

Acknowledged bindings:

- Manifest SHA256: `482a0c50816550cafaac641f28303352d5b68d1693f3ace97efb8c4e9d9a803d`
- Freeze-receipt SHA256: `5e527ef96deca453930d9c6ebe1817662cbd6dede9aa4625fe5cf9dc638e8f3a`
- Literal-packet SHA256: `980f6c2de6a829504e7b9892b266a06118bfc76e5201d2c079e2a4bd879d021a`

These are **parent-supplied metadata observations**, not child-recomputed hashes.

Before opening the scientific packet, I read through the endings of:

- manifest LF1–137;
- freeze receipt LF1–47;
- dispatch receipt LF1–20;
- parent live-metadata supply LF1–162;
- all fifteen manifest-listed status-only controls.

I then sent a **direct pre-body ACK to `agent://Main`**. Only afterward did I read the complete packet, consecutively from LF1 through LF795 in raw windows of at most twenty LF. Mathematical reconstruction began after the packet ending.

The complete scientific inputs were:

- **S1:** `f605-actual-ppt44-core-mixing-filter-and-complex-rank3-frontier/review-v1.md`, SHA256 `ae433b0a756112de057db00113a3a6f1378b3c4602ef7853532078f1bf91e5a0`, **all 736 logical lines**. The parent metadata’s LF735 count and the packet’s logical line736 are recorded distinctly.
- **S2:** `dispositions/physics-3-coherent-grid-merger-entire-ppt-family-exact-sn2-parent-v1.md`, SHA256 `7b118ec2d72d89442219fecdceebf36512e2676dcddcf381dd49713c848cf5f2`, **all 57 lines**.

No linked scientific source, author code, sibling review, or held mathematical payload was followed. All quarantined episodes and their consumers, including f586/f602/f596, remained NONINPUT.

No additional selected parameter, filter, state, matrix instance, or probe was introduced. The review below uses general symbolic reconstruction and the candidate’s own explicitly supplied example only. No scientific executable, CAS, solver, enumeration, build, test, lint, external-model CLI, or Git operation was run. No repository file was written; this is the complete body for parent materialization.

## 2. Claim-by-claim disposition

| Claim | Frozen source | Disposition |
|---|---|---|
| Actual filter output, trace, physical normalization and success probability | S1 LF65–191 | **SUPPORTED** |
| Parent and filtered PPT certificates, with complex conjugation | S1 LF195–257 | **SUPPORTED** |
| Full four-dimensional local supports | S1 LF247–254 | **SUPPORTED** |
| Five-root identity and complex rank-two vectors | S1 LF261–308 | **SUPPORTED** |
| Positive ellipsoid decomposition, arbitrary complex \(\alpha\), boundaries included | S1 LF312–356 | **SUPPORTED** |
| Entanglement for every finite complex \(w\) in the assigned source region | S1 LF360–416 | **SUPPORTED** |
| Entire complex \(\beta\)-coordinate line | S1 LF420–458 | **SUPPORTED** |
| Entire complex \(\gamma\)-coordinate line, including its conjugate placement | S1 LF461–501 | **SUPPORTED** |
| Distinction from the old coherent-merger gauge and covered-kernel extension | S1 LF505–546; S2 LF9–15 | **SUPPORTED** |
| Literal simultaneous-core-mixing physical example | S1 LF550–664 | **SUPPORTED** |
| Original parent’s corrected range-minor SN3 proof | S1 LF668–701; S2 LF33–37 | **SUPPORTED** |
| Consequence for universally complex rank-two-block-positive detectors | S1 LF703–716 | **SUPPORTED** |
| Unrestricted \(4\times4\) PPT/SN3 conclusion | S1 LF720–736 | **NOT CLAIMED / NOT ESTABLISHED** |

No candidate defect meeting the reporting criteria was found.

## 3. Physical filter and complete actual operator

For \(w=(\alpha,\beta,\gamma,0)^T\) and \(n=\|w\|^2\),

\[
K_w=[I_4\mid w],\qquad
K_wK_w^\dagger=I_4+ww^\dagger.
\]

Its squared operator norm is \(1+n\), including \(w=0\). Thus

\[
\widehat K_w=\frac{K_w}{\sqrt{1+n}}
\]

is a physical contraction.

Applying \(K_w\) to each source projector gives precisely S1 equation (5):

\[
R_w=[A]+[B]+[D]+s[F_w]+r[E]
+s[32]+s[0w]+r[23]+r[30],
\]

where \(F_w=02+3w\) and \(E=20+33\). In particular, the two source occurrences of old Bob coordinate4 contribute separately to \(F_w\) and \(0w\); neither is discarded.

The projector norms give

\[
T=7+4(s+r),\qquad
Z_w=7+2s(1+n)+4r.
\]

Consequently,

\[
p_w=\frac{Z_w}{(1+n)T}>0,
\]

and the stated bound follows from

\[
(1+n)T-Z_w=2s+(7+2s+4r)n\ge0.
\]

The block matrix in S1 equations (9)–(10) agrees with that projector expansion. Specifically:

- \(A,B\) generate \(X=E_{01}+E_{12}\);
- \(A\) generates \(Y=E_{02}\);
- \(A,D\) generate \(H=E_{12}-E_{01}\);
- \(s[F_w]\) generates \(P=s e_2w^\dagger\);
- \(r[E]\) generates \(J=rE_{03}\).

The four displayed diagonal blocks contain exactly the remaining diagonal contributions. The adjoints supply the required complex-conjugate entries. This is a specification of the actual physical \(16\times16\) operator, not a surrogate or a free-marginal relaxation.

## 4. PPT and local supports

The central parent partial-transpose block has the stated decomposition

\[
M_{s,r}
=[02+11-20]
+(s-1)\left[02+\frac{2}{s-1}20\right]
+\left(r-1-\frac4{s-1}\right)[20].
\]

Its diagonal coefficients are \(s,1,r\), and its off-diagonal coefficients are \(1,1,-1\), as required. All weights are nonnegative on

\[
s>1,\qquad r>1,\qquad(s-1)(r-1)\ge4.
\]

The remaining terms in S1 equation (12) correctly account for the parent partial transpose. Filtering on Bob requires conjugating the filter:

\[
R_w^\Gamma
=(I\otimes\overline K_w)Q_{s,r}^\Gamma
 (I\otimes\overline K_w)^\dagger.
\]

Accordingly, equation (13) correctly contains

\[
s[0\bar w+32]+s[3\bar w],
\]

rather than terms with unconjugated \(w\). Its other blocks remain unchanged. This proves PPT throughout the assigned source region, including equality.

The candidate correctly limits this to a **sufficient inherited region** for the filtered output; it does not assert a filtered-output PPT equivalence outside that region.

For local support, the positive summands \([A]+r[30]+r[23]\) alone imply both displayed lower bounds

\[
\operatorname{Tr}_B R_w\succeq\operatorname{diag}(1,1,1,r)>0,
\qquad
\operatorname{Tr}_A R_w\succeq\operatorname{diag}(1,1,1,r)>0.
\]

Hence both local ranks are four for every covered finite \(w\).

## 5. Five-root complex rank-two identity

The actual coefficient matrix of \(V_z\) in S1 equation (17) agrees with its defining vector. With zero-based column indices,

\[
C_2=z^{-1}C_1,\qquad C_3=0.
\]

This is an exact complex-linear relation for every fifth root \(z\), independently of \(\alpha,\beta\). Each \(V_z\) therefore has Schmidt rank at most two.

The five exponents

\[
1,\ 0,\ 2,\ -1,\ -2
\]

are distinct modulo five. Root orthogonality eliminates every cross term between their corresponding vector components, leaving

\[
\frac15\sum_{z^5=1}[V_z]
=[A]+[B]+[D]+[U]+|\beta|^2[32].
\]

The warning about fourth roots is also correct: exponents \(2\) and \(-2\) would coincide modulo four, so that average would not establish the stated identity for general \(\beta\).

No real-coefficient restriction is used.

## 6. Positive ellipsoid decomposition

Let

\[
\delta=s-|\beta|^2-\frac{s|\gamma|^2}{s-1}.
\]

Because \(s>1\), its nonnegativity is equivalent to the stated ellipsoid condition.

Expanding S1 equation (21):

- the \(U\)-projector coefficient is \(1+(s-1)=s\);
- the coefficient of \(|U\rangle\langle32|\) is \(s\bar\gamma\);
- the coefficient of \([32]\) is

\[
|\beta|^2+\frac{s^2|\gamma|^2}{s-1}+\delta
=s+s|\gamma|^2.
\]

These are exactly the contributions of \(s[F_w]+s[32]\). All other terms agree unchanged.

Every projector in this expansion has Schmidt rank at most two. In particular, \(U+t\,32\) has Alice support contained in \(\operatorname{span}\{|0\rangle,|3\rangle\}\); this remains true for arbitrary complex \(\alpha,\beta,t\). The \(E\) term has rank two, and the listed filler vectors are products.

Thus the positive decomposition proves \(\operatorname{SN}(\rho_w)\le2\) throughout the ellipsoid, with arbitrary complex \(\alpha\). It remains valid at \(\delta=0\) and at zero vector coefficients. It divides by neither \(\alpha,\beta,\gamma\) nor their moduli.

## 7. Entanglement lower bound

The filtered range matrix in S1 equation (23) is obtained by applying the filter to the displayed parent range. Its entries correctly include both changes involving old coordinate4:

- \(h\) contributes \(h(\alpha,\beta,\gamma)\) to Alice row0;
- \(c\) contributes \(c(\alpha,\beta,\gamma)\) to Alice row3.

The three specified minors are indeed

\[
m_1=a^2+bd,\qquad m_2=ad-be,\qquad m_3=ae.
\]

Their identity expands to

\[
a^2m_1-abm_2-b^2m_3=a^4.
\]

For a rank-one coefficient matrix all three minors vanish, so \(a=0\) over \(\mathbb C\). Thus every product vector in the output range has zero \(11\) component.

In a positive separable decomposition, each product vector must belong to the operator’s range: testing a kernel vector gives a sum of nonnegative squared overlaps, each of which must vanish. Such a decomposition would therefore force the output’s \(11\) diagonal entry to vanish, contradicting

\[
\langle11|R_w|11\rangle=1.
\]

This establishes entanglement for every finite complex \(w\) under the assigned positive source parameters. Combined with each available upper-bound decomposition, it establishes **exactly** SN2. As stated by the author, this rank-one obstruction is not an SN3 certificate.

## 8. Complete coordinate-line extensions

### 8.1 The \(\beta\)-line

For the stated \(T_\zeta\), the displayed relation

\[
C_1=\zeta^{-1}C_0-\zeta C_2
\]

holds exactly. The three characters \(0,1,-1\) are distinct modulo three, yielding

\[
\frac13\sum_{\zeta^3=1}[T_\zeta]
=[A]+[D]+[01].
\]

In equation (30), its additional \([01]\) combines with the residual coefficient \(s|\beta|^2-1\) to recover precisely \(s[0w]=s|\beta|^2[01]\). The remaining vectors have rank at most two.

The second certificate is positive when \(|\beta|^2\ge1/s\), while the ellipsoid certificate covers \(|\beta|^2\le s\). These regions cover the entire nonnegative modulus-squared axis because \(s>1\). Complex phases and zero endpoints are handled without dividing by \(\beta\).

This supports the entire line \(w=\beta|1\rangle\), with the other two core coefficients zero, exactly as claimed.

### 8.2 The \(\gamma\)-line

Set \(x=|\gamma|^2\). For equation (33), the projector

\[
s(1+x)\left[32+\frac{\bar\gamma}{1+x}02\right]
\]

has the required cross coefficient \(s\bar\gamma\) on \(|02\rangle\langle32|\). Its vector is a product vector because its Bob coordinate is fixed to2.

Its \([02]\) contribution, together with \(G_0\) and the stated residual, is

\[
1+\frac{s x}{1+x}
+\left(s-1+\frac{s x^2}{1+x}\right)
=s(1+x).
\]

Its \([32]\) coefficient is also \(s(1+x)\). These reproduce \(s[F_w]+s[32]+s[0w]\) on this coordinate line. The residual is positive for every \(x\ge0\), since \(s>1\).

Thus every finite complex \(\gamma\) is covered. The conjugate placement is correct, and no infinite-parameter endpoint is asserted.

## 9. Filter geometry and boundary crossing

The consuming mathematical object is explicitly the actual operator \(R_w=(I\otimes K_w)Q(I\otimes K_w)^\dagger\), and every decomposition and detector conclusion is attached to that same physical output.

For nonzero \(w\), the new filter has

\[
\dim K_w(E_{\rm ext})=2,\qquad
\dim\bigl(K_w(C)\cap K_w(E_{\rm ext})\bigr)=1.
\]

The old rank-four coherent merger specified by S2 has the corresponding dimensions \(1\) and \(0\). Those dimensions are invariant under invertible output transformations and input basis changes separately preserving the distinguished core and extension spaces. The claimed distinction is therefore supported at exactly that restricted gauge scope.

The kernel formula

\[
\ker K_w
=\operatorname{span}\{(-\alpha,-\beta,-\gamma,0,1)^T\}
\]

is correct.

Any rank-four \(K'\) with this same kernel induces an isomorphism from the same quotient as \(K_w\), so \(K'=LK_w\) with \(L\) invertible. Its output is consequently

\[
(I\otimes L)R_w(I\otimes L)^\dagger.
\]

Invertible local filtering preserves Schmidt number in both directions. Physical rescaling does not affect the normalized state. Thus the extension to all rank-four filters with a covered kernel is valid.

This does not classify all input transformations or all rank-four filters; the candidate explicitly preserves that limitation.

## 10. Literal physical example

I checked only the example explicitly supplied by S1:

\[
s=r=3,\qquad \alpha=\beta=\gamma=1.
\]

It has \(n=3\), \(\delta=1/2\), trace \(43\), and source trace \(31\). The supplied diagonal and off-diagonal blocks agree with the general actual-operator formula.

The partial-transpose decomposition in equation (37) is the correct specialization: its central residual coefficient vanishes on this source-region boundary. Equation (38) is the correct positive rank-two specialization of the ellipsoid decomposition.

The displayed marginals agree with the block traces and diagonal-block sum, respectively. Both have full rank by the general positive lower bounds. Finally,

\[
\widehat K_w=K_w/2,\qquad
p_*=\frac{43}{124},\qquad
\rho_*=R_*/43
\]

are consistent with the physical input \(Q_{3,3}/31\).

These are written checks of the supplied example, not a machine-executed finite corroboration.

## 11. Parent SN3 proof, detector implication and imports

For the displayed parent range matrix, the five \(g_i\) are genuine \(3\times3\) minors. With zero-based indices, their row/column sets can be read as:

- \(g_1:\ (0,1,3;\ 0,1,3)\);
- \(g_2:\ (1,2,3;\ 1,2,4)\);
- \(g_3:\ (0,1,3;\ 1,2,3)\);
- \(g_4:\ (1,2,3;\ 0,1,4)\);
- \(g_5:\ (0,1,2;\ 0,1,2)\).

The corrected identity follows directly because

\[
g_5-g_3-g_4=a^3+ace,\qquad
cg_1+eg_2=2a^2ce.
\]

It therefore gives \(a^4\), as stated. Rank-at-most-two range vectors have \(a=0\), contradicting the parent’s nonzero \(00\) diagonal in any positive rank-two decomposition. The original projector decomposition supplies the rank-three upper bound.

For the covered outputs, a Hermitian detector nonnegative on **all complex Schmidt-rank-at-most-two vectors** has nonnegative expectation term by term in the supplied positive decomposition. This also applies after invertible output filtering. No finite sampling argument is substituted for universal detector positivity.

S2 is imported only at its frozen scope: the specified old coherent-merger family, its prior disposition, and its published-parent/source qualification. I did not follow its linked paper, reviews, checker, or receipts, and do not independently recertify their execution history, source-wide accuracy, later corrections, or novelty. The new core-mixing mathematics above is reconstructed from S1’s displayed formulas rather than inferred from S2’s finite checks.

## 12. Final scope and remaining obligations

This review supports:

- the actual physical core-mixing filter family with \(\eta=0\);
- exact PPT/SN2 on the stated ellipsoid, with arbitrary complex \(\alpha\);
- the two complete additional complex coordinate lines;
- the same-kernel rank-four extensions;
- the supplied full-local-support physical example;
- the stated universally rank-two-block-positive detector consequence.

It does **not** establish:

- the general \(\eta\ne0\) canonical filter case;
- SN2 or SN3 outside the proved union;
- a \(4\times4\) PPT/SN3 witness;
- an unrestricted \(4\times4\) PPT/SN3 no-go theorem;
- another reviewer’s verdict, completion of the second WRITTEN gate, or the FINITEAUTHOR gate;
- independent-family, human, formal/kernel, or novelty verification.

For the uncovered region, the candidate correctly identifies the missing scientific step: a positive complex rank-two decomposition of the **actual \(R_w\)** or a universally rank-two-block-positive detector with negative expectation. A negative coefficient in this particular decomposition proves neither SN3 nor impossibility of another decomposition.

**Final disposition: SUPPORTED at the exact frozen candidate scope; 0 FATAL / 0 MAJOR / 0 MINOR. Child scientific execution NOT RUN. Parent adoption and the other required gates remain separate.**