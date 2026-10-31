# Original Tuscan-2(11), entire m = 9 distance-two branch, part 30: type C (0,2,0,0) closed, so type C is closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-typeE-0200-d5-closed-typeE-closed-v141.md` (SHA256 `f1ea7890aea810b28117d9ab89ab802402d4919501ceb658ddf8aa9df53e80de`).

Imports:
- type C formulas, v116 §2;
- RC, v134 §1;
- D2Q (v125 §1) and R3-pair (v130 §1), both of which use (R3);
- the pair count (K5) and the path-end rule, v141 §1.

This is written reasoning only. No interpreter, enumeration program, solver or search was used. Every finite case list is written out in full. It is not reviewed, formal or novelty-cleared.

## 1. Set-up for type C (0,2,0,0)

**Parameters.**
- n2 = 2 and n1 = n3 = nΛ = 0, so a = 3 and b = 8.
- ℓ1 = p1 + u, ℓ3 = 10 − p1 + u.
- x2 = x0 + p1 − 5, x3 = x1 + 5 − p1, and λ = 10 + x2 − x1.
- ℓ2 = 25 + x1 − x2 − u.
- Put A := 15 − x2 − u, B := 5 + x1 − u, d := B − A = x1 + x2 − 10, and κ := 10 − x3.

**F1 rows.**
- R_out = ℓ, T_int, b4, t1[1..u].
- M = t1[u..ℓ1−1], b5, t3[ℓ3−1..u].
- R_in = t3[u..1], b4, T_int, ℓ.

The F1 cuts are ℓ (v), t1[u] (c1) and t3[u] (c2).

**F2 rows** (mod 80). They follow from the positions K3 at x0, b4 at x0 + ℓ1, K2 at 30 + x1, K1 at 40 + x2 and K5 at 70 + x3.

| Row | Vertices |
|---|---|
| s0 | Λ[κ..λ−1], K3, T1 = t1[ℓ1−1..x2+u−5] |
| s1 | t1[x2+u−5..1], b4, t2[1..A] |
| s2 | t2[A..A+10] |
| s3 | t2[A+10..A+9+x1], K2, Λ[λ−1..x2] |
| s4 | Λ[x2..1], K1, t2[ℓ2−1..B+10] |
| s5 | t2[B+10..B] |
| s6 | t2[B..1], then b4 and t3[1..10−B] while 10 − B ≥ 0 |
| s7 | the rest of t3 up to t3[ℓ3−1], K5, Λ[1..κ] |

Here t2[A+9+x1] = t2[ℓ2−1] is adjacent to b5.

**General reductions,** exactly as in v138 §2:
- Row reversal (t1 ↔ t3) maps the cell to itself with d ↦ −d, so we may take d > 0.
- DP-1 on s2/s5 and s2/s6 leaves d ∈ {4, 5, 6}.
- x2 ≠ 5, since otherwise the s0/s1 cut t1[x2+u−5] would be t1[u]. Likewise x1 ≠ 5, by the s6/s7 cut t3[5+u−x1].
- As in v138, V_a ∈ t2[1..A−1], so A ≥ 2.
- R_out/s1 gives L(t2[1..A]) ⊆ T_int ∪ {v}.

**Label anatomy of type C.** Passage counts:
- a T-vertex has 2 F1 passages;
- a t1- or t3-vertex has 1 + 1;
- a t2- or Λ-vertex has 0 + 2;
- b4 has 2 + 2, and b5 has 1 + 4.

A label with its cut in F2 has 3 F1 and 7 F2 passages; one cut in F1 has 2 and 8. Hence:

| Label | Vertices |
|---|---|
| T_int (F2 cut) | T, one t1/t3 "M-vertex", three t2/Λ-vertices |
| F2-cut S | t1-arm, t3-arm, one M-vertex, two t2/Λ-vertices |
| c1 | t1[u], a t3-arm vertex, three t2/Λ |
| c2 | t3[u], a t1-arm vertex, three t2/Λ |
| w (F2 cut) | b4, W_M, two W's on t2 ∪ Λ |

**Where vertices lie in F2.**
- A t1 M-vertex lies in s1, on the s0/s1 cut, or in T1 ⊆ s0. A t3 M-vertex lies in s7.
- Λ[k] has its S_Λ1-passage in s4 if k < x2, in s3 if k > x2, and on the cut if k = x2. Its S_Λ2-passage is in s7 if k < κ, in s0 if k > κ, and on the cut if k = κ.
- A t2-vertex has one forward passage in s1, s2 or s3, and one backward passage in s4, s5 or s6.
- **(Π-slot)** A t2-vertex whose passages are a non-cut one in s3 and a non-cut one in s4 lies on t2[B+11..A+9+x1].

## 2. d = 4

**Set-up.**
- (x1, x2) ∈ {(6,8), (7,7), (8,6)}.
- Exchanging s2 with s5 gives the saturated block Q = L(P) = L(P′), with P = t2[A..A+3] and P′ = t2[A+11..A+14]. Here t2[A] is the s1/s2 cut and t2[A+14] is the s4/s5 cut.
- A Q-label covers s2 and s6 by P, and s3 and s5 by P′. It must still cover s0, s1, s4 and s7.

**RC classification of Q-labels.**
- **v ∉ Q:** V_a ∉ P.
- **T_int Q-labels.** The cut at t2[A+14] is impossible: the third t2/Λ-vertex would repeat s3, s4, s5 or s6. That leaves:
  - q1 = L(t2[A]), with a Λ-vertex in Λ[1..x2−1];
  - λ7 = L(Λ[κ]), which needs κ < x2 and an M-vertex strictly inside s1;
  - τ01 = L(t1[x2+u−5]), with a Λ-vertex on Λ[1..x2−1] whose S_Λ2-passage lies in s7.
- **F2-cut S.** The only one is S_end = L(t2[A+14]), with its t1-arm in s1, its M-vertex strictly inside T1, and its t3-arm strictly inside s7.
- **c1, c2.** Each has a Λ-vertex in Λ[1..x2−1], and its arm or t3[u] lies in s7 (strictly, for c1).
- **w.** If corner23 of b4 lies outside s6 (only for A = 7, which here means x2 = 6), w may stand at t2[A+14] instead of S_end. Otherwise R_in/s6 gives Q ⊆ S ∪ T_int ∪ {v}, so w ∉ Q.
- The label at t2[A+14] has no Λ-vertex. The other three Q-labels lie on the row-path Λ[1..x2−1] ⊆ s4.

By D2Q, x2 ≥ 7.
- **(6,8) is impossible.** S_end's t3-arm must lie strictly inside s7 and below t3[u]: t3[6+u−x1..u−1] = ∅.
- **(7,7) is impossible.**
  - S_end's t3-arm is forced to t3[u−1].
  - c1 would need that same vertex, and c2 = t3[u] would be adjacent to it. So Q = {q1, S_end, λ7, τ01}; if κ ≥ x2, λ7 is unavailable and |Q| < 4 already.
  - λ7's M-vertex must be t1[u+1], the only M-vertex strictly inside s1. It is adjacent to τ01's t1[u+2], against (E).

## 3. d = 6

**Set-up.** (x1, x2) ∈ {(7,9), (8,8), (9,7)}, and λ − x2 = 10 − x1 ≤ 3. As in v140:
- Q = L(P) = L(P′), with P = t2[A+7..A+10] and P′ the four vertices of s6 after t2[A] (same table by A).
- Q is saturated, so no other edge joins two Q-labels.
- (Z) places every Q-label at t2[A+7..A+9] on the last four vertices of s3: t2[A+17..A+9+x1], b5, Λ[λ−1..x2]. v ∈ Q, because the label at t2[A+6] is cut.

**RC in type C** (P′'s t2-vertices interior unless they are the s6/s7 cut).
- **T_int Q-labels:**
  - τ_P (cut t2[A+10], Λ-vertex on Λ[1..x2−1]);
  - τ_Λ (cut Λ[x2]);
  - τ_P′ (only for A ≥ 5: cut at the end of P′, a Π-slot t2-vertex, M-vertex in T1).
- **w** (A ≤ 4).
  - If w is not the label at t2[A+10], its b4 corner23 is interior to s6 (A ≤ 3). Then w is cut at Λ[x2].
  - For A = 4, w is cut at b4, which lies on the s6/s7 cut. It then has a Π-slot W and W_M in T1.
- **The S-label cut at the end of P′** has a Π-slot t2-vertex.
- **An F2-cut S-label not at t2[A+10]** with t3-arm interior to s6 is cut at Λ[x2].

**Cases.**
- **A ≥ 5.** Here Q ⊆ T_int ∪ {v}, so Q = {τ_P, τ_P′, τ_Λ, v}.
  - (9,7): τ_Λ = Λ[7] = Λ[λ−1] is adjacent to b5.
  - (8,8) (u = 2, A = 5): τ_P′'s Π-slot is t2[22] = t2[ℓ2−1], adjacent to b5.
- **A = 4.** Q = {τ_P, τ_Λ, v, w}. w's Π-slot must avoid t2[ℓ2−1], so x1 = 9. Then τ_Λ = Λ[λ−1] is adjacent to b5.
- **A = 3.** Q = {θ1, θ2, w, σ}, with σ = L(t3[1]) cut at the s6/s7 cut, so σ has a Π-slot.
  - If t2[13] = w: Q = {τ_Λ, v, w, σ}. σ's slot must avoid t2[ℓ2−1], forcing x1 = 9, and then τ_Λ = Λ[λ−1] is adjacent to b5.
  - If t2[13] = τ_P: w is cut at Λ[x2], so the other θ is v. σ's slot then forces x1 = 9, and w = Λ[7] = Λ[λ−1] is adjacent to b5.
- **A = 2.** θ = v. σ2 = L(t3[2]) has a Π-slot avoiding t2[ℓ2−1], so x1 = 9.
  - Every other Q-label not at t2[12] lies on Λ[x2] = Λ[λ−1] (adjacent to b5) or on Λ[x2+1..λ−1] = ∅.
  - Since t2[12] ∈ {w, σ1}, one of σ1 and w has no admissible place.

## 4. d = 5

**Set-up.**
- (x1, x2) ∈ {(6,9), (7,8), (8,7), (9,6)}.
- Q := L(P5) = L(P′5), with P5 = t2[A+6..A+10] and P′5 the five vertices of s6 after t2[A].
- μ = L(t2[A+5]); its vertex is cut, so μ ∉ Q and μ ≠ v.
- (Z5) as in v141. Its right side lives on Π, the last five vertices of s3: t2[A+16..A+9+x1], b5, Λ[λ−1..x2]. Π carries exactly μ, v and Q ∖ {v, T}, where T is the label at t2[A+10]. So v ∈ Q.
- μ must be interior to Π, otherwise there would be three extras. Then the two extras fix P5 by (K5).

**Cases.**
- **A ≥ 6.** |Q ∩ (T_int ∪ {v})| ≤ 4 < 5.
- **A = 5.** L(t2[1..4]) ⊆ {τ_P, τ_Λ, v} is impossible.
- **A = 4.** Q = {τ_P, τ_Λ, v, w, σ}. w is not at t2[14], and its b4 corner23 is interior to s6, so RC puts w at Λ[x2]. But Λ[x2] carries τ_Λ.
- **A = 3.** P′5 = (θ1, θ2, w, σ1, σ2), with t3[2] the cut.
  - RC: σ2 occupies a Π t2-slot.
  - w and any F2-cut σ1 other than T occupy π5 = Λ[x2].
  - c1 occupies a Λ-slot in Λ[x2+1..λ−1].
  - τ_Λ = π5.
  - **x1 = 6:** no t2-slot for σ2.
  - **x1 = 9:** no Λ-slot for c1, and π5 cannot hold two of {τ_Λ, w, σ1}.
  - **x1 = 7** (Π = t2[19], b5, Λ[10], Λ[9], Λ[8]): σ2 = π1 and v = π2.
    - T = τ_P: w = π5, σ1 = c1, and μ is the other of Λ[9..10].
      - μ = Λ[10] makes {σ1, w} an extra, which repeats P′5.
      - μ = Λ[9]: extras vσ2 and vσ1. θ2 = τ_P leaves path σ1–P–σ2–w–v with P interior; θ2 = v leaves P with degree 3.
    - T = w: π5 = τ_Λ, σ1 = c1. Required end w.
      - μ = Λ[10] (extras vσ2, Lσ1): θ2 = L gives path L–σ2–w–v–σ1, w interior; θ2 = v leaves v and σ1 isolated together.
      - μ = Λ[9] (extras vσ2, vσ1): θ2 = L gives path v–w–σ2–L–σ1, w interior; θ2 = v leaves v isolated.
    - T = σ1: τ_Λ and w both need π5.
  - **x1 = 8** (Π = t2[19], t2[20], b5, Λ[8], Λ[7]): c1 = Λ[8], μ = t2[20] and σ2 = t2[19].
    - T = τ_P: π5 = w, and the extra {σ1, w} repeats P′5.
    - T = w: π5 = τ_Λ, with extras vσ1 and σ1L. θ2 = L or v leaves σ2 with degree 3.
    - T = σ1: π5 conflict.
- **A = 2.** θ = v, P′5 = (v, w, σ1, σ2, σ3) with t3[3] the cut.
  - σ3 occupies a Π t2-slot.
  - The two labels of {w, σ1, σ2} ∖ {T} are π5 and a c1 on Λ[x2+1..λ−1].
  - **x1 = 6:** no t2-slot. **x1 = 9:** no Λ-slot.
  - **x1 = 7:** σ3 = t2[18], v = π2.
    - μ = Λ[10], c1 = Λ[9], extras vσ3 and c1·π5. Only (c1, π5, T) = (σ2, w, σ1) avoids repeating P′5, and it leaves path σ2–v–σ1–σ3–w with σ1 interior.
    - μ = Λ[9], c1 = Λ[10], extras vσ3 and v·c1.
      - c1 = σ1 leaves path v–σ2–w–σ3–σ1, whose ends exclude T ∈ {w, σ2}.
      - c1 = σ2 leaves path v–σ1–σ3–w–σ2, whose ends exclude T ∈ {w, σ1}.
  - **x1 = 8:** σ3 = t2[18], μ = t2[19], c1 = Λ[8], π5 = Λ[7], extras v·c1 and c1·π5.
    - Only c1 = σ2 with π5 = w avoids repeating P′5, so T = σ1.
    - The remaining pairs vσ1, vσ3, wσ3, σ1σ3 give σ3 degree 3.

## 5. Result

**WRITTEN, uses (R3) through D2Q (§2) only:** type C (0,2,0,0) is impossible. With v128–v137, **every type C cell of L2 (k = 3) is closed.**

**OPEN residual of L2 (k = 3):**
- type A (0,2,0,0) and (0,1,1,0);
- type B (0,2,0,0) and (0,1,1,0).

L1 types 1–4 and 7–12 remain open. The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
