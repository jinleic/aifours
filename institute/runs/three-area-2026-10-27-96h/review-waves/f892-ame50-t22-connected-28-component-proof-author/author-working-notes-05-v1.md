# f892 author working notes 05 (scratch; never edited)

## Lemma N2 (connected case)
In every pair graph E_XY, each neighbour of a degree-2 vertex has degree >=3. Proof: degree-2 y, N(y)={u,u'}; its two rectangles in one cut family are {u,u'}x{y,y*},{u,u'}x{y,y**}. If y*=y**: DR (y degree 2) gives deg u, deg u' >=4. Else u,u' are both adjacent to y,y*,y** (degree>=3).
Corollary: no E_XY edge joins two degree-2 vertices; 2|X2|+2|Y2|<=14.
Also refined: a degree-2 vertex's neighbours, if of degree 3, are in case (b) and have N(u) subset N(u') etc.

## Exclusions via N2
- Any two six-symbol parties: |X2|,|Y2|>=4 -> 16>14. Kills connected 3566,3666,4466,4566,4666,5566,5666,6666 (simpler than notes 02/03 routes; 3566/3666 also by the (2,2,2,2,3,3)^2 cover argument).
- Six-party D=(2,2,2,2,2,4) with any partner having a degree-2 vertex: impossible (degree-2 partner vertices need two degree>=3 D neighbours; only one). Every party with q>=5 has a degree-2 symbol. So in 4556/5556 D=(2,2,2,2,3,3).
- With D=(2,2,2,2,3,3): every degree-2 vertex a of partner X has N(a)={t1,t2} and (case b forced, DR excludes doubling since deg t=3) N(t1)=N(t2)={a,a',a''} contains all degree-2 X vertices; |X2|<=3.
- Five-party partner of D: P2=(2,2,3,3,4) impossible (a' gets double edge -> the degree-4 f; f's second double edge {x,x'} with D2 x forces doubled {x,x'}x{f,n_x}, DR needs n_x degree>=4: none); P4=(2,2,2,3,5) impossible (degree-5 vertex needs 5 D2 neighbours, only 4). P1, P3 admit E_DA covers.
- Four-party partner of D (4556): (2,2,5,5) impossible; (2,3,4,5) impossible; (3,3,4,4) impossible (4456 argument); (2,4,4,4) admits cover; (3,3,3,5) open.
4456 status: connected excluded (notes 04).
