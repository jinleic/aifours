# Deviation record — worker GB FIFO node unlinks (append-only, r1)

Recorded 2026-10-18T09:37:40.642441-07:00 at the parent's request. The parent found `os.unlink(fifo)` in frozen `gb_direct_r6.py` LF532. Deleting generated FIFO nodes is prohibited by the run's no-deletion rule, even though no proof or CNF bytes were ever at rest in them.

This record identifies every executed unlink in the lane's worker GB code. It does NOT:
- change any receipt, log, summary or code file;
- claim compliance;
- reconstruct any deleted node;
- change any scientific status.

## What was deleted
- **Artifact type:** FIFO node only. Each was a named-pipe inode with zero data bytes at rest, created by the worker pipeline and used to carry the kissat DRAT stream from the solver to the relay/collector. Proof bytes passed through it transiently and were hashed and counted by the relay or collector.
- **When:** each pipeline unlinked its own FIFO after joining the relay or collector threads.
  - In concurrent-transport runs (r1–r4), and in every `control_mismatch` control, this happened after both natives had exited.
  - In the staged r6 runs the order differs: `pipeline_staged` LF532 unlinked its FIFO after stage 1 (kissat) had finished and its collector thread had been joined, before stage 2 (drat-trim) started.
- **Nothing else was deleted.** In particular, no CNF, proof, log, receipt or other file.

## Executed unlink sites: 24 FIFO nodes in 6 executions
| Run directory | Script (SHA256) | Unlink site | Item | FIFO path (deleted) | Unlink before | Item receipt (outcome) |
|---|---|---|---|---|---|---|
| gb_probe_v1 | `code/gb_probe_r1.py` (`b4c6ca46930bc8a61c03024588b3d8152602466c9d44af42c94b4b542c32b483`) | pipeline LF250 | ctl-tiny-unsat | `L/evidence/gb_probe_v1/fifo/ctl-tiny-unsat.drat.fifo` | before 2026-10-18T07:55:58.014707-07:00 | receipt `20d90e3c85c03bfcb1f6831f20e8c66d2ed6ade08a95b223b011e21c4b97f2f3` (PASS) |
| gb_probe_v1 | `code/gb_probe_r1.py` (`b4c6ca46930bc8a61c03024588b3d8152602466c9d44af42c94b4b542c32b483`) | control_mismatch LF377 | ctl-sat-checker | `L/evidence/gb_probe_v1/fifo/ctl-sat-checker.drat.fifo` | before 2026-10-18T07:55:58.035927-07:00 | receipt `d225d9b8da6780f927249fc524ec6368248491c250023ee5c41b88a9b436e483` (control_ok) |
| gb_probe_v1 | `code/gb_probe_r1.py` (`b4c6ca46930bc8a61c03024588b3d8152602466c9d44af42c94b4b542c32b483`) | pipeline LF250 | GB-P1-B4 | `L/evidence/gb_probe_v1/fifo/GB-P1-B4.drat.fifo` | before 2026-10-18T07:59:14.353531-07:00 | receipt `052699927c71c2db6a2afcdb8c5ec982aa90343597bd4dbc77305182fee2867c` (FAIL) |
| gb_probe_v2 | `code/gb_probe_r2.py` (`1cb4406214a720fe9b2ae64a32cf42f17fe2c59ab0466302fa0edbe276c0806e`) | pipeline LF287 | ctl-tiny-unsat | `L/evidence/gb_probe_v2/fifo/ctl-tiny-unsat.drat.fifo` | before 2026-10-18T07:59:51.973135-07:00 | receipt `39d89860c0159181e2b9232f418fca30aa917ef034734948bf3567fbb3727161` (PASS) |
| gb_probe_v2 | `code/gb_probe_r2.py` (`1cb4406214a720fe9b2ae64a32cf42f17fe2c59ab0466302fa0edbe276c0806e`) | control_mismatch LF415 | ctl-sat-checker | `L/evidence/gb_probe_v2/fifo/ctl-sat-checker.drat.fifo` | before 2026-10-18T07:59:51.994090-07:00 | receipt `011d5ae0c2b9cd6d4a888dcd32a814bcc50fe73f19f42b2892107c867e7a13cc` (control_ok) |
| gb_probe_v2 | `code/gb_probe_r2.py` (`1cb4406214a720fe9b2ae64a32cf42f17fe2c59ab0466302fa0edbe276c0806e`) | pipeline LF287 | GB-P1-B4 | `L/evidence/gb_probe_v2/fifo/GB-P1-B4.drat.fifo` | before 2026-10-18T08:03:06.872522-07:00 | receipt `f82d10d572a8ba61b3c41fdd129710790f5c81c1e3e988f791b010315472b15b` (PASS) |
| gb_probe_v2 | `code/gb_probe_r2.py` (`1cb4406214a720fe9b2ae64a32cf42f17fe2c59ab0466302fa0edbe276c0806e`) | pipeline LF287 | GB-P0-B3 | `L/evidence/gb_probe_v2/fifo/GB-P0-B3.drat.fifo` | before 2026-10-18T08:14:30.436888-07:00 | receipt `c04f40984fd2e72bfaf4043d653058f6f2dcce4c0a8418f76f008448f5003bf7` (PASS) |
| gb_direct_v3/run-a1 | `code/gb_direct_r3.py` (`619cc455ebcef2f44f06d9de528c8cb1b35c1209e114daef81c072a425b56e07`) | pipeline LF370 | ctl-tiny-unsat | `L/evidence/gb_direct_v3/run-a1/fifo/ctl-tiny-unsat.drat.fifo` | before 2026-10-18T08:20:25.866149-07:00 | receipt `4f143809afdce7e595d6c725fae295349452fb637b11b3bb28179c2b9b685d4a` (PASS) |
| gb_direct_v3/run-a1 | `code/gb_direct_r3.py` (`619cc455ebcef2f44f06d9de528c8cb1b35c1209e114daef81c072a425b56e07`) | control_mismatch LF515 | ctl-sat-checker | `L/evidence/gb_direct_v3/run-a1/fifo/ctl-sat-checker.drat.fifo` | before 2026-10-18T08:20:25.888329-07:00 | receipt `146026a4a46dd1a387b705aadb3ca1ffb298f1a35c627758a530b828b559cda5` (control_ok) |
| gb_direct_v3/run-a1 | `code/gb_direct_r3.py` (`619cc455ebcef2f44f06d9de528c8cb1b35c1209e114daef81c072a425b56e07`) | pipeline LF370 | GB-P1-B4 | `L/evidence/gb_direct_v3/run-a1/fifo/GB-P1-B4.drat.fifo` | before 2026-10-18T08:23:39.947121-07:00 | receipt `934ac38391903abb15ce890dd7e015f189f70b42bcbc7830deb69ec95c94424e` (PASS) |
| gb_direct_v3/run-a1 | `code/gb_direct_r3.py` (`619cc455ebcef2f44f06d9de528c8cb1b35c1209e114daef81c072a425b56e07`) | pipeline LF370 | GB-P0-B4 | `L/evidence/gb_direct_v3/run-a1/fifo/GB-P0-B4.drat.fifo` | before 2026-10-18T08:26:45.276167-07:00 | receipt `e1188c2c918e40e08acb2d63758c4a6b82cecdfed4bc36c10988414904028d06` (PASS) |
| gb_direct_v4/run-b1 | `code/gb_direct_r4.py` (`80d731fed0b108b9be98be2ce951a15d99914a7bc48b32a765d0d192ee8180c0`) | pipeline LF375 | ctl-tiny-unsat | `L/evidence/gb_direct_v4/run-b1/fifo/ctl-tiny-unsat.drat.fifo` | before 2026-10-18T08:26:59.062699-07:00 | receipt `bba2ad0be2e8c256f8474e007a8afc3ddf91d44917ce58766f26ad614b1011f2` (PASS) |
| gb_direct_v4/run-b1 | `code/gb_direct_r4.py` (`80d731fed0b108b9be98be2ce951a15d99914a7bc48b32a765d0d192ee8180c0`) | control_mismatch LF523 | ctl-sat-checker | `L/evidence/gb_direct_v4/run-b1/fifo/ctl-sat-checker.drat.fifo` | before 2026-10-18T08:26:59.082892-07:00 | receipt `14d08d89f77c5b23051a8897525146bfff760a5826f7e1b2593dd0b7ea8eb6ce` (control_ok) |
| gb_direct_v4/run-b1 | `code/gb_direct_r4.py` (`80d731fed0b108b9be98be2ce951a15d99914a7bc48b32a765d0d192ee8180c0`) | pipeline LF375 | GB-P0-B5 | `L/evidence/gb_direct_v4/run-b1/fifo/GB-P0-B5.drat.fifo` | before 2026-10-18T08:30:12.124877-07:00 | receipt `975af5b2867e38e9435f0bbf436780374e8d6dea941e5e7ed7a617d11ef12647` (PASS) |
| gb_direct_v4/run-b1 | `code/gb_direct_r4.py` (`80d731fed0b108b9be98be2ce951a15d99914a7bc48b32a765d0d192ee8180c0`) | pipeline LF375 | GB-P0-B6 | `L/evidence/gb_direct_v4/run-b1/fifo/GB-P0-B6.drat.fifo` | before 2026-10-18T08:37:34.235119-07:00 | receipt `ec8d10a675731720a91294519414c9f420c7f4ea423bd5e4037878aa991e1631` (PASS) |
| gb_direct_v4/run-b1 | `code/gb_direct_r4.py` (`80d731fed0b108b9be98be2ce951a15d99914a7bc48b32a765d0d192ee8180c0`) | pipeline LF375 | GB-P1-B6 | `L/evidence/gb_direct_v4/run-b1/fifo/GB-P1-B6.drat.fifo` | before 2026-10-18T08:44:26.968229-07:00 | receipt `89b2bbce3df45fd017b5e1c71c10683f4d28b1154a678a58397fade60db1fca7` (PASS) |
| gb_direct_v4/run-b2 | `code/gb_direct_r4.py` (`80d731fed0b108b9be98be2ce951a15d99914a7bc48b32a765d0d192ee8180c0`) | pipeline LF375 | ctl-tiny-unsat | `L/evidence/gb_direct_v4/run-b2/fifo/ctl-tiny-unsat.drat.fifo` | before 2026-10-18T08:44:42.979859-07:00 | receipt `04387c6d65b2cd84f968c25fb444f6380aa0302de1f94f6177d4307355d8a70f` (PASS) |
| gb_direct_v4/run-b2 | `code/gb_direct_r4.py` (`80d731fed0b108b9be98be2ce951a15d99914a7bc48b32a765d0d192ee8180c0`) | control_mismatch LF523 | ctl-sat-checker | `L/evidence/gb_direct_v4/run-b2/fifo/ctl-sat-checker.drat.fifo` | before 2026-10-18T08:44:43.000487-07:00 | receipt `545483d0108e654a57e022667b3bc60828aff12939ba18cdba0f589f09860f7b` (control_ok) |
| gb_direct_v4/run-b2 | `code/gb_direct_r4.py` (`80d731fed0b108b9be98be2ce951a15d99914a7bc48b32a765d0d192ee8180c0`) | pipeline LF375 | GB-P2-C4 | `L/evidence/gb_direct_v4/run-b2/fifo/GB-P2-C4.drat.fifo` | before 2026-10-18T08:49:30.604048-07:00 | receipt `e36d1c0d171bd32dcd00f3d7e0ede1c7725a473bef44dfdbcd04e57481650847` (PASS) |
| gb_direct_v4/run-b2 | `code/gb_direct_r4.py` (`80d731fed0b108b9be98be2ce951a15d99914a7bc48b32a765d0d192ee8180c0`) | pipeline LF375 | GB-P2-C3 | `L/evidence/gb_direct_v4/run-b2/fifo/GB-P2-C3.drat.fifo` | before 2026-10-18T08:53:59.005254-07:00 | receipt `9255aaeb018c580778284bff4ae22f9ab0cac767ad4fd2231e15b009bdaaa793` (PASS) |
| gb_direct_v4/run-b2 | `code/gb_direct_r4.py` (`80d731fed0b108b9be98be2ce951a15d99914a7bc48b32a765d0d192ee8180c0`) | pipeline LF375 | GB-P0-B1 | `L/evidence/gb_direct_v4/run-b2/fifo/GB-P0-B1.drat.fifo` | before 2026-10-18T08:53:59.742545-07:00 | receipt `77145d848e30af3e54cfe507d423d8545654380b8d4fded5bfac92cdc30b63eb` (STOPPED_UNKNOWN) |
| gb_direct_v6/run-c1 | `code/gb_direct_r6.py` (`89fa8959fa83467a13f32e4222dcd9ede36c2fec51e4a9ac7f3cef72b78b7032`) | pipeline_staged LF532 | ctl-tiny-unsat | `L/evidence/gb_direct_v6/run-c1/fifo/ctl-tiny-unsat.drat.fifo` | before 2026-10-18T09:00:57.010361-07:00 | receipt `6a89e95b25132655f7b7a1a3242fab63121885216629127293dfa5c752570654` (PASS) |
| gb_direct_v6/run-c1 | `code/gb_direct_r6.py` (`89fa8959fa83467a13f32e4222dcd9ede36c2fec51e4a9ac7f3cef72b78b7032`) | control_mismatch LF709 | ctl-sat-checker | `L/evidence/gb_direct_v6/run-c1/fifo/ctl-sat-checker.drat.fifo` | before 2026-10-18T09:00:57.031477-07:00 | receipt `a6ba84503177bab67147f1b0c8bff23890c30e102b914407e85d286bb63af428` (control_ok) |
| gb_direct_v6/run-c1 | `code/gb_direct_r6.py` (`89fa8959fa83467a13f32e4222dcd9ede36c2fec51e4a9ac7f3cef72b78b7032`) | pipeline_staged LF532 | GB-P0-B1 | `L/evidence/gb_direct_v6/run-c1/fifo/GB-P0-B1.drat.fifo` | before 2026-10-18T09:12:45.807056-07:00 | receipt `bb0a8ffd7903a16618158d1fff989bbe599d6084cb9e3bc9fd96b55c96888f79` (PASS) |

The "Unlink before" column gives the receipt's `finished_at`/`at` timestamp. Each unlink executed within that item, before its receipt was written.

## Not executed (no deletion)
- `code/gb_direct_r5.py`: LF381 and LF532. It was never launched.
- `code/gb_direct_r7.py`: LF392, LF538 and LF715. Frozen, not authorized, never run.
- `code/gb_direct_r6.py` `pipeline()` LF386 is present but unused by r6 `main`. r6 used `pipeline_staged` (LF532) and `control_mismatch` (LF709).
- The worker's eval-kernel transport smoke at about 07:53 created `L/evidence/gb_probe_v1/fifo/smoke.drat.fifo` and did NOT unlink it. The node still exists.
- The r4 run-b1 P2-C4 item and the r3 run-a1 P0-B5 item were NOT_STARTED: no FIFO was created.

## Status consequences
None to scientific status. All of these runs are worker evidence only. Under the parent decision, none is counted, and their PASS, FAIL, STOPPED_UNKNOWN and NOT_STARTED labels are unchanged. The deviation affects only the lane's procedural compliance with the no-deletion rule, which is recorded here as NOT compliant for these 24 FIFO nodes. No further worker native run is authorized, and none will occur, so the unlink code is never executed again. The parent's counted replay preserves spent FIFOs instead (`review/GB_R6_PARENT_HANDOFF.r1.md` §5 is to be read with this record).
