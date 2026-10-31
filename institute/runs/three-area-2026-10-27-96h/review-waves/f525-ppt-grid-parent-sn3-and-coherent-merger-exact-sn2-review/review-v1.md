# f525 — Written review of the coherent-merger SN2 certificate and 4×5 SN3 parent

**Overall correctness: correct, at the exact scopes below.**  
**Findings: 0 FATAL / 0 MAJOR / 0 MINOR.**  
**Confidence: 0.98.**

The explicit algebra supports the candidate’s whole-family result: every PPT member of the specified coherent-merger family has Schmidt number exactly two, while its specified \(4\times5\) parent has Schmidt number exactly three. This does not settle unrestricted \(4\times4\) PPT/SN3 existence.

## 1. Binding, read coverage, and process boundary

Reviewed frozen wave:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f525-ppt-grid-parent-sn3-and-coherent-merger-exact-sn2-review/`

Parent-supplied bindings:

- Manifest SHA256: `5de824595cf19e2591fb6d49cf4b5c4264e735a23996a80e68e98e98acfe396d`
- Receipt SHA256: `bd4b2f98b43cb736b12cc6dd9f98ced7f40fdf17078e7829f48a3fafb0df8ec1`
- Literal-packet SHA256: `0a549f665b657954ad58cf714895119dc6761d4306f5ecac59d65aa8fe308d96`

These are **parent-observed metadata**, not child-executed hash or clock observations.

Before mathematical body reading, I read the complete manifest, freeze receipt, supplied metadata, dispatch receipt, and every named status-only control through its ending. I then sent Main a direct administrative pre-body ACK.

After that ACK, I read **all packet LF1–625**, consecutively in raw windows of at most 20 LF, including:

- **S1:** complete candidate, logical lines 1–589; source SHA256 `85d63cbec7a7115066565abba8b789e4873667fac7a247950f6b26accc4049cd`.
- **S2:** complete earlier physical-state/compression disposition, lines 1–34; source SHA256 `6c2f28329e06b6ffbace6937be43c691301874b2bff2cf26a6334958a04c2ed7`.

All reconstruction below occurred after that complete packet read. The review uses formal variables and manuscript-assigned instances only. No new selected mathematical instance, scientific executable, CAS, enumeration, author code, external source, sibling review, or held mathematical payload was used. Status controls supplied exclusions only; their held episodes and consumers were not mathematical inputs.

**No file was written. This full body is returned for Main materialization.**

## 2. Physical family, filter, and exact PPT region — SUPPORTED

**Anchors:** S1 LF34–167, LF395–407, LF415–426.

Write \([x]=|x\rangle\langle x|\), with the candidate’s vectors \(A,B,D,F_v,E_u\). For \(s,r>0\), every summand in

\[
R=[A]+[B]+[D]+s[F_v]+r[E_u]
+s|v|^2[03]+r|u|^2[23]+r[30]+s[32]
\]

is positive semidefinite. Its trace is exactly

\[
Z=3+2+2+s(1+|v|^2)+r(1+|u|^2)
+s|v|^2+r|u|^2+r+s
=7+2(s+r)+2d,
\]

where \(d=s|v|^2+r|u|^2\).

The stated \(K_{u,v}\) maps the parent’s projectors as required:

\[
02+34\mapsto02+v33,\qquad
20+33\mapsto20+u33,
\]

\[
04\mapsto v03,\quad23\mapsto u23,\quad
30\mapsto30,\quad32\mapsto32.
\]

Thus \(R=(I\otimes K)Q(I\otimes K)^\dagger\), with no omitted output term. Moreover,

\[
KK^\dagger=\operatorname{diag}(1,1,1,|u|^2+|v|^2).
\]

Consequently, a common scalar rescaling makes \(K\) a contraction without changing the normalized successful output. It is a coisometry when \(|u|^2+|v|^2=1\).

### Partial transpose

Direct termwise transposition gives the stated disjoint-block decomposition

\[
\begin{aligned}
R^\Gamma={}&[01+10]+[12+21]+[00]+[22]+M_{s,r}\\
&+r[\bar u\,23+30]+s[\bar v\,03+32]+d[33],
\end{aligned}
\]

where, on \((02,11,20)\),

\[
M_{s,r}=
\begin{pmatrix}
s&1&1\\
1&1&-1\\
1&-1&r
\end{pmatrix}.
\]

The conjugations are correct: for example, the \(\bar u\,|20\rangle\langle33|\) term becomes \(\bar u\,|23\rangle\langle30|\).

All other blocks are PSD and disjoint from this central block. Taking its Schur complement at the middle entry gives

\[
M_{s,r}\ge0
\iff
\begin{pmatrix}s-1&2\\2&r-1\end{pmatrix}\ge0
\iff
s>1,\quad r>1,\quad(s-1)(r-1)\ge4.
\]

The nonzero off-diagonal entry excludes a zero diagonal in the Schur complement. Equality in the determinant condition is included.

The displayed positive decomposition of \(M_{s,r}\) expands correctly:

\[
M_{s,r}
=[02+11-20]
+(s-1)\left[02+\frac2{s-1}20\right]
+\left(r-1-\frac4{s-1}\right)[20].
\]

For \(x=s-1>0\), \(y=r-1>0\), the conditions \(xy\ge4\) and \(x+y\ge2\sqrt{xy}\ge4\) give \(sr\ge9\), as used later.

The parent \(Q^\Gamma\) has the same central block and otherwise PSD disjoint blocks, so its exact PPT region is the same.

### Local ranks

The stated marginals expand correctly:

\[
R_A=\operatorname{diag}
(2+s+s|v|^2,\ 3,\ 2+r+r|u|^2,\ s+r+d),
\]

\[
R_B=\operatorname{diag}(2+2r,\ 3,\ 2+2s,\ 2d).
\]

Alice’s rank is four throughout \(s,r>0\). Bob’s rank is four exactly when \(d>0\), equivalently \((u,v)\ne(0,0)\). Thus **both local ranks are four exactly under that condition**; at the included zero-merger case their ranks are \((4,3)\).

## 3. Finite Schmidt-rank-two building blocks — SUPPORTED

**Anchors:** S1 LF171–260.

For the coefficient matrix of \(V_{z,w}(v,\alpha)\), the column identities are exact:

\[
C_2=z^{-1}C_1,\qquad
C_3=\alpha wC_0+\alpha zwC_1.
\]

In the second identity, the four entries on the right are

\[
2\alpha zw,\quad0,\quad\alpha z^3w,\quad vz^{-1},
\]

which are precisely \(C_3\). Thus each displayed vector has complex Schmidt rank at most two.

For the root average, the seven vector terms carry distinct characters of \(\mathbb Z_4\times\mathbb Z_3\):

\[
(1,0),\ (0,0),\ (2,0),\ (3,0),\
(1,1),\ (3,1),\ (3,2),
\]

respectively. Character orthogonality removes every cross term between these terms. Therefore

\[
G(v,\alpha)
=[A]+[B]+[D]+[F_v]
+4\alpha^2[03]+\alpha^2[23]
+\frac{|v|^2}{\alpha^2}[30]
\]

is exactly the stated twelve-vector positive decomposition.

The reflected construction is also correct. The map
\(L=(T\otimes T)\mathrm{SWAP}\) preserves Schmidt rank and sends

\[
A\mapsto A,\quad B\mapsto D,\quad D\mapsto B,\quad
F_{-u}\mapsto-E_u.
\]

Its action on the added singleton coordinates yields

\[
H(u,\alpha)
=[A]+[B]+[D]+[E_u]
+4\alpha^2[30]+\alpha^2[32]
+\frac{|u|^2}{\alpha^2}[03].
\]

The minus signs disappear at the corresponding projector level.

## 4. Exhaustive upper bound \(\mathrm{SN}(R)\le2\) — SUPPORTED

**Anchors:** S1 LF264–343.

All three cases provide exact positive decompositions; none requires a real-vector restriction.

### Case 1: \(v=0\)

The four-root average is exactly

\[
[A]+[B]+[D]+[02].
\]

Its vectors have rank at most two by the same column dependence, with the added coordinates absent. The remainder is

\[
(s-1)[02]+r[E_u]+r|u|^2[23]+r[30]+s[32],
\]

a positive sum of rank-at-most-two projectors.

### Case 2: \(v\ne0\), \(|v|\le r|u|\)

With \(\alpha^2=|v|^2/r>0\), subtraction gives exactly

\[
\begin{aligned}
R-G(v,\alpha)={}&(s-1)[F_v]+r[E_u]\\
&+|v|^2\left(s-\frac4r\right)[03]
+\left(r|u|^2-\frac{|v|^2}{r}\right)[23]+s[32].
\end{aligned}
\]

The coefficients are nonnegative because \(sr\ge9>4\) and
\(|v|^2\le r^2|u|^2\).

### Case 3: \(v\ne0\), \(|v|>r|u|\)

With \(\alpha^2=1/(sr^2)>0\), subtraction gives exactly

\[
\begin{aligned}
R-H(u,\alpha)={}&s[F_v]+(r-1)[E_u]\\
&+s(|v|^2-r^2|u|^2)[03]+r|u|^2[23]\\
&+\left(r-\frac4{sr^2}\right)[30]
+\left(s-\frac1{sr^2}\right)[32].
\end{aligned}
\]

The last two coefficients are positive since

\[
sr^3=(sr)r^2>9>4,\qquad s^2r^2\ge81>1.
\]

These cases exhaust arbitrary complex \(u,v\), including all stated zero and equality cases.

## 5. Entanglement and exact SN2 — SUPPORTED

**Anchors:** S1 LF347–391.

The \(3\times3\) local compression is exactly

\[
C=[A]+[B]+[D]+s[02]+r[20],
\]

whose range is the stated five-parameter matrix space

\[
X=
\begin{pmatrix}
a&b&c\\
d&a&b\\
e&-d&a
\end{pmatrix}.
\]

For a rank-at-most-one matrix in this range, the minors on rows/columns \(01/01\) and \(12/12\) give

\[
a^2-bd=0,\qquad a^2+bd=0.
\]

Their sum implies \(a=0\) over \(\mathbb C\).

In a positive separable decomposition of \(C\), each product vector must belong to \(\operatorname{range}C\): pairing with any kernel vector gives a sum of nonnegative squared overlaps equal to zero. Every such product vector would therefore have zero \(00\) component, contradicting \(C_{00,00}=1\).

Hence \(C\), and therefore \(R\), is entangled. Combined with the exhaustive upper bound,

\[
\boxed{\mathrm{SN}(R/Z)=2}
\]

throughout the exact PPT region.

## 6. The actual \(4\times5\) parent has SN3 — SUPPORTED

**Anchors:** S1 LF428–490.

The parent’s positive projector span is exactly

\[
Y=
\begin{pmatrix}
a&b&c&0&h\\
d&a&b&0&0\\
e&-d&a&k&0\\
f&0&g&e&c
\end{pmatrix}.
\]

Using the listed zero-based index sets, direct determinant expansion yields:

| Rows; columns | Determinant |
|---|---|
| \(013;013\) | \(e(a^2-bd)=g_1\) |
| \(123;124\) | \(c(a^2+bd)=g_2\) |
| \(013;123\) | \(e(b^2-ac)=g_3\) |
| \(123;014\) | \(-c(d^2+ae)=g_4\) |
| \(012;012\) | \(a^3+b^2e-d^2c-ace=g_5\) |

The polynomial combination is correct because

\[
g_5-g_3-g_4=a^3+ace,\qquad
\frac12(cg_1+eg_2)=a^2ce.
\]

Consequently,

\[
a(g_5-g_3-g_4)-\frac12(cg_1+eg_2)=a^4.
\]

Rank at most two forces all five minors to vanish, hence \(a=0\). Applying the same positive-decomposition/range argument, any decomposition of \(Q\) into rank-at-most-two vectors would force its \(00\) diagonal to vanish, contrary to its value one. Thus \(\mathrm{SN}(Q)>2\).

The defining projector decomposition has Schmidt ranks at most three, giving

\[
\boxed{\mathrm{SN}(Q)=3}.
\]

This proof is self-contained for the displayed parent. It does **not** require the different multiplier expression mentioned from the public source to be correct, and makes no finding that that printed expression or the source’s theorem is false.

## 7. Assigned integer member and filter normalization — SUPPORTED

**Anchors:** S1 LF496–544.

For the explicitly assigned \(s=r=3,\ u=v=1\):

- \(Z=7+12+12=31\).
- The stated partial-transpose decomposition follows from the general one and
  \[
  M_{3,3}=[02+11-20]+2[02+20].
  \]
- With \(\alpha=1/\sqrt3\), the stated remainder is exactly
  \[
  R_*-G(1,1/\sqrt3)
  =2[02+33]+3[20+33]+\frac53[03]+\frac83[23]+3[32].
  \]
- Both normalized marginals equal
  \[
  \frac1{31}\operatorname{diag}(8,3,8,12).
  \]

The parent has trace \(7+4(s+r)=31\) at these assigned weights. Since \(K_{1,1}K_{1,1}^\dagger=\operatorname{diag}(1,1,1,2)\), \(K_{1,1}/\sqrt2\) is a contraction. Its unnormalized output on \(Q_{3,3}/31\) is \(R_*/62\), with trace \(1/2\); conditioning on success gives exactly \(R_*/31\).

Thus the example is a full-local-rank physical \(4\times4\) PPT state with SN exactly two, not an SN3 witness.

## 8. Same-physical detector consequence — SUPPORTED

**Anchors:** S1 LF548–568.

For a Hermitian \(W\) nonnegative on **every complex Schmidt-rank-at-most-two vector**, each positive term in the finite decomposition has nonnegative pairing with \(W\). Therefore

\[
\operatorname{Tr}(WR/Z)\ge0.
\]

This excludes negative certification by any valid complex 2-block-positive detector **on the same physical \(4\times4\) system for this family**. It is not a universal no-go theorem or a claim about arbitrary detectors without that quantifier.

## 9. Earlier context and exact import ceilings

**Anchors:** S2 LF7–32.

The earlier displayed one-extension state independently has the stated trace \(25\), rank-eight disjoint projector decomposition, and rank-nine partial-transpose decomposition. Its supplied two-product-vector expression expands to the stated root-average vectors. The compression argument independently establishes its exact SN2 conclusion.

The general separable-core completion argument is also supported algebraically. For

\[
\rho=\begin{pmatrix}C&Z\\ Z^\dagger&D\end{pmatrix}\ge0,
\]

positivity supplies \(\operatorname{range}Z\subseteq\operatorname{range}C\) and
\(D-Z^\dagger C^+Z\ge0\). If \(C=\sum_j[x_j]\) is separable, lift each \(x_j=a_j\otimes b_j\) to

\[
\widetilde x_j=(x_j,\ Z^\dagger C^+x_j).
\]

Each lift has Schmidt rank at most two because its added component occupies one Bob coordinate. Their positive sum has blocks \(C,Z,Z^\dagger,Z^\dagger C^+Z\); the remaining block is separable. Singular and zero \(C\) are included.

For S2’s particular state, deleting Bob0 projects the given root-average vectors to the displayed product vectors. The remaining singleton projectors are separable; the removed \(30\) ket contributes nothing to this core.

**Import ceiling:** S2’s broader block-diagonal-core corollary additionally invokes the cited \(3\times2\) PPT–separability theorem. Its reduction is valid conditional on that exact theorem; the linked primary source and publication-history assertions were not independently source-adjudicated in this no-source-following duty. Neither that import nor prior review verdicts are needed for the main S1 SN2/SN3 proofs reconstructed above.

## 10. Final scope and exclusions

**Supported written scope:**

- The exact family \(R_{s,r}(u,v)\) in S1.
- Every \(s,r>1\) with \((s-1)(r-1)\ge4\), including equality.
- Arbitrary complex \(u,v\), including either or both zero.
- Both extension coherences active simultaneously.
- Exact SN2, with finite positive decompositions.
- Both local ranks four iff \((u,v)\ne(0,0)\).
- The specified \(4\times5\) parent is PPT and has exact SN3.
- The specified coherent mergers reduce its SN from three to two.
- The same-physical, fully complex 2-block-positive detector consequence.

**Not established by this gate:**

- Unrestricted \(4\times4\) PPT/SN3 existence or impossibility.
- General \(5\to4\) filters mixing core and extension coordinates.
- Exhaustion of \(4\times4\) PPT states by this family or S2’s sufficient core classes.
- Other grid supports, fillers, or coherent couplings.
- Any enlargement to all SDPs or adjudication of the separate public seed’s positivity/2-positivity status.
- Novelty, publication priority, exhaustive literature status, correctness or falsity of the different printed multiplier expression.
- Human, independent-model-family, formal/kernel, or machine-executed verification.

**Disposition:** the candidate is supported as a scoped same-harness written result, with no mathematical correction identified. Adoption remains Main’s decision; no original-target closure or automatic acceptance is asserted.