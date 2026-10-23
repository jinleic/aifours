#!/usr/bin/env python3
"""[F] Controls for proof-Eglobal.md: quality-seed existence under E>=2 even and Delta0>=3E/2+6.
Three branches: aligned mixed-packing (g>=B), E-wide (B-g>=2E+3), SA (remaining B>g).
No finite-range premise or full RUNS claim. Control ablation: using SA alone instead of the three-way split.
"""
import random,json,time,resource
GUARD="if __name__ == '__main__':\n    main()"
D={'__name__':'defect_prefix_lib'}
exec(compile(open('defect_prefix.py').read().replace(GUARD,''),'defect_prefix.py','exec'),D)
N=D['N'];C=D['C'];rnd=random.Random(194126)
def ceildiv(a,b):return -((-a)//b)
def sa(p,k,kap,B):
    E=2*p-2*k+2*kap;g=kap-B;De=p-kap-E//2;bs=min(B,E+1)
    lo=max(ceildiv(2*g+B+max(2,bs),3),B+2-De,1)
    hi=min((2*p-B-E-3)//3,De+B-bs-2,ceildiv(k-B-3,2))
    return lo,hi

def recipe(p,k,kap,B):
    E=2*p-2*k+2*kap;g=kap-B
    if g>=B:
        m=(kap+E+1)//2;y0=g+E+1
        return 'P',m,y0,2*m-y0,y0-m
    if B-g>=2*E+3:
        m=(kap+1)//2;c=2 if (m-g-E)%2==0 else 3;y0=g+E+c
        return 'R',m,y0,(m-y0)//2,(m+y0)//2
    lo,hi=sa(p,k,kap,B);assert lo<=hi
    return 'SA',lo,lo,0,lo

def main():
    tt=time.time();st={'classes':0,'P':0,'R':0,'SA':0,'target_types':0,'SA_only_ablation_fail':0};pool=[]
    for p in range(5,102):
        if not C['isprime'](p):continue
        for k,kap,B in C['classes'](p):
            E=2*p-2*k+2*kap;g=kap-B;De=p-kap-E//2
            if E<2 or De<3*E//2+6:continue
            kind,m,y0,v1,v2=recipe(p,k,kap,B)
            if kind=='P':assert v1>=0 and v2>=0 and 2*v1+3*v2<=k-2*B-4
            else:assert v1>=0 and v2>=0 and 2*m<=k-B-3 and (v1==0 or 2*v1<=B-E-3)
            A=p+g+E//2
            lam=lambda y,b:min(p-b+1,y+b-g,(y+B)//2+1)
            lc=lambda y,b:min(p-b+1,A-kap-y+b,(A-y)//2+1)
            U=lambda y,b:p-lc(y,b)
            gen=lambda y,b:lam(y,b)==(y+B)//2+1 and lc(y,b)==(A-y)//2+1
            for d in range(-min(B,E+1),E+2):
                et=abs(d)-1 if d else 1;er=E-et
                ys=range(y0-er,y0+er+1) if kind=='R' else range(y0,y0+er+1)
                for y in ys:
                    assert gen(y,m) and gen(y+d,m+1)
                    sl=lam(y+d,m+1)-U(y,m);sh=U(y+d,m+1)-lam(y,m)
                    assert 2*sl>=d-De+2 and 2*sh<=d+De-2
                    assert lam(d,1)-sh>-p and U(d,1)-sl<p
                    st['target_types']+=1
            lo,hi=sa(p,k,kap,B)
            if lo>hi:st['SA_only_ablation_fail']+=1
            st['classes']+=1;st[kind]+=1;pool.append((p,k,kap,B))
    print(json.dumps({'arithmetic':st}),flush=True)
    selected=[]
    for typ in ('P','R','SA'):
        pp=[t for t in pool if recipe(*t)[0]==typ]
        selected+=rnd.sample(pp,min(12,len(pp)))
    # Pin one B=1 case and both previously written large-B examples whenever they satisfy the stronger synthesis domain.
    selected += [(31,39,9,1),(41,73,33,30)]
    cs={'classes':0,'words':0,'configurations':0,'empty_actual_seed':0}
    for p,k,kap,B in selected:
        E=2*p-2*k+2*kap;De=p-kap-E//2
        if E<2 or De<3*E//2+6:continue
        kind,m,y0,v1,v2=recipe(p,k,kap,B);cs['classes']+=1
        for _ in range(3):
            W=D['word'](p,k,kap,B);cs['words']+=1
            for t,d in enumerate(W.d):
                path=[(t+2+s)%k for s in range(k-3)]
                Q=N['rz2'](path,W.a,W.b,v1,v2) if kind=='P' else N['rz'](path,W.a,W.b,v1,v2)
                y=sum(W.d[q] for q in Q);sl,sh=N['check_word_type'](W,t,Q,y,m)
                l,lc=N['arcs'](W,Q);lt,lct=N['arcs'](W,Q|{t})
                assert l==(y+B)//2+1 and lc==(W.A-y)//2+1
                assert lt==(y+d+B)//2+1 and lct==(W.A-y-d)//2+1
                if max(W.single_lo[t],sl)>min(W.single_hi[t],sh):cs['empty_actual_seed']+=1
                cs['configurations']+=1
    print(json.dumps({'constructive':cs}),flush=True)
    print(json.dumps({'seconds':round(time.time()-tt,2),'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
if __name__ == '__main__':
    main()
