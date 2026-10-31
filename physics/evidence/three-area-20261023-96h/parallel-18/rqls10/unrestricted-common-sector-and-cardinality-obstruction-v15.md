# RQLS10 v15 — an UNRESTRICTED common-sector obstruction, an86-ray ceiling, and five possible irreducible block patterns

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 06:15:16 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact finite-dimensional/operator/graph arguments only. No scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO, no private decimal/approximate scout or discarded-probe backconversion. No machine/kernel/formal/human/configured-family/novelty acceptance.

The ORIGINAL unrestricted maximal1-RQLS(10) question remains UNKNOWN. Unlike v10-v14 this theorem is NOT conditional on a Weyl, NEB, Hadamard, cyclic, qubit-product, phase-field or classical-seed ansatz. It applies to EVERY actual1-RQLS10 with its literal row, column and designated-transversal resolution. It excludes an entire low-dimensional common reducing mechanism, not the full problem.

## 1. Literal original object and the new statements

Let q_(i,j) be100 unit vectors in C^10. Every row and column is an ONB, and the ten designated transversals T_t partition the cells, each containing one cell per row/column and carrying an ONB. Put P_v=q_v*q_v^dagger for every cell v. Cardinality always means the number of DISTINCT RAYS, not vector phases.

A common reducing sector is an orthogonal projection E satisfying

    E*P_v=P_v*E for EVERY one of the100 cells.

This requirement concerns ALL vectors. Merely having some rays inside a chosen2-space, or merely writing C^10=C^2 tensor C^5, does NOT supply such a projection.

**Theorem A.** If a common reducing sector has dimension1, the array has cardinality at most91. If one has dimension2, its20 cells contain at most6 distinct rays and the full array has cardinality at most86. Thus no maximal1-RQLS10 can have ANY rank1 or rank2 common reducing projection.

**Theorem B.** Fix ANY actual row as an orthonormal coordinate basis. Form a graph on its10 coordinate directions, joining a,b whenever SOME cell vector has BOTH components nonzero. The connected components are EXACTLY the minimal common reducing sectors. This is a literal exact-zero support criterion, not a numerical tolerance or a phase-relaxation test.

**Theorem C.** In a maximal1-RQLS10, the common-projector irreducible block dimensions are necessarily one of

    10;
    3+7; 4+6; 5+5;
    3+3+4.

No assertion that the proper block patterns are impossible or feasible is made. In particular maximality is NOT being assumed to imply irreducibility. The decomposition keeps the original cells/contexts and every actual vector, rather than deleting a phase or replacing a principal block.

**Exact converse interface.** For any such orthogonal decomposition, a support label for each cell with d_a cells of label a in EVERY row/column/transversal, and actual unit vectors in its d_a-space forming an ONB on each such labeled context, give a full1-RQLS10. It is maximal iff all10*d_a rays inside EACH sector are distinct. No new proof makes the partial vector assignments exist.

## 2. Every context has the actual sector dimension

If a rank1 projector P_v commutes with E, then E*q_v is proportional to q_v. Since E^2=E, its eigenvalue there is0 or1. Thus each cell vector is ENTIRELY in range(E) or ENTIRELY in its orthogonal complement; a hidden mixed component is not allowed by the hypothesis.

For any original context C, sum_(v in C) P_v=I. Taking trace after multiplying by E gives

    number of sector cells in C=trace(E)=d.

Those d vectors form an actual ONB of the d-sector, because the full context is orthonormal and their projection sum is E. In particular there are EXACTLY10*d sector cells in the entire array, by counting its ten rows. The same count holds for columns and the designated transversals, not independently selected subcollections.

At d=1 all ten sector cells are the SAME ray. The other90 cells contribute at most90 more, giving cardinality<=91.

## 3. The rank2 sector: a SIMPLE cubic bipartite context graph

At d=2, let V be its20 actual sector cells. Make a graph on V by connecting the two sector cells in EACH actual row, EACH actual column and EACH designated transversal.

Every vertex has one neighbor of each of the three context types. These neighbors are DISTINCT:

- two cells cannot share both a row and a column;
- two distinct cells of one row cannot share a designated transversal, because that transversal meets each row only once;
- the same is true for columns and transversals.

Therefore this is a SIMPLE3-regular graph, not a multigraph or a graph where duplicate contexts can supply three parallel edges to one partner. This uses actual transversality, not just an abstract partition into ONBs.

On an edge, the rays are orthogonal inside C^2. A ray there has a UNIQUE orthogonal-complement ray. Consequently along any path the ray alternates between one ray L and its complement L^perp. An odd cycle would force L=L^perp, impossible for a nonzero ray. Thus every connected component is bipartite, and contributes AT MOST TWO distinct rays, however many of its cells occur.

Each part of a simple3-regular bipartite component has at least3 vertices, because every vertex has3 distinct neighbors. Hence each component has at least6 vertices. There are20 vertices total, so there can be at most3 connected components and therefore at most6 sector rays. The remaining80 cells yield at most80 other rays. This proves the86-ray bound and Theorem A.

No sharpness or construction attaining86 is claimed. Different components may in fact use the same rays, making the bound weaker, never invalid. No assumption that every2-sector is one connected ray pair was made.

The same mechanism works in order n: a2-sector contains2n cells, with at most2*floor(n/3) distinct rays. Its coarse total-cardinality ceiling is

    n^2-2n+2*floor(n/3).

The n=10 claim above is just its exact specialization, not a sampled matrix.

## 4. The full commutant is an elementary support graph

Choose one actual row as the coordinate ONB e_1,...,e_10. Any operator X commuting with its ten rank1 projectors is diagonal in this basis, say X=diag(x_1,...,x_10). It commutes with a further cell projector q*q^dagger iff

    (x_a-x_b)*q_a*conj(q_b)=0 for ALL a,b.

Thus x_a=x_b whenever that cell has both coordinates nonzero. Taking all100 cells, this says exactly that x is constant on each connected component of the support graph in Theorem B. Conversely every such diagonal X commutes with EVERY projector. Therefore the entire commutant is precisely this block-constant diagonal algebra.

Its minimal nonzero projections are the component indicators. Every cell support lies within ONE component: two nonzero coordinates in different components would themselves create an edge joining those components. Hence the original array really splits into these orthogonal common sectors, with no lost initial support, phase choice or context.

Each component sector is irreducible for the restricted projector family in the exact common-reducing-subspace sense. Any further reducing projection would belong to the commutant, contradicting its minimal component status. This proof does not need an unprovided classification of finite-dimensional C*-algebras or a guess that projector linear span is all matrices.

More quantitatively, if this support graph has n1 singleton and n2 two-vertex components, their mutually orthogonal sectors give

    cardinality <=100-9*n1-14*n2.

Each singleton replaces10 potential rays by at most1, and each2-component replaces20 by at most6. Other sector sizes are bounded only by their cell counts here. Therefore maximal cardinality100 forces EVERY component to have size at least3.

## 5. Exhaustive block dimensions and exact reconstruction interface

The component dimensions are positive integers summing10, and each is at least3 in a maximal array. The only sorted possibilities are

    {10}, {3,7}, {4,6}, {5,5}, {3,3,4}.

This is an exhaustive integer consequence of the proved dimension bound, not a graph/rate enumeration. A proof about only the10-dimensional irreducible branch would still need the four proper patterns before claiming an unrestricted no-go.

For a proper pattern, keep the FULL actual support-label matrix c(i,j). In every original row, column and designated transversal there are EXACTLY d_a cells of label a. Their assigned d_a-dimensional unit vectors must be an actual ONB in that sector. These are coupled partial-array constraints, not independent basis weights. Across different sectors the vectors are orthogonal automatically; within a sector, maximality still requires all10*d_a actual rays distinct.

Conversely, given such labels and genuine partial arrays with those ONB and distinctness conditions, take their orthogonal direct sum in C^10. Every original context is the union of sector ONBs and hence an ONB of C^10. Distinct-sector rays cannot collide, and the within-sector requirement excludes all other collisions. This proves the exact converse interface without asserting any unsolved partial array exists.

The support graph is relative to ANY chosen actual row basis, but its component ranges describe the SAME intrinsic commutant algebra up to coordinate/unitary change. No Fourier basis, tensor product, prescribed field or classical grid labeling was introduced. Coordinate zeros must be actual equalities; small numerical entries are not zeros and no tolerance-based algorithm is authorized here.

## 6. What this does and does not close

The ENTIRE common rank1/rank2 reducing mechanism is impossible for a maximal array, regardless of conference class, phases, all-P orientation, arbitrary designated resolution or other ansatz. This excludes attempts to keep an isolated qubit or one-dimensional hole as a GLOBAL reducing summand and then claim all100 rays are distinct. It does NOT exclude a tensor C^2 tensor C^5 representation, an array merely written in a9+1 coordinate basis, or a dense construction mixing every such coordinate summand. Those are different hypotheses.

The four proper patterns listed in Section5 remain OPEN, with exact support/context/vector requirements. No3-dimensional,4-dimensional or5-dimensional sector no-go follows from the2-dimensional unique-complement argument. The irreducible10 branch also remains the original difficult actual-array problem. The previous Weyl asymmetric phase master and general Hadamard companion construction can be assessed within these intrinsic branches without treating their own restrictions as WLOG.

This is a new UNRESTRICTED structural theorem inside the dossier, not an actual100-ray witness, full impossibility theorem, novelty/SOTA claim or finite-program gate. All earlier findings/frozenbytes, the v9 proof correction and ZERO-credit quarantines remain. Same original18 owners, exclusive root, cutoff2026-10-27T11:05:38-07:00/deadline12:35:38 and30min substantive actual-clock cadence. Primary research continues in the exact surviving branches; pending review is not a terminal park.
