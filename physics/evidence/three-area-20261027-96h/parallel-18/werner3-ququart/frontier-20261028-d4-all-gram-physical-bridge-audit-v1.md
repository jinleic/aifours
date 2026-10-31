# Physical factor-to-source bridge for every used d4 Gram row

**PhysicsResearch96h-2 / physics-1.** Native clock before writing: Wed Oct 28 18:21:18 PDT 2026. This addresses the active original-operator-to-certificate bridge, beyond the four coupled entries explicitly displayed in the consolidated proof. It checks **all** used d4 single-row and coupled-row source-family assignments against arbitrary complex physical factors, including the exact mapping actually consumed by our global identity checker. It does not infer parent adoption or replace the separate source-span, equality, identity, PSD, or runtime checks.

## 1. Literal physical index identity

Let a,b∈V=H⊗C² be arbitrary complex vectors. An actual source row is a four-token string `u=(u0,u1,u2,u3)`, each token `a`, `b`, `a*` or `b*`; star means componentwise complex conjugation of the **entire** V replica. Two rows u,v in one Gram type have the same starred slots, as required by the source definition.

For full replica indices `i=(i0,i1,i2,i3)`, `j=(j0,j1,j2,j3)`, the actual physical entry is

`|u><v|[i;j] = product_(t unstarred) uletter_t[i_t] conjugate(vletter_t[j_t])
                 · product_(t starred) conjugate(uletter_t[i_t]) vletter_t[j_t]`.      (1)

The source family Y_f is the actual outer product of `aaab`, `aabb`, or `bbba`. If its four family letters are L0..L3, an assigned family/ket/bra index rule `(f,kp,lp)` gives

`Y_f[kp;lp] = product_t L_t[kp_t] conjugate(L_t[lp_t])`.                              (2)

Both sides are products of commuting complex scalar coordinate factors. Equality for **arbitrary** a,b and **all** indices is therefore established exactly by equality of the multisets `(letter, original i/j slot, conjugation flag)`. This remains true when indices coincide or entries vanish; it is not a numerical generic-position assumption.

The `literal_rule` in our independent full corrected-identity checker chooses f,kp,lp directly from the row tokens. A different all-formal-factor checker independently forms the physical factor multiset from (1) and the assigned family multiset from (2), and compares them on every actual data type/row pair. The source's repeated letters are handled by the exact multiset, not by assuming an unproved ordered factor matching.

## 2. All actual d4 types and negative controls

`frontier-20261028-d4-all-physical-row-factor-check.py`, SHA256 `43e24e6ab64b2fae1fbf4e11104052007309d88eaa3dbdf36d588677f130ac3d`, reads only the hash-pinned public data and the hash-pinned owner global-checker mapping; no author `ep3core.py` or verifier is executed. Actual command `python3 frontier-20261028-d4-all-physical-row-factor-check.py` reported **PASS in 0.318 s**. Receipt `frontier-20261028-d4-all-physical-row-factor-check-results.json`, SHA256 `09c92fe97e57d6cb8588722145ddea1b45438ef7ab6feb8680e07e3548863aa9`:

- **1237** actual types: 1126 single rows and 111 two-row coupled types; no `gram2` type in this d4 data.
- **1570** total `(type,row,column)` occurrences, comprising **17** distinct physical row pairs.
- **Zero** formal factor multiset mismatches for all these occurrences.
- For **every one** of the 17 distinct pairs, swapping ket index assignments between two differently labeled letters was detected in memory. These intentional wrong-index tests are checker controls, not physical counterexamples.

The earlier four-entry table and its independent check remain a human-readable expansion of the coupled type; this new check additionally covers every single-row permutation/star pattern actually consumed by the identity algorithm. The source archive and corrected-data hashes, row counts and scoped method are recorded in the receipt. The checker shares the pinned owner `literal_rule` as the object being tested and Python data parser/runtime; the reference factor-multiset construction is separate. It is not an independent model-family or formal proof-assistant review.

## 3. From literal factors to original physical PSD

For each single-row type, `|u><u|` is a rank-one PSD operator on the four complete V replicas: starred slots simply contain conjugated physical vectors. For each actual two-row type, the physical operator is the **whole** rank-one block `|u⊕v><u⊕v|`; it is jointly PSD, not merely positive on each diagonal block. The four coupled-family entries agree with (1)–(2), including both different off-diagonal index orders.

Under a common local U on V, each unstarred slot transforms by U and each starred slot by conjugate(U). The two rows in a coupled type share their cut, so they carry the same tensor-unitary representation and the entire 2×2 block remains PSD under the actual common unitary twirl. Physical site permutations and complex conjugation likewise preserve PSD; their convex average does too. Arbitrary actual source module and joint-compression matrices act by congruence and therefore preserve PSD, with no independence, completeness, square or full-rank assumption.

The finite identity checker consumes exactly these family/index rules on its full orbit-sum source space; by linearity the factor identity applies after the same-pair physical twirl. The separately established 2- and 4-dimensional commutant spans, direct canonical source orbits, the five actual equality families, original unnormalized partial-trace objective, exact corrected identity and saved rational multiplier positivity are **all still required** for the full implication. This note is one bridge component, not a stand-alone q3 proof, a `gram2` audit for other dimensions, source-wide acceptance or a physical operational/novelty claim. Held historical results are nonpremises.
