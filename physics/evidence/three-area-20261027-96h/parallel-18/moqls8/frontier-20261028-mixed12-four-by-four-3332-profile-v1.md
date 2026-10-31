# The 12-cell 4×4 (4,3,3,2)/(4,3,3,2) profile is impossible for Q alone

**WRITTEN author candidate; full disjoint review pending.** An arbitrary complex order-8 QLS cannot have 12 mixed cells on a 4×4 board with degree profile `(4,3,3,2)` on both sides, relative to any chosen actual Q row. No mate, external classification, realness, equal-modulus or computation is assumed. This is the last 4×4 degree-profile case for the separate universal m12 synthesis; that synthesis and all its dependencies still require review.

## A degree-4 line lemma

In a degree-k mixed line, its mixed Q rays form an ONB of a complementary k-axis subspace. Degree-2 lines have a common support 2. A degree-3 line has at most one support-2 ray. Two orthogonal support-2 rays on one line have equal or disjoint supports. A degree-4 line cannot contain two support-2 rays and a support-3 ray: same supports fill their plane; disjoint 2-supports cover all four axes, and a 3-support meets one of them in exactly one coordinate.

**Stronger fact:** a degree-4 line cannot contain one support-2 ray p and two support-3 rays x,y. If U is p's support in the 4-axis line subspace K, each of x,y must contain both axes of U: a 3-set cannot be disjoint from U inside K, and intersection size one would give a nonzero single-coordinate inner product with p. Their nonzero U-projections are both collinear with the unique ray in U perpendicular to p. If their remaining axes differ, their U-projections give a nonzero inner product. If the remaining axes agree, p,x,y form an ONB of that 3-axis space and the fourth line ray is a singleton on the remaining axis. Both are impossible. In particular three support-2 rays on a 4-line force the fourth to have support 2.

We also use a 3-space observation: if u_1,u_2 are orthogonal on a common support-2 set U and x_1,x_2 are orthogonal full-support-3 rays on `U∪{z}`, then x_i⊥u_i for both i is impossible; relative to the ONB u_1,u_2,e_z, their inner product has a single nonzero e_z contribution.

Let H,A,B,L be the degree-4, degree-3, degree-3 and degree-2 mixed rows, and G,C,D,L' the analogous columns. H and G meet every incident column or row. There are two possible incidence cases.

## Low/low cell present

If `(L,L')` is mixed, row L has precisely G,L' and column L' has precisely H,L. Thus A,B each meet G,C,D and columns C,D each meet H,A,B. The H,L' ray has support 2; H,C and H,D have support at most 3. If exactly one has support 2, the 4-line contains two support-2 rays and a support-3 ray. If neither has support 2, it contains one support-2 ray and two support-3 rays. Both are impossible. Hence H,C and H,D have support 2, and the three-support-2 fact forces H,G to have support 2.

Column G has two support-2 rays at H and L. Its other two rays have support at most 3 because they lie in degree-3 rows; they cannot have support 3, so they have support 2. Each of the columns C,D has a support-2 ray in row H, and its A and B rays have full support 3. The A row's two full-support rays identify the 3-axis spaces of columns C,D; call the common set T. The H,C and H,D Q rays are orthogonal support-2 rays contained in T, and therefore have the same support. The A,C and A,D Q rays are orthogonal full-support-T rays and each is orthogonal to the corresponding H ray in its column. This contradicts the 3-space observation.

## Low/low cell absent

After exchanging A,B or C,D, the mixed incidences are exactly

`H: G,C,D,L'`; `A: G,D,L'`; `B: G,C,D`; `L: G,C`.

Indeed L' meets H and one degree-3 row, say A; L meets G and one degree-3 column, say C. The remaining degree equations force A to miss C and B to meet both C,D.

The A,L' Q ray has support 2, so A,G and A,D have full support 3. The L,C ray has support 2, so H,C and B,C have full support 3. In row H, H,L' has support 2 and H,C has support 3; H,D cannot also have support 3 by the stronger 4-line fact. Since H,D is mixed and belongs to the degree-3 column D, it has support 2. Therefore A,D and B,D have full support 3. The full-support B,C and B,D rays identify one common 3-axis subspace T for columns C,D and row B; the full-support A,D ray identifies T with row A as well.

The two Q rays in the low column L' share support U, so H,L' has support U⊂T because A,L' belongs to row A. The ray H,D has support 2 contained in T. They are orthogonal in row H; two distinct 2-subsets of T overlap once and cannot be orthogonal, so both have support U and fill its plane. But H,C has full support T and is orthogonal to both, impossible. Thus the second incidence case is also excluded.

This QLS-only result plus the separately named 4×4 profile packets can be synthesized only conditionally on complete independent review of each actual proof and import. Global four-family classicality, numerical M(8), original A10/A11, formal/human/executable verification and novelty remain open.
