#!/usr/bin/env python3
"""Standard-library exact audit of d4 reverse CRT data, bound and prime receipt.

Independently reads restricted source pickle and corrected JSON, reconstructs D,
W/count factors, integer coefficient maxima, cycle objective and B; verifies
all primes/product/CRT inequality. Local Amax/Emax are taken as independently
checked receipt inputs. This DOES NOT recompute any per-prime orbit residual.
"""
import hashlib
import io
import itertools
import json
import lzma
import math
import pickle
import sys
import tarfile
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parent
ARCHIVE=ROOT/'frontier-20261028-tomar-release-ep3-v3.tar.gz'
DATA=ROOT/'frontier-20261028-d4-corrected-multipliers-and-equalities.json.xz'
NEW=ROOT/'frontier-20261028-d4-reverse-independent-crt-check-results.json'
OLD=ROOT/'frontier-20261028-d4-modular-crt-identity-proof-results.json'
CODE=ROOT/'frontier-20261028-d4-reverse-independent-crt-check.py'
PINS={ARCHIVE:'2314805738a4f41b79eb3c1593e694ad337fe6f52d13e18a70db1acc726ff5e3',
      DATA:'c70c12a06273faa34bed204268188ee8c6b1732f07b2ceda453f163676024f94',
      NEW:'3afc85cf5f47645314fa4ec369247f357c6e415a834707e273425253eea0ca19',
      OLD:'f93866ea9171a6dd8b1ecd4ca78fbeb5afe86167aebdc02c701a721da9705d3b',
      CODE:'423e58d82a5be68486b8940199335b677f3d69cbb3ba33a37065e1bded42ebbc'}
MEMBER='release_ep3/certs/ep3_perd_d4.pkl.xz'
MEMBER_SHA='0eccbad8fc2f65954a6a7038094e7c6deb9259852aef3c406f5421a4a649194f'
OUT=ROOT/'frontier-20261028-d4-reverse-crt-stdlib-receipt-check-results.json'
N=24**4

class DataOnly(pickle.Unpickler):
    def find_class(self,module,name):raise pickle.UnpicklingError('globals forbidden')

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def prime(p):return p>=2 and all(p%d for d in range(2,math.isqrt(p)+1))
def cycles(p):
    seen=set();count=0
    for j in range(len(p)):
        if j not in seen:
            count+=1;k=j
            while k not in seen:seen.add(k);k=p[k]
    return count

def valid_primes(primes,D):
    return len(primes)==424 and len(set(primes))==424 and all(type(p)==int and prime(p) and D%p for p in primes)

def bound_matches(actual,reported):return actual==reported
def product_matches(primes,reported):return math.prod(primes)==reported
def enough_product(product,bound):return product>2*bound

def main():
    st=time.monotonic();sys.set_int_max_str_digits(0)
    if any(sha(path)!=expected for path,expected in PINS.items()):raise ValueError('pinned bytes mismatch')
    with tarfile.open(ARCHIVE,mode='r:gz') as tf:
        member=tf.getmember(MEMBER)
        if not member.isfile() or member.size>2_000_000:raise ValueError('bad member')
        raw=tf.extractfile(member).read()
    if hashlib.sha256(raw).hexdigest()!=MEMBER_SHA:raise ValueError('source member mismatch')
    pkg=DataOnly(io.BytesIO(lzma.decompress(raw,memlimit=256*1024*1024))).load()
    data=json.loads(lzma.decompress(DATA.read_bytes(),memlimit=256*1024*1024))
    new=json.loads(NEW.read_text());old=json.loads(OLD.read_text())
    if (pkg['d'],pkg['k'],data['dimension'],data['copies'])!=(4,3,4,3):raise ValueError('wrong target')
    if len(pkg['types'])!=1237 or len(data['matrices'])!=1237 or len(data['equality_coefficients'])!=329:raise ValueError('wrong data count')
    pairs=[];lams=[];D=2**31;blockfactor=0;wmax=0
    for t,z in zip(pkg['types'],data['matrices']):
        r=t['r'];k=len(t['rows']);W=t['W']
        if type(r)!=int or r<1 or k<1 or z['r']!=r or len(z['values'])!=r*r or len(W)%k or any(len(row)!=r for row in W):
            raise ValueError('bad type shape')
        n=len(W)//k;blockfactor+=k*k*r*r*n*n
        wmax=max(wmax,max(abs(x) for row in W for x in row))
        for a,b in z['values']:
            a=int(a);b=int(b)
            if b<=0:raise ValueError('bad matrix denominator')
            pairs.append((a,b));D=math.lcm(D,b)
    eqfactor=0
    for x in data['equality_coefficients']:
        a=int(x['numerator']);b=int(x['denominator']);name=x['group']
        if b<=0 or name not in pkg['eq_groups']:raise ValueError('bad lambda')
        eqfactor+=len(pkg['eq_groups'][name]['parts']);lams.append((a,b));D=math.lcm(D,b)
    if D!=int(old['denominator']) or D.bit_length()!=new['common_denominator_bits']:raise ValueError('denominator mismatch')
    maxz=max(abs(a)*(D//b) for a,b in pairs);maxlam=max(abs(a)*(D//b) for a,b in lams)
    perms=list(itertools.permutations(range(4)));tau=(3,1,2,0)
    site=[2*4**cycles(p)-4**cycles(tuple(tau[p[j]] for j in range(4))) for p in perms]
    aux=[2**cycles(tuple(tau[p[j]] for j in range(4))) for p in perms]
    cobj=max(map(abs,site))**3*max(map(abs,aux))
    # These map maxima are external inputs validated by the separate literal map audits.
    amax=int(new['max_local_map']);emax=int(new['max_equality_map'])
    if (amax,emax)!=(256,24):raise ValueError('map-maxima input mismatch')
    if (blockfactor,eqfactor,wmax,cobj)!=(new['block_factor'],new['equality_part_factor'],new['max_W'],new['max_objective_numerator']):
        raise ValueError('fresh source-derived factors mismatch')
    B=N*(blockfactor*maxz*wmax*wmax*amax**4+eqfactor*maxlam*emax**4+cobj*(D//2**31))
    if not bound_matches(B,int(new['height_bound'])) or not bound_matches(B,int(old['height_bound'])):raise ValueError('height mismatch')
    primes=new['primes_tested'];P=math.prod(primes)
    if not valid_primes(primes,D) or not product_matches(primes,int(new['prime_product'])) or not enough_product(P,B):raise ValueError('prime/product/bound failure')
    if (new['prime_count'],new['prime_product_bits'],new['height_bound_bits'])!=(424,P.bit_length(),B.bit_length()):raise ValueError('receipt bit/count mismatch')
    if new['nonzero_residue_primes'] or any(new['first_prime_residuals'].values()) or new['verdict']!='PASS':raise ValueError('reported nonzero residual')
    dup=list(primes);dup[-1]=dup[0]
    composite=list(primes);composite[-1]=65520
    controls={'duplicate_prime_rejected':not valid_primes(dup,D),
              'composite_prime_rejected':not valid_primes(composite,D),
              'wrong_reported_bound_rejected':not bound_matches(B,B+1),
              'wrong_reported_product_rejected':not product_matches(primes,P+1),
              'insufficient_product_rejected':not enough_product(B,B)}
    if not all(controls.values()):raise ValueError('fault control failed')
    if any(sha(path)!=expected for path,expected in PINS.items()):raise ValueError('pinned bytes changed')
    r={'kind':'stdlib_independent_reverse_crt_bound_prime_receipt_audit',
       'source_archive_sha256':PINS[ARCHIVE],'source_member_sha256':MEMBER_SHA,'corrected_data_sha256':PINS[DATA],
       'new_result_sha256':PINS[NEW],'prior_receipt_sha256':PINS[OLD],'reverse_code_sha256':PINS[CODE],
       'source_type_count':len(pkg['types']),'corrected_matrix_count':len(data['matrices']),
       'corrected_lambda_count':len(data['equality_coefficients']),
       'common_denominator_bits':D.bit_length(),'block_factor':blockfactor,'equality_part_factor':eqfactor,
       'max_W':wmax,'assumed_checked_local_maximum':amax,'assumed_checked_equality_maximum':emax,
       'cycle_objective_maximum':cobj,'fresh_bound_matches_both_receipts':True,'height_bound_bits':B.bit_length(),
       'prime_count':len(primes),'prime_product_bits':P.bit_length(),'all_trial_prime_distinct_and_denominator_safe':True,
       'exact_product_matches_receipt':True,'product_exceeds_twice_bound':P>2*B,
       'reported_nonzero_prime_count':len(new['nonzero_residue_primes']),
       'intentional_receipt_faults_detected':controls,'elapsed_seconds':round(time.monotonic()-st,3),
       'method':'Restricted standard-library data-only pickle and xz/JSON reads; fresh exact integer denominator, W/source count factors, coefficient maxima, cycle objective, B, trial primality, denominator safety and prime product.',
       'scope':'Audits input/height/prime/CRT receipt only. Amax and Emax are independently checked inputs from separate literal local-map audits; actual per-prime residual values are trusted as reported by the pinned reverse verifier, NOT recomputed. Not a physical/source proof or model-family/formal review.',
       'verdict':'PASS'}
    OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print(json.dumps(r,sort_keys=True,indent=2));return 0


if __name__=='__main__':raise SystemExit(main())
