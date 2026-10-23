# Parent-written finite-trial checker

`sat_independent_certificate.py` was implemented from the finite criterion in the written proof, without importing either trial producer/checker. It shares Python arbitrary-precision arithmetic and the mathematical formula with them; a different implementation does not independently establish the analytic bridge.

## Exact exponential enclosure

Use the dyadic grid `D=2^P`, with default `P=768` and `--precision-bits` for larger cutoffs. For a nonnegative rational `t`, monotonicity first bounds it by adjacent grid points. For each dyadic endpoint write `t=m+f` with integer `m>=0` and `0<=f<1`. The alternating Taylor series for `exp(-f)` has nonincreasing nonnegative term magnitudes. Every odd partial sum is a lower bound and every even partial sum an upper bound. The implementation brackets every term by integer floor/ceiling at grid scale, picks the correct endpoint for its sign, and returns an odd lower partial sum and its preceding even upper partial sum. Additional outward two-unit padding is conservative.

An independently formed exact rational bracket `S_399 <= exp(-1) <= S_400` supplies the integer part. Multiplication with outward integer rounding brackets `exp(-f)*exp(-1)^m`. Rational argument rounding is in the correct decreasing direction. All factors are nonnegative; an underflowing lower endpoint is clipped only to zero. These are interval enclosures, not assumptions about floating-point error.

## Logarithm upper bounds by an inverse inequality

For each exact rational product `W` in `[0,1)`, the checker proposes a dyadic `L` using mpmath, but accepts it only if its rigorous upper enclosure for `exp(-L)` is at most the exact rational `1-W`. Monotonicity then proves `-log(1-W) <= L`. The proposal is untrusted; failure to certify raises an error rather than supplying a fallback. `W=0` is handled by the exact value zero.

This differs from both existing checkers' direct logarithm-series approaches. The producer's exponential uses repeated squaring of tangent/reciprocal bounds; its alternate checker uses a positive Taylor series, reciprocal and seven squarings. The parent uses a signed alternating series and integer/fractional argument decomposition.

## Finite criterion

Products of the input rational law are enumerated and aggregated exactly. For the `(k-1)`-fold product `Q`, all `nu_i=E(1-Q)^i` are exact Fractions. The exponential interval encloses each `M_i=exp((k alpha/2)(nu_i-1))`. Alternating binomial sums select interval endpoints by coefficient sign to enclose `mu_j`, then intersect with its mathematically known range `[0,1]`. Squared lower endpoints give a lower bound on the nonnegative site sum. Upper logarithm bounds give an upper bound on the positive correction, yielding a rigorous `Psi_T` upper bound.

The alternating sum for `mu_j` amplifies grid errors by about `2^j`. A grid that is too coarse therefore remains rigorous but becomes weak: once an enclosure collapses to `[0,1]`, that positive site term is omitted. At `P=768`, the checker reproduced every `T=512` row exactly, but could not certify a `T=1024` row. The successful `T=1024` checks use `P=1536`; both outcomes are kept as receipts.

The checker requires both `Psi_T <= -epsilon` and `T exp(-y) <= epsilon/2`, using exact rational comparisons. No probabilistic sampling, floating comparison, asserted producer value, or convergence of population dynamics enters these gates. Failure gates use explicit control flow, so Python optimization cannot strip them. Decimal displays are exact integer ceilings on their stated decimal grids; the decision uses the underlying Fraction, not its display. The sampled moment displays also use directed decimal bounds.

## Observed evidence

- `sat-independent-improved-bounds.json`: all four new trials passed, including the headline `k=4, alpha=3973/400=9.9325` and `k=5, alpha=8447/400=21.1175`, each at `T=512`, `y=20`, `epsilon=1/200000`. The displayed upper bounds on `Psi_512` are `-0.000005994158771864` and `-0.000006835683244470`; the tail upper bound is `0.000001055310654688541607918562 < epsilon/2`.
- Before these trials, the checker also reproduced the old k4/k5 margins and the published k3 reference. The old display-only receipts predate the exact decimal renderer; their rational acceptance gates were unchanged.
- `sat-independent-subcavity-controls.json`: the old same-law density controls reject 9.90 and 21.10 while accepting 9.96 and 21.14.
- `sat-satisfiable-region-control.json`: a seeded finite search over 1,366 rational three-atom trials at known satisfiable densities found no negative upper certificate. It approached the zero-warning limit. This is a weak consistency/falsification check, not a nonnegativity theorem or an exhaustive search.
- **Random 3-SAT extension.** The input `physics/evidence/hard-continuation-20261015/k3-extension/certificates/trials.json` has SHA-256 `88b6a0de…ab422`. At 1536 bits, the checker passes `alpha=426679/100000=4.26679` at `T=1024`, `y=24` and `epsilon=3/10^7`, with `Psi_1024 <= -0.000000430631052284`. It also passes `10667/2500=4.2668` at `T=512`, with `Psi_512 <= -0.000000673892448493`. See `sat-independent-k3-1536.json`.
  - **Controls.** These copy the same six-atom law and change only the density. The checker rejects 4.26678 at `T=1024` and both 4.26679 and 4.2667 at `T=512`; see `sat-independent-k3-controls-1536.json`.
  - **Precision diagnosis.** At 768 bits, the receipts `sat-independent-k3.json` and `sat-independent-k3-controls.json` reproduce the `T=512` value but leave the `T=1024` row unconfirmed. This is the precision loss described above, not a contradiction.

The general interpolation, finite-y, model-transfer and concentration argument has a separate adversarial read-only review in `physics-adversarial-review.json`. Its verdict is correct, with presentation and checker-gating suggestions. Neither that model review nor these numerical executions is human peer review or full Lean verification.
