# One classical member: the eight-mixed-cell boundary is impossible

**WRITTEN author candidate; no catalogue, numerical solver, finite witness, external theorem or novelty premise. Disjoint mathematical review pending.** In any actual ordinary four-MOQLS(8) containing a classical member L, every other nonclassical QLS Q has **at least nine mixed cells** relative to any actual Q basis line in the three-net of rows, columns and L symbols. The other two members R,S are arbitrary complex QLS. This is not a complete q3 exclusion or an M(8)/A10/A11 result.

The separately review-pending ≥8 bound `frontier-20261028-four-family-one-classical-mixed8-v1.md` (SHA256 9f3882c9e5b8add15ccc097f3567ab89d4c150cf728e09e9860546a4dc008ad6) and the equality-profile classification `frontier-20261028-q3-mixed8-line-profile-v1.md` (SHA256 91f87da6a71ca11f22d41b2e724191a4d7e2e6abf90112708f9677fbb823b0ad) are named WRITTEN inputs: if Q has exactly eight mixed cells in an actual four-family, each of its three net classes partitions those cells as `3+3+2`. This packet excludes that final profile.

## 1. The 3+3+2 profile forces two identical Q bases

Rows, columns and L-symbol lines form a three-net; Q,R,S are actual ONBs on every line because the classical L ray is identical on each L-symbol line. Any two cells share at most one net line. Choose any net line as row 0 and independently normalize all four members there to coordinate rays e_j. A *mixed* Q ray is not one of Q's first-row axes.

On a three-mixed ONB line, five light singleton rays occupy distinct axes and the three mixed rays form an ONB of the complementary three-dimensional coordinate space. At most one mixed ray there has support size 2: two different 2-subsets of three axes intersect once and cannot be orthogonal; two orthogonal rays with the same 2-support span that two-space and force the third ray to be the remaining singleton. On a two-mixed line, both mixed rays have the same two-axis support.

Assume exactly eight mixed cells. Choose a net class with its three mixed groups X,Y,Z of sizes 3,3,2. Let T be the three-coordinate mixed subspace on X and choose a support-3 Q ray x on X; at least two exist. Each of the two other class-lines through x contains at least three mixed points, because x cannot lie on a two-mixed line. It cannot contain another point of X or two from either parallel group Y,Z, so it has exactly three mixed points: x, one Y point and one Z point. The two lines use both Z points and two distinct Y points. Since x has full support T, both lines' three-axis mixed subspaces equal T. Their two Y rays must have support size 3, because the corresponding Z rays have support size 2 and a three-mixed line has at most one such ray. Hence the mixed subspace on Y is also T; the remaining Y ray is in T, and both Z rays have a common two-axis support U⊂T.

Every support-3 x∈X has two net-line neighbors on Y, whose Q rays are orthogonal to x. The three Q rays on Y form an ONB of T, so x is collinear with the remaining Y ray. At least two independent X rays have support 3; their matched Y rays are distinct, forcing the third X and Y rays to be collinear as well. Thus X and Y carry the **same Q ONB** up to phases and reordering.

If all three of those basis rays have support size 3, all six corresponding R rays on X∪Y are pairwise orthogonal: within X or Y by the net line; across X,Y, equal Q rays force R orthogonality by Q⊗R, and different Q rays are net-line-adjacent by the support-3 argument. Each of the six Q rays overlaps all three first-row Q axes in T, so the six R rays are all orthogonal to the corresponding three first-row R axes. Six orthogonal nonzero vectors cannot fit in their five-dimensional complement. Hence exactly two basis rays have support 3 and the third has support 2.

Call the support-2 basis ray p_0 with support U_0, and the two support-3 basis rays p_1,p_2. Their restrictions to U_0 are nonzero collinear vectors along the unique ray v⊂span(U_0) perpendicular to p_0. The two Z rays form an orthonormal pair on their common two-axis support U⊂T.

## 2. Z cannot use a different two-axis support

Suppose `U≠U_0`. They are distinct 2-subsets of three axes, so they meet in exactly one axis. Each Z ray has nonzero overlap with p_0 and thus cannot share an ONB net line with either p_0 cell on X or Y. Each Z point nevertheless needs another mixed point on each of its two other class-lines; the only candidates lie on X or Y. Its Q ray must therefore be orthogonal to p_1 or p_2.

The two restricted vectors `p_1|_U,p_2|_U` are both nonzero, **not orthogonal and not collinear**. Their inner product on U is minus the product of their nonzero coefficients on the omitted third axis, since p_1⊥p_2 in T. If they were collinear on U, an appropriate nonzero linear combination of p_1,p_2 would be supported only on that omitted axis. This combination is orthogonal to p_0, which has a nonzero coefficient there (the omitted axis lies in U_0); hence the combination would vanish, contradicting independence of p_1,p_2.

In a two-dimensional space, two orthogonal Z rays cannot each be perpendicular to one of two nonorthogonal, noncollinear rays: the perpendicular of a given ray is unique, and perpendicular rays are orthogonal to each other exactly when the original two rays are orthogonal. Thus at most one Z ray can be orthogonal to p_1 or p_2. The other has no possible mixed neighbor on either other class-line, contradiction. Hence `U=U_0`.

## 3. The remaining case gives eight R rays in six dimensions

With U=U_0, p_1 and p_2 both restrict to the same nonzero ray v perpendicular to p_0. A Z ray must be orthogonal to at least one of p_0,p_1,p_2 to have a mixed neighbor on its other class-lines. Consequently the two orthogonal Z rays are, up to phases, exactly p_0 and v. Denote their cells z_0,z_v respectively.

The six R rays on X∪Y are pairwise orthogonal. Within either group this is a net-line ONB. Across groups, equal Q basis rays force R orthogonality by the actual Q⊗R product ONB; for different basis rays at least one is support-3, and that support-3 cell is net-line-adjacent to the other basis ray by the two-line argument in §1.

For z_0, each of its two other class-lines needs another mixed point. It cannot meet an X/Y p_0 cell on an ONB line, since Q would repeat the same ray. It also cannot lie on a two-mixed line with a support-3 ray, by the two-mixed-line lemma. Thus each of its other lines contains one support-3 cell from X and one from Y. The two lines are distinct and together cover all four support-3 cells. R_(z_0) is orthogonal to those four by net lines, and to the two X/Y p_0 cells by Q⊗R because their Q rays coincide with p_0. So it is orthogonal to all six R rays on X∪Y.

The ray v overlaps both p_1,p_2, since their restrictions to U_0 are nonzero multiples of v. Hence Q⊗R orthogonality makes R_(z_v) orthogonal to the four support-3 R rays. Its only possible mixed net-line neighbors outside Z are the X/Y p_0 cells, since v is orthogonal to p_0 and overlaps p_1,p_2; both other class-lines through z_v need one, so R_(z_v) is orthogonal to those two as well. It is orthogonal to R_(z_0) on the Z line. Therefore **all eight R rays on X∪Y∪Z are pairwise orthogonal**.

Every one of the eight Q rays uses both axes of U_0: p_1,p_2 have support T, while p_0 and v have support U_0. Comparing the actual Q⊗R products at those eight cells with the first-row products on the two U_0 axes forces all eight R rays into the complement of two first-row R axes, of dimension at most six. Eight orthogonal nonzero vectors cannot fit there. Contradiction.

Thus the only possible eight-mixed profile is also excluded, so the cited ≥8 bound strengthens to **≥9**. For a q3 four-family, all three nonclassical members satisfy this bound, yielding at least 27 mixed-cell incidences and at least 27 summed off-first-row support-surplus units. The incidences may overlap; this is not a global q3 contradiction.

Independent review should reconstruct the profile inputs, the common-three-axis and basis-identification step, the U≠U_0 two-dimensional argument, and every actual R-orthogonality edge in the final eight-in-six contradiction. No numerical/novelty promotion follows.
