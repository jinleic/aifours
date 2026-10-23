# Checkpoint 004 (rqls10 continuation)

Recorded 2026-10-19T00:51:10-0700. Owner ContinueRQLS10.

## Claim / actual result
- Target OPEN / UNKNOWN; no candidate.
- v4 control smoke (GO 743df986...) PASSED with the new non-vacuous polisher negative control C1p (20 forced
  Gauss-Newton steps leave v = 6 residuals 2.10 / 2.26). Stability gate v2 (observer_start schema pinned) passed its
  12-fixture self-test and the real stream.
- Independent exact checker v2 (trace-form zero test, Cauchy-Schwarz parallelism) reproduces all five old controls.
- New restricted result (written): the D_5 regular-orbit ansatz (B = Cay(D_5), K = D_5 x D_5 acting regularly) is
  impossible at any cardinality: the only admissible alpha-twisted representation classes contain a 2-dimensional block
  where three anticommuting reflections would need a zero Bloch vector (W7 erratum; the W7 v1 "survives" claim is
  withdrawn). With R4, all regular group-orbit ansatze of order-10 groups are excluded except Weyl-Heisenberg Z_10.
- Calibration-solution statistics recorded (v = 7: overlaps {0, 1/7, 2/7}; v = 8: two inequivalent maximal
  solutions; a continuum claim was withdrawn in addendum 2).

## Files (sha256)
- evidence/rqls_assay_v4.smoke.sv2.receipt.md: f384a2e86b291edbab614d86ec903b9932c605e683574c4c5f8786b6a7bf1d75
- evidence/gate-selftest-v2.receipt.md: e1c4e43d24f0283be8b0c474c8f288924d2165362de0181bc2a36c3401dcd400
- evidence/exact-checker-v2-controls.receipt.md: 41f83b8886c3e3c5f8fd61374c1a28afb4b2f8d2d032dcdb9f257ca464ec1bdb
- code/exact_rqls_checker_v2.py: 5bcdd698e228264af0b814e47113fc796bf73c7106c5ecac1f2d03ff6d09e8f7
- evidence/w7-d5-regular-orbit-ansatz-v1.md: 1914432707680ddba97caecf38e1fedca3a2fcf646bc3f86d94ddb8b744f4446
- evidence/w7-d5-regular-orbit-ansatz-v1.erratum-1.md: 64ce1b83fb8974f31e02fe4f4a8c83caa56337a76793733b0933854d1a389f15
- evidence/rqls_assay_v3.full.sv2.receipt-addendum-1.md: 95edcb99d3910bbda697f97072fb02c980e477447f483b3021ca0ffb7a1fd2e3
- evidence/rqls_assay_v3.full.sv2.receipt-addendum-2.md: 5e373d25f25ce1c6d92e1f371564091440e9b5dd1b20c32ec05fd1b187c220ed
- code/rqls_assay_v5.py: 598c86777244a8644d8abf04cd3ec06e23e25c5bc7f89779baa53666682a12cf
- review/rqls_assay_v4_to_v5.diff: 92c993a840f795e566e52527a29dda7437a6435a1bd3b7b381c3d58c8df00d83

## Blocker
v5 (reduced-LM forced Z_n + h) smoke awaits parent GO (requested with the v4->v5 diff).

## Next bounded actions
1. On GO: v5 smoke (gates + A5 + 8-start recovery K), then red1 only after parent check.
2. Prepare v6 stages: local excess at stored maximal v = 7/8 solutions; Z_5+5 reduced LM; WH_10 orbit LM (R4 open case).
