# Actual Tuscan11 distinct 3+5, disconnected — one-v-one-w windows, a triangle lemma at b_v, a loop-cycle lemma at b_w, and part of Type II with r_P = 3

Actual `/bin/date` before this body: **Mon Oct 26 10:58:57 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result. Separate, ungated successor line (not part of the v19-v49 freeze).

## 1. Setting and imports

The setting is v60 (SHA256 `d09ec901a98a25480d12b9c81622c43044f5c2415b196fb9d64bb71ae9ad6259`): the nine-row component H of a disconnected distinct 3+5 array, with b_v of degree 3 and b_w of degree 5. Neither v nor w is a cut in H. The copy counts are those of v60 §2.

**Imports:**
- the exchange identity, in which every row of H carries the 11 labels once;
- distinct cut labels.

**Lemma W (one v, one w per row).** Every row of H contains exactly one visit of a v-vertex and exactly one visit of a w-vertex.

*Proof.* Each row carries the label v once. A v-vertex visit is never a boundary, so it lies in exactly one row. Hence the visits of v-vertices (b_v and the copies) are in bijection with the rows of H; the same holds for w. ∎

Consequently, along each face, consecutive v-visits are separated by exactly one row boundary, and so are consecutive w-visits.

**Pure rows.** At a branch vertex z, call a row **pure** if it consists of z together with two initial segments, taken from z, of two different half-edges at z. Both segments must be nonempty and consist of interior vertices of their paths. A pure row's 10 non-z labels split into the labels of its two segments.

## 2. Triangle lemma at the degree-3 vertex

**Lemma T3.** Let R1, R2, R3 be the three rows through b_v, all pure. Each pair of them shares a half-edge: thread X for R1 and R2, Y for R2 and R3, Z for R3 and R1. Call a row **shorter** on a half-edge if its segment there is shorter than the other row's segment there; equal lengths would double a cut. Then every row is shorter on exactly one of its two half-edges.

*Proof.* Write U for the 10 non-v labels and S_h(m) for the labels of the first m vertices of half-edge h.

Let R1 have segments of lengths x1 on X and z1 on Z, R2 have x2 on X and y2 on Y, and R3 have y3 on Y and z3 on Z. Suppose R1 is shorter on both of its half-edges: S_X(x1) ⊊ S_X(x2) and S_Z(z1) ⊊ S_Z(z3).
- Complementing the X-inclusion in U, using the partitions of R1 and R2, gives S_Y(y2) ⊊ S_Z(z1).
- The Z-inclusion and the partition of R3 give S_Z(z1) ∩ S_Y(y3) = ∅.
- So S_Y(y2) ∩ S_Y(y3) = ∅. But both are nonempty initial segments of Y. Contradiction.

Now count: three half-edges carry three "shorter" marks, and no row carries two, so each row carries exactly one. ∎

## 3. Loop-cycle lemma at b_w (Type II)

In Type II, let Q_a and Q_b be O's rows through b_w(x) (A → D) and b_w(x+t) (D → B^-). Suppose D's forward pass carries exactly one O-boundary, at D[σ]. Then Q_a = A-segment, w, D[1..σ] and Q_b = D[σ..t−1], w, B-segment. Let R_P* be P's row through b_w, with B-segment S_B and A-segment S_A, not reaching b_v.

**Lemma C5.** If S_A lies inside Q_a's A-segment and S_B lies inside Q_b's B-segment (as vertex sets), then we have a contradiction.

*Proof.*
- From Q_b's labels: L(D[t−1..σ]) ⊂ U ∖ L(S_B) = L(S_A).
- From Q_a's labels: L(D[1..σ]) ⊂ U ∖ L(S_A) = L(S_B).
- R_P*'s two segments have disjoint labels, so L(D[1..σ]) and L(D[t−1..σ]) would be disjoint. Both contain L(D[σ]). Contradiction. ∎

The containment holds whenever both of R_P*'s boundaries next to b_w are nearer to b_w than the corresponding O-boundaries (those of Q_a on A and Q_b on B).

## 4. Type II with r_P = 3: forced structure and one excluded sub-case

Here P = B A^- has 3 rows of length 30, with |A| = x, |B| = y and x+y = 30. O = A D B^- C D^- C^- has 6 rows, with |D| = t and |C| = c = 15−t.

**Copies.** By v60 §2, A and B together carry two v-copies and two w-copies. C and D carry one v-copy, visited twice by O, and no w-copy.

O's positions:
- A at [0, x];
- D at [x, x+t];
- B^- at [x+t, 30+t];
- b_v at 30+t;
- C at [30+t, 45];
- D^- at [45, 45+t];
- C^- at [45+t, 60].

**(a) Each D pass has exactly one O-boundary.** There is no w-copy on D. So by Lemma W, exactly one boundary separates the consecutive w-visits b_w(x) and b_w(x+t), and likewise b_w(45) and b_w(45+t).

Let:
- Q_a ∋ b_w(x) and Q_b ∋ b_w(x+t), meeting at D[σ], with K := x+σ, so Q_a = [K−10, K] and Q_b = [K, K+10];
- Q_c ∋ b_w(45) and Q_d ∋ b_w(45+t), meeting at D[τ].

By Lemma W, O's six rows run cyclically as:
- n_A^w rows, each containing one A w-copy;
- then Q_a, Q_b;
- then n_B^w rows, each containing one B w-copy;
- then Q_c, Q_d;

with n_A^w + n_B^w = 2.

**(b) Sub-case n_A^w = n_B^w = 1 with 10+t < K < 20.** The rows are
- M2 = [K−20, K−10] = C[20−K..1], v, A[1..K−10];
- Q_a;
- Q_b = D[σ..t−1], w, B[y−1..ρ], with ρ = 20+t−K;
- M1 = [K+10, K+20] = B[ρ..1], v, C[1..K−10−t];
- Q_c;
- Q_d.

This follows from the positions: K < 20 puts b_v(0) in M2, and K > 10+t puts b_v(30+t) in M1. Lemma W then distributes the copies:
- M1 and M2 have v = b_v. So the A v-copy lies in Q_a and the B v-copy in Q_b, at most one each, hence exactly one each.
- The C/D v-copy cannot lie on D: its forward visit would give Q_a or Q_b a second v. So it lies on C, with its forward visit in Q_c and its backward visit in Q_d.
- The A w-copy lies in M2 and the B w-copy in M1.

On A, the w-copy (nearer b_v) precedes the v-copy; the same holds on B.

So P's six visits alternate v, w, v, w, v, w cyclically:
- b_v;
- the B w-copy, then the B v-copy;
- b_w;
- the A v-copy, then the A w-copy.

By Lemma W, P's three boundaries either all follow a w-visit (**option α**) or all follow a v-visit (**option β**).

**Option α.** P's b_v-row is R_P1 = A[10−β_P..1], v, B[1..β_P], with 10−β_P < a_w < K−10. So R_P1 is shorter on A than M2. By Lemma T3 it is not shorter on B, so β_P > ρ, i.e. K+β_P > 20+t.

P's b_w-row is R_P2 = B[β_P..y−1], w, A[x−1..20−β_P]:
- Its A-segment has length x−20+β_P, below Q_a's length 10−σ = x+10−K, because K+β_P < 30.
- Its B-segment has length y−β_P, below Q_b's length 10−t+σ = 10−t+K−x, because K+β_P > 20+t.

Lemma C5 gives a contradiction.

**Option β.** Now β_P < b_w' < ρ, where b_w' is the B w-copy's B-coordinate, so R_P1 is shorter on B. By Lemma T3, M2 is shorter on A, i.e. K+β_P < 20.

P's b_w-row is R_P3 = B[β_P+10..y−1], w, A[x−1..10−β_P]:
- Its A-segment has length x−10+β_P < x+10−K, because K+β_P < 20.
- Its B-segment has length y−β_P−10 < 10−t+K−x, because K+β_P > 10+t (from K > 10+t).

Lemma C5 gives a contradiction.

All rows used are pure, which the position bounds guarantee. So **sub-case (b) is impossible**.

## 5. Result and exact remaining gap

**WRITTEN.** Lemmas W, T3 and C5 hold in H. In Type II with r_P = 3, the sub-case n_A^w = n_B^w = 1 with 10+t < K < 20 is impossible.

Still open in Type II with r_P = 3:
- n_A^w = n_B^w = 1 with K ≥ 20 (b_v(0) in Q_d) or K ≤ 10+t (b_v(30+t) in Q_c);
- (n_A^w, n_B^w) = (2,0) and (0,2).

Also open: Type II with r_P = 2, and Type I with r_P = 3, 4.

The other residual lines (R4, R6) are unchanged (manifest v15-delta, SHA256 `c97eef158b7662465804d23e8eca0fe8927f112df891888ff42d2f0439d2c803`, plus v75).

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
