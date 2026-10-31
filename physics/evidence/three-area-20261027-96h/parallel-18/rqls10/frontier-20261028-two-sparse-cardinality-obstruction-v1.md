# Universal cardinality obstruction for two-sparse resolvable quantum Latin arrays

**NEW WRITTEN AUTHOR CANDIDATE, unreviewed; exact original-object check on one example.** Native `/bin/date` before writing: **Wed Oct 28 17:28:55 PDT 2026**. This is a universal result over ALL resolution incidences but ONLY for arrays globally two-sparse in some common orthonormal basis. It is NOT an unrestricted QLS10 no-go and does not assume that a general target array can be put in such a basis.

## 1. Exact theorem and original target consequence

Fix n>=3 and an array of n² unit vectors in C^n. Suppose its cells have k>=2 parallel classes of n disjoint n-cell blocks, with every block an ONB and any two blocks from different classes intersecting in exactly one cell. Suppose that, in SOME ONE common orthonormal coordinate basis, **every** array vector has support size at most2. Let s be the number of one-support cells and t=n²-s the number of exactly-two-support cells. Let C be the number of distinct rays among ALL n² actual cells.

**Theorem.** Every exactly-two-support ray occurs in at least k distinct cells, and

`C <= min(n,s)+floor(t/k) <= n+floor(n(n-1)/k)`.                    (1)

For the original 1-resolvable QLS(10), take its row, column and disjoint transversal partitions, so n=10,k=3. Therefore

`C<=10+floor(10*9/3)=40 < 100`.

Hence a maximal-cardinality 1-resolvable QLS(10), IF one exists, CANNOT have all100 vectors supported on at most2 coordinates in any one common orthonormal basis. This eliminates that entire ansatz over EVERY incidence L and EVERY complex coefficient choice; it does not say that an individual two-sparse vector is impossible if other vectors have larger support. It gives no information about an array that is not globally two-sparse.

## 2. Complete proof with the SAME blocks and complex vectors

Consider any ONB block in the globally two-sparse array. Two nonzero vectors whose supports have EXACTLY ONE common coordinate have nonzero inner product, because their inner product consists of one nonzero complex product. Thus orthogonal vectors cannot have one-coordinate support intersection. If a block contains a vector v with exactly-two support {a,b}, no singleton vector can use a or b, and no other two-support vector can use exactly one of a,b.

There must be ANOTHER block vector with nonzero a-coordinate: if v were the only one, the ONB identity `sum_(y in B)|<e_a,v_y>|²=1` would fail, since |<e_a,v>|²<1 because b is also nonzero. That other vector must have support exactly {a,b}. There are at most two nonzero mutually orthogonal vectors in this two-dimensional coordinate plane, so there is EXACTLY ONE such partner in the block. Its ray is the unique one-dimensional orthogonal-complement ray to v inside span{e_a,e_b}; arbitrary complex phases are harmless.

Let x be ANY cell with exactly-two-support ray R. In EACH of the k blocks containing x, the preceding argument gives a partner of the same complement ray R_perp. Those k partner cells are distinct: blocks from different classes intersect only in x. Pick any partner cell y of ray R_perp. Applying the identical argument at y shows that its k distinct partner cells all have ray R. Therefore EVERY exactly-two-support ray appearing anywhere has multiplicity at least k. This uses actual ONB completeness, the SAME full array, exact pairwise block intersections and the full complex 1D complement; no assumption of a particular phase or chosen L occurs.

The t two-support cells are partitioned by their actual ray classes, each of size at least k, so their number of distinct rays is at most floor(t/k). Every singleton-support ray is one of the n coordinate rays, giving at most min(n,s) such rays. The two categories cannot be parallel because their supports have different sizes. This proves the first inequality in (1).

For `s<=n`, the quantity `s+floor((n²-s)/k)` is nondecreasing in integer s, since increasing s by one changes the floor by either0 or−1. For `s>=n`, `n+floor((n²-s)/k)` is nonincreasing. Thus the first bound is maximized at s=n, proving the second inequality. No continuity or rounding assumption is hidden.

The original three partitions satisfy the intersection hypothesis because each L-transversal contains one cell from each row and each column; the row/column intersection is also a single cell. The given L is arbitrary. The argument does not claim 40 is an attained maximum; it establishes a universal upper bound at this support restriction.

## 3. Exact original-object check on the Parker construction

The ACTUAL 12-ray rational 1-resolvable QLS(10) constructed from Parker's published OA is in `frontier-20261028-coordinate-switch-result-v1.json`, SHA256 **e64b0e90d6b0f908a07727de96f44bacf24a1abbf723b306de7e681189c05533**. Every vector has denominator65 and support1 or2. Independent checker `frontier-20261028-partial-qls-exact-check-v1.py` SHA **40f201ed11f598afada8091ac59b7fe5865b7d75acd5bf5764b4024550a4ed47** previously verified 100/100 norms, all30 row/column/transversal ONBs and the original resolution exactly.

A separately written exact partner/profile checker `frontier-20261028-two-sparse-check-v1.py`, SHA256 **66efa6307c956de0276033103261c5c10d8d181283eb5e4f38f197b652b1abfb**, examined every exactly-two-support cell, its three distinct blocks, the partners' exact rational rays, and the resulting ray classes. Actual output:

```text
actual singleton-support cells 94 two-support cells 6
every 2-support cell has three distinct parallel partner cells: PASS
ray count 12 profile bound 12 uniform all-array bound 40
ray multiplicity histogram {3: 2, 7: 2, 10: 8}
```

This input attains the **profile-dependent** first bound in (1), `min(10,94)+floor(6/3)=12`. It does NOT show the uniform40 bound is sharp, and the checked object is not a 100-ray witness. Exact integer tests corroborate the example; the theorem's ALL-array proof is §2.

## 4. Boundary and next target

The bound is invariant under a common global unitary only in the appropriate existential sense: if an array becomes globally support<=2 after some common unitary/basis choice, apply the theorem in that resulting basis. It is NOT valid to assert that every quantum array admits such a unitary. Multiple 2-support shapes, arbitrary complex entries and phases, singular/zero coordinate entries, any L and all ray coincidences are covered at the theorem's stated scope. All-one-support arrays are also covered (t=0); unit vectors exclude empty support.

Beyond this restricted ansatz, the actual 100-ray problem remains open. A genuine next construction/obstruction must accommodate vectors of support at least3 somewhere in EVERY common basis, and must retain all30 original simultaneous ONBs and the100 distinct rays. The separately verified Parker13-ray array has three-support local vectors, but still only13 rays; it is not WLOG or global evidence. Independent review of this theorem and historical novelty screening remain outstanding. No external model, publication, deletion or infrastructure mutation occurred.

**END — every globally two-sparse 1-RQLS(10) has at most40 rays; unrestricted target remains open.**
