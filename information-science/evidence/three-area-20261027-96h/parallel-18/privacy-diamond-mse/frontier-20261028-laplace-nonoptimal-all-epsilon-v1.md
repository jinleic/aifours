# A genuine full-law obstruction: product Laplace is never squared-optimal

**AUTHOR CANDIDATE — WRITTEN, with exact bivariate polynomial checks; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 20:58:04 PDT 2026`.

## 1. Exact original model and claim

Fix ANY finite epsilon>0, b=e^(-epsilon) in (0,1), and the original class of ALL Borel additive-noise laws satisfying pure epsilon privacy for EVERY Borel event and EVERY shift in the FULL CLOSED unit l1 diamond D. Let

    V_J(epsilon)=inf E|X|_2^2

be the actual original all-law squared-Euclidean infimum. The product-Laplace law

    Q(dx)=(epsilon^2/4)e^(-epsilon||x||_1)dx

is genuinely full-D private and has `J(Q)=4/epsilon^2`. The source-independent written result is

    V_J(epsilon) <= J(P_gammaJ) < 4/epsilon^2       for EVERY epsilon>0,  (1)

where P_gammaJ is an explicitly defined ACTUAL full-D-private diamond staircase and gammaJ is the unique larger positive root of the explicit quintic in §4. Thus product Laplace is NEVER an all-law squared-Euclidean optimizer at finite epsilon. The proof does not assume a density, symmetry, radiality or existence for the original candidate class; these properties are used only to build an actual feasible competitor.

The same independent argument also gives a strictly better actual law for the first-norm objective than product Laplace, but the optimizing offsets are not identified with each other. Equation (1) is an obstruction/counterexample to Laplace optimality, NOT a new exact all-law optimum, source-equivalence, novelty or priority claim.

## 2. Exact mixture of feasible staircases equals product Laplace

For gamma in [0,1], let

    n_gamma(x)=max(0,ceil(||x||_1-gamma)),
    P_gamma(dx)=b^n_gamma(x) dx/Z_gamma.

Each P_gamma is an actual original private law: any h in D changes `||x||_1` by at most 1, hence changes n_gamma by at most 1 in either direction. All events inherit the pointwise inequality. Let

    w(gamma)=epsilon e^(-epsilon gamma)/(1-b),
    pi(gamma)=(epsilon^2/4) w(gamma) Z_gamma.                            (2)

For r=n+u, n integer>=0, 0<=u<1, `n_gamma(r)=n+1` if gamma<u and n otherwise. Direct integration gives the EXACT identity

    integral_0^1 w(gamma)b^n_gamma(r) dgamma
       =b^n[b integral_0^u w + integral_u^1 w]
       =b^n e^(-epsilon u)=e^(-epsilon r).                               (3)

By Tonelli, pi is a probability density, strictly positive on (0,1), and

    Q = integral_0^1 P_gamma pi(gamma)dgamma                             (4)

as Borel laws. Therefore `J(Q)=integral J(P_gamma)pi`, and similarly for L. These are exact actual-law mixture identities, not a source citation or a radial-optimality assumption.

## 3. Exact staircase costs and strictness

Write `m=b/(1-b)` and

    D(gamma)=gamma^2+2m gamma+m+2m^2,
    M3=gamma^3+3m gamma^2+3(m+2m^2)gamma+m+6m^2+6m^3,
    M4=gamma^4+4m gamma^3+6(m+2m^2)gamma^2
        +4(m+6m^2+6m^3)gamma+m+14m^2+36m^3+24m^4.

The exact diamond layer-sum formula gives

    Z_gamma=2D(gamma),
    L(P_gamma)=2M3/(3D),       J(P_gamma)=M4/(3D).                       (5)

These functions extend continuously to [0,1], and P_0=P_1 as normalized laws. Direct differentiation gives

    J'(0)=2/[3(1+2m)]>0,       L'(0)=2/[3(1+2m)^2]>0.                  (6)

Thus each cost is NONCONSTANT on [0,1]. Since the mixing density pi in (2) is strictly positive and all costs are finite, the minimum of either continuous cost over gamma is STRICTLY below its pi-weighted mean. For J this is exactly the strict inequality in (1), because the mean is the true product-Laplace cost 4/epsilon^2. This proof applies to every finite epsilon without invoking a preexisting original-optimum theorem.

## 4. A deterministic exact J competitor

The derivative in (5) has sign equal to

    P_m(gamma)=gamma^5+5m gamma^4+(2m+12m^2)gamma^3
       +(12m^3-2m)gamma^2-m(1+2m)(1+6m)gamma+m^2(1+2m).                (7)

Its coefficient signs have exactly two variations for EVERY m>0, even if the gamma^2 coefficient vanishes. `P_m(0)=m^2(1+2m)>0` and `P_m(1)=(1+m)^2(1+2m)>0`. Since J'(0)>0 but J(0)=J(1), the mean-value theorem forces P_m<0 somewhere in (0,1). Descartes' rule then gives exactly two simple positive roots, both in (0,1); the larger root gammaJ is the UNIQUE global minimizer of the **staircase family**. Together with (4), it is a fully specified genuine counterexample in (1). We do NOT infer that it is the original all-law optimizer.

## 5. Exact rational finite-epsilon control at ln 2

At epsilon=ln 2, m=1, take the simple actual full-D-private staircase `gamma=18/25`. Exact Fraction arithmetic from (5) gives

    J(P_(18/25))=16085017/1936875.                                       (8)

The elementary positive series `ln 2=2 sum_(k>=0)3^(-(2k+1))/(2k+1)` and a geometric bound on its tail give

    ln 2 < U=189094979/272806380,
    4/U^2-16085017/1936875
       =1444156567325984337503/69256667153905847911875 >1/50.            (9)

Consequently this ONE explicitly specified original-law mechanism improves J by MORE THAN 1/50 against product Laplace at epsilon=ln 2. Equations (8)–(9) are exact rational inequalities, not Decimal/float comparisons. They do not identify the optimum or its novelty.

## 6. Actual checks, imports and limits

The Python eval kernel used exact `fractions.Fraction` sparse-polynomial arithmetic to check the FULL bivariate identities `(partial_gamma M4)D-M4(partial_gamma D)=2P_m` and `(partial_gamma M3)D-M3(partial_gamma D)=Q_m` coefficient-by-coefficient (11 and 6 nonzero monomials, respectively); this checks the derivative algebra for all symbolic m,gamma, not the variational argument. Fraction arithmetic also checked (8)–(9). Exploratory floating renderings of the ln 2 bounds were printed but not used as evidence; no external model or new literature source was used.

The mixture, full-D feasibility, strict all-law counterexample and root proof above are WRITTEN and require only elementary geometry, Tonelli, continuity, the mean-value theorem and Descartes' sign rule. No LAW642, v241, v253, MDA, PMLR, earlier unreviewed author theorem or review verdict is imported. Existing literature may already contain this obstruction; no novelty or priority clearance has been attempted. No formal proof, independent/human/cross-model review or parent adoption is claimed. Priority review should check (3)–(4), all-event privacy of P_gamma, the quintic signs and endpoints, and the exact ln 2 tail bound.
