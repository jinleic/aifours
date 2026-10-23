import random, sys
from collections import Counter
from hw import windows
from chainlift_test import run, chain_lifts
from sample_famtest import inherited, has_full
def margins(p,a,b,l,sols):
    k=len(a); W=windows(a,b,l,p); A=sum(a); B=sum(b); R=A+B
    out=Counter()
    for phi in sols:
        lifts,tot,amb=chain_lifts(p,a,b,l,phi,W,0)
        bh=[2*lifts[t]-(a[t]-b[t]) for t in range(k)]
        Z=[t for t in range(k) if bh[t]<=0]
        BZ=sum(bh[t] for t in Z)
        out[('BZ+A',BZ+A)]+=1
        out[('nZ',len(Z))]+=1
    return out
if __name__=='__main__':
    p=int(sys.argv[1]); T=int(sys.argv[2]); seed=int(sys.argv[3]); const=int(sys.argv[4])
    rng=random.Random(seed); N=4*p-2; done=0; agg=Counter()
    while done<T:
        k=rng.randint(p+1,min(2*p-3,15)); R=rng.randint(k,2*p-3); F=N-R
        if F<k: continue
        def comp(n,k):
            c=sorted(rng.sample(range(1,n),k-1)); return [y-x for x,y in zip([0]+c,c+[n])]
        r=comp(R,k); l=comp(F,k)
        if const: a=list(r); b=[0]*k
        else:
            a=[rng.randint(0,x) for x in r]; b=[x-y for x,y in zip(r,a)]
            if sum(a)<sum(b): a,b=b,a
        if not inherited(a,b,l,p) or has_full(a,b,l,p): continue
        sols=run(p,1,a,b,l,3000,3000); done+=1
        if sols: agg.update(margins(p,a,b,l,sols))
    print(sorted((k,v) for k,v in agg.items() if k[0]=='BZ+A'))
    print(sorted((k,v) for k,v in agg.items() if k[0]=='nZ'))
