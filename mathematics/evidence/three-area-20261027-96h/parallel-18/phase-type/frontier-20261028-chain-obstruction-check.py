#!/usr/bin/env python3
"""Exact coefficient and Bernstein certificate for one PH7 chain family.

Verifies formal polynomial identities over Q, coefficientwise Bernstein signs
on closed rational intervals, and positive shifted-power coefficients on the
remaining ray. This certifies a family-specific obstruction only; it is not an
unrestricted PH7 result. All calculations use fractions.Fraction.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

OUT=Path(__file__).resolve().parent/'frontier-20261028-chain-obstruction-certificate.json'

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def add(a,b):
    return trim([(a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0)) for i in range(max(len(a),len(b)))])
def sub(a,b): return add(a,[-x for x in b])
def scale(a,s): return trim([x*s for x in a])
def mul(a,b):
    p=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): p[i+j]+=x*y
    return trim(p)
def const(x): return [F(x)]

def shift(p,a):
    return [sum(p[i]*comb(i,j)*a**(i-j) for i in range(j,len(p))) for j in range(len(p))]

def bernstein(p,lo,hi):
    n=len(p)-1; w=hi-lo
    power=[sum(p[i]*comb(i,j)*lo**(i-j)*w**j for i in range(j,n+1)) for j in range(n+1)]
    return [sum(power[j]*F(comb(k,j),comb(n,j)) for j in range(k+1)) for k in range(n+1)]

u=[F(0),F(1)]; one=const(1); u2=mul(u,u); u3=mul(u2,u); z=F(8,9)
a=add(scale(u,3),const(3)); b=add(add(scale(u2,3),scale(u,9)),const(3))
c3=add(add(add(u3,scale(u2,9)),scale(u,9)),one)
e4=add(add(scale(u3,3),scale(u2,9)),scale(u,3))
h0=sub(add(b,scale(a,4)),add(mul(a,a),const(6)))
L=add(sub(b,scale(a,4)),const(10-2*z))
N=add(sub(sub(scale(h0,4),c3),mul(b,sub(const(4),a))),const(4-4*z))
qnum=add(mul(sub(a,const(4)),N),mul(sub(h0,const(2*z)),L))
wnum=add(N,mul(sub(const(4),a),L))
phinum=sub(add(mul(e4,L),mul(c3,wnum)),add(add(scale(qnum,6+2*z),scale(N,4+4*z)),scale(L,(1+z)**2)))
P=[F(3184),F(-7776),F(9360),F(-5859),F(2025),F(-729),F(243)]
Q=[F(400,81),F(-32,3),F(25,3),F(-8),F(6)]
assert L==[F(-7,9),F(-3),F(3)]
assert N==[F(-32,9),F(3),F(-9),F(8)]
assert qnum==Q
assert scale(phinum,-243)==P
assert N==add(mul([F(-1,3),F(8,3)],L),[F(-103,27),F(110,27)])
intervals_P=[(F(0),F(1,2)),(F(1,2),F(1)),(F(1),F(3,2)),(F(3,2),F(2))]
intervals_Q=[(F(0),F(1,2)),(F(1,2),F(3,4)),(F(3,4),F(1))]
Pcert={f'{lo}:{hi}':bernstein(P,lo,hi) for lo,hi in intervals_P}
Qcert={f'{lo}:{hi}':bernstein(Q,lo,hi) for lo,hi in intervals_Q}
Ptail=shift(P,F(2)); Qtail=shift(Q,F(1))
assert all(x>0 for cs in Pcert.values() for x in cs)
assert all(x>0 for cs in Qcert.values() for x in cs)
assert all(x>0 for x in Ptail+Qtail)
report={
 'target':'z=8/9, u>0, exact fixed 3+3 chain family, positive diagonal normalization',
 'identities':{'L':[str(x) for x in L],'N':[str(x) for x in N],'q_times_L':[str(x) for x in Q],
               '-243_L_phi':[str(x) for x in P],'N_division_remainder':'(110u-103)/27'},
 'positive_bernstein_coefficients_P':{k:[str(x) for x in v] for k,v in Pcert.items()},
 'positive_bernstein_coefficients_Q':{k:[str(x) for x in v] for k,v in Qcert.items()},
 'positive_shift_coefficients_P_at_u_2':[str(x) for x in Ptail],
 'positive_shift_coefficients_Q_at_u_1':[str(x) for x in Qtail],
 'result':'P(u)>0 and qL(u)>0 for every u>=0. Feasible nonnegative initial coefficients B,C require q=u^2+uB+C>0, hence L>0; then phi=-P/(243L)<0. The L=0 coefficient equations have no solution. Only this chain/normalization family is excluded.',
 'verification':'Python Fraction exact coefficient identities and Bernstein/shift coefficient sign assertions; no numerical roots, floating-point checks, or external solver.'}
OUT.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2)); print('saved:',OUT)
