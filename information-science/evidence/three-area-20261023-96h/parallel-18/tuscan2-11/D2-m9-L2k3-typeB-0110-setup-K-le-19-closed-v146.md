# Original Tuscan-2(11), entire m = 9 distance-two branch, part 34: type B (0,1,1,0) — set-up, and the case K ≤ 19 closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-typeB-0200-delta-minus5-minus6-DP2-closed-v145.md` (SHA256 `b702f402dd2dc61a70338ffcb12a9ada07d2a86c414aef9fd1accfad7a5a651f`).

Imports:
- v143 §1: the group-1/group-2 anatomy, and the fact that rows R0, R1, R2 contain no group-2 vertex;
- DP-1 and DP-2, v114 §2;
- RC, v134 §1;
- D2Q, v125 §1, which uses (R3).

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Set-up

**Parameters.**
- n2 = n3 = 1, so a = 8 and b = 3.
- ℓ1 = p1 + u and λ = 15 − p1.
- ℓ2 = A′ + p3, with A′ = 15 − ℓ1.
- ℓ3 = 15 − p3 + p1 + u, and p4 = p3 + 5 − p1.

**F1 rows** (b5 at 10+p1, 25, 40+p3 and 50+p4):

| Row | Vertices |
|---|---|
| R0 | ℓ, T_int, b4, t1[1..u] |
| R1 | t1[u..ℓ1−1], b5, Λ[1..10−p1] |
| R2 | Λ[10−p1..14−p1], b5, t1[ℓ1−1..ℓ1−5] |
| R3 | t1[ℓ1−5..1], b4, t2[1..A′] |
| R4 | t2[A′..ℓ2−1], b5, Λ[14−p1..p4] |
| R5 | Λ[p4..1], b5, t3[ℓ3−1..u+10] |
| R6 | t3[u+10..u] (pure) |
| R7 | t3[u..1], b4, T_int, ℓ |

- V_2 lies in R3 and V_3 in R6.
- The F1 cuts are v, c1 (t1[u]), λ1\* (Λ[10−p1]), τ3 (t1[ℓ1−5]), α (t2[A′]), λ2\* (Λ[p4]), ζ (t3[u+10]) and c2 (t3[u]).
- As in v143, p1 ≠ 5 and p3 ≠ 5.

**F2 = S_23.**
- b5 sits at offset x, t2[j] at x + ℓ2 − j, b4 at K := x + ℓ2, and t3[j] at K + j.
- The v-passages b5, V_2, V_3 fall in r0, r1, r2 in this order.

**The case K ≤ 19.** Put s = 20 − K.

| Row | Vertices |
|---|---|
| r1 | t2[K−10..1], b4, t3[1..s] |
| r2 | t3[s..s+10] (pure) |
| r0 | t3[s+10..ℓ3−1], b5, t2[ℓ2−1..K−10] |

## 2. K ≤ 19 is impossible

**The shift.** R6 (backward) and r2 (forward) are pure t3-rows. Put δ3 := s − u.
- DP-1 (v114 §2) gives |δ3| ∉ {0, 1, 2, 3}.
- For |δ3| ∈ {7, 8}, exchanging R6 with r1 or r0 gives 3- or 2-blocks, which DP-1 also forbids.

**δ3 ∈ {5, 6}: DP-2 with block size m = 10 − δ3 ∈ {5, 4}.**
- R6 with r1 (shared t3[u..s]) gives L(t3[s+1..u+10]) = L(P1), where P1 is the first m vertices of r1.
- R5 with r2 (shared t3[u+10..s+10]) gives L(t3[s..u+9]) = L(P2′), where P2′ is the first m vertices of R5.

With P1′ = t3[s+1..u+10] and P2 = t3[s..u+9] = (t3[s], P1′ minus its last vertex), the four paths are pairwise disjoint as needed. DP-2 gives a contradiction.

**δ3 ∈ {−5, −6}: DP-2 with m = 10 + δ3 ∈ {5, 4}.**
- R7 with r2 (shared t3[s..u]) gives L(t3[u+1..s+10]) = L(P1), where P1 is the last m vertices of R7.
- R6 with r0 (shared t3[s+10..u+10]) gives L(t3[u..s+9]) = L(P2′), where P2′ is the m vertices of r0 beyond t3[u+10].

Here P2 = t3[u..s+9] = (t3[u], P1′ minus its last vertex). DP-2 gives a contradiction.

**δ3 = 4.** Exchanging R6 with r2 gives the saturated block Q = L(P) = L(P′), with P = t3[u..u+3] and P′ = t3[u+11..u+14].
- **Where the blocks lie.** P lies in R6 and r1, and t3[u] is c2's cut. P′ lies in R5 and r2, and t3[u+14] is the r2/r0 cut, labelled γ0′. Their interiors avoid cuts, so D2Q applies.
- **S-labels.** Any S-label other than c2 has its t3-arm in r1, as does P. So it is not in Q.
- **v and w.** V_3 lies in t3[u+5..u+9], so v ∉ Q. A W on P would share r1 with b4, so w ∉ Q.
- **Other F1-cut labels.** λ2\*'s cut covers R5, as does P′. ζ's cut covers R5 and R6, which P′ and P already cover.
- **The remaining F2-cut labels** have too few group-2 vertices.
- **λ1\*.** It is in Q only if p3 < 5, since its S_Λ2-passage must lie in R4.
- **Hence** Q = {c2, γ0′, τ3, α}, or λ1\* replaces one of τ3 and α when p3 < 5.

Applying RC:
- **γ0′** = {T, t1[k] with u < k < ℓ1−5, Λ[m] (R2, R4), P, t3[u+14]}. This forces **p1 ≥ 7**.
- **F1-cut Q-labels.** Three of them carry a t2-vertex strictly inside r0's t2-part, which has 9 − x vertices. D2Q gives x ≤ 3. Since x = 1 + p1 − p3, this gives p3 ≥ 6, so λ1\* ∉ Q.
- **τ3** = {T, t1[ℓ1−5], P, P′, t2 ∈ r0 ∩ R4}.
- **α** = {T, t1[j] with j ∈ [ℓ1−4, ℓ1−1], t2[A′], P, P′}.
- **c2** = {t3[u], t1-arm (R0, R3), t1[k′] with k′ ∈ [ℓ1−4, ℓ1−1] (R1, R2), P′, t2 ∈ r0 ∩ R4}. The arm cannot reach R2, because p1 ≥ 7.

In R1, τ3 sits at position p1 − 4, and α and c2 sit in [p1−3, p1]. Three pairwise non-adjacent Q-labels in five consecutive positions must sit at p1−4, p1−2 and p1. That gives two gaps of 2 that share a label, against D2Q.

**δ3 = −4.** The block is P = t3[u−4..u−1] (in R7 and r2, with t3[u−4] = t3[s] carrying the F2-cut label γ1) and P′ = t3[u+7..u+10] (in R6 and r0, with t3[u+10] carrying ζ).
- Since P lies on the t3-arm, Q ⊆ S.
- ζ ∈ Q and γ1 ∈ Q.
- RC excludes c1, τ3, λ1\*, c2 and the other F2-cut labels.
- So Q = {γ1, ζ, λ2\*, α}.

Each of ζ, λ2\* and α needs its third group-2 vertex to be a t2-vertex in R3 ∩ r1. So its t1-arm must reach R2: arm index j ∈ [ℓ1−4, u−1], which has 4 − p1 ≤ 3 vertices. Three pairwise non-adjacent Q-labels cannot fit there.

## 3. Result

**WRITTEN:** type B (0,1,1,0) with K ≤ 19 is impossible. (R3) is used through D2Q only at δ3 = 4.

**OPEN:**
- type B (0,1,1,0) with K ≥ 20, where b4 lies on the r1/r2 cut or in r2 and r1 is a pure t2-row;
- type A (0,2,0,0) and (0,1,1,0).

L1 types 1–4 and 7–12 remain open. The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
