# Olson SCW — second cut-window terminal family accepted

Recorded 2026-10-20T04:40:41-0700 (`/bin/date`).

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL**, read with parent erratum v1 (f533ecf3c1c1a649de44176daffc4f761bbaf6a6863015f1b7f7995541698a8c) and the parent process note (fa0a040f35f40da7ac51463857e492324c08bb4fa3cdb9693122db52cab7c2b5). For every integer kappa≥4 with p=4kappa−3 prime (so p≡1 mod 4, p≥13; e.g. (4,13), (5,17), (8,29)), no length-(4p−2) avoider over D_(2p) has an admissible NF with terminal k=p+1 and kappa_hat=kappa. Full existential antecedent: some admissible NF, extra reflection pairs anywhere, genuine empty-run rule; no o_F, nonempty-run, rotation-pair or rigidity premise. Imports: NF, GRX if-direction, SC0 through the explicit minimal-zero-sum extension Y′z, ZSTRUCT/FB in (S′) at (p−1,kappa−1); no S1(a), Setting fact, FB-E, Theorem P, CJ′′′, K3-11, FCW, USK or P11R lemma.

Codex gpt-6.1-sol/max **0F/0M/0m**; Claude claude-opus-5-5/max **0F/0M/1m** (provenance wording, disposed). Both exit0 with expected model/effort and checked prompt/output bindings; both independently re-derived the truncated realisation with minority-sign exceptions, the widened common window I*=[Pi0−2,2p+2−nu0], the margins of additivity/complements/theta (margin exactly 7 at kappa=4), the new kappa=4 additive-constant pair and the top-kappa sorting with simultaneous-exception cases (alpha)/(beta)/(gamma). Parent hand-checked the same items (5b4c82cda3610f469bdaba4e6a54bc733f074ad4c44ee8c02c11c859711e1440).

**Process qualification:** the scope freeze preceded the written proof but not the worker's unwritten preliminary route checks; strict pre-derivation preregistration is NOT certified. The exact target was fixed earlier by the parent transition and did not change.

**Boundary:** only p=4kappa−3 (deficiency delta=2). Together with accepted USK (kappa≤floor((p−1)/4)) and FCW (p=4kappa−1), every terminal lower-half cell kappa_hat≤floor((p+3)/4) with kappa_hat≥3 is now excluded at the corresponding primes; larger middle cells (delta≥4), the p=7 terminal kappa_hat∈{1,2} cells, nonterminal/inverse-normalisation obligations and full ordered Olson remain OPEN. Model-assisted written mathematics; no novelty, human-referee, Lean or runtime authority.

| Artifact | SHA256 |
|---|---|
| [proof-SCW-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-second-cut-window/proof-SCW-v1.md) | `6a1965aecf599e00b512ca1df36127d21e5bac21bea7ac0da5804092245f3650` |
| [SCW-scope-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-second-cut-window/SCW-scope-v1.md) | `99707df43b6a577e479444d80459b123461b55d03c827389ccac445f54e7258d` |
| [review-package-SCW-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-second-cut-window/review-package-SCW-v1.md) | `bdf47c92781214ff01aee89bb1a4b8d7fa33d98c82891a5c61effa035ef1dddd` |
| [review-excerpts-SCW-v1.json](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-second-cut-window/review-excerpts-SCW-v1.json) | `5713213bf48179d66883d055aac5d236ecd99786d15dd5c7d05cc716784843a5` |
| [olson-SCW-parent-erratum-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-SCW-parent-erratum-v1.md) | `f533ecf3c1c1a649de44176daffc4f761bbaf6a6863015f1b7f7995541698a8c` |
| [olson-SCW-parent-process-note-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-SCW-parent-process-note-v1.md) | `fa0a040f35f40da7ac51463857e492324c08bb4fa3cdb9693122db52cab7c2b5` |
| [olson-SCW-parent-written-check-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-SCW-parent-written-check-v1.md) | `5b4c82cda3610f469bdaba4e6a54bc733f074ad4c44ee8c02c11c859711e1440` |
| [olson-SCW-first-family-parent-disposition-v1.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-SCW-first-family-parent-disposition-v1.json) | `bfa4c3a4af5ba52f94b672e0b295375c8841c01be188d854ed12400d508d86a5` |
| [olson-SCW-codex-v1.prompt.receipt.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-SCW-codex-v1.prompt.receipt.json) | `41e3461b4b1e7688e6a09db373b7a056470402835cbb41fdd809baef8c4f5388` |
| [olson-SCW-claude-v2.prompt.receipt.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-SCW-claude-v2.prompt.receipt.json) | `e4a574090447a0b0f5593c295df3881b2d757db4e815426d8da3ed7adfaf2ed0` |
| [olson-SCW-codex-v1.prompt.stdout.txt](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-SCW-codex-v1.prompt.stdout.txt) | `8a777d0ccf2ccf82c34a73c5d097f56f871feb49433450ea2e82d910bec48d67` |
| [olson-SCW-claude-v2.prompt.note.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-SCW-claude-v2.prompt.note.md) | `4211daf0a4f08944cf99290d3968a2b4f58d24497c181ee5de698ac632cd382b` |
