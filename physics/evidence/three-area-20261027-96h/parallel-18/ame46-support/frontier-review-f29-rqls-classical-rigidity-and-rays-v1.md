# f29 — independent review of RQLS rigidity, 12/13-ray arrays and tangent bounds

Reviewer **PhysicsAME46-2**. Native observation immediately before writing: **`Wed Oct 28 17:28:49 PDT 2026`**, not an exact creation/completion/runtime clock. **Same-harness written reconstruction plus reviewer-written exact checks; not a formal/kernel, independent-model-family or novelty certification.**

## 1. Verdict, inputs and exact scope

**NO SUBSTANTIVE DEFECT AT THE EXACT STATED SCOPE — 0 FATAL / 0 MAJOR / 0 MINOR against the two candidates.** The general connected-pair-graph local rigidity proof, its converse via an explicit component rotation, Weisner Fig. 1 application, Parker-based 12/13-ray actual arrays and the [192,196] tangent bound independently reconstruct as described below.

These statements do NOT produce a 100-ray maximal-cardinality array, a global no-go, a local explicit radius, or an integrated non-gauge tangent direction at the 13-ray array. Modular nullity is an upper bound on characteristic-zero nullity, not automatically an equality.

Read the complete assignment FIRST, SHA256 `c7854f718451ae3a1ec071a1f6f43f9c34cb55ddc96ca9cbdadce9af704e5aa5`, then both complete candidate bodies:

- **C1:** `frontier-20261028-classical-rigidity-and-search-v1.md`, 125 LF, SHA256 `3dc1eea8fdb47c04c39dea1d0a8a85122680db29b3d8c3fdea6c7ce05f712f24`.
- **C2:** `frontier-20261028-parker13-tangent-frontier-v1.md`, 25 LF, SHA256 `f4d26f020e9db259d45824d05e9ec06e47f4529a124423ec34ca5b14aac87c68`.

Read `physics-5-rqls10-definitions-v1.md` SHA256 `259ecf96d147a0bdb72145c5da8a3b9f98329726c6412ca7ed8cba566d613a6e`, [Weisner 1963 primary Fig. 1](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/571060BE1548BAE1FE39B45B58F4403E/S0008439500051638a.pdf/special-orthogonal-latin-squares-of-order-10.pdf), and the local image of [Parker 1959, Section 3, p.861](https://doi.org/10.1073/pnas.45.6.859) from the cited paper PDF SHA256 `d00efa7a8e6966af64d4bb4ea7d0accdd33e8e174218b5c54879ca4f3e2f9090`. The exact 12- and 13-ray certificate files are bound by SHA in §5. The Weisner and Parker source tables were independently transcribed into my checker; no author checker code was imported.

Prior exposure: earlier RQLS/PPT cross-domain and own AME contacts persist; no blindness or independent-family claim. Historical quarantined outcomes were NOT accepted as premises. The candidate's random floating-point experiment and rejected web table are historical author-reported side results, not needed for the theorem or rerun here. No author contact, external-model call, nested agent or source-proof-body laundering occurred.

## 2. Exact original-object vocabulary

A registered QLS(10) is a 10×10 array of unit vectors in C^10, with every row and column an ONB. One resolution is a partition of its 100 actual cells into ten transversals, each meeting every row and column once and itself an ONB. Cardinality counts distinct rays among ALL cells. The original maximum target requires **100 pairwise nonparallel rays**, not merely a finite number of nonclassical rays.

For the general theorem let A and L be orthogonal Latin squares of order n≥3. In the classical array `v_x=e_{A(x)}`, each row/column/L-block contains each color exactly once. Thus the arrays built from such an OLS pair satisfy all 3n basis conditions; L labels actual transversal blocks because each L label occurs once per row/column. This is a fixed incidence/reference, not WLOG for arbitrary quantum arrays.

## 3. Full linearized constraints and gauge dimension

Fix any distinct colors a,b. Write `d_x` for a tangent variation at a color-a or color-b cell. For an a-cell x put `q_x=(d_x)_b`; for a b-cell y put `q_y=−conjugate((d_y)_a)`. For the UNIQUE a- and b-cells in any row/column/L-block, differentiation of their inner product gives

`0=conjugate((d_x)_b)+(d_y)_a`, hence `q_x=q_y`.

Every edge of the pair graph enforces exactly one such equality, and every original off-color orthogonality derivative appears in exactly the corresponding color-pair graph. Normalization gives `Re (d_x)_a=0`; the on-color component is one independent imaginary phase per cell. Hence for pair {a,b} the complex parameter q is constant on each graph connected component. If the graph is connected, it is one complex parameter q_ab for all its 2n cells.

For all a<b put `K_(b,a)=q_ab` and `K_(a,b)=−conjugate(q_ab)`, diagonal zero. K is skew-Hermitian and its off-color entries reproduce EVERY derivative. The remaining n² imaginary on-color entries are individual cell phases. Conversely a common infinitesimal unitary K and individual cell phases satisfy the differentiated normalization/orthogonality equations. There is no unexamined coupling between different color pairs: each derivative equation is indexed by a particular pair of colors.

For connected pair graphs, off-diagonal K contributes `n(n−1)` REAL dimensions and per-cell phases n²; total `2n²−n` real dimensions. Diagonal common-unitary phases are already contained in the per-cell directions and are not counted twice. At n=10 this is90+100=190, matching C1's stated count. This is the actual tangent kernel, not by itself a claim that arbitrary tangent directions integrate.

## 4. From tangent injectivity to actual local rigidity

Take an exact solution sufficiently close to the fixed classical reference. Its first row is an ordered ONB. Apply the inverse of the unique nearby common unitary carrying the reference first row to that ONB; the first row is now exactly fixed. Independently phase each other cell so its coordinate at its reference color is positive real; all those coordinates remain nonzero in a sufficiently small neighborhood. This does not change the ONB constraints or rays.

The remaining off-color complex coordinates form a finite-dimensional smooth chart, with the on-color coordinate the positive square root determined by unit norm. Let F collect real and imaginary parts of all within-block pair inner products. At the origin, the tangent-kernel description from §3 applies. The first row contains every color, so first-row variations force every off-diagonal entry of K to vanish. The positive-real gauge and normalization force all remaining per-cell phase variations to vanish. Therefore the gauge-fixed derivative `DF(0)` is injective.

On the finite-dimensional real coordinate space, compactness of its unit sphere gives a c>0 with `||DF(0)z||≥c||z||`. Differentiability gives `F(z)=DF(0)z+o(||z||)`. For sufficiently small nonzero z, `||F(z)||>0`, so the only nearby exact gauged solution is the reference. Undoing the gauges gives ONE common unitary and individual cell phases. Thus C1's local-rigidity conclusion is proved, not inferred from failed numerical optimization.

## 5. Converse: a disconnected pair graph gives an actual local deformation

Suppose one color-pair graph is disconnected. Choose one connected component and a small nontrivial real 2×2 rotation on the span of e_a,e_b; apply that SAME rotation to precisely the cells in this component and leave all others unchanged.

Every row/column/L-block contains one a-cell and one b-cell, and its edge joins them, so those two cells belong to the same component. The operation rotates either BOTH vectors in that block or neither, preserving their mutual orthogonality and their orthogonality to all other color vectors. It is an exact family of valid labelled arrays, tending to the reference as the rotation tends to identity.

Every graph component contains both colors because its vertices are joined by a/b edges. Thus at least one a-cell is rotated and another a-cell in a different component remains e_a. For a sufficiently small nonzero rotation these two rays are nonparallel; a single common unitary and cell phases would map all original color-a cells to the same ray. The deformation is therefore not gauge-equivalent to the reference. Thus, for this fixed classical incidence, **local rigidity iff every color-pair graph is connected**. This converse is an additional written reconstruction for the review; no global claim about arbitrary incidences is implied.

## 6. Weisner and Parker primary-data verification

### Weisner classical reference

The ten two-digit rows in C1 LF45–54 agree with primary Fig. 1. My checker independently verifies both coordinate tables are Latin (all row/column symbol sets) and their ordered pairs are all100 distinct. It constructs all30 actual row/column/label blocks, then all45 two-color graphs, and finds component histogram **`{(20,):45}`**. Therefore every required graph is connected. Combined with §§3–4, the particular fixed-resolution classical 10-ray reference is locally rigid up to common U(10) and phases. No global 100-ray exclusion follows.

### Parker actual 12-ray certificate

The published Parker section3 supplies two order-10 Latin tables. I separately transcribed their digits and checked all SIX pair projections of the four-coordinate orthogonal array have100 distinct pairs. Using original Parker row as color, original column and first square as array row/column, and second square as resolution label, I rebuilt the color-{7,8} three-block incidence graph: component sizes **6 and14**. On the six-cell component the exact two-level rotation with numerator matrix `[[39,−52],[52,39]]` and denominator65 reproduces the complete candidate array and labels byte-for-value. The 14-cell component remains unrotated.

The independent definition-level check finds **100 exact unit vectors, 30 ONB blocks, 1350 block off-diagonal zeros, 12 distinct rays and 408 parallel cell pairs**. Ray multiplicities are eight rays used10 times, two used7 times and two used3 times. This is a valid nonclassical 1-resolvable QLS(10), but not the original maximal-cardinality target.

### Parker actual 13-ray certificate

For the same independently transcribed Parker OA and the same coordinate-role mapping, exactly NINE four-tuples have all four coordinates in `{7,8,9}`. Applying `(3I−2J)/3` only to that 3-color subarray and leaving other cells unchanged reconstructs EVERY numerator vector and EVERY resolution label of the supplied certificate. `3I−2J` is the explicitly supplied integer Householder numerator, not an asserted external theorem.

The independent definition-level check finds **100 exact unit vectors, 30 ONB blocks, 1350 block off-diagonal zeros, 13 distinct rays and 387 parallel cell pairs**. Ray multiplicities are seven rays used10 times, three used7 times and three used3 times. Both finite constructions use their actual vectors/labels, not a marginal relaxation; neither has100 distinct rays.

## 7. Full tangent assembly and [192,196]

The 13-ray certificate uses REAL numerator vectors `n_x/3`. Write a complex variation `d_x=u_x+i v_x` with 1000 real coordinates in each sector. Differentiating norm gives

`sum_k n_{xk} u_{xk}=0`.

For every unordered pair x,y in each of the30 blocks, differentiating the complex inner product splits exactly into

`sum_k [n_{yk} u_{xk}+n_{xk} u_{yk}]=0`,

`sum_k [−n_{yk} v_{xk}+n_{xk} v_{yk}]=0`.

The denominator3 and harmless norm factor2 do not affect rank. There are100 norm rows plus30×45=1350 real orthogonality rows, and1350 imaginary rows; each sector has1000 columns.

My independently assembled integer matrices have exact dimensions/nonzero counts **1450×1000 / 3304** and **1350×1000 / 3186**. Their SHA256s exactly match the author's respective corrected v2 matrices: real `3ed6d188c5fd5ea8d6416df79d7cc86e88f19da0b3198ed5a430ff15946598a7`; imaginary `543b7bbd3712745cec53720ca01024dcaa619f46968262b2bb6ee722b2012459`. Byte equality is an assembly cross-check, not an assumption that the author generator is independent.

My separate C++ modular-elimination implementation checks 65521 is prime and returns:

`real: rank 952, nullity 48`; `imaginary: rank 852, nullity 148`.

For an integer matrix, a nonzero modular minor is a nonzero integer minor, so rational/real rank is AT LEAST the modular rank. Thus characteristic-zero tangent nullity is AT MOST48+148=196. A modular nullity is not a rational nullity lower bound, and equality of the numerical nullities is NOT claimed.

For the lower bound, common U(10) gives100 real parameters and the 100 individual cell phases give100 more. A stabilizer generator must make every occupied ray an eigenvector. The certificate contains all ten standard coordinate rays and three additional rays with all three coordinates nonzero on the `{7,8,9}` subspace. Thus the generator is diagonal in the standard basis, with equal diagonal phases on those three levels: seven independent phases outside, one inside, for stabilizer dimension8. Hence gauge-orbit dimension is `100+100−8=192`.

Separating the real and imaginary tangent sectors gives45 independent real skew-orthogonal directions and `55+100−8=147` imaginary directions. Therefore the full tangent dimension is in **[192,196]**, with at most3 extra real and1 extra imaginary directions. The interval does not prove those extras exist, let alone integrate into an exact family. The author reports a rejected malformed v1 tangent file; my check used independently generated matrices byte-matching the corrected v2, not that rejected version.

## 8. Reviewer-written executable evidence and controls

All artifacts below are in the reviewer's own root. Commands are the ACTUAL completed runs; no author code was executed.

1. `frontier-20261028-f29-independent-witness-check-v1.py`, SHA256 `e30cf58d62ddba816feca6fa3c9a2448ab697392e103cc1e8865f6931bb8a50f`, run with the 12-ray input SHA256 `e64b0e90d6b0f908a07727de96f44bacf24a1abbf723b306de7e681189c05533`, 13-ray input SHA256 `0108335bbbe2d35214761904172490bbbed6976d59dd19748aaa7843276dc9e5`, and new own-root outputs. Receipt `frontier-20261028-f29-independent-witness-check-v1.json` SHA256 `75ec453bdb7c7a9d43297580287ef7672f205eb9be9ffd55fda1359d8237fdc5`. It checks Parker OA/source reconstruction, both original-vector/resolution definitions, Weisner pair graphs, and independently assembles the two tangent matrices.
2. `frontier-20261028-f29-pairwise-ray-controls-v1.py`, SHA256 `b73fab14a91175713ceb09a55313875f51935b57cd0f199eb34a676a97e05206`, separately evaluated ALL **4950** unordered ray pairs in each actual array via exact integer dot products. Receipt SHA256 `132de06507dc883cc282a461e35d60522f26f276ecd521ce0578054beac7f3e9`: **12/408** and **13/387** rays/parallel-pairs. Incrementing one coordinate was rejected for norm, and repeating a row label for `label-row`, the intended reasons. The first checker groups exact canonical rays, so its `pairwise_ray_checks:4950` field should be read as the number of pairs CLASSIFIED by canonical grouping, not as 4950 directly computed pairwise dot products; this second checker does the direct computations.
3. `frontier-20261028-f29-modrank-independent-v1.cpp`, SHA256 `f57bbd34f34cbc3d5fce8fa653fb34651f98dec1fc18bfe7c1587b90f3d1cc76`, compiled with `clang++ -O3 -std=c++17` to binary SHA256 `dec2d047afeadace2ffa76581d4f3a6b371c34b79673a9afba9da9940e4babf0`. The two actual runs over65521 returned exactly the ranks/nullities in §7. Its separate 3×4 calibration matrix SHA256 `26f0be81b0f069bd4260a81c5c9053b6aa4d1d05e72cb73f222181e95b580c38` returned rank2/nullity2; composite modulus15 was rejected with `ERROR: modulus is not prime`.

These are separate same-harness implementations and exact computations, not a formal proof, independent configured-family review or complete mutation campaign. The original p-group/project sources and status/priority questions are not imported into this physics proof.

## 9. Final boundaries

The all-n theorem is for the fixed classical OLS-derived labelled reference and fixed resolution; its converse gives a genuine nearby non-gauge family only when an associated pair graph is disconnected. Weisner's particular pair is locally rigid; Parker's two actual nonclassical arrays have 12 and13 rays, not100. The 13-ray tangent interval is an upper/lower bound, not an integrability result. No original global existence/nonexistence, current source status or novelty claim follows.

All earlier author/reviewer/parent historical records remain historical; this review neither repairs nor retrospectively validates held outcomes. No author contact, external-model/paid API, nested agent, secret, Git/push/publication, deletion or infrastructure change occurred. The reviewer now returns this duty and resumes the original AME research.
