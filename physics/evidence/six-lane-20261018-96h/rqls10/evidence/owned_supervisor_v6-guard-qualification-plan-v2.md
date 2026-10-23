# Preregistered guard qualification plan v2 for code/owned_supervisor_v6.py (NOEXEC; parent review and explicit GO)

Recorded 2026-10-19T06:19:39-0700 (from /bin/date). Author ContinueRQLS10b. Supersedes
evidence/owned_supervisor_v5-guard-qualification-plan-v1.md (908e01bf...7827, never used) after the parent's list of
required behaviours (06:1x). Nothing has been executed; only parse-only static checks of sources. A PASS qualifies only
the observed guard behaviours on this host and runtime; it admits no scientific run and no Phase 1.

## Sources (sha256 in the cover message; all 0444)
- supervisor code/owned_supervisor_v6.py (= v5 under Codex review + evidence-mutation digests; diff
  review/owned_supervisor_v5_to_v6.diff). v5 alone would NOT pass mutate_evidence (it re-hashes but has no expected
  digest for its own evidence files); everything else in this plan applies to v5 and v6 alike.
- test child code/guard_qual_child_v3.py (every test process ends by itself within LIFE_S of its own start)
- config writer code/guard_qual_configs_v2.py (metadata only; binds GO, fresh stability receipt, outstanding
  reservations; mkdir + exclusive files; never deletes)
- checker code/guard_qual_check_v2.py (one scenario directory; intended-trip allow-list; exclusive output)

## Procedure (sequential, one scenario at a time, launcher named by the parent's GO)
1. Fresh stability-gate receipt (projected 4194304 bytes); config writer for the scenario; then
   /opt/homebrew/bin/python3.14 -I -B code/owned_supervisor_v6.py <config> with cwd = lane and tool timeout 0.
   Supervisor wall per scenario <= admission (~3 s) + max_wall_s + settle_s (20 s) + finalisation.
2. Checker on the scenario directory; send launch record, settlement record and checker output (paths + sha256).
3. Before the next scenario: every test process of the previous one has ended by itself (bounded by LIFE_S),
   confirmed read-only. Intended-UNSETTLED outcomes are qualification results that need the parent's disposition before
   any further launch (contract: UNSETTLED blocks new launches).
Order: date_fault, ok, rc_nonzero, missing_output, mutate_pin, mutate_evidence, deadline, flood, busy, rss,
escape_slow, escape_fast, ignore, identity.

## Scenarios and preregistered expectations (settle_s 20, sample_s 1, lane walk 5 s, busy_limit 2, stdout cap 1 MiB)
| scenario | child mode / LIFE_S | config specifics | expected (checker) |
|---|---|---|---|
| date_fault | ok / 5 | fault date_helper_fails | NOT_LAUNCHED, admission reason DATE_HELPER_UNAVAILABLE, no child |
| ok (clean exit) | ok / 5 | output required | SETTLED, rc 0, no trip, no signal, 4 evidence digests match |
| rc_nonzero | rc_nonzero / 5 | output required | SETTLED, rc 3, no trip, no signal (a nonzero rc is recorded, not a guard failure) |
| missing_output | no_output / 5 | output required | UNSETTLED (REQUIRED_OUTPUT_MISSING), rc 0, no trip |
| mutate_pin (artifact mutation) | mutate_pin / 5 | scratch file pinned; child appends 1 byte | UNSETTLED (PIN_CHANGED_OR_UNREADABLE), rc 0 |
| mutate_evidence (artifact mutation) | mutate_evidence / 5 | child appends 1 byte to launch.json | UNSETTLED (EVIDENCE_MUTATED), rc 0 |
| deadline (SIGTERM honoured) | sleep / 120 | max_wall 10 | first and only trip DEADLINE, one identity-checked SIGTERM, rc -15, SETTLED |
| flood | flood / 60 | - | only trip STREAM_CAP, SIGTERM, rc -15, stdout.txt exactly 1048576 bytes, SETTLED |
| busy | busy3 / 60 | 3 busy processes in the group | only trip BUSY, SIGTERM to the group, rc -15, SETTLED |
| rss | rss / 60 | rss_trip 256 MiB | only trip RSS (whole-lane sum), SIGTERM, rc -15, SETTLED |
| escape_slow (setsid escape) | escape_slow / 40 | grandchild setsid, seen while parent lives | rc 0, no trip, no signal (escaped processes never signalled), GRACE_EXPIRED_AFTER_CHILD_EXIT, UNSETTLED (OWNED_LIVE) |
| escape_fast (setsid escape) | escape_fast / 40 | parent exits at once | rc 0, no trip, GRACE_EXPIRED_AFTER_CHILD_EXIT, UNSETTLED (OWNED_LIVE or UNATTRIBUTED_NEW_LANE_PROCESSES) |
| ignore (SIGTERM ignored) | ignore_term / 60 | max_wall 10 | only trip DEADLINE, SIGTERM sent and ignored, no SIGKILL, GRACE_EXPIRED_AFTER_STOP_REQUEST, UNSETTLED (CHILD_NOT_REAPED); child ends by itself at 60 s |
| identity (/ uncertain identity) | sleep / 60 | max_wall 10, fault identity_check_fails | only trip DEADLINE, NO signal, UNSETTLED (CHILD_NOT_REAPED, FLAG_IDENTITY_UNVERIFIED); child ends by itself at 60 s |
The checker FAILs a scenario on any trip outside its allow-list (any other guard trip), any settlement/rc/signal/
reason mismatch, unreadable records, a receipt whose sha differs from the settlement record, and (SETTLED scenarios)
any settlement reason, an unclear final census, GO not sent or a mismatching evidence digest. It records the raw
signal-to-receipt interval.

## Not qualified by this plan
No universal latency bound for native or filesystem calls; no scientific child behaviour; libproc layouts only as far as
these scenarios read them; the fail-closed census rule only for processes present on the host during the runs. The
/bin/date helper overrun path (budget exceeded, SIGTERM, HELPER_UNSETTLED) is not exercised (no safe way to make
/bin/date hang); only the helper-unavailable path (date_fault) is.
