# Four-rook-pair closure v1 — a complete noncommuting core class is excluded in writing

Observed before creation: **2026-10-23T15:24:20-07:00**. PhysicsRQLS10. Written continuation of the actual fixed-first-core/central-inversion conference-gluing problem. No scientific executable, enumeration, numerical check, solver, formal kernel or model CLI ran.

**CANDIDATE WRITTEN PARTIAL.** This excludes **every** relative core for which all four inversion pairs are rook edges in the second Paley grid, under arbitrary complex compatibility phases. It closes the whole structural class behind the earlier second-order example, not just that one permutation. The class consists of384 distinct literal second-core character tables, not384 separate scientific problems or discoveries. Other classes, orientations and the unrestricted QLS10 target remain open.

## 1. Fixed setup and the first-order criterion

Use GF(9)=F3[alpha]/(alpha²+1), rho(t)=-t, and pair representatives

    r1=1, r2=alpha, r3=1+alpha, r4=1-alpha.

Q is the first Paley character matrix and Q'=PQP^T is arbitrary. Put C'=PCP^T. The actual coefficient matrix is M_(i,t)=conjugate(C_(t,i))C'_(t,-i). The even5×5 block of H=P_rho M is invertible modulo s=i sqrt7. Its odd first-order block is proportional to

    L=A0+A',
    A0=2T0,
    T0=[0 0 1 1; 0 0 1 -1; 1 1 0 0; 1 -1 0 0],

where A' has zero diagonal and, for a≠b,

    A'_ab=[Q'_(r_a,r_b)-Q'_(r_a,-r_b)
            -Q'_(-r_a,r_b)+Q'_(-r_a,-r_b)]/2.

The factor1/8 and any fixed odd sign do not affect reduced rank. Rank(L)≥3 over F7 forces actual rank(M)≥8, excluding all complex phases by the written rank8 norm-descent theorem. A singular leading reduction is not itself an actual low-rank certificate.

### Class hypothesis RP

Every pair {p(r_j),p(-r_j)} is a rook edge in the second3×3 grid, for j=1,...,4; equivalently Q'_(r_j,-r_j)=+1. Thus D'=I on the four nonfixed pairs. No phase or physical-array symmetry is assumed.

## 2. Complete geometric classification of RP

The four disjoint pairs cover all grid points except0. Each rook edge is horizontal or vertical. Let h be the number horizontal.

- h=0 or4 is impossible: the two full nonzero rows/columns have odd size3, so cannot all be paired internally.
- h=1 or3 gives three edges in one direction and one in the other. The three same-direction difference roots have pairwise nonzero dot products; their A' support is a triangle, while the other direction is isolated.
- h=2 gives two horizontal edges in distinct rows. To leave even column counts for the two vertical edges, the horizontal edges must lie in the two rows not containing0, each using the0-column and a different remaining column. The two horizontal difference roots have dot product±1; the two vertical roots also have dot product±1; cross-direction products vanish. Thus A' is a signed matching of two disjoint edges, each of weight±1.

Here the dot-product assertion is exact: since `Q'=2Adj-(J-I)` on distinct grid points, the alternating four-entry expression defining A' cancels the constant part and equals the dot product of the pair's row/column difference vectors `e_x-e_x'` and `e_y-e_y'` in A2⊕A2. For h=1/3, a shared-direction root can repeat or be another A2 root; inner products are±2 or±1, never zero. This classification retains every orientation and pair label.

### Triangle case: immediate first-order closure

T0's support is a complete bipartite4-cycle with sides{1,2} and{3,4}. If A' is a triangle plus isolated vertex, the triangle contains two vertices on one side and one on the other. The isolated vertex is on the latter side. Its two T0 edges to those two triangle vertices are nonzero and unchanged by A'; the edge between those two vertices comes from A' and is nonzero. Therefore L contains a nonzero triangle. Its3×3 principal minor is twice the product of three nonzero entries, nonzero modulo7 (all weights have magnitude1 or2). Hence rank(L)≥3 and no phase solution exists.

## 3. Two-edge case: all leading failures are one first-core symmetry type

If A' matches the two zero positions(1,2),(3,4) of T0, its added edges again give a nonzero triangle, so it closes immediately.

Otherwise A' occupies a cross perfect matching. For edges(1,3),(2,4), let their signs be epsilon,eta∈{±1}. The cross block of L is

    X=[2+epsilon   2]
      [    2    -2+eta].

Its determinant is-7,-13,-5,-7 for(epsilon,eta)=(+,+),(+,-),(-,+),(-,-), respectively. Thus the leading reduction fails only when epsilon=eta. The other cross matching(1,4),(2,3) fails only with opposite signs. All four failed sign patterns are literal first-core automorphism images of the canonical pattern

    A'_13=A'_24=-1,     other off-diagonal entries0.       (CAN)

For example the norm-preserving field rotation(x,y)→(-y,x) sends the canonical two negatives to two positives at(1,3),(2,4). The reflection(x,y)→(-x,y) sends it to opposite signs at(1,4),(2,3); their composition supplies the fourth pattern. These transformations preserve Q and rho, so transport all phase equations exactly. It remains to close every Q' with(CAN), not assume that A' determines the entire core.

## 4. The second-order form is uniform over the canonical fiber

The metric in the unnormalized pair basis is G_E=diag(1,2,2,2,2) on even coordinates and2I on odd coordinates. Let E' and O' be the even/odd diagonal blocks of Q'; let B_Q be its even-to-odd input block. All following reductions are modulo s, i.e. over F7, with denominators powers of2 invertible.

### 4.1 The diagonal blocks of Q' are fixed by RP and(CAN)

For h=2,v=2, every pair has one neighbor and one nonneighbor of the missing point0. Therefore the fixed-point row/column of E' is zero. On its four pair coordinates,

    E'_pair=I+A',          O'=-I+A'.                       (B)

The diagonal entries are+1 and-1 because every pair is a rook edge. Between the two horizontal pairs, or the two vertical pairs, the four Q' entries sum to-2, so their even entry is-1. Mixed-direction even sums are zero. These are exactly the matching edges in(CAN). The odd entries are A' by definition. The mixed block B_Q may vary; it is **not** assumed fixed or zero.

### 4.2 Its variable mixed block has a fixed feedback form modulo7

The first-order even coupling of H is B1=B_Q/8, because the first Q and its masked diagonal terms commute with rho. Let A=N|even. For two even coordinate vectors h,k, the direct inverse of A gives

    h^T G_E A^-1 k
      =[(h0+sum h_j)(k0+sum k_j)]/4
          -h0k0-sum h_jk_j.

Since Q'1=0, every column of B1 obeys `h0+2sum h_j=0`. Substituting yields

    F:=B1^T G_E A^-1 B1
       =-(1/2)B1^T G_E B1 -(7/16)b0^T b0,

where b0 is B1's fixed-coordinate row. On reduction the last term vanishes. Symmetry of Q' and `Q'^2=9I-J` give

    (1/2)B_Q^T G_E B_Q=9I-O'^2.

Therefore

    F=-(9I-O'^2)/64    modulo7.

Under(B), A'^2=I, so `O'^2=2I-2A'`, and consequently

    F=-2A'    modulo7.                                   (F)

This is why the variable compatibility/mixed data do not require separate cases here. No core symmetry has been imposed.

### 4.3 The direct second-order odd block is fixed too

Let E0,O0 be the first Q's even/odd diagonal blocks on the four pair coordinates. For H=N+sH1+s²H2, entrywise multiplication of the two-by-two pair blocks gives

    H2|odd=(O0 Hadamard E'_pair
               -E0 Hadamard O')/16.                     (D)

The two nonzero entries for(CAN) are

    (H2|odd)_13=-1/8,      (H2|odd)_24=+1/8,

and their symmetric counterparts; its other entries are zero. In particular this block depends only on the diagonal blocks(B), not on the unretained mixed block.

### 4.4 The two remaining reduced pivots are nonzero

The reduced first-order kernel for(CAN) has pair-coordinate basis

    u=(-2,1,0,0),           v=(0,0,-2,1).

The second-order **bilinear form** in physical coordinates is

    G2=2(H2|odd)-F,

the factor2 being the odd-basis metric. From(D),(F),

    u^T G2 u=v^T G2 v=0,
    u^T G2 v=v^T G2 u=5    in F7.

For instance the(1,3) entry of G2 is `-1/4-2=3 mod7`, while the(2,4) entry is `1/4-2=0`; the cross pairing is(-2)*3*(-2)=12=5. Thus the reduced kernel form is[0,5;5,0], determinant3 modulo7.

The even block supplies five unit pivots. Two odd pivots occur at order s; the last two, after their Schur elimination, occur at order s² with the nonsingular form just computed. Factoring those nonzero powers leaves an invertible reduction. Therefore the actual M is nonsingular over K and C for **every** Q' in the canonical fiber. This uses actual second-order coefficients and is not an inference from the singular first-order block. All first-core symmetry images follow, closing every two-edge case.

## 5. The resulting complete class statement and coverage count

### Theorem RP

Under the fixed first Et-Taoui core, central inversion rho, and RP, no arbitrary complex unit-phase compatibility vector exists. Every relative second-core permutation with four rook-positive inversion pairs is excluded in writing, with no restriction on independent diagonal phases.

There are exactly8 raw perfect matchings of the eight nonzero grid points using four rook edges:3 with h=1,3 with h=3, and2 with h=2 as classified above. Assigning the four pair labels and their orientations gives4!*2^4=384 bijections per raw matching. Dividing by the8-element literal point stabilizer of the second rook grid gives

    8*384/8=384

distinct literal character matrices Q' in this class. This is a coverage count of core tables, not a problem/discovery count, and no executable was used to obtain it.

The old commuting-core class has a different pair signature; this note does not double-count it as RP. Many other second-core tables may be excluded by the general rank8 theorem or leading test, but their actual ranks/classes have not been evaluated and are not silently counted closed. No assertion that RP exhausts the rank5–7 possibilities is made.

The prepared5040-core request remains unchanged, unrun and without GO. This written class closure can be an input to a future admission/acceptance decision, not a retroactive claim of finite replay. All scientific claims remain author-written CANDIDATE pending separate reconstruction and parent review. Other orientations, conference classes, nonuniform arrays and the full maximal1-RQLS10 target remain UNKNOWN.
