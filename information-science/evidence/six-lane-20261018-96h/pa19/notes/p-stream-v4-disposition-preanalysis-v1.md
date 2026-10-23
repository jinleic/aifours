# P-STREAM v4 / D2 v32 — pre-analysis of the parent-flagged B1 disposition items (written while parked)

Written 2026-10-19T07:25:16-0700 by ContinuePA19b. This is analysis only: no code was changed, nothing ran, and it is not a review result.
It concerns the frozen code/pilot_stream_drat_ms0{6,9}_v4.py (fe9ccadb…, 9a688cce…), code/pilot_file_drat_v32.py
(f5b7b37e…) and their shared `owner_identities_of_attempt`, `disposition_refusals` and `release_refusals`. The governing
review freeze is RUN/review/pa19-v4-v32-source-review-freeze-v2.json (806a1967…). I will fold these items in after the
findings arrive, together with whatever Codex reports.

## 1. Zombie counted as "ended" (flagged by the parent): a real gap

`disposition_refusals` treats `bsd_identity(pid)` returning ESRCH as "ended", and treats a readable SZOMB identity as
ended too. The old lane supervisor recorded that on this macOS, `proc_pidinfo(PROC_PIDTBSDINFO)` returns 0 with ESRCH
for an unreaped zombie, while `proc_listpids(PROC_PGRP_ONLY)` still lists it (OLD/src/supervise_pa19_v6.py docstring,
lines 11–19). So ESRCH cannot tell a zombie apart from a process that has gone. Because the rule has to be "all
processes ended", a zombie should not release anything.

Proposed rule:
- A listed (pid, start) counts as ended iff the pid is absent from `proc_listpids(PROC_ALL_PIDS)`, or it is present
  with a readable identity whose start differs (the pid was reused).
- An unreadable present pid, or a zombie, refuses.

## 2. Coverage of the disposition: a real gap

`owner_identities_of_attempt` returns only the UNSETTLED owners' leader identities. Two sets of processes are not
required to appear in the parent's identities, and the runner does not re-check them:
- the group members and PPID-closure descendants recorded in each owner's `live_census`;
- any process that joined the owner's group after the census.

Proposed rule:
- (a) The required identities = leaders plus every census group member and descendant (pid, start).
- (b) The runner also requires `proc_listpids(PROC_PGRP_ONLY, owner pgid)` to be empty for every owner. Since
  pgid == leader pid, an empty group means no member is left, zombies included.

For summary-less attempts, (b) applies to every child launch record's pid.

## 3. Late-artifact obligations are not part of the disposition: a completeness gap

The UNSETTLED receipt names late obligations: the cwd may gain entries, the proof FIFO may stay held, and a partial
proof file may exist. The release rule does not require the parent to have disposed of them, and it would not notice
a later change.

Proposed rule:
- The disposition carries `attempt_tree_census_sha256`: the SHA-256 of the canonical census of the attempt directory
  (the same `census_entry` tuples, sorted), taken after the parent confirmed that the processes ended.
- The runner recomputes this digest at admission. Any later change refuses until a new disposition is written.
- Lane usage already counts any late bytes.

## 4. Non-gaps checked

- No B1 path waits without bound. The loop audit is in review/p-stream-v4-v32-disposition-v1.json.
- An UNSETTLED attempt keeps its busy slot and reservation, because admission refuses until it is released.
- Helpers have no cwd. Their obligations are only the closure of the stdout pipe.

## 5. Planned delta (not frozen; after the findings)

The change would be confined to `owner_identities_of_attempt`, `disposition_refusals`, the disposition schema (adding
group pgids, the census identities and `attempt_tree_census_sha256`) and test v5's disposition scenarios. That last
part covers a zombie or live member in the owner's group, an uncovered census member and a tree changed after the
disposition. The functions are identical in P-STREAM and D2, so one shared change would apply to both.
