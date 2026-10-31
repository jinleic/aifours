#!/usr/bin/env python3
"""Check PSD directly from saved corrected rational JSON, independently of replay.

Uses exact FLINT rational Schur elimination. Verifies every stored matrix,
including zero-pivot cases; does not import/run author verifier or global code.
"""
import hashlib
import json
import lzma
import sys
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-python-deps'))
import flint
DATA=ROOT/'frontier-20261028-d4-corrected-multipliers-and-equalities.json.xz'
OUT=ROOT/'frontier-20261028-independent-saved-d4-psd-check-results.json'
EXPECTED='c70c12a06273faa34bed204268188ee8c6b1732f07b2ceda453f163676024f94'


def exact_psd(vals,n):
    A=[]
    for i in range(n):
        row=[]
        for j in range(n):
            num,den=vals[i*n+j];num=int(num);den=int(den)
            if den<=0:raise ValueError('non-positive denominator')
            row.append(flint.fmpq(num,den))
        A.append(row)
    if any(A[i][j]!=A[j][i] for i in range(n) for j in range(n)):
        return False,False
    rank=0
    while A:
        k=len(A)
        if any(A[i][i]<0 for i in range(k)):return False,False
        for i in range(k):
            if A[i][i]==0 and any(A[i][j]!=0 for j in range(k)):
                return False,False
        p=next((i for i in range(k) if A[i][i]>0),None)
        if p is None:break
        pivot=A[p][p];keep=[i for i in range(k) if i!=p]
        A=[[A[i][j]-A[i][p]*A[p][j]/pivot for j in keep] for i in keep]
        rank+=1
    return True,rank==n


def main():
    start=time.monotonic();sys.set_int_max_str_digits(0)
    raw=DATA.read_bytes();sha=hashlib.sha256(raw).hexdigest()
    if sha!=EXPECTED:raise ValueError('corrected data hash mismatch')
    data=json.loads(lzma.decompress(raw,memlimit=256*1024*1024))
    if data['dimension']!=4 or data['copies']!=3:raise ValueError('wrong physical target')
    bad=[];definite=0
    for i,m in enumerate(data['matrices']):
        n=m['r'];vals=m['values']
        if n<1 or len(vals)!=n*n:raise ValueError(f'invalid matrix shape {i}')
        ok,pd=exact_psd(vals,n)
        if not ok:bad.append(i)
        if pd:definite+=1
    result={'kind':'standalone_exact_saved_corrected_d4_psd_check',
            'corrected_data_sha256':sha,'dimension':4,'copies':3,
            'matrices_checked':len(data['matrices']),'psd_failed_indices':bad,
            'positive_definite_count':definite,'singular_psd_count':len(data['matrices'])-definite-len(bad),
            'method':'Exact FLINT fmpq rational Schur complements with explicit symmetry and zero-row checks; no author verifier imported.',
            'flint_version':flint.__version__,'elapsed_seconds':round(time.monotonic()-start,3),
            'scope':'PSD of exported exact corrected matrices only; source-map validity and exact identity are separate predicates.',
            'verdict':'PASS' if not bad else 'FAIL'}
    OUT.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps(result,sort_keys=True,indent=2),flush=True);return 0 if not bad else 1


if __name__=='__main__':raise SystemExit(main())
