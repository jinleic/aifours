# Original Tuscan-2(11), entire m = 9 distance-two branch, part 76: L1 type 12 with r2 = 3, c′ = 1 and v's V's on t3 and Λ (and its type-2 mirror) is closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-types12-2-r2eq3-cprime1-V-on-t1-and-Lambda-closed-v188.md` (SHA256 `72c327278b77b753e94d46860e122cee96a1e11803b6c0c419676a34cbbe4471`), with the same data (v186 §1) and imports (v117, v152, v160 §1, v165 §1, v176 §1, v185 §2), and the counts of v188 §1 (an F1-cut label has a = 2 and b = 3; an F2-cut label has a = 3 and b = 2; b3 never lies on a cut).

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. The case

c′ = 1, with one V of v on t3 (t3V) and one on Λ (Λ[kV]). So c = 0.

**v's F1 passages.** The middle ones, in order, are P2, ΛV₋ = P3 − kV, P3, t3V, P5 and ΛV₊ = P5 + kV, one in each of R1..R6:
- P2 ∈ R1, ΛV₋ ∈ R2, P3 ∈ R3;
- t3V ∈ R4, P5 ∈ R5, ΛV₊ ∈ R6.

So ℓ1 = P3 − 25 ∈ [6,14] and ℓ2 ∈ [1,4].

## 2. Pure rows and shift

**The rows.**
- R2 = [20,30] lies strictly between P2 and P3, so R2 = Λ[a2+10..a2] with a2 = ℓ1 − 5 ∈ [1,9].
- R6 = Λ[a6..a6+10] with a6 = 5 − ℓ2 ∈ [1,4], and Λ[a6+10] = Λ[λ−u] carries c7 at 70.

**Shift.** As in v188 §2, ρ := a2 − a6 ≥ 4, using cut pairs (20 or 30) with (60 or 70) and (E)/(PC). Also ρ ≤ u − 1.

**M.** R2 ∖ R6 = Λ[λ−u+1..λ−u+ρ] carries a set M ⊆ S ∖ {c7} with |M| = ρ, and L(R6 ∖ R2) = L(Λ[a6..a2−1]) = M.
- Λ[a2+10] lies at 20 and Λ[a6] at 60, so X20, X60 ∈ M.
- Each m ∈ M has an arm vertex (P− in R2, P+ in R7) and a low vertex Λ[k′], a6 ≤ k′ < a2. The low vertex has P− at P3 − k′ ∈ [31, 30+ρ] ⊂ R3, and P+ in R6 (at 60 for X60).

## 3. ρ = 4 and M = {c1, X20, X50, X60}

**F1-cut m** (G1 = arm and low vertex). R0, R2, R3, R6 and R7 are covered, so R1, R4 and R5 must be covered by its two other G2 and its cut. The possible cuts are:
- 10 (m = c1), 20 (X20) or 60 (X60);
- 50, through a t3-vertex covering R4 and R5.

The other positions are excluded:
- 30: Λ[a2] lies in R2 ∩ R6, so its label is not in M.
- 40: this is t3, t2 or b3. A t3 there would cover R3, which the low vertex already covers; a t2 would raise a to 3; b3 is w's.

So the F1-cut part of M lies in {c1, X20, X50, X60}.

**F2-cut m.** Its third G1 must cover two of R1, R4 and R5.
- A Λ would need P− in R1 and P+ in R5, i.e. k > a2 + 10 and k < a6. Impossible.
- So it is a t2-vertex with S_23 in R4, which needs P4 = 35 + ρ ≥ 42, i.e. ρ ≥ 7.

As in v188 §3, **ρ = 4 and M = {c1, X20, X50, X60}**, and the four labels are distinct and F1-cut. Hence:
- ℓ1 + ℓ2 = 14, ℓ3 = 16 + ℓ2, u ≥ 5;
- P2 = 24 − u, P1 = 24 − u − ℓ2, P3 = 39 − ℓ2, P4 = 39, P5 = 55 + ℓ2;
- a2 = 9 − ℓ2, a6 = 5 − ℓ2 and λ = 15 + u − ℓ2.

**The rows.**
- **R3** = Λ[a2] (30, X30), Λ[a2−1..1], b6, t2[1..ℓ2−1], b3 (39) and t3[ℓ3−1] (40, X40).
- **R4** = t3[ℓ3−1..5+ℓ2] is a **pure t3-row**. Its end t3[5+ℓ2] carries X50.
- **R5** = t3[5+ℓ2..1], b6 (P5), Λ[1..a6].
- **Λ.** Λ[a6] = X60, and Λ[a6+1..a2−1] carry {c1, X20, X50}.

**X50 and X60 in R1.** Each needs a t1-vertex inside R1 (X50: t1-arm, arm, low, cut 50; X60: t1-arm, arm, low at 60, plus t3 in R4). So P1 ≥ 13, i.e. u + ℓ2 ≤ 11.

**R3's free labels.** R3 holds X30, M, v, w and X40, together with the three labels E on Λ[1..4−ℓ2] ∪ t2[1..ℓ2−1]. So the eleven labels are v, w, M, X30, X40 and E.

**R2 ∩ R6.** R2 ∩ R6 = Λ[a2..a6+10] carries the seven non-M labels. Its ends are X30 and c7.

**Rule (ΛN).** Let Y be v or w. Then Y has a Λ-vertex with both passages inside R2 and R6, so its index lies in [a2+1, a6+9]. The two Λ-neighbours of that vertex carry two different non-M labels other than Y, and by (PC) Y is joined to neither of them through any other vertex.

## 4. b6 on an F2-cut

The F2-cuts are 0, 10 and 20. ℓ3 = 20 would put b3 on a cut, so ℓ3 ≤ 19, and [20,30] = t1[10..1], b6. Comparing it with R0 gives L(t1[u+1..10]) = {w} ∪ T_int. t1[10] is on a cut, so w lies on t1[u+1..9], at F1 positions 11..19 inside the t1-run, in R1. But b3 is at P1 ∈ [13,19] ⊂ R1. So w appears twice in R1. **Impossible.** (For u = 9, L(t1[10]) = w directly.)

## 5. t3V on an F2-cut

Let Q0 = [−x, 10−x] ∋ b6 with 1 ≤ x ≤ 9. Then t3V = t3[20−x] lies on the cut between Q1 and Q2, and Q1 = t3[10−x..20−x] is a **pure t3-row**. Also Q0 = t1[x..1], b6, t3[1..10−x] and Q2 = v, t3[21−x..ℓ3−1], b3, t1[ℓ1−1..x]. Put **f1 = L(t1[x])** and **f2 = L(t3[10−x])**, the two F2-cut labels other than v. x ≠ u, since c1 is F1-cut.

**5.1 Grid: d := ℓ2 + x − 5 ∈ [4,6].**
- **Q1 against R4.** The difference paths t3[21−x..15+ℓ2] (containing X40 at the cut 40) and t3[10−x..4+ℓ2] (containing f2) have d vertices. So d ≥ 4: d = 1 would give X40 = f2, and d ∈ {2,3} is excluded by (E)/(PC).
- **Q1 against R5.** The difference paths t3[1..9−x], b6, Λ[1..a6] and t3[6+ℓ2..20−x] have 10 − d vertices. So 10 − d ≥ 4: both paths contain v, and sizes 2 and 3 repeat a pair.

**5.2 f2 ∈ T_int and lies on t2.** f2 has t3[10−x] (in R5, since 10 − x ≤ ℓ2 + 1 < 5 + ℓ2) and a t3-vertex in the pure row R4. That is b = 2, so f2 has no t1-arm vertex and f2 ∈ T_int.
- Its G1 are T (R0, R7) and two more covering R1, R2, R3 and R6. A Λ-vertex's P+ can only be in R6, so they are one Λ (in R2 ∩ R6) and one t2-vertex (S_12 in R1, S_23 in R3).
- So ℓ2 ≥ 2, and f2 ∈ L(t2[1..ℓ2−1]).

**5.3 f1 lies on Λ[1..a6−1].** f1 has t1[x] and a t3-vertex in R4, so b = 2. Its other passage in R1 is its arm's P− (if x < u) or t1[x] itself (if x > u, at F1 position 10 − u + x ≤ 19). Either way, t2 is excluded and R1 and R7 are covered.
- Its remaining two G1 are Λ's covering R2, R3, R5 and R6. R2/R5 is impossible, and R3/R6 would be a low M-vertex. So they pair as R2/R6 and R3/R5.
- The second is Λ[k] with k ≤ a6 − 1. So **ℓ2 ≤ 3**, and f1 lies on Λ[1..4−ℓ2].

**5.4 E and two identities.**
- **E.** c7, f1 and f2 lie outside M ∪ {X30, X40, v, w}, so E = {c7, f1, f2}. Hence L(t2[1..ℓ2−1]) ⊆ {c7, f2}, and Λ[1..4−ℓ2] carry E minus the t2-labels.
- **R3 against R5.** They share b6 and Λ[1..a6], so L(t3[1..4+ℓ2]) = {c1, X20, X30, X40, w} ∪ L(t2[1..ℓ2−1]).
- **Q0 against R0.** They share b6 and t1[1..min(x,u)].

**5.5 x < u.** Here f1 is an S-label (an arm vertex at an F2-cut). Q0 against R0 gives L(t3[1..10−x]) = {w} ∪ T_int ∪ L(t1[x+1..u]). Since 10 − x ≤ 4 + ℓ2, this lies in the set of 5.4, so T_int ⊆ {X30, X40, f2}.

Q2 against R1 (sharing b3 and t1[u..ℓ1−1]) gives L(t3[21−x..ℓ3−1]) ∪ L(t1[x..u−1]) = L(t2) ∪ {X20} ∪ L(Λ[λ−u+5..λ−1]). X40 = L(t3[ℓ3−1]) lies on the left, so X40 lies on the arm and is an S-label. So T_int ⊆ {X30, f2}, and u ∈ {7,8}, since S ⊇ M ∪ {c7, f1, X40}.

Since d ≥ 4 and x ≤ u − 1, the possibilities are:
- **(ℓ2, u, x) = (2, 8, 7), (3, 8, 6) or (3, 8, 7).** T_int = {f2}, and its single vertex is adjacent to ℓ and b6. f2 also lies on t2, adjacent to b6 or to b3. So v–f2 or w–f2 is joined twice, contrary to (PC).
- **(3, 7, 6).** Here λ = 19 and the arm is Λ[12..18], with M on Λ[13..16] and {f1, X40} on Λ[17..18]. Λ[1] = f1 and t2[1..2] carry {c7, f2}.
  - **At b6.** b6 is adjacent to Λ[1] = f1, so Λ[18] = X40.
  - **The t3 labels.** t3[1..4] carry {w, X30, f2, c1}, with t3[4] = f2. The non-M labels other than v are {w, c7, X30, X40, f1, f2}.
  - **(ΛN) at v.** Four of b6's neighbours already carry such labels: T_int's last vertex (in {X30, f2}), t2[1], Λ[1] and Λ[18]. So t3[1] = c1, and t3[2..3] carry {w, X30}.
  - **t2[1] = f2.** Then T_int = (f2, X30) from ℓ, and ℓT_int[1] joins w and f2.
  - **t2[1] = c7.** Then b3t2[2] joins w and f2, so T_int = (X30, f2).
  - **Either way.** t3[3]t3[4] joins f2 with w or with X30, and both pairs are already used. Contrary to (PC).

**5.6 x > u.** Q0 holds b6 and the whole t1-arm. By the arm exchange (v173 §2), L(t1[u+1..x] ∪ t3[1..10−x]) = {w} ∪ T_int, so f1 ∈ T_int and T_int ⊆ {X30, X40, f1, f2}.
- **w's G2.** t1[u+1..x] lie in R1 before P1 (since x + ℓ2 ≤ 11), and R1 already holds b3. So w lies on t3[1..10−x], and t3[1] carries a label of {w, X30, X40, f2}.
- **(ΛN) at v.** The labels of the following b6-neighbours lie in {w, c7, X30, X40, f1, f2}: T_int's last vertex, t2[1], t3[1], Λ[1] (in {c7, f1}), and, if u ≥ 6, Λ[λ−1] (an S-label outside M ∪ {c7}, i.e. X30 or X40). These are distinct labels. So if u ≥ 6, at most one label is left for ΛV's two neighbours. Hence **u = 5**.
- **u = 5.** S = M ∪ {c7} and T_int = {f1, f2, X30, X40}. Q2 against R1, sharing b3 and t1[x..ℓ1−1], gives L(t3[21−x..ℓ3−1]) = {c1} ∪ L(t1[u+1..x−1]) ∪ L(t2) ∪ {X20} ∪ L(Λ[λ−u+5..λ−1]), where the last set is empty for u = 5. X40 = L(t3[ℓ3−1]) is on the left, so X40 lies on t1[6..x−1] and x ≥ 7. t3[10−x] = f2 and t3[1..10−x] holds w, so x ≤ 8. With d ∈ [4,6], (ℓ2, x) ∈ {(2,7), (2,8), (3,7), (3,8)}. Here t1[x] = f1, and T_int's first vertex is joined to w through ℓ.
  - **x = 8.** t3[1] = w and t3[2] = f2, so w–v and w–f2 are used.
    - **ℓ2 = 2:** t2[1] = f2 is adjacent to b3, so w–f2 is repeated.
    - **ℓ2 = 3:** t2[2] = f2 would repeat w–f2, so t2[1] = f2 and t2[2] = c7. Then w is already joined to v, f2, c7 and X40 (via b3t3[18]). By (ΛN) at w, its Λ-neighbours are X30 and f1. T_int[1] would then need a label of T_int = {f1, f2, X30, X40} not yet joined to w. Impossible.
  - **x = 7.** t1[6] = X40 and t3[1..3] carry {w, X30, f2}, with t3[3] = f2. Every option gives a contradiction:
    - If f2 lies on a t2-vertex adjacent to b3, then t3[2] ≠ w, so t3[1] = w and t3[2] = X30. w is then joined to f2, X40, v and X30. By (ΛN) at w, its Λ-neighbours are c7 and f1.
    - Otherwise (ℓ2 = 3 and t2[2] = c7), w is joined to c7 and X40 through b3, and to t3[1]'s or t3[2]'s neighbours. Either t3[1] = w (joined to v and X30, Λ-neighbours f1 and f2), or t3[1] = X30 and t3[2] = w (joined to X30 and f2, Λ-neighbours v and f1).
    - In every option, w is joined to all four labels f1, f2, X30 and X40 through vertices other than ℓ, so T_int[1] has no admissible label.

Every case is impossible.

## 6. Result

**WRITTEN:** L1 type 12 with r2 = 3, c′ = 1 and v's V's on t3 and Λ is impossible. By the mirror (v160 §1, t1 ↔ t2), **L1 type 2 with r2 = 3, c′ = 1 and v's V's on t3 and Λ is impossible**.

**OPEN (m = 9, L1):**
- types 2 and 12 with r2 = 2;
- types 2 and 12 with r2 = 3:
  - c′ = 0 with one V on each G2-thread;
  - c′ = 1 with V's on (t1, t2) or (t3, t2), in type-12 notation.
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
