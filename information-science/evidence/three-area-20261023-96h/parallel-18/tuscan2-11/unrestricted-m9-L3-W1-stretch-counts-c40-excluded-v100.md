# Actual Tuscan11, m = 9, L3, one face (W1): stretch counts and the case c = 40 (excluded)

Actual `/bin/date` before this body: **Mon Oct 26 14:24:16 PDT 2026**. InfoRecursiveMDS18-2.

**Status.** NEW exact WRITTEN CANDIDATE: not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO.

**Scope.** Tuscan-1-only support-ladder work on R6 (all m ≥ 9, no Tuscan-2 cap). This packet gives a necessary-case reduction and exclusion, not a construction or a Tuscan-2 statement. It is a separate, ungated successor line, outside the v19–v49 and v150b freezes.

## 1. Setting

**Imports.**
- v96 (SHA256 `a3d390e5e7c3f66007af04c40c8ef5c1ce6d312f4d8cebfe84251800f3648a91`): §1 (the L3 setting) and §2 (Lemma VL).
- v97 (SHA256 `eb504cf48859a839e2f335c8e40cae7a9a3a812074d206d77e7cc77381b891e2`): the v-neighbour count.

**The face.** In W1, b_w has rotation (Q, Y1, Y2), so there is a single face. Measured from ℓ, its walk is:

- ℓ, T, b′ at t;
- P to b″ at A1 = t+p;
- Y1 to b_w at B1;
- Y2⁻ to b″ at A2;
- P⁻ to b′ at c (the v-cut);
- Q to b_w at B2 = c+q;
- Y1⁻ to b″ at A3;
- Y2 to b_w at B3;
- Q⁻ to b′ at 110−t;
- T to ℓ at 110.

Rows are [10k, 10k+10]. Also c ≡ 0 (mod 10) and t+p+q+y1+y2 = 55.

**Where v and w occur.**
- b′ occupies rows 0, 10, c/10−1 (= R_end) and c/10 (= R_start), so the other 7 rows get their v from b″ (3 passages) and the v-2-vertices (4 passages).
- ℓ occupies rows 0 and 10, so rows 1..9 get their w from b_w (3 passages) and the w-2-vertices (6 passages).

## 2. Stretch counts

Call rows 1..c/10−1 the **first stretch** and rows c/10..9 the **second stretch**.

**Which stretch each passage lies in.**
- No v-2-vertex or w-2-vertex lies on T.
- A 2-vertex on P has both passages in the first stretch.
- A 2-vertex on Q has both passages in the second stretch.
- A 2-vertex on Y1 or Y2 has one passage in each stretch.

**The b″ and b_w passages.**
- b″: two passages (A1, A2) in the first stretch, one (A3) in the second.
- b_w: one passage (B1) in the first stretch, two (B2, B3) in the second.

**The counts.** Write n_P, n_Q, n_Y for the numbers of v-2-vertices on P, Q, Y1∪Y2, and m_P, m_Q, m_Y for the w-2-vertices. Counting rows that still need v or w gives:

    2n_P + n_Y = c/10 − 4,   2n_Q + n_Y = 8 − c/10,
    2m_P + m_Y = c/10 − 2,   2m_Q + m_Y = 8 − c/10,

with m_P ≥ 1, since Lemma VL puts w on P[u+1..10]. Hence **c ∈ {40, 50, 60, 70, 80}**, with:

| c | v-2 placement | w-2 placement |
|---|---|---|
| 40 | n_Q = 2 | (m_P, m_Q) = (1, 2) |
| 50 | n_Y = n_Q = 1 | m_P = m_Y = m_Q = 1 |
| 60 | (n_P, n_Q) = (1, 1), or n_Y = 2 | (2, 0, 1) or (1, 2, 0) |
| 70 | n_P = n_Y = 1 | (m_P, m_Y) = (2, 1) |
| 80 | n_P = 2 | m_P = 3 |

## 3. The case c = 40 is impossible

### 3.1 Placements

Since n_P = 0, Lemma VL gives:
- b″ at A1 in row 1 and at A2 = 40−p in row 2;
- b_w at B1 in row 2;
- q = 15+p, with p ≤ 14 and 16 ≤ p+t ≤ 19.

The two Q-v-vertices are z1 ∈ Q(10, u+10), in rows {5, 9}, and z2 ∈ Q(20, u+20), in rows {6, 8}. The w-vertices are:
- P-w in P(u,10), rows {1, 3};
- Q-w in Q(u,10), rows {4, 9};
- Q-w in Q(u+10, 20), rows {5, 8};
- b_w at B2 in row 6 and at B3 in row 7;
- b″ at A3 in row 7.

### 3.2 Segment types

| Segment | Rows | Segment | Rows |
|---|---|---|---|
| T | {0, 10} | Q[1,u) | {4, 10} |
| P[1,u) | {0, 3} | Q(u,10) | {4, 9} |
| P(u,10) | {1, 3} | Q(10,u+10) | {5, 9} |
| P(10, p−1] | {1, 2} | Q(u+10,20) | {5, 8} |
| Y2 | {2, 7} | Q(20,u+20) | {6, 8} |
| | | Q(u+20, q−1] | {6, 7} |

**Y1, with G = 20−t−p and H the index of Y1's backward cut at position 70.**
- If G < H, the types are {1,7}, {2,7} and {2,6}.
- If H < G, the types are {1,7}, {1,6} and {2,6}.

**Cuts.**
- P[u] → {0,1,3}; P[10] → {1,2,3}; Q[10] → {4,5,9}; Q[20] → {5,6,8}; Q[u+20] → {6,7,8}; Q[u+10] → {5,8,9}; Q[u] → {4,9,10}.
- Y1[G] → {1,2,·} and Y1[H] → {·,6,7}.

### 3.3 The order H < G

The Y1[G]-label has cut rows {1,2,6}. Row 7's possible partners are rows 1, 2 and 6, all used. Contradiction.

### 3.4 The order G < H

**The nine matchings.**

| Label | Vertices |
|---|---|
| P[u] | Q1, Q(10,u+10), Q(20,u+20), one {2,7}-vertex |
| P[10] | T, Q(u,10), Q(u+10,20), Q(u+20..] |
| Q[10] | T, P(u,10), Q(20,u+20), one {2,7}-vertex |
| Q[20] | Q(u,10), T, P(u,10), one {2,7}-vertex |
| Q[u+20] | Q(10,u+10), Q1, P1, P(10..] |
| Q[u+10] | Q1, P1, plus {P(10..], Q(u+20..]} or {Y1 {1,7}, Y1 {2,6}} |
| Q[u] | P1, Q(u+10,20), plus {P(10..], Q(u+20..]} or {Y1 {1,7}, Y1 {2,6}} |
| Y1[G] | P1, Q1, Q(10,u+10), Q(20,u+20) |
| Y1[H] | Q(u+10,20), Q(u,10), T, P(u,10) |

**Label classes.** The T-users P[10], Q[10], Q[20] and Y1[H] are exactly the T_int-labels. So t = 5 and u = 5.

**v's T_int-neighbours.** v needs 4 of them. The possible ones are:
- **b′:** T[1].
- **b″:** P[p−1] and Y1[1] carry S-labels. Y2[1] may carry the Q[10]-label or the Q[20]-label.
- **z1:** inside Q[10..u+10], its only T_int-neighbour is the Q[10]-label.
- **z2:** inside Q[20..u+20], its T_int-neighbours can only be the Q[20]-label and the Q[10]-label.

So the distinct T_int-neighbours lie in {L(T[1]), Q[10]-label, Q[20]-label}: at most 3 against the 4 needed. Contradiction.

## 4. Result

- **WRITTEN:** for L3 with one face, the stretch counts force c ∈ {40, 50, 60, 70, 80}.
- **c = 40 is impossible.**
- **Still open in L3 W1:** c ∈ {50, 60, 70, 80}.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
