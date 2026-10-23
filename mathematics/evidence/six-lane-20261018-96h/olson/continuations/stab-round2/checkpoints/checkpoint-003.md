# Checkpoint 003 (Slice A, OlsonSTABSuccessor)

Written after /bin/date 2026-10-19T05:23:21-0700.  All items CANDIDATE [W], unreviewed.
- erratum-1-CF-XT-ROW-range.md 767fe8f8605019b3b3b7aa1ff6a610f088279ede30b9b3429544d4c8487c1db7 (parent preflight: CF integer kappa range; XT uses only re-derived (ZP_kappa);
  rho-wording repair; exact scopes; STAB-extension to kappa = p - 1 false for every prime p >= 7, p = 5 undecided).
- proof-LS-caseII-v2.md 3df159ff61784cb3345b27a6cf9da873900051df92dbb3be019e846578d73a43 (v1 ceb27e1b... never sent) + addendum 1 c289db226c86ea7703af4a23c4a93dce543669cb911d36b5845e70aad2c98718: the
  dominant-value case (II) is excluded UNCONDITIONALLY (Step 5' replaces the induction-dependent Step 5; Lemma SH kept as a
  conditional lemma, unused).  Process note: addendum 1's header cites the 05:11:38 clock read; a later read (05:17:13) also
  preceded its writing.
- proof-LS-caseI-smalldelta-v1.md 2ad172a026ee64441f00fd228b8b402a0a5f2e0d85df04512c87f0e70e5a68b1: case (I) with delta0 <= 2 and 4e <= p + 1 + 2delta0 excluded (index-one on the
  zero-sum-free U, greedy interval, Lemma AP' forces a = -1, then (L) fails).  Corollary LS-small: LS(p, p-2) for p >= 7,
  LS(p, p-3) for p >= 11, LS(p, p-4) for p >= 13 -- the first unconditional LS cells beyond S1-sharp (sequence level only).
- Exact remaining obstruction for LS: case (I) with delta0 >= 3 (U may contain zero-sums mod p of size <= delta0 - 1, at most
  delta0 - 1 terms in any disjoint union), or with 4e > p + 1 + 2delta0 (zero-free part shorter than (p+1)/2: index-one unavailable).
- STAB/LS+: the same CF/ROW machinery needs a generator of multiplicity >= p - e at length 3kappa + 2; not yet available.
- Next bounded action: case (I), delta0 >= 3, small e, via Z0 = maximal disjoint union of mod-p zero-sums (|Z0| <= delta0 - 1)
  and index-one on U - Z0; then the large-e regime.
