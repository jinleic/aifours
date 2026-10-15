#!/usr/bin/env python3
"""Independent arity-four reconstruction from the book's seven identities.

Trees use operations p=prec, s=succ, d=dot and anonymous ordered leaves.
This finite exact assay does not prove admissibility of a monomial order.
"""
from functools import lru_cache
from fractions import Fraction
from collections import Counter
import hashlib
import json
from pathlib import Path

OPS = ('p','s','d')
LEAF = 'x'

def node(op, left, right):
    return (op, left, right)

@lru_cache(None)
def trees(n):
    if n == 1:
        return (LEAF,)
    return tuple(node(op, left, right) for i in range(1,n) for left in trees(i) for right in trees(n-i) for op in OPS)

def poly(*terms):
    out = Counter()
    for coefficient, term in terms:
        out[term] += coefficient
    return {t:c for t,c in out.items() if c}

def relations(a,b,c,mutant=False):
    # Left-minus-right polynomials, copied from the book page, not worker code.
    p = lambda x,y:node('p',x,y)
    s = lambda x,y:node('s',x,y)
    d = lambda x,y:node('d',x,y)
    return [
        poly((1,p(p(a,b),c)),(-1,p(a,p(b,c))),(-1,p(a,s(b,c))),(-1,p(a,d(b,c)))),
        poly((1,p(s(a,b),c)),(-1,s(a,p(b,c)))),
        poly((1,s(s(a,b),c)),(1,s(p(a,b),c)),(1,s(d(a,b),c)),(-1,s(a,s(b,c)))),
        poly((1,d(s(a,b),c)),(-1,s(a,d(b,c)))),
        poly((1,d(p(a,b),c)),(-1,d(a,s(b,c)))),
        poly((1,p(d(a,b),c)),(-1,d(a,p(b,c)))),
        poly((1,d(d(a,b),c)),(-1 if not mutant else 1,d(a,d(b,c)))),
    ]

def context(poly_, op, side):
    return {node(op,t,LEAF) if side=='left' else node(op,LEAF,t):c for t,c in poly_.items()}

def rref_rank(rows, columns):
    # Sparse exact elimination over Q.
    pivots={}
    for row in rows:
        vector = {columns[t]:Fraction(c) for t,c in row.items()}
        while vector:
            pivot=min(vector)
            if pivot not in pivots:
                scale=vector[pivot]
                pivots[pivot]={j:c/scale for j,c in vector.items()}
                break
            scale=vector[pivot]
            for j,c in pivots[pivot].items():
                new=vector.get(j,0)-scale*c
                if new:vector[j]=new
                elif j in vector:del vector[j]
    return len(pivots)

def root_rule(t, mutant=False):
    if t==LEAF or t[1]==LEAF:
        return None
    out, inner, c = t
    inn,a,b=inner
    n=node
    if out=='p' and inn=='p':
        return poly((1,n('p',a,n('p',b,c))),(1,n('p',a,n('s',b,c))),(1,n('p',a,n('d',b,c))))
    if out=='p' and inn=='s':return poly((1,n('s',a,n('p',b,c))))
    if out=='s' and inn=='s':return poly((1,n('s',a,n('s',b,c))),(-1,n('s',n('p',a,b),c)),(-1,n('s',n('d',a,b),c)))
    if out=='d' and inn=='s':return poly((1,n('s',a,n('d',b,c))))
    if out=='d' and inn=='p':return poly((1,n('d',a,n('s',b,c))))
    if out=='p' and inn=='d':return poly((1,n('d',a,n('p',b,c))))
    if out=='d' and inn=='d':return poly((1 if not mutant else -1,n('d',a,n('d',b,c))))
    return None

def paths(t):
    if t==LEAF:return [()]
    return [(t[0],)+p for p in paths(t[1])+paths(t[2])]

def pathkey(t):
    order={'p':0,'d':1,'s':2}
    return tuple((len(p),tuple(order[x] for x in p)) for p in paths(t))

def one_steps(t, mutant=False):
    if t==LEAF:return []
    op,left,right=t
    result=[]
    r=root_rule(t,mutant)
    if r is not None:result.append(r)
    for q in one_steps(left,mutant):
        result.append({node(op,u,right):c for u,c in q.items()})
    for q in one_steps(right,mutant):
        result.append({node(op,left,u):c for u,c in q.items()})
    return result

def add(a,b,scale=1):
    result=dict(a)
    for t,c in b.items():
        value=result.get(t,0)+scale*c
        if value:result[t]=value
        else:result.pop(t,None)
    return result

@lru_cache(None)
def nf(t,mutant=False):
    rewrites=one_steps(t,mutant)
    if not rewrites:return {t:1}
    out={}
    for u,c in rewrites[0].items():out=add(out,nf(u,mutant),c)
    return out

def nfpoly(q,mutant=False):
    out={}
    for t,c in q.items():out=add(out,nf(t,mutant),c)
    return out

def assay(mutant=False):
    alltrees=trees(4)
    columns={t:i for i,t in enumerate(alltrees)}
    rows=[]
    for i in range(3):
        for inner in trees(2):
            args=[LEAF]*3
            args[i]=inner
            rows.extend(relations(*args,mutant=mutant))
    for op in OPS:
        for side in ('left','right'):
            rows.extend(context(r,op,side) for r in relations(LEAF,LEAF,LEAF,mutant=mutant))
    rank=rref_rank(rows,columns)
    overlaps=[]
    bad_order=[]
    for t in alltrees:
        rewrites=one_steps(t,mutant)
        for q in rewrites:
            if any(pathkey(u)>=pathkey(t) for u in q):bad_order.append(t)
        if len(rewrites)>1:
            normalforms=[nfpoly(q,mutant) for q in rewrites]
            overlaps.append(all(v==normalforms[0] for v in normalforms))
    counts=[sum(not one_steps(t,mutant) for t in trees(i)) for i in range(1,7)]
    return {'ambient_arity4':len(alltrees),'relation_rows':len(rows),'relation_rank':rank,
            'quotient_dimension':len(alltrees)-rank,'irreducible_counts_arities1_to6':counts,
            'arity4_overlapping_trees':len(overlaps),'all_overlaps_join':all(overlaps),
            'nonjoining_overlaps':sum(not x for x in overlaps),'order_failures_sample':len(bad_order)}

if __name__=='__main__':
    good=assay()
    mutant=assay(mutant=True)
    result={'schema':'trialgebra-independent-finite-assay/1','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'original':good,'dot_associativity_sign_mutant':mutant,
            'control_detected':mutant['nonjoining_overlaps']>0,
            'limitation':'Finite overlap and dimension assay only. Admissibility and the arbitrary-arity Composition-Diamond bridge need a written proof.'}
    print(json.dumps(result,indent=2))
    assert good['all_overlaps_join'] and good['quotient_dimension']==45 and not good['order_failures_sample']
    assert result['control_detected']
