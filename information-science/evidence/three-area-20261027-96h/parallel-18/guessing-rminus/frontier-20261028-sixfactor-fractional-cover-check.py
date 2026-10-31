#!/usr/bin/env python3
"""Exact primal/dual checks for seven universal reconstruction-cover LPs."""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
CERT=('frontier-20261028-sixfactor-fractional-cover-certificates-v1.json','6caf5532b3c8c2eb74401afc39e669372ec618e8806c97242bafa056c0d4f77e')
MASKS=('frontier-20261028-two-syndrome-mobius-census-result.json','a1be7e3a7dc9b491cbe3395d2c9342c7fd419b086ea3144ec4971c79df31e957')
DIRECT=('frontier-20261028-two-syndrome-direct-check-result.json','51102bd81b2cb21ddd58dca01df1aadb54071c947c94622c486da6c9051aeb20')
OUT=ROOT/'frontier-20261028-sixfactor-fractional-cover-check-result.json'


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
    if not direct['all_checked'] or direct['cover_counts']['6']['no_universal_color']!=7:raise ValueError('DIRECT')
    data={r['factor_mask']:r for r in source['cases'] if r['factor_mask'].bit_count()==6 and r['color'] is None}
    if len(data)!=7 or len(certs)!=7 or {r['factor_mask'] for r in certs}!=set(data):raise ValueError('COVERAGE')
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
