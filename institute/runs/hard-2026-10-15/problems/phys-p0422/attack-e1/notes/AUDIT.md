# Adversarial audit of the proof and certificates

This is a separate audit record of the human-readable proof. There was no
external contact or delegated review. The numerical checker is independent
code; the mathematical proof has not been checked in a proof assistant.

1. **Ground-state insertion is exact only with integer costs.** Section 2
   proves that assumption, rather than silently replacing finite-temperature
   Gibbs averages by frozen-variable indicators. The counterexample
   H=(0,1/2), V=(1,0) has increment 1/2. The negative control rejects an
   attempted 0/1 identity on it. All clause and activated-site costs in the
   proof are integers. No finite-temperature insertion formula is asserted.

2. **Correlations among minimizers are retained.** The new clause indicator
   is a conjunction, so the universal quantifiers commute. The average
   <product b> is not replaced by product <b>. The independent replicas in
   Section 3 share the same new seed at each literal position. This is what
   yields <B_h^k>, rather than <B_h>^k. The small checks calculate actual
   new minima before comparing to the insertion identity.

3. **The odd-arity condition is explicit.** B_h and C_h are nonnegative
   indicator averages and rate moments. The factorization (F) is nonnegative
   for every such pair. Dropping this domain fails at B=-3,C=1,k=5, where
   the polynomial is -224; a negative control checks that failure. No
   signed-overlap hypothesis from an even-arity spin-glass theorem is used.

4. **Signs in the interpolation are fixed by finite induction.** The local
   inequality is Delta_C-k Delta_S+(k-1)d_y<=0; its Poisson average is
   f_clauses<=f_sites-(k-1)alpha n d_y. Since d_y is negative, its correction
   is positive. Later, d_y>=d_infinity implies the correction with d_infinity
   is an upper bound. Changing either sign would make the certificate invalid.

5. **The outer and inner expectations stay distinct.** Only site activation
   coins are averaged before log; indices, signs, and rates are averaged
   after log. The tilted law mu_y belongs to the old activations, independently
   of each fresh row. The sites-only calculation conditions on rows before
   exploiting independent activation groups. Marked-Poisson splitting is
   used only after averaging the number of rows.

6. **Truncations have rigorous signs.** The finite site-log sum drops negative
   terms, giving an upper bound. The finite-y error is at most T exp(-y).
   The positive correction uses an upper bound on -log(1-z), including its
   geometric tail. Alternating moment sums use outward intervals, not binary
   floating arithmetic. Negative lower endpoints for mu are clamped to zero
   before squaring. There is no degree truncation: exact Poisson generating
   functions sum the complete degree distribution.

7. **Finite y is chosen before n tends to infinity.** The exact checks prove
   the error bound at y=20. No numerical or analytic infinite-y limit is
   assumed. The optional finite-temperature comparison in Section 5 has an
   explicit per-variable error y log(2)/beta; it is not a premise of (A).

8. **Both ensemble changes have explicit expected losses.** They are at most
   sqrt(alpha n)+1 and alpha binom(k,2). Clause replacement changes energy
   by at most one, rather than introducing an unaccounted factor or loss
   proportional to n. Retaining fair signs while resampling bad variable
   tuples produces independent, fair signed distinct-variable clauses.

9. **A positive expectation is converted to high probability.** Doob
   differences for the independent fixed-count clause model have conditional
   range at most one. The resulting exponential lower-tail bound is applied
   at the positive expected energy. Poisson concentration is not asserted
   directly for an unbounded number of clauses.

10. **The finite audit has an exact stated range.** It checks all integer
    tables H:{0,1}^n->{0,1,2}, n=1,2, four specified old-site systems, and
    k=3,4,5. This gave 1,080 local comparisons and 1,203,048 clause insertion
    checks. Those finite counts do not establish the universal theorem;
    Sections 2–7 of PROOF.md do that analytically.

11. **Numerical replay is independent at the algorithm level.** It reads only
    trials.json, not results.json or the producer. Multinomial products,
    Taylor/reciprocal exponentials, a decimal grid, and atanh logarithms give
    the same signed margins as ordered products, elementary repeated-squaring
    bounds, a binary grid, and the direct log series. These are rigorous
    interval bounds, not independent sampling.

12. **Sanity controls.** Zero-warning trials have Psi=0 and are rejected by
    the required-negative-margin checks for both k. The same nonzero trial
    laws at densities 7.9 (k=4) and 18.7 (k=5) also fail certification; those
    densities lie below the lower bounds reported in the staged table.
    The staged k=3 trial at 4.268 is reproduced only as a functional check.
    Neither the k=3 preprint's theorem nor its claimed Lean formalization is
    used to justify the two requested results.

The two certified densities 9.96 and 21.14 are above the supplied cavity
estimates 9.931 and 21.117 and below the supplied upper benchmarks. This is
a sanity observation; the proof does not rely on those physical estimates.
