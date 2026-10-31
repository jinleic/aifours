# Order-eight counterexample search across the full BH(8,16) catalog

**CATALOG-CONDITIONAL COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 22:12:19 PDT 2026**. This is a direct search for an even-order cyclic-Fourier-product transversal, including non-Diţă Hadamards. It found none in the stated full finite catalog. It does NOT settle the arbitrary-complex-phase order8 or general even-order question.

## Scope and imported source

Conditional on the 2807-class monomial classification of BH(8,16) in [Lampio–Östergård–Szöllősi Theorem4.1/Table2](https://arxiv.org/html/1707.02287v1) and its [Aalto electronic supplement](https://wiki.aalto.fi/spaces/Butson/pages/120482304/Matrices+up+to+monomial+equivalence), EVERY BH(8,16) Fourier-product QLS has **NO orthogonal transversal**, even with repeated rays, arbitrary source-row order and row/column phases. The literal2807-line supplement used is `frontier-20261028-aalto-bh8-16-catalog-v1.txt` SHA **913992d501fa8f980daf0bc99d5b2d352a22364b4222de4c88890c2682989339**. Both programs independently validate ALL listed Hadamard rows and columns exactly. Their checks do not regenerate the source classification's completeness.

## Complete finite caller

Any transversal pairs physical row r with r+4, so K-column orthogonality plus the physical pair inner product forces a perfect matching of the eight K columns whose inner sums vanish separately on even and odd physical coordinates. For every representative, test all35 source-row four-subsets containing source row0; a cyclic coordinate shift and possible parity swap put ANY half choice in this normalization. Of **98245** such source halves, **48547** have a perfect matching. Each normalized half has `3!*4!=144` physical orders, giving **6990768** orders. A common physical-row shift moves the transversal's column0 cell to row0, so fixing that cell loses none.

Exact program `frontier-20261028-bh8-16-even-counterexample-v1.cpp` SHA **74da4aa5abee0239a9c3435166ae6dd8f5ef92b3f1257c1f71c02ccf12a98c24**, result SHA **3717c3d5468b424f3760cbd2f165611207bfcce62ef6b30d467d37b93d6a4526**, uses the `Phi16=x^8+1` integer basis and complete MRV backtracking on actual physical overlaps. It visits **8413196** DFS nodes and finds no transversal.

Independently written `frontier-20261028-bh8-16-independent-replay-v1.cpp` SHA **b031c3ca1ab0f4e6ec48eabe0f74446af876001f0addc1efdb67d4d63432e1d5**, result SHA **31bb210cc8c5dd675a6de731ba7479c3f1473a8afd423536f363e5b9d8277422**, regenerates all source matrices, halves, matching tests and physical orders in the tensor basis `Q(zeta8) + zeta16 Q(zeta8)`, uses subset-DP matching and FIXED-row backtracking, visits **8978888** nodes and likewise finds none. The different node counts are expected from the different DFS ordering. Both are full re-executions, not a retained per-order proof-certificate replay; they share the same finite mathematical symmetry caller and source catalog.

BH(8,4) and BH(8,8) are subsets because4|16 and8|16, so they are included. No general K or arbitrary-phase conclusion follows. A separate bounded floating search and the published non-Fourier 1-RQLS8 example do not change this boundary. The catalog, normalization and both programs require independent full review.
