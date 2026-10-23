# Local P0 projections and private-row capacity v1

Written after host clock 2026-10-19T14:01:52-0700; necessary constraints only.

Fix a P0 column c. Its complement of Q_c has eight nonempty rows and seven empty rows. Within a triple no two nonempty rows may have intersecting T-sets, no type may contain c, and no pair may have already agreed in P1 or in another P0 column.

The five occupancy categories give the following COMPLETE count projections for its five triples (nonempty counts, not completed triples):
- Every normal column: (2,2,2,1,1). Thus its eight N rows must be partitioned into three allowed pairs and two single rows. The three pairs take one E row each; the two singles take two E rows each. Which actual E rows are used must still be checked, including all E-E and E-N pair histories.
- The exceptional C3 column: (2,2,2,2,0). Thus four allowed N pairs plus one all-E triple of three distinct E rows.
- The exceptional C0 column: (3,2,1,1,1). Thus one allowed N triple, one allowed N pair, three N singles.
These follow directly by subtracting eps from3 in the exhaustive occupancy vectors. They are necessary count projections, not independent realizability assertions.

For b66/b68 all nonempty types have size1 or2. Any N triple of a P0 column must contain at least TWO private rows: three two-types would need six indices and two two-types plus a private would need five, whereas only the four indices other than c are available. The two private types must be distinct and neither equals c; their row identities remain distinct (in particular p0,p0' cannot be together). Any all-nonempty P1 triple, or the three N rows in the exceptional Q1 quad, must contain at least ONE private row, since three disjoint two-types need six indices but there are only five. These constraints further restrict C0/Q1/T2 but do not close them.

In category T2 for b66/b68 the sole nonempty member r of the eps2 P1 triple must be a two-type, not private. A private cannot be paired (R1 forbids private pair endpoints in T2), so its pattern would be (0,2,1). Then its four P0 triples contribute at least4, its quad at least2, and the eps2 P1 triple contributes2, already I>=8, impossible. If r is a paired two-type (1,1,1), its quad must have eps2 and its three P0 triples eps1: they contribute at least3+2+2=7, so equality is forced. If r is an unpaired two-type, all its P1 blocks are triples and the remaining choices are not excluded.

For every Q_c and every P1 column, its four rows must occupy four distinct blocks (rainbow). For different P1 columns, block intersections have size at most1. These constraints apply to actual row-labelled blocks, including empty-row assignments; they cannot be discharged by satisfying scalar occupancy or the all-triple graph alone.

No whole case closes here. The remaining obligations in rainbow-and-completion-v1.md continue to include all actual row/empty placements and all five P0 partitions jointly.
