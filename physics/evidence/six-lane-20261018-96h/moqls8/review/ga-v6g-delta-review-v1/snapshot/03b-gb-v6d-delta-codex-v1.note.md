VERDICT: HOLD

| Finding from snapshot/03 | Disposition | File:line evidence |
|---|---|---|
| NEW1 — every unpublished-launch failure → owned SIGTERM, wait, settlement, exit 4 | **PARTIAL** | Console closure, record construction, writing and announcement now share the failure handler; it attempts one SIGTERM without polling, then waits. However, settlement I/O can escape before the promised exit 4. `snapshot/10-launch_gb_v6d.py:173–225,249–260`; NEW finding 3 below. |
| NEW2 — terminal stage-backstop/native-cutoff veto | **PARTIAL** | The `>= NATIVE_STOP_AT` veto is present. Stage-backstop comparison is present but uses rounded elapsed time, leaving a narrow acceptance window. `snapshot/00-gb_staged_v6d.py:2280,2757–2765`; NEW finding 2. |
| NEW3 — single reap owner | **REPAIRED** | Registration cleanup reads `returncode` without reaping; `child.wait()` owns the reap, and settlement uses its cached return code. `snapshot/10-launch_gb_v6d.py:214–223,235–238`. |
| NEW4 — protected terminal handoff | **REPAIRED** | After waiting, SIGINT/SIGTERM/SIGHUP are blocked before settlement serialization and the final status decision. Mask failure records an error and selects failure. `snapshot/10-launch_gb_v6d.py:223–233,258–261`. |

1. **NEW — MAJOR: native admission does not depend on published registration.**

   The launcher spawns the independently running driver before filling the reserved launch record. Nothing passed to the driver acknowledges successful publication. The driver’s admission and spawn predicates check GO, identities, resources, signals and deadlines, but never registration completion.

   Counterexample schedule: suspend only the launcher immediately after spawning, while leaving the driver runnable. Given otherwise passing admission, the driver can complete its two-pass gate and spawn kissat while `LAUNCH-*.json` remains empty. No exception or blocking regular-file write is needed. The expanded exception handler therefore repairs failure coverage without establishing “no native execution before registration.”

   Require a publication acknowledgement that the driver must receive before any native spawn; an elapsed admission delay is insufficient. `snapshot/10-launch_gb_v6d.py:153–160,169–174,210–215`; `snapshot/00-gb_staged_v6d.py:1350–1424,2521–2546,2597–2608,3330–3351`.

2. **NEW — MINOR: rounded telemetry weakens the stage-backstop veto.**

   `_child_record()` rounds stage elapsed time to three decimal places. A measured duration of **300.0004 seconds** becomes **300.000**, so the terminal `> 300` comparison does not veto it. `supervise()` returns immediately on a successful reap, allowing this completion to bypass its unrounded in-flight comparison as well. The absolute and total-driver deadlines can still be comfortably in the future.

   Compare unrounded reap/spawn timestamps for enforcement; reserve rounding for presentation. `snapshot/00-gb_staged_v6d.py:2280–2282,2425–2434,2764–2765`.

3. **NEW — MINOR: settlement output exceptions bypass the required launcher status.**

   The inherited launcher tail protects descriptor closure with `finally`, but does not catch exceptions from settlement writing or announcement. For example, a broken stdout pipe makes the launch announcement raise; registration cleanup sends SIGTERM and waits, but the settlement announcement then raises on the same pipe. Execution never reaches `return 4`. In this example the settlement JSON is written before the second print fails.

   Separately, a settlement write/fsync exception leaves no successfully published settlement, with no fallback reporting path in this block. Catch settlement-writing and announcement failures independently and preserve the explicit failure-status path. `snapshot/10-launch_gb_v6d.py:211–225,249–265`.

Verified:

- **All 17 manifest-listed files match their SHA256 pins.** Review used static reads, comparisons and hashing only, entirely within `snapshot/`; no source execution, writes or delegation.
- Independent source diffs and eight matching region-hash pairs reconfirm unchanged **ACCEPTANCE, CRITERIA, evaluate/control evaluation, seven control definitions, regeneration/binding, measured writers, collector/feeder, qualification, publication/terminal exit and helper supervision**. Release validation changes its directory reference. Relevant v6d regions: `snapshot/00-gb_staged_v6d.py:344–499,614–951,995–1087,1478–1645,1788–1980,2805–3024`.
- Control outcomes remain **unsat → PASS**, **sat-checker → AS_PREREGISTERED_NOT_VERIFIED**, and the other five → **AS_PREREGISTERED_FAIL_CLOSED**, with their existing outcome, diagnostic and observation restrictions. `snapshot/00-gb_staged_v6d.py:394–462,2902–3014`.
- Remaining gbs5 deltas match the listed version/path/provenance, eleven-direct-input scope, admission/resource/observer, retained-log and deadline changes. No additional route around complete measured refutation was identified: both bound CNF feeds, collector/buffer/delivery equality, checker-consumed count, clean checker success and settlement remain mandatory. Qualification additionally requires bound publication records, cancellation absence, a clean summary and external release attesting strict integer exit zero. `snapshot/00-gb_staged_v6d.py:1559–1584,2821–2899,858–949`.
- No operative **2026-10-18 deadline** remains. Active limits use October 22. Native grace exhaustion remains explicitly reported and stops further launches. No additional unreported-survivor path was identified within the reviewed scope. Runtime realization is **NOT ESTABLISHED** by static inspection. `snapshot/00-gb_staged_v6d.py:288–298,2490–2497,2752–2780,3426–3430,3184–3187`; `snapshot/10-launch_gb_v6d.py:53–55`.