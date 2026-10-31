#!/usr/bin/env python3
"""Check every allowed difference in each two-coset four-factor mixed space."""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
SOURCE=('frontier-20261028-mincover-outsider-color-census-result.json','7c25535f2c52ffdc667f3c7b231c201fef4b1279e1da826299283230dbbb44c2')
COVERS=('frontier-20261028-syndrome-cover-check-result.json','e1bf3ece1f9204a8f0f779bf98a236d689946df2bef5d2a50408b30bc9f3418d')
OUT=ROOT/'frontier-20261028-mincover-two-coset-color-check-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError('HASH')
    return json.loads(raw)


def geometry(cover):
    Ts=[TRI[t-1] for t in cover];positions={};k=0
    for v in range(1,11):positions[v]=list(range(k,k+sum(v in T for T in Ts)));k+=len(positions[v])
    if k!=12:raise ValueError('GEOMETRY')
    out=[]
    for d in range(1,4096):
        vm=sum(1<<(v-1) for v in N if any(d>>j&1 for j in positions[v]));bad=any(not(vm&sum(1<<(u-1) for u in N[v])) for v in N if vm>>(v-1)&1)
        if bad:continue
        sy=0
        for t,T in enumerate(Ts):
            parity=0
            for v in T:
                slot=positions[v][[j for j,U in enumerate(Ts) if v in U].index(t)]
                parity^=(d>>slot)&1
            sy|=parity<<t
        out.append((sy,vm))
    return out


def verify(record,allowed,colors=None):
    sy=record['syndrome'];colors=record['vertex_colors'] if colors is None else colors
    if not 1<=sy<16:raise ValueError('SYNDROME')
    if len(colors)!=10 or any(x not in (0,1,2) for x in colors):raise ValueError('COLORS')
    classes=[sum(1<<i for i,c in enumerate(colors) if c==k) for k in range(3)];count=0
    for s,mask in allowed:
        if s not in (0,sy):continue
        count+=1
        if any(mask&~C==0 for C in classes):raise ValueError('COLOR')
    return count


def main():
    src=pin(SOURCE);cov=pin(COVERS);covers={tuple(x) for x in cov['exact_checks']['minimum_covers']}
    table={(tuple(r['factors']),r['syndrome']):r for r in src['cases']}
    if len(covers)!=19 or set(table)!={(J,s) for J in covers for s in range(1,16)}:raise ValueError('COVERAGE')
    total=0;cache={J:geometry(J) for J in covers}
    for key,r in table.items():total+=verify(r,cache[key[0]])
    if total!=140368:raise ValueError(('COUNT',total))
    first=next(iter(table.values()));controls={}
    for name,change,reason in (('monochrome',{'colors':[0]*10},'COLOR'),('zero_syndrome',{},'SYNDROME')):
        target=dict(first)
        if name=='zero_syndrome':target['syndrome']=0
        try:verify(target,cache[tuple(first['factors'])],**change)
        except ValueError as exc:
            if str(exc)!=reason:raise ValueError(('WRONG_REASON',name,str(exc)))
            controls[name]=reason
        else:raise ValueError(('MUTATION_ACCEPTED',name))
    out={'source_receipt_sha256':SOURCE[1],'cover_receipt_sha256':COVERS[1],
         'covers_checked':len(covers),'nonzero_syndromes_per_cover':15,'cases_checked':len(table),
         'allowed_difference_color_checks':total,'all_checked':True,'mutation_controls':controls,
         'limits':'Exact 12-bit allowed-difference coloring only; graph/entropy and full q8 conditional lifting are written separately.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
