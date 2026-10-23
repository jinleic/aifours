import random, sys
from collections import Counter
from scl_closure2 import closure2
from scl_closure import tables
from sample_famtest import inherited, has_full
if __name__=='__main__':
    p=int(sys.argv[1]); T=int(sys.argv[2]); seed=int(sys.argv[3]); const=int(sys.argv[4])
    rng=random.Random(seed); N=4*p-2; st=Counter(); ex=[]; done=0
    while done<T:
        k=rng.randint(p+1,min(2*p-3,13))
        R=rng.randint(k,2*p-3)
        F=N-R
        if F<k: continue
        def comp(n,k):
            c=sorted(rng.sample(range(1,n),k-1)); return [y-x for x,y in zip([0]+c,c+[n])]
        r=comp(R,k); l=comp(F,k)
        if const: a=list(r); b=[0]*k
        else:
            a=[rng.randint(0,x) for x in r]; b=[x-y for x,y in zip(r,a)]
            if sum(a)<sum(b): a,b=b,a
        H=sum(x//2 for x in l); kappa=p-1-H
        if not inherited(a,b,l,p) or sum(b)>kappa or has_full(a,b,l,p): continue
        done+=1
        bad=closure2(a,b,l,p)
        st['data']+=1; st['bad']+=len(bad); st['data_with_bad']+=(len(bad)>0)
        if bad and len(ex)<6: ex.append((a,b,l,[bin(P) for P in bad[:4]]))
    print(dict(st))
    for e in ex: print(e)
