# Original Tuscan-2(11), entire m = 9 distance-two branch, part 23: type C (1,1,0,0) ≅ (0,1,1,0) closed by row coverage

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-RC-lemma-typeE-0101-closed-v134.md` (SHA256 `3a08db2db1d83bd8f44720d826978215cfea8f3909151f08b8104f3239558579`). It completes v129 §3 and v130 §3, whose notation it uses. Lemma RC is v134 §1.

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. What remains of the cell

- v129 §3 excluded ρ1 = 4 with x1 ≤ 5.
- v130 §2 excluded ρ1 = 6.

So only **ρ1 = 4 with x1 ≥ 6** remains. Here x0 + p1 = 14, λ = 19 − x1 and ℓ2 = 6 + x1 − u.

**The saturated block.** The block is Q′ = L(t1[u..u+3]) = L(t1[u+11..u+14]), with P = t1[u+11..u+14] = (q′1, q′2, q′3, q′4) and c1 = L(t1[u]) ∈ {q′2, q′3}. By v130 §3, Q′ ∖ {c1} consists of T_int-labels.

**Face counts in type C, a = 4.** A T-vertex has two F1-passages. A t1- or t3-vertex has one passage in each face. A t2- or Λ-vertex has two F2-passages.

A T_int-label q ∈ Q′ ∖ {c1} has its vertices on T, on P′ and on P, so it uses its full F1-quota. Its two remaining vertices lie on t2 ∪ Λ, and its cut lies in F2. So q has 6 F2-passages covering the 7 F2-rows.

## 2. F2 rows (mod 70)

**Positions.**
- t1[j] sits at 24 + u − j, and b4 at 24 + u.
- t2[j] sits at 24 + u + j going forward.
- K2 sits at 30 + x1.
- In S_Λ1, Λ[k] sits at 49 − k, and K1 at 49.
- t2[j] sits at 55 + x1 − u − j going backward.

**Rows.**

| Row | Vertices |
|---|---|
| s1 | t1[u+14..u+4] |
| s2 | t1[u+4..1], b4, t2[1..6−u] |
| s3 | t2[6−u..5+x1−u], K2, Λ[18−x1..9] |
| s4 | Λ[9..1], K1, t2[5+x1−u] |
| s5 | t2-vertices going backward from t2[5+x1−u], then possibly b4 and t3[1..5−x1+u] |
| s6 | t3-part, K5, Λ[1..5+p1−x1] |
| s0 | Λ[5+p1−x1..18−x1], K3, t1-top |

Two facts about the rows:
- Every Λ-vertex has its S_Λ1-passage in s3 or s4.
- The S_Λ2 cut is at Λ[5+p1−x1]. Its index is at most 9, so its S_Λ1-passage lies in s4.

The t3-part of s5 lies inside the arm t3[1..u], because x1 ≥ 5. It therefore carries only S-labels.

## 3. The contradiction

Take q ∈ {q′1, q′_o}, where q′_o is the element of {q′2, q′3} ∖ {c1}. Its P′-vertex lies in t1[u+1..u+3], which is in s2. Its P-vertex lies in t1[u+11..u+13], which is in s1.

**Covering s5.** By RC, q occurs in s5. Row s5 contains only t2-vertices, b4 and S-labelled arm vertices, so q has a t2-vertex y whose backward passage lies in s5.
- If y's forward passage were in s2, or at the s2/s3 cut, q would occur twice in s2. So y's forward passage lies in s3.

**Covering s0, s4 and s6.** These rows must be covered by q's other t2/Λ-vertex z.
- If y were the s4/s5 cut vertex, z would have to cover s0 and s6 only. But z's S_Λ1-passage would repeat q in s3 or s4. So y is not that cut.
- Then z must cover s4, s6 and s0 with two passages. That forces z to be the S_Λ2 cut vertex Λ[5+p1−x1]: its S_Λ1-passage is in s4, and its S_Λ2-passage spans s6 and s0.

**Conclusion.** Both q′1 and q′_o would carry the single vertex Λ[5+p1−x1]. Contradiction.

## 4. Result

**WRITTEN:** type C cell (1,1,0,0) is impossible, and by the mirror so is (0,1,1,0). This uses (R3) in the v130 part, and here only (R1)–(R2) together with RC.

**Residual (v134 §3, updated):**

| Type | Remaining cells |
|---|---|
| A | (0,2,0,0), (0,1,1,0) |
| B | (0,2,0,0), (0,1,1,0) |
| C | (0,2,0,0); (0,1,0,1) with δ′ = −4 and x0 ∈ {3, 4}, or δ′ ∈ {4, 5, 6} |
| E | (0,2,0,0) |
| L1 | types 1–4 and 7–12 |

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
