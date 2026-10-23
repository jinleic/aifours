# review-package-R2MIX-v1: Theorem R2X (no R2-row in M3(1,1)) by a mixed-family d-fibre count; R1X; conditional M3E [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read immediately before this write: 2026-10-19T12:24:51-0700. Author SunR2MixedFibres.
- **Candidate:** `K62-R2MIX-v2.md`, sha256 b75e6dc7e72b8c0b1cd5388e8845a3bcd23854b0fbd83292fa6ff7c22ade0806 (283 lines,
  29,217 bytes). It supersedes the undelivered draft `K62-R2MIX-v1.md` (90d399eb…6f80: one garbled sentence in the proof of
  Lemma 3 (b), interface and remark wording; no statement, case or argument change). Scope frozen before the derivation:
  `K62-R2MIX-SCOPE-v1.md`, sha256 12a64d8e4c19cd6dd8f7d04d6ee7dabef06bd23707522fae07d27a2b4651e4e5 (12:01:42).
- **Excerpt manifest:** `review-excerpts-R2MIX-v1.json`, sha256 9500f7b911419c08e34c906e39146c8baf7b75303b00878046b66431528f7b9e:
  24 inclusive ranges {path, whole-file sha256, start, end}; embedded text 86,091 bytes; JSON 5,788 bytes. Hashes and ranges
  were checked against current bytes (packaging metadata only: shasum, wc, sed range extraction; no scientific computation).
  Pending texts appear in it only as definitions, as the sources of re-proved arguments, or as the conditional premise of
  Corollary M3E.
- Directory: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k62-r2-mixed/`.

## Outcome against the frozen scope
The primary target is claimed in writing: **Theorem R2X** — in the full class M3(1,1) (e_d >= 4, e* = 2, f* = 1, 3-marker on
t in O with f_t >= 2, orientation (1,1), 5-marker on d, i*, t, some p in O' or absent, exponents and w's unbounded, arbitrary
groups via R0) no family y has y_tu in {1, 2} for all four u in O'. This is the missing lemma (L-R2) of K62-M3R-v2 section 7 (c).
Also claimed: **Corollary R1X** (no R1-instance), with K62-M3R-v2 Theorem RR re-proved as Theorem 7; **Corollary 6.1**
(every M3(1,1) configuration satisfies NR of K62-MK-v2). **Corollary M3E** (M3(1,1) empty) is only CONDITIONAL ON the pending
K62-MK-v2 Theorem M3R.

## The argument in five lines
1. **Lemma 2 (new):** if (U_v cap U_j)(U_v cap U_k) = U_v, no fibre at v meets both j and k.
2. **Lemma 4 (= M3R-v2 Lemma C, re-proved):** tau_z({d, i*, e}) = 3 iff (Pi_d cap Pi_e)(Pi_d cap Pi_(i*)) = Pi_d. If no e in O' has this,
   then gcd(n_t, T_z(V minus {t})) = 6.
3. **Proposition 5 (new):** in the y'-configuration at d, fibres hold at most 3 pieces (Lemma 3 (a), Sun(4)). Pair granularity
   from y gives at least n_d / 4 d-fibres shared by t and each u in O' with y_tu in {1, 2} (Lemma 3 (b)). The t-fibres absorb at
   most n_d - s of these incidences. If e and i* never shared a d-fibre, e would meet at most n_d / 2 - 1 fibres, one short, at
   d's own fibre. So for an R2-row, tau_y'({d, i*, e}) <= 2 for every e in O', and every y_tu = 2.
4. **Theorem R2X:** by 2 and 3, gcd(n_t, T_y'(V minus {t})) = 6, so at least n_t / 6 fibres at t in y are empty (Lemma 1).
5. **The count:** weights 1/2 on O' and d form a feasible set (pairwise label gcds 2, so no allowed triple; Sun(3)). They give
   11/12 > 1 - 1/6. Contradiction.

## Requested checks (hostile)
1. **Family directions.** In both cases y = alpha and y = alpha*, the y'-configuration is the inversion of the y-configuration.
   So [G : W] in Lemma 1 is T_y({t, u}) = lcm(n_t, n_u) y_tu at d in y', and T_y'(V minus {t}) at t in y.
2. **Lemma 1.** The fibre count [W : W cap g_vU_vg_v^-1] >= n_v / gcd(n_v, [G : W]), and that these fibres miss every j in Q. The
   statement is translation-free.
3. **Lemma 2.** The product decomposition p^-1 q = ab and the common point pa = qb^-1.
4. **Lemma 3.** (a) The six labels at d (n_c / 2, n_(i*) / 4) have pairwise gcd exactly 3 in every marker placement, so at most
   3 pieces per fibre. (b) Inclusion-exclusion #both = #neither (both degrees n_d / 2), and gcd(n_d, lcm(n_c, n_c') z') =
   2^(1 + v2 z') for z' in {1, 2}, including when the 5-marker is on d.
5. **Lemma 4.** (a) gcd(n_e, T_(r-1)) = 6 at each chain step, with every 5-marker position (d, i*, t, p, none); k_e <= 3; the 3-adic
   count; gcd(n_t, T). (b) k_e = 3 implies the product equality. (c) The index bookkeeping
   [Pi_d : A cap B] = tau * 3 * 5^(h_e + h*) w_e w_*, hence |AB| / |Pi_d| = tau / 3.
6. **Proposition 5.** (i) |S_F cap O'| <= 2 - [i* in S_F] for fibres meeting t, and the sum bound n_d - s. (ii) The direction of
   the granularity (y' at d, bounded by y). (a) The number of fibres meeting neither t nor i* is n_d / 4 + s, and F_d is among
   them. (b) It forces all four y_tu = 2 and s = 0.
7. **Theorem R2X.** Step 1 needs Proposition 5 (a) for every e in O'. Step 2: Lemma 1 at t with Q = V minus {t}. Step 3: feasibility
   of c (labels 2 ell_u and n_d / 2 have pairwise gcd exactly 2 in every marker placement) and the arithmetic
   4 * (1/2)(2/6) + (1/2)(1/2) = 11/12 > 5/6. Check that y_(t i*) and R2N are nowhere used.
8. **Theorem 7 (RR re-proof).** Step (ii): the gcd(d_a, d_j) <= 2 claims. This includes a = p with x'_(t i*) = 5 excluded by Lemma 6
   (L1), and E3-a, which is used only at its accepted scope (C2 proof sub-claim Z11 (a)). Steps (iii)-(iv): the measure
   inequalities.
9. **Premise hygiene.** Nothing pending is used except in Corollary M3E. M3R-v2 R2N is not used. M13, GS, HD, GX and FH are not
   used. Computer-assisted Sun(5)/Sun(6) remain transitive imports.
10. **Mutation checks 1-8** of section 8 (thought experiments): in particular, dropping Lemma 2, using one family only, or dropping
    Sun(4) at d each removes the contradiction.

## Provenance and labels
Direct Sun instances: Sun(2) (Theorem 7 (iv)), Sun(3) (R2X step 3; Theorem 7 (ii)) and Sun(4) (Lemma 3 (a)). Through the import
E3-a: Sun(2). The LFC/VFC package and the K6.2* class reduction keep the computer-assisted Sun(5) (2cf02436…5301) and Sun(6)
(efe1d849…1e29) in the transitive closure. FH and Sun(7) are not used. All new claims are CANDIDATE_UNVERIFIED. This is written
mathematics only; no computation, novelty, priority, Lean or human-review claim is made. The parent owns all reviews and the
verdict.
