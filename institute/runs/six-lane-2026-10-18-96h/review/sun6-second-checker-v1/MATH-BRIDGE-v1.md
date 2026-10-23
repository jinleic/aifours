# Sun6 second checker v1: mathematical bridge and every-rule source map

- Clock (/bin/date immediately before writing): 2026-10-19T17:35:10-0700
- Checker: `code/sun6_second_checker_v1.py`, sha256 `1a092d0c1eca40f1939e83ebf1ddaac02cf7888c1d83601ae20450efd7bd704f` (not executed).
- Sources (read; hashes in READLOG-v1.json): README (R0, R1(6)), rules-k6-v1 (L0-L8), rules-k6-v2 (L9), rules-k6-v3 (L10-L12 + formats), proof-k6-lemmas-v1, rules-k6-erratum-v3 (C1-C22), CERT-FORMAT-k6-v3 (sections 0-4, 6), ACCEPTANCE-AMENDMENT-v1 (overlay), proof-k6-v3 (composition).
- Scope: this note states, for every predicate the checker decides, which written lemma turns it into "no configuration has this labelled pattern", and why the integer/rational decision is exact for EVERY admissible tau and EVERY pairwise-coprime cofactor vector with the given marker statuses. It does not re-prove the cited lemmas; they are imports (section 9). No new theorem, no novelty claim.

## 0. Notation used by the code

Vertices 0..5; `A[i][j]` = alpha_ij in {1,2,3,4} (L0.3: 1 <= alpha <= gcd - 1 = 4). A type is (e2, c2, e3). For a vertex z the code uses `r2(z)` in {0, 1, SAT} (v2(r_z) = 0; = 1 for E2 class 1; >= 2 for E2 class 2) and `r3(z)` in {0, SAT} (3 | r_z iff z = E3); SAT = 64. Sizes are in units of |G|.

## 1. Chain of the conclusion (what a PASS would mean)

1. R0 (README section 2): any counterexample in an arbitrary group gives one in a finite quotient with the same indices and disjointness.
2. Least-order frame (README section 2; C4, C15, C18): choose a finite counterexample G of minimal order; every proper subgroup satisfies Sun(6); Sun(k<=4) holds (Zhu Theorem 1.1, L0.6); Sun(5) holds (accepted import, section 9). By R1(6) G carries a Core5(6) configuration: indices 5r_i with pairwise coprime r_i and pairwise disjoint cosets.
3. Pattern: alpha_ij = [G:U_i cap U_j]/(5 r_i r_j) in {1..4}, plus markers E2 (with class), E3, E5 (any may coincide, C7).
4. Placement reduction (checker `placement_reduction`): all 13 x 7 = 91 placements of (E2 with class, E3) are mapped by some permutation in S6 onto exactly one of the 8 types. Relabelling vertices maps configurations to configurations, so every pattern is the image of a labelled pattern of one of the 8 types. E5 is not part of the type; see section 8.
5. Triangle rule T (section 2): a labelling with a T-failing triangle has no configuration. The checker enumerates EXACTLY the T-consistent labellings of each type (prunes only at completed triangles; every one of the 20 triangles is tested once; schedule self-checked).
6. Coverage (checker `check_coverage`): the stabiliser of the type (all p in S6 fixing e2 and e3 when present; sizes 720/120/24 asserted) maps the type to itself and preserves every rule; the union of the stabiliser orbits of the listed representatives must EQUAL the enumerated leaf set, orbits pairwise disjoint (no duplicate), every rep a leaf. Hence every T-consistent labelled pattern is the image of a listed rep.
7. Per-line rule checks (sections 3-7): each rep's witness, verified exactly, shows that rep admits no configuration in a least-order counterexample; relabelling transfers it to the whole orbit.
8. Hence no least-order Sun(6) counterexample carries Core5(6); by step 2 no least-order counterexample exists; so Sun(6) holds for all finite groups and, by R0, all groups (C18 form). The checker verifies steps 4-7 only.

## 2. Rule T (rules-k6-v1 L1; CERT-FORMAT 2) - `tri_bounds`, `t_consistent`, `triangle_tables`

- (T1) I_xy | L tau with L = 5 r_a r_b r_c (coprime r) gives alpha_xy | r_z tau, i.e. alpha_xy / gcd(alpha_xy, r_z) | tau. So tau is a multiple of tau_min = lcm of the three quotients.
- (T2)+(T3) give tau <= alpha_xy alpha_xz at each apex, so tau <= tau_max = min over the three vertices of the product of the two alphas there (= product of the two smallest).
- T-kill: tau_min > tau_max leaves no admissible tau (C9: "admissible" means satisfying these necessary constraints).
- Exactness for every cofactor: alpha in {1..4} has only primes 2, 3. gcd(alpha, r_z) = 2^min(v2(alpha), v2(r_z)) 3^min(v3(alpha), v3(r_z)). v2(r_z) is 0 unless z = E2 (exactly 1 for class 1, >= 2 for class 2) and v2(alpha) <= 2, so SAT = 64 gives the true value; v3(r_z) >= 1 iff z = E3 and v3(alpha) <= 1. This reproduces the L1 table for every instance (r_z = 1, prime powers, primes >= 7 included).

## 3. K (rules-k6-v1 L3, K1; CERT-FORMAT 3 "K", 6.7) - `verify_K`

- Predicate: S duplicate-free subset of N = V minus v; sum_(i in S) alpha_iv >= 5; for every pair {i,j} in S: tau_min(i,v,j) == alpha_iv alpha_vj.
- Bridge: for a T-consistent rep, tau_min <= tau <= tau_max <= alpha_iv alpha_vj (product at v), so the equality pins tau = alpha_iv alpha_vj for EVERY admissible tau (M1). By (T3) at apex i, |U_i(U_v cap U_j)| = tau/(5 alpha_vj) = alpha_iv/5 = |U_iU_v|, so L2 gives U_vU_i subset U_jU_i: the L3 pair condition. L3 then forces sum alpha_iv/5 <= 1 - 1/(5 r_v) < 1, i.e. sum <= 4, contradicting sum >= 5.
- Cofactors: only tau_min (section 2) and alphas are read. E5 irrelevant (C19). Imports: none beyond L0-L3.

## 4. P: Ppair and PB (rules-k6-v1 L4; C13; CERT-FORMAT 3, 6.7) - `p_bounds`, `verify_Ppair`, `verify_PB`

- X_j = U_vU_j, |X_j| = x_j = alpha_vj/5 (P1). |X_j cap X_k| is a union of (U_v, U_j cap U_k) double cosets (L0.5), each of size a multiple of 1/gcd(5 r_v, 5 r_j r_k alpha_jk) = 1/(5 gcd(r_v, alpha_jk)) =: u (L0.4; r_v coprime to r_j r_k). gcd(r_v, alpha_jk) is the section-2 value at z = v: exact for every instance.
- Lower bound (P3): U_v(U_j cap U_k) is inside the intersection and has size tau_vjk/(5 alpha_jk) >= tau_min/(5 alpha_jk) for every admissible tau (M1); also x_j + x_k - 1 and 0. lo = u ceil(Lb/u) is valid because the intersection is a multiple of u.
- Upper bound: min(x_j, x_k) rounded down to a multiple of u. If that equals min(x_j,x_k), equality would force X_j subset X_k (x_j < x_k), X_k subset X_j (x_k < x_j), or X_j = X_k (equal); by K2 (L3 at j with S = {v,k} using U_jU_v subset U_kU_v) X_j subset X_k needs alpha_vj + alpha_kj <= 4 (and symmetrically). When barred, the intersection is a strictly smaller multiple of u, so hi drops by u. The optional XE strengthening C21 is NOT used.
- Ppair: lo > hi leaves no value for |X_j cap X_k|.
- PB: union of Y_j = G minus X_j (j in S) avoids U_v (U_v subset every X_j), so its size is < 1; Bonferroni gives sum |Y_j| - sum |Y_j cap Y_k| <= |union| < 1 with |Y_j cap Y_k| = 1 - x_j - x_k + |X_j cap X_k| <= 1 - x_j - x_k + hi. So value >= 1 is impossible. The checker also enforces the format's precondition lo <= hi on every pair of N (if it failed, a Ppair would apply; enforcing it can only cause a fail-closed rejection).
- E5 irrelevant (alpha has no factor 5; C19).

## 5. RLP (rules-k6-v1 L7; rules-k6-v2 L9(b); C3, C10, C17; CERT-FORMAT 3 "RLP", 6.4) - `verify_RLP`, `check_q_dual`, `dual_condition`, `allowed_masks`

- Translate g_v = 1; D_j = U_v g_j U_j. (R1) D_j cap U_vU_j empty; (R2) |D_j| is a positive multiple of 1/gcd(5r_v,5r_j) = 1/5; so |D_j| = q_j/5 with 1 <= q_j <= 5 - alpha_vj, and d_j = |D_j|/|U_j| = q_j r_j. The true configuration has one such q (unknown), so EVERY q in the product is checked (itertools.product order, first neighbour slowest; key recomputed from (q, statuses)).
- Right U_v-cosets C partition G; mu(S) = mass of cosets with S_C = S (non-empty). Coverage sum_(S contains j) mu(S) = q_j/5; total <= 1 - |U_v| < 1 (U_v is in no D_j by R1).
- Support: by L9(b) (pieces in C, right-translated and inverted, are pairwise disjoint left cosets in U_v of indices d_l; Sun(|T|) in U_v for |T| <= 5) mu(S) > 0 only if every T subset of S, |T| >= 2, has a pair with gcd(d_x, d_y) >= |T| (|S| = 1 always allowed).
- maxgcd is the TRUE gcd for every instance: primes >= 5 cannot divide two d's (q <= 4, r's coprime); v2(gcd) = min(v2(q_x) + v2(r_x), v2(q_y) + v2(r_y)) with at most one E2; class 1 contributes exactly 1; for class 2, v2(r) >= 2 >= v2(q_partner), so the minimum is the partner's exponent, reproduced by SAT; likewise for 3 with E3 (v3(q) <= 1 <= v3(r_E3)). So the allowed family computed is exactly the family L9(b) permits, for every instance with the given markers (C5, C16 and proof-k6-lemmas-v1 section 1).
- Weak duality: if y >= 0, sum_(x in S) y_x <= 1 on EVERY allowed S, and sum (q_x/5) y_x >= 1, then total mass = sum_S mu(S) >= sum_S mu(S) sum_(x in S) y_x = sum_x y_x q_x/5 >= 1, contradiction. (With equality coverage y >= 0 is not mathematically needed; the checker enforces it because the format requires it - fail-closed.)
- Every used key is checked against all 31 non-empty subsets; results are memoised only by (q tuple, status tuple), which determine the check completely. Unused duals carry no weight and are counted.
- E5 irrelevant (C19). Imports: L0.6, Zhu (|T| = 3,4), Sun(5) (|T| = 5). Sun(6) never used (at most five pieces).

## 6. RPLP (rules-k6-v3 L12; proof-k6-lemmas-v1 section 4; CERT-FORMAT 3, 6.4, 6.5) - `rplp_frame`, `verify_RPLP`

- For each q (same enumeration as RLP): either ["R", key] whose key equals the recomputed key and whose dual passes section 5 (then that q is already impossible), or ["P", vec] with 30 exact rationals.
- Right U_v-cosets get types (A_C, S_C), A_C = {j : C subset Y_j}, S_C = {j : C subset D_j} subset A_C (R1). x(A,S) >= 0 masses on A non-empty; cosets with A empty lie in the intersection of the X_j and are excluded; total = |union Y_j| <= 1 - |U_v| < 1.
- Forced ORDERED pairs (w,j): tau_min(v,w,j) >= alpha_vw alpha_wj (product at w) pins tau = alpha_vw alpha_wj (T2 at w); (T3) at v gives |U_v(U_w cap U_j)| = alpha_vw/5 = |X_w|, so X_w subset X_j, Y_j subset Y_w: no coset has j in A and w not in A. Columns violating this have zero mass and are omitted; (w,j) and (j,w) are tested separately.
- Constraints: E1_j: sum_(S contains j) x = q_j/5; E2_j: sum_(A contains j) x = (5 - alpha_vj)/5; B_jk: ylo <= sum_(A contains j,k) x = |Y_j cap Y_k| <= yhi with ylo/yhi = 1 - (alpha_vj + alpha_vk)/5 + lo/hi from section 4 (valid for every admissible tau and instance).
- S must be empty, a singleton, or hereditary-allowed with maxgcd for this q (section 5).
- Weak duality: with a, b free and u, l >= 0, if every admitted column has coefficient sum_S a + sum_A b - sum_(p in A) u + sum_(p in A) l <= 1 and the objective sum a q/5 + sum b (5 - alpha)/5 - sum u yhi + sum l ylo >= 1, then sum x >= 1 for every feasible x, contradicting total < 1; an infeasible system is covered by the same check through Farkas (proof-k6-lemmas-v1 section 4).
- E5 irrelevant (C19). Imports as RLP.

## 7. FH5 (rules-k6-v1 L5, L6, L8; rules-k6-v2 L9(a); C2, C4, C6, C15, C16; CERT-FORMAT 3, 6.3) - `verify_FH5`, `fh5_search`

- Hypotheses checked: a != b, alpha_ab = 1, V recomputed as {v not in {a,b} : alpha_va = alpha_vb} equals the witness set (duplicate-free) and is non-empty.
- H5/L6: H := U_aU_b is a subgroup of index m = 5 containing U_a and U_b, and t_v = [U_v : U_v cap H] = alpha_va for v in V (t_v = 1, i.e. U_v subset H, when alpha_va = 1). H < G because [G:H] = 5.
- F1: g_lU_l meets exactly t_l left cosets of H (1 <= t_l <= 5). Cosets of H are labelled 0..4 up to relabelling; a meets one coset, fixed to 0 (only a is fixed, C6). Domains: b and V-vertices with alpha_va = 1: all 5 singletons; V-vertices with alpha_va = c > 1: all C(5,c) c-subsets; every other vertex: all 31 non-empty subsets with t = size.
- Rejection (both conditions are necessary in any configuration):
  - (F3) U_i subset H (t_i = 1) gives |U_iU_l| <= |HU_l| = t_l/5, i.e. alpha_il <= t_l.
  - (F2) with L9(a): the pieces of the cosets meeting a coset C of H, left-translated into H, are pairwise disjoint cosets of U_l cap H of index lambda_l = r_l t_l; every T subset of the members with |T| >= 2 needs a pair with gcd(lambda) >= |T|: Sun(2) = L0.6, Sun(3), Sun(4) = Zhu, Sun(5) = accepted import, Sun(6) = minimality of G applied to the proper subgroup H (THIS IS THE ONLY USE OF SUN(6), and it is valid only in the least-order frame of section 1).
- fgcd is the true gcd for every instance: t <= 5 so primes >= 7 cannot be common; class-1 E2 exact; class-2 E2 v2(r) >= 2 >= v2(t); E3 v3(r) >= 1 >= v3(t); E5 v5(r) >= 1 >= v5(t); SAT = 64 reproduces each minimum (C16; SAT5 >= 1 required and used).
- E5: the 7 placements None, 0..5 are all searched (E5 is not part of the type; an instance has at most one E5 vertex, possibly coinciding with E2/E3). [Observation, not used by the checker: since t_a = t_b = 1, a and b lie in distinct cosets (their lambdas are coprime), and a t = 5 vertex would meet both, needing gcd >= 2 with both; at most one of them can be E5, so no t = 5 vertex survives and E5 never changes an FH5 outcome here. The checker still runs all 7 placements as required.]
- Completeness: depth-first search over the full product of domains; a partial assignment is cut only when a rejection condition already holds, and both conditions persist under extension (F3 involves two assigned vertices; a failing subset T stays in the growing member set), so every completion is rejected. Exact accounting: (rejected-node weights = product of remaining domain sizes) + (complete assignments reached) must equal the domain product; any complete unrejected assignment is reported as FH5_SURVIVING_ASSIGNMENT. The engine's `counts` are informational only.

## 8. N26 (rules-k6-v3 L11; proof-k6-lemmas-v1 section 3; C11, C14, C19; CERT-FORMAT 3, 6.6) - `verify_N26`

- Predicate: v != E2; alpha_vj = 2 for all j != v; alpha_jk in {2,4} for all neighbour pairs; if v = E3: tau_max(j,k,l) < 3 tau_min(j,k,l) for every neighbour triple.
- Bridge: hypotheses (i)-(iii) are checked literally; (iv) gcd(r_v, tau_jkl) = 1: by C14 every admissible tau of a neighbour triangle is in {2,4,8,12,16} (a multiple of tau_min in {2,4} that is <= tau_max in {4,8,16}), so only 2 and 3 can divide it; r_v is odd (v != E2); if v != E3 then 3 does not divide r_v (covers r_v = 1, v = E5, primes >= 7, prime powers); if v = E3, tau_max < 3 tau_min leaves only tau in {tau_min, 2 tau_min}, powers of 2. Then L11 gives a contradiction.
- E5 irrelevant (covered by C14 consequence and C19).

## 9. Imports and dependencies stated literally

| Import | Where used by a certificate the checker accepts | Status |
|---|---|---|
| R0, R1(6), least-order frame | conclusion (section 1) | written, reviewed (README; C1, C12, C18); not checked by code |
| L0-L4, L6 (H5), L7 R1-R5', L9, L10-L12 written proofs | sections 2-8 | written, reviewed; imports |
| L0.6 (Sun(2)) | every hereditary test with |T| = 2 | classical |
| Zhu Theorem 1.1 (Sun(3), Sun(4)) | hereditary tests with |T| = 3, 4 | published import |
| Sun(5) in every group | hereditary tests with |T| = 5 (RLP/RPLP supports, FH5 cosets) and R1(6) p = 2 branch | accepted verdict 2cf0243687714e42d128b7cfd65c19ce538d7a73a603b1e027a5ae04d7065301 (sun-coset5 proof-v4 + erratum v3). That result is itself computer-assisted (including its S-D handling); THIS CHECKER DOES NOT re-verify or remove the Sun(5) computation; its second checker is a separate gate. |
| Sun(6) in proper subgroups | FH5 cosets with |T| = 6 only | valid only in the least-order counterexample frame (H < G) |

## 10. What the checker does NOT establish

- It does not verify the written lemmas, R0/R1(6), Zhu or Sun(5); it verifies that the pinned finite certificate set satisfies the written predicates exactly and covers the full labelled universe.
- It does not use the engine `code` field, run.json pruned_nodes/seconds or FH5 counts for any decision.
- A PASS is single-kernel CPython evidence with trusted OS/hardware; no Lean or formal kernel.
- No interface was found that could not be derived from the sources; no HOLD is raised at source level. The real-data outcome is unknown until an admitted run.
