# KDM-v1 — K7 (a2) by left-fibre counts and actual inversion: Lemma P5 and an exact obstruction [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read at 2026-10-19T18:31:45-0700, immediately before this exclusive create. Owner SunM13MixedFibres, slot math-1.
- **Authority:** `RUN/control/written-k7-direct-marker-residual-scope-v1.json`, sha256
  bfaea95f585c1a9e97eea9bd60b981d50acf3883be7f193329b65529e1eb39bb (RUN = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h).
- **Frozen scope:** `KDM-SCOPE-v1.md` (this directory), sha256 997950d867567d563b89e1dafc77d7d72f1881d174ab65eeaf64f6950f2300b0,
  frozen before any derivation. Pre-freeze sketch: none (scope section 3, which also discloses prior exposure).
- **Outcome (B): exact obstruction; (a2) is NOT closed here.** Theorem OBS gives one multiplier pattern on all 21 pairs, in
  both families, with alpha + alpha* <= 6, that passes the left-fibre count at every apex in both families (also in exact
  integer form, and also with Sun(5)/Sun(6) clauses added). So no proof of the requested short type exists. The only uniform
  consequence obtained is Lemma P5 (no unmarked multiplier 5), proved completely.

## 0. Target and import boundary
| item | kind | use |
|---|---|---|
| K7 (a2) | definition, KDM-SCOPE-v1.md section 1 (frozen from the authority) | target |
| Lagrange; product formula; finite-quotient reduction | elementary | inline |
| Sun(2) | coprime indices => cosets meet | proved inside FC |
| Sun(3), Sun(4) | Zhu, arXiv:0807.2207 Thm 1.1, literal classical scope | admissibility clauses of FC |
| FC, FCX, INV | method of the accepted K7-lane LFC/INV | RE-PROVED in section 2 with Sun(2)-Sun(4) only; the accepted package is not imported |
| Sun(5), Sun(6) clauses | pending S5W/S6W (via S56W, H5/H6; all UNREVIEWED) | only as the hypothetical strengthening FC+ in OBS(iv), to show the obstruction persists; no positive claim depends on them |
**Not used:** A2 Units 1-3 and A2X; the old long A2 arguments; accepted K7-lane lemmas (F, FG-a2, D23P, S1-S5, BRIDGE,
TRANSFER, ROW-1/2/U, M0, ...); the accepted NF and (a1) results; StageB; Sun(7); any engine, certificate, count or computation.

## 1. Setting
G is a group, U_1, ..., U_7 have finite index and g_1U_1, ..., g_7U_7 are pairwise disjoint. Replacing G by G/N, N the normal
core of U_1 cap ... cap U_7, changes no index, product set or coset relation, so G is finite. n_i = [G:U_i] = 6 r_i with the
r_i pairwise coprime, so gcd(n_i, n_j) = 6 for i != j. Put alpha_ij = alpha_ji = [G : U_i cap U_j]/lcm(n_i, n_j).
**Lemma MU.** alpha_ij is an integer in {1, ..., 5}. *Proof.* n_i and n_j divide [G : U_i cap U_j], so their lcm does.
|U_iU_j| = |U_i||U_j|/|U_i cap U_j| gives |U_iU_j|/|G| = [G : U_i cap U_j]/(n_i n_j) = alpha_ij/gcd(n_i, n_j) = alpha_ij/6.
Disjointness gives g_i^-1 g_j not in U_iU_j, so alpha_ij/6 < 1. QED
**(a2).** Distinct vertices z, t, p with r_z = 2^E w_z, r_t = 3^A w_t, r_p = 5^B w_p (E, A, B >= 1); the other four vertices
u_1, ..., u_4 are **unmarked**, r_u = w_u; all w pairwise coprime and coprime to 30 (w = 1 allowed).

## 2. Tools (complete proofs)
**Lemma INV.** The sets (g_iU_i)^-1 = g_i^-1 V_i with V_i = g_iU_ig_i^-1 are pairwise disjoint left cosets of subgroups of the
same indices: an (a2) configuration Gamma* with the same r_i and markers. Its multipliers satisfy alpha_ij + alpha*_ij <= 6.
*Proof.* Inversion is a bijection of G, and conjugate subgroups have equal index. By Lemma MU for Gamma*, alpha*_ij/6 =
|V_iV_j|/|G|, and V_iV_j = g_i(U_i h U_j)g_j^-1 with h = g_i^-1 g_j, so |V_iV_j| = |U_ihU_j|. Since h is not in U_iU_j, the
double cosets U_iU_j and U_ihU_j are distinct, hence disjoint: alpha_ij/6 + alpha*_ij/6 <= 1. QED

**Lemma FC (left-fibre count with Sun(2)-Sun(4) only).** Fix an apex v. For j != v put lambda_j = [U_v : U_v cap U_j] =
r_j alpha_vj and t_j = [U_j : U_j cap U_v] = r_v alpha_vj. Call a set S of neighbours of v **admissible** if every two members
have gcd(lambda) >= 2, every three contain two with gcd >= 3, and every four contain two with gcd >= 4 (hereditary). If w_j >= 0
and sum_(j in S) w_j <= 1 for every admissible S, then sum_j w_j alpha_vj/6 <= 1 - 1/n_v.
*Proof.* g_jU_j meets exactly t_j left cosets of U_v, none equal to g_vU_v. For a left coset B = bU_v != g_vU_v, each g_jU_j
meeting B does so in one piece p_j(U_j cap U_v) (p_j in g_jU_j cap B); b^-1 turns the pieces into pairwise disjoint left cosets
in U_v of the subgroups U_v cap U_j, of indices lambda_j. Sun(2) (if gcd(lambda, lambda') = 1, two subgroups H, K of U_v with
these indices have [U_v : H cap K] >= lambda lambda', so |HK| >= |U_v|, HK = U_v, and every coset of H meets every coset of K),
Sun(3) and Sun(4) (Zhu) applied in U_v to two, three or four pieces show that the set of j meeting B is admissible. Hence
sum_j t_j w_j = sum_B sum_(j meets B) w_j <= n_v - 1, i.e. sum_j r_v alpha_vj w_j <= 6 r_v - 1. Divide by 6 r_v. QED
(A fibre holds at most six pieces; sets of five or six are constrained only through their subsets.)
**FCX (exact form).** Let N_S be the number of cosets B != g_vU_v of U_v whose set of meeting j is S. The proof shows: N_S = 0
unless S is admissible, sum_S N_S = n_v - 1 (S = empty allowed), and sum_(S contains j) N_S = t_j for every j.
**FC+ (hypothetical strengthening).** FC/FCX with two more clauses: every five members contain two with gcd >= 5, every six
contain two with gcd >= 6. It is valid if Sun(5) and Sun(6) hold (pending S5W/S6W). It is used only in OBS(iv).
**Duality inequality.** A **cover** at v is y_S >= 0 on admissible sets with sum_(S contains j) y_S >= alpha_vj/6 for every j.
For every w as in FC, sum_j w_j alpha_vj/6 <= sum_j w_j sum_(S contains j) y_S = sum_S y_S sum_(j in S) w_j <= sum_S y_S.
So FC at v cannot fail if some cover has total <= 1 - 1/n_v.
**Gcd rule.** For neighbours j != k of v, every common prime of lambda_j and lambda_k is 2, 3 or 5: a prime q >= 7 dividing
lambda_j = r_j alpha_vj divides r_j (alpha <= 5), hence divides neither r_k nor alpha_vk. Here v_q(lambda_j) = v_q(r_j) +
v_q(alpha_vj); for unmarked j, v_2 = v_2(alpha), v_3 = [alpha = 3], v_5 = [alpha = 5]; for z, t, p add E to v_2, A to v_3,
B to v_5 respectively.

## 3. Lemma P5 (a uniform consequence)
**Lemma P5.** In neither Gamma nor Gamma* does an apex v have an unmarked neighbour j with alpha_vj = 5.
*Proof.* Let Phi be the family where this happens and Phi' the other one (alpha + alpha' <= 6 by INV). By the gcd rule
gcd(5 w_j, lambda_k) = 5 if 5 | lambda_k and 1 otherwise. If some other neighbour k has 5 not dividing lambda_k, the weights
w_j = w_k = 1 (all others 0) satisfy FC, since no admissible set contains both; the value is 5/6 + alpha_vk/6 >= 1 > 1 - 1/n_v,
a contradiction. So 5 | lambda_k for every neighbour k != j. Since 5 divides none of r_u, r_z, r_t, this forces alpha_vk = 5 for
every unmarked k and for z and t (when they are neighbours of v); p (if p != v) is unrestricted. By INV, alpha'_vk = 1 for every
neighbour k != p, and c' := alpha'_vp is in {1, ..., 5} (if p != v). In Phi' the labels are w_k (unmarked: gcd 1 with every
other label), 2^E w_z, 3^A w_t, 5^B w_p c', with gcd(z, t) = 1, gcd(z, p) > 1 iff c' is even, gcd(t, p) > 1 iff c' = 3. Put
weight 1 on every unmarked neighbour and on a set of pairwise coprime markers; such weights satisfy FC (every admissible set
has at most one positive member):
- v unmarked (3 unmarked neighbours): c' in {1, 5}: z, t, p all weight 1, value (3 + 1 + 1 + c')/6 >= 1; c' in {2, 4}: t, p,
  value (3 + 1 + c')/6 >= 1; c' = 3: z, p, value (3 + 1 + 3)/6 > 1.
- v = z: c' != 3: t, p, value (4 + 1 + c')/6 >= 1; c' = 3: p, value (4 + 3)/6 > 1.
- v = t: c' odd: z, p, value (4 + 1 + c')/6 >= 1; c' even: p, value (4 + c')/6 >= 1.
- v = p: z, t, value (4 + 1 + 1)/6 = 1.
Each value exceeds 1 - 1/n_v, contradicting FC in Phi'. QED (Only the Sun(2) clause of FC and INV are used.)

## 4. Theorem OBS (exact obstruction)
**Pattern G2** (one value per unordered pair; i != j):
| pair | alpha (Gamma) | alpha* (Gamma*) | sum |
|---|---|---|---|
| u_i u_j | 3 | 3 | 6 |
| u_i z | 3 | 3 | 6 |
| u_i t | 4 | 2 | 6 |
| u_i p | 3 | 3 | 6 |
| z t | 1 | 1 | 2 |
| z p | 3 | 3 | 6 |
| t p | 1 | 1 | 2 |
**Theorem OBS [CANDIDATE_UNVERIFIED].** Let E, A, B >= 1, and let the w be pairwise coprime and coprime to 30 with w_u >= 7
for the four unmarked u. Then:
(i) alpha, alpha* take values in {1, ..., 5}, alpha + alpha* <= 6 on every pair, and no multiplier equals 5 (so P5 holds);
(ii) at every apex v and in each family there is a cover of total c_v <= 1 - 1/n_v; by the duality inequality FC never fails;
(iii) if moreover every r_v >= 386, the exact system FCX is solvable at every apex in each family;
(iv) (ii) and (iii) also hold for FC+;
(v) hence no argument that only combines, apex by apex and in the two families, the constraints MU, FC, FCX or FC+ with
alpha + alpha* <= 6 can prove (a2) empty: G2, with suitable fibre numbers N_S, satisfies all of them.
*Proof of (ii).* Write a cover as sets with weights. All gcds follow from the gcd rule; E, A, B >= 1 are arbitrary.
- **Apex u_1** (every unmarked apex is the same up to renaming). Neighbours u_2, u_3, u_4, z, t, p.
  *Gamma:* labels 3w_k, 3*2^E w_z, 4*3^A w_t, 3*5^B w_p. Every pairwise gcd is 3 except gcd(z, t) = 3*2^min(E,2), which is 6
  or 12. Admissible: every set of size <= 3; a 4-set iff it contains z and t (no 5- or 6-set). Demands 1/2, except t: 2/3.
  Cover: {z,t,p,u_2} and {z,t,u_3,u_4} weight 1/3 each; {p,u_2,u_3}, {p,u_2,u_4}, {p,u_3,u_4}, {u_2,u_3,u_4} weight 1/18 each.
  Coverage: z, t: 2/3; p and each u_k: 1/3 + 3/18 = 1/2. Total c = 2/3 + 4/18 = 8/9.
  *Gamma*:* label of t is 2*3^A w_t; gcd(z, t) = 6, all other gcds 3; same admissible sets. Demands 1/2, except t: 1/3.
  Cover: the same two 4-sets with weight 1/4, the same four triples with weight 1/12. Coverage: z: 1/2; t: 1/2; p and each
  u_k: 1/4 + 3/12 = 1/2. Total c = 1/2 + 1/3 = 5/6.
- **Apex z, Gamma and Gamma* (identical rows).** Neighbours u_1..u_4 (alpha 3), t (1), p (3); labels 3w_k, 3^A w_t, 3*5^B w_p.
  Every pairwise gcd is 3, so the admissible sets are exactly those of size <= 3. Demands 1/2, except t: 1/6. Cover:
  {t,u_1,u_2}, {t,u_3,u_4} weight 1/12; the six triples {p,u_k,u_l} weight 1/12; the four triples {u_k,u_l,u_m} weight 1/18.
  Coverage: t: 2/12 = 1/6; p: 6/12 = 1/2; each u_k: 1/12 + 3/12 + 3/18 = 1/2. Total c = 2/12 + 6/12 + 4/18 = 8/9.
- **Apex p, Gamma and Gamma*.** Neighbours u_1..u_4 (3), z (3), t (1); labels 3w_k, 3*2^E w_z, 3^A w_t; every pairwise gcd is 3
  (gcd(z, t) = 2^0 3^1). This is the apex-z row with z in the role of p: the same cover, total c = 8/9.
- **Apex t.** *Gamma:* neighbours u_1..u_4 (4), z (1), p (1); labels 4w_k, 2^E w_z, 5^B w_p. gcd(u_k, u_l) = 4,
  gcd(u_k, z) = 2^min(E,2), and lambda_p is coprime to the others. Admissible: {p} and every subset of {z, u_1, ..., u_4} (pairs
  have gcd >= 2; three or four of them contain two u's, gcd 4). Demands u_k: 2/3, z and p: 1/6. Cover: {z,u_1,u_2,u_3,u_4}
  weight 2/3, {p} weight 1/6. Total c = 5/6.
  *Gamma*:* neighbours u_k (2), z (1), p (1); labels 2w_k, 2^E w_z, 5^B w_p. Inside {z, u_1, ..., u_4} every gcd is 2, so only
  singletons and pairs are admissible; p is isolated. Demands u_k: 1/3, z and p: 1/6. Cover: {u_1,u_2}, {u_3,u_4} weight 1/4;
  {z,u_1}, {z,u_3}, {u_2,u_4} weight 1/12; {p} weight 1/6. Coverage u_k: 1/4 + 1/12 = 1/3; z: 1/6. Total c = 11/12.
- **Bounds.** n_u = 6w_u >= 42, n_z >= 12, n_t >= 18, n_p >= 30, so 1 - 1/n_v >= 41/42, 11/12, 17/18, 29/30 >= c_v
  (c = 8/9 and 5/6 at u; 8/9 at z and p; 5/6 and 11/12 at t). w_u >= 7 is needed only at u in Gamma (8/9 > 5/6 = 1 - 1/6).
*Proof of (iii).* Fix v and a family, with cover y of total c <= 11/12. Trim y to exact coverage without changing its total:
while some j is over-covered, move weight from a set S containing j to S minus j (admissibility is hereditary; the empty set
is allowed). Let y' be the result, with support F (at most 64 subsets of the six neighbours) and K = sum over S in F of |S| <=
6*2^5 = 192. Put N_S = floor(6 r_v y'_S) for S in F. Since sum_(S contains j) 6 r_v y'_S = r_v alpha_vj = t_j, the deficit
d_j = t_j - sum_(S contains j) N_S is an integer with 0 <= d_j < #(S in F containing j); add d_j fibres of type {j} and let
the rest be of type empty. The fibres used number at most 6 r_v c + K <= 6 r_v - 1 when 6 r_v (1 - c) >= K + 1, which holds for
r_v >= 386 because 1 - c >= 1/12. All constraints of FCX hold. QED (iii)
*Proof of (iv).* FC+ differs from FC only on sets of size >= 5. The only such set used above is {z,u_1,u_2,u_3,u_4} at t in Gamma
(its gcds are <= 4, so FC+ forbids it). Replacement cover there: {u_1,u_2,u_3,u_4} weight 13/24; the four sets {z} + (three of
the u_k) weight 1/24 each (admissible: any three of the five members contain two u's, any four contain a gcd-4 pair);
{p} weight 1/6. Coverage u_k: 13/24 + 3/24 = 2/3; z: 4/24 = 1/6. Total 7/8 <= 17/18. The rounding of (iii) applies
unchanged. QED (iv)
*Proof of (v).* By (i)-(iv) the numbers alpha, alpha*, r_v and N_S satisfy every listed constraint at once, for infinitely many
parameter choices allowed by (a2). A derivation of a contradiction from those constraints alone is therefore impossible. QED

## 5. Where the short argument stops (exact local multiplier/marker obstruction) and failed routes
**Mechanisms that keep G2 alive.**
- **(M-a) Self-dual 3-cliques at z and p.** All six labels are divisible by 3 with every pairwise gcd exactly 3. FC caps a fibre
  at three pieces, so five neighbours of mass 1/2 and one of mass 1/6 need only 8/9. Multiplier 3 is self-dual under INV
  (3 + 3 = 6), so the same row survives in Gamma*. The light sixth member is the 3-marker t at multiplier 1: its home prime 3
  keeps it in the clique.
- **(M-b) The z-t bridge at an unmarked apex.** With z at multiplier 3 and t at multiplier 4 (Gamma) or 2 (Gamma*),
  gcd(lambda_z, lambda_t) is 6 or 12, so 4-sets {z, t, x, y} are admissible. Without a pair of gcd >= 4, triples only would
  cover the Gamma-row (total demand 19/6) with total >= 19/18 > 1. The marker pair (2-marker times multiplier 3, 3-marker times
  an even multiplier) is exactly what saves the unmarked apex.
- **(M-c) 4-block and 2-matching at t.** Unmarked neighbours at multiplier 4 share gcd 4 and fit in one fibre (5/6). Their INV
  partners at multiplier 2 form a fractional perfect matching (11/12). z and p at multiplier 1 are light: z joins the 2-adic
  block and p is isolated.
**Failed routes.**
- F1 (single-apex count plus INV at one apex): every apex type has a surviving row pair, namely the rows of G2.
- F2 (marker-free count at p): weights on unmarked neighbours only (C56W-template standard weights) kill every unmarked
  multiset at p except 17 (value 4/6: {1,1,1,1}, {2,2,2,2}, {3,3,3,3}, {4,4,4,4}, {2,2,4,4}, {2,4,4,4}, {1,3,3,3}, {1,2,2,2},
  {1,1,2,2}; value 5/6: {2,2,2,4}, {1,1,3,3}, {1,1,1,2}, {1,4,4,4}, {1,2,4,4}, {1,2,2,4}, {2,3,3,3}, {2,2,3,3}). Adding z
  and t leaves survivors, e.g. G2's p-row ({3,3,3,3}, alpha_pz = 3, alpha_pt = 1).
- F3 (M0-type parity, ">= three 4s at every vertex in both families, hence a 3-regular graph on 7 vertices"): no such row
  lemma follows from FC + INV, because G2's rows at z and p contain no 4 in either family.
- F4 (adding Sun(5)/Sun(6), pending S5W/S6W): G2 survives (OBS(iv)).
- F5 (exact integer fibre equations instead of FC): no extra power once every r_v >= 386 (OBS(iii)).
- F6 (small cofactors): for w_u = 1 the u-row of G2 in Gamma fails FC (8/9 > 5/6), but (a2) contains all cofactors, so this
  cannot prove (a2) empty.
**What a proof must add.** Information invisible to single-apex index-gcd fibre counts and alpha + alpha* <= 6: relations
between multipliers at different apexes (for example through intersections of three subgroups) or the structure of the
subgroups U_v cap U_j inside U_v beyond their indices. Not examined; no claim about which ingredient suffices.

## 6. Dependency DAG, review checks, non-claims
| node | depends on | status |
|---|---|---|
| MU, INV | Lagrange, product formula, finite quotient | reproduced complete proofs |
| FC, FCX | fibre construction; Sun(2) (proved); Sun(3), Sun(4) (Zhu) | re-proved; no Sun(5)/Sun(6) |
| P5 | FC (Sun(2) clause only), INV, gcd rule | new, CANDIDATE_UNVERIFIED |
| OBS (i)-(iii), (v) | gcd rule, explicit covers, duality inequality, rounding | new, CANDIDATE_UNVERIFIED |
| OBS (iv) | FC+ as a hypothesis only (pending S5W/S6W are not asserted) | new, CANDIDATE_UNVERIFIED |
Acyclic. **Computation boundary: none.** Every value above is a hand computation written in this file.
**Requested checks:** (1) the (a2) target and markers as frozen; (2) MU and INV, alpha + alpha* <= 6; (3) FC uses only 2-, 3-
and 4-subsets, FCX bookkeeping; (4) P5 for all four apex types and every parity of c'; (5) every gcd in section 4 for all
E, A, B >= 1 (in particular gcd(z, t) at u: 6 or 12 in Gamma, 6 in Gamma*; 3 at p); (6) admissibility of every cover set,
including the 4-sets at u (they contain z and t) and the 5-set at t; (7) every coverage and total; (8) 1 - 1/n_v >= c_v;
(9) the trimming/rounding argument of (iii); (10) the FC+ replacement cover; (11) the F2 list (35 multisets of four values in
{1,2,3,4} checked by hand).
**Non-claims.** (a2) is neither proved empty nor non-empty. G2 is a multiplier pattern, not a group configuration; nothing
is claimed about its realizability. No claim that triangle-type or inner-subgroup arguments close (a2), and no claim about
A2X (still pending; this file neither supports nor replaces it, apart from P5 as an alternative written proof of the
statement "no unmarked 5"). CANDIDATE_UNVERIFIED; no acceptance, novelty, Lean, human-review or Sun(7) claim; StageB's F-1 is
not cured.
