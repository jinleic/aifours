# Addendum 1: f677 candidate corrections and ACK count

Observed native clock before creation: `2026-10-30T16:01:32-0700 PDT`. The original `author-candidate-v1.md` is preserved unchanged; this addendum must accompany it in any assessment.

1. In Section 4 replace the sentence “All four `ell=0` E-row D blocks are consequently D3 or F” by: **All six `ell=0` E-row D blocks are consequently D3; the other two E-row blocks are F.** This follows because all four D0 blocks lie in `ell=1` graph mates. Later counting in the candidate already treats an H-cell as containing at most one magnitude-two E-row entry, and is not based on the erroneous number four.
2. In Section 6, the direct graph-transform check should say the possible values are **0, `±16`, or `±8`**, not “zero, 16, or `±8`”: the `ell`-frequency character may change the sign of a magnitude-16 coefficient. The only conclusion used is divisibility by eight, which remains valid.
3. The initial direct PREBODYACK said 19 manifest status controls. In fact **all 20** listed controls, including the prospective-author method-restoration control, were read completely through their endings before that ACK. The count was corrected additively in a direct status message to Main; packet reading and mathematical derivation occurred after the original ACK. This does not backdate or replace that message.

Both mathematical corrections are identified by the author without scientific execution. This addendum and the candidate remain unreviewed author work and do not change the stated unpaid original-caller obligations or assurance limits.
