# Original Tuscan-2(11), entire m = 9 distance-two branch, part 83: L1 type 12, r2 = 3, c′ = 0, one V on each G2-thread — the sub-cases k = 5 and (k = 4, b3 ∈ Q1) are closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-types12-2-r2eq3-cprime1-V-on-t1-and-t2-closed-cprime1-closed-v195.md` (SHA256 `48eefbd8a08239560163a190f3618e522dab20861ddb929323f4c899ce16d259`). It uses the data of v186 §1, the imports of v188, and the counts of v188 §1. The grid lemma is v184 §2 and Lemma DP★ is v165 §1.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. The case (α3)

c′ = 0, with one V of v on t1 (t1V) and one on t3 (t3V). So c = 1.

**F2.** v's three F2-passages b6, t3V and t1V lie inside the three F2-rows. With Q0 = [−x, 10−x] ∋ b6 (1 ≤ x ≤ 9), t3V lies inside Q1 and t1V inside Q2. b3 lies in Q1 (case B1) or in Q2 (case B2); in Q0 it would make Q1 a pure t1-row without t3V. So Q0 = t1[x..1], b6, t3[1..10−x].

**F1.** v's middle F1-passages are, in order, t1V, P2, P3, t3V and P5. They cover R1..R6 with one cut p_k at 10(k+1).

## 2. k = 5 (v's cut is P5 = 60)

**The numbers.**
- ℓ2 = 5 and λ = 10 + u.
- P3 = 25 + ℓ1 ∈ R3 gives ℓ1 ≤ 14, and P2 = 15 + ℓ1 − u ∈ R2 gives u ≤ ℓ1 − 6.
- P4 = 30 + ℓ1 ≠ 40 and u ≥ 4 give ℓ1 ∈ [11,14]. Hence ℓ3 ∈ [16,19] and P4 ∈ [41,44].
- So R5 = t3[10..1], b6 (60), and R4 = t2[15−ℓ1..4], b3 (P4), t3[ℓ3−1..10].

**R5 against Q0.** They share b6 and t3[1..10−x], so L(t3[11−x..10]) = L(t1[1..x]).
- x = 1 is impossible: t3[10] (F1-cut 50) and t1[1] (F2-cut −x) would carry one label.
- x ∈ {2,3} is impossible by (E)/(PC).

So **x ≥ 4**.

**Case B1 (b3 ∈ Q1).** Then ℓ3 < 20 − x ≤ 16, contrary to ℓ3 ≥ 16.

**Case B2 (b3 ∈ Q2).**
- **The F2-row Q1.** Q1 = t3[10−x..20−x] is pure. It occupies F1 positions 40+x..50+x around the cut 50, so the grid gives x ≤ 6.
- **Q1 against R4.** They share t3[10..20−x], which gives L(t3[10−x..9]) = L(t2-part of R4) ∪ {w} ∪ L(t3[21−x..ℓ3−1]). So w lies on t3[11−x..9], in R5.
- **w's second G2-W.** By the W-rule (b3 ∈ Q2), it lies in Q0:
  - on t3[1..9−x] it would also lie in R5;
  - on t1[1..x−1] it must avoid the arm, which forces x ≥ u + 2.

  So u = 4, x = 6 and w = L(t1[5]), at F1 position 11 in R1.
- **The clash.** P1 = 6 + ℓ1 ∈ [17,20], and 20 is a cut, so b3 also lies in R1. So w appears twice in R1. **Impossible.**

## 3. k = 4 with b3 in Q1

**The numbers.** v's cut is t3V at 50 and P5 ∈ R6, so t3V = t3[ℓ2+5] and R5 = t3[ℓ2+5..ℓ2−5] is a pure t3-row. P3 ∈ R3 gives ℓ1 ≤ 14, so ℓ3 ≥ 16.

**The F2-rows.**
- b3 ∈ Q1 gives ℓ3 < 20 − x, so x ≤ 3 < u.
- Q2 = t1[x..x+10] is a pure t1-row, and t1[x] is an arm vertex. So s\* := L(t1[x]) is an F2-cut S-label.

**s\* needs P1 ≤ 19.**
- s\*'s G2 are t1[x] and a t3-vertex of the pure row R5 (b = 2).
- If P1 ≥ 21, R1 would be a pure t1-row requiring a third G2. So P1 ≤ 19, and b3 lies in R1.

**w in R1.**
- Q2 against R0 (sharing t1[x..u]) gives L(t1[u+1..x+10]) = {w, v} ∪ T_int ∪ L(t1[1..x−1]).
- t1[x+10] lies on the F2-cut 20 − x, so w lies on t1[u+1..x+9], at F1 positions 11..19 − u + x, inside R1.

So w appears twice in R1. **Impossible.**

## 4. Result

**WRITTEN:** In L1 type 12 with r2 = 3, c′ = 0 and one V on each of t1 and t3, the sub-cases k = 5 and (k = 4, b3 ∈ Q1) are impossible. The same holds for their type-2 mirror images (v160 §1).

**OPEN (m = 9, L1):**
- types 2 and 12 with r2 = 2;
- types 2 and 12 with r2 = 3, c′ = 0, one V on each G2-thread: k ∈ {1, 2, 3}, and k = 4 with b3 ∈ Q2 (type-12 notation; type 2 is the mirror);
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
