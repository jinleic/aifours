# Exact descent audit for the defining-relations conjecture

Date: 2026-10-14 (PT). Scope: a mathematical audit, with hand-derived symbolic formulas. No code, builds, tests, linear-algebra programs, or solvers were executed.

## 1. Verdict and source premises

The proposed descent recurrence is **correct over characteristic zero**, provided that:

1. the preliminary algebra is the book's algebra with a **full Cartan realization**, not merely the span of the simple coroots when the matrix is singular;
2. the height-one case is set separately to `K_(epsilon_i) = 0`;
3. the lowering operators use one consistent sign convention and the **rows** of the Cartan matrix; and
4. the recurrence is computed in the free positive Lie algebra, before assuming the Serre presentation is complete.

It computes the actual positive part of the maximal Cartan-disjoint ideal, not an approximation to it. Computing it through a finite height therefore gives the actual root spaces of the contragredient quotient through that height. It does **not** establish equality with the Serre ideal at greater heights.

Two uniform special cases are proved below. For every rank-three GCM with all six off-diagonal entries strictly negative,

\[
K_{(1,1,1)}=I_{(1,1,1)}=0,
\qquad
K_{(2,1,1)}=I_{(2,1,1)}.
\]

The second assertion also holds after permuting the three indices. Combining these results with the symmetrizable rank-two theorem gives equality in every positive degree of height at most four for this family. This is a bounded-degree result, not an all-height nonsymmetrizable theorem.

The independent extension audit in §9 additionally proves equality in **every degree `(m,1,1)`, for all integers `m>=0`**, and its index permutations, for the same family. This is an infinite family of degrees, not equality in all root degrees. For each fixed matrix, the corresponding Serre quotient is already zero when `m>p+q`.

The stronger boundary theorem in §10 proves equality whenever one coefficient is one and the complementary principal submatrix on the support is symmetrizable. In rank three this excludes **every** degree with a coefficient one. Together with the rank-two theorem it proves equality through height five; the first degree not excluded by these arguments is `(2,2,2)`, not `(2,2,1)`.

Primary premises opened for this audit:

- **Book, printed pp. 226–227 / supplied PDF pp. 242–243:** [local excerpt](../sources/book-excerpt.txt), lines 12–23 give the GCM, full-rank matrix `C`, preliminary presentation, and quotient by `tau`; lines 25–34 give the symmetrizable theorem and Conjecture 1. The argument below uses the book's convention `[e_i,f_j] = delta_ij h_i`.
- **Timothée Marquis, _Around the Lie Correspondence for Complete Kac–Moody Groups and Gabber–Kac Simplicity_, §2.2:** [primary PDF](https://arxiv.org/pdf/1509.01976), [opened local text](../sources/marquis-2015.txt), lines 308–341. This explicitly supplies freeness of the positive and negative subalgebras, their triangular vector-space decomposition, and the maximal Cartan-disjoint ideal. Its displayed convention at lines 315–322 has the opposite sign for `[e_i,f_j]`; replacing every `f_i` by `-f_i` converts it to the book's convention. Its notation `g(A)` at lines 340–341 denotes the **Serre quotient**, unlike the book's notation for the maximal-ideal quotient. These two definitions must not be identified in the nonsymmetrizable case without proof.
- **Maria Gorelik, Vladimir Hinich, Vera Serganova, _Root groupoid and related Lie superalgebras_, §1.1.3:** [primary PDF](https://art.centre-mersenne.org/item/10.5802/art.13.pdf), [opened local text](../sources/gorelik-hinich-serganova.txt), lines 93–105, independently distinguishes the maximal-ideal and explicit-Serre constructions and states their agreement in the symmetrizable case.

No theorem from the failed HTML download named `zellhofer-thesis.pdf` is used. No quantum-specialization result is being substituted for the classical conjecture.

## 2. Setup, grading, and the lowering signs

The construction in this section works in any finite rank `n`. Let `F` be a characteristic-zero field, let `A=(a_ij)` be a GCM, and choose the full realization used in the book. Write

\[
\widetilde{\mathfrak g}=L^-\oplus\mathfrak h\oplus L^+,
\qquad L^+=\operatorname{Lie}_F(e_1,\ldots,e_n)
\]

for the triangular decomposition. The positive algebra is genuinely free here. Its degree is in the formal root lattice with basis `epsilon_i`; put `deg(e_i)=epsilon_i`, `deg(f_i)=-epsilon_i`, and `deg(h)=0`.

The book's full-column-rank matrix `C` makes the simple roots linearly independent as functionals on `h`. Thus distinct root-lattice degrees have distinct `h`-weights. Every ideal is `h`-stable, so it splits into homogeneous components: on the finite set of weights appearing in any particular vector, polynomial projections in a suitable `ad(h)` extract those components. This is where the full realization and characteristic zero matter. Using only the rows of a singular `A` to identify distinct weights would leave a gap in this argument.

For a positive degree `beta`, define

\[
w_i(\beta)=\sum_j a_{ij}\beta_j.
\]

The actual operator is `D_i = ad(f_i)` in the preliminary algebra. It satisfies

\[
D_i e_j=-\delta_{ij}h_i,
\qquad
D_i[u,v]=[D_i u,v]+[u,D_i v].
\]

For positive height at least two it maps `L_alpha` into `L_(alpha-epsilon_i)`, with an absent/nonpositive target interpreted as zero. At height one it can land in `h`, so it is **not** a derivation from the whole of `L^+` to `L^+`.

When a height-one factor produces `-h_i`, the replacements are exactly

\[
[-h_i,v]=-w_i(\deg v)v,
\qquad
[u,-h_i]=+w_i(\deg u)u.
\]

These formulas apply recursively to any bracket tree, including standard Lyndon bracket trees. The weight is that of the **remaining subtree**, including any occurrences of `e_i` and hence contributions from `a_ii=2`.

Useful sign checks, for `i != j`, are

\[
D_i[e_i,e_j]=-a_{ij}e_j,
\qquad
D_j[e_i,e_j]=a_{ji}e_i,
\]

and

\[
D_i(\operatorname{ad}e_i)^m e_j
=-m(a_{ij}+m-1)(\operatorname{ad}e_i)^{m-1}e_j.
\tag{2.1}
\]

The last identity follows by induction from the derivation rule and the weight `a_ij+2(m-1)` of `(ad e_i)^(m-1)e_j`.

Concrete implementation objections to avoid:

- `[u,-h_i]` has a **plus** weight, not a minus weight.
- The weight uses `a_ij`, not `a_ji`; transposition changes nonsymmetrizable examples.
- Omitting the diagonal contribution `2` gives the wrong coefficient already in degree `(2,1,0)`.
- `D_i e_i` is `-h_i`, not zero. Setting the simple-root kernel to zero is a separate boundary condition, not a license to erase that Cartan term inside a larger bracket.
- A consistent replacement `D_i -> -D_i` leaves the kernel recurrence unchanged, but mixing the book and Marquis conventions inside a derivation does not.

## 3. The Serre-ideal recurrence is exact

Let

\[
r_{ij}=(\operatorname{ad}e_i)^{1-a_{ij}}e_j,
\qquad i\ne j,
\]

and let `I^+` be the Lie ideal of `L^+` generated by these elements. Its homogeneous components satisfy

\[
I_\alpha
=\operatorname{span}\{r_{ij}:\deg r_{ij}=\alpha\}
+\sum_k[e_k,I_{\alpha-\epsilon_k}].
\tag{3.1}
\]

Indeed, the right-hand recursive construction contains every generator and is stable under bracketing with every `e_k`. Jacobi then makes it stable under bracketing with every element of the Lie algebra generated by the `e_k`. It is therefore precisely the generated Lie ideal; arbitrary brackets with longer words are not missing from (3.1).

Every `r_ij` is annihilated by every `D_k`. For `k=i`, use (2.1) with `m=1-a_ij`. For `k=j`,

\[
D_j r_{ij}=-(\operatorname{ad}e_i)^m h_j=0:
\]

if `a_ij<0`, then `m>=2` and `(ad e_i)^2 h_j=0`; if `a_ij=0`, then `m=1` and the GCM axiom gives `a_ji=0`. All other `D_k` vanish directly. This also covers zero off-diagonal entries, even though the low-degree lemmas below assume strict negativity.

## 4. Proof that the maximal-ideal recurrence is exact

Set `K_(epsilon_i)=0`. For positive degrees of height at least two define

\[
K_\alpha
=\{x\in L_\alpha:
D_i x\in K_{\alpha-\epsilon_i}\text{ for every }i\}.
\tag{4.1}
\]

Targets outside the positive cone are zero. Let `K^+` be the direct sum of these spaces.

### 4.1 Stability under all generators

**Cartan stability.** Every `K_alpha` is a subspace of one `h`-weight space, so it is stable under every `h`.

**Lowering stability.** It is built into (4.1). There is no unwanted Cartan output because `K_(epsilon_i)=0`.

**Raising stability.** Induct on the height of `x in K_alpha`. The height-one case is empty. For a generator `e_j`, Jacobi gives

\[
D_i[e_j,x]
=-\delta_{ij}w_i(\alpha)x+[e_j,D_i x].
\tag{4.2}
\]

The first term, if present, belongs to `K_alpha`. The second belongs to `K_(alpha-epsilon_i+epsilon_j)` by the induction hypothesis applied to the lower-height element `D_i x`. Thus every lowering of `[e_j,x]` lies in its required `K` component, proving `[e_j,x] in K_(alpha+epsilon_j)`.

Consequently `K^+` is an ideal of the **entire** preliminary algebra: it is stable under its generators `e_j`, `f_i`, and `h`. It lies in `L^+`, so it meets `h` trivially. Therefore `K^+` is contained in `tau`.

### 4.2 The reverse containment

The maximal Cartan-disjoint ideal is homogeneous by §2. It cannot contain `e_i`, because then it would contain `[f_i,e_i]=-h_i`, contradicting its trivial intersection with `h`.

Induct on height. If `x in tau intersect L_alpha`, then every `D_i x` lies in the lower-degree component of `tau`. The induction hypothesis puts each such lowering in `K_(alpha-epsilon_i)`. Equation (4.1) therefore puts `x` in `K_alpha`. Hence

\[
\boxed{K_\alpha=\tau\cap L_\alpha.}
\tag{4.3}
\]

For completeness, the Chevalley involution `e_i <-> f_i`, `h -> -h` gives the corresponding negative ideal `K^-`. Every Cartan-disjoint ideal is homogeneous, has zero degree-zero part, and has its positive and negative components contained in `K^+` and `K^-` by the same descent argument. Thus

\[
\tau=K^-\oplus K^+.
\]

This also constructs the unique greatest Cartan-disjoint ideal, rather than requiring an unsupported maximality assertion.

By §3, each positive Serre generator belongs to `K^+`; raising stability gives `I^+ subset K^+`. In fact `I^+` itself is lowering-stable: apply (4.2) inductively to its recursively generated elements, starting from `D_i r_jk=0`. Together with its negative counterpart it is exactly the full Serre ideal, without an additional intersection with `h`.

### 4.3 What a finite computation represents

For every positive degree,

\[
\mathfrak g(A)_\alpha\cong L_\alpha/K_\alpha,
\]

where `g(A)` now has the book's maximal-ideal definition. The positive component of the Serre quotient is `L_alpha/I_alpha`. The natural surjection from the latter to the former is an isomorphism exactly when `I_alpha=K_alpha`.

The recurrence is triangular in height, so degrees above `alpha` cannot change `K_alpha`. A calculation through height `N` is therefore exact for these individual root spaces and for structure maps whose source and target are among the calculated spaces.

It is **not** legitimate to call the spaces of the full algebra of absolute height at most `N` a quotient Lie algebra obtained by throwing away all larger degrees: lowering sends degree `N+1` to degree `N`, so the discarded full-algebra subspace is not generally an ideal. The positive algebra alone does have its usual quotient by positive degrees greater than `N`, but the full lowering action need not descend to that positive truncation.

All matrices here can be formed over the integers from `A`. Their ranks over `Q` are unchanged after extension to any characteristic-zero field. Thus a correct exact-`Q` result for a fixed GCM establishes the same componentwise result over `C` and over other characteristic-zero fields.

## 5. Uniform rank-three calculation in degree `(1,1,1)`

Write

\[
A=\begin{pmatrix}
2&-p&-q\\
-r&2&-s\\
-t&-u&2
\end{pmatrix},
\qquad p,q,r,s,t,u\in\mathbb Z_{>0}.
\]

Put `a=e_1`, `b=e_2`, `c=e_3`, and

\[
x=[a,[b,c]],\qquad y=[b,[a,c]].
\]

These form a basis of the two-dimensional free component `L_(1,1,1)`; for example, the standard Lyndon words `123` and `132` give `x` and `-y`.

Every two-letter component `L_(epsilon_i+epsilon_j)` has zero `K`, because its generator lowers to `-a_ij e_j != 0`. There are no Serre generators or their positive descendants in degree `(1,1,1)`, so `I_(1,1,1)=0`.

The lowerings are

| Operator and target basis | `x` | `y` |
|---|---:|---:|
| `D_1`, basis `[b,c]` | `p+q` | `q` |
| `D_2`, basis `[a,c]` | `s` | `r+s` |
| `D_3`, basis `[a,b]` | `-u` | `t` |

The first two rows have determinant

\[
(p+q)(r+s)-qs=pr+qr+ps>0.
\]

Thus the common kernel is zero, proving

\[
\boxed{K_{(1,1,1)}=I_{(1,1,1)}=0,
\qquad \dim\mathfrak g(A)_{(1,1,1)}=2.}
\tag{5.1}
\]

This proof is uniform in all six positive integer parameters and does not assume symmetrizability.

## 6. Uniform rank-three calculation in degree `(2,1,1)`

Let `E=ad(a)` and use the basis

\[
b_1=E^2[b,c],\qquad
b_2=E[b,Ec],\qquad
b_3=[b,E^2c].
\]

This is a basis, not merely a spanning list: the standard Lyndon basis for words `1123`, `1132`, and `1213` is respectively

\[
b_1,\quad -b_2,\quad [[a,b],[a,c]]=b_2-b_3.
\]

The last displayed list is an invertible integral change of basis from `(b_1,b_2,b_3)`. In particular `dim L_(2,1,1)=3`.

The two relevant lower-degree components are one-dimensional:

\[
K_{(2,1,0)}=I_{(2,1,0)}=
\begin{cases}\langle E^2b\rangle,&p=1,\\0,&p>1,\end{cases}
\]

and

\[
K_{(2,0,1)}=I_{(2,0,1)}=
\begin{cases}\langle E^2c\rangle,&q=1,\\0,&q>1.\end{cases}
\]

Indeed `D_1(E^2b)=2(p-1)[a,b]` and `D_1(E^2c)=2(q-1)[a,c]`; the other lowerings of these elements vanish.

### 6.1 The Serre subspace

Only the relations with repeated generator `a` can contribute in degree `(2,1,1)`. The two possible generators are

\[
R=[c,E^2b]=-b_1+2b_2-b_3\quad\text{if }p=1,
\]

and

\[
b_3=[b,E^2c]\quad\text{if }q=1.
\]

The identity for `R` follows by expanding

\[
E^2[b,c]=[E^2b,c]+2[Eb,Ec]+[b,E^2c],
\qquad [Eb,Ec]=b_2-b_3.
\]

Thus

\[
I_{(2,1,1)}=
\operatorname{span}\bigl(\{R:p=1\}\cup\{b_3:q=1\}\bigr).
\tag{6.1}
\]

When both generators occur they are independent.

### 6.2 All lowering matrices

In the target basis `(x,y)` of §5,

\[
D_1=
\begin{pmatrix}
2(p+q-1)&q&0\\
0&p+q-2&2(q-1)
\end{pmatrix}.
\tag{6.2}
\]

In the one-dimensional target bases `E^2c` and `E^2b`, respectively,

\[
D_2=\begin{pmatrix}s&r+s&2r+s\end{pmatrix},
\qquad
D_3=\begin{pmatrix}-u&t&0\end{pmatrix}.
\tag{6.3}
\]

These are maps in the **free** positive algebra. In the recurrence, the `D_2` constraint is vacuous if `q=1`, and the `D_3` constraint is vacuous if `p=1`, because the corresponding target is then entirely `K`. The `D_1` target always has zero `K` by (5.1).

Write a prospective kernel element as `z_1 b_1+z_2 b_2+z_3 b_3`.

- **`p>1`, `q>1`.** The first row of `D_1` and the `D_3` equation give `2(p+q-1)z_1+qz_2=0` and `-uz_1+tz_2=0`. The determinant `2t(p+q-1)+qu` is strictly positive, so `z_1=z_2=0`. The second row of `D_1` then gives `z_3=0`. Hence `K=0=I`.
- **`p=1`, `q>1`.** The two `D_1` equations give `z_2=-2z_1` and `z_3=z_1`, so their kernel is the line spanned by `R`. The remaining required `D_2` equation vanishes on this line since `s-2(r+s)+(2r+s)=0`. Thus `K=span(R)=I`.
- **`p>1`, `q=1`.** The second `D_1` equation gives `(p-1)z_2=0`; the first then gives `2pz_1=0`. Thus its kernel is `span(b_3)`, and `D_3 b_3=0`. Hence `K=span(b_3)=I`.
- **`p=q=1`.** Only the equation `2z_1+z_2=0` remains. Its two-dimensional solution space is `span(R,b_3)`, exactly `I`.

Therefore

\[
\boxed{K_{(2,1,1)}=I_{(2,1,1)},
\qquad
\dim\mathfrak g(A)_{(2,1,1)}
=3-\mathbf1_{p=1}-\mathbf1_{q=1}.}
\tag{6.4}
\]

Permuting the indices proves the corresponding statement in degrees `(1,2,1)` and `(1,1,2)`.

### 6.3 Bounded-height consequence and the named matrices

A degree supported on at most two generators has the same positive free algebra, Serre subspace, and lowering recurrence as the corresponding principal submatrix: every outside lowering vanishes. Each rank-two GCM is symmetrizable; for `[[2,-p],[-r,2]]`, a symmetrizer is `diag(r,p)`. The book's symmetrizable theorem therefore covers all such degrees. In rank three, the only degrees with full support and height at most four are `(1,1,1)` and the three permutations of `(2,1,1)`. Consequently the preceding results prove `I_alpha=K_alpha` for every positive degree of height at most four for rank-three GCMs with strictly negative off-diagonals.

For a fully connected rank-three GCM, a necessary symmetrizability condition is

\[
a_{12}a_{23}a_{31}=a_{21}a_{32}a_{13},
\quad\text{equivalently }pst=ruq.
\]

It follows by multiplying the three equations `d_i a_ij=d_j a_ji`. The two specified examples fail it:

| Matrix | `pst` | `ruq` | `dim g_(1,1,1)` | `dim I_(2,1,1)=dim K_(2,1,1)` | `dim g_(2,1,1)` |
|---|---:|---:|---:|---:|---:|
| `[[2,-1,-1],[-1,2,-1],[-2,-1,2]]` | 2 | 1 | 2 | 2 | 1 |
| `[[2,-1,-2],[-2,2,-1],[-1,-2,2]]` | 1 | 8 | 2 | 1 | 2 |

These entries are consequences of the symbolic proofs, not outputs of an executed numerical experiment. Neither cycle-product failure nor these low-degree dimensions settles the higher-degree defining-relations question.

## 7. Finite-field pitfalls and rigorous exact-Q certification

### 7.1 Why a modular defect is not a characteristic-zero counterexample

Use integral Lyndon/Hall bases of the free Lie algebra. All bracket and lowering matrices then have integer entries. Reduction modulo a prime can lower matrix rank, enlarge a lowering kernel, or lower the rank of the generated Serre subspace. Integral ideal lattices need not be saturated, and rational quotient bases cannot be reduced at primes dividing their denominators without additional care.

A concrete example is the degree `(2,1)` element `z=(ad e_1)^2 e_2` for the rank-two GCM `[[2,-4],[-1,2]]`. Its lowerings are

\[
D_1z=6[e_1,e_2],\qquad D_2z=0.
\]

Over `Q`, its `K` component and Serre component are both zero. Modulo `3`, the displayed lowering matrix is zero and the recursive modular kernel contains `z`, although no Serre relation has that degree. This is a bad-prime effect in the integral matrices, not a counterexample to the book's characteristic-zero theorem.

Agreement or disagreement between several primes is not a replacement for a stated certificate. In particular, finite-field counterexamples in a group-theoretic source do not automatically transfer to this characteristic-zero Lie-algebra conjecture.

### 7.2 Direct exact-Q route

At each height, retain exact rational bases for the lower `K_beta`. Choose an exact rational linear map `Q_beta` with `ker(Q_beta)=K_beta`. Then form

\[
T_\alpha=\operatorname{stack}_i(Q_{\alpha-\epsilon_i}D_i),
\qquad K_\alpha=\ker T_\alpha.
\]

Construct a column matrix `S_alpha` spanning `I_alpha` using (3.1). Fraction-free integer elimination or exact rational elimination can compute both spaces. A compact equality certificate consists of:

1. justified lower-degree quotient maps;
2. an exact basis or spanning certificate for `I_alpha` of dimension `r`;
3. the exact containment `T_alpha S_alpha=0`; and
4. a nonzero `(dim L_alpha-r)`-minor of `T_alpha`.

Containment bounds the rank above by `dim L_alpha-r`; the minor bounds it below by the same number. Equality follows. This avoids inferring rational ranks from numerical tolerances. For an actual counterexample, supply an exact vector in `K_alpha` and an exact linear functional separating it from `I_alpha`, together with certified lower-degree data.

### 7.3 A modular pass can also be a rigorous Q-certificate, under explicit conditions

It would be too strong to say that every modular equality is intrinsically inconclusive. There is a denominator-free certification route.

Let `B_alpha` contain **all complete lowering paths to height one**: its rows are the coefficients of the composites

\[
D_{i_{h-1}}\cdots D_{i_1}:L_\alpha\longrightarrow L_{\epsilon_j},
\qquad h=\operatorname{ht}(\alpha),
\]

for every compatible path and terminal simple root. No path is continued from a simple root into `h`. Set `B_(epsilon_j)` to the identity. Repeated substitution in (4.1) proves

\[
K_\alpha=\ker_{\mathbb Q} B_\alpha.
\]

`B_alpha` and the recursively generated Serre column matrix `S_alpha` are integer matrices, and

\[
B_\alpha S_\alpha=0.
\]

For any prime `ell`, both modular ranks are lower bounds on their rational ranks. If certified modular minors establish

\[
\operatorname{rank}_{\mathbb F_\ell}(S_\alpha)
+\operatorname{rank}_{\mathbb F_\ell}(B_\alpha)
=\dim L_\alpha,
\tag{7.1}
\]

then their rational ranks have sum at least `dim L_alpha`, while the exact annihilation identity forces the sum to be at most that number. Hence equality holds over `Q` and `I_alpha=K_alpha`.

Equivalently, an accurately computed modular recurrence that really is the kernel recurrence of these reduced integral matrices, together with the reduced integral Serre span, can give a valid positive certificate. The necessary conditions are the common integral free-Lie model, correct reductions, the exact annihilation/containment argument, and verifiable rank witnesses. A bare dimension log without those foundations is not such a certificate. A modular **failure** has no corresponding implication of a rational failure.

The all-path matrix need not be materialized in full: selected path rows with certified minors suffice for the required lower rank bound. This is a proposed certification method, not a computation performed in this audit.

## 8. Exact scope of the conclusions

Established here:

- the Serre recursion generates exactly the positive Serre ideal;
- the lowering recurrence generates exactly the positive part of `tau` over characteristic zero;
- the book's maximal quotient is therefore computed correctly componentwise by exact finite-height descent;
- the uniform rank-three lemmas (5.1) and (6.4), and their height-at-most-four consequence;
- the all-`m` mixed-string theorem independently audited in §9;
- the symmetrizable-Levi coefficient-one theorem of §10, which strengthens the rank-three bounded-height conclusion to height five;
- the nonsymmetrizability and stated low-degree dimensions of the two named examples;
- valid exact-rational and integral/modular rank-certificate routes.

Not established here:

- equality in all root degrees for either named matrix;
- equality for all nonsymmetrizable GCMs;
- a height bound after which no new Cartan-disjoint ideal can first appear;
- any inference from passing finitely many matrix/degree tests to the full conjecture.

A first exact failure at a finite degree would refute the conjecture. Any finite collection of passes proves only those degrees, unless an independent all-height theorem supplies a reduction to them. No such reduction has been supplied here.

## 9. Independent audit of the all-`m` mixed-string extension

The proposal in [mixed-string-proposal.txt](mixed-string-proposal.txt) was read and challenged after the initial low-degree audit. Its theorem is **correct under its stated strict-negativity assumptions**. The proof below supplies an explicit ideal-span argument, checks both triangular endpoint ranges, and removes any need to invoke a separate rank-two theorem for its one-string targets. It is a hand-derived mathematical audit, not an executed computation and not a novelty claim.

### 9.1 Statement and a free-Lie basis

Keep the six positive integer parameters and `a,b,c,E` from §§5–6. For every integer `m>=0`, put

\[
v_i^{(m)}=[E^i b,E^{m-i}c],\qquad 0\le i\le m.
\]

Then

\[
\boxed{
I_{(m,1,1)}=K_{(m,1,1)},\qquad
\dim\mathfrak g(A)_{(m,1,1)}
=\max\!\left(0,\min(m,p)-\max(0,m-q)+1\right).
}
\tag{9.1}
\]

First, the `v_i^(m)` form a basis of the **free** component. For spanning, a bracket monomial either separates its unique `b` and `c` between its two branches, giving two one-letter strings and hence a `v_i`, or has both in one branch. In the latter case the other branch consists only of `a` and is zero unless it is the single generator `a`. Induct on `m` and use

\[
E v_i^{(m-1)}=v_i^{(m)}+v_{i+1}^{(m)}.
\]

For an elementary independence proof, map the free Lie algebra to the free associative algebra on `a,b,c`, with commutator bracket. In the image of `v_i^(m)`, the coefficient of the word `a^j b a^(m-j)c` is

\[
\begin{cases}
(-1)^{i-j}\binom{i}{j},&0\le j\le i,\\
0,&j>i.
\end{cases}
\]

Indeed, in `(E^i b)(E^(m-i)c)` the `c` must be the final letter, while the reverse product has `c` before `b` and contributes nothing to this word. The coefficient matrix is triangular with diagonal entries one. Thus the images, and therefore the original Lie elements, are independent. This proves the basis assertion without requiring an unproved dimension count.

### 9.2 Exact characterization of the Serre subspace

The only original positive Serre generators whose degrees can be at most `(m,1,1)` coordinatewise are

\[
E^{p+1}b,\qquad E^{q+1}c.
\]

Every other generator repeats either `b` or `c` at least twice; positive ideal generation cannot decrease that count.

Every `v_i^(m)` with `i>p` or `m-i>q` belongs to the Serre ideal, since one of its factors is a descendant of the appropriate displayed generator. Conversely, §3 allows all ideal descendants to be written as linear combinations of iterated adjoints of the simple generators. A descendant of `E^(p+1)b` in the target degree must apply exactly one `ad(c)` and otherwise only `E`. Consequently it has the form

\[
E^k[c,E^{p+1+\ell}b],
\qquad k,\ell\ge0,\quad m=p+1+k+\ell.
\]

The derivation binomial formula expands this as

\[
-\sum_{j=0}^{k}\binom{k}{j}v_{m-j}^{(m)}.
\]

Every index `m-j` is at least `p+1+ell`, hence exceeds `p`. The analogous descendant

\[
E^k[b,E^{q+1+\ell}c],
\qquad m=q+1+k+\ell,
\]

expands as `sum_(j=0)^k binom(k,j) v_j^(m)`, and every term has `m-j>q`. This proves the reverse containment, including descendants obtained originally by bracketing with arbitrary Lie words.

Thus the Serre subspace has exactly the excluded `v_i` as a basis, and the quotient `V_m=L_(m,1,1)/I_(m,1,1)` has basis

\[
\bar v_i^{(m)},\qquad
\ell_m=\max(0,m-q)\le i\le u_m=\min(m,p).
\tag{9.2}
\]

An empty interval means the zero space; in particular `V_m=0` for `m>p+q`. The displayed dimension in (9.1) follows already for the Serre quotient.

### 9.3 Lowering maps and the induction targets

The lowering action descends to the Serre quotient because §4 proved that the positive Serre ideal is stable under every lowering. Formula (2.1) gives

\[
D_1\bar v_i^{(m)}
=i(p-i+1)\bar v_{i-1}^{(m-1)}
 +(m-i)(q-m+i+1)\bar v_i^{(m-1)}.
\tag{9.3}
\]

Any target index outside (9.2) is interpreted as zero. At a forbidden-to-allowed boundary the corresponding coefficient is itself zero, so this agrees with the actual descended map.

For `m>=1`, the other free-algebra lowerings are

\[
\begin{aligned}
D_2v_0^{(m)}&=(mr+s)E^m c,&
D_2v_1^{(m)}&=-rE^m c,&
D_2v_i^{(m)}&=0\quad(i\ge2),\\
D_3v_m^{(m)}&=-(mt+u)E^m b,&
D_3v_{m-1}^{(m)}&=tE^m b,&
D_3v_i^{(m)}&=0\quad(i\le m-2).
\end{aligned}
\tag{9.4}
\]

For `m=0`, use separately `D_2[b,c]=s c` and `D_3[b,c]=-u b`; no nonexistent `v_1` or `v_(-1)` is introduced.

The one-string components need no general rank-two theorem here. `L_(m,0,1)` is spanned by `E^m c`. For `0<=m<=q`, its Serre subspace is zero, and its `K` subspace is zero by induction from the simple-root case, using

\[
D_1 E^m c=m(q-m+1)E^{m-1}c\ne0
\qquad(1\le m\le q).
\]

For `m>q`, the Serre subspace is the whole one-dimensional free component, so `I subset K` forces equality there too. The corresponding assertions for `E^m b` hold with `p` replacing `q`. Thus the `D_2` target is a nonzero one-dimensional quotient exactly when `m<=q`, and the `D_3` target exactly when `m<=p`.

Now induct on `m`. At `m=0`, `s>0` and `D_2[b,c]=s c` prove `I=K=0`. For `m>0`, the `D_1` target has `I=K` by the previous induction step, and the other two targets have equality by the preceding one-string argument. Therefore `K_(m,1,1)/I_(m,1,1)` is exactly the joint kernel of the three descended lowering maps on `V_m`. This use of quotient maps is not circular.

### 9.4 Triangular ranges, including their endpoints

If `m>p+q`, then `I=L` by (9.2), so equality with `K` is automatic. Assume `1<=m<=p+q`.

**Case A: `m>q`.** The first allowed index is `ell_m=m-q>=1`. In (9.3), choose target rows `i-1` for the source columns `i=ell_m,...,u_m`. These rows belong to the target interval because

\[
\ell_{m-1}=m-q-1=\ell_m-1,\qquad
u_m-1\le\min(m-1,p)=u_{m-1}.
\]

This square submatrix is triangular, with diagonal entries `i(p-i+1)>0`: every source index satisfies `1<=i<=p`. Hence `D_1` is injective. This includes `m=q+1` and `m=p+q`.

**Case B: `m<=q` but `m>p`.** The source interval is `0,...,p`. Choose target rows `i=0,...,p`. They are allowed because the target interval is exactly `0,...,p` when `m>=p+1` and `m<=q`. This square submatrix is triangular with diagonal

\[
(m-i)(q-m+i+1)>0.
\]

Indeed `m-i>=m-p>=1` and `q-m+i+1>=1`. Thus `D_1` is injective here as well, including `m=p+1` and `m=q`.

**Case C: `1<=m<=min(p,q)`.** The source has indices `0,...,m`, and the target `0,...,m-1`. The bidiagonal matrix (9.3) has rank `m`; for example, target rows `i-1` and source columns `i=1,...,m` give a triangular minor with diagonal `i(p-i+1)>0`. Its kernel is one-dimensional.

Write a kernel vector as `z=sum_(i=0)^m z_i bar(v_i)`. The equation in target row `j` is

\[
(j+1)(p-j)z_{j+1}
 +(m-j)(q-m+j+1)z_j=0,
\qquad 0\le j\le m-1.
\]

Every leading coefficient `(j+1)(p-j)` is nonzero. Thus a nonzero kernel vector has `z_0!=0`, and its first equation gives

\[
z_1=-\frac{m(q-m+1)}p z_0.
\]

Using (9.4),

\[
D_2z=
\left(mr+s+\frac{rm(q-m+1)}p\right)z_0\,\overline{E^m c}\ne0.
\]

The coefficient is a strictly positive rational number, hence nonzero in characteristic zero, and the target vector survives because `m<=q`. Therefore even the only possible `D_1` kernel contains no nonzero joint-kernel vector. No `D_3` argument is required in this last case.

All ranges have zero joint kernel, completing the induction and proving (9.1). The boundary `p=q=1` is covered: `m=1` is Case C, `m=2` is Case A, and all `m>2` have zero quotient.

### 9.5 Exact scope of the extension

The theorem holds for all `m>=0` and after any permutation of the three indices. For a fixed GCM, only `0<=m<=p+q` can have a nonzero component along the displayed string; infinitely many remaining degrees vanish already from the Serre relations.

Combining only this all-`m` theorem with the rank-two symmetrizable result shows that any positive extra relation must have full support and at least two coefficients at least two. Section 10 proves the stronger statement that **all three** coefficients must be at least two. Thus `(2,2,1)` and its permutations are also excluded; `(2,2,2)` is the first degree left open by the combined arguments.

The extension does not prove the full book conjecture, does not cover all root degrees of either named matrix, and gives no finite bound reducing those remaining degrees to a completed calculation.

## 10. Stronger coefficient-one theorem via a symmetrizable Levi

### 10.1 Verdict and statement

The proposed integrable-lowest-weight argument is mathematically sound once the full Levi realization and the hypotheses of the symmetrizable representation theorem are made explicit. It is not necessary, however, to leave this audit dependent on an unopened representation-theory theorem: §§10.3–10.4 give a direct proof using the symmetrizable invariant-form premise already present in the opened sources.

Let `A` be any GCM in characteristic zero. Choose an index `i` and a set `J` not containing `i`. Assume that the principal matrix `A_J` is symmetrizable. Then

\[
\boxed{
I_\alpha=K_\alpha
\quad\text{whenever}\quad
\alpha_i=1,\quad
\operatorname{supp}(\alpha)\subseteq J\cup\{i\}.
}
\tag{10.1}
\]

Zero off-diagonal entries are allowed. No symmetrizability of the whole matrix `A` is assumed. The case `J` empty is the simple-root boundary condition.

### 10.2 Audit of the proposed lowest-weight-module proof

Write `S(A)` for the full Serre quotient, and `R(A)=tau/I` for the kernel of its natural map to the book's maximal quotient. Consider

\[
V=\bigoplus_{\beta\in\mathbb N^J}S(A)_{\epsilon_i+\beta}.
\]

The following details repair the potential gaps in the proposed representation-theoretic route.

1. **A full Levi realization exists inside the ambient Cartan.** Let `m=|J|` and `r=rank(A_J)`. The map from the ambient `h` to `F^J`, `h -> (alpha_j(h))_(j in J)`, is surjective because the ambient simple roots are independent. The image of `span{h_j:j in J}` has dimension `r`. Add `m-r` lifts of a complement to that image. Their span together with the `h_j` has dimension `2m-r` and realizes `A_J`. This includes the affine rank-two case, where an additional Cartan direction must not be silently omitted.
2. **The Levi embeds.** Its Chevalley generators and the constructed Cartan satisfy the Serre presentation in `S(A)`. The resulting homomorphism is injective on its Cartan. The symmetrizable theorem identifies its domain with the maximal-ideal quotient, which has no nonzero ideal meeting its Cartan trivially. Thus the homomorphism has zero kernel. This does not assume the nonsymmetrizable conjecture for `A`.
3. **Cyclicity is a Jacobi statement.** Every positive bracket with exactly one occurrence of `e_i` and other letters in `J` is a sum of iterated adjoints of the `e_j`, `j in J`, applied to `e_i`. Hence `V=U(n_J^+)e_i`. Also `[f_j,e_i]=0` and `[h_j,e_i]=a_ji e_i`.
4. **Integrability is genuine.** For fixed `j`, `ad(e_j)` and `ad(f_j)` are locally nilpotent on every Chevalley generator by the Serre relations and the three-dimensional `sl_2` calculation, and on each Cartan vector after at most two applications. The iterated derivation formula then proves local nilpotence on every finite bracket. Thus they are locally nilpotent on `S(A)` and on `V`. This exact mechanism is also stated in the opened [Gorelik–Hinich–Serganova text](../sources/gorelik-hinich-serganova.txt), lines 691–695.
5. **The weight-module hypotheses hold.** Relative to the full Levi Cartan, `V` has finite-dimensional weight spaces with weights in `lambda+Q_J^+`, where `lambda(h_j)=a_ji<=0`. Independence of the restricted simple roots prevents distinct `J`-degrees from collapsing into one weight. Thus it is a cyclic integrable lowest-weight module in the opposite-Borel analogue of category `O`; after the Chevalley involution its highest weight is dominant integral.
6. **The remaining theorem must be used only for the symmetrizable Levi.** The classical irreducibility of such integrable cyclic highest/lowest-weight modules gives irreducibility of `V`. Since `R(A) intersect V` is a Levi-submodule, a nonzero intersection would contain `e_i`, contrary to `K_(epsilon_i)=0`.

The supplied sources do not state that classical module theorem in exactly this general formulation. Rather than present a source-coverage gap as a completed citation, the next proof establishes the needed conclusion directly from the opened symmetrizable invariant-form premise. In particular, it does not assert irreducibility of arbitrary nonsymmetrizable integrable highest-weight modules.

### 10.3 A symmetrizable comparison matrix with the same coefficient-one slice

Because `A_J` is a symmetrizable GCM, choose positive **integer** symmetrizing numbers `d_j`, `j in J`. Such a choice follows by scaling positive rational symmetrizers on its connected components; along every nonzero edge their ratios are positive rational numbers.

On `J union {i}`, define a new GCM `B` by

\[
b_{jk}=a_{jk}\quad(j,k\in J),\qquad
b_{ji}=a_{ji},\qquad
b_{ij}=d_j a_{ji},\qquad
b_{ii}=2.
\tag{10.2}
\]

All off-diagonal entries are nonpositive integers, and the zero reciprocity axiom is preserved. The diagonal matrix with entries `d_j` on `J` and entry `1` at `i` symmetrizes `B`. Thus the symmetrizable defining-relations theorem applies to `B`.

The positive Serre quotients for `A` and `B` have canonically identical components in every degree supported on `J union {i}` with coefficient of `i` equal to one. This is a statement about the same free Lie words and the same contributing ideal generators:

- relations internal to `J` coincide;
- the relations `(ad e_j)^(1-a_ji)e_i` coincide;
- a relation repeating `e_i` has at least two copies of `e_i` if `a_ij<0`, so neither it nor a positive descendant contributes to the slice under consideration;
- if `a_ij=0`, then `a_ji=0` and also `b_ij=0`; the degree-one relation `[e_i,e_j]=0` is the same on both sides;
- a relation involving an index outside `J union {i}` cannot contribute, because positive ideal generation never removes that index.

Consequently the identity on free words induces a degree-preserving isomorphism between the coefficient-one slices of `S(A)` and `S(B)`. It intertwines every raising and lowering with index in `J`: the relevant rows restricted to `J union {i}` are exactly the same in `A` and `B`. No identification of the full algebras, their entire Cartans, or their `i`-lowering operators is claimed.

### 10.4 Nondegenerate pairing excludes an extra-ideal slice

Suppose the slice

\[
W=R(A)\cap
\bigoplus_{\beta\in\mathbb N^J}S(A)_{\epsilon_i+\beta}
\]

were nonzero. It is homogeneous, stable under the `J`-lowerings, and has zero simple-root component `W_(epsilon_i)`. Transport it through §10.3 into the corresponding slice of `S(B)`.

Since `B` is symmetrizable, `S(B)` is its maximal-ideal quotient and has a nondegenerate symmetric invariant bilinear form. This is the form invoked in the [book excerpt](../sources/book-excerpt.txt), lines 38–43; the opened [Gorelik–Hinich–Serganova text](../sources/gorelik-hinich-serganova.txt), §8.3.1, lines 2372–2385, explicitly explains that the radical on the preliminary algebra is the maximal Cartan-disjoint ideal and the quotient inherits a nondegenerate form in the symmetrizable setting.

The full Cartan realization and invariance imply that root spaces of degrees `gamma` and `delta` pair to zero unless `gamma+delta=0`. Indeed, applying any Cartan element to the pairing gives the scalar `(gamma+delta)(h)`. Nondegeneracy therefore gives a nondegenerate pairing between each positive root space and its opposite negative root space.

Choose a nonzero homogeneous `x` in the transported `W`, of degree

\[
\alpha=\epsilon_i+\sum_{j\in J}n_j\epsilon_j.
\]

Every vector of degree `-alpha` in the negative algebra is a sum of bracket monomials containing exactly one `f_i`. Jacobi rewrites each such monomial as a linear combination of

\[
\operatorname{ad}(f_{j_1})\cdots
\operatorname{ad}(f_{j_M})f_i,
\qquad j_k\in J,\quad M=\sum_jn_j.
\]

Invariance transfers all these adjoints to `x`:

\[
\left(x,\operatorname{ad}(f_{j_1})\cdots
\operatorname{ad}(f_{j_M})f_i\right)
=(-1)^M
\left(\operatorname{ad}(f_{j_M})\cdots
\operatorname{ad}(f_{j_1})x,f_i\right).
\]

The vector in the last pairing lies in the transported `W` because of its `J`-lowering stability. Its degree is `epsilon_i`, whose `W` component is zero. Hence `x` pairs to zero with the entire opposite root space, contradicting nondegeneracy. Thus `W=0`, proving (10.1).

This proof uses neither an embedding of the entire nonsymmetrizable algebra into a symmetrizable one nor a nondegenerate invariant form on `g(A)`. Both would be unjustified. Only its coefficient-one Serre slice is compared, and the invariant form belongs to the separately constructed symmetrizable algebra `g(B)`.

### 10.5 Rank-three consequence and the remaining gap

Every rank-two GCM is symmetrizable, including disconnected and affine examples. Therefore, for **every rank-three GCM**, (10.1) excludes extra positive relations in every degree having any coefficient equal to one. Degrees supported on at most two indices are already covered by the rank-two theorem.

Any degree supporting an additional relation modulo the Serre ideal in rank three must consequently have all three coefficients at least two. In particular:

\[
I_\alpha=K_\alpha
\quad\text{for every positive }\alpha
\text{ with }\operatorname{ht}(\alpha)\le5;
\]

the first degree not excluded by these arguments is `(2,2,2)`, of height six. This is not a claim that an extra relation occurs there. Both named nonsymmetrizable matrices satisfy this conclusion, as do all other rank-three GCMs.

The theorem also supplies an infinite boundary family, such as all `(1,m,n)` and their permutations, without bounding `m` or `n`. It still leaves every interior degree with all coefficients at least two unresolved in a genuinely nonsymmetrizable rank-three problem. No conclusion for all heights and all degrees follows.
