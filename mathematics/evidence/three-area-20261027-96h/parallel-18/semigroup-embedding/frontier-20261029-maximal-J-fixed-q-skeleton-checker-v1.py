"""Literal C2 controls for the maximal-J coset skeleton lemma.
Constructs a normal band over the same specified actor, collapsing nonmaximal
J-classes to zero and separating all same-fibre R-idempotent pairs in maximal
J-classes. This does NOT separate the lower ideal and does not prove Q1.
"""
from itertools import product
from pathlib import Path
import importlib.util
P8=((0,0),(0,1))

def maximal_classes(M):
    N=len(M);ideals=[]
    for x in range(N):
        z={x}|set(M[x])|{M[a][x] for a in range(N)}
        z|={M[M[a][x]][b] for a in range(N) for b in range(N)}
        ideals.append(frozenset(z))
    vals=set(ideals);maxi=[z for z in vals if not any(z<t for t in vals)]
    return [sorted(x for x in range(N) if ideals[x]==z) for z in sorted(maxi,key=lambda z:min(z))]

def construct(M,q,P):
    N=len(M);tops=maximal_classes(M);data=[]
    for T in tops:
        Ts=set(T)
        R={t:frozenset({t}|{M[t][u] for u in T if M[t][u] in Ts}) for t in T}
        L={t:frozenset({t}|{M[u][t] for u in T if M[u][t] in Ts}) for t in T}
        rv=sorted(set(R.values()),key=lambda x:min(x));lv=sorted(set(L.values()),key=lambda x:min(x))
        ri={t:rv.index(R[t]) for t in T};li={t:lv.index(L[t]) for t in T}
        e=next(t for t in T if M[t][t]==t);i0,l0=ri[e],li[e]
        H=[t for t in T if ri[t]==i0 and li[t]==l0]
        aa=[next(t for t in T if ri[t]==i and li[t]==l0) for i in range(len(rv))]
        bb=[next(t for t in T if ri[t]==i0 and li[t]==l) for l in range(len(lv))]
        p0=P[q[e][2]][q[e][0]];NN=frozenset(p0^q[h][1] for h in H)
        assert len(NN)==len(H) and 0 in NN and all(a^b in NN for a in NN for b in NN)
        u=[q[t][1] for t in aa];v=[p0^q[t][1] for t in bb]
        ir=[q[t][0] for t in aa];lc=[q[t][2] for t in bb]
        for t in T:
            hh=[h for h in H if M[M[aa[ri[t]]][h]][bb[li[t]]]==t]
            assert len(hh)==1 and q[t][1]==u[ri[t]]^p0^q[hh[0]][1]^v[li[t]]
            assert q[t][0]==ir[ri[t]] and q[t][2]==lc[li[t]]
        for l,i in product(range(len(lv)),range(len(rv))):
            r=v[l]^P[lc[l]][ir[i]]^u[i]
            assert (M[bb[l]][aa[i]] in Ts)==(r in NN)
        cos=lambda a,NN=NN:frozenset(a^z for z in NN)
        elems=[(a,i,b,l) for a,i,b,l in product(range(2),range(len(rv)),range(2),range(len(lv))) if cos(a^u[i])==cos(b^v[l])]
        data.append((T,Ts,ri,li,u,v,cos,elems,len(H)))
    Bels=[None]+[(k,)+x for k,d in enumerate(data) for x in d[7]];ix={x:i for i,x in enumerate(Bels)}
    def bm(x,y):
        if x is None or y is None or x[0]!=y[0]:return None
        k,a,i,b,l=x;_,aa,j,bb,m=y;d=data[k]
        if d[6](a^d[4][i])!=d[6](aa^d[4][j]):return None
        return (k,a,i,bb,m)
    B=[[ix[bm(x,y)] for y in Bels] for x in Bels]
    al=[0 if x is None else ix[(x[0],x[1]^1,x[2],x[3]^1,x[4])] for x in Bels]
    beta=[0]*N
    for k,d in enumerate(data):
        for t in d[0]:beta[t]=ix[(k,0,d[2][t],q[t][1],d[3][t])]
    return B,al,beta,tops,[d[8] for d in data]

def certify(name,M,q,P):
    N=len(M)
    assert all(M[M[x][y]][z]==M[x][M[y][z]] for x,y,z in product(range(N),repeat=3))
    assert all(any(M[M[x][y]][x]==x for y in range(N)) for x in range(N))
    assert all((M[x][x]==x)==(q[x][1]==P[q[x][2]][q[x][0]]) for x in range(N))
    assert all(q[M[x][y]]==(q[x][0],q[x][1]^P[q[x][2]][q[y][0]]^q[y][1],q[y][2]) for x,y in product(range(N),repeat=2))
    B,al,beta,tops,hsize=construct(M,q,P);n=len(B)
    for x,y,z in product(range(n),repeat=3):
        assert B[B[x][y]][z]==B[x][B[y][z]]
        assert B[B[B[x][y]][z]][x]==B[B[B[x][z]][y]][x]
    assert all(B[x][x]==x and al[al[x]]==x for x in range(n))
    assert all(al[B[x][y]]==B[al[x]][al[y]] for x,y in product(range(n),repeat=2))
    for x,y in product(range(N),repeat=2):
        w=q[x][1]^P[q[x][2]][q[y][0]]
        assert beta[M[x][y]]==B[beta[x]][al[beta[y]] if w else beta[y]]
    topset=set().union(*map(set,tops));E=[x for x in range(N) if M[x][x]==x]
    rp=[(e,f) for e in E for f in E if e<f and q[e]==q[f] and M[e][f]==f and M[f][e]==e]
    maxrp=[(e,f) for e,f in rp if e in topset]
    assert all(beta[e]!=beta[f] for e,f in maxrp)
    print('PASS',name,'source',N,'maximal classes',list(map(len,tops)),'H sizes',hsize,'normal band',n,'maximal R-pairs separated',len(maxrp),'lower R-pairs collapsed',sum(beta[e]==beta[f] for e,f in rp if e not in topset),flush=True)

if __name__=='__main__':
    root=Path(__file__).resolve().parent
    spec=importlib.util.spec_from_file_location('gt',root/'frontier-20261029-group-top-two-level-host-checker-v1.py');gt=importlib.util.module_from_spec(spec);spec.loader.exec_module(gt)
    S=gt.closure([10,37]);pos={s:i for i,s in enumerate(S)}
    M=[[pos[gt.PT[x][y]] for y in S] for x in S];q=[gt.PACT[x] for x in S]
    X=list(product(range(len(M)),range(2),range(2)));xx={x:i for i,x in enumerate(X)}
    M56=[[xx[(M[s][t],r,d)] for t,u,d in X] for s,r,c in X];q56=[q[s] for s,r,c in X]
    certify('CS top with same-fibre R-pairs',M56,q56,P8)
    A=((0,1,2,3,0),(3,2,1,0,1),(0,1,2,3,2),(3,2,1,0,3),(0,1,2,3,4));PP=((4,4,4),(4,1,3),(4,4,1));th=(0,1,0,1,0)
    Y=list(product(range(3),range(5),range(3)));yy={y:i for i,y in enumerate(Y)}
    M45=[[yy[(x[0],A[A[x[1]][PP[x[2]][y[0]]]][y[1]],y[2])] for y in Y] for x in Y];q45=[(x[0],th[x[1]],x[2]) for x in Y]
    P45=tuple(tuple(th[p] for p in row) for row in PP)
    certify('S45 nonclosed top',M45,q45,P45)
    # V-shaped three-element semilattice times RZ2 times C2.
    meet=((0,0,0),(0,1,0),(0,0,2));Z=list(product(range(3),range(2),range(2)));zz={z:i for i,z in enumerate(Z)}
    M12=[[zz[(meet[v][w],d,g^h)] for w,d,h in Z] for v,c,g in Z];q12=[(0,g,0) for v,c,g in Z]
    certify('two incomparable maximal J-classes',M12,q12,((0,),))
    # Purity negative control: forget S45's C2 label. Zero pattern no longer follows membership.
    T=[i for i,x in enumerate(Y) if x[1]==4]
    zero_cells=[(l,i) for l,i in product(range(3),repeat=2) if PP[l][i]!=4]
    forgotten=[(x[0],0,x[2]) for x in Y];P0=tuple((0,0,0) for l in range(3))
    assert all(forgotten[M45[x][y]]==(forgotten[x][0],0,forgotten[y][2]) for x,y in product(range(45),repeat=2))
    purity_failures=[t for t in T if M45[t][t]!=t and forgotten[t][1]==P0[forgotten[t][2]][forgotten[t][0]]]
    mismatch=[(l,i) for l,i in product(range(3),repeat=2) if (PP[l][i]==4)!=(P0[l][i] in {0})]
    assert purity_failures and set(mismatch)==set(zero_cells)
    print('PASS purity negative control: forgotten-label homomorphism has',len(purity_failures),'top purity failures; coset membership incorrectly predicts',len(mismatch),'zero cells nonzero')
    print('LIMIT three finite C2 controls; no lower-layer separation or Q1 conclusion')
