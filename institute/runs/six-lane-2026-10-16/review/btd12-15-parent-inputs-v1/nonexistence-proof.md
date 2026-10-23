# Candidate proof: there is no BTD(12,15;6,2,10;8,6)

Status: CANDIDATE, untrusted until parent review. Written by worker `InfoCyclic100` on 2026-10-17 (PDT, host clock)
after the README 1.0 freeze. It uses only the contract definition: no simplicity, cyclicity or other assumption, and
repeated columns are allowed. The arithmetic is re-checked mechanically by `code/proof_check.py`, which re-derives the
final case analysis (Steps 7-11) by exhaustive enumeration rather than replaying the text below. No novelty,
priority or significance claim is made.

## Setting
* Suppose M is a 12 x 15 matrix over {0,1,2} in which every row has six 1s and two 2s, every column sums to 8, and
  distinct rows have inner product 6.
* Write J for all-ones matrices and **1** for all-ones vectors.
* For a column j, let c_j be the number of 2s in column j, and n_c the number of columns with c_j = c.
* Let G = M^T M (15 x 15), with g_jk = G_jk, and define the integer matrix H := 40 I - 5 G + 24 J.

## Step 1 (identities)
* From the row compositions (squared row norm 6 + 2·4 = 14) and Lambda = 6: M M^T = 8I + 6J.
* M **1** = 10 **1** and M^T **1** = 8 **1**.
* Hence G **1** = M^T (10 **1**) = 80 **1**, so G J = J G = 80 J. Also
  G^2 = M^T (8I + 6J) M = 8G + 6 (M^T **1**)(**1**^T M) = 8G + 384 J.
* Expanding with J^2 = 15 J gives H^2 = 40 H, and H **1** = (40 - 400 + 360) **1** = 0.
* Entries:
  * H_jj = 40 - 5(8 + 2c_j) + 24 = 24 - 10 c_j;
  * for j != k, H_jk = 24 - 5 g_jk, which is congruent to -1 (mod 5).
* trace H = 360 - 10 · 24 = 120, since sum_j c_j = 24 (twelve rows with two 2s each).

## Step 2 (positivity)
* For every real x: x^T H x = x^T H^2 x / 40 = |Hx|^2 / 40 >= 0. So H is positive semidefinite, and x^T H x = 0
  implies H x = 0.
* H/40 is a symmetric idempotent with trace 3, so rank H = 3.
* Consequences:
  * (a) H_jj >= 0, so c_j <= 2: every column has at most two 2s.
  * (b) H_jk^2 <= H_jj H_kk.
  * (c) Every principal minor of H is >= 0, and every 4 x 4 minor of H vanishes.

## Step 3 (column types)
Since c_j <= 2 and sum c_j = 24 over 15 columns: n_1 + 2 n_2 = 24 and n_0 + n_1 + n_2 = 15. Hence
n_2 = 9 + n_0 >= 9, and n_1 = 24 - 2 n_2. A column with c_j = 2 is called type-2 (H_jj = 4); type-1 has H_jj = 14 and
type-0 has H_jj = 24.

## Step 4 (row relations of H)
* For every column j: sum_k H_jk = 0 (from H **1** = 0), and sum_k H_jk^2 = (H^2)_jj = 40 H_jj.
* For a type-2 column j, put t_k = (H_jk + 1)/5 = 5 - g_jk (an integer) for k != j. Then
  sum_{k != j} t_k = 2 and sum_{k != j} t_k^2 = 6.
  * Proof: sum_{k != j}(5 t_k - 1) = -4 and sum_{k != j}(5 t_k - 1)^2 = 160 - 16 = 144, using 14 terms.
* The multiset of nonzero t_k is therefore {1,1,1,1,-1,-1} or {2,1,-1}. In particular at most four columns k != j have
  H_jk = 4.

## Step 5 (pairs of type-2 columns)
* For type-2 columns j != k: |H_jk| <= 4 by Step 2(b), and H_jk is congruent to -1 mod 5. So H_jk is 4 or -1, i.e.
  g_jk is 4 or 5.
* If H_jk = 4, then (e_j - e_k)^T H (e_j - e_k) = 4 + 4 - 8 = 0. So H(e_j - e_k) = 0: columns j and k of H are
  equal.
* Hence "H_jk = 4" is an equivalence relation on the type-2 columns; call its classes the classes. H is constant on
  each class, and H = -1 between type-2 columns of different classes.
* By Step 4, a class has at most 5 columns.

## Step 6 (Lemma D: 3 x 3 principal minors of H have square determinants)
* Let S be any 3 columns. Write M = [N | P], with P the 12 x 3 submatrix on S and N the 12 x 12 integer submatrix on
  the other columns. Then N N^T = A - P P^T with A = 8I + 6J. Facts used:
  * A^{-1} = (I - (3/40) J)/8;
  * det A = 80 · 8^11 = 2^37 · 5;
  * P^T **1** = 8 **1**.
* By the matrix determinant lemma:

      det(N)^2 = det(A) det(I_3 - P^T A^{-1} P)
               = 2^37 · 5 · det((8 I - P^T P + (24/5) J)/8)
               = 2^37 · 5 · 2^{-9} · det(H[S]/5)
               = 2^28 det(H[S]) / 25.

* So det H[S] = (5 det(N) / 2^14)^2 is an integer that is the square of a rational number, hence a perfect square.

## Step 7 (at most two classes)
* Three type-2 columns from three different classes give H[S] = 5I - J (3 x 3), with determinant 50. That is not a
  perfect square, contradicting Step 6. So there are at most two classes.
* Each class has at most 5 columns (Step 5) and n_2 >= 9 (Step 3). Therefore there are exactly two classes, A and B,
  with |A| + |B| = n_2 in {9, 10} and |A|, |B| in {4, 5}.

## Step 8 (Schur complement on the plane of the classes)
* Fix a in A and b in B. Then Gamma := H[{a,b}] = [[4,-1],[-1,4]], det Gamma = 15, and
  Gamma^{-1} = (1/15)[[4,1],[1,4]].
* For every column k let p_k = (H_ka, H_kb). Define F_kl = p_k^T Gamma^{-1} p_l and Y_kl = H_kl - F_kl.
* (i) Y_kk = det H[{a,b,k}] / 15 >= 0.
* (ii) sum_k p_k p_k^T = 40 Gamma, because its entries are (H^2)_ab etc. So sum_k F_kk = trace(Gamma^{-1} · 40 Gamma) = 80,
  and sum_k Y_kk = trace H - 80 = 40.
* (iii) Y vanishes on the rows and columns a and b; on the other 13 indices it is the Schur complement of the
  invertible block Gamma in H. A Schur complement of a positive semidefinite matrix is positive semidefinite: for any
  x, x^T Y x = z^T H z with z = x - E Gamma^{-1} P^T x, where E = [e_a e_b] and P = H E. By Guttman rank additivity,
  rank Y = rank H - rank Gamma = 3 - 2 = 1. Hence Y = y y^T for a real vector y. (The 2 x 2 conditions
  Y_kl^2 = Y_kk Y_ll alone would not suffice.)
* (iv) Y **1** = 0, because sum_l H_kl = 0 and sum_l p_l = 0. Since sum_k Y_kk = 40 > 0, y != 0, and so sum_k y_k = 0.
* For type-2 columns k, p_k is (4,-1) or (-1,4), so F_kk = 4 = H_kk, Y_kk = 0 and y_k = 0. Hence the sum
  sum Y_kk = 40 runs over the non-type-2 columns only.

## Step 9 (values of p_k on non-type-2 columns)
* Apply Step 4 at a column of a class of size 5. Its four classmates have t = 1, so the multiset is
  {1,1,1,1,-1,-1}. Every column of the other class has t = 0. So on the non-type-2 columns this coordinate of p_k is
  -1 or -6, with exactly two values -6.
* At a column of a class of size 4: three classmates have t = 1, so the multiset is again {1,1,1,1,-1,-1}. On the
  non-type-2 columns this coordinate is: one value 4, two values -6, and all others -1.

## Step 10 (n_2 = 10 is impossible)
* Classes 5 + 5, n_1 = 4, n_0 = 1. The five non-type-2 columns have p_k in {-1,-6}^2, with exactly two -6 in each
  coordinate.
* F_kk = (4 p_A^2 + 2 p_A p_B + 4 p_B^2)/15 equals 2/3, 32/3 or 72/3 for zero, one or two entries -6.
* Step 8(ii) gives sum Y_kk = (4 · 14 + 24) - sum F_kk = 40, i.e. sum F_kk = 40 = 120/3.
* The possible distributions of the four -6 entries over five columns give sum F_kk = 130/3, 140/3 or 150/3. All
  differ from 120/3. Contradiction.

## Step 11 (n_2 = 9 is impossible)
* Classes |A| = 5 and |B| = 4 (names chosen), n_1 = 6, n_0 = 0.
* On the six type-1 columns: p_A has two values -6 and four values -1; p_B has one 4, two -6 and three -1.
* Y_kk = 14 - F_kk >= 0 excludes p = (-6,-6), for which F = 24.
* Step 8(ii) requires sum F_kk = 84 - 40 = 44 = 132/3. The F values are: (-1,-1) 2/3; (-6,-1) 32/3; (-1,-6) 32/3;
  (-1,4) 4; (-6,4) 32/3.
* Case I: the column with p_B = 4 has p_A = -1. The rest are four columns with F = 32/3 and one with 2/3, so
  sum F = 142/3. Contradiction.
* Case II: the columns are
  * k1 = (-6,4);
  * k2 = (-6,-1);
  * k3 = k4 = (-1,-6);
  * k5 = k6 = (-1,-1).

  This gives sum F = 132/3, which is allowed. Here Y_kk = 10/3 for k1..k4 and 40/3 for k5, k6.
  * Write y_k = s_k sqrt(Y_kk) with s_k = ±1.
  * H_{k5 k6} = F_56 + y_5 y_6 = 2/3 ± 40/3 must be an integer, which forces s_5 = s_6.
  * Then sum y_k = sqrt(10/3)(s_1 + s_2 + s_3 + s_4 + 4 s_5) = 0 forces s_1 = s_2 = s_3 = s_4 = -s_5.
  * But then H_{k1 k2} = F_12 + 10/3, with F_12 = (4·36 + (-6)(-1) + 4·(-6) + 4·4·(-1))/15 = 110/15 = 22/3. So
    H_{k1 k2} = 32/3, which is not an integer. Contradiction.
  * Finitary variant, without the rank-one factorisation of 8(iii). This uses only det H[{a,b,k,l}] = 0, i.e.
    Y_kl^2 = Y_kk Y_ll from rank H = 3, together with integrality and Y **1** = 0 from 8(iv).
    * Integrality of H_kl = F_kl ± sqrt(Y_kk Y_ll) fixes every sign in row k5:
      * F_15 = 2/3, so H_15 is -6 rather than 22/3, and Y_15 = -20/3;
      * F_25 = F_35 = F_45 = 7/3, so each H is 9 rather than -13/3, and each Y = +20/3;
      * F_56 = 2/3, so H_56 is 14 rather than -38/3, and Y_56 = +40/3.
    * Y_{k5,l} = 0 for every type-2 column l, since Y_ll = 0.
    * So row k5 of Y sums to (-20 + 20 + 20 + 20 + 40 + 40)/3 = 40 != 0, contradicting Y **1** = 0.

## Conclusion
* Steps 7, 10 and 11 exclude every value of n_2 >= 9.
* Hence no 12 x 15 matrix over {0,1,2} has six 1s and two 2s in each row, column sums 8 and pairwise row inner
  products 6. That is, BTD(12,15;6,2,10;8,6) does not exist (candidate; parent review pending).

## What is used
* Integer linear algebra on the column Gram matrix of a hypothetical design: Step 1, plus symmetric idempotent
  rank = trace.
* The matrix determinant lemma and det(N N^T) = det(N)^2 for an integer square matrix N (Step 6).
* Finite arithmetic (Steps 4, 7, 9-11).
* No computer search over matrices is used. `code/proof_check.py` mechanically re-checks the identities and the
  finite enumeration.
