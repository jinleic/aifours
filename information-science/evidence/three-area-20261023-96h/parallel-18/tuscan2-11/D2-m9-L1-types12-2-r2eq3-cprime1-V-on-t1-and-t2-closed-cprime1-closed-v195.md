# Original Tuscan-2(11), entire m = 9 distance-two branch, part 82: L1 type 12 with r2 = 3, c′ = 1 and V's on t1 and t2 is closed; hence c′ = 1 is closed for types 2/12 with r2 = 3

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-types12-2-r2eq3-cprime1-V-on-t3-and-t2-closed-v194.md` (SHA256 `e536157b9523c34d2ef700d1c869196a290049c801330f5a3abf8ee103b6291e`). It closes (β1-ii), the part of (β1) that v190 left open, using the notation, data and lemmas of v190 §1–§2:
- α = P2 − 30, β = 25 − ℓ1, μ = ℓ1 − 15, κ = 15 − ℓ2;
- (G0), (G-A) with (I1)–(I3), and (G-B).

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. General facts for (β1)

Recall t1V ∈ R1, t2V₁₂ ∈ R2, P2 ∈ R3, P3 ∈ R4, t2V₂₃ ∈ R5 and P5 ∈ R6, with P4 ≥ 52.

**(P1) R1 is a pure t1-row.** If P1 ≤ 19, then R2 = [20,30] lies strictly between P1 and P2 and is a pure t2-row. w would miss R2: its b3 lies at P1 ∈ R1 and P4 ∈ R5; its single G1-W is t2[jw] with jw < α, whose S_12 lies in R3; and R2 has no G2. P1 = 20 would put b3 on a cut. So P1 ≥ 21, and R1 = t1[u..u+10] with ends c1 and X20 := L(t1[u+10]).

**(P4) P4 ≤ 59.** If P4 ≥ 61, then R5 is a pure t2-row, which w misses in the same way. P4 = 60 would put b3 on a cut. So ℓ1 + ℓ2 ≤ 34, and R6 = t3[ℓ2−5..1], b6, Λ[1..κ] (v190 §2).

## 2. (β1-ii): t1V on an F2-cut

b6 lies inside Q0 = [−x, 10−x], and t1V = t1[10+x] lies on the cut 20 − x. t1V ∈ R1 means 20 − u + x ≤ 19, so x ≤ u − 1, and s\* := L(t1[x]) is an F2-cut S-label.
- **The F2-rows.** Q2 = t1[x..x+10] is a pure t1-row. DP★ puts b3 inside Q1, so Q0 = t1[x..1], b6, t3[1..10−x]. f2 := L(t3[10−x]) is the third F2-cut label.
- **Q2 against R1.** L(t1[x..u−1]) = L(t1[x+11..u+10]). So u − x ≥ 4 (u − x = 1 would identify X20 with s\*; 2 and 3 are excluded by (E)/(PC)). Also X20 ∈ L(t1[x+1..u−1]), so X20's t1-arm vertex lies in Q2.
- **Q2 against R0.** L(t1[u+1..x+9]) = {w} ∪ T_int ∪ L(t1[1..x−1]).
- **f2.** It has t3[10−x] and, since R1 is pure, a t1-vertex in R1. That makes b = 2, so f2 ∈ T_int.
- **w.** Its rows R0, R7, R2 (P1), R5 (P4) and R3, R4 (t2[jw]) are covered, so its G2-W's lie in R1 and R6. b3 lies in Q1, so they lie in Q2 and Q0. Hence w = {ℓ, b3, t2[jw], t1[c], t3[a]} with c ∈ [u+1, x+9] and a ≤ 9 − x (a ≤ ℓ2 − 6 also holds by (G-A)/(G-B)).

## 3. Case μ < κ (ℓ1 + ℓ2 ≤ 29)

**X40 ∈ T_int (I1).** Its G1 are T and Λ[μ] (cut 40; P+ in R6). So its three G2 cover R1, R2 and R5. In R2 the only G2-vertices are t1[u+10..ℓ1−1] (at 20..P1−1), and t1[u+10] carries X20. So **P1 ≥ 22**.

**X20.**
- Its rows R0 (t1-arm), R1 and R2 (cut 20), R3 (arm P−; the arm lies in R3 because κ > μ) and R7 are covered. It needs R4, R5 and R6 from one G1 and one G2.
- A t2-vertex is impossible, since S_12 lies in R2 ∪ R3. So the G1 is a non-arm Λ[k] with P− in R4 and P+ in R6, and the G2 is a t3-vertex in R5.
- Its t1[u+10] lies in Q1 (offset 20 − u) and its arm vertex in Q2. So that t3-vertex lies in Q0 ∩ R5 = t3[ℓ2−4..9−x].

**(PC) at w fails.** w's neighbours carry the labels of the following vertices, none of which is a vertex of X20:
- T_int[1];
- t1[ℓ1−1] (not t1[u+10], since P1 ≥ 22);
- t2[ℓ2−1] and t2[jw±1] (X20 has no t2-vertex);
- t3[ℓ3−1] (ℓ3 − 1 ≥ 10 − x);
- t1[c±1] with u ≤ c − 1 and c + 1 ≤ x + 10 < u + 10;
- t3[a±1] with a + 1 ≤ ℓ2 − 5 < ℓ2 − 4.

So w is not joined to X20. Impossible.

## 4. Case μ > κ (ℓ1 + ℓ2 ∈ [31,34])

**f2.** If t3[10−x] lay in R5 (ℓ2 + x ≤ 14), f2's two G1 besides T would have to cover R2, R3, R4 and R6. With α > β this is impossible:
- a t2-vertex covering R3 and R4 leaves R2 and R6 to one G1;
- a Λ (R3 or R4, and R6) leaves R2 and the other of R3, R4 to one t2-vertex, which would need α < j < β.

ℓ2 + x = 15 would put t3[10−x] on the F1-cut 60. So **ℓ2 + x ≥ 16**. Then 10 − x ≤ ℓ2 − 6, and Q0 against R6 (sharing b6 and t3[1..10−x]) gives L(t1[1..x]) = L(t3[11−x..ℓ2−5]) ∪ L(Λ[1..κ]).

**The non-arm Λ-vertices.** As x < u, t1[1..x] are arm vertices, so Λ[1..κ−1] carry S-labels. Such a label has P− in R4 there (k ≤ κ − 1 < μ), so its arm P− lies in R3, i.e. its arm vertex lies in Λ[μ+1..λ−1] (type II). Conversely:
- R3 against R4 (sharing b6, Λ[μ] and t2[1..β]; α > β) gives L(Λ[1..μ−1]) = L(t2[β+1..α]) ∪ L(Λ[μ+1..λ−1]). Arm labels are distinct, so L(Λ[μ+1..λ−1]) ⊆ L(Λ[1..κ−1]): each type-II label has a non-arm vertex in Λ[1..κ−1];
- it has only one, since two would meet R6 twice.

So κ − 1 = #type II = λ − 1 − μ = 9 − α (as α + β + λ = 20). Hence α = ℓ2 − 5 and u = ℓ1 + ℓ2 − 20 − α = ℓ1 − 15.

**The bound fails.** Then x ≤ u − 4 = ℓ1 − 19 and ℓ2 ≥ 16 − x ≥ 35 − ℓ1, so ℓ1 + ℓ2 ≥ 35, contrary to (P4). Impossible.

## 5. Result

**WRITTEN:** L1 type 12 with r2 = 3, c′ = 1 and v's V's on t1 and t2 is impossible: (β1-i) by v190, (β1-ii) here. By the mirror (v160 §1, t1 ↔ t2), **L1 type 2 with r2 = 3, c′ = 1 and V's on t2 and t1 is impossible**.

With v188 (t1, Λ), v189 (t3, Λ) and v191–v194 (t3, t2), **every L1 configuration of type 12 or type 2 with r2 = 3 and c′ = 1 is impossible**.

**OPEN (m = 9, L1):**
- types 2 and 12 with r2 = 2 (the remainder after v160 and v165);
- types 2 and 12 with r2 = 3, c′ = 0, with one V on each G2-thread ((α3) in type-12 notation);
- types 1 and 11 with r1 ∈ {4,5};
- type 8 with r1 ∈ {3,4}.

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
