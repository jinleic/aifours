**Native CONTROLS: GO-WITH-FIXES.** F1 and F4 remain incomplete; this frozen script is not cleared for launch.

**SCIENTIFIC FORMULAS/LEAVES: HOLD.** Resolve those findings and supply five real native control receipts for the resulting reviewed script hash.

All seven hashes and byte counts match. SOURCE01’s 33 hunks exactly match SOURCE02 → SOURCE00. Changes stay within F1–F4 plus naming/provenance. Review used only static reads, comparisons and hashes inside the snapshot.

1. **MAJOR — F1: descriptor ownership can still disappear during the claim.**  
   [SOURCE00:1117](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/n8-replay-v5c-delta-review-v1/snapshot/00-replay_v5c.py:1117) builds the return list by popping descriptors first. A `MemoryError` appending a popped descriptor leaves it absent from the registry before the caller receives it. Consequently, `fd` remains `None` at **SOURCE00:1127**, or `src/dst` remain `None` at **1201**; worker finalizers skip it, and supervisor cleanup at **1523–1525** cannot recover it.

   There is another remaining allocation before closure: `_relay()` constructs `close_errors = []` and its descriptor iteration tuple at **SOURCE00:1232–1233**, after claiming both descriptors. Allocation failure there bypasses both closes.

   **Required:** preallocate handoff and cleanup state before removing registry ownership; make partial transfers recoverable and close both descriptors independently before allocating diagnostics. These are static failure paths, not reproduced failures.

2. **MAJOR — F4: admission omits measured desk RSS.**  
   [SOURCE00:703](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/n8-replay-v5c-delta-review-v1/snapshot/00-replay_v5c.py:703) admits using `other + projected`, rather than the requested `other + max(measured_desk, projected)`.

   For example, other-lane RSS **10.25 GiB**, reservation **0.5 GiB**, and measured desk RSS **1 GiB** pass this calculation at **10.75 GiB**, although the required total is **11.25 GiB**. The correct in-flight calculation at **SOURCE00:1465–1476** acts after spawning.

   **Required:** include fresh measured desk RSS in admission, fail closed on an unreadable measurement, and cover measured RSS exceeding reservation. SOURCE04’s admission checks at **881–889** exercise reservation alone.

3. **BLOCKER — scientific native evidence remains unavailable in this snapshot.**  
   [SOURCE05:13](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/n8-replay-v5c-delta-review-v1/snapshot/05-UNITCHECK-v5c-r1.json:13) explicitly identifies stubs/fakes. Its reported **113/113** checks do not supply native control evidence. Scientific admission still requires all five qualifying receipts bound to the reviewed script, pinned binaries and referenced PRE-EXEC hashes (**SOURCE00:1789–1821, 1937–1940, 2030–2038**).

The other targeted repairs check out:

- **F1 startup portion fixed:** state/hash construction precedes claims; handles are registered before `start()` (**SOURCE00:1125, 1176–1201, 1369–1372, 1391–1392**). Interrupted startup retains the handle; unstarted threads are reported unfinished and veto PASS (**1532–1553, 1665–1666**).
- **F2 fixed:** bookkeeping precedes `Popen`; the enclosing ownership scope covers spawn through cleanup, retaining bounded SIGTERM-only reaping and survivor reporting (**SOURCE00:381–400, 412–470**).
- **F3 fixed:** `DIRECT_LEAVES` is enforced by the shared validator, called in preexec, run before logging/regeneration, and assemble before receipt consumption (**SOURCE00:1776–1781, 1933–1935, 2062–2067, 2340–2343**).
- **F4 remaining components correct:** both limits are 11 GiB; admission retains `busy + 2 <= 4`; in-flight accounting uses the required maximum; decision hashing is checked and recorded (**SOURCE00:174–181, 702, 1035–1044, 1465–1476, 1976, 2087**).

The **scientific PASS conjunction is unchanged**: the acceptance text and entire evaluator block are byte-identical to v5b (**SOURCE00:235–257, 1602–1731**). Measured feeds, exact native verdicts, FIFO EOF, positive equal proof streams and hashes, checker `N == D`, and settlement/stop vetoes remain conjunctive. All five controls—`unsat`, `sat-checker`, `truncate`, `early-close`, `suffix`—retain their inputs, observations and verdict predicates (**SOURCE00:197–216, 1694–1731**).