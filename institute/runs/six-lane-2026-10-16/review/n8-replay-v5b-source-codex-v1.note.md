**Native CONTROLS: GO-WITH-FIXES.** Findings F1 and F2 below are blocking repairs. The frozen v5b hash is not cleared for launch.

**SCIENTIFIC FORMULAS/LEAVES: HOLD.** Resolve F1/F2 and obtain the five actual native control receipts for the resulting reviewed script identity. Direct-leaf launches additionally require F3.

All nine supplied SHA256 hashes and byte counts match. SOURCE01’s 57 unified-diff hunks exactly match SOURCE02 → SOURCE00. Review used only static read, diff, and hash utilities within the snapshot. No reviewed code, tests, native jobs, network, writes, or delegation were used.

Three **MAJOR** findings remain. These are static failure paths, not reproduced failures.

1. **F1 — A: descriptors leave the registry before worker initialization is protected.**  
   At **SOURCE00:1092–1099**, `_writer()` takes its descriptor, then initializes the hash before entering `try/finally`. At **SOURCE00:1142–1167**, `_relay()` takes both descriptors before constructing hashes, state, and its delivery function.

   If initialization raises—for example, `MemoryError` constructing a hash—the worker exits without reaching its closing `finally`. The supervisor’s cleanup at **SOURCE00:1483–1488** sees only descriptors still registered, so it cannot close these claimed descriptors. Thus the stated “every FD closed exactly once” exception guarantee remains incomplete.

   **Repair:** prepare worker state before claiming descriptors, then protect the claim and every subsequent operation with closing `finally` blocks. Retain thread handles before starting them so interrupted startup can also be joined or reported.

   The original ordinary `Thread.start()` failure gap is repaired, and solver registration now precedes the fallible close at **SOURCE00:1344–1353**. The remaining defect concerns initialization after ownership transfer.

2. **F2 — B: helper ownership still has a post-spawn exception window.**  
   `Popen()` succeeds at **SOURCE00:400–401**, but the ownership handler begins at **405**. The intervening `chunks, err, sel, fatal = [], ...` at **404** allocates after spawn, outside that handler.

   An allocation failure or interruption there bypasses `_stop_helper()` and the explicit stdout cleanup. No `HELPER_SURVIVORS` entry is created for that path. The normal selector/setup exceptions are now covered, but the literal immediate-ownership requirement is not fully met.

   **Repair:** initialize bookkeeping before spawning and put spawn, supervision, and cleanup under one enclosing ownership scope. Once a helper exists, every exit must perform bounded SIGTERM-only cleanup and retain/report any unreaped PID.

   SOURCE04 tests selector failure and interruption *inside* supervision (**68–100**); it does not cover this remaining window.

3. **F3 — H: the 12-leaf restriction is enforced by `preexec`, not by `run`.**  
   The allowlist check exists at **SOURCE00:1807–1809**. However, `cmd_run()` reads a supplied PRE-EXEC and checks script/interpreter identities without repeating that restriction (**1946–1958**).

   `item_parts()` accepts any ID in the 16-case `ctx["cases"]` dictionary (**1054–1057**). The later leaf check binds bytes to RESULT and MANIFEST, but still does not check `DIRECT_LEAVES` (**2036–2045**).

   Consequently, a supplied or altered PRE-EXEC containing `leaf:P1-B1` with its correct bound fields can pass these checks and launch, despite that ID being excluded from direct leaves. Hashing the supplied PRE-EXEC records its identity; it does not establish that `cmd_preexec()` generated it. Assembly also lacks this allowlist check (**2233–2237**, **2256–2261**).

   **Repair:** apply a shared item validator when consuming PRE-EXECs, before regeneration or launch, and during assembly. Explicitly reject leaf IDs outside `DIRECT_LEAVES`. SOURCE04’s H2 checks the set partition, not rejection through `run` (**664–666**).

The prescribed-fix disposition is:

| Item | Static disposition |
|---|---|
| **A** | **Partial.** Locked descriptor handoff and child registration fix the reported ordinary startup/close ordering defects. F1 prevents full exception-safety approval. |
| **B** | **Partial.** Supervised failures receive SIGTERM and bounded reaping; survivors are recorded and inhibit helpers, gates, and native work. F2 remains. See **SOURCE00:366–450**, **700–704**, **1226–1235**, **2120–2124**. |
| **C** | **Fixed.** Both `ps` return codes are checked; `lsof` accepts only 0/1. Missing cwd/argv coverage for a candidate fails unless libproc establishes ESRCH. See **SOURCE00:459–514**. |
| **D** | **Fixed for the prescribed pipeline-time vetoes.** Scanner failures persist independently of `latest`; completion checks the latch; post-join state and the pre-evaluation check veto PASS and further work. See **SOURCE00:539–571**, **1370–1378**, **1498–1505**, **1610–1619**, **2081–2085**, **2120–2124**. |
| **E** | **Fixed.** After gate success, script, interpreter hash/realpath, and native binaries are rechecked. Scientific admission revalidates qualifying receipt hashes and their referenced PRE-EXEC hashes; mismatches refuse before `pipeline()`. See **SOURCE00:1692–1724**, **1910–1943**, **2065–2074**. |
| **F** | **Fixed.** Either native spawn error sets a stop reason; an owned checker receives bounded cleanup after solver-spawn failure; the driver stops on spawn-error fields. See **SOURCE00:1326–1328**, **1348–1363**, **1451–1479**, **2116–2119**. |
| **G** | **Implemented as requested.** See details below. |
| **H** | **Binding and proof predicate correct; launch restriction incomplete under F3.** |

G checks timezone-aware, strictly increasing sample timestamps; last age `0 <= age <= 30`; at least 25 samples spanning at least 290 seconds within the 300-second window; last free space at least `13.5e9 + 10 MiB`; and the ordered peak-to-later drop against `max(300000000, (free_last - 13500000000)//12)` (**SOURCE00:609–669**). Ordering plus nonnegative last age excludes future samples from a passing result. Missing/unreadable monitors and malformed complete records refuse; only the trailing unterminated fragment is ignored.

Both formulas and leaves request this gate, and a passing streak receives another monitor read and fresh `statvfs` (**SOURCE00:710–724**, **2054**).

The scientific PASS conjunction remains intact for both formulas and leaves at **SOURCE00:1558–1624**:

- Measured, complete, error-free CNF feeds match the bound lengths and hashes.
- Solver rc `20` and status list exactly `["s UNSATISFIABLE"]`.
- Checker rc `0`, an exact `s VERIFIED` line, and no NOT VERIFIED/TIMEOUT marker.
- Status parsing removes CR only (**1221–1223**, **1525–1546**).
- Positive proof read count equals delivery count, with equal SHA256; actual FIFO EOF; clean, finished relay; and checker `N == D`.
- Clean settlement and the added stop/scanner/thread/survivor vetoes.

Leaf regeneration binds both the fully pinned parent RESULT and MANIFEST (**SOURCE00:757–759**, **862–887**). I found no explicit driver path persisting CNF or proof streams into regular files: the feeds use anonymous pipes and proof transport uses the FIFO/relay.

The five controls retain their intended meanings:

| Control | Required observation |
|---|---|
| `unsat` | Full scientific predicate → `PASS`. |
| `sat-checker` | Complete equal transport, `N == D`, checker rc `1` and exact NOT VERIFIED → preregistered rejection. |
| `truncate` | Clean EOF with exactly two withheld bytes and differing streams → fail closed regardless of native verdict. |
| `early-close` | Both event releases, exact header-error outcome, zero delivery/EPIPE, and complete clean FIFO drain → fail closed. |
| `suffix` | Five suffix bytes delivered after EOF, `D = R + 5`, checker `N == D` → transport equality fails closed. |

These predicates are at **SOURCE00:1645–1682**. The pinned checker’s byte-count increments and EOF paths support the consumption check (**SOURCE06:983–994**, **1104–1125**, **1265–1267**); parsing continues beyond an empty clause (**1226–1235**).

For the previous review, findings **1, 2, 3, 8, and 9 remain resolved**. Finding **4** is resolved by D. Finding **5** remains partial through F2, while its exit-code, coverage, and scanner-latch defects are repaired. Finding **6** remains partial through F1; solver registration and spawn-stop propagation are repaired. Finding **7’s long-gate identity gap is repaired**. F3 is a new H admission defect, separate from the obsolete dependency lookup.

Mandatory runtime evidence remains:

- A newly frozen, reviewed identity after repairs, with actual interpreter and native executable identities matching its PRE-EXEC and post-gate checks.
- **Five real native control receipts**, including logs, measured feeds, relay counts/digests, checker counts, child reaping, and clean settlement. SOURCE05’s reported 89/89 covers Python plumbing/stubs and regeneration checks; it supplies no native proof verification.
- For each scientific launch, qualifying control identities, the passing monitor window and final free-space check, lane/RSS gates, and the existing launch/deadline limits.
- For each scientific PASS, the complete conjunction above, with no pipeline-time SIGTERM, failed scanner, unfinished cleanup, or helper survivor.
- Old receipts must retain `PROOF_DIGEST_MISSING`; fresh results cannot retrofit discarded proof digests. The separate second-encoding obligation remains open (**SOURCE07:7–11**).