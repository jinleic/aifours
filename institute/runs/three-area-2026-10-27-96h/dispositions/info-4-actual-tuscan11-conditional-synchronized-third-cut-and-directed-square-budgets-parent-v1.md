# Conditional actual T2(11): synchronized third cut and directed-square budgets

**Disposition: scoped same-harness written support plus an independently authored, exact physical-interface checker run once by the parent.** Assume (i) eleven ACTUAL permutation rows on the same eleven finite symbols form T2(11), (ii) the missing finite distance-two set M equals the actual last-to-first closing set C, and (iii) distinct six-symbol odd-position supports B,D each occur exactly three times. Then the same physical augmented Hamilton cycles satisfy the synchronized T=13 or T=14 restrictions below. Neither full T branch is excluded or constructed, M=C is not proved universally, and unrestricted T2(11) remains OPEN.

## Actual cycles and conditional square transport

Append one infinity vertex to each actual row to form a connected directed **12-vertex** Hamilton cycle. The original 110 finite adjacent events exhaust the finite directed arcs, forcing first and last columns each to be a permutation; all eleven cycles therefore partition all132 directed nonloop arcs on the SAME twelve vertices.

Under the indispensable premise M=C, their directed squares also partition all132 arcs: each square’s finite arcs are precisely nine original linear distance-two events plus the actual last-to-first closing pair; the two remaining arcs use infinity and the second/penultimate positions. M=C makes those columns permutations as well. The square of one connected twelve-cycle has two six-cycle orbits; it is not an eleven-cycle square, and arbitrary disconnected cycle covers are not substituted for the original Hamilton cycles.

The two tripled supports obey \(|B\cap D|=3\). Write the four three-vertex cells \(I=B\cap D,\ J=B\setminus D,\ K=D\setminus B,\ L=X\setminus(B\cup D)\), with infinity in L, and \(E=J\cup K=B\triangle D\). The six alternating cycles for B,D are disjoint, leaving the SAME five residual actual cycles. Let T be the sum, across those six alternating cycles, of each cycle’s run count in the other cut. For each cell the residual layout counts (full length-three run, pair plus singleton, three singleton runs) are forced to

\[T=13:(1,4,0),\qquad T=14:(2,2,1).\]

The three-full alternative is impossible because the six directed arcs on three vertices cannot be partitioned into three directed spanning paths. The proof uses the actual square decomposition, not independently specified cell ledgers.

## Synchronization on the same cycles

A residual adjacency joining opposite cells I–L or J–K forces both endpoints into nontrivial same-cell runs; at most one such join of each type occurs in one connected Hamilton cycle. Each opposite pair has exactly \(18-T\) residual joins.

- **T=13:** demand five saturates capacity, so EVERY one of the five residual cycles has exactly one I–L join and exactly one J–K join. No cycle has E as its alternating cut: \(k_E=0\).
- **T=14:** each cell has one all-singleton occurrence. Capacity forces I and L to have it in the same cycle; the actual 12-cycle then alternates across E, forcing J and K’s all-singleton occurrences into that SAME cycle \(h_E\). The four remaining residual cycles each have one join of each opposite kind. The cell word of \(h_E\) follows an orientation of I–J–L–K repeated three times while the underlying twelve labeled vertices remain one connected cycle. Its actual finite odd support is E, so \(k_E=1\).

For each regular residual cycle the number f of full cells is0,2,4, and f=2 uses an EDGE of the I–J–L–K cell square, not an opposite pair. Synchronized full-count patterns are:

| T | Regular-cycle full counts | Additional matching constraint |
|---|---|---|
| 13 | (4,0,0,0,0) or (2,2,0,0,0) | The two size-two masks form opposite edges. |
| 14 | (4,4,0,0), (4,2,2,0), or (2,2,2,2) | In the middle case the two size-two masks are opposite edges; in the last, edge multiplicities are \((x,2-x,x,2-x)\), \(x\in\{0,1,2\}\). |

These are simultaneous necessary conditions, not claims that the indicated schedules admit mutually compatible vertex labels or global decompositions.

## Actual directed budgets and vertex coupling

Neither B- nor D-alternating family contributes a square arc between opposite cells. The nine directed square arcs in each opposite-cell direction are residual. A diagonal adjacency contributes exactly two square arcs of its own direction; remaining contributions are centered at singleton cell vertices. If \(a,a'\) are residual opposite-direction I–L join counts, then:

- T=13: \(a+a'=5\), \(9=2a+u\), \(9=2a'+u'\), so \(1\le a,a'\le4\).
- T=14: \(h_E\) contributes three square arcs in EACH direction; among four regular cycles \(a+a'=4\), \(6=2a+u_{reg}\), \(6=2a'+u'_{reg}\), so \(1\le a,a'\le3\).

The analogous constraints hold for J–K. If x,y are I→L,L→I counts from the B-family and u,v from the D-family, their total is T and the four residual directions are \(9-x-u,9-y-v,9-x-v,9-y-u\). Thus EVERY cross sum c among \(x+u,x+v,y+u,y+v\) is in \([T-8,8]\), equivalently \(2T-16\le2c\le16\), or \(\max(x,y)+\max(u,v)\le8\). The factor two is explicit; the lower bound \(2T-16\) is not assigned to the undoubled c.

For T=14 a three-cycle family’s other-cut run sum9 forces a directional maximum at least6, while the other family’s sum5 forces maximum at least3, violating the bound8. Therefore the surviving family-sum pairs are **(6,8), (7,7), (8,6)**; no existence follows. For T=13, a sum9 family is not excluded: it forces its directed totals3,6 and the other family’s2,2.

For EACH physical vertex z, let m(z) be its number of middle positions in a full cell run across the same five residual cycles. Its singleton-cell occurrences equal \(1+m(z)\), because its two internal incoming and two internal outgoing occurrences overlap exactly in those middle occurrences. In T=14, after removing \(h_E\), the four regular cycles contain exactly m(z) singleton occurrences. Cell-total-only ledgers or unrelated relabeled collections are insufficient.

## Evidence and unpaid target

[Complete f489 author body](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f489-actual-tuscan11-conditional-two-tripled-support-residual-closure-frontier/review-v1.md) · [f552 synchronization written review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f552-tuscan-two-tripled-support-singleton-edge-synchronization-review/review-v1.md) · [f553 directed budgets and vertex coupling written review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f553-tuscan-three-cut-square-arc-budget-and-vertex-coupling-review/review-v1.md) · [independent f554 report](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f554-tuscan-joint-cycle-layout-and-square-arc-independent-exact-check/author-candidate-v1.md) · [FINITEmethod disclosure](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f554-tuscan-joint-cycle-layout-and-square-arc-independent-exact-check/method-disclosure-v1.md) · [exact verifier source](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f554-tuscan-joint-cycle-layout-and-square-arc-independent-exact-check/f554-independent-finite-v1.py) · [parent one-shot receipt](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f554-tuscan-joint-cycle-layout-and-square-arc-independent-exact-check/parent-independent-finite-run-v1-receipt.json) · [prior conditional joint-cut disposition](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-4-actual-tuscan11-overlap-budget-and-conditional-tripled-support-joint-cuts-parent-v1.md). Parent displayed543/225/394/203/730 author, review, report and source logical lines; written f552/f553 each found0F/0M/0m. F554’s disclosed fresh selected schematic fixture was designed BY HAND after complete frozen input read, within FINITE author permission; it is not a WRITTEN zero-new-instance review or observed execution.

The parent independently materialized the byte-pinned source and ran it once after GO: exit0, empty stderr,2.294s. The checker builds actual twelve-vertex Hamilton cycles and directed squares BEFORE projection for one deterministic labeled lift of every92,400 cell words; 356 have no B/D singleton, 2 are all-Q, with29 physical layout signatures. It checks all216 ordered triples of three-vertex paths (zero complete covers),625 Q-slot schedules (25 capacity survivors,5 physical-mask survivors, all synchronized), and 45 T13 /90 T14 regular-slot mask schedules (450 with the five possible \(h_E\) positions). Family type combinations yield the stated T14 sum pairs. All these schedule/type counts are **necessary projections**, not counts of compatible labeled cycle systems.

The observed controls discriminate a disconnected cover, reversed/incorrect-eleven-cycle square, independent per-cell Q slots, and mixed vertex ledgers. The wrong-full-mask control is **interface-only**; a physical mutant is NOTTESTED. Dropping M=C on a genuine T2(11) is **NOTTESTED**, because no such M≠C actual array was supplied; no fake flag-only test substitutes. Internal-arc fixtures do not certify cross-cell adjacency or square decompositions.

The first unpaid step is simultaneous labeled compatibility of all eleven actual Hamilton cycles and BOTH complete directed-arc decompositions, with the two stipulated triple families. Both T13 patterns and all three T14 patterns remain open. M≠C, fewer tripled supports, unrestricted original target, source equivalence, novelty, independent-family/human review and kernel acceptance remain unpaid. All held episodes and consumers remain NONINPUT.
