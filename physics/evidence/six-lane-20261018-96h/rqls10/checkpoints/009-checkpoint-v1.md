# Checkpoint 009 (rqls10 continuation, successor worker)

Recorded 2026-10-19T02:27:18-0700 (from /bin/date). Owner ContinueRQLS10b. Target OPEN / UNKNOWN; no candidate. No process
running (all three probes below settled; lane tmp/ empty).

## Actual results since 008
- W8 written analysis (note in preparation): exact reformulations; flat rank-2 planes P = 2I/5 + A_1 + A_2 + A_3 with A_k
  in the three complementary WH algebras; if one A_k = 0 then P is a "MUB-pair" plane (span of two vectors of one
  complementary WH basis); Theorem: no three representatives can have MUB-pair planes (K4-triangle parity, any frames).
- Float stdlib explorations (evidence only):
  - z5_flat_rank2_projectors_v1 (EXIT 0; bookkeeping threshold defects D-1, data re-read in its receipt);
  - w8_flat_planes_couples_v2 (EXIT 1, ZeroDivisionError, no output; D-2);
  - w8_flat_planes_couples_v3 (EXIT 0): 9,628 starts all converged to 130 flat planes = 30 MUB-pair + 100 "exotic"
    (4 WH-translation orbits); couples never mix MUB-pair and exotic planes; 867 K4 plane assignments pass all six pairwise
    couple tests, ALL fail the frame/holonomy test (min remaining couple residual 0.12360679775 = (sqrt5 - 1)/10); no W8
    solution in this list.
- R9 design: code/rqls_assay_v9.py frozen (e9079686...64db; AST: 37 v8 definitions identical, main changed, 8 helpers
  added); diff review/rqls_assay_v8_to_v9.diff (291edc71...f157); config evidence/rqls_assay_v9.r9.supervisor-config-v2.json
  (a0f04bc0...c3e7). Exact count (z9p1_resolution_classes_v1, EXIT 0): 2,025 Z_9+1 resolution squares with D_inf = {0},
  24 classes, 12 of them contain a known classical resolution. NOT run; GO request next.

## Files (sha256)
- code/z5_flat_rank2_projectors_v1.py be9dd762...a190; evidence/...launch.json 19527d81...3add; result 193bbc47...335
- evidence/z5_flat_rank2_projectors_v1.receipt.md 3fa2eead...fa39 (covers v1 and the v2 failure)
- code/w8_flat_planes_couples_v2.py 7e5b5fd2...626b; launch 8b75b1bb...1571 (no result)
- code/w8_flat_planes_couples_v3.py 232b202f...1c16; launch 0364c585...84d2; result 241219fd...4e5e
- code/z9p1_resolution_classes_v1.py f2dcfead...7186; launch 9e11e233...601d; result 23ebb08a...93f8
- code/rqls_assay_v9.py e9079686...64db; review/rqls_assay_v8_to_v9.diff 291edc71...f157;
  evidence/rqls_assay_v9.r9.supervisor-config-v2.json a0f04bc0...c3e7

## Deviations
D-1 (probe v1 threshold bookkeeping), D-2 (probe v2 crash). Both harmless (stdlib, settled, no claims rest on them).
