# Two-rook-pair closure v1 — the fixed-first-core/central-inversion gluing route closes in writing

Actual clock observed before creation: **2026-10-23T15:38:39-07:00**. PhysicsRQLS10. Written mathematical continuation; no scientific program, exact executable calculation, enumeration, numerical search, solver, formal kernel or outside-model CLI ran.

**COMPLETE AUTHOR-WRITTEN CANDIDATE FOR THE SPECIFIED LOCAL ROUTE.** This closes the actual k=2 residual of the previously prepared5040-core question. The difficult perpendicular class has **actual rank7**, but its entire complex kernel has fixed coordinate zero. The parallel exceptional class closes at second order. Together with the earlier signature/duality papers, this yields no phase gluing for any second core P at the **fixed first Et-Taoui core and rho(t)=-t on its same field labels**. It is NOT every first orientation, every conference class, H0 generally, or unrestricted maximal1-RQLS(10). No acceptance, novelty or solved-book claim is made before actual reconstruction/parent review.

## 1. Exact retained scope and algebra

Take GF(9)=F3[alpha]/(alpha²+1), chi its quadratic character, the literal first core C, and rho(t)=-t. The second character matrix is `Q'=PQP^T`, arbitrary P. Choose a representative p fixing0 by a second-grid translation, which leaves Q' unchanged. Every independent diagonal compatibility phase is retained; a physical gluing requires

    M delta=0,          |delta_t|=1,
    M_(i,t)=conjugate(C_(t,i)) C'_(t,-i).

Put s=i sqrt7 and H=P_rho M. H is symmetric. Its exact expansion is

    H=N+sH1+s²H2,
    N=J-I-P_rho+Fix(rho),
    H1=(Q'-P_rho Q-D'P_rho+D0)/8,
    H2_(i,t)=[1-Q'_(i,t)Q_(-i,t)]/8
               on t!=i,-i, and0 otherwise,

where D0=diag(Q_(i,-i)) and D'=diag(Q'_(i,-i)), with fixed diagonal entry0. H2 is0 or1/4 on each allowed position. In particular

    H2=4(H1 Hadamard H1)                                 (C)

entrywise, including masked zeros. This exact curvature relation is essential; the nonphysical rank7 method control did not satisfy it.

Use pair representatives r1=1,r2=alpha,r3=1+alpha,r4=1-alpha. On the four pair coordinates,

    D0=diag(1,1,-1,-1),
    A0=2*[0 0 1 1;0 0 1 -1;1 1 0 0;1 -1 0 0],
    O0=-D0+A0.

The first even pair block E0 has diagonal D0 and only off-diagonal entries E0_12=-2,E0_34=+2. The even5×5 block A of N is invertible over Q and modulo7. All odd pair bases here are **unnormalized differences**, with metric2I; the even metric is G_E=diag(1,2,2,2,2).

Let E',O',B_Q be the even-even, odd-odd and even-odd blocks of the real Q'. Then

    O'=-D'+A',
    (1/2)B_Q^T G_E B_Q=9I-O'^2.                          (Q2)

This follows from Q'^2=9I-J and real symmetry. It is auxiliary real character-matrix algebra, not a restriction of the sought physical phases to R.

### Retained first- and second-order tests

The first odd coefficient of H is `(A0+A')/8`. Rank at least3 modulo7 forces actual rank M≥8, which excludes all arbitrary complex phases by the earlier rank8 norm-descent theorem.

For a reduced first-order kernel, its second-order **physical bilinear form** in odd pair coordinates is

    G2=2(H2|odd)-F,
    F=B1^T G_E A^-1 B1,
    B1=B_Q/8.

The previous positive-pair proof, using Q'1=0 and(Q2), gives uniformly over all relative P

    F=-(9I-O'^2)/64   modulo7,
    H2|odd=(O0 Hadamard E'_pair
                  -E0 Hadamard O')/16.                  (S2)

The first formula does not discard the variable mixed block: it eliminates it using the exact real character identities. These formulas retain the rational pair-basis metrics.

## 2. Complete geometry of the two-rook-pair signature

Assume exactly two of the four paired edges in the second grid are rook edges. The other two are diagonal pairs. Each pair's off-diagonal inner products are computed from its row/column difference vector in A2⊕A2, exactly as in the previous signature papers.

### 2.1 The two rook pairs are parallel

Suppose both are vertical; the horizontal case is coordinate-dual. They must be in columns1 and2. If one were in column0, the remaining column with three points would need three diagonal partners, but there are only two diagonal edges.

Let a,b be the unused row levels in columns1 and2. The diagonal pairs join the two column0 points to these two leftovers, say

    D1={(0,r),(1,a)},    D2={(0,-r),(2,b)},   r!=0,

with a!=r,b!=-r. Thus

    a in{0,-r},       b in{0,r}.

The four possibilities, with arbitrary orientations and labels, give these A' shapes:

- a=b=0: complete K4 with two disjoint magnitude2 edges (rook-rook and diagonal-diagonal), and four magnitude1 cross edges;
- exactly one of a,b is0: a diamond (K4 minus one edge), with exactly one magnitude2 edge and four magnitude1 edges;
- a=-r,b=r: complete K4, all six magnitudes1.

These follow directly from the A2 roots. For the first case one may choose roots V1=V2=e1-e2 in y, D1=(e0-e1) in x plus(e1-e0) in y, D2=(e0-e2) in x plus(e2-e0) in y. Their off-diagonal products are2,2 and±1 as claimed. For the mixed case the diagonal-diagonal x/y products cancel, leaving the diamond. In the last case the two contributions to that product are1 and-2, giving magnitude1; every other product is between distinct A2 directions.

A complete graph with all weights1 leaves every A0 cross edge nonzero and has a triangle. A diamond with only one magnitude2 edge also leaves a triangle: if its missing edge is within an A0 side, avoiding both triangles on the opposite-side nonzero edge needs two distinct cross cancellations; if its missing edge is across A0, avoiding the two triangles containing that unchanged cross edge again needs two. Only one magnitude2 edge is available. Thus these subcases close at first order.

The two-heavy-edge complete graph is treated in §3.

### 2.2 One horizontal and one vertical rook pair

Call them H,V. If H is in row0 and V in column0, the diagonal pairs are uniquely the two opposite pairs of the remaining2×2 square. The matching is literal point inversion in the second grid; Q' commutes with rho. Its arbitrary-phase gluing is excluded by the earlier commuting-core averaging theorem.

If H is in row0 and V in column1 or2, the remaining diagonal pairs are the unique nonrook pairing of a2×2 rectangle. The analogous case with V in column0 is coordinate-dual. Call this **Type A**. A' is K2,2 between{H,V} and{D1,D2}; one rook vertex has two magnitude2 incident edges, and the other has two magnitude1 edges. The signed cross2×2 block has negative cycle product. The actual rank7 argument is in §4.

For completeness suppose H is in nonzero row r and V in nonzero column c. Write H's omitted column as a and V's omitted row as b. Disjointness requires a=c or b=r; otherwise both use their intersection(c,r).

- If a=c,b=r (both omit the intersection), the unique diagonal completion has a weighted K2,2 A' of the same1/2 pattern, but its heavy vertex is a **diagonal** pair. Call this **Type B**.
- If a=c,b=0, or coordinate-dually b=r,a=0, the completion gives a diamond with exactly one magnitude2 edge. These close by the same triangle argument above.
- The alternatives a=c,b=-r or b=r,a=-c leave three of the four unpaired points in one row or column; two diagonal edges cannot cover them. They are impossible.

To check these shapes without an unlisted classification, set r=c=1 using grid coordinate signs. In the both-omit case the diagonal edges are{(0,2),(2,0)} and{(2,2),(1,1)}; their A2 products give a weighted K2,2 with heavy diagonal vertex. In the one-omit case H={(0,1),(2,1)}, V={(1,1),(1,2)}, and the diagonals are{(1,0),(2,2)},{(2,0),(0,2)}. Their A' is a diamond with its only magnitude2 edge between H and the second diagonal. Arbitrary labels/orientations change signs but not the argument.

The exact complement/conjugation duality sends Type A to Type B: it preserves all A' magnitudes and support, while exchanging rook and diagonal pair tags, so changes which type of vertex is heavy. The complete list above has no other such weighted-K2,2 shape. It suffices to close Type A in both placements relative to the first A0 sides.

This exhausts the signature. As a coverage consistency check, there are16 parallel raw matchings and17 perpendicular ones: the latter split as1 central,4 Type A,4 Type B,8 diamond. Their total is33, the independent signature count previously derived.

## 3. Parallel exceptional class: uniform second-order nonsingularity

Its two heavy edges are the rook-rook and diagonal-diagonal edges. If either is within an A0 side, triangles remain because the other four edges have magnitude1. Otherwise the two heavy edges are a cross perfect matching. To avoid a triangle both must cancel the corresponding A0 entries. Literal first-core automorphisms preserving rho move their rook-heavy edge to(1,3), leaving the diagonal-heavy edge(2,4).

The cancellation signs and A2-root products then force

    A'_13=-2,       A'_24=+2,
    A'_12=A'_34=a,  A'_14=A'_23=-a,        a=±1.

For a=-1 the remaining4-cycle has determinant proportional to1-9=-8, nonzero modulo7. Only a=+1 is a first-order failure. Thus its canonical A' is

    A'=[ 0  1 -2 -1]
       [ 1  0 -1  2]
       [-2 -1  0  1]
       [-1  2  1  0],
    D'=diag(1,-1,1,-1).

Its first-order reduced kernel has pair-coordinate basis

    u=(1,0,-1,0),      v=(0,1,0,-1).

For every core in this canonical fiber, second-grid pair averages give E'_13=E'_24=0 and

    E'_12=E'_34=tau,
    E'_14=E'_23=-tau,          tau=±1,

with diagonal D'. The possible sign tau retains the relative average placement of the diagonal pairs; it is not fixed by A'. O'=-D'+A' is fixed and satisfies

    O'u=u+2v,       O'v=2u-v,
    O'^2=5I on span{u,v}.

Therefore the(9I-O'^2) contribution in(S2), paired physically with u,v of norm squared2, has diagonal8 and off-diagonal0. Direct Hadamard substitution gives the other contribution with diagonal0 and cross pairing4tau. Modulo7 the second-order kernel form is

    [1  4tau]
    [4tau  1],

whose determinant is1-16=-15=6 mod7. It is nonsingular for both tau values. The even5 pivots and the two first-order odd pivots followed by these two second-order pivots prove actual M nonsingular, exactly as in the earlier explicit example. Thus all complex phases are excluded in this entire parallel exceptional class, not only a chosen permutation.

## 4. Type A: the actual rank7 kernel is explicit and has no phase vector

### 4.1 Only aligned natural bipartitions can fail the leading test

If{H,V}|{D1,D2} is not the A0 bipartition, L has both nonzero within-side edges and at most one cancellable cross edge: the two cross zero positions of A' are supplied unchanged by A0, its light edge cannot cancel±2, and only one heavy edge is across. A nonzero triangle remains.

If the bipartitions agree, the heavy rook row/column must cancel completely for leading rank to drop. The negative cycle-product condition leaves only the following two canonical placements, with a=±1. First-core automorphisms can interchange the members of either A0 side, retaining every relevant orientation sign.

**Placement +:** rooks at1,2, heavy V at2; diagonals at3,4.

    D'=D0,
    A'_cross=[a  a; -2  2],
    u=e2,           v=e3-e4.

**Placement -:** rooks at3,4, heavy V at4; diagonals at1,2.

    D'=-D0,
    A'_cross=[a -2; a  2],
    u=e4,           v=e1-e2.

Here cross refers to rows{1,2},columns{3,4}. Every other heavy-sign choice gives a nonzero2×2 cross determinant modulo7. For example in Placement + the heavy row has entries0/4 and0/-4 after adding A0; unless both are zero its determinant is nonzero, using the required negative cycle product. The light row remains(2+a,2+a), with2+a=1 or3 nonzero modulo7. Thus the leading odd rank is exactly2 and actual rank M≥7 in the two retained placements.

### 4.2 The first-order kernel vectors are actual first-order kernel vectors

For either displayed placement a direct multiplication gives

    O'u=-u-2v,
    O'v=-4u+v,
    O'^2=9I on span{u,v}.

By(Q2) and positivity of the real character-matrix Gram, `B_Q u=B_Q v=0` **exactly**, not only modulo7. Both u,v also annihilate A0+A' exactly. Therefore the whole H1, not merely its odd projection, kills u,v. N kills them because they are odd.

Since u is the difference within one rho pair, H1's two corresponding columns coincide. Relation(C) makes the H2 columns coincide too. Hence

    H u=0.

This is the use of the genuine unit-coefficient curvature omitted by the abstract method control.

### 4.3 The second vector v is also in the exact kernel

The two diagonal pairs in Type A are the two opposite matchings of the same2×2 rectangle. Their coordinate averages are identical. Consequently the pair rows of B_Q at D1,D2 are identical. Also B_Qv=0 says the two corresponding columns are identical, and B_Qu=0 makes the heavy-rook column zero. The mixed diagonal entries of Q' are zero.

The actual even pair block has diagonal D', plus:

- Placement +: E'_34=2, E'_13=E'_14=-1, other off-diagonal entries0;
- Placement -: E'_12=2, E'_13=E'_23=-1, other off-diagonal entries0.

These average values are unaffected by pair orientation. The odd direct block formula(S2) shows H2|odd kills v: the Hadamard numerator has only equal entries on(1,3),(1,4) in Placement +, or equal entries on(1,3),(2,3) in Placement -, respectively.

For the even/odd mixed part, entrywise pair multiplication gives

    (H2_EO)_ab=[(O0)_ab (B_Q)_ba
                    -(E0)_ab (B_Q)_ab]/16

on pair rows, and at the fixed row the expression is proportional to `-(D0)_b(B_Q)_0b`. Apply this to the difference v of the two diagonal indices. Their first D0 signs are equal, so the fixed-row term vanishes by equality of their B_Q columns.

On pair rows, the remaining possibilities vanish as follows:

- on the light-rook row the two O0 coefficients are equal and the two relevant B_Q rows coincide;
- on the heavy-rook row their O0 difference is4, multiplied by the zero heavy-rook column of B_Q;
- on either diagonal row all surviving terms contain mixed diagonal entries or their identical-column partners, which are zero.

Thus the full even part H2v also vanishes. We have proved

    Hv=0

exactly in K. No coefficient-field assumption has been placed on a potential physical phase vector.

### 4.4 Exact rank and arbitrary complex phase exclusion

The two independent actual vectors u,v give rank M≤7. The leading rank-two odd block and invertible even block give rank M≥7. Therefore rank M=7 and

    ker_C M=span_C{u,v}.

Both vectors are pure odd and have fixed coordinate0 zero. Every complex kernel vector has that coordinate zero, contradicting the required unit modulus there. Thus no phase gluing exists in either Type A placement, even though this class truly has a two-dimensional kernel.

Complement/conjugation duality transports the conclusion to Type B, with all relative phases retained. This closes the actual higher-kernel class; it is not merely ruling out projective K phases or algebraic-integer phases.

## 5. Complete local-route composition and exact limits

All k=2 possibilities are now covered:

1. central matching: commuting-core arbitrary-phase averaging theorem;
2. all-one complete graphs and one-heavy diamonds: first-order triangle rank test plus rank8 exclusion;
3. parallel two-heavy exceptional graphs: uniform second-order nonsingularity;
4. perpendicular weighted K2,2 Types A/B: actual rank7 kernel with fixed coordinate zero.

Earlier papers cover k=4 by first/second order, k=0 by complement duality, k=3 by triangle geometry and k=1 by its duality. Therefore for the literal first Et-Taoui C and rho(t)=-t, **every** second core C'=PCP^T and **all** independent complex phases are excluded from the local triple. The5040 distinct literal second-core inputs of the prepared request are closed by this complete written composition, subject to actual reconstruction/review.

The source/request remain immutable and **UNRUN**; no scientific execution GO has issued or been consumed. This candidate gives the parent a reason to supersede that prepared assay in writing, not a claim that its controls passed or an instruction to delete/restart anything.

Crucial preserved scope:

- rho=-t on the first core's same field labels is an explicit orientation restriction, not WLOG for every cyclic10 core. The other20 safe first-orientation classes are not covered by this composition.
- Other conference9 monomial classes are not classified or excluded.
- H0 is a uniform-overlap ansatz; nonuniform100-ray arrays remain unrestricted.
- No actual maximal1-RQLS(10) witness or unrestricted impossibility follows. No full-book, novelty, kernel/human/cross-vendor or accepted-scientific-closure claim is made.

All subclaims here are author-written CANDIDATE pending an actual separate reconstruction and parent check on pinned bytes. Counts refer to discrete inputs in one local route, not independent theorem/discovery/problem counts. The primary physics-5 target remains UNKNOWN.
