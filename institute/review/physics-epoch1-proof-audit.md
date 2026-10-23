# Parent audit of the physics epoch-1 analytic bridge

Source inspected: `runs/hard-2026-10-15/problems/phys-p0422/attack-e1/notes/PROOF.md`, sections 1–8.
This is a written-proof audit, not a Lean/kernel check, human peer review, or novelty clearance.
The numerical certificates and the independent referee's eventual verdict remain separate evidence.

## Load-bearing steps checked

1. **Integer insertion (C).** If every old minimizer incurs the new 0/1 penalty, each old minimizer
   moves up by one and every nonminimizer already costs at least that much. Otherwise an old minimizer
   survives unchanged. Integrality is essential; the argument does not silently extend to fractional costs.
2. **Forced literals and replicas (D–F).** Universal quantification over minimizers commutes with the
   conjunction of all k violated literals. Replicas share each new literal seed but distinct literal
   positions are independently sampled. The resulting quantities B_h and C_h are nonnegative. The
   factorization `(B-C)^2 Σ_{ell=0}^{k-2}(ell+1) B^(k-2-ell) C^ell` is nonnegative for all k≥2, including
   k=5. No signed-overlap or even-k hypothesis is being borrowed.
3. **Log expansion and finite replacement (G–I).** For finite y, q<1 makes the log series uniformly
   absolutely bounded by y, permitting the stated averages. The binomial induction has the correct
   correction coefficient. Mixing N~Poisson(kαn) makes the binomially thinned clause count Poisson(αn).
   The linear bound y(K+L) controls those expectations.
4. **Site probability and finite-y estimate (J–M).** A_v+B_v−A_vB_v is the probability that a variable
   can avoid all site violations. Replacing its minimum violation count by the conflicting-variable
   indicator gives an upper bound on the negative exponential moment, in the stated direction.
   Marked Poisson splitting gives the exact compound-Poisson moments. The truncated negative log
   series is an upper bound, and `1-(1-exp(-y))^j ≤ j exp(-y)` yields the explicit T exp(-y) error.
   Since d_y≥d_infinity and its coefficient is negative, replacing it preserves the upper bound.
5. **Model transfers (N–P).** Coupling Poisson and fixed clause counts loses at most sqrt(αn)+1 in
   expected minimum cost. Resampling repeated variable tuples to independent proper tuples loses at
   most α·binom(k,2) in expectation. Retained signs stay independent and fair. Both losses are
   sublinear, and the supplied N0 bounds make the final expectation at least c0 n/2.
6. **High probability (Q).** Replacing one independent proper clause changes the energy by at most
   one. Conditional martingale-difference ranges therefore have length at most one, supporting the
   displayed bounded-difference tail. Applying it at t=E[energy] gives an exponentially vanishing
   satisfiability probability for n≥N0, without assuming existence of a limiting threshold constant.
7. **Scope of the numeric pair.** 249/25=9.96 and 1057/50=21.14 are below the opened historical
   comparison entries 10.23 and 21.33. Verifying them does not prove exact thresholds, optimality,
   current-best status, or the other four book challenges. The exact interval computations still
   need their successful independent replay; this audit does not substitute decimal values for it.

## Disposition

No analytic gap was identified in these steps on this pass. If the exact numerical premises pass
independent checking and the referee accepts the same statement, the written argument supports the
specified k=4,5 UNSAT bounds in the distinct-variable, fixed-count model. It remains partial progress
on the broad book challenge, with priority unresolved. Do not describe this audit as formal verification.

## Numerical implementation audit

Parent inspected `code/certify.py` and `code/independent_check.py` in the same immutable snapshot.
The checker imports no producer or stored numeric-result module. It enumerates multinomial
compositions rather than ordered tuples, uses a decimal fixed-point grid rather than a binary grid,
and bounds exponentials by positive Taylor terms plus a geometric tail followed by reciprocation,
rather than the producer's tangent/reciprocal seed and repeated squaring. Its logarithm uses an
atanh series with a positive-tail bound; the producer uses the direct positive log series.

Both moment calculations use exact rational trial inputs. Signed binomial sums choose the correct
opposite interval endpoint for negative coefficients, clip only to the analytically proved [0,1]
range, and reverse endpoints when subtracting squares. Clause-correction bounds have the correct
positive sign. All certification assertions use integer/Fraction arithmetic, not displayed decimals.
The independent finite-y check bounds T·exp(−y) outward and requires the stated half-margin.

No enclosure-direction error was identified in this pass. Executed numerical replay and its negative
controls must still be read from the generated replay receipts; this static audit is not their replacement.
