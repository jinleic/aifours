# Slice A (STAB / LS+ round 2): frozen scope before any derivation, v1

Owner OlsonSTABSuccessor.  Written after /bin/date 2026-10-19T04:44:49-0700.  Brief: run review/olson-two-slice-successor-brief-v1.md.
Status: SCOPE ONLY.  LS, LS+, STAB are conjectures; none is assumed.  Written research only; no computation.

## Inputs (read; status as recorded by the parent)
- Parent-accepted: S1-sharp (verdict review/olson-s1sharp-parent-verdict-v1.md; source 992ab63f...0cb0c + erratum 1 bf504cdf...f9507);
  SLZ3 (verdict review/olson-SLZ3-parent-verdict-v1.md 2b7b08a3ec861e953e35d2802d8deba2ae584edeed36f04350fc3a9c6fa1ae24; source 0cfe637f...3c1c + erratum 1
  483d9d1b70a895215a68654d329b73d8d8ab5221382fda290a933a937f5dda59): bounds a SHORTEST long zero-sum |T| <= 3kappa + 1, NOT |Y|;
  SLZ/EXT/PROP/RED, S(p), FB-p (verdict review/olson-KPS-SLZ-parent-verdict-v1.md 23d1a488...a612; SLZ-EXT source 24953003...d751 +
  erratum 1 907b3d06...4daa); FB (review/olson-FB-parent-verdict-v1.md).
- UNREVIEWED candidates (re-derived here before any use, never imported as accepted): LSplus-scope-v1.md 7dc04949...2cbc;
  proof-LSplus-partials-v2.md eedfa0f1...b6b2 (TV, RED+, SHIFT); addendum MAX v2 4b0be3e3...51c7 (MAX, STAB => LS+);
  notes-STAB-one-term-extensions-v1.md c1362947...20fe (handoff, not claims).

## Exact target (brief)
p >= 5 prime, kappa0 := floor(2p/3), kappa0 + 1 <= kappa <= p - 2, e := p - kappa (2 <= e, 3e <= p - 1).  Odd sequences Y over
C_(2p) with (ZP_kappa) (no zero-sum of length in [2kappa + 2, 2p]) and a long zero-sum (length >= 2p + 2).
LS+: |Y| <= 3kappa + 1.  Weaker sufficient LS: |Y| <= p + 2kappa.  STAB: length 3kappa + 1 forces E2/E3.  Not assumed.

## Frozen statements to be derived next (each will be labelled PROVED-[W] / FAILED-with-obstruction / OPEN)
(A) Lemma CF (coefficient form).  For ANY odd generator g, with M := v_g(Y), delta0 := 2p - M and U := the multiset of
    mu(x) := (c_x - 1)/2 in [1, p - 1] over the terms x = c_x g != g of Y (c_x odd in [3, 2p - 1]):
    (ZP_kappa) <=> (F): no sub-multiset W of U with sigma(W) = pq + rho, q >= 0, 0 <= rho <= e - 1, delta0 <= |W| + 2rho <= 2p;
    long zero-sum <=> (L): some W, some k >= 2, j >= 1 with sigma(W) = p(k - 1) - j and delta0 + 2j <= |W| <= 2p + 2j.
    LS+ for Y <=> |U| <= p - 3e + 1 + delta0.
(B) Lemma XT.  The (ZP_kappa) extensions of E2(kappa - 1) and of E3(kappa - 1) by at most three odd terms are listed
    exactly; in particular the only three-term extensions are E2(kappa) resp. E3(kappa) (same generator).
(C) Theorem TV2 (all two-value supports).  If Y has at most two distinct values, satisfies (ZP_kappa) and has a long
    zero-sum, then |Y| <= 3kappa + 1, with equality only for E2, E3.  (Generalises candidate Lemma TV from {h, 3h}.)
(D) Main attack: LS+ (or LS) for sequences with three or more values via (IP) = (A) with a generator of large
    multiplicity; or an explicit (ZP_kappa) sequence with a long zero-sum and |Y| >= 3kappa + 2 (falsifier); or an exact
    obstruction plus the next distinct lever.
A falsifier of STAB/LS+ would be a SEQUENCE-level statement only (no avoider claim).  No end-to-end ordered Olson claim.
