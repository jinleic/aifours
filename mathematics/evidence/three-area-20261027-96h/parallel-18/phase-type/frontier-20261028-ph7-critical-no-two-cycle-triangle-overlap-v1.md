# An unresolved overlap route for critical no-two-cycle PH7

Status: **FAILED WRITTEN ROUTE**, not a theorem, not an independent scientific-review result, and not a parent adoption. This records the exact gap in a potential all-transition-count graph condition; it makes no complete PH7 existence/exclusion claim.

## Goal and gap

The aspirational statement would say that at `z=8/9` every irreducible seven-state row generator with the target double pair and no directed two-cycle must have two triangles sharing an edge. **That statement is not proved here.**

## Attempted route

Import the exact critical triangle-imbalance capacity theorem `frontier-20261028-ph7-critical-triangle-imbalance-capacity-v1.md` (SHA256 `c2c95deebfaa048072704da11126636d19b166c60a3cc7f41a266927716dc409`): if the seven diagonal rates are sorted as `r_1<=...<=r_7`, then because there are no two-cycles the total oriented triangle product `W` must satisfy

`W > r_5*r_6*r_7`.

Assume no pair of triangles shares an edge; their vertex triples form a linear family. The deterministic row-map argument in `frontier-20261028-ph7-no-two-cycle-disjoint-triangles-v1.md` (SHA256 `7306b0cc0eeca0f78c75c1867f99b4675e169da2fdfada82c5c0f5175eb97ddf`) then implies that the graph has two **vertex-disjoint** directed triangles `A,B`. They use six vertices; call the seventh vertex `x`.

A third triangle in a linear family cannot contain two vertices of `A` or two of `B`, so it must consist of `x`, one vertex `a in A`, and one `b in B`. Two such connector triples must use different `A` and different `B` vertices, but no argument here shows that there cannot be two or three connector triples. Such multi-connector cases remain open.

Each realized triangle `C` has weight equal to the product of the three corresponding row fractions. For a linear triple family, the 3-cycle events in an independently sampled outgoing-edge map are pairwise mutually exclusive whenever the triples intersect. Their conflict graph is the intersection graph of the triples, so `sum_C weight(C)` is at most the fractional matching number; this alone can exceed one in the presence of two disjoint triangles and does not yield the desired contradiction. The earlier shared-hub and shared-edge budget lemmas eliminate only the cases with no disjoint pair or a common edge, and do not eliminate a linear family with multiple connector triples. Thus the aspirational universal overlap theorem is **not proved** by the current inputs.

The conditional statement on this slice remains weaker: there are at least two vertex-disjoint triangles (pending the named capacity/disjoint-triangle reviews), and the all-edge chain theorem excludes the specific case of **exactly three** triangles where the third is a connector triple. At least four linear triangles remain a live possibility. No assumption about 4/long cycles, an unproved classification, or selected graph enumeration may be substituted for a proof.

## Exact scope

This manuscript is an explicit **failed route**, not a theorem or an independent scientific-review result. It preserves the exact open combinatorial step, with no general 8/9 verdict, minimum-PH-order claim, novelty, formal proof, or parent adoption.
