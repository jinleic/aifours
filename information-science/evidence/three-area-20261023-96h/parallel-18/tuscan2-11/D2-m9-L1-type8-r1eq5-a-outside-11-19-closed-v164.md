# Original Tuscan-2(11), entire m = 9 distance-two branch, part 51: L1 type 8 with r1 = 5 is impossible unless ℓ1 − u ∈ [11, 19]

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-type8-r1eq6-excluded-by-v-count-v163.md` (SHA256 `84e20f0ae3e7b9c91b0cb33d60bc4bc85d63c9f4721fbd5acb810cdc66c542f1`). It uses:
- v117 and v152;
- Lemmas DP-1 and DP-2 of v114 §2, which allow the two passes to lie in different faces (F′ ≠ F);
- the overlap exchange;
- the mirror principle of v155 §5.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Type 8 with r1 = 5: data

**Rotation and faces.**
- The b6 rotation is (T, t1, Λ+, t3, Λ−, t2), so h1 = t1 and h5 = t2.
- F1 = S_T S_12 and F2 = S_23 P− S_31 P+.
- G1 = {T}, G2 = {t1, t2} and G3 = {t3, Λ}.

**Lengths.** r1 = 5, so F1 has 2t + ℓ1 + ℓ2 = 50 positions, and ℓ1 + ℓ2 = 30 + 2u. Put a = ℓ1 − u, so ℓ2 − u = 30 − a.

**F1 positions.**
- t1[j] lies at t + j, and b3 at 10 + a. So a ∉ {10, 20}, since w's only cut is ℓ.
- t2[j] lies at 40 + u − j, and the cuts are c1 = L(t1[u]) at 10 and c2′ = L(t2[u]) at 40.

**F2.** F2 contains the t1-run t1[ℓ1−1..1], read backward and ending at the b6-corner Z1 (t1→Λ+), so t1[j] lies at Z1 − j. Going down past index 1 it continues into b6 = Z1 and then Λ[1], Λ[2], … (P+). Going up past index ℓ1 it continues into b3 and then t3[ℓ3−1], … (S_31).

**The t1 double pass.**
- The forward pass is in F1 (cuts at j ≡ u) and the backward pass is in F2 (cuts at j ≡ Z1).
- The shift is ρ ≡ Z1 − u. The interior of t1 is t1[1..u+a−1].

## 2. The case a ≥ 21

**Pure rows.** Here b3 sits at 10 + a ≥ 31. So R1 = t1[u..u+10] and R2 = t1[u+10..u+20] are pure forward t1-rows, and u + 20 ≤ u + a − 1.

**ρ = 0** is impossible.

**DP-1.**
- **ρ ∈ {1, 2, 3}:** R1 with the backward row [u + ρ, u + ρ + 10], which is interior.
- **ρ ∈ {7, 8, 9}:** R2 with the backward row [u + ρ, u + ρ + 10], interior since a ≥ ρ + 11. This gives a C-block of size 10 − ρ.

**ρ = 4 (DP-2, m = 4).**
- R1 with the backward row [u+4, u+14] gives L(t1[u..u+3]) = L(t1[u+11..u+14]).
- R2 with the backward row [u+14, u+24] gives L(t1[u+10..u+13]) = L(P2′). Their common part t1[u+14..u+20] is interior. The backward row may run past index ℓ1 into b3 and t3, so P2′ is the path at backward indices u+21..u+24.
- Chain:
  - P1 = t1[u..u+3];
  - P1′ = t1[u+11..u+14];
  - P2 = t1[u+10..u+13];
  - P2′.

**ρ = 5 (DP-2, m = 5).** The same chain with blocks of size 5. Here P2′ is the backward path at indices u+21..u+25.

**ρ = 6 (DP-2, m = 4).**
- R2 with the backward row [u+6, u+16] gives L(t1[u+6..u+9]) = L(t1[u+17..u+20]).
- R1 with the backward row [u−4, u+6] gives L(t1[u+7..u+10]) = L(Q):
  - Q = t1[u−4..u−1] when u ≥ 5;
  - otherwise Q = (t1[u−1..1], b6 = Z1, Λ[1..4−u]), along F2 past index 0.
- Chain:
  - P1 = t1[u+17..u+20];
  - P1′ = (t1[u+9], …, t1[u+6]);
  - P2 = (t1[u+10], …, t1[u+7]);
  - P2′ = Q.

**DP-2 hypotheses.** In every chain, P2′ lies at indices or vertices disjoint from P1, P1′ and P2. Its extra vertices are b3/t3 or b6/Λ, so its edges are new.

**So type 8 with r1 = 5 and a ≥ 21 is impossible.**

## 3. The case a ≤ 9, by the mirror

Row reversal maps type 8 to itself and exchanges t1 with t2 (v155 §5). So it sends a = ℓ1 − u to ℓ2 − u = 30 − a ≥ 21. **Hence a ≤ 9 is impossible too.**

## 4. Result

**WRITTEN:** L1 type 8 with r1 = 5 survives only with ℓ1 − u ∈ [11, 19]. In that range, R1 = t1[u..u+10] and R3 = t2[u+10..u] are the only pure G2-rows of F1, so DP-2 is not available along either thread.

**OPEN (m = 9, L1):**
- type 8 with r1 ∈ {3, 4}, and with r1 = 5 and ℓ1 − u ∈ [11, 19];
- types 1 and 11 with r1 ∈ {4, 5, 6};
- types 2 and 12;
- type 7 with r2 ∈ {3, 4};
- types 3 and 9 with r2 = 3 (λ = 14, u ≥ 4) and with r2 = 4.

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
