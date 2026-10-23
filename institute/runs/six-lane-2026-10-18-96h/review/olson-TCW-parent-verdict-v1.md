# Olson TCW — third cut-window terminal family accepted

Recorded 2026-10-20T06:27:25-0700 (`/bin/date`).

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL**, read with worker erratum1 and parent errata v1–v3. For every integer kappa≥4 with p=4kappa−5 prime (p≡3 mod4, p≥11; e.g. (4,11), (6,19), (7,23), (9,31)), no length-(4p−2) avoider over D_(2p) has an admissible NF with terminal k=p+1 and kappa_hat=kappa. Full existential antecedent (some admissible NF, extra reflection pairs anywhere, genuine empty-run rule); no o_F, nonempty-run, rotation-pair or rigidity premise; all-rotations-equal configurations included without CJ. Imports: NF, GRX if-direction, SC0 through the minimal-zero-sum extension Y′z, ZSTRUCT/FB in (S′) at (p−1,kappa−1); no S1(a), Setting fact, FB-E, Theorem P, FCW/SCW/USK/K3 lemma.

Codex gpt-6.1-sol/max **0F/0M/3m**; Claude claude-opus-5-5/max **0F/0M/3m**; all six disposed by parent errata v1–v3 without changing any lemma or case. Both exit0 with expected model/effort and checked bindings; both independently re-derived the exception lists, widening tables, all-kappa triple additive constant, asymmetric theta bound, Lemmas 12–16 including the kappa=4 Case B.4 and the empty-alternating-set Lemma 13. Parent hand-check dc3a374a34ada6d2379644422306f9418234bd67da36e5eb00b4c548aa6408d8.

**Process (not correctness evidence):** worker checkpoint gap 4138 s (>1800 s) after a discarded long derivation; six pre-creation text replacements; metadata-only byte counts and a JSON parse. Strict cadence compliance is NOT certified.

**Boundary and composed consequence (union of separately accepted scopes, no new mathematics):** with K0T (kappa_hat0), LOWER-K1 (kappa_hat1, p≥11), K2 (kappa_hat2, p≥11), FCW ((3,11)), the upper-half composite (BOTTOM verdict LF9–14, p≥7) and PP1-EXCL (kappa_hat=p−1, p≥7), and Theorem R (0≤kappa_hat≤p−1): **for p=11 every terminal k=12 cell kappa_hat∈[0,10] is excluded**, i.e. no length-42 avoider over D_22 has an admissible NF with terminal k=12. Each cell carries its own imports (UH-A where used). Not claimed: other k at p=11, other primes' remaining middle cells (e.g. (5,13)), p=7 lower kappa_hat∈{1,2} (P7L under review), full ordered Olson, novelty, human-referee, Lean or runtime authority.

| Artifact | SHA256 |
|---|---|
| [proof-TCW-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-third-cut-window/proof-TCW-v1.md) | `62c747911239c32998d2ec2b3bd9ec538eee5e523f68b92233aa06e890f85713` |
| [TCW-scope-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-third-cut-window/TCW-scope-v1.md) | `f0dacbe3e1f2f8a4267f7bdfa5ea91097690168bbf0e50dced92e6cc49be02d1` |
| [erratum-1-proof-TCW-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-third-cut-window/erratum-1-proof-TCW-v1.md) | `00ba0139bc3f13025f7ba9474d3c48813c746839a35e33f95fb5ac3fa4edea01` |
| [review-package-TCW-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-third-cut-window/review-package-TCW-v1.md) | `39cca5eefc3de291405eca22db23f1e0168b2c9d9168c2449017a02b10c311cf` |
| [review-excerpts-TCW-v1.json](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-third-cut-window/review-excerpts-TCW-v1.json) | `3a21ad905ac96e68b60ecaeb1ced6bc9ed4dee122fbe5692f41fd9b6b0338058` |
| [olson-TCW-parent-erratum-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-TCW-parent-erratum-v1.md) | `eb673b3200d4d0f8f7e36f61fbf3225e5c3542e0b14de05a604ca50c640ee8c9` |
| [olson-TCW-parent-erratum-v2.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-TCW-parent-erratum-v2.md) | `a8204c0e533828fc86816ea6de648a2d52ff3409898f0c557bd8fe5a79f8e88d` |
| [olson-TCW-parent-erratum-v3.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-TCW-parent-erratum-v3.md) | `5443678bdeff966b4b4648b8042be2874a31cf67e44e7c6b26879730aa5395bf` |
| [olson-TCW-parent-written-check-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-TCW-parent-written-check-v1.md) | `dc3a374a34ada6d2379644422306f9418234bd67da36e5eb00b4c548aa6408d8` |
| [olson-TCW-first-family-parent-disposition-v1.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-TCW-first-family-parent-disposition-v1.json) | `836cb1e55d1749e4b7b6bd3f7c0f40438fee8ca5907c89163aa25f4a1a436aa7` |
| [olson-TCW-codex-v1.prompt.receipt.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-TCW-codex-v1.prompt.receipt.json) | `55da0beb2ea5653df56c83325625b436ab08f35a2a11540b2f8c9d062b5ef380` |
| [olson-TCW-claude-v2.prompt.receipt.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-TCW-claude-v2.prompt.receipt.json) | `072900bdeaaedb8a5291da511c55e612ab47ab8a465d5316b72988c658c1bc92` |
| [olson-TCW-codex-v1.prompt.stdout.txt](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-TCW-codex-v1.prompt.stdout.txt) | `f8c56c41377758953ac02a28f2eba5c3dddd5988878d50bacbf9cd5f3b379f54` |
| [olson-TCW-claude-v2.prompt.note.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-TCW-claude-v2.prompt.note.md) | `6b0faa9b33a2e329472b7f2380d42b3b0df70218f715da9de86f2cc1bf4ae30c` |
