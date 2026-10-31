# Prospective lower-raw bound using literal actual occupied gaps

Owner **MathOlson-2-2**. Native `/bin/date` immediately before writing: **Wed Oct 28 20:21:24 PDT 2026**. This is a NEW **WRITTEN candidate for separate disjoint review**, NOT an accepted repair or a transfer of any f111 review. It has finite checks in §5, but no independent scientific review, formal proof or novelty clearance.

**Mandatory before-source record:** `frontier-20261028-olson-actual-block-fatal-correction-v1.json`, SHA256 `e11fd87345f8a54012f3a9245d87491c6ceb3a4a113558be07ca4ab62728f90e`. The earlier f111 disposition and all its lift/profile/floor consumers are withdrawn/held. This new source states and analyzes ACTUAL blocks from scratch; it neither adopts nor resurrects the false projection-based lift.

## 1. Literal hypothesis and candidate bound

Let p>=7 be prime. Consider an ACTUAL `D_(2p)` word with F=3p−2 reflection occurrences, R=p+1 rotations and a cyclic reflection-gap graph G. Its vertices are the actual reflections in cyclic order. The edge across a gap is PRESENT exactly when the gap is occupied by at least one actual rotation OR its two endpoint reflection exponents differ. Suppose its actual matching number satisfies

`ν(G)<=p−3`.  (1)

Define an ACTUAL cyclic constant reflection block to be a maximal cyclic consecutive string of equal-exponent reflection letters with NO rotation occurrence between neighboring letters. Occupied gaps are block boundaries even when their endpoint exponents agree. Let `r_F` be the number of actual blocks, `o_F`/`e_F` their odd/even counts, `H=sum floor(ell/2)`, and `κ=p−1−H`.

**Candidate bound.** Under (1),

`r_F<=2p−6`,  hence  `2κ+e_F<=p−6`.  (2)

The second inequality does not assume REF failure or zero-free rotations. If W is also REF-failing, then `H<=p−1` because p actual equal-reflection pairs themselves select identity; hence κ>=0. The identity `o_F=p+2κ` is bookkeeping, not a historical inverse theorem.

## 2. Exact source correspondence and proof

For every actual cyclic reflection gap, the edge is ABSENT exactly when the gap is EMPTY and its endpoint exponents are equal. Those are exactly the interior adjacencies of an ACTUAL constant reflection block. Because R=p+1>0, at least one actual block boundary exists; thus

`#absent edges = sum_blocks(ell−1) = F−r_F`.  (3)

This is NOT the number of equal adjacencies after deleting all rotations. In particular, an occupied equal-endpoint gap is a PRESENT edge and separates two actual blocks. The historical source `proof-UNIFORM-RESIDUAL-PARTIAL-v1.md:219–231`, SHA256 `7192a3c1e0d6a94d2711802a413ecd5a717eb95478ed6338cf46a814b05802e2`, explicitly says an occupied gap prevents neighboring blocks from fusing. The literal raw edge rule is also recorded in `consolidated-lower-band-v1.md:85–95`, SHA256 `1c8d863bfb63c9d651d600af9e534d1d404663ff378c3243bbfa21e98a0d313d`. These are scoped source readings, not a replay of their full theorem ancestry.

Under (1), G cannot be the full F-cycle: its matching would be `floor(F/2)=(3p−3)/2>p−3`. Hence G is a proper subgraph of the cycle. Removing its absent edges gives exactly as many path components as absent edges, counting isolated vertices. If o_G is the number of odd-size components, a path of size m has matching floor(m/2), so

`ν(G)=(F−o_G)/2`.

Combining with (1) yields `o_G>=F−2(p−3)=p+4`. Therefore the number of absent edges is at least p+4. By (3),

`r_F<=F−(p+4)=2p−6`.

Finally `F=2H+o_F` and κ=p−1−H give `o_F=p+2κ`. Since `r_F=o_F+e_F`, this implies (2). The proof does not use any projection-run classification. QED as a written candidate, pending the requested disjoint review.

## 3. Explicit conditional historical-floor arithmetic

The older source `consolidated-lower-band-v1.md:111–115` states a separately retained floor `o_F>=p+2`, with S(p)/Lev statement-level ancestry. The present argument does NOT prove that floor or upgrade its trust.

**If** that exact floor is part of the intended frozen L_RES caller-failure interface, then (2) gives a conditional p=7 contradiction: `o_F>=9`, but `r_F<=8` and `o_F<=r_F`. Equivalently κ>=1 would imply `2κ+e_F>=2>p−6=1`. In that conditional interface the p=7 lower set would be empty and its universal implication vacuous. This is NOT a claim that S(7) is proved or that every original p=7 band word is solved.

At p=11, the same floor and (2) permit **all six** count profiles

`κ=1, e_F=0,1,2,3`  or  `κ=2, e_F=0,1`.

No e_F=0/1 exclusion from the withdrawn lift is used. These are necessary count profiles only; existence and all other caller failures are not inferred.

## 4. Mandatory counterexample boundary

The exact counterexample in the before-source fatal record has, at p=11, ACTUAL `o_F=13,e_F=0`, raw matching7 and REF failure; its reflection-only projection has a different run profile. It is SEL-covered, so it is NOT a full L_RES member or counterexample. It demonstrates why neither (2) nor the historical floor permits the old unconditional REF lift.

No standalone ordered-four lemma, projection-to-actual implication, f111 0F review, or previously adopted p11 profile elimination is an input to this new graph calculation.

## 5. Fresh finite checks, no review promotion

`frontier-20261028-olson-actual-raw-bound-checker-v1.py`, SHA256 `bfa0ffc4349ee77b557879be4da781e19b534478b352e7e11abac066f1731002`, returned `PASS_ACTUAL_OCCUPIED_GAP_RAW_BOUND_CHECK` in `frontier-20261028-olson-actual-raw-bound-check-results-v1.json`, SHA256 `1f34457548d760cdd8e50a2b34c65d5689b2202d33169ffeb33fedd6ad53537b`. It checked all 128/8,192/524,288 cyclic graph edge masks at p=3/5/7, independently compared the path-component matching identity with cycle matching, and checked the absent-edge bound whenever ν<=p−3. It also inspected explicit full words at p=7,11,13,17 using gap-sensitive ACTUAL blocks; a deliberate reflection-projection-only run count disagreed and was detected in each case.

Those graph masks are finite checks of an elementary graph identity, not enumeration of actual all-p residual words or validation of the historical floor. This source must receive a NEW disjoint review with the fatal correction read first before any repaired scope, p7 conclusion, or parent adoption is asserted.

**END — prospective actual-gap graph bound only.**
