"""Finite right-zero resolution of the maximal-J skeleton. Exact C2 tables.
The quotient is always a RIGHTSN host homomorphism over the specified q. Whether
real K-columns survive is tested, NOT assumed. This is not a Q1 proof.
"""
from itertools import product
from pathlib import Path
import importlib.util,json
ROOT=Path(__file__).resolve().parent

def module(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/file);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
skh=module('maxj_skeleton','frontier-20261029-maximal-J-fixed-q-skeleton-checker-v1.py')
csh=module('closed_cs','frontier-20261029-CS-top-two-level-host-checker-v1.py')

def resolve(M,q,P,T,K):
    up,ua,ub,tops,hsize=skh.construct(M,q,P)
    assert len(tops)==1 and set(tops[0])==set(T)
    A=list(range(1,len(up)));dc={};dcl=[];lc={};lcl=[]
    for x in A:
        ds=frozenset(y for y in A if up[x][y]!=0)
        if ds not in dcl:dcl.append(ds)
        dc[x]=dcl.index(ds)
        ls=frozenset(y for y in A if up[x][y]==x and up[y][x]==y)
        if ls not in lcl:lcl.append(ls)
        lc[x]=lcl.index(ls)
    cr=[min(c) for c in lcl];kr,kc,_,nk=csh.eggbox(M,K)
    mu=[q[next(k for k in K if kc[k]==c)][2] for c in range(nk)]
    krev=[next(k for k in K if kc[k]==c) for c in range(nk)]
    W=list(product(range(2),range(nk)));wi={w:i for i,w in enumerate(W)}
    pts=[('R',w) for w in range(len(W))]+[('F',w,x) for w in range(len(W)) for x in A]
    pts += [('C',c,y) for c,z in enumerate(cr) for y in A if dc[z]!=dc[y]]
    ix={p:i for i,p in enumerate(pts)}
    def act(p,x):
        if p[0]=='R':return ('F',p[1],x)
        if p[0]=='F':
            w,z=p[1:];return ('F',w,up[z][x]) if dc[z]==dc[x] else ('C',lc[z],x)
        c,z=p[1:];return ('C',c,up[z][x]) if dc[z]==dc[x] else ('C',lc[z],x)
    acts=[[ix[act(p,x)] for x in A] for p in pts]
    wflip=[wi[(m^1,c)] for m,c in W];cflip=[lc[ua[z]] for z in cr]
    def fl(p):
        if p[0]=='R':return ('R',wflip[p[1]])
        if p[0]=='F':return ('F',wflip[p[1]],ua[p[2]])
        return ('C',cflip[p[1]],ua[p[2]])
    pa=[ix[fl(p)] for p in pts];parent=list(range(len(pts)));queue=[]
    def find(x):
        while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
        return x
    def uni(x,y):
        x,y=find(x),find(y)
        if x!=y:parent[x]=y;queue.append((x,y))
    def real(m,c):return ix[('R',wi[(m,c)])]
    for w,(m,c) in enumerate(W):
        k=krev[c]
        for t in T:
            a=m^P[mu[c]][q[t][0]];x=ua[ub[t]] if a else ub[t];kt=M[k][t]
            uni(ix[('F',w,x)],real(a^q[t][1],kc[kt]))
    for s,t in product(T,repeat=2):
        st=M[s][t]
        if st not in K:continue
        w=q[s][1]^P[q[s][2]][q[t][0]]
        for a in range(2):
            x=ua[ub[s]] if a else ub[s];b=a^w;y=ua[ub[t]] if b else ub[t]
            assert dc[x]!=dc[y]
            uni(ix[('C',lc[x],y)],real(a^q[st][1],kc[st]))
    j=0
    while j<len(queue):
        a,b=queue[j];j+=1
        for v,vv in zip(acts[a],acts[b]):uni(v,vv)
        uni(pa[a],pa[b])
    roots=sorted({find(x) for x in range(len(pts))});ri={r:i for i,r in enumerate(roots)}
    rrep=[next(x for x in range(len(pts)) if find(x)==r) for r in roots]
    def point(p):return len(A)+ri[find(p)]
    B=[]
    for x in A:
        B.append([(up[x][y]-1 if up[x][y] else point(ix[('C',lc[x],y)])) for y in A]+[len(A)+i for i in range(len(roots))])
    for p in rrep:B.append([point(z) for z in acts[p]]+[len(A)+i for i in range(len(roots))])
    al=[ua[x]-1 for x in A]+[point(pa[p]) for p in rrep]
    beta=[ub[s]-1 if s in T else point(real(q[s][1],kc[s])) for s in range(len(M))]
    realclasses={w:find(ix[('R',w)]) for w in range(len(W))}
    collisions=[(W[a],W[b]) for a in range(len(W)) for b in range(a+1,len(W)) if realclasses[a]==realclasses[b]]
    return B,al,beta,{'top':len(A),'formal_bottom':len(pts),'bottom_quotient':len(roots),'real':len(W),'real_collisions':collisions,'relations_processed':len(queue)}

def certify(M,q,P,T,K):
    B,al,beta,info=resolve(M,q,P,T,K);n=len(B)
    for x,y,z in product(range(n),repeat=3):
        assert B[B[x][y]][z]==B[x][B[y][z]]
        assert B[B[B[B[B[x][y]][x]][z]][x]][y]==B[B[B[x][z]][x]][y]
    assert all(B[x][x]==x and al[al[x]]==x for x in range(n))
    assert all(al[B[x][y]]==B[al[x]][al[y]] for x,y in product(range(n),repeat=2))
    for s,t in product(range(len(M)),repeat=2):
        w=q[s][1]^P[q[s][2]][q[t][0]]
        assert beta[M[s][t]]==B[beta[s]][al[beta[t]] if w else beta[t]]
    E=[s for s in range(len(M)) if M[s][s]==s]
    rp=[(e,f) for e in E for f in E if e<f and q[e]==q[f] and M[e][f]==f and M[f][e]==e]
    print('CHECK source',len(M),'band',n,info,'R-pair collisions',[(e,f) for e,f in rp if beta[e]==beta[f]],flush=True)
    return B,al,beta,info

if __name__=='__main__':
    A=((0,1,2,3,0),(3,2,1,0,1),(0,1,2,3,2),(3,2,1,0,3),(0,1,2,3,4));P=((4,4,4),(4,1,3),(4,4,1));th=(0,1,0,1,0)
    S=list(product(range(3),range(5),range(3)));si={s:i for i,s in enumerate(S)}
    M=[[si[(x[0],A[A[x[1]][P[x[2]][y[0]]]][y[1]],y[2])] for y in S] for x in S];q=[(x[0],th[x[1]],x[2]) for x in S]
    PP=tuple(tuple(th[x] for x in row) for row in P);T=[i for i,s in enumerate(S) if s[1]==4];K=[i for i,s in enumerate(S) if s[1]!=4]
    B,al,beta,info=certify(M,q,PP,T,K)
    assert not info['real_collisions']
    J=json.loads((ROOT/'frontier-20261029-source45-rightSN-canonical-host-data-v1.json').read_text())
    OLD=J['band_table'];OA=J['band_action'];co=J['coordinates'];mp={};todo=[]
    def put(x,y):
        if x in mp:assert mp[x]==y
        else:mp[x]=y;todo.append(x)
    for s in range(45):put(co[s],beta[s]);put(OA[co[s]],al[beta[s]])
    k=0
    while k<len(todo):
        x=todo[k];k+=1
        for y in tuple(mp):put(OLD[x][y],B[mp[x]][mp[y]]);put(OLD[y][x],B[mp[y]][mp[x]])
    assert len(mp)==len(OLD) and len(set(mp.values()))==len(B)
    assert all(mp[OLD[x][y]]==B[mp[x]][mp[y]] for x,y in product(range(len(OLD)),repeat=2))
    assert all(mp[OA[x]]==al[mp[x]] for x in range(len(OLD)))
    print('PASS literal equivariant quotient of stored band306 onto band66; all 93636 products, all action/source coordinates. No canonical-freeness premise used.')
    print('LIMIT concrete S45 success; real-column injectivity for arbitrary two-layer RRL sources is NOT proved')
