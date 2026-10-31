# Exact all-law finite-privacy lower bound for mixed first and squared costs

**AUTHOR CANDIDATE — WRITTEN with exact rational sample checks; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 19:21:56 PDT 2026`.

## 1. Nonasymptotic theorem for every real weight

Fix ANY epsilon>0, b=e^(-epsilon), and real kappa. The full-D-private class consists of ALL Borel laws on R^2 obeying event privacy for EVERY shift in the closed l1-unit diamond D. For a law with finite second moment let

    J=E|X|_2^2, L=E||X||_1,
    phi_kappa(x)=|x|_2^2+kappa||x||_1,
    G_kappa(T)=integral_R2 (T-phi_kappa(x))_+ dx,
    d_kappa=inf_(x0 in R^2) integral_(x0+D) phi_kappa(x) dx.             (1)

Let B=B(b,kappa) be the UNIQUE real root above `min phi_kappa` of

    G_kappa(B)+2bB=b d_kappa.                                            (2)

Then EVERY actual full-D-private finite-J law satisfies the finite-privacy inequality

    J+kappa L >= B(b,kappa).                                             (3)

In particular (3) is a one-dimensional implicit lower boundary for the finite-epsilon (J,L) moment region for EVERY real scalar weight, with no optimizer family or privacy relaxation. For kappa>=0 laws with infinite J satisfy the bound trivially. For kappa<0 the finite-J requirement avoids undefined infinity-minus-infinity.

The exact translated floor constant d_kappa is elementary. For a=-kappa>0,

    d_kappa = 2/3+4kappa/3                         if kappa>=-1,
            = 2/3-4a/3-(16/3)(a-1)^3/a^2          if 1<a<=2,
            = 2/3-a^2                              if a>=2.             (4)

The minimizing floor center has both coordinates of absolute value 0, `2-2/a`, or `a/2` in the three respective regimes. Thus a negative scalar weight is NOT incorrectly forced to have its floor centered at zero. Equation (3) is a lower bound, NOT a finite-b optimizer-exactness claim.

## 2. Existence and uniqueness of the root

The physical scalar cost is coercive. Its minimum is 0 for kappa>=0 and `-kappa^2/2` for kappa<0. It is strictly greater than that minimum except at finitely many points, so every translated diamond has integrated cost STRICTLY above `2 min phi_kappa`; thus d_kappa>2 min phi_kappa. At `T=min phi_kappa`, the left side of (2) is `2b min phi_kappa < b d_kappa`. It tends to infinity, is continuous, and is strictly increasing because b>0. The unique root is strictly above the minimum, even if both B and d_kappa are negative.

## 3. Exact peak-floor and dual proof, including negative costs

Every feasible law has a bounded all-point private density representative p; take M=esssup p. For any eta>0 choose x0 with `p(x0)>=(1-eta)M`. Full-D privacy then gives the floor `ell=(1-eta)bM` on x0+D. Put `g=p-ell 1_(x0+D)`, so 0<=g<=M and its mass is `1-2ell`.

For ANY real T, the pointwise cap gives the exact nonnegative bathtub dual deficit

    integral phi_kappa g
       >= T(1-2ell)-M G_kappa(T).                                        (5)

This remains valid when phi_kappa or T are negative. Add the floor contribution and use `integral_(x0+D)phi_kappa>=d_kappa`:

    J+kappa L >= T+M[(1-eta)b(d_kappa-2T)-G_kappa(T)].                   (6)

At T=B, equation (2) makes `G_kappa(B)=b(d_kappa-2B)>=0`. Let eta->0; M is finite and (3) follows. The peak need not be attained, the law need not be centered or symmetric, and no density support restriction is imposed.

## 4. Computing the translated floor constant

The coordinate marginal of D is `2(1-|t|)_+`. Put `f(t)=integral_D |u1+t|du`, an even function. Direct integration gives, for t>=0,

    f(t)=2/3+2t^2-(2/3)t^3    for 0<=t<=1,
    f(t)=2t                    for t>=1.                                  (7)

Hence the translated floor integral is

    2/3+2(x1^2+x2^2)+kappa[f(|x1|)+f(|x2|)].                            (8)

The two one-coordinate minimizations are independent. For kappa=-a and 0<=t<=1 the derivative is `2t(2-2a+a t)`; for t>=1 it is `4t-2a`. Their global minimizing t is 0 when a<=1, `2-2/a` for 1<a<=2, and a/2 for a>=2. Substitution yields (4). Positive kappa also has t=0 by monotonicity.

## 5. Original objective and exact critical-scale specialization

For kappa=0 and T>=0, `G_0(T)=pi T^2/2`. Solving (2) yields the explicit finite-b lower bound

    J >= sqrt[4b/(3pi)+4b^2/pi^2] - 2b/pi.                              (9)

This agrees algebraically with the earlier independently written peak-floor bound but is derived here without importing it.

For fixed real theta, let `s=b^(1/4)` and `kappa=theta s`. For s sufficiently small, kappa>=-1 and the exact bound becomes `J+theta s L >= s^2 t_b`, where t_b is the unique threshold above min c_theta satisfying

    integral (t_b-|z|^2-theta||z||_1)_+ dz +2s^2 t_b
       =2/3+(4/3)theta s.                                                 (10)

If T_theta denotes the root with 2/3 on the right and zero normalization correction, implicit differentiation gives

    t_b = T_theta + [4theta/(3|K_theta|)]s + O_theta(s^2).                (11)

This is a FINITE-b supporting lower plane plus its fixed-theta expansion, not a matching higher-order assertion.

Optional conditional asymptotic comparison: if the separately pinned all-law crossover candidate `frontier-20261028-mixed-degree-three-regime-crossover-v1.md`, SHA-256 `712f291cdd97525ca9776f77150c03ee12130d309933ea406c46c921c0996085`, is correct, then for arbitrary nonnegative kappa(b), (3) is first-order sharp as b->0. B/(the actual optimum)->1: take any sequence of ratios kappa/b^(1/4), pass to a subsequence with a finite or infinite limit, and use (10) or the supercritical rescaling in §6 plus that candidate's actual upper laws. This optional comparison does NOT import the predecessor into (3)–(4), and does not certify the predecessor.

## 6. Supercritical rescaling of this very bound

If kappa/b^(1/4)->infinity with kappa>=0, put `d=(2+4kappa)/3`, `r=(b d/kappa)^(1/3)`, `alpha=r/kappa`, `B=kappa r t`. Equation (2) becomes EXACTLY

    integral (t-||z||_1-alpha|z|^2)_+ dz +(2kappa r/d)t=1.               (12)

Here r->0, alpha->0, and kappa/d<=3/4 even for unbounded kappa. Monotone bracketing and dominated convergence force `t->(3/2)^(1/3)`; so this finite-b lower bound alone gives

    B ~ [b kappa^2(1+2kappa)]^(1/3).                                     (13)

The matching upper law/all-nearopt shape is NOT asserted from the lower bound alone; it requires an actual separately established upper construction.

## 7. Actual rational checks and status

The Python eval kernel used `fractions.Fraction` for sample kappa values -3, -2, -3/2, -1, 0, 1. Selected exact outputs are

```text
kappa=-3/2  |center_i|=2/3  d=-44/27  2 min=-9/4  gap=67/108
kappa=-2    |center_i|=1    d=-10/3   2 min=-4    gap=2/3
kappa=-3    |center_i|=3/2  d=-25/3   2 min=-9    gap=2/3
kappa=-1    |center_i|=0    d=-2/3    2 min=-1    gap=1/3
kappa=0     |center_i|=0    d=2/3     2 min=0     gap=2/3
kappa=1     |center_i|=0    d=2       2 min=0     gap=2
```

These check only selected algebra and not the universal variational proof. Equations (1)–(13) are WRITTEN, not a formal or independently reviewed proof, and no novelty or parent acceptance is claimed. The finite lower bound and all real-weight floor minimization are source-independent; the optional first-order-sharpness comparison names its unreviewed predecessor explicitly.
