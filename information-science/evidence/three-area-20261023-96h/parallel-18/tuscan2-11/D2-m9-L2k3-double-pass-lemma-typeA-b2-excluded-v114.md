# Original Tuscan-2(11), entire m = 9 distance-two branch, part 3: L2 with k = 3 — face types, the double-pass lemma, and type A with b = 2 excluded

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143 (SHA256 `43af3295b857ccd709c9661d006de759bf9f07ce8607f0b6028d226db2206ec7`). It continues `D2-m9-L4B-W1-kx2-kx3-kx4-excluded-L4B-closed-v113.md` (SHA256 `a561978485912ece66908d9a41fa2689cf4cab510d50eff2c076837a8964d575`).

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. Everything here uses (R1)–(R2) only; distance two (R3) is not needed.

## 1. Setting: L2 with k = 3 (v94 §5.2)

**The graph H.**
- Label v has a leaf ℓ (the v-cut), the branch b5 of degree 5, and two 2-vertices.
- Label w has the branch b4 of degree 4 and three 2-vertices.
- The other nine labels have five 2-vertices each.
- H consists of the tail T (from ℓ to b4, length t ≤ 9), three threads t1, t2, t3 from b4 to b5 (lengths ℓ1, ℓ2, ℓ3), and a loop Λ at b5 (length λ).
- These lengths satisfy t + ℓ1 + ℓ2 + ℓ3 + λ = 55.
- The rotation at b4 is (T, t1, t2, t3), which names the threads.
- The array is connected and has 11 rows. Every row carries all 11 labels exactly once (the exchange identity).

**Imports:**
- **(E)** Exactness: |E| = 55 with one edge per unordered pair, so two distinct H-edges never have the same label pair (v94 §1).
- **(C)** Every label has exactly one cut (v79 §2).
- **(I)** The face identity passages_x(F) = r_F − [x's cut ∈ F] (v12 (1)). Consequently each face's rows alternate with its cuts: a label whose cut is not in F has exactly one passage per row of F.

**Arms.** Put u = 10 − t. Then:

    R_out = ℓ, T_int, b4, t1[1..u]   and   R_in = t3[u..1], b4, T_int, ℓ.

These give L(t1[1..u]) = L(t3[1..u]) = S := X ∖ ({v, w} ∪ L(T_int)), with |S| = u. No arm vertex carries v, so both arms stay inside their threads and ℓ1, ℓ3 ≥ u + 1 (v94 §6).

**Face types.** Write the rotation at b5 as (Λ+, t_x, Λ−, t_y, t_z) with type (x,y,z). Tracing gives two faces in each case:

| Type | F1 (contains T) | F2 |
|---|---|---|
| A = (1,2,3) | T t1 Λ t1⁻ t2 t3⁻ T⁻ | t3 Λ t2⁻ |
| B = (1,3,2) | T t1 Λ t1⁻ t2 Λ⁻ t3⁻ T⁻ | t3 t2⁻ |
| C = (2,1,3) | T t1 t3⁻ T⁻ | t2 Λ t2⁻ t3 Λ⁻ t1⁻ |
| E = (2,3,1) | T t1 Λ t3⁻ T⁻ | t2 Λ t2⁻ t3 t1⁻ |

Row reversal maps (x,y,z) to (σx, σz, σy) with σ = (1 3). So (3,1,2) is the mirror of A and (3,2,1) is the mirror of B, while C and E are self-mirror.

**Row counts.** Let r(F1) = a and r(F2) = b, with a + b = 11. Applying (I) to v:
- **Type A:** a = 9 − n′ and b = 2 + n′, where n′ is the number of v-2-vertices off t1. Also t + ℓ1 = 55 − 10b.
- **Type B:** (a, b) ∈ {(9,2), (8,3)}, ℓ2 + ℓ3 = 10b, and t + ℓ1 + λ = 55 − 10b.
- **Type C:** a = A + 3 ∈ {3, 4, 5}, where A is the number of v-2-vertices on t1 ∪ t3.
- **Type E:** a = A + 4 ∈ {4, 5, 6}, where A is the number of v-2-vertices on t1 ∪ Λ ∪ t3.

## 2. The double-pass lemma (T1)

**Set-up.** Let θ be a thread or the loop, with interior θ[1..L−1]. Its two passes run in opposite directions:
- θ[j] sits at position f + j in face F;
- θ[j] sits at position g − j in face F′ (possibly F′ = F).

Measure positions from each face's cut grid. Forward cuts then fall at indices j ≡ φ (mod 10) and backward cuts at j ≡ φ + ρ (mod 10), where ρ ≡ f + g − c_F − c_F′ (mod 10).

A forward θ-row is θ[s..s+10] with s ≡ φ, and a backward θ-row is θ[s′..s′+10] with s′ ≡ φ + ρ. Both require all eleven vertices to be interior to θ.

**Blocks.** The index line splits into alternating blocks:
- B-blocks [s, s+ρ−1], each starting at a forward cut;
- C-blocks [s+ρ, s+9], each starting at a backward cut.

Exchanging the forward row θ[s..s+10] (rule (X)) gives:
- with the backward row θ[s+ρ..s+ρ+10]: **L(B) = L(B + 11)**;
- with the backward row θ[s+ρ−10..s+ρ]: **L(C) = L(C + 11)**, for the C-block C = [s+ρ−10, s−1].

Here B + 11 is a path ending at a backward cut, and C + 11 is a path ending at a forward cut.

**Lemma DP-1 (one block).** Each of the following is impossible:
- **ρ = 0** while some interior index is ≡ φ. That vertex would have two cut passages.
- **A block of size m ∈ {1, 2, 3}** with its equality available. That is, ρ ∈ {1,2,3} with a window [s, s+ρ+10] ⊆ [1, L−1], or ρ ∈ {7,8,9} with a window [s+ρ−10, s+10] ⊆ [1, L−1].

*Proof.*
- m = 1: one label sits on a forward cut and on a backward cut, against (C).
- m = 2: the two one-edge paths carry the same label pair, against (E).
- m = 3: two 3-vertex paths on the same three labels each use two of the three pairs, so they share a pair, against (E). ∎

**Lemma DP-2 (chain).** Suppose:
- P1 and P1′ are vertex-disjoint paths of m vertices with L(P1) = L(P1′), where P1′ = (q1, …, qm);
- P2 = (y, q1, …, q_{m−1}) is a path;
- P2′ is a path of m vertices with L(P2′) = L(P2), and its edges differ from those of P1, P1′ and P2.

Then m ∉ {4, 5}.

*Proof.*
- By (E), the edges of P1 and P1′ carry distinct pairs.
- **m = 4:** P1 ∪ P1′ uses all six pairs of the four labels. P2′ has three edges on {y, q1, q2, q3}, and y lies on at most two of them. So at least one edge of P2′ joins two of the q's, and its pair is already used. Contradiction.
- **m = 5:** two of the ten pairs are unused. q5 is an end of P1′, so its unused degree is 3 − deg_P1(q5) ≥ 1. Hence at most one unused pair avoids q5. But P2′ needs at least two edges inside {q1,…,q4}: y lies on at most two of its four edges, and the pair {y, q1} is taken by P2. Contradiction. ∎

**Applying DP-2.** Inside a double pass, this applies to consecutive blocks of one kind when ρ ∈ {4, 5} (B-blocks) or ρ ∈ {5, 6} (C-blocks). The windows needed are:
- [s, s+ρ+20] for B-blocks;
- [s+ρ−10, s+20] for C-blocks.

The final partner P2′ may also be any path with L(P2′) = L(P2) supplied by an exchange, for example across b5 into Λ.

**Consequence.** If L ≥ 35, θ is impossible for every ρ. If L ≥ 24, then ρ ∈ {4, 5, 6}.

## 3. Type A with b = 2 is impossible

**Parameters.** Here n′ = 0, so both v-2-vertices lie on t1.
- a = 9, ℓ1 = 35 − t = u + 25, and ℓ2 + ℓ3 + λ = 20.
- In F1 (cuts at multiples of 10):
  - t1[j] sits at t + j;
  - b5 sits at 35;
  - Λ[k] sits at 35 + k;
  - b5 sits again at 35 + λ;
  - t1[j] sits again at 60 + u + λ − j;
  - b4 sits at 60 + u + λ;
  - then come t2, b5 and t3⁻, ending with t3[u] at 80 and R_in.

**DP on t1.** φ ≡ u and ρ ≡ λ (mod 10). The rows t1[u..u+10] and t1[u+10..u+20] are forward θ-rows, and every window in Lemma DP-1 fits inside [1, u+24]. So λ mod 10 ∈ {4, 5, 6}.

**Alternation of v in F1.**
- b5 at 35 and at 35 + λ needs a cut between, so λ ≥ 6.
- ℓ3 ≥ u + 1 and ℓ2 ≥ 1 give λ ≤ 18 − u.
- λ = 15 puts b5 on the cut 50.
- λ = 16 leaves row 4 = [40,50] with only Λ-vertices, and there is no v on Λ.

So λ ∈ {6, 14}.

**λ = 14.** Here ℓ2 + ℓ3 = 6, so u ≤ 4. Row 7 = [70,80] is:

    t1[u+4..1], b4, t2_int, b5, t3[ℓ3−1..u].

It contains all of t1[1..u], which carries S, and also t3[u], whose label c2 lies in S. Since c2 ≠ L(t1[u]) by (C), the label c2 occurs twice in row 7. Contradiction.

**λ = 6.** The relevant rows are:

| Row | Positions | Vertices |
|---|---|---|
| 2 | [20,30] | t1[u+10..u+20] |
| 3 | [30,40] | t1[u+20..u+24], b5, Λ[1..5] |
| 4 | [40,50] | Λ[5], b5, t1[u+24..u+16] |
| 5 | [50,60] | t1[u+16..u+6] |

Two exchanges follow:
- Rows 2 and 5 give L(t1[u+6..u+9]) = L(t1[u+17..u+20]). Here t1[u+6] is the backward cut at 60 and t1[u+20] is the forward cut at 30.
- Rows 3 and 4 give L(t1[u+16..u+19]) = L(Λ[1..4]).

Apply DP-2 with m = 4:
- P1 = t1[u+6..u+9];
- P1′ = t1[u+17..u+20];
- P2 = t1[u+16..u+19], which starts at the new backward cut t1[u+16] and continues with the first three vertices of P1′;
- P2′ = Λ[1..4].

This is a contradiction, for every u.

**So type A with b = 2 is impossible (T1).**

## 4. Result and open part

**WRITTEN:**
- the L2 (k = 3) face-type table and row counts (§1);
- Lemmas DP-1 and DP-2 (§2);
- type A with b = 2 is impossible (§3).

**Open in the v143 branch:**
- L2 with k = 3: type A with b ∈ {3, 4}; type B with b ∈ {2, 3}; type C with a ∈ {3, 4, 5}; type E with a ∈ {4, 5, 6};
- L1.

L4-B is closed (v113). The v143 acceptance ceiling is unchanged:
- the support-9 statement may be made only after all three families are excluded;
- an m ≥ 10 consequence needs the full m ≤ 8 plus m = 9 joint gate;
- every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
