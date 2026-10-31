# Diverse signed swaps in the `R=3p−4` band

Owner **MathOlson-2-2**. Native `/bin/date` immediately before writing: **Wed Oct 28 18:06:44 PDT 2026**. This is a written new-mechanism candidate and independently bounded actual-word check, not an independent peer review, formal proof, novelty clearance or closure of the full count band. It does NOT use the pending high-band candidate as a premise.

## 1. Exact theorem and no-selector residual

Let p>=5 be prime. Let W be an actual ordered `D_(2p)` word of length `4p−1`, with exactly `R=3p−4` rotations and `F=p+3` reflections. Fix ANY two actual reflection positions i<j, and sign each rotation exponent x as −x if it lies strictly between i,j, and +x otherwise. Let S be the resulting signed multiset, let M be its largest multiplicity, and choose a value x of multiplicity M.

The original word has an identity selector of exactly2p occurrences USING THIS SPECIFIED reflection pair if either:

1. S has at least three distinct values and `M<=2p−3`; or
2. `M=2p−2` and two distinct other values y,z obey `y−x != ±(z−x)`.

In particular the original no-selector residual must satisfy for EVERY actual pair one of the following: signed support has at most two values; OR `M>=2p−1`; OR `M=2p−2` with all nonmajority values belonging to a single opposite pair `{x+d,x−d}`. This is only a necessary restriction: no avoiding word is asserted and no conclusion is drawn for any pair failing the sufficient conditions.

The mechanism is not packet-lift or a long-reflection-run argument. It uses only original rotation occurrences, their ACTUAL interval signs, and two genuinely different swap lengths.

## 2. An exact inverse lemma for p−2 arbitrary nonzero swaps

Let `d_1,...,d_(p−2)` be ANY nonzero F_p elements, with no zero-sum-free assumption. Let A be their subset-sum set. Then |A|>=p−1; if |A|=p−1, all d_i belong to `{d,−d}` for one nonzero d. Consequently, if any two d_i are not equal up to sign, A is ALL of F_p.

Proof. A proper nonempty subset of F_p strictly grows after union with a translate by a nonzero element, because such a translate generates F_p. Hence |A|>=p−1. Suppose A misses exactly m. Fix i, and write B_i for the subset sums excluding d_i. Growth gives `|B_i|>=p−2`, and `B_i,B_i+d_i⊆A`. If |B_i|=p−1 then both are A, implying A=A+d_i, impossible. Therefore `|B_i|=p−2` and its exact complement is `{m,m−d_i}`.

If d_i and d_j are distinct, let C be subset sums after omitting both. Since p>=5, the remaining p−4 nonzero entries give `|C|>=p−3`. But `C⊆B_i∩B_j=F_p\{m,m−d_i,m−d_j}`, so C is EXACTLY that complement. Also `C+d_i+d_j⊆A`, so `m−d_i−d_j∉C`. It is one of the three missing values. Equality to `m−d_i` or `m−d_j` would give d_j=0 or d_i=0; hence it equals m, and `d_j=−d_i`. Thus any two unequal increments are opposites. QED.

## 3. Actual disjoint pair construction

A multiset of N values with maximum multiplicity K has `min(floor(N/2),N−K)` disjoint unequal pairs: greedily pair occurrences from the two largest piles. After one pair, either the maximum drops, or three piles shared the maximum and the remaining `N−K` bound is still at least the old pairing bound minus one. This is elementary complete-multipartite matching, not an imported computational result.

The R signed values use only p symbols, and R=3p−4>2p, so M>=3. Suppose condition1 holds, and pick a most frequent value x. The total number of non-x occurrences is at least `R−M>=p−1`, and there are at least two non-x values.

* If y,z have differences from x that are not opposite, select two DISJOINT unequal signed pairs `(x,y)` and `(x,z)`, using two distinct x occurrences. Their swap differences are not equal up to sign.
* Otherwise all non-x values lie in `{x+d,x−d}` and both are present. Since their total multiplicity is at least p−1>=4, one, say y, occurs at least twice. With z the other, select `(x,y)` and `(y,z)` disjointly. Their lengths are d and 2d up to sign; `2d != ±d` because p>=5.

After removing these four occurrences, the remaining multiset has length `3p−8` and maximum multiplicity at most `2p−4`. The latter is immediate unless an untouched pile had size `2p−3`; such a pile cannot coexist with the original x-pile of size `2p−3`, because their total would exceed R. In the second case the x-pile loses one, and in the first it loses two. Thus the pairing formula gives at least `p−4` more disjoint unequal pairs: both `floor((3p−8)/2)` and `(3p−8)−(2p−4)` are at least p−4.

Under condition2, M=2p−2 is the unique majority, and two nonmajority values have non-opposite differences from x. Select `(x,y),(x,z)` as in the first case, decreasing x to2p−4; all other piles together originally had only p−2 occurrences. The same extension gives p−4 further pairs.

In either case we obtain p−2 disjoint unequal pairs with at least two swap differences not equal up to sign. Their subset-sum support is all F_p by §2. Omit ONE member from each pair and retain every other rotation. Exactly p−2 of the original 3p−4 rotations are omitted, so `2p−2` remain. Their signed sum, together with the specified actual reflections `r^(y_i)s,r^(y_j)s`, has exponent

`sum(retained signed values)+y_i−y_j`.

Choose the omission sum to make this zero. The two actual reflections plus the retained actual rotations are distinct original indices, in original order, and total2p. QED.

## 4. Boundary fixture, not an avoidance claim

For every p>=5 and λ∈F_p, concatenate the actual occurrences

`[s, r^λ s] · [2p−2 copies of 1] · [p−3 copies of r] · [one r^2] · [p+1 copies of s]`.

It has R=3p−4 and F=p+3. For its first two reflection positions, the signed multiset has `M=2p−2` copies of 0 and nonmajority values1,2, whose difference classes from 0 are not opposite. The theorem applies at the exact boundary omitted by condition1.

An independently visible selector also exists: choose t copies of r and ε copies of r², where `0<=t<=p−3`, `ε∈{0,1}` and `t+2ε=λ` as an integer representative in `{0,...,p−1}`; these sums cover all such representatives. Fill to `2p−2` rotations with zero-exponent occurrences and select the first two reflections. The exponent is λ−λ=0. This is a solvable fixture, not a counterexample or a novelty claim.

## 5. Actual checks and explicit boundary

Exact producer `frontier-20261028-dihedral-three-value-experiment.py`, SHA256 `4ffcd690424145573542d0bd1ca0701f70a70566014f03ee72fca2b056d86f70`, generated 90 full original words at p=5,7,11 (30 each), fixed seed2026102809, and saved `frontier-20261028-dihedral-three-value-results.json`, SHA256 `daee5be28c8620a64f61c567b620ee7ca288c52533baf92862f48ecebe07f429`. Across all 4,920 actual reflection pairs, 4,438 met the sufficient condition; 482 did not and were NOT decided.

Independently written checker `frontier-20261028-dihedral-three-value-checker.py`, SHA256 `7ee50a9c47bb92ea524e06919ef800437fc6fad6a62deddfdfc97547ce962208`, imports no producer code. Actual output `frontier-20261028-dihedral-three-value-check-results.json`, SHA256 `2032bbc7e38b3881594f6a2082f32be6e1331af07b17718d58b4608377c6816d`, reports `PASS_INDEPENDENT_DIVERSE_SWAP_CHECK`: all4,920 pair classifications were recomputed; all4,438 qualifying selectors' distinct increasing original indices were directly multiplied; four boundary fixture words p=5,7,11,13 supplied 284 qualifying pair selectors that were likewise directly checked. A duplicate selected index, reused pair index, and false-eligibility mutation were rejected for their intended reasons.

The checker also exhausted ALL 2,64,7776 nonzero swap tuples of length p−2 for p=3,5,7. Among them the one-missing support counts were 2,16,96 and the all-field support counts 0,48,7680; every one-missing tuple had all entries equal up to sign. This is finite corroboration of §2, not a proof for arbitrary primes.

The necessary residual in §1, p=3, all other rotation-count bands and the original all-group ordered Olson theorem remain open. No L_RES implication, general avoiding family, independent-model-family, formal or novelty claim is made.

**END — R=3p−4 diverse-swap theorem, all-pair residual and exact checks.**
