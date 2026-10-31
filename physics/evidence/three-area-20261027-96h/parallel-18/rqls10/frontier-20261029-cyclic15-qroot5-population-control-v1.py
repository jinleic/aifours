#!/usr/bin/env python3
"""Exact Q(sqrt5) population control; not a vector realization."""
import datetime,hashlib,json
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent
z=(F(0),F(0));o=(F(1),F(0))
def add(x,y):return(x[0]+y[0],x[1]+y[1])
def neg(x):return(-x[0],-x[1])
def mul(x,y):return(x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
# eta=zeta15^3 satisfies eta²=((sqrt5-1)/2)eta-1.
c=(F(-1,2),F(1,2));eta=[(o,z)]
for _ in range(4):
 a,b=eta[-1];eta.append((neg(b),add(a,mul(c,b))))
omega=[(o,z),(z,o),(neg(o),neg(o))]
def root15(a):
 a0,a1=omega[(2*a)%3];b0,b1=eta[(2*a)%5]
 return(mul(a0,b0),mul(a1,b0),mul(a0,b1),mul(a1,b1))
X=(F(-1,3),F(1,3));Y=(F(1),F(-1,3));ex=(0,1,2,4,5,12);q=(X,X,Y,Y,X,Y)
assert add(X,Y)==(F(2,3),F(0)) and Y==mul(c,X)
co=[z,z,z,z]
for a,v in zip(ex,q):co=[add(x,mul(v,y))for x,y in zip(co,root15((-2*a)%15))]
assert all(x==z for x in co)
for r in range(3):
 vals=[q[i]for i,a in enumerate(ex)if a%3==r];assert len(vals)==2 and add(*vals)==(F(2,3),F(0))
# 2<sqrt5<5/2 proves 1/3<X<1/2 and 1/6<Y<1/3.
assert 2*2<5 and 5<F(5,2)**2
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'spectrum_exponents':ex,'q_coefficients_in_Qsqrt5':[[str(a),str(b)]for a,b in q],
 'paired_moment_zeta_minus2_coefficients_in_1_omega_eta_omegaeta':[[str(a),str(b)]for a,b in co],
 'each_U5_class_q_sum':'2/3','p2_equals_p7_equals_q_over_2':True,'p5_equals_half_minus_q':True,
 'scope':'exact nonnegative moment relaxation, not an orthogonal ray realization','status':'PASS'}
(P/'frontier-20261029-cyclic15-qroot5-population-control-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
