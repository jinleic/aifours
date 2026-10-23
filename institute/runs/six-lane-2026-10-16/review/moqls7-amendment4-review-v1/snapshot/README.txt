Snapshot map (pinned 2026-10-18T01:17:18-07:00; lane/ and parent/ copies are byte-identical to the sources in manifest.json;
prior/ files are line-numbered excerpts). Text only: NO CNF, proof, FIFO or binary file is included.
Lane root L = /Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum
Parent review root R = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review

UNDER REVIEW (exact pins; all must match manifest.json):
  lane/review/drafts/AMENDMENT-4.r1.md         ef87fa49...abb1  draft r1, NOT FROZEN, INACTIVE (own row/column-frame cuts for C311)
  lane/code/k3_cuts_r1.py                      0ec92c86...1b0a  cut generator + controls (ran once; clause block hashed, not written)
  lane/review/AMENDMENT-4.GENERATOR.r1.json    4c23ec44...5dd3  pin record of the generator (before execution)
  lane/evidence/k3cubes/cuts_r1_receipt.json   9cfc0e81...babbf generator receipt
  lane/review/K3-Q4-SIDECAR.r1.json            34bb5251...16e5  provenance sidecar for the old Q4 binding findings
  lane/review/K3-ERRATA.r1.md                  85fa93fa...c662  text errata E1-E8
  lane/evidence/k3cubes/bmap_oracle_r1.json    6e2bd95e...952c  runtime B-map oracle receipt
  lane/code/bmap_oracle_r1.py                  13f4a5e6...cd8e  runtime B-map oracle
Also new in this phase: lane/review/K3-BMAP-ORACLE.r1.json (oracle pin record), lane/code/k3_direct_B_r5.py (oracle-gated
B certificate driver), lane/review/K3-DIRECT-B-DELTA.r4.json, lane/evidence/k3cubes/cert_B_r4/B_C321.json (pre-oracle B
attempt, UNKNOWN), lane/evidence/PARENT-K2-K3COVER-0046.json (worker record of the parent 00:46 notice),
lane/archive/AMENDMENT-4.interim-2347.unreviewed-draft.md (retired interim text).

OLDER SOURCES (referenced by the reviewed files and by the earlier K3 cover review):
  lane/review/: drafts/AMENDMENT-4.md (old draft d9794b9d...47d7ee), AMENDMENT-2.r1 (+bindings), G6-G2-DERIVATION.r1,
                AMENDMENT-3.r1 (+bindings), GRAM-ENCODING.r2 (current G1-G5 text; r1 superseded, included because older
                texts cite it), LEMMAS.md, K2-THEOREM.r2 (parent-accepted text), K3-CERTIFICATION-DRIVER-DELTA r2/r3.
  lane/code/:   gram_enc.py (encoder A), gram_encB.py (encoder B), k3_cubes.py (cube wrapper), k3_lex.py (lex wrapper),
                k3_cube_certify_r2.py (driver of the A/C321, A/C411 receipts), k3_cube_certify_r3.py (in-memory regeneration helper).
  lane/evidence/k3cubes/: coverage_r1, g6_controls_r1, lex_controls_r1, no_duplicate_regen_controls_r1;
                cert_r2/A_C321.* and A_C411.* (producer receipts, metadata, solver/checker logs, checkpoints; CNF not copied).
  lane/explore/k3cubes/: metadata of the six cube CNFs (A/B x C311/C321/C411) and screenA_r1 receipts.
  lane/explore/k3lex/: metadata of the A/C311 lex CNF and its two interrupted screen receipts.
  lane/README.md: lane protocol (section 0, frozen 2026-10-17 16:59 PDT) and worker status log. lane/evidence/LOG.md: worker log.
  parent/: K1 parent verdict, K2 parent verdict, K3 cover parent disposition.
  prior/: findings-only excerpts of the earlier K3 cover review (desk RESULT, Codex note, Claude note). DELTA AUDIT ONLY.

STATUS FACTS at pin time (from the records and the parent's assignment; not conclusions of this review):
- K1 parent-ACCEPTED. K2 parent CORRECTNESS-ACCEPTED (computer-assisted, 2026-10-18 00:42:18 PDT). M(7) is still 2 or 3.
- K3 cover parent disposition: Q1 cover, Q2 G6/maps, Q3 lex ACCEPTED with text fixes; Q4 FIXES REQUIRED (provenance only);
  Q5 old draft NOT FROZEN.
- C321 (d598507d...8388) and C411 (2b92f5b1...ddf2): producer A-route DRAT certificates only. Parent replays of both are
  RUNNING; the oracle-gated B/C321 certification is RUNNING; B/C411 has not started. No parent verdict accepts either cube.
- C311: original A screen UNKNOWN at its 1800 s cap; both lex screens UNKNOWN safety stops (free-space floor). No C311+cuts
  CNF, solve, proof or receipt exists. AMENDMENT-4.r1 is NOT FROZEN and INACTIVE.
- manifest.json source_mtime_pt values are filesystem modification times observed at pin time, not attestations.
