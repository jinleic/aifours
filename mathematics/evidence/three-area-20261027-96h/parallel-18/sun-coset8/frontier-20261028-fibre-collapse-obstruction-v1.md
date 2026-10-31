# A quotient-fibre merge does not preserve a large-gcd certificate

**NEW WRITTEN OBSTRUCTION / CHECKED PARTIAL COSSET CONFIGURATION, not an eight-coset counterexample or reviewed result.** Native prewrite clock: **Wed Oct 28 17:14:08 PDT 2026**. The construction uses actual subgroups, actual cosets, actual projections and an exact normal kernel; it disproves one specific proposed bridge, not the Sun8 conjecture or either index2/3 transfer.

## 1. The tempting but false bridge

In a normal extension, suppose several original disjoint cosets project to quotient cosets with a common point. A natural quotient-only compression replaces that whole cluster by the intersection coset. It is FALSE in general that a large gcd involving the compressed quotient index and an outside quotient-coset index must come from a large gcd between one of the original G-indices and the outside original index.

The exact obstruction is that compression multiplies pairwise-coprime quotient-index factors drawn from DIFFERENT original labels. Their PRODUCT may meet a single outside index in a divisor >=8 even though each individual original-index gcd stays <=7. The following is a uniform family of actual group examples, not only an abstract index-tuple assertion.

## 2. Uniform actual-coset family

Let P be any set of distinct primes chosen from `{2,3,5}` whose product L is at least8. Thus P has at most three elements and 7 does not divide L. Let

    G = C7 × C_L,       N = C7 × {0},        G/N ≅ C_L,

with additive notation. Label the elements p∈P as p_1,...,p_r and choose pairwise distinct `z_i∈C7` (possible since r<=3). For each i put

    U_i = {0} × p_i C_L,        g_i = (z_i,0).

The p_i-th multiple subgroup `p_i C_L` has index p_i in C_L, so `[G:U_i]=7 p_i`. The actual cosets are

    g_i+U_i = {z_i} × p_i C_L.

They are pairwise disjoint because their first coordinates are distinct. Their original index pair gcds are exactly7: `gcd(7p_i,7p_j)=7` for i≠j.

Add the outside actual subgroup and coset

    U_* = C7 × {0},       g_*=(0,1),
    g_*+U_* = C7 × {1},   [G:U_*]=L.

Since no p_i divides1, the outside coset is disjoint from EVERY original cluster coset. For every i,

    gcd([G:U_i],[G:U_*]) = gcd(7p_i,L)=p_i <=5 <8.

Thus the r+1 ACTUAL cosets are pairwise disjoint, and every pair of their original indices has gcd<=7.

Their actual images in Q=C_L are

    C_i=p_i C_L,             C_*={1}.

The cluster images have common intersection `{0}`, since L is the product of the distinct p_i. This intersection is the left coset of the trivial subgroup of Q, with quotient index L. The outside quotient coset `{1}` is disjoint from EVERY C_i and has index L. Therefore the merged quotient pair has index gcd

    gcd(L,L)=L>=8,

while no original pair has index gcd>=8. This is a direct failure of flattening the merged quotient-gcd certificate back to a single original pair. All actual normal-fibre and subgroup conditions are explicit.

## 3. Concrete member and two independent representations

For P={2,3,5}, L=30 and `(z_1,z_2,z_3)=(0,1,2)`, the actual G subgroup indices are `[14,21,35,30]`; their six pair gcds, in lexicographic pair order, are `[7,7,2,7,3,5]`. Cluster quotient intersection is `{0}`, outside quotient coset is `{1}`, both quotient indices are30, and their gcd is30.

A direct product-representation checker `frontier-20261028-fibre-collapse-witness-check.py`, SHA256 `d4b550c813d2a6d1074c6f702b3842d9c8817cabd745bcf3e3e488fb67c10988`, constructs all210 group elements, checks each subgroup's finite closure, constructs each actual left coset, checks every actual pair disjoint, checks all six original index gcds, and computes actual quotient sets. Actual execution:

```text
group_order: 210
actual_subgroup_indices: [14, 21, 35, 30]
six_original_pair_gcds: [7, 7, 2, 7, 3, 5]
actual_pairwise_disjoint: True
quotient_cluster_intersection: [0]
outside_quotient_coset: [1]
merged_and_outside_indices: [30, 30]
merged_pair_gcd: 30
PASS: merged pair reaches >=8 while no original pair does
Wed Oct 28 17:13:45 PDT 2026
```

A separately written cyclic-representation verifier `frontier-20261028-fibre-collapse-cyclic-verifier.py`, SHA256 `d8c27eb9bcfdb3b367078305b7f509fed2ac647893f8c4865fa7302e67f29fe0`, uses the explicit isomorphism `C210 -> C7 × C30`, `z -> (z mod7,z mod30)`, and independently builds cosets as residue classes. It also checks two altered representatives are rejected specifically for intersecting original cosets. Actual execution:

```text
cyclic_original: VALID_BRIDGE_OBSTRUCTION
mutated_outside_representative: INTERSECTING_ACTUAL_COSETS
mutated_cluster_representative: INTERSECTING_ACTUAL_COSETS
PASS: cyclic witness and two intended intersection-negative controls
Wed Oct 28 17:14:01 PDT 2026
```

These two same-harness implementations and the written proof support this limited four-coset obstruction. No third independent checker, cross-family model, human review or formal certificate was run; the result is not promoted beyond that evidence.

## 4. Boundary

There are only r+1<=4 actual cosets in the family, not eight. No claim is made that the partial configuration extends to eight disjoint cosets, and it cannot be presented as an original Sun8 counterexample. The family has a solvable group and is compatible with the conditional solvable-group Sun8 candidate. It falsifies only the specific universal quotient-merge lifting implication in Section1; a correct eight-coset transfer proof may exploit extra hypotheses or other cosets. Source priority/novelty, full extension closure and finite-perfect quotient cases remain open.
