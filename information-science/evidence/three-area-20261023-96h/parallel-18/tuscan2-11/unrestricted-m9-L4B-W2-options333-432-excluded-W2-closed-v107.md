# Actual Tuscan11, m = 9, line L4-B: W2 options (3,3,3) and (4,3,2) excluded, which closes W2

Actual `/bin/date` before this body: **Mon Oct 26 15:07:54 PDT 2026**. InfoRecursiveMDS18-2.

**Status.** NEW exact WRITTEN CANDIDATE: not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO.

**Scope.** Tuscan-1-only support-ladder work on R6 (all m ≥ 9, no Tuscan-2 cap). This is a necessary-case exclusion, not a construction or a Tuscan-2 statement. It is a separate, ungated successor line, outside the v19–v49 and v150b freezes.

## 1. Setting

The setting, notation and the reverse-pair adjacency lemma (§2(a),(b)) are those of v106 (SHA256 `2247eec6ea726afcda6ee3984b97005d1dc16ad9a2a20b2b51b2784b3eae57c3`).

W2 has three faces:
- **F1** = T, P, Y1, Q⁻, T⁻;
- **F2** = Q, Y2⁻, P⁻;
- **F3** = Y2, Y1⁻.

Each H-row carries v1, v2 and v3 once. Only v3 has a cut in H (ℓ3, in F1).

**Cut rows and matchings.** For each non-special label c, the cut vertex lies in three rows. The other four vertices of c are 2-vertices, and their row pairs perfectly match the remaining six H-rows. "Stuck" means some remaining row has no available partner type.

**Fixed positions.**
- F1 is read from ℓ3. It has O = R_out, then the middle rows, then I = R_in.
- F2 is read from b1 along Q, with Q[j] at position j. Its rows are X = R_xy = [30−a, 30] ∪ [0, b], F2b = [b, b+10] and F2c = [b+10, b+20]. Here a + b = 10, a ≥ t + d, b ≤ e and Y2[k] lies at 10·r2 − d − k.
- F3 is read from b2 along Y2, with Y2[k] at k, b3 at y2 and Y1[k] at 10·r3 − k.
- The F3 cuts are f + 10i. Row γ contains b2.

## 2. Option (3,3,3)

**Data.**
- y1 = 15 − t, y2 = 15 + t, q = 15 − t − d = e + 5.
- v1 on (Y1, Y2, Q) = (1,2,0); v2 = (1,1,1); v3 = (0,2,0).

**F1.**
- O = ℓ3, T, b1, P, b2, Y1[1..e].
- M = Y1[e..14−t], b3, Q[q−1..u]. Here b3 is at 15 + d and d ≤ 4 (from q ≥ u+1).
- I = Q[u..1], b1, T, ℓ3.
- Q carries no v1, so M's v1 is Y1-v1. I's v2 is the Q-v2 at index j < u, so M's v2 is Y1-v2.

**F2.**
- If q > b + 10, then F2b = Q[b..b+10] is a pure Q-row and lacks v1. So q < b + 10 and b3 ∈ F2b.
- F2c = Y2[a−d..a−d+10] is a pure Y2-row. It holds one Y2-v1, the Y2-v2 and one Y2-v3.
- X's v3 is a Y2-v3 with index below a − d.
- F2b holds b3, the second Y2-v1 (index above a − d + 10) and the Q-v2, which lies in Q(b, u).

**F3.**
- If f > 5 + t, then β = [f+10, f+20] is a pure Y1-row and lacks v3.
- If f + 20 < 15 + t, then α and β are both pure Y2-rows and need two v2s, but Y2 carries one.
- b3 is not a cut. So f < 5 + t, b3 ∈ β, and γ's v3 is a Y2-v3 with index below f.

### S1: f < a − d

Both Y2-v1 vertices have index above f, so γ's v1 is Y1-v1, with e < index < 10 − f.

**Types.** Y1 regions: [1,e) {O,γ}, (e,10−f) {M,γ}, (10−f,14−t] {M,β}. Y2 regions: [1,f) {X,γ}, (f,a−d) {X,α}, (a−d,f+10) {F2c,α}, (f+10,a−d+10) {F2c,β}, (a−d+10,14+t] {F2b,β}. Q regions: [1,b) {I,X}, (b,u) {I,F2b}, (u,q−1] {M,F2b}.

**Two forced matchings.**
- The Y2[f]-label (cut rows {X,γ,α}) is forced: T, Y2(f+10,a−d+10), Q(u,q−1].
- The Y2[a−d+10]-label (cut rows {F2c,F2b,β}) is forced: Y2(f,a−d), Y1(e,10−f), T.

**v2 is adjacent to neither label in H.** The H-vertices of v2 are b2, Q-v2 ∈ Q(b,u), Y1-v2 ∈ (10−f,14−t] and Y2-v2 ∈ (a−d,f+10). Their neighbours are:
- P[d−1] (or b1);
- Y1[1], which is of type {O,γ} or the Y1[e]-cut;
- Y2[1], which is of type {X,γ}, since f ≥ 2 because the γ-Y2-v3 has index below f;
- vertices of Q[b..u];
- the Y1[10−f]-cut, {M,β}-vertices and b3;
- the Y2[a−d]-cut, the Y2[f+10]-cut and {F2c,α}-vertices.

None of these is a vertex of the two labels above. So v2 misses two labels in H, which contradicts v106 §2(b).

### S2: f > a − d

α = Y2(f, f+10) is a pure Y2-row, and Y2[f+10] ∈ F2b.
- If e < 10 − f: the Q[u]-label (cut rows {M,I,F2b}) is stuck. Row β's partners are M (via Y1) and F2b (via Y2), and both are removed.
- If e > 10 − f: the Y2[f+10]-label (cut rows {F2b,α,β}) is stuck. Row M's only partners are β (via Y1(e,14−t]) and F2b (via Q(u,q−1]), and both are removed.

So option (3,3,3) is impossible.

## 3. Option (4,3,2)

**Data.**
- y1 = 15 − t, y2 = 5 + t, q = 25 − t − d.
- v1 on (Y1, Y2, Q) = (1,1,1); v2 = (1,0,2); v3 = (0,1,1).

**F1.**
- F1 has rows O, A = [10,20], B = [20,30] and I. b3 is at 15 + d.
- If d ≥ 5, then A is a pure Y1-row (or b3 is a cut), and A lacks v3. So d ≤ 4 and b3 ∈ A.
- B = Q[20−t..u] is a pure Q-row, so it holds Q-v1, one Q-v2 and Q-v3.
- I holds the other Q-v2, at index below u. A holds Y1-v1 and Y1-v2 (index above e).

**F2.**
- The Q cut order is b < u < b + 10 < 20 − t < q.
- If q > b + 20, then X contains b3 and all of Y2, so X holds both b1 and the Y2-v1. Contradiction. So b3 ∈ F2c, and F2b = Q[b..b+10] is a pure Q-row.
- This forces:
  - Q-v1 and Q-v3 into Q(u, b+10);
  - the I-row Q-v2 into Q(b, u);
  - the B-row Q-v2 into Q(b+10, 20−t);
  - Y2-v1 into F2c (index above a − d);
  - Y2-v3 into X (index below a − d).

**F3.**
- F3 has two rows. If f > 5 + t, then α is a pure Y1-row and lacks v3. If f + 10 < 5 + t, then α is a pure Y2-row and lacks v2.
- So b3 ∈ α, γ's v3 is the Y2-v3 (index below f), and Y1-v2 ∈ α.

### P1: f < a − d

Then Y2-v1 ∈ α, so Y1-v1 ∈ γ with e < index < 10 − f.

**v1 and v2 need d = 1.** The v1-vertices and v2-vertices on Q and Y1 are separated by the cut vertices Q[u], Q[b+10] and Y1[10−f], and Y2 carries no v2. Q[1] is not the Q-v2 (index above b ≥ 1). Y1[1] and Y2[1] are not v1-vertices (indices above e ≥ 1 and above a − d ≥ t ≥ 1). So v106 §2(a) requires d = 1.

**But d ≥ 2.** The Y1[10−f]-label (cut rows {A,γ,α}) is forced to F2c–B (via Q), F2b–I (via Q) and O–X (via P). So P_int is non-empty and d ≥ 2. Contradiction.

### P2: f > a − d

- If e < 10 − f: the Q[20−t]-label (cut rows {A,B,F2c}) is stuck. Row α's only partners are F2c (via Y2(f,4+t]) and A (via Y1(10−f,14−t]).
- If e > 10 − f: the Y2[f]-label (cut rows {F2c,γ,α}) is stuck. Row A's only partners are F2c (via Q(20−t,q−1]) and α (via Y1(e,14−t]).

So option (4,3,2) is impossible.

## 4. Result

- **WRITTEN:** with v106, every W2 option of L4-B ((4,2,3), (3,3,3), (4,3,2)) is impossible. W2 is closed.

**Still open at m = 9:** L4-B W1, L1, and L2 with k = 3.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
