# PA19 ms09 structural route: empty-pair counting and forced pair demand (proof note v1)

written_after_host_clock: 2026-10-19T13:24:37-0700 · author: ContinuePA19d (info-1 slot) · scope: `notes/ms09-structural-route-scope-v1.md` (56ff66587b6480cce5fa271f531a5addf4e977ac5e2c2b5bba17cd43b7c5c923), frozen 2026-10-19T13:13:39-0700 before derivation · level: WRITTEN PROOF CANDIDATE (not reviewed, not parent-accepted, not solver-checked, not Lean) · execution: none

## Result and claim boundary

Exactly four named ms09 cases of `evidence/probes/frontier-v1.json` (0e7e4370961ea8713f8549576a3973c661c1b6499f8a345c74be97d0b4216a46) are excluded. Each exclusion uses a lemma stated for every ms09 skeleton and proved below from the definitions only.

| case | skeleton entry, `OLD/cycle2/skel-b/skeletons-b-ms09.json` (one physical line), bytes [start,end) | e | excluded by |
|---|---|---|---|
| b59 | `{"types": [[0, 1, 2], [0, 3, 4], [1, 3], [1, 4], [2, 3], [2, 4]], "empty": 7}` [3934,4011) | 7 | Theorem B |
| b67 | `{"types": [[0, 1, 2], [0, 3], [0, 4], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], "empty": 8}` [4594,4684) | 8 | Theorem A |
| b69 | `{"types": [[0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], "empty": 8}` [4775,4870) | 8 | Theorem A |
| b70 | `{"types": [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], "empty": 9}` [4872,4975) | 9 | Theorem A |

The same entries appear in frontier-v1.json at lines 5169-5213 (b59), 5549-5600 (b67), 5652-5706 (b69) and 5707-5767 (b70). Excerpt SHA-256 values are in `review/ms09-structural-route-excerpt-manifest-v1.json`. Nothing is claimed for the other 61 ms09 cases or for any of the 86 ms06 cases of frontier-v1; Section 6 gives the exact obstruction. PA(19,8,6) stays UNDECIDED.

## 0. Setting and bridge premise

A valid array for an ms09 case is a 19 x 8 array over 6 symbols in which any two rows agree in at most one column, with the column profiles of the file header (bytes [0,433)): columns 0..4 ("P0") have symbol-class sizes (4,3,3,3,3,3); columns 5, 6, 7 ("P1") have sizes (4,4,3,3,3,2); `"L": 0`. A block is a symbol class of one column; two rows agree in a column iff they share a block of it.

**Bridge premise B0 (skeleton semantics).** For each P0 column c the case fixes its 4-block Q_c (the P0 quad). Put T(r) = {c : r in Q_c} and t(r) = |T(r)|. The rows are: one row for each listed type (T equal to the listed set), then for each P0 column c exactly 4 - deg(c) private rows with T = {c} (deg(c) = number of listed types containing c), then `empty` rows with T empty. This is the member construction of the pinned encoder `code/vendor/encode_skel_b.py` (d0002e60d11ef5cba568309fde5b15e29280ca127bc0e6bb1f4d22929a5628e5): docstring lines 3-7 ("Rows: the given types (rows in >= 2 P0 quads) in the listed order, then for each P0 column v its 4 - deg(v) private rows, then the empty rows"), `build` lines 83-86, and line 99 (P0 symbol 0 fixed iff c in member[r]). It is also the semantics of the accepted b3 and b30/b44 proofs. The encoder is quoted, never run.

Write e for the number of empty rows (the `empty` field) and call the other rows nonempty.

## 1. Basic facts (every ms09 case)

**F1 (exactness).** Summing C(|block|,2) over all blocks gives 5*21 + 3*22 = 171 = C(19,2). Every pair agrees at most once, so every pair of distinct rows shares exactly one block.

**F2 (T-disjointness).** If T(r) and T(s) meet, r and s share a P0 quad, so by F1 they share no other block. Hence every block other than a P0 quad consists of rows with pairwise disjoint T-sets, and a triple of P0 column c contains no row of Q_c.

**F3 (row identity).** Row r agrees with exactly 18 rows, each in exactly one block, so the sum over its eight blocks of (|block| - 1) is 18. The P0 columns contribute 3 for each c in T(r) and 2 otherwise, 10 + t(r) in total. Let n4, n3, n2 be the numbers of P1 columns in which r lies in a block of size 4, 3, 2. Then n4 + n3 + n2 = 3 and 3 n4 + 2 n3 + n2 = 8 - t(r), so 2 n4 + n3 = 5 - t(r). The solutions are:
- t = 0: (n2, n3, n4) = (0, 1, 2);
- t = 1: (1, 0, 2) or (0, 2, 1);
- t = 2: (1, 1, 1) or (0, 3, 0);
- t = 3: (2, 0, 1) or (1, 2, 0).

**F4 (empty rows).** By F3 with t = 0, an empty row lies in exactly one triple of each P0 column, in exactly two P1 blocks of size 4 (in two different P1 columns), in exactly one P1 block of size 3, in no P0 quad and in no P1 block of size 2.

**F5 (pair blocks).** Each P1 column has exactly one block of size 2, its pair block. So there are exactly three pair blocks and the sum of n2 over all rows is 6. The two rows of a pair block are T-disjoint (F2) and nonempty (F4). A row with n2 = 2 lies in two different pair blocks.

A non-quad block is any block other than a P0 quad. For a block b, eps(b) denotes the number of empty rows in b.

## 2. Empty-pair counting

**Lemma 1 (empty-pair identity).** The sum of C(eps(b),2) over all non-quad blocks b equals C(e,2). In each P0 column the five triples have eps summing to e. The six P1 4-blocks have eps summing to 2e, and the nine P1 3-blocks have eps summing to e. Pair blocks and P0 quads have eps = 0.

*Proof.* By F1 every pair of empty rows shares exactly one block, which is neither a P0 quad (t = 0) nor a pair block (F4). The sums follow from F4. ∎

**Lemma 2 (balancing).** For integers x_1, ..., x_k >= 0 with sum n = qk + r, 0 <= r < k, the sum of C(x_i,2) is at least Phi_k(n) := k C(q,2) + r q, with equality iff every x_i is q or q + 1.

*Proof.* If x_i >= x_j + 2, replacing (x_i, x_j) by (x_i - 1, x_j + 1) lowers the sum by x_i - 1 - x_j >= 1. So the minimum is attained exactly at the balanced vectors, whose value is (k - r) C(q,2) + r C(q+1,2) = k C(q,2) + r q. ∎

**Theorem A.** An ms09 case with e = 8 or e = 9 has no valid array.

*Proof.* Lemmas 1 and 2 give C(e,2) >= 5 Phi_5(e) + Phi_6(2e) + Phi_9(e).
- e = 8: Phi_5(8) = 3 (8 = 1*5 + 3), Phi_6(16) = 6*1 + 4*2 = 14, Phi_9(8) = 0. The right side is 15 + 14 + 0 = 29 > 28 = C(8,2).
- e = 9: Phi_5(9) = 4, Phi_6(18) = 6*3 = 18, Phi_9(9) = 0. The right side is 20 + 18 + 0 = 38 > 36 = C(9,2). ∎

## 3. Seven empty rows

Assume e = 7, so there are 12 nonempty rows. By Lemma 2, Phi_5(7) = 2, Phi_6(14) = 10 and Phi_9(7) = 0.

**Lemma 3 (exactly one unit of excess).** Put X_c = (sum over the triples of P0 column c of C(eps,2)) - 2, X_Q = (sum over the P1 4-blocks) - 10 and X_T = sum over the P1 3-blocks. Then all of them are >= 0 and X_0 + ... + X_4 + X_Q + X_T = 21 - 20 = 1. Moreover:
1. X_c = 0 iff the eps-values of the triples of c are {2,2,1,1,1}; X_c = 1 iff they are {3,1,1,1,1} or {2,2,2,1,0}.
2. X_Q = 0 iff the six 4-block values are {3,3,2,2,2,2}; X_Q = 1 iff they are {4,2,2,2,2,2} or {3,3,3,2,2,1}.
3. X_T = 0 iff every P1 3-block has eps <= 1; X_T = 1 iff exactly one P1 3-block has eps = 2 and all others have eps <= 1.

*Proof.* Lemma 1 gives total 21 = C(7,2), and Lemma 2 gives the three lower bounds 5*2, 10 and 0. For the lists use C(0,2) = C(1,2) = 0, C(2,2) = 1, C(3,2) = 3, C(4,2) = 6.
- (1) Five values summing to 7. A total of 2 needs exactly two values equal to 2 and the rest <= 1, which forces {2,2,1,1,1}. A total of 3 needs either one value 3 and four values <= 1 summing to 4, giving {3,1,1,1,1}, or three values 2 and two values <= 1 summing to 1, giving {2,2,2,1,0}.
- (2) Let a_k be the number of 4-blocks with value k, so the a_k sum to 6, the k a_k sum to 14, and a_2 + 3 a_3 + 6 a_4 is 10 or 11. For 10: a_4 = 0, a_3 = 2, a_2 = 4. For 11: either a_4 = 1, a_2 = 5, or a_3 = 3, a_2 = 2, a_1 = 1. All other choices violate one of the three equations.
- (3) is immediate, since C(3,2) = 3 > 1. ∎

Consequently there is at most one P0 triple with eps = 0 (only if some X_c = 1 with values {2,2,2,1,0}), at most one P1 4-block with eps = 1 (only if X_Q = 1 with values {3,3,3,2,2,1}), and at most one P1 3-block with eps = 2 (only if X_T = 1). Since the total excess is 1, at most one of these three special blocks exists.

**Lemma 4 (empty incidence).** Every nonempty row r has sum over its eight blocks of eps equal to 7.

*Proof.* By F1, r shares exactly one block with each of the 7 empty rows. ∎

A P0 triple or P1 3-block containing a nonempty row has eps <= 2, and a P1 4-block containing a nonempty row has eps <= 3.

**Lemma 5 (rescue).** Let e = 7.
- (R1) If a private row p has n2(p) = 1, then p lies in the unique P0 triple with eps = 0, or in the unique P1 4-block with eps = 1.
- (R2) If a row r with t(r) = 3 has n2(r) = 1, then X_T = 1 and r lies in the unique P1 3-block with eps = 2.

*Proof.*
- (R1) By F3, p has pattern (1,0,2). Its blocks are its P0 quad and its pair block (eps = 0), four P0 triples, and two P1 4-blocks. By Lemma 3, every P0 triple has eps >= 1 except the special one with eps = 0, and every P1 4-block has eps >= 2 except the special one with eps = 1. If p is in neither special block, its eps-sum is at least 4*1 + 2*2 = 8, contrary to Lemma 4.
- (R2) By F3, r has pattern (1,2,0). Its blocks are three P0 quads and a pair block (eps = 0), two P0 triples (eps <= 2 each) and two P1 3-blocks. If r is not in the special 3-block with eps = 2, both of its P1 3-blocks have eps <= 1 (Lemma 3(3)), so its eps-sum is at most 2 + 2 + 1 + 1 = 6 < 7, contrary to Lemma 4. ∎

**Lemma 6 (forced double pairing).** Let e = 7, and let r be a row with t(r) = 3 and T(r) = {0,1,2,3,4} \ {x, y}, where {x, y} is not a listed type. Then n2(r) = 2.

*Proof.* By F3, n2(r) is 1 or 2. A pair-block partner s of r is nonempty (F5) and T-disjoint from r (F2), so T(s) is contained in {x, y}. T(s) = {x, y} would be a listed type, so s is a private row with T(s) = {x} or {y}. Since n2(s) >= 1 and t(s) = 1, F3 gives n2(s) = 1. If n2(r) = 1, then (R2) gives X_T = 1, so every X_c = 0 and X_Q = 0 (Lemma 3). Then neither special block of (R1) exists, and (R1) fails for s. Hence n2(r) = 2. ∎

**Theorem B.** Suppose an ms09 case has e = 7 and two rows r1, r2 with t = 3, neither of whose complements in {0,1,2,3,4} is a listed type. Then it has no valid array.

*Proof.* By Lemma 6, n2(r1) = n2(r2) = 2, so each of r1 and r2 lies in two pair blocks (F5). Since |T(r1)| + |T(r2)| = 6 > 5, T(r1) and T(r2) meet, so no pair block contains both (F2). Hence there are at least four pair blocks, contradicting F5. ∎

## 4. Application to the named cases

All data below are read from the quoted bytes. deg(c) counts the listed types containing c, and the private count of column c is 4 - deg(c).

| case | listed types (t) | deg(0..4) | private rows | checks: sum of t over types + private = 20; types + private + e = 19 | conclusion |
|---|---|---|---|---|---|
| b59 | {0,1,2}, {0,3,4} (t=3); {1,3}, {1,4}, {2,3}, {2,4} (t=2) | 2,3,3,3,3 | 2+1+1+1+1 = 6 | 14 + 6 = 20; 6 + 6 + 7 = 19 | e = 7. The t=3 rows have complements {3,4} and {1,2}; neither is listed. Theorem B: no valid array. |
| b67 | {0,1,2} (t=3); seven 2-sets {0,3}, {0,4}, {1,3}, {1,4}, {2,3}, {2,4}, {3,4} | 3,3,3,4,4 | 1+1+1+0+0 = 3 | 17 + 3 = 20; 8 + 3 + 8 = 19 | e = 8. Theorem A: no valid array. |
| b69 | nine 2-sets (all except {0,1}) | 3,3,4,4,4 | 1+1+0+0+0 = 2 | 18 + 2 = 20; 9 + 2 + 8 = 19 | e = 8. Theorem A: no valid array. |
| b70 | all ten 2-sets | 4,4,4,4,4 | 0 | 20 + 0 = 20; 10 + 0 + 9 = 19 | e = 9. Theorem A: no valid array. |

For every listed set of these four cases, two distinct listed sets meet in at most one element, as F2 requires. The exclusions therefore do not rest on a malformed skeleton.

## 5. Relation to accepted results

- The accepted b3, b30 and b44 exclusions use the pair partners of one row with t >= 4 (a single-row degree argument). b67, b69 and b70 have no row with t >= 4, and Theorem A uses only e and the empty-pair identity.
- Theorem B forces n2 = 2 for t = 3 rows through the e = 7 excess analysis (Lemmas 3-5). The pair-degree bounds alone (n2 between max(0, t - 2) = 1 and floor((t + 1)/2) = 2 when t = 3) also permit n2 = 1 for both t = 3 rows of b59, for example with pair blocks {{0,1,2}-row, private-3 row}, {{0,3,4}-row, private-1 row} and one further T-disjoint pair. So Theorem B does not follow from those bounds.
- No GPS-1/GPS-2 statement, applied count, list, solver, probe or encoder run is a premise. b3/b30/b44 are cited for comparison only.

## 6. Exact obstruction for the remaining cases; smallest missing lemma

**Slack of Lemma 1 alone.** Define slack(e) = C(e,2) - (5 Phi_5(e) + Phi_6(2e) + Phi_9(e)). The values are 0, 0, 1, 3, 4, 6, 4, 1, -1, -2 for e = 0, ..., 9. So Lemma 1 by itself excludes exactly e = 8 and e = 9.

The frontier-v1 ms09 cases by e (read from the skeleton entries) are:

| e | cases | count |
|---|---|---|
| 1 | b4, b5 | 2 |
| 2 | b6, b7, b10, b11, b12, b15 | 6 |
| 3 | b8, b9, b13, b16, b17, b18, b20, b22, b23, b25, b26, b28 | 12 |
| 4 | b14, b19, b21, b24, b27, b29, b31, b32, b35, b36, b37, b39, b41, b47 | 14 |
| 5 | b33, b34, b38, b40, b42, b43, b45, b48, b49, b50, b51, b53, b55, b57 | 14 |
| 6 | b46, b52, b54, b56, b58, b60, b61, b62, b64 | 9 |
| 7 | b59, b63, b65, b66, b68 | 5 |
| 8 | b67, b69 | 2 |
| 9 | b70 | 1 |

**e = 7, remaining b63, b65, b66, b68.**
- **b65.** Types {0,1,2}, {0,3}, {0,4}, {1,3}, {1,4}, {2,3}, {2,4}; one private row per column. Lemma 6 applies to g = {0,1,2} (complement {3,4} is not listed). So g pairs with the private rows p3 and p4 in two P1 columns j1, j2, and both need rescue by (R1). By Lemma 4 at equality, g's 4-block lies in the third P1 column j with eps = 3. Then p3 and p4 are both in the other 4-block of j and agree there. So the rescue cannot be one P0 triple holding both, since they would agree twice. It must be X_Q = 1 with that 4-block equal to {p3, p4, w, one empty row}, where w is the private row of column 0, 1 or 2. I derived no contradiction from this forced structure.
- **b63.** Types {0,1,2}, {0,4}, {1,3}, {1,4}, {2,3}, {2,4}, {3,4}. The complement {3,4} of g is listed, so Lemma 6 does not apply. g = (2,0,1) with partners p3 and the {3,4}-row is still open, and so is g = (1,2,0) with partner the {3,4}-row and X_T = 1.
- **b66, b68.** There is no t = 3 row. (R1) only forbids private pair rows outside the single special block, and three T-disjoint pair blocks among the t = 2 rows are compatible with Lemmas 3-5.

**e <= 6** (57 cases). The slack of Lemma 1 is at least 1, and the per-row incidence analysis is weak once two or more excess units are available. The case e = 2 also has slack 1 (b6, b7, b10, b11, b12, b15). There each nonempty row meets the two empty rows exactly twice in total, which is the most promising next family.

**Smallest missing lemma.** A single-excess-block lemma for e = 7: a written classification of the unique excess location (one triple of {3,1,1,1,1} or {2,2,2,1,0} type, one 4-block of {4,2,2,2,2,2} or {3,3,3,2,2,1} type, or one 3-block with eps = 2), combined with the P1 rainbow condition (each Q_c meets four distinct blocks of each P1 column) and the P0 triple structure of the columns missing from the t = 3 rows. For b65 this means analyzing one forced 4-block shape. In P0 columns 3 and 4, the three private rows p0, p1, p2 must then lie with three distinct rows of Q_4, resp. Q_3. That analysis is the next bounded written step.

**ms06.** Not attempted. With L = 1 the analogue of Lemma 1 has one leave pair and two P1 columns; I did not derive a transfer.

## 7. Verification boundary

- This is a written proof derived without any computation, enumeration code, solver, probe or encoder run. All arithmetic is shown inline.
- Bridge premise B0 is quoted from the skeleton bytes and the pinned encoder source. No list, encoder output, list-coverage or GPS-count premise is used.
- Not reviewed, not parent-accepted, not solver-checked, not Lean. No interval, list, queue or frontier count changes before parent disposition.
- The exclusions are independent of any solver record. In particular, the earlier runner-level run-003 commit for b70 (pending parent audit) is neither used nor counted here.
