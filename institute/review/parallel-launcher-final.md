**REJECT**

Two concrete defects remain:

1. **P1 — A killed worker can still leave replay processes alive.** Replay commands bypass executor PID publication: [ri.py:999](/Users/jinleic/jinleic-workspace/research-institute/explorer/ri.py:999) calls `sandboxed()`, whose [run_bounded invocation](/Users/jinleic/jinleic-workspace/research-institute/explorer/ri.py:1199) supplies no `on_start`. If replay starts and its worker is SIGKILLed between supervisor samples, the subprocess becomes reparented without entering the retained tree. [remember_executors()](/Users/jinleic/repos/aifours/institute/run_parallel.py:68) then has neither published liveness nor a living worker tree to discover it. Cleanup can release the lock while that replay continues without its watchdog.

   Publish replay PID/start identities through the same durable mechanism as model executors. This differs from the excluded Popen-before-on_start window: replay never registers an identity.

2. **P2 — Blocking deadline cleanup delays supervision and can misclassify completed siblings.** The supervisor captures `ready`, then performs blocking teardown for each lane before examining the next. [run_parallel.py:304](/Users/jinleic/repos/aifours/institute/run_parallel.py:304) A sibling that finishes during that teardown remains absent from the stale `ready` result, so it can be marked expired and have its successful report overwritten. A stubborn first lane can also consume the reserved grace before the other lanes receive termination; the subsequent tree sweep has no deadline bound. [run_parallel.py:372](/Users/jinleic/repos/aifours/institute/run_parallel.py:372)

   Check current exit state before classifying expiration, initiate termination for all expiring lanes before blocking joins, and include sweeps within their deadlines.

The four previous findings resolve as follows:

| Finding | Status | Code evidence |
|---|---|---|
| Cancellation interrupts forced cleanup | **FIXED** | [stop_lane:365](/Users/jinleic/repos/aifours/institute/run_parallel.py:365) blocks signals through termination, escalation, and the finally-protected sweep. |
| Already-dead worker leaves executors | **PARTIAL** | Published model executors are retained and swept even after worker death; unpublished replay processes remain exposed as described above. |
| Frozen inventory/input pins ignored | **FIXED** | [check_inputs:82](/Users/jinleic/repos/aifours/institute/run_parallel.py:82) verifies every declared pin and runs before inventory loading. |
| Durable writes escape through symlinks | **FIXED for the reported case** | The scan checks escaping symlinks and known destinations; [validate:251](/Users/jinleic/repos/aifours/institute/run_parallel.py:251) separately confines dossiers. Rendering and run-summary writes require successful admission. |

The parent checker now uses sandboxed replay, refuses `status="running"`, and fails incomplete batches. No additional concrete checker defect found.

Excluded residual limitations: the engine’s pre-existing Popen-before-on_start window and uncatchable SIGKILL of every lock holder.

Static review only; no tests or application code were executed, and no files were changed.