#!/usr/bin/env python3
"""Exact primal/dual verification of all 41 residual plane reconstruction LPs."""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
SRC=('frontier-20261028-three-syndrome-fourfactor-color-screen-result.json','218c42798aa317236225f99e5b03f2cd6bd87c21cbaeb606ebdb54b53d1ac7a8')
DIRECT=('frontier-20261028-three-syndrome-fourfactor-color-check-result.json','87b6d473e68795c3c6710d642d9a7de4fd03f9fed2378aecb2db216d878e1ea9')
CERT=('frontier-20261028-fourfactor-plane-fractional-certificates-v1.json','863f74fe993c7b6adbd867b97fa0b83de54fe8c65f4c699e66b41ebb8a8db4f4')
OUT=ROOT/'frontier-20261028-fourfactor-plane-fractional-check-result.json'

def pin(x):
    raw=(ROOT/x[0]).read_bytes()
    if sha256(raw).hexdigest()!=x[1]:raise ValueError('HASH')
    return json.loads(raw)

def check(c,masks):
    dual=[Fraction(x) for x in c['dual']];primal=[(int(I),Fraction(w)) for I,w in c['primal']]
    if len(dual)!=10 or any(x<0 for x in dual) or any(w<=0 or not 0<I<1024 for I,w in primal):raise ValueError('SIGN')
    if len({I for I,w in primal})!=len(primal):raise ValueError('DUPLICATE')
    def safe(I):return not any(D&I==D for D in masks)
    if any(not safe(I) for I,w in primal):raise ValueError('PRIMAL_SAFE')
    for v in range(10):
        if sum(w for I,w in primal if I>>v&1)<1:raise ValueError('PRIMAL_COVER')
    count=0
    for I in range(1024):
        if safe(I):
            count+=1
            if sum(dual[v] for v in range(10) if I>>v&1)>1:raise ValueError('DUAL')
    p=sum(w for I,w in primal);d=sum(dual)
    if p!=d or d!=Fraction(c['objective']) or d<=3:raise ValueError('OBJECTIVE')
    return {'factors':c['factors'],'syndrome_plane':c['syndrome_plane'],'optimum':str(d),'safe_sets':count}


def main():
    src=pin(SRC);direct=pin(DIRECT);cert=pin(CERT)
    if not direct['all_checked'] or direct['source_sha256']!=SRC[1] or direct['remaining_without_supplied_color']!=41:raise ValueError('DIRECT')
    table={(tuple(x['factors']),tuple(x['syndrome_plane'])):x for x in src['cases'] if x['color'] is None}
    if len(cert)!=41 or len(table)!=41 or {(tuple(x['factors']),tuple(x['syndrome_plane'])) for x in cert}!=set(table):raise ValueError('COVERAGE')
    result=[check(c,table[(tuple(c['factors']),tuple(c['syndrome_plane']))]['allowed_masks']) for c in cert]
    bad=json.loads(json.dumps(cert[0]));bad['dual'][0]=str(Fraction(bad['dual'][0])+1)
    try:check(bad,table[(tuple(bad['factors']),tuple(bad['syndrome_plane']))]['allowed_masks'])
    except ValueError as e:control=str(e)
    else:raise ValueError('MUTATION_ACCEPTED')
    out={'all_checked':True,'certificate_sha256':CERT[1],'direct_mask_replay_sha256':DIRECT[1],'cases':result,
         'optimum_counts':dict(Counter(x['optimum'] for x in result)),'negative_control':control,
         'limits':'Exact universal fractional-reconstruction LP optima only. A value >3 proves failure of this particular method, not an entropy law or gain.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='cases'},indent=2))


if __name__=='__main__':main()
