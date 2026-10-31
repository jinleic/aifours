#!/usr/bin/env python3
"""Strict domain/shape verification of all pinned n2/n4 commutator witnesses.

No modular rank is recomputed here; the pinned standalone rank result is a
separate prerequisite. In-memory faults exercise semantic guards only.
"""
import collections
import copy
import hashlib
import itertools
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
WIT=ROOT/'frontier-20261028-local-commutant-pivot-rows.json'
RANK=ROOT/'frontier-20261028-commutant-standalone-verifier-results.json'
PINS={WIT:'1cf37f5429892ac7a8da6fe6a90ad2fb2259a692887b1368e3329ffecc9fbbb4',
      RANK:'941c109c36a1536bcf2abf1c6c25ca7e4417104ede684a21221fb5e0582459b6'}
OUT=ROOT/'frontier-20261028-d4-commutator-witness-domain-check-results.json'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def fail(msg):raise ValueError(msg)

def dimension(n):
    counts=collections.Counter(tuple(word.count(i) for i in range(n)) for word in itertools.product(range(n),repeat=4))
    return sum(k*k for k in counts.values())

def validate(case,n,prime):
    N=dimension(n);target=N-({2:14,4:24}[n])
    if case['dimension']!=n or case['replicas']!=4 or case['modulus']!=prime or case['commutant_unknowns']!=N:
        fail('metadata')
    cols=case['pivot_columns'];rows=case['witness_rows']
    if len(cols)!=target or any(type(x)!=int or not 0<=x<N for x in cols) or len(set(cols))!=target:
        fail('pivot columns')
    if len(rows)!=target:fail('row count')
    seen=set()
    for row in rows:
        if len(row)!=4:fail('row arity')
        i,j,x,y=row
        if type(i)!=int or type(j)!=int or not 0<=i<n or not 0<=j<n or i==j:fail('generator')
        if len(x)!=4 or len(y)!=4 or any(type(z)!=int or not 0<=z<n for z in x+y):fail('word domain')
        wy=[y.count(k) for k in range(n)];wx=[x.count(k) for k in range(n)]
        if wy[j]==0:fail('empty action')
        wy[i]+=1;wy[j]-=1
        if wx!=wy:fail('weight')
        key=(i,j,tuple(x),tuple(y))
        if key in seen:fail('duplicate row')
        seen.add(key)
    return {'n':n,'same_weight_unknowns':N,'selected_rows':len(rows),'distinct_valid_pivot_columns':len(cols)}

def rejected(case,n,prime):
    try:validate(case,n,prime)
    except (ValueError,TypeError,KeyError,IndexError):return True
    return False

if any(sha(path)!=digest for path,digest in PINS.items()):raise ValueError('pin mismatch')
w=json.loads(WIT.read_bytes());rank=json.loads(RANK.read_bytes());prime=w['prime']
if type(prime)!=int or prime!=65521:raise ValueError('unexpected modulus')
cases={x['dimension']:x for x in w['cases']}
if set(cases)!={2,4}:raise ValueError('missing case')
summary=[validate(cases[n],n,prime) for n in (2,4)]
controls={}
for n in (2,4):
    orig=cases[n]
    a=copy.deepcopy(orig);a['pivot_columns'][0]=dimension(n);controls[f'n{n}_out_of_range_pivot']=rejected(a,n,prime)
    a=copy.deepcopy(orig);a['pivot_columns'][-1]=a['pivot_columns'][0];controls[f'n{n}_duplicate_pivot']=rejected(a,n,prime)
    a=copy.deepcopy(orig);a['witness_rows'][0][1]=a['witness_rows'][0][0];controls[f'n{n}_equal_generator_indices']=rejected(a,n,prime)
    a=copy.deepcopy(orig);a['witness_rows'][0][2][0]=n;controls[f'n{n}_out_of_range_word']=rejected(a,n,prime)
    a=copy.deepcopy(orig);a['witness_rows'][0][2][0]=(a['witness_rows'][0][2][0]+1)%n;controls[f'n{n}_wrong_weight']=rejected(a,n,prime)
    a=copy.deepcopy(orig);a['witness_rows'][-1]=copy.deepcopy(a['witness_rows'][0]);controls[f'n{n}_duplicate_row']=rejected(a,n,prime)
    a=copy.deepcopy(orig);a['pivot_columns'][0]=str(a['pivot_columns'][0]);controls[f'n{n}_noninteger_pivot']=rejected(a,n,prime)
if rank['verdict']!='PASS' or [x['commutator_minor_rank_mod_p'] for x in rank['cases']]!=[56,2692]:raise ValueError('rank receipt mismatch')
if any(sha(path)!=digest for path,digest in PINS.items()):raise ValueError('input changed')
r={'kind':'strict_all_n2_n4_commutator_witness_domain_audit','witness_sha256':PINS[WIT],
   'prior_rank_receipt_sha256':PINS[RANK],'prime':prime,'cases':summary,
   'intentional_faults_detected':controls,
   'scope':'All actual witness row/column semantic domains and shape only; modular ranks are read from the separately pinned prior result and NOT recomputed. Not a physical q3 theorem, formal proof or independent-family review.',
   'verdict':'PASS' if all(controls.values()) else 'FAIL'}
OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
print(json.dumps(r,sort_keys=True,indent=2));raise SystemExit(0 if r['verdict']=='PASS' else 1)
