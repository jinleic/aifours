# Sun k7: D23-CENTER and D23-MIX accepted at their stated subcase scopes

Recorded at 2026-10-19T03:37:58-0700.

**CORRECTNESS-ACCEPTED SCOPED PARTIAL (written mathematics).** For different 2- and 3-marked vertices z,t in K7:
- D23-CENTER excludes both z-rows being 4-type, with the 5-marker anywhere.
- D23-MIX excludes either z-row being 4-type when the five other vertices are unmarked (5-marker absent or on z/t). Both rows must then be 3-type as defined in the candidate.
All exponents remain unbounded; the finite-core quotient carries both conclusions to arbitrary groups with finite-index subgroups.

## Binding evidence
- [Candidate](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-D23-NO4-v1.md) `a3b47626687141dac49daf30aab302c1ea66f15a74f28ee638b2212258de189d`.
- [Mandatory erratum](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-D23-NO4-erratum-v1.md) `594c28aab89a269b32f79385552fd226eb22c41e8be538cc5bebf895acc54d6a`; X1-X13 dispose every finding. In particular q_a=1 permits inverse x*=5 before INV excludes it; it is not prematurely set to4. Exact common-rule acceptance is [old written verdict](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset7-written-parent-verdict-v1.md), not a new scope inferred from Z2.
- [Codex](sun7-D23-codex-v1.prompt.stdout.txt) `8be1767fce86eae423fcffabc12659fe4e82690d60a191d37fb5af26c9b08992`: CENTER ACCEPT0/0/0, MIX ACCEPT-WITH-FIXES0/0/1.
- [Claude](sun7-D23-claude-v1.prompt.note.md) `86f89f3c9409ab2ed59cd630e0c495fba38332737255d25061c25d9c12af1265`: CENTER AWF0/0/5, MIX AWF0/0/8 and1 general minor. Runtime receipts record gpt-6.1-sol and claude-opus-5-5; prompt-only mathematical review, no external human review.
- Parent independently derived both triangle tables, gcd reductions, F7 orientations, VFC mass bounds and row dichotomy before review; read the complete erratum against both reports afterward. The mixed case has D*_u contained in Y*_a minus D*_a of measure1/6, but the two u-sets have union at least2/6. No finite probe is a premise.

## Boundary
K7 stays OPEN: double-3 z-rows are not excluded; with a third 5-marked vertex, mixed rows are not covered. Shared2/3 plus separate5 remains the separate Z23-P5 candidate pending its reviews. K6.2* and K6.3 unaffected. The abstract obstruction note is unreviewed navigation, not part of this acceptance. No Lean, novelty clearance, full-target gate or human-review claim.
