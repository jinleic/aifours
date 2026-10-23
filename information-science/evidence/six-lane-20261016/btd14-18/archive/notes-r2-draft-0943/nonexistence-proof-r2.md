# Candidate proof r2: there is no BTD(14,18;7,1,9;7,4)

## Status
* CANDIDATE r2, untrusted until parent review. r2 is an editorial revision of `notes/nonexistence-proof-r1.md`
  (sha256 fd508ffbf77d7777e24f5b743589cab34ac17564d30654d471cf048d72287c0f), which is preserved unchanged. The
  mathematics, every equation and every number are those of r1; the change map below lists every difference.
* r1 was written by worker `InfoCyclic100` on 2026-10-17 (host clock PDT), after the lane README freeze (09:25:52) and
  before any Lean work. r2 was written at 09:43 by the same worker, applying exactly the five notational
  clarifications that the parent forwarded from the claude-opus-5-5 review.
* Reviews of r1 (parent files under `institute/review/`, read-only here):
  * gpt-6.1-sol (Codex CLI), hostile review: ACCEPT, no findings (`btd14-18-codex-hostile-review-v1.note.md`);
  * claude-opus-5-5 (Claude CLI), complete review: ACCEPT, no fatal or major finding, five editorial minors
    (`btd14-18-claude-complete-review-v1.note.md`).
* It uses only the contract definition: repeated columns are allowed, and no other assumption is made.
* It starts from the parent's untrusted lead (contract `parent_lead_untrusted`, and the IRC note
  `btd12-15/notes/parent-lead-btd14-18-received.txt`, read-only). The closing argument below is different: it needs
  no class/matching configuration count, no rank argument and no common-centre geometry. It uses Lemma D4 once.
* Exact arithmetic is re-checked by `code/proof_check.py` (written for r1; r2 changes no arithmetic).
* No novelty, priority or significance claim.

## Change map r1 -> r2 (editorial only)
| # | r1 location | r2 |
|---|---|---|
| 1 | line 27 (Step 1) uses g_jk without a definition | the Setting defines g_jk := G_jk |
| 2 | line 57 (Step 6): "Write M = [N \| P]" | "after a column permutation", plus M M^T = N N^T + P P^T for any column ordering |
| 3 | line 16 (Setting): sizes of J and **1** implicit | the Setting states the context-dependent sizes (18, 14, 4) |
| 4 | line 56, Step 6 heading ("perfect-square determinant up to a fixed square factor") | the heading names the identity actually used, 729 · det(N)^2 = 7^10 · det H[S] |
| 5 | line 64 (Step 6): "By the matrix determinant lemma" | names Sylvester's determinant identity det(A - P P^T) = det A · det(I_4 - P^T A^{-1} P) for invertible A, and det(N N^T) = det(N)^2 for square N; line 109 ("What is used") names the same identity |

Besides these five items only the title and this Status section changed.

## Setting
* Suppose M is a 14 x 18 matrix over {0,1,2}. Every row has exactly seven 1s and one 2, every column sums to 7, and
  any two distinct rows have inner product 4. Repeated columns are allowed.
* J denotes all-ones matrices and **1** all-ones vectors. Their sizes are fixed by context: 18 in G, H and
  J^2 = 18 J (Steps 1-5 and 7); 14 in M M^T = 7I + 4J, in A = 7I + 4J and A^{-1}, and for the inner J of P^T J P
  (Step 6); 4 in P^T J P = 49 J and in H[S] (Step 6). No equation is ambiguous.
* c_j is the number of 2s in column j.
* G = M^T M (18 x 18) with entries g_jk := G_jk, and H := 63 I - 9 G + 28 J (integer, symmetric).

## Step 1 (identities)
* Rows have squared norm 7 + 4 = 11 and pairwise inner product 4, so M M^T = 7I + 4J.
* M **1** = 9 **1** and M^T **1** = 7 **1**. Hence G J = J G = 63 J and G^2 = 7G + 4 (7**1**)(7**1**)^T = 7G + 196 J.
* With J^2 = 18 J: H^2 = 3969 I - 567 G + (3528 + 15876 - 31752 + 14112) J = 63 H, and
  H **1** = (63 - 567 + 504) **1** = 0.
* Entries:
  * G_jj = (7 - 2c_j) + 4c_j = 7 + 2c_j, so H_jj = 28 - 18 c_j;
  * for j != k, H_jk = 28 - 9 g_jk, which is congruent to 1 (mod 9).

## Step 2 (positivity tools)
For every integer vector x: 63 x^T H x = x^T H^2 x = |Hx|^2 >= 0. Hence:
* (P1) x^T H x >= 0;
* (P2) x^T H x = 0 implies H x = 0;
* (P3) (x^T H y)^2 <= (x^T H x)(y^T H y), by Cauchy-Schwarz for |Hx|, |Hy|, since 63 x^T H y = (Hx).(Hy).

## Step 3 (column types)
* By P1 with x = e_j, H_jj >= 0, so c_j <= 1.
* The 14 rows contain 14 entries 2, so exactly 14 columns have c_j = 1 (type-1, H_jj = 10) and 4 have c_j = 0
  (type-0, H_jj = 28).

## Step 4 (entries next to a type-1 column)
* For a type-1 column a and any k != a: H_ak^2 <= H_aa H_kk <= 10 · 28 = 280 (P3 with unit vectors), and H_ak is
  congruent to 1 mod 9. So H_ak is in {-8, 1, 10}.
* Row a of H satisfies sum_k H_ak = 0 and sum_k H_ak^2 = 63 · 10 = 630. Over the 17 entries k != a this gives
  sum H_ak = -10 and sum H_ak^2 = 530.
* For h in {-8, 1, 10}, (h - 1)(h + 8) = 162 [h = 10] and (h - 1)(h - 10) = 162 [h = -8]. Summing over k != a:
  * #{k != a : H_ak = 10} = (530 + 7(-10) - 8 · 17)/162 = 324/162 = 2;
  * #{k != a : H_ak = -8} = (530 - 11(-10) + 10 · 17)/162 = 810/162 = 5.

## Step 5 (two type-1 lemmas)
* (E) If a, k are type-1 with H_ak = 10, then x = e_a - e_k has x^T H x = 10 + 10 - 20 = 0. By P2, H x = 0, so
  H_la = H_lk for every l: columns a and k of H are equal.
* (F) If a, k, l are distinct type-1 columns with H_ak = H_al = -8, then H_kl = 10.
  * Proof: y = 2e_a + e_k + e_l has y^T H y = 40 + 10 + 10 - 32 - 32 + 2 H_kl = 2 H_kl - 4. This is >= 0 by P1, so
    H_kl >= 2, and H_kl = 10 because H_kl is in {-8, 1, 10}.

## Step 6 (Lemma D4: the exact complementary-minor identity 729 · det(N)^2 = 7^10 · det H[S])
* Let S be any 4 columns. After a column permutation, write M = [N | P], with P the 14 x 4 submatrix on S and N the
  integer 14 x 14 submatrix on the other 14 columns (equivalently, M M^T = N N^T + P P^T for any column ordering).
  Then N N^T = A - P P^T with A = 7I + 4J.
* Facts used:
  * A^{-1} = (I - (4/63) J)/7;
  * det A = 7^13 · 63 = 7^14 · 9;
  * P^T **1** = 7 **1**, so P^T J P = 49 J;
  * hence I_4 - P^T A^{-1} P = (63 I - 9 P^T P + 28 J)/63 = H[S]/63.
* By Sylvester's determinant identity for this rank-4 update, det(A - P P^T) = det A · det(I_4 - P^T A^{-1} P),
  valid because A is invertible; and det(N N^T) = det(N)^2 because N is square. Hence
  det(N)^2 = det A · det(H[S])/63^4 = 7^10 det(H[S]) / 729, that is, 729 · det(N)^2 = 7^10 · det H[S].

## Step 7 (closure)
* Pick a type-1 column a. By Step 4 it has five entries H_ak = -8, and only 4 columns are type-0. So some type-1
  column b has H_ab = -8 (b != a, since H_aa = 10).
* (i) Every type-1 column c has H_ca + H_cb = 2.
  * For c = a or c = b this reads 10 - 8 or -8 + 10.
  * Otherwise, if H_ca = 10 then by (E) H_cb = H_ab = -8. Symmetrically, if H_cb = 10 then H_ca = -8.
  * If H_ca = -8 and H_cb != 10, (F) at a (with b and c) gives H_bc = 10, a contradiction. Symmetrically for
    H_cb = -8. So the remaining case is H_ca = H_cb = 1.
* (ii) There is a type-1 column u with H_ua = H_ub = 1.
  * At most 3 columns k have H_ak = 10 (a itself and two others, Step 4), and likewise for b.
  * There are 14 type-1 columns, so some type-1 u has H_au != 10 and H_bu != 10. Then u != a, b.
  * By (i), H_ua + H_ub = 2 with both values in {-8, 1}, so H_ua = H_ub = 1.
* (iii) Every type-0 column c has H_ca + H_cb in {-7, 2}.
  * P3 with x = e_a + e_b and y = e_c gives (H_ca + H_cb)^2 <= (10 + 10 - 16) · 28 = 112.
  * The values lie in {-8, 1, 10}, so their sums lie in {-16, -7, 2, 11, 20}. Only -7 and 2 satisfy the bound.
* (iv) The value -7 is impossible.
  * If H_ca + H_cb = -7, then {H_ca, H_cb} = {-8, 1}, and w = H_cu is in {-8, 1, 10}.
  * Take S = {a, b, u, c}. H[S] has rows (10, -8, 1, x), (-8, 10, 1, y), (1, 1, 10, w), (x, y, w, 28), with
    (x, y) in {(-8, 1), (1, -8)}.
  * Its determinant is 3645 for w in {-8, 1} and -2187 for w = 10 (table below).
  * Step 6 would need 729 d^2 = 7^10 · det H[S] for an integer d.
    * For -2187 the right side is negative.
    * For 3645 = 729 · 5, d^2 = 5 · 7^10, which is congruent to 2 mod 3 and so not a square.
  * Contradiction.
* (v) Hence H_ca + H_cb = 2 for all 18 columns c. But sum_c H_ca = sum_c H_cb = 0, because the rows of H sum to 0 and
  H is symmetric. So 0 = sum_c (H_ca + H_cb) = 36. Contradiction.

| x = H_ca | y = H_cb | w = H_cu | det H[{a,b,u,c}] |
|---:|---:|---:|---:|
| -8 | 1 | -8 | 3645 |
| -8 | 1 | 1 | 3645 |
| -8 | 1 | 10 | -2187 |
| 1 | -8 | -8 | 3645 |
| 1 | -8 | 1 | 3645 |
| 1 | -8 | 10 | -2187 |

## Conclusion
No 14 x 18 matrix over {0,1,2} has seven 1s and one 2 in every row, column sums 7, and pairwise row inner products
4. Hence BTD(14,18;7,1,9;7,4) does not exist (candidate; parent review pending).

## What is used
* H^2 = 63H, H **1** = 0, and the positivity tools P1-P3, which follow from 63 x^T H x = |Hx|^2.
* Sylvester's determinant identity det(A - P P^T) = det A · det(I_4 - P^T A^{-1} P) (A invertible), and
  det(N N^T) = det(N)^2 (N square), for one 4-subset S (Step 6).
* Finite arithmetic. No rank or spectral argument, and no computer search over matrices.
