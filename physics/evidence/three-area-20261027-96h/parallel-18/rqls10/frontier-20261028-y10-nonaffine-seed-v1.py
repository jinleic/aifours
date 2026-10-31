#!/usr/bin/env python3
"""Exact principal-branch Y_10_3_278 seed at a=1,b=zeta3,c=1."""
import datetime,hashlib,itertools,json
from fractions import Fraction as Q
from pathlib import Path
P=Path(__file__).resolve().parent
# x+y*w, w=zeta6 and w^2=w-1.
def add(x,y):return(x[0]+y[0],x[1]+y[1])
def neg(x):return(-x[0],-x[1])
def sub(x,y):return add(x,neg(y))
def mul(x,y):return(x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]+x[1]*y[1])
def conj(x):return(x[0]+x[1],-x[1])
def inv(x):
 v=mul(x,conj(x));assert v[1]==0 and v[0]!=0;return tuple(k/v[0]for k in conj(x))
def div(x,y):return mul(x,inv(y))
def powi(x,n):
 if n<0:return powi(inv(x),-n)
 v=ONE
 for _ in range(n):v=mul(v,x)
 return v
ZERO=(Q(0),Q(0));ONE=(Q(1),Q(0));w=(Q(0),Q(1));om=powi(w,2);om2=powi(w,4)
a=ONE;b=om;c=ONE
D=sub(mul(a,b),add(a,b));C=sub(sub(mul(a,b),mul(powi(a,2),b)),mul(a,powi(b,2)))
N=add(sub(sub(add(neg(a),mul((Q(2),Q(0)),powi(a,2))),b),mul(powi(a,2),b)),add(sub(mul((Q(4),Q(0)),mul(a,b)),mul(a,powi(b,2))),mul((Q(2),Q(0)),powi(b,2))))
sqrt_rad=add((Q(2),Q(0)),om);assert mul(sqrt_rad,sqrt_rad)==sub(mul(N,N),mul((Q(4),Q(0)),mul(D,C)))
u=div(sub(N,sqrt_rad),mul((Q(2),Q(0)),D));assert u==ONE
p=sub(sub((Q(-2),Q(0)),div(a,b)),div(b,a));sqrtp=sub(mul((Q(2),Q(0)),w),ONE);assert mul(sqrtp,sqrtp)==sub(mul(p,p),(Q(4),Q(0)))
q=div(add(div(sub(p,sqrtp),(Q(2),Q(0))),ONE),sub(sub(sub(ONE,inv(u)),inv(a)),inv(b)))
r=sub(sub(sub(sub(q,ONE),div(q,u)),div(q,a)),div(q,b));s=div(sub(add(q,mul(q,r)),r),sub(add(ONE,r),q));t=div(neg(mul(mul(r,u),add(a,b))),mul(add(add(add(mul(r,u),r),s),mul(r,s)),b))
assert q==neg(ONE) and r==om2 and s==om and t==om
m=mul;d=div;ne=neg;O=ONE
K=[
 [O,O,O,O,O,O,O,O,O,O],
 [O,O,u,ne(d(m(s,q),r)),ne(d(m(s,q),r)),d(m(s,q),r),d(m(s,q),r),ne(u),ne(O),ne(O)],
 [O,O,ne(O),s,d(s,r),ne(d(m(s,q),m(b,r))),ne(d(m(s,q),m(a,r))),u,ne(inv(c)),inv(c)],
 [O,O,ne(O),d(s,r),s,ne(d(m(s,q),m(a,r))),ne(d(m(s,q),m(b,r))),u,inv(c),ne(inv(c))],
 [O,r,q,ne(q),ne(q),m(q,c),ne(m(q,c)),d(m(r,u),s),d(m(r,a),s),d(m(r,b),s)],
 [O,inv(r),d(q,r),ne(d(q,r)),ne(d(q,r)),ne(d(m(q,c),r)),d(m(q,c),r),d(u,s),d(b,s),d(a,s)],
 [O,d(a,b),a,m(a,c),ne(m(a,c)),ne(a),ne(a),t,ne(d(m(r,a),s)),ne(d(a,s))],
 [O,d(b,a),b,ne(m(b,c)),m(b,c),ne(b),ne(b),d(m(t,b),a),ne(d(b,s)),ne(d(m(r,b),s))],
 [O,ne(O),ne(c),ne(m(a,c)),ne(m(b,c)),ne(m(q,c)),ne(d(m(q,c),r)),ne(m(u,c)),c,c],
 [O,ne(O),c,m(b,c),m(a,c),d(m(q,c),r),m(q,c),m(u,c),ne(c),ne(c)]]
roots=[powi(w,k)for k in range(6)];E=[]
for row in K:
 E.append([roots.index(x)for x in row]);assert all(m(x,conj(x))==ONE for x in row)
def sm(xs):
 o=ZERO
 for x in xs:o=add(o,x)
 return o
for i,j in itertools.combinations(range(10),2):
 assert sm(m(conj(K[k][i]),K[k][j])for k in range(10))==ZERO
 assert sm(m(conj(K[i][k]),K[j][k])for k in range(10))==ZERO
obj={'source':'https://github.com/matrix-toolbox/chm/blob/main/CHM_SINKHORN/Y_10_3_278.m',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'phase_point':'a=1,b=zeta3,c=1','auxiliaries':'u=1,q=-1,r=zeta3^2,s=zeta3,t=zeta3',
 'radical_square_checked':True,'normalization_and_90_grams_checked':True,'all_entries_mu6':True,'exponent_matrix':E,'status':'PASS'}
(P/'frontier-20261028-y10-nonaffine-seed-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
