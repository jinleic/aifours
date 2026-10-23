# PA19 rev11 re-review (reviewer task PA19StagedAudit, delivered 2026-10-17 ~16:00 PDT)

Parent transcription of the reviewer's delivered result (agent output; transcript `history://PA19StagedAudit`). Read-only review; no execution, process polling or file changes by the reviewer.

## Rev11 re-review: REJECT — keep GO gated

**Overall correctness: incorrect. Confidence: 0.98.** Proof replay and compressed-tail handling are substantially fixed, but resource ownership and admission controls still have blocking gaps. No false mathematical UNSAT acceptance or actual resource excursion was demonstrated by this read-only review.

### Remaining findings

1. **MAJOR / P1 — Freeze admissions before the watchdog's termination wait.** `rss_watchdog2.py:111–120` signals the selected runner and waits up to 60 seconds without first closing admissions. COUNT is reduced only afterward at lines 126–129, and never below one. A waiting runner can replace the terminated holder while lane RSS remains excessive. Stop admissions before signalling/waiting, retaining the paused state until recovery is established. Confidence 1.00.
2. **MAJOR / P1 — Remove the non-token-holder watchdog fallback.** `rss_watchdog2.py:102–106` still selects the largest runner group when no token holder is established. Runner discovery at lines 49–50 matches script names without requiring the lane path, so this fallback can terminate a matching runner unrelated to an owned token. Absence of a verified holder should pause/escalate, not select another process. Confidence 0.99.
3. **MAJOR / P1 — Recheck admission after waiting for `bigmem`.** `stream_check11.py:427–429` starts drat-trim immediately after acquiring the potentially blocking memory lock; the admission check is before that wait, at line 420. Check admission again inside the acquired lock, immediately before spawning. Confidence 1.00.
4. **MAJOR / P1 — Put SAT-verification helpers under token and child ownership.** `run_hard11.py:90–92` launches both SAT verifiers through bare `subprocess.run`, after `kissat_staged` has returned and released its token. With two replacement stages active, verification can add a fifth busy process; these children bypass `ACTIVE`/`SPAWNING`, so SIGTERM can exit the runner while leaving a verifier unmanaged. Confidence 0.99.

### Disposition of the six original findings

| Original finding | Rev11 assessment |
|---|---|
| Survivor token/bigmem release | Fixed for registered solver/checker children; quarantine waits occur inside the lock scopes. Extension helpers retain their token through `communicate`; SAT verifiers remain outside ownership as above. |
| Compression CPU accounting | Addressed conditionally by parent-enforced COUNT ≤ 2 (two busy processes per token). SAT helpers remain an exception. |
| Watchdog attribution/admission | Partially fixed: runner-plus-descendant RSS grouping is present; pre-wait admission freeze and safe target selection remain unresolved. |
| Post-wait STOP/disk checks | Partially fixed: CPU-token, construction, solver and extension checks are present; the `bigmem` wait remains uncovered. |
| Replay write/close failure | Fixed: delivered bytes are hashed after successful blocking writes; close errors, incomplete zstd frame, reader errors and unfinished feeding prevent certification. |
| Compressed flush cap | Fixed: final-frame bytes are checked before being appended. |

### Certification and evidence limits

- The normal native gate still requires solver exit 20, checker self-exit 0, exactly `["s VERIFIED"]` after carriage-return stripping, reader completion, successful replay/hash/length matching, and no abort/cap failure. No lrat-check acceptance path was found.
- `summarize9.py:50–53` and `list_pending2.py:23–25` consume revision 11 with the new reader/replay/admission predicates; split-index interpretation remains compatible.
- The successful-registration SIGTERM race is covered structurally by `SPAWNING`, registration and terminate-after-registration. Run 3's helper test occurs after startup; it is not a direct registration-race control.
- The saved run-3 receipt reports A–L passing, including quarantine, feed failure, post-token refusal and helper attribution. It does not establish pre-grace admission closure, fallback safety, post-`bigmem` refusal or SAT-helper ownership.
- RSS remains sampled, not an instantaneous bound. The disclosed smoke-output rewrites remain a separate preservation deviation.

## Parent disposition

Production admissions stay at COUNT 0. All four blockers were forwarded to InfoPacking19 for a newly frozen REV11a with focused controls (pre-grace no-admission, no-eligible-owner pause, post-`bigmem` STOP/floor refusal, SAT verifier token/SIGTERM ownership). The reviewer will re-review exactly those changes before any parent GO.

Time note (appended 2026-10-17 16:22:34 PDT, host clock): the '~' delivery time in the title is an estimate from the surrounding tool receipts, not a host-clock reading; the host-clock save time is this note's time or earlier.
