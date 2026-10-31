# author-candidate-v1.md

## Exact Schmidt-number collapse under coherent merging of two grid extensions

**Status: AUTHOR CANDIDATE — complete written proof, not independently reviewed.**

**Result.** For the entire weighted grid-extension family defined below, every PPT member obtained by coherently merging the two added Bob coordinates has Schmidt number **exactly two**. The parameters include arbitrary complex merging coefficients, both extension coherences may be nonzero, and the resulting states have full four-dimensional local supports whenever the merging coefficients do not both vanish.

This is a whole-family obstruction to a specific, physically meaningful route from a \(4\times5\) PPT/SN3 state to a \(4\times4\) PPT/SN3 state. It is **not** an unrestricted \(4\times4\) no-go theorem.

### Provenance and execution boundary

Before scientific packet reading, I read the complete manifest, freeze receipt, all ten permission/status controls, and parent-supplied live metadata, then sent the direct pre-body ACK. I subsequently read the entire ordered literal packet, LF 1–108, in consecutive raw chunks of at most 20 LF, including its ending.

Bindings, **as observed and supplied by parent**, are:

- Manifest SHA256: `8e672f9fe55b7831023110900cec4c418a42bc2b6c11ec51213676b1aa790cdb`
- Receipt SHA256: `8a767b9205d460ba7ad1c9afea3096ec8c7c1fa43760c91d6721b394c55050a1`
- Packet SHA256: `013c048871819ce672e02c1b0783b6bdf103d1cd0ad6e379f6cc21c16a4e9704`
- Parent metadata clock: `2026-10-30T12:17:35-0700 PDT`

These are not child-executed hash or native-clock observations.

After packet reading, I consulted the public primary sources. The construction below uses the grid support and range parametrization in [Krebs–Gachechiladze, *Scaling Bound Entanglement through Local Extensions*, Theorem 5 and Eq. (11)](https://arxiv.org/html/2509.07086v1). Its parent \(4\times5\) construction is prior published mathematics; the coherent-merger family certificate below is the present author candidate. Publication priority has not been investigated.

Fresh selected written cases were used in this GENERAL AUTHOR duty, including balanced extension weights and the integer-coefficient example in §7. They are not presented as unselected review or independent evidence.

**Scientific execution: NOT RUN.** No scientific executable, solver, build, test, external-model CLI, or filesystem modification was used. There is no claimed stdout, runtime, or machine-verified PSD result. The certificates are the explicit algebraic identities below. No held scientific payload or consumer was opened.

---

## 1. The physical family

Use computational coordinates \(|ij\rangle\), and write \([x]=|x\rangle\langle x|\). Set

\[
\begin{aligned}
A&=|00\rangle+|11\rangle+|22\rangle,\\
B&=|01\rangle+|12\rangle,\\
D&=|10\rangle-|21\rangle,\\
F_v&=|02\rangle+v|33\rangle,\\
E_u&=|20\rangle+u|33\rangle.
\end{aligned}
\]

For \(s,r>0\) and arbitrary \(u,v\in\mathbb C\), define the following explicit \(16\times16\) operator:

\[
\boxed{
R_{s,r}(u,v)=
[A]+[B]+[D]
+s[F_v]+r[E_u]
+s|v|^2[03]+r|u|^2[23]+r[30]+s[32].
}
\tag{1}
\]

It is PSD by construction. Its trace is

\[
Z=7+2(s+r)+2\bigl(s|v|^2+r|u|^2\bigr)>0,
\tag{2}
\]

so \(\rho=R/Z\) is a normalized physical state.

This is not an artificial spectator extension. Consider the \(4\times5\) operator

\[
\begin{aligned}
Q_{s,r}={}&[A]+[B]+[D]\\
&+s\bigl([02+34]+[32]+[04]\bigr)\\
&+r\bigl([20+33]+[23]+[30]\bigr).
\end{aligned}
\tag{3}
\]

Define a Bob map \(K_{u,v}:\mathbb C^5\to\mathbb C^4\) by

\[
K|j\rangle=|j\rangle\quad(j=0,1,2),\qquad
K|3\rangle=u|3\rangle,\qquad
K|4\rangle=v|3\rangle.
\tag{4}
\]

Then

\[
R_{s,r}(u,v)
=(I\otimes K_{u,v})Q_{s,r}(I\otimes K_{u,v})^\dagger.
\tag{5}
\]

Thus \(u,v\) coherently merge the two extension coordinates into the same fourth Bob coordinate. Any such \(K\) can be rescaled to a contraction without changing the normalized output state. When \(|u|^2+|v|^2=1\), \(K\) is itself a coisometry retaining the original three Bob coordinates.

---

## 2. Exact PPT region

Let \(\Gamma\) denote Bob partial transpose. On the ordered basis \((|02\rangle,|11\rangle,|20\rangle)\), define

\[
M_{s,r}=
\begin{pmatrix}
s&1&1\\
1&1&-1\\
1&-1&r
\end{pmatrix}.
\tag{6}
\]

Direct partial transposition of (1) gives

\[
\begin{aligned}
R^\Gamma={}&
[01+10]+[12+21]+[00]+[22]+M_{s,r}\\
&+r[\bar u\,23+30]
+s[\bar v\,03+32]\\
&+\bigl(r|u|^2+s|v|^2\bigr)[33].
\end{aligned}
\tag{7}
\]

Here \(M_{s,r}\) is embedded on its indicated three-dimensional subspace. The displayed summands have mutually disjoint supports except within their specified blocks. Consequently \(R^\Gamma\ge0\) exactly when \(M_{s,r}\ge0\).

Taking the Schur complement of the middle entry \(1\), this is equivalent to

\[
\begin{pmatrix}
s-1&2\\
2&r-1
\end{pmatrix}\ge0.
\]

The nonzero off-diagonal entry excludes either diagonal being zero. Hence

\[
\boxed{
R_{s,r}(u,v)\text{ is PPT}
\iff s>1,\quad r>1,\quad (s-1)(r-1)\ge4.
}
\tag{8}
\]

This includes equality and all complex \(u,v\).

An explicit PSD certificate for the central block is

\[
\begin{aligned}
M_{s,r}={}&[02+11-20]\\
&+(s-1)\left[02+\frac{2}{s-1}20\right]\\
&+\left(r-1-\frac4{s-1}\right)[20].
\end{aligned}
\tag{9}
\]

Throughout the PPT region,

\[
sr\ge9.
\tag{10}
\]

Indeed, with \(x=s-1>0\), \(y=r-1>0\), one has \(xy\ge4\), \(x+y\ge4\), and \(sr=1+x+y+xy\ge9\).

---

## 3. A finite exact rank-two building block

Let \(z\) range over the fourth roots of unity and \(w\) over the third roots of unity. For \(v\in\mathbb C\) and real \(\alpha>0\), define

\[
\begin{aligned}
V_{z,w}(v,\alpha)={}&
zA+B-z^2D+z^{-1}F_v\\
&+2\alpha zw\,|03\rangle
+\alpha z^3w\,|23\rangle\\
&+\frac v\alpha z^{-1}w^{-1}|30\rangle.
\end{aligned}
\tag{11}
\]

Its coefficient matrix is

\[
\begin{pmatrix}
z&1&z^{-1}&2\alpha zw\\
-z^2&z&1&0\\
0&z^2&z&\alpha z^3w\\
(v/\alpha)z^{-1}w^{-1}&0&0&vz^{-1}
\end{pmatrix}.
\tag{12}
\]

Using zero-based column indices, its columns satisfy

\[
C_2=z^{-1}C_1,\qquad
C_3=\alpha w C_0+\alpha zw C_1.
\tag{13}
\]

Therefore every displayed vector has Schmidt rank at most two. This is a complex algebraic identity, not a real-vector or numerical test.

Root averaging gives the exact operator identity

\[
\boxed{
\begin{aligned}
G(v,\alpha)
&:=\frac1{12}\sum_{z^4=1}\sum_{w^3=1}[V_{z,w}(v,\alpha)]\\
&=[A]+[B]+[D]+[F_v]\\
&\quad+4\alpha^2[03]+\alpha^2[23]
+\frac{|v|^2}{\alpha^2}[30].
\end{aligned}}
\tag{14}
\]

For completeness, the original four terms have distinct \(z\)-characters \(1,0,2,3\). The added terms have nonzero \(w\)-characters, so their cross terms with the original terms vanish. The \(|03\rangle\)–\(|23\rangle\) cross term vanishes by its \(z\)-character difference two; cross terms involving \(|30\rangle\) vanish by a nontrivial \(w\)-character. This leaves precisely (14).

A reflected identity supplies the other extension. Put

\[
T=\operatorname{diag}(1,1,-1,1),\qquad
L=(T\otimes T)\operatorname{SWAP}.
\]

The transformation \(L\) preserves Schmidt rank and sends

\[
A\mapsto A,\quad B\mapsto D,\quad D\mapsto B,
\]
\[
|02\rangle\mapsto-|20\rangle,\quad
|33\rangle\mapsto|33\rangle,
\]
\[
|03\rangle\mapsto|30\rangle,\quad
|23\rangle\mapsto-|32\rangle,\quad
|30\rangle\mapsto|03\rangle.
\]

Thus

\[
\boxed{
\begin{aligned}
H(u,\alpha)
&:=L G(-u,\alpha)L^\dagger\\
&=[A]+[B]+[D]+[E_u]\\
&\quad+4\alpha^2[30]+\alpha^2[32]
+\frac{|u|^2}{\alpha^2}[03]
\end{aligned}}
\tag{15}
\]

also has an explicit twelve-vector Schmidt-rank-at-most-two decomposition.

---

## 4. Exhaustive Schmidt-number-two certificate

Assume the exact PPT conditions (8).

### Case 1: \(v=0\)

Four-root averaging alone gives

\[
\frac14\sum_{z^4=1}
[zA+B-z^2D+z^{-1}|02\rangle]
=[A]+[B]+[D]+[02].
\tag{16}
\]

Each vector has rank at most two, as follows from (12)–(13) with the added coordinates omitted. The remainder of \(R\) is

\[
(s-1)[02]+r[E_u]+r|u|^2[23]+r[30]+s[32],
\tag{17}
\]

a positive sum of Schmidt-rank-at-most-two projectors. Therefore \(\mathrm{SN}(R)\le2\).

### Case 2: \(v\ne0\) and \(|v|\le r|u|\)

Choose

\[
\alpha^2=\frac{|v|^2}{r}>0.
\]

Subtracting (14) from (1) gives

\[
\boxed{
\begin{aligned}
R-G(v,\alpha)={}&
(s-1)[F_v]+r[E_u]\\
&+|v|^2\left(s-\frac4r\right)[03]\\
&+\left(r|u|^2-\frac{|v|^2}{r}\right)[23]
+s[32].
\end{aligned}}
\tag{18}
\]

Every coefficient is nonnegative: \(sr\ge9>4\), and the case hypothesis gives \(|v|^2\le r^2|u|^2\). Every vector on the right has Schmidt rank at most two. Hence \(\mathrm{SN}(R)\le2\).

### Case 3: \(v\ne0\) and \(|v|>r|u|\)

Choose

\[
\alpha^2=\frac1{sr^2}>0.
\]

Subtracting (15) gives

\[
\boxed{
\begin{aligned}
R-H(u,\alpha)={}&
s[F_v]+(r-1)[E_u]\\
&+s\bigl(|v|^2-r^2|u|^2\bigr)[03]
+r|u|^2[23]\\
&+\left(r-\frac4{sr^2}\right)[30]
+\left(s-\frac1{sr^2}\right)[32].
\end{aligned}}
\tag{19}
\]

Again every coefficient is nonnegative. In particular,

\[
sr^3>9>4,\qquad s^2r^2\ge81>1,
\]

which establish the last two signs. This case includes \(u=0\). Therefore \(\mathrm{SN}(R)\le2\).

The three cases exhaust all complex \(u,v\), including every boundary and zero case.

---

## 5. The Schmidt number is exactly two

Compress \(R\) to Alice and Bob coordinates \(0,1,2\). The resulting operator is

\[
C=[A]+[B]+[D]+s[02]+r[20].
\tag{20}
\]

Its range consists of matrices

\[
X=
\begin{pmatrix}
a&b&c\\
d&a&b\\
e&-d&a
\end{pmatrix}.
\tag{21}
\]

If \(X\) has rank at most one, two of its minors give

\[
a^2-bd=0,\qquad a^2+bd=0.
\]

Over \(\mathbb C\), these imply \(a=0\).

In any positive separable decomposition of \(C\), every product vector lies in \(\operatorname{range}(C)\): its component along any kernel vector must vanish because the corresponding sum of squared overlaps is zero. Every such product vector would therefore have zero \(|00\rangle\) component. That contradicts

\[
\langle00|C|00\rangle=1.
\]

Thus \(C\) is entangled, so \(R\) is entangled. Together with §4,

\[
\boxed{
\mathrm{SN}\!\left(\frac{R_{s,r}(u,v)}{Z}\right)=2
}
\tag{22}
\]

for the entire PPT parameter region (8).

This is not restricted to states with a missing fourth local dimension. Writing \(d=s|v|^2+r|u|^2\), the unnormalized marginals are

\[
\operatorname{Tr}_B R
=\operatorname{diag}
\bigl(2+s+s|v|^2,\ 3,\ 2+r+r|u|^2,\ s+r+d\bigr),
\]

\[
\operatorname{Tr}_A R
=\operatorname{diag}(2+2r,\ 3,\ 2+2s,\ 2d).
\tag{23}
\]

Both have rank four whenever \((u,v)\ne(0,0)\).

---

## 6. The \(4\times5\) parent really has Schmidt number three

The contrast underlying the obstruction is genuine.

The partial transpose of (3) is

\[
\begin{aligned}
Q^\Gamma={}&
[01+10]+[12+21]+[00]+[22]+M_{s,r}\\
&+r[23+30]+s[04+32]+r[33]+s[34].
\end{aligned}
\tag{24}
\]

Hence \(Q\) is PPT in exactly the same region (8).

Because all its projector weights are positive, its range has the parametrization

\[
Y=
\begin{pmatrix}
a&b&c&0&h\\
d&a&b&0&0\\
e&-d&a&k&0\\
f&0&g&e&c
\end{pmatrix}.
\tag{25}
\]

This is the grid range in the cited primary source’s Eq. (11).

Five \(3\times3\) minors are

\[
\begin{aligned}
g_1&=e(a^2-bd),&
g_2&=c(a^2+bd),\\
g_3&=e(b^2-ac),&
g_4&=-c(d^2+ae),\\
g_5&=a^3+b^2e-d^2c-ace.
\end{aligned}
\tag{26}
\]

Their row/column index sets, respectively, are

\[
(013;013),\quad(123;124),\quad(013;123),\quad
(123;014),\quad(012;012).
\]

The following exact polynomial identity holds:

\[
\boxed{
a(g_5-g_3-g_4)-\frac12(cg_1+eg_2)=a^4.
}
\tag{27}
\]

Indeed,

\[
g_5-g_3-g_4=a^3+ace,\qquad
\frac12(cg_1+eg_2)=a^2ce.
\]

Consequently, rank at most two forces \(a=0\). Any positive decomposition of \(Q\) into Schmidt-rank-at-most-two vectors would then have zero \(|00\rangle\) diagonal, contradicting its value one. Thus \(\mathrm{SN}(Q)>2\). Its displayed projector decomposition has ranks at most three, so

\[
\boxed{\mathrm{SN}(Q)=3.}
\tag{28}
\]

Equation (27) is the identity actually used here, derived explicitly rather than quoted verbatim. The primary source’s printed post-Eq. (12) multiplier expression is different; no correctness claim about that printed multiplier expression is needed for this proof. This localized algebraic distinction does not refute its Theorem 5.

Therefore the theorem proved above says:

> Every coherent merger (4) of this entire weighted PPT/SN3 grid family reduces its Schmidt number from three to exactly two.

It does not address arbitrary Bob filters mixing the three core coordinates with the two extension coordinates.

---

## 7. An explicit integer-coefficient, full-local-rank \(4\times4\) member

Take \(s=r=3\) and \(u=v=1\). Then

\[
\begin{aligned}
R_*={}&[A]+[B]+[D]\\
&+3[02+33]+3[20+33]\\
&+3[03]+3[23]+3[30]+3[32],
\end{aligned}
\tag{29}
\]

with trace \(31\). Both extension coherences are active. Its exact partial-transpose certificate is

\[
\begin{aligned}
R_*^\Gamma={}&
[01+10]+[12+21]+[02+11-20]\\
&+2[02+20]+3[23+30]+3[03+32]\\
&+[00]+[22]+6[33]\ge0.
\end{aligned}
\tag{30}
\]

Its exact SN2 certificate is (14) at \(\alpha=1/\sqrt3\), together with

\[
\boxed{
R_*-G(1,1/\sqrt3)
=2[02+33]+3[20+33]
+\frac53[03]+\frac83[23]+3[32].
}
\tag{31}
\]

Every term has explicitly proved Schmidt rank at most two. The normalized state \(\rho_*=R_*/31\) satisfies

\[
\rho_{*,A}=\rho_{*,B}
=\frac1{31}\operatorname{diag}(8,3,8,12).
\tag{32}
\]

Thus this is an actual, full-local-rank \(4\times4\) PPT entangled state with **SN exactly two**, not an SN3 witness.

The merger producing it can be implemented by the contraction \(K_{1,1}/\sqrt2\). On the normalized \(Q_{3,3}/31\), its success probability is \(1/2\), and its normalized output is precisely \(\rho_*\).

These are written exact identities, not reported execution results.

---

## 8. Same-physical-detector consequence and remaining obligations

Let \(W\) be any Hermitian \(16\times16\) operator satisfying the full complex quantifier

\[
\langle\psi|W|\psi\rangle\ge0
\quad
\text{for every }\psi\in\mathbb C^4\otimes\mathbb C^4
\text{ of Schmidt rank at most two}.
\]

The explicit positive decompositions above immediately imply

\[
\boxed{
\operatorname{Tr}\!\left(W\,R_{s,r}(u,v)/Z\right)\ge0
}
\tag{33}
\]

throughout (8). Thus **no valid Schmidt-rank-two-block-positive detector on the same physical \(4\times4\) system can certify SN3 anywhere in this family**.

### Exact admissibility scope

The candidate covers:

- Every \(s,r>1\) with \((s-1)(r-1)\ge4\), including equality.
- Arbitrary complex \(u,v\), including either or both being zero.
- Both extension coherences active simultaneously.
- Full four-dimensional local supports whenever \((u,v)\ne(0,0)\).
- An explicit finite decomposition, with no numerical PSD assumptions or restriction of detector quantifiers to real vectors.

### What remains unproved

1. **The original \(4\times4\) PPT/SN3 existence question remains NOT PROVED.** No actual \(16\times16\) PPT/SN3 state–detector pair is supplied.
2. **There is no unrestricted no-go theorem.** No reduction shows that every \(4\times4\) PPT state has form (1).
3. General \(5\to4\) Bob filters that mix core and extension coordinates are outside the merger form (4).
4. Other grid supports, coherent couplings, filler patterns and detector constructions are outside this theorem.
5. Nothing here enlarges the frozen CP-collapse result to all SDPs, or changes the distinction between ordinary positivity and 2-positivity of the public Eq. (10) seed.
6. Disjoint review and parent disposition remain outstanding. No human, independent-model-family, formal/kernel, exhaustive literature, novelty, or original-target acceptance is claimed.

**Deliverable:** a complete written whole-family obstruction, with a genuinely SN3 \(4\times5\) parent and an exact proof that the specified coherent-merger route always yields SN2. The full body is returned for Main materialization; no file was written.