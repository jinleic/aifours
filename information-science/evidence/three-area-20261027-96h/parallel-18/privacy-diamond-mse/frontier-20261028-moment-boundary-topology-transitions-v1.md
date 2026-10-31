# Two exact topology transitions on the limiting moment-region boundary

**AUTHOR CANDIDATE — WRITTEN; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 19:19:15 PDT 2026`.

## 1. Import and exact scope

Condition on the unreviewed all-law candidate `frontier-20261028-full-critical-moment-region-v1.md`, SHA-256 `c8ce61fb2d40463f5fdf488cb2ed5aebe40bf59c8bd97dc18b7674caf94bf463`. Its ALL-real scalarization, uniqueness of the parameter and universal scaled TV limit are REQUIRED here. Its moment-region and private-law assertions are not independently accepted by this note.

Let b->0, s=b^(1/4), J=E|X|^2 and L=E||X||_1. For each finite boundary pair `(u,v)` on the imported region, all attaining original full-D-private sequences have `Law(X/s)->Uniform(K_theta)` in TV, where `K_theta={|z|^2+theta||z||_1<=T_theta}` and theta is selected by `T'_theta=v`.

The present geometric claim concerns the SUPPORT K_theta of that SCALED LIMITING BULK ONLY. Actual private densities remain positive everywhere; no finite-b support hole or finite-b disconnection is claimed. The topology changes occur on the high-mean, theta<0, non-Pareto half of the exact moment-boundary; they are not instructions to prefer a worse mean.

## 2. Exact transition parameters

Write theta=-a with a>0, and set

    tau=(3pi)^(-1/2),
    a_h=[8/(3pi+8)]^(1/4),
    a_d=2 sqrt(tau)=2(3pi)^(-1/4),
    v_h=a_h (pi+8/3)/(pi+2).                                             (1)

Then 0<a_h<a_d, and the limiting bulk sets have the following topology:

* `0<=a<=a_h`: K_-a is star-shaped about the origin and contains a neighborhood of it.
* `a_h<a<a_d`: K_-a is an annulus (homeomorphic to S^1 x [0,1]), with a bounded hole containing the origin.
* `a=a_d`: K_-a is four disks touching in a cycle at four points; it is connected but its interior has four components.
* `a>a_d`: K_-a is four pairwise disjoint closed disks.

At the first transition the point in moment coordinates is

    (u_h,v_h)=(a_h v_h, v_h).                                            (2)

At the second it is `(u_d,v_d)=(3tau,a_d)`. Since v=T'_-a strictly increases with a by the imported strict concavity, these thresholds label the limiting lower-boundary geometry unambiguously.

## 3. The first threshold: a central hole opens

In a quadrant use polar angle phi, radius r and `A(phi)=cos(phi)+sin(phi)`. Then `c_-a=r^2-a A r`. At T=0,

    integral (0-c_-a)_+
       =(a^4/3) integral_0^(pi/2)(cos phi+sin phi)^4 dphi
       =a^4(pi/4+2/3),                                                   (3)

because the angular integral is `3pi/4+2`. Equating (3) to 2/3 gives exactly a=a_h. Since G(T,-a) is strictly increasing in T, `T_-a>0` for a<a_h, equals 0 at a_h, and is negative for a>a_h.

When T>=0, in each direction the radial sublevel is `[0,r_+(phi)]`; at T=0 the positive radius is a A(phi), and `r^2-a||z||_1<=r(r-a)` also shows a whole ball of radius a is inside the sublevel. This proves star-shapedness and a full neighborhood of the origin through a=a_h.

At a=a_h, direct radial integration gives

    area(K_-a)=a^2(pi+2),
    integral_K ||z||_1 dz = a^3(pi+8/3).                                 (4)

The imported identity T'=mean l1 then yields v_h in (1); because T=0 and theta=-a, `u=T-theta v=a v`, giving (2).

## 4. The second threshold and the intermediate annulus

The completed-square identity is

    c_-a(z)=(|z1|-a/2)^2+(|z2|-a/2)^2-a^2/2.                         (5)

Set `rho^2=T_-a+a^2/2>0`. In each quadrant K is the corresponding radius-rho disk centered at `(±a/2,±a/2)`, restricted to that quadrant.

If rho<=a/2, these four disks stay inside their quadrants and the defining positive-part integral is exactly `2pi rho^4`. Thus rho^2=tau and this configuration is self-consistent exactly when a>=a_d. At equality the disks touch their neighbors at one point on each axis; beyond it they are disjoint.

For a_h<a<a_d, T<0, so rho^2<a^2/2. Also rho>a/2: otherwise the separated-disk calculation would force rho^2=tau and hence a>=a_d, contradiction. Therefore `a^2/4<rho^2<a^2/2`. Along every direction, with `A(phi)=|cos(phi)|+|sin(phi)|`, the quadratic has two distinct positive roots

    r_±(phi)=[a A(phi) ± sqrt(a^2 A(phi)^2+4T_-a)]/2.                  (6)

The discriminant is strictly positive even on axes because `4rho^2-a^2>0`; the roots vary continuously around the circle, with `0<r_-<r_+`. The polar map `(phi,t)->[(1-t)r_-(phi)+t r_+(phi)](cos(phi),sin(phi))` is therefore a homeomorphism from the closed cylinder to K. Its interior hole contains the origin, and the interval cannot be collapsed except at the endpoint a=a_d. This proves the annulus statement without a picture or a numerical topology test.

## 5. Computation and limitations

The Python eval kernel checked the rational simplification `(4/3)*(3/4)=1` and `(4/3)*2=8/3` in (4), using `fractions.Fraction`. Floating diagnostics gave

```text
a_h≈0.8231532241272098   v_h≈0.9298845140324229   u_h≈0.7654374357917526
a_d≈1.1414639861778906   v_d≈1.1414639861778906   u_d≈0.9772050238058398
```

These decimals are not interval certificates; all transitions and formulae above are written analytic claims, conditional on the pinned unreviewed c8ce proof for their all-private-law meaning. No formal verification, independent review, novelty, parent adoption or source-equivalence conclusion is claimed.
