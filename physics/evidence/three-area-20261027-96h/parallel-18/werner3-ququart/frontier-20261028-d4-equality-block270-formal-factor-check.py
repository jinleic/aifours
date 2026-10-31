#!/usr/bin/env python3
"""Formal coefficient identity for actual scalar source block270.

All a,b and conjugates are independent symbolic variables; no target state,
unitary, auxiliary vector or q3 value is numerically selected.
"""
import collections
import hashlib
import itertools
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
SOURCE=ROOT/'frontier-20261028-d4-equality-block270-source-check-results.json'
PIN='8a112e9e3e5acafefd0c27ddfc4e9a0c2754c33bfd85ae2a655749a1064c2316'
OUT=ROOT/'frontier-20261028-d4-equality-block270-formal-factor-check-results.json'
raw=SOURCE.read_bytes()
if hashlib.sha256(raw).hexdigest()!=PIN:raise ValueError('source binding result mismatch')
s=json.loads(raw)
if not s['actual_binding_passed'] or not s['corrected_scalar_strictly_positive'] or s['source_block_index']!=270:
    raise ValueError('source block not bound')

def variable(kind,site,q):return f'{kind}:{site}:{q}'
def monomial(*v):return tuple(sorted(v))
# Actual j_i = e3 e3 (e1 e0 - e0 e1) on every site.
local=((1,0,1),(0,1,-1));direct=collections.Counter()
for choices in itertools.product(local,repeat=3):
    left=''.join(str(x[0]) for x in choices);right=''.join(str(x[1]) for x in choices)
    sign=1
    for x in choices:sign*=x[2]
    direct[monomial(variable('abar','333',1),variable('abar','333',1),
                    variable('a',left,0),variable('b',right,0))]+=sign
# Independent epsilon formulation of h^2 times triple wedge contraction.
reference=collections.Counter()
for eps in itertools.product((0,1),repeat=3):
    left=''.join(map(str,eps));right=''.join(str(1-x) for x in eps)
    sign=(-1)**(3-sum(eps))
    reference[monomial(variable('abar','333',1),variable('abar','333',1),
                       variable('a',left,0),variable('b',right,0))]+=sign
fault=collections.Counter()
for choices in itertools.product(local,repeat=3):
    left=''.join(str(x[0]) for x in choices);right=''.join(str(x[1]) for x in choices)
    sign=1
    for x in choices:sign*=x[2]
    fault[monomial(variable('abar','333',1),variable('abar','333',1),
                   variable('a',left,1),variable('b',right,0))]+=sign
keys=set(direct)|set(reference);errors=[list(k) for k in keys if direct[k]!=reference[k]]
faults=sum(direct[k]!=fault[k] for k in set(direct)|set(fault))
r={'kind':'formal_block270_physical_factorization','source_binding_sha256':PIN,
   'formal_monomials':len(direct),'coefficient_errors':errors,
   'wrong_aux_column_fault_mismatch_count':faults,
   'scope':'Exact source scalar contraction factorization only; no target-state sample, Haar zero argument, equality sufficiency, full q3 or formal-kernel/model-family claim.',
   'verdict':'PASS' if len(direct)==8 and not errors and faults>0 else 'FAIL'}
OUT.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
print(json.dumps(r,sort_keys=True,indent=2));raise SystemExit(0 if r['verdict']=='PASS' else 1)
