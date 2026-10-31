# Original Tuscan-2(11), entire m = 9 distance-two branch, part 79: L1 type 12, r2 = 3, c′ = 1, V's on t3 and t2, t3V on an F2-cut — the case μ < κ is closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-type12-r2eq3-cprime1-V-on-t3-and-t2-b6-on-F2-cut-closed-v191.md` (SHA256 `46addbd7c63f8132529e89296aa97db7eef621601f8f17999ca974add00787a3`), with the notation of v191 §1 (α, β, μ = ℓ1 − 5, κ = 15 − ℓ2) and the imports of v191 (including Lemma DP★, v165 §1, and the grid lemma, v184 §2).

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. The case

**Setting.** This is (β3): c′ = 1, with V's of v on t2 and t3. Here v's F2-cut is t3V. So b6 lies inside the F2-row Q0 = [−x, 10−x] with 1 ≤ x ≤ 9, and t3V lies on the cut 20 − x between Q1 and Q2. t3V is a t3-vertex, so t3V = t3[20−x] with 20 − x < ℓ3, and Q1 = t3[10−x..20−x] is a pure t3-row.

**Grid on Q1.**
- Q1 occupies F1 positions P5 − 20 + x..P5 − 10 + x.
- Its end t3V lies in R5 (v's F1 order, v191 §1), so the single F1-cut inside Q1 is 60.
- Its ends carry v and L(t3[10−x]), which are F2-cut, hence not F1-cut.
- The grid lemma makes both pieces 25 − ℓ2 − x and ℓ2 + x − 15 at least 4. So **ℓ2 + x ∈ [19,21]**.

**x < ℓ1.**
- x = ℓ1 would put b3 (offset ℓ3 = 30 − ℓ1) on the cut −x.
- If x > ℓ1, Q2 = [20−x, 30−x] lies inside t3's range (30 − x < ℓ3). Then Q1 and Q2 are consecutive pure t3-rows, which DP★ excludes.

## 2. μ < κ is impossible

μ < κ means ℓ1 − 5 < 15 − ℓ2, i.e. ℓ1 + ℓ2 ≤ 19. With ℓ2 + x ≥ 19 this gives ℓ1 ≤ x, contrary to §1.

## 3. Result

**WRITTEN:** In L1 type 12 with r2 = 3, c′ = 1, v's V's on t3 and t2, and t3V on an F2-cut, necessarily ℓ1 + ℓ2 ≥ 21 (μ > κ, case (G-B)), ℓ2 + x ∈ [19,21] and x < ℓ1. Together with v191, (β3) survives only in this case. The same holds for its type-2 mirror image (v160 §1).

**OPEN (m = 9, L1):**
- types 2 and 12 with r2 = 2;
- types 2 and 12 with r2 = 3:
  - c′ = 0 with one V on each G2-thread;
  - c′ = 1 with V's on (t1, t2) and t1V on an F2-cut;
  - c′ = 1 with V's on (t3, t2), t3V on an F2-cut and μ > κ.

  These are in type-12 notation; type 2 is the mirror.
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
