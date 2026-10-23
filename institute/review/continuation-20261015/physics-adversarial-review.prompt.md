# Focused independent mathematical audit

Read-only. No delegation, writes, shell, credential reads, external contact, or changes to any artifact. Read only under /Users/jinleic/repos/aifours/institute/review/continuation-20261015/ and /Users/jinleic/repos/aifours/institute/runs/hard-2026-10-15/problems/phys-p0422/attack-e2/. Do not load unrelated project or private context.

Audit the theorem, not just arithmetic. Read notes/PROOF.md, certificates/trials.json and code/certify.py / independent_check.py. The proof has already had two broad model-referee passes, so this review must be targeted and adversarial rather than another generic endorsement.

Question: For every fixed integer k>=2 and finite probability law rho on [0,1), does the displayed finite criterion Psi_T<=-epsilon, T exp(-y)<=epsilon/2 genuinely imply exponentially small SAT probability for random independent, uniformly signed, distinct-variable clauses at floor(alpha n)? Try to construct a counterexample or identify a quantifier/conditioning/sign/transfer error, focusing on:
1. New clause minima vs products of per-literal universal minimizer indicators under auxiliary-activation reweighting. Does factorization survive repeated variable indices and reused replicas?
2. Interchange of rows, auxiliary replicas, logarithmic infinite series and Poisson/binomial averaging. Is any needed integrability/positivity assumption missing?
3. The site-only upper bound and the direction of the finite-y / d_y vs d_infinity corrections. Can a finite T and arbitrary finite rho invalidate an inequality?
4. Whether fixed-count and distinct-variable transfers lose a positive linear margin, and whether the claimed bounded-differences concentration really has the stated factor2.
5. Are k=2, rho=delta0, rho very near1, empty minimizer concerns, n<k and small n logically handled? These are controls, not permission to shrink the target.
6. Compare the derivation to classical 1RSB principles: no invention/priority claim is made. State exactly which mathematical portion might be an independently written specialization rather than a new method.

Output a strict JSON object with keys verdict (correct|fixable-gap|fatal-gap|inconclusive), checked_steps, findings (each severity/location/objection/evidence/required_fix), strongest_supported_theorem, attempted_counterexamples, residual_trust. Distinguish reading a numerical checker from executing it. A correct verdict requires a reasoned audit of all six numbered points, not merely agreement with the prior reviewers.
