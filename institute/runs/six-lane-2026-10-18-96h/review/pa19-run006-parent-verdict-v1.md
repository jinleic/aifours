# PA(19,8,6): ms06 b295 closed; 142 lane-original M2 cases remain

Recorded at 2026-10-19T03:56:11-0700.

**CORRECTNESS-ACCEPTED SCOPED PARTIAL.** Direct whole-case ms06 b295 (ms06_s00187) has a retained qualified UNSAT proof, independently rerun with the provenanced second drat-trim build. Remaining **142=79ms06+63ms09**. PA(19,8,6) remains UNDECIDED; M1 and the separate M2H views are unchanged.

Parent observed run006 exit0, all10children settled and C1-C7 intended outcomes; checked no latch/cancel/defects, nativeUNSAT/VERIFIED, CNF pin and complete proof hash/bytes. [Replay audit](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/pa19-ms06-provenanced-replay-v3/parent-audit-v1.json) `814394b9519e86f2e5c26ecd340068cfb24c59f043e722cec2b54e1772d5c334` confirms exit0/SETTLED, no trips, exactlyVERIFIED, consumed277250030=complete proof bytes, and unchanged pinned inputs. [Frontierv5](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/pa19-parent-frontier-v5.json) `be79dede711b315bd400511d583e20d12fd453c4f4eada8f65d8aa8c2448ed9c` removes exactly b295. Run summary SHA `222993f2974dde9b07a97c8049784a2c1dbe41c4a6819caedce0d8758a567565`, item record SHA `e9209637277001575a856aa3849ebaf3e6c183c0757158b53ee0ab89228febb0`.

Trust: direct build_v2 mathematical completeness is the previously reviewed premise, not reproved by UNSAT. SameDRATalgorithm in two builds, not two independent verification algorithms. The old v6 b295 UNKNOWN remains unchanged; this is a new attempt. No novelty or full-target claim.
