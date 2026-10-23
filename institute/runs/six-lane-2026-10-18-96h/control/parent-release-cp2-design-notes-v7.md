# CP2 v7 joined repair — SOURCE-ONLY, NOT ACCEPTED (independent review required)

Actual `/bin/date`: 2026-10-19T22:00:19-0700. No import, compile, AST parse, test, census or execution. These notes are self-contained: they carry every v6 note (line references and values adapted to v7) plus the v7 repairs. Owner throttle 3ba3ca96: the v7 review is deferred, not cancelled.

| Artifact | SHA256 |
|---|---|
| source `control/parent_release_identity_v7.py` (127471 B / 8 LF lines) | `8374a7055cd5ef792359aeeef4e512a65d9d960098f9c27fde0f66f30a651b30` |
| exact v6->v7 diff `review/parent_release_identity_v6_to_v7.diff` (14319 B) | `280c0c732f4accf2d02b597ff75ed07e283ce823bf870ad7cfb5d2393584bd53` |
| exact v4->v7 diff `review/parent_release_identity_v4_to_v7.diff` (94430 B) | `300168bf9469245a3e049554a81a96005abbb0370319c66b51c5199c70a3abc9` |
| v7 delta frozen before source `control/parent-release-cp2-design-freeze-v7.json` | `5e020705027fceb039fcc678f93a8a8fc668e5094b0140083772ca79c99c27c9` |
| v6 delta freeze `control/parent-release-cp2-design-freeze-v6.json` | `2135fc82e5acc80ae1122badcccd40e441824018190fca07d9158d777a266bf2` |
| base joined design `control/parent-release-cp2-design-freeze-v5.json` | `687a3f93f4a3df1a3929b60e2485fa5d6912a128749139f4ae898c7121d320ad` |
| final PRE-SOURCE frozen interface `control/parent-release-cp2-v5-frozen-interface-clarifications-v1.json` | `9ad1081be8ad7b4e97b3a27a9c84e11fed82ffa002c26e3042aac54c4c42a884` |
| all controls `review/parent-release-cp2-controls-v7.json` | `9c41d8d81e800e1eb7a9fcab00e8c8ad4022dfb54c9125d5d477aff16117a0f4` |
| v7 scope `control/parent-release-cp2-v7-joined-repair-scope-v1.json` | `c8bbb4770f8824248e326a3b18f0d2ed92252d937baaa62e208d32a43db2cab1` |
| v6 three-part HOLD `review/parent-release-cp2-v6-three-part-parent-HOLD-v1.json` | `e5f323de2de930b12694904f7c743f0632bc529eac75b7fe5c2195e6b3dc84d7` |
| v6 Codex reviews A / B / C (stdout) | `1cd473768c34e3e509e03754f0631a5a3b19e9b3b390027efd3bb09770c07a78` / `f3a516bd1a763b14c21fc4a44009872eee82496f58fa2a70eddf6f9a974623ed` / `4860e6912087b9b2fa2328ca308e2aa0971d3e9396bd987be9cce60a82c5590b` |
| v6 source (immutable, HOLD) | `a9b82a48548257782871404ed366ca2719abc2b081efa452c7e3907c0aecff5b` |
| v6 successor authority `control/parent-release-and-cp2-v6-successor-authority-v1.json` | `b08a12dd36d52a020a3927e64d28d483886505b4d02df4407142aaae3393e27e` |
| D8 decision `control/parent-release-cp1-D8-consumed-snapshot-join-decision-v1.json` | `79540a182203d805077c445e12283070dcebe52ce3c0b545bb94f5485dd177a2` |
| H09 self-hold record `review/parent-release-cp2-v5-native-priority-self-hold-v1.json` | `fd217f9f3ccff47b787cd766cfe40a4a55be4281e0b65ca0e56c5a8f8ac61db1` |
| v5 joined scope `control/parent-release-cp2-v5-joined-repair-scope-v1.json` | f05d60f8faee5f1db7539991507352520fefb8dd3ea3b6135ff1bc2a5763f997 |
| v4 review (0F/4M/4m) `review/parent-release-cp2-v4-review-prompt-v1.stdout.txt` | ca9d2eadc49a54fc1d51dfa2c6a1d82b44f3fac939bb9c8a0f98f76a64992097 |
| SR6 finding `review/parent-release-cp2-finding-sr6-v1.json` | 329c3cfb6197f4e3b76d403506ff7cfc815e337babf3b0abc2939642698696d0 |
| owner throttle `control/owner-workload-throttle-one-third-v1.json` | 3ba3ca96e2a869d5fee8fa76186184e5d380cc296fec5713da9d97c35776f9de |

## V7 changes: joined repair of the v6 three-part HOLD (source lines are v7)

v7 = v6 + the 17 ordered exact-once replacements frozen in design freeze v7; the exact v6->v7 diff shows nothing else.

- **M1 (CP2-V6-M1, callback admission).** `_build_union` (1969-2015) and `evaluate_endedness` (2331-2375) each compute ONE predicate `admitted = type(retain) is list and callable(read_bytes) and callable(deadline_check)` (1978, 2345). Not admitted -> nonpositive result with no reader/deadline/census callback; the final ORIGINAL check now also requires `admitted` (2003, 2361). Admitted calls keep every v6 check including the final one. `_Io.tick` (604-613) still refuses with `_RetentionStop` BEFORE any invocation once retention admission stopped (C68 unchanged). The evaluator predicate now includes the reader, so a non-callable reader is refused before binding/seal with E_INTERNAL_ERROR (v6 sealed, invoked the deadline and returned E_UNION_HELD). Controls C63, C69, C70, E39, E48, E49.
- **M2 (CP2-V6-M2, late poison).** `_endedness` keeps the sealed transaction and validated served entry in `view` (2256). After the LAST external callback (the final check passed, failed or was skipped) `_late_recheck` (2158-2177) runs with no callback and no seal: the `_seal` cleanliness predicate (sealed, not active/poisoned/retention-failed, reentries 0, calls 1, served 1, refusals 0) AND a fresh census view exactly equal to the reported one. Otherwise the view is refreshed, E_CENSUS_TRANSACTION fires and the result is reassembled HELD (2364-2365). A caught refused rebind (bind still poisons) or a post-seal census call during reader/deadline callbacks therefore yields HELD. Skipped once retention admission stopped (already MINIMAL/PREBUILT HELD). It is bounded internal work after the final check; a further deadline check would itself be a callback able to re-poison, so the recheck is last. Controls E45-E47, E50.
- **M3 (CP2-V6-M3, metadata).** `_tname` (303-310) returns the base-getset name only when `type(name) is str`, else `<metadata-unavailable>`. Audit (design freeze v7 `m3_audit`): foreign metadata reaches formatting only through `_tname`/`_why`/`_chain` (callback exceptions, their args/cause/context, non-None deadline returns); `_why` formats only exact str/int/None/bool args; request, reader bytes, identities and release token are exact-typed before use; native values are exact ints/bytes. No site concatenates, formats or compares a str subclass from foreign metadata. Where a whole diagnostic part equals the sentinel, `lost_saturated` forces the INTERNAL_ERROR cause on an already failing path. Controls H17-H20.
- **m4 (CP2-V6-m4).** The per-pid `except _NativeError` handler (954-960) calls `state.keep(exc)` on entry, before the poisoned test; identity dedup keeps `_native` errors once, and bracket-consistency errors (IDENTITY_CHANGED / IDENTITY_METADATA_CHANGED) now count toward stop30. Controls K29-K31.
- **m5 (CP2-V6-m5).** `_sticky` (1742-1786): with `main_wait` present the main identity is usable only if `_identity_ok` AND `_int(main_wait pid, True)` AND identity pid == that pid; otherwise a sticky U_UNKNOWN_INCARNATION detail (`main_child_without_identity` or `main_child_identity_pid_mismatch`). `main_wait` None keeps v6 handling; `_unknowns` rows are unchanged (informational). Controls C28 (clarified), C71, C72.
- **m6 (CP2-V6-m6).** `_Io.diagnose_completion` (594-602) and `_Io.settle_read` (615-631) keep the captured objects first and build events/descriptions only while not stopped; builder/evaluator/assembly handlers use `_detail` (681-683), a constant once stopped. Already guarded: `_guard`, the `_Io.read` success path, `_abort_end`/`_refusal`, the per-pid handler, `event()`. Controls E42 (refined), H21.

## V6 change: native exception priority (retained unchanged in v7)

v5 `_native` re-raised the completion-check secondary whenever one existed. If the native call raised a non-Exception primary P (KeyboardInterrupt, SystemExit or any other BaseException that is not an Exception) and the ORIGINAL completion check raised an ordinary secondary S, PRT could catch S as an ordinary failure and absorb P (**H09**, recorded as the v5 SELF-HOLD). v6/v7 `_native` (v7 source lines 728-750):

```
    except BaseException as primary:
        try:
            _check(state, stage, pid, 'after failed')
        except BaseException as secondary:
            state.keep(primary)
            state.keep(secondary)
            if _ordinary(primary) or not _ordinary(secondary):
                raise  # secondary selected; interpreter context keeps the primary
        state.keep(primary)  # identity-deduplicated: completion passed or the primary outranks an ordinary secondary
        raise
```

| native primary P | after-failed completion check | propagates |
|---|---|---|
| any | passes | P (as v5) |
| Exception | raises ordinary S | S, with S.__context__ = P (as v5) |
| Exception | raises non-Exception S | S (as v5) |
| non-Exception | raises ordinary S | **P (v6; v5 propagated S)** |
| non-Exception | raises non-Exception S | S (as v5) |

- Both actual objects stay in the transaction's retained list in every branch (`log.exceptions()`). `_retain` is identity-deduplicated, so the repeated `keep(primary)` stores P once.
- P is selected by a bare `raise` after the inner handler ends. That re-raises the currently handled P without interpreter context chaining. A literal `raise primary` inside the secondary handler (the H09 record's repair wording) would make the interpreter set `P.__context__ = S` and clear `S.__context__` to break the cycle; v6 rewrites neither. S keeps `S.__context__ = P`.
- Every ordinary `_check` failure latches `state.poisoned = True` before raising (v7 lines 711-725), so selecting P loses no fail-closed latch. `_attempt` (v7 line 968) and the census wrapper's `_refusal` (v7 line 981) also poison.
- `_ordinary` is `issubclass(type(exc), Exception)`: no foreign method, property or override is consulted.
- The reader path (`_Io.tick` 604-613, `_Io.settle_read` 615-631) already had this priority and is unchanged: a non-Exception S propagates, else P, and an ordinary S latches `crossed`. When both are ordinary the reader propagates P and `_native` propagates S; both outcomes are nonpositive.
- Controls: H09 and K11 now state the v6 behaviour; H11-H16 isolate every branch of the table; K29 documents the availability consequence below.

## Exception-priority sites audited (v7 line numbers; selection unchanged)

- `_check` (711-725), `CensusLog.bind` (883-898) and `_Transaction.journal` (851-865) each handle one exception: keep it, poison, bare re-raise.
- `_abort_end` (919-931) and `_refusal` (981-989) catch journal failures only as `Exception`, keep them and never replace the propagating exception. They skip journaling once retention has failed.
- The `_attempt` per-pid handler (954-960) catches only `_NativeError`, retains it (v7 m4) and re-raises it when the transaction is poisoned.
- The census wrapper (1052-1056) calls `_refusal` and then re-raises bare; its `finally` only clears `active`.
- Evaluator reader and diagnostic paths keep the v5 M3/SR6 rules (controls C43, E26, E41, E42, H06-H08).

## Limitations carried or newly documented

- When P outranks S, the attempt_end and refusal journal entries describe P's chain only. S survives as an actual retained object, and in the retained count, but not as a journal description. Outside minimal scope; the transaction is nonpositive either way.
- **K29.** Every retained identification failure (a pid that vanished between listing and identification, and since v7 m4 every bracket-consistency error) counts toward the cap. Thirty in one transaction, across up to 3 attempts, stop admission: the census refuses (HELD), and that attempt gets no attempt_end and no refusal entry, even where a later attempt might have completed. This fail-closed availability cost comes from the approved cap32/stop30 interface.
- **M2 conservatism.** Any post-seal transaction change during evaluation callbacks makes the evaluation HELD, including a refused post-seal census call that does not poison (E47). The evaluator refuses a non-callable reader before binding/seal (E49), so such a call leaves the transaction unsealed.
- SR4 (dependent row-conflict noise) and SR5 (no structured request binding inside the union) remain out of scope. There is no forgery protection; parent code and observation provenance stay prerequisites.

## D8 consumed-snapshot join (no CP2 interface change)

D8 (79540a18) is now REQUIRED for CP1. CP2 already provides what it needs:

- `census()` returns the exact served dict `{'complete': bool, 'processes': [{'pid', 'ppid', 'pgid', 'uid': int, 'start_fingerprint': str}, ...], 'observed_at_mono': finite float}`.
- `log.served_sha256()` and `summary()['served_sha256']` hold `sha256(_canonical(served))`, where `_canonical(v) = (json.dumps(v, sort_keys=True, ensure_ascii=True, allow_nan=False, separators=(',', ':')) + '\n').encode('ascii')`. The digest is set when the served entry is journaled, before the final ORIGINAL check, so it can exist on a refused call: it is NOT success.
- The evaluator's `census.served_sha256` must equal the digest recomputed from the journaled rows and the transaction's served digest (`_census_evidence`).
- CP2's row cap MAX_ROWS = 200000 equals PRT's row limit; more listed pids raise CensusRefusal('census process cap').
- The evaluator must receive the ORIGINAL inner census, the ORIGINAL deadline and the bound nonce, never CP1's wrapper; otherwise E_CENSUS_BINDING.

## Approved CP1/census interface

Main approved this SOURCE interface; CP1 accepted its call ordering, retention and emergency rules before code. Not runtime or pin acceptance. v7 keeps it unchanged; only the module and design-freeze values in item 6 change.

1. Parent: `census, log = make_census(D)` where D is the ORIGINAL nonrenewing deadline callable object used by the reader/PRT.
2. CP1's S1 creates fresh nonce T. As its LAST pre-PRT step (after served_count==0, source and authority checks), through its original-deadline wrapper: `log.bind(T) is True`. T is exact lowercase hex64. Refused bind poisons (malformed/reused token, already bound/sealed/poisoned/called/inflight); unbound census refuses and poisons. A module-instance token set is bounded4096 and never reuses a token.
3. CP1 passes its wrapper around the IDENTICAL inner `census` to PRT. Wrapper calls inner once, detaches a bounded exact-type copy and hashes its canonical bytes before returning that copy to PRT. CP1 records consumed_sha256. D8 (79540a18) now makes this wrapper REQUIRED; the evaluator still receives the same inner object.
4. `evaluate_endedness(request, read_bytes, census, census_log, identities, D, T, retain=fresh_exact_list)`.
5. Binding before seal: log issued by this module, token T equal to bound token, D is state.deadline, census is state.census. Mismatch -> E_CENSUS_BINDING, NO seal. Then seal single evaluation, require no poison/reentry/retention failure, calls1/served1/refusals0 and no inflight call.
6. Normal acceptance: exact dict, emergency None, module parent_release_identity_v7.py, design freeze `5e020705027fceb039fcc678f93a8a8fc668e5094b0140083772ca79c99c27c9`, scheme sv19-incarnation-v1, producer cb828a78..., format parent-release-identity-endedness-v1, state ENDED_CONDITIONAL, causes[], hex endedness_sha256, rebuilt union_sha256 equals pre-invoke union digest, union_state CLOSED_CONDITIONAL, union_causes[], identities_match True, deadline_crossed False, release_token T, census.release_token T, census.served_sha256==consumed_sha256, census.calls1/served1/refusals0/poisonedFalse. CP1 separately requires served_count0 before PRT, count1 after, wrapper calls1.
7. `log.served_sha256()` returns exact served-dict digest or None; a digest or count can survive late refusal and is NOT success. `log.exceptions()` returns actual retained objects; summary returns counters/chains/binding and poison flags.
8. Request schema/history keys unchanged. Union top-level item is request item; CP1 may bind it to owner/spec item. Version fields are consistency checks only. Rebuilding from captured histories remains load-bearing, not self-attestation.

## Complete exception-object preservation and admission cap

Public builders/evaluator have default retain=None only for conservative refusal. **A parent-owned exact list is REQUIRED before real callbacks** (build U_CALLBACKS_INVALID, eval E_INTERNAL_ERROR when absent). CP1 agreed to strongly own its fresh list BEFORE invocation and retain it across HELD/RELEASED/BaseException even if partial attachment fails. Parent pre-invoke builder likewise owns its list. JSON contains counts/descriptions; actual objects remain in these lists, log.exceptions or partial attributes.

Capacity32, admission stops at30, reserve2 for already-in-flight failures. The triggering object is stored BEFORE stop. IO stops callbacks and diagnostic/hash work, returns MINIMAL/PREBUILT; census poisons and stops acquisition/journal retries. Already-in-flight primary/completion-secondary both remain exact objects. Retention overflow/append failure has a strong overflow slot, independent best-effort external append and nonpositive latch. At interpreter inability to allocate/deliver exceptions the hard boundary applies; no drop-and-continue positive. Interrupted or failed journal publication cannot clear poison.

## Review and SR6 repairs implemented in v5 (retained unchanged in v6)

- **M1:** token + identical original deadline + identical inner callable + PRT-consumed-copy digest join, not merely unused issued log. Stale A with B callable/nonce is refused before sealing.
- **M2:** served record is serialized/hashed/journaled BEFORE the final ORIGINAL check immediately before return. Failed completion poisons/refuses even though served bytes/hash/count exist.
- **M3:** raw reader completion predicate is captured directly after reader invocation on success and every exception exit, BEFORE retain/format/hash/log. Protected diagnostics cannot mask selected callback errors. Non-Exception completion secondary wins (primary context retained), else exact primary; ordinary timing failures latch crossed. Actual primary/secondary both retained.
- **M4:** setup/body/assembly/finalization ordinary exception boundary; `_State.fire` nonpositive latch BEFORE allocation; lost diagnostic/retention forces HELD. Full hashed report -> MINIMAL unhashed dict -> prebuilt immutable mapping, no serialization/hash in either fallback.
- **m5:** every attempt end has typed exact count/boolean/status/error/chain/digest fields and count/status conservation. Earlier attempts' digest syntax is checked only; their rows are not stored, so no earlier digest recomputation claim. Final rows actually re-hashed, all served counts exact int.
- **m6:** unusable helper identities (null, malformed non-null dict/string, pid mismatch) independently sticky unknown. Malformed main identities with main_wait present also sticky.
- **m7:** caught active reentry poisons before raising and outer check refuses before next acquisition; start/setup/end journal failures poison and retain objects. No end-journal blind retry. Post-seal calls refuse before acquisition and only increase post_seal_refusals (journal unchanged).
- **m8:** E01 excludes deadline crossings; K08/E06 specify changes BETWEEN successful five-acquisition brackets; K25/K26 cover initial/final WITHIN-bracket aborts. E25 transient/persistent subcases correctly distinguish MINIMAL vs PREBUILT.
- **SR6:** no foreign exception str/repr/__name__/__context__/setattr/isinstance calls. Name via type getset, args via BaseException getset, exact safe primitive argument formatting only. Attach through base instance dict + dict.__setitem__; implicit interpreter context chain plus actual references preserve errors. Cause/context descriptions via base getsets, bounded cycle-safe8. Exact-JSON identities are bounded/preflighted/detached before equality, no hostile key hashing/equality.

v4 load-bearing union rebuild, baseline equality/recorded-only spawn chronology, every rich historical identity variant, sticky unknown history, native ABI/fingerprint convention and late-census endedness predicates are otherwise preserved. SR4 dependent row-conflict noise and SR5 absence of structured request inputs inside union remain recorded/out of scope.

## Exact emergency/alias/interpreter boundary

Normal report: independent mutable dict, emergency None, canonical digest. MINIMAL: fresh dict, emergency MINIMAL, state HELD, digest None; NO serialization/hash. PREBUILT: same module-import-created MappingProxyType object aliases across calls, deeply immutable (only tuple/str/bool/None nested values), state HELD, emergency PREBUILT, null digest. No allocation/hash/serialization needed to return it; CP1 must recognize it as HELD even though not exact dict, and perform no later readback/publication. Full version fields exist in all tiers, never a positive fallback.

Process death/uncatchable signals/native stalls or nontermination/hostile same-process code/interpreter failure before frame entry or while dispatching/handling/returning exceptions or the prebuilt object/asynchronous non-Exception interrupts remain unavoidable. No total-function or hard-real-time promise. The ordinary handlers cover operations that execute within their Python protected regions. BaseException propagation can still be interrupted by interpreter failure itself. Metadata helpers execute no foreign conversion methods (unlike the preliminary SR6 plan).

## Verification and review coverage

Only exclusive writes, byte hashes, exact-once text replacements, difflib diffs and regex checks. No subject import, AST, compile, tests or execution. All older files are untouched. The v7 bytes equal v6 with exactly the 17 replacements frozen in design freeze v7; the exact v6->v7 diff shows nothing else; a regex audit finds no process/signal/spawn/wait/open/exec/eval/repr/__name__/__context__/setattr/isinstance/format call. Controls v7 hold 74 union / 31 census / 50 endedness / 21 hostile-metadata / 3 native fixtures, frozen and NOT exercised. Review must cover the entire v7 source, both exact diffs, all controls, these notes, the freezes, the clarification and the retained findings (v4 review, SR6, H09, v6 HOLD). The complete partition is `review/parent-release-cp2-v7-review-partition-v1.json` (every part under 220000 B). The author launched no review. Do NOT review v6 or v5, and do not run qualification from this source-only delivery.
