#!/usr/bin/env python3
"""[F] Controls of proof-S2E.md. E even>=2, g>=B>=2, Delta0>=E+3, h+2Delta0>=3E+12+epsilon.
Recipe m=ceil((kappa+E)/2), y0=g+E+2, j1=2m-y0, j2=y0-m. This is a quality-seed recipe, not an avoider census.
"""
import random,json,time,resource
GUARD="if __name__ == '__main__':\n    main()"
D={'__name__':'defect_prefix_lib'}
exec(compile(open('defect_prefix.py').read().replace(GUARD,''),'defect_prefix.py','exec'),D)
N=D['N'];rnd=random.Random(193717)
def prime(p):return p>1 and all(p%q for q in range(2,int(p**.5)+1))
def cases(P):
    for p in range(7,P+1):
        if not prime(p):continue
        for E in range(2,p-3,2):
            for B in range(2,(p-3)//2+1):
                for g in range(B,p-2-B-E//2):
                    Delta=p-g-B-E//2;ep=(g+B+E)%2
                    if Delta<E+3 or g-B+2*Delta<3*E+12+ep:continue
                    yield p,E,g,B

def main():
    tt=time.time();st={'classes':0,'target_types':0,'arcs':0};pool=[]
    for p,E,g,B in cases(101):
        kap=g+B;Delta=p-kap-E//2;k=p+kap-E//2;A=p+g+E//2;delta=p-g-E//2
        m=(kap+E+1)//2;ep=2*m-kap-E;y0=g+E+2;j1=2*m-y0;j2=y0-m
        assert j1==B-2+ep and min(j1,j2)>=0
        assert 3*j2+2*j1<=k-2*B-4
        X=y0+2*m;Z=y0-2*m
        assert 2*g+B+E+2<=X<=2*p-B-E-3
        assert E+3-delta<=Z<=delta-2*B-2
        lam=lambda v,b:min(p-b+1,v+b-g,(v+B)//2+1)
        lc=lambda v,b:min(p-b+1,A-kap-v+b,(A-v)//2+1)
        U=lambda v,b:p-lc(v,b)
        gen=lambda v,b:lam(v,b)==(v+B)//2+1 and lc(v,b)==(A-v)//2+1
        for d in range(-min(B,E+1),E+2):
            et=abs(d)-1 if d else 1;er=E-et
            for y in range(y0-er,y0+er+1):
                assert gen(y,m) and gen(y+d,m+1)
                sl=lam(y+d,m+1)-U(y,m);sh=U(y+d,m+1)-lam(y,m)
                assert 2*sl>=d-Delta+2 and 2*sh<=d+Delta-2
                assert lam(d,1)-sh>-p and U(d,1)-sl<p
                st['target_types']+=1;st['arcs']+=4
        st['classes']+=1;pool.append((p,E,g,B))
    print(json.dumps({'arithmetic':st}),flush=True)
    chosen=rnd.sample(pool,min(36,len(pool)))+[(p,2,p-16,10) for p in (37,41,61,97)]
    cs={'classes':len(chosen),'words':0,'configurations':0,'empty_actual_seed':0}
    for p,E,g,B in chosen:
        kap=g+B;k=p+kap-E//2;m=(kap+E+1)//2;y0=g+E+2;j1=2*m-y0;j2=y0-m
        for lay in range(3):
            W=D['word'](p,k,kap,B);cs['words']+=1
            for t,d in enumerate(W.d):
                path=[(t+2+s)%k for s in range(k-3)];Q=N['rz2'](path,W.a,W.b,j1,j2);y=sum(W.d[q] for q in Q)
                et=abs(d)-1 if d else 1
                assert y0<=y<=y0+E-et
                sl,sh=N['check_word_type'](W,t,Q,y,m)
                l,lc=N['arcs'](W,Q);lt,lct=N['arcs'](W,Q|{t})
                assert l==(y+B)//2+1 and lc==(W.A-y)//2+1
                assert lt==(y+d+B)//2+1 and lct==(W.A-y-d)//2+1
                if max(W.single_lo[t],sl)>min(W.single_hi[t],sh):cs['empty_actual_seed']+=1
                cs['configurations']+=1
    print(json.dumps({'constructive':cs}),flush=True)
    print(json.dumps({'seconds':round(time.time()-tt,2),'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
if __name__ == '__main__':
    main()
