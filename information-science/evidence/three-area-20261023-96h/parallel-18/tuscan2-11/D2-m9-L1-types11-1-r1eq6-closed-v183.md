# Original Tuscan-2(11), entire m = 9 distance-two branch, part 70: L1 types 11 and 1 with r1 = 6 are closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-type8-r1eq5-closed-v182.md` (SHA256 `4592b9040db2cd2577bd47bcb34044b6a07b5aa81dfc16f7110f5a086366dc6a`). Operative imports:
- v117 §§1–2: the setting, the type-11 rotation (T, t1, t2, Λ+, t3, Λ−) and the faces F1 = S_T S_12 P+ and F2 = S_23 P− S_31 (SHA256 `77faa481d25f322fffd2d68fc12f9441ae52bbc1e315a9a52685f72378842e96`);
- v152 §§1–2: the anatomy for types 1, 8 and 11, and (K-w) (SHA256 `62e80ecc4878699ad5edd15e9198a0f474eb8c9490c9e870a6dbfe611ee2a18f`);
- v161 §1: the F2 order of type 11; and v161 §4: type 1 is the row-reversal mirror of type 11, with the same r1 and u (SHA256 `dd12edbdd81da32b501e38360f10db7fc2e6219e5cc6bb2da5a1c10414cc48cb`);
- v165 §1: Lemma DP★ (SHA256 `17742d50676579486b49d783c8d589765f1d8013bc3f2ec14c79c7f2b32e657a`);
- v176 §1: Lemma A4 and exactness (E) (SHA256 `9d440953b7e4bc4eb2ff4972806f76f708331d5165efe31e48775864e9283021`);
- the arm exchange of v173 §2 (SHA256 `0f399e93d91f26c7f5b0e7e9d8614601e84668f0b053360151e6a95f59ab93d8`).

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. Every variable stays free until the deductions below.

## 1. Data of type 11 with r1 = 6

**Lengths.** r1 = 6 and r2 = 5. F1 has 2t + ℓ1 + ℓ2 + λ = 60 positions and F2 has ℓ1 + ℓ2 + 2ℓ3 + λ = 50, so ℓ3 = t − 5 = 5 − u. Lemma A4 gives u ≥ 4, so:
- u = 4, t = 6 and ℓ3 = 1;
- t3 has no interior vertex;
- ℓ1 + ℓ2 + λ = 48.

**Anatomy (v152, G1 = {T}, G2 = {t1, t2, Λ}, G3 = {t3}).** With r1 = 6 and no G3-vertex available:
- An F2-cut S-label would need b = 6, so **every S-label is F1-cut**, with five G2-vertices.
- An F1-cut T_int-label would need a G3-vertex, so **every T_int-label is F2-cut**, with its T-vertex and four G2-vertices.
- w consists of ℓ, b3 and three G2-W's.

The six F1-cuts therefore carry w, the four S-labels and v, so c = 1, c′ = 0 and n1 + n2 + nΛ = 2. **The five F2-cuts carry exactly the five T_int-labels.**

**F1.**
- ℓ lies at 0 and 60, and T_int at 1..5 and 55..59.
- b6 lies at 6, at P2 = 6 + ℓ1 + ℓ2 = 54 − λ, and at 54.
- t1[j] lies at 6 + j, and b3 at P1 = 6 + ℓ1.
- t2[j] lies at P2 − j, and Λ[k] (P+) at P2 + k.
- R0 = ℓ, T_int, b6, t1[1..4], and R5 = Λ[λ−4..λ−1], b6, T_int, ℓ, since h5[j] = Λ[λ − j].
- S = L(t1[1..4]) = L(Λ[λ−4..λ−1]). c1 = L(t1[4]) is cut at 10 and c5 = L(Λ[λ−4]) at 50.

**v in F1.** v's F1 passages are b6 (R0), its V's on t1, its V's on t2, b6 at P2, its V's on Λ, and b6 (R5), in this order. The three middle passages supply R1..R4, with v's cut at 20, 30 or 40.

**nΛ ≤ 1.** If nΛ = 2, then P2 is the first middle passage, so P2 ≤ 20. Then two consecutive F1-rows among R2, R3, R4 lie inside the P+ run P2 + 1..53 and are pure Λ-rows. Λ's other pass is in F2, in the opposite direction, so Lemma DP★ excludes this.

**F2 offsets** (v161 §1, with no t3-interior):
- b6 at 0, t2[j] at j, b3 at ℓ2, and b6 at ℓ2 + 1;
- Λ[k] at ℓ2 + 1 + λ − k (P−), b6 at ℓ2 + 1 + λ, and b3 at ℓ2 + 2 + λ;
- t1[j] at 50 − j.

## 2. The F2-rows X, Y and W

v has no F2-cut, so each of the five F2-rows contains exactly one of v's five F2 passages: three b6-corners and two V's.

**X, the row through b6(0).** X = [−z, 10 − z].
- Its lower end is t1[z]. If z ≥ ℓ1, X would put b3 on a cut or contain a second b6-corner.
- The lower end carries a T_int-label, and t1[1..4] carry S, so z ≥ 5.
- Its upper end is t2[10 − z]. If 10 − z ≥ ℓ2, X would put b3 on a cut or contain b6(ℓ2 + 1).
- X contains b6 and the whole t1-arm, so the arm exchange gives L(t1[5..z] ∪ t2[1..10−z]) = {w} ∪ T_int.

**Y, the row through b6(ℓ2 + 1).** Y = [ℓ2 + 1 − y, ℓ2 + 11 − y].
- y ≥ 2, or b3 (offset ℓ2) would sit on a cut.
- The Λ-arm occupies offsets ℓ2 + 2..ℓ2 + 5 and carries S, so y ≤ 5. Hence Y contains b3, b6 and the whole Λ-arm.
- Its lower end is t2[ℓ2 + 1 − y], at offset ≥ 1, since Y cannot reach b6(0).

**W, the row through b6(ℓ2 + 1 + λ).** W = [ℓ2 + 1 + λ − p, ℓ2 + 11 + λ − p] = Λ[p..1], b6, b3, t1[ℓ1−1..ℓ1−9+p].
- 1 ≤ p ≤ 8, since p = 9 would put b3 on a cut.
- Its lower end is Λ[p], with p < λ, since W cannot reach b6(ℓ2 + 1).

**The rows between them.** The n2 rows between X and Y each hold a V on t2. The nΛ rows between Y and W each hold a V on Λ. The n1 rows between W and X each hold a V on t1. Hence

ℓ2 = 9 + y − z + 10n2,  λ = 10 − y + p + 10nΛ,  ℓ1 = 9 + z − p + 10n1.

**(W-rule).** w's two F2 passages at b3 lie inside Y and inside W. So its three G2-W's lie one in each of the other three F2-rows. The P− run of Λ lies inside Y, the Λ-rows and W. Hence:
- if nΛ = 0, w has no Λ-vertex;
- if nΛ = 1, w has at most one Λ-vertex.

## 3. Two grid lemmas

As in v181 §3: two rows carry the same labels, so the two vertex-disjoint paths left after removing a common part carry equal label sets. Sizes 1, 2 and 3 are excluded by "one cut per label" and by (E).

**(T1) If ℓ1 ≥ 15, then z ∈ {8,9}.**
- R1 = t1[4..14] is a pure row. Its end labels, c1 and X20, are F1-cut, and it occupies F2 offsets 36..46.
- The only F2-cut inside is 50 − z, the lower end of X.
- Comparing R1 with the row below X leaves t1[4..z−1] and a path of z − 4 vertices. So z − 4 ∉ {1,2,3}.

**(T2) If λ ≥ 15, then y = 2.**
- R4 = Λ[λ−14..λ−4] is a pure row. Its end labels, X40 and c5, are F1-cut, and it occupies F2 offsets ℓ2 + 5..ℓ2 + 15.
- The only F2-cut inside is Y's upper end, ℓ2 + 11 − y.
- Comparing R4 with the row above Y leaves Λ[λ−4..λ+y−9] and a path of 6 − y vertices. So 6 − y ∉ {1,2,3}.

## 4. The five v-patterns (n1, n2, nΛ)

**(2,0,0).** Here ℓ1 = 29 + z − p ≥ 26. Then R1 = t1[4..14] and R2 = t1[14..24] are consecutive pure t1-rows with 24 ≤ ℓ1 − 1, and t1's other pass is in F2, in the opposite direction. **Lemma DP★ excludes this.**

**(0,2,0).** The two rows between X and Y are t2[10−z..20−z] and t2[20−z..30−z]. They are pure, since 30 − z ≤ ℓ2 − 1 = 28 + y − z. t2's other pass is in F1, in the opposite direction. **Lemma DP★ excludes this.**

**(1,1,0).** Here ℓ1 = 19 + z − p ≥ 16, so z ∈ {8,9} by (T1).
- **Bounds on p.** DP★ on t1 gives ℓ1 ≤ 24, and P1 = 25 + z − p ≠ 30, so p ≥ z − 4 and P1 ∈ [25,29].
- **P2.** v's middle passages are t1V, t2V and P2, so P2 = 44 + y − p ∈ [40,49].
- **The rows.** The F2-rows are X, U2 = t2[10−z..20−z], Y, W, and U1 = t1[z..z+10].
- **Where w's G2-W's lie.** By the W-rule they lie in X, U2 and U1, and none is on Λ.
  - The U1-W is an interior t1[j] (j ∈ [z+1, z+9]). F1-row R2 already holds b3, and 20 is a cut, so the U1-W lies in R1.
  - The X-W therefore cannot be on t1[5..z−1], which lies in R1. Nor can it be one of X's ends t1[z] and t2[10 − z], which carry T_int-labels. So it is an interior t2[j], j ≤ 9 − z. This forces **z = 8 and w = L(t2[1])**, so p ≥ 4.
- **P2 = 40.** Then R4 = b6, Λ[1..10] contains no possible w-vertex. Contradiction.
- **P2 ∈ [41,49].** Put q = P2 − 40 = 4 + y − p ∈ [1,5]. Then R3 = t2[q..q+10] is a pure row whose end labels are F1-cut. The F2-cuts lie at offsets ≡ 2 (mod 10).
  - q = 1: w = L(t2[1]) would sit on the F1-cut 40.
  - q = 2: R3's end t2[2] would sit on an F2-cut.
  - q ∈ [3,5]: comparing R3 with U2 = [2,12] leaves t2[13..q+10] and t2[2..q−1], q − 2 ∈ {1,2,3} vertices each, which is excluded.

  **Impossible.**

**(1,0,1).** By (T2), since λ = 20 − y + p ≥ 16, y = 2. By (T1), since ℓ1 = 19 + z − p ≥ 16, z ∈ {8,9}. So λ = 18 + p and ℓ2 = 11 − z.
- **Bounds on p.**
  - DP★ on t1 gives p ≥ z − 5.
  - DP★ on Λ gives P2 = 36 − p ≥ 30. Otherwise R3 and R4 are consecutive pure Λ-rows.
  - P1 = 25 + z − p ≥ 27, so b3 lies in R2 (P1 ≠ 30).
- **w's Λ-vertex.** R4 is a pure Λ-row, so w's R4-W is its only Λ-vertex (W-rule).
- **p ≤ 5.** If p = 6, then R3 = b6, Λ[1..10] would need a second Λ-W.
- **v's cut.** For p ≤ 5, P2 ∈ [31,35] lies inside R3. So v's cut is t1V = t1[14] at 20, and its V on Λ lies in R4.
- **w's R3-vertex.** w's R3-passage is a t2-vertex at F1 positions 31..P2 − 1. All of t2 lies in X (offsets 1..ℓ2 − 1, with the F2-cut at ℓ2 − 1). So this vertex is t2[j] with j ≤ ℓ2 − 2:
  - z = 9 (ℓ2 = 2) leaves no such vertex;
  - z = 8 forces w = L(t2[1]) and P2 ≥ 32, so p ≤ 4.
- **The last values.** p = 3 gives P1 = 30, a cut. So p = 4, P2 = 32, ℓ2 = 3, and t2[2] = t2[ℓ2 − 1] lies at F1 position P2 − 2 = 30 and at F2 offset 2 = 10 − z. Both are cuts. **Impossible.**

**(0,1,1).** By (T2), since λ = 20 − y + p ≥ 16, y = 2. So λ = 18 + p, ℓ2 = 21 − z and ℓ1 = 9 + z − p.
- **Bounds on p.** DP★ on Λ gives P2 = 36 − p ≥ 30. R4 is a pure Λ-row, so w's R4-W is its only Λ-vertex.
- **p ≤ 5.** If p = 6, R3 = b6, Λ[1..10] needs a second Λ-W, because b3 is at P1 = 9 + z ∈ R1.
- **v's cut.** For p ≤ 5, P2 ∈ [31,35] lies inside R3, so v's cut is t2V = t2[16 − p] at 20. Then P1 = 15 + z − p ≤ 19, and R2 = t2[6−p..16−p] is a pure row whose end labels, v and X30, are not F2-cut.
- **z ≤ p.** Its F2 interval [6 − p, 16 − p] contains exactly one F2-cut, 10 − z (z = p + 4 would put X30 on it). Comparing R2 with U2 = [10 − z, 20 − z] leaves two paths of 4 + p − z vertices. So 4 + p − z ∉ {1,2,3}, i.e. z ≤ p.
- **The last values.** With z ≥ 5, this forces p = z = 5. Then R3 = t2[1], b6, Λ[1..9], where t2[1] sits on the cut 30 and b3 lies in R1. So w's R3-passage would be a second Λ-W. **Impossible.**

All five patterns are impossible, so **L1 type 11 with r1 = 6 is impossible**. Type 1 is its row-reversal mirror with the same r1 and u (v161 §4), so **L1 type 1 with r1 = 6 is impossible**.

## 5. Result

**WRITTEN:** L1 types 1 and 11 with r1 = 6 are impossible for every allowed value of every variable.

**OPEN (m = 9, L1):**
- types 2 and 12;
- types 1 and 11 with r1 ∈ {4,5};
- type 8 with r1 ∈ {3,4}.

Closed L1 types: 3, 4, 5, 6, 7, 9, 10. Also closed: type 8 with r1 ∈ {5,6}, and types 1 and 11 with r1 ∈ {3,6}. The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
