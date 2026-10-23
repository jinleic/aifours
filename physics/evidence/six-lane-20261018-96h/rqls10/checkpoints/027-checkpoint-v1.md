# Checkpoint 027 (rqls10 continuation, successor worker)

Recorded 2026-10-19T07:52:27-0700 (from /bin/date). Owner ContinueRQLS10b. Target OPEN / UNKNOWN; no candidate. No
process of this worker running; nothing executed since 05:07 except parse-only static checks and read-only inspections.
Parent HOLD on launches in force; no science, no controls, no Q1.

## Events since 026
- Codex review of supervisor v9: HOLD, 2 FATAL + 7 MAJOR
  (RUN/review/rqls10-owned-supervisor-v9-source-codex-v1.prompt.stdout.txt fa0061cd...82f6).
- Binding parent decision RUN/review/rqls10-supervisor-v10-scope-parent-decision-v1.json e441d858...b22: single-process
  reviewed children; any owned process other than the child is a latched contract violation that blocks release until
  verified ended; unlinked same-uid processes not blocking (fork+setsid residual documented); NO /bin/date helper and NO
  human-readable timestamps in the supervisor (raw labelled telemetry only; the parent writes /bin/date timestamps);
  GO carries raw not_after_epoch + stability receipt digest; commit-point freshness, exact publication budgeting,
  anchored lane root, deadline checks on every completion path, uniqueid+idversion+ruid/euid brackets.
- Read-only facts gathered for v10 (disclosed as D-19 in the next deviations record):
  - xnu kern_exec.c (downloaded to lane tmp/, 0444, sha256 89531d33...932d1a, lines 7096-7104): every exec assigns a
    new p_idversion, guaranteed different from the previous one (rdar://129775819); so (uniqueid, idversion) brackets
    detect exec. PROC_PIDPATHINFO has no same-user check (proc_info.c); libproc proc_pidpath returns strlen or 0.
  - read-only /bin/ps uid census: 4 "login" processes with ruid 501 / euid 0 (their cwd, argv and task information are
    not readable by an unprivileged supervisor) and loginwindow with ruid 0 / euid 501; 636 processes with euid 501.
- Supervisor v10 being authored under the decision; qualification package to be re-bound to v10 as new file versions
  (the cited v5 drafts will be frozen as they stand, per the new-version rule).
