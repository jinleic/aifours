#!/usr/bin/env python3
"""Recheck the saved rational relaxation point and its conditioned F_12 violation.

The point is a linear-relaxation object, not an entropic distribution or an
original guessing strategy. All arithmetic is exact Fraction arithmetic.
"""
from fractions import Fraction
from hashlib import sha256
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
import json
import math
import sys

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
spec=spec_from_file_location('sparse','frontier-20261028-sparse-certificate-cutting.py')
sparse=module_from_spec(spec);spec.loader.exec_module(sparse)
cert=sparse.cert
PRIMAL=ROOT/'frontier-20261028-exact-primal-family-scan-result.json'
PRIOR=ROOT/'frontier-20261028-sparse-certificate-cutting-result.json'
OUTPUT=ROOT/'frontier-20261028-f12-separating-point-check-result.json'
EXPECTED='55599041a5a2e73e69d0c70718bc9b049cbbd8e00f3983c5aa42ee86226e88e0'


def main():
    raw=PRIMAL.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('PRIMAL_HASH_MISMATCH')
    candidate=json.loads(raw)
    entries=candidate['primal_values']
    values={tuple(item['entropy_variables']):Fraction(item['value']) for item in entries}
    if len(values)!=len(entries):raise ValueError('DUPLICATE_ENTROPY_COORDINATE')
    for key,value in values.items():
        if value<0:raise ValueError(('NEGATIVE_ENTROPY',key,value))
    for name in cert.BASE:
        if values[(name,)]>1:raise ValueError(('SINGLETON_CAP',name))
    if values[tuple(cert.BASE)]!=Fraction(1847,276):raise ValueError('OBJECTIVE')
    data={key:(ROOT/info[0]).read_bytes() for key,info in cert.FILES.items()}
    for key,(_,digest) in cert.FILES.items():cert.pin(key,data[key],digest)
    source=cert.parse_input(data['layout'],data['text'])
    extras=json.loads(PRIOR.read_bytes())['added_cuts']
    rows=sparse.build_constraints(source,extras)
    for index,(terms,lo,hi,meta) in enumerate(rows):
        value=sum((values[key]*coef for key,coef in terms.items()),Fraction())
        if not math.isinf(lo) and value<Fraction(int(lo)):
            raise ValueError(('ROW_LOWER',index,meta,str(value)))
        if not math.isinf(hi) and value>Fraction(int(hi)):
            raise ValueError(('ROW_UPPER',index,meta,str(value)))
    def H(mask):
        return Fraction(0) if mask==0 else values[tuple(sparse.sets_from_mask(mask))]
    def I(A,B,Z):return H(A|Z)+H(B|Z)-H(A|B|Z)-H(Z)
    A,B,C,D,Z=2,512,32,12,401
    a=I(A,B,C|Z)
    delta=I(A,B,Z)-I(A,B,D|Z)-I(C,D,Z)
    d=I(A,C,B|Z)+I(B,C,A|Z)
    c=a-delta
    f12=13*a-12*delta+78*d
    if (a,c,d,f12)!=(Fraction(11,276),Fraction(-1,276),Fraction(0),Fraction(-1,276)):
        raise ValueError(('F12_NOT_EXPECTED',a,c,d,f12))
    result={'primal_sha256':EXPECTED,'coordinates':len(values),'exact_constraints_checked':len(rows),
            'all_source_shannon_FD_symmetry_and_prior_cut_rows_valid':True,
            'all_coordinate_nonnegative_and_singleton_caps':True,'objective':'1847/276',
            'substitution':{'A_mask':A,'B_mask':B,'C_mask':C,'D_mask':D,'Z_mask':Z},
            'a':str(a),'delta':str(delta),'d':str(d),'c=a-delta':str(c),
            'F12':str(f12),'F12_strictly_negative':f12<0,
            'exact_expression_for_all_positive_n':'F_n=(11-n)/276',
            'limits':'This is one exact point in a finite outer relaxation, not an entropic law or a bound improvement; universal validity of F_n and downstream dual certification are separate.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(result,stream,indent=2);stream.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
