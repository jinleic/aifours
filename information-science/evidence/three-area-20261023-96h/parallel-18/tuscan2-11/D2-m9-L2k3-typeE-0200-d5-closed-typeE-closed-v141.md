# Original Tuscan-2(11), entire m = 9 distance-two branch, part 29: type E (0,2,0,0) with d = 5 closed, so type E is closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-typeE-0200-d6-closed-v140.md` (SHA256 `d509d049f6141e8efdc0c1cb53fec4d117840b4c34bc66390d09243e8f95125c`). Notation, row table and label anatomy are those of v138 §1 and v140 §1. R3-pair is v130 §1 and uses (R3).

This is written reasoning only. No interpreter, enumeration program, solver or search was used. Every finite case list below was written out by hand and is shown in full. It is not reviewed, formal or novelty-cleared.

## 1. Set-up (d = 5)

**Parameters.**
- x1 + x2 = 15, so (x1, x2) ∈ {(6,9), (7,8), (8,7), (9,6)}.
- λ − x2 = 10 − x1.
- B = A + 5, with A = 15 − x1 − u ≥ 2.
- The p-ranges again give 10 − p1 < x2, so Λ[x2..λ−1] ⊆ M2. The Λ cuts are Λ[10−p1] and Λ[x2].
- ℓ2 − 1 = A + 9 + x1, so the last t2-vertex of s3 is adjacent to b5.

**Blocks.**
- **(C5)** Exchanging s2 with s6 gives Q := L(P5) = L(P′5). Here P5 = t2[A+6..A+10], whose end t2[A+10] is the s2/s3 cut, and P′5 is the five vertices of s6 after t2[A]. The last vertex of P′5 is the s6/s0 cut.
- **(μ)** μ := L(t2[A+5]). The vertex t2[A+5] is the s5/s6 cut, so μ ≠ v and μ ∉ Q.
- **(Z5)** Exchanging s3 with s5 (valid since x1 ≥ 6) gives

      L(t2[A+5..A+9]) = L(t2[A+16..A+9+x1]) ∪ {v} ∪ L(Λ[x2..λ−1]).

**(K5) Pair count.** P5 ∪ P′5 carry eight distinct Q-pairs. Every other edge joining two Q-labels (an *extra*) uses one of the remaining two pairs, and no extra may repeat a pair of P′5. When there are exactly two extras, P5 must be the Hamiltonian path on the four remaining pairs, and the label at t2[A+10] must be one of its ends.

**(T) T_int-labels in Q.** As in v140 §1(T): when the P′5-vertex of a T_int-label is a non-cut t2-vertex, the label is τ_P (cut at t2[A+10]) or τ_Λ (cut at Λ[x2]). The option τ_P′ (cut on P′5) requires the last vertex of P′5 to lie on t2.

**w.** For A ≤ 4, w ∈ Q because b4 ∈ P′5. An F1-cut w would need a vertex in s0, which here is T3, K3, T1. So w is F2-cut, with a single t2-vertex, lying on P5.

## 2. A ≥ 5 is impossible

- **A ≥ 6.** P′5 = t2[A−1..A−5] ⊆ t2[1..A], so Q ⊆ T_int ∪ {v}. By (T) with τ_P′, |Q| ≤ 3 + 1 = 4 < 5.
- **A = 5.** P′5 = (t2[4], t2[3], t2[2], t2[1], b4), with b4 on the cut. L(t2[1..4]) ⊆ T_int ∪ {v} has four labels, but by (T) at most τ_P, τ_Λ and v are available.

## 3. A = 4 is impossible

**Set-up.** P′5 = (t2[3], t2[2], t2[1], b4, t3[1]), with t3[1] on the cut, so σ := L(t3[1]) is F2-cut S. By (T), L(t2[1..3]) = {τ_P, τ_Λ, v}, so Q = {τ_P, τ_Λ, v, w, σ}.

By (Z5), the labels at t2[9..13] are μ, τ_Λ, v, w and σ. Since w and σ each have only one t2-vertex, both lie on Λ[x2+1..λ−1], with Λ[x2] = τ_Λ.

- **x1 ∈ {8, 9}.** Too few Λ-slots.
- **x1 = 7.** Λ[8..10] = {τ_Λ, w, σ}, which puts w and σ adjacent. But {w, σ} is the P′5 edge b4–t3[1].
- **x1 = 6.** Λ[9..12] = {τ_Λ, μ, w, σ}. Since w and σ are not adjacent, μ = Λ[11] and {Λ[10], Λ[12]} = {w, σ}.
  - Write X = L(Λ[12]) and Y = L(Λ[10]). The extras are {v, X} and {Y, τ_Λ}.
  - Write P = τ_P (the required end), L = τ_Λ and P′5 = (a, b, c, w, σ) with {a, b, c} = {P, L, v}.
  - An extra cannot repeat cw, so c ≠ v when X = w and c ≠ L when X = σ.
  - The remaining eight orders give the following four remaining pairs:

| X | (a, b, c) | Remaining pairs | Failure |
|---|---|---|---|
| w | (L, v, P) | PL, Pσ, Lw, vσ | path w–L–P–σ–v, P interior |
| w | (v, L, P) | Pv, Pσ, Lw, vσ | triangle P, v, σ |
| w | (P, v, L) | PL, Pw, Pσ, vσ | P has degree 3 |
| w | (v, P, L) | Pw, Pσ, Lv, vσ | path w–P–σ–v–L, P interior |
| σ | (L, v, P) | PL, Pσ, Lσ, vw | triangle P, L, σ |
| σ | (v, L, P) | Pv, Pσ, Lσ, vw | path w–v–P–σ–L, P interior |
| σ | (P, L, v) | Pv, Pw, Pσ, Lσ | P has degree 3 |
| σ | (L, P, v) | Pw, Pσ, Lv, Lσ | path w–P–σ–L–v, P interior |

## 4. A = 3 is impossible

**Set-up.** P′5 = (θ1, θ2, w, σ1, σ2) = (t2[2], t2[1], b4, t3[1], t3[2]), with t3[2] on the cut, and u = 12 − x1 ≥ 3.
- σ2 is F2-cut S.
- σ1 is F2-cut S or c1. It is not λ\*, because λ\*'s vertices miss s0.
- {θ1, θ2} ⊆ {τ_P, τ_Λ, v}. Since μ ≠ v, (Z5) forces v ∈ Q, so v ∈ {θ1, θ2}.
- T13 := L(t2[13]) is cut there, so T13 ∈ {τ_P, w, F2-cut σ1}.

**The (Z5) rule.** Each label at t2[9..12] other than v and τ_Λ lies on Λ[x2..λ−1] (at Λ[x2] only as its own cut, never σ2). The one exception is c1, which may use a second t2-vertex on t2[19..12+x1]. If that vertex is t2[12+x1] = t2[ℓ2−1], it adds the extra {v, c1}.

**R3-pair facts.** The non-cut vertex t3[1] realises {w, σ2} in both orders. P′5 has edges θ1θ2, θ2w, wσ1 and σ1σ2.

**x1 = 9.** σ2 needs Λ[x2+1..λ−1] = ∅.

**x1 = 8** (Λ[7..8], escape t2[19..20]):
- **(a) T13 = τ_P.** {θ1, θ2} = {τ_P, v}, w = Λ[7], σ2 = Λ[8], and σ1 = c1 escapes. The extras are wσ2 and vσ2.
  - θ2 = τ_P leaves Pσ1, Pσ2, vw, vσ1: path σ2–P–σ1–v–w, P interior.
  - θ2 = v leaves Pw, Pσ1, Pσ2, vσ1: P has degree 3.
- **(b) T13 = w.** {θ1, θ2} = {τ_Λ, v}, τ_Λ = Λ[7], σ2 = Λ[8], and σ1 escapes. The extras are Lσ2 and vσ2, and the required end is w.
  - θ2 = L leaves Lσ1, vw, vσ1, wσ2: path L–σ1–v–w–σ2, w interior.
  - θ2 = v leaves Lw, Lσ1, vσ1, wσ2: path v–σ1–L–w–σ2, w interior.
- **(c) T13 = σ1.** τ_Λ = Λ[7], and both w and σ2 would need Λ[8].

**x1 = 7** (Λ[8..10], escape t2[19] = t2[ℓ2−1]):
- **(a) T13 = τ_P.** {θ1, θ2} = {τ_P, v}. If σ1 were on Λ, then Λ[8..10] would hold w, σ1, σ2, giving three extras. So σ1 = c1 at t2[19], with extra vσ1, and μ ∈ Λ[8..10].
  - μ = Λ[8] gives three extras.
  - μ = Λ[9] forces Λ[10] = σ2 and Λ[8] = w. Then Λ[9] realises {w, σ2} in both orders, against t3[1] (R3-pair).
  - μ = Λ[10] forces Λ[9] = σ2 and Λ[8] = w, with extras wσ2 and vσ1.
    - θ2 = τ_P leaves Pσ1, Pσ2, vw, vσ2: path σ1–P–σ2–v–w, P interior.
    - θ2 = v leaves Pw, Pσ1, Pσ2, vσ2: P has degree 3.
- **(b) T13 = w.** τ_Λ = Λ[8]. If σ1 were on Λ there would be three extras. So σ1 = c1 at t2[19], with extra vσ1.
  - μ = Λ[9], σ2 = Λ[10]; extras vσ2, vσ1.
    - θ2 = L leaves Lσ1, Lσ2, vw, wσ2: path v–w–σ2–L–σ1, w interior.
    - θ2 = v leaves v isolated.
  - μ = Λ[10], σ2 = Λ[9]; extras Lσ2, vσ1.
    - θ2 = L leaves Lσ1, vw, vσ2, wσ2: L and σ1 isolated together.
    - θ2 = v leaves Lw, Lσ1, vσ2, wσ2: path σ1–L–w–σ2–v, w interior.
- **(c) T13 = σ1.** w and σ2 fill Λ[9..10] next to τ_Λ = Λ[8] and v, giving three extras.

**x1 = 6** (Λ[9..12], no escape). Λ[9..12] carries μ and the three Q-labels at t2[9..12] other than v. The pairs wσ1 and σ1σ2 cannot be Λ-neighbours. μ = Λ[9] gives three extras.
- **(a) T13 = τ_P.** {θ1, θ2} = {τ_P, v}, and Λ holds w, σ1, σ2 and μ.
  - μ = Λ[12] puts w, σ1, σ2 consecutively, so σ1 has a P′5-neighbour beside it.
  - μ = Λ[11] forces (Λ[12], Λ[10], Λ[9]) = (σ1, σ2, w), with extras vσ1, wσ2.
    - θ2 = τ_P leaves Pσ1, Pσ2, vw, vσ2: P interior.
    - θ2 = v leaves Pw, Pσ1, Pσ2, vσ2: P has degree 3.
  - μ = Λ[10] forces {Λ[12], Λ[11]} = {w, σ2} and Λ[9] = σ1, with extras vX and wσ2 where X = L(Λ[12]).
    - X = w: with θ2 = v the extra vw repeats P′5; with θ2 = τ_P, w is isolated.
    - X = σ2: θ2 = τ_P leaves Pσ1, Pσ2, vw, vσ1, path σ2–P–σ1–v–w with P interior; θ2 = v leaves P with degree 3.
- **(b) T13 = w.** τ_Λ = Λ[9]. σ1 and σ2 are not adjacent, so μ = Λ[11] and {Λ[10], Λ[12]} = {σ1, σ2}.

  | Λ[12] | θ2 | Remaining pairs | Failure |
  |---|---|---|---|
  | σ1 | L | Lσ1, vw, vσ2, wσ2 | L and σ1 isolated together |
  | σ1 | v | Lw, Lσ1, vσ2, wσ2 | path σ1–L–w–σ2–v, w interior |
  | σ2 | L | Lσ2, vw, vσ1, wσ2 | path L–σ2–w–v–σ1, w interior |
  | σ2 | v | Lw, Lσ2, vσ1, wσ2 | v and σ1 isolated together |
- **(c) T13 = σ1.** τ_Λ = Λ[9], and Λ[10..12] = {μ, w, σ2}. The required end is σ1.
  - μ = Λ[11] makes Λ[11] realise {w, σ2}, against t3[1] (R3-pair).
  - μ = Λ[12]: extras wσ2 and L·L(Λ[10]).
    - Λ[10] = w: θ2 = L repeats the P′5 edge Lw; θ2 = v leaves w isolated.
    - Λ[10] = σ2: θ2 = L leaves v with degree 3; θ2 = v leaves Lw, Lσ1, vσ1, vσ2, path σ2–v–σ1–L–w with σ1 interior.
  - μ = Λ[10]: extras wσ2 and v·L(Λ[12]).
    - Λ[12] = w: θ2 = v repeats vw; θ2 = L leaves w isolated.
    - Λ[12] = σ2: θ2 = L leaves Lσ1, Lσ2, vw, vσ1, path σ2–L–σ1–v–w with σ1 interior; θ2 = v leaves L with degree 3.

## 5. A = 2 is impossible

**Set-up.** P′5 = (θ, w, σ1, σ2, σ3) = (t2[1], b4, t3[1], t3[2], t3[3]), with t3[3] on the cut, and u = 13 − x1 ≥ 4.
- **θ = v.** v ∈ Q by (Z5) and (μ), and θ is the only possible place.
- σ3 is F2-cut S.
- σ1 and σ2 are each F2-cut S or c1. Neither is λ\*, which would miss s0.
- So Q = {v, w, σ1, σ2, σ3}, with P′5 edges vw, wσ1, σ1σ2 and σ2σ3. The non-P′5 pairs are vσ1, vσ2, vσ3, wσ2, wσ3 and σ1σ3.
- T12 := L(t2[12]) ∈ {w, F2-cut σ1, F2-cut σ2}.
- By (Z5), μ and the three labels Q ∖ {v, T12} occupy Λ[x2..λ−1] ∪ t2[18..11+x1]. Only c1 may use the t2 slots, and σ3 is never at Λ[x2].
- The non-cut vertex t3[2] realises {σ1, σ3} in both orders.

**x1 = 9.** One Λ-slot and at most one c1 cannot hold three labels.

**x1 = 8.** The Λ-slots are Λ[7], Λ[8], and c1 must sit at t2[18]: t2[19] = t2[ℓ2−1] would add a third extra. So σ3 = Λ[8] and X7 = L(Λ[7]) is cut there.
- X7 = σ2 repeats σ2σ3.
- X7 = w leaves vσ1, vσ2, wσ2, σ1σ3, path σ3–σ1–v–σ2–w. Its end w is cut at Λ[7], not at t2[12].
- X7 = σ1 leaves vσ2, vσ1, wσ2, wσ3, path σ1–v–σ2–w–σ3. Its end σ1 is cut at Λ[7].

**x1 = 7.** The slots are t2[18] (adjacent to b5) and Λ[8..10]. μ ∈ {t2[18], Λ[8]} gives three extras.
- **μ = Λ[10].** t2[18] = c1, σ3 = Λ[9], and X8 = L(Λ[8]) ≠ σ2. The extras are vc1 and σ3X8.

  | (c1, X8) | T12 | Remaining pairs | Failure |
  |---|---|---|---|
  | (σ1, w) | σ2 | vσ2, vσ3, wσ2, σ1σ3 | path w–σ2–v–σ3–σ1, σ2 interior |
  | (σ2, w) | σ1 | vσ1, vσ3, wσ2, σ1σ3 | triangle v, σ1, σ3 |
  | (σ2, σ1) | w | vσ1, vσ3, wσ2, wσ3 | path σ1–v–σ3–w–σ2, w interior |
- **μ = Λ[9].** t2[18] = c1, σ3 = Λ[10], and the extras are vσ3 and vc1. Λ[9] realises {σ3, X8}, so X8 ≠ σ1 by R3-pair against t3[2].

  | (c1, X8) | T12 | Remaining pairs | Failure |
  |---|---|---|---|
  | (σ1, w) | σ2 | vσ2, wσ2, wσ3, σ1σ3 | path v–σ2–w–σ3–σ1, σ2 interior |
  | (σ1, σ2) | w | same | w interior |
  | (σ2, w) | σ1 | vσ1, wσ2, wσ3, σ1σ3 | path v–σ1–σ3–w–σ2, σ1 interior |

**x1 = 6.** The slots are Λ[9..12] with no escape; write a_k = L(Λ[k]). μ = Λ[9] gives three extras.
- **μ = Λ[12].** The extras are a11a10 and a10a9, both non-P′5.
  - T12 = w: only σ1σ3 is available among σ1, σ2, σ3.
  - T12 = σ1: a10 = w, a9 = σ2, and v is left with degree 3.
  - T12 = σ2: a10 = σ3, and v is left with degree 3.
- **μ = Λ[11].** The extras are v·a12 and a10a9.
  - T12 = w: a9 = σ1, a10 = σ3, a12 = σ2. This leaves path σ1–v–σ3–w–σ2, w interior.
  - T12 = σ1, with (a10, a9) ∈ {(σ2, w), (w, σ2)}: then a12 = σ3, and the extras vσ3, wσ2 leave path σ2–v–σ1–σ3–w, σ1 interior.
  - T12 = σ1, with (a10, a9) = (σ3, w): then a12 = σ2, and the extras vσ2, wσ3 leave the triangle v, σ1, σ3.
  - T12 = σ2, with (a9, a12) = (w, σ1): path w–σ2–v–σ3–σ1, σ2 interior.
  - T12 = σ2, with (a9, a12) = (σ1, w): the extra vw repeats P′5.
- **μ = Λ[10].** The extras are v·a12 and a12a11.
  - T12 = w, a12 = σ1: σ1 isolated.
  - T12 = w, a12 = σ3: path σ1–v–σ2–w–σ3, w interior.
  - T12 = σ1: a12 = σ3, a11 = w. This leaves path σ3–σ1–v–σ2–w, σ1 interior.
  - T12 = σ2, (a12, a11) = (σ3, w): σ2 interior.
  - T12 = σ2, (σ1, σ3): σ1 isolated.
  - T12 = σ2, (σ3, σ1): path σ1–v–σ2–w–σ3, σ2 interior.

## 6. Result

**WRITTEN, uses (R3) only through R3-pair:** type E (0,2,0,0) with d = 5 is impossible, and by the mirror so is d = −5.

Together with v138 §2 (|d| ∉ {0,1,2,3,7,8}), v139 (d = ±4) and v140 (d = ±6), **type E (0,2,0,0) is closed. Every type E cell of L2 (k = 3) is therefore closed.**

**OPEN residual of L2 (k = 3):**
- type A (0,2,0,0) and (0,1,1,0);
- type B (0,2,0,0) and (0,1,1,0);
- type C (0,2,0,0).

L1 types 1–4 and 7–12 remain open. The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
