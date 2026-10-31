# Original Tuscan-2(11), entire m = 9 distance-two branch, part 75: L1 type 12 with r2 = 3, c′ = 1 and v's V's on t1 and Λ (and its type-2 mirror) is closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-types12-2-r2eq3-cprime0-two-V-on-t3-closed-v187.md` (SHA256 `bc2c02fe48026a98d3f5236b6680d54b9932ae7b91367c559c18f22008231887`) and uses the type-12, r2 = 3 data of v186 §1 (SHA256 `bda6949e0fcd829dd3a7c31307220f3a3b515d6ab4e7f5b6e7f42103413610c4`). Imports:
- v117: the setting, exactness and "one cut per label" (SHA256 `77faa481d25f322fffd2d68fc12f9441ae52bbc1e315a9a52685f72378842e96`);
- v152: the anatomy (SHA256 `62e80ecc4878699ad5edd15e9198a0f474eb8c9490c9e870a6dbfe611ee2a18f`);
- v160 §1: the type-2/type-12 mirror (SHA256 `3597c7633dcbf620c46f532ef3f7ba38e42627f029a738c4119bb3b96e888cff`);
- v165 §1: Lemma DP★ (SHA256 `17742d50676579486b49d783c8d589765f1d8013bc3f2ec14c79c7f2b32e657a`);
- v176 §1: (E) (SHA256 `9d440953b7e4bc4eb2ff4972806f76f708331d5165efe31e48775864e9283021`);
- v185 §2: (PC) (SHA256 `fb4c5f0ec9763615d80e7ffc590f05d4aee4dc7544f7638a628aff9af3a210ac`).

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. The case

**Counts for r2 = 3.** A label other than v and w has a G1-vertices and b G2-vertices, with a + b = 5. Its F1 passages number 2a + b and its F2 passages b. F1 has 8 rows and F2 has 3, and the label has one cut. So an F1-cut label has a = 2 and b = 3, and an F2-cut label has a = 3 and b = 2. w's cut is ℓ (at 0), so b3 never lies on a cut.

**The case.** c′ = 1, with one V of v on t1 (t1V) and one on Λ (Λ[kV]). So c = 0.

**v's F1 passages.** In order they are b6 (R0), t1V, P2, ΛV₋ = P3 − kV, P3, P5, ΛV₊ = P5 + kV and b6 (R7). With no F1-cut, the six middle ones lie one in each row:
- t1V ∈ R1, P2 ∈ R2 and ΛV₋ ∈ R3;
- P3 ∈ R4, P5 ∈ R5 and ΛV₊ ∈ R6.

Hence ℓ2 = P5 − 55 ∈ [1,4], ℓ1 = P3 − 25 ∈ [16,24] and λ = 15 + u − ℓ2.

## 2. Two pure Λ-rows and the shift

**The rows.**
- R3 = [30,40] lies strictly between P2 and P3, so R3 = Λ[a3+10..a3] (Λ[k] at P3 − k), with a3 = ℓ1 − 15 ∈ [1,9].
- R6 = [60,70] lies strictly between P5 and 70 + u, so R6 = Λ[a6..a6+10] (Λ[k] at P5 + k), with a6 = 5 − ℓ2 ∈ [1,4].
- R6's top vertex Λ[a6+10] = Λ[λ−u] carries c7 at 70.

**Shift lemma: ρ := a3 − a6 ≥ 4.** R3 and R6 carry the same labels, so the two end-paths left after removing Λ[a3..a6+10] (or Λ[a6..a3+10]) carry equal label sets of |ρ| vertices.
- ρ = 0 puts Λ[a3] on the cuts 40 and 60.
- |ρ| = 1 identifies two cut vertices (30 or 40 with 60 or 70).
- |ρ| ∈ {2,3} repeats a label pair, by (E)/(PC).
- ρ < 0 would need |ρ| = a6 − a3 ≤ 3.

**M.** Since R3 ⊆ Λ[1..λ−1], we have a3 + 10 ≤ λ − 1, i.e. ρ ≤ u − 1. So R3 ∖ R6 = Λ[λ−u+1..λ−u+ρ] consists of non-c7 arm vertices. Their label set M ⊆ S ∖ {c7} has |M| = ρ and equals L(R6 ∖ R3) = L(Λ[a6..a3−1]).
- Λ[λ−u+ρ] = Λ[a3+10] lies at 30 and Λ[a6] at 60, so X30, X60 ∈ M.
- Each m ∈ M has an **arm vertex** with P− in R3 (at 30..39) and P+ in R7.
- It also has a **low vertex** Λ[k′], a6 ≤ k′ < a3, with P− at P3 − k′ ∈ [41, 40+ρ] ⊂ R4 and P+ at P5 + k′ ∈ [60, 59+ρ]. The P+ passage is the cut 60 for X60 and lies in R6 otherwise.

## 3. ρ = 4 and M = {c1, X20, X30, X60}

**F1-cut m ∈ M** (a = 2): its G1 are exactly its arm and low vertices. Its possible cuts:
- 10 (m = c1), 20 (on t1), 30 (X30 by its arm) or 60 (X60 by its low vertex).
- Not 40: Λ[a3] lies in R3 ∩ R6, so its label is not in M.
- Not 50: position 50 holds t2, b3 or t3. A t2 would raise a to 3, b3 is w's, and a t3-cut would cover R4, which the low vertex already covers.
- Not 0 or 70: these belong to w and c7.

So the F1-cut part of M lies in {c1, X20, X30, X60}.

**F2-cut m ∈ M** (a = 3): R0, R3, R4, R6 and R7 are already covered, so its third G1-vertex g and its second G2-vertex must cover R1, R2 and R5.
- g is not T, which covers R0 and R7.
- A Λ would need P− in R2 and P+ in R5, i.e. k > a3 + 10 and k < a6. Impossible.
- So g is a t2-vertex whose S_23-passage lies in R5, which needs P4 = P3 + ℓ2 = 45 + ρ ≥ 52, i.e. ρ ≥ 7.

**Conclusion.**
- If ρ ≤ 6, M has no F2-cut label, so ρ ≤ 4.
- If ρ ≥ 7, then |M| ≤ 4 + 2 = 6 < ρ.

So **ρ = 4 and M = {c1, X20, X30, X60}**. Hence ℓ1 + ℓ2 = 24 and u ≥ 5, and:
- ℓ3 = 6 + ℓ2, P1 = 34 − u − ℓ2, P2 = 34 − u, P3 = 49 − ℓ2, P4 = 49, P5 = 55 + ℓ2;
- a3 = 9 − ℓ2, a6 = 5 − ℓ2.

**Consequences.**
- X20's cut is on t1, because anything else at 20 is t2, b3 or b6. So P1 ≥ 21, and **R1 = t1[u..u+10] is a pure t1-row** with ends c1 and X20.
- X60 (t1-arm, arm, low at 60) needs t1-vertices in R1 and in R2 at 21..P1−1. So P1 ≥ 22, i.e. u + ℓ2 ≤ 12.

**The rows R4 and R5.**
- R4 = Λ[a3] (40), Λ[a3−1..1], b6 (P3), t2[1..ℓ2−1], b3 (49), t3[ℓ3−1] (50).
- R5 = t3[ℓ3−1..1], b6 (P5), Λ[1..a6].
- Λ[6−ℓ2..8−ℓ2] carry c1, X20 and X30, and Λ[5−ℓ2] carries X60.
- Write X40 = L(Λ[a3]) and X50 = L(t3[ℓ3−1]).

## 4. b6 on an F2-cut

The F2-cuts are 0, 10 and 20. ℓ3 = 10 would put b3 on a cut, so ℓ2 ≤ 3, ℓ3 ≤ 9 and ℓ1 ≥ 21. The F2-rows are [20,30] = t1[10..1], b6 and [10,20] = t1[20..10], which is pure t1.
- **[20,30] against R0:** L(t1[u+1..10]) = {w} ∪ T_int. t1[10] lies on the F2-cut 20, so w lies on t1[u+1..9]. (If u = 9, L(t1[10]) = w, which is already a contradiction.)
- **[10,20] against R1:** L(t1[u..9]) = L(t1[u+11..20]). So w lies on t1[u+11..20], at F1 positions 21..30−u. These lie in R2, before P1 ≥ 31 − u.

w's b3 also lies at P1 ∈ R2, so w appears twice in R2. **Impossible.**

## 5. t1V on an F2-cut

Let Q0 = [−x, 10−x] ∋ b6 with 1 ≤ x ≤ 9. v meets Q1 and Q2 at their common cut 20 − x, so t1V = t1[10+x].

Since t1V ∈ R1, 20 − u + x ≤ 19, i.e. x ≤ u − 1. So t1[x] (on the cut −x) is an arm vertex, and **s\* := L(t1[x]) is an F2-cut S-label** with s\* ∉ M ∪ {c7}.

**5.1 The F2-rows.** Q2 = t1[x..x+10] is pure t1. If b3 lay inside Q0, Q1 would be pure t1 too, which DP★ excludes. So b3 lies inside Q1, and Q0 = t1[x..1], b6, t3[1..10−x].

The third F2-cut is t3[10−x]; let **σ := L(t3[10−x])**. If 10 − x = ℓ3 − 1, this vertex would also lie on the F1-cut 50. So 10 − x ≤ ℓ3 − 2, and t3[10−x] lies in R5 at 51..59.

**5.2 R1 against Q2.** The difference paths t1[x+11..u+10] and t1[x..u−1] have u − x vertices and equal labels.
- u − x = 1 would identify X20 with s\*.
- u − x ∈ {2,3} repeats a pair, by (E)/(PC).

So **u − x ≥ 4**.

**5.3 s\*.**
- **G2.** Its G2 are t1[x] and a t1-vertex inside the pure row R1, so it has no t3-vertex.
- **Arm vertex.** It is neither c7's Λ[λ−u] nor in M, so it lies on Λ[λ−u+5..λ−1] (hence u ≥ 6). Its P− is at P2 + 1..29, in R2, and its P+ is in R7.
- **The other two G1.** They must cover R3, R4, R5 and R6. T is excluded (R0, R7), and so is t2 (S_12 lies in R2). So both are Λ's:
  - one has P− in R3 and P+ in R6;
  - the other, Λ[k] with 1 ≤ k ≤ a6 − 1, has P− in R4 and P+ in R5. The pairing R3/R5 would need a3 < k < a6.
- Hence a6 ≥ 2, i.e. **ℓ2 ≤ 3**, and s\* lies on Λ[1..4−ℓ2].

**5.4 σ.**
- **G2.** σ ≠ c1, X20, so it has a t1-vertex inside R1. With t3[10−x], that gives b = 2, so σ has no arm vertex and **σ ∈ T_int**.
- **G1.** Its G1 are T (R0, R7) and two more covering R2, R3, R4 and R6. A Λ must have P+ in R6, so at most one is a Λ. The other is a t2-vertex (S_12 in R2, S_23 in R4).

So σ lies on t2[1..ℓ2−1], and ℓ2 ≥ 2.

**5.5 R4's free labels.** R4 holds:
- X40, the four M-labels, v (b6), w (b3) and X50;
- the three labels E on Λ[1..4−ℓ2] ∪ t2[1..ℓ2−1].

s\*, c7 and σ are distinct and lie outside M ∪ {X40, X50, v, w} (compare cuts), so E = {s\*, c7, σ}. Hence L(t2[1..ℓ2−1]) ⊆ {c7, σ}. The eleven labels are v, w, M, c7, s\*, σ, X40 and X50.

**5.6 Two identities.**
- **R4 against R5.** They share b6, t3[ℓ3−1] and Λ[1..a6], so L(t3[1..ℓ3−2]) = {c1, X20, X30, X40, w} ∪ L(t2[1..ℓ2−1]).
- **Q0 against R0.** They share b6 and t1[1..x], so L(t3[1..10−x]) = {w} ∪ T_int ∪ L(t1[x+1..u]).

Since 10 − x ≤ ℓ3 − 2, the second set lies inside the first. Therefore:
- T_int ⊆ {X40, σ}, so X50 is an S-label and u ∈ {7,8}. Here u = 8 exactly when X40 is an S-label, and then T_int = {σ}.
- The u − x ≥ 4 S-labels on t1[x+1..u] lie in {c1, X20, X30, c7, X40}. Of these, c7 counts only if it lies on t2, and X40 only if it is an S-label.

**5.7 End.**
- **ℓ2 = 2.** t2[1] = σ. The S-labels on t1[x+1..u] lie in {c1, X20, X30, X40}, so X40 is an S-label, u = 8 and T_int = {σ}. The single T_int vertex and t2[1] both carry σ and are both adjacent to b6. Two edges join v and σ, contrary to (PC).
- **ℓ2 = 3, u = 8.** Here T_int = {σ}, and its vertex is adjacent to ℓ and b6. t2[1..2] carry {c7, σ}. If t2[1] = σ (adjacent to b6), v–σ is joined twice; if t2[2] = σ (adjacent to b3), w–σ is. Contrary to (PC).
- **ℓ2 = 3, u = 7.** Here T_int = {X40, σ}, so x = 3 and t1[4..7] carry exactly {c1, X20, X30, c7}.
  - **Arm placements.** S = M ∪ {c7, s\*, X50}, so t1[1..2] carry {X60, X50} and t1[3] = s\*. λ = 19, so the arm is Λ[12..18], with M on Λ[13..16] and {s\*, X50} on Λ[17..18]. Λ[1] = s\*.
  - **At b6.** b6 is adjacent to Λ[1] = s\* and to Λ[18], so Λ[18] = X50 and Λ[17] = s\*. b6 is also adjacent to t1[1], so t1[1] = X60 and t1[2] = X50.
  - **The repeated pair.** t1[2]t1[3] and Λ[17]Λ[18] both join X50 and s\*, contrary to (PC).

Every case is impossible.

## 6. Result

**WRITTEN:** L1 type 12 with r2 = 3, c′ = 1 and v's two V's on t1 and Λ is impossible. By the mirror (v160 §1, t1 ↔ t2), **L1 type 2 with r2 = 3, c′ = 1 and v's V's on t2 and Λ is impossible**.

**OPEN (m = 9, L1):**
- types 2 and 12 with r2 = 2;
- types 2 and 12 with r2 = 3:
  - c′ = 0 with one V on each G2-thread;
  - c′ = 1 with V's on (t1, t2) or (t3, t2) or (t3, Λ). These are type-12 notation; type 2 is the mirror.
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
