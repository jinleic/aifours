#!/usr/bin/env python3
"""Bounded exact search for actual-context versus absent-context distinction.

Generates every one/two-generator transformation subsemigroup on 2 and 3
points, tests regularity directly and compares exact idempotence signatures.
No completeness claim beyond this finite search family; no external modules.
"""
from itertools import product


def compose(a,b):
    return tuple(a[b[i]] for i in range(len(a)))


def closure(generators):
    found=set(generators)
    while True:
        current=tuple(found)
        more={compose(a,b) for a,b in product(current,repeat=2)}-found
        if not more:return tuple(sorted(found))
        found.update(more)


def analyze(S):
    E={a for a in S if compose(a,a)==a}
    if not all(any(compose(compose(a,b),a)==a for b in S) for a in S):
        return None
    actual={a:bytes(compose(compose(x,a),y) in E for x,y in product(S,repeat=2)) for a in S}
    allctx=[None]+list(S)
    def test(x,a,y):
        z=a if x is None else compose(x,a)
        return (z if y is None else compose(z,y)) in E
    full={a:bytes(test(x,a,y) for x,y in product(allctx,repeat=2)) for a in S}
    difference=next(((a,b) for a,b in product(S,repeat=2)
                     if actual[a]==actual[b] and full[a]!=full[b]),None)
    return E,difference


def main():
    for n in (2,3):
        universe=list(product(range(n),repeat=n))
        sets={closure((a,b)) for a,b in product(universe,repeat=2)}
        regular=0
        for S in sorted(sets,key=lambda x:(len(x),x)):
            result=analyze(S)
            if result is None:continue
            regular+=1
            E,bad=result
            if bad is not None:
                idx={a:i for i,a in enumerate(S)}
                print('FOUND n=',n,' size=',len(S),' regular_sets_scanned=',regular,sep='')
                print('elements=',S,' idempotent_indices=',tuple(idx[e] for e in sorted(E)),sep='')
                print('actual_equal_but_full_distinct=',tuple(idx[e] for e in bad),sep='')
                print('table=',[[idx[compose(a,b)] for b in S] for a in S],sep='')
                print('LIMIT: finite regular transformation source; original-class eligibility not yet established')
                return
        print('n=',n,' generated_semigroups=',len(sets),' regular=',regular,' distinction=none',sep='')
    print('LIMIT: negative finite search does not prove universal equivalence')


if __name__=='__main__':main()
