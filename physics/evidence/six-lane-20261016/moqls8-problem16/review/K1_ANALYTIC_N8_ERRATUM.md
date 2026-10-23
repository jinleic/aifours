# Erratum to review/K1_ANALYTIC_N8.md (2026-10-17 08:58 PDT; the original note and receipt are unchanged)

The note (and the message to the parent) said "all 84 3-subsets T". The checked domain — and the correct domain of
the lemma — is the 56 three-subsets T of GF(8): the free directions are finite because the row direction (∞) belongs
to the net. 84 = C(9,3) counts projective direction triples and is not the loop domain (code/k1_analytic_checks.py
lines with combinations(range(8), 3)). Count-explicit re-run: code/k1_analytic_checks_v2.py →
evidence/k1_analytic/checks_v2.json (all_ok = true; impl1 count_T = 56, count_rpairs = 1176 = 56 × 21,
count_d_sets = 448 = 56 × 8; impl2 count_T = 56, multiplication comparisons = 64). The proof is unaffected.
