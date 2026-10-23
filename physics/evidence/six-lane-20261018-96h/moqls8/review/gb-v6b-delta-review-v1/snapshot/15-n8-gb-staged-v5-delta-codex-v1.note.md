**NO-GO for the native control run as currently documented.** The v5 runtime substantially repairs both v4 MAJORs, but the launch commands can report a successful tool invocation after a failing driver. Correct that status handoff before running controls.

All nine supplied SHA256 hashes and byte counts match. Review used static reads and hashing exclusively inside the snapshot. No interpreter, tests, writes, network, delegation or external paths were used.

No separate BLOCKER finding; **one MAJOR and two MINOR findings** follow.

1. **MAJOR — the control-plan shell commands swallow the driver’s exit status.** Both commands end with `; echo "driver exit status $?"`. The printed number reflects the preceding command, but the enclosing shell normally returns the successful `echo` status, **0**. Consequently, the parent’s tool can report success after driver exit 3/4/5 or signal death. This contradicts the stated purpose of foreground execution and weakens the critical requirement that the parent independently observe the driver’s successful termination. **SOURCE08:110–117, 148–150; SOURCE08:67–78.**

   The dangerous schedule remains relevant: summary publication fails after linking, veto creation fails, and the driver correctly returns 3; the wrapper nevertheless returns 0. A parent relying on the tool’s status could write an apparently valid release despite the runtime repair.

   **Repair:** propagate the captured status. After the existing launch command, replace the trailing `echo` with, for example, `driver_rc=$?; printf 'driver exit status %s\n' "$driver_rc"; exit "$driver_rc"`. Prefer a dedicated parent tool invocation whose returned status belongs directly to the driver. Preserve failures of `cd`, redirection and setup as well. Update both commands and refreeze the changed plan and its manifest references.

2. **MINOR — release pathname validation and opening are separate operations.** `release_problems()` checks `realpath`, `islink` and `isfile`, then calls ordinary `read_bytes()`, whose `open()` follows symlinks. A concurrent replacement between validation and opening could redirect the read to producer-controlled bytes while retaining the earlier successful pathname checks. **SOURCE01:514–516, 777–785.**

   This requires a modifier of the parent namespace; the prescribed exclusive, immutable parent publication does not itself introduce that schedule. Nevertheless, the strongest unconditional “symlinked releases are refused” claim exceeds this implementation.

   **Repair:** open the expected basename relative to a trusted review-directory descriptor with `O_NOFOLLOW`, verify the opened descriptor is regular using `fstat`, and parse/hash bytes from that descriptor.

3. **MINOR — selfcheck descriptions overstate some coverage.** H14 invokes the reader synchronously inside a publication wrapper after `real()` returns. It tests useful deterministic interleavings, but no independently concurrent reader or read between summary linking and directory sync. H2 checks that release hashes are present; it does not mutate a release and demonstrate rejection at science launch. H17 omits exit-5 cases and the deferred-handler handoff around blocking/default-disposition installation. **SOURCE03:1337–1345, 1708–1715, 1831–1856, 1865–1888.**

   **Repair:** describe the current coverage precisely and add a reader paused after summary linking, release-hash mutation checks, and child cases for flush failure and terminal thread/mask failures. These additions should retain the stub-only boundary.

For **(a), admission**, the required external-file gate is present. `qualification_problems()` first checks the receipt/commit/completion chain, item cancellation absence, producing-run summary, run cancellation absence, and matching COMPLETE summary entry. It then unconditionally incorporates `release_problems()` failures. Producer completion and summary bytes alone therefore cannot qualify a receipt. **SOURCE01:807–863.**

The release filename is derived from a strictly validated `YYYYMMDDTHHMMSS` run tag. An absent release fails; a stable symlink, nonregular object, file inside the desk, or file whose resolved parent differs from resolved `review/` fails. Unreadable JSON and non-object JSON fail. This establishes the requested location checks subject to finding 2’s replacement race. **SOURCE01:766–790.**

The required values are checked against:

- Schema `moqls8-gb-staged-parent-release/5`, status `PARENT_RELEASE`, the exact desk, and scope derived from the item kind.
- This script’s SHA256, the receipt’s PRE-EXEC SHA256, run tag, and current run-summary SHA256.
- `owned_children_after_exit == []`, `stop_or_signal_observed == null`, and `raw_audit == "PASS"`.
- A receipt-map entry containing this label’s exact receipt SHA256.
- **Strict integer zero** for `driver_exit_code`; JSON `true` is rejected because the check uses `type(exit_code) is int`. **SOURCE01:261–262, 791–804.**

Missing required fields fail, including the explicitly null field. These are exact required-value checks; the code does not reject additional metadata keys.

The release’s raw-byte SHA256 enters `validate_controls()` output and the science PRE-EXEC admission identity. Science run entry compares that hash again, and `identity_check()` revalidates controls and compares release hashes before both native stages. Changing an otherwise valid release’s bytes therefore changes the admission identity. **SOURCE01:1682–1687, 2916–2935, 3010–3018, 2830–2841, 2383–2385, 2443–2447.**

Parent authorship remains the protocol’s trust root: the validator cannot distinguish a fully matching false attestation from a truthful parent attestation merely by inspecting JSON. The implemented producer has no release-writing path, and the plan reserves creation for the parent after independent observation and audit. H14’s “forgeries” are malformed or mismatched attestations, rather than authenticated-author tests. **SOURCE01:766–804; SOURCE03:1724–1751; SOURCE08:67–78.**

For **(b), failure exits**, the v4 failed-veto schedule is repaired in the runtime. A post-link summary-sync exception populates `errors` and establishes a cancellation reason; failed veto creation adds another error. The final clean predicate requires a non-null summary digest, no errors, no cancellation, no stopped reason and no latched signal. That schedule cannot select zero. **SOURCE01:720–756, 3225–3233.**

Item cancellation, receipt durability failure, publication errors, child-settlement failures, signals, exceptions, spawn failures and failed safety predicates establish stopped reasons and terminate further work. **SOURCE01:3173–3212.** H15 specifically injects the second summary-directory sync failure and veto-creation ENOSPC; the recorded result is exit **3**, with the clean-looking summary still visible and no veto. Its release recording exit 3 is refused. **SOURCE03:1770–1805; SOURCE04:934–939.** Finding 1 concerns preserving this correct runtime result through the parent launcher.

For **(c), inherited masks**, `refuse_inherited_mask()` is the first operation in `cmd_run()`, preceding environment changes, reads, log creation and spawning. `pthread_sigmask(SIG_UNBLOCK, [])` queries the existing mask without changing its membership. Either blocked SIGTERM or blocked SIGINT triggers `die()`. **SOURCE01:686–693, 2960–2987.** H13 calls the actual entry path for each signal and checks refusal, retained masking and unchanged log inventory. **SOURCE03:1371–1386.** The shell’s console redirection is external to this driver-entry guarantee.

For **(d), terminal signals**, I find no lost-signal/exit-zero window in the intended standalone, settled, single-threaded CPython path.

During flushing, the latching handlers remain installed; flush exceptions convert a proposed zero into 5. The subsequent `pthread_sigmask(SIG_BLOCK, ...)` blocks both signals before either disposition changes. The delicate Python-deferral point matters: CPython’s wrapper processes already-tripped Python handlers before returning. A signal already delivered to the C handler may no longer appear in `sigpending()`; the latch supplies that evidence. A generic Python call boundary alone would not establish this guarantee. **SOURCE01:696–713.**

Once blocked, signals arriving between either `SIG_DFL` installation and the latch/pending checks remain pending. A signal arriving after the final sample is still pending when both signals are unblocked, at which point the default action terminates the process. Signals delivered after unblocking terminate directly, including the interval before `os._exit()`. Thread-count and saved-mask anomalies convert a proposed zero into 5. **SOURCE01:709–717.**

The clean path also requires finished workers, a stopped scanner and reaped children; failed settlement establishes a stopped run. Thus the reasoning does not rely solely on the terminal thread-count snapshot. **SOURCE01:2529–2549, 2658–2667, 3194–3199.**

For **(e), exit codes**, the implemented meanings are:

| Status | Meaning |
|---|---|
| 0 | Clean run surviving the terminal checks |
| 3 | Stopped run, publication error or cancellation without an already-latched signal |
| 4 | Latched signal selects failure |
| 5 | Terminal failure converts an otherwise-zero status |
| 143 / 130 | Shell representation of SIGTERM / SIGINT termination |

An existing nonzero code is retained by `code or ...`; the labels are not mutually exclusive precedence guarantees. Entry refusal ordinarily exits 1 through `die()`. H17’s refusal status 7 is deliberately chosen by its harness. **SOURCE01:490–491, 704–717, 3228–3233; SOURCE03:1848–1866.**

For **(f)**, SOURCE00’s 25 hunks show the stated release, signal, exit-status, naming/schema/pin and stale-rule repairs. I found no unrelated executable change in that diff. Full v4 source is absent, so unchanged regions cannot be independently reconstructed against v4 here. H1/H2 exercise release-gated stub admission; H13–H17 cover the paths described above. The supplied report contains 90 successful checks, but **native behavior remains unestablished**. **SOURCE00:11–415; SOURCE04:22, 997–998.**

For **(g)**, the GO and release templates otherwise match runtime fields, hashes and ordered controls. Release requires observed termination, survivor checks, raw audit and veto absence; science remains separately gated. **SOURCE08:41–78, 91–107, 120–127, 142–154; SOURCE01:1628–1636.** Correct the MAJOR status-propagation defect before the native control run.