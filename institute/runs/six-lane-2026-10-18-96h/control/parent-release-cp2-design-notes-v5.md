# CP2 v5 joined repair — SOURCE-ONLY, SELF-HOLD (H09)

Actual `/bin/date`: 2026-10-19T18:42:01-0700. No import, compile, AST parse, test, census or execution.

| Artifact | SHA256 |
|---|---|
| source `control/parent_release_identity_v5.py` (121975 B / 2303 LF lines) | `7a512b8e4a724b59fb2c8a651123a2dbce4ef6d4d38e152547624b6f477f9d53` |
| exact v4->v5 diff `review/parent_release_identity_v4_to_v5.diff` | `87521fcb4c6b7a17a558c1de0609117e5a9b028d36c31fe73c4ef386b6a050c3` |
| joined design `control/parent-release-cp2-design-freeze-v5.json` | `687a3f93f4a3df1a3929b60e2485fa5d6912a128749139f4ae898c7121d320ad` |
| final PRE-SOURCE frozen interface `control/parent-release-cp2-v5-frozen-interface-clarifications-v1.json` | `9ad1081be8ad7b4e97b3a27a9c84e11fed82ffa002c26e3042aac54c4c42a884` |
| all controls `review/parent-release-cp2-controls-v5.json` | `724eeccf2e09d5caa2077c5a6561e03ea1db1fef44fdc2be19f5f5d5c55a5036` |
| scope `control/parent-release-cp2-v5-joined-repair-scope-v1.json` | f05d60f8faee5f1db7539991507352520fefb8dd3ea3b6135ff1bc2a5763f997 |
| v4 review (0F/4M/4m) | ca9d2eadc49a54fc1d51dfa2c6a1d82b44f3fac939bb9c8a0f98f76a64992097 |
| SR6 plan | 1ec957ccdf650341551e8032df82a8e02021c23775c7923753da1b9797e2060e |

## STOP: newly identified exception-priority branch

v5 is NOT source-ready. In `_native`, a native KeyboardInterrupt/SystemExit primary plus an ordinary deadline completion secondary propagates the ordinary secondary. Both actual objects are retained, but PRT could absorb that secondary and thereby suppress the primary. The reader path already prioritizes correctly. This is **H09** in the frozen controls and a source-acceptance blocker. Main was asked to authorize an immutable successor before any review of v5. Minimal fix: after retaining both, if primary is non-Exception and secondary is Exception, raise primary; otherwise secondary. No runtime is involved. v5 remains immutable.

## Approved CP1/census interface

Main approved this SOURCE interface; CP1 accepted its call ordering, retention and emergency rules before code. Not runtime or pin acceptance.

1. Parent: `census, log = make_census(D)` where D is the ORIGINAL nonrenewing deadline callable object used by the reader/PRT.
2. CP1's S1 creates fresh nonce T. As its LAST pre-PRT step (after served_count==0, source and authority checks), through its original-deadline wrapper: `log.bind(T) is True`. T is exact lowercase hex64. Refused bind poisons (malformed/reused token, already bound/sealed/poisoned/called/inflight); unbound census refuses and poisons. A module-instance token set is bounded4096 and never reuses a token.
3. CP1 passes its wrapper around the IDENTICAL inner `census` to PRT. Wrapper calls inner once, detaches a bounded exact-type copy and hashes its canonical bytes before returning that copy to PRT. CP1 records consumed_sha256. Without the parent's D8 decision, it may pass inner straight to PRT but still uses the same inner object at evaluation.
4. `evaluate_endedness(request, read_bytes, census, census_log, identities, D, T, retain=fresh_exact_list)`.
5. Binding before seal: log issued by this module, token T equal to bound token, D is state.deadline, census is state.census. Mismatch -> E_CENSUS_BINDING, NO seal. Then seal single evaluation, require no poison/reentry/retention failure, calls1/served1/refusals0 and no inflight call.
6. Normal acceptance: exact dict, emergency None, module parent_release_identity_v5.py, design freeze `687a3f93f4a3df1a3929b60e2485fa5d6912a128749139f4ae898c7121d320ad`, scheme sv19-incarnation-v1, producer cb828a78..., format parent-release-identity-endedness-v1, state ENDED_CONDITIONAL, causes[], hex endedness_sha256, rebuilt union_sha256 equals pre-invoke union digest, union_state CLOSED_CONDITIONAL, union_causes[], identities_match True, deadline_crossed False, release_token T, census.release_token T, census.served_sha256==consumed_sha256, census.calls1/served1/refusals0/poisonedFalse. CP1 separately requires served_count0 before PRT, count1 after, wrapper calls1.
7. `log.served_sha256()` returns exact served-dict digest or None; a digest or count can survive late refusal and is NOT success. `log.exceptions()` returns actual retained objects; summary returns counters/chains/binding and poison flags.
8. Request schema/history keys unchanged. Union top-level item is request item; CP1 may bind it to owner/spec item. Version fields are consistency checks only. Rebuilding from captured histories remains load-bearing, not self-attestation.

## Complete exception-object preservation and admission cap

Public builders/evaluator have default retain=None only for conservative refusal. **A parent-owned exact list is REQUIRED before real callbacks** (build U_CALLBACKS_INVALID, eval E_INTERNAL_ERROR when absent). CP1 agreed to strongly own its fresh list BEFORE invocation and retain it across HELD/RELEASED/BaseException even if partial attachment fails. Parent pre-invoke builder likewise owns its list. JSON contains counts/descriptions; actual objects remain in these lists, log.exceptions or partial attributes.

Capacity32, admission stops at30, reserve2 for already-in-flight failures. The triggering object is stored BEFORE stop. IO stops callbacks and diagnostic/hash work, returns MINIMAL/PREBUILT; census poisons and stops acquisition/journal retries. Already-in-flight primary/completion-secondary both remain exact objects. Retention overflow/append failure has a strong overflow slot, independent best-effort external append and nonpositive latch. At interpreter inability to allocate/deliver exceptions the hard boundary applies; no drop-and-continue positive. Interrupted or failed journal publication cannot clear poison.

## Review and SR6 repairs implemented

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

Only exclusive writes, byte hashes, text replacements/diffs/regex. No subject import/AST/compile/tests/execution. All old files untouched. Every v4 control retained, 70 union/28 census/44 endedness/10 hostile metadata/3 native fixtures now frozen, NOT exercised. Review must cover the entire source, exact diff, all controls, notes and failure boundary; partitioned packets may be used with complete coverage manifest. Do NOT review unchanged v4 or run qualification from this source-only delivery.
