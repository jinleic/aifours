# Exact binary quotient-run criterion for the separated-packet ordered selector

Owner **MathOlson-2-2**, original math-2 slot.
Actual native `/bin/date` observed before this write: **Wed Oct 28 17:07:32 PDT 2026**.
**NEW written structural characterization with bounded exhaustive checks; not an all-word selector theorem or novelty claim.**

## 1. Original problem and exact result

The original ordered Olson target concerns EVERY word of length2n−1 in EVERY finite group G of order n, and an identity subsequence of EXACTLY n original occurrences in increasing-index order.
Here G has an ACTUAL index-two normal subgroup K of order k, so n=2k and the actual original word has length4k−1. No all-group claim is obtained by assuming such a subgroup exists.

Write its quotient image as a binary word. A **chronologically separated equal pair family** consists of pairs `(i_1,j_1),…,(i_t,j_t)` with

`i_1<j_1<i_2<j_2<⋯<i_t<j_t`

and equal quotient letters at each pair's two ORIGINAL positions. The pairs are actual, and no other pair may lie inside their span.

**Theorem A — exact saturation classification.** A binary word of length4k−1 has `2k−1` such pairs IFF its maximal equal-letter runs have either:

1. exactly ONE run of odd length; OR
2. exactly THREE odd-length runs, these three runs are consecutive among ALL runs, and the middle one has length1.

If O(K) is available — every length2k−1 K-word has an increasing-index identity selector of exactly k occurrences — then EVERY original G-word whose quotient pattern satisfies this criterion has an ORIGINAL-order identity selector of exactly2k occurrences.
This is a precisely characterized proper word class. It does not assert that every quotient pattern satisfies the criterion, that any failed pattern is an avoiding word, or that all finite groups possess an index-two normal subgroup.

**Theorem B — exact count.** Among all binary words of length4k−1, precisely

`4k · 2^(2k−1)`

have the separated-pair saturation property. Their fraction of all binary words is

`k / 2^(2k−2)`.

The count concerns quotient LETTER PATTERNS only; it is not the number of nonabelian group words, not a probability model for research, and not a counterexample count for the original conjecture.

## 2. Exact original-object caller from any saturated binary pattern

Each equal binary pair has identity product in G/K, so its ACTUAL ordered two-letter product lies in K.
The `2k−1` pair spans are chronologically separated. These actual packet products form a K-word of length2k−1.
Applying the explicitly stated O(K) hypothesis gives k increasing packet indices whose product is1 in K.
Their chronological union consists of exactly2k original occurrences, and its ordered G-product is precisely that packet product, because no selected pair interleaves another.
Hence the original G-word has the required selector.

This proof does not infer an unproved flattening of interleaved packets. The O(K) assumption is an ACTUAL word theorem, not an unordered quotient constant or an arbitrary kernel-label assignment.
For finite p-group K, prior ordered p-group existence is publicly stated in Dimitrov's 2004 paper, but that paper's proof is not used here; the conditional caller remains valid for ANY K with O(K).

## 3. Necessity of the run classification, including the single unused position

Set `N=4k−1`, `M=2k−1`, so N=2M+1.
Any M separated pairs use2M endpoints and leave exactly ONE original position unused.
Their disjoint inclusive spans each have length at least2. The sum of span lengths is at most N=2M+1.
Therefore exactly one of the following occurs:

- every span has length2, and the unused position lies outside all spans; or
- one span has length3, every other span length2, and the sole unused position is inside that length3 span.

In the first case all pairs consist of adjacent equal letters. Every full run other than the run containing the unused position is tiled by such pairs and has even length; the run containing it has odd length. Thus there is exactly one odd run.

In the second case the length3 span has equal endpoints. Its three quotient letters are either `aaa` or `aba` with a≠b.
If `aaa`, that whole triple lies inside one run. Every other portion of that run and every other run is tiled by adjacent equal pairs, so there is exactly one odd run.
If `aba`, the middle b is an entire singleton run, and the two endpoint a's belong to the two neighboring runs. Every remaining portion of those two runs is tiled by adjacent equal pairs, so both neighboring runs are odd. Every other run is even. Thus there are exactly three odd runs, consecutive among ALL runs, and their middle run has length1.
No case is omitted by allowing the unused position at either end of the word, a length1 run, or additional even-length runs outside the three odd runs.

## 4. Sufficiency and exact actual pairing

If there is exactly one odd run, pair consecutive equal letters within every run and leave one actual occurrence in the odd run unused. This gives M separated equal pairs.

If there are exactly three odd runs as in item2, pair adjacent letters within every OTHER run. In the first of the three odd runs leave its LAST occurrence, and in the third leave its FIRST. The middle odd run is a singleton; pair those two outer leftover a's across it, consuming the actual `aba` span and leaving the middle b unused. Pair all remaining occurrences within the two outer runs consecutively.
The spans are chronologically separated and equal at their endpoints; exactly one original position is unused and there are M pairs.
This proves Theorem A in both directions.

The construction uses the quotient letters at the actual ordered occurrences, not a freely rearranged binary multiset. It does not assign, replace or assume anything about their kernel coordinates.

## 5. Count the qualifying binary words by run compositions

For general odd length `N=2M+1`, a binary word is determined by its first bit and its positive run lengths. There are two possible first bits.

### One odd run

Let e be the number of even runs, 0≤e≤M. Choose the odd run's position among them in e+1 ways.
Write the odd length as `2c+1` with c≥0, and each even length as `2b_i` with b_i≥1.
The length equation is `c+∑b_i=M`.
After setting b_i'=b_i−1, the number of nonnegative solutions is `binom(M,e)` by the elementary stars-and-bars count.
Thus this case contributes

`2∑_(e=0..M)(e+1)binom(M,e)=(M+2)2^M`.

The binomial identities follow by counting subsets and pairs (subset, marked element), not from a sampled computation.

### Three consecutive odd runs with a singleton middle

Let e be the number of other, necessarily even runs. The three consecutive odd runs form one group that may occupy any of e+1 positions among the even runs.
Write the outer odd lengths as `2c+1` and `2d+1`, the middle as1, and the even lengths as `2b_i` with b_i≥1.
The length equation is `c+d+∑b_i=M−1`.
After b_i'=b_i−1, for e≤M−1 the number of nonnegative solutions is `binom(M,e+1)`.
Thus this case contributes

`2∑_(e=0..M−1)(e+1)binom(M,e+1)=M 2^M`.

The cases are disjoint because their numbers of odd runs differ. Their total is

`(2M+2)2^M=(N+1)2^M`.

Substitute M=2k−1,N=4k−1 to obtain Theorem B. For k=1 the formula is still valid; the second sum/empty-run boundary is interpreted normally and the trivial-kernel actual caller remains conditional as stated.

## 6. What this proves and does not prove about the original bridge

The general separated-packet transport was already written-supported in the prior parent disposition. The new content here is the exact run-pattern IFF, its actual word-class caller and its closed symbolic pattern count. Whether this elementary characterization is already in the literature is **not** established; no novelty or priority claim is made.

The alternating quotient word has all runs singleton. For larger k it does not satisfy the criterion, and it illustrates a limitation of THIS certificate only. It is not asserted to be an original group avoiding word, because a selector need not be a union of these separated pairs.
The exact fraction `k/2^(2k−2)` tends to zero as k grows, so the certificate by itself addresses a small structured pattern class. That combinatorial observation is not an all-word no-go, an empirical distribution claim for input words, or evidence that the original conjecture fails.

Any further full original solution must either supply selectors for the remaining quotient patterns or use a different valid all-word mechanism. The result is not a substitute for the old odd-prime dihedral intermediate bridge, the mixed-prime unrestricted problem or the all-finite-group assertion.

## 7. Bounded actual experiment and its exact verification scope

`frontier-20261028-binary-run-classification.py`, SHA256 `6f74f35ee9c1da98ca5f475492331ec98ae280eda64b65f75d6c0c1804b38da0`, was run once after the source was complete.
Its saved exact result is `frontier-20261028-binary-run-classification-results.json`, SHA256 `79689938e5d6097c88ce50cef866f37c06b6de32343631e3cf51620a778b3747`.
The producer uses ONLY standard-library integer/bit operations. It compares two distinct finite procedures: a direct dynamic program over original interval endpoints for the maximum separated-pair count, and the run-based classification. It also checks the two separate symbolic count expressions at each bounded domain.

Actual output:

| k | binary words checked | saturation words |
|---:|---:|---:|
| 1 | 8 | 8 |
| 2 | 128 | 64 |
| 3 | 2,048 | 384 |
| 4 | 32,768 | 2,048 |

The run completed with `PASS_FINITE_EXHAUSTION` and no mismatches on those four finite domains. This is a bounded combinatorial cross-check, not an independent checker written by another model, a theorem prover, exhaustive arbitrary-k verification or proof/novelty acceptance. The full all-k written proof is §§3–5.
No original group avoiding word was produced or claimed.

The latest owner direction authorized this bounded local scientific calculation prospectively. No old quarantined outcome is accepted or reclassified, no external model/paid API was used, and no deletion, Git push, publication or infrastructure mutation occurred.

**END — exact run-class criterion and original-order conditional caller.**
