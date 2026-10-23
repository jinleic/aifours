# Checkpoint 003 (rqls10 continuation)

Recorded 2026-10-19T00:35:32-0700. Owner ContinueRQLS10.

## Claim / actual result
- Target: OPEN / UNKNOWN; no v = 10 candidate.
- v3 smoke (GO 6fc27a15...) passed all gates; v3 full (GO 3bcf3103..., 00:05:03-00:32:38 PDT, SETTLED, rc 0, no trips)
  ran all stages. Stage L numerically confirms the exact first-order prediction (excess 0 at 300 classical forced-U
  Z_7+3 points; unsymmetric excess 6). Calibrations: maximal solutions found at v = 7 (Cay(Z_7), 1/6) and v = 8 (XOR,
  2/6). v = 10: no convergence in any target (T1 244, T1t 44, T2 81, T3 29, T4 6 runs; best RRR err 0.27-0.47), and
  the method failed to recover KNOWN classical v = 10 solutions (C7 0/10 symmetric, T4 Parker 0/2), so all v = 10
  misses are uninformative.
- New written restricted result: F_9 x| H + inf with |H| in {4,8} impossible (any cardinality).

## Files (sha256)
- evidence/rqls_assay_v3.smoke.sv2.receipt.md: eb884f457b5f75e054651cf9a44720c235d1097418bb4b8132e3efb0bcd2c820
- evidence/rqls_assay_v3.full.sv2.receipt.md: 04031d5706e5627a00e5e19b10e8719ca1c2a2a58e48fa51b449b38996e96c4c
- evidence/rqls_assay_v3.full.sv2.result.jsonl: b69d610920c2b9e896b7ff8a979009c8dc80b1de2d46d323c98247131c67c55c
- evidence/restricted-results-v3-f9-semidirect.md: 33f7681038fc50af66d12d45c37ea2409dbb693a6a14853a220c7a56ebde9a1c
- code/rqls_assay_v4.py: 286951e80d9468f5b3940d844430b02190cd93cd512774fa3b644c51783c346e
- evidence/rqls_assay_v4.smoke.supervisor-config-v2.json: c2caf4742fb87d520593ce214ee545b596099ec51e21f6b8de534d09e263b8a7
- evidence/rqls_assay_v4.sens1.supervisor-config-v2.json: 6ecb869db5a8e98da8eea673aabcf9c5f1b64973318699e7b910a7bdb0827338
- evidence/rqls_assay_v4.sens2.supervisor-config-v2.json: 8ce5ccf06524453b6651a92a3c582f529e280c2c33addd79b402a90707313fa8

## Blocker
v = 10 sensitivity of the solver is unqualified. v4 sensitivity campaign (gates + long unsymmetric runs on a v = 10
B with known classical solutions, v = 9 calibration, Cay(Z_10)/Cay(D_5)) awaits a parent GO.

## Next bounded actions
1. On GO: v4 smoke, then sens1 and sens2 in parallel (<= 3100 s wall each).
2. If RRR cannot converge at v = 10 even on Parker B, switch method (penalised LM / continuation from QLS-only
   solutions) or structural ansatz with analytically eliminated inf-lines; written work meanwhile.
