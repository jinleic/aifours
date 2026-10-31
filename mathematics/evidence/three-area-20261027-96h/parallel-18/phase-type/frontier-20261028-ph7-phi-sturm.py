#!/usr/bin/env python3
"""Exact polynomial/Sturm audit of the supported two-parameter PH7 chain.

At z=8/9, derive every coefficient numerator over the common denominator L
and isolate sign-changing real roots. This is a family-specific test, never an
all-topology exclusion. Fractions and exact Sturm sequences are independent
of the separate grid scan. No network, model, solver, or output overwrite
outside this script's named research artifacts.
"""
from fractions import Fraction as F
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
z=F(8,9)

def clean(p):
    p=list(p)
    while len(p)>1 and p[-1]==0: p.pop()
    return p

def add(a,b):
    return clean([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def neg(a): return [-v for v in a]
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return clean(c)
def sc(a,c): return clean([x*c for x in a])
def deriv(a): return clean([i*a[i] for i in range(1,len(a))] or [F(0)])
def val(a,x):
    out=F(0)
    for c in reversed(a): out=out*x+c
    return out

def divrem(a,b):
    a=clean(a); b=clean(b)
    if b==[0]: raise ZeroDivisionError
    q=[F(0)]*max(1,len(a)-len(b)+1)
    while a!=[0] and len(a)>=len(b):
        d=len(a)-len(b); t=a[-1]/b[-1]; q[d]+=t
        for j,c in enumerate(b): a[j+d]-=t*c
        a=clean(a)
    return clean(q),a

def sturm(p):
    seq=[clean(p),deriv(p)]
    if seq[-1]==[0]: return seq[:1]
    while seq[-1]!=[0]:
        r=divrem(seq[-2],seq[-1])[1]
        if r==[0]: break
        seq.append(neg(r))
    return seq

def signs_at(seq,x):
    return [1 if y>0 else -1 for p in seq if (y:=val(p,x))!=0]
def variations(s): return sum(s[i]!=s[i-1] for i in range(1,len(s)))
def roots_between(seq,lo,hi): return variations(signs_at(seq,lo))-variations(signs_at(seq,hi))

def main():
    one=[F(1)]; u=[F(0),F(1)]; u2=mul(u,u); u3=mul(u2,u)
    a=add(sc(u,3),[F(3)])
    b=add(add(sc(u2,3),sc(u,9)),[F(3)])
    c3=add(add(add(u3,sc(u2,9)),sc(u,9)),one)
    e4=add(add(sc(u3,3),sc(u2,9)),sc(u,3))
    e5=add(sc(u3,3),sc(u2,3)); e6=u3
    h0=add(sub(add(b,sc(a,4)),mul(a,a)),[F(-6)])
    L=add(sub(b,sc(a,4)),[F(10)-2*z])
    N=add(sub(sub(sc(h0,4),c3),mul(b,sub([F(4)],a))),[F(4)-4*z])
    Q=add(mul(sub(a,[F(4)]),N),mul(add(h0,[-2*z]),L))
    W=add(N,mul(sub([F(4)],a),L))
    B=sub(N,mul(sc(u,2),L))
    C=add(sub(Q,mul(u,N)),mul(u2,L))
    PHI=sub(add(mul(e4,L),mul(c3,W)),add(add(sc(Q,6+2*z),sc(N,4+4*z)),sc(L,(1+z)**2)))
    R2=sub(add(mul(e5,L),mul(e4,W)),add(sc(Q,4+4*z),sc(N,(1+z)**2)))
    R1=sub(add(mul(e6,L),mul(e5,W)),sc(Q,(1+z)**2))
    R0=mul(e6,W)
    D1=sub(R2,mul(sc(u,3),PHI))
    D2=sub(sub(R1,mul(sc(u2,3),PHI)),sc(D1,2))
    D3=sub(sub(sub(R0,mul(u3,PHI)),D1),D2)
    polys={'L':L,'p_num':N,'q_num':Q,'w_num':W,'B_num':B,'C_num':C,'phi_num':PHI,'D1_num':D1,'D2_num':D2,'D3_num':D3}
    # Predefined interval is the complete POSITIVE-rate range for this report:
    # (0, 10) and (10, +infinity) are both counted using Sturm at +infinity.
    def plus_signs(seq): return [1 if p[-1]>0 else -1 for p in seq if p!=[0]]
    report={'z':str(z),'coefficients_ascending':{},'sturm_positive_roots':{},'sample_signs_exact':{},
            'scope':'One specified common-matrix chain family, not an all-PH7 claim.'}
    points=[F(0),F(1),F(3,2),F(2),F(3),F(10)]
    for name,p in polys.items():
        seq=sturm(p)
        report['coefficients_ascending'][name]=[str(x) for x in p]
        report['sturm_positive_roots'][name]=variations(signs_at(seq,F(0)))-variations(plus_signs(seq))
        report['sample_signs_exact'][name]={str(x): ('+' if val(p,x)>0 else '-' if val(p,x)<0 else '0') for x in points}
    # Every positivity check at a rational u uses exact common denominator L.
    root=ROOT/'frontier-20261028-ph7-phi-sturm-result.json'
    root.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
    print('saved:',root)

if __name__=='__main__': main()
