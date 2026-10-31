# Original Tuscan-2(11), entire m = 9 distance-two branch, part 2: L4-B W1 with k_x = 2, 3, 4 excluded, so L4-B is closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4). Written reasoning only. No interpreter, enumeration, solver or search was used; every matching and count below was done by hand.

**Scope.** Family L4-B, single-face case W1 (v112 §3), with k_x ∈ {2, 3, 4} and every d, t, θ, ε and stretch-2 offset. Together with v112 §4 (k_x = 1) and v106–v107 (W2), this closes L4-B.

**What is used.** Only (R1)–(R2), through:
- the M_9 row structure (v94);
- the cut-label matching rule (v107 §1);
- the reverse-pair lemma v106 §2;
- the W1 stretch structure v112 §3.

Distance two (R3) is not used.

**Imports:** v94, v106 §1–2, v107 §1, v112 §3–4.

## 1. Set-up

**Notation.** Positions, rows [10k, 10k+10], the face order and the indicators θ, ε are as in v112 §3. Put e = 10 − t − d and u = 10 − t.

**Cuts.** Every cut position 10k (k = 1..8) carries a non-v 2-vertex, and each non-v label has exactly one cut passage. This is parity of row incidences:
- v1 and v2: 3 + 2·3 = 9;
- v3: 2 + 3 + 2·2 = 9;
- a non-v label: 1 + 2·4 = 9.

So branch vertices are never at cuts, and no 2-vertex has two cut passages.

**Y-coordinate.**
- Z_L carries b2 at z = 0 and b3 at z = y1, with L = y1 + y2.
- The stretch-1 position of z is t + d + z.
- The stretch-2 position of z is B2 + w, where w = (y1 − z) mod L.

**Identities.** x = t + 2d + L and q = 45 − x + d, so:
- B2 = 45 + d;
- B3 = 45 + d + L;
- A2 = x − d.

**Consequences of the identities.**
- **(i)** d ≠ 5, since otherwise B2 would sit on the cut at 50.
- **(ii)** k_x ≠ 4. R_in = Q[u..1], b1, T, ℓ3 needs q ≥ u + 1, that is x ≤ 34 + t + d. v94 Lemma TC needs x ≥ 10k_x + t + d.
- **(iii)** For k_x ∈ {2, 3}, A2 = x − d ≥ 10k_x + t > 10k_x, so ε = 0.
- **(iv)** d ≤ 4. If d ≥ 6, then B2 ∈ row 5, and the pure Q-rows strictly between x and B2 each need a forward Q-v3 passage. Those rows are row 4 for k_x = 3 and rows 3–4 for k_x = 2. But n_Q(v3) = 3 − k_x + θ, and θ = 1 needs one more forward Q-v3 passage in row k_x. The counts fail.
- **(v)** For k_x = 3, rows 5 and 6 are pure stretch-2 Y-rows, so θ = 0.
- **(vi)** For k_x = 2, row 3 is a pure Q-row. Its Q-v3 must return in a Q⁻-row containing neither B3 nor ℓ3. Since B3 ∈ rows 6–7, only row 7 can serve, and only when B3 ∈ row 6. Hence θ = 0, B3 ∈ row 6 and x ≤ 24 + t + d.

**Parameters for k_x = 3.**
- s3 = 40 − x ∈ [max(1, e−4), e], L = 30 + e − s3 − d, q = 5 + s3 + d.
- Q types: [1,s3) (3,8); cut Q[s3] {3,4,8}; (s3,u) (4,8); cut Q[u] {4,7,8}; (u,q−1] (4,7).
- Fixed rows: b1 {0,3,8}; b2 {0,3,A3}; b3 {B1,4,7}; ℓ3 {0,8}; T (0,8); P (0,3).
- Stretch-1 Y-cuts are at z = e, e+10, e+20. Stretch-2 Y-cuts are at ζ5 = y1−5+d, ζ6 = ζ5−10 and ζ7 = ζ5−20 (mod L).
- Stretch-2 arcs: row 4 = (ζ5, y1), row 5 = (ζ6, ζ5), row 6 = (ζ7, ζ6), row 7 = (y1, ζ7).

**v-placements for k_x = 3** (row counting from v112 §3):
- Q-v1 has type (4,7). Its forward row 3 holds b1 and its backward row 8 holds b1.
- Q-v2 has type (4,8). Row 3 holds A2, and row 8 = R_in needs its v2 from Q.
- The two Y-v1 have stretch-1 rows 1 and 2, and stretch-2 rows {5, 6}.
- The two Y-v3 have stretch-2 rows {5, 6}, and stretch-1 rows {1,2,3} ∖ {row B1}.
- The two Y-v2 have stretch-1 rows {1, 2}, and stretch-2 rows {5,6,7} ∖ {row A3}.
- A3 ∉ rows 3, 4, 8.

**Parameters for k_x = 2.**
- s = 30 − x ∈ [max(1, e−4), e], L = 20 + e − s − d, q = 15 + s + d.
- Q types: [1,s) (2,8); Q[s] {2,3,8}; (s,u) (3,8); Q[u] {3,7,8}; (u,s+10) (3,7); Q[s+10] {3,4,7}; (s+10,u+10) (4,7); Q[u+10] {4,6,7}; (u+10,q−1] (4,6).
- Fixed rows: b1 {0,2,8}; b2 {0,2,A3}; b3 {B1,4,6}; ℓ3 {0,8}; T (0,8); P (0,2).
- Stretch-1 cuts are at e and e+10. Stretch-2 cuts are at ζ5 = y1−5+d and ζ6 = ζ5−10.
- Stretch-2 arcs: row 4 = (ζ5, y1), row 5 = (ζ6, ζ5), row 6 = (y1, ζ6).

**v-placements for k_x = 2** (row counting):
- Q-v1 has types (3,7) and (4,6). The type (3,6) would need an index in (s,s+10) ∩ (u+10,q−1], which is empty.
- Q-v2 has types (3,8) and (4,7). Row 8 needs a Q-v2, and (4,8) would need an index in (s+10, q−1] ∩ [1,u), which is empty since d ≤ 4.
- Q-v3 has type (3,7).
- Y-v1 has type (1,5).
- Y-v3 has type (r,5), with r ∈ {1,2} ∖ {row B1}.
- Y-v2 has type (1,r′), with r′ ∈ {5,6} ∖ {row A3}.
- A3 ∈ {5, 6}.

**Tools.**
- **(M)** A cut label at {k−1, k} with its other passage in row r has three further 2-vertices. Their row pairs must partition the remaining six rows, using only types of nonempty regions. If no such partition exists, the label is *stuck*.
- **(F)** Which types meet rows 7 and 8:
  - For k_x = 3, the types meeting row 8 are T (0,8), (3,8) and (4,8), and those meeting row 7 are (4,7) and the Y-types (·,7).
  - For k_x = 2, every Y-type lies in {0,1,2} × {4,5,6}, so rows 7 and 8 are met only by T and the Q-types.
- **(B)** v106 §2. v1 and v2 are adjacent in H. v1 and v2 each miss exactly one label in H. Every other label misses exactly its two R-neighbours. So each of the following is a contradiction:
  - (B1) v1 and v2 never adjacent;
  - (B2) v1 or v2 missing two labels;
  - (B3) a non-v label missing three labels.

**Adjacency rule.** H-adjacency is read off the cycle. A thread vertex is adjacent only to its two thread neighbours: vertices of its own region, or the region's boundary vertices (cuts or branch vertices). The branch neighbours are:
- b1: τ, P[1], Q[1];
- b2: P[d−1], z = 1, z = L−1;
- b3: z = y1 ± 1, Q[q−1].

**Notation.** [p] denotes the label of the cut vertex at z = p, or at Q-index p for [Q p].

## 2. k_x = 3

Put δ := ζ6 − (e+10), taken in (−L/2, L/2] ∖ {0}. If |δ| ≤ L−21, the windows W1 = [e, e+20] (rows 1–2) and W2 = [ζ7, ζ5] (rows 5–6) overlap in one arc. Otherwise W2 passes z = 0 and meets W1 at both ends.

### (a) 1 ≤ δ ≤ L−21

Y-v1 needs an interior point of (e, e+10) ∩ W2 = (e+δ, e+10), so δ ≤ 8.

**(a1) ζ5 < L and y1 < L.** The cyclic order is:

    (0,e):(0,7) | e | (e,e+δ):(1,7) | e+δ | (e+δ,e+10):(1,6) | e+10 | (e+10,e+10+δ):(2,6) | e+10+δ | (e+10+δ,e+20):(2,5) | e+20 | (e+20,e+20+δ):(3,5) | e+20+δ | (e+20+δ,y1):(3,4) | b3 | (y1,L):(3,7)

Here A3 ∈ row 7 and B1 ∈ row 3. Each of v1, v2 and v3 has its Y-vertices of types (1,6) and (2,5).

By (M), the eight cut labels are:
- [Q s3]: {(0,7),(1,6),(2,5)};
- [Q u]: {P,(1,6),(2,5)};
- [e]: {(2,6),(3,5),(4,8)};
- [e+δ]: {(2,5),T,(3,4)} or {(2,5),P,(4,8)};
- [e+10]: {(3,5),(0,7),(4,8)} or {(3,5),T,(4,7)};
- [e+10+δ]: {(1,7),T,(3,4)} or {(1,7),P,(4,8)};
- [e+20]: {(1,6),(0,7),(4,8)} or {(1,6),T,(4,7)};
- [e+20+δ]: {T,(2,6),(1,7)}.

Consequences:
- No label uses (3,8) or (3,7), so s3 = 1 and y2 = 1, which means b3 is adjacent to b2.
- (1,7) holds exactly [e+10+δ] and [e+20+δ], so δ = 3.
- (0,7) holds [Q s3], so e ≥ 2.

The label [e] has vertices at the cut e and in (2,6), (3,5) and Q(s3,u).
- [e] is never adjacent to v1. b1's neighbours lie in T, in P, and at Q[1] = Q[s3]. v1's Y- and Q-regions and their boundaries carry no [e]-vertex.
- [e] is never adjacent to v3. ℓ3 meets T. b3 meets (3,4) or [e+20+δ], b2, and (4,7). Y-v3 lies in (1,6) or (2,5).
- [e] reaches v2, [Q u] and [e+δ] only through its Q(s3,u)-vertex. Its cut neighbours lie in (0,7) and (1,7), where (1,7) = {[e+10+δ], [e+20+δ]}. Its (2,6) and (3,5) vertices meet only (2,6), (3,5) and the cuts e+10, e+10+δ, e+20, e+20+δ. b2's neighbours are P, (0,7) and b3. That Q(s3,u)-vertex has two neighbours.

So [e] misses at least three labels, contradicting (B3).

**(a1′) ζ5 < L ≤ y1.** Then b2 lies in the row-4 arc, so A3 ∈ row 4. Contradiction.

**(a2) ζ5 ≥ L.** Here ζ5 − L ∈ (0, e). B1 ∉ row 0, so e ∈ (ζ5−L, y1) and [e] has rows {0,1,4}. By (F), row 8 must pair with 3. Row 7's types are then (4,7) and (1,7), since the row-7 arc (y1, e+δ) lies inside (e, e+10). Both are excluded, so [e] is stuck.

### (b) −(L−21) ≤ δ ≤ −1

**(b-i) e + δ > 0.** A3 ∈ row 7.
- If B1 ∈ row 2, then (e+20, L) lies in the row-7 arc, so no type (3,5) or (3,6) exists. Y-v3, whose stretch-1 rows are {1,3}, fails.
- If B1 ∈ row 3, then [e+20] has rows {2,3,4}. By (F), row 8 → 0, and row 7 → 0, since the only surviving Y-type is (0,7). [e+20] is stuck.

This argument does not use δ ≥ −(L−21).

**(b-ii) e + δ < 0.** Here ζ7 = L+e+δ ∈ [e+21, L−1] and A3 ∈ row 6.
- If δ ≤ −9, the region (e+10, e+20) has no row-5 or row-6 point, or (e, ζ6) is empty. Either way Y-v1 fails.
- If B1 ∈ row 3, the row-7 arc (y1, ζ7) lies inside (e+20, L). Y-v2 has stretch-2 rows {5, 7}, so it fails.
- If B1 ∈ row 2, the cyclic order is pattern **K2**:

      (0,e):(0,6) | e | (e,ζ6):(1,6) | ζ6 | (ζ6,e+10):(1,5) | e+10 | (e+10,ζ5):(2,5) | ζ5 | (ζ5,y1):(2,4) | b3 | (y1,e+20):(2,7) | e+20 | (e+20,ζ7):(3,7) | ζ7 | (ζ7,L):(3,6)

  The placements are forced:
  - Y-v1: (1,6) and (2,5);
  - Y-v2: (1,5) and (2,7);
  - Y-v3: (1,5) and (3,6).

  By (M):
  - [Q u] = {(2,5),(1,6),P}, so d ≥ 2;
  - [Q s3] = {(2,7),(0,6),(1,5)} and [e+20] = {(4,8),(0,6),(1,5)}, so e ≥ 3.

  **v1 and v2 are never adjacent:**
  - v1 lies in b1, (e,ζ6), (e+10,ζ5) and Q(u,q−1].
  - v2 lies in b2, (ζ6,e+10), (y1,e+20) and Q(s3,u).
  - These regions are pairwise separated by cuts or by b3.
  - b1 and b2 are not adjacent because d ≥ 2.
  - b1's neighbours lie in T, in P (labels [Q u] and possibly [ζ6]) and at Q[1] (in (3,8) or the cut Q[s3]).
  - b2's neighbours lie in P, at z = 1 ∈ (0,6), and at z = L−1 ∈ (3,6), whose labels are v3 or [e+10].

  This contradicts (B1).

### (c) L−21 < δ ≤ L/2

Put ω := ζ5 − L. Then ω ∈ [e+1, e+7] (ω = e would be a double cut), and y1 = ω+5−d ∈ (ω, e+11].

**(c1) ζ6 < L, so A3 ∈ row 5.**
- **(c1-i) δ ≥ 11.** (δ = 10 is a double cut.)
  - If y1 > e+10, then [e+10] has rows {1,2,4}. Row 7's types are (2,7) and (4,7), so [e+10] is stuck.
  - If y1 < e+10, the order is pattern K1 below.
- **(c1-ii) δ ≤ 9.** Then [ω] has rows {1,4,5}. Row 7's types are (1,7), because the arc (y1, e+δ) lies inside (e, e+10), and (4,7). So [ω] is stuck.

**(c2) ζ6 ≥ L.** Here A3 ∈ row 6 and ω ≥ 10.
- If y1 < e+10, then B1 ∈ row 1, and Y-v3 needs type (2,5) or (3,5). Neither exists, since the row-5 arc is (ω−10, ω) ⊂ (0, e+10).
- If y1 > e+10, then [e+10] has rows {1,2,4} and is stuck, as in (c1-i).

### (d) −L/2 < δ < −(L−21)

If e + δ > 0, the overlap is one-sided and (b-i) applies verbatim.

Otherwise put γ = δ+20 ∈ [4,14]. Then ζ5 = e+γ, ζ6 = e+γ−10 (mod L) and ζ7 = L+e+δ ∈ (e+10, e+20). (γ = 10 is a double cut, and γ+5−d = 10 would put b3 on a cut.)
- **(d-iii) γ > 10.** [ζ5] has rows {2,4,5}. Row 7's types are (2,7) and (4,7), so [ζ5] is stuck.
- **(d-ii) γ < 10 < γ+5−d.** z = e+10 lies in the row-4 arc, so [e+10] has rows {1,2,4} and is stuck.
- **(d-i) γ+5−d < 10.**
  - If e+γ > 10, then A3 ∈ row 6 and no (2,5) or (3,5) type exists, so Y-v3 fails.
  - If e+γ < 10, the order is pattern K1, with (ζ5, ζ7, ζ6) in the roles of (α, β, β′).

### Pattern K1

The cyclic order is:

    (0,e):(0,5) | e | (e,α):(1,5) | α | (α,y1):(1,4) | b3 | (y1,e+10):(1,7) | e+10 | (e+10,β):(2,7) | β | (β,e+20):(2,6) | e+20 | (e+20,β′):(3,6) | β′ | (β′,L):(3,5)

Here A3 ∈ row 5 and B1 ∈ row 1. The placements are forced:
- Y-v1: (1,5) and (2,6);
- Y-v2: (1,7) and (2,6);
- Y-v3: (2,6) and (3,5).

By (M), [α] (rows {1,4,5}) = {(2,7),(3,6),T}, and [β′] (rows {3,5,6}) = {T,(2,7),(1,4)}. Also [Q s3] and [e+10] both use (0,5), so z = 1 lies in (0,e).

v2's vertices and their possible neighbours are:
- b2: P, (0,e) and (β′,L);
- the Y-v2 in (y1,e+10): its region, b3 and [e+10];
- the Y-v2 in (β,e+20): its region, [β] and [e+20];
- the Q-v2 in Q(s3,u): its region, [Q s3] and [Q u].

None of these is a vertex of [α] or [β′]. So v2 misses two labels, contradicting (B2).

**So W1 with k_x = 3 is impossible.**

## 3. k_x = 2

Put δ := ζ6 − e, taken in (−L/2, L/2] ∖ {0}. Y-v1 of type (1,5) needs the arcs (e, e+10) and (ζ6, ζ5) to share an interior point. This forces |δ| ≤ 8. For 9 ≤ |δ| ≤ 11, an overlap through the wrap would need L ≤ 16 and |δ| = 8.

### (A) 1 ≤ δ ≤ 8

**(A1) ζ5 < L and y1 < L.** This is pattern **KA**:

    (0,e):(0,6) | e | (e,e+δ):(1,6) | e+δ | (e+δ,e+10):(1,5) | e+10 | (e+10,e+δ+10):(2,5) | e+δ+10 | (e+δ+10,y1):(2,4) | b3 | (y1,L):(2,6)

Here A3 ∈ row 6, B1 ∈ row 2, and Y-v1, Y-v2 and Y-v3 are all of type (1,5).

By (M):
- [Q s] = {(4,7),(0,6),(1,5)};
- [Q u+10] = {(3,8),(1,5),P};
- [e+δ+10] (rows {2,4,5}) = {(1,6),T,(3,7)}.

The vertices of [e+δ+10] and their possible neighbours are:
- the cut: (2,5) or [e+10], and (2,4) or b3;
- the (1,6)-vertex: (1,6), [e] and [e+δ];
- the T-vertex: T, b1 and ℓ3;
- the (3,7)-vertex: Q(u,s+10), [Q u] and [Q s+10].

These contain no vertex of [Q s], of [Q u+10], or of v2. b2's neighbours are P, z = 1 and z = L−1, and z = L−1 lies in (2,6) or is b3.

So [e+δ+10] misses three labels, contradicting (B3).

**(A1′) ζ5 < L ≤ y1.** Then A3 ∈ row 4. Contradiction.

**(A2) ζ5 ≥ L, with ζ5′ = ζ5 − L > 0.**
- If ζ5′ < e, then B1 ∉ row 0 puts e in the row-4 arc, so [e] has rows {0,1,4}. By (F), row 7 → 3 and row 8 → 2. Rows 5 and 6 are then left with no admissible pair. [e] is stuck.
- If ζ5′ > e, the order is:

      (0,e):(0,5) | e | (e,ζ5′):(1,5) | ζ5′ | (ζ5′,y1):(1,4) | b3 | (y1,ζ6):(1,6) | ζ6 | (ζ6,e+10):(1,5) | e+10 | (e+10,L):(2,5)

  Here [ζ5′] has rows {1,4,5}. Row 6's types are only (1,6) and (4,6), so [ζ5′] is stuck.

### (B) −8 ≤ δ ≤ −1

**(B1) e + δ > 0.**
- If y1 > e+10, then [e+10] has rows {1,2,4}, and rows 5 and 6 both need row 0. Stuck.
- If y1 < e+10, then B1 ∈ row 1 and Y-v3 needs type (2,5). But (e+10, L) lies outside the row-5 arc, so it fails.

**(B2) e + δ < 0, with ζ6 = L+e+δ.**
- If ζ6 < e+10, the cyclic order is the second order of (A2), and [ζ5] is stuck.
- If ζ6 > e+10 and y1 < e, then B1 ∈ row 0. Contradiction.
- If ζ6 > e+10 and y1 > e+10, Y-v2 needs type (1,6). None exists, so it fails.
- If ζ6 > e+10 and e < y1 < e+10, the order is pattern **KB**:

      (0,e):(0,5) | e | (e,e+δ+10):(1,5) | e+δ+10 | (e+δ+10,y1):(1,4) | b3 | (y1,e+10):(1,6) | e+10 | (e+10,ζ6):(2,6) | ζ6 | (ζ6,L):(2,5)

  Here A3 ∈ row 5, Y-v1 has type (1,5), Y-v2 has type (1,6), and Y-v3 has type (2,5).

  By (M):
  - [Q u+10] = {(3,8),(1,5),P}, so d ≥ 2;
  - [Q s] = {(4,7),(0,5),(1,6)} and [e+10] = {(0,5),(4,7),(3,8)}, so e ≥ 3.

  **v1 and v2 are never adjacent:**
  - v1 lies in b1, (e,e+δ+10), Q(u,s+10) and Q(u+10,q−1].
  - v2 lies in b2, (y1,e+10), Q(s,u) and Q(s+10,u+10).
  - These regions are separated by cuts or b3.
  - b1's neighbours lie in T, P and Q[1].
  - b2's neighbours lie in P, (0,5) and (ζ6, L), and the last region carries v3 and no v1.

  This contradicts (B1).

**So W1 with k_x = 2 is impossible.**

## 4. Result

**WRITTEN, (R1)–(R2) only.** L4-B W1 is impossible for every k_x:
- k_x = 1 by v112 §4;
- k_x = 4 by §1 (ii);
- k_x = 3 by §2;
- k_x = 2 by §3.

With v106–v107 (W2), **family L4-B is impossible.**

Every case above ends in one of four ways:
- a stuck cut label;
- a failed v-placement;
- a v1–v2 non-adjacency (patterns K2 and KB);
- a missing-label count above the v106 §2 budget (case (a1), patterns K1 and KA).

**Open in the v143 branch:** L2 with k = 3, and L1. The acceptance ceiling of v143 is unchanged:
- "every eligible original Tuscan-2(11) array with support 9 is impossible" may be stated only after all three families are excluded;
- any m ≥ 10 consequence needs the full m ≤ 8 plus m = 9 joint gate;
- every m in 10..110 remains unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. An unpacketed working note (on the case δ < −e of k_x = 3) had claimed a placement failure; this packet replaces it with pattern K2 and its v1–v2 non-adjacency. This candidate needs its own complete source-bound gate.
