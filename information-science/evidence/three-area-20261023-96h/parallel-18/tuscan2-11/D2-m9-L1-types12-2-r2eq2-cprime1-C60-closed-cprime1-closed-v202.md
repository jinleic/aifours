# Original Tuscan-2(11), entire m = 9 distance-two branch, part 89: L1 types 12 and 2 with r2 = 2, c′ = 1 — the case C = 60 is closed, so c′ = 1 is closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-types12-2-r2eq2-cprime1-C70-closed-v201.md` (SHA256 `650b2377b5992226f53822c2b1f95bae2e622b00715857c9f9ba57c404cd1836`). It uses:
- the data and §4 reduction of v200 (SHA256 `47e8b945f4afe3626d2b8c39f6273171b4c6fe466b58272222a2abe8334d2602`);
- (PC), v185 §2.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. It uses (R1)–(R2) only.

## 1. The case

**Parameters.** Type 12, r2 = 2, c′ = 1 and ℓ3 ≥ 11, with window cut C = 60 (v200 §4). So:
- ℓ2 = e + 5 with e ∈ {4,5,6};
- P5 = 60 + e;
- λ − u = 25 − ℓ2 = 20 − e;
- ℓ3 ≤ e + 9 and ℓ1 = 20 − ℓ3 ≤ 9.

**Positions.**
- v's only cut is in F2, so b6 avoids F1-cuts. Hence P3 = 35 + ℓ1 ≠ 40, so ℓ1 ≥ 6 and P3 ∈ [41,44]. Likewise P2 = 15 − u + ℓ1 + e ∈ [21,26], in R2.
- P4 = P3 + ℓ2 = 40 + ℓ1 + e ∈ [51,55], in R5.
- In F1, the t2 S_12-run lies in [12,25] and the S_23-run in [42,54]. The Λ P−-run lies in (P2, P3) ⊆ [22,43], and the P+-run starts at P5 + 1 ≥ 65.
- So R3 = [30,40] is reached only by Λ P−-passages, and R7 = [70,80] only by Λ P+-passages.

## 2. w

w has ℓ (R0, R8), b3 at P1 (R1) and P4 (R5), and t3[d] with 1 ≤ d ≤ e − 1 (at P5 − d ∈ [61,65], in R6, by v200 §4). Its two G1-W's must cover R2, R3, R4 and R7.
- A Λ-W with P− in R3 is needed, and so is one with P+ in R7.
- If these were two different Λ-W's, the one with P− in R3 would have its P+ in R6, R7 or R8, all of which are taken.
- So one Λ-W, Λ[kw], has P− ∈ R3 and P+ ∈ R7. The other W covers R2 and R4, so it is a t2-vertex t2[jw] with S_12 ∈ R2 and S_23 ∈ R4.

From P3 − kw ∈ [31,39] and P5 + kw ∈ [71,79]:

  kw ∈ [P3 − 39, P3 − 31] ∩ [11 − e, 19 − e].

## 3. c8

c8 = L(Λ[20−e]) is the S-label on the F1-cut 80. Its G2 are its t1-arm vertex t1[i8], with i8 ≤ u − 1, and one vertex t3[j8] of t3[1..9] (v200 §4).

**The arm passage.** Λ[20−e] has its P−-passage at P3 − 20 + e = 15 + ℓ1 + e ∈ [25,30].
- **If ℓ1 + e = 15** (ℓ1 = 9 and e = 6), this passage is the F1-cut 30. Then c8 has two cuts, 30 and 80, which is impossible.
- **So ℓ1 + e ≤ 14**, and this passage lies in R2.

**The remaining rows.** c8 is now in R0, R2, R7 and R8. It still needs R1, R3, R4, R5 and R6, from t3[j8] and two more G1-vertices.
- R1 is reached only by a t2 S_12-passage, so c8 has t2[pc] with S_12 ∈ R1.
- R3 is reached only by Λ P−, so c8 has Λ[kc] with P− ∈ R3. Its P+ must then lie in R6, which gives 1 ≤ kc ≤ 9 − e.
- t3[j8] therefore lies in R5, so j8 ≥ e + 1, and S_23 of t2[pc] lies in R4.

## 4. (PC) fails: c8 is not joined to w

| w's neighbour | Why it is not a c8-vertex |
|---|---|
| T_int[1] | c8 ∈ S |
| t1[ℓ1−1] | ℓ1 − 1 ≥ u > i8 |
| t3[ℓ3−1] | ℓ3 − 1 ≥ 10 > j8 |
| t2[ℓ2−1] | its passages are P1 + 1 (R1, or 20) and P4 − 1 (R5, or 50). t2[pc] has S_23 in R4, so they differ. |
| t3[d±1] | d + 1 ≤ e < j8 |
| t2[jw±1] | pc − jw = (P2 − jw) − (P2 − pc) ≥ 21 − 19 = 2 |
| Λ[kw±1] and Λ[kc] | kw − kc ≥ (11 − e) − (9 − e) = 2 |
| Λ[kw±1] and Λ[20−e] | see below |

**The arm vertex Λ[20−e].** kw ≤ 19 − e, so Λ[20−e] is a neighbour of Λ[kw] only if kw = 19 − e. That needs 19 − e ≤ P3 − 31 = ℓ1 + 4, i.e. ℓ1 + e ≥ 15, which was excluded in §3.

**Other vertices.** The neighbours of t1[i8] are t1-vertices or b6, and w has neither. The neighbours of t3[j8] are t3[j8 ± 1], and these are not w's t3[d] (|j8 − d| ≥ 2) or b3 (j8 ≠ ℓ3 − 1).

So no vertex of c8 is adjacent to a vertex of w, against (PC).

## 5. Result

**WRITTEN:**
- L1 type 12 with r2 = 2, c′ = 1, ℓ3 ≥ 11 and C = 60 is impossible.
- With v201 (C = 70) and v200 §3(a) (ℓ3 ≤ 9), **L1 type 12 with r2 = 2 and c′ = 1 is impossible**.
- By the mirror (v160 §1), **so is L1 type 2 with r2 = 2 and c′ = 1**.

**OPEN (m = 9, L1):**
- Types 2 and 12 with r2 = 2 and c′ = 0: either b3 lies inside Q1 (10 − x < ℓ3 < 20 − x), or ℓ3 > 20 − x (Q1 a pure t3-row). The case ℓ3 < 10 − x is closed by v200.
- Types 1 and 11 with r1 ∈ {4,5}.
- Type 8 with r1 ∈ {3,4}.

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
