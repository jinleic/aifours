# All-reference working checkpoint 017: the entire zero-sector p principal block is PPT-positive

Before-writing clock observed: `2026-10-23T19:06:31-07:00` (`/bin/date -Iseconds`).

Status: **CANDIDATE / UNREVIEWED written proof**. No scientific program, numerical evaluation, import, compilation, solver, model CLI, or proof assistant was used. This is one component of the same unfinished universal-reference W4 route, not a full W4 result or a novelty certification.

**Delta:** the zero-charge p-only upper block is the partial transpose of an explicit rank-nine orthoprojection. A local diagonal filter and a four-dimensional Hodge estimate prove its positivity for every reference. On the full positive reference interior its twelve-dimensional reference quotient is strictly positive. Thus the **upper** zero-charge block can instead reduce to a **six-dimensional q-plus Schur form**. The lower zero-nine obligation is not settled by this proof.

## 1. Identify the actual restricted map

The p coordinates of checkpoint 002 (SHA256 `3940d80c695b96272b59cb3c10c98ccadde720f63dc93152155be4f4b17fdea1`) are

```
p(i,j)=|i,i,j,j>.
```

Identify the diagonal two-site input/output subspaces `span{|ii>}` with `C^4`. On those subspaces the original `B=Lambda tensor Lambda` restricts to

```
Bdiag(X)=Tr(X)I-diag(X)+X/4.                 (17.1)
```

For `i!=k`, `B(|ii><kk|)=|ii><kk|/4`; for `i=k`, its output-diagonal entries are `1/4` at `|ii>` and one at the other `|jj>`. This proves (17.1) directly.

Let `c=(c_1,...,c_4)^T` be the normalized real Schmidt vector, `P=cc^T`, `Q=I-P`, `d_i=1-c_i^2`, and `D0=diag(d_i)`. The restricted reference output is

```
A0=Bdiag(P)=D0+P/4,
```

whose inverse is exactly the G block in checkpoint 005. The adjoints of the restricted L_i send every output-diagonal basis vector back into the diagonal auxiliary subspace. Hence the p-only block of the **full** conditional map is exactly the CP peeling

```
Phi=Bdiag-Mdiag,
Mdiag(E_ik)=Bdiag(|i><c|) A0^(-1) Bdiag(|c><k|).
```

There is no replacement of the full auxiliary inverse by an unrelated model: its actual invariant G block is used. The desired p-only upper matrix is `J(Phi)^Gamma`, partial transpose on this four-dimensional input.

We use column vectorization: `|K>>=sum_i |i>_input tensor K|i>_output`. Thus p(i,j) corresponds to the matrix unit with output row j and input column i.

## 2. The ordinary Choi remainder is an orthoprojection

The ordinary Choi matrix of Bdiag is

```
Pi=sum_(i!=j)|i,j><i,j|+|Omega_4><Omega_4|/4.
```

It is an orthoprojection of rank thirteen. In matrix-vectorization language its range is precisely the space of matrices K whose four diagonal entries are one common scalar.

The CP peeling ordinary Choi matrix is

```
J(Mdiag)=Pi(P tensor A0^(-1))Pi.
```

Indeed the column construction `T_v|i>=Bdiag(|i><c|)v` gives `|T_v>>=Pi(|c> tensor |v>)`. The input-c compression of Pi is A0, so this is the orthoprojection onto `ran[Pi(|c> tensor I)]`, of rank four. Therefore

```
J(Phi)=Pi-J(Mdiag)=Pi_S,
S={K:Kc=0, diag(K)=lambda 1}, dim S=9.       (17.2)
```

This establishes complete positivity of Phi. It does **not** establish its complete copositivity or PPT just from rank/projection. The remaining proof is essential.

## 3. Exact row-product decomposition of Pi_S

First assume every d_i is positive, which excludes only product-reference vertices. Set

```
q_i=Q e_i=e_i-c_i c,
T_i=|i><q_i|,
Y=sum_i 1/d_i, r=1/Y,
W0=D0^(-1)Q.
```

The four T_i are mutually orthogonal in Hilbert-Schmidt inner product and have squared norms d_i. The orthogonal complement of S is the sum of all matrices `|v><c|` and the traceless diagonal matrices. Projecting the latter onto the input-c-perpendicular space gives

```
{sum_i t_i T_i: sum_i t_i=0}.
```

Within `span{T_i}`, its orthogonal complement is `sum_i T_i/d_i=W0`, whose squared norm is Y. Consequently

```
Pi_S=B0+r|W0>><<W0|,

B0=sum_i [Q-|q_i><q_i|/d_i]_input
         tensor |i><i|_output.              (17.3)
```

Each bracket is an orthoprojection of rank two. B0 is positive, of rank eight. It is unchanged by input partial transpose because c and q_i are real. Formula (17.3) follows from orthogonal projections, not an assumed separable decomposition of Pi_S.

## 4. Apply a real local filter before estimating the partial transpose

Let `rho=Pi_S^Gamma`, and apply the invertible local output filter D0:

```
rho'=(I tensor D0)rho(I tensor D0).
```

Since `D0 W0=Q`, equation (17.3) becomes

```
rho'=B0'+r(P_s-P_a),                        (17.4)

B0'=sum_i d_i^2[Q-|q_i><q_i|/d_i]
                 tensor |i><i|.
```

Here `P_s` and `P_a` are respectively the symmetric and antisymmetric projections on `Q tensor Q`. More explicitly the second term in (17.4) is `r(Q tensor Q)F`, because the partial transpose of `|Q>><<Q|` equals `(Q tensor Q)F` for the real orthoprojection Q. Thus its only negative part is `-r P_a`.

The key estimate will be

```
B0'>=2r P_a.                                (17.5)
```

## 5. Hodge estimate proving (17.5)

An antisymmetric vector in `wedge^2(c^perp)` is a complex skew-transpose matrix K with `Kc=0`. There is a unique representation

```
K=star(c wedge v), c^T v=0,
||K||_HS^2=2||v||^2.
```

For each row i, the three-dimensional complex Lagrange identity gives

```
sum_j |K_ij|^2
=(sum_(j!=i)c_j^2)(sum_(j!=i)|v_j|^2)
 -|sum_(j!=i)c_j v_j|^2
=d_i||v||^2-|v_i|^2.                        (17.6)
```

The last equality uses `sum c_i v_i=0`. This derivation applies to complex v; it is not a restriction to real test directions.

Each row of K is orthogonal to c, and also to q_i because `K_ii=0` and `Kc=0`. Hence `|K>>` lies in the range of B0', whose Moore-Penrose inverse acts on that row by division by `d_i^2`. Thus

```
<<K|(B0')^+|K>>
=sum_i [d_i||v||^2-|v_i|^2]/d_i^2
=Y||v||^2-sum_i |v_i|^2/d_i^2
<=(Y/2)||K||_HS^2.                          (17.7)
```

For clarity, (17.7) implies the operator inequality (17.5), not merely a restricted quadratic-form inequality on the antisymmetric space. If psi is arbitrary and k is an antisymmetric vector, range inclusion and Cauchy-Schwarz give

```
|<k,psi>|^2
<=<k,(B0')^+k><psi,B0'psi>
<=(Y/2)||k||^2<psi,B0'psi>.
```

Take the supremum over unit k in that antisymmetric subspace. The result is

```
||P_a psi||^2 <=(Y/2)<psi,B0'psi>,
```

which is exactly `B0'>=(2/Y)P_a=2r P_a`.

## 6. PPT conclusion, including the correct domain

Equations (17.4)-(17.5) give

```
rho'
=[B0'-2r P_a]+r(P_s+P_a)
>=r(Q tensor Q)>=0.                        (17.8)
```

Undo the real invertible local filter. This proves `Pi_S^Gamma>=0`, equivalently positivity of the **whole p-only upper co-Choi block**, for every nonproduct reference. At a product-reference vertex, take a continuous limit: A0 remains uniformly positive (`A0>=I/4`), so the actual peeling map and its co-Choi matrix are continuous. No `1/d_i` or inverse output filter is evaluated at the zero denominator.

Thus every normalized reference is included. This proof establishes a PPT orthoprojection family in ordinary Choi form; it does not use a general assertion that projections of rank nine are PPT.

## 7. Strictness on the interior and the new upper zero-sector residual

For the full positive Schmidt interior, the p-only co-Choi form is strictly positive on its twelve-dimensional input-c-perpendicular quotient. Here is the kernel argument rather than an unsupported inversion.

If rho' has a zero vector in `Q_input tensor C^4_output`, (17.8) forces its output component to lie in `span{c}`. Write it as `v_input tensor c_output`, with `v orthogonal c`. The nonnegative decomposition in (17.8) also forces B0' to vanish on it. In output row i this requires `c_i v` to be proportional to q_i. When all c_i are positive, choose distinct i,j; their Gram determinant is

```
d_i d_j-c_i^2 c_j^2=1-x_i-x_j>0.
```

Thus q_i,q_j are independent, forcing v=0. This proves the required strictness. No complete extra-kernel classification at sparse boundary references is claimed.

In the original zero-charge twenty-eight-dimensional upper block, first remove the four true reference kernels. The six q-minus directions are reducing with their earlier positive pivot. The remaining p12 principal block is strictly positive on the interior by the proof above, so it can be eliminated **with all p/q-plus cross terms retained**. The resulting upper q-plus Schur form has dimension **six**.

This is an alternative pivot order to checkpoint 010's q-first/K-first nine-dimensional representation. The upper six sign is not proved here. If it is proved for the whole positive reference interior, positivity of the full physical zero block at sparse spectra must then be concluded by continuity, not by inverting a boundary-singular p pivot.

## 8. Source, review, and remaining scope

A quick existing-interface question to PhysicsPPT44 returned no already-read classification of (17.2); the peer did not perform a derivation, review, search, or execution. That is **not independent verification and not a novelty audit**. No sign verdict was imported from the rank, projection property, or that peer's separate P44 certificate families.

The same unfinished universal-reference route now has:

1. both nonzero-charge P4 Schur signs;
2. the upper zero-charge q-plus6 Schur sign on the full interior, with the required physical boundary extension;
3. the lower zero-charge9 Schur sign.

The entire p-only component is only a principal block of the zero-charge co-Choi matrix; it is not the full zero block. The ordinary rank-nine projection is not a rank-two Werner coefficient witness. No full universal-reference theorem, unrestricted W4 theorem, asymmetric route failure, novelty certification, independent acceptance of this leaf, or formal/kernel verification is claimed.
