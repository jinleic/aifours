# Theorem B0S-CJ''': Theorem B0S-CJ with (H) weakened to R >= 4 kappa - 4 and 2 kappa <= p - 1  (r3)

Owner OlsonReflectionRigidity.  r3 written after host clock 2026-10-18T07:33:09-0700.  Status: written proof [W], UNREVIEWED.
Supersedes proof-B0SCJx-r2.md (43032a0f712064bd765c4bef3aad3d4695e803ec39d234b8f9bde32df6485779) and r1 (58c02ebe...d42e).
Both are kept unchanged, and all their conclusions remain true.  r3 replaces two crude bounds by exact ones: the exact (A') criterion
in Lemma C2(a), and an increment analysis of B0S-r4's Case I greedy.  Together these take the theorem down to R = 4 kappa - 4.
Fix map in Sec. 4.  proof-B0SCJ-r1.md (a775321c...40af) and proof-B0SPP-r5.md (d388d391...bd64) stay frozen and unchanged.
Scope: B = 0 only.

## 0. Statement

**Theorem B0S-CJ'''.**  Theorem B0S-CJ (proof-B0SCJ-r1.md Sec. 0) holds verbatim, together with Corollaries 1 and 2 and the
Containment remark, when (H) R >= 4 kappa + 1 is replaced by
   (H''') R >= 4 kappa - 4  and  2 kappa <= p - 1.
For R >= 4 kappa - 2 the second condition follows from the first and R <= 2p - 1, which is r2.  It fails only when
kappa = (p + 1)/2 and R is 2p - 2 or 2p - 1.  These "edge cells" are excluded; see Sec. 2.
The p <= 23 claim of B0SCJ-r1 Corollary 2 is NOT extended.

## 1. Where (H) is used, and the replacement under (H''')

Throughout, w avoids, so R >= p >= 5, n_E <= 2 kappa and Delta <= kappa - 1 (B0SPP-r5 L53-55, from P0 only); also R <= 2p - 1.
1. **2 kappa <= p - 1 (B0SPP-r5 L55-56).**  Assumed.
2. **Windows nonempty (L59-61).**  The bound needs R >= 2 kappa + 1.  This holds: for kappa >= 3 since 4 kappa - 4 >= 2 kappa + 2,
   and for kappa <= 2 since R >= 5.
3. **Lemma C2(a), (A') for every split (L81-83), with the EXACT two-small criterion.**
   - Let m1, m2 <= 2 kappa and m3 = R - m1 - m2 > 2 kappa, and put T := m3.  Then
     g(m1) + g(m2) + g(m3) = R - 2 kappa - ceil(T/2).
     This is >= -2 iff T <= 2R - 4 kappa + 4, i.e. iff m1 + m2 >= 4 kappa - 4 - R.
   - Under (H''') the right side is <= 0, so the two-small case never fails.
   - One small: >= R/2 - 1 - kappa >= -2.
   - Three small: R - 3 kappa >= -2, since R >= 3 kappa - 2 (4 kappa - 4 >= 3 kappa - 2 for kappa >= 2; kappa = 1 is trivial).
   - None small: >= 0.
   [B0SPP-r5 L82 and r2 used the cruder bound (R - 1)/2 - 2 kappa, which needs R >= 4 kappa - 3.]
4. **Lemma C2(b) (L83-86).**
   - None small, or exactly one small: as in L84-86.
   - Exactly two small, s1 and s2, sharing the part Q_b of mass m_b:
     (B') = (s1 - kappa) + (s2 - kappa) + floor((R - m_b)/2) = floor((3R + m_b)/2) - 2 kappa,
     which is >= p - 2 iff 3R + m_b >= 2p + 4 kappa - 4.  This holds for every m_b >= 0, since 2R >= 2p and R >= 4 kappa - 4.
   - Three small: (B') = 2R - 3 kappa >= R + kappa - 4 >= p - 2 for kappa >= 2.  For kappa = 1 three small pair sums would
     force R <= 3 < p.
   So C2(b) holds as stated, and C2(c) follows from C2(a).
5. **SIGMA-2P for Delta <= 0.**  Uses only C2(b), C1(c).
6. **Sec. 3, the kill.**  We use B0S-r4's exact forms (proof-B0S-r4.md L74-75), delta_P = Phi(P) - rho_P - 2m, and an analysis of
   the LAST step of the Case I greedy (B0S-r4 L85-87).
   **Increment lemma.**  Let P = P' u {t} be the first set with Phi >= 2 kappa + 2.  Then Phi(P') <= 2 kappa, since Phi is always
   even (B0S-r4 L79).  Each defect has r_t + delta_t <= 2 kappa - 2, by (2.1).  Adding t changes the number of intervals by
   +1 (t not adjacent to P'), 0 (adjacent to one interval) or -1 (it joins two intervals).  Accordingly
   Phi(P) - Phi(P') = r_t + delta_t + 2, r_t + delta_t, or r_t + delta_t - 2.
   P' is nonempty, because one defect has Phi <= 2 kappa.  So:
   - Case +1: m(P) >= 2 and Phi(P) <= 4 kappa.
   - Case 0: m(P) >= 1 and Phi(P) <= 4 kappa - 2.
   - Case -1: m(P) >= 1 and Phi(P) <= 4 kappa - 4.
   In every case delta_P <= 4 kappa - 4 - rho_P and Phi(P) - 4m(P) <= 4 kappa - 6.
   P has at most kappa runs (Phi >= 2|P| + 2 for any set of defects, since each has r_t + delta_t >= 2), so P is proper.
   - **Case I.**
     * (U1) and (L1): Phi(P) <= 4 kappa <= 2p - 2.
     * (L2): Phi - 4m <= 4 kappa - 6 <= 2R - 2 kappa - 2, since R >= 3 kappa - 2.
     * (L3), exact (delta_P <= R - [R - rho_P odd]): from delta_P <= 4 kappa - 4 - rho_P.
       - R = 4 kappa - 4 (even): this needs rho_P >= [rho_P odd].
       - R = 4 kappa - 3 (odd): this needs rho_P + 1 >= [rho_P even].
       - R >= 4 kappa - 2: as in r2.
       All of these hold.
     * (U2), (U3): by construction.
   - **Case II.**
     * (L3): delta_P <= 2 kappa - 2 <= R - 1.
     * (L2): for W = {y}, r_y <= R <= 2R - 4 kappa + 5; otherwise 4 kappa - 4 <= 2R - 2 kappa - 2, since R >= 3 kappa - 1.  The
       latter holds for kappa >= 3, and for kappa <= 2 since R >= 5.
     * (U1): r_y + 1 <= 2p, and 3 kappa - 7 < 2p.
     * (L1): 4 kappa - 4 < 2p.
     * (U3) and |F| >= d/2 are generic.
7. **proof-B0SCJ-r1.md.**  (F1) and (F2) hold: (F2) needs only Delta <= p - kappa + 1, which is true.  Lemma CJ, the Theorem,
   Corollaries 1-2 and the Containment remark use only C1, C2, (F1) and (F2).  []

## 2. The boundary

- **At R = 4 kappa - 5,** both exact criteria fail in their worst case.  (A') fails for a split with two parts of total mass 0,
  e.g. two empty runs.  (L3) fails for a single all-empty interval of defects with delta_P = 4 kappa - 4.  Below this, SIGMA needs a
  substitute for (A'), and Case I needs a different selection.
- **The edge cells,** kappa = (p + 1)/2 and R in {2p - 2, 2p - 1}, have Delta <= -1, so J = 0 by SIGMA-2P.  Only (U1) and (L1) of
  Case I are unproved there.  Both fail only if Phi(P) = 4 kappa = 2p + 2 and, respectively, delta_P = 0 or rho_P = 0.
  For p <= 61 there are 32 edge cells, including (7, 4, 12) and (7, 4, 13).
- **Finite aids (not premises):**
  - E14 (plan-E14.md 84784dc0...f442, code ce09e887...9892, out/e14_cfunc_regime3.json e91fe646...f442): in 152,000
    interval-feasible leaves at (p, kappa, R) = (7, 3, 7) and (11, 4, 11), c = 0 on every proper interval and J = 0.
  - E14b (plan-E14b.md, code/e14b_cfunc_general_v2.py f8729c90...b905, out/e14b_cfunc_general.json): the same in 100,000 leaves
    of five IIIa configurations with general masses (2 kappa < R <= 4 kappa - 3).  For R <= 2 kappa ((7, 4, 7)), J ranged over
    [-4, 3], as expected: interval windows are empty there, so that sub-regime needs multi-interval patterns.

## 3. Coverage of R in [4 kappa - 4, 4 kappa]

For p <= 61 there are 588 cells (p, kappa, R, Delta, k) with R in [4 kappa - 4, 4 kappa], k >= p + 1, Delta <= kappa - 1,
p <= R <= 2p - 1 and 2 kappa <= p - 1.  Of these, 224 have R <= 4 kappa - 3.
* Delta <= 1: covered by Corollary 2 or SIGMA-2P.
* Delta >= 2: covered when p >= kappa + 5 Delta - 5.  This fails in 58 cells; the first are (13, 4, 13, 3, 21),
  (17, 5, 17, 4, 27) and (19, 5, 19, 4, 29).
The new cells for p = 7 are (7, 3, 8, 1, 12) and (7, 3, 9, 0, 11), both covered.  (7, 4, 12) and (7, 4, 13) are edge cells.
(Parameter enumeration only, in the eval transcript of this worker at 07:33 PDT.)

## 4. Fix map r2 -> r3

1. Statement: (H'') R >= 4 kappa - 2 becomes (H''') R >= 4 kappa - 4 with 2 kappa <= p - 1, which is automatic for
   R >= 4 kappa - 2.
2. Sec. 1 item 3: the exact two-small criterion m1 + m2 >= 4 kappa - 4 - R replaces the crude (R - 1)/2 - 2 kappa >= -2.
3. Sec. 1 item 4: the two-small case of C2(b) is written exactly (3R + m_b >= 2p + 4 kappa - 4).
4. Sec. 1 item 6: the increment lemma for the last greedy step gives delta_P <= 4 kappa - 4 - rho_P and
   Phi - 4m <= 4 kappa - 6.
5. Sec. 2: the r2 remark ("C2(a) down to 4 kappa - 3"; (U1)/(L1) edge at R = 4 kappa - 3) is superseded.  E14/E14b are
   recorded as aids.
6. Sec. 3: coverage now spans five R-values.
All r2 and r1 conclusions remain true.
