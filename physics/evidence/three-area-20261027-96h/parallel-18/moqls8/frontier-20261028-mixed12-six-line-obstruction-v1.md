# No 12-cell four-family member with six mixed columns

**WRITTEN author candidate; disjoint full review pending.** In an ordinary four-MOQLS(8), no member Q can have exactly 12 mixed cells relative to a chosen actual Q row and exactly six mixed columns. The incidence-transposed statement with six mixed rows also holds. Q and its three mates are arbitrary complex QLS; no classical mate, catalogue, phase or equal-modulus hypothesis is assumed. This excludes one complete 12-cell stratum, not all 12-cell shapes or the four-family target.

Named WRITTEN imports, not yet independently accepted: `frontier-20261028-exclusive-axis-cycle-bound-v1.md`, SHA256 0464e54938c55b35f45c81074f5736f93edfed4827ce3309d3afa6301939407b, for exclusive-axis support-2 cycles; and `frontier-20261028-four-family-no-degree2-mixed-graph-v1.md`, SHA256 5c925ec7df05ef4ec2d533248733938aa2ffadc99a73cae8205bb6ac4b2bd0a8, for an entirely degree-2 mixed incidence graph.

## A bridge of three rectangles

Use the chosen Q row and independently standardize all four members there to their respective coordinate bases. Suppose three mixed 2×2 rectangles have constant Q support sets U,V,W; U∩V=∅ and W meets each of U,V in exactly one coordinate. Suppose the U and V rectangles use disjoint columns and share at least one row. Then at most three family members exist.

For any mate M, each rectangle's four M rays are pairwise orthogonal: row/column pairs are orthogonal as QLS entries and opposite corners have collinear Q rays, forcing orthogonal M rays by Q⊗M. Every U-rectangle Q ray overlaps every W-rectangle Q ray in exactly one nonzero coordinate; likewise for V against W. Consequently the U and V M quadruples are each ONBs of the four-dimensional orthogonal complement of the W M quadruple. Their transition matrix is unitary. For either U-cell in a shared row, its two transition entries against the two V-cells in that row vanish. In that fixed matrix row at most two positions can be nonzero. For distinct mates, M⊗N product orthogonality makes their transition supports disjoint, whereas each transition row is nonzero. Hence at most two mates are possible, i.e. at most three members including Q.

In the cases below, U and V are disjoint because their support-2 rays appear on the same actual mixed Q row. If W fails to meet U, the U rectangle has an exclusive axis; if W fails to meet V, the V rectangle does. Such an exclusive C4 already excludes a single mate by the imported cycle bound. Otherwise the size-2 set W meets each of the disjoint U,V in exactly one axis, so the bridge argument applies. This exhausts the possible W, including W=U or W=V in the exclusive-axis alternatives.

## Degree and support setup

Six mixed columns with 12 cells means every mixed column has degree 2, and both Q rays there have the same support 2. Every incident row has even mixed degree: support-2 rays on one line have identical or disjoint supports, and each support plane is filled by exactly two orthogonal mixed rays. Thus the possible row profiles are `(6,6)`, `(6,4,2)`, `(4,4,4)`, `(6,2,2,2)`, `(4,4,2,2)`, `(4,2,2,2,2)`, and `(2,2,2,2,2,2)`. Regard each column as an edge between its two incident rows; parallel edges represent different columns. Along each degree-2 row and column, the two Q rays have the same 2-support. A degree-4 row contains two disjoint support pairs, each twice; a degree-6 row contains three pairwise-disjoint support pairs, each twice.

The `(6,4,2)` and `(4,4,4)` profiles are excluded by the explicit C4/C6 analysis in the imported cycle packet; the degree-2 profile is excluded by the imported no-degree-2 theorem. In `(6,6)`, all six column edges join the two rows. The degree-6 row uses three pairwise-disjoint support pairs, each twice, so there are three 2×2 rectangles on pairwise-disjoint supports; each is an exclusive C4.

## Four mixed rows

For `(6,2,2,2)`, all six column edges meet the degree-6 row. Each degree-2 row receives two of them and therefore supplies a constant-support rectangle. The three supports are pairwise disjoint in the degree-6 row, so each rectangle has an exclusive axis.

For `(4,4,2,2)`, denote the degree-4 rows A,B and the degree-2 rows C,D. Let e be the number of column edges between C and D.

* e=2: C,D form one W rectangle and A,B share four columns. The latter yield two rectangles with disjoint supports U,V. If W misses one of U,V, that rectangle is exclusive; otherwise the three-rectangle bridge above gives t≤3.
* e=1: C and D each have one remaining edge, and the degree equations force one to A and one to B; the remaining three edges join A to B. Propagating the common low-row supports gives one C8 on support U (the A–C–D–B path plus one A–B edge) and one C4 on a disjoint support V (the other two A–B edges). The V rectangle is exclusive.
* e=0: two edges join A,B, and the other four join high to low rows. Each high row has two high/low edges. If C joins A twice and D joins B twice, the two A–B columns have one common support W disjoint from both low-row supports, and give an exclusive rectangle. Otherwise each low row joins A and B once. If both low-row paths have the same support U, the two A–B columns give a disjoint exclusive-support rectangle V. If they have distinct supports U,V, they are disjoint in row A and the two A–B columns split between U,V; the supports give two exclusive C6s. These cover the high/low degree equations up to swapping A,B or C,D.

## Five mixed rows

For `(4,2,2,2,2)`, let A be the degree-4 row and C,D,E,F the degree-2 rows. Of the six column edges, four meet A and two connect low rows.

* If the two low/low edges are parallel, they give one W rectangle. The other two low rows each join A twice, giving rectangles U,V with U∩V=∅. The exclusive-axis alternative or bridge lemma rules out a four-family.
* If the two low/low edges share one low row but are not parallel, the remaining low row joins A twice and supplies an exclusive U rectangle. The other two A edges are connected through the low/low path and use the disjoint support V forced on A.
* If the two low/low edges are disjoint, each completes a three-edge path from A back to A. The two paths are support-2 C6s with disjoint supports in A, and each has an exclusive axis.

In all cases the 12-cell/six-column stratum is excluded. Transposing the incidence argument preserves the originally selected Q coordinate basis and gives the six-row statement. No conclusion is asserted for the remaining 12-cell boards with at most five mixed rows and columns, and no q2/q3/q4, M(8), A10/A11, formal or novelty gate is closed.
