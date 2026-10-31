#!/usr/bin/env python3
"""Independently verify one exact auxiliary-copy entropy separator.

Does not import the generator, LP, or Z3. Reconstructs each CMI and every
allowed b-copy equality directly and checks exact auxiliary cancellation.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from math import gcd
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
CERT=ROOT/'frontier-20261028-branch1-farkas-cut-result.json'
CERT_SHA='ae9d207260ef0855f84c9ab3ab6f7d62128562db5ad051a0337bf9ccac6e6498'
POINT=ROOT/'frontier-20261028-source-closure-primal-frozen.json'
POINT_SHA='97e38946440c30bd2d16e349c2c8e22d69ac133e1831e7f2d6ff913bfd2f2bec'
OUT=ROOT/'frontier-20261028-branch1-cut-independent-result.json'
BASE=tuple('abcdefghij')


class Invalid(Exception):pass


def normalize(terms):
    result={}
    for mask,coef in terms:
        if not 0<=mask<2048:raise Invalid('BAD_MASK')
        if mask:result[mask]=result.get(mask,0)+coef
    return tuple(sorted((m,c) for m,c in result.items() if c))


def allowed_copy_rows():
    # b'0 is bit10, b is bit1; given base Y excludes b,c.
    Y=1023^(1<<1)^(1<<2);result=set();subset=Y
    while True:
        row=normalize(((subset|(1<<1),1),(subset|(1<<10),-1)))
        result.add(row);result.add(tuple((m,-v) for m,v in row))
        if subset==0:break
        subset=(subset-1)&Y
    ci=normalize(((Y|(1<<10),1),(1023,1),(2047,-1),(Y,-1)))
    result.add(ci);result.add(tuple((m,-v) for m,v in ci))
    return result


def check(cert,point):
    entries=cert['exact_separator']['selected_rows'];allowed=allowed_copy_rows()
    if not entries:raise Invalid('NO_ROWS')
    acc={}; counts=Counter()
    for row in entries:
        weight=Fraction(row['weight']);meta=row['metadata'];terms=normalize(row['terms'])
        if not weight:raise Invalid('ZERO_WEIGHT')
        if row['equality']:
            if meta['kind']!='copy_equality' or terms not in allowed:raise Invalid('INVALID_COPY_EQUALITY')
            counts['copy_equality']+=1
        else:
            if weight<0:raise Invalid('NEGATIVE_INEQUALITY_WEIGHT')
            if meta['kind']=='CMI':
                i,j,z=meta['i'],meta['j'],meta['z']
                if not (0<=i<j<11 and 0<=z<2048 and not z&(1<<i) and not z&(1<<j)):
                    raise Invalid('INVALID_CMI_METADATA')
                expected=normalize(((z|(1<<i),1),(z|(1<<j),1),(z|(1<<i)|(1<<j),-1),(z,-1)))
                if terms!=expected:raise Invalid('INVALID_CMI_TERMS')
                counts['CMI']+=1
            elif meta['kind']=='conditional_entropy':
                i=meta['i'];expected=normalize(((2047,1),(2047^(1<<i),-1)))
                if terms!=expected:raise Invalid('INVALID_CONDITIONAL_ENTROPY')
                counts['conditional_entropy']+=1
            elif meta['kind']=='entropy_nonnegative':
                if terms!=normalize(((meta['mask'],1),)):raise Invalid('INVALID_ENTROPY_ROW')
                counts['entropy_nonnegative']+=1
            else:raise Invalid('INVALID_INEQUALITY_KIND')
        for mask,coefficient in terms:acc[mask]=acc.get(mask,Fraction(0))+weight*coefficient
    acc={m:c for m,c in acc.items() if c}
    if any(m&(1<<10) for m in acc):raise Invalid('AUXILIARY_NOT_CANCELLED')
    announced={int(m):Fraction(c) for m,c in cert['exact_separator']['original_entropy_coefficients']}
    if acc!=announced:raise Invalid('ANNOUNCED_COEFFICIENT_MISMATCH')
    h={sum(1<<BASE.index(v) for v in item['entropy_variables']):Fraction(item['value'])
       for item in point['primal_values'] if set(item['entropy_variables'])<=set(BASE)}
    if len(h)!=1023:raise Invalid('BASE_PROFILE')
    value=sum((c*h[m] for m,c in acc.items()),Fraction(0))
    if value!=Fraction(cert['exact_separator']['point_evaluation']) or value>=0:
        raise Invalid('NOT_A_SEPARATOR')
    common=0
    for c in acc.values():
        if c.denominator!=1:raise Invalid('NONINTEGRAL_COEFFICIENT')
        common=gcd(common,abs(c.numerator))
    if not common:raise Invalid('ZERO_INEQUALITY')
    return {'row_counts':dict(counts),'selected_rows':len(entries),'base_terms':len(acc),
            'exact_auxiliary_cancellation':True,'exact_base_point_value':str(value),
            'coefficient_gcd':common,'normalized_point_value':str(value/common),
            'normalized_base_terms':[[m,str(c/common)] for m,c in sorted(acc.items())]}


def main():
    craw=CERT.read_bytes();praw=POINT.read_bytes()
    if sha256(craw).hexdigest()!=CERT_SHA or sha256(praw).hexdigest()!=POINT_SHA:raise Invalid('INPUT_HASH')
    cert=json.loads(craw);point=json.loads(praw);result=check(cert,point)
    # In-memory mutations confirm that sign and row contents are actually checked.
    import copy
    controls=[]
    for name,expected in (('flip_weight','NEGATIVE_INEQUALITY_WEIGHT'),('alter_CMI','INVALID_CMI_TERMS')):
        altered=copy.deepcopy(cert);row=next(x for x in altered['exact_separator']['selected_rows'] if not x['equality'] and x['metadata']['kind']=='CMI')
        if name=='flip_weight':row['weight']=str(-Fraction(row['weight']))
        else:row['terms'][0][1]*=-1
        try:check(altered,point)
        except Invalid as error:
            if str(error)!=expected:raise Invalid(('WRONG_MUTATION_REASON',name,str(error)))
            controls.append({'mutation':name,'expected':expected,'observed':str(error)})
        else:raise Invalid(('MUTATION_ACCEPTED',name))
    out={'certificate_sha256':CERT_SHA,'base_point_sha256':POINT_SHA,
         'verdict':result,'controls':controls,
         'limits':'A valid one-copy Shannon inequality separating one exact base profile, pending written mathematical and independent human review. It is not itself a tighter R-minus upper bound.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
