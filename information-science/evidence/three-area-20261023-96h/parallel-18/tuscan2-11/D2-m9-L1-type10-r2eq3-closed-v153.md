# Original Tuscan-2(11), entire m = 9 distance-two branch, part 40: L1 type 10 with r2 = 3 is impossible

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-face-group-anatomy-and-counting-constraints-v152.md` (SHA256 `62e80ecc4878699ad5edd15e9198a0f474eb8c9490c9e870a6dbfe611ee2a18f`) and uses the notation of v117 and v152.

This uses only row coverage (each label once per row, one cut per label) and the face-group anatomy of v152. It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Type 10: rows

**Rotation and faces.**
- The b6 rotation is (T, t1, Λ+, t3, t2, Λ−), so h1 = t1 and h5 = Λ−.
- F1 = S_T S_12 P− S_31 P+ and F2 = S_23.
- G1 = {T, t1, Λ} and G2 = {t2, t3}.

**F1 positions.** Put P1 = t + ℓ1, P2 = P1 + ℓ2, P3 = P2 + λ, P4 = P3 + ℓ3 and P5 = P4 + ℓ1.

| Position(s) | Vertex |
|---|---|
| 0 | ℓ |
| 1..t−1 | T_int |
| t | b6 |
| t + j | t1[j] (S_12) |
| P1 | b3 |
| P2 − j | t2[j] (S_12) |
| P2 | b6 |
| P2 + λ − k | Λ[k] (P−) |
| P3 | b6 |
| P3 + j | t3[j] (S_31) |
| P4 | b3 |
| P5 − j | t1[j] (S_31) |
| P5 | b6 |
| P5 + k | Λ[k] (P+) |
| P5 + λ | b6 |
| P5 + λ + 1 .. 10r1 − 1 | T_int |
| 10r1 | ℓ |

**The tail rows.**
- R_out = ℓ, T_int, b6, t1[1..u], so t1[u] is the R0/R1 cut.
- R_in = Λ[λ−u..λ−1], b6, T_int, ℓ, so Λ[λ−u] is the R6/R7 cut (the cut at 10r1 − 10).
- Put c1 = L(t1[u]) and c5 = L(Λ[λ−u]). Both are F1-cut S-labels, and c1 ≠ c5.

## 2. The case r2 = 3

**Lengths.** Here r1 = 8. F2 = S_23 has 30 positions, so ℓ2 + ℓ3 = 30. F1 has 80 positions, so t + ℓ1 + λ = 25. Hence P4 = t + ℓ1 + ℓ2 + ℓ3 + λ = 55, P5 = 55 + ℓ1, and Λ[λ−u] sits at 70.

**Where G2 lies.** The G2-vertices of F1 lie in (P1, P2) and (P3, P4), all before position 55. So rows R6 = [60, 70] and R7 = [70, 80] contain no G2-vertex.

**Anatomy (v152).** An F1-cut label has exactly two G1-vertices and three G2-vertices.

**c1.**
- Its G1-vertices are t1[u] and one Λ-arm vertex Λ[k], with λ − u < k ≤ λ − 1. (Λ[λ−u] belongs to c5.)
- Λ[k] covers R7 through its P+-passage (positions 71–79). Its P−-passage lies before 55.
- t1[u] covers R0 and R1 through its cut, and has one more passage, at P5 − u = 55 + ℓ1 − u.
- The G2-vertices of c1 all lie before 55.
- So R6 is covered only if 60 < 55 + ℓ1 − u < 70. (Equality with 60 would put a second cut on t1[u].) Hence **6 ≤ ℓ1 − u ≤ 14**.

**c5.**
- Its G1-vertices are Λ[λ−u], whose cut covers R6 and R7, and one t1-arm vertex t1[j] with j ≤ u − 1.
- t1[j] covers R_out through S_12. Its S_31-passage at 55 + ℓ1 − j must avoid R6 and R7, which c5 already covers, and must avoid the cut at 60.
- So 55 + ℓ1 − j ≤ 59, i.e. **ℓ1 ≤ j + 4 ≤ u + 3**.

**The two bounds contradict.** Hence **type 10 with r2 = 3 is impossible.**

## 3. Result

**WRITTEN:** L1 type 10 with r2 = 3 is impossible. With v152 (type 10 with r2 = 4 is impossible), **type 10 survives only with r2 = 2**, that is, with (n2 + n3, c′) ∈ {(1, 0), (0, 1)}.

**OPEN:** L1 types 1–4, 7–9, 11 and 12, together with type 10 at r2 = 2. The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
