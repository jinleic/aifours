# f892 author working notes 03 (scratch; corrects notes 02; never edited)

## Correction of notes-02 R1 (self-found error)
A doubled rectangle {x,x'}x{y,y'} (same rectangle twice in one cut family) only forces a DOUBLE EDGE in the links of x', y, y'. A vertex with a link double edge has degree 2 OR >=4 (link = 2C2 or double edge + other cycles). "Isolated K2,2" follows only where all four degrees are <=3.
Consequences:
- (2,2,2,2,3,3)x(2,2,2,2,3,3) exclusion STANDS (all degrees <=3). Hence 3566 and 3666 connected cases excluded (their two six-parties have degrees <=3).
- (2,2,2,2,2,4)^2 exclusion re-proved: every degree-2 X vertex is in a doubled pair (case b impossible: needs two degree>=3 Y neighbours); count of doubled pairs at X4 is odd -> exactly one; X4's other two rectangles need non-degree-2 partners other than X4: none.
- (2,2,2,2,2,4)x(2,2,2,2,3,3): a rectangle cover EXISTS (K3,2 + doubled {x4,X4}x{y1,y2} + doubled {x5,X4}x{y3,y4}). NOT excluded by E_XY alone. Profiles 4466,4566,4666,5566,5666,6666 therefore NOT yet excluded.
- 4456 via E_DA: (2,2,2,2,3,3)x(2,4,4,4) has a cover (doubled {x,y}x{a0,a*}, {t1,t2} triangle-ish, doubled {r1,r2}x{a3,a4}); notes-02 4456 argument INVALID as written.

## New lemma DR (doubled rectangle, word level)
Cut DB|AC, two blocks with D-pair {x,y}, A-pair {a,a'}: words (x,b1,a,c1),(x,b1,a',c1'),(y,b1',a,c1),(y,b1',a',c1') and (x,b2,a,c2),(x,b2,a',c2'),(y,b2',a,c2),(y,b2',a',c2'); b1!=b2, c1!=c2, b1'!=b2', b1'!=b1, b2'!=b2. If x has degree 2 (tetrahedron) then L4 gives b1',b2' outside {b1,b2}, so a (and a') has >=3 B-neighbours; with the double edge, deg a, deg a' >= 4. Symmetrically a degree-2 A vertex forces deg x, deg y >= 4.
L4 (proved): for degree-2 x with tetrahedron, every mate through a pair not containing x's party has its third (non-x, non-shared) coordinate outside x's pair there (equal to one end gives twins or an 8-word box).
