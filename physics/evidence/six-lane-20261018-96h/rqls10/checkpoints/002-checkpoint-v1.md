# Checkpoint 002 (rqls10 continuation)

Recorded 2026-10-19T00:00:32-0700. Owner ContinueRQLS10.

## Claim / actual result
- Target unchanged: OPEN / UNKNOWN. No candidate witness, no unrestricted no-go.
- W2 erratum 1: the claim "no maximal Z_7+3 configuration is a deformation of a classical one" is withdrawn (parent
  scope note): classical Parker points admit forced-form U.
- W3 exact (stdlib, receipts): Redei bound p = 5 verified exhaustively (R3 now import-free); five classical Z_7+3
  MOLS(10) pairs found (control data); first-order deformation theory at classical points written and counted exactly:
  unsymmetric excess 6 (three inf-inf trade rotations), forced-U Z_7+3 excess 0 at all ten classical points
  => those points are locally rigid mod gauge in the forced form (restricted, local).
- New restricted exclusion (written): AGL(1,9) + inf symmetric 1-RQLS(10) impossible at any cardinality.
- W4: v1/v2 assay requests revised under parent review (fail-closed gates, capped writer, owned supervisor v2).
  Parent-GO smoke of v2 ran 23:57:46-23:57:56 PDT: supervisor EXITED/SETTLED, no trips; gates A 7/7 and C1 pass;
  **C2 failed (vacuous)**: RRR reaches maxdev ~1e-5 on v = 5 but not 1e-8 (sublinear convergence onto degenerate
  classical solutions). STOP S-NEW-1 latched on v2 (registry v2). Full v2 not run.

## Files (sha256)
- evidence/w2-cyclic-quasidifference-v1.erratum-1.md: 90073e5d21630aa06d037c8f8c34c86c83c12588d56f776aa84b947479dee5f3
- evidence/redei_p5_exhaustive_v1.receipt.md: 8e31e85e87b4390bbb7914b85bd4ed743d0e8093d468c077acad65c725363504
- evidence/parker_z7p3_classical_v1.receipt.md: 545b0624c518c64c8ce8d40a54f730af87a3000a7e4ea897597374c30e70f533
- evidence/classical-tangent-theory-v1.md: 733e454838a352094405e17036dfc1b854d23d09104d7124f0c3d6301cda75a3
- evidence/classical_tangent_count_v2.receipt.md: e0736fd5968acd8b26a1a88fe2b03af01d002f7bdcaf64b12925c1032b99f47f
- evidence/restricted-results-v2-agl19.md: 40534c10d10cb8f170fdba131751b4236989e55589a72be41d1e9cecda6af543
- evidence/rqls_assay_v2.smoke.sv2.receipt.md: 03c750bd5b891a66cce3ee142c5f42526ffdddca875b8898d2964499a81e7470
- review/stop-registry-v2.json: a47bb3ffbff22c0f15b1d7fba186812c27ac925ec77a73c76b1d7eb3f639acb7
- code/rqls_assay_v3.py: 3168e2a34f0cc6f52c26c82e18c4c3ddfee5b67afb380eb81930c084098c8e13
- evidence/rqls_assay_v3.smoke.supervisor-config-v2.json: eccccf9a11c8d228c299cc26d481e532adda8d66df9d782c745ef9c8cdf09a7d
- evidence/rqls_assay_v3.full.supervisor-config-v2.json: 0750bef74524ded3251337c6b68d733aa251afe11d5a1bbe655ddab161b3292c

## Blocker
Numerical assay waits for a new versioned parent GO for child v3 (v2 + Gauss-Newton polish of RRR endpoints; gates
unchanged; smoke first).

## Next bounded actions
1. On GO: v3 smoke (gates), then full only after parent check.
2. Meanwhile (written): sub-ansatz analysis for Z_5+5 and Z_9+1 structure; prepare high-precision polish /
   exact-recognition plan for any lead; independent exact checker only once a candidate's number field is known.
