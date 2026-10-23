# Source18 narrow interface delta — REVIEW ONLY

Actual `/bin/date` before write: 2026-10-19T12:53:02-0700.
Source `code/owned_supervisor_v18.py`: `e73cbd786c609ee1b3c82ebeec75fa4335f75619b5a817e0833ccfa02c9d2ff0`.
Exact17→18diff `review/owned_supervisor_v17_to_v18.diff`: `e1fbbc7862a8163644684a5fbe454117055da0da5d58bdf6b6f30b97a36a8111`.

The binding scope is RUN `review/rqls10-supervisor-v17-HOLD-source18-scope-parent-v1.json`, `0f9aff3ce810d04301f869d0f925e1473bdd2dedebf4f1bba382dfacd9d5cd33`. Full source17 review `339ed81c35700f7a52f703ba223a49f6ecc3dcf60cd1172b4a938b578f47230a` was read. Only its two MAJOR repairs are changed; v17 is immutable. No runtime or independent acceptance is claimed.

## M1: sticky cancellation-clock failure

The cancellation handler still latches the real signal first and retains honest mono=null/clock_error on a failed clock. If a supervisor is active, the handler immediately sets its sticky timing_failed flag; it does not make reentrant failure-list mutations. After initialization and before protected commits, outcome selection and the special handled-cancellation ACK branch, propagate_cancel_clock_error also retains the TIMING_EVIDENCE_UNAVAILABLE failure row. A clock error recorded before supervisor creation is propagated when initialization finishes.

Thus missing cancellation timing cannot be normalized into handled-cancel SETTLED/exit0. No timestamp is manufactured. Only the pre-existing bounded cleanup and original deadline/full-fingerprint TERM eligibility remain. No cancellation input, wire or authority is broadened.

## M2: recovery native wait retains runtime enforcement

Known-main recovery now calls the existing main `reap()` wrapper rather than directly calling `reap_record(main=True)`. Its before/after-native-wait checks can retain DEADLINE and MAIN_DEADLINE_ENFORCEMENT_LATE even when the wait succeeds after crossing the wall bound. The underlying single WNOHANG routine still stores destructive native status/reaped state/rc before nullable clocks. Clock-unavailable cleanup remains incomplete/HOLD, not invented runtime evidence.

## Unchanged

There are no new wire/config/healthy telemetry formats or accepted statuses. V17 acquisition-first raw/null/event/accounting/stream/closure evidence, typed binding, ordinary GO-newline+EOF, mutation-only line/original inode, owned bounded `/bin/date`, conservative coverage,4MiB cap, grace/TERM rights, exclusive publications and narrow actual14 terminal behavior remain. All original22 expected outcomes and fullv13/v14 matrix requirements remain unexecuted and unchanged. Packagev9/matrix final pins stay paused until an independent source-ready verdict; no preparation, runtime, release or scientific authority follows. Parent five-part release implementation remains a separate prerequisite.
