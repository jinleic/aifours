# C5W-v1 — a written Core(5) theorem: every Core(5) pattern is impossible (no finite bridge, no S-D step) [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read at 2026-10-19T17:41:42-0700, immediately before this exclusive create. Owner SunM13MixedFibres.
- **Frozen scope:** `C5W-SCOPE-v1.md` (this directory), sha256 3daa4a45e36530c3d66e7e4b02cf3f6b4fd69365716b68c5b7ff2f4cde57a24f, written
  before proof-v4/erratum v3 were read and before any derivation (no pre-freeze sketch). **Outcome (A)**, in the stronger
  form: no pattern survives, so the S-D class is empty without using the S-D refutation of proof-v4 section 6.
- **Authority:** `RUN/control/written-slot-transitions-sun5-moq-corner-20261019-1735-v1.json`, sha256
  59e3fb4319f20f578e8d504682343421d82bbc094e33eace85c996b3c261a7ca, key "math1".
- **Status:** CANDIDATE_UNVERIFIED (single author, unreviewed). A WRITTEN VERIFICATION REPLACEMENT of the finite Core(5)
  bridge inside the accepted Sun(5) proof (a case previously claimed by Z. Gong). No novelty claim. No engine, checker,
  certificate, orbit/leaf count, survivor list or the Sun(5) conclusion is a premise. No scientific computation, script,
  assertion, enumeration, test, model CLI or nested agent; only hash/byte/range metadata for packaging.
- Roots: O16 = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016; S = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7;
  RUN = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h; R16 = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review.

## 0. Target and import boundary
**Core(5)** (O16/sun-coset5/proof-v4.md line 49, verbatim): "No finite group G has subgroups U_1, ..., U_5 with
[G:U_i] = 4r_i, the r_i pairwise coprime, and pairwise disjoint cosets g_iU_i." In proof-v4 this is the only statement the
finite bridge (section 4) together with the S-D refutation (section 6) is used for (section 7). **Theorem C5W** below proves
Core(5) for EVERY finite group, with no minimal-order frame, every placement of the markers E2/E3 (proof-v4 line 113),
r_i = 1 allowed, and unbounded private cofactors.
| input | literal scope used | record (sha256) | role |
|---|---|---|---|
| Core(5) statement, E2/E3 definition | definitions only | O16/sun-coset5/proof-v4.md (3d17efcc034cca643515e581fa4667515086d0844a58b951e2641080d6c94516) lines 49, 113; accepted by R16/sun-coset5-parent-verdict-v1.md (2cf0243687714e42d128b7cfd65c19ce538d7a73a603b1e027a5ae04d7065301) | target |
| rules erratum v3 | read for completeness; E9/E10 concern L3 and Lemma R, neither used here | O16/sun-coset5/rules-v1-erratum-v3.md (1b3e126e1c398a71401b4c7e13cbc19c276befe095bb1c0043450c3cd425e8ed) | none load-bearing |
| Lagrange, product formula, coset-intersection criterion | elementary | proof-v4 line 256; S/K7-LFC-INV-erratum-v1.md (7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5) E1 | Lemma MU, proved below |
| Sun(2) | coprime indices => cosets meet | proof-v4 line 259 (L0.2 + L0.6) | proved below inside FC |
| Sun(3) | three disjoint left cosets => a pair with index gcd >= 3 | Zhu, arXiv:0807.2207 Thm 1.1 (proof-v4 lines 109, 255) | the ONLY non-elementary theorem used |
| left-fibre count, actual inversion | method only | S/K7-LFC-INV-v1.md (45be91622b5973bf5e461d8ed08ae3e00544685d8a1728a8c3ae54738092726c) lines 20-71 with erratum E1-E3, E6-E7; RUN/review/sun7-lfc-inv-parent-verdict-v1.md (8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18) lines 18-19 | RE-PROVED in section 2 using only Sun(2), Sun(3); the accepted package (which records Sun(5)/Sun(6) imports) is NOT imported, so no circularity |
**Not used:** Sun(4), Sun(5), Sun(6); the rules T, K, P, N2, F, H2, FH2 and L8 of rules-v1; Lemma R and the S-D refutation
(proof-v4 sections 5-6); the minimal counterexample (section 3); the engine, checker, bridge, certificates and all counts;
Prop 4.5 and R1 (they concern the reduction TO Core(5), which is upstream of this theorem); Gong; M-S Lemma 4.6; Menon.

## 1. Setting, multipliers and markers
Let G be finite, U_1..U_5 subgroups with n_i = [G:U_i] = 4 r_i, r_i pairwise coprime, and g_iU_i pairwise disjoint. Every
pair has g_ij = gcd(n_i, n_j) = 4. Let alpha_ij = [G : U_i cap U_j]/lcm(n_i, n_j).
**Lemma MU.** alpha_ij is an integer in {1, 2, 3}. *Proof.* n_i, n_j divide [G : U_i cap U_j] (Lagrange), so lcm does. The
multiplication map U_i x U_j -> U_iU_j has fibres of size |U_i cap U_j|, so |U_iU_j|/|G| = alpha_ij/4. Disjointness of g_iU_i
and g_jU_j means g_i^-1 g_j is not in U_iU_j, so alpha_ij/4 < 1. QED
**Markers** (proof-v4 line 113). E2 is the vertex whose r is even, E3 the vertex whose r is divisible by 3, if they exist;
by pairwise coprimality each exists at most once, and E2 = E3 is allowed. A vertex is **plain** if its r is coprime to 6
(r = 1 included). All exponents and all prime factors >= 5 of the r_i are unrestricted.

## 2. Two tools (complete proofs)
**Lemma INV.** Put U_i* = g_iU_ig_i^-1. The cosets g_i^-1 U_i* = (g_iU_i)^-1 are pairwise disjoint left cosets with the same
indices 4 r_i: a Core(5) configuration with the same r_i and the same E2, E3. Its multipliers satisfy
alpha_ij + alpha*_ij <= 4. *Proof.* Inversion is a bijection of G and conjugate subgroups have equal index. With
h = g_i^-1 g_j, conjugating by g_i^-1 gives alpha*_ij = [G : U_i cap hU_jh^-1]/lcm(n_i, n_j), and |U_ihU_j| =
|U_i||U_j|/|U_i cap hU_jh^-1|, so |U_ihU_j|/|G| = alpha*_ij/4. The double cosets U_iU_j and U_ihU_j are distinct (h is not in
U_iU_j), hence disjoint, so alpha_ij/4 + alpha*_ij/4 <= 1. QED. In particular **alpha_ij = 3 implies alpha*_ij = 1**.

**Lemma FC (left-fibre count with Sun(2), Sun(3) only).** Fix an apex v. For j != v put
lambda_j = [U_v : U_v cap U_j] = n_j alpha_vj/4 = r_j alpha_vj and t_j = [U_j : U_j cap U_v] = n_v alpha_vj/4 = r_v alpha_vj.
Call a set S of neighbours of v **admissible** if every two members have gcd(lambda, lambda') >= 2 and every three members
contain two with gcd >= 3. If w_j >= 0 and sum_(j in S) w_j <= 1 for every admissible S, then
  sum_j w_j alpha_vj/4 <= 1 - 1/n_v < 1.
*Proof.* g_jU_j meets exactly t_j left cosets of U_v (they are g_j u U_v with u in U_j, equal iff u, u' agree modulo
U_j cap U_v), and none of them is g_vU_v, which is disjoint from g_jU_j. For a left coset B = bU_v != g_vU_v let S_B be the set
of j whose coset meets B. For j in S_B pick p_j in g_jU_j cap B; then g_jU_j cap B = p_j(U_j cap U_v), and b^-1 p_j(U_j cap U_v)
is a left coset in the finite group U_v of a subgroup of index lambda_j; distinct j give disjoint cosets. Sun(2) in U_v: if
gcd(lambda, lambda') = 1 the two subgroups H, K satisfy [U_v : H cap K] >= lambda lambda' (it is a multiple of both), so
|HK| = |H||K|/|H cap K| >= |U_v|, HK = U_v and every left coset of H meets every left coset of K; impossible. Sun(3) (Zhu) in
U_v applied to any three pieces gives two with gcd >= 3. So every S_B is admissible. Summing the weight condition over the
n_v - 1 cosets B != g_vU_v counts each j exactly t_j times: sum_j w_j t_j <= n_v - 1; divide by n_v. QED
(At most four pieces share a fibre; only their 2- and 3-subsets are constrained. Neither Sun(4) nor Sun(5) is used.)

## 3. Local gcds
For distinct neighbours j, k of v, gcd(lambda_j, lambda_k) = 2^(min v_2) 3^(min v_3): the r's are pairwise coprime and
alpha <= 3, so no prime >= 5 is common. Here v_2(lambda_j) = v_2(r_j) + [alpha_vj = 2] and v_3(lambda_j) = v_3(r_j) + [alpha_vj = 3].
Hence, for a **plain** neighbour j: v_2(lambda_j) = [alpha_vj = 2] and v_3(lambda_j) = [alpha_vj = 3]; therefore
- (G1) a plain neighbour with alpha_vj = 1 has gcd(lambda_j, lambda_k) = 1 for every other neighbour k (it is **isolated**);
- (G2) two plain neighbours have gcd 2 if both multipliers are 2, gcd 3 if both are 3, and gcd 1 otherwise.
Write V2(m) for the best value contributed by m plain neighbours with multiplier 2 when they are pairwise compatible only
among themselves: V2(0) = 0, V2(1) = 1/2 (weight 1), V2(m) = m/4 for m >= 2 (weights 1/2; by (G2) every two have gcd 2,
so by the Sun(3) clause no admissible set contains three of them).

## 4. Lemma PR (plain rows)
**Lemma PR.** If all four neighbours of v are plain and not all four multipliers alpha_vj equal 3, contradiction.
*Proof.* Let n_1, n_2, n_3 count neighbours with multiplier 1, 2, 3 (n_1 + n_2 + n_3 = 4, n_3 <= 3). By (G2) the three
groups are pairwise incompatible, so every admissible set lies inside one group. Weights: 1 on each multiplier-1 neighbour
(isolated by G1); the V2 weights on the multiplier-2 group; 1/n_3 on each multiplier-3 neighbour (any admissible set holds at
most n_3 of them). The value of FC is n_1/4 + V2(n_2) + [n_3 >= 1]·3/4.
- n_3 >= 1: the other 4 - n_3 >= 1 neighbours contribute at least 1/4 (a 1 gives 1/4; a group of 2s gives >= 1/2 or m/4),
  so the value is >= 3/4 + 1/4 = 1.
- n_3 = 0: n_1/4 + V2(n_2) with n_1 + n_2 = 4 equals 1 (n_2 = 0), 5/4 (n_2 = 1), or (n_1 + n_2)/4 = 1 (n_2 >= 2).
In every case the value is >= 1, contradicting FC. QED

## 5. Lemma AR (the E2 apex when E2 != E3)
**Lemma AR.** Suppose E2 =: a and E3 =: b both exist and a != b; the other three vertices form the plain set P. If not all
three multipliers alpha_ap (p in P) equal 3, contradiction.
*Proof.* Work at v = a. Put beta = alpha_ab. Then lambda_b = r_b beta has v_2 = [beta = 2] (r_b is odd) and v_3 = v_3(r_b) + [beta = 3] >= 1.
For p in P, by section 3, gcd(lambda_b, lambda_p) = 2^[beta = 2 and alpha_ap = 2] 3^[alpha_ap = 3]; so b is compatible with
the multiplier-3 neighbours always, with the multiplier-2 neighbours iff beta = 2, and never with the multiplier-1 ones.
Let n_1, n_2, n_3 count p in P with alpha_ap = 1, 2, 3 (sum 3); assume n_3 <= 2.
- **n_3 in {1, 2}.** Weights: 1 on one multiplier-3 neighbour p*; 0 on b and on the other multiplier-3 neighbour; 1 on each
  multiplier-1 neighbour; the V2 weights on the multiplier-2 neighbours (n_2 <= 2, so pairs only). p* is compatible only
  with b and multiplier-3 neighbours (weight 0); multiplier-1 neighbours are isolated (G1); multiplier-2 neighbours are
  compatible only with each other and possibly b (weight 0). Every admissible set has weight <= 1. Value
  3/4 + n_1/4 + V2(n_2) >= 1, since n_1 + n_2 = 3 - n_3 >= 1.
- **n_3 = 0, beta in {1, 3}.** b is compatible with no p, hence isolated: weight 1 on b and on each multiplier-1 neighbour,
  V2 weights on the multiplier-2 group (by G2 and the Sun(3) clause). Value beta/4 + n_1/4 + V2(n_2) >= 1/4 + n_1/4 + V2(n_2),
  which is 1 for (n_1, n_2) = (3, 0), (1, 2), (0, 3) and 5/4 for (2, 1).
- **n_3 = 0, beta = 2.** b and the multiplier-2 neighbours are pairwise of gcd 2 (b: v_3(lambda_p) = 0, v_2 minimum 1), so by
  the Sun(3) clause an admissible set contains at most two of them; b is incompatible with multiplier-1 neighbours.
  Weights 1/2 on b and on each multiplier-2 neighbour (or 1 on b if n_2 = 0), 1 on multiplier-1 neighbours. Value
  1/4 + n_2/4 + n_1/4 = 1 if n_2 >= 1, and 1/2 + 3/4 if n_2 = 0.
Every case contradicts FC. QED

## 6. Theorem C5W
**Theorem C5W [CANDIDATE_UNVERIFIED].** Core(5) holds: no finite group has five pairwise disjoint left cosets with indices
4 r_i and r_i pairwise coprime. The proof covers every placement of E2/E3 (absent, equal, distinct), r_i = 1, and all
exponents and cofactors.
*Proof.* Let Gamma be such a configuration and Gamma* its inverse (Lemma INV: same r_i, E2, E3; alpha*_ij = 1 whenever
alpha_ij = 3).
- **Case 1: E2 and E3 are not two distinct vertices.** Choose v = E2 if E2 exists, otherwise v = E3 if E3 exists, otherwise
  any vertex. Every neighbour of v is plain (the markers are unique, and if both exist they equal v). If some
  alpha_vj != 3, Lemma PR for Gamma is a contradiction. Otherwise all alpha_vj = 3, so all alpha*_vj = 1 != 3, and Lemma PR
  for Gamma* is a contradiction.
- **Case 2: E2 = a and E3 = b exist with a != b.** If some alpha_ap != 3 (p in P), Lemma AR for Gamma is a contradiction.
  Otherwise all alpha_ap = 3, so all alpha*_ap = 1 != 3, and Lemma AR for Gamma* is a contradiction. QED

**Corollary (bridge replacement).** In the accepted proof-v4 section 7, the dichotomy "certificate orbit / S-D orbit" can be
replaced by Theorem C5W: no pattern (alpha, E2, E3) of a Core(5) configuration exists at all, in particular none in the S-D
orbit. Section 6 of proof-v4 (S-D) is then a redundant cross-check, and the minimal-order frame of section 3 is not
needed for Core(5). Together with the accepted WRITTEN sections 1-2 of proof-v4 (R0, the reduction to Core(5) and the
re-proved Prop 4.5), this yields a computation-free written proof of Sun(5) for every group, relative to Zhu's Sun(3)/Sun(4)
and the rules-v1 L0.3-L0.5, L1-L3 used by Prop 4.5. That composite is a CONDITIONAL observation pending review of this file;
it is not claimed as accepted, and Sun(5) remains a previously claimed case (Gong), so no novelty follows.
Consistency check (not a premise): for S-D, alpha_1j = 3 (j = 2, 3, 4) forces alpha*_1j = 1, so at E2 = 1 the inverse has three
isolated plain neighbours of mass 1/4 and b of mass alpha*_10/4 >= 1/4 that cannot share a fibre with them: total >= 1.

## 7. Dependency DAG, computation boundary and review checks
| node | depends on | status |
|---|---|---|
| MU, INV | Lagrange, product formula, coset-intersection criterion | reproduced complete proofs |
| FC | fibre construction; Sun(2) (proved); Sun(3) (Zhu) | new restricted count; no Sun(t), t >= 4 |
| G1, G2, V2 | pairwise coprime r, alpha <= 3 | elementary |
| PR | FC, G1, G2, V2 | new |
| AR | FC, G1, G2, V2 | new |
| C5W | PR, AR, INV | new, CANDIDATE_UNVERIFIED |
Acyclic. **Computation boundary: none.** Only Sun(2) (proved) and Zhu's Sun(3) enter; no computer-assisted theorem, no
engine/checker/bridge output, no Sun(5) instance (so no circularity with the theorem Core(5) serves).
**Requested checks:** (1) the Core(5) statement and E2/E3 are quoted exactly; (2) FC: fibre count, Sun(2) proof, only 2- and
3-subsets used; (3) INV gives a Core(5) configuration with the same markers and alpha + alpha* <= 4; (4) section 3 valuations,
G1, G2, V2; (5) Lemma PR: every (n_1, n_2, n_3) with n_3 <= 3 and every admissible set; (6) Lemma AR: every beta in {1, 2, 3}
and (n_1, n_2, n_3) with n_3 <= 2, including the compatibility of b; (7) the two-case split of the theorem and the passage to
Gamma*; (8) that nothing from the finite bridge, certificates, counts or the S-D section is used.
**Provenance.** The left-fibre count and inversion method come from the accepted K7-lane LFC/INV record (re-proved here at
k = 5 with Sun(2), Sun(3)); the plain-row and E2-apex weightings are written here. Exposure before the scope freeze is
listed in the scope (including the old bridge's rule names and counts, not used). No novelty, Lean or human-review claim.
