# Theorem B0S-CJ'': Theorem B0S-CJ with (H) weakened to R >= 4 kappa - 2  (r2)

Owner OlsonReflectionRigidity.  r2 written after host clock 2026-10-18T07:17:24-0700.  Status: written proof [W], UNREVIEWED.
Supersedes proof-B0SCJx-r1.md (58c02ebea88b9198cc0bf7f1218e83e5433515b571521a10a4c173db4642d42e, kept unchanged).  r1 proved the
same with R >= 4 kappa - 1, and everything it states remains true.  Its Remark Sec. 2 attributed the boundary to Case I's (L3).  That
rested on the crude bound delta_P <= 4 kappa - 2 <= R - 1; the exact form of (L3) also allows R = 4 kappa - 2 (fix map, Sec. 4).
proof-B0SCJ-r1.md (a775321c...40af) and proof-B0SPP-r5.md (d388d391...bd64) stay frozen and unchanged.
Scope: B = 0 only.  Regime (III) with R <= 4 kappa - 3 stays open.

## 0. Statement

**Theorem B0S-CJ''.**  Theorem B0S-CJ (proof-B0SCJ-r1.md Sec. 0) holds verbatim, together with its Corollaries 1 and 2 and the
Containment remark, when (H) R >= 4 kappa + 1 is replaced by
   (H'') R >= 4 kappa - 2.
The parameter claim for p <= 23 in B0SCJ-r1 Corollary 2 (L24-28) is NOT extended; see Sec. 3.

## 1. Where (H) is used, and the replacement under (H'')

The proofs in proof-B0SPP-r5.md Secs. 1-3 and proof-B0SCJ-r1.md use (H) only at the points below.  Throughout, w avoids, so
R >= p >= 5, n_E <= 2 kappa and Delta <= kappa - 1 (B0SPP-r5 L53-55, from P0 only); also R <= 2p - 1.
1. **2 kappa <= p - 1 (B0SPP-r5 L55-56).**  4 kappa - 2 <= R <= 2p - 1 gives 4 kappa <= 2p + 1, so 2 kappa <= p; p is odd.
2. **Windows nonempty (L59-61).**  The bound min(R - 2 kappa, (R - 1)/2 - kappa) needs R >= 2 kappa + 1.  This holds: for
   kappa >= 2 since 4 kappa - 2 >= 2 kappa + 1, and for kappa = 1 since R >= 5.
3. **Lemma C2(a) (L81-83).**  "Small" means m <= 2 kappa.
   - None small: >= (R - 3)/2 >= 0.
   - One small: >= R/2 - 1 - kappa >= -2, since R >= 2 kappa - 2.
   - Two small: >= (R - 1)/2 - 2 kappa >= -2, since R >= 4 kappa - 3.
   - Three small: = R - 3 kappa >= -2, since R >= 3 kappa - 2.
4. **Lemma C2(b) (L83-86).**  The pair sums s1, s2, s3 add up to 2R.  Any two add up to R + (mass of the part they share).
   - None small, or exactly one small: as in L84-86.  The other two pair sums are > 2 kappa, hence floor terms.
   - Exactly two small, s1 and s2, sharing the part Q_b of mass m_b:
     * R + m_b = s1 + s2 <= 4 kappa, so m_b <= 4 kappa - R <= 2.
     * s3 = R - m_b is not small (exactly two are), so g(s3) = floor(s3/2).
     * (B') = R + m_b - 2 kappa + floor((R - m_b)/2) >= (3R + m_b - 1)/2 - 2 kappa.
     * This is >= R - kappa - 1 + Delta = p - 2 iff (R + m_b + 1)/2 >= kappa + Delta.
     * The left side is >= (4 kappa - 1)/2 = 2 kappa - 1/2 > kappa + Delta, because Delta <= kappa - 1.
   - Three small: 2R <= 6 kappa together with R >= 4 kappa - 2 forces kappa <= 2.  kappa = 1 is impossible, since then R <= 3 < p.
     For kappa = 2 we get R = 6 and each pair sum is 4, so (B') = 2R - 3 kappa = 6 >= p - 2, as p <= R = 6.
   So C2(b) holds as stated: (B') holds whenever all three pair sums are >= 2 Delta - 1.  C2(c) follows from C2(a) (L87).
5. **Lemma SIGMA-2P for Delta <= 0 (L89-90).**  Uses only C2(b) and C1(c).
6. **Sec. 3, the kill (L103-114).**  Each inequality is checked under (H''), 2 kappa <= p - 1 and k >= 2 kappa + 1.  We use
   B0S-r4's exact forms (proof-B0S-r4.md L74-75), delta_P = Phi(P) - rho_P - 2m and Phi(P) <= 4 kappa (B0S-r4 L85-87).
   - **Case I, (U1), (L1).**  Phi(P) <= 4 kappa <= 2p - 2.
   - **Case I, (L2).**  delta_P + rho_P - 2m = Phi(P) - 4m <= 4 kappa - 4, and this is <= 2R - 2 kappa - 2 iff R >= 3 kappa - 1.
     The latter holds.  [B0SPP-r5 L107 used the cruder Phi(P) <= 2R - 2 kappa - 2 (R >= 3 kappa + 1), which fails at
     kappa = 2, R = 6.]
   - **Case I, (L3) (exact: delta_P <= R - [R - rho_P odd]).**
     * If rho_P >= 1: delta_P <= 4 kappa - 1 - 2m <= 4 kappa - 3 <= R - 1.
     * If rho_P = 0, R even: delta_P <= 4 kappa - 2 <= R.
     * If rho_P = 0, R odd: R >= 4 kappa - 1, so delta_P <= 4 kappa - 2 <= R - 1.
   - **Case I, (U2), (U3).**  By construction.
   - **Case II.**
     * (L3): delta_P <= 2 kappa - 2 <= R - 1.
     * (L2) for W = {y}: r_y <= R <= 2R - 4 kappa + 5, since R >= 4 kappa - 5.
     * (L2) otherwise: 4 kappa - 4 <= 2R - 2 kappa - 2, since R >= 3 kappa - 1.
     * (U1): r_y + 1 <= 2p, and 3 kappa - 7 < 2p.
     * (L1): 4 kappa - 4 < 2p.
     * (U3) and |F| >= d/2 are generic (k >= 2 kappa + 1).
7. **proof-B0SCJ-r1.md.**  (F1) and (F2) use P0 and 2 kappa <= p - 1 only.  Lemma CJ, the Theorem and Corollaries 1-2 use only
   C1, C2, (F1) and (F2).  The Containment remark is regime-free.  []

## 2. Remark on the boundary

At R = 4 kappa - 3:
* C2(a) still holds (two small: (R - 1)/2 - 2 kappa = -2).
* C2(b) still holds (two small: m_b + floor((R - m_b)/2) >= 2 kappa - 2 >= kappa + Delta - 1).
* (L3) also holds if the greedy's last step is analysed.  A new interval gives m >= 2; an extension adds at most 2 kappa - 2; a
  bridge adds at most 2 kappa - 4.  In each case delta_P <= 4 kappa - 4 - rho_P.
What has not been checked is the edge R = 2p - 1 = 4 kappa - 3.  There 4 kappa = 2p + 2, so (U1) and (L1) need a separate
argument.  Below R = 4 kappa - 3, C2(a) fails for splits with two light parts, and SIGMA needs a substitute.

## 3. Coverage of the three R-values 4 kappa - 2, 4 kappa - 1, 4 kappa

For p <= 61 there are 364 cells (p, kappa, R, Delta, k) with R in that range, k >= p + 1, Delta <= kappa - 1 and p <= R <= 2p - 1;
116 of them have R = 4 kappa - 2.
* Delta <= 1: covered by Corollary 2 or SIGMA-2P.
* Delta >= 2: covered when p >= kappa + 5 Delta - 5.
This fails in 30 cells.  The first are (19, 5, 19, 4, 29), (23, 6, 23, 5, 35) and (29, 8, 30, 6, 44).
The cells with p <= 13 and R = 4 kappa - 2:
* (5, 2, 6, 0, 8), (7, 3, 10, -1, 10), (11, 4, 14, 0, 16), (11, 5, 18, -3, 14), (13, 5, 18, -1, 18), (13, 6, 22, -4, 16):
  Delta <= 0, covered;
* (13, 4, 14, 2, 20): Delta = 2 and 13 >= 4 + 5, covered.
(Parameter enumeration only, in the eval transcript of this worker at 07:17 PDT; no word data.)

## 4. Fix map r1 -> r2

1. Statement: (H') R >= 4 kappa - 1 is replaced by (H'') R >= 4 kappa - 2.
2. Sec. 1 is re-done for R = 4 kappa - 2:
   - item 1: 4 kappa <= 2p + 1;
   - item 4: two-small case with m_b <= 2; three-small case at kappa = 2, R = 6;
   - item 6: (L2) uses Phi(P) - 4m <= 4 kappa - 4; (L3) uses B0S-r4's exact form and the parity of R.
3. Sec. 2: the r1 sentence "(H') is where Case I's (L3) stops" is withdrawn.  It used the crude bound delta_P <= 4 kappa - 2 <= R - 1.
   The new remark records what is known at R = 4 kappa - 3.
4. Sec. 3 coverage now covers three R-values.
All r1 conclusions remain true.
