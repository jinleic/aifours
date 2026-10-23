**RESULT: QUALIFIED**

**Scope.** This qualifies the terminal and publication contract of `checker_v2.py` (SHA `5b285da4…a3f2cf`) on this host (Homebrew CPython on Darwin), for a single-threaded checker process. The consumer rule must be applied after the process has exited:
- the process exited normally with status 0;
- the recorded `exit_code` is 0;
- `overall` is COMPLETE_VALID;
- no `<out>.CANCELLED.json` exists.

It makes no Sun7 claim and leaves F-1/EXPLORATORY unchanged. The Sun7 theorem still needs the second checker. I took v1↔v2 math equivalence and v1 math soundness from the prior audits and did not re-verify them.

**FATAL:** none. **MAJOR:** none.

**MINOR-1: the terminal downgrade only changes the overall result.**
- `_finish` rewrites `overall` and `exit_code` but never `universes[U].status`, and the stdout summary repeats those unchanged statuses.
- So a C1–C3-type file (rc 3, recorded `exit_code` 3, no marker) meets the in-file contract's conditions. It still reads `universes.<U>.status: COMPLETE_VALID` for a run the terminal decision ruled UNKNOWN. Only `overall` and `terminal` record the downgrade.
- The intended disposition is about one universe (X1). So X1 may be cited only from a record that meets the full parent rule. positive-v2 does. Never take X1's status from a file whose rc is not 0.
- No code change is needed for this qualification.

**MINOR-2: the positive-v2 replay is not tied to the frozen bytes in the evidence shown.**
- The controls went through the harness `--checker-sha` check. The frozen positive command runs `checker_v2.py` by path with no hash check.
- It also ran under `six-lane-2026-10-18-96h/review/sun7-stageA-v2-qualification-v1/`, not the frozen planned working directory.
- The `terminal` and `publication_contract` keys, and equality with v1 apart from timing, make a substituted file implausible. They still do not bind the executed bytes to the frozen hash.
- Before `positive-v2/result.json` (`b49afa28…`) is used in any disposition:
  - record the sha256 of the `checker_v2.py` that was actually executed;
  - declare the relocated command lines as a deviation.
- This does not affect the terminal qualification itself, which rests on the hash-checked controls.

**The controls do discriminate.**
- **v1 vs v2.** v1 wrongly accepts C1–C5 (5 of 5). v2 rejects all five by the predicted mechanisms:
  - C1–C3: UNKNOWN at decision time, no marker.
  - C4–C5: marker written by the late check.
- **H0** is accepted under both versions, so the consumer rule is not rejecting everything.
- **C4/C5 end in rc 3, not 143.** This shows four things happened in order:
  - the SIGTERM made pending before the SIG_DFL reset survived the reset;
  - the final `sigpending` saw it;
  - `sigwait` consumed it;
  - all of this happened before the unblock.
  If any step had failed, the process would have exited 0 or been killed (143).
- **C6 ends in rc 143.** This shows SIG_DFL was in effect at the unblock. If the Python handler had still been installed, the pending SIGTERM would have run inside the unblock and `_finish` would have returned 0.
- **C7** is a real test for the same reason: without the second resource sample it would have ended in rc 0.
- **C8** tests robustness, not the fix. v1 also rejects it, via rc 1.
- **Coverage.** For a single-threaded process the coverage is complete:
  - Changes to the signal mask and disposition are system calls, so behaviour is the same throughout each interval between them.
  - Self-signals sent at fixed hook points are deterministic, so one run per interval is enough.
  - Signal intervals:
    - before the block: C2;
    - blocked, before the decision read: C3;
    - between the decision read and the final read: C4, C5;
    - after the final read: C6;
    - after the unblock: same SIG_DFL disposition as C6.
  - Resource intervals:
    - before the decision: C1;
    - after publication: C7.
  - A resource stop after the second sample comes after fsync and close, so it does not matter.
- **Optional check on C3.** C3's evidence is "no marker" plus where the hook sits. `terminal.sigterm_pending_at_decision` in the v2-C3 result will show which decision-time branch ran. Either branch is correct.

**The terminal contract is sound.**
- **rc 0 implies a clean finish.** Every path that sets `problem` also sets `final` to 3 or 5. So rc 0 means there was no late SIGTERM, no late stop and no publication error.
- **Failures outside the try blocks fail closed.** These are `guard.report`, `signal.signal`, the final `sigpending` and the unblock. Errors there propagate out of `_finish`. v1-C8's rc 1 shows the entry point does not swallow such exceptions.
- **The design does not depend on `pthread_sigmask` running already-tripped handlers.** Suppose a SIGTERM arrived just before the block and its handler did not run there. It would run at the next point where the interpreter checks for signals. That is either the `guard.sample` or `_sigterm_pending` call, or inside `signal.signal()`, which checks for signals before changing the handler. The STOP recheck after the decision would then catch it.
- **"SIGTERM after the final check must not permit a normal 0" is met.** From the last `sigpending` onward the disposition is SIG_DFL. Delivery at or after the unblock runs no Python code, as C6 shows. The only SIGTERM that cannot count is one sent after the process has already entered kernel exit, which no design can observe.
- **rc 0 through `/usr/bin/time` is reliable.** It exits with the child's status on a normal exit and non-zero otherwise.

**Untested races: none are material.**
1. **Native threads.**
   - `pthread_sigmask` blocks a signal only in the calling thread. In a multi-threaded process, a SIGTERM sent to the process during the window would go to an unblocked thread and never show up in `sigpending`.
   - The handler, the STOP recheck and the reset-before-unblock would still catch it, except in one narrow case. That case is the other thread being preempted between the kernel delivering the signal and the handler flag being set, until the main thread has passed the final check.
   - A pure-Python checker should be single-threaded, but nothing in the evidence shows it.
   - Fix: log one thread count per run (`ps -M -p <pid>`), or add an assert in any v3.
2. **Signalling the wrapper.**
   - A SIGTERM sent only to the `/usr/bin/time` process kills the wrapper (rc 143, so rejected) but not Python.
   - Python can then finish writing an uncancelled COMPLETE_VALID/0 file. The rc still makes this fail closed.
   - The stop signal should target Python's pid or the process group, and a result file must never be read without its rc.
3. **Consumer timing.**
   - The absence of a marker means something only after the process has exited. A read between `outf.close()` and exit sees a COMPLETE_VALID/0 file that may still be cancelled.
   - Stdout is not a publication channel either: in C5 and C6 the success summary is printed first.
4. **Other signals.** Only SIGTERM is covered. SIGINT, for example, has no equivalent late guarantee. Runs meant to be accepted must use SIGTERM as their stop signal.

**Boundaries.** This qualifies publication semantics only:
- It does not lift F-1 and does not replace the second checker.
- It adds no mathematical bridge. The exit records show only that positive-v2's X1 COMPLETE_VALID was published under a sound terminal contract, subject to MINOR-2.
- K5.3 still comes only from the written X1⇒K5.3 implication, applied to an EXPLORATORY-class Stage A artifact.
- The disposition stays with the parent.
