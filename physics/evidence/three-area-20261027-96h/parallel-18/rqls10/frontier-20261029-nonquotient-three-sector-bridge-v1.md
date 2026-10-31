# Three-dimensional sector bridge for a non-Z2-quotient order-10 resolution

**WRITTEN + EXACT-INTEGER AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` before writing: Thu Oct 29 10:04:56 PDT 2026. The target unrestricted maximal 1-RQLS(10) remains **OPEN**. This packet neither constructs one nor proves it impossible.

This is a different bridge from the flat/covariant parity-core and fixed-core completion lines. The general observation applies to any resolution Latin square; the exact application uses a literal Weisner order-10 square that provably has **no Z2 quotient**. It makes a sector-support hypothesis, explicitly stated below. Stopped full-Gram and selected-calibration episodes are not inputs.

## 1. A universal three-dimensional sector constraint

Let Q be a 1-RQLS of order n, with resolution square L. Suppose there is a 3-dimensional subspace H such that every cell ray lies in H or H-perpendicular. Let P be the cells whose rays lie in H. Each row, each column and each L-class is an ONB of C^n, and exactly three rays in it lie in H. Consequently P has 3n cells and meets every one of those 3n contexts in three cells.

Call an **extra context triangle** a row R, a column C and an L-class T such that each of the three pairwise intersections is in P, but they are three distinct cells. Equivalently, in coordinates, P contains (r,c), (r,c'), (r',c), where r'≠r, c'≠c, L(r,c')=L(r',c)=t, and L(r,c)≠t.

**Theorem 1.** If P contains an extra context triangle then the six sector cells in R ∪ C ∪ T carry exactly three rays. Therefore Q has at most n²−3 distinct rays. In particular a maximal 1-RQLS(10) can never have such a sector-support triangle.

*Proof.* Let x be the sector ray at R∩C, y the ray at R∩T, and z the ray at C∩T. They are pairwise orthogonal because each pair occurs in one of the three sector ONBs. They are nonzero and therefore form an ONB of the 3D space H. The third sector ray in R is parallel to z; the third in C is parallel to y; the third in T is parallel to x, since each is determined by orthogonality to the other two. The three contexts intersect pairwise only in the indicated distinct cells, so these are six distinct cells. Six cells contribute three distinct rays, a loss of at least three from n². ∎

The statement is independent of sparsity in any coordinate basis, of which rays occur outside H, and of classicality. It does **not** say that every maximal array has a 3D sector.

## 2. Equality propagation beyond one triangle

For any fixed sector support P, start with a distinct formal ray class for each of its 3n cells. Put an edge between two classes when their cells occur together in a sector context. In H, orthogonal nonzero rays are distinct.

Whenever classes a and b occur together in a sector ONB, its third class c is the unique ray in H perpendicular to both. If another class d is connected by orthogonality edges to both a and b, then d=c. Merge c and d and repeat; each merge is an exact necessary equality, and it is valid regardless of how the other rays are chosen. If a merge ever forces two cells of one sector ONB to have the same class, that support is impossible. Otherwise, if the resulting partition has K classes, any array with that support has at most

`(n² − 3n) + K`

distinct rays: there are 3n sector cells and at most n²−3n other cells. Failure to merge two classes does not prove their rays can actually be chosen distinct.

Each emitted proof step contains a basis, its two reference cells a,b and third cell c, a witness cell d, and the two contexts certifying a⊥d and b⊥d. The independent replay checks these hypotheses under all earlier merges before accepting c=d. This is a finite proof system based only on 3D orthogonality; it is not a numerical rank or local-rigidity argument.

## 3. Literal nonquotient order-10 example

The following are the two independently normalized classical squares A and L (entries are digits 0–9, one per column). Their unnormalized pair is the literal Weisner table in `frontier-20261028-ols10-switch-v1.py`, SHA-256 `394c59221d0526ca623d46925d4d82e68d13ddb55b6c45f5bdada1ee622ff172`. A is used as a *combinatorial mate*, not as an assumption that Q's rays are classical.

```text
A                              L
0123456789                     0123456789
3654089172                     5802617934
7019863254                     6758290341
9765231048                     1937524860
8271940563                     9046372158
1347528690                     7481963205
2508794316                     8315049627
5496372801                     2560781493
6982107435                     4279835016
4830615927                     3694108572
```

Integer checks show each row and column of each square is a permutation and all 100 ordered pairs (A,L) are distinct. Thus every A-color class is an L-transversal. In fact L has no balanced Z2 quotient: if it did, any transversal would contain five cells with T0 labels. The row and column balances force its counts in the Q00 and Q11 blocks to be equal, so the number in those two T0 blocks would be even, contradicting five. Hence this application genuinely lies outside the Z2-quotient branch.

### A literal extra triangle

Take P to be the cells where A belongs to {0,1,2}, using zero-based indices. The relevant three sector contexts are

```text
row R0:     (0,0), (0,1), (0,2)
column C1:  (0,1), (2,1), (4,1)
label T0:   (0,0), (4,1), (9,5)
```

The three pairwise shared cells are (0,1), (0,0) and (4,1), all distinct. Thus any Q with this L and sector support P must have

`ray(0,2)=ray(4,1)`, `ray(2,1)=ray(0,0)`, and `ray(9,5)=ray(0,1)`.

The propagation certificate goes further: all ten cells of each of the three A-color transversals have the same ray. Hence there are just three sector rays and Q has at most 73 rays. This is a necessary bound even if the complementary 7D cells use arbitrary complex vectors.

## 4. Exact coverage of three-transversal supports

For the fixed literal L above, a **three-transversal sector support** means a set P that is the union of any three pairwise disjoint L-transversals. No extension of those three transversals to a complete classical mate is assumed for the first result.

**Theorem 2 (exact finite census, author candidate).**

- L has exactly **728** transversals.
- There are **3,365,592** unordered triples of pairwise disjoint transversals.
- **3,363,624** of those triples have an extra context triangle and are excluded for maximal 1-RQLS(10) by Theorem 1.
- The remaining **1,968** triples have no extra triangle; they give **1,968 distinct sector supports**. They are residual cases, not constructions and not proved completable.

Thus a maximal Q with this fixed L and a 3D sector whose support is a union of three transversals would have to use one of the 1,968 literally listed support masks. This is not a claim about sector supports that cannot be decomposed into three transversals.

**Stronger exact statement for complete classical mates.** The same literal L has exactly **10** first-row-normalized classical mates. Choosing any three color classes of any one of them gives 1,197 distinct sector supports. For **1,194** supports, the equality propagation of §2 proves that the 30 sector cells carry exactly three rays, so any such Q has cardinality at most **73**. The remaining **3** supports have no extra triangle and no equality is inferred by this propagation rule; whether they admit a maximally distinct realization is open here. Every one of the 1,197 supports is a union of three disjoint transversals; these figures are not a classification of arbitrary 3-plexes of L.

## 5. Exact computation and replay

- Producer `frontier-20261029-nonquotient-three-sector-certificate-v1.py`, SHA-256 `177e65d99d868eaf37969d4849b4136a54f1794265ff2b5d0df1f835548dd9e4`; 309 LF. Result `frontier-20261029-nonquotient-three-sector-certificate-v1.json`, SHA-256 `975e381fff5745f687bbe5e0a25d84a21239e0c7dcbf02cf023eac80f74a1900`, 1,061,800 bytes; observed native clock Thu Oct 29 10:03:21 PDT 2026.
- Independent author implementation `frontier-20261029-nonquotient-three-sector-replay-v1.py`, SHA-256 `636eca06493efd4de98af1d282efa12f5f69ecc53311ed43d62c750af21e423c`; 227 LF. Result `frontier-20261029-nonquotient-three-sector-replay-v1.json`, SHA-256 `a72959304f011cdd5e5059950e91af2800d9e3249f8bc96e2542e8a338e40bc1`; observed native clock Thu Oct 29 10:04:30 PDT 2026.

The producer reads the pinned source as an AST **literal**, never executes it, verifies the Latin/orthogonality properties, and independently enumerates L-transversals by an exact row/column/label bitset DFS. It tests disjoint triples using exact integer bitsets, derives the 10 full mates by exact cover, outputs all 1,968 residual masks and a proof record for each of the 1,197 mate supports, and replays its equality steps.

The second implementation reads the pinned producer **output**, not its code. It independently regenerates all 728 transversals by testing all 10! column permutations; uses transversal-membership bitsets rather than the producer's cell bitsets for the 3,365,592 triple census; recomputes the full mate exact covers by selecting uncovered cells; and replays **32,238** individual equality steps from the output. Its in-memory mutations of an outside-sector witness, an invalid context, and a false orthogonality each fail for their intended error reason. Both programs use integer/bitset arithmetic only. These are same-harness author computations, not independent-model-family review, formal proof or novelty clearance.

## 6. Remaining gap

The order-10 target remains open: an actual maximal 1-RQLS(10) need not use this L, need not possess a 3D orthogonal sector, and even a sector with this L need not be a union of three transversals. The 1,968 triangle-free supports and the 3 special complete-mate supports are only necessary-condition survivors. No completed non-diagonal parity core, no universal no-go, and no new 100-ray witness are claimed.
