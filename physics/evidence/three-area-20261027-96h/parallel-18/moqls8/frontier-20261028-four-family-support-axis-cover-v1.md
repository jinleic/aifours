# Every mixed support-2 axis is covered by a higher-support ray

**SELF-CONTAINED WRITTEN AUTHOR CANDIDATE; disjoint full review pending.** In an ordinary complex four-MOQLS(8), fix any member Q and any actual Q row as coordinate basis. For every coordinate axis a used by a mixed Q ray, **some mixed Q ray using a has support size at least 3**. Equivalently, the union of the supports of mixed support-2 Q rays is contained in the union of supports of mixed Q rays of support at least 3. Other mixed rays, lines and components are arbitrary. In particular no nonclassical member can have all its mixed rays supported on exactly two chosen-row axes.

This is an all-variable necessary support condition for the actual four-family, not a support-only sufficiency statement, full classicality, a numerical M(8) bound, A10/A11 closure or priority claim. It is independent of the 13-mixed-cell and 14-distinct-ray candidates. No classical mate, catalogue, selected witness, solver, realness or equal-modulus assumption is used.

## Exact physical setup

An ordinary QLS of order 8 is an 8×8 array of unit vectors in C^8 whose rows and columns are ONBs. Q,R,S,T form a four-MOQLS(8) when, for each pair, their 64 same-cell tensor products form an ONB of C^8⊗C^8. Independently standardize the chosen actual board row of each array to its own coordinate basis at the shared column labels. For distinct cells x,y and distinct members M,N, actual product orthogonality is `<M_x,M_y><N_x,N_y>=0`. A Q cell is mixed if its ray is not one of Q's standardized row rays; its support is its set of nonzero Q coordinates.

Assume, toward contradiction, that at least one mixed Q ray uses axis a and **every** mixed Q ray using a has support size 2. Other mixed rays avoiding a may have any support and may share rows or columns with the rays considered below.

## Axis groups and exact span saturation

A mixed ray on support `{a,b}` has nonzero coefficients in both coordinates. In any row containing it, another mixed ray must use a: a light e_a is not orthogonal to it, and row completeness requires total squared coefficient 1 on axis a. That other ray also has support 2 by the assumption. Its other support coordinate must be b, since a different 2-support `{a,c}` would give a single nonzero shared-coordinate inner product. The two rays are orthogonal and form an ONB of span{e_a,e_b}. A third same-line mixed ray using a cannot occur, since these two fill that plane. The identical statement holds in every column.

Group all mixed Q cells using a by (i) their support pair `{a,b}`, and (ii) the projective orthonormal two-ray basis on that pair, up to phases and exchange. Every row or column that meets a group contains one ray from each of that group's two ray classes. A row cannot meet two groups: different support pairs containing a give a single nonzero-coordinate overlap, and two distinct bases on the same 2-plane give nonzero cross-overlaps. The chosen standardized row meets no group. If group g uses k_g rows, it also uses k_g columns, and `K=Σ_g k_g≤7`.

For any actual mate M, the k_g M rays over either fixed Q-ray class are pairwise orthogonal by Q⊗M. Rays from distinct groups have nonzero Q inner products: distinct support pairs share exactly a, while distinct orthonormal bases in one 2-space have no zero cross-overlaps. Therefore the mate spans of distinct groups are mutually orthogonal. Each of the 8−K other rows has a light Q=e_a cell, even if it contains other mixed Q rays avoiding a. The corresponding M rays are pairwise orthogonal and orthogonal to every group span. Consequently

`(8−K) + Σ_g dim(span M_g) ≤ 8`,

while each group span has dimension at least k_g. Equality holds throughout. Thus in every group the two k_g-ray mate classes are ONBs of the same k_g-dimensional space.

For any p cell of a group, its actual row and column contain two distinct q cells. These give two zeros in the corresponding transition-matrix row between its p and q mate ONBs. For distinct mates M,N, their transition supports are disjoint by M⊗N orthogonality. Three unitary matrices require three distinct nonzero positions in each transition row, so `k_g−2≥3`, i.e. `k_g≥5`. Since K≤7, there can be only one group.

## The one-group light-cell pigeonhole

Let its support be `{a,b}` and row count k. For each mate M, its group span W_M has dimension k, and the 8−k light-Q=e_a M rays form an ONB of W_M^⊥. All group Q rays use b, so comparison of their Q⊗M products with the standardized first-row product at b shows that the first-row M=e_b ray lies in W_M^⊥. The first row is one of the light-e_a rows and contributes M=e_a, which is perpendicular to e_b. Hence each mate must have nonzero e_b overlap at at least one of the **other** 7−k light-e_a cells.

Two distinct mates cannot choose the same such cell: their pair-product at that cell would have nonzero inner product with their first-row product at b. Three mates therefore require `7−k≥3`, or k≤4. This contradicts k≥5.

Thus an occupied mixed coordinate a cannot be used exclusively by support-2 mixed rays. The axis-cover conclusion follows for every chosen Q row. The proof allows arbitrary additional mixed rays avoiding a and does not infer nonzero inner products from multi-coordinate overlap without proof. Its group partition, exact dimension equality, transition zeros and off-first-row pigeonhole require independent full review; no parent, formal, human, executable, configured-family or novelty acceptance is asserted. The original four-family/global q1/q2/q3/q4 and exact A10/A11 questions remain open.
