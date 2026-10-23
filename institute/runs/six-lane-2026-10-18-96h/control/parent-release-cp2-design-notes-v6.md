# CP2 v6 minimal successor — SOURCE-ONLY, NOT ACCEPTED (independent review required)

Actual `/bin/date`: 2026-10-19T21:21:02-0700. No import, compile, AST parse, test, census or execution. These notes are self-contained: they carry every v5 note (adapted only where v6 changes a value) plus the v6 change.

| Artifact | SHA256 |
|---|---|
| source `control/parent_release_identity_v6.py` (123255 B / 2316 LF lines) | `a9b82a48548257782871404ed366ca2719abc2b081efa452c7e3907c0aecff5b` |
| exact v5->v6 diff `review/parent_release_identity_v5_to_v6.diff` (4147 B) | `eeb6f1789029bf8cfafdbdd10b0a6f4db89c3e4c3164168479a45cb790892874` |
| exact v4->v6 diff `review/parent_release_identity_v4_to_v6.diff` (89526 B) | `82afe0b396c1cf12af8ddfe72988fbd32b94c672d95479917e0d5f621c2b9846` |
| v6 delta frozen before source `control/parent-release-cp2-design-freeze-v6.json` | `2135fc82e5acc80ae1122badcccd40e441824018190fca07d9158d777a266bf2` |
| base joined design `control/parent-release-cp2-design-freeze-v5.json` | `687a3f93f4a3df1a3929b60e2485fa5d6912a128749139f4ae898c7121d320ad` |
| final PRE-SOURCE frozen interface `control/parent-release-cp2-v5-frozen-interface-clarifications-v1.json` | `9ad1081be8ad7b4e97b3a27a9c84e11fed82ffa002c26e3042aac54c4c42a884` |
| all controls `review/parent-release-cp2-controls-v6-rev2.json` (supersedes rev1 `review/parent-release-cp2-controls-v6.json` 67f408b81fe690332305d3dcd68d4722523ff2b81fa43bb95f62972d43d3955f) | `37193a55819d6a8b79c5410232fbc56f0a6f8e344dc0b97591db107f548ec292` |
| successor authority `control/parent-release-and-cp2-v6-successor-authority-v1.json` | `b08a12dd36d52a020a3927e64d28d483886505b4d02df4407142aaae3393e27e` |
| D8 decision `control/parent-release-cp1-D8-consumed-snapshot-join-decision-v1.json` | `79540a182203d805077c445e12283070dcebe52ce3c0b545bb94f5485dd177a2` |
| v5 source (immutable SELF-HOLD, never reviewed, not CP1 eligible) | `7a512b8e4a724b59fb2c8a651123a2dbce4ef6d4d38e152547624b6f477f9d53` |
| H09 self-hold record `review/parent-release-cp2-v5-native-priority-self-hold-v1.json` | `fd217f9f3ccff47b787cd766cfe40a4a55be4281e0b65ca0e56c5a8f8ac61db1` |
| scope `control/parent-release-cp2-v5-joined-repair-scope-v1.json` | f05d60f8faee5f1db7539991507352520fefb8dd3ea3b6135ff1bc2a5763f997 |
| v4 review (0F/4M/4m) `review/parent-release-cp2-v4-review-prompt-v1.stdout.txt` | ca9d2eadc49a54fc1d51dfa2c6a1d82b44f3fac939bb9c8a0f98f76a64992097 |
| SR6 finding `review/parent-release-cp2-finding-sr6-v1.json` | 329c3cfb6197f4e3b76d403506ff7cfc815e337babf3b0abc2939642698696d0 |
| SR6 plan | 1ec957ccdf650341551e8032df82a8e02021c23775c7923753da1b9797e2060e |

## V6 change: native exception priority (the only source delta)

v5 `_native` re-raised the completion-check secondary whenever one existed. If the native call raised a non-Exception primary P (KeyboardInterrupt, SystemExit or any other BaseException that is not an Exception) and the ORIGINAL completion check raised an ordinary secondary S, PRT could catch S as an ordinary failure and absorb P (**H09**, recorded as the v5 SELF-HOLD). v6 `_native` (source lines 706-728):

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
- Every ordinary `_check` failure latches `state.poisoned = True` before raising (lines 689-703), so selecting P loses no fail-closed latch. `_attempt` (line 945) and the census wrapper's `_refusal` (line 958) also poison.
- `_ordinary` is `issubclass(type(exc), Exception)`: no foreign method, property or override is consulted.
- The reader path (`_Io.tick` 589-598, `_Io.settle_read` 600-614) already had this priority and is unchanged: a non-Exception S propagates, else P, and an ordinary S latches `crossed`. When both are ordinary the reader propagates P and `_native` propagates S; both outcomes are nonpositive.
- Controls: H09 and K11 now state the v6 behaviour; H11-H16 isolate every branch of the table; K29 documents the availability consequence below.

## Exception-priority sites audited (unchanged in v6)

- `_check` (689-703), `CensusLog.bind` (861-876) and `_Transaction.journal` (829-843) each handle one exception: keep it, poison, bare re-raise.
- `_abort_end` (897-909) and `_refusal` (958-966) catch journal failures only as `Exception`, keep them and never replace the propagating exception. They skip journaling once retention has failed.
- The `_attempt` per-pid handler (930-937) catches only `_NativeError` and re-raises it when the transaction is poisoned.
- The census wrapper (1029-1033) calls `_refusal` and then re-raises bare; its `finally` only clears `active`.
- Evaluator reader and diagnostic paths keep the v5 M3/SR6 rules (controls C43, E26, E41, E42, H06-H08).

## Limitations carried or newly documented (no code change)

- When P outranks S, the attempt_end and refusal journal entries describe P's chain only. S survives as an actual retained object, and in the retained count, but not as a journal description. Outside minimal scope; the transaction is nonpositive either way.
- **K29.** Every ordinary identification failure (a pid that vanished between listing and identification) is a retained object. Thirty in one transaction, across up to 3 attempts, stop admission: the census refuses (HELD), and that attempt gets no attempt_end and no refusal entry, even where a later attempt might have completed. This fail-closed availability cost comes from the approved cap32/stop30 interface and is unchanged since v5.
- SR4 (dependent row-conflict noise) and SR5 (no structured request binding inside the union) remain out of scope. There is no forgery protection; parent code and observation provenance stay prerequisites.

## D8 consumed-snapshot join (no CP2 interface change)

D8 (79540a18) is now REQUIRED for CP1. CP2 already provides what it needs:

- `census()` returns the exact served dict `{'complete': bool, 'processes': [{'pid', 'ppid', 'pgid', 'uid': int, 'start_fingerprint': str}, ...], 'observed_at_mono': finite float}`.
- `log.served_sha256()` and `summary()['served_sha256']` hold `sha256(_canonical(served))`, where `_canonical(v) = (json.dumps(v, sort_keys=True, ensure_ascii=True, allow_nan=False, separators=(',', ':')) + '\n').encode('ascii')`. The digest is set when the served entry is journaled, before the final ORIGINAL check, so it can exist on a refused call: it is NOT success.
- The evaluator's `census.served_sha256` must equal the digest recomputed from the journaled rows and the transaction's served digest (`_census_evidence`).
- CP2's row cap MAX_ROWS = 200000 equals PRT's row limit; more listed pids raise CensusRefusal('census process cap').
- The evaluator must receive the ORIGINAL inner census, the ORIGINAL deadline and the bound nonce, never CP1's wrapper; otherwise E_CENSUS_BINDING.

## Approved CP1/census interface

Main approved this SOURCE interface; CP1 accepted its call ordering, retention and emergency rules before code. Not runtime or pin acceptance. v6 keeps it unchanged; only the module and design-freeze values in item 6 change.

1. Parent: `census, log = make_census(D)` where D is the ORIGINAL nonrenewing deadline callable object used by the reader/PRT.
2. CP1's S1 creates fresh nonce T. As its LAST pre-PRT step (after served_count==0, source and authority checks), through its original-deadline wrapper: `log.bind(T) is True`. T is exact lowercase hex64. Refused bind poisons (malformed/reused token, already bound/sealed/poisoned/called/inflight); unbound census refuses and poisons. A module-instance token set is bounded4096 and never reuses a token.
3. CP1 passes its wrapper around the IDENTICAL inner `census` to PRT. Wrapper calls inner once, detaches a bounded exact-type copy and hashes its canonical bytes before returning that copy to PRT. CP1 records consumed_sha256. D8 (79540a18) now makes this wrapper REQUIRED; the evaluator still receives the same inner object.
4. `evaluate_endedness(request, read_bytes, census, census_log, identities, D, T, retain=fresh_exact_list)`.
5. Binding before seal: log issued by this module, token T equal to bound token, D is state.deadline, census is state.census. Mismatch -> E_CENSUS_BINDING, NO seal. Then seal single evaluation, require no poison/reentry/retention failure, calls1/served1/refusals0 and no inflight call.
6. Normal acceptance: exact dict, emergency None, module parent_release_identity_v6.py, design freeze `2135fc82e5acc80ae1122badcccd40e441824018190fca07d9158d777a266bf2`, scheme sv19-incarnation-v1, producer cb828a78..., format parent-release-identity-endedness-v1, state ENDED_CONDITIONAL, causes[], hex endedness_sha256, rebuilt union_sha256 equals pre-invoke union digest, union_state CLOSED_CONDITIONAL, union_causes[], identities_match True, deadline_crossed False, release_token T, census.release_token T, census.served_sha256==consumed_sha256, census.calls1/served1/refusals0/poisonedFalse. CP1 separately requires served_count0 before PRT, count1 after, wrapper calls1.
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

Only exclusive writes, byte hashes, exact-once text replacements, difflib diffs and regex checks. No subject import, AST, compile, tests or execution. All older files are untouched. The v6 bytes equal v5 with exactly the five replacements frozen in design freeze v6 (title, V6 docstring paragraph, design-freeze pin, module name, `_native` selection); the exact v5->v6 diff shows nothing else. Controls rev2 hold 70 union / 29 census / 44 endedness / 16 hostile-metadata / 3 native fixtures, frozen and NOT exercised. Review must cover the entire v6 source, both exact diffs, all controls, these notes, both design freezes, the clarification and the retained findings (v4 review M1-M4/m5-m8, SR6, H09). The complete partition is `review/parent-release-cp2-v6-review-partition-v1.json` (parts A/B/C, each under 220000 B). The author launched no review. Do NOT review v5 or unchanged v4, and do not run qualification from this source-only delivery.
