# Slice BASE2 (LS at the first p = 2 (mod 3) cells): frozen scope before derivation, v1

Owner OlsonSTABSuccessor.  Written after /bin/date 2026-10-19T07:39:01-0700, on the parent's instruction after run
review/olson-LSplus-chain-parent-verdict-v1.md (4005007f4e073386236016b62949cba925cb5cde12ba13c24ce27b2a2c351b55): 'Next ONE written slice: try the smallest p = 2 (mod 3) BASE2
LS cells (17,12)/(23,16) ... OR prove a translation/multiplier-pinning lemma for the SC2008 normal form.'  Status: SCOPE ONLY.
Written research; no computation.  LS, LS+, STAB are not assumed.

## Statements under test (in this order)
(S1) LS(17, 12): every odd Y over C_34 with no zero-sum of length in [26, 34] and |Y| >= 42 has no zero-sum of length >= 36.
(S2) LS(23, 16): every odd Y over C_46 with no zero-sum of length in [34, 46] and |Y| >= 56 has no zero-sum of length >= 48.
(S3) Only if (S1), (S2) close by a uniform argument: LS(p, (2p + 2)/3) for every prime p = 2 (mod 3), p >= 17 (the BASE2 cells,
     e = (p - 2)/3); otherwise the exact residual configuration and the failing step.
Each is a sequence-level statement; no INV*, ordered-Olson or LS+/STAB claim.

## Method (frozen before derivation)
- Reduction (accepted imports only): RED (threshold length p + 2kappa + 1), DGM-p (dominant generator g0), the LS-threshold dichotomy,
  LS-II' (case (II) excluded), Proposition I-small at its literal hypotheses, CF (a)/(b) (through E1/R4), Lemma AP (R6) and AP' (D1),
  the index-one record at n = p only where its length hypothesis is checked, and the accepted greedy step of LS+2 Sec. 3 (C).
- Residual case analysis by delta0 (case (I): 1 <= delta0 <= e - 2): maximal mod-p zero-sum core Z0, zero-sum-free part U'.
- Where index one is unavailable (|U'| + 1 < (p + 3)/2), a direct argument or the atomic decomposition of a shortest long zero-sum T
  (|T| = 2p + 2 = 3kappa at these cells: T is a product of two atoms, or of three atoms of length kappa each), with any needed
  inverse step RE-PROVED; Zeng-Yuan 2011 / Savchev-Chen 2007/2008/2016 statements are not imported.
- The alternative lever (translation/multiplier pinning for the SC2008 normal form) is NOT attempted in this slice unless (S2) stalls.

## Imports (accepted; exact)
review/olson-CFXT-ROW-LSII-parent-verdict-v1.md ca6e4ca75bba7f88024667951e160ffb8555d99389d50e34fd2cceef31b420e0; review/olson-STAB-delta-parent-verdict-v1.md
ac8ead13b89b4d89dc62d13fd2a20dbf7957b1b427be46bf7e8db5bbb8d5a4c5 (LS-II', I-small, AP' via D1, LS+2 greedy step); review/olson-LSplus-chain-parent-verdict-v1.md 4005007f...1b55
(context only); RED (review/olson-KPS-SLZ-parent-verdict-v1.md); SLZ3 (2b7b08a3...ae24, |T| only); index-one record e4615144...35c6.
