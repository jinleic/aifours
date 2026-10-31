# Actual Tuscan11, m = 9, line L4-B: the reverse-pair adjacency lemma, and W2 option (4,2,3) excluded

Actual `/bin/date` before this body: **Mon Oct 26 14:59:15 PDT 2026**. InfoRecursiveMDS18-2.

**Status.** NEW exact WRITTEN CANDIDATE: not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO.

**Scope.** Tuscan-1-only support-ladder work on R6 (all m ≥ 9, no Tuscan-2 cap). This is a necessary-case exclusion, not a construction or a Tuscan-2 statement. It is a separate, ungated successor line, outside the v19–v49 and v150b freezes.

## 1. Setting

The setting is v94 §5.4 and §8.2 (SHA256 `1c5465c4f0a5835ecda93a2a9877d42f3b607d774f63e49be9f1228a951c396c`).

**The two components.**
- The reverse pair R consists of the rows x0 = v1, x1, …, x10 = v2 and their reverse. Its 10 edges are the pairs {x_i, x_{i+1}}.
- H is the 9-row component. Its branches are:
  - b1 (label v1): carries the tail T, of length t, to the leaf ℓ3 (label v3, the v3-cut), and the paths P (to b2) and Q (to b3);
  - b2 (label v2), with the paths P, Y1 and Y2;
  - b3 (label v3), with the paths Q, Y1 and Y2.
- No branch is a cut. Every H-row carries v1, v2 and v3 exactly once.

**Rotations.** By the row-reversal mirror, b1 has rotation (T, P, Q). By naming, b2 has rotation (P, Y1, Y2). b3 has rotation (Q, Y1, Y2) (W1, one face) or (Q, Y2, Y1) (W2, three faces).

**Arms.** Write u = 10 − t. By Lemma TC with b1 not a cut, d := |P| ≤ u − 1. Then:
- R_out = ℓ3, T, b1, P_int, b2, Y1[1..e], with e = u − d ≥ 1;
- R_in = Q[u..1], b1, T, ℓ3;
- S := L(Q[1..u]) = L(P_int) ∪ {v2} ∪ L(Y1[1..e]).

T_int and P_int carry none of v1, v2, v3.

## 2. Reverse-pair adjacency lemma (all of L4-B)

By F2, the 55 label pairs are the 45 H-edges together with the 10 R-edges. The R-edges form the Hamilton path from v1 to v2. Hence:
- (a) **v1 and v2 are adjacent in H.** They are the two ends of R, so they are not adjacent in R.
- (b) The H-neighbours of every label are distinct. v1 and v2 each miss exactly one label in H; every other label misses exactly two.

**Ways (a) can hold.** v1–v2 adjacency in H can only arise through:
- d = 1 (b1 adjacent to b2);
- a v2-2-vertex at Q[1];
- a v1-2-vertex at Y2[1];
- a v1-2-vertex adjacent to a v2-2-vertex.

The other neighbours of b1 and b2 are excluded, because T_int, P_int and Y1[1..e] carry none of v1, v2.

## 3. W2, option (4,2,3) is impossible

**Data** (face identities, as in checkpoint 148):
- r = (4,2,3), y1 = 25 − t, y2 = 5 + t, q + d = 15 − t;
- v1 on (Y1, Y2, Q) = (2,1,0); v2 = (2,0,1); v3 = (1,1,0).
- Face 2 has two rows, R_xy and Qr. Face 3 is the Y-cycle, with cuts f, f+10, f+20.

### 3.1 b3 in R_xy

Then R_xy runs through all of Y2 and b3 into Q, and Qr = Q[b..20−a] is a pure Q-row. Qr needs v1, but Q carries no v1. Contradiction.

### 3.2 b3 in Qr

The face-2 counts force:
- the Y2-v1 into Qr;
- the Y2-v3 into R_xy and the F3 row γ;
- the Y1-v2 vertices into the F3 rows α and β;
- b3 into α.

Put δ = t + d − f, which compares the F1 and F3 cuts on Y1.

**Order a − d < f, either sign of δ.** The Y2[f]-label has cut rows {Qr, γ, α}. Row B's partners are Qr (via Q) and α (via Y1), or else β, which strands row A. Contradiction.

**Order f < a − d with δ < 0.** The Y2[a−d]-label has cut rows {R_xy, Qr, α}. Row B has no partner. Contradiction.

**Order f < a − d with δ > 0.**
- The matchings give consistent segment equations: d = 2, f = t − 2, e = 8 − t, q = 13 − t, with t ∈ {4, 5}. This leaves six explicit skeletons.
- In every one of them:
  - d = 2, so P_int is a single vertex;
  - the v2-2-vertex on Q lies in Q(b,u), so it is not Q[1];
  - Y2[1] lies in Y2[1,f), whose users are v3 and possibly the Y1[e+10]-label, so it is not a v1-vertex;
  - every v1-segment of Y1 is separated from every v2-segment by a cut (Y1[10−f], Y1[e+10] or Y1[20−f]).
- So v1 and v2 are not adjacent in H, which contradicts §2(a).

## 4. Result

- **WRITTEN:** the reverse-pair adjacency lemma (§2) holds for L4-B.
- **WRITTEN:** W2 option (4,2,3) is impossible.

**Still open in L4-B:** W2 options (4,3,2) and (3,3,3), and W1. Also open at m = 9: L1 and L2 with k = 3.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
