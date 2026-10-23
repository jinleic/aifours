# Parent release CP1 caller v3 — source-only integration plan v3 (PLAN ONLY, NOEXEC)

Actual `/bin/date` before this write: `2026-10-19T21:38:46-0700`.

This plan **supersedes plan v2** (`RUN/control/parent-release-cp1-v3-integration-plan-v2.md` `933228b46c7cb2dc5872968383e5a82a39644b8193c40cdcfedef0ff1b1ee1bd`) together with the amendments recorded in CP1 checkpoints 010–019 (`2e0093b8…`, `0e0ec8bf…`, `f77917e7…`, `d2d762c3…`, `35a9f09d…`, `03f5c3db…`, `0b04f950…`, `a2716c2d…`, `1b857a89…`, `334c9c00…`). Plan v2 and every checkpoint stay immutable. It covers exactly ONE caller successor, `RUN/control/parent_release_caller_v3.py`. **No successor source has been written.**

CP1 v2 `9f3d158bd80a31d6ce2d964e216244d5095eb9422782bc448dc3a671d81e4cb4` and v1 `4072c50ef5be021a22e72a43571550c1338ab8a4d243752d88e3b7cc71a75cae` stay immutable. Neither may be invoked or receive attestations, because both pin PRT v3 (HOLD).

Governing parent decisions:
- `RUN/control/parent-release-cp1-v3-integration-decisions-v1.json` `887016938b8ab84b7e6770e8bd8dec0ea3d0a8af9a273b3871df55f19b8a8e86`: D1, D2, D3, D4, D6 and D7 YES; D5 and D7b NO; strict G1/G2.
- `RUN/control/parent-release-cp1-D8-consumed-snapshot-join-decision-v1.json` `79540a182203d805077c445e12283070dcebe52ce3c0b545bb94f5485dd177a2`: D8 approved and required.
- `RUN/control/parent-release-cp1-D8-copy-caps-decision-v1.json` `ae43b4f9da523de1b71acbc5254eec774e45cc8a577626508255df439abb5d8e`: conservative CP2-format caps.
- `RUN/control/parent-release-v6-known-limit-disposition-v1.json` `f4ba9427c41243d3f049762e287a0e8d3d6e846db84d0762e0c5814df5c964fa`: known-limit gate.

**No import, compile, AST, exec, test, probe or model CLI** was used. Only reading, `shasum`/`wc`, arithmetic on synthetic JSON lengths, IRC and this exclusive write. Global HOLD is unchanged; nothing was repinned.

## 0. Gates and pin policy

- **G1/G2 (strict).** CP1 v3 source is written only after BOTH the PRT source and the CP2 source it will pin have frozen non-HOLD parent source dispositions.
- **Known-limit gate (`f4ba9427…`).** No v6 non-HOLD disposition and no CP1 repin until one of two things holds:
  - (a) preferred: a PRT successor ensures no authoritative RELEASED record can exist without an exact matching returned or attached result, or an explicit durable failure/invalidator;
  - (b) independent review establishes that every consumer requires the exact returned result and treats a bare journal line as non-authoritative, with that contract frozen in CP1 and the registry.

  §1 freezes the CP1 side of (b). It is required under (a) as well.
- **Expected v7.** The parent plans one joined v7 scope after both v6 reviews. Every pin-dependent value below is therefore **taken from whichever PRT and CP2 sources receive non-HOLD dispositions**. The v6 values are recorded as candidates and were checked against the interface. If later sources are accepted instead, their values are verified the same way and recorded in the replacement-list checkpoint. This plan is not edited for a re-pin; only a material interface change needs a new plan version.
- **After G1/G2:**
  1. Freeze an exact-once, function-level replacement list against CP1 v2 bytes `9f3d158b…` in a new CP1 checkpoint.
  2. Write, all mode `x`: the v3 source, the exact v2→v3 diff, notes v3, disposition v3 and a final checkpoint.
  3. Park.

  No runtime pin migration happens before acceptance.

## 1. Journal-authority contract (frozen for CP1 and its consumer)

**J1 — Only release evidence.** The only release evidence is a result that meets all of these:
- returned normally (not raised) by the pinned PRT entry, inside the current `invoke_release` call;
- detached by CP1's own bounded copy;
- satisfying CP1's complete RELEASED predicate (`_not_released`, carried forward with the current formats).

Results attached to raised exceptions are never release evidence. PRT always builds them HELD, and CP1 reads them only for resource accounting.

**J2 — Exact join to disk.** All of these must hold before any receipt:
- (a) **Disposition.** It is re-read through the original reader at exactly `commit_dir/<prefix><slug>-<sha256>.json`. Its bytes and SHA equal the returned `disposition.sha256`/`bytes`, and the reader-observed inode equals the returned identity. The document is RELEASED for this item and carries CP1's spec digest.
- (b) **Registry.** It is re-read. Exactly one line has a SHA-256 (LF excluded) equal to the returned `registry.line_sha256`, and it comes after the unique allocation line. That line is a current-format RELEASED row bound to that disposition path and SHA, the allocation, the reservation and `recorded_at`, with `remaining_output_reservation_bytes: 0`.
- (c) **Other rows.** Every other same-item row after the allocation line is an earlier current-format HELD row for the same allocation.

**J3 — Bare journal data is never authority.** None of the following authorizes a release by itself, whatever its syntax, `state`, `remaining_output_reservation_bytes` or presence: a registry line, a disposition file, an exception-attached report, a CP2 report, a caller receipt or a parent document. CP1 never searches the journal for a RELEASED line, never adopts one and never infers a release from one.

**J4 — Stray RELEASED lines block; they never release.** Take a RELEASED line not produced and fully observed by the current invocation. Examples are the v6 known limit (`decide_and_commit` can raise an ordinary exception at line 1818 after the line was appended) or a foreign writer. Such a line makes every later release of that allocation HELD, in two independent places:
- PRT fires `P1_ALLOCATION_NOT_CURRENT` (v6 `_allocation` 870–898, `_held_for` 865–867);
- CP1's registry readback refuses under J2(c) with `CP1_REGISTRY_READBACK`.

Recovery needs a separately authorized parent procedure. CP1 never repairs, removes or reinterprets journal bytes.

**J5 — After a PRT exception (ordinary or not).**
- The result is HELD, with no CP2 evaluation, readback or receipt.
- The report is read only from the identical propagated object, through the base instance dict. Prior-tuple members can carry superseded attachments and are never consulted.
- A missing report adds a permanent in-process "PRT resource state unknown" entry to the global ledger.
- The outcome's uncertainty text states that a partial or complete disposition and a RELEASED registry line may exist. Such bytes are non-authoritative and block later releases of the allocation (J4).

**J6 — Consumer.** `ReservationAccount.release` accounts only the identical minted effective `CallerOutcome`, plus a fresh receipt readback under the outcome's original deadline. No API accepts registry lines, dispositions, receipts, result dicts, reports or digests. After a process restart nothing can be accounted.

**J7 — Receipt binding.** The receipt records:
- the returned-result digest;
- disposition path, SHA, bytes, inode and `recorded_at`;
- registry path, plus the observed registry bytes and SHA;
- the allocation line index, and the returned line's index and SHA.

A later reader can therefore tell which journal line CP1 joined. The receipt itself is not authority (J3).

**J8 — Scope.** This contract binds CP1 code and CP1's own consumer only. Every other consumer of the registry or dispositions (scheduler, admission, audit tooling) must adopt J1–J4 independently. CP1 cannot verify that, so it stays a named external prerequisite. PRT's `release_effect` text in every disposition and row states the same non-authority.

**Status in CP1 v2.** J1–J3 and J5–J7 are already implemented, in `_result`, `_not_released`, `_disposition`, `_registry`, `_attached`, `_notes` and `ReservationAccount`. v3 adds the current formats, the explicit J4/J5 uncertainty text and the base-dict read in J5.

## 2. Dependency pins (candidates; hashes read 21:29–21:37)

| Role | Object | SHA256 | Status |
|---|---|---|---|
| PRT candidate | `control/parent_release_v6.py` | `65eef494580b81adcd6e80eda54c26c368f3b009c435c9941b3d9cdd0bc01e69` (88789 B, 1864 lines) | Source-only; Codex review in flight; known-limit gate open |
| PRT v6 notes | `control/parent-release-v6-design-notes.md` | `e56f1a66c526eddf38ebc9cdaa3cfc12ec5f570a2076e5774aee8237ad5c2c04` | — |
| PRT v5→v6 diff | `review/parent_release_v5_to_v6.diff` | `3153a21834aa862a772a5c0d5cd97a8bc3e325693ec0965af724e4828dc2d8b9` (268 lines) | Read in full |
| PRT owner addendum | `review/parent-release-checkpoint-016-v1.json` | `dc3f41d94c2cd84de98b3e858cfc218d7dc48d90a1b5c5e4c0199ac45eae9672` | Known-limit facts |
| CP2 candidate | `control/parent_release_identity_v6.py` | `a9b82a48548257782871404ed366ca2719abc2b081efa452c7e3907c0aecff5b` (123255 B, 2316 lines) | Source-only; Codex reviews A/B/C in flight (stdout empty at 21:33) |
| CP2 design freeze v6 | `control/parent-release-cp2-design-freeze-v6.json` | `2135fc82e5acc80ae1122badcccd40e441824018190fca07d9158d777a266bf2` | Equals `DESIGN_FREEZE_SHA256` (v6 l.65) |
| CP2 v6 notes | `control/parent-release-cp2-design-notes-v6.md` | `d44bfd3f3feef52ac1b22697793c836d5b073f319aa2b2cbe82cc30e941515e8` | — |
| CP2 v5→v6 diff | `review/parent_release_identity_v5_to_v6.diff` | `eeb6f1789029bf8cfafdbdd10b0a6f4db89c3e4c3164168479a45cb790892874` (63 lines) | Read in full |
| Reader | `control/beta_parent_reader_v1.py` | `1fc8f00c08cd9f78885c9a38fa0797ce5b01aba8e8ad39a6d19d7b6ce3370ec6` | Unchanged |

**Forbidden PRT digests:**
- v1 `6bc92891…`, v2 `addcdf4c…`, v3 `161ae04c…`, v4 `4c4a84f0…`, v5 `82feb74c…`;
- v6 `65eef494…` too, if it is superseded.

**Forbidden CP2 versions:** v1–v5 modules, and v6 if it is superseded. CP1 refuses them through the caller-side version check (§4). CP1 never loads CP2 bytes.

## 3. PRT interface for CP1 (verified against v6: full v5→v6 diff plus the CP1-relevant regions)

- **Entry:** `decide_and_commit(spec, read_bytes, census, owned_date, commit_dir, deadline_check)`, unchanged since v2.
- **Values (v6 candidate):**
  - module `parent_release_v6.py`;
  - formats `parent-release-result-v6`, `parent-release-disposition-v6` and `parent-release-registry-v6`;
  - file prefix `prt-v6-`;
  - `repair_scope_sha256s` = [`2fdf13b4…`, `1f9befdb…`, `32d161b0…`, `ef0ab41a…`, `b08a12dd36d52a020a3927e64d28d483886505b4d02df4407142aaae3393e27e`];
  - contract `4d122872…`, unchanged.
- **Unchanged, re-verified for whichever pin passes G1:**
  - the 22 result keys;
  - the disposition (10), registry (7, plus optional `path`/`detail`), resources (5) and registry-row (13) key sets;
  - ack ∈ {`ACK_NOT_ATTEMPTED`, `ACK_ATTEMPTED`, `ACK_FAILED`, `ACK_UNPROVED_DEADLINE`, `ACK_OK`};
  - registry status ∈ {`NOT_ATTEMPTED`, `ATTEMPTED`, `APPENDED`, `DEADLINE_CROSSED`, `FAILED`};
  - `final_deadline_check` ∈ {`PASSED`, `CROSSED`, `NOT_PERFORMED_ALREADY_CROSSED`, `BASE_EXCEPTION`, `NOT_PERFORMED`};
  - effective release = `state:'RELEASED'` ∧ `final_deadline_check:'PASSED'` (v6 `_final` 1686–1703 also requires no retained BaseException);
  - pure-JSON `parent_release_result`.
- **Attachment.**
  - Writes go through `_EXC_DICT = BaseException.__dict__['__dict__']` plus `dict.__setitem__`. `parent_release_prior_exceptions` is written before `parent_release_result`, in at most 8 rounds.
  - The propagated object is the newest actual origin: `keep(exc, origin)`, `latest_base` and `base_revision` (307–324, 1745–1774).
  - The prior tuple holds the original objects in first-retention order, excluding the propagated one.
- **Census consumption** (`_take_census`, v6 1094–): exact keys {`complete`, `processes`, `observed_at_mono`}; at most 200000 rows; row keys {`pid`, `ppid`, `pgid`, `uid`, `start_fingerprint`}; nonnegative ints; text fingerprint; unique pids. A non-finite float gives `P4_CENSUS_STALE`.
- **Known limit (J4/J5):** ordinary escapes at 1794, 1818 and 1828. Open and parent-known.

## 4. CP2 interface for CP1 (verified against v6 source)

- **`make_census(deadline_check) -> (census, log)`** (969–1036). The pair starts unbound and allows one call. A census call while unbound refuses and poisons. Fields come from native u32 (`pid`, `ppid`, `pgid`, `uid`=`euid`; 756–762), u64 `uniqueid` and i32 `idversion` (751–753).
- **`log.bind(release_token)`** (861–876):
  - requires an exact lowercase hex64 token and is one-shot;
  - is refused if the log is already bound, sealed, poisoned, active or called, if the token was reused in the module instance, or once 4096 tokens have been bound;
  - a refusal poisons the log; success returns `True`.
- **Log methods:**
  - `log.served_count()`;
  - `log.served_sha256()`: SHA-256 of `_canonical(exact served dict)`, set at journaling (836–837);
  - `log.exceptions()`: at most 32 objects, plus overflow;
  - `log.summary()`.
- **`build_identity_union(request, read_bytes, deadline_check, retain)`** (1988–1995). An exact list is required, otherwise `U_CALLBACKS_INVALID`. The parent calls it before `invoke_release` and keeps its own list (D5 NO).
- **`evaluate_endedness(request, read_bytes, census, census_log, identities, deadline_check, release_token, retain)`** (2278–2316):
  - Binding (`_bound` 2007–2012): the token must be equal, `census` must be the identical inner callable issued with the log, and `deadline_check` the identical original predicate. A mismatch gives `E_CENSUS_BINDING` without sealing.
  - Seal (`_seal` 2015–2023): requires calls=1, served=1, refusals=0.
  - It rebuilds the union, preflights the identities and never raises Exception.
  - It returns a normal dict, a MINIMAL dict or a PREBUILT `MappingProxyType`.
- **Version values (v6 candidate):**
  - module `parent_release_identity_v6.py` (l.71);
  - design freeze `2135fc82…` (l.65);
  - scheme `sv19-incarnation-v1` (l.72);
  - producer `cb828a78367dc2023bfc6e330696745f186f186811752361472747e5fe547e93` (l.69).

  All four are present in normal, MINIMAL and PREBUILT union and endedness reports.
- **Union keys CP1 uses:** `format`, the four version fields, `item`, `state`, `emergency`, `causes`, `union_sha256`, `prt_identities`.
- **Endedness keys CP1 uses:**
  - the four version fields, plus `state`, `emergency`, `release_token`, `causes`, `union_sha256`, `union_state`, `union_causes`, `identities_match`, `census`, `retained`, `retention_failed`, `deadline_crossed`, `endedness_sha256`;
  - census view (`_census_view` 2118–2125): `calls`, `served`, `refusals`, `release_token`, `poisoned`, `reentries`, `post_seal_refusals`, `retention_failed`, `complete`, `observer_ok`, `served_sha256`.
- **Request:** format `parent-release-identity-request-v1`; keys `format`/`item`/`histories`; history keys `family`/`producer`/`wait_record`/`launch_record`/`stdout`/`receipt`/`settlement` (unchanged).
- **Precedence** (v6 `_native` delta): a non-Exception primary outranks an ordinary completion secondary. This agrees with CP1 S2 (§7).

## 5. Census snapshot join (D8) — frozen encoding and caps

1. **Roles.** A per-invocation CP1 wrapper `W` is passed to PRT as `census`. The parent's inner census `C` (from `make_census`) goes to `evaluate_endedness`, never `W`.
2. **One call.** `W()` works on the first call only. A second call raises a CP1 refusal and latches the invocation nonpositive. `W` calls `C` exactly once (CP2 checks the original deadline at census start). It then calls the identical original `deadline_check` **before** the copy and **again after** the hash, immediately before returning the copy. A crossing or a non-None return refuses; there is no renewal.
3. **Accepted shape and caps** (copy-caps decision):
   - exact dict with keys {`complete`, `processes`, `observed_at_mono`};
   - `complete` exact `bool`;
   - `observed_at_mono` exact finite `float`;
   - `processes` exact list of 0..200000 rows;
   - each row an exact dict with keys {`pid`, `ppid`, `pgid`, `uid`, `start_fingerprint`};
   - four exact ints in 0..4294967295 (bool refused);
   - `start_fingerprint` exact `str` of 1..64 characters, all in `[A-Za-z0-9:-]`.

   **Verified against the CP2 v6 producer.** Rows are built at 1013–1016 from u32 native fields. The fingerprint comes from `start_fingerprint` (453–456): at most 63 characters over `[a-z0-9:-]`. `observed_at_mono` comes from `time.monotonic`, finite-checked at 1009–1011. The u32 cap therefore matches the producer, as the copy-caps decision requires.
4. **Copy.** An iterative bounded walk with exact type checks only (no `isinstance`, no user hooks). It builds fresh containers and reuses immutable scalars. CP1 keeps only the digest, the byte count and the row count, never the snapshot.
5. **Encoding.**
   - `_canonical` = `json.dumps(sort_keys=True, ensure_ascii=True, allow_nan=False, separators=(',', ':')) + LF`, as ASCII. It is textually identical in CP1 v2 (264–266), PRT v6 and CP2 v6 (422–424).
   - `consumed_sha256` = SHA-256 of those bytes.
   - Hard cap: 33,554,432 bytes.
   - Author arithmetic bound: 31,800,077 bytes (rows ≤158 B, envelope ≤78 B including the LF and a ≤24-character float repr, 199,999 commas). This is not a reviewed theorem. The cap is a safety cap, not a claim that every PRT-acceptable census fits.
6. **Failure.**
   - Any shape, cap, encoding, hash or deadline failure raises a CP1 refusal (an ordinary exception) to PRT and is recorded in CP1 evidence. PRT then fires `P4_CENSUS_FAILED`, giving HELD.
   - Nothing is ever truncated, filtered, shrunk or replaced with an empty fallback.
   - A non-Exception BaseException from `C`, the copy, the hash or the deadline predicate is kept by CP1 at encounter, as an origin, and re-raised bare. PRT handles it under its own rules, and CP1 selects at its boundary (§7).
7. **Post-RELEASED join.**
   - `W` was called exactly once, with no violation.
   - `log.served_count() == 1`.
   - `log.served_sha256() == consumed_sha256`.
   - The endedness `census.served_sha256 == consumed_sha256`.
   - The receipt records both digests.
   - Any mismatch gives `CP1_ENDEDNESS`.
8. **Supplements, not replaces, the binding:** the nonce bind, the identical inner `C` and the identical original deadline.

## 6. CP1 v3 change units against v2 (each becomes one or more exact-once replacements)

- **U1 — Version-neutral identifiers (D6).**
  - `PRT3_*` becomes `PRT_*`; the `'prt3'` ledger labels and "PRT3" texts become PRT.
  - The exec namespace name becomes neutral.
  - No aliases.
- **U2 — PRT pin values (§3).** Forbidden list as in §2. `ACK_STATES` gains `ACK_ATTEMPTED`.
- **U3 — CP2 pins.**
  - `CP2_UNION_VERSION` gets the §4 values.
  - A new endedness version check uses the same four values (D2).
  - A new `CP2_SOURCE_SHA256` constant serves D4.
- **U4 — Identity input.**
  - `identity` = exact {`union`, `request`, `census_log`, `evaluate_endedness`}.
  - The top-level `census` argument is the CP2 inner callable.
  - `_check_callbacks` is updated to match.
- **U5 — Union checks (S3b).**
  - Existing bounded detach: a `MappingProxyType` emergency union fails detach, giving `CP1_IDENTITY_UNION`.
  - Version check: `CP1_UNION_VERSION`.
  - Then `emergency is None`, `CLOSED_CONDITIONAL`, `causes == []`, hex digest, `prt_identities` typed-equal to `spec.identities`, and `union.item == owner.item` (D1).
- **U6 — Request (new).**
  - Bounded detach with CP1 caps, and the request format.
  - `request.item == owner.item` (D1).
  - D7, all typed-equal:
    - the main history's `wait_record` equals `spec.exit.wait_record`;
    - the main `launch_record` equals `spec.launch`;
    - `spec.oracle.wait_record` is in the set of oracle histories' `wait_record`.
  - Failure cause: `CP1_IDENTITY_UNION`. D7b is not implemented.
- **U7 — D3.** `served_count() == 0` before PRT, read through `observe`.
- **U8 — D4.** The `identity_union_census_cp2` attestation must also carry `cp2_source_sha256 == CP2_SOURCE_SHA256`. The parent's attestation covers CP2's PARENT_CODE_PROVENANCE condition.
- **U9 — S6b bind.** This is the last pre-invocation step, after S4–S6 pass. `observe('census_log bind', log.bind, nonce)` must return exactly `True`; otherwise `CP1_IDENTITY_UNION` and PRT is not invoked. By CP2's design, a refused bind poisons that log.
- **U10 — S7.** PRT is invoked with `W` (§5) as `census`.
- **U11 — S8b.**
  - Run the §5.7 join.
  - Call `evaluate_endedness(request copy, call.reader.read_bytes, C, log, fresh detached spec.identities, original deadline_check, nonce, retain)` through `observe`. `retain` is a fresh list registered in the process ledger before the call.
  - Check `type(e) is dict` before detaching.
  - Record retained objects as a count plus class names only.
  - **Acceptance list:**
    - `format` = ENDEDNESS_FORMAT, `state` = `ENDED_CONDITIONAL`, `causes` = [], `emergency` = None;
    - all four version fields equal the pins (D2);
    - hex `endedness_sha256`;
    - `union_sha256` equals the pre-invocation union digest;
    - `identities_match` True, `union_state` `CLOSED_CONDITIONAL`, `union_causes` [];
    - `deadline_crossed` False, `retention_failed` False;
    - `release_token` equals the nonce;
    - census: `served_sha256 == consumed_sha256`, `release_token == nonce`, `calls` 1, `served` 1, `refusals` 0, `poisoned` False, `reentries` 0, `post_seal_refusals` 0, `retention_failed` False, `complete` True, `observer_ok` True.
  - **CP1-added consistency check (availability only):** the retain list is empty and `e.retained == 0`. An evaluation that observed any exception is not a clean positive.
- **U12 — Receipt v2.**
  - `parent-release-caller-receipt-v2`, prefix `prt-caller-v2-`.
  - Adds request SHA/bytes, `consumed_sha256`, `served_sha256`, the wrapper call count, the CP2 module and design freeze, and the endedness module.
  - The J7 fields are unchanged.
- **U13 — Outcome v2.**
  - `parent-release-caller-outcome-v2`.
  - Adds the S2/S3/D8 evidence: CP1-retained exception count and class names, PRT prior count and class names, CP2-retained count and class names, consumed digest and wrapper calls.
- **U14 — J texts (§1).**
  - J4/J5 uncertainty strings in `_notes`.
  - The base-dict report read in `_attached`.
- **U15 — S1–S4** (§7).
- **U16 — `ReservationAccount`.**
  - `_account_checks` also compares the receipt v2 fields to the outcome.
  - Otherwise unchanged; `ACCOUNT_FORMAT` unchanged.

**No new cause names:**
- D1, D3, D7, request failures and bind failures give `CP1_IDENTITY_UNION`;
- D2 and D8 give `CP1_ENDEDNESS`;
- D4 gives `CP1_PREREQUISITE_MISSING`;
- wrapper refusals surface as PRT HELD, giving `CP1_RESULT_NOT_RELEASED`.

## 7. Exception handling (S1–S4, mirroring PRT v6 and consistent with CP2 v6)

- **S1 — Progress before the completion check.** Receipt create, identity, write, fsync, readback and directory fsync, and the PRT load flag, are recorded through the `retain` hook in `_Call.native` **before** the original-deadline completion check.
- **S2 — Exception ledger.**
  - **Retention.** An identity-unique retention list in first-retention order, with a separate `latest`/`revision`.
  - **Origin events (`origin=True`):** a callback raising (the PRT entry, CP2 calls, `C` inside `W`, the reader, the deadline predicate); a native call raising; a destructive close raising; a bookkeeping failure (description or attachment).
  - **Propagation-only boundaries (`origin=False`)** never reorder.
  - **Precedence.** An ordinary exception is never selected over a retained non-Exception object.
  - **Cleanup.** `_Call.release` attempts every close once and raises the newest non-Exception object among its attempts locally.
  - **Final selection** happens at the `invoke_release` / `ReservationAccount.release` boundary:
    - if any non-Exception object is retained, a HELD outcome is attached and `latest` propagates;
    - otherwise CP1 returns normally, HELD or RELEASED.
  - **Attachment.**
    - At most 8 rounds. Each round re-finalizes the HELD outcome, then writes `parent_release_caller_prior_exceptions` and then `parent_release_caller_outcome`, through the base instance dict and `dict.__setitem__`.
    - `parent_release_caller_prior_exceptions` is a plain tuple in first-retention order, excluding the propagated object.
    - Any origin event during a round forces reselection.
    - After 8 failed rounds, `latest` is raised without guaranteed attributes.
  - **No `__context__` writes.** No Python-level `__context__` writes; the prior tuple is the retention channel.
  - **Ledger copy.** Every retained object is also stored strongly in the process ledger, so it survives an attachment failure.
- **S3 — PRT priors.** CP1 records the count and class names of `parent_release_prior_exceptions`, read from the propagated object's base dict.
- **S4 — Metadata safety.**
  - Type names come from `type.__dict__['__name__'].__get__(type(x))`.
  - `str(exc)` runs only inside a BaseException guard that keeps failures as origins.
  - Classification uses the real type: `issubclass(type(exc), Exception)`.
  - Attachments are read with `dict.get` on the base instance dict.
  - No `getattr`/`setattr` on foreign exceptions.

## 8. Expectations to freeze with the source (NOT exercised)

Notation as in notes v1/v2. All F01–F48, V01–V14 and A01–A10 expectations carry forward with v3 names and formats.

**Journal authority:**

| ID | Case | Expected |
|---|---|---|
| K1 | Registry already holds a same-item RELEASED line from an escaped earlier run | PRT `P1_ALLOCATION_NOT_CURRENT` → H(`CP1_RESULT_NOT_RELEASED`); no receipt |
| K2 | Synthetic PRT raises `MemoryError` after appending a RELEASED line | H(`CP1_PRT_EXCEPTION`); unknown-state ledger entry; J5 uncertainty text; a later invocation for the same allocation behaves as K1 |
| K3 | PRT returns RELEASED but the registry holds a second same-item RELEASED line | H(`CP1_REGISTRY_READBACK`) |
| K4 | `ReservationAccount.release` given a dict built from journal or receipt bytes | `AC_OUTCOME_NOT_EFFECTIVE` |
| K5 | Prior-tuple member carries a superseded report that differs from the propagated object's | CP1 uses only the propagated object's report |

**D8 census copy:**

| ID | Case | Expected |
|---|---|---|
| N1 | 200001 rows | `W` refusal → PRT `P4_CENSUS_FAILED` → H(`CP1_RESULT_NOT_RELEASED`) |
| N2 | Fingerprint of 65 characters, or a character outside the alphabet | As N1 |
| N3 | Int above u32, or a bool in an int field | As N1 |
| N4 | `observed_at_mono` NaN, inf or int | As N1 |
| N5 | Extra or missing key at either level | As N1 |
| N6 | Synthetic second `W` call | Refusal plus latch → HELD |
| N7 | Synthetic `served_sha256` ≠ `consumed_sha256` | H(`CP1_ENDEDNESS`) |
| N8 | Deadline crosses between `C`'s return and the copy, or after the hash | Refusal → PRT HELD |
| N9 | KeyboardInterrupt from `C` | Propagates under S2 with a HELD outcome attached |
| N10 | Maximal in-bounds 200000-row snapshot | Passes the caps; byte length ≤ the hard cap |

**CP2 binding:**

| ID | Case | Expected |
|---|---|---|
| B1 | Bind refused (log already used) | H(`CP1_IDENTITY_UNION`); PRT not invoked |
| B2 | Synthetic bind returns non-True | As B1 |
| B3 | `served_count() == 1` before PRT | H(`CP1_IDENTITY_UNION`) |
| B4 | MINIMAL or PREBUILT endedness | H(`CP1_ENDEDNESS`) |
| B5 | Endedness module or freeze mismatch | H(`CP1_ENDEDNESS`) |
| B6 | `release_token` echo mismatch | H(`CP1_ENDEDNESS`) |
| B7 | Synthetic ENDED with a non-empty retain list | H(`CP1_ENDEDNESS`) |
| B8 | D7 ref mismatch | H(`CP1_IDENTITY_UNION`) |
| B9 | `union.item` or `request.item` ≠ owner item | H(`CP1_IDENTITY_UNION`) |
| B10 | Attestation lacks `cp2_source_sha256` | H(`CP1_PREREQUISITE_MISSING`) |

**Exceptions** (plan v2 W01–W18 and checkpoints 014–015):
- A, then B, then the same A: A propagates; the priors hold B.
- KeyboardInterrupt primary plus ordinary completion secondary: the KeyboardInterrupt propagates.
- Ordinary primary plus KeyboardInterrupt secondary: the KeyboardInterrupt propagates.
- KeyboardInterrupt, then SystemExit: SystemExit propagates; the priors hold the KeyboardInterrupt.
- Hostile metadata (`__context__` property, `__setattr__`, `__str__`, `__class__`): no unretained escape.
- Attachment fails 8 times: `latest` propagates without guaranteed attributes, and the objects stay in the ledger.

## 9. Availability costs (disclosed)

- The copy caps accept only CP2's genuine census format, not every census PRT would accept.
- CP2's sticky unknown incarnations make a quiescent host necessary for a positive.
- One reader instance allows 1024 calls, shared by PRT, CP1 and the CP2 rebuild.
- A stray RELEASED line (J4) blocks its allocation until a separately authorized parent procedure.
- Any PRT exception without an attached report blocks all later releases in that process.
- CP2 allows at most 4096 binds per module instance.
- The census copy can hold up to 200000 rows of Python dicts in memory once: bounded, but not small.

## 10. Boundaries (unchanged in kind)

- Native calls and callbacks, including `W`, `C` and the deadline predicate, can stall. Checks follow completion; there is no hard-real-time guarantee.
- In-process forgery, module reload or restart is outside what the source can prevent.
- `exec` of verified PRT bytes trusts the interpreter.
- Hashes and self-reported version fields authenticate selected bytes or claims, never origin.
- CP1 cannot detect an omitted historical identity, and CP2 results are conditional on its listed conditions.
- J8: consumers other than CP1 must adopt the journal contract independently.
