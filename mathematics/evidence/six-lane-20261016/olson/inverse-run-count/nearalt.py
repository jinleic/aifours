import sys, random
from collections import Counter
from hw import windows
from chainlift_test import run, chain_lifts
p=int(sys.argv[1]); k=int(sys.argv[2]); seed=int(sys.argv[3]); trials=int(sys.argv[4])
rng=random.Random(seed); N=4*p-2; R=k; F=N-R
agg=Counter()
for _ in range(trials):
    # reflection runs: k runs summing to F, mostly 1's, odd lengths
    extra=F-k
    l=[1]*k
    while extra>0:
        i=rng.randrange(k); add=2 if extra>=2 else 1
        l[i]+=add; extra-=add
    a=[1]*k; b=[0]*k
    H=sum(x//2 for x in l)
    if H>p-1: continue
    W=windows(a,b,l,p)
    if any(hi-lo+1>=p for lo,hi in W.values()): agg['full']+=1; continue
    sols=run(p,1,a,b,l,500,500)
    agg['data']+=1; agg['nsols']+=len(sols)
    for phi in sols:
        x,tot,amb=chain_lifts(p,a,b,l,phi,W,0)
        bh=[2*x[t]-1 for t in range(k)]
        agg[('minbh',min(bh))]+=1; agg[('tot',tot)]+=1
print(p,k,dict(agg))
