# Nine-edge critical PH7 requires nonsingleton input or exit support

Status: **WRITTEN**, pending independent review. The graph-specific result below is exact and requires no numerical search, no hidden-root reality assumption, and no new coefficient certificate. Its application to every nine-edge PH7 depends on the separate, as-yet-unadopted graph-template and irreducibility results named at the end. It is not a general PH7 exclusion.

## 1. Claim

On the graph consisting of two disjoint directed triangles, one remaining vertex, and three directed connector edges forming a cycle between the three contracted components, there is no seven-state representation of the target transform at any `z>1/5` with **both** the input supported on a single state and the exit supported on a single state. In particular, at `z=8/9`, such a nine-edge graph would require at least two input states **or** at least two exit states (or both).

The statement concerns a row-conservative normalized generator `G` with this graph, nonnegative input `beta` and exit `gamma`, and transfer function proportional to

`1/[y*((y+1)^2+z)^2]`.

The graph has no bidirectional edge. The result is invariant under the positive diagonal similarity and positive rescalings used in the Perron normalization, because they preserve the zero/nonzero supports of the original PH input and exit vectors.

## 2. Unique simple route between different components

Inside either triangle every vertex reaches every other in at most two directed edges. The singleton reaches itself in zero edges. Therefore if a supported input/exit pair has shortest-path distance at least four, its endpoints lie in **different** contracted components.

For any two vertices in different components, their directed simple path is unique. To leave a triangle the path must reach its unique connector-departure vertex by following the directed triangle; it cannot go around and repeat that vertex. The contracted component graph is one directed 3-cycle, so to make a full additional lap before reaching a different destination component would repeat a connector endpoint (or the singleton). Finally, on entering the destination triangle, the directed internal segment to its destination is unique; an external detour would require repeating a connector endpoint. Thus no distinct simple path exists.

## 3. Trace contradiction

Let the singleton input and exit states be `i,j`, and assume the target transfer has relative degree five. Because all off-diagonal transition rates and supported input/exit weights are positive, the first nonzero Markov parameter is the weight of the shortest directed walks. Hence the shortest distance from `i` to `j` is exactly four. By §2 the unique simple `i`-to-`j` path `P` has four edges and visits five vertices.

The path expansion of the adjugate then says, up to one strictly positive scalar, that the transfer numerator is the characteristic polynomial of the principal submatrix on the two vertices outside `P`. There are no two-cycles in this graph, so if their normalized diagonal rates are `rho,sigma`, this numerator is exactly

`(y+rho)*(y+sigma)`.

On the other hand the characteristic polynomial is

`D_z(y)*Q(y)`, where `D_z(y)=y*((y+1)^2+z)^2`,

and the target transfer is a nonzero constant divided by `D_z`. Multiplication by the determinant forces the monic hidden quadratic to be `Q(y)=(y+rho)*(y+sigma)`, even if no separate assumptions about hidden roots or minimality are made.

Writing the seven diagonal rates as `u_v=-G_vv`, trace comparison gives

`sum_v u_v = 4+rho+sigma`, hence `sum_{v in P} u_v=4`.

There are no directed two-cycles, so `tr(G^2)=sum_v u_v^2`. The eigenvalue list implied by the characteristic polynomial gives

`sum_v u_v^2 = 4*(1-z)+rho^2+sigma^2`.

Consequently `4*(1-z)=sum_{v in P} u_v^2 >= (sum_{v in P}u_v)^2/5 = 16/5` by Cauchy-Schwarz. Therefore `z<=1/5`, proving the claim. No input/exit normalization factor enters this argument.

## 4. Application and scope

The independent graph-specific claim in §§1–3 requires the specified triangle-connector graph, not a priori graph enumeration. Applying it to **every** critical PH representation with nine transitions additionally requires the pending result `frontier-20261028-ph7-critical-nine-edge-graph-template-v1.md`, its triangle-imbalance capacity and overlap-budget inputs, and the round's separately supported reduction to a seven-state irreducible Perron-normalized generator. These are not retroactively adopted here.

This support restriction does not exclude multisupport PH7, does not exclude graphs with ten or more transitions, and does not establish existence or exclusion at `8/9`. It is not a formal proof, independent audit, novelty clearance, or parent adoption.
