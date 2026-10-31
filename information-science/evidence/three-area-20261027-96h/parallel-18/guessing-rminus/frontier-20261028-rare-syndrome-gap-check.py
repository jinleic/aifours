#!/usr/bin/env python3
"""Exact coarse integer margins for the rare-syndrome FD-law obstruction."""
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
SOURCE=('frontier-20261028-rare-syndrome-counterexample-check-result.json','88781d264e4b4666f3d92747f5ba2203a8f05796e9ecac307e7424f73c846e0f')
OUT=ROOT/'frontier-20261028-rare-syndrome-gap-check-result.json'


def inequalities(removed=68,exponent=128):
    N=2**20;M=N-removed
    # (2/3)*10*64*(removed/M)^2 < removed/(2N).
    if not 2560*removed**2*N < 3*removed*M**2:raise ValueError('OLD_GAP')
    # h(2^-exponent)<(exponent+2)*2^-exponent < removed/(4N).
    if not 4*(exponent+2)*N < removed*2**exponent:raise ValueError('MIXTURE')
    if not 9*(2**17-removed)>M:raise ValueError('MARGINAL')
    return {'N':N,'removed':removed,'old_support':M,'outside_weight_exponent':exponent,
            'old_gap_bound_nats':f'< -{removed}/(2*{N})',
            'mixture_entropy_bound_nats':f'< {removed}/(4*{N})'}


def main():
    raw=(ROOT/SOURCE[0]).read_bytes()
    if sha256(raw).hexdigest()!=SOURCE[1]:raise ValueError('HASH')
    src=json.loads(raw)
    if not src['all_checked'] or src['exact_checks']['removed_codewords']!=68 or src['exact_checks']['old_support_size']!=(2**20-68):raise ValueError('SOURCE')
    checks=inequalities();controls={}
    try:inequalities(exponent=4)
    except ValueError as exc:
        if str(exc)!='MIXTURE':raise ValueError(('WRONG_REASON',str(exc)))
        controls['large_outside_weight']='MIXTURE'
    else:raise ValueError('MUTATION_ACCEPTED')
    out={'source_receipt_sha256':SOURCE[1],'exact_checks':checks,'all_checked':True,'mutation_controls':controls,
         'limits':'Exact integer margins only; logarithmic/entropy bounds and the original graph-FD law are written separately.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
