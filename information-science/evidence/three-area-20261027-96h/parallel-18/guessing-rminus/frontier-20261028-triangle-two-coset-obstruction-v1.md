# Triangle-cover strategy and its two-coset obstruction

**Status: WRITTEN with exact finite graph checks; restricted construction only.** This is not a new bound on the guessing number. The construction reproduces the previously known lower bound `20/3`. Its obstruction rules out only supports contained in the union of two affine cosets of one specified triangle-parity code. Supports involving three or more cosets, other codes, nonlinear laws and arbitrary alphabets are not ruled out.

## Concrete graph and strategy

Use the original ten-vertex R-minus graph with neighbour sets

```
1: 2,3,4,5,6,7       2: 1,3,7,9,10
3: 1,2,4,8,9         4: 1,3,5,8,10
5: 1,4,6,9,10        6: 1,5,7,8,9
7: 1,2,6,8,10        8: 3,4,6,7,9,10
9: 2,3,5,6,8        10: 2,4,5,7,8
```

The following ten triangles cover every vertex exactly three times:

```
123  145  167  239  2,7,10  389  4,5,10  4,8,10  569  678
```

Let `A` be any finite abelian group of order `s >= 2`. Give each vertex one `A`-coordinate for each of its three triangle occurrences, so its alphabet is `A^3`, of size `q=s^3`. For each triangle `t`, require the sum of its three coordinates to be zero. A vertex recovers each of its three components as minus the sum of the two components at the other triangle vertices, which are original graph neighbours. This defines a full-domain decoder, not merely a decoder on the support. The ten triangle constraints use mutually disjoint coordinate triples. Therefore their solution subgroup `C` has exactly `s^20` words, attaining `log_q |C| = 20/3`. For `A=F_2`, this is the explicit `q=8`, `2^20`-word support.

## Two-coset theorem

More generally, let a finite simple `K4`-free graph have a triangle multiset in which each vertex occurs the same number of times. Construct its coordinatewise triangle-sum code `C` over any finite abelian group `A` exactly as above, with separate coordinates for triangle occurrences. Then **every functional-dependence support contained in the union of any two affine cosets of `C` has cardinality at most `|C|`**.

Proof. Let the *syndrome* of a coordinate vector be the vector of its triangle sums. The syndrome map is a group homomorphism with kernel `C`. Fix a nonzero syndrome `z`, choose an occurrence `t0` with `z[t0] != 0`, and choose a vertex `v` of that triangle. For every triangle occurrence `t` containing `v`, put `z[t]` into its coordinate at `v` and put zero in its other two coordinates. For a triangle occurrence not containing `v`, at least one of its vertices is not adjacent to `v`: otherwise that triangle together with `v` would form a `K4`. Put `z[t]` at one such non-neighbour and put zero at the other two coordinates. The resulting coordinate vector has syndrome `z`; its symbol at `v` is nonzero because of `t0`; and its symbols at every neighbour of `v` are zero. Thus it is a forbidden difference for any valid functional-dependence support.

Consider distinct cosets `a+C` and `b+C`. Join two words, one in each coset, when their difference is such a forbidden difference. The preceding construction gives at least one edge. Translation by `C` acts transitively on each side and preserves edges, so this finite bipartite graph is `d`-regular for some `d>0`, with both parts of size `|C|`. Hall's condition follows by counting the `d|U|` edges from a left subset `U`: their right endpoints number at least `|U|`. Hence there is a perfect matching. A valid support cannot contain both endpoints of any matching edge, so it contains at most `|C|` words in the two cosets combined. If the cosets coincide, the same bound is immediate. QED.

For the concrete R-minus cover this proves, for every finite abelian `A`, that no nonlinear selection from any two cosets of the above parity code can improve its `s^20`-word support. It does **not** show that all valid supports are of this form.

## Evidence and scope

* Baseline construction code SHA-256 `d72c85e79c93be68b847e3901b645f4fc11abfc931bb971a486c7a3974c741e1`; result `frontier-20261028-triangle-baseline-result.json` SHA-256 `1ef666a1eaa04836d3ae07a0f91a8883b57f7130bc26e7bd41eb7e4c47e13e82`. Z3 selected the cover; the script then checked the graph edges, cover multiplicities, the binary parity-check rank 10 and decoder components with integer arithmetic. The written construction applies to arbitrary finite abelian `A` independently of the Z3 choice.
* Separate graph-premise code `frontier-20261028-triangle-k4-check.py` SHA-256 `e282336df1dd3a8c752af26f7bc18503bf00d7118d7c9fc5269d93dca44d426a`; receipt SHA-256 `65d0b89e9516269cd87f7e9056b5b87db87a9183b959cb06bfb1214902aaed08`. It checked all 210 four-vertex sets for `K4`s, the ten named triangles and their vertex multiplicities, and 100 vertex/triangle non-neighbour premises.
* Independently of the general written proof, the binary syndrome code `frontier-20261028-triangle-coset-obstruction.py` SHA-256 `e43499dd9d70fa3f2e8bf6738105f9b4fa89ec8546187e307cdd0b0e0c29109e` constructed an explicit isolated-vertex witness for each of the 1,023 nonzero binary syndromes; receipt with witnesses SHA-256 `20b96652c8b74557a53ed0d6c2276b8c9b6c44df8ab3df9aec51508e8feb8d88`.

No formal proof, cross-model review, source-novelty clearance, global nonlinear upper bound or improved lower bound is claimed. The principal mathematical new idea is the elementary `K4`-free syndrome witness plus perfect-matching argument; its novelty has not been checked.
