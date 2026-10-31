# Original Tuscan-2(11), entire m = 9 distance-two branch, part 84: L1 type 12, r2 = 3, c′ = 0, one V on each G2-thread — the sub-cases k = 2 and k = 3 are closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-type12-r2eq3-cprime0-alpha3-k5-and-k4B1-closed-v196.md` (SHA256 `0a844326a435ac4843bf35268e8eddbe93dda46873403d7abaff8d71a6d08d8c`), with its notation (§1 there) and imports.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

**A remark used twice.** w's G1-W is a single vertex. So if two F1-rows contain neither b3 nor any G2-vertex, and one of them also contains no t2-vertex, w needs a Λ-vertex there. It then has no t2-vertex, and it cannot meet a row whose only G1-vertices are t2-vertices, unless that row holds b3.

## 1. k = 3 (v's cut is P3 = 40)

**R3 is pure Λ.** ℓ1 = 15, so ℓ3 = 15. P2 ∈ R2, so R3 = Λ[10..1], b6 (40) consists of Λ-vertices and v's cut. w must meet R3, so w's single G1-W is some Λ[k] with k ≤ 9, and w has no t2-vertex.

**Bounding ℓ2.**
- P4 = 40 + ℓ2. If P4 ≥ 51, R4 = b6, t2[1..10] would have no vertex of w. P4 = 50 would put b3 on a cut. So ℓ2 ≤ 9.
- **R3 against R6.** R6 = t3[ℓ2−5..1], b6 (P5), Λ[1..κ] with κ = 15 − ℓ2, as P4 < 60. The two rows share b6 and Λ[1..κ], which gives L(Λ[κ+1..10]) = L(t3[1..ℓ2−5]). Size 1 would identify the cuts 30 (Λ[10]) and 60 (t3[ℓ2−5]), and sizes 2 and 3 repeat a pair, by (E)/(PC). So ℓ2 ≥ 9.

**ℓ2 = 9.** Then λ = 6 + u and P2 = P3 − λ = 34 − u. P2 ∈ R2 forces u ≥ 5, and P1 = P2 − 9 = 25 − u ≠ 20 forces u ≥ 6, so P1 ≤ 19.
- R2 = [20,30] then consists of t2-vertices (20..P2−1), b6 and Λ-vertices.
- w's b3 lies at P1 ∈ R1 and at P4 = 49 ∈ R4, its G1-W lies in R3 and R6, and R2 has no G2-vertex.

So w misses R2. **Impossible.**

## 2. k = 2 (v's cut is P2 = 30)

**R3 is pure Λ.** P3 ∈ R4, so R3 = b6 (30), Λ[λ−1..λ−10]. w's single G1-W is a non-arm Λ-vertex with P− in R3, so w has no t2-vertex.

**The numbers.**
- If P4 ≥ 51, R4 = Λ, b6 (P3), t2-vertices would have no vertex of w. So P4 = 25 + ℓ1 + ℓ2 ≤ 49.
- λ = P3 − P2 = ℓ1 − 5 = 15 + u − ℓ2, so ℓ1 + ℓ2 = 20 + u ≤ 24. Hence **u = 4**, ℓ1 + ℓ2 = 24, ℓ2 ∈ [6,8] (P3 ∈ R4 gives ℓ1 ≥ 16) and ℓ3 = 6 + ℓ2.
- P1 = 30 − ℓ2 ≥ 22, so **R1 = t1[4..14] is pure t1**.

**Case B1 (b3 ∈ Q1).**
- ℓ3 < 20 − x gives x ≤ 13 − ℓ2 ≤ 7.
- Q2 = t1[x..x+10] is a pure t1-row. Its ends are F2-cut and x ≠ u = 4. It occupies F1 positions 6+x..16+x, around one F1-cut (10 or 20).
- The grid gives |x − 4| ∈ [4,6], i.e. x ≥ 8. **Impossible.**

**Case B2 (b3 ∈ Q2).**
- ℓ3 > 20 − x gives x ≥ 15 − ℓ2 ≥ 7.
- Q1 = t3[10−x..20−x] is a pure t3-row at F1 positions 35+ℓ2+x..45+ℓ2+x ⊆ [50, 62]. Its end t3[20−x] is F2-cut, so it is not on the cut 50. Hence the single F1-cut inside is 60.
- The grid gives ℓ2 + x ≥ 19, i.e. x ≥ 11. **Impossible.**

## 3. Result

**WRITTEN:** In L1 type 12 with r2 = 3, c′ = 0 and one V on each of t1 and t3, the sub-cases k = 2 and k = 3 are impossible. The same holds for their type-2 mirror images (v160 §1).

With v196, only **k = 1** and **(k = 4, b3 ∈ Q2)** remain in (α3).

**OPEN (m = 9, L1):**
- types 2 and 12 with r2 = 2;
- types 2 and 12 with r2 = 3, c′ = 0, one V on each G2-thread: k = 1, and k = 4 with b3 ∈ Q2 (type-12 notation; type 2 is the mirror);
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
