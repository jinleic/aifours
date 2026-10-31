# The 12-cell 4×4 (4,4,2,2)/(4,3,3,2) profile is impossible for Q alone

**WRITTEN author candidate; independent review pending.** An arbitrary complex order-8 QLS cannot have exactly 12 mixed cells on a 4×4 incidence board with row degrees `(4,4,2,2)` and column degrees `(4,3,3,2)`, nor the incidence transpose, relative to any chosen actual Q row. No mate, numerical source, realness or phase condition is used. This is one profile exclusion, not full m12/four-family classicality.

Choose the actual Q row as coordinate basis. A mixed line of degree k has a complementary k-axis subspace whose mixed rays form an ONB. A degree-2 line uses a common support 2; a degree-3 line has at most one support-2 ray. Orthogonal support-2 rays on one line have equal or disjoint support. A 4-mixed line cannot contain two support-2 rays and a support-3 ray: equal 2-supports fill their plane; distinct supports are disjoint and a 3-support meets one of them in exactly one coordinate.

## Forced incidences

Both degree-4 rows meet all four columns. The degree-2 column therefore meets precisely those rows and has common support U. Each degree-3 column already meets the two degree-4 rows; its third cell lies on a degree-2 row and has support 2, so both of its degree-4-row Q rays have full support 3. The degree-4 column meets all rows, and each degree-2 row therefore has one cell there and one in a degree-3 column. The two degree-3 columns meet different degree-2 rows. Let V_1,V_2 be these two low-row 2-supports; let T_1,T_2 be the degree-3 column 3-axis subspaces, K_1,K_2 the two degree-4 row 4-axis subspaces, and L the degree-4 column 4-axis subspace. Each T_j⊂K_1∩K_2 and V_j⊂T_j.

## The two row subspaces coincide

If K_1≠K_2, their intersection has size exactly 3, so T_1=T_2=:T. The low-row rays in the degree-4 column are orthogonal support-2 rays on V_1,V_2⊂T; in a 3-set they cannot be distinct and disjoint, so V_1=V_2=:V. They fill span(V). The two high-row rays in that degree-4 column therefore avoid V. In high row i they lie in K_i\V, a 2-axis set, and are mixed, so have support 2. That high row already has its support-2 ray in the degree-2 column and full-support-3 rays in the degree-3 columns, contradicting the 4-line fact. Hence K_1=K_2=:K.

The two low-row rays in the degree-4 column cannot share their support, for then they fill that 2-plane and its two high-row rays are support 2 in the 2-axis complement of L; this again gives a high row two support-2 rays and a support-3 ray. Thus V_1,V_2 are disjoint. The high-row rays of the degree-4 column cannot have support 2 (same 4-line contradiction) or support 3 (two disjoint low support-2 rays in a 4-line), so both have full support 4. Consequently L=K and V_1⊔V_2=K.

## Projector balance contradicts the row orthogonality

Sum the twelve actual Q rank-one projectors by rows and by columns. All line subspaces are coordinate subspaces, so

`2 P_K + P_(V_1) + P_(V_2) = P_K + P_(T_1) + P_(T_2) + P_U`.

Using V_1⊔V_2=K and writing T_j=K\{a_j}, this is

`P_U = P_(a_1) + P_(a_2)`.

Thus a_1,a_2 are distinct and U={a_1,a_2}. But in either high row its degree-2-column Q ray has support U and is orthogonal to its degree-3-column Q ray with full support T_j. Since U meets T_j in exactly one coordinate, their inner product cannot vanish. Contradiction.

The incidence transpose is valid without changing the original chosen coordinate basis. No assertion is made about profiles `(4,4,2,2)/(3,3,3,3)`, `(4,3,3,2)/(4,3,3,2)` or those with an all-degree-3 side; A10/A11 and global four-family questions remain open. Review must reconstruct forced low-row incidences, full-support conditions, both cases for K, and the exact projector identity. No parent, formal, human, configured-family, executable or novelty verdict is asserted.
