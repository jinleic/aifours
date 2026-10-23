# PA19 REV11a final re-review (reviewer task PA19StagedAudit, delivered 2026-10-17 ~16:22 PDT)

Parent transcription of the reviewer's delivered result (agent output; transcript `history://PA19StagedAudit`). Read-only; no execution, process polling, live-log inspection or file modification by the reviewer.

## REV11a outcome: REJECT — one ownership-safety blocker remains

Overall correctness: incorrect. Confidence 0.95. The four requested fixes are present, and no certification regression was found. However, the watchdog's "proven current token owner" test is not sufficient to guarantee that SIGTERM targets an owned process.

### Remaining finding

**MAJOR / P1 — Revalidate lock ownership and process identity before signalling.** `rss_watchdog3.py:92–98` reads token metadata and accepts a PID because `lsof -t` shows that PID has the file open; this does not establish that it holds the exclusive flock. `trip()` then selects that numeric PID using the earlier process-group snapshot and signals it at lines 132–142, after potentially several additional `lsof` calls. The holder can release/exit during this interval; PID reuse can consequently direct SIGTERM to a non-owned replacement. Open-but-not-locked descriptors during acquisition also do not constitute ownership proof. Keep admissions paused and skip signalling unless ownership and runner identity are re-established through a suitably synchronized owner check or cooperative per-runner stop mechanism. Confidence 0.96; source-level race, not an observed event.

### Four-fix disposition

| Blocker | Assessment |
|---|---|
| Pause before watchdog grace wait | Fixed. `pause_admissions()` writes COUNT0 and creates STOP files before ownership lookup or signalling (`rss_watchdog3.py:109–130`). The watchdog never resumes admissions. |
| Unsafe largest-group fallback | Removed. Runner discovery requires the exact absolute lane script argument; no eligible owner means no signal. The ownership-proof race above remains. |
| Admission after `bigmem` wait | Fixed. `stream_check12.py:431–440` rechecks after acquiring the lock and returns uncertified without starting drat-trim when refused. |
| SAT-verifier ownership | Fixed for the inspected production helpers. `run_hard12.py:85–115` preserves raw output and the decoded array, then runs both verifiers under a token through `run_helper`; refusal/abort marks verification deferred. |

### Regression and consumer checks

- The `stream_check11`→`stream_check12` diff contains only the documented admission check, revision identifier and explanatory header; all rev-11 survivor, replay, EOF, tail-cap and verdict fixes remain.
- `summarize10.py:52–55` and `list_pending3.py:23–25` accept revision 12 with the full predicate; no dispatch drop or weakening found.
- Production extension helpers and the inspected Python/C verifier sources introduce no subprocess descendants.

### Receipt interpretation and residuals

- Smoke attempt 16:02:57 is 6/7 (not a pass); attempt 16:04:54 is 7/7. The controls do not test stale metadata, lock-versus-open ownership, PID reuse or ownership changing during slow lookup.
- Missing `lsof`: uncaught exception, but COUNT0 and STOP files are already established; cannot reopen admissions. Slow `lsof`: admissions remain paused, monitoring delayed.
- RSS sampling and cooperative termination do not provide an instantaneous 8-GiB bound. No actual production CPU/RSS excursion or false mathematical UNSAT was demonstrated.

## Parent disposition (2026-10-17)

GO withheld. Required REV11b: a new watchdog file that never signals any process (pause admissions, write an alert, stop; recovery is a parent decision), with a signal-free smoke control. Parent will read the watchdog diff and the smoke receipt before issuing GO with COUNT = 2.

Time note (appended 2026-10-17 16:22:34 PDT, host clock): the '~' delivery time in the title is an estimate from the surrounding tool receipts, not a host-clock reading; the host-clock save time is this note's time or earlier.

Parent GO addendum (2026-10-17 16:25:49 PDT, host clock): REV11b replaces the signalling watchdog with src/rss_watchdog4.py (sha256 b178c185ceba2f20e9b61abf51eeb81746e170659225dd7b3f1044ee24875b28), which never signals any process; the parent read the full watchdog3→4 diff (cycle2/diff-rss_watchdog3-to-4.diff, sha256 dfafe4c445937a5758fdecfb3dc660cd30de3810ca5546655e134e2d02992ed7) and the source header/imports. Smoke attempt 2 (cycle2/smoke-rev12b-20261017T162424.json, sha256 d271618fd02dbf3c39ddb865e352d7b8c187af8c994e3b12eb54d8a9ab518def) passed S0–S2; attempt 1 (substring static check false positive) is retained as failed. GO issued with COUNT = 2; the ownership MAJOR is resolved by removing signalling, at the cost that an RSS trip only pauses admissions (running stages end at their native limits).
