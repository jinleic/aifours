import random, sys
from collections import Counter
from hw import windows
from chainlift_test import run, chain_lifts
from sample_famtest import inherited, has_full
def single_lifts(p,a,b,l,phi,W):
    k=len(a); xs=[]
    for t in range(k):
        lo,hi=W[1<<t]
        if lo>hi: xs.append(None); continue
        xs.append(hi+1+((phi[t]-(hi+1))%p))
    return xs
if __name__=='__main__':
    p=int(sys.argv[1]); T=int(sys.argv[2]); seed=int(sys.argv[3]); const=int(sys.argv[4]); fam=int(sys.argv[5]) if len(sys.argv)>5 else 1
    rng=random.Random(seed); N=4*p-2; done=0; agg=Counter()
    while done<T:
        k=rng.randint(p+1,min(2*p-3,14)); R=rng.randint(k,2*p-3); F=N-R
        if F<k: continue
        def comp(n,k):
            c=sorted(rng.sample(range(1,n),k-1)); return [y-x for x,y in zip([0]+c,c+[n])]
        r=comp(R,k); l=comp(F,k)
        if const: a=list(r); b=[0]*k
        else:
            a=[rng.randint(0,x) for x in r]; b=[x-y for x,y in zip(r,a)]
            if sum(a)<sum(b): a,b=b,a
        if not inherited(a,b,l,p) or has_full(a,b,l,p): continue
        sols=run(p,fam,a,b,l,2000,2000); done+=1
        W=windows(a,b,l,p)
        for phi in sols:
            xc,tot,amb=chain_lifts(p,a,b,l,phi,W,0)
            xs=single_lifts(p,a,b,l,phi,W)
            if None in xs: agg['single_empty']+=1; continue
            agg['jumps=%d'%sum(1 for t in range(k) if xc[t]!=xs[t])]+=1
            agg['sum_single=%d'%(sum(xs)//p if sum(xs)%p==0 else -999)]+=1
    print(dict(agg))
