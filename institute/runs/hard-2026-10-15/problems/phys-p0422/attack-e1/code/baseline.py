"""Exact audit of the classical single-flip upper-bound equation.

Original citations and its tabulated two-decimal benchmarks are present in
the supplied Achlioptas--Peres reader. The primary original papers were not
staged. notes/BASELINE.md independently derives this criterion for the
contract's distinct-variable model. This script brackets its positive roots.
"""
from fractions import Fraction as F


GRID = 1 << 300


def ceil_div(a, b):
    return -((-a)//b)


def exp_neg(x):
    assert x >= 0
    t = x / 64
    # Positive Taylor with exact rational arithmetic; t is small here.
    term, lower = F(1), F(1)
    for j in range(1, 100):
        term = term*t/j
        lower += term
    nxt = term*t/100
    upper = lower + nxt/(1-t/101)
    lo = F(1,1)/upper
    hi = F(1,1)/lower
    # Keep rational denominators bounded through the six squares.
    low = lo.numerator * GRID // lo.denominator
    high = ceil_div(hi.numerator * GRID, hi.denominator)
    for _ in range(6):
        low, high = low*low//GRID, ceil_div(high*high, GRID)
    return F(low,GRID), F(high,GRID)


def neglog(z):
    assert 0 <= z < 1
    term, lower = z, F(0)
    for j in range(1, 240):
        lower += term/j
        term *= z
        # Round each exact term's contribution? Not needed: the input is
        # dyadic and at most 1/2, with only 239 summands.
    return lower, lower+term/(240*(1-z))


def g_interval(k, a):
    # g(a)=a log(1-2^-k)+log 2+log(1-exp(-ka/(2^k-1))/2).
    A0,A1 = neglog(F(1,2**k))
    L0,L1 = neglog(F(1,2))
    e0,e1 = exp_neg(k*a/(2**k-1))
    N0,_ = neglog(e0/2)
    _,N1 = neglog(e1/2)
    return -a*A1+L0-N1, -a*A0+L1-N0


def main():
    # First display decimal reconnaissance only after exact signs are checked.
    # Endpoints below need not be the tightest intervals.
    brackets = [(4,F(1022,100),F(1023,100)),
                (5,F(2132,100),F(2133,100))]
    for k,low,high in brackets:
        lo0,lo1 = g_interval(k,low)
        hi0,hi1 = g_interval(k,high)
        assert lo0 > 0, f'lower bracket for k={k} is not below the positive root'
        assert hi1 < 0, f'upper bracket for k={k} is not an UNSAT criterion'
        print(f'PASS baseline k={k}: g({low})>0, g({high})<0, positive root lies in ({low},{high})')
    print('Original primary texts absent: this is a self-contained reconstruction, not a current literature/novelty check.')


if __name__=='__main__':
    main()
