#!/usr/bin/env python3
"""Exact modular replay of the 162x162 leading determinant ONLY.

Clears denominators by row, computes a rigorous integer row-L1 determinant
bound, and checks the stated determinant modulo distinct small primes until
product >2*bound. NumPy int64 products are <2^30: NO overflow or floats.
Does not reconstruct source, validate the listed L entries, or prove a cone.
"""
import hashlib
import json
import math
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent


def prime(n):
    if n<2:return False
    if n%2==0:return n==2
    for d in range(3,math.isqrt(n)+1,2):
        if n%d==0:return False
    return True


def modular_det(integer,p):
    A=np.array([[v%p for v in row] for row in integer],dtype=np.int64);n=A.shape[0]
    assert A.shape==(n,n) and 16384<p<32768
    det=1
    for j in range(n):
        nz=np.flatnonzero(A[j:,j])
        if not len(nz):return 0
        pivot=j+int(nz[0])
        if pivot!=j:A[[j,pivot],:]=A[[pivot,j],:];det=(-det)%p
        q=int(A[j,j]);det=(det*q)%p
        if j+1<n:
            factors=(A[j+1:,j]*pow(q,-1,p))%p
            A[j+1:,j:]=(A[j+1:,j:]-factors[:,None]*A[j,j:])%p
    return det


def main():
    inp=ROOT/'frontier-20261028-level6-446-leading-map-cone-v1.json';raw=inp.read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='606b1cfe1fdadf3d741b0d5aa649ac59a7fc7ca094ff68cf242096cc76adf3ed'
    P=json.loads(raw);assert P['status']=='LEADING_INJECTIVE_COFAC_CONE'
    L=[[Q(entry[0]) for entry in row] for row in P['matrix_entries']];n=len(L)
    assert n==162 and all(len(row)==n for row in L)
    scales=[math.lcm(*(q.denominator for q in row)) for row in L]
    integer=[[int(q*scales[i]) for q in row] for i,row in enumerate(L)]
    expected=Q(P['leading_determinant'])*math.prod(scales);assert expected.denominator==1;expected=int(expected)
    bound=math.prod(sum(abs(v) for v in row) for row in integer);assert abs(expected)<=bound
    mod_product=1;primes=[]
    for p in range(32749,16384,-2):
        if not prime(p):continue
        assert modular_det(integer,p)==expected%p,('determinant residue mismatch',p)
        primes.append(p);mod_product*=p
        if mod_product>2*bound:break
    assert mod_product>2*bound
    result={'leading_data_sha256':hashlib.sha256(raw).hexdigest(),'matrix_size':n,
            'independent_backend':'numpy '+np.__version__+' exact int64 modular elimination; products <2^30',
            'distinct_primes':primes,'prime_count':len(primes),'modulus_product_bits':mod_product.bit_length(),
            'twice_row_L1_determinant_bound_bits':(2*bound).bit_length(),
            'expected_row_scaled_determinant':str(expected),
            'residue_equal_all_primes_and_product_gt_twice_bound':True,
            'mathematical_conclusion':'the exact rational determinant of the LISTED leading matrix equals the pinned value',
            'status':'PASS_EXACT_MODULAR_LEADING_DETERMINANT_ONLY',
            'not_checked':'source/kernel basis and matrix entries, Cartan/ideal descent, independent scientific review or cone theorem'}
    out=ROOT/'frontier-20261028-level6-446-modular-determinant-replay-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS exact modular 162x162 listed-matrix determinant:',len(primes),'primes; modulus bits',mod_product.bit_length(),'bound bits',(2*bound).bit_length(),out.name,flush=True)

if __name__=='__main__':main()
