#!/usr/bin/env python3
"""Independent raw-coordinate check of the universal syndrome-visibility identity.

Every row is pushed through each of the four factor-preserving graph
automorphisms, its premise is re-checked on the image, and the averaged
identity is compared on all 2,047 entropy coordinates.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
CERT=('frontier-20261028-visibility67-dual-v1.json','2d52767c052cbcf9fcc181812e79909f345b8c6f096a50e6077d39889019ac12')
OUT=ROOT/'frontier-20261028-visibility67-dual-check-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
S=1<<10;V=S-1;FULL=(1<<11)-1

def vm(vs):return sum(1<<(v-1) for v in vs)
def local(v):return {u for t in TRI if v in t for u in t if u!=v}

def image_row(row,p):
    k=row[0]
    def pv(v):return p[v-1]
    def pm(m):return (m&S)|sum(1<<(p[i]-1) for i in range(10) if m>>i&1)
    if k=='cmi':
        i,j,K=row[1:]
        if not 0<=i<j<11 or K&((1<<i)|(1<<j)) or not 0<=K<=FULL:raise ValueError('CMI_ROW')
        a,b=pm(1<<i),pm(1<<j);K2=pm(K);return [(K2|a,1),(K2|b,1),(K2|a|b,-1),(K2,-1)],'nonnegative',None
    if k=='fd':
        v=pv(row[1]);n=vm(N[v]);return [(n|1<<(v-1),1),(n,-1)],'zero',None
    if k=='local-fd':
        v=pv(row[1]);L=vm(local(v));return [(L|S|1<<(v-1),1),(L|S,-1)],'zero',None
    if k=='syndrome-neighborhood':
        v=pv(row[1]);n=vm(N[v]);return [(n|S,1),(n,-1)],'zero',v
    if k=='syndrome-global-fd':
        return [(V|S,1),(V,-1)],'zero',None
    raise ValueError(('UNKNOWN',row))

def check(doc,change=False):
    group=[tuple(p) for p in doc['group']];need=set(doc['visibility_required'])
    E={tuple(sorted((u,v))) for u in N for v in N[u]};T={tuple(sorted(t)) for t in TRI}
    if len(group)!=4 or len(set(group))!=4:raise ValueError('GROUP')
    for p in group:
        if set(p)!=set(N) or {tuple(sorted((p[a-1],p[b-1]))) for a,b in E}!=E:raise ValueError('GRAPH')
        if {tuple(sorted(p[v-1] for v in t)) for t in TRI}!=T:raise ValueError('FACTORS')
    if not all(tuple(p[q[i]-1] for i in range(10)) in group for p in group for q in group):raise ValueError('CLOSURE')
    acc=[Fraction(0)]*(FULL+1);counts=Counter();used=set()
    for item in doc['multipliers']:
        q=Fraction(item['multiplier']);counts[item['row'][0]]+=1
        for p in group:
            terms,kind,vis=image_row(item['row'],p)
            if kind=='nonnegative' and q>=0:raise ValueError('SIGN')
            if vis is not None:
                if vis not in need:raise ValueError('VISIBILITY_NOT_ASSUMED')
                used.add(vis)
            for m,w in terms:
                if m:acc[m]+=q*w/4
    target=[Fraction(0)]*(FULL+1);target[V]=Fraction(1)
    for i in range(10):target[1<<i]-=Fraction(2,3)
    if change:target[V]+=Fraction(1,7)
    if acc!=target:raise ValueError('COEFFICIENT_IDENTITY')
    return {'rows':dict(counts),'visibility_vertices_used':sorted(used),'coordinates_checked':FULL}

def main():
    raw=(ROOT/CERT[0]).read_bytes()
    if sha256(raw).hexdigest()!=CERT[1]:raise ValueError('HASH')
    doc=json.loads(raw);res=check(doc);controls={}
    if set(res['visibility_vertices_used'])!=set(doc['visibility_required']) or set(doc['visibility_required'])!={6,7}:raise ValueError('VISIBILITY_SET')
    try:check(doc,True)
    except ValueError as e:controls['changed_target']=str(e)
    else:raise ValueError('CONTROL')
    bad=json.loads(raw);bad['visibility_required']=[v for v in bad['visibility_required'] if v!=7]
    try:check(bad)
    except ValueError as e:controls['dropped_visibility_7']=str(e)
    else:raise ValueError('CONTROL')
    bad=json.loads(raw);x=next(r for r in bad['multipliers'] if r['row'][0]=='cmi');x['multiplier']=str(-Fraction(x['multiplier']))
    try:check(bad)
    except ValueError as e:controls['flipped_cmi_sign']=str(e)
    else:raise ValueError('CONTROL')
    out={'certificate_sha256':CERT[1],'all_checked':True,'result':res,'negative_controls':controls,
         'limits':'Exact raw-coordinate identity, signs and premise bookkeeping. Validity of local decoders and visibility for a given support is a written argument.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
