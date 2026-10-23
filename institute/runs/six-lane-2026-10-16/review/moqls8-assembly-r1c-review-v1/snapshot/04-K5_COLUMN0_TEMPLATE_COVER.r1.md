# K5 column0: a proposed 16-template genuine-vector cover (13 after the imported c112 exclusion)

Model-authored proof candidate; frozen before any template solver run. Parent approval/review is required. The current
full-product searches/ledgers are not changed. This is a semantic cover of genuine K5 vectors, not a tautological
Boolean cover of the Gram CNF. No K4/K5 exclusion is asserted.

## 1. Both degree bounds for the column0 transition

For a genuine set of five MOQLS(8), let l be any row or column and p a cell off l. For each square s, its overlaps
with the ONB on l form a nonempty support S_s. By Prop1/G2, the five supports S_s are pairwise disjoint on the EIGHT
aligned cells of l. The cell of l in p's column (if l is a row), or p's row (if l is a column), is orthogonal to p
in every square, so at most seven coordinates are available. Thus |S_s|<=7-4=3 for every s.

Apply this once with frame row0 and once with frame column0. In the transition matrix

    U[k,i]=<Q1(0,k),Q1(i,0)>, k,i=0,...,7,

BOTH every row and every column has at most three nonzeros. This does not use F3, minimality, H3 CNF clauses or a
catalogue. U is unitary. Entry(0,0) is1 and the other entries of row0/column0 are0, leaving a seven-dimensional
unitary support pattern. Its column i=1 has support A={1,2,3} by the accepted K5 SB2 normalisation.

## 2. Elementary sparse-unitary support theorem

**Theorem.** The bipartite support graph of any unitary matrix whose row and column degrees are at most3 decomposes
into components of the following five types, up to independent row/column permutations:

    K11; K22; K33 with one edge removed; K33; K44 with a perfect matching removed.

Only support patterns are classified; coefficient values/phases are not fixed.

**Proof.** Distinct rows, and distinct columns, cannot have exactly one common nonzero position, since their inner
product would then be one nonzero summand. Every vertex has positive degree. Each connected component has equally
many row and column vertices: the restricted rows are nonzero orthonormal vectors supported in its column space,
and the restricted columns are nonzero orthonormal vectors supported in its row space, giving both dimension
inequalities.

A degree1 row has one column neighbour x. No other row can touch x (singleton intersection), so x also has degree1
and this component is K11. The transposed argument handles a degree1 column.

Suppose a component has a degree2 row u with neighbours x,y. Any other row touching x must also touch y, and
conversely; hence N(x)=N(y)=R. With degree1 vertices already handled, |R| is2 or3.
- If |R|=2, write R={u,v}. An extra neighbour z of v would give columns x,z exactly one common row v (u has only
  x,y), impossible. Thus v also has just x,y and the component is K22.
- If |R|=3, write R={u,v,w}. Each of v,w has at most one extra neighbour. If v has z, columns x,z must share at
  least two rows; u does not touch z, so w must touch the SAME z. No row outside R can touch z, since it would then
  intersect v only at z (x,y are already full). This gives K33 minus the edge(u,z). If neither v nor w has an extra
  neighbour, the component is K32, impossible by the equal-size rank argument.
Apply the transposed argument if only a column of degree2 was initially found.

The remaining case is a component with all degrees3. Pick a row with neighbours a,b,c. The other rows touching
these columns account for exactly six incidences, and each such row uses at least two of a,b,c. The possibilities
are two rows using all three (giving K33 and closure), or three rows using two each. In the latter case the degree
counts force the pairs ab,ac,bc exactly once. Write the rows ab+x, ac+y, bc+z, with x,y,z outside {a,b,c}. Pairwise
row intersections cannot be singletons, so x=y=z. This common new column has degree3 and the component closes as
K44 minus a perfect matching. This exhausts all cases. QED.

## 3. Allowed residual normalisations

Use exactly the accepted K5 row0/SB2/ROWLEX bridge, as made explicit in `K5_RESIDUAL_NORMAL_FORM.r3-IMPORTS.md`.
We may permute coordinates and columns by any sigma in Sym(A) x Sym(B), B={4,5,6,7}, fixing0. Relabel squares2–5
to restore their singleton supports at(1,0), and commonly permute rows2–7 to restore ascending non-strict ROWLEX.
Q1's support A at(1,0) is unchanged as a SET (its coefficient order need not be fixed). All reduced-K5/P4 properties
are preserved. No other symmetry predicate is active in F. The row sort places every pure-B column before every
column meeting A.

The component containing column1 (support A) must be:
- **P0:** K33 on coordinate set A. Its other two columns both have support A.
- **P1:** K33 minus one edge, still on coordinate set A. Its other two columns have supports A minus one coordinate
  and A. By Sym(A), make the former {2,3}; these are the final two columns in ROWLEX order.
- **P2:** K44 minus a matching, on A union {b}, b in B. By Sym(B), put b=4. Its other three columns have supports
  {2,3,4},{1,3,4},{1,2,4}, in exactly this ROWLEX order.

Consequently the pure-B part has dimension4 on B for P0/P1, or dimension3 on {5,6,7} for P2. Apply the theorem to
that remaining unitary block. In dimension4 the possible partitions/types are I4, K22+I2, K22+K22, K33+I1,
(K33-minus-edge)+I1, and the four-dimensional matching-complement. In dimension3 they are I3, K22+I1,
K33-minus-edge, and K33. Independent coordinate permutations inside the pure-B set and row ordering give the
following canonical support lists. These operations do not disturb the already-fixed A component.

## 4. The explicit 16 templates

In every template Q1(0,0)={0}, Q1(1,0)=A. A list below specifies, in order, the supports of Q1(i,0), i=2,...,7.
Notation123 means {1,2,3}, etc. Sets in each list are already nondecreasing in the exact ROWLEX bit order.

For **each** P in {P0,P1}, choose one of the following six B lists for rows2–5:

| B type | rows2,3,4,5 | root |
|---|---|---|
| B1=I4 | 7;6;5;4 | c064 |
| B2=K22+I2 | 7;6;45;45 | c064 |
| B3=K22+K22 | 67;67;45;45 | c096 |
| B4=K33+I1 | 7;456;456;456 | c064 |
| B5=(K33-e)+I1 | 7;56;456;456 | c064 |
| B6=K44-matching | 567;467;457;456 | c112 |

Complete these12 templates by rows6,7 =123;123 for P0, or23;123 for P1.

For **P2**, the remaining four templates are:

| C type | rows2,3,4,5,6,7 | root |
|---|---|---|
| C1=I3 | 7;6;5;234;134;124 | c064 |
| C2=K22+I1 | 7;56;56;234;134;124 | c064 |
| C3=K33-e | 67;567;567;234;134;124 | c096 |
| C4=K33 | 567;567;567;234;134;124 | c112 |

To justify the B/C canonical choices, map isolated coordinates to the rightmost available positions, then map the
non-singleton blocks as displayed; for a three-dimensional one-zero block, put its missing coordinate leftmost.
For two K22 blocks, map their coordinate pairs to45 and67. For a matching-complement block, the distinct missing
coordinates determine its columns, so the ROWLEX sort gives the displayed list. Sym(B) acts independently of Sym(A).

Thus every genuine K5 configuration admits one of these16 normal forms. The three c112 templates (P0-B6,P1-B6,
P2-C4) are covered by the already parent-replayed c112 root refutation pinned in normal-form r2§4. There remain
EXACTLY13 templates:10 with rootc064 and3 with rootc096.

## 5. Proposed certification interface (no run before approval)

For each of the13 remaining templates append42 units to the SAME old unconditional F: for each i=2,...,7 and
c=1,...,7 fix g_1((0,c),(i,0)) according to the template. These are precisely the variables V1–V6 (no new variable,
new encoder family, or H3 clause). Any independently replayed UNSAT of all13 formulas, together with this theorem,
the accepted original necessity bridge, and the c112 proof, would exclude genuine K5.

This does NOT establish a Boolean cover of F: the semantic projection/rank argument need not apply to arbitrary
support SAT models. The old full-product ledger must remain incomplete where it is incomplete. A separate
semantic-template manifest would pin this proof, its16 cases, the13 CNF hashes/units, and their strict receipts;
it would not mark omitted old roots/children certified. K4 still needs a different analysis because L's row sort
consumes the unrestricted row permutation used here.

Suggested first experiment, only if parent approves after review: three representative complete-column formulas
P0-B1,P1-B3,P2-C3, each proof-free native300s, streamed/no retained CNF, same resource caps, before a full13-case
strict run. This proposal does not interrupt the currently authorised c064/c096 full128-child passes.
