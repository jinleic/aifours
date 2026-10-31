# Five-point FD laws on K4-free graphs obey the balance bound

**Status: WRITTEN with independently checked exact R-minus graph census; scientific review and novelty clearance pending.** Let a finite joint law satisfy the FDs of a finite loop-free directed graph whose underlying undirected graph is `K4`-free. If its joint support has at most **five** outcomes, then

\[
H(X_V)\le \frac23\sum_{v\in V}H(X_v).
\]

The actual R-minus graph is `K4`-free, so any original-neighbour R-minus FD law with a strictly positive balance gap must have **at least six** joint support words. This supersedes the support-three restriction in `frontier-20261028-three-point-support-bound-v1.md` (SHA-256 `1b1285d7f2a08dba922d49f517889f2e80e5edcfd37fa4c0dfbc1cd2f262ce82`). It is not a general no-gain proof, an alphabet-size lower bound, or a new guessing-number upper bound.

## A small coloring lemma

**Lemma.** In any `K4`-free simple graph, every non-3-colorable subgraph with at most ten edges has exactly the ten edges of a five-wheel `W5` (a 5-cycle and a hub joined to all five rim vertices), plus possible isolated vertices. Moreover, distinct five-wheels cannot share nine edges.

For the first claim, choose a vertex-minimal non-3-colorable subgraph. Every vertex has degree at least 3, since a 3-coloring after deleting a vertex could otherwise be extended. With at most ten edges it has at most six vertices. Four vertices would force `K4`. On five vertices its complement has maximum degree at most one. Two complement edges give a 3-coloring by pairing their endpoints, while at most one complement edge leaves a `K4`.

On six vertices it has nine or ten edges. With nine, it is cubic, so its complement is either a 6-cycle or two disjoint triangles; the former has a perfect matching and the latter is the union of two independent triples in the original graph. Either gives a 3-coloring. With ten edges, minimum degree three leaves either one vertex of degree five and five of degree three, or two vertices of degree four and four of degree three. In the first case the five neighbours of the degree-five vertex induce a 2-regular simple graph on five vertices, hence a 5-cycle, producing `W5`. In the second case the complement has degrees `(1,1,2,2,2,2)`, so it is `P6`, `P2` plus `C4`, or `P3` plus `C3`. In the first two cases it has a perfect matching, and in the third the complement triangle is an independent triple in the original graph while the other three original vertices need only two colors. Thus all three cases are 3-colorable. The non-3-colorable critical subgraph must be `W5`; its ten edges exhaust the original edge budget.

For the second claim, remove one edge from a five-wheel. If a spoke is removed, the old hub is the only vertex of degree four, so any one-edge completion to a five-wheel must restore that spoke. If a rim edge is removed, the old hub remains the unique degree-five vertex, and the only completion restoring all rim degrees is the removed edge. No new vertex can participate, because every old vertex still has positive degree. Thus a different five-wheel cannot share nine of its edges.

## From FD supports to three colors

Let `Omega` be the set of joint support words. For two distinct words `x,y`, put `D(x,y)={v:x_v!=y_v}`. Every vertex in this set has a graph neighbour in the set: otherwise the neighbour values of `x,y` would coincide while their value at that vertex differed, contradicting its FD. Hence the underlying graph induced by `D(x,y)` has no isolated vertex and in particular contains an edge.

Choose one such edge for each unordered pair of distinct support words and let `F` be their union. There are at most `binom(|Omega|,2)` chosen edges. If `|Omega|<=4`, `F` has at most six edges and the coloring lemma makes it 3-colorable. For `|Omega|=5`, suppose for contradiction that **no** choice of edges makes `F` 3-colorable. Any choice then produces a `W5` by the lemma. Its ten edges must be distinct, so the ten pairs of support words map bijectively to the ten edges of that wheel.

Fix one such choice. If some difference set induces another graph edge, replace its chosen edge by that second edge. If the replacement edge was already chosen, the new union has at most nine edges and is 3-colorable. If it was not, the new ten-edge union shares nine edges with the old wheel and cannot be a different wheel, so again the coloring lemma makes it 3-colorable. Both contradict the supposition. Thus every difference set induces exactly its chosen edge. Since it has no isolated vertex, the difference set consists of exactly that edge's two endpoints.

For any three support words `x,y,z`, the three corresponding graph edges are distinct. At every graph vertex, membership in exactly one of `D(x,y),D(x,z),D(y,z)` is impossible: equality of the other two coordinate pairs would force equality of the third. Therefore those three edges form a graph triangle. The `binom(5,3)=10` triples of support words give ten **distinct** graph triangles, because the ten support-word pairs map bijectively to the wheel edges. A five-wheel has only five triangles, a contradiction. Consequently some edge choice yields a 3-colorable `F` for every support of size at most five.

Color `F` with three colors and extend the coloring arbitrarily to isolated graph vertices. Each support-word difference set contains a chosen edge, so it meets at least two color classes. Let `Y_1,Y_2,Y_3` be the tuples of coordinates in the classes. Any two of these three tuples jointly distinguish all support words and hence determine `X_V`. Pairwise entropy subadditivity gives

\[
2\sum_{r=1}^{3}H(Y_r)\ge3H(X_V),\qquad
H(Y_r)\le\sum_{v:\,\mathrm{color}(v)=r}H(X_v),
\]

which proves the bound for arbitrary probabilities on the support.

## Exact graph evidence

The R-minus neighbours are exactly those listed in `frontier-20261028-sparse-coloring-structure-result.json` SHA-256 `75884fb96097853126b328c6308c822a8439bee05c0e94c083e91320e4c3062f`. Its producer `frontier-20261028-sparse-coloring-structure.py` has SHA-256 `ef6debf0726dd9fe7e940ad0d58a4cf93e14e8b5470912786656ab1039424146`. Integer enumeration checks all 848 induced subgraphs on at most six of the ten vertices, in particular all 210 four-vertex subsets, none of which is a `K4`. It identifies four non-3-colorable induced six-vertex subgraphs, all five-wheels, and records a 3-coloring after each of their 40 single-edge deletions.

Separately written brute-force checker `frontier-20261028-sparse-coloring-independent.py` SHA-256 `f9060fbf1d3036ee69999512ce872c3db0a669e772d440cd0794c6b07e30bb46`, receipt SHA-256 `5994e7fbec78f4fa864e713438e28d9676a107bf4a5e66df9044fe3103863eb4`, rechecks all 848 subgraphs, all 40 deletion-color witnesses, the five triangles per wheel, the original graph, and rejects 40 intended invalid-color mutations. The general coloring and entropy implications above are written arguments, not proof-assistant formalization or an independent scientific review.
