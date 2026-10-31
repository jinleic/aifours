# Original Tuscan-2(11), entire m = 9 distance-two branch, part 9: the K4-saturation lemma, and L2 type A cell (1,0,0,1) excluded

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-branch-consolidated-status-and-exact-gap-v119.md` (SHA256 `866b9f9a8eb99bc504c6eac64a9007f3053bb5a5b1742a886c194f14e12b7334`). Notation is that of v114–v116.

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. It uses (R1)–(R2) only.

## 1. K4-saturation lemma (T1)

**Lemma KS.** Suppose:
- P and P′ are vertex-disjoint paths of four vertices with L(P) = L(P′) = Q, so |Q| = 4;
- R is a path of four vertices, edge-disjoint from P and P′, with |L(R) ∩ Q| ≥ 3.

This is impossible.

*Proof.*
- By exactness (v114 (E)), the six edges of P and P′ carry six distinct pairs of Q. Those are all the pairs, so Q is *saturated*.
- Any edge of R joining two labels of Q would repeat one of these pairs. Hence every edge of R meets the at most one label of L(R) ∖ Q.
- R has three edges, so that label would need three neighbours on a path, which allows at most two. ∎

## 2. Type A, cell (1,0,0,1), is impossible

**The cell.** This is the λ = 16 case of v115 §3 and v116 §4:
- b = 3 and a = 8;
- V1 lies on t1 and V2 = Λ[k2];
- y0 = 5, y1 = 1 and ρΛ = 6;
- the F2 cuts sit at ℓ3 + 5, ℓ3 + 15 and ℓ3 + 25 (mod 30).

**The four rows.**
- F1 row 2 = [20,30] = t1[u+10..u+14], b5, Λ[1..5].
- F1 row 3 = [30,40] = Λ[5..15].
- F1 row 4 = [40,50] = Λ[15], b5, t1[u+14..u+6].
- F2 row R_A = [ℓ3+5, ℓ3+15] = Λ[11..1]. This holds because Λ[k] sits at ℓ3 + 16 − k in F2.

**Exchanges.**
- Rows 3 and R_A share Λ[5..11]. So **L(Λ[1..4]) = L(Λ[12..15]) =: Q**, a pair of vertex-disjoint 4-paths. Hence Q is saturated, and L(Λ[15]) ∈ Q.
- Rows 2 and 4 share t1[u+10..u+14] and b5. So L(Λ[1..5]) = {L(Λ[15])} ∪ L(t1[u+6..u+9]).
- Λ[5] and Λ[12..15] all lie in row 3, so L(Λ[5]) ∉ Q. Row 4 contains Λ[15] and t1[u+6..u+9], so L(Λ[15]) ∉ L(t1[u+6..u+9]).

Together these give:

    L(t1[u+6..u+9]) = (Q ∖ {L(Λ[15])}) ∪ {L(Λ[5])}.

So the 4-path R = t1[u+6..u+9] has three labels in Q. It is edge-disjoint from the Λ-paths. This contradicts Lemma KS.

Every step holds for every u and every p3. **Cell (1,0,0,1) of type A is impossible.** Only type A b = 3 with λ = 14, u ≤ 6 and V2 on t2 remains of the b = 3 part.

## 3. Status

**WRITTEN:**
- Lemma KS;
- L2 type A cell (1,0,0,1) is impossible.

**The v119 gap list shrinks by this cell:**
- type A keeps (1,1,0,0) with λ = 14 and u ≤ 6, plus the four n1 = 0 cells (0,2,0,0), (0,1,1,0), (0,1,0,1), (0,0,1,1);
- types B, C and E are unchanged;
- L1 types 1–4 and 7–12 are unchanged.

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
