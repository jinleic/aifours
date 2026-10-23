import random, sys
from collections import Counter
from hw import windows
from chainlift_test import run, chain_lifts
from sample_famtest import inherited, has_full
p=int(sys.argv[1]); T=int(sys.argv[2]); seed=int(sys.argv[3]); allodd=int(sys.argv[4])
rng=random.Random(seed); N=4*p-2; done=0; st=Counter(); ex=[]
while done<T:
    k=rng.randint(p+1,min(2*p-3,15)); R=rng.randint(k,2*p-3); F=N-R
    if F<k: continue
    c=sorted(rng.sample(range(1,R),k-1)); r=[y-x for x,y in zip([0]+c,c+[R])]
    if allodd:
        if (F-k)%2: continue
        l=[1]*k
        for _ in range((F-k)//2): l[rng.randrange(k)]+=2
    else:
        c2=sorted(rng.sample(range(1,F),k-1)); l=[y-x for x,y in zip([0]+c2,c2+[F])]
    a=list(r); b=[0]*k
    if not inherited(a,b,l,p) or has_full(a,b,l,p): continue
    done+=1
    W=windows(a,b,l,p)
    sols=run(p,1,a,b,l,1500,1500)
    for phi in sols:
        x,tot,amb=chain_lifts(p,a,b,l,phi,W,0)
        bh=[2*x[t]-a[t] for t in range(k)]
        SY=sum(v for v in bh if v>=1)
        st['heavy' if SY>2*(2*p-R) else 'light']+=1
        if SY>2*(2*p-R) and len(ex)<3: ex.append((a,l,phi,bh))
print(dict(st)); 
for e in ex: print(e)
