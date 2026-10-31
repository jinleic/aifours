# Twelve-step alternating P7 exclusion by alternating-block projection

**Status: WRITTEN candidate, conditional on the cited public A_r classification and earlier written base/window induction; not independently reviewed or accepted.** Let r≥419 be a prime which is not a prime-power repunit (q^d−1)/(q−1), d≥2, and assume r+1>7·12!. Then A_(r+12) has no seven proper subgroups whose indices have all pairwise gcd exactly 7. Together with the prior t≤11 packet this excludes direct P7 in all twelve consecutive simple groups A_(r+1),…,A_(r+12) under this size bound. The earlier elementary count supplies infinitely many eligible r. This is not a claim of published priority, historical novelty, unrestricted Sun8, or all-alternating/global closure.

The genuine new representation is to continue past an intransitive orbit by projecting to the alternating group on its large block. A proper projection contributes another actual subgroup index; a full projection forces a large alternating subgroup in the original subgroup. This extra information excludes the six-type integer patterns which survive a first-intransitivity-only relaxation.

## 1. Dependencies and basic notation

Theorem 2(i)(d) of https://arxiv.org/html/2307.13976v2 states that a fixed Sylow-r subgroup of A_r has unique maximal overgroup M0=AGL1(r)∩A_r for the eligible r here. Its order is r(r−1)/2, so [A_r:M0]=(r−2)!. The source theorem and proof DAG have not been independently checked.

The common-index base, actual point-stabilizer descents, nonoverlapping typed numerator windows and elementary eligible-prime count were written in `frontier-20261028-alternating-interval-packing-p7-v1.md`, SHA `cc6aa191d75c2658a6f93e92468d6ac9aab178c1cfc54effa3c0e50e1cc11e4f`, and its named ancestors. We use those written results conditionally and rederive the additional projection step below. Standard simplicity/order of A_n, Sylow, Lagrange and orbit-stabilizer are also used. No Sun7 import is made.

The writer had nonblind Sun exposure and the incidental cross-topic display recorded in `frontier-20261028-incidental-cross-topic-search-frontier-v1.json`, SHA `d939059c390641a282d495bb2f8a5dff6a486380fec6cc417cb54b7dc93e8dec`. No such excerpt is an input here, and no historical hold is changed.

## 2. The actual alternating-block projection lemma

Let H<A_n contain a fixed r-cycle R, with n=r+j<2r. Suppose H is intransitive and U is its orbit containing the r moved points. Put m=|U|=r+j−u and V=U^c, |V|=u≥1. Let B=(S_U×S_V)∩A_n and define
\[K=H\cap(A_U\times A_V),\qquad P=\pi_U(K)\le A_U.\]
Then R≤K, P contains R, and
\[\binom nu\,[A_U:P]\ \mid\ [A_n:H].\tag{1}\]
For u=1, B=A_U, K=H and (1) is immediate. For u≥2, A_U×A_V has index 2 in B and [H:K] is 1 or 2. Thus
\[[A_n:H]=\binom nu\frac{2}{[H:K]}[A_U\times A_V:K],\]
and [A_U:P] divides the final index by projection. The quotient 2/[H:K] is integral.

Moreover P is transitive on U. Indeed π_U(H) is transitive, P is a normal subgroup of it of index at most 2, and an intransitive P would have exactly two equal orbits of size m/2<r. This is impossible because R≤P has an orbit of size r.

If P=A_U, then A_U×1≤H. To see this, Q={a∈A_U:(a,1)∈K} is normal in A_U. Simplicity makes Q either A_U or 1. If Q=1, K injects into A_V while surjecting onto A_U, impossible since m≥r>u and |A_U|>|A_V|. Thus Q=A_U. For u=1 this says H=A_U and [A_n:H]=n. For u≥2 the quotient B/A_U is S_V, so [B:H] divides u!; no stronger quotient classification is needed.

If P<A_U, then P is an actual proper r-containing subgroup of A_U and its r-free index can be followed recursively. Formula (1) preserves every extracted binomial factor in the original index. Transitive point-stabilizer descents preserve index; intransitive steps strictly decrease the number of R-fixed positions. The resulting numerator windows are disjoint within a chain. The chain terminates either with P=A_U at an intransitive step, or at a proper r-containing subgroup of A_r, in which case the original index is divisible by F=(r−2)!.

## 3. A factorial-terminal index cannot appear in a seven-pattern

A proper subgroup of A_N, N≥5, has index at least N: otherwise its core-free coset action would embed A_N into S_(N−1), but N!/2>(N−1)!. Suppose one of seven indices with all pairwise gcd 7 is divisible by F=(r−2)!. Because F is divisible by 7² and by every prime at most r−2, each of the other six indices is 7 times an integer >1 whose prime divisors are at least r−1; these six cofactors are pairwise coprime.

All those prime divisors divide |A_(r+12)|, so lie at most r+12. The only possible primes in [r−1,r+12] are r and primes among r+2,r+4,r+6,r+8,r+10,r+12. At least two of those six odd numbers are divisible by 3: r+2 and r+8 when r≡1 mod 3, or r+4 and r+10 when r≡2 mod 3. Thus there are at most five possible distinct primes, but six pairwise-coprime cofactors >1 need six. Contradiction. Hence no factorial-terminal index can occur in a P7 pattern.

## 4. Multi-window and one-cell alternatives

Set t=12 and n=r+12. Among seven P7 indices at least six are r-free. For each choose an actual complete projection/descent chain. By Section 3 none terminates in the factorial case, so every chain terminates at a full large-block projection. A chain with only **one numerator cell** has exactly one intransitive step with u=1; it then terminates with H=A_(r+j−1) and its original index is r+j. If j<12 this contradicts the minimum-index bound in A_n. Thus the only possible one-cell chain is j=12, namely a point-stabilizer index n; in a P7 pattern this requires 7|n. There is at most one such label, since two equal indices n>7 cannot have gcd 7. Every other r-free chain consumes at least two numerator cells.

For two different labels, shared cells are impossible: if both windows contain h, then (r+h)/gcd(r+h,12!)>7 divides both indices, by the earlier Euclidean denominator argument and r+1>7·12!. Windows within one chain are disjoint because each intransitive projection passes to a smaller block and subsequent endpoints lie before its window. Thus all cells used by the selected labels are disjoint within {1,…,12}.

For an odd index every extracted binomial is odd. An odd binomial window contains at least as many even positions as odd positions: if its endpoint j is even, this is immediate from the alternating positions; if j is odd, r+j is even, and an odd binomial forces even window length. An odd two-cell chain is therefore either two singleton windows at even positions or one adjacent length-two window.

For an adjacent length-two window, its binomial is odd exactly when the numerator factor at its unique odd position c satisfies r+c≡2 mod 4. Allowed edges therefore form at most three disjoint **clusters**: centers 1,5,9 when r≡1 mod 4, and centers 3,7,11 when r≡3 mod 4. Two edges in the same cluster share its center, so at most three allowed odd adjacent windows can be pairwise disjoint.

## 5. No point-stabilizer label

Choose any six r-free labels. If none is the one-cell point label, each uses at least two disjoint cells; hence all six use exactly two cells and fill all twelve positions. At most one index is even, so at least five are odd. An odd two-cell label either uses two even singleton positions or one allowed odd adjacent window. If q of those five use two even positions, they consume 5+q of the six even positions, so q≤1. At least four therefore require distinct allowed odd adjacent windows, but Section 4 permits at most three. Contradiction.

## 6. With the point-stabilizer label

The point label has index n=r+12, is odd and requires 7|n. Choose it and five further r-free labels. These five use at least two cells each; at most one is even. There are five available even positions, 2,4,6,8,10. Among at least four odd nonpoint labels, each uses at least one even position; at most one can use two or more. Any odd label using exactly one even position and at least two cells is one allowed odd adjacent window. As there are at most three such windows, there are exactly four odd nonpoint labels: three adjacent-window labels and one label using exactly two even positions. The fifth nonpoint label is even.

There is at most one spare cell: 1 point cell + 6 adjacent cells + at least 2 for the two-even label + at least 2 for the even label totals 11. The two-even odd label can therefore use only 2 or 3 cells. If it uses an additional odd adjacent window plus an even singleton, it would give four disjoint allowed adjacent windows, impossible. If it is one odd length-three binomial window ending at even j, then C(r+j,3) is odd only when r+j≡3 mod 4; its central odd position c=j−1 then satisfies r+c≡2 mod 4. The length-three window occupies c and both neighbors, blocking one whole allowed-edge cluster and leaving at most two clusters for the other three adjacent labels. This too is impossible. Three singletons cannot be an odd label with exactly two even positions, since a singleton at an odd position contributes an even factor. Thus the two-even label consists of **two even singleton windows**.

Every available even position is now used either by that double-singleton label or by one of the three odd adjacent labels. In either case its label's index is divisible by r+k: for an odd adjacent binomial the division by 2 removes a factor from the even numerator r+odd, leaving the odd numerator r+k intact. The two positions whose r+k are divisible by 3 must belong to the same label, since two distinct indices both divisible by 3 and 7 would have gcd≥21. An adjacent label uses only one even position, so the double-singleton label must occupy exactly those two positions.

- If r≡1 mod 4, the three odd-edge clusters have centers 1,5,9. Center 1 has only edge {1,2}. When r≡1 mod 3, the 3-divisible even positions are 2 and 8, so the double label blocks that compulsory edge. When r≡2 mod 3 they are 4 and 10, so edge {1,2} occurs; its binomial C(r+2,2) contains (r+1)/2, divisible by 3, and collides with the double label.
- If r≡3 mod 4, the centers are 3,7,11. Position 12 is occupied by the point label, so the center-11 edge must be {10,11}. When r≡2 mod 3, the double label occupies 4 and 10 and blocks that edge. When r≡1 mod 3 it occupies 2 and 8; C(r+11,2) contains (r+11)/2, divisible by 3, and collides with the double label.

All cases contradict the assumed gcd 7. This completes the t=12 written argument.

## 7. Actual finite controls and remaining boundary

`frontier-20261028-alternating-projection-check.py`, SHA-256 `f26fe71d35a219b085c6bd8630d98170d9bc73a56fd0b615d525e637ce879d1c`, 112 LF / 3610 bytes, ran at 19:02:28 PDT on 2026-10-28. It found four eligible primes above 7·12!, one in each combination of r mod 4 and r mod 3 with 7|(r+12), and exactly checked the finite no-point and point-window packing relaxations using parity and 3-divisibility. It does not construct or enumerate actual subgroups, prove the projection lemma, validate the source classification or replace written review.

**Review-critical:** independently reconstruct the K/P index formula and transitivity, the full-projection normal-subgroup argument, the factorial-prime count, the one-cell terminal classification, the length-three cluster argument, and all four residue cases. No earlier held source is adopted; no formal or independent proof review is claimed.
