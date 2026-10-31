#!/usr/bin/env python3
"""Exact certificate: no linear group-regular covariant 1-RQLS(10) with non-abelian symmetry group.

Setting (see the companion packet for the written reductions).  A group Gamma of order 100 acts regularly on the
100 cells; rows, columns, label classes are the left cosets of subgroups H1, H2, H3 of order 10 that pairwise
factorise Gamma exactly; psi(gamma) = pi(gamma) v for a LINEAR unitary representation pi on C^10.  Then
pi restricted to every H_i is the regular representation of H_i (a row/column/class is an orthonormal basis that
is one H_i-orbit), so the character of pi vanishes on X = (H1 u H2 u H3) minus {e} and has degree 10.
The written reduction gives Gamma = Z5^2 semidirect V, V = Z2^2, H_i = P_i semidirect <(c_i, x_i)>, with
P_i three distinct lines and x_i the three involutions of V.  Up to GL(2,5)-conjugacy and permutation of the three
(symmetric) types, the action of V is: trivial (abelian; excluded by Hall-Paige, not computed here), 'negI'
(-I, I, -I), 'D' (D, I, D) [also run: (D, D, I)], or 'Klein' (D, -D, -I), D = diag(1,-1).

For every subgroup triple of each non-abelian action this script builds all irreducible characters EXACTLY
(values in Z[zeta5], stored as integer coefficient vectors modulo 1+z+z^2+z^3+z^4) and searches, by an exact
meet-in-the-middle over multiplicity vectors r (0 <= r_rho <= d_rho, sum r_rho d_rho = 10), for a representation
whose character vanishes on X.  Positive control: Z7^2 with three lines must give the 133 orthomorphisms of Z7.
"""
import datetime,hashlib,itertools,json,time
import numpy as np
from pathlib import Path
P=Path(__file__).resolve().parent
T0=time.time()
def mm(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))%5 for j in range(2)) for i in range(2))
def mv(A,p):return tuple(sum(A[i][k]*p[k] for k in range(2))%5 for i in range(2))
def minv(M):
    (a,b),(c,d)=M;di=pow((a*d-b*c)%5,-1,5);return ((d*di%5,(-b)*di%5),((-c)*di%5,a*di%5))
def tr(M):return ((M[0][0],M[1][0]),(M[0][1],M[1][1]))
I2=((1,0),(0,1));NEG=((4,0),(0,4));DD=((1,0),(0,4));DM=((4,0),(0,1))
V=[(0,0),(1,0),(0,1),(1,1)]
def vadd(x,y):return ((x[0]+y[0])%2,(x[1]+y[1])%2)
def cyc_norm(c,n):
    # c: list of n ints = coefficients of z^0..z^{n-1}; reduce modulo 1+z+...+z^{n-1} (n prime)
    return tuple(ci-c[-1] for ci in c[:-1])
def group(A,B):
    Mx={(0,0):I2,(1,0):A,(0,1):B,(1,1):mm(A,B)}
    els=[(p,x) for x in V for p in itertools.product(range(5),repeat=2)];idx={g:i for i,g in enumerate(els)}
    def mul(g,h):
        (p,x),(q,y)=g,h;Mq=mv(Mx[x],q);return (((p[0]+Mq[0])%5,(p[1]+Mq[1])%5),vadd(x,y))
    return els,idx,mul,Mx
def exact_characters(A,B):
    els,idx,mul,Mx=group(A,B);dual={x:tr(minv(Mx[x])) for x in V}
    seen=set();chars=[]
    for c0 in itertools.product(range(5),repeat=2):
        if c0 in seen:continue
        for x in V:seen.add(mv(dual[x],c0))
        stab=[x for x in V if mv(dual[x],c0)==c0]
        reps=[];cov=set()
        for x in V:
            if x in cov:continue
            reps.append(x);cov.update(vadd(x,s) for s in stab)
        lamkeys=set()
        for y in V:
            key=tuple((y[0]*s[0]+y[1]*s[1])%2 for s in stab)
            if key in lamkeys:continue
            lamkeys.add(key)
            d=len(reps);row=[]
            for (p,x) in els:
                c=[0]*5
                if x in stab:
                    sg=(-1)**((y[0]*x[0]+y[1]*x[1])%2)
                    for t in reps:
                        q=mv(minv(Mx[t]),p);c[(c0[0]*q[0]+c0[1]*q[1])%5]+=sg
                row.append(cyc_norm(c,5))
            chars.append((d,row))
    assert sum(d*d for d,_ in chars)==100
    return chars,els,idx,mul,Mx
def subgroups(Mx,xi):
    M=Mx[xi];out=[]
    for dvec in [(1,0)]+[(k,1) for k in range(5)]:
        Pl={((dvec[0]*t)%5,(dvec[1]*t)%5) for t in range(5)}
        if mv(M,dvec) not in Pl:continue
        cosets=set()
        for c in itertools.product(range(5),repeat=2):
            cMc=tuple((c[k]+mv(M,c)[k])%5 for k in range(2))
            if cMc in Pl:cosets.add(frozenset(((c[0]+q[0])%5,(c[1]+q[1])%5) for q in Pl))
        for cs in cosets:out.append((dvec,[(q,(0,0)) for q in Pl]+[(q,xi) for q in cs]))
    return out
def enum_half(ids,d,vecs,maxdim):
    # exact integer accumulation (numpy int64); leaves keyed by the raw bytes of the integer vector
    out=[]
    def rec(i,dim,acc,r):
        if i==len(ids):out.append((dim,acc.tobytes(),tuple(r)));return
        k=ids[i]
        for val in range(d[k]+1):
            nd=dim+val*d[k]
            if nd>maxdim:break
            nacc=acc+val*vecs[k] if val else acc
            rec(i+1,nd,nacc,r+([(k,val)] if val else []))
    rec(0,0,np.zeros(len(vecs[0]),dtype=np.int64),[])
    return out
def count_patterns(d,vecs,target):
    vecs=[np.array(v,dtype=np.int64) for v in vecs]
    ids=sorted(range(len(d)),key=lambda k:d[k]);A=ids[0::2];B=ids[1::2]
    HA=enum_half(A,d,vecs,target);HB=enum_half(B,d,vecs,target);tab={}
    for dim,key,r in HB:tab.setdefault((dim,key),[]).append(r)
    pats=[]
    for dim,key,r in HA:
        neg=(-np.frombuffer(key,dtype=np.int64)).tobytes()
        for r2 in tab.get((target-dim,neg),[]):pats.append(r+r2)
    return pats
results={}
# positive control: Z7^2, three lines, characters chi_c(g)=z7^{c.g}; exact vectors modulo Phi7
els7=[(a,b) for a in range(7) for b in range(7)]
X7=[g for g in els7 if g!=(0,0) and (g[0]==0 or g[1]==0 or g[0]==g[1])]
def vec7(c):
    out=[]
    for g in X7:
        v=[0]*7;v[(c[0]*g[0]+c[1]*g[1])%7]+=1;out.extend(cyc_norm(v,7))
    return tuple(out)
pc=count_patterns([1]*49,[vec7(c) for c in els7],7)
results['positive_control_Z7sq_three_lines']={'patterns':len(pc),'expected_orthomorphisms_of_Z7':133}
ACTIONS={'negI(-I,I,-I)':(NEG,I2),'D(D,I,D)':(DD,I2),'D(D,D,I)':(DD,DD),'Klein(D,-D,-I)':(DD,DM)}
total_setups=0;total_patterns=0
for name,(A,B) in ACTIONS.items():
    chars,els,idx,mul,Mx=exact_characters(A,B)
    e=idx[((0,0),(0,0))];d=[c[0] for c in chars]
    S1=subgroups(Mx,(1,0));S2=subgroups(Mx,(0,1));S3=subgroups(Mx,(1,1))
    ns=0;npat=0;nontriv=0
    for h1 in S1:
        for h2 in S2:
            if h2[0]==h1[0]:continue
            for h3 in S3:
                if h3[0] in (h1[0],h2[0]):continue
                Hs=[{idx[g] for g in h[1]} for h in (h1,h2,h3)]
                for H in Hs:
                    assert len(H)==10 and all(idx[mul(els[a],els[b])] in H for a in H for b in H)
                assert all(len(Hs[i]&Hs[j])==1 for i in range(3) for j in range(i+1,3))
                X=sorted(set().union(*Hs)-{e})
                vecs=[tuple(x for g in X for x in row[g]) for _,row in chars]
                pats=count_patterns(d,vecs,10)
                ns+=1;npat+=len(pats)
    results[name]={'irreducible_degrees':sorted(d),'subgroup_triples':ns,'patterns_found':npat}
    total_setups+=ns;total_patterns+=npat
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'clock_finish':datetime.datetime.now().astimezone().isoformat(),'seconds':round(time.time()-T0,1),
     'results':results,'total_nonabelian_triples':total_setups,'total_patterns':total_patterns,
     'status':'PASS' if (len(pc)==133 and total_patterns==0) else 'CHECK',
     'scope':'Linear representations only; abelian Gamma excluded by Hall-Paige (written); projective case not covered.'}
(P/'frontier-20261029-group-regular-pattern-certificate-v1.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
