# Triple-layer Gram note v1 (PA(19,8,6) lane info-1): written research only

Written after host clock read 2026-10-18T14:30-0700, following the parent lead of about 14:28. No probe, list or native work was run for this note, and it edits no earlier file. Status: one rigorous lemma with corollaries; NO uniform obstruction; the 151 open M2 cases remain open.

## 0. Hypotheses

- **Array and validity:** a valid array A, with 19 distinct rows and 8 columns over 6 symbols, in which any two rows agree in at most one column.
- **All-P1 case (ms06 or ms09):**
  - c0 columns have block sizes (4,3,3,3,3,3) (P0);
  - m = 8 - c0 columns have block sizes (4,4,3,3,3,2) (P1);
  - L = 3 - m (ms09: m = 3, L = 0; ms06: m = 2, L = 1).
- **Blocks:** a "block" is a cell (c, s), identified with the set of rows having symbol s in column c.
  - QP blocks: the blocks of size 4 or 2. T-blocks: the blocks of size 3.
  - n4(r), n2(r), tT(r): the number of size-4, size-2 and size-3 blocks containing row r; n4 + n2 + tT = 8.
- **Graphs and their Laplacians:**
  - G_QP: the graph on the rows whose edges are the pairs lying in a common QP block; L_QP is its Laplacian.
  - G_lv: the leave graph (pairs agreeing nowhere), with adjacency A_lv, Laplacian L_lv and degrees l(r).
- **Matrices:** J_B is the 19x19 0/1 matrix with ones exactly on B x B (diagonal included). J is all-ones, I the identity.

## 1. Row-agreement Gram identity (verified from incidence)

Let M in {0,1}^(19 x 48) with M[r,(c,s)] = [A[r][c] = s]. Then (M M^T)[r,r'] = #{c : A[r][c] = A[r'][c]}:
- this is 8 when r = r';
- for r != r' it is 1 for an agreeing pair and 0 for a leave pair, by validity.

Hence

    M M^T = 8I + (J - I) - A_lv = 7I + J - A_lv,        and also   M M^T = sum over all 48 blocks of J_B,

since column (c,s) of M is the indicator of block (c,s). For ms09 (A_lv = 0) the eigenvalues are 26 (once, eigenvector 1) and 7 (18 times).

## 2. Lemma TG (triple-layer Gram)

In the all-P1 setting:

    sum over T-blocks of J_T  =  L_QP + L_lv + J - diag(1 + 6 n2(r) - 3 l(r)).        (TG)

In particular the right-hand side is POSITIVE SEMIDEFINITE, since it is a sum of the PSD matrices J_T = 1_T 1_T^T.

**Proof.**
1. *Row identity.* A row in a block of size b agrees with b - 1 rows there, so 3 n4 + 2 tT + n2 = 18 - l. Together with n4 + tT + n2 = 8 this gives n4 - n2 = 2 - l.
2. *QP part.* J_B = |B| I_B - L(K_B), where K_B is the complete graph on B. By validity, distinct blocks share at most one row, so the K_B are edge-disjoint and sum_QP L(K_B) = L_QP. Hence

       sum_QP J_B = diag(4 n4 + 2 n2) - L_QP.

3. *Leave part.* A_lv = diag(l) - L_lv.
4. *Assembly.* By §1, sum_T J_T = 7I + J - A_lv - sum_QP J_B = L_QP + L_lv + J + diag(7 - l - 4 n4 - 2 n2). Substituting n4 = 2 - l + n2 gives 7 - l - 4 n4 - 2 n2 = -1 + 3l - 6 n2. ∎

**Checks.**
- Both sides of (TG) have diagonal tT(r) = 6 + l - 2 n2: deg_QP = 3 n4 + n2 = 6 - 3l + 4 n2, and deg_QP + l + 1 - 1 - 6 n2 + 3l = 6 + l - 2 n2.
- Off the diagonal, the left side is 1 exactly on pairs covered by a triple and 0 elsewhere.

**What is new.** TG is a consequence of validity, like every necessary condition. Its PSD part is a global quadratic constraint that no single clause, local degree count or pair-block condition (GPS) expresses, and it binds the QP layer to the triple layer.

## 3. Corollaries

**C1 (exact reformulation).** Let K = [QP-block incidence], a 19 x b matrix (b = number of QP blocks), and let s be its column-sum vector (block sizes). Then

    (TG is PSD)  <=>  K K^T <= 7I + J - A_lv   (Loewner order).

For ms09 this is further equivalent to Lambda - s s^T/26 <= 7 I_b, where Lambda = K^T K is the block intersection matrix: diagonal |B|, off-diagonal |B ∩ B'| in {0,1}.

*Proof.* sum_QP J_B = K K^T. For ms09, (7I + J)^(-1) = (I - J/26)/7, and K K^T <= A holds iff K^T A^(-1) K <= I. ∎

By interlacing, ms09 then needs lambda_2(Lambda) <= 7.

**C2 (ms09 expansion inequality).** Let S be a set of k rows and N2(S) = sum over r in S of n2(r); recall that sum over all rows of n2 is 6. Then

    cut_QP(S)  >=  k(19 - k)/19 + 36 k^2/361 + 6 N2(S) (1 - 2k/19).

*Proof.* Evaluate (TG) at w = 1_S - (k/19) 1, using sum w = 0 and w^T L_QP w = cut_QP(S). ∎

The same value is obtained from Sum_T (|T ∩ S| - 3k/19)^2 >= 0, using:
- sum_T |T ∩ S| = 6k - 2 N2(S);
- sum_T C(|T ∩ S|, 2) = C(k,2) - e_QP(S);
- 34 triples.

**C3 (ms09 connectivity).** G_QP is connected.

*Proof.* If S is a union of components, then cut_QP(S) = 0. But the right side of C2 is positive for 1 <= k <= 9, and it is symmetric under S <-> complement of S. ∎

Linear counting alone does not give C3: for a component, the crossing-pair count 2(#crossing triples) = k(19 - k) is automatically consistent. C3 needs the second moment.

**C4 (pair-free heuristic, NOT a proof).** If all rows had n2 = 0 (impossible in ms09, where sum n2 = 6), C1 would read lambda_2(4I + A_Gamma) <= 7. Here A_Gamma is the adjacency matrix of the quad intersection graph (11 quads, about 4-regular). So theta_2(Gamma) <= 3 would be required; size-2 blocks perturb this. The inequality alone is satisfiable by some 4-regular graphs on 11 vertices: the circulant C_11(1,2) has theta_2 = 2cos(2π/11) + 2cos(4π/11) ≈ 2.51. I have not studied how theta_2 is distributed over admissible quad layers. Whether any admissible ms09 layer realizes a passing graph is open.

## 4. Exact obstruction to a uniform proof

What is missing: a uniform proof that no admissible QP layer of ms09 or ms06 satisfies TG-PSD. I found none. The reasons are specific:

1. **Layer dependence.** TG involves the FULL QP layer: every P1 4-block and pair as well as the P0 quads. The lane's frozen objects fix only the P0 quads (skeletons) and at most the first P1 column (lists).
   - Unknown QP blocks enter TG with a negative-semidefinite contribution, since sum_T J_T = 7I + J - A_lv - (known) - (unknown).
   - The only generic upper bound, L(unknown) <= diag(4 n4'' + 2 n2''), cancels the n2-dependence. At skeleton level the necessary condition reduces to L_Q0 + J + diag(7 - 4t) >= 0. The test vectors I tried by hand (a single quad indicator; e_h for a t = 5 row, giving 15 + 1 + 7 - 20 = 3) do not violate it.
2. **Good expanders pass.** TG-PSD is a spectral-expansion requirement (C2, C3). QP layers whose quad intersection graph expands well are not excluded by it. Whether such layers are realizable inside ms09/ms06, under the column, class and A/B constraints, is exactly the unresolved finite question.
3. **Rank, parity and rational Gram routes are vacuous at dimension level.**
   - *Rational:* every positive definite rational form in n variables is a sum of n + 3 rational squares (Hasse–Minkowski), and 48 >= 19 + 3, so 7I + J - A_lv has rational 19 x 48 representations.
   - *Finite fields:* over GF(7), M M^T = J, so the row differences are pairwise orthogonal and isotropic and orthogonal to the 8 column indicators. Over GF(2) (M M^T = I + J) and GF(3) I likewise found no dimension or rank contradiction, and none is claimed.
   - *Cut parity:* implied by the even H-degrees (12 - 4 n2 for ms09).
4. **ms06 is weaker.** Leave rows have demand 1 - 3 + 6 n2, which can be negative, so even C3 is not established for ms06.

## 5. Status and what would test it (not authorized now)

- Proven: Lemma TG with exact hypotheses, and C1-C3 (C2 and C3 for ms09). C4 is heuristic.
- No open case is closed. No pruning claim is made. TG has not been evaluated on any configuration.
- **Test that would measure strength** (requires a separate frozen probe and GO, and full QP layers):
  - lambda_min of (TG) on each full layer;
  - a control: TG must hold on the known (13,5,4) L=0 model with its analog constants. For N=13, k=5 the identity's constant changes, so it would need re-derivation first.
- C3/C2 could also serve as pruning constraints inside a future layer enumerator. No such work is requested or authorized here.
