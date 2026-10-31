# Small alternating degrees: explicit exact coloring and repeated-index analysis

**Status: WRITTEN-checked-in-kernel, CONDITIONAL, UNREVIEWED.** This separate successor attempts the Sun8 statement for A_n, 5≤n≤13, without importing the old Sun7 or R8 verdicts. Together with the unreviewed n≥14 result in `frontier-20261028-alternating-all-degrees-p7-v1.md` SHA `6c22ef729ab54ba297b282e5923a749c186aab9c407ec9fc1f975d0e3af2227a`, it gives a **conditional candidate** for Sun8 for every finite simple alternating group. Nothing here adopts either candidate, changes the previous direct-P7 proof, certifies a public source proof, implies Sun8 for every finite simple group, or claims priority. The earlier packet's conditional small-degree Sun7/R8 route remains a valid statement of its own scope and is not edited.

**Mandatory pre-source correction:** first read in full `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` SHA `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`. Read it before the all-degree candidate or any older source named there. Public imports, exactly as scoped by that candidate, are Bertrand, Jordan/Jones Theorems 1.1 and 1.2(k=2), and the 2024 odd-prime unique-Sylow-overgroup theorem for A_(2r). Those imports are needed for n≥14, NOT for the small-degree proof below. The familiar facts that A_n is simple for n≥5, that |A_n|=n!/2, Sylow's theorem, and elementary permutation-group facts are named classical inputs. No old Sun7/R8, held history, or incidental cross-topic snippet is an input. Nonblind incidental cross-topic display was previously disclosed in `frontier-20261028-incidental-cross-topic-search-frontier-v1.json` SHA `d939059c390641a282d495bb2f8a5dff6a486380fec6cc417cb54b7dc93e8dec`; no clean-cognition or historical rehabilitation claim is made.

## 1. Exact certificate and what it does—and does not—show

For each 5≤n≤13 define V_n as all positive integer divisors m of n!/2 with m≥n. Make a simple graph on V_n, joining **distinct** m,m' exactly when 2≤gcd(m,m')≤7. The following certificate partitions V_n into at most seven classes, each containing no edge:

- `frontier-20261028-small-alternating-sun8-colors-v1.json`, SHA256 `e43fedc2b3662b72313e8c5294bc9befa2a9529bb0e5b938fa2a6fec674ad3cc`, 1 LF / 18195 bytes. Each row supplies n, n!/2, and the complete explicit color classes.
- Author checker `frontier-20261028-small-alternating-sun8-colors-check-v1.py`, SHA256 `9127b4d4253608e0a628e26a600e3d46e20350f6b76b279d4caaa14bf1e058fc`, 65 LF / 2482 bytes. In the author's Python eval kernel it independently enumerated divisors by integer square-root trial divisors, checked exact set coverage and absence of duplicates, compared group orders with n!/2, and directly checked all 347034 within-class unordered pairs for absence of a gcd in 2,…,7. The SHA of the certificate bytes was checked. No external scientific process was launched. This is a separate implementation from the author's coloring generation but NOT an independent reviewer.

| n | Divisors m≥n | Color classes | Same-color pairs checked |
|---:|---:|---:|---:|
| 5 | 8 | 4 | 4 |
| 6 | 19 | 5 | 41 |
| 7 | 42 | 6 | 130 |
| 8 | 77 | 6 | 664 |
| 9 | 132 | 6 | 2143 |
| 10 | 231 | 6 | 6078 |
| 11 | 470 | 7 | 23029 |
| 12 | 709 | 7 | 54386 |
| 13 | 1428 | 7 | 260559 |

The certificate proves the graph's distinct-vertex clique number is at most the number of classes. **It does not itself rule out repeated indices 5,6,7**: the simple graph has no loops. Sections 4–6 deal with that gap explicitly. Author-only in-memory controls rejected an omitted index, duplicated index, split into eight colors, moving 22 into the class containing 42, and an incorrect factorial order for the intended checker reasons; these controls bypassed only the fixed-byte hash test in order to exercise validation. They do not replace independent certificate verification.

## 2. Elementary group lemmas

For a proper subgroup H≤A_n, its index m divides n!/2 and is at least n. Indeed the core of H is trivial by simplicity; the coset action embeds A_n into S_m, whereas m<n would give m!≤(n−1)!<n!/2. If two subgroup indices are coprime, every pair of their left cosets intersects: the index of the subgroup intersection is divisible by both indices and at most their product, hence equals their product, so the product of the two subgroups is the whole group. Thus in a proposed set of pairwise disjoint cosets with all pairwise index gcds at most 7, every pairwise gcd is in 2,…,7.

**Index-n star lemma.** In A_n, n≥5, any collection of at least three pairwise disjoint left cosets of index-n subgroups belongs to a common partition into n cosets of one index-n subgroup; the partition is either entirely left cosets or entirely right cosets. More precisely, after identifying a faithful degree-n coset action with the natural action of A_n, the collection consists either of events g(x)=y_i with one fixed x and distinct y_i, or of events g(x_i)=y with one fixed y and distinct x_i. A coset disjoint from r such events lies in the union of the n−r remaining events of the partition.

*Proof.* Fix one subgroup H of index n. Its coset action is faithful by simplicity, and its image is the unique index-two subgroup A_n of S_n. Any other index-n subgroup K is either transitive in this action, in which case HK is the entire group and every H-coset meets every K-coset, or intransitive. In the latter case an orbit of size u≤n/2 forces binomial(n,u) to divide n, impossible for u≥2 because binomial(n,u)>n; hence K fixes a point and is its full point stabilizer by order. Therefore every coset disjoint from the first is a point-to-point event g(x)=y in this same action. Any two such events with distinct sources and distinct targets intersect because A_n can realize any prescribed compatible two-point map: at least three points remain to adjust parity. Thus disjoint events must share their source or their target, and three or more mutually disjoint events have one common source or one common target. The n possible values of the other coordinate give the claimed partition. Inverting all group elements swaps source and target and preserves disjointness and coset indices.

For use below, if the partition consists of right cosets, first invert every set, thereby converting each original left coset into a left coset of a conjugate subgroup and the partition into left cosets. If a left coset C of K lies inside one event F of the resulting index-n partition, translating F to its subgroup identifies C with a coset of a subgroup of that index-n subgroup, of relative index [A_n:K]/n. If two such C inside the same F have ambient index gcd at most 7 and n∈{6,7}, their relative indices are coprime, so they intersect. (The ambient indices are multiples of n and their gcd must be exactly n.)

## 3. Degrees 8,…,13

All subgroup indices are at least n≥8. Two equal indices therefore have gcd at least 8, so under the contrary Sun8 hypothesis all eight indices would be **distinct**. They would form an eight-clique in V_n, contradicting the certificate's at-most-seven coloring.

## 4. Degree 5

The possible indices divide 60 and are at least 5: 5,6,10,12,15,20,30,60. The only possible repeated indices are 5 and 6; they cannot both occur in pairwise disjoint cosets since gcd(5,6)=1. If the repeated value appears r≤4 times, all other indices are distinct neighbors of its graph vertex and occupy at most the other three of the certificate's four colors, so there are at most seven cosets. If neither value repeats there are at most four.

Five cosets of index 5, or six of index 6, already cover the whole group by disjointness, leaving no room for an eighth. It remains to rule out five cosets of index 6 plus three others. Their distinct other indices must be chosen from 10,12,15,20,30,60 with all pairwise gcds between 2 and 7. The only possible triples are (10,12,15) and (12,15,20); their reciprocal sums are 1/4 and 1/5, respectively. But five index-6 cosets occupy 5/6 of the group, leaving density only 1/6. Both triples exceed that remainder. Thus A5 has Sun8.

## 5. Degree 6

The only index that can repeat is 6. Let r be its multiplicity. If r=0, all indices are distinct and the certificate gives at most five; if 1≤r≤3, the distinct other indices are neighbors of vertex 6 and occupy at most the other four colors, giving at most r+4≤7.

For r≥4 apply the star lemma. If r=4, invert if necessary so the four events have fixed source x; their complement is the union of two remaining fibers of g(x). Any additional coset aK is contained in that union, so the K-orbit of x has size 1 or 2. In the first case the entire coset lies in one remaining fiber, and at most one additional coset can lie in each fiber by the coprime-relative-index observation. In the second case K stabilizes a two-set, so its ambient index is divisible by binomial(6,2)=15; there can be at most one such coset since any two would have index gcd at least 15. Hence at most three additional cosets, and at most seven total. If r=5, at most one more coset can lie in the single remaining fiber; if r=6 the six fibers cover the group; r>6 is impossible by density. Thus A6 has Sun8.

## 6. Degree 7

The only repeated index possible is 7. If it occurs at most once, all indices are distinct and the six-color certificate gives at most six. Suppose it occurs r≥2 times. Each other index must be 7a with a>1 and a dividing 360=2^3·3^2·5, and the a values are pairwise coprime. At most two such indices occur: three pairwise-coprime a>1 would require one to be a power of 2, hence 2,4 or 8, but A7 has no subgroup of index 14,28 or 56, as follows.

Such a subgroup K has order 360/a, not divisible by 7, hence is intransitive in the natural degree-seven action. For an orbit of size u≤3, binomial(7,u) divides 7a; the values for u=1,2,3 are 7,21,35. Since a is a power of 2 only u=1 is possible, so K lies in A6 with relative index a. The simple group A6 has no subgroup of index 2 or 4, by the faithful-coset-action order bound. An index-8 subgroup would have order 45; its number of Sylow-5 subgroups divides 9 and is 1 modulo 5, hence is 1. It would normalize a C5, but the normalizer of a 5-cycle's C5 in S6 has order 20 and contains an odd element, so its intersection with A6 has order 10, impossible for a group of order 45. This proves the three claimed nonexistences.

If 2≤r≤5 there are therefore at most r+2≤7 cosets. If r=6, the star lemma leaves one index-7 fiber, which contains at most one additional coset by the coprime-relative-index observation; r=7 fills the group and r>7 is impossible by density. Thus A7 has Sun8.

## 7. Review boundary

The small-degree argument uses the displayed finite coloring as an exact certificate plus the written lemmas above. It is not a Lean proof, an independent checker run, a human-reviewed proof, an adoption, or a novelty clearance. Before any integration, an independently authored checker should reconstruct the divisor universe without using the author's generator or checker, verify the pinned certificate hash and every within-class gcd, and attack the small-index repetitions, index-n star lemma (including coset orientation/inversion), A6 index-8 obstruction, and the n=5 density triples. The n≥14 half additionally requires independent review of all imports and proof steps in the frozen candidate; the public source proof DAG remains unreplayed. Scope is alternating groups only; no all-simple-groups conclusion follows.
