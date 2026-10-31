# Actual Tuscan11, m = 9, L3, one face (W1): c = 80 excluded; c = 70 reduced to one sub-order

Actual `/bin/date` before this body: **Mon Oct 26 14:31:32 PDT 2026**. InfoRecursiveMDS18-2.

**Status.** NEW exact WRITTEN CANDIDATE: not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO.

**Scope.** Tuscan-1-only support-ladder work on R6 (all m ≥ 9, no Tuscan-2 cap). This packet gives necessary-case exclusions and reductions, not constructions or Tuscan-2 statements. It is a separate, ungated successor line, outside the v19–v49 and v150b freezes.

## 1. Imports

- v100 (SHA256 `86cb5e2723ae0fbcf3be7090a662ac6df461ca38538cce4ac9c528453788b591`): the W1 face, the stretch counts, and the table of v-2 / w-2 placements by c.
- v96 (SHA256 `a3d390e5e7c3f66007af04c40c8ef5c1ce6d312f4d8cebfe84251800f3648a91`): Lemma VL and the matching method.
- v97: the neighbour count. Label v has exactly one edge to every other label, through its 10 neighbour slots.

## 2. c = 80 is impossible

Here n_P = 2 and m_P = 3, and no other v-2 or w-2 vertices exist.

### 2.1 Placements

**The second stretch (rows 8 and 9).**
- b″'s third passage A3 lies in row 9, and b_w's passages lie in rows 8 and 9.
- R_start = b′, Q, b_w forces q ≤ 9, so p = q+25.

**Rows 1 and 2.** Both are pure P rows. A P-vertex at index j occupies rows ⌊(t+j)/10⌋ and ⌊(80−j)/10⌋, and these sum to 7 or 8. So the two P-v vertices are forced into rows (1,6) and (2,5), and b″ lies in rows 3 and 4.

**The P-w vertices.** They are forced into rows (1,7), (2,6) and (3,5), with b_w's first passage in row 4.

### 2.2 The two Y1 orders

**Segment types.** P gives {0,7}, {1,7}, {1,6}, {2,6}, {2,5}, {3,5} and {3,4}. Q gives {8,10} and {8,9}. Y2 gives {4,9}. Y1's types depend on the order of its forward cut G″ (row 3/4) and its backward cut H (row 8/9).

**H < G″.** The Y1[H]-label's cut rows are {3,8,9}. Row 4's possible partners are 3 (via P(30..]), 9 (via Y2) and 8 (via Y1), all used. Contradiction.

**G″ < H.**
- The nine matchings make the T_int-labels exactly P[10], P[20], P[30] and Y1[H]. So t = 5.
- No v-vertex is adjacent to a vertex labelled P[30] or Y1[H], except through T[1]: v's 2-vertices lie in P(10,u+10) and P(20,u+20), and b″'s neighbours lie in P(30..], Y1[1,G″) and Y2.
- T[1] can supply only one of these two labels, so v misses a T_int-label. Contradiction.

## 3. c = 70

Here n_P = n_Y = 1 and (m_P, m_Y) = (2, 1).

### 3.1 Forced placements

| Item | Placement |
|---|---|
| q | u+1 ≤ q ≤ 9 |
| p | p = q + 15 |
| P-v | rows (1,5) |
| P-w | rows (1,6) and (2,5) |
| b″ | rows 2 and 4, plus row 8 or 9 |
| b_w | rows 7, 9, plus row 3 or 4 |
| Y-v | first passage in row 3 |

### 3.2 Sub-case (α): A3 in row 8

- The Y-v and the Y-w both lie on Y2. The Y-v occupies rows {3, 9}; the Y-w occupies rows {4, 8}.
- The matchings force the order G3 < H8 and K9 < K4. They make the T_int-labels P[10], P[20], Y1[H8] and Y2[K9]. So t = 5.
- v's possible T_int-neighbours are T[1] and the P[10]-label. Its Y2-vertex sees only S-labels or b_w. Contradiction.

### 3.3 Sub-case (β): A3 in row 9

**Placements.** The Y-v and the Y-w both lie on Y1, with types {3,8}. b_w's first passage lies in row 4. The Y1 types run in the order (2,9), (3,9) or (2,8), (3,8), (4,8) or (3,7), (4,7).

**Three of the four orders fail.**
- **(H9 < G3, G4 < H8):** the Y1[H8]-label leaves row 3 without a partner.
- **(G3 < H9, H8 < G4):** the Y1[G4]-label leaves row 8 without a partner.
- **(H9 < G3, H8 < G4):** the Y1[G4]-label forces rows 8 and 9 both onto row 2.

**The surviving order (G3 < H9, G4 < H8).** The five binary matching options are:
- c1 (Cα);
- the P[10]-label (Yα);
- the P[u+10]-label (Dα);
- the Y1[H9]-label (S or T, Hs);
- the Y1[G4]-label (S or T, Gs).

All segment equations are consistent:

    t = 6 − Hs − Gs,  p = 22 + Yα + Hs,  q = 7 + Yα + Hs,  G3 = 2 + Gs − Yα,
    H9 = 6 + Gs − Yα − Cα − Dα,  y2 = 1 + Cα + Dα,  y1 = 19 + Gs − 2Yα − Cα − Dα − Hs.

**v's T_int-neighbours.**
- The Y1[H8]-label is reachable only through T[1].
- The other T_int-labels are reachable through the Y1-v's two slots and through the P-v or b″ (for the P[10]-label).

So Hs = Gs = 0 is impossible, since it needs 5 against at most 4. The cases with Hs + Gs ≥ 1 survive this count. **They remain open**, as explicit pair-uniqueness skeletons.

## 4. Result

**WRITTEN, Tuscan-1 necessary cases, L3 with one face:**
- c = 80 is impossible.
- At c = 70, sub-case (α) is impossible, and sub-case (β) reduces to one order with three explicit skeleton families (Hs + Gs ≥ 1).

**Still open in L3 W1:** c ∈ {50, 60}, and the c = 70 (β) skeletons.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
