# Checkpoint 009: FB accepted; KPS (conditional) candidate; LS conjecture survives complete small-p falsification

Owner ContinueOlson.  Written after /bin/date 2026-10-19T02:28:50-0700.  Continues checkpoint 008 (7c8e817d...dcb).

## Actual result
- FB: parent verdict run review/olson-FB-parent-verdict-v1.md (8d6d4967...d63a) accepts FB v1 + erratum 1
  (evidence/proof-FB-v1-erratum-1.md 33de46d2...e202) as a written scoped partial: uniform band
  F - o_F >= 2(p - 1 - floor(2p/3)), o_F <= p - 1, p >= 7.
- CANDIDATE (unreviewed, CONDITIONAL on S(p)): evidence/proof-KPS-cond-v3.md cfaf3cc5...ed01 (k = p cells reduce to S(p);
  Lemma FB-p, Lemma ARC0).
- LS (parent conjecture) scope frozen (evidence/LS-scope-v1.md 80ae8041...dfa); probe v11
  (evidence/probe-v11/RECEIPT-v11-v1.md b7e4c9eed025ad44ede8ad43fec9c456288a85cb20eb3a2085449d3cc0804d97): complete DFS p = 7 (kappa 4, 5), p = 11 (kappa 8, 9): 0 counterexamples.
- Written, not yet frozen as a candidate: Lemma SLZ (shortest long zero-sum): in a (ZP_kappa) sequence a zero-sum of length
  >= 2kappa + 2 of minimal length N satisfies N <= p + 2kappa + 1 (proof: delete d in T, FB on T - d gives d = (2p - W) g and
  the proper zero-sum d u (T - d - g^s - (-sg)) of length N - s - 1 forces N <= p + kappa + t0; the n- = 0 case is excluded
  by Davenport).  Consequently a minimal-length LS counterexample has length exactly p + 2kappa + 1 (otherwise every long
  zero-sum would use all terms and SLZ applies to Y itself).

## Exact blocker
LS at length exactly p + 2kappa + 1 (k = p - 1 cells): there T - d may have a zero-sum of length exactly 2kappa with
complement of length exactly p (the S(p) boundary again), and the extra terms Y - T must be used.

## Next bounded action
Freeze Lemma SLZ + the reduction as a candidate note; attack the threshold case with the extra terms; small aid (v12) on the
maximum length of (ZP)-and-not-(S1) multisets (sharpness of LS) after a launch plan.
