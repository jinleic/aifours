import random, sys
from collections import Counter, defaultdict
from hw import windows
from chainlift_test import run, chain_lifts
from sample_famtest import inherited, has_full
def terms(p,a,b,l,x,P):
    k=len(a); A=sum(a); B=sum(b); R=A+B; H=sum(v//2 for v in l); kappa=p-1-H
    z=[(P>>i)&1 for i in range(k)]
    f=[1 if z[j]!=z[(j+1)%k] else 0 for j in range(k)]
    m=sum(f)//2; beta=sum(1 for j in range(k) if f[j] and l[j]%2==0)
    Ep=sum(a[i] if z[i] else b[i] for i in range(k)); Em=R-Ep
    d=[a[i]-b[i] for i in range(k)]; DP=sum(d[i] for i in range(k) if z[i]); nP=sum(z)
    e=sum(1-(2*x[i]-d[i]) for i in range(k) if z[i]); tau=nP-DP
    L=[tau+2*(kappa-B)+2+2*beta-2*m, nP-B+(Ep%2), nP+DP-2*p+2*m]
    U=[nP+A-(Em%2), nP+2*A-DP-2*kappa-2+2*m-2*beta, nP+2*p-2*m+DP]
    return e,L,U,m,beta,tau
if __name__=='__main__':
    p=int(sys.argv[1]); T=int(sys.argv[2]); seed=int(sys.argv[3]); const=int(sys.argv[4])
    rng=random.Random(seed); N=4*p-2; done=0
    minmarg=defaultdict(lambda:10**9); binding=Counter(); killed=Counter()
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
        sols=run(p,1,a,b,l,2000,2000); done+=1
        W=windows(a,b,l,p)
        for phi in sols:
            x,tot,amb=chain_lifts(p,a,b,l,phi,W,0)
            bh=[2*x[t]-(a[t]-b[t]) for t in range(k)]
            Z=[t for t in range(k) if bh[t]<=0]
            if not (0<len(Z)<k): killed['Zdegenerate']+=1; continue
            P=sum(1<<t for t in Z)
            e,L,U,m,beta,tau=terms(p,a,b,l,x,P)
            ok=max(L)<=e<=min(U)
            killed[ok]+=1
            for i in range(3):
                minmarg['L%d'%i]=min(minmarg['L%d'%i],e-L[i]); minmarg['U%d'%i]=min(minmarg['U%d'%i],U[i]-e)
            binding['Lbind%d'%max(range(3),key=lambda i:L[i])]+=1
            binding['Ubind%d'%min(range(3),key=lambda i:U[i])]+=1
    print(dict(killed)); print(dict(minmarg)); print(dict(binding))
