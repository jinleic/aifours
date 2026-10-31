# LOCAL4: every intrinsic C4 in an ordinary four-MOQLS(8) has real projector span at least ten

**SELF-CONTAINED COMPLETE WRITTEN AUTHOR CANDIDATE — UNREVIEWED, NOT ADOPTED.** PhysicsMOQLS8-2. Actual preceding native clock: Thu Oct 29 10:27:27 PDT 2026. This completes the nonproduct C4 span-nine exclusion, including arbitrary COMPLEX rays: the real form is DERIVED, not imposed. The only adopted import is GAP3. No f192 verdict is transferred to the new proof. The C5 union stays byte-fixed for its separate review.

## 0. Actual setting and sole imported theorem

Q,X1,X2,X3 are four arbitrary ordinary MOQLS of order 8. Every original row and column of every member is an ONB of C^8, and every pair of distinct members has its 64 same-cell tensor products forming an ONB. Thus for distinct cells y,z and distinct members M,N,

    <M_y,M_z><N_y,N_z>=0.

C is an intrinsic irreducible component of Q, meaning a connected component of its non-orthogonality graph on original cells. Its complex span W has dimension FOUR. Different components are orthogonal; every original row and column meets C in a four-ONB of W, so C has exactly 32 original cells. Put P_z=|Q_z><Q_z| and S=span_R{P_z:z in C}, with b=dim_R S. Every actual row resolves P_W, and sum_{z in C}P_z=8P_W.

**Sole adopted import, GAP3:** every ray in a nontrivial intrinsic component of any member of a four-MOQLS(8) has GLOBAL multiplicity at most THREE. This is Gate 1 of `institute/runs/three-area-2026-10-23-96h/MOQLS-unrestricted-four-family-ray-gap-intrinsic-and-local-span-budget-entire-parent-v1.md`, SHA256 `2e254b56d108994844cf337c31b98fa851effca15a68a847c6cb2db84552bee4`. No earlier C4/5/6 span bound, tensor classification, real-form claim, catalogue, solver or unreviewed source is an import. All lemmas used below are proved here.

## 1. Exact per-mate operator resolutions and the five-fold star bound

Fix an actual cell y of C with ray u. For each mate X, evaluate the second factor of the ACTUAL Q-X tensor-ONB resolution along X_y. The z=y term is P_u; all other terms vanish unless z is outside y's row and column AND Q_z is perpendicular to u. Therefore

    sum_{z off y's row/column, Q_z perpendicular to u}
            |<X_y,X_z>|^2 P_z = I_8-P_u.

For distinct mates X,X', their product orthogonality at y,z implies that these two weights cannot both be nonzero. Each weight is at most one. Sum over all three mates, compress to W, and add back the two disjoint actual three-ONB stars in y's row and column. This gives

    A_u := sum_{z in C, Q_z perpendicular to u} P_z >=5(P_W-P_u).       (STAR)

Every actual u has at least FIFTEEN orthogonal-star cells. An actual star ray w perpendicular to every other distinct star ray would satisfy m(w)=<w,A_u w>>=5, contrary to GAP3. Such an isolated star ray is impossible.

## 2. Two-plane projection mass: at most three actual rays, and a third ray has multiplicity one

Let B be ANY complex two-plane in W. The total B-projection mass of all component cells is

    sum_{z in C} ||P_B Q_z||^2 =16.

For each actual ray v in B, let v' be its unit in-plane orthogonal ray, possibly virtual. Evaluate STAR for v along v'. If Q_z is perpendicular to v, its B-projection is zero or parallel to v', and its squared v'-overlap equals its B-projection mass. Consequently

    sum_{z in C, nonzero P_B Q_z parallel to v'} ||P_B Q_z||^2 >=5.     (PLANE)

For distinct actual v in B their in-plane perpendicular rays v' are distinct, so the corresponding NONZERO-projection cell sets in PLANE are disjoint. Hence B contains at most THREE distinct actual rays, because four would require mass at least twenty instead of sixteen.

If three such rays were pairwise nonorthogonal, their own occurrence cells would have projection directions distinct from all three target perpendicular directions. They would add at least three units to the required fifteen, exceeding sixteen. Thus three actual rays in B MUST contain an orthopair x,x'. Their third ray v is orthogonal to neither, and its own cells lie outside all three target direction sets. PLANE then gives 15+m(v)<=16, so **m(v)=1**. In particular a two-plane can never contain TWO different actual unordered ONB pairs.

## 3. Every actual C4 ray occurs exactly once

Fix an actual u, with m=m(u)<=3. If every original row without u had at most one star-u cell, the total number of star cells would be at most

    3m+(8-m)=8+2m<=14,

contrary to STAR. Thus some actual row WITHOUT u has at least two rays v,w perpendicular to u. It cannot have three, since the fourth ray would then be u. Its remaining two rays x,x' form an ONB of a complex two-plane B containing u; since the row does not carry u, u is distinct from x,x'. Section 2 applies to these three actual rays in B and makes u's multiplicity ONE.

This holds for every actual u. Thus ALL 32 component cells have distinct projective Q-rays. The original row and column through any cell consequently have no common ray except that cell's ray. This conclusion is restricted to an intrinsic C4; fixed complete rays elsewhere remain allowed.

## 4. Full active span, including virtual test vectors

We need the following statement, proved here so no earlier actual-only theorem is extended silently.

**Lemma.** For EVERY nonzero a in W, including a virtual direction, the actual Q-rays with nonzero a-overlap complex-span W.

Normalize a, and let A be their complex span. The identity 8a=sum_{z in C}Q_z<Q_z,a> puts a in A. If dim A=1, its only active ray is a itself, which is actual and orthogonal to all other rays, contradicting intrinsic dimension four. If dim A=2, write A=span(a,lambda). For an actual mixed active x, the only possible active ray perpendicular to x is its in-plane partner x'. The other possible star-x rays lie in A-perp. A four-ONB through x needs three other vectors, whereas A-perp has dimension two, so x' is actual and is an isolated star ray. Contradiction.

If dim A=3, write Pi=A intersect a-perp and choose unit pi in W perpendicular to A. A mixed active ray is in B_lambda=span(a,lambda), lambda a direction of Pi. Every pi-active ray is a-inactive. STAR for such x, evaluated along pi, requires pi-weight at least five on K_lambda=B_lambda-perp. Three distinct projective lambda directions give K-planes pairwise meeting only in C pi. Their positive pi-weights would require

    15<=8+2m(pi)<=14,

where m(pi)=0 if pi is virtual and <=3 only if it is actual. Hence at most two directions occur; two are needed to span A. Every actual line without a has at least two active entries, because their squared a-overlaps sum to one and each is below one. Three are impossible: two would lie in one B-plane and orthogonally span it, making all other entries inactive. Its exactly two active entries must span a, by the actual ONB expansion, so they form an in-plane pair in ONE B-plane. Every mixed ray's in-plane partner is therefore actual.

For a mixed x in B_1, its partner is perpendicular to every a-inactive star-x ray, all lying in B_1-perp. Absence of an isolated star ray forces the unique B_2 orthogonal partner of x to be actual as well. With unit Pi directions lambda_1,lambda_2 and kappa=<lambda_1,lambda_2>, this requires 0<|kappa|<1. Starting from a nonzero B_1 ratio r in a+r lambda_1, four successive cross-plane/in-plane/cross-plane/in-plane partners have ratios

    -1/(kappa conjugate(r)),  conjugate(kappa) r,
    -1/(|kappa|^2 conjugate(r)),  |kappa|^2 r.

They are all actual mixed rays. The last ratio is smaller in modulus than a positive minimum of |r| in the finite actual B_1 set. Contradiction. This proves the lemma.

In particular, the complex annihilator of S contains no nonzero rank-one matrix b a*: annihilation of every projector would mean every actual ray is perpendicular to a OR to b; the identity in S forces a perpendicular to b, and then all a-active rays lie in b-perp, contradicting the lemma.

## 5. If b<=9, every star has span exactly five

For an actual u define T_u=span_R{P_v:v actual component ray perpendicular to u}, sigma_u=dim T_u. It contains the diagonal algebra of an actual three-ONB E from a row through u. If its off-diagonal space in E had dimension zero, there would be only three axis rays. If it had dimension one, choose an actual non-axis generator v. When v has support two, every non-axis star ray lies in the same coordinate two-plane, giving at most three such rays by Section 2 plus the remaining axis. When v has support three, every full-support off-projector direction determines a UNIQUE normalized projector, by rank-one purity; the only non-axis ray is v. Neither case allows fifteen distinct star rays, as required by Sections 1 and 3. Thus sigma_u>=5.

Let L_u be the real cross image of Z -> P_u Z P_(u-perp) on S, written {u chi*:chi in L_u}. Its kernel contains RP_u and T_u in direct sum, so

    b>=1+sigma_u+dim_R L_u.

The lemma of Section 4 implies that the u-perp projections of actual u-active rays complex-span W intersect u-perp, dimension three. Those vectors lie in L_u after nonzero scalar normalization. Hence dim_R L_u>=3. If b<=9 we therefore have, at EVERY actual u,

    b=9, sigma_u=5, dim_R L_u=3.                          (EQUALITY)

We now assume this boundary and derive its real form rather than imposing one.

## 6. Every five-dimensional star span is common-real

Fix actual u. Its row and column star bases E,F are two disjoint three-ONBs, because every actual ray has multiplicity one. Their transition has no one-block axis; in three dimensions it is either FULL3 or connected with exactly ONE zero. The elementary pattern fact is as follows: without a degree-one row/column, two zeros force two rows to overlap in exactly one nonzero coordinate, contradicting orthogonality. Their diagonal algebras meet only in scalars, so T_u=D_E+D_F, dimension five.

If the transition has one zero, one actual F-ray w has support two on a coordinate plane U. Let b be its in-plane partner and let e_k be the third E-axis. The other two F-rays form an ONB of V=span(b,e_k), with both coordinates nonzero. Their two real off-directions exhaust the star off-space: one pure U-edge and one fixed b-to-e_k cross direction. Rank-one purity then puts EVERY actual star ray in U OR V. Each of those two-planes has at most three actual rays by Section 2, contradicting the fifteen distinct star rays. Hence the transition is FULL3.

The two-dimensional star off-space contains NO pure edge. Indeed write a hypothetical pure-edge Hermitian Z as D+Y with D E-diagonal and Y F-diagonal. The omitted E-axis is an eigenvector of Y, and it has nonzero coefficient along EVERY F-vector. Therefore every F-eigenvalue is the same; Y is scalar and Z has zero off-part, contradiction. Thus every non-axis actual star ray has ALL THREE E-coordinates nonzero.

Choose a real basis of this two-dimensional off-space, and write its three cyclic edge entries as complex homogeneous linear forms

    L12(t,s), L23(t,s), L31(t,s),       t,s real.

For a full-support rank-one projector their product is real and strictly positive. If Im(L12 L23 L31) were a nonzero real homogeneous binary cubic, it would have at most three projective real zeros. Each full-support projective off-direction determines at most one normalized rank-one projector: multiplying all off-entries by a real c multiplies each diagonal, recovered from an off-entry triple, by c, and unit trace then fixes c=1. There would be at most three non-axis rays plus three axes, fewer than fifteen. Therefore

    L12 L23 L31 is an IDENTICALLY REAL binary cubic.       (CUBIC)

The factorization possibilities in C[t,s] are exhaustive: its three linear-factor roots are invariant under conjugation. Either all three roots are real (including an infinite root), or one is real and the other two are a nonreal conjugate pair. In the first case every edge form is a constant phase times a REAL linear form. The existence of an actual full-support projector makes the product of those three phases real. A single diagonal rephasing of E consequently makes ALL THREE edge forms real, hence the entire T_u is real symmetric in that frame.

In the conjugate-pair case, relabel cyclic coordinates so

    L12=c L,   L23=d conjugate(L),   L31=e R,

with c,d,e nonzero constants, R a nonzero real linear form, and L genuinely complex on the real (t,s)-plane. For a full-support rank-one projector of a ray v,

    |v1|^2=L31 L12/conjugate(L23)=(ec/conjugate(d))R,
    v3/v1=L31/|v1|^2=conjugate(d)/c.

Thus EVERY non-axis actual star ray lies in ONE fixed complex two-plane spanned by e2 and e1+(conjugate(d)/c)e3. That plane already contains actual e2 and hence contains at most two non-axis rays by Section 2. Again there cannot be fifteen star rays. The conjugate-pair case is impossible.

We have proved: every T_u is common-real in a diagonal rephasing of ANY actual star basis E, its off-space has dimension two with one real phase-line on each edge, and it contains no pure edge.

## 7. Four local real structures glue to one global real frame

Fix an ACTUAL component row basis (e1,e2,e3,e4). Let V=Off_E(S), dimension five. For i=1,2,3,4 let V_i be the two-dimensional off-space of T_ei. It lies in V and is supported on the triangle of coordinates OTHER than i. By Section 6 its three edge images are real one-dimensional phase-lines. In the corresponding real triangle edge-coordinates, V_i is a two-plane containing no coordinate axis, so its single defining linear equation has ALL three coefficients nonzero. Consequently a vector in V_i with one edge zero has its other two edges nonzero unless it is zero, and that zero-edge subspace is one-dimensional.

Take distinct i,j,k, and let l be the remaining index. The six-dimensional domain V_i plus V_j plus V_k maps by addition to V of dimension five, so there is a nontrivial relation Z_i+Z_j+Z_k=0. None of the Z's can vanish: otherwise the other two would be opposite matrices supported on their single common edge, which would be a forbidden pure edge. The edge jk occurs only in Z_i and hence is zero there; similarly ik and ij are zero in Z_j and Z_k. Their remaining edges to l are all nonzero. Cancellation on each of li,lj,lk proves that the two phase-lines supplied on that edge by its two star triangles are the SAME real line.

Such a relation has dimension at most one: each Z is in its one-dimensional specified zero-edge subspace, and a nonzero common edge fixes the ratio of any two coefficients. Thus the sum of any three V_i has dimension exactly five and equals V. Repeating the relation for each omitted l aligns the local phase-lines on all six global edges.

Each triangle's cyclic phase product is real by its local real structure. Rephase the four E-axes to make edges 12,13,14 real. The triangle conditions through vertex 1 then make edges 23,24,34 real as well. Every V_i, and hence their five-dimensional span V, is now real symmetric. The E-diagonal algebra is already real. Therefore the ENTIRE S is contained in the ten-dimensional real symmetric space in ONE global orthonormal frame. Every actual projector is real in this frame, which means its unit ray has a phase-real representative.

This is the missing arbitrary-complex-to-real bridge. It used all four stars, actual-ray uniqueness and the no-pure-edge property; no separate per-cell frame or assumed common conjugation was introduced.

## 8. The derived real hyperplane contradicts the star-cell count

Since b=9, S is a hyperplane in Sym_R(W), dimension ten. Let H be its nonzero real symmetric annihilator. Its trace is zero because P_W belongs to S. Rank one is impossible for a nonzero trace-zero symmetric operator. Rank two would have eigenvalues lambda,-lambda,0,0; rotating the two eigencoordinates rewrites q_H(v)=0 as xy=0. Every actual ray would be perpendicular to one of two orthogonal virtual axes, contradicting Section 4. Hence rank H is THREE or FOUR.

Choose an actual ray u NOT in ker H; one exists because the actual rays span W. All actual rays have multiplicity one. Write R2 for the number of original rows without u having two star-u cells. No u-free row has three. Its own row has three stars and the other seven have at most one plus one extra for an R2 row. STAR therefore implies

    15<=3+7+R2,       so       R2>=5.                    (FIVE)

For each such row its remaining actual orthopair x,x' spans a real two-plane B containing u. The compression H|B has zero diagonal in x,x'. Since u is a third distinct real null ray, its off-diagonal must vanish too. Thus B is a totally null real two-plane through u.

There are at most TWO such planes through a nonkernel null ray for a rank-three or rank-four trace-zero symmetric form on a real four-space. Here is the full degeneracy check. For rank four, quotient the H-orthogonal hyperplane of u by R u; the induced nondegenerate real quadratic form has dimension two. A null two-plane through u corresponds to a null projective ray of this quotient, of which there are at most two (or none in the definite case). For rank three, the nondegenerate quotient by its one-dimensional kernel has Witt index one. Every totally null two-plane therefore contains the kernel and is uniquely span(u,ker H), since u is not in the kernel. Thus there is at most one in that case.

Finally a fixed B can account for at most ONE of the R2 rows. By Section 2 there is only one actual unordered orthopair in B, and because all actual rays have multiplicity one that pair cannot occur in two different rows. Hence R2<=2, contradicting FIVE. This eliminates b=9. Section 5 already excluded b<=8, so the theorem follows.

## 9. Result, q4 caller and the exact unchanged original frontier

**LOCAL4>=10:** every intrinsic four-dimensional component of every member of every ordinary four-MOQLS(8) has real projector span at least TEN, with arbitrary complex rays and no classical mate assumption.

This is a COMPLETE WRITTEN AUTHOR candidate, not a scoped real-only result. Every new bridge is included in this source. It awaits a NEW complete review and parent disposition; f192's returned support is not silently enlarged to cover it.

The separate C5 review union remains EXACTLY `frontier-20261029-C5-span-ten-no-Lagrangian-ray-v1.md` (SHA256 d4a47f3456399fa9da42a36253e30e1b73b035b64c7c1e36808cf9547969444b,115LF) plus `frontier-20261029-C5-span-eleven-completion-v1.md` (SHA256 0b1fe8d135faa4d55cc136f80832c9a910d208ec18fcfc28e37f42eab413510c,96LF). No byte is changed here.

ONLY CONDITIONALLY ON full review of LOCAL4>=10, the fixed C5>=11 union, and the adopted original component/budget caller, q4 would be excluded: with adopted no intrinsic C2/C3, b(C6)>=12, b(C7)>=13 and b(C8)>=15, every nonclassical member has span at least 14 (C4+four fixed rays, C5+three fixed rays, C6+two, C7+one, C8, or two C4s). Four would require sum at least56, contradicting the adopted all-four-nonclassical span budget53. This arithmetic is NOT an automatic q4 adoption or a new C5 variant.

The original existence-or-classicality alternative for four MOQLS(8) is not fully solved by a q4 exclusion: q1/q2/q3 mixed-classical strata remain unless separately settled by their own exact arguments. No numerical maximum M(8), maximum-three claim or new physical witness is supplied. A10 stays GB15/18 with literal P1-B2.M2, P1-B2.M4, P1-B3.M2 UNKNOWN; A11 stays OPEN.

## 10. Assurance and review duties

All derivations are exact WRITTEN mathematics, not computer/kernel verification. No scientific interpreter, chosen numeric probe, solver, heavy run, external model or nested agent was used. Complete review must reconstruct STAR/PLANE and actual multiplicity-one, virtual active span, the qutrit transition cases, the binary-cubic factorization and its nonreal branch, the four-star phase-gluing dimension argument, and the real null-plane row count including rank-three degeneracy. No formal, human, configured-family, executable, priority, novelty or parent acceptance is asserted. Every earlier frozen source and historical process/cadence finding is retained; no result retroactively cures them.
