# Checkpoint 012 (rqls10 continuation, successor worker)

Recorded 2026-10-19T03:02:06-0700 (from /bin/date). Owner ContinueRQLS10b. Target OPEN / UNKNOWN; no candidate. No
process running (R9 SETTLED, independent census empty, lane tmp/ empty).

## Actual results since 011
- Parent GO for ONE R9 run (RUN/review/rqls10-v9-r9-parent-GO-v1.json c406e6b1...06d0, launch owner = this worker),
  received 02:47. Launched exactly once 02:48:26 (gate PASS ac37a6ef...212a; supervisor 55967, child 55969 = PGID);
  launch reported to Main with paths/SHAs; EXITED rc 0 03:00:56, SETTLED; settlement reported to Main.
- Result (receipt evidence/rqls_assay_v9.r9.sv2.receipt.md eef2a8a8...628f): all 13 gates PASS; R9 = 24 classes x 64 =
  1,536 runs, 10 verified endpoints, all classical (10 rays), 0 maximal; model-defect screen 0. Scoped UNKNOWN.
- Analysis script code/rqls_assay_v9_r9_analysis_v1.py (76fb109d...3aca) frozen before the output existed, self-tested on
  the v8 JSONL (reproduced the audited v8 counts; self-test output written outside the lane at
  /private/tmp/rqls_v9_analysis_selftest_on_v8_0249.json); output evidence/rqls_assay_v9.r9.analysis-v1.json (6ae901e3...1ce2).

## Files since 011 (sha256)
- checkpoints/011-checkpoint-v1.md 0ca123da3915777ceda8db5947c59abd28a8524ba9f5cb566dcb91c190722e73 (frozen 02:47 before the GO arrived)
- evidence/stability-gate.v9-r9.v2.json ac37a6ef3f809afc0bd2d719ab3bbb6c169bb41c4a2b2330af8936cf34bb212a
- evidence/rqls_assay_v9.r9.sv2.launch.json e7fa113658fd6a54a2cc88fd9b10290c8f72512d4670a829a733ed9070e6465f
- evidence/rqls_assay_v9.r9.sv2.result.jsonl 2bbc0defba49a9bd65a1757a4eb45b856f1f025d9d250c6f3e49cc0771d9c154
- evidence/rqls_assay_v9.r9.sv2.samples.jsonl bb8c7db1bee5aa4f44a3c283cd93c59da2a162c28764b13ca1242b89f8662d6b
- evidence/rqls_assay_v9.r9.sv2.supervisor-receipt.json 9091f64692393c0d546d291bbd7bb2b4c736e95a3fd2ba05ad01b71309388d1c
- evidence/rqls_assay_v9.r9.sv2.stdout.txt, .stderr.txt e3b0c442...b855 (empty)
- code/rqls_assay_v9_r9_analysis_v1.py 76fb109d9d9583701366d7f387ecf97e5ad534c2d8f7a6c308fd0bfa5e8e3aca
- evidence/rqls_assay_v9.r9.analysis-v1.json 6ae901e3cd6d505c30c0e4ba0ee7b2dce989680d8dccc67516a0c39286221ce2
- evidence/rqls_assay_v9.r9.sv2.receipt.md eef2a8a828584b4ec718df9871baa05acc5f1ff0fb4e2d1ecf65c1ef90f8628f

## What remains
W8 exact closure (E1)-(E4) of evidence/w8-decision-v1-addendum-1.md; WH_10 single-orbit ansatz (proposal, needs a GO
for any float search); no further R9 runs requested.
