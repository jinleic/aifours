# Actual Tuscan11, m = 9, line L3 (3+3 at v, 3 at w): v-location lemma, W2 face identities, option (1,1,0)

Option (1,1,0) is reduced to eight explicit skeletons.

Actual `/bin/date` before this body: **Mon Oct 26 14:09:13 PDT 2026**. InfoRecursiveMDS18-2.

**Status.** NEW exact WRITTEN CANDIDATE: not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO.

**Scope.** Tuscan-1-only support-ladder work on R6 (all m ≥ 9, no Tuscan-2 cap). This packet makes necessary-case reductions, not constructions and not Tuscan-2 statements. It is a separate, ungated successor line, outside the v19–v49 and v150b freezes.

## 1. Setting

The setting is v94 §5.3 and §8.1 (SHA256 `1c5465c4f0a5835ecda93a2a9877d42f3b607d774f63e49be9f1228a951c396c`).

**Branches and paths.**
- b′ (label v) carries the tail T, of length t, to the leaf ℓ (label w).
- P joins b′ to b″ (label v); Q joins b′ to b_w (label w).
- Y1 and Y2 join b″ to b_w.
- Indices run from b′ on P, Q and T, and from b″ on Y1 and Y2. Lengths are p, q, y1, y2 edges.
- Put u = 10 − t and S = X ∖ ({v, w} ∪ L(T_int)).

**Rotations.**
- By the row-reversal mirror, b′ has rotation (T, P, Q). By naming, b″ has (P, Y1, Y2).
- b_w has (Q, Y1, Y2) (W1, one face) or (Q, Y2, Y1) (W2, three faces).

**Imported (v94 §8.1).**
- The v-cut is at b′'s corner (P→Q).
- R_out = ℓ, T, b′, P[1..u] and R_in = Q[u..1], b′, T, ℓ, with L(P[1..u]) = L(Q[1..u]) = S.
- R_end = P[10..1], b′, so p ≥ 11. R_start = b′ followed by 10 walk vertices along Q.
- L(P[u+1..10]) = {w} ∪ L(T_int), and likewise for walk positions u+1..10 along Q.

## 2. Lemma VL (v-location; W1 and W2)

**(a) The P side.** Let R_1 be the row after R_out in its face. Then R_1 ⊇ P[u..10]. Its last u walk vertices (positions 11..u+10 from b′ along P) carry (S ∖ {c1}) ∪ {v}, where c1 = L(P[u]).

So R_1 contains b″ (if p ≤ u+10) or a v-2-vertex on P[11..u+10] (if p ≥ u+11).

**(b) The Q side.** If q ≥ 11, then Q[u+1..10] carries w. So the row before R_in cannot reach b_w; it is Q[u..u+10], and q ≥ u+11. Exchanging it with R_start gives L(Q[11..u+10]) = (S ∖ {L(Q[u])}) ∪ {v}. So a v-2-vertex lies on Q[11..u+10].

*Proof.* Both parts are exchanges of rows sharing an initial segment at b′, with the imported label sets. ∎

## 3. W2: faces, identities, options

**Faces.**
- F1 = T, T⁻, P, Y1, Q⁻ (contains ℓ).
- F2 = Q, Y2⁻, P⁻ (contains the v-cut).
- F3 = Y2, Y1⁻.

**Identities.** Let a, b, c1, c2 count the v-2-vertices on P, Q, Y1, Y2, and a′, b′, c1′, c2′ the w-2-vertices. Then v12 (1) gives:
- r1 = 3 + a + b + c1 = 3 + a′ + b′ + c1′;
- r2 = 3 + a + b + c2 = 1 + a′ + b′ + c2′;
- r3 = 1 + c1 + c2 = 1 + c1′ + c2′.

Using a+b+c1+c2 = 2 and a′+b′+c1′+c2′ = 3 gives **c1 = c1′ + 1 ≥ 1**.

**Options.** (c1, c2, a+b) ∈ {(1,0,1), (1,1,0), (2,0,0)}, with r = (5,4,2), (4,4,3), (5,3,3). The face lengths give:

| Option | y1 | y2 | p + q |
|---|---|---|---|
| (1,0,1) | 15 − t | 5 + t | 35 − t |
| (1,1,0) | 15 − t | 15 + t | 25 − t |
| (2,0,0) | 25 − t | 5 + t | 25 − t |

## 4. Option (1,1,0)

### 4.1 Forced shape

**Parameters.**
- Since a = b = 0, Lemma VL gives p ≤ u+10 and q ≤ 10. b_w is not a cut, so q ≤ 9.
- Placing b″ and b_w off the rows that contain b′ or ℓ, and b_w off R_1 (whose w is the P-w-vertex), gives:
  - 11 ≤ p ≤ 14;
  - 16 ≤ t+p ≤ 19;
  - q = 25 − t − p;
  - s := q + t − 5 = 20 − p.
- **The w-2-vertices.** a′ ≥ 1 is forced: L(P[u+1..10]) ∋ w puts a w-vertex on P[u+1..10]. Then the identities give a′ = 1 with that vertex in P[u+1..9], c2′ = 2, and b′ = c1′ = 0.
- **t ≥ 2.** P[10] is an F2 cut, so its label y0 is not w, the w-cut being ℓ. Hence y0 ∈ T_int.

**The eight rows of F1 and F2.**

| Face | Row | Vertices |
|---|---|---|
| F1 | R_out | ℓ, T, b′, P[1..u] |
| F1 | R_1 | P[u..p−1], b″, Y1[1..g], with g = 20 − t − p |
| F1 | R_2 | Y1[g..14−t], b_w, Q[q−1..u] |
| F1 | R_in | Q[u..1], b′, T, ℓ |
| F2 | R_start | b′, Q[1..q−1], b_w, Y2[14+t..s+10] |
| F2 | mid1 | Y2[s..s+10] |
| F2 | mid2 | Y2[1..s], b″, P[p−1..10] |
| F2 | R_end | P[10..1], b′ |

**The rows of F3.** F3 is b″, then Y2[1..14+t], b_w, then Y1⁻, then b″, with three rows. Each row has one v and one w. The v's are b″, the Y1-v and the Y2-v. The w's are b_w and the two Y2-w's, j2 (in mid2) and j1 (in mid1). Their cyclic order forces cuts f1, f1+10, f1+20 with:
- j2 < f1 < j1 and f1 < 5 + t;
- Row_A = Y2[f1..f1+10];
- Row_B = Y2[f1+10..14+t], b_w, Y1[h..14−t], with h = 10 − f1;
- Row_C = Y1[1..h], b″, Y2[1..f1].

The alternative, in which Row_C's w is b_w, puts two v's in Row_C.

Put δ = f1 − s. Then δ ≠ 0, because the cuts are distinct.

### 4.2 δ > 0 is impossible

- R_start against Row_B gives L(Y1[h..14−t]) = {v} ∪ L(Q[1..q−1]) ∪ L(Y2[s+10..f1+9]). So Row_B's Y1 part contains all of S.

**If h ≥ g.** R_2 against Row_B gives L(Y2[f1+10..14+t]) ∋ L(Q[u]) ∈ S. So Row_B contains that label twice. Contradiction.

**If h < g.**
- R_2 lies inside Row_B's Y1 part together with b_w and Q[u..q−1].
- R_start against R_in gives L(Q[u+1..q−1]) ⊔ L(Y2[s+10..14+t]) = L(T_int).
- So L(Y2[s+10..14+t]) ⊆ L(Y2[s+10..f1+9]). Both segments lie in R_start, so their labels are distinct. Hence f1 ≥ 5+t. Contradiction.

### 4.3 δ < 0: the skeleton

**h > g.** mid2 against Row_C gives L(Y1[1..h]) = L(Y2[f1+1..s]) ⊔ L(P[10..p−1]). So y0 = L(P[10]) lies on Y1[1..h], and not on Y1[1..g], since R_1 contains P[10]. Hence h > g.

**Row pairs.** Every 2-vertex now lies in a fixed pair of rows:

| Segment | Row pair |
|---|---|
| T | {R_out, R_in} |
| P1 = P[1..u−1] | {R_out, R_end} |
| P2 = P(u..10) | {R_1, R_end} |
| P3 = P(10..p−1] | {R_1, mid2} |
| Q1 = Q[1..u−1] | {R_in, R_start} |
| Q2 = Q(u..q−1] | {R_2, R_start} |
| Y1a = [1,g) | {R_1, Row_C} |
| Y1b = (g,h) | {R_2, Row_C} |
| Y1c = (h,14−t] | {R_2, Row_B} |
| Y2a = [1,f1) | {mid2, Row_C} |
| Y2b = (f1,s) | {mid2, Row_A} |
| Y2c = (s,f1+10) | {mid1, Row_A} |
| Y2d = (f1+10,s+10) | {mid1, Row_B} |
| Y2e = (s+10,14+t] | {R_start, Row_B} |

**Cut vertices.**
- P[u] → {R_out, R_1, R_end}; P[10] → {R_1, R_end, mid2}; Q[u] → {R_2, R_in, R_start}.
- Y1[g] → {R_1, R_2, Row_C}; Y1[h] → {R_2, Row_C, Row_B}.
- Y2[f1] → {mid2, Row_C, Row_A}; Y2[s] → {mid2, mid1, Row_A}; Y2[f1+10] → {mid1, Row_A, Row_B}; Y2[s+10] → {R_start, mid1, Row_B}.

**Forced vertex types for v and w.**
- v: b′, b″, one vertex of type Y1c and one of type Y2c.
- w: ℓ, b_w, one vertex each of types P2, Y2a and Y2c.

**Matchings.** Each of the other nine labels has one cut triangle. Its other four 2-vertices must perfectly match the remaining eight rows using the pairs above. The matchings are:

| Cut | Label | Remaining four vertices |
|---|---|---|
| (1) P[u] | c1 | Q1, plus {Y1b, Y2b, Y2d} (V=1) or {Y2a, Y2c, Y1c} (V=0) |
| (2) P[10] | y0 | T, Y2c, Y1b, Y2e |
| (3) Q[u] | c_in | P1, Y2d, Y2b, Y1a |
| (4) Y1[g] | λ4 | P1, Q1, Y2b, Y2d |
| (5) Y1[h] | λ5 | P1, Q1, P3, Y2c |
| (6) Y2[f1] | λ6 | T, P2, Q2, Y2d |
| (7) Y2[s] | λ7 | α: Y1a, P1, Q1, Y1c; or β: T, P2, Y1b, Y2e |
| (8) Y2[f1+10] | λ8 | α: P1, Q1, P3, Y1b; or β: T, P2, Y2a, Q2 |
| (9) Y2[s+10] | λ9 | T, P2, Y1b, Y2b |

**Segment-length equations.** Write B = [7β], C = [8α], D = 1 − C. Equating each segment's length with the number of labels using it (all fourteen equations are mutually consistent) gives:

    t = 4 + B + D,  p = 12 + C,  q = 8 − B,  s = 7 + D,  f1 = 3 + D − V,  g = 3 − B,  h = 7 − D + V.

**Skeletons.** These are eight explicit skeletons, indexed by (B, C, V). Every row automatically carries each label once. **The only open condition is pair uniqueness** on the 55 split edges: one edge per unordered label pair, and no edge between equal labels. The paths are:
- P = P1{c_in, λ4, λ5, λ7α, λ8α}, c1, P2{λ6, λ9, λ7β, λ8β, w}, y0, P3{λ5, λ8α};
- Q = Q1{c1, λ4, λ5, λ7α, λ8α}, c_in, Q2{λ6, λ8β};
- Y1 = Y1a{c_in, λ7α}, λ4, Y1b{c1 if V=1, y0, λ7β, λ8α, λ9}, λ5, Y1c{c1 if V=0, λ7α, v};
- Y2 = Y2a{c1 if V=0, λ8β, w}, λ6, Y2b{c1 if V=1, c_in, λ4, λ9}, λ7, Y2c{c1 if V=0, y0, λ5, v, w}, λ8, Y2d{c1 if V=1, c_in, λ4, λ6}, λ9, Y2e{y0, λ7β};
- T{y0, λ6, λ9, λ7β, λ8β}.

## 5. Result

**WRITTEN, Tuscan-1 necessary cases:**
- Lemma VL holds for L3.
- W2 has exactly the three options above.
- In option (1,1,0), δ > 0 is impossible.
- δ < 0 reduces to the eight skeletons of §4.3, which are open on pair uniqueness.

**Still open in L3:** options (1,0,1) and (2,0,0) of W2, and all of W1.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
