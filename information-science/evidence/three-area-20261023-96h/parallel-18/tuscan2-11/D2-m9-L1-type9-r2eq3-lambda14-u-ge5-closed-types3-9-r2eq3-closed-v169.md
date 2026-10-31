# Original Tuscan-2(11), entire m = 9 distance-two branch, part 56: L1 type 9 with r2 = 3, λ = 14 and u ≥ 5 is impossible, so types 3 and 9 with r2 = 3 are closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-type9-r2eq3-lambda14-u4-closed-v168.md` (SHA256 `4b082a4653d5ab2e2738220d7634eb7c738c318de242fa60e75104b2cc1acc82`). It uses:
- the v158 §1 data with λ = 14;
- the v152 anatomy;
- the overlap exchange;
- the F2-offset conventions of v168 §3.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Forced roles when u ≥ 5

**F1 positions.** t1[j] lies at 10 − u + j and at 56 + u − j. C2 = 56 + u ≥ 61.

| Row | Vertices |
|---|---|
| R1 | t1[u..u+10] |
| R4 | v40, b3 (41), t1[u+14..u+6] |
| R5 | t1[u+6..u−4], pure |
| R6 | t1[u−4..1], b6 (C2), Λ[1..14−u] |
| R7 | Λ[14−u..13], b6, T, ℓ |

**Exchanges.** The cuts are Xp at p ∈ {20, 30, 40, 50, 60}, c1 at 10 and c5 = L(Λ[14−u]) at 70.
- R1 against R4 gives L(t1[u..u+5]) = {X40, w} ∪ L(t1[u+11..u+14]).
- The S_12-copy of R5 is the window [6, 16], which carries t1[u−4..u+6].
  - Against R1 it gives L(t1[u+7..u+10]) = L(t1[u−4..u−1]).
  - Against R0 = ℓ, T_int, b6 (at t ≤ 5), t1[1..u] it gives L(t1[u+1..u+6]) = {w, v} ∪ T_int ∪ L(t1[1..u−5]).

**The resulting placement.** Every label lies once in R1 and once in R4.
- Labels of kind (B) have a vertex in t1[u..u+5] and another in R4 ∖ R1. They are c1, w, X40 and the three labels Y1, Y2, Y3 that share t1[u+11..u+14] with c1.
- The F1-cut labels other than c1, w and X40 form the five labels of t1[u+6..u+10]: X20, X30, X50, X60 and c5.
  - c5's t1-arm passes in R0 and R5. Its cut at 70 covers R6 and R7, so the arm's S_31-passage lies at most at 59.
  - Its second t1-vertex must therefore cover R1 (S_12 in 11–19) and R4 (S_31 in 42–49), which places it in t1[u+7..u+9].

Hence:
- t1[u+6] = X50 and t1[u+10] = X20.
- t1[u+7..u+9] carry {c5, X30, X60}, with X60 = L(t1[u−4]).
- t1[u+1..u+5] carry {w, X40, Y1, Y2, Y3}. The Y's are the labels with two non-arm t1-vertices, so they are F2-cut or v.
- {X40, X50, Y1, Y2, Y3} = {v} ∪ T_int ∪ {the S-labels with arms in t1[1..u−5]}.

**v's two cases.**
- **(α)** v is F1-cut and v ∈ {X40, X50}, with one t1-V and one G2-V.
- **(β)** v is one of the Y's, F2-cut, with two t1-Vs and no G2-V.

**Rows R2 and R3.**
- Positions 26–30 carry {c5, X30, X40, X50, X60}, with X30 at 30.
- Positions 31–39 carry {c1, c5, X20, X50, X60, w, Y1, Y2, Y3}.
- Position 40 carries X40.
- One of these entries is v's b6 = C1.

**R6 and R7.**
- R6 gives L(Λ[1..13−u]) = {c1, X20, X30, w} ∪ T_int.
- R7 says Λ[14−u..13] carry S, with c5 on Λ[14−u].

## 2. F2 rows

**Offsets.** As in v168 §3:
- b6 at 0;
- block 1..15 (t2[1..ℓ2−1], b3 at ℓ2, t3[ℓ3−1..1]);
- b6 at 16;
- the Λ-arm at 17..16 + u, with c5 at 16 + u;
- Λ[13−u..1] at 17 + u..29.

The cuts sit at o, o + 10 and o + 20.

**v needs three F2-rows.**
- In case (α), v's F2-passages are the two b6's and one block vertex (its G2-V). None of them is a cut.
- In case (β), v's passages are the two b6's only, and one of them is its F2-cut.

**o ∈ [7, 9].** Row B = [o + 10, o + 20] lies in offsets 17–29 (Λ only). Rows C and A already contain v, through b6 at 0 and b6 at 16. In case (α), v's G2-V in the block would repeat v in A or C. In case (β), v has no passage in B. Impossible.

**o = 0 or o = 6.** This needs case (β), with the cut on b6. By §1, v's b6 is a Y-entry of positions 31–39, so C1 ∈ [31, 39] and ℓ2 ∈ [6, 14]. Positions 26–30 are t2[ℓ2−5..ℓ2−1], at offsets [ℓ2 − 5, ℓ2 − 1], and X40's vertex v40 lies at offset ℓ2 + 1.
- **o = 0** (row A = [0, 10]):
  - ℓ2 ≤ 9 puts both X40-vertices in row A.
  - ℓ2 = 10 puts b3 on the cut 10.
  - ℓ2 ∈ [11, 14] puts an F1-cut label of {c5, X30, X40, X50, X60} on the cut 10.
- **o = 6** (row A = [6, 16]):
  - ℓ2 ∈ [11, 14] puts both X40-vertices in row A.
  - ℓ2 ∈ [7, 10] puts an F1-cut label on the cut 6.
  - ℓ2 = 6 puts b3 on the cut 6.

**o ∈ [1, 5].**
- Rows: A = [o, o + 10] lies inside the block; B contains b6 at 16; C contains b6 at 0.
- In case (β), v has no passage in A. So this is case (α), and the three cuts carry the three Y's.
- Let D be the member of {X40, X50} other than v.

## 3. Case (α) with o ∈ [1, 5]

**ℓ2 ∈ [6, 14].** Then C1 ∈ [31, 39] is v's b6 among the R3-entries, so v = X50 and D = X40. Positions 26–30 sit at offsets [ℓ2 − 5, ℓ2 − 1], and v40 at ℓ2 + 1.
- **o ∈ [ℓ2 − 9, ℓ2 − 5]:** X40 occurs twice in row A.
- **o ≥ ℓ2 − 4:** the cut at o is a non-Y label (o ≤ ℓ2 − 1), or b3 (o = ℓ2).
- **o ≤ ℓ2 − 10:** the cut at o + 10 is b3 (o + 10 = ℓ2), or a non-Y label in [ℓ2 − 5, ℓ2 − 1].

**ℓ2 = 15.** Then C1 = 40, so v = X40, and positions 26–30 sit at offsets 10..14. Every o ∈ [1, 5] puts either a non-Y label (offsets 11–14) or b3 (offset 15) on the cut o + 10.

**ℓ2 = 5.** Then C1 = 30, so v = X30, contradicting v ∈ {X40, X50}.

**ℓ2 ∈ [1, 4].**
- C1 ∈ [26, 29], and positions 30–40 are t3[5−ℓ2..15−ℓ2]. Their F2-copy is W3 = [ℓ2 + 1, ℓ2 + 11], carrying all labels, with X40 at ℓ2 + 1 and X30 at ℓ2 + 11.
- The block offsets 1..ℓ2 − 1 and ℓ2 + 12..15 carry labels from {c5, X60, D}.
- **o = ℓ2 + 1:** X40 lies on a cut.
- **o < ℓ2 + 1:** L([o, ℓ2]) = L([o + 11, ℓ2 + 11]) ∋ X30, but [o, ℓ2] carries only labels from {c5, X60, D, w}.
- **o > ℓ2 + 1:** the cut at o + 10 ∈ [ℓ2 + 12, 15] carries a non-Y label.

Every case is a contradiction.

## 4. Result

**WRITTEN:**
- L1 type 9 with r2 = 3, λ = 14 and u ≥ 5 is impossible.
- With v158, v159 and v168, **L1 type 9 with r2 = 3 is impossible**. By the mirror (v156 §3), so is type 3 with r2 = 3.
- Types 3 and 9 are now open only at r2 = 4, in the region of v166.

**OPEN (m = 9, L1):**
- types 3 and 9 with r2 = 4 (v166 region);
- type 7 with r2 ∈ {3, 4};
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
