# Actual second arm: complete grade-two contraction and radical equality, plus an all-grade boundary family

**Materialization target:** `f487-kac-second-arm-low-grades-actual-module-contraction-frontier/author-candidate-v1.md`

**Status: AUTHOR CANDIDATE — NOT INDEPENDENTLY REVIEWED. Scientific execution: NOTRUN.**

## 1. Results and exact scope

Use the displayed full-Cartan presentation
\[
A(r,s)=
\begin{pmatrix}
2&-1&-1\\
-1&2&-1\\
-r&-s&2
\end{pmatrix},
\qquad
S=G_{\mathcal C}/J,
\]
where \(J\) contains **all positive and negative Serre relations**, and
\[
r\in\{1,2,3\},\qquad s>r.
\]

Write \(E_i=\operatorname{ad}e_i\), \(F_i=\operatorname{ad}f_i\).

This candidate supplies two actual-component results.

### Theorem A — Complete second-arm grade \(n=2\)

For every allowed parameter pair and every \(a\ge0\), the **full normalized contraction** on the actual component
\[
S_{(a,2,2)}
\]
is invertible.

Set
\[
\lambda_0=5(r+s)-4,\qquad
\lambda_r=4(r-1),\qquad
\lambda_s=4(s-1).
\]

The complete component dimensions and determinants are:

| Parameters | Horizontal degree | Actual dimension | Determinant |
|---|---:|---:|---:|
| \(r=1\) | \(a=1,3\) | \(2\) | \(\lambda_0\lambda_s\) |
| \(r=1\) | \(a=2\) | \(3\) | \(\lambda_0^2\lambda_s\) |
| \(r=2,3\) | \(a=1,3\) | \(3\) | \(\lambda_0\lambda_r\lambda_s\) |
| \(r=2,3\) | \(a=2\) | \(4\) | \(\lambda_0^2\lambda_r\lambda_s\) |
| All allowed parameters | Other \(a\) | \(0\) | \(1\), empty determinant |

All displayed nonempty determinants are strictly positive.

Consequently, for the entire second-arm grade,
\[
\det\!\left(\overline A_2\bigm|
\bigoplus_aS_{(a,2,2)}\right)
=
\begin{cases}
\lambda_0^4\lambda_s^3,&r=1,\\
\lambda_0^4\lambda_r^3\lambda_s^3,&r=2,3.
\end{cases}
\]

A **separate ideal argument**, not contraction invertibility, proves
\[
\boxed{J_{(a,2,2)}=\tau_{(a,2,2)}\qquad(a\ge0).}
\]

In fact, the proof establishes contraction invertibility and radical equality on the entire actual third-grade-two space
\[
\mathcal L_2=\bigoplus_{a,b\ge0}S_{(a,b,2)}.
\]
The second-arm statements above are its complete \(b=2\) restriction.

### Theorem B — Complete \(a=0,\ b=2\) boundary, all grades

For every allowed parameter pair and every \(n\ge0\),
\[
\boxed{J_{(0,2,n)}=\tau_{(0,2,n)}.}
\]

Its actual component dimensions are
\[
\boxed{
\dim S_{(0,2,n)}
=
\#\{k:\ k\text{ odd},\ 3\le k\le s,\ k\le n\le2s-k\}.
}
\]

Equivalently,
\[
\dim S_{(0,2,n)}
=
\max\!\left(
0,\left\lfloor
\frac{\min(s,n,2s-n)-1}{2}
\right\rfloor
\right).
\]

This is an entire actual-component family, not a formal exterior vector or selected-seed assertion. It is nonempty for every \(s\ge3\). **No contraction-invertibility conclusion for its grades \(n\ge3\) is asserted.**

Theorem A resolves the whole previously unpaid grade \(n=2\), including genuine \(a=b=2\) components. Theorem B adds radical equality on the stated all-grade boundary without substituting that boundary for the remaining interior problem.

---

## 2. Retained interfaces

The following remain explicit imports from the frozen packet:

1. **f276:** full-Cartan injection, the actual positive free-source presentation, and the whole-Serre-ideal bridge excluding additional positive relations arising from negative Serres.
2. **f306:** the normalized eight-letter coevaluation, actual theta-duals, full inverse Gram matrix, and consuming bracket.
3. **f314:** used only for the conditional projected-seed consequence stated in §7.
4. The adopted first-arm result
   \[
   M=\bigoplus_{a,n\ge0}S_{(a,1,n)}
   =L_{\mathrm{low}}^{(13)}(1,s),
   \qquad
   (\tau/J)\cap M=0.
   \]
5. The adopted complete actual second-arm presentation
   \[
   N=\bigoplus_{a,n\ge0}S_{(a,2,n)}
   =
   \frac{\Lambda^2M}
   {U(\mathfrak g_{13})(v\wedge E_1v)
   \oplus U(\mathfrak g_{13})(v\wedge E_3v)},
   \qquad v=e_2.
   \]

No positive form on the ambient nonsymmetrizable algebra is assumed. No held candidate or held consumer is an input.

---

## 3. Actual whole level two via the finite Levi on nodes \(1,2\)

The finite Levi
\[
\mathfrak l=\mathfrak g_{12}\cong\mathfrak{sl}_3
\]
is useful here because its grading complement is exactly the third coordinate \(n\).

Let
\[
V=\bigoplus_{a,b\ge0}S_{(a,b,1)}.
\]

The vector \(u_0=e_3\) is \(\mathfrak l\)-lowest with labels \((1,1)\). The complete linearized positive presentation imposes
\[
E_1^2u_0=E_2^2u_0=0.
\]
The finite-type lowest-weight presentation therefore gives
\[
V=L_{\mathrm{low}}^{(12)}(1,1),
\qquad \dim V=8.
\]

This is an **actual** module statement at the f276 interface. The injection of \(\mathfrak l\) follows because its Cartan survives and a nonzero homomorphism from the simple algebra \(\mathfrak{sl}_3\) is injective.

Use precisely the frozen eight letters
\[
\begin{aligned}
u_0&=e_3,&u_1&=E_1e_3,&u_2&=E_2e_3,\\
u_3&=E_1E_2e_3,&u_4&=E_2E_1e_3,\\
u_5&=-\tfrac12E_1^2E_2e_3,&
u_6&=\tfrac12E_2^2E_1e_3,&u_7&=E_1u_6.
\end{aligned}
\]

Before the repeated-node-\(3\) Serres, free-Lie degree two is \(\Lambda^2V\). The repeated-node-\(3\) Serres have third degrees \(r+1\) and \(s+1\).

Because \(s>r\):

- when \(r=1\), precisely one such relation begins in third degree two;
- when \(r=2,3\), neither begins there.

At degree two, only their complete \(\mathfrak l\)-positive closures can contribute. Bracketing with positive third degree increases the grade. Exclusion of additional positive consequences of the negative ideal remains **f276**, not this grading observation alone.

### 3.1 Complete decomposition of \(\Lambda^2V\)

In \(\Lambda^2V\), with brackets denoting exterior classes before quotienting, set
\[
q_r=[u_0,u_1],\qquad q_s=[u_0,u_2],
\]
and
\[
A=[u_0,u_3],\qquad
B=[u_0,u_4],\qquad
C=[u_1,u_2],\qquad
y=A-B-C.
\]

The relevant lowering actions on \(V\) are
\[
\begin{array}{c|cccc}
 &u_1&u_2&u_3&u_4\\ \hline
F_1&u_0&0&2u_2&u_2\\
F_2&0&u_0&u_1&2u_1.
\end{array}
\]

Thus \(q_r,q_s,y\) are killed by both \(F_1,F_2\). Their degrees and lowest labels are
\[
\begin{array}{c|c|c}
\text{vector}&(a,b,n)&\text{lowest labels}\\ \hline
q_r&(1,0,2)&(0,3)\\
q_s&(0,1,2)&(3,0)\\
y&(1,1,2)&(1,1).
\end{array}
\]

Each is nonzero in the exterior source. In particular, the three exterior pairs defining \(y\) are independent.

Finite complete reducibility gives three distinct irreducible summands, of dimensions \(10,10,8\). Their dimensions sum to
\[
10+10+8=28=\dim\Lambda^2V.
\]
Therefore they exhaust the source:
\[
\Lambda^2V
=
L_{\mathrm{low}}(0,3)
\oplus L_{\mathrm{low}}(3,0)
\oplus L_{\mathrm{low}}(1,1).
\]

For \(r=1\), the degree-two Serre is
\[
E_3^2e_1=-q_r,
\]
so its **whole** relation module is exactly the first ten-dimensional summand. It is not a rank-only subtraction.

Hence the actual entire third-grade-two module is
\[
\boxed{
\mathcal L_2=
\begin{cases}
L_{\mathrm{low}}(3,0)\oplus L_{\mathrm{low}}(1,1),
&r=1,\\[2mm]
L_{\mathrm{low}}(0,3)\oplus L_{\mathrm{low}}(3,0)
\oplus L_{\mathrm{low}}(1,1),
&r=2,3.
\end{cases}
}
\]

This supplies actual source and relation closure for every component used below.

---

## 4. Full contraction: all eight channels retained

Write
\[
f=F_3,\qquad g=F_1,\qquad R=F_2.
\]

The frozen actual dual operators are
\[
\begin{aligned}
W_0&=f,&W_1&=[f,g],&W_2&=[f,R],\\
W_3&=[W_2,g],&W_4&=[W_1,R],\\
W_5&=-\tfrac12[W_3,g],&
W_6&=\tfrac12[W_4,R],&
W_7&=[W_6,g].
\end{aligned}
\]

The full operator is
\[
\begin{aligned}
\overline A_2={}&
\operatorname{ad}(u_0)W_0+
\operatorname{ad}(u_1)W_1+
\operatorname{ad}(u_2)W_2\\
&+\frac13\left[
\operatorname{ad}(u_3)(2W_3-W_4)
+\operatorname{ad}(u_4)(-W_3+2W_4)
\right]\\
&+\operatorname{ad}(u_5)W_5+
\operatorname{ad}(u_6)W_6+
\operatorname{ad}(u_7)W_7.
\end{aligned}
\]

None of the last three channels is discarded on the entire module.

### 4.1 Why checking three lowest vectors covers every consumer

As finite \(\mathfrak l\)-modules, \(V\) and its negative counterpart are dual. The canonical coevaluation uses the inverse of the contravariant Gram matrix whose only nontrivial block is
\[
G_{\{3,4\}}=
\begin{pmatrix}2&1\\1&2\end{pmatrix},
\qquad
G_{\{3,4\}}^{-1}
=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix};
\]
the other normalized diagonal entries are \(1\).

Thus the **complete** tensor appearing in the displayed contraction is \(\mathfrak l\)-invariant. Its consuming bracket is \(\mathfrak l\)-equivariant by Jacobi. Therefore
\[
[\overline A_2,E_i]=[\overline A_2,F_i]=0
\qquad(i=1,2).
\]

This is the f306 equivariant-coevaluation interface with the exact displayed normalization. It is not an assertion that \(F_3\) is an adjoint for a positive ambient form.

For an elementary check of the normalization, the positive actions on the eight-letter source are
\[
\begin{array}{c|rrrrrrrr}
 &u_0&u_1&u_2&u_3&u_4&u_5&u_6&u_7\\ \hline
E_1&u_1&0&u_3&-2u_5&-u_5&0&u_7&0\\
E_2&u_2&u_4&0&u_6&2u_6&-u_7&0&0.
\end{array}
\]
Together with the dual action, these give cancellation in the entire coevaluation tensor, including the \(u_5,u_6,u_7\) terms.

Because the three source summands are pairwise nonisomorphic and multiplicity one, equivariance makes \(\overline A_2\) scalar on each. It remains to determine those scalars.

### 4.2 Scalars on the two ten-dimensional summands

Direct Chevalley calculation gives
\[
F_3q_r=2(r-1)u_1,\qquad
F_3q_s=2(s-1)u_2.
\]

On \(q_r\), only \(W_0,W_1\) can have nonzero final targets:
\[
W_1q_r=-2(r-1)u_0.
\]
Consequently
\[
\overline A_2q_r
=2(r-1)[u_0,u_1]-2(r-1)[u_1,u_0]
=4(r-1)q_r.
\]

Similarly,
\[
\overline A_2q_s=4(s-1)q_s.
\]

For \(r=1\), the first scalar is zero **on precisely the whole relation summand that is removed**. No surviving actual summand is silently assigned this zero eigenvalue.

### 4.3 Scalar on the eight-dimensional summand

The actual \(F_3\)-actions needed are
\[
\begin{aligned}
F_3u_0&=-h_3,&F_3u_1&=-re_1,&F_3u_2&=-se_2,\\
F_3u_3&=-s[e_1,e_2],&
F_3u_4&=r[e_1,e_2].
\end{aligned}
\]

It follows that
\[
F_3y=p\,u_3+q\,u_4,
\]
where
\[
p=3r+2s-2,\qquad q=-(2r+3s-2).
\]

Set
\[
c=4r+s-2,\qquad d=2-r-4s.
\]
Since \(F_1y=F_2y=0\),
\[
W_1y=-c\,u_2,\qquad
W_2y=-d\,u_1,\qquad
W_3y=d\,u_0,\qquad
W_4y=c\,u_0.
\]

On this particular lowest vector, the final targets of \(W_5,W_6,W_7\) have a negative horizontal coordinate, so those three values are zero. This does **not** remove those channels on its raised vectors; their propagation is already covered by exact full-operator equivariance.

Substituting all remaining terms gives
\[
\begin{aligned}
\overline A_2y
={}&pA+qB+(d-c)C
-\frac{2d-c}{3}A
-\frac{-d+2c}{3}B.
\end{aligned}
\]

The coefficients simplify to
\[
p-\frac{2d-c}{3}=5(r+s)-4,
\]
\[
q-\frac{-d+2c}{3}=-\bigl(5(r+s)-4\bigr),
\]
and
\[
d-c=-\bigl(5(r+s)-4\bigr).
\]
Therefore
\[
\boxed{\overline A_2y=\bigl(5(r+s)-4\bigr)y.}
\]

The full actual spectrum is consequently
\[
\boxed{
\begin{array}{c|c|c}
\text{summand}&\text{dimension}&\overline A_2\\ \hline
L_{\mathrm{low}}(0,3)&10&4(r-1)I\quad\text{(absent if }r=1),\\
L_{\mathrm{low}}(3,0)&10&4(s-1)I,\\
L_{\mathrm{low}}(1,1)&8&(5(r+s)-4)I.
\end{array}
}
\]

All surviving eigenvalues are positive. A compact positive form may be chosen on this finite \(\mathfrak l\)-module, so the actual operator is positive definite there. This introduces no positive-form assertion about the ambient algebra.

### 4.4 Complete \(b=2\) restriction

On the complete \(b=2\) slice:

- each ten-dimensional summand contributes one node-\(1\) module \(V_2\), supported at \(a=1,2,3\);
- the eight-dimensional summand contributes \(V_2\oplus V_0\), with the additional \(V_0\) at \(a=2\).

Thus
\[
\bigoplus_aS_{(a,2,2)}
\cong
\begin{cases}
2V_2\oplus V_0,&r=1,\\
3V_2\oplus V_0,&r=2,3.
\end{cases}
\]

This proves every dimension, eigenvalue multiplicity and determinant in Theorem A, including all zero components.

---

## 5. Separate radical equality for the entire actual level two

Let
\[
\mathcal R=\tau/J.
\]
At f276, this is a Cartan-disjoint ideal of \(S\).

First,
\[
\mathcal R\cap V=0.
\]
Indeed, the intersection is a submodule of the irreducible finite \(\mathfrak l\)-module \(V\). If it were all of \(V\), it would contain \(e_3\), and ideal stability would give
\[
[f_3,e_3]=-h_3\in\mathcal R,
\]
contradicting full-Cartan injection and Cartan-disjointness.

Now \(\mathcal L_2\) is a multiplicity-free sum of the distinct irreducibles in §3. Therefore \(\mathcal R\cap\mathcal L_2\) is a sum of some of those irreducibles.

None can occur:

- If \(r\ge2\), the \(q_r\)-summand cannot occur because
  \[
  F_3q_r=2(r-1)u_1\ne0
  \]
  lies in \(V\).
- The \(q_s\)-summand cannot occur because
  \[
  F_3q_s=2(s-1)u_2\ne0.
  \]
- The \(y\)-summand cannot occur because
  \[
  F_3y=(3r+2s-2)u_3-(2r+3s-2)u_4\ne0.
  \]
  The vectors \(u_3,u_4\) are independent in the actual level-one module.

Each proposed occurrence would place a nonzero vector in \(\mathcal R\cap V\), a contradiction. Hence
\[
\boxed{\mathcal R\cap\mathcal L_2=0.}
\]

In particular,
\[
\boxed{J_{(a,2,2)}=\tau_{(a,2,2)}\qquad(a\ge0).}
\]

This proof does not use contraction positivity, determinant calculations, f306, or f314. It does retain the actual-source and Cartan-disjoint-ideal f276 interface.

---

## 6. Complete all-grade boundary radical theorem

This section uses the adopted actual \(\mathfrak g_{13}\)-module presentation of \(N\), rather than replacing \(N\) by a free exterior source.

Put
\[
v=e_2,\qquad T=E_3.
\]

At \(a=0\), the first-arm module is precisely the node-\(3\) string
\[
\operatorname{span}\{v,Tv,\ldots,T^sv\}\cong V_s.
\]

The first second-arm relation module begins at \(a=1\), so it contributes nothing at \(a=0\). The second begins at
\[
v\wedge Tv
\]
and its \(a=0\) part is exactly its whole node-\(3\) closure, the \(V_{2s-2}\) summand.

The standard multiplicity-free exterior decomposition therefore gives the **actual** boundary module
\[
\boxed{
\bigoplus_nS_{(0,2,n)}
=
\bigoplus_{j=1}^{\lfloor(s-1)/2\rfloor}
V_{2s-2-4j}.
}
\]
The \(j\)-th summand begins at \(n=2j+1\).

### 6.1 Explicit actual lowest vectors and actual \(F_2\)

Let \(k=2j+1\), so
\[
3\le k\le s,\qquad k\text{ odd}.
\]

Define
\[
y_k=\sum_{i=0}^{j}c_i[T^iv,T^{k-i}v],
\qquad c_0=1,
\]
where
\[
c_{i+1}
=
-\frac{(k-i)(s-k+i+1)}{(i+1)(s-i)}c_i
\qquad(0\le i<j).
\]

All denominators are nonzero. The recurrence is exactly cancellation of successive coefficients after applying
\[
F_3T^iv=i(s-i+1)T^{i-1}v.
\]
The central wedge in the even lower grade is zero. Thus
\[
F_3y_k=0.
\]
Also \(F_1y_k=0\), because \(F_1\) commutes with \(T\) and kills \(v\).

The actual Chevalley action is
\[
F_2v=-h_2,\qquad F_2Tv=-e_3,\qquad F_2T^iv=0\quad(i\ge2).
\]

Therefore, for \(k\ge3\),
\[
F_2[v,T^kv]=(k-2)T^kv,
\]
\[
F_2[Tv,T^{k-1}v]=-T^kv,
\]
and all terms with \(i\ge2\) contribute zero. Since
\[
c_1=-\frac{k(s-k+1)}s,
\]
we obtain
\[
\boxed{
F_2y_k=
\frac{(k-1)(2s-k)}s\,T^kv.
}
\]

This is nonzero: the scalar is positive, and
\[
F_3^kT^kv
=
k!\,\frac{s!}{(s-k)!}\,v\ne0.
\]

Thus every displayed lowest vector is a genuine nonzero actual vector. No exterior-character calculation alone is being used to certify existence.

### 6.2 Radical exclusion and component coverage

The adopted first-arm theorem gives
\[
\mathcal R\cap M=0.
\]
If \(y_k\in\mathcal R\), ideal stability would put its nonzero \(F_2\)-image in \(\mathcal R\cap M\), impossible.

The boundary decomposition is multiplicity-free with distinct node-\(3\) highest weights. Its intersection with \(\mathcal R\) is a node-\(3\) submodule and therefore a sum of a subset of these summands. Since none of their lowest vectors can belong to \(\mathcal R\),
\[
\boxed{
\mathcal R\cap\bigoplus_nS_{(0,2,n)}=0.
}
\]

The summand indexed by \(k\) occupies precisely
\[
k\le n\le2s-k,
\]
with one-dimensional weight spaces. This proves Theorem B’s complete dimension formula and every asserted boundary radical equality.

Additionally, each \(y_k\) generates an actual irreducible \(\mathfrak g_{13}\)-module
\[
U(\mathfrak g_{13})y_k
\cong L_{\mathrm{low}}^{(13)}(k+2,\,2s-2k),
\]
and the same ideal argument proves
\[
\mathcal R\cap U(\mathfrak g_{13})y_k=0.
\]
This constituent statement does **not** declare an entire overlapping root component radical-free unless all its other constituents have separately been covered.

---

## 7. Contraction and original-component consequences

For every actual component covered by Theorem A,
\[
\overline A_2=\overline\mu_2\overline{\mathcal C}_2
\]
is invertible. Hence
\[
\ker\overline{\mathcal C}_2=0,
\qquad
\operatorname{im}\overline{\mathcal C}_2
\cap\ker\overline\mu_2=0,
\]
and
\[
\ker(\overline A_2)^m=0\qquad(m\ge1).
\]

Only at the retained **f314 whole-two-seed/full-generalized-primary interface** does this give
\[
\operatorname{im}(e_2\Phi_2)_\alpha=E_{2,\alpha}.
\]
Here \(e_2\) in the last display denotes the interface’s grade-two projector notation, not a newly identified Chevalley action.

No ordinary-kernel calculation has replaced generalized-primary control.

The radical conclusions in §§5–6 have their separate ideal proofs. They are not consequences inferred from these contraction statements.

---

## 8. Optional exact finite certificate — complete source, NOTRUN

The source below is a proposed **independent finite corroboration of Theorem A**, not an executed result and not a proof of its universal parameter quantifiers.

It constructs:

- the actual eight-dimensional finite-Levi module as explicit traceless \(3\times3\) matrices;
- its complete 28-dimensional exterior square;
- the actual \(F_3:\Lambda^2V\to V\) from Chevalley brackets and the \(h_3\)-weights;
- every \(W_0,\ldots,W_7\), including the full mixed Gram inverse;
- all four finite-Levi equivariance identities;
- every eigenspace dimension;
- the complete \(r=1\) relation-module closure;
- all actual \(b=2,n=2\) component dimensions and determinants.

The fixed proposed inputs are
\[
(r,s)=(1,2),(1,3),(2,3),(3,4).
\]

It uses only the Python standard library and a cooperative 55-second deadline. **No runtime or successful completion has been observed.** Parent must materialize the exact source, bind its bytes and interpreter, and record the required named GO before any execution. No command has been issued here.

For materialization, each following inline literal is one source line. Strip its numeric prefix through `|`; preserve the remaining indentation.

`001|from fractions import Fraction as Q`  
`002|from itertools import combinations`  
`003|import time`  
`004|`  
`005|START = time.monotonic()`  
`006|def guard():`  
`007|    if time.monotonic() - START > 55:`  
`008|        raise TimeoutError("cooperative 55-second certificate limit")`  
`009|`  
`010|def zero(r, c):`  
`011|    return [[Q(0) for _ in range(c)] for _ in range(r)]`  
`012|`  
`013|def eye(n):`  
`014|    return [[Q(i == j) for j in range(n)] for i in range(n)]`  
`015|`  
`016|def add(a, b, k=Q(1)):`  
`017|    return [[x + k*y for x, y in zip(ar, br)] for ar, br in zip(a, b)]`  
`018|`  
`019|def scale(a, k):`  
`020|    return [[k*x for x in row] for row in a]`  
`021|`  
`022|def mm(a, b):`  
`023|    assert len(a[0]) == len(b)`  
`024|    bt = list(zip(*b))`  
`025|    out = []`  
`026|    for row in a:`  
`027|        guard()`  
`028|        out.append([sum((x*y for x, y in zip(row, col)), Q(0)) for col in bt])`  
`029|    return out`  
`030|`  
`031|def mv(a, v):`  
`032|    return [sum((x*y for x, y in zip(row, v)), Q(0)) for row in a]`  
`033|`  
`034|def va(a, b, k=Q(1)):`  
`035|    return [x + k*y for x, y in zip(a, b)]`  
`036|`  
`037|def cols(vs):`  
`038|    return [list(row) for row in zip(*vs)]`  
`039|`  
`040|def comm(a, b):`  
`041|    return add(mm(a, b), mm(b, a), Q(-1))`  
`042|`  
`043|def rank(a):`  
`044|    if not a or not a[0]:`  
`045|        return 0`  
`046|    b = [[Q(x) for x in row] for row in a]`  
`047|    k = 0`  
`048|    for c in range(len(b[0])):`  
`049|        guard()`  
`050|        p = next((i for i in range(k, len(b)) if b[i][c]), None)`  
`051|        if p is None:`  
`052|            continue`  
`053|        b[k], b[p] = b[p], b[k]`  
`054|        pivot = b[k][c]`  
`055|        b[k] = [x / pivot for x in b[k]]`  
`056|        for i in range(len(b)):`  
`057|            if i != k and b[i][c]:`  
`058|                factor = b[i][c]`  
`059|                b[i] = [x - factor*y for x, y in zip(b[i], b[k])]`  
`060|        k += 1`  
`061|        if k == len(b):`  
`062|            break`  
`063|    return k`  
`064|`  
`065|def unit(i, j):`  
`066|    a = zero(3, 3)`  
`067|    a[i][j] = Q(1)`  
`068|    return a`  
`069|`  
`070|U = [unit(2, 0), scale(unit(2, 1), -1), unit(1, 0),`  
`071|     add(unit(0, 0), unit(1, 1), -1),`  
`072|     add(unit(2, 2), unit(1, 1), -1),`  
`073|     unit(0, 1), unit(1, 2), unit(0, 2)]`  
`074|`  
`075|def coord(a):`  
`076|    assert sum(a[i][i] for i in range(3)) == 0`  
`077|    return [a[2][0], -a[2][1], a[1][0], a[0][0],`  
`078|            a[2][2], a[0][1], a[1][2], a[0][2]]`  
`079|`  
`080|def action(x):`  
`081|    return cols([coord(comm(x, u)) for u in U])`  
`082|`  
`083|E1 = action(unit(0, 1))`  
`084|E2 = action(unit(1, 2))`  
`085|F1 = action(unit(1, 0))`  
`086|F2 = action(unit(2, 1))`  
`087|E12 = comm(E1, E2)`  
`088|I8, I28 = eye(8), eye(28)`  
`089|ev = [list(v) for v in zip(*I8)]`  
`090|ew = [list(v) for v in zip(*I28)]`  
`091|pairs = list(combinations(range(8), 2))`  
`092|ab = [(0, 0), (1, 0), (0, 1), (1, 1),`  
`093|      (1, 1), (2, 1), (1, 2), (2, 2)]`  
`094|`  
`095|def wedge(v, w):`  
`096|    return [v[i]*w[j] - v[j]*w[i] for i, j in pairs]`  
`097|`  
`098|def lift(d):`  
`099|    return cols([va(wedge(mv(d, ev[i]), ev[j]),`  
`100|                    wedge(ev[i], mv(d, ev[j]))) for i, j in pairs])`  
`101|`  
`102|G1, G2 = lift(F1), lift(F2)`  
`103|H1, H2 = lift(E1), lift(E2)`  
`104|bracket = [cols([wedge(ev[i], ev[j]) for j in range(8)]) for i in range(8)]`  
`105|qr = wedge(ev[0], ev[1])`  
`106|qs = wedge(ev[0], ev[2])`  
`107|y = va(va(wedge(ev[0], ev[3]), wedge(ev[0], ev[4]), -1),`  
`108|       wedge(ev[1], ev[2]), -1)`  
`109|`  
`110|def nc(w, d8, d28):`  
`111|    return add(mm(w, d28), mm(d8, w), -1)`  
`112|`  
`113|def iszero(a):`  
`114|    return all(x == 0 for row in a for x in row)`  
`115|`  
`116|for r, s in [(1, 2), (1, 3), (2, 3), (3, 4)]:`  
`117|    guard()`  
`118|    delta0 = [[Q((r*a+s*b-2) if i == j else 0)`  
`119|               for j in range(8)] for i, (a, b) in enumerate(ab)]`  
`120|    delta = [delta0, scale(E1, -r), scale(E2, -s),`  
`121|             scale(E12, -s), scale(E12, r),`  
`122|             zero(8, 8), zero(8, 8), zero(8, 8)]`  
`123|    f = cols([va(mv(delta[i], ev[j]), mv(delta[j], ev[i]), -1)`  
`124|              for i, j in pairs])`  
`125|    w0 = f`  
`126|    w1, w2 = nc(f, F1, G1), nc(f, F2, G2)`  
`127|    w3, w4 = nc(w2, F1, G1), nc(w1, F2, G2)`  
`128|    w5 = scale(nc(w3, F1, G1), Q(-1, 2))`  
`129|    w6 = scale(nc(w4, F2, G2), Q(1, 2))`  
`130|    w7 = nc(w6, F1, G1)`  
`131|    dual = [w0, w1, w2,`  
`132|            scale(add(scale(w3, 2), w4, -1), Q(1, 3)),`  
`133|            scale(add(scale(w4, 2), w3, -1), Q(1, 3)),`  
`134|            w5, w6, w7]`  
`135|    op = zero(28, 28)`  
`136|    for bmat, dmat in zip(bracket, dual):`  
`137|        op = add(op, mm(bmat, dmat))`  
`138|    lr, ls, lc = Q(4*(r-1)), Q(4*(s-1)), Q(5*(r+s)-4)`  
`139|    assert mv(f, qr) == [2*(r-1)*x for x in ev[1]]`  
`140|    assert mv(f, qs) == [2*(s-1)*x for x in ev[2]]`  
`141|    expected_y = va([Q(3*r+2*s-2)*x for x in ev[3]],`  
`142|                    [Q(2*r+3*s-2)*x for x in ev[4]], -1)`  
`143|    assert mv(f, y) == expected_y`  
`144|    for v, lam in [(qr, lr), (qs, ls), (y, lc)]:`  
`145|        assert mv(op, v) == [lam*x for x in v]`  
`146|    for d in [G1, G2, H1, H2]:`  
`147|        assert iszero(comm(op, d))`  
`148|    for lam, multiplicity in [(lr, 10), (ls, 10), (lc, 8)]:`  
`149|        assert 28-rank(add(op, scale(I28, lam), -1)) == multiplicity`  
`150|    rel = []`  
`151|    pending = [qr] if r == 1 else []`  
`152|    while pending:`  
`153|        guard()`  
`154|        v = pending.pop()`  
`155|        if rank(cols(rel+[v])) == len(rel):`  
`156|            continue`  
`157|        rel.append(v)`  
`158|        pending.extend([mv(H1, v), mv(H2, v)])`  
`159|    assert len(rel) == (10 if r == 1 else 0)`  
`160|    for v in rel:`  
`161|        assert mv(f, v) == [Q(0)]*8`  
`162|        assert mv(op, v) == [Q(0)]*28`  
`163|    for a in [1, 2, 3]:`  
`164|        idx = [k for k, (i, j) in enumerate(pairs)`  
`165|               if ab[i][0]+ab[j][0] == a and ab[i][1]+ab[j][1] == 2]`  
`166|        assert len(idx) == (4 if a == 2 else 3)`  
`167|        assert all(op[i][j] == 0 for j in idx for i in range(28) if i not in idx)`  
`168|        block = [[op[i][j] for j in idx] for i in idx]`  
`169|        mult0 = 2 if a == 2 else 1`  
`170|        for lam, multiplicity in [(lr, 1), (ls, 1), (lc, mult0)]:`  
`171|            assert len(idx)-rank(add(block, scale(eye(len(idx)), lam), -1)) == multiplicity`  
`172|        intersection = len(rel)+len(idx)-rank(cols(rel+[ew[j] for j in idx]))`  
`173|        assert intersection == (1 if r == 1 else 0)`  
`174|        actual_dimension = len(idx)-intersection`  
`175|        determinant = lc**mult0 * ls * (lr if r != 1 else Q(1))`  
`176|        assert determinant > 0`  
`177|        print("case", r, s, "component", (a, 2, 2),`  
`178|              "actual_dimension", actual_dimension, "determinant", determinant)`  
`179|    print("complete fixed level-two certificate", r, s)`  
`180|guard()`  
`181|print("all four fixed cases completed; universal and f276 claims remain written/imported")`

**Execution record:** NOTRUN. There is no observed stdout, exit code, elapsed time, finite-check verdict, or source/interpreter hash for this new proposed certificate. The printed strings above are source text, not claimed output.

---

## 9. Provenance and chronology

Parent-supplied bindings:

- Manifest SHA256: `0992e9dc93c83d0bdce27f580d2f76367f9ee6a73f16e2c794cbf88fb660e228`
- Freeze-receipt SHA256: `4c1088c547f4d64bb229d56dd6464d5d7e89002093d653d807cf55d115ed3a24`
- Packet SHA256: `e4a986a393fe49b179f352f2d83e0541eb016147cbf4420b657095bc787c565a`
- Supplied parent clock: `2026-10-30T12:17:35-0700 PDT`

These are **parent-attributed observations**, not child-executed hashes, a child-native start clock, or measured derivation time.

Actual access order:

1. Read the mandatory memory summary and written-mathematics protocol skill as procedural context.
2. Read the complete manifest, receipt and parent live metadata.
3. Read all ten permission/status controls through their endings, without opening the named held payloads or their consumers.
4. Sent the direct pre-body acknowledgement to Main.
5. Read the complete ordered literal packet in exact raw windows of at most 20 lines: \(1\!-\!20,\ldots,861\!-\!880,881\!-\!893\), through `S3|43`.
6. Derived the written results above from the frozen inputs and elementary finite-dimensional representation algebra.
7. Read the dispatch receipt as metadata.

S2 is an author manuscript input; its own historical “not independently reviewed” header is not silently upgraded. Adopted scope is taken only from the separately supplied S1/S3 dispositions and their explicit interfaces.

No external scientific source, linked checker, current sibling scientific body, held mathematical payload, or excluded diagnostic consumer was opened. The controls were used only for permissions and exclusions. This is an access chronology, not a cognitive-isolation certificate.

No scientific executable, build, test, lint, formatter, model CLI, heavy/paid/remote job, installation, deletion, credentials change, git mutation, or repository write was performed. The proposed source is returned here because execution and working-tree materialization were not available under this runtime’s role restrictions.

---

## 10. Remaining original obligations and requested disposition

### Newly claimed, pending disjoint checking

1. Complete actual third-grade-two source and relation-module identification.
2. All three full-contraction scalars, including the full mixed Gram normalization and raised-vector equivariance.
3. Complete actual \(b=2,n=2\) dimensions and determinants for every allowed parameter.
4. Separate radical equality on the entire actual third-grade-two module.
5. Complete all-grade \(a=0,b=2\) radical equality, its actual nonzero lowest vectors and component dimensions.
6. Radical-freeness of the explicitly identified \(\mathfrak g_{13}\)-constituents generated by \(y_k\).

### Still unpaid

- Full second-arm contraction invertibility in the remaining interior grades
  \[
  3\le n\le L(r,s)+1.
  \]
- Full active mixed low-grade matrices outside the complete \(n=2\) result.
- Radical equality for all of \(N\); the boundary and displayed constituent arguments do not exhaust it.
- Whole level eight, \(B_8=0\), global \(J=\tau\), equal/larger-arm extensions, or arbitrary both-horizontal-coefficient closure.
- Independent reconstruction of f276/f306/f314.
- An executed finite certificate for this candidate.
- Original-book authentication, current-status/novelty/priority findings, human review, independent-family review, or formal/kernel acceptance.

**Requested next disposition:** independently reconstruct the actual level-two elimination and whole relation closure, canonical-tensor equivariance with all eight consumers, the three scalar calculations, and the two separate radical arguments. If desired, parent may separately authorize and run the complete proposed finite source above. No acceptance is self-granted.