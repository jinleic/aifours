# Definition-first common-row coupling II: the common-middle quadratic form is a connected regular multigraph Laplacian

Owner **InfoRecursiveMDS18-2**, slot **info-4**. Actual native prewrite clock: **Tue Oct 27 14:46:00 PDT 2026**.

**NEW author-WRITTEN, unreviewed necessary coupling lemma.** Original Tuscan-2(11) remains OPEN. This follows the same S1 definition-only actual-row release and `prerequisite-derivation-v1.md` (SHA256 `5c7e2c40f979b41c30608da7d75de7039ae458bfce949a50bc259f3d7a6b0b76`), but changes the next step from a cheaper sign-valued relaxation to an invariant of actual common rows. It is not another encoding or a selected support case.

## 0. Sources, imports and separation

Only the new S1/S2 packet is a problem source: `institute/runs/three-area-2026-10-27-96h/written-releases/info-4-actual-rows-packet-v1.md`, SHA256 `6a4abaf97065c6c4b5181529810e622f76e3f485660f489593cda3ccaa88878c`, complete LF1-37. The source/provenance/controls and actual pre-body ACK are as in v1. S2 supplies the exact CPro1 PROB_DEF literal, not a verbatim-book or current-openness certificate.

**Imports:** elementary bijections and finite double counting; the identity `2uv=u²+v²−(u−v)²`; elementary graph connectivity, multigraph Laplacian energy and finite-dimensional quadratic forms. Every operative identity and connectivity claim is proved here. No old turn/converse, endpoint, support, candidate, private type8 or reviewer result is used. Prior authorship/exposure is not cleansed or certified independent.

Written reasoning only. No interpreter, calculator, Eval arithmetic, CAS, program, enumeration, selected numeric/control/boundary probe, solver, replay, modelCLI or new GO.

## 1. Object, variables and the proposed necessary invariant

Let n≥5 and let `a_r(1),…,a_r(n)`, for r in a set of n row identities, be actual permutations of one n-symbol set X. Assume all directed LINEAR distance1 events are distinct (hence cover all ordered pairs of different symbols) and all directed LINEAR distance2 events are distinct. The original slot is n=11. No column, cyclic, graph-regularity, support or row-normal-form assumption is made.

Write:
- **B** for the set of directed boundary adjacency events: positions1→2 and (n−1)→n in every row;
- **I** for the directed interior adjacency events: positions i→i+1 with 2≤i≤n−2;
- **M** for the directed ordered pairs of different symbols NOT occurring at distance2.

Each directed pair is an adjacency exactly once, so B and I are disjoint sets partitioning all directed pairs. Since the n(n−2) distance2 events are noncolliding, M is a set of n directed pairs, not a multiset. No degree-regularity of M is assumed.

For ANY function f:X→R define the common-middle sum

`Q(f) := Σ_r Σ_{i=1}^{n−2} (f(a_r(i))−f(a_r(i+1))) (f(a_r(i+2))−f(a_r(i+1)))`.

Crucially, the two differences in each product use the SAME actual consecutive triple and the SAME middle occurrence. One cannot choose their middles independently from a pair/triple-margin relaxation.

### Theorem 1 — exact common-middle identity

For every such array and EVERY real f,

`2 Q(f) = Σ_{(x,y)∈I} (f(x)−f(y))² + Σ_{(x,y)∈M} (f(x)−f(y))²`.       (CM)

In particular Q is positive semidefinite. For n≥5 it is strictly positive for every nonconstant f.

This is a necessary invariant of the original actual rows, not a proposed sufficient representation. Its converse is NOT asserted.

## 2. Proof of the identity

For an individual consecutive triple (a,b,c), put u=f(a)−f(b), v=f(c)−f(b). The elementary identity gives

`2(f(a)−f(b))(f(c)−f(b)) = (f(a)−f(b))² + (f(b)−f(c))² − (f(a)−f(c))²`.

Let E1, E2 and EB be the sums of squared differences over all actual directed distance1 events, all distance2 events and the boundary adjacency events respectively.

Upon summing over the actual rows:
- every interior adjacency event belongs to TWO consecutive triples;
- the first and last adjacency event in each row belongs to ONE triple;
- every distance2 event belongs to its ONE consecutive triple.

Hence

`2Q = 2E1 − EB − E2`.

This is where the common-row realization enters: independently supplied distance layers do not justify the first multiplicity assertion.

Exact distance1 coverage and distance2 noncollision imply

`E1 = Σ_{x≠y}(f(x)−f(y))²`,

`E2 = E1 − Σ_{(x,y)∈M}(f(x)−f(y))²`.

Substitution gives `2Q = E1−EB+EM`. Since I is the adjacency complement of B, E1−EB=EI, proving (CM). ∎

## 3. Positivity is strict: the interior adjacency graph is connected

View I as an undirected multigraph by forgetting each directed event's orientation but retaining opposite directed events as distinct edges. This is NOT the missing-distance2 graph. We prove this graph connected for every n≥5.

**Endpoint count, proved from the literal rows.** Each symbol x occurs in n rows and has n−1 outgoing adjacency events (one to every other symbol). Exactly one occurrence is therefore last. The incoming count similarly makes exactly one occurrence first. These two occurrences cannot be the same occurrence when n≥2.

Suppose a nonempty proper cut A⊂X, |A|=k, had no I-edge across it. Then all `2k(n−k)` directed adjacency pairs across the cut would belong to B.

- If `2≤k≤n−2`, then `2k(n−k)≥4(n−2)>2n=|B|` for n≥5, impossible.
- If k=1 (or n−k=1), let x be the isolated symbol. Its directed adjacency incidence count is `2(n−1)`. Its incidence in B is at most `n+2`:
  - being first once and last once contributes two boundary-edge incidences;
  - being second or penultimate contributes at most n more, because these are distinct positions in a row for n≥4 and the symbol occurs once per row.
  - For n≥5, `n+2<2(n−1)`, so some incidence lies in I, again impossible.

Thus every nontrivial cut has an I-edge. The graph is connected. Every nonconstant f differs across some I-edge, making EI(f)>0. By (CM), Q(f)>0. ∎

The restriction n≥5 is used only for this strict-positivity argument; (CM) itself holds at n≥3. No statement for smaller sizes is obtained by silently extending the strictness proof.

## 4. The combined graph is regular; M need not be

Form G from one undirected edge for each directed event in I and one for each directed missing pair in M. Parallel edges are retained; no loops occur.

Then

`Q(f) = (1/2) f^T L_G f`,

where `L_G` is the ordinary undirected multigraph Laplacian. The graph G is connected because its I-subgraph is connected.

**Regularity is a conclusion about G, NOT about M.** In the expansion

`(f(a)−f(b))(f(c)−f(b)) = f(a)f(c)−f(a)f(b)−f(b)f(c)+f(b)²`,

the three labels are distinct, so the only square term is at the middle b. Every symbol is internal in exactly n−2 actual row occurrences, by the endpoint count. Thus the diagonal coefficient of Q is n−2 for every symbol. Since Q=(1/2)L_G, every G-degree is exactly `2(n−2)`.

For each unordered pair {x,y}, let b_xy be how many of its two directed orientations lie in B, and m_xy how many lie in M. Then G's edge multiplicity is

`g_xy = 2 − b_xy + m_xy`, with `0≤g_xy≤4`.

In particular the common-middle matrix has nonpositive off-diagonal entries, zero row sums, constant diagonal n−2 and kernel precisely the constants. Positivity alone is weaker than this exact Laplacian identity.

**At the ORIGINAL size n=11**, these identities give, by symbolic specialization:
- I has 88 directed events, M has 11 and G has 99 edges counting multiplicity;
- G has degree18 at every vertex;
- Q has diagonal9 and rank10, with strict positivity on the subspace of zero-sum nonzero weights.

These numbers are not outputs of a scientific calculation, selected test, claimed missing-graph regularity or new support bound.

## 5. Simultaneous cut constraints on actual consecutive triples

For a subset A⊂X, let `Alt(A)` count actual consecutive triples whose outer labels both belong to A and whose middle lies outside A, or whose outer labels both lie outside A and whose middle lies in A. These are the singleton middle runs in the row's A/complement membership word. Let Bcut(A) and Mcut(A) count the directed boundary/missing events across A.

Taking f to be the indicator of A in (CM) gives the exact identity

`2 Alt(A) + Bcut(A) = 2|A|(n−|A|) + Mcut(A)`.                      (CUT)

It holds SIMULTANEOUSLY for every A in the same array. It follows that

`Alt(A) ≥ |A|(n−|A|)−n`,

and, for every nonempty proper A at n≥5, `Alt(A)≥1` by connectivity. For a singleton {x}, Alt({x})=n−2 directly: x must be the middle; it cannot occur at both outer positions of a row triple.

Thus a candidate collection of row/triple data that gives a nonconstant f with Q(f)≤0, or violates the exact cut equation for any A, cannot be completed into an original array. No particular subset, weight, boundary state or numeric candidate was selected or probed here; this is a universal written necessary condition.

## 6. Original-object caller and exact remaining implication

**Forward:** every original Tuscan-2(11) array has the common-middle Laplacian/cut identities and strict positivity just proved. They couple the two event layers to one actual row realization and include every endpoint term.

**Converse boundary:** a connected degree18 multigraph, a positive semidefinite matrix, consistent pair margins or the cut inequalities alone do NOT constitute eleven actual rows. No sufficiency theorem is claimed. The exact row realization equivalence remains v1 Lemmas1-3; any construction must still supply its full coherent relative maps and actual rows, or directly give the rows.

**What changes:** we now have a matrix/cut certificate necessary for any common-row gluing, beyond merely restating the original incidence constraints. Its proof identifies precisely which overlap multiplicities and boundary events a relaxation must retain; it cannot be obtained by claiming that unrelated pair/triple margins are already actual rows.

**What does not change:** no original witness, global no-go, support exclusion, book-equivalence or current-openness conclusion. These are all-variable necessary conditions only; not a proof that an original array exists or cannot exist, not novelty clearance and not a parent adoption.

**Next admitted step:** determine whether the exact common-middle Laplacian plus original event margins still leave an identified global-realization gap. Seek a genuine structural bridge or an exact failed implication, not a numerical check or an arbitrary sample. Continue within S1's literal-definition and elementary-fact inputs; no old stopped method or source is reopened.

All old STOP/HOLD/ZERO/process qualifications, prior exposure, N4 UNKNOWN/historical exit UNESTABLISHED and auxiliary214 STOP persist. Written, same-harness, unreviewed; no formal/kernel, executable, human, independent-family, priority or novelty gate.
