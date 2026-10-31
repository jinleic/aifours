# Mixed-block visibility certificates for binary syndrome planes

**Status: WRITTEN with 73 exact independently checked certificates; scientific review pending; partial census.** This extends `frontier-20261028-visibility-lattice-theorem-v1.md` SHA-256 `4180f4e072d3e3e7108c66d90aeadebd169fee6b46dcf64e72b37ab10a357b50` to planes where the full-model lattice does not apply, by first conditioning away the fixed-syndrome factors.

## Statement

In the q=8 binary ten-triangle encoding, let an original-neighbour FD law have syndrome support inside an affine two-plane whose varying-factor set `J` covers all vertices and has at least five elements. Condition on the full tuples of the fixed-syndrome factors; in each fiber let `Y_v` be the selected `J`-components and `S` the selected syndrome vector. Then `Y` satisfies the original graph FDs, `H(S|Y_V)=0`, the `J`-local component FDs `H(Y_v|Y_{L_J(v)},S)=0` (with `L_J(v)` the other vertices of selected triangles through `v`), the conditional factor gate `3H(Y_V)+17H(S)-2 sum_v H(Y_v,S)<=0`, and `H(S|Y_{N(v)})=0` at every vertex whose incident selected parities are injective on the plane.

For each pair `(J,U)` in `frontier-20261028-mixed-visibility-certs-part1.json` SHA-256 `5b3189f3dc081367334e3ddc55773b50d802e1bc73739bc18b3151607c669620`, there is an exact rational identity, averaged over a stabilizer subgroup of the four factor-preserving graph automorphisms, expressing the mixed-block `Delta` as negative multiples of elemental CMIs, a positive multiple of the conditional factor gate, and vanishing FD terms, with visibility used only on `U`. Thus every mixed-block fiber with visibility containing `U` has nonpositive gap, and fixed-factor tensorization (as in the pinned noncover gate) gives `Delta<=0` for the original law, for **any** syndrome support in the plane, arbitrary probabilities and correlations. The plane-specific bound `H(S)<=2` was excluded from every certificate.

`frontier-20261028-mixed-visibility-check.py` SHA-256 `699b486874902dd0826bcbe7877874eeeed5c2b29c239321933df40835284413`, receipt SHA-256 `a32e9a32e2bea276d725e13334e81feca66a5200e1979585954ce5db0e77b1c4`, independently pushes every row through its stabilizer, verifies that each subgroup element preserves `J` and `U`, checks gate and CMI signs, rejects the cap row, verifies all 2,047 raw coefficients exactly, and rejects a certificate whose visibility set is shrunk.

## Exhaustive plane accounting

The same receipt classifies all 174,251 direction planes:

| class | planes | justification |
|---|---:|---|
| varying factors do not cover | 20,993 | noncover gate (pinned proper-subgraph import) |
| covering, exactly four varying factors | 247 | `frontier-20261028-fourfactor-plane-complete-theorem-v1.md` SHA-256 `7148eb8fa7ef068743d927454c779290b0f3b4238940c7f4226b50bcb707cde5` |
| full-model visibility contains a generator | 145,248 | full-model lattice theorem |
| mixed-block certificate applies | 2,770 | this note |
| **unresolved by these methods** | **4,993** | — |

Thus, subject to independent review of every imported theorem and of this note, `Delta<=0` holds for all original FD laws supported in any affine translate of 169,258 of the 174,251 binary syndrome direction planes. A bounded continuation of the mixed-block search is in progress; unresolved planes are not counterexamples. This does not bound the unrestricted guessing number; formal proof and novelty clearance are not claimed.
