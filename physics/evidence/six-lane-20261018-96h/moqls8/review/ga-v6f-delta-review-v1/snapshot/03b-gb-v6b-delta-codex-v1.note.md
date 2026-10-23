VERDICT: HOLD

All file references below are relative to `snapshot/`.

| Finding from 03 | Disposition | Evidence |
|---|---|---|
| **H1 — physical containment** | **REPAIRED** | `check_desk_tree()` requires real directories with matching realpaths; PRE-EXEC creation is directly in DESK. Launcher additionally requires a regular, physically contained PRE-EXEC. `00-gb_staged_v6b.py:3086–3113`; `10-launch_gb_v6b.py:62–100`. These are pathname checks, assuming the namespace remains stable after checking. |
| **H2 — helper capacity** | **REPAIRED** | CAP=4/MINE=3 covers native, driver and one transient helper. The same constant controls admission, checker boundary and flight. Helpers run sequentially. `00-gb_staged_v6b.py:294`, `:1009–1076`, `:1353`, `:2458–2459`, `:2528–2530`. Actual runtime compliance is **NOT ESTABLISHED**. |
| **H3 — GA markers** | **REPAIRED** | Both old and new GA desk markers remain, and exclusion tests either marker. `00-gb_staged_v6b.py:313–314`, `:1086–1089`. |
| **H4 — retained logs** | **REPAIRED** | Sink state precedes descriptor claim; independently protected closes, capped writes and continued draining are present. Sink faults veto in flight. A bounded join precedes `stage1_ok()`’s log read; unfinished/unclean sink refuses stage 2 and causes terminal stop. Filter writes at most 32 MiB and caps cause terminal stop. Its kept digest/count still describe exactly bytes written, consistent with the unchanged disk-hash criterion. `00-gb_staged_v6b.py:1989–2004`, `:2197–2261`, `:2468–2469`, `:2544–2563`, `:2622–2627`, `:2747–2759`, `:2851–2859`. |
| **H5 — GO file type** | **REPAIRED** | `lstat`, regular-file and realpath checks precede reading; location errors also return before reading. `00-gb_staged_v6b.py:1693–1708`. |
| **H6 — chunk/deadlines** | **PARTIAL** | DRIVER_T0 starts at run entry; supplied absolute end is validated. Both stage boundaries require remaining backstops to fit; controls use 300 s backstops. Live-child polling checks elapsed and absolute limits. However, completion bypasses those checks: NEW 1. Recorded/enforced end equality also fails: NEW 4. `00-gb_staged_v6b.py:2298–2299`, `:2470–2477`, `:2515–2519`, `:3186–3196`. Arithmetic is correct: **19:00:33 + 3720 + 120 + 6360 + 120 = 21:52:33 = 21:56:33 − 180 − 60**. |
| **H7 — evidence limits** | **ACCEPTED-LIMIT** | All 16 supplied files match MANIFEST SHA256 entries, repairing the missing-manifest issue. The native audit covers gbs5 only. v6b native controls, science, actual GO and release are **NOT ESTABLISHED**. `MANIFEST.json:3–99`; `11-moqls8-gb-staged-gbs5-controls-parent-audit-v1.json:4–9`. |

1. **NEW — MAJOR: completion can bypass the new deadlines.**  
   `supervise()` reaps first and returns immediately for a reaped child, checking only latched signal/scanner/exclusion/helper state. Absolute end, DRIVER_T0 and stage duration are checked later, exclusively for an unreaped child. There is no terminal deadline veto. After suspension or delayed scheduling, a checker can remain alive beyond the recorded end plus 120 s, finish before the next supervision iteration, and leave no explicit deadline violation. PASS/COMPLETE and exit 0 remain possible if the other predicates hold; the reaped timestamp merely exposes the lateness for an external audit. Conservatively reject late or unverifiable completion before returning from supervision.  
   `00-gb_staged_v6b.py:2411–2424`, `:2470–2485`, `:2744–2761`, `:2857–2876`, `:3463–3465`.

2. **NEW — MAJOR: launcher ownership does not cover every post-spawn path.**  
   Popen occurs before the protected `try`; closing the console descriptor occurs outside it. An exception there skips waiting altogether. More practically, KeyboardInterrupt during the unprotected `os.waitpid()` inside `finally` escapes without writing settlement. Because the driver has its own session, foreground interruption need not reach it. Thus “finally-wait” is established only on ordinary paths. Enclose ownership immediately around spawning and defer interruption until reap and settlement reporting.  
   `10-launch_gb_v6b.py:143–147`, `:182–200`.

3. **NEW — MAJOR: failed launch-record publication does not stop the launch.**  
   A `put_json()` failure is caught, the driver continues, and the launcher eventually returns its status—even zero. Exclusive creation reserves a pathname, not space or successful publication. The mandatory registration can therefore be absent throughout native execution; its error is reported only after the run finishes. This contradicts immediate parent-readable registration and permits a successful launcher status despite registration failure. Fail closed while retaining child ownership and settlement.  
   `10-launch_gb_v6b.py:130–144`, `:180–200`; `06-launch-contract-tightening-v1.json:23`.

4. **NEW — MINOR: recorded absolute end differs from the enforced value.**  
   The launcher records the original floating-point `chunk_end`, but passes `"%.3f" % chunk_end`. The driver enforces the parsed rounded value. Equality is therefore **NOT ESTABLISHED**; rounding can extend enforcement by approximately 0.5 ms. Quantize once, then use that identical value for environment, record and settlement deadline.  
   `10-launch_gb_v6b.py:123`, `:141`, `:164–169`; `00-gb_staged_v6b.py:3190–3196`.

5. **NEW — MINOR: STOP-registry containment is lexical, and the frozen registry is not required.**  
   A path such as `LANE/review/../code/gb_staged_v6b.py`, with its matching digest, passes the registry test. Ancestor symlinks are also unchecked. Moreover, any matching file is accepted rather than requiring the supplied STOP registry’s path/hash or an explicit supersession. Canonicalize its parent and bind the intended registry. Citation of snapshot 14 and stop dispositions in an actual GO are **NOT ESTABLISHED**.  
   `10-launch_gb_v6b.py:108–117`; `MANIFEST.json:83–86`; `06-launch-contract-tightening-v1.json:25`.

Verified:

- Review used static reads, comparison and hashing only: no interpreter, checker execution, writes or delegation. Actual source diffs contain the listed changes. No operative **2026-10-18 deadline** remains; current cutoff constants and PRE-EXEC limits use October 22. `00-gb_staged_v6b.py:279–286`, `:3165–3167`.
- Paired source-region hashes match gbs5 for ACCEPTANCE, criteria/evaluation, control definitions and allowed outcomes, regeneration/GBBINDING binding, measured writers/collector/feeder, publication/terminal exit, helper supervision and `qualification_problems()`. Release-directory changes and the filter cap are the stated exceptions. `00-gb_staged_v6b.py:340–490`, `:612–942`, `:986–1078`, `:1469–1612`, `:1779–1963`, `:2802–3005`.
- Seven preregistrations remain: **unsat → PASS**; **sat-checker → AS_PREREGISTERED_NOT_VERIFIED**; **short-cnf, truncate, suffix, digest-alter, early-close → AS_PREREGISTERED_FAIL_CLOSED**. Exact native exit/status/diagnostic alternatives and intended-failure checks are unchanged. Old controls cannot satisfy the new script/label identity. `00-gb_staged_v6b.py:385–453`, `:1727–1775`.
- No new bypass of complete measured refutation transport was found: both CNF feeds remain bound, collected/buffer/delivered proof digests must agree, checker-consumed count must equal delivery, and qualification still requires completion, clean summary, cancellation absence and external parent release. Actual v6b refutation remains **NOT ESTABLISHED**. `00-gb_staged_v6b.py:849–940`, `:2815–2878`.
- Launcher checks status, lane, desk, driver/launcher hashes, PRE-EXEC hash, ordered items, tightening hash and 80 MiB reservation; verifies real output directories; exclusively reserves all three outputs before Popen; and ordinarily propagates driver exit/signals. Exceptions are NEW 2–5. `10-launch_gb_v6b.py:62–74`, `:94–144`, `:184–200`.