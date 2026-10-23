# K62-DG-v1: exact 2-adic grids at d in the e_d >= 4 residue; necessary depth conditions; P_ob excluded [CANDIDATE]

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T06:12:14-0700.
- **Author:** Sun63Successor; single author, unreviewed; **no computation** (none run; HOLD 6c1d8440… respected).
- **Setting:** class K6.2*, **e_d >= 4, e* = 2** (frontier of the accepted K62-E3, verdict sha256
  576969ddb99fc2d0f5c6382f66428a7f4d7d3a1b59f681fc4d9d0f458fecbb0f), any 3-/5-marker placement, arbitrary exponents.
  Notation of `K62-E3-v1.md` section 0. After inversion if necessary (K62-E3 step 0): **alpha_(d i*) = 1**; g_d = 1;
  U*_j := g_jU_jg_j^-1; fibres F = left cosets of U_d; S_F as in K62-E3; B(F) := O minus S_F. For non-empty Q in O:
  W*_Q := intersection of U*_c (c in Q), T*_Q := [G : W*_Q], N(Q) := #{F : Q contained in B(F)}.
- **Premises (accepted):** old README section 0 L0.1 with Lagrange; E1; LFC (a)-(d), INV (a)-(b) with E6 (verdict
  8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18); rules-k7-v1 L1 (T rule: (T1), (T3), tau_min, tau_max)
  and VFC (V1)-(V4), accepted in `six-lane-2026-10-16/review/sun-coset7-written-parent-verdict-v1.md` (sha256
  73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35), applied to the configuration or to its inverted
  configuration (INV (a): again a configuration with the same indices); K62-E3 with errata v1-v2 (accepted): Lemma 1,
  Lemma 2, Lemma 3 in the proof form for every non-empty Q (erratum v2 Z10), steps 1-3, and the C2 sub-claim (a)
  (alpha, alpha* in {1, 2, 4} on O-O pairs). Sun instances: Sun(3) via (V3) in section 5 only; others only inside the
  accepted imports. **Not used:** K62-FG, K62-R2, K62-SH, RPLP, TG, F7 as an import (containments are re-derived),
  any probe output.

## 1. Lemma DG-1 (grids)
For non-empty Q in O, N(Q) is a positive multiple of n_d / 2^(min(e_d, v2 T*_Q)).
*Proof.* For c in O, L_c := g_cU_cU_d is a union of fibres of measure alpha_dc/g_dc = 1/2 (LFC (a)-(b)); U*_cU_d has
measure [G : U*_c cap U_d]/(n_c n_d) = alpha*_dc/g_dc = 1/2 (L0.1) and is disjoint from L_c (K62-E3 step 3, whose argument
uses only w in U*_c). Hence U*_cU_d = G minus L_c, and c is in B(F) iff F lies in U*_cU_d. So N(Q) = n_d mu(Z_Q) with
Z_Q := intersection of U*_cU_d (c in Q). Z_Q is left W*_Q-invariant and right U_d-invariant, hence a union of double
cosets W*_Q x U_d, each of measure [G : W*_Q cap xU_dx^-1]/(T*_Q n_d), a multiple of 1/gcd(T*_Q, n_d) (L0.1, Lagrange).
gcd(n_d, T*_Q) = 2^(min(e_d, v2 T*_Q)) by K62-E3 Lemma 3 (proof form for Q). N(Q) >= 1 since U_d lies in Z_Q. QED

## 2. Lemma DG-2 (counting at d)
Let A_4 := #{F : |B(F)| >= 4}. Then (i) N(O) + A_4 <= n_d/4 - 1; (ii) sum over 3-subsets R of O of N(R) <=
n_d - 2 + 3 N(O); (iii) sum over 4-subsets Q of O of N(Q) <= n_d/4 - 1 + 3 N(O). In particular N(O) <= n_d/8 - 1/2.
*Proof.* K62-E3 steps 1-2: sum_F |S_F cap O| = 5 n_d/2 and |S_F| <= 3, so sum_F (|B(F)| - 2) = n_d/2 with all terms >= 0
(B(U_d) = O). The n_d/4 fibres met by g_(i*)U_(i*) (LFC (b)) have |S_F cap O| <= 2, and U_d is another fibre with
|B| = 5; so #{|B| >= 3} >= n_d/4 + 1 and n_d/2 >= #{|B| >= 3} + A_4 + N(O), giving (i). With b_k := #{|B(F)| = k}:
b_3 + 2 b_4 + 3 b_5 = n_d/2, b_5 = N(O), b_4 = A_4 - N(O); the sum in (ii) is b_3 + 4 b_4 + 10 b_5 = n_d/2 + 2 A_4 + 5 N(O),
and the sum in (iii) is b_4 + 5 b_5 = A_4 + 4 N(O); insert (i). The last claim is (i) with A_4 >= N(O). QED

## 3. Lemma DG-3 (triples) and DG-4 (4-subsets)
(DG-3) For a 3-subset R of O with alpha*-values x1 <= x2 <= x3 on its edges: v2(T*_R) = 1 + v2(tau*_R), where tau*_R
is a multiple of lcm(x1, x2, x3) with tau*_R <= x1 x2. Hence **v2(T*_R) <= 3 unless (x1, x2, x3) is (2,4,4) or (4,4,4)**.
*Proof.* L1 for the inverted configuration: T*_R = lcm(n_a, n_b, n_c) tau*_R and v2(lcm) = 1 (e_c = 1 on O). Here g = gamma = 6
and ell_z = n_z/6 is odd, so gcd(x, ell_z) = 1 for x in {1, 2, 4} (C2 sub-claim (a)): (T1) gives x | tau* for each edge,
and tau_max = min over apexes of x_opp * min(other two) = x1 x2. A multiple of 8 is <= x1 x2 only if x1 x2 >= 8. QED
(DG-4) For a 4-subset Q = R plus {e} with e unmarked (n_e = 6 w_e; such e exists, at most two O-vertices are
marked): v2(T*_Q) <= v2(T*_R) + v2(m_e), m_e := min over j in R of alpha*_(ej).
*Proof.* T*_Q = lcm(n_e, T*_R) k (Lagrange) with k / gcd(n_e, T*_R) = mu(U*_e W*_R) <= alpha*_(ej)/6 (L0.1); gcd(n_e, T*_R) =
6 (w_e is prime to T*_R by K62-E3 Lemma 3's proof for R, and 6 | T*_R), so k <= m_e in {1, 2, 4}, v2(k) <= v2(m_e); and
v2(lcm(n_e, T*_R)) = v2(T*_R). QED

## 4. Theorem DG (orientation alpha_(d i*) = 1)
(a) If min(e_d, v2 T*_Q) <= 4 for all five 4-subsets Q of O, then N(O) <= n_d/16 and
  **sum over the ten 3-subsets R of 2^(-min(e_d, v2 T*_R)) <= 19/16 - 2/n_d.**
(b) Hence, under the hypothesis of (a), at least one 3-subset R has min(e_d, v2 T*_R) >= 4 (so by DG-3 its alpha*-values
are (2,4,4) or (4,4,4) and tau*_R in {8, 16}), and if only one does, it has min(e_d, v2 T*_R) >= 5 (values (4,4,4),
tau*_R = 16, e_d >= 5).
*Proof.* (a) If N(O) > n_d/16, each 4-subset Q has N(Q) >= N(O) > n_d/16 and N(Q) a multiple of n_d/16 (DG-1 and the
hypothesis), so N(Q) >= n_d/8, and DG-2 (iii) gives 5 n_d/8 <= n_d/4 - 1 + 3 N(O), i.e. N(O) > n_d/8 - 1/2, contradicting
DG-2. So N(O) <= n_d/16; then DG-2 (ii) and N(R) >= n_d 2^(-min(e_d, v2 T*_R)) (DG-1) give the sum bound.
(b) If no R has min(e_d, v2 T*_R) >= 4, every term is >= 1/8 and the sum is >= 10/8; if exactly one has it and its value
is 4, the sum is >= 9/8 + 1/16 = 19/16. Both exceed 19/16 - 2/n_d. QED
The same holds for the alpha-family whenever alpha*_(d i*) = 1 (inverted configuration).

## 5. Corollary: the pattern P_ob of `K62-STATUS-v2.md` is excluded (any markers, any e_d >= 4)
P_ob: O = {c_1, ..., c_5} (indices mod 5), alpha = 4 and alpha* = 2 on the cycle edges c_ic_(i+1), alpha = 2 and alpha* = 4
on the chords c_ic_(i+2); alpha_(i* .) = (4,2,2,4,1), alpha*_(i* .) = (2,4,4,2,2); alpha = alpha* = 1 on all d-edges.
1. *alpha*-triples.* Consecutive triples {c_i, c_(i+1), c_(i+2)} have values (2,2,4): tau* = 4 (DG-3: 4 | tau* <= 4).
   The others {c_i, c_(i+1), c_(i+3)} have values (2,4,4): tau* in {4, 8}.
2. *tau* != 8.* Suppose tau* = 8 on R = {c_1, c_2, c_4} (other i by rotation). In the inverted configuration at apex c_4
   (L1 (T3), gamma = 6): mu(U*_4(U*_1 cap U*_2)) = 8/(6 alpha*_12) = 2/3 = alpha*_41/6 = alpha*_42/6, so (finite sets, inclusion)
   X*_1 = X*_2 where X*_j := U*_4U*_j. From the consecutive triples {c_2,c_3,c_4} and {c_4,c_5,c_1} (tau* = 4):
   mu(U*_4(U*_2 cap U*_3)) = 4/(6 * 2) = 1/3 = alpha*_43/6 gives X*_3 contained in X*_2, and likewise X*_5 contained in X*_1.
   Every edge c_4c_j (j in O) is tight (alpha + alpha* = 6 = g), so the VFC sets of the inverted configuration at c_4
   satisfy D~_j = G minus X*_j (V1, INV (b)). Hence D~_1 = D~_2 is contained in D~_3; it is non-empty (measure
   alpha_41/6 = 1/3), and every right coset R in it has S_R containing {c_1, c_2, c_3}, with local indices
   n_j alpha_4j/6 (j = 1, 2, 3; alpha_41 = alpha_42 = 2, alpha_43 = 4), whose pairwise gcds are 2 (the w's and marker parts are
   pairwise coprime). Three pieces with pairwise gcds < 3 violate (V3) (Sun(3)). So tau* = 4 on all ten triples.
3. *Depths.* v2(T*_R) = 3 for all ten R (DG-3). For Q = {c_i, ..., c_(i+3)} take R = {c_i, c_(i+1), c_(i+2)}, e = c_(i+3)
   (choose i so that e is unmarked: the five 4-subsets are rotations, and each 4-subset has at least two unmarked
   vertices among its two ends c_i, c_(i+3) or else use the end c_i with R = {c_(i+1), c_(i+2), c_(i+3)}, which is also
   consecutive): m_e = min(4, 4, 2) = 2, so v2(T*_Q) <= 4 (DG-4).
4. Theorem DG (a) applies (P_ob has alpha_(d i*) = 1), and the triple sum is 10/8 > 19/16. Contradiction. QED

## 6. Scope
- **Candidate results:** Lemmas DG-1..DG-4 and Theorem DG (necessary conditions in the whole e_d >= 4 residue, any
  markers), and the exclusion of the explicit pattern P_ob (any markers, e_d >= 4).
- **Not claimed:** exclusion of the residue. Theorem DG forces, in each family to which it applies, a deep 4-subset
  (min(e_d, v2 T*_Q) >= 5) or deep triples with alpha*-values (2,4,4)/(4,4,4) and tau* >= 8; whether such patterns survive the
  apex constraints (as in section 5 step 2) and the rows at O-vertices and i* is not settled here.
- No novelty claim. Full K6.2* (e_d >= 4) and full Sun(7) remain OPEN.
