# M7 K3 — encoder-A C311 with cuts: parent exact-CNF verdict v1

Recorded at 2026-10-18T11:06:26-07:00.

**ACCEPTED UNSAT for the exact encoder-A C311+cuts CNF.** The parent has re-solved the formula and checked a fresh kissat DRAT proof with the parent drat-trim. No B-side C311+cuts, full K3, or M(7) conclusion follows yet.

- Formula SHA256 `18583aabb486b2d7fdf2159ed2172c9dfc9b29bbd2e50c63a5d7d94d44ba2e5e`,24,477,803 bytes, header `p cnf 107513 897308`.
- [Receipt](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-k3-B-cube-parent-replay-v1/receipts/A_C311cuts-p2.json), SHA256 `59b27e911837fea015ca021c233b8ea6ad2a6e0f95d63d3615ad1b2996c569b4`; [RESULT](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-k3-B-cube-parent-replay-v1/RESULT.A_C311cuts-p2.json), SHA256 `51470bce8e0a67ad7a3be71bcf89c101389cd15f8545a8346a74117df42fcd76`.
- [Parent raw audit](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-A-C311cuts-parent-audit-v1.json), SHA256 `73660641dbadab97e195b59beeffaf445261d57c88739564117f71eea2f3e306`: all43 conditions, regenerated CNF/both complete measured feeds, exact native self-exits20/0 and singleton UNSATISFIABLE/VERIFIED lines, raw-log hashes, source/binary identity, clean supervisor completion and token/slot settlement. No stop, signal or quarantine.
- Pipeline09:39:16–10:58:29,4,753.8seconds. Checker reports consuming705,539,296 proof bytes. Proof stream is not retained or hashed; no retrospective digest or equality with the producer's proof is claimed.
- The producer used CaDiCaL and a lane checker; this parent run used kissat and the independently built parent drat-trim. Different checker/proof statistics are expected and are not an acceptance criterion.

## Mathematical boundary
This is the formula-level evidence for K3-COMPOSITION r4 Link12. Using its cuts for genuine C311 triples additionally requires the accepted G1/G2 cube facts and the scoped cut-transport/normalization/encoder-necessity lemmas. [G1](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-k3-G1-parent-verdict-v1.md) and [G2](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-k3-G2-parent-verdict-v1.md) are accepted; encoder-B C311+cuts and the final composition reconciliation remain mandatory.

The r14 script identity, reused transport controls and historical deviations are recorded in the [desk report](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-k3-B-cube-parent-replay-v1/REPORT.A_C311cuts-p2.md) and [deviations](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-k3-B-cube-parent-replay-v1/deviations-A_C311cuts-p2.json). The report's line25 fixed template claiming empty logs is false: actual solver/checker log sizes16/475bytes, with exact statuses and hashes checked by the parent audit. Frozen reports are not rewritten.

Earlier stopped/disarmed attempts remain UNKNOWN/NOT_STARTED and are not counted. No novelty claim. Exact finite computation trusting the stated software/hardware, not Lean.
