**CONTROL SOURCE: GO-WITH-FIXES — BLOCKING.**  
**SCIENCE: HOLD.**

All 14 supplied hashes and byte counts match. Review used snapshot reads and hashes only.

Two **MAJOR** blockers remain:

1. **F4 durability — failed publication remains admissible.** At **[SOURCE02:528](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/n8-gb-staged-v3-delta-review-v1/snapshot/02-runtime-gb_staged_v3.py:528)–534**, `os.link()` exposes the already-serialized `qualified: true` commit **before** the final directory sync. An EIO or other exception afterward leaves those bytes unchanged. **2815–2829** marks only the run entry unqualified and stops. Admission at **1332–1352** ignores that failure and accepts the commit. Thus failure on the seventh control can leave all seven admissible.  
   **Required:** admission must reject failed or incomplete publication, using completion evidence bound to the commit. Cover post-link directory-sync/full-sync/close failures and interrupted completion.

2. **F4 cancellation — the repair weakens the previous requirement, and misidentifies its boundary.** **[SOURCE02:519](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/n8-gb-staged-v3-delta-review-v1/snapshot/02-runtime-gb_staged_v3.py:519)–527** samples pending signals before `active_count()`, `decided_at`, commit construction and serialization. A signal after that snapshot can leave qualification true, including before the recorded decision time or link. H8 explicitly accepts a signalled publication (**SOURCE04:1453–1468**). That does not close the earlier serialization/publication cancellation finding (**SOURCE00:12–13; SOURCE12:27**).  
   **Necessary rule change if retaining this design:** explicitly authorize qualification to linearize at one precisely identified protected cancellation snapshot; signals observed before it veto the item, while arrivals afterward—including during serialization, link and directory sync—only stop subsequent work, provided publication ultimately succeeds. Align code and documentation with that actual operation. Without this amendment, preserve the previous cancellation semantics.

Disposition of the three previous blockers:

| Previous finding | Judgment |
|---|---|
| Scalar FD acquisition | **Closed.** Scalar ownership precedes registration; rollback and registry cleanup have distinct ownership (**SOURCE02:1729–1767; 2064–2068; 2124–2127**). D9h injects registration `MemoryError` at all three single-FD sites (**SOURCE04:745–761**). |
| Protected publication | **Not closed**, as above. Base preparation, masking, pending/thread checks, non-overwriting link and mask restoration are implemented. |
| Receipt/commit durability | **Partial; not closed.** Unbuffered writes, `fsync`, macOS `F_FULLFSYNC`, and directory syncing are real calls (**SOURCE02:473–503**), unmocked in supplied H1. Receipt/pre-link failures reject qualification; post-link failure does not. |

The retained results contain **v3b 85/85** passes and **v3 81/82**, with the removed-`acquire` hook failure preserved (**SOURCE10:552–555**). Coverage remains insufficient: H5 signals before the protected decision, H7 injects pending SIGINT, H8 injects SIGTERM after linking; H9 fails only the first receipt fsync, and H10 fails the link itself (**SOURCE04:1399–1500**). Missing checks include both signals during commit serialization/before link, the snapshot-to-`decided_at` gap, prepared-commit durability failures and post-link EIO.

No regression found in the closed v2 obligations: independent native-failure vetoes/seven control outcomes, reaped-child safety, scanner/exclusion latches, exact feeds/digests/EOF/counts, disk gates/deadlines and GA exclusion. The control expectations remain consistent with SOURCE11’s parser.

**Science remains blocked** until repaired source is cleared, all seven native control receipts **and qualified commits** are independently audited, then each science item receives explicit GO.