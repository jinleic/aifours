#!/usr/bin/env python3
"""Exact finite search for an RF-vs-natural-order counterexample.

Enumerates all 2-generator submonoids of a specified finite band-by-C2 host,
keeps only regular submonoids, and compares the RF and fibre-maximum predicates
using all actual elements and idempotent witnesses. No general conclusion from
failure to find an example.
"""
from itertools import product


def rm(a,b):
    if a is None:return b
    if b is None:return a
    return (a[0],b[1])


def flipr(a,h):return a if a is None or not h else (1-a[0],1-a[1])

def flipm(m,h):return m if not h else ((m&1)<<1)|((m&2)>>1)

def mul(a,b):return (rm(a[0],flipr(b[0],a[2])),a[1]&flipm(b[1],a[2]),(a[2]+b[2])%2)


def close(gens):
    values=set(gens)
    while True:
        old=tuple(values)
        added={mul(a,b) for a,b in product(old,repeat=2)}-values
        if not added:return tuple(sorted(values,key=repr))
        values.update(added)


def main():
    R=[None]+list(product(range(2),repeat=2))
    host=list(product(R,range(4),range(2)))
    one=(None,3,0)
    sources={close((one,a,b)) for a,b in product(host,repeat=2)}
    regular=surj=elements=0
    for A in sorted(sources,key=lambda a:(len(a),repr(a))):
        if not all(any(mul(mul(a,b),a)==a and mul(mul(b,a),b)==b for b in A) for a in A):continue
        regular+=1
        if not any(a[2]==1 for a in A):continue
        surj+=1
        E=[a for a in A if mul(a,a)==a]
        for p in A:
            elements+=1
            rf=all(mul(mul(a,p),a)==a for a in A if a[2]==p[2])
            left={mul(e,p) for e in E};right={mul(p,e) for e in E}
            below=left&right
            maximum=all(x in below for x in A if x[2]==p[2])
            if rf!=maximum:
                x=next((x for x in A if x[2]==p[2] and x not in below),None)
                idx={x:i for i,x in enumerate(A)}
                print('FOUND source_size=',len(A),' E_size=',len(E),' RF=',rf,' maximum=',maximum,sep='')
                print('p=',p,' same_fibre_order_failure=',x,sep='')
                print('elements=',A,sep='')
                print('table=',[[idx[mul(a,b)] for b in A] for a in A],sep='')
                print('LIMIT: finite original-compatible base; Rees source application must still be checked')
                return
    print('generated_submonoids=',len(sources),' regular=',regular,' pure_actor_surjective=',surj,
          ' elements_checked=',elements,sep='')
    print('PASS RF iff maximum for all tested elements; no counterexample in this restricted family')
    print('LIMIT: a negative search cannot prove the general equivalence')


if __name__=='__main__':main()
