#!/usr/bin/env python3
"""Exact finite search: Z2-quotient 1RQLS(10) in the flat Z5^2-diagonal four-orbit ansatz.

Ansatz (stated precisely in the companion .md): rows/columns/labels split into halves R0,R1,C0,C1,T0,T1 of size 5;
quadrant Q_ij = R_i x C_j has labels in T_(i+j).  Every quadrant is indexed by x in Z5^2 and carries vectors
psi_q(x)_j = zeta5^<c_j,x> * exp(i phi_{q,j}) / sqrt(10)  (j=0..9, characters c_j in Z5^2, multiset T).
Each basis type (R0:Q00,Q01  R1:Q10,Q11  C0:Q00,Q10  C1:Q01,Q11  T0:Q00,Q11  T1:Q01,Q10) is a pair of cosets of one
line L (same line in both quadrants) with offset delta.  For flat vectors, orthonormality of all bases is EXACTLY:
 (U) T uniform along L (each value of <c,l> taken twice), and
 (P) for each frequency pair {j,j'}: (phi_{q',j}-phi_{q,j})-(phi_{q',j'}-phi_{q,j'}) = pi + (2pi/5)(<c_j',delta>-<c_j,delta>) mod 2pi.
(P) is an integer linear system over the torus; it is solvable iff y.rhs = 0 mod 10 (units pi/5) for an integer
basis y of the left kernel.  WLOG (GL(2,5) and quadrant re-indexing) the K-part lines are (0,1),(1,0),(1,4) with
zero offsets and T is taken up to translation.  The search enumerates every admissible T, every completion line
triple and every Q11 offset pair.  Scope: this ansatz only.
"""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent
def dot5(c,x):return (c[0]*x[0]+c[1]*x[1])%5
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
    rows=[];rhs=[]
    for (q,q2,ell,delta) in types:
        cls=collections.defaultdict(list)
        for j,c in enumerate(T):cls[dot5(c,ell)].append(j)
        if len(cls)!=5 or any(len(v)!=2 for v in cls.values()):return None
        for f,(j,j2) in sorted(cls.items()):
            a=[0]*(nq*10);a[q2*10+j]+=1;a[q*10+j]-=1;a[q2*10+j2]-=1;a[q*10+j2]+=1
            rows.append(a);rhs.append((5+2*(dot5(T[j2],delta)-dot5(T[j],delta)))%10)
    return rows,rhs
def solvable(T,types,nq):
    S=build(T,types,nq)
    if S is None:return None
    rows,rhs=S;return all(sum(a*b for a,b in zip(y,rhs))%10==0 for y in int_left_kernel(rows))
LINES=[(1,0),(0,1),(1,1),(1,2),(1,3),(1,4)]
def same(a,b):return (a[0]*b[1]-a[1]*b[0])%5==0
def coset_reps(ell):
    out=[];seen=set()
    for x in itertools.product(range(5),repeat=2):
        k=frozenset(((x[0]+t*ell[0])%5,(x[1]+t*ell[1])%5) for t in range(5))
        if k not in seen:seen.add(k);out.append(x)
    return out
# all multisets T uniform along alpha (l=(1,0)), beta (l=(0,1)), alpha-beta (l=(1,4))
comps=[c for c in itertools.product(range(3),repeat=5) if sum(c)==2];allT=[]
def rec(i,cols,acc):
    if i==5:
        T=[(a,b) for a in range(5) for b in range(5) for _ in range(acc[a][b])]
        cnt=collections.Counter(dot5(c,(1,4)) for c in T)
        if all(cols[k]==2 for k in range(5)) and len(cnt)==5 and all(v==2 for v in cnt.values()):allT.append(T)
        return
    for c in comps:
        nc=[x+y for x,y in zip(cols,c)]
        if max(nc)<=2:rec(i+1,nc,acc+[c])
rec(0,[0]*5,[])
def canon(T):
    return min(tuple(sorted(((a+u)%5,(b+v)%5) for a,b in T)) for u in range(5) for v in range(5))
Tcan=sorted({canon(T) for T in allT})
K=[(0,1,(0,1),(0,0)),(0,2,(1,0),(0,0)),(1,2,(1,4),(0,0))]
LR0,LC0,LT1=(0,1),(1,0),(1,4)
records=[];total_tested=0;total_uniform=0;total_solvable=0
for T in Tcan:
    T=list(T);ksol=solvable(T,K,3);tested=uniform=sol=0
    for LT0 in LINES:
        if same(LT0,LR0) or same(LT0,LC0):continue
        for LC1 in LINES:
            if same(LC1,LR0) or same(LC1,LT1):continue
            for LR1 in LINES:
                if same(LR1,LC0) or same(LR1,LT1) or same(LR1,LC1) or same(LR1,LT0) or same(LC1,LT0):continue
                for dR in coset_reps(LR1):
                    for dC in coset_reps(LC1):
                        r=solvable(T,K+[(2,3,LR1,dR),(1,3,LC1,dC),(0,3,LT0,(0,0))],4);tested+=1
                        if r is not None:uniform+=1
                        if r:sol+=1
    total_tested+=tested;total_uniform+=uniform;total_solvable+=sol
    records.append({'T':T,'K_part_solvable':ksol,'completion_cases':tested,'uniform_cases':uniform,'solvable_completions':sol})
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'admissible_T_total':len(allT),'admissible_T_up_to_translation':len(Tcan),
 'T_with_solvable_K_part':sum(1 for r in records if r['K_part_solvable']),
 'completion_cases_tested':total_tested,'cases_with_uniform_T':total_uniform,'solvable_full_completions':total_solvable,
 'records':records,'scope':'flat Z5^2-diagonal four-orbit ansatz only; exact integer torus-solvability criterion',
 'status':'NO_COMPLETION_IN_ANSATZ' if total_solvable==0 else 'COMPLETION_FOUND'}
(P/'frontier-20261029-flat-diagonal-z5sq-completion-search-v1.json').write_text(json.dumps(out,indent=1)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
