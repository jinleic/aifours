# K62-SH-v1: the i*-shadow at d in the e_d >= 4 residue (partial necessary conditions) [CANDIDATE]

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T05:58:11-0700.
- **Author:** Sun63Successor; single author, unreviewed, no computation.
- **Setting:** class K6.2* with **e_d >= 4, e* = 2** (the frontier left by the accepted K62-E3, verdict
  `RUN/review/sun7-K62E3-parent-verdict-v1.md` sha256 576969ddb99fc2d0f5c6382f66428a7f4d7d3a1b59f681fc4d9d0f458fecbb0f).
  Notation as in `K62-E3-v1.md` section 0: n_d = 2^(e_d) 5^(h_d) w_d, n_(i*) = 4 * 3^(f*) 5^(h*) w_*,
  n_c = 2 * 3^(f_c) 5^(h_c) w_c (c in O); t = the 3-marked vertex of O if it exists (then f* = 1).
- **Premises (accepted):** old README section 0 L0.1 with Lagrange; E1 (1 <= alpha <= g - 1); LFC (a)-(d), INV (a)-(b)
  with E6 (verdict 8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18); K62-E3 Lemma 1 and the facts of its
  proof steps 1-3 (accepted verdict above): after inversion if necessary, **alpha_(d i*) = 1**; then (g_d = 1) every
  fibre F != U_d (left coset of U_d) has |S_F| <= 3, the sum of |S_F| is 11 n_d / 4, and for every c in O the set
  L_c = g_cU_cU_d is disjoint from U*_cU_d (U*_j := g_jU_jg_j^-1). Sun instances: only those inside these imports
  (Sun(4) via K62-E3 step 2). **Not used:** VFC, TG, CLIQUE, the T rule, RPLP, F7 (re-derived below by granularity),
  any computation.

## 1. Lemma SH-1
With alpha_(d i*) = 1 and g_d = 1: (a) for c in O, **U*_cU_d = G minus L_c** (both have measure 1/2 and are disjoint);
(b) U*_(i*)U_d is disjoint from L_(i*) = g_(i*)U_(i*)U_d and mu(U*_(i*)U_d) = alpha*_(d i*)/4.
*Proof.* mu(L_c) = t_c / n_d = alpha_dc / g_dc = 1/2 (LFC (a)-(b)); by L0.1, mu(U*_cU_d) = [G : U*_c cap U_d]/(n_c n_d) =
alpha*_dc / g_dc = 1/2; disjointness is K62-E3 step 3 (its argument uses only w in U*_c). (b): the same disjointness
argument with i* in place of c, and mu(U*_(i*)U_d) = alpha*_(d i*)/g_(d i*) by L0.1. QED

## 2. Lemma SH-2 (forced containment and exclusion by granularity)
Let c in O and a := alpha*_(i* c); put J := [G : U*_(i*) cap U*_c] = lcm(n_(i*), n_c) a.
(a) If alpha*_(d i*) = 1 and (a in {1, 3}, or a = 5 and h_d = 0), then **U*_(i*)U_d is contained in U*_cU_d**.
(b) If alpha*_(d i*) = 3 (so t exists by K62-E3 Lemma 1), c != t, and (a = 1, or a = 5 and h_d = 0): contradiction.
*Proof.* Z := U_d(U*_(i*) cap U*_c) lies in U_dU*_(i*) and in U_dU*_c. By L0.1, mu(Z) = [G : U_d cap U*_(i*) cap U*_c] /
(n_d J), and the numerator is a common multiple of n_d, J and I := [G : U_d cap U*_(i*)] = lcm(n_d, n_(i*)) alpha*_(d i*).
(a) mu(Z) >= lcm(n_d, J)/(n_d J) = 1/gcd(n_d, J), and gcd(n_d, J) = 2^(min(e_d, 2 + v2 a)) 5^(min(h_d, max(h*, h_c) + v5 a))
= 4 under the hypotheses (a odd; if h_d >= 1 then h* = h_c = 0 and 5 does not divide a). So mu(Z) >= 1/4 =
mu(U_dU*_(i*)); Z lies in U_dU*_(i*), so Z = U_dU*_(i*) (finite sets), and U_dU*_(i*) lies in U_dU*_c. Invert.
(b) Here f* = 1 and f_c = 1, so I has 3-part 3^2 and J has 3-part 3 (a in {1, 5}); 2-parts: n_d, I: 2^(e_d); J: 4;
5-parts: at most one of h_d, h*, h_c is positive and J carries an extra 5 exactly when a = 5 (then h_d = 0). Hence
mu(Z) >= lcm(n_d, J, I)/(n_d J) = 3/4 > 1/2 = mu(U_dU*_c), impossible since Z lies in U_dU*_c. QED

## 3. Theorem SH (orientation alpha_(d i*) = 1)
Put Odd* := {c in O : alpha*_(i* c) in {1, 3}, or alpha*_(i* c) = 5 and h_d = 0}.
- **(i)** If alpha*_(d i*) = 1, then **|Odd*| <= 2**.
- **(ii)** If alpha*_(d i*) = 3, then **Odd* minus {t} contains no c with alpha*_(i* c) in {1, 5}**, i.e. every c in O minus {t}
  has alpha*_(i* c) in {2, 3, 4}, or alpha*_(i* c) = 5 with h_d >= 1.
- **(iii)** If alpha_(d i*) = alpha*_(d i*) = 1, then also |Odd| <= 2 with Odd := {c in O : alpha_(i* c) in {1, 3}, or
  alpha_(i* c) = 5 and h_d = 0} (apply (i) to the inverted configuration, INV (a) with E6).
*Proof of (i).* Write B(F) := O minus S_F. Then sum_F |B(F)| = 5 n_d - 5 n_d / 2 = 5 n_d / 2, so
sum_F (|B(F)| - 2) = n_d / 2, and every term is >= 0 (|S_F| <= 3; B(U_d) = O). The n_d / 4 fibres met by g_(i*)U_(i*)
(LFC (b); U_d is not among them) have |S_F cap O| <= 2, so their terms are >= 1. By SH-1 (b) the n_d / 4 fibres
contained in U*_(i*)U_d are disjoint from L_(i*), hence distinct from those; U_d is one of them (term 3); and by SH-2 (a)
and SH-1 (a) each of them lies in G minus L_c for every c in Odd*, so |B(F)| >= |Odd*|. If |Odd*| >= 3, the sum is
>= n_d/4 + 3 + (n_d/4 - 1) = n_d/2 + 2 > n_d/2. (ii) is SH-2 (b). QED
R0 lifts all statements to arbitrary groups.

## 4. Scope
Partial necessary conditions on the i*-rows; **no sub-case of the residue is excluded by this file alone.** Example:
the pattern P_ob of `K62-STATUS-v2.md` (alpha*_(i* .) = (2, 4, 4, 2, 2), alpha_(i* .) = (4, 2, 2, 4, 1)) satisfies (i)
and (iii). Full K6.2* (e_d >= 4, e* = 2) and full Sun(7) remain OPEN. No novelty claim.
