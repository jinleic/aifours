VERDICT: HOLD

| Prior finding | Disposition | File:line evidence |
|---|---|---|
| **NEW1 — registration handshake** | **REPAIRED** | Run entry validates `MOQLS8_LAUNCH_RECORD` placement. `registration_problem()` requires nonempty regular-file JSON naming this driver’s PID and exactly `ABS_CHILD_END`. Both native spawns pass `boundary()` immediately beforehand. `snapshot/00-gb_staged_v6e.py:3243–3248,3115–3129,2538–2540,2607–2618,2673–2684`; launcher supplies the reserved pathname at `snapshot/10-launch_gb_v6e.py:155–166`. |
| **NEW2 — unrounded terminal veto** | **REPAIRED** | `_child_record()` retains `wall_seconds_raw`; terminal enforcement compares that field directly with the applicable stage backstop. Missing raw telemetry defaults to infinity. `snapshot/00-gb_staged_v6e.py:2280–2289,2767–2775`. |
| **NEW3 — settlement/status survival** | **PARTIAL** | Primary writing, separately reserved fallback writing and announcement have independent handlers. Cached child status survives these handlers. A failed **launch** announcement records an error without SIGTERMing the published driver. However, interpreter shutdown can still override the selected launcher status; fallback reporting is also incomplete. `snapshot/10-launch_gb_v6e.py:157–166,216–226,233–248,259–288`. |

1. **NEW — MINOR: caught stdout failures can still replace the required launcher exit status.**

   The launcher catches announcement failures and reaches `return 4`, but ultimately exits through `raise SystemExit(main())`. With ordinary buffered stdout connected to a broken pipe, failed flushing can leave buffered output pending. CPython shutdown retries flushing; another failure can change the process status to **120**, overriding the selected **4**.

   Thus the prior broken-pipe counterexample is repaired inside `main()`, but unconditional preservation of the launcher’s final process status remains **NOT ESTABLISHED**. The settlement’s cached driver status survives.

   Guard terminal flushing and finish through a status-preserving terminal path. The driver already uses guarded flushing followed by `os._exit()`. Evidence: `snapshot/10-launch_gb_v6e.py:222–226,271–288`; `snapshot/00-gb_staged_v6e.py:797–810`.

2. **NEW — MINOR: successful fallback settlement is announced using the failed primary pathname.**

   If primary settlement writing raises and fallback writing succeeds, the fallback digest is discarded. The subsequent announcement still names `settle`, with `sett_sha == None`. The launch record likewise advertises only the primary settlement pathname.

   The fallback bytes exist, but neither published registration nor announcement identifies the successful fallback artifact and its digest. Additionally, a settlement-announcement exception is appended to `errors` **after** serialization; no subsequent publication persists that diagnostic.

   Track and announce the successful settlement pathname/digest, and preserve late announcement diagnostics through a separate guarded reporting path. Evidence: `snapshot/10-launch_gb_v6e.py:208–210,260–274`.

Verified:

- **All 18 manifest-listed files match their SHA256 pins.** Inspection used static reads, comparisons and hashing exclusively within `snapshot/`; no interpreter, solver, checker, writes or delegation.

- Independent source comparison and a matching SHA256 over eight selected unchanged regions reconfirm unchanged **ACCEPTANCE, CRITERIA, evaluate/control evaluation, seven control definitions, regeneration/binding, measured writers, collector/feeder, qualification, publication/terminal exit and helper supervision**. Release validation changes its directory reference. Representative regions: `snapshot/00-gb_staged_v6e.py:356–506,621–956,1002–1092,1485–1650,1831–1985,2815–3031`.

- The seven controls retain their exact outcome, diagnostic and observation restrictions: **unsat → PASS**, **sat-checker → AS_PREREGISTERED_NOT_VERIFIED**, and the other five → **AS_PREREGISTERED_FAIL_CLOSED**. `snapshot/00-gb_staged_v6e.py:401–469,2912–3024`.

- Remaining gbs5 changes match the listed version/path/provenance, eleven-direct-input scope, admission/resource/observer, retained-log, deadline/chunk, terminal-veto and registration changes. No additional acceptance relaxation appeared in the independent diff. `snapshot/01-DIFF-gb_staged_v5-to-v6e.txt:9–704`.

- No new route to a qualifying scientific receipt without complete measured refutation of the exact bound GB bytes was identified. Regeneration must match the binding and both expected CNF feeds; collector/buffer/feeder lengths and digests must agree; checker-consumed count must equal delivery; clean checker success and pipeline settlement remain mandatory. `snapshot/00-gb_staged_v6e.py:1566–1591,2831–2909`.

- Science admission still requires all seven controls for this script identity. Qualification additionally requires bound commit/completion records, cancellation absence, a clean producing-run summary and external parent release attesting **strict integer exit zero**. `snapshot/00-gb_staged_v6e.py:865–956,1743–1790`.

- **No operative October 18 deadline remains.** Active deadlines use October 22. In-flight enforcement and terminal late-reap veto remain; grace exhaustion records surviving children and prevents further launches. No additional unreported-survivor path was identified within the stated review limits. Runtime realization is **NOT ESTABLISHED** by this static review. `snapshot/00-gb_staged_v6e.py:293–300,2487–2502,2762–2790,3468–3470`; `snapshot/10-launch_gb_v6e.py:57–59`.