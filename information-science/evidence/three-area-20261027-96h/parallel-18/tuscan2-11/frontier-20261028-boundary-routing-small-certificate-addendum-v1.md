# Boundary-routing addendum: T2 does not generally force the canonical Latin completion

Owner **InfoRecursiveMDS18-2**, info-4. Actual native clock before writing: **Wed Oct 28 22:15:42 PDT 2026**. Additive to `frontier-20261028-boundary-routing-parity-and-unique-completion-v1.md` (SHA-256 `b8617ddf72595a35ecffd5f153adf1e2acc10bd58bce71359cb3f4fd35d246f9`), unchanged.

**WRITTEN finite certificate + exact small check in the owner's Python kernel.** Not a T2(11) witness or no-go, not new existence science at order 4, not independent-model/formal/novelty acceptance. No native solver, search or heavy campaign was run for this addendum.

## 1. Explicit order-four certificate

The earlier recorded order-four rows are

```
0 1 2 3
1 3 0 2
2 0 3 1
3 2 1 0
```

Their adjacent pairs, grouped by row, are

```
01 12 23
13 30 02
20 03 31
32 21 10
```

These are exactly all twelve ordered pairs of distinct symbols. Their distance-two pairs are

```
02 13
10 32
23 01
31 20
```

All eight are distinct. Hence the displayed array is T2(4), directly from the definition, independent of any solver outcome. Its four missing distance-two pairs are M={03,12,21,30}.

Using the preceding packet's P_b and Q_b gives

```
b           0  1  2  3
P_b         1  3  0  2
Q_b         1  3  0  2
```

Every canonical boundary pair is diagonal: (1,1),(3,3),(0,0),(2,2). Thus B is the identity matrix, not the incidence matrix of M, and every forced placement for the outer-triple Latin completion lands on an already-filled diagonal. The completion is impossible although the array is a valid T2 square.

This disproves the GENERAL premise "every T2(n) forces B=M and the canonical Latin completion." It does not disprove that property at order 11, and it gives no rule-out of T2(11). Any use of that completion route for the original target still needs an additional original-order theorem; it cannot be silently treated as necessary.

## 2. Routing parity check, explicitly

Here E=(0 3)(1 2), so sign(E)=+1. The four σ_b are respectively (2 3), (0 2), (1 3), (0 1), each with its indicated boundary predecessor fixed. Their sign product is +1, agreeing with (−1)^10·sign(E)=+1. The two endpoint cycles each have length 2, so the routing permutation Φ has two cycles of length (4−1)·2=6, as predicted. These checks illustrate the unconditional routing identity even when the conditional Latin-completion premise fails.

## 3. Small checks actually executed

From the pinned existing row JSONs, the owner's Python kernel rechecked row permutations, all D1/D2 event counts, all local σ_b bijections and the sign identity, then compared the full boundary-pair multiplicity Counter to the complete missing-pair set. Only integers, set operations, itertools-style finite enumeration and collections.Counter were used.

- `frontier-20261028-channel-n4-run-01.json`, SHA `bcd7fc2a04f187028d8f722c302f9b98b41b4681fdfa9d2c0debe706f03bff61`: parity identity holds; B≠M, as exhibited in full above.
- `frontier-20261028-channel-n6-run-01.json`, SHA `b675aed530321c81f96acd3b1e7191b6cd77b6b7ea0adba2e23981cc04f61199`: parity identity holds; B≠M.
- Six explicit arrays in `frontier-20261028-channel-n8-enumeration.json`, SHA `5a77f081cd4acc2731ed984989d6d861d26c3002416dffa4e697dd248264ff00`: parity identity holds for every displayed array; B=M exactly for zero-based indices 3 and 5, and not for indices 0,1,2,4.

The last statement is restricted to those six explicit arrays. Completeness of the old order-eight enumeration has not been admitted from its unverified final UNSAT, and is not assumed here. No small-order observation is extrapolated into an original-order existence or nonexistence claim.
