# K7-A2-ZT5-A: in (a2-zt5) granularity holds away from z or t; the split T* = W / |T*| = 3; the branch T* = W is empty (conditional)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T07:51:01-0700.
- **Owner:** Sun7K62Successor. Single author, unreviewed. No computation.
- **Status:** CANDIDATE. Lemma FG-zf and Lemma ZS use only accepted imports plus `K7-A2-FIVE-v1.md` (93fd95d7...8dfc;
  Lemma F, FG-a2, D23-a2, Proposition K7-A2-ZT5) as amended by `K7-A1-A2-delta-erratum-v1.md` (0e477743...7e54e).
  Theorem K7-ZT5-A is **conditional** on `K7-CASEA-K23-v1.md` (f70c8fdc...3fd3), `K7-CELL-v1.md` (d421e08c...aae) with
  `K7-CELL-erratum-v1.md` (56829e8d...132), and the A1 package they import. No closure claim; (a2-zt5) with |T*| = 3
  is NOT covered.

## 0. Setting

(a2-zt5) with the five in orientation alpha (the other orientation is symmetric by inversion): alpha_zt = 5,
alpha_zu = 3 for u in W := W' cup {p}, alpha*_zt = 1, alpha*_zu in {1,2,3}, T* := {u in W : alpha*_zu = 3}, |T*| >= 3,
alpha_tu in {2,4} (u in W'), alpha_tp in {1,2,4}, no other entry 5, E >= 2 (Proposition K7-A2-ZT5).

## 1. Lemma FG-zf (granularity away from z, resp. t) [NEW]

For u in W, x in {alpha, alpha*}:
- (a) every feasible y at u (orientation x) with y_z = 0, resp. y_t = 0, has val(y) <= 5; if val(y) = 5, every fibre C
  with S_C not contained in {z}, resp. {t}, has weight exactly 1;
- (b) at an apex a in W of C^alpha and of C^alpha*, the union of the D_j over j not in {a, z}, resp. not in {a, t}, has
  measure <= 5/6.
*Proof.* For x = alpha (and for C^alpha*) this is Corollary 5/6-a2 / FG-a2 with beta = alpha* (alpha*_zt = 1). For
x = alpha* (and for C^alpha), let N' := V \ {u, z}, resp. V \ {u, t}, and W' := the intersection of the conjugates (or
of the U_j) over N', pair parameters beta = alpha. Order N' as t, p, then W' (resp. z, p, then W'), omitting u: the base
factor is alpha_tp <= 4 (resp. alpha_zp = 3), and every later step factor is <= beta to an earlier vertex <= 4 (all
entries other than z-t are <= 4); so no prime >= 5 enters any factor, the prime-to-30 part of [G : W'] is the product of
the w_j (j in N'), and 5 divides [G : W'] only through n_p (p in N'). Hence gcd(n_u, [G : W']) = 6 for u in W' and for
u = p. The rest is the proof of RICH Corollary 5/6 (resp. Lemma FG-V) with W' in place of W*: the fibres (resp. cosets)
in W'U_u avoid every L_j (resp. D_j) with j in N' and may meet only z (resp. t), which carries weight 0. QED
**Consequences.** Rigid rows whose weight vectors vanish on z keep their containments L_i subset L_j for i != z (and, if
the vectors also vanish on t, the containments with i = z via the t-free version). Lemma K3, K2, EQ hold with unions
taken without z; Lemmas SUB, IN, CELL are unaffected; Lemma B holds in both orientations at rows with c = 3 (each of its
kills vanishes on z or on t); PFG-t and the "at least two entries 4" part of Corollary L hold in both orientations.

## 2. Lemma ZS (the split) [NEW]

**Either T* = W, or |T*| = 3 and W \ T* = {v1, v2} with alpha_v1v2 = 4, alpha_tv = 4 and alpha_va = 2 for every
a in T*, the alpha-rows of v1, v2 being (2,2,2,4 | 4).**
*Proof.* For u in T*, v in O* := W \ T*, the triangle {z, u, v} (alpha*_zu = 3, alpha*_zv in {1,2}) forces
alpha*_uv in {3,4} (RICH TZ (i) argument; no five), hence alpha_uv <= 3, and alpha_uv in {1,2} (alpha has no W-three by
the W3 argument: RICH R3 for alpha-rows with FG, TR and CC at z in C^alpha with alpha*_zt = 1, and the triangle step of
A1-STRUCT Corollary W3). A vertex v in O* has >= 3 alpha-entries <= 2, so Lemma B gives a single alpha-four inside O* and
alpha_tv = 4; hence |O*| != 1, and |O*| <= 2 as |T*| >= 3. The triangle (4, alpha_v1a, alpha_v2a) passes only as
(4, 2, 2). QED

## 3. Theorem K7-ZT5-A (conditional) [NEW]

**In (a2-zt5) there is no configuration with T* = W.**
*Proof (dependency audit).* With T = T* = W both orientations have c = 3 at every W-vertex, so the setting is the
(a2-no5)-type Case A with p in W, except that granularity is available only in the z-free / t-free form of Lemma FG-zf.
The proofs of K7-CASEA-K23 and Theorem K7-CELL-A go through verbatim with these replacements:
- every rigid row of (R-c) is used only through containments not involving z on the left (all weight vectors vanish
  on z), except R4 at v_i in the alpha_v1v2 = 1 branch, whose vectors vanish on z and t, so L_z subset L_x holds by the
  t-free version;
- Lemma K3 (all its uses have j, u != z), K2, CL, S, (S-a)-(S-f) and the 3-side R2 step are unchanged;
- the alpha_v1v2 = 1 branch of section 4 uses the t-free union: D_z (3/6) and D_v1, D_v2 (2/6 each, disjoint from D_z)
  lie in the union over j != t, of measure <= 5/6, so D_v1 = D_v2 = R with mu(R) = 2/6, and y (4/6) meets R: the triple
  {y, v1, v2} violates Sun(3) as before;
- Lemma EQ in Theorem K7-CELL-A uses the union over j != z (the counted vertices are v_i', t, x, y, w, resp. y, w, v1, v2,
  t); SUB, IN, CELL, the LFC (d) step at t (weights vanish on z) and the final step mu(U_zU_v1) = alpha_zv1/6 = 1/2 are
  unchanged; labels of p and z carry no new common prime (z has no 5-part; only p carries 5^B).
QED

## 4. Scope
Proved (accepted imports + A2-FIVE as amended): Lemma FG-zf, Lemma ZS. Conditional: Theorem K7-ZT5-A. Open: the branch
|T*| = 3 of (a2-zt5) (there alpha*_va may be 3, TZ (ii) for alpha* is not available, and the K7-TC-B count needs
L_z-containments that FG-zf does not give); K6.2*; full Sun(7). No novelty, Lean or human-review claim.
