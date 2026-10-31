#!/usr/bin/env python3
"""Exact rational diagnostics for the original delayed forcing/range formula.

Uses a nilpotent physical drift, affine L2 kernel, polynomial deterministic input,
exact rational interior-node interpolation integration, and separate direct SDE-
mean and kernel constructions. Also handles h=0. Finite cases do not prove the
universal theorem; no author checker is imported.
"""
from fractions import Fraction as F
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-review-f54-delayed-kernel-independent-check-results.json'
N=3
P=[[F(0),F(1),F(0)],[F(0),F(0),F(1)],[F(0),F(0),F(0)]]
Q=[[F(1),F(0),F(1)],[F(0),F(2),F(1)],[F(0),F(0),F(0)]]
B=[F(1),F(-1),F(2)]; C=[F(2),F(1),F(-1)]; B0=[F(1),F(1),F(0)]
L0=F(2,3); LH=F(-1,4); HA=F(1,3); HB=F(2,5)
T=F(7,5); H=F(2,5); INPUT_A=F(3,2); INPUT_B=F(-2,7)


def add(a,b):return [x+y for x,y in zip(a,b)]
def scale(c,a):return [c*x for x in a]
def mv(M,v):return [sum((M[i][j]*v[j] for j in range(N)),F(0)) for i in range(N)]
def expP(r,v):return add(add(v,scale(r,mv(P,v))),scale(r*r/2,mv(P,mv(P,v))))
def v(x,S):return INPUT_A+INPUT_B*x if 0<=x<=S else F(0)
def hval(r):return HA+HB*r


def weights(m):
    nodes=[F(i+1,m+1) for i in range(m)];out=[]
    for i,x in enumerate(nodes):
        poly=[F(1)];den=F(1)
        for j,y in enumerate(nodes):
            if i==j:continue
            nxt=[F(0)]*(len(poly)+1)
            for k,c in enumerate(poly):nxt[k]-=y*c;nxt[k+1]+=c
            poly=nxt;den*=x-y
        out.append(sum((c/F(k+1) for k,c in enumerate(poly)),F(0))/den)
    return nodes,out
NODES,WEIGHTS=weights(9)  # exact on polynomials of degree <=8


def quad(fun,a,b,dim):
    if b<=a:return [F(0)]*dim
    vals=[fun(a+(b-a)*x) for x in NODES]
    return [(b-a)*sum((w*val[j] for w,val in zip(WEIGHTS,vals)),F(0)) for j in range(dim)]


def pieces(fun,a,b,knots,dim):
    cuts=sorted({a,b,*[x for x in knots if a<x<b]});out=[F(0)]*dim
    for lo,hi in zip(cuts,cuts[1:]):out=add(out,quad(fun,lo,hi,dim))
    return out


def rdel(t,S,h):
    lo=max(F(0),t-S);hi=min(h,t)
    conv=quad(lambda u:[hval(u)*v(t-u,S)],lo,hi,1)[0]
    return L0*v(t,S)+LH*v(t-h,S)+conv


def direct(t,h,S):
    if h==0:
        R=lambda s:(L0+LH)*v(s,S)
    else:
        R=lambda s:rdel(s,S,h)
    force=lambda s:add(scale(R(s),B),scale(v(s-h,S),C))
    x=pieces(lambda s:expP(t-s,force(s)),F(0),t,[h,S,S+h],N)
    return add(mv(Q,x),scale(R(t),B0))


def kernel(r,h):
    if h==0:
        Fv=add(scale(L0+LH,B),C)
        return mv(Q,expP(r,Fv))
    first=expP(r,scale(L0,B))
    delayed=expP(r-h,add(scale(LH,B),C)) if r>=h else [F(0)]*N
    integ=quad(lambda u:scale(hval(u),expP(r-u,B)),F(0),min(h,r),N)
    return add(mv(Q,add(add(first,delayed),integ)),scale(hval(r),B0) if r<h else [F(0)]*N)


def via_kernel(t,h,S):
    if h==0:atoms=scale((L0+LH)*v(t,S),B0)
    else:atoms=scale(L0*v(t,S)+LH*v(t-h,S),B0)
    lo=max(F(0),t-S)
    reg=pieces(lambda r:scale(v(t-r,S),kernel(r,h)),lo,t,[h],N)
    return add(atoms,reg)


def outer(v):return [v[i]*v[j] for i in range(N) for j in range(N)]
def rank(cols):
    A=[[c[i] for c in cols] for i in range(N)]
    r=0
    for j in range(len(cols)):
        p=next((i for i in range(r,N) if A[i][j]),None)
        if p is None:continue
        A[r],A[p]=A[p],A[r];d=A[r][j];A[r]=[x/d for x in A[r]]
        for i in range(N):
            if i!=r and A[i][j]:
                d=A[i][j];A[i]=[x-d*y for x,y in zip(A[i],A[r])]
        r+=1
        if r==N:break
    return r


def range_check(h):
    S=T-h
    atoms=[scale(L0,B0),scale(LH,B0)] if h else [scale(L0+LH,B0)]
    gamma=[sum((u[i]*u[j] for u in atoms),F(0)) for i in range(N) for j in range(N)]
    gamma=add(gamma,pieces(lambda r:outer(kernel(r,h)),F(0),T,[h],N*N))
    gamma_cols=[[gamma[i*N+j] for i in range(N)] for j in range(N)]
    intervals=[(F(0),h),(h,T)] if h else [(F(0),T)]
    # Each K segment has degree <=4; five distinct interior evaluations span
    # its coefficient vectors by exact Vandermonde interpolation.
    cols=list(atoms)
    for lo,hi in intervals:
        if hi>lo:
            cols.extend(kernel(lo+(hi-lo)*F(i,6),h) for i in range(1,6))
    return {'gamma_rank':rank(gamma_cols),'kernel_span_rank':rank(cols),
            'joint_rank':rank(gamma_cols+cols),
            'gamma_matrix':[[str(gamma[i*N+j]) for j in range(N)] for i in range(N)]}


def main():
    for j in range(N):
        basis=[F(int(i==j)) for i in range(N)]
        if any(mv(P,mv(P,mv(P,basis)))):raise ValueError('drift cube is nonzero')
    cases=[]
    for h in (H,F(0)):
        S=T-h;ts=[F(1,7),h if h else F(1,3),F(11,15),S,(S+T)/2,T]
        mismatches=[]
        for t in ts:
            a=direct(t,h,S);b=via_kernel(t,h,S)
            if a!=b:mismatches.append({'t':str(t),'direct':list(map(str,a)),'kernel':list(map(str,b))})
        rr=range_check(h)
        cases.append({'h':str(h),'T':str(T),'S':str(S),'time_points':[str(t) for t in ts],
                      'direct_vs_kernel_mismatches':mismatches,'range':rr})
    ok=all(not c['direct_vs_kernel_mismatches'] and c['range']['gamma_rank']==c['range']['kernel_span_rank']==c['range']['joint_rank'] for c in cases)
    result={'kind':'independent_exact_rational_delayed_forcing_check',
            'parameters':{'P':[[str(x) for x in r] for r in P],'Q':[[str(x) for x in r] for r in Q],
                          'B':list(map(str,B)),'C':list(map(str,C)),'B0':list(map(str,B0)),
                          'L0':str(L0),'Lh':str(LH),'H(r)':f'{HA}+({HB})r',
                          'input':f'{INPUT_A}+({INPUT_B})t on [0,S]'},
            'cases':cases,'method':'Exact Fraction arithmetic; independent direct Volterra and kernel integrations with 9-node rational polynomial quadrature; exact rational Gaussian elimination.',
            'scope':'Selected finite rational diagnostics, including h>0 and h=0; no proof of universal delayed characterization.',
            'verdict':'PASS' if ok else 'FAIL'}
    OUT.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps(result,sort_keys=True,indent=2));return 0 if ok else 1


if __name__=='__main__':raise SystemExit(main())
