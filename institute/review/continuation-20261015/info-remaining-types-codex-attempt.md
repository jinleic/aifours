RESULT: PARTIAL

## Statements

Write
\[
\mathcal Z=\{a:p(a)=0\},\qquad z=|\mathcal Z|,
\qquad c=\#\{a:|p(a)|=1\}.
\]
Under the task’s hypotheses, the following stronger necessary conditions hold.

| Type | Necessary condition proved here |
|---|---|
| \((6,112)\) | \(z=4\) or \(z\ge12\). If \(z=4\), then \(c\in\{8,12,16,20,24,28\}\). |
| \((6,128)\) | \(z=8\) or \(z\ge12\). If \(z=8\), the zero set is invariant under \(\operatorname{rad}(B)\cap D^{-1}(0)\). |
| \((8,120)\) | \(z=10\) or \(z\ge14\). |
| \((8,136)\) | If \(z=12\), the pair \((D,\mathcal Z)\) has the unique linear normal form below. |

The twelve-zero normal form, with coordinates \(x_0,\ldots,x_7\), is
\[
\begin{aligned}
D_*={}&x_0(x_1+\cdots+x_7)
+x_1x_2+x_1x_3+x_2x_3+x_4x_5+x_6x_7,\\
\mathcal Z_*={}&
\{0,1,2,4,8,15,16,32,62,64,128,206\}.
\end{aligned}
\tag{1}
\]
Integers encode vectors by their binary coordinates. Thus every twelve-zero case of type \((8,136)\) is linearly equivalent to this explicit configuration.

There is also a general geometric restriction:

> If an affine \(m\)-flat \(A\subseteq D^{-1}(0)\), with \(m\ge4\), meets \(\mathcal Z\), then
> \[
> \deg(1_{\mathcal Z}|_A)\le3,
> \qquad |\mathcal Z\cap A|\ge2^{m-3}.
> \tag{2}
> \]
> In particular, intersections with zero four-flats have even cardinality; intersections with zero five-flats have even cardinality and XOR zero.

No complete remaining type is excluded. No novelty claim is made.

## Proofs

### 1. Imported facts and conventions

I use the established [zero-set and next-bit lemmas](reviewed/zero-set-lemmas-candidate.md), with their [review errata](reviewed/zero-set-lemmas-opus-review.json), and the supplied canonical-spectrum facts.

In particular,
\[
p\in\{-3,\ldots,3\},\quad
\widehat p\in\{0,\pm64\},\quad
D=p\bmod2,\quad
\widehat{p^2}\equiv0\pmod{32},
\tag{3}
\]
and
\[
E=(p-D)/2\bmod2=F_4+P_3,\qquad \deg P_3\le3,
\tag{4}
\]
where \(F_4\) has the prescribed Pfaffian coefficients.

Also,
\[
z\equiv0\pmod2,\qquad
\bigoplus_{a\in\mathcal Z}a=0,\qquad
\sum_{a\in\mathcal Z}aa^{\mathsf T}=\mathcal C(B).
\tag{5}
\]
On \(D=0\), the allowed values \(p=0,\pm2\) give
\[
1_{\mathcal Z}=1+E.
\tag{6}
\]

All polynomial identities in what follows are over \(\mathbb F_2\), unless indicated otherwise. I apply the imported lemmas directly after each linear coordinate change: the Fourier hypotheses are invariant under such changes. This avoids assuming a cofactor covariance formula.

### 2. Restriction to affine zero flats

Let \(A=a_0+V\), \(\dim V=m\), and \(A\subseteq D^{-1}(0)\). The Fourier transform of a restriction is
\[
\widehat{p|_A}(\lambda)
=2^{m-8}\sum_{x|_V=\lambda}
(-1)^{x\cdot a_0}\widehat p(x).
\]
Consequently every coefficient is divisible by \(2^{m-2}\).

Because \(p|_A\) is even, put \(u=p|_A/2\). Its transform is divisible by \(2^{m-3}\).

For an integer function \(v\) on \(m\) variables, divisibility
\(\widehat v\equiv0\pmod{2^k}\) implies
\[
\deg(v\bmod2)\le m-k.
\tag{7}
\]
Indeed, mixed Fourier differences show that every moment
\(\sum_{a:a_i=1\ (i\in T)}v(a)\) is even for \(|T|<k\). Descending through the ANF coefficients gives the asserted degree bound.

Here \(u\bmod2=1+1_{\mathcal Z}|_A\), so (7) proves the degree assertion in (2). A nonzero Boolean polynomial of degree at most three on \(m\) variables has weight at least \(2^{m-3}\). This follows by induction, splitting in one variable and using the derivative’s degree bound.

For \(m=4\), summing a cubic gives even weight. For \(m=5\), summing it after multiplication by any coordinate also gives zero. These are precisely the stated intersection parity and XOR conditions.

### 3. A quadratic restriction bound in six variables

Put
\[
q=x_0x_1+x_2x_3+x_4x_5,\qquad
U_0=\{x\in\mathbb F_2^6:q(x)=0\}.
\]
Thus \(\operatorname{wt}(q)=28\) and \(|U_0|=36\).

For every quadratic \(b\notin\{0,q\}\),
\[
\operatorname{wt}(b|_{U_0})\ge6.
\tag{8}
\]

To prove this, use
\[
2\operatorname{wt}(b|_{U_0})
=\operatorname{wt}(b)+\operatorname{wt}(b+q)-28.
\tag{9}
\]
A nonzero six-variable quadratic has weight at least sixteen; its next possible weight is twenty-four. Weight sixteen forces polar rank two. Both \(b\) and \(b+q\) cannot have weight sixteen, since their polar matrices would have ranks two and their sum would have rank at most four, whereas \(q\) has rank six. Their weights therefore sum to at least forty, proving (8).

Two consequences will be used:

* The only quadratics vanishing on \(U_0\) are \(0,q\).
* Every nonzero affine function takes value one on at least sixteen points of \(U_0\). For a nonconstant affine function this count is sixteen or twenty, by the quadratic weight formula.

### 4. Type \((6,112)\): four zeros or at least twelve

Choose linear coordinates
\[
D=q(x),\qquad K=\operatorname{rad}(B)=\langle r,t\rangle.
\]
The prescribed quartic is independent of \(r,t\), so (4) has the unique form
\[
E=F_4(x)+A_3(x)+rB_2(x)+tC_2(x)+rtL_1(x),
\tag{10}
\]
where subscripts bound degrees.

Suppose \(z<12\).

If \(L_1\ne0\), it is one on at least sixteen points of \(U_0\). At each such \(x\), \(1+E(x,r,t)\) is a two-variable quadratic with \(rt\)-coefficient one, and hence has odd, nonzero weight. This gives \(z\ge16\), a contradiction. Thus \(L_1=0\).

If either \(B_2|_{U_0}\) or \(C_2|_{U_0}\) is nonzero, (8) gives at least six \(x\)-fibres where \(1+E\) is a nonconstant affine function of \(r,t\). Each contributes two zeros, giving \(z\ge12\).

Therefore \(\mathcal Z\) is \(K\)-invariant when \(z<12\).

Every \(K\)-coset has second-moment matrix equal to the standard alternating matrix on \(K\). In rank six, (5) requires precisely that matrix. Thus a \(K\)-invariant zero set contains an odd number of \(K\)-cosets:
\[
z\equiv4\pmod8.
\tag{11}
\]
The only positive possibility below twelve is \(z=4\). This proves the first zero-count restriction.

The argument also proves the more geometric statement
\[
\mathcal Z\text{ not }K\text{-invariant}\quad\Longrightarrow\quad z\ge12.
\tag{12}
\]

### 5. Type \((6,112)\) with four zeros: \(c\ge8\)

The reviewed four-point equality case and balance give
\[
\mathcal Z=K.
\tag{13}
\]

For \(k\in K\), the derivative \(E(a+k)+E(a)\) is quadratic: \(F_4\) is independent of \(K\). By (6) and (13), this derivative vanishes on \(D=0\).

A quadratic on \(\mathbb F_2^6\oplus K\) vanishing there is \(0\) or \(D\). Compare coefficients in \(r,t\); their affine coefficients vanish on \(U_0\), and then apply (8) to the remaining quadratic. Consequently
\[
E(a+k)+E(a)=\chi(k)D(a)
\tag{14}
\]
for one character \(\chi:K\to\mathbb F_2\). Additivity follows from the derivative identity and \(K\)-invariance of \(D\).

For \(x\in\mathbb F_2^6\), define
\[
v(x)=\frac14\sum_{k\in K}(-1)^{\chi(k)}p(x,k).
\tag{15}
\]
This is integral. On \(q=0\), it averages four values \(\pm2\), except for the zero fibre. On \(q=1\), (14) and the definition of \(E\) give
\[
v(x)=\varepsilon_x(-3+\ell_x),
\qquad
\ell_x=\#\{k:|p(x,k)|=1\}.
\tag{16}
\]
Furthermore,
\[
v(0)=0,\qquad \widehat v\in\{0,\pm16\},
\qquad \sum_{q(x)=1}\ell_x=c.
\tag{17}
\]

We need the following global consequence of (17).

**Dual-zero lemma.** Set \(e=\widehat v/16\), and let \(M=\{y:e(y)=0\}\), \(m=|M|\). Then \(Q=v\bmod2\) is quadratic with \(Q(0)=0\), and
\[
B_Q=\sum_{y\in M}yy^{\mathsf T}.
\tag{18}
\]
Moreover \(m\) is even, \(\bigoplus M=0\), and if \(r=\operatorname{rank}B_Q>0\), then
\[
m\ge r+2,\qquad
\sum_xv(x)^2=256-4m.
\tag{19}
\]

To prove it, Fourier inversion gives \(\widehat e=4v\) and \(\sum e=0\). Expanding characters modulo eight,
\[
v(a)\equiv
-\sum_i\frac{\sum_y e(y)y_i}{2}a_i
+\sum_{i<j}\Bigl(\sum_y e(y)y_iy_j\Bigr)a_ia_j
\pmod2.
\]
The displayed halves are integral because \(\widehat e\) is divisible by four. Since \(e\bmod2\) is the indicator of \(M^c\), this proves (18), evenness and XOR zero. The finite-set rank bound gives \(r\le m-2\). Parseval gives the energy formula in (19).

Now put \(b=\operatorname{wt}((Q+q)|_{q=1})\). Equation (16) implies
\[
b=\#\{x:q(x)=1,\ \ell_x\text{ odd}\}\le c.
\]
For \(0\le\ell\le4\),
\[
(\ell-3)^2\ge9-4\ell-(\ell\bmod2).
\]
Adding this on \(q=1\), and using \(v^2\ge Q\) on \(q=0\), yields
\[
\sum_xv(x)^2\ge224-4c+\operatorname{wt}(Q).
\tag{20}
\]

Suppose \(c\le4\).

* If \(Q=q\), then (19) gives energy at most \(224\), whereas (20) gives at least \(252-4c\ge236\).
* Otherwise \(Q+q\) is a nonzero quadratic, so
  \[
  \operatorname{wt}(Q)
  =28+\operatorname{wt}(Q+q)-2b
  \ge44-2c\ge36.
  \]
  Thus \(Q\) is nonlinear, and (19) gives energy at most \(240\). But (20) gives at least \(268-6c\ge244\).

Both cases contradict (17). Hence \(c>4\).

The exact square identity gives
\[
\sum p^2=1024+5(112)-4(4)-8c=1568-8c.
\]
Divisibility by thirty-two forces \(c\equiv0\pmod4\). Therefore \(c\ge8\).

Finally, the established slack identity and correlation bound give
\[
\Gamma=-2304-64(a+c)\ge-4096,
\]
so \(c\le28\). This proves the stated six-value list.

### 6. Type \((6,128)\): eight zeros or at least twelve

Use linear coordinates
\[
D=q(x)+r,\qquad
K=\operatorname{rad}(B)\cap D^{-1}(0)=\langle t\rangle.
\]
Write
\[
E=F_4(x)+A_3(x,r)+t\bigl(C_2(x)+rL_1(x)\bigr).
\]
On \(D=0\), substitute \(r=q(x)\). The coefficient of \(t\) becomes
\[
H(x)=C_2(x)+q(x)L_1(x).
\tag{21}
\]

Every nonzero function of the form (21) has weight at least twelve.

If \(L_1\) is constant, \(H\) is quadratic and its nonzero weight is at least sixteen. Otherwise, after a symplectic coordinate change and absorption of lower-degree terms,
\[
H=C'_2+x_0(x_2x_3+x_4x_5).
\]
The two restrictions at \(x_0=0,1\) are quadratics on five variables. If both are nonzero, each has weight at least eight. If one is zero, the other has polar rank four and weight at least twelve. This proves the assertion.

Each \(x\) with \(H(x)=1\) contributes exactly one point to \(\mathcal Z\). Thus \(z<12\) implies \(H=0\), and \(\mathcal Z\) is \(K\)-invariant.

If it consists of \(N\) \(K\)-cosets, its XOR is \(Nt\). Equation (5) makes \(N\) even, hence \(z=2N\) is divisible by four. The reviewed lower bound \(z\ge8\) now leaves only \(z=8\) below twelve.

### 7. Twelve zeros in rank eight force (1)

Assume rank eight and \(z=12\). Balance puts \(0\in\mathcal Z\). Let \(A\) be the \(8\times11\) matrix whose columns are the other eleven points. Then
\[
AA^{\mathsf T}=B^{-1},\qquad A\mathbf1=0.
\]
Consequently
\[
H=A^{\mathsf T}BA
\]
is symmetric, has zero diagonal, satisfies \(H^2=H\), has rank eight, and annihilates \(\mathbf1\).

Its kernel is a nondegenerate three-space for the ordinary dot product. Because \(\mathbf1\cdot\mathbf1=1\), choose \(u,v\) in its orthogonal complement to \(\mathbf1\), with \(u\cdot v=1\). The projection formula gives
\[
H=I+\mathbf1\mathbf1^{\mathsf T}+uv^{\mathsf T}+vu^{\mathsf T}.
\tag{22}
\]

Partition the eleven indices by their labels \((u_i,v_i)\), with class sizes \(n_0,n_1,n_2,n_3\). Then
\[
n_0\text{ is even},\qquad n_1,n_2,n_3\text{ are odd}.
\tag{23}
\]
For distinct indices, (22) says:

* polar pairing is one within each class;
* it is zero between distinct nonzero classes;
* it is one between class zero and every other class.

Also \(\ker H=\ker A\). Every affine function of the labels therefore supplies a relation among the points. Such a nonzero relation has weight at least three, since the columns are distinct and nonzero.

The relations supported on classes \(1,3\) and \(2,3\), together with \(D=0\) on all columns, imply
\[
\binom{n_1}{2}+\binom{n_3}{2}
=\binom{n_2}{2}+\binom{n_3}{2}=0\pmod2.
\]
Hence all three odd sizes are congruent modulo four.

Up to permutation, the possibilities are
\[
(8;1,1,1),\ (4;1,1,5),\ (0;1,1,9),\
(0;1,5,5),\ (2;3,3,3).
\]
The first three give a relation of weight two. The fourth gives a relation of weight one. Therefore
\[
(n_0;n_1,n_2,n_3)=(2;3,3,3).
\tag{24}
\]

Choose one class-zero point, all three class-one points, two class-two points and two class-three points as a basis. Independence follows directly from the three kernel relations. In these coordinates the remaining points are \(15,62,206\), and the polar pairings give exactly \(D_*\) in (1). This proves uniqueness of the pair’s linear normal form.

Its sign sum is \(-16\): at \(x_0=0\), the three-variable factor \(x_1x_2+x_1x_3+x_2x_3\) has sign sum zero; at \(x_0=1\), the three factors have sign sums \(-4,-2,-2\). Thus
\[
\operatorname{wt}(D_*)=(256+16)/2=136.
\]
Twelve zeros are consequently impossible for type \((8,120)\). The reviewed evenness and lower bounds complete both rank-eight statements.

## Gaps

**GAP — entire-type exclusion:** None of these arguments excludes an entire remaining type. In particular, the four-zero case of \((6,112)\) survives when \(c\ge8\), and its cases with at least twelve zeros remain unresolved.

**GAP — rank-two Boolean realizability:** I did not obtain an obstruction from the coupled six-variable cubic functions for \((2,192)\).

**GAP — sufficiency:** The zero geometries and residue conditions proved here do not establish Boolean realizability. The unreviewed notes’ referenced solver witnesses are not present in this snapshot, and I have not treated their reported statuses as verified evidence.

## Suggested audits

All computations below are finite and use exact integer or binary arithmetic. The proofs above do not depend on solver verdicts.

1. **Six-variable restriction bound.** Evaluate all quadratics on \(U_0\), remove the duplicate caused by adding \(q\), and enumerate the resulting \(2^{21}\) words. My in-memory enumeration found minimum positive weight six, attained by 336 words. A smaller positive weight falsifies (8).

2. **The \((6,128)\) bound.** Enumerate all \(2^{22}\) quadratic perturbations of
   \[
   x_0(x_2x_3+x_4x_5).
   \]
   I obtained minimum weight twelve, attained 32 times. The constant-linear-part case reduces to ordinary quadratic weights.

3. **The four-zero \(c\)-bound.** Enumerate the \(2^{21}\) six-variable quadratics \(Q\) with \(Q(0)=0\). For
   \[
   b=\operatorname{wt}((Q+q)|_{q=1})\le4,
   \]
   I obtained exactly:
   
   | \((b,\operatorname{wt}Q,\operatorname{rank}B_Q)\) | Number |
   |---|---:|
   | \((0,28,6)\) | 1 |
   | \((4,36,6)\) | 210 |
   | \((4,48,2)\) | 105 |
   
   Each violates the energy inequalities for \(c\le4\). This independently audits the finite quadratic possibilities in that proof.

4. **Twelve-zero classification.** Enumerate the five size patterns above and all seven nonzero affine label functions; only \((2;3,3,3)\) avoids relations of weight one or two. Evaluate (1) on all 256 points and check
   \[
   D_*|_{\mathcal Z_*}=0,\quad
   \operatorname{wt}(D_*)=136,\quad
   \sum_{\mathcal Z_*}aa^{\mathsf T}=B_*^{-1}.
   \]
   My checks confirmed these identities.

5. **Direct candidate falsification.** Given any proposed target, compute its 256-entry \(p,D,E\). Check the table in Statements, and enumerate affine zero flats to check (2). A genuine target violating any assertion falsifies the corresponding result.

All checks were performed in memory; no files were modified.

## Why other routes fail

**The original zero moments allow geometries that the new restriction rejects.** For example, with \(D=q(x)\),
\[
X=\{(a,0,b,0,0,0,r,ab):a,b,r\in\mathbb F_2\}
\]
has eight points, contains zero, lies in \(D=0\), has XOR zero, and has second-moment matrix equal to the required alternating matrix on \(\langle r,t\rangle\). Nevertheless, Section 4 excludes it. Thus the strengthened restriction is strictly stronger than those zero moments.

**Bare single-character projection remains insufficient for the four priority types.** If equivariance holds along a zero-radical subspace of dimension \(\tau\), projection gives
\[
9d-24c\le2^{12-\tau}.
\tag{25}
\]
Indeed, project the core \(-3(-1)^E1_{D=1}\) and its correction \(4(-1)^E1_{\{|p|=1\}}\). Their cross term is \(-24c\); Parseval and \(|\widehat p|\le64\) give the right side.

Already at \(c=0\), the relevant numbers are
\[
1008\le1024,\quad1152\le2048,\quad
1080\le4096,\quad1224\le4096.
\]
The stronger four-zero argument above also uses the dual zero-set matrix and Fourier integrality; (25) alone gives no contradiction.

**Energies, canonical means and the \(R\)-side residue geometry still admit explicit integer fakes.** Here is one for \((8,120)\).

Let \(D=\sigma_2\) and \(E=\sigma_4\), the elementary symmetric polynomials on eight variables. In increasing integer order, let:

* \(C\): vectors of weights four or five;
* \(N\): vectors of weights two or three;
* \(P\): vectors of weights six or seven.

Define \(p=2\) on the first 99 members of \(C\), \(p=-2\) on its remaining 27 members, \(p=-3\) on \(N\), \(p=3\) on \(P\), and zero elsewhere.

Set \(T=20\) on the first 43 positive members of \(C\), the first 19 negative members of \(C\), the first 41 members of \(N\), and the first member of \(P\). Set \(T=-28\) elsewhere, and define
\[
S=(-1)^DT,\quad R=8p,\quad
K=(S+R)/2,\quad L=(S-R)/2.
\]

Direct arithmetic gives
\[
\begin{gathered}
|K|+|L|\le28,\qquad K,L\equiv2\pmod8,\\
\sum K=\sum L=256,\qquad
\sum K^2=\sum L^2=65536,\qquad \sum SR=0,\\
z=10,\quad c=0,\quad \Gamma=-2176.
\end{gathered}
\]
It also has the correct quadratic \(D\), the correct next bit \(E\), and the zero set
\[
\{0,e_0,\ldots,e_7,\mathbf1\},
\]
which satisfies all the zero moments and the new geometric restrictions.

Its failures are explicit:
\[
\widehat p(1)=-200,
\qquad
\operatorname{wt}(J_K)=140,\quad
\operatorname{wt}(J_L)=108.
\]
Thus Fourier realizability and the individual quadratic-residue requirements detect it. This fake proves only that the listed energy, mean and \(R\)-side geometric conditions remain insufficient; it does not satisfy the full Boolean system.