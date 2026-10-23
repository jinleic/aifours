# Deviations record, worker ContinueRQLS10b (v1)

Recorded 2026-10-19T02:34:18-0700 (from /bin/date). Append-only by new versions; this file is not edited after freezing.

- D-1 (2026-10-19T02:14, probe z5_flat_rank2_projectors_v1): two bookkeeping thresholds were wrong (MUB-pair block-norm
  test 1e-6 below the ~6e-6 stopping displacement at degenerate zeros; kernel-count cut-off 1e-18 inside round-off). Raw
  data intact; correct reading in evidence/z5_flat_rank2_projectors_v1.receipt.md; classification redone in v3-v5.
  No claim rests on the v1 labels.
- D-2 (2026-10-19T02:22:32, probe w8_flat_planes_couples_v2): crash (ZeroDivisionError in frame()) after its search
  stage; EXIT 1, no output file; settled. Superseded by v3 (single fix).
- D-3 (written 02:26-02:29): four files carry a "Recorded" time that was ESTIMATED from an earlier /bin/date reading
  instead of read from /bin/date: evidence/z5_flat_rank2_projectors_v1.receipt.md ("02:26:00", earlier reading 02:25:07
  quoted), review/rqls10-r9-GO-request-v1.md ("02:28:30"), evidence/z9p1_resolution_classes_v1.receipt.md ("02:29:00"),
  evidence/w8_flat_planes_couples_v3.receipt.md ("02:29:30"). /bin/date at the end of that writing was
  2026-10-19T02:28:44-0700, so the last two stamps are later than the actual write. The /bin/date readings quoted inside
  those files (02:25:07, 02:27:18) are the true anchors. Files are frozen and not edited; from 02:29 on every stamp is a
  literal /bin/date reading.
- Note (not a deviation): the float probes are stdlib-only, <= 300 s, single process, launched with PID = PGID recorded
  by a wrapper before work; they are labelled evidence-only and no impossibility claim uses them as a premise.
