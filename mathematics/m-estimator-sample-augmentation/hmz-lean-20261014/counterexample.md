# A fixed nested-design counterexample with infinite-variance errors

2026-10-14 PT. **Broad formalization (c) refuted: written proof,
parent-audited, independent Opus referee correct (minor fixes applied).**
This is not a full Lean-certified proof and was not HMZ-accepted. The
fixed law has E|epsilon|=infinity; Cui's unspecified regular-error question
and the finite-moment general-convex regime remain open beyond the proved
subclasses. The unchanged reviewed snapshot is
`evidence/counterexample-reviewed.md`; this integrated copy adds only the
five presentation clarifications recorded in `independent-referee-resolution.json`.

## 1. Fixed loss, fixed error law, and one infinite design

Set eta = 1/(4 pi) and use the **one fixed** loss

    rho(r) = r^2/2 + (eta/pi)(1-cos(pi r)).

Its score is `psi(r) = r + eta sin(pi r)` and
`rho''(r) = 1 + (1/4) cos(pi r)`, so globally
`m = 3/4 <= rho'' <= M = 5/4`. It is finite, C2, strictly convex,
and coercive. This does not contradict the existing Theorem 9: the law
below has infinite variance and even infinite absolute first moment.

For j = 1,2,... define the following **integer** scales:

    N_j = 2^(4 * 10^j),         H_j = 2 N_j,
    T_j = N_j H_j = 2 N_j^2,   A_j = N_j^10,
    B_j = N_j^(1/4),           C_j = N_j^(3/4),
    P_j = N_j H_j^2 = 4 N_j^3.

The quarter powers are integers because the exponent of N_j is divisible
by four. Also N_j = N_{j-1}^10. Fix the symmetric atomic probability law

    F{T_j} = F{-T_j} = 1/(2 N_j),
    F{0} = 1 - sum_{j>=1} 1/N_j.

All errors are iid with this same law. All support points are even integers.
Its absolute first and second moments are infinite, since
`sum T_j/N_j = sum 2N_j` and `sum T_j^2/N_j = sum 4N_j^3`
diverge. The probability at 0 is strictly larger than every other atom.
Thus different translates have their unique largest atom at different
locations. In particular the location family is identifiable.

Take beta_0 = (0,0). Start the design with e_1,e_2. Then append these
blocks in the stated order for every j:

1. One buffer row `(0,B_j)`.
2. N_j rows `(A_j H_j,0)`.
3. C_j consecutive five-row cycles, each consisting of four rows
   `(A_j,1)` followed by one row `(2A_j,-2)`.

This specifies **one infinite deterministic nested design**, with an
already spanning prefix of size two. No old row is changed at a later
stage. All counts are finite integers; their very large values are irrelevant
to the mathematical definition. The error stream is one iid stream on
these rows. The replicate is an independent iid stream with exactly F,
on exactly the first n rows for each n.

For every n >= 2 both sample criteria are finite and coercive with Hessians
at least m S_n and 2m S_n, respectively, so both have unique minimizers.
Their dependence on the finite response vector is continuous, hence
measurable. The initial e_1,e_2 rows and the identifiable location law make
the regression family identifiable. All frozen hypotheses are satisfied.

## 2. Exact reduction to deterministic curvature and random linear scores

For every support point e in 2Z and every real t, periodicity gives

    rho(e-t)-rho(e) = rho(t) - e t.                         (2.1)

Consequently, after subtracting its value at zero, the original criterion is

    D_n(beta) - L_n' beta,
    D_n(beta) = sum_{i<=n} rho(x_i'beta),
    L_n = sum_{i<=n} x_i epsilon_i.                         (2.2)

D_n is deterministic. The pooled criterion, divided by two and centered
at zero, is **the same D_n** with linear score `(L_n+L_n')/2`.
There is no population expected-loss argument or undefined expectation
in this reduction: these are finite-sample exact identities.

Writing x_i = (a_i,b_i), the gradient equation is

    S_n beta + eta sum_{i<=n} x_i sin(pi x_i'beta) = L_n.    (2.3)

Every complete five-row cycle has zero quadratic cross term, strong
quadratic coefficient 8 A_j^2, and weak quadratic coefficient 8.
An incomplete cycle has cross coefficient at most 4 A_j in absolute
value. All previous stages end in complete cycles.

## 3. Elementary tail and prefix estimates

All stage estimates in sections 3--5 are asserted for **j >= 2**.
The finitely many prefixes through the end of stage 1 are irrelevant to
convergence in probability. No stage 0, T_0, or stage-0 strong-block bound
is assumed; the initial e_1,e_2 rows remain exactly as specified.

Let `V_{j-1} = E[epsilon^2 1{|epsilon|<=T_{j-1}}]`.
Symmetry gives zero mean to every such truncated error, and

    V_{j-1} = sum_{l<j} T_l^2/N_l = O(N_{j-1}^3)
            = O(N_j^(3/10)).                              (3.1)

The total number of preceding rows is O(N_{j-1}). The sums of their
absolute strong and weak coefficients are respectively

    sum_old |a_i| = O(N_{j-1}^12) = O(N_j^(6/5)),
    sum_old |b_i| = O(C_{j-1}) = O(N_j^(3/40)).             (3.2)

Their strong Gram coefficient is O(N_{j-1}^23); their weak Gram
coefficient is O(C_{j-1}). These bounds follow term by term from the
specified rows; earlier super-exponentially smaller stages are absorbed
by the last one. Constants below are independent of the prefix in a stage.

The probabilities of the following unwanted events tend to zero:

- A preceding row or the new buffer has |epsilon| > T_{j-1}:
  `O((N_{j-1}+1)/N_j) = o(1)`.
- A row in the full new high block has |epsilon| > T_j:
  `O(N_j/N_{j+1}) = o(1)`.
- A row in the full new low block has |epsilon| >= T_j:
  `O(C_j/N_j) = o(1)`.

Let `Tgood_j` denote the intersection of the complements of these three
full-block bad events. It has probability 1-o(1), independently of which
deterministic prefix within the stage is under consideration. Define
`Tgood'_j` in the same way for the replicate stream.

These are union bounds using the fixed tail masses. They remain valid
for either stream or for both streams together. On the first good event,
old weak linear score and buffer score divided by B_j^2 are bounded by

    O(T_{j-1} C_{j-1}/B_j^2) = O(N_j^(-9/40)),
    T_{j-1}/B_j = O(N_j^(-1/20)),                          (3.3)

respectively, and both tend to zero.

For a prefix of the low block, let k be the number of completed cycles
and ell in {0,...,4} the number of following positive rows. The new weak
Gram weight is `w = 8k+ell`. The centered truncated weak linear score
has variance `V_{j-1} w`. Since the total weak Gram coefficient Q obeys
`Q >= B_j^2+w`, Chebyshev gives, for every fixed z > 0,

    P(|low weak score|/Q > z)
       <= V_{j-1} w/[z^2(B_j^2+w)^2]
       <= V_{j-1}/(4 z^2 B_j^2) = o(1).                  (3.4)

The last inequality is `(b-w)^2>=0`, with b = B_j^2.
This bound is uniform in every deterministic prefix k,ell. Removing the
truncation costs only the third tail event above. We need weak consistency
at every prefix, **not** an almost-sure supremum over all prefixes.
Thus (3.4) is exactly the needed uniform error-probability estimate.

## 4. Original consistency, including all transitions and partial cycles

For every stage j >= 2, its prefixes are covered by the following explicit
partition: the buffer row; a high-block prefix `1 <= h <= N_j`; a
nonempty low-block prefix `(k,ell)` with `0 <= k < C_j`, `0 <= ell <= 4`,
and `5k+ell >= 1`; or the completed low block `(C_j,0)`.
The high-block endpoint also has the low-prefix notation `(0,0)`, where
both proofs apply; excluding `(0,0)` from the nonempty low case makes the
partition disjoint. We prove convergence uniformly in these deterministic
choices as j tends to infinity, not an almost-sure supremum over prefixes.

**Buffer prefix.** The quadratic Gram matrix is diagonal. Its strong entry
and strong linear score are unchanged from the preceding completed stage.
On the first good event, all old errors are at most T_{j-1}; equation (2.3)
and bounded sine imply

    |beta_1| <= (T_{j-1}+eta) sum_old|a_i| / S_old,11
               = O(N_{j-1}/A_{j-1}) -> 0.

Here `S_old,11 >= N_{j-1}(A_{j-1}H_{j-1})^2`, and (3.2) supplies the
matching upper bound on the sum of absolute coefficients. For fixed beta_1,
the derivative in beta_2 is increasing with slope at least m S_n,22.
Its value at beta_2=0 consists of the weak linear scores plus an old sine
term of absolute value at most eta sum_old|b_i|. The new buffer sine is
zero there. Divide by `S_n,22 >= B_j^2` and use (3.3). The unique root
beta_2 therefore tends to zero. The preceding completed-stage prefix is
the low prefix `(C_{j-1},0)` of stage j-1. Its next prefix is the present
buffer prefix; these are distinct cases in the partition above.

**High-block prefixes.** The Gram matrix remains diagonal. After h >= 1
new high rows its strong entry is at least `h(A_jH_j)^2`.
On the second good event the new errors have magnitude at most T_j.
Equation (2.3) gives, uniformly for 1 <= h <= N_j,

    |beta_1| <= T_j/(A_j H_j) + eta/(A_j H_j)
       + O((T_{j-1}+eta) N_{j-1}^12/(A_j^2H_j^2)) -> 0.

The leading ratio is `N_j/A_j = N_j^-9`. There are no new weak rows,
so the same weak derivative bound as at the buffer prefix applies,
regardless of the value of beta_1 (bounded sine is sufficient).
Thus beta_2 also tends to zero throughout this phase.

**Low-block prefixes.** Set `u = A_j beta_1`, `v = beta_2`.
Let K_j be the number of +T_j errors minus the number of -T_j errors
in the completed high block. It is integer-valued and uniformly tight:
its absolute value is at most the number of level-j observations, whose
expectation is one. Define the prefix-independent lower-level noise

    R_j = (1/T_j) sum_high epsilon_i 1{|epsilon_i|<=T_{j-1}}.

It has mean zero and variance `V_{j-1}/P_j=O(N_j^(-27/10))`.
On `Tgood_j`, the high linear score in u divided by P_j is exactly
`K_j+R_j`. The full exact u- and v-equations are

    G_uu u + ell v + eta s_u(u,v) = L_u,
    ell u + Q v + eta s_v(u,v) = L_v,
    G_uu = P_j + 8k+ell + S_old,11/A_j^2 >= P_j,
    Q = S_old,22 + B_j^2 + 8k+ell,
    L_u = sum_old (a_i/A_j) epsilon_i
          + H_j sum_high epsilon_i
          + sum_low-prefix c_i epsilon_i,
    L_v = sum_old b_i epsilon_i + B_j epsilon_buffer
          + sum_low-prefix b_i epsilon_i,

where c_i is 1 for the four positive rows in a cycle and 2 for its
last row. Here s_u and s_v are the corresponding deterministic sine
sums in these transformed coordinates:

    s_u(u,v) = sum_old (a_i/A_j) sin(pi(a_i u/A_j+b_i v))
       + N_j H_j sin(pi H_j u)
       + (4k+ell) sin(pi(u+v)) + 2k sin(2pi(u-v)),
    s_v(u,v) = sum_old b_i sin(pi(a_i u/A_j+b_i v))
       + B_j sin(pi B_j v)
       + (4k+ell) sin(pi(u+v)) - 2k sin(2pi(u-v)).

Define prefix-independent deterministic bounds

    c_j = (T_{j-1}/P_j)(sum_old |a_i|/A_j + 6C_j+4) -> 0,
    q_j = (sum_old |a_i|/A_j + N_j H_j + 6C_j+4)/P_j -> 0.

On `Tgood_j`,

    L_u/P_j = K_j+R_j+d_{j,k,ell},  |d_{j,k,ell}| <= c_j,
    |s_u(u,v)|/P_j <= q_j   for every real u,v.

Also `S_old,11/A_j^2=O(N_j^(-177/10))=o(1)`, and
`sup_{k,ell}(G_uu/P_j-1)->0`. None of these bounds presupposes tight v.
Set the prefix-independent tight random variable

    X_j = |K_j|+|R_j|+c_j+eta q_j,

and, for each deterministic low prefix, set

    Y_{j,k,ell} =
      (|L_v|+eta(sum_old |b_i|+6k+ell))/(m Q).

The Y variables are uniformly tight in the probability-bound sense, by
(3.3)--(3.4) and `Q>=B_j^2+8k+ell`. Their low-score terms depend on
the prefix; no almost-sure bound on their maximum is asserted. The
tail events, K_j, R_j, X_j, c_j and q_j do not depend on the prefix.
The exact u-equation and the weak derivative at v=0, whose slope is at
least mQ, give on `Tgood_j`

    |u| <= X_j + 4|v|/P_j,
    |v| <= Y_{j,k,ell} + 4|u|/(m B_j^2).

The contraction factor is explicitly
`delta_j=16/(m P_j B_j^2)->0`. For j large enough that delta_j<1,

    |u| <= (X_j+4Y_{j,k,ell}/P_j)/(1-delta_j).

Thus u and v are uniformly tight. Returning to the exact u-equation,

    u-K_j = R_j+d_{j,k,ell}-eta s_u(u,v)/P_j
            -ell v/P_j-(G_uu/P_j-1)u,

proves

    u - K_j -> 0 in probability, uniformly in low prefixes. (4.1)

Now evaluate the weak derivative at v=0. The complete new cycles contribute

    eta k [4 sin(pi u)-2 sin(2 pi u)].

Both sines vanish for every integer K_j, and their differences from those
values are bounded by pi|u-K_j| and 2pi|u-K_j|. Dividing by Q >= 8k
bounds this contribution by eta pi |u-K_j| (with zero contribution if k=0).
The incomplete-cycle quadratic cross term is at most 4|u|, and its sine
term at most 4eta; both vanish after division by Q >= B_j^2.
Old sine terms vanish by (3.2), and all weak linear scores vanish by
(3.3)--(3.4). The buffer sine at v=0 is zero. Thus the entire weak derivative
at zero, divided by Q, tends to zero in probability, uniformly in prefixes.
Its derivative in v is at least m Q globally. Its root satisfies

    |v| <= |weak derivative at v=0|/(m Q) -> 0.

Together with tight u and A_j -> infinity this gives beta_1=u/A_j -> 0.
All three prefix types have uniform failure-probability bounds tending to
zero. Any deterministic n tending to infinity has its stage j tending to
infinity, so this proves **original weak consistency along all n**, not only
the completed blocks or a triangular subsequence.

## 5. The pooled estimator is inconsistent

Take n at the completed low block `(C_j,0)` of stage j. Dividing the
pooled criterion by two leaves D_n unchanged and averages its linear
scores. The cross Gram entry is exactly zero, and the sine bound q_j
holds for every u,v. Hence the exact u-equation gives directly

    u_tilde - (K_j+K'_j)/2 -> 0 in probability.             (5.1)

No tightness assumption or conclusion for v_tilde is needed for this step.

Let E_j be the event that the original high block has exactly one +T_j
and no other level-j observation, while the replicate has no level-j
observation at all. Independence gives its probability exactly

    [1/2 (1-1/N_j)^(N_j-1)] (1-1/N_j)^N_j
        -> (1/2) exp(-2) > 0.                            (5.2)

On E_j, K_j=1 and K'_j=0. At this completed prefix Q/C_j->8,
so Q<=9C_j for all sufficiently large j. Write L_tilde_v for the
averaged weak linear score of all observations, including old rows and
the buffer. Its ratio to C_j tends to zero in probability: (3.3) handles
old/buffer scores, while the new low-score variance is
`O(C_j V_{j-1})`, so `V_{j-1}/C_j->0`. Removing the truncation costs
only the full-block tail events. Also `sum_old |b_i|/C_j->0`.

For all sufficiently large j define the explicit good set

    G_j = E_j intersect Tgood_j intersect Tgood'_j
          intersect {|u_tilde-1/2|<=1/10}
          intersect {(|L_tilde_v|+eta sum_old |b_i|)/C_j<=eta}.

Every additional failure costs o(1) unconditionally, except the
half-integer condition, whose failure *within E_j* is bounded by
`P(|u_tilde-(K_j+K'_j)/2|>1/10)=o(1)` from (5.1). Therefore
`P(G_j)>=P(E_j)-o(1)` and `liminf P(G_j)>=exp(-2)/2`.

Let g_j(v) be the weak derivative of the averaged-score criterion with
the strong coordinate fixed at u_tilde. Its value at zero is exactly

    g_j(0) = eta C_j [4sin(pi u_tilde)-2sin(2pi u_tilde)]
             +eta sum_old b_i sin(pi a_i u_tilde/A_j)-L_tilde_v.

The buffer sine is zero at v=0. On G_j this gives the explicit bound

    g_j(0)/C_j
      >= eta[4cos(pi/10)-2sin(pi/5)-1] > eta.

The last strict inequality follows, for example, from
`cos(pi/10)>sqrt(3)/2`, `sin(pi/5)<sqrt(2)/2`, and
`2sqrt(3)-sqrt(2)>2`; no numerical simulation is used.
Everywhere `mQ<=g_j'(v)<=MQ<=9MC_j`, and its unique root is v_tilde.
Since g_j(0)>0, integrating the upper derivative bound to that negative
root gives, on G_j,

    v_tilde <= -eta/(9 M).

For delta = eta/(20 M) > 0 it follows that

    liminf_j P(||beta_tilde_2n|| > delta)
       >= (1/2) exp(-2) > 0.                             (5.3)

This disproves pooled weak consistency. It uses two independent streams of
the **same fixed** F on the **same first n rows**, one nested original
design, and one fixed globally strongly convex loss. Both minimizers are
unique. There is no tie selector, n-dependent loss, triangular original
design, strong-consistency coupling claim, or population assumption.

## 6. Formalized connection and review boundary

`Formal.lean` proves the derivative of the fixed ripple loss and its score,
the global curvature constants 3/4 and 5/4, and the derivative of the general
real profile `4 rho(u+v)+rho(2(u-v))`. It proves zero profile score at every
integer u and profile score 4eta at u=1/2. It also proves the general
independent weighted second-moment identity and the prefix ratio
`k/(b+k)^2 <= 1/(4b)` used in (3.4). These are substantive calculus and
stochastic components tied to this actual asymptotic construction. The
whole infinite design/law and every-prefix convergence are written proofs,
not represented as a compiled full asymptotic Lean theorem.

The parent-owned independent no-tools Claude Opus 5.5/max referee returned
**correct**, checking 44 claims and establishing every-prefix original
consistency, pooled inconsistency and the target hypotheses. It reviewed
the written snapshot with hash
`f8e22b6f4c4fe7eb1d19291e2998abdce9ce2e99ed507f9fa239c25ae7c8acfd`,
not this clarified presentation. The five minor findings are resolved
here without changing the loss, law, design or mathematical conclusion.
**The referee did not inspect or use Lean artifacts**: it re-derived the
calculus, moment identity and prefix inequality by hand. Its verdict is
written-proof review, not kernel certification.

The earlier Huber/smooth bounded-score partial work is retained separately.
The exact checker and Lean sources remain unchanged. The actual HMZ run
ended `stopped` without a reviewer verdict; the separate referee's
correct verdict does not create `done:true`, `ended how:done`, or RLAR
acceptance. The fixed law has infinite absolute first moment and variance,
so neither Cui's unspecified regular-error question nor the finite-moment
general-convex regime is claimed resolved beyond Theorems 9/10.
