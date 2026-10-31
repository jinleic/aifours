# The 12-cell 4×4 (4,3,3,2)/(3,3,3,3) profile is impossible for Q alone

**WRITTEN author candidate; disjoint review pending.** An arbitrary complex order-8 QLS cannot have 12 mixed cells on four rows and four columns, with row degree profile `(4,3,3,2)` and all four columns of degree 3. The incidence transpose is likewise impossible, using the same originally chosen coordinate basis. No mate, source catalogue, equal-modulus, reality or numerical premise is used. Other 4×4 profiles are not addressed here.

A degree-k mixed line supplies an ONB of its complementary k-axis subspace; a degree-2 line uses one common support-2 set; a degree-3 line has at most one support-2 ray. A pair of orthogonal support-2 rays in a common 3-set cannot be distinct, since distinct 2-subsets meet once. We also use the following observation: two orthogonal full-support-3 rays x_1,x_2 and two orthogonal support-2 rays u_1,u_2 in their common 3-axis space cannot satisfy x_i⊥u_i for i=1,2, since in the ONB u_1,u_2,e_z the x rays have a single nonzero shared e_z contribution.

Let H be the degree-4 row, A,B the degree-3 rows and L the degree-2 row. H meets all columns. Each column meeting L has a support-2 ray there and hence full-support-3 rays at its other two cells. Since A and B each miss exactly one column, the two L columns omit A and B respectively; the other two columns meet H,A,B. Let the two Q rays in row L have common support U, with orthogonal rays u_A,u_B in the L columns that meet A,B respectively. The column meeting A has the same 3-axis subspace T_A as row A because its A ray has full support 3; similarly the other L column has subspace T_B. Both T_A,T_B contain U and are subsets of H's 4-axis mixed subspace K.

## Same 3-subspace

If T_A=T_B, H's two Q rays in the L columns are orthogonal full-support rays in that common 3-space and each is orthogonal to its corresponding L-row ray u_A or u_B. The observation above gives a contradiction.

## Distinct 3-subspaces

Otherwise T_A∩T_B=U, and write `T_A=U∪{c}`, `T_B=U∪{d}`, `K=U∪{c,d}`. Let C_1,C_2 be the 3-axis subspaces of the other two columns. Summing the actual twelve Q projectors by rows and by columns gives

`P_K + P_(T_A) + P_(T_B) + P_U = P_(T_A) + P_(T_B) + P_(C_1) + P_(C_2)`,

so `P_(C_1)+P_(C_2)=P_K+P_U`. Coordinate multiplicities force C_1,C_2 to be T_A,T_B in some order.

In the column with space T_A, the B-row Q ray belongs both to T_B and T_A and is mixed; its support is exactly U. Similarly the A-row ray in the T_B column has support exactly U. Thus each of those columns already has a unique support-2 ray, and its other two Q rays have full support 3. Let v_B be the B-row support-U ray in the T_A column and v_A the A-row support-U ray in the T_B column.

The H-row ray in the L/B column has full support T_B and is orthogonal to u_B, so its U-projection is a nonzero multiple of u_A. The H-row ray in the other T_A column has full support T_A and is orthogonal to v_B. These H-row rays are orthogonal and their supports meet only in U, so their U-projections are orthogonal. Thus the latter U-projection is a nonzero multiple of u_B, forcing v_B collinear with u_A. Similarly v_A is collinear with u_B.

The A row contains two orthogonal full-support-T_A rays: one in its L column, perpendicular to u_A, and one in the other T_A column, perpendicular to v_B, which is collinear with u_A. They therefore form an ONB of span{u_B,e_c}. But the A-row ray in the T_B column is v_A, collinear with u_B, so it cannot be orthogonal to that ONB. Contradiction.

The full m12 4×4 `(4,3,3,2)/(4,3,3,2)` and all-degree-3/all-degree-3 profiles remain to be analyzed, as do global q2/q3/q4 and original A10/A11. Review must reconstruct the low-column incidence matching, exact projector balance, nonzero support projections and final 2-space saturation. No parent, formal, human, executable or novelty acceptance is inferred.
