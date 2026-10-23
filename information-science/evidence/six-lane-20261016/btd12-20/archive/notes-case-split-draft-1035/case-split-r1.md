# Candidate case split r1: there is no BTD(12,20;4,3,10;6,4)

## Status
* CANDIDATE r1, computer-assisted, untrusted until parent review. Written by worker `InfoCyclic100` on 2026-10-17
  (host clock PDT) after the lane README freeze (10:12:02).
* Uses only the contract definition (repeated columns allowed, no other assumption).
* Parts A-C below are mathematics. Part D (every case has no completion) currently rests on CP-SAT INFEASIBLE answers,
  which are information only. The certificate plan (an independent small CNF per case, kissat DRAT proofs checked by
  drat-trim, encoding controls) is in Part E and is NOT yet done.
* Lemma T and its use follow the parent's untrusted lead (contract `parent_lead_untrusted`). Its statement matches
  Elkies-Kominers arXiv:0902.1942v1 Section 1.1 (pinned, which cites Koch without proof); the proof below is
  self-contained and does not use that source.
* No novelty, priority or significance claim.

## Setting
M is a 12 x 20 matrix over {0,1,2}; every row has four 1s and three 2s; every column sums to 6; distinct rows have
inner product 4. Write M = A + 2D with A, D the 0/1 indicator matrices of the 1s and 2s; A_i, D_i are the supports
of row i (|A_i| = 4, |D_i| = 3, disjoint). Column j has a_j ones and d_j twos, a_j + 2 d_j = 6.

## Part A: elementary facts
* (I1) For i != k: 4 = M_i . M_k = |A_i cap A_k| + 2(|A_i cap D_k| + |D_i cap A_k|) + 4 |D_i cap D_k|, so
  |A_i cap A_k| is even: 0, 2 or 4.
* (I2) a_j = 6 - 2 d_j is even: a_j is 0, 2, 4 or 6.
* Hence the distinct row supports of A ("tetrads") pairwise meet in 0 or 2 points, and the multiset of the 12 rows of
  A is a multiset of tetrads in which every column is covered 0, 2, 4 or 6 times.

## Part B: Lemma T (connected tetrad families)
Let F be a set of distinct 4-sets, any two meeting in 0 or 2 points; call two members adjacent if they meet in 2
points. Suppose the adjacency graph on F is connected, and let S be the union of F. Then exactly one of:
* (d) S has a partition into pairs such that every member of F is the union of two of the pairs;
* (e7) |S| = 7 and F is contained in the 7 tetrads of an e7 structure on S (complements of the lines of a Fano plane);
* (e8) |S| = 8 and F is contained in the 14 tetrads of an e8 structure on S (planes of AG(3,2)).
(For (d) the case |F| = 1 is included: pair the four points arbitrarily.)

Proof.
1. Over GF(2), the span C of F consists of words that meet every member of F (indeed every word of C) in an even
   number of points, because members pairwise meet evenly.
2. For an adjacent pair T, T' in F, T is split into the two pairs T cap T' and T \ T'. Suppose first that for every
   T in F all its neighbours induce the same split of T (call the two parts the parts of T). If parts P of T and P' of
   T' share exactly one point z, then z is in T cap T', so T, T' are adjacent (they meet, hence in 2 points); then the
   part of T containing z is T cap T' and the part of T' containing z is T' cap T, so P = P' -- a contradiction.
   Hence all parts are pairwise equal or disjoint, every member of F with a neighbour is the union of its two parts,
   and the parts partition S (by connectivity every member has a neighbour unless |F| = 1). This is case (d).
3. Otherwise some T in F has neighbours T1, T2 inducing different splits of T. Any part of one split of a 4-set meets
   any part of a different split in exactly one point, so after renaming T = {1,2,3,4}, T cap T1 = {1,2},
   T cap T2 = {1,3}. T1 and T2 share 1, so they meet in exactly 2 points; 2 is not in T2 and 3 is not in T1 (else T
   would meet T2 or T1 in 3 points), so T1 = {1,2,a,b}, T2 = {1,3,a,d} with 1,2,3,4,a,b,d distinct. Put
   X = {1,2,3,4,a,b,d}. The span of {T, T1, T2} has the seven nonzero words T, T1, T2, T+T1 = {3,4,a,b},
   T+T2 = {2,4,a,d}, T1+T2 = {2,3,b,d}, T+T1+T2 = {1,4,b,d}, all of weight 4: it is a [7,3,4] code on X, i.e. e7, and
   its seven tetrads are the complements of the lines of a Fano plane on X.
4. Order F as T, T1, T2, T3, ... so that each later member is adjacent to an earlier one (connectivity). Let G be the
   set of members before T'. Inductively span(G) is e7 on X or e8 on X + {y} (one extra point y), and G is inside its
   tetrads. By step 1, T' meets every word of span(G) evenly.
   * If span(G) = e7 on X: T' cap X lies in the dual of e7 on X, the [7,4,3] Hamming code (weights 0, 3, 4, 7). T'
     meets a member of G in 2 points, so |T' cap X| is 3 or 4. If 4, T' is a weight-4 Hamming word, i.e. one of the
     seven e7 tetrads. If 3, T' = L + {y} with L a Hamming weight-3 word (a line) and y outside X; then the span
     becomes the extended Hamming code e8 on X + {y}, whose 14 tetrads are the seven e7 tetrads and the seven
     L + {y}.
   * If span(G) = e8 on X + {y}: e8 is self-dual, so T' cap (X + {y}) is an e8 word of weight 0, 4 or 8; it is at
     least 2, so T' is one of the 14 e8 tetrads.
   Hence F lies in the tetrads of e7 on X (|S| = 7) or of e8 on X + {y} (|S| = 8), and S is all of X or X + {y}.
   This is case (e7) or (e8). Cases (d) and (e7)/(e8) exclude each other (step 2 vs step 3).
The facts about the [7,3,4], [7,4,3] and [8,4,4] codes used here are finite and are re-checked by
`code/tetrad_facts.py` (Part E).

## Part C: the case list
* Apply Lemma T to the set of distinct rows of A. Its adjacency components have pairwise disjoint supports (members
  of different components meet in 0 points). A d-type component, with its row multiplicities, is a loopless multigraph
  whose vertices are the pairs and whose edges are the rows; a vertex is a pair of columns each covered as many times
  as the vertex degree, so by (I2) every degree is 2, 4 or 6. An e-type component is a multiset of e7 tetrads on 7
  columns or of e8 tetrads on 8 columns, each of these columns covered 2, 4 or 6 times.
* All d-type components together form one multigraph with all degrees in {2, 4, 6}. At most two e-type components
  fit (three would need at least 21 columns). Columns covered by no row are free.
* So, up to row and column permutations (which preserve the definition), A is one of:
  * (E0) a multigraph with 12 edges, n vertices, all degrees in {2,4,6}, 2n <= 20 (n = 4..10: fewer vertices cannot
    carry degree sum 24 with degrees <= 6);
  * (E1) one or two full-support e-components with r rows in total, plus a multigraph with 12 - r edges, all degrees
    in {2,4,6}, on 2n columns with 2n <= 20 - (columns of the e-components) (possibly no edges).
* Enumeration (exhaustive up to isomorphism):
  * multigraphs: nauty 2.9.3 `geng -q -d1 -D6 n lo:e` (all simple graphs with n vertices, minimum degree >= 1,
    maximum degree <= 6, lo..e edges) piped into `multig -q -e<e> -D6 -T` (all ways to give the edges multiplicities
    >= 1 with e edges in total and maximum degree <= 6, isomorphs removed), then keep degrees in {2,4,6}
    (`code/mg_filter.py`, `code/e_combos.py`). Every multigraph with the required properties has an underlying simple
    graph with these bounds, so it appears.
  * e-components: `code/e_multisets.py` runs over all multiplicity vectors on the 7 (e7) or 14 (e8) tetrads with total
    <= 12 and point degrees <= 6, keeps point degrees in {0,2,4,6}, and keeps one representative per orbit of the full
    automorphism group (orders 168 and 1344, computed by brute force). Full-support representatives: 204.
  * Counts: (E0) 2069 multigraphs (n = 4..10: 7, 59, 312, 550, 616, 352, 173); (E1) 1004 patterns. Total 3073.
  * Files: `runs/mg-v1/mg-n{4..10}.txt`, `runs/e-v1/e-multisets.json` (b5498c35…31ca14),
    `runs/e-v1/e-combos-v2.jsonl` (8864ab42…c3b3).

## Part D: no case has a completion (computational; to be certified)
* For a fixed A, a BTD with 1-pattern A is exactly a 0/1 matrix D supported off A with row sums 3, column sums
  (6 - a_j)/2 and, for i < k, |A_i cap A_k| + 2(|A_i cap D_k| + |D_i cap A_k|) + 4|D_i cap D_k| = 4.
* CP-SAT (OR-Tools 9.15, 1 worker, 60 s limit per case; `code/restricted_batch.py`) answered INFEASIBLE for all 3073
  cases (`runs/mg-v1/res-n*.jsonl`, `runs/e-v1/res-e-combos-v2.jsonl`; slowest 26.8 s). This is information only.

## Part E: certification plan (not yet run)
* `code/tetrad_facts.py`: exhaustive check of the code facts used in Lemma T.
* Independent cross-checks of the enumeration (a second implementation of the multigraph and e-multiset counts).
* One small dedicated CNF per case (variables d_ij off A; exact cardinality counters for rows, columns and the pair
  equation), with positive controls (published BTDs: their own A must give SAT and decode to a verified BTD) and
  counting controls against brute force on small instances; kissat DRAT proofs checked by drat-trim, all hashes
  recorded.
* Only after Part E passes and the parent reviews would the case split support a nonexistence claim.
