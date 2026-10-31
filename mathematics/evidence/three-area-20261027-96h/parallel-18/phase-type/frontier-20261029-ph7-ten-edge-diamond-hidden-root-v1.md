# A topology-fixed hidden pole on a ten-edge diamond support

Status: **WRITTEN**, a small exact strengthening of `frontier-20261029-ph7-ten-edge-diamond-support-factorization-v1.md` (SHA256 `d6a4ec797a1be76ab2afe0e0d67d0d72bf9694dedabb4e31cee4f151f4a56c8f`). It is specific to that graph and the support pair input `{1}`, exits `{4,5}`; it does not exclude the graph or decide PH7 at `8/9`.

With the graph, edge indices and positive rates `e0,...,e9` as in the parent manuscript, let the input be supported on state 1 and exit weights `beta_4,beta_5>0`. The entire actual numerator factorizes as

`alpha_1*e3*e4 * [beta_4*y+beta_4*e7+beta_5*e6] * [(e1*e5+e2*e9)*y+e1*e5*(e8+e9)+e2*e5*e9]`.

If the target is represented, the two hidden decay rates are therefore

`r=e7+(beta_5/beta_4)*e6 > e7`,

`s=[(e1*e5)*(e8+e9)+(e2*e9)*e5]/(e1*e5+e2*e9)`.

Here `u_3=e5` and `u_6=e8+e9` are the actual diagonal escape rates of the two diamond branches. The second hidden decay rate `s` is **independent of both input/exit weights** and is their weighted arithmetic mean:

`min(u_3,u_6) <= s <= max(u_3,u_6)`,

with strict inequalities unless `u_3=u_6`. The first decay rate can be tuned by the positive exit-weight ratio; the second cannot. This is an exact same-matrix path identity, not an eigenvalue computed from a selected numerical state. The separately frozen five-edge theorem forces `beta_5>0`, and relative degree forces `beta_4>0` in this slice.

Any exact realization must additionally make the characteristic polynomial vanish at both `-r,-s` and contain the doubled target pair. These are actual algebraic constraints, not shown inconsistent here. Other support rectangles, all 2-cycle topologies and the original PH7 question remain open. The imported factorization/five-path callers require disjoint scientific review; no novelty or parent adoption is claimed.
