**GO — BLOCKER: none; MAJOR: none; MINOR: none in the admission delta.**

- **No active-process or reused-PID bypass found.** Both snapshots must match the pinned child’s PID/PPID/PGID/UID/start and show `Z`; the parent must satisfy identity, start, app-path, consistency and cwd checks. Unresolved live processes reach the refusal branch before the exception. SOURCE00:558–568, 625–632.
- **No reservation or slot concealment found.** The exclusion does not filter live lane accounting, supervisor reservations or slot ancestry. Unknown slots still block admission; the final census remains under the admission lock. SOURCE00:649–678, 699–712, 758–764, 958–997.
- **Excluded `None` argv cannot reach the regex.** `pid not in excluded` short-circuits before `B411_R7.search`. Other unresolved entries return for retry first; helper failures and malformed enumeration retain refusal behavior. SOURCE00:586–592, 641–643, 679–680, 719–739.
- **The remaining launcher delta is scoped correctly.** Direct comparison against SOURCE03 confirms only exception handling/reporting, selftest additions and version/help text changes.
- **Assembler acceptance is unchanged.** PASS still requires every condition. Report prefixes now use `K.SCRIPTS`; interruption/disarm additions preserve UNKNOWN/NOT_STARTED history and add evidence references without changing acceptance. SOURCE01:279–309, 167–178, 426–427, 511, 642–649.
- **Evidence agrees.** The supplied selftest records both exclusions and passing mismatch checks, bound to the reviewed script hashes. SOURCE06:348–470, 599–610, 617, 627.

All **seven SHA-256 hashes and byte counts match**. Review used snapshot-only static reads, comparison and hashes; no interpreters, tests, signals, writes, network or delegation.