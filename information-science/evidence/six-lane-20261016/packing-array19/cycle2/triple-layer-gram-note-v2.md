# Triple-layer Gram note v2: supplement to v1 (written research only)

Supplements `cycle2/triple-layer-gram-note-v1.md` (SHA-256 `4a68eeef659a05f925d12b0da2221501cc71ed52d4427c0e83483ddb0ee427bc`), which is unchanged. Written after host clock read 2026-10-18T14:4x-0700.

The hypotheses and notation are those of v1 §0, and Lemma TG of v1 §2 is used throughout. No probe, list or native work was run. No open case is closed, and no pruning is claimed.

## C2' (unified expansion bound, ms06 and ms09)

Put c_r = 1 + 6 n2(r) - 3 l(r), so that TG reads L_QP + L_lv + J - diag(c) >= 0. Here Σ_r c_r = 55 for ms09 (Σ n2 = 6, Σ l = 0) and 37 for ms06 (Σ n2 = 4, Σ l = 2).

For a row set S with |S| = k, let C_S = Σ_{r in S} c_r. Then

    cut_QP(S) + cut_lv(S)  >=  C_S (1 - 2k/19) + (Σ_r c_r) k^2 / 361.

*Proof.* Evaluate TG at w = 1_S - (k/19) 1. Then Σ w = 0, w^T L_QP w = cut_QP(S) and w^T L_lv w = cut_lv(S). Also

    Σ_r c_r w_r^2 = (1 - k/19)^2 C_S + (k/19)^2 (Σc - C_S) = C_S (1 - 2k/19) + Σc k^2/361.

The bound is invariant under S <-> complement (w -> -w). For ms09 it is v1's C2. ∎

## C3' (ms06: G_QP is connected)

*Proof.* Suppose S is a union of components of G_QP with 1 <= k <= 18. Then cut_QP(S) = 0 and cut_lv(S) <= 1.

1. **Sizes of closed sets.** For every r in S, all QP-neighbors of r lie in S, and deg_QP(r) = 3 n4 + n2 = 6 - 3l + 4 n2.
   - A non-leave row has degree >= 6.
   - A leave row has degree >= 3, and none of its QP-neighbors is the other leave row, since x and y share no block.
   - So S cannot consist of leave rows only. It contains a non-leave row, hence k >= 7. The same holds for the complement, hence 7 <= k <= 12.
2. **Reduction.** By the symmetry of C2', assume k in {7, 8, 9}.
3. **Contradiction.** C_S >= k - 3·2 >= 1 and 1 - 2k/19 >= 1/19. So the right side of C2' is >= 1/19 + 37·49/361 > 5, whereas the left side is <= 1. ∎

Thus C3 (connectivity of G_QP) holds for BOTH open multisets. This corrects v1 §4 item 4, which said C3 was not established for ms06.

## C5 (ms09: bridging bound for the two quads of a P1 column)

Let A_j, B_j be the two 4-blocks of P1 column j, and S = A_j ∪ B_j (k = 8). Let N2 = Σ_{r in S} n2(r), and let q_AB be the number of the 16 pairs {a, b} (a in A_j, b in B_j) that lie in a QP block of another column. Then

    q_AB <= 6.49 + 1.53 N2,     so q_AB <= 6 when N2 = 0.

Hence at least 16 - q_AB of those cross pairs are covered by triples.

*Proof.*
1. **QP edges inside S.** Pairs inside A_j (or inside B_j) already agree in column j, so no other block contains two of them. Hence e_QP(S) = 12 + q_AB.
2. **The cut.** cut_QP(S) = Σ_{r in S} (6 + 4 n2) - 2 e_QP(S) = 24 + 4 N2 - 2 q_AB.
3. **Apply C2'** (ms09, C_S = 8 + 6 N2): 24 + 4 N2 - 2 q_AB >= 88/19 + 2304/361 + 6 N2 (3/19). This rearranges to the stated bound. ∎

**Comparison.** A priori q_AB <= 11: each of the other 9 quads and 2 pairs contains at most one row of A_j and at most one of B_j. So C5 is a genuine global restriction, but its effect on actual layers is untested.

## Status

- C2', C3' and C5 are rigorous consequences of validity, via Lemma TG.
- None was evaluated on any configuration. Their pruning strength is unknown.
- A uniform obstruction is still missing. The obstruction analysis of v1 §4 items 1-3 stands; item 4 is superseded by C3'.
- The 151 lane-original open M2 cases remain open.
