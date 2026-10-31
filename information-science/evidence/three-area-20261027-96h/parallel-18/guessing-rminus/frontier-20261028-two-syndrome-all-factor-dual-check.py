#!/usr/bin/env python3
"""Check an exact symmetrized 11-variable two-syndrome entropy certificate."""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
CERT=('frontier-20261028-two-syndrome-all-factor-dual-v1.json','a8f6822f2c3e3a8e0b0fd639a9b0095a8ea6f38c7833f0ef2fb6551fa9bba087')
OUT=ROOT/'frontier-20261028-two-syndrome-all-factor-dual-check-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
S=1<<10;V=S-1;FULL=(1<<11)-1

def mask(vertices):return sum(1<<(v-1) for v in vertices)

def row_terms(row):
    kind=row[0]
    if kind=='mono':
        i=row[1]
        if len(row)!=2 or not 0<=i<11:raise ValueError('MONO_ROW')
        return [(FULL,1),(FULL^(1<<i),-1)],'nonnegative'
    if kind=='cmi':
        if len(row)!=4:raise ValueError('CMI_ROW')
        i,j,k=row[1:];a=1<<i;b=1<<j
        if not 0<=i<j<11 or not 0<=k<=FULL or k&(a|b):raise ValueError('CMI_ROW')
        return [(k|a,1),(k|b,1),(k|a|b,-1),(k,-1)],'nonnegative'
    if kind in ('fd','syndrome-neighborhood','local-triangle-fd'):
        if len(row)!=2 or row[1] not in N:raise ValueError('FD_ROW')
        v=row[1];nm=mask(N[v]);a=1<<(v-1)
        if kind=='fd':return [(nm|a,1),(nm,-1)],'zero'
        if kind=='syndrome-neighborhood':return [(nm|S,1),(nm,-1)],'zero'
        local={u for t in TRI if v in t for u in t if u!=v};lm=mask(local)|S
        return [(lm|a,1),(lm,-1)],'zero'
    if kind=='syndrome-triangle':
        if len(row)!=2 or not 1<=row[1]<=10:raise ValueError('TRIANGLE_ROW')
        t=mask(TRI[row[1]-1]);return [(t|S,1),(t,-1)],'zero'
    if kind=='global-syndrome-gate':
        if len(row)!=1:raise ValueError('GATE_ROW')
        return [(V,3),(S,17)]+[(S|(1<<i),-2) for i in range(10)],'nonpositive'
    raise ValueError('UNKNOWN_ROW')


def check(doc,mutate_target=False):
    if doc['factors']!=list(range(1,11)):raise ValueError('FACTORS')
    group=[tuple(p) for p in doc['group']]
    if len(group)!=4 or len(set(group))!=4:raise ValueError('GROUP')
    edges={tuple(sorted((v,u))) for v in N for u in N[v]};tris={tuple(sorted(t)) for t in TRI}
    for p in group:
        if set(p)!=set(N):raise ValueError('PERMUTATION')
        if {tuple(sorted((p[a-1],p[b-1]))) for a,b in edges}!=edges:raise ValueError('GRAPH_AUTOMORPHISM')
        if {tuple(sorted(p[v-1] for v in t)) for t in TRI}!=tris:raise ValueError('FACTOR_AUTOMORPHISM')
    if not all(tuple(p[q[i]-1] for i in range(10)) in group for p in group for q in group):raise ValueError('GROUP_CLOSURE')
    def move(m,p):return (m&S)|sum(1<<(p[i]-1) for i in range(10) if m&(1<<i))
    accum=[Fraction(0) for _ in range(FULL+1)];counts=Counter()
    for item in doc['multipliers']:
        row=item['row'];q=Fraction(item['multiplier']);terms,kind=row_terms(row);counts[row[0]]+=1
        if not q:raise ValueError('ZERO_WEIGHT')
        if kind=='nonnegative' and q>=0:raise ValueError('SHANNON_SIGN')
        if kind=='nonpositive' and q<=0:raise ValueError('GATE_SIGN')
        for p in group:
            for m,c in terms:
                if m:accum[move(m,p)]+=q*c/len(group)
    target=[Fraction(0) for _ in range(FULL+1)];target[V]=1
    for i in range(10):target[1<<i]-=Fraction(2,3)
    if mutate_target:target[V]+=Fraction(1,7)
    if accum!=target:raise ValueError('COEFFICIENT_IDENTITY')
    return {'row_counts':dict(counts),'group_order':len(group),'entropy_coefficients_checked':FULL,'exact_target':'H(X_V)-(2/3)sum_i H(X_i)','gate_row_multiplier':next(x['multiplier'] for x in doc['multipliers'] if x['row'][0]=='global-syndrome-gate')}


def main():
    raw=(ROOT/CERT[0]).read_bytes()
    if sha256(raw).hexdigest()!=CERT[1]:raise ValueError('HASH')
    doc=json.loads(raw);result=check(doc);controls={}
    try:check(doc,mutate_target=True)
    except ValueError as e:controls['altered_target']=str(e)
    else:raise ValueError('TARGET_CONTROL')
    bad=json.loads(raw);cmi=next(x for x in bad['multipliers'] if x['row'][0]=='cmi');cmi['multiplier']=str(-Fraction(cmi['multiplier']))
    try:check(bad)
    except ValueError as e:controls['flipped_cmi_sign']=str(e)
    else:raise ValueError('SIGN_CONTROL')
    out={'certificate_sha256':CERT[1],'all_checked':True,'result':result,'negative_controls':controls,
         'limits':'Exact coefficient/sign/graph checks. Mathematical validity of the conditional triangle gate and lifting argument requires written review; no unrestricted q or multi-syndrome conclusion.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
