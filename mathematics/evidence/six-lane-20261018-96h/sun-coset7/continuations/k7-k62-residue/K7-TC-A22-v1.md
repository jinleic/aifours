# K7-TC-A22: in Case A of (a1) no configuration has every W-vertex with two alpha-fours and two alpha*-fours

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T06:07:57-0700.
- **Owner:** Sun7K62Successor. Single author, unreviewed, no computation.
- **Status:** CANDIDATE, **conditional** on `K7-D23-RICH-v1.md` (ba32d282...f2bb3) + erratum (8261831b...0ba69),
  `K7-A1-STRUCT-v1.md` (c8a16f14...e3ccf, sections 1-3: Corollary W3, E3, PFG-t with Corollary L) and `K7-TC-v1.md`
  (cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117: Lemma TC, row R1). It generalises Proposition TC-P of
  K7-TC (the pattern Pc5'). (a1) is NOT excluded; full Sun(7) remains OPEN.

## 0. Scope

(a1), Case A: T = T* = W (alpha_zu = alpha*_zu = 3 for all u in W). By Corollary W3, E3 and NO5, all W-W and W-t entries
of alpha and alpha* lie in {1, 2, 4}. F := {uv : alpha_uv = 4}, F* := {uv : alpha*_uv = 4} (disjoint by INV).
**Hypothesis A22:** every u in W has exactly two F-neighbours and exactly two F*-neighbours.

**Theorem K7-TC-A22 [NEW].** No (a1) configuration satisfies Case A and A22 (any group, R0).

## 1. Structure under A22

(a) F is 2-regular on five vertices, so it is a 5-cycle; F* is 2-regular and edge-disjoint from F, so it is the
complementary 5-cycle. (b) No entry 1 on W: if alpha_uv = 1 (uv not in F), the W-triangle rule ((1, a, b) passes only for
a = b; A1-STRUCT section 0) gives alpha_uw = alpha_vw for every other w, so u and v would have the same F-neighbours,
but two vertices at distance 2 on a 5-cycle share exactly one neighbour. The same for alpha* on F. Hence alpha = 2 off F
and alpha* = 2 off F*, and every row is ({2,2,4,4} | 3 | e) in both orientations (c = 3 in Case A).
(c) Such a row with e in {1, 2} forces **L_f1 = L_f2** for its two fours f1, f2 (fibres of the configuration whose row it
is): for e = 2 this is R1 of K7-TC; for e = 1 take y1 = (f1 1/2, f2 1/2, twos 0, t 1, z 0) and y2 = (f1 1/4, f2 1/4, twos
1/2 each, t 1, z 0), both feasible of value 5 (t's label 3^A w_t meets only z; {f1,f2,z,s}, {s1,s2}, {f1,f2,s} weigh <= 1);
a set S of weight 1 under both has (#fours in S)/4 = (#twos in S)/2, so it contains both fours or neither.
(d) PFG-t in both orientations: Gamma^alpha = F* -complement... precisely {uv : alpha_uv <= 2} = the complement of F, a
5-cycle, is connected; so Corollary L (C^alpha) gives P* := {u : alpha*_tu = 4} with |P*| >= 2. Likewise
{uv : alpha*_uv <= 2} is the complement of F*, connected, so (C^alpha*) P := {u : alpha_tu = 4} has |P| >= 2.
P cap P* = empty (INV).

## 2. The count at a vertex whose F-neighbours avoid P

Let u in W with both F-neighbours w1, w2 outside P (alpha_tw <= 2), and let w1', w2' be the other F-neighbours of w1, w2;
they are the two vertices at F-distance 2 from u, i.e. u's F*-neighbours. By 1(c) applied at w_i in C^alpha,
L_u^(w_i) = L_wi'^(w_i); Lemma TC (apex u) gives **D_wi' cap D_wi = empty** (i = 1, 2) in C^alpha at u.
At u (C^alpha, VFC; masses alpha*_uj/6, INV (b)): w1', w2' 4/6 each; w1, w2 2/6 each; z 3/6; t alpha*_tu/6. Local indices:
4w for w1', w2'; 2w for w1, w2; 3 2^E w_z and alpha*_tu 3^A w_t for z, t. A right coset containing w1' and w2' contains
neither w1 nor w2; one containing w1' but not w2' contains no w1 (and at most w2); one containing w2' but not w1' at most w1;
one containing neither holds at most two of w1, w2 (a third element z or t would give a triple with all gcds <= 2,
Sun(3)). With K the measure of the cosets containing w1' and w2': the w1'-only and w2'-only cosets have measure 4/6 - K
each and absorb at most min(4/6 - K, 2/6) of the mass of w2, resp. w1; the rest of the 4/6 two-mass needs cosets of the
last kind, two per coset. So mu(union) >= K + 2 (4/6 - K) + max(0, 2K - 4/6)/2 >= 1, contradicting V4 (the union avoids U_u).

The same argument in C^alpha* at a vertex u whose two F*-neighbours avoid P* (rows ({2,2,4,4}|3|e*) with e* <= 2 at those
neighbours, fours on F*; at u in C^alpha* the masses are alpha_uj/6: 4/6 on the F-neighbours, 2/6 on the F*-neighbours).

## 3. Proof of the theorem

On a 5-cycle, any 2-set Q has a vertex with no neighbour in Q (if Q = {p, q} is an edge, the vertex opposite to it; if
p, q are at distance 2, p itself). If |P| = 2, apply this to F and P (section 2 in C^alpha). If |P| >= 3, then |P*| = 2
(|P| + |P*| <= 5, |P*| >= 2), and apply it to F* and P* (section 2 in C^alpha*). Either way a contradiction. R0 lifts the
statement to arbitrary groups. QED

## 4. Remaining Case A

Case A configurations with a vertex whose (alpha-fours, alpha*-fours) degrees are (3,1), (1,3), (2,1) or (1,2) are NOT
covered. Example structure not covered: F = K_{2,3}, F* = {pq} plus the triangle on the 3-side (degrees (3,1) at p, q and
(2,2) on the 3-side); there Corollary L applies only in C^alpha* and the transfers from the deg-1 rows at p, q do not yet
give a contradictory count. No novelty, Lean or human-review claim.
