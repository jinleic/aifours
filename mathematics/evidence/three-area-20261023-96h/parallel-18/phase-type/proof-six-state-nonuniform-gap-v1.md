# A topology-unrestricted heterogeneity gap for residual six-state PH representations

Before-creation clock observed: **2026-10-23T13:59:11-07:00**. Owner: `MathResearch96h`, retained slotmath-1. Status: **CANDIDATE / NOVELTY_UNCLEAR**, written reasoning only. This is the first new primary proof packet in the18-slot write root. Exploratory symbolic reasoning preceded the new-slot freeze and was disclosed in its selection. No scientific program, matrix sampling or symbolic-algebra execution occurred.

## 1. Exact claim and what it does not prove

Let a>c>0,b>0,d=a-c and beta=b/d. Suppose

    H(s)=c(a^2+b^2)^2/[(s+c)((s+a)^2+b^2)^2]

has an arbitrary six-state PH representation(alpha,T), and assume

    beta^2>1/2.

No equality of diagonals, companion form, irreducibility assumption, single initial state or single exit state is imposed. Put

    lambda_i=-T_ii,
    mu=(1/6)sum_i lambda_i,
    sigma^2=sum_i(lambda_i-mu)^2.

The characteristic polynomial necessarily has form D5(s)(s+u). The candidate conclusion is the quantitative gap

    sigma > (sqrt3/2)d,                                    (G1)

    max_i lambda_i-min_i lambda_i > d/sqrt2,                (G2)

    mu-a > [(sqrt26-4)/20]d,                               (G3)

    u-c > [(8+3sqrt26)/10]d.                               (G4)

Thus any residual PH6 must be a **genuinely far-from-uniform** holding-rate representation, with a correspondingly separated hidden real pole. An infinitesimal tuning of the equal-diagonal endpoint cannot extend it above beta^2=1/2.

These are necessary conditions, NOT a six-state impossibility. Large holding-rate variation and large hidden u are still allowed by the inequalities. The unrestricted minimum in the G7 band remains6or7; the proof does not claim7.

## 2. Characteristic binding and the accessible dominant pole

The reduced target denominator D5 is monic degree5 and uncanceled. For six states it divides det(sI-T), so

    det(sI-T)=D5(s)(s+u)

with u real and positive by Hurwitz stability.

The universal five-state trace obstruction from the operative baseline is elementary: an order5 generator shifted by c has spectrum0,-d+ib twice,-d-ib twice. Its trace-square is4(d^2-b^2), while diagonal Cauchy bounds it below16d^2/5. Hence beta^2<=1/5 for every order5 representation, and degree excludes lower orders. In the present region, deleting an unreachable state from a six-state representation would contradict this fact. Thus all six states are reachable from the positive initial support.

Every transient PH state can reach a positive exit. Otherwise its reachable graph would contain a final class with no exits and zero row sums, forcing eigenvalue0. For a dominant irreducible diagonal block, reachability and co-reachability make the initial and exit semigroup factors strictly nonzero on that block. Positive left/right Perron vectors then imply a lower bound C exp(rho t) on f(t+2t0), where rho is the block spectral abscissa and t0>0 is fixed. The exact inverse density of H has leading positive term

    [c(a^2+b^2)^2/(d^2+b^2)^2] exp(-ct),

with all other terms polynomial times exp(-at). Therefore rho cannot exceed-c. Since-c is a pole/eigenvalue, the full spectral abscissa is-c and

    u>=c.                                                 (1)

This positivity argument prevents a canceled slower Perron mode; it does not assume all noncritical hidden eigenvalues are observable. It is the same trimming argument independently checked in the earlier L6 packet, with its pair-block wording correction applied by addendum001. The argument here does not use an ell0 conjugate-pair comparison.

## 3. Mean-centered spectral traces

The trace of the characteristic spectrum gives

    6mu=c+4a+u.

Write

    h=mu-a, Delta=b^2-d^2/2>0.

Then

    u-c=2d+6h, h>=-d/3,                                   (2)

using(1). Let C=T+mu I. It is a real Metzler matrix with trace0, not necessarily entrywise nonnegative. Its eigenvalues are

    d+h, -d-5h, h+ib twice, h-ib twice.

Consequently, by direct algebraic-multiplicity trace expansion,

    tau2=tr(C^2)=2d^2+12dh+30h^2-4b^2
                =12dh+30h^2-4Delta,                        (3)

    tau3=tr(C^3)
        =-12h[d^2+6dh+10h^2+b^2].                          (4)

No diagonalizability or spectral-realization sufficiency is used. Formula(4) expands from(d+h)^3-(d+5h)^3+4(h^3-3hb^2).

Let delta_i=C_ii=mu-lambda_i. Their sum is zero and sum delta_i^2=sigma^2. Decompose

    C=D+B, D=diag(delta_i), B>=0 entrywise, diag B=0.

Then tau2=sigma^2+tr(B^2)>=0. If -d/3<=h<=0, the first two terms in(3) are

    6h(2d+5h)<=0,

because2d+5h>=d/3>0. Subtracting4Delta makes tau2 negative, impossible. Hence

    h>0, tau3<0.                                         (5)

In particular sigma cannot be zero: if it were, C=B would be nonnegative and tau3=tr(B^3)>=0. Also tau2>0, since tau2>=sigma^2.

## 4. A six-dimensional centered-Metzler trace inequality

For any distinct i,j let x=delta_i+delta_j. The remaining four diagonal entries sum to-x. Cauchy–Schwarz on those two groups gives

    sigma^2>=x^2/2+x^2/4=3x^2/4,

so

    delta_i+delta_j>=-2sigma/sqrt3.                        (6)

Also each delta_i>=-sigma, yielding

    sum_i delta_i^3>=-sigma sum_i delta_i^2=-sigma^3.       (7)

Put q_ij=B_ij B_ji>=0 for i<j, and P2=2sum_(i<j)q_ij=tr(B^2). Cyclic trace expansion gives exactly

    tau3=sum_i delta_i^3
         +3sum_(i<j)(delta_i+delta_j)q_ij
         +tr(B^3).

The last term is nonnegative. Using(6)/(7),

    tau3>=-sigma^3-sqrt3 sigma P2
         >=-sqrt3 sigma(sigma^2+P2)
         =-sqrt3 sigma tau2.                              (8)

The second inequality uses sqrt3>=1. This bound is derived directly for the trace-zero Metzler matrix; it does NOT incorrectly apply nonnegative-matrix trace positivity to C itself.

## 5. The variance gap and its consequences

Let R=d^2+6dh+10h^2+b^2. Combining(4)/(8) gives

    12hR<=sqrt3 sigma tau2.

Since Delta>0 and h>0, equation(3) gives the strict bound

    tau2<12dh+30h^2=6h(2d+5h).

After canceling h>0,

    sigma > (2/sqrt3) R/(2d+5h).                           (9)

Moreover

    R>(3/2)d^2+6dh+10h^2
      >(3d/4)(2d+5h),

because the remaining positive expression is(9/4)dh+10h^2. Substituting into(9) proves(G1): sigma>sqrt3 d/2.

For the holding-rate range M=max lambda_i-min lambda_i, the mean minimizes the sum of squared deviations. Using the midpoint of the smallest and largest rate therefore gives

    sigma^2<=6 M^2/4=(3/2)M^2.

Together with(G1), this implies M>d/sqrt2, proving(G2).

Finally tau2>=sigma^2>3d^2/4 while tau2<12dh+30h^2. With t=h/d>0,

    40t^2+16t-1>0,

whose positive root is(sqrt26-4)/20. This proves(G3). Substituting in u-c=2d+6h gives

    u-c>[2+(3/10)(sqrt26-4)]d
        =[(8+3sqrt26)/10]d,

which is(G4). Every inequality and constant has a written derivation; none was inferred from sample points.

## 6. Checks, interpretation and the exact remaining gap

At the already constructed uniform-rate six-state endpoint beta^2=1/2, sigma0 and u-c2d. That does not contradict the theorem, whose hypothesis is the strict inequality beta^2>1/2. The proof's strict use of Delta>0 is visible in(3),(5),(9).

The new obstruction is topology-unrestricted and quantitatively rules out an entire neighborhood of equal holding rates, rather than one fixed companion. It supports the previous restricted uniform-rate exclusion without retroactively changing that old packet's review label. It still leaves a real class to analyze: nonuniform PH6 with sigma>sqrt3 d/2, rate span>d/sqrt2 and hidden u above(G4), subject also to the L6 layer/path constraints.

Next bounded action: bind this separated hidden-pole/heterogeneity regime to the positive-path identity and the single doubled layer. A missing global rate inequality is not supplied by the variance gap alone. No full minimum7, all-beta minimum formula or solved-book claim is made.

This candidate requires parent and separate pinned written reconstruction. The proof uses classical trace/walk/Perron mechanisms; priority remains unestablished. The shared parent verification and timestamp errata are mandatory. No proof-assistant kernel, outside-model review or scientific program has been used in this slot.
