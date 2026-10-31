#!/usr/bin/env python3
"""Independent exact verifier for the R-minus linear-rank upper dual.

Rebuilds the graph, automorphism group, all 150 rows and all orbit coefficients;
uses Fraction only. Ingleton's representable-rank validity is a written import,
not a claim that arbitrary entropy laws satisfy it.
"""
from collections import Counter,deque
from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
CERT=ROOT/'frontier-20261028-linear-ingleton-exact-dual-v1.json'
CERT_HASH='ce3fe7a8a77576dca4fd21315055cffdf767484a7a60883a2dc532b15708086a'
BASE=ROOT/'frontier-20261028-triangle-baseline-result.json'
BASE_HASH='1ef666a1eaa04836d3ae07a0f91a8883b57f7130bc26e7bd41eb7e4c47e13e82'
OUTPUT=ROOT/'frontier-20261028-linear-dual-independent-check-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
GEN=((7,9,6,5,8,2,3,0,1,4),(0,4,5,6,1,2,3,7,8,9))
FULL=1023


def pin(path,h):
    raw=path.read_bytes()
    if sha256(raw).hexdigest()!=h:raise ValueError(('INPUT_HASH',path.name))
    return json.loads(raw)


def graph_group():
    edges={tuple(sorted((u-1,v-1))) for u,ns in N.items() for v in ns}
    if len(edges)!=26 or any(u not in N[v] for u,ns in N.items() for v in ns):raise ValueError('GRAPH')
    for p in GEN:
        if sorted(p)!=list(range(10)) or {tuple(sorted((p[u],p[v]))) for u,v in edges}!=edges:
            raise ValueError('GENERATOR')
    ident=tuple(range(10));seen={ident};todo=deque([ident])
    while todo:
        p=todo.popleft()
        for g in GEN:
            q=tuple(g[p[i]] for i in range(10))
            if q not in seen:seen.add(q);todo.append(q)
    if len(seen)!=8:raise ValueError('GROUP')
    return sorted(seen)


def image(mask,p):return sum(1<<p[i] for i in range(10) if mask&(1<<i))


def cmi(a,b,z,scale=1):
    return [(a|z,scale),(b|z,scale),(a|b|z,-scale),(z,-scale)]


def rebuild(meta):
    kind=meta['kind']
    if kind=='CMI':
        i,j,z=meta['i'],meta['j'],meta['condition_mask']
        if not (1<=i<j<=10 and 0<=z<=FULL and not z&((1<<(i-1))|(1<<(j-1)))):raise ValueError('CMI_INPUT')
        return cmi(1<<(i-1),1<<(j-1),z)
    if kind=='conditional-ingleton':
        vals=[meta[k] for k in ('A','B','C','D')];z=meta['Z_mask']
        if len(set(vals))!=4 or any(v<1 or v>10 for v in vals) or not 0<=z<=FULL:
            raise ValueError('INGLETON_INPUT')
        a,b,c,d=(1<<(v-1) for v in vals)
        if z&(a|b|c|d):raise ValueError('INGLETON_CONDITION')
        return cmi(a,b,c|z)+cmi(a,b,d|z)+cmi(c,d,z)+cmi(a,b,z,-1)
    if kind=='FD':
        v=meta['vertex']
        if v not in N:raise ValueError('FD_INPUT')
        n=sum(1<<(u-1) for u in N[v])
        return [(n|(1<<(v-1)),1),(n,-1)]
    raise ValueError(('UNKNOWN_ROW',kind))


def verify(doc,group):
    rep={m:min(image(m,p) for p in group) for m in range(1,FULL+1)}
    reps=sorted(set(rep.values()));idx={x:i for i,x in enumerate(reps)}
    if doc['orbits']!=reps or len(reps)!=185:raise ValueError('ORBITS')
    if doc['bound']!='20/3' or len(doc['rows'])!=150:raise ValueError('BOUND_OR_COUNT')
    acc=[Fraction(0) for _ in reps];kinds=Counter()
    for row in doc['rows']:
        meta=row['metadata'];kind=meta['kind'];weight=Fraction(row['weight']);kinds[kind]+=1
        if kind!='FD' and weight<0:raise ValueError('NEGATIVE_INEQUALITY_WEIGHT')
        terms={}
        for mask,c in rebuild(meta):
            if mask:
                i=idx[rep[mask]];terms[i]=terms.get(i,0)+c
        terms={i:c for i,c in terms.items() if c}
        if sorted(terms.items())!=[tuple(x) for x in row['orbit_terms']]:raise ValueError('ROW_MISMATCH')
        for i,c in terms.items():acc[i]+=weight*c
    if kinds!=Counter({'CMI':64,'conditional-ingleton':83,'FD':3}):raise ValueError(('ROW_KINDS',kinds))
    caps={}
    for cap in doc['caps']:
        m=cap['orbit_representative'];w=Fraction(cap['weight'])
        if m not in idx or m.bit_count()!=1 or m in caps or w<0:raise ValueError('INVALID_CAP')
        caps[m]=w;acc[idx[m]]-=w
    if caps!={1:Fraction(4,3),2:Fraction(8,3),4:Fraction(8,3)} or sum(caps.values())!=Fraction(20,3):
        raise ValueError('CAPS')
    acc[idx[rep[FULL]]]+=1
    residual={reps[i]:str(x) for i,x in enumerate(acc) if x}
    if residual:raise ValueError(('IDENTITY',residual))
    return dict(kinds)


def check_lower(base):
    tri=[tuple(t) for t in base['chosen_triangles']]
    if len(tri)!=10 or len(set(tri))!=10:raise ValueError('LOWER_TRIANGLES')
    if any(sum(v in t for t in tri)!=3 for v in range(1,11)):raise ValueError('LOWER_COVER')
    if any(any(b not in N[a] for a,b in combinations(t,2)) for t in tri):raise ValueError('LOWER_EDGES')
    # Each of the ten checks is supported on its own three bit coordinates.
    checks=[7<<(3*j) for j in range(10)];basis={}
    for x in checks:
        while x:
            p=x.bit_length()-1
            if p in basis:x^=basis[p]
            else:basis[p]=x;break
    if len(basis)!=10 or (1<<(30-len(basis)))!=1048576:raise ValueError('LOWER_RANK')
    return '10 disjoint triangle parity checks give 2^20 words on q=8 with neighbour XOR decoders'


def main():
    doc=pin(CERT,CERT_HASH);base=pin(BASE,BASE_HASH);group=graph_group();kinds=verify(doc,group);lower=check_lower(base)
    controls={}
    def expect_bad(name,mutate):
        changed=deepcopy(doc);mutate(changed)
        try:verify(changed,group)
        except (ValueError,KeyError,TypeError,ZeroDivisionError):controls[name]='rejected'
        else:raise ValueError(('MUTATION_NOT_REJECTED',name))
    i=next(i for i,r in enumerate(doc['rows']) if r['metadata']['kind']=='conditional-ingleton')
    j=next(i for i,r in enumerate(doc['rows']) if r['metadata']['kind']=='CMI')
    expect_bad('changed_inequality_weight',lambda x:x['rows'][j].__setitem__('weight','1'))
    expect_bad('negative_inequality_weight',lambda x:x['rows'][j].__setitem__('weight','-1'))
    expect_bad('overlapping_ingleton_condition',lambda x:x['rows'][i]['metadata'].__setitem__('Z_mask',1<<(x['rows'][i]['metadata']['A']-1)))
    expect_bad('wrong_cap',lambda x:x['caps'][0].__setitem__('weight','1'))
    expect_bad('changed_stored_row_coefficient',lambda x:x['rows'][j]['orbit_terms'][0].__setitem__(1,99))
    out={'certificate_sha256':CERT_HASH,'baseline_sha256':BASE_HASH,'graph_automorphisms':8,'graph_edges':26,
         'entropy_orbits':185,'row_kinds':kinds,'caps':3,'bound':'20/3','coefficient_residual':{},
         'nonnegative_weights_and_original_metadata_checked':True,'lower_strategy':lower,'mutation_controls':controls,
         'limits':'Exact algebra plus written Ingleton validity establish a representable-rank bound only. No arbitrary-entropy/nonlinear upper bound or novelty clearance follows.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
