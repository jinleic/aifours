# zx-check-v1 run1: cooperative stop receipt, v1

Written after host clock 2026-10-18T12:38:09-07:00 by OlsonRotationRigidity.

Decision: parent IRC at about 12:37.  Keep this slice to one busy process.  Stop only the owned zx-check-v1 run1, by
SIGTERM with a bounded wait (never SIGKILL), and preserve all output.  Reason recorded as instructed: superseded aid; the
new frozen residual T-representation search (t-search-v1) has priority.  No accepted theorem depends on this run.

## Stop

- The process was identified by its command line before signalling: pid 41379, parent 61118 (the bash job of the
  11:48:02 launch).  Command: Python -B code/zx_check_v1.py out/run1.jsonl.  Elapsed 49:58 at 12:38:01.
- SIGTERM was sent at 12:38:08.  The process exited within 1 s (bounded wait of at most 30 s, polled with kill -0).  No
  other signal was sent.
- The launching job reported exit=143 at 12:38:08, wall time 3005 s.
- Output files, hashed after the stop:
  - out/run1.jsonl: cf8f4dec4a88807b5dc8eb3d9a500efd54933b9ef4491b5d70eca9953c739f95 (87 lines; START, UNIT_TESTS,
    75 ITEM lines, heartbeats; no DONE line);
  - out/run1.stdout.txt: 5893ffe10894cef65a0d9730a3f7ad161ef4ccba21320ebd6870fa5d4cba8b28;
  - out/run1.stderr.txt: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 (empty).

## Per-item status (78 items in PLAN-v1)

- COMPLETED: 75 items, every one with its ITEM line.  These are all 57 items with p <= 13, then the p = 17 items in
  R order up to and including (17, 10, 8).
  - UNIT_TESTS: all five flags true.
  - Every completed item met EXPECTED-v1: zp2_fail = 0; zx_fail = {}; in ZX-region items s1_fail = 0 and
    conc_fail = 0; in every item with kappa = k - 1, type II was found and passed and M1 fired; found counts equal to
    run1 on all 57 items with p <= 13.
  - Completed items in the plan's "residual" class (2kappa >= p + 1): (7,5,4), (11,7,6), (13,8,7), (13,9,7), (13,9,8).
    Each had s1_fail = 0 and conc_fail = 0.  Found counts were 1, 1, 1, 3, 1.
- UNKNOWN (in progress at the stop): (17, 11, 9).  Its last heartbeat was at 12:38:02, 181,039,104 nodes, elapsed
  3000 s.  No result is claimed.
- NOT_STARTED: (17, 10, 9) and (17, 11, 10).

Disclosed separately in DEVIATION-v1.md: the launch used ulimit -t 9300.  The CPU limit never fired; the stop was the
SIGTERM above.
