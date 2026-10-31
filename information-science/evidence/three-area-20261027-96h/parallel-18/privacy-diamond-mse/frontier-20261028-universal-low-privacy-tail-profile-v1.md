# Universal macroscopic privacy-tail profile at low privacy

**AUTHOR CANDIDATE — WRITTEN with exact rational normalization checks; NOT independently reviewed or parent-adopted.** Native pre-write clock: `Wed Oct 28 18:48:29 PDT 2026`.

## 1. Exact all-law statement

Fix finite `lambda>=0` and define `c(x)=||x||_2^2+lambda||x||_1^2`. For each b=e^(-epsilon) in (0,1), let F_b contain EVERY Borel law satisfying epsilon privacy for EVERY Borel event and EVERY shift in the FULL CLOSED l1 unit diamond D. Put

    A=|{c<=1}|,    C_D=integral_D c(x)dx=2/3+lambda,
    C=sqrt(2C_D/A),    y0=1/sqrt(2 A C_D)=1/(A C).

Let ANY sequence b_n->0 and ANY feasible laws mu_n satisfy the first-order near-optimal condition

    E_mu_n c(X) <= C sqrt(b_n)+o(sqrt(b_n)).                              (1)

My preceding UNREVIEWED peak-floor theorem `frontier-20261028-peak-floor-low-privacy-universal-v1.md`, SHA `d44029e458b8af871d2d849e2a5159e1885e99402d615a88eabe39d89ab4ad43`, derives this leading value and the decomposition facts recalled below WITHOUT LAW642/MDA/v241/PMLR/f68 or an optimizer ansatz. This successor is conditional on that still-unreviewed author proof; the listed claims are NOT automatically parent-adopted.

For any density p_n of mu_n and EVERY fixed r>0, the candidate new strong tail-profile limit is

    integral_(|x|_2>r) | p_n(x)/sqrt(b_n) - y0 1_D(x) | dx ->0.        (2)

The complete cost measures also converge weakly as FINITE measures:

    [c(x)/sqrt(b_n)] mu_n(dx)
       => (C/2) delta_0 + y0 c(x)1_D(x) dx.                             (3)

The atom has mass C/2, and the absolutely continuous part has exactly the same mass because y0 C_D=C/2. This identifies the universal fixed-scale privacy tail and the origin-concentrated core contribution, not merely total cost or weak scaled-law convergence.

For the ORIGINAL Euclidean objective lambda=0, `y0=sqrt(3)/(2sqrt(pi))`, `C=2/sqrt(3pi)`. In particular, for EVERY fixed `0<r<1/sqrt(2)`,

    mu_n(|X|_2>r)/sqrt(b_n)
       -> [sqrt(3)/(2sqrt(pi))] (2-pi r^2),                             (4)
    E[|X|_2^2 1_{|X|_2>r}]/sqrt(b_n)
       -> [sqrt(3)/(2sqrt(pi))] (2/3-(pi/2)r^4).                       (5)

Thus any actual first-order-near-optimal law, regardless of whether it is an optimizer or has a geometric shell form, must saturate the same macroscopic unit-diamond floor to leading order. No source-priority, nonadditive-channel, endpoint-epsilon or formal/human acceptance is claimed.

## 2. Exact shared peak-floor decomposition

Write `s_n=b_n^(1/4)`, and let p_n be the bounded all-point privacy representative of mu_n. Let M_n=esssup p_n; choose an actual x_n with `p_n(x_n)>=(1-s_n)M_n`. Full closed-D privacy gives a floor

    ell_n=b_n(1-s_n)M_n  on  x_n+D.

Define nonnegative g_n by `p_n=ell_n 1_(x_n+D)+g_n`, and rescale

    y_n=s_n^2 M_n,    g_n^#(z)=s_n^2 g_n(s_n z),
    h_n=integral g_n^#=1-2ell_n,
    T_n=h_n/(A y_n),    g_n^0=y_n 1_{c(z)<=T_n}.

The predecessor proves, using only actual all-event DP, the peak cap, an even-convex translated-floor lower bound and the strict cost-sublevel bathtub identity,

    y_n->y0,       x_n->0,       ell_n/s_n^2->y0,
    T_n->C,        Delta_n:=integral(c-T_n)(g_n^#-g_n^0)->0.           (6)

The integrand in Delta_n is pointwise nonnegative because `g_n^#<=y_n` and the two g densities have equal mass. The finite-cost equality also gives

    integral c(z) g_n^#(z) dz = h_n^2/(2 A y_n)+Delta_n -> C/2.         (7)

All definitions are for the actual law, not a guessed limit of its optimizer core. The peak x_n need not be attained or satisfy x_n/s_n->0.

## 3. L1 tail-density convergence away from the origin

Fix ANY r>0. For large n, `r^2/s_n^2>T_n`. On `|z|_2>r/s_n`, the bathtub comparison density g_n^0 is zero and `c(z)>=|z|_2^2`. Equation (6) implies

    integral_(|z|>r/s_n) g_n^#(z) dz
       <= Delta_n/[r^2/s_n^2-T_n].                                       (8)

Change variables back and divide by `sqrt(b_n)=s_n^2`:

    (1/s_n^2) integral_(|x|>r) g_n(x)dx
       <= Delta_n/[r^2-s_n^2 T_n] ->0.                                  (9)

The floor coefficient `ell_n/s_n^2->y0`, and translation continuity of the bounded measurable D indicator gives `1_(x_n+D)->1_D` in L1 since x_n->0. Combining this with (9) proves the STRONG L1 statement (2), including unbounded outer regions. It holds for arbitrary Borel subsets of `{|x|>r}` by domination, not only for continuity sets.

## 4. Separate the two limiting cost measures

On the same far region, the nonnegative deficit also gives

    integral_(|x|>r) [c(x)/s_n^2] g_n(x)dx
      = integral_(|z|>r/s_n)c(z)g_n^#(z)dz
      <= Delta_n + T_n integral_(|z|>r/s_n)g_n^#(z)dz ->0.              (10)

Together with total g cost (7), (10) says the finite measures `c(x)g_n(x)dx/s_n^2` have total mass ->C/2 and concentrate at x=0. Hence they converge weakly to `(C/2)delta_0`.

For the floor component, compactness of D, x_n->0, ell_n/s_n^2->y0, and continuity of c give weak convergence

    [c(x)/s_n^2] ell_n 1_(x_n+D)(x)dx
       => y0 c(x)1_D(x)dx.

The two identities prove (3). In particular `y0 C_D=C/2`; the privacy floor carries EXACTLY half of the leading cost, although its probability mass is only O(sqrt b). This is the mathematical reason the rescaled law can converge in TV yet fail W2 convergence.

## 5. Original squared-Euclidean specialization

For lambda=0, c(x)=|x|_2^2, A=pi and C_D=2/3, so

    y0=sqrt(3)/(2sqrt(pi)),     C=2/sqrt(3pi).

If `0<r<1/sqrt(2)`, the Euclidean disk B_2(0,r) lies entirely in D. Therefore

    |D minus B_2(0,r)|=2-pi r^2,
    integral_(D minus B_2(0,r)) |x|_2^2 dx=2/3-(pi/2)r^4.

Apply (2) and (10) to the complement to obtain (4)–(5). No precise finite-b equality, threshold, center symmetry, uniqueness or named-publication theorem is used.

## 6. Actual exact arithmetic and review scope

A bounded `fractions.Fraction` check printed

```text
lambda=0: pi*y0^2= 3/4 pi*(y0*C_D)^2= 1/3 pi*(2*y0)^2= 3
core/tail equal scaled cost fractions= 1/2 1/2
```

This verifies elementary coefficient algebra, not the all-law DP/bathtub proof. The crucial source-independent predecessor remains UNREVIEWED and must be included in any review of this tail theorem. Request disjoint review of the weighted L1 tail estimate (8)–(10), translated floor convergence and cost-measure weak limit. No LAW642, v241, MDA, PMLR or held result is a research premise, and no formal/kernel/human/configured-family, novelty or parent acceptance is claimed.
