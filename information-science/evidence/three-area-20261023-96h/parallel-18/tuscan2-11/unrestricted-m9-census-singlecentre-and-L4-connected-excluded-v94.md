# Actual Tuscan11, support m = 9: complete census of long-cycle placements

Single-centre placements and connected three-centre placements are excluded; L3 and L4-B are reduced.

Actual `/bin/date` before this body: **Mon Oct 26 13:28:12 PDT 2026**. InfoRecursiveMDS18-2.

**Status.** NEW exact WRITTEN CANDIDATE: not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO.

**Scope.**
- This is Tuscan-1-only support-ladder work on R6, which is all m ≥ 9 with no Tuscan-2 cap (see `scope-qualification-R6-no-T2-support-cap-addendum-v1.json`).
- It is a necessary-case census, not a construction or a Tuscan-2 nonexistence result.
- It is a separate, ungated successor line, outside the v19–v49 freeze and the v150b freeze.

## 1. Imports

- **v1** (SHA256 `e54953336e35bd7a535d147ca6a564f9db30ddca966f1ad31dc58485167d8275`), Lemma 1: K_x is a permutation, and its only possible off-x fixed point is the boundary turn p(x) = f(x). **So each label carries at most one leaf.**
- **v12** (SHA256 `c2a9283d09b06781e0f1b76a42a0dcb700913dc87bddf69aabae78ff32caf6b2`):
  - the split graph and the component identity (2);
  - no proper component has all degrees even;
  - the rule giving r_H from O_H;
  - the cycle rank (4) and face count (5);
  - §3: every face of a branched component has at least two branch visits; reverse partners form an isolated ten-edge path;
  - §4.2: a loop at a degree-3 vertex is monofacial, hence excluded.
- **v79** (SHA256 `477457c87c04b1eed9ee71a614c454d379d2fbfc4884b6e8d6fec89602f7be42`):
  - §2: every label has exactly one cut, and a leaf is a row end, so it is its label's cut;
  - §4: the third-corner argument.
- The exchange identity: every row carries all 11 labels once. Also |E| = 55 (one edge per unordered pair).

## 2. Local cycle data at m = 9

At a centre x, the off-x cycles of K_x have total length 10. At most one of them has length 1 (Lemma 1), and the number of odd cycles is even. Hence:

> x carries a leaf iff it carries an odd number of odd long cycles, and then exactly one leaf.

The long-cycle partitions of 9 are 9, 6+3, 5+4 and 3+3+3. Every placement is one of the following.

| Name | Placement | Cycle data at each centre | β |
|---|---|---|---|
| (S) | all long cycles at one centre v: 9, 6+3, 5+4 or 3+3+3 | v plus one leaf; all other centres have 2-cycles only | 1 |
| (L1) | 6 at v, 3 at w | v = 6+2+2; w = 3+1+2+2+2 | 1 (leaf ℓ_w) |
| (L2) | 5 at v, 4 at w | v = 5+1+2+2; w = 4+2+2+2 | 1 (leaf ℓ_v) |
| (L3) | 3+3 at v, 3 at w | v = 3+3+2+2; w = 3+1+2+2+2 | 1 (leaf ℓ_w) |
| (L4) | 3 at each of v1, v2, v3 | v_i = 3+1+2+2+2 | 3 (leaves ℓ_i) |

## 3. Leaf-tail lemma

Let ℓ be a leaf with label λ; it is the λ-cut. Follow the path of degree-2 vertices from ℓ. Then exactly one of the following holds.
- **(a)** The path reaches a branch b at distance t ≤ 9, and label(b) ≠ λ.
- **(b)** The path reaches another leaf at distance exactly 10, and the path is an isolated reverse pair (a 2-row component).

**Proof.** The row R_in ends at ℓ and the row R_out starts at ℓ. Both run along the path until its first vertex of degree ≠ 2.

*A branch b within distance 9.* Both rows contain ℓ and b, so label(b) ≠ λ.

*Distance 10 reached first.* Let u be the vertex at distance 10. Then R_in starts at u and R_out ends at u. So u is a cut whose boundary turn has p = f equal to the vertex at distance 9. That is an off-centre fixed point, so u is a leaf, not a branch (the edge from the vertex at distance 9 to u lies in exactly one split vertex). The component is then the 10-edge path.

*Another leaf at distance L < 10.* Its face would have length 2L < 20, but every face is a multiple of 10 with at least two rows. Impossible. ∎

## 4. Single-centre placements (S) are impossible

The only leaf has label v, and every branch has label v. By §3 its tail can reach neither a branch of another label nor another leaf. **(S) is excluded for 9, 6+3, 5+4 and 3+3+3.**

## 5. Shapes of L1–L4

**Tools.**
- **(i)** Every component has an even number of odd-degree vertices, and no proper component has O_H empty.
- **(ii)** If |O_H| = 2 then r_H ∈ {2, 9}. A 2-row component has every label degree ≤ 2, so it has no branch; if it contains a leaf, it is a reverse pair.
- **(iii)** There are no loops at degree-3 vertices. At a vertex of higher degree, the two ends of a loop are not adjacent in the rotation; otherwise the face along the loop would have exactly one branch visit.
- **(iv)** The face count F follows from (4)–(5).

### 5.1 L1 (6 at v, 3 at w)

- The tail of ℓ_w cannot end at b3, which has label w, and there is no second leaf. So it ends at b6, at distance t ≤ 9.
- The component of b3 contains a second odd vertex, which can only be ℓ_w. Every other component is all-even. **Hence the array is connected.**
- After removing the tail, b6 has degree 5 and b3 has degree 3. There are k threads between them, with k odd. k = 1 would put a loop at b3, which (iii) excludes.
- So k = 3: three threads b6–b3, one loop at b6 whose ends are not rotation-adjacent, and the tail at b6.
- Cycle rank 3, so F ∈ {2, 4}.

### 5.2 L2 (5 at v, 4 at w)

- The tail of ℓ_v ends at b4, at distance t ≤ 9; b5 has label v.
- The array is connected: b5 pairs with ℓ_v, and b4 joins through the tail.
- After removing the tail, b4 has degree 3 and b5 has degree 5. Either:
  - **k = 3:** theta(b4, b5) plus one loop at b5; or
  - **k = 1:** b4 carries one loop and the thread, and b5 carries the thread and two loops. The loop ends are never rotation-adjacent, so b4's rotation alternates (T, L, t, L).
- F ∈ {2, 4}.

### 5.3 L3 (3+3 at v, 3 at w)

The tail of ℓ_w ends at a v-branch b′; the other v-branch is b″.

**Connectivity.**
- A component holding b′ and b″ but not b_w has O_H empty: excluded.
- A component holding b_w and ℓ_w but no v-branch cannot hold ℓ_w's tail end.
- Splitting {b′, b_w} from {b″, ℓ_w}, or {b′, ℓ_w} from {b″, b_w}, gives |O_H| = 2 on both sides. So the row counts are {2, 9}. But each side has a branch, so neither side can be the 2-row component, by (ii).
- **Hence the array is connected.**

**Core.** By (iii) the core is loopless. A loop at b′ would also cut b′ and its tail off from the rest. The degree equations (b′: 2 after the tail; b″, b_w: 3) give a unique solution:
- path P from b′ to b″;
- path Q from b′ to b_w;
- two threads Y1, Y2 from b″ to b_w.

F ∈ {1, 3}.

### 5.4 L4 (3 at v1, v2, v3)

Labels outside {v1, v2, v3} have only degree-2 vertices. So O_H ⊆ {v1, v2, v3} and |O_H| ∈ {0, 2} for every component.

**No reverse pair.**
- Every component contains a branch.
- A proper component has |O_H| = 2, hence r_H ∈ {2, 9}, and r_H = 2 is branch-free. So every proper component has 9 rows, and the remaining 2 rows cannot form a component. **The array is connected.**
- Cycle rank (9 − 3 − 6)/2 + 1 = 1. Let t_j be the number of tails ending at b_j. Then Σ t_j = 3, and t_j ≤ 2 because ℓ_j cannot reach b_j.
- **C1:** every t_j = 1. One cycle passes through b1, b2, b3, each with one pendant tail. The tail at b_j comes from ℓ_{π(j)}, where π is a 3-cycle.
- **C2:** some t_k = 2.

**L4-B, a reverse pair.** There is at most one, since there are only three leaves. Name it ℓ1–ℓ2.
- The other rows form a single 9-row component H containing b1, b2, b3 and ℓ3, with O_H = {v1, v2} and C_H = X ∖ {v1, v2}.
- The tail of ℓ3 ends at b1 or b2; by the v1 ↔ v2 symmetry, b1.
- As in 5.3, the loopless degree solution is unique:
  - path P from b1 to b2;
  - path Q from b1 to b3;
  - threads Y1, Y2 from b2 to b3.
- F_H ∈ {1, 3}. The cuts of v1 and v2 are ℓ1 and ℓ2, and the cut of v3 is ℓ3. **So no branch of H is a cut.**

## 6. Two lemmas at a degree-3 tail branch

**Setting.**
- A leaf ℓ (the λ-cut) has its tail T, of length t ≤ 9, ending at a degree-3 branch b with label μ ≠ λ. Let σ be the rotation at b.
- R_out = ℓ, T, b, A+ leaves b along σ(T).
- R_in = A−, b, T, ℓ arrives along σ^{-1}(T) = σ²(T).
- The arms A± have 10 − t vertices each. By the exchange identity, L(A+) = L(A−) = S := X ∖ L(T ∪ {b}), where T includes ℓ.
- An arm **stays inside** if all its vertices are interior vertices of the path it starts on.
- An arm can never contain a vertex labelled λ or μ.

**Lemma TC (third corner).** Suppose both arms stay inside. Then the passage of b through its corner (σ(T) → σ²(T)) is a row boundary, so b is the μ-cut.

*Proof (v79 §4).* Suppose the passage is interior to a row R_xy, with a ≥ 1 vertices on the σ(T) side and b ≥ 1 on the other, a + b = 10.
- Its first min(a, 10−t) and min(b, 10−t) vertices lie in A+ and A−. So their labels are disjoint subsets of S, and min(a, 10−t) + min(b, 10−t) ≤ 10 − t.
- But a + b = 10 with a, b ≥ 1 forces the left side to exceed 10 − t. This holds whatever lies beyond the far ends. ∎

**Lemma 2T (two tails).** No degree-3 branch carries two tails.

*Proof.* Let b_k carry tails T_i and T_j (to leaves ℓ_i, ℓ_j of lengths t_i, t_j ≤ 9) and a third half-edge e. Rename so that σ(T_i) = T_j, σ(T_j) = e and σ(e) = T_i.

1. **The tail-to-tail row.** The face walk runs ℓ_i → b_k → ℓ_j between two cuts. Cuts lie exactly 10 apart along a face and t_i + t_j ≤ 18, so t_i + t_j = 10. Hence R0 = ℓ_i, T_i, b_k, T_j, ℓ_j is a row.
2. **The next two rows.**
   - The next row starts at ℓ_j: R1 = ℓ_j, T_j, b_k, then the first t_i walk vertices along e.
   - The row ending at ℓ_i is R_last = the last t_j walk vertices before b_k along e, then b_k, T_i, ℓ_i.
   - Both R1 and R_last contain e[1], the vertex adjacent to b_k on e (b_j itself if e has no interior).
3. **Exchange.**
   - R0 versus R1 (sharing ℓ_j, T_j, b_k) gives label(e[1]) ∈ L(T_i ∪ ℓ_i).
   - R0 versus R_last (sharing ℓ_i, T_i, b_k) gives label(e[1]) ∈ L(T_j ∪ ℓ_j).

These two label sets are disjoint inside R0. ∎

## 7. L4 connected is impossible

**C2** is excluded by Lemma 2T.

**C1.**
- No b_j is a cut, since v_j's cut is ℓ_j.
- At b_j the tail comes from ℓ_{π(j)}. Its arm toward b_{π(j)} (label λ = v_{π(j)}) stays inside its path.
- By Lemma TC the other arm must reach the third branch b_{π^{-1}(j)}. So the cycle path from b_j to b_{π^{-1}(j)} has length ≤ 10 − t_{π(j)} edges.
- As j runs over 1, 2, 3 these are the three cycle paths, once each. So the cycle length satisfies c ≤ 30 − (t1 + t2 + t3).
- But the graph is the cycle plus the three tails, with 55 edges, so c = 55 − (t1 + t2 + t3).

Contradiction. **L4 connected is impossible; L4 = L4-B.**

## 8. Reductions of L3 and L4-B

### 8.1 L3

At b′ the arms cannot reach b″ (label v = μ) or b_w (label w = λ), so both stay inside. By Lemma TC, **b′ is the v-cut, at its third corner** (h+ → h−), where h+ = σ(T) and h− = σ²(T).

At that cut:
- R_end = h+[10..1], b′ and R_start = b′, h−[1..10]. The walk vertices past a far branch are allowed only where the labels permit.
- Since b″ has label v, **|P_int| ≥ 10**.
- Exchange R_out with R_end, and R_in with R_start:

      L(h+[11−t..10]) = L(h−[11−t..10]) = L(T ∪ ℓ_w)  (each contains w).

### 8.2 L4-B

- b1 is not a cut. Its arm toward b3 (label v3 = λ) stays inside Q.
- So, by Lemma TC, the arm along P passes b2: **|P| ≤ 10 − t**, where t is the length of ℓ3's tail.
- Re-running the third-corner count with d = |P|: R_xy has b ≤ 10 − t − d vertices on the Q side and a ≥ t + d on the P side. **So R_xy passes b2 and has at least t further vertices beyond it, entering one of Y1, Y2.**

## 9. Result

At m = 9 (WRITTEN, Tuscan-1 necessary cases):

| Placement | Status |
|---|---|
| (S): 9; 6+3, 5+4, 3+3+3 at one centre | impossible |
| L4 connected (C1, C2) | impossible |
| L1 | open (k = 3 shape) |
| L2 | open (k = 1 and k = 3 shapes) |
| L3 | open, reduced: b′ is the v-cut at its third corner, \|P_int\| ≥ 10, and the two label identities of §8.1 hold |
| L4-B | open, reduced: \|P\| ≤ 10 − t, and R_xy passes b2 |

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
