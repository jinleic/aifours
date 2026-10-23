"""Exact displayed constants in the ensemble-transfer/concentration theorem."""
from fractions import Fraction as F
import json
from math import comb
from pathlib import Path


def ceiling(x):
    return -((-x.numerator)//x.denominator)


trials=json.loads(Path('certificates/trials.json').read_text())['trials']
for t in trials:
    if t['name'] not in ('k4','k5'):
        continue
    k,alpha,epsilon,y=t['k'],F(t['alpha']),F(t['epsilon']),t['y']
    c0=epsilon/(2*y)
    c=c0/2
    count_cutoff=16*alpha/c0**2
    replacement_cutoff=4*(1+alpha*comb(k,2))/c0
    n0=ceiling(max(F(k),count_cutoff,replacement_cutoff))
    exponent=2*c*c/alpha
    target=F(1023,100) if k==4 else F(2133,100)
    assert alpha<target
    assert F(n0)>=count_cutoff and F(n0)>=replacement_cutoff
    print(f'k={k}, alpha={alpha}, epsilon={epsilon}, y={y}, c0={c0}, c={c}, N0={n0}')
    print(f'For every integer n>=N0: P[SAT] <= exp(-({exponent}) n).')
