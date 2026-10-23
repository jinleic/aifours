**DISPOSITION: HOLD — one blocking MAJOR and one MINOR.**

All 26 files match the supplied SHA-256 hashes and byte counts. Review was confined to static reads and hashes inside the snapshot; no source execution, writes, network, or delegation.

1. **MAJOR — Bounded exits can still discard a real feed failure before classification.**

   [SOURCE05:334–347](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v5-source-review-v1/snapshot/05-src-m2_native_staged_v5.py:334) catches `BoundedUnknown`, sets `stop`, and immediately copies the feed dictionaries. This bypasses the feeder joins at `SOURCE05:305–306,332–333`.

   However, `feed_cnf` publishes its error, cancellation and close observations only at its final `record.update` (`SOURCE05:103–115`). A valid interleaving is: a feeder encounters a real write/close failure; the bounded-exit thread snapshots its still-empty record before that update; the feeder’s subsequent update goes to the detached dictionary. `outcome` then returns `UNKNOWN / NOT_EVALUATED / halt_production=False` at `SOURCE05:241–244`.

   Supervision does not necessarily supply the missing veto: the native process can exit before the supervisor’s final sample (`SOURCE23:287–306`). Clean supervision then preserves the ordinary UNKNOWN, and `persist_veto` writes nothing (`SOURCE06:27–34,63–74`).

   The 16 new cases construct already-finalized feed records (`SOURCE13:344–358`), so they cannot detect this race. **V4 MAJOR 1 is therefore only partially fixed.**

   **Repair:** after setting `stop`, settle every started CNF feeder before freezing its observations. Use bounded thread joins; classify an unsettled feeder as an explicit lifecycle/integrity failure. Add a deterministic, synchronized pipeline control that delays a real failing feeder’s publication across the bounded exit and requires persistent INVALID even with clean supervisor settlement.

2. **MINOR — Exceptional native controls still accept unrelated causes.**

   [SOURCE13:804](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v5-source-review-v1/snapshot/13-src-check_m2_ms09_k1_v5.py:804) accepts any reason beginning `incomplete native lifecycle`. The corresponding ownership assertion also accepts any nonempty supervisor trip, including measurement uncertainty (`SOURCE13:188–192`).

   Consequently, those controls do not establish that the intended post-Popen or collector-start injection caused the rejection.

   **Repair:** assert the exact injected `CONTROL post-Popen exception` or `CONTROL collector start failure` reason, affirm that the injection ran, and require the intended supervisor cleanup cause. This finding is individually nonblocking.

The five v4 findings resolve as follows:

| V4 finding | V5 assessment |
|---|---|
| Feed failures hidden by cap/bounded outcomes | **Partial.** Finalized records now receive correct precedence (`SOURCE05:219–244`); the publication race above remains. |
| Broken no-retry archive assertion | **Fixed statically.** Specific claim plus numeric timestamp suffix, original claim absent, first UNKNOWN SHA unchanged (`SOURCE13:533–554`; production naming `SOURCE08:31–36`). |
| No-op checker-feed mutant | **Fixed statically.** Exactly one counted edit is required; the checker predicate fixture and cap-hides-real-feed mutant distinguish original rejection from mutant acceptance (`SOURCE13:616–676`). |
| Missing specific-cause assertions | **Mostly fixed.** Gates, markers and post-wait controls assert their causes (`SOURCE13:210–218,260–262`). The safety-trip control requires group start, external SIGTERM, matching owned-leader wait and quiescence (`SOURCE13:598–608`). The exceptional-native gap above remains. |
| Incomplete admission inventory | **Fixed.** Classified union is exposed (`SOURCE04:75–85`; `SOURCE10:382`), M9 has a distinct resource-stop stage and control (`SOURCE08:99–103`; `SOURCE13:704–724`), and M6 distinguishes veto-scan from resource-stop (`SOURCE09:138–153`). |

The feeder’s **finalized provenance is correctly constructed**: cancellation is assigned at the explicit stop/deadline checks; real syscall failures retain uncancelled provenance, and a close failure has an independent `close_error` (`SOURCE05:76–115`). Expected TIMEOUT-interrupted replay remains ordinary UNKNOWN with exact CNF feeds (`SOURCE05:260–264`; control `SOURCE13:330–335`).

I found no substantive source change outside intended changes (1)–(5), apart from version/schema/path renames. Both frozen contracts bind the supplied v5 source hashes (`SOURCE24:5–25`; `SOURCE25:8–28`).

The **published UNSAT/QUALIFIED predicate remains unchanged**, apart from v5 identities: exact completed verdicts, both measured CNF feeds, complete matching proof replay, frozen binary observations, clean supervision and explicit settlement remain required (`SOURCE07:64–127`; `SOURCE11:97–113`). No acceptance bypass was found.

Active v5 paths retain SIGTERM-only cleanup, explicit owned-leader waiting before capacity release, exclusive evidence creation, and no automatic retry or setuid-helper invocation (`SOURCE23:213–264,337–390`; `SOURCE04:335–377`; `SOURCE10:59–74`). Legacy `SOURCE21` contains timeout/helper code but is outside these active paths.

For the operational note: **the proof-cap escalation itself protects certification and process ownership; its cost is liveness/availability and manual clearance.** A solver still alive after worker exit triggers supervisor cleanup and persistent HALT, with capacity retained through settlement. This escalation is conditional: a solver that exits before the final sample can leave an ordinary UNKNOWN. It therefore cannot substitute for preserving feed failures in finding 1.

Controls remain **NOT_RUN**, with no observed receipt (`SOURCE03:4,147–151`).