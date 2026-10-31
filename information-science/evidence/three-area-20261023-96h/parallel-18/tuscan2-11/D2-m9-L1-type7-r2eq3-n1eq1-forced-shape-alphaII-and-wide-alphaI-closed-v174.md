# Original Tuscan-2(11), entire m = 9 distance-two branch, part 61: L1 type 7 with r2 = 3 — P2 ≥ 31 and P3 ≤ 49; the forced shape when v's G2-V lies on t1; two sub-cases closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-type7-r2eq4-lemmaT7prime-nLambda-cases-closed-v173.md` (SHA256 `0f399e93d91f26c7f5b0e7e9d8614601e84668f0b053360151e6a95f59ab93d8`). It uses:
- the data and notation of v172 §1;
- Lemma DP-1 (v114 §2);
- the consecutive-rows property and OL.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. P2 ≥ 31 and P3 ≤ 49 (type 7, r2 = 3, every case)

**c1's two t2-vertices.** c1 is F1-cut, so a = 2. A T-vertex would repeat c1 in R0 or R7, so both of its G1-vertices lie on t2.

**c1's S_12-passes.** These two passes lie in two distinct rows. Neither row is R0 or R1 (c1's cut is at 10), and neither pass sits on a cut. If P2 ≤ 30, the S_12-run [P1 + 1, P2 − 1] lies in [12, 29], so both passes would fall in R2. Hence **P2 ≥ 31**.

**c5.** The same argument for c5 (cut at 70) with the S_23-run gives **P3 ≤ 49**.

## 2. v's G2-V on t1 (c′ = 0, n1 = 1): the forced shape

**v's F1-passages.** In F1-order, v's passages are:
- t (R0);
- t1V;
- t2V12;
- P2 and P3;
- t2V23;
- P5 (R7).

**The cut.** Exactly one of these passages is v's cut.
- By §1, P2 ∈ [31, 39] (P2 = 40 would force P3 ≥ 51) and P3 ∈ [41, 49].
- So no cut precedes P3, and the cut is t2V23 at 60.

**The forced shape.**
- t1V lies in R1, t2V12 in R2, P2 in R3 and P3 in R4.
- **v = X60**, and v's t2-vertex is t2[ℓ3 + 5], whose S_12-pass 20 + δ lies in R2 (δ := ℓ1 − ℓ3 ∈ [1, 9]).
- ℓ1, ℓ3 ∈ [6, 14].

**F2.**
- v's passages b6(0), b6(λ) and t1V lie in consecutive rows A, D and C, so D = [κ1, κ1 + 10] ∋ λ.
- C contains t1V, so its upper cut κ3 = 30 − x lies on t1 (on t1[x]).
- A = t1[x..1], b6(0), Λ[1..10−x].
- Either:
  - **(α-i)** κ2 = λ + y lies on t3: D = Λ[10−x..λ−1], b6(λ), t3[1..y] and C = t3[y..ℓ3−1], b3, t1[ℓ1−1..x];
  - **(α-ii)** κ2 lies on t1[x + 10]: C = t1[x..x+10] is pure, and D contains all of t3 and b3.
- x ≠ u, since c1 is not an F2-cut. Likewise y ≠ u.

## 3. α-ii is impossible

**x ≥ u + 1.**
- ℓ1 ≥ x + 11 and ℓ1 ≤ 14 force u = 2, x = 3 and ℓ1 = 14.
- Then R1 = t1[2..12] and C = t1[3..13] have shift 1.
- OL gives c1 = L(t1[2]) = L(t1[13]). But t1[13] is the F2-cut κ2, which is impossible for the F1-cut label c1.

**x ≤ u − 1.**
- The F1-copy W_C = [10 − u + x, 20 − u + x] of C carries all labels.
- Against R1, W_C ∖ R1 = t1[x..u−1] carries S-labels only.
- R1 ∖ W_C consists of one of:
  - t1[x+11..u+10], when P1 ≥ 21. These vertices lie in D's t1-part, which by the arm exchange against R7 carries T_int only.
  - a set containing b3, when P1 ≤ 19 (P1 ≥ 21 − (u − x)). This puts w among the S-labels.
- Either way, impossible.

## 4. α-i: the wide case closes when P1 ≤ 19

**Setting.** Assume x ≥ u + 1 and y ≥ u + 1.
- The arm exchanges (A against R0, D against R7) give L(Λ) ⊆ {w} ∪ T_int, and all three F2-cut labels (on t1[x], Λ[10−x], t3[y]) are T_int.
- P1 ≤ 19 and P4 ≤ 59 cannot hold together: P4 ≤ 59 needs ℓ3 ≥ u + 11 ≥ 13, so ℓ1 = 14 and u = 2, and then P1 = 22.

**Suppose P1 ≤ 19 and P4 ≥ 61.** Then R2 and R5 are pure t2-rows.
- R3 against R4 (sharing b6, position 40 and t2[1..ℓ3−5]) gives L(t2[ℓ3−4..ℓ1−5]) = L(Λ[1..P3−41]) ⊆ {w} ∪ T_int. So X30 = L(t2[ℓ1−5]) ∈ T_int. Also X40 lies on Λ, so X40 ∈ T_int.
- **S-labels.**
  - An S-label other than c1 and c5 meets R2–R5 only through t2. Its third G2-vertex lies in R1 or in R6.
  - So it needs a t2-pass on a cut, and is some Xp.
  - X20 is excluded: t2[ℓ1+5] has its S_23-pass at 60 + δ ∈ R6, leaving R4 or R5 uncovered. X30 and X40 are T_int, and X60 = v.
  - So S ⊆ {c1, c5, X50}, and u ≤ 3.
- **F1-cut T_int labels.**
  - Each has a single t2-vertex. It must give the S_12-pass in R2 and the S_23-pass in R5 (or a cut at 30).
  - So its three G2-vertices together with its cut must cover R1, R3, R4 and R6. That needs the cut at 30 (X30) or at 40 (X40).
  - Hence there are at most 2 such labels, while there are 9 − u − 3 = 6 − u ≥ 3. Impossible.

## 5. Result

**WRITTEN:**
- Type 7 with r2 = 3 always has P2 ≥ 31 and P3 ≤ 49.
- With v's G2-V on t1, the shape of §2 is forced.
- α-ii is impossible.
- α-i with x, y ≥ u + 1 and P1 ≤ 19 is impossible.
- The mirror (t1 ↔ t3) gives the same for v's G2-V on t3.

**Remaining for type 7, r2 = 3:** α-i, in one of three forms:
- x, y ≥ u + 1 and P1 ≥ 21. Then ℓ1 ≥ u + 11 and ℓ1 ≤ 14, so u ≤ 3, ℓ1 ∈ {13, 14} and R1 = t1[u..u+10]. Further restrictions:
  - **Shift.** OL of R1 with C gives a block of size x − u. Its C-side contains b3, so size 1 is impossible, and sizes 2–3 are excluded by (E). So x − u ≥ 4.
  - **S-labels.**
    - R1 is pure t1, so every S-label other than c1 has its third G2-vertex in R1.
    - For those other than c5, R2–R6 must then be covered by 4 t2-passes and a cut:
      - the S_12-run lies in [22, 38], so its two passes give R2 and R3;
      - the cut must therefore be an S_23-pass at 50 (60 is v's).
    - So S ⊆ {c1, c5, X50}.
- x ≤ u − 1, which forces P1 ≤ 19: otherwise R1 = t1[u..u+10] would lie inside C, which contains b3.
- y ≤ u − 1, which forces P4 ≥ 61.

Each of these comes with its mirror.

**OPEN (m = 9, L1):**
- type 7 with r2 = 3 (the α-i forms above) and with r2 = 4 (a G2-V of v on t1 or t3, v173);
- types 2 and 12;
- types 1 and 11 with r1 ∈ {4, 5, 6};
- type 8 with r1 ∈ {3, 4}, and with r1 = 5 and ℓ1 − u ∈ [11, 19].

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
