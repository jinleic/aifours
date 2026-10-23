# Rederived imports and full single-excess occupancy classification v1

Written after host clock 2026-10-19T13:52:45-0700. No prior candidate lemma is assumed accepted.

## Definitions and exactness
An ms09 array has 19 rows and eight columns over six symbols. The first five columns P0 have block sizes (4,3,3,3,3,3); the last three P1 have sizes (4,4,3,3,3,2). Any distinct row pair agrees in at most one column. Its P0 quads Q_c are specified by the skeleton; T(r)={c:r in Q_c}, t(r)=|T(r)|. The seven rows with T empty form E; N is the other twelve rows. A private row has t=1. The exact pinned case bytes will be bound separately.

There are 5*21+3*22=171=C(19,2) agreeing row pairs, so every pair agrees exactly once. Consequently any two blocks from different columns meet in at most one row. Every block other than a P0 quad contains pairwise T-disjoint rows. Each Q_c meets four DISTINCT blocks of each P1 column (rainbow condition).

Let n_i(r) count the P1 blocks of size i containing r, and write patterns in order (n2,n3,n4). Counting the eighteen partners of r gives 10+t+3n4+2n3+n2=18 and n2+n3+n4=3. Thus:
- t=0: (0,1,2);
- t=1: (0,2,1) or (1,0,2);
- t=2: (0,3,0) or (1,1,1);
- t=3: (1,2,0) or (2,0,1).
In particular every empty row belongs to five P0 triples, two P1 quads, one P1 triple, and no pair. There are exactly three P1 pair blocks; their endpoints are nonempty, T-disjoint, and repeated pairs are forbidden.

## Empty-pair count and the five occupancy categories
Write eps(B)=|B intersect E|. Counting each pair of empty rows in its unique agreeing block gives sum_B C(eps(B),2)=21. In each P0 column its five triple eps values sum to7; the six P1 quad values sum to14; the nine P1 triple values sum to7. The pair blocks and P0 quads contribute zero.

For k nonnegative integers summing to n, sum C(x,2) is minimized by values differing by at most1: moving one unit from a>=b+2 to b lowers the sum by a-b-1>0. Hence minima are 2 for each P0 column,10 for the six P1 quads,0 for the nine P1 triples. Their excesses X_c,X_Q,X_T are nonnegative integers summing to21-(5*2+10)=1.

Exactly one of the following FIVE categories holds. This is a classification of occupancy numbers ONLY, NOT of complete block assignments or arrays.

| category | exceptional occupancy | all other occupancies |
|---|---|---|
| C3 | one P0 column triples (3,1,1,1,1) | P0 (2,2,1,1,1); P1 quads (3,3,2,2,2,2); P1 triples <=1 |
| C0 | one P0 column triples (2,2,2,1,0) | same others as C3 |
| Q4 | P1 quads (4,2,2,2,2,2) | all P0 (2,2,1,1,1); P1 triples <=1 |
| Q1 | P1 quads (3,3,3,2,2,1) | all P0 (2,2,1,1,1); P1 triples <=1 |
| T2 | one P1 triple eps=2, all other P1 triples <=1 | all P0 (2,2,1,1,1); P1 quads (3,3,2,2,2,2) |

Proof of exhaustiveness: five values <=3 with sum7 and pair-count2 must be (2,2,1,1,1). Pair-count3 means one3 and four1s or three2s plus1,0. For the six quad values <=4, let a_i count occurrences of i: sum a_i=6, sum i*a_i=14, a2+3a3+6a4 is10 or11. Solving these three small integer identities gives only (3,3,2,2,2,2), or the two exceptional vectors Q4/Q1. Nine values <=3 with pair-count1 must contain exactly one2 and no3. The five categories place the only unit of excess; no combination of categories is permitted.

## Per-row empty incidence and rescue
Every nonempty row r satisfies I(r):=sum_{B containing r} eps(B)=7, since it agrees exactly once with each empty row.

(R1) A private pair endpoint has pattern (1,0,2). Unless it belongs to the unique eps0 P0 triple (C0) or unique eps1 P1 quad (Q1), its four P0 triples each contribute at least1 and its two P1 quads at least2, giving I>=8. Thus every private pair endpoint lies in the unique rescue block. That block has exactly three nonempty rows, so there are at most three distinct private pair endpoints. In C3,Q4,T2 there are none.

(R2) A t3 row with n2=1 has pattern (1,2,0). Its two P0 triples contribute at most4 and its two P1 triples at most2 unless it belongs to the eps2 P1 triple. Hence it requires category T2 and membership in that unique eps2 triple. Equality forces both its P0 triples to have eps2 and its other P1 triple eps1.

(R3) A t3 row with n2=2 has pattern (2,0,1). Its two P0 triples contribute at most4 and its quad at most3; equality I=7 forces eps2,eps2,eps3 respectively. In particular category Q4 is impossible for such a row (all quads touching a nonempty row then have eps2).

(R4) If the two-element complement of a t3 row is NOT a listed type, every possible pair partner is private (it must be nonempty and T-disjoint). If that row had n2=1, R2 would force T2, while its private partner would need C0/Q1 by R1, impossible. Thus n2=2, with two distinct private partners.

These statements are rederived directly above; they do not import GPS list coverage, solver status, or acceptance of the earlier candidate proof. Nothing here asserts that a numerical occupancy pattern extends to an array.
