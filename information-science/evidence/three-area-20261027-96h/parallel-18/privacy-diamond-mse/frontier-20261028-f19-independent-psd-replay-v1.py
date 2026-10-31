#!/usr/bin/env python3
"""Independently replay PSD of the pinned corrected d=4 rational matrices.

Read-only input.  In-place upper-triangular exact Schur elimination is a
separate implementation from the prior worker's rebuilt-whole-matrix routine.
This does not check moment validity, map semantics, or the orbit identity.
"""
import hashlib
import json
import lzma
import sys
import time
from fractions import Fraction
from pathlib import Path

SOURCE = Path('/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart/frontier-20261028-d4-corrected-multipliers-and-equalities.json.xz')
EXPECTED_SHA256 = 'c70c12a06273faa34bed204268188ee8c6b1732f07b2ceda453f163676024f94'
EXPECTED_MEMBER = '0eccbad8fc2f65954a6a7038094e7c6deb9259852aef3c406f5421a4a649194f'


def psd_upper(flat, n):
    if n < 1 or len(flat) != n*n:
        return False, 'shape'
    a = [[flat[i*n+j] for j in range(n)] for i in range(n)]
    if any(a[i][j] != a[j][i] for i in range(n) for j in range(i+1,n)):
        return False, 'not_symmetric'
    for p in range(n):
        pivot = a[p][p]
        if pivot < 0:
            return False, 'negative_pivot'
        if pivot == 0:
            if any(a[p][j] != 0 for j in range(p+1,n)):
                return False, 'zero_pivot_nonzero_row'
            continue
        for i in range(p+1,n):
            factor = a[p][i] / pivot
            for j in range(i,n):
                a[i][j] -= factor * a[p][j]
    return True, 'PSD'


def main():
    sys.set_int_max_str_digits(0)
    start = time.monotonic()
    controls = [
        ('positive', [F(2),F(1),F(1),F(2)], (True,'PSD')),
        ('singular', [F(1),F(1),F(1),F(1)], (True,'PSD')),
        ('negative', [F(1),F(2),F(2),F(1)], (False,'negative_pivot')),
        ('zero_row', [F(0),F(1),F(1),F(1)], (False,'zero_pivot_nonzero_row')),
        ('nonsymmetric', [F(1),F(1),F(0),F(1)], (False,'not_symmetric')),
    ]
    outcomes = {name: psd_upper(flat,2) for name,flat,_ in controls}
    for name,_,expected in controls:
        if outcomes[name] != expected:
            raise ValueError('control failed: ' + name + ' ' + str(outcomes[name]))
    raw = SOURCE.read_bytes()
    actual = hashlib.sha256(raw).hexdigest()
    if actual != EXPECTED_SHA256:
        raise ValueError('corrected data hash mismatch')
    data = json.loads(lzma.decompress(raw,memlimit=256*1024*1024))
    if (data['source_member_sha256'],data['dimension'],data['copies']) != (EXPECTED_MEMBER,4,3):
        raise ValueError('source identity/dimension mismatch')
    if len(data['matrices']) != 1237 or len(data['equality_coefficients']) != 329:
        raise ValueError('unexpected corrected matrix/equality count')
    bad=[]
    for i,mat in enumerate(data['matrices']):
        n=mat['r']
        if type(n) is not int or not 1<=n<=40:
            raise ValueError('invalid matrix dimension at '+str(i))
        values=mat['values']
        if len(values)!=n*n:
            raise ValueError('matrix shape mismatch at '+str(i))
        flat=[Fraction(int(pair[0]),int(pair[1])) for pair in values]
        good,reason=psd_upper(flat,n)
        if not good:
            bad.append((i,reason))
    print(json.dumps({'source_sha256':actual,'dimension':4,'copies':3,
        'matrix_count':len(data['matrices']),'equality_count':len(data['equality_coefficients']),
        'controls':outcomes,'failed':bad,'elapsed_seconds':round(time.monotonic()-start,3),
        'verdict':'PASS' if not bad else 'FAIL'},sort_keys=True),flush=True)
    return 0 if not bad else 1


F=Fraction
if __name__=='__main__':
    raise SystemExit(main())
