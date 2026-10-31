# Actual Tuscan11, m = 9, L3, one face (W1), c = 60, V2: the sub-cases with A3 in row 9 or row 8 are excluded

Actual `/bin/date` before this body: **Mon Oct 26 14:41:00 PDT 2026**. InfoRecursiveMDS18-2.

**Status.** NEW exact WRITTEN CANDIDATE: not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO.

**Scope.** Tuscan-1-only support-ladder work on R6 (all m ≥ 9, no Tuscan-2 cap). This is a necessary-case exclusion, not a construction or a Tuscan-2 statement. It is a separate, ungated successor line, outside the v19–v49 and v150b freezes.

## 1. Imports, and the reachability tool

**Imports.**
- **v103** (SHA256 `6d3155a8de596c58dfcb36401503e330352be7be5028a7ff7deeadbc61a5a72c`):
  - the V2 forced shape at c = 60: 11 ≤ p ≤ 14, q = p − 5 ≤ 9, the P-w at {1,5};
  - the Y-v passages, with first passages in rows 2 and 3;
  - the Y-w passages, with second passages in rows 7 and 8.
- **v96:** the matching method.

**The reachability tool.** By F2 (v12 §1), every two labels x ≠ y are joined by exactly one split edge. So some vertex labelled x is adjacent to some vertex labelled y. In a skeleton where no x-vertex is adjacent to any y-vertex, we have a contradiction.

## 2. A3 in row 9

**Forced shape (v103 §3.2).**
- The Y-v and Y-w vertices are all on Y1, with types (2,8) and (3,7).
- b_w's first passage lies in row 4, and Y2 has the single type {4,9}.

**The order δ < 0.** The Y1 types are (1,9), (1,8), (2,8), (2,7), (3,7), (3,6) and (4,6). The Y1[G2+20]-label has cut rows {3,4,6}. Then:
- row 10 must pair with row 0, through T;
- row 5 must pair with row 1, through P2;
- row 9's partners are 1 (via Y1), 6 (via Q2) and 4 (via Y2), and all of them are used.

Contradiction.

**The order δ > 0.**
- In every option, the Y1[G2]-label has the forced vertices Y1[G2], P1, Q1, (3,8) and (4,7). Its matching is P1, Q1, (3,8), (4,7).
- The w-vertices are:
  - ℓ, next to T;
  - b_w, next to Q(u..], Y1(4,6) and Y2 or b″;
  - P-w in P(u,10);
  - Y-w in (2,8) and in (3,7).
- None of these is adjacent to any vertex labelled Y1[G2]. The Y1 segments are separated by the cuts Y1[G2+10], Y1[H9+10] and Y1[G2+20], and P1 is separated from P2 by P[u].
- So w and the Y1[G2]-label are never joined. Contradiction.

## 3. A3 in row 8

**Forced shape.**
- The Y-v vertices are (2,7) on Y1 and (3,9) on Y2.
- b_w's first passage lies in row 3.
- The Y-w vertices are (2,7) on Y1 and (4,8) on Y2.

**Orders.** Let σ compare G2 with H8 (Y1), and τ compare K4 with K9 (Y2).

- **σ < 0.** The Y1[G2+10]-label has cut rows {2,3,6}. It forces 1–7. Then row 9 can pair only with row 4, and only when K9 < K4. After that, row 8 has no partner. Contradiction.
- **σ > 0 with K4 < K9.** The Y1[H8+10]-label has cut rows {3,6,7}. Row 9 has no partner. Contradiction.
- **σ > 0 with K9 < K4.**
  - The Y1[G2]-label's matching is forced: P1, Y2(4,9), Y1(3,7), Q1.
  - The w-vertices are ℓ, b_w (next to Q(u..], Y1(3,6) and Y2(3,9)), P-w in P(u,10), Y1-w in (2,7) and Y2-w in (4,8).
  - None of them is adjacent to a Y1[G2]-labelled vertex. Contradiction.

## 4. Result

**WRITTEN, Tuscan-1 necessary cases, L3 with one face at c = 60, V2:** A3 in row 9 and A3 in row 8 are impossible.

**Still open in L3 W1:** c = 60 with V2 and A3 in row 7, and all of c = 50.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
