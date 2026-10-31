# f892 author working notes 02 (scratch, NOT candidate; never edited)

## L4 (square shape without twins)
No twins => every block of cut AX|YZ is (a,x,y,z),(a,x,y',z'),(a',x',y,z),(a',x',y',z') with a!=a', x!=x', y!=y', z!=z' (equalities give twins). Its XY cells form the all-E rectangle {x,x'}x{y,y'} (four distinct cells); likewise AY, AZ, XZ rectangles.

## L5 (rectangle double cover / links)
For parties X,Y separated by a cut, the 7 blocks of that cut give 7 rectangles (multiset) contained in E_XY covering every E_XY cell exactly twice (each cell has two words, each word in one block, block cells distinct). A vertex x of E_XY-degree d lies in exactly d rectangles; the column pairs of those rectangles form a 2-regular multigraph ("link") on N(x): degree 2 -> double edge; degree 3 -> triangle; degree 4 -> C4 or two double edges.
R1: degree-2 x, N(x)={y,y'}: rectangles {x,x'}x{y,y'}, {x,x''}x{y,y'}. If x'=x'' then {x,x'}x{y,y'} is an isolated K2,2 of E_XY (all four degree 2). Else y,y' have degree>=3 and N(y),N(y') contain x,x',x''.

## Exclusions obtained (connected case)
- Both sides (2,2,2,2,3,3): impossible (Case I all degree-2 in isolated K2,2 -> degree-3 starved; Case II -> T_Y={p,q}, N(p)=N(q)={x,x',x''}; subcase s=q leaves x4 stranded; subcase s!=q leaves remaining 3+3 degree-2 graph = C6, no rectangle).
- Sides (2,2,2,2,2,4) with (2,2,2,2,2,4): odd number (5) of degree-2 X vertices cannot pair into isolated K2,2, and a non-isolated degree-2 vertex needs two degree>=3 neighbours.
- Sides (2,2,2,2,2,4) with (2,2,2,2,3,3): non-isolated degree-2 X count odd (1 or 3, at most 3); 3 -> K3,2 then degree-4 starved; 1 -> x',x'' both must be the degree-4 vertex.
=> any profile with TWO six-symbol parties has no connected case: 3566,3666,4466,4566,4666,5566,5666,6666.
- 4456 via E_DA: D=(2,2,2,2,3,3) (P-moment bound), A=(2,4,4,4): a0's rectangles force N(t1)=N(t2)={a0,a*,a**}, fourth A symbol a3 adjacent to all D2, D2 vertex at a* has only one partner -> contradiction. A=(3,3,4,4): an alpha (deg 3) with two D2 neighbours forces three D2 with N={alpha1,alpha2} -> t's starved; else N(alpha_i)={t1,t2,u_i}; u1=u2 -> N(t)={alpha1,alpha2,beta}, beta link double edge, other beta'' starved; u1!=u2 -> N(beta)={t1,t2,u1,u2}, other beta'' starved.
Remaining connected profiles to treat: 4555, 4556, 5555, 5556.
