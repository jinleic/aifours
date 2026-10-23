**REJECT**

Static review only; I read the ten tests without executing them.

| Earlier finding | Status | Evidence |
|---|---|---|
| P1-1 cancellation/teardown | **PARTIAL** | Worker cancellation is latched and teardown shielded at [run_parallel.py:139](/Users/jinleic/repos/aifours/institute/run_parallel.py:139) and [168](/Users/jinleic/repos/aifours/institute/run_parallel.py:168). Supervisor cleanup still has the gaps below. |
| P1-2 hard ceiling | **PARTIAL** | Fork-relative deadlines and timed waits exist at [246](/Users/jinleic/repos/aifours/institute/run_parallel.py:246) and [260](/Users/jinleic/repos/aifours/institute/run_parallel.py:260), but surviving executors can escape that enforcement. |
| P1-3 liveness relocation | **FIXED** | Original and lane liveness are checked at [197](/Users/jinleic/repos/aifours/institute/run_parallel.py:197) and [213](/Users/jinleic/repos/aifours/institute/run_parallel.py:213), using PID/start identity through [178](/Users/jinleic/repos/aifours/institute/run_parallel.py:178). |
| P1-4 owner binding/resume | **FIXED** | The contract replaces targets with the owner statement at [95](/Users/jinleic/repos/aifours/institute/run_parallel.py:95); receipt and selection-contract checks precede resume at [219](/Users/jinleic/repos/aifours/institute/run_parallel.py:219). |
| P2-5 timeout receipts | **FIXED** | `timed-out` becomes `incomplete` at [159](/Users/jinleic/repos/aifours/institute/run_parallel.py:159), preventing batch success at [280](/Users/jinleic/repos/aifours/institute/run_parallel.py:280). |
| P2-6 input names | **FIXED** | Pattern and resolved direct-parent checks precede copying at [114](/Users/jinleic/repos/aifours/institute/run_parallel.py:114). |
| P2-7 source/render provenance | **PARTIAL** | PDF hashing and unidentified-cache refusal exist at [206](/Users/jinleic/repos/aifours/institute/run_parallel.py:206) and [224](/Users/jinleic/repos/aifours/institute/run_parallel.py:224), but frozen inventory hashes are not enforced. |
| P2-8 output location | **PARTIAL** | The resolved selection parent is constrained at [339](/Users/jinleic/repos/aifours/institute/run_parallel.py:339); durable descendant destinations are not. |

Remaining findings:

1. **P1 — Cancellation can interrupt forced cleanup after the lane has been killed.**  
   **Trigger:** During deadline enforcement, a lane requires escalation; SIGINT/SIGTERM/SIGHUP arrives after `process.kill()` but before its descendant sweep completes. The deadline path calls `stop_lane()` at [run_parallel.py:265](/Users/jinleic/repos/aifours/institute/run_parallel.py:265), before supervisor signal shielding at [293](/Users/jinleic/repos/aifours/institute/run_parallel.py:293). Inside [stop_lane:321](/Users/jinleic/repos/aifours/institute/run_parallel.py:321), killing/joining precedes the sweep.  
   **Impact:** Interruption discards the captured tree. Final cleanup sees an already-dead lane and skips it, allowing executors to survive lock release and their deadline.  
   **Minimal fix:** Block/defer cancellation throughout `stop_lane()` and guarantee the captured-tree sweep in `finally`.

2. **P1 — An unexpectedly dead lane receives no executor cleanup.**  
   **Trigger:** Only a lane is SIGKILLed or otherwise exits abruptly while its executor remains alive; the supervisor survives. The unexpected-exit branch at [run_parallel.py:274](/Users/jinleic/repos/aifours/institute/run_parallel.py:274) stops the batch, but [stop_lane:317](/Users/jinleic/repos/aifours/institute/run_parallel.py:317) performs no sweep when that lane is already dead.  
   **Impact:** Its reparented executors survive outside the lock. Their watchdog died with the lane, so the supervisor’s six-hour limit no longer bounds them.  
   **Minimal fix:** Retain executor PID/start identities and descendant groups in the supervisor, and sweep them on every lane exit, including already-dead lanes.

3. **P2 — PDF verification trusts an inventory that is no longer pinned.**  
   **Trigger:** Inventory regeneration changes a selected article’s PDF path/hash or page range after selection freezes. The manifest pins inventory hashes at [selection.json:15](/Users/jinleic/repos/aifours/institute/runs/hard-2026-10-15/selection.json:15), but [validate:200](/Users/jinleic/repos/aifours/institute/run_parallel.py:200) loads the current inventory and compares the PDF against that inventory’s current hash. `input_sha256` is never checked.  
   **Impact:** Changed source evidence can be accepted and attributed to the frozen selection.  
   **Minimal fix:** Verify the frozen inventory hashes before using inventory metadata; enforce the other declared input pins as well.

4. **P2 — A symlink beneath an authorized run redirects durable writes outside the repository.**  
   **Trigger:** For example, `run/problems/math-p0039` is a symlink to an external directory. The parent-only check at [run_parallel.py:339](/Users/jinleic/repos/aifours/institute/run_parallel.py:339) passes, while receipt creation at [149](/Users/jinleic/repos/aifours/institute/run_parallel.py:149) and engine record writes through [ri.py:657](/Users/jinleic/jinleic-workspace/research-institute/explorer/ri.py:657) follow that destination.  
   **Impact:** Receipts, records, source extraction, and attack artifacts can be written outside the authorized repository.  
   **Minimal fix:** Reject escaping symlink components in durable destinations and verify their resolved containment before writing.

These supervision gaps remain actionable while the supervisor is alive. They are distinct from pre-existing engine risks such as its [Popen-to-try window](/Users/jinleic/jinleic-workspace/research-institute/explorer/ri.py:227) or SIGKILL of every lock-holding process.