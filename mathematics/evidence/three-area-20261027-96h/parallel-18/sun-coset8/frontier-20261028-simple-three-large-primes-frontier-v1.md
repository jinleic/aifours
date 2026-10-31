# Exact saturation frontier with three primes above seven

**Status: WRITTEN, UNREVIEWED.** Let S be a finite nonabelian simple group whose order has exactly three distinct prime divisors p,q,r greater than 7. If eight pairwise disjoint left cosets have every pairwise subgroup-index gcd at most 7, their actual subgroup indices have the four-type structure in §2 below. In particular exactly five indices are pairwise-gcd-6 indices of specific forms, at most two of the eight indices are divisible by 7, and each of the other three indexed subgroups contains full Sylow subgroups for all of p,q,r. No common choice of these Sylow subgroups is claimed. **Consequently, such an S satisfies Sun8 if any of 2,3,5,7 does not divide its order.** The remaining four-pattern structural statement is a necessary condition, not a constructed configuration or an unrestricted k=3 exclusion. No all-simple theorem, novelty clearance or acceptance is claimed.

## 1. Inputs and finite-simple index bound

Read the complete overlays in order before affected sources: `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` SHA `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`, `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` SHA `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04`, and `frontier-20261028-alternating-p7-cardinality-addendum-v1.json` SHA `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218`. This packet uses the **unreviewed** written support/resource argument in `frontier-20261028-small-prime-support-sun8-v1.md` SHA `619c36eb5a029e97095b94f3d845772e8f4852fae05b60e33dbee55355e59ec8`; it does not import Sun7/R8, Jones or CFSG for §§1–3. The author's earlier finite type check was nonblind corroboration, not a proof input. Incidental cross-topic display is separately disclosed and unused.

Let p<q<r. Then r≥17. Every proper subgroup of S has index at least r: its coset action is faithful by simplicity, so |S| divides the factorial of the index, and r divides |S|. In particular no index is 12. Coprime-index cosets intersect, so every pairwise index gcd is in 2,…,7.

The cited support proof applies with k=3 and bounds the number of cosets by 8. We now analyze equality instead of inferring an exclusion. Its small supports are subsets of {2,3,5,7}, and a prime greater than 7 can divide at most one index.

## 2. Equality forces five 2–3-core indices and one of four patterns

If every index shares one small prime, the resource proof gives at most 7 labels for common prime 3,5 or 7. For common prime 2 it gives seven one-use resources 8,9,5,7,p,q,r and at most one resource-free index, which must be 12. Equality at eight would require that index 12, impossible by §1. Thus no small prime divides all indices.

In the no-common-prime case, the cited written type lemma gives at most four distinct small supports; every support has size at least two, and only {2,3} can repeat. The {2,3} labels each use one of the five one-use resources 4,9,p,q,r, so there are at most five. Equality at eight therefore forces exactly five {2,3} labels and exactly three other, nonrepeated support types. It also forces each of the five resources 4,9,p,q,r to occur exactly once and on a different {2,3} index. Consequently, up to relabeling, the five core indices are

\[3\cdot 2^{a},\quad 2\cdot3^{b},\quad 6p^{e_p},\quad6q^{e_q},\quad6r^{e_r},\]

with a≥3, b≥2 and e_p,e_q,e_r≥1; every pair among these five has gcd exactly 6. (The lower bound a≥3 follows because index 12 is impossible.) None of p,q,r can divide any of the other three indices, since each already divides its dedicated core index and any shared prime greater than 7 would violate the gcd bound.

The written four-type argument in the cited source gives exactly these possibilities for the other three small supports; e.g. `25` means the support {2,5}, not an index equal to 25:

| Case | Other three small supports | Number of indices divisible by 7 |
|---|---|---:|
| I | 25, 27, 357 | 2 |
| II | 25, 35, 237 | 1 |
| III | 27, 37, 235 | 2 |
| IV | 35, 37, 257 | 2 |

For completeness, the list follows by taking a four-type, empty-common-intersection family containing {2,3}. It must contain a triple. If the triple is {2,3,c} with missing d∈{5,7}, the only way to reach four types is to add {2,d} and {3,d}, giving II or III. If the triple omits 2 or 3, the other three types must be the three pairs joining the omitted prime to each triple member, giving I or IV. No support of size 4 is compatible with empty common intersection, and pair types alone have at most three members.

Every row contains 5 and 7, and the five core indices contain 2 and 3. Therefore a counterexample in this k=3 class requires all four primes 2,3,5,7 to divide |S|. If any one of them is absent, no table row is possible, proving the Sun8 subgroup-family consequence stated at the start. This consequence uses only the written support lemma and elementary simple-group coset actions, not the optional Sun3 or Sun7 statements.

For illustration only, the classical simplicity and order formula for PSL2(67) give |PSL2(67)|=67(67²−1)/2=150348=2²·3·11·17·67, so this particular simple group lies in the stated family. Those classical PSL2 facts are additional named inputs for the example, not for the general result; their proofs are not replayed here. The integer factorization was checked in the author's eval kernel, and no novelty is claimed for this group.

Each of the three noncore indices has no prime divisor above 7 and is therefore a product of prime powers supported exactly on its displayed type. Its associated proper subgroup has index prime to p,q,r and hence contains some Sylow p-, q- and r-subgroups of S, respectively. Each subgroup associated with 6p^e is q- and r-free and contains some Sylow q- and r-subgroups. These are subgroup-by-subgroup statements: a common choice of Sylow subgroups across different vertices is neither assumed nor proved.

## 3. Boundaries and optional Sun3 filter

The table gives at most two indices divisible by 7. Hence, if the separate Sun7(S) statement is assumed, deleting one 7-divisible label leaves seven disjoint cosets with all pairwise gcds at most 6, a contradiction. This is a conditional consequence only; it does not replace an unconditional exclusion or re-prove Sun7. The prior R8 reduction was already known and is not credited as a discovery.

As a separate prospective published import, Zhu, *On Sun's Conjecture concerning Disjoint Cosets*, Theorem 1.1(k=3), says that among any three disjoint cosets some pair of indices has gcd at least 3. Its exact primary statement and bytes are pinned in `frontier-20261028-zhu-sun3-source-v1.json` SHA `c50fc9e9243bd7bfc2da2d1dfb87ca40d0069735c3098bc0cf03fd7fa8bb73a2`; the source proof has not been independently replayed. In case I, a core index 6p^e has gcd exactly 2 with each of the two indices of types 25 and 27. The published Sun3 statement therefore forces the gcd of those two indices to be 4 rather than 2, so both are divisible by 4. This is only an additional necessary condition; it does **not** rule out case I.

No claim is made that any of the four integer patterns is realizable by actual subgroups, that the subgroup/Sylow constraints are sufficient, or that the remaining three-large-prime simple families are solved. A disjoint reviewer should attack equality saturation, the four-type list, all prime-power forms and the Sylow statements, and check the optional Sun3 exponent condition independently. The high-prime condition, support lemma and source imports are not accepted merely by this report.
