# LS (length-sensitive S1): frozen scope (before proof text or probe)

Owner ContinueOlson.  Written after /bin/date 2026-10-19T02:17:07-0700, on parent instruction (IRC 2026-10-19 ~02:14: 'consider a distinct
LENGTH-SENSITIVE lemma (unproved parent conjecture, don't assume) ... bounded falsification first ... stop on explicit Y
satisfying ZP but long zero ... if true at finite aids, write proof attempt using extra Y-T occurrences beyond shortest long
zero T; don't extend S1-sharp unchanged outside its range; alternatively explicit counterfamily would show word-level GRX
needed').  Status: CONJECTURE (parent's), not assumed anywhere.

## Statement under test
LS(p, kappa): p >= 5 prime, 0 <= kappa <= p - 2 integer; every sequence Y of odd elements of C_(2p) with |Y| >= p + 2kappa + 1
satisfying (ZP_kappa) (no zero-sum of length in [2kappa + 2, 2p]) satisfies (S1_kappa) (no zero-sum of length > 2kappa,
equivalently none of length >= 2p + 2).
- For kappa <= floor(2p/3), LS(p, kappa) is implied by the accepted S1-sharp (no length condition); the new range is
  floor(2p/3) + 1 <= kappa <= p - 2.  The S1-sharp sharpness families (length 2p + 2) lie below the threshold there
  (p + 2kappa + 1 > 2p + 2), so they do not refute LS.
- Use: terminal 2 <= k <= p - 1 has R = 2p + 2kappa^ - k >= p + 2kappa^ + 1, so LS(p, kappa^) gives (S1) at kappa^ and
  Theorem ROT-FB (a) (proof-FB-v1.md + erratum 1) would give rotation rigidity for every terminal 2 <= k <= p - 1.
- Counterexample: an explicit Y (exact p, kappa) with |Y| >= p + 2kappa + 1, (ZP_kappa), and a zero-sum of length >= 2p + 2
  (exact DP).  It would be SEQUENCE-LEVEL only (no avoider claimed) and would show that word-level (GRX) input is needed.
- Note: (ZP) is hereditary; a counterexample of length R > p + 2kappa + 1 whose long zero-sum T has |T| < R yields one of
  length max(|T|, p + 2kappa + 1) by deleting elements outside T; so lengths beyond the threshold must still be searched only
  when |T| exceeds the threshold.

## Planned finite aids (falsification only; launch plan to the parent and gated pre-launch PID record first)
- p = 7, kappa = 5 (new range) and kappa = 4 (control: S1-sharp range, expect no failure at any length): complete DFS over
  all (ZP_kappa) multisets of odd elements of C_14 of every length <= 4p - 2 (hereditary pruning by exact length DP);
  report every (ZP) multiset of length >= p + 2kappa + 1 with a zero-sum of length >= 2p + 2 (counterexample) and, as a
  positive control, the number of (ZP)-and-not-(S1) multisets below the threshold.
- p = 11, kappa = 8, 9: the same DFS with the canonical normalisation 'value 1 is a most frequent generator value' (valid by
  an automorphism when a generator occurs, which holds for |Y| > 2kappa + 1), budget-limited with completeness flags; plus a
  structured random search Y = T X (T of index 2 w.r.t. g = 1, |T| >= 2p + 2; X random extra odd elements) for p = 11, 13.
