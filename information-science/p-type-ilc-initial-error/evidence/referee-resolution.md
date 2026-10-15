# Hostile-referee disposition

Date: 2026-10-14 (PT). Independent-model command: `python3 work/run_referee.py`; exact CLI arguments, model identity, duration, and exit status are in `codex-referee-run.json` and `codex-referee.log`. The configured Codex delegate was `gpt-6.1-sol`, effort `max`, read-only sandbox; elapsed 524.39 seconds, exit 0. The saved prompt prohibited edits, network access, further delegation, and reading outside this target. The final reply is preserved verbatim in `codex-referee.md`.

## Verdict and fixes

| Claim / objection | Referee verdict | Disposition in `work/theorems.md` |
|---|---|---|
| A: Volterra spectrum prevents strict contraction | Correct with fixes | Replaced merely bounded gain by **continuous** gain for operators on `C([0,T])`; stated use of complexification. A discontinuous `L` can make `LG` leave `C`, so the original wording was too broad. Constant P0 gains were unaffected. |
| A: nonlinear derivative | Correct after clarification | Wrote the input-space learning map explicitly and its derivative `I-LG`, with fixed initial state, instead of leaving the operator space implicit. |
| B: all integer relative degrees, arbitrary bounded initial errors | **Correct** | The reviewer independently derived the resolvent/generating function, checked every sign/degree case, and validated the uniform-boundedness step giving **one infinite** bounded sequence. No mathematical correction needed. |
| B: time quantifier | Clarification | Made explicit `for each prescribed t_*>0, there exists a sequence`, not a single sequence asserted to diverge at all positive times simultaneously. |
| B: zero gain | Correct, make example explicit | Added `y_d=t^q/q!`, `u_d=1`, zero actual initial states/input, which directly fails nominal tracking when the gain is zero. |
| C: disturbance sign, repeated-integration indices, Gram positivity, error bound | Correct | Preserved the proof and recorded the reviewer's exact error identity and sharper intermediate bound `[1+κ(1-ρ^i)]δ`. |
| C: arbitrary bounded functions may not be integrable | Correct with fixes | Specified continuous disturbances in the present theorems. A bounded-measurable extension would need Carathéodory solutions/essential-sup norms; it is not silently claimed. The negative result already uses zero continuous disturbances. |
| C: bounded states do not imply containment within a local normal-form domain | Correct with fixes | Required `a,b` globally defined/continuous, locally Lipschitz in state, and `|b|>=b_min` globally; alternatively a local version would need separately established compact containment. The reviewer supplied `a(x)=1/(1-x)` on `x<1` as a counterexample to the original loose inference. Both simulated sine-drift plants meet the repaired global assumptions. |
| C: broader controller and realizability restrictions | Restrictions confirmed | Kept full-state exact cancellation, no internal dynamics, finite-dimensional target realizability, and whole-trace filtering explicit. No P0 or original-book full-solution claim was added. |

The repairs were checked directly: continuous multiplication preserves the `C` spaces; globally continuous coefficients are bounded on the common compact state set derived from the chain recurrence; and the explicit zero-gain example has the required relative degree. They do not change the rational identities or numerical controllers, so the already exercised numerical suite was not rerun merely to confirm unchanged results.

## Trust boundary

This is an independent model's mathematical review, not human peer review or a Lean/kernel certificate. The complete analytic proof is the certification artifact; exact rational tests only check its finite algebraic identities. The reviewer did not perform a literature/novelty audit, did not validate all source papers, and did not review the subsequently added finite nonlinear-coordinate diagnostic as a separate theorem. That diagnostic is labeled empirical, and no extra general theorem is inferred from it.

The broad original P-type design question remains unresolved by this attempt. Refuting P0 and validating a better-informed restricted benchmark must not be reported as fully solving it.
