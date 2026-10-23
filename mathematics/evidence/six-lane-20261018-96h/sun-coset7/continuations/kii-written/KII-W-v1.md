# KII-W-v1 — written exclusion of the full KII class [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read at 2026-10-19T17:30:56-0700, immediately before this exclusive create. Owner SunM13MixedFibres.
- **Frozen scope:** `KII-W-SCOPE-v1.md` (this directory), sha256 6ed700c2b7660889c60759c55424ccd8a945c685b3bbc2c2385fa1451cb7e1e6,
  written before any derivation (it states that no pre-freeze sketch existed). **Outcome (A):** complete written proof.
- **Authority:** `RUN/control/written-slot-transitions-sun-physics-20261019-1700-v1.json`, sha256
  b29119aa12222bf31cdaf6afdb59e81bc58ad2525fa9e08c5384bf86bc7d6bf2, key "math1".
- **Status:** every new lemma and the theorem are CANDIDATE_UNVERIFIED (single author, unreviewed). This is a written
  VERIFICATION REPLACEMENT for the KII branch of StageB, not a new class closure. Independent of StageB code, certificates,
  outputs and its accepted KII conclusion (only output COUNTS were ever seen; disclosed in the scope). The K52-W candidate
  is NOT a premise; the fibre count and inversion are re-proved here. No scientific computation, enumeration, script,
  assertion, test, model CLI or nested agent; only hash/byte/range metadata for packaging. No full Sun(7), acceptance,
  novelty, Lean or human-review claim.
- Roots: O16 = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7;
  S = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7;
  RUN = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h; R16 = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review.

## 0. Target and import boundary
A *configuration* is a group G with finite-index subgroups U_j and pairwise disjoint left cosets g_jU_j, j in V, |V| = 7;
n_j = [G : U_j]. Class KII is README class line 96: a counterexample configuration (CE, README lines 33-35: all pairwise
index gcds <= 6) with a = |A_5| = 2 (A_p = {j : p | n_j}). **Theorem KII-W** (section 6): no group with finite-index
subgroups contains a KII configuration; all exponents, cofactors and marker placements are included.

| input | literal scope used here | record (sha256) and acceptance | role |
|---|---|---|---|
| CE, A_p, class KII | definitions only | O16/README.md (2a6d6d6e1dadbad522c8c8f9322c17eae719fb01fe373e6b1caf8c40cadc3fd1) lines 33-35, 96; R16/sun-coset7-written-parent-verdict-v1.md (73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35) lines 16-21, overlay A-1 (line 46) | target; the structure (R1(7)(II), README line 62) is RE-DERIVED in Lemma SHAPE |
| R0 | finite-core quotient | README lines 27-29; LFC/INV verdict item 6 | Lemma R0, proof reproduced |
| L0.1, L0.2, Lagrange | product formula, coset-intersection criterion | README lines 21-24; S/K7-LFC-INV-erratum-v1.md (7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5) E1 | Lemma MU, proofs reproduced |
| Sun(2) | coprime indices => cosets meet | README line 24 (L0.6); erratum E2 | proof reproduced in FC23 |
| Sun(3) | three disjoint left cosets in a group => a pair with index gcd >= 3 | Zhu, arXiv:0807.2207 Thm 1.1; accepted contract import (README line 15; written verdict line 60) | the ONLY non-elementary theorem used, applied inside U_c |
| LFC (a),(b), fibre construction of (c), count (d); INV (a),(b) | actual disjoint cosets; actual inversion | S/K7-LFC-INV-v1.md (45be91622b5973bf5e461d8ed08ae3e00544685d8a1728a8c3ae54738092726c) lines 20-45, 54-71, with erratum E1-E3, E6-E7; RUN/review/sun7-lfc-inv-parent-verdict-v1.md (8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18) lines 18-19, 23 | origin of FC23 and INV; both RE-PROVED in section 2 with only Sun(2), Sun(3) |
**Not used anywhere:** Sun(4), Sun(5), Sun(6), Sun(7); the general LFC(c) with Sun(t), t >= 4 (whose accepted package
records computer-assisted Sun(5)/Sun(6) provenance); VFC as a black box; T/K/P/RPLP/CAP; any StageB certificate, output,
code, engine or checker; the accepted K5.2*/KII StageB conclusion; K52-W; M-S Lemma 4.6; Menon; minimal-counterexample
frames; exponent caps; any pending candidate (K7-NF, A2X, SUN7-COMP).

## 1. Lemma SHAPE (exact raw normalisation of KII)
**Lemma SHAPE.** A labelled index tuple is a KII tuple iff, after naming the two 5-divisible vertices x, y and putting
C := V \ {x, y} (|C| = 5),
  n_x = 10 r_x,  n_y = 15 r_y,  n_c = 6 r_c (c in C),
with (S1) 3 does not divide r_x, r_y is odd, 5 does not divide r_c; (S2) gcd(r_x, r_y) = gcd(r_y, r_c) = gcd(r_c, r_c') = 1
(c != c' in C); (S3) gcd(r_x, r_c) in {1, 2} for every c in C. All exponents and prime-to-30 cofactors are otherwise free.
*Proof.* (=>) In a CE every pairwise gcd lies in [2, 6]: <= 6 by definition, >= 2 by Sun(2) (two disjoint cosets cannot
have coprime indices; FC23 below proves Sun(2)). Let A_5 = {x, y}. For j not in A_5, gcd(n_x, n_j) is in [2,6], not
divisible by 5 and has no prime >= 7 (it is <= 6), so 2 or 3 divides both; hence x in A_2 cup A_3, likewise y.
gcd(n_x, n_y) is divisible by 5 and <= 6, so it equals 5: x and y share neither 2 nor 3. They cannot both lie in A_3, so
one of them lies in A_2; call it x. Then y is not in A_2, so y in A_3, and x is not in A_3. For j in C, gcd(n_x, n_j) in [2,6] with 3, 5 not dividing it (3 does not
divide n_x, 5 does not divide n_j) forces 2 | n_j; gcd(n_y, n_j) forces 3 | n_j. So C = A_2 cap A_3 and A_5 cap C = empty:
n_x = 10 r_x (3 does not divide r_x), n_y = 15 r_y (r_y odd), n_c = 6 r_c (5 does not divide r_c). Then
  gcd(n_x, n_y) = 5 gcd(r_x, r_y), gcd(n_x, n_c) = 2 gcd(r_x, r_c), gcd(n_y, n_c) = 3 gcd(r_y, r_c), gcd(n_c, n_c') = 6 gcd(r_c, r_c'),
because in each case the displayed extra primes 2, 3, 5 divide only one side (by (S1)). The bound <= 6 gives (S2), and
gcd(r_x, r_c) <= 3 with 3 not dividing r_x gives (S3). (<=) The four identities give gcds 5, 2 or 4, 3, 6, all <= 6; A_5 = {x, y}
since 5 does not divide 6 r_c; so the tuple is a CE with a = 2, i.e. KII. QED

**Markers (index-defined).** By (S2), at most one c in C has r_c even; call it i* if it exists. Since gcd(r_x, r_c) in {1,2}
(S3), min(v_2(r_x), v_2(r_(i*))) <= 1, and gcd(r_x, r_c) = 1 for every c != i*. By (S2), at most one vertex of {y} cup C has
3 | r; call it t if it exists (3 never divides r_x). 5 divides at most one of r_x, r_y (S2) and never r_c. Write a_x := v_2(r_x) >= 0.

## 2. Elementary tools (complete proofs)
**Lemma R0.** N := intersection of the cores of the U_j is normal of finite index (each core is the kernel of the action
on the finite set G/U_j) and N <= U_j. Each g_jU_j is a union of N-cosets, so indices and disjointness pass to G/N, and the
labelled tuple is unchanged. Hence it suffices to treat finite G. (No least-order frame is used.)

**Lemma MU.** For i != j put g_ij = gcd(n_i, n_j), I_ij = [G : U_i cap U_j], alpha_ij = I_ij / lcm(n_i, n_j). Then alpha_ij is an
integer and 1 <= alpha_ij <= g_ij - 1. *Proof.* n_i, n_j divide I_ij (Lagrange), so lcm | I_ij. The multiplication map
U_i x U_j -> U_iU_j has fibres of size |U_i cap U_j|, so |U_iU_j|/|G| = I_ij/(n_i n_j) = alpha_ij/g_ij. Disjointness of
g_iU_i and g_jU_j means g_i^-1 g_j is not in U_iU_j, so this ratio is < 1. QED
In KII: alpha_(x c) = 1 whenever g_xc = 2; alpha_(y c) in {1, 2}; alpha_(c c') in {1, ..., 5}.

**Lemma INV.** Put U_j* = g_jU_jg_j^-1. The cosets g_j^-1 U_j* = (g_jU_j)^-1 are pairwise disjoint left cosets with the same
indices n_j: an actual configuration with the same labelled tuple, hence (Lemma SHAPE) a KII configuration with the same
x, y, C, i*, t. Its multipliers alpha* satisfy alpha_ij + alpha*_ij <= g_ij. *Proof.* Inversion is a bijection; conjugate
subgroups have equal index. With h = g_i^-1 g_j, conjugating by g_i^-1 gives alpha*_ij = [G : U_i cap hU_jh^-1]/lcm(n_i,n_j), and
|U_i h U_j| = |U_i||U_j|/|U_i cap hU_jh^-1|, so |U_ihU_j|/|G| = alpha*_ij/g_ij. The double cosets U_iU_j and U_ihU_j are distinct
(h not in U_iU_j), hence disjoint, and the two ratios sum to at most 1. QED. (Inverting twice returns the original.)
Consequences used: **(I1)** alpha_yc + alpha*_yc <= 3, so alpha_yc = 1 or alpha*_yc = 1; **(I2)** alpha_cc' + alpha*_cc' <= 6.

**Lemma FC23 (restricted left-fibre count; Sun(2), Sun(3) only).** Fix an apex v. For j != v put
lambda_j = [U_v : U_v cap U_j] = n_j alpha_vj/g_vj and t_j = [U_j : U_j cap U_v] = n_v alpha_vj/g_vj (index chains), and
mu_j := alpha_vj/g_vj. Call a set S of vertices != v **admissible** if every two members j, j' have gcd(lambda_j, lambda_j') >= 2
and every three members contain two with gcd >= 3. If w_j >= 0 and sum_(j in S) w_j <= 1 for every admissible S, then
  sum_(j != v) w_j mu_j <= 1 - 1/n_v < 1.
*Proof.* g_jU_j meets exactly t_j left cosets of U_v (they are g_j u U_v, u in U_j, equal iff the u's agree modulo U_j cap U_v),
none equal to g_vU_v (disjointness). For a left coset B = bU_v != g_vU_v put S_B = {j : g_jU_j meets B}. For j in S_B pick
p_j in g_jU_j cap B; then g_jU_j cap B = p_j(U_j cap U_v), and b^-1 p_j(U_j cap U_v) is a left coset in U_v of a subgroup of
index lambda_j; these cosets are pairwise disjoint. Sun(2) in U_v: if gcd(lambda, lambda') = 1 then the two subgroups H, K
satisfy |HK| = |H||K|/|H cap K| >= |U_v| (as [U_v : H cap K] is a multiple of lambda lambda'), so HK = U_v and every left coset
of H meets every left coset of K, impossible. Sun(3) (Zhu) applied in U_v to any three of the pieces gives two with
gcd >= 3. So every S_B is admissible. Summing the weight inequality over the n_v - 1 cosets B != g_vU_v counts j exactly
t_j times: sum_j w_j t_j <= n_v - 1; divide by n_v. QED. (Larger fibre sets are constrained only through their 2- and
3-subsets; neither Sun(4), Sun(5) nor Sun(6) is used.)

## 3. The apex c and its exact local gcd table
**Choice of c.** If t exists, t in C and t != i*, put c := t. Otherwise let c be any vertex of C \ {i*}. Then c != i*, and
the five other vertices split as {x, y} and the four C-neighbours of c, which are **i*** (if it exists; possibly i* = t)
and the remaining **plain** vertices p, for which r_p is coprime to 30 (r_p odd since p != i*; 3 does not divide r_p since
p != t; 5 never divides r_c). There are four plain neighbours if i* does not exist and three if it does.
**Labels and masses at v = c**, in either family Phi in {alpha, alpha*} (an actual KII configuration by INV):
- g_xc = 2 gcd(r_x, r_c) = 2 (r_c odd), so Phi_xc = 1: label X = 5 r_x, mass mu_x = 1/2.
- g_yc = 3: label Y = 5 r_y phi with phi := Phi_yc in {1, 2}, mass phi/3.
- i*: label I = r_(i*) gamma with gamma := Phi_(c i*) in {1, ..., 5}, mass gamma/6.
- plain p: label P = r_p pi_p with pi_p := Phi_(c p) in {1, ..., 5}, mass pi_p/6.
**Lemma GCD.** Any two of these labels have gcd 2^(min v_2) 3^(min v_3) 5^(min v_5), with
| label | v_2 | v_3 | v_5 |
|---|---|---|---|
| X | a_x | 0 | >= 1 |
| Y | [phi = 2] | v_3(r_y) (>= 1 iff t = y) | >= 1 |
| I | v_2(r_(i*)) + v_2(gamma) >= 1 | v_3(r_(i*)) + v_3(gamma) | [gamma = 5] |
| P | v_2(pi) | [pi = 3] | [pi = 5] |
*Proof.* The prime-to-30 parts of the labels divide r_x, r_y, r_(i*), r_p respectively; these share no odd prime ((S2),(S3)) and the
multipliers are <= 5, so only 2, 3, 5 can be common. The valuations follow from (S1), the plainness of p, and phi <= 2. QED
Consequences used below:
- **K1** gcd(X, P) = 1 for plain p with pi in {1, 3}; gcd(X, Y) >= 5.
- **K2** a plain p with pi = 1 has gcd(P, Q) = 1 for every other label Q (all its valuations are 0).
- **K3** a plain p with pi = 5 has gcd(P, Q) = 1 for every C-neighbour Q whose entry is not 5 (v_2(P) = v_3(P) = 0, v_5(Q) = 0).
- **K4** if phi = 1: gcd(Y, P) = 1 for plain p with pi in {1, 2, 4}; gcd(Y, I) = 3^[t = y and gamma = 3] 5^[gamma = 5]
  (if t = y then t != i*, so v_3(I) = v_3(gamma)).
- **K5** plain p, p' with pi, pi' in {2, 4}: gcd = 2^min(v_2 pi, v_2 pi'), which is 2 unless pi = pi' = 4.
- **K6** for plain p with pi = 2 and every gamma: gcd(I, P) = 2 (v_2(I) >= 1, v_3(P) = v_5(P) = 0) and gcd(X, P) <= 2; if gamma in
  {1, 3}, gcd(X, I) <= 2 (v_2: min(a_x, v_2(r_(i*))) <= 1; v_3(X) = 0; v_5(I) = 0). (For gamma = 5, gcd(X, I) >= 5.)

## 4. Three row lemmas (any family Phi; contradiction means FC23 at c fails)
**Lemma B (plain five).** If some plain p has pi_p = 5 and some C-neighbour q has entry e != 5, contradiction.
*Proof.* Weights w_p = w_q = 1, all others 0. By K3 no admissible set contains both, so every admissible set has weight
<= 1. Objective 5/6 + e/6 >= 1. QED
**Lemma A (odd plain).** If some plain p has pi_p = 3, or three plain p_1, p_2, p_3 have pi = 1, contradiction.
*Proof.* Weights w_x = 1 and w = 1 on that p (resp. on p_1, p_2, p_3), others 0. By K1 x is incompatible with these p, and by
K2 the three 1-entries are pairwise incompatible; so no admissible set contains two positive-weight items. Objective
1/2 + 3/6 = 1. QED
**Lemma Z (all five).** If all four entries of the row of c in Phi equal 5, then in the other family Phi' all four
equal 1 (INV (I2) and Lemma MU), and Lemma A applied to Phi' (at least three plain neighbours) gives a contradiction.

## 5. Main Lemma (phi = 1)
**Main Lemma.** Let phi = Phi_yc = 1 and suppose every plain entry lies in {1, 2, 4}, at most two of them equal to 1.
Then FC23 at c fails. Let n_1, n_2, n_4 count plain entries equal to 1, 2, 4; N := n_1 + n_2 + n_4 is 4 (i* absent) or 3.
In every weighting below, plain 1-entries get weight 1 and are singletons in every admissible set (K2); y is compatible
with no plain item (K4) and with x; it is compatible with i* exactly when gamma = 5 or (t = y and gamma = 3) (K4).
- **(M1) n_4 >= 1.** w_y = 1, w = 1/n_4 on each plain 4, w = 1 on plain 1s, all else 0. Admissible sets containing y lie in
  {x, y, i*}: weight 1. Other admissible sets carry at most the plain-4 total 1, or a single plain 1. Objective
  >= 1/3 + n_4 (1/n_4)(4/6) = 1.
- **(M2) n_4 = 0, N = 4.** Then n_2 = 4 - n_1 >= 2. w_y = 1, plain 2s 1/2, plain 1s 1, else 0. By K5 every two plain 2s have
  gcd 2, so no admissible set contains three of them (no pair with gcd >= 3). Objective 1/3 + n_1/6 + n_2/6 = 1.
- **(M3) n_4 = 0, N = 3, (n_1, n_2) = (2, 1).** w_y = 1, the plain 2 weight 1, plain 1s weight 1, else 0. Admissible sets
  with y lie in {x, y, i*}; any other carries at most one positive item. Objective 1/3 + 2/6 + 2/6 = 1.
- **(M4) n_4 = 0, N = 3, (n_1, n_2) in {(1, 2), (0, 3)}** (so n_1 + n_2 = 3 and i* exists):
  - **(M4a) gamma in {2, 4}.** w_y = 1, w_(i*) = 1/2, plain 2s 1/2, plain 1 weight 1, w_x = 0. K4: y is compatible with neither
    i* nor plain items. K5, K6: all pairs inside {i*} cup {plain 2s} have gcd 2, so admissible sets contain at most two of
    them. Objective 1/3 + gamma/12 + (n_1 + n_2)/6 = 5/6 + gamma/12 >= 1.
  - **(M4b) gamma = 1.** w_x = w_y = w_(i*) = 1/2, plain 2s 1/2, plain 1 weight 1. K4: y's only companion is x. K5, K6: all pairs
    inside {x, i*} cup {plain 2s} have gcd <= 2, so admissible sets contain at most two of them; a set with y lies in {x, y}.
    Objective 1/4 + 1/6 + 1/12 + (n_1 + n_2)/6 = 1.
  - **(M4c) gamma = 3.** w_x = w_(i*) = 1/2, plain 2s 1/2, plain 1 weight 1, w_y = 0. K6 (gamma = 3) and K5: all pairs inside
    {x, i*} cup {plain 2s} have gcd <= 2 (v_3(P) = 0 kills a common 3), so admissible sets contain at most two of them.
    Objective 1/4 + 3/12 + (n_1 + n_2)/6 = 1.
  - **(M4d) gamma = 5.** w_y = w_(i*) = 1/2, plain 2s 1/2, plain 1 weight 1, w_x = 0. A set with y lies in {x, y, i*} (weight
    <= 1). Without y, by K5, K6 all pairs inside {i*} cup {plain 2s} have gcd 2, so at most two of them occur. Objective
    1/6 + 5/12 + (n_1 + n_2)/6 = 13/12 > 1.
Each case contradicts FC23. These cases exhaust the hypothesis (n_4 >= 1; or n_4 = 0 with N = 4; or N = 3 and n_1 + n_2 = 3
with n_1 <= 2; and gamma in {1, ..., 5}). QED

## 6. Theorem KII-W
**Theorem KII-W [CANDIDATE_UNVERIFIED].** No group with finite-index subgroups contains seven pairwise disjoint left cosets
whose labelled index tuple lies in README class KII. This covers every exponent and cofactor, every position of i*, t
and of the high 5-part, and both values of every multiplier.
*Proof.* By R0 take G finite; Lemma SHAPE gives the normalisation and markers; choose c as in section 3. By (I1) one of the
two actual families Phi in {alpha, alpha*} (the configuration or its inverse, both KII with the same markers and the same
apex c) has Phi_yc = 1; work in it. If a plain entry equals 5: either some entry differs from 5 (Lemma B) or all four
equal 5 (Lemma Z, which passes to the other family). If no plain entry equals 5 and some plain entry is 3, or at least
three plain entries are 1, Lemma A applies. Otherwise every plain entry is in {1, 2, 4} with at most two 1s, and the Main
Lemma applies since phi = 1. Every case contradicts FC23. QED

## 7. Dependency DAG, Sun boundary and review checks
| node | depends on | status |
|---|---|---|
| SHAPE + markers | CE/KII definition, Sun(2), elementary gcd arithmetic | new written re-derivation of README R1(7)(II) plus the raw normalisation |
| R0, MU, INV | finite-index cores, Lagrange, product formula, coset-intersection criterion | reproduced complete proofs of accepted lemmas |
| FC23 | fibre construction, Sun(2) (proved), Sun(3) (Zhu) | new restricted count; no Sun(t) for t >= 4 |
| GCD, K1-K6 | SHAPE, MU | exact valuations; no capping |
| B, A, Z | FC23, K1-K3, INV (I2) | new |
| Main | FC23, K2, K4-K6 | new; every weight checked on all admissible sets |
| KII-W | R0, SHAPE, INV (I1), B, A, Z, Main | new, CANDIDATE_UNVERIFIED |
Acyclic. **Sun boundary: only Sun(2) (proved) and Zhu's Sun(3); no computer-assisted theorem (Sun(5), Sun(6), StageB) is
used.** If accepted, this proof would remove KII's dependence on the StageB computation. It does not by itself remove the
computer-assisted Sun(5)/Sun(6) imports of the global six-class reduction, does not cure the permanent StageB F-1 deviation,
and does not settle K5.2* (separate candidate) or any other class.
**Requested checks:** (1) SHAPE both directions; (2) apex choice: c != i*, plain neighbours have r coprime to 30, x has
multiplier 1 in both families; (3) FC23 uses only 2- and 3-subsets; (4) the valuation table and K1-K6, especially
min(a_x, v_2(r_(i*))) <= 1 and the t = y / t = i* / t = c placements; (5) every admissible set in each weighting, including sets
with zero-weight items; (6) exhaustiveness in sections 5-6 and the passage to the inverse in Lemma Z.
**Provenance.** The fibre-count and inversion method is that of the accepted LFC/INV record; the choice of a C-apex where
x has mass 1/2 and the y-centred weightings are written here. The author also wrote the K52-W candidate (similar method,
different class); nothing from it is imported. No StageB leaf, certificate or code was read; only its reported counts.
