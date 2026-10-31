#!/usr/bin/env python3
"""Exact primal/dual checks for 95 universal reconstruction-cover LPs."""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
CERT=('frontier-20261028-full-fractional-cover-certificates-v1.json','9f549e01128dd5a207742d1acf6040ae766058026df15709ba97f7f63ad1b148')
MASKS=('frontier-20261028-two-syndrome-full-census-result.json','c36f2adbf02f6dc926693c29d991f8d9c4c58536c64159c132f8f14fc559f47c')
DIRECT=('frontier-20261028-two-syndrome-full-independent-result.json','190959f0b121a69fe2e2fe97bc24457702a081c73efe5540706a3b0469ab12bd')
OUT=ROOT/'frontier-20261028-full-fractional-cover-check-result.json'


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return json.loads(raw)


def check(cert,allowed):
    masks=set(allowed);dual=[Fraction(x) for x in cert['dual']];primal=[(int(I),Fraction(w)) for I,w in cert['primal']]
    if len(dual)!=10 or any(x<0 for x in dual) or any(w<=0 or not 0<I<1024 for I,w in primal):raise ValueError('SIGN')
    if len({I for I,w in primal})!=len(primal):raise ValueError('DUPLICATE')
    def independent(I):return not any(D&I==D for D in masks)
    if any(not independent(I) for I,w in primal):raise ValueError('PRIMAL_MASK')
    for v in range(10):
        if sum(w for I,w in primal if I>>v&1)<1:raise ValueError('PRIMAL_COVER')
    independent_count=0
    for I in range(1024):
        if independent(I):
            independent_count+=1
            if sum(dual[v] for v in range(10) if I>>v&1)>1:raise ValueError('DUAL_CONSTRAINT')
    p=sum(w for I,w in primal);d=sum(dual);expected=Fraction(cert['objective'])
    if p!=d or d!=expected or d<=3:raise ValueError('OBJECTIVE')
    return {'factors':cert['factors'],'objective':str(d),'primal_terms':len(primal),'independent_sets_checked':independent_count}


def main():
    certs=pin(CERT);source=pin(MASKS);direct=pin(DIRECT)
    if not direct['all_checked'] or sum(x['no_universal_color'] for x in direct['cover_counts'].values())!=95:raise ValueError('DIRECT')
    data={r['factor_mask']:r for r in source['cases'] if r['color'] is None}
    if len(data)!=95 or len(certs)!=95 or {r['factor_mask'] for r in certs}!=set(data):raise ValueError('COVERAGE')
    results=[check(c,data[c['factor_mask']]['allowed_difference_masks']) for c in certs];controls={}
    bad=json.loads(json.dumps(certs[0]));bad['dual'][0]=str(Fraction(bad['dual'][0])+1)
    try:check(bad,data[bad['factor_mask']]['allowed_difference_masks'])
    except ValueError as exc:
        if str(exc)!='DUAL_CONSTRAINT':raise ValueError(('WRONG_REASON',str(exc)))
        controls['increased_dual_weight']='DUAL_CONSTRAINT'
    else:raise ValueError('MUTATION_ACCEPTED')
    out={'certificate_sha256':CERT[1],'mask_census_sha256':MASKS[1],'direct_replay_sha256':DIRECT[1],
         'cases':results,'all_checked':True,'mutation_controls':controls,
         'limits':'Exact fractional universal-reconstruction cover optima only; entropy no-go for individual supports is not inferred.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
