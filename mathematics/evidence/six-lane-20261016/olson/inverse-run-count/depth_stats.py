import random, sys
from collections import Counter, defaultdict
from hw import windows
from chainlift_test import run, chain_lifts
from sample_famtest import inherited, has_full
p=int(sys.argv[1]); T=int(sys.argv[2]); seed=int(sys.argv[3])
rng=random.Random(seed); N=4*p-2; done=0
worst=defaultdict(int); cnt=Counter()
while done<T:
    k=rng.randint(p+1,min(2*p-3,15)); R=rng.randint(k,2*p-3)
    if R+2*k<=4*p-3: continue   # high kappa only
    F=N-R
    if F<k or (F-k)%2: continue
    c=sorted(rng.sample(range(1,R),k-1)); r=[y-x for x,y in zip([0]+c,c+[R])]
    l=[1]*k
    for _ in range((F-k)//2): l[rng.randrange(k)]+=2
    a=list(r); b=[0]*k
    if not inherited(a,b,l,p) or has_full(a,b,l,p): continue
    done+=1
    W=windows(a,b,l,p); H=sum(v//2 for v in l); kappa=p-1-H
    sols=run(p,1,a,b,l,1000,1000)
    for phi in sols:
        x,tot,amb=chain_lifts(p,a,b,l,phi,W,0)
        bh=[2*x[t]-a[t] for t in range(k)]
        md=max([-v for v in bh if v<=0],default=0)
        key=(k,R,kappa)
        worst[key]=max(worst[key],md); cnt[key]+=1
for key in sorted(worst): print('k,R,kappa',key,'max depth',worst[key],'2p-R+1=',2*p-key[1]+1,'n',cnt[key])
