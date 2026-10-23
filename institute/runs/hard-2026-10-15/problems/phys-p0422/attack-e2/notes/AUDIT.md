# Adversarial audit of the proof and certificates

This is an audit record of the human-readable proof. There was no external
contact or delegated review. The alternate numerical checker is an
algorithmically distinct implementation of the same formula, written by the
same producer in the prior attempt. It checks arithmetic, not the formula or
the analytic bridge. The written proof was rechecked line by line in this
continuation; it is not formally verified or externally refereed. The
supplied referee feedback is review data, not an authenticated publication.

Method attribution: the integer-cost, y-reweighted comparison is Vorobyev's
(2026) k=3 method, re-derived and extended to k here; the nonnegative degree-k
remainder is credited to Lelarge–Oulamara (2018), following the staged
preprint's condition-(4)/equation-(30) citation. No independent discovery or
verification of the preprint's claimed Lean development is asserted.

1. **Ground-state insertion is exact only with integer costs.** Section 2
   proves that assumption, rather than silently replacing finite-temperature
   Gibbs averages by frozen-variable indicators. The counterexample
   H=(0,1/2), V=(1,0) has increment 1/2. This is an illustrative counterexample
   to an extension, not a negative control of the checker. All costs in the
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
   the polynomial is -224. This illustrates a failed extension; it is not
   a negative control of the checker. No
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
    checks. It uses only t=exp(-y)=1/2 and the rate law giving equal mass
    to 1/4 and 3/4. Those finite counts do not establish the universal theorem;
    Sections 2–7 of PROOF.md do that analytically.

11. **Numerical replay cross-checks the same formula.** It reads only
    trials.json, not results.json or the producing code. Multinomial products,
    Taylor/reciprocal exponentials, a decimal grid, and atanh logarithms give
    the same signed margins as ordered products, elementary repeated-squaring
    bounds, a binary grid, and the direct log series. These are rigorous
    interval bounds. Algorithmic diversity can detect arithmetic mistakes;
    it does not independently establish the formula or the analytic bridge.

12. **Sanity controls.** Zero-warning trials have Psi=0 and are rejected by
    the required-negative-margin checks for both k. The same nonzero trial
    laws at densities 7.9 (k=4) and 18.7 (k=5) also fail certification; those
    densities lie below the lower bounds reported in the staged table.
    The staged k=3 trial at 4.268 is reproduced only as a functional check.
    Neither the k=3 preprint's theorem nor its claimed Lean formalization is
    used to justify the two requested results.

13. **The finite audit now has a real negative control.** The old
    --break-integer and --break-odd-domain modes asserted counterexamples
    without calling check_system; they did not test that checker. They are
    retained as aliases of --illustrate-noninteger and --illustrate-signed-odd
    and explicitly labeled illustrations. The new --break-comparison mode
    calls check_system at n=1, H=(0,1), k=5, with the two old sites
    (0,0,1/3) and (0,1,2/3). It first passes with the correct expression, then
    reverses only the sign of the (k-1)d_y correction inside check_system.
    Exact log intervals give a strictly positive lower bound for the mutated
    expression, and the same upper<=0 assertion as in the ordinary audit
    rejects it. The replay requires both exit 1 and the comparison-failure
    message, so an unrelated exception does not count as detection.

14. **Expectation order and finite-n scope are explicit.** Equation (E) now
    states E_new[W_C^h]=<B_h^k>_h,
    E_new[W_S^h]=<B_h>_h C_h^(k-1), and E_new[W_D^h]=C_h^k,
    with old rows fixed and h independent old-activation replicas. Both
    B_h and C_h are in [0,1]. Inequality (A) holds for every n>=1; n>=k
    is imposed only for the distinct-variable transfer.

The two certified densities 9.96 and 21.14 are above the supplied cavity
estimates 9.931 and 21.117 and below the supplied upper benchmarks. This is
a sanity observation; the proof does not rely on those physical estimates.
