# Sun k7 Stage A: mathematical replay complete, promotion held

Recorded at 2026-10-18T16:40:49-07:00.

**NOT PROMOTED: K5.3 remains OPEN in the accepted result ledger.** X1/MSP45/CORE5 were fully verified by independent checker v1 and by a parent rerun, but the audit found a terminal-stop/publication status defect. The source repair is frozen; its required terminal controls and positive replay have NOT_STARTED because free disk is below admission. No claim that the underlying mathematics was refuted.

## Evidence already obtained

- [Independent RESULT](sun-coset7-stageA-independent-v1/RESULT.json), SHA256 `72bab5023f7f81649c738b6abc27caf3221160ff270c16889caa919f4c07055f`: X1/MSP45/CORE5 COMPLETE_VALID; genuine group controls PASS;19intended-reason mutations rejected,2benign accepted. No producer code was read/imported/executed by the checker author.
- [Parent replay receipt](sun-coset7-stageA-parent-replay-v1/replay-receipt.json) and [comparison addendum](sun-coset7-stageA-parent-replay-v1/comparison-addendum.json): parent pinned16outputfiles plus definitions/receipt/engine-hash-only source and ran checker v1, exit0, all three COMPLETE_VALID and controls PASS. Result differences are timing/input paths only. This reuses one independent implementation, not a second checker.
- [Codex static audit](sun-coset7-stageA-checker-codex-v1.note.md), SHA256 `81ab8c60d35dd6d9c3c2ad556d5123f78a0e5d34e788768882a4dfe2f2526d8f`: SOUND for the mathematical implication on a genuine clean complete execution. It confirms unbounded CAP coverage, role orbits, full alpha walk, all-q VFC, PB/RPLP and pin handling. MAJOR publication hazard: final guard.sample can set STOP after overall is decided; late SIGTERM likewise need not change exit0. MINOR uneven cooperative checkpoints remains.

## Frozen repair; no runtime claim

- [checker_v2.py](sun-coset7-stageA-independent-v1/checker_v2.py), SHA256 `5b285da4078c9047917af637751872de6f5abe5645f3e2b0ca18500e86a3f2cf`.
- [Exact delta](sun-coset7-stageA-independent-v1/checker_v1-to-v2.diff), SHA256 `64e4a8de4338a1d3a4944210273af7b57f0f6e24c47876b26ac163bb950cc289`.
- [Frozen controls/commands manifest](sun-coset7-stageA-independent-v1/manifest_v2.json), SHA256 `e0252b6bf1970176ad4ee01e587d7280c211b94c6203a5b1b2fdf1601f8e0629`.
- [Worker HOLD receipt](sun-coset7-stageA-independent-v1/RESULT-v2-HOLD.json), SHA256 `7da8d5a1f46adb0f9839b63ae74cfd662c799fc6eba5e6e80b6013656dd9750d`.
- [Parent static scope check](sun-coset7-stageA-v2-parent-static-scope-v1.json): all original mathematical/parser/pruning/Guard top-level ASTs unchanged; only VERSION/main and new terminal publication helpers differ. SIGTERM masking, pending checks, UNKNOWN/3, fsynced output, cancellation marker and default-disposition final unblocking are inspected statically only.

The nine v2 terminal controls, seven sensitivity runs against v1, and the positive v2 full replay are NOT_STARTED. No harness or checker behavior is claimed from source inspection. The v1 complete outputs remain evidence, but do not bypass the requested repair-and-replay gate.

## Resource and process boundary

Admission requires fresh≥12,216,777,216B. Worker readings were11,459,792,896B at15:24:54;10,834,374,656B at15:29:06;9,313,492,992B at15:34:38;8,844,410,880B at15:35:31. Parent read4,384,600,064B at16:39:56. No automatic retry is authorized; if capacity recovers before17:29, a separate parent GO is required. No disk cleanup/deletion was authorized.

Late CERT-FORMAT/RPLP freezing remains permanent F-1, irrespective of any later acceptance. checker_v2 was created by cp-n then edited before freezing, not create-once; disclosed. A sleep/df recheck was cancelled after the no-poll instruction; it ran no checker. The original v1/math proofs remain unchanged.

## Scientific frontier

Accepted [StageB](sun-coset7-stageB-classes-parent-verdict-v1.md) excludes K5.2* (including D2′) and KII. K7, K6.2*, K6.3 and K5.3 remain OPEN. K7's accepted written reductions are in the structure, BLOCK/PAIR, Q5+ and unmarked verdicts; they do not close K7. No Sun(7), novelty, Lean or human-review claim.

Exact restart obligation: preserve all current files, satisfy a fresh resource gate and cutoff, run the frozen terminal controls with their intended outcomes, run positive v2 once, parent-audit observed exits/cancellation markers/full coverage, and issue a NEW disposition through the already accepted X1⇒K5.3 bridge. This is not scheduled or authorized by this note.
