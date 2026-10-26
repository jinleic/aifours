# Wave v25 parent disposition — wording overlay 1

Actual clock before creation: **2026-10-24T06:52:23-0700 PDT**. Additive only; the frozen [wave-v25 disposition](wave-v25-ribbon-probe-parent-v1.md) and all receipts are unchanged. Author InfoGuessingRminus reported the error after reading the complete actual review and disposition.

## Correction

Disposition item 5 currently reads that a coordinate-revealing auxiliary is "automatically HC-disqualifying". That inverts the proved inequality. The core (Section F) and the actual review (Section 6) prove, for ANY finite FD law with Phi<0 and any finite auxiliary W determining a coordinate:

    3 I(W;X_V) - 2 sum_i I(W;X_i) = E_w Phi(X|W=w) - Phi(X) >= -Phi(X) > 0.

Rearranged, 2 sum_i I(W;X_i) <= 3 I(W;X_V) - (-Phi) < 3 I(W;X_V) is not the right reading either: the strict positive quantity is 3I(W;X_V) - 2ΣI(W;X_i) itself, i.e. the HC-expression slack computed with weights (2/3,…,2/3) is at least -Phi>0 in the SATISFYING direction. Such a probe therefore **automatically SATISFIES the (2/3,…,2/3) HC inequality with slack at least -Phi>0 — it is HC-redundant, unable to disqualify a negative law**. That is precisely why a useful probe of a hypothetical negative minimizer must avoid determining any nonconstant coordinate; the disposition's following sentence already said this and remains correct.

No other item changes. Item 5's second sentence, all mathematics in the actual review Section 6, the frozen candidate bytes and every receipt are unaffected. This overlay is binding on any future reading of the disposition.
