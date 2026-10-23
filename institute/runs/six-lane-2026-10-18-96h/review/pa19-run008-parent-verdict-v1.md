# PA19 run-008: three whole ms06 cases closed (frontier 141 -> 138)

Recorded at 2026-10-19T04:47:02-0700.

**CORRECTNESS-ACCEPTED SCOPED PARTIAL (case-level).** The whole direct cases ms06 b88, b89 and b186 are UNSAT under the lane-original M2 encoding. Frontier v7 has 138 undecided cases: 76 ms06 + 62 ms09. **PA(19,8,6) remains UNDECIDED.** This is not a PA19 verdict and not the measured M2H view.

## Evidence chain
- Parent launch under [GO v21](pa19-pilot-v21-parent-GO-v1.json) (`a1e2aad705eb86583a48665c18ebb52cc44c4969801387dac455bdc238f6d76c`); run directory `/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/pa19/evidence/pilot-v1/run-008`; summary `fff4807e996b8adb37b960b6bfc5f47a29425fe3ccf3bcad86c231ec6fa4f4d0`; 14 children settled; controls C1–C7 at intended outcomes.
- [Raw parent audit](pa19-run008-raw-parent-audit-v1.json) (`c17c324d7cf68a264c2f6efd8c962e059129b32907a979e807c0054a99968db1`): for each item the CNF equals the request/preflight pin (sha, bytes, header); kissat self-exit 20 with exactly `s UNSATISFIABLE`; proof sink complete (received = written = file bytes, sha equal); drat-trim (lane build) self-exit 0 with exactly `s VERIFIED`; checker-consumed proof bytes equal the retained file bytes.
- Provenanced second-build replay (drat-trim build `a46c0c71…`, same DRAT algorithm, not an independent checker) under `owned_supervisor_v2`, each with a fresh stability gate: [b89](pa19-ms06-provenanced-replay-v4/ms06_b00089_direct/parent-audit-v1.json), [b186](pa19-ms06-provenanced-replay-v4/ms06_b00186_direct/parent-audit-v1.json), [b88](pa19-ms06-provenanced-replay-v4/ms06_b00088_direct/parent-audit-v1.json): receipts SETTLED, rc 0, no trips, empty group census; `s VERIFIED`; consumed 50,554,158 / 170,874,376 / 348,478,371 B equal to the retained proofs; inputs re-hashed equal afterwards.
- Case binding: frontier v6 entries b88/b89/b186 carry s_tags ms06_s00241/ms06_s00250/ms06_s00262; the frozen preflight (`c693e4e1b67ecec24eca58b4d05dc42c9cd982c72e25d3fb835d0ec32194c0c2`) regenerated each CNF equal to the runner and evidence pins with equal skeleton fields and whole_case_direct=true. Encoder-to-case completeness remains the previously accepted bridge.

## Disclosures and deviations
- Every checker output (lane and replay) carries 152 drat-trim `detected and deleted duplicate literal` WARNING lines at formula-phase line numbers; disclosed, not a runner defect class.
- GO v21's owner_launch text says "run-006"; the actual parent launch was run-008 under the same items and runner pin.
- Replay chain: an advisory noted the first parent chain advanced unconditionally after each supervisor. The parent placed an exclusive HOLD file at b88's gate path (`a6231fe4102b14025071564aac0fb5536a903a756e4f1c53f176c909c796b3d2`), the chain stopped before b88, and b88 was launched singly after both earlier receipts were checked clean ([addendum](pa19-ms06-provenanced-replay-v4/ms06_b00088_direct/plan-addendum-v1.json)). No guard trip occurred in any replay.

## Frontier
[Frontier v7](pa19-parent-frontier-v7.json) (`64d0cb62a40f260b6492e80dec9898548068292546ced20e53a58397398e3f0b`) supersedes v6 (`64be77f84293f8b4078cecd864a063abfddd2792b458ff0fd23e8b7193c792d0`). It removes only these three cases. Prior UNKNOWN records stay preserved, and the M2H views stay separate and unmerged.
