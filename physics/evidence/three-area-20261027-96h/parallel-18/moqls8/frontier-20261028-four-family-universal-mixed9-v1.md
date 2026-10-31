# Every nonclassical member of a four-MOQLS(8) has at least nine mixed cells

**WRITTEN author candidate; no classical-mate, catalogue, numerical solver or finite-witness premise. Disjoint full mathematical review is essential.** In any actual ordinary four-MOQLS(8), choose any member Q and any actual Q row as its coordinate ONB. If Q is nonclassical, at least **nine** of its 64 cells are not rays of that row. The other three QLS may all be arbitrary complex and nonclassical.

This is a universal structural bound, not a proof that every four-family is classical, an M(8) bound, an A10/A11 qualification or a novelty claim. It imports two separately review-pending WRITTEN candidates: the universal ≥8 bound `frontier-20261028-three-qls-universal-mixed8-v1.md` (SHA256 7464f79b7bddaf7c4345544b2fad332d6c1b56698238df4cee215bc790d63a7f), and the no-degree-two-incidence-graph result `frontier-20261028-four-family-no-degree2-mixed-graph-v1.md` (SHA256 5c925ec7df05ef4ec2d533248733938aa2ffadc99a73cae8205bb6ac4b2bd0a8). This packet excludes every possible **eight-mixed-cell** graph not already excluded by the latter.

## 1. Basic line facts and exhaustive graph shapes

Independently normalize Q and its three actual orthogonal mates R,S,T on the chosen first row to their own coordinate bases e_j with common column labels. A Q cell is *mixed* if it is not a first-row basis ray. Every row or column meeting the mixed set H contains at least two mixed points: on any coordinate occupied by a mixed ray no same-line singleton can occur, and ONB completeness requires another mixed ray on that coordinate.

On a line with exactly k mixed rays, the n−k light singleton rays occupy distinct coordinate axes, so its mixed rays form an ONB of the complementary k-dimensional coordinate space. In particular, two mixed rays have the same two-axis support, and on a three-mixed line at most one ray has support size 2. Indeed, distinct 2-subsets of three axes intersect once and cannot be orthogonal; two orthogonal rays with the same 2-support force the third to be the remaining singleton.

Suppose `|H|=8`. If r rows and c columns meet H, minimum degree two gives r,c≤4, while rc≥8. Up to exchanging “row” and “column” in the argument, the only possibilities are

`(r,c)=(2,4), (3,4), (3,3), (4,4)`.

For `(4,4)`, every incident row and column has degree exactly 2, excluded by the named no-degree-two theorem. All remaining cases are handled below without assuming any classical mate.

## 2. The (2,4) and (3,4) shapes contain an isolated two-axis rectangle

In either case all four incident columns have exactly two mixed cells. Every mixed ray therefore has support size 2. A row with exactly three mixed rays would contain three support-2 rays, contradicting the line fact above. Thus `(2,4)` has two degree-4 rows, and `(3,4)` has row degrees `(4,2,2)`.

On the degree-4 row, its four mixed rays form an ONB of a four-coordinate subspace and each has support size 2. Distinct 2-supports cannot meet in exactly one coordinate, and no two-dimensional support can contain more than two orthogonal rays. Hence the four supports are exactly **two disjoint two-sets**, each used twice. The two mixed cells in every incident column have equal supports. In the `(2,4)` case this gives two 2×2 mixed rectangles, one for each disjoint support. In the `(3,4)` case each degree-2 row has one common 2-support and occupies the two columns in that same support group, so the mixed cells again split into two 2×2 rectangles, possibly sharing the degree-4 row. The two rectangles have disjoint coordinate supports.

Choose one rectangle H_0 with two-axis support `{a,b}`. Its four Q rays alternate between two collinear ray pairs; opposite parts share a row/column. For any actual orthogonal mate R, same-part R rays are orthogonal by Q⊗R and opposite-part R rays are orthogonal by R's row/column ONB. Thus the four R rays on H_0 are pairwise orthogonal.

No mixed Q ray outside H_0 uses axis a, because the other rectangle's support is disjoint. H_0 occupies two rows. In each of the other six rows, all mixed Q rays avoid a and the remaining Q rays are light, so the row ONB contains exactly one light Q=e_a ray. Their six R rays are mutually orthogonal and each is orthogonal to all four R rays on H_0 by Q⊗R. Ten nonzero orthogonal rays cannot fit in C^8. The cases obtained by exchanging row and column use the identical argument along columns, **without changing the chosen first-row coordinate basis**.

## 3. The (3,3) shape forces three incompatible partial 3×3 QLS

With three incident rows and columns and eight edges, the mixed graph is K3,3 with one missing cell. Relabel these rows and columns so the missing mixed cell is (2,2). Two rows and two columns contain three mixed cells; the remaining row and column contain two. The four cells in the upper-left 2×2 lie on both a three-mixed row and a three-mixed column. In each such row or column, the cell in the degree-2 column/row has support size 2, so the other two mixed rays must have support size 3. The four 2×2 corner rays therefore all have support size 3; their three-coordinate row/column subspaces coincide along intersections. Call the common three-axis set T.

The two rays in the degree-2 row have one common two-axis support U⊂T; the two rays in the degree-2 column have one common two-axis support V⊂T. They cannot be equal. If U=V, each upper-left Q ray has a nonzero projection to this two-space and must be orthogonal both to its row's degree-2-column ray and its column's degree-2-row ray. Those two rays would have to be collinear. For either fixed upper-left row, this would force the two orthogonal rays in the degree-2 row to be collinear, contradiction. Thus U and V are different 2-subsets of T and intersect in one axis a. Every one of the eight mixed Q rays has nonzero coordinate a.

The three mixed rows leave five rows containing only light Q rays. Each has a unique Q=e_a cell. For any mate R, those five R rays are mutually orthogonal and orthogonal to all eight R_H rays by the actual Q⊗R product ONB. Hence `dim span(R_H)≤3`. Any full three-mixed row supplies three orthogonal R rays, so their common span V_R has dimension exactly 3. The same is true independently for S and T.

The eight R_H rays occupy a 3×3 grid missing (2,2); its first two rows and first two columns are ONBs of V_R, and its final row/column each contain two orthogonal rays. Comparing the sum of their eight rank-one projectors by rows and by columns gives

`P_(2,0)+P_(2,1) = P_(0,2)+P_(1,2)`.

Both sides are rank-two orthogonal projections. Their one-dimensional complements in V_R are therefore the same ray. Adding that ray at the missing cell completes the eight **actual** R_H rays to a 3×3 QLS on V_R. Do the same independently for S and T; no claim is made that these auxiliary missing rays equal the original family rays at (2,2).

Every order-3 QLS is classical. For completeness, normalize its first row to e_0,e_1,e_2. Its next row has the form `(0,a,b),(c,0,d),(e,f,0)` in those coordinates. If all three rays had support 2, each pair would have exactly one common nonzero coordinate and could not be orthogonal; hence one is a singleton. That singleton, the column zeros and row orthogonality force the other two second-row rays to be the remaining singletons, and each last-row ray is then forced by its column. Thus all rays are from the same ONB.

Independently label the first row of each completed R,S,T 3×3 QLS as symbols 0,1,2. A Latin square of order 3 with that first row has only **two** possibilities: the other two rows are the two cyclic derangements, in either order. Among three mates, two have the same symbol pattern. In the eight actual cells each symbol occurs at least twice, so for two distinct actual cells both mates have collinear rays in both factors. Their original pair-product vectors then have nonzero overlap, contradicting the actual R⊗S (or corresponding) product ONB. The auxiliary ninth cell is not used in this contradiction.

All eight-cell graph shapes are impossible in an actual four-family. Together with the named universal ≥8 bound this proves the candidate **≥9**. For q4 the summed support-surplus is at least 36, with overlaps between members allowed; for q3 it is at least 27, while stronger results may hold when a classical mate is present. These lower budgets alone do not exceed the total 168-unit upper budget and are not a global q3/q4 exclusion.

A disjoint reviewer should reconstruct the degree enumeration, the isolated-rectangle occurrence count, the common-axis 3×3 span bound, the projector-sum completion and the order-3/pair-product pigeonhole independently, and should review both named written imports before adoption.
