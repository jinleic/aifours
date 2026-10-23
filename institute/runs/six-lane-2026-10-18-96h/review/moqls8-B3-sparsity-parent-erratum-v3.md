# B3 sparse-axis proof: second-family precision erratum v3

Recorded at 2026-10-19T16:21:57-0700. Apply after immutable candidate `46288f4efae9815aa5e428cc74e7293b116e2d744a6d16b2e6fedf5c9ee8ac2e` and parent erratav1(a9748009),v2(021bfe54). Disposes five MINORs of [Claude](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/moqls8-B3-sparsity-claude-v2.prompt.note.md) `c475c98915af535233115ffa5d50c7881578419d521f4ca86ae1925eb32d078b`;0F/0M. No theorem statement weakened or enlarged.

1. **A-1, line47.** Begin “Suppose the two supports meet. If they meet in exactly one column, …; if in two, both equal some {a,b}.” The disjoint alternative is already the desired conclusion.
2. **C-1, line198.** Read “B4 lists exactly the item-2 shapes with n_s<=8. The only other item-2 shape, full3x3 and possible only in case(b), is excluded by items2-3 jointly:9+3*3=18>17=|Z|.” This avoids importing a necessity-side bound into sufficiency without proof.
3. **C-2, heading180, lines202/264.** The exact residual S characterizes **row-0/column-0 data only**. For full H1-H4 configurations membership in S is only necessary. Nonempty S proves neither a full configuration nor an extension.
4. **D-1, line238.** Replace the clause-evaluation phrase about M_2,M_3,M_4,M_5 by “all four X_s are permutation supports.” No Boolean clause or arbitrary-model statement is certified.
5. **G-1, line270.** Replace undefined W8 attribution by the direct conditional fact: under standard row0 H2, tensor orthogonality between (0,c) and (i,j), i>=1, gives disjoint common-frame supports Q_s(i,j),Q_t(i,j) for s!=t. This is the B0(ii) argument applied to those cells, not a new template or completed-grid implication.

Earlier phase correction (independent phases per monomial entry), full3x3 Fourier example, precise primary excerpt range and direct-axis-only route obstruction remain mandatory. No T-exclusion is inserted into this old packet; the later interior candidate re-proves a stronger degree bound independently.
