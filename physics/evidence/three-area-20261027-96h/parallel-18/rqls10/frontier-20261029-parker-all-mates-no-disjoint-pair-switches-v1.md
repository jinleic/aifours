# The Parker resolution admits no two disjoint independent color-pair switches

**COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Thu Oct 29 00:27:15 PDT 2026**. This is a complete finite census for ONE fixed Latin resolution, not an impossibility theorem for other resolutions or for nonclassical constructions.

## Claim

Take the Parker order10 resolution L printed in `frontier-20261028-parker-13ray-result-v1.json` SHA **0108335bbbe2d35214761904172490bbbed6976d59dd19748aaa7843276dc9e5**. For EVERY classical Latin square A orthogonal to L, it is impossible to find two disjoint pairs of A colors for which the corresponding row/column/L pairing graphs are both disconnected. Hence the standard scheme that independently rotates two disjoint color pairs on proper graph components cannot improve a classical array from 10 to 14 rays with this L.

A color class of A is a transversal of L. For two colors, make a graph on their 20 cells, with edges pairing the two colors within each common row, column and L-label class. A proper connected component can be independently rotated by a 2×2 unitary on those two color rays, preserving all30 ONBs. Two disjoint color pairs would require four cell-disjoint L-transversals whose two associated pairing graphs are disconnected.

The complete exact census finds **1272** L-transversals and **311214** cell-disjoint transversal pairs. Exactly **162** pairs have disconnected pairing graphs, each with component row sizes 3 and7 (equivalently 6 and14 cells). No two such pairs involving FOUR distinct transversals are mutually cell-disjoint. There are 72 compatible pairs of trade edges sharing one transversal; they form exactly **24** three-transversal triangles. For every such triangle the short components are in rows7–9 and the three transversals use columns7–9 there, so they lie in the same 3×3 block as the existing 13-ray construction.

The census tests compatible partial transversal sets, whether or not they extend to a full orthogonal mate. Therefore the no-two-disjoint-switch conclusion holds for **all** classical mates, without having to enumerate or assume connectivity of the space of mates. The separate classical-switch BFS from the existing Parker mate visits six normalized mates and then exhausts its reachable orbit, but that BFS by itself is NOT a census of all mates.

## Exact evidence

`frontier-20261029-parker-all-mates-trade-census-v1.py` SHA **3b8182c0303a4033d7611ab7080a66191714e27724ad1731e212b67ab26263e6**, result SHA **68c116e3ad50438a30ec33de141561f177caf720332f7dcd7e188ff1f0e9c170**, enumerates all permutations by row-recursive Latin constraints and computes trade components via the two induced row permutations.

Independently, `frontier-20261029-parker-trade-dsu-replay-v1.py` SHA **7a7783be09eb571ea4866cb16c52db637a901663491054aa3fa3043fe204a455**, result SHA **6446901b2381b956a76407630c0b5341650e6f41ced9cc23ed8caa6696b84fef**, uses dynamic MRV transversal enumeration and a 20-cell disjoint-set union for all three context pairings. `frontier-20261029-parker-trade-coverage-v1.py` SHA **91ddd8852d9b0e8fa607ac67616db486e47c3a511a8fc8539373596054222f0a**, result SHA **6ee13527005ce0c215e93c5a9efa4a6170bf247ed92f14ec807d2ec609193393**, compares every one of 1272 permutations and all162 literal trade edges and component memberships. `frontier-20261029-parker-trade-triangle-structure-v1.py` SHA **4f4d6a56052ef6bbf2bb8876c0bf31aeadddcae84fec655fe6aea24285180c86**, result SHA **908e57cfd8f059cf2b28bb3779c8a0285630b0529f695cc1d04ca4c40f3c6cf3**, checks the common short block in all24 triangles.

The finite enumeration, source L, interpretation as switches, and cell/coordinate bookkeeping require independent review. This does NOT rule out sequential switches using overlapping colors, larger-plane moves, nonclassical starting arrays, 1RQLS10 with L, or a 100-ray 1RQLS10 with some other resolution.
