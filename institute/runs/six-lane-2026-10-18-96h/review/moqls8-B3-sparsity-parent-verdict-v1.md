# MOQLS8 B3: sparse-unitary classification and direct-axis residual accepted

Recorded at 2026-10-19T16:21:57-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL.** Written linear algebra and necessary structure; **genuine B3 exclusion remains OPEN**, GB remains15/18, fulln8 OPEN. No solver/Boolean/SAT/UNSAT, Lean, human or novelty claim.

## Accepted scope

- **A:** every7x7 unitary with<=12 nonzero entries, up to row/column permutation, has components P (seven singletons), D1 (one dense2x2 plus five singletons), D2 (two dense2x2 plus three singletons), or T (one3x3 with exactly one zero plus four singletons). Counts7/9/11/12 respectively. P is monomial with independent entry phases, not necessarily one common phase.
- **B1-B6:** under genuineQLS/MOQLS definitions plus the stated row0/SB2/P1-B3 conditioning, the four other column0 bases obey the literal sparse/isolated/residual/local-shape/incidence conditions. At least two support matrices are permutations; D2 is excluded by four forced singleton components. The remaining T possibility in this necessary list is neither asserted realizable jointly nor newly excluded by this verdict.
- **C:** its three conditions characterize the exact **direct row0/column0 data**. Necessity for a fullconfiguration is not sufficiency for completion; no enumeration/count of S is certified.
- **D:** the explicit datum satisfies those directaxis equations, showing that those equations alone cannot imply contradiction. This is a partial datum, not a fullgrid counterexample and not a counterexample to an axis-only condition derived from interior completability.

## Text and independent reviews

[Candidate](/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/continuations/b3-support-sparsity/B3-COLUMN0-SUPPORT-SPARSITY-CANDIDATE-v1.md) `46288f4efae9815aa5e428cc74e7293b116e2d744a6d16b2e6fedf5c9ee8ac2e`; mandatory [erratumv1](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/moqls8-B3-sparsity-parent-erratum-v1.md) `a9748009e403b953938f56189c83a2e8040bacbb44b314cbb28929116a3e0279`, [v2](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/moqls8-B3-sparsity-parent-erratum-v2.md) `021bfe542ff870685483de66ba9bed4e927cac9bafcf38f162d02bab9b6c93ad`, [v3](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/moqls8-B3-sparsity-parent-erratum-v3.md) `db5fffa7e3738e53ba843e937cacd028bd3221589c2ab8a317ba134cb1c8c9d2`.

- [Codex gpt-6.1-sol/max](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/moqls8-B3-sparsity-codex-v1.prompt.stdout.txt) `bf6719eab7a7300e2330dc20d145016ad62560064cc28d88e1e6077b765c05b1`:0F/0M/1m; missing full3x3 example supplied in erratumv2; A-D mathematically accepted at partial scope.
- [Claude claude-opus-5-5/max](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/moqls8-B3-sparsity-claude-v2.prompt.note.md) `c475c98915af535233115ffa5d50c7881578419d521f4ca86ae1925eb32d078b`:0F/0M/5m, dispositioned above; A-D all accept or accept-with-editorial-fixes.
- Parent freeze `8d8e40d3` records complete source/copy pin and proof checks, including the corrected physical-LF194-223 primary excerpt rather than the old nominal195-225. Parent rechecked current proof anchors, A3 component argument, B1/B2 counts, C sufficiency's joint18>17 exclusion and the direct-axis/Boolean boundaries against the final second-family findings. No scientific execution performed.

H2-H4 are conditioning hypotheses; this packet does not certify the global U/T16 bridge or all nonclassical sets. Only QLS/MOQLS definitions are load-bearing external mathematical input. The later B3 interior/full-row candidates retain their own review gates and are not accepted here. No B2/A10/A11 or previous UNKNOWN is changed. Runtime remains HOLD.
