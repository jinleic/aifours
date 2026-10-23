# Parent release CP2 v4: rebuild-based endedness, census transactions, baseline witness (NOEXEC)

Actual `/bin/date` before this write: `2026-10-19T17:52:58-0700`.

| Artifact | SHA-256 |
|---|---|
| `RUN/control/parent_release_identity_v4.py` (105992 B, 1919 lines, ASCII) | `39c51017a6f01fad779d40c22ad0912cde2d0384e4ed7e7baad2206bc8e93d7c` |
| `RUN/review/parent_release_identity_v3_to_v4.diff` (exact, 18 edits of v3) | `a9c01e1247c21474bf7a8976566eb466b6ae16b3b0a3e7c498ca0142a73745f1` |
| `RUN/control/parent-release-cp2-design-freeze-v4.json` (frozen before code) | `72eb4720f5d21d77195aac9fe939f4c427656ad55a8815dc76d22dd5671b2805` |
| `RUN/review/parent-release-cp2-controls-v4.json` (62 union, 16 census, 28 endedness, 3 native) | `1ae171eda0068ba5746011d09bb75724605b2e5fad97d97cda74cd62bc5dee7d` |
| scope `RUN/control/parent-release-cp2-v4-repair-scope-v1.json` | `18fe620f22dae58ccd1c5007f9084a13ba19e77a2057ab689e2c7b0adb388175` |
| review `RUN/review/parent-release-cp2-v3-codex-v1.prompt.stdout.txt` (HOLD 0F/6M/3m) | `969e2fd23b48e3b0ffeb2274b750bc36d6d27f0a2b9b2816ea8dcf997a6a2a39` |
| v3 source (immutable) | `f21b4296ae52778fe31677f749a871d8982c31c6d5133609dc1d0b0e0fe58b38` |

Status: NOEXEC source candidate. It is unreviewed and unqualified, and I did not approve it myself. Nothing was imported, compiled, AST-parsed, tested or run. Verification was limited to exact-once text edits of v3, the unified diff, regex consistency checks (every `U_` cause has a prerequisite; every `E_`/`U_` cause used is declared) and a grep audit. The audit found no kill, killpg, posix_spawn, subprocess, fork, waitpid, open, write, exec, eval or `time.time` call, and every CDLL, dlsym, getpid, proc_pidinfo, proc_listallpids, sleep and monotonic call goes through `_native`.

## Repair map

- **M1 (load-bearing rebuild).** The new signature is `evaluate_endedness(request, read_bytes, census_log, identities, deadline_check)`, and it never takes a union. It rebuilds the union from the frozen parent-captured histories with `_build_union`, the same builder `build_identity_union` wraps. ENDED requires all of the following:
  - the rebuilt state is `CLOSED_CONDITIONAL` with no causes, else `E_UNION_HELD`;
  - the rebuilt report lists no unknown incarnation, else `E_UNION_UNKNOWN` (defensive; the sticky rule already prevents it);
  - `identities` (PRT `spec.identities`) typed-equals the rebuilt `prt_identities`, else `E_IDENTITIES_MISMATCH`.

  Version, freeze, producer and digest fields are outputs only; none is an input. The result echoes the rebuilt `union_sha256`. `spec_identities_match`, `_union_version` and `_v_union` are removed.
- **M2 (census transactions).** `make_census` issues a `CensusLog` handle; its state lives in a module-private weakref registry. Each census call journals immutable canonical byte entries with `seq` numbers (`attempt_start`, `attempt_end`, `served`, `refusal`), chained by SHA-256. A factory serves one census call; a second call is refused. Evaluation, with causes:
  - `E_CENSUS_LOG_FOREIGN`: the handle is not a registered `CensusLog`.
  - `E_CENSUS_TRANSACTION`: the transaction is sealed first, then requires no call in flight and calls=1, served=1, refusals=0. A second evaluation is refused.
  - `E_CENSUS_EVIDENCE_INVALID`: re-validation fails. It covers the chain, entry order and canonical form, key sets, attempt sequence and statuses, listed = identified + missing, the missing sample, per-row and rows digests, observer pid = factory pid, the observer bracket and completeness flags recomputed from retained rows, finite `observed_at_mono`, and the digest of the served dict rebuilt from rows.

  Processes are evaluated only after all of this passes. **Boundary (parent clarification):** this prevents accidental fabrication and cross-transaction substitution. It is not cryptographic protection against an adversarial same-process caller. The `PARENT_CODE_PROVENANCE` condition says so in every report, and control E22 names the residual.
- **M3 (prespawn baseline witness).**
  - `_baseline_scan` reads only recorded sv19 evidence. The leading `observation_attempts` of kind `identity_scan`, phase `ADMISSION`, `inside_helper` false are the `establish_baseline` loop; there must be 1 to 3 of them. Each is not aborted, has no error and has a finite, ordered window. Every one but the last has a coverage stamp inside its window; the last has none.
  - **Equality compared:** the recorded `baseline_uniqueids` must equal the set of uniqueids whose raw tape observations lie inside the last scan window. There must be exactly one unflagged observation per uid, `identified_count` must match, and no observation may straddle the window.
  - For an ACK, the receipt baseline refs must lie inside that window and `mono_complete` must be at or after its end.
  - `_baseline_chronology` (`U_BASELINE_CHRONOLOGY`) needs, for every helper, a recorded `mono_spawn` after baseline completion. The main child needs the receipt's recorded `mono_spawn` after completion. No spawned identity may be a baseline uid. **No time is inferred.** Refusal histories with a main child record no main spawn time, so they stay HELD (control C02b).
- **M4.** `_native` checks the ORIGINAL deadline before and after each native acquisition. On failure the completion check still runs; a failing check raises with the primary as `__context__`, else the primary is re-raised. `_Io.read` runs its completion tick on the `read_bytes` BaseException branch too.
- **M5.** The endedness final check runs after the full result is assembled and hashed. On failure it fires `E_DEADLINE` and reassembles a HELD result with no further callback. A deadline crossing seen during the rebuild stops all later callbacks.
- **M6.** Assembly and hashing run inside an Exception boundary. The fallback is a minimal HELD result built only from constants, cause names, a hex digest and counters. BaseException keeps `parent_release_endedness_partial`.
- **m7.** `_sticky` never raises. It adds a sticky detail for:
  - a `raw_acquisitions` that is not a list of dicts;
  - a halted history or any overflow;
  - a non-dict overflow, or an overflow observation without an identity dict;
  - an unenumerable coverage history or helper report;
  - every gap, identity-less helper and identity-less main child.
- **m8.** Each attempt journals `attempt_start` before acquiring, then exactly one `attempt_end` on every exit: COMPLETE, INCOMPLETE, or ABORTED with identified count, partial rows digest, missing sample, last pid and error type. Every exceptional census exit journals a `refusal`.
- **m9.** C36 is split into C36a [U_FAMILY_INVALID] and C36b [U_FAMILY_INVALID, U_ROW_CONFLICT]. N01 now has exact causes [E_UNION_HELD, E_MEMBER_ALIVE, E_GROUP_NONEMPTY].

## Why naturally ended pre-existing processes are never reclassified

The baseline set is fixed by the prespawn scan, and equality is checked there, not at the last census.
- **A baseline process that exits during the run** stays a baseline identity. It never becomes a member, so its pid and pgid never become historical member pids or pgids. The H7 last-census rule stays inside(L) subset-of baseline with exact cardinality, so its absence is neither an error nor a reclassification (control C60).
- **A process born later** cannot enter the set, because the set must equal the scan window and every recorded spawn follows the scan. Requiring L to equal the baseline would turn every natural exit into a HOLD without blocking inflation (inflation is control C50).
- **An unrelated process started later and alive at L** has a non-baseline uid and HOLDs (U_LAST_CENSUS_OPEN). It is never silently treated as baseline.

## CP1 interface (sent to ParentCallerCP1)

These are unchanged:
- `build_identity_union(request, read_bytes, deadline_check)`. The union keeps its format, keys and states. Its module is `parent_release_identity_v4.py`, its design freeze `72eb4720f5d21d77195aac9fe939f4c427656ad55a8815dc76d22dd5671b2805`, its scheme `sv19-incarnation-v1` and its producer `cb828a78...`; these are consistency fields only.
- `make_census(deadline_check)` and `log.served_count()`.

What changes for CP1:
- The identity dict becomes `{union, request, census_log, evaluate_endedness}`, and every transaction uses a new `make_census`.
- Endedness result keys are `format`, `state`, `causes`, `endedness_sha256` and `union_sha256` (the rebuilt digest), plus `module`, `scheme`, `design_freeze_sha256`, `producer_sha256`, `union_state`, `union_causes`, `identities_match`, `census`, `deadline_crossed`, `callbacks`, `conditions` and `boundary`.

## Residuals and availability

- **SR-4 and SR-5 (recorded MINOR, outside scope).** SR-4: a dependent `U_ROW_CONFLICT` fires when member assembly is blocked. SR-5: the union report has no structured request binding; the rebuild compensates inside CP2.
- **Uncaught MemoryError.** An Exception raised while serializing the constants-only M6 fallback is not caught. Only MemoryError is plausible there.
- **Fewer runs can be released.** Every coverage gap, unenumerable source, refusal with a main child, or post-baseline process alive at the last census is HELD. A release-eligible run needs a quiescent host and an ACK history. Not weakened.
- **External conditions.** These remain in every report: parent observation authenticity, parent code provenance, direct launch, supervisor19 qualification, non-descendant creation channels, publication freeze and the CP1 join.
