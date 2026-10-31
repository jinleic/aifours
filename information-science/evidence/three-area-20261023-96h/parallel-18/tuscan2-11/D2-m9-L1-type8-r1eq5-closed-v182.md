# Original Tuscan-2(11), entire m = 9 distance-two branch, part 69: L1 type 8 with r1 = 5 is closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-type7-r2eq4-case-P-closed-type7-closed-v181.md` (SHA256 `8bcc54a6f8e96f340caba4f864b13b99d248e75104393abda8ea9ad2ab6c9ade`). Operative imports:
- v117 §§1–2, the setting, the type-8 rotation (T, t1, Λ+, t3, Λ−, t2) and the faces F1 = S_T S_12, F2 = S_23 P− S_31 P+ (SHA256 `77faa481d25f322fffd2d68fc12f9441ae52bbc1e315a9a52685f72378842e96`);
- v163 §1, n1 + n2 + n3 + nΛ = 2 and r1 = 2 + n1 + n2 + c (SHA256 `84e20f0ae3e7b9c91b0cb33d60bc4bc85d63c9f4721fbd5acb810cdc66c542f1`);
- v164 §1, the F1 positions and a = ℓ1 − u ∈ [11,19] (SHA256 `d7faebb6520629fbc880c0f165484f46c49b0424acda3eda0be2cd31576acdb3`);
- v176 §1, Lemma A4 and exactness (E) (SHA256 `9d440953b7e4bc4eb2ff4972806f76f708331d5165efe31e48775864e9283021`);
- the type-8 mirror of v155 §5, exchanging t1 and t2 (SHA256 `660996ba8be146a445353c9bbb865b1fc880793ccc94bc94f9c8f2d704a1a72f`).

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. Every variable stays free until the deductions below.

## 1. Data

**Lengths.** r1 = 5 and r2 = 6. F1 has 50 positions, so ℓ1 + ℓ2 = 30 + 2u. F2 has 60 positions, ℓ1 + ℓ2 + 2ℓ3 + 2λ = 60, so ℓ3 + λ = 15 − u. By v164, a = ℓ1 − u ∈ [11,19] and ℓ2 = 30 + u − a.

**v.** By v163, n1 + n2 + c = 3 and n1 + n2 ≤ 2. So c = 1 (v's cut is in F1, c′ = 0), n1 + n2 = 2 and n3 = nΛ = 0.

**F1** (v164 §1).
- t1[j] lies at 10 − u + j, b3 at 10 + a ∈ [21,29], and t2[j] at 40 + u − j.
- R1 = t1[u..u+10] and R3 = t2[u+10..u] are pure rows: a ≥ 11 and a ≤ 19 make t1[u+10] and t2[u+10] interior.
- The F1-cuts are ℓ at 0 (w), c1 = L(t1[u]) at 10, position 20, position 30, and c2′ = L(t2[u]) at 40.

**v's cut.** v's F1 passages are b6 in R0, its two V's, and b6 in R4, in this order, and one of them is a cut. Positions 10 and 40 carry c1 and c2′, so the cut is at 20 or 30.
- If it is at 20, it is t1V = t1[u+10], covering R1 and R2. The remaining V must supply R3, which is pure t2, so t2V = t2[j2] with j2 ∈ [u+1, u+9]. (A V placed before the cut would repeat v in R0 or R1.)
- The mirror exchanges the cuts at 20 and 30, and maps a to 30 − a ∈ [11,19]. So we may assume **the cut is at 20**.

**F2 offsets.** Take the b6-corner between S_31 and P+ as offset 0, and read F2 in the direction S_31 → P+ → S_23 → P− (v117 successor rule):
- Λ[k] (P+) at k, and b6 at λ;
- t2[j] at λ + j, and b3 at λ + ℓ2;
- t3[j] (S_23) at λ + ℓ2 + ℓ3 − j, and b6 at λ + ℓ2 + ℓ3 = 45 − a;
- the P− pass of Λ, with Λ[k] at 45 − a + λ − k, and b6 at 45 − a + λ;
- t3[j] (S_31) at 45 − a + λ + j, and b3 at 60 − ℓ1;
- t1[j] at 60 − j, and b6 at 60 ≡ 0.

**v's F2 passages.** These are b6(0), b6(λ), t2V at λ + j2, b6(45 − a), b6(45 − a + λ) and t1V at 50 − u, in increasing order. Since c′ = 0, the six F2-rows contain exactly one each, in this cyclic order:
- A6 = [−x, 10 − x] ∋ 0;
- B6 = [10 − x, 20 − x] ∋ λ;
- C6 = [20 − x, 30 − x];
- D6 = [30 − x, 40 − x] ∋ 45 − a;
- E6 = [40 − x, 50 − x] ∋ 45 − a + λ;
- F6 = [50 − x, 60 − x] ∋ 50 − u;

where 1 ≤ x ≤ 9. Since t1V lies inside F6, x > u.

## 2. R1 against F6 and A6: u ∈ {4,5}

R1 = t1[u..u+10] occupies F2 offsets 50 − u..60 − u. Its ends carry v (no F2-cut) and c1 (F1-cut), and the only F2-cut strictly inside is 60 − x. Put d = x − u. Two rows carry the same labels, so the vertex-disjoint paths left after removing a common part carry equal label sets:
- **R1 against F6:** the paths are t1[u..x−1] and the offsets 50 − x..49 − u, with d vertices each.
  - d = 1 would put c1 on an F2-cut.
  - d = 2 or 3 contradicts (E).
- **R1 against A6:** the paths are t1[x+1..u+10] and the offsets 61 − u..70 − x, with 10 − d vertices each.
  - 10 − d = 1 would put v on an F2-cut.
  - 10 − d = 2 or 3 contradicts (E).

So x = u + d with d ∈ [4,6]. Since x ≤ 9, u ≤ 5, and Lemma A4 gives **u ∈ {4,5}**.

## 3. R3 against F2: the position of B6's end

R3 = t2[u..u+10] occupies F2 offsets λ + u..λ + u + 10. Its ends carry c2′ and X30, both F1-cut, so exactly one F2-cut lies strictly inside. The same comparison with the two F2-rows meeting there shows that this F2-cut is t2[u + d′] with d′ ∈ [4,6].

Put g2 = 20 − x − λ ∈ [1,9], since 10 − x < λ < 20 − x. This is the t2-index at B6's upper end. The F2-cut inside R3 is 20 − x when g2 > u, and 30 − x when g2 < u (g2 = u would put c2′ on an F2-cut).
- **g2 < u.** Then d′ = g2 + 10 − u ∈ [4,6] forces u = 5 and g2 = 1. So x = 9 and λ = 10, which gives ℓ3 = 15 − u − λ = 0. Impossible.
- **g2 > u.** Then g2 = u + d′ ∈ [u+4, u+6], and g2 ≤ 9.

**λ ≥ 3.** If λ = 2, the two edges between b6 and Λ[1] join the same labels, contrary to (E).

This leaves:
- u = 5: x = 9 and g2 = 9, so λ = 2. Excluded.
- u = 4, x = 9, g2 = 9: λ = 2. Excluded.
- (α) u = 4, x = 8, g2 = 8, λ = 4, ℓ3 = 7;
- (β) u = 4, x = 8, g2 = 9, λ = 3, ℓ3 = 8;
- (γ) u = 4, x = 9, g2 = 8, λ = 3, ℓ3 = 8.

## 4. The range of a and b3 off the grid

D6 ∋ 45 − a and E6 ∋ 45 − a + λ give 30 − x < 45 − a < 40 − x and 40 − x < 45 − a + λ < 50 − x. With a ∈ [11,19]:
- (α) a ∈ [14,16];
- (β) a ∈ [14,15];
- (γ) a ∈ [15,16].

b3 carries w, whose only cut is ℓ, so neither F2 passage of b3 lies on an F2-cut. These passages are λ + ℓ2 = λ + 34 − a and 60 − ℓ1 = 56 − a, and the F2-cuts are the offsets ≡ −x (mod 10).
- (α), cuts ≡ 2: a = 14 gives 56 − a = 42, and a = 16 gives λ + 34 − a = 22. Both are excluded, so a = 15.
- (β), cuts ≡ 2: a = 14 gives 42, and a = 15 gives 37 − a = 22. **(β) is impossible.**
- (γ), cuts ≡ 1: a = 15 gives 41, and a = 16 gives 37 − a = 21. **(γ) is impossible.**

## 5. The last case (α), a = 15

Here ℓ1 = ℓ2 = 19, λ = 4 and ℓ3 = 7. The P+ pass of Λ occupies offsets 1, 2, 3 and the P− pass occupies 45 − a + λ − k = 34 − k, that is 31, 32, 33. The middle vertex Λ[2] therefore lies at offsets 2 and 32, and both are F2-cuts (≡ 2 mod 10). Its label would have two cuts. **Impossible.**

## 6. Result

**WRITTEN:** L1 type 8 with r1 = 5 is impossible. Together with v163, type 8 has r1 ∈ {3,4}.

**OPEN (m = 9, L1):**
- types 2 and 12;
- types 1 and 11 with r1 ∈ {4,5,6};
- type 8 with r1 ∈ {3,4}.

L1 type 7 is closed (v181). The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
