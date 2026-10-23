# M7 K3 — encoder-B C311 with cuts: parent exact-CNF verdict v1

Recorded at 2026-10-18T12:09:07-07:00.

**ACCEPTED UNSAT for the exact encoder-B C311+cuts CNF.** A fresh parent replay regenerated the formula, re-solved it with kissat, and checked its streamed DRAT proof using the parent drat-trim build. Both C311+cuts formula obligations are now accepted. **The final genuine-configuration-to-formula composition remains mandatory; this verdict does not yet determine M(7).**

- Formula SHA256 `ae3b8309601d115e2258782ae3cb793f4dc4b5950064b9536b1eca61521f783a`, 38,353,647 bytes; header `p cnf 461370 1867942`.
- [Attempt receipt](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-k3-B-cube-parent-replay-v1/receipts/B_C311cuts-p2.json), SHA256 `edfbb2f134615fe3f6c09ab24ef52b5b4f13702ce357904625a71a1fc380241e`; [assembled RESULT](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-k3-B-cube-parent-replay-v1/RESULT.B_C311cuts-p2.json), SHA256 `45eee709b8c4fe5a1438a8930da908379ef17ecf9351d1795a94fbd3468fc3f5`.
- [Independent parent raw audit](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-B-C311cuts-parent-audit-v1.json), SHA256 `024e636da51941a0bdbf8ebb62c35ea6ca02ca9f77c1a4eb52bb4d90a349cab9`: all 43 assembled conditions true, with 39 grouped parent predicates independently checking raw receipt hashes, measured CNF feeds, native exits, literal status lines, raw logs, source/binary identities, admission, supervision and release. No stop, signal, quarantine or remaining owned child is recorded.
- Both measured feeds wrote all 38,353,647 bytes with the bound CNF digest. Solver self-exit 20 with exactly `s UNSATISFIABLE`; checker self-exit 0 with exactly `s VERIFIED` after removing CR only. Neither log contains NOT VERIFIED or TIMEOUT.
- Pipeline 2026-10-18 10:55:09–12:05:22 PDT, 4,212.783 seconds. Solver wall time 2,245.714 seconds. The checker reports consuming 842,063,946 proof bytes.
- **Proof provenance boundary:** the proof stream has no recorded digest and is not retained. No proof-byte identity with the producer is claimed or reconstructed. This is the existing M7 exact-CNF protocol, not n8's stricter stream-digest protocol.
- Raw solver/checker logs are 16/478 bytes, with hashes `bde6e1eede96772c07c8ce29fd18088863815bd043aa59a06f11f5838cf8a162` / `d55db210e80e07230ffe01610b0b3edd252f08d7ea583e4a2fc53711419130f2`.

## Composition boundary

This discharges the exact formula replay in K3-COMPOSITION r4 Link 13. The [A/C311+cuts verdict](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-k3-A-C311cuts-parent-verdict-v1.md), [G1](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-k3-G1-parent-verdict-v1.md) and [G2](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-k3-G2-parent-verdict-v1.md) remain in force. Their cut-transfer, normalization and encoder-necessity premises must be reconciled in the frozen r5 composition and both-family final reviews before any K3 or M(7) conclusion.

## Preserved deviations and corrections

- [REPORT.B_C311cuts-p2.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-k3-B-cube-parent-replay-v1/REPORT.B_C311cuts-p2.md) line 25 falsely says both logs are empty. The raw byte counts above govern; the frozen report is unchanged.
- [Recorded deviations](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-k3-B-cube-parent-replay-v1/deviations-B_C311cuts-p2.json), SHA256 `948c4b3167a47b1b9f074e6c4705ed6436c7cce0e207b163024ec397123bcdfa`. The earlier interrupted B/C311cuts-p1 remains UNKNOWN; no retrospective upgrade.
- The parent's first audit compared the gate's RSS-cap object to a scalar and stopped before acceptance. [Failed audit](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-B-C311cuts-parent-audit-attempt1-UNKNOWN.json) is retained. Reading `gate.rss_cap.value` gives the same 2,797,076,480-byte cap as the supervisor and driver. No scientific replay was repeated.
- **A-side reporting clarification:** the A/C311cuts parent audit labels the checker's 466 CR-normalized bytes as “raw_log_bytes”. Its actual raw log is 475 bytes (SHA256 `4fb0b9a94ddd41d4222c7a04dc9fbbf014c811a6af19ab39ec94239db6de9348`), as the A-side verdict already states. This is a byte-count label correction only; statuses and input/proof-check outcomes are unchanged.

Exact finite computation trusting the recorded toolchain and hardware, not Lean. No novelty claim or publication.
