# RECEIPT: probe v11 (falsification aid for the parent's conjecture LS), v1

Owner ContinueOlson.  Written after /bin/date 2026-10-19T02:28:50-0700.  Aid only, never a premise.  Scope: evidence/LS-scope-v1.md
80ae8041...dfa (frozen before the probe).  Launched through code/lane_launcher_v2.py (c10c2855...aef4) with the exclusive
pre.json PID record before the gate byte; plan sent to the parent first; self-budgeted; stdout only.

| probe | script sha256 | pid | rc | wall s | pre / post / stdout sha256 |
|---|---|---|---|---|---|
| v11 LS | 912e592c9f35d0268b0d49848c24b2a9095728b1cbf7b632961c6b0dc649970e | 50170 | 0 | 270.0 | 4713589513ecdd68f9967bc2c255b159cf796f3ad2a8400fed5dd11df2e226ef / c1bae9d81c2543b37ef2b96dad0151175435ce7ade5b95820c56b184f5b537e1 / 67de9615ed05955c46c10bd37ac5104f301e5e8f1c225b6e257ff7917fe802c9 |

Results (complete DFS over all (ZP_kappa) multisets of every length <= 4p - 2, exact length DP, hereditary pruning):
- p = 7, kappa = 4 (control; S1-sharp range): 24,058 multisets (incl. empty), max length 17, 0 not-(S1) at any length.
- p = 7, kappa = 5: 58,008 multisets, max length 18 = p + 2kappa + 1 (6 multisets of length 18), 0 counterexamples to LS;
  12 not-(S1) multisets below the threshold (e.g. 11^6 13^10, i.e. (-3g)^6 (-g)^10: the F1 shape).
- p = 11, kappa = 8 (canonical: value 1 a most frequent generator value): 5,124,873 multisets, COMPLETE, max length 29,
  4 of length >= 28, 0 counterexamples; 7 not-(S1) below threshold (e.g. 1^14 3^10 = F1).
- p = 11, kappa = 9 (canonical): 11,980,841 multisets, COMPLETE, max length 30, 1 of length >= 30, 0 counterexamples; 164
  not-(S1) below threshold.
- Part C (random T X constructions, p = 11, 13, 1.65M+ trials): 0 (ZP) hits (uninformative).
Observation (not a premise): the maximum length of a (ZP_kappa) multiset equals 2p + kappa - 1 in all four DFS cells (the
value of g^(2p-1)(-g)^kappa), which is the length bound Lemma FB implies for (S1) sequences (|Y| = L + 2t <= 2p - 1 + n-,
n- <= t <= kappa).
