# Bounded verification protocol

Recorded before running the numerical suite, 2026-10-14 (PT).

## Claim, baseline, missing ingredient

* Claim: certify the analytic constant-gain pure-P impossibility in `theorems.md` for every integer relative degree; separately illustrate a finite-dimensional derivative-free filtered/state-feedback controller with a proved disturbance bound.
* Baseline: the exact book P0 update; initial-rectification/adaptive methods in the literature are not assumed equivalent to P0. No AI or optimality advantage is claimed.
* Missing ingredient for a full positive book solution: a controller-class-compatible theorem for general output-only nonlinear systems, not a better simulation score. The finite-dimensional benchmark does not supply it.

## Cheap checks and numerical protocol

1. Standard-library exact rational checks: independently derive the finite impulse coefficients using polynomial integration and using the binomial formula, for relative degrees 1 through 5 and horizon 10. Check the finite worst-case sign witness exactly for horizons 8, 32, 128, relative degrees 1 and 2, with gain one, `t*=1`, and `ε0=1/20`. Preserve numerator/denominator certificates. This checks identities, not the infinite quantifier of Theorem B.
2. Compute the `q=1` Laguerre impulse absolute sums at horizons 100, 1,000, 10,000, 100,000 as floating-point illustrations, not certificates.
3. Simulate the two nonlinear plants stated in Theorem C using physical-state RK4, `T=1`, 200 trials, `γ=0.7`, `ell=1`, nominal target `y_d=t^q`, constant virtual input `v=q! θ`, `θ0=0`. Use 400 and 800 uniform time steps, fixed seed `20261014+q`. Run both P0 and the filtered controller on the same bounded initial/disturbance arrays. P0 has no nonlinear cancellation; the filtered controller has exact state feedback, so this is not a matched-information benchmark.
4. Disturbance bounds: `ε0=0.02`, `εη=0.01`, `εξ=0.005`; use bounded random initial components and smooth random-phase sinusoidal process/measurement disturbances. Repeat zero-disturbance and half-amplitude cases for the filtered controller without tuning. No held-out generalization claim is made.
5. For the one-dimensional basis `ψ=t^q`, `κ=(2q+1)/(q+1)` exactly. Check every measured sup error against `(1-γ)^i ||y_d||∞+(1+κ)δ`, allowing `1e-5` discretization slack. Record any failure without silently changing gains or bounds.
6. Independently compare physical RK4 outputs with the analytic repeated-integral formula for the canceled plant. Use the analytic Gram integral `W=1/(2q+1)`, not a discretized direct-feedthrough model. Record coarse/fine differences, nominal residual, and all finite divergence/control-input observations.
7. Independently check the special-function generating function at selected interior complex points with 80-digit arithmetic, by summing impulse coefficients versus a root-of-unity exponential representation. These numerical checks supplement, not replace, the analytic proof.

All runs are cheap local verification, one process, one numerical thread, under 100 MB numerical memory. No large adaptive search or frozen computational campaign is justified by the mathematical blocker. Save commands, versions, seeds, errors, and raw trial metrics. Never label finite sampling as a proof of universal convergence or divergence.
