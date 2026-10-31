#!/usr/bin/env python3
"""Exact finite checks for the all-nontrivial-noise abstract obstruction."""
from fractions import Fraction as F
import json


def multiply(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


def product(roots):
    value=[F(1)]
    for root in roots:value=multiply(value,[root,F(1)])
    return value


def main():
    rows=[]
    for t in (F(1,1000),F(1,200),F(1,3),F(9,10),F(999,1000)):
        a,b=(1+t)/2,(1-t)/2
        A,Q,R=a**4,a**3*b,a*a*b*b
        eps=(Q-R)/10
        y=[A]+[Q]*4+[R]*6+[a*b**3]*4+[b**4]
        x=[A-3*eps]+[Q+2*eps]*2+[Q-eps]*2+[R+eps]+[R]*5+[a*b**3]*4+[b**4]
        assert sum(x)==sum(y)==1 and all(x[i]>=x[i+1] and y[i]>=y[i+1] for i in range(15))
        differences=[sum(x[:k])-sum(y[:k]) for k in range(1,17)]
        assert differences==[-3*eps,-eps,eps,0,-eps]+[0]*11
        for s in (F(0),eps):
            assert A-3*s>=Q+2*s>=Q-s>=R+s>0
            assert Q-R>=5*s and 3*(A-Q)>=18*s and 3*A-2*Q-R>=20*s
        altered_x=[A-3*eps]+[Q+2*eps]*2+[Q-eps]*2+[R+eps]
        altered_y=[A]+[Q]*4+[R]
        delta=[v-w for v,w in zip(product(altered_x),product(altered_y))]
        assert all(z>=0 for z in delta) and delta[0]>0
        rows.append({'t':str(t),'epsilon':str(eps),'strict_k3_excess':str(differences[2]),
                     'other_prefixes_nonpositive':True,'positive_logdet_difference_coefficients':True,
                     'all_power_endpoint_conditions':True})
    print(json.dumps({'scope':'five exact abstract spectra, not physical outputs or a substitute for the written all-t proof',
                      'rows':rows},indent=2,sort_keys=True))


if __name__=='__main__':main()
