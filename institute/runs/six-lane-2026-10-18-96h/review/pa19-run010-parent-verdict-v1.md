# PA19 run-010: three whole ms06 cases closed

Recorded at 2026-10-19T05:09:46-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL:** direct cases ms06 b154, b168 and b169 are UNSAT under the lane-original M2 encoding. [Frontier v8](pa19-parent-frontier-v8.json), SHA256 `841d207a3f9a9975938a32dd299040bb4677a1c8403610329ccc476e8e9e138a`, now contains **135 undecided cases: 73 ms06 + 62 ms09**. PA(19,8,6) remains UNDECIDED. Measured M2H views are unchanged and not merged.

## Evidence and binding

- [Item GO v23](pa19-pilot-v23-parent-GO-v1.json), SHA256 `d1ef9f89837c74ea6d84a2db5cda58c1764f168afca3200eb9fcdda21853d4cf`. run-009 is deliberately unused: the parent prioritised whole ms06 cases over v22's partial ms09 intervals under the unchanged disk ceiling.
- [Raw endpoint audit](pa19-run010-raw-parent-audit-v1.json), SHA256 `4b5420d705b67e0279b8acd10c6b653194ef80f6cb3018263d6f16d81e0af8ce`. Summary `d5fbf539a6974d972b3c420c524b23fb4b4fa56b9fe4bebdc9d9d49ea2b88881`; controls `881dc8503805e48fcc78a0db75bb9354ba3ecbf728bb3818083f84e26d534d1f`; 14 children SETTLED; C1–C7 reached their intended outcomes with raw output hashes checked. Every item has self-exit20/UNSATISFIABLE, complete proof sink, checker self-exit0/VERIFIED, and parsed proof bytes equal retained proof bytes. Commit record hashes match the summary; no latch/cancel/terminal defect.
- Case identities: b154 -> ms06_s00269; b168 -> ms06_s00272; b169 -> ms06_s00275. Each was open in frontier v7. Request v8 and the frozen preflight `c693e4e1b67ecec24eca58b4d05dc42c9cd982c72e25d3fb835d0ec32194c0c2` bind the same CNF SHA256/byte count/header and equal skeleton fields. Whole-case encoder completeness is the accepted prior bridge, not inferred merely from a digest.
- Three provenanced second-build replays used drat-trim `a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37`, the same DRAT algorithm, **not an independent checker algorithm**. Every supervisor launch was separately gated and followed an explicit clean receipt check; no unconditional replay loop.

| Case | Retained and checker-parsed proof bytes | Parent replay audit |
|---|---:|---|
| b154 | 65,858,564 | [audit](pa19-ms06-provenanced-replay-v5/ms06_b00154_direct/parent-audit-v1.json) |
| b168 | 352,603,752 | [audit](pa19-ms06-provenanced-replay-v5/ms06_b00168_direct/parent-audit-v1.json) |
| b169 | 44,071,465 | [audit](pa19-ms06-provenanced-replay-v5/ms06_b00169_direct/parent-audit-v1.json) |

Every replay receipt is SETTLED, rc0, no trip/cancel, empty descendant census; exact status/header/consumed-byte checks and input/output rehashes pass. All three raw and replay checker logs retain 152 duplicate-literal warnings each; these are disclosed, not suppressed as if absent.

Only these three cases are removed. Older UNKNOWN evidence is preserved. No full-target, novelty or breakthrough-gate claim follows.
