# Original Tuscan-2(11), entire m = 9 distance-two branch, part 35: Lemma Λ2 for type B (p3 ≤ 4, p1 ≤ 3); type B (0,1,1,0) closed; addendum for ℓ1 ≤ 4

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-typeB-0110-setup-K-le-19-closed-v146.md` (SHA256 `9c3083006e5b8535f7a95e5ea5404e6903c3b8b4b987edfd2109f10522afedb2`).

Imports:
- notation of v143 §1 and v146 §1;
- DP-1 and DP-2, v114 §2.

This uses (E), (C), (X) and RC only. It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Lemma Λ2 (type B, both b = 3 cells)

**Statement.** In type B (0,2,0,0) and type B (0,1,1,0), **p3 ≤ 4 and p1 ≤ 3**.

**Set-up for the proof.**
- λ2\* := L(Λ[p4]) is the label of an F1 cut, at position 60 in (0,2,0,0) and 50 in (0,1,1,0). It is neither v, c1 nor λ1\*.
- Λ[p4]'s other F1-passage (its S_Λ1-passage) sits at position 10 + p1 + p4 = 15 + p3. That is in R1 if p3 < 5, in R2 if p3 > 5, and p3 = 5 is excluded.
- R0 = ℓ, T_int, b4, t1[1..u] and R1 = t1[u..ℓ1−1], b5, Λ[1..10−p1] contain no group-2 vertex.
- An F1-cut label has exactly two group-1 vertices (2·n1 + n2 = 7 and n2 = 3).

**Proof.**
- **λ2\* ≠ w.** An F1-cut w would be {b4, Λ[p4], two group-2 W's}. Its only possible R1-vertex is Λ[p4], so p3 < 5. Its R2-vertex would then have to be b4 or a group-2 W, which forces ℓ1 ≤ 4 and hence p1 ≤ 2. So the statement holds in this case as well.
- **p3 > 5 is impossible.** For λ2\* ≠ w, the two group-1 vertices are Λ[p4] and one more vertex, g. If p3 > 5, Λ[p4] covers R2 but neither R0 nor R1, so g must cover both R0 and R1. Only the cut vertex t1[u] does that, and it belongs to c1.
- **p1 ≤ 3.** So p3 < 5, and Λ[p4] covers R1, leaving g to cover R0 (as T or as a t1-arm vertex). R2 must then be covered as follows:
  - If ℓ1 ≥ 5, R2 = Λ, b5, t1 contains no group-2 vertex. So g is a t1-arm vertex t1[j] whose S_12-passage lies in R2, i.e. ℓ1 − 5 < j < u. This forces p1 ≤ 3.
  - If ℓ1 ≤ 4, then p1 = ℓ1 − u ≤ 2. ∎

## 2. Type B (0,1,1,0) with K ≥ 20 is impossible

**K = 20.** Here b4 is on the r1/r2 cut, so r1 = t2[10..1], b4 and r2 = b4, t3[1..10].
- Exchanging R6 with r2 and with r0 gives blocks of sizes u and 10 − u. DP-1 then gives u ∈ {4, 5, 6}, so ℓ1 ≥ 5.
- Exchanging R3 = t1[ℓ1−5..1], b4, t2[1..A′] with r1 gives L(t1[1..ℓ1−5]) = L(t2[A′+1..10]). DP-1 then gives ℓ1 ∈ {5, 9}.
  - ℓ1 = 5 puts t2[10] on both an F1 and an F2 cut.
  - ℓ1 = 9 needs p1 = 3 and u = 6. Then K = x + ℓ2 = x + 6 + p3 = 20 gives p3 = 14 − x ≥ 5, against Lemma Λ2.

**K ≥ 21.** Here r1 = t2[K−20..K−10] is pure. Put e := A′ − K + 20 and d3 := 30 − K − u. Exchanging r1 with R4 and R3 (or the pure R3 when ℓ1 ≤ 4), and R6 with r0 and r2, gives four blocks:
- t2[K−20..A′−1] with R4's tail (e vertices);
- t2[A′+1..K−10] with R3's head (10 − e vertices);
- t3[u..29−K] with r0's tail (d3 vertices);
- t3[31−K..u+10] with r2's head (10 − d3 vertices).

DP-1 gives e, d3 ∈ {4, 5, 6}. Counting the tails gives e = 20 − x − p3 and d3 = 15 − x + p1 − p3, so d3 = e + p1 − 5.
- With p1 ≤ 3 (Lemma Λ2), d3 ≥ 4 forces e = 6, p1 = 3 and d3 = 4.
- Then x + p3 = 14, so p3 ≥ 5, against Lemma Λ2.

**Hence type B (0,1,1,0) is closed.** K ≤ 19 is v146, and K ≥ 20 is above.

## 3. Addendum to v143, v144 and v146 (the case ℓ1 ≤ 4)

When ℓ1 ≤ 4, R2 contains b4 and t2[1..4−ℓ1], and R3 = t2[A′−10..A′] is a pure t2-row. Those three packets wrote their row tables for ℓ1 ≥ 5. Their conclusions stand for ℓ1 ≤ 4 too:

| Packet | Case | Why it still dies |
|---|---|---|
| v143 | δ = 4 | Needs p3 ≥ 6, against Lemma Λ2. Directly: H\* has only two group-2 vertices, both outside the pure row R3. |
| v144 | δ = 6, 5 | Need p3 ≥ 7 and p3 ≥ 6, against Lemma Λ2. The arguments given there do not use R2 or R3. |
| v146 | δ3 = 4 | Needs p1 ≥ 7, against Lemma Λ2. |
| v146 | δ3 = −4 | Has u ≥ 5, hence ℓ1 ≥ 6. |

**v144, δ = −4 with ℓ1 ≤ 4: a new DP-2 chain.** Exchanging the pure R3 with r2 (shared t2[A′−10..A′−4]) gives L(t2[A′−3..A′]) = L(r2's last four vertices). Put:
- P1′ = t2[A′−3..A′] and P1 = r2's last four vertices;
- P2 = t2[A′−4..A′−1] = (t2[A′−4], P1′ minus its last vertex);
- P2′ = t2[A′+7..A′+10], with L(P2′) = L(P2) from v144's block.

These paths are pairwise disjoint, so DP-2 with m = 4 gives a contradiction.

**Hence every type B conclusion of v143–v146 holds for all ℓ1. Type B (0,2,0,0) and type B (0,1,1,0) are both closed.**

## 4. Result

**WRITTEN:** Lemma Λ2. Type B (0,1,1,0) is impossible, and the ℓ1 ≤ 4 addendum holds. With v123 (the b = 2 cells), v143–v146 and the above, **every type B cell of L2 (k = 3) is closed.**

Together with v142 (type C) and v141 (type E), **the only open cells of L2 (k = 3) are type A (0,2,0,0) and type A (0,1,1,0).**

L1 types 1–4 and 7–12 remain open. The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
