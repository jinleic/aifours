#!/usr/bin/env python3
"""Exact finite controls for tight sandwich elements in two faithful models.

Uses the separately pinned same-owner finite monoid operations.  Enumerates
all15 elements/products. No external code, random data or file writes.
"""
import importlib.util
from hashlib import sha256
from itertools import product
from pathlib import Path

HERE=Path(__file__).resolve().parent
BASE=HERE/'frontier-20261028-tight-nonunit-rees-checker-v1.py'
PIN='0398f9ed436b7fdbe2be250d4f6f07db134bded4ec77c6e58ff2945cf3c70bee'
if sha256(BASE.read_bytes()).hexdigest()!=PIN:raise ValueError('base pin')
spec=importlib.util.spec_from_file_location('tight_base',BASE)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)


def require(ok,why):
    if not ok:raise ValueError(why)


def main():
    R=[None]+list(product(range(2),repeat=2))
    A=[(r,U,h) for r in R for h in range(2) for U in ((0,1) if h==0 else (0,))]
    one=(None,1,0);p=(None,0,1);e=(None,1)
    beta=lambda a:(a[0],a[1])
    tight=lambda a: beta(a)==m.bm(e,m.alpha(e,a[2]))
    tight_elements=[a for a in A if tight(a)]
    require(tight(p) and not tight(m.am(p,p)),'expected product failure')
    require(all((m.am(a,b)[1]==(a[1]&b[1])) for a,b in product(A,repeat=2)),
            'mask homomorphism')
    # Enlarge the band by the two-element mask semilattice, with trivial C2 action.
    beta2=lambda a:(beta(a),a[1])
    def mul2(x,y):return (m.bm(x[0],y[0]),x[1]&y[1])
    def alpha2(x,h):return (m.alpha(x[0],h),x[1])
    require(len({(beta2(a),a[2]) for a in A})==len(A),'second model injective')
    require(all(beta2(m.am(a,b))==mul2(beta2(a),alpha2(beta2(b),a[2]))
                for a,b in product(A,repeat=2)), 'second model homomorphism')
    e2=beta2(one)
    tight2=lambda a: beta2(a)==mul2(e2,alpha2(e2,a[2]))
    require(not tight2(p),'representation-dependence')
    failures=[(a,b,m.am(a,b)) for a,b in product(tight_elements,repeat=2) if not tight(m.am(a,b))]
    require(failures,'expected tight nonclosure')
    print('source_size=',len(A),' original_tight_count=',len(tight_elements),sep='')
    print('tight_elements=',tight_elements,' product_failure=',(p,p,m.am(p,p)),sep='')
    print('two_faithful_models_same_group: p_tight=',tight(p),' p_tight_after_enlargement=',tight2(p),sep='')
    print('PASS all225 mask-homomorphism and enlarged-model product/injectivity checks')
    print('LIMIT: one finite source; universality requires the written identity')


if __name__=='__main__':main()
