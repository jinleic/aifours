#!/usr/bin/env python3
"""Exactify a proposed Ingleton linear-rank LP dual by rational elimination.

The LP supplies only a support. All weights are recomputed as Fractions,
checked for sign and checked against every orbit coefficient. An independent
checker must reconstruct all rows and graph symmetries before admission.
"""
from fractions import Fraction as F
from hashlib import sha256
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
import json,sys

ROOT=Path(__file__).resolve().parent
PROPOSAL=ROOT/'frontier-20261028-conditional-ingleton-linear-lp-result.json'
EXPECTED='31d438989981bcc5f20eaaca8fe33cf6416808a21c5836887f79a8db21b122f7'
BASE=ROOT/'frontier-20261028-copy-family-upper-lp.py'
BASE_HASH='f23e91be2a2440ab29b759983f4b0306e146c4a2dabc90038c6a461582c275e0'
OUT=ROOT/'frontier-20261028-linear-ingleton-exact-dual-v1.json'


def main():
    raw=PROPOSAL.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED or sha256(BASE.read_bytes()).hexdigest()!=BASE_HASH:raise ValueError('INPUT_HASH')
    doc=json.loads(raw)
    if doc['status_float_unverified']!='Optimal':raise ValueError('NO_SOLVER_PROPOSAL')
    sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
    spec=spec_from_file_location('entropybase',BASE);base=module_from_spec(spec);spec.loader.exec_module(base)
    orbit,reps=base.canonical_orbits(base.automorphism_group());ids={m:i for i,m in enumerate(reps)}
    row=[x for x in doc['nonzero_duals'] if x['kind']=='row']
    caps=[x for x in doc['nonzero_duals'] if x['kind']=='column']
    if len(row)!=150 or len(caps)!=3 or len(reps)!=185:raise ValueError('SUPPORT_SHAPE')
    n,m=len(row),len(reps);eq=[{} for _ in range(m)];rhs=[F(0) for _ in range(m)]
    for j,x in enumerate(row):
        for i,c in x['orbit_terms']:eq[i][j]=F(c)
    for x in caps:
        q=F(x['dual'])
        if q<=0 or x['orbit_representative'] not in (1,2,4):raise ValueError('CAP')
        rhs[ids[x['orbit_representative']]]+=q
    rhs[ids[base.FULL]]-=1
    for j in range(n):
        candidates=[i for i in range(j,m) if j in eq[i]]
        if not candidates:raise ValueError(('DEPENDENT_SUPPORT',j))
        k=min(candidates,key=lambda i:len(eq[i]));eq[j],eq[k]=eq[k],eq[j];rhs[j],rhs[k]=rhs[k],rhs[j]
        pivot=eq[j][j];eq[j]={i:c/pivot for i,c in eq[j].items()};rhs[j]/=pivot
        for i in range(j+1,m):
            factor=eq[i].pop(j,F(0))
            if not factor:continue
            rhs[i]-=factor*rhs[j]
            for k,c in eq[j].items():
                if k==j:continue
                z=eq[i].get(k,F(0))-factor*c
                if z:eq[i][k]=z
                else:eq[i].pop(k,None)
    if any(eq[i] or rhs[i] for i in range(n,m)):raise ValueError('INCONSISTENT_EXACT_SYSTEM')
    weights=[F(0)]*n
    for i in range(n-1,-1,-1):weights[i]=rhs[i]-sum(c*weights[j] for j,c in eq[i].items() if j!=i)
    for x,w in zip(row,weights):
        if x['metadata']['kind']!='FD' and w<0:raise ValueError(('NEGATIVE_INEQUALITY_WEIGHT',x['metadata'],str(w)))
    out={'proposal_sha256':EXPECTED,'base_sha256':BASE_HASH,'claim_scope':'representable/vector-linear entropy ranks only',
         'bound':'20/3','orbits':reps,'caps':[{'orbit_representative':x['orbit_representative'],'weight':x['dual']} for x in caps],
         'rows':[{'metadata':x['metadata'],'orbit_terms':x['orbit_terms'],'weight':str(w)} for x,w in zip(row,weights)],
         'expected_row_count':150,'fraction_elimination_status':'exact','nonnegative_inequality_weights_checked':True,
         'limits':'Candidate certificate only until the independent verifier rebuilds graph, all rows, signs and the identity.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({'rows':n,'caps':len(caps),'orbits':m,'bound':'20/3',
                      'FD_weights':[str(w) for x,w in zip(row,weights) if x['metadata']['kind']=='FD'],
                      'max_denominator':max(w.denominator for w in weights)},indent=2))


if __name__=='__main__':main()
