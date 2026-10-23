import sys, random
from collections import Counter
from hw import windows
from chainlift_test import run, chain_lifts
from margin6 import terms
p=int(sys.argv[1]); k=int(sys.argv[2]); seed=int(sys.argv[3]); trials=int(sys.argv[4]); R=int(sys.argv[5]) if len(sys.argv)>5 else k
rng=random.Random(seed); N=4*p-2; F=N-R
agg=Counter(); worst={}
for _ in range(trials):
    extra=F-k
    l=[1]*k
    while extra>0:
        i=rng.randrange(k); add=2 if extra>=2 else 1
        l[i]+=add; extra-=add
    r=[1]*k; ex=R-k
    while ex>0:
        i=rng.randrange(k); r[i]+=1; ex-=1
    a=list(r); b=[0]*k
    H=sum(x//2 for x in l)
    if H>p-1: continue
    W=windows(a,b,l,p)
    if any(hi-lo+1>=p for lo,hi in W.values()): agg['full']+=1; continue
    sols=run(p,1,a,b,l,500,500)
    agg['data']+=1; agg['nsols']+=len(sols)
    for phi in sols:
        x,tot,amb=chain_lifts(p,a,b,l,phi,W,0)
        bh=[2*x[t]-r[t] for t in range(k)]
        Z=[t for t in range(k) if bh[t]<=0]
        P=sum(1<<t for t in Z)
        e,L,U,m,beta,tau=terms(p,a,b,l,x,P)
        ok=max(L)<=e<=min(U)
        agg[('Zkill',ok)]+=1
        for i in range(3):
            worst['L%d'%i]=min(worst.get('L%d'%i,99),e-L[i]); worst['U%d'%i]=min(worst.get('U%d'%i,99),U[i]-e)
print(p,k,R,dict(agg),worst)
