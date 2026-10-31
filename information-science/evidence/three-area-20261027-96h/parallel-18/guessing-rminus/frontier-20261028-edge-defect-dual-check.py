#!/usr/bin/env python3
"""Independent exact check of the R-minus edge-defect Shannon identity.

Rebuilds the edge set, verifies that 3--4 is the only edge outside the ten
triangles, rebuilds every FD row of the edge-deleted graph, checks CMI signs,
and verifies the identity on all 1,023 nonempty entropy coordinates.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
CERT=('frontier-20261028-edge-defect-dual-v1.json','09750933bddc4e47a25e94d1e11882f0742bdcc8cf0ab0f841836ec9ead3dc39')
OUT=ROOT/'frontier-20261028-edge-defect-dual-check-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
V=(1<<10)-1

def check(doc,change=False):
    E={tuple(sorted((u,v))) for u in N for v in N[u]};C={tuple(sorted(e)) for t in TRI for e in combinations(t,2)}
    if not C<=E or E-C!={(3,4)} or len(E)!=26:raise ValueError('EDGES')
    M={v:{u for u in N[v] if tuple(sorted((u,v))) in C} for v in N}
    acc=[Fraction(0)]*(V+1);fd=set()
    for item in doc['multipliers']:
        row=item['row'];q=Fraction(item['multiplier'])
        if row[0]=='cmi':
            i,j,K=row[1:]
            if not 0<=i<j<10 or not 0<=K<=V or K&((1<<i)|(1<<j)):raise ValueError('CMI')
            if q>=0:raise ValueError('SIGN')
            a,b=1<<i,1<<j;terms=[(K|a,1),(K|b,1),(K|a|b,-1),(K,-1)]
        elif row[0]=='triangle-graph-fd':
            v=row[1];n=sum(1<<(u-1) for u in M[v]);terms=[(n|1<<(v-1),1),(n,-1)];fd.add(v)
            if q!=Fraction(1,3):raise ValueError('FD_WEIGHT')
        else:raise ValueError('ROW')
        for m,w in terms:
            if m:acc[m]+=q*w
    if fd!=set(N):raise ValueError('FD_ROWS')
    tgt=[Fraction(0)]*(V+1);tgt[V]=Fraction(1)
    for i in range(10):tgt[1<<i]-=Fraction(2,3)
    if change:tgt[V]+=Fraction(1,7)
    if acc!=tgt:raise ValueError('IDENTITY')
    return {'cmi_rows':sum(1 for x in doc['multipliers'] if x['row'][0]=='cmi'),'fd_rows':len(fd),'fd_weight':'1/3','coordinates_checked':V}

def main():
    raw=(ROOT/CERT[0]).read_bytes()
    if sha256(raw).hexdigest()!=CERT[1]:raise ValueError('HASH')
    doc=json.loads(raw);res=check(doc);controls={}
    try:check(doc,True)
    except ValueError as e:controls['changed_target']=str(e)
    else:raise ValueError('CONTROL')
    bad=json.loads(raw);x=next(r for r in bad['multipliers'] if r['row'][0]=='cmi');x['multiplier']=str(-Fraction(x['multiplier']))
    try:check(bad)
    except ValueError as e:controls['flipped_cmi_sign']=str(e)
    else:raise ValueError('CONTROL')
    out={'certificate_sha256':CERT[1],'all_checked':True,'result':res,'negative_controls':controls,
         'limits':'Exact Shannon coefficient identity on ten variables. Its use for R-minus laws is the written argument that only the FD rows at 3 and 4 can be nonzero.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
