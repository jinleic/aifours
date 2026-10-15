# Mathematical progress: nested-design replication

Date: 2026-10-14 PT. **The original full goal is unresolved in this attempt.**
The results below are partial, with their additional hypotheses displayed.
Neither artifact-check success nor these partial results warrants reviewer
`done:true`. No independent reviewer was launched by this actor.

## Scope and the existing theorem

The target is still the implication for every fixed finite convex coercive
loss, every identifiable iid error law, and one deterministic nested
eventually spanning design, with almost-sure uniqueness of both sample
minimizers. No error moment or population identification condition has been
added to that target.

The existing target's Theorem 9 is retained as existing work: a fixed C2
loss with global `0 < m <= rho'' <= M`, finite-variance iid errors, and an
independent replicate with exactly the same law. Its bounds are centered at
the deterministic population minimizer theta_n, respectively
`M^2 Var(epsilon) p / (m^2 lambda_min(S_n))` and one half of that bound.
It does not assume score centering. Nondegeneracy is needed for its Gram
necessity/characterization, not for replication; a degenerate law gives
identical criteria up to a factor of two. Nothing below is a relabeling of
that theorem.

## 1. A uniqueness obstruction to the suggested Gaussian LAD/Huber route

**Proposition U (written proof; scalar Huber algebra also formalized).**
Suppose F has positive probability in both tails beyond every finite
threshold. For any finite deterministic design and independent same-law
replication, pure LAD and symmetric Huber have a positive-probability event
on which the pooled criterion has a ball of global minimizers. Consequently
these Gaussian-error experiments do not satisfy the frozen goal's
almost-sure pooled uniqueness hypothesis. This is an incompatibility result,
not a counterexample to the replication implication.

Translate beta_0 to zero. Fix r > 0, and put
`a_i = r ||x_i||`. In the Huber case let the fixed threshold be k > 0.
The independent event

    epsilon_i >= k + a_i,  epsilon'_i <= -k - a_i,  all i <= n

has strictly positive probability, a finite product of positive tail
probabilities. For any h with ||h|| <= r, put t_i = x_i'h. Each positive
residual is in the right linear tail and each negative residual is in the
left linear tail. Their paired loss is exactly

    rho_k(epsilon_i - t_i) + rho_k(epsilon'_i - t_i)
       = k(epsilon_i - epsilon'_i) - k^2.

For *every* real t, the same paired loss is at least that constant: use
the two global supporting affine functions `k s - k^2/2` and
`-k s - k^2/2`. Summing proves global minimality at every point of the
closed r-ball. Since p >= 1, there are distinct minimizers. Zero rows cause
no difficulty. For LAD omit k from the tail thresholds; the triangle
inequality gives the paired lower bound `epsilon_i - epsilon'_i`, attained
throughout the same ball. A nondegenerate Gaussian or Cauchy law has the
required tail probabilities. Uniqueness need not fail for every outcome;
a positive-probability failure is enough to exclude almost-sure uniqueness.

The result does not exclude LAD/Huber with all other error laws, and does
not turn a tie selector into a counterexample. Sufficiency for *all*
minimizer selections would still be useful theory. The remainder uses a
strictly convex smooth bounded-score loss to obtain an admissible new case.

## 2. Gram necessity beyond a global lower curvature bound

**Proposition N (written only).** Let rho be fixed C2, finite, convex,
coercive, with `0 < rho''(s) <= M < infinity` for every real s; its infimum
may be zero. For a nested eventually spanning design and a nondegenerate
iid error law, consistency of the unique minimizer forces
`lambda_min(S_n) -> infinity`. No error moments, density, score centering,
or expected loss are used.

Here is the full modification of the influence argument. If Gram divergence
fails, the decreasing inverses S_n^{-1} have a nonzero positive-semidefinite
limit B. The spanning fixed prefix contains an x_i with
`c = x_i' B x_i > 0`, so `x_i' S_n^{-1} x_i >= c` for all later n.
Fix every response other than y_i. Strict positivity of rho'' and the
spanning design make the finite-sample Hessian positive definite; the
implicit function theorem gives a continuously differentiable fitted
value `g(y_i) = x_i' beta_hat(y_i)` with

    g'(y_i) = rho''(y_i-g(y_i)) x_i' H^{-1} x_i
            >= (c/M) rho''(y_i-g(y_i)) > 0.

The Hessian upper bound is global: `H <= M S_n`. A global *lower* bound
on rho'' is not used.

Choose two bounded closed error intervals A = [a_0,a_1], B_1 = [b_0,b_1]
with a_1 < b_0 and positive masses q_A and q_B. Such intervals exist for
any nondegenerate real law, including atoms. Write `v_0 = x_i' beta_0` and

    m_* = min { rho''(s) : a_0-1 <= s <= b_1+1 } > 0,
    eta = min(1/2, c m_* (b_0-a_1)/(4M)) > 0.

For the fixed other responses, there cannot be a response from *each*
error interval whose fitted value is within eta of v_0. Otherwise monotonicity
of g keeps its fitted values inside that small interval on the whole path
between the two responses. Its residuals then stay in
`[a_0-1,b_1+1]`, and integration of the derivative lower bound forces a
fitted-value separation at least `c m_* (b_0-a_1)/M > 2 eta`, a contradiction.
Thus at least one entire error interval gives fitted-value error > eta.
Independence leaves its conditional law equal to F. The unconditional
failure probability is at least `min(q_A,q_B) > 0`, contradicting consistency
of the fixed fitted value. This establishes Gram necessity.

This proposition does **not** assert universal Gram necessity: LAD is not
C2 with everywhere positive curvature, so the atomic bounded-Gram LAD
example in the existing Theorem 4A is unaffected. Pure Huber also lacks the
required positive curvature. For the smooth loss in section 4 this is a
genuine extension of the existing necessity argument to an infimum-zero
curvature regime and arbitrary nondegenerate error laws; no literature
priority is asserted.

## 3. A self-contained bounded-score sufficiency theorem

**Theorem S (written proof; the stochastic matrix bottleneck is Lean-proved).**
Fix p, one nested deterministic eventually spanning design, and a fixed
finite convex coercive C1 loss rho with measurable score psi = rho'. Assume

1. `|psi(s)| <= L < infinity` for all real s;
2. `E psi(epsilon) = 0` for the fixed iid error law F;
3. constants a > 0, K >= 0, m > 0 have
   `q = P(|epsilon| <= K) > 0`, and

       rho(e-t) - rho(e) + psi(e)t
         >= (m/2) 1{|e| <= K} t^2       for |t| <= a;

4. `lambda_min(S_n) -> infinity` and
   `d_n = max_{i<=n} x_i' S_n^{-1} x_i -> 0`.

Then every measurable minimizing selection is weakly consistent. Independent
same-law exact replication is also weakly consistent. A globally strictly
convex rho makes all minimizers unique, as required by the frozen target.
These are extra assumptions defining a partial regime. In particular,
score centering and vanishing leverage are not derived for the full target.

There is **no error first- or second-moment assumption**. Indeed, bounded
score makes rho L-Lipschitz, so each population *contrast*
`rho(e-t)-rho(e)` is integrable, bounded in absolute value by L|t|.
The expected uncentered loss may be infinite; it is never used in the proof.
The score variance `v = Var(psi(epsilon)) <= L^2` exists.

For n with S_n > 0 set

    z_i = S_n^{-1/2} x_i,       sum_i z_i z_i' = I_p,
    B_i = 1{|epsilon_i| <= K},  G_n = sum_i B_i z_i z_i',
    Z_n = sum_i z_i psi(epsilon_i).

The B_i are independent Bernoulli variables of mean q. They may be correlated
with their own scores; independence of G_n and Z_n is neither asserted nor
used. Pairwise independence across observations and centering give

    E ||G_n-q I||_F^2 = q(1-q) sum_i ||z_i||^4
                       <= q(1-q) p d_n,
    E ||Z_n||^2 = v sum_i ||z_i||^2 = v p.

The Frobenius bound follows from the actual entrywise independent variance
calculation, not from a Gibbs distribution variance inequality. The identity
`sum_i ||z_i||^2 = p` and `||z_i||^2 <= d_n` give its last step.
Markov's inequality and `||A||_op <= ||A||_F` imply

    P(lambda_min(G_n) < q/2) <= 4(1-q) p d_n / q.

More precisely, our good event is `||G_n-qI||_F < q/2`, which ensures the
displayed eigenvalue lower bound and has the same failure bound.

Put `h = S_n^{-1/2} u` and fix R > 0. When `R sqrt(d_n) <= a`, every
individual prediction shift on ||u|| <= R is at most a. Summing assumption
3 gives the exact, sample-dependent local lower bound

    F_n(beta_0+S_n^{-1/2}u) - F_n(beta_0)
       >= -u' Z_n + (m/2) u' G_n u.

On the good matrix event this is positive on the R-sphere whenever
`||Z_n|| < m q R/4`. A convex function with f(0)=0 and strictly positive
values on that sphere has every global minimizer inside the sphere: if a
minimizer lay on or outside, its radial contraction to the sphere would
have value <= f(0), contradicting positivity. Hence

    P(||S_n^{1/2}(beta_hat_n-beta_0)|| >= R)
      <= 4(1-q) p d_n/q + 16 v p/(m^2 q^2 R^2),             (S.1)

whenever `R sqrt(d_n) <= a`. This argument also applies to nonunique
minimizers and controls every selection on the good event.

For each fixed R, the first term tends to zero and the local-shift condition
holds eventually. Taking R large makes the second term arbitrarily small,
so the normalized errors are tight. For any fixed delta > 0,
`delta sqrt(lambda_min(S_n)) >= R` eventually, and error >= delta implies
normalized error >= R. Thus consistency follows. This is the order of
limits; it does not replace R by a growing radius without checking the
local-shift condition.

Exact replication uses `2 S_n`, rows `z_i/sqrt(2)` twice, and independent
same-law errors. Its maximum normalized leverage is `d_n/2`; the same q,
m, v, and score centering apply. The bound becomes

    P(||(2S_n)^{1/2}(beta_tilde_2n-beta_0)|| >= R)
      <= 2(1-q) p d_n/q + 16 v p/(m^2 q^2 R^2),             (S.2)

when `R sqrt(d_n/2) <= a`. The score term in this *normalized* bound has
not been halved. Replication halves the fourth-moment/curvature fluctuation
term and doubles the physical Gram matrix. This differs from Theorem 9's
theta_n-centered Euclidean mean-square bound.

**Noncentered variant (written).** Score centering can instead be replaced,
in this partial theorem, by the explicit deterministic design/score bound

    sup_n ||b_n|| <= C < infinity,
    b_n = E psi(epsilon) S_n^{-1/2} sum_{i<=n} x_i.

Write Z_n as its centered version plus b_n. The centered version still has
second moment v p. For `m q R/4 > C`, the score failure bound in (S.1) becomes
`v p/(m q R/4-C)^2`; the matrix term is unchanged. The same order of limits
proves consistency. Replication replaces b_n by `sqrt(2) b_n`, still uniformly
bounded, and replaces d_n by d_n/2. This proves replication in this variant
without assuming a zero mean score. The deterministic drift bound is an
extra hypothesis here, not a conclusion derived for the full frozen goal.

For Huber, assumption 3 holds with m = 1 and K = k-a when 0 < a < k.
`Replication.huber_core_remainder` proves precisely this scalar inequality.
Pure Huber remains excluded by Proposition U for unbounded two-sided laws
under the frozen uniqueness requirement; (S.1) still controls all selections.
For LAD there is no pointwise quadratic remainder of this type, even at
typical individual observations. The present curvature proof therefore
does not prove LAD sufficiency. Its stochastic local-increment/convexity
argument remains a different bottleneck.

## 4. A genuinely admissible smooth case with infinite-variance errors

Take the fixed loss

    rho(s) = sqrt(1+s^2)-1,
    psi(s) = s/sqrt(1+s^2),
    rho''(s) = (1+s^2)^(-3/2).

It is finite, coercive, strictly convex, C2, and has bounded score, while its
curvature infimum is zero. On `|e| <= K`, `|t| <= a`, Taylor's integral
remainder gives assumption 3 with
`m = (1+(K+a)^2)^(-3/2) > 0`. Outside that core the convex supporting-line
inequality gives the required nonnegative remainder.

With a centered symmetric Cauchy law, psi is odd and bounded, so its
ordinary expectation is zero although the errors have no first or second
moment. Every K > 0 has q > 0. The Cauchy location law is identifiable:
distinct shifts change its density; a spanning prefix transfers this to
identifiability of beta. Full-rank finite design criteria are coercive and
strictly convex, so both original and pooled minimizers exist uniquely for
every n beyond the spanning prefix. The argmin is a measurable continuous
function of the finite response vector (local uniform coercivity and the
usual compact-subsequence argument prove continuity).

For example let x_i cycle through e_1,...,e_p. This is one fixed infinite
nested design, `lambda_min(S_n) = floor(n/p)` for n >= p, and
`d_n <= 1/floor(n/p)`. Theorem S proves original and pooled weak consistency
for every fixed p and beta_0. This is an actual admissible asymptotic case,
not a finite simulation or an n-dependent loss; it lies outside the existing
Theorem 9 both in curvature and in error moments.

An example with a **nonzero mean score** is any fixed nonzero shift of the
symmetric Cauchy law with rows cycling `e_1,-e_1,...,e_p,-e_p`. The sum of the
design rows stays bounded along every prefix, so b_n tends to zero and is
uniformly bounded once the design spans. Strict increase and oddness of psi
make its mean nonzero for a nonzero positive or negative location shift.
The noncentered variant gives original and pooled consistency with the same
unique smooth-loss minimizers and infinite error moments. The error law is
fixed throughout, including in the independent replicate.

More generally, for this smooth loss and any nondegenerate law satisfying
score centering, Proposition N derives Gram divergence from original
consistency. If vanishing normalized leverage is separately assumed,
Theorem S finishes the replication implication. Bounded design rows imply
vanishing leverage once Gram divergence holds. Neither bounded rows nor
vanishing leverage is part of the original full goal.

## 5. Lean component and trust boundary

`Formal.lean` is self-contained apart from direct Mathlib imports. Its
principal stochastic claims are an exact Bernoulli matrix second moment,
integrability of that square, its leverage/trace bound, and the resulting
tail bound on an arbitrary probability space. The proof derives the variance
of binary observations and uses independence to remove cross terms. The
scalar Huber supporting-line, quadratic-core, and opposite-tail paired
minimum identities, contrast integrability, and convex radial localization
are also proved. There are 21 claimed positive declarations, all printed,
with their actual axiom lists recorded in `claims.json` after elaboration.

The Frobenius fluctuation bound is the precise stochastic bottleneck in
Theorem S, including its smooth example. The Huber paired minimum proves
the scalar algebra underlying Proposition U. The whole asymptotic theorem,
Proposition N, Gaussian/Cauchy tail positivity, matrix whitening, and the
smooth-loss calculus are written mathematics, **not** claimed as Lean-proved
in this attempt. No OAI corpus import is used. No Comparator or nanoda
acceptance is claimed.

The required negative control instantiates the sharp second-moment bound
at one binary row, q = 1/2, d = p = 1, and asserts a spurious factor 1/2.
Its left side is 1/4 and its claimed right side 1/8. It must fail on that
false real inequality. This finite check tests a constant in the positive
proof; it is not evidence for the broad asymptotic conjecture.

Every incremental elaboration retains its source snapshot, transcript,
command, and hash under `evidence/lean-attempts/`. Import-name mistakes and
failed elaborations are retained there. The exact final `python3 verify.py`
is run once after final artifact edits; its separate receipt is authoritative
for artifact checks only. The actor does not supply a reviewer verdict.

## 6. Remaining original-goal obstruction

No genuine nested counterexample satisfying both almost-sure uniqueness
conditions has been constructed. The full implication is not proved.
The written sufficiency proof requires vanishing leverage and centered
bounded score. Original consistency does not supply these in the full
convex-loss class. Gram divergence itself need not imply vanishing leverage:
already scalar rows x_i = 2^i have Gram divergence and nonvanishing maximum
leverage. The existing atomic LAD example also prevents treating Gram
divergence as universally necessary.

For general convex losses without a positive global lower curvature bound,
sample curvature can vanish. For LAD, random local increments require a
different uniform argument; for arbitrary high leverage even the good-core
matrix concentration in Theorem S need not vanish. Unbounded scores and
arbitrary error laws add an integrability/concentration obstruction. The
complete Zhao--Rao--Chen theorem could potentially resolve a regular
Gram-only sufficiency regime, but its theorem/proof pages were not obtained
and are not silently assumed. Neither Proposition U nor the new smooth
partial case resolves those remaining quantifiers. An independent reviewer
must therefore report `done:false` for the frozen original goal.
