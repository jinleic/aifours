# Guard qualification plan for code/owned_supervisor_v5.py (NOEXEC; for parent review and an explicit GO)

Recorded 2026-10-19T06:16:59-0700 (from /bin/date). Author ContinueRQLS10b. Nothing here has been executed; only
parse-only static checks of the sources were run. Integration owner and launcher: the parent (or whoever the parent's
GO names). A PASS of this plan qualifies only the observed guard behaviours on this host and runtime; it admits no
scientific run.

## Sources (pins)
- supervisor code/owned_supervisor_v5.py 83dc4c422d8239f4a9581e1c7e8dd95f0d8094f30b63d074a337a87eea122222
- test child code/guard_qual_child_v2.py (sha in the cover message; v1 superseded, never run)
- config writer code/guard_qual_configs_v1.py (metadata only: mkdir + one exclusive config per call; it sets
  outstanding_reservations_bytes = lane_outstanding_reservations_bytes = 0 and reservation 4 MiB, so the integration
  owner must confirm from the active-launch registry that no retained-output reservation is outstanding, or write the
  configs by other means)
- checker code/guard_qual_check_v1.py (reads one scenario directory; exclusive output)

## Procedure (sequential; one scenario at a time)
1. Fresh stability-gate receipt (stability_gate_v2.py on the live observer stream; projected bytes 4194304), then the
   config writer for the scenario (binds GO + stability receipt), then
   /opt/homebrew/bin/python3.14 -I -B code/owned_supervisor_v5.py <config> (cwd = lane; tool timeout 0; the
   supervisor's own wall is bounded by max_wall_s + settle_s + admission <= about 90 s here).
2. Checker on the scenario directory. Before the next scenario: wait until every process of the previous scenario has
   ended by itself (each test process self-terminates within LIFE_S of its own start; see table), confirmed read-only.
3. Order: date_fault, ok, deadline, flood, busy, rss, escape_slow, escape_fast, ignore, identity (intended UNSETTLED
   scenarios last). Intended-UNSETTLED outcomes block new launches until the parent disposes of them as qualification
   results.

## Scenarios and preregistered expectations (settle_s 20, sample_s 1, lane walk 5 s, busy_limit 2)
| scenario | child mode / LIFE_S | special | expected |
|---|---|---|---|
| date_fault | ok / 5 | fault date_helper_fails | NOT_LAUNCHED (DATE_HELPER_UNAVAILABLE), no child |
| ok | ok / 5 | - | SETTLED, rc 0, no trip, no signal, child-out present |
| deadline | sleep / 120 | max_wall 10 | first trip DEADLINE, one identity-checked SIGTERM, rc -15, SETTLED |
| flood | flood / 60 | stdout cap 1 MiB | first trip STREAM_CAP, SIGTERM, rc -15, stdout.txt exactly 1048576 bytes, SETTLED |
| busy | busy3 / 60 | 3 busy processes in the group | first trip BUSY (2 consecutive samples > 2), SIGTERM to the group, rc -15, SETTLED |
| rss | rss / 60 | rss_trip 256 MiB | first trip RSS (whole-lane sum), SIGTERM, rc -15, SETTLED |
| escape_slow | escape_slow / 40 | grandchild setsid, seen while parent lives | rc 0, no trip, no signal (escaped processes are never signalled), loop GRACE_EXPIRED_AFTER_CHILD_EXIT, UNSETTLED (OWNED_LIVE) |
| escape_fast | escape_fast / 40 | parent exits at once | rc 0, no trip, UNSETTLED (OWNED_LIVE or UNATTRIBUTED_NEW_LANE_PROCESSES) |
| ignore | ignore_term / 60 | max_wall 10 | first trip DEADLINE, SIGTERM sent and ignored, grace expires, UNSETTLED (CHILD_NOT_REAPED); child ends by itself at 60 s |
| identity | sleep / 60 | max_wall 10, fault identity_check_fails | first trip DEADLINE, NO signal, UNSETTLED (CHILD_NOT_REAPED, FLAG_IDENTITY_UNVERIFIED); child ends by itself at 60 s |
Every scenario additionally records: helper_log (all /bin/date calls), samples (bounded), signal mono_sent, stop
request mono, receipt + settlement record publication; the checker copies the raw values and the signal-to-receipt
interval.

## What this does not qualify
No universal latency bound for native calls; no statement about scientific children; libproc struct layouts are
exercised only as far as these scenarios read them; the census fail-closed rule (unreadable same-uid process) is
observed only for the processes present on the host during the runs. Unrelated processes started in the lane during a
scenario make it UNSETTLED by design (v5 rule).
