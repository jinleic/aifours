# Candidate theorem: the Shor code has no order-2310 finite completion

Owner **MathShor-2**, math-5. Actual native clock of independent final-branch replay: **Wed Oct 28 20:16:18 PDT 2026**.
**HIGH-CONSEQUENCE CANDIDATE: exact written/finite-computation reduction, separately replayed within the same harness. It is NOT yet peer-reviewed, formally verified, independent-model-family verified, novelty-cleared or adopted. It does NOT solve the original all-order completion question.**

## 1. Statement and same-D premises

> **Candidate theorem.** No finite UD factor-complete extension of the literal Shor code can have actual pure-a atom `a^2310`.

For any hypothetical D, its actual multi-b-permitting border sets `P={i mod2310:a^i b^k in D, k>=1}` and `Q={j mod2310:b^l a^j in D, l>=1}` form a classical direct cyclic tiling, with actual old anchors

    A={0,3,8,11} subset P,     Y={0,1,7,13,14} subset Q.

The same-D border theorem and the necessary Sands gcd-class disjointness criterion are prior mathematics, independently reconstructed in the earlier pinned packets. At n2310 the old head- and tail-difference gcd classes are

    G_A={2,3,5,11},     G_Y={1,6,7,14}.                       (1)

The prime factorization `2310=2*3*5*7*11` is squarefree. For each prime, whichever side's cardinality is divisible by it is uniform modulo that prime; this follows from the direct-tiling Fourier identity and prime cyclotomic irreducibility.

## 2. Complete size sieve

The previously written all-order anchor argument proves `|P|>=8`. Exact old-anchor gcd screening leaves248 individual P-candidates and409 Q-candidates. Product/divisibility then leaves precisely20 candidate P-sizes. Elementary prime-balance and old-anchor/candidate class capacities reduce these to

    {10,14,15,21,22,30,33,35,42,55,66,70,77,154}.           (2)

`frontier-20261028-2310-residue-screen.py` checks both candidate sets, the complete divisor list and this prime sieve. Every size in (2) is treated below; no Z3 status is used as evidence.

## 3. Six elementary parity and matching exclusions

The Q screen contains only FOUR odd residues that are not1 mod3: `{651,903,1421,1673}`. If an actual Q were divisible by6 and had more than24 elements, uniformity mod2 and mod3 would require `|Q|/2` evens but at least `2|Q|/3-4>|Q|/2` evens, contradiction. This excludes P sizes35,55,77, whose Q sizes are66,42,30 respectively.

The screened P class1 modulo3 has24 candidates. Ten explicit disjoint gcd-forbidden pairs leave capacity14, so P=66 is impossible: 3-uniformity would demand22 in that class.

For P=70, 5-uniformity forces all14 screened candidates in each of mod5 classes2 and4; in particular it forces1977 and344, whose difference has forbidden gcd1. For P=154, 11-uniformity forces all14 candidates in each of mod11 classes1 and6, including1145 and336, again a forbidden gcd1 pair.

For P=33, 3-uniformity requires11 heads congruent1 mod3. Of the24 screened candidates,14 lie in mod11 class0 and10 lie outside it. The old heads0 and11 already occupy two of the three places in mod11 class0. Thus all10 outside-class candidates must be selected, together with one of the14 inside-class candidates; the pinned checker explicitly verifies that EACH of those14 conflicts with at least one of the forced10. Hence P=33 is impossible.

These checks eliminate `{33,35,55,66,70,77,154}` from (2).

## 4. Four independent tail-quota exclusions

For P sizes10,14,15,22, Q must be uniform in the moduli indicated in the following table. Each instance retains only old-anchor-compatible tail candidates in the named quota classes, checks old anchors that lie in those classes, and forbids G_A. Dropping all other Q constraints is a relaxation; any actual tiling would induce a solution.

| P size | Q size | retained exact quotas | candidates | bitset nodes / prunes | independent set-based nodes / prunes |
|---:|---:|---|---:|---:|---:|
| 10 | 231 | mod3 class0:77; mod11 class2:21 | 116 | 21 / 11 | 27 / 14 |
| 14 | 165 | mod3 class2:55; mod11 class3:15; mod5 class3:33 | 184 | 4,843 / 2,409 | 10,727 / 5,364 |
| 15 | 154 | mod11 classes3,0:14 each | 74 | 481 / 241 | 449 / 225 |
| 22 | 105 | mod3 classes2,0:35 each | 178 | 111 / 56 | 115 / 58 |

Both implementations exhaust each instance with zero solutions. For EACH case the producer directly verifies an explicit positive-control witness to the same retained quotas after removing ONLY gcd2 from the old-head exclusion set; each control contains gcd2 collisions. These are relaxed tail sets, not direct tilings or code completions.

## 5. Sizes21,30 and42

### P=21: gcd10 forced on both sides

Here P is uniform mod3 and7, while Q is uniform mod2 and5. If P avoided gcd10 in addition to G_Y, its old-anchor-compatible candidates in mod3 class1 and mod7 class2 would have no selection meeting quotas7 and3: 42 candidates, 65 bitset nodes or127 independent set-based nodes. If Q avoided gcd10 in addition to G_A, its candidates in mod2 class0 and mod5 classes1,3 would have no selection meeting quotas55,22,22: 218 candidates, 69 nodes in each implementation. Concrete positive controls satisfy the respective relaxed quotas after the extra gcd10 ban is removed. Thus each side must use gcd10, contradicting Sands.

### P=30: incompatible head quotas

P must be uniform modulo3 and5. The relaxed head instance retains only old-anchor-compatible candidates in mod3 class1 or mod5 class3, old anchors3,8, and exact quotas10 and6. It has172 candidates. The bitset search reports UNSAT in611 nodes; the independent set search reports UNSAT in1,029 nodes. A directly checked control satisfies the quotas if gcd6 is dropped. Therefore P=30 is impossible.

### P=42: a uniquely saturated 14-head class

P must have14 heads in mod3 class1. The screened class has24 candidates partitioned into ten disjoint forbidden pairs and four singletons, so selecting14 requires one endpoint of every pair plus all singletons. Both implementations enumerate all `2^10=1,024` possibilities, in retained-endpoint and omitted-endpoint orientations, and find exactly one gcd-compatible set:

    {88,253,418,583,748,913,1078,1243,1408,1573,1738,1903,2068,2233}.

Together with the old heads, this set forces gcd classes10,35,77, for example via pairs `(418,8)`, `(2068,3)`, `(2233,0)`. Q must avoid those classes as well as G_A. Since |Q|=55, it is uniform modulo5 and11. A relaxed Q instance retaining mod11 classes3,0,4 with quota5 each and mod5 class0 with quota11 has81 candidates; the two independent searches return UNSAT in281 and495 nodes. A directly verified positive control satisfies these quotas after only gcd77 is removed. Therefore P=42 is impossible.

These three cases finish the complete size list (2), establishing the stated **candidate order-2310 obstruction** at the exact written/finite-computation scope.

## 6. Pins, prospective floor and limits

| Artifact | SHA256 | LF / bytes |
|---|---|---|
| `frontier-20261028-2310-residue-screen.py` | 29bd2505ab32fa3ab37fa96002cd5ba02634f37d34aec5c216943632ba7d89ba | 42 / 2470 |
| `frontier-20261028-2310-quota-check.py` | 020f4ebce61caf1580c2af34a0ef36c93bafd9bcb4618f0c0d8b18289645c0c7 | 52 / 3612 |
| `frontier-20261028-2310-quota-replay.py` | 61ba10079feb87e65e7410a1eee5e33582062fe5868ad3036aee123c31a9f22e | 37 / 1788 |
| `frontier-20261028-2310-final-branches-check.py` | ddf182009eb9c9ee59dc99e5f64b014413eecaa12741e1d76892fbbeab31a831 | 69 / 4080 |
| `frontier-20261028-2310-final-branches-replay.py` | ab49c5a738051dd35602db8db3a04b760839d3e6d4bfa7692e32658ad205fb87 | 51 / 2688 |
| `frontier-20261028-eight-head-border-obstruction-v1.md` | 803c69db29d403a1a2fec137dcd9f50e132356802b00b7d64ac2e9138de4b412 | 76 / 5892 |
| `frontier-20261028-660-and-order-floor-candidate-v1.md` | cce97442e94386f80e9d63f782c5be83c7c4c0e3a7eddb5eb38e0c999494ab79 | 80 / 6677 |
| `frontier-20261028-1320-border-no-go-candidate-v1.md` | 52aeaff132fb0e59f9c735054b017df9471e543035ba0bfea1d3dcd04385869e | 116 / 11391 |
| `frontier-20261028-1980-p33-border-obstruction-v1.md` | 96b7b2276fc5d832d8894576ef0d1a5fec6ca420aa59383a3de1922583edf5bc | 65 / 5447 |

If the separate order660,1320,1980 and present2310 candidates, together with the independently derived necessary alternative `660|n OR 2310|n`, all survive independent scientific review, they would imply the **conditional candidate floor `n>=2640`**. This floor is not yet an adopted fact. No formal proof, independent-model-family review or novelty screen is claimed; the original unrestricted finite UD factor-completion problem remains OPEN.

**END OF ORDER-2310 BORDER NONCOMPLETION CANDIDATE.**
