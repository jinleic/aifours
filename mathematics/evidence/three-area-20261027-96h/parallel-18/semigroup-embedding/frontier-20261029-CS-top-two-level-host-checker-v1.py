"""Exact C2 checks of the closed completely-simple-top construction.
The arbitrary-group theorem is WRITTEN in the accompanying packet. This checker
constructs the partial-function orbits explicitly and checks the final literal
band, action, host equations, and every same-fibre R-pair. No freeness claim.
"""
from itertools import product
from pathlib import Path
import importlib.util
P8=((0,0),(0,1))

def eggbox(M,A):
    right={x:frozenset(M[x][y] for y in A) for x in A}
    left={x:frozenset(M[y][x] for y in A) for x in A}
    rs=sorted(set(right.values()),key=lambda z:min(z));ls=sorted(set(left.values()),key=lambda z:min(z))
    ri={x:rs.index(right[x]) for x in A};li={x:ls.index(left[x]) for x in A}
    assert all(any(ri[e]==i and li[e]==j and M[e][e]==e for e in A) for i in range(len(rs)) for j in range(len(ls)))
    return ri,li,len(rs),len(ls)

def construct(M,q,T,K,P=P8):
    N=len(M);assert set(T).isdisjoint(K) and set(T)|set(K)==set(range(N))
    assert all(M[x][y] in T for x in T for y in T)
    assert all(M[x][y] in K and M[y][x] in K for x in K for y in range(N))
    assert all(M[M[x][y]][z]==M[x][M[y][z]] for x in range(N) for y in range(N) for z in range(N))
    assert all((M[x][x]==x)==(q[x][1]==P[q[x][2]][q[x][0]]) for x in range(N))
    for x,y in product(range(N),repeat=2):
        i,g,l=q[x];j,h,m=q[y];assert q[M[x][y]]==(i,g^P[l][j]^h,m)
    tr,tc,nr,nc=eggbox(M,T);kr,kc,_,nk=eggbox(M,K)
    it=[q[next(t for t in T if tr[t]==i)][0] for i in range(nr)]
    mu=[q[next(k for k in K if kc[k]==c)][2] for c in range(nk)]
    assert all(q[t][0]==it[tr[t]] for t in T)
    krep=[next(k for k in K if kc[k]==c) for c in range(nk)]
    cdot=lambda c,t:kc[M[krep[c]][t]]
    W=[(m,c) for m in range(2) for c in range(nk)];wi={w:i for i,w in enumerate(W)}
    C=list(product(range(2),range(nc)));ci={c:i for i,c in enumerate(C)}
    fixed=[any(M[e][e]==e and cdot(c,e)==c for e in T) for m,c in W]
    entry=lambda w,i:w[0]^P[mu[w[1]]][it[i]]
    fs=[]
    for w in W:
        fsrow=[]
        for i in range(nr):
            a=entry(w,i);v=[]
            for b,l in C:
                ts=[t for t in T if tr[t]==i and tc[t]==l and q[t][1]==a^b]
                assert len(ts)<=1
                v.append(-1 if not ts else wi[(b,cdot(w[1],ts[0]))])
            fsrow.append(tuple(v))
        fs.append(fsrow)
    funcs=sorted(set(f for row in fs for f in row));fi={f:i for i,f in enumerate(funcs)}
    for w,row in enumerate(fs):
        if fixed[w]:assert all(f==row[0] for f in row)
        for f in row:
            for out in f:
                if out>=0:assert fixed[out] and all(g==f for g in fs[out])
    pts=[('R',w) for w in range(len(W))]
    pts += [('O',f,c) for f in range(len(funcs)) for c,out in enumerate(funcs[f]) if out<0]
    pts += [('M',w,a,i,c) for w in range(len(W)) if not fixed[w] for a,i in product(range(2),range(nr)) if a!=entry(W[w],i) for c in range(len(C))]
    pset=set(pts)
    def Gamma(f,c):
        v=funcs[f][c];return ('R',v) if v>=0 else ('O',f,c)
    def action(p,a,i,c):
        if p[0]=='R':
            w=p[1]
            if fixed[w]:return Gamma(fi[fs[w][0]],c)
            if a==entry(W[w],i):return Gamma(fi[fs[w][i]],c)
            return ('M',w,a,i,c)
        if p[0]=='O':return Gamma(p[1],c)
        return ('M',p[1],p[2],p[3],c)
    wrflip=[wi[(m^1,c)] for m,c in W];cflip=[ci[(b^1,l)] for b,l in C]
    fflip=[fi[tuple(-1 if f[cflip[c]]<0 else wrflip[f[cflip[c]]] for c in range(len(C)))] for f in funcs]
    def pflip(p):
        if p[0]=='R':return ('R',wrflip[p[1]])
        if p[0]=='O':return ('O',fflip[p[1]],cflip[p[2]])
        return ('M',wrflip[p[1]],p[2]^1,p[3],cflip[p[4]])
    elems=[('T',a,i,c) for a,i in product(range(2),range(nr)) for c in range(len(C))]+[('C',p) for p in pts]
    ix={x:i for i,x in enumerate(elems)}
    def mult(x,y):
        if y[0]=='C':return y
        if x[0]=='T':return ('T',x[1],x[2],y[3])
        p=action(x[1],y[1],y[2],y[3]);assert p in pset;return ('C',p)
    B=[[ix[mult(x,y)] for y in elems] for x in elems]
    def flip(x):
        return ('T',x[1]^1,x[2],cflip[x[3]]) if x[0]=='T' else ('C',pflip(x[1]))
    al=[ix[flip(x)] for x in elems]
    beta=[ix[('T',0,tr[s],ci[(q[s][1],tc[s])])] if s in T else ix[('C',('R',wi[(q[s][1],kc[s])]))] for s in range(N)]
    return B,al,beta,{'top_rows':nr,'top_columns':nc,'K_columns':nk,'real_points':len(W),'partial_functions':len(funcs),'orbit_phantoms':sum(p[0]=='O' for p in pts),'moved_phantoms':sum(p[0]=='M' for p in pts)}

def certify(name,M,q,T,K,P=P8):
    B,al,beta,counts=construct(M,q,T,K,P);n=len(B);R=range(n)
    assert all(B[x][x]==x and al[al[x]]==x for x in R)
    for x in R:
        for y in R:
            xy=B[x][y];xyx=B[xy][x]
            assert al[xy]==B[al[x]][al[y]]
            for z in R:
                assert B[xy][z]==B[x][B[y][z]]
                assert B[B[B[xyx][z]][x]][y]==B[B[B[x][z]][x]][y]
    for s,t in product(range(len(M)),repeat=2):
        w=q[s][1]^P[q[s][2]][q[t][0]]
        assert beta[M[s][t]]==B[beta[s]][al[beta[t]] if w else beta[t]]
    E=[s for s in range(len(M)) if M[s][s]==s]
    rp=[(e,f) for e in E for f in E if e<f and q[e]==q[f] and M[e][f]==f and M[f][e]==e]
    assert rp and all(beta[e]!=beta[f] for e,f in rp)
    print('PASS',name,'source',len(M),'band',n,'R-pairs',len(rp),counts,flush=True)

if __name__=='__main__':
    root=Path(__file__).resolve().parent
    spec=importlib.util.spec_from_file_location('gt',root/'frontier-20261029-group-top-two-level-host-checker-v1.py');gt=importlib.util.module_from_spec(spec);spec.loader.exec_module(gt)
    S=gt.closure([10,37]);pos={x:i for i,x in enumerate(S)}
    M=[[pos[gt.PT[x][y]] for y in S] for x in S];q=[gt.PACT[x] for x in S]
    K,T,h=gt.analyse(M,q);certify('14-element group-top source',M,q,T,K)
    # Product with RB22, but actor deliberately ignores the RB coordinate.
    X=list(product(range(len(M)),range(2),range(2)));ix={x:i for i,x in enumerate(X)}
    M56=[[ix[(M[s][t],r,d)] for t,u,d in X] for s,r,c in X]
    q56=[q[s] for s,r,c in X];T56=[ix[x] for x in X if x[0] in T];K56=[ix[x] for x in X if x[0] in K]
    certify('nontrivial CS top; actor ignores RB22 factor',M56,q56,T56,K56)
    # A two-layer six-band: top RB22, bottom RZ2; bottom·(r,c)=c.
    L=list(range(6));BT=[[0]*6 for _ in L]
    for x,y in product(L,repeat=2):
        BT[x][y]=y if y>=4 else (2*(x//2)+(y%2) if x<4 else 4+y%2)
    aut=(3,2,1,0,5,4)
    Y=[(b,(i,g,l)) for b in L for i,g,l in product(range(2),repeat=3)];iy={x:i for i,x in enumerate(Y)}
    def ym(x,y):
        b,(i,g,l)=x;c,(j,h,m)=y;w=g^P8[l][j]
        return iy[(BT[b][aut[c] if w else c],(i,w^h,m))]
    M48=[[ym(x,y) for y in Y] for x in Y];q48=[d for b,d in Y]
    T48=[i for i,(b,d) in enumerate(Y) if b<4];K48=[i for i,(b,d) in enumerate(Y) if b>=4]
    certify('physical source with genuinely varying top actor rows',M48,q48,T48,K48)
    # Inflate an idempotent of D8 upward to a new singleton top; then take RZ2.
    # Top maximal groups are trivial, so their C2 image is proper: orbit phantoms occur.
    D=list(product(range(2),repeat=3));di={d:i for i,d in enumerate(D)}
    dm=lambda x,y:di[(x[0],x[1]^P8[x[2]][y[0]]^y[1],y[2])]
    DM=[[dm(x,y) for y in D] for x in D]
    M9=[[DM[0 if x==8 else x][0 if y==8 else y] if (x,y)!=(8,8) else 8 for y in range(9)] for x in range(9)]
    q9=D+[D[0]];Z=list(product(range(9),range(2)));zi={z:i for i,z in enumerate(Z)}
    M18=[[zi[(M9[x][y],b)] for y,b in Z] for x,a in Z];q18=[q9[x] for x,a in Z]
    T18=[zi[(8,a)] for a in range(2)];K18=[zi[(x,a)] for x in range(8) for a in range(2)]
    certify('proper top-group image; both phantom types',M18,q18,T18,K18)
    print('LIMIT arbitrary-group theorem is written; these are four exact C2 instances only')
