# A reflection-turn exclusion for the original Olson lower residual

Owner **MathOlson-2-2**, original math-2. Native `/bin/date` immediately before this write: **Wed Oct 28 18:55:05 PDT 2026**. This is a **WRITTEN proof candidate** with the bounded original-word checks in §7. It has not received a disjoint scientific review, formal proof, novelty or global-adoption verdict.

## 1. Original problem boundary and exact contribution

The original named L_RES residual concerns actual zero-free singleton-gap words with `R=p+1` rotations, `F=3p−2` reflections, raw matching number `<=p−3`, and ALL retained OLD/REF/SEL/IPGEN/GS/DS3 caller failures. It asks for an original identity selection of exactly2p positions by a matching-packet route or a separately proved actual selector. The original precise statement is `mathematics/evidence/three-area-20261023-96h/parallel-18/ordered-olson/lower-matching-mechanism-PARK-v1.json` field `exact_unproved_residual_bridge` and `selection-lower-matching-packet-lift-v1.md:11–21,53–57`. No held mathematical guidance is used as a premise here.

A **REF-covered** word already has a reflection-only identity selector of length2p; it therefore satisfies the original identity selection but is OUTSIDE the actual REF-FAILURE residual. The earlier false L_MAX example is REF-covered, so it is not a counterexample to L_RES.

This paper proves new exact, all-prime **REF exclusions** from that residual. It does NOT prove L_RES, construct a residual avoiding word, or assume its other caller failures. The mechanism operates directly on the ACTUAL reflection-only subsequence and does not use the refuted raw matching packet-lift.

## 2. The general turn-matching theorem

Let p be any odd prime. Let an arbitrary original `D_(2p)` word contain exactly `F=3p−2` reflection occurrences, with chronological reflection exponents `y_1,...,y_F`; rotations, their positions and values are otherwise arbitrary. Put `d_t=y_(t+1)−y_t` in F_p for the LINEAR reflection order.

Suppose there is an index i with

`d_i !=0`, `d_(i+1)!=0`, and `d_i != d_(i+1)`,  (1)

and, after excluding the three reflection occurrences i,i+1,i+2, there are `p−3` disjoint pairs of consecutive reflection occurrences elsewhere whose exponent differences are nonzero. Then the original word has a **reflection-only** identity selector of exactly2p actual occurrences.

The paired reflections are consecutive in the **reflection subsequence**; they need not be adjacent in the full word because all intervening rotations are unselected. The p=3 case permits the common outside matching to be empty.

## 3. Proof: complementary omissions and an actual local flip

Take the same `p−3` outside pairs and form two actual reflection matchings:

* M_1 adds the first edge `(i,i+1)` of the turn triple;
* M_2 adds the second edge `(i+1,i+2)` of that triple.

Each matching consists of `p−2` disjoint adjacent-reflection edges with nonzero differences. Choose exactly ONE endpoint from each edge and retain every unmatched reflection. There are `F−(p−2)=2p` selected reflections in their actual chronological order.

Think of each paired edge as one two-choice block and each unmatched reflection as one singleton block. There are precisely2p blocks. The alternating sign ε_t of each block is fixed by its block position, independent of the endpoint chosen, because each block supplies exactly one reflection. For matching M, let μ_M be the midpoint of the two completely complementary endpoint choices:

`μ_M = sum_(singleton blocks t) ε_t y_t + (1/2) sum_(paired blocks t) ε_t (y_left+y_right)`.

As the p−2 endpoints are independently switched, each swap changes the alternating exponent by a nonzero residue. A proper nonempty subset of F_p grows under union with a nonzero translate, so the attainable support has at least p−1 values. Complementing every pair choice sends an attainable exponent v to `2μ_M−v`. Thus, if 0 is NOT attainable, support is exactly `F_p\{0}` and its unique missing value 0 is fixed by this involution. Since p is odd, this forces `μ_M=0`.

All common pairs and all blocks before the turn triple are identical for M_1 and M_2. The triple occupies exactly TWO blocks under each matching, so all later block signs also agree. If ε is the sign of the triple's first block, its doubled midpoint contribution is

`ε(y_i+y_(i+1)−2y_(i+2))` for M_1,

`ε(2y_i−y_(i+1)−y_(i+2))` for M_2.

Therefore

`2(μ_M1−μ_M2) = ε[2y_(i+1)−y_i−y_(i+2)] = ε(d_i−d_(i+1)) !=0`.  (2)

The two midpoint values cannot both be zero. Hence at least one matching family attains exponent0; choosing its actual reflection endpoints gives identity with2p reflections. In `D_(2p)`, an even reflection product has exponent the alternating sum just calculated. The actual full-word rotations are simply skipped. QED.

No independence or affine cancellation is asserted between separate raw-gap packet choices: the proof uses an explicit pairwise-disjoint matching in the reflection-only sequence and proves the one local midpoint difference (2).

## 4. Sparse equal-adjacency and no-equality consequences

Let z be the number of t=1,...,F−1 with `d_t=0`. If `z<=(p−1)/2` and there is ANY nonzero turn as in (1), the outside matching in §2 is automatic. Indeed, after deleting the triple the left and right paths have L+R=F−3=3p−5 vertices. Pair adjacent vertices greedily within each path. The number of disjoint pairs is at least

`floor(L/2)+floor(R/2) >= (3p−7)/2`.

Discard at most z pairs whose difference is zero; at least `p−3` nonzero pairs remain. Thus the general theorem applies.

In particular, if NO two consecutive reflection exponents are equal, W is always REF-covered. If a nonzero turn exists, use the previous paragraph. Otherwise all consecutive differences are one fixed nonzero d. Select the first2p actual reflections: the alternating exponent is p copies of −d, hence `−p d=0`.

This works for arbitrary actual rotation values, all raw matching counts and all reflection exponents satisfying the condition; it is not a statement that every word is REF-covered.

## 5. Cyclic consequence, retaining original order

Let `z_cyc` count equal-exponent edges between consecutive reflections in the CYCLIC reflection order, including last-to-first. A **cyclic nonzero turn** means two consecutive cyclic differences that are both nonzero and unequal.

If `z_cyc=0`, §4 already gives a reflection-only identity. If `1<=z_cyc<=(p+1)/2` and there is a cyclic nonzero turn, cut the cyclic reflection order at any equal-exponent edge. That zero edge is omitted, leaving at most `(p−1)/2` zero edges in the linear order; the two nonzero turn edges are not cut. Apply §4.

To return the selected indices to the original full-word order, sort those same actual reflection occurrences. Their selected product is a CYCLIC ROTATION of the product in the cut order. A cyclic rotation of an identity product remains identity: if UV=1, then VU=1. Therefore the selector is valid in the original order, not merely the cyclic order.

Consequently, any actual original REF-FAILING word—including any genuine L_RES residual—must satisfy

`z_cyc >= (p+3)/2`,

OR `1<=z_cyc<=(p+1)/2` and there is NO cyclic nonzero turn. In the latter case every maximal cyclic run of nonzero consecutive differences has a constant difference. This is a necessary residual condition only: it does NOT assert either alternative is realized, or that their union implies an avoiding word.

## 6. Exact remaining gap

Neither §4 nor §5 handles, in general, sparse-equality words whose nonzero-step runs are each straight but have different slopes across zero edges, nor words with many equal-adjacency edges. The retained OLD/REF/SEL/IPGEN/GS/DS3 residual failures and the raw matching bound are not reconstructed or discharged here. Proving that their remaining intersection has an original identity selector, or giving an actual counterexample, remains the user's L_RES task. REF-covered examples, including those in §7, are excluded from that intersection and are NOT counterexamples.

## 7. Actual bounded checks

`frontier-20261028-olson-reflection-turn-experiment.py`, SHA256 `7790784005e05ac1efaf9f5abc375f132da4f9d84c969fa8bb462408e50e9b11`, generated `frontier-20261028-olson-reflection-turn-results.json`, SHA256 `53b0d7c3351b07ece3c5dc61e052bb54a0726b82faa2635ef30332a155e43120`. Independently written `frontier-20261028-olson-reflection-turn-checker.py`, SHA256 `ed7b519328156f26e4f89f5290e8586b469eb43edecd153ce34427b60b0ce1db`, imported no producer code and returned `PASS_INDEPENDENT_REFLECTION_TURN_CHECK` in `frontier-20261028-olson-reflection-turn-check-results.json`, SHA256 `bcb4cd33bac0e130d63f361a54a9c3454cb4117db0edcac867906961342ded05`. It reconstructed 777 full original words with R=p+1 nonzero rotations and singleton CYCLIC reflection gaps at p=3,5,7,11,13; checked all matching blocks, support sizes, doubled midpoints, actual local-flip difference and original indices; directly multiplied every reflection-only selector. Branches were 742 turn-flips and 35 constant-step words; seven generated p=3 layouts without the tested turn were skipped and NOT claimed solved. Duplicate-index, false-midpoint and invalid-turn mutations were rejected for their intended reasons.

`frontier-20261028-olson-cyclic-turn-experiment.py`, SHA256 `70df3a13fd47a5411b94be1470e5424025368c1e74ceedda47224ef7be5a3d90`, reused the pinned turn constructor to generate cyclic-cut data `frontier-20261028-olson-cyclic-turn-results.json`, SHA256 `48ed6784fc525ec128ea774b9ae6b3dd7c975800dc91b1a9cd84dee89ebc58b9`. Independently written `frontier-20261028-olson-cyclic-turn-checker.py`, SHA256 `22c5c0869f13df89617e9c6473e3f607cea7bdd51514d9ff8408193a9b377082`, returned `PASS_INDEPENDENT_CYCLIC_TURN_CHECK` in `frontier-20261028-olson-cyclic-turn-check-results.json`, SHA256 `6f6888985b0f97af4f4111d09b56375f0361c4d1192edb351cc3f57dde3a43d9`. It checked 300 full original singleton-gap words, including 289 selected lists crossing the original start; it directly multiplied the cyclic-order AND restored-original-order selectors, and rejected three targeted mutations. The independent checker did not import the producer.

These finite checks do not establish the universal theorem, independently authenticate the historical caller failures, or confer formal/human/cross-family/novelty assurance. A complete disjoint written scientific review is requested.

**END — original-scope reflection-turn exclusion and honest L_RES residual.**
