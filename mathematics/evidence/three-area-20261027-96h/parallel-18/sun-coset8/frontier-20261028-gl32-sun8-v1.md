# Sun8 for GL3(2): a finite subgroup-and-coset certificate

**Status: WRITTEN-checked-in-kernel, UNREVIEWED.** This candidate proves the Sun8 index conclusion for the actual simple group GL3(2)≅PSL3(2): among eight pairwise disjoint left cosets of finite-index subgroups, some two subgroup indices have gcd at least 8. It does not use the false universal seven-index exclusion: this group has seven distinct point stabilizers of index 7 and seven disjoint cosets which partition it. No eight-coset counterexample, formal verification, human/independent review, priority claim, all-simple or arbitrary-group theorem is asserted.

Before affected prior candidate bodies, read the complete pre-source overlays in order: `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` SHA `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`, `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` SHA `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04`, then `frontier-20261028-alternating-p7-cardinality-addendum-v1.json` SHA `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218`. No earlier source, process disposition or hold is changed. This proof uses no Jordan/Jones, Sun7, R8 or public classification theorem; it uses elementary group theory plus the exact finite matrix checks below. The author's incidental nonblind cross-topic display remains disclosed and unused.

## 1. The exact group and finite certificate

Let G be the invertible 3×3 matrices over F2. It has 168 elements by the ordered-basis count (8−1)(8−2)(8−4). The prior author checker `frontier-20261028-gl32-index7-check-v1.py` SHA `de3d309fa78f46c971604b9fd8d6c38a5b678f3cb61fc5a07552b2f4663d6d64`, 62 LF / 2474 bytes, computed conjugacy classes of sizes 1,21,24,24,42,56 and checked that no identity-containing nontrivial proper class sum divides 168. Since a normal subgroup is a union of conjugacy classes and its order divides 168, this is an author-only exact computation showing G is simple. Its validity is an explicit input to the following subgroup-completeness proof, not an independently verified fact.

The separate author checker `frontier-20261028-gl32-sun8-check-v1.py` SHA `26487887979926b48033ecb36caf393a15063578a06eec641f685acf62925c37`, 111 LF / 3860 bytes, was executed in the author's Python eval kernel before 20:52:24 PDT on 2026-10-28. It established the following finite claims using integer bit operations only:

1. All subgroups of order at most 24 were generated; the counts by order are 1:1, 2:21, 3:28, 4:35, 6:28, 7:8, 8:21, 12:14, 21:8, 24:14.
2. The 14 subgroups of order 24 have exactly 98 distinct left cosets of size 24. Among these cosets there are exactly 1568 unordered six-tuples of pairwise disjoint sets, and the complement of **every** such six-tuple is another coset in those 98.
3. The divisors of 168 which are at least 8 are partitioned into `[8,21,168]`, `[12,24,84]`, `[14,28,42,56]`. Inside each class every pair has gcd either 1 or greater than 7. A duplicate-coset count control is also checked.

For claim 1, the checker starts with the trivial subgroup and repeatedly adjoins each element, retaining generated groups of size at most 24. This is exhaustive for such subgroups: any subgroup of order at most 24 can be built by adjoining its elements, and every intermediate subgroup remains inside it. Generated subgroups are computed by finite closure under right multiplication; in a finite group the generated monoid is the generated subgroup. The six-tuple checker enumerates increasing indices in the complete 98-coset list and verifies complement membership at every leaf, not a sample. These are author checks of the displayed algorithms, not independent replay, a human proof or a formal certificate.

## 2. Why all proper subgroups are covered

For any proper H<G, the coset action is faithful because G is simple. If [G:H]<7, G would embed in S_m for m<7, but 7 divides 168 and does not divide m!, a contradiction. Thus every proper subgroup has order at most 24. The author subgroup enumeration therefore covers every proper subgroup, conditional on the preceding simplicity computation and enumeration's correctness.

Two left cosets of coprime-index subgroups must intersect: the index of the intersection of the subgroups is divisible by both indices and at most their product, hence equals their product, so the subgroup product is G. Assume for contradiction that eight left cosets are pairwise disjoint and their subgroup indices have all pairwise gcd≤7. Then all pairwise gcds are in 2,…,7, and all subgroups are proper. Let b count the indices equal to 7.

## 3. The repeated-index cases

If b=0, every index is at least 8, so equal indices cannot occur. All indices divide 168 and belong to the three color classes in Section 1. Since an edge in the index-gcd graph joins any two of our distinct indices, there can be at most one index in each class, hence at most three cosets.

If 1≤b≤5, every other index has gcd 7 with an index-7 subgroup, hence is 7a with a>1. These a values divide 168/7=24 and are pairwise coprime. Since 24 has only the prime divisors 2 and 3, at most two such indices occur. Therefore the whole collection has at most b+2≤7 cosets.

If b=7, the seven disjoint index-7 cosets already cover G, and b>7 is impossible by counting. If b=6, Section 1 says their complement is a single left coset F of an index-7 subgroup. Both remaining cosets must lie in F. Translate F to its subgroup K: the remaining sets become left cosets of subgroups of K, with relative indices a and a', and the ambient indices are 7a and 7a'. Their ambient gcd must be exactly 7, so gcd(a,a')=1; the coprime-index lemma then makes the two relative cosets intersect, contradiction. This exhausts all cases and proves the stated Sun8 candidate.

## 4. Review boundary

The exact computation is intentionally finite and fully specified; it is not an all-variable proof for any other family. A reviewer must independently reconstruct the group and subgroup lattice without importing either author checker, verify the normal-class simplicity step, all 14 index-7 subgroups and 98 cosets, and the 1568 six-coset complements, and mutation-check completeness. The named checker output is one author run only. The earlier A7 parent check and this candidate do not license an eight-coset P7 implication, global claim, novelty statement or historical-hold rehabilitation.
