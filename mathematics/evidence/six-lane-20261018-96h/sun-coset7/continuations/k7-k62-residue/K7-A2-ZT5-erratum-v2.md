# K7-A2-ZT5-erratum-v2: the gap of item ZA.1 is closed by Lemma ZW; Theorem K7-ZT5-A is reinstated (conditional)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T08:01:37-0700.
- **Owner:** Sun7K62Successor. Author's own repair; no computation.
- **Overlays (frozen, not modified):** `K7-A2-ZT5-A-v1.md` 4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919; `K7-A2-ZT5-erratum-v1.md`
  82d01721688ad10dfa44ed01aca0b914c515f0c508e24345587e063c6dca6dc4 (whose withdrawal ZA.1/ZA.2 is hereby superseded; ZB.1, ZB.2, MAP.2 stay in force).
- **Status:** the new Lemma ZW is a **materially new proof step** and must be reviewed with the A2-side package.

## Lemma ZW (alpha*-side in (a2-zt5) with T* = W) [NEW]

In (a2-zt5) with T* = W (notation of K7-A2-ZT5-A): **(i)** an alpha*-row at u in W with a W-entry 3 has W-part (3,3,1,1),
(3,3,2,2), (3,3,3,1), (3,3,3,2) or (3,3,3,3) (in particular no W-entry 4), and for (3,3,1,1), (3,3,2,2) also
alpha*_ut <= 3; **(ii)** alpha* has no W-entry 3; **(iii)** alpha*_ut != 3 for u in W. Hence every W-W and W-t entry of
alpha* lies in {1,2,4}.

*Proof.* (i) At u in C^alpha* the labels are 3w (W-threes), e w (other W-entries e in {1,2,4}), 3 2^E w_z (z, as
c* = 3) and e* 3^A w_t (t). All weights below vanish on z, and on t unless stated, so Lemma FG-zf (a) bounds their
values by 5. A three-label is coprime to every non-three W-label. k3 = 1: y = 1 on the three plus the E8 standard weights
on the other three neighbours (value >= 3): value >= 6. k3 = 2, others b1, b2: y = 1/2 on the threes plus the standard
weights on {b1, b2}: 3 + 2, 3, 5, 2, 3, 4 for (1,1), (1,2), (1,4), (2,2), (2,4), (4,4); only (1,1), (2,2) are <= 5.
k3 = 3, other b: y = 1/3 on the threes and y_b = 1: 3 + b, so b != 4. For (3,3,1,1) and (3,3,2,2) the weights (threes 1/3,
t 1/3, ones 1 resp. twos 1/2) are feasible ({threes, t} has pairwise gcd 3; {s, s', t} has all gcds 2; a three never meets
a one or a two) of value 4 + alpha*_ut/3, so alpha*_ut <= 3 (FG-zf with y_z = 0).
(ii) Let Theta* := {uv in W : alpha*_uv = 3} and suppose it is non-empty. For uv in Theta* and w in W \ {u, v} the
alpha*-triangle {u, v, w} has entries (3, alpha*_uw, alpha*_vw); if neither is 3, both lie in {1,2,4} and the triangle
passes only as (3, 4, 4) (computation of A1-STRUCT Corollary W3; ell's of W-vertices are odd and prime to 3), which gives u
a W-four besides a W-three, against (i). So every w is Theta*-adjacent to u or v; with (i), every vertex of W has
Theta*-degree >= 2, and degree 4 is impossible (alpha <= 3, hence alpha in {1,2}, on all four W-pairs at u - alpha has no
W-three by the proof of Lemma ZS - and Lemma B for alpha-rows forces a four). The domination property says that two
non-Theta* pairs wu, wv force uv not in Theta*, so the complement of Theta* in W is a disjoint union of cliques, each of
size >= 2 (Theta*-degrees <= 3): it is K3 + K2, i.e. Theta* = K(A, B) with |A| = 3, B = {d, e}. For d in B the alpha-entries
towards A are <= 2, so Lemma B gives alpha_de = 4 and alpha_td = 4, hence alpha*_td <= 2, and the alpha-triangles
(4, alpha_da, alpha_ea) force alpha = 2 on A x B. Then Gamma^alpha contains A x B and is connected, and Corollary L
("at least two entries 4") in C^alpha gives two vertices with alpha*_t = 4, necessarily in A. But each a in A has
Theta*-degree 2, so its alpha*-row is (3,3,1,1) or (3,3,2,2) and alpha*_ta <= 3 by (i). Contradiction; Theta* is empty.
(iii) By (ii) the W-labels at u are 2^i w; if alpha*_ut = 3, t's label 3^(A+1) w_t is coprime to all of them and meets
only z; the standard weights on the four W-neighbours (>= 4), y_z = 0, y_t = 1 give value >= 7 > 5 (FG-zf). QED

## Reinstatement

Item ZA.1 of erratum-v1 is superseded: **Theorem K7-ZT5-A is reinstated as a conditional candidate**, its audit being read
with the additional first step "by Lemma ZW, every W-W and W-t entry of alpha* lies in {1,2,4} (Corollary W3 and Lemma E3
for alpha* in the (a1) sources)". Item ZA.2 (scope) is superseded accordingly. In the closure map, edge E-a2-7 reads
again "pending, review (3)", now with Lemma ZW as part of it; in the A2 review package, Lemma ZW is added to the files
under review. ZB.1, ZB.2 and MAP.2 of erratum-v1 stay in force.
