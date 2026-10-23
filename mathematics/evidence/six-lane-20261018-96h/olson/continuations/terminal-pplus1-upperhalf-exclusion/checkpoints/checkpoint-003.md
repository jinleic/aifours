# Checkpoint 003: UH-EXCL, outcome decided (O3: proved slice + whole-interval constraints + obstruction)

Owner OlsonPP1Exclusion. /bin/date 2026-10-19T13:40:07-0700. Previous: checkpoint-002.md sha256
cc91be36f173276467fa3ec214debfd108ec35902a0cc95b738c29c4f05ea859 (13:28:29).

- Actual results now worked out in full (to be frozen next, CANDIDATE_UNVERIFIED, inputs NF/GRX/RS(b) only, CT not needed):
  (T1) Theorem UH-A (whole interval (p-1)/2 <= kappa^ <= p-3, full NF antecedent kept): if w is an avoider with such an NF then
       the dominant multiplicity satisfies A >= 2kappa+3, i.e. at most p-4 rotation letters differ from the dominant value.
       Route: Lemma P/U (re-derived) -> window -> heavy run (b + delta >= 2e-4 holds for b >= p-3) -> light sets or the
       two-high-set structure (A' = kappa, a-letters in <= 2 runs, all (-a)-letters in one run) -> >= 2 empty runs ->
       M-set analysis (|M| <= p-1-b <= 2): b = p-1 by lambda = -1, b = p-2 forces tau = -(2e-2)a, b = p-3 forces tau = -2a,
       and two empty runs then give an identity 2p-subword (e not = 1, 2, 3 mod p issues checked: 2e = 2, 4 = 0, 2 = 0 fail).
  (T2) Proposition SH (e <= (p+2)/3): Lemma MW at m = e plus an explicit path of m = e sets gives a run h with
       alpha_h >= e_h >= p+1+delta; then every set avoiding h is low, lambda >= 0, and >= 2 empty runs.
  (T3) Lemma MW (multi-length window) and Proposition L (additive integer lifts along arcs in the +-a light region).
- Not achieved: exclusion for 2kappa+3 <= A <= 2p-1. Exact failure: two empty runs force only floor(c/2)+2 elements of M by
  Cauchy-Davenport against |M| <= c := A-2kappa (no contradiction once c >= 3); heavy run needs b + delta >= 2e-4; light sets
  need delta >= e-2 or a separate two-high-set analysis.
- Next bounded action: freeze proof file, obstruction note, review package and manifest; IRC Main; park.
