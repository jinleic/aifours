# Preregistered guard qualification plan v5 for code/owned_supervisor_v9.py (DRAFT, UNFROZEN; written only)

Drafted 2026-10-19T07:3x (from /bin/date at freeze). Author ContinueRQLS10b. Supersedes
evidence/owned_supervisor_v7-guard-qualification-plan-v4.md (1de3fce1...9ebca, never used) after the Codex HOLD on package
v4 (RUN/review/rqls10-guard-qualification-v4-codex-v1.prompt.stdout.txt 9ba728d1...6f26). Kept unfrozen until the
parent's Codex source review of supervisor v9 (freeze record RUN/review/rqls10-owned-supervisor-v9-source-review-freeze-v1.json)
returns; interface corrections are then folded into ONE frozen package with a per-finding map. Nothing is executed and
no GO is requested by this draft. A PASS of any control qualifies only that observed control on this host and runtime.

## Sources
- supervisor code/owned_supervisor_v9.py c7674b907a37297cc35758ce994983b5b6878c07f994b387225e422a3283a1cd (frozen)
- test child code/guard_qual_child_v6.py, config writer code/guard_qual_configs_v5.py, checker
  code/guard_qual_check_v5.py (drafts; sha256 fixed at package freeze)
- dependencies (unchanged, previously approved): code/stability_gate_v2.py
  1f62874aff9b22657a90f180b81c678117fd703afe2345f7576454e0faae008a reading the parent observer v3 stream (observer
  source RUN/control/resource_observer_v3.py fe311f28d122310da004d0968272ae294a99757756b4898f0d9db4cb13f04196); the gate
  writes exactly one file, RUN_DIR/stability.json, and starts only its own /bin/date calls.

## Confinement
One fresh qualification root QROOT = <lane>/qual-pkg-v5 (real directory chain validated before any creation; created by
the writer if absent). Per scenario RUN = QROOT/<scenario> (must not pre-exist): config.json, tmp/, pinned-scratch.txt
(mutate_pin only), go.json (parent, exclusive), stability.json (gate), supervisor-summary.txt (parent capture of the
supervisor's single stdout line, exclusive), check.json (checker, exclusive), parent-*.json (parent records) - all
OUTSIDE the supervisor output root RUN/out, which is empty at admission and holds only the supervisor's declared files,
the child's declared output, and (stray_file) the intended stray file. mutate_* targets are exactly this scenario's
fixture (RUN/pinned-scratch.txt) or this scenario's own launch record (RUN/out/launch.json), opened without creation
and without following symlinks, regular with one link, fixture content verified before the one-byte append.

## Per-invocation parent transaction (one scenario at a time; nothing advances on file existence, shell rc or checker
PASS alone)
1. Authorization: the parent writes an exclusive authorization record for exactly this config sha256 with the current
   reservation totals and the slots it allocates: 20971520 bytes and cpu_slots 1, except busy: cpu_slots 2 (both CPU
   slots, independent of its trip threshold busy_limit 1). It then writes RUN/go.json exclusively, listing exactly this
   config with the writer's GO entry (go_unlisted: a GO that does not list it).
2. Run: fresh code/stability_gate_v2.py (projected 20971520 bytes) && /opt/homebrew/bin/python3.14 -I -B
   code/owned_supervisor_v9.py RUN/config.json (cwd lane, tool timeout 0); the parent stores the supervisor's single
   stdout line in RUN/supervisor-summary.txt (exclusive) and records the exit code.
3. Check: code/guard_qual_check_v5.py <scenario> -> RUN/check.json (exit 0 only for PASS).
4. Ended processes: read-only confirmation by the parent that every identified test process has ended - the child
   (launch-record identity), reported descendants (child-out.json grandchild / zombie / holder pids, the IDS stdout line
   of busy2 and rss, final-census blocking pids) and every /bin/date helper (receipt helpers list). No signal is sent;
   the parent waits at most until each process's own lifetime bound (LIFE_S from the child start; escapes 40 s, ignore
   and identity 60 s) plus a margin; a process still alive after that HOLDs the sequence with reservations retained.
5. Late-artifact audit and disposition: the parent lists RUN/out; every name not in the receipt's inventory must be the
   documented late child-out.json of ignore/identity with a birth time after the receipt's decision epoch (anything else
   HOLDs). The parent then writes a NEW exclusive disposition record binding the authorization, supervisor exit and
   summary, verified receipt/settlement digests, checker verdict, ended-process evidence and late-artifact audit; only
   that record releases the reservation and CPU slots and allows the next invocation. An UNSETTLED receipt remains
   immutable; a disposition never turns it into SETTLED and never claims scientific success.

## Timing (nominal, not enforced bounds)
Admission includes two complete censuses 2 s apart; a launched control then runs max_wall_s (10 or 60 s) at most before
DEADLINE, plus settle_s 20 s of observation; FINALIZE_ALLOWANCE_S (120 s) is only admission arithmetic. Individual
operations have deadlines; native calls cannot be interrupted (overruns fail closed on return). The child's own
lifetimes are enforced by the child: GO wait bounded by LIFE_S from the child's start, non-blocking flood writes, the
double-fork grandchild sleeps only the remaining lifetime, descendant errors exit 1 with a traceback.

## Scenarios and preregistered expectations (checker v5 EXPECT; settle_s 20, sample_s 1, lane walk 5 s)
Order: date_fault, go_unlisted, ok, rc_nonzero, missing_output, mutate_pin, mutate_evidence, stray_file, deadline,
flood, busy, rss, zombie_hold, escape_slow, escape_fast, double_fork_escape, ignore, identity.
| scenario | settlement / exit / child rc / loop | trips | exact failure codes | signal / stop | identity proof |
|---|---|---|---|---|---|
| date_fault | NOT_LAUNCHED / 10 / - / - | - | HELPER_FAULT_INJECTED; admission DATE_HELPER_UNAVAILABLE, STABILITY_AGE_UNVERIFIABLE, FAILURE_LATCHED | none | - |
| go_unlisted | NOT_LAUNCHED / 10 / - / - | - | none; admission GO_DOES_NOT_NAME_THIS_CONFIG only | none | - |
| ok, rc_nonzero | SETTLED / 0 / 0, 3 / EXITED | - | none | none | child-out pid = launch identity; ok stdout exactly 3 lines |
| missing_output | UNSETTLED / 11 / 0 / EXITED | - | REQUIRED_OUTPUT_MISSING | not sent (reaped) / FAILURE | - |
| mutate_pin | UNSETTLED / 11 / 0 / EXITED | - | PIN_CHANGED_OR_UNREADABLE | not sent / FAILURE | fixture = bytes + b"x" |
| mutate_evidence | UNSETTLED / 11 / 0 / EXITED | - | EVIDENCE_MUTATED | not sent / FAILURE | launch.json = published bytes + b"x" |
| stray_file | UNSETTLED / 11 / 0 / EXITED | - | UNDECLARED_ENTRIES | not sent / FAILURE | stray.txt content |
| deadline | SETTLED / 0 / -15 / EXITED | DEADLINE | none | sent / DEADLINE | trip after mono_spawn + max_wall, timeliness bound arithmetic |
| flood | SETTLED / 0 / -15 / EXITED | STREAM_CAP | none | sent / STREAM_CAP | bytes_seen > cap, written = cap = file size, digest |
| busy | SETTLED / 0 / -15 / EXITED | BUSY | none | sent / BUSY | IDS busy_pids [child, grandchild] = busy pids of a sample with lane_busy 2 and of the trip detail |
| rss | SETTLED / 0 / -15 / EXITED | RSS | none | sent / RSS | IDS rss_pid = child; a sample with the trip's lane_rss > rss_trip |
| zombie_hold | SETTLED / 0 / 0 / EXITED | - | none | none | reported zombie pid in a sample's blocking_zombies |
| escape_slow, escape_fast | UNSETTLED / 11 / 0 / GRACE_EXPIRED_AFTER_CHILD_EXIT | - | GRACE_EXPIRED_AFTER_CHILD_EXIT, BLOCKING_LIVE, STREAMS_NOT_CLOSED, SINK_THREADS_NOT_FINISHED | not sent / FAILURE | final census blocking = [reported grandchild] |
| double_fork_escape | UNSETTLED / 11 / 0 / GRACE_EXPIRED_AFTER_CHILD_EXIT | - | GRACE_EXPIRED_AFTER_CHILD_EXIT, BLOCKING_LIVE | not sent / FAILURE | final census blocking = [reported grandchild] |
| ignore | UNSETTLED / 11 / - / GRACE_EXPIRED_AFTER_STOP_REQUEST | DEADLINE | GRACE_EXPIRED_AFTER_STOP_REQUEST, CHILD_NOT_REAPED, BLOCKING_LIVE, STREAMS_NOT_CLOSED, SINK_THREADS_NOT_FINISHED | sent / DEADLINE | final census blocking = [child]; late child-out.json audited |
| identity | as ignore | DEADLINE | as ignore + IDENTITY_UNVERIFIED | not sent / DEADLINE | as ignore |
Every launched scenario additionally requires: config reconstructed exactly from the writer template; per-invocation GO
listing exactly this config; receipt, settlement record (same inode as its .staged link, two links) and captured summary
mutually bound by the checker's own digests; summary acknowledged with the expected exit code and post_publish_mono after
the decision; artifacts and evidence digests equal to the checker's own reads; output-root listing equal to the expected
names; non-empty samples, all strictly parsed with a census, lane_busy <= 2, strictly increasing monotonic times, count,
bytes and maxima equal to the receipt; helper log only OK or refused-after-latch outcomes and every helper SETTLED;
signalled SETTLED controls: post_publish_mono within 7 s of mono_sent and of the trip. lane_busy <= 2 is SAMPLED
evidence, not a continuous cap.

## Not exercised (an unexpected occurrence HOLDs the sequence with reservations retained)
Real /bin/date failure or overrun, helper descendants and group-check failure (date_fault is an injected branch that
spawns nothing; identity bypasses the fresh comparison); supervisor exceptions and the exception observation path; GO
expiry, GO reuse and chunk-limit refusals; FREE, OUTPUT and LANE_CEILING trips; supervisor cancellation; stderr and
sample caps; capture, publication and directory-sync failures; incomplete final census; PID reuse; native-call
latency bounds.
