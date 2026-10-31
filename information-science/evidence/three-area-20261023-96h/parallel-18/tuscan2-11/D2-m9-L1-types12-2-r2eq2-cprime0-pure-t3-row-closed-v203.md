# Original Tuscan-2(11), entire m = 9 distance-two branch, part 90: L1 types 12 and 2 with r2 = 2, c′ = 0 and ℓ3 > 20 − x (Q1 a pure t3-row) — closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-types12-2-r2eq2-cprime1-C60-closed-cprime1-closed-v202.md` (SHA256 `028c211c4374fcca667d3ad61993b169f7cd8bf2a5369f3f794693f9dcde41d7`).

It uses:
- the data of v200 §1 (SHA256 `47e8b945f4afe3626d2b8c39f6273171b4c6fe466b58272222a2abe8334d2602`);
- (PC), v185 §2;
- the far-label method of v201/v202.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. It uses (R1)–(R2) only.

## 1. The sub-case

Type 12, r2 = 2, c′ = 0 (so 1 ≤ x ≤ 9, and v's cut is in F1), and ℓ3 > 20 − x.

**Parameters.** ℓ1 = 20 − ℓ3 < x and ℓ1 ≥ u + 1, so x ≥ u + 2 ≥ 6.

**F2-rows.**
- Q1 = [10 − x, 20 − x] = t3[10−x..20−x] is a pure t3-row.
- Q0 = t3[20−x..ℓ3−1], b3, t1[ℓ1−1..1], b6, t3[1..10−x] contains b3, b6 and all of t1.

**Labels.**
- Z0 = L(t3[20−x]) and Z1 = L(t3[10−x]) are the F2-cut labels. Each has b = 1, so neither has a t1-arm vertex, and both are T_int-labels.
- The interior t3[11−x..19−x] of Q1 carries every label except Z0 and Z1. Since b3 and b6 lie in Q0, this includes w's G2-W, v's G2-V and every S-label's second G2-vertex.

## 2. The window of Q1

**The window and its cut.**
- In F1, Q1 is the window W = [L0, L0+10] with L0 = P5 − 20 + x = 35 + ℓ2 + x. Here t3[20−x] sits at L0 and t3[10−x] at L0 + 10.
- W carries every label, and its ends are F2-cut. So W is not an F1-row: it contains exactly one F1-cut C strictly inside. Write d = C − L0, and let Ra and Rb be the rows ending and starting at C.

**The size of d.**
- d = 1 would put Z0 on the F1-cut C + 10.
- 10 − d = 1 would put Z1 on the F1-cut C − 10.
- Pieces of size 2 or 3 contradict (E).
- So **d ∈ {4,5,6}**.
- Since 46 ≤ L0 ≤ 68, C ∈ {50, 60, 70} and ℓ2 = C − 35 − x − d.

**(Rb)** L(Rb ∖ W) = L(t3[21−x−d..20−x]).
- Rb ∖ W consists of t3[9−x..1], then b6 at P5 = L0 + 20 − x (inside Rb ∖ W, because 10 < 20 − x ≤ d + 10), then Λ[1..d+x−10].
- Z0 lies on neither t3[1..9−x] (it has b = 1) nor b6.
- So Z0 = L(Λ[k]) for some k ≤ d + x − 10, which forces **d ≥ 11 − x**.

**(Ra)** L(W ∖ Ra) = L(Ra ∖ W), with W ∖ Ra = t3[10−x..19−x−d].
- Here Z1 ∈ L(Ra ∖ W). For C ≥ 60, Ra ∖ W lies above 49 ≥ P3, so it consists of t3[21−x..ℓ3−1], then b3 at P4, then S_23 t2-vertices.
- Z1 is neither a t3-vertex (b = 1) nor w, so it lies on an S_23 t2-vertex inside Ra ∖ W. Hence **b3 ∈ Ra ∖ W**, i.e. P4 ∈ Ra, and **w's G2-W is t3[dw] with 11 − x ≤ dw ≤ 19 − x − d**. That vertex lies at a position in [C+1, L0+9] ⊂ Rb.

## 3. C = 50

Here ℓ2 = 15 − x − d ≥ 5, so x + d ≤ 10. That forces x = 6 and d = 4, against d ≥ 11 − x = 5. **Impossible.**

## 4. C = 60

**Numbers.**
- ℓ2 = 25 − x − d, and x + d ≥ 11 by §2. So P5 = 55 + ℓ2 ∈ [65,69].
- P2 = 10 − u + ℓ1 + ℓ2 ∈ [21,26] (R2), P3 = 35 + ℓ1 ∈ [40,43], and P4 = 60 + ℓ1 − x − d ∈ [51,55] (R5 = Ra).
- R3 = [30,40] is reached only by Λ P− (inside (P2, P3)), and R7 only by Λ P+.

**w.**
- w is in R0, R8 (ℓ), R1, R5 (b3) and R6 (t3[dw]). Its G1-W's must cover R2, R3, R4 and R7.
- A single Λ must take both R3 and R7: otherwise the Λ with P− in R3 would need a P+ row from R6, R7, R8, all taken.
- So w = {ℓ, b3, t3[dw], Λ[kw] (P− ∈ R3, P+ ∈ R7), t2[jw] (S_12 ∈ R2, S_23 ∈ R4)}. If no such t2-vertex exists, w misses R2 and the case already fails.

**c8 = L(Λ[λ−u]).**
- Its arm P−-passage is P2 + u = 35 + ℓ1 − x − d ∈ [25,30]. The value 30 would be a second cut, so it lies in R2.
- Its G2 are t1[i8] (i8 ≤ u − 1) and t3[j8] in Q1.
- R1 needs a t2 S_12-passage, and R3 needs a Λ P−-passage. That Λ, Λ[kc], has P+ in R6 (R7 and R8 are taken), so P5 + kc ≤ 69.
- Then t3[j8] lies in R5, so j8 ∈ [21−x−d, 19−x], and the t2-vertex t2[pc] has S_12 ∈ R1 and S_23 ∈ R4.

**(PC) fails.** c8 is not joined to w:

| Possible contact | Why it fails |
|---|---|
| t2[pc] and t2[jw] | pc − jw ≥ 21 − 19 = 2 |
| Λ[kc] and Λ[kw] | kw − kc ≥ (71 − P5) − (69 − P5) = 2 |
| Λ[λ−u] and Λ[kw] | needs kw = λ − u − 1, whose P−-passage P2 + u + 1 ≤ 30 is not in R3 |
| t3[j8] and t3[dw] | j8 − dw ≥ 2 |
| t2[ℓ2−1] and t2[pc] | t2[ℓ2−1] has S_23 at P4 − 1, which is the cut 50 or lies in R5, never in R4 |
| t1[ℓ1−1] and t1[i8] | ℓ1 − 1 ≥ u > i8 |
| t3[ℓ3−1] and t3[j8] | ℓ3 − 1 ≥ 20 − x > j8 |
| T_int[1] | c8 ∈ S |

The t1-arm vertex t1[i8] has only t1- and b6-neighbours, and w has neither.

## 5. C = 70

**Numbers.**
- ℓ2 = 35 − x − d ≤ 24, so P5 = 90 − x − d ∈ [75,79]. P2 ∈ [31,36] (R3), P3 ∈ [40,43], and P4 = 70 + ℓ1 − x − d ∈ [61,69] (R6 = Ra).
- The Λ P+-run lies in R7 ∪ R8.

**w.**
- w is in R0, R8, R1, R6 and R7 (t3[dw]). Its G1-W's cover R2..R5, so both are t2-vertices.
- The one with S_12 ∈ R3 has j ≤ 5 and S_23 ∈ R4, so w = {ℓ, b3, t3[dw], t2[j1] (R3, R4), t2[j2] (R2, R5)}.

**c8.**
- By (Rb) with Rb = R7, the vertex at 80, Λ[λ−u], lies in Rb ∖ W. So c8's t3-vertex is t3[j8] with j8 ∈ [21−x−d, 19−x], and it lies in R6.
- Its arm P−-passage P2 + u = 45 + ℓ1 − x − d ∈ [35,40] lies in R3, since 40 would be a second cut.
- Its last two G1-vertices must cover R1, R2, R4 and R5, so both are t2-vertices: t2[p] with (R1, R5), since S_12 ∈ R1 gives S_23 ≥ 52, and t2[q] with (R2, R4).

**(PC) fails** with the differences of v201 §4:
- p − j2 ≥ 2, j2 − q ≥ 2, q − j1 ≥ 2 and p − j1 ≥ 12;
- t2[ℓ2−1] has S_23 ∈ R6 ∪ {60}, so it is neither t2[p] nor t2[q];
- t3[dw ± 1] stays below j8;
- t1[ℓ1−1] lies beyond the arm, and t3[ℓ3−1] beyond t3[j8].

## 6. Result

**WRITTEN:** L1 type 12 with r2 = 2, c′ = 0 and ℓ3 > 20 − x is impossible. By the mirror (v160 §1), so is the corresponding type-2 case.

With v200 §3(b), the only open part of types 12 and 2 with r2 = 2 is **c′ = 0 with b3 inside Q1** (10 − x < ℓ3 < 20 − x).

**OPEN (m = 9, L1):**
- types 2 and 12 with r2 = 2, c′ = 0 and 10 − x < ℓ3 < 20 − x;
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
