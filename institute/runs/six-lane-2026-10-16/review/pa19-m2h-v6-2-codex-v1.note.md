| Scope | Disposition |
|---|---|
| Supervisor v5 / transport | **HOLD — blocking MAJOR remains** |
| M2H pilot admission | **HOLD — blocking qualification gap; M1 retry543 also remains active** |

All 49 supplied hashes and byte counts match. Only static snapshot reads, hashes and comparisons were performed.

1. **MAJOR, blocking — late cancellation can still qualify clean.**  
   [SOURCE02:419](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-m2h-v6-2-review-v1/snapshot/02-supervise_pa19_v5.py:419) checks the signal flag before assembling/publishing the record. A signal arriving afterward can leave `completed_cleanly=True`; line446 updates only `observed_signal`. If it arrives before line429, the persisted and returned records can agree on that contradictory state. [SOURCE26:54](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-m2h-v6-2-review-v1/snapshot/26-m2_item_owner_v6_2.py:54) and SOURCE28:73 reject neither `observed_signal` nor owner cancellation. Setting `_CANCEL` stops subsequent work but need not disqualify this item.

   **Fix:** make cancellation finalization consistent through handler restoration/publication, and reject observed signals and owner cancellation in outcome composition and qualification. Add publication-window and settlement-window signal controls. Preserve the prohibition on signalling a reaped PGID.

2. **MAJOR, blocking — qualification omits one admission’s cutoff binding.**  
   [SOURCE10:186](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-m2h-v6-2-review-v1/snapshot/10-run_m2h_v6_2.py:186) scans the two owner gates and solver/checker gates, omitting `native_result.worker_preconstruction_gate`. SOURCE28:107 validates that gate through `gate_errors`, whose checks at lines26–56 contain no cutoff validation. Thus otherwise qualifying evidence can carry a missing/wrong/post-cutoff worker-preconstruction timestamp.

   The **live worker does enforce** the cutoff through SOURCE24:405; this is a reader gap.

   **Fix:** validate the frozen cutoff and timestamp for all five required admissions through one shared predicate. Add isolated negative controls for this omitted gate.

3. **MINOR, nonblocking for this frozen pilot — exclusion census checks cardinality, not domain equality.**  
   [SOURCE10:149](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-m2h-v6-2-review-v1/snapshot/10-run_m2h_v6_2.py:149) permits replacing an excluded case with an arbitrary unique out-of-domain name while preserving every assertion.

   **Fix:** construct the complete skeleton case set and require `covered ∪ excluded == universe`, with disjointness and uniqueness. No malformed excluded entry is demonstrated in the supplied manifest.

| Previous finding | Re-review result |
|---|---|
| 1: delayed reap | Loop repaired: strict sampling, bounded sleeps/polls, unreaped-only stopping and cancellation propagation. Finalization defect above remains. |
| 2: historical qualification | **Fixed:** SOURCE10:169–195 requires measured schema and contract/pin/commit/runner/coverage/historical/list/supervisor bindings. |
| 3: clocks | **Runtime enforcement fixed:** SOURCE10:34,235 and SOURCE22:257,312 enforce the frozen clocks, cleanup reservation and group-budget fit. Reader gap above remains. |
| 4: historical identity | Revision-specific identity, interval, CNF, limit and list checks added at SOURCE10:59–89,127–147. Census caveat above remains. |
| 5: BindingRefusal | **Fixed:** SOURCE26:107–112 returns unattempted without pin/job/group/veto; other constructor failures retain persistent integrity handling. |
| 6: M6/M9 continuity | **Unresolved; PARKED.** Renaming supplies no attempt continuity or resumption authority. |

Independent source comparisons support SOURCE08/09’s semantic delta: seven bodies are rename-only; substantive transport changes concern clocks/cancellation, BindingRefusal and supervisor binding.

SOURCE06 reports **13/13** current supervisor controls. SOURCE07 retains an earlier failed B expectation under a different harness hash. These inject record signatures and safety events; they establish **no live kernel-race reproduction**. SOURCE20 reports **35/35** M2H controls, with named stubs and zero native children; neither publication-window cancellation nor the omitted gate is covered.

The manifest contains **5,393 direct + 187 intervals = 5,580 unique items**, covering **5,424 cases**, plus **82 unique exclusions**. SOURCE18 binds its complete 5,580-match census to SOURCE17 and SOURCE13. Original input bytes remain imports; these are not independently regenerated or native execution results from this review.

The singleton and `--max-attempts` guards are present at SOURCE10:217–226,257,303. Before any future pilot GO: resolve the blocking findings, review the new hashes/immutable contract and targeted controls, obtain the **later parent notice that M1 retry543 ended with owned groups quiescent**, and capture fresh accounting/admission gates. The first bounded pilot must then demonstrate the actual publisher → reader → inventory path; split evidence is still required before broader rollout.

Any eventual acceptance is limited to **one M2H pipeline**. It authorizes no automatic retries, changes to old UNKNOWNs, M6/M9/E0 resumption, or PA19/M2 completeness claim.