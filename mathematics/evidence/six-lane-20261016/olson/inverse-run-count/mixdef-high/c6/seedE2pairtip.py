#!/usr/bin/env python3
"""[F] Controls for proof-E2pairtip.md: E2,Delta0=3,g-B>=15,B>=1; ordinary aligned pairs and singles.
All target weights -3..3. Mutation permits nonordinary aligned runs, falsifying the fixed mass when it selects them.
"""
import random,json,time,resource
GUARD="if __name__ == '__main__':\n    main()"
D={'__name__':'defect_prefix_lib'}
exec(compile(open('defect_prefix.py').read().replace(GUARD,''),'defect_prefix.py','exec'),D)
N=D['N'];rnd=random.Random(195152)
def prime(p):return p>1 and all(p%d for d in range(2,int(p**.5)+1))
def config(W,t,j1,j2,mut=False):
    path=[(t+2+s)%W.k for s in range(W.k-3)]
    segs=N['intervals'](path,lambda q:W.b[q]==0 and (mut or W.a[q]==1))
    np=[];need=j2
    for seg in segs:v=min(need,(len(seg)+1)//3);np.append(v);need-=v
    assert need==0
    Q=set()
    for seg,z in zip(segs,np):
        for u in range(z):Q.update(seg[3*u:3*u+2])
    need=j1
    for seg,z in zip(segs,np):
        for pos in range(3*z,len(seg),2):
            if need==0:break
            Q.add(seg[pos]);need-=1
    assert need==0
    return Q

def main():
    tt=time.time();st={'classes':0,'target_types':0};pool=[]
    for p in range(7,402):
        if not prime(p):continue
        for B in range(1,(p-19)//2+1):
            g=p-4-B;h=g-B
            if h<15:continue
            m=(p-3)//2;y=g+2;j1=B-1;j2=(h+3)//2
            assert m==j1+j2 and y==j1+2*j2 and 3*j2+2*j1<=2*g-5
            kap=p-4;A=p+g+1
            lam=lambda v,b:min(p-b+1,v+b-g,(v+B)//2+1)
            lc=lambda v,b:min(p-b+1,A-kap-v+b,(A-v)//2+1)
            U=lambda v,b:p-lc(v,b)
            gen=lambda v,b:lam(v,b)==(v+B)//2+1 and lc(v,b)==(A-v)//2+1
            assert gen(y,m)
            for d in range(-3,4):
                assert gen(y+d,m+1)
                sl=lam(y+d,m+1)-U(y,m);sh=U(y+d,m+1)-lam(y,m)
                assert 2*sl>=d-1 and 2*sh<=d+1
                assert lam(d,1)-sh>-p and U(d,1)-sl<p
                st['target_types']+=1
            st['classes']+=1
            if p<=101:pool.append((p,g,B))
    print(json.dumps({'arithmetic':st}),flush=True)
    chosen=rnd.sample(pool,min(56,len(pool)))+[(23,18,1),(23,17,2),(31,23,4),(43,31,8)]
    cs={'classes':len(chosen),'words':0,'target_configurations':0,'mutation_mass_reject':0}
    for p,g,B in chosen:
        k=2*p-5;kap=p-4;m=(p-3)//2;y=g+2;j1=B-1;j2=(g-B+3)//2
        for _ in range(3):
            W=D['word'](p,k,kap,B);cs['words']+=1
            for t,d in enumerate(W.d):
                Q=config(W,t,j1,j2);sl,sh=N['check_word_type'](W,t,Q,y,m)
                assert 2*sl>=d-1 and 2*sh<=d+1
                bad=config(W,t,j1,j2,True)
                if sum(W.d[q] for q in bad)!=y:cs['mutation_mass_reject']+=1
                cs['target_configurations']+=1
    print(json.dumps({'constructive':cs}),flush=True)
    print(json.dumps({'seconds':round(time.time()-tt,2),'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
if __name__ == '__main__':
    main()
