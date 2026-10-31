# Required pre-source erratum: publisher cross-branch remark

**REQUIRED BEFORE SOURCE.** Read this erratum before reading, reviewing, adopting or citing the frozen candidate `frontier-20261028-full-source-lp-optimum-v1.md`, SHA-256 `08af469a09689dcdf40b07bbb086c851349141f582b92714b92d5a7eef63fcdd`. The candidate's bytes and all f110 gate inputs remain unchanged.

## Correction

In the candidate's **Exact LP scope** paragraph, the reference to **“Remark 3.8”** as the source of the omitted cross-branch Shannon inequalities is incorrect. Replace that reference, when interpreting the frozen text, with **Remark 5.4** of the 2024 publisher paper. Theorem 5.2 item 2 specifies the three elemental variable sets. Remark 5.4 explicitly explains that elemental inequalities mixing variables from different listed branches—for example both `X2'` and `X4''`, corresponding here to `b'0` and `d'1`—were omitted for computational reasons.

Publisher source: `institute/runs/three-area-2026-10-27-96h/public-sources/gurpinar-kybernetika60-2024-553-575.pdf`, SHA-256 `373e8a2567fc7de9d40d0e5fabca9655cbb7b689a162005262b4f4d432bb46d8`. The locally extracted text `gurpinar-publisher-layout-v1.txt`, SHA-256 `98d1dba760d383db92948026002bfa7dd95ebbe558cf1917f0c471189b528c88`, has Theorem 5.2 item 2 at lines 949–955 and Remark 5.4 at lines 985–995. Remark 3.8 instead concerns a different earlier LP comparison and is not the cited cross-branch exclusion.

## Scope and disposition

This is a **source-reference correction**, the same MINOR reported by both f110 reviews as relayed by Main. It does not alter the defined three branch variable sets, the exact primal/dual values, the all-disjoint `F_n` check, or the stated exclusion of unmodeled cross-branch constraints. The `1847/276` conclusion remains strictly about the specified three-branch LP, not an entropy realization or a new unrestricted guessing-number bound. This erratum does not independently assess or adopt the separate cross-branch/gluing successors.
