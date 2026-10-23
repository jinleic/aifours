# K62-STATUS-v2: K6.2* after K62-E3 — exact frontier and an explicit locally consistent pattern at e_d >= 4

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T04:30:28-0700.
- **Author:** Sun63Successor. No computation. Supersedes `K62-STATUS-v1.md` (sha256
  1dd9129545eadd7e03c094be4df4ce24a9bf81ff19c0a44638cb5f2dee9e6797) as navigation; that file stays frozen.
- **Status labels:** everything below is CANDIDATE/navigation unless a parent verdict is cited. The obstruction in
  section 3 is a statement about which written constraints a pattern passes; it is not a claim that a group exists.

## 1. Frontier (if `K62-E3-v1.md`, sha256 70a60d551583e8d6ad920acadb829d3ddf0d9c5c46ac988f8677645ee5457372, is accepted)
K6.2* remains open exactly for **e_d >= 4, e* = 2** (3-marker on i*, on a vertex t of O, or absent; 5-marker
anywhere; arbitrary exponents). The R2 candidates (`K62-FG-v1.md` Theorem R2-11, `K62-R2-v1.md`) and the accepted
K62-A lie inside e_d <= 3 and are subsumed.

## 2. Written facts available in the residue (candidates, with their sources)
- Lemma 1 of K62-E3: alpha_(d i*) = alpha*_(d i*) = 1 unless t exists; otherwise (1,1), (1,3) or (3,1).
- Lemma 2 of K62-E3 (with the h_d = 0 five argument of its Corollary C2): every O-O entry of alpha and alpha* lies in
  {1, 2, 4}; at most two 1s per O-row.
- K62-E3 step 4 and C1, C2, in each orientation x with x_(d i*) = 1, for the conjugate family of the other
  orientation: v2 of the O-intersection index >= 4; of every 4-subset index >= 3; n_4 >= 2 n_1 + 2.
- T rule (L1) on O-triangles: forbidden (1,1,2), (1,1,4), (1,2,4); on triangles {v, u, i*} (v, u in O, f* = 1, unmarked):
  with a = x_vu, b = x_(v i*), c = x_(u i*): forbidden a = 1 with b != c; a = 2 with {b, c} = {1, 4}; a = 4 with
  b = c = 1. (Derived from tau_min = lcm(a / gcd(a, 2), b, c) and tau_max = min(a min(b,c), b min(a,c), c min(a,b)).)

## 3. Explicit pattern P_ob (no 3-marker beyond f = 1, no 5-marker, e_d >= 4, e* = 2)
O = {c1, ..., c5}; indices are taken mod 5.
- alpha on O: 4 on the cycle edges c_i c_(i+1), 2 on the chords c_i c_(i+2). alpha* on O: 2 on cycle edges, 4 on chords.
- alpha_(i* c) = (4, 2, 2, 4, 1), alpha*_(i* c) = (2, 4, 4, 2, 2) for c = c1, ..., c5.
- alpha = alpha* = 1 on all six d-edges.

**P_ob passes every one of the following written tests:**
1. INV (b) on all 21 edges (O-O: 2 + 4; i*: 4+2, 2+4, 2+4, 4+2, 1+2; d: 1+1).
2. Lemma 1, Lemma 2, Corollaries C1/C2 of K62-E3 in both orientations (n_1 = 0, n_4 = 5; every 4-subset of O contains
   a 4-edge of the relevant family, so the 4-subset 2-adic bound is automatic; the O-intersection bound v2 >= 4 is a
   condition on the group which the pattern does not decide).
3. The T rule on all 35 triangles: O-triangles are (2,4,4) or (2,2,4) (allowed); {v, u, i*} triangles avoid the three
   forbidden shapes in both orientations (the chords carrying 2 in alpha join i*-entries (4,2), (4,4), (2,4), (2,1),
   (2,1); the cycle edges carrying 2 in alpha* join (2,4), (4,4), (4,2), (2,2), (2,2)); triangles through d have
   tau_min = 1 <= tau_max for every entry pattern with alpha_vd = alpha_(i* d) = 1 and e_d >= 4.
4. **LFC and VFC at every O-vertex even with the bound 5/6** (val <= 5 in units of 1/6 for every feasible y). Each
   O-row is one of {2,2,4,4 | x_*} with x_* in {1, 2, 4}; labels have 2-power types (twos 2, fours 4; i*: 2 (x_* odd),
   4 (x_* = 2), 8 (x_* = 4); d: >= 8, load 3). Dual certificates (weights on allowed sets covering every load):
   - x_* = 1: weight 4/3 on each of {a1, f1, f2, d}, {a2, f1, f2, d}, {i*, f1, f2, d} and 2/3 on {a1, a2}: total 14/3;
   - x_* = 2: weight 2 on {f1, f2, d, i*}, 1 on {a1, f1, f2, d}, 1 on {a2, f1, f2, i*}, 1 on {a1, a2}: total 5;
   - x_* = 4: weight 2 on each of {d, i*, f1, f2, a1}, {d, i*, f1, f2, a2} (allowed 5-sets: types >= 8, 8, 4, 4, 2): total 4.
   (a1, a2 the O-twos, f1, f2 the O-fours.)
5. **LFC at i* with bound 5/6** (stronger than the 11/12 granularity bound available when f* = 1): rows
   {1, 2, 2, 4, 4} (alpha) and {2, 2, 2, 4, 4} (alpha*), d of type 2^(e_d - 2) >= 4 and load 3/2. Duals: weight 2 on each
   {a_i, f1, f2, d} (alpha; plus 1 on the isolated 1-entry): total 5; weight 4/3 on each {a_i, f1, f2, d} and 1/3 on
   each pair of twos (alpha*): total 5.
6. LFC at d: all six labels have pairwise gcd 3 and the uniform optimum is 11/12 < 1; the K62-E3 count holds as soon
   as v2([G : W*_O]) >= 4 (group data, not pattern data).

**Not tested against P_ob:** forced containments (F7) combined with VFC tightness and (V3) at several vertices,
pair-intersection systems (Ppair/RPLP-type), Lemma XE/L6-type subgroup arguments, two-orbit/group structure. At c1,
for instance, F7 gives X_c3 in X_c5, X_c4 in X_c2, X_c3 in X_(i*), X_c5 = X_(i*), and every edge at c1 is tight
(D_j = Y_j); these relations were not pushed to a contradiction here.

## 4. What a closure of e_d >= 4 needs (navigation, not a claim)
- A written route must go beyond single-vertex LFC/VFC (with or without granularity), INV, Lemma OO and the T rule,
  since P_ob passes all of them. Candidates: (a) F7 + tightness + VFC (V3) systems at several vertices (in P_ob
  every O-O edge and every d-edge is tight); (b) group structure at d (for c in O, U_d has exactly two orbits on
  G/U_c, since D_c = Y_c is one double coset of measure 1/2), in the spirit of `K63-TWO-ORBIT-v1.md`.
- If a computational route is chosen instead: the universe can be made finite exactly as in rules-k7-v1 Lemma CAP,
  with e_d capped at 4 (every gcd at an O-vertex, at i* and at d, and every granularity condition used above, is the
  same for all e_d >= 4) and 3-/5-exponents capped at 2; the load-bearing completeness lemma would be a CAP extension
  to coupled (alpha, alpha*) patterns that also covers the 2-adic granularity conditions of K62-E3 (which depend on
  min(e_d, v2(.)), hence on e_d only through min(e_d, 4) for the thresholds used). Nothing is implemented or run;
  any such route needs a frozen universe/coverage/certificate contract, two independent checkers and a parent GO.
