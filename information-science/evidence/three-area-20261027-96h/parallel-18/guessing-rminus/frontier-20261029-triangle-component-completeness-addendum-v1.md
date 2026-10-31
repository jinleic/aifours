# Selected-degree completeness for component extensions

Read the source/representation contract in `frontier-20261029-triangle-component-extension-lemma-v1.md` first. This adds an actual encoding identity, not a graph-FD inference and not a two-syndrome entropy theorem.

For selected-factor set J, the variable Y_v is BY DEFINITION the tuple of the components at v belonging to selected incident triangles. If exactly one selected factor t contains v, then this tuple has one entry, its modeled component U. Hence Y_v and U determine each other, and H(K,Y_v,U)=H(K,Y_v)=H(K,U) for every K. The entropy-coordinate representation may identify them exactly.

The premise is checked from the actual coloring: `{t in J: v in T_t}={the modeled factor}`. It must not be inferred just because one factor's projection is modeled. Case 65 at factor 2 has this property at vertex 1. Case 493 does not have it at any vertex of factor 2, so the new identification must NOT be applied there.

Any proof using the identification must preserve this completeness premise in its certificate and validate it again when transporting the resulting coarse inequality. Extra fixed-factor components have already been conditioned to constants in the mixed-block fiber, as in the original representation contract. No independence, uniformity, entropy cap or original-graph-neighborhood deletion is assumed.

Status: WRITTEN elementary identity of the specified selected-component tuple; no Delta exclusion or global bound claimed.
