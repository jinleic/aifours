# f626 — Written review of core mixing, range entanglement, kernel equivalence and the physical member

**Role:** WRITTEN.  
**Scientific execution:** NOT RUN.  
**Mathematical disposition:** SUPPORTED at the candidate’s explicitly restricted scope.  
**Findings:** **0 FATAL / 0 MAJOR / 0 MINOR mathematical findings.**

This is a same-harness written reconstruction, not independent-model-family, human, formal/kernel or novelty verification. It does not supply the other required review gates or parent adoption.

## 1. Inputs, read coverage and process boundary

The review used only the frozen mathematical inputs:

- **S1:** the complete f605 candidate, source labels **1–736**, SHA256 `ae433b0a756112de057db00113a3a6f1378b3c4602ef7853532078f1bf91e5a0`.
- **S2:** the complete prior coherent-merger disposition, source labels **1–57**, SHA256 `7b118ec2d72d89442219fecdceebf36512e2676dcddcf381dd49713c848cf5f2`.

Assignment bindings, attributed to the supplied parent metadata rather than child-computed hashes:

- Manifest: `d8b53418dcfa1db6b51733216c72da590746b39c8fa9883cdeed95e6fce6c8b9`.
- Freeze receipt: `35b314851166f9304757d3966a2667182f2a96e6afd2b78e007526179545d257`.
- Literal packet: `980f6c2de6a829504e7b9892b266a06118bfc76e5201d2c079e2a4bd879d021a`.

Before reading mathematical packet content, I read the complete manifest, freeze receipt, parent live-metadata supply, dispatch receipt and all fifteen assigned status-only controls through their endings, then delivered the direct pre-body ACK to Main. An unsupported numeric endpoint for the live-metadata file in that ACK was immediately withdrawn in a second administrative message, still before mathematical packet reading; coverage was correctly described as raw selectors 1–120 and 121–220 through the visible closing brace.

I subsequently read **the entire literal packet, LF1–795, in consecutive raw windows of at most twenty lines**, including both source endings, before deriving the mathematics below.

No linked source, sibling review, author code or held mathematical payload was followed. All quarantined episodes—including f586, f602 and f596—and every associated consumer remained NONINPUT. No new selected mathematical instance, filter, parameter or probe was introduced. No scientific executable, CAS, interpreter, solver, enumeration, replay, build, test, lint, external-model CLI, Git operation or repository mutation was used. This full body is returned for parent materialization.

## 2. Claim-level disposition

| Claim | Disposition | Source scope |
|---|---|---|
| The displayed \(R_w\) is the actual filtered \(4\times4\) operator, with the stated trace, normalization and success probability | **SUPPORTED** | S1 LF65–191 |
| PPT, including complex conjugation of the Bob filter, and full local supports | **SUPPORTED** | S1 LF195–257 |
| The fifth-root identity gives genuine complex Schmidt-rank-at-most-two vectors | **SUPPORTED** | S1 LF261–308 |
| The ellipsoid certificate gives SN at most two | **SUPPORTED** | S1 LF312–356 |
| Every finite complex \(w\) gives an entangled output | **SUPPORTED** | S1 LF360–416 |
| Both additional complete complex coordinate lines have SN exactly two | **SUPPORTED** | S1 LF420–501 |
| Nonzero-\(w\) filters differ from the old merger under the declared core/extension-preserving gauge | **SUPPORTED** | S1 LF505–532; S2 LF9–15 |
| Every rank-four filter with a covered kernel has the same exact SN conclusion | **SUPPORTED** | S1 LF534–546 |
| The assigned \(s=r=3,\ \alpha=\beta=\gamma=1\) member has the stated physical matrix, marginals, PPT/SN2 certificates and probability | **SUPPORTED** | S1 LF550–664 |
| The displayed \(4\times5\) parent has SN exactly three | **SUPPORTED by the displayed general algebra** | S1 LF668–695; corrected identity also in S2 LF33–37 |
| Universal complex rank-two-block-positive detectors have nonnegative expectation on covered outputs | **SUPPORTED** | S1 LF703–716 |
| Unrestricted \(4\times4\) PPT/SN3 existence or impossibility, arbitrary-filter classification, novelty or source-wide equivalence | **INCONCLUSIVE here and expressly not claimed** | S1 LF720–736; S2 LF57 |

The older coherent-merger continuum theorem and its historical finite-run claims are used only as frozen, exact-scope documentary inputs. I did not independently replay that run or reconstruct its omitted twelve-vector formula from linked material. The new candidate’s positive decompositions and lower bound are displayed sufficiently to reconstruct them directly.

## 3. Actual filter, physical operator and complete matrix specification

The source is

\[
Q_{s,r}=[A]+[B]+[D]
+s([02+34]+[32]+[04])
+r([20+33]+[23]+[30]).
\]

The filter fixes Bob coordinates \(0,1,2,3\) and maps coordinate \(4\) to

\[
w=\alpha|0\rangle+\beta|1\rangle+\gamma|2\rangle.
\]

Consequently the source vectors \(02+34\) and \(04\) become \(02+3w\) and \(0w\), respectively; the other source vectors remain unchanged. This gives exactly

\[
R_w=[A]+[B]+[D]+s[02+3w]+r[20+33]
+s[32]+s[0w]+r[23]+r[30].
\]

Thus equation (6) is equality of the actual physical operators, not an auxiliary Gram-matrix or free-marginal representation.

Writing \(n=\|w\|^2\), the projector traces give

\[
T=\operatorname{Tr}Q_{s,r}=7+4(s+r),
\qquad
Z_w=\operatorname{Tr}R_w=7+2s(1+n)+4r.
\]

Also,

\[
K_wK_w^\dagger=I_4+ww^\dagger,
\qquad \|K_w\|^2=1+n,
\]

so \(K_w/\sqrt{1+n}\) is a physical contraction. On \(Q_{s,r}/T\), its success probability is

\[
p_w=\frac{Z_w}{(1+n)T}>0.
\]

The stated upper bound follows from the exact difference

\[
(1+n)T-Z_w=2s+(7+2s+4r)n\ge0.
\]

I checked the block matrix against the projector expansion. Its diagonal blocks are

\[
\begin{aligned}
D_0&=\operatorname{diag}(1,1,s,0)+sww^\dagger,\\
D_1&=\operatorname{diag}(1,1,1,0),\\
D_2&=\operatorname{diag}(r,1,1,r),\\
D_3&=\operatorname{diag}(r,0,s,r)+sww^\dagger.
\end{aligned}
\]

Its upper off-diagonal blocks are precisely

\[
X=E_{01}+E_{12},\quad
Y=E_{02},\quad
H=E_{12}-E_{01},\quad
P=s e_2w^\dagger,\quad
J=rE_{03},
\]

with the remaining block zero and lower blocks the adjoints. These account for every entry, including the complex conjugates in \(ww^\dagger\) and \(e_2w^\dagger\).

**Disposition: SUPPORTED.**

## 4. PPT and full local supports

On coordinates \((02,11,20)\), the stated decomposition

\[
M_{s,r}
=[02+11-20]
+(s-1)\left[02+\frac{2}{s-1}20\right]
+\left(r-1-\frac4{s-1}\right)[20]
\]

has diagonal entries \(s,1,r\) and off-diagonal entries \(1,1,-1\) in the required positions. Every coefficient is nonnegative on

\[
s>1,\qquad r>1,\qquad(s-1)(r-1)\ge4.
\]

The source partial transpose in equation (12) follows by transposing the Bob indices of the three core projectors and the two extension projectors.

For complex filters, the consuming-side identity is correctly

\[
R_w^\Gamma
=(I\otimes\overline K_w)Q_{s,r}^\Gamma
(I\otimes\overline K_w)^\dagger.
\]

In particular, the source terms \(s[04+32]\) and \(s[34]\) become

\[
s[0\bar w+32],\qquad s[3\bar w],
\]

not expressions with unconjugated \(w\). The explicit equation (13) therefore is a positive decomposition of the actual Bob partial transpose, including the source-region boundary.

For local supports, the positive summands \([A]\), \(r[30]\) and \(r[23]\) suffice. Their Alice marginal dominates \(\operatorname{diag}(1,1,1,r)\), and their Bob marginal does too. This proves both local ranks are four without imposing a condition on \(w\).

**Disposition: SUPPORTED.** The candidate correctly treats the inherited PPT region as sufficient, without asserting its necessity for the filtered family.

## 5. Range obstruction: entanglement for every complex \(w\)

The range parametrization in equation (23) follows directly from the filtered projector vectors:

\[
X=
\begin{pmatrix}
a+\alpha h&b+\beta h&c+\gamma h&0\\
d&a&b&0\\
e&-d&a&k\\
f+\alpha c&\beta c&g+\gamma c&e
\end{pmatrix}.
\]

In particular:

- the \(0w\) coefficient \(h\) modifies the first row;
- the \(02+3w\) coefficient \(c\) produces the bottom-row entry \(\beta c\);
- no independence or uniqueness of this parametrization at degenerate \(w\) is needed.

For a product vector, this coefficient matrix has rank at most one. Using the candidate’s zero-based row/column sets, its minors are

\[
\begin{aligned}
(12;12)&:\quad
\det\begin{pmatrix}a&b\\-d&a\end{pmatrix}=a^2+bd=m_1,\\
(12;02)&:\quad
\det\begin{pmatrix}d&b\\e&a\end{pmatrix}=ad-be=m_2,\\
(13;13)&:\quad
\det\begin{pmatrix}a&0\\\beta c&e\end{pmatrix}=ae=m_3.
\end{aligned}
\]

The bottom-row \(\beta c\) entry does not spoil the third minor because the opposite upper entry is zero. The first-row \(h\) terms enter none of these minors.

The polynomial identity expands exactly:

\[
\begin{aligned}
a^2m_1-abm_2-b^2m_3
&=a^2(a^2+bd)-ab(ad-be)-b^2ae\\
&=a^4.
\end{aligned}
\]

Hence every rank-one range vector has \(a=0\), over \(\mathbb C\). Its physical \(11\) component is therefore zero.

In a positive separable decomposition, each product vector belongs to \(\operatorname{ran}R_w\): its overlap with every kernel vector must vanish because the corresponding positive sum of squared overlaps is zero. Such a decomposition would force the \(11\) diagonal entry to vanish. The actual operator has

\[
\langle11|R_w|11\rangle=1,
\]

from \([A]\), a contradiction.

This proves

\[
\operatorname{SN}(\rho_w)\ge2
\]

for every finite complex \(\alpha,\beta,\gamma\), independently of the ellipsoid.

**Disposition: SUPPORTED.** This excludes separability, not Schmidt number two; the candidate maintains that distinction.

## 6. Rank-two upper bounds and their integration with the lower bound

### Fifth-root certificate and ellipsoid

For the displayed \(V_z\), the coefficient matrix has

\[
C_2=z^{-1}C_1,\qquad C_3=0.
\]

Thus every vector has complex Schmidt rank at most two. The exponents \(1,0,2,-1,-2\) are distinct modulo five, so character averaging gives exactly

\[
G_{\alpha,\beta}
=[A]+[B]+[D]+[U]+|\beta|^2[32].
\]

The sign on the \(D\) term disappears in its projector, while all cross-character terms vanish.

In equation (21), the total \(U\)-projector coefficient is \(s\), the coefficient of \(|U\rangle\langle32|\) is \(s\bar\gamma\), and the total \(32\) diagonal coefficient is

\[
|\beta|^2+\frac{s^2|\gamma|^2}{s-1}+\delta
=s+s|\gamma|^2.
\]

These recover exactly \(s[U+\gamma32]+s[32]\). All remaining source terms are unchanged.

When

\[
\delta=s-|\beta|^2-\frac{s|\gamma|^2}{s-1}\ge0,
\]

every coefficient is nonnegative. The additional nonproduct vectors have Alice support in \(\operatorname{span}\{|0\rangle,|3\rangle\}\), or are \(E=20+33\); each has rank at most two. Combining this positive decomposition with Section 5 proves SN exactly two, including equality and zero coefficients.

### Entire \(\beta\) line

For \(w=\beta|1\rangle\), the stated third-root vectors obey

\[
C_1=\zeta^{-1}C_0-\zeta C_2,
\]

and their average is \([A]+[D]+[01]\). Equation (30) then reproduces the actual output with residual coefficient \(s|\beta|^2-1\).

The ellipsoid certificate covers \(|\beta|^2\le s\), while this certificate covers \(|\beta|^2\ge1/s\). Since \(s>1\), these intervals cover all nonnegative \(|\beta|^2\).

### Entire \(\gamma\) line

For \(w=\gamma|2\rangle\), set \(x=|\gamma|^2\). The square in equation (33) gives the required cross coefficient \(s\bar\gamma\), a \(32\) coefficient \(s(1+x)\), and, after adding \(G_0\) and the residual, a \(02\) coefficient

\[
1+\frac{sx}{1+x}+s-1+\frac{sx^2}{1+x}=s(1+x).
\]

The square’s vector has fixed Bob coordinate \(2\), so it is a product vector. All coefficients are nonnegative and \(1+x>0\).

Both line certificates therefore integrate correctly with the universal entanglement lower bound.

**Disposition: SUPPORTED.** No infinite-parameter endpoint or SN3 conclusion outside these positive decompositions follows.

## 7. Gauge distinction and every filter with a covered kernel

For a rank-four old coherent merger, the distinguished extension space has one-dimensional image disjoint from the image of the core.

For the present filter with \(w\ne0\),

\[
K_w(E_{\rm ext})=\operatorname{span}\{|3\rangle,w\},
\qquad
K_w(C)\cap K_w(E_{\rm ext})=\operatorname{span}\{w\}.
\]

These have dimensions two and one, respectively. Invertible output maps preserve both dimensions. Invertible input changes preserving \(C\) and \(E_{\rm ext}\) separately preserve their images as subspaces. The stated distinction therefore holds under exactly the declared gauge. It does not establish inequivalence under every possible source automorphism, and the candidate expressly avoids that stronger claim.

The kernel is

\[
\ker K_w=\operatorname{span}\{(-\alpha,-\beta,-\gamma,0,1)^T\}.
\]

If another rank-four \(K'\) has this same kernel, both maps induce isomorphisms from the common four-dimensional quotient to the output. Thus \(K'=LK_w\) for an invertible \(L\).

The resulting output is

\[
R'=(I\otimes L)R_w(I\otimes L)^\dagger.
\]

Applying \(L\) to a positive Schmidt-rank-at-most-\(k\) decomposition preserves its rank bound; applying \(L^{-1}\) proves the reverse inequality. Consequently Schmidt number is preserved **in both directions**, not merely bounded above. PPT also survives, by congruence with \(\overline L\) after Bob partial transpose. A nonzero scalar rescaling makes \(K'\) a physical contraction without changing the normalized output or its Schmidt number.

**Disposition: SUPPORTED.** The extension covers precisely the kernels represented by the proved canonical parameters, not arbitrary rank-four filters.

## 8. Assigned simultaneous-core-mixing physical member

Only the literal assigned member was evaluated:

\[
s=r=3,\qquad \alpha=\beta=\gamma=1.
\]

Here \(n=3\), the source PPT condition is saturated, and

\[
\frac13+\frac12=\frac56<1,\qquad \delta=\frac12.
\]

The projector specification in equation (36) is exactly the general physical output specialized to these values. Its trace is \(43\). Substituting into the general blocks gives the displayed diagonal and off-diagonal matrices without changing any entry or conjugation.

For PPT, the central residual coefficient vanishes, leaving

\[
M_{3,3}=[02+11-20]+2[02+20].
\]

Substitution into equation (13) gives precisely the positive decomposition in equation (37).

For the finite SN2 certificate, substituting into equation (21) gives

\[
R_*
=G_*+2\left[U_*+\frac32\,32\right]
+\frac12[32]
+3[20+33]+3[00+01+02]+3[23]+3[30].
\]

The five vectors in \(G_*\) retain the proved column relation. All other vectors have rank at most two, and the universal range obstruction proves entanglement. Thus \(\operatorname{SN}(R_*/43)=2\).

The block traces give the Alice marginal

\[
\rho_{*,A}=\frac1{43}
\begin{pmatrix}
14&0&0&3\\
0&3&0&0\\
0&0&8&0\\
3&0&0&18
\end{pmatrix}.
\]

Summing the four diagonal Bob blocks gives

\[
\rho_{*,B}=\frac1{43}
\begin{pmatrix}
14&6&6&0\\
6&9&6&0\\
6&6&14&0\\
0&0&0&6
\end{pmatrix}.
\]

Their full rank also follows from the general positive marginal lower bounds; no numerical eigensolver is needed.

Finally, the input normalization is correctly **\(Q_{3,3}/31\)**. Since \(1+n=4\), the physical filter is \(K_w/2\), with

\[
p_*=\frac{43}{4\cdot31}=\frac{43}{124},
\]

and the conditional output is exactly \(R_*/43\).

**Disposition: SUPPORTED as written algebra, not an executed finite check.**

## 9. Parent SN3 and actual detector consequence

For the displayed parent range matrix \(Y\), the five stated expressions are indeed \(3\times3\) minors. In particular, their polynomial combination satisfies

\[
g_5-g_3-g_4=a^3+ace,
\qquad
cg_1+eg_2=2a^2ce,
\]

so

\[
a(g_5-g_3-g_4)-\frac12(cg_1+eg_2)=a^4.
\]

Every rank-at-most-two parent range vector therefore has \(a=0\). Positivity and the range argument contradict a rank-two decomposition of \(Q_{s,r}\), whose \(00\) diagonal is one. Its displayed projector decomposition has ranks at most three. Thus the source SN is exactly three.

This supports the actual restricted physical transition

\[
\text{PPT/SN3 parent}\ \longrightarrow\ \text{PPT/SN2 output}.
\]

For a Hermitian detector \(W\) nonnegative on **all complex** Schmidt-rank-at-most-two vectors, evaluating \(W\) on each vector of the positive output decompositions gives

\[
\operatorname{Tr}(W\rho_w)\ge0.
\]

The same reasoning applies after invertible output filtering because those vectors retain their rank bound. No sampling argument or weaker detector property is substituted at this consuming step.

The public paper’s priority, complete proof and printed-multiplier history were not newly audited; that external material was not followed.

## 10. Findings, residual and verdict

No mathematical defect requiring correction was found in the frozen candidate.

The supported result is a **proper core-mixing filter-family exact-SN2 theorem**, with the stated ellipsoid, complete coordinate-line enlargements, same-kernel extension and explicit full-local-rank physical member. It is not an unrestricted \(4\times4\) PPT theorem or an SN3 witness.

The residual is accurately stated: arbitrary \(\eta\) is untreated, and outside the positive-certificate region a negative residual coefficient only invalidates that certificate. It does not establish SN3.

**Overall correctness: correct.**

**Explanation:** The actual filter and physical output, complex PPT congruence, universal entanglement lower bound, positive rank-two decompositions, kernel-equivalence argument and assigned member’s normalization all reconstruct correctly from the frozen packet. The candidate maintains its proper-family boundary and makes no unrestricted PPT44, all-filter, novelty or machine-verification claim.

**Confidence: 0.99.**