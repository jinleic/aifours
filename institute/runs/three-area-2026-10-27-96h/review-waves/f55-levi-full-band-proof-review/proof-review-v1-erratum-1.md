# F55 proof review — pointwise first-defect wording correction

Observed native clock immediately before this new erratum: **2026-10-28T17:53:43-0700 PDT**. This is a pre-write observation, not a claimed creation time.

The frozen `proof-review-v1.md`, SHA-256 `e1bd71a468cc5a84bf4c6bce01e02db3c7cece8a2f4caf7a693963fec320dd74`, ends its §5 with the mistaken sentence “Pointwise `Ddef_alpha=0` must not be substituted for a first-defect argument without its predecessor boundary.” Replace that sentence conceptually by:

> Pointwise vanishing of the simultaneous singular kernel `K_alpha(S)` does not by itself establish `Ddef_alpha=0` by the least-height argument without control of predecessor defect components. In contrast, `Ddef_alpha=0` itself is exactly the desired pointwise equality `J_alpha=tau_alpha`. The downward-closed whole-band first-defect argument given immediately before the sentence is unchanged.

This is a correction of the review's wording, not a claimed defect in the candidate. The INCONCLUSIVE verdict, findings, source/hash coverage and remaining finite-certificate obligation are unchanged; do not edit or replace the original report.
