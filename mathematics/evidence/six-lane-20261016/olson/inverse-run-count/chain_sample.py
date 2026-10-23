import random, sys, json
from collections import Counter
from hw import windows
from chainlift_test import run, chain_lifts, in_win
from sample_famtest import inherited, has_full
def chain_test(p,a,b,l,sols):
    k=len(a); W=windows(a,b,l,p)
    out=Counter(); fails=[]
    for phi in sols:
        lifts,tot,amb=chain_lifts(p,a,b,l,phi,W,0)
        bh=[2*lifts[t]-(a[t]-b[t]) for t in range(k)]
        out[('tot',tot)]+=1; out[('minbh',min(bh))]+=1; out[('amb',amb>0)]+=1
        Z=[t for t in range(k) if bh[t]<=0]
        ok=False
        if 0<len(Z)<k:
            P=sum(1<<t for t in Z); s=sum(lifts[t] for t in Z)
            lo,hi=W[P]
            if lo<=hi and lo<=s<=hi: ok=True
        out[('Zkill',ok)]+=1
        if not ok and len(fails)<3: fails.append((phi,lifts,bh))
    return out,fails
if __name__=='__main__':
    p=int(sys.argv[1]); T=int(sys.argv[2]); seed=int(sys.argv[3]); const=int(sys.argv[4]); allodd=int(sys.argv[5])
    rng=random.Random(seed); N=4*p-2; done=0; agg=Counter(); allfails=[]
    while done<T:
        k=rng.randint(p+1,min(2*p-3,15))
        # regime B: choose R in [k, 2p-3]
        R=rng.randint(k,2*p-3); F=N-R
        if F<k: continue
        # rotation composition of R into k parts, reflection comp of F into k parts
        def comp(n,k):
            c=sorted(rng.sample(range(1,n),k-1)); return [y-x for x,y in zip([0]+c,c+[n])]
        r=comp(R,k); l=comp(F,k)
        if allodd and any(x%2==0 for x in l): continue
        if const: a=list(r); b=[0]*k
        else:
            a=[rng.randint(0,x) for x in r]; b=[x-y for x,y in zip(r,a)]
            if sum(a)<sum(b): a,b=b,a
        if not inherited(a,b,l,p): continue
        if has_full(a,b,l,p): continue
        sols=run(p,1,a,b,l,3000,3000)
        done+=1
        if not sols: agg['interval_certified']+=1; continue
        out,fails=chain_test(p,a,b,l,sols)
        agg.update(out)
        if fails: allfails.append((a,b,l,fails[0]))
    print(dict(agg)); 
    for f in allfails[:5]: print(f)
