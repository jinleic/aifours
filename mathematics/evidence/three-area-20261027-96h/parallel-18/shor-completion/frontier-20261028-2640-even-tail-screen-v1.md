# Shor completion: an even-tail screen at order 2640

Owner **MathShor-2**, math-5. Native clock of the independent finite certificate check: **Wed Oct 28 20:32:17 PDT 2026**.
**WRITTEN plus exact finite certificate, restricted to the requested even-|Q| branch. It does not exclude n2640, settle an all-order problem or claim peer/formal/cross-family/novelty acceptance.**

## 1. Result

For any hypothetical finite UD factor-complete extension of the literal Shor code whose actual pure-a order is2640 and whose actual b-run tail border Q has EVEN size, its same-code direct border factors satisfy

    |Q|<=266,
    |P| in {10,12,15,20,22,24,30,33,40,44,55,88}.             (1)

These are only necessary conditions. In particular the P8/Q330 branch is excluded. No odd-Q theorem or cofactor classification is used in this packet, and none of the 12 listed branches is asserted feasible.

## 2. Classical gcd-class screen and the 266-clique certificate

The actual-word border factorization and the necessary Sands gcd-difference criterion are classical results independently reconstructed in the previous written packets. The old anchors are

    A={0,3,8,11} subset P,  Y={0,1,7,13,14} subset Q,
    G_A={3,5,8,11},         G_Y={1,2,6,12},

where the last two sets are the gcd classes of nonzero old differences at2640. Thus each Q-element must be individually compatible with Y against G_A, and any two Q-elements must also avoid G_A.

The screened set has658 candidates. The explicit JSON certificate partitions ALL658 into266 nonempty cliques, each with every within-clique difference in a forbidden G_A class. Hence Q can take at most one per clique: `|Q|<=266`. In particular P8 would force Q330 and is impossible.

The screened P set has224 candidates. Among its24 candidates congruent1 modulo3, eight disjoint explicit forbidden-G_Y pairs leave capacity16. If 3 divides |P|, P is uniform modulo3, so `|P|/3<=16`. Exact prime-balance/candidate capacities for5 and11, old anchors, product divisibility, and the stated even-|Q| condition give exactly the 12 sizes in (1). The earlier written `|P|>=7` anchor lemma suffices:7 does not divide2640, so any size in this order is at least8.

## 3. Independently checked certificate and limits

| Artifact | SHA256 | LF / bytes |
|---|---|---|
| `frontier-20261028-2640-even-tail-cover-v1.json` | 791016f119addb8367e729d803da53e8eb2ea4d1ed393ecbce9bfa830bbff758 | 1 / 3689 |
| `frontier-20261028-2640-even-tail-cover-generator.py` | 70fab0f6f5738225c1936976ff79c9cb8a36cf741ab325de69df73a4d2c2bcb8 | 29 / 1398 |
| `frontier-20261028-2640-even-tail-cover-check.py` | bc0881e5aae25837c857bda4b9434c708f0246ed0a9f1fe6159ff4385eddadba | 38 / 1849 |

The independent checker reconstructs both candidate sets and their old gcd classes, verifies clique coverage/disjointness and EVERY pair, checks all eight disjoint P-pairs, and recomputes the divisor/prime sieve. It returned the exact values in §1. These are finite integer checks, not formal proof or independent-model-family verification. The original finite UD factor-completion problem remains OPEN.

**END OF ORDER-2640 EVEN-TAIL SCREEN.**
