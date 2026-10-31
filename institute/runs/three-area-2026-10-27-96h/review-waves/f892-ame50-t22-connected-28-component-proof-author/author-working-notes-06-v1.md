# f892 author working notes 06 (scratch; never edited)

## Five-party pair lemmas (connected case), P1=(2,3,3,3,3) P2=(2,2,3,3,4) P3=(2,2,2,4,4) P4=(2,2,2,3,5)
- P1xP1: impossible (twin-pair argument, three placements of N(y0)).
- P1xP3: impossible (Y2 vertices pair into disjoint twin pairs of degree-3 X vertices; options (3) or (2,1); degree overflow at f).
- P3xP3: impossible (N(xi)={G1,G2}, N(yj)={F1,F2}; the two H-H cells cannot be covered).
- P2xP2: impossible (N(x1)={r1,r2} strands x2; N(x1)={r1,G} forces C4 link at G, x2=w, then x',x'' degree 3 strands F or degree 4 duplicates F).
- P4xP4: impossible (N(xi)={r,G}, N(yj)={s,F}; s overflows).
- P1xP2: a cover exists (not needed).
## Six-party partner
D=(2,2,2,2,2,4) impossible beside any party with q>=5 (N2). D=(2,2,2,2,3,3) beside a five-party X forces X in {P1,P3} (P2: double edge at f then DR; P4: degree-5 vertex starved).
## Profile closure (connected case, all 13)
3566,3666,4466,4566,4666,5566,5666,6666: two six-parties -> N2 count 16>14.
4456: D=(2,2,2,2,3,3); A,B forced (2,4,4,4) via E_DA/E_DB ((3,3,4,4) excluded); two-hole contradiction.
4556: B,C in {P1,P3} -> E_BC impossible.
5556: A,B,C in {P1,P3} -> any pair impossible.
4555: B,C,D in {P1,P2,P3} (degrees<=4); same-profile pairs impossible -> all distinct -> contains P1,P3 -> impossible.
5555: four parties in {P1..P4}; same-profile pairs impossible -> all distinct -> contains P1,P3 -> impossible.
=> NO connected 28-word E at any of the 13 profiles. With S5: 3566,3666,4456 wholly excluded; t22 reduces to 12+16 split on the other ten profiles.
