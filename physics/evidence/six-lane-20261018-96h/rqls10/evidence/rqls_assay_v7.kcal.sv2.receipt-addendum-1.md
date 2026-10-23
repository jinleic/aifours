# Addendum 1 to evidence/rqls_assay_v7.kcal.sv2.receipt.md (sha256 0a2e39e93974bd1ead961cc2b2d87c39efaa6b25f9975ae65c9dc54a0af06881)

Recorded 2026-10-19T01:17:34-0700, after the parent's scope note. The receipt is not edited; this addendum supersedes its "Interpretation"
paragraph and one phrase.
1. Replace "one implementation / one exact-arithmetic-free float program" by: one float implementation (numpy LM and
   verifier); numerical results only; no exact or formal verification.
2. Replace the interpretation by: on the finite recorded instances, the reduced parametrisation/LM recovered the known
   classical points (KP 16/16 at amplitudes 1e-3, 1e-2, 0.1; 13/16 at 0.5; KR 48/256). This does NOT establish that the
   parametrisation or Jacobian is sound in general, and the ~19% per-start recovery of known classical solutions does
   NOT transfer to unknown (maximal) configurations: any detection-rate statement for targets is [INFERENCE], not assay
   power. Sensitivity for maximal targets remains uncalibrated.
