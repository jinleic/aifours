# Checkpoint 018 (rqls10 continuation, successor worker)

Recorded 2026-10-19T04:45:27-0700 (from /bin/date). Owner ContinueRQLS10b. Target OPEN / UNKNOWN; no candidate. No
process of this worker running; lane tmp/ empty.

## Events since 017
- 04:29 exact stdlib probe wh10_flat_system_v1 (PID 81837, EXIT 0, 0.64 s): all checks pass. Result
  evidence/wh10_flat_system_v1.result.json 81b5c12b71062ec8b63461f2b1e98f07989f78a1aa3aab04d0c33b48887deaeb; receipt
  evidence/wh10_flat_system_v1.receipt.md 91fc6d602e8dc8c8281d099ea2313a7624c373bb6ff351ea6e5bf60285143a6c.
- Parent STOP of the WH10 construction route (prior published obstruction: Grassl-McNulty-Mista-Paterek arXiv:1611.08962
  Sec. V / Table I; parent note RUN/review/rqls10-WH10-prior-obstruction-parent-v1.md d5013204...a9). Preserved, not
  continued: evidence/wh10-flat-planes-v1.md frozen as written before the STOP (52a4536a...35b3); status addendum
  evidence/wh10-prior-art-addendum-v1.md 888261b662ce08662a72af5feb0982f6817895e9b6df6a9b36c87aede7c3120f. ACK sent to Main.
- New lever (parent IRC): fixed-B model with NO orbit symmetry, q_ij = U_i e_j, U_0 = I; source-screen Hall-Paige /
  quantum complete-mapping no-gos for B = Cay(Z_10); exact v = 7 and v = 8 maximal anchors through the same path plus
  near-anchor recovery mandatory; no numpy GO yet.
- 04:37 exact stdlib probe fixedb_anchors_v1 (PID 82955, EXIT 0, 0.14 s): Huang-Li v = 7 (non-affine complete mapping
  of Z_7, cyclic B) and Zhang-Cao v = 8 Example 3.3 (XOR B) verified EXACTLY in U-form (49 / 64 rays, U_0 = I); controls
  pass. Code 87069e53...431b, launch e3145094...d5ea, result 13d6ed64...2b95, receipt
  evidence/fixedb_anchors_v1.receipt.md dee13731c6e548854b4222b385bb8d2c1426986344b4d25019de7347f8327d4e.
- Source screen (in progress): lane sources Zhang-Cao, Huang-Li, Ball-Simoens read for Cay / complete-mapping
  statements; added sources/han-zang-zhang-tian-2507.20154.eprint (3f85d526...891; downloaded into lane tmp/ then moved,
  tmp/ empty again). No quantum Hall-Paige statement found so far. Read-only scout UnsymPathScout is extracting how the
  earlier unsymmetric RRR path (rqls_assay_v3/v8 unsym) chose B and what it found.

## Plan
1. Design note evidence/fixedb-unitary-model-proposal-v1.md: model, B choice with source screen and headroom argument,
   calibration ladder (v = 4, 5, 6 imported negatives / classical-only; v = 7 / 8 exact anchors + near-anchor; v = 8
   Cay(Z_8) discriminating probe), immediate-stop protocol copied from rqls_wh10_lm_v2.
2. Frozen numpy source + supervisor config + GO request (no launch without GO naming this worker).
3. Stdlib validation of residual/Jacobian definitions on the exact anchors (initial scope).
