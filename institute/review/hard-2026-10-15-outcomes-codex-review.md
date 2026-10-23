ACCEPT-WITH-FIXES

1. **Major — Replay coverage is overstated.** [institute/review/hard-2026-10-15-outcomes.md:31](/Users/jinleic/repos/aifours/institute/review/hard-2026-10-15-outcomes.md:31)

   Evidence: `parent-check.json` contains 36 successful contract entries, but four have no executable commands: `closure-lemma`, `fixed-filter-limit`, `finite-moment-reformulation`, and `general-integer-comparison`. Their verify/check return codes are null. Commands actually ran for 32 claims.

   Replace the first sentence with:

   > After the supervisor exited, the wrapper checked all 36 delivered claim contracts (21 math, 9 information science, 6 physics). It replayed commands for 32 claims in sandboxed temporary snapshots; four proof-only entries had no executable commands.

   Apply the same distinction at these locations:

   - [institute/runs/hard-2026-10-15/README.md:23](/Users/jinleic/repos/aifours/institute/runs/hard-2026-10-15/README.md:23): replace “The wrapper's parent replay passed for all 36 claims.” with “The wrapper's parent check passed all 36 claim contracts; 32 had executable replay commands and four were proof-only entries.”
   - [batches/03/receipt.json:48](/Users/jinleic/repos/aifours/institute/runs/hard-2026-10-15/batches/03/receipt.json:48): replace the value with `"PASS: 36/36 delivered claim contracts; executable commands replayed for 32 claims; four proof-only entries had no commands"`.

2. **Minor — One displayed upper bound rounds inward.** [institute/review/hard-2026-10-15-outcomes.md:38](/Users/jinleic/repos/aifours/institute/review/hard-2026-10-15-outcomes.md:38)

   Evidence: `physics-subcavity-control/result.json:80` reports approximately `0.000680764424`. Fresh read-only evaluation gives the enclosure `[0.000680764423849635, 0.000680764423849636]`. Consequently, `+0.00068` is below the enclosed value and cannot be called an upper bound.

   Exact replacement: change `+0.00068` to `+0.000681`.

3. **Minor — “Opened 19 sources” overstates recorded access.** [institute/review/hard-2026-10-15-outcomes.md:50](/Users/jinleic/repos/aifours/institute/review/hard-2026-10-15-outcomes.md:50)

   Evidence: physics epoch-1 `sota.output.sources` contains 19 entries: 17 marked `full-text`, one `abstract`, and one `inaccessible` (`record.json:247`, including access fields at lines 252 and 414).

   Replace the first sentence with:

   > The literature stage recorded 19 sources on 2026-10-15—17 full-text, one abstract-only, and one inaccessible—and located no certified k=4/5 constant below 10.23/21.33 in the accessible material.

4. **Minor — The remaining half-classes were screened.** [institute/review/hard-2026-10-15-outcomes.md:81](/Users/jinleic/repos/aifours/institute/review/hard-2026-10-15-outcomes.md:81)

   Evidence: information-science `record.json:1047` calls them “252 screened half-classes”; line 1273 says they passed the necessary-condition screen. The ledger’s own line 21 agrees.

   Replace the final bullet with:

   > Information science: search the 252 half-classes that passed the necessary-condition screen, or find an argument for arbitrary degree-eight tables.

The remaining checks found no discrepancy:

- **Times, durations, budgets and cutoff:** UTC−7 conversions, stage sums, minute totals, remaining allocations and displayed completion times reconcile. Supervisor completion left 26 minutes 15 seconds; the shortest observed lane needed 25.8 minutes before novelty and reserve. Not requeuing is consistent. Parent replay’s later completion is explicitly excluded from research time.
- **Verdicts and scope:** Claim and verdict counts match. “No claim judged wrong or unsupported” is correctly confined to batch 03. Engine `unverified`/`PROOF-OBLIGATION` outcomes and absent novelty verdicts are accurately represented.
- **Receipt integrity:** All 13 listed hashes match their artifacts. All 12 archived copies match their originals.
- **Mathematics:** Imported premises remain explicit; the larger C-run ranges are consistently empirical reports rather than certified bounds.
- **Information-science proof audit:** Mathematically sound. Both Parseval caps, `253,952` and `249,856`, are below `262,144`; the degree/support-XOR equivalence and quadratic attainer check out. No existence or nonexistence claim is made.
- **Physics controls:** Apart from names/role metadata, only alpha changes. Both checkers freshly reproduce all eight recorded acceptance/rejection results. The live snapshot hash matches the recorded before/after hash.
- **Physics attribution and caveats:** The even-arity Franz–Leone attribution agrees with [Mertens–Mézard–Zecchina’s introduction](https://arxiv.org/pdf/cs/0309020); the odd-arity statement agrees with [Lelarge–Oulamara condition (4)](https://arxiv.org/html/1708.02457v2). Formal-verification, peer-review and novelty caveats are preserved.

No files were modified.