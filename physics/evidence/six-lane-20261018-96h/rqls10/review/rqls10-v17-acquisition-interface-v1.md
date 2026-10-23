# Source17 acquisition-first recovery contract — REVIEW ONLY

Actual `/bin/date` before this write: 2026-10-19T12:33:40-0700.
Source `code/owned_supervisor_v17.py`: `6222526cd4a9ec7c61d413a52129b24020769fda2b953ca28e39c3d133464a21`.
Diff `review/owned_supervisor_v16_to_v17.diff`: `0bfa4891fdceb416115ec17820d44cc017213d2a68ab17f2b15b8630430d1d8a`.

This is a frozen source-review candidate, NOT source-ready, package-ready, runtime authority or GO. The parent scope is RUN `review/rqls10-supervisor-v16-HOLD-source17-scope-parent-v1.json`, SHA `dd90a376c7f080182f8d4b68137f23bb706b7e0ff3c4e825a10abd031b4485c3`. It repairs the full source16 review `ed93189282d5e89ecffe5d0738b755e27571bc3808b4b3045042939003c0e9de` (1F/4M), preserving source16 unchanged. No scientific source/NumPy or runtime was touched.

## Raw first, optional timing second

Returned native data and destructive effects are stored before auxiliary clocks. `aux_clock(record,field,epoch=False,sink=False)` stores the actual clock or null plus an error type, latches `timing_failed`, and never invents time. Non-sink failures retain a raw failure row before any timestamp. Missing clocks cannot qualify as fresh or complete evidence. Mandatory deadline/fit/fingerprint checks remain mandatory; a missing usable cleanup deadline denies TERM rather than widening it.

`raw_acquisitions` is a bounded (128 simultaneously pending) map of actual native acquisition records. Each has id/kind/source/native_returned, nullable begin/end, identity and event_ref; task records additionally retain their returned RSS/ticks and linked partial measurement. The native identity/result is assigned before end timing. Pure installer callbacks put validated main/helper cleanup identity/group state in place before any end-clock/history failure can escape. Healthy complete acquisitions move into the unchanged charged canonical identity-event tape; pending/missing-time/cap acquisitions remain raw, with null intervals/references and HOLD. There is no fake successful event or interval.

The healthy v16 compact event/count/variant/first-last/fit/typed-authority schema remains. Raw evidence and nullable errors are not accepted replacements for healthy original22 evidence. The4MiB history cap is unchanged and no truncated or uncharged overflow is relabelled complete.

## Known main PID recovery

Immediately after successful posix_spawn, the pre-registered record receives PID and the role-specific main `s.child/s.pid` attribution before the optional PID-registration clock. An auxiliary failure cannot erase that attribution.

Both a spawn-call exception before local `child` assignment and the outer known-PID exception handler consume the actual registered record. Recovery reuses actual spawn telemetry where available, attempts a full native identity acquisition with immediate validated cleanup-state installation, retains any missing timing honestly, requests the existing fresh-deadline/full-fingerprint checked stop, closes retained parent/raw endpoints, and uses the destructive-result-safe reap/observation path. Merely moving the timestamp is not the repair. Missing identity or captures keep allocations held; no alias or permissive fallback is added.

## Destructive wait before timestamps

There is one `os.waitpid(record['pid'], os.WNOHANG)` site, in `reap_record`. Its returned native tuple/raw status and terminal reaped state/rc are retained before optional monotonic/epoch timestamps. Main and helper paths, including history-cap cleanup, use it. A consumed terminal record cannot be re-waited or re-signalled because an exit timestamp is null. A nonterminal native wait event is not falsely called a reaped exit. `main_wait` and helper raw-wait fields expose the actual data; clock failure retains null time and HOLD, never a fabricated exit instant.

## Verified resource data before telemetry

Task RSS/ticks are stored in a raw record immediately after the native return. The final identity acquisition stores its full native result before end timing; its pure installer verifies the unchanged safety fingerprint, installs the composite/partial RSS total and latches a known RSS excess before fallible end-clock work. BUSY stays null when the required clocks are unavailable; no false BUSY value or successful measurement ref is invented. Known RSS enforcement still occurs, and incomplete returned observations cannot disappear into a successful retry. Healthy rows preserve the v16 task/identity event references and actual intervals; pending raw measurements remain explicit and unqualified.

Main stream native read counts/EOF, native write progress and raw closure flags precede clocks. `write_all` has an internal fixed progress callback used by the sink so each returned write count reaches prefix bookkeeping before the next deadline check. `prefix_bytes` says exactly how many retained bytes the prefix digest covers; `hash_pending` distinguishes an acquired write count from hash completion. Null read/write/EOF/close timing and errors remain HOLD. Helper captured bytes/EOF are also retained before post-read deadline checks. Main streams and metadata-helper captures remain separate schemas.

Raw stream flags include eof_seen/fsync_returned/out_closed/pipe_closed. They are not substituted for successful complete `closed` evidence. Cleanup continues finite raw close attempts when no timing deadline can be established, without claiming timed completion or fresh coverage.

## Native free/accounting and honest stages

The actual fstatvfs result/free value is stored before any post-completion check. The completed accounting resource values and actual establishing minimum witness are installed before the optional observation clock; the original completion deadline is checked afterward. An unsuccessful call remains returned=false; b/end caller fields remain genuinely null if the assignment never returned. The four pre-payload/pre-b/pre-end/post-end cases are not collapsed and no fresh value substitutes for historical evidence.

Receipt/current evidence adds timing_failed/raw_acquisitions/last_native_free/main_wait and actual raw helper wait/recovery fields. Failure-row/trip times may be null on evidence failure; those are not healthy original22 outcomes and must not be admitted by broadening accepted sets.

## Missing-time bounded cleanup is not settlement

A timing failure prevents further scanner retries and successful GO/ACK completion. Necessary raw endpoint/WNOHANG/drain attempts remain finite; the helper raw cleanup has an explicit maximum3 passes, always leaves settled=false, and introduces no clockless TERM. Main cleanup requests the existing safe stop if one has not been requested; all original deadline/fingerprint prerequisites still apply. A current mandatory clock failure cannot be waived just because an earlier raw identity exists.

A begun ACK retains the v15 actual14 terminal behavior and cannot emit a second stdout summary. Missing/incomplete captures still hold allocations. The ordinary GO-newline/EOF and mutation-only canonical creation line, original-inode checks, negative-control authorizations, conservative all-unproved/mixed-UID coverage and independent parent five-part release remain unchanged.

## Verification and pending work

Only static AST parsing and exact-byte hashing occurred. No source import, test/build/lint/formatter, helper/control/fixture/preparation, native/numerical run or Q1 occurred. All original22 and the full v13/v14 matrix remain unexercised. Their exact expected healthy outcomes are unchanged; new raw/null failure evidence is HOLD, not a waiver.

Packagev9 producers/oracle must bind the final independently accepted source and complete all eight v8 consumer repairs, including nullable-failure rejection for healthy controls, full accounting/auth/fit/events/registry/stream/signal/private-join transport validation. Matrix final pins remain paused until the telemetry contract stabilizes. The parent owns every allocation/gate/admission/release and the still-separate real five-part release implementation; no readiness verdict supplies that implementation or grants runtime.
