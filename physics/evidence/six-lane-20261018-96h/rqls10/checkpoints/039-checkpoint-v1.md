# Checkpoint039 — source17 raw-first repairs at safe boundary

Actual `/bin/date` before write: 2026-10-19T12:30:14-0700. Interval from038 is15m38s, within the20minute target/30minute maximum. No earlier deviation is erased.

Source17 remains NEW/UNFROZEN and unaccepted. Current AST-only draft SHA `2e89c538436e950eef651480122a7c39f68d0d2d12966be7f84394a1c5b0f9a1` (2665lines). No import/execution/test occurred; the static AST contains one centralized `os.waitpid(record['pid'], os.WNOHANG)` call.

Written repairs now cover all five authorized source16 findings:
1. Main-role PID/record assignment precedes auxiliary registration time. Both spawn-call and outer known-PID exception paths adopt the actual registered record, acquire/install checked identity/group, handle endpoints, request the existing safe stop and enter bounded observation; merely moving a timestamp is not treated as enough.
2. Bounded raw identity captures preserve native returns before optional end clocks. Pure cleanup-state installers run before end timing/history. Missing timing is null with sticky evidence failure; mandatory deadline/fingerprint checks remain required and TERM is not widened.
3. Native task results and verified final identity/RSS composites survive timing failures; known RSS excess is latched before end timing, missing BUSY timing is not invented, and incomplete returned observations cannot be erased by a retry. Stream native read/EOF/write counters and prefix bookkeeping precede clocks; raw closure flags and pending/hash-prefix states distinguish missing evidence.
4. Returned fstatvfs data, completed accounting values and the actual minimum witness are retained before completion clocks/checks; unsuccessful caller b/end stay null.
5. One destructive reap routine latches native wait result/reaped state/rc before nullable timestamps. Consumed terminal statuses cannot become re-waits or restore signal eligibility.

This is written implementation plus a syntax-only observation, NOT an independent correctness verdict. Next work is the exact17diff/disposition/nullable telemetry interface and parent source review. Any author-found or reviewer finding must preserve frozen evidence and use only parent-authorized versioning. Source17 is not yet frozen or source-ready.

Packagev9 child12/writer12/checker11 and fullmatrix drafts remain UNFROZEN/unadmitted. Coherent consumer repairs, original22, all fullv13/v14 matrix bodies/admissions/actual outcomes and the independent parent's five-part release implementation remain open prerequisites. Held scientific source/NumPy remain unchanged/unrun. Scientific target OPEN/UNKNOWN; no GO/science/settlement claim.

Next active target12:50:14; binding maximum13:00:14.
