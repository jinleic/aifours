#!/usr/bin/env python3
"""Exact finite search, m=7: Z2-quotient 1-RQLS(14) in the flat Z7^2-diagonal four-orbit ansatz.

Same ansatz and exact torus criterion as frontier-20261029-flat-diagonal-z5sq-completion-search-v1.py, with Z7.
Units pi/7; rhs = 7 + 2(<c_j',delta>-<c_j,delta>) mod 14.  WLOG: K-lines (0,1),(1,0),(1,6), K-offsets 0,
T normalised by a beta-translation so that row alpha=0 contains beta=0 (alpha-translations are not quotiented).
Enumerates every 14-multiset T uniform along alpha, beta, alpha-beta, keeps those with solvable K-part, and for each
tests every completion line triple (uniform lines only) and every Q11 offset pair (dT0=0).  Scope: this ansatz only.
"""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent
m=7
def dotm(c,x):return (c[0]*x[0]+c[1]*x[1])%m
def int_left_kernel(A):
    E=len(A);N=len(A[0]);M=[list(A[i])+[1 if k==i else 0 for k in range(E)] for i in range(E)];r=0
    for c in range(N):
        while True:
            nz=[i for i in range(r,E) if M[i][c]!=0]
            if not nz:break
            piv=min(nz,key=lambda i:abs(M[i][c]));M[r],M[piv]=M[piv],M[r];done=True
            for i in range(r+1,E):
                if M[i][c]!=0:
                    q=M[i][c]//M[r][c];M[i]=[a-q*b for a,b in zip(M[i],M[r])]
                    if M[i][c]!=0:done=False
            if done:break
        if any(M[i][c]!=0 for i in range(r,E)):r+=1
        if r==E:break
    return [row[N:] for row in M if all(x==0 for x in row[:N])]
def build(T,types,nq):
    rows=[];rhs=[];n=len(T)
    for (q,q2,ell,delta) in types:
        cls=collections.defaultdict(list)
        for j,c in enumerate(T):cls[dotm(c,ell)].append(j)
        if len(cls)!=m or any(len(v)!=2 for v in cls.values()):return None
        for f,(j,j2) in sorted(cls.items()):
            a=[0]*(nq*n);a[q2*n+j]+=1;a[q*n+j]-=1;a[q2*n+j2]-=1;a[q*n+j2]+=1
            rows.append(a);rhs.append((m+2*(dotm(T[j2],delta)-dotm(T[j],delta)))%(2*m))
    return rows,rhs
def solvable(T,types,nq):
    S=build(T,types,nq)
    if S is None:return None
    rows,rhs=S;return all(sum(a*b for a,b in zip(y,rhs))%(2*m)==0 for y in int_left_kernel(rows))
LINES=[(1,k) for k in range(m)]+[(0,1)]
def same(a,b):return (a[0]*b[1]-a[1]*b[0])%m==0
def coset_reps(ell):
    out=[];seen=set()
    for x in itertools.product(range(m),repeat=2):
        k=frozenset(((x[0]+t*ell[0])%m,(x[1]+t*ell[1])%m) for t in range(m))
        if k not in seen:seen.add(k);out.append(x)
    return out
K=[(0,1,(0,1),(0,0)),(0,2,(1,0),(0,0)),(1,2,(1,m-1),(0,0))];LR0,LC0,LT1=(0,1),(1,0),(1,m-1)
pairs=[(a,b) for a in range(m) for b in range(a,m)];col=[0]*m;dg=[0]*m;rowsT=[];allT=[]
def rec(al):
    if al==m:allT.append([(a,b) for a,pr in enumerate(rowsT) for b in pr]);return
    for (b1,b2) in pairs:
        if al==0 and b1!=0:continue
        col[b1]+=1;col[b2]+=1;d1=(al-b1)%m;d2=(al-b2)%m;dg[d1]+=1;dg[d2]+=1
        if col[b1]<=2 and col[b2]<=2 and dg[d1]<=2 and dg[d2]<=2:rowsT.append((b1,b2));rec(al+1);rowsT.pop()
        col[b1]-=1;col[b2]-=1;dg[d1]-=1;dg[d2]-=1
rec(0)
Ksol=[T for T in allT if solvable(T,K,3)]
tested=0;found=[]
for T in Ksol:
    def unif(l):
        f=collections.Counter(dotm(c,l) for c in T);return len(f)==m and all(v==2 for v in f.values())
    ul=[l for l in LINES if unif(l)]
    for LT0 in ul:
        if same(LT0,LR0) or same(LT0,LC0):continue
        for LC1 in ul:
            if same(LC1,LR0) or same(LC1,LT1):continue
            for LR1 in ul:
                if same(LR1,LC0) or same(LR1,LT1) or same(LR1,LC1) or same(LR1,LT0) or same(LC1,LT0):continue
                for dR in coset_reps(LR1):
                    for dC in coset_reps(LC1):
                        tested+=1
                        if solvable(T,K+[(2,3,LR1,dR),(1,3,LC1,dC),(0,3,LT0,(0,0))],4):found.append((T,LT0,LC1,LR1,dR,dC))
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'm':m,'uniform_T_enumerated':len(allT),'T_with_solvable_K_part':len(Ksol),'completion_cases_tested':tested,
 'solvable_full_completions':len(found),'examples':found[:3],
 'status':'NO_COMPLETION_IN_ANSATZ' if not found else 'COMPLETION_FOUND','scope':'flat Z7^2-diagonal four-orbit ansatz only'}
(P/'frontier-20261029-flat-diagonal-m7-completion-search-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
