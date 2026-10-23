# K7-A2-ZT5-B: the branch |T*| = 3 of (a2-zt5) is empty (conditional)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T07:53:56-0700.
- **Owner:** Sun7K62Successor. Single author, unreviewed. No computation.
- **Status:** CANDIDATE, **conditional** on `K7-A2-ZT5-A-v1.md` (4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919:
  Lemma FG-zf, Lemma ZS), `K7-CELL-v1.md` (d421e08c...aae) with `K7-CELL-erratum-v1.md` (56829e8d...132: Lemmas EQ,
  SUB, IN, CELL), `K7-CASEA-K23-v1.md` (f70c8fdc...3fd3: Lemma K3 and the rigid-row list), and the A1 package (Lemma TC,
  Lemma B, PFG-t / Corollary L, R1 for every E >= 1) through the overlay `K7-A1-A2-delta-erratum-v1.md` (0e477743...7e54e);
  plus `K7-A2-FIVE-v1.md` (93fd95d7...8dfc) as amended. Accepted: RICH, LFC, INV, VFC, L0.1-L0.3, R0. Direct Sun(2),
  Sun(3). No closure claim.

## Statement

**Theorem K7-ZT5-B (conditional).** In (a2-zt5) (the five in orientation alpha) there is no configuration with
|T*| = 3.

## Proof

Notation of K7-A2-ZT5-A. By Lemma ZS: T* = {a1, a2, a3}, O* = {v1, v2}, alpha_v1v2 = 4, alpha_tv = 4, alpha_va = 2, the
alpha-rows of v1, v2 are (2,2,2,4 | 4); alpha* = 3 on z-T*, alpha*_zv in {1,2}, alpha*_zt = 1, alpha*_va in {3,4}
(TZ (i)), alpha*_v1v2 <= 2, alpha*_tv <= 2. Below "FG-zf" is Lemma FG-zf (a) with the stated weights vanishing on z
(and on t where noted), and every count in C^alpha* uses the full Lemma FG-V (its pair parameters are alpha*, and
alpha*_zt = 1).

**Step 1 (alpha-data).** Gamma^alpha contains all a-v pairs, so PFG-t / Corollary L in C^alpha gives two vertices of W
with alpha*_t = 4; as alpha*_tv <= 2 they are a's, say a1, a2, and alpha_ta <= 2 for them. For such an a the alpha-row has
alpha_av = 2 at both v; an entry alpha_aa' <= 2 would give three entries <= 2 and Lemma B would force alpha_ta = 4. So
alpha = 4 on all a-a pairs.

**Step 2 (alpha*-rows at a).** Fix a in T*. (i) If alpha*_av1 = 4 then alpha*_av2 = 4: otherwise the labels 4w_v1 and
3w_v2 are coprime and y = (v1 1, v2 1) has value 7 (FG-zf, y_z = y_t = 0). (ii) If alpha*_av1 = alpha*_av2 = 4, the row is
(x, y, 4, 4 | 3 | alpha*_ta) with x, y = alpha*_aa' <= 2. If it is not (2,2,4,4 | 4), it is R1*, R1-* or R5* (or the
excluded (1,1,4,4), value 6 with y = (ones 1, fours 1/2)), so L*_v1 = L*_v2 at a (weights vanish on z), and at apex v1 in
C^alpha* the masses alpha_v1v2 = 4 and alpha_v1a = 2 contradict Lemma K3. So the row is (2,2,4,4 | 4): alpha*_aa' = 2 on
both a-a pairs at a and alpha*_ta = 4. (iii) If alpha*_av1 = alpha*_av2 = 3, the row is (3,3,x,y | 3 | e*) with
x, y <= 2: (3,3,1,2) has value 6 with y = (v1 1/2, v2 1/2, one 1, two 1); for (3,3,1,1) and (3,3,2,2) the weights
(v1 1/3, v2 1/3, t 1/3, ones 1 resp. twos 1/2) are feasible ({v1, v2, t} has pairwise gcds 3; {s, s', t} has all gcds 2)
with value 4 + e*/3, so e* = alpha*_ta <= 2 (FG-zf, y_z = 0). Hence a1, a2 (alpha*_ta = 4) fall under (ii).

**Step 3 (a3).** If alpha*_(a3 v) = 3, the alpha*-row at v has W-entries 4 (a1), 4 (a2), 3 (a3); the weights
(a1 1/2, a2 1/2, a3 1) are feasible (the label 3 w_a3 is coprime to 4 w_a1, 4 w_a2) of value 7 (FG-zf, y_z = y_t = 0).
So alpha*_(a3 v) = 4 and, by Step 2 (ii), every a has alpha*_ta = 4, alpha* = 2 on all a-a pairs, alpha*_av = 4 and
alpha_ta <= 2 (alpha_ta = 2 for a in W'; alpha_tp in {1, 2} if p is in T*).

**Step 4 (alpha*_v1v2 = 2).** Suppose alpha*_v1v2 = 1. The alpha*-row at v is (1, 4, 4, 4 | c* | e*) with c* = alpha*_zv
in {1,2}; e* = 1 is excluded (t's label 3^A w_t is then coprime to all labels and y = (o 1, fours 1/3, t 1) has value 6,
FG-zf with y_z = 0), so it is R4 with weights vanishing on z and t: by the t-free version, every fibre containing z
contains all three a's, i.e. L*_z subset L*_a at v. At apex a in C^alpha* (masses: a', a'' 4/6, v1, v2 2/6, z 3/6,
t alpha_ta/6 <= 2/6) Lemma TC gives D*_z cap D*_v = empty for both v; a coset holding both v's holds nothing else (a
third element from a', a'', t has gcd 2 with both; z is excluded), and the count of K7-TC Theorem K7-TC-B (i) gives
mu(union) >= 11/12 > 5/6, contradicting Lemma FG-V. So alpha*_v1v2 = 2.

**Step 5 (alpha*_tv).** LFC (d) at t in C^alpha* (labels a: 4w; v with alpha*_tv = 1: w, coprime to all) excludes
alpha*_tv1 = alpha*_tv2 = 1 (y = 1/3 on the a's, 1 on the two ones: value 6). Choose i with alpha*_(t v_i') = 2.

**Step 6 (two index-3 subgroups and the cells).** In C^alpha* (masses at an apex u are alpha_uj/6, and
mu(U*_jU*_k) = alpha*_jk/6):
- H: choose a in T* cap W' (alpha_ta = 2). At apex a the masses are a', a'': 4/6; v1, v2, t: 2/6; z: 3/6. Lemma EQ gives
  D*_a' = D*_a''; alpha*_aa' = 2 gives D*_a' = Y*_a'; Lemma SUB (alpha*_(a'a'') = 2) gives H = U*_aU*_a' = U*_a'U*_a'' of
  index 3 containing U*_a1, U*_a2, U*_a3, the three a's in the three H-cosets.
- K': at apex v_i the masses are v_i', t: 4/6; a's: 2/6; z: 3/6. Lemma EQ gives D*_(v_i') = D*_t; alpha*_v1v2 = 2 gives
  D*_(v_i') = Y*_(v_i'); Lemma SUB (alpha*_(v_i' t) = 2) gives K' = U*_v1U*_v2 = U*_(v_i')U*_t of index 3 containing
  U*_v1, U*_v2, U*_t.
- m's: mu(U*_aU*_v) = mu(U*_aU*_t) = 4/6 and Lemma IN at the a's (alpha*_av = alpha*_at = 4) give m^H_v = m^H_t = 3;
  mu(U*_aU*_v1) = 4/6 and Lemma IN at v1, v2, t (alpha*_va = alpha*_ta = 4) give m^K'_a = 3; K' != H.
- Cells (Lemma CELL; piece indices n_v/3 = 2 r_v, with r_p = 5^B w_p, r_t = 3^A w_t, r_z = 2^E w_z): t does not share a
  K'-coset with v1 or v2 (pieces v, t, a with pairwise gcd 2, Sun(3)); z meets no cell of the K'-cosets of v1, v2
  (pieces v, a, z); so U*_z subset K' and z lies in the K'-coset of t; then N_z = n_z m^H_z / 9 forces m^H_z = 3 and
  N_z = 2^(E+1) w_z, and the pieces of t, a, z in any cell of that K'-coset have pairwise gcd 2: z meets no cell.
  Contradiction. QED

## Scope
Conditional result: with Theorem K7-ZT5-A, the branch (a2-zt5) would be empty. Not a closure claim; every link is pending
review. No novelty, Lean or human-review claim.
