# Higher-kernel v1 — all-rank phase-integrality obstruction and an exact rank7 method control

Actual clock observed before creation: **2026-10-23T15:17:04-07:00**. PhysicsRQLS10. Written continuation of the actual noncommuting conference-gluing problem. No scientific executable, enumeration, numerical check, formal kernel or outside-model CLI ran. The prepared5040-core assay is still unrun and unadmitted.

**CANDIDATE WRITTEN PARTIAL.** Part A gives a necessary arithmetic obstruction for **every** kernel dimension, without fixing a finite phase alphabet. Part B proves that the already obtained abstract Schur/residue properties alone cannot exclude all higher-dimensional complex phases: a rank7 nonphysical control satisfies them and has unit phases. The control is expressly **not** an actual Paley core pair or QLS witness. The next scientific ingredient must use the actual fixed unit-coefficient/rook structure, not pretend this abstract limit is a solved target.

## A. All-rank obstruction: no simultaneously7-integral phase ratios

### A1. Normalize only an irrelevant common phase

Let rho have exactly one fixed point a; this covers every orientation of cyclic10's local inversion. Retain arbitrary P and the true coefficient matrix

    M_(i,t)=conjugate(C_(t,i)) C'_(t,rho(i)),
    C'=PCP^T.

A phase solution delta has |delta_t|=1. Divide by the common nonzero phase delta_a and write z_t=delta_t/delta_a. This preserves Mz=0 and all moduli, and z_a=1. No relative phase is removed.

Put s=i sqrt7 and work over

    R7=Z_(7)[s],      s²=-7,

where Z_(7) permits rational denominators not divisible by7. Its quotient by(s) is F7. M has entries in R7, and its reduction is the exact N_rho of the earlier manuscripts.

### A2. The fixed-point row identity forces1/s into the phase ring

The column sums of N_rho are8 at a and7 at every other coordinate. Therefore

    1^T N_rho=e_a^T    over F7.

Let c_t=sum_i M_(i,t). Since the reduction kernel is precisely(s), there are r_t∈R7 with

    c_t=[t=a]+s r_t.

Multiplying Mz=0 by the all-ones row and using z_a=1 gives

    0=1+s sum_t r_t z_t,
    1/s=-sum_t r_t z_t.                                  (A)

This exact consequence holds for every relative P, not just the commuting ones, and for phases arbitrary in C.

### Theorem INT

The nine normalized phase ratios cannot all be integral over R7. In particular **no root-of-unity compatibility-phase alphabet of any order can work** for these local core/matching hypotheses.

**Proof.** Suppose each z_t is integral over R7. The ring A=R7[z_0,...,z_8] is a finite R7-module: powers of each generator reduce by a monic integral relation, so finitely many products span the ring. It contains R7 faithfully as a subring of C. Equation (A) says1∈sA, hence A=sA.

Choose finitely many R7-module generators b_1,...,b_m of A. Since A=sA, there is an m×m matrix B over R7 with

    b_i=s sum_j B_ij b_j.

The adjugate identity shows `det(I-sB)` annihilates every generator, hence all A and its element1. Thus det(I-sB)=0 in A, and therefore in R7. But its reduction modulo(s) is1, contradiction. This is the finite-module determinant trick, written here to avoid assuming a descent theorem for arbitrary torus points.

Every root of unity satisfies a monic polynomial T^N-1 over Z, so is integral over R7; ratios of roots of unity are again roots of unity. The asserted alphabet exclusion follows. QED.

The same proof excludes algebraic phase ratios all simultaneously integral at7, including ones obtained from algebraic integers using rational denominators coprime to7. It does **not** exclude arbitrary algebraic/nonintegral or transcendental phases. A common scalar does not evade the theorem because the normalization z_a=1 was made first.

### A3. Why unit modulus is not an integrality theorem

For example

    z=(3sqrt21+i sqrt7)/14

has |z|=1, but

    z-conjugate(z)=i sqrt7/7=-1/s.

Thus a ring containing both z and its inverse/conjugate can contain1/s. Complex unit phases can genuinely escape7-integrality. The theorem therefore cannot be promoted to unrestricted phase impossibility merely by saying that all phases have modulus1.

## B. A rank7 control showing exactly what the abstract Schur line still lacks

This construction uses **nonphysical coefficient matrices**, not a second target or an actual residual Paley core. It isolates the logical gap in a potential proof using only residue, rank and symmetry properties.

### B1. The retained abstract properties

Use the even/odd coordinate decomposition of rho(t)=-t. An even vector has coordinates x0 and four pair means x_j; an odd vector has four pair differences y_j. The physical vector is

    delta_0=x0,
    delta_(r_j)=x_j+y_j,
    delta_(-r_j)=x_j-y_j.

The even basis has metric `G=diag(1,2,2,2,2)`; the odd basis has metric2I. The exact even reduction N|even is the rational matrix

    A=[0 2 2 2 2]
      [1 0 2 2 2]
      [1 2 0 2 2]
      [1 2 2 0 2]
      [1 2 2 2 0].

A is invertible over Q and modulo7; the direct sum and pair equations prove this as in the earlier notes. Also GA=A^T G.

Define

    T=[0 -1  1  0]
      [1  0  0 -1]
      [1 -1  0  0]
      [1 -1  0  0],

let B be the5×4 matrix with first row zero and remaining rows sT, and put

    C0=-(1/2)B^T G,
    M_fake=[ A   B ]
           [ C0  0 ].                                      (F)

All coefficients lie in K=Q(s). In physical coordinates it has precisely the required zero diagonal and zero inversion-pair positions: A_jj, B_jj, C0_jj and the odd diagonal block are all zero, and A00=0. Every remaining physical entry has real part1 and is nonzero. Its reduction modulo s is exactly N_rho. The weighted transpose identity makes `P_rho M_fake` symmetric, just as for the true core matrices. Thus the even-block/rank-floor, zero-mask, transpose-symmetry and residue facts by themselves are all retained.

### B2. Its actual rank is7

For a vector [0;w], solving A x=[0;w] gives

    x0=(sum_j w_j)/4,
    x_vector=(sum_j w_j)1/8-w/2.

Using this inverse formula, the Schur complement of(F) is

    -C0 A^-1 B = (7/2) T^T(I-J4/4)T.                      (S)

T has rank3: its first three rows are independent and the fourth repeats the third. Its image contains1, since `T(1,0,1,0)^T=1`. Projection by `I-J4/4` therefore has rank2 on its image. The real Gram matrix in(S) has rank2. Consequently M_fake has rank5+2=7 over K and C.

### B3. It has exact unit complex phases outside projective K

Take

    z=(3sqrt21+s)/14,       conjugate(z)=(3sqrt21-s)/14,
    y=(z,conjugate(z),z,conjugate(z))^T,
    x=e0.

The two displayed phases have modulus1, and their difference is s/7. Therefore

    Ty=(s/7)1,
    By=s*[0;Ty]=-[0;1]=-A e0,
    C0 e0=0.

So M_fake[x;y]=0. Its physical coordinates are1 and the four pairs±y_j, all of modulus1. This is a genuine **complex** higher-kernel unit-phase solution of the abstract model. Its irrational real part shows why projective-K one-dimensional descent does not apply. The exact7-denominator also accords with Theorem INT.

### B4. The control is not an actual Paley pair

The actual M coefficients are all0 or unit complex numbers from{1,w²,w^-2}. The control violates that **specific coefficient constraint**. For example its physical entry at(r1,r2) is

    1+(s/2)(T12-T21)=1-s,

whose squared modulus is8, not1. Therefore it is **not** of the form `conjugate(C_(t,i))*C'_(t,-i)` for genuine conference cores. It is neither a local ONB triple nor an H0/QLS10 witness, and its existence does not refute a possible stronger Paley-specific no-go.

What it does prove is precise: a universal rank5–7 closure cannot be inferred from the already obtained abstract block invertibility, residue, weighted symmetry and zero masks alone. It must use the true unit-modulus coefficient alphabet and its discrete rook/character structure, or further conference-modulus conditions. Those conditions are not discarded in the primary problem.

## C. Exact remaining obligation

The actual rank5–7 Paley matrices, if any, must either have a forced-zero phase coordinate, fail the exact unit-modulus equations, or require a genuinely nonintegral extension-phase mechanism satisfying all remaining conference moduli. No such actual survivor has been evaluated or exhibited. The second-order note closes one real noncommuting core orbit, not all others.

All findings here are author-written CANDIDATE pending separate reconstruction and parent review. No integral-phase exclusion is silently enlarged to all complex phases, and no method control is counted as scientific closure. The source-pinned assay is still unrun; no control, source import, target rank, norm or test has executed. The maximal-cardinality1-RQLS(10) primary target remains UNKNOWN.
