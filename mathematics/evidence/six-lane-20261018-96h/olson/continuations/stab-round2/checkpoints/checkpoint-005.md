# Checkpoint 005 (Slice A, OlsonSTABSuccessor)

Written after /bin/date 2026-10-19T06:00:33-0700.  No live scientific child process (only date/shasum shell calls, all exited); written
work only, consistent with the parent's runtime-guard HOLD (6c1d8440...).
- erratum-2-prereq-consolidated.md fb136e6ef71f7250774c3102a35c88a9709fee827091df84f67b433fb13106d5: ONE consolidated erratum disposing Codex d049d531... and Claude 8decff29...
  for the prerequisite package (R1-R13), sent 05:58.
- erratum-1-delta-APprime.md e035f8d14b6bcb57c0af0d5beb170ddf3471674490583e66b75d0d34cc90c461: corrected AP' proof for the delta package (LS-small), AP pointer for addendum 1.
- NEW proof-LS-lin-v1.md 434a5dfd38e3f82ef596b7c23cdf528069207e35581c573e83e1613626c19aec [W, unreviewed]: Theorem LS-lin: LS(p, kappa) for every cell with
  e = p - kappa >= 3 and p >= 6e - 10.  Case (I) of the LS-threshold dichotomy is closed by: maximal mod-p zero-sum Z0 (|Z0| <= e - 3),
  index one on the zero-sum-free core U', an integer no-wrap AP step forcing a = -1, first-crossing bounds on Z0's sub-sums, then (L)
  fails.  Together with LS-II' (case (II), unconditional) and e = 2 (LS+2): LS holds whenever p - kappa <= (p + 10)/6.
- Exact LS gap now (lane candidates): 5 <= e <= (p - 1)/3 with p < 6e - 10, i.e. the band (p + 10)/6 < p - kappa <= (p - 1)/3 near
  kappa0.  Failure points of the method there: index one needs |U'| >= (p + 1)/2, the no-wrap AP step needs p > 6e - 11.
- LS+/STAB: LS+2 (e = 2) and BASE1 (kappa0 + 1, p = 1 mod 3) only; the case-(alpha) analogue of Step 6 fails (first-crossing gives
  f >= |Z''| + delta' but needs delta0 = delta' + |Z0|).
- Next bounded action: LS+ case (beta) for p >= C e (reduction to E2-core plus <= e - 2 extra terms), then case (alpha) with a = -1/2.
