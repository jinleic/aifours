# Nonproduct C4 span nine: virtual-neighbour transitivity and real-quadric inertia exclusions

**NEW WRITTEN AUTHOR ADDENDUM — UNREVIEWED.** PhysicsMOQLS8-2. Actual preceding native clock: Thu Oct 29 10:03:09 PDT 2026. The operator/product packets in f192 are immutable; this addendum is NOT retrospectively included in that review or its returned support. Parent full read and disposition of f192 remain pending. The C5 union is kept fixed as directed; no C5 variant is supplied here.

The original local target is still LOCAL4>=10. This addendum excludes additional real nonproduct quadric strata and strengthens the neighbour statement to EVERY virtual test direction. It does not classify arbitrary complex span-nine spaces or close LOCAL4, q4, M(8), A10 or A11.

## 1. Setting and family identities

Q,X1,X2,X3 are four ordinary MOQLS(8), with every actual row/column ONB and every one of the six same-cell tensor-product ONBs. C is an intrinsic irreducible component of Q spanning a complex FOUR-space W. It has 32 original cells, and every actual row/column meets it in a four-ONB. S is its real projector span. The sole adopted import used below is GAP3: every actual ray of C has global multiplicity at most three. Its source is Gate 1 of the prior-round parent disposition SHA256 `2e254b56d108994844cf337c31b98fa851effca15a68a847c6cb2db84552bee4`, named in the earlier operator packet.

For any ACTUAL component ray v, the complete Q-X tensor resolution evaluated along X_y at a cell y carrying v gives a positive weighted resolution I-P_v on the off-row/off-column star. Three mate weights at each distinct cell are disjoint and sum to at most one. Compressing to W and adding the two actual line stars proves

    sum_{z in C, Q_z perpendicular to v} P_z >= 5(P_W-P_v).        (V-STAR)

This immediately forbids an isolated star ray, since it would have multiplicity at least five. It also gives at least FIFTEEN star cells for every actual v. These identities are re-derived from the actual family, not presumed for an abstract cone.

## 2. The neighbour-span theorem extends to EVERY test vector

**Theorem V.** For EVERY nonzero a in W, including a which is not an actual ray, the actual Q-rays having nonzero a-overlap complex-span W. Equivalently the complex span of S applied to a is W.

Normalize a. Let A be the complex span of its active actual rays. The identity sum_{z in C}P_z=8P_W implies

    8a=sum_{z in C} Q_z <Q_z,a>,

so a belongs to A even when virtual. If dim A=1, its only active ray is a itself; it is actual and orthogonal to all other rays, contrary to intrinsic dimension four. If dim A=2, every mixed a-active ray has a unique in-plane orthogonal partner, forced actual on each line by the two-dimensional outside complement. All other rays orthogonal to it are perpendicular to that partner. V-STAR forbids the resulting isolated star ray.

If dim A=3, put Pi=A intersect a-perp and choose a unit pi in W perpendicular to A. A mixed active ray lies in B_lambda=span(a,lambda), lambda a direction of Pi. Every pi-active ray is a-inactive. For such a ray x, all pi-active star-x rays lie in K_lambda=B_lambda-perp. V-STAR evaluated at pi gives total pi-weight at least five on K_lambda. Three distinct lambda directions give K-planes pairwise intersecting exactly in C pi. Since the total pi-weight is eight, and pi has at most three occurrences if actual and zero otherwise,

    15 <=8+2m(pi)<=14

would follow. Hence only two lambda directions can occur, and two are needed to span A. Every actual line without a (all lines if a is virtual) has at least two a-active entries; three would put two orthogonal entries in one of those two B-planes and force the rest inactive. Its exactly two active entries must span a by the actual ONB expansion, so they are an in-plane pair in ONE B-plane.

For each such pair, the absence of an isolated star ray forces its cross-plane orthogonal partner to be actual as well. If kappa is the inner product of the two unit Pi directions, then 0<|kappa|<1. Alternating cross-plane and in-plane partners twice sends a nonzero B_1 ratio r to |kappa|^2 r, exactly as in the earlier operator packet's finite closure proof. A finite set of actual mixed rays cannot contain a strictly smaller positive |r| than its minimum. This contradiction eliminates dimension three and proves Theorem V. No multiplicity was assigned to virtual a; the ONLY virtual-axis count used was m(pi), bounded only if pi is actually present.

A useful equivalent forbidden configuration is a pair of orthogonal nonzero test vectors a,b in W such that EVERY actual Q-ray is perpendicular to a OR perpendicular to b. All a-active rays would then be in b-perp and fail Theorem V. Thus the complex annihilator of S has no nonzero rank-one matrix: a matrix b a* annihilating S would give precisely this support separation (and the identity in S forces a perpendicular to b).

## 3. A real quadric with no totally null two-plane is impossible

Assume now that ALL actual component rays admit phase-real representatives in ONE orthonormal real frame of W. Let H be ANY nonzero REAL symmetric operator with

    q_H(v)=v^T H v=0 for every such actual representative v,

and suppose no two-dimensional real subspace has q_H identically zero. This is a conditional real-cone assertion; no reality is inferred for an arbitrary C4.

Fix an actual unit u. Consider any actual row with at least two rays v,w perpendicular to u. The other two row rays x,x' span the two-plane B=span(v,w)-perp, which contains u. Both x,x' and u have q_H=0. In the real ONB (x,x') of B, the compression H|B has zero diagonal. If it is nonzero, its quadratic form is a nonzero scalar multiple of the product of the two coordinates, whose only null projective rays are x and x'. Hence u must be one of x,x', so the row contains u. If H|B is zero, B is a totally null two-plane, contrary to hypothesis.

Therefore every row WITHOUT u has at most ONE star-u cell, whereas each of the m(u) rows carrying u has exactly three. The total number of star cells is at most

    3m(u)+(8-m(u))=8+2m(u)<=14,

contrary to the lower bound fifteen from V-STAR. Thus no such H is possible.

In particular a nondegenerate symmetric H of inertia (3,1) or (1,3) has no totally null real two-plane. To see this directly, write q_H=||p||^2-||n||^2 in its positive/negative eigencoordinates. If one sign-space has dimension one, projection to that space is injective on any totally null subspace: a vector with zero projection has zero norm in the other sign-space too. A two-dimensional null subspace cannot inject into a line. Thus the entire signature-(3,1)/(1,3) real-quadric stratum is excluded.

## 4. Rank-two real annihilators are excluded by virtual transitivity

The trace of any real annihilator H is zero because each actual row resolves P_W. A nonzero rank-two such H has eigenvalues lambda,-lambda,0,0. A real orthogonal change within the first two eigencoordinates rewrites its null equation as xy=0. Let a,b be the two resulting orthogonal coordinate axes. Every actual ray is perpendicular to a OR to b. Theorem V excludes this, even if neither axis is actual. No tensor-product classification or chosen numerical example is used.

## 5. The exact remaining real span-nine possibilities

If b=9 and all rays are phase-real in one frame, their projectors span a hyperplane of Sym_R(W), whose dimension is ten. There is a UNIQUE nonzero symmetric annihilator H up to real scaling, and tr H=0. Sections 3–4 leave only:

- rank three, inertia (2,1,1 zero) or its sign reverse;
- rank four, inertia (2,2).

Rank one is impossible for a nonzero trace-zero symmetric operator; rank two and the other indefinite nondegenerate inertias have been excluded. This is a necessary classification only WITH the common-real hypothesis.

One further subcase of inertia (2,2) is already in the product stratum: if H^2=lambda^2 I with lambda!=0, orthogonally diagonalize H/lambda to diag(1,1,-1,-1). The isometric real identification

    (x1,x2,x3,x4) -> (1/sqrt2) [[x1+x3, x4+x2],
                               [x4-x2, x1-x3]]

preserves the squared norm and has determinant (x1^2+x2^2-x3^2-x4^2)/2. Every nonzero null ray is therefore a rank-one real 2-by-2 matrix. Extending this isometry complex-linearly gives ONE common unitary C2 tensor C2 factorization in which all actual rays are product. The complete product-component exclusion is in immutable `frontier-20261029-C4-product-component-exclusion-v1.md`, SHA256 `bfb192d7266c703d413b47cc3f99b5edffe9670b7cd9128d20dc6d0c1f50a01d`; its f192 review support still awaits parent disposition. Thus this equal-magnitude (2,2) case is excluded CONDITIONAL ON that whole proof, not by this addendum alone.

The real nonproduct b9 frontier is consequently rank-three H or rank-four inertia (2,2) with H^2 not scalar. A general complex b9 component has not been shown common-real and remains outside this conditional classification. No spectral normalization or reality premise is silently imposed on it. The missing original-target implication is still elimination of EVERY such b9 C4, or a coupled actual-family obstruction when at least three low-span C4 members coexist. No new q4 conclusion or A10/A11 upgrade follows. The C5 union remains byte-fixed during its separate review preparation, as Main directed.

## 6. Assurance

These are exact WRITTEN derivations, no scientific interpreter, selected numeric state, solver or heavy run. The operator identities concern actual same-cell tensor ONBs; abstract quadratic cones are not claimed to supply mates. Nothing is formal/kernel, human, configured-family, executable, novelty or parent acceptance. New conclusions here require a NEW full-scope review; no f192 verdict is transferred. Earlier frozen packets and all process/cadence disclosures are preserved.
