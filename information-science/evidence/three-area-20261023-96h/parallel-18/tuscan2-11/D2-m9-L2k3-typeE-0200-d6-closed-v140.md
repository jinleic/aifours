# Original Tuscan-2(11), entire m = 9 distance-two branch, part 28: type E (0,2,0,0) with d = 6 closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-typeE-0200-d4-closed-v139.md` (SHA256 `c3f83e7f3677dcd53f7eeb28a249dae1ebb360cfd822f6532458aca405943cc3`). Notation is that of v138 §1. RC is v134 §1.

This uses only (E), (C) and RC; no distance-two step is needed. It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Set-up (d = 6)

**Parameters.**
- x1 + x2 = 16, so (x1, x2) ∈ {(7,9), (8,8), (9,7)}.
- λ = 10 + x2 − x1, so λ − x2 = 10 − x1 ≤ 3.
- B = A + 6, with A = 15 − x1 − u ≥ 2 (V_a needs a t2-vertex inside s1).

**The F1 cut on Λ.** The p-ranges give 10 − p1 < x2 in all three cases:

| (x1, x2) | p1 range | 10 − p1 |
|---|---|---|
| (7,9) | [3, 7] | ≤ 7 |
| (8,8) | [4, 9] | ≤ 6 |
| (9,7) | [5, 9] | ≤ 5 |

So Λ[x2..λ−1] ⊆ M2.

**Row s6.** s6 is t2[A+6], t2[A+5], …, continued past t2[1] through b4 into t3. Let P′ be the four vertices of s6 that follow t2[A]. Then:

| A | P′ |
|---|---|
| ≥ 5 | t2[A−1..A−4] |
| 4 | (t2[3], t2[2], t2[1], b4) |
| 3 | (t2[2], t2[1], b4, t3[1]) |
| 2 | (t2[1], b4, t3[1], t3[2]) |

In every case the last vertex of P′ is the s6/s0 cut.

**Label anatomy of type E.**

| Label | Vertices | Cut |
|---|---|---|
| T_int | T, two t1/t3/Λ-vertices (one in M1, one in M2), two t2-vertices | F2 |
| S (F2 cut) | four t1/t3/Λ-vertices, one t2-vertex | F2 |
| c1 | t1[u], a t3-arm vertex, an M2-vertex, two t2-vertices | F1 |
| c2 | t3[u], a t1-arm vertex, an M1-vertex, two t2-vertices | F1 |
| λ\* | Λ[10−p1], two arm vertices, two t2-vertices | F1 |
| w (F2 cut) | b4, W_M1, W_M2, one t2-vertex W_t2 | F2 |
| w (F1 cut, λ\* = w) | b4, Λ[10−p1], two t2-vertices | F1 |

Also, from R_out/s1, L(t2[1..A]) ⊆ T_int ∪ {v}.

**Facts used.**
- **(Q) Saturated block.** Exchanging s2 with s6 gives Q := L(P) = L(P′), where P = t2[A+7..A+10] and t2[A+10] is the s2/s3 cut. By (E), P ∪ P′ carries all six Q-pairs, so no other edge joins two Q-labels. In particular, when v ∈ Q no Q-label sits at Λ[λ−1], which is adjacent to b5.
- **(Z) Exchange of s3 with s5.** Since x1 ≥ 7, these rows share t2[A+10..A+16], so

      L(t2[A+6..A+9]) = L(t2[A+17..A+9+x1]) ∪ {v} ∪ L(Λ[x2..λ−1]).

  Consequently, a label at t2[A+7..A+9] that already has all of its t2-vertices on P ∪ P′ lies in {v} ∪ L(Λ[x2..λ−1]). It can sit at Λ[x2] only if Λ[x2] is its cut.
- **(T) RC for a T_int label in Q** whose P′-vertex is a non-cut vertex of t2. Its P- and P′-vertices fill s2, s5, s1 and s6. The single cut that lets two more vertices fill s0, s3 and s4 is one of:
  - (i) t2[A+10], giving τ_P;
  - (ii) the s6/s0 cut on P′, giving τ_P′, possible only if A ≥ 5;
  - (iii) Λ[x2], giving τ_Λ.

## 2. A ≥ 5 is impossible

Here A ≥ 5 occurs only for x1 ∈ {7, 8}.

1. P′ ⊆ t2[1..A], so Q ⊆ T_int ∪ {v}. By (T), at most three T_int-labels lie in Q. Hence Q = {τ_P, τ_P′, τ_Λ, v}.
2. The labels at t2[A+7..A+9] are τ_P′, τ_Λ and v. By (Z), τ_P′ ∈ L(Λ[x2+1..λ−1]).
3. τ_P′ must not be adjacent to τ_Λ at Λ[x2] or to v at b5, so it lies on Λ[x2+2..λ−2]. That interval is empty because λ − x2 ≤ 3.

Contradiction.

## 3. A ≤ 4 is impossible

**w is in Q and is F2-cut.** b4 ∈ P′, so w ∈ Q. An F1-cut w (vertices b4, Λ[10−p1] and two t2-vertices) would need a vertex in s0. For A ≤ 3, s0 = T3, K3, T1 contains none of them. For A = 4, the only candidate is b4, which lies on the s6/s0 cut, an F2 cut. So w is F2-cut, and its only t2-vertex lies on P.

**A = 4.**
1. The P′-vertices t2[1..3] are interior to s1 and s6, so by (T) the T_int ∩ Q labels are among τ_P and τ_Λ. Hence Q = {τ_P, τ_Λ, v, w}.
2. w's cut is b4, so its W on P lies in t2[11..13]. By (Z), w ∈ L(Λ[x2+1..λ−1]).
3. As in §2, w must avoid both τ_Λ and v, which is impossible.

**A = 3.** Put σ = L(t3[1]). It is an S-label cut at t3[1], so it is F2-cut with one t2-vertex. Then Q = L(t2[1..2]) ∪ {w, σ}, with T_int ∩ Q ⊆ {τ_P, τ_Λ}. The label at t2[13] is τ_P or w.
- **If it is w:** then Q = {τ_Λ, v, w, σ}. By (Z), σ ∈ L(Λ[x2+1..λ−1]), and it must avoid τ_Λ and v. That is impossible.
- **If it is τ_P:** then w and σ lie at t2[10..12]. By (Z), both lie on Λ[x2..λ−1] and are non-adjacent, with σ ≠ Λ[x2].
  - This forces x1 = 7, w = Λ[9] and σ = Λ[11].
  - Λ[x2] then carries w, so the fourth Q-label is v. But v is adjacent to σ at b5.

**A = 2.** Put θ = L(t2[1]) ∈ T_int ∪ {v}, σ1 = L(t3[1]) and σ2 = L(t3[2]).
- σ2 is F2-cut at the s6/s0 cut.
- σ1 is F2-cut S or c1. It is not λ\*, because λ\* would have no vertex in s0.
- So Q = {θ, w, σ1, σ2}, and θ ∈ {τ_P, τ_Λ, v}.

The label at t2[12] = t2[A+10] is cut there, so it is θ = τ_P, w, or an F2-cut σ1.

By (Z), each label at t2[9..11] lies on Λ[x2..λ−1] (Λ[x2] only as its own cut), with these exceptions:
- v;
- τ_Λ;
- c1, which may instead use a second t2-vertex in t2[19..11+x1]. That interval is empty for x1 = 7.

By (Q), the Q-labels on Λ are pairwise non-adjacent. Λ[x2+1] is excluded when τ_Λ ∈ Q, and Λ[λ−1] is excluded when v ∈ Q.
- **(a) t2[12] = τ_P.** w and σ2 lie on Λ[x2..λ−1]. Only x1 = 7 with w = Λ[9] and σ2 = Λ[11] fits. Then σ1 has no free Λ-position, and the c1 escape t2[19..18] is empty.
- **(b) t2[12] = w.**
  - If θ = τ_Λ, then σ2 must lie on Λ[x2+2..λ−1]. That is Λ[11] for x1 = 7, and empty otherwise. σ1 then has no free position and no escape.
  - If θ = v, then σ2 must lie on Λ[x2+1..λ−2]. That is Λ[10] for x1 = 7, and empty otherwise. σ1 then has no position non-adjacent to Λ[10], and no escape.
- **(c) t2[12] = σ1 (F2-cut).** θ, w and σ2 lie at t2[9..11].
  - If θ = τ_Λ, then w and σ2 must both lie on Λ[x2+2..λ−1], which has at most one vertex.
  - If θ = v, then w and σ2 must lie non-adjacently on Λ[x2..λ−2], which has at most two consecutive vertices.

## 4. Result

**WRITTEN:** type E (0,2,0,0) with d = 6 is impossible. By the mirror (v138 §2(a)), so is d = −6. Only (E), (C) and RC are used.

**OPEN residual of type E (0,2,0,0):** d = 5 only, with (x1, x2) ∈ {(6,9), (7,8), (8,7), (9,6)}.

Every other residual item is as in v138. The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
