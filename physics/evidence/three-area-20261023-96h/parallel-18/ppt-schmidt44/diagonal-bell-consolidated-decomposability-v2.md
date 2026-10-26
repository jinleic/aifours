# Consolidated diagonal-Bell route: every two-block-positive member is decomposable in 4 by 4

Actual `/bin/date` observation before writing: **Sun Oct 25 05:05:44 PDT 2026**. PhysicsPPT44-2 / physics-3. **AUTHOR-WRITTEN CANDIDATE; independent reconstruction and parent disposition pending.** Strictly written algebra and public source reading only. No scientific interpreter, eval, arithmetic program, enumeration, certificate replay or solver was run. Metadata clocks/hashes and source retrieval are not scientific admission. HOLD v2 and parent erratum v7 remain binding.

## 1. Consolidation outcome and exact scope

The previous packet `diagonal-bell-grassmannian-ppt-dual-v1.md`, SHA-256 `9cb9bbf9e4d3631443171b1933c37997caab2034e9913f6ec6e7f2191375e9ab`, left open whether its diagonal-minus-Bell witness family has indecomposable two-positive headroom. This successor provides an explicit **whole-class decomposability proof**, not another parameter increment.

**Theorem.** Let a=(a_ij) be any entrywise nonnegative real4 by4 matrix, and set

```
Omega=00+11+22+33,
W(a)=sum_(i,j=0)^3 a_ij P(ij)-P(Omega).
```

If W(a) is nonnegative on EVERY complex Schmidt-rank-at-most-two vector, then there are explicitly specified PSD operators P,Q with

```
W(a)=P+Q^Gamma.                                            (T)
```

Thus W(a) is nonnegative on **every**4 by4 PPT state. No state restriction is imposed in this conclusion. It is still a **witness-class theorem**, not a no-go for every two-block-positive witness or every P44 state. Positivity of a may have zero entries; the boundary is handled below, not silently discarded.

The proof needs only one fixed matching of the four coordinate indices, elementary two-variable quadratic minimization, a2 by2 PSD criterion, and an explicit operator-entry identity. Neither the unadmitted x1111 table nor the accepted37-term x1111 decomposition is an input.

Consequently this entire witness family should be retired as a positive P44 attack **if this new proof is independently reconstructed**. The previous Grassmannian/PPT-dual reductions remain correct descriptions, but their hoped-for pair a,r cannot exist under the theorem. No more search of that route is warranted merely because its original headroom was unknown.

## 2. Source comparison: the Grassmannian criterion and invariant sparsity are established frameworks

This consolidation exercised a bounded public-source screen, not a novelty clearance or full P44-status certification.

1. Hou–Li–Poon–Qi–Sze, *A new criterion and a special class of k-positive maps*, Linear Algebra Appl.470(2015),51–69, DOI10.1016/j.laa.2014.02.008. Read the author-hosted [primary PDF](https://faculty.sites.iastate.edu/ytpoon/files/inline-files/pmaps_LAA_2015.pdf), especially its definition(8), Proposition4.1 and the explicitly restricted results4.4,4.9,4.10. In their convention

   `L_D(X)=diag_j(sum_i X_ii D_ij)-X`,

   its Choi matrix is exactly our W(a) with **D=a**, not a transposed coefficient matrix. Proposition4.1 already supplies the inverse-compression criterion for k-positivity. Our positive-entry/isometric Grassmannian formulation is a specialization, not a new general characterization. Proposition4.4 has its stated row/column-sum restriction and is not read as an unrestricted D-type classification. Proposition4.10 concerns its permutation/involution subclass, not all a considered here.

2. Britz–Laurent, [arXiv:2512.06551v2](https://arxiv.org/html/2512.06551v2), version metadata24May2026, *Semidefinite hierarchies for diagonal unitary invariant bipartite quantum states*. Read the introduction's CLDUI definitions and equations(5),(8)–(11), and its stated small-cone background near equation(36). Their CLDUI pattern is exactly the coherent-diagonal block plus off-diagonal product diagonals used below. This is an existing invariant-state framework, not a newly discovered sparsity pattern. The source's matrix-cone background is not needed in the proof of (T).

3. The captured Yang–Leung–Tang1603.03534v1 gives its M3-to-M3 result. It is not promoted to an M4 theorem. The Park symplectic family is not assumed to contain our diagonal D-type class.

The searches did not establish an exact earlier equivalent of the whole coefficient-wise decomposition below. That is **not** proof of novelty. The new theorem is presented for route settlement at its own written scope, with priority and broader significance UNCLEAR.

## 3. The prior exact reductions, stated once

For a coefficient matrix C,

```
<vec(C),W(a)vec(C)>=sum_ij a_ij |C_ij|^2-|Tr C|^2.         (1)
```

When all a_ij>0, let U be any complex4 by2 isometry, u_j=U*e_j, and

```
A_j(U)=U*diag(a_0j,a_1j,a_2j,a_3j)U,
H_a(U)=sum_j u_j* A_j(U)^(-1)u_j.
```

Then W(a) is two-block-positive iff H_a(U)<=1 for every U. Indeed write C=UZ for any rank-at-most-two C. Its energy is `sum_j z_j*A_j z_j` and its trace is `sum_j u_j*z_j`. Weighted Cauchy–Schwarz gives the sufficiency. Conversely `z_j=A_j^(-1)u_j` makes (1) equal to `H_a(U)[1-H_a(U)]`, giving a rank-at-most-two negative direction whenever H>1. Basis changes within the same plane conjugate consistently. This agrees with the cited D-type criterion; it is not a finite/real-only test.

The W-preserving diagonal-unitary average of any PPT state has the form

```
R(r,s)=sum_ij r_ij |ii><jj|+sum_(i!=j) s_ij P(ij),
r>=0, s_ij>=0, s_ij s_ji>=|r_ij|^2.                       (2)
```

The conditions follow from the coherent block and the six partial-transpose2 by2 blocks. With d_i=a_ii-1 and c_ij=sqrt(a_ij a_ji), the minimum expectation at fixed r, for positive pair coefficients, is

```
F_a(r)=sum_i d_i r_ii+2sum_(i<j)[c_ij|r_ij|-Re(r_ij)],      (3)
```

attained by `s_ij=|r_ij|sqrt(a_ji/a_ij)`. Thus a negative pair a,r satisfying the Grassmannian condition would be a P44 construction within this class. The rest of this packet proves that no such pair exists, by decomposing W directly. No root finding or optimization of (3) is required.

## 4. A fixed rank-two matching test supplies a copositive4 by4 matrix

Fix the single matching M={{0,1},{2,3}}. For any z_i>=0, consider coefficient matrices C supported on those two2 by2 blocks, with C_ii=z_i and

```
C_ij C_ji=z_i z_j on each matched edge.
```

Each block has determinant zero and rank at most one. Hence the full C has rank at most two. If a_ij,a_ji>0, choose the two nonnegative off-diagonal entries to minimize their energy, obtaining

```
a_ij |C_ij|^2+a_ji |C_ji|^2=2c_ij z_i z_j.
```

If one pair coefficient is zero, the same expression0 is the infimum: keep the product fixed and send the entry carrying positive cost to zero while the other grows. Every approximating matrix still has rank at most two. Nonnegativity of (1) for all of them implies nonnegativity of the limiting finite expression. If both costs vanish, the expression is zero directly. If z_i z_j=0, choose both off-diagonals zero. Thus no boundary case is omitted.

Define the real symmetric matrix K by

```
K_ii=d_i,
K_01=K_10=c_01-1,
K_23=K_32=c_23-1,
K_ij=-1 on the four other unordered pairs.                 (4)
```

The matching tests show

```
z^T K z>=0 for every entrywise nonnegative z.              (5)
```

This means copositivity, not PSD; replacing it by PSD without proof would be invalid. The next steps construct a controlled PSD part explicitly.

Order z=(x,y), where x=(z0,z1), y=(z2,z3). Let

```
B=[d0  b0; b0 d1], b0=c_01-1,
C=[d2  b1; b1 d3], b1=c_23-1,
J=all-ones2 by2 matrix.
```

Then

```
K=[B  -J; -J  C],
z^T K z=x^T Bx+y^T Cy-2(sum x)(sum y).                    (6)
```

This rank-one cross-block structure is the key additional information beyond general4 by4 copositivity.

## 5. Two scalar minima and a controlled cap of the matched edges

Define the attained scalar minima

```
mu=min {x^T Bx:x>=0, sum x=1},
nu=min {y^T Cy:y>=0, sum y=1}.                             (7)
```

Copositivity first gives mu,nu>=0. Taking minimizing x,y and independently scaling them by nonnegative t,s gives

```
mu t^2+nu s^2-2ts>=0 for all t,s>=0.
```

Neither minimum can be zero: with the other scale fixed, sending its scale to infinity would make the displayed expression negative. Consequently

```
mu>0, nu>0, mu nu>=1.                                    (8)
```

For example, setting s=1,t=1/mu gives the last inequality. The endpoint choices in (7) imply d0,d1>=mu and d2,d3>=nu.

There is no hidden multivariable solve in these minima. For a2 by2 matrix with diagonal entries p,q and off-diagonal b, its simplex minimum is

```
min(p,q),                          if b>=min(p,q),
(pq-b^2)/(p+q-2b),                 if b<min(p,q).          (9)
```

The second branch has positive denominator and its stationary point `(q-b)/(p+q-2b)` lies in(0,1); the first branch has its minimum at an endpoint (including the constant case). This follows by expanding the one quadratic in t. Definition(7) is enough for the proof; (9) makes the prescription explicit in the original coefficients.

Set

```
g0=sqrt((d0-mu)(d1-mu)),
h0=min(b0,mu+g0), n0=b0-h0,

g1=sqrt((d2-nu)(d3-nu)),
h1=min(b1,nu+g1), n1=b1-h1.                               (10)
```

All roots are of nonnegative numbers. We prove the needed bounds without assuming any of the factors is nonzero.

By definition of mu, `B-mu J` is copositive. A real2 by2 matrix with nonnegative diagonal A,D is copositive iff its off-diagonal is at least `-sqrt(AD)`: sufficiency is the identity

```
A u^2+2buv+D v^2
 =(sqrt(A)u-sqrt(D)v)^2+2[b+sqrt(AD)]uv,
```

and necessity follows by choosing the nonnegative ratio that cancels the square, or taking a limit when a diagonal entry vanishes. Therefore

```
b0>=mu-g0, b1>=nu-g1.
```

Together with (10), this yields

```
mu-g0<=h0<=mu+g0,
nu-g1<=h1<=nu+g1.                                        (11)
```

It follows by the2 by2 determinant criterion that

```
Bhat=[d0 h0;h0 d1] >=mu J,
Chat=[d2 h1;h1 d3] >=nu J.                               (12)
```

The discarded amounts satisfy the crucial coefficient control

```
0<=n0=max(0,b0-mu-g0)<=max(b0,0)<=c_01,
0<=n1=max(0,b1-nu-g1)<=max(b1,0)<=c_23.                   (13)
```

Here b=c-1 and c>=0, so the last inequalities include c=0. This bound is what permits a positive partially-transposed remainder; arbitrary PSD-plus-entrywise-nonnegative decompositions of K would not suffice.

## 6. An explicit PSD coherent block

Define

```
P0=[Bhat -J; -J Chat].                                   (14)
```

It is PSD, because

```
P0=diag(Bhat-mu J,Chat-nu J)
   +[mu -1;-1 nu] tensor J.                              (15)
```

The first summand is PSD by (12). The scalar2 by2 matrix is PSD by (8), and J is PSD, so the second summand is PSD. Thus no abstract copositive-cone classification is imported.

Embed it into the physical coherent subspace:

```
P_coh=sum_ij (P0)_ij |ii><jj| >=0.                        (16)
```

Its diagonal entries are d_i. Its matched off-diagonals are h0,h1, and its four unmatched off-diagonals are -1.

## 7. Positive pair blocks and the full decomposable identity

For a matched edge e={i,j}, let n_e be n0 or n1, c_e=sqrt(a_ij a_ji), and define

```
T_e=a_ij P(ij)+a_ji P(ji)
    -(c_e-n_e)(|ij><ji|+|ji><ij|).                       (17)
```

The2 by2 matrix of T_e on span{ij,ji} has nonnegative diagonals and determinant

```
a_ij a_ji-(c_e-n_e)^2=c_e^2-(c_e-n_e)^2>=0,
```

by0<=n_e<=c_e. Hence T_e>=0, including zero coefficient/zero determinant boundaries.

Let

```
D_unmatched=sum_(i!=j, {i,j} not in M) a_ij P(ij)>=0.
```

Then the exact operator identity is

```
W(a)=P_coh+D_unmatched+T_01^Gamma+T_23^Gamma.              (18)
```

Every coefficient group can be checked directly:

- On ii the coefficient is d_i=a_ii-1, supplied by P_coh, exactly matching W.
- On an unmatched coherent pair ii/jj, P_coh contributes -1 and no other term contributes.
- On matched pair ii/jj, P_coh contributes `h_e=c_e-1-n_e`; T_e^Gamma contributes `-(c_e-n_e)`. Their sum is **-1**.
- On an off-diagonal product position ij, the diagonal coefficient a_ij is supplied by T_e if matched and by D_unmatched otherwise.
- No operator above has any other matrix entry.

Thus (18) is precisely (T), with `P=P_coh+D_unmatched>=0` and `Q=T_01+T_23>=0`. The construction is explicit through (7)–(10), or the closed scalar formula(9). It uses no scientific computation and no large finite certificate.

For any PPT state rho, therefore,

```
Tr(W rho)=Tr(P rho)+Tr(Q rho^Gamma)>=0.                   (19)
```

This concludes the whole-class no-detection theorem for arbitrary tested PPT states. In map language it says every two-positive D-type map on M4 in this coefficient convention is decomposable. The Choi/map equivalence is only terminology; the operator identity itself proves the physical statement.

## 8. What is settled in the route, and the actual remaining primary gap

The original witness-side plan had two coupled obligations: universal complex H_a(U)<=1 and a negative PPT Gram objective F_a(r). Equation(18) shows that satisfying the first makes the second impossible in this class. The weaker v1 absolute-Gram and diagonal-dominance barriers remain valid but are no longer the operative frontier; there is no reason to add more controls or coefficient subfamilies inside this now-closed route if the proof is accepted.

The exact dimension-four restriction is not cosmetic: the proof uses TWO rank-one2 by2 coefficient blocks, whose union still has Schmidt rank at most two, and the resulting two scalar simplex minima. A larger rank-one block cannot in general minimize every pair energy independently; replacing two2 by2 blocks by a2-plus3 partition would not justify the same matching inequality. No claim for arbitrary dimension, arbitrary negative part, or every two-positive M4 map follows.

The literal x1111 input is already retired only through the parent's accepted37-term proof in `ame-twoF-ppt-small-phase-parent-v1.md` Section2. Its old21-table is still NOT_RECONSTRUCTED, native N4 remains UNKNOWN/incomplete with child exit unestablished, and no retry follows. This consolidation does not add another x1111 certificate.

**Unrestricted P44 remains unanswered.** A genuinely useful next state/separator attack must escape the full diagonal-minus-a-single-Bell-projector D-type class, not merely change the coefficient matrix, its symmetry, its filter or its rational denominators. A source-valid full theorem for all two-positive M4 maps would also suffice, but none was located or established by this bounded screen. This packet supplies no different explicit PPT/SN3 state and is not the user's full-target acceptance.

Correctness: complete author-WRITTEN candidate, independent reconstruction pending. Source trust: bounded primary-section comparison as above; no whole-literature priority claim. Novelty/significance: UNCLEAR. Formal/kernel, finite scientific execution, cross-vendor/human review and publication acceptance: NOT_PERFORMED. The scientific HOLD remains binding; no GO is requested.
