# Ordered dihedral selector at `R=3p−2`

Owner **MathOlson-2-2**. Native `/bin/date` immediately before this write: **Wed Oct 28 18:20:29 PDT 2026**. This is a self-contained **WRITTEN theorem candidate**, plus bounded exact checks below. It has not received an independent review, formal proof, novelty determination or global-adoption verdict.

## 1. The theorem and scope

Let p be ANY odd prime and let W be an ACTUAL original-order word of length `4p−1` in

`D_(2p)=<r,s | r^p=s^2=1, srs=r^(-1)>`.

If W has exactly `3p−2` rotation occurrences, and hence exactly `p+1` reflection occurrences, then W has an identity-product subsequence of EXACTLY `2p` original occurrences in increasing index order.

This is the `R=3p−2` count band only. It does not rely on, establish or review the separate `R=3p−3` candidate, any other rotation-count band, L_RES, arbitrary finite groups, or a novelty claim.

## 2. Fixed-pair selector lemma

Fix two ACTUAL reflection positions i<j with exponents y_i,y_j. Sign each rotation exponent by +1 outside their interval and −1 strictly inside. If this signed multiset has maximum multiplicity `M<=2p−1`, the word has an identity selector using these specified two reflections and exactly `2p−2` actual rotations.

Indeed, `R−M>=p−1` and `floor(R/2)>=p−1`, so there are p−1 disjoint pairs of unequal signed values. Elementary proof of the pairing count: repeatedly pair occurrences from two largest value piles; after each step `min(floor(N/2),N−M)` drops by at most one. If its maximum does not drop, at least three piles shared it, which supplies the needed slack. There are `R−2(p−1)=p` actual rotations outside these pairs; fix ONE of them as an additional omission. Omit one member of each pair as well, for exactly p omitted rotations. Every independent swap changes the omission sum by a nonzero element of F_p, and any nonempty proper subset of F_p strictly grows upon union with a nonzero translate. Thus the p−1 swaps make all p omission sums available.

The actual original-order selected product is

`r^[ sum(selected signed rotation exponents) + y_i−y_j ]`.

Choose the attainable omission sum that makes this exponent zero. This retains exactly `R−p=2p−2` rotations plus the specified reflections, using actual distinct original indices.

## 3. Every hypothetical avoiding word has a globally aligned majority

Assume for contradiction there is NO original identity selector of length2p. The lemma forces the signed multiset for EVERY reflection pair to have a unique value of multiplicity at least2p. It cannot be zero: that would give 2p actual zero-exponent rotations, an all-rotation identity selector.

Fix one reflection pair and its nonzero majority h. At least2p raw rotation exponents lie in `{h,−h}`. The majority classes for any two pairs intersect in at least `4p−(3p−2)=p+2` actual rotation occurrences. At a shared occurrence the two signed majority values are each ± the same nonzero raw exponent. Therefore every signed majority is h or −h.

Orient h as a so that m=#raw `r^a` rotations is at least p. If m>=2p, select 2p of them; if at least p raw `r^(−a)` rotations also occur, select p of each. Thus, under no-selector, with n=#raw −a rotations,

`p<=m<=2p−1`,  `n<=p−1`.  (1)

## 4. Count EVERY consecutive reflection gap

For ANY actual reflection pair i<j, let

`u_ij = #(raw a rotations strictly between) − #(raw −a rotations strictly between)`.

The signed multiplicities of +a and −a are respectively `m−u_ij` and `n+u_ij`. Since the unique signed majority must be ±a and has at least2p occurrences,

`u_ij <= m−2p <= −1`   OR   `u_ij >= 2p−n >= p+1`.  (2)

There are p+1 reflections and hence exactly p gaps between CONSECUTIVE reflections. Every one has nonzero u by (2).

* A gap with positive u contains at least p+1 actual a-rotations. There is at most ONE such gap, since `m<=2p−1`.
* A gap with negative u contains at least one actual −a rotation. There are at most n<=p−1 such gaps.

The p gaps must be covered. Consequently there is exactly one positive gap and exactly p−1 negative gaps, n=p−1, and each of those negative gaps contains exactly one of the p−1 raw −a occurrences. In particular ALL raw −a occurrences lie between the first and last reflections. The one positive gap contains at least p+1 raw a occurrences, likewise between those endpoints. Other rotation values, if any, are not assumed absent and do not affect this counting argument.

## 5. The endpoint pair gives the contradiction

For the ACTUAL first and last reflections, every one of the p−1 inside raw −a rotations becomes a signed +a occurrence. At least p+1 inside raw a rotations become signed −a occurrences. Thus their signed multiset contains at least p−1 of each of the two different values +a and −a.

Pair p−1 actual signed +a occurrences with p−1 actual signed −a occurrences. There are p other original rotations outside these pairs; fix one as the further omission. The same p−1 independent nonzero swaps as in §2 cover F_p, giving the EXACT `2p−2` rotation count and making the endpoint reflection product identity. This is a selector in W, contradicting the assumption.

The argument does not need to locate or select an earlier all-rotation witness, to assume a positive/negative gap has no other rotation value, or to couple different reflection anchors by an unproved joint-affinity claim. QED.

## 6. Explicit actual family with NO eligible consecutive pair

For every odd prime p, choose arbitrary `y_0,...,y_p∈F_p` and concatenate the original occurrences

`[p−2 copies r] · r^(y_0)s · [p+1 copies r] · r^(y_1)s · product_(j=2)^p ( r^(−1) · r^(y_j)s )`.

There are `2p−1` raw +1 and p−1 raw −1 rotations, for total3p−2, and p+1 reflections. This expression is ordered concatenation, not a group-power simplification.

For the first consecutive reflection pair, the p+1 intervening +1 rotations flip to −1 and combine with the p−1 −1 rotations outside, producing a signed −1 multiplicity 2p. For each later consecutive pair, exactly one −1 rotation flips to +1 and combines with the 2p−1 +1 rotations outside, producing signed +1 multiplicity 2p. Therefore EVERY consecutive pair fails the fixed-pair lemma's `M<=2p−1` condition.

For the first and last reflections, all p−1 −1 rotations are inside and flip to +1, the p−2 initial +1 rotations remain +1, and the p+1 central +1 rotations flip to −1. The signed multiplicities are `2p−3` and `p+1`, both at least p−1; hence the endpoint pair ALWAYS supports an actual length2p identity selector, for arbitrary reflection exponents. This exhibits an actual separated-gap coupling, not an avoiding family or a novelty claim.

## 7. Exact bounded checks, no global inference

`frontier-20261028-dihedral-r3p-minus2-experiment.py`, SHA256 `83244cb962bc5b3b4ba62f5c5d6615e9d04b2c28b035ece2952b29a07929d3e1`, generated 480 actual full words at p=3,5,7,11 (120 each; uniform, biased or constant rotation values), with seed2026102810. Saved data `frontier-20261028-dihedral-r3p-minus2-results.json`, SHA256 `4454ffa75eb2c62881fe761a9b5da2ee60859cc8423f6d3c072582f8104d90b8`.

An independently written checker `frontier-20261028-dihedral-r3p-minus2-checker.py`, SHA256 `3adbceff2de26c63ed4ad2279d95e9da27e0c9058befd8105b441cc63c3632e6`, imported no producer code and returned `PASS_INDEPENDENT_R3P_MINUS2_CHECK`; saved result `frontier-20261028-dihedral-r3p-minus2-check-results.json`, SHA256 `7dca4ccc7290b6c250fe8e617fceb2f66d00d0ad86a79889d09fd98b48da276b`. It reclassified ALL 13,800 actual reflection pairs and directly multiplied 10,147 qualifying selectors with distinct increasing original indices; the other 3,653 pairs were NOT decided by the fixed-pair sufficient condition. It also checked 100 actual §6-family words at p=3,5,7,11,13, independently confirming every consecutive pair ineligible and the endpoint eligible, and directly checked 680 qualifying original selectors across those words. Duplicate-index, reused-pair and inside-pair-fixed-omission mutations were rejected for their intended reasons.

These finite checks are diagnostic and do NOT independently establish the all-word counting contradiction, a formal proof, novelty, or any other count band. A disjoint full-source scientific review is requested.

**END — exact R=3p−2 band candidate and evidence.**
