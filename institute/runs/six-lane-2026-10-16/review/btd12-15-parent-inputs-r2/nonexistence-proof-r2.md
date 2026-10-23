# Candidate proof r2: there is no BTD(12,15;6,2,10;8,6)

## Status and provenance
* Status: CANDIDATE r2, untrusted until the parent's verdict. It was written by worker `InfoCyclic100` on
  2026-10-17, host clock PDT, and frozen when `notes/freeze-receipt-r2.txt` was written. No novelty, priority or
  significance claim is made.
* r1 is `notes/nonexistence-proof.md`, sha256 837a26eaaf76a0406a1701ab02ca2b4616abdec927eafc062dcc578a3ba9e7a5. It is
  frozen and unchanged.
* r2 keeps Steps 1-7 of r1 (wording tightened) and replaces r1 Steps 8-11 by the three-line closure in Step 8 below.
  * The closure was recommended in the parent's review `review/btd12-15-claude-complete-review-v1.note.md` (sha256
    46ee1d00…0481) and hand-checked by the parent.
  * It is verified independently here, by hand and by `code/proof_check_r2.py` (stdlib exact arithmetic; the
    script SHA and its receipt are in the freeze receipt).
* The change removes the minor findings on r1 Step 8: the indexing of Y_kk = det H[{a,b,k}]/15 for k in {a,b}
  (parent Codex review, sha256 64e10184…cb22) and the parenthetical about 2 x 2 minors. Those parts are no longer
  used.
* r1 Steps 8-11 remain an independent second closure. They are reviewed in the same two notes.
* r2 uses no rank or spectral argument: positivity comes from x^T H x = |Hx|^2/40.

## Setting
* Suppose M is a 12 x 15 matrix over {0,1,2} in which every row has exactly six 1s and two 2s, every column sums to
  8, and any two distinct rows have inner product 6.
* Repeated columns are allowed. No other assumption is made.
* J denotes all-ones matrices and **1** all-ones vectors.
* c_j is the number of 2s in column j, and n_c is the number of columns with c_j = c.
* G = M^T M, with g_jk = G_jk, and H := 40 I - 5 G + 24 J. H is an integer symmetric 15 x 15 matrix.

## Step 1 (identities)
* M M^T = 8I + 6J: rows have squared norm 6 + 2·4 = 14 and pairwise inner product 6.
* M **1** = 10 **1** and M^T **1** = 8 **1**. Hence G J = J G = 80 J and
  G^2 = M^T (8I + 6J) M = 8G + 6 (M^T **1**)(M^T **1**)^T = 8G + 384 J.
* With J^2 = 15 J, expanding gives H^2 = 1600 I - 200 G + (9600 + 8640 + 1920 - 19200) J = 40 H, and
  H **1** = (40 - 400 + 360) **1** = 0.
* Entries:
  * H_jj = 40 - 5(8 + 2 c_j) + 24 = 24 - 10 c_j;
  * for j != k, H_jk = 24 - 5 g_jk, which is congruent to -1 (mod 5).

## Step 2 (positivity)
* For every real vector x: x^T H x = x^T H^2 x / 40 = |Hx|^2 / 40 >= 0. So:
  * (a) H_jj >= 0, hence c_j <= 2;
  * (b) H_jk^2 <= H_jj H_kk, from x = H_kk e_j - H_jk e_k, or from the nonnegative 2 x 2 principal minors;
  * (c) if x^T H x = 0 then H x = 0;
  * (d) every principal minor of H is >= 0. This is used in Step 8 only as a remark.

## Step 3 (column types)
* Twelve rows with two 2s each give sum_j c_j = 24. With c_j <= 2: n_1 + 2 n_2 = 24 and n_0 + n_1 + n_2 = 15.
  Hence n_2 = 9 + n_0 >= 9 and n_1 = 24 - 2 n_2.
* Columns with c_j = 2, 1, 0 are called type-2, type-1, type-0. They have H_jj = 4, 14, 24.

## Step 4 (row relations at a type-2 column)
* For every j: sum_k H_jk = 0 (from H **1** = 0) and sum_k H_jk^2 = (H^2)_jj = 40 H_jj.
* For a type-2 column j, the integers t_k = (H_jk + 1)/5 = 5 - g_jk (k != j) satisfy
  sum_{k != j} t_k = 2 and sum_{k != j} t_k^2 = 6, because sum_{k != j} (5 t_k - 1) = -4,
  sum_{k != j} (5 t_k - 1)^2 = 160 - 16 = 144, and there are 14 terms.
* The nonzero t_k therefore form {1,1,1,1,-1,-1} or {2,1,-1}. In particular at most four columns k != j have
  H_jk = 4.

## Step 5 (classes of type-2 columns)
* For type-2 columns j != k: |H_jk| <= 4 (Step 2(b)) and H_jk is congruent to -1 mod 5, so H_jk is 4 or -1.
* If H_jk = 4, then (e_j - e_k)^T H (e_j - e_k) = 4 + 4 - 8 = 0. So H (e_j - e_k) = 0 (Step 2(c)), and columns j
  and k of H are equal.
* Hence "H_jk = 4" is an equivalence relation on type-2 columns. Its classes have equal H-columns, H = -1 holds
  between different classes, and each class has at most 5 columns (Step 4).

## Step 6 (Lemma D: every 3 x 3 principal minor of H has a perfect-square determinant)
* Let S be any 3 columns. Write M = [N | P], with P the 12 x 3 submatrix on S and N the integer 12 x 12 submatrix
  on the other 12 columns. Then N N^T = A - P P^T with A = 8I + 6J.
* Facts used:
  * A^{-1} = (I - (3/40) J)/8;
  * det A = 80 · 8^11 = 2^37 · 5;
  * P^T **1** = 8 **1**, hence P^T J P = 64 J;
  * therefore I_3 - P^T A^{-1} P = (40 I - 5 P^T P + 24 J)/40 = H[S]/40.
* By the matrix determinant lemma, det(N)^2 = det(A) · det(H[S]/40) = 2^28 det(H[S]) / 25.
* So det H[S] = (5 det N / 2^14)^2: an integer that is the square of a rational, hence a perfect square (possibly
  0). Neither invertibility of N nor simplicity is needed.

## Step 7 (exactly two classes)
* Three type-2 columns from three different classes would give H[S] = 5I - J (3 x 3), with determinant 50. That is
  not a perfect square, contradicting Step 6. So there are at most two classes.
* Each class has at most 5 columns and n_2 >= 9, so there are exactly two classes, A and B, and n_2 = |A| + |B| is 9
  or 10.
* Consequently n_1 = 24 - 2 n_2 is 6 or 4 > 0: type-1 columns exist.

## Step 8 (closure, new in r2)
* Take a in A, b in B, and any type-1 column k, so k is not in {a, b}. Then H_aa = H_bb = 4, H_ab = -1 and
  H_kk = 14.
* Put x = H_ka and y = H_kb. By Step 2(b), x^2 <= 14 · 4 = 56, so |x| <= 7, and x is congruent to -1 mod 5. Hence x
  is in {-6, -1, 4}, and likewise y.
* Expanding det H[{a,b,k}] = det [[4, -1, x], [-1, 4, y], [x, y, 14]] gives
  4·4·14 + 2·(-1)·x·y - 4 y^2 - 4 x^2 - 14·(-1)^2 = 210 - (4x^2 + 2xy + 4y^2).
* All nine cases:

  | x = H_ka | y = H_kb | 4x^2 + 2xy + 4y^2 | det H[{a,b,k}] | nonnegative perfect square? |
  |---:|---:|---:|---:|:---:|
  | -6 | -6 | 360 | -150 | no (negative) |
  | -6 | -1 | 160 | 50 | no |
  | -6 | 4 | 160 | 50 | no |
  | -1 | -6 | 160 | 50 | no |
  | -1 | -1 | 10 | 200 | no |
  | -1 | 4 | 60 | 150 | no |
  | 4 | -6 | 160 | 50 | no |
  | 4 | -1 | 60 | 150 | no |
  | 4 | 4 | 160 | 50 | no |

* In every case det H[{a,b,k}] is not a nonnegative perfect square (14^2 = 196 < 200 < 225 = 15^2;
  7^2 < 50 < 8^2; 12^2 < 150 < 13^2). This contradicts Step 6 (and in the first case also Step 2(d)).

## Conclusion
* The assumption is impossible. No 12 x 15 matrix over {0,1,2} has six 1s and two 2s in every row, column sums 8
  and pairwise row inner products 6.
* Hence BTD(12,15;6,2,10;8,6) does not exist, including designs with repeated blocks (candidate; parent verdict
  pending).

## What is used
* Integer and rational linear algebra on the column Gram matrix: Steps 1-2, positivity from H^2 = 40H.
* The matrix determinant lemma, and det(N N^T) = det(N)^2 for a square integer matrix N (Step 6).
* Finite arithmetic: Steps 4, 5, 7, 8.
* No computer search over matrices is used. `code/proof_check_r2.py` re-checks every number in this note by exact
  arithmetic: the Step 1 algebra, A^{-1} and det A, the Lemma D factor, the Step 4 multisets, the Step 5 values,
  det(5I - J) = 50, and the nine-case table.
