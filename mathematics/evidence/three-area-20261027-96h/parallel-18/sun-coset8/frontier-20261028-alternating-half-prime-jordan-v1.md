# A_(2r) half-prime case without the unique-overgroup classification

**Status: WRITTEN, source-conditional, UNREVIEWED.** For every prime r>7, in A_(2r) any three proper-subgroup indices include a pair with gcd greater than 7. Consequently no seven such indices can have every pairwise gcd 7, and eight disjoint cosets satisfy the Sun8 index conclusion. The proof imports only the classical Jordan prime-cycle theorem (Theorem 1.1 of Gareth A. Jones, https://arxiv.org/html/1209.5169v1), together with elementary Sylow, block-action and alternating-group facts. Unlike the previous all-degree candidate, it does **not** import Theorem 2(i)(b) of arXiv:2307.13976v2. It reconstructs the needed half-prime overgroup statement directly; this is a proof-source simplification, not a priority or novelty claim.

This is a new prospective source argument, not a change to f116, earlier frozen packets, any historical hold or any accepted verdict. Before the previous all-degree candidate or a successor using it, read the following in order: `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` SHA `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`; `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` SHA `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04`; `frontier-20261028-alternating-p7-cardinality-addendum-v1.json` SHA `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218`. The old candidate's n≤13 seven-index claim is false and is not imported here. The author's nonblind incidental cross-topic display remains disclosed; no such excerpt is used.

## 1. Sylow subgroup and its supports

Let the disjoint r-sets A and B partition the 2r points. Take x and y to be r-cycles supported on A and B respectively. Both cycles are even. The group R=⟨x,y⟩ is isomorphic to C_r×C_r and is a Sylow r-subgroup of A_(2r), since v_r((2r)!/2)=2. Set M=(S_A wr S_2)∩A_(2r), the setwise stabilizer of the unordered partition {A,B}; it is proper and contains R.

We claim that **every proper subgroup H containing R lies in M**. If H is intransitive, its orbits are unions of the two R-orbits A and B, so they are precisely A and B and H lies in M.

Now suppose H is transitive. If H is primitive, Jordan applies to the r-cycle x, which fixes r≥11≥3 points; hence H contains A_(2r), contrary to properness. Thus H is imprimitive. In any nontrivial block system, the block size divides 2r and is neither 1 nor 2r; since r is prime, it is 2 or r.

If the block size is 2, there are r blocks. The permutation of the blocks induced by x has order dividing r. If nontrivial, it is an r-cycle of the blocks, and therefore moves all 2r points: no point in a moved block can remain fixed. This contradicts that x moves only r points. If x fixes every block setwise, its restriction to each two-point block has order dividing both r and 2, hence is trivial, again a contradiction. Block size 2 is impossible.

If the block size is r, there are two blocks, and x and y each fix both blocks setwise because their odd order cannot induce a transposition. The r moved points of x must then all lie in a single block, so A is that block and B is the other. Hence H preserves {A,B} and H≤M. This finishes the claim. In particular, M is itself the unique maximal overgroup of this Sylow subgroup: a proper larger overgroup would also have to lie in M. This is a derivation under Jordan, not a source-proof reconstruction of the 2024 classification.

## 2. Index collision

The index of M in A_(2r) is binomial(2r,r)/2: S_(2r) acts transitively on unordered splits into two r-sets, and the stabilizer contains an odd transposition within A, so A_(2r) is also transitive. This index is at least r>7. If an index [A_(2r):H] is prime to r, H contains some Sylow r-subgroup; by Sylow conjugacy we may conjugate H to contain R, so its index is divisible by [A_(2r):M]>7. Consequently two r-free indices cannot have gcd≤7. Two indices divisible by r cannot have gcd≤7 either, since r>7. Among any three indices, two are in the same category, proving the assertion.

## 3. Review boundary and combination

This supplies a replacement proof for the prime m=r part of Section 4 of `frontier-20261028-alternating-all-degrees-p7-v1.md` SHA `6c22ef729ab54ba297b282e5923a749c186aab9c407ec9fc1f975d0e3af2227a`. If independently accepted, that proof's n≥14 no-four-index conclusion would depend on Bertrand and the stated Jordan/Jones theorems, not on the 2024 unique-overgroup classification. The separate n≤13 certificate-based Sun8 candidate and the seven-index A7 exception keep their own scopes and review obligations. No public source proof, separate group-family candidate, all-simple result, or novelty assertion is certified here. A disjoint reviewer should attack the imprimitive action of x on two-point blocks, the unordered partition index, Sylow conjugation, and the exact Jordan hypothesis.
