# Checkpoint040 — exact source18 candidate, NOEXEC

Actual `/bin/date` before write: 2026-10-19T12:53:02-0700. Interval from039 is22m48s:20minute target missed, binding30minute maximum not yet reached; persistence follows this reading. Earlier deviations stay recorded.

Parent source17 review `339ed81c35700f7a52f703ba223a49f6ecc3dcf60cd1172b4a938b578f47230a` returned HOLD0F/2M; full82lines read. Parent decision RUN `review/rqls10-supervisor-v17-HOLD-source18-scope-parent-v1.json` authorizes ONE minimal18 repairing exactly sticky cancellation-clock failure and recovery runtime-check bypass. Source17 remains unchanged; obligations1/3/4/5 were statically fixed, timing obligation2 partial.

Source18 now frozen0444, `code/owned_supervisor_v18.py`, SHA `e73cbd786c609ee1b3c82ebeec75fa4335f75619b5a817e0833ccfa02c9d2ff0`. Exact17→18diff `review/owned_supervisor_v17_to_v18.diff`, `e1fbbc7862a8163644684a5fbe454117055da0da5d58bdf6b6f30b97a36a8111`.

Written changes only: cancellation's clock error immediately sets sticky timing failure on the active supervisor; failure-row propagation is deferred out of the signal handler and checked before initialization completion, commits/outcome/handled-cancelACK. Honest signal/nullmono remain; no reentrant failure-list mutation or widened TERM. Main recovery's native reap goes through existing `reap()` pre/post runtime checks; destructive native status latching remains before clocks, and clock-unavailable cleanup remains HOLD. No other behavior or accepted statuses changed.

AST-only parse and exact hashes, no source import/execution/test. Disposition/interface delta and independent source18 review are next; no readiness or GO claimed. Packagev9 child12/writer12/checker11 and fullmatrix drafts remain UNFROZEN/unadmitted pending a stable source-ready verdict. All eight consumer obligations, original22, fullmatrix actual outcomes, heldassay EOF/backend work, and real parent five-part release implementation remain required. Scientific target OPEN/UNKNOWN; no NumPy/control/fixture/numerical/Q1 run.

Next active target13:13:02; binding maximum13:23:02.
