# K62-FG R2 Codex review: disposition (superseded for the frontier)

Recorded at 2026-10-19T04:50:29-0700.

**Not accepted; superseded.** The candidates K62-FG-v1 Theorem R2-11 and K62-R2-v1 are not accepted. They are superseded for the frontier by the stronger candidate K62-E3 (no K6.2* configuration with e_d<=3), which is frozen for dual review ([freeze](sun7-K62E3-review-freeze-v1.json)). No K6.2* exclusion is accepted from this review.

## Review facts
- [Codex output](sun7-K62FG-R2-codex-v1.prompt.stdout.txt) (`4dcb0ee15e04bde1c69569e918c0222161ed918bb6d3c6f0aa2d56bb2a51d7ad`); [receipt](sun7-K62FG-R2-codex-v1.prompt.receipt.json) (`acc6a804df2804672628f772c5b2ccdcb23f8f08ed79b40692a7b4ca1fdc9542`): observed gpt-6.1-sol, effort max, read-only sandbox, 985 s.
- Findings: FATAL none; **MAJOR**: Step C, II.1, k3=3 omits the branch where r meets d but neither t nor a three (local data h_d>0, z_t=1, (z_a,z_b,z_c,z_r)=(3,3,3,5)); Codex supplied an exhaustive replacement certificate set. MINOR: FG orientation summary; explicit y_d=0 in the generic k3=2 outside-five certificate; replace "when r,t share 2" by z_r>=2; README locator for L0.1.
- Codex's own frontier statement after repair: R2 excluded for e*∈{2,3}, the (1,1) pair for arbitrary e*; asymmetric R2 with e*>=4, all R1, and full Sun(7) open.

## Disposition
- No erratum is requested now. If K62-E3 fails review, the R2 route needs a consolidated erratum implementing the Codex repair, plus the Claude review (still running at this record) before any acceptance.
- The Claude K62-FG R2 review, when it returns, is recorded as a superseded review in a new note; it cannot promote R2-11 on its own.
- Sun(7) remains OPEN.
