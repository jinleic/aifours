# Original Tuscan-2(11), entire m = 9 distance-two branch, part 88: L1 types 12 and 2 with r2 = 2, c′ = 1, ℓ3 ≥ 11 — the case C = 70 is closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-types12-2-r2eq2-arm-window-lemma-two-subcases-closed-v200.md` (SHA256 `47e8b945f4afe3626d2b8c39f6273171b4c6fe466b58272222a2abe8334d2602`) and uses its §1 data and §4 reduction. (PC) is v185 §2 (SHA256 `fb4c5f0ec9763615d80e7ffc590f05d4aee4dc7544f7638a628aff9af3a210ac`): every pair of different labels is joined by exactly one H-edge.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. It uses (R1)–(R2) only.

## 1. The case

**Parameters.** Type 12, r2 = 2, c′ = 1 and ℓ3 ≥ 11, with the window cut C = 70 (v200 §4). So:
- ℓ2 ∈ {19,20,21} and e = P5 − 70 = ℓ2 − 15 ∈ {4,5,6};
- λ − u = 25 − ℓ2 = 10 − e;
- ℓ3 ≤ e + 9 and ℓ1 = 20 − ℓ3 ≤ 9.

**Positions.**
- P3 = 35 + ℓ1 is not the cut 40, because v's only cut is in F2. So ℓ1 ≥ 6 and P3 ∈ [41,44].
- P2 = 10 − u + ℓ1 + ℓ2 ≥ 11 + ℓ2 ≥ 30, and P2 ≠ 30, so P2 ∈ [31,36].
- P4 = P3 + ℓ2 ∈ [61,65], since 60 is a cut and b3 never lies on one.
- P1 ∈ [11,19] and P5 ∈ [74,76].

**F1-passages of the threads.**
- **t2-vertex t2[j].** Its S_12-passage P2 − j lies in R1, R2 or R3, and its S_23-passage P3 + j lies in R4, R5 or R6.
  - If S_12 ∈ R1, then j ≥ P2 − 19 ≥ 12, so S_23 ≥ 53 and lies in R5 or R6.
  - If S_12 ∈ R3, then j ≤ P2 − 31 ≤ 5, so S_23 ≤ 49 and lies in R4.
- **Λ-vertex.** Its P−-passage lies in R3 or R4, and its P+-passage in R7 or R8.

## 2. w

w consists of ℓ (R0, R8), b3 at P1 (R1) and at P4 (R6), its G2-W t3[d] with 1 ≤ d ≤ e − 1 (at P5 − d ∈ [71,75], so in R7, by v200 §4), and two G1-W's.
- The G1-W's must cover R2, R3, R4 and R5.
- A Λ-W would need R7 or R8, so both are t2-vertices.
- The one with S_12 in R3 has S_23 in R4, so the other has S_12 in R2 and S_23 in R5.

Hence **w = {ℓ, b3, t3[d], t2[j1], t2[j2]}**, where:
- P2 − j1 ∈ [31,39] and P3 + j1 ∈ [41,49];
- P2 − j2 ∈ [21,29] and P3 + j2 ∈ [51,59].

## 3. c8

c8 = L(Λ[λ−u]) = L(Λ[10−e]) is the S-label on the F1-cut 80.
- **Its t3-vertex.** By v200 §4 (Rb), L(Λ[1..10−e]) = {Z} ∪ L(t3[e+1..9]). Since c8 ≠ Z, c8's t3-vertex (its G2-vertex in Q0) is some t3[j8] with e + 1 ≤ j8 ≤ 9. It sits at P5 − j8 ∈ [61 + e, 69], in R6.
- **Its arm vertex.** Λ[10−e] has its P−-passage at P3 − 10 + e ∈ [35,40]. The value 40 would be a second cut, so this passage is in R3. Its P+-passage is the cut 80 (R7, R8).
- **The rest.** Its t1-arm vertex t1[i8] lies in R0, with i8 ≤ u − 1 since t1[u] carries c1.
- **Its last two G1-vertices.** These must cover R1, R2, R4 and R5. A Λ would need R7 or R8, so both are t2-vertices. R1 and R2 are reached only by S_12-passages. The one with S_12 in R1 has S_23 in R5 (R6 is already covered). So c8 has:
  - t2[p] with P2 − p ∈ [12,19] and P3 + p ∈ [51,59];
  - t2[q] with P2 − q ∈ [21,29] and P3 + q ∈ [41,49].

## 4. (PC) fails: c8 is not joined to w

| w's neighbour | Why it is not a c8-vertex |
|---|---|
| T_int[1] (via ℓ) | c8 ∈ S |
| t1[ℓ1−1] (via b3) | ℓ1 − 1 ≥ u > i8 |
| t3[ℓ3−1] (via b3) | ℓ3 − 1 ≥ 10 > j8 |
| t2[ℓ2−1] (via b3) | its passages are at P1 + 1 ∈ [12,20] and P4 − 1 ∈ [60,64]. Neither (R1, R5) nor (R2, R4) fits, so it is neither t2[p] nor t2[q]. |
| t3[d±1] | d + 1 ≤ e < j8 |
| t2[j1±1], t2[j2±1] | see the differences below |

The differences:
- p − j2 = (P2 − j2) − (P2 − p) ≥ 21 − 19 = 2;
- j2 − q = (P3 + j2) − (P3 + q) ≥ 51 − 49 = 2;
- q − j1 = (P2 − j1) − (P2 − q) ≥ 31 − 29 = 2;
- p − j1 ≥ 12.

So no vertex of c8 is adjacent to a vertex of w. The arm vertices t1[i8] and Λ[10−e] have only t1-, Λ- or b6-neighbours, and w has no such vertex. This contradicts (PC).

## 5. Result

**WRITTEN:** L1 type 12 with r2 = 2, c′ = 1, ℓ3 ≥ 11 and window cut C = 70 (ℓ2 ∈ {19,20,21}) is impossible. By the mirror (v160 §1), so is the corresponding type-2 case.

**OPEN (m = 9, L1):**
- Types 2 and 12 with r2 = 2:
  - c′ = 1 with ℓ3 ≥ 11 and C = 60 (ℓ2 ∈ {9,10,11});
  - c′ = 0 with b3 inside Q1, or with ℓ3 > 20 − x.
- Types 1 and 11 with r1 ∈ {4,5}.
- Type 8 with r1 ∈ {3,4}.

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
