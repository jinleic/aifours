# Critical first-norm / Euclidean-square crossover for all private laws

**AUTHOR CANDIDATE — WRITTEN with a bounded numerical curve diagnostic; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 19:07:48 PDT 2026`.

## 1. Exact original class and the new critical-weight limit

For b=e^(-epsilon) in (0,1), let F_b be ALL Borel noise laws on R^2 satisfying epsilon privacy for EVERY Borel event and EVERY shift in the FULL CLOSED l1 unit diamond D. Let `s=b^(1/4)` and fix any finite theta>=0. Define the genuine mixed-degree all-law optimum

    H_theta(b)=inf_(mu in F_b) E_mu[ |X|_2^2 + theta s ||X||_1 ].       (1)

The first-norm weight is `theta b^(1/4)`, not a fixed lambda on squared-l1. It is precisely the scale at which the mean-l1 and original squared-Euclidean losses both survive in the rescaled core objective.

Put

    c_theta(z)=|z|_2^2+theta||z||_1,
    G_theta(T)=integral_R2 [T-c_theta(z)]_+ dz.

G is continuous, strictly increasing for T>0, starts at 0 and tends to infinity. There is therefore a UNIQUE `T_theta>0` with

    G_theta(T_theta)=2/3.                                                (2)

The candidate source-independent theorem is

    H_theta(b)=T_theta sqrt(b)+O_theta(b^(3/4))                          (3)

for EVERY fixed finite theta>=0. For ANY actual feasible laws whose mixed cost is `<=T_theta sqrt(b)+o(sqrt(b))`,

    Law(b^(-1/4)X) -> Uniform{z:c_theta(z)<=T_theta} in TOTAL VARIATION. (4)

No optimizer existence/uniqueness, symmetry or radial ansatz is assumed. Theta=0 is the ORIGINAL squared-Euclidean problem and `T_0=2/sqrt(3pi)`. The first moment and Euclidean components have explicit different limits in §6. This is a source/target crossover, not a claim that PMLR printed a mixed-cost theorem or that this is a novel global result.

## 2. The curve, exact quadrature, and endpoint behavior

For `a(phi)=cos(phi)+sin(phi)` in [0,pi/2], the boundary radius of the actual cost sublevel is

    R_theta(phi,T)=[sqrt(theta^2 a(phi)^2+4T)-theta a(phi)]/2.

Thus the equation in (2) is the explicit one-dimensional geometric integral

    G_theta(T)=4 integral_0^(pi/2)
       [T R^2/2 - R^4/4 - theta a R^3/3] dphi =2/3.                  (5)

No unknown density or optimizer family remains in this equation. At theta=0, `G_0(T)=pi T^2/2`, giving `T_0=2/sqrt(3pi)` and disk radius `(4/(3pi))^(1/4)`.

The map theta->T_theta is strictly increasing: for fixed T, the integrand in G decreases strictly as theta increases on a positive-area region. It is concave, because for each b the original-law infimum H_theta(b) is the infimum of affine functions of theta, and the pointwise leading limit H_theta(b)/sqrt b=T_theta preserves concavity.

At theta=0, differentiating G under the bounded integral gives

    T'_0 = [integral_(|z|<=R0)||z||_1 dz]/[pi R0^2]
         = 8 R0/(3pi),      R0=(4/(3pi))^(1/4).                         (6)

As a SEPARATE ITERATED theta->infinity limit, put T_theta=theta^(2/3)u and z=theta^(-1/3)v. Then

    G_theta(T_theta)=integral [u-||v||_1-theta^(-4/3)|v|_2^2]_+ dv.

For fixed u, dominated convergence gives `(2/3)u^3`; monotonicity of G and bracketing around u=1 therefore give `T_theta/theta^(2/3)->1`, and the correspondingly rescaled cost bodies approach D. This is NOT a claimed uniform joint limit for theta(b)->infinity.

## 3. All-law peak-floor lower bound with a nonhomogeneous scaled cost

Every original feasible law has a bounded all-point private density representative p. Let M=esssup p and choose x0 with `p(x0)>=(1-s)M`. All-point full-D privacy gives a density floor `ell=b(1-s)M` on x0+D. Put g=p-ell 1_(x0+D), y=s^2 M and h=integral g=1-2ell. Then 0<=g<=M and ell=(1-s)y s^2.

For the physical cost `|x|^2+theta s||x||_1`, the floor's integrated cost on a translate is

    F_s(x0)=integral_(x0+D)[|x|^2+theta s||x||_1]dx
             >= 2/3+2|x0|^2+(4/3)theta s.                              (7)

The squared term is exact by symmetry; the translated norm integral is an even convex function of x0 and is minimized at zero. Scaling `g^#(z)=s^2 g(sz)`, its mass is h, its cap is y, and the EXACT cost decomposition is

    E[|X|^2+theta s||X||_1]/s^2
       =(1-s)y F_s(x0) + integral c_theta(z)g^#(z)dz.                  (8)

For ANY 0<=g^#<=y and ANY T>0,

    integral c_theta g^# >= T h - y G_theta(T).                         (9)

This pointwise dual bathtub inequality follows by adding/subtracting T and using the cap only where c_theta<T. Choose T=T_theta so `G_theta(T)=2/3`. For eta->0 instead of eta=s, (7)–(9) also show the useful nonasymptotic fact: if theta>0 and `s<=2theta/(3T_theta)`, then EVERY fully private law satisfies `cost>=T_theta s^2` exactly.

For theta=0 or the general leading asymptotic, an actual upper law below bounds a minimizing sequence's cost/s^2; its positive J-floor then bounds y above. With eta=s, (7)–(9) give `cost/s^2>=T_theta-O_theta(s)` for such a sequence. Together with the upper law this proves (3), without assuming the peak is attained or that the unknown optimizer has any shell form.

## 4. Genuinely private matching upper law

Take the actual compact convex core `S=s K_theta`, `K_theta={z:c_theta(z)<=T_theta}`. Its normalized geometric shell density is `b^(min{k:x in S+kD})/Z`. The triangle inequality for the closed D proves full event privacy; this is an actual law.

Let `A_theta=|K_theta|`, `I_theta=integral_(K_theta)c_theta(z)dz`. The defining equality (2) is `T_theta A_theta-I_theta=2/3`. The top core has area `s^2 A_theta` and physical cost integral `s^4 I_theta`. The k=1 shell contributes `s^4[2/3+O_theta(s)]` to the numerator, because `S+D` lies between D and a D-enlargement by O_theta(s), and the first-moment weight is theta s. The k>=2 contribution is O_theta(s^8); the positive layer normalizer has denominator `s^2 A_theta+O(s^4)`. Hence the actual law has cost

    s^2 [I_theta+2/3]/A_theta+O_theta(s^3)
      =T_theta s^2+O_theta(s^3),

which is the matching upper bound in (3).

## 5. EVERY first-order-near-optimal law has the unique core shape

Let any feasible laws satisfy the near-optimal condition in (4), and use the SAME actual peak-floor variables (8). The J-floor bounds y uniformly above; after `ell=O(s^2)` its mass h tends to 1. Since `c_theta(z)>=|z|^2`, the ordinary 2D squared-cost bathtub lower bound forces y away from 0.

Define the nonnegative dual deficit at the FIXED threshold T=T_theta:

    Delta = integral_(c<T)(T-c)(y-g^#) + integral_(c>T)(c-T)g^#.       (10)

Using (8), h=1-2(1-s)y s^2, G_theta(T)=2/3 and (7) gives

    cost/s^2 >= T + 2(1-s)y|x0|^2 - O_theta(s)y + Delta.                (11)

Near-optimality, y bounded above/below and Delta>=0 therefore force `x0->0` and `Delta->0`.

The target cap profile is `y 1_(c<=T)`. For any d>0, the deficit controls its L1 error outside the band `|c-T|<d` by Delta/d. The band has area O_theta(d): formula (5)'s boundary radius is differentiable in T in a neighborhood of the strictly positive T_theta, with uniformly bounded radial derivative. Both densities are <=y. Hence `||g^#-y 1_(c<=T)||_1->0`. Since the mass h->1, this forces `y->1/A_theta`, and the cap profile tends to the UNIFORM density on K_theta. The physical floor has total probability 2ell=O(s^2), so it disappears in TV after rescaling. This proves (4) for EVERY near-optimal original law, not merely the constructed shell.

## 6. Separate objective limits and the macroscopic floor

The scaled density convergence and bounded mixed cost give uniform integrability of the SCALED FIRST norm: `||z||_1<=sqrt(2)|z|` and the second moments are uniformly bounded. The floor contributes only O(s) to `E||X||_1/s`, since x0->0 and its mass is O(s^2). Thus

    E||X||_1/s -> (1/A_theta) integral_(K_theta)||z||_1 dz = T'_theta.  (12)

The equality with T'_theta follows by implicit differentiation of (2), with finite positive area A_theta.

For the squared component, the SAME bathtub deficit makes the remaining-core scaled cost concentrate at x=0, while the floor density ell/s^2 tends to 1/A_theta on D because x0->0. Consequently

    E|X|^2/s^2 -> (1/A_theta)integral_(K_theta)|z|^2 dz
                   +(2/3)/A_theta.                                       (13)

The extra `(2/3)/A_theta` is a genuine macroscopic privacy-tail contribution. Equations (12)–(13) sum to T_theta by (2). Thus the scaled-law TV limit does NOT capture the entire second moment, and W2 convergence to that uniform law is impossible. This is not a claim that the unscaled noise has a hard finite support.

## 7. Actual bounded curve diagnostic and limits

An in-kernel Python cell evaluated (5) with floating `math`, Simpson grids N=256 and512 and 60 bisections. Actual output:

```text
theta= 0.0 T_simpson512= 0.651470016 N256_vs512_abs= 2.22e-16
theta= 0.5 T_simpson512= 0.972753243 N256_vs512_abs= 4.93e-12
theta= 1.0 T_simpson512= 1.261048043 N256_vs512_abs= 2.46e-11
theta= 2.0 T_simpson512= 1.773108537 N256_vs512_abs= 9.33e-11
theta= 10.0 T_simpson512= 4.712132019 N256_vs512_abs= 7.39e-10
theta0 exact= 0.651470016
```

These are numerical diagnostics, not interval enclosures or proof of (2)–(4). The exact result is the written peak-floor/dual-bathtub argument above; it imports NO LAW642, MDA, PMLR, v241, f68 or any earlier research theorem. Request disjoint review of fixed-threshold dual equality, density-cap uniform integrability, all-law near-minimizer quantifiers and the macroscopic second-moment term. No independently reviewed/formal/kernel/human/configured-family, priority, novelty or parent acceptance is claimed.
