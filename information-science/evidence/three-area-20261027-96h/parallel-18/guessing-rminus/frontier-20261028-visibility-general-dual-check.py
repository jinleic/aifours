#!/usr/bin/env python3
"""Independent raw-coordinate checker for full-model visibility certificates.

Usage: python3 script.py OUT.json CERT1.json SHA1 [CERT2.json SHA2 ...]
Each certificate lists a subgroup of the factor-preserving graph
automorphisms (closure checked), a visibility set closed under it, and
multipliers. Every row is pushed through every group element, premises are
re-checked on each image, and the averaged identity is compared on all 2,047
raw coordinates with exact Fractions.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json,sys

ROOT=Path(__file__).resolve().parent
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
S=1<<10;V=S-1;FULL=(1<<11)-1

def vm(vs):return sum(1<<(v-1) for v in vs)
def local(v):return {u for t in TRI if v in t for u in t if u!=v}

def image_row(row,p):
    k=row[0]
    def pm(m):return (m&S)|sum(1<<(p[i]-1) for i in range(10) if m>>i&1)
    if k=='cmi':
        if len(row)!=4:raise ValueError('CMI_ROW')
        i,j,K=row[1:]
        if not 0<=i<j<11 or not 0<=K<=FULL or K&((1<<i)|(1<<j)):raise ValueError('CMI_ROW')
        a,b,K2=pm(1<<i),pm(1<<j),pm(K);return [(K2|a,1),(K2|b,1),(K2|a|b,-1),(K2,-1)],'nonnegative',None
    if k=='mono':
        i=row[1];a=pm(1<<i);return [(FULL,1),(FULL^a,-1)],'nonnegative',None
    if k=='fd':
        v=p[row[1]-1];n=vm(N[v]);return [(n|1<<(v-1),1),(n,-1)],'zero',None
    if k=='local-fd':
        v=p[row[1]-1];L=vm(local(v));return [(L|S|1<<(v-1),1),(L|S,-1)],'zero',None
    if k=='syndrome-neighborhood':
        v=p[row[1]-1];n=vm(N[v]);return [(n|S,1),(n,-1)],'zero',v
    if k=='syndrome-global-fd':
        if len(row)!=1:raise ValueError('GLOBAL_ROW')
        return [(V|S,1),(V,-1)],'zero',None
    raise ValueError(('UNKNOWN',row))

def check(doc,change=False,drop=None):
    group=[tuple(p) for p in doc['group']];need=set(doc['visibility_required'])
    if drop is not None:need.discard(drop)
    E={tuple(sorted((u,v))) for u in N for v in N[u]};T={tuple(sorted(t)) for t in TRI}
    if not group or len(set(group))!=len(group) or tuple(range(1,11)) not in group:raise ValueError('GROUP')
    for p in group:
        if set(p)!=set(N) or {tuple(sorted((p[a-1],p[b-1]))) for a,b in E}!=E:raise ValueError('GRAPH')
        if {tuple(sorted(p[v-1] for v in t)) for t in TRI}!=T:raise ValueError('FACTORS')
    if not all(tuple(p[q[i]-1] for i in range(10)) in group for p in group for q in group):raise ValueError('CLOSURE')
    acc=[Fraction(0)]*(FULL+1);counts=Counter();used=set();g=len(group)
    for item in doc['multipliers']:
        q=Fraction(item['multiplier']);counts[item['row'][0]]+=1
        if not q:raise ValueError('ZERO')
        for p in group:
            terms,kind,vis=image_row(item['row'],p)
            if kind=='nonnegative' and q>=0:raise ValueError('SIGN')
            if vis is not None:
                if vis not in need:raise ValueError('VISIBILITY_NOT_ASSUMED')
                used.add(vis)
            for m,w in terms:
                if m:acc[m]+=q*w/g
    target=[Fraction(0)]*(FULL+1);target[V]=Fraction(1)
    for i in range(10):target[1<<i]-=Fraction(2,3)
    if change:target[V]+=Fraction(1,7)
    if acc!=target:raise ValueError('COEFFICIENT_IDENTITY')
    return {'rows':dict(counts),'group_order':g,'visibility_vertices_used':sorted(used),'coordinates_checked':FULL}

def main():
    out=ROOT/sys.argv[1];pairs=list(zip(sys.argv[2::2],sys.argv[3::2]));results=[]
    if not pairs:raise ValueError('NO_CERTS')
    for name,digest in pairs:
        raw=(ROOT/name).read_bytes()
        if sha256(raw).hexdigest()!=digest:raise ValueError(('HASH',name))
        doc=json.loads(raw);res=check(doc)
        if set(res['visibility_vertices_used'])!=set(doc['visibility_required']):raise ValueError('VISIBILITY_SET_NOT_MINIMAL_RECORD')
        controls={}
        try:check(doc,change=True)
        except ValueError as e:controls['changed_target']=str(e)
        else:raise ValueError('CONTROL')
        try:check(doc,drop=min(doc['visibility_required']))
        except ValueError as e:controls['dropped_one_visibility']=str(e)
        else:raise ValueError('CONTROL')
        results.append({'certificate':name,'sha256':digest,'visibility_required':doc['visibility_required'],**res,'negative_controls':controls})
    report={'all_checked':True,'cases':results,'limits':'Exact raw-coordinate identities, signs, subgroup closure and visibility bookkeeping. Written validity of local decoders and of visibility for any concrete support is separate.'}
    with out.open('x',encoding='utf-8') as f:json.dump(report,f,indent=2);f.write('\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
