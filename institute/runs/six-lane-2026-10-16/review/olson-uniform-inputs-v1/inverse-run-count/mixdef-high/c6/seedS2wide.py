#!/usr/bin/env python3
"""[F] Controls of proof-S2wide.md, uniform all-single-letter g>=B>=2, kappa<=p-3.
Default recipe: m=ceil(kappa/2), y=g+c, c=1 if m-g odd else 2, mixed aligned pairs/singles.
Exceptions (Delta,h)=(3,0),(3,2),(4,1),(5,0): m=y=g aligned singles; (3,4): one pair + g-2 singles, m=g-1,y=g.
Check availability, genericity outside the five exceptional families, exact seed table inside them, quality/no-wrap/P2/PIN.
Then build all target configurations in 66 sampled/pinned classes, 3 layouts. No residue or group-avoider assertion is made by controls.
"""
import json,random,time,resource
GUARD="if __name__ == '__main__':\n    main()"
N={'__name__':'replayLB_lib'}
exec(compile(open('replayLB.py').read().replace(GUARD,''),'replayLB.py','exec'),N)
EXCEPT={(3,0),(3,2),(3,4),(4,1),(5,0)}
TABLE={(3,0):{1:(0,1),-1:(-1,0)},(3,2):{1:(0,0),-1:(-1,0)},(3,4):{1:(0,0),-1:(-1,0)},(4,1):{1:(0,1),-1:(-1,0)},(5,0):{1:(-1,2),-1:(-2,1)}}
def prime(p):return p>1 and all(p%d for d in range(2,int(p**.5)+1))
def recipe(p,g,B):
    Delta=p-g-B;h=g-B
    if (Delta,h) in EXCEPT:
        if (Delta,h)==(3,4):return 'mix',g-1,g,g-2,1
        return 'single',g,g,g,0
    m=(g+B+1)//2;c=1 if (m-g)%2 else 2;y=g+c
    return 'mix',m,y,2*m-y,y-m

def main():
    start=time.time();st={'classes':0,'default':0,'exceptional':{},'omitting_exception_capacity_reject':0};pool=[]
    for p in range(7,402):
        if not prime(p):continue
        for B in range(2,(p-3)//2+1):
            for g in range(B,p-2-B):
                kappa=g+B;n=p+g;k=n+B;Delta=p-kappa;h=g-B
                kind,m,y,j1,j2=recipe(p,g,B)
                assert j1>=0 and j2>=0 and m==j1+j2 and y==j1+2*j2 and 2*m+2<=k
                if kind=='single':assert 2*m<=n-3
                else:assert 3*j2+2*j1<=n-B-4
                lam=lambda v,b:min(p-b+1,v+b-g,(v+B)//2+1)
                lc=lambda v,b:min(p-b+1,p-B-v+b,(p+g-v)//2+1)
                U=lambda v,b:p-lc(v,b)
                generic=lambda v,b:lam(v,b)==(v+B)//2+1 and lc(v,b)==(p+g-v)//2+1
                if (Delta,h) not in EXCEPT:assert generic(y,m) and all(generic(y+d,m+1) for d in (1,-1));st['default']+=1
                else:
                    key=str((Delta,h));st['exceptional'][key]=st['exceptional'].get(key,0)+1
                    m0=(g+B+1)//2;c0=1 if (m0-g)%2 else 2;y0=g+c0
                    if m0+y0>n-B-4:st['omitting_exception_capacity_reject']+=1
                seeds={}
                for d in (1,-1):
                    sl=lam(y+d,m+1)-U(y,m);sh=U(y+d,m+1)-lam(y,m)
                    if (Delta,h) in EXCEPT:assert (sl,sh)==TABLE[(Delta,h)][d]
                    assert 2*sl>=d-Delta+2 and 2*sh<=d+Delta-2
                    L1,U1=lam(d,1),U(d,1)
                    assert L1-sh>-p and U1-sl<p
                    seeds[d]=(max(L1,sl),min(U1,sh))
                if all(a<=b for a,b in seeds.values()):
                    for d1 in (1,-1):
                        for d2 in (1,-1):
                            for mm in (1,2):
                                assert seeds[d1][0]+seeds[d2][0]>=1-lc(d1+d2,mm)
                                assert seeds[d1][1]+seeds[d2][1]<=p+lam(d1+d2,mm)-1
                    assert all(b-lam(d,1)<=p-1 for d,(a,b) in seeds.items())
                st['classes']+=1
                if p<=97:pool.append((p,g,B))
    print(json.dumps({'arithmetic':st}),flush=True)
    rnd=random.Random(192238)
    chosen=rnd.sample(pool,60)+[(7,2,2),(11,3,3),(11,4,4),(13,6,4),(11,6,2),(43,32,8)]
    # Correct pinned recipes are validated against the theorem domain before construction.
    chosen=[t for t in chosen if t[1]>=t[2]>=2 and sum(t[1:])<=t[0]-3]
    cs={'classes':len(chosen),'words':0,'configurations':0,'empty_actual_seed':0}
    for p,g,B in chosen:
        kind,m,y,j1,j2=recipe(p,g,B)
        for layout in range(3):
            W=N['word_from'](p,g,B,layout);cs['words']+=1
            for t in range(W.k):
                path=[(t+2+s)%W.k for s in range(W.k-3)]
                Q=N['rz'](path,W.a,W.b,0,m) if kind=='single' else N['rz2'](path,W.a,W.b,j1,j2)
                sl,sh=N['check_word_type'](W,t,Q,y,m)
                if max(W.single_lo[t],sl)>min(W.single_hi[t],sh):cs['empty_actual_seed']+=1
                cs['configurations']+=1
    print(json.dumps({'constructive':cs}),flush=True)
    print(json.dumps({'seconds':round(time.time()-start,2),'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
if __name__ == '__main__':
    main()
