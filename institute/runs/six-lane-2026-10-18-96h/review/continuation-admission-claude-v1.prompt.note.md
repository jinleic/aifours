**RESULT: GO-WITHIN-INITIAL-SCOPE**

Written research can start now. Initial-scope probes should wait until finding 1 is recorded and finding 2 is sent to workers. Both are cheap and touch old state read-only.

Issue no native, checker-replay, compilation or expensive-enumeration GO under v1 as written. First freeze findings 5–9 as a tightening-only v2, cited by SHA-256 in every GO and acknowledged by each worker, so no rule is frozen after the work it governs.

Inherited STOP markers cannot be ignored under this contract (`old_stops`, info-1 frontier). Finding 7 only makes that enforceable.

No FATAL items.

**Needed now (before probes run or any status is recorded)**

1. **MAJOR — `preservation`; `previous_*_sha256`; `lanes[*]` (no baseline field); worker brief "pinned lane closeout"**
   - **Why:** "Remain unchanged" cannot be verified.
     - Only the old contract and report are pinned. The closeouts workers must build on are never named or hashed.
     - Git can't serve as baseline. `commit` is false, and the session's git status snapshot already shows old-round records (`packing-array19/STATUS.json`, `six-lane-2026-10-16/transitions.json`) modified relative to HEAD.
     - The owner's cleanup scope is unrecorded, so artifacts the pinned report relies on may be gone.
     - Nothing checks for prior-round processes that outlived the disk-exhaustion stop.
   - **Fix:** The parent exclusive-creates the following in the run dir, then re-verifies the manifest at close:
     - (a) A manifest of the previous run dir and every `six-lane-20261016` evidence tree. Use SHA-256 for regular files and lstat-only (type, mode, size, inode, mtime) for FIFOs, sockets and symlinks. Never open a FIFO: the open blocks, and timeouts are banned.
     - (b) Each lane's closeout path and SHA-256, checked against any hashes in the pinned report. Anything missing or mismatched is "inherited-unavailable" and not load-bearing.
     - (c) A read-only `ps` census matched to prior-round launch records by start time and argv. Report any survivor to the owner, count it against resources, and don't signal it, because this round doesn't own it.

2. **MINOR — `resources.initial_go` with `resources.stop`; worker brief "no … tool timeouts"**
   - **Why:** "≤300 s" has no enforcement mechanism.
     - Claude Code's Bash tool ends foreground commands at 120 s by default. A 300 s foreground probe is therefore stopped by the very automatic tool timeout the contract bans.
     - Nothing limits whose code may run.
     - Nothing bars opening non-regular files in old trees. A recursive grep/cat can block on an old FIFO, or connect to a surviving writer.
   - **Fix:**
     - "≤300 s" means an in-probe wall-clock self-budget with clean exit. Set the call limit above it (max 600 s), or run the probe detached under a launch record.
     - Probes are worker-authored and hash-frozen; third-party or downloaded code is data until a GO.
     - Keep cwd and all writes inside the lane path, and read old trees regular-file-only.
     - Allow no hard links and no symlinks to old inodes in writable dirs; a `"w"` open through one truncates old evidence.

3. **MAJOR — `lanes[*].frontier` (phys-1 "GA16/18, GB1/18"; info-1 decided cases) vs worker brief "never duplicate accepted computation"**
   - **Why:** Inherited closures may rest on the prior round's named defects: weak transport checks, output written during disk exhaustion, or a status later found false. "Never duplicate" discourages rechecking them, and phys-1's "final composition" would inherit any error.
   - **Fix:** Each lane's initial inventory classifies every inherited closure by evidence path.
     - Closures depending on a proof stream, the exhaustion window, or a corrected status are "inherited-unqualified".
     - They are not load-bearing in any composition until re-qualified under a GO.
     - Re-qualification is not duplication.

4. **MAJOR — `completion`, `breakthrough_gate`, `cutoffs.report_due` (no terminal-status rule; last round published a false PASS)**
   - **Fix:** Freeze a status vocabulary and reporting rules now.
     - Each target or sub-obligation is one of: VERIFIED (every gate item recorded), CANDIDATE-UNVERIFIED, SCOPED-PARTIAL (exact scope stated), OPEN, UNKNOWN.
     - Sub-obligation closures (K5.3, GA/GB items) need the same evidence and parent verification as the final claim.
     - Run status describes execution only, never scientific success. It cannot be PASS/COMPLETE while any process is unsettled, the manifest has drifted, or final-report review is incomplete.
     - Status lives only in versioned files; an exclusive-created `README.md` is an index, not a status.
     - Add a report-freeze time (e.g. 22:26:33) so review finishes before `report_due`. Ideally set `report_due` a few minutes before `deadline_at_pt`, since the anchor is the first observation *after* authorization.
     - Any candidate that hasn't cleared the gate by then is reported as CANDIDATE.
     - The report lists every launch-registry entry with its final state, plus the manifest re-check.

**Needed in v2 before the first native GO** (each also adds a field to the GO request template)

5. **MAJOR — `cutoffs` vs `resources.max_chunk_seconds` / `resources.stop`**
   - **Why:** A chunk launched at the 20:56:33 launch stop with a 10800 s self-budget ends at 23:56:33. That is 2 h after `owned_compute_settled_by` and 1 h after the deadline. The "bounded wait" has no value, "settled" is undefined, and the worker brief repeats only the launch stop and deadline.
   - **Fix:**
     - Each chunk's self-budget is an absolute wall-clock end ≤ `owned_compute_settled_by` − W − margin, with W frozen (e.g. 300 s). An elapsed-time budget can overrun after system sleep.
     - Don't admit jobs that can't fit.
     - The parent SIGTERMs registered survivors at the settlement time minus W.
     - "Settled" means: exit status reaped, descendants gone, outputs closed with size and SHA-256, final checkpoint written.
     - Anything else is UNSETTLED in the report, blocks launches (state whether per lane or globally), and is reported to the owner. SIGKILL only on owner instruction.

6. **MAJOR — `process_identity`; `preservation` ("Parent owns shared run control"); `orchestration` ("in-session")**
   - **Why:** File ownership is defined; process ownership is not. A worker or subagent can end (return, crash, context loss) while its detached job runs. There is no watchdog, and "owned SIGTERM" doesn't say whether the parent may signal a worker's job.
   - **Fix:**
     - At launch, each job's record is exclusive-created in a parent-readable registry with owner, budget end, output paths and byte budget.
     - The parent may signal any registered process.
     - Ownership passes to the parent automatically when the launcher ends.
     - No one signals unregistered processes.

7. **MAJOR — `old_stops` (last round ignored its STOP registry)**
   - **Why:**
     - The deadline/disk vs. correctness split treats disk stops as benign, but disk exhaustion can silently truncate logs, proofs and status files.
     - Nothing says who may supersede a marker, or that each GO must consult the registry.
     - New-round STOPs and worker "safety issue" notices have no defined effect.
   - **Fix:** The parent keeps one registry of old and new STOPs, keyed by path and SHA-256.
     - Every GO cites the registry version and the disposition of each relevant entry.
     - Only the parent supersedes a STOP, via a versioned GO. Markers are never edited.
     - Artifacts from disk-stopped runs are UNKNOWN until shown complete.
     - A correctness or safety defect needs evidence of resolution, not just a GO.
     - Any safety notice opens a STOP on the affected item.

8. **MAJOR — `resources.free_floor_bytes`, `per_lane_new_disk_bytes`, `launch_rule`, `lanes[*].rss_bytes`**
   - **Why:** The floor and caps are checked only at launch. With no watchdog and only in-session polling, an output stream that outgrows its estimate is caught late. Swap and CLI/session logs share the same volume. The last round ended in disk exhaustion.
   - **Fix:**
     - Each job writes through a byte-capped writer set at its frozen estimate; overflow means clean exit and UNKNOWN.
     - The parent maintains `fresh free − Σ remaining live byte budgets ≥ free_floor_bytes`, checked at every launch and at a stated poll interval.
     - On violation: block launches, SIGTERM registered jobs largest-growth first, and notify the owner.
     - Define `rss_bytes` as a lane total including descendants.

9. **MAJOR — `evidence`; phys-1 frontier "measured proof feeds" (transport checks were a named failure)**
   - **Fix:** For every proof stream:
     - Producer-side and consumer-side byte count and SHA-256 must match.
     - Every pipeline stage's exit status or signal is recorded; any failure means UNKNOWN.
     - The checker verdict is bound to the formula SHA, proof SHA and size, checker binary SHA, and argv.
     - Positive and mutation controls run on the same checker binary.
     - If the proof is streamed rather than stored, the GO states what independent parent verification will rerun.

10. **MINOR — `orchestration` / `completion` ("exactly two active slots"; replacement targets)**
    - **Why:** "Exactly two active" conflicts with "scientifically justified", and a slot awaiting a GO isn't active. Target replacement has no approver.
    - **Fix:**
      - Allow at most two slots, with BLOCKED/IDLE plus a recorded reason permitted.
      - A replacement needs parent approval and written evidence of exhaustion or prior work.
      - The original target's outcome is reported as-is; results on the replacement never count as progress on it.

Reviewer: Claude Opus 5.5 (`claude-opus-5-5`). No tools were used. I reviewed only the embedded text and the session's git status snapshot; I did not verify any path, hash, process or literature status.
