# Parent disposition - uniform classical-neighborhood rigidity for m-MOQLS(n) (f2)

Observed native clock before writing: **2026-10-28T17:21:08-0700 PDT**. Same-harness written support; not formal/kernel, human, configured-family or novelty acceptance. Frontier-first direction: [contract addendum 2](../contract-addendum-2-frontier-first-owner-direction-v1.json).

## Complete reads by Main

| Input | SHA-256 | LF | Read |
|---|---|---|---|
| Candidate `frontier-20261028-uniform-classical-neighborhood-v1.md` (PhysicsMOQLS8-2) | `12d8a6e3e3c27ff0e5c776a196578a94ed1010f907986680ef74c0e7f42eb8aa` | 141 | raw 1-141 through ending |
| Review `frontier-review-f2-moqls-neighborhood-v1.md` (InfoResearch96h-2) | `dd325e80dfaf34dcefc5e3ac58b94655f13b85b30a9edf24b5704bba2f122238` | 170 | raw 1-170 through ending |
| Assignment `review-waves/f2-moqls-neighborhood/assignment-v1.json` | `21ff09e930d7d884e707783ddaf36f12a447132367fd81eba8866ce3376be448` | 20 | frozen before dispatch |

## Adopted statement (exact scope)

**Theorem.** Let n >= 2 and m >= 1 with 2(m+1) > n. Let C be any actual classical labelled m-MOQLS(n) family (member a has its own ONB and Latin symbol map L_a, independent cell phases) and Q any actual complex m-MOQLS(n) family on the same labelled grid (every member a QLS; every pair of members has all n² same-cell tensor products forming an ONB). If the maximum over members and cells of the projective chordal distance sqrt(1 - |<Q_a(i,j), C_a(i,j)>|²) is at most 1/[8n(n+1)], then there are separate unitaries U_a and cell phases with U_a Q_a(i,j) = λ_(a,i,j) e^a_(L_a(i,j)) for all a,i,j; in particular every member of Q is classical. Hence any actual nonclassical m-family has distance strictly greater than 1/[8n(n+1)] from every labelled classical reference. For n=8, m=4 the radius is 1/576.

## Parent verification

Main reconstructed the proof by hand: (i) for member a and symbols p != q, the row, column and m-1 companion-symbol classes are m+1 pairwise edge-disjoint perfect matchings between the n p-cells and n q-cells (Latin property and the pair-product ONB of the reference, which forces every ordered symbol pair exactly once), giving a simple (m+1)-regular bipartite graph; 2(m+1) > n forces any two same-side vertices to share a neighbour (distance <= 2 from the first-row anchors); (ii) alignment: with phases chosen so reference overlaps are nonnegative, ||v - e||² = 2(1 - sqrt(1-d²)) <= 2d², so the first-row unitaries satisfy ||F - E||_op <= 2 sqrt(n) η, U_a = E F* fixes the first row exactly and ||U_a - I||_op <= 2nη, hence every cell's leakage δ <= 2(n+1)η = 1/(4n); (iii) every companion edge gives |<Q_b(x),Q_b(y)>| >= (1-δ²) - δ² > 0, so the pair-product ONB forces the exact selected-member zero <Q_a(x),Q_a(y)> = 0, while row/column edges are exact zeros by the QLS condition; (iv) expanding the exact zero gives |c_(y,p) + conj(c_(x,q))| <= δ²(1+2δ) on every edge, anchors have potential 0, distance <= 2 gives |c_(x,q)| <= 2δ²(1+2δ), hence δ <= 2 sqrt(n-1) δ²(1+2δ); with δ <= 1/(4n) and sqrt(n-1) <= n this forces 1 <= 1/2 + 1/(4n) < 1 unless δ = 0. The argument is nonlinear and uses no tangent integrability, support bound or classicality of Q.

Reviewer verdict NO_SUBSTANTIVE_DEFECT, 0F/0M/0m, including the vacuity accounting for m+1 > n, the n=2 empty-sum case, and the exact n=8 constants (δ <= 1/32, contraction factor 17/32); the reviewer's exact small-order incidence enumeration (n = 2,3,4) is diagnostic only. The author's GF(8) finite control was read as a claim, not executed by Main.

## Not established

Existence or nonexistence of a nonclassical four-MOQLS(8) at distance greater than 1/576 from all classical references; connectedness of the solution space; M(8); any equality-case 2(m+1) = n statement; novelty (NR). The adopted five-family classicality and this local theorem are separate results. Historical quarantines for this slot remain historical records, not premises.
