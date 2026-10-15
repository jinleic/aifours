# Round 2: coefficient two, the missing coupling, and certified infinite bands

Date: 2026-10-14 (America/Los_Angeles).

**Scope.** The full nonsymmetrizable Gabber–Kac/Serre-ideal conjecture remains the goal and is not proved or refuted. This note supplies:

1. an exact explanation of why the coefficient-one comparison proof does not automatically extend to coefficient two;
2. a presentation of level two as a quotient of an exterior square, with an exact remaining-lowering criterion;
3. a short certificate-to-band proof, plus an optional independent hand proof, of coefficient-two equality for the uniform family
   \[
   A(r,s)=\begin{pmatrix}2&-1&-1\\-1&2&-1\\-r&-s&2\end{pmatrix},\qquad r,s\in\mathbb Z_{\ge1},
   \]
   at the third node, including `A_one=A(2,1)`;
4. a certificate-to-infinite-band theorem under an entrywise nonnegative inverse hypothesis. Applied to the existing exact height-12 receipt for `A_one`, it excludes every defect with
   \[
   \alpha_1\le3\quad\text{or}\quad\alpha_2\le2\quad\text{or}\quad\alpha_3\le4,
   \]
   at **every height**.

The last conclusion is a proved transfer from a finite certificate, not extrapolation from samples. No research computation, build, test, model call, or additional certificate verification was run for this note. The displayed calculations are symbolic hand derivations. No novelty claim is made.

## 1. Setup and previously established premises

Use the conventions of [proof.md](../proof.md), especially §§2–4 and 7–9, and [descent-audit.md](descent-audit.md), §§9–10. Let `S(A)` be the full Serre quotient and let

\[
R=\tau/I=\ker(S(A)\longrightarrow\mathfrak g(A)).
\]

Only its positive homogeneous components are considered below. Fix a node `i`, let `J` be its complement in the supported principal matrix, and write

\[
S_k=\bigoplus_{\beta\in\mathbb N^J}S(A)_{k\epsilon_i+\beta},
\qquad R_k=R\cap S_k,\qquad V=S_1.
\]

Here `k` is the **level**, not total height. Put `E_j=ad(e_j)`, `F_j=ad(f_j)` and `D_i=ad(f_i)`.

The previously proved facts used are:

- the positive Serre ideal is stable under every lowering;
- the exact recurrence for `K` identifies it with the maximal Cartan-disjoint ideal;
- if `A_J` is symmetrizable, then `R_1=0`;
- every `ad(e_j)` and `ad(f_j)` is locally nilpotent on `S(A)`;
- a positive homogeneous vector annihilated by all simple lowerings has `A alpha<=0`.

For completeness, the last assertion needs only an elementary `sl_2` calculation. If `F_j x=0`, `h_j x=m x`, and `t` is the largest integer with `E_j^t x!=0`, then

\[
F_jE_j^n x=-n(m+n-1)E_j^{n-1}x.
\]

Applying this at `n=t+1` gives `m=-t<=0`. Existence of `t` follows from local nilpotence. This argument does not use irreducibility of a nonsymmetrizable module.

We work over `C` when using the finite-dimensional Levi representations. All presentations and displayed maps are rational; the resulting equalities also hold over `Q`, since a nonzero rational quotient vector remains nonzero after extension of scalars.

## 2. Two distinct failures of the naive comparison argument

### 2.1 The omitted row controls a genuinely different lowering

The comparison in proof §7 retains the rows indexed by `J`, but replaces row `i` by

\[
b_{ij}=d_j a_{ji},\qquad b_{ii}=2.
\]

Consequently the `J`-lowerings agree, but `D_i` need not agree, even on coefficient-one words. For `j!=i`, direct use of the defining relations gives

\[
[f_i,[e_j,e_i]]=[e_j,-h_i]=a_{ij}e_j.
\tag{2.1}
\]

In the comparison algebra the scalar is `b_ij`, not `a_ij`. Thus equality of the positive slices and their Levi actions never supplies equality of their omitted-node lowering maps.

At coefficient two, the positive slices themselves can also change. A relation with leading index `i` contributes precisely at level `1-a_ij`. Hence the relation

\[
(\operatorname{ad}e_i)^2e_j=0
\]

appears in level two exactly when `a_ij=-1`. Changing `-1` to `-2` removes a level-two relation; changing `-2` to `-1` introduces one. Equality of the coefficient-one presentations does not prevent this.

For `A_one` with `i=3`, a symmetrizable comparison retaining rows 1 and 2 must have `b_31=b_32`. It cannot retain both `a_31=-2` and `a_32=-1`. Choosing both comparison entries to be `-1` adds a level-two relation absent from `A_one`; choosing both at most `-2` removes a level-two relation present in `A_one`. Section 4 identifies the corresponding nonzero modules, so this is not just a possible presentation mismatch.

### 2.2 Two occurrences of `f_i` cannot be moved into one innermost `f_i`

Every word

\[
\operatorname{ad}(f_{j_1})\cdots\operatorname{ad}(f_{j_m})f_i,
\qquad j_\nu\in J,
\]

has `i`-coefficient exactly one. It therefore cannot span a nonzero negative root space with `i`-coefficient two. This is an exact grading obstruction, not a missing application of Jacobi.

What Jacobi does provide at level two is a span by brackets `[u,v]`, where each of `u,v` contains one `f_i` and is obtained by `J`-adjoints from `f_i`. In the invariant pairing of a symmetrizable comparison algebra,

\[
(x,[u,v])=([x,u],v).
\]

The operation `[x,u]` now uses an occurrence of `f_i`. Moving all adjoints across the pairing therefore requires the omitted-node lowering, or brackets built from it. Its equality between `A` and the comparison matrix has not been established and generally fails by (2.1).

Equivalently, `J`-lowerings preserve level. At level one they can descend to the known zero extra-ideal component at `epsilon_i`. At level two they can stop at a nonzero Levi-lowest vector without ever reaching level one. Section 4 gives an explicit such vector even in the symmetrizable affine comparison `A(1,1)`.

These facts refute the attempted *proof implication*. They do not produce an extra Serre relation or a counterexample to the conjecture.

## 3. Exact level-two presentation and the remaining map

Assume `A_J` is symmetrizable, and put `v=e_i` in `V`. The action of the Levi algebra on `V` is the actual adjoint action inside the Serre quotient. In particular

\[
F_jv=0,\qquad h_jv=a_{ji}v,\qquad
E_j^{1-a_{ji}}v=0.
\]

### 3.1 Exterior-square presentation

**Proposition.** There is a canonical Levi-module isomorphism

\[
S_2\cong\frac{\Lambda^2V}{T},\qquad
T=\sum_{\substack{j\in J\\a_{ij}=-1}}
U(\mathfrak g_J)(v\wedge E_jv).
\tag{3.1}
\]

The bracket realizes the displayed quotient. Entries `a_ij<=-2` introduce no level-two relation. Zero entries are already incorporated in `V` through `E_jv=0`.

**Proof.** Let `N=n_J^+`, and form the cyclic `N`-module

\[
M=U(N)v\Big/\sum_{j\in J}U(N)E_j^{1-a_{ji}}v.
\]

Let `L(M)` be the free Lie algebra on the vector space `M`. The `N`-action on `M` extends uniquely to derivations of `L(M)`, giving a semidirect product `N lt L(M)`.

This semidirect product is precisely the positive Lie algebra with the relations internal to `J` and the relations whose leading index lies in `J`, before imposing the remaining `i`-leading Serre relations. To check this without importing a free-Lie elimination theorem, map its generators to that presented algebra. The cyclic module relations make the map from `M` well defined; freeness extends it to `L(M)`, and the adjoint action gives compatibility with the semidirect product. Conversely, the same named generators in `N lt L(M)` satisfy all the specified relations. The two resulting maps are inverse because each composition fixes every generating `e_j` and `v`.

No remaining positive relation has level one, except a zero-edge commutation already present in `M`. Thus `M=V`. The degree-two component of the free Lie algebra on `V` is `Lambda^2 V`: skew-symmetry imposes the exterior-square relation, while Jacobi first imposes relations in degree three. One can check injectivity directly in the tensor algebra by `u wedge w -> u tensor w-w tensor u`.

For `a_ij=-q<0`, the remaining Serre relation is

\[
(\operatorname{ad}v)^{q+1}e_j
=-(\operatorname{ad}v)^q(E_jv),
\]

of level `q+1`. Positive brackets cannot decrease that level. Thus only `q=1` contributes to level two, and its level-two descendants are exactly the `U(N)`-span of `v wedge E_jv`.

Finally these spans are already full Levi-submodules. For every `k in J`,

\[
F_k(v\wedge E_jv)=0:
\]

if `k!=j`, both terms vanish; if `k=j`, the only possible term is `v wedge(-a_ji v)=0`. Each generator is a Cartan weight vector. Reordering a word in Levi generators using the commutator relations moves all negative generators to the right, where they kill this vector, and then moves Cartan generators to the right, where they act by scalars. Hence its full Levi span equals its `U(N)`-span. This proves (3.1). QED.

This proposition describes the presentation, not the radical. There is still a nontrivial map

\[
D_i:S_2\longrightarrow V
\]

to analyze, and its coefficients use the original row `i`.

### 3.2 An exact detection criterion

For `k>=2`, set

\[
P_k=\{x\in S_k:F_jx=0\text{ for every }j\in J\}.
\]

**Lemma.** If `R_(k-1)=0`, then

\[
R_k=0\quad\Longleftrightarrow\quad
D_i\big|_{P_k}\text{ is injective}.
\tag{3.2}
\]

**Proof.** If `R_k!=0`, choose a nonzero homogeneous component of `R_k` of least total `J`-degree. Its vector `x` is killed by every `F_j`, since these preserve level and decrease total `J`-degree. Moreover `D_i x` belongs to `R_(k-1)=0`. Thus injectivity fails.

Conversely, a nonzero vector in the kernel of the displayed restriction has a nonzero homogeneous component `x` with the same property. All simple lowerings of a free-Lie representative of `x` lie in the Serre ideal. They therefore lie in `K`, and the exact recurrence from proof §3 puts the representative in `K`. Since `x!=0` in the Serre quotient, `R_k!=0`. QED.

In particular the coefficient-one theorem makes (3.2) applicable at level two. For a finite-dimensional Levi module, (3.1) often makes `P_2` accessible. But replacing `P_2` by the single line `Cv` would be wrong, and `D_i` is not generally a Levi-module homomorphism.

## 4. A proved uniform coefficient-two theorem with an `A_2` Levi

**Theorem.** For every pair of positive integers `r,s`, and

\[
A(r,s)=\begin{pmatrix}2&-1&-1\\-1&2&-1\\-r&-s&2\end{pmatrix},
\]

one has

\[
I_\alpha=K_\alpha\qquad\text{for every positive degree with }\alpha_3=2.
\tag{4.1}
\]

The family is nonsymmetrizable when `r!=s`. Its first two rows and its third column are fixed; this is not a theorem for every GCM having an `A_2` deletion.

### 4.1 Primary proof: the uniform height-six theorem plus the band lemma

For every matrix in this family, deleting node 3 gives

\[
B=\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\qquad
a_{J3}=\binom{-1}{-1},\qquad
-B^{-1}a_{J3}=\binom11.
\]

Thus the constant in the band theorem proved in §5.1 is `C_3=3`, independently of the bottom-row parameters `r,s`. Proof §9 has already established equality through height six for **every** rank-three GCM. Its non-boundary polynomial certificate has the opened `PASS` receipt [symbolic-222/all-cells-independent-check.json](symbolic-222/all-cells-independent-check.json); the coefficient-zero/one theorem handles the other degrees.

Apply §5.1 with `H=6`, `k=2`: `floor(C_3 k)=6`. It follows that equality holds throughout the band `alpha_3<=2`, in particular (4.1). This proof is uniform in `r,s`, uses no highest-weight representation theorem, and needs no new computation. QED.

The remaining §§4.2–4.5 are an **optional independent corroboration**. They do not use the uniform height-six certificate. They are retained because they resolve the requested exterior-square/coupling audit explicitly and show precisely which part of the coefficient-one comparison fails.

### 4.2 Independent proof: the level-one module is the adjoint module

Take `i=3`, `J={1,2}`. The Levi is `sl_3`, with

\[
e_1=E_{12},\quad e_2=E_{23},\quad
f_1=E_{21},\quad f_2=E_{32},
\]

and `h_1=E_11-E_22`, `h_2=E_22-E_33`. The coefficient-one vector `v` is a cyclic integrable lowest-weight vector of weight `(-1,-1)`.

The precise representation fact used here is restricted to this **symmetrizable Levi**: its maximal integrable highest-weight module of dominant integral highest weight is irreducible. This is stated explicitly in the opened Heckenberger–Kolb text, §2.1, lines 103–115; the lowest-weight version follows by the Chevalley involution. Thus any nonzero cyclic integrable lowest-weight module of weight `(-1,-1)` is the corresponding simple module.

The adjoint `sl_3` module has such a lowest vector `E_31`, and is irreducible because `sl_3` is simple. Consequently

\[
V\cong\mathfrak{sl}_3,\qquad v\longmapsto E_{31}.
\]

This is not an assertion about irreducibility for the nonsymmetrizable algebra `S(A(r,s))`.

Put

\[
u=E_1v,\quad w=E_2v,\quad
p=E_1E_2v,\quad q=E_2E_1v.
\]

In the matrix realization,

\[
u=-E_{32},\quad w=E_{21},\quad p=h_1,\quad q=-h_2.
\tag{4.2}
\]

In particular `p,q` are independent. The lowering actions needed below are

\[
\begin{array}{c|ccccc}
 &v&u&w&p&q\\\hline
F_1&0&v&0&2w&w\\
F_2&0&0&v&u&2u
\end{array}
\tag{4.3}
\]

and follow either directly from the matrix brackets or from the `sl_2` relations and the weights.

### 4.3 Independent proof: decomposition of the exterior square

In `Lambda^2 V` define

\[
t_1=v\wedge u,\qquad t_2=v\wedge w,\qquad
z=v\wedge(p-q)-u\wedge w.
\tag{4.4}
\]

Using (4.3), `F_1` and `F_2` kill each of these vectors. For `z`, explicitly,

\[
F_1z=2v\wedge w-v\wedge w-v\wedge w=0,
\]

\[
F_2z=v\wedge u-2v\wedge u+v\wedge u=0.
\]

Their respective lowest weights and full multidegrees are

\[
\begin{array}{c|c|c}
\text{vector}&(h_1,h_2)\text{-weight}&(\alpha_1,\alpha_2,\alpha_3)\\\hline
t_1&(0,-3)&(1,0,2)\\
t_2&(-3,0)&(0,1,2)\\
z&(-1,-1)&(1,1,2).
\end{array}
\tag{4.5}
\]

All three are nonzero. For `z`, the terms `v wedge p`, `v wedge q`, `u wedge w` are independent exterior basis vectors after extending `v,u,w,p,q` to a basis.

Let `M_1,M_2,M_0` be their cyclic Levi-submodules. Each is an integrable lowest-weight module, so the same symmetrizable-Levi irreducibility theorem identifies it with the simple module of its specified lowest weight.

For clarity, the dimensions used here do not require a tensor-product table. The simple module of lowest weight `(0,-3)` is `Sym^3 C^3`, of dimension ten. To verify simplicity directly, use the monomials `x_1^a x_2^b x_3^c`, `a+b+c=3`, with `E_ab` acting as `x_a partial_b`. Their Cartan weights are distinct. A nonzero invariant subspace contains a monomial weight vector; lowering moves it with a nonzero coefficient to `x_3^3`, and raising from `x_3^3` obtains every degree-three monomial. The module of lowest weight `(-3,0)` is its dual and has dimension ten; the dual is simple because the annihilator of a proper invariant subspace would be a proper invariant subspace of the original simple module. The module of lowest weight `(-1,-1)` is the adjoint eight-dimensional module already identified above.

These three simple modules are pairwise nonisomorphic, so their sum is direct. Indeed two have zero intersection; a simple module embedded in their direct sum would have a nonzero projection to one of the summands and hence be isomorphic to it. Finally

\[
10+10+8=28=\dim\Lambda^2(\mathbb C^8),
\]

so the direct sum exhausts the exterior square:

\[
\Lambda^2V=M_1\oplus M_2\oplus M_0.
\tag{4.6}
\]

In each summand the common kernel of `F_1,F_2` is just its displayed lowest line. One way to see this without a semisimplicity assertion about an unknown algebra is that any other homogeneous lowest vector would generate a nonzero submodule, hence the whole simple summand; its positive-root descendants could not then recover the original smaller lowest weight. The original lowest weight space is one-dimensional in the explicit modules above.

### 4.4 Independent proof: the quadratic Serre summands

By (3.1), the relation with leading node 3 and target node 1 contributes to level two exactly when `r=1`; its exterior-square vector is `-t_1`. Similarly the relation targeting node 2 contributes exactly when `s=1`, with vector `-t_2`. Thus

\[
S_2\cong M_0
\oplus\begin{cases}M_1,&r\ge2,\\0,&r=1,\end{cases}
\oplus\begin{cases}M_2,&s\ge2,\\0,&s=1.\end{cases}
\tag{4.7}
\]

In particular

\[
\dim S_2=28-10\mathbf1_{r=1}-10\mathbf1_{s=1}.
\]

This is a presentation result valid uniformly in `r,s`; no finite sample was used. It also proves the comparison-slice mismatch discussed in §2: `A_one=A(2,1)` has an eighteen-dimensional level-two space, whereas the equal-row symmetrizable comparisons with row entries both `-1` or both at most `-2` have dimensions eight or twenty-eight respectively.

### 4.5 Independent proof: the original omitted-row lowering

Now use the actual third row `(-r,-s,2)`, and write `D=ad(f_3)`. Put `t=[e_1,e_2]`. The defining relations give

\[
Dv=-h_3,\quad Du=-r e_1,\quad Dw=-s e_2,
\quad Dp=-s t,\quad Dq=r t,
\quad [t,v]=p-q.
\tag{4.8}
\]

For example, `Du=[e_1,-h_3]=-r e_1`, displaying explicitly the omitted-row dependence.

Interpret (4.4) in the level-two quotient using brackets. Since `h_3` acts on `u` with weight `2-r`,

\[
Dt_1=[-h_3,u]+[v,-r e_1]=2(r-1)u.
\]

Likewise

\[
Dt_2=2(s-1)w.
\tag{4.9}
\]

Both maps are nonzero whenever the corresponding summand survives (4.7); precisely at `r=1` or `s=1`, the zero is accounted for by the actual quadratic Serre relation.

The remaining vector is detected for every `r,s>=1`. The weight of `p-q` under `h_3` is `2-r-s`, so

\[
\begin{aligned}
D[v,p-q]
&=[-h_3,p-q]+[v,-(r+s)t]\\
&=(2r+2s-2)(p-q),\\
D[u,w]&=-r p+s q.
\end{aligned}
\]

Therefore

\[
\boxed{Dz=(3r+2s-2)p-(2r+3s-2)q.}
\tag{4.10}
\]

The vectors `p,q` are independent, and both displayed scalar magnitudes are strictly positive. Hence `Dz!=0`.

The surviving lowest lines in (4.7) have distinct full multidegrees (4.5), so their `D`-images have distinct multidegrees and cannot cancel each other. Equations (4.9)–(4.10) prove injectivity of `D` on `P_2`. Since `R_1=0` by the coefficient-one theorem, (3.2) yields `R_2=0`. This proves (4.1). QED.

For the affine symmetrizable comparison `r=s=1`, the nonzero vector `z` is killed by both Levi lowerings, but `Dz=3(p-q)!=0`. This is the promised explicit obstruction to detecting level two using only the `J`-lowerings. It is a surviving ordinary root vector, **not** an extra relation.

For fixed finite-type Levi, a fixed-level slice such as this one is finite-dimensional. The theorem covers all degrees in the slice and all positive parameters `r,s`, but does not control unbounded level `alpha_3`. For `A_one` its slice is also contained in the already certified finite-height region; its value here is an independent structural proof and the uniform parameter statement, not a newly observed numerical range.

## 5. An inverse-nonnegative deletion transfers a certificate to an infinite band

This section audits the parent's additional structural proposal. It requires no highest-weight representation theorem and does not assume symmetrizability of the full matrix or even impose it separately on the deletion.

### 5.1 The theorem and its full proof

**Theorem.** Fix a node `i`, let `J` be its complement, and suppose

\[
B=A_J\text{ is invertible},\qquad B^{-1}\ge0
\]

entrywise. Define

\[
r=-B^{-1}a_{Ji}\ge0,\qquad C_i=1+\sum_{j\in J}r_j.
\tag{5.1}
\]

Suppose `I_alpha=K_alpha` has been established for **every** positive degree of total height at most `H`. If an integer `k>=0` satisfies

\[
\lfloor C_i k\rfloor\le H,
\tag{5.2}
\]

then equality holds for every positive degree with `alpha_i<=k`, without a total-height restriction.

**Proof.** Assume there is a defect in the band `alpha_i<=k`, and choose one of least total height **within that band**. This choice does not claim global minimality among defects outside the band.

All lowerings decrease total height and remain inside the band. The extra ideal has no simple-root or Cartan component. Thus every simple lowering of a nonzero vector `x` in the chosen extra-ideal component is zero in the Serre quotient. The elementary integrable `sl_2` argument in §1 gives

\[
A\alpha\le0.
\]

The rows indexed by `J` say

\[
B\alpha_J\le-a_{Ji}\alpha_i.
\]

Multiplication by the entrywise nonnegative matrix `B^{-1}` preserves these coordinatewise inequalities, giving

\[
\alpha_J\le r\alpha_i.
\tag{5.3}
\]

Consequently

\[
\operatorname{ht}(\alpha)
=\alpha_i+\sum_{j\in J}\alpha_j
\le C_i\alpha_i\le C_i k.
\]

Since height is integral, (5.2) puts this defect at height at most `H`, contradicting the assumed certificate scope. QED.

The same proof permits the slightly sharper integer bound

\[
k+\sum_j\lfloor r_jk\rfloor\le H,
\]

because `alpha_i<=k` and `r>=0` imply `alpha_j<=floor(r_j k)`. The simpler bound (5.2) suffices for the applications below.

The downward-closed-band step is indispensable: merely bounding the globally first defect would not exclude a later defect inside the band if an earlier one existed elsewhere. Choosing the least defect inside the band closes that gap exactly.

### 5.2 Application to the accepted height-12 `A_one` certificate

For

\[
A_{\rm one}=\begin{pmatrix}2&-1&-1\\-1&2&-1\\-2&-1&2\end{pmatrix},
\]

the three deletions have entrywise nonnegative inverses. In the natural increasing order of `J`, their parameters are

\[
\begin{array}{c|c|c|c}
i&B^{-1}&r&C_i\\\hline
1&\frac13\begin{pmatrix}2&1\\1&2\end{pmatrix}
 &(4/3,5/3)&4\\[2pt]
2&\begin{pmatrix}1&1/2\\1&1\end{pmatrix}
 &(3/2,2)&9/2\\[2pt]
3&\frac13\begin{pmatrix}2&1\\1&2\end{pmatrix}
 &(1,1)&3.
\end{array}
\tag{5.4}
\]

The opened [height-12 scope](height12-scope.json) specifies every positive degree through height 12 for exactly this matrix. The opened [independent-check receipt](rational-height12/independent-check.json) reports `PASS`, field `Q`, requested height 12 and matrix `one_asymmetric_edge`, with certificate SHA-256

`df670cfc9f6fa2e890e6631283c3a39f525e51d29a3f28cc78cf1ae103c0f9de`.

This note reads and uses that existing receipt; it does not claim a new checker execution. The theorem applied separately at the three nodes gives the unconditional consequence of that accepted certificate:

\[
\boxed{I_\alpha=K_\alpha\quad\text{if}\quad
\alpha_1\le3\ \text{or}\ \alpha_2\le2\ \text{or}\ \alpha_3\le4.}
\tag{5.5}
\]

In particular, coefficient two at **any** node of `A_one` is excluded at every height. This statement is stronger for this fixed matrix than the independent family theorem of §4, but it uses the existing exact finite certificate as a premise.

Any defect not covered by (5.5) must satisfy

\[
\alpha_1\ge4,\qquad\alpha_2\ge3,\qquad\alpha_3\ge5.
\tag{5.6}
\]

The certificate alone still says nothing unbounded about that remaining region.

### 5.3 The height-13 implication is conditional, and the exact target is isolated

**Conditional statement.** If equality for every positive degree through height 13 is established, then the same theorem gives

\[
I_\alpha=K_\alpha\quad\text{if}\quad
\alpha_1\le3\ \text{or}\ \alpha_2\le3\ \text{or}\ \alpha_3\le4,
\tag{5.7}
\]

because `floor((9/2)*3)=13`. Thus coefficient three at any node would also be excluded at every height. No height-13 computation is claimed in this note.

The preceding arguments also justify why the parent-owned degree `(4,4,5)` suffices as the remaining height-13 target. By (5.6), the only degrees of height 13 not already excluded by the infinite bands are

\[
(5,3,5),\qquad(4,4,5),\qquad(4,3,6).
\]

A defect at height 13 is primitive because equality through height 12 is already established. At `(5,3,5)`, row 1 gives `2*5-3-5=2>0`; at `(4,3,6)`, row 3 gives `-2*4-3+2*6=1>0`. Both contradict the primitive inequality. The middle degree has

\[
A_{\rm one}(4,4,5)^T=(-1,-1,-2)^T,
\]

so this argument does not exclude it. Therefore an accepted exact equality proof at `(4,4,5)`, together with the already established premises, would supply the full height-13 premise of (5.7). The exact computation and its acceptance remain owned by the parent.

## 6. What remains indispensable for the full conjecture

Neither the exterior-square theorem nor the infinite-band transfer solves the unbounded problem.

- For a general symmetrizable deletion, the missing coefficient-two statement is the concrete injectivity
  \[
  D_i:\left(\Lambda^2V/T\right)^{\{F_j=0:j\in J\}}\longrightarrow V.
  \]
  The domain may have many lowest-weight summands and multiplicities. The actual row `i` must be retained. Symmetrizable comparison alone proves neither injectivity nor compatibility of this map.
- Beyond coefficient two, the exact sufficient-and-necessary inductive target is (3.2) for every level, after the preceding level is known to have no extra ideal. The free-Lie presentation from §3 extends to higher level, but its additional relations and its primitive subspaces become more complicated. No irreducibility theorem for a nonsymmetrizable ambient algebra is supplied or assumed.
- The band theorem only excludes bounded coordinate bands from a fixed finite certificate. Its bound grows with `k`; it provides no finite bound on all possible defects. For example `A_one*(m,m,m)^T=(0,0,-m)^T` for every positive integer `m`. For sufficiently large `m` these degrees lie outside all the currently excluded bands. They are **candidates not ruled out by these necessary conditions**, not asserted roots or defects.

A full proof must eliminate the remaining unbounded interior region, for example by proving the remaining-lowering injectivity uniformly at all levels. A counterexample would require an actual nonzero vector in `K/I` with an exact characteristic-zero witness. Neither has been obtained here.

## 7. Sources actually opened and the limits of their use

- [proof.md](../proof.md), §§2–4 and 7–9: exact lowering, descent recurrence, coefficient-one comparison, integrability/primitive-weight argument, and the uniform rank-three height-six theorem.
- [descent-audit.md](descent-audit.md), §§9–10: the mixed-string proof, full-Levi bookkeeping and the carefully limited symmetrizable comparison.
- Heckenberger–Kolb, *On the Bernstein–Gelfand–Gelfand resolution for Kac–Moody algebras and quantized enveloping algebras*, [arXiv:math/0605460](https://arxiv.org/abs/math/0605460), opened local text [sources/heckenberger-kolb-2006.txt](../sources/heckenberger-kolb-2006.txt), lines 103–115 and 257–262. The former explicitly states irreducibility of the maximal integrable highest-weight quotient for a **symmetrizable** algebra. The latter explicitly warns that simplicity for arbitrary Kac–Moody algebras is not known there. Only the `A_2` Levi use is made in §4.
- Marquis, opened [minicourse text](../sources/marquis-minicourse-2023.txt), Example 0.1(1), lines 75–77: the `A_2` Cartan matrix gives `sl_3`.
- Gorelik–Hinich–Serganova, opened [local text](../sources/gorelik-hinich-serganova.txt), §8.3.1, lines 2372–2385: the invariant-form radical statement supporting the already established symmetrizable comparison premise. No invariant form on the nonsymmetrizable ambient algebra is inferred.
- [height12-scope.json](height12-scope.json) and [rational-height12/independent-check.json](rational-height12/independent-check.json): the fixed-matrix finite premise for §5, read without rerunning it.
- [symbolic-222/all-cells-independent-check.json](symbolic-222/all-cells-independent-check.json): opened `PASS` status and exact scope of the uniform `(2,2,2)` certificate used, together with the boundary theorem, in the primary proof §4.1. No checker was rerun.
