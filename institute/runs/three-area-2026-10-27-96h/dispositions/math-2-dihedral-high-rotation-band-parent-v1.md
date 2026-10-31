# Ordered dihedral words: the entire R=3p−3 band

Native clock observed before writing: **2026-10-28T18:14:35-0700 PDT**. This is a same-harness written theorem at elementary finite-group/arithmetic facts, corroborated by exact bounded word checks. No novelty, human/cross-model review, formal verification, or general ordered-Olson solution is claimed.

## Exact statement

For **every odd prime p**, every actual word of length `4p−1` in `D_(2p)=<r,s | r^p=s²=1, srs=r^(−1)>` containing **exactly `3p−3` rotations and `p+2` reflections** has an identity-product subsequence of exactly `2p` distinct original occurrences, selected in increasing original index order.

This settles that one count band. The [original target](../written-releases/math-2-ordered-word-definitions-v1.md) quantifies over every finite group and every length-`2|G|−1` word; other dihedral count bands and that unrestricted question remain open at this scope. Reordering selected elements is not allowed or used.

## Complete inputs and repaired wording

The parent read the full [mandatory f63 overlay](/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/ordered-olson/frontier-20261028-dihedral-high-band-f63-overlay-v1.md) **before** the complete [125-LF high-band proof](/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/ordered-olson/frontier-20261028-dihedral-high-rotation-band-proof-v1.md), and then the full [f66 review](../review-waves/f66-dihedral-high-rotation-band/review-v1.md). Review verdict: **0 FATAL / 0 MAJOR / 2 MINOR**, both explicitly qualified here:

- A signed majority class has **at least** `L=2p−1` occurrences. In the intersection argument choose any L occurrences from each class; do not assert the whole classes have exactly L elements. Their intersection still has at least `p+1` elements.
- For an interior equal-reflection triple, select its first two actual adjacent members, or select first/third and explicitly skip the middle. In the latter case they are consecutive **among selected occurrences**, not in the original word; no rotation lies between them. Neither choice changes the product argument.

The before-source overlay's three earlier precision corrections and its finite-check count qualification carry forward. Historical certificate strict-separation claims are not premises, and a four-reflection construction is sufficient here, not globally necessary for every word.

## Parent reconstruction

For a fixed pair of chosen reflections, actual multiplication signs every rotation inside their original interval negatively and every rotation outside positively. If the largest multiplicity among these signed values is at most `2p−2`, select `p−1` disjoint unequal pairs. Omitting one of each from the full `3p−3` rotations leaves `2p−2`; the p−1 nonzero swap differences cover all residues in the prime cyclic group. One choice cancels the two-reflection exponent.

Thus a hypothetical no-selector word has a nonzero signed majority of at least `2p−1` for every reflection pair. The majority cannot be zero because more than p reflections give two equal exponents and the available zero rotations complete a selector. Intersecting chosen L-subsets of two majority classes forces all signed majorities to be one fixed pair of opposite nonzero residues. The consecutive-reflection interval count then forces **exactly L identical raw rotations** `a≠0`; otherwise all-rotation selectors or a zero-difference reflection interval contradict the majority requirement. The remaining `p−2` exponents `b_i` have zero-sum-free translates `b_i−a`.

For any two reflections with no rotation between, their possible `2p−2`-rotation sums are `−2a+A`, where A is the translated extras' subset-sum set. If no selector exists, A has exactly p−1 values. The elementary equality lemma then forces all translated extras equal: for each omitted term the remaining subset-sum complement has two residues, and zero-sum-freeness identifies the missing residue's negative with that term. Consequently two disjoint actual adjacent reflection pairs would already yield a four-reflection selector. There are at most two adjacent-reflection boundaries; if two, they overlap into one equal-exponent triple and all extras are `−a`.

Let g be the number of distinct core-prefix counts at reflections and A the number of actual adjacent-reflection boundaries. There are `F−g−A` core-free nonempty gaps, each consuming an extra. A positive-core gap either contains at least as many inverse extras as cores or contains at least `p+1` cores. At most one gap can be of the latter kind. If `g=1`, the extra budget forces `A≥3`, impossible. If `g≥2`, it forces `A≥2`, hence exactly two boundaries and the triple. Equality of the extra budget forces exactly one large core-only gap, exactly one extra in each other counted nonempty gap, and **no extras outside the endpoint reflections**.

For the first and last reflections, all `p−2` extras are therefore signed `+a` and at least `p+1` cores are signed `−a`. Any outside core would give `p−1` opposite pairs and a selector. Otherwise the possible `2p−2`-rotation sums are exactly the nonzero residues, so unequal endpoint exponents also yield a selector. If endpoints have equal exponents, choose `p−2` signed rotations of each sign, both endpoints and two further reflections from the equal triple. The inserted pair contributes identity when interior; if the triple contains an endpoint, its three equal reflections have that endpoint's original action. There are exactly `2p` selected occurrences and their original-order product is identity. This covers p=3 and both endpoint-overlap cases.

## Actual checks and limits

The parent independently implemented direct dihedral multiplication and constructed full actual words at p=3,5,7,11,13 with the endpoint/equal-triple/inverse-extra form. It selected first/third triple members, skipped the middle, verified exact length and increasing distinct indices, and obtained identity in each case. Changing the endpoint exponent made each submitted selector fail. These are five diagnostic scenarios, not the all-prime proof.

The f66 reviewer separately authored two checkers: [main checker](../review-waves/f66-dihedral-high-rotation-band/checker-v1.py) and [outside-core checker](../review-waves/f66-dihedral-high-rotation-band/outside-core-checker-v1.py). Its complete review records actual source/hash bindings, 1,892 saturated endpoint words, 1,200 outside-core words, 96 unrestricted sampled words, subset-sum checks and reason-sensitive mutation controls. None is represented as exhaustive over all p or all original words; the universal conclusion rests on the written contradiction and elementary prime-group facts above.
