# Quantitative density and reverse-infinity stability at high privacy

**AUTHOR CANDIDATE — WRITTEN; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 20:09:01 PDT 2026`.

## 1. Precise statement and import

Condition on the unreviewed source-independent quantitative all-law result `frontier-20261028-quantitative-high-privacy-rigidity-v1.md`, SHA-256 `dc2e2881f2b2f2978ab03ce505175f569272a26a8501e33a6c2feda7381b79be`. For 0<epsilon<=1/4 let X be ANY original full-D-private law with finite first moment. Put `Z=epsilon X`, let f be its all-point private density, `lambda(z)=(1/4)e^(-||z||_1)`,

    D=E||Z||_1-2e^(-epsilon)>=0,
    H=D^(1/3)+D+epsilon.                                                 (1)

There are universal positive constants C,h0 such that, whenever H<=h0,

    ||f-lambda||_infinity <= C H^(1/4),
    D_infinity(Lambda||Law(Z)) <= C H^(1/4).                            (2)

The infinity norm is essential supremum, and the directed max divergence is `log esssup(lambda/f)`. In particular every fixed reverse Rényi order is at most the second bound. These are explicit universal moduli in terms of a genuine finite-epsilon mean gap, not just qualitative nearopt convergence. No forward-order>1 convergence is asserted; the separately pinned unreviewed 924c candidate gives counterexamples even for original-J-nearopt laws.

## 2. Smoothing a W1 bound into a density sup bound

The import proves `w=W1_l1(Law(Z),Lambda)<=C H`. Group privacy implies the all-point ratio

    f(z+h)<=e^(||h||_1+epsilon) f(z),
    ||f||_infinity<=e^(1+epsilon)/2.                                     (3)

Let rho_delta(z)=delta^(-2)rho(z/delta), where rho is a fixed smooth probability kernel supported in D. For delta<=1,

    ||f-f*rho_delta||_infinity <= C(delta+epsilon),
    ||lambda-lambda*rho_delta||_infinity <= C delta.                     (4)

For the difference of mollifications, any coupling of Z and Lambda and the Lipschitz norm of the kernel give

    ||f*rho_delta-lambda*rho_delta||_infinity
       <= ||grad rho_delta||_infinity W1_l1 <= C w/delta^3.               (5)

In 2D, the kernel height contributes delta^-2 and its gradient another delta^-1. Choosing `delta=w^(1/4)` when w<=1, with a limiting argument at w=0, yields

    ||f-lambda||_infinity <= C(w^(1/4)+epsilon) <= C H^(1/4).             (6)

The last inequality uses epsilon<=H<=h0<=1. No weak compactness or nonquantitative subsequence argument is needed.

## 3. Reverse infinity bound

Applying (3) from z to 0 gives the GLOBAL lower envelope

    f(z)>=f(0)e^(-epsilon-||z||_1)
        =[4 f(0)e^(-epsilon)]lambda(z).                                  (7)

By (6), `4f(0)->1` quantitatively; the all-point representative and its convolution obey the same bound even at z=0. Normalization ensures `4f(0)e^(-epsilon)<=1`. For H sufficiently small the factor is bounded away from 0, and

    D_infinity(Lambda||Law(Z))
       <=epsilon-log[4f(0)] <=C(w^(1/4)+epsilon) <=C H^(1/4).           (8)

Rényi divergence is monotone in order, proving the announced reverse finite-order corollary. The inequality's direction is essential: it supplies NO analogous forward max-divergence bound.

## 4. Status

The smoothing and envelope argument is WRITTEN, conditional only on the pinned unreviewed dc2 W1 modulus; standard coupling and smooth-kernel estimates are used. No numerical, formal, independent-model or human verification, novelty, source-equivalence or parent acceptance is claimed. Review should check the 2D delta^-3 factor, all-point value at 0, parameter regime H<=h0 and the direction of (7).
