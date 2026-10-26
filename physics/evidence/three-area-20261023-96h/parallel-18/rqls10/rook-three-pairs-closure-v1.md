# Three-rook-pair closure v1 — the dual one-rook-pair class closes as well

Observed before creation: **2026-10-23T15:28:04-07:00**. PhysicsRQLS10. Written proof for actual Paley core relabelings; no scientific executable, enumeration, numerical rank test, solver, kernel or model CLI ran.

**CANDIDATE WRITTEN PARTIAL.** This proves that every relative core with exactly three rook-positive inversion pairs has first-order odd rank at least3 and therefore actual rank M≥8. The written rank8 theorem excludes all arbitrary complex compatibility phases. Complement duality closes the one-rook-pair class. Together with the previous extreme-signature proofs, only the two-rook-pair signature remains in this fixed-first-core/oriented-rho route. This is not all of QLS10 or all conference orientations.

## 1. Retained first-order test and actual geometric data

Fix the first Et-Taoui core C on GF(9), rho(t)=-t and arbitrary second Q'=PQP^T. Represent p with p(0)=0 using a second-grid translation, which leaves Q' unchanged. Its four paired edges cover the eight other3×3 grid points.

As in the previous papers, the first odd Schur coefficient is proportional modulo7 to

    L=A0+A',
    A0=2*[0 0 1 1; 0 0 1 -1; 1 1 0 0; 1 -1 0 0].

A' is the zero-diagonal Gram-off-diagonal matrix of the four pair-difference vectors in A2⊕A2. A rook pair contributes one nonzero A2 root (horizontal or vertical). A diagonal/nonrook pair contributes one root in each coordinate factor. Inner products of nonzero A2 roots are±1 or±2, never0; magnitude2 means parallel roots.

If L has a triangle of three nonzero entries modulo7, its3×3 principal minor is twice their product and is nonzero. All relevant entries below have integer magnitude at most4, so nonzero entries do not accidentally reduce to0 modulo7. Thus such a triangle gives rank(L)≥3, actual rank(M)≥8, and the full arbitrary-phase exclusion.

Assume exactly three of the four pairs are rook pairs. Let h be the number of horizontal rook pairs; the others are vertical. There is exactly one diagonal pair D. Coordinate interchange allows h=0 or1 to represent h=3 or2, respectively. This is a geometric relabeling of the second grid, not a restriction on the first-core placement of pair labels or phase orientations.

## 2. Three parallel rook pairs: a complete signed graph with just one double edge

Take h=0, so three vertical pairs and one diagonal pair D. Initial nonzero point counts per column are2,3,3. Removing D must leave every column even for the vertical pairing. Therefore D joins points in columns1 and2, say(1,a),(2,b), with a≠b because D is diagonal.

The remaining vertical roots have missing y-levels0,a,b, respectively. D's y-root has the third missing level c, where{a,b,c}={0,1,2}. Consequently the four y-root directions have missing-level multiset

    {0,a,b,c}={0,0,1,2}.

Exactly one pair of roots is parallel. Their off-diagonal weight has magnitude2, and every other pair has magnitude1. D's extra x-root does not contribute against the three vertical roots. Thus A' is a signed complete graph K4 with exactly one magnitude2 edge and five magnitude1 edges.

A0 is supported on K2,2 with sides{1,2},{3,4}. Both within-side edges of A' are nonzero. If L had no nonzero triangle, the within-side edge(1,2) would require at least one of L13,L23 to vanish, and at least one of L14,L24 to vanish. This requires at least two cancellations of A0's cross edges. A cancellation of an entry±2 requires an A' entry of magnitude2. Only one such entry exists. Contradiction. Therefore L has a nonzero triangle. This closes h=0, and by coordinate interchange h=3.

## 3. One horizontal and two vertical rook pairs: a signed paw with a simple pendant edge

Take h=1. Let H be the horizontal pair. To leave even column counts for the two vertical pairs after removing H and D, the four removed endpoints have per-column counts(2,1,1). Indeed columns1 and2 start with odd counts3 and each can lose at most two points, so each must lose exactly one; column0 must lose the other two. Hence both H and D use column0, and their other endpoints use different columns a,b∈{1,2}.

Since the missing point is(0,0), H lies in a nonzero row r and joins(0,r),(a,r). The column0 endpoint of D is(0,-r); its other endpoint is(b,u), with u≠-r. Thus u is0 or r. The two vertical pairs lie in columns a and b, with missing y-levels r and u, respectively.

H's x-root and D's x-root use different directions, so their inner product has magnitude1. H is orthogonal to both vertical roots because they lie in different coordinate factors. Among the two vertical roots and D's y-root, exactly two are parallel:

- if u=0, D's y-root, joining-r to0, has missing level r and is parallel to the vertical root in column a;
- if u=r, the two vertical roots have the same missing level r, while D's y-root has missing level0.

Therefore A' is a **paw graph**: a triangle on the two vertical pairs and D, with H as a pendant joined only to D. The pendant edge has magnitude1. Among the triangle edges exactly one has magnitude2 and the others magnitude1. Every sign and pair-label placement remains allowed.

### The paw always leaves a nonzero triangle in L

If H and D lie in the same bipartition side of A0's K2,2, the vertical vertices lie in the other side. The H-to-vertical cross edges come solely from A0 and are both nonzero. At most one D-to-vertical cross edge can cancel, because at most one A' edge has magnitude2. A surviving one makes a triangle with the nonzero within-side H-D pendant edge.

If H and D lie on opposite sides, choose the vertical vertex V in D's side. The edge D-V is a nonzero within-side A' triangle edge. H-V is an unchanged nonzero A0 edge because A'_HV=0. H-D is an A0 edge±2 plus the A' pendant weight±1, hence nonzero. Thus H,D,V already form a nonzero triangle, regardless of every other cancellation.

This closes h=1 and, by coordinate interchange, h=2. All possibilities for the three rook pairs are exhausted.

## 4. Actual arbitrary-phase conclusion

### Theorem R3

For every Q' with exactly three rook-positive inversion pairs, rank(L)≥3 over F7. Hence the actual M has rank at least8. The complete rank8 norm-descent theorem excludes every complex unit-phase kernel, with no requirement that the phases be integral, roots of unity, symmetric, or in K.

The exact complement map `Q'→-gQ'g^T`, where g is a nonsquare multiplication and the physical bases are simultaneously conjugated/relabelled, preserves the first core and rho while changing k to4-k. Therefore **every one-rook-pair core is excluded too**, for arbitrary phases.

The coverage note gives1344 literal core tables in each of the k=3 and k=1 signatures. These are finite input tables of one restricted route, not scientific-problem/theorem/discovery counts. With the extreme k=0 and k=4 closures, all signatures except k=2 are now covered by written arguments. No input has been computationally enumerated or replayed.

## 5. Precise residual and trust boundary

The remaining signature k=2 has1584 literal core tables in the current coverage decomposition. That number is not a count of feasible phase kernels; it is an unclassified input class for this argument. Its commuting-core subcases remain excluded by the earlier arbitrary-phase averaging theorem. No claim that the remaining noncommuting two-rook-pair inputs have low rank or support phases is made.

The primary problem still permits other first orientations, other conference classes and all nonuniform overlaps. No H0-wide or unrestricted1-RQLS10 conclusion follows. The prepared5040 source/request and controls remain unchanged/unexecuted, with no GO. All new claims here are author-written CANDIDATE pending actual separate reconstruction and parent check; novelty and significance remain uncertified.
