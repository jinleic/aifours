# Supercritical mixed-loss allocation and Wasserstein phase change

**AUTHOR CANDIDATE — WRITTEN; exact finite Fraction checks are separately identified below; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 19:12:52 PDT 2026`.

## Scope and explicit import

Assume the unreviewed peak-floor/dual statements and notation in `frontier-20261028-mixed-degree-three-regime-crossover-v1.md`, SHA-256 `712f291cdd97525ca9776f77150c03ee12130d309933ea406c46c921c0996085`, §§4–6. No prior LAW642/MDA/PMLR theorem is imported. Let b->0 and kappa=kappa(b)>0 with `kappa/b^(1/4)->infinity`; kappa may tend to zero, a positive limit, or infinity, or oscillate. Define

    A=[b(1+2kappa)/kappa]^(1/3), C=kappa A,
    J=E|X|_2^2, L=E||X||_1.

For EVERY actual full-D-private law sequence satisfying `J+kappa L<=C(1+o(1))`, the imported candidate gives `(J+kappa L)/C->1` and `Law(X/A)->Uniform(D)` in TV. The additional WRITTEN conclusions are, with o(1) interpreted along the ENTIRE actual kappa sequence,

    J/C - 1/[3(1+2kappa)] ->0,                                           (1)
    L/A - [2/3+2kappa/{3(1+2kappa)}] ->0.                               (2)

Thus kappa L/C has the same moving expression as L/A and the two normalized contributions sum to 1 asymptotically. There is no assumption that either moving rational expression itself converges.

If kappa->0 then `Law(X/A)->Uniform(D)` in W1 (for either Euclidean or l1 ground metric); if kappa does NOT tend to 0 then W1 does not tend to zero. Indeed, for the l1-ground Wasserstein distance,

    W1(Law(X/A),Uniform(D)) >= 2kappa/[3(1+2kappa)]+o(1).                (3)

For EVERY supercritical kappa sequence, the scaled Euclidean second moment diverges and so does the corresponding W2 distance from Uniform(D):

    E|X/A|_2^2 -> infinity,    W2(Law(X/A),Uniform(D))->infinity.         (4)

These statements concern scaled laws. They do not say the unscaled near-optimum has infinite moments; each near-optimum here has finite J and L.

## Centering the actual peak floor uniformly in kappa

Use the imported proof's exact variables: `d=(2+4kappa)/3`, `r=(b d/kappa)^(1/3)`, `alpha=r/kappa->0`, `T=(3/2)^(1/3)`, `A=Tr`, `C=T kappa r`; choose the `(1-r)`-near peak x0, cap `y=r^2 M`, floor `ell=b(1-r)M`, and residual `g^#`. Its mass is h=1-2ell, and the imported proof establishes y bounded above/below, `ell=O(r)->0`, `y->1/(2T^2)`, and the nonnegative L1-bathtub deficit Delta->0.

Set

    F_kappa(x)=integral_(x+D)[|u|^2+kappa||u||_1]du,
    Q(x)=integral_(x+D)||u||_1du - 4/3.

Exactly `F_kappa(x)-d=2|x|^2+kappa Q(x)`. Q is even, continuous, nonnegative, strictly positive off zero, and coercive: its coordinate integrals `integral_D |u_i+x_i|du` are strictly minimized at x_i=0, since the D coordinate marginal has positive density on (-1,1). Moreover

    [F_kappa(x)-d]/d
      >= [(1+kappa)/d] min(2|x|^2,Q(x))
      >= (3/4) min(2|x|^2,Q(x)).                                        (5)

The last constant is uniform for all kappa>=0. The exact decomposition underlying the imported (13) strengthens to

    (J+kappa L)/(kappa r)
      = T + (1-r)y[F_kappa(x0)-d]/d + Delta
          +alpha integral |z|^2 g^# - r y -2T ell.                       (6)

All terms explicitly following T are nonnegative except the final two; those final errors vanish. Since near-optimality makes the left side tend to T, (5)–(6), and y bounded away from zero, force

    x0->0,  alpha integral |z|^2 g^# ->0.                                 (7)

This centering is derived uniformly EVEN if kappa->infinity; relying on the quadratic part alone would not suffice there.

## Cost allocation

The physical floor is `ell 1_(x0+D)`, and the residual's scaled quadratic contribution to J/C is `alpha integral |z|^2 g^#/T`, which tends to zero by (7). Its floor contribution is

    J/C = [(1-r)y/(Td)] [2/3+2|x0|^2] + o(1).

Because `y/T->1/(2T^3)=1/3` and `1/d<=3/2`, this is (1):

    J/C = 2/(9d)+o(1) = 1/[3(1+2kappa)]+o(1).

For the first-norm part, the exact dual identity gives `integral ||z||_1 g^# =Th-y+Delta ->T-y`. The floor contributes `(1-r)y kappa/(Td)` times `integral_(x0+D)||u||_1du`; continuity and x0->0 make this integral tend to 4/3. Since kappa/d<=3/4,

    L/A = (T-y)/T + (4/3)(y/T)(kappa/d)+o(1)
        = 2/3+2kappa/[3(1+2kappa)]+o(1),

which is (2). Its first 2/3 is the uniformly distributed core's first moment; the extra `2kappa/[3(1+2kappa)]` is a first-moment contribution of the macroscopic privacy floor. Total variation convergence alone would miss it.

## W1 iff kappa->0, and W2 divergence

`Uniform(D)` has mean l1 norm 2/3. The norm is 1-Lipschitz in the l1 metric, so the Kantorovich lower bound and (2) give (3). If kappa->0, (2) instead yields convergence of l1 first moments to 2/3, while the imported TV convergence gives weak convergence; weak convergence plus convergence of the first moment gives W1 convergence. The l1 and Euclidean ground metrics are equivalent. Conversely, W1 convergence makes the moment discrepancy vanish, forcing `kappa/(1+2kappa)->0`, hence kappa->0.

For W2, no upper moment estimate or uniform integrability is being assumed. The peak floor alone gives

    E|X/A|^2 >= [b(1-r)y/(T^2 r^4)] (2/3).

As b=s^4 and r^3=b d/kappa,

    b/r^4 = [kappa/(d s)]^(4/3)->infinity.

Indeed kappa/d is bounded below by a fixed multiple of min(kappa,1), and both `kappa/s` and `1/s` tend to infinity. The displayed bound diverges because y stays bounded away from zero. Minkowski's inequality for any coupling then lower-bounds W2 by the difference between square roots of second moments, proving (4).

## Exact identity checks and examples

The Python eval kernel used `fractions.Fraction` to check that the rational formulae for the normalized J and kappa-L shares sum to 1 for kappa in {0, 1/2, 1, 3, 1000}. It printed, respectively,

```text
kappa=0    J/C=1/3    kL/C=L/A=2/3       L1-tail-excess=0
kappa=1/2  J/C=1/6    kL/C=L/A=5/6       L1-tail-excess=1/6
kappa=1    J/C=1/9    kL/C=L/A=8/9       L1-tail-excess=2/9
kappa=3    J/C=1/21   kL/C=L/A=20/21     L1-tail-excess=2/7
kappa=1000 J/C=1/6003 kL/C=L/A=6002/6003 L1-tail-excess=2000/6003
```

The kappa=0 row is the LIMIT of formulae (1)–(2), not an admissible fixed member of the supercritical regime. These finite checks establish only rational algebra, not the asymptotic universal claims. This result depends on the pinned unreviewed predecessor and is not independently reviewed, formal, a novelty claim, or parent-accepted.
