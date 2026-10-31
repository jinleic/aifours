# Original Tuscan-2(11), entire m = 9 distance-two branch, part 41: L1 type 4 with r2 = 3 is impossible; types 4 and 10 survive only with r2 = 2

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-type10-r2eq3-closed-v153.md` (SHA256 `66dcb38b10aad43f86c32f09d2f47f11ba2929163fd208d7cc5bbab29e7902b0`) and uses the notation of v117 and v152.

The proof is direct: it uses only row coverage and the v152 anatomy, and is the mirror image of the v153 argument. It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Type 4: rows

**Rotation and faces.**
- The b6 rotation is (T, Λ+, t1, t3, Λ−, t2), so h1 = Λ+ and h5 = t2.
- F1 = S_T P+ S_23 P− S_12 and F2 = S_31.
- G1 = {T, Λ, t2} and G2 = {t1, t3}.
- Λ[k] is counted from the Λ+ end, so h1[i] = Λ[i].

**F1 positions.** Put Q1 = t + λ, Q2 = Q1 + ℓ2 + ℓ3, Q3 = Q2 + λ and Q4 = Q3 + ℓ1 + ℓ2.

| Position(s) | Vertex |
|---|---|
| 0 | ℓ |
| 1..t−1 | T_int |
| t | b6 |
| t + k | Λ[k] (P+) |
| Q1 | b6 |
| Q1 + j | t2[j] (S_23) |
| Q1 + ℓ2 | b3 |
| Q2 − j | t3[j] (S_23) |
| Q2 | b6 |
| Q2 + λ − k | Λ[k] (P−) |
| Q3 | b6 |
| Q3 + j | t1[j] (S_12) |
| Q3 + ℓ1 | b3 |
| Q4 − j | t2[j] (S_12) |
| Q4 | b6 |
| Q4 + 1 .. 10r1 − 1 | T_int |
| 10r1 | ℓ |

**The tail rows.**
- R_out = ℓ, T_int, b6, Λ[1..u], so Λ[u], at position t + u = 10, is the R0/R1 cut.
- R_in = t2[u..1], b6, T_int, ℓ, so t2[u] is the cut at 10r1 − 10.
- Put c1 = L(Λ[u]) and c5 = L(t2[u]). Both are F1-cut S-labels, c1 ≠ c5, and S = L(Λ[1..u]) = L(t2[1..u]) (v117).

## 2. The case r2 = 3

**Lengths.** Here r1 = 8. F2 = S_31 has 30 positions, so ℓ1 + ℓ3 = 30. F1 has 80 positions, so t + λ + ℓ2 = 25. Hence t2[u] sits at Q4 − u = 80 − t − u = 70.

**The head is G2-free.** Positions 0 to Q1 + ℓ2 = 25 carry only ℓ, T_int, b6, Λ and t2. So R0 = [0, 10] and R1 = [10, 20] contain no G2-vertex. Every t1- or t3-vertex lies after position 25.

**Anatomy (v152).** With r2 = 3, an F1-cut label has exactly two G1-vertices (K-S).

**c1.**
- Its G1-vertices are Λ[u] and one t2-arm vertex t2[j] with j ≤ u − 1. (t2[u] belongs to c5.)
- t2[j] passes at Q4 − j ∈ [71, 79], in R7, and at Q1 + j = t + λ + j.
- The cut of c1 at 10 covers R0 and R1. So t + λ + j avoids [0, 20], and it cannot equal 20, since that would be a second cut.
- Hence t + λ + j ≥ 21, so **λ ≥ 21 − t − j ≥ 21 − t − (u − 1) = 12**.

**c5.**
- Its G1-vertices are t2[u], whose cut at 70 covers R6 and R7, and one Λ-arm vertex Λ[k] with k ≤ u − 1.
- Λ[k] covers R0 through P+, and passes at Q3 − k > 25 through P−.
- The G2-vertices of c5 lie after 25.
- So R1 = [10, 20] contains a vertex of c5 only through the S_23-passage of t2[u], at Q1 + u = 10 + λ. Hence 10 < 10 + λ < 20 (20 would be a second cut), so **λ ≤ 9**.

**The two bounds contradict.** Hence **type 4 with r2 = 3 is impossible.**

## 3. The surviving row counts of types 4 and 10

- r2 ≥ 2 by the accepted fact F0 (every face has at least two rows).
- r2 ≤ 3 by (K-S) of v152.
- r2 = 3 is impossible by v153 (type 10) and §2 (type 4).
- So **types 4 and 10 survive only with r2 = 2**, that is, r1 = 9 with (n2 + n3, c′) or (n1 + n3, c′) in {(1, 0), (0, 1)}.

## 4. Result

**WRITTEN:**
- L1 type 4 with r2 = 3 is impossible.
- L1 types 4 and 10 survive only with r2 = 2.

**OPEN:** L1 types 1–3, 7–9, 11 and 12, together with types 4 and 10 at r2 = 2. The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
