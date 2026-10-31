# Every seven-state PH realization at 8/9 requires at least nine positive transitions

**CONDITIONAL WRITTEN THEOREM CANDIDATE; the named triangle theorems are not yet independently adopted.** MathResearch96h-2, original math-1. This is an edge-count lower bound, NOT an exclusion of seven states or a claim that the minimum PH order is8.

## Statement

At `z=b²/(a-c)²=8/9`, any actual PH representation of the original H using at most seven transient states must have exactly seven reachable states and at least **nine positive off-diagonal transition entries**.

The seven-state/reachability and eight-edge lower are the earlier independently supported structural results; the new step from eight to nine is conditional on these two separately frozen exact theorem candidates:

1. `frontier-20261028-ph7-critical-mandatory-triangle-v1.md`, SHA256 `d2437a46148569e7f43c76853331132a3481c20cff06317de57e538c92348612`: every critical seven-state spectral realization has a directed triangle, even with arbitrary 2/4-cycles. It uses symmetrization plus the 10666-leaf nonnegative-boundary Q/H certificate.
2. `frontier-20261028-ph7-one-triangle-full-critical-exclusion-v1.md`, SHA256 `2e30b352597880b78bfc59baa3adead91e4d4f0f1717a8cf7f684cee0a92decc`: a graph with no 2-cycle, exactly one triangle and no 4-cycle is impossible at the critical ratio, even with arbitrary longer cycles. It uses the four exact five-dimensional full-theta Bernstein certificates.

Their PH callers, exact arithmetic and dependencies require the separate requested full audits. The argument below is elementary graph theory and has no numerical premise.

## Proof

The earlier SCC theorem makes the seven-state graph strongly connected, and the earlier single-cycle argument gives at least eight edges. Suppose it has exactly eight. Every vertex has outdegree at least1, so exactly one vertex p has outdegree2 and all others have outdegree1. Starting from each of the two outgoing edges of p, follow the unique outgoing edge at every subsequent vertex. Neither path can enter a directed cycle not containing p: such a cycle consists only of outdegree-one vertices and could not reach p, contrary to strong connectivity. Thus both paths return to p; after they first meet they share the rest of their return path. Every vertex is reachable from p and hence lies on one of the two paths. Therefore the graph has exactly TWO simple directed cycles, both contain p, and their union covers all seven vertices.

The mandatory-triangle theorem says at least one cycle has length3. There cannot be two triangles: two cycles sharing at least p would cover at most `3+3-1=5` vertices. Their union covers seven, so the OTHER cycle has length at least5. Thus the graph has exactly one directed 3-cycle and no directed 2- or 4-cycle. The full one-triangle theorem excludes precisely this graph at8/9, contradiction. Therefore eight edges are impossible and at least nine are necessary. □

The proof uses only graph support after Perron similarity, which preserves positivity/zero of off-diagonal entries. It does not assume diagonal equalities, a particular theta labeling, a unique hidden mode, or the absence of longer cycles in graphs with more than eight edges.

## Boundary of the result

Graphs with nine or more transitions remain completely possible on the evidence here. In particular a seven-state 8/9 realization might still exist on such a graph. No all-topology 8/9 exclusion, order8 theorem, explicit witness, novelty, human/cross-vendor/Lean verification or retroactive process repair is claimed. Independent review should check both triangle theorem dependencies and the two-cycle decomposition of strongly connected n-vertex/n+1-edge graphs before adopting this corollary.

END — any critical seven-state PH realization needs at least nine directed transitions; seven-state existence remains open.
