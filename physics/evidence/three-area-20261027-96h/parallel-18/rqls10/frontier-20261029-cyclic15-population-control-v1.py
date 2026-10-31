#!/usr/bin/env python3
"""Rational interval positivity for an exact irrational spectral-population control."""
import datetime,hashlib,json
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent
def q(x):return(F(x),F(x))
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def sub(a,b):return(a[0]-b[1],a[1]-b[0])
def mul(a,b):
 v=[x*y for x in a for y in b];return(min(v),max(v))
def div(a,b):
 assert b[0]>0
 return mul(a,(1/b[1],1/b[0]))
s5=(F(2236,1000),F(2237,1000));s=(F(4071,1000),F(4073,1000))
assert s5[0]**2<5<s5[1]**2
rad=sub(q(30),mul(q(6),s5));assert s[0]**2<rad[0] and s[1]**2>rad[1]
# h=cos(2pi/15), t=cos(7pi/15), exact positive radical embeddings.
A=div(add(q(1),s5),q(4));h=div(add(add(q(1),s5),s),q(8));t=div(sub(sub(s,q(1)),s5),q(8));B=add(q(F(1,2)),h);C=sub(q(F(1,2)),t)
b=q(F(1,9));e=q(F(2,9));c=div(sub(q(F(1,4)),mul(A,b)),B);a=sub(sub(q(F(1,2)),b),c)
f=div(sub(q(F(1,4)),mul(A,e)),C);d=sub(sub(q(F(1,2)),e),f)
p2=[a,b,c,c,b,a];p7=[d,e,f,f,e,d];p5=[sub(sub(q(F(1,2)),x),y)for x,y in zip(p2,p7)]
assert all(x[0]>0 and x[1]<F(1,2) for x in p2+p5+p7)
assert b[0]+e[0]==F(1,3)
def outival(x):return [str(x[0]),str(x[1])]
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'spectrum_exponents':[0,1,2,3,4,5], 'sqrt5_interval':outival(s5),'sqrt30_minus_6sqrt5_interval':outival(s),
 'p2_intervals':[outival(x)for x in p2],'p5_intervals':[outival(x)for x in p5],'p7_intervals':[outival(x)for x in p7],
 'all_populations_strictly_between_zero_and_half':True,
 'scope':'positivity intervals only; linear moment identities follow symbolically from the written defining formulas; not a vector/Gram realization',
 'status':'PASS'}
(P/'frontier-20261029-cyclic15-population-control-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
