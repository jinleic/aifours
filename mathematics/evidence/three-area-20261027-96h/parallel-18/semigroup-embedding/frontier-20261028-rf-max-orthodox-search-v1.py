#!/usr/bin/env python3
"""Bounded exact search for RF versus fibre maximum in orthodox local monoids.

Examines local monoids of (rectangular-band-with-1 x powerset semilattice)
semidirect C2 or C3. All elements and natural-order witnesses in each finite
monoid are enumerated; this is not a classification of all regular monoids.
"""
from itertools import product


def main():
    total=0; elements=0;rf_good=0
    for n in (2,3):
        R=[None]+list(product(range(n),repeat=2))
        G=range(n)
        masks=range(8)
        def rm(a,b):
            if a is None:return b
            if b is None:return a
            return (a[0],b[1])
        def rr(a,g):
            return a if a is None else ((a[0]+g)%n,(a[1]+g)%n)
        def pm(mask,g):
            out=0
            for k in range(3):
                if mask&(1<<k):
                    if n==2:
                        target=(1-k if k<2 and g==1 else k)
                    else:
                        target=(k+g)%3
                    out|=1<<target
            return out
        def mul(a,b):
            r,U,g=a;s,V,h=b
            return (rm(r,rr(s,g)),U&pm(V,g),(g+h)%n)
        for er,mask in product(R,masks):
            source=set()
            for r,U,g in product(R,masks,G):
                rr0=rm(rm(er,r),rr(er,g))
                source.add((rr0,mask&U&pm(mask,g),g))
            A=tuple(sorted(source,key=repr))
            E=[a for a in A if mul(a,a)==a]
            identity=(er,mask,0)
            if not all(mul(identity,a)==a==mul(a,identity) for a in A):
                raise ValueError('local identity')
            if not all((a[2]==0)==(a in E) for a in A):
                raise ValueError('pure group')
            for p in A:
                invlabel=(-p[2])%n
                rf=all(mul(mul(a,p),a)==a for a in A if a[2]==invlabel)
                below_left={mul(e,p) for e in E}
                below_right={mul(p,e) for e in E}
                below=below_left&below_right
                maximum=all(x in below for x in A if x[2]==p[2])
                rf_good+=int(rf)
                if rf!=maximum:
                    witness=next((x for x in A if x[2]==p[2] and x not in below),None)
                    print('FOUND n=',n,' e=',(er,mask),' source_size=',len(A),sep='')
                    print('p=',p,' RF=',rf,' fibre_max=',maximum,' failed_order_witness=',witness,sep='')
                    print('source_elements=',A,sep='')
                    print('LIMIT: exact finite example; general classification not inferred')
                    return
            total+=1;elements+=len(A)
    print('local_monoids=',total,' source_elements_checked=',elements,' RF_good_elements=',rf_good,sep='')
    print('PASS RF iff fibre-maximum on every element of these C2/C3 finite local monoids')
    print('LIMIT: no general equivalence or all-host theorem follows from a negative search')


if __name__=='__main__':main()
