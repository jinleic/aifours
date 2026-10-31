# reviewer-correction-1-v1 — additive wording correction to review-v1.md (f138)

Observed clock before this write: 2026-10-29T03:57:07Z. Target: `review-v1.md` SHA-256 `9d397e6eca476af1e64084329089a865eb659fd933b4a623c011edd912ee72c1` (19109 B), which is left byte-unchanged. Trigger: wording correction received from Main after delivery; verified by the reviewer.

## Affected sentences
1. `review-v1.md` §2.2, bullet "Adapted/nonanticipating": "$w$ is left-continuous and $\mathcal F_t$-adapted, hence predictable (progressive)."
2. `review-v1.md` §6 (and the reviewer's delivery message): "is predictable".

## Correction
The displayed witness $w_t=\sqrt{N/\delta}\,\mathbf 1_{\{t<\rho\}}=\sqrt{N/\delta}\,\mathbf 1_{[0,\rho)}(t)$ is **right**-continuous in $t$: at $t=\rho$ its value is $0$ while its left limit is $1$, so the phrase "left-continuous" is false for this version. Correct statement:
- $\mathbf 1_{[0,\rho)}$ is right-continuous and $\mathcal F_t$-adapted ($\{t<\rho\}=\{\rho\le t\}^c\in\mathcal F_t$), hence optional and progressively measurable — sufficient for the Itô integral and for every statement in §2.2.
- The left-continuous version $\tilde w_t=\sqrt{N/\delta}\,\mathbf 1_{\{t\le\rho\}}=\sqrt{N/\delta}\,\mathbf 1_{[0,\rho]}(t)$ is left-continuous and adapted, hence predictable. $w$ and $\tilde w$ differ only on the graph $\{t=\rho\}$, a $dt\times P$-null set, so they have the same Itô integral $x_t=\int_0^t w\,dW=\int_0^t\tilde w\,dW$ (indistinguishable), the same $\|w\|^2_{L^2[0,T]}=\tau\wedge N$, the same support $[0,\rho]\subset[0,\delta]$, and the same $\|z\|$.

## Effect on the verdict
None. Every quantitative step (§2.1–§2.6), every exact control (A/B, 31/31), the negative controls, and the §6 verdict "VERIFIED at exact given-law scope; no FATAL/MAJOR" stand unchanged; "predictable" in §6 is read as applying to the indistinguishable left-continuous version $\tilde w$, and "progressive/adapted" to both. No mathematical counterexample to the witness is inferred or exists from this wording issue.

## Record discipline
Additive erratum; `review-v1.md` and `reviewer-receipt-v1.txt` are not modified. `reviewer-receipt-v2.txt` (additive) lists this file's hash.
