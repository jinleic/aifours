RESULT: PARTIAL

I do not obtain an optimal normal-subgroup lift or an all-word odd-dihedral proof. I give explicit obstructions to two proposed repairs, and prove the universal bounds
\[
z(G)\le
\begin{cases}
(n^2+1)/2,&n\text{ odd},\\[2mm]
n(n+1)/2,&n\text{ even}.
\end{cases}
\]
They improve \(n(n-1)+1\) strictly for every \(n\ge3\). Their novelty is **unknown**.

Throughout, a subword is a subsequence with increasing indices. Its product always uses that order.

**The lifting attempt and its exact missing correction.** Let \(H\triangleleft G\), with \(|H|=h\) and \([G:H]=m\). Assume the ordered EGZ property in both \(H\) and \(G/H\).

From a word of length \(2hm-1\), one can extract \(2h-1\) pairwise disjoint \(m\)-element index sets \(B_j\), each having quotient product \(1\). Indeed, before the last extraction there remain
\[
2hm-1-(2h-2)m=2m-1
\]
entries. Write
\[
b_j=\prod_{i\in B_j}^{\nearrow}a_i\in H.
\]
The hypothesis in \(H\) supplies \(j_1<\cdots<j_h\) with
\[
b_{j_1}\cdots b_{j_h}=1.
\]
This controls the product in the concatenated block order.

There is an exact description of the discrepancy when \(G\) has nilpotency class at most two. Use
\[
[x,y]=xyx^{-1}y^{-1}.
\]
For selected blocks, let \(L\) list their indices block by block, keeping increasing order inside each block. Define
\[
C(L)=
\prod_{\substack{u<v\\v\text{ precedes }u\text{ in }L}}
[a_v,a_u].
\]
All factors are central, so their order is immaterial. Adjacent swaps, using
\[
xy=[x,y]\,yx,
\]
give the exact identity
\[
\prod_{\text{block order}}a_i
=
\left(\prod_{\text{original order}}a_i\right)C(L).
\tag{1}
\]
Consequently, if the selected block products multiply to \(1\), their union has original-order product
\[
C(L)^{-1}.
\]
A valid correction argument must therefore force \(C(L)=1\) jointly with the \(H\)-EGZ selection. Centrality makes the correction computable; it does not make it vanish.

For odd dihedral groups, the same issue has an explicit affine form. Put
\[
D_{2d}=\langle r,s:r^d=s^2=1,\ srs=r^{-1}\rangle,
\qquad d\text{ odd},
\]
and write \(a_i=r^{x_i}s^{\varepsilon_i}\), with \(x_i\in\mathbb Z/d\mathbb Z\) and \(\varepsilon_i\in\{0,1\}\). For \(I=\{i_1<\cdots<i_{2d}\}\),
\[
\prod_{j=1}^{2d}a_{i_j}
=
r^{X(I)}s^{E(I)},
\]
where
\[
E(I)=\sum_j\varepsilon_{i_j}\pmod2,
\qquad
X(I)=
\sum_{j=1}^{2d}
(-1)^{\sum_{\ell<j}\varepsilon_{i_\ell}}x_{i_j}
\pmod d.
\tag{2}
\]
Thus the required all-word statement is:

For every choice of \(4d-1\) pairs \((x_i,\varepsilon_i)\), there is a \(2d\)-element set \(I\) satisfying \(E(I)=0\) and \(X(I)=0\).

The signs in \(X(I)\) depend on the selected reflections preceding each selected entry. They cannot be fixed from the original word before \(I\) is chosen. Applying ordinary cyclic EGZ to fixed signed exponents would leave precisely this gap. I do not prove the simultaneous conditions in (2).

**Explicit failures of strengthened lifting lemmas.**

First, optimal-budget extraction with separated supports is false even in \(S_3=D_6\). Let
\[
r^3=s^2=1,\qquad srs=r^{-1},\qquad H=\langle r\rangle,
\]
and take the length-\(11\) word
\[
(r,s,r,s,r,s,r,s,r,s,r).
\]
Here \(h=3,m=2\), so the proposed extraction needs five quotient-identity pairs with separated supports.

A quotient-identity pair must occupy two positions of the same parity. Its index interval therefore contains at least three positions. Separated supports give disjoint intervals, so at most
\[
\left\lfloor 11/3\right\rfloor=3
\]
such pairs exist. Five are impossible.

The word nevertheless has an ordered six-term identity subword: its six occurrences of \(r\), whose product is \(r^6=1\).

Second, abelian block products do not repair interleaving. In the same group, consider
\[
(a_1,\ldots,a_6)=(rs,s,rs,s,1,1).
\]
Choose
\[
B_1=\{1,3\},\qquad B_2=\{2,4\},\qquad B_3=\{5,6\}.
\]
Each block has length \(m=2\), and
\[
P(B_1)=(rs)^2=1,\qquad P(B_2)=s^2=1,\qquad P(B_3)=1.
\]
Their three products multiply to \(1\) in \(H\). Their union has the required target length \(hm=6\), but its original-order product is
\[
(rs)s(rs)s=r^2\ne1.
\]
In affine coordinates, the separate block sums are \(1-1=0\) and \(0-0=0\), while the union sum is \(1-0+1-0=2\).

Third, even central \(H\) does not suffice. Let
\[
G=D_8=\langle r,s:r^4=s^2=1,\ srs=r^{-1}\rangle,
\qquad H=\langle r^2\rangle=Z(G).
\]
Thus \(h=2,m=4\). Take
\[
(a_1,\ldots,a_8)=(r,s,r^{-1},s,1,1,1,1)
\]
and
\[
B_1=\{1,3,5,7\},\qquad B_2=\{2,4,6,8\}.
\]
Both length-four block products equal \(1\), whereas
\[
\prod_{i=1}^{8}a_i
=rsr^{-1}s=r^2\ne1.
\]
This is exactly a nontrivial central commutator correction.

These examples falsify proof lemmas. They do not falsify Olson’s conjecture, and they do not exclude a more carefully coupled extraction and selection.

**A universal bound.** A slightly stronger even-order statement is useful. If
\[
t=\bigl|\{g\in G:g^2=1\}\bigr|,
\]
including the identity, then
\[
z(G)\le
\begin{cases}
(n^2+1)/2,&n\text{ odd},\\[2mm]
\bigl(n(n+1)-t\bigr)/2+1,&n\text{ even}.
\end{cases}
\tag{3}
\]
For even \(n\), inverse pairing shows that \(t\) is even and at least two, giving the announced bound.

Here is a self-contained proof.

First we need the following cyclic fact:

> If \(C\) is cyclic of order \(d\), \(d\mid N\), then every word of length \(N+d-1\) in \(C\) has an ordered \(N\)-term identity subword.

For completeness, prove the prime-order EGZ theorem directly. Given \(a_1,\ldots,a_{2p-1}\in\mathbb F_p\), set
\[
F(X)=\sum_iX_i^{p-1},
\qquad
Q(X)=\sum_i a_iX_i^{p-1}.
\]
The number of common zeros is congruent modulo \(p\) to
\[
\sum_{X\in\mathbb F_p^{\,2p-1}}
(1-F(X)^{p-1})(1-Q(X)^{p-1}).
\]
Every monomial has degree at most
\[
2(p-1)^2<(2p-1)(p-1).
\]
A monomial can have nonzero sum over all \(X\) only if every variable has positive exponent divisible by \(p-1\), requiring degree at least \((2p-1)(p-1)\). Thus the displayed sum is zero modulo \(p\).

The zero vector is a common zero, so another common zero exists. Its support size is a positive multiple of \(p\), at most \(2p-1\), hence exactly \(p\). The corresponding \(p\) entries sum to zero.

Now induct on the cyclic order \(d\). Write \(d=ph\), with \(p\) prime. From \(2d-1\) entries in \(C_d\), extract \(2h-1\) disjoint \(p\)-term subsequences whose products lie in its subgroup \(C_h\), using the prime-order result in the quotient. Before the last extraction, \(2p-1\) entries remain. Induction in \(C_h\) selects \(h\) block products multiplying to \(1\).

All original entries lie in the same cyclic group. They commute, so the union of those selected blocks has original-order product \(1\) and length \(d\). This establishes cyclic EGZ.

Finally, from \(N+d-1\) entries extract \(N/d\) disjoint \(d\)-term identity subsequences. Before the last extraction, \(2d-1\) entries remain. Their union has product \(1\), again because all entries lie in \(C\). This proves the cyclic fact.

Now let \(W\) be any word in \(G\) containing no ordered \(n\)-term identity subword. Every individual group element occurs at most \(n-1\) times, since \(g^n=1\).

For \(g\) of order \(d>2\), let \(x,y\) count occurrences of \(g,g^{-1}\), and put
\[
\delta=\frac d{\gcd(d,2)}.
\]
If
\[
x+y\ge n+\delta-1,
\]
then, since \(x,y\le n-1\), the integer interval
\[
[n-y,x]
\]
contains at least \(\delta\) consecutive integers. It contains a multiple \(k\) of \(\delta\). Selecting \(k\) copies of \(g\) and \(n-k\) copies of \(g^{-1}\) gives product
\[
g^{2k-n}=1.
\]
Therefore
\[
x+y\le n+\delta-2.
\tag{4}
\]
In particular, the bounds for \(d=3,4,6\) are respectively
\[
n+1,\qquad n,\qquad n+1.
\tag{5}
\]

Partition the group into sets
\[
\Gamma(C)=\{g:\langle g\rangle=C\},
\]
one for each cyclic subgroup \(C\). These generator sets are disjoint even when the subgroups intersect.

If \(|C|=d\), then \(|\Gamma(C)|=\varphi(d)\). The cyclic fact bounds the number of entries from \(\Gamma(C)\) by
\[
n+d-2.
\]
Whenever \(\varphi(d)\ge4\),
\[
n+d-2\le2n-2
\le\frac{n-1}{2}\varphi(d).
\tag{6}
\]
For \(d>2\), the only cases with \(\varphi(d)=2\) are \(d=3,4,6\); these are covered by (5).

Suppose first that \(n\) is even. Write \(n=2k\), and let \(I=\{g:g^2=1\}\), of size \(t\ge2\). I claim that \(W\) contains at most \(kt\) entries from \(I\).

Indeed, suppose it contains at least \(kt+1\). Let \(v\) be the number of identity entries. If \(v\ge n\), we are done. Otherwise put
\[
e=2\lfloor v/2\rfloor,\qquad j=k-\lfloor v/2\rfloor.
\]
There are at least \(jt\) nonidentity involution entries, because
\[
kt+1-v-jt
=1-v+t\lfloor v/2\rfloor\ge0.
\]
Partition \(jt\) of them, in their induced order, into \(j\) successive windows of length \(t\). Each window uses only \(t-1\) possible symbols, so contains two equal involutions. Select such a pair from each window.

The pairs have separated supports and each pair multiplies to \(1\). Their union therefore has product \(1\). Adding \(e\) identity entries gives exactly
\[
2j+e=n
\]
entries, still with product \(1\). This proves the claim.

For every noninvolution generator class, (5)–(6) imply the uniform bound
\[
\#\{\text{entries from }\Gamma(C)\}
\le\frac{n+1}{2}|\Gamma(C)|.
\]
Consequently,
\[
|W|
\le\frac{nt}{2}+\frac{n+1}{2}(n-t)
=\frac{n(n+1)-t}{2}.
\]
This proves the even-order assertion in (3).

Suppose next that \(n\) is odd. The identity is the only involution. Let \(v\) count identity entries, and let \(c\) be the number of cyclic subgroups of order three. Then
\[
2c\le n-1.
\]

If \(v=0\), (6) bounds every generator class except order three at a rate of \((n-1)/2\) per group element. Each order-three class has two elements and, by (5), contributes at most \(n+1=(n-1)+2\). Hence
\[
|W|
\le\frac{(n-1)^2}{2}+2c
\le\frac{n^2-1}{2}.
\tag{7}
\]

If \(v\ge1\), an order-three generator class actually contributes at most \(n-1\). To check this, let \(g\) have order three, with multiplicities \(x,y\) for \(g,g^{-1}\). Suppose \(x+y\ge n\). According to \(x\bmod3\):

- If \(x\equiv0\), select \(x\) copies of \(g\) and \(n-x\) copies of \(g^{-1}\).
- If \(x\equiv1\), select \(x\) copies of \(g\), \(n-1-x\) copies of \(g^{-1}\), and one identity.
- If \(x\equiv2\), select \(x-1\) copies of \(g\), \(n-x\) copies of \(g^{-1}\), and one identity.

Each selection is available, has length \(n\), and has product \(1\). Thus \(x+y\le n-1\).

All nonidentity generator classes now satisfy the rate in (6). Since \(v\le n-1\),
\[
|W|
\le v+\frac{(n-1)^2}{2}
\le\frac{n^2-1}{2}.
\tag{8}
\]
Equations (7)–(8) prove the odd-order assertion in (3).

Every combination of factors in this proof occurs either inside one cyclic subgroup, or among identity pairs whose supports are separated. The global counting step does not multiply products from different generator classes.

Two small checks make the exceptional cases concrete. In \(C_3=\langle r\rangle\), the four-entry word
\[
(r,r,r^{-1},r^{-1})
\]
has no three-term identity subword: such a selection would require three copies of one symbol. The odd-order bound gives \(z(C_3)\le5\), so it is exact here. With an identity available, one copy each of \(1,r,r^{-1}\) already gives the required product.

For \(S_3\), \(n=6\) and \(t=4\). The involution argument bounds their total multiplicity by \(12\). The remaining generator class \(\{r,r^2\}\) has multiplicity at most \(7\): eight entries, with neither symbol occurring six times, give at least three copies of each, whose six-term product is \(1\). Thus every length-\(20\) word in \(S_3\) has an ordered six-term identity subword. This verifies the stronger bound (3) by hand; it does not reach the conjectured length \(11\).

The load-bearing unresolved step at \(2hm-1\) is to couple quotient-block extraction with the \(H\)-EGZ selection so that interleaving corrections vanish. In class two this means enforcing \(C(L)=1\) in addition to the identity among block products. In odd dihedral groups it means satisfying both conditions in (2), with signs determined by the selected subsequence itself. Neither abelianity of \(H\), centrality of \(H\), nor identity of every selected block product supplies that missing condition.