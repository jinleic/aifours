#!/usr/bin/env python3
"""[F] Controls for the WRITTEN uniform mixed-single seed lemma (proof-RZwide.md).
Parameters: prime p>=7, g=kB>=1, B>=g+1, kappa=g+B<=p-3; E=0, n=p+g.
Recipe m=ceil(kappa/2), c=1 if m-g odd else 2, y=g+c, i=(m-y)/2, j=(m+y)/2.
Check RZ availability, all four generic arcs for both target signs, (QS), no wrap, P2 and PIN; primes through 401.
Literal configurations: 60 sampled classes through p=97 plus pinned small/large classes, 3 layouts, all target runs, independent
slow_lambda. Controls: forcing c=1 (parity) and replacing c=1 with c=3 (same parity; availability/genericity can fail).
"""
import json,random,time,resource
GUARD="if __name__ == '__main__':\n    main()"
N={"__name__":"replayLB_lib"}
exec(compile(open('replayLB.py').read().replace(GUARD,''),'replayLB.py','exec'),N)
def prime(p):return p>1 and all(p%d for d in range(2,int(p**.5)+1))
def params(p):
    for g in range(1,(p-4)//2+1):
        for B in range(g+1,p-2-g):yield p,g,B

def calc(p,g,B,c_override=None):
    kap=g+B;m=(kap+1)//2;c=(1 if (m-g)%2 else 2) if c_override is None else c_override;y=g+c
    return m,c,y,(m-y)//2,(m+y)//2

def generic(p,g,B,y,m):
    A=p+g;kap=g+B
    lam=min(p-m+1,y+m-g,(y+B)//2+1)
    lc=min(p-m+1,A-kap-y+m,(A-y)//2+1)
    return lam,lc,(lam==(y+B)//2+1 and lc==(A-y)//2+1)

def valid(p,g,B,m,c,y,i,j):
    return (m-y)%2==0 and i>=0 and j>=0 and (i==0 or 2*i<=B-3) and 2*m<=p+g-3 and 2*m+2<=p+g+B

def main():
    t=time.time();stat={'classes':0,'target_signs':0,'parity_mutation_reject':0,'c3_mutation_reject':0};sample=[]
    for p in range(7,402):
        if not prime(p):continue
        for p,g,B in params(p):
            m,c,y,i,j=calc(p,g,B);assert valid(p,g,B,m,c,y,i,j)
            l,lc,ok=generic(p,g,B,y,m);assert ok
            lam=lambda yy,mm:min(p-mm+1,yy+mm-g,(yy+B)//2+1)
            lamc=lambda yy,mm:min(p-mm+1,p-B-yy+mm,(p+g-yy)//2+1)
            seeds={}
            delta=p-g-B
            for d in (1,-1):
                lt,lct,ok2=generic(p,g,B,y+d,m+1);assert ok2
                sl=lt-p+lc;sh=p-lct-l
                assert 2*sl>=d-delta+2 and 2*sh<=d+delta-2
                L1=lam(d,1);U1=p-lamc(d,1)
                assert L1-sh>-p and U1-sl<p
                seeds[d]=(max(L1,sl),min(U1,sh));stat['target_signs']+=1
            # If an actual seed is empty the class is already excluded. Otherwise verify P2/PIN as an independent arithmetic control.
            if all(a<=b for a,b in seeds.values()):
                for d1 in (1,-1):
                    for d2 in (1,-1):
                        for mm in (1,2):
                            assert seeds[d1][0]+seeds[d2][0]>=1-lamc(d1+d2,mm)
                            assert seeds[d1][1]+seeds[d2][1]<=p+lam(d1+d2,mm)-1
                assert all(b-lam(d,1)<=p-1 for d,(a,b) in seeds.items())
            if (m-(g+1))%2:stat['parity_mutation_reject']+=1
            bad=False
            if c==1:
                mm,cc,yy,ii,jj=calc(p,g,B,3)
                bad=not valid(p,g,B,mm,cc,yy,ii,jj)
                if not bad:bad=not (generic(p,g,B,yy,mm)[2] and all(generic(p,g,B,yy+d,mm+1)[2] for d in (1,-1)))
            if bad:stat['c3_mutation_reject']+=1
            stat['classes']+=1
            if p<=97:sample.append((p,g,B))
    print(json.dumps({'arithmetic':stat}),flush=True)
    rnd=random.Random(191805);chosen=rnd.sample(sample,60)+[(7,1,2),(7,1,3),(11,2,5),(23,1,19),(29,1,25),(43,5,35)]
    cs={'classes':len(chosen),'words':0,'target_configurations':0,'empty_actual_seed':0}
    for p,g,B in chosen:
        m,c,y,i,j=calc(p,g,B)
        for layout in range(3):
            W=N['word_from'](p,g,B,layout);cs['words']+=1
            for q in range(W.k):
                path=[(q+2+s)%W.k for s in range(W.k-3)]
                Q=N['rz'](path,W.a,W.b,i,j)
                sl,sh=N['check_word_type'](W,q,Q,y,m)
                alo=max(W.single_lo[q],sl);bhi=min(W.single_hi[q],sh)
                if alo>bhi:cs['empty_actual_seed']+=1
                cs['target_configurations']+=1
    print(json.dumps({'constructive':cs}),flush=True)
    print(json.dumps({'seconds':round(time.time()-t,2),'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
if __name__ == '__main__':
    main()
