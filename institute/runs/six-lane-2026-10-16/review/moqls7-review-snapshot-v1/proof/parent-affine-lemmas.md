# MOQLS(7): analytic versions of affine-plane Facts C and L

Parent derivation for independent review; not a claim that Problem16 is solved. These facts concern AG(2,7). Identifying a completed order7 net with AG(2,7) still imports uniqueness of the projective plane of order7, and extension of three MOLS still imports the cited classification. They are not replaced by the arguments below.

## Fact C: the two-symbol graph is one14-cycle

Take three distinct parallel classes of AG(2,7) as rows, columns and symbols. In affine coordinates the resulting Latin square is L(i,j)=a*i+b*j with nonzero a,b in F7, up to permutations of rows, columns and symbols. For two distinct symbols s,t, every symbol-cell has exactly one row-neighbour and one column-neighbour among the other symbol's cells, so their graph is a disjoint union of even cycles.

Start from an s-cell in row i. Its row-neighbour is the t-cell with column displaced by (t-s)/b. Moving next along the column to an s-cell changes the row by (s-t)/a. This nonzero additive step has order7 in F7. The alternating walk visits all seven s-cells and all seven t-cells, so the graph is a single14-cycle. Thus no enumeration of336 coordinate triples is needed for this fact.

## Fact L: every three free directions admit exactly two linear complement directions

The directions of AG(2,7) form P1(F7). GL(2,7) induces PGL(2,7), which takes any ordered triple of distinct directions to any other: the unique fractional-linear map can be constructed by sending the triple to infinity,0,1. We may therefore take the free set F={infinity,0,1}. Its complement has five possible directions c=2,3,4,5,6.

For a fixed c, change direction coordinates by f_c(x)=1/(x-c), taking c to infinity. The free directions become the three-element subset T_c={0,-1/c,1/(1-c)} of F7. In affine coordinates with c vertical, let L0 have x=0 and L1 have x=1. The points of L0 joined to q=(1,y) in a free direction are A(q)={y-f:f in T_c}. For distinct y,y', the size of A(q) intersection A(q') equals the multiplicity of y'-y among the directed differences of T_c. Hence all intersections have size at most1 exactly when those six directed differences are distinct (then they are F7 minus{0}).

All arithmetic in the following table is modulo7.

| c | T_c | Six directed differences all distinct? |
|---|---|---|
| 2 | {0,3,6} | No: difference3 repeats |
| 3 | {0,2,3} | Yes: exactly1,2,3,4,5,6 |
| 4 | {0,2,5} | No: difference2 repeats |
| 5 | {0,4,5} | Yes: exactly1,2,3,4,5,6 |
| 6 | {0,1,4} | No: difference3 repeats |

Exactly two complement directions are linear. The geometric property is invariant under the preceding invertible coordinate changes and rescaling the separation of L0,L1, so this proves Fact L for every free triple and every pair of distinct lines of the chosen complement class.

## Consequence for the proposed Theorem B

If a quantum assignment is an ONB on every line of five parallel classes, choose one of the two linear classes c in that five-set and a reference line L0. Every vector on another c-line has support, relative to the ONB on L0, contained in its three-element A(q). Distinct q on that line are orthogonal, and their allowed supports intersect in at most1 coordinate. An actual one-coordinate intersection would give a nonzero inner product, so actual supports are disjoint. Seven nonempty disjoint supports on seven coordinates must all be singletons. Thus all entries use the same seven rays and the assignment is classical.

This last conclusion assumes the five-net really comes from five classes of AG(2,7); the imported extension/uniqueness hypotheses remain essential. It proves neither the K2/K3/K4 support exclusions nor the symmetry-breaking soundness.
