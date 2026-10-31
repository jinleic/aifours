# Exact one-dimensional mixed optimum as a two-dimensional lower bound

**AUTHOR CANDIDATE — WRITTEN with exact rational checks and explicitly nonrigorous decimals; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 19:53:09 PDT 2026`.

## 1. Exact all-law claim

Fix epsilon>0, `b=e^(-epsilon)`, `m=b/(1-b)` and kappa>=0. Let V_1,kappa be the infimum of `E[Y^2+kappa|Y|]` over ALL Borel laws Y satisfying the ONE-DIMENSIONAL all-event epsilon privacy condition for EVERY shift |h|<=1. Define gamma in (0,1) as the UNIQUE root of

    P(gamma)=gamma^3+(3m+3kappa/4)gamma^2
              +(3m^2+3kappa m/2)gamma
              -(3m^2/2+3kappa m/4+m/2)=0.                               (1)

Then the source-independent written theorem is the EXACT finite-epsilon one-dimensional optimum

    V_1,kappa=2m^2+m+kappa m+(2m+kappa)gamma+gamma^2,                   (2)

attained by the symmetric 1D staircase density proportional to `b^(max(0,ceil(|y|-gamma)))`.

For the ORIGINAL two-dimensional full-l1-diamond class, each coordinate marginal is 1D private; therefore EVERY actual law satisfies

    J+kappa L >= 2 V_1,kappa.                                           (3)

This is a valid original all-law lower bound, not a claim that two 1D-optimal staircases can be combined into a 2D full-D-private law or that equality in (3) holds.

At kappa=0, gamma and the lower bound are explicit:

    gamma=[m^3+(3m^2+m)/2]^(1/3)-m,
    J >= 2[m^2+m+(m^3+(3m^2+m)/2)^(2/3)].                              (4)

For the pure first norm the same proof gives `inf_1D E|Y|=sqrt[m(m+1)]`, hence the 2D lower bound

    L >= 2sqrt[m(m+1)] = 1/sinh(epsilon/2).                              (5)

No LAW642, MDA, PMLR, one-dimensional optimality theorem or previous research candidate is imported. The proof below derives (1)–(5) directly.

## 2. Reduction of a general private law to a bounded-ratio fractional profile

Any 1D private Borel law has a bounded all-point density representative, by integrating privacy over shifts in [-1,1] and taking ball-average limsups. Symmetrize p to `(p(y)+p(-y))/2`; privacy and the even cost are unchanged.

For x in (0,1), put `p_n(x)=p(n+x)` for n>=0 and `S(x)=sum_(n>=0)p_n(x)`. Privacy along integer shifts gives `p_(n+k)(x)>=b^k p_n(x)`. Thus the normalized weights p_n/S have tail at least b^k, so their integer variable N obeys

    E[N|x]>=m,       E[N^2|x]>=m+2m^2.                                   (6)

The function `g(x)=2S(x)` integrates to 1. Because |x-y|<=1, the same privacy condition gives `g(x)<=b^(-1)g(y)` for all x,y in (0,1). Hence, with `a=essinf g`, `a<=g<=a/b` a.e. and a>0. For kappa>=0, (6) yields

    E[Y^2+kappa|Y|] >=2m^2+m+kappa m
                         +integral_0^1[(2m+kappa)x+x^2]g(x)dx.           (7)

No independence between N and x is assumed.

## 3. Exact fractional minimization and attaining law

The cost `c(x)=(2m+kappa)x+x^2` is strictly increasing. For any gamma, the normalized two-level profile

    g_gamma=[1_(0,gamma)+b 1_(gamma,1)]/[b+(1-b)gamma]                 (8)

has fractional expectation `N(gamma)/(m+gamma)`, with

    N(gamma)=(2m+kappa)(m+gamma^2)/2+(m+gamma^3)/3.                     (9)

Its derivative numerator is `(2/3)P(gamma)` with P in (1). P is strictly increasing on [0,1], with P(0)<0 and P(1)>0, so it has exactly one root gamma*. At this root, the expected cost equals `c(gamma*)`.

This is a GLOBAL lower bound over ALL admissible g, not just a two-level ansatz: for any g in [a,a/b], pointwise minimization of `(c-c(gamma*))g` uses g=a/b below gamma* and g=a above it. Since (8)'s threshold is stationary, the resulting weighted integral is 0. Hence `integral c g>=c(gamma*)`. Substituting in (7) gives (2).

The displayed symmetric staircase has shell indices differing by at most one under any |h|<=1; it is actual all-event private. Its fractional profile is exactly (8), and its p_n satisfy `p_(n+k)=b^k p_n`, so every inequality above is an equality. Therefore (2) is an exact 1D optimum, not merely a lower bound.

For kappa=0, (1) becomes `(gamma+m)^3=m^3+(3m^2+m)/2`, giving (4). For cost |Y| alone, replace c(x) by x; the stationary equation is `gamma^2+2m gamma-m=0`, so gamma=`sqrt[m(m+1)]-m` and the exact optimum is `m+gamma=sqrt[m(m+1)]`. This proves (5).

## 4. High-privacy precision and a concrete original-model bracket

As epsilon->0, expansion of the exact 1D bound gives

    2 V_1,0 =4/epsilon^2 -1/6 +epsilon^2/360+O(epsilon^3),
    2 inf_1D E|Y|=2/epsilon-epsilon/12+7epsilon^3/2880+O(epsilon^5).   (10)

Thus the first line improves the earlier elementary coordinate-tail lower bound from a deficit of order 1/epsilon to a deficit of order 1, while keeping the exact leading 4/epsilon^2. Optional conditional comparison: the separately pinned parent-v253/author series candidate `frontier-20261028-high-privacy-sharp-value-series-v1.md`, SHA-256 `f59f37a4848b27d98442fae91270a5b482592074e8654d4b6b948f0045214ef2`, would give an actual 2D optimum minus this 1D relaxation equal to `1/6-(sqrt(3)/54)epsilon+O(epsilon^3)`. That comparison is conditional on the unreviewed series and is not used to prove (1)–(10).

At epsilon=ln 2, m=1, (4) gives `J>=4+2*3^(2/3)`. The actual 2D full-D-private diamond staircase with gamma=18/25 has exact J=`16085017/1936875`; hence

    4+2*3^(2/3) <= V_J(ln 2) <= 16085017/1936875.                      (11)

A Fraction check gives `(16085017/1936875-4)^3-72 = 56412430585587992413/7266157055419921875>0`, so the displayed endpoints are rigorously ordered. Decimal approximations are 8.1601676461 and 8.3046231688; they are illustrative, not required for the ordering proof.

## 5. Actual checks and limitations

The Python eval kernel used `fractions.Fraction` to check the cubic derivative identity for three rational `(m,kappa,gamma)` samples and to derive the exact trial J and endpoint ordering above. Separate high-precision Decimal point evaluations suggested the epsilon->0 expansion; they are not interval enclosures. The all-law 1D optimization, feasibility, 2D relaxation and series are WRITTEN, not machine-verified or independently reviewed. No novelty, exact 2D optimizer, source-equivalence, formal proof or parent acceptance is claimed. Disjoint review should examine (6), the ratio-profile global minimum, endpoint/step privacy and the high-privacy expansion.
