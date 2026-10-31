# Generic global qubit encodings have full support on every local site

**PhysicsResearch96h-2 / physics-1.** This is a WRITTEN all-variable structural theorem about the original global isometry domain, strengthening the one-site obstruction `frontier-20261028-d4-global-qubit-local-support-obstruction-v1.md`, SHA256 `8bcbf55a2dd63d524323588b133f38fc8f361dee2ef58e77de2e053d6f5511a2`. It does not evaluate q3 on a chosen vector/state, use a numerical parameter/control, disprove the target, or claim novelty/review/formal acceptance.

## Theorem

Let `H=(C⁴)^tensor3` and let `St(2,H)` be the space of all isometries `V:C²→H`. The set

`U={ V : rank[Tr_(other two sites)(VV†)] = 4 for EACH of the three sites }`

is **nonempty, relatively open and dense** in `St(2,H)`. Thus the original global rank-two encoding does not, even generically, give a local support of dimension at most2 at any site.

## Proof without selecting a target instance

Fix formal bases only to describe matricizations. For i=1,2,3, identify `H=C⁴_i⊗C¹⁶_(other sites)` and flatten a **formal variable** u∈H to a 4×16 matrix X_i(u). Let f_i be the determinant of any fixed 4×4 submatrix. Each f_i is a nonzero polynomial in the 64 complex coordinates: its determinant expansion contains a distinct diagonal monomial with coefficient1. The product `f_1 f_2 f_3` is nonzero because the complex polynomial ring is an integral domain. A nonzero polynomial over the infinite field C cannot vanish identically; hence there exist formal-variable values where all three matricizations have full row rank. No such value is specified, evaluated in q3, or used as a control.

More strongly, the nonvanishing locus of this homogeneous product is open and dense on the unit sphere of H: it is open by continuity; if it vanished on an open sphere patch, real-analytic continuation would make it vanish on the entire sphere, and homogeneity would then make it vanish on all of H, contradiction. Thus every unit u can be approximated by unit u' for which every X_i(u') has rank4.

For any V with orthonormal columns (u,v), choose such u' arbitrarily near u and apply the usual Gram–Schmidt step `v'=(v−u'<u',v>)/||v−u'<u',v>||`, defined for u' sufficiently near u. Then V'=(u',v') tends to V. For each i,

`Tr_(other sites)(V'V'†) >= Tr_(other sites)|u'><u'| = X_i(u')X_i(u')†`,

and the right side has rank4. Hence V'∈U, proving density. Each condition `det Tr_(other sites)(VV†)>0` is continuous on the isometry space, so U is relatively open. This also proves nonemptiness. All statements are exact linear algebra; no selected physical input or q3 value is used.

## Exact analytic implication and nonclaims

The local lemma `frontier-20261028-d4-local-qubit-corner-eb-analytic-v1.md`, SHA256 `3589a59a3dc019da87169a63844995c63e2016167dbcf1e863a048815a96eee8`, proves that `Psi∘iota_W` is measure–prepare for every **local** W:C²→C⁴. The theorem above shows that an attempted full original proof cannot obtain a local two-dimensional support merely from the global isometry condition, even by selecting whichever of the three sites looks favorable. A separate all-global-isometry tensor/PPT argument is still required; the theorem does **not** show such an argument is impossible or that global tensor EB/PPT fails.

The original fixed-d4 q3 target remains the complete arbitrary complex rank<=2 statement, and its separate public-source computer-assisted certificate remains conditional on the pinned math/code/runtime and review gates. No narrowed subclass is presented as the solution, no source novelty is asserted, and f62/parent, human/model-family and formal/Lean acceptance are not inferred. Old held outcomes are not premises; the actual earlier cadence gaps remain disclosed in `frontier-20261028-1904-cadence-breach-self-stop-v1.json`, SHA256 `8b794de4b92c3a50b497333ac1164ddb3800b17c9a8aa541eae57b104c60d24e`.
