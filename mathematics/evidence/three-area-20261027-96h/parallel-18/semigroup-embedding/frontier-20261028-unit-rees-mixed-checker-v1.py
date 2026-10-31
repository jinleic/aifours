#!/usr/bin/env python3
"""Exact finite and bounded checks for a Rees semigroup over an acted band.

The finite subsemigroup is exhaustively checked.  Infinite Bic components are
checked only on the stated bounded labels/contexts and are never truncated
when multiplying. No external files, library, network or randomness.
"""
from itertools import product


def need(ok, why):
    if not ok:
        raise ValueError(why)


def bm(a,b):
    if a is None: return b
    if b is None: return a
    return (a[0],b[1])


def flip(b,h):
    if b is None or h==0: return b
    return (1-b[0],1-b[1])


def bicyc(a,b):
    i,j=a; k,l=b
    return (i+max(k-j,0),l+max(j-k,0))


def am(a,b):
    x,e,h=a; y,f,k=b
    return (bicyc(x,y),bm(e,flip(f,h)),(h+k)%2)


def sand(lam,j):
    return ((0,0),None,int(lam==1 and j==1))


def sm(s,t):
    i,a,lam=s; j,b,mu=t
    return (i,am(am(a,sand(lam,j)),b),mu)


def idem(s):
    return sm(s,s)==s


def actor(s):
    i,(x,e,h),lam=s
    return (i,x[0]-x[1],h,lam)


def alpha(beta,shift):
    index,e=beta; n,h=shift
    return (index+n,flip(e,h))


def bandmul(x,y):
    return (max(x[0],y[0]),bm(x[1],y[1]))


def beta(s):
    i,(x,e,h),lam=s
    return (x[0],e)


def ctx(x,s,y):
    z=s if x is None else sm(x,s)
    return z if y is None else sm(z,y)


def main():
    band=[None]+list(product(range(2),repeat=2))
    finite=[(i,((0,0),e,h),lam) for i,e,h,lam in product(range(2),band,range(2),range(2))]
    bounded=[(i,(xy,e,h),lam) for i,xy,e,h,lam in product(range(2),product(range(2),repeat=2),band,range(2),range(2))]
    need(len(finite)==40 and len(bounded)==160, 'size')
    fset=set(finite)
    need(all(sm(a,b) in fset for a,b in product(finite,repeat=2)), 'finite closure')
    need(all(sm(sm(a,b),c)==sm(a,sm(b,c)) for a,b,c in product(finite,repeat=3)), 'finite associativity')
    E=[s for s in finite if idem(s)]
    need(all(any(sm(sm(a,b),a)==a and sm(sm(b,a),b)==b for b in finite) for a in finite), 'finite regularity')
    nonclosed=next(((e,f,sm(e,f)) for e,f in product(E,repeat=2) if not idem(sm(e,f))),None)
    need(nonclosed is not None, 'expected nonorthodox')
    noncommuting_corner=None
    for e in E:
        corner={sm(sm(e,s),e) for s in finite}
        ec=[x for x in corner if idem(x)]
        need(all(idem(sm(x,y)) for x,y in product(ec,repeat=2)), 'local orthodox')
        need(all(sm(sm(sm(sm(x,y),x),z),x)==sm(sm(sm(x,y),z),x)
                 for x,y,z in product(ec,repeat=3)), 'local regular')
        if noncommuting_corner is None:
            pair=next(((x,y) for x,y in product(ec,repeat=2) if sm(x,y)!=sm(y,x)),None)
            if pair is not None: noncommuting_corner=(e,pair)
    need(noncommuting_corner is not None, 'expected local non-inverse')

    # All finite-source contexts, including independent absent whole factors.
    contexts=[None]+finite
    sig={s:bytes(idem(ctx(x,s,y)) for x,y in product(contexts,repeat=2)) for s in finite}
    need(all((sig[s]==sig[t])==(actor(s)==actor(t)) for s,t in product(finite,repeat=2)), 'finite actual tau')
    need(all((actor(s)[1]==0 and actor(s)[2]==int(s[2]==1 and s[0]==1))==idem(s)
             for s in finite), 'finite actor purity')

    # Exact physical coefficient law, with source p_{lambda,j} in actor weight.
    def physical(s,t,wrong=False):
        i,(x,e,h),lam=s; j,(y,f,k),mu=t
        weight=(x[0]-x[1], (h+int(lam==1 and j==1))%2)
        if wrong: weight=(weight[0],h)
        return bandmul(beta(s),alpha(beta(t),weight))
    need(all(beta(sm(s,t))==physical(s,t) for s,t in product(bounded,repeat=2)), 'band host law')
    need(len({(beta(s),actor(s)) for s in bounded})==len(bounded), 'bounded injection')
    wrong=sum(beta(sm(s,t))!=physical(s,t,True) for s,t in product(bounded,repeat=2))
    need(wrong>0,'missing sandwich-action mutation')

    # Bounded subset of the infinite source: exact idempotent and R/L tests.
    Eb=[s for s in bounded if idem(s)]
    same=[(e,f) for e,f in product(Eb,repeat=2) if e!=f and actor(e)==actor(f)]
    rp=[(e,f) for e,f in same if sm(e,f)==f and sm(f,e)==e]
    lp=[(e,f) for e,f in same if sm(e,f)==e and sm(f,e)==f]
    need(rp and lp and all(beta(e)!=beta(f) for e,f in rp+lp), 'bounded R/L')
    p=((0,1),None,0)
    q=((1,0),None,0)
    one=((0,0),None,0)
    need(am(p,q)==one and am(q,p)!=one,'bicyclic non-group')

    print('finite_source=40 finite_idempotents=',len(E),' finite_actor_classes=',len({actor(s) for s in finite}),sep='')
    print('finite_complete_contexts=1681 nonclosed_E_witness=',nonclosed,sep='')
    print('PASS finite associativity, regularity, nonorthodox, locally_r, local_noninverse, actual_tau, pure_actor')
    print('bounded_infinite_labels=',len(bounded),' same_actor_idempotent_pairs=',len(same),
          ' R_pairs=',len(rp),' L_pairs=',len(lp),sep='')
    print('PASS bounded host law/injection/R-L; Bic p*q=1!=q*p')
    print('CONTROL omitted-sandwich-action mismatches=',wrong,sep='')
    print('LIMIT: finite source fully checked; infinite source needs universal written argument')


if __name__=='__main__':
    main()
