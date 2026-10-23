# Review resolution — 2026-10-15

## Scientific selection

| Reviewer | Verdict | Disposition |
|---|---|---|
| Claude Opus 5.5 max, read-only safe mode ([raw](selection-review.json)) | ACCEPT with minimum changes | Accepted. Every requirement is frozen as `review_requirements` in `runs/hard-2026-10-15/selection.json`, and the stronger catalog claims were narrowed. |
| Codex gpt-6.1-sol max, read-only ([review](selection-codex-review.md)) | ACCEPT with minimum changes | Accepted. Schedules now fit the four-hour attack; confidence labels, success definitions, and non-vacuous negative-result standards are frozen. |

## Parallel launcher

| Round | Verdict | Resolution |
|---|---|---|
| [Initial](parallel-launcher-codex-review.md) | REJECT: 4 P1, 4 P2 | Fixed cancellation latching, hard ceilings, liveness checks, owner-target binding, timed-out receipts, unsafe input names, PDF hashes and output location. |
| [Re-review](parallel-launcher-codex-rereview.md) | REJECT: 2 P1, 2 P2 | Fixed protected forced cleanup, retained executor identities after worker death, frozen inventory pins and escaping durable symlinks. |
| [Final](parallel-launcher-final.md) | REJECT: 1 P1, 1 P2 | Fixed replay PID publication and current-state deadline classification; all due lanes are signaled before blocking cleanup. |
| [Release](parallel-launcher-release.md) | REJECT: 1 P2 | Fixed after review: every lane now shares one ceiling, so lanes cannot become due one by one during another lane's cleanup. A real-process regression stops three SIGTERM-ignoring lanes at the shared ceiling. This final edit was tested but not re-reviewed before launch. |

The first Claude launcher review timed out after 1,800 seconds and produced no verdict.

Accepted residual limitation: the external engine has a short window between `Popen` and its watchdog
registration, and SIGKILL of every lock holder cannot be handled by any user-space supervisor.
These limitations existed before this launcher.
