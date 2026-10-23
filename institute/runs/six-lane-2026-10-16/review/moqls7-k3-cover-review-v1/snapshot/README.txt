Snapshot map (pinned 2026-10-17T23:46:48-07:00; copies are byte-identical to the sources listed in manifest.json).
Lane root L = /Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum
Parent review root R = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review

lane/review/   claim/amendment texts. AMENDMENT-2.r1 (frozen cubes + G6), G6-G2-DERIVATION.r1 (proof-only addendum),
               AMENDMENT-3.r1 (lex leaders, frozen), drafts/AMENDMENT-4.md (UNFROZEN DRAFT, not authorised for any run or cutover),
               GRAM-ENCODING.r2 (current G1-G5 soundness text; r1 included only because AMENDMENT-2 cites it), LEMMAS.md,
               K2-THEOREM.r2 (candidate K2; NOT accepted; independent parent proof replay still running),
               K3-CERTIFICATION-DRIVER-DELTA r2/r3 (driver-only).
lane/code/     k3_cubes.py (cube wrapper), k3_lex.py (lex wrapper), gram_enc.py (encoder A), gram_encB.py (encoder B),
               g6_controls.py, k3_cube_certify_r2.py (certificate driver used for the A/C321, A/C411 receipts).
lane/evidence/k3cubes/  coverage_r1.json, g6_controls_r1.json, lex_controls_r1.json, no_duplicate_regen_controls_r1.json,
               cert_r2/A_C321.* and A_C411.* (producer DRAT receipts + full solver/checker logs + checkpoints + metadata;
               CNFs and proofs are NOT copied).
lane/explore/k3cubes/   metadata of the six original cube CNFs (A/B x C311/C321/C411); screenA_r1/ screen receipts.
lane/explore/k3lex/     metadata of the A/C311 lex CNF and its interrupted screen receipt (safety stop, UNKNOWN).
parent/moqls7-k1-parent-verdict.md   parent acceptance of Theorem K1 (M(7) not decided; K2/K3 not accepted).
desk/cnf-static-excerpts.txt   desk byte excerpts/hashes of CNFs that are not copied.

Status facts (from the receipts/LOG at pin time, not claims of this review):
- K1 parent-ACCEPTED. K2 is a candidate under independent parent replay (not accepted).
- K3: A/C311 original screen UNKNOWN (1800 s); A/C311 lex screen r1 stopped on a free-space safety floor (UNKNOWN) and a
  fresh r2 screen was restarted on the same lex CNF; A/C321 and A/C411 have producer DRAT certificates (rc 20/0,
  exact 's VERIFIED') that are NOT yet parent-accepted. B cube routes are pending.
