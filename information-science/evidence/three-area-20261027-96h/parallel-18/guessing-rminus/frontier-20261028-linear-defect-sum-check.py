#!/usr/bin/env python3
"""Sum the exact nonnegative Ingleton multipliers in the pinned certificate."""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
CERT=ROOT/'frontier-20261028-linear-ingleton-exact-dual-v1.json'
EXPECTED='ce3fe7a8a77576dca4fd21315055cffdf767484a7a60883a2dc532b15708086a'
OUTPUT=ROOT/'frontier-20261028-linear-defect-sum-check-result.json'


def main():
    raw=CERT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    weights=[Fraction(r['weight']) for r in json.loads(raw)['rows'] if r['metadata']['kind']=='conditional-ingleton']
    if len(weights)!=83 or any(w<=0 for w in weights):raise ValueError('WEIGHTS')
    total=sum(weights,Fraction(0));expected=Fraction(1856350733,320150190)
    if total!=expected:raise ValueError(('SUM',str(total)))
    out={'certificate_sha256':EXPECTED,'strict_positive_ingleton_rows':len(weights),'sum_weights':str(total),
         'inverse_sum':str(1/total),'limits':'Sum only; full identity and graph checks are in the independent dual verifier.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
