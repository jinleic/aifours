# Actual Tuscan11, m = 9, line L2 (5 at v, 4 at w), core k = 1 — excluded by the tail face

Actual `/bin/date` before this body: **Mon Oct 26 13:43:25 PDT 2026**. InfoRecursiveMDS18-2.

**Status.** NEW exact WRITTEN CANDIDATE: not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO.

**Scope.** Tuscan-1-only support-ladder work on R6 (all m ≥ 9, no Tuscan-2 cap). This is a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result. It is a separate, ungated successor line, outside the v19–v49 and v150b freezes.

## 1. Setting and imports

**Setting** (v94 §5.2, SHA256 `1c5465c4f0a5835ecda93a2a9877d42f3b607d774f63e49be9f1228a951c396c`):
- The leaf ℓ has label v and is the v-cut. Its tail T has length t ≤ 9 and ends at b4, which has label w.
- In the k = 1 core:
  - b4 has rotation (T, L, θ, L′), where L and L′ are the ends of a loop Λ of length λ and θ is the thread to b5;
  - b5 (label v) has the interleaved rotation (θ, M1, N1, M2, N2), with loops M and N (v94 §5 (iii)).
- v has exactly two 2-vertices and w has three.

**Imports:**
- the face identity of v12 (1): passages_x(F) = r_F − 1_(x ∈ C_F), where passages count visits of x-vertices along F;
- each label has one cut;
- two vertices with the same label lie in different rows of every face that passes both. Equivalently, along a face, some cut lies strictly between them;
- the exchange identity;
- the row-reversal symmetry: reversing all rows gives a Tuscan-1 array with the same split graph and reversed rotations.

## 2. Faces

Tracing gives exactly two faces:
- **F_T:** b4 → T → ℓ → T → b4 → Λ (from L to L′) → b4, with corners (T→L) and (L′→T).
- **F′:** b4 → θ → b5 → M → b5 → N⁻ → b5 → M⁻ → b5 → N → b5 → θ⁻ → b4 → Λ⁻ (from L′ to L) → b4. It visits the remaining two corners of b4 and all five corners of b5.

Write u = 10 − t. Then R_out = ℓ, T, b4, Λ[1..u] and R_in = Λ[λ−u..λ−1], b4, T, ℓ are rows of F_T, and

    L(Λ[1..u]) = L(Λ[λ−u..λ−1]) = S := X ∖ ({v, w} ∪ L(T_int)).

Every other row of F_T lies inside Λ's interior. Call these the middle rows M1, M2, ….

## 3. Face identities

T_int lies in R_out ∩ R_in, which contain ℓ (label v) and b4 (label w). So T carries no v and no w.

**Label v.** Let A be the number of v-2-vertices on Λ, and B = 2 − A the number elsewhere. Then:
- F_T contains the v-cut ℓ: 1 + A = r_T − 1;
- F′: 5 + A + 2B = r′.

Hence **r_T = A + 2 ∈ {2, 3, 4}** and r′ = 9 − A.

**Label w.** Let A_w be the number of w-2-vertices on Λ, and ε_T = 1 if the w-cut lies in F_T. Then 2 + A_w = r_T − ε_T, so A_w = A − ε_T.

Every middle row is a pure loop row, so it contains a v-vertex and a w-vertex of Λ. Also λ = 10 r_T − 2t.

## 4. r_T = 2 is impossible

Here λ = 20 − 2t, and R_out ∪ R_in covers all of Λ's interior. **So no loop vertex carries v or w.**

**Case t ≤ 8.**
- Since Λ[u] is common to both arms, L(Λ[1..u−1]) = L(Λ[u+1..2u−1]).
- The vertex Λ[u−1] and its equal-label partner in Λ[u+1..2u−1] must be separated in F′. The cut cannot sit at Λ[u], whose label already has its cut in F_T. So F′ has a cut c ≥ u+1.
- Symmetrically, Λ[u+1] and its partner force a cut c′ ≤ u−1.
- Cuts along a face differ by multiples of 10, and c − c′ ≤ 2u − 2 < 20. So c = c′ + 10, and the F′ row Λ[c′..c] lies inside the loop.
- That row must contain v. Contradiction.

**Case t = 9.** Λ has the single interior vertex Λ[1], which is the F_T cut. So F′ passes b4, Λ[1], b4 within one row. Contradiction.

## 5. r_T = 3 is impossible

Here A = 1, and M1 = Λ[u..u+10] needs a w on Λ. So A_w = 1 and ε_T = 0.

**Loop labels.**
- Λ carries exactly one v-vertex and one w-vertex, and every T_int label exactly once, all inside M1int = Λ[u+1..u+9].
- Put c1 = L(Λ[u]) and c2 = L(Λ[u+10]); these are F_T cuts, and c1, c2 ∈ S.
- Each x ∈ S ∖ {c1, c2} has loop vertices i1 < u < i2 < u+10 < i3, with i2 in M1int.

**At most one full loop row in F′.** Every F′ row lying inside the loop needs the single loop v-vertex. That vertex is not a cut, so at most one such row exists, and F′ has at most two cuts on the loop.

**Case t ≤ 7.** Here S ∖ {c1, c2} ≠ ∅.
- Some such x forces F′ cuts in (i1, i2) and in (i2, i3). These are γ and γ+10, and Φ = Λ[γ..γ+10] is a full loop row containing i2 for every such x.
- Φ carries all 11 labels. The vertices with labels v, w and T_int, together with these i2, are exactly the nine vertices of M1int. So M1int ⊆ Φ, and γ ∈ {u−1, u+1}.
- If γ = u−1: Φ = Λ[u−1..u+9], so L(Λ[u−1]) = c2, an F′ cut on a c2-vertex. Contradiction.
- If γ = u+1: L(Λ[u+11]) = c1, an F′ cut on a c1-vertex. Contradiction.

**Case t = 9.** Both arms are single cut vertices with S = {c1}, so c1 = c2. Two cuts of one label. Contradiction.

**Case t = 8.** Here λ = 14 and Λ[1], Λ[2], Λ[12], Λ[13] carry c2, c1, c2, c1.
- The pairs force exactly one F′ cut on the loop, at γ ∈ [4, 10]; a second cut would land on Λ[1] or Λ[13].
- The two F′ rows meeting at Λ[γ] both contain b4.
- The loop w-vertex lies in M1int = Λ[3..11], so it falls in one of these rows. Contradiction.

## 6. r_T = 4 is impossible

Here A = 2 (so B = 0) and A_w = 2 (one w on each middle row). Write j_v1, j_w1 ∈ M1int and j_v2, j_w2 ∈ M2int.

**Exactly two full loop rows in F′.**
- The two F′ rows at the ends of the loop stretch contain b4, so the loop w-vertices lie in full loop rows: there are at least two.
- Each full loop row needs a loop v-vertex, of which there are two: there are at most two.
- So F′ has exactly the cuts γ, γ+10, γ+20 on the loop. The full rows are Φ1 = Λ[γ..γ+10] and Φ2 = Λ[γ+10..γ+20]. The end row E1 contains Λ[1..γ] and b4.

**Normalising δ.** Put δ = γ − u.
- δ ≠ 0, since cuts do not coincide.
- Row reversal maps δ to −δ, so take δ ≥ 1.
- Φ2 ends inside the loop, so δ ≤ u − 1.

**Exchanges.**
1. j_v1 ∈ Φ1, not E1, so E1's loop part Λ[1..u+δ] has no v.
2. E1 versus R_out gives L(Λ[u+1..u+δ]) ⊆ {v} ∪ L(T_int). So these labels are T_int labels.
3. M1 versus Φ1 gives L(Λ[u..u+δ−1]) = L(Λ[u+11..u+10+δ]) ⊆ {c1} ∪ T_int.
4. M2 versus Φ2 gives L(Λ[u+10..u+9+δ]) = L(Λ[u+21..u+20+δ]) ⊆ S, since this lies in R_in's arm.
5. Hence the δ−1 vertices Λ[u+11..u+9+δ] have distinct labels in S ∩ ({c1} ∪ T_int) = {c1}, so δ ≤ 2.

**Both values fail.**
- **δ = 1.** Step 3 gives L(Λ[u+11]) = c1. But Λ[u+11] = γ+10 is an F′ cut. Contradiction.
- **δ = 2.** Steps 3 and 5 give L(Λ[u+11]) = c1. Step 4 then gives {L(Λ[u+21]), L(Λ[u+22])} = {c2, c1}. But Λ[u+22] = γ+20 is an F′ cut on a c-label vertex. Contradiction.

## 7. Result

**L2 with core k = 1 is impossible** (WRITTEN, Tuscan-1 necessary case).

Remaining at m = 9 (v94): L1, L2 with k = 3, L3 (reduced) and L4-B (reduced). Separately: L2 with k = 3 always has exactly two faces. Tracing all six relative orders of the three threads at b4 and b5 gives F = 2 in every case; this tracing is part of the next packet.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
