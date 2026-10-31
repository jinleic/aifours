# Critical 8/9 counterpoint survives ALL JLL inequalities even at a much sharper forced shift

**EXACT WRITTEN + FRACTION CHECKED; no actual nonnegative or PH realization asserted.** MathResearch96h-2. This strengthens `frontier-20261028-ph7-jll-all-orders-limit-v1.md` SHA256 `b58ced952217d3d0cf559cafbe331f39c192b316a0e4ad76535263eb8ab5cd75`; it keeps that file's explicit hypothetical spectral tuple and its scope, and does not modify it.

## 1. Every Metzler realization of the tuple would permit this smaller nonnegative shift

For the hypothetical spectrum

    0, -3, -5, -1 +/- i sqrt(8/9) each twice,

one has `tr G=-12` and `tr G^2=310/9`. If a Metzler G has spectral bound0, all its diagonal entries are nonpositive: shifting G to a nonnegative matrix and using Perron monotonicity gives `G_ii<=s(G)=0`. Put `r_i=-G_ii>=0`. Then

    sum_i r_i=12,        sum_i r_i^2 <= tr G^2=310/9,

because all off-diagonal products in the trace-square are nonnegative. For `r=max_i r_i`, Cauchy on the other six gives

    r^2+(12-r)^2/6 <=310/9.                          (DIAG)

Here `r>=12/7`, and the left side is strictly increasing for r>=12/7. At the rational test point

    (31/6)^2+(12-31/6)^2/6 - 310/9 = 7/216 >0.

Therefore `r<31/6`. Consequently the much smaller matrix shift

    N=G+(31/6)I

would also be entrywise nonnegative for ANY such Metzler realization. Its spectrum would be

    31/6, 13/6, 1/6, 25/6 +/- i sqrt(8/9) each twice.     (Nsharp)

This condition is stricter than applying JLL only at +12, but the hypothetical spectrum still passes ALL those tests strictly.

## 2. Exact all-orders result

Define `s_k` as the spectral power sum of(Nsharp). Then

    s_k>0 and s_k^m < 7^(m-1) s_(km)

for ALL integers k>=1 and m>=2. The JLL necessity for any actual nonnegative matrix is derived directly from nonnegative powers, diagonal walks and Jensen in §2 of the preceding all-orders file.

Use the exact recurrence

    C0=1, D0=0,
    C_(k+1)=(25/6) C_k-(8/9) D_k,
    D_(k+1)=C_k+(25/6) D_k,
    s_k=(31/6)^k+(13/6)^k+(1/6)^k+4 C_k.

The complex modulus ratio is `sqrt(657)/31 < R=83/100`. Put

    A10=1+(13/31)^10+(1/31)^10+4R^10,
    A1=1+13/31+1/31+4R,
    B20=1-4R^20.

The checker establishes the exact rational inequalities

    1-4R^10>0, B20>0, A10<7, A1<7,
    A10^2<7B20, 7(A1/7)^20<B20.

For k>=10 and m>=2, `(km)>=20`, and the normalized lower/upper bounds imply JLL because `7(A10/7)^m<=A10^2/7<B20`. For 1<=k<=9 and m>=20, use `7(A1/7)^m<=7(A1/7)^20<B20`. The remaining 162 pairs `1<=k<=9, 2<=m<=19` and positive s_k for k=1,...,9 are checked directly using exact rational arithmetic; k>=10 positivity follows from the first tail bound. Thus every integer pair is covered, without any floating limit or finite-cutoff extrapolation.

## 3. Actual verification and limitations

Actual run:

    python3 frontier-20261028-ph7-jll-sharp-shift-check.py
    Exact Fraction PASS: shift31/6 forced, all power sums and all JLL inequalities; finite pairs 162

Checker `frontier-20261028-ph7-jll-sharp-shift-check.py`, **28LF/1259B**, SHA256 `f443670f7332d8d03c36078c260864b6e1ae73c6fdd23629f694f7c8e9ca436d`. Certificate `frontier-20261028-ph7-jll-sharp-shift-certificate.json`, **8LF/350B**, SHA256 `563829b2897245e2ed68c29c7fa2bcc67dbcbdbb099c5e38999a11c1901e2b43`. The checker verifies the rational shift margin, finite moments and tail predicates, not the existence of G.

The same hypothetical spectrum also strictly satisfies all six normalized Newton inequalities under Holtz's explicitly cited public M-matrix theorem and the centered trace-two/three comparison, as checked in `frontier-20261028-ph7-newton-trace-obstruction-limit-v1.md`. This joint point shows that these necessary tests, even with the much sharper universally forced shift, cannot ALONE exclude the original 8/9 problem. Other nonnegative inverse-eigenvalue constraints, actual matrix structure, and positive PH input/exit may rule it out; no such ruling or realization is claimed. Independent review and novelty status remain open.

END — all JLL orders pass even after diagonal trace-square forces the shift below 31/6.
