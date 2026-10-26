# Next obligation: reverse-direction feasibility separation

Observed freeze clock: **2026-10-23T14:24:42-0700**, `/bin/date '+%Y-%m-%dT%H:%M:%S%z'`. This is a consequential continuation of the **same info-3 problem**, not a replacement or an additional problem slot. The original `selection-v1.md` and `proof-v1.md` remain unchanged.

The first manuscript gives finite-gain comparison factors, not a prescribed-gamma characterization. The next exact question is whether a mean-square feasible controller can fail to imply **existence of any controller** under the literal printed norm at the same gamma. The old gamma6 baseline proves only the opposite implication fails. A genuine reverse-direction example would close a distinct route ambiguity rather than repeat that baseline.

## Model and target frozen

Seek an **infinite-horizon**, continuous-time, constant-matrix example with a strictly positive finite preview length, nonzero effective drift actuation and control-dependent diffusion, full-rank control cost, internal mean-square stability under an exhibited controller, and all adapted square-integrable disturbances. Require:

1. A controller of the book's state/window form with mean-square induced gain strictly below one exact `gamma`.
2. For **every** nonanticipative adapted controller, including nonlinear/history-dependent laws and all preview pre-action, literal induced gain strictly greater than that same `gamma`.

Use the cascade

`dx1 = kappa(-x1+w(t-h))dt`,

`dx2 = (-epsilon*x2+u)dt + (x1+u)dW`,

`z=(x2,r*u)`, `x(0)=0`.

All coefficients are constant. The candidate parameter scale is `epsilon=2^-29`, `h=2^-29>0`, `kappa=2^28`, `r=2^43`, and `gamma=16386`. These are exact rational values, not numerical optimizer outputs. The proposed comparison controller is `u=0`. The adversarial input is `w(t)=1_(t<tau)`, where `tau` is the first Brownian exit from `(-1,1)`; this is adapted, has `E integral w^2=1`, and does not inspect future noise. The plant receives the actual **delayed** input `w(t-h)`. Its delayed filtering error must be bounded explicitly rather than silently setting `h=0`.

## Missing ingredient and attack

Prove an explicit strict inequality `E sqrt(tau)<1`, use the stopped Brownian output as a lower anchor for the slow OU state, and quantitatively control both the low-pass and positive-delay errors. Then bound the entire control-only stochastic response in the **literal** norm and use the separate `r*u` output channel to prove an all-controller lower bound. The resulting no-go must include preview pre-action, not assume the controller is inactive before a disturbance arrives.

Pre-freeze disclosure: informal written reasoning after the assigned SPR review identified the stopped-Brownian construction, an elementary Jensen-gap bound, and a triangle-inequality route to the control-cost lower bound. No numerical/scientific execution or new scientific manuscript had been produced for it before this addendum. This is an explicit disclosure, not a claim that all mathematical thinking began after file creation.

## Verification boundary

A complete immutable manuscript must state all plant matrices, horizon, input/control admissibility, exact gamma margins, and source/dependency pins. It may use the already written source-checked monotone Lenglart transfer only with an explicit dependency on `proof-v1.md`; it may not import an unmatched Riccati theorem. All estimates must be written, including the stopping-time and positive-delay steps. Separate reconstruction and parent review are required before correctness acceptance. No scientific execution, solver, simulation, external-model CLI or kernel replay is authorized. Novelty remains UNCLEAR until primary comparison; a successful example is a counterexample to same-level substitution, **not** full N&S synthesis.
