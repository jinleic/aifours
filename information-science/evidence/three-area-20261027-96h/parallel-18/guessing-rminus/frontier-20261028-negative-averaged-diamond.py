#!/usr/bin/env python3
"""Exact negative automorphism-averaged diamond Ingleton example.

Rebuilds the original graph group, pairwise FDs, entropy coefficients and
integer entropy products. Uses no floating-point entropy or solver.
"""
from collections import Counter,defaultdict,deque
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
CERT=ROOT/'frontier-20261028-two-ingleton-exact-dual-v1.json'
EXPECTED='b8d049baf687e6b38024c085369970c0b05fa46e4c1ba7517b9c2c7a652b5d9c'
OUTPUT=ROOT/'frontier-20261028-negative-averaged-diamond-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
GEN=((7,9,6,5,8,2,3,0,1,4),(0,4,5,6,1,2,3,7,8,9))
WORDS=(0,6,3,15);WEIGHTS=(21,4,16,9)


def graph_group():
    edges={tuple(sorted((u-1,v-1))) for u,ns in N.items() for v in ns}
    for p in GEN:
        if {tuple(sorted((p[u],p[v]))) for u,v in edges}!=edges:raise ValueError('AUTOMORPHISM')
    ident=tuple(range(10));seen={ident};todo=deque([ident])
    while todo:
        p=todo.popleft()
        for g in GEN:
            q=tuple(g[p[i]] for i in range(10))
            if q not in seen:seen.add(q);todo.append(q)
    if len(seen)!=8:raise ValueError('GROUP_SIZE')
    return seen


def avg_terms(meta,group):
    out=defaultdict(int)
    for p in group:
        def perm(mask):return sum(1<<p[i] for i in range(10) if mask&(1<<i))
        a,b,c,d=[perm(1<<(meta[k]-1)) for k in ('A','B','C','D')];z=perm(meta['Z_mask'])
        def cmi(x,y,w,q):
            out[x|w]+=q;out[y|w]+=q;out[x|y|w]-=q;out[w]-=q
        cmi(a,b,c|z,1);cmi(a,b,d|z,1);cmi(c,d,z,1);cmi(a,b,z,-1)
    if sum(out.values())!=0:raise ValueError('COEFFICIENT_SUM')
    return {m:c for m,c in out.items() if c}


def partition(mask):
    groups={}
    for i,w in enumerate(WORDS):groups.setdefault(w&mask,[]).append(i)
    return tuple(sorted(tuple(v) for v in groups.values()))


def main():
    raw=CERT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    rows=json.loads(raw)['rows'];metas=[r['metadata'] for r in rows if r['metadata']['kind']=='conditional-ingleton']
    if len(metas)!=2:raise ValueError('GATE_SHAPES')
    if [tuple(m[k] for k in ('A','B','C','D','Z_mask')) for m in metas]!=[(2,4,1,3,1008),(2,5,3,6,713)]:raise ValueError('GATE_ORDER')
    group=graph_group()
    for a,b in combinations(WORDS,2):
        d=a^b
        if any((d>>(v-1))&1 and all(not ((d>>(u-1))&1) for u in N[v]) for v in range(1,11)):
            raise ValueError(('FD',a,b))
    if sum(WEIGHTS)!=50 or sum(w for x,w in zip(WORDS,WEIGHTS) if x&1)!=25:raise ValueError('MARGINAL')
    terms=avg_terms(metas[0],group);left=right=1
    for mask,c in terms.items():
        counts=Counter()
        for x,w in zip(WORDS,WEIGHTS):counts[x&mask]+=w
        prod=1
        for n in counts.values():prod*=n**n
        if c>0:left*=prod**c
        else:right*=prod**(-c)
    if left<=8*right:raise ValueError('NO_STRICT_MARGIN')
    p2=defaultdict(int)
    for mask,c in avg_terms(metas[1],group).items():p2[partition(mask)]+=c
    if any(p2.values()):raise ValueError('J2_NOT_IDENTICALLY_ZERO_ON_SUPPORT')
    out={'certificate_sha256':EXPECTED,'words':WORDS,'probability_numerators':WEIGHTS,'denominator':50,
         'FD_pair_vertex_checks':60,'graph_automorphisms':8,'max_singleton_entropy_bits':1,
         'J1_avg_strict_upper_bits':'-3/400','J2_avg_exact_bits':0,
         'two_J1_plus_J2_strict_upper_bits':'-3/200',
         'exact_entropy_product_L_greater_than_8R':True,'L_bits':left.bit_length(),'R_bits':right.bit_length(),
         'limits':'Shows the averaged two-defect combination can be negative on an actual FD law; this does not beat or refute the 20/3 guessing bound.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
