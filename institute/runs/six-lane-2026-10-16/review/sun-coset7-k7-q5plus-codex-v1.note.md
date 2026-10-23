**Step 1: ACCEPT. Step 2: ACCEPT-WITH-FIXES. Lemma K7-Q5+: ACCEPT-WITH-FIXES.** The mathematical exclusion is sound. Two MINOR corrections concern wording and the claimed COV consequence; no FATAL or MAJOR proof defect. All six supplied SHA256 hashes match.

The bound \(|U|\ge4\) follows from K7 itself: each marker 2, 3, 5 has at most one carrier, hence \(|M|\le3\) (SOURCE01:21). If \(|U|=4\), there are three marked vertices. Their three nonempty, mutually disjoint marker sets must partition all three markers into singletons. Thus \(z_2,z_3,z_5\) exist, are distinct, and carry exactly their named markers. SOURCE00:32 is justified.

For Step 1, the opposite edge at \(z\) is \(vv'\), whose label is 5. Since \(h_z=0\), \(\delta_z(5)=1\), regardless of any excess 2- or 3-valuation. Its contribution to \(\tau_{\min}\) is therefore 5, and the P-grid at \(z\) is \(1/6\). At \(v,v'\), all relaxation factors equal 1 and both grids are \(1/6\). Consequently \(\tau_{\min},\tau_{\max}\), the rounded P bounds, and the label-dependent K2 containment restrictions coincide with the all-unmarked tests. K7-U then forces type \((5,5,5)\). Choosing another unmarked vertex for each \(v\) proves every asserted \(\alpha_{vz}=5\); V1 forces \(q_{v\to z}=1\).

For Step 2, write \(a=e_{z_2}-1\ge1\), \(b=f_{z_3}-1\ge1\), and \(h=h_{z_5}\ge1\). The six local indices are
\[
w_1,w_2,w_3,\quad 2^aw_{z_2},\quad3^bw_{z_3},
\quad q_5\,5^hw_{z_5}.
\]
The first five \(q\)-coordinates equal 1. Pairwise coprimality of the \(w\)-parts, their coprimality to 30, and \(q_5\le5\) isolate each unmarked neighbour.

Among marked neighbours, \(z_2z_3\) has gcd 1; \(z_2z_5\) is allowed exactly when \(q_5\) is even, and \(z_3z_5\) exactly when \(3\mid q_5\). Both pairs cannot occur because that requires \(6\mid q_5\). Heredity excludes every triple: a triple either contains an isolated unmarked neighbour or contains the forbidden pair \(z_2z_3\). Thus the complete allowed-set family consists of the empty set, singletons, and at most one specified pair.

In coordinate order \((u_1,u_2,u_3,z_2,z_3,z_5)\), three weight vectors suffice:

| \(q_5\) | Feasible \(y\) | \(\sum y_jq_j/6\) |
|---|---|---|
| 1 or 5 | \((1,1,1,1,1,1)\) | \(1\) or \(10/6\) |
| 2 or 4 | \((1,1,1,0,1,1)\) | \((4+q_5)/6=1\) or \(8/6\) |
| 3 | \((1,1,1,1,0,1)\) | \(7/6\) |

Every singleton has weight at most 1, and the sole allowed pair, when present, has weights 0 and 1.

VFC-count is strictly bounded by \(1-|U_v|/|G|<1\) (SOURCE04:48), so equality at \(q_5=1,2\) also contradicts it. Every admissible vector is covered: only \(q_5\) remains variable, and any \(\alpha_{vz_5}\in\{1,\ldots,5\}\) merely restricts its range within \(1,\ldots,5\). The weights may depend on \(q\). No special valuation cap or assumption on \(\alpha_{vz_5}\) is needed.

- **MINOR — [SOURCE00:55](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset7-k7-q5plus-review-v1/snapshot/00-K7-Q5-strengthening-v1.md:55):** After assigning zero weight, the allowed pair does not have “two positive weights.” Replace that sentence with: “The only allowed pair has weights 0 and 1; every other nonempty allowed set is a singleton.”
- **MINOR — [SOURCE00:64](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset7-k7-q5plus-review-v1/snapshot/00-K7-Q5-strengthening-v1.md:64):** Qualify dropping Q5 as valid for coverage of actual configurations. Rewriting COV’s abstract pattern statement requires adding the mixed-triangle tests used in Step 1; SOURCE03:27 does not presently require those tests between distinct singleton blocks and marked vertices.

The accepted \(|U|\ge5\) lemma is used only after independently excluding \(|U|=4\). **Q5 is excluded; K7 remains OPEN.**