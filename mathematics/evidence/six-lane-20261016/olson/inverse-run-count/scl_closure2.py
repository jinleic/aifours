import random, sys
from collections import Counter
from scl_closure import tables
from sample_famtest import inherited, has_full
def closure2(a,b,l,p):
    k=len(a); U,L=tables(a,b,l,p)
    nonempty={P for P in U if U[P]+L[P]>=0}
    full={P for P in U if U[P]+L[P]+1>=p}
    derived=set()
    for P in sorted(U,key=lambda P:bin(P).count('1')):
        if P not in nonempty or P in full: continue
        if bin(P).count('1')==1: derived.add(P); continue
        # all splits P=Q1|Q2, Q1<Q2 to avoid duplicates
        Q1=(P-1)&P; ok=False
        while Q1>0:
            Q2=P^Q1
            if Q1<Q2 and Q1 in derived and Q2 in derived:
                if U[Q1]+U[Q2]+L[P]>=-2 and L[Q1]+L[Q2]+U[P]>=p-2: ok=True; break
            Q1=(Q1-1)&P
        if ok: derived.add(P)
    bad=[P for P in nonempty if P not in full and P not in derived]
    return bad
if __name__=='__main__':
    p=int(sys.argv[1]); T=int(sys.argv[2]); seed=int(sys.argv[3]); kmin=int(sys.argv[4]); kmax=int(sys.argv[5])
    rng=random.Random(seed); N=4*p-2; st=Counter(); ex=[]; done=0
    while done<T:
        k=rng.randint(kmin,kmax)
        R=rng.randint(k,2*p-3)
        F=N-R
        if F<k: continue
        def comp(n,k):
            c=sorted(rng.sample(range(1,n),k-1)); return [y-x for x,y in zip([0]+c,c+[n])]
        r=comp(R,k); l=comp(F,k)
        a=[rng.randint(0,x) for x in r]; b=[x-y for x,y in zip(r,a)]
        if sum(a)<sum(b): a,b=b,a
        if not inherited(a,b,l,p) or has_full(a,b,l,p): continue
        done+=1
        bad=closure2(a,b,l,p)
        st['data']+=1; st['bad']+=len(bad); st['data_with_bad']+=(len(bad)>0)
        if bad and len(ex)<4: ex.append((a,b,l,bad[:6]))
    print(dict(st))
    for e in ex: print(e)
