# Critical 8/9 counterpoint passes all JLL tests after every nonnegative-polynomial transform

**EXACT NECESSARY-TEST COUNTERPOINT; not an actual Metzler or PH witness.** MathResearch96h-2. This strengthens the explicit spectral point and forced shift of `frontier-20261028-ph7-jll-sharp-shift-limit-v1.md`. No claim is made about tests outside the stated polynomial-moment family, or that the point is realizable.

## The result

For the hypothetical critical spectrum `0,-3,-5,-1 +/- i sqrt(8/9)` each complex eigenvalue twice, any Metzler realization would have entrywise nonnegative

    N=G+(31/6)I,

as the preceding exact trace-square/Cauchy argument establishes. Let

    mu=(31/6,13/6,1/6,25/6 +/- i sqrt(8/9) each twice),
    s_j=sum_{mu} mu^j,  j>=0.

For EVERY real polynomial `f(x)=sum_j c_j x^j` with finitely many coefficients `c_j>=0`, write `S_k(f)=sum_mu f(mu)^k`. We prove EXACTLY

    S_k(f)>=0 and S_k(f)^m <= 7^(m-1) S_(km)(f)
    for every integers k>=1,m>=2.                            (POLY-JLL)

If N were nonnegative, f(N) would be nonnegative, so(POLY-JLL) is a genuine infinite family of necessary nonnegative-matrix tests. This result shows that no finite or infinite combination of those tests can, by itself, exclude this spectral point. Even a polynomial transform is only a derived necessary test; passing them does not construct N.

## 1. A stronger mixed power-sum inequality

The exact statement underlying(POLY-JLL) is

    7 s_(a+b) >= s_a s_b for ALL integers a,b>=0,            (PAIR)

strict when a,b>0 and equality when either is0. The equality follows from `s0=7`. All s_j are positive: s0=7 and the remaining s_j are checked/proved below.

For any indices j1,...,jm>=0, repeated application of(PAIR) yields

    product_(i=1)^m s_(j_i) <= 7^(m-1) s_(sum_i j_i).

Expanding `(sum_j c_j s_j)^m` and summing this coefficientwise inequality with nonnegative products `c_(j1)...c_(jm)` gives

    (sum_j c_j s_j)^m <= 7^(m-1) sum_mu f(mu)^m.

To get the general k in(POLY-JLL), apply this to the polynomial `g=f^k`, whose coefficients remain nonnegative. Positivity follows because each S_k is a nonnegative-coefficient sum of the positive s_j. No matrix realization or diagonalizability is used in this purely spectral implication.

## 2. Exact proof of every mixed inequality

Let `R=83/100`, and write

    A_j=1+(13/31)^j+(1/31)^j+4 R^j,
    B_j=1-4 R^j.

Because `|25/6+i sqrt(8/9)|/(31/6)=sqrt(657)/31<R`, exact complex-modulus bounds give

    B_j <= s_j/(31/6)^j <= A_j.                             (BOUND)

The rational checker verifies `B10>0`,

    A10^2 < 7 B20,         A1 A20 < 7 B21.                  (TAIL)

If a,b>=10, the left side of(PAIR), normalized by `(31/6)^(a+b)`, exceeds `7 B20`, while the right is at most `A10^2`. If one index is at most9 and the other at least20, compare `7 B21` against `A1 A20`. Thus both infinite regions satisfy(PAIR) strictly. The remaining finite cases are exactly `1<=a<=9`, `1<=b<=19`, with indices interchangeable; 171 rational pairs are checked by the recurrence

    C0=1, D0=0,
    C_(j+1)=(25/6)C_j-(8/9)D_j,  D_(j+1)=C_j+(25/6)D_j,
    s_j=(31/6)^j+(13/6)^j+(1/6)^j+4 C_j.

The checker separately verifies `s1,...,s9>0`; (BOUND) with B10>0 gives all larger positive s_j. No unbounded case is left to numerical extrapolation.

## 3. Actual verification and scope

Actual invocation:

    python3 frontier-20261028-ph7-all-polynomial-moments-check.py
    Exact Fraction PASS: all polynomial-transform JLL orders, finite mixed pairs 171

Checker `frontier-20261028-ph7-all-polynomial-moments-check.py`, **32LF/1360B**, SHA256 `c252716fd876de79ab45b19f36b29811fe3bbdf61d5360f2bb915c67cff4631c`; certificate `frontier-20261028-ph7-all-polynomial-moments-certificate.json`, **9LF/370B**, SHA256 `5739a4383eec20330146d0c78d6be67202c989746cdd741959a466ba9f4b906e`. All arithmetic is exact standard-library Fraction. The checker verifies the 171 finite mixed comparisons and rational tail constants, not an actual matrix, all possible spectral inequalities, the transfer numerator, or a formal proof.

The same spectral point passes all normalized M-matrix Newton inequalities and centered trace2/3, with public-source qualification in the companion `frontier-20261028-ph7-newton-trace-obstruction-limit-v1.md`. The all-polynomial conclusion is derived independently of Holtz. It does not imply spectral realizability: new inverse-eigenvalue constraints, sign structure, the Jordan chains or actual PH input/output may still fail. No 8/9 existence/exclusion, PH8 minimum, novelty, independent review, or historical process repair is claimed.

END — ALL polynomial-transform JLL moment tests at a trace-square-forced shift remain compatible with the critical hypothetical spectrum.
