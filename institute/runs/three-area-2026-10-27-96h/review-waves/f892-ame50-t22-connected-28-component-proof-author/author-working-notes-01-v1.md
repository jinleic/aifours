# f892 author working notes 01 (NOT the candidate; exclusive scratch record, never edited)

Packet read complete before this file: part01 raw windows 1-20,...,401-418 (ending S7|119); part02 raw windows 1-20,...,401-416 (ending S10|139). No clipping observed (raw mode, all windows < 30000 B).

## Established written lemmas (connected 28-word E, actual N50/t22 tensor)

L1 (twin closure). If two E words differ in exactly one coordinate, say w=(a,b,c,d), w'=(a,b,c,d'), then AB, AC, BC values of w are saturated by {w,w'}. In AD|BC the column (b,c) has rows (a,d),(a,d'); its K2,2 partner column (b2,c2) gives twins (a,b2,c2){d,d'} with b2!=b, c2!=c. Likewise AB|CD gives twins (a3,b3,c){d,d'} (a3!=a,b3!=b), AC|BD gives (a4,b,c4){d,d'}. Every twin triple has exactly one twin neighbour sharing exactly A, B, C respectively, with the SAME D pair {d,d'}. The closure T x {d,d'} is closed under all six mate involutions, hence is a whole agreement component with D-alphabet of size 2. Connected 28 has every q_i>=3, so: NO TWINS. Consequences: every word has six distinct mates (agree in exactly two coordinates); agreement graph 6-regular with proper 6-edge-colouring by pair; slice of a degree-d symbol induces a cubic 3-edge-coloured graph on its 2d words.

L2 (degree two = parity tetrahedron, flat moduli). Degree-2 slice: three balanced partitions; coincidence of two = twins (excluded), so all distinct: words (x,b_i,c_j,d_k), i+j+k even (after local relabel). It contains triangles -> odd cycle -> p_w=1/2 on the whole connected component. Every one of the 13 profiles has a party with q>=5, which forces a degree-2 symbol (five or six symbols with degree>=3 would sum >=15>14). Hence in the connected case ALL 28 E moduli are exactly 1/sqrt2 (forced, not chosen).

L3 (degree three slice). Six words, pairwise share <=1 of the other coordinates; each other-pair projection is a 6-cycle (K3,3 minus perfect matching) on the 3+3 neighbour symbols; induced slice graph is K3,3 or triangular prism.

P incidence: a degree-d symbol has 6-d P words, which use each non-neighbour symbol of every other party exactly once.

Signed-square dual: each word lies in exactly 3 squares (one per cut); within a square the two words of one row have opposite signs. A +-1 odd dependency = odd set S of squares, each word in 0 or 2 of them, balanced signed graph.
