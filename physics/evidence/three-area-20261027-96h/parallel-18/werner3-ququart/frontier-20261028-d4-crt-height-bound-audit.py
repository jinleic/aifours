#!/usr/bin/env python3
"""Independently recompute d4 CRT height, modulus product, and map maxima.

Does not recompute all residues; checks the exact height/prime certificate of
the separate modular run from the pinned actual matrices and literal maps.
"""
import hashlib
import importlib.util
import itertools
import json
import math
import sys
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parent
GLOBAL=ROOT/'frontier-20261028-independent-d4-global-identity-check.py'
CRT=ROOT/'frontier-20261028-d4-modular-crt-identity-proof-results.json'
OUT=ROOT/'frontier-20261028-d4-crt-height-bound-audit-results.json'
HASH_GLOBAL='b6b6f5ee18f43d0ae18a18878c47b7559a5a00375754497bf21d6dec93e1be8d'
HASH_CRT='f93866ea9171a6dd8b1ecd4ca78fbeb5afe86167aebdc02c701a721da9705d3b'
HASH_BASE='bb9cf61ea6a26c0eb4570cd28abf2c26c94f64a4054640902f84ba8e4aff69ec'
HASH_AUX='0949e4945fa5cd20bac6a5d4e976c6756f97a16de2fb5c6b20c759f60798e99c'


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod


def isprime(p):return p>=2 and all(p%d for d in range(2,math.isqrt(p)+1))


def literal_counts(n,p):
    ordinary=swapped=0
    for source in itertools.product(range(n),repeat=4):
        row=[None]*4
        for i in range(4):row[p[i]]=source[i]
        ordinary+=int(tuple(row)==source)
        row[0],row[3]=row[3],row[0]
        swapped+=int(tuple(row)==source)
    return ordinary,swapped


def main():
    start=time.monotonic();sys.set_int_max_str_digits(0)
    auxpath=ROOT/'frontier-20261028-independent-d4-aux-equality-objective-check.py'
    basepath=ROOT/'frontier-20261028-independent-d4-base-check.py'
    if (sha(GLOBAL),sha(CRT),sha(basepath),sha(auxpath))!=(HASH_GLOBAL,HASH_CRT,HASH_BASE,HASH_AUX):
        raise ValueError('checker/helper/result hash mismatch')
    receipt=json.loads(CRT.read_bytes());g=module('literal_reference_height_audit',GLOBAL)
    pkg,corr=g.load_data();aux=module('aux_reference_height_audit',auxpath)
    D=8*(2*4**3)**4
    for z in corr['matrices']:
        for _,den in z['values']:D=math.lcm(D,int(den))
    for x in corr['equality_coefficients']:D=math.lcm(D,int(x['denominator']))
    if D!=int(receipt['denominator']):raise ValueError('common denominator mismatch')
    site={};qaux={}
    for t in pkg['types']:
        for a in t['rows']:
            for b in t['rows']:
                _,kp,lp=g.literal_rule(a,b)
                for mod in t['modules'][:3]:
                    key=(mod,kp,lp)
                    if key not in site:site[key]=g.make_site_map(mod,kp,lp,pkg)
                mod=t['modules'][3];key=(mod,kp,lp)
                if key not in qaux:qaux[key]=g.make_aux_map(mod,kp,lp,pkg)
    eq={}
    for group in pkg['eq_groups'].values():
        for part in group['parts']:
            for spec in part['local']:
                key=(spec[0],spec[1],tuple(spec[2]),spec[3],tuple(spec[4]))
                if key not in eq:eq[key]=g.eq_reference(spec,pkg,aux)
    maxlocal=max(abs(int(x)) for arr in list(site.values())+list(qaux.values()) for x in arr.ravel())
    maxeq=max(abs(int(x)) for arr in eq.values() for x in arr.ravel())
    maxw=max(abs(int(x)) for t in pkg['types'] for row in t['W'] for x in row)
    maxz=max(abs(int(num))*(D//int(den)) for z in corr['matrices'] for num,den in z['values'])
    maxlam=max(abs(int(x['numerator']))*(D//int(x['denominator'])) for x in corr['equality_coefficients'])
    terms=sum(len(t['rows'])**2*t['r']**2*(len(t['W'])//len(t['rows']))**2 for t in pkg['types'])
    eqterms=sum(len(pkg['eq_groups'][x['group']]['parts']) for x in corr['equality_coefficients'])
    counts4=[literal_counts(4,p) for p in g.PERMS];counts2=[literal_counts(2,p) for p in g.PERMS]
    obj=max(abs(2*a-b) for a,b in counts4)**3*max(abs(b) for a,b in counts2)
    B=(24**4)*(terms*maxz*maxw**2*maxlocal**4+eqterms*maxlam*maxeq**4+obj*(D//(8*(2*4**3)**4)))
    if B!=int(receipt['height_bound']):raise ValueError('actual residual height bound mismatch')
    if B-1==int(receipt['height_bound']):raise ValueError('height fault guard failed')
    ps=receipt['primes_tested']
    if len(ps)!=len(set(ps)) or not all(isprime(p) and D%p for p in ps):raise ValueError('prime list invalid')
    prod=math.prod(ps)
    if prod!=int(receipt['prime_product']) or prod<=2*B:raise ValueError('CRT product not sufficient')
    if receipt['nonzero_residue_primes'] or receipt['verdict']!='PASS':raise ValueError('residue calculation did not pass')
    if not any(receipt['in_memory_aab_plus_one_fault_residuals'].values()):raise ValueError('fault not detected')
    maxp=max(ps);maxrank=max(t['r'] for t in pkg['types'])
    if maxrank*(maxp-1)**2>=2**63:raise ValueError('Gram int64 overflow bound')
    # Source modular backend explicitly checks each mode contraction's axis width.
    if (24**4)*(maxp-1)>=2**63:raise ValueError('orbit int64 overflow bound')
    result={'kind':'independent_d4_crt_height_and_moduli_audit','crt_receipt_sha256':HASH_CRT,
            'source_archive_sha256':g.EXPECTED_ARCHIVE,'corrected_data_sha256':g.EXPECTED_CORRECTED,
            'common_denominator_bits':D.bit_length(),'recomputed_height_bound_bits':B.bit_length(),
            'height_bound_exact_match':True,'deliberate_B_minus_1_rejected':(B-1!=int(receipt['height_bound'])),
            'prime_count':len(ps),'all_distinct_prime_and_denominator_safe':True,
            'prime_product_bits':prod.bit_length(),'prime_product_exact_match':True,
            'prime_product_exceeds_twice_bound':prod>2*B,'largest_prime':maxp,
            'max_multiplier_rank':maxrank,'int64_gram_and_orbit_bounds':'PASS',
            'site_map_count':len(site),'aux_map_count':len(qaux),'equality_spec_count':len(eq),
            'max_local':maxlocal,'max_equality':maxeq,'max_W':maxw,
            'block_factor':terms,'equality_part_factor':eqterms,'max_objective':obj,
            'reused_literal_maps':'independent global reference helpers, pinned before this run',
            'scope':'Recomputes input-derived bound and independently checks prime list/product; trusts separate per-prime residual computation and shared literal-map helpers. Not formal-kernel or independent-model review.',
            'elapsed_seconds':round(time.monotonic()-start,3),'verdict':'PASS'}
    OUT.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps(result,sort_keys=True,indent=2));return 0


if __name__=='__main__':raise SystemExit(main())
