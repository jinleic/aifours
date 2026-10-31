# Original Tuscan-2(11), entire m = 9 distance-two branch, part 36: type A (0,2,0,0) — set-up, two covering rules, and δ ∈ {4, 6, −4, −5, −6} closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-typeB-lambda2-lemma-typeB-closed-v147.md` (SHA256 `14f049df17d412ab14b22bbab20bfd3f02ca50e775ad10d29704c0bcb871f5b8`).

Imports:
- type A formulas, v116 §2;
- DP-1 and DP-2, v114 §2;
- RC, v134 §1;
- D2Q, v125 §1, which uses (R3).

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Set-up

**Parameters.**
- p1 = 5, n2 = 2, a = 7, b = 4.
- ℓ1 = 5 + u, λ = 5 + p2, ℓ2 = A + 10 + p3 and ℓ3 = 10 − p3 + u.
- Put A := 15 − p2 − u.
- y1 = y0 + p2 − 5, with y0, y1 ∈ [1, 9].

**F1 rows** (b5 at 15, 20 + p2 and 50 + p3). Here the R2/R3 cut is t1[u+p2−5] when u + p2 ≥ 6.

| Row | Vertices |
|---|---|
| R0 | ℓ, T_int, b4, t1[1..u] |
| R1 | t1[u..u+4], b5, Λ[1..5] |
| R2 | Λ[5..4+p2], b5, t1[u+4..u+p2−5] |
| R3 | t1[u+p2−5..1], b4, t2[1..A] |
| R4 | t2[A..A+10] (pure) |
| R5 | t2[A+10..A+9+p3], b5, t3[ℓ3−1..u] |
| R6 | t3[u..1], b4, T_int, ℓ |

The F1 cut labels are:
- v;
- c1 = L(t1[u]);
- λ5\* = L(Λ[5]);
- τ3 at the R2/R3 cut;
- α = L(t2[A]);
- β = L(t2[A+10]);
- c2 = L(t3[u]).

**F2 rows** (S_Λ2 then S_23). Put G2 := ℓ2 + y1 − 20 and H2 := G2 + 10.

| Row | Vertices |
|---|---|
| q0 | t3-tail, b5 (y0), Λ[λ−1..y1] |
| q1 | Λ[y1..1], b5 (10+y1), t2[ℓ2−1..H2] |
| q2 | t2[H2..G2] (pure) |
| q3 | t2[G2..1], b4, t3-head |

The q0/q1 cut is Λ[y1], so y1 ≠ 5.

**Anatomy.**
- *Group 1* = T and t1: two F1-passages, no F2-passage.
- *Group 2* = Λ, t2 and t3: one passage in each face.
- An F1-cut label has one group-1 vertex and four group-2 vertices.
- An F2-cut label has two group-1 vertices and three group-2 vertices.

## 2. Two covering rules (type A with a = 7)

**Rule A1 (R0).** R0 = ℓ, T_int, b4, t1[1..u] contains no group-2 vertex. So every F1-cut label other than v and w covers R0 with its single group-1 vertex, which is T, a t1-arm vertex, or c1's t1[u].

- If u + p2 ≥ 6, τ3 = L(t1[u+p2−5]) has that vertex as its group-1 vertex. It is not w, because an F1-cut w has no group-1 W. So t1[u+p2−5] must lie in R0, which forces **p2 ≤ 4**.
- If u + p2 ≤ 5, then p2 ≤ 5 − u ≤ 3.

**Rule A2 (R1).** R1's only group-2 vertices are Λ[1..5], and Λ[5] is λ5\*'s cut. By Rule A1, an F1-cut label other than v, w, c1 and λ5\* has its group-1 vertex in R0 but not in R1. So it has a Λ-vertex in Λ[1..4].

## 3. The shift and the easy values

R4 (forward) and q2 (backward) are pure t2-rows. Put δ := G2 − A = p3 + y1 − 10. As in v143 §1, DP-1 gives δ ∈ {±4, ±5, ±6}.

**δ ∈ {−5, −6}: DP-2**, exactly as in v145 §1, with R3 in place of v145's R3 and q1, q2 in place of r0, r1:
- R3 with q2 gives L(t2[A+1..A+10−m]) = L(the first 10 − m vertices of R3);
- R4 with q1 gives L(t2[A..A+9−m]) = L(the 10 − m vertices of q1 beyond t2[A+10]).

DP-2 with block size 10 − m ∈ {5, 4} gives a contradiction.

**δ = 6: the 4-path argument of v144 §1.**
- Exchanging R4 with q3 gives the saturated block Q = L(t2[A+7..A+10]).
- Exchanging R5 with q2 (shared vertices t2[A+10..A+16], so p3 ≥ 7) gives L(t2[A+6..A+9]) = L(the last four vertices of R5).
- Three Q-labels on a 4-path force an adjacency, against (E).

## 4. δ = 4 is impossible

**Set-up.** Q = L(P) = L(P′), with P = t2[A..A+3] (in R4 and q3; t2[A] is α's cut) and P′ = t2[A+11..A+14] (in R5 and q2; t2[A+14] = t2[H2] carries the F2-cut label H\*). D2Q applies.

**Candidates.** A Q-label's P and P′ already fill R4, R5, q3 and q2.
- β and c2: their cuts would repeat R4 or R5.
- c1: it would need a group-2 vertex in R3 outside q3.
- If u + p2 ≤ 5, the R2/R3 cut label lies on b4 or t2, and it is excluded the same way. That leaves too few candidates. So **u + p2 ≥ 6**.
- The F2-cut labels other than H\*: the q2/q3 and q3/q0 cut labels repeat q2 or q3. The q0/q1 cut label λy\* = L(Λ[y1]) has P, P′ and Λ[y1] as its group-2 vertices. Its two group-1 vertices must then cover R0, R3, R6 and one of R1, R2. T is forced (R6) and takes R0, so one t1-vertex would need passages in R3 and in R1 or R2. That is impossible for p2 ≤ 4.

**Hence Q = {α, H\*, τ3, λ5\*}**, with these RC forms:
- τ3 = {t1[u+p2−5], P, P′, Λ (R1, q1), t3 ∈ q0 ∩ R6};
- λ5\* = {t1-arm (R0, R3), Λ[5] ∈ q1, P, P′, t3 ∈ q0 ∩ R6}, which needs **y1 > 5**;
- H\* = {two t1-vertices, t2[H2], P-vertex, t3 ∈ q0 ∩ R6};
- α = {T, t2[A], P′, Λ ∈ R1, Λ ∈ R2} or {t1-arm (R0, R2), t2[A], P′, Λ ∈ R1, t3 ∈ q0 ∩ R6}.

**Contradiction.**
1. The t3-vertices in q0 ∩ R6 lie on t3[7−A..u−1], a row-path with u + A − 7 = 8 − p2 vertices.
2. τ3, λ5\* and H\* place three Q-labels there, so D2Q gives 8 − p2 ≥ 6, i.e. p2 ≤ 2.
3. y1 > 5 forces y0 + p2 > 10, so p2 = 2 and y1 = 6.
4. α's first form needs a Λ-vertex in R2 other than Λ[5]; the only one is Λ[6] = Λ[y1], which is an F2 cut.
5. So α takes the second form. Then four Q-labels need non-adjacent positions on a 6-vertex row-path, against D2Q.

## 5. δ = −4 is impossible

**Set-up.** Q = L(P) = L(P′), with P = t2[A−4..A−1] (in R3 and q2; t2[A−4] = t2[G2] carries G\*) and P′ = t2[A+7..A+10] (in R4 and q1; t2[A+10] carries β).

**RC.**
- β = {t1-arm (R0, R2), Λ (R1, q0), t3 ∈ R6 ∩ q3, P, P′}.
- c2 = {t1-arm (R0, R2), Λ (R1, q0), t3[u] ∈ q3, P, P′}.
- λ5\* = {T, Λ[5] ∈ q0, P, P′, t3 ∈ R5 ∩ q3}.
- c1 = {t1[u], P, P′, t3 ∈ R5, t3 ∈ R6}.

**F2-cut candidates.** A Q-label's P and P′ fill q2 and q1, so its cut must cover q0 and q3. G\* (q2/q3) is in Q. The q0/q1 and q1/q2 cut labels repeat q1. The q3/q0 cut label γ = L(t3[14−A]) can lie in Q, in the form γ = {T, t1[j] (R1, R2), t3[14−A] ∈ R5, P, P′}, which needs 14 − A > u, i.e. p2 ≥ 2.

Every other F1-cut label repeats R3 or R4. So Q = {G\*, β} together with two of {c1, λ5\*, c2, γ}. By RC, G\* = {T, t1[j] (R1, R2), t2[A−4], P′, t3 ∈ R5 ∩ q0}.

**c2 ∉ Q.**
- β and c2 need non-adjacent t1-arm vertices with their S_12-passages in R2. These lie on t1[u+p2−4..u−1], which has 4 − p2 vertices, so p2 = 1.
- Then A = 14 − u, and q3's t3-part ends at t3[14−A] = t3[u].
- That puts c2's cut vertex on the q3/q0 cut as well, so it carries two cuts. Contradiction.

**The remaining pairs.** β needs an arm vertex in t1[u+p2−4..u−1], so p2 ≤ 3. λ5\* needs t3 ∈ R5 ∩ q3 = t3[u+1..13−A], so p2 ≥ 3.
- **{c1, λ5\*}.** Here p2 = 3, and β's arm vertex is t1[u−1]. In R2 = Λ[5..7], b5, t1[u+4..u−2], this vertex is adjacent to c1's t1[u], against (E).
- **{c1, γ}.** In R1 = t1[u..u+4], b5, Λ[1..5], c1 sits at position 1, and G\* and γ sit among positions 2–5. Three pairwise non-adjacent Q-labels in five consecutive positions occupy 1, 3 and 5, giving two gaps of 2 that share a label. D2Q forbids this; its hypotheses hold because the interiors of P and P′ avoid the cuts t2[A], t2[A+10], t2[A−4] and t2[A+6].
- **{λ5\*, γ}.** Here p2 = 3, so A = 12 − u. λ5\*'s t3-vertex is t3[u+1], and γ's cut vertex is t3[14−A] = t3[u+2]. These are adjacent Q-labels, against (E).

## 6. Result

**WRITTEN:**
- Rules A1 and A2.
- Type A (0,2,0,0) is impossible for δ ∈ {4, 6, −4, −5, −6}. (R3) enters through D2Q at δ = 4 only.

**OPEN residual of L2 (k = 3):**
- type A (0,2,0,0) with δ = 5;
- type A (0,1,1,0).

L1 types 1–4 and 7–12 remain open. The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
