# The optimizer stability cutoff: all finite Lp norms, but not Linfinity

**AUTHOR CANDIDATE — WRITTEN with a rational jump check; NOT independently reviewed or parent-adopted.** Native pre-write clock: `Wed Oct 28 18:05:36 PDT 2026`.

## 1. Exact statement for original feasible laws

Fix ANY finite epsilon>0, b=e^(-epsilon), D the FULL CLOSED unit l1 diamond, and F_epsilon all Borel laws satisfying the epsilon event inequality for EVERY Borel set and EVERY shift in D. Let V and mu_* be the original all-law squared-Euclidean optimum and its unique law.

**Conditional on the new all-law TV-stability candidate and named LAW642:** for EVERY feasible sequence with `J(mu_n)->V`, the densities p_n converge to p_* in L^p(R^2) for EVERY finite `1<=p<infinity`, and the laws converge in W2. The p=1 case is precisely 2TV; the same single sequence satisfies all finite-p statements. No density symmetry, smoothness, parameterized family or common exceptional set is assumed.

**Sharp endpoint failure, independently from TV stability:** for EVERY finite epsilon>0, there exists a sequence of full-D-private C-infinity strictly positive densities q_n whose privacy parameter is EXACTLY epsilon and whose costs tend to V, but

    liminf ||q_n-p_*||_(L^infinity,ess) >= (1-b)/(2Z) > 0,              (1)

where Z is the actual canonical optimizer normalizer. In fact EVERY continuous q has this same bound, even if q is not a probability density or is not private. It already holds on EVERY neighborhood of ANY core-boundary point. The two density plateaux are meant a.e.; arbitrary pointwise-version edits do not evade the essential-sup norm.

Thus strong convergence holds in all finite Lp norms at fixed epsilon, while L-infinity/locally uniform density stability fails. This does not contradict uniqueness, TV convergence, or individual continuous-law nonattainment. No finite-p or Wasserstein rate, uniform-in-epsilon statement, source equivalence or novelty is claimed.

## 2. Named inputs

The original LAW642 parent theorem `institute/runs/three-area-2026-10-23-96h/privacy-all-law-self-contained-parent-v1.md`, SHA `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`, gives the actual unique optimum and canonical density

    p_*=Z^(-1)b^(n_S),      n_S(x)=min{k>=0:x in S+kD},

where S is a compact convex body containing 0 in its interior. This remains a named same-harness WRITTEN_SUPPORTED theorem, not a formal/human proof.

The all-law near-optimum TV and W2 convergence is the still-UNREVIEWED own candidate `frontier-20261028-all-law-tv-stability-v1.md`, SHA `3f6c2a61738cc92f615e375d88f6dfb10f96b553585b5c8468480a7ec9683f79`. Its plateau-neighbor and weak-closure arguments are not re-certified by this successor. The lower essential-sup discontinuity and the smooth exact-privacy construction below are reconstructed directly from LAW642 and elementary analysis, without requiring that unreviewed stability claim.

## 3. Uniform density bound upgrades TV to every finite Lp

For any original feasible mu and every finite-area Borel A, integrate the privacy inequality over h in D:

    2 mu(A) <= b^(-1) integral_D mu(A+h)dh <= b^(-1)|A|.

Tonelli proves the last bound. Thus every feasible law has a density p with `0<=p<=C:=1/(2b)` a.e. The same bound applies to p_* and every p_n, with null-set versions irrelevant.

For 1<=p<infinity,

    ||p_n-p_*||_p^p
       <= C^(p-1) ||p_n-p_*||_1
       = 2 C^(p-1) TV(mu_n,mu_*).                                       (2)

The first inequality uses `|p_n-p_*|<=C` a.e. Therefore the named all-law TV stability makes every finite Lp norm tend to 0. It also gives W2 convergence as a separate part of that named candidate; neither TV alone nor (2) is used to infer W2.

## 4. A fixed essential-sup jump on every core-boundary neighborhood

Take ANY z0 in the boundary of S. Since S is a convex body, every neighborhood of z0 meets int(S) in a nonempty open set. A supporting hyperplane at z0 gives points arbitrarily close to z0 outside S. For a small displacement h with `||h||_1<1`, z0+h lies in the OPEN set `S+int D`, hence in int(S+D); choosing the displacement outward gives a nonempty open set outside S. Thus every neighborhood of z0 contains nonempty open sets on which p_* is respectively

    a=1/Z,          b a=b/Z.

If a continuous q has essential-sup error at most E on the neighborhood, continuity and the fact that the two plateaux are open force

    |q(z0)-a|<=E,        |q(z0)-ba|<=E.

Consequently `E>=a(1-b)/2=(1-b)/(2Z)`. This proves (1) for EVERY continuous q and EVERY neighborhood of z0, without needing equality of any pointwise density versions at the boundary itself. It also reproves the no-continuous-version statement from the canonical jump, without using the earlier one-review S20 lemma.

## 5. Actual smooth exact-epsilon near-optimizers

Let U have a centrally symmetric C-infinity density supported in [-1,1]^2, strictly positive in its interior, and set `kappa=E|U|_2^2>0`. If X_* has law mu_* independently, put q_t as the density of `X_*+tU`. Convolution preserves the event inequality for EVERY h in D, is C-infinity and positive everywhere. Independence and E U=0 give the exact cost

    J(q_t)=V+kappa t^2.                                                   (3)

The privacy parameter is also exactly epsilon, not merely <=epsilon. Since S is compact choose B larger than its coordinate maxima, and let `c=max_(x in S)(x1+x2)`. Whenever x1,x2>B, `n_S(x)=ceil(x1+x2-c)`. For all x1,x2>B+t and every u in the kernel support, translation by h=(1,0) raises this index exactly by 1; hence `q_t(x+h)=b q_t(x)`. Any nonempty bounded open rectangle E in that far quadrant has positive q_t mass and `q_t(E)=b^(-1)q_t(E+h)`. Thus no smaller privacy parameter is possible.

Taking t_n->0 gives actual smooth exact-epsilon near-optimal densities. Each q_t is continuous, so §4 supplies the SAME strictly positive essential-sup lower bound, both globally and on every neighborhood of any chosen core-boundary point. This establishes the p=infinity failure independently of the new TV theorem. If that theorem is accepted at its named scope, these SAME laws still converge in all finite Lp norms and W2, giving the stated sharp topology cutoff.

## 6. Actual exact check and assurance limits

A bounded local Fraction check for a SYNTHETIC staircase with b=1/2 and Z=12 produced

```text
synthetic staircase b=1/2,Z=12: half_jump= 1/48 upper_plateau= 1/12 lower_plateau= 1/24
two plateau-to-boundary distances cannot both be below half_jump: True
```

The values merely check arithmetic in the half-jump argument; S=D in that synthetic example is not claimed to be the actual optimal core. The all-law TV stability input is unreviewed, and no finite-Lp conclusion is promoted past its scope. The continuous essential-sup lower bound and actual smooth exact-epsilon construction are written consequences of the named LAW642 geometry and ordinary analysis. Request disjoint review of the shared TV dependency, boundary neighborhoods, all-shift exact privacy and moment normalization before adoption. No external model, formal/human/configured-family or novelty gate is claimed; historical held results are not accepted premises.
