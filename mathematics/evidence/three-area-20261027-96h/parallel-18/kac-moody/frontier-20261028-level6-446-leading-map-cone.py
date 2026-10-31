#!/usr/bin/env python3
"""Explore the entire (4,4,6) free-Levi map for a certified large-row cone.

No old cone guide or certificate is read. Formal evaluations at r,s=0,1
extract coefficients of the EXACT affine local bracket; they are not
claimed as physical test Cartan matrices. If the leading map is singular,
record that obstruction, not a fallback theorem. If nonsingular, determinant
and cofactor bounds are exact Fraction/integer and give an explicit cone.
"""
import importlib.util
import json
import math
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def load(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/file);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
levi=load('levi','frontier-20261028-levi-lie-engine.py')
det=load('det','frontier-20261028-level5-type-determinant.py')
lift=levi.lift
DEGREE=(4,4,6)


def difference(a,b):
    result=dict(a)
    for k,c in b.items():result[k]=result.get(k,Q(0))-c
    return {k:c for k,c in result.items() if c}


def main():
    out=ROOT/'frontier-20261028-level6-446-leading-map-cone-v1.json'
    if out.exists():raise FileExistsError(out)
    source=levi.lie_basis(DEGREE)
    h=[]
    for _,v in source:
        c={}
        for i,g in enumerate(('f1','f2')):c.update({(i,w):q for w,q in levi.levi_action(v,g,0,0).items()})
        h.append(c)
    coeff=lift.kernel_with_coefficients(h)
    vec=[lift.combine([v for _,v in source],c) for c in coeff];k=len(vec)
    print('full source',len(source),'horizontal kernel',k,flush=True)
    E=[levi.lower3(v,0,0) for v in vec]
    L=[difference(levi.lower3(v,1,1),E[j]) for j,v in enumerate(vec)]
    K=[difference(levi.lower3(v,1,0),levi.lower3(v,0,1)) for v in vec]
    span=lift.Span()
    for col in L:span.add(col)
    result={'degree':DEGREE,'free_source_dim':len(source),'horizontal_kernel_dim':k,'leading_f3_rank':len(span),
            'source_words':[''.join(map(str,w)) for w,_ in source],
            'horizontal_kernel_coefficients':[{str(i):lift.rational_text(q) for i,q in sorted(c.items())} for c in coeff],
            'formal_parameters':'r=t+d,s=t-d; D=tL+dK+E extracted at formal r,s in {0,1}',
            'actual_region':'integer r,s>=6, entire Serre source and target have no node3 seed ideals',
            'not_formal_or_external_model_review':True}
    if len(span)<k:
        result['status']='LEADING_MAP_RANK_DEFECT_NO_CONE_PROOF'
    else:
        rows=sorted(span.rows);assert len(rows)==k
        LL=[[Q(L[j].get(row,0)) for j in range(k)] for row in rows]
        KK=[[Q(K[j].get(row,0)) for j in range(k)] for row in rows]
        EE=[[Q(E[j].get(row,0)) for j in range(k)] for row in rows]
        scales=[math.lcm(*(q.denominator for q in row)) for row in LL]
        integer=[[int(q*scales[i]) for q in row] for i,row in enumerate(LL)]
        DD=Q(det.bareiss(integer),math.prod(scales));assert DD
        M=max(abs(q) for row in LL for q in row)
        Km=max(abs(q) for row in KK for q in row)
        Em=max(abs(q) for row in EE for q in row)
        C=Q(k*k*math.factorial(k-1))*M**(k-1)/abs(DD)
        result.update({'status':'LEADING_INJECTIVE_COFAC_CONE',
                       'target_word_pivots':[''.join(map(str,w)) for w in rows],
                       'leading_determinant':str(DD),'leading_entry_abs_max':str(M),
                       'difference_entry_abs_max':str(Km),'constant_entry_abs_max':str(Em),
                       'cofactor_bound_C':str(C),
                       'criterion':'t > C*(abs(d)*Kmax+Emax), t=(r+s)/2, d=(r-s)/2',
                       'matrix_entries':[[[str(LL[i][j]),str(KK[i][j]),str(EE[i][j])] for j in range(k)] for i in range(k)]})
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('DONE',result['status'],'leading rank',len(span),'of',k,out.name,flush=True)

if __name__=='__main__':main()
