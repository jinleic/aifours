# An intrinsic C4 in a four-MOQLS(8) cannot lie on a common-real rank-three quadric

**COMPLETE WRITTEN AUTHOR STRATUM EXCLUSION — UNREVIEWED.** PhysicsMOQLS8-2. Actual preceding native clock: Thu Oct 29 10:10:53 PDT 2026. This removes the entire rank-three real-annihilator branch left by the preceding C4 quadric addendum. No projector-span bound is needed for this exclusion. It does not prove that arbitrary complex C4 span-nine data are common-real or remove the unequal full-rank (2,2) branch. LOCAL4>=10 and q4 remain OPEN. The C5 union stays byte-fixed as Main directed.

## 1. Original objects, exact additional hypothesis and sole import

Q,X1,X2,X3 are ANY four ordinary MOQLS(8): all original row/column ONBs and all six original 64-dimensional same-cell tensor-product ONBs. C is an intrinsic irreducible component of Q with complex span W of dimension FOUR. It has exactly 32 original cells, and each of the eight actual rows and eight actual columns meets C in a four-ONB.

Assume there is ONE orthonormal real frame of W in which all actual component rays have phase-real unit representatives, and there is a nonzero REAL symmetric operator H of rank THREE satisfying v^T H v=0 for every such representative v. Because each actual row resolves P_W, tr H=0. Thus H has inertia (2,1,one zero) or its sign reverse. Let g be its unit real kernel ray. No common-real assumption is silently applied outside this stated stratum.

The sole adopted theorem used is GAP3: each actual ray of this nontrivial component has GLOBAL multiplicity at most three. Source: Gate 1 of the prior-round parent disposition SHA256 `2e254b56d108994844cf337c31b98fa851effca15a68a847c6cb2db84552bee4`. Every other family identity and counting step is supplied below. The earlier operator/quadric packets are not assumed adopted.

## 2. Every actual ray has at least fifteen orthogonal-star cells

For an actual ray u at cell y and each mate X, taking the partial matrix element along X_y in the Q-X tensor-ONB resolution gives

    sum_{z off y's row/column, Q_z perpendicular to u}
           |<X_y,X_z>|^2 P_z = I_8-P_u.

The three mate weights at every distinct z are disjoint by mate-pair product orthogonality, and their sum is at most one. Compress to W and add back y's row and column stars, each an actual three-ONB of W intersect u-perp. Thus

    sum_{z in C, Q_z perpendicular to u} P_z >=5(P_W-P_u).

Taking traces proves that every actual u has at least FIFTEEN star cells. GAP3 applies to actual u and all other actual component rays, not to virtual g.

## 3. Null-plane geometry and the exact row inequality

In the nondegenerate three-dimensional quotient by the kernel g, the quadratic form has one positive or one negative direction. Any totally null real subspace there has dimension at most one: projection to that one-dimensional sign-space is injective. Therefore every totally null real TWO-plane in W contains g. For a null ray u!=g the UNIQUE such plane containing u is

    B_u=span_R(g,u),

regarded complex-linearly when speaking of its actual rays and orthogonal complement. A real two-plane B of this form will be called a generator plane.

Fix any generator plane B that contains an actual ray u!=g. Let R_B count original rows whose component four-ONB has TWO entries in B. Those two entries form an ONB of B. The other two entries form an ONB of D=B-perp and are null for H. The compression H|D is trace zero and NONZERO: if both B and D compressions were zero, the B-D cross block would have rank at most one because it kills g, so H would have rank at most two. A nonzero trace-zero real symmetric two-by-two form has exactly two orthogonal null rays. Hence EVERY one of these R_B rows carries the SAME two actual D-rays. By GAP3,

    R_B<=3.                                                (R1)

Let m(u) be the actual multiplicity of u, and let r_B(u) count those R_B rows which also carry u. If a row WITHOUT u has two star-u entries v,w, its remaining pair x,x' spans a real two-plane B' containing u. Their H-diagonal entries are zero. A nonzero compression H|B' has precisely the two null rays x,x', which would force u to equal one of them. Therefore H|B'=0; uniqueness of the generator plane through u gives B'=B_u=B. Conversely every B-pair row not containing u has exactly two star-u entries, its complementary D-pair. Thus the u-free rows having two star entries are EXACTLY R_B-r_B(u).

Rows containing u have three star entries; all other rows have at most one. The lower bound fifteen therefore gives

    15 <=8+2m(u)+R_B-r_B(u),
    R_B-r_B(u)>=7-2m(u).                                  (R2)

This is an actual row/cell count, not a dimension heuristic. Also, if N_B counts ALL component cells whose rays are in B, every B-pair row contributes two and every other row at most one, so

    N_B<=8+R_B.                                            (R3)

The same column facts hold but are not needed below.

## 4. Multiplicities on a generator plane

By R1–R2, an actual u!=g cannot have m(u)=1: it would require R_B-r_B(u)>=5>3. Hence every such ray has multiplicity TWO or THREE.

If u!=g appears in any B-pair row, then r_B(u)>=1. Multiplicity two would require R_B-r_B(u)>=3 and contradict R_B<=3. Thus every nong-kernel ray used in B-pair rows has multiplicity THREE. For such a ray, R2 says r_B(u)<=R_B-1: it cannot appear in ALL B-pair rows.

There is at least one B-pair row, since m(u)<=3 and R2 gives R_B>=1. But R_B=1 is impossible: its B-ONB contains at least one nong-kernel ray, which would appear in all B-pair rows. Therefore R_B is TWO or THREE.

Different unordered ONBs of a two-space have disjoint ray sets: sharing one ray fixes its unique orthogonal partner. At most one such basis can contain g.

### R_B=2

The two B-pair rows use different unordered B-bases; otherwise their nong-kernel rays would appear in both rows. If neither basis contains g, their four nong-kernel rays each have multiplicity three, giving N_B>=12>10=8+R_B, contradiction. Therefore one basis is {g,lambda} and the other is a distinct mixed pair {x,x'}. The three nong-kernel rays lambda,x,x' have multiplicity three, so N_B>=9+m(g). With R3 this forces m(g)=1 and N_B=10. In particular g is ACTUAL and there is no additional actual B-ray.

### R_B=3

No unordered B-basis can occur in all three rows, because it has a nong-kernel ray. If three different bases occur, at least five nong-kernel rays occur, each with multiplicity three, giving N_B>=15>11. Thus exactly TWO bases occur, in row counts 2+1. If neither contains g, their four nong-kernel rays give N_B>=12>11. Hence again the actual pair-row rays are {g,lambda} and one other pair {x,x'}, with the three nong-kernel rays of multiplicity three.

Now N_B>=9+m(g), while R3 gives N_B<=11; consequently 1<=m(g)<=2. Any additional actual nong-kernel B-ray would have multiplicity at least two by the first paragraph, yielding N_B>=9+m(g)+2>=12, impossible. Thus there is no such additional ray.

We have proved a uniform conclusion for EVERY generator plane containing any actual nong-kernel ray:

    g is actual,  m(g) is 1 or 2;
    B has EXACTLY THREE other distinct actual rays;
    EACH of those three has multiplicity THREE.            (R4)

The mixed B-pair and the g-orthogonal ray lambda are all actual original rays, not inserted completion vectors.

## 5. The final cell-count contradiction

Distinct generator planes intersect only in g. Every actual nong-kernel ray belongs to its UNIQUE generator plane. There are finitely many such planes because the actual ray set is finite. Let their number be k. By R4, each contributes exactly three nong-kernel rays of multiplicity three, hence NINE original cells. All g occurrences belong to every plane but are counted only once globally. The component's 32 cells would therefore satisfy

    32=m(g)+9k,           m(g) in {1,2}.

This is impossible: the right side is congruent to one or two modulo nine, whereas 32 is congruent to five. This completes the rank-three real-quadric exclusion. No executable enumeration or numerical parameter test is used.

## 6. Remaining original-target frontier and assurance

Together with the preceding C4 virtual-neighbour/quadric addendum, a COMMON-REAL span-nine C4 can only have a full-rank real symmetric annihilator of inertia (2,2). The scalar-square case is already the separately excluded common-product cone. The remaining common-real possibility has H^2 nonscalar; arbitrary complex span-nine components have not been shown common-real and remain unexcluded. No general LOCAL4>=10 or coupled q4 conclusion is established here.

The exact fixed C5 review union is unchanged. A10 remains GB15/18 with P1-B2.M2, P1-B2.M4, P1-B3.M2 UNKNOWN; A11 remains OPEN. These are WRITTEN AUTHOR candidates only, requiring a new complete review and parent disposition. No formal/kernel, human, configured-family, executable, novelty or priority acceptance is claimed. No scientific interpreter, selected probe, solver, heavy run, external CLI or nested agent was used. Earlier frozen packets and all historical process/cadence findings remain preserved; this is not a retroactive f192 scope expansion.
