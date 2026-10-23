# Supervisor v19 interface delta — NOEXEC

Recorded after actual `/bin/date`: 2026-10-19T13:04:23-0700.

- Source: `code/owned_supervisor_v19.py`, SHA-256 `cb828a78367dc2023bfc6e330696745f186f186811752361472747e5fe547e93`.
- Exact v18→v19 diff: `review/owned_supervisor_v18_to_v19.diff`, SHA-256 `31b5b49d2c796b26d7d7b8313d3b29341982bac691a04b4bc97efa169e0c4c06`.
- Binding authorization: RUN `review/rqls10-supervisor-v18-HOLD-source19-scope-parent-v1.json`, SHA-256 `af46437e487de9d57e346450e8d9be82664df448af96ef4c645a0c5e3d2e2f1b`.

The healthy telemetry/schema and all caps, signal/reap rights, original grace, ordinary exact GO-plus-EOF and mutation-only creation channel remain unchanged from v18. This is not package/runtime admission.

The existing `Supervisor.reap()` wrapper now contains the post-wait `enforce_runtime("after_waitpid_including_success")` exception. Its first action on that exception is the sticky `timing_failed=True`; only afterward does it record existing failure code `MAIN_RUNTIME_CLOCK_UNAVAILABLE`, with detail `["after_waitpid_including_success", actual_exception_type]`, through the existing failure/stop mechanism. No catch fabricates the failed clock value, repeats the consumed native wait, calls TERM directly, retries observation, or extends grace. The already recorded native wait tuple/status/reaped state/rc are untouched. Missing timing remains incomplete/HOLD, not a weaker accepted status.

Source review must decide adequacy; no empirical execution has occurred. Package v9 remains UNFROZEN pending parent disposition and must still implement all eight consumer obligations. The original22 and complete separately mapped finite matrix remain required and unexercised. Parent five-part release, held assay EOF/backend obligations, and `fabe57ab` remain unchanged prerequisites.
