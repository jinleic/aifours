# A complete order-twelve ternary counterexample search

**CATALOG-CONDITIONAL COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 22:34:03 PDT 2026**. This checks a new EVEN dimension outside the previously studied n8/n10 families. It found no cyclic-Fourier transversal in the two ternary classes; it does NOT prove a universal even-order obstruction.

Conditional on the two-class BH(12,3) classification in [Lampio–Östergård–Szöllősi Table2](https://arxiv.org/html/1707.02287v1) and its [Aalto supplement](https://wiki.aalto.fi/download/attachments/120482261/BH-12-3.txt?version=1%26modificationDate=1499265161013%26api=v2), every BH(12,3) Fourier-product QLS has NO orthogonal transversal, regardless of source-row order, row/column phases or ray multiplicity. Literal source input SHA **5f8d44af39ef67ae047db473adc1b82fce0cb1ce454ee88b6b8a9de1f4c7a0c0**; both programs directly validate both 12×12 Hadamards. The prior classification completeness is an import, not independently rederived.

Any transversal pairs physical rows r and r+6; column Gram zero and physical pair Gram zero force a perfect matching on each six-coordinate parity half. The 2×462 normalized source halves yield **84** matching halves. Each has `5!*6!=86400` normalized physical orders, for **7257600** total. A global physical row shift fixes the T cell `(0,0)` WLOG.

`frontier-20261028-bh12-3-even-counterexample-v1.cpp` SHA **487479dc4a8752c24bec62d820d9e8ced19d13b7edaba5cd72bafc95bf556537**, result SHA **1bd6e6ece54f458a4baa98df2e2bfe23afee8552bd1b9a94763f3be087c4f928**, uses exact Phi12=x⁴−x²+1 arithmetic and complete MRV DFS: **7466592** nodes, no T, and its 60-second budget was NOT reached (all orders completed).

Independent `frontier-20261028-bh12-3-even-replay-v1.cpp` SHA **f8003e3a5c681950c7298920b61f76036f9fb908aa30e905959b0037b9322031**, result SHA **f1a9b10a56bdf2f75d3f8998035c00c742a98e4e504eb27a564ac04863992053**, uses `Q(zeta6) + i Q(zeta6)` arithmetic, subset-DP matching and FIXED-row DFS: same924/84/7257600 coverage, **8483328** nodes and no T. They are full independent reexecutions with different DFS, not retained per-order proof certificates; the same symmetry caller and primary catalog are shared.

Other order12 Hadamards and phases, all larger even orders, and the original unrestricted order10 problem remain open. Catalog, caller, arithmetic and both programs require independent review before adoption.
