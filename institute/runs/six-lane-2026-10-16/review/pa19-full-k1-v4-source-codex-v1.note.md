**DISPOSITION: HOLD — three blocking MAJORs.**

All 26 files match the supplied SHA-256 hashes and byte counts. This review used static reads and hashes inside the snapshot only. Nothing was executed or modified.

1. **MAJOR — Incomplete/error feeds can still lose their integrity veto behind cap or bounded-stop outcomes.**

   [SOURCE05:209–230](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v4-source-review-v1/snapshot/05-src-m2_native_staged_v4.py:209) checks overruns and **completed** mismatching feeds early. Feed errors, incomplete delivery and failed close are checked later, at `SOURCE05:233–252`, after the ordinary cap/bounded returns.

   Consequently, an independently recorded CNF write/close failure with `complete=False`, combined with `proof_cap_hit` or `bounded_unknown`, can return `UNKNOWN / NOT_EVALUATED / halt_production=False`. The pipeline can omit `input_integrity_error` because its cap return precedes that assignment (`SOURCE05:293–300`). A clean supervisor then leaves no persistent veto (`SOURCE06:27–34,63–74`).

   **Repair:** classify independently established feed failures before cap/bounded outcomes. Preserve provenance distinguishing actual transport failures from cancellation or interruption caused by the bound itself. Add combined incomplete/write/close-failure controls with cap and bounded outcomes; keep expected TIMEOUT-interrupted proof replay ordinary UNKNOWN.

2. **MAJOR — The no-retry control necessarily fails its archive assertion.**

   [SOURCE13:524](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v4-source-review-v1/snapshot/13-src-check_m2_ms09_k1_v4.py:524) searches for `*.claim`. However, [SOURCE08:32–34](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v4-source-review-v1/snapshot/08-src-run_m2_ms09_k1_v4.py:32) archives the claim as `<name>.claim.<time_ns>`.

   Even when `calls == [second]` correctly proves the runner skipped the existing UNKNOWN, the next assertion fails. This prevents the aggregate suite from reaching the refusal controls, M6 old-marker control and mutation controls (`SOURCE13:724–728`).

   **Repair:** assert the specific second task’s archived claim, including its timestamp suffix, and verify that its original claim is absent and the first UNKNOWN remains unchanged.

3. **MAJOR — The checker-feed omission mutant is now a no-op and necessarily fails.**

   [SOURCE13:588–590](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v4-source-review-v1/snapshot/13-src-check_m2_ms09_k1_v4.py:588) targets a loop over `result['cnf_feeds'].values()`. V4 instead loops over `feeds.items()` (`SOURCE05:209`).

   The mutant therefore retains the production function. Its short checker feed remains INVALID, contradicting the required mutant UNSAT assertion at `SOURCE13:622`. Merely updating the loop matcher is insufficient: the explicit checker-feed predicate at `SOURCE05:245–252` independently rejects the fixture.

   **Repair:** update the mutation to remove the actual checker-feed enforcement being tested, require the expected AST changes, and demonstrate original rejection versus mutant acceptance. Preserve the production checks.

4. **MINOR — Several controls still assert rejection without asserting the specific cause.**

   Gate/marker controls assert only non-admission (`SOURCE13:210–213`). The post-wait old-marker control likewise accepts any gate rejection at [SOURCE13:253–255](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v4-source-review-v1/snapshot/13-src-check_m2_ms09_k1_v4.py:253). The safety-trip refusal control accepts any nonempty `trip_reason` and does not affirm that a group actually started (`SOURCE13:569–572`).

   **Repair:** require `STOP/veto m2k1-HALT.flag` for the post-wait case; require `group_started=True`, the intended external SIGTERM cause, explicit owned-child waiting and quiescence for the safety-trip case. Native negative controls should also assert their intended transport/verdict failure.

5. **MINOR — Inventory consumes only the persistent subset of the requested admission union.**

   `ADMISSION_MARKERS` includes `RESOURCE_STOPS`, but [SOURCE04:75–76](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v4-source-review-v1/snapshot/04-src-m2_supervised_runtime_v4.py:75) and [SOURCE10:247](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v4-source-review-v1/snapshot/10-src-m2_ms09_contract_v4.py:247) inspect only `PERSISTENT_VETO_FLAGS`. Resource STOPs are consequently absent from initialization veto inventories and final readiness reporting.

   Native gates still block those STOPs, so this is not a spawn bypass. **Repair:** expose the complete admission union through inventory and initialization receipts, retaining a distinct resource-stop classification.

The three v3 MAJORs resolve as follows:

| V3 MAJOR | V4 assessment |
|---|---|
| Old persistent vetoes omitted from admission | **Fixed for native admission.** Shared old/new flags are checked by `full_gate` (`SOURCE04:38–43,236–237`), after capacity waits before worker admission (`SOURCE04:289–298`), and immediately before solver/checker launches (`SOURCE05:283–286,307–310`). M6 now scans and publishes a veto deferral (`SOURCE09:137–152`). |
| Shadow contract rejected before intended behavior | **Original fault fixed.** Production-root loading precedes shadow adapters (`SOURCE13:704,343–349`); M6 validates before installing its scoped verifier (`SOURCE13:653–674`). M9’s resumed-veto assertion now requires inventory stage and the named marker (`SOURCE13:443–444`). The separate control failures above remain blocking. |
| TIMEOUT suppresses transport corruption | **Specified completed-mismatch cases fixed; broader precedence incomplete.** Completed bad feeds and bad completed replay are checked before TIMEOUT (`SOURCE05:209–218`). Exact feeds plus TIMEOUT-interrupted replay remain ordinary UNKNOWN (`SOURCE05:245–250`). Finding 1 remains. |

I found no substantive source change outside intended changes (1)–(4), apart from version/schema/path renames, in the supplied diffs.

The **published UNSAT/QUALIFIED acceptance predicate remains intact**: exact completed singleton verdicts, both complete measured CNF feeds, frozen binary observations, complete measured proof replay, and clean supervision/explicit settlement remain required by [SOURCE07:64–127](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v4-source-review-v1/snapshot/07-src-m2_supervised_evidence_v4.py:64). No acceptance bypass was found.

The normal pre-pin/pre-worker refusal paths now avoid HALT and item publication (`SOURCE06:96–123`; `SOURCE08:152–159`; `SOURCE09:177–180`). Supervisor safety still dominates worker UNKNOWN and persists a hold before capacity release (`SOURCE06:63–74,156–157`).

The active v4 production paths retain SIGTERM-only cleanup, explicit owned-child waiting, exclusive evidence publication, and no automatic native retry or `ps`/setuid-helper invocation. Frozen legacy `SOURCE21` contains older timeout/helper code but is outside those active paths.

Controls remain explicitly **NOT_RUN**, with no observed receipt (`SOURCE03:4,150`). Production remains HOLD pending the blocking repairs and corrected control evidence.