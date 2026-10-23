# PA19 R8 subcase binding (parent task PA19SubcaseBinding)

Append-only checkpoint log. Host-clock timestamps from date. Formula binding only; no UNSAT acceptance; PA(19,8,6) undecided.

- 2026-10-17T14:45:32-0700 created directory (exist_ok=False). RELEASE received from Main (2 production slots free since 14:37:47). Reading R5/R6 receipts, audits, live lane L and snapshot S; writing driver next.
- 2026-10-17T14:56:07-0700 pin start (driver 5a819d32a15f3e0a4b2f9a89b73c3c9b9ac6b7e3edc8a65bd7471b8186043c10)
- 2026-10-17T14:56:09-0700 pin done: 25711 records (a3/single/=17438, a3/single/exact=16, a3/single/r2=1, a3/single/r3=1, m2part_drat/batch/=69, part/batch/=3569, part/batch/r2=1, part/batch/r3=1, part/single/=4615), struct_ok 25711, structural failures 0, unbound-range 0; pins.json sha 238aa310a01169f7f188630a6d1f955f4b604af1ce5fed6fc6be8bd004a280a2
- 2026-10-17T14:56:26-0700 sample frozen: 374 items (20 reruns, 18 rerun originals, 338 ordinary sample), sample-manifest.json sha 943d5a0c86f1e85f327cd815bde47b6c2bd6e7ce4e3f26db6567acc28bad1f18; no CNF generated yet
- 2026-10-17T14:56:34-0700 run run-001 start (manifest 943d5a0c86f1e85f, already done 0)
- 2026-10-17T14:57:11-0700 run run-001 end: complete, 380 evaluated, {"cpu_user_s": 36.41, "cpu_sys_s": 0.7, "maxrss_bytes": 415531008}
- 2026-10-17T14:57:33-0700 finalize: verdict PASS; items {'PASS': 374}; sample {'PASS': 338}; reruns {'PASS': 20}; controls ok True; late 0 changed 0 removed 0; result sha 594e1998839c47af7786dc944ff98415dad325e531fe04f925f45a7b59552377
- 2026-10-17T15:04:07-0700 pin-records: 374 of 374 frozen-selection records copied byte-exact to pinned-records/ (manifest pinned-records.sha256 faa1fcef0b1567d09d1e620289778066a4c798a3a49e040cd0e66d5a8275b028); skipped 0 []; main receipt 594e1998839c47af7786dc944ff98415dad325e531fe04f925f45a7b59552377 unchanged
- 2026-10-17T15:04:10-0700 late inc-001 start
- 2026-10-17T15:04:27-0700 late inc-001: listing 2026-10-17T15:04:10-0700..2026-10-17T15:04:10-0700, late 253 ({'FORMULA_EQUAL_LIST_UNVERIFIED': 253}), changed 0, removed 0; inc-result.json sha 6f510d81a8b2f500a8b87465d0e5ddc04c6f48e90cb5359214ead1f195726483
- 2026-10-17T15:04:53-0700 closeout: main receipt subcase-binding-result.json (sha 594e1998839c47af7786dc944ff98415dad325e531fe04f925f45a7b59552377, verdict PASS on the frozen selection of 374 records: 20 reruns + 18 originals + 338 sampled; formula binding only); late census incremental/inc-001 (inc-result.json sha 6f510d81a8b2f500a8b87465d0e5ddc04c6f48e90cb5359214ead1f195726483: 253 ms06_s00150 batches FORMULA_EQUAL_LIST_UNVERIFIED, i.e. PENDING an R6-style extend_p1q replay). Scripts made read-only (bind_subcases.py 5a819d32..., incremental_bind.py 0a25645d...). No solver/checker/CNF/proof files; no UNSAT acceptance; PA(19,8,6) undecided.
