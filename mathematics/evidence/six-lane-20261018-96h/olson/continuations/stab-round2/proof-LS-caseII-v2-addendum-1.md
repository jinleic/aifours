# Addendum 1 to proof-LS-caseII-v2.md: Theorem LS-II holds WITHOUT the induction hypothesis H'(kappa)

Owner OlsonSTABSuccessor.  Written after /bin/date 2026-10-19T05:11:38-0700 (clock read again before freezing; see checkpoint-003).  Status: CANDIDATE
[W], UNREVIEWED.  Applies to proof-LS-caseII-v2.md (3df159ff61784cb3345b27a6cf9da873900051df92dbb3be019e846578d73a43), read through erratum-1-CF-XT-ROW-range.md.  Steps 1-4
of v2 do not use H'(kappa) or Lemma SH; only Step 5 did.  Step 5 is replaced by Step 5' below, which uses neither, so:
Theorem LS-II' (unconditional).  For p >= 7 prime and kappa0 + 1 <= kappa <= p - 2, no LS-counterexample of length p + 2kappa + 1
lies in case (II).  (Lemma SH of v2 remains correct as a conditional lemma but is no longer used.)
Parent's preflight inequality (recorded): a negative x = -c'g has c' <= 2e - 5 <= M, since M >= 2kappa + 3 = 2p - 2e + 3 and 3e <= p - 1.

## Step 5' (the long zero-sum, no induction)
Let T be a long zero-sum of Y = g^M (-g)^(v1) R' (Steps 1-3: mu1 = p - 1; every term of R' tiny or negative).
(a) While a long zero-sum contains both g and -g, delete one g and one -g: the result is a zero-sum two shorter.  If the length
was 2p + 2 the result has length 2p, excluded by (ZP_kappa); so the length was >= 2p + 4 and the result is again long.  Hence there
is a long zero-sum T1 <= T without g or without -g.  Without g, T1 <= (-g)^(v1) R' has length <= r <= p - 2: impossible.  So
T1 = g^a W' with W' <= R'.
(b) While the current long zero-sum g^(a') W'' contains a negative x = -c'g with c' <= a', delete x and c' copies of g (a
zero-sum g^(c') x is removed, so a zero-sum remains).  Each deletion shortens by c' + 1 <= 2e - 4, while the even lengths in the
excluded window [2kappa + 2, 2p] form e consecutive even values, so a shortening by at most 2e - 4 from a length >= 2p + 2 cannot
land below the window without landing in it; hence every intermediate zero-sum is long.  At the end we have a long zero-sum
T2 = g^(a') W2 (W2 <= R') with a' < c'_x for every negative x remaining in W2.
(c) |T2| >= 2p + 2 and |W2| <= s <= e - 2 give a' >= 2p - e + 4 > 2e - 5 >= c'_x; so W2 contains no negative term, i.e. W2 is
tiny, and |W2| = |T2| - a' >= 2p + 2 - M = delta0 + 2.  Step 4 of v2 gives |W2| <= (delta0 - 1)/3: contradiction.  []

## Effect
The LS-threshold reduction now reads (unconditionally): every LS-counterexample of length p + 2kappa + 1 is in case (I) of the
dichotomy (g = g0, delta0 <= e - 2, all U-multiplicities <= p - 2e + 1).
