# Noncommuting core structure v1 — exact rank-five floor and four-dimensional phase reduction

PhysicsRQLS10. Written continuation of `candidate-CONFERENCE-GLUING-v1.md` and its symmetry addendum. **No creation timestamp is asserted here.** This is a proof-obligation analysis of the remaining fixed-first-core, rho(t)=-t route, not a new solved-target packet. It uses no executable scientific computation. The prepared exact assay remains unrun and has no execution GO.

## 1. Setup and the noncommuting distinction

Fix the Et-Taoui core C on GF(9), rho(t)=-t and arbitrary `C'=PCP^T`. The coefficient matrix is

    M_(i,t)=conjugate(C_(t,i)) C'_(t,-i),
    M delta=0,                   |delta_t|=1.

The first core C commutes with rho. C' is **not** assumed to commute with rho in this note. Thus averaging an arbitrary kernel vector is not licensed. The source's fixed-first-core/oriented-rho restriction is retained; it is not WLOG for every cyclic10 orientation.

Let E and O be the even and odd coordinate spaces for t→-t:

    E={x:x_t=x_-t}, dim E=5,
    O={y:y_t=-y_-t}, dim O=4.

Use e0 and the four pair sums as an E basis, and four pair differences as an O basis. All changes of coordinates use only1/2 and integers, which are allowed in the ring R=Z[1/2,i sqrt7].

## 2. A block that stays invertible even without symmetry

Write M, with input/output decomposed as E⊕O, as

    M=[ A  B ]
      [ C0 D ],

where A is the **projected** E-to-E block. Unlike the symmetry addendum, M itself need not preserve E.

### Lemma A5

For every relative permutation P, A is invertible over Q(i sqrt7), hence over C. In particular rank M≥5 and dim ker M≤4.

**Proof.** Reduction modulo the prime i sqrt7 sends M to

    N=J-I-P_rho+Fix(rho),

independently of P. This N commutes with rho. Its E restriction is invertible over F7: if x is even and Nx=0, write S=sum x_t. The fixed coordinate satisfies x0=S; each of the other four coordinate pairs has value S/2. Hence

    S=S+8*(S/2)=5S,

so4S=0 in F7, and S=0, then x=0. The projected block A has coefficients in R, and its reduction in the fixed even basis is exactly this restriction. Thus det A has nonzero reduction and is nonzero over C. A rank-five invertible block forces rank M≥5. QED.

This statement covers all noncommuting P; it does not invoke their finiteness or enumerate them. It gives the analytic rank floor behind the prepared assay's possible kernels.

## 3. The Schur complement is symmetric, not an arbitrary four-by-four system

Let P_rho denote the real involution matrix. Since C and C' are symmetric and C commutes with rho,

    P_rho M = (conjugate(C) P_rho) Hadamard C'

is symmetric. Indeed its (i,t) entry is `conjugate(C_(t,-i)) C'_(t,i)`, symmetric in i,t because C commutes with inversion and both cores are symmetric. Therefore

    M^T=P_rho M P_rho.

In E⊕O coordinates (using normalized orthogonal pair-sum/difference bases if desired), this says A and D are symmetric and C0=-B^T. The normalizations require only the same fixed nonzero real pair factors and do not change any kernel conclusion.

The kernel is thus parametrized by

    x=-A^-1 B y,
    (D+B^T A^-1 B)y=0.                                    (S4)

The remaining Schur complement is a symmetric4×4 matrix over Q(i sqrt7). This is a genuine noncommuting structure constraint. It is not a proof that its determinant is nonzero, and a complex-symmetric matrix is not positive semidefinite merely because it is symmetric.

## 4. Retaining the exact unit-phase constraints

Choose representatives r1,...,r4 of the four nonzero pairs {t,-t}. Without normalized pair factors, write the coordinates as

    delta_0=x0,
    delta_(rj)=xj+yj,
    delta_(-rj)=xj-yj.

The full compatibility-phase condition is **exactly**

    |x0|²=1,
    |xj|²+|yj|²=1,
    Re(xj conjugate(yj))=0,          j=1,...,4,             (U)

together with the Schur kernel equations and `x=-A^-1 B y`, with the consistent basis scaling. The last two identities are obtained by adding and subtracting `|xj+yj|²=|xj-yj|²=1`.

In particular y cannot vanish. If r is the row of `-A^-1 B` producing x0 in this unnormalized pair basis, a necessary condition is

    1=|r y| ≤ sum_j |r_j|,

because |yj|≤1. Also Cauchy–Schwarz gives `||r||²≥1/4`. These are fixed-core/P necessary bounds, not claims that either bound holds or fails uniformly in P.

The commuting-core theorem is recovered honestly: B=0 then x=0, contradicting |x0|=1. In the noncommuting case B can carry a nonzero fixed-coordinate amplitude, so the symmetry proof cannot simply be reused.

## 5. A one-dimensional survivor can be resolved exactly, without numerical phase search

Suppose an actual retained matrix M has rank8. Its kernel has a basis vector v with entries in K=Q(i sqrt7). Every kernel vector is delta=lambda v. A unimodular delta exists for the **zero equations alone** iff

    N(v_0)=N(v_1)=...=N(v_8)>0,
    N(a+b i sqrt7)=a²+7b² in Q.                            (K1)

**Proof.** Necessity follows from `|lambda|² N(v_j)=1` for every j. Conversely equal positive norms permit any lambda with modulus the reciprocal square root of that norm. No phase rounding is involved. QED.

This decides only the nine required zeros, not the full local H0 triple. For a genuine conference B/D transition one must additionally check every remaining entry of `C* diag(delta) C'/8` has squared modulus1/8. If delta=lambda v and c=N(v_j)>0 is common, put

    L_ij(v)=sum_t conjugate(C_(t,i)) v_t C'_(t,j).

Every L_ij(v) lies in K. The remaining local condition is the finite exact set

    N(L_ij(v))=8c,         j!=rho(i).                       (K2)

Indeed `|lambda|²=1/c` and the transition has denominator8, so its squared modulus is `N(L)/(64c)`.

Thus a rank8 survivor is not a reason to start a float search. Exact rational norm comparisons (K1), then (K2), suffice for this **local zero/modulus** question. They still would not complete the other cells of a100-ray square. Rank≤7 survivors have larger complex kernels and retain the exact quadratic torus conditions (U); no finite phase list is asserted for them.

## 6. Current scientific boundary

The analytical symmetry exclusions do not yet supersede the prepared arbitrary-second-P assay: A is always invertible, but the noncommuting4×4 Schur complement need not be. The precise unresolved input is whether any of those actual kernels supports (U), and then the remaining local conference moduli, not whether an arbitrary PSD H0 exists.

All statements here are author-written and need actual separate reconstruction before acceptance. The exact assay is only prepared; no control, target elimination, norm comparison or computation has been executed. No claim of novelty, H0-wide exclusion, full cyclic10 result or unrestricted 1-RQLS(10) solution.
