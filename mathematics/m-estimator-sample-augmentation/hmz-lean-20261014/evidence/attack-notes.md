# Full-goal attack notes and rejected inferences

2026-10-14 PT. These record mathematical attempts, not accepted counterexamples.
The fixed nested design and all-prefix consistency requirements were retained.

## Gram-only boundary attempt

For Gaussian LAD, the expected contrast at prediction shift t grows like
`min(t^2, |t|)`, rather than a uniformly positive multiple of t^2. A variance
bound for any *one* fixed parameter direction does not give the necessary
uniform boundary bound when the deterministic design is arbitrarily
anisotropic. A fixed finite Euclidean net can have enormous criterion
oscillations between its points under high leverage. No correct uniform
argument from Gram divergence alone was obtained in this attempt.

For a bounded-score local quadratic-core proof, whitened rows have
`sum ||z_i||^2 = p`, but their fourth powers need not tend to zero.
That is exactly why the formal curvature fluctuation bound retains d_n.
For the single nested scalar design x_i = 2^i,

    S_n = sum_{i=1}^n 4^i -> infinity,
    max_{i<=n} x_i^2/S_n -> 3/4.

Gaussian least squares is nevertheless consistent there, with variance
`sigma^2/S_n`, and has unique original and pooled minimizers. Thus even
original consistency in the frozen class does not force diffuse leverage.
The current sufficient theorem's extra design assumption cannot be inferred
just from the known Gram necessity result.

## Growing-stage polytope counterexample attempt

A possible way around the prior retained weak-direction penalties was to
give the new low-row population criterion an expanding weight and a flat
polytope of minima. A convex polytope can have fibers selecting weak value
zero at strong-coordinate vertices but larger weak fibers at averages of
vertices; this is the sort of geometry that could distinguish original and
pooled observations. Merely having this finite geometry does not construct
a stochastic nested counterexample.

For example with Rademacher errors and a fixed coercive convex loss
`rho(r) = |r| + lambda r`, `|lambda| < 1`, a row with |t| <= 1 has the exact
contrast

    rho(e-t)-rho(e) = -(e+lambda)t.

Across m independent such rows the random linear coefficient has size
sqrt(m), even if a design-pair construction cancels the population lambda
drift. A finite number of high rows with bounded errors have only order-one
loss differences in their rescaled strong coordinates. Thus they cannot
retain the supposed vertex pinning when those random low-row gradients grow.
Shrinking the low coefficients to suppress that fluctuation also shrinks
the fixed-scale shifts needed for a nonhomogeneous flat polytope. The small
shift limit returns to the homogeneous hinge geometry and the retained
weak-direction penalties diagnosed in the source target. No argument
reconciles these requirements, and no counterexample is claimed.

This is a diagnosis of this candidate mechanism, not an impossibility
theorem for all convex losses or all nested counterexamples.

## Smooth bounded-score result that survives the audit

The strictly convex loss sqrt(1+r^2)-1 avoids the pooled flat-minimum
obstruction of pure LAD/Huber while retaining bounded score and positive
curvature on every bounded residual interval. The written proof uses
contrast integrability, a random core Gram matrix, its exact independent
Frobenius second moment, and convex radial localization. It handles fixed
Cauchy errors, including a balanced-design noncentered variant. The required
vanishing leverage and drift/centering conditions remain explicitly partial.

The two-bounded-error-interval influence proof establishes Gram necessity
for everywhere positive globally upper-bounded curvature without an error
moment assumption. It does not supply the missing Gram-only stochastic
sufficiency or treat arbitrary nonsmooth convex losses.

## Research limit

Repeated direct publisher requests and primary-location searches did not
obtain the complete Zhao--Rao--Chen or Bai--Wu articles. The visible preview
and metadata are not a license to assume the missing theorem statements.
There is consequently no literature-based completion claim for the broad
implication. Required original-goal verdict: unresolved, reviewer done:false.
