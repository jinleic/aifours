#!/usr/bin/env python3
"""Exact fraction-free Sylvester/Bareiss positivity on saved d4 multipliers.

This algorithm is independent of the replay's characteristic-polynomial test
and the other Schur-elimination check. It uses FLINT integers, never floats.
"""
import hashlib
import json
import lzma
import math
import sys
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-python-deps'))
import flint
DATA=ROOT/'frontier-20261028-d4-corrected-multipliers-and-equalities.json.xz'
OUT=ROOT/'frontier-20261028-independent-d4-bareiss-positivity-results.json'
EXPECTED='c70c12a06273faa34bed204268188ee8c6b1732f07b2ceda453f163676024f94'


def bareiss_positive(vals,n):
    parsed=[(int(x),int(y)) for x,y in vals]
    if any(d<=0 for _,d in parsed):raise ValueError('nonpositive denominator')
    den=math.lcm(*(d for _,d in parsed))
    A=[[flint.fmpz(parsed[i*n+j][0]*(den//parsed[i*n+j][1])) for j in range(n)] for i in range(n)]
    if any(A[i][j]!=A[j][i] for i in range(n) for j in range(n)):
        return False,[]
    prev=flint.fmpz(1);piv=[]
    for k in range(n):
        pivot=A[k][k];piv.append(pivot)
        if pivot<=0:return False,piv
        if k==n-1:break
        for i in range(k+1,n):
            for j in range(i,n):
                numerator=pivot*A[i][j]-A[i][k]*A[k][j]
                val,rem=divmod(numerator,prev)
                if rem:raise ArithmeticError('nonexact Bareiss division')
                A[i][j]=A[j][i]=val
        for i in range(k+1,n):A[i][k]=A[k][i]=flint.fmpz(0)
        prev=pivot
    return True,piv


def main():
    st=time.monotonic();sys.set_int_max_str_digits(0)
    raw=DATA.read_bytes();sha=hashlib.sha256(raw).hexdigest()
    if sha!=EXPECTED:raise ValueError('corrected bytes mismatch')
    data=json.loads(lzma.decompress(raw,memlimit=256*1024*1024))
    if (data['dimension'],data['copies'])!=(4,3):raise ValueError('wrong target')
    failed=[];h=hashlib.sha256();pivot_count=0;maxbits=0
    for i,m in enumerate(data['matrices']):
        n=m['r'];vals=m['values']
        if n<1 or len(vals)!=n*n:raise ValueError('bad matrix shape')
        ok,piv=bareiss_positive(vals,n)
        if not ok:failed.append(i)
        for j,x in enumerate(piv):
            z=int(x);h.update(f'{i}:{j}:{z}\n'.encode());pivot_count+=1;maxbits=max(maxbits,z.bit_length())
    first=data['matrices'][0]
    if first['r']!=1:raise ValueError('unexpected first block')
    a,b=first['values'][0];mut=[[str(-abs(int(a))-int(b)),b]]
    mutation_rejected=not bareiss_positive(mut,1)[0]
    if not mutation_rejected:raise ValueError('negative diagonal control accepted')
    result={'kind':'saved_d4_corrected_bareiss_sylvester_positivity',
            'corrected_data_sha256':sha,'matrix_count':len(data['matrices']),
            'positive_definite_fail_indices':failed,'positive_pivot_count':pivot_count,
            'maximum_pivot_bit_length':maxbits,'pivot_stream_sha256':h.hexdigest(),
            'negative_diagonal_mutation_rejected':mutation_rejected,
            'flint_version':flint.__version__,'elapsed_seconds':round(time.monotonic()-st,3),
            'method':'Exact positive leading principal minors by fraction-free integer Bareiss elimination, after positive common-denominator scaling. Every division checked exact.',
            'scope':'Strict positivity of the SAVED 1237 corrected matrices; q3, source-span and orbit identity are separate premises. Not a formal proof-assistant or other-family review.',
            'verdict':'PASS' if not failed else 'FAIL'}
    OUT.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps(result,sort_keys=True,indent=2));return 0 if not failed else 1


if __name__=='__main__':raise SystemExit(main())
