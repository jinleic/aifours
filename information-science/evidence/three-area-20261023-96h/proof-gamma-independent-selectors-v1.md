# Two data-only quantile crossings determine the entire gamma sensitivity curve

**Status: CANDIDATE / NOVELTY_UNCLEAR.** A further written consequence within the frozen bounded-real target. This is not a new target, a new executed search, or a claim of a novel optimization principle. Read the main sharp-bound manuscript with its operative ADDENDUM-1. No scientific computation was used.

## 1. Statement

Use all notation and hypotheses of `proof-bounded-outcome-sharp-bounds-v1.md`: I=[l,u], h=q-p, t=r-h, eta=gamma-g_min in [0,1], the two upper tail integrals u_s and lower tail integrals ell_s. Define

    W(r)=u_0(r)+u_1(r-h),
    Wbar(r)=r+(r-h)-ell_0(r)-ell_1(r-h).

Choose any two data-dependent maximizers

    r_minus in argmax_(r in I) [W(r)-r],
    r_plus  in argmax_(r in I) [Wbar(r)-r].                  (1)

They exist by compactness and do not depend on gamma. For a closed nonempty interval J, let clamp_J(x)=min(max(x,min J),max J). Let med(x,y,z) denote the middle of the three numbers, with repetitions allowed.

For every compatible eta, set

    r_L(eta)=clamp_I( med(h+eta, 1-eta, r_minus) ),
    r_U(eta)=clamp_I( med(h+1-eta, eta, r_plus) ).             (2)

Then the exact sharp endpoints from the main theorem are

    L(gamma)=F_eta(r_L(eta)),
    U(gamma)=G_eta(r_U(eta)).                                (3)

Thus no new switch-mass optimization is needed when gamma changes: two data-only one-dimensional concave optimizations, or their corresponding quantile crossings, determine the whole sensitivity curve by the explicit clamps (2). The statement retains arbitrary atoms, nonunique optimizers, zero-mass strata and singleton I.

## 2. Elementary convex lemma

Let W be continuous and concave on a compact interval I, with

    0<=W(y)-W(x)<=2(y-x) for x<=y in I.                     (4)

Choose r_0 minimizing r-W(r) on I. For any real a,b, the function

    f(r)=(r-a)_+ +(r-b)_+ -W(r)

is minimized by

    r_*=clamp_I(med(a,b,r_0)).                              (5)

**Proof.** Relabel a,b so a<=b. Below a, f=-W is nonincreasing by (4). Above b,

    f=2r-a-b-W(r)

is nondecreasing by the upper bound in (4). If I lies entirely below a, its right endpoint is a minimizer; if I lies entirely above b, its left endpoint is a minimizer. Formula (5) gives exactly those endpoints.

In every remaining case J=I intersect [a,b] is a nonempty interval. Any r below J can be moved to its lower endpoint without increasing f, and any r above J can be moved to its upper endpoint without increasing f, using the two monotonicity observations. On J,

    f(r)=r-a-W(r).

The function r-W(r) is convex. Clamping any of its global I-minimizers r_0 to the subinterval J gives a J-minimizer: if r_0 lies to one side of J, convexity makes the function monotone away from its minimizer set on that side; if it lies inside J, the assertion is immediate. Because I and [a,b] intersect, clamp_J(r_0)=clamp_I(med(a,b,r_0)). This proves (5), including flat intervals and coincident endpoints. QED.

## 3. Applying the lemma to the lower bound

Each u_s is nondecreasing, concave and 1-Lipschitz. Therefore W satisfies (4). The lower objective is exactly

    F_eta(r)=(r-(h+eta))_+ +(r-(1-eta))_+-W(r).

Its r_0 from the lemma is any maximizer r_minus in (1). Taking a=h+eta and b=1-eta proves the first formula of (2) and (3). No differentiability assumption is used.

## 4. Applying the lemma to the upper bound

Reflect the factual outcomes by y'=1-y. Its upper-tail integral at selected mass x is

    u_s^ref(x)=x-ell_s(x).

Consequently its combined W is exactly Wbar. It too is nondecreasing, concave and 2-Lipschitz. Complementing the entire potential outcomes replaces eta by 1-eta and delta by -delta; explicitly,

    -F^ref_(1-eta)(r)
      =r+t-(r-eta)_+-(t+eta-1)_+-ell_0(r)-ell_1(t)
      =G_eta(r).

The lower-selector formula for the reflected law therefore gives the second formula of (2), which maximizes the original upper objective. This proves (3).

## 5. Exact quantile interpretation

The data-only objective for r_minus is u_0(r)+u_1(r-h)-r. At an interior differentiability point its derivative is

    Q_0(p_0-r)+Q_1(p-(r-h))-1.

The objective for r_plus is r-h-ell_0(r)-ell_1(r-h), up to an irrelevant additive constant. Its derivative is

    1-Q_0(r)-Q_1(r-h).

Thus the two optimizers are, respectively, upper-tail and lower-tail quantile crossings at sum 1, with interval-end inequalities and subgradient intervals when needed. These are characterizations of (1), not substituted assumptions excluding discrete laws.

The main positive-effect threshold satisfies

    Gamma_*=g_min+1-r_minus+W(r_minus),

for any r_minus in (1), so the same data-only crossing controls both the sharp sign threshold and all fixed-gamma lower bounds.

## 6. Claim boundary

The scientific content is a deterministic symbolic simplification of the already-written arbitrary-law formula, not another finite range or failed search. It changes a per-gamma scalar optimization into two fixed data-only optimizers plus a clamp. Classical convexity, rearrangement and sensitivity analysis may make this a routine corollary; no independent novelty claim is attached. Parent/independent written checking is still required for this additional manuscript. It does not repair the unresolved Kuroki full-text/priority gate and does not add continuous-surrogate, non-strong-surrogate, unbounded-outcome or statistical-estimation coverage.
