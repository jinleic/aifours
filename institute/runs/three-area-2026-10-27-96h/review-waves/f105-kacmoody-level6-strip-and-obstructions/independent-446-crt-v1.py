#!/usr/bin/env python3
"""Check the partial modular replay's bound and receipt against a direct determinant."""
import hashlib,json,math,subprocess
from fractions import Fraction
from pathlib import Path
R=Path(__file__).resolve().parent
E=Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/kac-moody')
def load(name,sha):
    b=(E/name).read_bytes();assert hashlib.sha256(b).hexdigest()==sha
    return json.loads(b)
L=load('frontier-20261028-level6-446-leading-map-cone-v1.json','606b1cfe1fdadf3d741b0d5aa649ac59a7fc7ca094ff68cf242096cc76adf3ed')
rec=load('frontier-20261028-level6-446-modular-determinant-replay-v1.json','a47159906c4b624e2ce39a29fec41159b97c11024240a9e38df758d11f68d8af')
actual=json.loads((R/'independent-446-receipt-v1.json').read_bytes())
rows=[[Fraction(e[0]) for e in row] for row in L['matrix_entries']]
scales=[math.lcm(*(x.denominator for x in row)) for row in rows]
rows=[[int(x*scales[i]) for x in row] for i,row in enumerate(rows)]
bound=math.prod(sum(map(abs,row)) for row in rows)
primes=rec['distinct_primes']
def prime(p):return p>=2 and all(p%d for d in range(2,math.isqrt(p)+1))
assert len(primes)==256==len(set(primes)) and all(prime(p) and 16384<p<32768 for p in primes)
prod=math.prod(primes)
assert prod>2*bound and prod.bit_length()==rec['modulus_product_bits']==3825
assert (2*bound).bit_length()==rec['twice_row_L1_determinant_bound_bits']==3814
expected=int(rec['expected_row_scaled_determinant']);direct=int(actual['row_scaled_integer_determinant'])
assert direct==expected and abs(expected)<=bound
# Equality of the independently computed integers implies equality modulo
# every listed prime; no separate execution of the author's code is needed.
print('PASS',len(primes),'distinct primes; product bits',prod.bit_length(),'; double L1 bound bits',(2*bound).bit_length(),'; integer determinant equals receipt',flush=True)
r={'clock_before_receipt_creation':subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip(),
'prime_count':len(primes),'modulus_product_bits':prod.bit_length(),'twice_row_L1_bound_bits':(2*bound).bit_length(),
'modulus_gt_twice_bound':True,'all_primes_distinct_and_prime':True,
'direct_integer_determinant_matches_receipt':True,
'scope':'only receipt, listed matrix determinant, and CRT arithmetic; no 446 source/entries/cone verification'}
with (R/'independent-446-crt-receipt-v1.json').open('x') as f:json.dump(r,f,indent=2);f.write('\n')
