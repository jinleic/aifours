# rqls10 (phys-2) 96-hour continuation lane - navigation (written 2026-10-19T01:09:41-0700)

Target (unchanged): maximal-cardinality 1-RQLS(10). **Status: OPEN / UNKNOWN.** No candidate witness, no unrestricted
no-go. Receipts and notes are the authority; this README is navigation only. Worker: ContinueRQLS10 (Claude subagent;
model as declared by the harness, anthropic/claude-opus-5-5). Parent declared openai-codex/gpt-6-astra.

## Plan, registry, checkpoints
- review/plan-v1.md (6c6a02c2b56d9034e2c46ec151dbffd63fc361acc98a6abf0fb0296fd7190732); review/stop-registry-v1.json (95f0ac093c23ef26a403dca52132ea9bb176b2295796ff5417090ed32fef97d5);
  review/stop-registry-v2.json (a47bb3ffbff22c0f15b1d7fba186812c27ac925ec77a73c76b1d7eb3f639acb7, adds S-NEW-1 latched on rqls_assay_v2).
- checkpoints/001..005 (latest 005: bbfe01170ab907e78afcc96b277242f6823f48407f81627d9b0fdc2026d466b2).

## Written results (lane-internal, unreviewed, restricted unless stated)
- W1 R1-R10 re-derivation: evidence/r-items-validation-v1.md (5762556ce331bf1e29cbada09789d85d691566a1a45a73d806fa4e3cf0a99652).
- W2 cyclic Z_n+h ansatze: evidence/w2-cyclic-quasidifference-v1.md (7f224d30da658d69f4371226505cdefd4fdd13eec700c5f7ded9538bd865875a) +
  erratum-1 (90073e5d21630aa06d037c8f8c34c86c83c12588d56f776aa84b947479dee5f3).
- Classical first-order deformation theory: evidence/classical-tangent-theory-v1.md (733e454838a352094405e17036dfc1b854d23d09104d7124f0c3d6301cda75a3).
- F_9 x| H + inf exclusions: evidence/restricted-results-v2-agl19.md, evidence/restricted-results-v3-f9-semidirect.md
  (33f7681038fc50af66d12d45c37ea2409dbb693a6a14853a220c7a56ebde9a1c).
- D_5 regular orbit: evidence/w7-d5-regular-orbit-ansatz-v1.md + erratum-1 (64ce1b83fb8974f31e02fe4f4a8c83caa56337a76793733b0933854d1a389f15).
- R11 linear Z_5^2 orbit for Cay(Z_10): evidence/restricted-results-v4-z5sq-linear-orbit.md (30b3a3a0f68e78f455160d111615aeb14c8ee9c85b86270b7439f5b64c3fc469).
- W8 WH_5 (x) C^2 setup (not run): evidence/w8-wh5-c2-orbit-ansatz-setup-v1.md (bedfe9a7b35771f4c4e119c8431535d839c87180170bc67523fee6c6c5ce6471).

## Exact stdlib probes (initial scope; receipts)
- Redei p=5: evidence/redei_p5_exhaustive_v1.receipt.md; classical Z_7+3 pairs: evidence/parker_z7p3_classical_v1.receipt.md;
  tangent counts: evidence/classical_tangent_count_v2.receipt.md; classical Z_9+1 pairs + rigidity:
  evidence/z9p1_classical_search_v1.receipt.md, evidence/classical_tangent_count_z9_v1.receipt.md; R11 computations:
  evidence/z5sq_twoplex.receipts.md; checker v2 controls: evidence/exact-checker-v2-controls.receipt.md;
  stability gate v2 self-test: evidence/gate-selftest-v2.receipt.md.

## Parent-GO numerical runs (float only, not certificates)
- v2 smoke: GATE_FAIL at C2 (S-NEW-1): evidence/rqls_assay_v2.smoke.sv2.receipt.md.
- v3 smoke PASS; v3 full (no v=10 solution, v=10 sensitivity unqualified): evidence/rqls_assay_v3.full.sv2.receipt.md
  (04031d5706e5627a00e5e19b10e8719ca1c2a2a58e48fa51b449b38996e96c4c) + addenda 1-2.
- v4 smoke PASS (C1p polisher negative control): evidence/rqls_assay_v4.smoke.sv2.receipt.md.
- v5 smoke: gates + A5 pass, K = 0/8 recoveries (red1 held): evidence/rqls_assay_v5.smoke.sv2.receipt.md.
- Pending, NOT run: v7 K-only calibration (code/rqls_assay_v7.py fed4be6ab718a1630a1272f554c988f382a22c1167a25e37518b6eb87fa547f4, config
  evidence/rqls_assay_v7.kcal.supervisor-config-v2.json); parked, not requested: code/rqls_assay_v6.py.

## Tools
- code/owned_supervisor_v2.py (1fece595258d7ba448875c407e8b221bdbd01966824dc267147c316ef54115aa), code/stability_gate_v2.py (1f62874aff9b22657a90f180b81c678117fd703afe2345f7576454e0faae008a),
  code/exact_rqls_checker_v2.py (5bcdd698e228264af0b814e47113fc796bf73c7106c5ecac1f2d03ff6d09e8f7).
