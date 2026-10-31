# Original Tuscan-2(11), entire m = 9 distance-two branch, part 18: type C (1,0,0,1) ≅ (0,0,1,1) excluded, and type C (1,1,0,0) ≅ (0,1,1,0) reduced

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-ARMCplus-typeE-1010-1001-typeC-1010-excluded-v128.md` (SHA256 `56686ab733c139ff0cd108f691d23cfdf5fcc0ee2eabb5557617dc9151ac9a35`). Notation is that of v116 §2 (type C); D2Q, ARM-C and ARM-C+ are v125, v127 and v128 (they use R3).

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Type C conventions

**Faces.**
- F1 = ℓ T b4 t1 b5 t3⁻ b4 T ℓ, with b5 at P1 = t + ℓ1 (offset p1).
- F2 = K3 → t1⁻ → b4 → t2 → K2 → S_Λ1 → K1 → t2⁻ → b4 → t3 → K5 → S_Λ2 → K3.

**Indexing Λ.** Index Λ from the Λ+ end:
- S_Λ1 runs Λ[λ−1] → Λ[1];
- S_Λ2 runs Λ[1] → Λ[λ−1].

**Offsets** (v116):
- x2 = x0 + p1 − 5 and x3 = x1 + 5 − p1;
- ρ1 = p1 + x0, ρ3 = x1 + 5 and ρΛ = x0 + x1.

**The v-order.** Consecutive v-passages lie in consecutive rows. Between K2 and K1, and between K5 and K3, the number of cuts is 1 + nΛ.

## 2. Type C, cell (1,0,0,1), and by the mirror (0,0,1,1)

**Parameters.**
- a = 4 and b = 7, with λ = 15 + x0 + p1 − x1.
- The F2 v-order is K3, V1, K2, VΛ, K1, K5, VΛ. So x1 + λ ∈ [21, 29], that is, x0 + p1 ∈ [6, 14].
- By the arm table, ρ1 = x0 + p1 ∈ {4, 5, 6} (mod 10). So x0 + p1 ∈ {6, 14}.

### ρ1 = 4 (x0 + p1 = 14)

**Lemma OL on Λ** (L = 29 − x1, φ ≡ −x1) leaves only ρΛ = 4 with x1 ≥ 4. Then:
- x0 = 14 − x1 and p1 = x1;
- ℓ2 = x1 − 4 − u ≥ 1.

**Rows.** Write positions mod 70.

| Face | Row | Vertices |
|---|---|---|
| F1 | r1 | t1[u..u+10] |
| F1 | r2 | t1[u+10..u+9+p1], b5, t3[u+9−p1..u] |
| F2 | s1 | t1[u+14..u+4] |
| F2 | s2 | t1[u+4..1], b4, t2[1..x1−5−u], K2, Λ[λ−1..λ−10+x1] |
| F2 | s0 | Λ[λ−x0..λ−1], K3, t1[u+9+p1..u+14] |

**Exchanges.**
- r1 with s1 gives Q′ = L(t1[u..u+3]) = L(t1[u+11..u+14]).
- r2 with s0 gives L(Λ[λ−x0..λ−1]) = L(t1[u+10..u+13]) ⊔ L(t3[u..u+9−p1]).

So q′1, q′2 and q′3 lie on s0's Λ-part. Row s2 contains P′ = t1[u..u+3] and Λ[λ−10+x1..λ−1], so these three labels avoid that block. They therefore sit on Λ[λ−x0..λ−11+x1], which has x0 + x1 − 10 = 4 vertices. Two of them are adjacent, which contradicts (E).

### ρ1 = 6 (x0 + p1 = 6)

**Parameters.** ARM-C+ gives u = 8. Then ℓ2 = x1 − 4 ≥ 1, so x1 ≥ 5. Lemma OL on Λ (L = 21 − x1) leaves ρΛ ∈ {4, 5, 6}, so (x0, x1) ∈ {(1, 5), (5, 9)}.

The second-pass v-order needs x3 + λ ∈ [21, 29]:
- (5, 9) has x3 = 3 and λ = 12, which fails;
- (1, 5) remains, with p1 = 5, λ = 16 and ℓ2 = 1.

**Contradiction.** Here t2 has no interior, so s2 = t1[4..1], b4, K2, Λ[15..11]. Exchanging R_out with s2 gives:

    L(Λ[11..15]) = {τ} ∪ L(t1[5..8]),

which contains three Q-labels on five consecutive Λ-vertices. This contradicts D2Q.

**The cells (1,0,0,1) and (0,0,1,1) are impossible.**

## 3. Type C, cell (1,1,0,0): reduction

**Parameters.**
- a = 4 and b = 7, with λ = 5 + x0 + p1 − x1 and ℓ2 = 20 + x1 − x0 − p1 − u.
- The F2 v-order is K3, V1, V2, K2, K1, V2, K5. Consecutive K2/K1 gives x0 + p1 ∈ [6, 14]. With the arm table, x0 + p1 ∈ {6, 14}.

**ρ1 = 4 (x0 + p1 = 14).** Here λ = 19 − x1, and K1 sits at position 49, so the S_Λ1 cut is at Λ[9].
- Exchanging r1 with s1 gives Q′ as in §2.
- Consecutive K5/K3 needs x3 = x1 + 5 − p1 ≥ 1.

*x1 ≤ 5.* Row s6 = t3[5+u−x1..ℓ3−1], K5, Λ[1..5+p1−x1]. Exchanging r2 with s6 gives:

    L(Λ[1..5+p1−x1]) = L(t1[u+10..u+9+p1]) ⊔ L(t3[u..u+4−x1]) ⊇ Q′.

By D2Q, 5 + p1 − x1 ≥ 8. So x1 ∈ {p1 − 4, p1 − 3}.
- **x1 = p1 − 4.** The S_Λ2 cut is also at Λ[9]. A vertex on two cuts is impossible.
- **x1 = p1 − 3.** Exchanging s4 = Λ[9..1], K1, t2[ℓ2−1] with s6 = t3[ℓ3−2..ℓ3−1], K5, Λ[1..8] gives {L(Λ[9]), L(t2[ℓ2−1])} = L(t3[ℓ3−2..ℓ3−1]). The vertex t3[ℓ3−2] sits on a cut (position 60), while Λ[9] (position 40) and t2[ℓ2−1] (position 50) sit on other cuts. So some label would have two cuts. Contradiction.

*x1 ≥ 6.* Two applications of D2Q bound the parameters:
- s0's Λ-part carries q′1..q′3, so x0 = 14 − p1 ≥ 6, that is, p1 ≤ 8;
- Λ[1..5+p1−x1] carries at least Q′ ∖ {c1}, because the t3- and t2-parts of s6 carry no Q′-label other than c1. So p1 ≥ x1 + 1.

These leave (x1, p1) ∈ {(6,7), (6,8), (7,8)}, with 2 ≤ u ≤ 6. **This sub-case is OPEN.**

**ρ1 = 6 (x0 + p1 = 6).** ARM-C+ gives u = 8, and consecutive K5/K3 gives x1 ≤ p1 + 4. **This sub-case is OPEN.**

## 4. Result

**WRITTEN, uses (R3) through D2Q and ARM-C+:**
- type C (1,0,0,1) and (0,0,1,1) are impossible;
- type C (1,1,0,0) ≅ (0,1,1,0) is reduced to the two OPEN sub-cases of §3.

**Residual:**

| Type | Remaining cells |
|---|---|
| A | (0,2,0,0), (0,1,1,0) |
| B | (0,2,0,0), (0,1,1,0) |
| C | (0,2,0,0), (0,1,0,1), and the two OPEN sub-cases of (1,1,0,0) |
| E | (0,2,0,0), (0,1,0,1) |
| L1 | types 1–4 and 7–12 |

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
