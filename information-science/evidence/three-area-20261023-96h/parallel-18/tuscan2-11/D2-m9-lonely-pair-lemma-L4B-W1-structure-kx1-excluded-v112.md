# Original Tuscan-2(11), entire m = 9 distance-two branch, part 1: the lonely-pair lemma, L4-B corner facts, the W1 stretch structure, and W1 with k_x = 1 excluded

Actual `/bin/date` before this body: **Mon Oct 26 16:18:09 PDT 2026**. InfoRecursiveMDS18-2.

**Status.** NEW exact WRITTEN CANDIDATE under parent direction v143 (SHA256 `43af3295b857ccd709c9661d006de759bf9f07ce8607f0b6028d226db2206ec7`). It is a bounded necessary branch of the original Tuscan-2 problem: every eligible array with support 9 in L1, L2 (k = 3) or L4-B W1, with all variables free. It is not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, program, enumeration tool, solver, replay, chosen row, chosen example or probe.

**Intake.** Intake binding `intake-binding-D2-entire-m9-L1-L2k3-L4BW1-v1.json` (SHA256 `82cbe1fb85d381d326838003ca77f723fee445e22f11726b860e6ff446947d54`). Every bound source was read whole before this derivation: v94, v95, v96, v97, v100, v104, v106, v107, v108, v109.

## 1. Lonely-pair lemma (all m = 9 families, uses (R3))

Fix an eligible array with m = 9.

**Definitions.**
- A **fully internal 2-cycle** (a b) of some K_x is a non-cut 2-vertex of label x with neighbour labels {a,b}.
- U_int is the set of their unordered pairs. By v108 (C1) these pairs are distinct, so |U_int| = N2_int.
- U_rest is the set of the other 55 − N2_int unordered pairs.
- **Lonely arcs** are:
  - the internal arc f(x) → p(x) of every boundary 2-cycle (a cut at a 2-vertex);
  - every internal arc of a long cycle (a non-cut branch corner).

  There are N2_bd + m − (11 − β − N2_bd) of them (v108 §4).

**Lemma LP.**
- (i) Every lonely arc lies on a U_rest pair.
- (ii) Both arcs of every U_int pair are distance-two events.
- (iii) The 2|U_rest| arcs of the U_rest pairs are exactly the lonely arcs together with the 11 arcs of M.

Hence, if d (respectively z) counts the U_rest pairs carrying two lonely arcs (respectively two M arcs),

    d − z = (#lonely − 11)/2 = (2·N2_bd + β − 13)/2.

**Proof.**
- (i) Suppose a lonely arc a → b at middle x lay on a U_int pair, i.e. on an internal 2-cycle (a b) of some K_y. If y = x, K_x would contain a → b both in that 2-cycle and in the lonely cycle. If y ≠ x, the event (a,b) occurs twice, against (R3).
- (ii) An internal 2-cycle gives both events at its middle.
- (iii) Every ordered pair is either a distance-two event or in M. The distance-two events are the 2·N2_int arcs of U_int pairs plus the lonely arcs. ∎

**Values (v108 §5).**
- L1, L2, L3: β = 1, so d − z = N2_bd − 6 ∈ {3, 4}.
- L4-B: β = 3 and N2_bd = 8, so d − z = 3.

**So in every remaining family at least three unordered pairs carry two lonely arcs at two different middles.** Each such pair is one of three kinds:
- (br,br): two corners a → b and b → a at branches of different labels;
- (bd,br): a boundary 2-cycle at x together with a corner p(x) → f(x), which makes x a D-hit (v109 §5);
- (bd,bd): two boundary 2-cycles x, x′ with p(x′) = f(x) and f(x′) = p(x).

## 2. L4-B: no (br,br) pair between b1 and b2

Use the v106 §1 notation and let u = 10 − t.

**Corners at b1 and b2.** The branch b1 is not a cut, so its three corners are internal. They form K_(v1) = (τ π1 κ1), where:
- τ is the label of b1's T-neighbour, so τ ∈ L(T_int) ∪ {v3};
- π1 is the label of b1's P-neighbour, so π1 ∈ L(P_int) ⊆ S ∖ {v2}, or π1 = v2 if d = 1;
- κ1 = L(Q[1]) ∈ S.

At b2 the corners form K_(v2) = (π′ η1 ζ1), where:
- π′ = L(P[d−1]) ∈ S, or π′ = v1 if d = 1;
- η1 = L(Y1[1]) ∈ S ∖ {v2};
- ζ1 = L(Y2[1]).

**Facts used.** S = X ∖ ({v1, v3} ∪ L(T_int)), so τ ∉ S.
- R_out holds P_int, b2 and Y1[1..e] at distinct positions, so η1 ≠ π1.
- R_xy holds P_int, b1, b2, Y2[1..a−d] (with a − d ≥ t ≥ 1) and Q[1..b] (with b ≥ 1) at distinct positions (v94 §8.2). So ζ1 ∉ {π1, κ1} and π′ ≠ κ1.

**Checking the three reversed arcs.** A b2-arc reversing a b1-arc would need one of:
- π1 → τ: impossible. The only b2-arcs with head τ would be η1 → ζ1 = τ with η1 = π1, or ζ1 → π′ = τ, but τ ∉ S ∪ {v1}.
- κ1 → π1: impossible. This needs η1 = π1, or ζ1 = π1, or ζ1 = κ1.
- τ → κ1: impossible. This needs a b2-tail equal to τ, so ζ1 = τ and then π′ = κ1.

For d = 1 the b1-arcs are τ → v2, v2 → κ1 and κ1 → τ. No b2-arc has v2 as head or tail. A b2-arc τ → κ1 would need ζ1 = τ and v1 = κ1 ∈ S, which is false.

So every (br,br) pair of L4-B involves b3. This holds for both W1 and W2.

## 3. L4-B W1: stretch structure

**The face.** In W1 the single H-face (90 arcs, rows 0..8, positions from ℓ3) is:
- T, then b1 at t;
- P, then b2 at A1 = t+d;
- Y1, then b3 at B1;
- Y2⁻, then b2 at A2;
- P⁻, then b1 at x;
- Q, then b3 at B2;
- Y1⁻, then b2 at A3;
- Y2, then b3 at B3;
- Q⁻, then b1 at 90−t, and T⁻ back to ℓ3.

Here t + d + q + y1 + y2 = 45.

**Rows and stretches.**
- Let k_x be the row of x. Row 0 = R_out and row 8 = R_in = Q[u..1], b1, T, ℓ3.
- Stretch 1 is (t, x); stretch 2 is (x, 90−t).
- A Y-vertex has one passage in each stretch. A Q-vertex has both passages in stretch 2.
- T and P carry no v (v106 §1).

**Two indicators.** Let ε = 1 if A2 lies in row k_x − 1, which happens exactly when a P-vertex is the cut at 10k_x. Let θ = 1 if row k_x takes its v3 from its stretch-2 part.

**Counts.** Counting, row by row, the rows that need each v gives:

    n_Y(v1) = k_x − 1,  n_Q(v1) = 4 − k_x;
    n_Y(v3) = k_x − 1 − θ,  n_Q(v3) = 3 − k_x + θ;
    n_Y(v2) = k_x − 1 − ε,  n_Q(v2) = 3 − n_Y(v2).

Also A3 ∉ row k_x when ε = 0, A3 ∉ row 8, and B2, B3 lie in rows k_x..7.

**Consequences.**
- k_x ∈ {1, 2, 3, 4}.
- θ = ε = 0 when k_x = 1.
- θ = 1 when k_x = 4.

This corrects an unpacketed earlier note that had k_x ≤ 3 by implicitly taking θ = 0.

## 4. W1 with k_x = 1 is impossible

**The v-vertices.** Here every v-2-vertex of H is on Q: three for v1, three for v2, two for v3.

**Where b3 sits in stretch 2.**
- Stretch 1 lies in rows 0–1, with B1, A2 and x in row 1.
- A stretch-2 row strictly inside the Y-part (B2..B3) would lack v1. So B2 ∈ row r and B3 ∈ row r+1.
- The Q⁻ rows r+2..7, and the Q rows 2..r−1, are pure Q-rows.

**Forced rows.**
- v1's forward passages fill rows 2..r and its backward passages fill rows r+1..7, so r = 4.
- v2's forward and backward counts must be equal, and row 8 needs a Q-v2. This forces A3 ∈ row 5.

**Q coordinates.** Put s = 20 − x. The forward rows on Q are 1: [1,s), 2: (s,s+10), 3: (s+10,s+20), 4: (s+20,q−1]. The backward rows are 8: [1,u), 7: (u,u+10), 6: (u+10,u+20), 5: (u+20,q−1]. The row-4 Q-v2 must return in row 6, 7 or 8, so s < u.

The v-vertices are therefore:
- v1 in Q(u,s+10) of type (2,7), Q(u+10,s+20) of type (3,6), and Q(u+20,q−1] of type (4,5);
- v2 in Q(s,u) of type (2,8), Q(s+10,u+10) of type (3,7), and Q(s+20,u+20) of type (4,6);
- v3 in Q(u,s+10) of type (2,7) and Q(u+10,s+20) of type (3,6).

**v1 and v2 force d = 1.** On Q the v1-regions and v2-regions are separated by the cut vertices Q[u], Q[s+10], Q[u+10], Q[s+20] and Q[u+20]. Q[1] ∈ [1,s) carries no v, and Y1, Y2 carry none. By v106 §2(a), v1 and v2 can be adjacent in H only if d = 1, so P_int = ∅.

**The stuck matching.** The Q[u+20]-label has cut rows {4,5,6}. Its remaining rows {0,1,2,3,7,8} must be matched by the types T (0,8), Q (1,8), (2,8), (2,7) and (3,7). Every Y-type meets row 4 or 5, and P is empty.
- Row 3 is forced to 7.
- Row 2 is then forced to 8.
- Rows 0 and 1 both need 8. Contradiction.

So **W1 with k_x = 1 is impossible.** This uses (R1)–(R2) only.

## 5. Result and open part

**WRITTEN:**
- Lemma LP (§1, uses (R3)): d ≥ 3 lonely–lonely pairs in every remaining m = 9 family.
- L4-B has no (br,br) pair between b1 and b2 (§2).
- The W1 stretch structure, with k_x ∈ {1,2,3,4} and indicators (θ, ε) (§3).
- W1 with k_x = 1 is impossible (§4).

**Open in the v143 branch:**
- L4-B W1 with k_x ∈ {2, 3, 4} and every (θ, ε);
- L2 with k = 3: four face types A, B, C, E up to the mirror, F = 2 in all six rotation orders. The tracing is recorded in the next packet;
- L1.

**Acceptance ceiling (v143).** Only if all three families are excluded does the statement "every eligible original Tuscan-2(11) array with support 9 is impossible" follow. Any m ≥ 10 consequence needs the full m ≤ 8 plus m = 9 joint gate. Every m in 10..110 remains unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
