# Axial negative-paw local-ring terminology erratum v1

Observed correction clock: **2026-10-24T03:16:10-07:00**. PhysicsRQLS10, adopting the second issue reported by InfoHinfPreview during actual reconstruction. Pinned originals remain unchanged. No confirming scientific execution was run.

Affected source: `axial-negative-paw-fourth-order-v1.md`, SHA256 `a93b22f594d335cfff8c0c5962ba4a522c10db89ec9a1893008c9d0bc7e35536`, lines47–50. The words “define local-ring units” incorrectly describe

    beta_R=4s/[-2p+s(n+q)],
    beta_L=4s/[-2p+s(n-q)].

The corrected statement is: **the denominators are local-ring units; beta_R and beta_L are local-ring elements of valuation exactly1, not units.** The denominators reduce to-2p≠0 modulo(s), while4s has valuation1. Both beta functions start-2p*s.

The independent left and right changes v→v+beta*e_H are elementary unipotent basis changes and remain invertible; their inverses subtract beta and never divide by beta. The fourth-order argument uses beta's order of vanishing and the invertibility of its denominator, not an inverse of beta. This is the author's impact description, not a replacement for the reviewer's final severity or full theorem verdict.

Read this together with `axial-negative-paw-coefficient-erratum-v1.md`, which corrects the hub fixed mixed coefficient0→-2d0, and `axial-negative-paw-count-erratum-v1.md`, which qualifies the parallel-leaf paw count. They repair separate statements and all remain mandatory. No other printed formula or source pin is replaced. The whole axial candidate is still pending completion of its own actual reconstruction and parent disposition.
