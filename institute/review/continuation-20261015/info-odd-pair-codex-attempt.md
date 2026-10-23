RESULT: PARTIAL

## Statements

I obtain further necessary conditions, including a substantial restriction on the balanced type \((4,128)\). I do not prove (P) impossible or exclude an entire listed type.

All matrices, polynomial coefficients, and set moments below are over \(\mathbb F_2\).

**1. A matrix identity for the zero set.** Use the canonical spectra from the supplied proofs, and set
\[
S=K_g+K_h,\qquad R=K_g-K_h,\qquad p=R/8.
\]
Let
\[
\mathcal Z=\{a:p(a)=0\},\qquad z=|\mathcal Z|,
\]
and let \(B\) be the polar matrix of \(D\). Then
\[
z\equiv0\pmod2,\qquad \bigoplus_{a\in\mathcal Z}a=0,
\tag{1}
\]
and
\[
\boxed{\quad
\sum_{a\in\mathcal Z}aa^{\mathsf T}=\mathcal C(B),\qquad
\mathcal C(B)_{ij}=
\begin{cases}
\operatorname{Pf}(B_{\widehat i\,\widehat j}),&i\ne j,\\
0,&i=j.
\end{cases}
\quad}
\tag{2}
\]
Here \(B_{\widehat i\,\widehat j}\) is the principal matrix obtained by deleting coordinates \(i,j\), and the Pfaffian is the sum of products over perfect matchings.

Consequently:

- If \(\operatorname{rank}B\le4\), a nonempty \(\mathcal Z\) has at least eight points; it cannot have ten points. If it has eight points, it is an affine three-dimensional subspace.
- If \(\operatorname{rank}B=6\), then \(z\ge4\); if additionally \(\mathrm{wt}(D)=128\), then \(z\ge8\).
- If \(\operatorname{rank}B=8\), then \(z\ge10\); if additionally \(\mathrm{wt}(D)=136\), then \(z\ge12\).

These statements hold under (P), with nonemptiness required only in the first bullet.

For a balanced nine-variable candidate, \(\mathcal Z\) is exactly its Walsh zero set, viewed in \(s^\perp\). Thus:

| Type of \(Q\) | Necessary number of Walsh zeros |
|---|---:|
| \((2,192)\) | at least \(8\) |
| \((4,128)\) | exactly \(8\), with the further restrictions below |
| \((4,160)\) | at least \(8\) |
| \((6,112)\) | at least \(4\) |
| \((6,128)\) | at least \(8\) |
| \((6,144)\) | at least \(4\) |
| \((8,120)\) | at least \(10\) |
| \((8,136)\) | at least \(12\) |

**2. The balanced type \((4,128)\) has only three possible absolute-value histograms.** Its Walsh zero set must be a **linear three-dimensional subspace of \(s^\perp\)**. On \(s^\perp\),
\[
\#\{W_f=0\}=8,\qquad
\#\{|W_f|=16\}=120,\qquad
\#\{|W_f|=24\}=128.
\tag{3}
\]
In particular, every frequency with \(Q=1\) has magnitude \(24\).

The complete spectrum must have one of these three histograms:

| Magnitude | Histogram I | Histogram II | Histogram III |
|---|---:|---:|---:|
| \(0\) | 8 | 8 | 8 |
| \(4\) | 2 | 4 | 1 |
| \(8\) | 0 | 0 | 0 |
| \(12\) | 0 | 0 | 3 |
| \(16\) | 120 | 120 | 120 |
| \(20\) | 108 | 104 | 105 |
| \(24\) | 128 | 128 | 128 |
| \(28\) | 146 | 148 | 147 |

**3. An explicit condition on the next residue bit.** Define
\[
E(a)=\frac{p(a)-D(a)}2\pmod2.
\]
Then
\[
\boxed{\quad
E(a)=
\sum_{|I|=4}\operatorname{Pf}(B_I)\prod_{i\in I}a_i
+P_3(a),\qquad \deg P_3\le3.
\quad}
\tag{4}
\]
Thus, once \(D\) is fixed, this residue bit lies in an explicit affine space with \(93\) binary parameters.

Equations (1), (2), and (4), together with the restrictions in (3), add location and residue information beyond the rank/weight inequality in `SHARPER.md`.

## Proofs

### 1. Fourier divisibility behind the zero identity

Write
\[
\widehat v(x)=\sum_{a\in\mathbb F_2^8}v(a)(-1)^{a\cdot x}.
\]
I use the reviewed canonical-sign facts in the supplied files:
\[
\widehat K_g,\widehat K_h\in\{-256,256\},\qquad
R\equiv8D\pmod{16}.
\]
Since \(R\) is divisible by \(8\) and \(|R|\le28\),
\[
p\in\{-3,-2,-1,0,1,2,3\},\qquad p\bmod2=D,
\]
and
\[
\widehat p\in\{-64,0,64\}.
\tag{5}
\]

Put \(e=\widehat p/64\), so \(e\in\{-1,0,1\}\). Fourier inversion gives
\[
\sum_x e(x)=4p(0).
\]
Therefore \(\sum e(x)^2\) is even, since \(e^2\equiv e\pmod2\).

The Fourier product formula gives
\[
\widehat{p^2}(b)
=16\sum_x e(x)e(x+b).
\]
For \(b\ne0\), the summands pair under \(x\leftrightarrow x+b\), so their sum is even. For \(b=0\), evenness was just established. Hence
\[
\boxed{\widehat{p^2}(b)\equiv0\pmod{32}\quad\text{for every }b.}
\tag{6}
\]

Let \(Z=1_{\{p=0\}}\) and \(L=1_{\{|p|=1\}}\). Checking the seven permitted values of \(p\) proves the exact identity
\[
p^2=4+5D-4Z-8L.
\tag{7}
\]
Indeed, its values are \(0,4,1,9\) respectively when \(p=0,\ p=\pm2,\ p=\pm1,\ p=\pm3\).

For a coordinate subset \(T\), mixed differences of a character transform satisfy
\[
\Delta_T\widehat v(0)
=(-2)^{|T|}
\sum_{a:\,a_i=1\ (i\in T)}v(a).
\tag{8}
\]
This follows by expanding each factor \((-1)^{a_i}-1=-2a_i\).

Combining (6) and (8), for \(|T|\le2\), the corresponding moment of \(p^2\) is divisible by \(2^{5-|T|}\), hence by \(8\). Equation (7) therefore gives
\[
4\sum_{a:\,a_T=1} Z(a)
\equiv
5\sum_{a:\,a_T=1}D(a)\pmod8.
\tag{9}
\]

A quadratic on \(m\) variables with polar rank \(2t\) has weight
\[
2^{m-1},\quad\text{or}\quad 2^{m-1}\pm2^{m-t-1}.
\tag{10}
\]
To obtain this, choose a symplectic basis. A nonzero linear term on the radical cancels the sign sum; otherwise each nondegenerate pair contributes a sign sum of magnitude \(2\), and each radical coordinate contributes \(2\).

For \(m=8\) or \(7\), every weight in (10) is divisible by \(8\). Thus (9), with \(|T|=0,1\), proves (1).

For \(|T|=2\), the restricted quadratic has six variables. Its weight is \(4\bmod8\) exactly when its polar matrix is nonsingular: the full-rank weights are \(28,36\), while all lower-rank weights are divisible by \(8\). Thus
\[
\sum_a a_i a_j Z(a)
=\operatorname{Pf}(B_{\widehat i\,\widehat j}).
\]
For an alternating matrix, its determinant is the square of its Pfaffian: in the determinant expansion, permutations containing a cycle of length at least three cancel with their reversed cycles, leaving the perfect matchings. Over \(\mathbb F_2\), nonsingularity therefore equals Pfaffian \(1\).

The diagonal entries are zero by (1). This proves (2).

### 2. Consequences of the matrix identity

Choose linear coordinates putting
\[
B=\operatorname{diag}(\underbrace{J,\ldots,J}_{r},0),
\qquad
J=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
Inspection of its six-coordinate principal Pfaffians gives
\[
\operatorname{rank}\mathcal C(B)=
\begin{cases}
0,&\operatorname{rank}B\le4,\\
2,&\operatorname{rank}B=6,\\
8,&\operatorname{rank}B=8.
\end{cases}
\tag{11}
\]
In rank six, \(\operatorname{im}\mathcal C(B)=\operatorname{rad}B\). In rank eight,
\[
\mathcal C(B)=B^{-1}.
\tag{12}
\]
These assertions persist under a change of coordinates: the polar matrix transforms by congruence, while the point-moment matrix transforms by the inverse congruence.

Here are the required elementary facts about finite sets.

**Rank bound.** Suppose \(X\ne\varnothing\) has even size \(z\) and XOR zero. Let \(A\) have its points as columns. Then
\[
\operatorname{rank}(AA^{\mathsf T})\le z-2.
\tag{13}
\]
Indeed, \(A\mathbf1=0\), and \(\operatorname{im}A^{\mathsf T}\subseteq\mathbf1^\perp\). The restriction of \(A\) to \(\mathbf1^\perp\) has \(\mathbf1\) in its kernel, because \(z\) is even. Its rank is at most \(z-2\).

**Zero moment matrix.** If also \(AA^{\mathsf T}=0\), append an all-one row to \(A\). The resulting row space is self-orthogonal, so its dimension is at most \(z/2\). That dimension is \(1+\dim\operatorname{aff}(X)\). Consequently
\[
|X|\le2^{z/2-1}.
\]
This excludes \(z=2,4,6\). For \(z=8\), it forces affine dimension three, so \(X\) is the whole affine three-flat.

It also excludes \(z=10\). Such a set would span an affine four-flat \(F\). The full \(F\) has all moments of degrees zero, one, and two equal to zero: after parametrization these are polynomials of degree at most two on four variables, each having even sum. Hence \(F\setminus X\), of size six, would also have zero moments through degree two, contradicting the preceding bound.

**Six points.** Any six distinct points with XOR zero have moment-matrix rank four. Translate one point to zero; translation preserves the moment matrix by evenness and XOR zero. The other five points sum to zero. They span dimension four: dimension at most three would put the six points inside an eight-point three-flat whose two-point complement would have XOR zero, which is impossible. In suitable coordinates the set is therefore
\[
\{0,e_1,e_2,e_3,e_4,e_1+e_2+e_3+e_4\}.
\]
Its moment matrix is \(I_4+\mathbf1\mathbf1^{\mathsf T}\), which is invertible because its square is \(I_4\).

Now apply these facts to \(\mathcal Z\).

- Rank at most four gives the first bullet of Statement 1.
- Rank six gives \(z\ge4\) by (11), (13). Six zeros are impossible by the six-point fact. If \(z=4\), XOR zero makes \(\mathcal Z\) an affine two-flat. Its moment-matrix image is its direction space, so (11) makes that direction space \(\operatorname{rad}B\). Since \(D=0\) throughout \(\mathcal Z\), \(D\) has zero linear part on its radical. Formula (10) then excludes weight \(128\). Thus rank six, weight \(128\), requires \(z\ge8\).
- Rank eight gives \(z\ge10\). Suppose \(z=10\). Translate a zero to the origin. By (12), the remaining nine points span dimension eight and sum to zero. They can therefore be written
  \[
  e_1,\ldots,e_8,\mathbf1.
  \]
  Their moment matrix is \(I_8+\mathbf1\mathbf1^{\mathsf T}\), whose inverse is itself. Thus the polar matrix of the translated \(D\) has every off-diagonal entry one. Since \(D\) vanishes at \(0,e_1,\ldots,e_8\), its constant and linear terms vanish:
  \[
  D(a)=\sum_{i<j}a_i a_j.
  \]
  This is one exactly at Hamming weights \(2,3,6,7\), giving weight
  \[
  \binom82+\binom83+\binom86+\binom87=28+56+28+8=120.
  \]
  Weight \(136\) therefore requires \(z\ge12\).

This proves all zero-count bounds.

### 3. Proof of the next-bit condition

For \(|T|\le4\), equations (5), (8) show that the corresponding moment of \(p\) is divisible by \(4\). Writing \(p=D+2e_0\), where \(e_0\bmod2=E\), gives
\[
\sum_{a:\,a_T=1}E(a)
\equiv
\frac12\sum_{a:\,a_T=1}D(a)\pmod2.
\tag{14}
\]

If \(|T|\le3\), the restricted quadratic has at least five variables, so (10) makes its weight divisible by four. The right side is zero.

If \(|T|=4\), the restricted quadratic has four variables. Half its weight is odd exactly when its polar rank is four. Hence the right side is
\[
\operatorname{Pf}(B_{T^c}).
\]

For an ANF \(E=\sum_I c_I a_I\),
\[
\sum_{a:\,a_T=1}E(a)=\sum_{I\supseteq T^c}c_I\pmod2.
\]
Descending through \(|I|=8,7,6,5\), the vanishing moments for \(|T|\le3\) force those coefficients to vanish. The moments for \(|T|=4\) then give
\[
c_I=\operatorname{Pf}(B_I)\qquad(|I|=4).
\]
This proves (4). The remaining coefficients number
\[
1+8+\binom82+\binom83=93.
\]

### 4. Identification with the balanced spectrum

For the split used in `PROOF.md`, the two halves have equal support XOR and opposite canonical phases. Thus, for some affine sign character \(\eta(a)\),
\[
R(a)=\eta(a)W_f(a),\qquad
S(a)=\eta(a)W_f(a+u),
\tag{15}
\]
where \(a\in s^\perp\) and \(u\cdot s=1\).

Therefore \(\mathcal Z\) is the Walsh zero set on \(s^\perp\). There are no zeros outside \(s^\perp\), because those Walsh values are \(4\bmod8\). Balance puts \(0\in\mathcal Z\). An eight-point affine three-flat \(\mathcal Z\) is consequently linear.

### 5. Exact slack accounting

Define
\[
a=\#\{|S|\in\{4,12\}\},\qquad
c=\#\{|R|=8\},\qquad
z=\#\{R=0\},
\]
and write
\[
\Gamma=\sum_a(-1)^{D(a)}S(a).
\]
Put \(T=(-1)^D S\), as in `SHARPER.md`. Its four values give the exact identity
\[
T^2+8T=560-512\,1_{\{|S|\in\{4,12\}\}}.
\]
Similarly, checking the possible values of \(R\) gives
\[
R^2=256+320D-256\,1_{\{R=0\}}-512\,1_{\{|R|=8\}}.
\]
Summing and using \(\sum(S^2+R^2)=262144\) yields
\[
\boxed{\Gamma=40d-6656-64(a+c)-32z.}
\tag{16}
\]

Now assume \(D\) has rank four and weight \(128\), and \(\mathcal Z\ne\varnothing\). The reviewed correlation bound is \(\Gamma\ge-2048\), so
\[
z+2(a+c)\le16.
\tag{17}
\]
The zero-set result gives
\[
z\in\{8,12,14,16\}.
\]

Equation (6) at zero, together with (7), gives
\[
z+2c\equiv0\pmod8.
\tag{18}
\]
Also \(\Gamma\) is a multiple of \(128\): its Fourier expression consists of products of \(0,\pm512\) with \(0,\pm64\), divided by \(256\). Equation (16) therefore gives
\[
z+2(a+c)\equiv0\pmod4.
\tag{19}
\]

The cases in (17)–(19) are exactly
\[
(z,c,a)=
(8,0,0),(8,0,2),(8,0,4),(8,4,0),
(12,2,0),(14,1,0),(16,0,0).
\tag{20}
\]
For completeness: when \(z=8\), \(c=0\) or \(4\), and \(a+c\le4\) is even; when \(z=12,14,16\), the possibilities are respectively \((c,a)=(2,0),(1,0),(0,0)\).

The last four cases have \(a=0,\Gamma=-2048\). But \(a=0\) means every \(T\) is \(-28\) or \(20\), so
\[
\Gamma=-7168+48n.
\]
The equation \(-2048=-7168+48n\) would give \(48n=5120\), impossible.

It remains to exclude \((8,0,0)\). Here \(\Gamma=-1792\). Let \(n_0,n_1\) count \(T=20\) on \(D=0,D=1\). Since both level sets have size \(128\),
\[
\sum S=48(n_0-n_1).
\]
But \(\sum S\in\{-512,0,512\}\), so \(\sum S=0\). Consequently \(\sum R=\pm512\).

Pointwise, \(SR\equiv2R\pmod3\): on \(D=0\), \(S\in\{-28,20\}\), both \(2\bmod3\); on \(D=1\), \(c=0\) gives \(R=\pm24\). However,
\[
\sum SR=\sum K_g^2-\sum K_h^2=0.
\]
It follows that \(\sum R\equiv0\pmod3\), contradicting \(\sum R=\pm512\).

Thus
\[
\boxed{z=8,\qquad c=0,\qquad a\in\{2,4\}.}
\tag{21}
\]
This proves (3) and the linear three-flat assertion.

Finally, let \(N_j\) count off-\(s^\perp\) magnitudes \(j\). Their energy is
\[
262144-(120\cdot256+128\cdot576)=157696.
\]
Using \(N_4+N_{12}=a\) and \(N_{20}+N_{28}=256-a\), this becomes
\[
3N_{28}+N_{12}=432+3a.
\]
For \(a=2\), necessarily \(N_{12}=0\). For \(a=4\), necessarily \(N_{12}=0\) or \(3\). These give exactly the three displayed histograms.

## Gaps

**GAP toward (1):** none of the arguments proves (P) impossible.

**GAP toward (2):** no entire surviving rank/weight type is excluded. In particular, I have not excluded signed Boolean realizations of the three remaining \((4,128)\) histograms.

The zero identities and next-bit condition are necessary conditions. Their sufficiency is not claimed.

## Suggested audits

1. **Audit the general identities independently of (P).** Enumerate
   \[
   e\in\{-1,0,1\}^{256},\qquad p=\widehat e/4,
   \]
   retaining integral vectors with \(|p|\le3\) and quadratic \(D=p\bmod2\). These are exactly the vectors satisfying (5). Check:
   - \(\widehat{p^2}\equiv0\pmod{32}\);
   - equations (1), (2), and (4);
   - all stated zero-count bounds and equality cases.

   Any retained counterexample falsifies the corresponding claimed lemma.

2. **Audit the \((4,128)\) arithmetic.** Enumerate the 28 ordered canonical pairs
   \[
   (k,\ell)\in\{-22,-14,-6,2,10,18,26\}^2,\qquad |k|+|\ell|\le28.
   \]
   Check both exact slack identities pointwise. Enumerate the integer triples satisfying (17)–(19), verify list (20), and check the two subsequent contradictions.

3. **Audit candidate balanced spectra.** For rank four, weight \(128\), check that the zero set is a three-dimensional linear subspace contained in \(Q^{-1}(0)\), and that the absolute-value histogram is one of the three displayed rows. Any actual candidate failing either check falsifies Statement 2.

4. **Audit the residue lift efficiently.** Given \(D\), compute its \(70\) principal four-coordinate Pfaffians. For a proposed \(p\), compute the ANF of \((p-D)/2\bmod2\); its terms above degree four must vanish, and its quartic coefficients must equal those Pfaffians.

I ran 300 deterministic exact controls satisfying (5) and \(|p|\le3\), covering polar ranks \(2,4,6,8\). All passed the quartic, zero-moment, and refined zero-count checks. I also checked the three histogram energies exactly. These controls support the arithmetic; the proofs above establish the universal claims. No files were modified.

## Why other routes fail

The scalar correlation and moment constraints still admit explicit integer fake spectra. Here is one with genuinely quadratic residue functions.

Index frequencies by integers \(0,\ldots,255\), with coordinates \(a_0,\ldots,a_7\), and put
\[
D=a_0a_1+a_2a_3+a_4.
\]
For an integer mask \(m\), write \(a_m=\prod_{i:\,m_i=1}a_i\), with \(a_0=1\) when the subscript denotes the zero mask. Define
\[
J_g=\sum_{m\in M}a_m,\qquad J_h=J_g+D,
\]
where
\[
M=\{0,4,5,12,17,20,24,32,40,64,65,72,96,128,129,160,192\}.
\]
Both quadratics have rank six and weight \(144\); their joint cell sizes are
\[
(N_{00},N_{01},N_{10},N_{11})=(48,64,64,80).
\]

Construct integer vectors \(K,L\) using this table. Process rows in the displayed order, assigning each row to the smallest unused indices in its required \((J_g,J_h)\) cell.

| \(K\) | \(L\) | Count |
|---:|---:|---:|
| \(-22\) | \(-6\) | 40 |
| \(-22\) | \(2\) | 29 |
| \(-14\) | \(-14\) | 1 |
| \(-14\) | \(10\) | 1 |
| \(-6\) | \(-22\) | 32 |
| \(-6\) | \(10\) | 1 |
| \(2\) | \(-22\) | 25 |
| \(2\) | \(18\) | 29 |
| \(2\) | \(26\) | 38 |
| \(10\) | \(10\) | 7 |
| \(18\) | \(2\) | 18 |
| \(26\) | \(2\) | 35 |

The required cell is obtained directly from \((k^2-4)/32\bmod2\). The table exhausts precisely the four cell sizes above, so this defines all 256 entries.

Direct finite arithmetic gives
\[
\begin{gathered}
|K|+|L|\le28,\qquad
\sum K=-256,\quad\sum L=256,\\
\sum K^2=\sum L^2=65536,\qquad
\sum SR=0,\\
\sum S^2=154\cdot1024,\qquad
\sum R^2=102\cdot1024,\\
\Gamma=-1920,\qquad
\sum(-1)^D R=-128,\qquad
(z,c,a)=(8,0,2).
\end{gathered}
\]
Its scalar correlations are
\[
\begin{array}{c|rr}
 &K&L\\ \hline
(-1)^{J_g}&1216&1728\\
(-1)^{J_h}&1536&1088\\
(-1)^D&-1024&-896
\end{array}
\]
and satisfy the corresponding quadratic correlation bounds. Thus cap, energies, canonical means, quadratic residues, and these scalar correlation bounds do not alone eliminate this type.

For reproducibility, the polar-matrix rows of \(J_g,J_h\), encoded as eight-bit integers, are respectively
\[
(212,0,25,116,13,200,169,97),\qquad
(214,1,17,112,13,200,169,97).
\]
Binary row reduction gives rank six. Evaluating their explicit ANFs gives the joint cell counts above; every remaining numerical assertion follows by summing the twelve table rows.

Nevertheless, its \(R\)-zero locations are
\[
\{4,233,234,247,251,252,253,254\},
\]
whose XOR is \(244\ne0\). It therefore fails (1). It is an integer fake, not a Boolean Walsh pair.

This example identifies the limitation of count arguments precisely: they discard the spatial Fourier constraints. The additional zero identity detects information that those scalar constraints miss. Whether the strengthened conditions suffice to exclude any whole remaining type is unresolved here.