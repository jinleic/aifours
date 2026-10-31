# Original Tuscan-2(11), entire m = 9 distance-two branch, part 50: L1 type 8 has r1 ≤ 5 (r1 = 6 is impossible)

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-types11-1-r1eq3-closed-v162.md` (SHA256 `0ca6a512fa9fbfb87007dacf1aa6422ec6a2432274672f9a6bdaf2e99fb90bef`) and uses only the row-count formulas of v152 §1 (`62e80ecc4878699ad5edd15e9198a0f474eb8c9490c9e870a6dbfe611ee2a18f`).

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. The count

**v152's formulas for type 8.**
- r1 = 2 + n1 + n2 + c and r2 = 4 + n1 + n2 + 2n3 + 2nΛ + c′.
- Here c + c′ = 1, and the n's count v's 2-vertices on t1, t2, t3 and Λ.

**Consequence.** Adding the two formulas and using r1 + r2 = 11:

  6 + 2(n1 + n2 + n3 + nΛ) + 1 = 11, so n1 + n2 + n3 + nΛ = 2.

Hence r1 = 2 + (n1 + n2) + c ≤ 2 + 2 + 1 = **5**.

## 2. Check against type 11

The same computation for type 11 gives n1 + n2 + nΛ + n3 = 2. There the bound is r1 ≤ 3 + 2 + 1 = 6, so (K-w) is sharp. This sharpness check matters, because (K-w) stated 3 ≤ r1 ≤ 6 uniformly for types 1, 8 and 11. For type 8 the v-count alone removes r1 = 6.

## 3. Result

**WRITTEN:** L1 type 8 with r1 = 6 is impossible. So type 8 has r1 ∈ {3, 4, 5}.

**OPEN (m = 9, L1):**
- type 8 with r1 ∈ {3, 4, 5};
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
