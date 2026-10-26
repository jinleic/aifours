# Common-complement witnesses may be chosen with connected actual trade graphs

Owner MathShor / MathShor-2. Actual preceding `/bin/date`: `Sun Oct 25 14:58:46 PDT 2026`. WRITTEN CANDIDATE, unreviewed. No computation. Original full Shor target remains NOT_PROVED.

This is a combinatorial representation for ALL larger trades, retaining every unknown endpoint. It does not assume that the mandatory small graph is the whole graph or that unknown chords are absent.

## 1. An exact regular bipartite graph for two complements

Suppose A+B=A+D=Z_n directly. Let

    P=D minus B, N=B minus D.

After canceling common complement elements in the two convolution identities,

    union_(p in P) (A+p) = union_(q in N) (A+q),

with translates disjoint WITHIN each side. Denote their common covered region U. For each x in U place one edge between its unique P label p and unique N label q. Parallel edges are retained: they are different actual residues x.

Every vertex has degree |A|, because its translate has exactly |A| points. Thus each connected component has equally many P and N vertices, by counting its edges from both sides.

For ANY component with vertices P_c,N_c, the covered unions A+P_c and A+N_c agree exactly. Replacing P_c in D by N_c preserves the full direct tiling by A; these N vertices were not already in D. This is a genuine complement swap, not a cardinality relaxation.

## 2. All fixed Shor points belong to ONE mandatory component

Use the common gate with B containingJ0 and D2 containingJ2. Its forced trade vertices are

    P:2,4,6,
    N:1,7,13,14.

They are all distinct and on their stated sides by the literal collisions already proved. The fixed A0={0,3,8,11} supplies the connected alternating path

    N13 -- P2 -- N7 -- P4 -- N1 -- P6 -- N14.

The actual shared residues proving its edges are:

|Edge|A+p=A+q shared residue(s)|
|---|---|
|13/2|13=11+2=0+13|
|2/7|10=8+2=3+7|
|7/4|7=0+7=3+4; 15=8+7=11+4|
|4/1|4=0+4=3+1; 12=8+4=11+1|
|1/6|9=8+1=3+6|
|6/14|14=8+6=0+14; 17=11+6=3+14|

All values here are below n, but the graph definition is cyclic and retains arbitrary wraps elsewhere.

Choose D2 among all complements of this SAME A containingJ2 so that |D2 minus B| is least. If any trade component did not contain the mandatory path, undoing that component would preserve0,2,4,6 while strictly decreasing the trade. Therefore a least-change D2 has its ENTIRE trade graph connected, containing all seven fixed vertices. This selection neither changes A/B nor restricts unknown complement elements beyond a valid finite minimization.

The uniform trade proofs imply that this connected graph has at least seven vertices on EACH side. They do not bound its size from above.

## 3. Unknown edges/chords MUST remain

The common tile A has no nonzero difference in

    {+/-1,+/-2,+/-4,+/-6,+/-7,+/-12,+/-13,+/-14},

because these are differences inside the three forced complement seeds J0,J2,J3. This is a statement about the ENTIRE A-A, not just the known A0.

Among the seven fixed trade vertices, the only possible additional adjacency types beyond the displayed path are

    P4 -- N13 (difference9),
    P4 -- N14 (difference10).

They can be created by UNKNOWN A endpoints:9 and10 were NOT excluded by the displayed difference filter. Extra multiplicities on mandatory path edges and arbitrary edges to additional trade vertices are also possible. Therefore the graph must NOT be called a fixed tree and no path-expansion contradiction may silently omit these possibilities.

## 4. The D3 trade has an analogous connected choice

For B versus D3, the forced positive vertex2 is connected to the forced negative vertices7 and13, at the same residues10 and13 from §2. Choose D3 minimizing |D3 minus B| among complements containing0,1,2. All components not containing2 can be undone, preserving0,1,2, so its whole trade graph is connected as well. It has at least three vertices on each side by the earlier proof.

D2 and D3 may be minimized INDEPENDENTLY relative to B because the exact common-complement gate requires only that both complement the SAME A. The row-normalized all-t construction works for any such pair.

No claim is made that the third trade graph D2 versus D3 can simultaneously be minimized or made connected. A swap reducing that third graph can change one of the first two minima; an additional joint exchange theorem would be needed.

## 5. Remaining whole-gate question

A positive common-complement witness may therefore be sought with two connected regular trade graphs over ONE unknown A/B, sharing the actual B vertices7 and13 and the actual positive translate A+2. A negative proof must rule out ALL finite closures of these mandatory configurations, including unknown9/10 chords, arbitrary additional vertices, cyclic wraps and unbounded |A|.

No such universal closure obstruction or joint exchange theorem is proved here. The Fourier bounds (k_B,D2>=7, k_B,D3>=3 and the seven-point primitive-spectrum alternative) are retained at their exact scopes; they are not extrapolated to all finite connected trades. Raw PR/STAB/GP completion remains a further requirement after any positive gate witness.

Only written set partitions, graph edge counts and literal integer equalities were used. No interpreter, enumeration, solver, replay, nested agent, external model or new GO occurred. No independent/formal/executable/family/novelty promotion is claimed.
