#!/usr/bin/env python3
"""Separate semantic reconstruction of a triangle-component Farkas cut.
Usage: python3 script.py OUT.json CERT.json CERT_SHA
Imports no producing model/solver. Rebuilds every 15-variable Shannon row and
the exact component projection/parity/inverse premises. L is a function of S,
so masks containing S drop L. Checks signs, cancellation of ALL unknowns and
the declared coarse coefficient vector, and replays the reference separating
value exactly as Fractions of its binary floats. This is not a proof that an
abstract graph law has these physical component projections; the specific
triangle-encoding caller supplies them (see written extension lemma).
"""
from ast import literal_eval
from collections import Counter
from copy import deepcopy
from fractions import Fraction
from functools import reduce
from hashlib import sha256
from math import gcd,lcm
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parent
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
FULL=(1<<15)-1;STATE=1<<10;FUNCTIONAL=1<<11;COMPONENTS=(1<<12)|(1<<13)|(1<<14)

def semantic_row(meta,vertices,color):
    def K(mask):
        if mask&STATE:mask=mask&~FUNCTIONAL
        if mask==0:return None
        if mask&COMPONENTS:return ('u',mask)
        return ('f',mask&1023,1 if mask&STATE else (2+color if mask&FUNCTIONAL else 0))
    kind=meta[0]
    if kind=='mono':
        i=meta[1]
        if not isinstance(i,int) or not 0<=i<15:raise ValueError('MONO_INDEX')
        raw=[(FULL,1),(FULL^(1<<i),-1)];direction='ge'
    elif kind=='cmi':
        i,j,z=meta[1:]
        if not 0<=i<j<15 or not 0<=z<=FULL or z&((1<<i)|(1<<j)):raise ValueError('CMI_ARGUMENTS')
        raw=[(z|1<<i,1),(z|1<<j,1),(z|1<<i|1<<j,-1),(z,-1)];direction='ge'
    elif kind=='component-projection':
        slot,v=meta[1:]
        if not 0<=slot<3 or v!=vertices[slot]:raise ValueError('PROJECTION_PREMISE')
        bit=1<<(12+slot);yv=1<<(v-1);raw=[(yv|bit,1),(yv,-1)];direction='eq'
    elif kind=='component-parity':
        if len(meta)!=1:raise ValueError('PARITY_PREMISE')
        raw=[(COMPONENTS|FUNCTIONAL,1),(COMPONENTS,-1)];direction='eq'
    elif kind=='component-inverse':
        slot=meta[1]
        if len(meta)!=2 or not 0<=slot<3:raise ValueError('INVERSE_PREMISE')
        raw=[(COMPONENTS|FUNCTIONAL,1),((COMPONENTS^(1<<(12+slot)))|FUNCTIONAL,-1)];direction='eq'
    else:raise ValueError(('UNSUPPORTED_ROW',kind))
    terms={}
    for mask,c in raw:
        key=K(mask)
        if key is not None:terms[key]=terms.get(key,0)+c
    return {key:c for key,c in terms.items() if c},direction

def check(cert):
    if not cert.get('proof_found'):raise ValueError('NO_PROOF')
    factor=cert['factor'];vertices=cert['vertices'];color=cert['functional_color']
    if not isinstance(factor,int) or not 1<=factor<=10 or list(vertices)!=list(TRI[factor-1]) or color not in (0,1,2):raise ValueError('FACTOR_PREMISE')
    acc={};counts=Counter()
    for item in cert['multipliers']:
        w=Fraction(item['multiplier']);ts,direction=semantic_row(item['row'],vertices,color)
        if not w:raise ValueError('ZERO_WEIGHT')
        if direction=='ge' and w<0:raise ValueError('SHANNON_SIGN')
        for key,c in ts.items():acc[key]=acc.get(key,Fraction())+w*c
        counts[item['row'][0]]+=1
    acc={key:q for key,q in acc.items() if q}
    if any(key[0]!='f' for key in acc):raise ValueError('UNKNOWN_COMPONENT_NOT_CANCELLED')
    if any(not 0<=key[1]<=1023 or key[2] not in (0,1,2+color) for key in acc):raise ValueError('COARSE_COORDINATE')
    declared={}
    for key,q in cert['base_cut']:
        key=tuple(key)
        if key in declared:raise ValueError('DUPLICATE_BASE_COORDINATE')
        declared[key]=Fraction(q)
    if {key:q for key,q in declared.items() if q}!=acc:raise ValueError('BASE_COEFFICIENT_IDENTITY')
    reference={literal_eval(key):Fraction(float(v)) for key,v in cert['reference_profile_float'].items()}
    value=sum((q*reference[key] for key,q in acc.items()),Fraction())
    if value!=Fraction(cert['separation_value_on_binary_float_reference']) or value>=0:raise ValueError('REFERENCE_SEPARATION')
    D=1
    for q in acc.values():D=lcm(D,q.denominator)
    integers={key:int(q*D) for key,q in acc.items()};g=reduce(gcd,(abs(x) for x in integers.values()));primitive=[]
    for key,num in sorted(integers.items()):
        slot='none' if key[2]==0 else ('state' if key[2]==1 else 'factor')
        primitive.append({'original_mask':key[1],'auxiliary_slot':slot,'coefficient':num//g})
    return counts,value,primitive,Fraction(D,g)

def main():
    raw=(ROOT/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('CERTIFICATE_HASH')
    cert=json.loads(raw);counts,value,primitive,scale=check(cert);controls={}
    gi=next((i for i,row in enumerate(cert['multipliers']) if row['row'][0] in ('cmi','mono')),None)
    if gi is not None:
        mutant=deepcopy(cert);mutant['multipliers'][gi]['multiplier']=str(-Fraction(mutant['multipliers'][gi]['multiplier']))
        try:check(mutant)
        except ValueError as e:controls['flipped_shannon_sign']=str(e)
        else:raise ValueError('CONTROL')
    mutant=deepcopy(cert);mutant['base_cut'][0][1]=str(Fraction(mutant['base_cut'][0][1])+1)
    try:check(mutant)
    except ValueError as e:controls['changed_coarse_coefficient']=str(e)
    else:raise ValueError('CONTROL')
    mutant=deepcopy(cert);mutant['factor']=1 if cert['factor']!=1 else 2
    try:check(mutant)
    except ValueError as e:controls['changed_factor_premise']=str(e)
    else:raise ValueError('CONTROL')
    doc={'certificate_sha256':sys.argv[3],'checker_source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'all_checked':True,
      'factor':cert['factor'],'vertices':cert['vertices'],'source_functional_color':cert['functional_color'],'rows':sum(counts.values()),'row_kinds':dict(counts),
      'unknown_component_coefficients_all_zero':True,'coarse_coefficient_identity':True,'reference_separating_value':str(value),
      'primitive_schema_coefficients':primitive,'primitive_scale':str(scale),'negative_controls':controls,
      'schema_scope':'The proof uses only a generic factor functional L determined by S, not its numerical color. Instantiate the factor slot at the selected factor\'s actual functional; the actual projection/parity premises must hold.',
      'limits':'Exact same-harness semantic coefficient/sign check of a specific-component extension inequality, not a global R-minus entropy inequality, actual code, formal proof, scientific adoption or novelty claim. The floating reference is not asserted exactly feasible.'}
    with open(ROOT/sys.argv[1],'x') as f:json.dump(doc,f,indent=1);f.write('\n')
    print(json.dumps({key:v for key,v in doc.items() if key!='primitive_schema_coefficients'},indent=1))
if __name__=='__main__':main()
