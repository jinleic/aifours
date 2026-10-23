# K7-A1-STRUCT: the (a1) residue after RICH: no W-threes, partial granularity at t, Case-B structure, and two abstract patterns that pass every written rule so far

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T05:42:53-0700.
- **Owner:** Sun7K62Successor. Single author, unreviewed. No computation was run; no probe is a premise.
- **Status:** CANDIDATE written mathematics (sections 1-5) plus a precise OBSTRUCTION record (section 6). Sections 1 and 5
  are **conditional on the candidate `K7-D23-RICH-v1.md`** (sha256 ba32d2829d62a684d82748994e2fd519d22b041d4d41ed00ecb44235f43f2bb3)
  with its erratum (sha256 8261831ba11777cf1a7c4a1c714ba324f77bc58a3c4fdb297029dce67790ba69), now in parent review. Nothing
  here claims that the (a1) family is excluded; full Sun(7) remains OPEN.

## 0. Scope, notation, imports

Setting (a1) and notation exactly as `K7-D23-RICH-v1.md` section 0: z carries the 2-marker (r_z = 2^E 5^Bz w_z), t the
3-marker (r_t = 3^A 5^Bt w_t), E, A >= 1, Bz Bt = 0, W = V \ {z, t} unmarked; T = {u : alpha_zu = 3},
T* = {u : alpha*_zu = 3}; x ranges over {alpha, alpha*}; C^alpha is the configuration and C^alpha* its inverse (INV (a)).
From RICH (imports, at their candidate scope): G0, Lemma FG7 and Corollary 5/6 (val <= 5 at u in W, both orientations),
NO5 (no W-W or W-t entry 5), Lemma R3 (the rows with a W-three are S1-S4: c = 3, e = 2, no W-four), Lemma TZ, Lemma LZ,
Theorem K7-D23-RICH. Accepted imports as listed in RICH section 0 (R0, LFC, INV and errata E1/E2/E6/E7/E8, L1 (T),
VFC (V1)-(V4), D23-MIX). Sun(2)-Sun(5) are used only inside LFC (c) / VFC (V3); Sun(5) appears exactly where five pieces
with pairwise gcds <= 4 are declared not allowed (Corollary L, the two kills marked [Sun(5)]). No Sun(6) or Sun(7).

**Triangle evaluation used throughout.** For a triangle all of whose vertices are in W, or {t, a, b} with a, b in W,
and whose three entries lie in {1, 2, 4}, every ell-divisor is trivial (w's and 3^A 5^Bt are prime to 2), so with the
entries sorted p <= q <= r: tau_min = lcm = r and tau_max = min(r p, p q, q p) = p q. **T passes iff r <= p q**:
allowed (1,1,1), (1,2,2), (1,4,4), (2,2,2), (2,2,4), (2,4,4), (4,4,4); forbidden (1,1,2), (1,1,4), (1,2,4).

**Allowed sets of a two/four class.** For local indices or labels 2^i w (i in {1, 2}; "twos" and "fours") with pairwise
coprime w's prime to 30, the pairwise gcds are 2, except 4 between two fours. Hence (through LFC (c) / VFC (V3)) the
allowed sets inside such a class are exactly: singletons, all pairs, the triples with >= 2 fours (Sun(3)), the 4-sets
with >= 3 fours (Sun(4)); no 5-set is allowed (five pieces with pairwise gcds <= 4) [Sun(5)]. Elements of local index or
label w alone ("ones") lie only in singletons (Sun(2)).

## 1. Corollary W3 (conditional on RICH) [NEW]

**In (a1), W3 = W3* = empty: every W-W entry of alpha and of alpha* lies in {1, 2, 4}.**

*Proof.* Let alpha_uv = 3 and w in W \ {u, v}. If neither alpha_uw nor alpha_vw is 3, the triangle {u, v, w} has entries
(3, a, b) with a, b in {1, 2, 4} (NO5); tau_min = 3 lcm(a, b) and tau_max <= 3 min(a, b) force a = b, and then
tau_max = a min(3, a) >= 3a only for a = 4. So alpha_uw = 4, but u in W3 has no W-four (R3). Hence every w lies in W3,
i.e. W3 = W, so T* subset W3, which Theorem K7-D23-RICH excludes. Same for alpha* (inverted configuration). With NO5
the entries lie in {1,2,4}. QED

## 2. Lemma E3 [NEW]

**For u in W and x in {alpha, alpha*}: x_ut != 3.** Hence (NO5) every W-t entry lies in {1, 2, 4}.

*Proof.* At u the W-labels are powers of 2 times w's (section 1); the t-label 3^(A+1) 5^Bt w_t shares no prime with them
and at most the prime 3 with the z-label (only if c = 3; at most one of Bz, Bt is positive). Standard class weights on the
four W-neighbours give >= 4 (E8), y_z = 0, y_t = 1: val >= 7 > 5, against Corollary 5/6. QED

## 3. Lemma PFG-t (partial granularity at t) [NEW]

Let x in {alpha, alpha*} and suppose the graph Gamma^x := {uv subset W : x_uv <= 2} is **connected**. Work in C^x,
normalised g_t = 1, at apex t: D_j := U_t g_j U_j has measure x*_tj/6 and local index d_j = x*_tj r_j (VFC (V1), (V2),
INV (b) applied to C^x). Then:
- (i) mu(U_t W_W) >= 1/6, where W_W := intersection of the U_u (u in W) of C^x; hence for every y on W that is feasible
  for the allowed subsets of W: sum_(u in W) y_u x*_tu <= 5.
- (ii) If (i) holds with equality for y, then every right U_t-coset R contained in the union of the D_u (u in W) satisfies
  y(S_R cap W) = 1; and D_z := U_t g_z U_z contains such a coset R, so S_R contains z and is allowed (VFC (V3)).

*Proof.* (i) Choose a spanning tree of Gamma^x and order W so that the first two vertices are adjacent in it and every
later vertex has an earlier tree-neighbour. With V_u = U_u (C^x), T_2 = lcm(n_u1, n_u2) x_u1u2 with x_u1u2 <= 2, and as in
FG7 each later factor satisfies k = T_(m+1)/lcm(n_e, T_m) <= gcd(n_e, T_m) mu(V_e V_j) = x_ej <= 2 for the tree-neighbour j
(gcd(n_e, T_m) = 6). So T_W = [G : W_W] = 6 (prod of w_u) * (factors in {1, 2}), whence v3(T_W) = 1, 5 does not divide T_W,
and gcd(n_t, T_W) = gcd(6 * 3^A 5^Bt w_t, T_W) = 6. G0 gives mu(U_t W_W) >= 1/6. U_tW_W lies in U_tU_u = X_u for every
u in W, hence (V1) avoids every D_u. VFC count restricted to W (S_R cap W is allowed by heredity):
sum_u y_u mu(D_u) = sum_R mu(R) y(S_R cap W) <= mu(union_W D_u) <= 1 - 1/6.
(ii) Equality forces mu(U_tW_W) = 1/6, union_W D_u = G \ U_tW_W and y(S_R cap W) = 1 on that union. D_z avoids U_t (V4)
and U_t subset U_tW_W, so mu(D_z cap U_tW_W) <= 1/6 - 1/n_t < 1/6 <= x*_tz/6 = mu(D_z); D_z therefore meets the union,
which is a union of right cosets, in a right coset R. QED

**Corollary L (allowed t-rows).** Under the hypothesis of PFG-t, the multiset M of t's x*-entries on W is one of

  4,4,2,2,2 (z four-type) | 4,4,1,2,2 (z four-type) | 4,4,4,1,2 | 4,4,4,2,2 | 4,4,4,4,2,

where "z four-type" means E + v2(x*_tz) >= 2 (the local index x*_tz 2^E 5^Bz w_z has gcd 4 with a local index 4 w_u).
*Proof.* Entries lie in {1,2,4} (E3, NO5). The W-local indices x*_tu w_u have pairwise gcds gcd(x*_tu, x*_tu'), so the
allowed W-sets are those of the two/four class plus singleton ones. Write k1, a, b for the numbers of entries 1, 2, 4.
The following weights are feasible and violate (i) (value > 5):
- b = 1: every triple of the class needs two fours, so only pairs are allowed there: y = 1/2 on the twos and the four,
  y = 1 on the ones (if a = 0: y = 1 on the four): value k1 + a + 2 = 6, resp. k1 + 4 = 8.
- b = 0, a = 1: y = 1 on the four ones and on the two: 4 + 2 = 6.
- b = 2, k1 >= 2: y = 1/2 on the two fours, 1 on the ones: 4 + k1 >= 6.
- b = 3, k1 = 2: y = 1/3 on the fours, 1 on the ones: 4 + 2 = 6.
The following have a feasible y of value exactly 5, so equality holds in (i) and (ii) applies to that y; in each case
every W-set of y-weight 1 fails to be allowed together with z:
- 11111 (y = 1): weight-1 W-sets are single ones; {z, one} has coprime local indices (Sun(2)).
- 1^(5-a) 2^a, 2 <= a <= 5 (y = 1 on ones, 1/2 on twos): weight-1 W-sets are {one}, {two, two'}; the local index of z has
  gcd 2 with every two, so {z, two, two'} has all pairwise gcds 2 (Sun(3)).
- 44441 (y = 1 on the one, 1/4 on fours) and 44444 (y = 1/4): weight-1 W-sets are {one} or the four fours (resp. any four
  fours); z with four fours is a 5-set with pairwise gcds <= 4 [Sun(5)].
- 44222 (y = 1/4 on fours, 1/2 on twos) and 44122 (the same, 1 on the one): weight-1 W-sets are {f1, f2, two}, {two, two'}
  and {one}; {z, f1, f2, two} is allowed only if z is four-type (otherwise its 3-subset {z, f1, two} has all gcds 2), and
  {z, two, two'}, {z, one} never are.
The remaining multisets are 44412 (value 5 with y = 1 on the one, 1/3 on fours; {z, f, f, f} is allowed), 44422 and
44442 (no claim on their values is needed), and 44222, 44122 with z four-type. QED

In particular every surviving M has **at least two entries 4**.

## 4. Lemma B (rows with three W-entries <= 2 at c = 3) [NEW]

Let u in W, x an orientation with c = x_uz = 3 and at least three W-entries in {1,2} (all W-entries in {1,2,4}). Then the
W-part is (1,2,2,4) or (2,2,2,4) as a multiset, **E >= 2 and x_ut = 4**.

*Proof.* At u: z-label 3 * 2^E * 5^Bz w_z (coefficient 3) has gcd 1 with a one, 2 with a two, 2^min(E,2) with a four.
- W-part in {1,2} only: z and the a twos have pairwise gcd 2, so with y = 1 on the ones and 1/2 on each two and on z
  (y_t = 0) the weights are feasible (no allowed triple among them, Sun(3)); val = 4 + 3/2 if a >= 1, and val = 4 + 3
  (y_z = 1) if a = 0. Both > 5.
- (1,1,1,4): W-alone 3 + 4; (1,1,2,4): 2 + V24(1,1) = 6. Both > 5.
- (1,2,2,4) or (2,2,2,4) with E = 1: z and the four have gcd 2, so twos, four and z have pairwise gcd 2: y = 1/2 on them
  (and 1 on the one): val = 1 + (2 + 2 + 4 + 3)/2 or (2 + 2 + 2 + 4 + 3)/2, both 13/2.
- E >= 2, x_ut = 1: the W-part alone has an optimal weight with y_z = 0 of value 5 ((1,2,2,4): one 1, four 1; (2,2,2,4):
  1/2 each, only pairs are allowed among them); t's label 3^A w_t meets only z: y_t = 1 adds 1. val = 6.
- E >= 2, x_ut = 2: y = 1 on a one, 1/2 on each two, on the four and on t, y_z = 0. Allowed sets through t are {t, two},
  {t, four}, {t, z, two}, {t, z, four} (t has gcd 2 with twos and fours, 6 with z; {t, two, two'}, {t, two, four} have all
  gcds 2); {z, four, two} weighs 1. Feasible; val = 6 in both cases.
So x_ut = 4 (E3 excludes 3, NO5 excludes 5). QED

## 5. Theorem K7-CASEB (conditional on RICH) [NEW]

**If T = W and T* != W, then |T*| = 3; writing T* = {a1, a2, a3} and W \ T* = {v1, v2}: E >= 2; alpha_v1v2 = 4;
alpha_tv = 4 (v = v1, v2); alpha_av = 2 for all a in T*, v in {v1, v2}; alpha_aa' = 4 for all a != a' in T*;
alpha_ta in {2, 4} for every a in T*, with alpha_ta = 2 and alpha*_ta = 4 for at least two a; alpha*_av = 4; alpha*_aa',
alpha*_v1v2, alpha*_tv, alpha*_zv lie in {1, 2}.** (The case T* = W, T != W is the same with alpha and alpha* exchanged.)

*Proof.* TZ (ii) for alpha* gives alpha* = 4 on T* x (W \ T*), so alpha <= 2 there (INV). Each v in W \ T* has c = 3
(T = W) and at least |T*| >= 3 W-entries <= 2; by Lemma B its W-part has exactly one 4, E >= 2 and alpha_vt = 4. The 4
cannot point into T*, so |W \ T*| >= 2 and |T*| = 3, alpha_v1v2 = 4. Triangle {v1, v2, a}: entries (4, alpha_v1a,
alpha_v2a) with the last two <= 2; only (2, 2, 4) passes, so alpha_av = 2. For a in T*: the t-triangle {t, a, v} has entries
(alpha_ta, 4, 2), so alpha_ta != 1, i.e. alpha_ta in {2, 4} (E3, NO5). Gamma^alpha contains all six a-v edges and is
connected, so Corollary L applies in C^alpha: t's alpha*-row on W has at least two entries 4, and alpha*_tv <= 6 - 4 = 2, so
at least two a have alpha*_ta = 4, hence alpha_ta <= 2, hence alpha_ta = 2. For such an a, Lemma B (which would force
alpha_ta = 4 if a had three W-entries <= 2) gives alpha_aa' = alpha_aa'' = 4; two such a make all three T*-edges 4. The
alpha*-statements follow from INV and the 3-type alpha*-row at z (D23-MIX). QED

## 6. OBSTRUCTION: two abstract patterns passing every written rule used so far

The following are abstract (alpha, alpha*) patterns with index shapes, NOT group constructions and NOT claimed realisable.
Common data: E = 2, A = 1, Bz = Bt = 0 (any w's); alpha_zt = alpha*_zt = 1; alpha_zu = 3 for all u in W.

**Pattern Q_B (Case B).** W = {a1, a2, a3, v1, v2}.
alpha: a-a 4, a-v 2, v1v2 4, t-a 2, t-v 4. alpha*: z-a 3, z-v 1, a-a 2, a-v 4, v1v2 1, t-a 4, t-v 2.
**Pattern Pc5' (Case A).** W = {u1, ..., u5}; C5 := {u1u2, u2u3, u3u4, u4u5, u5u1}, P5 := the other five pairs.
alpha: C5 4, P5 2, t-(u1..u5) = (4, 4, 2, 2, 2). alpha*: z-u 3, C5 2, P5 4, t-(u1..u5) = (2, 2, 4, 4, 2).

**Checks (each by explicit weights or covers; units 1/6).**
1. INV: every pair sums to <= 6 (Q_B: z-a 6, z-v 4, z-t 2, a-a 6, a-v 6, v1v2 5, t-a 6, t-v 6; Pc5': 6 everywhere except
   z-t 2 and t-u5 4). D23-MIX: both z-rows are 3-type. NO5, E3: no 5 or 3 off the z-row. W3 = W3* = empty.
2. FG rows (<= 5) at W-vertices, both orientations. Four row types occur (W-multiset | c | e; units 1/6; each bound by an
   explicit cover with allowed sets, E = 2):
   R1 = ({2,2,4,4} | 3 | 2): value 5; cover weight 1 on {f1,f2,z,s1} and {f1,f2,z,s2}, 2 on {f1,f2,z,t}, 1 on {s1,s2}.
   R2 = ({2,2,4,4} | 3 | 4): value <= 4; cover weight 2 on each 5-set {f1,f2,z,t,s_i} (allowed: gcd(z,t) = 12, and every
   4-subset has three fours or {z,t}).
   R3 = ({2,2,2,4} | 3 | 4): value 5; cover 4/3 on each {f,z,t,s_i}, 1/3 on each pair of twos.
   R4 = ({1,4,4,4} | 1 | 2): value 5; cover 2 on {f1,f2,f3,z} (z-label 4 w_z), 2 on {f1,f2,f3,t}, 1 on {one}.
   Q_B: a has alpha-row R1 and alpha*-row R2; v has alpha-row R3 and alpha*-row R4. Pc5': alpha-rows R2 at u1, u2 and R1 at
   u3, u4, u5; alpha*-rows R1 at u1, u2, u5 and R2 at u3, u4 (fours on the C5-neighbours for alpha, on the P5-neighbours for
   alpha*).
3. LFC at z (< 6): all six labels with pairwise gcd 3 (alpha; alpha* of Pc5'): <= 16/3. alpha* of Q_B: the a's and t
   (gcd 3) give <= 10/3, the coprime v-labels 2: total <= 16/3.
4. LFC at t (< 6): W-parts (2,2,2,4,4) or (4,4,4,2,2) or (4,4,2,2,2) with z four-type of coefficient 1: covers of total 5
   (weight 4/3 on each {f, f, z, s_i} and 1/3 on pairs of s's, or 2 on {f,f,f,s_i} plus 1 on {z}).
5. PFG-t: Q_B: Gamma^alpha (all a-v edges) connected, t's alpha*-row (4,4,4,2,2) value 4 <= 5; Gamma^alpha* is
   disconnected (T* and {v1, v2}), no condition. Pc5': Gamma^alpha = P5 and Gamma^alpha* = C5 are connected; t's rows
   (2,2,4,4,2) and (4,4,2,2,2) are 44222 with z four-type (E = 2): value 5 and D_z can sit in cosets of type
   {z, f1, f2, s} (allowed).
6. T on all 35 triangles, both orientations: W-triangles and t-W-W triangles have entries in {1,2,4} and are of the allowed
   types (Q_B alpha: (4,4,4), (2,2,4), (2,2,4); alpha*: (2,2,2), (2,4,4), (1,4,4); t-triangles alpha (2,2,4), (2,2,4),
   (4,4,4), alpha* (2,4,4), (2,4,4), (1,2,2); Pc5': every K5-triangle has two C5-edges and one P5-edge or vice versa,
   giving (2,4,4)/(2,2,4); the ten t-triangles per orientation are (4,4,4), (2,2,4), (2,4,4), (2,2,2) types).
   z-W-W: (3,3,x): tau_min = 3 <= 3 min(3,x). Q_B alpha* {z,a,v}: (3,1,4): tau_min = 3 = tau_max; {z,v1,v2}: (1,1,1).
   z-t-W: tau_min = lcm(1, 3/3, x_tu/gcd(x_tu, 4)) = 1 for all x_tu in {1,2,4} (E = 2), so every such triangle passes.
7. TZ, LZ are consistent (Q_B: T = W, T* = {a's}, alpha* = 4 on T* x {v's}, Gamma*_1 = {v1v2} disconnected; Pc5': T = T* = W,
   Gamma_1 = Gamma*_1 empty). RICH's hypothesis fails (W3 = empty). Lemma CASEB's conclusions hold for Q_B.
8. Centre counts at z: with D_u = Y_u for tight u, the counts only require that D_t meets the T*-union in positive measure
   (Q_B, alpha*_zt = 1) and that sum_u phi_u lies in [3, 5) (Pc5'); FG-tightness at the rows above forces y_z = 0 in every
   optimal weight, so it does not fix phi_u. No contradiction.

## 7. Exact missing lemma and scope

- **Missing lemma (precise):** a cross-vertex constraint that, for rows with forced y_z = 0 (above), either forces every
  t-fibre at u to meet z (then RICH's count closes) or bounds sum_u phi_u below 3; equivalently, a global double count of
  the (U_u, W_N)-double cosets of measure 1/6 across different u. Without it Q_B and Pc5' (and their analogues) remain.
- **Proved here (conditional on RICH):** Corollary W3, Lemma E3, Lemma PFG-t with Corollary L, Lemma B, Theorem K7-CASEB.
  These are narrowings, not exclusions of (a1).
- **Not covered:** (a2) beyond `K7-D23P-v1.md`; K6.2*; full Sun(7). No novelty, Lean or human-review claim.
