**DISPOSITION: HOLD. Three MAJOR findings block production.**

All 26 snapshot files match their supplied SHA-256 hashes and byte counts. This review used static reads, comparison, and hashes only. No source or controls were executed.

1. **MAJOR — Per-spawn admission drops persistent v2 vetoes. Blocking repair.**

   [SOURCE17:225–226](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v3-source-review-v1/snapshot/17-src-m2_supervised_runtime_v3.py:225) checks only the new `m2k3-*` markers, omitting `m2k1-SAT.flag`, `m2k1-INVALID.flag`, `m2k1-HALT.flag`, and `m2k1-QUARANTINE.flag`. The deletion is explicit in `SOURCE02:2045–2046,2095–2097`.

   M9’s initialization inventory still recognizes both generations (`SOURCE13:247–269`; `SOURCE15:85–86`). M6 has no equivalent initialization scan (`SOURCE23:131–160`). Consequently, with COUNT permitting admission and the other guards passing, M6 can launch—and qualify an otherwise valid item—while an old persistent hold remains. M9 also misses an old marker appearing after initialization.

   **Repair:** use the union of old and new veto names at every admission gate. Share the marker registry with inventory, and add old-marker controls covering M6 and post-wait admission. Do not clear or reinterpret old markers automatically.

2. **MAJOR — Shadow controls reject the contract before reaching the intended runner behavior. Blocking repair.**

   [SOURCE24:384,467](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v3-source-review-v1/snapshot/24-src-check_m2_ms09_k1_v3.py:384) replaces `C.LANE` with a shadow directory, then calls the actual runner (`SOURCE24:415,493`). The frozen checker authority still names the production lane (`SOURCE03:52–54`).

   `C.load()` requires that checker path to equal `C.LANE/tools/drat-trim/drat-trim` (`SOURCE13:188`). It therefore rejects this unchanged contract under the shadow root. The runner records initialization deferral before reaching its inventory veto or queue logic (`SOURCE15:83–86,103–106`).

   Two consequences follow statically:

   - The resumed-veto control can falsely pass: `SOURCE24:418` accepts **any** initialization deferral without checking its cause.
   - The no-retry control leaves `calls == []`, then fails its required `calls == [second]` assertion (`SOURCE24:489–496`).

   **Repair:** validate the frozen contract against the production authority root before changing output roots, then supply that validated contract through a scoped control adapter. Preserve production path checks. Require the veto control to prove inventory was reached and the deferral specifically resulted from the persistent veto.

3. **MAJOR — Checker TIMEOUT can suppress independently recorded transport corruption. Blocking repair.**

   [SOURCE18:225–238](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v3-source-review-v1/snapshot/18-src-m2_native_staged_v3.py:225) returns ordinary UNKNOWN for an exact completed `s TIMEOUT` **before** checking the checker CNF feed and proof replay.

   With otherwise valid solver measurements, a checker-feed SHA mismatch or a completed replay with the wrong SHA can therefore produce:

   `status=UNKNOWN`, `integrity_status=NOT_EVALUATED`, `halt_production=False`.

   The pipeline does not separately promote these checker-stage measurements into `input_integrity_error` or `proof_integrity_error` (`SOURCE18:289–315`). A clean supervisor then permits ordinary UNKNOWN without a veto (`SOURCE19:63–72`); inspection likewise returns `UNQUALIFIED` without evaluating the transport evidence (`SOURCE12:101–112`).

   This does **not** admit UNSAT, but it leaves the required persistent treatment of corrupted evidence incomplete.

   **Repair:** evaluate independent transport-integrity faults before choosing an ordinary timeout outcome. Keep scientific UNKNOWN, but retain INVALID integrity metadata and persist its veto when corruption is established. Add TIMEOUT-plus-bad-feed and TIMEOUT-plus-bad-replay controls; distinguish expected timeout interruption from independently established corruption.

The seven v2 findings resolve as follows:

| V2 finding | Actual v3 assessment |
|---|---|
| **1. Tier-2 retry not fail-closed** | **Fixed by removal.** Capacity owns one normal token; the owner makes one supervision call. Existing results, including UNKNOWN, are skipped (`SOURCE17:249–287`; `SOURCE19:116`; `SOURCE15:112–115`; `SOURCE23:147–150`). |
| **2. Attempt hashes replace frozen authority** | **Fixed.** Contract authority enters admission, job, and qualification unchanged (`SOURCE15:93–94`; `SOURCE19:78,110–112,138–143`). Every gate compares observed binaries against it; qualification checks those observations against contract expectations (`SOURCE17:177–189,218–220`; `SOURCE20:36–41,68,84`). |
| **3. Ordinary UNKNOWN erases supervisor safety** | **Fixed in outcome composition.** Supervisor errors dominate worker outcomes, and veto publication precedes capacity release (`SOURCE19:50–72,150–151`). Finding 1 above is a separate admission regression. |
| **4. Late leader not explicitly reaped** | **Fixed.** Exact `Popen` retention, explicit `wait()`, and post-reap group checks are implemented (`SOURCE25:337–340`; `SOURCE17:321–342`). |
| **5. Start-of-chunk accounting envelope** | **Replaced with the stated bounded census amendment**, detailed below. |
| **6. Failed certification classified INVALID scientifically** | **Scientific classification fixed:** unsuccessful certification returns UNKNOWN with separate metadata (`SOURCE18:191–239`). Integrity-veto completeness remains partial because of finding 3 above. |
| **7. Wrong lifecycle-control expectations/schema** | **Original mistakes corrected:** definite nonclean stops no longer require uncertainty; `killpg_error` and late-leader controls are present (`SOURCE24:187–191,260–298`). The suite remains blocked by finding 2 above. |

The accounting amendment is implemented as stated, subject to its documented external-writer assumption:

| Requirement | Static verification |
|---|---|
| **Census age ≤600 s** | Hash-bound census records are validated; age greater than 600 s triggers refresh. Age is checked again after the other guards (`SOURCE17:159–174,204,235–238`). Age is measured from census completion. |
| **Re-census after waits >600 s** | Capacity wait duration forces refresh in the owner lease and immediately before worker admission (`SOURCE19:90–95`; `SOURCE17:273,281–283`). |
| **Unknown census refuses** | Census creation and cache loading reject unknown accounting, stat errors, or noninteger usage; gate measurement failures deny admission (`SOURCE17:144–149,167–168,239–246`). |
| **Whole-plan reservation over unfinished work** | The gate requires at least the full original plan bound, **2,631,532,544 B**. Keeping the full bound rather than subtracting finished items is conservative (`SOURCE17:31–34,200–203`; `SOURCE03:72273`; `SOURCE04:38`). |
| **256 MiB margin** | Exactly **268,435,456 B**, added to census usage plus the whole-plan bound (`SOURCE17:36,203`). |
| **Fresh statvfs before each spawn** | `full_gate()` takes fresh `statvfs` after census processing; worker, solver, and checker spawns follow their gates (`SOURCE17:229–238,281–287`; `SOURCE18:265–268,289–292`). |

The residual remains explicit: the route bound covers route writes, while other lane writers must add no more than 256 MiB within 600 s (`SOURCE01:22`; `SOURCE17:5–7`). The code does not establish writer exclusion; that is the parent’s stated assumption.

The local adapter introduces **only** the optional retained-child parameter and append; direct comparison against SOURCE05 agrees with `SOURCE02:2916–2933`. I found no additional monitoring or signaling change. Settlement requires matching owned handles, group quiescence, explicit leader waiting, and another group check before setting capacity safe (`SOURCE17:321–342`). A late successful exit does not turn the original nonclean supervisor receipt into a clean one.

For a **published owner `checked=True` UNSAT or final QUALIFIED item**, I found no bypass of complete measured CNF feeds, exact singleton verdicts, matching frozen binary observations, complete measured proof replay, or clean settlement. These conditions are checked by `SOURCE18:214–239` and independently by [SOURCE20:73–127](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v3-source-review-v1/snapshot/20-src-m2_supervised_evidence_v3.py:73); qualification failures downgrade the owner result to UNKNOWN (`SOURCE19:137–145`). B3 remains a separately classified structural acceptance (`SOURCE13:344–347`).

**No automatic native retry path remains in the v3 production runners.** Capacity, settlement, census-refresh, and veto-publication loops do not respawn attempts.

Production remains HOLD pending the three blocking repairs, updated hashes/contracts, and observed passing corrected controls. The supplied pack explicitly records controls **NOT_RUN** and `observed_receipt: null` (`SOURCE01:4,149–153`).