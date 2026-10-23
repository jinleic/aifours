# M7 K3 — Gate G2: C411 on encoders A and B

Parent recorded at 2026-10-18T10:57:25-07:00.

**G2 ACCEPTED: both exact C411 cube CNFs are UNSAT by parent-replayed DRAT evidence.** This discharges K3-COMPOSITION Link9 at its formula-level scope. With G1 it supplies the two cube-CNF premises used by the conditional cut transport; it does not by itself close C311, K3 or M(7).

| Encoder | Exact CNF SHA256 | Accepted parent evidence |
|---|---|---|
| A | `2b92f5b15cd641e4a07ecec241b7957deac972aa3c7333056ff3e739e46addf2` | [A-cubes verdict](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-k3-A-cubes-parent-verdict-v1.md), SHA256 `0ba3fe4f0e14d17abbb21766523f1a18627cb1ca6178c5bf546d4eec2cb81f97`; parent receipt `308e255ee1ec4c687f1b79db4157a44c3c3ae9fc1b8cffa24b976f8690707442` |
| B | `01acf46491feef2fc26060266af8c2dead0cec9832c9e9ecbed83f886ecb8bf8` | Fresh attempt B_C411-p3: [RESULT](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-k3-B-cube-parent-replay-v1/RESULT.B_C411-p3.json), SHA256 `e1ef46d1249b9cc3dcb6a220cce0d744f75459d03cfe2b9b1cdd573925e189f0`; [receipt](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-k3-B-cube-parent-replay-v1/receipts/B_C411-p3.json), SHA256 `c176b738bdafddf286896dd917a67edf9175bca6535fe0f174c743a867440ab1` |

## Parent audit of B/C411
[Raw evidence audit](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-B-C411-parent-audit-v1.json), SHA256 `9850fd8b1be897e4a55366513c9247fc3bb3aa4af66daf4f25a1c212e5020e12`. The parent re-hashed all referenced receipts, raw logs, scripts, pinned input files and binaries, then checked:
- regenerated CNF identity:31,379,006 bytes, `p cnf 461370 1629802`, exact pinned SHA; complete solver and checker feeds match that identity;
- kissat4.0.4 self-exit20, singleton exact `s UNSATISFIABLE`; parent drat-trim self-exit0, singleton exact `s VERIFIED` after removing only CR; no NOT VERIFIED/TIMEOUT;
- recorded scripts agree at admission, pre-execution and run end; binaries match at spawn, after execution and assembly;
- all43 assembly conditions, clean supervisor completion and native reaping, no signal/stop/quarantine, and slot release;
- existing transport controls and generation precheck are hash-bound and reused, not rerun.

The pipeline ran09:44:03–10:53:35, 4,172.606seconds. The checker reports consuming1,072,845,839 proof bytes. Its input was the fresh solver's FIFO proof stream, **not** a retained producer proof; this runtime does not record a proof-stream digest. No proof-byte identity or retrospective digest is claimed. The A-side limitations in its verdict remain unchanged. These are the existing M7 exact-CNF replay obligations, not the separate stricter n8 provenance protocol.

## Report correction
The immutable [REPORT.B_C411-p3.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-k3-B-cube-parent-replay-v1/REPORT.B_C411-p3.md), SHA256 `cc37da454799410bec0bd5b6c7facc6844a3c4dbcc730c421848a5c377deabd2`, has a stale template sentence at line25 saying both logs are empty. It is false. The raw solver log is16 bytes (`bde6e1eede96772c07c8ce29fd18088863815bd043aa59a06f11f5838cf8a162`); the checker log is479 bytes (`88308e10c51d00670db09844c62838e57fe95ec1234e96f21c5a418de83bf04c`). They contain the exact statuses checked above. The audit records this erratum; no original report or receipt was rewritten.

## Remaining obligations
[K3-COMPOSITION r4](/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/review/K3-COMPOSITION.r4.md), SHA256 `152e13cbd6815ba54489bdf3d62857451f51514f0b34e52b2de1a7967d777b3e`, supplies the named link interface. Turning these CNF facts into statements about genuine QLS triples still uses its accepted normalization, Gram necessity and conditional encoder-instantiation lemmas. Both A/B C311+cuts replays and final composition acceptance remain mandatory.

The interrupted B_C411-p1 stays UNKNOWN; disarmed gate-only B_C411-p2 stays NOT_STARTED. Neither contributes to G2. [Desk deviations](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-k3-B-cube-parent-replay-v1/deviations-B_C411-p3.json) remain part of the evidence. No novelty, complete K3, or M(7) verdict is made here.
