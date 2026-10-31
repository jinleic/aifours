# Actual Tuscan11, m = 9, L3, W2, option (1,0,1) — excluded; L3 with three faces (W2) closed

Actual `/bin/date` before this body: **Mon Oct 26 14:20:04 PDT 2026**. InfoRecursiveMDS18-2.

**Status.** NEW exact WRITTEN CANDIDATE: not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO.

**Scope.** Tuscan-1-only support-ladder work on R6 (all m ≥ 9, no Tuscan-2 cap). This is a necessary-case exclusion, not a construction or a Tuscan-2 statement. It is a separate, ungated successor line, outside the v19–v49 and v150b freezes.

## 1. Imports

- **v96** (SHA256 `a3d390e5e7c3f66007af04c40c8ef5c1ce6d312f4d8cebfe84251800f3648a91`):
  - the L3 setting and Lemma VL;
  - the W2 identities;
  - the row-pair / matching method.
- **v97** (SHA256 `eb504cf48859a839e2f335c8e40cae7a9a3a812074d206d77e7cc77381b891e2`): the v-neighbour count.
- **v98** (SHA256 `b676880a85a221aafbd58e938197047504c9b83910ec7cc83ec9cb555fb14cbc`): the F3 cut analysis pattern.

**Option (1,0,1)** means: c1 = 1, c2 = 0, a + b = 1, r = (5,4,2), y1 = 15 − t, y2 = 5 + t, p + q = 35 − t, c1′ = 0, c2′ = 1, a′ + b′ = 2, a′ ≥ 1.

**F3** has two rows. Exactly as in v98, its cuts are f and f+10 with j < f < 5+t, where j is the Y2-w index. With h = 10 − f:
- Row_X = Y2[f..4+t], b_w, Y1[14−t..h], containing b_w and the Y1-v;
- Row_Y = Y1[h..1], b″, Y2[1..f], containing b″ and the Y2-w.

## 2. Sub-case (A): a = 1, b = 0

**Parameters.**
- Lemma VL gives q ≤ 9, so p ≥ 26 − t > u + 10. Hence R_1 = P[u..u+10], and the P-v lies in P(10..u+10).
- In F1, R_2 and R_3 need b″ and the Y1-v. If b″ were in R_3, then R_2 would be pure P and would contain no v. So b″ ∈ R_2, giving 26 ≤ t+p ≤ 29.
- In F2, the P-v lies in m2. So b″ lies in m1, giving p ≥ 21.
- Then m2 = P[10..20] is pure and needs a second P-w. Hence a′ = 2 and b′ = 0.

**Rows.**
- F1: R_out; R_1 = P[u..u+10]; R_2 = P[u+10..p−1], b″, Y1[1..G], with G = 30 − t − p; R_3 = Y1[G..14−t], b_w, Q[q−1..u]; R_in.
- F2: R_start = b′, Q[1..q−1], b_w, Y2[4+t..σ], with σ = q + t − 5; m1 = Y2[σ..1], b″, P[p−1..20]; m2 = P[20..10]; R_end.

**Segment types.**

| Segment | Rows | Segment | Rows |
|---|---|---|---|
| P1 = P[1..u−1] | {R_out, R_end} | Q1 = Q[1..u−1] | {R_in, R_start} |
| P2 = P(u..10) | {R_1, R_end} | Q2 = Q(u..q−1] | {R_3, R_start} |
| P3 = P(10..u+10) | {R_1, m2} | T | {R_out, R_in} |
| P4 = P(u+10..20) | {R_2, m2} | | |
| P5 = P(20..p−1] | {R_2, m1} | | |

The cuts are:
- P[u] → {R_out, R_1, R_end}; P[10] → {R_1, m2, R_end}; P[u+10] → {R_1, R_2, m2}; P[20] → {R_2, m1, m2}; Q[u] → {R_3, R_in, R_start};
- Y1[G], Y1[h], Y2[σ] and Y2[f], whose rows depend on the orders G ⋚ h and f ⋚ σ.

**Forced types for v and w.**
- v: b′, b″ = {R_2, m1, Row_Y}, P3, and Y1-type {R_3, Row_X}.
- w: ℓ, b_w = {R_3, R_start, Row_X}, P2, P4, and Y2-type {m1, Row_Y}.

**The four orders.**

*h < G, f < σ.* The Y1[h]-label has cut rows {R_2, Row_Y, Row_X}. m1's partners are R_2 (P5), Row_Y and Row_X, all used. Contradiction.

*G < h, σ < f.* The Y2[f]-label has cut rows {R_start, Row_Y, Row_X}. R_3's partners are R_start, Row_Y and Row_X, all used. Contradiction.

*h < G, σ < f.* The same Y2[f]-label argument applies. Contradiction.

*G < h, f < σ.*
- The nine matchings give exactly four T_int-labels: P[10], P[20], Y2[f] and Y2[σ]. So t = 5 and u = 5. All segment equations are consistent.
- v needs 4 T_int-neighbours. Its possible ones are:
  - T[1];
  - y0 = L(P[10]), reachable only through P[p−1], Y1[1] or the P-v.
- b″'s third neighbour Y2[1] lies in Y2[1,f), whose labels are c1 or the P[u+10]-label (both S) or w.
- The Y1-v sits in Y1(h..], whose labels and boundary labels are S or w.
- So v has at most 2 T_int-neighbours. Contradiction.

**Sub-case (A) is impossible.**

## 3. Sub-case (B): a = 0, b = 1

**Parameters.**
- **Lemma VL** gives q ≥ u+11, a Q-v in Q[11..u+9], and p ≤ u+10. Since L(Q[u+1..10]) ∋ w, also b′ ≥ 1, so a′ = b′ = 1.
- **b_w ∈ R_2.** If not, R_2 is a pure Y1 row with no w, because c1′ = 0. So p ≤ 14, and R_3 = Q[u+10..u] carries the Q-v and the Q-w.
- **q < 20.** In F2 the Q-v lies in m1. If q > 20, then m1 = Q[10..20] has no w. So q < 20.
- Altogether: p ∈ [11,14], t+p ∈ [16,19], q ∈ [16,19].

**Rows.**
- F1: R_out; R_1 = P[u..p−1], b″, Y1[1..G′], with G′ = 20 − t − p; R_2 = Y1[G′..14−t], b_w, Q[q−1..u+10]; R_3 = Q[u+10..u]; R_in.
- F2: R_start = b′, Q[1..10]; m1 = Q[10..q−1], b_w, Y2[4+t..σ′], with σ′ = q + t − 15; m2 = Y2[σ′..1], b″, P[p−1..10]; R_end.

**Forced types for v and w.**
- v: b′, b″ = {R_1, m2, Row_Y}, Q(10..u+10) = {R_3, m1}, and Y1-type {R_2, Row_X}.
- w: ℓ, b_w = {R_2, m1, Row_X}, P2, Q(u..10) = {R_3, R_start}, and Y2-type {m2, Row_Y}.

**Orders.**
- If f > σ′, the Y2[f]-label (rows {m1, Row_Y, Row_X}) leaves R_2 without a partner.
- If h < G′, the Y1[h]-label (rows {R_1, Row_Y, Row_X}) leaves m2 without a partner.
- So G′ < h and f < σ′.

**The count.**
- The matchings give exactly four T_int-labels: P[10], Q[10], Y2[f] and Y2[σ′]. So t = 5.
- v's possible T_int-neighbours are T[1] and the Q[10]-label. The latter is reachable only through b″'s Y2[1], the Q-v at Q[11], or the Y1-v.
- That gives at most 2 against the 4 needed. Contradiction.

**Sub-case (B) is impossible.**

## 4. Result

**Option (1,0,1) of L3, W2 is impossible.** With v97 (option (1,1,0)) and v98 (option (2,0,0)), **L3 with three faces (W2) is impossible** (WRITTEN, Tuscan-1 necessary case).

**Still open at m = 9:** L3 with one face (W1); L1; L2 with k = 3; L4-B.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
