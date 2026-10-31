#!/usr/bin/env python3
"""Prove the exact d4 orbit identity via an independent modular backend.

Computes a conservative integer height bound from the actual corrected data
and all literal local maps. Verifies all orbit residues modulo enough distinct
primes that their product exceeds twice the bound. Then CRT implies that each
integer residual is exactly zero. No author verifier or FLINT big-matrix
aggregation is used, but literal-map/orbit generators are shared with our
previous independent exact checker and NumPy int64 remains trusted.
"""
import hashlib
import importlib.util
import json
import math
import sys
import time
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
MOD=ROOT/'frontier-20261028-d4-independent-modular-identity-check.py'
GLOBAL=ROOT/'frontier-20261028-independent-d4-global-identity-check.py'
OUT=ROOT/'frontier-20261028-d4-modular-crt-identity-proof-results.json'
EXPECT_MOD='5be6e2f2bd6df4e0ffffab73b12bf17721d982385967e74fe1afa34deb834f88'
EXPECT_GLOBAL='b6b6f5ee18f43d0ae18a18878c47b7559a5a00375754497bf21d6dec93e1be8d'
HELPERS={
    ROOT/'frontier-20261028-independent-d4-base-check.py':'bb9cf61ea6a26c0eb4570cd28abf2c26c94f64a4054640902f84ba8e4aff69ec',
    ROOT/'frontier-20261028-independent-d4-aux-equality-objective-check.py':'0949e4945fa5cd20bac6a5d4e976c6756f97a16de2fb5c6b20c759f60798e99c',
}
TIME_LIMIT=540.0


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m


def main():
    start=time.monotonic();sys.set_int_max_str_digits(0)
    pins={MOD:EXPECT_MOD,GLOBAL:EXPECT_GLOBAL,**HELPERS}
    if any(sha(path)!=value for path,value in pins.items()):raise ValueError('checker/helper script hash mismatch')
    m=load('independent_modular_backend',MOD);g=m.load_module('independent_literal_generator',GLOBAL)
    pkg,corr=g.load_data()
    # Preparse exact rational integer strings once; this changes memory only.
    D=8*(2*4**3)**4
    for z in corr['matrices']:
        for pair in z['values']:
            pair[0]=int(pair[0]);pair[1]=int(pair[1]);D=math.lcm(D,pair[1])
    for lam in corr['equality_coefficients']:
        lam['numerator']=int(lam['numerator']);lam['denominator']=int(lam['denominator'])
        D=math.lcm(D,lam['denominator'])
    orbits={f:g.generate_orbits(s) for f,s in g.LETTERS.items()}
    sc={};ac={};ec={};first=65521
    if not m.prime(first) or D%first==0:raise ValueError('first prime invalid or divides denominator')
    residues=m.run_prime(g,pkg,corr,first,orbits,sc,ac,ec)
    if any(residues.values()):raise ValueError('first prime already rejects actual certificate')
    # Negative control: alter one actual equality coefficient by +1 in memory.
    chosen=next(x for x in corr['equality_coefficients'] if x['group']=='aab')
    old=chosen['numerator'];chosen['numerator']=old+chosen['denominator']
    injected=m.run_prime(g,pkg,corr,first,orbits,sc,ac,ec);chosen['numerator']=old
    if not any(injected.values()):raise ValueError('equality mutation was not detected')

    # Uniform per-word numerator bounds, using actual data maxima and all
    # exact precomputed local-map entries. Every orbit has at most 24^4 words.
    max_z=max(abs(num)*(D//den) for z in corr['matrices'] for num,den in z['values'])
    max_lam=max(abs(x['numerator'])*(D//x['denominator']) for x in corr['equality_coefficients'])
    max_w=max(abs(int(x)) for t in pkg['types'] for row in t['W'] for x in row)
    max_local=max(abs(int(x)) for arr in list(sc.values())+list(ac.values()) for x in arr.ravel())
    max_equal=max(abs(int(x)) for arr in ec.values() for x in arr.ravel())
    block_factor=sum(len(t['rows'])**2*t['r']**2*(len(t['W'])//len(t['rows']))**2 for t in pkg['types'])
    eq_factor=sum(len(pkg['eq_groups'][x['group']]['parts']) for x in corr['equality_coefficients'])
    aux=g.module('crt_aux_reference',ROOT/'frontier-20261028-independent-d4-aux-equality-objective-check.py')
    site_counts=[aux.swap_trace_counts(4,p) for p in g.PERMS]
    q_counts=[aux.swap_trace_counts(2,p) for p in g.PERMS]
    max_obj=max(abs(2*a-b) for a,b in site_counts)**3*max(abs(b) for a,b in q_counts)
    obj_den=8*(2*4**3)**4
    per_word_bound=(block_factor*max_z*max_w**2*max_local**4
                    +eq_factor*max_lam*max_equal**4+max_obj*(D//obj_den))
    B=(24**4)*per_word_bound
    if B<=0:raise ValueError('invalid residual height bound')
    product=first;tested=[first];bad=[]
    for p in range(first-2,2,-2):
        if product>2*B:break
        if not m.prime(p) or D%p==0:continue
        if time.monotonic()-start>TIME_LIMIT:break
        counts=m.run_prime(g,pkg,corr,p,orbits,sc,ac,ec)
        tested.append(p);product*=p
        if any(counts.values()):bad.append({'prime':p,'residual_counts':counts});break
        if len(tested)%50==0:print('checked primes',len(tested),'product_bits',product.bit_length(),'bound_bits',B.bit_length(),'elapsed',round(time.monotonic()-start,1),flush=True)
    if any(sha(path)!=value for path,value in pins.items()):raise ValueError('checker/helper changed during run')
    complete=(product>2*B and not bad)
    receipt={'kind':'rigorous_modular_crt_d4_orbit_identity','source_archive_sha256':g.EXPECTED_ARCHIVE,
             'corrected_data_sha256':g.EXPECTED_CORRECTED,'global_map_helper_sha256':EXPECT_GLOBAL,
             'modular_backend_sha256':EXPECT_MOD,'denominator':str(D),'denominator_bits':D.bit_length(),
             'helper_sha256':{path.name:value for path,value in HELPERS.items()},
             'height_bound':str(B),'height_bound_bits':B.bit_length(),
             'bound_components':{'orbit_size_bound':24**4,'block_factor':block_factor,
                                 'equality_part_factor':eq_factor,'max_W':max_w,
                                 'max_local_map':max_local,'max_equality_map':max_equal,'max_objective_numerator':max_obj},
             'primes_tested':tested,'prime_count':len(tested),'prime_product':str(product),
             'prime_product_bits':product.bit_length(),'product_exceeds_twice_bound':product>2*B,
             'nonzero_residue_primes':bad,'actual_first_prime_residuals':residues,
             'in_memory_aab_plus_one_fault_residuals':injected,
             'orbit_counts':{f:orbits[f][1] for f in g.LETTERS},
             'elapsed_seconds':round(time.monotonic()-start,3),
             'method':'All source orbit sums recomputed for every listed prime with int64-safe modular tensor contractions; actual input max-norm bounds yield |integer residual|<=B; distinct-prime product>2B implies exact zero by CRT.',
             'independence':'No author verifier/core and no FLINT big-matrix global aggregation; shares our earlier exact checker literal-map/orbit generators and ordinary Python/numpy runtime.',
             'scope':'Exact identity of the saved corrected d4 rational certificate, subject to height-bound proof and implementation/runtime correctness. Physical moment validity and PSD are separately checked; no formal proof-assistant or other-family acceptance.',
             'verdict':'PASS' if complete else ('FAIL' if bad else 'INCONCLUSIVE')}
    OUT.write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n')
    print(json.dumps({k:v for k,v in receipt.items() if k not in ('denominator','height_bound','prime_product','primes_tested')},sort_keys=True,indent=2),flush=True)
    return 0 if complete else (1 if bad else 2)


if __name__=='__main__':raise SystemExit(main())
