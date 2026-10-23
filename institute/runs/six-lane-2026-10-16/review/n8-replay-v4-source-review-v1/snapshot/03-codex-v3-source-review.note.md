**DISPOSITION: HOLD.** The normal relay path has sound descriptor ownership and byte accounting. Failure handling and control qualification need repairs before the control-only run.

All seven supplied SHA256 hashes and byte counts match. Review used only static reads, comparisons, and hashes inside the snapshot.

1. **MAJOR — before controls: checker failure can count as successful rejection.**  
   At [SOURCE00:1155](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/n8-replay-v3-source-review-v1/snapshot/00-replay_v3.py:1155), the invalid-proof control requires complete transport, then accepts any outcome lacking `s VERIFIED`. A checker that prints the parsing count and subsequently crashes or times out can return `AS_PREREGISTERED_NOT_VERIFIED`, with no reasons. The branch ignores checker return code, timeout, parsed-header validity, and the presence of an actual rejection status. This weakness is inherited from SOURCE02:1007–1014.

   **Repair:** preregister a normal proof-rejection exit code and exact rejection status, require the expected parsed header, and reject timeouts, signal deaths, and unrelated parser errors as `INVALID_CONTROL`.

2. **MAJOR — before controls: the early-close control can credit an incomplete drain.**  
   At [SOURCE00:1133](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/n8-replay-v3-source-review-v1/snapshot/00-replay_v3.py:1133), success requires only an error string beginning with `EPIPE`. If a subsequent FIFO read fails, SOURCE00:815 appends that exception to the same string; it still begins with `EPIPE` and can satisfy the control. Moreover, `eof_at`/`eof_mono` are written in `finally`, including after read failures, and therefore do not establish EOF.

   **Repair:** separate delivery errors from drain errors. Set `fifo_eof_seen=True` and its timestamp only when `os.read()` returns `b""`. Credit early-close only for the expected EPIPE, successful drain to actual EOF, successful closes, both event waits released by their events, and a normal preregistered header-error exit from the checker. Crashes and additional relay errors must invalidate the control.

3. **MAJOR — before controls: recorded close errors do not veto PASS.**  
   [SOURCE00:817](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/n8-replay-v3-source-review-v1/snapshot/00-replay_v3.py:817) records `close_error_dst` and `close_error_src` without changing `ok` or `error`. `relay_complete_and_equal()` ignores those fields. CNF writers likewise record `close_error` at SOURCE00:761 while their acceptance checks ignore it.

   Consequently, complete equal streams plus a recorded close failure can still produce `PASS`, contrary to SOURCE03:40’s no-relay/feed-error requirement.

   **Repair:** make every close failure an explicit failed criterion; require both feed threads to have finished. Preserve single-owner closing rather than adding a second unconditional close from the supervisor.

4. **MAJOR — before controls: pending SIGTERM can lose to launch or successful completion.**  
   At [SOURCE00:401](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/n8-replay-v3-source-review-v1/snapshot/00-replay_v3.py:401), a passing gate returns `launch=True` before checking `stop["signal"]`. SIGTERM during the second passing scan can therefore authorize a launch.

   At SOURCE00:939, observing both children finished breaks before checking the signal. The receipt is evaluated and written at SOURCE00:1420–1429; the driver checks the signal afterward. A signal already received during the pipeline can therefore accompany a PASS receipt.

   **Repair:** prioritize the latched stop before gate success, check immediately before each spawn, and propagate a stop received during the pipeline into its receipt before evaluation. These ordering defects are inherited from v2.

5. **MAJOR — before controls: the supervisor does not provide the stated safety bounds.**  
   [SOURCE00:285](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/n8-replay-v3-source-review-v1/snapshot/00-replay_v3.py:285), 308, and 319 synchronously call `subprocess.run()` for scan helpers. In-flight supervision calls this scanner before checking SIGTERM, deadlines, or grace expiry. A hung helper suspends those checks indefinitely. A returned scan failure merely increments a counter and permits continued operation using stale RSS information.

   **Repair:** supervise helpers asynchronously with explicit monotonic deadlines; keep native-child stop checks independent of scan completion. Treat failed or stale guard measurements as a safety stop. Use explicit SIGTERM-only helper cleanup, avoiding subprocess timeout APIs and `subprocess.run()`’s exception-time kill cleanup.

6. **MAJOR — before controls: exceptional setup can abandon descriptors and native children.**  
   At [SOURCE00:901](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/n8-replay-v3-source-review-v1/snapshot/00-replay_v3.py:901), descriptors are popped before thread startup succeeds. If `Thread.start()` raises, those descriptors have no registered owner. Similar transfers occur for both feed writers. An exception after spawning children reaches a `finally` that closes only descriptors remaining in `fds`; it does not SIGTERM/reap the children, and subsequent joins and receipt construction are skipped.

   **Repair:** cover acquisition through finalization with one cleanup scope. Make descriptor transfer exception-safe. On operational exceptions, record UNKNOWN, SIGTERM owned live children, perform bounded reaping and thread cleanup, and prohibit further launches.

7. **MAJOR — before formulas: successful controls are not an enforced admission prerequisite.**  
   [SOURCE00:1192](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/n8-replay-v3-source-review-v1/snapshot/00-replay_v3.py:1192) accepts missing controls or formulas preceding controls. At SOURCE00:1368, an existing self-test receipt is skipped without checking its verdict. Only newly executed self-tests encounter the expected-verdict check.

   Assembly also selects receipts by label without validating their script/preexec binding against the requested evidence, and repeated preexec items can duplicate formula counts (SOURCE00:1535–1552).

   **Repair:** require all four qualifying control receipts, bound to the reviewed script and pinned binaries, before any formula launch. Validate existing receipts instead of silently skipping failed controls. Validate bindings during assembly and deduplicate formula identities. Freeze repaired code under fresh artifact names; preserve existing receipts.

8. **MINOR — before using legacy leaf controls: the v3 prefix breaks their dependency lookup.**  
   [SOURCE00:1374](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/n8-replay-v3-source-review-v1/snapshot/00-replay_v3.py:1374) still looks for `receipts/<id>.json`, while v3 leaf receipts are `receipts/v3-<id>.json`. A successful v3 leaf can be ignored, or an old unprefixed PASS can satisfy the dependency. SOURCE00:1275 advertises the same stale path.

   **Repair:** resolve dependencies through the same versioned label function and verify their provenance. This does not affect the four `selftest` controls.

9. **MINOR — diagnostic repair: `ANOMALY_PASS` is unreachable.**  
   At [SOURCE00:1138](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/n8-replay-v3-source-review-v1/snapshot/00-replay_v3.py:1138), the truncation observation requires `D=R−2`, while full acceptance requires `D=R`. Early-close requires an error, while full acceptance forbids one. Neither accepted observation can reach `ANOMALY_PASS`.

   **Repair:** remove the dead branch or implement a separate diagnostic for the intended anomaly. Native `s VERIFIED` on truncation is explicitly permitted by its preregistration; it does not constitute full pipeline PASS.

The normal descriptor lifecycle is correct:

| Descriptor | Ownership and closure |
|---|---|
| FIFO read end | Parent opens it, then transfers it to the relay; relay closes it. |
| FIFO keepalive writer | Parent retains it until solver reaping, solver spawn failure, or cleanup. |
| `cpr` / `cpw` | Checker receives `cpr` as stdin; parent closes its copy. Relay owns `cpw`. |
| `ccr` / `ccw` | Checker receives its CNF read end; its feed thread owns the writer. |
| `scr` / `scw` | Solver receives its CNF read end; its feed thread owns the writer. |

At SOURCE00:890–919, `pass_fds` contains only each child’s CNF read descriptor; default `close_fds=True` prevents inheritance of keepalive or pipe writers. The relay starts before the solver. I found no normal-path double-close or inherited writer preventing EOF.

Blocking proof delivery while drat-trim parses its CNF creates backpressure, without a circular dependency: the checker’s CNF writer runs independently. After EPIPE, delivery stops and FIFO reading continues. Solver exit plus keepalive closure permits EOF. Under ordinary Python startup, SIGPIPE is ignored in the parent, so this path raises `BrokenPipeError`; native children retain their own subprocess signal behavior.

Read-side hashing includes every returned FIFO byte. Delivered hashing follows each successful `os.write()` return, including partial writes. The two-byte tail correctly spans chunk boundaries and withholds `min(R,2)` bytes. Empty streams receive the empty SHA256 but fail the positive-length acceptance requirement. Normal EPIPE, truncation, missing parsing counts, and unequal counts cannot become formula PASS.

The joins have a **five-second bound per thread only after grace expiry**; otherwise they are unbounded. Three sequential joins can add fifteen seconds. Daemon status supplies process-exit abandonment, not graceful completion or proof provenance.

For the checker byte count, **SOURCE06:49 confirms the exact output format and reports `274062094` bytes**. SOURCE06:1 identifies stdin as the proof source despite the wording “proof file.” SOURCE05 records no independently measured proof-stream length, so these artifacts cannot establish that the checker counter equals raw delivered bytes.

If drat-trim stops after the empty clause, successful pipe writes can still include an unread buffered suffix. An exact consumed-byte counter would make `N < D` and fail closed; a read-ahead counter would not establish that every delivered byte was parsed. **Before formulas, establish this counter’s semantics from the pinned checker reader source and a preregistered valid-prefix-plus-suffix control. Keep the equality requirement pending that evidence.** The recorded checker/relay timestamps compare reap observation with relay finalization, not actual exit with actual EOF.

Block hashes confirm that limits, gates, formula composition, and in-flight monitoring code remain unchanged from v2; inherited defects above remain present. Native solver/checker launch paths contain no explicit SIGKILL, `.kill()`, or subprocess timeout. CNFs and proofs traverse memory, pipes, and the FIFO; no regular CNF/proof copy is introduced. Exclusive creation and versioned item labels prevent direct receipt overwriting. Driver logs and run summaries lack the claimed universal `v3-` prefix, but also use exclusive creation.

**Required sequence:** repair findings 1–6, freeze fresh source/artifact identities, then perform the control-only run. Keep formulas held until all four controls qualify, finding 7 is addressed, and the checker byte-counter contract is established. SOURCE05 remains historical evidence with missing proof-digest provenance under SOURCE04.