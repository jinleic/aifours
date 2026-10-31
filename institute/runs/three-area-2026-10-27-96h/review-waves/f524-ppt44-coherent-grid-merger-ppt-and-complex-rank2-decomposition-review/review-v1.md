# f524 — Written review of the coherent-grid-merger PPT and complex rank-two decomposition

**Verdict: SUPPORTED at the stated coherent-merger-family scope.**  
**Findings: 0 FATAL / 0 MAJOR / 0 MINOR.**

The displayed algebra proves the exact PPT region and an explicit finite Schmidt-rank-at-most-two decomposition for every member of that region, with arbitrary complex merging coefficients. The separate compression argument establishes entanglement, hence Schmidt number exactly two. This is a family-specific obstruction, not a resolution of the unrestricted \(4\times4\) PPT/SN3 existence question.

## 1. Review binding, coverage, and execution boundary

The review is bound to:

- Manifest: `e60cf66302d73bac2e36e1eba42ba7742a66375579949d2668266fb2f5c66dea`.
- Freeze receipt: `a2bdb04b1dd2f527d0c08a758c76d0efc08166641a8587fd79b37532eca8d8d1`.
- Literal packet: `0a549f665b657954ad58cf714895119dc6761d4306f5ecac59d65aa8fe308d96`.

These hashes are **parent-supplied metadata**, not independently executed child hashes.

Before mathematical packet reading, I completely read the manifest, freeze receipt, dispatch receipt, parent metadata supply, and all eleven status/permission controls, then delivered a direct administrative pre-body ACK to Main. Subsequently I read packet lines **1–625**, in consecutive raw windows of at most twenty lines, including both source endings. No elision was observed.

The complete mathematical inputs were:

- **S1:** `review-waves/f490-ppt44-actual-sn3-boundary-or-global-certificate-frontier/review-v1.md`, SHA256 `85d63cbec7a7115066565abba8b789e4873667fac7a247950f6b26accc4049cd`; packet source labels **1–589**, through its deliverable ending. The receipt reports 588 LF separators.
- **S2:** `dispositions/physics-3-ppt44-separable-compression-family-and-exact-sn2-parent-v1.md`, SHA256 `6c2f28329e06b6ffbace6937be43c691301874b2bff2cf26a6334958a04c2ed7`; source labels **1–34**, through its assurance ending.

All held episodes and their consumers were treated as **status-only NONINPUT**. In particular, no held reviewer mathematics, clean-fragment salvage, sibling review, or excluded source link was used. S2’s report of an earlier favorable review was not used as mathematical evidence.

**Scientific execution: NOT RUN.** No scientific code, CAS, solver, interpreter, enumeration, replay, build, test, external-model CLI, or new privately chosen parameter instance was used. Reconstruction below uses formal variables and the manuscript’s expressly assigned example only. No repository file was modified; this full review is returned for parent materialization.

## 2. Per-claim dispositions

| Claim | Frozen location | Disposition |
|---|---|---|
| Explicit physical \(16\times16\) family, trace, and Bob merger | S1:32–95 | **SUPPORTED** |
| Exact PPT region, including equality and complex phases | S1:99–167 | **SUPPORTED** |
| Rank-two vectors, twelve-term root average, and reflected identity | S1:171–260 | **SUPPORTED** |
| Exhaustive positive rank-two decompositions | S1:264–343 | **SUPPORTED** |
| Entanglement and therefore exact SN2 | S1:347–391 | **SUPPORTED** |
| Full local supports when \((u,v)\neq(0,0)\) | S1:393–407 | **SUPPORTED** |
| Displayed \(4\times5\) parent is PPT/SN3 | S1:411–492 | **SUPPORTED from the displayed proof**, without independently certifying the linked publication |
| Assigned integer-coefficient example and physical success probability | S1:496–544 | **SUPPORTED** |
| Nonnegative pairing with every complex 2-block-positive detector | S1:548–568 | **SUPPORTED** |
| S2 intermediate state, exact SN2, and separable-core completion argument | S2:5–28 | **SUPPORTED**, with the external \(3\times2\) PPT-separability import qualified below |
| Publication priority, novelty, and correctness of unprovided public-source expressions | S1:24,486; S2:30–34 | **INCONCLUSIVE / not adjudicated** |
| Unrestricted \(4\times4\) PPT/SN3 existence or unrestricted no-go | S1:580–587; S2:34 | **NOT PROVED**, as the manuscript expressly states |

No claim in the assigned mathematical scope was refuted.

## 3. Physical family and merger reconstruction

Write
\[
d=s|v|^2+r|u|^2.
\]
Every coefficient in
\[
R=[A]+[B]+[D]+s[F_v]+r[E_u]
+s|v|^2[03]+r|u|^2[23]+r[30]+s[32]
\]
is nonnegative for \(s,r>0\). Thus \(R\ge0\), without any assumption about its partial transpose.

The first three projector traces sum to \(3+2+2=7\). The extension projectors contribute
\[
s(1+|v|^2)+r(1+|u|^2),
\]
and the remaining four terms contribute \(d+s+r\). Consequently
\[
\operatorname{Tr}R=7+2(s+r)+2d>0,
\]
as claimed in S1:58–65.

The proposed Bob map sends
\[
|02\rangle+|34\rangle\longmapsto F_v,\qquad
|20\rangle+|33\rangle\longmapsto E_u,
\]
while the four fillers map to the displayed weighted fillers. This verifies the operator identity in S1:87–93 term by term.

Moreover,
\[
KK^\dagger=\operatorname{diag}
(1,1,1,|u|^2+|v|^2).
\]
A positive scalar multiple of \(K\) can therefore be made a contraction. This scales the successful output operator by a positive scalar and leaves its normalized state unchanged. When \(|u|^2+|v|^2=1\), the displayed identity also verifies the claimed coisometry property.

The marginal formulas in S1:393–407 follow directly because each coherence in an individual defining projector joins different Alice coordinates and different Bob coordinates:
\[
\operatorname{Tr}_B R
=\operatorname{diag}
(2+s+s|v|^2,\ 3,\ 2+r+r|u|^2,\ s+r+d),
\]
\[
\operatorname{Tr}_A R
=\operatorname{diag}(2+2r,\ 3,\ 2+2s,\ 2d).
\]
Alice’s marginal has rank four throughout \(s,r>0\). Bob’s has rank four exactly when \(d>0\), equivalently when \((u,v)\neq(0,0)\). The full-local-rank claim therefore does not rely on adding an unused spectator dimension.

## 4. Exact PPT criterion, including conjugation and boundary

Under Bob partial transpose, the extension coherences become
\[
r\bar u\,|23\rangle\langle30|+\text{h.c.},
\qquad
s\bar v\,|03\rangle\langle32|+\text{h.c.}.
\]
These are exactly the cross terms in
\[
r[\bar u\,23+30],\qquad s[\bar v\,03+32].
\]
Thus the complex conjugates in S1:119–120 have the correct orientation.

The remaining core terms give the stated central block
\[
M_{s,r}=
\begin{pmatrix}
s&1&1\\
1&1&-1\\
1&-1&r
\end{pmatrix}
\]
on \((02,11,20)\), together with the positive disjoint blocks in S1:117–121. Therefore \(R^\Gamma\ge0\) if and only if \(M_{s,r}\ge0\).

Taking the Schur complement of its middle diagonal entry gives
\[
\begin{pmatrix}
s-1&2\\
2&r-1
\end{pmatrix}.
\]
Its off-diagonal entry excludes a zero diagonal entry in a positive semidefinite matrix. Its positivity is consequently equivalent to
\[
s>1,\qquad r>1,\qquad (s-1)(r-1)\ge4.
\]
No boundary point with equality is lost.

Expanding S1’s additional certificate
\[
[02+11-20]
+(s-1)\left[02+\frac2{s-1}20\right]
+\left(r-1-\frac4{s-1}\right)[20]
\]
recovers every entry of \(M_{s,r}\); its last coefficient is nonnegative exactly on the stated region.

Finally, with \(x=s-1\) and \(y=r-1\),
\[
xy\ge4,\qquad x+y\ge2\sqrt{xy}\ge4,
\]
so
\[
sr=1+x+y+xy\ge9.
\]
This establishes the bound subsequently used in both nonzero-coherence branches.

## 5. Complex rank-two building blocks and their averaging

For the coefficient matrix in S1:186–195, direct column comparison gives
\[
C_2=z^{-1}C_1,\qquad
C_3=\alpha wC_0+\alpha zwC_1.
\]
In the latter identity, the four entries on the right are
\[
2\alpha zw,\quad 0,\quad \alpha z^3w,\quad vz^{-1},
\]
matching the fourth column exactly. Hence every \(V_{z,w}\) has matrix rank, and thus Schmidt rank, at most two. This argument is valid over \(\mathbb C\); it does not impose a real-vector restriction.

For root averaging, the seven vector components have distinct characters modulo \((4,3)\):
\[
(1,0),\ (0,0),\ (2,0),\ (3,0),\
(1,1),\ (3,1),\ (3,2).
\]
The minus sign multiplying \(D\) does not change its character. Orthogonality of these finite characters eliminates every cross term between the seven components and leaves precisely
\[
G(v,\alpha)
=[A]+[B]+[D]+[F_v]
+4\alpha^2[03]+\alpha^2[23]
+\frac{|v|^2}{\alpha^2}[30].
\]
In particular, the internal coherence within \([F_v]\) is retained rather than incorrectly averaged away.

For the reflected identity, \(L=(T\otimes T)\mathrm{SWAP}\) preserves Schmidt rank, interchanges \(B\) and \(D\), fixes \(A\), and satisfies
\[
L F_{-u}=-E_u.
\]
The global minus sign disappears at projector level. The fillers transform as listed in S1:241–243, giving
\[
H(u,\alpha)
=[A]+[B]+[D]+[E_u]
+4\alpha^2[30]+\alpha^2[32]
+\frac{|u|^2}{\alpha^2}[03].
\]
There is no missing complex conjugation in this reflection step.

## 6. Exhaustive decomposition and coefficient signs

### \(v=0\)

The four-root vectors in S1:273–275 retain the relation \(C_2=z^{-1}C_1\), with the added row and column absent. They therefore have Schmidt rank at most two. Their average removes exactly one copy of \([02]\) along with the three core projectors.

The residual
\[
(s-1)[02]+r[E_u]+r|u|^2[23]+r[30]+s[32]
\]
is positive and consists entirely of projectors onto vectors of Schmidt rank at most two. This branch includes both \(u=0\) and \(u\neq0\), without division by a vanishing parameter.

### \(v\neq0\), \(|v|\le r|u|\)

Here \(\alpha^2=|v|^2/r>0\). Subtracting \(G\) gives the exact residual in S1:301–305. Its potentially restrictive coefficients are
\[
|v|^2\left(s-\frac4r\right)\ge0,
\qquad
r|u|^2-\frac{|v|^2}{r}\ge0.
\]
The first follows from \(sr\ge9\), the second from the branch condition. The \([30]\) coefficient cancels exactly. The equality boundary \(|v|=r|u|\) is included.

### \(v\neq0\), \(|v|>r|u|\)

For \(\alpha^2=1/(sr^2)>0\), subtraction of \(H\) gives S1:325–330 exactly. The \([03]\) coefficient is
\[
s\bigl(|v|^2-r^2|u|^2\bigr)>0.
\]
The other potentially restrictive coefficients obey
\[
r-\frac4{sr^2}=\frac{sr^3-4}{sr^2}>0,
\qquad
s-\frac1{sr^2}=\frac{(sr)^2-1}{sr^2}>0.
\]
Indeed, \(sr^3=(sr)r^2>9\) and \((sr)^2\ge81\). The remaining coefficients are plainly nonnegative. This branch permits \(u=0\).

These three branches exhaust all complex \(u,v\). Each residual extension vector \(F_v\) or \(E_u\) is itself a sum of at most two product vectors, and every filler is a product vector. The resulting decomposition is therefore an explicit positive finite Schmidt-rank-at-most-two decomposition throughout the entire PPT region.

## 7. Entanglement and exact SN2

The local compression to core coordinates has range
\[
X=
\begin{pmatrix}
a&b&c\\
d&a&b\\
e&-d&a
\end{pmatrix}.
\]
For a rank-one matrix in this range, the minors on rows/columns \((01;01)\) and \((12;12)\) give
\[
a^2-bd=0,\qquad a^2+bd=0.
\]
Over \(\mathbb C\), these force \(a=0\).

Every vector in a positive separable decomposition must lie in the operator’s range: its overlap with each kernel vector vanishes because the corresponding positive sum of squared overlaps is zero. Thus a separable decomposition of this compression would have zero \(00\) diagonal, contradicting its actual value one.

The compression is entangled, and a local compression cannot create entanglement from a separable state. Therefore \(R\) is entangled. Combined with the proved upper bound, this yields
\[
\mathrm{SN}(R/Z)=2.
\]
This includes the zero-merger case; the claim is not restricted to full-local-rank outputs.

## 8. Displayed \(4\times5\) parent: independent reconstruction

The partial-transpose formula for \(Q\) follows by the same core calculation and the extension blocks
\[
r[23+30]+r[33],\qquad
s[04+32]+s[34].
\]
Thus its PPT region is the same exact region established above.

The positive defining weights give precisely the displayed range matrix \(Y\). Expanding the five minors at the listed row/column sets yields
\[
g_1=e(a^2-bd),\qquad g_2=c(a^2+bd),
\]
\[
g_3=e(b^2-ac),\qquad
g_4=-c(d^2+ae),
\]
\[
g_5=a^3+b^2e-d^2c-ace.
\]
Their formal combinations satisfy
\[
g_5-g_3-g_4=a^3+ace,\qquad
\frac12(cg_1+eg_2)=a^2ce,
\]
and hence
\[
a(g_5-g_3-g_4)-\frac12(cg_1+eg_2)=a^4.
\]

Rank at most two makes every displayed \(3\times3\) minor zero, forcing \(a=0\). The positive-decomposition range argument then excludes any Schmidt-rank-at-most-two decomposition of \(Q\), since its \(00\) diagonal equals one. Its defining projector decomposition has ranks at most three. Therefore
\[
\mathrm{SN}(Q)=3.
\]

This support comes from the **displayed range, minors, and polynomial identity**, not from treating the linked theorem or a prior review as an unchecked premise. The comparison with a different multiplier expression in the public paper remains unadjudicated; it is unnecessary to the proof just reconstructed.

## 9. Assigned example and detector consumer

For the manuscript’s assigned \(s=r=3,\ u=v=1\) example:

- The trace formula gives \(31\).
- Substitution in the central-block certificate gives the stated partial-transpose decomposition.
- Substitution into the first nonzero-coherence branch gives exactly the residual coefficients \(2,3,5/3,8/3,3\) in S1:525–527.
- The marginal formulas give \(\operatorname{diag}(8,3,8,12)/31\) on both sides.
- The parent trace is \(7+4(s+r)=31\). Filtering by \(K_{1,1}/\sqrt2\) produces \(R_*/2\) from \(Q_{3,3}\), so on the normalized parent the success probability is \(1/2\), with normalized output \(R_*/31\).

For the consuming detector statement, each term of the proved positive decomposition has Schmidt rank at most two. Consequently every Hermitian \(W\) nonnegative on **all complex** Schmidt-rank-at-most-two vectors satisfies
\[
\operatorname{Tr}(WR/Z)\ge0.
\]
The conclusion in S1:568 follows with the correct quantifier and on the same physical system. No restriction to real detectors, sampled vectors, or a finite detector family has been substituted.

## 10. S2 reconstruction and exact sufficient-class ceiling

The intermediate state in S2 has eight independent, disjoint-support defining vectors, rank eight, and trace twenty-five. Its partial-transpose decomposition has total block rank nine, as stated. Expanding its displayed two-product-vector expression recovers \(v_z\), and four-root averaging gives its explicit rank-two decomposition. The same core-range minors prove that its Schmidt number is exactly two.

For the general completion claim, let
\[
\rho=\begin{pmatrix}C&Z\\ Z^\dagger&D\end{pmatrix}\ge0,
\qquad
C=\sum_j[x_j],\quad x_j=a_j\otimes b_j.
\]
Block positivity gives
\[
\operatorname{range}Z\subseteq\operatorname{range}C,\qquad
D-Z^\dagger C^+Z\ge0.
\]
Set \(S=Z^\dagger C^+\). The lifted vectors \((x_j,Sx_j)\) sum to the operator with blocks
\[
\begin{pmatrix}
C&Z\\ Z^\dagger&Z^\dagger C^+Z
\end{pmatrix}.
\]
Each lift is the sum of its original product vector and a vector on one added Bob coordinate, so it has Schmidt rank at most two. The remaining Schur block is positive on that single Bob coordinate and is separable. This verifies the completion statement, including singular and zero \(C\).

Deleting Bob coordinate zero from S2’s \(v_z\) removes its second product summand. It leaves
\[
(|0\rangle+z|1\rangle+z^2|2\rangle)
\otimes(|1\rangle+z^{-1}|2\rangle).
\]
Thus the displayed \(C_0\) has the separable decomposition
\[
C_0=\frac14\sum_{z^4=1}
\left[
(|0\rangle+z|1\rangle+z^2|2\rangle)
\otimes(|1\rangle+z^{-1}|2\rangle)
\right]
+2[02]+3[33]+3[23]+3[32].
\]
There is no surviving \([30]\) term. Every positive completion with core \(tC_0\), \(t\ge0\), consequently has SN at most two.

S2’s broader three-block sufficient condition uses one external mathematical import: **every \(3\times2\) PPT state is separable**. Conditional on precisely that import, its argument is sound: the indicated core block is \(3\times2\) PPT, and each of the other two blocks has one local dimension. I did not follow the public-source link or independently verify its theorem text. No stronger separability theorem is imported.

The completion result therefore covers **separable codimension-one cores**, including the stated \(C_0\) family and the specified block-diagonal PPT sufficient class. It does not establish that arbitrary \(4\times4\) PPT states possess such a core.

## 11. Scope and assurance limits

The supported coherent-merger theorem covers exactly:

- The displayed \(R_{s,r}(u,v)\), for \(s,r>0\).
- PPT if and only if \(s,r>1\) and \((s-1)(r-1)\ge4\).
- Every complex \(u,v\), including vanishing coefficients and all stated boundaries.
- Simultaneously active extension coherences.
- Full four-dimensional local supports when \((u,v)\neq(0,0)\).
- Exact SN2 and nonnegative pairing with every fully complex 2-block-positive detector.

It does **not** cover arbitrary \(5\to4\) filters mixing core and extension coordinates, arbitrary grid supports or filler patterns, or arbitrary \(4\times4\) PPT states. It supplies neither an SN3 state–detector pair on \(4\times4\) nor an unrestricted no-go theorem. Publication attribution, novelty, exhaustive literature status, and unrelated CP-collapse claims are not certified.

This is an independent **same-harness written reconstruction** of the frozen inputs, not human, independent-model-family, formal/kernel, or executable verification. It does not itself constitute parent adoption or original-target closure.

**Overall correctness:** correct within the frozen mathematical scope.  
**Explanation:** The partial-transpose blocks, complex rank-two identities, exhaustive residual signs, and entanglement lower bound reconstruct without a defect. The resulting obstruction remains limited to the specified coherent-merger family and the separately identified separable-core completion classes.  
**Confidence:** 0.98.