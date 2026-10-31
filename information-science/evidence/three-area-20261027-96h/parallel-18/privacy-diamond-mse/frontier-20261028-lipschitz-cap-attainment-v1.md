# Fixed Lipschitz cap restores attainment and a positive gap

**AUTHOR CANDIDATE — WRITTEN, PARTLY CHECKED BY EXACT RATIONAL ARITHMETIC; NOT YET INDEPENDENTLY REVIEWED.** Native pre-write clock: `Wed Oct 28 17:04:52 PDT 2026`.

## 1. All-law model, one research import and exact delta

Fix arbitrary finite epsilon>0. Put `b=exp(-epsilon)`, `D={h:|h1|+|h2|<=1}` and let F_epsilon be ALL Borel laws mu satisfying `mu(A)<=b^(-1)mu(A+h)` for EVERY Borel A and EVERY h in the full CLOSED D. The objective is `J(mu)=integral |x|_2^2 mu(dx)` and the original infimum is V.

The named research import is the adopted LAW642 theorem at its exact scope, `institute/runs/three-area-2026-10-23-96h/privacy-all-law-self-contained-parent-v1.md`, SHA-256 `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`, lines 14–22: V is finite, there is exactly ONE all-law optimizer mu_*, and one version of its density is

    p_*(x)=Z^(-1)b^(n(x)),    n(x)=min{k>=0:x in S+kD},

where S is compact convex with nonempty interior and 0 in S, and Z is the normalizer. I do not reprove LAW642. This remains an ordinary same-harness written import, not a kernel/formal/human acceptance.

For each REAL L>0, define H_L to be the subset of F_epsilon having a globally L-Lipschitz density version in the Euclidean metric, and put `V_L=inf_{mu in H_L} J(mu)`. L is a fixed bound on the density itself, not a bound on log-density, sensitivity, a finite set of shifts or a restriction on the original target. The new precise statements are:

1. H_L is nonempty and V_L is attained for EVERY L>0. Every minimizer has strictly larger cost than V, so `V_L>V` for every fixed finite L. No uniqueness or exact privacy of the H_L minimizer is asserted.
2. The explicit all-L cost bound is

       0 < V_L-V <= 2/(3 Z^2 L^2).                                      (1)

   The upper witness is not just feasible: it has exact privacy epsilon attained by an actual event and boundary shift, and its density is C^1.
3. Define `T_L=inf_{mu in H_L} TV(mu,mu_*)`. For one explicitly specified positive jump height w and every sufficiently large L,

       w^2/(8L) <= T_L <= [P(S)+4 sqrt(2)b/(1-b)]/(sqrt(6) Z^2 L).      (2)

   Thus `T_L=Theta(1/L)` at each fixed epsilon. The LOWER bound holds even without imposing privacy, for every probability law with an L-Lipschitz density. The upper witness has exact epsilon privacy. The constants depend on the imported actual optimizer and are not claimed uniform in epsilon.

The result improves on the already recorded continuous-density nonattainment: unconstrained continuous densities have no positive infimum gap by the separate smoothing construction, whereas every fixed global Lipschitz cap has an actually attained, strictly larger minimum. The upper rate (1) does not prove a matching L^(-2) lower COST bound, and the TV statement does not imply one. No exact H_L selector, original optimizer re-solution, source equivalence, literature novelty or uniform-in-epsilon claim is made.

## 2. Explicit full-shift-private Lipschitz witness

Let U have the independent-coordinate triangular density

    phi(u1,u2)=(1-|u1|)_+(1-|u2|)_+.

It integrates to 1; `E U=0`, `E|U|^2=1/3`, and its support is `[-1,1]^2`. Let X have the actual law mu_* independently of U, and set

    q_t(x)=integral p_*(x-tu)phi(u)du,      mu_t=Law(X+tU).             (3)

For every Borel A and h in D, integrating the original inequality for mu_*(A-tu) gives `mu_t(A)<=b^(-1)mu_t(A+h)`, including every closed boundary shift. Independence, zero mean and finite original cost give

    J(mu_t)=V+t^2/3.                                                     (4)

The normalized scaled triangular kernel `phi_t` has weak first partial derivatives in L1, each integrating to zero and satisfying

    integral |partial_i phi_t| = 2/t,        i=1,2.                     (5)

Because `0<=p_*<=1/Z`, convolution and the zero signed integral sharpen the usual L1 bound:

    |partial_i q_t(x)| <= (1/Z) integral (partial_i phi_t)_+ = 1/(Zt).

Indeed for any signed g of total integral 0 and any 0<=f<=M, `|integral f g|<=M integral g_+`. The convolution derivative is continuous because translated L1 kernels are continuous in L1, so q_t is C^1 and globally

    Lip_2(q_t) <= sqrt(2)/(Zt).                                          (6)

Choose `t=sqrt(2)/(ZL)`. This actual mu_t lies in H_L and (4) yields the explicit upper bound in (1). No optimal-core-dependent root needs evaluation.

For exact privacy, choose B strictly above both coordinate suprema of S and set `c=max_{s in S}(s1+s2)`. For every x1,x2>B,

    n(x)=ceil(x1+x2-c).                                                   (7)

Indeed each coordinate of every s lies below x and its l1 distance to x is `x1+x2-(s1+s2)`; the minimum is attained and closed dilation converts distance to the ceiling. For every x1,x2>B+t and every u in the square support, (7) gives `p_*(x+(1,0)-tu)=b p_*(x-tu)`, even on shell boundaries. Hence `q_t(x+(1,0))=b q_t(x)`. Any nonempty bounded open rectangle E in that far quadrant has positive mu_t mass and satisfies `mu_t(E)=b^(-1)mu_t(E+(1,0))`. Since (3) is epsilon-private, its exact smallest privacy parameter is epsilon.

## 3. Weak closure, compact attainment and strictness

Fix L>0. First every NONNEGATIVE L-Lipschitz probability density q has a global uniform bound depending only on L. At any x, if q(x)=M>0 then q>=M/2 on the Euclidean disk of radius `M/(2L)` about x. Thus

    1 >= pi M^3/(8 L^2),    so M <= (8L^2/pi)^(1/3).                  (8)

This argument uses all of R^2 and holds at every x, even when the supremum is not attained.

Suppose a sequence of laws in H_L converges weakly to a probability law mu. Choose their globally L-Lipschitz, nonnegative density versions. Equation (8) and equicontinuity give, by Arzela–Ascoli on compact sets and a diagonal subsequence, locally uniform convergence to one nonnegative globally L-Lipschitz q. Against each compactly supported continuous test function, local uniform convergence and the SAME weak law limit show `mu(dx)=q(x)dx` as Radon measures. Since mu is a probability law, q integrates to 1. Thus this density constraint is weakly closed; no hidden pointwise-density version for every shift is required.

For each fixed h in D and nonnegative compactly supported continuous f, the event privacy inequality is equivalent to

    integral f(x) mu_j(dx) <= b^(-1) integral f(x-h) mu_j(dx).

Both sides pass to the SAME weak limit. Radon measure order then gives the full Borel event inequality for that h. Since h was arbitrary, the resulting single limit law is in F_epsilon for EVERY h; one need not take h-dependent subsequences or intersect uncountably many density null sets. Therefore H_L is weakly closed.

The witness (3), (6) makes V_L finite. A minimizing sequence has uniformly bounded second moment, hence is tight; Prokhorov gives a weakly convergent subsequence, its limit remains in H_L, and lower semicontinuity of the nonnegative squared-Euclidean cost gives an actual minimizer. These are standard analysis imports, not a scientific solver run.

To prove strictness, choose integer k with `c+k>2B+8`. From (7), immediately below the far diagonal `x1+x2=c+k`, p_* equals `a=Z^(-1)b^k`, and immediately above it equals `ab`. The two values differ, and the two open sets share an accumulation boundary point. Any continuous function equal to p_* a.e. would be both values at that boundary point. Thus mu_* has no continuous density version. By the imported all-law uniqueness, no law in H_L can have J=V. In particular the attained H_L minimizer has J>V, proving `V_L>V`. The argument does NOT claim a positive gap over the union of ALL L or over all continuous densities.

## 4. Explicit lower total-variation separation at fixed L

Use the same k and let the positive height of that ACTUAL far-tail jump be

    w=a(1-b)=Z^(-1)b^k(1-b)>0.                                         (9)

Introduce orthonormal coordinates

    r=(x1+x2-c-k)/sqrt(2),    s=(x1-x2)/sqrt(2).

For `|s|<1/2` and `|r|<d0=1/(4sqrt(2))`, both coordinates stay above B and no other shell boundary is crossed. The Jacobian is 1; p_* is a on r<0 and ab on r>0.

Let q be ANY L-Lipschitz density (privacy is NOT assumed). For every s in the unit-length tangent interval and 0<r<d0, the triangle inequality and the fact that the Euclidean distance from (s,-r) to (s,r) is 2r give

    |q(s,-r)-a| + |q(s,r)-ab| >= w-2Lr.                                (10)

Take `d=w/(2L)` when `L>=w/(2d0)=2sqrt(2)w`. Integrating (10) from 0 to d and along the tangent interval gives

    integral_strip |q-p_*| dx >= integral_0^d (w-2Lr)dr = w^2/(4L).

Therefore every such q, regardless of privacy, obeys

    TV(q dx,mu_*) >= w^2/(8L).                                           (11)

This is a bound for versions of probability density laws and is unaffected by null-set changes. No universal bound for every L is being extrapolated from (11): only the stated large-L range is used.

## 5. Matching-order constructive TV upper bound

The nested convex `K_j=S+jD` give

    p_*=(1-b)/Z sum_{j>=0} b^j 1_{K_j}.                                  (12)

The standard BV translation estimate `||1_K(.-y)-1_K||_1<=|y|P(K)` and planar convex Minkowski perimeter identity `P(S+jD)=P(S)+4sqrt(2)j` imply, by Tonelli,

    TV(mu_t,mu_*) <= t sqrt(1/3)/(2Z) [P(S)+4sqrt(2)b/(1-b)].           (13)

Here `E|U|<=sqrt(E|U|^2)=1/sqrt(3)`. Substituting `t=sqrt(2)/(ZL)` yields the upper bound in (2); the same witness is exact-epsilon private by section 2. This and (11) prove `T_L=Theta(1/L)` at fixed epsilon. The standard BV and convex-perimeter identities are explicit nonresearch imports and have not been formalized by this calculation.

Combining (1)–(2) is NOT an inference that J(mu)-V universally controls TV(mu,mu_*) from either side. In particular it does not prove `V_L-V>=c/L^2`; that remains an actual open quantitative question at this candidate's scope.

## 6. Actual exact rational sanity computation

A separate bounded in-kernel checker used Python `fractions.Fraction`, no floats and no scientific solver. It takes a SYNTHETIC admissible staircase core S=D, b=1/2, Z=12, k=5, and L=1; this is not claimed to be LAW642's actual optimal core. The checker verifies the paired-strip algebra and the upper-bound arithmetic only:

```python
from fractions import Fraction as F
b, Z, k, L = F(1,2), F(12), 5, F(1)
w=(1-b)*b**k/Z
d=w/(2*L)
pair_integral=w*d-L*d*d
bound_tv=pair_integral/2
print('jump_height=',w,'optimal_halfwidth=',d)
print('paired_cross_section_integral=',pair_integral,'= w^2/(4L):',pair_integral == w*w/(4*L))
print('TV_lower_for_unit_tangent_length=',bound_tv,'= w^2/(8L):',bound_tv == w*w/(8*L))
print('1d_triangular_kernel_total_variation=2; 2d_variance=1/3')
print('Lipschitz_feasible_construction_cost_upper=',F(2,3)/(Z*Z*L*L))
```

Actual output:

```text
jump_height= 1/768 optimal_halfwidth= 1/1536
paired_cross_section_integral= 1/2359296 = w^2/(4L): True
TV_lower_for_unit_tangent_length= 1/4718592 = w^2/(8L): True
1d_triangular_kernel_total_variation=2; 2d_variance=1/3
Lipschitz_feasible_construction_cost_upper= 1/216
```

The printed derivative/moment sentence is a label: the moments were separately verified by the prior fractions checker; the 1D total variation 2 is an elementary integral of the triangular kernel's piecewise derivative and was not itself calculated by this cell. This selected synthetic check is not a proof of weak closure, original optimality, convergence, source priority, or the whole theorem. The general argument is the written proof above.

## 7. Attribution and review limits

The publisher PMLR theorem's objective is FIRST-power l1 sensitivity norm. Squared-l1 and registered squared-Euclidean objectives are different; this note imports neither a publisher optimality theorem nor an external selector. The fresh result is a conditional consequence of the named original all-law theorem and elementary geometry, not a proof of SOURCE-MATCH-U1, worldwide novelty or parent adoption. Historical held outcomes are not accepted premises. No preexisting file was edited or overwritten. Request complete disjoint review of the closure/attainment, (5)–(6), all-shift exact-privacy caller, BV upper and strip lower before adoption; no full-proof scientific execution, formal/kernel/human/configured-family review, or novelty clearance is claimed.
