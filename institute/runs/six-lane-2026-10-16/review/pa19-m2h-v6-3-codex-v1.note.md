| Scope | Disposition |
|---|---|
| Supervisor v6 / transport v6_3, as used by M2H | **GO — source acceptance** |
| M2H pilot admission | **HOLD — outstanding operational prerequisite** |

All **32 SHA256 hashes and byte counts match**. Review used snapshot reads and hashes only.

The three previous defects are **fixed**:

- **MAJOR 1 — late cancellation:** [SOURCE02:423](./pa19-m2h-v6-3-review-v1/snapshot/02-supervise_pa19_v6.py:423) saves the old mask and blocks SIGTERM/SIGINT through final checking, record publication and handler restoration; line453 restores the old mask afterward. In this single-threaded path, pending signals reach the restored outer handler, without post-publication signal-field mutation. Owner cancellation becomes UNKNOWN with a persistent veto at SOURCE09:164–172; SOURCE10:75–76 rejects signal/cancellation evidence. SOURCE20:335–348 blocks publication around its final cancellation check, and lines225–227 reject cancelled UNSAT records.
- **MAJOR 2 — omitted admission:** [SOURCE20:61](./pa19-m2h-v6-3-review-v1/snapshot/20-run_m2h_v6_3.py:61) applies one predicate to all five admissions, requiring the correct phase, frozen cutoff and strictly earlier timestamp. UNSAT requires all five admitted; the exact reader invokes this predicate at line223.
- **MINOR 3 — exclusion census:** SOURCE20:156–189 enforces unique item/direct identities, exact split partitions, unique exclusions, disjointness and **covered ∪ excluded = skeleton universe**.

**No remaining BLOCKER/MAJOR source defect found in the audited M2H path.** Exact and normalized deltas agree on the substantive changes. Delayed-reap sampling before each poll, unreaped-only group signalling, frozen clocks and cleanup reservation, singleton operation, disk gates, sampled resource limits, and measured contract/pin/commit/runner/coverage/denominator/supervisor bindings remain intact.

The supplied receipts report **15/15 adapter controls**—12 v6 cases plus three baseline comparisons—and **46/46 M2H controls**. P6 observes identical published/returned JSON and one restored-handler call. Delayed-reap timing is injected; M2H uses named stubs and starts zero native children. These are private observed control results, **not live kernel-race reproduction or successful native qualification**. The 5,580-match census establishes formula binding only.

**MAJOR operational prerequisite, blocking pilot admission:** [SOURCE00:40](./pa19-m2h-v6-3-review-v1/snapshot/00-previous-HOLD-v6_2.note.md:40) requires a later parent notice that **M1 retry543 ended with its owned groups quiescent**. None is supplied. SOURCE31’s gate preview does not establish that release. **Fix:** supply that notice and fresh accounting/admission evidence; this snapshot cannot establish M1’s current state.

After release, permit only one bounded M2H pipeline pilot demonstrating the actual **publisher → exact reader → inventory** path. Split-path runtime evidence remains necessary before expansion. This grants no PA19/M2 completeness claim or M6/M9/E0 resumption.