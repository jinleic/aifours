# Actual Tuscan11 distinct-centre 4+4, class (a)-II, r_P2 = 3 four/three shape — the T1/T2 thread table (supplies v56 §1's input set)

Actual `/bin/date` before this body: **Mon Oct 26 06:21:45 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36).

## 1. Purpose and disclosed gap

v56 §1 (SHA256 `d1051179578875ea456550802ffe9c441b8d3c96b6d9bc3a6ce6f9627d4d77f9`) starts from "the previously surviving set {19, 20, 21 (p0>=2), 24 (p0<=3), 25, 26}" of Sigma for the four/three shape. No pinned packet derives that set. This is a **citation gap in v56**. v56's bytes are unchanged; this packet supplies the missing derivation.

**Setting** (v56 §1):
- B_j = H1[10j-o0, 10j+10-o0] for j = 0..3, with o0 in 5..10;
- D_i = H2[10i-p0, 10i+10-p0] for i = 0..2, with p0 in 1..4;
- l = |T1| in 1..24, and Sigma = l+o0+p0 in 7..38.

**Imports:**
- rule (R) and the bd clash of v49 (SHA256 `0b02a602b2d03bbea47fc5db072da4d0cba5395900f31c75301dcccadf67ded9`);
- clean pairs, bd chains and the shift-5 lemma of v50 (SHA256 `b7bcd3730661be24c9f1dd218254ff6881821c06ab1402cbbd690f3e7e5ac5bc`);
- boundary coincidence (L3) of v57 (SHA256 `41ae55f5aeff940eadfcd9c947bd43ea7c323b9ef3cc3bf42eee56646d4eaa89`).

## 2. Windows and leaving

The windows are those of v52 §2 (SHA256 `c7d0b41044cda03fb4879c2c2b89594665e2c13dccd52d8cf3aff6868443fc45`), with n = i+j:
- **T1:** B_j = [10j-o0, 10j+10-o0] and D_i = [Sigma-o0-10-10i, Sigma-o0-10i], so k = |10(n+1) - Sigma|.
- **T2:** B_j = [15+o0-10j, 25+o0-10j] and D_i = [10i-Sigma+o0, 10i+10-Sigma+o0], so k = |Sigma+15-10n|.

Leaving the threads (ending exactly at a branch vertex is not leaving):
- **T1:**
  - B_0 always leaves low; B_j leaves high iff Sigma-p0 < 10(j+1).
  - D_0 always leaves high (p0 >= 1). D_1 and D_2 never leave high, and D_i leaves low iff Sigma-o0 < 10(i+1).
- **T2:**
  - B_3 always leaves low, and B_0..B_2 never do; B_j leaves high iff Sigma-p0 > 10j.
  - D_2 always leaves high (p0 <= 4), and D_0, D_1 never do; D_i leaves low iff Sigma-o0 > 10i.

So pairs with i, j >= 1 are clean on T1, and pairs with j <= 2, i <= 1 are clean on T2. For a clean pair, k < 10 is a genuine overlap on the thread.

## 3. Table

**Always-clean pairs with k <= 3:**
- T1: (B_1,D_1) for Sigma in 27..33; (B_1,D_2) and (B_2,D_1) for Sigma in 37..38.
- T2: (B_1,D_1) and (B_2,D_0) for Sigma in 7..8; (B_2,D_1) for Sigma in 12..18.

The remaining values in 7..38 are 9, 10, 11, 19..26 and 34..36. In the table, window starts are given relative to o0 on T2 and relative to -o0 on T1. Every chain path lies inside the thread.

| Sigma | Contradiction |
| --- | --- |
| 9 | T2 bd chain D_0, B_2, D_1, B_1 (starts -9, -5, 1, 5); both k=4 pairs are always clean |
| 10 | T2 shift-5 chain D_0, B_2, D_1, B_1 (starts -10, -5, 0, 5); all three pairs are always clean |
| 11 | T2 bd chain B_2, D_1, B_1, D_2 (starts -5, -1, 5, 9); (B_1,D_2) is clean since Sigma-p0 <= 10 |
| 22 | T2 (B_2,D_2), k = 3, clean iff p0 >= 2; T1 (B_1,D_0), k = 2, clean iff p0 <= 2 |
| 23 | T1 (B_1,D_0), k = 3, clean iff p0 <= 3; T2 (B_2,D_2), k = 2, clean iff p0 >= 3 |
| 21 with p0 = 1 | T1 (B_1,D_0), k = 1, clean |
| 24 with p0 = 4 | T2 (B_2,D_2), k = 1, clean |
| 20 with o0 = 10 | b_v(0) ends B_0, and b_v(K) at H2-position l = 10-p0 is the D_0\|D_1 boundary: a doubled v-cut |
| 34 | T1 bd chain B_1, D_1, B_2, D_0 (starts 10, 14, 20, 24); (B_2,D_0) is clean since Sigma-p0 >= 30 |
| 35 | T1 shift-5 chain D_2, B_1, D_1, B_2 (starts 5, 10, 15, 20); all three pairs are always clean |
| 36 | T1 bd chain D_2, B_1, D_1, B_2 (starts 6, 10, 16, 20); both k=4 pairs are always clean |

**Values that survive the window table.**
- Sigma = 19: on T1 the k = 1 pairs (B_0,D_1) and (B_1,D_0) both leave through a common end. On T2 the only clean k = 4 pair is (B_2,D_1), and every chain through it meets the unclean (D_2,B_1) or (D_0,B_3).
- Sigma = 21 with p0 >= 2, Sigma = 24 with p0 <= 3, and Sigma = 26: every k <= 3 pair is unclean and no chain closes.
- Sigma = 20 with o0 <= 9, and every Sigma = 25: not decided by this table (Sigma = 25 with o0 = 5 also has a T1 shift-5 chain B_0, D_1, B_1, D_0, which is not needed). Both are excluded entirely by boundary coincidence in v56 §2.

## 4. Result

The four/three shape survives the T1/T2 window analysis exactly for:
- Sigma in {19, 21 (p0 >= 2), 24 (p0 <= 3), 26};
- Sigma in {20 (o0 <= 9), 25}, which v56 §2 then removes.

This is the set used in v56 §1. It is invariant under Sigma -> 45-Sigma (with p0 -> 5-p0), as v56 needs. With this packet, v56's reductions rest only on pinned written sources.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
