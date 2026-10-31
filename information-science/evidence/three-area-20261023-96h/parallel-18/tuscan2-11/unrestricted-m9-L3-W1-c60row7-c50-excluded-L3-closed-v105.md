# Actual Tuscan11, m = 9, L3, one face (W1): c = 60 with A3 in row 7, and c = 50, are excluded; line L3 is closed

Actual `/bin/date` before this body: **Mon Oct 26 14:44:20 PDT 2026**. InfoRecursiveMDS18-2.

**Status.** NEW exact WRITTEN CANDIDATE: not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO.

**Scope.** Tuscan-1-only support-ladder work on R6 (all m ≥ 9, no Tuscan-2 cap). This is a necessary-case exclusion, not a construction or a Tuscan-2 statement. It is a separate, ungated successor line, outside the v19–v49 and v150b freezes.

## 1. Imports

- **v100** (SHA256 `86cb5e2723ae0fbcf3be7090a662ac6df461ca38538cce4ac9c528453788b591`): the W1 face and the stretch counts.
- **v103** (SHA256 `6d3155a8de596c58dfcb36401503e330352be7be5028a7ff7deeadbc61a5a72c`): the forced V2 shape at c = 60.
- **v104** (SHA256 `bba96d7709e99be96dd1c51b52b9369863c507d3457697ee02a1a5d2a95b5b90`): the reachability tool. Every label pair needs an adjacent pair of vertices (F2).
- **v96:** Lemma VL and the matching method.

## 2. c = 60, V2, with A3 in row 7

**Forced shape.**
- Rows 8 and 9 need their v from Y2. So b_w's first passage lies in row 2.
- Y2 carries the v-vertices of types (2,9) and (3,8) and the w-vertices of types (3,8) and (4,7).
- Rows 3 and 8 are pure Y2 rows. Y2 has bwd cuts K4 and K3 = K4+10 (at positions 40 and 30), and fwd cuts K8 and K9 = K8+10 (at positions 80 and 90).
- Y1 has the single forward cut G2 (at position 20) and the single backward cut H7 (at position 70).

**Case K4 < K8.** The Y1[G2]-label has cut rows {1,2,7} (if G2 < H7) or {1,2,6} (otherwise).
- In the first case, row 4 has no partner left: P3 needs row 1, and (4,7) needs row 7.
- In the second case, row 9 has no partner left: Q2 needs row 6, and (2,9) needs row 2.

Contradiction.

**Case K8 < K4, with G2 > H7.** The Y1[G2]-label (cut rows {1,2,6}) leaves row 5 without a partner. Contradiction.

**Case K8 < K4, with G2 < H7.**
- The matchings force the Y1[G2]-label onto the vertices (4,8), (3,9), Q1 and P1.
- w's vertices are:
  - ℓ, next to T;
  - b_w, next to Q(u..], Y1(2,6) or Y1[H7], and Y2(2,9) or Y2[K3];
  - P-w in P(u,10);
  - Y2-w in (3,8) and in (4,7).
- No w-vertex is adjacent to a Y1[G2]-labelled vertex:
  - the cuts Y2[K8], Y2[K4], Y2[K9] and Y2[K3] separate the relevant Y2 segments;
  - P[u] and Q[u] separate P1 and Q1 from w's P-vertex and Q-vertex.

Contradiction.

**So c = 60 is impossible.** This combines v103 and v104 with the cases above.

## 3. c = 50

### 3.1 Forced shape

**Placements from the stretch counts (n_Y = n_Q = 1, m_P = m_Y = m_Q = 1).**
- Lemma VL gives p ≤ 20 − t and q = p + 5 ≥ 16. The Q-v lies in Q(10, u+10), in rows {6,9}. The Q-w lies in Q(u,10), in rows {5,9}.
- b″'s three passages are in row 1, row 3, and row 7 or 8.
- The P-w occupies rows {1,4}.
- A pure-Q row 6 would lack a w. So p ≤ 14, and b_w's passages lie in row 6 (second passage) and row 8 (third passage).

**The rows of the Y-vertices.**
- The Y-v has first passage in row 2 and second passage in row 7 or 8.
- The Y-w has first passage in row 2 or 3 (whichever does not hold b_w) and second passage in row 7.

### 3.2 A3 in row 7

**Shape.** b_w's first passage lies in row 2. The Y-v (2,8) and the Y-w (3,7) both lie on Y2.

**Orders.** The Y1[G2]-label forces G2 < H7 and K8 < K3. Otherwise row 9 or row 3 has no partner.

**Contradiction.** The matching of the Y1[G2]-label is P1, Q1, Q3 = Q(10,u+10), (3,8). No w-vertex is adjacent to any of these vertices:
- the Y2-w in (3,7) is separated from (3,8) by the cut Y2[K8];
- the Q-w in Q(u,10) is separated from Q1 and Q3 by Q[u] and Q[10];
- b_w's neighbours lie in Q(u+10..], Y1(2,6) or at Y1[H7], and in Y2(2,8) or at Y2[K3].

### 3.3 A3 in row 8

**Shape.** b_w's first passage lies in row 3. Y2 has the single type {3,8}. The Y-v and the Y-w are both of type (2,7) on Y1.

**Order δ < 0.** The Y1[G3]-label (cut rows {2,3,6}) leaves row 7, or row 9, without a partner. Contradiction.

**Order δ > 0.** The Y1[G2]-label's matching is P1, Q1, Q3, (3,7). No w-vertex is adjacent to these:
- the Y1-w in (2,7) is separated from (3,7) by the cut Y1[G3];
- the Q-w is separated by Q[u] and Q[10];
- b_w's neighbours lie in Q4, Y1(3,6) or at Y1[H7], and in Y2(3,8).

Contradiction.

**So c = 50 is impossible.**

## 4. Result: L3 is impossible

| Part of L3 | Packets |
|---|---|
| W2 | v96–v99 |
| W1, c = 40 | v100 |
| W1, c = 80 | v101 |
| W1, c = 70 | v101, v102 |
| W1, c = 60 | v103, v104, §2 above |
| W1, c = 50 | §3 above |

**Line L3 (3+3 at v, 3 at w) of the m = 9 census is impossible** (WRITTEN, Tuscan-1 necessary case, built on unreviewed bodies v94–v105).

**Still open at m = 9:** L1, L2 with k = 3, and L4-B.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
