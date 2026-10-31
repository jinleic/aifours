# Explicit positive finite-epsilon joint-privacy gap

**AUTHOR CANDIDATE — WRITTEN; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 19:57:07 PDT 2026`.

## 1. Statement and named input

Condition on the unreviewed exact all-law 1D value/profile proof `frontier-20261028-exact-scalar-marginal-relaxation-v1.md`, SHA-256 `cde9bcc08bd4f87e635f1a2566fb2eaae6f1b289df5ebd4d36707229c8fc60ed`. The earlier qualitative strict-gap candidate is NOT imported.

For any fixed epsilon>0, b=e^(-epsilon), kappa>=0, put m=b/(1-b), `k=2m+kappa`, and let gamma in (0,1) be the pinned 1D optimal cubic root. Let V_1,kappa be the pinned exact 1D infimum, and V_2,kappa the original 2D infimum of `J+kappa L` under all events and FULL closed l1-diamond privacy. Define explicit quantities

    C=4/epsilon^2+2kappa/epsilon+1,
    R=max{1,sqrt(2C)},   N=ceil(2R+2),
    d=(1/4)min{gamma,1-gamma,1},
    zeta=b^(N+1)(1-b)d^2/(8R^2),
    c0=2(1-b^2)sqrt[2/(b k)],
    gap=[2zeta/(c0+sqrt(c0^2+4b zeta))]^2 >0.                          (1)

The written claim is the COMPUTABLE finite-epsilon lower bound

    V_2,kappa >= 2 V_1,kappa + gap.                                     (2)

It holds for every epsilon>0 and kappa>=0. The constant is intentionally extremely conservative. It strengthens the earlier nonquantitative strictness proof but does not establish optimality or novelty.

For pure L, the SAME construction gives a positive explicit gap above `2sqrt(b)/(1-b)`: use 1D gamma=`sqrt[m(m+1)]-m`, k=1, C_L=`2/epsilon+1`, R=max{1,2C_L}, and the same N,d,zeta,c0,gap formulae.

A concrete certified-in-written-form example at epsilon=ln 2 and kappa=0 is

    V_J(ln 2) >= 4+2*3^(2/3) + 1/(1,310,720,000)^2.                    (3)

Here the extra term is deliberately tiny; it is an explicit witness of incompatibility of the two exactly optimal marginal staircases, not a practical error estimate.

## 2. A rectangle incompatibility inequality

Let f be the actual bounded all-point 2D private density. Put I=(gamma-d,gamma), I+=(gamma,gamma+d), Q=I x I, and for each marginal define the nonnegative privacy slacks

    A_i=mu_i(I+)-b mu_i(I) >=0.                                          (4)

The horizontal and vertical D shifts of size d give nonnegative pointwise differences. On Q, telescoping the two shifts and comparing with the direct diagonal shift (d,d), also in D, gives

    b(1-b) mu(Q) <= A_2+b A_1 <= A_1+A_2.                              (5)

If J<=C, Markov gives `mu([-R,R]^2)>=1/2`. Every point of Q is at l1-distance <=2R+2 from every point of that square. Repeated full-D privacy yields `f(x)>=b^N f(y)` for every such pair, hence

    mu(Q)>=b^N d^2/(8R^2),       A_1+A_2>=zeta.                         (6)

The same argument for pure L uses Markov with R>=2C_L. No independence or 2D optimizer symmetry is assumed.

## 3. Quantitative 1D jump-deficit bound

For one coordinate let `Delta=E[Y^2+kappa|Y|]-V_1,kappa>=0`. Symmetrize its density p_s; its cost is unchanged. Use the cde9 notation `p_n(x)=p_s(n+x)`, `S=sum p_n`, `g=2S`, and `a=essinf g`, x in (0,1). Full 1D privacy gives `a<=g<=a/b`, `a<=1`. Write the fractional cost `c(x)=k x+x^2` with `c'(x)>=k>0`.

The exact deficit splits into nonnegative integer-tail and fractional-profile terms. The fractional term is

    Delta_frac=integral_0^gamma [c(gamma)-c(x)](a/b-g(x))dx
              +integral_gamma^1 [c(x)-c(gamma)](g(x)-a)dx <=Delta.      (7)

Set `Remainder(x)=S(x)-p_0(x)/(1-b)>=0`. The first integer-tail slack is `(1-b)Remainder`, and its contribution to squared cost is at least twice its integral. Hence

    2(1-b) integral_0^1 Remainder(x)dx <=Delta.                          (8)

Let A_s be the I-to-I+ shift slack of the symmetric marginal. Using `p_0=(1-b)g/2-(1-b)Remainder`, (7), and a band of arbitrary width h>0 around gamma gives

    A_s <= (1-b^2)/2 [Delta/(k h)+h/b] + b Delta/2.                     (9)

Indeed away from the h-band, the cost difference is >=k h; inside, each density deficit is <=1/b and each band's length is <=h. Both the positive-side slack A and reflected negative-side slack are nonnegative, and `A_s=(A+A_reflected)/2`, so A<=2A_s. Choosing `h=sqrt(b Delta/k)` (or a limiting h if Delta=0) yields

    A <= 2(1-b^2)sqrt[Delta/(b k)] + b Delta.                           (10)

For pure L, c(x)=x and the integer mean tail has the same first-slack bound (8), so (10) remains true with k=1.

## 4. Combining the two coordinates

Let `Delta_i` be the exact 1D scalar cost gaps of the two marginals and `Delta=Delta_1+Delta_2=J+kappa L-2V_1,kappa`. Apply (10) twice and `sqrt(Delta_1)+sqrt(Delta_2)<=sqrt(2Delta)`:

    A_1+A_2 <= c0 sqrt(Delta)+b Delta.                                    (11)

Equations (6) and (11) force the explicit root inequality in (1), proving (2) for every law with J<=C. The actual product-Laplace law has mixed cost `C-1`, so a minimizing sequence is eventually in that class; taking its infimum gives (2) without assuming attainment. The pure-L case is identical, with the first-moment Markov bound in §2.

For (3), b=1/2, m=1, k=2, gamma=`3^(1/3)-1` lies between 2/5 and 1/2. The actual feasible gamma=18/25 2D staircase from cde9 has J<10, so a minimizing sequence has J<=10; choose R=5, N=12 and d=1/10. Then `zeta=1/327680000` and `c0=(3/2)sqrt(2)<3`. If Delta<=1, (11) gives `zeta<4sqrt(Delta)`; if Delta>1 the resulting bound is trivial. Thus `Delta >=1/(1,310,720,000)^2`, proving (3).

## 5. Status and review targets

No numeric run, formal proof, independent review, novelty or parent acceptance is claimed. The exact 1D optimum/profile is explicitly conditional on pinned unreviewed cde9; the quantitative jump-deficit, full-D rectangle and gap are new WRITTEN deductions. Suggested disjoint review: nonnegative tail-slack decomposition, (9)'s band constants, rectangle telescoping (5), all-point density/Markov floor, and the concrete rational bound.
