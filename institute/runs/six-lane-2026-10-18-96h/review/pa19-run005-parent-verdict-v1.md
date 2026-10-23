# PA(19,8,6): three further whole ms06 M2 cases closed; 143 remain

Recorded at 2026-10-19T03:35:49-0700.

**CORRECTNESS-ACCEPTED SCOPED PARTIAL.** Whole lane-original M2 cases b189 (ms06_s00159), b202 (ms06_s00158), and b177 (ms06_s00148) have qualified retained UNSAT proofs from run-005 and completed provenanced replays. The remaining count is **143 = 80 ms06 + 63 ms09**. PA(19,8,6), M1, and both separate M2H views are not settled or merged by this result.

- [Raw audit](pa19-run005-raw-parent-audit-v1.json): `48be66644f8a04a2c0c70cf628e4a8d5e0eb4be1cdafd29bb615e27750ad6bfc`; exit0, controls C1-C7 matched, all14 children settled, no cancellation/latch, exact CNF and proof pins match.
- [Provenanced replays](pa19-ms06-provenanced-replay-v2/science-results-v1.json): `9c23f5882b2b4640ee1fa3d9d554f88414b66fe98d17e2b7dd50ed1815c7915b`; all three child exits0, exactly `s VERIFIED`, clean settlement/no trips; parsed byte counts equal complete retained proof sizes 254061918, 213897101, 317826679 respectively. Rehashed inputs unchanged.
- [Frontier v4](pa19-parent-frontier-v4.json): `5bc070391d61c6e65fb49c9851d776b5468bcd4fa60bf9bdb04a6c079c52adc4`; explicit removal of exactly these three distinct b-indices from v3. Full-case identity uses unchanged reviewed build_v2 direct encoding; no placement intervals or denominators.
- [Duplicate-literal disclosure](pa19-duplicate-literal-disclosure-v1.json): parse warnings identify idempotent repeated literals, not an omitted proof suffix; logical clauses unchanged. Earlier run003/004 wording corrected there.

Trust boundary: one DRAT verification algorithm, two separately built binaries. Retained files support replays but do not independently prove the encoding's mathematical completeness; that remains the previously reviewed build_v2 premise. No novelty claim.
