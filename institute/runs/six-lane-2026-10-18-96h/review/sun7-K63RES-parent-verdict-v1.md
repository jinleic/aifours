# Sun k7: the full K6.3 class is excluded

Recorded at 2026-10-19T04:01:41-0700.

**CORRECTNESS-ACCEPTED SCOPED PARTIAL.** K63-RES excludes every K6.3 configuration with f_d>=2 and a C-vertex of2-valuation>=2, with arbitrary5-marker placement and unbounded exponents, in arbitrary groups with finite-index subgroups. Together with accepted K63-D (f_d=1) and K63-E (f_d>=2 without a2-marker inC), this exhausts **all of K6.3**. Full Sun(7) remains OPEN: K7 and K6.2* still remain.

## Sources and verification
- [K63-RES](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/K63-RES-v1.md) `1542a551f6d9787784a2434d18a5aa7275f673b23aab4901a384518206f67515`; mandatory overlays [v1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/K63-RES-erratum-v1.md) `e70a5518a74ee4230d442a1b81d562d65b683ab6fcb904ff306792ea0ac3b49b` and [v2](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k63-residue/K63-RES-erratum-v2.md) `c31d76238e26a8ceb5105cda1d685aaa110b7e5df3948e9e5cf1406d7d544cb5`.
- [Codex](sun7-K63RES-codex-v1.prompt.stdout.txt) `690f7badba9c8c2dfd301d67a81d88fb9e1d7af07a7c1370938edc0fa3407a44`: all5claims ACCEPT,0fatal/0major/1minor.
- [Claude](sun7-K63RES-claude-v1.prompt.note.md) `43f80bf971e2acc4c1b911f4e9930813c7801bc4c5a012b6a9b1369f17147367`: all5claims CORRECT,0fatal/0major/9minor. OverlayX1-X8 disposes every finding; productformula/LCM replaces any broadenedTG import, VFC acceptance is pinned, and the restrictedstar remark uses the RowLemma rather than a broadenedCLIQUE.
- Parent independently re-derived FG's index induction (basei*,d has multiplier<=2;5-marker ordering; later multipliers<=5), both noncommutative fibre counts, every rowweight case, and the final INV contradiction. Both overlays read in full against reviewfindings.
- [Independent exact-weight controls](k63-row-controls-v1/parent-audit-v1.json) `032cea1015611544ec7bcb263f163ef51ec435cec27d354b7da98b9931043009`: all43750gcd-type representative rows have feasible explicit weights with minimumvalue31/6>5. Positive17/3 case and intentionalinfeasible-weight mutation behave as intended. Exit0/SETTLED with no trips. This validates finite arithmetic only and is not a premise for the group theorem or an LP/Lean certificate.

## Core argument
At a non-5-marked odd C-vertex v, FG proves gcd(n_v,index(intersection of any other subgroup subset)) divides6, also for the conjugated subgroup family. An omitted set of measure>=1/6 strengthens both fibre counts to<=5/6. Explicit row weights then force alpha_vd=alpha*_vd=2, contradicting alpha_vd+alpha*_vd<=3.

## Verification boundary
Written proof, model reviews only, no Lean or human review. The import closure includes **computer-assisted Sun(6)** (load-bearing in the all-gcd5 six-neighbour case); this is not a wholly computation-free proof chain. K63-U0 is redundant in the final three-way partition. No novelty clearance, fullSun(7) gate, or extension ofFG to arbitraryK7/K6.2* is asserted.
