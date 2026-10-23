**DISPOSITION: GO for running the frozen v7 controls.** No remaining BLOCKER, MAJOR, or MINOR findings in the requested repair scope; no repairs required.

All 11 files match the supplied SHA-256 hashes and byte counts.

- **Thread bootstrap:** `SOURCE02:147–176` replaces only `N.threading` with a scoped proxy. Global threading primitives remain intact. The stop wrapper uses pre-captured `get_ident()`; thread bootstrap retains ordinary internal events.
- **Deterministic race:** `SOURCE02:108–116,178–185,216–225` holds solver exit until pipeline return and feeder publication until join entry. Production enters that settlement after recording the bounded exit (`SOURCE06:335–358`). Deadline expiry fails the handshake rather than establishing the expected result.
- **Discriminating mutant:** `SOURCE02:196–206` removes exactly one settlement loop. Assertions require the normal case’s real write-error provenance, clean supervision and persistent integrity flag; the mutant must produce `UNKNOWN/NOT_EVALUATED` with the exact cap reason (`SOURCE02:275–295,895–913`). These checks prevent vacuous success.
- **Waits and reasons:** subprocess completion uses monotonic polling followed by parameterless `wait()` (`SOURCE02:218–224`). Both exceptional fields are compared exactly against the injected `RuntimeError` representation (`SOURCE02:266–269`).
- **Boundaries:** the supplied active sources contain no subprocess timeout, SIGKILL, deletion, or automatic native retry. SOURCE01 accounts for the harness changes.

The supplied production modules match their pinned hashes. Unchanged contract identities are declared in `SOURCE04:10–20`; their raw bytes are absent, so independent contract comparison remains unverified within this snapshot.

**Controls remain NOT_RUN.** Review used only static reads and hashes inside the authorized snapshot.