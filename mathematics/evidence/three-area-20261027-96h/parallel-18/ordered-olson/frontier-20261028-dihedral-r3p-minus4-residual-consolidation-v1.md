# Conditional consolidation of the `R=3p−4` residual

Owner **MathOlson-2-2**. Native `/bin/date` before this write: **Wed Oct 28 18:44:01 PDT 2026**. This is a **CONDITIONAL WRITTEN consequence** of the exact same-owner candidate inputs listed below. Those candidates are pending the applicable disjoint full-source reviews; this consolidation does NOT upgrade their assurance, settle L_RES, or claim an original avoiding word.

## 1. Exact inputs, scope and conditional high-diversity theorem

For odd primes p>=5 and actual original `D_(2p)` words of length4p−1 with R=3p−4 rotations, the following exact pinned candidates are used:

* `frontier-20261028-dihedral-three-value-swaps-v1.md`, SHA256 `dc24d3f6e6bbc0c25a2682c5ab2a5a0115b9aa3e114cba70d2de23d055d6bccf`: a fixed actual reflection pair with signed support>=3 and M<=2p−3 has a two-reflection selector; the stated diverse-boundary case also works.
* `frontier-20261028-dihedral-boundary-half-sum-v1.md`, SHA256 `05128e734e2287e469d763e93e340f184459faa4070fa74a11adaaa42f6d881c`: at M=2p−2, the specified pair's selected-rotation support is full unless all outlier differences belong to a single opposite class, in which case its unique missing residue is T_ij/2.
* `frontier-20261028-dihedral-all-high-proof-v1.md`, SHA256 `d1b0e65b31b9c7128f2c3f74b30550b367e39890717d0fb0ba2118dfc3427e74`: if EVERY actual reflection pair has signed M>=2p−1 then an original selector exists.

Conditional on those inputs, if the raw rotation exponents have **at least seven distinct values**, W has an actual original-order identity selector of exactly2p occurrences.

Proof: for ANY pair, each signed value can originate from at most its two raw values ±x. Thus at least seven raw values imply at least four distinct signed values. If its M<=2p−3, the first input selects. If M=2p−2, at least three distinct outlier values cannot all belong to one opposite difference class, so the second input selects. Under no-selector, every pair must therefore have M>=2p−1; the third input selects. QED conditional on the named candidates. For p=5 the seven-value premise is impossible and no theorem about all p=5 words is inferred.

## 2. The exact 5–6-value residual

Assume the same candidate inputs and suppose, only for deriving necessary conditions, that an actual W has NO original selector and has at least five distinct raw rotation values. Every signed pair has at least three values. Every pair with `M<=2p−3` would select by the first input. Every pair with `M=2p−2` and more than one opposite outlier-difference class would select by the second. The all-high input says at least one pair must have `M<=2p−2`.

Consequently every low pair of this hypothetical word has all of these properties:

1. `M=2p−2` and its unique signed majority x has the other signed values in exactly one symmetric class `{x+d,x−d}` with d!=0. Its selected-rotation support has the unique missing value `T_ij/2`.
2. x!=0: otherwise `2p−2` actual zero rotations and two equal-exponent reflections, guaranteed by `F=p+3>p`, would give an identity selector.
3. Its raw rotation exponents lie in `{±x, ±(x+d), ±(x−d)}`. In particular a no-selector word has at most six distinct raw rotation values, and at least `2p−2` raw occurrences in `{x,−x}`.

These conditions also explain why the high-diversity threshold above is seven, not a silent claim for five or six values.

## 3. Global majority alignment and graph potential

Each pair's signed maximum is at least2p−2 and has a UNIQUE majority, because `2(2p−2)>3p−4`. Any two such majority classes share at least

`2(2p−2)−(3p−4)=p`

actual rotation occurrences. Zero majorities have just been excluded. On a shared actual raw exponent the two signed values differ only by sign. Therefore there is a single nonzero a, determined up to sign, such that EVERY actual pair's majority is a or −a. This is a written necessary condition, not a guessed common anchor.

For each LOW pair (i,j) with `M=2p−2`, no-selector forces the exact directed reflection difference `y_j−y_i=T_ij/2`. Let P_i be the raw sum of the actual rotation exponents strictly before reflection i, and T_0 the total raw rotation exponent. Then `T_ij=T_0−2(P_j−P_i)`, hence

`(y_j+P_j)−(y_i+P_i)=T_0/2`.  (1)

Thus all low edges carry the SAME directed increment in the actual potential `y+P`. In particular, if `T_0!=0`, the low-edge graph has no triangle in a hypothetical no-selector word; more generally every oriented cycle must have zero edge-label sum. These are necessary graph constraints only. They do NOT assert that a zero-cycle potential yields an avoiding word, a four-reflection selector, or an L_RES bridge.

## 4. Two raw opposite values: conditional precise reduction

If instead the raw support consists only of `{a,−a}` for nonzero a, all-rotation selection already works when either sign appears at least2p times or both appear at least p times. Otherwise orient the more frequent sign so that its count is at least p−1 and the other count is at most p−1. Because the total is3p−4, the three remaining possibilities are

`(2p−1,p−3)`, `(2p−2,p−2)`, `(2p−3,p−1)`.

The latter two are separately addressed by same-owner pending candidates `frontier-20261028-dihedral-type2-separated-proof-v1.md`, SHA256 `556fd2a1e92eb3a6b4bff4a89068949608db37f938cd44334870f9abc8b79530`, and `frontier-20261028-dihedral-type3-triangle-proof-v1.md`, SHA256 `5ad3a0981c377dd0d4e21317223fdb5b137e73a61a6e439da757129d94568f61`. Conditional on those proofs, only `(2p−1,p−3)` remains in the two-sign branch. Its no-selector residual is narrowed, but not closed, by `frontier-20261028-dihedral-type1-separated-proof-v1.md`, SHA256 `244dfd9d900ad39e2c26c6aa4497675cb4fc1106c8471a0b34791a9e4e2aa4ec`.

A third identical core orientation or an isolated reflection-run example is not a substitute for paying this exact remaining compatibility gap. The separately proved six-reflection family is solvable and shows that restricting to two/four reflections is insufficient.

## 5. Assurance

No new scientific computation was performed for this consolidation. It combines the exact scoped written implications above and elementary cardinality, and remains conditional until each named input receives its own applicable review. This is not an independent source audit, formal/kernel result, SOTA/novelty claim, L_RES proof or global ordered-Olson closure.

**END — conditional high-diversity and exact low-edge residual.**
