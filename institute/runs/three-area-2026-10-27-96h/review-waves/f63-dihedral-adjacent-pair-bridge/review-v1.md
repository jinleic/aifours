# f63 dihedral adjacent-pair bridge — same-harness review v1

Observed native clock before writing this review: **2026-10-28T18:01:23-0700 PDT**. This is an observation before creation, not a claimed file-creation timestamp.

## Disposition and exact scope

**SUPPORTED at the stated scope:** for every odd prime `p`, in an actual ordered `D_(2p)` word with length `4p−1`, exactly `3p−3` rotations and `p+2` reflections, the first input's no-selector core reduction and stated long-reflection-run conclusions follow; and the successor's original-order length-`2p` identity selector follows if there are two disjoint actual adjacent reflection pairs. The pairs may abut each other or be separated. One adjacent pair imposes the stated stronger necessary form under a hypothetical no-selector assumption. The p=3, b=0 and b=−a cases are included without division by b or a+b.

**FATAL: 0. MAJOR: 0. MINOR: 3**, plus one explicitly disclosed correction to this reviewer's own receipt below. The minor points do not invalidate the stated theorems.

The conclusion is **not** that every word in this count band for every odd prime has a selector. The p=3 concentrated core was exhaustively checked separately; the general residual is stated below. This is a same-harness mathematical reconstruction with a finite independently written exact check: no independent-family or external-model review, human refereeing, formal/kernel certification, priority/novelty determination, other dihedral count-band theorem, or original all-finite-groups Olson conclusion is claimed.

## Frozen inputs and reading order

Manifest `manifest-v1.json`, SHA256 `f4634edcc78ee637a1c73d95f12390b8dee7e301415a536d7c20cb0b448077ed`, was read first. The two entire author inputs were then read in the manifest's order, after their whole-file hashes were checked:

1. `frontier-20261028-dihedral-core-and-four-reflections-v1.md`: SHA256 `5e7f65b8764d4f52ccddadd9ea2934d0635ca5c2085a3c41e520b336a93c767f`, 10,495 bytes, 82 LF. Called **A** below.
2. `frontier-20261028-dihedral-two-adjacent-pairs-v1.md`: SHA256 `fc4b420c2d4f66b2be06640dec5a161567fa35c4024e626653c15d8f29e8e363`, 8,303 bytes, 64 LF. Called **B** below.

Their location is `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/ordered-olson/`. Line references below address these exact pinned files. No earlier held source is used as a premise.

## Findings

1. **MINOR — qualify the word “necessary” in A:70.** The displayed example establishes that a construction restricted to *two reflections selected from that all-equal run* fails, while four from it work. It does not establish that every such word can be solved only by four reflections, nor logical uniqueness of this proof method. Concrete p=3 actual word, with `r^3=s^2=1` and `srs=r^−1`: `[r,r,r,r,r] [s,s,s,s] [r^2] [rs]`. It has 6 rotations, 5 reflections, length 11 and a maximal all-equal run of 4 reflections. Selecting original 1-based indices `1,2,3,4,6,11` gives `r^4 s(rs)=r^(4−1)=1` with **two** reflections, one outside the run. This does not contradict A:70's specific restriction to pairs *from the run*. Recommend “necessary for the two-from-that-run construction” rather than unqualified necessity.
2. **MINOR — the historical strict-separation assertions in B:54 are not fully independently auditable from these two pinned inputs.** The exact definitions of the earlier fixed-I, same-gap, saturated separated-packet and short-run certificates and their strict inequalities are not provided here. I independently checked the corrected family's relevant actual counts, supports, and odd-run counts and its four-reflection selector; these are consistent with the quoted numerical features. They do not themselves establish all claims about those unpinned certificates. No such earlier certificate is needed for the proof of B:7. Treat the larger historical separation statement as unverified, not as a theorem premise or novelty finding.
3. **MINOR — make the three-reflection implication at B:36 explicit.** Equation (1) was stated for adjacent pairs; the first and third reflections of a length-3 run are not adjacent. The same derivation nevertheless applies to any two reflections with **no rotation between them**, since the middle reflection can be skipped. Thus all three directed differences equal `−(a+b)`; the two adjacent differences add to the first-to-third difference, forcing that common value to zero and hence `b=−a`. Alternatively A:62–68 already proves the same consequence. This is an exposition gap with a direct repair, not a missing mathematical step after reconstruction.

**Own-receipt correction, not an author finding.** The receipt key `also_bruteforced_all_6_index_subsets_for` is too strong: for 3,278 sampled p=3 words, `next(...)` searches original 6-index combinations only **until the first identity**; it does not enumerate all 462 combinations when it finds one. The actual DP witness for **each** of all 449,064 normalized core words was separately multiplied in original order. The v1 source and receipt are preserved unchanged; this paragraph is the additive correction.

## Independent reconstruction

Use the actual multiplication `(x,e)(z,f)=(x+(−1)^e z,e+f mod 2)` for `r^x s^e`. In particular, if the only selected reflections occur at original positions `i<j` with exponents `y_i,y_j`, the final reflection parity is even and the exponent is

`sum(rotations outside (i,j)) − sum(rotations inside (i,j)) + y_i − y_j`.

No selected rotation is moved, and unselected reflections do not change the parity of the selected subsequence.

### Signed-pair selector and majority

For fixed i<j, sign each of the actual `3p−3` rotations according to that interval. If its maximum signed-value multiplicity is at most `2p−2`, there are `p−1` disjoint unequal signed pairs: the largest part has at most `n−(p−1)` entries and `n=3p−3` has at least `2(p−1)` entries. Equivalently, the complete multipartite matching maximum is `min(floor(n/2),n−M)`. Omit one from each pair, retain one from each pair and all `p−1` unpaired rotations: the retained count is `(p−1)+(p−1)=2p−2`. For each pair a swap changes the exponent by a nonzero residue. Starting from `{0}`, each of the `p−1` independent swap differences grows the reachable set unless it is already the whole field; a nonempty proper subset cannot be invariant under a nonzero translate of the prime cyclic group. Thus all p targets are reached. Adding the two actual reflections yields a length-`2p` identity selector.

Consequently, under no selector every reflection pair has a unique signed majority of at least `2p−1`. A zero majority supplies `2p−1` actual zero rotations; among `p+2` reflections two exponents coincide, and those two with any `2p−2` zero rotations select identity. Thus each majority is nonzero. Choose one majority h. Its class and any other pair's majority class overlap in at least `2(2p−1)−(3p−3)=p+1` actual rotation occurrences; any common raw rotation exponent belongs to both `{h,−h}` and `{h',−h'}`. Therefore every pair's majority is one of `±h` (A:20–28).

### Concentration, signs, and forbidden core gaps

Let `a∈{h,−h}` be the raw sign with `m≥p` occurrences; let `n` be the number of raw `−a` occurrences. The signs are distinct because p is odd. If `m≥2p`, `2p` copies alone select identity; if `n≥p`, then p copies each of a and −a do. Hence `p≤m≤2p−1` and `n≤p−1`.

For each reflection interval write `u=(#a inside)−(#−a inside)`. The signed multiplicities are exactly `m−u` and `n+u`, so the majority condition gives `u≤m−(2p−1)≤0` or `u≥2p−1−n≥p`. There are `p+1` intervals between consecutive reflections. At most one can have positive u, because each requires at least p actual a's and `m≤2p−1`; at most n≤p−1 can have negative u, because each contains at least one actual −a. At least one interval has u=0. Its nonzero majority must be +a, forcing `m=2p−1`; the number of extra rotations is `(3p−3)−(2p−1)=p−2`.

For a reflection pair with c core occurrences inside, `c=p−1` or p leaves at least `p−1` core occurrences **both** inside and outside. Pair an inside `−a` with an outside `+a` for each of `p−1` disjoint pairs and run the same swap argument. Thus both central counts are forbidden under no selector (A:30–44).

### Zero-sum-free extras and the equality lemma

Put the p−2 extra exponents `b_i`, `d_i=b_i−a`. If a nonempty k-subset of the d_i sums to zero, select those k actual extras and `2p−k` actual cores; `1≤k≤p−2` makes the required core count at most `2p−1`, and the exponent is `sum b_i+(2p−k)a=sum d_i=0`. Hence the d_i are nonzero and zero-sum-free.

For their subset-sum set A, translation growth yields `|A|≥p−1`. If `A=F_p\{m}`, fix i and let B be the subset sums of the other `p−3` entries. Since `B⊆A`, `B+d_i⊆A` and `|B|≥p−2`, the case `|B|=p−1` would imply `B=A=B+d_i`, impossible for nonzero d_i. Therefore `|B|=p−2` and its complement is precisely `{m,m−d_i}`. Zero-sum-freeness gives `−d_i∉B`; hence `−d_i=m` or `m−d_i`. The latter makes `m=0`, impossible because `0∈A`. Thus every `d_i=−m`. For p=3 the other sequence is empty and `B={0}`, so the proof still works (A:46–58).

### Actual long runs and the one-pair condition

In a contiguous reflection run H, every rotation lies outside H. For a k-subset S of extras, selecting it with `2p−2−k` actual cores is always feasible, including k=0. Its exponent is `−2a+sum_(i∈S)d_i`. Two selected reflections `r^y s,r^z s`, in that order, therefore yield identity exactly when `z−y∈T=−2a+A`.

If a no-selector H has at least three reflections, T cannot be all of F_p, and all three directed pair differences must equal its one missing value w. As the adjacent differences add to the first-to-third difference, w=0; all reflections of the run are equal. The missing A-residue is then `m=2a`, the equality lemma gives `d_i=−2a`, and every extra is `b_i=−a`. If H has four reflections, select any four from H, `p−2` actual cores and all `p−2` extras. This uses exactly `4+2(p−2)=2p` occurrences, each selected rotation is outside H, the rotation exponent is zero, and the four equal reflections give identity. Thus the no-selector assumption fails. The nonconstant three-run theorem follows from the same reasoning.

For even one adjacent pair, the same T argument forces A to miss one m and all extras to be the single `b=a−m`, with `b≠a`. For each adjacent pair `(y,z)` the only unavailable target is `z−y=−2a+m=−a−b`. The same m is global, not pair-dependent. As noted in finding 3, the same formula holds for any two reflections with no intervening rotation, even if unselected reflections lie between them (B:18–28).

### Two actual adjacent pairs, including exceptional boundaries

Take actual disjoint pairs `(y1,z1)` and `(y2,z2)`, each adjacent in the original word, and select `p−2` cores plus all `p−2` extras. These are `2p−4` rotations, leaving exactly four selected reflection occurrences and total length `2p`. Each pair contributes `y−z=a+b`; the rotation exponent is `(p−2)(a+b)=−2(a+b)`. Inside each selected pair there is no rotation; before the first pair, between the two pairs, and after the second, the number of selected reflections already passed is 0, 2, or 4, respectively. Therefore all selected rotations enter with **positive** sign in their actual order, and the total exponent is `−2(a+b)+2(a+b)=0`. Reflection parity is even. This remains valid if the pairs are contiguous or separated by rotations and/or skipped reflections.

At p=3 the choice is one core, one extra and four reflections. For a=1, b=0, each pair has `z−y=2`, so the selected rotation sum 1 plus two pair contributions 1+1 is 0 mod 3. For a=1, b=−a=2, each pair has equal exponents, the chosen rotations sum to 0 and each pair contributes 0. The general proof uses no inversion of b or a+b (B:30–36).

## Corrected illustrative family and first diagnostic

For B:46–52, the word has `2p−1` cores, `p−2` inverse extras and `2+3+(p−3)=p+2` equal reflections. Its reflection-run lengths are `2,3,1,...,1`, and selecting `p−2` cores, all `p−2` inverse extras and the first two reflections in each of the first two runs gives the actual length-`2p` identity. All cores precede all reflections. For any two reflection positions the signed rotation list contains at least `2p−1` values +1 and at most `p−2` values −1, so the preceding signed-majority sufficient condition does not apply. If exactly `2p−2` signed rotations are chosen and q of them are −1, their exponent is `2p−2−2q=−2(q+1)`, with `0≤q≤p−2`; this is never 0 mod odd p. The equal reflection exponents add no correction. Thus this family genuinely needs something beyond any two-reflection selector, but it is **not** a counterexample or an avoiding-word family.

B:60 reports that the first proposed diagnostic actually failed with `ValueError: prior signed-pair test unexpectedly qualifies` and produced no result file. That is a failed strict-separation example, not a disproof of the theorem or a failed corrected proof. I did not open or rerun that separate unpinned first checker. My own independently constructed variants at p=5,7 place exactly one core rotation between the tested reflections; their signed maxima are respectively 8 and 12, exactly `2p−2`, and the checker constructs and directly multiplies actual identity witnesses. This demonstrates the reported failure mechanism, not byte-level replay of the historical first file.

## Bounded independent checks and controls

Fresh stdlib-only source `checker-v1.py`, SHA256 `c281e379c2794ea3e3fe7f4a2e6f40e424620e598b79a2816883f613c29678c6`, was run as `python3 -B checker-v1.py`. Receipt `checker-receipt-v1.json`, SHA256 `d2e432a8e6ce6ce89d5ee950cd5860484cc2317a6c22e6eb5d8b5c5db7343323`, reports `PASS_BOUNDED_CHECKS` and clock `2026-10-28T18:00:37-0700 PDT` before receipt creation. The checker uses no author code.

* Exact nonzero tuples of length p−2 for p=3,5,7: respectively `2,64,7776` tuples; `2,16,36` zero-sum-free; `2,4,6` one-missing cases. All one-missing cases satisfy the equality lemma, including every omitted-entry complement; the other zero-sum-free cases have full A.
* All signed multiplicity vectors for p=3,5,7 were checked: `28,1820,134596` vectors in total, with `19,1645,131362` eligible under the maximum-multiplicity bound; greedy unequal pairing and all-field swap reachability succeeded in each eligible vector.
* Forty seeded actual words per p=3,5,7 gave `371,840,1440` eligible reflection pairs, respectively; for **every eligible pair**, the checker constructed actual retained original indices and directly multiplied the selected word to identity. The p=3 sample also contained 29 ineligible pairs; absence of eligibility is not a failure of the theorem.
* The explicit conditional four-reflection selector was directly multiplied for `468,5200,22932` actual configurations at p=3,5,7, respectively. These cover all nonzero a, every b≠a, all y1,y2, b=0 and b=−a, and both contiguous and genuinely separated pairs across the coded placements of selected rotations. They do not exhaust all possible arrangements for p>3.
* At p=5,7,11,13, the corrected illustrative family was constructed and directly multiplied. All `21,36,78,105` reflection pairs respectively were checked for the signed-majority condition and two-reflection exponent support, and the exact run/odd-type counts were checked.
* For p=3, after automorphically normalizing the nonzero core exponent to 1 and the first reflection exponent to 0, **all 449,064** actual words with five core rotations, one extra b∈{0,2}, and five reflections were traversed by left-to-right length/parity/exponent DP. Every returned 6-index witness was then directly multiplied in original order: zero no-selector words occurred. A further 3,278 deterministic samples were searched by original index combinations until finding identity; see the own-receipt correction above. This finite check, together with the independently reconstructed core reduction and the normalization automorphisms `r↦r^u`, `s↦r^v s`, supports the whole **p=3 instance of this one count band** at computer-assisted bounded-check level; it is not a written all-prime closure.
* Intended-reason negative controls: replacing a selected reflection by an unused rotation was rejected specifically as `REFLECTION_PARITY`; altering one selected reflection exponent as `NONZERO_EXPONENT`; and duplicating an actual index as `INDEX_ORDER_OR_DUPLICATE`. Two additional concrete correct-identity words show that the all-plus crossing-sign mutant and the reversed `y−z` mutant each predict nonzero exponent 2 instead of actual exponent 0. These are sign-sensitive controls, not arbitrary exceptions.

## Remaining frontier and limits

For an all-prime hypothetical avoiding word in this band, the core is `2p−1` copies of a nonzero a, the p−2 translated extras are zero-sum-free, and no reflection pair crosses `p−1` or p core occurrences. At most one actual reflection run has length greater than one; if it exists, its length is 2 or 3. In the one-pair branch all extras are the same b≠a and every adjacent directed difference is `−a−b`; the length-3 branch further forces b=−a and all three exponents equal. The no-adjacent-pair branch remains as a general-p possibility, not a constructed counterexample. The core-gap argument requires at least two extras in that branch, so it is impossible under the no-selector hypothesis at p=3; the separate finite normalized p=3 check rules out the remaining concentrated p=3 configurations as described above. For general odd primes, these are necessary conditions only, not a proof that an avoiding word exists or that the entire count band is closed.

Other count bands, arbitrary finite groups, previous-certificate applicability beyond the stated checks, historical/priority claims, and the independent-family, human and formal gates remain outside this review. No author contact, external-model CLI, paid call or publication was performed.
