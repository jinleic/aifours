# A parity core forbids odd-dimensional and 2D sectors

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Thu Oct 29 00:44:21 PDT 2026**. This strengthens the balanced-resolution parity context result for actual quantum arrays, but does not rule out the 4+6 sector case or arbitrary order10 resolutions.

## General parity statement

Suppose an odd number M of ONB contexts in C^N is selected from a t-resolvable QLS, and every selected cell occurs in either zero or exactly two of these contexts. Let X be the set of selected cells. If an orthogonal projector P commutes with EVERY rank-one projector `P_x` for x in X, then `rank(P)` is even. This holds regardless of repeated rays and requires no support/number-field restriction.

Indeed summing the selected basis identities gives `M I=2 sum_(x in X) P_x`. Multiplication by P and trace gives

`M rank(P)=2 sum_(x in X) tr(P P_x)`.

For a commuting orthogonal projector and rank-one P_x, every trace on the right is 0 or1. Since M is odd, rank(P) must be even. Equivalently, if every selected ray lies in either H=ran(P) or H-perpendicular, H has even dimension. This condition is required ONLY on the selected parity-core rays; the other cells may be arbitrary mixed-sector states.

If in addition all selected cell rays are distinct and different selected contexts intersect in at most one cell, no rank-2 such projector exists. A selected H-ray x is in two selected contexts; each restricts to an H-ONB of two rays, so both contain the UNIQUE H-ray orthogonal to x. Those partner cells are distinct by context intersection, but carry the same ray, contradiction. The complementary rank N-2 is excluded as well.

## Order10 consequence

If a 1RQLS10 resolution L admits the balanced Z2 quotient described in `frontier-20261028-resolution-parity-context-and-2adic-v1.md` SHA **e9403271de19ba2c8ddb1a01bc49b0c1e93e34e9efc78897363c7a5e2b3806d4**, it has M=15 selected bases and 75 cells each occurring twice. This includes a cyclic resolution L. Thus NO odd-rank projection can commute with all 75 selected ray projectors, even if the full QLS is not maximal.

If additionally all 100 rays are distinct, any nontrivial projection commuting with all 75 selected ray projectors must have rank **4 or6**. In particular no 1+9, 2+8, 3+7 or 5+5 split of just the parity-core rays is possible, even allowing ALL other25 cells to mix the sectors. Equivalently, the 75-ray core is either orthogonally irreducible or admits only a 4+6 split. The latter is a genuine remaining case, not a contradiction: published 4D parity systems with 30 rays in 15 bases do exist; e.g. [Waegell–Aravind, Table5](https://arxiv.org/html/1109.1299v2#S3.T5). Their existence alone does not supply the special K5,5,5 incidence or a QLS10 completion.

The selected-context kernel hypothesis is essential; Parker's and Weisner's tested resolution squares have no such odd kernel. This is not an unrestricted no-go. The parity-core identity, rank-two uniqueness and K5,5,5 incidence caller require independent written review.
