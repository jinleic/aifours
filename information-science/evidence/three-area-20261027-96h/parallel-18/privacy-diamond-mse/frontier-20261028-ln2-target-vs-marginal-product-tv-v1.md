# Exact TV certificate: true target versus optimal marginal product at ln 2

**AUTHOR CANDIDATE — WRITTEN plus exact Fraction interval arithmetic; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 20:22:41 PDT 2026`.

## 1. Named inputs and exact interval

At epsilon=ln 2, let P be the ACTUAL original full-D squared-Euclidean optimal law, conditional on parent v253/v241 as explicitly pinned by `frontier-20261028-ln2-original-target-certificate-v1.md` SHA-256 `50bfec41598fc25005f9630694f374571e92e2afc0788c5f37eed86154b1d5e4`. It is the radial diamond staircase with offset eta, the larger root of `eta^5+5eta^4+14eta^3+10eta^2-21eta+3=0`.

Let Q be the product of the two 1D squared-error optimal epsilon-private marginals, conditional on unreviewed `frontier-20261028-exact-scalar-marginal-relaxation-v1.md` SHA-256 `cde9bcc08bd4f87e635f1a2566fb2eaae6f1b289df5ebd4d36707229c8fc60ed`; its 1D staircase offset is `gamma=3^(1/3)-1`. Q is an auxiliary NON-full-D-private comparator, not an asserted original feasible law.

The written geometry plus exact Fraction checks establish

    140433557476/10^12 < TV(P,Q) < 140433557477/10^12.                 (1)

The decimal rendering is TV≈0.140433557476783. This is a real difference of complete laws, distinct from either their objective-value gap or the nearest-private TV distance. The actual-optimal-law interpretations explicitly depend on the named unreviewed/parent inputs.

## 2. Exact density levels and threshold regime

At b=1/2, m=1 define `D_eta=eta^2+2eta+3`, `Z_P=2D_eta`, `Z_1=2(gamma+1)` and

    C=Z_P/Z_1^2=D_eta/[2(gamma+1)^2].                                   (2)

For the two 1D indices n1,n2 and radial index n_R, the density ratio is

    q/p=C b^(n1+n2-n_R).                                                  (3)

The exact rational intervals in §4 imply

    0<eta-gamma<gamma,  0<2gamma-eta<1,  1<C<2.                        (4)

Write `|x_i|=n_i+u_i`. For n_i=0, `u_i in [0,gamma]`; for n_i>=1, `u_i in [gamma-1,gamma]`. On the full measure space, (4) implies the integer `k=n1+n2-n_R` lies in {-1,0,1}. Since b=1/2 and 1<C<2, Q's density is less than P's EXACTLY when k=1.

## 3. Exact sum of two angular triangles

The case k=1 is `u1+u2<=eta-1`. If both 1D indices are positive, the triangle area in the unit u-square is `(1+eta-2gamma)^2/2`; if exactly one index is 0, its triangle area is `(eta-gamma)^2/2`; if both are 0, the area is 0. The regime (4) makes both triangles untruncated. Summing the four sign quadrants and the two geometric indices, at m=1,

    Q(k=1)=[(1+eta-2gamma)^2/2+(eta-gamma)^2]/(gamma+1)^2.             (5)

On this region q/p=C/2, so

    TV(P,Q)=Q(k=1)[2/C-1].                                                (6)

Equations (2),(5),(6) are EXACT for these actual staircase laws. No numerical quadrature or inference from an objective difference is involved.

## 4. Actual exact interval checks

The Python eval kernel used `fractions.Fraction` for the brackets

    gamma in (4422495703074083823216,4422495703074083823217)/10^22,
    eta   in (7271025149432606453616,7271025149432606453617)/10^22.

It checked `(1+gamma_lo)^3<3<(1+gamma_hi)^3`, the exact P signs for eta, all inequalities (4), and an outward rational enclosure of (6). For (5), each of `1+eta-2gamma` and `eta-gamma` is positive, so replacing gamma by its upper endpoint and eta by its lower endpoint gives a lower numerator, and the opposite replacements give an upper numerator; combine with monotone denominators. Bound C similarly, then multiply the positive outward bounds for `Q(k=1)` and `2/C-1`. Exact rational comparisons certify both strict endpoints in (1).

The Fraction checks do not prove the parent v253/v241 theorem, cde9 scalar optimum, or the written triangular geometry. No formal, independent review, source-equivalence, novelty or parent adoption is claimed. Suggested review: central-shell triangle areas, the k range, likelihood signs, and outward interval monotonicity.
