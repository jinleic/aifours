# Original Tuscan-2(11), entire m = 9 distance-two branch, part 55: L1 type 9 with r2 = 3, λ = 14 and u = 4 is impossible (type 3 by the mirror)

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues:
- `D2-m9-L1-type9-r2eq3-lambda14-u-le-3-closed-v159.md` (SHA256 `3bfe0cbb24972d90c9b77d4d69272a1d5ae4aececb00d1c8ab0369d741259d54`);
- `D2-m9-consolidated-status-L1-open-cell-atlas-v167.md` (SHA256 `bad9940e229cc254441587898b67f66bc24b96030bfeae8630c163b533247f9b`).

It uses the v158 §1 data with λ = 14, the v152 anatomy and the overlap exchange. Rows of F2 are cut every 10 positions of F2.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. F1 when u = 4

t = 6, ℓ1 = 19 and ℓ2 + ℓ3 = 16. t1[j] lies at 6 + j (S_12) and at 60 − j (S_31). b3 lies at 25 and 41, and b6 at 6, C1 = 25 + ℓ2, 60 and 74. Λ[k] lies at 60 + k.

| Row | Vertices |
|---|---|
| R0 | ℓ, T[1..5], b6, t1[1..4] |
| R1 | t1[4..14] |
| R2 | t1[14..18], b3, then positions 26–30 |
| R3 | positions 30–40 |
| R4 | v40 (position 40), b3, t1[18..10] |
| R5 | t1[10..1], b6 |
| R6 | b6, Λ[1..10] |
| R7 | Λ[10..13], b6, T, ℓ |

**Cuts.**
- c1 = L(t1[4]) at 10, X20 = L(t1[14]), X30, X40 = L(v40), X50 = L(t1[10]), and c5 = L(Λ[10]) at 70.
- The cut at 60 is b6, so **v's cut is at 60**. Hence c = 1, v has one t1-V and one G2-V, and the three F2-cut labels are not v.

## 2. The label roles

**The exchange R1 / R4.** It gives L(t1[4..9]) = {X40, w} ∪ L(t1[15..18]).
- c1 needs R4. Its second t1-vertex has S_31-passage in 42–49 and S_12-passage outside R1, so it is in t1[15..18].
- Any other label on t1[15..18] carries two non-arm t1-vertices. Such a label is neither T_int nor S, so it is F2-cut. Call these labels Y1, Y2, Y3.

**Placement on t1.**
- t1[5..9] carries {w, X40, Y1, Y2, Y3}.
- c5's second t1-vertex lies in t1[11..13] (v158 §1).
- v's t1-V must cover R1 and R4, so it also lies in t1[11..13].
- Hence t1[10..14] carries X50, then {c5, v, X30} in some order, then X20.

**Types of the labels.**
- An S-label among X40, X50 or the Y's would occur twice in R5. Its arm passes at 57–59, and its other vertex at 51–55, or the cut at 50.
- So T_int = {X40, X50, Y1, Y2, Y3} and S = {c1, c5, X20, X30}.

**Row content forced by the above.**
- R6: L(Λ[1..9]) = {c1, w, X20, X30, X40, X50, Y1, Y2, Y3}.
- R7: Λ[11..13] carry {c1, X20, X30}.
- R2: positions 26–30 carry {c5, X30, X40, X50, v}, with X30 at 30.
- R3: positions 31–39 carry {c1, c5, X20, X50, v, w, Y1, Y2, Y3}, and position 40 carries X40.
- So positions 26–40 hold the multiset {c5², X40², X50², v², X30, c1, X20, w, Y1, Y2, Y3}. One of the two v's is b6 = C1.

## 3. F2 = S_23 P− (30 positions)

**Offsets.** Measured from the b6 at z:
- b6 at 0;
- the block t2[1..ℓ2−1], b3 (offset ℓ2), t3[ℓ3−1..1] at offsets 1..15;
- b6 at 16;
- Λ[k] at offset 30 − k, so Λ[13..11] lie at 17–19 and Λ[10] (c5) at 20.

**Block content.** The block carries the F1 positions 26–40 with C1 replaced by b3. Its multiset is {c5², X40², X50², v, w², X30, c1, X20, Y1, Y2, Y3}.

**The cuts.**
- They sit at offsets o, o + 10 and o + 20.
- No cut lies at offsets 0 or 16 (v is F1-cut) or at 17–20 (F1-cut S-labels). So o ∈ [1, 5]. Every cut vertex is one of the Y's.
- **o ≠ 1.** Row C = [o + 20, o + 30] must contain c5. c5's F2-vertices are Λ[10] (offset 20, in row B only) and two block vertices, which forces a block vertex at offsets 1..o − 1. That range is empty when o = 1.
- So **o ∈ [2, 5]**.

**The excluded block positions.** Row A = [o, o + 10] lies inside the block and carries all 11 labels. So the four block positions outside row A carry exactly the duplicated labels {c5, X40, X50, w}.

## 4. ℓ2 ∈ [6, 14]

**Positions.** F1 positions 26–30 are t2[ℓ2−5..ℓ2−1], at F2 offsets ℓ2 − 5..ℓ2 − 1. v's G2-V lies there, since C1 ≥ 31. X40's other vertex v40 = t3[ℓ3−1] lies at offset ℓ2 + 1.

**The three ranges of o.**
- **o ∈ [ℓ2 − 9, ℓ2 − 5].** Row A ⊇ [ℓ2 − 5, ℓ2 + 1], so X40 occurs twice in row A. Impossible.
- **o ≥ ℓ2 − 4.**
  - If o ≤ ℓ2 − 1, the cut at offset o carries a label from {c5, X30, X40, X50, v}, which is not a Y.
  - o = ℓ2 puts b3 on a cut.
  - o ≥ ℓ2 + 1 contradicts o ≤ 5 < ℓ2.
- **o ≤ ℓ2 − 10.**
  - o = ℓ2 − 10 puts b3 on the cut o + 10.
  - Otherwise ℓ2 − 5 ≤ 12 ≤ o + 10 ≤ ℓ2 − 1, so the cut at o + 10 carries a non-Y label.

## 5. ℓ2 ∈ [1, 4], and ℓ2 ∈ {5, 15}

**ℓ2 ∈ [1, 4].**
- Here C1 = 25 + ℓ2 ∈ [26, 29], and F1 positions 30–40 are t3[5−ℓ2..15−ℓ2].
- Their F2 copy is the window W3 = [ℓ2 + 1, ℓ2 + 11], which carries all labels, with X40 at ℓ2 + 1 and X30 at ℓ2 + 11.
- The block offsets 1..ℓ2 − 1 and ℓ2 + 12..15 carry labels from {c5, X40, X50}.
- **o = ℓ2 + 1:** W3 is row A, so X40 lies on a cut. Impossible.
- **o < ℓ2 + 1:** overlap gives L([o, ℓ2]) = L([o + 11, ℓ2 + 11]) ∋ X30. But [o, ℓ2] carries only labels from {c5, X40, X50, w}. Impossible.
- **o > ℓ2 + 1:** the cut at o + 10 ∈ [ℓ2 + 12, 15] carries a label from {c5, X40, X50}, which is not a Y. Impossible.

**ℓ2 = 5 or 15.** These put C1 at 30 or 40, a second cut of v. Impossible.

## 6. Result

**WRITTEN:**
- L1 type 9 with r2 = 3, λ = 14 and u = 4 is impossible. By the mirror (v156 §3), so is type 3.
- With v158 and v159, **types 3 and 9 with r2 = 3 survive only with λ = 14 and u ≥ 5**.

**OPEN (m = 9, L1):** as in the v167 atlas, with the r2 = 3 cell of types 3 and 9 narrowed to u ≥ 5. The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
