# Deviations record, worker ContinueRQLS10b (v2; supersedes v1 272d54e40757f8cd0ab913a02682fa164f3eddf1d7d3700aa8adaff2ada09fe9)

Recorded 2026-10-19T02:41:28-0700 (from /bin/date). D-1 to D-3 unchanged from v1 (summarised); D-4 new.

- D-1 (02:14, z5_flat_rank2_projectors_v1): wrong bookkeeping thresholds (MUB-pair label, kernel count); data re-read in
  its receipt; classification redone in v3-v5. No claim rests on the v1 labels.
- D-2 (02:22, w8_flat_planes_couples_v2): crash in frame(), EXIT 1, no output; superseded by v3.
- D-3 (02:26-02:29): four "Recorded" stamps estimated instead of read from /bin/date (z5_flat_rank2_projectors_v1.receipt.md,
  rqls10-r9-GO-request-v1.md, z9p1_resolution_classes_v1.receipt.md, w8_flat_planes_couples_v3.receipt.md); actual
  /bin/date after that writing 2026-10-19T02:28:44-0700; true anchors quoted inside.
- D-4 (found 02:36, w8_flat_planes_couples_v3/v4): the strict couple-compatibility rule (relative lambda_1 < 1e-18)
  undercounted compatible pairs: v5 shows a clean gap (lambda_1 <= 10^-16.2 or >= 10^-0.96) and with a rule inside the
  gap the counts are MUB-MUB 90/90/90 and exotic-exotic 20/20/20 (not 83/67/75 and 13/18/15 or 16/17/14 as in the v3
  receipt 6f43db55...e5a and the v4 run). The v3/v4 K4 statements stay true for the assignments they list; the
  gap-justified v5 rule confirms that no K4 assignment contains an exotic plane; the extra all-MUB assignments are
  covered by the written Theorem A. Correct counts: evidence/w8_flat_planes_couples_v4_v5.receipt.md.
- Tool-side note (not a lane-contract item): one bash call used /usr/bin/tail on df output (02:09); no effect on files.
