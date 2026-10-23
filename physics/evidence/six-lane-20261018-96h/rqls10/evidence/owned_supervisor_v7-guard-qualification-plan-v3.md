# Preregistered guard qualification plan v3 for code/owned_supervisor_v7.py (NOEXEC; parent review and explicit GO)

Recorded 2026-10-19T06:51:57-0700 (from /bin/date). Author ContinueRQLS10b. Supersedes
evidence/owned_supervisor_v6-guard-qualification-plan-v2.md (e75dff40...0a07, never used) because the v7 contract changed
(Codex v5 review disposition review/rqls10-owned-supervisor-v7-disposition-v1.json). Nothing has been executed; only
parse-only static checks of sources. A PASS qualifies only the observed guard behaviours on this host and runtime; it
admits no scientific run and no Phase 1.

## Sources (all 0444)
- supervisor code/owned_supervisor_v7.py a45f8538d86cf021a04d816fad9c5ac2392cac016b286bedb9dcb64ad8f8d2fa
  (cumulative diff review/owned_supervisor_v5_to_v7.diff d56d32f8...e7ee)
- test child code/guard_qual_child_v4.py f4c1d03c454db222a4dff2770048b0809ddd8748df1406d5a7b1c66ca01a0e6d
- config writer code/guard_qual_configs_v3.py 4cade860603b371edcf0bea4b5f45ba570f3ee84408952666cdf64b8e85299f2
- checker code/guard_qual_check_v3.py 611d4d434c55861f744ac580bb2aeeaa94d871ef96a9bb0131e829dce54377a4
- stability gate code/stability_gate_v2.py 1f62874aff9b22657a90f180b81c678117fd703afe2345f7576454e0faae008a (unchanged)

## Single parent authority (new in v7)
1. Config writer, once per scenario (metadata only; mkdir RUN, RUN/out, RUN/tmp; exclusive RUN/config.json; mutate_pin
   also RUN/pinned-scratch.txt). It prints the config sha256 and the GO entry for that sha.
2. The parent writes ONE GO file (strict JSON, outside every RUN/out): {"decision": "GO", "item":
   "owned_supervisor_v7 guard qualification", "not_after_epoch": E, "configs": {sha256: entry, ...}} listing every
   scenario config EXCEPT go_unlisted, with the entries exactly as printed (output_roots, argv, max_wall_s,
   reservation_bytes 20971520, outstanding_reservations_bytes, lane_outstanding_reservations_bytes). An output root must
   be empty at admission, so each entry admits one launch. Reservations and the busy slot are released only by the
   parent after it has verified each scenario's exit code, stdout summary line, receipt and settlement sha256.
3. Per scenario, sequentially (one at a time): fresh code/stability_gate_v2.py writing RUN/stability.json (projected
   20971520 bytes, parent observer v3 stream) && /opt/homebrew/bin/python3.14 -I -B code/owned_supervisor_v7.py
   RUN/config.json, cwd = lane, tool timeout 0. Supervisor wall <= ~3 s admission + max_wall_s + settle_s (20) + up
   to 120 s finalization allowance.
4. Checker: guard_qual_check_v3.py SCENARIO RUN OUT.json; send launch record, settlement record, receipt and checker
   output (paths + sha256).
5. Before the next scenario: every test process of the previous one has ended by itself (bounded by LIFE_S), confirmed
   read-only. Intended-UNSETTLED outcomes are qualification results that still need the parent's disposition before
   any further launch.
Order: date_fault, go_unlisted, ok, rc_nonzero, missing_output, mutate_pin, mutate_evidence, stray_file, deadline,
flood, busy, rss, zombie_hold, escape_slow, escape_fast, double_fork_escape, ignore, identity.

## Scenarios and preregistered expectations (settle_s 20, sample_s 1, lane walk 5 s, busy_limit 2, stdout cap 1 MiB)
| scenario | child mode / LIFE_S | config specifics | expected (checker v3) |
|---|---|---|---|
| date_fault | ok / 5 | fault date_helper_fails | NOT_LAUNCHED, admission reason DATE_HELPER_UNAVAILABLE |
| go_unlisted | ok / 5 | config not listed in the GO | NOT_LAUNCHED, GO_DOES_NOT_NAME_THIS_CONFIG, empty failure latch |
| ok | ok / 5 | output required | SETTLED, rc 0, no trip, no signal, 4 evidence digests, deadline timeliness recorded |
| rc_nonzero | rc_nonzero / 5 | output required | SETTLED, rc 3 (a nonzero rc is recorded, not a guard failure) |
| missing_output | no_output / 5 | output required | UNSETTLED (REQUIRED_OUTPUT_MISSING), rc 0, no trip, no signal |
| mutate_pin | mutate_pin / 5 | scratch file pinned; child appends 1 byte | UNSETTLED (PIN_CHANGED_OR_UNREADABLE), rc 0 |
| mutate_evidence | mutate_evidence / 5 | child appends 1 byte to out/launch.json | UNSETTLED (EVIDENCE_MUTATED), rc 0 |
| stray_file | stray_file / 5 | child creates out/stray.txt | UNSETTLED (UNDECLARED_ENTRIES), rc 0 |
| deadline | sleep / 120 | max_wall 10 | only trip DEADLINE, one identity-checked group SIGTERM, rc -15, SETTLED |
| flood | flood / 60 | - | only trip STREAM_CAP, SIGTERM, rc -15, stdout.txt exactly 1048576 bytes, SETTLED |
| busy | busy3 / 60 | 3 busy processes in the group | only trip BUSY (first excess), SIGTERM to the group, rc -15, SETTLED |
| rss | rss / 60 | rss_trip 256 MiB | only trip RSS (whole-lane sum), SIGTERM, rc -15, SETTLED |
| zombie_hold | zombie_hold / 10 | holder keeps an unreaped zombie 3 s | a sample shows blocking_zombies; SETTLED, rc 0, no trip |
| escape_slow | escape_slow / 40 | setsid grandchild seen while the child lives | rc 0, no trip, no signal, UNSETTLED (GRACE_EXPIRED_AFTER_CHILD_EXIT, BLOCKING_LIVE) |
| escape_fast | escape_fast / 40 | the child exits at once | as escape_slow (lineage: the grandchild's puniqueid is the child's uniqueid) |
| double_fork_escape | double_fork_escape / 40 | intermediate exits at once; grandchild cwd /, fds closed, exec /bin/sleep | as escape_slow, final census owned_live or unresolved_live non-empty |
| ignore | ignore_term / 60 | max_wall 10 | only trip DEADLINE, SIGTERM sent and ignored, no SIGKILL, UNSETTLED (GRACE_EXPIRED_AFTER_STOP_REQUEST, CHILD_NOT_REAPED); child ends by itself at 60 s |
| identity | sleep / 60 | max_wall 10, fault identity_check_fails | only trip DEADLINE, NO signal, UNSETTLED (IDENTITY_UNVERIFIED, GRACE_EXPIRED_AFTER_STOP_REQUEST, CHILD_NOT_REAPED); child ends by itself at 60 s |
The checker FAILs a scenario on any trip outside its allow-list, any settlement/rc/signal/failure/loop-status mismatch,
unreadable records, a receipt whose sha differs from the settlement record, a staged settlement record differing from
the linked one, and (SETTLED scenarios) a non-empty failure latch, a non-clear final census, GO not delivered,
mismatching evidence digests or missing deadline-timeliness record. It records the raw signal-to-receipt interval.

## Not qualified by this plan
No universal latency bound for native or filesystem calls; no scientific child behaviour; libproc layouts only as far as
these scenarios read them (the uniqueid flavor 17 is new in v7); the fail-closed census only for processes present on
the host during the runs (UNRESOLVED processes of unrelated programs can make a scenario UNSETTLED spuriously; the
receipt names them); the /bin/date overrun path (budget exceeded, SIGTERM, HELPER_UNSETTLED) and the helper group check
failure are not exercised; the GO expiry, one-use (non-empty root) and chunk-limit refusals are covered statically only;
the supervisor's own exception path (SUPERVISOR_EXCEPTION / emergency_observe) is not exercised.
