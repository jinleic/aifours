# Supervisor v16 telemetry/type-binding interface — REVIEW ONLY

Recorded after actual `/bin/date`: 2026-10-19T11:31:57-0700.
Source `code/owned_supervisor_v16.py`, SHA-256 `71965fb7b378cebd5fa2624a557982f6fc21a46f501da0acd2f36a3388082770`.
Diff from immutable v15: `review/owned_supervisor_v15_to_v16.diff`, `f400b24da126cd678427aeff5c0923f8a4d13ba73f6c0ba64e248f08643714cb`.

This is not source acceptance, package acceptance, an item GO or runtime authority. Parent source15 fixed guard behavior, binding correction fabe57ab, actual owned bounded `/bin/date`, conservative census, at-most-one freshly checked TERM, finite WNOHANG cleanup, actual14 terminal path, exclusive publications and parent release gates remain. No science/numerical source changes or new accepted statuses. Original22 exact outcomes remain unchanged and unexecuted.

## Exact authority types and initial fit

`typed_equal(left,right)` checks exact JSON scalar/container types recursively; booleans cannot alias integer CPU slots or zero reservation totals. It is used for the complete GO config entry, authorization reread equality, and preparation source/allocation/run-anchor bindings. No authority is relaxed.

Receipt header and current reconciliation contain `initial_fit`:
`{start_epoch,start_mono,chunk_epoch_bound,owned_epoch_bound,fit_epoch,fit_mono}`.
All are actual raw clock telemetry. Formulae remain:
- chunk epoch bound = start_epoch + cfg.max_chunk_seconds -120;
- owned epoch bound = cfg.owned_compute_settled_by_epoch -180;
- fit_epoch = min(the two);
- fit_mono = start_mono + fit_epoch - start_epoch.

Every commit must satisfy its exact original epoch/monotonic fit checks. The applicable `authorization` is also exposed in receipt/current evidence, exactly the object from authorization_io: GO/stability digests, not_after_epoch, parsed stability_epoch and canonical actual stability_date. Only deliberate `go_unlisted` has no established authorization. The existing launch artifact already carries the duplicated launch_commit/mono_spawn/epoch_spawn/start_date; the successor checker must join all of them, not merely two digests.

## Compact completed native identity acquisition references

`identity_events` is append-only. Reference numbers are one-based array positions. Each row is:
`[uniqueid, variant_index, native_status, mono_begin, mono_end, unproved_at_retention]`.
The two clocks bracket the actual `identify(pid)` acquisition; they are not invented registration times. `variant_index` addresses that UID's `identity_history.variants`, zero-based. A variant contains full acquired metadata except status may differ; reconstruct the exact acquired identity by copying the variant and replacing status with the row's native_status. Telemetry variant identity is `identity_form`: pid/uniqueid/idversion/euid/ruid/ppid/pgid/traced/comm; signal-safety fingerprint remains the unchanged original fingerprint.

History `observations` is exactly the count of committed acquisition-event references for that UID, not a claimed independently verified scalar. It does not count registration as another acquisition. Each identity ledger has first_event_ref/last_event_ref and mono_first_begin/mono_first_seen/mono_last_begin/mono_last_seen; their identities/times are reconstructible from the event tape. First/last select physical acquisition chronology, not later retention order. A final resource bracket can be retained after nested stop/helper observations, so event array order is retention order and must not be misrepresented as strictly increasing acquisition time. Receipt→current event prefix remains exact.

Unproved history has its own actual first/last event references/intervals. The boolean row flag records the source's unproved classification at retention; later proved ownership never erases the historical record. All events share the existing conservatively charged4MiB history cap; no cap is increased. A current acquisition that cannot be charged stays in bounded `history_overflow.completed_identity_observation` with full identity, actual acquisition interval and source; the first overflow witness is retained too. Scanning does not resume. Such an outcome is HOLD, not successful qualification. Raw once-only signal witnesses remain available even with history halted.

Baseline identities have parallel event_refs. Every census has owned_event_refs/unproved_event_refs parallel to the full identity arrays, including explicit empty arrays on an aborted pre-header attempt. Rooted registry entries carry identity_event_ref; current-parent registrations additionally carry parent_before_ref/child_ref/parent_after_ref in proof. Registration reuses the actual acquired snapshot rather than pretending to observe it again. The checker must validate every historical receipt/current owned identity and helper-proof identity against the fully rooted registry, not just final/reported identities.

Measurements retain the original identity and identity_event_ref, actual before_task_event_ref, actual mono_task_begin/mono_task_end, full raw identity_after plus identity_after_interval and identity_after_event_ref, RSS/ticks/busy/mono_observed. The final raw bracket is still acquired/verified and the complete composite/partial totals enforced before fallible history charging. On cap, final ref may remain null while the complete composite/interval remains in bounded overflow evidence; it cannot qualify as a complete measurement. Compatible acquisition/task intervals and full applicable fingerprints must be checked.

Signal records preserve full identity_observed, mono_check, actual mono_identity_begin/mono_identity_observed, and mono_sent if sent; identity_event_ref is supplied when retained. Native identity/signal safety is not delayed by charging. On a history cap the direct raw bounded signal witness persists and no cap outcome passes. Helper TERM continues to update, never replace, its signal record.

## Actual accounting history and minimum witness

`accounting_observations` records every complete native accounting result as:
`{id,phase,inside_helper,mono_begin,mono_observed,resources,retained,returned}`.
Resources remain exactly `{charged_bytes,lane_bytes,free}`. IDs are one-based append positions. `returned` becomes true only after the accounting completion deadline check; a complete but late observation is not a successful b/end. A charging failure leaves its actual bounded event in last_accounting_observation/min_free_witness and overflow, with retained=false/returned=false, never as a successful caller return.

`min_free_witness` is the actual establishing accounting event (first one on ties); min_free must equal the minimum of the applicable actual observations and the witness's free. No fresh value is substituted. For the five original admission negatives the receipt has only the final pre-publication accounting observation, so receipt.min_free equals publication_precheck.free exactly.

Admission, launch preparation, pre-GO preparation, each sample and publication_precheck now include their corresponding accounting_ref; launch/pre-GO resources are retained too. Receipt/current histories and witness permit exact reconciliation before every return. Actual b/end/payload exports and honest nulls remain unchanged from v15. Current reconciliation includes the complete actual history and last observation; receipt freezes its pre-publication prefix.

## Helper deadline provenance

Deadline records expose actual `{mono_created,seconds,until,end}` without changing their original calculation/check. Helpers expose call_deadline and cleanup_deadline plus existing actual call/cleanup timestamps, mono_spawn/epoch_spawn, and mono_pid_registered. PID registration still occurs immediately after posix_spawn returns, before later fallible work. `identity_event_ref` joins the initial actual helper identity.

The checker must reconstruct the call/grace deadline from its real creation time, configured duration and then-applicable fit/stop/exit cutoffs, join launch/registration/proof/reap chronology, and reject independently plausible but unrelated timestamps. No new helper is introduced.

## Coherent main-stream telemetry (not helper capture)

Each main stdout/stderr row contains original counts/closure/error/hash fields plus cap_bytes, write_inflight, pending_bytes, sha256_prefix, mono_created, mono_last_update, mono_last_read, mono_last_write, mono_eof and mono_close_completed. Updates of related read/write fields are atomic dict updates; in-flight data is explicit. Overflow becomes visible with the actual overflowing read rather than being hidden while its capped write completes. This does not relax a limit or add a new accepted status.

The prefix digest covers completed retained writes. During an in-flight write the file can contain a partial uncommitted extent, but its recorded completed prefix remains verifiable. Any write/close error is HOLD; the old completed-write sha256_written is not falsely claimed as the full physical artifact hash in that error state. Healthy final closure requires exact retained bytes/digest and no in-flight remainder. Every sample must have typed monotonic counters and causally valid prefix/closure/hash relationships; helper captures remain in their separate helper schema.

Stream snapshots are copied before the sample's timestamp and frozen once for the receipt/digest map, preventing a live row from changing while serialized. Receipt stream_snapshot_mono and current mono_snapshot bound their respective copied rows. Original stream capture/cleanup and cap behavior remain finite and conservative.

## Boundaries and remaining work

No field here proves an OS-universal sandbox or independent runtime verification. The charged cap can cause conservative availability HOLD and must not be raised or waived to obtain PASS. No source16 import/helper/control/test/fixture/numerical execution occurred; only AST parsing and hashes.

Packagev9 must rebind all pins and implement all eight v8 review repairs, including full main-stream checks, complete authorization/fit replay, exact identity event/count/interval reconstruction, every historical rooted registry entry, full signal/busy/RSS fingerprints, canonical private join role/parent/incarnation/deadline and complete bounded original intermediate transport. Child/writer/checker successors and full matrix final pins are not admitted by this source contract. Existing22 and the full v13/v14 matrix remain separately required and unexercised.
