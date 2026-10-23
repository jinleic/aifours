# PA(19,8,6): ms09 b9 closed; 141 M2 cases remain

Recorded at 2026-10-19T04:18:37-0700.

**CORRECTNESS-ACCEPTED SCOPED PARTIAL.** Run007 closes the complete lane-original M2 case ms09 b9 (ms09_s00001), covering every placement index0–814 of its pinned815-entry list. Remaining **141=79ms06+62ms09**. It also certifies indices0–99 for b25 (100/374) and b69 (100/704); those two cases stay open. M1 and the separate M2H views are unchanged.

- [Raw audit](pa19-run007-raw-parent-audit-v1.json) `3b3724063ee10cf31cfe37f6e15313ada2ef2670dc8b306bf456baf895acbc08`: controlsC1-C7 intended, all14children settled, exit0/no latch/cancel; retained CNF and proof pins match.
- [Provenanced replay audit](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/pa19-ms09-provenanced-replay-v1/parent-audit-v1.json) `c1ceea84964c0edbbc94cb3021c8f8c33516b4717cb866592199ea69cd0eb1b1`: all3checks exit0/SETTLED, no trips/errors; exactlyVERIFIED and completechecker-consumed byte equality. Rehashed inputs unchanged.
- [List binding](pa19-run007-list-binding-v1.json) `305c34d3d23a3657ad1326b770ab9ca38b4a9022a071d5e2044d3a7e061a900f`: actual immutable listbytes, b-index and denominators checked; exactcoverage set for b9, strictsubsets for25/69.
- [Frontier v6](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/pa19-parent-frontier-v6.json) `64be77f84293f8b4078cecd864a063abfddd2792b458ff0fd23e8b7193c792d0`: removes onlyb9 and stores the two acceptedpartial intervals separately.

Trust remains the prior reviewed build_partbatch/list-generation completeness; two DRAT builds share one verification algorithm. Byte-identical proof reproduction is not an independent mathematical encoding proof. No PA19 solution or novelty claim.
