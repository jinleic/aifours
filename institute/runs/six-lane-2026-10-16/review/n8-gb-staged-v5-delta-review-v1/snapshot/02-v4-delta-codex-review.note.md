**CONTROL SOURCE: AWF (blocking). SCIENCE: HOLD.**

All 12 supplied SHA256 hashes and byte counts match. Review used static reads, comparison and hashing inside the snapshot only. No interpreter, tests, native processes, writes, network or delegation were used.

The two previous MAJORs remain **partially repaired, not closed end to end**:

| Previous MAJOR | Disposition |
|---|---|
| Failed publication remains admissible — SOURCE00:8–9 | The item-level bypass is repaired. The final run-summary publisher reintroduces premature admission and lacks a reliable fallback when its veto cannot be created. |
| Cancellation semantics weakened — SOURCE00:11–12 | Commit/completion window checks substantially improve cancellation. An inherited blocked mask still permits a signal during final settlement to escape persistent veto. The terminal boundary remains insufficiently specified. |

V4 correctly makes `qualified: true` a decision record rather than sole authority. `qualification_problems()` requires matching receipt, commit and completion hashes, no item veto, and a producing-run summary containing a matching COMPLETE entry with no stop, signal or run veto. `validate_controls()` consumes that predicate; science revalidates control identities before work and before native spawns. These are substantive repairs. **SOURCE02:691–740, 1517–1564, 2706–2716, 2882–2891.**

Receipt durability errors prevent eligibility. Commit publication errors prevent a successful completion digest. Completion errors produce CANCELLED/FAILED publication and a stopped run; an absent run summary also prevents admission. Consequently, an item-level cancellation-write failure has a useful independent fallback: its producing run cannot honestly report that item COMPLETE. **SOURCE02:564–636, 3001–3046.**

1. **MAJOR — the final run summary is admissible before its publication succeeds; failed veto creation can leave it permanently admissible.**

   [`SOURCE02:536–543`](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/n8-gb-staged-v4-delta-review-v1/snapshot/02-gb_staged_v4.py:536) exposes each record through `os.link()` **before** its final directory `fsync`/`F_FULLFSYNC` and close. The run summary uses that same publisher at **658**. Its serialized bytes already contain clean signal fields and COMPLETE item entries.

   A reader can therefore load a fully formed, apparently successful summary while the publisher is still syncing it, checking pending signals, restoring its mask or preparing a cancellation. Admission checks file contents and veto-name absence; it does not establish that summary publication has returned successfully or that the producer has finished settlement. **SOURCE02:655–681, 724–737.** This is an acceptance window for incomplete publication, even when a later veto eventually repairs subsequent reads.

   There is also a lasting failure schedule: the summary link succeeds; its final directory sync/full-sync/close fails; then cancellation creation fails before creating its directory entry—for example, because the same storage failure prevents `os.open(O_EXCL)`. The clean summary remains visible, with every matching control entry. The error and cancellation status are returned only in memory and printed. Nothing changes the summary’s admissible bytes, and no persistent fallback denies it. **SOURCE02:550–560, 662–681, 3092–3093.** With a successful final print, `cmd_run()` can return normally despite these errors.

   A post-link failure followed by **successful** veto creation rejects correctly. The blocker is the reader race and the failed-veto fallback. After the latter, future `qualification_problems()` and `validate_controls()` calls can admit all seven controls from that failed producing run. The plan’s assertion that a failed veto is rescued by the required run summary applies to item publication, but fails when the failure occurs while publishing that summary itself. **SOURCE06:31.**

2. **MAJOR — restoring an already-blocked mask can conceal a signal received during final settlement.**

   [`SOURCE02:652–681`](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/n8-gb-staged-v4-delta-review-v1/snapshot/02-gb_staged_v4.py:652) saves and restores the caller’s mask without refusing an inherited blocked SIGINT/SIGTERM. `_latched_after_unmask()` subsequently reads only the Python latch; it does not inspect pending signals. **SOURCE02:639–642.**

   A concrete static schedule is:

   - The incoming mask already blocks SIGTERM; no signal is initially pending.
   - Summary publication succeeds and the pending/latch sample at **659** is clean.
   - SIGTERM arrives after that sample but before mask restoration at **672**.
   - Restoring `old` leaves SIGTERM blocked. No handler delivery occurs; the latch read returns `None`.
   - The function returns without cancellation, leaving clean, admissible records.

   This needs one signal and no storage fault or unrelated thread. The signal arrives before the documented mask-restoration settlement completes. Treating it as outside cancellation would require an explicit contract change, which is not authorized.

   Ordinary restoration to an unblocked mask is covered by the supplied delivery checks. That does not establish correctness for an inherited blocked mask. Neither run startup nor the publisher establishes an unblocked-entry precondition. **SOURCE02:2866–2872, 652–681.**

The actual boundaries need explicit treatment. Item status becomes COMPLETE after the completion publisher and the latch check, but admission additionally depends on the later run summary. For readers, the effective acceptance boundary is currently the **summary link**, ahead of final durability and cancellation settlement. For the writer’s cancellation logic, the last observation is the latch read reached at **673**. A signal delivered after that read can merely update `stop`; the handler has no persistent veto action, and the remaining path prints and returns. **SOURCE02:2868–2869, 3092–3093, 3126–3127.**

This does **not** require cancellation forever after a genuinely completed run. It requires one precise, finite, contract-consistent terminal point covering preparation, serialization, publication, durability and settlement, with admission coordinated with that point. Adding another completion file using the same publish-then-veto pattern merely moves the exposed tail again. I have not accepted the early decision snapshot, last latch sample or summary link as an authorized replacement boundary. The stale commit `rule` still naming a “linearization point” and removed `publish_commit()` should also be corrected. **SOURCE02:3015–3018.**

Power-loss risk is broader than the documented creation-to-directory-sync interval. Cancellation serialization precedes exclusive creation; a crash can also occur after a clean summary becomes visible but before the veto is created. After creation, loss before successful directory durability can erase the veto while earlier clean evidence survives. **SOURCE02:546–560, 658–680; SOURCE06:57.** File hashes establish byte agreement, not successful publication or survival of an absent cancellation record.

The supplied result contains **85 check entries and 85 `ok: true` entries**, ending in PASS. Its runtime/selfcheck hashes match this snapshot. It explicitly identifies stub natives and fake lane helpers; these results are not native qualification. **SOURCE08:5–22, 889–890.**

Coverage now includes commit serialization, before/after commit linking, after completion linking, mask restoration, receipt fsync failure, post-link item directory/full-sync/close failures and interrupted completion. **SOURCE04:1455–1613.** However, H10f raises before the completion publisher executes; H12 injects a summary signal and allows veto creation to succeed. Missing cases include summary post-link durability failures, veto creation failure, concurrent admission during terminal publication, inherited blocked-mask restoration and the final shutdown boundary. **SOURCE04:1601–1636.** The retained **82/83** attempt is documented with hashes and the overbroad link-hook explanation; its failed result itself is not supplied here. **SOURCE01:27–35; SOURCE05:110–126.**

No regression was found in the previously closed operational mechanisms. Static comparison of the actual v3/v4 files leaves intact:

- Scalar FD acquisition rollback, exactly-once descriptor handoff, and feeder close-before-diagnostics cleanup. **SOURCE02:1568–1597, 1735–1750, 1930–1968.**
- Reaped-child ownership termination before diagnostics, owned-child-only signalling, and bounded cooperative cleanup. **SOURCE02:2039–2072, 2370–2425.**
- Independent native-failure/TIMEOUT/outcome/diagnostic vetoes, resource thresholds, scanner/exclusion latches and launch checks. **SOURCE02:2114–2225, 2600–2662.**
- Exact measured feeds, independent proof-buffer digest, actual collector EOF, proof-byte counts and narrow duplicate-line filtering. **SOURCE02:1604–1678, 1753–1898, 2483–2545.**

The extra-thread guard rejects unrelated Python threads conservatively at the decision; it does not authorize signalling them or synchronize external readers. **SOURCE02:580–582.** Control expectations remain consistent with the pinned C parser’s EOF counting, TIMEOUT/0, header-error/0 and diagnostic behavior. **SOURCE11:905, 983–994, 1064–1067, 1104–1115, 1265–1267.**

Seven native controls remain unestablished in the supplied freeze. GA exclusion remains mandatory: the frozen PRE-EXEC records GA driver **64001**, drat-trim **47633** and cadical **47634**; these are snapshot observations, not current host status. **SOURCE01:58–60; SOURCE07:492–570.**

Release requires repaired/refrozen source, an exact controls GO binding the resulting script and PRE-EXEC hashes and ordered seven controls, then independent audit of native receipts, commits, completions, successful terminal evidence and veto absence. Science subsequently needs separate exact-input GO within the unchanged twelve-direct/six-strengthened allowlist. **SOURCE02:187–191, 1491–1514; SOURCE06:59–125.** No native or science release is granted by this review.