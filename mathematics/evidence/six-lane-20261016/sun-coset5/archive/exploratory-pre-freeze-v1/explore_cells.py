# EXPLORATORY, PRE-FREEZE. Verbatim copy of the Python cells run in the
# session's eval kernel (Python 3.14.3) between 2026-10-18 08:57 and 09:23 PDT,
# before any README/rule freeze. Not preregistered; not gate evidence.
# Cell 1 timed out (30 s); cells 2-6 completed. Outputs: see outputs.txt.

# ---------------- cell 1 (timed out after 30 s; definitions persisted) -------------
import itertools, os
os.environ['TMPDIR']='/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset5/tmp'
V=range(5)
E=list(itertools.combinations(V,2))
eidx={e:i for i,e in enumerate(E)}
def a(al,i,j):
    return al[eidx[(i,j) if i<j else (j,i)]]
def kills(al,ev,th):
    # ev: vertex with r even or None; th: vertex with 3|r or None
    def div(b,v):
        return (b==2 and v==ev) or (b==3 and v==th)
    out=[]
    for (u,v,w) in itertools.permutations(V,3):
        if u<v:  # edge uv has alpha 1 considered; ordered (u,v) unordered handled by perm
            pass
    for tri in itertools.combinations(V,3):
        for (u,v,w) in itertools.permutations(tri):
            if a(al,u,v)==1:
                b=a(al,u,w); c=a(al,v,w)
                # Lemma 3.10a: b <= c*gcd(r_v,b)
                g = b if div(b,v) else 1
                if b==1: g=1
                if b> c*g: out.append(('L3.10a',u,v,w)); 
                # Lemma 3.10b: if b == c*g then |UV|+|VW|<|G| i.e. 1+c<4
                if b==c*g and 1+c>=4: out.append(('L3.10b',u,v,w))
    for v in V:
        others=[w for w in V if w!=v]
        if all(a(al,v,w)==1 for w in others): out.append(('C3.9',v))
        if all(a(al,v,w)==3 for w in others) and v!=ev and v!=th: out.append(('N1',v))
    if all(x==2 for x in al): out.append(('N2',))
    for q in itertools.combinations(V,4):
        if all(a(al,i,j)==1 for i,j in itertools.combinations(q,2)): out.append(('N3',q))
    return out
perms=list(itertools.permutations(V))
def canon(al,ev,th):
    best=None
    for p in perms:
        nal=[0]*10
        for (i,j),x in zip(E,al):
            pi,pj=p[i],p[j]
            nal[eidx[(pi,pj) if pi<pj else (pj,pi)]]=x
        key=(tuple(nal), -1 if ev is None else p[ev], -1 if th is None else p[th])
        if best is None or key<best: best=key
    return best
surv=set()
cnt=0
for al in itertools.product((1,2,3),repeat=10):
    for ev in [None]+list(V):
        for th in [None]+list(V):
            if not kills(al,ev,th):
                cnt+=1
                surv.add(canon(al,ev,th))
print(cnt,len(surv))

# ---------------- cell 2 -------------
# precompute edge permutation maps
pmaps=[]
for p in perms:
    m=[0]*10
    for k,(i,j) in enumerate(E):
        pi,pj=p[i],p[j]
        m[k]=eidx[(pi,pj) if pi<pj else (pj,pi)]
    pmaps.append((p,m))
def canon_al(al):
    best=None;bp=[]
    for p,m in pmaps:
        nal=[0]*10
        for k in range(10): nal[m[k]]=al[k]
        t=tuple(nal)
        if best is None or t<best: best=t;bp=[p]
        elif t==best: bp.append(p)
    return best
classes={}
for al in itertools.product((1,2,3),repeat=10):
    c=canon_al(al)
    if c not in classes: classes[c]=None
print(len(classes))

# ---------------- cell 3 -------------
def stab(al):
    out=[]
    for p,m in pmaps:
        nal=[0]*10
        for k in range(10): nal[m[k]]=al[k]
        if tuple(nal)==tuple(al): out.append(p)
    return out
def et_reps(al):
    S=stab(al); seen=set(); reps=[]
    for ev in [None]+list(V):
        for th in [None]+list(V):
            if (ev,th) in seen: continue
            orb=set()
            for p in S:
                orb.add((None if ev is None else p[ev], None if th is None else p[th]))
            seen|=orb
            reps.append((ev,th))
    return reps
pat=[]
for al in classes:
    for ev,th in et_reps(al):
        pat.append((al,ev,th))
print(len(pat))
surv=[x for x in pat if not kills(*x)]
print(len(surv))
from collections import Counter
print(Counter((x[1] is None, x[2] is None) for x in surv))

# ---------------- cell 4 -------------
from fractions import Fraction as Fr
from math import gcd
def lcm(a,b): return a*b//gcd(a,b)
def isp(v,p,ev,th): return (p==2 and v==ev) or (p==3 and v==th)
def taumin(al,a_,b_,c_,ev,th):
    t=1
    for (x,y,z) in ((a_,b_,c_),(a_,c_,b_),(b_,c_,a_)):
        A=a(al,x,y)
        if A>1 and not isp(z,A,ev,th): t=lcm(t,A)
    return t
def kills2(al,ev,th, use=('T','K','P','F')):
    out=[]
    tau={}
    for tri in itertools.combinations(V,3):
        x,y,z=tri
        als=sorted([a(al,x,y),a(al,x,z),a(al,y,z)])
        tm=taumin(al,x,y,z,ev,th)
        tau[tri]=tm
        if 'T' in use and tm>als[0]*als[1]: out.append(('T',tri))
    if out: return out
    def T(i,j,k): return tau[tuple(sorted((i,j,k)))]
    def linked(v,i,j): return T(v,i,j)==a(al,v,i)*a(al,v,j)
    for v in V:
        oth=[w for w in V if w!=v]
        if 'K' in use:
            for r in (2,3,4):
                for S in itertools.combinations(oth,r):
                    if all(linked(v,i,j) for i,j in itertools.combinations(S,2)) and sum(a(al,i,v) for i in S)>3:
                        out.append(('K',v,S))
        if 'P' in use:
            # Bonferroni at v
            X={j:Fr(a(al,v,j),4) for j in oth}
            smax={}
            bad=False
            for j,k in itertools.combinations(oth,2):
                g=gcd(1 if not isp(v,2,ev,th) and not isp(v,3,ev,th) else (2 if v==ev else 1)*(3 if v==th else 1), a(al,j,k))
                # g = gcd(r_v, alpha_jk) computed from specials
                g=1
                A=a(al,j,k)
                if A==2 and v==ev: g=2
                if A==3 and v==th: g=3
                unit=Fr(1,4*g)
                lo=max(Fr(T(v,j,k),4*A), X[j]+X[k]-1)
                m=min(X[j],X[k])
                # containment allowed?
                if X[j]<X[k]: allow = a(al,v,j)+A<=3
                elif X[k]<X[j]: allow = a(al,v,k)+A<=3
                else: allow = (a(al,v,j)+A<=3) and (a(al,v,k)+A<=3)
                hi = m if allow else m-unit
                if hi<lo: bad=True; out.append(('P-pair',v,(j,k)))
                smax[(j,k)]=hi
            if not bad:
                for r in (2,3,4):
                    for S in itertools.combinations(oth,r):
                        tot=sum(1-X[j] for j in S)-sum(1-X[j]-X[k]+smax[(j,k)] for j,k in itertools.combinations(S,2))
                        if tot>=1: out.append(('P',v,S))
    if 'F' in use:
        for tri in itertools.combinations(V,3):
            if all(a(al,i,j)==1 for i,j in itertools.combinations(tri,2)):
                if not fibre_ok(al,ev,th,tri): out.append(('F',tri))
    return out
def fibre_ok(al,ev,th,I0):
    rest=[l for l in V if l not in I0]
    # cosets 0,1,2 occupied by I0 members in order; enumerate t_l and M_l for rest
    # vertices in I (U_l in H) have t=1 and must have alpha=1 with all of I
    choices={}
    for l in rest:
        opts=[]
        lo=max(a(al,i,l) for i in I0)
        for t in range(lo,5):
            for M in itertools.combinations(range(4),t):
                opts.append((t,M))
        choices[l]=opts
    def ok_pair(l,tl,m,tm):
        for p in (2,3):
            if (tl%p==0 or isp(l,p,ev,th)) and (tm%p==0 or isp(m,p,ev,th)): return True
        return False
    occ={I0[0]:(1,(0,)),I0[1]:(1,(1,)),I0[2]:(1,(2,))}
    for combo in itertools.product(*[choices[l] for l in rest]):
        asg=dict(occ); asg.update(dict(zip(rest,combo)))
        good=True
        # I members: t=1 vertices among rest must have alpha 1 to all in I0 and to each other (U_l in H); also distinct cosets from other I members
        for l in rest:
            t,M=asg[l]
            if t==1 and any(a(al,i,l)!=1 for i in I0): good=False
        if not good: continue
        for l,m in itertools.combinations(V,2):
            tl,Ml=asg[l]; tm,Mm=asg[m]
            if set(Ml)&set(Mm) and not ok_pair(l,tl,m,tm): good=False;break
        if good: return True
    return False
surv2=[x for x in pat if not kills2(*x)]
print(len(surv2))
print(Counter((x[1] is None, x[2] is None) for x in surv2))

# ---------------- cell 5 -------------
def show(x):
    al,ev,th=x
    M=[[0]*5 for _ in V]
    for (i,j),v in zip(E,al): M[i][j]=M[j][i]=v
    return ' '.join(''.join(str(M[i][j]) if i!=j else '.' for j in V) for i in V)+f'  e={ev} t={th}'
for x in sorted(surv2,key=lambda x:(x[1] is not None)+(x[2] is not None)):
    print(show(x))

# ---------------- cell 6 -------------
INF=99
def vp(n,p):
    c=0
    while n%p==0: n//=p; c+=1
    return c
def maxgcd(l,tl,k,tk,m,ev,th):
    # max possible gcd of local indices (4/m) r t ; returns integer
    base=4//m
    a1=vp(base,2)+vp(tl,2)+(INF if l==ev else 0); a2=vp(base,2)+vp(tk,2)+(INF if k==ev else 0)
    b1=vp(tl,3)+(INF if l==th else 0); b2=vp(tk,3)+(INF if k==th else 0)
    return 2**min(a1,a2)*3**min(b1,b2)
def sun_ok(S,asg,m,ev,th):
    k=len(S)
    if k<=1: return True
    for l,q in itertools.combinations(S,2):
        if maxgcd(l,asg[l][0],q,asg[q][0],m,ev,th)>=k: return True
    return False
def fibre_general(al,ev,th,m,inside,forced_inside=()):
    """H of index m; 'inside' = list of vertices known with U in H, placed in distinct cosets? (m=4 from alpha-1 products)
    returns True if some assignment survives."""
    ncos=m
    rest=[l for l in V if l not in inside]
    choices={}
    for l in rest:
        opts=[]
        lo=1
        for i in inside:
            A=a(al,i,l)
            lo=max(lo, A if m==4 else (A+1)//2)
        for t in range(lo,m+1):
            if t==1 and l in forced_inside: pass
            if l in forced_inside and t!=1: continue
            for M in itertools.combinations(range(ncos),t):
                opts.append((t,M))
        choices[l]=opts
    # inside vertices: place in cosets; enumerate placements
    for place in itertools.product(range(ncos),repeat=len(inside)):
        asg={i:(1,(c,)) for i,c in zip(inside,place)}
        for combo in itertools.product(*[choices[l] for l in rest]):
            asg2=dict(asg); asg2.update(dict(zip(rest,combo)))
            good=True
            # inside pairs must have alpha 1 if m==4 (U_iU_j subset H, size alpha/4 <= 1/4)
            ins=[l for l in V if asg2[l][0]==1]
            for i,j in itertools.combinations(ins,2):
                if m==4 and a(al,i,j)!=1: good=False;break
                if m==2 and a(al,i,j)>2: good=False;break
            if not good: continue
            # t lower bounds relative to all inside
            for l in V:
                for i in ins:
                    if i==l: continue
                    A=a(al,i,l)
                    t=asg2[l][0]
                    if (m==4 and A>t) or (m==2 and A>2*t): good=False
            if not good: continue
            for c in range(ncos):
                S=[l for l in V if c in asg2[l][1]]
                if not sun_ok(S,asg2,m,ev,th): good=False;break
            if good: return True
    return False
def kills3(al,ev,th):
    out=kills2(al,ev,th)
    if all(x==2 for x in al): out.append(('N2',))
    # H from 1-1-1 triangles
    for tri in itertools.combinations(V,3):
        if all(a(al,i,j)==1 for i,j in itertools.combinations(tri,2)):
            if not fibre_general(al,ev,th,4,list(tri)): out.append(('F4-tri',tri))
    # W' : alpha_01=1 and v with alpha_v0=alpha_v1=2
    for (x,y) in E:
        if a(al,x,y)!=1: continue
        vs=[v for v in V if v not in (x,y) and a(al,v,x)==2 and a(al,v,y)==2]
        if not vs: continue
        ok4=fibre_general(al,ev,th,4,[x,y])
        ok2=fibre_general(al,ev,th,2,[x,y],forced_inside=vs)
        if not ok4 and not ok2: out.append(('W',(x,y)))
    return out
surv3=[x for x in surv2 if not kills3(*x)]
print(len(surv3))
for x in surv3: print(show(x))
