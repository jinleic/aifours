# Checkpoint 005 (rqls10 continuation)

Recorded 2026-10-19T01:09:19-0700. Owner ContinueRQLS10.

## Claim / actual result
- Target OPEN / UNKNOWN; no candidate.
- v5 smoke (GO 914e55bb...): gates incl. A5 pass; K = 0/8 random-start recoveries -> red1 held (parent final
  disposition: does not qualify sensitivity). v7 bounded K-only calibration (KP perturbations around the classical
  anchor + 256 random starts) frozen and requested; v6 (broad) parked, not requested.
- New exact restricted results (initial-scope stdlib probes, single kernel):
  * R11: the linear Z_5^2-orbit ansatz for B = Cay(Z_10) (four representatives, 10 character points forming a 2-plex of
    Cay(Z_5)) is impossible at any cardinality: all 130 2-plexes give a rank-27 phase system with an odd-parity integer
    left kernel (no real solution); moduli are forced flat by the K4 triangles.
  * Classical Z_9 + 1 MOLS(10) exist (20 pairs found in 0.02 s); all 40 resulting classical 1-RQLS(10) are locally rigid
    even in the unsymmetric problem (every pair graph connected, excess 0).
- W8: setup note for the projective WH_5 (x) C^2 orbit ansatz (B = Cay(Z_10)), with a p = 3 negative control; not run.

## Files (sha256)
- evidence/rqls_assay_v5.smoke.sv2.receipt.md: 19dda2724df7b592648584498c64bef01fe64d0b030220f8f0130974d25f5566
- code/rqls_assay_v7.py: fed4be6ab718a1630a1272f554c988f382a22c1167a25e37518b6eb87fa547f4
- review/rqls_assay_v5_to_v7.diff: cfcc71587d4d186d952b2e3e362e6c7457f5ec2df61e13da5bd4edbcb3210332
- evidence/z9p1_classical_search_v1.receipt.md: acde6b56b38636b5f8121954154cd3e6d413704125386d741fba20b6991ea700
- evidence/classical_tangent_count_z9_v1.receipt.md: 8e4de06f4260110a786d263513eb55ed9e69a02991533868f5276a30a92ba5b4
- evidence/z5sq_twoplex.receipts.md: 69e687a1cc10eb0021f252826ddd5d574ee096d3c5b7a269b9c571fae2f0bc45
- evidence/restricted-results-v4-z5sq-linear-orbit.md: 30b3a3a0f68e78f455160d111615aeb14c8ee9c85b86270b7439f5b64c3fc469
- evidence/w8-wh5-c2-orbit-ansatz-setup-v1.md: bedfe9a7b35771f4c4e119c8431535d839c87180170bc67523fee6c6c5ce6471
- code/rqls_assay_v6.py: f9bf6b59c174bc30dc18d35fce9c5af126d6af594b68f3e6404812831dc26014

## Blocker
v7 GO pending (parent reading the 166-line delta).

## Next bounded actions
1. On GO: v7 (gate && supervisor, <= 300 s). If KP fails near the anchor, debug Reduced.resid vs full verify/Jacobian
   conditioning with A5 before any more starts.
2. Then propose a cheap WH_5 (x) C^2 LM stage with the p = 3 negative control.
