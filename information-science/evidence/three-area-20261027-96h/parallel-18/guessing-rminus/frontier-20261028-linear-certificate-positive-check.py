#!/usr/bin/env python3
"""Check strict positivity of all inequality multipliers in the pinned dual."""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
CERT=ROOT/'frontier-20261028-linear-ingleton-exact-dual-v1.json'
EXPECTED='ce3fe7a8a77576dca4fd21315055cffdf767484a7a60883a2dc532b15708086a'
OUTPUT=ROOT/'frontier-20261028-linear-certificate-positive-check-result.json'


def main():
    raw=CERT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    rows=json.loads(raw)['rows'];counts=Counter()
    for row in rows:
        kind=row['metadata']['kind']
        if kind in ('CMI','conditional-ingleton'):
            if Fraction(row['weight'])<=0:raise ValueError(('NONPOSITIVE',row['metadata']))
            counts[kind]+=1
    if counts!=Counter({'CMI':64,'conditional-ingleton':83}):raise ValueError(('COUNTS',counts))
    out={'certificate_sha256':EXPECTED,'strictly_positive_inequality_rows':dict(counts),
         'limits':'Checks multiplier signs only; full row/identity checks are in the separate independent certificate checker.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
