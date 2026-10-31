# Original Tuscan-2(11), entire m = 9 distance-two branch, part 31: type B (0,2,0,0) — set-up, the shift screen, and δ = 4 closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-typeC-0200-closed-typeC-closed-v142.md` (SHA256 `57be8ae451f595247f9516f1a89997665820b1dea859babd20bfd6fed9548894`).

Imports:
- type B formulas, v116 §2 and v123 §1;
- RC, v134 §1;
- D2Q, v125 §1, which uses (R3).

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Set-up

**Parameters.**
- n2 = 2, so a = 8 and b = 3.
- ℓ1 = p1 + u and λ = 15 − p1.
- ℓ2 = 25 + p3 − p1 − u = A′ + 10 + p3, where A′ := 15 − ℓ1.
- ℓ3 = 5 − p3 + p1 + u, and p4 = p3 + 5 − p1 ∈ [1, 9].

**F1 rows** (b5 at 10+p1, 25, 50+p3 and 60+p4):

| Row | Vertices |
|---|---|
| R0 | ℓ, T_int, b4, t1[1..u] |
| R1 | t1[u..ℓ1−1], b5, Λ[1..10−p1] |
| R2 | Λ[10−p1..14−p1], b5, t1[ℓ1−1..ℓ1−5] |
| R3 | t1[ℓ1−5..1], b4, t2[1..A′] |
| R4 | t2[A′..A′+10] |
| R5 | t2[A′+10..A′+9+p3], b5, Λ[14−p1..p4] |
| R6 | Λ[p4..1], b5, t3[ℓ3−1..u] |
| R7 | t3[u..1], b4, T_int, ℓ |

The F1 cuts carry these labels:
- v at ℓ;
- c1 at t1[u];
- λ1\* at Λ[10−p1];
- τ3 at t1[ℓ1−5];
- α at t2[A′];
- β at t2[A′+10];
- λ2\* at Λ[p4];
- c2 at t3[u].

**F2 = S_23** (b5 at offset x). Put G := ℓ2 + x − 20 and H := G + 10.

| Row | Vertices |
|---|---|
| r0 | t3[ℓ3−x..ℓ3−1], b5, t2[ℓ2−1..H] |
| r1 | t2[H..G] (pure) |
| r2 | t2[G..1], b4, t3[1..ℓ3−x] |

The F2 cuts carry γ0 at t3[ℓ3−x], H\* at t2[H] and G\* at t2[G].

**Forbidden coincidences.**
- p1 ≠ 5: otherwise t1[u] = t1[ℓ1−5] would carry two cuts.
- p3 ≠ 5: otherwise p4 = 10 − p1, and Λ[p4] would carry two cuts.
- ℓ3 − x ≠ u: otherwise t3[u] would carry an F1 and an F2 cut.

**Anatomy.**
- T, t1 and Λ are *group 1*: two F1-passages, no F2-passage.
- t2 and t3 are *group 2*: one passage in each face.
- An F1-cut label has three group-2 vertices, one in each F2-row and none on an F2-cut, plus two group-1 vertices.
- An F2-cut label has two group-2 vertices, one of them on its F2-cut, plus three group-1 vertices.
- V_a ∈ t2[1..min(A′,G)−1], and V_b lies on t2 strictly inside R4 ∩ r1.

**The shift.** δ := G − A′ = p3 + x − 10. R4 and r1 are pure t2-rows of opposite direction. By DP-1 (v114 §2, same proofs), δ ∉ {0, ±1, ±2, ±3}. For |δ| ∈ {7, 8}, exchanging R4 with r2 or with r0 gives complementary 3- or 2-blocks, which DP-1 also forbids.

**Hence δ ∈ {±4, ±5, ±6}.**

## 2. δ = 4 is impossible

**The block.** Exchanging R4 with r1 gives the saturated block

    Q = L(P) = L(P′),   P = t2[A′..A′+3],   P′ = t2[A′+11..A′+14].

- t2[A′] is α's F1 cut, and t2[A′+14] = t2[H] is H\*'s F2 cut.
- The interiors of P and P′ are not on cuts, so D2Q applies.
- P′ ⊆ t2 forces p3 ≥ 5, hence p3 ≥ 6.

**Who can be in Q.**
- **v ∉ Q:** V_a < A′ and V_b < A′+11.
- **w ∉ Q:** a W on P and b4 would both lie in r2.
- **G\*, γ0, β, λ2\* ∉ Q:** the first two have too few group-2 vertices. β's own vertex t2[A′+10] lies in r1, as does P′. λ2\*'s cut covers R5, as does P′.

So every Q-label other than H\* is F1-cut. Its P- and P′-vertices fill R4/r2 and R5/r1, and its third group-2 vertex is a t3-vertex in r0 that is not on γ0's cut.

**RC.**
- **H\* (F2-cut).** Only T reaches R7, so H\* ∋ T. Covering R1, R2, R3 and R6 then forces:
  - a t1-vertex t1[k] with u < k < ℓ1 − 5 (rows R1, R3);
  - a Λ-vertex Λ[m] with 10 − p1 < m < p4 (rows R2, R6).
  
  This needs **p1 ≥ 7** and p4 ≥ 12 − p1, i.e. **p3 ≥ 7**.
- **Three F1-cut Q-labels** (α and two others) carry t3-vertices strictly inside r0's t3-part, which has x − 1 = 13 − p3 vertices. D2Q gives 13 − p3 ≥ 6, so **p3 ≤ 7**.

Hence **p3 = 7**, and Λ[m] is forced to Λ[11−p1], the second vertex of R2.

**Consequences in R2** = Λ[10−p1..14−p1], b5, t1[ℓ1−1..ℓ1−5]:
- c1 would need a Λ-vertex in the same range (rows R2 and R6). Its only candidate is Λ[11−p1], which is H\*'s. So c1 ∉ Q.
- λ1\* sits at Λ[10−p1], adjacent to H\*. So λ1\* ∉ Q.

So Q = {α, H\*, c2, τ3}, where by RC:
- α = {T, t1[k_α] with k_α ∈ [ℓ1−4, ℓ1−1], t3 ∈ R6, P, P′};
- c2 = {t3[u], a t1-arm vertex, t1[k′] with k′ ∈ [ℓ1−4, ℓ1−1], P, P′};
- τ3 = {T, t1[ℓ1−5], t3 ∈ R6, P, P′}.

**R1 = t1[u..ℓ1−1], b5, Λ[1..10−p1].** Its positions p1−4, …, p1 hold τ3 (at p1 − 4), α and c2. These are three pairwise non-adjacent Q-labels in five consecutive positions, so they sit at p1−4, p1−2 and p1. Both gaps then have length 2, so the middle label would lie in two special pairs (D2Q). Contradiction.

## 3. Result

**WRITTEN, uses (R3) through D2Q:** in type B (0,2,0,0), δ ∈ {±4, ±5, ±6}, and **δ = 4 is impossible**.

**OPEN residual:**
- type B (0,2,0,0) with δ ∈ {5, 6, −4, −5, −6};
- type B (0,1,1,0);
- type A (0,2,0,0) and (0,1,1,0).

L1 types 1–4 and 7–12 remain open. The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
