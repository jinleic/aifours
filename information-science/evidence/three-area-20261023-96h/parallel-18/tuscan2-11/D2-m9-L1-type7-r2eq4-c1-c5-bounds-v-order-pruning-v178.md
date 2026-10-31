# Original Tuscan-2(11), entire m = 9 distance-two branch, part 65: L1 type 7 with r2 = 4 — the c1/c5 bounds ℓ1, ℓ3 ≥ 7 and the resulting v-order pruning

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-type7-r2eq3-forms-ii-iii-closed-type7-r2eq3-closed-v177.md` (SHA256 `6997ee0e94802c406c350b3a6d5bf69f4872233a2bb97b1936f02b2a8f11c68c`). It uses:
- the type-7, r2 = 4 data of `D2-m9-L1-type7-r2eq4-lemmaT7prime-nLambda-cases-closed-v173.md` §1 (SHA256 `0f399e93d91f26c7f5b0e7e9d8614601e84668f0b053360151e6a95f59ab93d8`);
- the v152 anatomy;
- the consecutive-rows property.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. ℓ1 ≥ 7 and ℓ3 ≥ 7

**c1 has one t2-vertex.** In r2 = 4, an F1-cut label other than v and w has a = 1. For c1 a T-vertex would repeat c1 in R0 or R6, so its single G1-vertex lies on t2.

**ℓ1 ≥ 7.**
- c1 occupies R0 and R1 through its cut at 10, so the S_12-pass of its t2-vertex lies at a position ≥ 21.
- The S_12-run is [P1 + 1, P2 − 1], so P2 ≥ 22. Since P2 = 15 + ℓ1, this gives ℓ1 ≥ 7.

**ℓ3 ≥ 7.**
- c5 = L(t3[u]) occupies R5 and R6 through its cut at 60.
- So the S_23-pass of its single t2-vertex lies at a position ≤ 49.
- Hence P3 ≤ 48. Since P3 = 55 − ℓ3, this gives ℓ3 ≥ 7.

## 2. Pruning the cases of v173

v173 leaves the cases where v has a G2-V on t1 or t3. In F1-order, v's passages are:
- t (R0);
- the t1-V's;
- t2V12 if n2 = 1;
- P2, then the Λ-V's, then P3;
- t2V23 if n2 = 1;
- the t3-V's;
- P5 (R6).

They fill R0..R6 with one cut when c′ = 0, and with none when c′ = 1. If the cut is the k-th passage, it sits at 10k. Passages before it lie in R_{k−1}, and passages after it lie in R_k.

**c′ = 0, (nΛ, n1, n3) = (1, 1, 0).** The passages are t, t1V, P2, ΛV, P3, P5. Every placement of the cut forces either P3 ∈ R5 or P3 = 50 (ℓ3 = 5):
- t1V at 20 gives P2 ∈ R3, ΛV ∈ R4, P3 ∈ R5;
- P2 at 30 gives P3 ∈ R5;
- ΛV at 40 gives P3 ∈ R5;
- P3 at 50 gives ℓ3 = 5.

All contradict ℓ3 ≥ 7. **Impossible.** The mirror case (1, 0, 1) is impossible as well.

**c′ = 0, (0, 2, 0).** The passages are t, t1V, t1V, P2, P3, P5. Again every placement of the cut gives P3 ∈ R5 or P3 = 50. **Impossible**, and likewise (0, 0, 2).

## 3. What remains of type 7 with r2 = 4

**(P) c′ = 1 with n1 = 1.**
- v's passages fill R0 t, R1 t1V, R2 t2V12, R3 P2, R4 P3, R5 t2V23, R6 P5.
- Hence ℓ1 ∈ [16, 24] and ℓ3 ∈ [7, 14].
- The mirror case is n3 = 1.

**(Q) c′ = 0 with n1 = n3 = 1**, and the cut at t1V (20) or at P2 (30). The mirror cases have the cut at P3 (40) or at t3V (50).

The two cut positions give:
- **cut at 20:** P2 ∈ R3, P3 ∈ R4 and t3V ∈ R5;
- **cut at 30:** t1V ∈ R1, P2 = 30 (ℓ1 = 15), P3 ∈ R4 and t3V ∈ R5.

In every remaining case u ≥ 4 (Lemma A4).

## 4. Result

**WRITTEN:**
- In type 7 with r2 = 4, ℓ1 ≥ 7 and ℓ3 ≥ 7.
- The cases (1,1,0), (1,0,1), (0,2,0) and (0,0,2) of c′ = 0 are impossible.
- Type 7 with r2 = 4 survives only in cases (P) and (Q) of §3 and their mirrors.

**OPEN (m = 9, L1):**
- type 7 with r2 = 4, cases (P) and (Q);
- types 2 and 12;
- types 1 and 11 with r1 ∈ {4, 5, 6};
- type 8 with r1 ∈ {3, 4}, and with r1 = 5 and ℓ1 − u ∈ [11, 19].

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
