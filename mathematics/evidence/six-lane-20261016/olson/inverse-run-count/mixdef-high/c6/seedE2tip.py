#!/usr/bin/env python3
"""[F] Controls for proof-E2tip.md: E=2,Delta0=3,g>=3,B>=g+3, kappa=p-4.
Only ordinary singleton aligned/anti RUNS enter Q. All possible target weights -3..3 are checked.
Literal-word control uses independent slow_lambda; mutation permits nonordinary runs in the fixed-mass construction.
"""
import random,json,time,resource
GUARD="if __name__ == '__main__':\n    main()"
D={'__name__':'defect_prefix_lib'}
exec(compile(open('defect_prefix.py').read().replace(GUARD,''),'defect_prefix.py','exec'),D)
N=D['N'];rnd=random.Random(194847)
def prime(p):return p>1 and all(p%q for q in range(2,int(p**.5)+1))
def ordinary_rz(W,t,i,j,mut=False):
    path=[(t+2+s)%W.k for s in range(W.k-3)]
    ai=lambda q:W.a[q]==0 and (mut or W.b[q]==1)
    al=lambda q:W.b[q]==0 and (mut or W.a[q]==1)
    anti=[q for seg in N['intervals'](path,ai) for q in seg[::2]]
    assert len(anti)>=i
    picked=set(anti[:i]);ban=set(picked)
    for z,q in enumerate(path):
        if q in picked:
            if z:ban.add(path[z-1])
            if z+1<len(path):ban.add(path[z+1])
    ap=[q for seg in N['intervals'](path,lambda q:al(q) and q not in ban) for q in seg[::2]]
    assert len(ap)>=j
    return picked|set(ap[:j])
def main():
    tt=time.time();st={'classes':0,'target_sign_types':0};pool=[]
    for p in range(13,402):
        if not prime(p):continue
        for g in range(3,(p-7)//2+1):
            B=p-4-g;kap=p-4;k=2*p-5;m=(p-3)//2;r=m-g;c=2 if r%2==0 else 3;y=g+c;i=(m-y)//2;j=(m+y)//2
            assert i>=0 and j>=0 and 2*m<=p+g-6 and (i==0 or 2*i<=B-7)
            lam=lambda v,b:min(p-b+1,v+b-g,(v+B)//2+1)
            lc=lambda v,b:min(p-b+1,p-B+1-v+b,(p+g+1-v)//2+1)
            # A-kappa=p-B+E/2=p-B+1; A=p+g+1.
            U=lambda v,b:p-lc(v,b)
            gen=lambda v,b:lam(v,b)==(v+B)//2+1 and lc(v,b)==(p+g+1-v)//2+1
            assert gen(y,m)
            for d in range(-3,4):
                assert gen(y+d,m+1)
                sl=lam(y+d,m+1)-U(y,m);sh=U(y+d,m+1)-lam(y,m)
                assert 2*sl>=d-1 and 2*sh<=d+1
                assert lam(d,1)-sh>-p and U(d,1)-sl<p
                st['target_sign_types']+=1
            st['classes']+=1
            if p<=101:pool.append((p,g,B))
    print(json.dumps({'arithmetic':st}),flush=True)
    chosen=rnd.sample(pool,min(56,len(pool)))+[(13,3,6),(17,3,10),(31,3,24),(43,7,32)]
    cs={'classes':len(chosen),'words':0,'target_configurations':0,'mutation_mass_reject':0}
    for p,g,B in chosen:
        kap=p-4;k=2*p-5;m=(p-3)//2;r=m-g;c=2 if r%2==0 else 3;y=g+c;i=(m-y)//2;j=(m+y)//2
        for _ in range(3):
            W=D['word'](p,k,kap,B);cs['words']+=1
            assert sum(a==1 and b==0 for a,b in zip(W.a,W.b))>=p+g-3
            assert sum(a==0 and b==1 for a,b in zip(W.a,W.b))>=B-4
            for t,d in enumerate(W.d):
                Q=ordinary_rz(W,t,i,j);sl,sh=N['check_word_type'](W,t,Q,y,m)
                assert 2*sl>=d-1 and 2*sh<=d+1
                bad=ordinary_rz(W,t,i,j,True)
                if sum(W.d[q] for q in bad)!=y:cs['mutation_mass_reject']+=1
                cs['target_configurations']+=1
    print(json.dumps({'constructive':cs}),flush=True)
    print(json.dumps({'seconds':round(time.time()-tt,2),'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
if __name__ == '__main__':
    main()
