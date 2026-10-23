**DISPOSITION: HOLD.** Repairs remain necessary before the controls run.

All six supplied SHA256 hashes and byte counts match. Review used only static reads and hashes inside the snapshot; no interpreter, writes, network, or delegation.

The nine prior findings resolve as follows:

| Prior finding | Decision | Exact v4 evidence |
|---|---|---|
| **1 — checker failure credited as rejection** | **Fixed for the pinned checker contract.** Requires normal rejection rc `1`, exact `s NOT VERIFIED`, no VERIFIED, correct header, complete transport, and `N == D`. | `SOURCE00:1334–1342`, `1247`. Pinned checker rejection/timeout exits agree at `SOURCE04:905`, `1481–1500`. |
| **2 — incomplete early-close drain credited** | **Fixed.** EOF is recorded only after an empty read. Qualification requires EPIPE, zero delivery, actual EOF, finished relay, both event releases, clean drain/closes, and the exact header-error outcome. | `SOURCE00:913–948`, `1353–1360`. |
| **3 — close errors did not veto PASS** | **Fixed for feed and relay ownership.** Both feeds must finish without write/close errors; relay close errors veto acceptance. | `SOURCE00:1201–1206`, `1259–1276`, `1297–1302`. |
| **4 — pending SIGTERM lost to launch/completion** | **Partly fixed.** Gate and pre-spawn checks were added; completion can still produce PASS with a latched SIGTERM. | Checks: `SOURCE00:505–508`, `1041–1068`. Remaining defect: `1090–1092`, `1287–1288`, `1664–1688`. |
| **5 — scanner defeated safety bounds** | **Partly fixed.** Helpers have deadlines, and scanning moved off the watchdog. Failed-helper classification, exceptional cleanup, and terminal races remain defective. | `SOURCE00:309–357`, `422–447`, `1111–1144`; defects below. |
| **6 — exceptional setup abandoned ownership** | **Partly fixed.** The wider cleanup scope exists, but descriptor transfers remain unsafe and a spawned solver can escape the process registry. | Scope: `SOURCE00:1033–1197`. Remaining defects: `1056–1059`, `1072–1076`. |
| **7 — controls/admission/assembly unenforced** | **Core checks added; launch-time enforcement remains incomplete.** Five controls, script/binary pins, receipt hashes, and existing-control validation are checked. Assembly checks script/pre-exec bindings and rejects repeated labels. Validation nevertheless precedes a potentially hours-long gate. | `SOURCE00:1377–1408`, `1493–1500`, `1597–1623`, `1784–1809`; timing gap at `1639–1656`. |
| **8 — obsolete leaf dependency lookup** | **Fixed by removing those item kinds.** | `SOURCE00:820–842`, `1436–1492`. |
| **9 — unreachable ANOMALY_PASS** | **Fixed by removal.** Missing observations become INVALID_CONTROL. | `SOURCE00:1331–1367`. |

Remaining and newly exposed defects:

- **MAJOR — blocking the controls run: descriptor and child ownership still have exception gaps.** At **SOURCE00:1056–1059** and **1076**, descriptors are popped before `_start_relay()`/`_start_writer()` completes. A constructor/start failure leaves them outside both the worker registry and final descriptor cleanup. Separately, **SOURCE00:1072** closes `scr` before **1074** registers the successfully spawned solver. If that close raises, `term_live()` and `reap()` know only about the checker; the outer fallback cannot recover the solver handle.

  **Repair:** register worker ownership before startup and use an explicit handoff that closes each descriptor exactly once after a failed start. Register the solver immediately after successful `Popen`, before any close or other fallible operation. The normal successful path has no identified double-close; adding unconditional supervisor closes would introduce one.

- **MAJOR — blocking the controls run: helper cleanup is not exception-safe.** At **SOURCE00:318–322**, helper setup occurs after spawning but before the cleanup `try`. Failures in `set_blocking`, selector creation, or registration abandon the helper and its stdout ownership. Exceptions inside selector/read processing reach the `finally` but bypass **344–353**, the only SIGTERM/reap path. A helper surviving the five-second termination wait is also returned without retaining/reporting its PID; the Scanner can start another scan.

  **Repair:** establish one ownership scope immediately after successful helper spawn. On exceptional exit, SIGTERM the live helper, perform bounded reaping, and close resources independently. Retain/report any surviving PID and latch a desk-stopping failure; halt further helper/native launches. Preserve the prohibition on escalation.

- **MAJOR — blocking the controls run: failed helpers can become healthy empty measurements.** **SOURCE00:386–400** ignores both later helpers’ `_rc` values. A helper that crashes before its deadline returns a nonzero rc with `err=None`; that is accepted. Missing cwd/argv records then remove candidates at **413**, potentially returning `([], None)` and understating lane occupancy. Tolerating disappearing PIDs does not justify accepting arbitrary exit failures.

  **Repair:** validate every helper return code and coverage of surviving candidates. Allow disappearance only when established; treat unresolved live candidates as a failed measurement or count them conservatively.

- **MAJOR — blocking the controls run: completion bypasses latched stop and scanner failures.** **SOURCE00:1090–1092** still breaks before inspecting SIGTERM or the Scanner. A signal or failed scan can arrive while children are live, followed by both children exiting before the next watchdog tick. Finalization records scanner statistics at **1200**, but neither those failures nor `alive_after_join` participate in **1287–1288**. Evaluation runs before the driver handles its latch at **1686**. Thus a receipt can contain **PASS plus `stop_latched: SIGTERM`**; a missed scanner failure can also permit another item.

  **Repair:** latch scanner failures independently of `latest`; inspect stop/failure state before the completion break and again before evaluation. Make a pipeline-time latched SIGTERM, scanner failure, or unfinished cleanup veto success and further launches. Recording the latch while preserving PASS does not close prior finding 4.

- **MAJOR — blocking the controls run for binary identity; blocking formulas for admission freshness: validation occurs before the long gate.** Control receipts are revalidated at **SOURCE00:1613–1623**, binaries/script at **1639–1641**, then `gate()` may wait against the six-hour budget before **1656** launches. There is no post-gate identity check. A replaced binary can therefore execute under the previously recorded hash; changed or removed qualifying evidence can escape formula admission revalidation.

  **Repair:** after gate success, recheck script and executable identities and, for formulas, the complete qualifying control identities against `admission_controls`, immediately before launch. Record those final checks.

One additional operational gap belongs to finding 6: **SOURCE00:1049–1050 and 1070–1071** catch spawn failures without setting a desk-stop reason. Formula evaluation becomes UNKNOWN, but **1689–1706** does not stop on spawn-error fields, so another formula can launch. **This repair blocks formulas:** route spawn failures through the operational-failure cleanup and stop policy.

The suffix implementation matches its stated preregistration. **SOURCE00:175** defines the five binary bytes `64 02 04 06 00`; **931–934** appends them only after observed FIFO EOF. **1348–1352** requires clean completed transport, five appended bytes, `D = R + 5`, and checker `N == D`, then returns `AS_PREREGISTERED_FAIL_CLOSED`. The pinned parser counts marker/literal bytes at **SOURCE04:986–988 and 1107–1115** and continues parsing past an empty clause through the ordinary loop at **1226–1235**.

The substantive formula PASS conjunction remains at **SOURCE00:1289–1310**:

- Solver rc `20` and exactly `["s UNSATISFIABLE"]`.
- Checker rc `0`, an exact `s VERIFIED` line, and no NOT VERIFIED/TIMEOUT.
- Both complete, measured CNF feeds matching their bound lengths and hashes.
- Positive relay read count equal to delivery, equal SHA256, actual FIFO EOF, finished threads, and no feed/relay/close errors.
- Present checker count `N == D`.
- No **recorded** safety stop, exception, spawn error, or exceeded termination grace.

The missing stop propagation above prevents an unconditional confirmation of the safety requirement.

I found no explicit path that copies CNF/proof streams into regular files: feeds use anonymous pipes, proof output uses the FIFO and relay, and read-side proof provenance remains recorded at **SOURCE00:1212–1213**. No executable use of SIGKILL, `Popen.kill`, or subprocess timeout APIs appears. Explicit termination sites use SIGTERM at **346** and **1024**, with bounded native reaping; the ownership gaps prevent that cleanup guarantee from covering every spawned child.