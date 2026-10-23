# K1 corollaries: resolvable and pandiagonal quantum Latin squares of order seven

These are direct corollaries of Theorem K1 (`K1-THEOREM.r3.md`), not new searches. They inherit K1's verification
status; parent theorem integration is separate. They do not determine M(7), and no priority claim is made.

## Conventions and prior-art acknowledgement
Cardinality counts projective rays: unit vectors differing by a phase are identified. A single QLS(7) has
cardinality seven **iff it is classical** in the isotopy-invariant sense of Ball–Simoens [2607.12933v2,
§2.2](https://arxiv.org/abs/2607.12933v2): any ONB row already supplies seven rays; if these are all the rays, every
entry is parallel to one of that row's basis vectors. Conversely, a classical square uses exactly one ONB's rays.
Maximal cardinality in the cited cardinality papers means 49, not seven.

Zhang–Cao [2608.29201v2, Definition 1.1](https://arxiv.org/html/2608.29201v2#S1.Thmtheorem1) defines a t-RQLS(v) as
a QLS with t resolutions into v disjoint transversals, with every transversal from one resolution meeting every
transversal from another in exactly one cell. A transversal contains one cell per row/column and its vectors form
an ONB. Their [Lemma 2.2](https://arxiv.org/html/2608.29201v2#S2.Thmtheorem2) proves the equivalence:

    A is a t-RQLS(v) iff A together with t classical QLS forms (t+1)-MOQLS(v).

The lane's (C1)/net reformulation is therefore prior art, not an independent methodological contribution.
Ball–Simoens [Thirty-six quantum officers are entangled, 2603.02334v1, Lemma 21,
§4.2](https://arxiv.org/html/2603.02334v1#Thmtheorem21) already gives the order-six classical-companion case as an
orthonormal representation of the complement of a Latin-square graph. Zhang–Cao Lemma 2.2 gives the general
resolution/classical-companion formulation. These precedents are acknowledged independently of the order-seven
K1 exclusion.

## Corollary 1. Every 2-RQLS(7) is classical; none has maximal cardinality
Let A be a 2-RQLS(7). By Zhang–Cao Lemma 2.2, there are two classical squares B0,B1 such that A,B0,B1 are three
MOQLS(7). If A were non-classical, this would be precisely K1, which is excluded. Thus A is classical and has
cardinality seven. In particular a maximal-cardinality 2-RQLS(7), which would have cardinality 49, does not exist.
This addresses the order-seven case left among the remaining orders in Zhang–Cao v2 §5; it makes no claim about
the other orders listed there.

## Corollary 2. Every pandiagonal QLS(7) is classical; MCPQLS(7) does not exist
Use the definition in Huang–Li [2606.27758v1, Introduction and
§5](https://arxiv.org/abs/2606.27758v1): every diagonal and broken diagonal in both directions must be a quantum
transversal. Index cells by (x,y) in F7². Besides the row/column classes, these are exactly the lines

    y-x = b and y+x = b, for b in F7.

Each family partitions the cells, and a line from each family has a unique intersection because 2 is invertible
in F7. They give two orthogonal transversal resolutions, so a PQLS(7) is a 2-RQLS(7). Corollary 1 therefore applies.

Equivalently, this is the explicit harmonic-net proof. The four direction classes are {infinity,0,1,-1}.
The invertible shear (x,y) -> (u,v)=(x,y+x) sends a finite slope m to m+1 and fixes the vertical class, so the
image directions are {infinity,0,1,2}, the harmonic Desarguesian net (class5 in the K1 proof). Transporting the
vectors by this cell bijection preserves every line ONB and the projective-ray set. K1's class5 rigidity therefore
forces exactly seven rays. Consequently no maximal-cardinality PQLS(7), denoted MCPQLS(7) and requiring 49 rays,
exists. This addresses the order-seven MCPQLS case identified as undetermined in Huang–Li v1 §5.

This is not nonexistence of all PQLS(7): classical examples remain. Nor does it address merely diagonal QLS(7),
where only the two unbroken diagonals are constrained. Neither corollary requires, or establishes, a K2/K3
exclusion or an exact value of M(7).
