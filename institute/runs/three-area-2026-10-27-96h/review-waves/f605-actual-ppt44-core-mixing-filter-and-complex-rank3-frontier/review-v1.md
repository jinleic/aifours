# author-candidate-v1.md

## A genuinely core-mixing \(5\to4\) filter family with exact Schmidt-number collapse

**Status: GENERALAUTHOR candidate. Complete written certificates below; scientific execution NOT RUN; no independent review or parent acceptance claimed.**

### Result and original-target boundary

For the specified \(4\times5\) PPT/SN3 grid state \(Q_{s,r}\), consider Bob filters that retain coordinates \(0,1,2,3\) and map the remaining extension coordinate into the **original three-dimensional core**:
\[
K_w|j\rangle=|j\rangle\quad(0\le j\le3),\qquad
K_w|4\rangle=w=\alpha|0\rangle+\beta|1\rangle+\gamma|2\rangle.
\]

The resulting actual \(4\times4\) physical output has **Schmidt number exactly two** whenever
\[
\boxed{\frac{|\beta|^2}{s}+\frac{|\gamma|^2}{s-1}\le1,}
\]
with **arbitrary complex \(\alpha\)** and the entire original PPT parameter region
\[
s>1,\qquad r>1,\qquad(s-1)(r-1)\ge4.
\]

The conclusion also holds on the two entire complex coordinate lines
\[
w=\beta|1\rangle\quad\text{and}\quad w=\gamma|2\rangle,
\]
including points outside that ellipsoid. The line \(w=\alpha|0\rangle\) is already included without any restriction on \(\alpha\).

These are genuinely core-mixing filters, not the earlier family that sends both extension coordinates into a single fourth output coordinate. The result extends to **every rank-four Bob filter having the same kernel as a covered \(K_w\)**, not just the displayed canonical matrices.

An explicit member below mixes the discarded extension into **all three core coordinates simultaneously**, has full four-dimensional local supports, and comes with its complete \(16\times16\) operator specification, physical success probability, PPT certificate and finite complex rank-two decomposition.

**The unrestricted \(4\times4\) PPT/SN3 existence question remains NOT PROVED.** This candidate supplies a new proper filter-family obstruction, not an SN3 witness or an unrestricted no-go theorem.

---

## 1. Read chronology, provenance and execution boundary

Before reading the scientific packet or deriving mathematics, I:

1. Read the complete manifest, all thirteen controls in their manifest order, and the complete freeze receipt, through their endings, using raw windows of at most twenty LF.
2. Sent a direct pre-body acknowledgement to `agent://Main`.
3. Subsequently read the entire ordered literal packet, LF \(1\)–\(681\), in consecutive raw windows of at most twenty LF, including its final line. This included all \(57\) lines of S1, all \(589\) logical lines of S2, and all \(33\) lines of S3.
4. Only after that complete packet read developed the written constructions below.
5. Later read the complete parent live-metadata supply and dispatch receipt. They supplied administrative metadata, not additional scientific premises.

Assignment bindings, **parent-supplied rather than child-computed**, are:

- Manifest SHA256: `2b95ba1a243cc2bfdf43f8dc92d9e2a0390fc6a8bcc510d745baee41669fbcb1`
- Freeze-receipt SHA256: `833be4e46fdf4d65c03917759c1116bc4dcb3bf6eee34c8a4a9bc890a5e3defb`
- Packet SHA256: `711d84f187a6c40ec8d5f3d0fd6ff6cb8039490b4d8d496a0b64d5d3c8ed3667`
- Parent-observed pre-creation clock: `2026-10-30T14:11:42-0700 PDT`

Fresh selected written constructions were used in this GENERALAUTHOR duty, including coordinate-aligned filters and the simultaneous-core-mixing member \(\alpha=\beta=\gamma=1\). This is disclosed author research, not blind review or independent corroboration.

**Scientific execution: NOT RUN.** No scientific executable, solver, build, test, external-model CLI, package installation or filesystem modification was used. No program output, runtime, machine-checked identity or locally recomputed hash is claimed. The evidence consists of the explicit written identities below.

All held episodes and their consumers remain NONINPUT. No held mathematical payload or cleaner fragment was used.

The \(4\times5\) parent construction is prior published mathematics, identified in the frozen inputs with [Krebs–Gachechiladze, *Scaling Bound Entanglement through Local Extensions*, Theorem 5 and Eq. (11)](https://arxiv.org/html/2509.07086v1). I did not conduct a new external literature or priority audit. The source’s previously qualified printed multiplier is not used.

---

## 2. Original parent and a physical core-mixing filter

Write \([x]=|x\rangle\langle x|\), and set
\[
\begin{aligned}
A&=|00\rangle+|11\rangle+|22\rangle,\\
B&=|01\rangle+|12\rangle,\\
D&=|10\rangle-|21\rangle.
\end{aligned}
\]

The original \(4\times5\) operator is
\[
\boxed{
Q_{s,r}
=[A]+[B]+[D]
+s\bigl([02+34]+[32]+[04]\bigr)
+r\bigl([20+33]+[23]+[30]\bigr).
}
\tag{1}
\]
Its trace is
\[
T=7+4(s+r).
\tag{2}
\]

For arbitrary \(\alpha,\beta,\gamma\in\mathbb C\), put
\[
w=\alpha|0\rangle+\beta|1\rangle+\gamma|2\rangle,\qquad
n=\|w\|^2.
\]
Define \(K_w:\mathbb C^5\to\mathbb C^4\) as in the introduction. In matrix form,
\[
K_w=
\begin{pmatrix}
1&0&0&0&\alpha\\
0&1&0&0&\beta\\
0&0&1&0&\gamma\\
0&0&0&1&0
\end{pmatrix}.
\tag{3}
\]

Since
\[
K_wK_w^\dagger=I_4+|w\rangle\langle w|,
\]
its squared operator norm is \(1+n\). Therefore
\[
\widehat K_w=\frac{K_w}{\sqrt{1+n}}
\tag{4}
\]
is an actual physical contraction.

Define
\[
F_w=|02\rangle+|3\rangle\otimes w,\qquad
E=|20\rangle+|33\rangle.
\]
The unscaled output is exactly
\[
\boxed{
R_w
=[A]+[B]+[D]
+s[F_w]+r[E]
+s[32]+s[0w]+r[23]+r[30],
}
\tag{5}
\]
where \(|0w\rangle=|0\rangle\otimes w\). In particular,
\[
R_w=(I\otimes K_w)Q_{s,r}(I\otimes K_w)^\dagger.
\tag{6}
\]

Its trace and normalized physical state are
\[
Z_w=7+2s(1+n)+4r,\qquad
\rho_w=\frac{R_w}{Z_w}.
\tag{7}
\]
On input \(Q_{s,r}/T\), the physical filter (4) succeeds with probability
\[
\boxed{p_w=\frac{Z_w}{(1+n)T}>0.}
\tag{8}
\]
The probability is at most one: directly,
\[
(1+n)T-Z_w=2s+(7+2s+4r)n\ge0.
\]

### Complete \(16\times16\) operator specification

Let \(e_j=|j\rangle\in\mathbb C^4\), and let \(E_{ij}=|i\rangle\langle j|\) denote Bob matrix units. In the ordered physical basis
\[
(00,01,02,03;\ 10,11,12,13;\ 20,21,22,23;\ 30,31,32,33),
\]
the entire operator is the following \(4\times4\) block matrix, with each block \(4\times4\):
\[
\boxed{
R_w=
\begin{pmatrix}
D_0&X&Y&P\\
X^\dagger&D_1&H&0\\
Y^\dagger&H^\dagger&D_2&J\\
P^\dagger&0&J^\dagger&D_3
\end{pmatrix},
}
\tag{9}
\]
where
\[
\begin{aligned}
D_0&=\operatorname{diag}(1,1,s,0)+sww^\dagger,\\
D_1&=\operatorname{diag}(1,1,1,0),\\
D_2&=\operatorname{diag}(r,1,1,r),\\
D_3&=\operatorname{diag}(r,0,s,r)+sww^\dagger,\\
X&=E_{01}+E_{12},&
Y&=E_{02},\\
H&=E_{12}-E_{01},&
P&=s\,e_2w^\dagger,&
J&=rE_{03}.
\end{aligned}
\tag{10}
\]
All unlisted block entries are zero. Thus (9)–(10) specify every physical matrix entry, including its complex conjugation.

---

## 3. PPT and full local supports

Let \(\Gamma\) denote Bob partial transpose. On \((02,11,20)\), define
\[
M_{s,r}=
\begin{pmatrix}
s&1&1\\
1&1&-1\\
1&-1&r
\end{pmatrix}.
\]
Throughout the stated source region, its explicit PSD decomposition is
\[
\begin{aligned}
M_{s,r}
={}&[02+11-20]\\
&+(s-1)\left[02+\frac{2}{s-1}20\right]\\
&+\left(r-1-\frac4{s-1}\right)[20].
\end{aligned}
\tag{11}
\]

The original parent has
\[
\begin{aligned}
Q_{s,r}^{\Gamma}
={}&[01+10]+[12+21]+[00]+[22]+M_{s,r}\\
&+r[23+30]+s[04+32]+r[33]+s[34].
\end{aligned}
\tag{12}
\]
This proves its PPT property, including the boundary.

For the actual filtered operator,
\[
R_w^\Gamma
=(I\otimes\overline K_w)Q_{s,r}^\Gamma
 (I\otimes\overline K_w)^\dagger.
\]
More explicitly,
\[
\boxed{
\begin{aligned}
R_w^\Gamma
={}&[01+10]+[12+21]+[00]+[22]+M_{s,r}\\
&+r[23+30]+s[0\bar w+32]+r[33]+s[3\bar w].
\end{aligned}
}
\tag{13}
\]
Every term is PSD. No numerical partial-transpose test or real-coefficient restriction is involved.

The output always has full local supports. Indeed, \(R_w\) contains the positive summands \([A]\), \(r[30]\) and \(r[23]\). Hence
\[
\operatorname{Tr}_B R_w\succeq\operatorname{diag}(1,1,1,r)>0,
\]
and
\[
\operatorname{Tr}_A R_w\succeq\operatorname{diag}(1,1,1,r)>0.
\tag{14}
\]

Here and below the asserted PPT region is a sufficient region inherited from the original parent. No necessity assertion about the filtered operator outside that region is made.

---

## 4. A new five-character complex rank-two identity

Separate the final core component:
\[
U=|02\rangle+\alpha|30\rangle+\beta|31\rangle,
\qquad
F_w=U+\gamma|32\rangle.
\tag{15}
\]

For each fifth root of unity \(z\), define
\[
\boxed{
V_z=zA+B-z^2D+z^{-1}U+\beta z^{-2}|32\rangle.
}
\tag{16}
\]
Its actual coefficient matrix is
\[
\begin{pmatrix}
z&1&z^{-1}&0\\
-z^2&z&1&0\\
0&z^2&z&0\\
\alpha z^{-1}&\beta z^{-1}&\beta z^{-2}&0
\end{pmatrix}.
\tag{17}
\]
The columns obey
\[
C_2=z^{-1}C_1,\qquad C_3=0.
\tag{18}
\]
Thus every \(V_z\) has complex Schmidt rank at most two, for all complex \(\alpha,\beta\).

The five character exponents
\[
1,\quad0,\quad2,\quad-1,\quad-2
\]
are pairwise distinct modulo five. Consequently
\[
\boxed{
G_{\alpha,\beta}:=\frac15\sum_{z^5=1}[V_z]
=[A]+[B]+[D]+[U]+|\beta|^2[32].
}
\tag{19}
\]

**The use of fifth roots matters.** Fourth roots would identify exponents \(2\) and \(-2\), retaining unwanted \(D\)–\(32\) cross terms. Equation (19) is not obtained by reusing the earlier four-root average without modification.

---

## 5. Exact SN2 theorem on a genuinely core-mixing region

Assume
\[
\delta:=s-|\beta|^2-\frac{s|\gamma|^2}{s-1}\ge0.
\tag{20}
\]
Equivalently,
\[
\frac{|\beta|^2}{s}+\frac{|\gamma|^2}{s-1}\le1.
\]

Then the following is an exact identity on the actual physical \(4\times4\) system:
\[
\boxed{
\begin{aligned}
R_w={}&G_{\alpha,\beta}\\
&+(s-1)\left[U+\frac{s\gamma}{s-1}|32\rangle\right]
+\delta[32]\\
&+r[E]+s[0w]+r[23]+r[30].
\end{aligned}
}
\tag{21}
\]

To verify it, the \(U\) coefficient is \(1+(s-1)=s\), its cross term with \(32\) has the required coefficient \(s\bar\gamma\), and the total \(32\) coefficient is
\[
|\beta|^2+\frac{s^2|\gamma|^2}{s-1}+\delta
=s+s|\gamma|^2.
\]
These are precisely the coefficients of \(s[F_w]+s[32]\); the other summands are unchanged.

Every term in (21) is a positive projector of Schmidt rank at most two:

- Equation (19) supplies five explicit complex rank-two vectors.
- \(U+t|32\rangle\) has Alice support contained in \(\operatorname{span}\{|0\rangle,|3\rangle\}\).
- \(E\) has Schmidt rank two.
- \(|0w\rangle,|23\rangle,|30\rangle,|32\rangle\) are product vectors.

Therefore
\[
\boxed{\operatorname{SN}(\rho_w)\le2}
\tag{22}
\]
on the entire stated region, including \(\delta=0\) and all zero coefficients. There is no division by \(\alpha,\beta\) or \(\gamma\).

---

## 6. Entanglement persists for every complex \(w\)

This lower bound does **not** require the ellipsoid condition.

Because the source projector weights are positive, every vector in the filtered range has a coefficient matrix of the form
\[
X=
\begin{pmatrix}
a+\alpha h&b+\beta h&c+\gamma h&0\\
d&a&b&0\\
e&-d&a&k\\
f+\alpha c&\beta c&g+\gamma c&e
\end{pmatrix}.
\tag{23}
\]

For a rank-one such matrix, the following \(2\times2\) minors vanish:
\[
m_1=a^2+bd,\qquad
m_2=ad-be,\qquad
m_3=ae.
\tag{24}
\]
Their row/column index sets are, respectively,
\[
(12;12),\qquad(12;02),\qquad(13;13).
\]
The exact identity
\[
\boxed{a^2m_1-abm_2-b^2m_3=a^4}
\tag{25}
\]
therefore forces \(a=0\) over \(\mathbb C\).

Every product vector in the range of \(R_w\) consequently has zero \(11\) component. But
\[
\langle11|R_w|11\rangle=1.
\tag{26}
\]
In a positive separable decomposition every product vector must lie in the operator’s range: a kernel vector has a sum of nonnegative squared overlaps equal to zero. Equations (25)–(26) therefore rule out separability.

Thus, for **every** \(\alpha,\beta,\gamma\),
\[
\operatorname{SN}(\rho_w)\ge2.
\tag{27}
\]
Combining this with (21),
\[
\boxed{
\operatorname{SN}(\rho_w)=2
\quad\text{if}\quad
\frac{|\beta|^2}{s}+\frac{|\gamma|^2}{s-1}\le1.
}
\tag{28}
\]

This is a complex product-vector range obstruction proving entanglement. It is **not** an SN3 obstruction: (25) concerns rank-one vectors, whereas SN3 would require excluding rank-two decompositions.

---

## 7. Two complete complex coordinate lines beyond the ellipsoid

### 7.1 Arbitrary mixing into core coordinate \(1\)

Let \(w=\beta|1\rangle\), with no restriction on \(|\beta|\). Equation (28) already covers \(|\beta|^2\le s\).

For the complementary regime, use a second identity. For third roots of unity \(\zeta\), put
\[
T_\zeta=A+\zeta D+\zeta^{-1}|01\rangle.
\]
Its coefficient matrix has zero fourth row and column, and its first three columns satisfy
\[
C_1=\zeta^{-1}C_0-\zeta C_2.
\]
Hence every \(T_\zeta\) has Schmidt rank at most two, and
\[
\boxed{
\frac13\sum_{\zeta^3=1}[T_\zeta]=[A]+[D]+[01].
}
\tag{29}
\]

Whenever \(s|\beta|^2\ge1\),
\[
\begin{aligned}
R_{\beta|1\rangle}
={}&\frac13\sum_{\zeta^3=1}[T_\zeta]+[B]
+s[02+\beta31]+r[E]\\
&+(s|\beta|^2-1)[01]+s[32]+r[23]+r[30].
\end{aligned}
\tag{30}
\]
All remaining vectors have rank at most two.

The conditions \(|\beta|^2\le s\) and \(|\beta|^2\ge1/s\) cover all nonnegative \(|\beta|^2\), since \(s>1\). Together with §6,
\[
\boxed{\operatorname{SN}(\rho_{\beta|1\rangle})=2
\quad\text{for every }\beta\in\mathbb C.}
\tag{31}
\]

### 7.2 Arbitrary mixing into core coordinate \(2\)

Let \(w=\gamma|2\rangle\) and \(x=|\gamma|^2\). Define
\[
G_0=\frac15\sum_{z^5=1}
[zA+B-z^2D+z^{-1}|02\rangle]
=[A]+[B]+[D]+[02].
\tag{32}
\]
Its vectors satisfy the same rank-two column relation.

Direct completion of a square gives
\[
\boxed{
\begin{aligned}
R_{\gamma|2\rangle}
={}&G_0\\
&+s(1+x)\left[32+\frac{\bar\gamma}{1+x}02\right]\\
&+\left(s-1+\frac{s x^2}{1+x}\right)[02]\\
&+r[E]+r[23]+r[30].
\end{aligned}
}
\tag{33}
\]
The second-line vector is a product vector with Bob coordinate \(2\). All coefficients are nonnegative for every \(x\ge0\).

For example, its combined \(02\) coefficient, excluding \(G_0\), is
\[
\frac{s x}{1+x}+s-1+\frac{s x^2}{1+x}
=s(1+x)-1,
\]
and its cross coefficient with \(32\) is \(s\bar\gamma\), as required.

Consequently
\[
\boxed{\operatorname{SN}(\rho_{\gamma|2\rangle})=2
\quad\text{for every }\gamma\in\mathbb C.}
\tag{34}
\]

No projective limiting endpoint at infinite parameter is included in these finite-parameter exact-SN2 statements.

---

## 8. Why this is not the old coherent-merger gauge

Let the original distinguished Bob spaces be
\[
C=\operatorname{span}\{|0\rangle,|1\rangle,|2\rangle\},\qquad
E_{\rm ext}=\operatorname{span}\{|3\rangle,|4\rangle\}.
\]

For a rank-four old coherent merger:

- \(\dim K(E_{\rm ext})=1\);
- \(K(C)\cap K(E_{\rm ext})=\{0\}\).

For the present \(K_w\), whenever \(w\ne0\):

- \(K_w(E_{\rm ext})=\operatorname{span}\{|3\rangle,w\}\) has dimension two;
- \(K_w(C)\cap K_w(E_{\rm ext})=\operatorname{span}\{w\}\) has dimension one.

These dimensions are invariant under invertible output-coordinate changes and under input basis changes separately preserving the distinguished core and extension spaces. Thus the present nonzero-\(w\) filters cannot be obtained from the old coherent merger by those gauge changes.

Equivalently,
\[
\ker K_w=\operatorname{span}\{(-\alpha,-\beta,-\gamma,0,1)^T\},
\tag{35}
\]
which has a nonzero core component whenever \(w\ne0\). The old merger’s kernel lies entirely in \(E_{\rm ext}\).

This establishes the relevant fixed-source, core-versus-extension distinction. It is not an exhaustive classification of all local automorphisms of the original source family.

### All filters with a covered kernel

If \(K'\) is any rank-four \(4\times5\) matrix satisfying
\[
\ker K'=\ker K_w,
\]
then
\[
K'=LK_w
\]
for an invertible \(4\times4\) matrix \(L\), by the induced isomorphisms from the common quotient.

Its output is \((I\otimes L)R_w(I\otimes L)^\dagger\). Invertible local filtering preserves Schmidt number in both directions, so every covered-kernel filter has SN exactly two after normalization. Physical rescaling does not change that conclusion.

---

## 9. Explicit simultaneous-core-mixing physical member

Take
\[
s=r=3,\qquad \alpha=\beta=\gamma=1,\qquad
w=|0\rangle+|1\rangle+|2\rangle.
\]
The ellipsoid condition holds:
\[
\frac13+\frac12=\frac56<1,\qquad \delta=\frac12.
\]

The actual operator is
\[
\boxed{
\begin{aligned}
R_*={}&[A]+[B]+[D]\\
&+3[02+30+31+32]+3[20+33]\\
&+3[00+01+02]+3[32]+3[23]+3[30].
\end{aligned}
}
\tag{36}
\]
Its trace is \(43\). In the complete block matrix (9), its diagonal blocks are
\[
D_0=
\begin{pmatrix}
4&3&3&0\\3&4&3&0\\3&3&6&0\\0&0&0&0
\end{pmatrix},\quad
D_1=\operatorname{diag}(1,1,1,0),
\]
\[
D_2=\operatorname{diag}(3,1,1,3),\quad
D_3=
\begin{pmatrix}
6&3&3&0\\3&3&3&0\\3&3&6&0\\0&0&0&3
\end{pmatrix}.
\]
Its off-diagonal blocks are
\[
X=E_{01}+E_{12},\quad Y=E_{02},\quad H=E_{12}-E_{01},
\]
\[
P=
\begin{pmatrix}
0&0&0&0\\0&0&0&0\\3&3&3&0\\0&0&0&0
\end{pmatrix},\qquad J=3E_{03},
\]
with the adjoints and zero blocks exactly as in (9). This fully specifies the actual \(16\times16\) matrix.

### Exact PPT certificate

Equation (13) becomes
\[
\begin{aligned}
R_*^\Gamma
={}&[01+10]+[12+21]+[00]+[22]\\
&+[02+11-20]+2[02+20]\\
&+3[23+30]+3[00+01+02+32]\\
&+3[33]+3[30+31+32]\succeq0.
\end{aligned}
\tag{37}
\]

### Exact finite SN2 certificate

Put \(U_*=|02\rangle+|30\rangle+|31\rangle\). Then
\[
G_*=\frac15\sum_{z^5=1}
[zA+B-z^2D+z^{-1}U_*+z^{-2}|32\rangle],
\]
and
\[
\boxed{
\begin{aligned}
R_*={}&G_*+2\left[U_*+\frac32|32\rangle\right]
+\frac12[32]\\
&+3[20+33]+3[00+01+02]+3[23]+3[30].
\end{aligned}
}
\tag{38}
\]
Every vector has the stated rank-two or product certificate. Section 6 supplies the entanglement lower bound, so
\[
\operatorname{SN}(R_*/43)=2.
\]

Its marginals, computed by direct partial traces of (36), are
\[
\rho_{*,A}=\frac1{43}
\begin{pmatrix}
14&0&0&3\\
0&3&0&0\\
0&0&8&0\\
3&0&0&18
\end{pmatrix},
\]
\[
\rho_{*,B}=\frac1{43}
\begin{pmatrix}
14&6&6&0\\
6&9&6&0\\
6&6&14&0\\
0&0&0&6
\end{pmatrix}.
\tag{39}
\]
Both have full rank, also established independently by the general positive lower bounds (14).

Here the physical filter is \(K_w/2\). Applied to the original \(Q_{3,3}/31\), it succeeds with probability
\[
\boxed{p_*=\frac{43}{124}}
\tag{40}
\]
and produces exactly \(R_*/43\).

---

## 10. Relation to the original SN3 parent and actual detectors

For completeness, the original parent’s range matrices are
\[
Y=
\begin{pmatrix}
a&b&c&0&h\\
d&a&b&0&0\\
e&-d&a&k&0\\
f&0&g&e&c
\end{pmatrix}.
\]
The five source minors are
\[
\begin{aligned}
g_1&=e(a^2-bd),&
g_2&=c(a^2+bd),\\
g_3&=e(b^2-ac),&
g_4&=-c(d^2+ae),\\
g_5&=a^3+b^2e-d^2c-ace.
\end{aligned}
\]
They satisfy the corrected identity already supplied in the frozen inputs,
\[
a(g_5-g_3-g_4)-\frac12(cg_1+eg_2)=a^4.
\tag{41}
\]
Thus every rank-at-most-two parent range vector has \(a=0\), inconsistent with a positive rank-two decomposition of a parent having \(00\) diagonal entry one. The original projector decomposition has ranks at most three. Hence its SN is exactly three.

The present candidate therefore establishes an actual
\[
\boxed{\text{PPT/SN3 parent}\ \longrightarrow\ \text{PPT/SN2 output}}
\]
under a different, explicitly core-mixing filter class.

On the same physical \(4\times4\) output space, let \(W=W^\dagger\) satisfy
\[
\langle\psi|W|\psi\rangle\ge0
\quad\text{for every complex }\psi
\text{ with Schmidt rank at most two}.
\]
The positive decompositions above imply
\[
\boxed{\operatorname{Tr}(W\rho_w)\ge0}
\tag{42}
\]
for every covered output, and likewise after any invertible output filtering when the detector has the corresponding full complex rank-two property.

This is the actual state–detector consequence. No sampled detector positivity, ordinary-positive-map surrogate or free-marginal SDP certificate is substituted for universal complex rank-two block positivity.

---

## 11. Exact residual and unpaid obligations

1. **Original target:** no \(4\times4\) PPT/SN3 state or universally valid detecting \(W\) with negative expectation is supplied. The unrestricted existence question remains open here.

2. **Uncovered canonical filters:** general maps fixing \(0,1,2,3\) may send
   \[
   |4\rangle\mapsto\alpha|0\rangle+\beta|1\rangle+\gamma|2\rangle+\eta|3\rangle.
   \]
   The new theorem treats \(\eta=0\), with the stated ellipsoid and coordinate-line enlargements. It does not classify arbitrary \(\eta\).

3. **Outside the proved region:** when \(\eta=0\), \(\delta<0\), and neither additional coordinate-line certificate applies, the first missing step is a positive complex rank-two decomposition of the **actual \(R_w\)**, or an actual universally rank-two-block-positive detector separating it. A negative residual coefficient in (21) only invalidates that decomposition; it does not prove SN3.

4. **Assurance:** disjoint reconstruction and parent disposition remain required. No independent-model-family, human, formal/kernel, exhaustive literature, novelty or source-wide equivalence claim is made.

5. **Execution and materialization:** all displayed results are written algebra. No scientific code was generated or run, and no file was written. This full body is returned for Main materialization without a file-write bypass.

**Deliverable:** a self-contained new proper core-mixing filter-family SN2 theorem, whole-line enlargements, a complex range-based entanglement proof, and an explicit full-local-rank physical \(4\times4\) PPT/SN2 member with exact filter success probability.